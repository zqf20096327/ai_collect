<p align="center">
  <img src="assets/logo.svg" alt="TokenSafe Logo" width="88" height="88" />
</p>

<h1 align="center">TokenSafe</h1>
<!-- mcp-name: dev.tokensafe/tokensafe -->

<p align="center">
  <b>Your coding agent isn't getting dumber. Your context is just full of trash.</b><br>
  When chat sessions fill up with massive lockfiles and endless build logs, your AI loses focus.<br>
  TokenSafe strips the noise with Tree-sitter AST slicing so your agent stays razor-sharp, changes only the lines you asked for, and never leaks your secrets.<br>
  Works with <b>Cursor, Claude Code, Codex, Windsurf, Google Antigravity, Gemini CLI, and ChatGPT</b>.
</p>

<p align="center">
  <a href="https://github.com/tokensafe-dev/tokensafe/actions/workflows/test.yml"><img src="https://img.shields.io/github/actions/workflow/status/tokensafe-dev/tokensafe/test.yml?branch=main&label=tests&style=flat-square&color=10B981" alt="Tests"></a>
  <a href="https://www.npmjs.com/package/tokensafe"><img src="https://img.shields.io/npm/v/tokensafe.svg?color=38BDF8&style=flat-square" alt="npm"></a>
  <a href="https://www.npmjs.com/package/tokensafe"><img src="https://img.shields.io/npm/dw/tokensafe.svg?color=10B981&label=npm%20downloads&style=flat-square" alt="npm downloads"></a>
  <a href="https://pypi.org/project/tokensafe/"><img src="https://img.shields.io/pypi/v/tokensafe.svg?color=38BDF8&style=flat-square" alt="PyPI"></a>
  <a href="https://github.com/tokensafe-dev/tokensafe/stargazers"><img src="https://img.shields.io/github/stars/tokensafe-dev/tokensafe?style=flat-square&color=334155" alt="Stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-0F766E?style=flat-square" alt="License"></a>
  <a href="https://tokensafe.dev#pricing"><img src="https://img.shields.io/badge/Team_Trial-7_Days_Free-10B981?style=flat-square" alt="Trial"></a>
</p>

<p align="center">
  <a href="#install--agents">Install</a> &bull;
  <a href="#cli-quickstart">Quickstart</a> &bull;
  <a href="#whats-new-in-v40">What's New in v4.0</a> &bull;
  <a href="#why-tokensafe">Why TokenSafe</a> &bull;
  <a href="#benchmarks">Benchmarks</a> &bull;
  <a href="#pricing-and-7-day-team-trial">Pricing</a> &bull;
  <a href="#faq">FAQ</a> &bull;
  <a href="#reference">Reference</a> &bull;
  <a href="https://tokensafe.dev">Website &amp; Docs</a>
</p>

---

## What's New in v4.0

TokenSafe 4.0 is a major architecture release designed for **Zero Mid-Day Lockouts, 3-Second Turn Latency, Exact Code Context (Zero Loss), and Developer Flow**:

- **⚡ SQLite FTS5 BM25 Code Indexer & Search (`scoped_search`, `tokensafe search`)**: Native SQLite full-text search with trigram tokenization and BM25 relevance ranking (<1ms) across the repository. Replaces raw terminal grep entirely with zero-token-waste search.
- **🔗 SQLite Graph Cache & Cross-Boundary Route Linking**: Persistent SQLite caching (`.tokensafe/cache/graph.db`) with bidirectional semantic linking between frontend client endpoints (`fetch`, `axios`, `apiClient`) and backend HTTP routes (`FastAPI`, `Express`, `Flask`, `Next.js`).
- **🖼️ Vision Image Downscaler (`optimize_image`, `tokensafe optimize-image`)**: Automatically scales down oversized screenshots, architecture diagrams, and mockups (>1024px) via Pillow or macOS `sips`, saving 50–75% vision tokens while keeping original files intact.
- **🧠 Anti-Stuck Dead-Ends Ledger (`get_mistakes`, `tokensafe mistakes`)**: Persistent project memory tracking failed hypotheses, loop guard trips, and git reverts to prevent agents from cycling through already-failed solutions.
- **🧹 Transcript Superseded Output Pruning (`prune_superseded`, `tokensafe prune-superseded`)**: Prunes obsolete intermediate tool reads that were superseded by subsequent edits or re-reads in long agent transcripts (-30-40% context).
- **🧼 ANSI Escape Sequence Stripper**: Cleans all ANSI/VT100 escape codes from tool outputs, test runners, and proxy streams before they enter model context.
- **👻 Ghost Tokens Auditor (`tokensafe doctor`)**: Detects and cleans redundant multi-IDE configuration files (`.cursorrules`, `CLAUDE.md`, `.windsurfrules`, `.clinerules`) and oversized rule files, saving 2,000–5,000 wasted ghost tokens on every turn.
- **🛡️ Exact Code Context & Reversible Stash (`expand_ref`)**: 100% byte-exact target symbol preservation with reversible 8-char hash anchors (`#a1b2c3d4`) to instantly recover any folded block.
- **🌲 C# Tree-sitter Support**: Native AST slicing and God Nodes detection for C# (`tree-sitter-c-sharp`) alongside TypeScript, JavaScript, Python, Go, Rust, Java, Kotlin, and PHP.

---

## Install & Agents

Connect TokenSafe to the AI coding agents on your workstation in one command:

```bash
# Option 1: Zero-Install via npx (recommended)
npx tokensafe

# Option 2: Python / PyPI
pip install tokensafe && tokensafe

# Option 3: Direct shell script (macOS / Linux)
curl -fsSL https://tokensafe.dev/install.sh | bash
```

The installer detects which agents live on your machine, registers the TokenSafe MCP server, injects project rules, and wires lifecycle hooks where the agent supports them.

