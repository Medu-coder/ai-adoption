# Rutas en cada herramienta

Dónde está cada cosa en los menús. **Revisado el 26/10/2026 (tarde); skills, plugins y uso del ordenador, el 26/10/2026 (noche); reglas básicas y guardado de skills, el 27/10/2026; app de escritorio de ChatGPT revisada en pantalla el 27/10/2026; requisito y subida de skills en Claude, permisos y activación del uso del ordenador en ChatGPT, el 28/10/2026** con la ayuda oficial de cada herramienta; donde algo no está confirmado, se indica. Las apps cambian a menudo: si lo que ve la persona no coincide, díselo y buscadlo a partir de lo más parecido.

## Claude (web y escritorio)
| Qué | Ruta | Notas |
|---|---|---|
| Reglas básicas | Iniciales (abajo a la izquierda) → **Settings / Configuración** → **Your Claude** → **Instructions for Claude** | En versiones anteriores: **Account** → **Instructions for Claude**. Se aplican a todas las conversaciones (web, escritorio y móvil). La ayuda oficial no publica límite de caracteres. En versiones anteriores de la app de escritorio, las sesiones de Cowork tenían además sus propias **Global instructions** (**Settings** → **Cowork** → **Edit**); en la versión actual forman parte de **Instructions for Claude**. |
| Proyecto | **Projects / Proyectos** → crear proyecto → nombre, instrucciones y archivos | Las instrucciones del proyecto solo se aplican dentro de él. |
| Carpeta del ordenador (solo app de escritorio) | Debajo del cuadro de texto de una conversación, opción para **añadir una carpeta**; después, permitir que Claude trabaje con sus archivos. | Incluido en los planes de pago. Permite leer y editar archivos de esa carpeta. Es distinto de las extensiones de escritorio (**Settings** → **Desktop app** → **Extensions**). El nombre exacto del botón no está en la ayuda oficial. |
| Conectores | En la barra lateral, **Customize** → **Connectors**. Desde un chat: botón **+** → **Connectors** → **Manage connectors** → **+**. Elegir el servicio → **Connect** e iniciar sesión. | Los conectores web están disponibles en todos los planes, también el gratuito. En el móvil se pueden instalar (en beta); lo conectado en web o escritorio también funciona en el móvil. En cuentas de empresa, el administrador puede tener que habilitarlos. |
| Requisito para skills | Planes individuales (Free, Pro, Max): **Settings / Configuración** → **Capabilities** → activar **Create and edit files** (en versiones anteriores, **Code execution and file creation**). Team y Enterprise: lo activa el propietario en **Organization settings** → **Plugins & skills**. | Sin esto, las skills no funcionan (aparecen en gris). Disponible en todos los planes. |
| Creador de skills | En la barra lateral, **Customize / Personalización** → **Skills** → activar **skill-creator**. Después, pedir en el chat crear una skill para la tarea. | Viene incluido; solo hay que activarlo. |
| Guardar y activar una skill | Si la crea skill-creator: guardar el archivo de skill que entrega Claude al terminar, con la opción que ofrezca. Para subir una skill preparada: **Customize / Personalización** → **Skills** → **+** → **+ Create skill** → **Upload a skill** → elegir el archivo ZIP. Aparece en la lista con un interruptor para activarla o desactivarla. | El ZIP lleva una carpeta con el nombre de la skill y su `SKILL.md` dentro; errores habituales: el nombre de la carpeta no coincide con el de la skill o falta el `SKILL.md`. El botón exacto con que skill-creator ofrece guardarla no está en la ayuda oficial. Escribir un fichero en un ordenador no la añade a esta lista. En Claude Code, las skills personales van en la carpeta `.claude/skills` de su carpeta personal. |
| Plugins oficiales | **Customize** → **Plugins**. Catálogo oficial de Anthropic: https://claude.com/plugins | El marketplace oficial (`claude-plugins-official`) lo cura Anthropic. |
| Creador de skills en Claude Code | `/plugin install skill-creator@claude-plugins-official` | Del marketplace oficial de Anthropic, que Claude Code ya trae añadido. |
| Uso del ordenador | App de escritorio (Mac o Windows), actualizada: **Settings / Configuración** → apartado **Desktop app** → activar **Computer use**. En Mac, aceptar los permisos de grabación de pantalla y accesibilidad. | Pro y Max, en vista previa. En la misma pantalla se pueden añadir apps bloqueadas. Claude pide permiso antes de usar cada app. El ordenador debe estar encendido y la app abierta. |

