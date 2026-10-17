# Knowledge Graph Fusion

Part 2 of the persistent knowledge layer: from routing to fusion.

The second iteration of the [persistent knowledge layer](https://github.com/mcekikj/persistent-knowledge-layer): the query router is retired in favor of an **always-fused retrieval pipeline** - every query runs hybrid search AND bounded typed graph traversal, the union is reranked once with relationship paths visible, and the grounded bundle carries the paths as evidence. Relationships live in a real graph engine with **bitemporal edges** (validity windows plus ingest time), contradictions are **detected at ingest** instead of curated, and entity resolution is a first-class two-threshold pipeline with embedding blocking and gray-zone LLM adjudication.

Part 1's repository stays frozen as the artifact its article describes; this repository carries the evolution. The corpus, the contradiction gate, the effective-date scoping and the no-keys identity model all carry over unchanged.

**What Part 2 adds**

| Capability | Where |
|---|---|
| Always-fused retrieval (no modes, no router) | `app/services/pipeline.py` |
| Graph engine: bounded typed traversal, Gremlin + in-memory | `app/services/graphstore.py` |
| The ontology (Part 1's curated vocabulary, frozen as the edge-type schema) | `app/services/ontology.py` |
| Two-threshold entity resolution with gray-zone adjudication | `app/services/resolution.py` |
| Union reranker (external - the built-in ranker cannot rerank a hand-assembled union) | `app/services/rerank.py` |
| Bitemporal edges + timeline/diff query modes | `graphstore.py` + `pipeline.py` |
| Ingest-time contradiction detection (auto-supersede vs surface) | `pipeline.py` |
| Cosmos DB for Apache Gremlin + projection Function App infra | `infra/main.bicep` |

Measured on the live deployment: resolution fragmentation reduced from 149 to 120 concepts like-for-like against Part 1's alias-only resolver; contradiction detection fired unprompted during the corpus seed; fused retrieval adds an average of 10 typed relationship paths per grounded bundle. Full detail in [VALIDATION.md](VALIDATION.md).

**What Part 3 adds (additive - the Part 2 fused pipeline is unchanged)**

Part 3 puts a bounded agent over the same knowledge layer: the fixed pipeline is retired as the *only* option, not replaced. Every Part 2 module is untouched; the agent is new files plus one new endpoint, so `/query` and everything the Part 2 article describes behave exactly as before.

| Capability | Where |
|---|---|
| Eight read-only tools exposing the layer's semantics (MCP-shaped) | `app/services/tools.py` |
| Bounded agent loop (hard tool-round/token/time caps, full trace) | `app/services/agent.py` |
| Composer: grounding check + contradiction gate as post-loop policy | `app/services/composer.py` |
| Model-family adaptation (gpt-4 / gpt-5 families) | `app/services/model_compat.py` |
| `POST /agent/query` (toolset, policy_on) next to the unchanged `/query` | `app/main.py` |
| 15-question golden set + live experiment + benchmark runners | `demo_data/golden_set_v2.json`, `scripts/` |

Measured live on Azure across four models (gpt-4o-mini, gpt-4.1, gpt-5-mini, gpt-5): the agent wins the multi-hop subset and loses the single-hop subset to the fixed pipeline (so it is an escalation lane, not a default); tool-seeking and token cost rise with model capability while answer quality peaks at gpt-5-mini; and on the contested questions every configuration - fixed pipeline, search-box agent, and full agent with the gate on or off - disclosed the contradiction rather than choosing a side. The one governance miss was the fixed pipeline returning an empty answer on a customer-phrased contested question, which the agent's explicit contradiction lookup handled. Reproduce with `python scripts/run_experiments.py` (APP_MODE=azure) and `python scripts/summarize.py`.

A RAG evidence layer grounds answers in source documents. A **knowledge layer** beside it accumulates what the system has already worked out - concepts, typed relationships, scoped decisions, comparisons, and (the interesting one) **contradictions it refuses to resolve on its own authority**.

> Everything in `demo_data/` is synthetic. Ostermere Mutual, its policies, claims, wind zones, regulator and staff are all invented for this demonstration. Nothing here is insurance, legal, underwriting or claims advice.

---

## What makes this more than another RAG demo

The synthetic corpus is engineered so that a pure retrieval system fails - **fluently**, with an answer that reads perfectly well. Six traps are live in the data:

| Trap | What plain RAG does | What this does |
|---|---|---|
| **Scoped supersession** | Retrieves "15 years", reports it as the general rule | Decision carries `scope: "New business only. Zone H3 only."` |
| **Genuine contradiction** | Retrieves one of two conflicting *current* documents and picks a side | Raises `con-001`, returns **both** statements, names the owner, **gives no answer** |
| **Terminology drift** | Creates four concept pages for one concept | Entity resolution: `cash settlement basis` → `actual-cash-value` |
| **Effective-date scoping** | Applies a rule that took effect *after* the date of loss | `as_of` selects the documentation in force on that date |
| **Rationale loss** | Never surfaces the email explaining *why* the threshold is 15 | `rationale` + `rationale_source` on the decision |
| **Multi-hop** | Ranks chunks; cannot traverse | 28 typed relationships |

The load-bearing demo is the contradiction. Two **current** documents disagree about whether trace-and-access is standard cover or a paid endorsement. Neither supersedes the other. The system detects the conflict and **refuses to settle it** - because recency is not applicability.

---

## Run it locally - no Azure account needed

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://localhost:8000/docs>.

### See the contradiction

```bash
curl -s -X POST http://localhost:8000/query \
  -H 'Content-Type: application/json' \
  -d '{"question": "Is trace and access covered under Hearthmere?", "mode": "wiki"}' \
  | jq '.warnings, .contradictions[0].statements'
```

### See temporal scoping

Claim CLM-1108 has a date of loss of **2026-02-20**. The H3 rule took effect **2026-03-01**, so it cannot apply:

```bash
curl -s -X POST http://localhost:8000/query \
  -H 'Content-Type: application/json' \
  -d '{"question": "What roof inspection threshold applied?", "mode": "evidence", "as_of": "2026-02-20"}' \
  | jq '.evidence[].source_id'
# INS-SYN-004 is absent - it was not yet in force
```

And in reverse - a superseded document still governs an older loss:

```bash
curl -s -X POST http://localhost:8000/query \
  -H 'Content-Type: application/json' \
  -d '{"question": "Is depreciation recoverable?", "mode": "evidence", "as_of": "2025-08-01"}' \
  | jq '.evidence[] | {source_id, in_force_at_as_of}'
# INS-SYN-009 (superseded today) comes back marked in_force_at_as_of: true
```

### The contradiction register

```bash
curl -s http://localhost:8000/wiki/contradictions | jq '{count, unresolved}'
```

---

## API reference

| Method & path | Purpose |
|---|---|
| `GET /health` | Mode and workspace check. |
| `GET /wiki` | List all wiki objects; filter with `?item_type=` (`source`, `concept`, `relationship`, `comparison`, `decision`, `contradiction`, `open_question`, `process`). |
| `GET /wiki/contradictions` | The contradiction register, with counts; filter with `?status=` (`unresolved`, `monitoring`). |
| `GET /wiki/{item_id}` | Fetch one wiki object by id. |
| `POST /query` | `{ question, mode, top_k, as_of }`. `mode`: `auto` \| `wiki` \| `evidence` \| `hybrid`. `as_of` (YYYY-MM-DD) is the date the question is *about* - e.g. a date of loss - and selects the documentation in force on that date. |
| `POST /agent/query` | **(Part 3)** The bounded agent over the typed tool surface: `{ question, as_of, toolset, policy_on }`. `toolset`: `full` (eight tools) \| `search_only` (the control arm). `policy_on` toggles the composer's contradiction gate. Returns the answer plus the full `trace`, `grounding`, `gate` and `bounds`. The fixed `/query` pipeline is unchanged. |
| `POST /ingest/text` | Ingest a document from JSON: `{ document_id, title, text, effective_date }`. |
| `POST /ingest/file` | Ingest an uploaded UTF-8 `.txt`/`.md` file (multipart form: `document_id`, `title`, `effective_date`, `file`). |
| `POST /cost-estimate` | Run the token-volume amortization model with your own assumptions. |
| `POST /export/obsidian` | Regenerate the Obsidian vault from the wiki store into `runtime_obsidian_export/`. |
| `POST /export/obsidian.zip` | Same, returned as a downloadable zip. |

Two behaviours worth knowing in demo mode: uploaded documents land in `demo_data/uploads/` (the local stand-in for the Blob Storage raw-sources container - the curated corpus in `demo_data/raw/` is never written to), and ingested wiki objects live in memory only. `demo_data/demo_state.json` is not modified, so a restart always returns the demo to its known-good state.

---

## Project structure

```text
app/
  main.py           FastAPI surface
  models.py         Request/response schemas
  config.py         Environment-driven settings
  services/
    pipeline.py     Routing, temporal scoping, the contradiction gate
    repository.py   Wiki store (local JSON | Cosmos DB)
    retrieval.py    Evidence store (local | Azure AI Search)
    llm.py          Model client (deterministic demo | Foundry)
    obsidian_exporter.py   Regenerates the whole vault from the store
    storage.py      Source store (local | Blob Storage)
infra/main.bicep    Full Azure deployment, managed identity, no keys
demo_data/
  raw/              21 synthetic source documents
  demo_state.json   The compiled wiki: 19 concepts, 28 relationships,
                    5 decisions, 4 comparisons, 2 contradictions,
                    4 open questions, 2 processes
  obsidian_vault/   55 generated pages - open this in Obsidian
cost_model/         Token-volume amortization model
tests/              13 tests, including the contradiction and temporal gates
```

## The Obsidian vault

```bash
open demo_data/obsidian_vault   # then: Obsidian → Open folder as vault
```

Every page is **generated** from `demo_state.json` - nothing is hand-written. Turn on graph view and look for the red cluster: that is `con-001` and everything it blocks.

Regenerate at any time:

```bash
curl -X POST http://localhost:8000/export/obsidian
```

## Tests

```bash
pytest -q     # 13 passed
```

The two I would keep if I had to delete the rest:

- `test_asking_about_trace_and_access_surfaces_the_conflict_instead_of_answering`
- `test_as_of_excludes_a_rule_that_had_not_taken_effect_yet`

---

## Azure mode

```bash
az group create -n rg-wikirag-demo -l swedencentral
az deployment group create -g rg-wikirag-demo -f infra/main.bicep -p namePrefix=wikirag
```

The Bicep provisions Blob Storage (versioning + soft delete), Azure AI Search (vector + semantic, local auth disabled), Cosmos DB for NoSQL (serverless, `/workspace_id` partition key), Microsoft Foundry with chat and embedding deployments, Key Vault, Log Analytics, Application Insights and the Container App - wired together with a **user-assigned managed identity and no keys anywhere**.

Then:

```bash
cp .env.example .env        # populate from the deployment outputs
export APP_MODE=azure
python -m app.create_search_index
python -m app.seed_azure
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for the full checklist and the RBAC breakdown.

## Cost model

```bash
python cost_model/cost_model.py
```

Token volumes, not prices. Replace the assumptions with telemetry from your own corpus and query mix, then apply current Azure pricing separately.

## License

MIT - see [LICENSE](LICENSE). This covers the code, the infrastructure templates, and the synthetic dataset (all documents in `demo_data/` were written by the author for this demonstration; none is derived from real insurer material).
