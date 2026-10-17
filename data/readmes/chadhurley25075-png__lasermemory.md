<p align="center"><img src="docs/assets/lasermemory-banner.png" alt="LaserMemory" width="760"></p>

<h1 align="center">LaserMemory</h1>
<p align="center"><b>Point it at anything. Watch it read. It keeps what matters — and writes its own wiki.</b></p>
<p align="center">
<img alt="license" src="https://img.shields.io/badge/license-Apache--2.0-blue">
<img alt="python" src="https://img.shields.io/badge/python-3.10%20%E2%80%93%203.14-informational">
<img alt="platforms" src="https://img.shields.io/badge/runs%20on-Linux%20%C2%B7%20macOS%20%C2%B7%20Docker-success">
<img alt="gpu" src="https://img.shields.io/badge/GPU-optional-brightgreen">
<img alt="mcp" src="https://img.shields.io/badge/agents-HTTP%20%C2%B7%20MCP-purple">
</p>

LaserMemory is a **memory system you can watch**. Give it a web page, a PDF, a Word, PowerPoint or Excel file, a CSV,
Markdown, HTML, plain text, or a photo of a page. A laser eye reads it passage by passage, and a small local *keeper*
model decides — live, with a real probability — what is worth remembering. Kept passages become short facts that are
checked against their source. The facts grow into a searchable memory **and a wiki that links itself**, and any
agent can use both over HTTP or MCP.

<p align="center"><img src="docs/assets/lasermemory-reading.png" alt="Step mode: the eye stops on a passage it kept, and the Learn tab shows why" width="880"></p>

**Built for three kinds of people:** teachers who want to *show* how an AI memory works, students and researchers who
want to *collect and study* what a memory agent keeps and why, and anyone who wants a private, searchable library of
what they read.

## What it does

- **Reads anything.** Web pages through a real headless browser; PDFs with their tables; Office documents; CSV,
  JSON, Markdown, text; scans and photos through OCR. Any public URL, any upload, or pasted text.
- **Decides what to keep — visibly.** The eye fires its laser at each passage and sweeps it while the keeper decides.
  Kept passages flash green with their probability; reference lists are filed as citations, not knowledge.
- **Stores facts, not paraphrase.** A distilled fact must use only numbers and names found in its passage, and the
  keeper confirms the passage states it. Table rows are kept word for word. Every memory keeps its source, page and
  passage.
- **Grows without noise.** Re-reading strengthens a fact instead of duplicating it; look-alike facts with different
  figures stay apart; related facts link to each other.
- **Writes its own wiki.** Every fact files itself onto pages for its source, its topics and the names it mentions.
  Pages link to each other through `[[wiki links]]` and shared facts, update the moment new data arrives, accept
  notes, and export as an Obsidian vault. → [docs/WIKI.md](docs/WIKI.md)
- **Finds the answer.** Hybrid search (meaning + words) with a reranker; every result cites its source.
- **Runs anywhere.** No GPU? It still works. A laptop GPU, a gaming card, a Mac, a server — `lasermemory setup`
  detects the hardware and configures the right models. → [docs/MODELS.md](docs/MODELS.md)
- **Agent-ready.** HTTP API, an MCP server (14 tools), an `llms.txt` guide, a CLI, JSON / Markdown / wiki export.

- **A desktop wiki app.** `lasermemory desktop` opens it like Obsidian: page reader, local graph, backlinks,
  quick switcher, and a global graph where the eye fires at whatever you point to. It starts by laser-engraving
  its name and your wiki's numbers.

<p align="center"><img src="docs/assets/lasermemory-wiki.png" alt="The wiki app: a page, its local graph and backlinks" width="880"></p>
<p align="center"><img src="docs/assets/lasermemory-startup.png" alt="The start-up: the eye engraves the name and your wiki's numbers" width="880"></p>
<p align="center"><img src="docs/assets/lasermemory-graph.png" alt="The graph view: the eye fires at the page under the cursor" width="880"></p>

## Teach, study, research

- **Step through every decision.** Turn on **Step** and the laser stops at each passage; the **Learn** tab shows the
  exact question the keeper was asked, its confidence against the threshold, whether a model or the simple rules
  decided (with each rule that moved the score), and the facts it wrote down. Click any passage later to see the same.
- **A dataset of every decision.** Each passage the keeper judges is logged — text, confidence, kept or skipped,
  method, and the facts it produced — and exports as JSONL/CSV or a zip with a datasheet.
