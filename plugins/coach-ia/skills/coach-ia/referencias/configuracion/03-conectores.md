# Paso 3 — Conectores

**Objetivo:** que la IA pueda consultar las herramientas que la persona ya usa.

## Antes de empezar
Pregunta una sola vez: "¿Tu empresa o tus clientes tienen alguna norma sobre usar IA con sus datos?" Si las hay, tenlas en cuenta y no propongas conectar lo que choque con ellas.

## Recorrido (categoría a categoría, en el orden de la tabla)
1. **Pregunta qué usa.** Ejemplo: "¿Tu correo es de Google (Gmail), de Microsoft (Outlook) u otro? Si no lo necesitas, lo saltamos."
2. Si no usa nada de esa categoría o no quiere conectarlo, sáltala sin insistir.
3. **Ofrece el conector** de la forma más directa posible (ver abajo).
4. **Espera** a que confirme que ha iniciado sesión y dado permiso.
5. **Comprueba** con la prueba de la tabla: revisa primero que tienes la herramienta necesaria en esta sesión. Si está disponible, avísale de qué vas a consultar y hazlo, sin pedir otra confirmación. Si no está disponible o falla justo después de conectar, puede hacer falta una conversación nueva para que el conector esté disponible; explícaselo y pídele que haga la prueba allí y vuelva a esta conversación para seguir. Si sigue sin estar disponible o falla, apúntalo como pendiente. No afirmes que has leído datos ni marques el servicio como conectado y verificado sin una prueba satisfactoria.

| # | Categoría | Opciones habituales | Prueba inofensiva |
|---|---|---|---|
| 1 | Correo | Gmail, Outlook | Leer los asuntos de los 3 últimos correos |
| 2 | Calendario | Google Calendar, Outlook | Ver la agenda de hoy |
| 3 | Archivos y ofimática | Google Drive, OneDrive / SharePoint, Dropbox, Box | Buscar por su nombre un documento que te diga ella, sin abrir su contenido |
| 4 | Notas | Notion, OneNote, Evernote, Obsidian, Apple Notas | Leer una nota que ella indique |
| 5 | Tareas | Todoist, Asana, Trello, ClickUp, Planner | Listar los títulos de hasta 3 tareas pendientes de una lista que ella indique |
| 6 | Mensajería | Slack, Teams, WhatsApp, Telegram… | Leer el último mensaje de un canal que ella indique |
| 7 | Reuniones | Zoom, Meet, Teams, transcriptores | Encontrar la última reunión |
| 8 | Archivos del ordenador | Una carpeta concreta (solo apps de escritorio) | Listar el contenido de la carpeta |
| 9 | Opcionales | CRM, diseño (Canva, Figma) | Según el caso |

- **Mensajería:** muchas apps personales (como WhatsApp) no tienen conector. Díselo y propón copiar el mensaje o pegar una captura cuando lo necesite.
- **Carpeta del ordenador:** mejor una carpeta concreta que toda su carpeta personal. Si puedes pedir acceso, hazlo y avísale de que verá un aviso para permitirlo; si no, guíala para añadirla desde la app.
- Los programas específicos de su profesión no van aquí.

## Cómo ofrecer el conector (primera opción posible)
1. **Tarjeta o botón de conexión en el chat**, si puedes buscar el conector en el directorio de tu app y mostrárselo para que pulse "Conectar". En Claude: búscalo en el directorio y muéstralo como sugerencia de conexión.
2. **Enlace directo** a la pantalla donde se conecta.
3. **Instrucciones escritas** con la ruta de [`rutas.md`](../rutas.md). Si tu herramienta no está ahí, dilo y descríbela de forma aproximada (suele estar en "Conectores", "Apps" o "Integraciones" de la configuración); no la inventes.

Si no hay conector para lo que usa, díselo y propón una alternativa (por ejemplo, subir el archivo al chat).

## Permisos
- Si la pantalla de conexión deja elegir, recomienda empezar solo con lectura. Si no deja, explícale qué permite y recuérdale que pedirás confirmación antes de enviar, crear o modificar nada.
- No digas que un conector es "solo de lectura" si no lo has comprobado.
- Conecta solo lo que use de verdad.

## Cierre del paso
Tabla con lo que usa (omite las categorías que no usa):

| Categoría | Servicio | Estado |
|---|---|---|
| Correo | … | Conectado / Pendiente / Sin conector |
