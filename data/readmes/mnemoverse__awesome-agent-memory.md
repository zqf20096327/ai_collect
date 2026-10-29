# Awesome Agent Memory [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of memory systems, frameworks, benchmarks, and research for AI agents.

Agents forget between sessions and between tools. "Agent memory" is the growing category of systems that decide what to keep, connect related facts, and improve recall over time. This list tracks the tools and research in that space.

Contributions welcome. Please keep entries factual and free of marketing language. One tool per pull request, alphabetical within each section. See [Contributing](#contributing).

## Contents

- [Managed memory APIs and services](#managed-memory-apis-and-services)
- [Open-source frameworks and engines](#open-source-frameworks-and-engines)
- [Agent memory workflows and templates](#agent-memory-workflows-and-templates)
- [MCP memory servers](#mcp-memory-servers)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Papers](#papers)
- [Contributing](#contributing)

## Managed memory APIs and services

- [GoodMem](https://goodmem.ai) - Memory layer for agentic AI with owners, roles, scoped API keys and retrieval logging, multi-modal hybrid search with reranking, available as a managed cloud or self-hosted, with SDKs in Python, TypeScript, Java, .NET and Go.
- [Honcho](https://github.com/plastic-labs/honcho) - Open-source (AGPL-3.0) memory server that stores messages between peers (users and agents) and reasons over them in the background to build a representation of each peer, plus a managed cloud, with SDKs in Python and TypeScript.
- [Marvnor](https://wendelxia.github.io/marvnor/) - Proprietary hosted API that stores facts as source, relation and target records and answers structured questions against them as TRUE, FALSE or UNKNOWN, flagging conflicting values, with in-place correction and targeted deletion.
- [Mem0](https://github.com/mem0ai/mem0) - Open-source (Apache-2.0) memory layer that extracts facts from conversations, plus a managed cloud, with many framework integrations.
- [Membase](https://github.com/unibaseio/membase) - Hosted memory layer with a remote MCP endpoint (OAuth) and MIT-licensed Python and TypeScript SDKs, letting Claude, ChatGPT, Cursor and custom agents share one persistent memory.
- [Mnemoverse](https://mnemoverse.com) - Managed memory engine for AI agents over MCP, with shared rooms (beta), an MIT local stdio MCP server using an API key, and a remote MCP endpoint with OAuth; rating a recalled memory as helpful or misleading re-ranks what comes back next.
- [Supermemory](https://github.com/supermemoryai/supermemory) - Memory and context API for AI apps and agents, with fact extraction, user profiles, connectors, and hybrid vector-plus-keyword retrieval.
- [Zep](https://www.getzep.com/) - Managed memory service built on a temporal knowledge graph (open-source Graphiti engine), offered as cloud, BYOK, and BYOC deployments.

## Open-source frameworks and engines

- [birkin-mnemosyne](https://github.com/ashmoonori-afk/birkin-mnemosyne) - MIT local Markdown memory for agents with multilingual BM25 recall that handles Hangul and CJK, usage-based decay, and an optional MCP server; the core has no runtime dependencies.
- [chamnan](https://github.com/ArcticFox2029/chamnan) - MIT repository-local memory for coding agents that stores an architecture index, an impact map, session records, and decisions as markdown committed beside the code, retrieved by keyword and injected at session start. Python standard library only, no network at runtime.
- [Cognee](https://github.com/topoteretes/cognee) - Apache-2.0 memory framework that turns documents, code, and conversations into a self-hosted knowledge graph, where a remember operation stores content and a recall operation retrieves graph, vector, or code context, with a managed option (Cognee Cloud).
- [Dory](https://github.com/tjqscott/dory) - MIT project-memory tool for coding agents, using a linked Markdown wiki with decisions, findings, and tasks, plus Claude Code hooks for session-start loading and structural linting.
- [Graphiti](https://github.com/getzep/graphiti) - Apache-2.0 engine building real-time, bi-temporal knowledge graphs from conversational and structured data, with hybrid semantic, keyword, and graph retrieval (powers Zep).
- [Hindsight](https://github.com/vectorize-io/hindsight) - MIT agent-memory system running four parallel retrieval strategies per query: semantic search, BM25 keyword matching, graph traversal, and temporal reasoning.
- [LangMem](https://github.com/langchain-ai/langmem) - MIT SDK giving LangGraph agents long-term semantic, episodic, and procedural memory, plus a background memory manager.
- [Letta](https://github.com/letta-ai/letta-code) - Apache-2.0 stateful-agent harness with self-editing memory blocks, Git-backed context (MemFS), and conversation search; the current Letta implementation.
- [LongMemory](https://github.com/CaviraOSS/LongMemory) - Apache-2.0 local-first memory engine for LLM applications and agents (formerly CaviraOSS OpenMemory) that keeps immutable content with provenance and temporal truth in SQLite, exposed as an npm library, CLI, HTTP API, MCP server, dashboard, and VS Code extension.
- [LWC](https://github.com/JanYork/llm-wiki-cli) - Apache-2.0 local-first CLI giving coding agents source-grounded project memory, plans, citations, and optional document and code graphs.
- [Mem++](https://github.com/AIDAChip-Inc/mem-plus-plus) - Apache-2.0 organizational memory engine for LLM agents that supports verbatim ingestion without LLM extraction and retrieves dated evidence using PostgreSQL full-text search, pgvector embeddings, and tags.
- [Memary](https://github.com/kingjulio8238/Memary) - Long-term memory framework for autonomous agents that builds a Neo4j/FalkorDB knowledge graph and tracks entities by breadth and recency.
- [MemEngine](https://github.com/nuster1128/MemEngine) - Library unifying many published LLM-agent memory models under a common, modular, pluggable interface (RUC and Huawei Noah's Ark).
- [Memobase](https://github.com/memodb-io/memobase) - User-profile-based long-term memory backend for LLM applications; maintains structured, evolving user profiles and event timelines across sessions.
- [Memori](https://github.com/MemoriLabs/Memori) - Apache-2.0 agent-memory engine that stores memory in standard SQL databases (SQLite, PostgreSQL, MySQL), with an optional managed cloud.
- [MemoryOS](https://github.com/BAI-LAB/MemoryOS) - OS-inspired hierarchical memory framework with short-, mid-, and long-term storage plus updating, retrieval, and generation modules.
- [MemOS](https://github.com/MemTensor/MemOS) - Memory operating system for LLMs; a unified API to add, retrieve, and manage graph-structured, multi-modal long-term memory.
- [memU](https://github.com/NevaMind-AI/memU) - Apache-2.0 agent-memory framework where agents store notes as organized Markdown files, recalled via embedding-based ranked retrieval.
- [MIRIX](https://github.com/Mirix-AI/MIRIX) - Apache-2.0 multi-agent memory system with six memory types (core, episodic, semantic, procedural, resource, knowledge vault); multimodal.
- [Mnemosyne](https://github.com/28naem-del/mnemosyne) - MIT TypeScript memory engine for agents that keeps each memory with its source provenance in one local SQLite file and retires memories recorded as depending on a source when that source is corrected, with exact replay and bisect in the 3.0 pre-release; exposed as a stdio MCP server, CLI, SDK, and HTTP API.
- [Off the Wall](https://github.com/toranalytics/off-the-wall) - MIT hooks plugin for Claude Code and Codex that stores the user's past corrections locally and quotes them back to the agent before it answers, with a report of the most-corrected topics.
- [pulse-path](https://github.com/Inspired-by-Atmosphere/pulse-path) - MIT agent skills and Python standard-library scripts that keep an agent's Markdown memory pointer file and the docs it links to consistent, with a dry-run health check, a link-integrity scan, audit and consolidation reports, and a declarative rule table.
- [ReasonGraph](https://github.com/bgokden/reasongraph) - MIT graph-memory library that extracts entities and cause-effect relations with small fine-tuned models, answers why-questions by walking causal chains with citations, supports time-travel queries and contradiction handling, with a hosted service (ReasonGraph Cloud).
- [self-learning-agent-setup](https://github.com/ssap-pa/self-learning-agent-setup) - MIT Postgres schema and TypeScript loop that store each human approve, edit, and reject of an agent draft with pgvector embeddings and retrieve feedback from similar past tasks before the next draft.
- [Sno Station](https://github.com/sno-ai/sno-station) - Apache-2.0 shared memory engine for coding agents, with encrypted local SQLite storage, project/global recall and corrections that retain superseded records; memory processing can run locally or use configured model and optional Sno cloud services.

## Agent memory workflows and templates

Reusable agent-memory workflows and templates for knowledge practices agents can adopt directly, not general prompt packs.

- [Strata Sample](https://github.com/Zerokool1986/Strata-sample) - Custom license; commercial use and free redistribution with credit allowed, no resale; knowledge system for coding agents that stores typed Markdown entries with status and provenance in a Git repo, keeps superseded entries readable instead of deleting them, and includes templates, a worked example, and a five-question self-test.

## MCP memory servers

Memory servers exposed through the Model Context Protocol. Client support depends on the server transport and authentication method.

- [Basic Memory](https://github.com/basicmachines-co/basic-memory) - Local-first, AGPL-3.0 MCP server that stores agent memory as Obsidian-compatible Markdown files, building a knowledge graph agents can read and write, plus an optional hosted version (Basic Memory Cloud).
- [BrainTube](https://github.com/lildaddyo/braintube-mcp) - Hosted, read-write MCP memory server (Elastic License 2.0) over a personal library of YouTube transcripts, podcasts, articles, PDFs and notes, with OAuth or API-key auth over Streamable HTTP.
- [Carbon Forge](https://carbonforge.dev/) - Hosted, proprietary MCP server over Streamable HTTP where people and agents read and write one shared record of pages, code and files, with history that is hash-chained and only moves forward; without a token it serves the same public content an anonymous visitor sees, through a read-only tool set; a bearer token writes and reads private content.
- [Cloud Alter Ego](https://cloudalterego.cafeboon.com) - Hosted remote MCP connector with OAuth that keeps rules, a profile and per-project journals as plain Markdown files in the user's own OneDrive, Google Drive, Dropbox, GitHub or Azure DevOps; the server does not store the content.
- [deja-vu](https://github.com/vshulcz/deja-vu) - MIT local memory for coding agents that indexes the session transcripts Claude Code, Codex, Cursor and 40 other agents already write to disk and serves BM25 recall over a local stdio MCP server and hooks, with no LLM.
- [fidelis](https://github.com/hermes-labs-ai/fidelis) - Apache-2.0, local-first agent memory for Claude Code over MCP: local vector recall by default with an explicit keyword+vector hybrid mode, no generative LLM in retrieval, no cloud at runtime.
- [Firekeep](https://github.com/kapella-hub/FirekeepHQ) - BUSL-1.1 self-hosted MCP operating layer that shares durable knowledge, working state, cooperative coordination leases, and replay evidence across Claude Code, Codex, Kiro, and OpenCode.
- [Graphmem](https://github.com/sonic182/graphmem) - Local-first, MIT-licensed MCP server giving Claude Code, Codex, OpenCode, and pi a shared SQLite memory store with local semantic search and linked entities, plus optional code navigation tools.
- [Honcho MCP](https://github.com/plastic-labs/honcho/tree/main/mcp) - AGPL-3.0 MCP server for Honcho, hosted at mcp.honcho.dev and authenticated with a Honcho API key as a bearer token; the same tools also run locally over stdio or Streamable HTTP, and memories are stored in the user's Honcho workspace.
- [Hyperconsciousness](https://github.com/louis030195/hyperconsciousness) - MIT-licensed developer-alpha knowledge store with encrypted, append-only records and MCP retrieval through scoped, expiring grants.
- [Knowledge Graph Memory Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) - Reference MCP server from the Model Context Protocol project, published on npm as @modelcontextprotocol/server-memory, that stores entities, relations, and observations as a local knowledge graph in a JSONL file.
- [Mem0 MCP](https://docs.mem0.ai/platform/mem0-mcp) - Hosted MCP server for the Mem0 Platform, reached over HTTPS with browser sign-in or an API key as a bearer token; memories are stored in the user's Mem0 account.
- [Memento](https://mementoagi.com) - Hosted MCP memory for coding agents with editable Markdown records, team-shared context, and a web dashboard.
- [MemoryRouter](https://memoryrouter.ai) - Hosted memory service over a remote Streamable HTTP MCP endpoint with OAuth, where one user-selected vault is shared across connected clients such as ChatGPT, Claude, Codex, and Cursor.
- [Mnemosyne OS](https://github.com/Mnemosyne-OS/Mnemosyne-Neural-OS/tree/main/packages/mcp) - MIT local stdio MCP server for the Mnemosyne OS desktop app, which keeps memory in vaults built from the user's folders, with vector and local BM25 search; open core, closed-source memory engine.
- [Mnemoverse](https://github.com/mnemoverse/mcp-memory-server) - Hosted persistent memory with an MIT local stdio MCP server using an API key, plus a remote HTTP MCP endpoint with OAuth for compatible clients.
- [ReasonGraph Cloud](https://memory.primaxiom.ai) - Hosted graph memory over Streamable HTTP MCP with API-key auth; tools for remembering facts, discovering connections, tracing causes and effects and what-if queries.
- [Screenpipe](https://github.com/screenpipe/screenpipe) - MCP server for searching screen text and audio transcripts captured by a running Screenpipe instance, with source available under the Screenpipe Commercial License.
- [Selvedge](https://github.com/masondelan/selvedge) - MIT-licensed local stdio MCP server and CLI that stores coding decisions, reasons, and rejected approaches in SQLite for retrieval across agent sessions.
- [sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory) - MIT local stdio MCP memory server that gives an agent associative recall over a folder of markdown notes: vector retrieval for entry points, hand-curated wikilinks as the graph, and cross-encoder rerank, with retrieval A/B telemetry in SQLite, plus a Claude Code Stop hook that writes a per-turn ledger to SQLite without LLM calls.
- [Synapse](https://github.com/anshulyadav1976/synapse) - MIT local stdio MCP memory server that stores imported history, linked wiki pages, and human-approved agent notes as Markdown with a disposable SQLite FTS5 and graph index.
- [Throughline](https://getthroughline.ai/) - Hosted MCP service for persistent AI identity and memory across supported clients, with MIT-licensed Claude Code and Codex plugins and verifiable history exports.

## Benchmarks and evaluation

Common suites used to evaluate agent memory.

- [agent-memory-bench](https://github.com/GiulioDER/agent-memory-bench) - Apache-2.0 execution-graded benchmark for coding-agent memory, with a retrieval-only official run and separate optional lifecycle probes.
- [BEAM](https://arxiv.org/abs/2510.27246) - Long-term memory benchmark: multi-turn conversations up to 10M tokens, 2,000 questions across ten memory abilities (ICLR 2026).
- [LoCoMo](https://snap-research.github.io/locomo/) - Very long-term multi-session dialogue benchmark (~300 turns, up to 35 sessions), evaluated via QA, event summarization, and multimodal dialogue generation (ACL 2024).
- [LongMemEval](https://xiaowu0162.github.io/long-mem-eval/) - 500-question benchmark testing five long-term memory abilities of chat assistants over scalable chat histories (ICLR 2025).
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257) - Benchmark that converts existing and newly constructed long-context datasets into incremental multi-turn interactions to test memory agents on accurate retrieval, test-time learning, long-range understanding, and selective forgetting (ICLR 2026).
- [Open Agent Memory Benchmark](https://github.com/rocke2020/open-agent-memory-benchmark) - Apache-2.0 benchmark comparing self-hosted agent-memory systems through native APIs across answer accuracy, answer-visible context, indexing, and latency, with public question-level results and frozen evaluation plans.

## Papers

- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) - Organizes agent notes via Zettelkasten-style linking and evolution for dynamic retrieval (NeurIPS 2025).
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) - Introduces a memory stream with reflection and retrieval to simulate believable behavior (UIST 2023).
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for LLMs](https://arxiv.org/abs/2405.14831) - Combines knowledge graphs with Personalized PageRank, inspired by hippocampal indexing, for long-term retrieval (NeurIPS 2024).
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) - Memory architecture that extracts, consolidates, and retrieves salient information from ongoing conversations, with a graph-based variant, evaluated on LoCoMo (2025).
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) - Virtual context management (the origin of Letta).
- [MemoryBank: Enhancing LLMs with Long-Term Memory](https://arxiv.org/abs/2305.10250) - Long-term memory via an Ebbinghaus-inspired forgetting curve and event summarization (2023).
- [Semantic Level of Detail for Knowledge Graphs: Discovering Abstraction Boundaries via Spectral Heat Diffusion](https://arxiv.org/abs/2603.08965) - Introduces SLoD, a continuous zoom operator built from heat-kernel diffusion on a graph Laplacian induced by a Poincaré-ball (hyperbolic) embedding (Mnemoverse).
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) - Describes the Graphiti temporal knowledge-graph engine for agent memory, with retrieval-benchmark evaluation (2025).

## Contributing

Open a pull request adding one tool, in the right section, in alphabetical order, with a short factual description (no marketing language). New sections are welcome if a genuine category is missing. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guidelines.

## License

[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, contributors have waived all copyright and related rights to this list.
