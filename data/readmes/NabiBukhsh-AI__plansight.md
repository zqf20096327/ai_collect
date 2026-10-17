# Plansight

Construction document intelligence. Ingest architectural drawing sets, RFIs, and
specifications, then get back **validated building quantities**, **cited
answers**, and a **grounded scope of work**.

---

## What it does

Point it at a permit set or an RFI package and it will:

| Capability | Output |
| --- | --- |
| **Structured extraction** | Site area, floors, units, per-unit areas — validated, unit-aware, with page-level provenance |
| **Document Q&A** | Answers with `[n]` citations back to a specific sheet and page |
| **Scope of work** | Trade-categorised, prioritised work items, each traceable to the passage that justified it |

## Why the architecture looks like this

Three decisions drive the whole design.

### 1. A drawing set is not one kind of document

A permit set interleaves prose (specifications, RFI narratives, cover sheets)
with CAD sheets whose text layer is a scattering of dimension callouts. Reading
every page through a PDF text extractor produces a corpus that is *empty exactly
where the building data lives*.

Ingestion routes **per page**. Prose goes through the text layer — instant and
free. Drawing sheets are rasterised and read by a vision model with a prompt
that asks for the title block, unit tags, schedules, and annotations
specifically. Dense sheets that carry both get both.

```
                    ┌─ text layer ────────────┐
PDF ─→ per-page ────┼─ vision transcription ──┼──→ chunks (page + sheet tagged)
       routing      └─ hybrid (both) ─────────┘
```

### 2. "How many units?" is an extraction problem, not a retrieval one

Asking an LLM to re-read unit counts off retrieved drawing text on every query
is slow, expensive, and non-deterministic — the same question returns different
numbers twice in a row.

So quantities are extracted **once, at ingest**, under a constrained schema, and
persisted as a validated `BuildingSpec`. A query router then sends each question
to the track that suits it:

```
                       ┌─→ STRUCTURED ─→ validated BuildingSpec (deterministic, free)
question ─→ router ────┼─→ HYBRID ─────→ both
                       └─→ SEMANTIC ───→ dense + BM25 retrieval ─→ cited answer
```

Routing is a keyword-and-shape heuristic first (free, covers most traffic), with
an LLM classifier only for genuinely ambiguous questions.

### 3. Construction queries are full of exact tokens

Sheet numbers (`A-201`), unit tags (`2B`), room names, code references. Embedding
models are weak at rare alphanumerics. Retrieval fuses a dense arm and a BM25
lexical arm with weighted reciprocal-rank fusion, so `"what is on sheet A-201"`
matches lexically while `"fire-rated corridor assembly"` matches semantically.

---

## Quick start

```bash
python -m venv .venv && .venv/Scripts/activate    # Windows
# python -m venv .venv && source .venv/bin/activate  # macOS / Linux

pip install -e ".[dev]"
cp .env.example .env        # then set PLANSIGHT_OPENAI__API_KEY
```

### CLI

```bash
plansight create-project "17 Julian Place"
plansight ingest prj_xxx  drawings/*.pdf
plansight spec   prj_xxx
plansight ask    prj_xxx "How many units are on level 2 and what is their total area?"
plansight scope  prj_xxx --focus "outstanding RFI responses"
```

### API

```bash
plansight serve --reload         # http://localhost:8000/docs
```

```bash
# Create a project
curl -X POST localhost:8000/v1/projects \
  -H 'Content-Type: application/json' \
  -d '{"name":"17 Julian Place"}'

# Upload — returns 202 with a job id
curl -X POST localhost:8000/v1/projects/prj_xxx/documents \
  -F 'file=@drawings/architectural-rfi-4.pdf'

# Poll progress
curl localhost:8000/v1/jobs/job_xxx

# Ask
curl -X POST localhost:8000/v1/projects/prj_xxx/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"What is the site area?"}'
```

### Docker

```bash
docker compose up --build
```

---

