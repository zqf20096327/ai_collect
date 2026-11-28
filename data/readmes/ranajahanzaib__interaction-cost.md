# InteractionCost

**Understanding the conversational effort behind every request.**

InteractionCost is a local-first research platform for studying how the structure of an initial user request relates to observed human–AI conversation patterns. It extracts a transparent 22-signal feature registry directly from the initial prompt and models two empirical interaction targets: **observed user-message count** and **follow-up probability**.

> [!NOTE]
> Predictions describe empirical interaction patterns in observed datasets—not measures of task complexity, user satisfaction, model intelligence, or human effort.

![InteractionCost Overview](docs/screenshots/overview.png)

---

## Key Features

- **Responsive Prediction Laboratory**: Interactive Next.js dark editorial interface with real-time prompt analysis, transparent keyword heuristic domains, and feature contribution signals.
- **Transparent Feature Registry**: 22 deterministic syntactic and structural signals extracted strictly from the initial request (character/word counts, lexical density, constraint markers, punctuation ratios).
- **FastAPI Analytical Engine**: High-performance local backend with strict Pydantic validation, bounded batch (`/api/v1/predict/batch`), and comparison (`/api/v1/predict/compare`) routes.
- **DuckDB-Powered Analytics**: Zero-copy queries over compressed Parquet datasets (`/api/v1/analytics/overview`, `distributions`, `languages`, `correlations`, and `conversation-patterns`).
- **Leakage-Aware Training Pipeline**: Grouped duplicate-aware holdout training (`GroupShuffleSplit`) ensuring identical prompt variations never leak across train/test splits.
- **Dual Inference Modes**: Runs seamlessly in deterministic synthetic demonstration mode or against locally fitted Scikit-Learn baseline models with fingerprint verification.
- **Privacy & Data Governance**: Canonical conversation normalization with automatic email and phone redaction, field allowlisting, and no transcript persistence.

---

## Visual Showcase & Workflows

### 1. The Prediction Laboratory

Test initial requests interactively. The laboratory predicts expected user turns and follow-up probability while rendering the top structural feature contributions.

![Prediction Laboratory](docs/screenshots/lab-prediction.png)

### 2. CLI Normalization & Training Pipeline

Stream or import source conversations, normalize records to compressed Parquet with SHA-256 manifests, and fit leakage-aware baselines directly from the terminal.

![CLI Pipeline Demo](docs/screenshots/cli-demo.svg)

### 3. Research Observatory & Analytics

Inspect observed conversation distributions, median user turns, follow-up prevalence, and multilingual breakdowns computed in-memory via DuckDB.

![Research Overview](docs/screenshots/research-overview.png)

### 4. Feature Intelligence & Request Comparison

Inspect the 22 deterministic features or contrast two prompt formulations to evaluate structural shifts.

|                        Feature Intelligence                        |                       Request Comparison                       |
| :----------------------------------------------------------------: | :------------------------------------------------------------: |
| ![Feature Intelligence](docs/screenshots/feature-intelligence.png) | ![Request Comparison](docs/screenshots/request-comparison.png) |

---

## Architecture

```text
Initial Request ──> FastAPI Validation ──> Shared Feature Extractor ──> Local Model
                                                    │                   └─> Predictions + Limits
Source Records  ──> Private JSONL      ──> Normalization/Redaction  ──> Parquet (DuckDB)
                                                                        └─> Labels & Baseline Training
Next.js App Router ──> Local Versioned REST API (/api/v1)
```

- `apps/web`: Next.js 16 App Router application (strict TypeScript, Tailwind CSS).
- `src/interactioncost`: FastAPI backend, 22-signal feature extraction, JSONL normalization, and training pipeline.
- `tests`: Hermetic test suite covering API contracts, normalization, feature extraction, and model training.
- `docs/`: Dataset provenance, evaluation, methodology, limitations, and API documentation.

---

## Quick Start

### Prerequisites