## ChatGPT
La app de escritorio (Mac) se revisó en pantalla el 27/10/2026, con la interfaz en español; entre paréntesis, el nombre en inglés cuando se conoce.

| Qué | Ruta | Notas |
|---|---|---|
| Reglas básicas (cuenta) | **Web**: **Configuración** → **Personalización** → activar **Habilitar personalización** → **Instrucciones personalizadas** y, debajo, **Sobre ti** (**Apodo**, **Ocupación** y **Más sobre ti**). Móvil: **Configuración** → **Personalizar ChatGPT**. | Se aplican al chat en la web, el móvil y el modo **Chat** de la app de escritorio. La app de escritorio no tiene estos campos: se editan en la web. Límites: 1.500 caracteres en Free/Go y 5.000 en Plus/Pro/Business/Enterprise/Education (la ayuda no aclara si **Más sobre ti** cuenta aparte). |
| Reglas básicas (app de escritorio, modos **Work** y **Codex**) | Menú **ChatGPT** → **Configuración** (⌘,) → **Personalización** → **Instrucciones personalizadas** → **Instrucciones de Codex**. | La propia pantalla dice que edita el fichero `AGENTS.md` del ordenador (carpeta `.codex` de su carpeta personal). No usa las instrucciones de la cuenta ni se copia a otros ordenadores: hay que guardar las reglas en los dos sitios. |
| Permisos de la conversación | Debajo del cuadro de texto, el selector de permisos, con tres opciones: **Solicitar aprobación** (pide confirmación antes de editar archivos externos y usar internet), **Aprobar automáticamente** (solo pide aprobación para acciones potencialmente inseguras) y **Acceso completo** (sin restricciones a internet ni a los archivos del ordenador). | Para que AI Onboarding guarde las reglas o una tarea en el ordenador, normalmente basta con aprobar la petición cuando aparezca. **Acceso completo** quita todas las restricciones: no es la solución general; solo si es la única forma, explicado y volviendo después al modo anterior. Se habilita en **Configuración** → **General** → **Permisos**. El uso del ordenador, el acceso a apps y estos permisos son cosas distintas. |
| Proyecto | **Nuevo proyecto** (barra lateral) → nombre. Instrucciones: abrir el proyecto → menú **•••** → **Configuración del proyecto**. Archivos: añadirlos como fuentes del proyecto. | Dentro del proyecto, sus instrucciones **prevalecen** sobre las personalizadas. Límite de archivos según plan (5 en gratuito, 25 en Plus). |
| Conectores | Web: **Configuración** → **Plugins** → elegir el servicio → **Conectar** e iniciar sesión. App de escritorio: **Configuración** → **Complementos** (Plugins) → pestaña **Aplicaciones**, o **Explorar directorio**. | La disponibilidad depende del servicio, el plan, la región y la cuenta; en cuentas de empresa, el administrador decide cuáles hay. |
| Complementos (plugins) | App de escritorio: **Configuración** → **Complementos**, con pestañas **Complementos**, **Aplicaciones**, **MCP**, **Habilidades** (skills) y **Tienda** (marketplaces), más **Explorar directorio** y el menú **Añadir** (**Crear complemento**, **Añadir un marketplace**, **Añadir servidor MCP**, **Grabar una habilidad**). Web y móvil: **Plugins** en la barra lateral. | En **Tienda**, cada marketplace tiene **Actualizar**. Algunos plugins llevan la insignia **OpenAI Verified**. |
| Creador de skills | Solo en la app de escritorio, en **Work**: escribir `@skill-creator` en el chat. | En la web y el móvil no se pueden crear ni usar skills sueltas; solo las que vienen dentro de un plugin instalado. |
| Ver sus skills | App de escritorio: **Configuración** → **Complementos** → pestaña **Habilidades** (aparecen como **Personales**). | Ahí se activan y desactivan. |
| Guardar una skill | La guarda `@skill-creator` al terminar. Si la guarda AI Onboarding, en la carpeta `.agents/skills` de su carpeta personal. | La app muestra como **Personales** las de `.agents/skills` y las de `.codex/skills`; AI Onboarding usa `.agents/skills`, la que indica la documentación oficial. |
| Grabar una skill (Record & Replay) | Solo app de escritorio en Mac: **Configuración** → **Complementos** → **Añadir** → **Grabar una habilidad** → revisar el texto propuesto y enviarlo → aceptar el permiso → hacer la tarea → parar la grabación. | Necesita el uso del ordenador activado. En cuentas de empresa puede estar desactivado. |
| Uso del ordenador | App de escritorio (Mac o Windows), en **Work** o **Codex**. Desde cero: 1) **Complementos** (Plugins) → **Computer Use** → **Instalar complemento** o **Activar** si lo pide → activar los interruptores del servidor y de la habilidad (skill). 2) En Mac, **Ajustes del Sistema** → **Privacidad y seguridad**: permitir **Grabación de pantalla** y **Accesibilidad** para **Codex Computer Use**. 3) **Configuración** → **Uso del ordenador** → en **Control**, **Cualquier aplicación** (Any App). | La pantalla **Uso del ordenador** se revisó en pantalla el 27/10; la instalación del complemento sale de la ayuda oficial (28/10), sin revisar en pantalla en español. En la misma pantalla: la extensión de Google Chrome, el complemento de Microsoft Excel, **Uso bloqueado** y **Aplicaciones siempre permitidas**. Pide permiso antes de usar cada app (**Permitir siempre** evita repetirlo). Leer o editar ficheros y ejecutar órdenes siguen los permisos de la conversación. En cuentas de empresa el administrador puede desactivarlo. En Windows trabaja en primer plano. |

