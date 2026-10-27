#!/usr/bin/env python3
"""Exercise local plugin installation without changing the user's Codex profile.

Requires Python 3.11+, Ruby (for safe YAML parsing), and Codex CLI.
No login, model request, connector, Git fetch, or real account installation.
"""

import hashlib
import json
import os
from pathlib import Path
import queue
import re
import shutil
import subprocess
import tempfile
import threading
import time
import tomllib


REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins/ai-onboarding"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def user_configuration():
    # Fingerprint configuration and plugin/skill files, never copy credentials.
    roots = [Path.home() / ".codex", Path.home() / ".agents"]
    if os.environ.get("CODEX_HOME"):
        roots.append(Path(os.environ["CODEX_HOME"]))
    files = set()
    for root in roots:
        files.update(p for p in [root / "config.toml", root / "AGENTS.md",
                                root / "AGENTS.override.md"] if p.is_file())
        for folder in [root / "plugins", root / "skills"]:
            if folder.is_dir():
                files.update(p for p in folder.rglob("*") if p.is_file())
    return {str(p): digest(p) for p in files}


def command(args, env, cwd):
    result = subprocess.run(args, env=env, cwd=cwd, capture_output=True,
                            text=True, timeout=30, check=True)
    return result.stdout


def discovered_skills(env, cwd):
    proc = subprocess.Popen(["codex", "app-server", "--stdio"], env=env,
                            cwd=cwd, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            text=True)
    messages = queue.Queue()

    def read():
        for line in proc.stdout:
            messages.put(json.loads(line))

    threading.Thread(target=read, daemon=True).start()

    def request(identifier, method, params):
        proc.stdin.write(json.dumps({"id": identifier, "method": method,
                                     "params": params}) + "\n")
        proc.stdin.flush()
        end = time.monotonic() + 20
        while time.monotonic() < end:
            message = messages.get(timeout=max(.01, end - time.monotonic()))
            if message.get("id") == identifier:
                assert "error" not in message, message
                return message["result"]
        raise TimeoutError(method)

    try:
        initialized = request(1, "initialize", {
            "clientInfo": {"name": "ai-onboarding-isolated-check", "version": "0.1.0"},
            "capabilities": {"experimentalApi": True}})
        assert Path(initialized["codexHome"]).resolve() == Path(env["CODEX_HOME"]).resolve()
        proc.stdin.write('{"method":"initialized"}\n')
        proc.stdin.flush()
        return request(2, "skills/list", {"cwds": [str(cwd)], "forceReload": True})
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def main():
    before = user_configuration()
    try:
        manifest = json.loads((PLUGIN / "plugin.json").read_text())
        claude = json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())
        assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
        assert manifest["name"] == claude["name"] == "ai-onboarding"
        assert manifest["version"] == claude["version"]
        assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])
        interface = manifest["extensions"]["com.openai"]["interface"]
        assert 0 < len(interface["shortDescription"]) <= 30
        assert all(isinstance(v, str) and v.strip() for v in interface.values())
        for skill in PLUGIN.glob("skills/*/SKILL.md"):
            text = skill.read_text()
            assert text.startswith("---\n")
            frontmatter = text.split("---", 2)[1]
            parsed = json.loads(subprocess.run(
                ["ruby", "-ryaml", "-rjson", "-e",
                 "puts JSON.generate(YAML.safe_load(STDIN.read))"],
                input=frontmatter, text=True, capture_output=True, check=True).stdout)
            assert parsed["name"] == skill.parent.name
            assert isinstance(parsed["description"], str) and parsed["description"].strip()
        for file in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (file.parent / target.split("#")[0]).resolve()
                assert resolved.is_relative_to(PLUGIN.resolve()) and resolved.exists(), (file, target)
        print("PASS: manifests, YAML frontmatter and contained reference links")

        # Both native and Claude-only marketplace discovery are exercised.
        with tempfile.TemporaryDirectory(prefix="ai-onboarding-isolated-") as directory:
            root = Path(directory).resolve()
            for catalog in ["native", "claude-compatible"]:
                case = root / catalog
                source, profile, work = case / "source", case / "codex", case / "work"
                source.mkdir(parents=True)
                profile.mkdir()
                work.mkdir()
                shutil.copytree(PLUGIN, source / "plugins/ai-onboarding")
                catalog_path = ".agents/plugins" if catalog == "native" else ".claude-plugin"
                (source / catalog_path).mkdir(parents=True)
                shutil.copy2(REPO / catalog_path / "marketplace.json", source / catalog_path)
                # Only this process receives a temporary Codex profile. HOME is unchanged.
                # User skills may be discovered read-only by app-server; none are executed.
                env = {"PATH": os.environ["PATH"], "HOME": str(Path.home()),
                       "TMPDIR": str(root), "CODEX_HOME": str(profile),
                       "LANG": "en_US.UTF-8"}
                empty = json.loads(command(["codex", "plugin", "list", "--available", "--json"], env, work))
                assert empty == {"installed": [], "available": []}, empty
                command(["codex", "plugin", "marketplace", "add", str(source)], env, work)
                available = json.loads(command(["codex", "plugin", "list", "--available", "--json"], env, work))
                assert len(available["available"]) == 1
                assert available["available"][0]["version"] == manifest["version"]
                command(["codex", "plugin", "add", "ai-onboarding@ai-adoption"], env, work)
                installed = json.loads(command(["codex", "plugin", "list", "--json"], env, work))["installed"]
                assert len(installed) == 1 and installed[0]["enabled"]
                cached = profile / "plugins/cache/ai-adoption/ai-onboarding" / manifest["version"]
                for file in PLUGIN.rglob("*"):
                    if file.is_file():
                        assert digest(file) == digest(cached / file.relative_to(PLUGIN))
                loaded = discovered_skills(env, work)
                matches = [s for entry in loaded["data"] for s in entry["skills"]
                           if s["name"] == "ai-onboarding:ai-onboarding"]
                assert len(matches) == 1 and matches[0]["enabled"]
                assert Path(matches[0]["path"]).resolve().is_relative_to(cached)
                errors = [e for entry in loaded["data"] for e in entry["errors"]
                          if Path(e["path"]).resolve().is_relative_to(cached)]
                assert not errors, errors
                configuration = tomllib.loads((profile / "config.toml").read_text())
                assert not configuration.get("mcp_servers")
                assert not (profile / "auth.json").exists()
                print(f"PASS: {catalog}: discover, install, enable, intact cache and engine skill discovery")
        print("PASS: temporary profiles removed; no login, model call or connector used")
    finally:
        assert user_configuration() == before, "User configuration or plugin/skill files changed"
        print("PASS: user's configuration and plugin/skill files unchanged")


if __name__ == "__main__":
    main()
