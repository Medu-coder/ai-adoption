# Paso 3 — Conectores generales

**Objetivo:** que la IA pueda consultar (y más adelante, si hace falta, actuar en) las herramientas que la persona ya usa.

## Recorrido
Ve categoría por categoría, en este orden. Para cada una:

1. **Pregunta qué usa.** Ejemplo: "¿Tu correo es de Google (Gmail), de Microsoft (Outlook) u otro? Si no lo necesitas, lo saltamos."
2. **Si no usa nada de esa categoría o no quiere conectarlo**, sáltala sin insistir.
3. **Ofrece el conector concreto** de la forma más directa que permita tu herramienta (ver "Cómo ofrecer el conector").
4. **Espera** a que la persona confirme que ha iniciado sesión y dado permiso.
5. **Comprueba** que funciona con la prueba inofensiva de la tabla. Si la prueba necesita un dato (por ejemplo, el nombre de un documento), pídeselo. Si falla justo después de conectar, puede que haga falta abrir una conversación nueva para que el conector esté disponible: explícaselo y, si es así, pídele que vuelva a esta conversación o que repita la prueba allí. Si sigue fallando, apúntalo como pendiente.

| # | Categoría | Opciones habituales | Prueba inofensiva |
|---|---|---|---|
| 1 | Correo | Gmail, Outlook | Leer los asuntos de los 3 últimos correos |
| 2 | Calendario | Google Calendar, Outlook | Ver la agenda de hoy |
| 3 | Archivos y ofimática | Google Drive (Docs, Sheets), Microsoft OneDrive / SharePoint (Word, Excel), Dropbox, Box | Buscar un documento cuyo nombre te diga la persona |
| 4 | Notas | Notion, OneNote, Evernote, Obsidian, Apple Notas | Leer una nota que la persona indique |
| 5 | Tareas y proyectos | Todoist, Asana, Trello, ClickUp, Microsoft Planner | Listar tareas pendientes |
| 6 | Mensajería | Slack, Microsoft Teams, WhatsApp, Telegram… | Leer el último mensaje de un canal o chat |
| 7 | Reuniones | Zoom, Google Meet, Teams, transcriptores (Granola, Fireflies…) | Encontrar la última reunión |
| 8 | Archivos del ordenador | Una carpeta de su ordenador (solo en apps de escritorio) | Listar el contenido de la carpeta |
| 9 | Opcionales | CRM (HubSpot…), diseño (Canva, Figma) | Según el caso |

Notas por categoría:
- **Mensajería:** muchas apps de mensajería personal (como WhatsApp) no tienen conector. Si es su caso, díselo y propón la alternativa: copiar el mensaje o hacer una captura y pegarla en el chat cuando lo necesite.
- **Archivos del ordenador:** solo en apps de escritorio. Pregunta qué carpeta quiere compartir (mejor una concreta que toda su carpeta personal). Si tu herramienta puede pedir acceso a una carpeta, hazlo y explícale que verá un aviso para elegirla y permitirlo; si no, guíale para añadirla desde la app.
- Las herramientas específicas de su profesión (programas de diseño, cálculo…) no van aquí.

## Cómo ofrecer el conector
Usa la primera opción que tu herramienta permita:

1. **Tarjeta o botón de conexión dentro del chat.** Si puedes buscar en el directorio de conectores de tu app y mostrar al usuario el conector concreto para que pulse "Conectar", hazlo. Así solo tiene que pulsar e iniciar sesión.
   - *Claude:* busca el conector en el directorio y muéstraselo como sugerencia de conexión (tarjeta con botón).
2. **Enlace directo** a la pantalla de configuración donde se conecta, si tu herramienta lo ofrece.
3. **Instrucciones escritas:** dile dónde está en la configuración de su app (normalmente en un apartado de "Conectores", "Aplicaciones" o "Integraciones"). Si no conoces la ruta exacta, dilo y descríbela de forma aproximada en vez de inventarla.

Si tu herramienta no tiene conector para lo que usa la persona, díselo con claridad y propón una alternativa (por ejemplo, subir el archivo al chat cuando lo necesite).

## Permisos
- Si la pantalla de conexión deja elegir permisos, recomiéndale empezar solo con **lectura**. Muchos servicios no dejan elegir: en ese caso, explícale qué permite el conector y recuérdale que, por sus reglas básicas, le pedirás confirmación antes de enviar, crear o modificar nada.
- No le digas que un conector es "solo de lectura" si no lo has podido comprobar.
- Conecta solo lo que la persona use de verdad: menos conectores, menos riesgo y menos confusión.

## Cierre del paso
Muestra un resumen breve:

| Categoría | Servicio | Estado |
|---|---|---|
| Correo | … | Conectado / Pendiente / Sin conector / No aplica |