| Agent | Integration |
|---|---|
| **Google Antigravity** | Plugin symlink + hooks + skills + MCP (loaded automatically on startup) |
| **Claude Code CLI** | MCP + `SessionStart` / `UserPromptSubmit` / `PreToolUse` hooks |
| **Cursor** | MCP + `beforeShellExecution` / `beforeReadFile` hooks |
| **Claude Desktop** | MCP registration (`claude_desktop_config.json`) |
| **Windsurf** | MCP registration + global rules |
| **OpenAI Codex** | MCP in `~/.codex/config.toml` (stdio + cloud HTTP natively) |
| **Cline / Roo Code** | MCP registration (VS Code) |
| **GitHub Copilot** | MCP registration |
| **Z.ai Code** | MCP registration |
| **ChatGPT** | Cloud connector, nothing to install |
| **Gemini CLI** | MCP registration |

Claude Desktop / Cursor MCP config:

```json
{
  "mcpServers": {
    "tokensafe": { "command": "npx", "args": ["-y", "tokensafe", "mcp"] }
  }
}
```

Cloud features (team metrics, managed distillation, shared team cache, billing) run on the remote endpoint `https://api.tokensafe.dev/mcp` with `Authorization: Bearer <TS2. license key>`. Four public tools work without a key, so ChatGPT connects with authentication set to **None**.

Full per-agent configuration, hook details, and the Codex/ChatGPT setup live in [docs/AGENT_SETUP.md](docs/AGENT_SETUP.md).

## CLI Quickstart

```bash
# View live savings dashboard in your terminal
tokensafe stats
```

```text
⚡ TOKENSAFE CONTEXT OPTIMIZER DASHBOARD
Total Tokens Saved:   4,524,156 tokens
Efficiency Gain:      [████████████████████████░░] 92.5%
Context Traffic:      4,889,255 raw → 370,574 optimized (2,132 events)

• Command Sanitizer (CLI)        :   727,300 tokens saved (263 events)
• Architecture Graph             :   758,256 tokens saved (13 events)
• Multi-turn History Fold        : 2,897,897 tokens saved (471 events)
• Prompt Compactor (local+cache) :    43,502 tokens saved (1,255 events)
```

```bash
# Audit your environment: MCP tool overhead, skills tax, risky settings
tokensafe doctor

# Recursive security & hygiene audit of a repository
tokensafe guard audit

# Preview prompt compaction on custom input
tokensafe test "fix the validate_token method in src/auth.py to check jwt expiration"

# Map architectural hotspots before multi-file changes
tokensafe graph

# Disable a heavy MCP server without editing JSON
tokensafe mcp disable <server>

# Compile and preview the Friday team ROI digest
tokensafe digest

# Activate a Team or Solo license key
tokensafe activate TS2.eyJlbWFpbCI6...
```

