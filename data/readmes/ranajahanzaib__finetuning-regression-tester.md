# FineTuning Regression Tester

**See what your model gained. See what it forgot.**

FineTuning Regression Tester compares a local language model before and after fine-tuning on the exact same held-out examples. It measures target-task gains, preserved capabilities, pass-to-fail regressions ("forgetting"), and exact case-level output transitions. It operates as an independent evaluation and regression analysis layer around MLX-LM—not another trainer.

![FineTuning Regression Tester Dashboard Overview](docs/screenshots/overview.png)
_Interactive dashboard displaying paired baseline vs. adapted metrics, operational forgetting rates, and the Plotly capability map heatmap._

---

## What Problem It Solves

Fine-tuning a language model on a specialized domain (such as structured JSON extraction) often improves target accuracy while inadvertently degrading general instruction-following, arithmetic, formatting adherence, or abstention capabilities.

Aggregate benchmark scores often hide these regressions because target improvements cancel out retention losses in net accuracy. FineTuning Regression Tester isolates every evaluation case, pairs before-and-after model responses side-by-side, and classifies each transition deterministically:

- **PRESERVED_SUCCESS**: Both baseline and adapted models solved the case correctly.
- **REGRESSION**: The baseline model succeeded, but the adapted model failed (operational forgetting).
- **IMPROVEMENT**: The baseline model failed, and the adapted model succeeded (task adaptation).
- **PRESERVED_FAILURE**: Neither model succeeded.
- **INCONCLUSIVE**: One or both evaluations encountered runtime exceptions, empty outputs, or missing grades.

---

## Key Features

- **Deterministic Data Synthesis**: Generates synthetic product-extraction train, validation, and held-out test splits with strict split-specific entity pools and template families to prevent leakage.
- **Standardized Retention Suite**: Evaluates 80 general capability cases (arithmetic, classification, instruction following, text transformation, extraction), 12 format contracts (JSON, CSV, boolean, numbered lists, plain text), 20 missing-data abstention cases, 10 unsupported-capability refusal cases, and 10 regression sentinels.
- **Deterministic Multi-Modal Graders**: Syntax verification, schema compliance (Pydantic), exact field accuracy, and semantic validation separated from superficial formatting.
- **Rich Offline Artifacts**: Exports machine-readable `manifest.json`, `comparison.json`, `capabilities.json`, `comparisons.csv`, formatted `report.md`, and an offline, zero-dependency `report.html`.
- **Interactive Local Dashboard**: Streamlit and Plotly dashboard featuring a capability change heatmap, multi-dimension regression explorer, and run provenance inspector.
- **Bounded Apple Silicon MLX Integration**: Optional support for 4-bit MLX base inference and LoRA adapter training with explicit memory guardrails.
- **Fully Functional Offline Mode**: Generation, validation, evaluation parsing, paired comparison, report export, and fixture demo operate with zero external network or GPU requirements.

---

## Visual Showcase & Screenshots

### Interactive Streamlit Dashboard

|                           Capability Map & Overview                            |                       Regression Explorer & Case Filter                        |
| :----------------------------------------------------------------------------: | :----------------------------------------------------------------------------: |
|         ![Overview and Capability Map](docs/screenshots/overview.png)          |        ![Regression Explorer](docs/screenshots/regression-explorer.png)        |
| _High-level paired metrics, duration breakdown, and capability delta heatmap._ | _Interactive filtering by transition type, capability, severity, and outcome._ |

### Offline HTML Report & CLI Verification

|                      Self-Contained Offline HTML Report                      |                        Real Terminal CLI Execution                         |
| :--------------------------------------------------------------------------: | :------------------------------------------------------------------------: |
|           ![Offline HTML Report](docs/screenshots/report-html.png)           |            ![CLI Execution Demo](docs/screenshots/cli-demo.svg)            |
| _Standalone HTML export for sharing, archiving, and CI artifact collection._ | _Authentic terminal output from `doctor`, `data validate`, and `compare`._ |

---

## Requirements and Installation

Python 3.11+ is required. Offline analysis runs on macOS, Linux, and Windows. Real model training and inference require macOS on Apple Silicon with `mlx-lm`.

