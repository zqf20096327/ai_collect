# Predictive maintenance on real fleet data

Predicting failures of an engine component across a fleet of SCANIA trucks: when it will fail, how sure the model
is, what the alert is worth in maintenance cost, and why it fired.

> Version 2, rebuilt on real fleet data: a verified data pipeline, survival models scored in maintenance cost, a
> live plant on industrial standards, monitoring with a gated retraining loop, a maintenance copilot with an MCP
> server, and a dashboard for planners.

![The fleet view: every truck's risk within 48 time steps, its cost-optimal workshop action and its 90% window set, live](docs/images/dashboard-fleet.png)

**Stack:** Python 3.13, Polars, LightGBM, scikit-survival, MLflow, Dagster, FastAPI, TimescaleDB, OPC UA, MQTT
Sparkplug B, Eclipse BaSyx (Asset Administration Shell), Prometheus, Grafana, MCP, React 19, TypeScript, Docker.
Every picture below is from one live run: 120 held-out test trucks replayed through the plant.

## Results

Scored with SCANIA's own cost matrix (a missed or late failure costs 200 to 500, an unnecessary workshop check 7 to
10) on the 5,045 test trucks, against never alerting, which is what a fleet without predictive maintenance pays.

| Model | C-index | AUC at 6 / 12 / 24 / 48 steps | Test cost | Saving (95% CI) |
| --- | --- | --- | --- | --- |
| **Discrete-time hazard (LightGBM)** | 0.770 | **0.834 / 0.844 / 0.853 / 0.842** | **41,337** | **26% [17%, 35%]** |
| Accelerated failure time (XGBoost) | **0.786** | 0.807 / 0.823 / 0.835 / 0.828 | 43,377 | 23% [14%, 31%] |
| Cox proportional hazards | 0.729 | 0.757 / 0.751 / 0.753 / 0.762 | 43,700 | 22% [7%, 33%] |
| Window classifier (ignores censoring) | 0.767 | 0.783 / 0.825 / 0.842 / 0.837 | 49,811 | 11% [5%, 17%] |
| Never alert | | | 56,100 | 0% |

C-index and AUC are measured on 4,710 held-out training trucks (23,550 cut points) with their true repair times.
The model was chosen on SCANIA's validation set; the test set was scored once and never used to choose anything.

**What the numbers say**

- **Handling censoring is worth it.** The classifier has to discard 30,507 cut points whose outcome is unknown and
  saves less than half of what the survival models save.
- **The sensors carry real degradation signal, but the cost gain beyond age is within noise.** Retraining the
  champion on nested feature sets (`predmaint ablation`):

  | Features | C-index | AUC at 48 | Validation cost | Test saving (95% CI) |
  | --- | --- | --- | --- | --- |
  | Age only | 0.682 | 0.769 | 51,960 | 18% [3%, 29%] |
  | Age and truck specification | 0.717 | 0.794 | 43,635 | 24% [12%, 34%] |
  | All features | 0.770 | 0.842 | 38,673 | 26% [17%, 35%] |

  Ranking quality rises clearly at every step, on a large holdout. On the 5,045-truck test set the extra saving over
  age and specification overlaps its interval, so it is not claimed as significant.
- **The model is better at "at risk" than at "exactly when".** Conformal sets at 90% average 3.4 of the 5 windows,
  and coverage on the rarest windows is loose (0.78 to 0.97 per window) with only 14 to 76 failing trucks per window
  to calibrate on.
- **The three published splits are not one population.** Against the training trucks, 20 of 87 monitored
  variables shift significantly (PSI above 0.25) in the test trucks and 16 in the validation trucks, led by
  histogram load rates: `h397_rate` reaches a PSI of 3.0 on test and 5.6 on validation, and the model's own risk
  output shifts by 0.46 and 1.02. By the last readout the median histogram 397 total is about 1.4 times the
  training median on test trucks and 3 times on validation trucks, at shorter observed ages. The test saving above
  is measured on these shifted trucks, so it already includes the effect; `predmaint skew` reproduces the table.

## A tour

