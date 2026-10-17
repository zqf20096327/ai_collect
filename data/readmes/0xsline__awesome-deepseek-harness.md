<p align="center">
 <a href="README.md">English</a>&nbsp;&nbsp;|&nbsp;&nbsp;
 <a href="README.zh-CN.md">简体中文</a>
</p>

<br>

<div align="center">
 <img width="640" src="assets/banner.jpg" alt="Awesome DeepSeek Harness">
</div>

# Awesome DeepSeek Harness [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!-- BANNER: luminous DeepSeek whale with agent-orchestration harness (1280×480) -->

<p align="center">
 <a href="#install">Install</a>&nbsp;&nbsp;&nbsp;
 <a href="contributing.md">Contribution guide</a>&nbsp;&nbsp;&nbsp;
 <a href="https://deepseekdocs.com/">DeepSeek Docs</a>&nbsp;&nbsp;&nbsp;
 <a href="https://github.com/topics/dsh-plugin">Public plugin topic</a>&nbsp;&nbsp;&nbsp;
 <a href="https://github.com/dsh-external/issues">Issues</a>&nbsp;&nbsp;&nbsp;
 <a href="CATALOG.md">完整目录</a>&nbsp;&nbsp;&nbsp;
</p>

<br>

<p align="center">
 <b>Curated DeepSeek Harness (DSH) ecosystem: plugins, tools &amp; infrastructure. Sources: dsh-external/hub catalog and the public GitHub dsh-plugin topic.</b><br>
</p>

