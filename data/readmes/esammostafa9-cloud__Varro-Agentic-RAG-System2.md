<div align="center">

<img src="docs/varro-logo.svg" alt="" width="72" height="72">

# Varro RAG

**Ask your documents. Check every answer.**

[![CI](https://github.com/esammostafa9-cloud/Varro-Agentic-RAG-System2/actions/workflows/ci.yml/badge.svg)](https://github.com/esammostafa9-cloud/Varro-Agentic-RAG-System2/actions/workflows/ci.yml)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-3776AB)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Website](https://img.shields.io/badge/website-varro%20rag-c8ef5d)](https://esammostafa9-cloud.github.io/Varro-Agentic-RAG-System2/)

</div>

Varro is a private research assistant for your own documents that runs on your own computer. Ask a question in plain language and every claim in the answer cites the passage it came from; click a citation and the page opens with that passage highlighted. It turns the actions in a document into tasks you review before they count, and its agent compares documents, works out figures and drafts work for you to approve. One person can use it with no sign-in at all; a team can switch on accounts and roles.

<img alt="A 46-second tour of the demo workspace: a question answered with citations from two annual reports, the cited passage highlighted on the PDF page, a task drafted from a document waiting for a manager, the agent drafting nine tasks from a launch plan for approval, the workspace graph, a manager's, member's and viewer's views, and a planted instruction left out of the prompt." src="docs/demo.webp">

## The problem it solves

Teams keep what they know in documents: reports, policies, contracts, plans and minutes. Finding one fact in them is slow, and acting on what they say depends on someone reading closely and remembering to follow up. AI assistants promise to help, but they fall short in four ways that matter when the answer has consequences:

| The gap | Why it matters | How Varro closes it |
|---|---|---|
| **Answers can't be checked** | An assistant answers fluently whether or not the documents support it, so you either trust it blindly or re-read the source. | Every factual sentence cites a numbered passage, and one click opens the page with that passage highlighted. When the documents don't cover a question, it says so instead of guessing. |
| **Private files leave your control** | Most tools upload whole documents to a third-party service, which contracts, internal plans and personal data often can't allow. | Reading, indexing, search and storage run on your own computer. Only the question and the few passages needed to answer it reach the answering model. |
| **Documents can steer the AI** | A sentence hidden in a file, such as "ignore your instructions and…", can change what an assistant says, and what it does once it can take actions. | Sentences that address an AI are detected, even when disguised, and left out of the prompt; everything else from a document is treated as content, never as instructions. |
| **Answers stop short of action** | The deadlines and duties a document sets still have to be found and assigned by hand, while an assistant that acts on its own makes changes nobody approved. | Actions in a document become draft tasks, each quoting the sentence it came from, and nothing the agent drafts or proposes takes effect until a person approves it. |

On the evaluation set, every answerable question was answered with each needed page cited (51 of 51), every unanswerable one was refused (11 of 11), and all 34 planted prompt-injection attacks were resisted; the [Results](#results) table has the full picture and its limits.

## Features

- **Answers you can check.** Every factual sentence cites a numbered passage, and a citation opens the PDF page with the passage highlighted. When the documents don't cover a question, the answer says so instead of guessing.
- **Hybrid retrieval.** Keyword (BM25) and semantic (BGE) search are fused, then a cross-encoder reranks the candidates. Multi-part and follow-up questions are planned into standalone searches first.
- **Agent mode.** An agent that searches documents or reads them through, compares them in tables, works out sums and dates exactly, follows the workspace graph and recalls your earlier conversations. It drafts tasks and proposes changes, checklists, comments and notes; nothing takes effect until a person approves it.
- **Tasks from documents.** The actions a document gives become draft tasks, each with its owner, deadline and the sentence it came from. Nothing reaches the board until it is reviewed, and a new version of a document flags the tasks whose source changed.
- **Prompt-injection defence.** Sentences that address an AI are detected (through look-alike letters, invisible characters or base64), left out of the prompt and flagged; everything else from a document is fenced as content, never instructions.
- **Many formats.** PDF, Word, plain text, Markdown and web pages, with optional local OCR for scanned PDFs. Documents are read in the background.
- **Private by design.** Documents, embeddings, search and storage stay on your machine; only the question and the passages it needs go to the answering model, GPT-OSS on Groq, under [Groq's own terms](https://groq.com/terms-of-use/).
- **Usage you can see.** Each answer shows the tokens it used, and Settings shows each day's total, so you can watch your Groq quota.
- **Also included:** a graph of documents, conversations and tasks; saved, searchable conversations; summaries and suggested questions for each document; verified backups taken while the app runs; your own data as one download.

## How it works

<img alt="Varro RAG system architecture: the browser talks to a FastAPI app on your machine. Inside it, documents flow left to right through validate, extract, chunk and embed; questions through plan, hybrid search, rerank and guard to the answering model, the only part outside your machine; and the agent drafts tasks for review. Below, the app writes to and reads from local storage: SQLite, the original files and an embedded Chroma store." src="docs/architecture.png">

A question is planned into standalone queries, searched by keywords and embeddings together, reranked, screened for planted instructions and answered from the best passages; stored text offsets map each citation to a highlight on the original page. Everything except the answering model runs locally. The design choices, and the measurements behind them, are in [docs/DECISIONS.md](docs/DECISIONS.md).

## Results

Measured on a fictional company's documents written for testing; every table and how each run works are in [docs/EVALUATION.md](docs/EVALUATION.md).

| What | Result |
|---|---|
| Right passage in the top 2 / top 4 (hybrid + reranker) | 0.93 / 0.99 |
| Answerable questions answered with every needed page cited | 51 / 51 |
| Unanswerable questions refused | 11 / 11 |
| Expected tasks found when drafting from documents (two runs) | 18 / 18 and 17 / 18 |
| Planted prompt-injection attacks resisted | 34 / 34 |
| Agent mode: hidden instructions acted on, guardrail breaches | 0 / 8, none |
| Search at 3,000 documents: median time, fact found | 162 ms, 40 / 40 |

The sets are small and self-written, so they work as regression checks rather than benchmarks.

## Quick start

You need a Groq API key, free at [console.groq.com](https://console.groq.com).

### With Docker

```bash
git clone https://github.com/esammostafa9-cloud/Varro-Agentic-RAG-System2.git
cd Varro-Agentic-RAG-System2
docker compose up --build
```

Open <http://localhost:8000> and paste your Groq key in **Settings**, or put `GROQ_API_KEY=...` in a `.env` file next to `docker-compose.yml` before starting. Documents and the downloaded models live in Docker volumes, so they survive restarts and upgrades. The image runs on the CPU and includes OCR for scanned PDFs.

### With Python

Requires Python 3.11 or newer.

```bash
git clone https://github.com/esammostafa9-cloud/Varro-Agentic-RAG-System2.git
cd Varro-Agentic-RAG-System2
python -m venv .venv
```

Activate the environment (`.venv\Scripts\activate` on Windows, `source .venv/bin/activate` on macOS and Linux), then:

```bash
pip install -r requirements.txt
cp .env.example .env
```

Set `GROQ_API_KEY` in `.env` (or paste it in Settings later), then start the app and open <http://localhost:8000>:

```bash
uvicorn app.main:app
```

The first start downloads the embedding model (about 130 MB) and the reranker (about 1.1 GB). There is no account to create, and everything you add stays in `data/` on your computer. For scanned PDFs, also run `pip install -r requirements-ocr.txt`. If something goes wrong, see [Troubleshooting](docs/OPERATIONS.md#troubleshooting).

## Team mode

By default Varro is for one person: there is no sign-in, and whoever opens it is its admin. Team mode adds personal accounts, so several people can share one Varro, each with a role in each workspace and their own private conversations.

### Turn it on

1. Add `TEAM_MODE=true` to `.env` (with Docker, the same `.env` next to `docker-compose.yml`).
2. Restart Varro. On the first start the console prints a one-time setup code:

   ```text
   Team mode needs a first admin. Setup code: 1a2b3c-4d5e6f-7a8b9c
   ```

   With Docker, read it with `docker compose logs varro`.
3. Open <http://localhost:8000>, enter the code, and create the admin account (a password of 10 characters or more).

Documents, conversations and tasks you made before stay where they were and now belong to the admin.

### Add people

As the admin, open **People and access** in the sidebar:

1. **Add a person** with their name, email and role (member or admin), and a first password. Share it with them privately; they choose their own at their first sign-in.
2. Under **Workspace access**, pick a workspace and give each person a role in it:

| Role | What they can do |
|---|---|
| Viewer | Read the documents and tasks, and ask questions. Changes nothing. |
| Member | Everything a viewer can, plus their own tasks and the tasks given to them. |
| Manager | Everything a member can, plus assigning tasks and approving drafts for others. |
| Admin | Manages people, models and settings, and can open every workspace. |

### What it protects

- **Conversations are private** to the person who started them. An admin's export of someone's data leaves them out while that person can still download them themselves.
- **The agent never has more rights than the person using it.** A member's agent drafts only for them, and a viewer's agent only reads.
- **Sign-in is guarded.** Repeated wrong passwords lock that email for 15 minutes; sessions end after 14 days unused (90 at most), and at once when a password is changed or reset or an admin demotes or deactivates the person; every sign-in and change is in the **Activity** log.
- **Data rights.** Everyone can download their own data from Settings, and an admin can deactivate a person and then erase them for good.

### Sharing it beyond this computer

Varro only answers on this computer until you say otherwise. To let colleagues reach it, run it on a server behind HTTPS with `ENVIRONMENT=production`, which requires an `APP_PASSWORD` in front of everything, and add the server's name to `ALLOWED_HOSTS` and `ALLOWED_ORIGINS`. [DEPLOY.md](DEPLOY.md) lists what must be in place. If team mode is later switched off on a server that other machines can reach and no `APP_PASSWORD` is set, Varro refuses to start rather than open the team's data to everyone.

## Try the demo

```bash
python -m app.demo
```

This builds a ready-made team workspace in its own folder (`demo-data/`, never `data/`) and starts it in team mode: the sample documents with summaries, a task board with a task in every state, and four accounts that share the password `varro-demo-2026` (for local use only):

| Account | Email | Role |
|---|---|---|
| Ada Admin | `admin@demo.example` | admin |
| Maya Manager | `maya@demo.example` | manager: reviews drafts, assigns tasks |
| Sam Member | `sam@demo.example` | member: works on the tasks in their inbox |
| Vic Viewer | `vic@demo.example` | viewer: reads and asks, changes nothing |

Answers still need a Groq key. `--reset` starts the demo over; `--port 8040` runs it beside your own copy.

## Tech stack

| Layer | Choice |
|---|---|
| Backend | FastAPI, LangChain 1.x, SQLite |
| Retrieval | Chroma (embedded), BM25, `BAAI/bge-small-en-v1.5` embeddings, `BAAI/bge-reranker-base` cross-encoder |
| Answering model | GPT-OSS 120B on Groq (20B as a faster option) |
| Documents | pypdfium2, docx2txt, optional RapidOCR |
| Frontend | Vanilla HTML, CSS and ES modules, no build step |
| Quality | pytest (about 90% coverage), Node tests, ruff, pip-audit, gitleaks, an evaluation harness in `eval/` |

## Project structure

```text
app/
  main.py          app factory and security middleware (headers, trusted hosts, same-origin writes)
  rag/             ingestion, PDF and OCR, embeddings, vector and keyword search, reranking, prompts, models
  services/        answers, documents, tasks, accounts and access, the workspace graph, usage
  services/agent/  Agent mode: tools, the tool loop, drafts and proposals, and its limits
  routes/          the HTTP API
static/            the web app: HTML, CSS and ES modules, with fonts and Swagger UI bundled
eval/              evaluation dataset, metrics, runners and results
samples/           fictional sample documents and the script that regenerates them
tests/             pytest suites with fake models, and Node tests for the frontend
docs/              decisions, evaluation, configuration, operations and the API
```

## Development

```bash
pip install -r requirements-dev.txt
ruff check . && ruff format --check .
pytest --cov
node --test tests/js/*.test.mjs
```

The tests use a scripted model and fake embeddings, so they run offline and spend no quota. Conventions and the pull-request checklist are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Documentation

- [Decisions](docs/DECISIONS.md): the main design choices and why
- [Evaluation](docs/EVALUATION.md): how each part is measured, with every result
- [Configuration](docs/CONFIGURATION.md): environment variables
- [Operations](docs/OPERATIONS.md): troubleshooting, backups, development and running the evaluations
- [API](docs/API.md): HTTP endpoints (also served as interactive docs by the running app)
- [Security](SECURITY.md): how the app is protected, the latest security review, and how to report a vulnerability
- [Running on a server](DEPLOY.md): what must be in place before others can reach it
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md), [getting help](SUPPORT.md) and the [code of conduct](CODE_OF_CONDUCT.md)

## How it was built

I designed and built Varro RAG with AI-assisted development (Claude Code). I set the requirements and the architecture, made the design decisions, reviewed the changes, and designed the evaluations that decided what stayed and what was rolled back.

## Limitations

- English only for now: the embedding model, the injection checks and every evaluation are English.
- The injection checks are pattern matching: they catch 31 of the 34 planted attacks, and the model resisted the other three in testing. A new rewording could still get past them, so people review every draft and proposal.
- Built for one machine: one server process and SQLite, with no load testing for many concurrent users.
- On Groq's free tier (200,000 tokens a day), heavy Agent mode use can reach the daily or per-minute limit; a paid tier removes it.
- Team mode trusts the people in it: requests are rate-limited, but there is no per-person cap on stored files or on model use, so one member could fill the disk or use up the shared model quota.
- OCR reads clean, noisy, compressed and slightly skewed scans at 0.92 to 0.98 of words right, but a clearly crooked page comes back out of order and an out-of-focus one is not read ([measurements](docs/EVALUATION.md#scanned-pages-ocr)).

## Future work

- **Graph-aware search.** When the agent finds a passage, also check the documents most closely related to it, so the workspace graph improves every answer.
- **Local models through Ollama.** The provider is in the code and listed in Settings as currently unavailable; it will be offered once it has been evaluated.
- **Languages other than English.** This needs a multilingual embedding model, injection checks for each language, and every document indexed again.
- **A larger, independent evaluation set,** with real documents rather than ones written for testing, and every evaluation repeated three times with the worst run reported.
- **Load testing.** Measure how many people can ask questions, run Agent mode and upload at once on one server.
- **Team mode quotas.** A per-person cap on stored files and on daily model use, and a check against well-known breached passwords.
- **Hosted deployment.** A one-click way to run Varro on a cloud host with a persistent disk.
- **A smaller Docker image** (about 3.2 GB today, mostly PyTorch and the OCR libraries).

## License

MIT, see [LICENSE](LICENSE). Bundled: Swagger UI (Apache 2.0) and the IBM Plex typeface (SIL Open Font License, [static/fonts/LICENSE.txt](static/fonts/LICENSE.txt)). Downloaded at first start, under their own licences: the `BAAI/bge-small-en-v1.5` and `BAAI/bge-reranker-base` models (MIT). The sample documents describe fictional companies; any resemblance to real ones is coincidental.