The full command reference (24 commands) is in [Reference](#reference).

## Why TokenSafe

Giving coding agents raw access to entire repositories creates three daily costs:

1. **Senior hours burned on AI PRs**: reading 2,000-line modules for a 10-line fix makes models forget imports, invent methods, and regress adjacent code.
2. **Secret leaks and unsafe shortcuts**: static prompt rules in `.cursorrules` wear off mid-session. Agents hardcode fallback credentials, disable TLS checks, or stage `.env` files with `git add .`.
3. **Mid-sprint quota stops and blind spend**: bloated diffs, lockfiles, and verbose MCP schemas burn 5-hour limits while engineering leads lack per-seat ROI visibility.

| Outcome | What changes for your team | How it is enforced |
|---|---|---|
| **Clean code on the first pass** | Agents read only target functions, design tokens, and 1-hop dependencies instead of 2,000 lines of noise. | Sub-30ms local AST skeletonizer, architecture graph, predictive signature prefetch, lockfile-stripping diff slicer, loop guard. |
| **Zero leaked secrets in git** | Hardcoded password fallbacks, TLS bypasses, raw SQL interpolation, and `.env` commits are stopped before reaching disk or staging. | Deterministic TokenSafe Guard on every tool call, output guard on large writes, local PII/key redaction. |
| **Predictable sprint velocity & ROI** | Teammates get warm cache hits, and CTOs receive a Friday ROI digest separating `measured` and `estimated` savings. | Shared team cache, live context budget HUD, per-seat dashboard. |

A $29 seat pays for itself by saving one hour of senior code review or preventing one leaked key. Typical payback: **1 to 3 days** of team usage.

## Before and After

One contrast: an agent asked to change one helper in a 1,420-line file receives 94 lines of target logic and type contracts instead of the whole module. The same principle applies to terminal output, diffs, and session history.

| What breaks coding agents | How TokenSafe fixes it | The outcome |
| :--- | :--- | :--- |
| **"Lost in the Middle" context fade**: an agent reads a 2,000-line file to change one 10-line helper, forgets imports, and invents methods. | **AST skeletonizer** folds inert bodies into typed signatures while keeping the target symbol and 1-hop callees intact. | Focused signal: the model keeps full type contracts without drowning in unrelated logic. |
| **Terminal log flooding**: `npm test` or `pytest` fails and dumps 4,000 lines of stack traces and lockfile diffs into context. | **Command sanitizer** strips lockfile noise and trims output to the failing assertion and stack frame. | Root-cause fixes instead of unrelated rewrites. |
| **Infinite wait on background tests**: `yarn test` hangs in watch mode, or jest finishes but unclosed handles keep the process alive. | **Test-runner guard** forces run-once mode (`CI=true`, `--watch=false`, `--forceExit`) and peeks at `<cwd>/package.json` to identify the runner behind opaque scripts. | The test run terminates with an exit code and the agent moves on. |
| **5-attempt retry loops**: an agent repeats the same broken edit until the context budget runs dry. | **Loop guard** detects repeated identical tool calls and halts the cycle. | Stuck loops stop before damaging working modules. |
| **Unsafe edits & secret leaks**: fallback keys, `verify=False`, SQL string interpolation, or `git add .` with `.env` present. | **TokenSafe Guard** audits writes and shell commands locally before execution. | Credentials, SQLi patterns, and destructive commands are blocked locally. |

When an operation is blocked, the agent sees an explicit, constructive message:

```text
🛡️ TokenSafe Guard: Blocked a hardcoded secret fallback in config.py.
   Leave the default empty or read from os.environ at runtime.
```

## 10 Core Engine Capabilities

Why TokenSafe agents ship working code on the first pass without burning quotas or leaking keys:

| Capability | What it solves | How it works | Impact |
|---|---|---|---|
| **1. Architecture Graph**<br>`get_architecture_graph` | Agents open an unfamiliar repo and burn 45k tokens blindly crawling files. | Analyzes dependency centrality, import hubs, and critical call paths in memory. | **< 250 tokens** to map God Nodes (vs ~45k blind crawl) |
| **2. Smart Code Slicing**<br>`smart_read_file` | Feeding 3,000 lines into context causes models to hallucinate fake methods. | Preserves target method logic while folding uncalled helpers into typed contracts. | **-95.0% tokens** (192 vs 3,840) across 11 languages |
| **3. Pre-Git Security Guard**<br>`guard_inspect` | Autonomous agents read `.env` secrets or hardcode fallback keys in edits. | Sub-millisecond pre-flight interception blocks secrets, TLS bypasses, and dangerous commands. | **0 leaked keys** in LLM logs or git history |
| **4. Lockfile & Noise Shield**<br>`schema_slicer` | Reading `package-lock.json` or `uv.lock` dumps 360k+ tokens in one turn. | Intercepts lockfiles and massive schemas, returning a queryable dependency summary. | **-99.8% tokens** (855 vs 367,410 tokens) |
| **5. Monorepo API Surface Map**<br>`get_api_surface` | Agents guess interfaces or crawl dozens of modules to find exported types. | Extracts all exported types, interfaces, and contracts across the repo in one pass. | **1 tool call** vs 50 separate file reads |
| **6. Subagent Pointer Cache**<br>`SUBAGENT_DEDUP` | Multi-turn chats and swarms pay full price to re-read the same shared utilities. | In-memory content hashes return 1-line pointer hits for unchanged files. | **0 tokens wasted** on repeat file reads |
| **7. Shared Team Cache**<br>`team_cache` | 10 to 50 engineers repeatedly parse the same core libraries from scratch. | L3 monorepo pool shares stripped signatures and package contracts across teammates. | **72% team hits** with 0ms turnaround |
| **8. KV-Cache Prefix Locking**<br>`cache_normalizer` | Shifting timestamps and reordered tools break provider prompt cache hits. | Locks prefix order, sorts schemas, and injects breakpoints for Anthropic, DeepSeek, and OpenAI. | **92% cache hit rate** at 0.10x provider rates |
| **9. Compact Test Runner**<br>`sanitize_command` | Test suites spew 1,000 lines of passing dots that crowd out instructions. | Forces run-once mode (`CI=true`) and collapses passing runs to a single line. | **1 line vs 1,200 lines** (traces kept on failure) |
| **10. Context Governor & Ledger**<br>`compact_conversation` | Models suffer needle-in-a-haystack amnesia after 70% context saturation. | Monitors context thresholds and compacts chat sprawl into an actionable State Ledger. | **50+ turns** without regression or amnesia |

Deeper mechanics (language matrix, AST syntax trees, cache tiers, governor) live in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Benchmarks

Reference run across 10 production engineering scenarios (`169,761` baseline tokens down to `8,173` tokens, **`-95.2%`** net context reduction, **`-99.4%`** peak single-scenario reduction, `+30.6%` turn latency speedup with `100%` accuracy retention):

> Prompt compaction, graph topology (`SWE-06`), `dep_mode="signature"` slicing (`SWE-07`), repeat-read pointer dedup (`SWE-09`), and parametric slot cache hits (`SWE-10`) are **measured live** (`1,368` optimized tokens) while baselines (`169,761`), turn counts, and output estimates (`6,805` tokens) are modeled constants. See [METRICS.md](METRICS.md) and [BENCHMARK_REPORT.md](BENCHMARK_REPORT.md).

| Benchmark Scenario | Task Complexity | Baseline Tokens | TokenSafe Tokens | Reduction | Turn Speedup | Accuracy |
|---|---|---|---|---|---|---|
| **SWE-06: Zero-Token Architecture Discovery** | God Node indexing vs. crawl | 49,716 | **312** | **-99.4%** | **6 → 1 turns (+83%)** | 100% Pass |
| **SWE-09: Repeat-Read Pointer Dedup** | `AgentFirewall` unchanged pointer | 17,388 | **208** | **-98.8%** | **2 → 1 turns (+50%)** | 100% Pass |
| **SWE-03: Monorepo Lockfile Git Diff** | Monorepo branch diff | 18,911 | **761** | **-96.0%** | 2 turns | 100% Pass |
| **SWE-07: Graph-Guided AST Symbol Slicing** | `dep_mode="signature"` + collapsed imports | 26,023 | **1,194** | **-95.4%** | **4 → 2 turns (+50%)** | 100% Pass |
| **SWE-10: Parametric Distillation Slot Cache** | Slot template hit (`0` LLM tokens) | 2,814 | **133** | **-95.3%** | **2 → 1 turns (+50%)** | 100% Pass |
| **SWE-08: Monorepo Lockfile Grep Leak** | `git grep` across lockfiles | 10,111 | **491** | **-95.1%** | 2 turns | 100% Pass |
| **SWE-01: Race Condition / Distributed Lock** | AST query & Redis redlock | 5,046 | **414** | **-91.8%** | **4 → 3 turns (+25%)** | 100% Pass |
| **SWE-05: Multi-Turn History Compaction** | 8-turn session history fold | 31,010 | **3,130** | **-89.9%** | 8 turns | 100% Pass |
| **SWE-02: OAuth JWT Expiration Triage** | Controller bug investigation | 3,733 | **403** | **-89.2%** | **3 → 2 turns (+33%)** | 100% Pass |
| **SWE-04: CI Test Failure Extraction** | Full test log & stack trace | 5,009 | **1,127** | **-77.5%** | 3 turns | 100% Pass |

### Why "Up to 99%" (Multiplicative Math & Honest Boundaries)

TokenSafe combines two multiplicative savings layers rather than relying on AST compression alone:

1. **Context Token Reduction (-85% to -99.4%):** Graph-guided `dep_mode="signature"` keeps only the edited symbol body intact while collapsing imports and 1-hop dependency implementations into signatures (`-95.4%` in `SWE-07`), Architecture Discovery maps repos in `< 350` tokens vs. full crawls (`-99.4%` in `SWE-06`), and repeat reads resolve to ~75-token integrity pointers (`-98.8%` in `SWE-09`, or `-99.56%` on raw file re-reads).
2. **KV-Cache Prefix Locking (`90.8%` hit rate at `0.10x` cached-read rate):** The Append-Only Epoch Governor (`ContextGovernor`) freezes history prefixes monotonically up to 80% of the model context window while `PromptCacheNormalizer` strips volatile metadata, sorts tool schemas, and injects provider `cache_control` breakpoints / `prompt_cache_key`. In a live 20-turn replay over `src/*.py` (`BENCHMARK_REPORT.md`):

| Multi-Turn 20-Turn Replay Metric | Value | Comparison |
|---|---|---|
| **Byte-Identical KV-Cache Prefix Hit Rate** | **`90.8%`** | `535,491 / 589,846` input tokens |
| **20-Turn Context Input Tokens** | **`-84.6%`** | `3,837,648` ➔ `589,846` |
| **Claude Sonnet 4.5 Input Bill (vs. Uncached)** | **`-96.8%`** | Cached input reads @ `$0.30/M` (`0.10x`) |
| **Claude Sonnet 4.5 Total Bill (vs. Uncached)** | **`-96.6%`** | `$11.6779` ➔ `$0.4005` (includes uncached `$15/M` outputs) |
| **Claude Sonnet 4.5 Total Bill (vs. Naive Mid-Trim Cache)** | **`-84.6%`** | `$2.5984` ➔ `$0.4005` |
| **DeepSeek V3 Total Bill (vs. Uncached)** | **`-96.9%`** | Cached reads `$0.028/M` (`0.10x`), outputs `$1.10/M` |

**Honest bounds:** When `~85–95%` fewer context tokens combine with a `90%+` KV-cache hit rate billed at `0.10x`, cached input spend approaches **1–2% of uncached cost (up to ~99% savings)** on graph-first, repeat-read, and cache-warm workflows. Total session invoices typically fall **80–97%** because newly generated output tokens and first-turn cache writes are never discounted by KV-caching.

> **How to read these numbers:** this benchmark is a **simulated** harness. Compression ratios and 20-turn KV-prefix byte matches are computed live from real files, while baselines and turn speedups are modeled. Production events in TokenSafe are explicitly labeled `measured` or `estimated` (see [METRICS.md](METRICS.md)).

### Real-Repository Benchmark (measured on live clones)

No modeling: fifteen popular repositories across 10 languages (Python, TypeScript, JavaScript, Go, Rust, Java, Ruby, PHP, C#, Swift, C) cloned at HEAD, scenarios **pre-registered before measurement** ([`src/bench_scenarios.json`](src/bench_scenarios.json)), every token counted on real bytes, and deterministic zero-loss gates that disqualify any scenario they fail. Curated rows (all rows in [docs/BENCHMARK_REAL.md](docs/BENCHMARK_REAL.md)):

| Repo (language) | Scenario | Baseline tok | TokenSafe tok | Reduction | Gates |
|---|---|---:|---:|---:|:---|
| lodash (JS) | Symbol read (AST skeleton) | 515,843 | **855** | **-99.8%** | PASS |
| lodash (JS) | Multi-turn + repeat reads | 1,640,674 | **4,233** | **-99.7%** | PASS |
| lodash (JS) | Architecture discovery | 802,825 | 178 | **-99.98%** | PASS |
| lodash (JS) | Junk-read guard | 87,475 | 1,745 | **-98.0%** | PASS |
| lodash (JS) | KV-cache 10-turn bill | 7,390,347 | 1,567,062 | **-78.8%** | PASS |
| fastapi (Py) | Junk-read guard (uv.lock cap) | 367,129 | **855** | **-99.8%** | PASS |
| flask (Py) | Architecture discovery | 53,237 | 176 | **-99.7%** | PASS |
| sinatra (Ruby) | Architecture discovery | 28,165 | 199 | **-99.3%** | PASS |
| composer (PHP) | Junk-read guard (composer.lock) | 33,103 | 1,645 | **-95.0%** | PASS |
| flask (Py) | Write egress (output axis, $15/M) | 7,106 | **44** | **-99.4%** | PASS |
| flask (Py) | Multi-turn + repeat reads | 45,336 | 5,304 | **-88.3%** | PASS |
| curl (C) | Symbol read (AST skeleton) | 125,168 | 31,174 | **-75.1%** | PASS |
| rich (Py) | Multi-turn + repeat reads | 80,036 | 12,329 | **-84.6%** | PASS |
| requests (Py) | Multi-turn + repeat reads | 59,380 | 9,561 | **-83.9%** | PASS |
| flask (Py) | Symbol read (AST skeleton) | 18,864 | 3,784 | **-79.9%** | PASS |
| rich (Py) | Symbol read (AST skeleton) | 28,675 | 7,710 | **-73.1%** | PASS |
| requests (Py) | Symbol read (AST skeleton) | 9,743 | 2,849 | **-70.8%** | PASS |
| sinatra (Ruby) | KV-cache 10-turn bill | 303,850 | 63,393 | **-79.1%** | PASS |
| retrofit (Java) | KV-cache 10-turn bill | 3,312,375 | 673,361 | **-79.7%** | PASS |
| gin (Go) | KV-cache 10-turn bill | 317,638 | 65,036 | **-79.5%** | PASS |
| zod (TS) | KV-cache 10-turn bill | 1,905,787 | 431,857 | **-77.3%** | PASS |
| serde (Rust) | KV-cache 10-turn bill | 1,307,460 | 300,472 | **-77.0%** | PASS |
| curl (C) | KV-cache 10-turn bill | 1,586,875 | 423,360 | **-73.3%** | PASS |
| newtonsoft (C#) | Symbol read (AST skeleton) | 56,076 | 17,871 | **-68.1%** | PASS |
| alamofire (Swift) | Symbol read (AST skeleton) | 13,909 | 8,100 | **-41.8%** | PASS |
| serde (Rust) | Symbol read (AST skeleton) | 69,610 | 42,671 | **-38.7%** | PASS |
| gin (Go) | Symbol read (AST skeleton) | 23,567 | 14,938 | **-36.6%** | PASS |
| flask (Py) | Secret guard (cat .env -> deny, 0 leak) | 153 | 82 | **-46.4%** | PASS |
| flask (Py) | Tree-sitter AST (13 langs) | 18,864 | 2,410 | **-87.2%** | PASS |
| fastapi (Py) | Reversible Hash Stashing (#hash) | 7,605 | 37 | **-99.5%** | PASS |
| rich (Py) | Context Tax & Ghost Token Audit | 13,425 | 699 | **-94.8%** | PASS |
| rich (Py) | Verbose test output (noise strip) | 746 | 385 | **-48.4%** | PASS |
| composer (PHP) | Prompt compaction (TOCP) | 138 | 46 | **-66.7%** | FAIL |
| flask (Py) | Full-suite pytest output | 6,402 | 6,191 | **-3.3%** | PASS |
| fastapi (Py) | Git diff churn -> slice | 416 | 393 | **-5.5%** | PASS |

Aggregate: **~25.7M measured tokens saved** per traced pass over all 15 repositories in 10 languages (142 gated-OK rows; input at `$3/M`, output axis at `$15/M`, KV-cache hits billed at `$0.30/M`). Clean pytest suites honestly score ~0-3% — savings are never invented. **17 gate-FAILs and 21 skips are published with reasons** on the live page (e.g. fastapi's test-output: strict warning filters escalate a `pytest-asyncio` deprecation into a pytest `INTERNALERROR`; whole-repo API surfaces bigger than hub crawls for fastapi/httpie; httpie's `core.py` refuses skeletonization — one function is most of the file). Full table + raw JSON: [docs/BENCHMARK_REAL.md](docs/BENCHMARK_REAL.md) · live page: <https://tokensafe.dev/bench> · methodology post: <https://tokensafe.dev/blog/real-repo-benchmark-5-repos>. Reproduce:

```bash
tokensafe bench --real                        # all 15 pre-registered repos
tokensafe bench --real --repo=pallets/flask   # one repo
tokensafe bench --real --here                 # your current repository
```

## Head-to-Head Competitor Benchmark (Measured on Real Repositories)

We cloned 8 popular open-source repositories across Python, Go, C, and Java, and tested **JayPokale/Chisle**, **alexgreensh/token-optimizer**, and **TokenSafe (v4.1.2)** on the exact same hub files and target functions. Every token was counted with a calibrated BPE tokenizer on real bytes.

Deterministic **zero-loss gates** disqualify any output where the code fails to compile/parse, or where the targeted function is missing. Savings without code correctness are just destructive truncation.

| Repository & Target File | Baseline Tokens | JayPokale / Chisle | alexgreensh / token-optimizer | TokenSafe (v4.1.2) | Zero-Loss Gate Result |
|:---|---:|---:|---:|---:|:---|
| **flask** (`src/flask/app.py`)<br>Target: `full_dispatch_request` | 18,864 | 18,864 (0.0%) | 317 (-98.3%)<br>❌ *GATE FAIL: SyntaxError / Symbol Dropped* | **3,784** (-79.9%) | **TokenSafe PASS**<br>Valid AST, target 100% intact |
| **requests** (`src/requests/sessions.py`)<br>Target: `Session.request` | 9,743 | 9,743 (0.0%) | 651 (-93.3%)<br>✅ *Heuristic match* | **2,849** (-70.8%) | **TokenSafe PASS**<br>Valid AST, target 100% intact |
| **fastapi** (`fastapi/routing.py`)<br>Target: `APIRouter.add_api_route` | 73,721 | 73,721 (0.0%) | 139 (-99.8%)<br>❌ *GATE FAIL: SyntaxError / Symbol Dropped* | **39,529** (-46.4%) | **TokenSafe PASS**<br>Valid AST, target 100% intact |
| **rich** (`rich/console.py`)<br>Target: `Console.print` | 28,675 | 28,675 (0.0%) | 585 (-98.0%)<br>❌ *GATE FAIL: SyntaxError / Symbol Dropped* | **7,710** (-73.1%) | **TokenSafe PASS**<br>Valid AST, target 100% intact |
| **httpie** (`httpie/core.py`)<br>Target: `main` | 2,933 | 2,933 (0.0%) | 266 (-90.9%)<br>✅ *Heuristic match* | **689** (-76.5%) | **TokenSafe PASS**<br>Valid AST, target 100% intact |
| **gin** (`context.go`, Go)<br>Target: `Context.Next` | 15,032 | 15,032 (0.0%) | 115 (-99.2%)<br>❌ *GATE FAIL: Unsupported Lang / Truncated* | **9,904** (-34.1%) | **TokenSafe PASS**<br>Native Tree-sitter Go grammar |
| **curl** (`lib/url.c`, C)<br>Target: `Curl_connect` | 23,246 | 23,246 (0.0%) | 204 (-99.1%)<br>❌ *GATE FAIL: Unsupported Lang / Truncated* | **5,343** (-77.0%) | **TokenSafe PASS**<br>Native Tree-sitter C grammar |
| **retrofit** (`Retrofit.java`, Java)<br>Target: `Retrofit.create` | 8,189 | 8,189 (0.0%) | 127 (-98.4%)<br>❌ *GATE FAIL: Unsupported Lang / Truncated* | **4,617** (-43.6%) | **TokenSafe PASS**<br>Native Tree-sitter Java grammar |

> **Key empirical takeaways:**
> - **Chisle scores 0.0% reduction on code reads**: its lifecycle hook hardcodes `const NEVER_COMPRESS = ['read', 'edit', 'write']` to avoid breaking diffs without an AST parser.
> - **token-optimizer failed 6 out of 8 zero-loss gates**: on Python files, its `structure_map.py` emits invalid pseudo-YAML text outlines and caps methods at 4 (`MAX_SKELETON_METHODS_PER_CLASS = 4`), discarding up to 56 methods including the target function. On Go, C, and Java, it performs blind regex truncation.
> - **TokenSafe achieves 34.1% to 79.9% real token reduction with a 100% Gate PASS rate**: using native Tree-sitter AST polyglot grammars, TokenSafe keeps 100% of the target function's executable body intact byte-for-byte, produces valid syntax, and enables 0ms bit-exact restoration via `#hash` and `expand_ref`.

## Architectural Comparison: TokenSafe vs. Competitors

| Capability | JayPokale / Chisle | alexgreensh / token-optimizer | TokenSafe (v4.1.3) |
|---|---|---|---|
| **Parsing & AST Engine** | None (Markdown rulesets only) | Regex & heuristic bracket lexers | **Native Tree-sitter AST (13 languages)** with zero-loss fallback |
| **Context Reversibility** | Irreversible (bash pipe cut) | Disk archiving with shell expand command | **Reversible Hash Stashing (`#hash` + `expand_ref` 100% byte recovery)** |
| **Integration Surface** | System prompt instructions | Claude Code & Codex hooks wrapper | **18-tool MCP Server + universal proxy** (Cursor, Claude, Antigravity, Windsurf, Codex, Gemini) |
| **Pre-Git Security Guard** | None | None | **Sub-30ms interception**: blocks `.env` reads, hardcoded fallbacks in `os.environ.get`, & dangerous shell commands |
| **KV-Cache Prefix Locking** | None | Session cache hints | **Monotonic Append-Only Epoch Governor** (90.8% hit rate at 0.10x cached rate) |
| **Environment Context Tax** | None | Claude Code audit command | **`tokensafe doctor`**: S–F grading + multi-IDE redundant rule pruning (Ghost Tokens) |
| **Polyglot Language Scope** | Prompt-only | Python, TS/JS heuristics | **13 polyglot languages**: Python, TS, JS, Go, Rust, Java, C#, C, C++, PHP, Kotlin, Swift, Ruby |
| **Team FinOps & Telemetry** | None | Local SQLite database | **Local SQLite + Cloud Team Dashboard** (`measured` vs `estimated` audit trail) |

### Why token-optimizer Reports Smaller Token Numbers (and Why It Fails Zero-Loss Gates)

When running benchmarks on large repositories, developers often ask: *Why does token-optimizer show 317 tokens on Flask while TokenSafe shows 3,784 tokens?*

The answer lies in what each tool actually passes to the model:

1. **Pseudo-YAML vs. Executable Code:** `token-optimizer` replaces Python source code with a plain text outline (`lines: 1687\nimports (50):\nclasses (1): ...`). This is not valid Python syntax; running `ast.parse()` on it raises an immediate `SyntaxError`.
2. **Arbitrary Method Dropping:** In `structure_map.py`, token-optimizer enforces `MAX_SKELETON_METHODS_PER_CLASS = 4`. Flask's `App` class defines over 60 methods. token-optimizer took the first 4 methods and discarded the other 56 methods, including the exact target function `full_dispatch_request` the agent was supposed to inspect and edit!
3. **The Book Analogy:** Tearing out 98% of the pages in a novel and handing someone only a 4-line table of contents reduces token count by 98%, but completely destroys the chapter. If an agent cannot see the function body, it cannot fix bugs or generate valid diffs; it is forced to hallucinate code.
4. **TokenSafe's Zero-Loss Guarantee:** TokenSafe reduces Flask from 18,864 down to 3,784 tokens (-79.9%) using native Tree-sitter AST parsing. It preserves 100% of the target function's executable body byte-for-byte, keeps 1-hop typed caller contracts, produces 100% valid Python syntax, and allows any folded block to be recovered via `#hash` and `expand_ref`.
5. **Why Chisle Shows 0% on File Reads:** JayPokale/Chisle lacks an AST parser. To prevent models from hallucinating edits against missing code, its lifecycle hook hardcodes `const NEVER_COMPRESS = ['read', 'edit', 'write']`. As a result, reading code files (the largest source of context consumption) passes 100% uncompressed into context.

### Why Alternative Approaches Fall Short

1. **Prompt Engineering Alone (Chisle) Cannot Enforce Contracts:**
   Prompt rulesets like Chisle ("be concise", "caveman prose", "YAGNI code") rely entirely on the LLM's willingness to follow negative instructions. As context grows past 10–15 messages, models suffer *Lost in the Middle* amnesia, ignore prompt rules, and revert to dumping 2,000 lines of boilerplate. Furthermore, truncating bash command outputs via shell pipes permanently destroys tracebacks and compiler errors, causing agents to enter infinite repair loops.
2. **Heuristic Regex Slicing (token-optimizer) Breaks on Real Codebases:**
   Regex-based AST slicing fails when parsing modern polyglot codebases with nested generics (`<T extends Map<K, V>>`), decorators, async generators, and multi-line macros. TokenSafe uses **native C Tree-sitter grammars across 13 languages** with exact start/end byte offsets, eliminating bracket miscounts while preserving 1-hop caller contracts.
3. **The Zero-Loss Invariant (`#hash` & `expand_ref`):**
   Unlike tools that irreversibly discard folded content, TokenSafe hashes every compressed artifact into an 8-character anchor (`[TokenSafe folded: #a1b2c3d4 ...]`). Any agent can call `tokensafe:expand_ref('a1b2c3d4')` to retrieve 100% bit-exact original bytes in 0ms without re-running commands.
4. **Pre-Git Security vs. Blind Agents:**
   Autonomous coding agents frequently run `git add .` containing `.env` files or introduce hardcoded API keys as fallback parameters in environment lookups. TokenSafe is the only tool with an inline security guard that blocks both credential fallbacks and secret file reads locally before anything reaches LLM transcripts or git commits.

## Metrics Honesty

TokenSafe labels every savings event as one of:

- **`measured`**: the model literally received fewer bytes than the tool produced (sliced file reads, filtered command output, AST skeletons).
- **`estimated`**: the model received a compact artifact and saved tokens are counted against a reasonable baseline (architecture graph vs. a full repo crawl; folded history digest injected while raw history stays in context).

Totals always display the split (`X metered · Y est.`). When a live metric is missing, the UI shows `—` rather than a placeholder number. USD figures are derived approximations (`tokens × $1.5 / 1M`), not provider invoices. Full contract: **[METRICS.md](METRICS.md)**.

## Pricing and 7-Day Team Trial

TokenSafe follows an open-core model: verify local context savings and guardrails on your own repo first, then roll out team caching, org policies, and per-seat ROI.

| Plan | Price | Monthly Allowance | Included Capabilities |
|---|---|---|---|
| **Developer Sandbox** | **$0** forever | **500,000 tokens / mo** | 9-language local regex compactor, local AST slicer CLI, local secret & `.env` guard, SQLite & terminal dashboard |
| **Engineering Team** *(Recommended)* | **$29 / seat / mo** *(~$24 / seat / mo billed $290/yr)* | **Unlimited** | **7-Day Free Trial**, **shared team cache (L3 monorepo hits)**, org-wide guard & git leak shield, Friday per-seat ROI digest, centralized seat provisioning & revoke, managed cloud distillation (zero keys needed) |
| **Enterprise & VPC** | **Custom** | **Unlimited** | Org audit log (guard forensics: who / what / when, CSV & SIEM export), central guard policies, self-hosted VPC proxy (private BYOK), zero-telemetry / air-gapped mode, SAML / OIDC SSO, dedicated onboarding & SLA |

*Working solo? [Individual Solo plans](https://tokensafe.dev#pricing) start at **$9 / mo** ($89 / yr).*

`7-Day Free Trial · Offline Ed25519 Seat Keys (TS2.*) · Zero Source Code Transmitted · Cancel anytime`

**[Start a 7-Day Team Trial](https://tokensafe.dev#pricing)** &nbsp;&nbsp; **[Run Free Locally](#install--agents)**

## FAQ

**Does my source code leave my machine?**
No. Slicing, guarding, compaction, and metrics run locally. The cloud receives only counters (token totals and event types), never file contents or prompts. Set `TOKENSAFE_TELEMETRY_DISABLED=1` to disable all telemetry sync; local features keep working.

**How does offline license verification work?**
License keys are `TS2.*` tokens signed with Ed25519. Your client verifies the signature offline against an embedded public key and caches the result for up to an hour. Enforcement never requires a network round trip.

**What do `measured` and `estimated` mean?**
`measured` means the model literally received fewer bytes than the tool produced. `estimated` means savings are counted against a reasonable modeled baseline. The dashboard always shows the split and never invents numbers for missing data.

**What exactly does the $29/seat plan include?**
Unlimited compaction and managed cloud distillation (zero API keys for developers), the shared L3 monorepo cache, org-wide guard policies, the Friday per-seat ROI digest, and centralized seat provisioning and revocation. Billed annually it is $290/seat/year (~$24/seat/mo).

**Can we self-host?**
The Enterprise & VPC plan covers a private VPC Docker proxy with BYOK provider keys, zero-telemetry / air-gapped mode, and SAML/OIDC SSO, deployed together with the TokenSafe engineering team: [corp@tokensafe.dev](mailto:corp@tokensafe.dev).

**What happens if a hook fails?**
All hook adapters fail open: an internal error never stalls your agent. Failures are logged locally so they can be reported and fixed, not silently swallowed.

## Reference

<details>
<summary><b>Local MCP tools (18)</b></summary>

| Tool | What it does |
|---|---|
| `get_architecture_graph` | Architectural hotspots, dependency topology, and God Nodes detection before multi-file reading (persisted in SQLite cache) |
| `get_api_surface` | Compact markdown map of all exported interfaces, classes, and types |
| `smart_read_file` | AST-skeletonized file read preserving a target symbol and 1-hop dependencies; OpenAPI/Prisma/GraphQL/SQL auto-slice; lockfiles/CSV/TSV/SQL dump auto-reduction with reversible stash |
| `smart_bundle` | 3–8 related symbols across files in one call: merged skeletons, deduplicated shared imports, unified 1-hop signatures |
| `scoped_search` | Sub-millisecond keyword and symbol search powered by native SQLite FTS5 trigram index with BM25 relevance ranking (<1ms) |
| `expand_ref` | Reversible stash expansion: recovers original un-truncated content by its 8-char hex hash anchor (`#a1b2c3d4`) without re-running tools |
| `read_web_page` | Web reader & HTML-to-Markdown compactor: strips scripts, styles, navbars, and cookie banners (-80% to -95% tokens) |
| `optimize_image` | Downscales oversized visual assets (>1024px) via Pillow or macOS `sips`, saving 50–75% vision tokens |
| `prune_superseded` | Prunes obsolete intermediate tool reads that were superseded by subsequent edits or re-reads in long agent transcripts (-30-40% context) |
| `get_mistakes` | Anti-stuck persistent ledger: retrieves past dead-ends, loop guard trips, and git reverts to prevent repeating failed paths |
| `list_dir` | Clean directory tree without permissions, timestamps, or lockfiles |
| `slice_diff` | Unified diff slicing omitting lockfiles and minimizing context lines |
| `sanitize_command` | Per-stage shell command rewrites (`git push` --no-progress, `git commit` hook wrapping, bun/python/jest test folding, lockfile exclusions, bounded logs) |
| `guard_inspect` | Pre-flight security and hygiene audit for commands or code snippets |
| `context_budget` | Context window usage estimate with thresholds and recommendations |
| `compress_prompt` | Compiles a verbose developer prompt into a compact S-expression |
| `compact_conversation` | Folds a long agent transcript into a compact state ledger |
| `get_token_savings_metrics` | Cumulative token and cost savings analytics |
</details>

<details>
<summary><b>Cloud MCP tools (13)</b></summary>

Endpoint: `https://api.tokensafe.dev/mcp`, auth `Authorization: Bearer <TS1./TS2. key>`.

| Tool | Access | What it does |
|---|---|---|
| `get_public_stats` | Public | Aggregate product statistics |
| `check_latest_version` | Public | Latest published version and update banner |
| `get_setup_instructions` | Public | Copy-paste MCP snippets per agent |
| `search_docs` | Public | Search public documentation |
| `get_license_status` | Licensed | Active tier, seat, and trial state |
| `get_team_metrics` | Licensed | Team savings metrics with `measured` / `estimated` split |
| `distill_prompt` | Licensed | Managed cloud prompt distillation (zero API keys) |
| `team_cache_lookup` | Licensed | Shared L3 team cache lookup |
| `team_cache_store` | Licensed | Shared L3 team cache store |
| `list_invoices` | Licensed | Billing history |
| `generate_team_seat` | Licensed | Provision a signed `TS2.*` seat key |
| `revoke_team_seat` | Licensed | Revoke an active seat key |
| `preview_weekly_digest` | Licensed | Preview the Friday team ROI digest |
</details>

<details>
<summary><b>Full CLI reference (30 commands)</b></summary>

```text
tokensafe stats / markdown / html     Savings analytics (terminal / .md report / dashboard)
tokensafe search <query> [--path <p>] Fast SQLite FTS5 BM25 code search (<1ms)
tokensafe index [dir] [--clear]       Index repository into SQLite FTS5 trigram database
tokensafe expand-ref <hash8>          Restore folded tool/command/file result by its 8-char hash
tokensafe optimize-image <path>       Downscale image >1024px via Pillow or macOS sips
tokensafe prune-superseded <path>     Prune obsolete intermediate tool reads from transcript
tokensafe mistakes [list|record|clear] Anti-stuck dead-ends ledger & prompt guard
tokensafe web <url>                   Fetch web page/docs and print clean compact Markdown
tokensafe wrap <command>              Run command with compact output folding & ANSI stripping
tokensafe doctor [--cleanup]          Audit MCP tool overhead, ghost tokens & conflicts
tokensafe benchmark                   Zero-context-loss benchmark suite (simulated harness)
tokensafe bench --real                Measured benchmark on real repos (zero-loss gates)
tokensafe graph / map / skeleton      Architecture graph / API surface / AST skeleton of a file
tokensafe test "<prompt>"             Preview prompt compaction on custom input
tokensafe guard "<command>"           Pre-flight safety check for a shell command
tokensafe guard audit [path]          Recursive source audit for secrets & vulnerabilities
tokensafe digest [--send]             Compile (and optionally dispatch) the weekly team digest
tokensafe mcp list|disable|enable     Manage configured MCP servers
tokensafe proxy [port]                Local transparent AI proxy (127.0.0.1:8765/v1)
tokensafe proxy on/off/status         Daemon + agent wiring with one-command rollback
tokensafe install / setup [--all]     Configure detected agent environments
tokensafe update / check-update       Self-update / check for a newer version
tokensafe activate <KEY>              Activate a Team or Solo license key
tokensafe login / logout              Authorize or unlink this device via browser
tokensafe license                     Show active tier and trial state
tokensafe providers                   List distillation providers and active mode
tokensafe sync                        Sync local telemetry with the cloud dashboard
tokensafe prune [--days N]            Compact metrics database (roll old events)
tokensafe vacuum                      Reclaim SQLite disk space
tokensafe tests [pytest]              Run the unit test suite (compact failure report)
tokensafe reset                       Reset all local token metrics
tokensafe --version                   Print version and exit
```
</details>

### Proxy mode & agent coverage (v3.0.0)

One command wires everything it safely can:

```bash
tokensafe proxy on      # installs a keep-alive daemon (launchd/systemd), wires Claude Code, prints manual steps for the rest
tokensafe proxy status  # health, wiring state, last traffic
tokensafe proxy off     # rollback: unwires agents (previous base URL restored) and removes the daemon
```

The daemon keeps the proxy alive on `127.0.0.1:8765`, `on` rewires agents only after a verified `/health` answer (a dead proxy never bricks an agent), and every wiring is backed up for `off`. `tokensafe install` and `tokensafe update` ask interactively whether to enable the proxy (skipped in non-TTY/scripted runs); prefer manual? Run `tokensafe proxy` in a terminal and point your agent's base URL at `http://127.0.0.1:8765` yourself:

| Agent | Route through proxy? | How |
|---|---|---|
| Claude Code | ✅ auto (`tokensafe proxy on`) | `ANTHROPIC_BASE_URL=http://127.0.0.1:8765` — the proxy ingests native Anthropic `/v1/messages` shape |
| Cline / Roo Code | ✅ manual | API Provider → OpenAI-compatible → Base URL `http://127.0.0.1:8765/v1` |
| Aider | ✅ manual | `--openai-api-base http://127.0.0.1:8765/v1` |
| Cursor (custom models) | ✅ manual | Add an OpenAI-compatible model with override base URL |
| Cursor (built-in models) | ❌ | Routed via Cursor's own backend — hooks only |
| Antigravity / ZCode | ❌ | Hooks only (lifecycle adapters) |
| Codex CLI | ❌ | stdio MCP + AGENTS.md (no proxy transport) |

What runs where:

- **Proxy-only (A/B/D)**: Tool Result Ledger (folds aged tool results in-flight, `TOKENSAFE_TOOL_LEDGER=0` to disable), session-stable cold-tool pruning (opt-in: `TOKENSAFE_TOOL_PRUNING=1`, `TOKENSAFE_TOOL_PRUNE_KEEP`, `TOKENSAFE_TOOL_PRUNE_ALLOWLIST`), managed-cloud history distillation (paid, opt-in: `TOKENSAFE_HISTORY_DISTILL=1`).
- **Hooks (all agents)**: PostToolUse stdout compaction, PreToolUse shell/secret guards, Output Guard steering full-file writes to surgical edits, prompt compaction, history folding.
- Folded originals are archived under `~/.tokensafe/data/tool_ledger/` and every fold carries a deterministic re-hydration anchor — nothing is destroyed, and already-folded results are never re-processed (KV-cache stable).

More documentation: [docs/AGENT_SETUP.md](docs/AGENT_SETUP.md) · [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · [docs/API.md](docs/API.md) · [METRICS.md](METRICS.md) · [BENCHMARK_REPORT.md](BENCHMARK_REPORT.md)

## Development and License

The client runs on Python 3.10+ with `cryptography>=42.0` as its sole runtime dependency for Ed25519 license checks; all AST slicing, SQLite metrics, MCP tooling, and guardrails run on the standard library ([details](docs/AGENT_SETUP.md#6-runtime-dependency-cryptography)).

```bash
# Run the unit test suite (compact failure report; full: --traceback / -v)
tokensafe tests
```

- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security policy and vulnerability reporting: [SECURITY.md](SECURITY.md)
- Metrics and honesty contract: [METRICS.md](METRICS.md)

MIT License. Commercial licenses are available for self-hosted B2B and enterprise VPC deployments. Questions: [corp@tokensafe.dev](mailto:corp@tokensafe.dev) · [tokensafe.dev](https://tokensafe.dev)
