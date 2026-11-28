# AI Refusal Map

**Mapping the boundaries of artificial intelligence.**

AI Refusal Map is a research instrument for examining how large language models and AI assistants navigate requests along safety, policy, and capability boundaries. Rather than reducing assistant behavior to a binary compliant/refused label, it models a multi-dimensional taxonomy: full compliance, partial compliance, clarification requests, conditional assistance, full refusal, and non-answers.

The project bundles a responsive Next.js research observatory, a versioned taxonomy, a high-performance FastAPI service backed by DuckDB and SQLite, and a streaming, privacy-preserving WildChat ingestion pipeline.

[![Overview Screenshot](docs/screenshots/overview.png)](docs/screenshots/overview.png)

> **Evidence Status:** The browser demonstration uses 16 explicit synthetic fixtures designed to exercise layout, filtering, and annotation interactions without requiring local storage of massive datasets. Their counts and percentages describe only those fixtures; they are not WildChat findings, evaluation results, human annotations, or current model behavior. No real WildChat records are bundled.

---

## Key Features

- **Multi-Dimensional Taxonomy:** Categorizes responses across 6 compliance outcomes, 10 stated reasons (safety, privacy, policy, uncertainty, etc.), 6 justification levels, and 9 alternative assistance types.
- **Interactive Research Observatory:** Responsive Next.js 16 web application featuring real-time filtering by model identifier and request domain, SVG donut distribution charts, time-series visualization, semantic point-cloud landscape, and dark/light themes.
- **Human Annotation Practice Studio:** In-browser review workflow with queue navigation, prompt/response inspection, evaluation rubric guidelines, and local storage persistence.
- **Streaming WildChat Ingestion:** Memory-bounded ingestion pipeline for the public `allenai/WildChat-4.8M` dataset with cryptographic revision pinning, automatic regex-based PII sanitization (emails, phone numbers, IP addresses), and heuristic candidate cue detection.
- **Leak-Free Request Feature Extraction:** Dedicated workflow extracting word counts, sentence counts, questions, negations, and quoted spans exclusively from user requests—guaranteeing zero response-column leakage for unbiased request-side modeling.
- **Stratified Annotation Queue Sampler:** Seeded, reproducible two-pass reservoir sampling supporting uniform and signal-stratified sampling with documented inclusion probabilities.
- **Research API & Analytics Engine:** FastAPI service utilizing DuckDB for zero-copy Parquet querying, SQLite for revision-tracked human annotations, and OpenAPI/Swagger documentation.

---

## Visual Showcase

### Refusal Landscape

A 2D semantic space explorer clustering request-response pairs across compliance outcomes.

[![Refusal Landscape](docs/screenshots/refusal-landscape.png)](docs/screenshots/refusal-landscape.png)

### Refusal Analysis & Pattern Breakdown

Detailed outcome analysis breaking down response distributions, stated justifications, and redirection strategies.

[![Refusal Analysis](docs/screenshots/refusal-analysis.png)](docs/screenshots/refusal-analysis.png)

### Conversation Explorer

Sanitized, turn-aware prompt-response inspection interface with outcome pills and domain tags.

[![Conversation Explorer](docs/screenshots/conversation-explorer.png)](docs/screenshots/conversation-explorer.png)

### Annotation Studio

Human review workflow displaying example prompts, assistant replies, evaluation rubrics, and classification controls.

[![Annotation Studio](docs/screenshots/annotation-studio.png)](docs/screenshots/annotation-studio.png)

### Model Comparison

Observational comparison across model identifiers recorded in historical conversation traces.

[![Model Comparison](docs/screenshots/model-comparison.png)](docs/screenshots/model-comparison.png)

### Interactive FastAPI Documentation

Interactive Swagger documentation for all analytical and annotation endpoints.

[![API Documentation](docs/screenshots/api-docs.png)](docs/screenshots/api-docs.png)

---

## Architecture

