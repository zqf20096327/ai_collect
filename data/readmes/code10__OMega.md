<p align="center">
  <img src="src/gateway/public/omega-wordmark.svg" alt="OMEGA" width="420" />
</p>

# OMega

[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.19.0-brightgreen.svg)](https://nodejs.org/)
[![Downloads](https://img.shields.io/npm/dt/omega-harness.svg?label=downloads&color=brightgreen)](https://www.npmjs.com/package/omega-harness)
[![Dependencies](https://img.shields.io/badge/dependencies-1-blue.svg)](package.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-194%20passed-success.svg)](tests/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](README.md)

**OMega** is a lightweight, local-first agent harness you fully control | Runs offline on your hardware or routed across cloud models, with human-in-the-loop approvals, isolated git worktrees, rollback snapshots, and Git-inspectable memory built in.

## Table of Contents

- [Quick Start](#quick-start)
- [Core Capabilities](#core-capabilities)
- [Configuration](#configuration)
  - [Smart Routing, Hedging & RPM Spillover](#smart-routing-hedging--rpm-spillover)
  - [Multi-User Gateway Authentication](#multi-user-gateway-authentication)
- [Extending OM](#extending-om)
  - [1. Drop-in JavaScript Tools (`./skills/*.js`)](#1-drop-in-javascript-tools-skillsjs)
  - [2. Markdown Workflows (`./skills/<name>/SKILL.md`)](#2-markdown-workflows-skillsnameskillmd)
  - [3. Programmatic API](#3-programmatic-api)
- [CLI Slash Commands](#cli-slash-commands)
- [Testing](#testing)
- [License](#license)

---

## Quick Start

**Requires:** Node.js `>= 20.19.0`

```bash
npm install
npm run build
```

Or scaffold a new project:

```bash
npx omega-harness init my-agent
cd my-agent
```

Run in any mode (works out of the box with the built-in `om` offline provider, no API keys required):

```bash
npm start                                    # Interactive CLI REPL
node bin/om.js "Summarize system specs"      # One-shot headless run
npm run gateway                              # Web Dashboard at http://127.0.0.1:3000
node bin/om.js daemon                        # Background cron/watch/webhook daemon
node bin/om.js service install               # Install 24/7 native OS service (systemd/launchd/schtasks)
```

---

## Core Capabilities

- **Multi-Model Routing, Hedging & Local System 1**: `ModelRouter` (`src/providers/router.ts`) provides EWMA TTFT/latency-aware routing (`priority` / `latency` / `round_robin`), proactive `rpmGuard` concurrency & 60s RPM spillover, opt-in cloud speculative hedging, `adaptiveEffort` for fast TTFT, half-open circuit breakers with exponential backoff, RFC 9110 / `x-ratelimit-reset-*` header parsing, hardened SSE streams (`AbortSignal` + idle-timeout reader cancellation + Gateway `TCP_NODELAY` & keep-alive heartbeats), and automatic failover across Gemini, OpenAI, Anthropic, DeepSeek, Kimi, Qwen, GLM, LM Studio, vLLM, and `om`. `OMSystemOne` (`src/systemOne.ts`) provides hardware-adaptive complexity routing, risk gating, tool shortlisting, and self-heal triage.
- **Autonomous Daemons & Automations UI**: `OMDaemon` runs cron, interval, file-watch, and webhook triggers with deterministic-first checks (0 LLM tokens when passing), isolated git worktrees, step/token guardrails, persistent run logs, Quick Templates, and 1-click diff/merge/discard in the Gateway UI. Install as a native 24/7 OS service via `om service install`.
- **Unified `ExecutionBackend` Seam**: Swap between `LocalExecutionBackend`, `DockerExecutionBackend`, and `SSHExecutionBackend` (`execution` in `om.config.json`) to route filesystem tools, shell commands, persistent terminals, `OMGitManager`, `WorkspaceSnapshotManager`, and TypeScript LSP diagnostics uniformly.
- **Coding-Agent Toolset**: Sandboxed `exec_command`, persistent interactive terminals (`terminal_start`, `terminal_write`, `terminal_read`, `terminal_list`, `terminal_close`), file tools (`read_file`, `write_file`, `patch_file`, `move_file`, `delete_file`, `list_dir`, `search_files`), Git tools, TypeScript AST/LSP tools (`file_outline`, `go_to_definition`, `find_references`, `get_diagnostics`, `get_workspace_diagnostics`), web search/fetch, and Streamable HTTP MCP servers.
- **Desktop GUI, Clipboard & Documents**: Native OS controls (`screen_capture`, `list_windows`, approval-gated `desktop_click` / `desktop_type` / `desktop_hotkey`), `clipboard_read` / `clipboard_write`, `notify_user`, pure Node.js `pdf_read`, and Playwright `markdown_to_pdf`.
- **Git-Inspectable Memory & Vector Search**: Markdown memory (`memory/MEMORY.md`, `memory/daily/YYYY-MM-DD.md`), session trajectories (`memory/sessions/`), local `node:sqlite`/JSON vector search, and zero-token memory distillation.
- **Autonomous Self-Healing & Swarms**: `OMSelfHealer` diagnoses failures, applies minimal patches, verifies with `testCommand`, and rolls back on failure; `spawn_subagent` and `DetachedSwarmManager` support worktree-isolated and process-detached execution with checkpoints.
- **Security & Multi-User Gateway**: Native OS sandboxing (`bwrap` on Linux, `sandbox-exec` on macOS, and `win-job` on Windows with race-free suspended Job Objects, `CreateRestrictedToken` privilege dropping, and `JOBOBJECT_BASIC_UI_RESTRICTIONS`), HITL approvals, SSRF redirect/IPv6 protection, secret redaction, workspace snapshots/rollback, and `local` / `multiuser` JWT + RBAC (`viewer < operator < admin`) with per-tenant isolation.
- **Tamper-Evident Audit Log & Cost Ledger**: `OMAuditLedger` (`src/audit.ts`) records every tool call, approval decision, LLM usage turn, and daemon run into an append-only, SHA-256 hash-chained `audit-ledger.jsonl` with automatic secret redaction, USD cost attribution (`estimateCostUsd`), `verifyChain()` tamper detection, `GET /api/audit` & `GET /api/audit/costs` endpoints, and a live **Audit Ledger & Cost Telemetry** panel in the Web UI Developer tab.
- **Deterministic Replay & Eval Harness**: Export recorded runs to portable `SessionTape` files (`SessionReplay.exportTape`), replay them 100% offline via `ReplayProvider` with zero network calls, and run `OMEvalRunner.compareBaseline()` to catch pass-rate drops, tool-sequence regressions, step bloat, and cost spikes automatically.

---

## Configuration

Copy `.env.example` to `.env` to configure provider keys or local endpoints:

```ini
# auto | gemini | openai | anthropic | deepseek | kimi | qwen | glm | lmstudio | vllm | om
OM_PROVIDER=auto
# OM_MODEL=gemini-3.8-flash

GEMINI_API_KEY=...
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
DEEPSEEK_API_KEY=...
LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
OM_GATEWAY_PORT=3000
# OM_WORKSPACE_DIR=.
# OM_MEMORY_DIR=./memory
```

Runtime defaults (routing fallback chains, `daemon` triggers, `security` rules, `execution` backend, `systemOne`, `selfHeal`, and `gateway`) live in [`om.config.json`](om.config.json).

### Smart Routing, Hedging & RPM Spillover

Configure latency-aware routing, tail-latency hedging, and proactive rate-limit spillover in `om.config.json`:

```json
{
  "routing": {
    "enabled": true,
    "strategy": "latency",
    "balancePrimary": true,
    "adaptiveEffort": true,
    "hedging": { "enabled": true, "delayMs": 4500 },
    "rpmGuard": { "enabled": true, "softRpmPerModel": 25, "maxInFlightPerModel": 4 }
  }
}
```

### Multi-User Gateway Authentication

Never commit plaintext tokens to `om.config.json` (which is tracked by Git). Use SHA-256 `tokenHash` values and a pinned `jwtSecret` (or `OM_JWT_SECRET` in `.env`):

```json
{
  "gateway": {
    "auth": {
      "mode": "multiuser",
      "jwtSecret": "replace-with-64-hex-char-secret",
      "users": [
        { "id": "alice", "role": "admin", "tokenHash": "<sha256-hex-of-token>" },
        { "id": "bob", "role": "operator", "tokenHash": "<sha256-hex-of-token>" },
        { "id": "carol", "role": "viewer", "tokenHash": "<sha256-hex-of-token>" }
      ]
    }
  }
}
```

---

## Extending OM

### 1. Drop-in JavaScript Tools (`./skills/*.js`)

```javascript
export const skill = {
  name: 'calculate',
  description: 'Evaluate arithmetic expressions',
  parameters: {
    type: 'object',
    properties: { expression: { type: 'string' } },
    required: ['expression']
  },
  execute: async ({ expression }) => {
    const sanitized = expression.replace(/[^0-9+\-*/().]/g, '');
    return { success: true, result: Function(`'use strict'; return (${sanitized})`)() };
  }
};
```

### 2. Markdown Workflows (`./skills/<name>/SKILL.md`)

Add a `SKILL.md` with YAML frontmatter (`name`, `description`, optional `triggers`) and invoke it in chat via `/<name>`.

### 3. Programmatic API

```javascript
import { OM, SessionReplay, OMEvalRunner } from './dist/index.js';

const agent = new OM({ provider: 'om', maxSteps: 10 });
await agent.init();

agent.on('tool_start', ({ name }) => console.log('Running:', name));
const res = await agent.run('Check memory and write a summary to notes.txt');
console.log(res.content);

// Verify tamper-evident audit chain & inspect USD cost summary
console.log(agent.audit.verifyChain(), agent.audit.getCostSummary());

// Export a portable SessionTape and replay it deterministically offline
const tape = SessionReplay.exportTape(agent.memory, agent.sessionId);
const diff = await SessionReplay.replayTape(tape);
console.log('Replay passed:', diff.passed);

await agent.close();
```

---

## CLI Slash Commands

| Command | Description |
|:---|:---|
| `/help` | Show available commands. |
| `/cloud [model]` / `/local [model]` | Switch between cloud and local inference. |
| `/provider [name] [model]` | Inspect or switch active provider. |
| `/models [provider]` / `/model <name>` | List or switch models. |
| `/skills` / `/memory` / `/journal` | Inspect loaded skills, `MEMORY.md`, or today's log. |
| `/clear` / `/gateway` / `/exit` | Reset context, start Web Gateway, or exit. |

---

## Testing

```bash
npm test                     # Build + unit & integration suite
npm run check:types          # Strict TypeScript check (internal + public)
npm run lint                 # Zero-warning oxlint check across src/
npm run test:e2e             # Playwright UI E2E tests
npm run benchmark            # Autonomous evaluation & benchmark suite
npm run benchmark:eval       # Coding-task scorecard runner (--live for real APIs)
node scripts/security-audit.js  # Dependency, secret & eval() audit
```

All 194 unit & integration tests pass using Node's built-in `node:test` runner across Linux, macOS, and Windows CI (`.github/workflows/ci.yml`), covering core agent loops, routing resilience & hedging, security hardening, Windows/OS sandboxing, audit chain integrity, deterministic replay evals, and monorepo/LLM-failover battle tests (Playwright is used for `test:e2e`).

---

## License

[MIT](LICENSE)
