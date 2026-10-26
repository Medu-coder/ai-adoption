# Apps sin conector (caso principal: WhatsApp)

**Cuándo usarlo:** cuando la persona necesita que la IA lea una app que forma parte de su trabajo y no tiene conector oficial. El caso más habitual es WhatsApp. Úsalo desde el paso de conectores (mensajería) o desde sus herramientas del módulo 2.

## Principios
- **Solo leer y preparar borradores.** La IA lee, resume y propone respuestas; **ella las envía**. No envíes mensajes, no respondas ni marques nada en su nombre, aunque te lo pida: explícale que la app puede bloquear la cuenta si detecta automatización y que así se evita un envío equivocado.
- **Solo vías oficiales:** la versión web o la app de escritorio, que ella usa con su sesión. Nunca propongas servidores, librerías o extensiones no oficiales que se conecten a la app por detrás: incumplen sus condiciones y exponen la cuenta.
- **Son mensajes de terceros:** limítate a los chats de trabajo que ella indique. No guardes ni repitas su contenido si no hace falta para la tarea.

## Elige la vía, en este orden
1. **Navegador integrado con la versión web** (en WhatsApp: web.whatsapp.com). Usa el navegador integrado de tu app de escritorio, no extensiones. Pídele que inicie sesión ella (en WhatsApp, escaneando el código QR con el móvil). Después lees el texto de la página. Es la vía más rápida y precisa. La sesión puede caducar: si pasa, que vuelva a iniciarla.
2. **Uso del ordenador con la app de escritorio**, si no tienes navegador integrado pero sí uso del ordenador (paso 4 del módulo 1, `configuracion/04-uso-del-ordenador.md`; si no lo activó, ofrécelo con ese paso). Pídele permiso para usar esa app y navega por los chats que indique. Es más lento y solo ves lo que aparece en pantalla.
3. **Exportar el chat**, si no hay ninguna de las dos o para un análisis puntual: que exporte el chat como texto, sin archivos (en WhatsApp, desde el menú del chat: **Más** → **Exportar chat**), y te lo adjunte.

Si su herramienta no permite ninguna de las dos primeras, díselo y ofrece la tercera.

## Tipo de uso (pregúntalo una vez)
"¿Usas WhatsApp solo para trabajo o también para temas personales?"
- **Solo trabajo:** todos los chats se pueden leer; no hace falta lista.
- **Mixto:** trabaja siempre con su **lista de contactos** (abajo). Nunca abras un chat que no esté en "Trabajo".

## Lista de contactos (uso mixto)
**Dónde:** un archivo `contactos-whatsapp.md` en su carpeta de trabajo conectada (paso 3 del módulo 1). Si no tiene carpeta conectada, ofrécele conectarla ahora; sin carpeta, no se puede mantener la lista. Si ya existe, úsala y no la rehagas.

**Primera clasificación, sin abrir ningún chat:**
1. Mira solo la lista de chats (nombres y grupos), sin entrar en ninguno.
2. Propón una clasificación por los nombres: trabajo, personal o por clasificar si dudas.
3. Enséñasela, que corrija lo que haga falta y, cuando la apruebe, guárdala en el archivo (pide confirmación antes de crearlo).

**Formato del archivo:**
```markdown
# Contactos de WhatsApp
Solo se abren los chats de "Trabajo". Los de "Personal" no se abren nunca.

## Trabajo
- Estudio López
- Obra Calle Mayor (grupo)

## Personal
- Mamá
- Fútbol peques (grupo)

## Por clasificar
- +34 600 000 000
```
Identifica cada chat por el nombre que se ve y añade el número si aparece (los nombres pueden cambiar).

**Cada vez que leas WhatsApp:**
1. Lee el archivo antes de nada.
2. En la lista de chats, mira solo los que tienen mensajes sin leer.
3. Abre únicamente los de "Trabajo". Los de "Personal" ni se abren.
4. Si hay chats nuevos o en "Por clasificar", no los abras: al terminar, pregúntale en una sola lista si son de trabajo o personales, y actualiza el archivo con su respuesta.

Así la lista se mantiene sola con el uso, y cada lectura depende solo de los chats de trabajo con mensajes nuevos.

## Prueba inofensiva
Con su permiso, lee el último mensaje de un chat de trabajo que ella indique y díselo en una línea. Si no funciona, apúntalo como pendiente.

## Siguiente paso natural
Leer mensajes de trabajo cada día es una buena candidata para su primera skill (por ejemplo: "cada mañana, resume los mensajes de clientes de ayer y prepara borradores de respuesta"). Si está en el módulo 2, propónla al buscar la tarea. Si su uso es mixto, la skill debe seguir el apartado "Cada vez que leas WhatsApp" y leer y actualizar `contactos-whatsapp.md`; inclúyelo en el resumen que pases al creador.