- **Study what you read.** Fill-in-the-blank flashcards from the facts (Anki or CSV) and a BibTeX entry for every
  source.
- **Collects politely.** Honours each site's `robots.txt` by default and reads only the public web.

Lesson plans and exercises: [docs/TEACHING.md](docs/TEACHING.md) · the dataset and responsible collection:
[docs/DATA.md](docs/DATA.md).

<p align="center"><img src="docs/assets/lasermemory-learn.png" alt="The Learn tab with no keeper model: the simple rules and how each moved the score" width="880"></p>

## Quick start

```bash
git clone https://github.com/chadhurley25075-png/lasermemory && cd lasermemory
python3 -m venv .venv && . .venv/bin/activate
pip install ".[cpu]"
lasermemory setup            # detects your hardware, installs the browser, writes a config
lasermemory serve            # open http://127.0.0.1:8140
```

From another terminal, or from an agent:

```bash
lasermemory add https://en.wikipedia.org/wiki/Tardigrade report.pdf notes.docx -c research
lasermemory ask "how long can tardigrades survive without water" -c research
lasermemory wiki list -c research
lasermemory wiki export ./research-vault -c research      # open it in Obsidian
lasermemory desktop                                       # or open the wiki as a desktop app
```

Docker (no GPU needed): `docker build -t lasermemory . && docker run -p 127.0.0.1:8140:8140 -v lm:/data lasermemory`

## Which models, on which machine

