# synadia-agents-labs

Hands-on, runnable examples for the **Synadia Agent Protocol for NATS** — learn
the SDKs by reading and running small, self-contained programs.

An **agent** is a service on NATS that answers prompts; a **client** discovers
and prompts agents; replies **stream** back over NATS. This repo covers both
sides — from a five-line echo agent to LLM agents that **call tools**,
**remember** things in JetStream KV, and reach **sensors across NATS domains**.

Everything runs on your machine, in **TypeScript and Python**. LLM examples talk to a local
[Ollama](https://ollama.com) **or** to [OpenRouter](https://openrouter.ai) with
an API key — *same code, one env var*. No cloud required, though it all works
against NGS / Synadia Cloud too.

**Read it, run it, tweak it.** Every file is heavily commented, and every folder
is self-contained — its own dependencies, its own README with a *How it works*
walkthrough. Copy one folder out of the repo and it still runs.

## Quickstart — an agent in 60 seconds

You need **Node.js 20+** (or Bun) and a local
**[nats-server](https://docs.nats.io/running-a-nats-server/introduction/installation)**
— that's all for the first example. Two terminals:

```sh
# terminal 1 — start the echo agent
cd typescript/agent/01-echo      && npm install && npm start

# terminal 2 — discover it on the bus
cd typescript/client/01-discover && npm install && npm start   # → finds echo/<you>/main
```

That's the whole pattern, everywhere: each example is one folder,
`npm install && npm start`, and agents pair with clients across two terminals —
any client works against any agent.

<details>
<summary><b>🐍 Python instead?</b></summary>

The Python examples run with [uv](https://docs.astral.sh/uv/), which builds each
folder's venv automatically — no install step:

```sh
cd python/agent/01-echo      && uv run python agent.py    # terminal 1
cd python/client/01-discover && uv run python client.py   # terminal 2
```

</details>

<details>
<summary><b>📦 Zero setup? Use the dev container.</b></summary>

[`infra/`](infra/README.md) ships a Docker dev container with the whole
toolchain — Node, Bun, Python, uv, Go, a NATS server, the `nats` CLI. It
**mounts your checkout**, so you edit locally in your editor of choice and run
inside the container — one click in VS Code, too.

</details>

<details>
<summary><b>☁️ Remote or cloud NATS?</b></summary>

Every example resolves its connection the same way: `NATS_CONTEXT` (a named
[NATS CLI context](https://docs.nats.io/using-nats/nats-tools/nats_cli/nats_contexts),
credentials included) → `NATS_URL` → `nats://127.0.0.1:4222`. Set one env var
and any example talks to your server — see
[Environment variables](#environment-variables).

</details>

## Pick your path

| You want… | Go to |
|---|---|
| 🎓 **A guided course** — short lab sheets, for a live workshop or self-study | [`labs/`](labs/) — labs 00 → 09 |
| 📚 **Self-paced examples** — numbered folders, each adds exactly one idea | [`typescript/`](typescript/) · [`python/`](python/) — start at `agent/01-echo`, tables [below](#whats-inside) |
| 🛠️ **Bigger demos** — tools, persistent memory, humans-in-the-loop, multi-agent | [`projects/`](projects/) — trailers below |

## What's inside

Two sides of the protocol — **clients** (callers) and **agents** (hosts) — plus,
inside the projects, **responders**: ordinary NATS programs in any language that
back agent tools. Difficulty hints: **beginner** · **intermediate** ·
**advanced**. The prompts and answers quoted below are **real**, captured
running these examples against Ollama.

### 🧑‍💻 Client examples — the caller side

[`typescript/client/`](typescript/client/) · [`python/client/`](python/client/)
— the same small numbered steps in both languages.

| # | Example | Level | What it does |
|---|---------|-------|--------------|
| 01 | **discover** | beginner | list every agent on the bus and the metadata it advertises |
| 02 | **prompt-text** | beginner | send a prompt, stream the reply token by token |
| 03 | **prompt-attachment** | intermediate | send a file with a prompt; the SDK enforces `max_payload` / `attachments_ok` *before* any bytes leave |
| 04 | **query-reply** | intermediate | answer an agent's clarifying question mid-stream |
| 05 | **liveness** | intermediate | watch agents' heartbeats and online/offline status |
| 06 | **chat** | intermediate | an interactive multi-turn REPL — string prompts into a conversation |

*Together these are the whole caller API: discover → prompt → attach → answer
queries → track liveness → chat.*

### 🤖 Agent examples — the host side

[`typescript/agent/`](typescript/agent/) · [`python/agent/`](python/agent/) —
each example is the one before it, plus a little more.

| # | Example | Level | What it does |
|---|---------|-------|--------------|
| 01 | **echo** | beginner | the smallest possible agent — replies `echo: <your text>` |
| 02 | **llm-ollama** | beginner | stream a **local** model's answer (Ollama) |
| 03 | **llm-openrouter** | beginner | stream a **hosted** model's answer (OpenRouter) |
| 04 | **llm-combined** | intermediate | auto-pick Ollama **or** OpenRouter — the reusable base later agents build on |
| 05 | **system-prompt** | beginner | give the agent a **persona** — edit one string, get a pirate *(TS only for now)* |
| 06 | **chat-agent** | intermediate | the conversation **accumulates** — multi-turn memory in a few lines *(TS only for now)* |
| — | **reference-agent** | beginner | the SDK's own spec-compliant agent, ready to run as a target |

*The lesson hiding in this sequence: the **shape never changes** — an agent is
just a function from a prompt to a streamed reply (`onPrompt`); only the body
differs. `04-llm-combined` factors model access into `llm.ts` (`llm.py` in
Python), which the tool-calling agents then **copy and extend**.*

> The `02`–`06` agents need a model: a local [Ollama](https://ollama.com)
> **or** an `OPENROUTER_API_KEY`. `04-llm-combined` auto-selects (key present →
> OpenRouter, else Ollama) and logs the choice.

### 🛠️ Projects — where it comes together

Bigger, self-contained demos under [`projects/`](projects/). Each project's
README tells the full story — these are the trailers:

**[tool-calling](projects/tool-calling/)** · intermediate → advanced · TS + Python
— **the heart of the repo.** An agent gets **tools**; each tool's whole body is
a single `nc.request(subject)`, answered by **polyglot responders**
(TypeScript · Go · Python — swap the language, the agent never changes a line;
start several and they form a load-balanced **fleet** via queue groups). Four
agents, one progression: one tool → the model **chooses** among four →
multi-step **chains** → **persistent memory** in a JetStream KV bucket that
survives restarts.

> *"How much warmer is Berlin than Reykjavík?"* → `temperature`(Berlin) = 19 °C,
> `temperature`(Reykjavík) = 4 °C, `calculate`(19−4) →
> **"Berlin is about 15 °C warmer."**

**[human-tool](projects/human-tool/)** · intermediate · TS — **the tool is a
person.** The agent's `ask_expert` tool publishes to `tools.expert.<owner>`,
and a human answers with `nats reply`, live from a terminal.

> *"Ask the expert: should we take a coffee break?"* → *(a human types)* →
> **"The expert says: absolutely — they've earned it."**

**[crowd-poll](projects/crowd-poll/)** · intermediate · TS — **the tool is the
whole room.** One `ask_the_room` call scatter-gathers (`requestMany`) every
reply on `room.poll` within 10 s; the LLM turns a pile of one-liners into a
summary with a winner. Joining the poll is one command:
`nats reply 'room.poll' 'tabs, obviously'`.

**[agent-of-agents](projects/agent-of-agents/)** · advanced · TS — **agents
composing agents.** A reporter whose tools are the caller SDK itself
(`list_agents` + `ask_agent`). Ask it to interview the room: it discovers
whoever is online, questions a few, and files a report quoting them by name —
no framework required.

**[edge-sensor](projects/edge-sensor/)** · advanced · TS + Go — **a tool call
that crosses two NATS systems.** An agent on a *cloud* NATS reads a sensor on a
separate *edge* NATS through a Go bridge. Your existing edge infrastructure
becomes an agent capability — the agent just calls a subject.

> *"What's the chip temperature, and is it overheating?"* →
> **"It's about 45 °C — below the 80 °C limit, so it isn't overheating."**

### 🎓 Labs — the guided track

[`labs/`](labs/) sequences everything above into a course: ten short lab sheets
(`00-setup` → `09-agent-of-agents`), each a handful of paste-ready commands
with the *why* attached. Built for a live workshop (secrets arrive via the
workshop chat, never the repo) and equally usable for self-study — every lab
has a *Self-study* note.

## Things to try

These aren't just demos — they're starting points:

- **Swap a responder's language** — run the Go calculator instead of the
  TypeScript one; the agent can't tell the difference.
- **Start a fleet** — run two or three calculator responders at once; they
  load-balance with zero config. Kill one mid-stream — nothing breaks.
- **Add your own tool** — copy a responder, then give an agent a new tool whose
  body is a single `nc.request`.
- **Change the model** — set `OPENROUTER_API_KEY` and the same agent talks to a
  hosted model instead of Ollama.
- **Watch the bus** — `nats micro ls` while a tool agent is up, or
  `nats kv watch agent_memory` while one remembers.

Every example's README has a **"How it works"** section that walks through the
code.

---

## Reference

### Prerequisites

The [quickstart](#quickstart--an-agent-in-60-seconds) needs only Node and a
`nats-server`; here is everything, by tier:

| You're running… | You need |
|---|---|
| TypeScript examples | **Node.js 20+** (scripts run via [tsx](https://github.com/privatenumber/tsx)) — **Bun** works too |
| Python examples | **[uv](https://docs.astral.sh/uv/)** — builds each folder's venv automatically |
| Any example | A **NATS server** — local `nats-server`, a CLI context, or a URL (NGS / Synadia Cloud); the memory example needs JetStream (`nats-server -js`) |
| LLM examples (agents `02`+, all projects) | A local **[Ollama](https://ollama.com)** (use a tool-capable model like `llama3.1:8b` for tool-calling) **or** an **`OPENROUTER_API_KEY`** |
| Poking around *(optional)* | The **[`nats` CLI](https://github.com/nats-io/natscli)** — inspect agents, answer as a human tool, watch KV buckets |

Or skip all of it with the [dev container](infra/README.md), which bundles the
whole toolchain.

### Environment variables

Configuration is by environment variable; **nothing is required** — the
defaults connect to a local server. Our connection and agent variables share a
**`NATS_` prefix**; third-party tool variables (Ollama, OpenRouter) keep their
conventional, un-prefixed names so they interoperate with whatever you already
have configured. Each example's README lists the subset it reads.

**Connection** — every example:

| Variable       | Default                 | Purpose |
| -------------- | ----------------------- | ------- |
| `NATS_CONTEXT` | _(unset)_               | Connect via a named [NATS CLI context](https://docs.nats.io/using-nats/nats-tools/nats_cli/nats_contexts). Takes precedence when set. |
| `NATS_URL`     | `nats://127.0.0.1:4222` | Connect via a raw URL; credentials in the userinfo (`nats://user:pass@host`) are honored. Used when `NATS_CONTEXT` is unset. |

**Agent identity & heartbeat** — agent examples. The subject is
`agents.prompt.<agent>.<owner>.<name>`:

| Variable                        | Default                    | Purpose |
| ------------------------------- | -------------------------- | ------- |
| `NATS_AGENT_OWNER`              | your `$USER` (else `anon`) | The `owner` token — set it so several people running the same example against one server don't collide. |
| `NATS_AGENT_NAME`               | `main`                     | The instance `name` token — give each instance a different name to run several at once. |
| `NATS_AGENT_HEARTBEAT_INTERVAL` | `30`                       | Heartbeat cadence in **seconds** (the SDK/spec default is 30). Lower it (e.g. `2`) for a livelier `05-liveness` demo. |

The `<agent>` token (e.g. `echo`) is fixed per example; it's what the example *is*.

**LLM backend** — the LLM-powered agent examples:

| Variable             | Default                  | Purpose |
| -------------------- | ------------------------ | ------- |
| `OLLAMA_URL`         | `http://localhost:11434` | Base URL of a local [Ollama](https://ollama.com). |
| `OLLAMA_MODEL`       | _(per example)_          | Ollama model name (use a tool-capable model — e.g. `llama3.1:8b`, `gpt-oss` — for tool examples). |
| `OPENROUTER_API_KEY` | _(unset)_                | API key for [OpenRouter](https://openrouter.ai) — required by the OpenRouter examples. |
| `OPENROUTER_MODEL`   | _(per example)_          | OpenRouter model name. |

### Conventions (read once)

1. **Every example is self-contained.** Its own `package.json` /
   `pyproject.toml`, its own README, all of its code in the folder — copy one
   out and it still runs. A little duplication is the price of clarity.
2. **Pinned, published SDKs.** Examples depend on `@synadia-ai/agents` & friends
   from npm (TS) and `synadia-ai-agents` & friends from PyPI (Python) — never a
   path back to the SDK source. (Current pins: npm `^0.5.2`; PyPI
   `synadia-ai-agents>=0.7`, `synadia-ai-agent-service>=0.4`.)
3. **Role-based filenames.** `agent.{ts,py}` (a host), `client.{ts,py}` (a
   caller), `responder.{ts,py}` (a plain-NATS tool backend), `llm.{ts,py}` (the
   model client).
4. **Reuse is copy-forward.** A later example carries its *own copy* of a shared
   file (e.g. `llm.ts`) with a note pointing back — locality beats DRY in a
   teaching repo.
5. **Clients and agents are decoupled.** Any client works against any agent —
   that's what discovery is for.
6. **Uniform connection resolution**, everywhere: `NATS_CONTEXT` → `NATS_URL` →
   `nats://127.0.0.1:4222`.

### Reference Repositories

- **The SDKs** — [`synadia-ai/synadia-agents`](https://github.com/synadia-ai/synadia-agents):
  the source of the published packages these examples depend on, and of the
  agent plugins.
- **The protocol spec** — [`synadia-ai/synadia-agent-sdk-docs`](https://github.com/synadia-ai/synadia-agent-sdk-docs):
  the source of truth for wire shape; these labs show how to *use* it.

## License

[Apache-2.0](LICENSE).
