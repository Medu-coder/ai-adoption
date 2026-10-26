# Instrucciones para agentes (y personas)

Este fichero lo leen varias herramientas de IA (Claude carga `CLAUDE.md`, que a su vez carga este).

## Regla nº 1: repositorio PÚBLICO
- Nunca añadir claves de API, tokens, contraseñas, cookies, ficheros `.env`, certificados ni credenciales de ningún tipo.
- Nunca añadir datos reales: personas atendidas, sus clientes, proyectos, documentos o plantillas internas, ni datos de empresas (incluido Minsait/Indra o sus clientes).
- Solo entra la versión **generalizada** de cada skill o rutina, con ejemplos ficticios.
- Los datos reales del trabajo con cada persona viven **fuera de este repo** (o, como red de seguridad, en `privado/`, que está ignorado por git).
- Las skills que necesiten credenciales las piden en el entorno del usuario (conector o configuración local); jamás las incluyen.
- Antes de cada commit, revisar el diff buscando secretos y datos reales. Si se sube un secreto por error: avisar y revocarlo de inmediato (borrar el commit no basta).

## Agnóstico de herramienta
- Cada skill o rutina se escribe primero en formato neutro (`plantillas/`): objetivo, cuándo usarla, entradas, pasos, salida, ejemplo y límites.
- Las adaptaciones a herramientas concretas son secundarias y van como sección o fichero aparte dentro de la propia skill.
- No asumir que la persona usa Claude ni que su herramienta permite rutinas programadas o conectores; comprobarlo.

## Proceso (ver `docs/proceso.md`)
Preparar → Descubrir → Construir → Generalizar → Compartir → Particularizar.

## Organización
- `sectores/<sector>/skills/<nombre-skill>/` para skills generalizadas de un sector.
- `sectores/_comun/skills/` para skills útiles a cualquier perfil.
- Nombres de carpeta en minúsculas y con guiones.

## Estilo
- Español, lenguaje claro para personas no técnicas.
- Simplicidad: nada de infraestructura extra sin necesidad.