**For the maintenance planner**

| | |
| --- | --- |
| ![Truck detail](docs/images/dashboard-truck.png) | **Truck detail.** Risk over time, the probability of each failure window with the 90% set, the expected cost of every possible decision (why this action and not the next), the drivers in plain words and the truck's digital twin. |
| ![Workshop plan](docs/images/dashboard-workshop.png) | **Workshop plan.** Given N free slots, the trucks that save the most expected cost by coming in now, and what is left uncovered. |
| ![Score a file](docs/images/dashboard-upload.png) | **Score a file.** Readouts and specifications in SCANIA's published CSV format in, every truck scored at its last readout out, with drivers and a CSV download. |
| ![Copilot](docs/images/dashboard-copilot.png) | **Maintenance copilot.** Plain-language questions answered only from the platform's tools, with every tool call shown under the answer so each figure can be checked. |

**For operations**

| | |
| --- | --- |
| ![Grafana](docs/images/grafana.png) | **Grafana.** Ingest and scoring rates, batch latency, the queue, alerts per warning window, the riskiest trucks from TimescaleDB, drift, champion against challenger and digital twin updates. |
| ![Drift report](docs/images/drift-report.png) | **Drift report.** Every monitored feature and the model output against the training reference, with bin-by-bin bars. Here it shows the real shift between SCANIA's training and test trucks. |
| ![Models and drift](docs/images/dashboard-models.png) | **Models and drift.** Champion and challenger, shadow agreement, the promotion gate check by check, and the most shifted features. |

**For the ML lifecycle**

| | |
| --- | --- |
| ![MLflow runs](docs/images/mlflow-runs.png) | **MLflow runs.** Every model's metrics, logged per training run. |
| ![MLflow registry](docs/images/mlflow-registry.png) | **MLflow registry.** Versions with `champion` and `challenger` aliases; promotion moves the aliases. |
| ![Dagster](docs/images/dagster-lineage.png) | **Dagster.** The pipeline as assets with lineage, from the verified download to the exported serving bundles; a sensor on drift starts the retraining job. |
| ![API](docs/images/api-docs.png) | **The API.** FastAPI with interactive docs: fleet, vehicles, decisions, the workshop plan, uploads, models, drift, the copilot and Prometheus metrics. |

## How the models work

- **Survival, not plain classification.** Every model predicts the probability of failing within 6, 12, 24 and 48
  time steps, which gives SCANIA's five warning windows directly. Censored trucks, still running when observation
  ended, are used correctly instead of being labelled healthy or thrown away.
- **Cost-optimal alerts.** Each truck gets the window with the lowest expected cost under SCANIA's matrix given its
  probabilities: the Bayes-optimal decision. No threshold is fitted, so there is nothing to overfit to the small
  validation set (tuning one was tried and made the test cost worse).
- **Prediction sets with a coverage guarantee.** Class-conditional split conformal prediction, calibrated on the
  validation trucks, returns the set of windows that contains the true one with 90% probability.
- **Explanations.** Exact TreeSHAP contributions from LightGBM for every truck's imminent-failure risk.
- **MLflow registry with champion and challenger.** `predmaint train` compares all four models and registers the
  best on validation cost. The first model becomes `champion`; every later one becomes `challenger` and has to earn
  promotion (see below). The registered model returns window probabilities, the alert and the conformal set in one
  call.

## The data