## API surface

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health`, `/ready` | Liveness and readiness probes |
| `POST` | `/v1/projects` | Create a project |
| `GET` | `/v1/projects` | List projects |
| `GET` | `/v1/projects/{id}` | Project detail |
| `DELETE` | `/v1/projects/{id}` | Delete a project and its index |
| `POST` | `/v1/projects/{id}/documents` | Upload a PDF → `202` + job id |
| `GET` | `/v1/projects/{id}/documents` | List documents |
| `DELETE` | `/v1/projects/{id}/documents/{doc}` | Remove a document and its chunks |
| `POST` | `/v1/projects/{id}/ask` | Ask a question, get a cited answer |
| `GET` | `/v1/projects/{id}/spec` | Extracted building quantities |
| `POST` | `/v1/projects/{id}/scope` | Generate a scope of work |
| `GET` | `/v1/jobs/{id}` | Poll an ingestion job |

Errors always use one envelope, with the correct HTTP status:

```json
{
  "error": { "code": "document_too_large", "message": "..." },
  "request_id": "a1b2c3d4e5f60718"
}
```

---

## Layout

```
src/plansight/
├── config.py              typed settings, env-driven
├── errors.py              exception hierarchy carrying HTTP status + code
├── logging_setup.py       structlog with request-scoped correlation ids
├── service.py             application service — shared by API and CLI
├── cli.py                 typer CLI
├── domain/
│   ├── building.py        BuildingSpec, Floor, Unit, Quantity, Evidence
│   └── models.py          Project, Document, Page, Chunk, Job
├── providers/
│   ├── base.py            LLM / Embedding / Vision protocols
│   ├── openai_provider.py OpenAI adapter, structured outputs, batching
│   └── fake.py            deterministic doubles — the suite needs no API key
├── ingestion/
│   ├── pdf.py             PyMuPDF text layer + capped-resolution rendering
│   ├── router.py          per-page text-vs-vision decision
│   ├── vision.py          drawing-sheet transcription prompts
│   ├── chunking.py        structure-aware, page-scoped splitting
│   └── pipeline.py        concurrent orchestration
├── extraction/
│   ├── schema.py          constrained-decoding DTOs
│   ├── extractor.py       per-page extraction
│   └── merge.py           cross-page reconciliation with corroboration scoring
├── retrieval/
│   ├── store.py           NumPy (default) and FAISS vector stores
│   ├── lexical.py         Okapi BM25
│   └── hybrid.py          RRF fusion + citable context building
├── qa/
│   ├── router.py          structured / semantic / hybrid routing
│   ├── prompts.py         answering prompts
│   └── engine.py          cited answer generation
├── scoping/generator.py   grounded scope-of-work items
├── storage/
│   ├── repository.py      async SQLite persistence
│   └── index_registry.py  per-project index cache + write locks
└── api/                   FastAPI app, routes, DTOs, middleware
```

---

## Development

```bash
pytest              # full suite, no API key required
ruff check src tests
ruff format src tests
mypy
```

The provider protocols in `providers/base.py` are the seam: `providers/fake.py`
supplies deterministic doubles, so the entire pipeline — ingestion, extraction,
retrieval, routing, scoping, and the HTTP layer — runs offline in tests.

## Configuration

Every setting is environment-driven under the `PLANSIGHT_` prefix, with `__` as
the section delimiter. See [.env.example](.env.example).

| Variable | Default | Notes |
| --- | --- | --- |
| `PLANSIGHT_OPENAI__API_KEY` | — | Required |
| `PLANSIGHT_OPENAI__EMBEDDING_DIMENSIONS` | `1024` | Matryoshka truncation of `text-embedding-3-large` |
| `PLANSIGHT_INGESTION__TEXT_LAYER_MIN_CHARS` | `280` | Below this, a page routes to vision |
| `PLANSIGHT_INGESTION__MAX_CONCURRENT_PAGES` | `6` | Bounds vision concurrency |
| `PLANSIGHT_RETRIEVAL__DENSE_WEIGHT` | `0.6` | Dense vs lexical weight in RRF |
| `PLANSIGHT_STORAGE__VECTOR_BACKEND` | `numpy` | `numpy` or `faiss` |
| `PLANSIGHT_API__AUTH_TOKENS` | — | Comma-separated bearer tokens; empty disables auth |

### Scaling notes

- **Vector backend.** Exact NumPy cosine search is faster than an approximate
  index at project scale (thousands of chunks) with no recall loss. Set
  `VECTOR_BACKEND=faiss` and install the `faiss` extra when a project outgrows
  it; the store interface is unchanged.
- **Job execution.** `JobRunner` in `service.py` is deliberately a narrow
  interface. Moving ingestion to Celery, ARQ, or a cloud queue means replacing
  that one class.
- **Persistence.** `Repository` is the only module that touches SQL. The schema
  is standard enough to move to Postgres — at which point `pgvector` can back
  the vector store behind the same protocol.

## Licence

MIT.
