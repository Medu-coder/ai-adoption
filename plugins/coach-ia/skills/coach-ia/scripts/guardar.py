#!/usr/bin/env python3
"""Guarda un texto en el ordenador de la persona de forma segura.

Lee el contenido por la entrada estándar, guarda una copia de lo que hubiera,
escribe, vuelve a leer y comprueba. Responde con una línea JSON:
  {"estado": "ok" | "sin_permiso" | "error", "ruta": ..., "copia": ..., "detalle": ...}

Destinos:
  reglas-codex        Instrucciones globales de Codex y de la app de escritorio de
                      ChatGPT (AGENTS.override.md si existe; si no, AGENTS.md).
  reglas-claude-code  Instrucciones globales de Claude Code (CLAUDE.md).
  tarea-codex         Una skill para Codex / ChatGPT escritorio (requiere --nombre).
  tarea-claude-code   Una skill para Claude Code (requiere --nombre).
  fichero             Cualquier fichero de su carpeta de trabajo (requiere --ruta).

Ejemplo:
  python3 guardar.py --destino reglas-codex <<'FIN'
  ...texto aprobado...
  FIN
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def destino(args):
    home = Path.home()
    if args.destino == "reglas-codex":
        base = Path(os.environ.get("CODEX_HOME") or home / ".codex").expanduser()
        override = base / "AGENTS.override.md"
        return (override if override.exists() else base / "AGENTS.md"), override.exists()
    if args.destino == "reglas-claude-code":
        base = Path(os.environ.get("CLAUDE_CONFIG_DIR") or home / ".claude").expanduser()
        return base / "CLAUDE.md", False
    if args.destino in ("tarea-codex", "tarea-claude-code"):
        if not args.nombre or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.nombre):
            raise ValueError("--nombre obligatorio, en minúsculas y con guiones (p. ej. preparar-acta)")
        base = home / ".agents" / "skills" if args.destino == "tarea-codex" else home / ".claude" / "skills"
        return base / args.nombre / "SKILL.md", False
    if args.destino == "fichero":
        if not args.ruta:
            raise ValueError("--ruta obligatoria con el destino fichero")
        return Path(args.ruta).expanduser().resolve(), False
    raise ValueError("destino desconocido")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--destino", required=True,
                   choices=["reglas-codex", "reglas-claude-code", "tarea-codex", "tarea-claude-code", "fichero"])
    p.add_argument("--nombre")
    p.add_argument("--ruta")
    args = p.parse_args()
    resultado = {"estado": "error", "ruta": None, "copia": None, "detalle": ""}
    try:
        texto = sys.stdin.read()
        if not texto.strip():
            raise ValueError("no llegó ningún texto por la entrada estándar")
        if not texto.endswith("\n"):
            texto += "\n"
        ruta, es_override = destino(args)
        resultado["ruta"] = str(ruta)
        if es_override:
            resultado["detalle"] = "existía AGENTS.override.md: se ha actualizado ese fichero. "
        ruta.parent.mkdir(parents=True, exist_ok=True)
        if ruta.exists():
            anterior = ruta.read_text(encoding="utf-8")
            if anterior == texto:
                resultado.update(estado="ok", detalle=resultado["detalle"] + "ya tenía exactamente este texto")
                print(json.dumps(resultado, ensure_ascii=False))
                return 0
            copia = ruta.with_name(ruta.name + ".antes-" + datetime.now().strftime("%Y%m%d-%H%M%S"))
            copia.write_text(anterior, encoding="utf-8")
            resultado["copia"] = str(copia)
        temporal = ruta.with_name("." + ruta.name + ".tmp")
        temporal.write_text(texto, encoding="utf-8")
        os.replace(temporal, ruta)
        if ruta.read_text(encoding="utf-8") != texto:
            raise IOError("al releer, el contenido no coincide")
        resultado.update(estado="ok", detalle=resultado["detalle"] + "guardado y comprobado")
        print(json.dumps(resultado, ensure_ascii=False))
        return 0
    except PermissionError as e:
        resultado.update(estado="sin_permiso", detalle=str(e))
    except OSError as e:
        if getattr(e, "errno", None) in (1, 13, 30):  # EPERM, EACCES, EROFS
            resultado.update(estado="sin_permiso", detalle=str(e))
        else:
            resultado["detalle"] = str(e)
    except Exception as e:  # noqa: BLE001
        resultado["detalle"] = str(e)
    print(json.dumps(resultado, ensure_ascii=False))
    return 2 if resultado["estado"] == "sin_permiso" else 1


if __name__ == "__main__":
    sys.exit(main())
