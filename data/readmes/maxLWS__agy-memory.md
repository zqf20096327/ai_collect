# agy-memory

[中文版](./README.zh-CN.md)

[![CI](https://github.com/maxLWS/agy-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/maxLWS/agy-memory/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/maxLWS/agy-memory?style=flat&color=38BDF8)](https://github.com/maxLWS/agy-memory/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-22C55E?style=flat)](LICENSE)
[![Glama MCP Server](https://glama.ai/mcp/servers/maxLWS/agy-memory/badges/score.svg)](https://glama.ai/mcp/servers/maxLWS/agy-memory)

**agy-memory** is a local, zero-dependency MCP plugin for Google Antigravity (`agy` CLI, Desktop, and IDE). It lets any session search and inspect your local conversation history without grepping raw JSONL transcripts, running a vector database, or sending data off-machine:

1. **Cross-conversation recall**: search Antigravity transcripts (hydrating truncated turns from `transcript_full.jsonl`), Markdown artifacts, Swarm boards, and opt-in local **Codex** (`~/.codex`) / **Claude Code** (`~/.claude`) sessions.
2. **File & error history**: check which past sessions edited vs. only read a file (`mode="file_history"`), or look up past command failures, exit codes, and matching reruns (`mode="error_history"`).
3. **Editable Markdown notes**: store long-lived notes as plain files (`topics/<id>.md` + `MEMORY.md`) with `expectedRevision` compare-and-swap checks.

## Architecture

![agy-memory architecture](./assets/architecture.svg)

- **Catalog & search (`src/store.ts`, `src/search.ts`)**: reads `conversation_summaries.db` read-only (`node:sqlite` / `sqlite3` / Python / JS fallback), caches parsed sessions by mtime, and hydrates truncated turns from `transcript_full.jsonl`.
- **Trace & external adapters (`src/trace.ts`, `src/adapters.ts`)**: streams JSONL incrementally with a 32 MB / 2.5 s scan budget, verifies write/rerun outcomes, and reads `~/.codex` / `~/.claude` under qualified IDs (`codex:<id>`, `claude:<id>`).
- **Notes & budget packer (`src/notes.ts`, `src/snapshot.ts`)**: keeps all 5 MCP tools under `<=8,650` UTF-8 bytes so responses stay inline instead of spilling to `output.txt`, and injects a read-only `<=1.8 KB` startup snapshot on `SessionStart`.

## What It Looks Like

![Trace and cross-CLI output examples](./assets/trace-output.svg)

![Before vs After agy-memory](./assets/before-after.svg)

## Quick Start

Requires **Node.js >= 20** (no `npm install` needed; pre-built ESM bundles live in `dist/`).

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/maxLWS/agy-memory/main/install.sh | sh
```

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/maxLWS/agy-memory/main/install.ps1 | iex
```

Or paste into any Antigravity session:

```text
Clone https://github.com/maxLWS/agy-memory.git, run `node scripts/install.mjs install && node scripts/install.mjs doctor` inside it to install and verify the agy-memory plugin, and enable it in agy.
```

<details>
<summary>Manual or per-project install</summary>

```bash
git clone https://github.com/maxLWS/agy-memory.git && cd agy-memory
node scripts/install.mjs install                       # global (~/.gemini/config/plugins/agy-memory)
node scripts/install.mjs install --project /path/repo  # single workspace
node scripts/install.mjs doctor                        # verify MCP handshake, hook, and agy --strict
```

</details>

Start a new `agy` session after installing.

## Benchmarks

![v0.3.0 benchmarks](./assets/v030-benchmarks.svg)

Measured with real headless `agy -p` runs on a frozen 139-session snapshot (+6 Codex, +6 Claude), isolated per-run `HOME`, and pinned `gemini-3.8-flash-medium`. On a synthetic 55 MB transcript in a fresh process, a 32 MB capped scan finishes in `484 ms` with `INCOMPLETE SCAN`, and a second call resumes 32 → 55 MB in `355 ms` (`VmHWM = 119.5 MB`).

Full per-task tables, failure analyses, and known limits (including where Markdown notes do not save tokens): [docs/BENCHMARK_REPORT.md](./docs/BENCHMARK_REPORT.md).

## CLI Usage

Swarm workers and shell scripts can invoke the same bundle directly via `--cli`:

```bash
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli list --source all --limit 10
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli search "rate limiter 缓存击穿"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli search --mode file_history "utils.py"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli search --mode error_history "pytest"
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli read codex:01ab34cd --mode turns --tail 5
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli read a1b2c3d4 --mode swarm --tail 25
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli note-save --topic "Cache TTL" --content "Keep mutex TTL at 15s" --tags cache
node ~/.gemini/config/plugins/agy-memory/dist/mcp-server.mjs --cli stats --recent 50
```

## Code Reading Path

```text
src/
├─ mcp-server.ts      stdio JSON-RPC (JSONL + LSP framing) & --cli entrypoint
├─ session-start.ts   SessionStart hook wrapper (read-only <=1.8 KB snapshot)
├─ tools.ts           5 eager MCP tool definitions & argument dispatcher
├─ store.ts           SQLite/JS catalog, transcript hydration, digest/turns/swarm reader
├─ search.ts          CJK+EN search, literal rg prefilter, snippet ranking
├─ trace.ts           file_history & error_history extractor (positive outcome checks)
├─ adapters.ts        read-only Codex/Claude adapters & incremental JSONL streamer
├─ notes.ts           topics/<id>.md + MEMORY.md index, lockfile, expectedRevision CAS
└─ analytics.ts       offline transcript usage analyzer (--cli stats)
```

## Development

```bash
npm install
npm run typecheck && npm run build && npm test && npm run bench:stress && npm run validate
```

Coexists cleanly with `agy-fast` (separate plugin dir, MCP namespace, and hook). Zero network calls; see [SECURITY.md](./SECURITY.md) and [CHANGELOG.md](./CHANGELOG.md). Licensed under [MIT](./LICENSE).