The recommended base model is [`mlx-community/Qwen2.5-1.5B-Instruct-4bit`](https://huggingface.co/mlx-community/Qwen2.5-1.5B-Instruct-4bit). Model weights are not bundled with this repository.

```bash
git clone https://github.com/ranajahanzaib/finetuning-regression-tester.git
cd finetuning-regression-tester

# Standard install with dashboard, dev tools, and model utilities
uv sync --extra dev --extra dashboard --extra models

# On Apple Silicon macOS, add MLX training/inference support:
uv sync --extra dev --extra dashboard --extra models --extra mlx
```

To prefetch the configured model snapshot before inference:

```bash
uv run finetuning-regression-tester model download --config configs/product-extraction.yaml
```

---

## Quick Start: Offline Demo

You can exercise the full analysis pipeline immediately without downloading model weights:

```bash
# 1. Verify runtime dependencies and environment
uv run finetuning-regression-tester doctor

# 2. Generate deterministic synthetic dataset and evaluation suite
uv run finetuning-regression-tester data generate --output data/product

# 3. Validate split hygiene, entity partitioning, and checksums
uv run finetuning-regression-tester data validate --dataset data/product

# 4. Create packaged demo fixtures and generate offline reports
uv run finetuning-regression-tester demo --output demo-results

# 5. Recompute paired comparison directly from evaluation results
uv run finetuning-regression-tester compare \
  --baseline demo-results/baseline_results.jsonl \
  --adapted demo-results/adapted_results.jsonl \
  --output demo-results/recomputed_comparison.json

# 6. Launch the interactive local Streamlit dashboard
uv run finetuning-regression-tester dashboard --comparison demo-results/comparison.json --demo
```

The persistent **DEMO DATA** banner in the dashboard and exported reports explicitly marks fictional fixture outputs.

---

## Complete Experiment Workflow

When working on Apple Silicon with MLX-LM installed, run individual stages or orchestrate the entire pipeline:

### Step-by-Step Execution

```bash
# 1. Generate & validate data
uv run finetuning-regression-tester data generate --output data/product
uv run finetuning-regression-tester data validate --dataset data/product

# 2. Evaluate the unchanged base model on evaluation suite
uv run finetuning-regression-tester baseline \
  --cases data/product/evaluation_cases.jsonl \
  --output runs/manual/baseline_results.jsonl \
  --config configs/product-extraction.yaml

# 3. Train LoRA adapter on training split (bounded smoke preset or full)
uv run finetuning-regression-tester train \
  --dataset data/product \
  --adapter runs/manual/adapter \
  --config configs/product-extraction.yaml \
  --smoke

# 4. Evaluate adapter on the identical evaluation cases
uv run finetuning-regression-tester evaluate \
  --cases data/product/evaluation_cases.jsonl \
  --adapter runs/manual/adapter \
  --output runs/manual/adapted_results.jsonl \
  --config configs/product-extraction.yaml

# 5. Compute paired transitions and metrics
uv run finetuning-regression-tester compare \
  --baseline runs/manual/baseline_results.jsonl \
  --adapted runs/manual/adapted_results.jsonl \
  --output runs/manual/comparison.json

# 6. Export offline reports and launch dashboard
uv run finetuning-regression-tester report \
  --comparison runs/manual/comparison.json \
  --output runs/manual/report

uv run finetuning-regression-tester dashboard \
  --comparison runs/manual/comparison.json
```

### One-Command Orchestration

Run baseline evaluation, bounded training, adapted evaluation, paired comparison, and report generation sequentially in a single command:

```bash
# Standard 160-iteration training preset
uv run finetuning-regression-tester run --config configs/product-extraction.yaml --output runs

# Quick 5-iteration smoke check
uv run finetuning-regression-tester run --config configs/product-extraction.yaml --output runs --smoke

# Inspect planned stages without loading models or training
uv run finetuning-regression-tester run --config configs/product-extraction.yaml --output runs --dry-run
```

---

## CLI Command Reference

| Command          | Description                                                                       | Supported Flags                                                                       |
| ---------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `doctor`         | Inspects Python version, OS platform, memory, and MLX / dependency readiness.     | `--verbose`                                                                           |
| `data generate`  | Generates deterministic synthetic product extraction dataset & retention suites.  | `--output`, `--train`, `--valid`, `--test`, `--seed`                                  |
| `data validate`  | Verifies JSONL schema validity, absence of contamination, and manifest hashes.    | `--dataset`                                                                           |
| `model download` | Explicitly pre-downloads and caches Hugging Face model snapshot.                  | `--config`, `--dry-run`                                                               |
| `baseline`       | Evaluates the unadapted base model against evaluation cases.                      | `--cases`, `--output`, `--config`, `--dry-run`                                        |
| `train`          | Trains a bounded MLX-LM LoRA adapter with gradient checkpointing.                 | `--dataset`, `--adapter`, `--config`, `--smoke`, `--resume-adapter-file`, `--dry-run` |
| `evaluate`       | Evaluates fine-tuned adapter against the identical evaluation cases.              | `--cases`, `--adapter`, `--output`, `--config`, `--dry-run`                           |
| `compare`        | Validates configuration parity and computes paired behavioral transitions.        | `--baseline`, `--adapted`, `--output`                                                 |
| `report`         | Generates `report.md`, `report.html`, `comparisons.csv`, and `capabilities.json`. | `--comparison`, `--output`                                                            |
| `dashboard`      | Launches local Streamlit dashboard with Plotly heatmap and interactive filters.   | `--comparison`, `--demo`                                                              |
| `demo`           | Sets up packaged fixture results and exports without running models.              | `--output`                                                                            |
| `run`            | End-to-end automated pipeline executing all stages sequentially.                  | `--dataset`, `--output`, `--config`, `--smoke`, `--dry-run`                           |

---

## Target Schema and Grading Methodology

### Product Schema

Target extraction instances expect a strict JSON record matching `Product`:

```json
{
  "product_name": "TrailPack 20L",
  "brand": "Acme",
  "price": "79.99",
  "currency": "USD",
  "color": "navy blue",
  "size": "20L",
  "quantity": null
}
```

- **Price**: Must be a decimal string (e.g., `"79.99"`), never a floating-point number.
- **Currency**: Explicit `$` maps to `"USD"`. Currency is never inferred from locale.
- **Missing attributes**: Must be serialized as explicit JSON `null`.
- **Strictness**: Additional keys, prose commentary, or markdown fences outside pure JSON trigger format or schema failure.

### Metric Definitions

- **Accuracy**: Successful graded cases divided by valid cases for that model.
- **Accuracy Change**: Paired adapted accuracy minus baseline accuracy on cases valid for both models (`adapted_accuracy - baseline_accuracy`).
- **Retention Rate**: Preserved successes divided by baseline successes (`preserved_successes / baseline_successes`). Undefined if baseline successes are zero.
- **Forgetting Rate**: Regressions divided by baseline successes (`regressions / baseline_successes`). Undefined if baseline successes are zero.

> [!NOTE]
> Operational regressions reflect observed pass-to-fail transitions on the specific evaluation set, not a theoretical proof of permanent capability erasure. Small sample sizes are exploratory and do not warrant generalized claims about a model's latent weights. See [methodology](docs/methodology.md) and [limitations](docs/limitations.md).

---

## Architecture

```
finetuning_regression_tester/
├── core.py         # Schemas (Product, Case, Result), deterministic generator, graders, comparison logic
├── cli.py          # Typer CLI application orchestrating commands and provenance tracking
├── report.py       # Offline exports (Markdown, standalone HTML, CSV, capability JSON)
├── dashboard.py    # Local Streamlit + Plotly interactive inspection application
├── mlx.py          # Isolated Apple Silicon MLX-LM inference and LoRA subprocess execution
├── config.py       # Pydantic-validated YAML configuration schemas
└── fixtures/       # Packaged fixture evaluation outputs and configuration sidecars
```

See [docs/architecture.md](docs/architecture.md) for detailed component interactions and data flows.

---

## Development and Testing

```bash
# Install development dependencies
uv sync --extra dev --extra dashboard --extra models

# Run code style and lint checks
uv run ruff check .

# Run unit and integration tests
uv run pytest
```

---

## License & Attribution

FineTuning Regression Tester is distributed under the [MIT License](LICENSE).

Model weights are not distributed with this software. The default model (`mlx-community/Qwen2.5-1.5B-Instruct-4bit`) is governed by its respective [Hugging Face model card and licensing terms](https://huggingface.co/mlx-community/Qwen2.5-1.5B-Instruct-4bit).
