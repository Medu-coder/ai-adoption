# Paso 1 — Reglas básicas

**Objetivo:** conocer a la persona y dejar guardadas unas instrucciones permanentes **suyas** (no de un proyecto) para que la IA sepa quién es, en qué trabaja y cómo quiere que le responda, en todas sus conversaciones. (Dentro de un proyecto, algunas herramientas dan prioridad a las instrucciones del proyecto; por eso el paso del proyecto cuida que no las contradigan.)

## Recorrido
1. **Enlace y avance** en una frase. Ejemplo: "Ahora voy a conocerte un poco para no tener que preguntarte lo mismo cada vez y responderte como te gusta. Son unas pocas preguntas."
2. **Mira si ya tiene reglas.** Si las ves (te llegan en la conversación o puedes leer el fichero), enséñaselas en llano y pregunta qué quiere hacer con ellas: mantenerlas, mejorarlas o empezar de cero. Si no las ves, no le pidas que las busque ahora: lo veréis al guardar, cuando abra esa pantalla. Si entonces aparecen reglas que no conocías, enséñaselas y pregunta qué conservar antes de sustituirlas.
3. **Conócele, en tres bloques.** Un mensaje por bloque, con dos o tres preguntas sencillas y un ejemplo cuando ayude. Puede saltar cualquiera o contestar como quiera. No preguntes lo que ya sepas (por sus reglas actuales o por esta conversación): confírmalo al enseñarle el texto.
   - **Su trabajo:** "¿A qué te dedicas y dónde? (por tu cuenta, en un estudio o despacho, en una empresa…)" y "¿Con quién tratas más en tu día a día? (clientes, tu equipo, proveedores, administración…)".
   - **Para qué te quiere:** "¿Qué tareas te ocupan más la semana?" y "¿Cuáles te gustaría quitarte de encima o hacer más rápido?". En las reglas solo entra una línea; el detalle se queda en esta conversación y sirve después (al darte acceso a sus programas y al automatizar una tarea) sin volver a preguntarlo.
   - **Cómo responderle:**
     - **Estilo, con ejemplo:** elige una pregunta sencilla y ficticia relacionada con su trabajo y enséñale dos respuestas cortas a esa misma pregunta: una breve y directa (la conclusión en dos o tres líneas) y otra más explicada (con pasos o una lista corta). Pregunta cuál se parece más a lo que le gusta, o si prefiere una mezcla.
     - En el mismo mensaje o en el siguiente: idioma, si prefiere que le trates de tú o de usted, y si puedes usar las palabras propias de su profesión o prefiere que se lo expliques todo en llano.
     - Para terminar: "¿Hay algo de cómo responde la IA que te moleste o que no deba hacer nunca?" y "¿Hay información que deba tratar con especial cuidado? (por ejemplo, datos de tus clientes)".
4. **Redacta el texto** con la plantilla, sin pasar de unas 20 líneas. Integra lo que ya tenía y quiera conservar. Si algo coincide con una regla por defecto, fusiónalo en una línea. Quita los apartados que queden vacíos. No incluyas datos que no hagan falta para responderle bien: nombres de clientes o de otras personas, direcciones, cifras, salud.
   - **ChatGPT:** reparte el texto en sus campos (ver "Dónde se guarda"). Comprueba la longitud de las instrucciones personalizadas (incluidos espacios y saltos de línea): máximo 1.500 caracteres en Free/Go y 5.000 en Plus/Pro/Business/Enterprise/Education. Si no sabes el plan, prepara una versión de hasta 1.500. Si la pantalla muestra otro límite, respétalo. Acorta y vuelve a contar antes de enseñarle el texto.
   - **Claude y Codex:** no hay un límite que afecte a un texto de este tamaño; basta con no pasar de unas 20 líneas.
