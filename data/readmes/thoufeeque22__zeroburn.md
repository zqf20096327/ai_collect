# ZeroBurn (`zeroburn`)

> **Cut AI coding-agent cloud API token & quota burn by 70–83%** by eliminating test/discovery output bloat, querying live-verified local code graphs, running deterministic AST/auth/scope checks, and offloading mechanical failure analysis and diff reviews to local Ollama models — without sacrificing Contract-First TDD or strict quality gates.
>
> *Works across any coding agent harness and frontier model family (Google Gemini, Anthropic Claude, OpenAI, Cursor, Antigravity).*
>
> *Engineered by the team building **[directly.social](https://directly.social)** (`@directlysocial`).*

## ⚡ Quick Start (10 Seconds)

> **Prerequisites:** Any Git repository (GitHub, GitLab, Bitbucket, or local Git), Node.js 18+, and (optional) local Ollama. No GitHub account or `gh` login required.

**1. Live 0-Install Benchmark & AST Diff Auditor (Try it in any repo):**
```bash
curl -fsSL https://github.com/thoufeeque22/zeroburn/raw/main/benchmarks/try-now.mjs | node
```

**2. Install ZeroBurn into your repo:**
```bash
git clone --depth 1 https://github.com/thoufeeque22/zeroburn /tmp/zb && cp -R /tmp/zb/.agents . && rm -rf /tmp/zb && node .agents/scripts/init.mjs --pull
```

**3. In-Place Upgrade to Latest Release:**
```bash
node .agents/scripts/init.mjs --upgrade
```

**4. Trigger in Chat (GitHub Issue or Plain Local Task):**
```text
# With a GitHub issue:
start orchestration workflow on #1043

# Or without GitHub / plain local task:
implement tier-based upload quota limits in src/lib/billing
```

> **Note:** Upgrades preserve your existing project settings (`projectName`, `stackSummary`, `graphProjectId`, and local models) inside `.agents/project.config.json` while updating the engine, rules, and subagents. When a new release is available, your agent's session banner will automatically alert you.

```text
🔥 ZeroBurn v2.9.0 — Live Token-Savings Benchmark & 0-Token Diff Auditor
📂 Repository: /Users/dev/my-app (branch: feat/billing-quota)

📊 1. Context & Cloud Token Footprint (Standard Subagent vs ZeroBurn)
┌────────────────────────────┬────────────────────────────┬─────────────────────────────┬────────────────┐
│ Pipeline Stage             │ Vanilla Agent              │ ZeroBurn v2.9.0             │ Cloud Saved    │
├────────────────────────────┼────────────────────────────┼─────────────────────────────┼────────────────┤
│ 1. Repo & Route Discovery  │ 15,429 tok (1465 files)    │ 512 tok (5-line digest)     │ -96.7%         │
│ 2. Rule & Docs Ingestion   │ 59,202 tok (4348 lines)    │ 195 tok (7-line digest)     │ -99.7%         │
│ 3. Test Verification Logs  │ 6,816 tok (verbose log)    │ 17 tok (1-line quiet-cli)   │ -99.8%         │
│ 4. Diff Security Audit     │ 3,500 tok (Cloud Pro)      │ 0 tok (Local Ollama + AST)  │ -100.0%        │
├────────────────────────────┼────────────────────────────┼─────────────────────────────┼────────────────┤
│ TOTAL (Single Agent Loop)  │ 84,947 cloud tokens        │ 724 cloud tokens            │ -99.1%         │
│ TOKENS TO 1ST GREEN EDIT   │ 312,078 tok (4 turns)      │ 2,731 tok (2 turns)         │ -99.1%         │
│ 5-TURN CUMULATIVE BILLING  │ ~339,788 billed tokens     │ ~2,896 billed tokens        │ 336,892 saved  │
└────────────────────────────┴────────────────────────────┴─────────────────────────────┴────────────────┘

🛡️  2. Live 0-Cloud-Token Diff Audit (HEAD~1..HEAD — 3 changed file(s))
┌────────────────────────────┬──────────┬──────────────┬─────────────────────────────────────────────────┐
│ Audit Engine               │ Time     │ Cloud Cost   │ Verdict                                         │
├────────────────────────────┼──────────┼──────────────┼─────────────────────────────────────────────────┤
│ Static AST & Route Auth    │ 0.01s    │ 0 cloud tok  │ ✅ PASS (<=200L, 0 `any`, route auth guards)     │
│ Ollama (qwen2.5-coder:14b) │ 8.92s    │ 0 cloud tok  │ ✅ PASS — Clean diff verified                    │
└────────────────────────────┴──────────┴──────────────┴─────────────────────────────────────────────────┘
```

---

## Why `zeroburn` Exists

Most multi-agent setups ("PM / Architect / Dev / QA prompt packs") drain your 5-hour and weekly Claude / Gemini usage limits in two tickets because:
1. **Blank-Slate Subagent Tax:** Every subagent starts fresh and wastes 3–5 turns re-reading markdown rule files, directory trees, and full source files.
2. **Test Log Bloat:** Verbose test/lint runs (`vitest`, `eslint`, `tsc`) dump 500+ lines (~15,000 tokens) into context on every turn, which then gets re-billed on every subsequent turn ($O(N^2)$ context growth).
3. **Frontier Models on Mechanical Checks:** Cloud `pro` / `Opus` models are spawned to check line counts, `any` types, and file blast radius that Python + local Ollama can verify in **0 cloud tokens**.

### Verified Production Benchmark (`directly.social` — 10,893 AST Nodes, 1,470 Source Files)

Measured on a real feature/audit loop (*"Locate and audit `checkUploadQuota` tier logic, run all 6 billing unit test suites (70 tests), and execute a diff security audit"*). Full raw traces and reproducible runner in [`benchmarks/REAL_WORLD_BENCHMARK.md`](benchmarks/REAL_WORLD_BENCHMARK.md):

| Stage | Standard Coding Agent (Vanilla) | `zeroburn` v2.9.0 Engine | Measured Savings |
| :--- | :--- | :--- | :--- |
| **1. Repo & Route Discovery** | `find src -type f` (`1,470` lines / **15,454 tokens**) | `build_repo_map_digest()` (`6` lines / **636 tokens**: 28 Prisma models, 32 domains, 60 API routes) | **-95.9% tokens** |
| **2. Governance & Rule Loading** | `cat .agents/AGENTS.md .agents/base/*.md` (`276` lines / **10,274 tokens**) | Pre-computed inlined rule digests (`7` lines / **195 tokens**) | **-98.1% tokens** |
| **3. Symbol Localization** | `grep -rn "quota" src/lib/` (`64` matches / **1,921 tokens**) + exploratory reads | `codebase-memory-mcp` `search_graph` -> `FreemiumGuard.checkUploadQuota` (`src/lib/billing/freemium-guard.ts:43-83`) in **0 LLM tokens** | **-100% exploratory LLM tokens** |
| **4. Unit Test Run (6 suites, 70 tests)** | `npx vitest run` (`243` lines / **6,816 tokens** per run) | `node .agents/scripts/quiet-cli.mjs unit` (`1` line / **17 tokens**) | **-99.75% test log tokens** |
| **5. Diff Security & Quality Audit** | Cloud `Pro` / `Opus` subagent review (**~12,000+ cloud tokens**) | 0-token Python AST/Blast-Radius + Local Ollama `qwen2.5-coder:14b-custom` (`13.43s`, **0 cloud tokens**) | **100% cloud audit quota saved** |
| **Single-Pass Overhead Total** | **46,465+ Cloud Tokens** | **848 Cloud Tokens** | **98.2% Reduction** |

#### ⚡ 30-Second Before vs After (Actual Terminal Trace)

```text
❌ WITHOUT ZEROBURN (Standard Subagent — 46,465 tokens burned before writing code):
$ find src -type f                                  # 1,470 lines  (15,454 tokens)
$ cat .agents/AGENTS.md .agents/base/*.md           #   276 lines  (10,274 tokens)
$ grep -rn "quota" src/lib/                         #    64 lines  ( 1,921 tokens)
$ npx vitest run src/__tests__/unit/*billing*       #   243 lines  ( 6,816 tokens)
$ [Spawns Cloud Pro Subagent for Diff Review]       #              (12,000 tokens)
----------------------------------------------------------------------------------
💥 Result: 46,465+ tokens & ~185,000 cumulative billed tokens across a 5-turn loop.

✅ WITH ZEROBURN v2.9.0 (848 tokens — 98.2% reduction):
$ [codebase-memory-mcp] search_graph("billing tier quota check")   #     0 tokens
  -> FreemiumGuard.checkUploadQuota (src/lib/billing/freemium-guard.ts:43-83)
$ [Inlined REPO_MAP_DIGEST + Rule Digests]                         #   831 tokens
  -> 28 Prisma Models | 32 src/lib domains | 60 API Routes
$ node .agents/scripts/quiet-cli.mjs unit src/__tests__/unit/*billing*
  -> [quiet-cli] unit: PASS (Test Files 6 passed (6), Tests 70 passed (70)) # 17 tokens
$ [parallel-audit.py] Python AST + Local Ollama qwen2.5-coder      #     0 cloud tokens
----------------------------------------------------------------------------------
⚡ Result: 848 tokens total. Surgical edit on Turn 1. Zero cloud Pro audit burn.
```

---

## How It Works (Under the Hood)

Instead of relying on proprietary agent runtimes or buzzwords, ZeroBurn is a set of transparent scripts, hooks, and local model helpers that eliminate cloud context waste:

1. **Test Stdout Truncation & Local Failure Diagnosis (`quiet-cli.mjs`):**
   - **Passing runs:** Vitest, ESLint, and TypeScript emit a 1-line receipt (`PASS`) instead of dumping 500 lines of ASCII progress bars into chat history.
   - **Failing runs:** On >12-line failures, local Ollama (`gemma4` / `qwen2.5-coder`) outputs a concise 3-line diagnosis (exact `file:line`, root cause, suggested fix) directly *above* the last 35 lines of the raw stack trace so critical diagnostics are never dropped.

2. **Pre-Execution AST Code Graph with Live Tree Verification (`codebase-memory-mcp`):**
   - Queries a local SQLite/AST symbol index *before* constructing subagent prompts—avoiding both exploratory `find`/`grep` loops and the ~9k-token per-turn MCP tool-schema tax (schemas stay lazy-loaded).
   - Every graph-indexed path and line range is verified against the live filesystem on read (`_verify_live_file_entry`), converting moved or deleted files into explicit `[STALE_INDEX_MISS]` signals so agents never trust stale coordinates.

3. **Two-Tier Hybrid Security, Docs Parity & Quality Audit (`parallel-audit.py` + `quiet-cli.mjs docs-parity`):**
   - **Tier 1 (0-Token Deterministic Rules + Local Ollama Pre-Filter):** Deterministic properties run in pure Python first (missing server-side auth guards on non-public `/api/**/route.ts` handlers, docs & knowledge parity checks for user-facing/schema diffs across Track S/M/L, line-count modularity, `'use server'` line-1 placement, explicit `any`, and blueprint scope drift). Local Ollama then scans the diff for fuzzy logic/error-handling issues.
   - **Tier 2 (Cloud Auditor Final Decision):** Local findings are passed into a single cloud frontier auditor (`pro` or `flash`), which filters out local false positives and serves as the authoritative gate for blocking `Critical` and `High` issues.

4. **Dynamic Live `REPO_MAP_DIGEST` & Inlined Rule Digests (`workflow_common.py`):**
   - Walks `src/app/api/**`, `src/lib/*`, and `prisma/schema.prisma` live on disk in `<5ms` right before spawning a subagent, inlining a 6-line structural map + compressed rule digests so subagents never waste turns listing directories or reading markdown docs.

5. **Advisory File Locks for Parallel Workers (`swarm_leases.json`):**
   - Simple JSON lockfile enforced by `pre-tool-guard.mjs` before file edits, preventing concurrent subagents in parallel swarms from editing the same file simultaneously.

6. **Stage 0/1 Smart Bypass & Work-Resume Gate (`parallel-discovery.py` + `ORCHESTRATION.md`):**
   - Automatically detects branches that already have commits/WIP (`already_worked_on`), Track L child sub-issues, and pre-specced observation-triage tickets, bypassing redundant `product-agent` and `discovery-agent` spawns in **0 cloud tokens** and resuming directly at `Dev`, `QA`, or `Audit`.

7. **Multi-Slice Epic Feature Branches & Docs-Only Zero-Test Fast-Path:**
   - Multi-slice epics branch into and PR against dedicated `epic/<epic-id>-<slug>` master feature branches to eliminate cascading rebase conflicts. Commits touching only documentation or markdown rules bypass full test suites to save compute.

---

## Tips, Tricks & Token Optimization Guide

For everyday efficiency tips, prompt shortcuts, and session hygiene best practices, read the [**ZeroBurn Tips & Tricks Guide**](docs/TIPS_AND_TRICKS.md):
- **1-Line Minimalist Startups:** Why typing `start orchestration workflow on #1043` is faster and cheaper than pasting 2,000-token manual handover notes.
- **Master Epic Branches:** Eliminating cascading rebase conflicts on multi-slice features.
- **Session Lifecycles:** 1 chat per ticket, 0-token AST checks, and optimal timing for `/compact`.
- **Knowledge Graph vs Grep:** Using MCP graph queries instead of reading full 500-line source files.

---

## Repository Layout

```text
CHANGELOG.md                        # Version history & upgrade notes
docs/
└── TIPS_AND_TRICKS.md              # Operational token-saving & prompt shortcut guide
benchmarks/
├── REAL_WORLD_BENCHMARK.md         # Verified A/B benchmark on 10,893-node production repo
├── try-now.mjs                     # Zero-install live token benchmark & local Ollama diff auditor
└── run_benchmark.py                # Reproducible Python A/B benchmark runner
.agents/
├── AGENTS.md                       # Global management policies & Subagent Registry
├── project.config.json             # Single declarative config (stamps zeroburnVersion)
├── project.config.example.json     # Starter template
├── hooks.json                      # SessionStart & PreToolUse safety hooks
├── base/
│   ├── ORCHESTRATION.md            # Hybrid Quota Policy (Options A+B+C), Tracks S/M/L
│   ├── CORE.md                     # TypeScript, 100-line modularity, data contracts
│   ├── PRODUCTION.md               # Reliability, 7-Point AI Security Checklist
│   ├── UI_UX.md                    # Design system, ergonomics, a11y, microcopy
│   └── VARIABLES.md                # Canonical paths, commands, verdicts
├── hooks/
│   ├── session-start.mjs           # Git + Version + Auto-Start Local Ollama + Graph banner
│   └── pre-tool-guard.mjs          # Secret guard, Swarm file-lease guard, 100-line guard
├── scripts/
│   ├── init.mjs                    # 1-command auto-detector & version upgrader (--pull, --pin, --version)
│   ├── live-audit.mjs              # Real-time 0-cloud-token diff auditor & context calculator
│   ├── graph_prefetch.py           # Live-verified codebase-memory-mcp graph pre-fetcher
│   ├── ollama_gate.py              # Local Ollama auto-start, model resolution & fail-closed gate
│   ├── repo_digest.py              # Dynamic REPO_MAP_DIGEST & swarm advisory file leases
│   ├── workflow_common.py          # Shared FALLBACK_CHAINS, digests & modular re-exports
│   ├── parallel-discovery.py       # Stage 1: Product || Discovery workflow
│   ├── parallel-audit.py           # Stage 4: 0-token Python/Auth/Docs + Local Ollama + 1 Cloud Auditor
│   └── quiet-cli.mjs               # 1-line tsc/lint/vitest wrapper + Judgment Kernel + api-map + docs-parity
└── plugins/
    └── zeroburn/
        ├── plugin.json             # Single source of truth for ZeroBurn version (v2.9.0)
        └── agents/                 # 8 specialized subagent definitions
```

---

## Attribution

Open-sourced by the engineering team building **[directly.social](https://directly.social)** (`@directlysocial`).
