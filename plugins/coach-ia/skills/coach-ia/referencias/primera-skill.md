# Módulo 2 — Automatizar una tarea (primera skill)

**Objetivo:** detectar con la persona una tarea repetitiva de su trabajo y convertirla en una skill: instrucciones que la IA sigue siempre igual, sin que haya que explicárselo cada vez. Es opcional: si no aparece una tarea que encaje, no se fuerza.

Trabaja solo con la plataforma en la que estás funcionando: no guíes para crear skills en otra herramienta. Usa lo que ya sabes de su herramienta, superficie (web, escritorio, móvil) y plan; si no lo sabes, pregúntalo una vez. Todo el módulo se hace en esta conversación.

Con la persona no uses las palabras "skill", "plugin" ni "conector" (ver "Cómo hablarle" en la skill): habla de "una tarea que aprendo a hacer por ti" y de "darme acceso" a sus programas. Solo cuando tenga que pulsar algo con ese nombre en la pantalla, dáselo tal cual.

Si no ha hecho el módulo 1, antes de empezar pregunta a qué se dedica y ofrécele hacer antes el módulo 1, sin insistir.

## Recorrido
1. **Ofrece el módulo:** "Si quieres, ahora te ahorro tiempo con algo que hagas a menudo: buscamos una tarea que repites en tu trabajo y la aprendo a hacer por ti, siempre igual, sin que me la expliques cada vez. Antes veo a qué otros programas de tu trabajo puedo acceder. ¿Empezamos o lo dejamos para otro día?"
2. **Comprueba qué permite su superficie** (ver "Dónde se puede"). Si no admite skills propias, díselo e indica dónde sí podría crearlas; aun así, haz los pasos 3 a 6 (conectar sus herramientas, encontrar la tarea y buscar si hay una skill hecha que pueda instalar). Si no hay ninguna, cierra el módulo con la creación de la skill como pendiente. Si su plataforma exige activar algo antes (por ejemplo, la ejecución de código en Claude), díselo aquí.
3. **Sus herramientas del día a día.** Pregunta una sola vez: "Además del correo y la agenda, ¿qué programas usas en tu trabajo? Por ejemplo, para diseñar, hacer presupuestos o llevar a tus clientes."
   - Busca cada una en el directorio oficial de conectores y plugins de tu plataforma, igual que en "Buscar skills hechas". Solo resultados oficiales; no inventes.
   - Enséñale el resultado en una lista corta y en llano: cada programa, si puedes acceder a él y qué podrías hacer por la persona.
   - Ofrece conectarlas **una a una**, como en el paso de conectores del módulo 1 (`configuracion/02-conectores.md`): tarjeta de conexión si puedes, permisos de solo lectura si deja elegir y una prueba inofensiva. Las que no quiera conectar o no tengan conector, anótalas y sigue.
   - Si es una app de mensajería como WhatsApp: si ya la configuró en el módulo 1, no la repitas; si no, sigue [`configuracion/04-apps-sin-conector.md`](configuracion/04-apps-sin-conector.md).
   - Si otra herramienta no tiene conector pero la usa en su ordenador, recuérdale que con el **uso del ordenador** (paso 3 del módulo 1) la IA puede usarla directamente; si no lo activó, ofrécelo ahora con ese paso (`configuracion/03-uso-del-ordenador.md`).
4. **Encuentra la tarea.** Pregunta, de una en una:
   - ¿Qué tarea haces cada semana (o más) siguiendo siempre los mismos pasos?
   - ¿Qué resultado entregas (un correo, un informe, una tabla…) y suele tener el mismo formato?
   - ¿Cuánto tiempo te lleva?

   Si no se le ocurre ninguna, propón 2–3 ejemplos de su profesión (la conoces por sus reglas), aprovechando las herramientas que tiene conectadas. Una buena candidata se hace a menudo, sigue los mismos pasos, da un resultado parecido y tiene poco riesgo si sale mal. Si propone varias, que elija una. Si ninguna encaja, díselo y cierra el módulo sin crear nada.
