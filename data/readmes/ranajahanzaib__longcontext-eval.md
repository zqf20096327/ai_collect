<div align="center">

# LongContext-Eval

### *Understanding conversations beyond the context window.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python: 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](./pyproject.toml)
[![FastAPI: 0.115+](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](./apps/api)
[![Next.js: 15.5](https://img.shields.io/badge/Next.js-15.5-000000?logo=next.js&logoColor=white)](./apps/web)
[![CI: Pytest](https://img.shields.io/badge/Pytest-19%20Passed-brightgreen.svg)](./tests)
[![Reproducibility: Deterministic](https://img.shields.io/badge/Reproducibility-Deterministic%20Fixtures-cyan.svg)](./data/fixtures)

**A rigorous open-source scientific benchmarking platform for evaluating how Large Language Models and context-management systems understand long, naturally occurring human-AI conversations.**

[Overview](#overview) • [Visual Observatory](#visual-observatory--demonstrations) • [Task Taxonomy](#task-taxonomy-7-primary-categories) • [Context Strategies](#context-management-strategies-16-built-in) • [Scientific Integrity](#scientific-integrity--experimental-controls) • [Quickstart](#quickstart) • [CLI Guide](#cli-guide) • [Python SDK](#python-sdk-usage) • [Citation](#citation)

---

<p align="center">
  <img src="docs/screenshots/overview.png" alt="LongContext-Eval Scientific Research Observatory Overview" width="100%" />
</p>

*Figure 1: The LongContext-Eval Research Observatory dashboard showing dataset health, eligible dialogue corpora, token counts, task taxonomy distribution, and active context strategies.*

---

</div>

## Overview

Existing LLM evaluation benchmarks (such as RULER, Needle-in-a-Haystack, or generic question-answering leaderboards) frequently evaluate artificial text concatenation or synthetic key-value insertions.

**LongContext-Eval** was designed from the ground up for naturally occurring, multi-turn dialogues where critical information is scattered across hundreds of turns, topics mutate over time, constraints supersede earlier choices, and entity references require resolving distant context.

### What researchers investigate with LongContext-Eval:

- **Information Retention & Decay**: Exactly what information models retain vs. forget as conversational turns increase.
- **Constraint Tracking**: Whether systems understand when a user requirement has been explicitly superseded (e.g. migrating from MongoDB to PostgreSQL 16) vs. when requirements remain active.
- **Retrieval vs. Truncation**: Whether lexical, dense, hybrid Reciprocal Rank Fusion (RRF), or structured memory outperform recent-window truncation under equivalent token budgets.
- **Temporal Reasoning**: Whether models reconstruct the true chronological ordering of rescheduled events rather than assuming message order equals event order.
- **Abstention Integrity**: Whether systems correctly abstain when answers are missing or unanswerable instead of hallucinating.

---

## Visual Observatory & Demonstrations

LongContext-Eval couples an analytical computational backend with an interactive scientific web observatory.

### 1. Conversation Memory Map

The signature visualization provides an interactive horizontal message timeline rendering every user and assistant turn, token length bars, semantic topic bands, and bezier evidence arcs directly connecting evaluation questions to historical ground-truth turns.

<p align="center">
  <img src="docs/screenshots/memory-map.png" alt="Conversation Memory Map with Bezier Evidence Arcs" width="100%" />
</p>

*Figure 2: The Conversation Memory Map (`/conversations/[id]`) tracing semantic topic bands, active constraints, entity states, and non-linear ground truth evidence links across 80+ conversation turns.*

---

### 2. Multi-Track Scientific Leaderboard

Separates competitive benchmarks into distinct tracks with 95% conversation-clustered bootstrap confidence intervals:
- **Budget-Constrained Track (4K Tokens)**: Rigid memory limits testing selective retrieval algorithms.
- **Budget-Constrained Track (8K Tokens)**: Extended budget evaluating summarization and hybrid fusion.
- **Full-Context Track**: Evaluates entire conversation prefixes with automatic budget overflow flags.
- **Diagnostic Oracle Track**: Isolates reasoning errors from retrieval misses.

<p align="center">
  <img src="docs/screenshots/leaderboard.png" alt="Multi-Track Scientific Leaderboard" width="100%" />
</p>

*Figure 3: Multi-Track Scientific Leaderboard (`/leaderboard`) featuring bootstrap confidence intervals, Kendall's $\tau$ temporal ranking, and task category breakdowns.*

---

### 3. Interactive Context Laboratory

An interactive test bench for empirical experimentation. Researchers can configure token budgets, choose context strategies, inspect selected vs. omitted messages, and trigger real-time evaluations across local or remote model adapters.

<p align="center">
  <img src="docs/screenshots/context-lab.png" alt="Interactive Context Laboratory" width="100%" />
</p>

*Figure 4: Context Laboratory (`/lab`) displaying interactive token budget sliders, strategy selection, token utilization meters, and live model inference.*

---

### 4. Root-Cause Failure Analysis Observatory

Diagnoses model errors using an empirical taxonomy distinguishing **Retrieval Omission** (evidence turns never reached the context window) from **Reasoning Errors** (evidence was retrieved but the model failed to synthesize the answer).

<p align="center">
  <img src="docs/screenshots/failure-analysis.png" alt="Failure Analysis Observatory" width="100%" />
</p>

*Figure 5: Failure Analysis Observatory (`/failures`) classifying failure modes across context strategies and task types.*

---

### 5. Multi-Dimensional Analytical Views

| Context Retention Matrix | Evidence Distance Observatory | Topic River Streamgraph |
| :---: | :---: | :---: |
| [![Context Retention Matrix](docs/screenshots/retention-matrix.png)](docs/screenshots/retention-matrix.png) | [![Evidence Distance Observatory](docs/screenshots/evidence-distance.png)](docs/screenshots/evidence-distance.png) | [![Topic River](docs/screenshots/topic-river.png)](docs/screenshots/topic-river.png) |
| *Strategy vs. task-type correctness heatmap* | *Accuracy degradation over turn distance* | *Dynamic topic emergence and re-entry* |

---

### 6. Automated CLI Diagnostics & Evaluation

The platform includes a CLI interface with built-in system diagnostics and reproducible evaluation commands:

<p align="center">
  <img src="docs/screenshots/cli-demo.svg" alt="LongContext-Eval CLI Terminal Session" width="100%" />
</p>

*Figure 6: Terminal session recording of `longcontext-eval doctor` and `longcontext-eval evaluate`.*

---

## Task Taxonomy (7 Primary Categories)

| Task Category                      | Evaluated Challenge                                                     | Key Metrics                                                        |
| ---------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **01. Fact Retrieval**             | Recovering isolated facts across distant distractor topics              | Exact Match, Normalized EM, Token F1, Distance Degradation         |
| **02. Constraint Tracking**        | Preserving evolving constraints and discarding superseded rules         | Active Constraint Recall, Superseded Rejection Rate, Constraint F1 |
| **03. Temporal Ordering**          | Chronological ordering of events, relative dates, and rescheduled plans | Pairwise Ordering Accuracy, Exact Sequence Match, Kendall's $\tau$ |
| **04. Entity Resolution**          | Resolving ambiguous pronouns, aliases, and project identifiers          | Entity Identification Accuracy, Mention Span F1                    |
| **05. Contradiction Detection**    | Distinguishing explicit updates from unresolved contradictions          | Macro F1, False-Positive Contradiction Rate                        |
| **06. Conversation Summarization** | Preserving atomic information units and architectural decisions         | Fact Coverage, Decision Retention, Redundancy Ratio                |
| **07. Topic Retrieval**            | Locating earlier discussions and re-entry points after divergence       | Recall@K, Precision@K, Segment Overlap, MRR, nDCG                  |

---

## Context-Management Strategies (16 Built-in)

Every strategy implements a unified prefix-bounded interface accepting an evaluation question and token budget:

- `no_context`: Zero conversation history ablation baseline.
- `full_context`: Entire conversation prefix when it fits within context budget.
- `recent_window`: Most recent turns fitting within the token budget.
- `first_and_last`: 50% budget allocated to early setup, 50% to recent messages.
- `random_selection`: Deterministic pseudo-random sampling baseline.
- `bm25`: Lexical BM25 Okapi term matching over conversational chunks.
- `dense_retrieval`: Normalized dense vector semantic retrieval.
- `hybrid_retrieval`: Lexical BM25 + Dense vector Reciprocal Rank Fusion (RRF).
- `mmr_retrieval`: Maximal Marginal Relevance balancing relevance and diversity.
- `reranked_retrieval`: Hybrid retrieval followed by cross-encoder re-scoring.
- `topic_aware`: Segment-level retrieval focused on coherent topic clusters.
- `hierarchical`: High-level table-of-contents summary followed by detailed turns.
- `rolling_summary`: Incremental executive compression of historical dialogue.
- `summary_plus_retrieval`: Executive dialogue summary paired with top retrieved turns.
- `structured_memory`: Explicit state tables tracking constraints, entities, and decisions.
- `oracle_evidence`: Ground-truth diagnostic upper bound (strictly separated from competitive tracks).

---

## Scientific Integrity & Experimental Controls

LongContext-Eval enforces strict architectural boundaries to eliminate benchmark contamination and methodological artifacts:

1. **Strict Prefix Boundary**: Retrieval engines, context strategies, and vector indices are strictly forbidden from indexing or observing conversation turns past `context_cutoff`.
2. **Contamination Control**: All evaluation tasks derived from a conversation ID are strictly grouped into the same split (Train, Dev, or Test). Ground truth answers never enter prompts or retrieval indices.
3. **Context Budget Enforcement**: Context strategies must strictly respect token budgets. `full_context` experiments exceeding budget raise explicit `budget_exceeded: true` flags rather than silently truncating messages.
4. **Statistical Rigor**: All leaderboard rankings report 95% conversation-clustered bootstrap confidence intervals (1,000 iterations).

---

## Repository Architecture

```text
longcontext-eval/
├── apps/
│   ├── web/                    # Next.js 15 / React 19 / TypeScript / Tailwind CSS / ECharts
│   └── api/                    # FastAPI analytical backend
├── src/
│   └── longcontext/            # Core Python framework
│       ├── api/                # REST endpoints and routing
│       ├── cli.py              # Command-line interface
│       ├── shared/             # Pydantic schemas (Conversation, Task, Result, Strategy)
│       ├── datasets/           # Ingestion, privacy redaction, deduplication, sampling
│       ├── retrieval/          # BM25, Dense Vector, Hybrid RRF, Cross-encoder Reranker
│       ├── context_management/ # 16 Context-management strategies
│       ├── model_adapters/     # Deterministic, OpenAI, vLLM, Ollama, HuggingFace adapters
│       ├── metrics/            # Scientific metrics, Kendall's tau, Clustered Bootstrap CI
│       └── evaluation/         # EvaluationRunner, failure classification, DuckDB storage
├── data/
│   ├── fixtures/               # Deterministic synthetic research benchmark fixtures
│   └── benchmarks/             # Immutable JSON and Parquet experiment artifacts
├── tests/
│   ├── unit/                   # Schema, privacy, and metric unit tests
│   ├── scientific/             # Contamination control and boundary isolation tests
│   └── integration/            # Full end-to-end evaluation runner and API tests
├── docs/
│   └── screenshots/            # Visual observatory captures and terminal proof
├── Makefile                    # Developer workflow automation
├── docker-compose.yml          # Containerized deployment
└── pyproject.toml              # Unified package manifest
```

---

## Quickstart

### Prerequisites

- Python 3.11+ (Python 3.12 recommended)
- `uv` Python package manager
- Node.js 20+ and `pnpm`

### 1. Setup & Installation

```bash
# Clone the repository
git clone https://github.com/ranajahanzaib/longcontext-eval.git
cd longcontext-eval

# Create virtual environment and install dependencies
uv venv --python 3.12 .venv
uv pip install -e ".[dev]"
pnpm install
```

### 2. Run Diagnostics

```bash
.venv/bin/longcontext-eval doctor
```

### 3. Initialize Fixtures & Seed Baselines

```bash
# Ingest deterministic synthetic research fixtures
.venv/bin/longcontext-eval ingest

# Execute baseline evaluation
.venv/bin/longcontext-eval evaluate --strategy hybrid_retrieval --model deterministic-eval-v1
```

### 4. Run Development Servers

```bash
# Start FastAPI backend (port 8000 by default, or configurable via PORT)
.venv/bin/uvicorn longcontext.api.main:app --host 0.0.0.0 --port 8000 --reload &

# Start Next.js frontend (port 3000)
pnpm --filter web dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## CLI Guide

The platform can be operated entirely through the terminal:

```bash
# Run system diagnostic checks
longcontext-eval doctor

# Inspect registered and external datasets
longcontext-eval datasets inspect

# Ingest and validate conversation fixtures
longcontext-eval ingest

# Run benchmark evaluation experiment
longcontext-eval evaluate --strategy hybrid_retrieval --model deterministic-eval-v1 --budget 4096

# List completed experiments
longcontext-eval experiments list

# Start the analytical FastAPI backend
longcontext-eval serve --port 8000
```

---

## Python SDK Usage

LongContext-Eval can be integrated directly into custom evaluation workflows:

```python
from longcontext.datasets.fixtures import build_synthetic_fixtures
from longcontext.evaluation.runner import EvaluationRunner
from longcontext.evaluation.persistence import BenchmarkStorage
from longcontext.shared.schemas import ExperimentConfig

# 1. Load conversation corpora and benchmark tasks
conversations, tasks = build_synthetic_fixtures()

# 2. Configure experiment
config = ExperimentConfig(
    run_id="custom_hybrid_eval",
    name="Hybrid Retrieval (4096 budget)",
    model_id="deterministic-eval-v1",
    strategy_id="hybrid_retrieval",
    token_budget=4096,
    dataset_split="test",
)

# 3. Execute evaluation
runner = EvaluationRunner(conversations)
results = runner.run_experiment(config, tasks)

# 4. Save results to DuckDB storage
storage = BenchmarkStorage("data")
storage.save_experiment(config, results)

print(f"Evaluated {len(results)} tasks. Mean Score: {sum(r.primary_score for r in results)/len(results):.4f}")
```

---

## Testing

Run the full pytest suite:

```bash
.venv/bin/pytest tests/
```

Test coverage includes:
- **Prefix Boundary Enforcement**: Verification that messages past `context_cutoff` are strictly masked from retrieval.
- **Contamination Control**: Verification that grouped splitting keeps all tasks from a conversation within the same split.
- **Metric Verification**: Exact match, normalized EM, token F1, and temporal pairwise ordering accuracy.
- **REST API Endpoints**: Verification of health, overview, strategies, models, and multi-track leaderboard endpoints.

---

## Citation

If you use LongContext-Eval in your research, please cite:

```bibtex
@article{jahanzaib2026longcontext,
  title={LongContext-Eval: Understanding Conversations Beyond the Context Window},
  author={Jahanzaib, Rana},
  journal={Open Source Scientific Benchmarking Repository},
  year={2026},
  url={https://github.com/ranajahanzaib/longcontext-eval}
}
```

---

## License & Custom Work

[![Hire me](https://img.shields.io/badge/Open%20to%20work-work%40withrana.com-brightgreen)](mailto:work@withrana.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-workwithrana-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/workwithrana)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-14A800?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01bbcf6edb91a8df5f)
[![Contra](https://img.shields.io/badge/Contra-Hire%20Me-000000?style=flat)](https://contra.com/ranajahanzaib/)

**License:** MIT, see [LICENSE](LICENSE). Free for personal, academic, and commercial use.

**Author:** Rana Jahanzaib

**Need this built for your stack?** Email me what you're working on: work@withrana.com
