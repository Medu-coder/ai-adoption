# AI Adoption

Plugins para empezar a usar la IA en tu día a día y tu trabajo, **con la herramienta que prefieras** (Claude, ChatGPT/Codex…).

## Coach IA
Te guía paso a paso: deja tu IA configurada (tus reglas, un proyecto y tus servicios conectados) y te ayuda a ponerla en práctica. No necesitas conocimientos técnicos y nunca te pedirá contraseñas en el chat.

### Cómo empezar
Abre tu herramienta de IA y escribe:

> Lee https://github.com/Medu-coder/ai-adoption (empieza por su AGENTS.md) y ayúdame a configurarme.

El asistente te preguntará qué herramienta usas y, si se puede, te propondrá instalar el Coach IA para tenerlo siempre a mano (en Claude con plan de pago y en la app de escritorio de ChatGPT/Codex). Si no puedes añadir este marketplace en tu entorno, te guiará directamente en esa conversación.

Si prefieres instalarlo tú:
- **Claude** (plan de pago): Customize → Plugins → Add marketplace → `Medu-coder/ai-adoption` → instalar **Coach IA** → activar **Sync automatically** para recibir mejoras.
- **Claude Code:** `/plugin install coach-ia --marketplace Medu-coder/ai-adoption`
- **ChatGPT / Codex (app de escritorio):** ejecuta en la terminal de tu ordenador `codex plugin marketplace add Medu-coder/ai-adoption` (o pide al asistente de la app que lo haga), reinicia la app e instala **Coach IA** desde el directorio de plugins. Para recibir mejoras: `codex plugin marketplace upgrade`.

ChatGPT web permite instalar plugins del directorio, pero eso no añade automáticamente este marketplace de GitHub a una cuenta personal. En un workspace, su administrador puede importar el marketplace para el equipo. Los plugins no están disponibles en móvil. Si no tienes una vía de instalación compatible, puedes seguir usando el Coach en la conversación con el mensaje anterior.

El repositorio mantiene un único Coach compartido: un manifiesto portable `plugins/coach-ia/plugin.json`, un marketplace nativo de OpenAI en `.agents/plugins/marketplace.json` y los manifiestos de compatibilidad de Claude. No hace falta duplicar sus instrucciones.

## Plugins disponibles
| Plugin | Para quién | Qué hace |
|---|---|---|
| `coach-ia` | Cualquiera | Configuración guiada y acompañamiento para usar la IA en el trabajo |

## Compatibilidad y pruebas

La versión 0.1.5 se ha probado con Codex CLI en perfiles temporales, tanto con el marketplace nativo de OpenAI como con el compatible con Claude. Consulta [el alcance, los límites y cómo repetir la prueba](docs/compatibilidad-openai.md). La interfaz de ChatGPT todavía no se ha probado de extremo a extremo.

Todo es público y genérico: aquí no hay datos de nadie, y el kit no recoge ni envía tus datos a ningún servidor propio. Tu herramienta de IA y los servicios que conectes tratan tus datos según sus propias condiciones.
