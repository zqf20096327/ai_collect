<p align="center">
  <a href="https://agentic-ai-from-scratch.vercel.app/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/readme/header-dark.svg">
      <img src="assets/readme/header-light.svg" alt="Agentic AI from Scratch" width="840">
    </picture>
  </a>
</p>

<p align="center">
  Build AI agents from a raw while-loop and an HTTP call, before a single framework gets imported.<br>
  Tools, memory, planning, MCP, multi-agent systems, evals, and safety, written by hand and tested.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/ramakrushnamohapatra"><img src="assets/readme/icons/linkedin.svg" width="16" height="16" alt="LinkedIn"> ramakrushnamohapatra</a> &nbsp;·&nbsp;
  <a href="https://www.instagram.com/techwith.ram/"><img src="assets/readme/icons/instagram.svg" width="16" height="16" alt="Instagram"> techwith.ram</a> &nbsp;·&nbsp;
  <a href="https://x.com/techwith_ram"><img src="assets/readme/icons/x.svg" width="16" height="16" alt="X (Twitter)"> techwith_ram</a>
</p>

<p align="center">
  <a href="https://agentic-ai-from-scratch.vercel.app/"><b>Website</b></a> ·
  <a href="phases/00-setup-and-tooling/01-your-agent-dev-environment/docs/en.md"><b>Start learning</b></a> ·
  <a href="#learning-paths"><b>Choose a path</b></a> ·
  <a href="#contents"><b>Curriculum</b></a> ·
  <a href="ROADMAP.md"><b>Roadmap</b></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-1a1a1a?style=flat-square&labelColor=fafaf5" alt="MIT License"></a>
  <a href="#contents"><img src="https://img.shields.io/badge/phases-16-EC4D36?style=flat-square&labelColor=fafaf5" alt="16 phases"></a>
  <a href="ROADMAP.md"><img src="https://img.shields.io/badge/lessons-163-EC4D36?style=flat-square&labelColor=fafaf5" alt="163 lessons"></a>
  <a href="https://github.com/Ramakm/agentic-ai-from-scratch/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Ramakm/agentic-ai-from-scratch/ci.yml?branch=main&style=flat-square&labelColor=fafaf5&label=tests" alt="Tests"></a>
  <a href="https://github.com/Ramakm/agentic-ai-from-scratch/stargazers"><img src="https://img.shields.io/github/stars/Ramakm/agentic-ai-from-scratch?style=flat-square&labelColor=fafaf5&color=EC4D36" alt="GitHub stars"></a>
</p>

Turn your coding agent into a tutor with one command:

```bash
npx skills add Ramakm/agentic-ai-from-scratch
```

Then, in Claude Code, Codex, Cursor, or any agent that reads `SKILL.md`: **"Use start-building to begin the course."**

---

## Why build agents from scratch

Most agent material is framework tutorials. You can wire a crew of five agents but can't say why the third one loops forever. You can install an MCP server but couldn't write the JSON-RPC message it answers.

This course goes the other way. Every pattern is built by hand first, in plain Python you can read in one sitting:

| You build | Before you use |
|-----------|----------------|
| A tool dispatcher with schema validation | Native function calling, `@function_tool` |
| A ReAct loop in ~120 lines | LangGraph, the OpenAI and Claude Agent SDKs |
| A vector store in ~80 lines | pgvector, Chroma, LlamaIndex |
| An MCP server over stdio | Off-the-shelf MCP servers |
| An orchestrator with parallel workers | CrewAI, AutoGen, LangGraph `Send` |
| An eval harness and trace viewer | LangSmith, Braintrust, OpenTelemetry backends |

When the frameworks show up in Phase 9, you already know what they do under the hood, and when to skip them.

## How every lesson works

Each lesson follows the same four steps:

1. **The problem.** A concrete failure, e.g. *a model only returns text; ask it to book a flight and it describes booking one.*
2. **Build it.** Raw code, no framework, standard library wherever possible.
3. **Use it.** The same idea in the production tools, so you can read what they're doing.
4. **Ship it.** An artifact you keep: a tool, a prompt, an MCP server, or a skill your coding agent can load.

Every live lesson folder has the same shape:

```text
phases/03-the-agent-loop/01-the-agent-loop-in-120-lines/
├── docs/en.md          the lesson
├── code/main.py        runnable, offline by default (scripted model)
├── code/test_main.py   unit tests, run in CI
├── quiz.json           6 questions: pre, check, post
└── outputs/            what you ship: skill-*.md, prompt-*.md
```

Lessons run **offline by default** against a scripted model, so they're deterministic and free. Point them at a real model with two environment variables. Ollama, OpenAI, vLLM, LM Studio and any other OpenAI-compatible server work:

