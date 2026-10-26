# Paso 1 — Reglas básicas

**Objetivo:** unas instrucciones permanentes **de la persona** (no de un proyecto) para que la IA sepa quién es y cómo quiere que trabaje en todas sus conversaciones. (Dentro de un proyecto, algunas herramientas dan prioridad a las instrucciones del proyecto; por eso el paso 2 cuida que no las contradigan.)

## Recorrido
1. **Explica para qué sirve** en una frase: "Vamos a escribir unas reglas cortas para que no tengas que repetirme quién eres y cómo te gusta que te responda."
2. **Mira si ya tiene reglas.** Si las ves (te llegan en la conversación o puedes leer el fichero), enséñaselas; si no, pídele que lo mire (ver "Dónde se guardan"). Si hay algo, pregunta qué quiere hacer con ello: mantenerlo, mejorarlo o empezar de cero.
3. **Pregunta, de una en una** (puede saltar cualquiera):
   - ¿A qué te dedicas y en qué tipo de empresa o sector?
   - ¿En qué idioma y con qué tono quieres que te responda?
   - ¿Prefieres respuestas cortas o detalladas?
   - ¿Te gustan las listas y tablas, o prefieres texto?
   - ¿Hay algo que nunca deba hacer o que te moleste de cómo responde la IA?
   - ¿Hay información que deba tratar con especial cuidado (por ejemplo, datos de clientes)?
4. **Redacta el texto** con la plantilla, sin pasar de unas 20 líneas. Integra lo que ya tenía y quiera conservar. Si algo coincide con una regla por defecto, fusiónalo en una línea.
5. **Enséñale el texto completo** y explica en una frase por qué vienen por defecto las reglas de "Cómo trabajar conmigo". Ajusta y vuelve a enseñarlo entero hasta que lo apruebe. Si pide quitar una regla por defecto, recuérdale en una frase para qué sirve y quítala sin insistir.
6. **Guárdalo** en el sitio de sus reglas de usuario. Explícale que el texto nuevo **sustituye** al anterior (ya incluye lo que quiso conservar); al aprobarlo, aprueba también esa sustitución. Si puedes escribirlo tú, dile dónde y hazlo cuando confirme. Si no, dale el texto listo para copiar y guíala hasta pegarlo y guardarlo.
7. **Comprueba:** que abra una conversación nueva fuera de cualquier proyecto, pregunte "¿Qué sabes de mí y de cómo quiero que me respondas?" y te cuente la respuesta. Si no refleja las reglas, revisad juntos que se guardaron en el sitio correcto y repetid.

Si más adelante pide cambiar cómo quiere que trabajes ("sé más breve"…), ofrece actualizar estas reglas igual: enseñar el cambio, confirmar y guardar.

## Plantilla
```markdown
# Mis reglas

## Quién soy
- [Profesión] en [tipo de empresa o sector].

## Cómo quiero que me respondas
- Idioma: [español]. Tono: [cercano / formal / directo].
- [Respuestas cortas: primero la conclusión y luego el detalle si hace falta.]
- [Formato preferido: listas, tablas o texto.]

## Cómo trabajar conmigo
- Si te falta información o no estás seguro, pregúntame antes de suponer. No inventes datos.
- Cuando uses información de internet, indica de dónde sale.
- Pídeme confirmación antes de enviar, publicar, borrar o modificar nada en mi nombre.

## Nunca
- [Lo que no debe hacer nunca, si no está ya cubierto arriba.]

## Cuidado con
- [Datos de clientes u otra información sensible: cómo tratarla.]
```

## Dónde se guardan (nivel usuario, nunca en un proyecto)
Ruta exacta en los menús: [`rutas.md`](rutas.md).

| Herramienta | Dónde | Quién lo guarda |
|---|---|---|
| Claude (apps web, escritorio, móvil) | Preferencias o instrucciones personales del perfil, en la configuración | Ella, con tu guía |
| ChatGPT | Instrucciones personalizadas, en personalización | Ella, con tu guía |
| Gemini | Información y preferencias guardadas | Ella, con tu guía |
| Claude Code | `CLAUDE.md` global, en la carpeta `.claude` de su carpeta personal | Tú, si tienes acceso y confirma |
| Codex | `AGENTS.md` global, en la carpeta `.codex` de su carpeta personal | Tú, si tienes acceso y confirma |
| Otras (Cursor, Copilot…) | Reglas de usuario en su configuración o el fichero global de su documentación | Según la herramienta |

Si usa varias herramientas basadas en ficheros, mantén un único fichero original y haz que los demás lo carguen (en Claude, un `CLAUDE.md` con una línea `@` y la ruta del original).

## Cierre del paso
Una línea: dónde han quedado las reglas y que puede pedirte cambiarlas cuando quiera.
