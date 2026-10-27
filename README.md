# AI Adoption

Plugins para empezar a usar la IA en tu día a día y tu trabajo, **con la herramienta que prefieras** (Claude, ChatGPT/Codex…).

## AI Onboarding
Te guía paso a paso: deja tu IA configurada (tus reglas, un proyecto y tus servicios conectados) y te enseña a automatizar una tarea que repites en tu trabajo. No necesitas conocimientos técnicos y nunca te pedirá contraseñas en el chat.

### Cómo empezar
Abre tu herramienta de IA y escribe:

> Lee https://github.com/Medu-coder/ai-adoption (empieza por su AGENTS.md) y ayúdame a configurarme.

El asistente te preguntará qué herramienta usas y te guiará para instalar AI Onboarding (en Claude con plan de pago y en la app de escritorio de ChatGPT/Codex). AI Onboarding necesita estar instalado: si tu herramienta no lo permite, el asistente te dirá qué opciones tienes.

Si prefieres instalarlo tú:
- **Claude** (plan de pago): Customize → Plugins → Add marketplace → `Medu-coder/ai-adoption` → instalar **AI Onboarding** → activar **Sync automatically** para recibir mejoras.
- **Claude Code:** `/plugin install ai-onboarding --marketplace Medu-coder/ai-adoption`
- **ChatGPT / Codex (app de escritorio):** menú **ChatGPT** → **Configuración** → **Complementos** → **Añadir** → **Añadir un marketplace** → `Medu-coder/ai-adoption`; después instala **AI Onboarding**. Para recibir mejoras: pestaña **Tienda** → **Actualizar**. También por terminal: `codex plugin marketplace add Medu-coder/ai-adoption`.

ChatGPT web permite instalar plugins del directorio, pero eso no añade automáticamente este marketplace de GitHub a una cuenta personal. En un workspace, su administrador puede importar el marketplace para el equipo. En el móvil se pueden usar los plugins ya disponibles en tu cuenta, pero este marketplace se añade desde la app de escritorio.

El repositorio mantiene un único AI Onboarding compartido: un manifiesto portable `plugins/ai-onboarding/plugin.json`, un marketplace nativo de OpenAI en `.agents/plugins/marketplace.json` y los manifiestos de compatibilidad de Claude. No hace falta duplicar sus instrucciones.

## Plugins disponibles
| Plugin | Para quién | Qué hace |
|---|---|---|
| `ai-onboarding` | Cualquiera | Configuración guiada y primera skill para usar la IA en el trabajo |

## Compatibilidad y pruebas

La instalación se probó con la versión 0.1.5 en Codex CLI, en perfiles temporales, tanto con el marketplace nativo de OpenAI como con el compatible con Claude. Consulta [el alcance, los límites y cómo repetir la prueba](docs/compatibilidad-openai.md). La interfaz de ChatGPT todavía no se ha probado de extremo a extremo.

Todo es público y genérico: aquí no hay datos de nadie, y el kit no recoge ni envía tus datos a ningún servidor propio. Tu herramienta de IA y los servicios que conectes tratan tus datos según sus propias condiciones.