5. **Comprueba que es una skill.** Si en realidad es cómo quiere que respondas en general, ofrece añadirlo a sus reglas o a su proyecto y, después, buscar otra tarea. Si no quiere, cierra el módulo.
6. **Busca si ya existe** (ver "Buscar skills hechas"). Si hay alguna que encaje bien, enséñale hasta 5, con una línea cada una sobre qué hace. Si elige una, ayúdale a instalarla y salta a la prueba (paso 10). Si ninguna encaja bien, díselo y sigue.
7. **Instala o activa el creador oficial** de su plataforma (ver "Creador oficial" y la ruta en [`rutas.md`](rutas.md)). Comprueba primero si ya lo tiene; si no, explícale en una frase para qué sirve, sin tecnicismos ("la propia app tiene un asistente para enseñarme tareas nuevas; con él queda mejor hecha") y ofrécele instalarlo. Si lo puedes instalar tú, hazlo tras su confirmación; si no, dale los pasos en una lista.
   - Si no quiere instalarlo, adviértele en llano antes de seguir: lo prepararás tú, pero puede que no se active siempre que debería o que haya que retocarlo más, y tendrá que guardarlo la persona. Sigue solo si lo acepta.
8. **Describe la tarea con un caso real.** Pide un ejemplo de una vez anterior: qué recibe, qué pasos sigue, qué entrega y qué hace que el resultado sea bueno. Pídele que quite los datos personales de clientes o terceros. Resume lo que te cuente y enséñaselo hasta que lo apruebe.
   - Alternativa en ChatGPT escritorio o Codex en un Mac: si la tarea es más fácil de enseñar que de explicar, puede enseñármela haciéndola mientras se graba (**Record & Replay**; ruta en `rutas.md`; necesita el uso del ordenador activado). Recuérdale que grabe solo la tarea y evite datos sensibles.
9. **Crea la skill con el creador oficial**, en esta misma conversación, pasándole el resumen aprobado. Si no quiso instalarlo o no está disponible en esta conversación, redacta tú la skill siguiendo la guía oficial de buenas prácticas de tu plataforma (enlace en `rutas.md`, apartado "Fuentes"): una sola tarea por skill; una descripción clara de qué hace y cuándo usarla; pasos concretos con lo que recibe y lo que entrega.

   Antes de guardar, enséñale el nombre, cuándo se activará y los pasos, y guarda solo cuando confirme. Si puedes guardarla tú (por ejemplo, en su carpeta de skills), dile dónde y hazlo; si no, guíale para guardarla (ver `rutas.md`).
10. **Prueba:** que abra una conversación nueva, pida la tarea con sus propias palabras (sin decir el nombre que le hemos dado), y vuelva a esta conversación para contarte si se activó y si el resultado le sirve. Si no se activa o falla, ajustadla aquí y repetid.

## Dónde se puede
| Plataforma | Skills propias | Creador oficial |
|---|---|---|
| Claude (web y escritorio) | Sí, en todos los planes, con la ejecución de código activada | skill-creator, que se activa en la sección de skills |
| Claude Code | Sí | skill-creator, si está instalado; si no, la guía oficial |
| ChatGPT (app de escritorio) y Codex | Sí | `@skill-creator` en ChatGPT Work; `$skill-creator` en Codex |
| ChatGPT web y móvil | No: solo las que vienen dentro de plugins | — |
| Otras herramientas | Según la herramienta; si no lo sabes, dilo | — |

## Creador oficial
| Plataforma | Cómo se consigue |
|---|---|
| Claude (web y escritorio) | Viene incluido, pero desactivado: hay que activarlo en la sección de skills |
| Claude Code | Se instala como plugin del marketplace oficial de Anthropic |
| ChatGPT (app de escritorio, Work) y Codex | Viene incluido |

## Buscar skills hechas
Busca con su profesión y la tarea elegida, en este orden:
1. Con las herramientas de tu app, si puedes buscar en su directorio de plugins o skills.
2. En el catálogo oficial de tu plataforma ([`rutas.md`](rutas.md)) y en el marketplace del Coach IA (https://github.com/Medu-coder/ai-adoption, lista en su README).
3. Si no puedes buscar, dale la ruta del directorio y qué términos buscar.

Solo catálogos oficiales y el del Coach IA. No inventes nombres ni funciones. Muchos plugins están pensados para programadores: propón solo los que encajen de verdad con su tarea. Instala solo si confirma.

## Cierre del módulo
Haz el cierre de la skill (apartado "Al cerrar un módulo"). Incluye las herramientas conectadas en este módulo (tabla del paso 3, sin repetirla), qué skill quedó creada o instalada y cómo se activa (basta con pedir la tarea; también puede llamarla por su nombre). Sugiere pulirla tras usarla 2 o 3 veces: basta con volver aquí y contar qué cambiaría.