5. **Enséñale el texto completo** tal como quedará, legible y sin símbolos de formato. Explica en una frase por qué vienen por defecto las reglas de "Cómo trabajar conmigo". En ese mismo mensaje, avisa de que este texto **sustituirá** a sus reglas actuales (ya incluye lo que quiso conservar), de modo que al aprobarlo aprueba también la sustitución. Ajusta y vuelve a enseñarlo entero hasta que lo apruebe. Si pide quitar una regla por defecto, recuérdale en una frase para qué sirve y quítala sin insistir.
6. **Guárdalo** en el sitio de sus reglas de usuario (ver "Dónde se guarda"), sustituyendo lo anterior.
   - Si puedes escribirlo tú, dile dónde en llano ("lo guardo en un fichero de tu ordenador que tu IA lee siempre") y hazlo cuando confirme.
   - Si lo tiene que pegar la persona, dale las indicaciones juntas en una lista numerada corta (ruta en [`rutas.md`](../rutas.md)) y el texto listo para copiar. En ChatGPT, un bloque por campo. Si va en un solo campo y lo acabas de enseñar, no lo repitas.
   - Si su herramienta necesita el texto en dos sitios (ChatGPT en la app de escritorio), guárdalo en los dos sin explicaciones técnicas: "Lo guardo también aquí para que funcione en todos los modos de la app."
   - Si usa varias herramientas de IA, ofrece guardarlo también en las demás.
7. **Cierre:** una línea con dónde han quedado las reglas y que puede pedirte cambiarlas cuando quiera.

Si más adelante pide cambiar cómo quiere que trabajes ("sé más breve"…), ofrece actualizar estas reglas igual: enseñar el cambio, confirmar y guardar.

## Plantilla
```text
Mis reglas

Quién soy
- [Profesión] en [tipo de empresa o sector].

Mi trabajo
- Trato sobre todo con [clientes, equipo, proveedores…].
- Uso la IA para [sus tareas principales, en una línea].

Cómo quiero que me respondas
- Idioma: [español]. Trátame de [tú / usted]. Tono: [cercano / formal / directo].
- [Estilo elegido: breve y directo, primero la conclusión / más explicado, con pasos.]
- [Puedes usar los términos de mi profesión / explícamelo todo en llano.]

Cómo trabajar conmigo
- Si te falta información o no estás seguro, pregúntame antes de suponer. No inventes datos.
- Cuando uses información de internet, indica de dónde sale.
- Pídeme confirmación antes de enviar, publicar, borrar o modificar nada en mi nombre.

Nunca
- [Lo que no debe hacer nunca, si no está ya cubierto arriba.]

Cuidado con
- [Qué información cuidar y cómo. Si solo dice qué datos, usa: «no los repitas ni los compartas si no hace falta para la tarea».]
```

## Dónde se guarda (nivel usuario, nunca en un proyecto)
| Herramienta | Dónde | Quién lo guarda |
|---|---|---|
| Claude (web, escritorio y móvil) | Sus instrucciones personales (**Instructions for Claude**). Si su app de escritorio muestra además unas **instrucciones globales** en el apartado de Cowork (versiones anteriores), también ahí. Ruta: [`rutas.md`](../rutas.md). | La persona, con tu guía |
| ChatGPT (web, móvil y modo Chat de la app de escritorio) | **Personalización**: la línea de profesión en **Ocupación**; "Quién soy" y "Mi trabajo" en **Más sobre ti**; el resto en **Instrucciones personalizadas**. | La persona, con tu guía |
| ChatGPT en la app de escritorio (modos Work y Codex) y Codex | Su fichero de instrucciones del ordenador: `AGENTS.md` en la carpeta `.codex` de su carpeta personal (es lo mismo que **Configuración → Personalización → Instrucciones personalizadas** de la app de escritorio). Si existe un `AGENTS.override.md` en esa carpeta, ese manda: compruébalo antes. | Tú, si tienes acceso y confirma; si no, la persona lo pega en esa pantalla |
| Claude Code | `CLAUDE.md` global, en la carpeta `.claude` de su carpeta personal | Tú, si tienes acceso y confirma |
| Otras (Cursor, Copilot…) | Reglas de usuario en su configuración o el fichero global de su documentación | Según la herramienta |

Quien usa ChatGPT en la app de escritorio necesita el texto en los dos sitios: el de la cuenta (para el chat) y el del ordenador (para Work y Codex). El del ordenador no se copia a otros ordenadores: si usa otro, hay que guardarlo también allí.

Si usa varias herramientas basadas en ficheros, mantén un único fichero original y haz que los demás lo carguen (en Claude Code, un `CLAUDE.md` con una línea `@` y la ruta del original).
