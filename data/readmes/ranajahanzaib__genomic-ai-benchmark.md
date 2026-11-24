# Genomic AI Benchmark

An independent, reproducible research observatory for evaluating genomic foundation models, conventional sequence baselines, biological generalization, and sequence leakage across dataset splits.

[![Observatory Dashboard](docs/screenshots/overview.png)](docs/screenshots/overview.png)

---

## Overview

Modern genomic foundation models are frequently evaluated on tasks where sequence homology, reverse-complement equivalence, or substring containment between training and evaluation splits can inflate performance metrics.

**Genomic AI Benchmark** provides a local research observatory and evaluation harness designed to:

- Test biological generalization using **leave-one-species-out cross-validation**.
- Detect cross-split sequence leakage (**exact matches, reverse-complement matches, and substring containment**).
- Validate declared dataset partitions before benchmarking.
- Provide a conventional **3-mer nearest-centroid sequence baseline** to calibrate model expectations.
- Inspect sequence representations, nucleotide coordinates, and model metadata through an interactive workspace.
- Provide full **dark mode** support and **WCAG AA accessible typography** (calibrated font sizes, high-contrast nucleotide base coloring, and responsive data displays).
- Generate deterministic, cryptographically hashed **reproducibility manifests** for every evaluation run.

> **Demonstration Notice:** The included local observatory is a research demo initialized with synthetic promoter sequence fixtures. The Evo 2 adapter adheres to the upstream scoring and embedding interface, but local model inference requires Linux with CUDA and validated weights. Results on synthetic fixtures exercise pipeline mechanics and do not represent biological evidence.

---

## Visual Tour & Interface Showcase

### Benchmark Explorer

Evaluates sequence classification across independent species groups using leave-one-species-out partitioning, computing accuracy, balanced accuracy, macro-F1, per-class metrics, and held-out predictions:

![Benchmark Explorer](docs/screenshots/benchmarks.png)

### Leakage Inspector

Scans declared dataset splits for exact matches, reverse-complement orientation matches, and substring containment to audit split integrity:

![Leakage Inspector](docs/screenshots/leakage-inspector.png)

### Embedding Atlas & Genome Browser

Deterministic 2D projection of sequence composition metrics paired with a nucleotide-level viewer displaying sequence coordinates and color-coded bases (A, C, G, T):

|                                         Embedding Atlas                                          |                                        Genome Browser                                         |
| :----------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: |
| [![Embedding Atlas](docs/screenshots/embedding-atlas.png)](docs/screenshots/embedding-atlas.png) | [![Genome Browser](docs/screenshots/genome-browser.png)](docs/screenshots/genome-browser.png) |

### Model Observatory & Dataset Registry

Track model capabilities, verified architecture metadata, and hardware requirements independently from marketing claims. Import custom FASTA files or retrieve public NCBI nucleotide accessions:

|                                           Model Observatory                                            |                                          Dataset Registry                                           |
| :----------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------: |
| [![Model Observatory](docs/screenshots/model-observatory.png)](docs/screenshots/model-observatory.png) | [![Dataset Registry](docs/screenshots/dataset-registry.png)](docs/screenshots/dataset-registry.png) |

### Experiment Runs & Audit History

Every evaluation and leakage scan is persisted locally in SQLite with its timestamp, status, and full result payload:

![Experiment Runs](docs/screenshots/experiment-runs.png)

---

## Terminal & CLI Workflows

In addition to the web observatory, all evaluation and audit workflows can be executed directly from the command line, emitting reproducibility manifests with fixture digests and runtime metadata:

![CLI Demonstration](docs/screenshots/cli-demo.svg)

### Available CLI Commands

```bash
# Run leave-one-species-out grouped baseline evaluation
.venv/bin/python -m research.cli evaluate --output artifacts/demo-evaluation.json

# Audit dataset splits for exact, reverse-complement, or containment leakage
.venv/bin/python -m research.cli leakage --output artifacts/demo-leakage.json

# Validate declared split labels for species crossings
.venv/bin/python -m research.cli validate-split --output artifacts/demo-split-validation.json
```

Each generated manifest includes:

- `manifest_version`
- `created_at` (ISO 8601 UTC timestamp)
- `python` runtime version
- `fixture_id` and SHA-256 fixture checksum
- Full structured `result` payload

---

## Architecture

The project is structured into three clean layers:

