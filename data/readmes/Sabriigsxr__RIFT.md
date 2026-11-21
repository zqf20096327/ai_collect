# RIFT

<div align="center">

![RIFT — Local Offensive Security Knowledge Engine](assets/visuals/rift-hero.svg)

**MCP-powered retrieval for authorized offensive-security intelligence.**

[![CI](https://github.com/Sabriigsxr/RIFT/actions/workflows/ci.yml/badge.svg)](https://github.com/Sabriigsxr/RIFT/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-8cff66)
![Local-first](https://img.shields.io/badge/query--time-local-62dcff)

</div>

> **Authorized use only.** RIFT retrieves knowledge; it does not execute
> commands or autonomously exploit systems. Read
> [`docs/ETHICAL_USE.md`](docs/ETHICAL_USE.md) and [`WARNING.txt`](WARNING.txt).

## What RIFT does

RIFT turns a local offensive-security Q&A knowledge base into an inspectable
MCP tool. Ask a question, retrieve semantically related entries, and review
the stored `doc_id`, score, metadata, question, and answer.

![RIFT product overview](assets/visuals/rift-product-overview.svg)

**Implemented:** semantic search with Sentence Transformers + FAISS,
extractive answers, index statistics, an MCP prompt, stdio transport, and
optional streamable HTTP on localhost. **Not implemented:** shell tools,
command execution, autonomous exploitation, or generated attack plans.

## How it works

![RIFT architecture](assets/visuals/rift-architecture-overview.svg)

![RIFT data flow](assets/visuals/rift-data-flow.svg)

The bundled index contains 23,737 aligned entries. Query-time retrieval uses
the local model and `IndexFlatIP`; after the model is cached, no network is
required for search.

## Quick start

![Getting started](assets/visuals/rift-getting-started.svg)

```bash
git clone https://github.com/Sabriigsxr/RIFT.git
cd RIFT
python3 -m venv .venv
.venv/bin/pip install -e .
bash scripts/restore_index.sh
.venv/bin/rift --version
```

Then connect an MCP client using the examples in [`examples/`](examples/) and
ask it to search for authorized detection, DFIR, or research guidance.

## See a real result

The repository includes verified text transcripts in
[`docs/demo/`](docs/demo/). Terminal screenshots are intentionally not
replaced with mockups: capture them on a workstation using
[`assets/screenshots/CAPTURE_CHECKLIST.md`](assets/screenshots/CAPTURE_CHECKLIST.md).

![Illustrative search result layout](assets/visuals/rift-search-example.svg)

The graphic above is an **illustration of the result shape**, not a runtime
screenshot. For actual values, use [`docs/demo/SEARCH_EXAMPLE.md`](docs/demo/SEARCH_EXAMPLE.md).

## MCP integration

![MCP workflow](assets/visuals/rift-mcp-workflow.svg)

RIFT exposes:

| Capability | Purpose |
|---|---|
| `search_offensive_scenarios` | JSON semantic search with scores and metadata |
| `ask_offensive_scenario` | Readable extractive rendering of search results |
| `index_stats` | Local index, model, and alignment statistics |
| `offensive_scenario_brief` | Grounded briefing prompt template |

Full contracts and client configuration live in
[`docs/MCP_INTEGRATION.md`](docs/MCP_INTEGRATION.md).

## Learn visually

| Level | Start here |
|---|---|
| Beginner | [`docs/visual-guide/WHAT_IS_RIFT.md`](docs/visual-guide/WHAT_IS_RIFT.md) · [`FIRST_SEARCH_TUTORIAL.md`](docs/visual-guide/FIRST_SEARCH_TUTORIAL.md) |
| Intermediate | [`MCP_EXPLAINED.md`](docs/visual-guide/MCP_EXPLAINED.md) · [`HOW_RIFT_WORKS.md`](docs/visual-guide/HOW_RIFT_WORKS.md) |
| Advanced | [`LOCAL_FIRST_ARCHITECTURE.md`](docs/visual-guide/LOCAL_FIRST_ARCHITECTURE.md) · [`SEMANTIC_SEARCH.md`](docs/visual-guide/SEMANTIC_SEARCH.md) |

See the complete [visual learning path](docs/visual-guide/LEARNING_PATH.md) or
the [short product presentation](docs/presentation/RIFT_PRODUCT_OVERVIEW.md).

## Local-first and security boundaries

![Local-first architecture](assets/visuals/rift-local-first.svg)

RIFT reads the local model, FAISS index, and aligned JSONL records. The
optional HTTP transport has no built-in authentication; keep it on loopback or
behind an access-controlled boundary with TLS. Review all retrieved material
before acting.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), preserve the bundled data and index,
and keep RIFT retrieval-only. See [`docs/SECURITY.md`](docs/SECURITY.md) for
the security posture and [`docs/ROADMAP.md`](docs/ROADMAP.md) for future work.

**Made in Egypt by Ahmed Sabry ([Sabriigsxr](https://github.com/Sabriigsxr)).**
