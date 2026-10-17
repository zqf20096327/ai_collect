# chao-rag-wiki

A RAG (retrieval-augmented generation) skill for Claude Code. It builds a
semantic vector index over your local `raw/` document corpus and answers
questions by retrieving the most relevant chunks.

- **Embeddings:** any OpenAI-compatible `/embeddings` endpoint, set via
  `RAG_EMBED_*` env vars (default: Qianfan `bge-large-zh`, 1024-d). OpenAI,
  Voyage, OneAPI/OpenRouter, local vLLM all work.
- **Retrieval:** hybrid — dense vector search
  ([turbovec](https://github.com/RyanCodrai/turbovec) `TurboQuantIndex`) fused
  with lexical **BM25** via Reciprocal Rank Fusion (CJK-aware, dependency-free),
  plus an optional **LLM rerank** stage (`--rerank`) for higher precision
- **Inspired by:** `karpathy-llm-wiki`, but retrieval-first — `raw/` is never
  modified and there is no manual article-compilation step.

## Install

```bash
npx skills add smallnest/chao-rag-wiki
```

## Requirements

- An embedding API key — `QIANFAN_API_KEY` for the default Qianfan provider,
  or `RAG_EMBED_API_KEY` for any other (see *Embedding provider* below)
- Python 3 (a self-contained venv is created under `.venv/`)

## Embedding provider

Provider-agnostic via env vars (no keys are hard-coded or stored in the index):

| Env var | Default | Meaning |
|---------|---------|---------|
| `RAG_EMBED_BASE_URL` | `https://qianfan.baidubce.com/v2` | API base (no `/embeddings`) |
| `RAG_EMBED_API_KEY`  | falls back to `QIANFAN_API_KEY`, then `OPENAI_API_KEY` | Bearer key |
| `RAG_EMBED_MODEL`    | `bge-large-zh` | model name |
| `RAG_EMBED_DIM`      | `1024` | vector dimension |

OpenAI: `RAG_EMBED_BASE_URL=https://api.openai.com/v1 RAG_EMBED_MODEL=text-embedding-3-small RAG_EMBED_DIM=1536`.
Voyage (Anthropic's recommended embeddings — Claude has no embedding API):
`RAG_EMBED_BASE_URL=https://api.voyageai.com/v1 RAG_EMBED_MODEL=voyage-3`.
Changing provider/model/dim requires a full rebuild.

## Quick start

```bash
SK=~/.claude/skills/chao-rag-wiki

# one-time venv (skip if .venv exists)
python3 -m venv $SK/.venv && $SK/.venv/bin/pip install -q turbovec numpy requests

# first-run preflight: checks deps, the embedding key, and the live endpoint
$SK/.venv/bin/python $SK/scripts/setup_check.py
#   if it complains the key is missing (default Qianfan provider):
#     export QIANFAN_API_KEY="bce-v3/..."   # from https://console.bce.baidu.com/qianfan/
#   or use another provider, e.g. OpenAI:
#     export RAG_EMBED_BASE_URL=https://api.openai.com/v1 RAG_EMBED_API_KEY=$OPENAI_API_KEY
#     export RAG_EMBED_MODEL=text-embedding-3-small RAG_EMBED_DIM=1536

# build the index over ./raw
$SK/.venv/bin/python $SK/scripts/build_rag.py --raw raw --out .rag

# ask a question (hybrid dense+BM25 by default)
$SK/.venv/bin/python $SK/scripts/query_rag.py --out .rag --query "SPEC 和 PRD 的区别" -k 8

# add a second-stage LLM rerank for higher precision (one chat call, ~10s)
$SK/.venv/bin/python $SK/scripts/query_rag.py --out .rag --query "SPEC 和 PRD 的区别" -k 8 --rerank

# force a single retriever when you want it
$SK/.venv/bin/python $SK/scripts/query_rag.py --out .rag --query "rotate_writer.go" --mode bm25
$SK/.venv/bin/python $SK/scripts/query_rag.py --out .rag --query "如何让 agent 自我迭代" --mode dense
```

Re-index after edits with `--update` (continuous indexing — only re-embeds
new/changed files, drops deleted ones):

```bash
$SK/.venv/bin/python $SK/scripts/build_rag.py --raw raw --out .rag --update
```

Preview pending changes without embedding anything:

```bash
$SK/.venv/bin/python $SK/scripts/build_rag.py --raw raw --out .rag --check
```

Since `raw/` grows daily, run `--update` on a schedule (cron/launchd) or a git
hook — a no-op run exits in seconds and makes no embedding calls.

## How it works

1. `build_rag.py` walks `raw/`, splits each markdown file on headings into
   ~1200-char chunks, embeds them via `embed.py`, and writes:
   - `.rag/index.tv` — the turbovec quantized index
   - `.rag/meta.json` — per-row metadata (path, title, heading, text)
   - `.rag/vectors.npy` — raw embeddings, reused by `--update`
   - `.rag/manifest.json` — build config + per-file content hashes
2. `query_rag.py` embeds the query, runs `TurboQuantIndex.search`, and maps the
   returned row ids back to chunks. turbovec preserves insertion order, so row
   ids line up 1:1 with `meta.json`.
3. The agent reads the retrieved chunks (use `--json`) and synthesizes a cited
   answer.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition + workflow the agent follows |
| `scripts/embed.py` | Batched, retrying Qianfan embedding client |
| `scripts/build_rag.py` | Chunk → embed → build turbovec index |
| `scripts/query_rag.py` | Embed query → search → render results |

## Config (env vars)

| Var | Default | Notes |
|-----|---------|-------|
| `QIANFAN_API_KEY` | — | required |
| `RAG_EMBED_MODEL` | `bge-large-zh` | rebuild if changed |
| `RAG_EMBED_DIM` | `1024` | must match model |
| `RAG_EMBED_BATCH` | `16` | inputs per embedding request |
