# 𝐓𝐞𝐜𝐡𝐑𝐀𝐆 𝐚 ROE - RAGraph Ontological Engine

A hybrid, ontology-driven retrieval engine for technical documentation.
Rather than fetching only semantically similar chunks like classic RAG, ROE
builds a structured knowledge representation at ingestion time and delivers
precise, traceable context to the LLM at query time:

- **Vector embeddings** via LanceDB (bge-m3, OpenAI-compatible endpoint)
- **Domain ontology** + **knowledge graph** following the SQLGraph approach (SQLAlchemy)
- **Atomic facts** with source back-reference
- **Response audit metadata** (evidence coverage, reasoning score, recovery)

## Architecture

```
roe/
├── config.py          # ROESettings (OpenAI-compatible endpoints, storage paths)
├── clients.py         # LLMClient + EmbeddingClient (openai.OpenAI)
├── vector_store.py    # LanceDB vector store (cosine, L2-normalized)
├── knowledge_store.py # SQLGraph-based knowledge graph (SQLAlchemy)
├── ontology.py        # Ontology bootstrap + graph extraction via LLM
├── ingestion.py       # Parsing (PDF/MD/TXT) + chunking + embedding + graph
├── retrieval.py       # Adaptive vector search + graph context + answer assembly
├── pipeline.py        # ROEPipeline facade
└── cli.py             # roe ingest|query|ask|stats
```

## Setup

```bash
uv sync
cp .env.example .env   # or use an existing .env
```

`.env` (local test with Ollama):

```
ROE_LLM_BASE_URL=http://localhost:11434/v1
ROE_LLM_API_KEY=ohne
ROE_LLM_MODEL=qwen2.5:7b

ROE_EMBED_BASE_URL=http://localhost:11434/v1
ROE_EMBED_API_KEY=ohne
ROE_EMBED_MODEL=bge-m3:latest

ROE_DATA_DIR=./roe_data
```

All endpoints are addressed **OpenAI-compatibly** (Ollama `/v1`, OpenAI, vLLM,
...). No local transformer models are loaded in the code; embeddings are
always requested through the OpenAI-compatible `/v1/embeddings` endpoint.

## Usage

```bash
# Ingest a file (PDF / Markdown / plain text)
uv run roe ingest doc.pdf
uv run roe ingest manual.md

# Ask a question (answer + audit)
uv run roe query "Which maintenance steps require safety goggles?"

# Answer only
uv run roe ask "Which component triggers alarm A1?"

# Statistics
uv run roe stats
```

## Pipeline

### Ingestion
1. Parsing (pypdf / UTF-8 text)
2. Chunking (~1000 chars, 200 overlap)
3. Embedding via OpenAI-compatible endpoint -> LanceDB
4. Originals + chunks -> SQLAlchemy (KnowledgeStore)
5. Ontology bootstrap over a distributed sample of chunks
6. Per-chunk graph extraction: atomic facts as triples with source back-reference

### Retrieval
- Vector search (max. 4 chunks)
- Adaptive query expansion when top similarity < 0.45 (rewrite + second pass up to 8 chunks)
- Graph context: <=10 facts, <=24 nodes, <=18 edges, <=12 paths
- Seeds derived from chunk texts via fact-entity matching

### Answer
- Three prompt blocks (chunks / facts / paths)
- Instruction: "answer only from the supplied evidence"
- Claims classified as Verified / Contradicted / Unsupported
- Metrics: evidence coverage + reasoning score
- Recovery cycle when coverage < 40%

## Technology stack

| Component | Choice |
|---|---|
| Embeddings | bge-m3 (Ollama, OpenAI-compatible) |
| Reasoning LLM | qwen2.5:7b (Ollama, OpenAI-compatible) |
| Vector database | LanceDB |
| Knowledge graph / knowledge store | SQLGraph (SQLAlchemy) - https://github.com/FBR65/SQLGraph |
| Supported formats | PDF / Markdown / plain text |

## Configuration (`ROESettings` excerpt)

| Field | Env var | Default |
|---|---|---|
| `llm_base_url` | `ROE_LLM_BASE_URL` | `http://localhost:11434/v1` |
| `llm_model` | `ROE_LLM_MODEL` | `qwen2.5:7b` |
| `embed_model` | `ROE_EMBED_MODEL` | `bge-m3:latest` |
| `chunk_size` | - | 1000 |
| `chunk_overlap` | - | 200 |
| `max_chunks` | - | 4 |
| `expand_threshold` | - | 0.45 |
| `max_facts` / `max_nodes` / `max_edges` / `max_paths` | - | 10 / 24 / 18 / 12 |
| `min_coverage` | - | 0.40 |

## Verification (smoke test)

```bash
# Markdown sample
uv run roe ingest sample.md          # -> 1 chunk, 13 entities, 9 facts
uv run roe query "What triggers alarm A1?"
# Audit: evidence_coverage=1.0, n_chunks=1, n_facts=10, n_nodes=15, n_edges=11

# Bundled PDF
uv run roe ingest ROE_*.pdf          # -> 50 chunks, 263 entities, 213 facts
uv run roe query "What is the purpose of ROE?"
# Audit: evidence_coverage=0.6, n_chunks=4, n_facts=10, n_nodes=24, n_edges=17
```

## Licence
MIT


## Note of Thanks

Inspiration to this System is the Articel:

RAGraph Ontological Engine (ROE): Building a Hybrid Ontology-Driven Retrieval Engine for Technical Manuals - Andrea Belvedere