```bash
AGENT_BASE_URL=http://localhost:11434/v1 AGENT_MODEL=llama3.2 python3 code/main.py
```

## Choose how to learn

- **On the website.** Every lesson, with quizzes and progress saved in your browser: **[agentic-ai-from-scratch.vercel.app](https://agentic-ai-from-scratch.vercel.app/)**
- **With your coding agent as tutor.** Install the skills, then:

  | Skill | What it does |
  |-------|--------------|
  | `find-your-level` | 10-question placement quiz that maps you to a starting phase |
  | `start-building` | Interviews you and writes `BUILD.md`, your personal build plan |
  | `build` | Teaches the next lesson section by section, quizzes you, and reviews your code |
  | `check-understanding` | Quizzes you on any phase or lesson |
  | `debug-my-agent` | Reads your agent's trace or error and points to the lesson that fixes it |

- **Locally.** Clone, then run any lesson's code and tests:

  ```bash
  git clone https://github.com/Ramakm/agentic-ai-from-scratch.git
  cd agentic-ai-from-scratch
  python3 phases/00-setup-and-tooling/01-your-agent-dev-environment/code/main.py --ping
  ```

## Learning paths

| Path | For | Phases |
|------|-----|--------|
| **01 · Building single agents** | Your first agent that actually finishes the job | 01 → 06 |
| **02 · Tools, protocols & computer use** | MCP, browser and terminal control, coding agents | 07, 10 |
| **03 · Multi-agent systems** | Orchestrators, handoffs, A2A, frameworks | 08 → 09 |
| **04 · Reliable agents in production** | Evals, tracing, guardrails, durable execution, UX | 11 → 15 |

## Where to start

| If you are… | Start at |
|-------------|----------|
| New to agents | [00.01 Your agent dev environment](phases/00-setup-and-tooling/01-your-agent-dev-environment/docs/en.md) |
| Shipping LLM apps already | [02.02 Tool schemas from first principles](phases/02-tool-use/02-tool-schemas-from-first-principles/docs/en.md) |
| Here to build an agent from scratch | [03.01 The agent loop in 120 lines](phases/03-the-agent-loop/01-the-agent-loop-in-120-lines/docs/en.md) |
| Going multi-agent | [08.02 Orchestrator–worker](phases/08-multi-agent-systems/02-orchestrator-worker/docs/en.md) |

Prerequisites: comfortable Python, and a terminal. No ML background needed.

## Contents

<!-- CONTENTS:START -->
<!-- Generated by scripts/build.mjs. Edit curriculum.json instead. -->

**16 phases · 163 lessons · 137 live · ~127 hours**

<details open>
<summary><b>Phase 00 · Setup & Tooling</b> · 8 lessons · 8 live</summary>

A dev environment, local and hosted models, raw HTTP calls, streaming and tracing, all wired up before writing an agent.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 00.01 | [Your agent dev environment](phases/00-setup-and-tooling/01-your-agent-dev-environment/docs/en.md) | ■ live | 45 min |
| 00.02 | [Python & TypeScript for agents](phases/00-setup-and-tooling/02-python-typescript-for-agents/docs/en.md) | ■ live | 60 min |
| 00.03 | [Running local models with Ollama](phases/00-setup-and-tooling/03-running-local-models-with-ollama/docs/en.md) | ■ live | 40 min |
| 00.04 | [API keys, providers & rate limits](phases/00-setup-and-tooling/04-api-keys-providers-rate-limits/docs/en.md) | ■ live | 30 min |
| 00.05 | [Calling an LLM over raw HTTP](phases/00-setup-and-tooling/05-calling-an-llm-over-raw-http/docs/en.md) | ■ live | 45 min |
| 00.06 | [Streaming responses with SSE](phases/00-setup-and-tooling/06-streaming-responses-with-sse/docs/en.md) | ■ live | 40 min |
| 00.07 | [Tracing from day one](phases/00-setup-and-tooling/07-tracing-from-day-one/docs/en.md) | ■ live | 35 min |
| 00.08 | [Project layout for agent repos](phases/00-setup-and-tooling/08-project-layout-for-agent-repos/docs/en.md) | ■ live | 30 min |

[Phase overview →](phases/00-setup-and-tooling/README.md)

</details>

<details open>
<summary><b>Phase 01 · LLM Foundations for Agents</b> · 10 lessons · 10 live</summary>

What a model actually returns, how context windows fill, and how to force structured, parseable output.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 01.01 | [What an LLM actually returns](phases/01-llm-foundations/01-what-an-llm-actually-returns/docs/en.md) | ■ live | 45 min |
| 01.02 | [Tokens and the context window](phases/01-llm-foundations/02-tokens-and-the-context-window/docs/en.md) | ■ live | 50 min |
| 01.03 | [Sampling: temperature, top-p, determinism](phases/01-llm-foundations/03-sampling-temperature-top-p-determinism/docs/en.md) | ■ live | 40 min |
| 01.04 | [Chat templates and message roles](phases/01-llm-foundations/04-chat-templates-and-message-roles/docs/en.md) | ■ live | 40 min |
| 01.05 | [System prompts as contracts](phases/01-llm-foundations/05-system-prompts-as-contracts/docs/en.md) | ■ live | 35 min |
| 01.06 | [Structured output & JSON mode](phases/01-llm-foundations/06-structured-output-json-mode/docs/en.md) | ■ live | 50 min |
| 01.07 | [Parsing and validating with schemas](phases/01-llm-foundations/07-parsing-and-validating-with-schemas/docs/en.md) | ■ live | 45 min |
| 01.08 | [Token budgets & cost math](phases/01-llm-foundations/08-token-budgets-cost-math/docs/en.md) | ■ live | 35 min |
| 01.09 | [Model selection for agent work](phases/01-llm-foundations/09-model-selection-for-agent-work/docs/en.md) | ■ live | 40 min |
| 01.10 | [Why capable models still fail](phases/01-llm-foundations/10-why-capable-models-still-fail/docs/en.md) | ■ live | 45 min |

[Phase overview →](phases/01-llm-foundations/README.md)

</details>

<details open>
<summary><b>Phase 02 · Tool Use & Function Calling</b> · 11 lessons · 11 live</summary>

Turn text into action. Tool schemas, dispatchers, parallel calls, and errors fed back as observations.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 02.01 | [Text in, text out: the limit](phases/02-tool-use/01-text-in-text-out-the-limit/docs/en.md) | ■ live | 30 min |
| 02.02 | [Tool schemas from first principles](phases/02-tool-use/02-tool-schemas-from-first-principles/docs/en.md) | ■ live | 50 min |
| 02.03 | [Writing a tool dispatcher](phases/02-tool-use/03-writing-a-tool-dispatcher/docs/en.md) | ■ live | 60 min |
| 02.04 | [Parallel tool calls](phases/02-tool-use/04-parallel-tool-calls/docs/en.md) | ■ live | 45 min |
| 02.05 | [Tool errors as observations](phases/02-tool-use/05-tool-errors-as-observations/docs/en.md) | ■ live | 40 min |
| 02.06 | [Designing tools models can use](phases/02-tool-use/06-designing-tools-models-can-use/docs/en.md) | ■ live | 50 min |
| 02.07 | [Idempotency and side effects](phases/02-tool-use/07-idempotency-and-side-effects/docs/en.md) | ■ live | 40 min |
| 02.08 | [Human approval gates](phases/02-tool-use/08-human-approval-gates/docs/en.md) | ■ live | 45 min |
| 02.09 | [Tool results that fit the context](phases/02-tool-use/09-tool-results-that-fit-the-context/docs/en.md) | ■ live | 40 min |
| 02.10 | [Native function calling across providers](phases/02-tool-use/10-native-function-calling-across-providers/docs/en.md) | ■ live | 50 min |
| 02.11 | [Testing tools in isolation](phases/02-tool-use/11-testing-tools-in-isolation/docs/en.md) | ■ live | 40 min |

[Phase overview →](phases/02-tool-use/README.md)

</details>

<details open>
<summary><b>Phase 03 · The Agent Loop</b> · 12 lessons · 12 live</summary>

A while-loop, a model, and a toolbox. ReAct, stop conditions, retries, interrupts, and the loop as a graph.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 03.01 | [The agent loop in 120 lines](phases/03-the-agent-loop/01-the-agent-loop-in-120-lines/docs/en.md) | ■ live | 60 min |
| 03.02 | [ReAct: reason, act, observe](phases/03-the-agent-loop/02-react-reason-act-observe/docs/en.md) | ■ live | 60 min |
| 03.03 | [Stop conditions & max steps](phases/03-the-agent-loop/03-stop-conditions-max-steps/docs/en.md) | ■ live | 35 min |
| 03.04 | [Scratchpads and thought traces](phases/03-the-agent-loop/04-scratchpads-and-thought-traces/docs/en.md) | ■ live | 40 min |
| 03.05 | [Handling malformed actions](phases/03-the-agent-loop/05-handling-malformed-actions/docs/en.md) | ■ live | 40 min |
| 03.06 | [Retries, backoff & recovery](phases/03-the-agent-loop/06-retries-backoff-recovery/docs/en.md) | ■ live | 45 min |
| 03.07 | [Streaming an agent's steps](phases/03-the-agent-loop/07-streaming-an-agent-s-steps/docs/en.md) | ■ live | 45 min |
| 03.08 | [Interrupts and resumption](phases/03-the-agent-loop/08-interrupts-and-resumption/docs/en.md) | ■ live | 50 min |
| 03.09 | [State machines for agents](phases/03-the-agent-loop/09-state-machines-for-agents/docs/en.md) | ■ live | 55 min |
| 03.10 | [The loop as a graph](phases/03-the-agent-loop/10-the-loop-as-a-graph/docs/en.md) | ■ live | 55 min |
| 03.11 | [Cost and step budgets](phases/03-the-agent-loop/11-cost-and-step-budgets/docs/en.md) | ■ live | 35 min |
| 03.12 | [Debugging a stuck loop](phases/03-the-agent-loop/12-debugging-a-stuck-loop/docs/en.md) | ■ live | 45 min |

[Phase overview →](phases/03-the-agent-loop/README.md)

</details>

<details open>
<summary><b>Phase 04 · Memory & Context Engineering</b> · 11 lessons · 11 live</summary>

Context is the program. Buffers, summaries, embeddings, a vector store by hand, and memory that stays clean.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 04.01 | [Context is the program](phases/04-memory-and-context/01-context-is-the-program/docs/en.md) | ■ live | 40 min |
| 04.02 | [Conversation buffers & truncation](phases/04-memory-and-context/02-conversation-buffers-truncation/docs/en.md) | ■ live | 40 min |
| 04.03 | [Summarization memory](phases/04-memory-and-context/03-summarization-memory/docs/en.md) | ■ live | 45 min |
| 04.04 | [Embeddings from scratch](phases/04-memory-and-context/04-embeddings-from-scratch/docs/en.md) | ■ live | 60 min |
| 04.05 | [A vector store in 80 lines](phases/04-memory-and-context/05-a-vector-store-in-80-lines/docs/en.md) | ■ live | 60 min |
| 04.06 | [Episodic memory](phases/04-memory-and-context/06-episodic-memory/docs/en.md) | ■ live | 50 min |
| 04.07 | [Semantic & procedural memory](phases/04-memory-and-context/07-semantic-procedural-memory/docs/en.md) | ■ live | 50 min |
| 04.08 | [Memory writes: what to keep](phases/04-memory-and-context/08-memory-writes-what-to-keep/docs/en.md) | ■ live | 45 min |
| 04.09 | [Context compaction](phases/04-memory-and-context/09-context-compaction/docs/en.md) | ■ live | 45 min |
| 04.10 | [Files as long-term memory](phases/04-memory-and-context/10-files-as-long-term-memory/docs/en.md) | ■ live | 40 min |
| 04.11 | [Memory poisoning & hygiene](phases/04-memory-and-context/11-memory-poisoning-hygiene/docs/en.md) | ■ live | 40 min |

[Phase overview →](phases/04-memory-and-context/README.md)

</details>

<details open>
<summary><b>Phase 05 · Retrieval & Agentic RAG</b> · 10 lessons · 10 live</summary>

Retrieval as a tool the agent decides to call. Hybrid search, reranking, rewriting, and self-correcting loops.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 05.01 | [Naive RAG and where it breaks](phases/05-agentic-rag/01-naive-rag-and-where-it-breaks/docs/en.md) | ■ live | 45 min |
| 05.02 | [Chunking strategies](phases/05-agentic-rag/02-chunking-strategies/docs/en.md) | ■ live | 45 min |
| 05.03 | [Hybrid search: BM25 + vectors](phases/05-agentic-rag/03-hybrid-search-bm25-vectors/docs/en.md) | ■ live | 55 min |
| 05.04 | [Reranking](phases/05-agentic-rag/04-reranking/docs/en.md) | ■ live | 40 min |
| 05.05 | [Query rewriting & decomposition](phases/05-agentic-rag/05-query-rewriting-decomposition/docs/en.md) | ■ live | 45 min |
| 05.06 | [Retrieval as a tool](phases/05-agentic-rag/06-retrieval-as-a-tool/docs/en.md) | ■ live | 45 min |
| 05.07 | [Self-correcting RAG](phases/05-agentic-rag/07-self-correcting-rag/docs/en.md) | ■ live | 55 min |
| 05.08 | [Corrective RAG loops](phases/05-agentic-rag/08-corrective-rag-loops/docs/en.md) | ■ live | 50 min |
| 05.09 | [Graph-based retrieval](phases/05-agentic-rag/09-graph-based-retrieval/docs/en.md) | ■ live | 55 min |
| 05.10 | [Evaluating retrieval quality](phases/05-agentic-rag/10-evaluating-retrieval-quality/docs/en.md) | ■ live | 45 min |

[Phase overview →](phases/05-agentic-rag/README.md)

</details>

<details open>
<summary><b>Phase 06 · Planning & Reasoning</b> · 10 lessons · 10 live</summary>

Plan-and-execute, task trees, Tree of Thoughts, reflection, verifiers, and knowing when not to plan.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 06.01 | [Chain-of-thought for actions](phases/06-planning-and-reasoning/01-chain-of-thought-for-actions/docs/en.md) | ■ live | 40 min |
| 06.02 | [Plan-and-execute](phases/06-planning-and-reasoning/02-plan-and-execute/docs/en.md) | ■ live | 55 min |
| 06.03 | [Task decomposition trees](phases/06-planning-and-reasoning/03-task-decomposition-trees/docs/en.md) | ■ live | 50 min |
| 06.04 | [Tree of Thoughts search](phases/06-planning-and-reasoning/04-tree-of-thoughts-search/docs/en.md) | ■ live | 60 min |
| 06.05 | [Reflection & self-critique](phases/06-planning-and-reasoning/05-reflection-self-critique/docs/en.md) | ■ live | 45 min |
| 06.06 | [Reflexion: learning from failures](phases/06-planning-and-reasoning/06-reflexion-learning-from-failures/docs/en.md) | ■ live | 55 min |
| 06.07 | [Verifiers and checkers](phases/06-planning-and-reasoning/07-verifiers-and-checkers/docs/en.md) | ■ live | 50 min |
| 06.08 | [Replanning on surprise](phases/06-planning-and-reasoning/08-replanning-on-surprise/docs/en.md) | ■ live | 45 min |
| 06.09 | [Reasoning models in the loop](phases/06-planning-and-reasoning/09-reasoning-models-in-the-loop/docs/en.md) | ■ live | 45 min |
| 06.10 | [When not to plan](phases/06-planning-and-reasoning/10-when-not-to-plan/docs/en.md) | ■ live | 30 min |

[Phase overview →](phases/06-planning-and-reasoning/README.md)

</details>

<details open>
<summary><b>Phase 07 · Model Context Protocol</b> · 11 lessons · 11 live</summary>

MCP from the wire up. JSON-RPC over stdio, a server and a client by hand, transports, auth, and security.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 07.01 | [Why MCP exists](phases/07-model-context-protocol/01-why-mcp-exists/docs/en.md) | ■ live | 35 min |
| 07.02 | [The protocol: JSON-RPC over stdio](phases/07-model-context-protocol/02-the-protocol-json-rpc-over-stdio/docs/en.md) | ■ live | 50 min |
| 07.03 | [Build an MCP server from scratch](phases/07-model-context-protocol/03-build-an-mcp-server-from-scratch/docs/en.md) | ■ live | 60 min |
| 07.04 | [Tools, resources & prompts](phases/07-model-context-protocol/04-tools-resources-prompts/docs/en.md) | ■ live | 50 min |
| 07.05 | [Build an MCP client](phases/07-model-context-protocol/05-build-an-mcp-client/docs/en.md) | ■ live | 55 min |
| 07.06 | [Streamable HTTP transport](phases/07-model-context-protocol/06-streamable-http-transport/docs/en.md) | ■ live | 50 min |
| 07.07 | [Auth for remote servers](phases/07-model-context-protocol/07-auth-for-remote-servers/docs/en.md) | ■ live | 50 min |
| 07.08 | [Sampling and elicitation](phases/07-model-context-protocol/08-sampling-and-elicitation/docs/en.md) | ■ live | 45 min |
| 07.09 | [Composing many servers](phases/07-model-context-protocol/09-composing-many-servers/docs/en.md) | ■ live | 45 min |
| 07.10 | [Testing MCP servers](phases/07-model-context-protocol/10-testing-mcp-servers/docs/en.md) | ■ live | 40 min |
| 07.11 | [MCP security pitfalls](phases/07-model-context-protocol/11-mcp-security-pitfalls/docs/en.md) | ■ live | 45 min |

[Phase overview →](phases/07-model-context-protocol/README.md)

</details>

<details open>
<summary><b>Phase 08 · Multi-Agent Systems</b> · 12 lessons · 12 live</summary>

Orchestrators, workers, handoffs, supervisors, blackboards, A2A, and the real cost of coordination.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 08.01 | [When one agent is not enough](phases/08-multi-agent-systems/01-when-one-agent-is-not-enough/docs/en.md) | ■ live | 35 min |
| 08.02 | [Orchestrator–worker](phases/08-multi-agent-systems/02-orchestrator-worker/docs/en.md) | ■ live | 55 min |
| 08.03 | [Handoffs between agents](phases/08-multi-agent-systems/03-handoffs-between-agents/docs/en.md) | ■ live | 50 min |
| 08.04 | [Supervisor hierarchies](phases/08-multi-agent-systems/04-supervisor-hierarchies/docs/en.md) | ■ live | 50 min |
| 08.05 | [Shared blackboards](phases/08-multi-agent-systems/05-shared-blackboards/docs/en.md) | ■ live | 45 min |
| 08.06 | [Debate and critique](phases/08-multi-agent-systems/06-debate-and-critique/docs/en.md) | ■ live | 45 min |
| 08.07 | [Agent-to-agent (A2A) protocol](phases/08-multi-agent-systems/07-agent-to-agent-a2a-protocol/docs/en.md) | ■ live | 55 min |
| 08.08 | [Message passing & mailboxes](phases/08-multi-agent-systems/08-message-passing-mailboxes/docs/en.md) | ■ live | 50 min |
| 08.09 | [Parallel fan-out, fan-in](phases/08-multi-agent-systems/09-parallel-fan-out-fan-in/docs/en.md) | ■ live | 45 min |
| 08.10 | [Role design & specialization](phases/08-multi-agent-systems/10-role-design-specialization/docs/en.md) | ■ live | 40 min |
| 08.11 | [Failure modes of swarms](phases/08-multi-agent-systems/11-failure-modes-of-swarms/docs/en.md) | ■ live | 45 min |
| 08.12 | [Cost of coordination](phases/08-multi-agent-systems/12-cost-of-coordination/docs/en.md) | ■ live | 35 min |

[Phase overview →](phases/08-multi-agent-systems/README.md)

</details>

<details open>
<summary><b>Phase 09 · Frameworks & SDKs</b> · 10 lessons · 10 live</summary>

Now import the frameworks. The same loop in LangGraph, Agents SDKs, CrewAI, AutoGen, and when to skip them all.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 09.01 | [The same loop, ten frameworks](phases/09-frameworks-and-sdks/01-the-same-loop-ten-frameworks/docs/en.md) | ■ live | 40 min |
| 09.02 | [LangGraph: state graphs](phases/09-frameworks-and-sdks/02-langgraph-state-graphs/docs/en.md) | ■ live | 60 min |
| 09.03 | [OpenAI Agents SDK](phases/09-frameworks-and-sdks/03-openai-agents-sdk/docs/en.md) | ■ live | 50 min |
| 09.04 | [Claude Agent SDK](phases/09-frameworks-and-sdks/04-claude-agent-sdk/docs/en.md) | ■ live | 50 min |
| 09.05 | [CrewAI roles & crews](phases/09-frameworks-and-sdks/05-crewai-roles-crews/docs/en.md) | ■ live | 45 min |
| 09.06 | [AutoGen conversations](phases/09-frameworks-and-sdks/06-autogen-conversations/docs/en.md) | ■ live | 45 min |
| 09.07 | [LlamaIndex agents](phases/09-frameworks-and-sdks/07-llamaindex-agents/docs/en.md) | ■ live | 45 min |
| 09.08 | [Pydantic AI typed agents](phases/09-frameworks-and-sdks/08-pydantic-ai-typed-agents/docs/en.md) | ■ live | 45 min |
| 09.09 | [Choosing (or skipping) a framework](phases/09-frameworks-and-sdks/09-choosing-or-skipping-a-framework/docs/en.md) | ■ live | 35 min |
| 09.10 | [Porting between frameworks](phases/09-frameworks-and-sdks/10-porting-between-frameworks/docs/en.md) | ■ live | 45 min |

[Phase overview →](phases/09-frameworks-and-sdks/README.md)

</details>

<details open>
<summary><b>Phase 10 · Coding & Computer-Use Agents</b> · 11 lessons · 11 live</summary>

Agents that edit files, run tests, drive browsers and terminals. Ends with a mini coding agent of your own.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 10.01 | [Anatomy of a coding agent](phases/10-coding-and-computer-use/01-anatomy-of-a-coding-agent/docs/en.md) | ■ live | 45 min |
| 10.02 | [File read, edit & search tools](phases/10-coding-and-computer-use/02-file-read-edit-search-tools/docs/en.md) | ■ live | 55 min |
| 10.03 | [Running code in a sandbox](phases/10-coding-and-computer-use/03-running-code-in-a-sandbox/docs/en.md) | ■ live | 55 min |
| 10.04 | [Test-driven agent loops](phases/10-coding-and-computer-use/04-test-driven-agent-loops/docs/en.md) | ■ live | 55 min |
| 10.05 | [Repository maps & context](phases/10-coding-and-computer-use/05-repository-maps-context/docs/en.md) | ■ live | 50 min |
| 10.06 | [Skills and SKILL.md](phases/10-coding-and-computer-use/06-skills-and-skill-md/docs/en.md) | ■ live | 45 min |
| 10.07 | [Browser agents](phases/10-coding-and-computer-use/07-browser-agents/docs/en.md) | ■ live | 55 min |
| 10.08 | [Computer use: screenshots to clicks](phases/10-coding-and-computer-use/08-computer-use-screenshots-to-clicks/docs/en.md) | ■ live | 60 min |
| 10.09 | [Terminal agents](phases/10-coding-and-computer-use/09-terminal-agents/docs/en.md) | ■ live | 50 min |
| 10.10 | [Long-horizon tasks](phases/10-coding-and-computer-use/10-long-horizon-tasks/docs/en.md) | ■ live | 50 min |
| 10.11 | [Build a mini coding agent](phases/10-coding-and-computer-use/11-build-a-mini-coding-agent/docs/en.md) | ■ live | 90 min |

[Phase overview →](phases/10-coding-and-computer-use/README.md)

</details>

<details open>
<summary><b>Phase 11 · Evaluation & Observability</b> · 10 lessons · 10 live</summary>

Golden tasks, trajectory evals, careful LLM judges, OpenTelemetry traces, replay, and your own eval harness.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 11.01 | [Why agent evals are hard](phases/11-evaluation-and-observability/01-why-agent-evals-are-hard/docs/en.md) | ■ live | 35 min |
| 11.02 | [Golden tasks & datasets](phases/11-evaluation-and-observability/02-golden-tasks-datasets/docs/en.md) | ■ live | 45 min |
| 11.03 | [Trajectory evaluation](phases/11-evaluation-and-observability/03-trajectory-evaluation/docs/en.md) | ■ live | 50 min |
| 11.04 | [LLM-as-judge, carefully](phases/11-evaluation-and-observability/04-llm-as-judge-carefully/docs/en.md) | ■ live | 50 min |
| 11.05 | [Tool-call accuracy](phases/11-evaluation-and-observability/05-tool-call-accuracy/docs/en.md) | ■ live | 40 min |
| 11.06 | [Tracing with OpenTelemetry](phases/11-evaluation-and-observability/06-tracing-with-opentelemetry/docs/en.md) | ■ live | 50 min |
| 11.07 | [Replay and regression](phases/11-evaluation-and-observability/07-replay-and-regression/docs/en.md) | ■ live | 45 min |
| 11.08 | [Online metrics & feedback](phases/11-evaluation-and-observability/08-online-metrics-feedback/docs/en.md) | ■ live | 40 min |
| 11.09 | [Benchmarks: SWE-bench to τ-bench](phases/11-evaluation-and-observability/09-benchmarks-swe-bench-to-tau-bench/docs/en.md) | ■ live | 45 min |
| 11.10 | [Building an eval harness](phases/11-evaluation-and-observability/10-building-an-eval-harness/docs/en.md) | ■ live | 70 min |

[Phase overview →](phases/11-evaluation-and-observability/README.md)

</details>

<details open>
<summary><b>Phase 12 · Safety, Security & Guardrails</b> · 11 lessons · 11 live</summary>

The agent threat model. Prompt injection, exfiltration, least privilege, sandboxes, permissions, red-teaming.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 12.01 | [The agent threat model](phases/12-safety-and-security/01-the-agent-threat-model/docs/en.md) | ■ live | 45 min |
| 12.02 | [Prompt injection, direct & indirect](phases/12-safety-and-security/02-prompt-injection-direct-indirect/docs/en.md) | ■ live | 55 min |
| 12.03 | [Data exfiltration paths](phases/12-safety-and-security/03-data-exfiltration-paths/docs/en.md) | ■ live | 45 min |
| 12.04 | [Least-privilege tools](phases/12-safety-and-security/04-least-privilege-tools/docs/en.md) | ■ live | 40 min |
| 12.05 | [Sandboxing with containers](phases/12-safety-and-security/05-sandboxing-with-containers/docs/en.md) | ■ live | 55 min |
| 12.06 | [Permission systems](phases/12-safety-and-security/06-permission-systems/docs/en.md) | ■ live | 50 min |
| 12.07 | [Input & output guardrails](phases/12-safety-and-security/07-input-output-guardrails/docs/en.md) | ■ live | 45 min |
| 12.08 | [Secrets and credentials](phases/12-safety-and-security/08-secrets-and-credentials/docs/en.md) | ■ live | 35 min |
| 12.09 | [Human-in-the-loop design](phases/12-safety-and-security/09-human-in-the-loop-design/docs/en.md) | ■ live | 40 min |
| 12.10 | [Red-teaming your agent](phases/12-safety-and-security/10-red-teaming-your-agent/docs/en.md) | ■ live | 55 min |
| 12.11 | [Audit logs](phases/12-safety-and-security/11-audit-logs/docs/en.md) | ■ live | 35 min |

[Phase overview →](phases/12-safety-and-security/README.md)

</details>

<details>
<summary><b>Phase 13 · Production Agents</b> · 10 lessons · 0 live</summary>

Durable execution, queues, caching, routing, cost control, versioning, and incident playbooks.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 13.01 | From notebook to service | □ planned | 45 min |
| 13.02 | Durable execution | □ planned | 55 min |
| 13.03 | Queues, workers & long jobs | □ planned | 50 min |
| 13.04 | Prompt caching & latency | □ planned | 45 min |
| 13.05 | Cost control at scale | □ planned | 40 min |
| 13.06 | Model routing & fallbacks | □ planned | 45 min |
| 13.07 | Versioning prompts and tools | □ planned | 40 min |
| 13.08 | Deploying with Docker | □ planned | 45 min |
| 13.09 | Rate limits & backpressure | □ planned | 40 min |
| 13.10 | Incident playbooks | □ planned | 35 min |

[Phase overview →](phases/13-production-agents/README.md)

</details>

<details>
<summary><b>Phase 14 · Agent UX & Interfaces</b> · 8 lessons · 0 live</summary>

Streaming step views, approvals and undo, voice, background agents, and the design of trust.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 14.01 | Streaming UIs for agents | □ planned | 45 min |
| 14.02 | Showing the work: step views | □ planned | 40 min |
| 14.03 | Approvals & undo | □ planned | 40 min |
| 14.04 | Chat is not the only interface | □ planned | 35 min |
| 14.05 | Voice agents | □ planned | 55 min |
| 14.06 | Background agents & notifications | □ planned | 40 min |
| 14.07 | Generative UI | □ planned | 45 min |
| 14.08 | Trust and explainability | □ planned | 35 min |

[Phase overview →](phases/14-agent-ux/README.md)

</details>

<details>
<summary><b>Phase 15 · Capstone: Your Own Agent Harness</b> · 8 lessons · 0 live</summary>

Everything at once. A loop, tool registry, memory, MCP, subagents, permissions, and evals, shipped as a CLI.

| # | Lesson | Status | Time |
|---|--------|--------|------|
| 15.01 | Why build a harness | □ planned | 35 min |
| 15.02 | The core loop & tool registry | □ planned | 70 min |
| 15.03 | Memory & context manager | □ planned | 70 min |
| 15.04 | MCP client integration | □ planned | 60 min |
| 15.05 | Subagents & delegation | □ planned | 60 min |
| 15.06 | Permissions & sandbox | □ planned | 60 min |
| 15.07 | Evals & traces | □ planned | 60 min |
| 15.08 | Ship it: CLI + docs | □ planned | 60 min |

[Phase overview →](phases/15-capstone-agent-harness/README.md)

</details>

<!-- CONTENTS:END -->

## Contributing

The curriculum is planned; most lessons still need writing. If you've built agents, you can help.

1. Pick a planned lesson from the [roadmap](ROADMAP.md) and open an issue saying you're on it.
2. Copy the structure in [LESSON_TEMPLATE.md](LESSON_TEMPLATE.md).
3. Make the code run offline with a scripted model, add tests, write the quiz, and ship one artifact.
4. Run `node scripts/build.mjs` and `python3 scripts/test_lessons.py`, then open a PR.

Full guide: [CONTRIBUTING.md](CONTRIBUTING.md). Agents contributing on someone's behalf should read [AGENTS.md](AGENTS.md).

## Maintainer

<table>
  <tr>
    <td width="96"><img src="https://github.com/Ramakm.png?size=192" width="88" alt="Ramakrushna Mohapatra"></td>
    <td>
      <b>Ramakrushna Mohapatra</b><br>
      Sr. Data Scientist · GenAI &amp; LLM engineer · Tech trainer · Founder of <a href="https://www.growtechie.in">GrowTechie</a><br>
      <a href="https://www.linkedin.com/in/ramakrushnamohapatra"><img src="assets/readme/icons/linkedin.svg" width="16" height="16" alt="LinkedIn"> ramakrushnamohapatra</a> &nbsp;·&nbsp;
      <a href="https://www.instagram.com/techwith.ram/"><img src="assets/readme/icons/instagram.svg" width="16" height="16" alt="Instagram"> techwith.ram</a> &nbsp;·&nbsp;
      <a href="https://x.com/techwith_ram"><img src="assets/readme/icons/x.svg" width="16" height="16" alt="X (Twitter)"> techwith_ram</a>
    </td>
  </tr>
</table>

If this course helps you, star the repo and share it. It helps other people find it.

## License

[MIT](LICENSE) © 2026 Ramakrushna Mohapatra. Use it, fork it, teach with it.
