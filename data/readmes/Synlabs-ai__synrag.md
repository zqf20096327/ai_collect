<div align="center">

# synrag

**CPU-native search and context for AI agents.**<br>
Hybrid retrieval · multilingual embeddings · document parsing · compact, cited LLM context — in one 3 MB binary. No GPU.

[![Website](https://img.shields.io/badge/site-ai.synlabs.pro-5eead4?style=flat-square)](https://ai.synlabs.pro)
[![Release](https://img.shields.io/github/v/release/Synlabs-ai/synrag?style=flat-square&color=a78bfa)](https://github.com/Synlabs-ai/synrag/releases)
[![Install test](https://img.shields.io/github/actions/workflow/status/Synlabs-ai/synrag/smoke.yml?style=flat-square&label=install%20test)](https://github.com/Synlabs-ai/synrag/actions/workflows/smoke.yml)
![Platform](https://img.shields.io/badge/platform-linux%20x86--64-30363d?style=flat-square)
![GPU](https://img.shields.io/badge/GPU-not%20needed-30363d?style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/synrag?style=flat-square&label=pypi&color=30363d)](https://pypi.org/project/synrag/)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.github.Synlabs--ai%2Fsynrag-30363d?style=flat-square)](https://registry.modelcontextprotocol.io/v0/servers?search=synrag)
![Telemetry](https://img.shields.io/badge/telemetry-none-30363d?style=flat-square)

[Website](https://ai.synlabs.pro) · [Docs](https://ai.synlabs.pro/docs/) · [Benchmarks](BENCHMARKS.md) · [Pricing](https://ai.synlabs.pro/pricing/) · [Download](https://github.com/Synlabs-ai/synrag/releases/latest)

</div>

---

```bash
curl -fsSL https://ai.synlabs.pro/install.sh | sh
```

```console
$ synrag index ./company-docs -o kb.syn --student ~/.synrag/models/synapse.synm
$ synrag serve kb.syn --student ~/.synrag/models/synapse.synm &
$ curl -s 'localhost:7878/context?q=what+is+our+refund+window&budget=300'
{
  "context": "Customers can return any item within 30 days for a full refund [1]. ...",
  "sources": [{"cite": 1, "source": "policies/refunds.pdf", "title": "Refund policy", "page": 2, ...}],
  "tokens": 61
}
```

Most RAG stacks glue together a parser, an embedding API or GPU, a vector database, a keyword index and a prompt
packer. **synrag is all of that in one process** you run next to your app — with its own embedding model
(Synapse, 21M parameters) that runs on a plain CPU.

## Why synrag

| | |
|---|---|
| ⚡ **Seconds, not minutes** | 57.6K documents searchable in **1.6 s** on a 6-core CPU. Embedding models need 60–282 s on a GPU or 16 min–1.7 h on the same CPU. |
| 🧠 **Own embedding model on CPU** | Synapse embeds **51,600 documents/s** on 6 cores — no GPU, no embedding API, nothing leaves your machine. |
| 🔎 **Hybrid retrieval** | BM25 with an analyzer for any language + Synapse vectors + an optional contextual reranker, fused per query. |
| 📄 **Reads your real files** | PDF, DOCX, XLSX, PPTX, ODF, HTML, Markdown, CSV, JSON, ZIP — built-in parsers; OCR via any external command. |
| ✂️ **Compact, cited context** | Picks the sentences that answer the question under a token budget: **43% fewer prompt tokens** at the same answer quality, with `[n]` citations (source, section, page). |
| 🔁 **Live updates, crash-safe** | Add or replace a document in 0.2 ms while searches continue; every change is journaled and fsynced. |
| 🤖 **Agents first** | MCP server for Claude, Cursor and any MCP client; REST API; dependency-free Python SDK; OpenAI-style tool definitions. |
| 🏢 **Ready for the security review** | SSO (OIDC), per-document ACLs inside retrieval, hash-chained audit log, encryption at rest, sharded cluster, Helm. |

## Benchmarks, including where we lose

nDCG@10 on public **test** sets, one machine for every system (AMD Ryzen 5 7500F, 6 cores, 31 GB RAM; models on an RTX 5060 Ti).
synrag settings were chosen on train/dev only. Full tables, methods and scripts: **[BENCHMARKS.md](BENCHMARKS.md)**.

| System | Hardware | English (BEIR, 3 sets) | 5 languages (MLQA) | 14 languages (Belebele) | Index 57.6K docs | RAM |
|---|---|---:|---:|---:|---:|---:|
| **synrag + reranker** | CPU | 0.455 | **0.664** | **0.874** | **1.6–4.8 s** | **443–475 MB** |
| EmbeddingGemma | GPU | **0.503** | 0.658 | 0.852 | 282 s | 2.8 GB + 5.6 GB VRAM |
| bge-small-en-v1.5 | GPU | 0.478 | 0.224 | — | 107 s | 2.1 GB + 0.8 GB VRAM |
| multilingual-e5-small | GPU | 0.430 | 0.624 | 0.830 | 74 s | 2.5 GB + 1.1 GB VRAM |
| Elasticsearch + embedding model | GPU | 0.455–0.474 | 0.641–0.657 | 0.843–0.853 | ES + model | 4.9 GB + model |
| Elasticsearch BM25 | CPU | 0.424 | 0.585 | 0.791 | 12.7 s | 4.9 GB |
| Tantivy + Model2Vec (Rust) | CPU | 0.430 | 0.644 | 0.815 | 2.8 s | 1.85 GB |

- **Where synrag loses:** best English quality still comes from transformer models on a GPU (bge-small +0.023, EmbeddingGemma +0.048);
  on large languages (Hindi, Persian, Russian, Arabic, Turkish, German) EmbeddingGemma is better; cross-lingual search is weak.
- **Where it leads:** cost and speed on a CPU, and low-resource languages — Kazakh, Uzbek, Kyrgyz, Tajik: +0.10…+0.24 over EmbeddingGemma.
- **Over HTTP** (FiQA, keep-alive): p50 **0.76 ms**, 6,325 q/s from 12 clients, 315 MB — Elasticsearch 8.15: 1.96 ms, 3,197 q/s, 4.7 GB.
- **Scale:** 8.8M MS MARCO passages on one server — BM25 ready in 22 s, with Synapse in 2.4 min, 7–10 ms per query.

## Install

| | |
|---|---|
| **One line** | `curl -fsSL https://ai.synlabs.pro/install.sh` <code>&#124;</code> `sh` — the 3 MB binary to `~/.local/bin`, the models (~86 MB: Synapse; reranker 0.3 MB) to `~/.synrag/models`, SHA-256 verified ([script](install.sh)); `SYNRAG_NO_MODELS=1` for the binary only (BM25) |
| **Manual** | [Releases](https://github.com/Synlabs-ai/synrag/releases/latest): `synrag-1.16.0-linux-x86_64`, `synapse-v2.synm`, `rerank-v1.synr`, Python wheel, `SHA256SUMS` |
| **Docker** | `docker compose up` with [docker-compose.yml](docker-compose.yml) — image built from the release binary ([Dockerfile](docker/Dockerfile)) |
| **Python** | `pip install synrag` ([PyPI](https://pypi.org/project/synrag/)) |
| **MCP server** | `uvx synrag-mcp` ([PyPI](https://pypi.org/project/synrag-mcp/), [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=synrag): `io.github.Synlabs-ai/synrag`) |

Linux x86-64 with glibc 2.30+ (Ubuntu 20.04+, Debian 11+, RHEL 9). Windows: WSL2. macOS / ARM builds are coming.

## Quickstart

```bash
M=~/.synrag/models
synrag index ./docs -o docs.syn --student $M/synapse.synm             # parse + index a folder
synrag search docs.syn "how do refunds work" -k 5 --student $M/synapse.synm
synrag context docs.syn "how do refunds work" --budget 600 --student $M/synapse.synm
synrag serve docs.syn --student $M/synapse.synm --rerank $M/rerank.synr --port 7878
```

| HTTP | |
|---|---|
| `GET /search?q=…&k=10` | hybrid search: one hit per document with source, title, heading, page, text, score |
| `GET /context?q=…&budget=1500` | the sentences that answer the query, with `[n]` citations and sources |
| `POST /add` `{"docs":[{"source","title","text"}]}` | add or replace documents, searchable immediately |
| `POST /upload?source=report.pdf` | parse and index a file on the server |
| `POST /delete` `{"sources":[…]}` | delete documents |

Collections, API keys and roles: `synrag serve --data ./data --api-keys keys.json` — see the [docs](https://ai.synlabs.pro/docs/).

## Use it from an agent

**MCP** (Claude Desktop, Cursor, Windsurf, Claude Code…) — [examples/mcp](examples/mcp):

```json
{
  "mcpServers": {
    "synrag": {
      "command": "uvx",
      "args": ["synrag-mcp", "--index", "/home/me/notes.syn", "--build-from", "/home/me/notes"]
    }
  }
}
```

Tools: `search_documents`, `get_context`, `list_collections`; with `--allow-writes` also `add_document`, `add_file`, `delete_documents`.
Claude Code: `claude mcp add synrag -- uvx synrag-mcp --index ~/notes.syn --build-from ~/notes`. The server finds the
installed engine and the Synapse model by itself.

**Python** — `pip install synrag` · [python/](python):

```python
import os
from synrag import Server

with Server("docs.syn", build_from=["./docs"], student=os.path.expanduser("~/.synrag/models/synapse.synm")) as rag:
    ctx = rag.context("how do refunds work?", budget=800)
    print(ctx.text)       # sentences with [n] citations
    print(ctx.sources)    # source, title, page per [n]
    rag.add([{"source": "faq.md", "title": "FAQ", "text": "..."}])   # live update
```

A complete tool-calling agent with any OpenAI-compatible LLM (Ollama, vLLM, OpenAI): [python/examples/agent_demo.py](python/examples/agent_demo.py).
Connectors with incremental sync: S3, Confluence, SharePoint / OneDrive, Google Drive, SQL, folders — `synrag.connectors`.

## Editions

| | Community | Production | Enterprise | OEM |
|---|---|---|---|---|
| Price | **free** | [see pricing](https://ai.synlabs.pro/pricing/) | [see pricing](https://ai.synlabs.pro/pricing/) | on request |
| Chunks | 1M per organization | 50M per installation | unlimited | by agreement |
| Covers | your organization | one installation per subscription unit | your organization | your distributed product |
| Search, Synapse, reranker, parsers, MCP, SDK, API keys | ✓ | ✓ | ✓ | ✓ |
| SSO, document ACLs, audit, encryption at rest, cluster | | | ✓ | ✓ |
| Redistribution in software you ship | | | | ✓ |

Commercial use and SaaS backends are allowed in the free Community edition. Licenses are signed files verified **offline** —
no activation server, no telemetry. After a paid term ends: 30 days fully working, then 90 days read-only, then serving stops
until renewal; `synrag export` gets every document out at any time. Who may do what: **[LICENSE.md](LICENSE.md)**.
Plans and a free 14-day Enterprise trial: **[ai.synlabs.pro/pricing](https://ai.synlabs.pro/pricing/)**.

## Documentation

- [Docs](https://ai.synlabs.pro/docs/) — install, CLI, HTTP API, Python, MCP, collections, licenses
- [Production guide](docs/production.md) — Docker, Kubernetes, SSO, ACLs, audit, encryption, backups, cluster
- [Security review](docs/security-review.md) — method, findings and fixes, residual risks
- [Benchmarks](BENCHMARKS.md) — every table and how to reproduce it
- Full technical report (Russian, PDF): [ai.synlabs.pro/report](https://ai.synlabs.pro/report/synrag-benchmark-report-ru.pdf)

## What is in this repository

The engine ships as a binary in [Releases](https://github.com/Synlabs-ai/synrag/releases); its source is not published.
This repository holds everything around it, under Apache 2.0: the [Python SDK, connectors and MCP server](python),
[examples](examples), the [Dockerfile](docker/Dockerfile), the [installer](install.sh) and [benchmark scripts](benchmarks); plus the [documentation](docs).
Issues and feature requests are welcome here.

## License

- **Engine binary and models:** [synrag Community License](LICENSE.md) — free, including commercial use, up to 1M chunks per
  organization; paid editions per [pricing](https://ai.synlabs.pro/pricing/) and [Terms](https://ai.synlabs.pro/terms/). Not open source.
- **Code in this repository** (Python SDK, connectors, MCP server, examples, scripts, Docker files): [Apache 2.0](LICENSE-APACHE-2.0.txt).

© 2026 SYNLABS MCHJ (SYNLABS LLC) · [info@synlabs.pro](mailto:info@synlabs.pro)
