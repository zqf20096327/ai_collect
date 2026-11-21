# filing-qa

> **A research prototype for question answering over financial filings.** Multimodal RAG with
> hybrid retrieval and numeric grounding checks, measured on a 119-question golden set. It has
> not been run as a real deployment.

[![CI/CD](https://github.com/Mattral/filing-qa/actions/workflows/ci.yml/badge.svg)](https://github.com/Mattral/filing-qa/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![HF Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/Mattral/RAG-Financial-Multimodal)

## Status

**Measured** by scripts in this repo, with raw outputs in [`evals/results/`](evals/results/)
([BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md)):

* Golden-set integrity: 119 questions over 16 public filings. All 209 evidence strings were found
  in the source documents, and all 42 calculations reproduce.
* Offline retrieval on those filings, with no reranker: an answer-bearing chunk is in the top 5
  for 71% of questions at default settings.
* Answer quality for one model (`gemini-3.8-flash`) in one run, scored by deterministic checks
  with no LLM judge: the asked-for figure is stated in 68% of answers.

**Not measured:**

* The full ingest path: unstructured parsing, vision chart extraction, reranking, and the
  guardrails and Program-of-Thought calculator inside the pipeline.
* Chart extraction accuracy. The 9 chart questions can also be answered from tables, so they do
  not test the vision path.
* RAGAS or LLM-judged scores, latency under load, and cost per query.
* Any real deployment. The Helm chart and Kubernetes manifests only pass lint and schema checks
  in CI.

Feature claims below carry one of three labels. **Implemented, tested**: covered by tests that
gate CI, and measured where a figure is given. **Implemented, not evaluated**: the code exists,
but its output quality or effect has not been measured, and any unit tests use mocked models or
services. **Not deployed**: the configuration exists but has never run in a real environment.

> **About the history:** this codebase was rebuilt from scratch in 2026. The commits from
> February 2024 at the start of the history are an earlier, unrelated upload: a notebook,
> two pickled data files and an image. Nothing in the rebuild used them, so they were removed
> from the tree in October 2026. They remain in the history (commits `781d919`–`1d08a81`).


---

## System Architecture

![Architecture Pipeline](docs/assets/architecture_pipeline.png)

*Ingestion (top) and query (bottom) pipelines. Every component is pluggable — switch provider by changing one config value.*

---

## Why This System

Financial documents are mixed-media: narrative text, tables, charts, footnotes, cross-references.
Text-only RAG misses data that appears only in charts, and LLMs can state numbers that their
sources do not contain.

| Problem | Approach | Status |
|---|---|---|
| Some data appears only in charts | A vision LLM (GPT-4o / Gemini / Qwen2-VL / local vLLM) describes each chart image at ingest, and the description is indexed with the text | **Implemented, not evaluated.** Whether the extracted values are correct has not been measured |
| Exact figures like `$23.35B` or `TSLA` miss semantic search | Hybrid RRF: dense embeddings + BM25 keyword fused with Reciprocal Rank Fusion | **Implemented, tested.** Evidence hit@5 0.71 at default chunks, tying BM25 alone; 0.53 vs 0.42 at 1,000-char chunks ([Retrieval Quality](#retrieval-quality)) |
| LLMs can state numbers their sources do not contain | Numeric grounding guardrail: flags any number in the answer that does not appear in the retrieved context | **Implemented, tested** by unit tests. The pipeline guardrail has not been run on the golden set. The answer eval uses its own check of the same kind ([Evaluation Quality](#evaluation-quality)) |
| PII in documents reaches external APIs | Parsed document text is redacted before embedding and indexing: Presidio when installed, plus regex patterns for CUSIP, ISIN and account numbers | **Implemented, tested** for the ISIN and CUSIP patterns. Account-number patterns have no test, and CI does not install Presidio. Queries are not redacted |
| One failing provider stops a stage | Vision: ordered provider chain, then skip the image. Parser: fallback to `pypdf`. Generator: retry on a configured fallback model after a 429/503 | **Implemented, tested** for the vision chain and parser fallback, with mocked providers. The generator fallback has no test |

---

## Retrieval Quality

![Retrieval quality, measured](docs/assets/retrieval_measured.png)

Measured offline on the 16 real filings behind the golden dataset (119 questions), using this
repo's BM25, local `bge-small` embeddings and RRF fusion with default settings and no reranker.
*Evidence hit@5* means a top-5 chunk contains the exact supporting text for the answer.

| Strategy (4,000-char chunks, default) | Evidence hit@5 | Doc hit@5 |
|---|---|---|
| BM25 only | 0.71 | 0.87 |
| Dense only | 0.61 | 0.99 |
| **Hybrid RRF** | **0.71** | 0.93 |
| Hybrid RRF + knowledge graph (optional) | 0.72 | 0.90 |

With 1,000-character chunks, hybrid reaches 0.53 versus 0.42 (BM25) and 0.46 (dense), so fusion
helps there. At the default chunk size it only ties BM25. About 3 in 10 questions get no
answer-bearing chunk in the top 5. Full results, method and caveats are in
[BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md). Earlier versions of this README claimed 89%
Recall@5. That figure could not be reproduced and has been withdrawn; the original charts are
kept, with a provenance note, in [BENCHMARK_RESULTS.md section 4](BENCHMARK_RESULTS.md#4-previously-published-figures-not-reproduced).

---

## Quickstart

```bash
git clone https://github.com/Mattral/filing-qa
cd filing-qa
cp .env.example .env          # set OPENAI_API_KEY or GOOGLE_API_KEY
docker compose up -d

curl -X POST http://localhost:8000/api/v1/ingest \
  -F "file=@tesla_10k.pdf" -F "tenant_id=demo"

curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What was gross margin in Q3 2023?", "tenant_id": "demo"}'

# Same query, answer streamed token by token (server-sent events)
curl -N -X POST http://localhost:8000/api/v1/query/stream \
  -H "Content-Type: application/json" \
  -d '{"query": "What was gross margin in Q3 2023?", "tenant_id": "demo"}'
```

Streamed tokens are provisional: guardrails run on the full answer and are reported in the
final `done` event ([REST API docs](docs/api/rest.md#streaming-answers-post-apiv1querystream)).

Or use the CLI:
```bash
pip install -e ".[all]"
filing-qa ingest tesla_10k.pdf --tenant demo
filing-qa query "What was Q3 revenue?" --tenant demo --show-sources
```

---

## Multi-Provider Support

![Provider Matrix](docs/assets/provider_matrix.png)

*Every model-facing layer (text generation, vision, embeddings, vector store) is independently pluggable. Switch via a single `.env` line — zero code changes.*

### Fully open-source / zero-API-cost configuration

```bash
LLM_CONFIG__PROVIDER=local_vllm
LLM_CONFIG__MODEL=meta-llama/Llama-3.1-8B-Instruct
LOCAL_VLLM_GENERATOR_BASE_URL=http://localhost:8090/v1

VISION_CONFIG__PROVIDER=local_vllm
VISION_CONFIG__MODEL=Qwen/Qwen2-VL-7B-Instruct

VECTOR_STORE_CONFIG__EMBEDDING_PROVIDER=local
VECTOR_STORE_CONFIG__EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
```

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8090 --host 0.0.0.0
vllm serve Qwen/Qwen2-VL-7B-Instruct --port 8080 --host 0.0.0.0
```

---

## Evaluation Quality

![Answer quality, measured](docs/assets/answer_quality_measured.png)

* **Golden dataset:** [119 QA pairs](evals/golden_datasets/README.md) over 16 public filings
  from 10 companies. The mix is 56 factual, 24 calculation, 17 comparative, 13 table and 9 chart
  questions. Every figure is traced to a quoted passage in its source document (209/209 verified
  against the primary documents) and every derived number has an arithmetic check.
  Re-checking found errors in 9 of the original 22 samples, and those have been corrected.
* **Scoring:** RAGAS and an LLM-as-judge numeric scorer (needs an OpenAI key), plus two
  deterministic checks that need no LLM: whether the answer states the expected values, and
  whether it cites the expected source document.
* **Answer quality:** run on all 119 questions with `gemini-3.8-flash` over top-5 hybrid
  context, with deterministic scoring:

  | Metric | All 119 | When retrieval found the supporting text (63) |
  |---|---|---|
  | Asked-for figure stated | 0.68 | 0.84 |
  | Cites an expected document | 0.75 | 0.95 |
  | Abstained ("not available") | 0.35 | 0.16 |
  | States a number absent from its context | 0.05 (6 answers) | 0.06 (4 answers) |

  **Number grounding, and its scope.** One model (`gemini-3.8-flash`), one run, on this repo's
  own single-author golden set. All 119 answers were scored automatically by
  `evals/answer_eval.py`, with no LLM judge. Six answers stated a number that does not appear in
  their context. Those six were checked by hand (the repo does not record by whom), and all were
  correct derivations: shares, differences, a ratio, and "flat" restated as 0%. The check cannot
  catch a real number used for the wrong thing. One such case turned up among the headline
  misses: a full-year question answered with Q3 figures. Only flagged answers and headline misses
  were read by hand.

  Most misses are abstentions caused by retrieval. Calculation questions are weakest: the model
  abstained on 15 of 24. Details are in
  [BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md#3-answer-quality-gemini-38-flash-all-119-questions).

```bash
pytest tests/unit/test_golden_dataset.py      # dataset integrity, offline
python -m evals.retrieval_benchmark           # retrieval, offline
python -m evals.answer_eval --rpm 5           # retrieval + generation, needs an LLM key
```

---

## Latency and Cost

Not yet measured in a reproducible run. Earlier latency, load-test and cost-per-query charts
had no committed run outputs, so they are no longer cited. They are kept, with a provenance
note, in [BENCHMARK_RESULTS.md section 4](BENCHMARK_RESULTS.md#4-previously-published-figures-not-reproduced).
The only measured latency so far is generation alone, from the answer eval: p50 3.0 s,
p95 5.0 s with `gemini-3.8-flash`. `tests/load/locustfile.py`
and `scripts/benchmark.py` can measure them against a running deployment. The SLO targets
(p99 < 8 s, < 1% errors) are configured in `src/filing_qa/config.py` and the alerting rules.

---

## SLO Alerting

![SLO Burn Rate](docs/assets/slo_burn_rate.png)

*Design diagram, not live data: it illustrates how the configured alert rules behave and is
not taken from a running deployment. Multi-window multi-burn-rate alerting from the Google
SRE Workbook, with four alert tiers (14.4×, 6×, 3×, 1× burn rate) routing to PagerDuty/OpsGenie.*

---

## Architecture Layers

| Layer | Component | Technology | Status |
|---|---|---|---|
| **Parsing** | PDF text + tables | Unstructured.io / Docling / Marker | **Implemented, tested** for Unstructured, which the CI image smoke test runs on a text-only PDF. Docling and Marker: **implemented, not evaluated**, with no CI test |
| **Vision** | Chart + graph description | GPT-4o / Gemini / Qwen2-VL / local vLLM (fallback chain) | **Implemented, not evaluated.** Unit tests use mocked providers |
| **Layout** | Semantic grouping | Table-caption pairing, multi-page merge, HTML wrapping | **Implemented, tested** |
| **Embedding** | Dense vectors + cache | OpenAI / Voyage / Cohere / local BAAI/bge, Redis cache | **Implemented, tested.** Local `bge-small` is used in the retrieval benchmark. The other providers are tested with mocks. The Redis cache has no test |
| **Indexing** | Vector store | DeepLake / pgvector / Qdrant | **Implemented, tested.** CI runs upsert/reopen/query round trips against real backends |
| **Retrieval** | Hybrid (dense + BM25) | Reciprocal Rank Fusion, k=60 | **Implemented, tested.** Measured offline ([Retrieval Quality](#retrieval-quality)) |
| **Reranking** | Cross-encoder | ms-marco-MiniLM / Cohere Rerank v3 | **Implemented, not evaluated.** On by default, but not part of the retrieval benchmark |
| **Generation** | Cost-routed, multi-provider | OpenAI / Gemini / Anthropic / Local vLLM | **Implemented, tested** with mocked APIs. Only Gemini has been evaluated, with cost routing off |
| **Guardrails** | Numeric grounding + PII | Presidio + custom regex + restricted-interpreter PoT calculator | **Implemented, tested** by unit tests. Not run on the golden set. CI does not install Presidio |
| **API** | REST + OpenAPI | FastAPI + uvicorn | **Implemented, tested** by API tests and the CI image smoke test |
| **Observability** | Traces + metrics | OpenTelemetry + Prometheus + Grafana dashboards | **Implemented, not evaluated.** Grafana dashboards: **not deployed** |
| **Security** | Auth + audit trail | API key; JSONL audit log with a SHA-256 hash of each event | **Implemented, tested.** Event hashes are not chained or keyed |
| **Multi-tenancy** | Isolated namespaces | Per-tenant partitions (BM25, vector-store filters, cache, document registry) + monthly token quotas | **Implemented, tested** by unit tests. A per-tenant rate-limiter module exists, but no API route calls it |
| **Deployment** | Container + K8s | Docker; Helm + HPA + NetworkPolicy | Docker: **implemented, tested**, since CI builds and smoke-tests the image. Helm/K8s: **not deployed**, only linted and schema-validated in CI |

---

## Key Features

### Multimodal ingestion
- **Vision LLM fallback chain** (*implemented, not evaluated*): providers are tried in order,
  and the image is skipped with a logged error if all fail. Extraction quality is unmeasured
- **Layout-aware chunker** (*implemented, tested*): tables stay with their captions; multi-page
  tables merged
- **ColPali visual retrieval** (*implemented, not evaluated*; component only, not yet called by
  the query pipeline): late-interaction MaxSim scoring on page images (no OCR)
- **Delta detection** (*implemented, tested*): skip unchanged documents on re-ingest; per-document
  version history with point-in-time lookup

### Retrieval
- **Hybrid RRF (k=60)** (*implemented, tested*): dense + BM25, equal-weight Reciprocal Rank
  Fusion. Measured: beats both dense-only and BM25 at 1,000-char chunks (evidence hit@5 0.53 vs
  0.46 and 0.42), and ties BM25 at the default 4,000-char chunks (0.71). See
  [Retrieval Quality](#retrieval-quality)
- **Cross-encoder reranking** (*implemented, not evaluated*): ms-marco-MiniLM-L-6-v2 or Cohere
  Rerank v3
- **Query analyzer** (*implemented, tested*): intent classification → cost routing, entity
  extraction, query rewriting. The effect of routing has not been measured
- **Semantic cache** (*implemented, tested*): a query whose embedding is close enough to a
  cached one (cosine ≥ 0.92) is answered from cache, skipping retrieval and generation. The
  saving has not been measured
- **Knowledge graph** (*implemented, tested*; optional, `ENABLE_KNOWLEDGE_GRAPH=true`):
  LLM-extracted entities/relations (COMPANY, METRIC, DATE; REPORTED_METRIC, FOR_PERIOD, …) and
  graph-augmented retrieval that walks query entities to related metrics/periods and RRF-fuses
  the linked chunks with hybrid results. Measured: evidence hit@5 0.72 vs 0.71, within noise.
  The graph is in memory only ([tutorial](docs/tutorials/graphrag.md))

### Quality assurance
- **Numeric grounding guardrail** (*implemented, tested*): flags numbers in the answer that do
  not appear in the retrieved context. Not run on the golden set
- **Program-of-Thought calculator** (*implemented, tested*): the LLM writes the calculation; a
  restricted arithmetic interpreter (no `exec()`, no attribute access) evaluates it. Not part of
  the answer eval
- **RAGAS evaluation** (*implemented, not evaluated*): faithfulness, answer relevancy, context
  precision + LLM-as-judge. No RAGAS run has been recorded, and the judge needs an OpenAI key
- **Test suite**: unit, integration, property-based (Hypothesis) and API tests. CI runs them on
  every PR, with lint, mypy (on two core modules) and a 70% coverage floor, and blocks on failure

### Operations
- **OpenTelemetry** (*implemented, not evaluated*): trace spans around pipeline stages
- **18 Prometheus metrics** (*implemented, not evaluated*): latency, cost, hallucination score,
  citation coverage, cache hits, tenant token usage. Tests cover only the tenant-quota gauges
- **Multi-window SLO alerting** (*not deployed*): alert rules following the Google SRE workbook
  burn-rate pattern, with PagerDuty/OpsGenie routing. CI does not validate the rules
- **Kubernetes** (*not deployed*): HPA 2–10 replicas, PodDisruptionBudget, NetworkPolicy, and a
  commented-out IRSA annotation. CI lints the Helm chart and schema-validates the manifests
- **Terraform** (*not deployed*): EKS + RDS(pgvector) + ElastiCache + S3 + KMS modules. CI does
  not validate them

---

## Try It Live

**Interactive notebook**: [`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb) walks through the
full pipeline end-to-end — ingestion, hybrid retrieval, vision/chart queries, Program-of-Thought
calculations, guardrails, and cost tracking — using Tesla's real Q3 2023 Investor Update as the
example document.

**Hosted demo**: [Mattral/RAG-Financial-Multimodal](https://huggingface.co/spaces/Mattral/RAG-Financial-Multimodal)
on Hugging Face Spaces (status `RUNNING` when checked on 2026-10-14). Bring your own OpenAI or
Gemini key. The Space defaults to `gemini-2.5-flash`, which returns 404 for newly created
Google API keys; pick a 3.x model or use OpenAI. On the free CPU tier the Space sleeps when
idle, so the first load can take a minute.

Its source is in [`spaces/rag-financial/`](spaces/rag-financial/). To run it locally:

```bash
cd spaces/rag-financial
pip install -r requirements.txt
python app.py
```

Bring your own OpenAI or Google Gemini API key (Gemini has a free tier). The Space mirrors
`src/filing_qa/`'s hybrid retrieval + guardrail logic in a self-contained form with full
pipeline transparency — see exactly how each answer was retrieved and generated.

---

## Repository Structure

```
src/filing_qa/
├── api/          FastAPI app, routers (ingest/query/documents/tenants/feedback)
├── agentic/      LangGraph multi-step reasoning with self-correction loop
├── cli.py        Typer CLI (ingest, query, evaluate, serve, health)
├── components/
│   ├── base.py            ABCs for all pluggable components
│   ├── parser/             Unstructured, Docling, Marker adapters
│   ├── vision/             GPT-4o, Gemini, Qwen2-VL, LocalVLLM + fallback chain
│   ├── embedder/           OpenAI, Voyage, Cohere, local (BAAI/bge)
│   ├── vector_store/       DeepLake, pgvector, Qdrant
│   ├── retriever/          HybridRetriever (dense + BM25 + RRF)
│   ├── reranker/           CrossEncoder, Cohere, NoOp
│   ├── generator/          OpenAI, Gemini, Anthropic, LocalVLLM
│   ├── evaluator/          RAGAS + LLM-as-judge numeric scorer
│   ├── guardrails/         Numeric grounding, PII redaction, injection detection
│   ├── knowledge_graph.py  Real LLM entity/relation extraction + graph traversal
│   ├── colpali_retriever.py  Real MaxSim late-interaction visual retrieval
│   ├── pot_executor.py     Program-of-Thought sandboxed calculator
│   ├── layout_parser.py    Table-caption pairing, semantic chunking
│   ├── query_analyzer.py   Intent classification, entity extraction
│   ├── version_manager.py  Delta detection, point-in-time retrieval
│   └── connectors/         S3, Azure Blob, GCS
├── config.py     Pydantic v2 BaseSettings, 12 nested sub-configs
├── pipeline/     RAGPipeline orchestrator (dependency injection)
├── sdk/          Python SDK (async + sync wrappers)
└── utils/        Telemetry, cost tracker, audit log, semantic cache, drift detector

terraform/        EKS + RDS(pgvector) + ElastiCache + S3 + IAM + KMS (IaC)
k8s/               Base manifests + Kustomize overlays (dev/prod)
helm/              Helm chart (linted in CI, not deployed)
spaces/            Standalone HuggingFace Space demos
└── rag-financial/ Gradio app — OpenAI + Gemini, hybrid retrieval, guardrails
```

---

## Quick Reference

```bash
make setup          # Install deps + copy .env
make dev            # Start full stack with observability
make test           # Run the test suite with coverage
make eval           # Run RAGAS evaluation against golden dataset
make lint           # Ruff lint
make typecheck      # mypy
make docs           # Serve MkDocs site
make query Q="What was Q3 revenue?"
```

---

## Limitations

* **Evaluation is partial.** Dataset integrity, offline retrieval and retrieval-plus-generation
  with one model are measured. The full ingest pipeline (unstructured parsing, reranker,
  guardrails, Program-of-Thought), RAGAS scores, load latency and cost have not been measured
  on a reproducible run yet (see [BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md)).
* **Retrieval misses often.** About 30% of golden questions get no answer-bearing chunk in the
  top 5 at default settings, and multi-row tables are the weakest case when chunks are small.
* **Small, single-author golden set.** 119 questions on fiscal 2023, Tesla-heavy (40 of 119),
  written by one person from the filings themselves. Their wording favors keyword search.
* **Chart questions are text-checkable.** The 9 chart questions use charts whose values also
  appear in tables, so they do not isolate the vision path.
* **Gemini judge not wired.** The LLM-as-judge and RAGAS scorers call OpenAI. With only a Gemini
  key, just the deterministic metrics are available.
* **Calculations are often declined.** Under the default "never estimate" system prompt the
  model frequently refuses to compute derived figures (ratios, sums) unless Program-of-Thought
  handles them.
* **Page citations are unreliable** when chunks lack page metadata. The model invents them.
* **Thinking-token budget.** On Gemini thinking models, reasoning tokens count against the
  output limit. `LLM_CONFIG__THINKING_BUDGET_TOKENS` (default 1024) now reserves them
  separately; with it unset, answers can truncate.
* **Retired model names.** Google no longer serves `gemini-2.5-*` to new API keys. Defaults
  that still name them need a current model such as `gemini-3.8-flash`.

---

## Documentation

| Document | Description |
|---|---|
| [Architecture Overview](docs/architecture/overview.md) | System design and component interactions |
| [Configuration Reference](docs/configuration.md) | All environment variables |
| [Quickstart](docs/quickstart/docker.md) | Up and running in 10 minutes |
| [10-K Analysis Tutorial](docs/tutorials/10k-analysis.md) | End-to-end walkthrough |
| [Anomaly Detection](docs/tutorials/anomaly-detection.md) | Multi-quarter statistical analysis |
| [Performance & Cost Tuning](docs/performance-cost-tuning.md) | Latency and cost optimisation |
| [Troubleshooting](docs/troubleshooting.md) | Common issues + on-call runbook |
| [Security](docs/security.md) | Auth, PII, audit, compliance |
| [ADR Index](docs/architecture/adr-index.md) | Architecture decisions |
| [BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md) | Quality, latency, cost numbers |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guide |

---

## License

MIT — see [LICENSE](LICENSE). Built with care by [@Mattral](https://github.com/Mattral).
