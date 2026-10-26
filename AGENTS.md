# Instrucciones para agentes (y personas)

## Regla nº 1: repositorio PÚBLICO
- Nunca añadir claves de API, tokens, contraseñas, cookies, ficheros `.env`, certificados ni credenciales de ningún tipo.
- Nunca añadir datos personales, datos de clientes o de empresas (incluido Minsait/Indra o sus clientes), ni nombres reales de usuarios del kit.
- Los ejemplos usan siempre datos ficticios.
- Las skills que necesiten credenciales las piden al usuario en su propio entorno (conector o variable local); jamás las incluyen.
- Antes de cada commit, revisar el diff buscando secretos. Si se sube uno por error: avisar, revocar la clave de inmediato (borrar el commit no basta).

## Contenido
- `docs/`: enfoque, metodología, guías de instalación para usuarios no técnicos.
- `plugins/<nombre>/`: un plugin por perfil o caso de uso, con sus skills.

## Estilo
- Español, lenguaje claro para personas no técnicas.
- Simplicidad: nada de infraestructura extra sin necesidad.