[SCANIA Component X](https://doi.org/10.5878/jvb5-d390) (version 3, CC BY 4.0): real operational data from a fleet
of SCANIA trucks, published with the paper by Kharazian et al. in
[Scientific Data (2025)](https://doi.org/10.1038/s41597-025-04802-6).

| Split | Trucks | Readouts | Target |
| --- | --- | --- | --- |
| Train | 23,550 | 1,122,452 | Time to repair, or time observed without repair (censored) |
| Validation | 5,046 | 196,227 | Warning window before failure, 5 classes |
| Test | 5,045 | 198,140 | Warning window before failure, 5 classes |

Each readout holds 8 counters and 6 histograms (105 columns), sampled irregularly per truck. Every one of them is a
cumulative lifetime counter, so the pipeline models how fast they grow and how the load pattern shifts, not their raw
values.

## Data pipeline

```
download ──► validate ──► features
  pinned        data          per-readout features using only each truck's past,
  SHA-256       contracts     random cut points for training (as the test set was cut),
  checks        (Pandera)     survival targets and warning windows
```

- **Reproducible download.** Every file is pinned by size and SHA-256 and resumed if interrupted.
- **Data contracts.** Each table is validated before use: types, no negative counters, unique readouts, every truck
  present in all tables, no readout after the end of its observation.
- **No leakage.** Features at a readout use only earlier readouts, which a test checks directly.
- **Censoring handled honestly.** A truck still running when observation ended, less than 48 steps after a cut
  point, has an unknown warning window; it is left out of classification training rather than labelled healthy.
- **Fast.** The full dataset validates in about 10 seconds and the feature tables build in about 16 (Polars).

## The live plant

The held-out test trucks are replayed as a running fleet, end to end through the standards a German plant or fleet
operator actually uses, and scored by the champion as their readouts arrive.

```
 fleet simulator         edge gateway            Unified Namespace          platform                digital twin
 OPC UA server    ──►    OPC UA client    ──►    MQTT, Sparkplug B   ──►    FastAPI         ──►     Asset Administration
 (IEC 62541)             subscribe + read        (Mosquitto)                score, store            Shell per truck
 40 real trucks          batched per cycle       spBv1.0/scania-fleet       TimescaleDB             (Eclipse BaSyx)
```

- **OPC UA at the machine.** The simulator exposes every truck as `Fleet/Truck_<id>` with its specification,
  counters and histograms, and writes the time step last so a reader never sees half a readout.
- **Sparkplug B on MQTT.** The gateway announces itself and each truck (NBIRTH, DBIRTH with the specification),
  registers NDEATH as its last will, and publishes every readout as DDATA with a sequence number. Payloads use the
  official Eclipse Tahu schema.
- **Exactly-once effect on an at-least-once wire.** MQTT QoS 1 can deliver twice, so storing a readout is idempotent
  (a per-truck advisory lock and an insert that skips a readout already stored). Replaying a whole run stores nothing
  twice; repeats and sequence gaps are counted on `/health` instead of disappearing.
- **Micro-batched scoring.** Every truck that reported within 250 ms is scored in one call, which shares the fixed
  cost of building features: about 7 ms per truck in a batch of 40, against 190 ms for one truck alone. A truck with
  several new readouts is scored once, on its latest state.
- **The same score online and offline.** Serving rebuilds features from raw stored readouts; a test checks that the
  result equals the offline feature table's score on real test trucks. Serving loads an exported bundle, so it does
  not need MLflow at run time.
- **Digital twin.** Each truck is an Asset Administration Shell (IEC 63278) with a Specification and a Health
  submodel: risk within 48 steps, the cost-optimal alert, the conformal window set, the window probabilities and the
  top drivers. Updates are pushed through the standard AAS API v3, so any compliant repository works, not just BaSyx.
- **Time series storage.** Readouts and predictions are TimescaleDB hypertables with retention policies (90 and 365
  days by default).

**Measured on this machine**, 40 trucks reporting every second: every truck's readouts arrived complete and in order
up to its last recorded readout, with 0 sequence gaps, 0 duplicates and the scoring queue never above one batch.

## Monitoring and the model lifecycle

```
 platform ──► /metrics ──► Prometheus ──► Grafana dashboard, alert rules
    │
    ├─► drift monitor (PSI against the training holdout, in the serving bundle)
    │       │ "drift"
    │       ▼
    │   Dagster sensor ──► retrain job ──► MLflow: new challenger ──► exported bundle
    │                                                                    │ hot reload
    └─◄─────────────── challenger scored in shadow on the same rows ◄────┘
                               │
                       predmaint promote (gate) ──► champion, old one kept as `previous`
```

- **Drift against what the model was evaluated on.** Each serving bundle carries a reference profile built from
  20,000 holdout cut points: decile edges for the 86 numeric features the model uses, and for its risk output.
  Live, the last 2,000 scored rows are compared with it by PSI every 10 seconds.
- **Two verdicts, two actions.** *Feature shift*: a few features moved while the fleet and the model output did
  not, which points at a sensor or the data pipeline, so it raises an alert to investigate and never retrains
  (retraining on a broken sensor teaches the model the fault). *Drift*: a fifth of the features or the model output
  moved, so the population has changed and a Dagster sensor starts the retraining job, at most once a day.
- **What it found.** Replaying the test trucks, the live monitor reported drift from the first minute, led by
  `h397_rate`, `h167_rate` and `h459_rate`: the same features, at similar magnitudes, as the offline split analysis
  above, reached independently from live readouts. That agreement is the check that the monitor measures the data
  and not the replay.
- **Shadow before promotion.** A new challenger is exported and hot-reloaded by serving without a restart, then
  scored on the very same feature rows as the champion and stored under its own role. `predmaint promote` passes
  only if the challenger has a lower validation cost, at least 500 shadow assessments, and does not raise the share
  of trucks sent to the workshop by more than 5 points. A retrain on unchanged data (version 2, identical to the
  champion: 3,254 shadow assessments, 100% alert agreement) is correctly refused for not being better.
- **Prometheus and Grafana.** Ingest, scoring latency, queue, alerts per warning window, shadow agreement, drift
  per feature and twin updates as metrics; seven alert rules (drift, feature shift, sequence gaps, backlog, slow
  scoring, failing twin updates, platform down); a provisioned dashboard that reads Prometheus and TimescaleDB.
- **ONNX, measured and not adopted.** `predmaint onnx-eval` runs the champion through ONNX Runtime on all 5,046
  validation trucks. It is faster in bulk (about 160 ms against 180 to 195 ms) but slower at the live batch size
  (5 to 9 ms against 3 ms for 40 trucks), and ONNX trees compare in 32-bit floats, which moves probabilities by up
  to 0.029 and changes one truck's alert. The model call is a few milliseconds of a batch dominated by feature
  building, so there is nothing for ONNX to win.

**Measured**, 120 trucks coming online over a minute with the challenger in shadow: about 39 readouts a second
sustained, 0 sequence gaps, the queue peaking at 65 trucks and draining, and a scoring batch of about 39 trucks
taking 0.8 s at the median and 2.3 s at the 95th percentile. Features are rebuilt from each truck's full history
on every batch, which keeps live scores identical to offline ones; loading only the window the features need is
the next optimisation, with the parity test as its guard.

## The dashboard

A React app for the people who plan maintenance, served by nginx next to the API:

- **Fleet**: every truck's risk within 48 steps, its recommended action and its 90% window set, live, filterable
  by action.
- **Truck**: the risk over time, the probability of each failure window, the expected cost of every possible
  decision (why this action and not the next one), the drivers in plain words, and the truck's Asset
  Administration Shell as stored in BaSyx.
- **Workshop plan**: given N free slots, the trucks that save the most expected cost by coming in now, and what is
  left uncovered.
- **Score a file**: upload readouts and specifications in SCANIA's published CSV format and get every truck
  scored at its last readout, with the drivers and a CSV download. Twelve held-out test trucks are one click away.
- **Models and drift**: champion against challenger, the promotion gate check by check with a promote button that
  only works when every check passes, and the drift verdict with the most shifted features.
- **Copilot**: questions in plain language (below).

The decision arithmetic lives in one Python module used by the API, the copilot and the dashboard alike, so the
three can never disagree.

## Maintenance copilot and MCP server

Six read-only tools over the live platform: fleet overview, truck status, explain a decision (the expected cost of
every action under SCANIA's cost matrix), plan the workshop, drift status and model status. They are defined once
and served two ways:

- **A copilot** (`POST /copilot`, `predmaint ask`, the dashboard's Copilot page): a tool-calling agent over any
  OpenAI-compatible API, DeepSeek by default. The system prompt requires every number to come from a tool result,
  and every answer comes back with its full tool trace so each figure can be checked. Asked "Which three trucks
  need attention most, and why the top one?", it called five tools and answered with the trucks, their risk, the
  cost comparison (6.61 to send truck 29171 in now against 310.65 for doing nothing) and the drivers; asked about
  tomorrow's weather, it said it has no tool for that.
- **An MCP server** (`predmaint mcp`): the same tools, plus the cost matrix as a resource, for Claude Desktop,
  Claude Code or any MCP client. Tested over stdio with the official client.

The language model never touches the database or the API directly, and nothing it can call changes the fleet, the
models or the data. Tests run the agent loop against a scripted model, so CI needs no key.

## Security

Secrets live only in environment variables or a gitignored `.env` (see `.env.example`) and are typed as
`SecretStr`, so they never appear in logs or errors. Every push is scanned across the whole history by gitleaks in
CI, and a pre-commit hook runs the same scan before each commit. The dashboard is served with a strict Content
Security Policy, and nginx and the platform image run as non-root users. See [SECURITY.md](SECURITY.md).

## Run it

Requires [uv](https://docs.astral.sh/uv/) and Python 3.13.

```bash
uv sync
uv run predmaint download    # about 1.65 GB, verified file by file
uv run predmaint prepare     # validate and convert to Parquet
uv run predmaint features    # build the modelling tables
uv run predmaint train       # compare models, register the best in MLflow
uv run predmaint ablation    # does each feature group earn its place?
```

Browse runs and the model registry with `uv run mlflow ui --backend-store-uri sqlite:///data/mlflow/mlflow.db`.

Or run the same steps as Dagster assets with lineage: `uv run dagster dev`, then open http://localhost:3000.

Then the live plant, after `uv run predmaint export` (writes the champion bundle to `data/serving/champion`):

```bash
docker compose up -d                                   # TimescaleDB, Mosquitto, BaSyx
PREDMAINT_MQTT_HOST=localhost PREDMAINT_AAS_URL=http://localhost:8081 uv run predmaint serve
uv run predmaint simulate --trucks 40 --interval 1.0   # OPC UA server on port 4840
uv run predmaint gateway                               # OPC UA to Sparkplug B
```

The dashboard, against the running platform:

```bash
cd frontend && npm ci && npm run dev         # http://localhost:5173
```

Or everything in containers: `docker compose --profile plant up -d --build`, with the dashboard at
http://localhost:8088. The API is at http://localhost:8010 (interactive docs at `/docs`), the twins at
http://localhost:8081/shells, Grafana at http://localhost:3001 and Prometheus at http://localhost:9090.

The copilot needs a key: copy `.env.example` to `.env` and set `PREDMAINT_LLM_API_KEY`. Then
`uv run predmaint ask "Which trucks should come in this week?"`, or connect an MCP client to `uv run predmaint mcp`:

```json
{ "mcpServers": { "predmaint": { "command": "uv", "args": ["run", "--directory", "/path/to/repo", "predmaint", "mcp"] } } }
```

The model lifecycle:

```bash
uv run predmaint simulate --trucks 120 --stagger 60 --drift-after 100 --drift-factor 3   # recalibrate a counter
curl localhost:8010/monitoring/drift          # the verdict; /monitoring/report is the HTML report
uv run predmaint skew                         # training against serving skew of the published splits
uv run dagster job execute -m predmaint.pipeline.definitions -j retrain   # or start drift_sensor in the UI
uv run predmaint export --alias challenger    # serving picks it up and scores it in shadow
uv run predmaint promote --dry-run            # the gate's verdict and reasons
uv run predmaint rollback                     # put the previous champion back
uv sync --group onnx && uv run predmaint onnx-eval
```

Checks: `uv run pytest`, `uv run ruff check .`, `uv run mypy`.

## Documentation

[Model card](docs/model_card.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

## Licence

Code: Apache 2.0. Data: CC BY 4.0, Scania CV AB; cite Kharazian et al., Scientific Data 12, 493 (2025).
