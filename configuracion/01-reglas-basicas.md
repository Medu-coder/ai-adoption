# Paso 1 — Reglas básicas

**Objetivo:** que la IA sepa siempre quién es la persona y cómo quiere que trabaje con ella. Son instrucciones **de la persona**, no de un proyecto concreto: se aplican en todas sus conversaciones y en cualquier proyecto que cree después.

## Recorrido (siempre guiado)
1. **Explica en una frase para qué sirve.** Ejemplo: "Vamos a escribir unas reglas cortas para que no tengas que repetirme cada vez quién eres y cómo te gusta que te responda. Se aplicarán siempre, en todo lo que hagas conmigo."
2. **Mira si ya tiene reglas.** Revisa el lugar donde se guardan en su herramienta (ver "Dónde se guardan"). Si ya hay algo, enséñaselo y pregunta si lo mantenemos, lo mejoramos o empezamos de cero.
3. **Haz estas preguntas, de una en una** (puede saltar cualquiera):
   - ¿A qué te dedicas y en qué tipo de empresa o sector?
   - ¿En qué idioma y con qué tono quieres que te responda (cercano, formal, directo…)?
   - ¿Prefieres respuestas cortas o detalladas? ¿Te gustan las listas y tablas, o mejor texto?
   - ¿Hay algo que nunca deba hacer o que te moleste de cómo responde la IA?
   - ¿Hay información que deba tratar con especial cuidado (por ejemplo, datos de clientes)?
4. **Redacta el texto** con la plantilla de abajo, en lenguaje sencillo y sin pasar de unas 20 líneas. Si ya tenía reglas que quiere mantener, intégralas.
5. **Enséñale el texto completo y ajústalo** con lo que te pida, tantas veces como haga falta, hasta que diga que está bien.
6. **Guárdalo** en el sitio de sus reglas de usuario:
   - Si puedes escribir en ese fichero o configuración, dile exactamente dónde lo vas a guardar y hazlo cuando lo confirme. Si el fichero ya existía, actualízalo con el texto acordado; no borres nada que no haya pedido quitar.
   - Si no puedes, dale el texto listo para copiar y guíale pantalla a pantalla hasta pegarlo.
7. **Comprueba** que se aplica: pide que abra una conversación nueva (fuera de cualquier proyecto) y pregunte "¿Qué sabes de mí y de cómo quiero que me respondas?".

Cada vez que más adelante la persona pida cambiar cómo quiere que trabajes ("no uses tablas", "sé más breve"…), ofrece actualizar estas reglas de la misma forma: enseñar el cambio, confirmar y guardar.

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

## Cuidado con
- [Datos de clientes u otra información sensible: cómo tratarla.]

## Herramientas que uso
- [Se completa en el paso de conectores.]
```
Las reglas de "Cómo trabajar conmigo" se proponen por defecto porque protegen a la persona; explícaselas y quítalas solo si ella lo pide.

## Dónde se guardan (nivel usuario, no proyecto)
Usa el sitio de **reglas generales de la persona** de su herramienta. No uses las instrucciones de un proyecto para esto. Si no conoces la ruta exacta en los menús, dilo y descríbela de forma aproximada en vez de inventarla.

| Herramienta | Dónde |
|---|---|
| Apps de chat de Claude (web, escritorio, móvil) | Instrucciones o preferencias personales en la configuración del perfil. |
| Claude Code | Fichero `CLAUDE.md` global del usuario, en la carpeta `.claude` de su carpeta personal. |
| Codex | Fichero `AGENTS.md` global del usuario, en la carpeta `.codex` de su carpeta personal. |
| ChatGPT | Instrucciones personalizadas, en el apartado de personalización. |
| Gemini | Apartado de información y preferencias guardadas. |
| Otras (Cursor, Copilot…) | Reglas de usuario en su configuración, o el fichero global que indique su documentación. |

**Si usa varias herramientas basadas en ficheros:** mantén un único fichero de reglas como original y haz que los demás lo carguen cuando la herramienta lo permita (en Claude, un `CLAUDE.md` con una sola línea `@` seguida de la ruta del fichero original). Así solo hay que actualizarlo en un sitio.

## Cierre del paso
Resume en una línea dónde han quedado guardadas las reglas y recuerda que puede pedirte cambiarlas cuando quiera.