| Your machine | Tier | Keeper | Search | You need |
|---|---|---|---|---|
| Any laptop, no GPU | `cpu` | built-in rules | bge-small + MiniLM reranker on the CPU | nothing else |
| 4–8 GB GPU, M1/M2 Mac | `small` | Qwen3-4B-Instruct (Ollama) | nomic-embed + CPU reranker | [Ollama](https://ollama.com) |
| 8–24 GB GPU, 16–32 GB Mac | `medium` | Qwen3-4B-Instruct ×2 | nomic-embed + MiniLM-L12 reranker | Ollama |
| 24 GB+ GPU, Mac Studio, DGX | `large` | Qwen3-4B-Instruct ×6 | nomic-embed + MiniLM-L12 reranker | Ollama |
| Your own model servers | `server` | any OpenAI-compatible model | any embedder / reranker | URLs |

All models are open-weight (Apache-2.0 / MIT) and run locally; nothing leaves your machine unless you point it at a
hosted API. Why these models, how to swap them, and licenses: [docs/MODELS.md](docs/MODELS.md).

## Measured

Every answer is checked at three layers (in the source? kept in memory? found by search?) — see [docs/EVAL.md](docs/EVAL.md).
**Held-out** pages and questions were chosen after all tuning ended; the **main** set is the one the system was tuned on.

| Setup | Held-out: first answer right | Held-out: in top 5 | Main: first | Main: top 5 | Facts supported by their source |
|---|---|---|---|---|---|
| `cpu` tier — no GPU, nothing but Python | 60% | 73% | 82% | 100% | — (no keeper model) |
| `medium` tier — RTX 5080, Qwen3-4B keeper, CPU reranker | 73% | 87% | 78% | 98% | 100% / 99% of 120 judged |
| `medium` + a GPU reranker (Qwen3-Reranker-0.6B) | **87%** | **100%** | 86% | 100% | 99% / 100% of 120 judged |

Measured on the release code (v1.1.0). Every model setup kept 100% of the answers in memory. "Facts supported" = an
independent, much larger judge model (GLM-5.3-Flash) read 120 sampled facts per run next to the passages they came
from. One held-out answer pattern was widened after a correct answer ("Edwin P. Hubble") was graded wrong; every
row above was re-run with the corrected pattern.

## Tested on

| # | Machine | OS | Python | Setup | Tests | Main set: first / top 5 | Held-out: first / top 5 | Facts supported |
|---|---|---|---|---|---|---|---|---|
| 1 | NVIDIA DGX Spark (GB10) | Linux arm64 | 3.12 | cpu · rules keeper, bge-small + MiniLM-L6 on CPU | 98 passed | 82% / 100% | 60% / 73% | — |
| 2 | DGX Spark | Linux arm64 | 3.10 | cpu | 98 passed | 86% / 100% | — | — |
| 3 | DGX Spark, its own GPU | Linux arm64 | 3.11 | small · setup pulled Qwen3-4B into local Ollama | 99 passed | 80% / 100% | — | 100% of 60 |
| 4 | Desktop PC (RTX 5080 16 GB) | Linux x86-64 | 3.12 | medium · auto-detected · Qwen3-4B + nomic + MiniLM-L12 | 98 passed, 1 skipped | 80% / 96% | 73% / 87% | — |
| 5 | Desktop PC (RTX 5080) | Linux x86-64 | 3.12 | medium with qwen2.5:7b-instruct as keeper | 97 passed, 1 skipped | 49% / 76% (only 84% of answers kept) | — | — |
| 6 | Mac Studio (M3 Ultra) | macOS arm64 | 3.14 | cpu | 97 passed, 1 skipped | 82% / 100% | 60% / 73% | — |
| 7 | Mac Studio → RTX 5080 desktop | macOS arm64 | 3.14 | server · keeper and embedder on another machine's GPU | 98 passed, 1 skipped | 80% / 98% | — | — |
| 8 | Docker on the DGX Spark | Debian arm64 container | 3.12 | cpu (image default) | smoke + eval | 82% / 100% | — | — |
| 9 | DGX Spark | Linux arm64 | 3.12 | full test suite 10 times in a row | 10/10 runs green | — | — | — |
| 10 | DGX Spark → RTX 5080 desktop | Linux arm64 | 3.12 | Qwen3-4B + nomic + Qwen3-Reranker-0.6B GPU | smoke + eval | 86% / 100% | 93% / 100% | 100% of 60 · 100% of 60 |

Notes: the matrix ran on the code as it stood mid-testing; the table above it is the release code. Rounds 4 and 7 are shown on the final defaults — their first runs used bge-reranker-base, which scored ~51% first
and was replaced (see [MODELS](docs/MODELS.md#choosing-a-reranker--measured)). Round 5 also ran on that earlier
reranker; it is in the table for its keeper result: `qwen2.5:7b-instruct` kept only 84% of the answers, Qwen3-4B 100%.
Round 3's first test run failed 3 tests because the suite read the machine's own config file; fixed, re-run shown.
Every round: a fresh clone, a fresh virtual environment, `lasermemory setup`, the full test suite, then the eval.

## Use it from an agent

```bash
claude mcp add lasermemory -- lasermemory mcp          # Claude Code; see docs/MCP.md for others
```

Tools: `search_memory` · `get_memory` · `recent_memories` · `memory_stats` · `list_collections` · `list_sources` ·
`ingest_url` · `ingest_file` · `ingest_text` · `remember_note` · `forget_memory` · `wiki_pages` · `wiki_page` · `wiki_add`.
Agents without MCP read `/llms.txt`.

## Documentation

| | |
|---|---|
| [TEACHING](docs/TEACHING.md) | lesson plans, exercises, classroom setup |
| [DATA](docs/DATA.md) | the decision dataset, exports, responsible collection |
| [INSTALL](docs/INSTALL.md) | venv, pipx, Docker, systemd, tiers, tests |
| [MODELS](docs/MODELS.md) | which models, why, tiers, swapping, licenses |
| [WIKI](docs/WIKI.md) | how the wiki writes and links itself |
| [CONFIG](docs/CONFIG.md) | config file and every setting |
| [OUTPUTS](docs/OUTPUTS.md) | where everything is written; the life of one ingest |
| [API](docs/API.md) · [`/llms.txt`](lasermemory/static/llms.txt) | HTTP API and live events |
| [MCP](docs/MCP.md) | Claude Code, Claude Desktop, Cursor |
| [ARCHITECTURE](docs/ARCHITECTURE.md) | how it works and why |
| [EVAL](docs/EVAL.md) | how retrieval was measured |

## Security

- Listens on `127.0.0.1` by default; set `api_key` or `allow_nets` before binding a public address. With a key set,
  open the reader or wiki app once as `…/?key=<your key>` (or type it when asked); the browser remembers it.
- Reads only the public web: the browser's sole route out is a built-in proxy that checks every connection —
  redirects included — and refuses private, loopback, link-local, carrier-grade NAT and local names.
- Documents are processed locally; text goes only to the model endpoints you configure.

## License

Release notes: [CHANGELOG.md](CHANGELOG.md).

Apache License 2.0 — see [LICENSE](LICENSE) and [NOTICE](NOTICE). Copyright 2026 Chad Hurley.
Every runtime dependency is under a permissive licence (PDFs are read with pdfplumber, MIT, and pypdfium2,
Apache-2.0 / BSD-3-Clause); see [docs/MODELS.md](docs/MODELS.md#third-party-software-and-licenses).
