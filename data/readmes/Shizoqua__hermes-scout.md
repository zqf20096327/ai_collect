<div align="center">

<img src="docs/logo.svg" width="88" height="88" alt="hermes-scout logo">

# hermes-scout

**Search your local files by meaning, not just keywords.**<br>
A [Hermes Agent](https://github.com/NousResearch/hermes-agent) plugin and a standalone command line tool.

![hermes-scout: find anything in your files by meaning](docs/banner.png)

[![PyPI](https://img.shields.io/pypi/v/hermes-scout?label=pypi&color=7c5cff&logo=pypi&logoColor=white&labelColor=1e1b2e&style=flat-square)](https://pypi.org/project/hermes-scout/)
[![Downloads](https://img.shields.io/pepy/dt/hermes-scout?label=downloads&color=ec4899&logo=python&logoColor=white&labelColor=1e1b2e&style=flat-square)](https://pepy.tech/project/hermes-scout)
[![tests](https://img.shields.io/github/actions/workflow/status/Shizoqua/hermes-scout/tests.yml?branch=main&label=tests&logo=githubactions&logoColor=white&labelColor=1e1b2e&style=flat-square)](https://github.com/Shizoqua/hermes-scout/actions/workflows/tests.yml)
[![docs](https://img.shields.io/github/actions/workflow/status/Shizoqua/hermes-scout/docs.yml?branch=main&label=docs&logo=materialformkdocs&logoColor=white&labelColor=1e1b2e&style=flat-square)](https://shizoqua.github.io/hermes-scout/)
<br>
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-3b82f6?logo=python&logoColor=white&labelColor=1e1b2e&style=flat-square)](https://www.python.org/)
[![Hermes Agent plugin](https://img.shields.io/badge/Hermes%20Agent-plugin-a855f7?labelColor=1e1b2e&style=flat-square)](https://github.com/NousResearch/hermes-agent)
[![Zero dependencies](https://img.shields.io/badge/dependencies-zero-14b8a6?labelColor=1e1b2e&style=flat-square)](#development)
[![License: MIT](https://img.shields.io/badge/license-MIT-f59e0b?labelColor=1e1b2e&style=flat-square)](LICENSE)
[![OpenSSF Scorecard](https://img.shields.io/ossf-scorecard/github.com/Shizoqua/hermes-scout?label=openssf%20scorecard&logo=securityscorecard&logoColor=white&labelColor=1e1b2e&style=flat-square)](https://scorecard.dev/viewer/?uri=github.com/Shizoqua/hermes-scout)

[**Documentation**](https://shizoqua.github.io/hermes-scout/) ·
[**Getting started**](https://shizoqua.github.io/hermes-scout/getting-started/) ·
[**Changelog**](CHANGELOG.md) ·
[**Report a bug**](https://github.com/Shizoqua/hermes-scout/issues/new/choose)

</div>

---

Ask *"where do we handle rate limits?"* and get back the relevant paragraphs from your notes, docs
or code, even when they never use the words "rate limit". Results come with file paths, line
numbers and a similarity score.

hermes-scout works two ways:

- **As a Hermes Agent plugin**, adding two tools: `scout_search` (find passages) and
  `scout_similar` (find files related to a file or passage).
- **As a standalone command**, `hermes-scout search "..." ~/notes`, for anyone with Python.

Embeddings come from any OpenAI-compatible `/embeddings` endpoint. By default that is a local
[Ollama](https://ollama.com) server, so indexing and searching stay on your machine and cost nothing.

![Demo: hermes-scout doctor, a keyword search that misses the backups doc, the default search that finds it first, an error code search and find similar](docs/demo.gif)

<sub>A real session with `nomic-embed-text` on Ollama, on the synthetic benchmark project. The raw
recording is [docs/demo.cast](docs/demo.cast); only the typing speed is paced.</sub>

## Contents

- [Why](#why)
- [Architecture](#architecture)
- [What's inside](#whats-inside)
- [What's new in 0.5](#whats-new-in-05)
- [What you can ask](#what-you-can-ask)
- [What this is, and what it is not](#what-this-is-and-what-it-is-not)
- [Screenshots](#screenshots)
- [Features](#features)
- [Quick start](#quick-start)
- [Command line](#command-line)
- [Choosing a search mode](#choosing-a-search-mode)
- [In Hermes: the /scout command](#in-hermes-the-scout-command)
- [Example](#example)
- [How it works](#how-it-works)
- [Benchmark](#benchmark)
- [Supported embedding servers](#supported-embedding-servers)
- [Settings](#settings)
- [Troubleshooting](#troubleshooting)
- [Disclosure](#disclosure)
- [Roadmap](#roadmap)
- [Repository layout](#repository-layout)
- [Development](#development)
- [Contributing](#contributing)
- [Star History](#star-history)
- [License](#license)

## Why

Keyword search only finds the words you remember. Notes say "back off and retry", code says
`except HTTPError as err: if err.code == 429`, and docs say "throttling". You remember none of
those phrasings. Semantic search compares *meaning*: the query and every passage are turned into
embedding vectors, and the passages pointing in the most similar direction come back first.

![Keyword search: the question shares no words with docs/backups.md, so it is not found](docs/problem.png)

![hermes-scout: the same question puts docs/backups.md first, and the code name E4021 still works](docs/solution.png)

Both cards show real output on the benchmark project; the semantic result is from the recorded demo.

## Architecture

hermes-scout reads the folder you name, splits its files into chunks of whole lines and turns each
chunk into a meaning vector with your embeddings server. The vectors and a keyword index are saved
in one SQLite file on your machine. For every question, `scout_search` and `scout_similar` rank that
index and return the file, the lines and a score. Details in [How it works](#how-it-works).

![hermes-scout architecture: your folder is read, split and embedded by the index pipeline, saved to a SQLite index, and ranked by scout_search and scout_similar](docs/architecture.png)

## What's inside

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/cover-search.png" alt="scout_search: find passages by meaning and by exact names">
      <p><strong><code>scout_search</code></strong></p>
      <p>Finds the passages that answer a question in a folder of notes, docs, code and documents (PDF, Word, Excel, PowerPoint, OpenDocument), best first, with file, line range and score.</p>
      <p><b>Ask Hermes:</b> <i>"Search ~/notes for my backup plan."</i></p>
      <p><b>Ranking:</b> <code>hybrid</code> (default), <code>semantic</code> or <code>keyword</code></p>
    </td>
    <td width="50%" valign="top">
      <img src="docs/cover-similar.png" alt="scout_similar: find the files most related to a file or a passage">
      <p><strong><code>scout_similar</code></strong></p>
      <p>Finds the files most related to a file, a line range of it, or a passage you paste: related notes, overlapping docs, code that does the same job.</p>
      <p><b>Ask Hermes:</b> <i>"What else in ~/notes is like notes/ideas.md?"</i></p>
      <p><b>Returns:</b> one result per file, closest first</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/cover-command.png" alt="/scout: check your setup and look after the index">
      <p><strong><code>/scout</code></strong></p>
      <p>A command inside Hermes to check the setup and look after the index, without asking the agent.</p>
      <p><b>Try:</b> <code>/scout doctor</code>, <code>/scout status</code>, <code>/scout index ~/notes</code>, <code>/scout clear ~/notes</code></p>
    </td>
    <td width="50%" valign="top">
      <img src="docs/cover-cli.png" alt="hermes-scout: the same search in any terminal">
      <p><strong><code>hermes-scout</code> command</strong></p>
      <p>The same search in any terminal, no Hermes needed. <code>--json</code> output for scripts.</p>
      <p><b>Install:</b> <code>pipx install hermes-scout</code></p>
      <p><b>Try:</b> <code>hermes-scout search "how I set up backups" ~/notes</code></p>
    </td>
  </tr>
</table>

## What's new in 0.5

- **Excel, PowerPoint and OpenDocument files** are searched too (`.xlsx`, `.pptx`, `.odt`, `.ods`,
  `.odp`), next to PDF and Word, still with the Python standard library only.
- **Every result from a document says where it is**: it starts with its `[page N]`, `[slide N]` or
  `[sheet Name]` line, even when that line is far above the passage.

Version 0.4 brought PDF and Word files, the measured default ranking, `/scout` and `hermes-scout
doctor`, the built-in skill and the public benchmark. Full list in the [changelog](CHANGELOG.md).

## What you can ask

Inside Hermes, ask in your own words; the agent calls `scout_search` or `scout_similar`:

- *"Where do we handle rate limits in ~/project?"*
- *"Which of my notes covers the backup plan?"*
- *"Find the meeting notes where we decided to switch databases."*
- *"What does error E4021 mean? Search the billing code."*
- *"Which PDFs in ~/reports mention the restore drill, and on which page?"*
- *"Which slide in ~/decks covers the migration timeline?"*
- *"What else in ~/notes is like notes/ideas.md?"*

## What this is, and what it is not

**It is** a private search engine for one folder at a time: notes, docs, code and documents (PDF,
Word, Excel, PowerPoint, OpenDocument) on your own machine, ranked by meaning with exact names and
codes found first.

**It is not** a web search, a chat memory or a document store. It never edits or uploads your files;
only text chunks go to the embeddings server you choose, which by default runs on your machine. In
Hermes, the passages a search returns are read by the model Hermes uses, like any file Hermes
opens. Scanned PDFs (pictures of pages), images and older `.doc`, `.xls` and `.ppt` files are not
read. See [PRIVACY.md](PRIVACY.md).

## Screenshots

<table>
  <tr>
    <td><img src="docs/screenshots/exact-search.png" alt="Searching the sample project for an error code and a tool name, with a folder filter"></td>
    <td><img src="docs/screenshots/doctor.png" alt="hermes-scout doctor explaining how to start the embeddings server"></td>
  </tr>
  <tr>
    <td><img src="docs/screenshots/scout-command.png" alt="The /scout command inside Hermes"></td>
    <td><img src="docs/screenshots/benchmark.png" alt="Benchmark results: 93% of questions answered with the right file first"></td>
  </tr>
</table>

The demo, the cards and the diagram are made by scripts too: the `demo` workflow records a real
session (`scripts/record_demo.py`), `scripts/render_demo.py` turns it into `docs/demo.gif` and
`docs/demo.mp4`, and `scripts/make_visuals.py` renders the pictures (sources in `docs/visuals/`).
Each screenshot shows real hermes-scout output on the synthetic project in `benchmarks/corpus`, or
the measured benchmark numbers, made by [`scripts/make_screenshots.py`](scripts/make_screenshots.py).

## Features

- **Hybrid search.** Ranks by meaning *and* by exact words together, so it finds "how we handle
  throttling" and `ERR_4291` alike. Switch to meaning-only or keyword-only when you want.
- **Documents.** Reads the text of PDF, Word, Excel, PowerPoint and OpenDocument files on your own
  machine; each result says which page, slide or sheet it came from.
- **Find similar.** Point at a file or a passage and get the most related files: related notes,
  overlapping docs, code that does something similar.
- **Local-first.** Works out of the box with Ollama, LM Studio, llama.cpp or vLLM on your own machine.
- **Fast repeat searches.** An incremental index re-embeds only files that changed since the last search.
- **Safe by default.** Skips hidden files (such as `.env`), dependency folders and binaries, and in
  Hermes every path Hermes's own file tools refuse to read, such as credential stores.
- **Zero dependencies.** Python standard library only: nothing extra to install or audit.
- **Respects `.gitignore`.** Files your project ignores (build output, logs, generated code) stay
  out of the index, at every folder level, with `!` re-includes, just like git.
- **Filters.** Narrow a search to `*.md`, `docs/` or `src/**/*.py` without re-indexing.
- **Precise results.** Every hit names the file, the line range and a cosine similarity score
  (keyword-only searches have no score).
- **Cross-platform.** Tested on Linux, macOS and Windows with Python 3.11 to 3.14.
- **Two ways to use it:** as a Hermes tool or as a `hermes-scout` command in any terminal.
- **Configurable** from the Hermes Desktop settings page or `hermes plugins config hermes-scout`.

## Quick start

1. **Start a local embeddings server** (Ollama shown; see [other servers](#supported-embedding-servers)):

   ```bash
   ollama pull nomic-embed-text
   ollama serve            # if it is not already running
   ```

2. **Install hermes-scout** in Hermes:

   ```bash
   hermes plugins install Shizoqua/hermes-scout/hermes_scout
   hermes plugins enable hermes-scout
   ```

   or as a command line tool:

   ```bash
   pipx install hermes-scout      # or: pip install hermes-scout
   ```

3. **Check the setup** before your first search, using the option that matches your install:

   - **Hermes plugin:** run `/scout doctor` inside Hermes.
   - **Standalone CLI:** run `hermes-scout doctor` in a terminal.

   This checks the embeddings server, model and keyword search. If something fails, see
   [Troubleshooting](#troubleshooting).

4. **Search.** Ask Hermes:

   > Search my notes in ~/notes for how I set up backups.

   or run:

   ```bash
   hermes-scout search "how I set up backups" ~/notes
   ```

The first search of a folder builds its index. Later searches only re-read files that changed.

For example, to search Markdown notes only or look up an exact error code from the terminal:

```bash
hermes-scout search "meeting notes about backups" ~/notes -g "*.md"
hermes-scout search "ERR_4291" ~/project --ranking keyword
```

Use `--ranking keyword` when you already know the exact term or identifier you're looking for.

## Command line

```console
$ hermes-scout search "how do we keep a copy of the database in case it gets lost" benchmarks/corpus -k 3
0.63  docs/backups.md:1-15
      # Backups and restores
0.57  src/storage/cache.py:1-19
      """Read-through cache in front of the primary store."""
0.54  notes/meeting-2026-05-12.md:1-15
      # Platform meeting, 12 May
```

Real output with `nomic-embed-text` on Ollama, from the [recorded demo](docs/demo.cast).

| Command | What it does |
|---|---|
| `hermes-scout search QUERY [PATH]` | Search a folder (default: the current one). `-k 10` for more results, `-g "*.md"` to filter, `--ranking keyword` for exact words only, `--json` for scripts. |
| `hermes-scout similar FILE --in FOLDER` | Files most related to `FILE` (or `--text "..."`); `--lines 10-40` for part of a file. |
| `hermes-scout index [PATH]` | Build or refresh the index ahead of time. |
| `hermes-scout doctor` | Check the embeddings server, the model and keyword search, and say how to fix what fails. |
| `hermes-scout status` | List the indexed folders with file and chunk counts. |
| `hermes-scout clear PATH` | Forget a folder's index (`--all` for every folder). |
| `hermes-scout --version` | Print the version. |

Point it at another server with `--base-url` and `--model`, or the `SCOUT_BASE_URL` and
`SCOUT_MODEL` environment variables. Hosted endpoints read their key from `SCOUT_API_KEY`. The
index lives in your user cache folder (`~/.cache/hermes-scout/index.db` on Linux). Full reference:
[Command line docs](https://shizoqua.github.io/hermes-scout/cli/).

## Choosing a search mode

Search uses `hybrid` ranking by default, but you can switch modes depending on what you know
about the text you're looking for:

| Mode | When to use it | Example |
|---|---|---|
| `hybrid` (default) | Most searches. Questions are ranked by meaning; code names like `ERR_4291` put exact matches first. | `hermes-scout search "handling API timeouts" ~/project` |
| `semantic` | You know the idea but aren't sure how the files describe it | `hermes-scout search "recovering from failed requests" ~/project --ranking semantic` |
| `keyword` | You know an exact name, code or identifier | `hermes-scout search "ERR_4291" ~/project --ranking keyword` |

Start with `hybrid` if you're unsure. Keyword mode is useful for identifiers that embeddings
may not match reliably. Semantic mode is useful when your search terms differ from the wording
in the files. Keyword ranking requires SQLite FTS5; if it is unavailable, search falls back
to semantic ranking.

## In Hermes: the `/scout` command

| Command | What it does |
|---|---|
| `/scout doctor` | Checks the embeddings server, the model and keyword search in one go, with the fix for anything that fails. |
| `/scout status` | Lists the indexed folders with file and chunk counts. |
| `/scout index [folder]` | Builds or refreshes a folder's index now, so the first search does not wait for it. |
| `/scout clear <folder>`, `/scout clear all` | Forgets a folder's index, or every index. |

The plugin also ships a `scout` skill that tells the agent when searching by meaning beats a plain
text search, and how to narrow and cite results.

## Example

What the model receives from `scout_search` for the search above. Paths, line ranges, passages and
index counts are exact; the scores are the recorded ones, shown to two decimals; the passages are
cut short here.

```json
{
  "query": "how do we keep a copy of the database in case it gets lost",
  "ranking": "hybrid",
  "root": "/home/me/hermes-scout/benchmarks/corpus",
  "model": "nomic-embed-text",
  "results": [
    {
      "path": "docs/backups.md",
      "lines": "1-15",
      "score": 0.63,
      "text": "# Backups and restores\n\n## Nightly dumps\n\nA scheduled job runs `pg_dump` at 02:00 UTC for every region ..."
    },
    {
      "path": "src/storage/cache.py",
      "lines": "1-19",
      "score": 0.57,
      "text": "\"\"\"Read-through cache in front of the primary store.\"\"\"\n\nTTL_SECONDS = 300 ..."
    }
  ],
  "index": {"indexed_files": 0, "reused_files": 23, "removed_files": 0, "chunks": 23}
}
```

The answer comes first although the question shares no words with it, and `"indexed_files": 0`
shows that this search reused the index instead of embedding the folder again.

## How it works

The [architecture picture](#architecture) above shows the three steps; here is each one in detail.

1. **Chunking.** Text files are split into chunks of whole lines (1,200 characters by default).
   Neighbouring chunks share up to two lines, so a passage that straddles a boundary is still found
   whole. A line longer than the chunk size is split into pieces, so nothing is cut off.
2. **Embedding.** Chunks are sent to the embeddings endpoint in batches of 32 and stored as float32
   vectors with their precomputed norms.
3. **Incremental index.** The index lives in SQLite in the plugin's own data folder
   (`<hermes home>/plugin-data/hermes-scout/index.db`), keyed by folder and embedding model. Only
   new or changed files (by modification time and size) are re-embedded, and deleted files are dropped.
4. **Ranking.** The question is embedded the same way and every chunk gets a cosine similarity,
   `score = (q · c) / (‖q‖ ‖c‖)`. The question's words are also looked up in a keyword index
   (SQLite full-text search with BM25 and word stemming, built alongside the vectors), leaving out
   filler words such as "how" or "the" that appear everywhere. The default `hybrid` ranking picks by
   query: questions in words are ranked by meaning, which [the benchmark](#benchmark) measured as
   the most accurate for them; a query made only of code-like names (`ERR_4291`, `pg_dump`,
   `getUserById`), which embedding models often blur, merges both rankings by score with keywords
   at 75% and meaning at 25%, so the exact name comes first. The `ranking` setting (or the tool's `ranking` argument, or `--ranking`) switches to meaning only (`semantic`) or
   words only (`keyword`). If Python's SQLite lacks full-text search (FTS5), search falls back to
   meaning only and says so in a one-line note.
5. **Find similar.** `scout_similar` averages the vectors of a file (or a line range of it) and
   returns the other files whose best passage is closest, one result per file.

Indexes for different embedding models are kept apart, so switching models never mixes vectors.

**What gets indexed:** common text, documentation, code and config extensions (`.md`, `.txt`, `.py`,
`.ts`, `.go`, `.rs`, `.json`, `.yaml`, ...), plus the text of documents up to 20 MB: PDF, Word
(`.docx`), Excel (`.xlsx`), PowerPoint (`.pptx`) and OpenDocument (`.odt`, `.ods`, `.odp`)
([details](https://shizoqua.github.io/hermes-scout/how-it-works/#documents)). **Skipped:** hidden
files and folders, dependency and build folders (`node_modules`, `venv`, `dist`, `build`, ...),
anything a `.gitignore` file ignores, symlinks, binary files, files over the size limit and, in
Hermes, every path Hermes's file tools refuse to read.

## Benchmark

On a synthetic project of 23 files with 30 questions whose answer is known, using `nomic-embed-text`
on Ollama ([details and method](https://shizoqua.github.io/hermes-scout/benchmark/)):

| Ranking | Right file first | Right file in top 5 |
|---|---|---|
| Default (`hybrid`) | 93% | 100% |
| Meaning only (`semantic`) | 93% | 100% |
| Keywords only (`keyword`) | 63% | 83% |

Exact names and error codes are found first in every mode. Questions worded differently from the
answer are where meaning-based search pays off: 89% first-place hits against 39% for keywords alone.

## Supported embedding servers

Any server that implements the OpenAI `POST /embeddings` API works. Set `base_url` to its `/v1` root.

| Server | `base_url` | Example `embedding_model` |
|---|---|---|
| [Ollama](https://ollama.com) (default) | `http://localhost:11434/v1` | `nomic-embed-text`, `mxbai-embed-large` |
| [LM Studio](https://lmstudio.ai) | `http://localhost:1234/v1` | the embedding model you loaded |
| [llama.cpp server](https://github.com/ggml-org/llama.cpp) (`--embeddings`) | `http://localhost:8080/v1` | the loaded model's name |
| [vLLM](https://github.com/vllm-project/vllm) | `http://localhost:8000/v1` | e.g. `BAAI/bge-m3` |
| Hosted OpenAI-compatible APIs | the provider's `/v1` URL | the provider's embedding model (set `api_key`) |

## Settings

In Hermes, edit them in the Desktop app (**Settings → Plugins → hermes-scout**) or with
`hermes plugins config hermes-scout`. The command line takes the same settings as flags
(`--base-url`, `--model`, `--chunk-chars`, `--max-files`, `--max-file-kb`, `--no-gitignore`, `--no-documents`, `-k`).

| Setting | Default | Meaning |
|---|---|---|
| `base_url` | `http://localhost:11434/v1` | OpenAI-compatible base URL; the plugin calls `<base_url>/embeddings` |
| `embedding_model` | `nomic-embed-text` | Model name the endpoint serves |
| `api_key` | not set | Only for hosted endpoints; stored by Hermes as `SCOUT_API_KEY` |
| `top_k` | `5` | Passages returned per search (the model may ask for 1 to 20) |
| `chunk_chars` | `1200` | Chunk size in characters; applies to files indexed afterwards |
| `max_files` | `2000` | Files indexed per folder |
| `max_file_kb` | `1000` | Larger files are skipped |
| `respect_gitignore` | `true` | Skip files and folders that `.gitignore` files in the searched folder ignore |
| `read_documents` | `true` | Also index the text of PDF, Word, Excel, PowerPoint and OpenDocument files up to 20 MB |
| `ranking` | `hybrid` | `hybrid`: meaning for questions, exact words first for code names like `ERR_4291`; `semantic`: meaning only; `keyword`: exact words only |

## Troubleshooting

| Message | Fix |
|---|---|
| Not sure what is wrong | Run `/scout doctor` in Hermes or `hermes-scout doctor` in a terminal. It checks everything and names the fix. |
| `cannot reach the embeddings server at http://localhost:11434/v1` | Start Ollama (`ollama serve`) or point `base_url` at your server. |
| `answered HTTP 404 ... model not found` | Pull the model (`ollama pull nomic-embed-text`) or set `embedding_model` to one the server has. |
| `answered HTTP 401` | A hosted endpoint needs `api_key`. |
| A document never shows up in results | A scanned PDF (pictures of pages) or an encrypted file has no text to read, older `.doc`, `.xls` and `.ppt` files are not read, and anything over 20 MB is skipped. Check that `read_documents` is on. |
| No results for files you expected | Check the file's extension, size (`max_file_kb`), that it is not hidden or in a skipped folder, and that no `.gitignore` ignores it. |
| Search returns fewer files than expected | Check whether the folder contains more than `max_files` (2,000 by default) or whether the file exceeds `max_file_kb` (1,000 KB by default). Narrow the folder or adjust those limits. |
| The first search is slow | Expected for a large folder: every file is embedded once. Later searches only embed changes. |

If the server check fails, first confirm your embedding service is running. For the default
Ollama setup, `ollama list` shows your installed models; if `nomic-embed-text` is missing,
run `ollama pull nomic-embed-text`. Then run `hermes-scout doctor` again (or `/scout doctor`
inside Hermes).

If a search returns nothing, try the folder without a `-g` filter and check whether the file
is excluded by `.gitignore`. Hidden files, symlinks and binary files are not indexed even when
a search filter would match their names.

## Disclosure

The short version is below; [PRIVACY.md](PRIVACY.md) answers the common questions in full.

- **Network:** file contents (chunks) and search queries are sent to the embeddings endpoint you
  configure. The default is a server on your own machine. If you point `base_url` at a hosted API,
  that service receives the text of the files you search.
- **Files read:** text files under the folder the model asks to search, minus the skipped paths
  listed above, and documents (PDF, Word, Excel, PowerPoint, OpenDocument) unless `read_documents`
  is off. Their text is extracted on your machine with Python's standard library; no file is
  uploaded anywhere except as text chunks to the embeddings endpoint. The plugin never writes to
  that folder.
- **Results:** the passages a search returns go to Hermes, which reads them with the model you
  chose for Hermes, as it would any file it opens. With a hosted model, that provider sees them.
- **Files written:** the index database in the plugin's own data folder only. `/scout clear`
  deletes rows from it; nothing else is ever deleted.
- **Health check:** `/scout doctor` sends one fixed test sentence to the embeddings endpoint.
- **Credentials:** the optional API key is read through Hermes's secret store and sent only to the
  configured endpoint. It is dropped if the endpoint redirects to another origin.
- No telemetry, no background processes, no shell commands, no self-updating.

## Roadmap

- A published speed test on a large synthetic folder, next to the accuracy benchmark.
- An optional setting that puts the best matches in front of the model before it answers.
- Result diversity (MMR) so near-duplicate chunks do not crowd the top results.

Ideas and bug reports are welcome in [Issues](https://github.com/Shizoqua/hermes-scout/issues).

## Repository layout

```text
hermes-scout/
├── hermes_scout/              the plugin, also installed as the hermes-scout command
│   ├── plugin.yaml            manifest read by Hermes
│   ├── __init__.py            Hermes wiring: tools, /scout, settings, file-safety checks
│   ├── engine.py              chunking, file walking, the SQLite index and ranking
│   ├── documents.py           PDF, Office and OpenDocument text, standard library only
│   ├── embeddings.py          OpenAI-compatible embeddings client
│   ├── patterns.py            .gitignore rules and search filters
│   ├── checks.py              the doctor checks
│   ├── cli.py                 the hermes-scout command
│   ├── schemas.py             tool definitions shown to the agent
│   └── skills/scout/SKILL.md  the built-in skill
├── tests/                     unit tests, no network needed
├── benchmarks/                synthetic project and 30 questions with known answers
├── fuzz/                      Atheris fuzzing for the document readers
├── scripts/                   benchmark, screenshots, pictures and the demo
├── docs/                      documentation site (MkDocs Material), pictures and videos
└── .github/                   CI workflows and hash-locked CI tool requirements
```

## Development

The search engine (`hermes_scout/engine.py`) and the HTTP client (`hermes_scout/embeddings.py`) use
only the Python standard library and do not import Hermes, so the tests run without a Hermes install
or network access:

```bash
python -m pip install --require-hashes -r .github/requirements/test.txt -r .github/requirements/lint.txt
python -m pytest --cov=hermes_scout     # no network needed
ruff check . && ruff format --check .
mypy                                    # strict type check
```

Before a release, check the plugin the way the Hermes catalog does:

```bash
hermes plugins validate hermes_scout --install-deps
hermes plugins doctor hermes_scout --ci
```

Every pull request and every change to `main` runs lint, a strict type check, the tests on Linux,
macOS and Windows with Python 3.11 to 3.14 with a 90% coverage floor, and CodeQL security analysis.
Changes to the docs also get a strict docs build. An OpenSSF Scorecard rating runs on every change
to `main` and weekly. The document readers are fuzzed with Atheris every week and on every change to
them. CI tools are installed from hash-locked files in `.github/requirements/` (kept current by
Dependabot). Publishing a GitHub release uploads the package to PyPI.

## Contributing

Bug reports, ideas and pull requests are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md);
the [Code of Conduct](CODE_OF_CONDUCT.md) applies everywhere in this project. Report security
problems privately as described in [SECURITY.md](SECURITY.md). Release notes live in
[CHANGELOG.md](CHANGELOG.md).

If hermes-scout is useful to you, a star helps other people find it.

## Star History

<a href="https://star-history.com/#Shizoqua/hermes-scout&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Shizoqua/hermes-scout&type=Timeline&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Shizoqua/hermes-scout&type=Timeline" />
    <img alt="Star history of hermes-scout" src="https://api.star-history.com/svg?repos=Shizoqua/hermes-scout&type=Timeline&theme=dark" />
  </picture>
</a>

## License

MIT, see [LICENSE](LICENSE). Made by [Lanre Shittu](https://github.com/Shizoqua). To cite this project, use
the "Cite this repository" button on GitHub ([CITATION.cff](CITATION.cff)).
