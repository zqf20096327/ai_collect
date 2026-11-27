# agy-memory

[中文版](./README.zh-CN.md)

[![CI](https://github.com/maxLWS/agy-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/maxLWS/agy-memory/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/maxLWS/agy-memory?style=flat&color=38BDF8)](https://github.com/maxLWS/agy-memory/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-22C55E?style=flat)](LICENSE)
[![Glama MCP Server](https://glama.ai/mcp/servers/maxLWS/agy-memory/badges/score.svg)](https://glama.ai/mcp/servers/maxLWS/agy-memory)

Open a second chat in a Google Antigravity Project and it starts blank. Ask what failed in `pytest` yesterday and the agent burns 10 turns grepping raw 50 MB JSONL logs.

**agy-memory** fixes both with one local, zero-dependency plugin for Antigravity (`App`, `CLI`, and `IDE`). Every chat in the same Project gets the active Markdown blackboard on Turn 0, backed by read-only search over your local transcripts, file edit history, command failures, and Swarm boards. No cloud sync, no vector database, no background LLM calls.

Listed in [Awesome Antigravity Plugins](https://github.com/biTQ-m/awesome-antigravity-plugins/blob/main/README.md#performance-workflow--swarm-orchestration) under **Performance, Workflow & Swarm Orchestration**.

![Before vs After agy-memory v0.4.1](./assets/before-after.svg)

## Install in 10 seconds

Requires **Node.js 20 or newer**. Pre-built single-file bundles live in `dist/`, so no `npm install` is needed.

**macOS and Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/maxLWS/agy-memory/main/install.sh | sh
```

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/maxLWS/agy-memory/main/install.ps1 | iex
```

<details>
<summary>Manual install, per-project install, or migrating v0.3 notes</summary>

```bash
git clone https://github.com/maxLWS/agy-memory.git && cd agy-memory
node scripts/install.mjs install                       # global (~/.gemini/config/plugins/agy-memory)
node scripts/install.mjs install --project /path/repo  # single repo only
node scripts/install.mjs doctor                        # verify MCP handshake, hook, and agy --strict

# Optional non-destructive import from v0.3 topics/*.md or notes.json (originals stay untouched):
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli migrate-notes --scope global
```

</details>

Start a new Antigravity session after installing.

## Why `v0.4.1`

- **Shared Project memory on Turn 0, with real isolation.** Named Projects resolve by `project_id` (reading Protobuf field 18 from `conversations/<id>.db` before `conversation_summaries.db` is populated), so two Projects pointing at the same folder never bleed into each other. Plain CLI sessions unify linked Git worktrees automatically.
- **Full forensic archive kept intact and unclipped.** Search hydrates truncated turns from `transcript_full.jsonl`, proves which session *edited* vs. only *read* a file (`mode="file_history"`), traces command failures with later passing reruns (`mode="error_history"`), and in `v0.4.1` reads full single Swarm messages without the old 1,400-char cutoff.
- **Lighter than every previous version.** Cutting Codex/Claude adapters, the legacy global-lock notes store, and standalone `list_sessions` brought the plugin down to **4 tools**, **-341 lines of source vs. `v0.3.0`** (`6,309 -> 5,968`), a **58.5 ms** startup hook, and the **lowest Turn-1 token cost since `v0.1.0`** (`-20%` vs. `v0.3.0`, `-32%` vs. `v0.2.0`).

## Benchmarks (`v0.1.0` -> `v0.4.1`)

![agy-memory benchmarks v0.1 to v0.4.1](./assets/benchmarks.svg)

Measured across **150+ real isolated `agy -p` runs** on `gemini-3.8-flash-medium` and `claude-sonnet-5-5-medium`:

| Version | Archive Recall (`T1–T7`) | File / Error / Swarm Trace | Blackboard & Isolation (`B1–B5`) | Turn-1 Prompt Tax |
| :--- | :--- | :--- | :--- | :--- |
| **No plugin** | `594.4s` model, `699k` tok, `10` spills | `file`: `113.5s` · `error`: `78.2s` *(pre-hint `v0.3`)* · Swarm: Timeout (`125.7s`) | `0/15` (0%) | Baseline (`9,617` tok) |
| **`v0.2.0`** | **`213.2s` (-64%)**, `374k` tok, **`0` spills** | No trace mode (`90.0s`) | No `project_id` board | `+3,907` tok (`11,022 B`) |
| **`v0.3.0`** | **`208.7s` (-65%)**, `375k` tok, **`0` spills** | `file`: **`21.6s`** · `error`: **`21.6s`** · Swarm: Timeout (`126.0s`) | `11/15` Gemini, `6/10` Claude (**0/5 dual-project pass, 5/5 bleed**) | `+3,304` tok (`7,674 B`) |
| **`v0.4.1`** | Preserved (`T7` `44.7s`, `T9` `16.9s`, `0` spills) | **`file`/`error` kept + Swarm `50.4s` / `5` turns / `0` spills** | **`15/15` Gemini, `10/10` Claude (5/5 zero bleed)** | **`+2,648` tok (`7,092 B`, 4 tools)** |

Full per-task tables, medians, ranges, and every defect we fixed from `v0.1.0` to `v0.4.1`: [docs/BENCHMARK_REPORT.md](./docs/BENCHMARK_REPORT.md).

## What it looks like on disk

Chat A records an active decision with `board_post` as one plain Markdown file you can edit by hand:

```markdown
<!-- ~/.gemini/agy-memory/boards/project_api-v2_<hash>/entries/retry-policy.md -->
---
schema: 1
key: "retry-policy"
title: "HTTP retry policy"
updatedAt: "2026-11-26T04:10:00.000Z"
sourceClient: "cli"
sourceSession: "a629d4f8-1a06-45a6-8a35-0f4a175c64f3"
---

Use `retry_backoff_ms=450`, header `X-Epoch-812`, and `max_batch=32`.
```

When Chat B starts in that Project, `SessionStart` injects the whole board (when `<= 1,536` UTF-8 bytes) or a whole-key index (above `1,536` bytes, never chopping mid-entry):

```text
[agy-memory] session=51459fb0 (id=51459fb0-..., scope=project/api-v2)
Project board (1 active, inline):
## retry-policy — HTTP retry policy (rev=e6aa61696c47 · 2h ago · from a629d4f8)
Use `retry_backoff_ms=450`, header `X-Epoch-812`, and `max_batch=32`.
```

![agy-memory v0.4 architecture](./assets/architecture.svg)

## Tools & scope rules

| Tool | What it does |
| :--- | :--- |
| `board_read` | Read active board entries (`project`, `global`, or `all`) with `Revision` and file `Path`. |
| `board_post` | Create, replace, or delete one keyed entry (`expectedRevision` required on updates/deletes; per-key atomic `linkSync` lock with dead-PID reaping). |
| `search_sessions` | Omit `query` to list recent sessions, or search (`text`, `file_history`, `error_history`). Pass `conversationId` to stay inside the current project and exclude self; pass `allScopes=true` to search across projects. |
| `read_session` | Inspect one session (`digest`, `turns` with `transcript_full.jsonl` hydration, `artifacts`, `swarm` with unclipped single-message reads). Stays under `8,650` UTF-8 bytes inline. |

Scopes resolve to five disjoint buckets: `project/<projectId>` (App / CLI / IDE shared, folder collisions isolated), `cli_repo/<gitCommonDir>` (linked Git worktrees unified with zero subprocesses), `cli_workspace/<realpath>`, `global`, or fail-closed `unresolved`.

## What it does not do

- **No background LLM summarization.** If Chat A never calls `board_post`, the board does not guess. Chat B relies on the 1-line sibling hint (`AGY_MEMORY_SIBLING_HINT=0` to disable) and `search_sessions`.
- **No Codex or Claude Code adapters.** Removed in `v0.4.0` so scope isolation, trace semantics, and tool schemas stay focused on Antigravity.
- **Turn-1 prefix overhead is non-zero.** Mounting 4 eager tools adds ~2,648 Turn-1 input tokens on Gemini. For one-off workspaces, install per-project via `--project`.

## CLI usage & development

Swarm workers do not mount MCP servers and can call the same bundle directly:

```bash
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli board-read --scope global
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli board-post --scope project/<id> --key cache-ttl --body "Keep mutex TTL at 15s"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli search --conversation <uuid> "rate limiter"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli search --all-scopes --mode file_history "utils.py"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli search --all-scopes --mode error_history "pytest"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli read a1b2c3d4 --mode swarm --start-seq 79 --end-seq 79
```

```bash
npm install
npm run typecheck && npm run build && npm test && npm run bench:stress && npm run validate
```

Coexists with `agy-fast` in a separate plugin directory and hook. Zero network calls. See [CHANGELOG.md](./CHANGELOG.md), [SECURITY.md](./SECURITY.md), and [MIT LICENSE](./LICENSE).
