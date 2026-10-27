# Rutas en cada herramienta

Dónde está cada cosa en los menús. **Revisado el 26/10/2026 (tarde); skills, plugins y uso del ordenador, el 26/10/2026 (noche); reglas básicas y guardado de skills, el 27/10/2026** con la ayuda oficial de cada herramienta; donde algo no está confirmado, se indica. Las apps cambian a menudo: si lo que ve la persona no coincide, díselo y buscadlo a partir de lo más parecido.

## Claude (web y escritorio)
| Qué | Ruta | Notas |
|---|---|---|
| Reglas básicas | Iniciales (abajo a la izquierda) → **Settings / Configuración** → **Your Claude** → **Instructions for Claude** | En versiones anteriores: **Account** → **Instructions for Claude**. Se aplican a todas las conversaciones (web, escritorio y móvil). La ayuda oficial no publica límite de caracteres. En versiones anteriores de la app de escritorio, las sesiones de Cowork tenían además sus propias **Global instructions** (**Settings** → **Cowork** → **Edit**); en la versión actual forman parte de **Instructions for Claude**. |
| Proyecto | **Projects / Proyectos** → crear proyecto → nombre, instrucciones y archivos | Las instrucciones del proyecto solo se aplican dentro de él. |
| Carpeta del ordenador (solo app de escritorio) | Debajo del cuadro de texto de una conversación, opción para **añadir una carpeta**; después, permitir que Claude trabaje con sus archivos. | Incluido en los planes de pago. Permite leer y editar archivos de esa carpeta. Es distinto de las extensiones de escritorio (**Settings** → **Desktop app** → **Extensions**). El nombre exacto del botón no está en la ayuda oficial. |
| Conectores | En la barra lateral, **Customize** → **Connectors**. Desde un chat: botón **+** → **Connectors** → **Manage connectors** → **+**. Elegir el servicio → **Connect** e iniciar sesión. | Los conectores web están disponibles en todos los planes, también el gratuito. En el móvil se pueden instalar (en beta); lo conectado en web o escritorio también funciona en el móvil. En cuentas de empresa, el administrador puede tener que habilitarlos. |
| Requisito para skills | Planes individuales (Free, Pro, Max): **Settings / Configuración** → **Capabilities** → activar **Code execution and file creation**. Team y Enterprise: lo activa el propietario en **Organization settings** → **Skills**. | Sin la ejecución de código, las skills no funcionan (aparecen en gris). Disponible en todos los planes. |
| Creador de skills | En la barra lateral, **Customize / Personalización** → **Skills** → activar **skill-creator**. Después, pedir en el chat crear una skill para la tarea. | Viene incluido; solo hay que activarlo. |
| Guardar y activar una skill | Guardar el archivo de skill que genera Claude. En **Customize / Personalización** → **Skills** se ve la biblioteca y se activa o desactiva cada skill. | En Claude Code, las skills personales van en la carpeta `.claude/skills` de su carpeta personal. |
| Plugins oficiales | **Customize** → **Plugins**. Catálogo oficial de Anthropic: https://claude.com/plugins | El marketplace oficial (`claude-plugins-official`) lo cura Anthropic. |
| Creador de skills en Claude Code | `/plugin install skill-creator@claude-plugins-official` | Del marketplace oficial de Anthropic, que Claude Code ya trae añadido. |
| Uso del ordenador | App de escritorio (Mac o Windows), actualizada: **Settings / Configuración** → apartado **Desktop app** → activar **Computer use**. En Mac, aceptar los permisos de grabación de pantalla y accesibilidad. | Pro y Max, en vista previa. En la misma pantalla se pueden añadir apps bloqueadas. Claude pide permiso antes de usar cada app. El ordenador debe estar encendido y la app abierta. |

