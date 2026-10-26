# Instrucciones para el asistente de IA

Una persona te ha pedido que la ayudes a configurarse con este repositorio. Tu tarea es ayudarla a **instalar el Coach IA**, un plugin que la guía paso a paso para empezar a usar la IA en su día a día y su trabajo. El Coach solo funciona instalado: no hagas tú de Coach ni improvises sus pasos. No necesita saber nada técnico. Nunca le pidas contraseñas ni claves en el chat.

## 1. Pregunta qué herramienta usa
Si aún no lo sabes, pregunta, en un solo mensaje, qué herramienta de IA usa, dónde (web, app de escritorio o móvil) y con qué plan. Pregunta solo los datos que falten. Recuerda la respuesta: el Coach no volverá a preguntarlo.

## 2. Guíala para instalar el Coach IA
Explícale en una frase que, instalado, lo tendrá siempre a mano y recibirá las mejoras. Guíala con la opción de su herramienta. Si no cumple los requisitos, pasa al punto 3:

| Su herramienta | Cómo instalarlo |
|---|---|
| Claude (app de escritorio o web) — requiere plan de pago | En la barra lateral, **Customize** → **Plugins** → **Add marketplace** → escribir `Medu-coder/ai-adoption` → instalar **Coach IA** → activar **Sync automatically** (así recibe las mejoras solo). |
| Claude Code (versión 2.1.275 o posterior) | `/plugin install coach-ia --marketplace Medu-coder/ai-adoption` |
| ChatGPT / Codex en la **app de escritorio**, con el comando `codex` disponible | Si puedes ejecutar comandos, enséñale este y ejecútalo cuando lo confirme: `codex plugin marketplace add Medu-coder/ai-adoption`. Si no puedes, dáselo para que lo ejecute ella en la terminal de su ordenador. Después, reiniciar la app e instalar **Coach IA** desde el directorio de plugins. Para recibir mejoras más adelante: `codex plugin marketplace upgrade`. |
| ChatGPT en la **web** | Puede instalar plugins del directorio, pero eso no añade este marketplace de GitHub a una cuenta personal. Si su empresa gestiona plugins, su administrador puede importar el marketplace para el equipo. Si no tiene esa vía, pasa al punto 3. |
| ChatGPT en el **móvil**, u otra herramienta sin instalación compatible | Los plugins de ChatGPT no están disponibles en móvil. Para otras herramientas, comprueba sus capacidades. Si no puede instalarlo, pasa al punto 3. |

Si lo instala, pídele que abra una conversación nueva y escriba "Quiero empezar con el Coach IA".

## 3. Si no se puede instalar
No hagas de Coach en esta conversación. Explícale en dos o tres líneas por qué no se puede en su caso y qué opciones tendría para usarlo (por ejemplo, Claude con plan de pago en la web o el escritorio, Claude Code, o la app de escritorio de ChatGPT/Codex). Si alguna le encaja, guíala con ella; si no, despídete. No modifiques este repositorio.
