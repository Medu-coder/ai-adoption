# Paso 1 — Reglas básicas

**Objetivo:** que la IA sepa desde el principio quién es la persona y cómo quiere que trabaje con ella. Son unas pocas instrucciones permanentes que la herramienta tiene en cuenta en cada conversación.

## Recorrido
1. **Explica en una frase para qué sirve.** Ejemplo: "Vamos a escribir unas reglas cortas para que no tengas que repetirme cada vez quién eres y cómo te gusta que te responda."
2. **Haz estas preguntas, de una en una** (la persona puede saltar cualquiera):
   - ¿A qué te dedicas y en qué tipo de empresa o sector?
   - ¿En qué idioma y con qué tono quieres que te responda (cercano, formal, directo…)?
   - ¿Prefieres respuestas cortas o detalladas? ¿Te gustan las listas y tablas, o mejor texto?
   - ¿Hay algo que nunca deba hacer o que te moleste de cómo responde la IA?
   - ¿Hay información que deba tratar con especial cuidado (por ejemplo, datos de clientes)?
3. **Redacta un borrador** con la plantilla de abajo, en lenguaje sencillo y sin pasar de unas 20 líneas.
4. **Enséñaselo y ajústalo** hasta que la persona diga que está bien.
5. **Guárdalo donde corresponda** en su herramienta (ver "Dónde se guardan").
6. **Comprueba** que se aplica: pide a la persona que abra una conversación nueva y pregunte "¿Qué sabes de mí y de cómo quiero que me respondas?".

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

## Dónde se guardan
Depende de la herramienta. Usa la opción que tengas disponible y, si no conoces la ruta exacta en los menús, dilo y descríbela de forma aproximada en vez de inventarla.

| Herramienta | Dónde |
|---|---|
| Claude (web, escritorio, móvil) | Instrucciones o preferencias personales en la configuración del perfil. Si trabaja dentro de un Proyecto, también en las instrucciones del proyecto. |
| ChatGPT | Instrucciones personalizadas, en el apartado de personalización. |
| Gemini | Instrucciones de una Gem o el apartado de información y preferencias guardadas. |
| Agentes que trabajan sobre una carpeta (Claude Code, Codex, Cursor, Copilot…) | Un fichero `AGENTS.md` en la carpeta de trabajo. Para Claude, añade además un `CLAUDE.md` con una sola línea: `@AGENTS.md` (así Claude carga el mismo fichero). |

Si tienes acceso a sus archivos, ofrece crear tú el fichero `AGENTS.md` (y `CLAUDE.md`) en la carpeta que indique, y hazlo solo cuando lo confirme. Si no, dale el texto listo para copiar y pegar, y dile dónde.

## Cierre del paso
Resume en una línea dónde han quedado guardadas las reglas y recuerda que puede cambiarlas cuando quiera.
