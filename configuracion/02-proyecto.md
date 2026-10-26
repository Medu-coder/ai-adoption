# Paso 2 — Proyecto (opcional)

**Objetivo:** decidir con la persona si le conviene crear un proyecto y, si quiere, crearlo con ella.

## 1. Explica qué es y qué aporta
Un proyecto es un espacio de trabajo para un tema concreto (por ejemplo, "Obras en curso", "Clientes" u "Oposiciones"). Explícale, en sencillo, qué gana:

- **Instrucciones propias** de ese tema, que se suman a sus reglas básicas (paso 1) sin repetirlas.
- **Documentos de referencia** que la IA tiene siempre a mano (normativa, plantillas, precios…), sin tener que subirlos en cada conversación.
- **Conversaciones agrupadas** y, en algunas herramientas, memoria propia del tema.

Y cuándo **no** hace falta: si solo va a hacer consultas sueltas, puede empezar sin proyecto y crearlo más adelante.

## 2. Pregunta si quiere uno
"¿Quieres que creemos ahora un proyecto para algún tema de tu trabajo, o lo dejamos para más adelante?"
Si no quiere, sáltalo sin insistir y pasa al paso 3.

## 3. Si quiere, créalo guiado
1. **Tema y nombre:** pregunta para qué tema lo quiere y propón un nombre corto.
2. **Instrucciones del proyecto:** pregunta, de una en una:
   - ¿Para qué vas a usar este proyecto? ¿Qué tareas harás en él?
   - ¿Hay algo que la IA deba tener siempre en cuenta en este tema (forma de trabajar, criterios, documentos que debe usar)?

   Redacta unas pocas líneas **solo de ese tema**. No repitas sus reglas básicas ni las contradigas; si algo del tema choca con ellas, pregúntale cuál manda. Enséñaselas y ajústalas hasta que las apruebe. Ejemplo de instrucciones de proyecto:
   ```
   - Este proyecto es para el seguimiento de las obras en curso.
   - Ayúdame con mediciones, presupuestos y cambios que pida el cliente.
   - Para presupuestos, usa la estructura de la plantilla adjunta.
   ```
3. **Documentos:** pregunta qué documentos de referencia quiere añadir. Recuérdale que solo suba lo que esté dispuesta a que la IA consulte y que, si contienen datos personales de terceros (clientes, empleados…), es mejor subir versiones sin esos datos (por ejemplo, la plantilla vacía).
4. **Crearlo**, según su herramienta:

| Herramienta | Cómo | Quién lo crea |
|---|---|---|
| Claude (web, escritorio) | Un proyecto en el apartado de Proyectos, con nombre, instrucciones y documentos. | La persona, con tu guía |
| ChatGPT | Un proyecto desde la barra lateral, con instrucciones y archivos. | La persona, con tu guía |
| Gemini | Una Gem con las instrucciones y los documentos del tema. | La persona, con tu guía |
| Agentes que trabajan sobre una carpeta (Claude Code, Codex, Cursor…) | Una carpeta para el tema con su propio `AGENTS.md` (las instrucciones del proyecto) y, para Claude, un `CLAUDE.md` con una sola línea: `@AGENTS.md`. | Tú, si tienes acceso y lo confirma |

5. **Comprueba:** que abra una conversación nueva dentro del proyecto, pregunte "¿En qué consiste este proyecto y qué documentos tienes?" y te cuente qué le ha contestado.

## Cierre del paso
Resume en una línea qué proyecto ha quedado creado (o que se ha dejado para más adelante) y recuerda que puede crear más cuando quiera.
