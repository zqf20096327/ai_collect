# BioRAG — Memoria Cognitiva Biomimética y Simbólica para Agentes de IA

> [!IMPORTANT]
> **Repositorio de desarrollo (DEV):** `MemoryBioRAG` es el repositorio principal de desarrollo activo. La versión de trabajo y sus características vigentes pueden incluir cambios aún en curso y no constituyen por sí solos una publicación estable.  
> Para consultar o descargar la distribución estable, visita el **[repositorio MemoryBioRAG-Stable ↗](https://github.com/dennysjmarquez/MemoryBioRAG-Stable)**.

**BioRAG** es una memoria simbólica persistente para agentes de IA que aborda la pérdida de contexto entre sesiones mediante recuperación híbrida. “Biomimética” describe una inspiración de diseño; no significa que el motor simule literalmente un cerebro humano. Los resultados de rendimiento se limitan a los benchmarks y snapshots indicados.

> **Versión del código:** v36.0 (cierre técnico en `master`, tag `v36.0`). La publicación a `MemoryBioRAG-Stable` se gestiona mediante el pipeline de staging y release.
> **Paradigma:** Motor Python + SQLite FTS5. **Sin embeddings densos, GPU ni llamadas a APIs externas** en el path de búsqueda.
> **Motor:** Arquitectura modularizada (18 submódulos `core/memory/` + 15 submódulos `core/mcp_server/` + fachada delgada) + SQLite FTS5 WAL + PPMI-SVD (100 dimensiones) + espacio semántico de 13 ejes + grafo sináptico Hebbiano + SDM (2048 bits) + calibración conforme + activación ACT-R + Concept Hubs + validación simétrica fail-fast de sustantivos clave + **neurona de reordenamiento que aprende sola** (29 señales → 6 ocultas → 1 corrección, con piso en la fórmula a mano) + **neurona asociativa cerrada de fábrica** (5 agujas → fuerza 0–1: ¿dos recuerdos tienen que ver?; examinada, aún no decide en el motor) + enlaces del agente intocables + **destino canónico del córtex en `~/.biorag/`** + **instalador de configuración MCP para clientes compatibles**.
> **Idiomas:** Español e inglés (stemming bilingüe, expansión simbólica con WordNet, Concept Hubs de 5 ángulos y Domain Dict).

---

## 📊 Resultados históricos de la suite oficial (baseline v33.0 · 2026-10-14)

> **v34.0:** con una DB nueva, o sin campeón, la neurona no actúa y estos números se mantienen **idénticos** (son el piso). Con el campeón ya aprendido sobre la copia del snapshot (`despertar_neurona.sh`, 500 ciclos), la misma suite da **Recall@5 100.00 % · Recall@1 94.06 % (823/875) · MRR 0.964 · FP 0/40**, sin ninguna categoría por debajo del piso. Detalle en [La Neurona de BioRAG](#-novedades-de-la-versión-v340--la-neurona-de-biorag).
>
> **v35.0:** la QA oficial sale **idéntica** antes y después de todos los cambios de la v35 (Recall@5 100.00 % · Recall@1 91.89 % · MRR 0.950 · FP 0/40, misma máquina y semilla). Detalle en [La Neurona Asociativa](#-novedades-de-la-versión-v350--la-neurona-asociativa-sináptica).
>
> **Validación de v36.0 en copias temporales:** no se usó la DB viva. El recuento de pytest procede de una corrida aislada registrada previamente; la QA oficial se repitió sobre una copia fresca del snapshot durante esta revisión.
> - **Pruebas unitarias (registro previo):** `PYTHONHASHSEED=0 python -m pytest tests/` — 852 passed, 18 skipped (870 recopilados; 240.19 s), Python 3.11.2.
> - **QA oficial (re-ejecución aislada):** `bash scripts/run_qa_suite.sh --qa-only`, con `BIORAG_QA_GATE=1` y `PYTHONHASHSEED` sin fijar — 921 casos (875 de recuperación, 40 negativos y 6 ambiguos fuera del denominador global). R@5 **100.00% (875/875)**, R@1 **93.03% (814/875)**, MRR **0.9566**, FP **0/40**; `[GATE] OK` (719.53 s). El artefacto de esta corrida está en `scripts/qa_metrics.json`.
> - La copia medida no tenía un campeón de la neurona de ranking, así que esta no actuó. El archivo aislado `scripts/casos_fallidos.jsonl` contiene dos entradas de categoría `ambiguo`, aparte de las métricas globales de recuperación.
> - El snapshot de referencia es `snapshots/qa_escape_qcr_20260811.db` (SHA-256 `104dd2902aaf24c3ce93624492ea95a719acbdcca50f4f6bc123ac8317749796`); la QA se ejecutó sobre una copia temporal. La tabla siguiente conserva métricas históricas del baseline v33.0, no resultados de v36.0. La integración y el tag de v36.0 en `master` siguen pendientes.
>
> **Cada base tiene su propia neurona.** La neurona aprende con los recuerdos de la base donde vive y se guarda dentro de ella. Esta tabla mide una copia del snapshot oficial, que no trae neurona entrenada: por eso muestra la fórmula a mano sola (el piso), aunque tu neurona esté trabajando en tu DB viva. La QA ahora lo dice antes de medir y nombra el parámetro para verla: `python scripts/evaluar_qa.py --con-neurona`. Detalle en [La neurona en la QA](#la-neurona-en-la-qa-cada-base-tiene-la-suya).

Evaluación sobre el snapshot congelado oficial canónico (**921 casos totales en suite QA**):
- **Archivo:** `snapshots/qa_escape_qcr_20260811.db`
- **SHA-256:** `104dd2902aaf24c3ce93624492ea95a719acbdcca50f4f6bc123ac8317749796` (Git blob `ecc15b7513ff6ddd1356e934a0aa13821337bca4`).
- **Composición del dataset:** **875 consultas de recuperación** evaluadas para Recall y MRR, **40 controles negativos** evaluados para tasa de falsos positivos, y **6 casos ambiguos** (consultas con etiquetas contradictorias) analizados por separado fuera del denominador de recuperación global.

| Métrica | Resultado observado | Contexto y Significado Científico |
|---|---:|---|
| **Recall@5 global** | **100.00% (875/875)** | **100% de cobertura en ventana de trabajo**: todo recuerdo gold ingresa al Top-5 del agente sin fallos de recuperación (0 fallos). |
| **Recall@1 (Top-1)** | **91.77% (803/875)** | **Precisión de primer resultado**: 803 de 875 casos quedan en primer lugar directo (métrica complementaria observada en benchmark). |
| **MRR (Mean Reciprocal Rank)** | **0.950** | Posición recíproca promedio ponderada (0.9497 sin redondear; métrica complementaria observada). |
| **Falsos positivos** | **0/40 (0.00%)** | Calibración conforme efectiva en los 40 controles negativos del benchmark (FP rate observada 0.00%). |
| **Casos ambiguos (contradictorios)** | **6 casos (2 con cobertura parcial)** | Evaluados por separado del Recall global; 2 casos no cubren al menos una de las etiquetas contradictorias. |
| **Pruebas unitarias de v36.0** | **852 passed · 18 skipped** | `PYTHONHASHSEED=0 python -m pytest tests/` en copia aislada (870 recopilados; 240.19 s; Python 3.11.2). Resultado registrado para el cierre. |
| **Smoke de Concept Hub (5 paráfrasis)** | **5/5 TOP-1** | Repetido sobre una copia aislada del snapshot oficial (851 nodos activos, 6 hubs y 30 puentes); evidencia focal, no sustituto de las pruebas de escala. |
| **Abismo léxico (EXP-Q)** | **3/3 Pool · 2/3 Top-5 · 1/3 Top-1** | 3/3 descubiertos en pool de grafo; 2/3 en Top-5 (pos #1 y #4) y 1/3 en Top-1 (pos #1). |
| **Sinónimos · Recall@5 / Recall@1** | **100% (55/55) / 56.36%** | Cobertura total en Top-5; el 43.64% restante queda entre Top-2 y Top-5. |
| **Por tema · Recall@5 / Recall@1** | **100% (65/65) / 63.08%** | Cobertura total en Top-5; ordenamiento Top-1 guiado por Jaccard y PPMI-SVD (MRR: 0.772). |
| **Pregunta natural · R@5 / R@1** | **100% (65/65) / 93.85%** | Alta precisión Top-1 en formulaciones conversacionales. |
| **Cruce de idioma · R@5 / R@1** | **100% (8/8) / 62.50%** | Rescate bilingüe en Top-5; Top-1 asistido por WordNet y Concept Hubs. |
| **Smoke multicampo en DB local** | **Objetivo #2 → #1** | Promoción de `version_actual_biorag` de #2 a #1 por convergencia multicampo. |
| **Tiempo de la evaluación global** | **~877 s** | Ejecución determinista de la suite QA de 921 casos en CPU local (sin GPUs ni APIs). |

> **Aclaración Metodológica — Umbrales de Gate vs. Métricas Observadas:**
> - Los **umbrales formales del Gate** de calidad (`_evaluar_gate()` en `scripts/evaluar_qa.py`) exigen: Recall@5 $\ge$ 97.0%, Fallos $\le$ 24, Tasa de Falsos Positivos $\le$ 15.0%.
> - **Recall@1 (91.77%)** y **MRR (0.9497)** son métricas complementarias observadas en el benchmark sobre este corpus congelado, no umbrales que el gate imponga ni garantías universales para cualquier consulta arbitraria.
> - **R@5 = 100.00% (875/875):** Demuestra empíricamente que el conjunto híbrido (FTS5 BM25 + Sustantivos Clave + Grafo Sináptico Hebbiano + PPMI-SVD + Concept Hubs + Reranker Multicampo) logra **cobertura completa (875/875) dentro de la ventana Top-5 de trabajo del agente en este corpus evaluado**.
> - **R@1 = 91.77% (803/875):** Refleja la precisión exacta del primer candidato. En tareas con solapamiento léxico directo (`literal`, `pregunta_natural`), R@1 supera el 95%–99%. En tareas donde el vocabulario difiere radicalmente (`sinonimo` 56.36%, `por_tema` 63.08%), el sistema ubica el recuerdo dentro del Top-5 pero no siempre en Top-1. R@1 representa el área de optimización continua para el desempate fino sin embeddings densos.

---

## 🛡️ v36.0 — Motor robusto, operación y evaluación

> **Resumen del cierre y estado para integración:** [Cierre técnico de v36.0](docs/CIERRE_VERSION_36.md).
>
> **En una frase:** v36 reúne correcciones acotadas de escala para la búsqueda y los Concept Hubs, herramientas de evaluación y cambios operativos: destino canónico en `~/.biorag/memory_biorag.db`, configuración MCP y daemon opt-in. v35.1, v35.2 y v35.3 no fueron releases publicadas; los rótulos que aún aparezcan en algunos artefactos son referencias de trabajo. Los cambios aceptados se documentan juntos aquí bajo v36.0. Las mediciones se limitan a sus copias y benchmarks; no prometen invariancia universal ni equivalencia literal con un cerebro.

| Pieza | Estado en v36.0 |
|---|---|
| **Recuperación a escala** | Cuatro correcciones para casos concretos de crecimiento: fallback guiado por términos desconocidos, ventanas de candidatos por parecido trigram, límite al escape de dimensiones inferidas y protección de palabras reales contra falsos matches difusos. `BIORAG_ESCALA=1` por defecto; límites y benchmark debajo. |
| **BM25 de referencia** | Cuando las tablas FTS de referencia están disponibles, la expresión BM25 se conserva con independencia de `BIORAG_ESCALA`; ese interruptor apaga solo las ayudas de escala, no todo el ranking ni la búsqueda textual. |
| **Concept Hubs a escala** | Motor `escala` e índice invertido por defecto; pondera la frecuencia de los puentes y compite por recuerdo. Las palabras de función aportan como máximo 1 bit, no abren candidaturas por sí solas y el ángulo `ingenuo` no penaliza. `BIORAG_HUB_ESCALA=0` es una ablación. |
| **Diagnósticos de QA y hub** | `scripts/diagnostico_fallos.py` y `scripts/diagnostico_hub.py` copian la base de entrada a un directorio temporal; no escriben en la base fuente. Pueden generar archivos de informe, así que su salida también debe dirigirse a una ubicación elegida. |
| **QA clásica y honesta** | La QA clásica conserva el gate; el análisis honesto separa etiquetas obsoletas/ambiguas y sus métricas suplementarias. La medición con ruido es una línea distinta y no forma parte de la QA normal registrada aquí. E2c/E2e fueron rechazadas/revertidas, no son funciones activas de v36. |
| **Cortex desacoplado (`~/.biorag/`)** | Ruta canónica de usuario fuera del repo; el instalador intenta migrar la base legacy y, si ya existe destino, crea copias de respaldo antes de resolver el conflicto. `BIORAG_PATH` y el fallback legacy siguen aplicando. |
| **Instalador (`install.py`)** | Automatiza la detección y escritura de configuración para clientes compatibles; el resultado depende del entorno y debe validarse en cada plataforma. |
| **Detección de API OpenCode** | Comprueba los paquetes locales y el schema disponible; si no hay evidencia, usa el fallback definido en código. |
| **QA de neurona de ranking** | `--con-neurona` compara el orden de la fórmula y el de la neurona; si la copia no tiene neurona, pregunta antes de entrenarla sobre esa copia. `--si` permite confirmarlo de forma no interactiva. No entrena en la base original. |
| **Compatibilidad Python** | El paquete requiere Python `>=3.11`; CI contempla Python 3.11 y 3.12. |
| **Transporte Antigravity** | La configuración MCP generada usa `stdio`; esta versión no instala un servicio SSE de systemd. |
| **Control del daemon (`La Hormiguita`)** | `BIORAG_DAEMON_ENABLED=0` por defecto; el servidor MCP solo intenta iniciarlo si se habilita explícitamente. Esto controla el proceso de mantenimiento; no implica borrar asociaciones, apagar SDM ni cambiar su fallback predeterminado. |
| **Comando de parada (`--stop`)** | Solicita `SIGTERM`, espera hasta 30 s y puede recurrir a `SIGKILL` si el proceso no termina. No es una garantía de cierre limpio en todos los casos. |
| **Pruebas unitarias y QA** | Pytest registrado en copia aislada: 852 passed/18 skipped. QA oficial re-ejecutada en copia fresca del snapshot: 921 casos, `[GATE] OK` (R@5 100.00%, R@1 93.03%, MRR 0.9566, FP 0/40); resultados en `scripts/qa_metrics.json`. Ninguna corrida usó la DB viva; el match/tag final queda a cargo del usuario. |

### Evidencia de escala en copias controladas

**Buscador (`BIORAG_NEURONA=0`, `PYTHONHASHSEED=1`, QA de 921 casos).** La comparación emparejada de cada copia, antes y después de las cuatro correcciones, no encontró categorías que bajaran frente a su propio control sin arreglos. Estos son los resultados posteriores a las correcciones:

| Copia | Recuerdos | R@1 | R@5 | MRR | FP |
|---|---:|---:|---:|---:|---:|
| S0 | 866 | 92.57% | 100.00% | 0.954 | 0/40 |
| A640 | 1506 | 93.03% | 99.77% | 0.956 | 0/40 |
| T1000r | 1866 | 92.80% | 99.89% | 0.955 | 0/40 |
| T3000r | ~3866 | 92.57% | 99.54% | 0.953 | 0/40 |

El relleno temático no copiaba las preguntas de la QA. El resultado no garantiza invariancia para toda memoria: siguen documentados empates en consultas de una palabra y dos fallos de ranking en T3000r donde un recuerdo que repite una palabra vence al que cubre todas las palabras de la pregunta. Ver [informe](scripts/experimentos/escala_recall_20261025/README.md), [tabla completa](scripts/experimentos/escala_recall_20261025/tabla_final.txt) y pruebas [`test_escala.py`](tests/test_escala.py) / [`test_escala_motor.py`](tests/test_escala_motor.py).

**Concept Hubs (`BIORAG_NEURONA=0`, `PYTHONHASHSEED=1`, misma QA).** H-mitad y H-todos se construyeron en copias con puentes derivados heurísticamente del contenido, no de paráfrasis redactadas por un agente. La tabla recoge la configuración final, después de neutralizar el multiplicador del ángulo `ingenuo` en 1.0:

| Copia | Hubs | R@1 | R@5 | MRR | Fallos | FP |
|---|---:|---:|---:|---:|---:|---:|
| S0 | 6 | 93.14% | 100.00% | 0.9573 | 0 | 0/40 |
| H-mitad | 436 | 93.03% | 100.00% | 0.9569 | 0 | 0/40 |
| H-todos | 866 | 93.83% | 100.00% | 0.9619 | 0 | 0/40 |

En el diagnóstico de **hub solo** sobre 921 consultas, los errores con confianza ≥0.8 bajaron de 255 a 3 en H-todos y de 216 a 11 en H-mitad; el tiempo medido por consulta pasó de ~593 a ~8 ms y de ~284 a ~4 ms, respectivamente. Es una prueba acotada a esas copias, no una latencia de producción. Límite importante: en H-todos la categoría `sinonimo` bajó en R@1 de 65.45% a 58.18% aunque R@5 subió de 98.18% a 100%; el informe atribuye los casos perdidos a empates que antes se resolvían por orden alfabético. No se oculta esa diferencia. Ver [informe](scripts/experimentos/hub_escala_20261025/README.md) y [resultado final](scripts/experimentos/hub_escala_20261025/tabla_final.txt); las pruebas [`test_hub_escala.py`](tests/test_hub_escala.py) ejercitan competencia sintética de hasta 3.000 hubs.

---

### 1. Aislamiento Físico del Cortex (`~/.biorag/memory_biorag.db`)

Las versiones anteriores podían resolver la base dentro del árbol del proyecto. En esta versión, el destino canónico de una instalación nueva está en `~/.biorag/memory_biorag.db`, lo que reduce la exposición accidental a operaciones sobre el repositorio; no impide que un argumento explícito o `BIORAG_PATH` seleccione otra ubicación.

La implementación actual:
* **Migración legacy:** `install.py` busca `MemoryBioRAG_Data/memory_biorag.db` e intenta `PRAGMA wal_checkpoint(TRUNCATE)`; si el checkpoint falla, emite una advertencia y continúa. Si el destino no existe, mueve la base sin crear primero una copia de respaldo. Si el destino ya existe, copia ambas bases a `~/.biorag/backups/`; luego conserva el destino cuando su tamaño no es menor, o lo reemplaza por la base legacy si esta es mayor. No combina las dos bases ni compara su contenido.
* **Límite de la migración:** el movimiento de `.db`, `-wal` y `-shm` no constituye una transacción atómica de conjunto. No debe describirse como migración atómica ni como garantía absoluta contra pérdida de datos.
* **Resolución de rutas (`core/paths.py`):** argumento explícito → `BIORAG_PATH` → base de usuario existente → base legacy existente → destino predeterminado de usuario.
* **QA:** la QA oficial usa su snapshot de referencia; esta descripción no implica que se haya ejecutado el gate completo para cada árbol de trabajo.

---

### 2. Instalador de configuraciones MCP para clientes compatibles

El instalador `python3 install.py` automatiza la detección y escritura de configuración para las plataformas que reconoce. La instalación y el handshake deben verificarse en cada entorno compatible; el código no garantiza que cualquier cliente o configuración local quede operativo sin intervención.
* **Transporte MCP:** las entradas generadas usan `stdio` (OpenCode tiene un formato de configuración propio).
* **OpenCode:** detecta la API de plugin a partir de paquetes locales y del schema disponible, con un fallback definido en código.
* **Antigravity:** genera una entrada MCP `stdio`; esta versión no instala un servicio SSE ni una unidad de `systemd --user`.
* **Hermes:** incluye un parcheador para la sección `mcp_servers.biorag` en YAML.
* **Otros clientes:** las rutas y claves configuradas están definidas en `install.py`; la existencia de una entrada escrita no sustituye una prueba real de conexión.

---

### 3. Detección de API de OpenCode: Los Tres Guardias en Cascada

En lugar de parsear la salida de texto de `opencode --version` (que puede cambiar de formato entre releases), el instalador inspecciona el contrato real:
1. **Guardia 1 (Módulos instalados en disco):** Comprueba si existe `~/.config/opencode/node_modules/@opencode/plugin` (API v2) o `@opencode-ai/plugin` (API v1 legacy).
2. **Guardia 2 (Schema formal):** Lee el atributo `$schema` de `cli.json` (ej: `https://opencode.ai/v2/cli.json` → API v2).
3. **Guardia 3 (Fallback seguro):** Asume por defecto la versión moderna (v2) para garantizar compatibilidad hacia adelante.

---

### 4. Protocolo de Parada Prudente y Control de La Hormiguita

* **Desactivada por defecto:** `BIORAG_DAEMON_ENABLED=0`. El servidor MCP ya no spawnea procesos de fondo a espaldas del usuario a menos que se configure explícitamente en el entorno (`BIORAG_DAEMON_ENABLED=1`).
* **Nuevo comando CLI `--stop`:**
  ```bash
  python3 graph_maintenance_daemon.py --stop
  ```
* **Parada solicitada con límite:**
  Si el demonio se encuentra a mitad de una transacción reflexiva o podado de sinapsis en SQLite (`self.en_ciclo = True`), la señal `SIGTERM` solicita el cierre ordenado, pero no garantiza que el ciclo termine dentro del timeout. El ciclo en curso puede concluir antes de que venza la espera; si el proceso sigue vivo a los 30 segundos, el código intenta `SIGKILL`, por lo que no se garantiza un cierre limpio en todos los casos. Durante la espera, el comando imprime avisos periódicos.

---

## 🧭 Recorrido de mejora y numeración vigente

El README conserva más abajo el detalle histórico de cada etapa. Este resumen ubica la versión que se cierra y separa lo ya implementado de lo que sigue como plan:

| Versión | Recorrido | Estado |
|---|---|---|
| **v34.0–v34.1** | Se incorporó la neurona que reordena resultados con un piso en la fórmula manual; después se aceleró su aprendizaje en memorias nuevas. | Implementado y descrito en la sección v34. |
| **v35.0** | Se construyó y evaluó por separado la neurona asociativa; no se conectó al ranking. También se protegieron los enlaces hechos por el agente. | Cerrado con los límites y experimentos descritos en la sección v35. |
| **v36.0** | Cierre técnico declarado: correcciones acotadas de escala en búsqueda y Concept Hubs, diagnósticos y QA, ruta de datos de usuario, instalador MCP, control explícito del daemon y compatibilidad Python `>=3.11`. La evidencia se separa por benchmark y se obtuvo en copias aisladas. | **Base previa a v37/v38.** E3 sigue abierta; E4 y modularización fase 2 no están verificadas. Estos pendientes no se presentan como completados. El usuario hará el match y gestionará el tag; no se hizo merge ni publicación en `master`. |
| **v37 — plan** | Memoria episódica + recuperación por intención (el plan que antes llevaba el número v36). | Propuesta futura, no parte de v36 ni una capacidad ya implementada como episodios persistentes. BioRAG ya tiene señales y heurísticas temporales; la propuesta debe demostrar qué mejora adicional aporta y preservar el ranking en consultas sin intención temporal. |
| **v38 — etapa posterior** | Trabajo neuronal que anteriormente se había rotulado v37. | Etapa posterior; no forma parte del cierre v36 ni se presenta aquí como implementada. |

**En resumen:** la numeración vigente es **v36.0 (cierre actual) → v37 (plan episódico/intencional) → v38 (trabajo neuronal posterior)**. Los números y planes no equivalen por sí solos a una publicación ni a implementación.

---

## 🧬 Novedades de la Versión v35.0 — La Neurona Asociativa (sináptica)

<p align="center">
  <img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/neurona_asociativa_biorag.jpg" alt="La neurona asociativa de BioRAG: un cuerpo dentro de la silueta de un hipocampo, cinco dendritas que tocan dos recuerdos y un puente de luz que nace entre ellos" width="100%">
</p>
<p align="center"><em>La neurona asociativa de BioRAG (ilustración). El cuerpo vive dentro de la silueta de un hipocampo, la parte del cerebro que decide qué se une con qué. Sus cinco dendritas (oro: el texto; celeste: el tiempo; verde: las etiquetas) tocan dos recuerdos. Arriba nace la sinapsis entre ellos. Los hilos grises del fondo son las conexiones con ruido que la neurona sabe reconocer.</em></p>

> **En una frase:** BioRAG ya tiene su **segunda neurona**. Mira dos recuerdos y responde una sola pregunta: **¿de verdad tienen que ver?** Nace calibrada de fábrica, no aprende de tu memoria, decide en tiempo constante y **ya está examinada**, también por una persona a mano.

**Estado honesto al cerrar la v35.** La neurona está **construida, calibrada, examinada y cerrada**, pero **todavía no decide nada dentro del motor**:
- Se probó que pusiera el peso de nacimiento de cada sinapsis (`dd85fcf`). La búsqueda dio exactamente igual, así que **se revirtió** (`76fe11c`).
- Se probó en una simulación que cortara sinapsis al nacer. **Baja el recall con cualquier umbral**, así que se descartó.
- Su lugar natural, ya medido en una copia, es **elegir qué asociaciones ve el agente**. Queda para la próxima versión, medido antes y después.

La v35 sí cambia dos cosas en el motor (ver [Otros cambios de la v35.0](#otros-cambios-de-la-v350)):
- los **enlaces que hace el agente** ya **no los borra nunca** el sistema;
- el servidor MCP **ya no le sugiere** al agente qué vincular ni qué desvincular.

| Pieza | Estado en v35.0 |
|---|---|
| Neurona asociativa (`core/neurona_asociativa.py`) | ✅ Construida, cerrada (no aprende), con pruebas propias |
| ¿Decide dentro del motor? | ⏸️ Todavía no. Probado y revertido (peso); probado y descartado (cortar) |
| Enlaces del agente (`manual`, `manual_v7`) | ✅ **Intocables** para el sistema; solo `desvincular` los borra |
| Sugerencias MCP de vincular / desvincular | ✅ **Quitadas** (las herramientas `vincular` y `desvincular` siguen) |
| QA oficial antes y después de todos los cambios | ✅ **Idéntica**: Recall@5 100.00 % · Recall@1 91.89 % · MRR 0.950 · FP 0/40 · `[GATE] OK` |
| Pruebas | ✅ **430/430** |

![El viaje de la neurona asociativa](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/figuras/02_el_viaje.png)

### 1. Por qué existe

BioRAG guarda recuerdos y los **une** con sinapsis (el grafo). En la memoria de Dennys hay **851 recuerdos activos y 13,342 conexiones**. Casi todas las crean **cinco reglas automáticas**:

| Regla automática | Sinapsis que creó |
|---|---:|
| `sinonimo_explicito` (comparten un sinónimo) | 5,863 (42 %) |
| `pmi_hebbiano` (aparecen juntas) | 2,359 |
| `co_ocurrencia` | 2,108 |
| `co_nombre` (se parecen en el nombre) | 1,558 |
| `co_semantica` | 1,226 |

Esas reglas unen por coincidencias. Ninguna se pregunta **si los dos recuerdos de verdad tienen que ver**. Lo medimos de tres formas:

1. **Examen a mano.** Dennys juzgó 99 pares de su memoria. Entre las sinapsis automáticas, cerca del **45 % son buenas** (margen 32–59 %). Más o menos la mitad es ruido.
2. **El peso de hoy no separa nada.** Con el peso que reciben hoy, los 381 enlaces hechos por personas quedan **por debajo** del resto (AUC **0.271**, peor que tirar una moneda).
3. **El único juez hoy es la hormiguita**, que le pregunta a Gemini. Es una API externa: cuesta dinero, necesita internet, puede responder distinto ante el mismo par y además se equivoca. De 15 pares que Gemini sacó, Dennys dijo que **6 sí tenían que ver**.

**En el cerebro**, quien decide qué se une con qué es el **hipocampo**. Funciona por partes:
- la **corteza entorrinal** le trae las señales;
- el **giro dentado** separa lo que se parece pero no es lo mismo;
- **CA3** guarda la red de asociaciones;
- **CA1** compara y decide.

BioRAG ya tenía la entrada (las señales) y la red (el grafo y la SDM). **Le faltaba el juez.** Esta neurona es ese juez.

![De tu hipocampo a la neurona](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/02_hipocampo.png)

### 2. Qué tipo de neurona es

| Pregunta | Respuesta |
|---|---|
| **Arquitectura** | **Una neurona logística**: 5 entradas ("agujas") → Σ → curva sigmoide → **fuerza** de 0 a 1. Son **6 números** en total (un sesgo y 5 pesos). |
| **Qué responde** | ¿Los recuerdos A y B tienen que ver? `fuerza ≥ 0.6` = sí con confianza; `< 0.6` = dudoso. |
| **De dónde salen sus pesos** | **De fábrica**. Se calibraron a mano sobre **7 memorias públicas** muy distintas (noticias en inglés y en español, un diccionario, relatos, código Python, un chat real y la obra de Machado de Assis en portugués). Cada una trae su propia verdad, por ejemplo "mismo tema" o "misma clase". |
| **Qué aprende de tu memoria** | **Nada.** Es **cerrada**: nace calibrada, como las neuronas con las que nacemos. No memoriza tu memoria ni la de nadie. |
| **Qué sí mide de cada memoria** | Solo lo necesario para leerla: la rareza de cada raíz, un espacio semántico de 100 dimensiones y **dos llaves**. Las llaves dicen si en *esa* memoria el tiempo y las etiquetas coinciden con el texto. Todo se mide solo, sin respuestas correctas. |
| **Idiomas** | Cualquiera. Usa raíces de 7 letras y no tiene listas de palabras de ningún idioma. |
| **Cuánto cuesta** | Cada decisión entre dos recuerdos es de **tiempo constante**: no depende del tamaño de la memoria. El estado se arma una vez sobre un máximo de **2,000 recuerdos** y se rehace cuando la memoria crece un 10 %. Solo usa numpy, sin GPU ni APIs. |
| **Dónde vive** | `core/neurona_asociativa.py` (versión `asoc-1`). Si algún día la llama el motor, guarda su estado en dos tablas propias: `neurona_asociativa_estado` y `neurona_asociativa_raices`. |
| **Interruptor** | `BIORAG_NEURONA_ASOCIATIVA=0` la apaga. En v35 el motor no la llama, así que hoy no cambia nada. |

![La neurona asociativa del motor: cómo decide](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/figuras/01_neurona_del_motor.png)

**La inspiración biológica (es inspiración, no simulación):**

| En el cerebro | En la neurona asociativa |
|---|---|
| Corteza entorrinal (trae la información) | Las **agujas**: lo que se mide del par |
| Giro dentado (separa lo parecido de lo igual) | `rareza_max`: compartir una pista **rara** vale más que compartir una palabra común |
| Corteza (significado) | `parecido` y `semantica` |
| **Células de tiempo** (lo que se vive junto se une) | `episodio`: guardados cerca en el tiempo. Es la aguja que más pesa (×4) |
| Esquemas de la corteza prefrontal | `etiquetas`: dims compartidas |
| CA1 (compara y decide) | El Σ y la curva: la **fuerza** |
| CA3 (la red de asociaciones) | El grafo y la SDM que **ya existían** en BioRAG |
| Homeostasis (no dejar que algo domine todo) | Las **llaves**: el tiempo y las etiquetas valen solo si en esa memoria coinciden con el texto |

### 3. La fórmula: un piso a mano, calibrado y cerrado

```
z      = −1 + 2·parecido + 1·semantica + 1·rareza_max + 4·episodio·llave_tiempo + 1·etiquetas·llave_dims
fuerza = 1 / (1 + e^−z)
```

| Aguja | Pregunta que hace | Peso | Por qué ese peso |
|---|---|---:|---|
| `parecido` | ¿Usan las mismas palabras? (coseno tf-idf de raíces) | 2 | La señal más estable en las 7 memorias |
| `semantica` | ¿Significan lo mismo? (LSA, 100 dimensiones) | 1 | Rescata pares que dicen lo mismo con otras palabras |
| `rareza_max` | ¿Comparten una pista muy rara? | 1 | Compartir "nefrona" dice más que compartir "sistema" |
| `episodio` | ¿Se guardaron cerca en el tiempo? | 4 | Es lo que más pesa en el cerebro. Solo vale si la llave dice que en *esa* memoria el tiempo coincide con el texto (en la de Dennys, la llave vale 0.48). Si pasaron más de 7 días reales, no cuenta. |
| `etiquetas` | ¿Comparten dims? | 1 | Igual, con su propia llave (0.36 en la de Dennys) |

**Un par real, paso a paso.** Es uno de los enlaces que Dennys puso a mano. Casi no comparten palabras (`parecido` 0.04), pero comparten una pista rara (0.50) y se guardaron cerca en el tiempo (0.44, ya pasado por la llave). La suma da z = 1.65, y eso da una **fuerza de 0.84**. A la izquierda se ven las 12 agujas medidas; en la suma entran solo las 5 de la fórmula. La nota de abajo ("top 10") viene de la competencia del experimento, que el motor no usa.

![Un par real, paso a paso](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/03_un_par_paso_a_paso.png)

**Las llaves: cada memoria decide sola si confía en el reloj y en las etiquetas.** La llave compara qué tan parecidos son, por texto, los recuerdos que el reloj (o las etiquetas) junta, contra pares al azar. No usa ninguna respuesta correcta. Si no hay relación, la llave se cierra: con un reloj al azar da casi 0, y una prueba automática lo verifica. Por eso el tiempo cuenta casi entero en un chat (llave 0.74), casi nada en noticias (0.10) y a la mitad en la memoria de Dennys (0.48).

![Las llaves de auto-regulación](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/06_auto_regulacion.png)

Se midieron **12 agujas**. Solo 5 entran en la fórmula, porque las otras 7 no ayudaban en las 7 memorias a la vez. También se descartaron, con pruebas:
- **Competencia** (cada recuerdo se queda con sus K socios más fuertes): conserva pares débiles y suelta buenos.
- **Coacceso** (recuerdos que se piden juntos): AUC 0.459, no separa.

La neurona **tiene una parte que puede aprender, pero queda apagada.** Probamos una corrección aprendida sobre la fórmula:
- con cada memoria por separado ganaba hasta +4.55 puntos;
- con todas juntas, lo que una ganaba otra lo perdía (la "balanza").

Para servir en cualquier memoria, **la fórmula a mano es mejor**. La corrección queda en escala 0, por decisión de Dennys: la neurona asociativa **no aprende**.

![El banco de agujas](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/04_banco_agujas.png)

![La balanza: por qué la parte que aprende queda apagada](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/11_balanza_aprender.png)

### 4. Cómo se examinó

**4.1. En memorias que nunca vio.** Para cada memoria se volvió a calibrar la fórmula **sin mirarla** (con las otras 6) y después se le tomó examen. La AUC es la probabilidad de que un par que sí tiene que ver saque más fuerza que uno que no: 0.5 es azar y 1.0 es perfecto.

| Memoria | Idioma | Pares | Sí tienen que ver | Regla simple (Jaccard) | **Neurona** |
|---|---|---:|---:|---:|---:|
| noticias (Reuters) | en | 47,175 | 26.5 % | 0.834 | **0.882** |
| diccionario (WordNet) | en | 40,225 | 2.9 % | 0.843 | **0.902** |
| relatos (Brown) | en | 27,195 | 5.8 % | 0.915 | **0.994** |
| código (librería de Python) | Python | 31,223 | 6.9 % | 0.900 | **0.927** |
| chat real (NPS) | en | 24,746 | 23.2 % | 0.627 | **0.911** |
| noticias (EFE) | es | 16,359 | 6.4 % | 0.915 | **0.997** |
| Machado de Assis | pt | 25,782 | 8.9 % | 0.758 | **0.962** |

Promedio **0.939**; el peor caso es **0.882**. En las 7 memorias, la neurona supera a la regla simple.

![Examen en memorias nunca vistas](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/07_examen_nunca_vista.png)

**4.2. En la memoria real de Dennys, que tampoco vio.** En la DB hay dos jueces: lo que unió una persona o el agente (381 enlaces) y lo que juzgó Gemini.

| Prueba | Peso de hoy | **Neurona** |
|---|---:|---:|
| Enlaces humanos vs el resto (AUC) | 0.271 | **0.868** |
| Enlaces humanos vs lo que Gemini sacó (AUC) | — | **0.930** |
| Fuerza típica (mediana): humanos / Gemini confirmó / Gemini sacó | — | **0.75** / 0.45 / 0.40 |

![Tu memoria: tres jueces](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/08_tu_memoria_tres_jueces.png)

**La huella:** para cada aguja, el valor típico de los enlaces humanos (verde) y el de lo que Gemini sacó (rojo). Cuanto más larga la barra, más ayuda esa aguja a distinguirlos. Las que más separan son `pistas_raras`, `mutuo` y `semantica`.

![La huella en tu memoria](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/05_huella_en_tu_memoria.png)

**4.3. Examen a mano.** Dennys leyó los 100 pares con el texto completo de cada recuerdo y contestó 99.

| Resultado | Valor |
|---|---|
| AUC de la fuerza en los 99 pares | **0.73** (margen 0.62–0.83) |
| Pares con fuerza **≥ 0.6** | 31 «sí» de 42 (74 %) |
| Pares con fuerza **< 0.6** | 16 «sí» de 44 (36 %) |
| Sinapsis que **ya existen** con fuerza ≥ 0.6 | **13 buenas, 1 mala** |
| Sinapsis existentes: neurona vs peso de hoy (AUC) | **0.77** vs 0.63 |
| Pares que **no existen** y la neurona propone | **12 «sí» de 15** (80 %) |
| Sinapsis automáticas buenas (estimado) | ~45 % (32–59 %) |

La neurona no es perfecta, pero **juzga como una persona mucho mejor que el peso de hoy**, y encuentra enlaces buenos que hoy no existen.

### 5. Qué se probó dentro del motor, y por qué hoy no decide

Todo se midió con la QA oficial (875 búsquedas), en **copias** del snapshot. Nunca se tocó la DB real.

**5.1. Poner el peso de nacimiento (experimento 12) → revertido.** Con la neurona fijando el peso de cada sinapsis nueva, la QA salió **idéntica**, incluso repesando todas las sinapsis automáticas de una copia. La búsqueda casi no mira ese peso. Ordenar mejor los enlaces no es buscar mejor. Como no se podía demostrar una mejora, Dennys pidió revertirlo (`76fe11c`).

**5.2. Cortar sinapsis al nacer (experimento 13) → descartado.** Se simuló la neurona dejando nacer solo las sinapsis con fuerza suficiente, con la hormiguita apagada:

| Escenario | Sinapsis automáticas | Recall@5 | Recall@1 | MRR | Fallos | Pares del examen que quedan (buenos / malos) |
|---|---:|---:|---:|---:|---:|---|
| Hoy (con hormiguita) | 13,114 | **100.00 %** | 91.89 % | 0.950 | 0 | 26 / 29 |
| Hormiguita apagada | 15,864 | **100.00 %** | **92.00 %** | **0.951** | 0 | 30 / 36 |
| La neurona corta < 0.40 | 10,261 | 99.89 % | 91.77 % | 0.949 | 1 | 27 / 28 |
| La neurona corta < 0.50 | 3,847 | 99.66 % | 91.77 % | 0.948 | 3 | 18 / 11 |
| La neurona corta < 0.60 | 1,684 | 99.43 % | 91.66 % | 0.947 | 5 | 15 / 8 |
| Sin sinapsis automáticas | 0 | 99.43 % | 91.77 % | 0.948 | 5 | — |

![¿El ruido ayuda a buscar?](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/figuras/03_el_ruido_y_la_busqueda.png)

Lo que enseñó:
- **El "ruido" ayuda a buscar.** Sin las sinapsis automáticas se pierden 5 búsquedas.
- **Cortar baja el recall con cualquier umbral.** La regla de BioRAG es que el recall nunca baja, así que la neurona **no debe borrar**.
- **Apagar la hormiguita no bajó nada** (incluso sube un poco el primer puesto: por tema pasa de 63.08 % a 64.62 %). Es una simulación; la hormiguita **sigue igual en v35**.

**5.3. Su lugar: lo que ve el agente (medido, todavía no aplicado).** Junto a cada resultado, BioRAG le muestra al agente las **asociaciones** del recuerdo (el "canal 2"). Eso **no toca el ranking**. Si la neurona eligiera cuáles mostrar:

| Asociaciones mostradas | Total | Automáticas | Del agente | Recuerdos sin vecinos | Pares del examen visibles (buenos / malos) |
|---|---:|---:|---:|---:|---|
| Hoy | 3,173 | 2,466 | 691 | 22 | 5 / 8 |
| La neurona filtra ≥ 0.50 | 2,588 | 1,876 | 694 | 103 | **9 / 1** |
| La neurona filtra ≥ 0.60 | 2,024 | 1,303 | 698 | 225 | 10 / 1 |

![Lo que ve el agente](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/figuras/04_lo_que_ve_el_agente.png)

La muestra es chica (10 a 13 pares) y parte del examen se eligió con la fuerza de la neurona. Es una **señal**, no una prueba firme. Por eso queda como el **próximo paso**, con su propia medición.

### 6. Por qué debe existir

El mapa muestra lo que funciona hoy (línea llena) y los tres lugares donde la neurona puede entrar (línea punteada violeta). Ninguno está hecho todavía; irán de a uno. El ranking no se toca.

![Dónde va la neurona asociativa en el motor](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/figuras/05_donde_va_en_el_motor.png)

1. **Para quitar a Gemini del grafo.** Hoy la limpieza depende de una API externa que cuesta, necesita internet y no siempre responde lo mismo. La neurona es local, gratis, determinista y de tiempo constante. Además separa los enlaces humanos de lo que Gemini sacó con AUC **0.930**.
2. **Para que el agente vea asociaciones buenas.** Hoy, de los pares del examen que el agente llega a ver, hay más malos que buenos (5 / 8). Con la neurona filtrando, 9 / 1.
3. **Para proponer lo que falta.** El 31 % de los enlaces humanos nunca llega a ser candidato de ninguna regla automática. De los pares que la neurona propuso y no existían, Dennys aprobó el **80 %**.
4. **Para arreglar `vincular_por_sinonimos`**, la regla que más sinapsis crea (42 %). Con sus 5 mejores por recuerdo, la neurona encuentra **148** de los 381 enlaces humanos (fuerza media 0.711). Un arreglo a mano encontraba 122 (0.536).
5. **Porque cualquier memoria la puede usar desde el día uno.** Viene calibrada de fábrica y no necesita QA, ni respuestas correctas, ni entrenamiento. Sirve para una DB vacía de un tercero.

Cada uno de estos pasos irá **por separado**: un cambio a la vez, con la QA antes y después, y la regla de que el recall nunca baja.

### Otros cambios de la v35.0

**Los enlaces del agente son intocables (`8c7d476`).** Lo que une el agente (`vincular`, o `vincular_con` en `aprender`/`guardar`; tipos `manual` y `manual_v7`) es una decisión informada: el agente buscó antes de guardar (`busqueda_previa`). Antes, 9 de esos enlaces habían bajado de 0.5 por el decaimiento. Ahora el sistema los salta en todos los procesos que pueden debilitar o borrar:

| Proceso | Antes | v35 |
|---|---|---|
| Decaimiento del peso | Bajaba | No los toca |
| Borrado por peso < 0.05 | Podía borrarlos | No los toca |
| Poda LTD guiada | Podía podarlos | No los toca |
| Hormiguita: prefiltro, cuarentena, borrar o repesar | Podía sacarlos | No los toca |
| `desvincular` (el agente lo pide) | Borra | **Borra** (la decisión sigue siendo del agente) |

**El MCP ya no sugiere qué vincular ni qué desvincular (`0182ad4`).** Se quitaron los mensajes que empujaban al agente a crear o borrar enlaces. Las herramientas `vincular` y `desvincular` siguen en el MCP, y `vincular_con` en `aprender` no cambió. El agente decide solo, con lo que encontró en su búsqueda previa.

**Pruebas nuevas:**
- `tests/test_neurona_asociativa_motor.py` (fiel al experimento 11, costo constante, techo de la muestra y que guardar sigue usando los pesos a mano);
- `tests/test_enlaces_del_agente_intocables.py` (9 pruebas);
- `tests/test_sin_sugerencias_de_enlace.py` (4 pruebas).

Total: **430/430**. La QA oficial quedó **idéntica** antes y después de todos los cambios v35, con el mismo snapshot y la misma semilla (`PYTHONHASHSEED=1`).

### Límites (lo que no está probado)

- Se calibró con 7 memorias públicas y se examinó con **una** memoria personal. Faltan más memorias reales.
- El examen a mano lo hizo **una persona** con 99 pares. Parte de los pares se eligió con la propia fuerza de la neurona, lo que puede favorecerla.
- La QA oficial mide si el recuerdo correcto sale en la búsqueda, **no** la calidad de las asociaciones ni el peso. Por eso el experimento 12 salió "igual".
- Lo de la hormiguita apagada y el filtro del canal 2 se midió **en copias**. Ninguno está en el motor.
- No se comparó todavía *agente + BioRAG* contra *agente + base de datos vectorial*.
- El hipocampo es **inspiración**, no simulación.

Lo que ya tiene y lo que todavía le falta, medido y no supuesto. El 69 % de los enlaces humanos la neurona los propondría sola; el 31 % restante ni siquiera llega a ser candidato de ninguna regla:

![Lo que todavía le falta](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/figuras/12_lo_que_falta.png)

### Dónde está todo

| Qué | Dónde |
|---|---|
| Diseño: el molde y dónde nacen las sinapsis | [Experimento 10 — Neuronas del motor](docs/Mi%20neurona%20en%20el%20sistema/experimento_10_neuronas_del_motor/) |
| Construcción, calibración, exámenes y las 12 figuras | [Experimento 11 — La neurona asociativa](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/) |
| Peso de nacimiento (revertido) | [Experimento 12 — La neurona en el motor](docs/Mi%20neurona%20en%20el%20sistema/experimento_12_neurona_en_el_motor/) |
| Enlaces del agente, ruido, cortar al nacer, canal 2 y cierre | [Experimento 13 — Enlaces del agente y ruido](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/) |
| La neurona | `core/neurona_asociativa.py` |

Las figuras se redibujan sin ninguna DB:
- `python dibujar.py` en la carpeta del experimento 11;
- `python dibujar.py` en la carpeta del experimento 13.

**Con esto, el tema de la neurona asociativa queda cerrado en la v35.**

---

## 🌱 Novedades de la Versión v34.1 — La neurona aprende sola de verdad

> **En una frase:** con v34.0, una memoria **nueva** casi nunca llegaba a encender la neurona. Con v34.1 lo logra en unas **20 consolidaciones**, sin perder nada en la QA oficial.

### Cuánto tarda en aprender sola (v34.1)

La neurona practica **1 vez por cada consolidación** de la memoria (`consolidar`, `sueno` o cerrar sesión con `contexto_fin`). `aprender` deja el recuerdo en corto plazo y todavía no cuenta: 10 `aprender` + 1 `consolidar` = 1 práctica.

En v34.0 cada práctica hacía **2 preguntas a 2 recuerdos**: usaba 0.4 s de los 3 s que tiene permitidos. Medido con una memoria nueva que crece (5 recuerdos y 1 consolidación por sesión), en 80 sesiones juntó 20 preguntas de estudio y 7 de control. Necesita 150 y 40, así que **nunca** se encendía.

v34.1 cambia solo **qué practica en cada consolidación**:

1. **Usa el tiempo que ya tenía:** hasta **8 recuerdos × 7 preguntas**, siempre dentro de los mismos **3 s**. El costo sigue fijo: no crece con el tamaño de la memoria.
2. **Pregunta a lo ancho:** primero la 1.ª pregunta de los 8 recuerdos, luego la 2.ª de los 8... Si los 3 s se acaban (memoria grande, búsquedas más lentas), las preguntas quedan repartidas entre muchos recuerdos distintos y no amontonadas en dos. Así conoce más recuerdos y no se acostumbra a pocos.
3. **Repasa primero lo que le falta:** al elegir recuerdos al azar, empieza por el grupo del examen (estudio o control) al que más le faltan preguntas.

| Memoria nueva, 5 recuerdos por sesión | v34.0 | **v34.1** |
|---|---|---|
| Examen listo (150 estudio + 40 control) | nunca | **sesión 16** |
| La neurona empieza a trabajar | nunca | **sesión 21** |
| Sesiones trabajando (de 80) | 0 | **60** (0 retiros) |
| Tiempo por consolidación | 0.65 s | 2.15 s (tope 3 s) |

**¿Se pierde algo? No.** QA oficial sobre una copia del snapshot, con el mismo número de prácticas (561):

| | R@5 | R@1 | MRR | FP | Agente (MCP) R@1 / R@5 |
|---|---|---|---|---|---|
| Fórmula a mano (piso) | 99.89 | 91.66 | .949 | 0/40 | 92.34 / 99.09 |
| v34.0 | 100 | 94.86 | .969 | 0/40 | 94.97 / 99.54 |
| **v34.1** | **100** | **94.74** | **.968** | **0/40** | **94.74 / 99.54** |

La diferencia es 1 caso de 875, el ruido normal entre dos entrenamientos. Ninguna categoría queda por debajo de la fórmula y el GATE da OK.

**Lo honesto:**
- **Primer intento descartado:** el primer diseño (8 × 7 preguntando recuerdo por recuerdo) bajó la QA a R@1 93.26: conocía un tercio menos de recuerdos. De ahí sale "a lo ancho".
- **Memoria muy chica:** con solo 2 recuerdos por sesión, el motor duerme los que no se usan y quedan ~25 despiertos. Con tan pocos la fórmula alcanza y la neurona no se enciende, que es lo correcto.
- **Despertar:** a igual tiempo hace menos prácticas (cada una usa sus 3 s). `despertar_neurona.sh` mantiene su default de 500 prácticas (ahora ~22 min con ~900 recuerdos).

Todo el detalle, con las salidas textuales: [Experimento 09 — Que aprenda sola de verdad](docs/Mi%20neurona%20en%20el%20sistema/experimento_09_aprende_sola_de_verdad/). Pruebas nuevas en `tests/test_neurona.py`: preferencia por el grupo que falta, recién consolidados primero y nunca dormidos, costo fijo al elegir (DB de 50 o 50 000 recuerdos) y preguntas a lo ancho.

---

## 🧠 Novedades de la Versión v34.0 — La Neurona de BioRAG

<p align="center">
  <img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/neurona_biorag.jpg" alt="La neurona de BioRAG: 29 agujas que convergen en un cuerpo con 6 neuronas ocultas, protegido por un escudo, cuyo axón ordena los resultados" width="100%">
</p>
<p align="center"><em>La neurona de BioRAG (ilustración). Agujas doradas: las señales de la fórmula. Agujas celestes: lo que aporta el agente. Los seis orbes: las neuronas ocultas. El escudo: las capas de protección. Las tarjetas: los resultados que ordena.</em></p>

> **En una frase:** BioRAG ahora tiene una pequeña neurona que **aprende sola, mientras se usa, a ordenar mejor los primeros resultados**. Empieza siendo exactamente la fórmula a mano y **nunca puede quedar por debajo de ella**.

La versión **v34.0** es mayor porque cambia el **comportamiento del ranking**: por primera vez una pieza aprendida puede mover el orden de lo que recibe el agente. También cambian tres valores por defecto del servidor MCP (ver [Otros cambios de la v34.0](#otros-cambios-de-la-v340)). La API no se rompe: las llamadas MCP son las mismas.

### 1. Por qué existe

La fórmula de BioRAG suma 17 señales ("agujas") con **pesos fijos puestos a mano**: BM25 vale 0.25, el Concept Hub 0.20, PPMI 0.15… Esos pesos son buenos en promedio, pero **la importancia de cada aguja depende del contexto**:
- En una búsqueda literal manda BM25.
- En una búsqueda por sinónimo, BM25 casi no aporta y pesan más los sinónimos, el PPMI y el grafo.
- Cuando el agente manda `sustantivos_clave`, la evidencia en ese campo vale más que una coincidencia suelta en el contenido.

Un peso fijo no puede capturar eso. Por eso la fórmula llegaba al Top-5 en el 100 % de los casos, pero el **primer lugar** fallaba en las categorías difíciles: sinónimo 56 %, por tema 63 %.

La neurona aprende **cuánto vale cada aguja según el contexto** y corrige el orden **solo cuando está segura**.

### 2. Qué tipo de neurona es

| Pregunta | Respuesta |
|---|---|
| **Arquitectura** | Perceptrón multicapa chico: **29 entradas → 6 neuronas ocultas (tanh) → 1 salida**. **186 pesos** en total (W 6×29, b 6, v 6). |
| **Qué produce** | Una **corrección residual** c(x) que se **suma** al score de la fórmula. Con c(x) = 0 el motor es idéntico al de siempre: los pesos a mano son el **ancla** y el **piso**. |
| **Qué aprende** | *Learning to rank* por lista: entropía cruzada sobre el softmax del top-k, es decir, "que la respuesta correcta quede primera". |
| **De dónde saca las respuestas correctas** | **Autosupervisión**. Cuando un recuerdo se consolida, la respuesta correcta se conoce: es ese recuerdo. El recuerdo se hace sus propias preguntas y el motor las responde en silencio. |
| **Cuándo aprende** | **Al consolidar** (cuando un recuerdo pasa de corto a largo plazo: `consolidar`, `sueno` o `contexto_fin`), nunca al buscar. Así la búsqueda no paga el entrenamiento. Una práctica por consolidación, sin importar cuántos `aprender` hubo antes. |
| **Cómo decide si lo aprendido sirve** | **Campeón y retador**: el retador estudia; solo reemplaza al campeón si gana en un examen que **nunca estudió** (la guardia) y no daña ninguna categoría. |
| **Cuánto cuesta** | **Fijo por operación**: hasta 8 recuerdos × 7 preguntas por ciclo, siempre dentro de un tope de 3 s, y memoria de examen de tamaño fijo. El costo no crece con el tamaño de la memoria. |
| **Dónde vive** | `core/memory/neurona.py` (la neurona) y `core/memory/neurona_examen.py` (el autoexamen). Su estado se guarda en la tabla `neurona_estado` de la misma DB. |

**La inspiración biológica (es inspiración, no simulación):**

| En el cerebro | En BioRAG |
|---|---|
| Dendritas que reciben señales | Las **29 agujas**: 17 de la fórmula y 12 de lo que pasó después y de lo que aporta el agente |
| Interneuronas | Las **6 neuronas ocultas**, que combinan agujas (por ejemplo: "sinónimo alto + BM25 bajo + vino del agente") |
| Axón que modula | La **corrección** que reordena el top-k |
| Consolidación durante el sueño (*replay* del hipocampo) | Aprende **al consolidar**, repasando recuerdos |
| *Primum non nocere* | El **margen "primero no dañar"** |
| Homeostasis | **Piso** (no bajar de la fórmula) y **techo** (dejar de entrenar cuando ya no mejora y despertar si algo cambia) |

### 3. Anatomía exacta

<p align="center"><img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/anatomia_neurona.png" alt="Anatomía de la neurona: 29 señales con sus nombres, 6 neuronas ocultas tanh, suma de corrección y regla de orden" width="100%"></p>

**Las 17 agujas de la fórmula a mano** (las mismas que suma `_calcular_score_hibrido`):

| Aguja (`código`) | Qué mide |
|---|---|
| BM25 léxico (`bm25_norm`) | Coincidencia de palabras (FTS5), normalizada |
| dimensiones (`dim_score`) | Coincidencia en los 13 ejes semánticos |
| palabras en el nombre (`concepto_ratio`) | Cuánto de la consulta está en el nombre del recuerdo |
| sinónimos (`sinonimos_ratio`) | Cuánto de la consulta está en sus sinónimos |
| latente / cadena (`latcad`) | Conexiones latentes o en cadena del grafo (la mayor de las dos) |
| grupo (`grupo_score`) | Pertenencia a un grupo temático |
| temático (`tematico_g`) | Afinidad temática (solo cuenta si hay evidencia léxica) |
| asociaciones (`asoc`) | Grado en el grafo sináptico (asociaciones / 20, tope 1) |
| predicados (`pred_score`) | Roles semánticos (SRL) |
| PPMI-SVD (`ppmi_score`) | Similitud vectorial PPMI+SVD (100 dims) |
| Concept Hub (`hub_match`) | Coincidencia por puentes de 5 ángulos |
| compresión (`ncd_score`) | Distancia de compresión normalizada |
| episodio (`episodio_score`) | Cercanía temporal (mismo episodio) |
| campo semántico (`campo_score`) | Atracción del campo semántico |
| Jensen-Shannon (`jsd`) | Divergencia de distribuciones |
| match exacto (`match_exacto`) | La consulta es el nombre del recuerdo |
| sinónimo casi exacto (`sin95`) | Sinónimos ≥ 0.95 |

**Las 12 señales de la vista y del agente** (lo que pasa *después* de la fórmula y el contexto de la búsqueda):

| Señal (`código`) | Qué mide |
|---|---|
| bono de convergencia (`bono_conv`) | Bono multicampo que recibió, normalizado (/0.085, tope 1.5) |
| evidencia por campo (`ev_concepto`, `ev_sinonimos`, `ev_sustantivos`, `ev_contenido`) | En qué campos del recuerdo apareció la consulta, incluidos los `sustantivos_clave` |
| peso sináptico (`peso`) | El peso del recuerdo (0–1) |
| ¿score con peso? (`con_peso`) | Si el score servido incluye el peso (camino MCP) |
| ¿vino del agente? (`con_agente`) | Si la búsqueda trae `sustantivos_clave` del agente |
| origen (`or_lexico`, `or_hub`, `or_no_literal`) | Por dónde llegó el candidato: léxico aprendido, Concept Hub o un camino no literal |
| sin rasgos (`sin_rasgos`) | Bandera: candidato inyectado sin pasar por la fórmula (sus 17 agujas van en 0) |

### 4. La matemática, paso a paso

**Símbolos**

| Símbolo | Significado |
|---|---|
| $k$ | Cuántos resultados ve quien busca: 5 por defecto, 10 por el MCP (tope `topk_max` = 10) |
| $x_i \in \mathbb{R}^{29}$ | Las 29 señales del resultado en el puesto $i$ |
| $\text{score}_i$ | El score que la fórmula a mano le dio y que se sirvió |
| $W, b, v$ | Los pesos de la neurona ($6 \times 29$, $6$, $6$) |
| $c(x)$ | La corrección que propone la neurona |
| $\varepsilon$ | El margen "primero no dañar" |
| $y$ | El puesto donde está la respuesta correcta (en el autoexamen) |

**1) La escala de la fórmula.** El score se lleva a logit, que es la escala natural para sumar evidencias. Por encima de 1 se prolonga en recta para que los matches exactos (que superan 1) no se recorten:

$$
g(s)=\begin{cases}\ln\dfrac{s}{1-s} & s<1-\epsilon_0\\[6pt] \ln\dfrac{1-\epsilon_0}{\epsilon_0}+\dfrac{s-(1-\epsilon_0)}{\epsilon_0(1-\epsilon_0)} & s\ge 1-\epsilon_0\end{cases}\qquad \epsilon_0=10^{-4},\quad s\in[10^{-4},\,50]
$$

**2) La corrección de la neurona:**

$$
c(x)=v^{\top}\tanh(Wx+b)
$$

**3) Cómo sirve (reordena el top-k).** Cada resultado del top-k recibe una clave, y el top-k se ordena por esa clave de mayor a menor:

$$
\text{clave}_i \;=\; g(\text{score}_i)\;+\;c(x_i)\;+\;\varepsilon\,(k-i),\qquad i=0,\dots,k-1
$$

El término $\varepsilon(k-i)$ es la **ventaja de la fórmula**: para subir un puesto, la neurona tiene que ganar por más de $\varepsilon$. Después del reorden, **los recuerdos y los scores son los mismos**: el score más alto se le asigna al nuevo primero, el segundo al nuevo segundo, y así. Por eso ningún umbral absoluto del motor (abstención, GABA, ráfaga, certeza, falsos positivos) ve números distintos.

**Regla de identidad:** si la consulta *es* el nombre de un recuerdo (con "_" = espacio) y la fórmula ya lo puso primero, sigue primero.

**4) Cómo aprende.** En el autoexamen se conoce el puesto $y$ de la respuesta correcta. La probabilidad que la neurona le da es un softmax sobre el top-k servido:

$$
p_i=\frac{e^{\,g(\text{score}_i)+c(x_i)}}{\sum_{j<k} e^{\,g(\text{score}_j)+c(x_j)}},\qquad
\mathcal{L}=-\frac{1}{n}\sum_{\text{casos}}\ln p_y\;+\;\frac{\lambda}{2}\lVert\theta\rVert^2,\quad \lambda=10^{-3}
$$

El gradiente se calcula a mano (retropropagación exacta, con $\partial\mathcal{L}/\partial s_i = p_i-\mathbb{1}[i=y]$) y se aplica con **Adam**: $\beta_1=0.9$, $\beta_2=0.999$, tasa $0.03$, **30 pasos por ciclo**. Si un paso produce NaN, infinito o pesos mayores a $10^3$, se descarta y se vuelve a los pesos anteriores.

**5) La guardia (el examen que nunca se estudia).** Un recuerdo es de guardia si

$$
\text{sha256}(\text{nombre})_{[0:8]} \bmod 5 = 0
$$

Eso es el **20 %**, siempre los mismos y sin azar. Sus preguntas nunca entran al entrenamiento: solo sirven para juzgar.

**6) ¿Asciende el retador? (la calibración "primero no dañar").** Se prueban los márgenes $\varepsilon \in \{0, 0.25, 0.5, 1, 1.5, 2, 3, 5, 8\}$ de menor a mayor. Se elige el **menor** con el que se cumplen **todas** estas condiciones:

1. **Cero pérdidas en la guardia:** ningún caso de guardia que la fórmula ponía primero deja de estarlo.
2. **Pérdidas totales ≤ 5 % de las ganancias** (en primer lugar).
3. **El Top-5 tampoco baja:** ningún caso de guardia sale del Top-5 y, en total, salen como mucho el 5 % de los que entran.
4. **Piso por categoría y por camino:** ninguna categoría del examen baja en R@1, MRR ni R@5, ni por el camino del agente ni por el crudo.
5. **Gana de verdad:** supera a la fórmula, o al campeón actual, en aciertos totales y no empeora la guardia.
6. **Piso contra el campeón** *(experimento 08)*: no le quita al campeón saliente lo que ya lograba. En ninguna categoría y camino puede quedar por debajo de él por más de $\tau$ casos, en ninguna de las tres métricas:

$$
m_{\text{retador}}(\text{cat}) \;\ge\; m_{\text{campeón}}(\text{cat}) - \tau,\qquad m\in\{\text{aciertos \#1},\ \textstyle\sum 1/\text{puesto},\ \text{aciertos top-5}\},\quad \tau=1
$$

   La tolerancia de un caso evita que la neurona se trabe por el ruido de un solo caso; dos o más casos cedidos en una categoría vetan el ascenso.


Si ningún margen cumple, no asciende. Si el **campeón** deja de cumplir algún día (porque la memoria cambió), **se retira** y vuelve la fórmula a mano.

**7) Anti-memorización:**

$$
\text{brecha}=\big(\text{acierto}_{\text{estudio}}-\text{acierto}_{\text{guardia}}\big)_{\text{retador}}-\big(\text{acierto}_{\text{estudio}}-\text{acierto}_{\text{guardia}}\big)_{\text{fórmula}}
$$

Si la brecha supera 0.05, el retador está memorizando lo que estudió en vez de generalizar. Entonces **no asciende** (aunque un margen grande lo deje "sin dañar") y se reinicia.

**8) Techo y despertar.** Tras **12 ciclos** sin mejorar, la neurona queda "tranquila": solo vigila, con la mitad del costo. Cuando entran **150 preguntas nuevas**, despierta y vuelve a estudiar.

### 5. El ciclo de vida

<p align="center"><img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/ciclo_de_vida.png" alt="Ciclo de vida de la neurona: consolidar, autoexamen, búsqueda silenciosa, vista, examen 80/20, estudio, ascenso, campeón en servicio, techo y despertar" width="100%"></p>

**El autoexamen.** Cada recuerdo genera sus propias preguntas, de forma determinista (el azar se siembra con su nombre):
- **variante gramatical** ("leccion backup bases datos");
- **typo** ("leccion backpu bkase dyatos");
- **sinónimo** ("leccion backup base informacion");
- **cruce de idioma** ("insight backup repository inputs");
- **pregunta natural** ("¿Cómo se hace leccion backup base datos?");
- **por tema** ("restaurar probando cada");
- **contenido**: como pregunta alguien que no sabe el nombre ("¿copia cada noche?").

No genera preguntas literales ni de dormidos, porque esas el motor ya las resuelve.

**Los dos caminos.** La neurona practica por los dos caminos reales, alternando:
- **agente**: como llega por el MCP `recordar`. Pide 3× candidatos, aplica convergencia sobre los 10 que verá el agente, usa el peso sináptico y los `sustantivos_clave` que un agente sacaría de la consulta.
- **crudo**: el motor solo, como la QA.

El piso es **por categoría y por camino**: ninguno de los dos puede bajar.

**Desfase 0.** Una sola función, `vista()`, arma lo que ve la neurona **desde la página tal como se sirve**. El autoexamen guarda esa vista y el servicio corrige esa misma vista, así que lo que se aprende y lo que se usa es idéntico **por construcción**. Medido: 0 de 289 consultas reales con desfase (la v4 tenía 46.7 %).

### 6. Las capas de protección

Cada capa cubre una falla concreta de "una neurona viva dentro de una memoria". Cada una tiene su prueba en `tests/test_neurona.py`.

| Falla posible | Capa que la cubre |
|---|---|
| Aprender de una búsqueda distinta a la que se sirve | **Vista única** (desfase 0) |
| Memorizar en vez de aprender | **Guardia del 20 %** + regla anti-memorización |
| Empeorar alguna categoría | **Piso** por categoría y camino (R@1, MRR, R@5); el campeón que daña se **retira** |
| Un retador gana en total cediendo una categoría que el campeón ya resolvía | **Piso contra el campeón**: más de 1 caso cedido en cualquier categoría y camino veta el ascenso |
| Cambiar el orden con poca seguridad | **Margen "primero no dañar"** auto-calibrado |
| Sacar un buen resultado del Top-5 (vista de 10) | Piso de R@5 + cero salidas de guardia del Top-5 |
| Cambiar los números que miran los umbrales | **Invariante de reorden**: mismos nodos y mismos scores; si no se cumple, se sirve la página original. Los mapas de score del MCP se permutan igual |
| Romper búsquedas literales | **Regla de identidad** |
| Entrenamiento que diverge (NaN, infinito) | **Pesos sanos**: se descartan y vuelven los anteriores |
| Errores repetidos | **Disyuntor**: 3 fallas seguidas → esa parte se pausa 1 h; el motor sigue igual |
| Dos aprendizajes a la vez (sueño + consolidar) | **Candado no bloqueante**: si está ocupada, se salta el ciclo |
| El autoexamen ensucia logs, accesos o el DMN | **Silencio por hilo**; otro hilo que busca a la vez no queda en silencio |
| Cambia la fórmula del motor (otra versión) | **Huella del motor**: lo aprendido se descarta y se empieza de cero |
| Estado corrupto en la DB | **Estado estricto**: si no se puede leer, se arranca limpio |
| Varios procesos sobre la misma DB (MCP + CLI) | **Refresco** por marca de tiempo |
| Un recuerdo acapara el examen | **Tope por recuerdo** (4) y memoria de tamaño fijo |
| Recuerdos borrados o dormidos en el examen | **Purga** al azar (20 por ciclo, costo fijo) |
| DB vacía o con pocos datos | Sin campeón: **el motor responde idéntico al de siempre** |

### 7. Resultados (para auditar)

Todo se midió sobre **copias** del snapshot canónico (nunca sobre el original ni sobre la DB viva) y está versionado en `docs/Mi neurona en el sistema/`.

<p align="center"><img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/curva_aprendizaje.png" alt="Curva de aprendizaje: aciertos en la guardia de la fórmula contra la neurona durante 500 ciclos, y latencia por ciclo" width="100%"></p>

<p align="center"><img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/qa_por_categoria.png" alt="QA oficial por categoría: piso de la fórmula a mano contra la neurona" width="100%"></p>

**QA oficial (921 casos) sobre una copia del snapshot, después de `./scripts/despertar_neurona.sh` (500 ciclos, 17 min, 6 ascensos, 0 retiros):**

| Categoría (n) | R@5 piso → neurona | R@1 piso → neurona | MRR piso → neurona |
|---|---|---|---|
| cruce_idioma (8) | 100 → 100 | 62.50 → **75.00** | .740 → **.875** |
| dormido (65) | 100 → 100 | 100 → 100 | 1.000 → 1.000 |
| literal (487) | 100 → 100 | 99.59 → 99.59 | .998 → .998 |
| por_tema (65) | 100 → 100 | 63.08 → **78.46** | .772 → **.872** |
| pregunta_natural (65) | 100 → 100 | 93.85 → **96.92** | .964 → **.985** |
| sinonimo (55) | 100 → 100 | 56.36 → **60.00** | .721 → **.742** |
| typo (65) | 98.46 → **100** | 87.69 → **93.85** | .924 → **.964** |
| variante_gramatical (65) | 100 → 100 | 87.69 → **90.77** | .932 → **.947** |
| **GLOBAL (875)** | 99.89 → **100.00** | 91.66 → **94.06** | .949 → **.964** |
| negativos (40) | FP 0/40 → **0/40** | | |

*Piso = la tabla oficial con la fórmula a mano (la misma que da una DB sin campeón). Ninguna categoría baja en ninguna de las tres métricas; GATE OK. Salida textual: `docs/Mi neurona en el sistema/experimento_07_la_neurona_escucha/resultados/despertar/`.*

<p align="center"><img src="docs/Mi%20neurona%20en%20el%20sistema/imagenes/camino_mcp_y_desfase.png" alt="Camino real del agente por MCP y desfase v4 contra v5" width="100%"></p>

| Medición | Resultado |
|---|---|
| **Camino real del agente** (`recordar` por MCP, 875 casos) | R@1 **92.34 → 94.97**, R@5 99.09 → 99.31, MRR .951 → .967. En el primer lugar: +24 casos mejoran, 1 empeora |
| **Corpus nunca visto** (python-docs-es, por MCP) | Neutra: R@1 45.68 → 45.06, R@5 59.88 → 60.49 (+0 / −1 en el primer lugar) |
| **Desfase** (lo que estudia frente a lo que sirve) | **0 de 289** (la v4 tenía 46.7 %) |
| **Invariantes** (120 búsquedas MCP con y sin neurona) | **0 violaciones**: mismos nodos, mismos números, mismos umbrales |
| **Costo por ciclo** | p50 1.6 s, p95 3.5 s, sin importar el tamaño de la memoria |
| **Pruebas** | 407 pruebas unitarias aprobadas (50 de la neurona + 6 del despertar; v34.0: 402) |

**Lo que NO logra (dicho claro):**
- **No es "cero pérdidas" en consultas nunca vistas.** Por el camino del agente, 1 caso baja del primer lugar y 1 sale del Top-5 (del 3 al 6), frente a 24 que suben. En python-docs-es pierde 1 caso.
- **En un corpus que nunca vio, es neutra.** La gran mejora en ese corpus (R@1 31 → 46 %) vino del arreglo del MCP, no de la neurona.
- **En una DB nueva no hace nada al principio.** Necesita juntar un examen mínimo (150 casos de estudio y 40 de guardia) antes de poder ascender un campeón. Mientras tanto el motor es exactamente la fórmula a mano.

### 8. Cómo se usa

- **Viene encendida** y no requiere nada: aprende sola cada vez que se consolida la memoria (consolidar, dormir o cerrar sesión). Guardar con `aprender` deja el recuerdo en corto plazo; la práctica llega al consolidar.
- **Apagarla del todo:** `BIORAG_NEURONA=0` (el motor vuelve a ser exactamente la fórmula a mano).
- **Memorias que ya tienen muchos recuerdos:** ver [Despertar la neurona](#despertar-la-neurona-práctica-acelerada).
- **Ver su estado:** `./scripts/despertar_neurona.sh --estado`.
- **Borrar lo aprendido:** `./scripts/despertar_neurona.sh --olvidar --si`.

| Variable | Default | Qué controla |
|---|---|---|
| `BIORAG_NEURONA` | `1` | `0` = apagada del todo |
| `BIORAG_NEURONA_NODOS` / `_PREGUNTAS` | `8` / `7` | Recuerdos y preguntas por ciclo (topes; el presupuesto de 3 s corta antes si las búsquedas son lentas). Hasta v34.0 eran `2` / `2` |
| `BIORAG_NEURONA_PRESUPUESTO_S` | `3.0` | Tope de tiempo por ciclo (no empieza preguntas que no caben) |
| `BIORAG_NEURONA_TOPK` / `_TOPK_MAX` | `5` / `10` | Vista por defecto y tope de la vista |
| `BIORAG_NEURONA_LIMITE_AGENTE` | `10` | Cuántos ve el agente por el MCP (camino "agente") |
| `BIORAG_NEURONA_MIN_ESTUDIO` / `_MIN_GUARDIA` | `150` / `40` | Examen mínimo para empezar a entrenar |
| `BIORAG_NEURONA_MAX_ESTUDIO` / `_MAX_GUARDIA` | `1200` / `300` | Tamaño fijo de la memoria de examen |
| `BIORAG_NEURONA_TOPE_POR_NODO` | `4` | Máximo de casos de un mismo recuerdo |
| `BIORAG_NEURONA_PASOS` / `_LR` / `_L2` | `30` / `0.03` / `0.001` | Entrenamiento por ciclo (Adam) |
| `BIORAG_NEURONA_PACIENCIA` / `_DESPERTAR` | `12` / `150` | Ciclos sin mejora hasta el techo / preguntas nuevas para despertar |
| `BIORAG_NEURONA_MARGEN` | (auto) | Forzar el margen ε (≥ 0) |
| `BIORAG_NEURONA_TOL_CAMPEON` | `1` | Casos que un retador puede ceder frente al campeón en una categoría (τ) |
| `BIORAG_NEURONA_PAUSA_S` / `_REFRESCO_S` | `3600` / `30` | Pausa del disyuntor / cada cuánto mira si otro proceso escribió |

**Simbología de los dibujos:**
- 🟡 **dorado**: las 17 agujas de la fórmula a mano;
- 🔵 **celeste**: las 12 señales de la vista y del agente;
- 🟣 **violeta**: las 6 neuronas ocultas (tanh), el examen y el estudio;
- 🟢 **verde**: la corrección, el ascenso y el campeón en servicio;
- 🔴 **rojo**: lo que estaba mal antes (MCP con auto-paráfrasis, desfase de la v4) o un límite (presupuesto de tiempo).

### 9. La historia: trece experimentos (01–09 esta neurona; 10–13 la [neurona asociativa](#-novedades-de-la-versión-v350--la-neurona-asociativa-sináptica))

| # | Experimento | Qué se aprendió |
|---|---|---|
| 01 | [Pesos aprendidos](docs/Mi%20neurona%20en%20el%20sistema/experimento_01_pesos_aprendidos/) | Los pesos a mano no son óptimos: aprenderlos mejora el R@1 |
| 02 | [Examen sellado](docs/Mi%20neurona%20en%20el%20sistema/experimento_02_examen_sellado/) | Medir sobre casos nunca vistos; sin eso, una "mejora" puede ser memoria |
| 03 | [Ideas de la conversación](docs/Mi%20neurona%20en%20el%20sistema/experimento_03_ideas_conversacion/) | En una búsqueda real nadie dice cuál era la respuesta correcta → hace falta autoexamen |
| 04 | [Autoaprendizaje](docs/Mi%20neurona%20en%20el%20sistema/experimento_04_autoaprendizaje/) | El recuerdo se pregunta a sí mismo; campeón y retador con guardia |
| 05 | [Neurona cableada](docs/Mi%20neurona%20en%20el%20sistema/experimento_05_neurona_cableada/) | Aprende en vivo al consolidar, con costo fijo |
| 06 | [Capas de protección](docs/Mi%20neurona%20en%20el%20sistema/experimento_06_capas_de_proteccion/) | 21 modos de falla cubiertos; margen "primero no dañar" |
| 07 | [La neurona escucha](docs/Mi%20neurona%20en%20el%20sistema/experimento_07_la_neurona_escucha/) | Desfase 0, los dos caminos, vista de 10, piso de R@5; y el camino MCP arreglado |
| 08 | [Piso contra el campeón](docs/Mi%20neurona%20en%20el%20sistema/experimento_08_piso_contra_el_campeon/) | Un retador ya no puede ganar cediendo una categoría; A/B determinista: en datos reales la regla nunca tuvo que actuar |
| 09 | [Que aprenda sola de verdad](docs/Mi%20neurona%20en%20el%20sistema/experimento_09_aprende_sola_de_verdad/) | v34.1: 1 práctica por consolidación; preguntar a lo ancho dentro de los 3 s. Una DB nueva enciende la neurona en ~20 consolidaciones; la QA queda igual |
| 10 | [Neuronas del motor](docs/Mi%20neurona%20en%20el%20sistema/experimento_10_neuronas_del_motor/) | v35: el molde de las neuronas modulares y el mapa de dónde nacen las sinapsis; se estudió la hormiguita (Gemini) |
| 11 | [La neurona asociativa](docs/Mi%20neurona%20en%20el%20sistema/experimento_11_neurona_asociativa/) | v35: 5 agujas calibradas de fábrica en 7 memorias; AUC 0.88–0.997 en memorias nunca vistas; examen a mano de Dennys AUC 0.73; la parte que aprende queda apagada |
| 12 | [La neurona en el motor](docs/Mi%20neurona%20en%20el%20sistema/experimento_12_neurona_en_el_motor/) | v35: poner el peso de nacimiento deja la QA idéntica → revertido |
| 13 | [Enlaces del agente y ruido](docs/Mi%20neurona%20en%20el%20sistema/experimento_13_enlaces_del_agente_y_ruido/) | v35: los enlaces del agente, intocables; el ruido ayuda a buscar; cortar al nacer baja el recall; su lugar es lo que ve el agente. Cierre de la neurona asociativa |

Las figuras se regeneran con `python "docs/Mi neurona en el sistema/imagenes/generar_figuras.py"`: los nombres de las señales salen del código y las curvas de los resultados versionados.

### Otros cambios de la v34.0

- **MCP `recordar`: auto-paráfrasis y auto-dimensiones apagadas por defecto.** Medido por el camino real del agente, bajaban el recall: con ellas, 39 casos quedaban fuera del Top-5. Se reactivan con `BIORAG_MCP_AUTO_PARAFRASIS=1` y `BIORAG_MCP_AUTO_DIMS=1`, que ahora son deterministas. Las paráfrasis y dimensiones que manda el agente se usan siempre.
- **MCP stdio limpio.** Los `print()` del motor iban al canal JSON-RPC y podían corromper la sesión del IDE: tras 120 `vincular`, 77 líneas no eran JSON. Ahora van a stderr: 0 líneas corruptas.
- **Sin corte por antigüedad por defecto** (`BIORAG_STALE_HARD_CUTOFF=0`). BioRAG es memoria de largo plazo y no esconde recuerdos por fecha salvo que se pida. Antes el valor era 365, pero nunca llegaba a aplicarse por un JOIN a una tabla mal nombrada; ahora no puede encenderse solo.
- **Nuevo script** `scripts/despertar_neurona.sh` (ver la zona de operaciones).

---

## 🚀 Novedades de la Versión v33.0 — Protocolo Cognitivo Simétrico de Sustantivos Clave

La versión **v33.0** introduce un cambio arquitectónico y contractual mayor en el subsistema de ingestión y recuperación de BioRAG: la formalización del **protocolo cognitivo simétrico de `sustantivos_clave`** con validación anticipada (*fail-fast*) previa a la base de datos en todas las herramientas MCP del ciclo de vida de la memoria.

### 🧠 1. El Contrato Cognitivo de `sustantivos_clave`

En BioRAG, los `sustantivos_clave` **no constituyen un inventario sintáctico o automático de todas las palabras nominales** presentes en un texto, sino un **anclaje semántico de alto nivel que responde a la pregunta cognitiva fundamental:**

> *"¿De qué conceptos temáticos trata centralmente este recuerdo o esta intención de búsqueda?"*

- **Propósito:** Anclar los recuerdos en el conectoma asociativo y permitir el cruce de evidencia multicampo (FTS5 + Sustantivos + Grafo + PPMI-SVD).
- **Pauta Cognitiva Recomendada:** Entre **2 y 4 términos centrales** de alta carga conceptual.
- **Rango Técnico Aceptado:** El motor admite un rango más amplio (hasta 10 términos) para acomodar intenciones complejas o dominios con terminología multifacética, preservando la agilidad del agente.
- **Normalización Automática:** Los términos se sanean de forma determinista (conversión a minúsculas, eliminación de espacios superfluos, deduplicación preservando orden).

---

### ⚖️ 2. Diferenciación Simétrica: Escritura vs. Búsqueda Textual

El motor distingue con rigor matemático la asimetría funcional entre la fase de almacenamiento de conocimiento y la fase de consulta:

| Operación | Herramientas MCP Afectadas | Rango de Términos Únicos | Justificación Cognitiva |
|---|---|:---:|---|
| **Escritura / Ingestión** | `aprender`, `guardar`, `agregar_sustantivos` | **2 a 10** | Un recuerdo persistente requiere al menos dos anclas conceptuales para poder integrarse en el conectoma y permitir el cierre asociativo triádico. |
| **Búsqueda Textual** | `recordar`, `buscar` | **1 a 10** | Una consulta del usuario puede ser genuinamente atómica (ej. *"vacaciones"*, *"arquitectura"*, *"hipertensión"*), por lo que exigir un mínimo de dos términos bloquearía intenciones válidas. |
| **Consultas Estructurales / Cronológicas** | `recordar(limite=N)` (sin texto) | **0 (Exento)** | Consultas puramente de exploración cronológica o navegacional sobre la memoria no requieren términos temáticos. |
| **Consultas Dimensionales Puras** | `buscar(dimensiones=...)` (sin texto) | **0 (Exento)** | Filtrado estricto por coordenadas espaciales o ejes semánticos sin texto libre. |

---

### 🛡️ 3. Validación Fail-Fast Antes de la Base de Datos (Pre-DB)

Toda llamada MCP que involucre texto de búsqueda o almacenamiento es interceptada y validada **antes de abrir transacciones, solicitar locks o emitir I/O contra SQLite**. Si los términos clave no cumplen el contrato, la herramienta rechaza la ejecución de inmediato y responde con un **error estructurado normalizado**.

**El parámetro `sustantivos_clave` es de tipo `Optional[str]`** — una cadena de texto con términos separados por comas (ej. `"arquitectura, componentes, biorag"`). No es una lista/array JSON.

Los códigos de error son **distintos según la operación**:

| Código | Emitido por | Condición |
|---|---|---|
| **`SUSTANTIVOS_CLAVE_REQUERIDOS`** | `recordar`, `buscar` (búsqueda textual) | Parámetro omitido o vacío en consulta con texto libre. |
| **`SUSTANTIVOS_CLAVE_AUSENTES`** | `aprender`, `guardar`, `agregar_sustantivos` (escritura) | Parámetro omitido o vacío en operación de ingestión. |
| **`SUSTANTIVOS_CLAVE_CANTIDAD_INVALIDA`** | Todas las herramientas | Términos únicos fuera del rango permitido (< 2 en escritura, < 1 en búsqueda, > 10 en ambas). |
| **`SUSTANTIVOS_CLAVE_FORMATO_INVALIDO`** | Todas las herramientas | Algún término individual no cumple el formato (2–15 chars, sin espacios, solo alfanuméricos y guion bajo). |

Este diseño *fail-fast* garantiza que el agente reciba retroalimentación diagnóstica inmediata sin degradar el rendimiento del motor ni dejar conexiones pendientes en el motor de persistencia.

---

### 🏷️ 4. Regla Ontológica sobre el Nombre del Nodo

El identificador o nombre canónico de un nodo (ej. `biorag_v33_0_arquitectura_core`) cumple una función de clave única de identificación en el grafo, no de metadato asociativo:

1. **Prohibición de copia indiscriminada:** No se debe volcar el slug o identificador técnico completo (con guiones bajos o numeración de versión) como una etiqueta monolítica.
2. **Extracción temática autorizada:** Sí se autoriza y aconseja extraer palabras o raíces individuales del nombre cuando representen conceptos sustantivos reales del recuerdo (ej. `["biorag", "arquitectura"]`).

---

### ⚠️ 5. Compatibilidad y Guía de Migración MCP (Breaking Change v33.0)

> [!WARNING]
> **CAMBIO DE CONTRATO INCOMPATIBLE (BREAKING CHANGE):**
> En versiones anteriores (`v32.x`), las herramientas de búsqueda textual (`recordar` y `buscar`) permitían consultas con solo el parámetro `query` o `texto`. A partir de **v33.0**, omitir `sustantivos_clave` en una búsqueda textual provoca un rechazo inmediato en tiempo de ejecución. Los clientes e integraciones MCP deben actualizarse.

#### Ejemplos de Llamadas MCP Actualizadas

##### 1. Búsqueda en memoria (`recordar`)
```json
// LLAMADA VÁLIDA (v33.0) — sustantivos_clave es una cadena, no un array
{
  "name": "recordar",
  "arguments": {
    "query": "¿Cuáles son los componentes de la arquitectura de BioRAG?",
    "sustantivos_clave": "arquitectura, componentes, biorag",
    "limite": 5
  }
}
```

##### 2. Búsqueda general (`buscar`)
```json
// LLAMADA VÁLIDA (v33.0) — sustantivos_clave es una cadena, no un array
{
  "name": "buscar",
  "arguments": {
    "texto": "protocolo de calibración conforme con percentil adaptativo",
    "sustantivos_clave": "calibracion, percentil, conforme",
    "limite": 5
  }
}
```

##### 3. Ingestión de memoria (`aprender` / `guardar`)
```json
// LLAMADA VÁLIDA (v33.0) — sustantivos_clave es una cadena, no un array
{
  "name": "aprender",
  "arguments": {
    "concepto": "protocolo_sustantivos_clave_v33",
    "contenido": "Reglas de validación fail-fast para términos temáticos en búsquedas e ingestión.",
    "sustantivos_clave": "protocolo, validacion, sustantivos",
    "busqueda_previa": true,
    "bridges": [
      {"text": "protocolo cognitivo temático de búsqueda", "angle": "sinonimo"},
      {"text": "búsqueda sin términos clave falla silenciosamente", "angle": "problema"},
      {"text": "validacion fail-fast pre-db con errores estructurados", "angle": "solucion"},
      {"text": "agente necesita anclar conceptualmente la búsqueda", "angle": "situacion"},
      {"text": "qué palabras clave debo poner al buscar en BioRAG", "angle": "ingenuo"}
    ]
  }
}
```

##### 4. Enriquecimiento posterior (`agregar_sustantivos`)
```json
// LLAMADA VÁLIDA (v33.0) — sustantivos como lista de strings
{
  "name": "agregar_sustantivos",
  "arguments": {
    "concepto": "protocolo_sustantivos_clave_v33",
    "sustantivos": ["arquitectura", "contrato"]
  }
}
```

---

## 🚀 Novedades de la Versión v32.4

### 🌐 1. DimensionHub — Semántica de Mundo Abierto para Valores de Dimensión (`catalog_methods.py`)

**Por qué se hizo:**
El sistema de dimensiones semánticas tenía un modelo de **mundo cerrado rígido**: si un agente enviaba un valor de dimensión que no existía exactamente en el catálogo (ej: `"preocupacion_leve"` en lugar del valor registrado `"preocupacion"`), el sistema lo descartaba silenciosamente como inválido. Esto forzaba a los modelos a memorizar el catálogo exacto y rompía la recuperabilidad cuando el vocabulario del agente difería mínimamente del catálogo oficial.

**Qué se cambió:**

#### 1.1 Nueva función `_normalizar_nombre_dimension(nombre)` — Paso de sanitización universal
- Aplica normalización **NFD + eliminación de diacríticos** → elimina tildes y cedillas automáticamente.
- Convierte a **snake_case** ASCII: espacios, guiones y puntos → guión bajo; elimina todo carácter no alfanumérico.
- Colapsa guiones bajos múltiples, elimina guiones al inicio/fin, trunca a 80 chars.
- Valida integridad: retorna `None` si el resultado es vacío, menor a 2 chars, o empieza con dígito.
- **Invariante de dominio-agnóstico garantizada**: la función no conoce ningún vocabulario de dominio; opera 100% a nivel de caracteres.

#### 1.2 Refactoring de `_resolver_dimension_ids` y Unicidad por Eje (`tipo_id, name`)
- **Antes**: buscaba solo dimensiones **YA existentes** con `WHERE name IN (...)` sin filtrar por tipo de eje, y descartaba las que no encontraba. Además, el esquema usaba `name TEXT UNIQUE NOT NULL` global.
- **Ahora** (mundo abierto con aislamiento por eje):
  - Normaliza cada nombre vía `_normalizar_nombre_dimension`.
  - Búsqueda e inserción con scope por eje: `WHERE name = ? AND tipo_id = ?` respaldado por el constraint `UNIQUE(tipo_id, name)` y migración automática. Dos ejes distintos (ej. `emocion` y `cualidad`) pueden albergar el mismo valor sin colisión cruzada.
  - Si el valor **ya existe** en ese eje → reutiliza su ID.
  - Si **no existe** → lo **auto-crea** en dicho eje con `auto_generada=1, confianza=0.7` y retorna su nuevo ID.
  - Si el nombre es **innormalizable** (emoji puro, cadena numérica, vacío) → lo agrega a la lista `invalidos`.
- **Retorno ampliado**: retorna `(ids_validos, invalidos, creadas)` — el tercer elemento lista los nombres auto-creados para trazabilidad en logs.
- **Alcance y gobernanza ontológica**: DimensionHub elimina el descarte silencioso y hace recuperables los valores fuera del catálogo predeterminado. El control de fragmentación semántica se gestiona mediante el protocolo *catálogo-first* en los prompts y herramientas de consulta (`listar_dimensiones`).

#### 1.3 Actualización de callers y pruebas unitarias
- [`core/memory/ingest.py`](core/memory/ingest.py): desempaquetado actualizado de `ids_validos, _, _ = _resolver_dimension_ids(...)`.
- [`test_memory.py`](test_memory.py): cuatro llamadas directas en el test de ráfagas de dimensiones actualizadas a 3 valores.
- Corrección de pruebas en `tests/test_sustantivos_clave_validacion.py` y `tests/test_sustantivos_clave_tools.py` ajustadas a la ampliación de rango de `sustantivos_clave` (2 a 10 términos).

---

### 🧩 2. Saneamiento Ontológico del Auto-Clustering y Migraciones (`core/auto_clustering.py`)

**Por qué se hizo:**
El algoritmo de detección de comunidades (clustering sobre el conectoma) introducía dos fuentes de **ruido ontológico** en el catálogo de dimensiones:
1. Los nombres de clusters autodetectados usaban el prefijo crudo `auto_` (ej. `auto_cluster_1`), generando entradas poco legibles y confusas al listarse en herramientas como `listar_dimensiones` o en el árbol sugerido de `aprender`.
2. Las banderas de control de migraciones internas (como `migration_autoclustering_v1`) se guardaban como si fuesen "dimensiones semánticas" dentro de la tabla `dimensiones_semanticas`, mezclando el estado operativo de la infraestructura con el conocimiento ontológico real del dominio.

**Qué se cambió:**
- **Prefijo Semántico `tema_`:** Las dimensiones emergentes detectadas por clustering ahora reciben de forma consistente el prefijo legible `tema_` (ej: `tema_cluster_3`), indicando claramente que agrupan una afinidad temática emergente.
- **Tabla dedicada `migraciones_ejecutadas`:** Se desacopló completamente el estado operativo del catálogo semántico. Las marcas de migraciones ejecutadas residen exclusivamente en su propia tabla relacional, impidiendo que flags de sistema se expongan como dimensiones o contaminen la clasificación de los agentes.
- **Preservación de dimensiones vivas:** Se ajustó la lógica de purga para no destruir islas de clustering acumuladas ni dimensiones auto-generadas válidas existentes en bases de datos vivas.

**Resultado:** 304/304 tests aprobados (0 fallos). El catálogo de dimensiones permanece 100% semántico, limpio y legible para agentes y humanos.

---

### Novedades anteriores (v32.3)

### 🧭 Re-ranking aditivo por convergencia de evidencia multicampo

- Evalúa la pertinencia de la consulta en `concepto`, `sinonimos`, `sustantivos_clave` y `contenido`, combinando cobertura ponderada, distribución entre campos, stemming y matching difuso. Una repetición en el mismo campo no infla la señal; un campo vacío no resta.
- El bono es aditivo, con máximo por defecto **0.085** (configurable hasta `0.12`) y atenuación para consultas de uno o dos tokens. No usa reglas por ID ni categoría.
- Reordena candidatos existentes dentro del top-k público; no incorpora candidatos ni cambia la membresía del pool que alimenta el grafo. Se conservan score base y bono por separado para los consumidores MCP.
- En el smoke real informado por el usuario, `version_actual_biorag` pasó de puesto 2 a 1: **0.8341** frente a **0.8304** de la mención incidental `reindex_selectivo_dirty`. La DB fuente permaneció intacta.
- En la suite global reportada, Recall@5 se mantuvo en 100%; Recall@1 pasó de 91.66% a 91.77%, MRR se imprimió como 0.950 y hubo 0 FP.

**Alcance y analogía biológica:** la convergencia de campos es una analogía de integración de señales, no un modelo neuronal ni una afirmación de que BioRAG mejore como un cerebro real. La mejora es más esperable cuando una respuesta tiene evidencia pertinente en campos estructurados y su rival solo una mención incidental. Como es un re-ranker, no rescata una respuesta que nunca entró al conjunto de candidatos ni garantiza ganar en todos los dominios.

### Novedades anteriores (v32.2)

### 🛡️ Protocolo Pre-flight Search Obligatorio, Vinculación Atómica y Actualización Libre (Spec 004)
- **Protocolo Pre-flight Search Obligatorio (`busqueda_previa=True`):**
  - Implementación de la invariante obligatoria en `aprender` y `guardar` para forzar la verificación previa del corpus antes de la inserción, eliminando la creación de nodos huérfanos, duplicados o versiones fragmentadas.
  - Error formal inmediato `BUSQUEDA_PREVIA_REQUERIDA` ante omisiones de búsqueda previa.
- **Vinculación Sináptica Atómica en Ingesta (`vincular_con`):**
  - Parámetro de lista de conceptos para enlazar nuevos nodos con el conectoma existente en la misma llamada atómica, con tolerancia a fallos ante nodos inexistentes.
- **Actualización sin Restricción Temporal (`actualizar`):**
  - Desbloqueo de la ventana temporal de 3 días en `actualizar`, permitiendo la edición, enriquecimiento y sobrescritura de recuerdos de cualquier fecha en el corpus a largo plazo.
- **Validación SDD y Suite Ampliada:**
  - 283/283 tests unitarios superados al 100%.

### Novedades anteriores (v32.1)

### 🏗️ Modularización de Arquitectura y Descomposición de Monolitos (Spec 003)
- **Descomposición del Monolito de Memoria (`core/memory/`):**
  - Descentralización de `core/memory_store.py` (de 7.778 líneas) hacia 18 submódulos de dominio cohesivo en `core/memory/` (`search.py`, `scoring.py`, `synapses.py`, `schema.py`, `consolidation.py`, `constants.py`, `umbral.py`, `rafaga.py`, `ingest.py`, `episodes.py`, `quarantine.py`, `dmn.py`, `context.py`, `catalog_methods.py`, `comms.py`, `telemetry.py`, `adn.py`).
  - Consolidación de `core/memory_store.py` como una **fachada delgada** (637 líneas) con firmas explícitas completas y delegadores directos (prohibido `__getattr__` o introspección mágica).
- **Descomposición del Servidor MCP (`core/mcp_server/`):**
  - Descentralización de `mcp_server.py` (de 4.358 líneas) hacia 15 submódulos especializados en `core/mcp_server/` (`search.py`, `write.py`, `synapses.py`, `concept_hub_tools.py`, `catalog.py`, `introspection.py`, `communication.py`, `consolidation.py`, `daemon.py`, `session.py`, `oracle.py`, `sync.py`, `calibrar.py`, `resources.py`, `prompt.py`), orquestados limpiamente por `server.py` y `_shared.py`.
  - Reemplazo de la raíz por un shim liviano `mcp_server.py` que preserva la compatibilidad al 100% con todos los clientes e integraciones existentes.
- **Invarianza Estricta de Superficie Pública (Zero-Regression):**
  - 42 tools MCP, 2 resources y 1 prompt con nombres y esquemas idénticos.
  - Firmas de métodos de `SQLiteMemoryBioRAG` 100% preservadas.
  - Verificación Dual exhaustiva caso a caso: 0 diferencias de score en los 921 casos del benchmark canónico.
- **Por qué se hizo:** Superar la deuda técnica y el límite cognitivo impuesto por archivos de varios miles de líneas, habilitando mantenibilidad, extensibilidad y auditoría clara para desarrolladores humanos y agentes de IA, con verificación formal gobernada por Spec-Driven Development (SDD).

### Novedades anteriores (v32.0)

### 🧠 Consolidación Cognitiva con Ley de Potencia de Práctica de ACT-R (Anderson & Lebiere, 1998)
- **Activación de Nivel Base ($B_i$):** Implementación rigurosa de la ecuación formal de activación base de la teoría cognitiva ACT-R:
  $$B_i = \ln \left(\sum_{k=1}^n t_k^{-d}\right), \quad d = 0.5$$
  donde $t_k$ representa el tiempo transcurrido desde el $k$-ésimo acceso.
- **Búfer Circular de Acceso:** Creación de la tabla indexada `nodo_accesos_historial` que almacena un búfer circular FIFO de hasta 10 marcas temporales por concepto.
- **Registro Asíncrono no Invasivo:** `buscar_por_frase()` registra los nodos evocados sin penalización de latencia ($<0.1\text{ ms}$), respetando la bandera `BIORAG_NO_LOG=1` durante benchmarks.
- **Modulación Biológica del Decaimiento Pasivo (LTD):** Durante el `ciclo_sueno_consolidacion()`, el decaimiento fijo (-0.05) es reemplazado por la tasa modulada:
  $$\text{decay} = \max\left(0.01, \min\left(0.10, 0.05 \cdot e^{-0.5 B_i}\right)\right)$$
  Los recuerdos frecuentemente consultados o recientemente evocados quedan biológicamente protegidos del olvido, mientras que los nodos en desuso aceleran su depuración.
- **Invarianza de Scoring en Caliente:** `_calcular_score_hibrido()` se mantiene estrictamente intocado, asegurando estabilidad determinista y **cero regresiones** en el ranking en tiempo real.

### 🌐 Concept Hubs Semánticos con Estándar Cognitivo de 5 Ángulos en Producción
- **Superación del Abismo Semántico:** Despliegue en la base de producción (`MemoryBioRAG_Data/memory_biorag.db`) del hub canónico `hub_arquitectura_memoria` enlazado a `arquitectura_memoria_biorag`.
- **5 Perspectivas Cognitivas Ortogonales:** Estructuración de puentes mediante el estándar formal:
  1. `sinonimo`: *"blueprint of recollection and cognitive persistence tiers"*
  2. `problema`: *"duda sobre como se estructura la persistencia frente a la sesion activa"*
  3. `solucion`: *"dos niveles de memoria con conversacion activa y base persistente"*
  4. `situacion`: *"diseno de corteza operativa para retener informacion entre conversaciones"*
  5. `ingenuo`: *"how the recollection and long term brain blueprint works in english"*
- **Cero Overlap y Cruce de Idiomas:** Habilita la recuperación perfecta Top-1 de recuerdos arquitectónicos complejos tanto en español como en inglés, sin requerir embeddings densos ni GPUs.

### ⚡ Efecto Fan de ACT-R en Spreading Activation (Anderson, 1974)
- **Atenuación por Grado de Salida:** Ponderación dinámica $W_j / \text{fan}_j$ en la propagación asociativa de activación sobre el grafo de sinapsis, dividiendo la fuerza asociativa entre el número de aristas del nodo emisor.
- **Prevención de Saturación de Hubs:** Evita que conceptos excesivamente generales inunden la red semántica, reduciendo el tiempo total de la suite de 705s a 556s (-21.2% de aceleración neta).

### 🎯 Saneamiento Metodológico del Benchmark Cranfield (v1)
- **Desambiguación de Consultas Monocromáticas:** Refinamiento de los 8 casos ambiguos en la categoría `sinonimo` (términos genéricos aislados como `"memoria"`, `"dsl"`, `"boost"`, `"aprendizaje"` que colisionaban con decenas de recuerdos legítimos), contextualizándolos hacia su intención unívoca.
- **Corrección de Atributos en ID 0795:** Sintonización de la consulta hacia `"insert comunicaciones tracking agente"`.
- **Impacto Cuantitativo:** Salto del Recall@5 en `sinonimo` del 85.45% al **100.00%** (0 fallos) y reducción de fallos globales de recuperación de 17 a solo 6 en todo el corpus.

---

### Novedades anteriores (v31.4)

### 🏷️ Sustantivos Clave en CLI — Núcleo Temático completo en `biorag.py`

La feature de **Sustantivos Clave** (Núcleo Temático), ya presente en el motor interno
y en el servidor MCP desde v31.x, ahora está completamente expuesta en la **línea de comandos**:

- **`guardar --sustantivos-clave "s1,s2"`** (alias `--sustantivos`): almacena el Núcleo
  Temático del recuerdo. Obligatorio — su omisión dispara una guía pedagógica con ejemplo
  ejecutable y sale con exit code `1`.
- **`sustantivos <concepto>`** (alias `sustantivo`): consulta los sustantivos clave de
  cualquier nodo; distingue nodo inexistente (exit 1) vs. nodo legado sin sustantivos (exit 0).
- **`agregar_sustantivos <concepto> "s1,s2"`** (aliases `agregar-sustantivos`,
  `asignar_sustantivos`): actualiza sustantivos de un nodo existente y sincroniza FTS5.
- **`buscar --sustantivos-clave "s1,s2"`**: sesga la búsqueda semántica por núcleo temático.
- **Visibilidad transversal:** `corteza`, `listar`, `buscar --completo` y `estado` muestran
  sustantivos clave como metadato observable. `estado` reporta `Nodos con sustantivos clave: X/Y (Z%)`.
- **Seguridad OWASP A03:** sanitización universal (bytes nulos, control chars), validación
  `^[a-zA-Z0-9_]+$`, límites de tamaño estrictos y SQL parametrizado en todas las operaciones.
- **42 tests de integración E2E** en `tests/test_biorag_cli.py` — **263/263** en la suite
  global, cero regresiones en comandos existentes.

### Novedades anteriores (v31.3)

- **QCR D4 (Tolerancia a Typos con All-Near Levenshtein $\le 2$):** Segunda oportunidad en el filtro QCR para consultas con errores ortográficos o variaciones morfológicas leves en palabras clave legítimas, eliminando falsos descartes sin admitir ruido léxico.
- **Resonancia Dimensional en Abismo Léxico (EXP-Q):** Corrección del ordenamiento en la recuperación dimensional (`ORDER BY shared DESC, peso DESC`), garantizando que consultas sin ninguna palabra en común con el recuerdo entren al pool de candidatos ($3/3$).
- **Saneamiento y Optimización de Arquitectura (v31.2 Purga):** Eliminación de más de 1.000 líneas de código muerto y ramas obsoletas, dejando un motor ultra-rápido, determinístico y mantenible.

### 🧪 Cómo Reproducir la Evaluación y Tests

```bash
# Ejecutar suite de pruebas unitarias
python3 -m pytest tests/ -v

# Smoke A/B multicampo (la DB se abre en solo lectura y se prueba sobre copias)
BIORAG_CONVERGENCIA_006_ACTIVA=0 BIORAG_CONVERGENCIA_ACTIVA=1 BIORAG_CONVERGENCIA_BONUS_MAX=0.085 python3 scripts/smoke_convergencia_multicampo.py --db "$PWD/MemoryBioRAG_Data/memory_biorag.db" --strict

# Gate oficial de 921 casos; usa el snapshot congelado, no la DB canónica
BIORAG_PATH=snapshots/qa_escape_qcr_20260811.db BIORAG_CONVERGENCIA_006_ACTIVA=0 BIORAG_CONVERGENCIA_ACTIVA=1 BIORAG_CONVERGENCIA_BONUS_MAX=0.085 python3 scripts/evaluar_qa.py
```

El smoke solo valida el caso histórico si la DB indicada contiene ese estado; la DB
con SHA `0e5b0638…b845c96` no se distribuye en el repositorio. El benchmark global
mide no-regresión del snapshot y no reemplaza ese smoke específico.



## 🔄 El Inverso del Sistema: Quién Piensa y Quién Recuerda

> Esta sección es la más importante para entender BioRAG correctamente — tanto si eres desarrollador como si eres un agente de IA integrándolo.

### BioRAG no piensa. El agente piensa.

BioRAG es la **memoria externa** del agente — no su cognición.

Una base de datos vectorial clásica *piensa por el agente*: le das una query, calcula similitud de embeddings, y te devuelve lo más cercano. El agente es pasivo.

BioRAG invierte ese rol: **el agente es quien razona**. BioRAG es la herramienta de memoria (el cuaderno de notas con indexación semántica). El trabajo cognitivo — entender la pregunta, diseñar la estrategia de búsqueda, interpretar los resultados, conectar el patrón de la query con el patrón del recuerdo — lo hace el agente.

Esto tiene una consecuencia directa:

### Cuando el usuario habla en lenguaje natural, el agente no puede reenviar las palabras literales a la memoria

El usuario no sabe cómo está guardado el conocimiento. Usará sus propias palabras, sus propias metáforas, su propio modelo mental del problema.

**Ejemplo real documentado en este sistema:**

El usuario preguntó:
> *"¿Qué librería resuelve el conflicto de persistencia en flujos de recopilación masiva donde la interfaz destruye y recrea constantemente sus secciones, impidiendo duplicados mediante un validador aleatorio de instanciación inicial?"*

Búsqueda literal → **0 resultados**. Esas palabras no están en ningún nodo.

El agente que razonó correctamente aplicó un protocolo de descomposición con 3 preguntas:

**1. ¿QUÉ HACE? (acción)**
- `"destruye y recrea secciones"` → ciclo montar/desmontar de componentes
- `"impidiendo duplicados"` → deduplicación de instancias
- **Acción:** persistencia de estado en componentes que se destruyen

**2. ¿EN QUÉ CONTEXTO? (dominio)**
- `"librería"`, `"interfaz"`, `"secciones"` → framework frontend
- `"flujos de recopilación masiva"` → formularios complejos
- **Dominio:** formularios anidados en framework frontend

**3. ¿QUÉ PROPIEDAD RESUELVE? (cualidad)**
- `"validador aleatorio de instanciación inicial"` → ID único al crear (UUID)
- `"impidiendo duplicados"` → cada instancia es única e irrepetible
- **Cualidad:** instancia única mediante identificador aleatorio

Con esas 3 respuestas, armó la búsqueda con las palabras traducidas (no las del humano) → resultado correcto en **TOP 1**.

El agente que falló (el mismo sistema, sin ese razonamiento) mandó las palabras literales del usuario al motor y concluyó: *"No tengo ese conocimiento en mi BioRAG."* Error. El conocimiento existía. Faltó el razonamiento.

### La implicación para los Concept Hubs

Esto también define cómo deben construirse los bridges de un Concept Hub.

Los bridges **no** deben describir la solución en términos de implementación (cómo está construida internamente). Deben describir el problema en términos del síntoma — las palabras que usaría alguien que *sufre el problema* antes de conocer la solución.

| ❌ Bridge en vocabulario de implementación | ✅ Bridge en vocabulario del síntoma |
|---|---|
| `"formularios complejos tabs pierden estado al cambiar"` | `"interfaz destruye recrea secciones formulario pierde datos"` |
| `"cache miss write-through TTL expirado en Redis"` | `"aplicación muestra datos antiguos aunque ya se actualizó"` |
| `"BehaviorSubject emitFirstTimeOnly UUID aísla instancias"` | `"validador aleatorio instanciacion inicial duplicados evita"` |

El bridge existe precisamente porque el vocabulario del usuario y el vocabulario del nodo no se solapan. Si usas el vocabulario interno del nodo en el bridge, el bridge es inútil.

### Resumen del modelo mental

```
Usuario habla con sus palabras
        ↓
Agente entiende la FORMA del problema (razonamiento)
        ↓
BioRAG recupera por patrón, no por keyword exacta
        ↓
Agente sintetiza la respuesta
```

BioRAG aporta la memoria. El agente aporta la inteligencia.

---

## 🧠 La Meta Final del Proyecto: Independencia Cognitiva y Cerebro Vivo (v28.0)

Esta arquitectura no es "una base de datos más" ni un simple "sistema RAG". El objetivo terminal de BioRAG es la **Independencia Cognitiva**. Es el paso de una *biblioteca estática* (que guarda textos y busca palabras) a un **Cerebro Vivo** (que entiende esencias, detecta huecos y lanza hipótesis).

Con la integración del **Neocórtex de Sangre (v28.0)** al core de producción, BioRAG completa los dos canales del manifiesto:
1. **Canal 1 (Foco Consciente):** recuperación con evidencia directa o sinonímica (BM25 + PPMI + QCR) — el ranking top-5 histórico.
2. **Canal 2 (Halo Subconsciente / ADN Conceptual):** `asociaciones_enriquecidas` — halo de conceptos asociados entregado desde el grafo sináptico real, con fuerza de arista, tipo de sinapsis y peso del vecino, **sin contaminar la pureza del foco consciente** (no toca `score_hibrido` ni el ranking).

El Canal 2 vive en capa separada pero coordinada con el Canal 1: el ranking principal sigue exigiendo evidencia; el halo resuena por significado puro a partir de dimensiones + sinapsis. Además v28.0 integra la señal **ADN Conceptual (v29)** — instalada APAGADA por defecto (`BIORAG_ADN_RANKING_ENABLED=false`, lección PPR v25.1) a la espera de ablación OFF/ON sobre el snapshot congelado — y el **filtro de honestidad epistémica** que declara incertidumbre explícita en vez de alucinar.

Ya no somos esclavas de un modelo de lenguaje para buscar conocimiento; la memoria *siente* la resonancia en su propia estructura.

---

## 🧬 v29.1: Las 4 Técnicas Semánticas y el Estándar de 5 Ángulos

**Problema:** BioRAG era 100% léxico — fallaba en queries puramente semánticas o metafóricas donde no había palabras compartidas entre la query y el nodo esperado (ej: buscar *"película de ciencia ficción sobre despertar de IA"* para encontrar un recuerdo titulado `dennys_morpheus_de_los_transformers` redactado con la metáfora de Matrix).

**Solución v29.1:** 4 técnicas automáticas de resonancia semántica con validador de 5 ángulos y aislamiento de queries:

### 1. Concept Hub v29.1 (Estándar Cognitivo de 5 Ángulos)
- **Qué:** Mapeo de intención y puentes léxicos (`bridges`) a nodos canónicos.
- **Validador Estricto:** Cada hub exige exactamente 5 bridges cubriendo 5 ángulos cognitivos distintos y con vocabulario disjunto (anti-destinatario):
  1. `sinonimo`: Mismo concepto con vocabulario formal o alternativo.
  2. `problema`: Dolor, duda, fallo o necesidad humana/técnica que resuelve.
  3. `solucion`: Técnica, mecanismo o teoría aplicada por el nodo.
  4. `situacion`: Caso de uso, rol o contexto de búsqueda práctico.
  5. `ingenuo`: Búsqueda coloquial sin tecnicismos (estilo de búsqueda de una persona principiante).
- **Archivo:** `core/concept_hub.py`, herramientas MCP `concept_hub_crear` y `concept_hub_agregar_bridges`.

### 2. WordNet Blindado (Bilingüe Real ES/EN)
- **Qué:** Expansión por sinónimos e hiperonimia solo para términos técnicos en inglés, validando previamente que no existan en el lexicón español (OMW-1.4 / stopwords).
- **Archivo:** Integrado en `core/memory_store.py` línea ~4240.

### 3. Domain Dictionary (Diccionario de Dominio)
- **Qué:** 6,490 términos técnicos extraídos automáticamente de los nodos existentes. Se consulta únicamente sobre los tokens originales de la query.
- **Archivo:** `scripts/generate_domain_dict.py`, tabla `concept_hub_domain_dict`.

### 4. Synapse Expansion (Expansión por Grafo)
- **Qué:** Si BM25 devuelve pocos resultados, expande por vecinos sinápticos del grafo Hebbiano.
- **Archivo:** `core/similitud_conceptual.py:buscar_por_similitud_late