## Codex (app, CLI y extensión del IDE)
| Qué | Ruta | Notas |
|---|---|---|
| Reglas básicas | App: igual que la fila de la app de escritorio de ChatGPT (**Instrucciones de Codex**). CLI y extensión: el fichero `AGENTS.md` de la carpeta `.codex` de su carpeta personal. | Si existe `AGENTS.override.md` en esa carpeta, se lee ese en su lugar. Codex deja de leer instrucciones cuando el total (globales y de cada carpeta) llega a 32 KiB por defecto (es configurable). |
| Permisos para guardar | App: el selector de permisos de la conversación (ver ChatGPT). CLI: `/permissions`. | En el modo habitual, Codex pide aprobación para escribir fuera de la carpeta de trabajo, por ejemplo en `.codex`: basta con aprobar esa petición. |
| Creador de skills | Escribir `$skill-creator` en el chat. | Viene incluido con Codex. |
| Guardar una skill | Carpeta `.agents/skills` de su carpeta personal (una carpeta por skill con su `SKILL.md`). | Codex detecta los cambios solo; si no aparece, reiniciar Codex. |
| Plugins oficiales | App: **Configuración** → **Complementos** → **Explorar directorio**. CLI: `/plugins`. | |
| Uso del ordenador | Igual que en la app de escritorio de ChatGPT. | No disponible en la CLI. |

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
- Repositorios oficiales de plugins y skills: https://github.com/anthropics/knowledge-work-plugins, https://github.com/anthropics/claude-plugins-official, https://github.com/anthropics/skills y https://github.com/openai/plugins (`openai/skills` está retirado y remite a `openai/plugins`)