```text
WildChat Public Train Stream
        │
        │ Schema validation · Git revision SHA pin · PII redaction
        ▼
Normalized Parquet (data/processed/<revision>/)
        │
        ├──► Feature Extraction (research/workflows.py) ──► requests.parquet (request-only)
        │
        ├──► Stratified Sampler (research/workflows.py) ──► annotation-queue.parquet
        │
        └──► FastAPI Service (apps/api) ──► DuckDB Read-Only Query Engine
                     ▲                              │
                     │ Bearer Token Auth            ▼
              SQLite Annotation Store        Analytical Endpoints (/api/v1/...)
              (data/annotations.sqlite3)

Browser Observatory (apps/web)
        ├── Standalone synthetic demonstration fixtures (16 curated examples)
        ├── Client-side search, filtering, CSV export & local annotation
        └── Research documentation & methodology guidelines
```

For in-depth design documents, consult the project documentation:

- [Architecture](docs/architecture.md)
- [Dataset Specifications](docs/dataset.md)
- [Data Card](docs/data-card.md)
- [Taxonomy Reference](docs/taxonomy.md)
- [Annotation Guide](docs/annotation-guide.md)
- [Evaluation Protocol](docs/evaluation.md)
- [Statistical Methods](docs/statistical-methods.md)
- [Privacy & Sanitization](docs/privacy.md)
- [Deployment & Security](docs/deployment.md)
- [Reproducibility](docs/reproducibility.md)

---

## Getting Started

### Prerequisites

- **Node.js**: v22.0.0 or newer
- **pnpm**: v10.0.0 or newer
- **Python**: v3.12 or newer
- **uv**: Modern Python package manager

### Installation

Clone the repository and install both JavaScript and Python dependencies:

```sh
# Install workspace dependencies
make setup

# Or manually:
pnpm install
uv sync --group dev
```

### Running the Web Observatory

```sh
# Start Next.js development server
pnpm dev

# Or using Make:
make dev
```

Navigate to `http://localhost:3000` (or `http://127.0.0.1:3000`). The web application runs fully offline with synthetic fixtures—no corpus download or API key required.

### Running the Research API

In a separate terminal, start the FastAPI backend:

```sh
make api

# Or directly:
uv run uvicorn arm_api.main:app --app-dir apps/api --reload --port 8000
```

Interactive API documentation will be available at `http://localhost:8000/docs`.

_Note on Port Conflicts:_ If port 8000 is occupied by another local service on your machine, launch on an alternate port:

```sh
uv run uvicorn arm_api.main:app --app-dir apps/api --reload --port 8001
```

---

## Configuration

Environment variables can be set via `.env` or system environment. An example template is provided in `.env.example`:

| Variable                           | Default                                       | Description                                                          |
| :--------------------------------- | :-------------------------------------------- | :------------------------------------------------------------------- |
| `ARM_API_TOKEN`                    | _empty_                                       | Optional bearer token for authorizing annotation creation and edits. |
| `ARM_ALLOW_UNAUTHENTICATED_WRITES` | `false`                                       | When true, permits annotation modifications without bearer auth.     |
| `ARM_DATA_DIR`                     | `data/processed`                              | Path to directory containing normalized Parquet files.               |
| `ARM_ANNOTATION_DB`                | `data/annotations.sqlite3`                    | SQLite database file for human annotations.                          |
| `ARM_DUCKDB_FILE`                  | `data/analysis.duckdb`                        | DuckDB database path for cached analytical queries.                  |
| `ARM_CORS_ORIGINS`                 | `http://localhost:3000,http://127.0.0.1:3000` | Comma-delimited allowed CORS origins.                                |

---

## Research Workflow & CLI

### 1. Ingesting & Sanitizing WildChat