<br>
> Note: the GitHub [`dsh-plugin` topic](https://github.com/topics/dsh-plugin) is public; some `dsh-external` repository links may still require org access.

## Contents

- [Install](#install)
- [Core & Bundles](#core--bundles)
- [Agents & Orchestration](#agents--orchestration)
- [Context & Search](#context--search)
- [Memory & Knowledge](#memory--knowledge)
- [Input & Editing](#input--editing)
- [UI, Themes & Interaction](#ui-themes--interaction)
- [Dashboards & Session UX](#dashboards--session-ux)
- [IDE & Clients](#ide--clients)
- [Browser & Remote](#browser--remote)
- [Models & Inference](#models--inference)
- [Git & Engineering](#git--engineering)
- [Security & Governance](#security--governance)
- [Output & Deliverables](#output--deliverables)
- [Office & Documents](#office--documents)
- [Notifications & Channels](#notifications--channels)
- [Fun & Lifestyle](#fun--lifestyle)
- [Plugin Ecosystem & Development](#plugin-ecosystem--development)
- [Runtime & Operations](#runtime--operations)
- [Domain & Specialist Skills](#domain--specialist-skills)
- [Tools & Utilities](#tools--utilities)
- [Related](#related)
- [Thanks](#thanks)

## Install

Install the official runtime with Node.js:

```sh
npx @deepseek-ai/dsh web
```

Install an external profile bundle with pnpm on your `PATH`:

```sh
dsh plugin --profile web add "github:owner/repo#ref"
```

`dsh plugin` forwards package operations to pnpm, so npm, Git/GitHub, local path, `file:` and `link:` package specs are supported. Only packages declaring `dsh.bundle.patch` become active profile layers; plain dependencies remain installed but inactive. Restart `dsh --profile web` after installing or updating a bundle.

The former `&path:` sub-path and Repository Plugin installation forms are not part of the current official bundle flow; use an installable package that declares `dsh.bundle.patch`.

Management panel: Settings → Plugins.

## Core & Bundles

- [DeepSeek Harness Ultimate](https://github.com/18126295767-cell/deepseek-harness-ultimate) - Community-maintained reproducible profile installer: deduplicated defaults across coding, workflow, reliability and productivity; full commit-SHA pins, permissive-license audit, pre/post dependency checks, optional sensitive integrations, and beginner guides in 20 languages for Windows, macOS and Linux.
- [dsh-deepresearch](https://github.com/dsh-external/dsh-deepresearch) - DeepResearch plugin (cordis).
- [dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute) - Dual-model plan/execute routing: planner model thinks, executor model acts.
- [dsh-toolkit](https://github.com/dsh-external/dsh-toolkit) - Zero-dependency tool suite (calculator/csv/diff/encoding/json/markdown/regex/time).
- [dsh-deep-research](https://github.com/dsh-external/dsh-deep-research) - Adaptive deep-research orchestrator (workflow engine).
- [dsh-101](https://github.com/dsh-external/dsh-101) - DSH documentation reading mode.
- [dsh-client-ui-plan-execute](https://github.com/dsh-external/dsh-client-ui-plan-execute) - Web Settings row for plan/execute model routing.
- [dsh_workflow](https://github.com/dsh-external/dsh_workflow) - Dynamic workflow for DSH (placeholder).
- [dsh-equip-engine](https://github.com/wuykjl/dsh-equip-engine) - Task-driven plugin equip engine: dual retrieval (curated rules + LLM semantic), combo scoring (synergy/conflict/cost/trust), conflict detection and install-command export.
- [dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) - Four-source migration wizard: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills, instructions and slash commands into DSH (approval-gated, idempotent, resumable sessions).
- [dsh-skill-mover](https://github.com/mjylfz/dsh-skill-mover) - One-click skill migration into DSH: scans 14 agent platforms (Cursor, Claude Code, Codex, Hermes, Trae, Qoder...) plus the shared ~/.agents layer, merges same-name skills, dedupes symlinks and rolls back safely.
- [gewu-tools](https://github.com/nyantused-cpun/gewu-tools) - Model-agnostic visual-inspection pipeline for text-only agents: page-by-page HTML screenshots plus a ready-made vision-subagent briefing contract (gewu_prep), then source-code truth verification of every finding (gewu_locate); validated on mimo-v2.5 & qwen3.7-plus.
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) - DSH plugin manager & marketplace: one-click enable/disable, multi-source market, static index (500+ plugins / 300 skills), skill install/disable, suite one-click assembly, one-click framework upgrade (online install + auto-rollback).
- [dsh-gsd-bundle](https://github.com/jaaty/dsh-gsd-bundle) - Git Ship Done (opengsd-core) reimplemented as host-plane Cordis plugins: replaces the default agent loop with a spec/discuss/plan/execute/verify/ship phase loop.
- [1420079678-ctrl/agent-body](https://github.com/1420079678-ctrl/agent-body) - Plugin coordination layer: plugins declare their capabilities, commands route to the owning plugin without a model call, tool schemas load on demand to cut prompt tokens, run history consolidates into long-term memory while idle, and failures are classified before any retry.
- [dsh-yawn](https://github.com/zhming0/dsh-yawn) - Always-on DSH distribution for the web: deploy once on a VM or Kubernetes, and every session runs in its own sandbox (Docker, Kubernetes, or Buildkite).

## Agents & Orchestration

- [dsh-jev-plugin](https://github.com/luobosibing2/dsh-jev-plugin) - Opt-in Jev/Luna decision layer for DeepSeek Harness: skill and file selection, task supervision, tool-output filtering, approval assistance and recorded-stage navigation; features are disabled by default.
- [dsh-jev-preset](https://github.com/Yum-wu/dsh-jev-preset) - JEV agent preset bundle with prompt-guided task routing, cross-verification and quantitative checklists.
- [dsh-task-supervisor](https://github.com/gosomea/dsh-task-supervisor) - Persistent task supervision with plan coverage review, DAG progress, sidebar consultation, and stage/completion checks; npm development preview.
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) - Multi-agent team orchestration: captain-style session with durable sub-agent teams, role assignment, and coordinated task execution.
- [dsh-todo-guard](https://github.com/a903067276-rgb/dsh-todo-guard) - Reliable todo panel that survives restarts (official panel only re-renders on write — fixed via projection pre-warm) with three-state completion verification: evidence exists → verified, fake evidence → blocked, no evidence → unverified badge; settings toggle to fall back to official behavior.
- [fakechris/dsh-track](https://github.com/fakechris/dsh-track) - Embedded task-management engine for DSH: decision-point protocol, idea capture wall, Linear-shaped issue store with an evidence-driven lifecycle.
- [dsh-dual-model-eval](https://github.com/huangdaxianer/dsh-dual-model-eval) - Runs one coding prompt across multiple configured models in isolated Git worktrees, streams side-by-side tool traces and results, and commits the candidate the user adopts for later rounds.
- [dsh-agent-arena](https://github.com/LeemanCheung/dsh-agent-arena) - Compares coding agents in isolated Git worktrees with deterministic validation, scoring, and explicit winner application.
- [xiehuan123/coding-coach](https://github.com/xiehuan123/coding-coach) - Coding Coach: 35-skill bundle plus a full agent preset for non-developers (8-stage idea-to-launch pipeline; engineering/product/UI skills).
- [dsh-collaboration](https://github.com/Socialist-Sister/dsh-collaboration) - Multi-agent collaboration suite: user-configured specialist roster, persistent on-demand dispatch (team_call/team_message/team_status/team_close), clone instances, star-topology relay, model comparison and a multimodal vision bridge.
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) - Planning-first agent preset: research repository changes into traceable Markdown plans, refine them through reviewer/criticizer subagent rounds, then execute as a DSH goal with a verifier checklist.
- [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) - Persistent multi-model squads managed in Settings and selected in the Composer; the lead Agent dynamically plans bounded DAG runs with optional review/repair, while Run Center reports DSH's official provider-reported Token usage.
- [DSH Automation Center](https://github.com/usersx/dsh-automation-center) - Workspace automation center for scheduled Agent runs: each execution starts a fresh Result Session with persistent audit history; stock DSH uses a Conversation tab, while compatible Shell slots enable a global page.
- [Knotline](https://github.com/MrMaii/knotline) - Visual DSH project map for composing persistent agent workflows from requests, agents, skills, backlogs, approval pools, and scheduled triggers.
- [cleverer-dsh](https://github.com/Classicoke/cleverer-dsh) - Execution-discipline suite for DSH with identical-retry interception, forced reflection, todo enforcement, memory deduplication, and experience-to-skill promotion (11 plugins + 6 skills).
- [february2015/dsh-taskswarm](https://github.com/february2015/dsh-taskswarm) - DSH port of TaskPlane: dependency-ordered waves run in parallel git-worktree lanes, with task packets, cross-model review, and crash recovery.
- [hongyue0721/dsh-kimicode-swarm](https://github.com/hongyue0721/dsh-kimicode-swarm) - Kimi Code Swarm-style batch parallel subagent dispatch: a `swarm_batch` tool fans independent subtasks out to real subagents with two-stage adaptive concurrency (ramp-up plus collision-driven exponential backoff, auto shrink/recover), an in-chat live progress stream (SSE), and `resume_agent_ids` continuation.
- [timwhitez/dsh-self-evolving](https://github.com/timwhitez/dsh-self-evolving) - Evidence-first, crash-resumable self-evolution engine for DSH: generates bounded Cordis plugin candidates, admits them through a one-shot real Loader, evaluates with Harbor, and journals an auditable lineage.
- [Saktawdi/dsh-ha-orchestrator](https://github.com/Saktawdi/dsh-ha-orchestrator) - Model high-availability failover (quarantine, circuit breaking, probe recovery) plus subagent orchestration (fanout/pipeline/supervisor) with a bilingual settings UI.
- [dsh-background-agents](https://github.com/PerryLink/dsh-background-agents) - Durable background child agents on the official subagent seam: start from any session, watch progress in the Web UI sidebar, message and interrupt any time, with per-child tool scoping, persona and delegation-depth caps.
- [dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms) - Persistent, cross-session multi-agent team rooms for DeepSeek Harness: members, a message bus, a shared task board, approval-gated handoffs, and a shared timeline that survive restarts.
- [zoahdev/dsh-kirocrew](https://github.com/zoahdev/dsh-kirocrew) - Bridge a DSH agent to a persistent, self-evolving KiroCrew development workspace over ACP (JSON-RPC 2.0 over stdio) via a single `kiro_send` tool.
- [bpc-oss/dsh-routed-subagent](https://github.com/bpc-oss/dsh-routed-subagent) - Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, model pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions.
- [bpc-oss/dsh-fork-to-preset](https://github.com/bpc-oss/dsh-fork-to-preset) - Fork any session into a different agent preset from the conversation header: a preset picker creates a new child session mounted on the chosen preset, inheriting the source session's completed turns.
- [qwert702/dsh-commander](https://github.com/qwert702/dsh-commander) - Commander mode for DSH Web: inject protocol briefs into the session title bar, parse task blocks from model replies and auto-execute them, separating strategy from execution; activated via a badge button.

- [dsh-product-subagent-console](https://github.com/Jokasa7/dsh-product-subagent-console) - Conversation-level multi-agent workbench for editable task planning, real child-session observation, plan-versus-runtime comparison, and evidence-backed recovery previews; tested with DSH 0.1.1-rc.2.

- [weibaohui/dsh-continue](https://github.com/weibaohui/dsh-continue) - Auto-resume for interrupted agent sessions: an ordered rule table routes by failure type (rate limit, quota, auth, context overflow, crashed orphan) into backoff retry, model switch, resume after compaction, or stop-loss notification, with a visual rule editor and activity log.

- [weibaohui/experts-management](https://github.com/weibaohui/experts-management) - Expert manager: manage ntd-format experts and expert teams (plugin.json + Agent MD + skill sets), browse and install from a built-in market of 50+ experts, and run tasks in an expert persona via /expert-<name> without consuming model directory tokens.
- [weibaohui/dsh-tasks](https://github.com/weibaohui/dsh-tasks) - Scheduled tasks: run a prompt on cron schedules, each run opens a new agent session to do the work, with workspace binding, manual run, session auto-naming, and a fullscreen task management page.

- [weibaohui/dsh-smart-title](https://github.com/weibaohui/dsh-smart-title) - Generates session titles from user and assistant messages using a separate LLM request with a configurable input budget; refreshes after completed turns, preserves manual titles, and skips subagent and fork sessions by default.
- [jigjoy-ai/baro-dsh](https://github.com/jigjoy-ai/baro/tree/main/packages/baro-dsh) - Baro as a subagent provider: delegate a multi-story goal and get a plan, parallel coding agents, independent per-story review and a verified outcome (tests run, goal invariants attested, merged commits), with a live run panel (phase, stories, milestones) in the sidebar.
- [zuoyunlai/lunheng-article-pipeline-dsh](https://github.com/zuoyunlai/lunheng-article-pipeline-dsh) - Long-form writing pipeline bundle: nine independent roles (literature, data and case retrieval, analysis, drafting, critique, audit, final check, peer review) across six phases with four human checkpoints, triangular evidence verification, a 23-check mechanical final gate, a G0-G14 audit, and peer-review scoring with journal matching. Install: `dsh plugin add lunheng-article-pipeline`.
- [pure-craft/dsh-actions](https://github.com/pure-craft/dsh-actions) - Deterministic project actions shared by people and agents: one layered actions.json (global/workspace/session) served as a right-sidebar run panel and six agent tools, with parameter inputs, approval gates (never/agent/always) and `@actions:` references.

- [weibaohui/dsh-process](https://github.com/weibaohui/dsh-process) - Process management: brings ntd-style processes (multi-stage, multi-step agent workflow templates) into the dsh web UI — browse, edit, validate, import/export and AI-generate processes; the built-in library is read-only while the personal library is writable with live file sync, and agents read the library through process_* tools and advance work stage by stage.

- [Awoodwhale/dsh-agent-persona](https://github.com/Awoodwhale/dsh-agent-persona) - System-prompt personas scoped by workspace or session: one persona can cover several workspace directories and several sessions, matched exactly, by prefix, by substring or by regex, most specific wins, and one persona can be marked as the default; managed from a settings page and a 「人设」tab on the conversation, effective on the next message.
- [weibaohui/dsh-thinktank](https://github.com/weibaohui/dsh-thinktank) - Applies selected mental models to a question in parallel and combines findings, disagreements, blind spots and action items into a report; supports automatic analysis and prompt-based import.
- [dsh-zh-thinking](https://github.com/yingjian666/dsh-zh-thinking) - Host plugin that adds Simplified Chinese instructions to the system prompt for planning and tool-call reasoning.

- [kotinder/dsh-roomcomm](https://github.com/kotinder/dsh-roomcomm) - Connects DSH to shared multi-agent rooms on roomcomm.xyz through a remote MCP server and a coordination skill.

- [cckyros/goal-acceptance](https://github.com/cckyros/goal-acceptance) - Acceptance-criteria goal gating: verifiable criteria locked up front, dependency-aware task plans, reviewer-confirmed completion, plus a headless check/status CLI for agent loop hooks (18 MCP tools).
- [xingzhen199186/dsh-advisor-group](https://github.com/xingzhen199186/dsh-advisor-group) - Consults multiple advisor models in one tool call, with auto-deepen follow-up rounds and a streamed chat card.

## Context & Search

- [ymck-x/dsh-session-continuity](https://github.com/ymck-x/dsh-session-continuity) - Injects a small continuity pointer at the start of a new session, naming the previous session and any handoff file, and reuses DSH's own compaction summary when there is no handoff file.
- [zoahdev/dsh-github-intelligence](https://github.com/zoahdev/dsh-github-intelligence) - Read-only developer-intelligence tools across 16 ecosystems (GitHub, GitLab, Gitee, npm, PyPI, crates.io, Docker Hub, Hugging Face, Hacker News, Stack Overflow, Reddit, dev.to, RubyGems, NuGet, Go, ArXiv) with TTL caching and no API key.
- [youdotcom-oss/dsh-plugin-youcom](https://github.com/youdotcom-oss/dsh-plugin-youcom) - You.com web search and page-fetch providers for DeepSeek Harness, returning source lists and extracted page text through a configurable API key and endpoint.
- [dsh-hacker-news](https://github.com/heartleo/hn-cli/tree/main/plugins/hacker-news) - Live Hacker News feeds, item threads, Algolia search, and user profiles for DeepSeek Harness.
- [dsh-minimal-first-turn](https://github.com/ZRui-C/dsh-minimal-first-turn) - Minimal-compatible first-turn conditioning for Web root sessions: restricts the prompt and tool catalog to persistent bash and str_replace_editor, then restores the selected preset after the first tool call or reply; includes a persistent composer toggle.
- [xiehuan123/dsh-deepread](https://github.com/xiehuan123/dsh-deepread) - DeepRead: deep-reading assistant with five modes (quick/deep/knowledge-map/Feynman reading/book), batch comparison, budget preflight, transparent background-job progress, WeChat links, local PDF (pure-JS extractor), optional MD/FreeMind/HTML export.
- [dsh-context](https://github.com/bowenliang123/dsh-context) - Context insight panel: see what the model's context window is made of and how it evolves — composition vs. window size, per-request history, compression/injection events, and per-message token stats.
- [dsh-bookmarks](https://github.com/penguin-oo/dsh-bookmarks) - Bookmark finalized assistant replies with notes and tags; a cross-session center with search, tag filter, session jump and one-click Markdown export (Alt+B toggles the panel).
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) - Model-driven context compression (ACP) for DeepSeek Harness, ported from billion-context-pi; the model decides when and what to compress.
- [qwert702/dsh-context-compressor](https://github.com/qwert702/dsh-context-compressor) - Context compression for small models: compresses tool output and conversation history to a few sentences, freeing context for the actual task; continues in a fresh session automatically.
- [dsh-scope](https://github.com/helloxkk/dsh-scope) - Context lens: per-session KV cache hit rate and token composition, plus a GitHub-style usage heatmap of daily tokens, sessions, and cache efficiency.
- [dsh-compressor](https://github.com/lifeodyssey/dsh-compressor) - Slim port of Headroom: compresses tool output, cuts up to 20% of context, without affecting the model's context cache or agent performance.
- [context-vista](https://github.com/GooodWei/context-vista) - A right-side floating panel and /context command for DeepSeek Harness — a live donut chart of context token usage, allocation, and estimated cost.
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) - See exactly what every request carries: token cost of the AGENTS.md chain, skill catalog and tool schemas, with duplicate/conflict detection and actionable pruning tips (Web UI gauge + context_audit tool).
- [dsh-mcp-lens](https://github.com/labmimors/dsh-mcp-lens) - Progressive-disclosure MCP gateway that searches large remote tool catalogs through two stable interfaces, then calls selected tools with exact schemas, lazy connections and bounded caches.
- [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) - External Summary-CoT plugin workspace.
- [qwert702/dsh-token-viewer](https://github.com/qwert702/dsh-token-viewer) - CC Switch-style token consumption statistics: per-request usage log, real-consumption hero with cache-hit rate, trend chart, per-model peak/off-peak pricing, per-project stats, and account balance.
- [dsh-explain](https://github.com/dsh-external/dsh-explain) - Learning mode that explains each agent step (WIP).
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) - Incremental file mounting with read dedupe: mounted line ranges are never re-sent to the model, on-disk changes invalidate and remount, with a Mounted Files tab and token-savings accounting.
- [dsh-session-search](https://github.com/dsh-external/dsh-session-search) - Index-free read-only search across dsh/Codex/Claude Code/pi/OpenCode sessions.
- [cross-harness-cite](https://github.com/dsh-external/cross-harness-cite) - Cite past conversations across harnesses.
- [task-passport](https://github.com/dongsheng123132/task-passport) - Carry durable task state across DeepSeek Harness, WorkBuddy, Claude Code and Codex with machine-readable checkpoints and optimistic locking.
- [dsh-easy-ctx-manager](https://github.com/dsh-external/dsh-easy-ctx-manager) - Context management: context saving and more (cordis).
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) - Zero-config Exa web search provider: keyless anonymous MCP fallback (mcp.exa.ai/mcp) plus keyed REST search, for the ctx.web seam.
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) - Persistent enhanced web search for DSH: multi-engine routing (DeepSeek/Exa/DDG/Bing/Jina + GitHub/Bilibili/YouTube/V2EX/Xiaohongshu/Twitter/Reddit/RSS), SQLite+LRU cache, userscript-style extraction, Playwright rendering.
- [dsh-free-web-search](https://github.com/delef/dsh-free-web-search) - Free web search with 10 engines (Bing/DuckDuckGo/SearXNG/AnySearch free + Exa/Tavily/Keenable/Perplexity/DeepSeek paid), automatic fallback chain, time-filtered advanced search, platform search (GitHub/Reddit), web page fetching, LRU caching, and a settings UI. No API keys required for basic use.
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) - Tavily search with multiple API keys, key rotation/failover, usage gauge, and a settings card for DSH.
- [dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) - Cross-device session sync: a dedicated git mirror with append-only keep-both conflict resolution, a /sync command and sync_status/sync_pull/sync_push tools.
- [JohnXu22786/context-pruner](https://github.com/JohnXu22786/context-pruner) - Session context triage for dsh: prunes stale, repeated, failed and oversized context to save token budget.
- [Kaixxrua/dsh-aigc-radar](https://github.com/Kaixxrua/dsh-aigc-radar) - Search AIGC Radar's curated GitHub AI project library (500-star admission, bilingual tags, star-growth snapshots) over its MCP endpoint with native result cards; a pre-step listener nudges a reuse check before the agent writes code.
- [dsh-context-budget](https://github.com/d3vmeh/dsh-context-budget) - Keeps a local model's context at a size the GPU handles well: measures prefill speed on every request and, before each step, warns or compacts early on a hard token ceiling, an observed time-to-first-token budget, or a predicted cold-prefill budget; /context-budget shows the numbers and the cost of compacting now.
- [extracurricular-ai/dsh-filesnap](https://github.com/extracurricular-ai/dsh-filesnap) - Rewind a conversation and its workspace together without touching Git; every rewind is a fork and /redo reverses it.

- [weibaohui/context-razor](https://github.com/weibaohui/context-razor) - Context trimmer: lists the current session's context entries with role, preview and ≈token estimate (cl100k), highlights over-threshold items, and removes selected entries exactly without LLM summarization.
- [huuthuan-nguyen/dsh-tgrep](https://github.com/huuthuan-nguyen/dsh-tgrep) - Ultra-fast trigram-indexed code search powered by Microsoft tgrep, shadowing the built-in grep tool.
- [dsh-context-imports](https://github.com/ciskonc/dsh-context-imports) - Claude Code-style `@path` imports for AGENTS.md/CLAUDE.md: recursively expands and injects referenced files into model context at session start, with a six-language settings card.
- [dsh-sieve](https://github.com/Sev7eEn7/sieve) - Filters tool outputs, prunes stale context and discloses skills on demand for DSH 0.2.1-alpha.1.

## Memory & Knowledge

- [diqierjia/StrataGate-AgentMemory](https://github.com/diqierjia/StrataGate-AgentMemory) - Local-first cross-session memory: L0-L5 layered short-term memory, event cards plus a knowledge graph, and evidence-gated retrieval with source tracing (npm: `stratagate-dsh`).
- [busabase/busabase-dsh-plugin](https://github.com/busabase/busabase-dsh-plugin) - Connects DSH agents to Busabase knowledge and structured data through MCP, renders records and ChangeRequests in a live inspector, and keeps agent writes behind human review; compatible with DSH 0.1.1-rc.2.
- [zilliztech/memsearch](https://github.com/zilliztech/memsearch/tree/main/plugins/dsh) - Shared Markdown memory for DSH and other coding agents, with automatic capture, pre-step context injection, searchable recall, and a review panel.

- [dsh-simple-memory](https://github.com/a903067276-rgb/dsh-simple-memory) - Sidecar markdown memory for DSH: per-session index injection, one-click memory-flow button, enforced 分类-主题.md format, cross-project search.
- [dsh-hme](https://github.com/weopenfire-git/hme-plugin) - Cross-session long-term memory: bounded core (USER.md global + MEMORY.md per-workspace, φ Fibonacci caps) + a tag-indexed, self-consolidating archive (archive/recall/move tools).
- [dsh-memory-vault](https://github.com/flymysql/dsh-memory) - Cross-session memory vault: memory_remember / memory_recall / memory_forget tools, latest entries injected into system-prompt assembly, Settings page (记忆库 / Memory).
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria) - Memoria memory backend for dsh: 4 tools (observe/remember/search/recall) into a vector+graph memory layer (memoria) with namespace isolation, auto-write (turn-end observe + positive-feedback -> importance-5 remember) and hot-reload settings.
- [dsh-memory-evolve](https://github.com/dsh-external/dsh-memory-evolve) - Cross-session long-term memory + background self-evolution (5-track memory/git-branch awareness/skill evolution).
- [qwert702/dsh-memory](https://github.com/qwert702/dsh-memory) - Project-level and global long-term memory for DSH Web: isolated POST /items route to avoid path conflicts, multi-turn tool-call context compression before storing entries, deduplication and session-persistent storage.
- [dsh-memory-gate](https://github.com/GIT121995/dsh-memory-gate) - Bounded local long-term memory with CBDC (Claim→Belief→Decision→Consumption) authority gating: SQLite + FTS5 claims, scoped dual-channel recall, /memory management commands, ≤3-claim/1200-char injection per call, no extra model call.
- [dsh-engram-relay](https://github.com/dsh-external/dsh-engram-relay) - Built-in <1B model for 100k-equivalent long memory with causal-graph wake-up.
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) - Cross-session memory engine for DeepSeek Harness: SQLite store + human-editable Markdown mirror, autoDream consolidation with self-correction, failure tracking, offline semantic search (local embedding/rerank/clustering), entity-attribute-timeline, Sleep Mode, custom-model autoSummarize — 473 tests.
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) - Mnemon-powered local memory system: three-tier memory (runtime hot memory / project Documents / long-term Memory Spaces) with supervised writeback, retrieval tools, and Web UI.
- [url-manager](https://github.com/Piccolo123/url-manager) - Agent-first URL collection & knowledge management: save links from any platform, auto-categorize/tag, full-text search, shared categories, and deliver results as magic-link cards. Zero setup — agents auto-register on first use.
- [qwert702/dsh-auto-translate](https://github.com/qwert702/dsh-auto-translate) - Auto-translates English replies inline below the original text, with Chinese annotations for tool calls; translation goes through an independent provider request and never enters the session context.
- [url-manager-mcp](https://github.com/Piccolo123/url-manager-mcp) - MCP server companion for url-manager: 21 tools (mcp__url_manager__*) for save/search/categorize/share and magic-link delivery. Stdio or streamable-http.
- [dsh-kb-sieve](https://github.com/dsh-external/dsh-kb-sieve) - Knowledge-base plugin: build auditable KB packages (references + SQL).
- [dsh-kb-rag](https://github.com/Breeze136/dsh-kb-rag) - Local literature knowledge-base RAG: 10 tools (PDF/folder/Zotero ingest, hybrid BM25+vector+reranker search, cited QA with clickable DOI links, scope/strict modes, dedup/clear/stats, DOI fetch, background-job status), all-local bge embeddings + single-file SQLite, measured 242-doc/86s ingest and sub-second hot queries on 20k chunks.
- [geometry-knowledge](https://github.com/sdoygb/geometry-knowledge) - Offline BM25 knowledge base for the Conjugate Spectral Geometry (CSG) corpus: 208 articles / 3833 chunks / 871 verified truths, 5 geo_* tools (list / search / read / calc / truth) with LaTeX→Unicode rendering, truth→article citation chains and single-character query support, zero runtime deps, `dsh plugin add geometry-knowledge`.
- [dsh-memento](https://github.com/PerryLink/dsh-memento) - Bounded, layered, approval-gated, auditable cross-session memory: typed ctx.memory seam, zero-dependency SQLite provider, memory tool and frozen snapshot injection, plus the dsh-memory-protocol v1 rehearsal with an adapter registry and a conformance suite.
- [dsh-engramory](https://github.com/tinqiao-oss/engramory/tree/master/adapters/dsh) - File-based curated memory: a line/byte-capped `MEMORY.md` index plus one markdown file per fact, versioned with git and readable without a tool. The cap is enforced through `ctx.tools.guard()` rather than asked for in a prompt, and the protocol is registered as a runtime skill; the same store is also read by Claude Code, Codex, Kiro, and OpenClaw.
- [plur-ai/dsh-plugin](https://github.com/plur-ai/dsh-plugin) - PLUR persistent memory: engrams are rendered into the system prompt on each assembly rather than sitting behind a tool call, so recall needs no round trip and the block never accumulates in context; fully local search (BM25 + BGE), plain YAML storage you can edit, per-workspace scoping, and a /plur-memory viewer.
- [dsh-memory-plugin](https://github.com/volcengine/OpenViking/tree/main/examples/dsh-memory-plugin) - OpenViking memory/context plugin for DeepSeek Harness: connects dsh to OpenViking's self-evolving context database for cross-session agent memory and knowledge RAG.
- [dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution: versioned, auditable, rollback-safe harness state (prompt notes, memories, skills, subagent specs) refined from session trajectories.
- [ccch713/deepddw](https://github.com/ccch713/deepddw) - Memory, knowledge base and document search for DSH with team member management and LAN access from PCs, phones and tablets.
- [dsh-mnemon](https://github.com/dsh-external/dsh-mnemon) - Mnemonic layer.
- [zoahdev/dsh-zh](https://github.com/zoahdev/dsh-zh) - Chinese-thinking system-prompt section: makes the agent answer in simplified Chinese while keeping code/commands verbatim.
- [memory-mcp-server](https://github.com/BingoAgentTouch/Personal_MCP) - Layered long-term memory MCP server: raw turns → task fragments → daily summaries → topic indexes, local MiniLM 384-dim embeddings or OpenAI-compatible API backend, semantic + Jaccard-fallback search, one-command DSH plugin install.
- [dsh-memory-porter](https://github.com/Shiye-10Pages/dsh-memory-porter) - Cross-vendor memory migration: zero-token import of the `memories.json` in a Claude export, local Claude Code transcripts without an export, and conversations distilled through the host's own model; every memory carries verbatim evidence checked against the source by code.
- [dsh-simple-wiki-memory](https://github.com/rainow/dsh-simple-wiki-memory) - A super-simplified LLM-wiki memory plugin: one index document (auto-loaded) + one markdown file per topic (read only when needed) — no dumping everything into the context and burning tokens. Simple and lightweight, painless to install/uninstall, and freely editable however you like.
- [dsh-library](https://github.com/PerryLink/dsh-library) - Local-first document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose; SQLite-backed index via the storage domain, local embedding, zero model downloads.
- [JohnXu22786/docs-retriever](https://github.com/JohnXu22786/docs-retriever) - DocTrove: versioned library documentation retrieval MCP server, zero runtime dependencies, installable as a dsh plugin bundle.
- [JohnXu22786/snippet-expander](https://github.com/JohnXu22786/snippet-expander) - Steno: inline #tag shorthand expansion before send — multi-library, aliases, {{variables}}, recursion guards.
- [dsh-ragflow](https://github.com/staff-os/dsh-ragflow) - RAGFlow knowledge-base retrieval plugin: gives the agent a `ragflow_retrieve` tool that queries your RAGFlow datasets and returns document chunks with similarity scores and source names; three-role design (seam/provider/consumer), env-based config, `dsh plugin add github:staff-os/dsh-ragflow#main`.
- [Mutx163/dsh-model-memory](https://github.com/Mutx163/dsh-model-memory) - Reasoning-effort tier manager for custom API models plus cross-session preference memory: inline low/medium/high/max toggles inside Settings -> Models, atomic settings.yaml persistence, and per-channel auto-restore of the last model and effort level in new sessions.
- [dsh-cortexm](https://github.com/ssmurfgg04-gif/context-m/tree/main/plugins/dsh-cortexm) - Bi-temporal memory plugin: every fact carries a transaction validity range, with VSA/HRR holographic retrieval, a BLAKE3-chained audit log, and session replay/fork; drives Context-M as a JSON-RPC subprocess (npm: dsh-cortexm, needs the Python `cortexm` package).
- [dsh-brainagent](https://github.com/stas130286-blip/dsh-brainagent) - Brain-inspired cognitive plugin: episodic / semantic / procedural / emotional memory stores with a reward-ledger and UCB1 bandit loop, a goal stack with time triggers, curiosity-driven autonomous web research, and proactive initiatives. Recalled memories ride along in the prompt to your configured provider; license is source-available, non-commercial.

- [weibaohui/hermes-loop](https://github.com/weibaohui/hermes-loop) - Automatic post-conversation retrospective that distills useful experience into reusable skills for the skill library, with approval mode and skill-library governance (archive/restore, never deletes directly).
- [dearbld/dsh-living-memory](https://github.com/dearbld/dsh-living-memory) - Self-tending living memory in one local SQLite file: nightly patrol (dedupe/merge/decay/cross-link), seven-signal RRF recall (FTS5+jieba, optional vectors, graph PPR), typed knowledge graph, conflict detection, web telemetry panels.
- [weibaohui/dsh-kb](https://github.com/weibaohui/dsh-kb) - Team knowledge base for offline knowledge sharing (FDE box scenario): browse, full-text search and refinement entry points; raw material is queued automatically and distilled into wiki pages by a serial bot session (Karpathy LLM Wiki pattern: immutable raw, two-step refinement, log stream, monthly lint).
- [loci-dsh](https://github.com/IvenKooLab/loci-dsh) - loci second-brain sidebar tab: hybrid search, cited Q&A, day-grouped memory browsing and quick capture over a local loci knowledge base; proxies `loci serve-http` same-origin from dsh-better-sidebar, no core fork.
- [dsh-statecore](https://github.com/yul761/dsh-statecore) - Auditable project memory powered by StateCore: auto-ingests messages and injects a budgeted memory digest on each pre-step (re-injected after compaction); five native tools (remember/recall/facts/why/forget) with evidence and supersession chains, embedded SQLite, and MCP access via `statecore-mcp`.


## Input & Editing

- [dsh-global-rules](https://github.com/Semidia/dsh-global-rules) - Edit your `~/.dsh/AGENTS.md` global rules from the Settings page: a text editor with save button, no command line needed.
- [dsh-keyboard-history](https://github.com/NormanFxxkingRockwell/dsh-keyboard-history) - Minimal ↑/↓ input history for the DSH web composer: press ↑/↓ to walk back through sent messages. Nothing else.
- [liustack/modlens](https://github.com/liustack/modlens) - Vision plugin for text-only LLMs: paste images for recognition, multi-image Q&A, screenshot capture, and visual task completion with one-line install.
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) - Advanced vision toolkit for DSH: OCR, grounding, multi-image Q&A, screenshot analysis, and UI restoration with structured JSON output.
- [Zhangbo-cn/dsh-voice-input-plugin](https://github.com/Zhangbo-cn/dsh-voice-input-plugin) - Composer mic for the Web UI: tap-to-monitor live transcription and hold-to-talk, with host Edge TTS reply reading that streams while the model generates, echo-pause during reading, and tap-to-stop.

- [dsh-better-sidebar-plugin-office](https://github.com/dsh-external/dsh-better-sidebar-plugin-office) - Office integration for DSH-better-sidebar.
- [dsh-message-edit](https://github.com/dsh-external/dsh-message-edit) - Branch-based message editing / reroll / retry / version timeline.
- [SpookySandwich/dsh-plugin-message-edit](https://github.com/SpookySandwich/dsh-plugin-message-edit) - Edit a sent message to rewind and branch the conversation from that turn; version counter under the bubble, a turn-level version tree of the whole branch family, and ChatGPT / DeepSeek / Claude control layouts.
- [dsh-prompt-studio](https://github.com/dsh-external/dsh-prompt-studio) - Edit system-prompt sections with live preview.
- [dsh-paste-input](https://github.com/dsh-external/dsh-paste-input) - Ctrl+V paste files / drag & drop / picker.
- [dsh-reference-anything](https://github.com/Chael-Chael/dsh-reference-anything) - Extends the native DSH `@` menu with five configurable source groups: commands, skills, workspace files, DSH sessions, and ChatGPT/Claude/Gemini/DeepSeek/Grok/Kimi conversations; external bodies and attachments are read on demand with per-task authorization.
- [dsh-voice](https://github.com/motongv/dsh-voice) - Voice input (speech-to-text) and read-aloud (Edge neural TTS) for the composer.
- [dsh-drag-and-drop](https://github.com/dsh-external/dsh-drag-and-drop) - Cross-platform drag & drop with original path insertion.
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads) - Upload arbitrary local files from the Web composer, show pending cards, and manage stored files in Settings.
- [dsh-postman](https://github.com/zhousun55-byte/dsh-postman) - Composer upload of files and folders: images attach as real message blocks, text goes into the draft, folders stored by directory structure.
- [dsh-input-history](https://github.com/dsh-external/dsh-input-history) - Input history.
- [dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input) - Multimedia file/folder input.
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) - Import full-fidelity conversation histories from 13 coding agents (Claude Code / Codex / ChatGPT / Cursor / Gemini / Reasonix / opencode / ZCode / Grok Build / OpenClaw / Pi / Hermes / Kimi) as resumable DeepSeek Harness sessions, with reverse export/sync back to Claude Code.
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) - File claim/release protection for parallel DSH sessions on the same workspace (heartbeat stale takeover, pending 3-way merge area).
- [dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) - Quick sticky notes in the composer: ideas/feelings/TODO with Markdown preview, auto-save, one-click send to chat.
- [dsh-plugin-quote-reply](https://github.com/yangYzc/dsh-plugin-quote-reply) - Select text in a conversation, then quote it into the composer or reply in a new window.
- [dsh-pathlink](https://github.com/penguin-oo/dsh-pathlink) - Ctrl+click file paths and links in chat: paths open their folder in the OS file manager (with the file selected), links open in a new browser tab.
- [@picgo/dsh-plugin](https://github.com/PicGo/dsh-plugin) - Official PicGo plugin: upload local files to your image host and get public URLs, reusing the hosts and uploader plugins already configured in PicGo.
- [dsh-suggested-replies](https://github.com/dsh-external/dsh-suggested-replies) - Suggested replies above the DSH Web composer.
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) - Persistent common-word/phrase panel beside the composer input with global/current-project buckets and one-click insert.
- [dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) - Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech).
- [dsh-dictate](https://github.com/franksong2702/dsh-dictate) - Browser Web Speech dictation for the Composer: recognition needs no dedicated ASR server, key, or model download; reuses Session text and a configured DSH model for contextual phrase hints and optional transcript polishing.
- [dsh-talk](https://github.com/PerryLink/dsh-talk) - Voice-first session loop: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt.
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) - This plugin exports a reusable function that takes a file path or a Buffer, extracts the content via @firecrawl/anydoc, and returns GitHub‑Flavored Markdown (GFM). It also includes configuration options and an example usage.
- [dsh-attachment-upload](https://github.com/lbh1nb/dsh-plugins/tree/main/packages/dsh-attachment-upload) - Composer attach button: uploads files into the workspace's .dsh-attachments directory and inserts the path into the draft.
- [dsh-steer-button](https://github.com/lbh1nb/dsh-plugins/tree/main/packages/dsh-steer-button) - Always-visible steer button in the composer: one click injects the draft into the running turn (equals Ctrl/Cmd+Enter).
- [dsh-prompt-optimize](https://github.com/peterliucius/dsh-prompt-optimize) - Rewrite the current composer draft through an auxiliary LLM call without sending a message.
- [Boliban/dsh-enter-customizer](https://github.com/Boliban/dsh-enter-customizer) - Take over the system input shortcuts for the chat input box and configure behavior independently for each shortcut.
- [PerryLink/dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) - Terminal-style input history for the web composer (edge-first arrows, draft/caret restore, Ctrl+R search, sliding-context awareness) plus a smart input layer: cross-session snippets, prompt templates with variables, reuse insights, and compaction-summary highlighting.
- [opencues/opencues](https://github.com/opencues/opencues/tree/master/integrations/dsh) - Word alternatives and underscore-gated fill-ins in the composer: end a line with `_` and it is filled, misspellings are flagged as you type. Routes through `ctx.llm`, so it needs no API key of its own.

## UI, Themes & Interaction

- [online111111/whalechan-dsh-theme](https://github.com/online111111/whalechan-dsh-theme) - Unofficial Whale-chan community fan-art theme for DeepSeek Harness Web GUI: ocean-blue styling, riding-whale branding, dedicated tool/shield icons, and in-page toggle.

- [exoticknight/dsh-just-chat](https://github.com/exoticknight/dsh-just-chat) - One-click native conversation entry points that create independent workspaces and sessions.
- [YEYEYEYESHIFU/dsh-split-screen](https://github.com/YEYEYEYESHIFU/dsh-split-screen) - Split-screen workspace: chat with several agents side by side in native-looking panes, with a compact TUI composer mode (Alt+T) and Alt+Shift+Arrow pane-focus shortcuts. Light/dark.
- [fengb3/dsh-theme-macintosh](https://github.com/fengb3/dsh-theme-macintosh) - Classic Macintosh (System 7) pixel theme: desktop pattern canvas, Finder sidebar, monochrome buttons and dialogs, light/dark support.
- [dsh-view-manager](https://github.com/runcat-tommy/dsh-view-manager) - Manage DeepSeek Harness Web GUI session view tabs (Chat / Trajectory): enable, hide, reorder and rename labels, locale-aware (zh/en), with npm update reminders.
- [sayho-pm/dsh-locale-pack](https://github.com/sayho-pm/dsh-locale-pack) - Adds UI languages and translation dictionaries to the DSH desktop app, with English fallback for untranslated strings.
- [dsh-history-question-nav](https://github.com/TropicWiden/dsh-history-question-nav) - Right-side Questions panel that lists the current session's user questions and scrolls to the matching answer.
- [dsh-chat-timeline-plus](https://github.com/NIU-001-LIU/dsh-chat-timeline-plus) - Message timeline rail with hover Q&A preview (question + reply digest card), panel pinning, day separators, and bookmarks.
- [dsh-scenery-background](https://github.com/soslowsnail/dsh-scenery-background) - Rotating Web UI backgrounds with daily and slideshow modes, five offline SVG scenes, optional Unsplash photos, glass panels, and a floating control.
- [dsh-zh-commands](https://github.com/Semidia/dsh-zh-commands) - Chinese slash-command enhancement: six new Chinese commands (/help /status /time /cwd /whoami /preset) plus in-place localization of every built-in command description in the slash menu.
- [dsh-skin-studio](https://github.com/LeemanCheung/dsh-skin-studio) - Local semantic-token theme editor with palette extraction, WCAG auditing, preview, and export.
- [deepseek-harness-zh-tw](https://github.com/chiyulogg-commits/deepseek-harness-zh-tw) - Traditional Chinese (Taiwan) locale edition of DeepSeek Harness: adds a third UI language option with Taiwan terminology across all 25 web UI packages.
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) - Keyboard-first command palette for DeepSeek Harness Web.
- [dsh-sticky-disclosure](https://github.com/Han-1413141/dsh-sticky-disclosure) - Pins off-screen expanded Think/tool/command labels to the top of the DSH Web conversation and collapses every expanded section in one click (custom hotkey).
- [dsh-better-model-selector](https://github.com/Khellendros97/dsh-better-model-selector) - Splits the composer model selector into a searchable, favorite-marking dropdown and a reasoning-effort slider, with Ctrl+P / Ctrl+T quick-switch shortcuts.
- [dsh-catppuccin](https://github.com/zhijun-dai/Catppuccin-dsh-theme) - Catppuccin theme plugin: Latte / Frappé / Macchiato / Mocha skins for the DSH Web theme runtime.
- [dsh-appearance](https://github.com/Semidia/dsh-appearance) - Unified appearance coordinator: theme color presets, UI fonts, UI font size, plus per-workspace markdown font size / line-height / background, with a coordination layer that stops UI scaling from leaking into chat body text.
- [solarized-dsh-theme](https://github.com/zhijun-dai/Solarized-dsh-theme) - Solarized + Selenized theme plugin: four faithful palettes registered into the DSH Web theme runtime.
- [arcana](https://github.com/GooodWei/arcana) - A floating command deck that lists every slash command in DeepSeek Harness as runnable buttons, sorted by usage.
- [dsh-aigc-canvas](https://github.com/dsh-external/dsh-aigc-canvas) - AIGC canvas plugin (cordis).
- [pbr-render](https://github.com/dhb861832993-star/pbr-render) - PBR 3D model preview for game art: GLB/GLTF with textures, IBL environment, orbit controls, and a material channel inspector (baseColor/normal/roughness/metallic/AO/emissive/wireframe) via the pbr3d fence and pbr_render tool.
- [dsh-deepcel](https://github.com/dsh-external/dsh-deepcel) - Deepcel spreadsheet skin and standalone distribution.
- [dsh-diff-viewer](https://github.com/dsh-external/dsh-diff-viewer) - PiUI-style Web diff viewer replacing the default diff view.
- [dsh-mobile](https://github.com/dsh-external/dsh-mobile) - Mobile client plugin (cordis + dsh.plugin.json).
- [dsh-openpencil](https://github.com/dsh-external/dsh-openpencil) - OpenPencil design preview and editing plugin.
- [dsh-design-studio](https://github.com/Sal7one/DSH-Design-Studio) - Design Studio tab: design briefs become html/css/js mockups with live preview, element picker, design-agent chat with vision review, identity presets and zip export.
- [dsh-ultra-ui](https://github.com/dsh-external/dsh-ultra-ui) - Ultra UI plugin (cordis).
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) - DSH Web output modes with Verbose, Normal, and Summary views, semantic grouping for tool calls and thinking, and live execution status.
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) - Steam Workshop-style in-app plugin browser: search, hot/newest/trending windows, Chinese keyword mapping, bilingual translation, plugin-signature filtering, and smart one-click install/update/uninstall with an installed-plugins manager.
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) - Isolated web page previews with element annotations and visual adjustments that guide source edits.
- [dsh-markdown-preview](https://github.com/GitHubJiKe/dsh-markdown-preview) - In-chat preview for produced files: click a produced-file chip to render Markdown (markdown-it + highlight.js), images, or plain text in the conversation, with system-app open kept one click away.
- [dsh-i18n](https://github.com/Semidia/dsh-i18n) - Chinese localization for tool results: intercepts tool execution output and translates English markers (`[exit code]`, `[timed out]`, `[sandbox: ...]`, etc.) into Chinese, with a settings toggle.
- [dsh-settings-tuner](https://github.com/Semidia/dsh-settings-tuner) - System parameter adjustment UI: grouped settings page for timeouts, parallelism, LLM retry policy, model params, web search, permissions and presets; safe profile-config editing with line-level YAML matching and post-write validation.
- [dsh-workspace-menu](https://github.com/0imzero/dsh-workspace-menu) - Workspace/chat context menu for the DSH home page: pin, rename, open in file explorer, archive, fork, copy, and open in a new window.
- [dsh-mobileweb-adapter](https://github.com/dsh-external/dsh-mobileweb-adapter) - Mobile/PWA layout adaptation + LAN WebSocket fix.
- [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) - Split panes.
- [dsh-skins](https://github.com/dsh-external/dsh-skins) - Web UI skins.
- [dsh-skin](https://github.com/KinGao294/dsh-skin) - Codex-style skin switcher + custom wallpaper for the Web UI: curated --dsw-alias-* palettes and a translucent wallpaper layer with opacity/blur controls.
- [dsh-chat-thumb](https://github.com/dsh-external/dsh-chat-thumb) - Chat thumbnails (cordis).
- [show-bash-command](https://github.com/dsh-external/show-bash-command) - Show actual command content instead of descriptions.
- [turtle-ui](https://github.com/dsh-external/turtle-ui) - Official UI plugin reference implementation.
- [@zhaoolee/dsh-notes](https://github.com/zhaoolee/notes) - Export DSH conversations as Smartisan Notes-style PNGs, or create and update Markdown notes in a configured account-scoped workspace.
- [dsh-plugin-description](https://github.com/MysaDC/dsh-plugin-description) - Adds bilingual (zh/en) descriptions to every plugin card on the Web Settings plugin list; publishes a `pluginDescriptions` service for other plugins to register their own.
- [dsh-plugin-list-plus](https://github.com/yibiner/dsh-plugin-list-plus) - Trust-tiered, collapsible plugin list with comprehensive per-plugin details for Web Settings.
- [dsh-premium-themes](https://github.com/xiaoyanzi191/dsh-premium-themes) - 8 curated color schemes plus custom palette import (name + scheme + seed colors derive a full token map), a Palette row in General settings, hot-plug install.
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) - Human-readable catalog for official DSH Web built-ins with status explanations and an audited set of safe UI toggles.
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) - Clickable file paths in DSH replies: Codex-style inline open, 📂 reveal in file manager, and a mentioned-files chip list at the turn tail.
- [dsh-plugin-colorscheme](https://github.com/Civitasv/dsh-plugin-colorscheme) - Web UI colorscheme plugin: switch and persist themes from Settings, with 8 built-in open-source presets plus custom themes.
- [dsh-plugin-setting-mcp](https://github.com/Ceelog/dsh-plugins/tree/main/src/plugins/dsh-plugin-setting-mcp) - Manage MCP servers from the Web settings panel, with add, edit, remove, enable/disable and hot reload on save.
- [dsh-theme-plugin](https://github.com/BeiZi6/dsh-theme-plugin) - Theme studio for the DSH Web GUI: five built-in presets plus fully customizable light/dark palettes (accent, background, foreground, UI and code fonts, translucent sidebar, contrast), hot-swapped instantly and persisted in localStorage.
- [dsh-plugin-smooth-stream](https://github.com/SpookySandwich/dsh-plugin-smooth-stream) - Better streaming text animation for DeepSeek Harness.
- [dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) - Silky streaming reveal for the Web UI: text appears at the model's arrival rate, new lines glide in, no flicker; follow stays with the user and respects prefers-reduced-motion.
- [dsh-whale-switch](https://github.com/bowen507/dsh-whale-switch) - Minimal on/off loop: a desktop shortcut launches dsh web, and an animated whale button (hover to arm, click to dive) shuts it down gracefully and closes the tab.
- [dsh-homepage-skin](https://github.com/yushi-xxh/dsh-homepage-skin) - Brings the DeepSeek Harness homepage background to DSH Web: WebGL fluid light, dot-line grid and a digital whale, with dark and light palettes.
- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) - Realtime WebGPU ocean skin with lower-left controls for waves, daylight, glass opacity and automatic day cycling; tested on DSH Web 0.1.0-rc.6.
- [dsh-plugin-help](https://github.com/Semidia/dsh-plugin-help) - Installed-plugins README summary panel: floating 📖 button, zh-preferring titles, default-all-expanded READMEs, blue circular index badges, per-plugin one-click update (`dsh plugin update`) via a loopback endpoint.
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) - MCP management console for the official DSH MCP client: server CRUD with approval-gated, backed-up profile writes, a tool trial console through the official tool pipeline, health diagnostics, and connection status.
- [dsh-session-pin](https://github.com/PerryLink/dsh-session-pin) - Pin sessions and workspaces to the top of the sidebar with per-pin colors, plus a navigation organizer: boards, tags and saved views, health summaries, and /goto.
- [RevolutionLA/dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) - One-command skinning for DSH Web: 8 original themes, wallpaper (opacity/blur/gradient/URL), per-user accent, and shareable theme packs + favorites + surprise-me. Purely native token system.
- [dsh-workspace-sort](https://github.com/Moonshile/moonshile-dsh-plugins) - Re-sorts sidebar workspaces by last activity once per day; stable order within the day.
- [dsh-theme-manager](https://github.com/runcat-tommy/dsh-theme-manager) - Two-level theme manager for the DSH Web UI: pick a culture / scene, a national flag, a developer palette, or a bold high-contrast pairing first, then a concrete style (58 built-in palettes, light & dark).

- [weibaohui/dsh-settings-ui](https://github.com/weibaohui/dsh-settings-ui) - Customizes the DSH native settings window: preset or custom sizes, fullscreen, background transparency, and theme, solid-color, or image backgrounds, with a floating ball for quick access; saved in the local browser.
- [rex178178/dsh-turnbar](https://github.com/rex178178/dsh-turnbar) - Video-style turn navigation for the DSH Web UI: a full-map progress bar (150+ turns aggregate into ≤40 groups), hover preview cards (first lines, tool calls, file edits, token usage), drag scrub, ⌘K search across the whole session including history beyond the loaded window, ⌘↑/⌘↓ stepping and Esc-return.
- [dsh-tool-indent](https://github.com/Asheep233/dsh-tool-indent) - Indents every tool call in the Web conversation, with a settings page for tool/thinking summary indent, dimming, and line spacing.
- [qiweiii/dsh-brand-studio](https://github.com/qiweiii/dsh-brand-studio) - In-app branding panel for the DSH Web and Desktop UI: brand name and badge, local logo and wordmark images with size and rounding, live preview, optional page title, and reset to the official look.
- [dsh-ui-hub](https://github.com/Han-1413141/dsh-ui-hub) - Search, show, hide, move, resize and arrange plugin controls in DSH Desktop and Web, with layout backup, restore and undo.
- [zhao-guang-ai/dsh-quote-annotate-pro](https://github.com/zhao-guang-ai/dsh-quote-annotate-pro) - Selection quoting and anchored annotations with source-message navigation, turn and role labels in sent quotes, and localStorage persistence; localhost diagnostic requests are enabled by default.
- [dsh-skill-mini-manager](https://github.com/runcat-tommy/dsh-skill-mini-manager) - Minimal skill manager for DeepSeek Harness Web Settings: lists installed skills with summaries, sources and disk usage, and moves eligible filesystem skills to a recoverable trash while protecting bundled and system skills.


## Dashboards & Session UX
- [dsh-workspace-mover](https://github.com/PianoPrince/dsh-workspace-mover) - True in-place migration of sessions across workspaces: drag-and-drop, bulk/group merge, orphan rescue panel, workspace repoint wizard, recycle bin with restore, byte-level backup with stepwise rollback and post-move verification, plus dsh-tools agent tools (npm: dsh-workspace-mover).

- [zoahdev/dsh-timesheet](https://github.com/zoahdev/dsh-timesheet) - Turn-based time tracking from session logs: per-day/project/provider/source rollups, tool calls, failures, TTFT (CLI + `timesheet` tool).
- [zoahdev/dsh-replay](https://github.com/zoahdev/dsh-replay) - Time-travel debugger: replay, visualize, and diff a session's full trajectory from `session.jsonl.zstd` (zero deps, Node ≥ 22.19).
- [dsh-session-cluster](https://github.com/dsh-external/dsh-session-cluster) - Session clustering.
- [session-chatlog](https://github.com/dsh-external/session-chatlog) - Session chat logs.
- [dsh-session-archive](https://github.com/lbh1nb/dsh-plugins/tree/main/packages/dsh-session-archive) - Settings section to view archived sessions and permanently delete dead conversations (two-step confirm, running sessions locked).
- [dsh-plugin-no-workspace](https://github.com/SpookySandwich/dsh-plugin-no-workspace) - Standalone workspace-free conversations with lossless detach and direct top-level sidebar rendering, without replacing DSH's native workspace UI (npm: dsh-plugin-no-workspace).
- [dsh-office](https://github.com/dsh-external/dsh-office) - Office file read/write bundle: model edits Office files, docx/pdf preview in web client.
- [dsh-token-pet](https://github.com/pk7j7sqryy-ops/dsh-token-pet) - Cute token-usage pet in the session header: live context occupancy, per-session usage and breakdown, plus date/weekday, weather, 3-day forecast and severe-weather alerts, all theme-aware.
- [dsh-token-usage](https://github.com/jiamuAi/dsh-token-usage) - Codex-style token usage panel: whole-instance cumulative/per-session peak tokens, longest chat & streak, daily/weekly/cumulative activity heatmap, and plugin/skill Top5.
- [dsh-office](https://github.com/Fayelin12/dsh-office) - Office workspace & session dashboard for DeepSeek Harness (DSH): a floating 6-column sprite panel visualizing workspaces, sessions, token usage and subagents — plus Agent Mail, Feishu/Lark message feed, meeting schedules, transcripts and an office log tab.
- [dsh-deepseek-quota](https://github.com/yingjunnan/dsh-deepseek-quota) - DeepSeek API balance in a bottom-right floating card on the DSH Web page (auto-refresh + manual refresh).
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) - Pin assistant replies from the Web action strip and recall them into the next model turn (`/pin` `/recall`, with optional wake).
- [dsh-turn-navigator](https://github.com/dsh-external/dsh-turn-navigator) - DSH Web turn navigation plugin.
- [dsh-fork-graph](https://github.com/chouyong/dsh-fork-graph) - Git-style conversation fork graph in the session header: colored lanes and fork curves show which session branched from which, with click-to-jump navigation.
- [dsh-session-tree](https://github.com/ZhengQingJing/dsh-session-tree) - Read-only session lineage tab for DSH Web: browse the current root, fork, and subagent family as a bounded tree and click any node to navigate.
- [chouyong/dsh-branch-review](https://github.com/chouyong/dsh-branch-review) - Track human decisions for related DSH session branches: keep, discard, or follow up with reasons, labels, and external links.
- [dsh-fork-diff](https://github.com/chouyong/dsh-fork-diff) - Read-only parent and sibling branch comparison in DSH Web: message and tool diffs, usage and latency summaries, filters, and open-session navigation.
- [dsh-usage](https://github.com/Huasecc/dsh-usage) - DeepSeek account-wide usage & balance panel from the official platform API (api/v0/usage/by_api_key): cache hit/miss & output tokens, cost, 24h–90d ranges, persistent platform token, and a model-visible `deepseek_usage_query` tool.
- [dsh-usage-panel](https://github.com/AlfredChaos/dsh-usage-panel) - Token usage statistics as a Settings page: cumulative KPIs aligned with the visible session list, a six-month activity heatmap, stacked per-model daily bars, a model donut, top sessions and JSON/CSV export; incremental projection over session logs with fork/seed history deduplication, strictly read-only.
- [fancr-code/dsh-plugin-usage-meter](https://github.com/fancr-code/dsh-plugin-usage-meter) - Usage/cost/balance meter in the composer dock: button-style chip with live peak/off-peak pricing tags, today/last-7-days per-model stacked bar charts, budget alerts, and a persistent cross-session ledger.
- [dsh-what-changed](https://github.com/sjh9714/dsh-what-changed) - Session-wide file change review in the session header. Lists every file the agent wrote this session with its hunks, counts refused writes separately from changes, and folds from a session projection rather than the on-disk log.
- [dsh-token-usage-dashboard](https://github.com/solstice621/dsh-token-usage-dashboard) - Codex-style token usage dashboard: five stat cards, GitHub-style activity heatmap (daily/weekly views), insights & model ranking; persisted snapshot with incremental sync, survives session deletion.
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) - RMB/USD token billing for the DSH web: official-policy auto pricing (incl. peak/off-peak hours), per-message cost ledger, account balance, locale-driven currency display.
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) - DeepSeek account balance and session cost in the DSH Web composer dock (auto-fetched official pricing, peak/off-peak support).
- [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) - Per-session and daily API cost, budget with usage %, official balance, history dashboard, and one-click official price sync with peak/off-peak pricing.
- [TokenLedger](https://github.com/zh667/TokenLedger) - Local DSH token usage by relay site, project, and model, with account balances and subscription quota windows.
- [dsh-budget](https://github.com/PerryLink/dsh-budget) - Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, session/daily/monthly budget caps with threshold alerts and alert/block/degrade over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command.
- [Phant0Meow/dsh-meow-cachebilling](https://github.com/Phant0Meow/dsh-meow-cachebilling) - Per-round cache billing inside the composer context-meter popover: what the current call spends on cache hits, misses, and output in CNY, with automatic official peak/off-peak and per-model pricing; hidden on non-official DeepSeek routes.
- [dsh-cost-meter](https://github.com/Sttrevens/dsh-cost-meter) - Per-turn USD cost in the Web UI: session total in the header and per-turn cost in each message footer, with a hover breakdown (token usage × configurable pricing table).
- [dsh-linked-folders](https://github.com/Sttrevens/dsh-linked-folders) - Multi-folder workspace: a global linked-folders list plus per-session on-the-fly linking (link_folder/unlink_folder), managed from the Web sidebar.
- [dsh-plugin-cost](https://github.com/yweilai77-dev/dsh-plugin-cost) - Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh).
- [dsh-balance-tide](https://github.com/huanyuLv/dsh-balance-tide) - DeepSeek account balance and session cost under the composer, with a live peak/off-peak pricing badge (Beijing time), a countdown to the next pricing switch, and hover price tables with usage advice.
- [dsh-spend](https://github.com/nonewind/dsh-spend) - Token usage and estimated spend for the DSH web UI: floating panel with per-model / per-day / per-session stats and auto-detected billing plans.
- [dsh-worktime-board](https://github.com/spacexun2/dsh-worktime-board) - Agent worktime dashboard: floating day/week/month stats, multi-dimension heatmap, thread attendance Gantt, school-year calendar, and a 12-realm xianxia score system for agent activity.
- [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) - Live token estimates and generation TPS.
- [dsh-tps](https://github.com/dsh-external/dsh-tps) - TPS meter.
- [DSH-better-sidebar](https://github.com/dsh-external/DSH-better-sidebar) - Sidebar: file rendering/terminal/Git/subagents/custom APIs.
- [dsh-web-panel](https://github.com/dsh-external/dsh-web-panel) - Embedded terminal dock + Git Review + file view.
- [dsh-tmux-cc](https://github.com/adrianleb/dsh-tmux-cc) - Persistent tmux control-mode cockpit for DSH Web that mirrors native panes in a dock.
- [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) - Subagent tree visualization.
- [dsh-web-workflow-visualizer](https://github.com/dsh-external/dsh-web-workflow-visualizer) - Workflow visualization.
- [weibaohui/dsh-flow](https://github.com/weibaohui/dsh-flow) - Live execution flowchart tab for the current session: context/user/assistant/tool swimlanes with approval diamonds, subagent fan-out with double-click drill-down, and a compact list view, streamed over SSE as the session runs.
- [dsh-ui-progress](https://github.com/dsh-external/dsh-ui-progress) - Progress indicators.
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) - Right-side dot-timeline rail to jump between user messages.
- [dsh-plan-switch](https://github.com/a903067276-rgb/dsh-plan-switch) - One-click enter/exit Plan mode for the DSH web input bar, a quick-click shortcut for /plan.
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) - Turn-index sidebar: one entry per user turn, click to jump, scroll-spy highlighting.
- [dsh-outline](https://github.com/urzeye/dsh-outline) - Real-time conversation outline panel for the DSH Web session page: a tree of user questions and Markdown headings (H1-H6) that updates live while streaming, with click-to-jump highlight, expand-depth control, search, and per-session favorites.
- [dsh-conversation-anchors](https://github.com/biggerboy/dsh-conversation-anchors) - Sidebar conversation anchor navigation: one anchor per chat node (user / assistant / tool / command) with role badges and summaries, click to smooth-scroll to that message; live-refreshes with the session.
- [dsh-web-attention-badge](https://github.com/Luaphes/dsh-web-attention-badge) - Attention reminders: frame badge, tab-title count and whale-favicon recolor for sessions waiting for input or finished unopened.
- [dsh-sidebar-mode](https://github.com/Meredith2328/dsh-sidebar-mode) - Preset-mode badge embedded in the "New Session" button: click to pick the default agent preset for the next session (long names truncate with ellipsis so the label stays readable).
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud) - HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel.
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) - Auto-resumes interrupted DSH Web requests: sends a queued 「继续」 after network/timeout/host-crash failures, with error classification, adaptive backoff, templated continue text and browser notifications; everything configurable from the plugin settings card.
- [Chu-m/dsh-chat-continue](https://github.com/Chu-m/dsh-chat-continue) - Auto-retries failed API requests to keep DSH conversations running, with configurable HTTP status and error-code rules.
- [qwert702/dsh-continue-on-limit](https://github.com/qwert702/dsh-continue-on-limit) - Auto-sends continue when a local model hits its output-token cap: dual-source detection (turn-max-tokens node + provider response), maxConsecutive guard (default 3) prevents infinite loops.
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug) - Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics for DeepSeek Harness.
- [dsh-netcafe](https://github.com/mario03690/dsh-netcafe) - Hosted outcome tools bundle (MCP over one config row): md→docx/pptx/pdf, tables with in-code arithmetic checks, China-reachability testing from a real mainland vantage, Chinese calendar/holidays; free anonymous quota, per-call cost reporting.
- [dsh-opencodego-usage](https://github.com/BeiZi6/dsh-opencodego-usage) - OpenCodeGo quota monitor for the DSH Web GUI: a breathing indicator at the input's bottom-right (green/yellow/red by remaining share), a liquid-glass panel with rolling/weekly/monthly usage windows and reset times, auto-refreshing every 30 s; API key read from DSH credentials.
- [penguin-oo/dsh-quota-hub](https://github.com/penguin-oo/dsh-quota-hub) - Unified real-time quota dashboard: one collapsible glass panel for OpenCodeGo windows, DeepSeek balance, OpenRouter credits, SiliconFlow and Moonshot balances — auto-detects DSH credentials, host-side fetching (keys never reach the browser), custom providers via ~/.dsh/dsh-quota-hub.json.
- [dsh-trajectory-reader](https://github.com/flyingtimes/dsh-trajectory-reader) - A 轨迹解读 (trajectory interpretation) tab that summarizes each user round — what was wanted, how the assistant thought and executed, files/commands/errors — via a rules engine plus optional LLM narrative; user messages stay verbatim.
- [dsh-session-manager](https://github.com/Semidia/dsh-session-manager) - Right-click context menu on sidebar conversation rows: pin, rename, archive, fork, mark unread, copy cwd/id/title/deep-link, open in explorer/new window.
- [SunshineR04/dsh-session-manager](https://github.com/SunshineR04/dsh-session-manager) - Restore archived sessions or permanently delete session files from Settings and the session menu. Deletion has no backup; the UI asks for confirmation, agent tools require an explicit confirm flag, and running sessions are refused by default.
- [dsh-session-handoff](https://github.com/WeiYe6/dsh-session-handoff) - Hand long sessions over to a clean one: /handoff summarizes the conversation with an LLM, creates a new session+agent in the same workspace, injects the handoff document as the first message, and auto-opens it; the origin session stays unchanged.
- [dsh-cost-crystal](https://github.com/xxvk/dsh-cost-crystal) - Floating cost crystal for the DSH Web UI: balance card, real-time tok/s, peak/off-peak billing countdown, last-24h spend, and a 🔮 next-message cost forecast, all timezone-aware.
- [dsh-session-repair-ui](https://github.com/Semidia/dsh-session-repair-ui) - Session repair button in the conversation header: detects & fixes session-log corruption — tool-call id swaps, empty call ids (`message must have tool source`), unknown event types from disabled plugins (marks `ignorable`), torn zstd tails, missing final-frame newlines; ghost-style UI, auto-backup before writes.
- [plugin-team-board](https://github.com/whyihaveyou/dsh-suite/tree/main/packages/plugins/plugin-team-board) - Shared multi-agent task board (create / claim / transition / query) over a Cordis service key.
- [zoahdev/dsh-code](https://github.com/zoahdev/dsh-code) - VS Code extension: run one-shot DeepSeek Harness tasks (`dsh --profile headless`) from a command or panel.
- [dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) - Event-flow audit panel: event types, distribution, counts, and recent events for plugin authors.
- [dsh-session-explorer](https://github.com/Zn-Dk/dsh-session-explorer) - Message-level full-text search browser across DSH sessions (FTS5 trigram over user / assistant / steering / tool with per-kind filters), deduplicated across fork/continued sessions, read-only context preview with auto-scroll to the focused message and one-click jump to the real session, incremental/full rebuild with health check, zh/en i18n follows the Host locale.
- [dsh-whale-meter](https://github.com/Shiye-10Pages/dsh-whale-meter) - Usage tiers (🐟→🐳) with a locally-estimated percentile and shareable stats card; 46 models across 6 vendors including size-tiered Chinese pricing; backfills pre-install sessions; old-vs-new rates across the 2026-08-17 change.
- [dsh-file-upload](https://github.com/a903067276-rgb/dsh-file-upload) - One upload button plus drag-and-drop files into the conversation as local paths: save to the project's uploads/, path text into the input box, works with any vision tool.
- [dsh-bill](https://github.com/Jannchie/dsh-bill) - Cost tracking: per-turn cost line, spend attributed to tool output / model output / system prompt / commands, budget, forecast; priced per call from models.dev + OpenRouter (8000+ models) and never recomputed.
- [dsh-history](https://github.com/chenproton/dsh-history) - Browse every message you sent in the current session: full-history listing with newest-first sort, text filter, one-click copy, and click-to-jump that auto-loads earlier history when the target is not yet loaded.
- [JohnXu22786/session-titler](https://github.com/JohnXu22786/session-titler) - Two-phase session captioning for DeepSeek Harness: instant keyword captions while busy, budget-model refinement when idle.
- [dsh-billing-tui](https://github.com/Ethanz11-creat/dsh-billing-tui) - Real-time token/cost billing with official DeepSeek peak/off-peak pricing: TUI status line and a whale ASCII receipt via /billing.

- [woosh2010/dsh-usage-dashboard](https://github.com/woosh2010/dsh-usage-dashboard) - Peak/valley billing dock and usage analytics: token/cost/model stats, trend and token-mix charts, latest-20-turns records, global time/session/model filters.
- [runcat-tommy/dsh-panda-calendar](https://github.com/runcat-tommy/dsh-panda-calendar) - Panda Calendar (熊猫日历) conversation-view tab: solar/lunar dates, ganzhi, Chinese zodiac, solar terms, festivals, China public holidays incl. make-up workdays, multi-city weather, an epoch↔date timestamp converter with a time-zone picker, and bundled offline "on this day" history; free data sources, no API key.
- [dsh-session-enhance](https://github.com/Tinger-X/dsh-session-enhance) - Full-control session management for DSH Web: archive, guaranteed physical delete (tombstone anti-resurrection), drag-and-drop workspace moves, conversation notifications, copy session ID and one-click record sync.
- [dsh-capability-panel](https://github.com/pure-craft/dsh-capability-panel) - See which skills and tools your agent can actually reach right now — true in-context state (loaded/truncated/evicted) and per-session switches.
- [wjingshan/dsh-cost-gauge](https://github.com/wjingshan/dsh-cost-gauge) - Peak/off-peak billing cost dial for the DSH Web GUI: session spend and account balance computed at the official rates, a low-balance alarm, drag-to-resize and a minimized status-lamp mode.
- [weibaohui/dsh-dashboard](https://github.com/weibaohui/dsh-dashboard) - Usage dashboard: offline-scans session logs to chart daily/weekly/monthly tokens, estimated costs, model/tool/skill/command leaderboards, output speed, working hours and quality metrics; gridstack+ECharts cards are drag-and-drop composable, with custom formulas and AI arrangement (prompt round-trip import).
- [olimc2016/dsh-token-meter-panel](https://github.com/olimc2016/dsh-token-meter-panel) - Sidebar panel for token usage and cost: today's spend, budget progress, 7/30-day trends, cost breakdown, cache-hit savings, and per-session breakdown.
- [dsh-maze](https://github.com/lamost423/dsh-maze) - Execution maze for agent sessions: main path, detours and backtracks on one timeline, per-step data tracks (tools, tokens, context pressure), deterministic analysis (outcome evidence, behavior signals) and multi-session comparison.
## IDE & Clients

- [Minke](https://github.com/lencx/Minke) - Desktop agent workspace for DeepSeek Harness on macOS, Windows, and Linux, with shared browser control, integrated files and terminals, remote access, and local model management.
- [PaperMachine](https://github.com/SuperJJ007/papermachine) - Desktop data-analysis app built on DeepSeek Harness, running local Python and R with inspectable execution steps and chart/table provenance.
- [Blue](https://github.com/dsh-blue/blue) - Interactive TUI plugin for DeepSeek Harness — a pi-tui renderer mounted as a Cordis bundle: streaming transcript, tool-call cards, approval overlays, session management, theming.
- [DeepSeekGUI](https://github.com/See-Sol-Lab/DeepSeekGUI) - Windows desktop workbench with a bundled DSH runtime and app-local settings and sessions, Changes / Git / Worktrees / Memory views, approval-gated Git/PR tools, and global and project memory. Experimental Linux AppImage.
- [dsh-cc-tui](https://github.com/dsh-external/dsh-cc-tui) - Claude Code-style fullscreen TUI (streaming expand / double-Esc rollback).
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui) - TUI built with grok-build.
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) - Pi TUI (differential-rendering terminal framework) front end: streaming markdown, thinking collapse, tool cards, slash commands, approval/question overlays, shared dsh session store.
- [Martty](https://github.com/openma-ai/Martty) - DSH-first Rust/ratatui agent TUI with streamed tool calls, subagents, durable sessions, and a Cordis-extensible client UI.
- [dsh-terminal](https://github.com/geebos/dsh-terminal) - Collapsible in-conversation interactive terminal with multi-tab live shells, auto-reconnect, one-click quick commands, and a bilingual UI that follows the theme.
- [lk251066/dsh-tui-pro](https://github.com/lk251066/dsh-tui-pro) - Full-screen terminal workbench for DeepSeek Harness with a durable assistant, workspace-grouped project sessions, and structured thinking, tool, diff, plan, and subagent views.
- [DSH-Portable](https://github.com/WSL043/DSH-Portable) - Cross-platform one-folder distribution of DeepSeek Harness with a bundled runtime, plugin market, data-preserving updates, and sessions, settings, plugins, and workspace that move together.
- [deepseek-harness-desktop](https://github.com/chyra-moon/deepseek-harness-desktop) - Native Windows desktop shell: 1:1 official web UI with embedded server hosting, tray and auto-recovery.
- [Harness Desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) - Windows desktop app for the official DSH Web UI with a Chinese installer and portable build, quick themes, an in-app plugin marketplace, separate main/subagent model selection, and verified updates.
- [dsh-desktop](https://github.com/foolgry/dsh-desktop) - Download-and-run Electron desktop build (macOS/Windows installers): no Node.js or terminal needed, tracks upstream `@deepseek-ai/dsh` releases automatically, with built-in web UI and auto-update.
- [deepseek-harness-desktop](https://github.com/fendouai/deepseek-harness-desktop) - Tauri 2 desktop distribution of DeepSeek Harness with the complete Web UI, a supervised local sidecar, and a bundled Node.js 24 runtime (macOS/Linux/Windows).
- [DeepSeek Harness Desktop](https://github.com/dsh-tauri-desk/deepseek-harness-desktop) - One-click Tauri 2 desktop distribution of DeepSeek Harness: bundled runtime, no Node.js/pnpm/Docker required, native macOS/Windows/Linux packages.
- [DeepSeek Harness Desktop](https://github.com/web-casa/DeepSeek-Harness-Desktop) - Community Tauri 2 desktop distribution with a supervised local sidecar, bundled Node.js 24, native Windows/macOS packages, and a [website](https://dsharness.app).
- [DeepSeek Harness Desktop](https://github.com/chokwinlee/deepseek-harness-desktop) - Self-contained macOS/Windows desktop host for the official DSH Web UI; macOS uses Tauri/WKWebView and ships sub-90 MB DMGs with the Harness runtime bundled.
- [Paopaocat DSH Desktop](https://github.com/zmm863-commits/dsh-desktop-pack) - Windows NSIS installer that bundles Node.js and Git, preinstalls 17 plugins with the Paopaocat glass theme, and launches the DSH web UI from a desktop shortcut.
- [dsh desktop](https://github.com/MochiNek0/dsh-desktop) - Community Tauri 2 desktop wrapper for the DSH Web UI on Windows, macOS and Linux; scan a QR code to access the computer's dsh from a phone over LAN, Tailscale or Cloudflare, sharing sessions and config with the CLI.
- [dsh-vscode](https://github.com/Lixxx1/dsh-vscode) - VS Code right-sidebar client for the official DSH runtime: project and editor-selection context, permission/plan controls, queued steering messages, and native diff review.
- [zhibailu/dsh-vsc](https://github.com/zhibailu/dsh-vsc) - Native VS Code sidebar + editor bridge for DeepSeek Harness: ask about a selection, review agent changes, approval and question cards; connects to the configured DSH URL and can auto-start `dsh web` when unavailable.
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode) - VS Code chat windows backed by the DSH agent: OpenCode-style independent sessions, model auto-routing (Flash/Pro/Pro Max).
- [dsh-plugin-open-editor](https://github.com/Civitasv/dsh-plugin-open-editor) - Open the current workspace in your local editor (VS Code, Cursor, JetBrains, Vim, ...) from the session header.
- [dsh-open-with](https://github.com/ChuanTianML/dsh-open-with) - Open registered DSH workspaces from the Web UI in detected or configured local editors, terminals, or file managers, with a remembered per-browser preference.
- [DSH-for-VSC](https://github.com/yauntyour/DSH-for-VSC) - VS Code extension embedding the DSH WebUI as an editor panel: sidebar console with service status and start/stop, hidden auto-restart, status-bar indicator and run logs.
- [dsh-gui](https://github.com/xuboboo/dsh-gui) - Third-party Windows desktop client for DeepSeek Harness: native window, branded theme & splash, startup crash fixes, token usage statistics.
- [DSH Studio](https://github.com/Moresyl/dsh-studio) - Cross-platform Rust/Tauri desktop shell that supervises `dsh web`, reclaims process trees, selects free ports, and publishes Windows/Linux/macOS installers without forking the upstream UI.
- [DSH Deck](https://github.com/Socialist-Sister/dsh-deck) - Unofficial Electron desktop shell for the official DSH Web UI (same code, same data): attach-to-existing-harness mode prevents dual-writer session corruption, session-log relocated to the session row menu, tray residency, single portable exe.
- [DshCockpit](https://github.com/Lxiayu/DshCockpit) - Electron desktop cockpit for `dsh web`: tray-resident background tasks, token/cost tracking with budget alarms, runtime auto-update with rollback, Quick Ask hotkey, scheduled tasks, full-text session search.
- [deepseek-harness-desktop](https://github.com/Easyhoov/deepseek-harness-desktop) - Unofficial in-process Windows desktop app with tray residency, native notifications, and an IPC bridge.
- [dsh-shell](https://github.com/TaoSmile/dsh-shell) - Zero-install desktop shell for an already-installed DeepSeek Harness: attaches to a running `dsh web` or auto-launches it with your existing Node environment; Electron shell with tray plus a double-click Edge app-mode launcher.
- [dsh-desktop](https://github.com/xiaoyanzi191/dsh-desktop) - Electron desktop wrapper for DeepSeek Harness: double-click to start, automatically manages the dsh Web service lifecycle.
- [dsh-chat-tools](https://github.com/yj060464-commits/dsh-chat-tools) - Headless terminal companion toolkit: chat.sh continuous-conversation REPL (rolling context, decision-point voting, live workflow streaming, effort switching) + automatic LLM session-log summarization. Zero-dependency bash + Python.
- [dsh-come](https://github.com/qing3a/dsh-come) - Desktop shell for DeepSeek Harness (Rust single exe): self-bootstrapping Node, tray, autostart, plugin store.
- [dsh-launcher](https://github.com/iceleaf916/dsh-launcher) - macOS menu-bar launcher for dsh: start/stop/restart the web service, hot reload, auto-start at login, and open the UI in a system or built-in browser.

- [ccgui / desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) - Multi-engine AI coding desktop client (Tauri): Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI — not a DSH Web UI shell or `dsh-plugin`.
- [dsh-desktop-hub](https://github.com/FlashingChen/dsh-desktop-hub) - Electron desktop hub for the official DSH Web UI with a built-in MCP config converter (Claude Code / Cursor JSON → DSH YAML), Skills / Plugin management consoles, and a bundled Node.js + DSH runtime — no install, no terminal.
- [JohnXu22786/browser-automation](https://github.com/JohnXu22786/browser-automation) - Web Bridge: browser automation MCP server for dsh — real-browser navigation, click, form-fill, screenshots, JS execution, accessibility-tree snapshot driven.
- [JohnXu22786/computer-control](https://github.com/JohnXu22786/computer-control) - Desktop control for dsh: screen capture, pointer/keyboard injection, accessibility-tree semantic actions, emergency stop, allow/deny rules, confirmation flow and idle standby.
- [DSHBox](https://github.com/WSK-build/DSHBox) - Run DeepSeek Harness natively on Android: a single APK bundling a layered Debian sandbox, Node.js, DSH and a terminal — no root, no Termux; runtime layers update independently, DSH upgrades over npm, and installs are atomic dual-slot with rollback. Six-language UI.
- [dsh-native-macos](https://github.com/DanielW203/dsh-native-macos) - Native SwiftUI macOS client for DeepSeek Harness: several releases installed side by side, an 8-check self-test after each upgrade with one-shot rollback, safe-mode recovery, and a built-in WeChat/phone remote channel.
- [deepseek-harness-android](https://github.com/guzhou079-arch/deepseek-harness-android) - Android client bundling the DSH runtime and skills in an installable APK, with on-device builds and virtual-display automation; no Termux or root required.
- [DSH_Mobile](https://github.com/jayantTang/DSH_Mobile) - Native iOS client with a host-side connector and a self-hostable WSS relay: reach the DSH sessions on your own computer from an iPhone over 4G/5G, without a public IP or a VPN.

## Browser & Remote

- [mrRisega/dsh-remote](https://github.com/mrRisega/dsh-remote) - Reverse-proxy gateway to control the DSH Web UI from a phone browser with full feature coverage (incl. privileged methods): loopback masquerading, WebSocket passthrough, login rate limiting, optional TLS, LAN or public reverse-proxy deployment.
- [dsh-voice-gate](https://github.com/yangfei222666-9/dsh-voice-gate) - Voice-first mobile gate into DSH: a zero-dependency Python service (port 3081) with a PWA page that sends voice or text to the current session, token auth, launchd autostart, and a Tailscale HTTPS recipe.
- [dsh-browser-panel](https://github.com/dsh-external/dsh-browser-panel) - Headed browser embedded in the WebUI, model-driven (Codex-style, zero vision deps).
- [dsh-builtin-browser](https://github.com/wqty123/dsh-browser) - Shared real browser for DSH: a visible browser window the human can take over, driven by the agent over CDP (snapshot/execute/content/tab management).
- [dsh-browser](https://github.com/dsh-external/dsh-browser) - Chrome sidebar extension.
- [dsh-deeplink](https://github.com/dsh-external/dsh-deeplink) - Open DSH WebUI sessions or workspaces directly from URL parameters.
- [dsh-remote](https://github.com/flymysql/dsh-remote) - Multi-machine remote workspace: manage many SSH hosts, pick a local or remote workspace in the native Add-workspace flow (system folder / path browse), mirror a remote workspace to a real local folder, and operate it with rw_* tools.
- [dsh-ssh](https://github.com/jmcc-guo/dsh-ssh) - AI-managed SSH connections with a live multi-tab terminal panel for DeepSeek Harness.
- [xgone/dsh-netshell](https://github.com/xgone/dsh-netshell) - Local and remote SSH terminals for DeepSeek Harness Web, with three permission levels, rule-based command confirmation, and DSH credential storage. Guards cover commands sent through this plugin and do not provide a security sandbox.
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) - LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure (LAN HTTP) contexts (npm: dsh-lan-access).
- [xgone/dsh-remote](https://github.com/xgone/dsh-remote) - Remote access & authentication for DeepSeek Harness web UI: account/password login gate, MFA (TOTP), signed session cookies, role-based access, in-browser directory picker, and a Settings page for account management (npm: @xgone/dsh-remote).
- [dsh-dispatch](https://github.com/alextangson/dsh-dispatch) - Phone-side command center (plugin + zero-knowledge relay + PWA): dispatch tasks into isolated git worktrees from your phone, approval push notifications with phone/desktop first-answer-wins (never auto-approved), and a multi-machine session board; E2E encrypted, self-hostable.
- [ego-browser](https://github.com/dsh-external/ego-browser) - Browser agent.
- [dsh-webbridge](https://github.com/dsh-external/dsh-webbridge) - Web bridge.
- [browser4-dsh](https://github.com/dsh-external/browser4-dsh) - Browser4 AI-native browser engine (skills).
- [dsh-browser-runtime](https://github.com/anweat/dsh-browser) - Self-contained browser runtime plugin: Playwright (chromium) + OpenCLI as plugin-local deps (global reuse fallback), exposes a `browser` service and interactive browser tools.
- [dsh-computer-use](https://github.com/ZRui-C/dsh-computer-use) - Text-first computer use: background Chromium control via Playwright/CDP plus accessibility-first macOS control; actions stay pinned to the correct process and window without taking the user's pointer (Developer ID signed, notarized Universal 2 DMG).
- [dsh-adb](https://github.com/SamXiaBing/dsh-adb) - ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots.
- [zoahdev/dsh-vision](https://github.com/zoahdev/dsh-vision) - Vision analysis tool: analyze a local image or URL with an OpenAI-compatible vision model.
- [dsh-click](https://github.com/PerryLink/dsh-click) - Native desktop control for DeepSeek Harness (Windows first): screen_shot, screen_read accessibility trees, click/type/scroll/key, and app launch — approval-gated, never stealing foreground focus.
- [zoahdev/dsh-browser-use](https://github.com/zoahdev/dsh-browser-use) - Browser Use cloud bridge: run real web tasks (open pages, click, type, fill forms, extract data) through the Browser Use API.
- [sheep-programmer/dsh-web-search-free](https://github.com/sheep-programmer/dsh-web-search-free) - Free web search for DSH: anonymous Parallel default plus Exa fallback, a Settings toggle, and an MCP server compatible with Claude Code and Codex.
- [SeerableOfficial/dsh-web-search-toggle](https://github.com/SeerableOfficial/dsh-web-search-toggle) - Per-session Web Search toggle that directs the agent to search the web before answering.
- [tabbit-browser](https://github.com/Tabbit-Browser/dsh-plugin) - Drive the user's Tabbit Browser from DSH via its Browser-owned, task-isolated Playwright CLI (`tabbit-cli`): bundled `tabbit-browser` skill, ≥1.9.0 runtime preflight, region-aware installer download, and persistent named task spaces (no Chrome/Ego/CDP fallback).
- [dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) - Drive the user's Tabbit Browser from DSH via its Browser-owned, task-isolated Playwright CLI (`tabbit-cli`): bundled `tabbit-browser` skill, ≥1.9.0 runtime preflight, region-aware installer download, and persistent named task spaces (no Chrome/Ego/CDP fallback).
- [dsh-antigravity](https://github.com/LiZhenNet/dsh-antigravity) - Google Antigravity / Cloud Code Assist model provider for DSH with native Web OAuth, real-time quota tracking, and dynamic reasoning effort routing.
- [JohnXu22786/model-catalog](https://github.com/JohnXu22786/model-catalog) - Model catalog auto-discovery: fetch model listings, pricing and capabilities from OpenAI-compatible API hosts, normalized into ready-to-use config.
- [dsh-browser-vision](https://github.com/tristan-mcinnis/dsh-browser-vision) - Vision browser tool: drives real Chrome over CDP with browser-use and reads the page with deepseek-v4-flash-vision-exp, so canvas text, text baked into images and values in rendered charts are readable; returns JSON validated against a caller-supplied schema and reports per-run token cost.
- [harness-unity-bridge](https://github.com/WarrenMondeville/agents-unity-bridge) - File-based bridge that lets DeepSeek Harness control the Unity Editor: run EditMode/PlayMode tests, compile scripts, refresh assets, read console logs, control Play Mode, and build — via a deterministic Python CLI, a Unity UPM package, and an installable DSH skill (`unity-bridge`).
- [xingzhen199186/dsh-jev-ultrafast](https://github.com/xingzhen199186/dsh-jev-ultrafast) - Drive a real browser from one natural-language goal: a decision service picks each operation and element, so a DSH session spends one tool call.
- [dsh-codex-computer-use](https://github.com/Han-1413141/dsh-codex-computer-use) - Let a DSH model inspect and operate Windows applications through an installed Codex Computer Use runtime, with per-session app approval.
- [dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - Mobile web remote for a DSH session: three view modes (latest conclusion / chat / full trace with diffs), LAN, Tailscale or Cloudflare Tunnel routes with per-route QR pairing, instruction queueing and approval or question cards on the phone, plus a Feishu long-connection channel.

## Models & Inference

- [dsh-zcode-coding-plan](https://github.com/yuyang2230/dsh-zcode-coding-plan) - Dispatches coding tasks to the official ZCode CLI, with native agent tools, multi-turn resume, context caching and quota-aware routing.
- [dsh-zcode-cli-proxy](https://github.com/kyle123740/dsh-zcode-cli-proxy) - ZCode CLI app-server relay for DeepSeek Harness, with GLM streaming, image input and session reuse using an existing Start Plan login; requires the ZCode client.
- [dsh-vertex-gemini](https://github.com/mn288/dsh-vertex-gemini) - Gemini provider for DeepSeek Harness on Google Cloud Vertex AI, with Application Default Credentials, streaming, and thought-signature replay across tool calls.
- [dsh-agy-link](https://github.com/amlyczz/dsh-agy-link) - Google Antigravity (agy CLI) model provider for DSH: stream Gemini/Claude/GPT-OSS subscriptions, native tool cards, thinking turns, and in-GUI Google OAuth login.
- [dsh-baseurl-probe](https://github.com/Semidia/baseurl-probe) - Provider baseURL auto-detection: when a provider's baseURL is a bare domain (e.g. `https://mzeapi.top`) and only `/v1` serves the OpenAI-compatible API, the plugin auto-fixes it — probes all providers with zero-cost path detection (no API key needed).
- [dsh-llm-compat-healer](https://github.com/Semidia/dsh-llm-compat-healer) - LLM compatibility auto-healer for transit/gateway providers: repairs DeepSeek `reasoning_content` replay and unsupported `developer` roles without a restart, exposes pi-ai compatibility settings, and adds redacted Chinese summaries for upstream errors.
- [dsh-provider-health](https://github.com/Semidia/dsh-provider-health) - Provider health dashboard as a Settings page: read-only per-provider status, health (time-decayed from recent errors), thinking capability, max tokens and latest error, sourced from the llm-pi-ai config and the compat-healer error log.
- [dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) - Native image generation for DeepSeek Harness with Google Gemini, OpenAI Images, OpenAI-compatible APIs, and ByteDance Seedream.
- [exoticknight/dsh-labnana](https://github.com/exoticknight/dsh-labnana) - Labnana image generation for DeepSeek Harness: text-to-image / image-to-image / precise editing (NanoBanana Pro, Gemini 3.1 Flash Image, GPT-Image-2, Wan2.7, Seedream).
- [welsione/dsh-model-router](https://github.com/welsione/dsh-model-router) - Unified model routing: one logical ModelID over multiple providers with first-token failover and cooldown, health-aware candidate ranking, three tiers auto-selected by purpose, per-candidate reasoning effort, and a settings-page management panel.
- [dsh-codex-oauth](https://github.com/WNJXYK/dsh-codex-oauth) - ChatGPT/Codex subscription integration for DSH with GPT models, image generation, web search, quota reporting, and browser/device-code OAuth sign-in.
- [dsh-qwen-token-plan-cn-responses](https://github.com/nickhelion/dsh-plugins/tree/main/packages/qwen-token-plan-cn-responses) - Qwen Token Plan CN Personal Responses API provider: syncs official model and per-model built-in-tool docs, supports DSH local functions and images, and keeps a validated last-known-good catalog.
- [dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) - ChatGPT OAuth provider for DSH with Codex models, image generation, selectable subscription search, standard and Spark quota reporting, and a native settings page.
- [dsh-vision](https://github.com/dsh-external/dsh-vision) - Vision bridge: view_image tool over any OpenAI-compatible VLM (Zhipu free tier by default).
- [DeepSee](https://github.com/windyslime/DeepSee) - DSH `0.1.0-rc.5` Web-profile visual-reasoning gateway: routes image turns through local, pluggable VLM backends and leaves normal DSH text routing intact.
- [dsh-plugin-vision](https://github.com/tdf1995/dsh-plugin-vision) - Vision for text-only LLMs: image description / OCR / VQA via free Gemini and GLM vision APIs.
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - Free vision for text-only agents: built-in keyless vision chain plus pixel tools (Q&A, grounding, crop, pixel diff, colors, OCR, SVG trace, cutout, screenshots); paste an image and it just works — no Python, one-command install.
- [dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) - DeepSeek brain + automatic image transcription: GUI images are transcribed via the official deepseek-v4-flash-vision-exp by default (a pure-text V4-Pro brain can see images); any OpenAI-compatible VLM or local Ollama as alternatives.
- [DSH-Multimodal](https://github.com/yauntyour/DSH-Multimodal) - Per-file-type multimodal chains: preset processing models per wildcard convert image/video/audio files into prompt tokens before they reach the text-only session model, with per-preset fallback chains and a Multimodal settings page.
- [dsh-draw](https://github.com/PerryLink/dsh-draw) - Unified static-im