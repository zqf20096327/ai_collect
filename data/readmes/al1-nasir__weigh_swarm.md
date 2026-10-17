<h1 align="center">Weigh Swarm</h1>

<p align="center"><strong>Evidence-first research RAG with a Laya decision engine.</strong></p>

Turn a research question or supplied papers into a **cited, inspectable draft**.
LLMs plan the investigation, extract source passages, and write the synthesis.
Laya handles bounded decisions across relevance, claims, evidence, methodology,
contradictions, and answer verification.

<h2 align="center">See it in action</h2>

[![Inside the engine: a recorded two-paper research run with real LLM and Laya activity](demo/remotion/public/engine-top.png)](demo/remotion/out/weigh-swarm-two-paper-demo.mp4)

<p align="center"><a href="demo/remotion/out/weigh-swarm-two-paper-demo.mp4"><strong>Watch the 66-second demo</strong></a></p>

<p align="center"><strong>2 PDFs · 28 source-aligned claims · 7 evidence passages<br>107 Laya batches · 322 bounded questions</strong></p>

This recorded run uses Gemini and Laya. The video combines real product captures
with animation of saved run artifacts.

<h2 align="center">What you can do</h2>

- **Start with a question or PDFs.** Search Semantic Scholar, OpenAlex, arXiv,
  and PubMed, or investigate one or two papers you already have.
- **Follow the evidence.** Explore paper, claim, evidence, and methodology
  nodes; inspect exact excerpts and available page/section locations.
- **Inspect Laya decisions.** Open **Inside the engine** to see task lanes,
  recorded batches, model calls, token usage, and stage replay.
- **Review the answer.** Follow citations to sources and inspect verification
  feedback before accepting or revising a draft.

<h3 align="center">Explore the evidence network</h3>

![Actual evidence network connecting the two papers, their claims, and source passages](demo/remotion/public/engine-graph.png)

The graph represents stored research artifacts. Selecting a node opens its
source details and relationships.

<h3 align="center">Read a draft with citations</h3>

![Recorded answer draft with clickable citations and evidence coverage](demo/remotion/public/result-answer.png)

This recorded draft is **unverified**. Its source links make review possible;
verification feedback identifies statements that need repair.

<h2 align="center">How it works</h2>

<h3 align="center">1. Discover papers and analyze their sources</h3>

![Research workspace, planning, search, paper selection, and Laya analysis swarms](Weigh-Swarm-Architecture-Page-1.png)

<h3 align="center">2. Compare evidence and draft an answer</h3>

![Cross-paper analysis, ResearchState, synthesis, verification, human review, and engine inspection](Weigh-Swarm-Architecture-Page-2.png)

**Stack:** React + Vite · FastAPI · Celery + Redis · PostgreSQL + pgvector ·
Neo4j · GROBID · Laya · replaceable LLM providers.

<h2 align="center">Run locally</h2>

You need **Docker with Compose**. For live research, configure an LLM provider
in `.env`; supported adapters include Gemini, Groq, OpenAI, OpenRouter, and
other OpenAI-compatible endpoints.

```bash
cp .env.example .env
# Configure your provider and model in .env, then start:
docker compose up --build
```

Open `http://localhost:5173` after the services start. Choose **Start with PDFs**,
enter your question and the exact paper titles, and upload one or two PDFs.
Follow the run, open **Inside the engine**, then inspect the draft and citations.
Literature search is also available.

The default configuration uses mock models and produces no source-grounded
answer. The setup guide below includes live provider configuration and opt-ins
for real, experimental Laya decisions. The Compose worker includes CPU Laya;
its checkpoint loads on first use. Keep credentials in the ignored `.env` file.

<h2 align="center">Current scope</h2>

A working research prototype with a recorded end-to-end Gemini + Laya run.
The demo ends with a partial, unverified draft. Laya's scientific judgments
are uncalibrated; answer quality and latency gains still need evaluation.
Groq and Gemini development profiles keep automatic runs small for free-tier
budgets.

<h2 align="center">Documentation</h2>

<p align="center"><a href="docs/LOCAL_DEVELOPMENT.md">Setup and configuration</a> · <a href="ARCHITECTURE.md">Architecture</a> · <a href="CONTRIBUTING.md">Contributing</a></p>