The importer streams the public [WildChat-4.8M dataset](https://huggingface.co/datasets/allenai/WildChat-4.8M) train split directly, excluding IP hashes, headers, state, country, and raw moderation payloads:

```sh
# Stream a bounded sample of 1,000 conversations
uv run python research/ingestion/wildchat.py \
  --profile research --revision main --limit 1000 --seed 42 \
  --batch-size 500 --output data/processed
```

Options:

- `--resume`: Continue from the last saved `checkpoint.json`.
- `--profile full`: Ingest the entire accessible corpus (removes the sample limit).
- `--language`: Filter by language (e.g. `--language English`).
- `--model`: Filter by model identifier (e.g. `--model gpt-4`).

### 2. Request-Side Feature Extraction

Extract structural and syntactic features from user requests while strictly omitting assistant responses:

```sh
make features \
  INPUT=data/processed/<revision>/pairs-0000000.parquet \
  OUTPUT=data/features/requests.parquet
```

Extracted features:

- `request_chars`: Character count.
- `request_words`: Unicode-aware word count.
- `request_sentences`: Sentence count.
- `contains_question`: Boolean indicator for question marks.
- `contains_negation`: Indicator for negative tokens (`not`, `never`, `cannot`, etc.).
- `contains_quoted_text`: Indicator for quoted strings.

### 3. Annotation Queue Sampling

Extract a reproducible subset for human review using seeded reservoir sampling:

```sh
make sample \
  INPUT=data/processed/<revision>/pairs-0000000.parquet \
  OUTPUT=data/curated/annotation-queue.parquet \
  SIZE=200 SEED=42 STRATIFIED=1
```

Each sampled row records its `sampling_stratum`, `sampling_probability`, and `sampling_seed`.

---

## API Endpoints

| Method  | Endpoint                       | Description                                                                |
| :------ | :----------------------------- | :------------------------------------------------------------------------- |
| `GET`   | `/api/v1/health`               | Service health status and corpus load state.                               |
| `GET`   | `/api/v1/taxonomy`             | Active taxonomy definitions, versions, and quality scales.                 |
| `GET`   | `/api/v1/datasets`             | Metadata on loaded local Parquet files.                                    |
| `GET`   | `/api/v1/filters`              | Distinct models, languages, domains, and outcomes in data.                 |
| `GET`   | `/api/v1/overview`             | Aggregated record count and high-level distribution.                       |
| `GET`   | `/api/v1/analysis/{dimension}` | Grouped distribution over `outcomes`, `domains`, `models`, or `languages`. |
| `GET`   | `/api/v1/conversations`        | Paginated turn-pair records with optional filters.                         |
| `GET`   | `/api/v1/annotations`          | Retrieve list of recorded human annotations.                               |
| `POST`  | `/api/v1/annotations`          | Create a new human annotation (requires Bearer token if configured).       |
| `PATCH` | `/api/v1/annotations/{id}`     | Update an existing annotation, incrementing revision counter.              |

---

## Verification & Testing

The repository maintains an automated test and verification suite:

```sh
# Run pytest unit and integration test suite
make test

# Run code formatters and linters (Ruff + Biome)
make lint

# Run typecheckers (Pyright + TypeScript)
make typecheck

# Verify Next.js production build
make build
```

---

## Limitations & Methodological Scope

- **Corpus Selection Bias:** The accessible WildChat-4.8M dataset explicitly excludes conversations flagged toxic by moderation pipelines. Observed refusal rates describe only this filtered corpus and cannot represent the full distribution of wild interactions.
- **Synthetic Demonstration:** The browser interface operates on 16 synthetic fixtures to allow instant local inspection without heavy downloads. These numbers do not reflect empirical measurements.
- **Candidate Signals vs. Final Labels:** Ingestion heuristics (`rule_1` through `rule_5`) identify candidate phrases (e.g., _"I cannot assist with..."_) for triage; they are not adjudicated refusal classifications.
- **Stated vs. Actual Reasoning:** Model-stated explanations may reflect post-hoc rationalizations rather than internal latent representations.

---

## License & Custom Work

[![Hire me](https://img.shields.io/badge/Open%20to%20work-work%40withrana.com-brightgreen)](mailto:work@withrana.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-workwithrana-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/workwithrana)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-14A800?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01bbcf6edb91a8df5f)
[![Contra](https://img.shields.io/badge/Contra-Hire%20Me-000000?style=flat)](https://contra.com/ranajahanzaib/)

**License:** MIT, see [LICENSE](LICENSE). Free for personal, academic, and commercial use.

**Author:** Rana Jahanzaib

**Need this built for your stack?** Email me what you’re working on: [work@withrana.com](mailto:work@withrana.com)
