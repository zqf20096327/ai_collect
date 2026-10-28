# Support Triage Agent

> A terminal-based AI agent that triages real support tickets across three very
> different worlds — **HackerRank**, **Claude**, and **Visa** — answering from a
> grounded support corpus or escalating to a human when it shouldn't guess.

🏆 **1st place — [HackerRank Orchestrate](https://www.hackerrank.com/contests/hackerrank-orchestrate-may26/challenges/support-agent/leaderboard) (May 2026).**
Out of **12,885** registrations across ~50 countries, 2,002 shipped an agent and
1,349 defended it to an AI judge. This one finished #1.

📝 **The full story:** [How I won HackerRank Orchestrate](https://saai.syvendra.com/myspace/hackerrank-orchestrate)
— the thinking behind the design, the prompt-injection ticket, and what it was
like being interviewed by an AI.

![The support triage agent running in its terminal UI](https://res.cloudinary.com/dzjalh3mb/image/upload/v1779684601/Screenshot_2026-05-25_at_10.18.57_endoay.png)

## The problem

Read a customer support ticket, figure out what the user actually wants, then
either **answer it** — grounded _only_ in the provided corpus, with a citation to
the exact article — or **escalate** it to a human. No live internet. No invented
policies. Tickets span three unrelated domains and arrive in multiple languages,
some carrying prompt-injection attempts.

## Design philosophy: one agent, one tool

The instinct is to over-build: three agents (one per company), a router, a
separate injection model, a fistful of search tools. I went the other way.

> Reach for a multi-agent system only when a dire need forces you to. A single,
> well-built agent is far more powerful than people give it credit for.

So: **one agent, one tool.** The tool is a read-only window into the corpus with
three modes, and the agent decides which to use, per call:

- **`search`** — hybrid semantic + keyword retrieval over the docs
- **`read`** — pull a specific article in full (and the _only_ thing that earns a citation)
- **`grep`** — pin down an exact token (error code, order ID, phone number) that fuzzy matching would lose

Search to find, read to be sure, grep to nail a literal — the same three moves a
human support rep makes in the help center.

## How it works

```
ticket
  │
  ├─▶ pre-LLM short-circuit ── pleasantries · injection · off-topic · empty
  │       └─ Haiku 4.5 tags product_area, skips the expensive model
  │
  ├─▶ agent (Claude Sonnet 4.6) ── search → read → reply, with citations
  │       └─ hybrid retrieval: BM25 + dense (RRF) → Cohere rerank
  │
  └─▶ guardrails ── citation guard · escalation trim · "when in doubt, escalate"
          └─ structured SupportTicketDecision → output.csv
```

- **Hybrid retrieval.** BM25 (exact words) + dense vectors (meaning) fused with
  Reciprocal Rank Fusion, then reranked with Cohere — so the best hit floats to
  the top regardless of how the ticket is phrased. LanceDB stores it locally;
  chunking is deterministic, so the same ticket gives the same answer every run.
- **Prompt injection, handled before the model.** Middleware reads each ticket
  first; if it smells like someone fishing for the system prompt or internal
  rules, it refuses there and never calls the model. Multilingual on purpose —
  the attempts weren't going to stay in English.
- **Citations you can check.** A citation only counts if the agent actually
  _opened_ that file during the turn. Try to answer without reading anything, and
  a post-hoc guard turns the reply into an escalation.
- **Don't pay a genius to say "you're welcome."** Cheap rules plus a fast Haiku
  call dispatch the trivial tickets; Sonnet only wakes up for the ones that need
  thinking.
- **When in doubt, escalate.** A stolen card, a full outage, a refund request,
  anything the corpus can't answer safely — the agent surfaces what it can (the
  right hotline, the status page) and routes the rest to a human. A confident
  wrong answer is worse than an honest "let me get someone."

## Quickstart

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r code/requirements.txt
cp .env.example .env          # add ANTHROPIC_API_KEY, OPENAI_API_KEY, COHERE_API_KEY

python code/main.py --build-index   # embed the corpus → LanceDB (one-time, ~30s)
python code/main.py --run           # triage all 29 tickets → support_tickets/output.csv
python code/main.py --tui           # or chat with it interactively
```

Full setup, environment variables, and the eval harness live in
[`code/README.md`](./code/README.md).

## Repository layout

```
code/                 the agent (entry point: main.py)
  agent/              builder, prompts, classifier, safety middleware
  retrieval/          the support_kb tool: hybrid search, reader, grep, filters
  ingest/             corpus parsing, chunking, index builder
  runner/             pipeline, CSV I/O, sample eval
  tui/                Textual terminal UI
data/                 local support corpus — hackerrank / claude / visa  (provided)
support_tickets/      input tickets + the agent's output.csv
problem_statement.md  the original task spec
```

## Tech

Claude Sonnet 4.6 (agent) + Haiku 4.5 (classifier) · LangChain `create_agent` ·
OpenAI `text-embedding-3-large` · Cohere `rerank-v3.5` · LanceDB · Textual.
Keys are read from environment variables only — nothing is hardcoded.