```
genomic-ai-benchmark/
├── apps/
│   └── web/                   # Next.js App Router & interactive research workspace
│       ├── public/            # Static observatory client bundle (app.js, style.css, index.html)
│       └── src/app/           # Next.js workspace wrapper
├── services/
│   └── api/                   # FastAPI backend & SQLite persistence layer
│       ├── main.py            # REST endpoints, CORS, request limits, lifespans
│       ├── app.py             # SQLite storage and fixture seeding
│       └── providers/         # External data providers (rate-limited NCBI EFetch)
├── research/                  # Core scientific algorithms & CLI
│   ├── cli.py                 # Reproducible CLI workflow runner & manifest emitter
│   ├── genomics.py            # k-mer vectorization, leave-one-species-out evaluation, leakage audits
│   └── models/                # Model adapter contracts (Evo 2 StripedHyena 2 adapter)
├── fixtures/                  # Checked-in synthetic sequence fixtures
└── docs/                      # Scientific methodology, architecture, and topic guides
```

---

## Getting Started

### Prerequisites

- **Python 3.11+**
- **Node.js 20+**
- **npm** or **pnpm**

### 1. Installation

Create a Python virtual environment and install the locked dependencies:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.lock
.venv/bin/pip install -r requirements-dev.lock
```

Install frontend dependencies:

```bash
npm --prefix apps/web install
# or: pnpm --dir apps/web install
```

### 2. Configuration (Optional)

Create a local environment configuration if desired:

```bash
# Optional: set custom SQLite database path
export GAB_DATABASE="data/benchmark.sqlite3"

# Optional: set contact email required for public NCBI accession retrieval
export GAB_NCBI_EMAIL="researcher@example.org"
```

### 3. Running Locally

Start the backend API and frontend service:

```bash
# Terminal 1: Start FastAPI Backend (http://127.0.0.1:8000)
.venv/bin/uvicorn services.api.main:app --app-dir . --host 127.0.0.1 --port 8000

# Terminal 2: Start Next.js Observatory (http://127.0.0.1:3000)
npm --prefix apps/web run dev
# or: pnpm --dir apps/web run dev
```

Open **[http://127.0.0.1:3000](http://127.0.0.1:3000)** in your browser. The API initializes `data/benchmark.sqlite3` with synthetic sequence fixtures on first startup.

---

## API Reference

| Method | Endpoint                  | Description                                                              |
| :----- | :------------------------ | :----------------------------------------------------------------------- |
| `GET`  | `/api/health`             | Health check and storage engine status                                   |
| `GET`  | `/api/overview`           | Aggregated sequence, dataset, model, and run counts                      |
| `GET`  | `/api/models`             | Registered model configurations and adapter statuses                     |
| `GET`  | `/api/models/evo2/status` | Runtime diagnostic check for Evo 2 dependencies                          |
| `GET`  | `/api/datasets`           | Dataset registry with provenance metadata                                |
| `GET`  | `/api/sequences`          | Indexed sequence records with species, split, and label                  |
| `GET`  | `/api/runs`               | Persisted evaluation and leakage audit execution history                 |
| `GET`  | `/api/splits/validate`    | Audit declared dataset splits for species group crossings                |
| `POST` | `/api/evaluate`           | Execute grouped leave-one-species-out 3-mer baseline                     |
| `POST` | `/api/leakage`            | Audit sequence corpus for cross-split exact, RC, and containment matches |
| `POST` | `/api/import/fasta`       | Validate and import user-supplied FASTA sequences                        |
| `POST` | `/api/import/ncbi`        | Fetch single versioned accession via NCBI Nucleotide EFetch              |

---

## Verification & Testing

Run the full verification suite across Python and TypeScript components:

```bash
# 1. Run Python test suite (33 unit tests)
.venv/bin/pytest

# 2. Run Ruff code quality and format checks
.venv/bin/ruff check research services/api
.venv/bin/ruff format --check research services/api

# 3. Run Next.js production build, TypeScript typecheck, and ESLint
npm --prefix apps/web run build
npm --prefix apps/web run typecheck
npm --prefix apps/web run lint
```

---

## Documentation

Comprehensive guides on benchmark methodology and system design are available in [`docs/`](docs/):

- [Getting Started](docs/getting-started.md)
- [Architecture & Data Flow](docs/architecture.md)
- [Benchmark Methodology](docs/benchmark-methodology.md)
- [Leakage Detection & Overlap Analysis](docs/leakage-detection.md)
- [Splitting & Biological Generalization](docs/splitting-and-generalization.md)
- [Model Adapters & Runtime Boundaries](docs/model-adapters.md)
- [Reproducibility & Manifests](docs/reproducibility.md)
- [Limitations & Non-Goals](docs/limitations.md)

---


## License & Custom Work

[![Hire me](https://img.shields.io/badge/Open%20to%20work-work%40withrana.com-brightgreen)](mailto:work@withrana.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-workwithrana-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/workwithrana)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-14A800?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01bbcf6edb91a8df5f)
[![Contra](https://img.shields.io/badge/Contra-Hire%20Me-000000?style=flat)](https://contra.com/ranajahanzaib/)

**License:** MIT, see [LICENSE](LICENSE). Free for personal and commercial use.

**Author:** Rana Jahanzaib

**Need this built for your stack?** Email me what you're working on: work@withrana.com
