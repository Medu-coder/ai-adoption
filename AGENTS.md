# Instrucciones para el asistente de IA

Una persona te ha pedido que le ayudes a configurarse con este repositorio. Tu tarea es ayudarle a **instalar AI Onboarding**, un plugin que le guía paso a paso para empezar a usar la IA en su día a día y su trabajo. AI Onboarding solo funciona instalado: no lo sustituyas tú ni improvises sus pasos. No necesita saber nada técnico. Nunca le pidas contraseñas ni claves en el chat.

## 1. Pregunta qué herramienta usa
Si aún no lo sabes, pregunta, en un solo mensaje, qué herramienta de IA usa, dónde (web, app de escritorio o móvil) y con qué plan. Pregunta solo los datos que falten.

## 2. Guíale para instalar AI Onboarding
Explícale en una frase que, instalado, lo tendrá siempre a mano y recibirá las mejoras. Guíale con la opción de su herramienta. Si no cumple los requisitos, pasa al punto 3:

| Su herramienta | Cómo instalarlo |
|---|---|
| Claude (app de escritorio o web) — requiere plan de pago | En la barra lateral, **Customize** → **Plugins** → **Add marketplace** → escribir `Medu-coder/ai-adoption` → instalar **AI Onboarding** → activar **Sync automatically** (así recibe las mejoras solo). |
| Claude Code (versión 2.1.275 o posterior) | `/plugin install ai-onboarding --marketplace Medu-coder/ai-adoption` |
| ChatGPT / Codex en la **app de escritorio** | Guíale: menú **ChatGPT** → **Configuración** → **Complementos** → **Añadir** → **Añadir un marketplace** → en **Origen**, escribir `Medu-coder/ai-adoption` → **Añadir marketplace**. Después, en la pestaña **Complementos** (o **Explorar directorio**), instalar **AI Onboarding**. Para recibir mejoras: pestaña **Tienda** → **Actualizar** junto a AI Adoption. Si prefiere, puedes hacerlo tú con su permiso: `codex plugin marketplace add Medu-coder/ai-adoption`. |
| ChatGPT en la **web** | Puede instalar plugins del directorio, pero eso no añade este marketplace de GitHub a una cuenta personal. Si su empresa gestiona plugins, su administrador puede importar el marketplace para el equipo. Si no tiene esa vía, pasa al punto 3. |
| ChatGPT en el **móvil**, u otra herramienta sin instalación compatible | En el móvil solo se pueden usar los plugins que ya estén disponibles en su cuenta; este marketplace se añade desde la app de escritorio. Para otras herramientas, comprueba sus capacidades. Si no puede instalarlo, pasa al punto 3. |

Si lo instala, pídele que abra una conversación nueva y escriba "Quiero empezar con AI Onboarding", añadiendo en el mismo mensaje lo que ya te ha contado. Dale la frase completa lista para copiar, por ejemplo: "Quiero empezar con AI Onboarding. Uso Claude en la app de escritorio, con un plan de pago."

## 3. Si no se puede instalar
No sustituyas a AI Onboarding en esta conversación. Explícale con amabilidad, en dos o tres líneas, qué necesitaría para usarlo (por ejemplo, Claude con plan de pago en la web o el escritorio, Claude Code, o la app de escritorio de ChatGPT/Codex). Si alguna opción le encaja, guíale con ella; si no, dile que puede volver con este mismo mensaje cuando la tenga. No modifiques este repositorio.