- **Python 3.12+** and [uv](https://github.com/astral-sh/uv)
- **Node.js 20.9+** and [pnpm](https://pnpm.io/)
- _(Optional)_ **Docker Compose** for containerized execution

### 1. Installation

```sh
# Clone repository
git clone https://github.com/ranajahanzaib/interaction-cost.git
cd interaction-cost

# Install Python dependencies and locked web packages
uv sync --all-groups
cd apps/web && pnpm install --frozen-lockfile && cd ../..
```

### 2. Running Locally

Start both the FastAPI backend and Next.js frontend concurrently:

```sh
make dev
```

- **Web Application**: [http://localhost:3000](http://localhost:3000)
- **FastAPI Service**: [http://localhost:8000](http://localhost:8000)
- **Interactive Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

_Note: If ports 3000 or 8000 are occupied, configure `WEB_PORT` and `API_PORT` (e.g. `WEB_PORT=3010 API_PORT=8010 make dev`)._

### 3. Synthetic Demo Mode vs. Trained Model Mode

- **Synthetic Demo Mode** (`INTERACTIONCOST_DEMO_MODE=true`): Default mode. Generates deterministic illustrative predictions without requiring an external dataset.
- **Trained Model Mode** (`INTERACTIONCOST_DEMO_MODE=false`): Loads your locally trained artifact at `artifacts/models/interactioncost.joblib`.

---

## CLI & Pipeline Workflows

### 1. Normalize Conversations to Parquet

Prepare raw JSONL conversation exports into private, redacted Parquet with strict field allowlisting:

```sh
uv run interactioncost prepare-jsonl data/raw/export.jsonl data/processed/conversations.parquet \
  --source wildchat-demo --revision v1
```

### 2. Fit Baseline Prediction Models

Train HistGradientBoosting regressors and classifiers with grouped duplicate-aware splitting:

```sh
uv run interactioncost train data/processed/conversations.parquet \
  --output artifacts/models/interactioncost.joblib --max-rows 100000
```

The holdout evaluation metrics are written directly to `artifacts/models/interactioncost.metrics.json`:

```json
{
  "test_rows": 21,
  "train_rows": 81,
  "turn_count_mae": 0.2844,
  "turn_count_rmse": 0.4282,
  "followup_brier": 0.0012,
  "followup_roc_auc": 1.0,
  "observed_followup_prevalence": 0.4286,
  "sampled_rows": 102
}
```

### 3. Stream Supported Hub Datasets

To stream a permitted research dataset (e.g. WildChat-1M), review the [source terms](docs/DATASETS.md) first, then acknowledge explicitly:

```sh
uv run interactioncost download allenai/WildChat-1M --profile development \
  --output data/processed/conversations.parquet --revision main --accept-source-terms
```

---

## API Usage Examples

### Single Prediction

```sh
curl -s -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Plan a two-week trip to Japan with a daily itinerary, transit options, a $3,000 budget, and rainy-day alternatives."}' | jq
```

**Response:**

```json
{
  "available": true,
  "expected_user_turns": 2.0,
  "followup_probability": 0.9636,
  "domain": [{ "name": "Planning", "method": "transparent keyword heuristic" }],
  "explanations": [
    { "feature": "chars", "value": 115.0 },
    { "feature": "words", "value": 19.0 },
    { "feature": "avg_sentence_words", "value": 19.0 },
    { "feature": "avg_word_chars", "value": 4.84 },
    { "feature": "quantity_constraints", "value": 2.0 }
  ],
  "mode": "trained-model",
  "probability_status": "uncalibrated model score"
}
```

### Batch Prediction

```sh
curl -s -X POST http://localhost:8000/api/v1/predict/batch \
  -H "Content-Type: application/json" \
  -d '{"requests": [{"text": "What is the capital of France?"}, {"text": "Write a compiler in Rust."}]}' | jq
```

### Feature Extraction Only

```sh
curl -s -X POST http://localhost:8000/api/v1/features/extract \
  -H "Content-Type: application/json" \
  -d '{"text": "List 5 items in CSV format."}' | jq .features
```

---

## Testing & Quality Assurance

Run the test suite and static analysis:

```sh
# Run hermetic Python unit tests
uv run pytest

# Run Python linter and formatter
uv run ruff check src tests

# Run frontend type-check, linter, and production build
cd apps/web && pnpm lint && pnpm exec tsc --noEmit && pnpm build
```

Or execute all checks via Make:

```sh
make test
make lint
```

---

## Scientific Boundary & Limitations

1. **Observed Targets Only**: Modeled outcomes are empirical interaction lengths (user turn count and follow-up occurrence). They do not measure human effort, cognitive difficulty, task success, or model capability.
2. **Correlation vs. Causation**: Feature associations indicate predictive correlation in the training distribution. Differences between reworded requests do not imply that editing causes an outcome change.
3. **Weak Labels**: Heuristic clarification, reformulation, and multi-step labels are weak indicators and are not offered as validated ground truth.
4. **Distribution Shift**: A model fitted on conversational assistant data cannot be assumed to generalize to other user populations, task modalities, or system designs.

---

## Community & Security

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](.github/SECURITY.md)
- [Changelog](CHANGELOG.md)
- [Citation Metadata](CITATION.cff)
- [Data Governance & Privacy](docs/DATA-GOVERNANCE.md)

---

## License & Custom Work

[![Hire me](https://img.shields.io/badge/Open%20to%20work-work%40withrana.com-brightgreen)](mailto:work@withrana.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-workwithrana-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/workwithrana)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-14A800?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01bbcf6edb91a8df5f)
[![Contra](https://img.shields.io/badge/Contra-Hire%20Me-000000?style=flat)](https://contra.com/ranajahanzaib/)

**License:** MIT, see [LICENSE](LICENSE). Free for personal, academic, and commercial use.

**Author:** Rana Jahanzaib

**Need this built for your stack?** Email me what you’re working on: work@withrana.com
