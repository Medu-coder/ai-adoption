# Compatibilidad de AI Onboarding con OpenAI

Revisión: 26/10/2026. Versión del plugin: **0.1.5**.

## Resultado

La instalación, habilitación y detección de la skill pasan con **Codex CLI
0.137.0**, tanto desde el marketplace nativo de OpenAI como desde una copia
que solo contiene el marketplace compatible con Claude. El motor devuelve
`ai-onboarding:ai-onboarding` habilitada y sin errores de carga del plugin.

Esto acredita compatibilidad de paquete y carga en Codex. **No acredita una
prueba de extremo a extremo en la interfaz de ChatGPT**, ni la conexión real
de Gmail u otros servicios. El nombre y los metadatos de presentación se han
validado en el manifiesto, sin comprobación visual en el directorio.

## Cambios

- Metadatos de presentación para OpenAI en el manifiesto portable; identidad
  conservada y versión 0.1.5 sincronizada con el manifiesto de Claude.
- Instrucciones personales limitadas también por caracteres según plan de
  ChatGPT; si no se conoce el plan, se usa el límite de 1.500 caracteres.
- Nota corregida sobre aplicación inmediata de las instrucciones personales.
- Diferenciación entre instalar desde el directorio de ChatGPT web, importar
  este marketplace de GitHub y usar AI Onboarding sin instalación; móvil separado.
- El arranque pregunta únicamente los datos que faltan.
- Un conector sin herramienta o sin prueba satisfactoria queda pendiente de
  verificación; no se afirma lectura ni conexión verificada.

## Prueba reproducible

Requisitos: Python 3.11 o posterior, Ruby con YAML/JSON y Codex CLI.
Desde la raíz del repositorio:

```bash
python3 scripts/check-openai-compatibility.py
```

El script analiza JSON y YAML, comprueba enlaces relativos contenidos en el
plugin y ejecuta ambos recorridos de instalación con copias temporales.
Comprueba la versión descubierta, la instalación habilitada, la copia íntegra
de todos los archivos y la carga real con `skills/list` del app-server.

## Aislamiento y límites

- Cada recorrido usa un `CODEX_HOME` temporal y un directorio de trabajo vacío,
  fuera del repositorio. Empieza sin plugins disponibles ni instalados.
- No se copian credenciales, configuración personal ni variables de API. No
  se inicia sesión, no se llama a un modelo ni se conectan servicios.
- Solo se registra la copia local del marketplace; no se actualiza el
  marketplace personal ni se instala en el perfil habitual.
- Los perfiles temporales de la prueba reproducible se eliminan al terminar.
- Las huellas de la configuración, los plugins y las skills del usuario se
  comparan antes y después. Resultado observado: **sin cambios**.
- Es aislamiento de configuración y archivos de prueba, no una máquina
  virtual. `HOME` no se cambia: el app-server puede descubrir metadatos de
  skills personales en modo lectura. No se ejecutan esas skills ni se envía
  su contenido a un modelo. Los errores ajenos al plugin no se cuentan como
  errores de AI Onboarding.

## Simulación conversacional independiente

Un subagente revisó el recorrido con datos sintéticos, sin instalar ni escribir
archivos. Los seis escenarios resultaron coherentes con las instrucciones:

| Escenario | Resultado esperado |
|---|---|
| Profesora en ChatGPT web Free; contexto ya conocido | Una pregunta sobre sus reglas, sin repetir plataforma o plan |
| Preferencias extensas en Free | Texto de hasta 1.500 caracteres; guía para guardarlo sin afirmar que ya está guardado |
| Gmail anunciado como conectado, pero sin herramienta | Estado pendiente de verificación; ninguna lectura inventada |
| Retomar reglas completadas, proyecto saltado y Gmail pendiente | Continuar por Gmail, sin reiniciar el cuestionario |
| Duda suelta sobre cómo pedir un resumen | Respuesta práctica sin iniciar todo el módulo |
| Usuaria de Claude | Mantener su recorrido de instalación y configuración |

La simulación es una revisión del comportamiento esperado, no una ejecución
real de conversaciones de ChatGPT ni una garantía de respuestas deterministas.

## Referencias oficiales

- [Paquetes y marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Importación de marketplaces en workspaces](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Disponibilidad de plugins](https://learn.chatgpt.com/docs/plugins)
- [Instrucciones personalizadas y límites](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)