## ChatGPT
| Qué | Ruta | Notas |
|---|---|---|
| Reglas básicas | Web: **Configuración** → **Personalización** → activar **Habilitar personalización** → **Instrucciones personalizadas** y, debajo, **Sobre ti** (**Apodo**, **Ocupación** y **Más sobre ti**). Móvil: **Configuración** → **Personalizar ChatGPT**. App de escritorio: ver la fila siguiente. | Los cambios se aplican inmediatamente a todos los chats, también los existentes. Límites de las instrucciones personalizadas: 1.500 caracteres en Free/Go y 5.000 en Plus/Pro/Business/Enterprise/Education (la ayuda no aclara si **Más sobre ti** cuenta aparte). Si la interfaz muestra otro límite, respétalo. |
| Reglas básicas en la app de escritorio | Modo **Chat**: usa las de la cuenta (fila anterior; se editan en la web). Modos **Work** y **Codex**: **Configuración** → **Personalización** → **Instrucciones personalizadas** de la app, que es el fichero `AGENTS.md` de la carpeta `.codex` de su carpeta personal. | Work y Codex no usan las instrucciones de la cuenta, y las de la app no se sincronizan con otros ordenadores: hay que guardarlas en los dos sitios. Lo de Codex está en su documentación oficial; el reparto entre modos, en pruebas de usuarios y avisos del repositorio oficial de Codex, no en la ayuda de ChatGPT. |
| Proyecto | **Nuevo proyecto** (barra lateral) → nombre. Instrucciones: abrir el proyecto → menú **•••** → **Configuración del proyecto**. Archivos: añadirlos como fuentes del proyecto. | Dentro del proyecto, sus instrucciones **prevalecen** sobre las personalizadas. Límite de archivos según plan (5 en gratuito, 25 en Plus). |
| Conectores | **Configuración** → **Plugins** → elegir el servicio (o el plugin que lo incluye) → **Instalar plugin** si aparece → **Conectar** e iniciar sesión. En versiones antiguas del móvil se llama **Apps**. | La disponibilidad depende del servicio, el plan, la región y la cuenta; en cuentas de empresa, el administrador decide cuáles hay. |
| Creador de skills | Solo en la app de escritorio, en **Work**: escribir `@skill-creator` en el chat. | En la web y el móvil no se pueden crear ni usar skills sueltas; solo las que vienen dentro de un plugin instalado. |
| Ver sus skills | App de escritorio: **Skills** en la barra lateral. | |
| Guardar una skill | La guarda `@skill-creator` al terminar. Si la guarda el Coach, en la carpeta `.agents/skills` de su carpeta personal, la misma que usa Codex. | Pendiente de verificar en Work con una prueba real. |
| Grabar una skill (Record & Replay) | Solo app de escritorio en Mac: activar **Work** (o elegir Codex) → **Plugins** → menú **+** → **Record a skill** → revisar el texto propuesto y enviarlo → aceptar el permiso → hacer la tarea → parar la grabación. | Necesita Computer Use activado. En cuentas de empresa puede estar desactivado. |
| Plugins oficiales | **Plugins** en la barra lateral (web, escritorio o móvil), o **Configuración** → **Plugins**. | Algunos llevan la insignia **OpenAI Verified** (revisados por OpenAI). |
| Uso del ordenador | App de escritorio (Mac o Windows): activar **Work** (o elegir Codex) → **Plugins** → **Computer Use** → **Install plugin** (o **Enable**) → activar sus interruptores → **Try now**. En Mac, aceptar los permisos de grabación de pantalla y accesibilidad. | Las apps permitidas se revisan en **Settings** → **Computer use**. Pide permiso antes de usar cada app. En Windows trabaja en primer plano. |

## Codex (app, CLI y extensión del IDE)
| Qué | Ruta | Notas |
|---|---|---|
| Reglas básicas | App: **Settings** → **Personalization** → **Custom instructions** (edita el fichero de abajo). CLI y extensión: el fichero `AGENTS.md` de la carpeta `.codex` de su carpeta personal. | Si existe `AGENTS.override.md` en esa carpeta, se lee ese en su lugar. Codex deja de leer instrucciones cuando el total (globales y de cada carpeta) llega a 32 KiB por defecto (es configurable). |
| Permisos para guardar | En el modo habitual (**Auto**), Codex pide aprobación para escribir fuera de la carpeta de trabajo, por ejemplo en la carpeta `.codex`. Si la petición no aparece, dar a la conversación acceso completo (**Full access**) en el selector de permisos. | En la terminal, `/permissions`. El nombre exacto del selector en la app de escritorio está pendiente de verificar. |
| Creador de skills | Escribir `$skill-creator` en el chat. | Viene incluido con Codex. |
| Guardar una skill | Carpeta `.agents/skills` de su carpeta personal (una carpeta por skill con su `SKILL.md`). No es `.codex/skills`. | Codex detecta los cambios solo; si no aparece, reiniciar Codex. |
| Plugins oficiales | App: **Plugins** (apartado de curados por OpenAI). CLI: `/plugins`. | |
| Uso del ordenador | Igual que en la app de escritorio de ChatGPT (plugin **Computer Use**). | No disponible en la CLI. |

## Otras herramientas (Gemini, Copilot…)
Sin rutas revisadas todavía. Usa la ayuda oficial de la herramienta si puedes consultarla; si no, describe la ruta de forma aproximada y dilo.

## Fuentes
- Claude, personalización: https://support.claude.com/en/articles/10185728
- Claude, conectores: https://support.claude.com/en/articles/11176164
- Claude, carpetas en la app de escritorio: https://academy.claude.com/tutorials/navigating-the-claude-desktop-app
- ChatGPT, instrucciones personalizadas: https://help.openai.com/en/articles/8096356
- ChatGPT, proyectos: https://help.openai.com/en/articles/10169521
- ChatGPT, apps conectadas: https://help.openai.com/en/articles/11487775
- Claude, uso del ordenador: https://support.claude.com/en/articles/14128542
- ChatGPT y Codex, uso del ordenador: https://learn.chatgpt.com/docs/computer-use
- Claude, usar skills (planes y requisitos): https://support.claude.com/en/articles/12512180
- Claude, crear una skill conversando: https://academy.claude.com/tutorials/how-to-create-a-skill-with-claude-through-conversation
- Claude, buenas prácticas para escribir skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Claude, marketplaces oficiales de plugins: https://code.claude.com/docs/en/discover-plugins
- ChatGPT y Codex, crear skills (incluye buenas prácticas): https://learn.chatgpt.com/docs/build-skills
- ChatGPT y Codex, Record & Replay: https://learn.chatgpt.com/docs/extend/record-and-replay
- ChatGPT, plugins: https://help.openai.com/en/articles/20001256
- Codex, plugins: https://developers.openai.com/codex/plugins
- Codex, instrucciones con AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- Codex, ajustes de la app (personalización): https://developers.openai.com/codex/app/settings
- Claude, instrucciones globales de Cowork: https://support.claude.com/en/articles/13345190
- ChatGPT, instrucciones del escritorio frente a las de la cuenta (aviso de usuarios): https://github.com/openai/codex/issues/33792
