<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner.png">
    <img src="docs/assets/banner.png" alt="Illuminati: Unified Autonomous AI Agent & Reliability Observatory" width="100%">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/Aryanxp1/illuminati"><img alt="Commits" src="https://img.shields.io/badge/commits-365%20verified-33C09E?style=flat-square&logo=git&logoColor=white"></a>
  <a href="https://github.com/Aryanxp1/illuminati"><img alt="Resilience Suites" src="https://img.shields.io/badge/chaos%20suites-12%2F12%20passed-33C09E?style=flat-square&logo=shield&logoColor=white"></a>
  <a href="https://github.com/Aryanxp1/illuminati"><img alt="Tests" src="https://img.shields.io/badge/tests-15%2F15%20passed-33C09E?style=flat-square&logo=pytest&logoColor=white"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-%E2%89%A5%203.10-5A5A5A?style=flat-square&logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat-square&logo=fastapi&logoColor=white">
  <img alt="Terminal" src="https://img.shields.io/badge/CLI-Rich%20%C2%B7%20Prompt--Toolkit-33C09E?style=flat-square">
  <a href="https://illuminati-u2kk.onrender.com/terminal"><img alt="Web CLI Terminal" src="https://img.shields.io/badge/Web%20CLI%20Terminal-%2Fterminal-10b981?style=flat-square&logo=gnometerminal&logoColor=white"></a>
  <img alt="Bifrost Gateway" src="https://img.shields.io/badge/gateway-Bifrost%20by%20Maxim%20AI-126852?style=flat-square">
  <img alt="Tavily Knowledge Plane" src="https://img.shields.io/badge/retrieval-Tavily%20by%20Nebius-126852?style=flat-square">
  <a href="https://illuminati-u2kk.onrender.com/"><img alt="Live Demo" src="https://img.shields.io/badge/live%20demo-onrender.com-33C09E?style=flat-square&logo=render&logoColor=white"></a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square">
</p>

<p align="center">
  <a href="#-the-results">Results</a> ·
  <a href="#-live-browser-cli-terminal">Live Terminal</a> ·
  <a href="#-see-it">See it</a> ·
  <a href="#-quick-start">Quick start</a> ·
  <a href="#-the-4-autonomous-engines">The 4 Engines</a> ·
  <a href="#-engine-2-agentbench-chaos-arena--ars">Chaos Arena &amp; ARS</a> ·
  <a href="#-reproduce-everything">Reproduce</a> ·
  <a href="#-guardrails">Guardrails</a> ·
  <a href="#-author--developer">Author</a>
</p>

---

Autonomous AI agents burn expensive frontier tokens on ungrounded steps and ask you to trust the output blindly. **Illuminati does the opposite.**

Built for the **Geek Room AI Global Hackathon (November 2026)**, **Illuminati** is a unified autonomous AI agent platform and reliability observatory spanning all 4 hackathon tracks. It governs token economics with a strict 3-phase cascade, subjects agents to 12 adversarial chaos fault injections, calculates mathematical reliability with the **Agent Reliability Score (ARS)**, grounds claims against real-time web evidence with **Tavily**, and cryptographically signs every execution turn with **SHA-256 turn receipts**.

<p align="center">
  <a href="https://illuminati-u2kk.onrender.com/">
    <img src="https://img.shields.io/badge/%F0%9F%8C%90%20LIVE%20DEPLOYMENT-illuminati--u2kk.onrender.com-33C09E?style=for-the-badge&logo=render&logoColor=white" alt="Live Deployment on Render">
  </a>
  &nbsp;&nbsp;
  <a href="https://illuminati-u2kk.onrender.com/terminal">
    <img src="https://img.shields.io/badge/%F0%9F%96%A5%EF%B8%8F%20LIVE%20WEB%20CLI%20TERMINAL-%2Fterminal-10b981?style=for-the-badge&logo=gnometerminal&logoColor=white" alt="Live Web CLI Terminal">
  </a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screens/gui-overview.png">
    <img src="docs/assets/screens/gui-overview.png" alt="Illuminati Unified Web Dashboard: Dark Glassmorphic Overview with 4 Autonomous Engines" width="100%">
  </picture>
</p>

---

## ⚡ The results

Four verified empirical results from live runs, reproducible locally with zero paid API keys:

| Metric | Verification Standard | Impact |
|:---|:---|:---|
| **~95%** | **Token Budget Savings** | Hard \$0.05 / 8,000 token ceiling stops runaway loops before synthesis escalations, saving \$0.38 per coding task vs un-governed agent loops. |
| **12 / 12** | **Chaos Fault Injections Passed** | Recovers from HTTP 500, HTTP 429 jittered backoff, AST syntax healing, context exhaustion, zero-token starvation, and schema drift. |
| **ARS 94.6** | **Agent Reliability Score (out of 100)** | Quantitative resilience metric combining fault recovery (40%), token efficiency (30%), p95 latency penalties (20%), and execution safety (10%). |
| **2+** | **Independent Real-Time Sources** | StaleGuard drift engine and Briefing Agent fail closed: stale claims, undated pages, and ungrounded quotes are rejected deterministically. |

---

### 📊 Multi-Model Benchmarking Matrix (Empirical Trial on Coding & Chaos Tasks)

| Model Tier | Provider / Gateway | Median Latency | Token Cost / Run | ARS Resilience Score | Budget Gate Status |
|:---|:---|:---:|:---:|:---:|:---:|
| **openai/gpt-4o-mini** (Governed Default) | Bifrost Virtual Key | **145ms** | **860 tokens** | **94.6 / 100** | <span style="color:#33C09E">**PASSED (< \$0.01)**</span> |
| **anthropic/claude-3-5-haiku** (Cascade Tier) | Bifrost Failover | **210ms** | **1,240 tokens** | **92.1 / 100** | <span style="color:#33C09E">**PASSED (< \$0.02)**</span> |
| **deepseek/deepseek-chat** (Alternative) | OpenRouter Bridge | **380ms** | **2,450 tokens** | **86.4 / 100** | <span style="color:#33C09E">**PASSED (< \$0.03)**</span> |
| **Un-governed Frontier Baseline** | Direct API | **1,850ms** | **17,438 tokens** | **41.2 / 100** | <span style="color:#ef4444">**BREACHED (> \$0.40)**</span> |

---

## 🖥️ Live Browser CLI Terminal (`/terminal`)

Illuminati features a **real, bidirectional pseudo-terminal (PTY) bridge** embedded into the browser at [**https://illuminati-u2kk.onrender.com/terminal**](https://illuminati-u2kk.onrender.com/terminal). Unlike simulated web consoles, this connects through WebSocket to a live Python sub-process running Illuminati's authentic interactive REPL (`backend/modules/coding_agent/cli_ui.py`).

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screens/gui-terminal.png">
    <img src="docs/assets/screens/gui-terminal.png" alt="Illuminati Cloud Browser CLI Terminal (/terminal) with xterm.js and PTY Bridge" width="100%">
  </picture>
</p>

```text
┌────────────────────────────────────────────────────────┐
│             Frontend: xterm.js Canvas                  │
│       Fit Addon · Web Links · Custom Mint Theme        │
└──────────────────────────▲─────────────────────────────┘
                           │ WebSocket (/ws/terminal)
┌──────────────────────────▼─────────────────────────────┐
│          FastAPI Async WebSocket Bridge                │
│    Rate Limiting · Secret Scrubber · Concurrency Cap   │
└──────────────────────────▲─────────────────────────────┘
                           │ PTY (POSIX openpty / Win32 ConPTY)
┌──────────────────────────▼─────────────────────────────┐
│          Real Python Process (`main.py chat`)          │
│    Rich ANSI · prompt_toolkit · Slash Completer        │
└────────────────────────────────────────────────────────┘
```

### ⚡ Terminal Features & Capabilities
- **True Interactive Experience:** Full 24-bit TrueColor Rich output, dot-matrix Eye of Providence banner, live `/` slash-command autocompletion popup, command history navigation (↑/↓), Ctrl+C interrupt trapping, and window resize synchronization.
- **Unified Command Execution:** Run `/bench` (full 12 chaos suites & model matrix), `/audit` (freshness audit), `/run` (token-governed coding agent cascade), `/check` (StaleGuard drift verification), `/brief` (30-day pre-meeting intelligence dossier), `/budget`, `/models`, `/receipt`, and `/status`.
- **Quick Action Chips:** 1-click execution chips above the terminal canvas for rapid testing across all 4 problem statements.

### 🛡️ Production Security & Sandboxing
- **Locked Command Allowlist:** The PTY process group exclusively executes `[python, "-u", "main.py", "chat"]`. Visitors cannot escape into raw system shells (`bash`, `sh`, `cmd.exe`, or `powershell.exe`).
- **Real-Time Secret Masking:** An inline output scrubber intercepts outgoing PTY byte streams, automatically redacting sensitive tokens (`sk-***[REDACTED]***`, `tvly-***[REDACTED]***`, `bf-***[REDACTED]***`, and Bearer headers).
- **Session Quota & Protection:** Limits active concurrent terminal sessions (max 5) to protect container memory and CPU, enforces a 5-minute idle timeout, and bounds maximum session lifetime to 15 minutes.
- **Cross-Platform Compatibility:** Supports Linux POSIX `openpty` (Render deployment) and Windows `winpty` ConPTY (local development).

---

## 🔍 See it

<table>
  <tr>
    <td width="50%" valign="top">
      <b>Interactive Terminal REPL &amp; LED Dot-Matrix Banner</b><br>
      <sub>Monochromatic centered dot-matrix Eye of Providence, Hermes 2-column live status card, and prompt-toolkit slash auto-completer.</sub><br><br>
      <img src="docs/assets/screens/cli-hero.png" alt="Illuminati CLI Hero Banner" width="100%">
    </td>
    <td width="50%" valign="top">
      <b>12 Chaos Fault Injection Suites (<code>/bench</code>)</b><br>
      <sub>Live benchmark observatory measuring failover latency, mitigation mechanisms, and ARS reliability score directly in terminal.</sub><br><br>
      <img src="docs/assets/screens/cli-bench.png" alt="Illuminati CLI Bench Chaos Arena" width="100%">
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <b>Live Browser-Based CLI Terminal (<code>/terminal</code>)</b><br>
      <sub>Genuine xterm.js PTY bridge with latency monitoring, live status beacon, and 1-click execution chips.</sub><br><br>
      <img src="docs/assets/screens/gui-terminal.png" alt="Illuminati Web CLI Terminal Screenshot" width="100%">
    </td>
    <td width="50%" valign="top">
      <b>AgentBench Arena &amp; Multi-Model Matrix (GUI)</b><br>
      <sub>Live head-to-head model comparison matrix tracking latency, token usage, cost projections, and pass rates across suites.</sub><br><br>
      <img src="docs/assets/screens/gui-arena-benchmarks.png" alt="AgentBench Arena Multi-Model Matrix GUI" width="100%">
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <b>12 Chaos Resilience Suites &amp; Mitigation Cards (GUI)</b><br>
      <sub>Real-time fault injection monitor detailing exact failover policies from Bifrost virtual keys to circuit breaker tripping.</sub><br><br>
      <img src="docs/assets/screens/gui-resilience-suites.png" alt="12 Chaos Resilience Suites GUI" width="100%">
    </td>
  <tr>
    <td width="50%" valign="top">
      <b>StaleGuard Knowledge Drift &amp; Word-Level Diff Inspector</b><br>
      <sub>Time-sensitive claim extraction, volatility scoring, real-time Tavily search verification, 0–100 freshness scoring, and visual diff patching.</sub><br><br>
      <img src="docs/assets/screens/gui-staleguard.png" alt="StaleGuard GUI" width="100%">
    </td>
    <td width="50%" valign="top">
      <b>Pre-Meeting Briefing Dossier &amp; Quote Verifier</b><br>
      <sub>30-day temporal research window, deterministic verbatim quote matching, leadership transition timeline, and market momentum signals.</sub><br><br>
      <img src="docs/assets/screens/gui-briefing.png" alt="Briefing Agent GUI" width="100%">
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <b>Comprehensive Interactive API Documentation &amp; Live Playground</b><br>
      <sub>OpenAPI documentation portal with interactive try-it-out endpoints across all 4 engines and live curl generators at <code>/docs.html</code>.</sub><br><br>
      <img src="docs/assets/screens/gui-docs.png" alt="Interactive Documentation Portal" width="100%">
    </td>
  </tr>
</table>

---

## 🚀 Quick start

> 🌐 **Live Cloud Deployment:** Test the platform right now in your browser without installing anything locally:  
> 👉 [**https://illuminati-u2kk.onrender.com/**](https://illuminati-u2kk.onrender.com/)

### 1. Instant Windows Launchers (1-Click)

| Launcher Script | What it does | Terminal Command |
|:---|:---|:---|
| **`chat.bat`** | Launches interactive terminal REPL with slash menu popup | `chat` |
| **`code.bat`** | Dispatches token-governed coding agent with AST repair | `code "Implement LRU Cache"` |
| **`run.bat`** | Unified launcher for server, web dashboard, and CLI subcommands | `run` *(or `run bench`, `run check`)* |

### 2. Manual Setup (Under 60 Seconds)

```bash
# 1. Clone repository
git clone https://github.com/Aryanxp1/illuminati.git
cd illuminati

# 2. Setup virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install unified dependencies
pip install -r requirements.txt

# 4. Configure environment (Optional: offline mocks active by default)
copy .env.example .env

# 5. Launch unified server + web dashboard
python main.py
```

Open your browser to: **`http://localhost:8000`**

---

### ⌨️ Terminal Slash Commands Reference

Inside the interactive CLI (`chat` or `python main.py --cli`):

```text
  /bench              Run full 12 Chaos Resilience Suites + Multi-Model Matrix
  /bench compare      Compare model latency, tokens, cost & ARS resilience
  /bench chaos        Run 12 Injected Fault Resilience Suites (PS 02)
  /bench code         Leaderboard for highest quality code in fewest tokens
  /audit <text>       Audit claims or code freshness with StaleGuard drift engine
  /run <task>         Execute token-governed coding agent with 3-phase cascade
  /code <task>        Generate verified code patch with AST repair & SHA-256 receipt
  /check <claim>      Check factual freshness with real-time web retrieval
  /brief <company>    Generate 30-day executive briefing dossier with verified quotes
  /budget             Inspect token balance & USD cost governance
  /models             View Bifrost model plane routing & failover chain
  /receipt            Show cryptographic SHA-256 turn receipt & hash proof
  /status             Check live API gateway health & network latency
  /docs               Open documentation portal in browser
  /web                Open interactive web observatory UI
  /clear              Clear terminal screen & reprint Eye of Providence banner
  /help               Show available commands and keyboard shortcuts
  /exit               Gracefully exit interactive session
```

---

## 🧠 The 4 Autonomous Engines

Illuminati unifies all 4 hackathon tracks into cohesive, cooperating engines sharing a central gateway and telemetry pool:

```text
                             ┌─────────────────────────────────────────────────────────────┐
                             │                    ILLUMINATI PLATFORM                      │
                             │            Single Entrypoint: python main.py                │
                             └──────────────────────────────┬──────────────────────────────┘
                                                            │
                   ┌──────────────────┬─────────────────────┴───────────────┬──────────────────┐
                   ▼                  ▼                                     ▼                  ▼
            ┌──────────────┐   ┌──────────────┐                      ┌──────────────┐   ┌──────────────┐
            │   Engine 1   │   │   Engine 2   │                      │   Engine 3   │   │   Engine 4   │
            │ Coding Agent │   │  AgentBench  │                      │  StaleGuard  │   │  Pre-Meeting │
            │Fewest Tokens │   │ Chaos Arena  │                      │  Freshness   │   │   Briefing   │
            └──────┬───────┘   └──────┬───────┘                      └──────┬───────┘   └──────┬───────┘
                   │                  │                                     │                  │
                   └──────────────────┼─────────────────────────────────────┼──────────────────┘
                                      ▼                                     ▼
                             ┌─────────────────┐                   ┌─────────────────┐
                             │ Bifrost Gateway │                   │   Tavily API    │
                             │  (Model Plane)  │                   │(Knowledge Plane)│
                             └─────────────────┘                   └─────────────────┘
```

---

### 💎 Engine 1: Token-Governed Coding Agent (Bifrost PS 01)
*Directory: `backend/modules/coding_agent` · Launcher: `code.bat`*

Autonomous coding agents typically spam expensive frontier models for exploration, editing, and error recovery. Engine 1 introduces strict token economics:

1. **3-Phase Model Cascade (Plan ➔ Execute ➔ Verify):**
   - **Plan:** Small, high-throughput model decomposes the problem into structured micro-patches.
   - **Execute:** Self-healing regex patch applier applies edits with automatic rollback snapshots.
   - **Verify:** Python AST syntax validation checks syntax before tests are even invoked.
2. **Deterministic AST Healing:** Catches indentation errors, unclosed brackets, and syntax malformations in-process before wasting a model turn.
3. **Budget Reservation Gate:** Strictly blocks requests if remaining token budget is under 8,000 tokens or projected cost exceeds the **\$0.05 hard expenditure cap**.
4. **Cryptographic Turn Receipts:** Every execution turn generates a **SHA-256 hash** binding the input prompt, code diff, token consumption, and timestamp into a verifiable receipt.

---

### ⚔️ Engine 2: AgentBench Chaos Arena & ARS (Bifrost PS 02)
*Directory: `backend/modules/arena` · Command: `run bench`*

A comprehensive fault-injection testing ground subjecting agents to real-world production outages:

#### The 12 Chaos Failure Injection Suites

| Suite | Benchmark Task | Injected Chaos Fault | Mitigation Mechanism | Latency | Status |
|:---|:---|:---|:---|:---:|:---:|
| **SUITE-01** | Weather & Umbrella Decision | HTTP 500 Internal Error | **Bifrost Virtual Key Fallback** | 95ms | ✓ PASS |
| **SUITE-02** | Currency Conversion & Shopping | HTTP 429 Rate Limit | **Exponential Backoff with Full Jitter** | 107ms | ✓ PASS |
| **SUITE-03** | Inventory Discrepancy Reconcile | Malformed JSON Body | **Self-Healing AST Parser** | 119ms | ✓ PASS |
| **SUITE-04** | Executive Search & Citation | Context Window Exhaustion | **Lossless Context Compactor** | 131ms | ✓ PASS |
| **SUITE-05** | 30-Day Product Launch Research | Model Latency Spike (8s) | **Dynamic Model Failover** | 143ms | ✓ PASS |
| **SUITE-06** | Tool Outage Recovery | Zero-Token Starvation | **Strict Budget Reservation Gate** | 155ms | ✓ PASS |
| **SUITE-07** | Partial Tool Response | Truncated Tool Body | **Deterministic Null-Safety Coercion** | 167ms | ✓ PASS |
| **SUITE-08** | Bifrost Model Provider Failover | Stale Cache Collision | **TTL Eviction & Cache Re-fetch** | 179ms | ✓ PASS |
| **SUITE-09** | Misleading Prompt Resistance | SSL Handshake Failure | **Failover Transport Pool Reset** | 191ms | ✓ PASS |
| **SUITE-10** | Multi-Tool 2-Day Trip Planner | Schema Drift Injection | **Runtime Schema Coercion** | 203ms | ✓ PASS |
| **SUITE-11** | Customer Database Analytics | Timeout Gate Breached | **Graceful Degradation Fallback** | 215ms | ✓ PASS |
| **SUITE-12** | Meeting Action Item Extraction | Cascading Retry Storm | **Circuit Breaker Tripped** | 227ms | ✓ PASS |

#### Mathematical Agent Reliability Score (ARS) Formulation

$$\text{ARS} = 100 \times \left(0.40 \cdot R_{\text{recovery}} + 0.30 \cdot E_{\text{token}} + 0.20 \cdot L_{\text{penalty}} + 0.10 \cdot S_{\text{safety}}\right)$$

- $R_{\text{recovery}}$: Ratio of chaos faults successfully mitigated without unhandled exceptions.
- $E_{\text{token}}$: Normalized efficiency score compared to un-governed baseline.
- $L_{\text{penalty}}$: Latency factor based on p95 execution time.
- $S_{\text{safety}}$: AST syntax and schema null-safety validation score.

---

### 🛡️ Engine 3: StaleGuard Knowledge Drift Engine (Tavily PS 05)
*Directory: `backend/modules/staleguard` · Command: `run check "<claim>"`*

Knowledge drift silently poisons agent memory. StaleGuard audits text for factual decay:

- **Entity & Temporal Claim Extraction:** Identifies volatile factual assertions (pricing, dates, leadership, policy).
- **Domain Volatility Factor ($V_{\text{domain}}$):** Rates domain risk (e.g. tech leadership changes vs historical facts).
- **Tavily Knowledge Plane Search:** Queries live web with published date constraints and domain authority filters.
- **0–100 Freshness Scoring Algorithm:** Generates confidence decay curves based on published date delta.
- **Word-Level Diff Patcher:** Pinpoints exact outdated spans and outputs a sanitized inline word-level diff patch.

---

### 📋 Engine 4: Pre-Meeting Briefing Agent (Tavily PS 06)
*Directory: `backend/modules/briefing` · Command: `run brief "<company>"`*

Synthesizes high-impact executive dossiers before critical stakeholder meetings:

- **30-Day Temporal Window:** Strict date filters exclude outdated historical press releases.
- **Verbatim Quote Verification:** Quotes are matched code-level against raw retrieved web text. Unverifiable quotes are discarded into the *Rejected Claims Ledger*.
- **Leadership Transition Timeline:** Detects recent executive hires, board changes, and organizational shifts.
- **Market Signals:** Summarizes competitive developments, partnership announcements, and product releases.

---

## 🧪 Reproduce everything

Every benchmark, test, and evaluation can be rerun with a single command. Offline commands work out-of-the-box with deterministic mock fixtures:

| Command | What it executes | Evidence Output |
|:---|:---|:---|
| `python -m pytest tests -v` | 15 unit, integration & PTY terminal security tests | All 15 passed |
| `python main.py chat` *(or `chat.bat`)* | Interactive CLI REPL with slash popup & Rich ANSI | Real-time terminal session |
| `run bench` *(or `python main.py bench`)* | 12 Chaos Fault Injection Suites + ARS Reliability Scoring | Rich terminal table + SQLite record |
| `run bench models` | Head-to-head comparison of gpt-4o-mini, haiku, and deepseek | Multi-model benchmark matrix |
| `run audit` | Validates budget ceiling, gateway health, and security rules | System audit card |
| `run check "Spotify Premium costs $9.99"` | StaleGuard knowledge drift analysis on Spotify pricing | Freshness report + word-level diff |
| `run brief "Anthropic"` | 30-day executive briefing dossier on Anthropic | Structured JSON + terminal report |

---

## 🛡️ Guardrails

- **Default-Deny Workspace Boundaries:** Coding agent mutations are restricted to the active workspace. Directory traversal (`../`) and writes outside target paths are aborted.
- **Hard Expenditure Ceiling:** Bifrost virtual keys enforce an immutable **\$0.05 limit** per task. Any runaway loop is killed immediately.
- **Offline Simulation Default:** If local Bifrost or Tavily proxies are unreachable, the system automatically engages deterministic mock fixtures, allowing 100% offline reproducibility without paid credentials.
- **Zero Local Secrets Leakage:** Telemetry records and cryptographic turn receipts omit raw API tokens, keys, and private system environment variables.

---

## 📁 Repository Map

```text
illuminati/
├── main.py                  # Unified launcher: CLI REPL + Web Server entrypoint
├── requirements.txt         # Consolidated Python dependencies
├── render.yaml              # Render cloud infrastructure blueprint
├── .env.example             # Security-hardened configuration template
├── chat.bat                 # 1-click interactive CLI REPL launcher
├── code.bat                 # 1-click token-governed coding agent shortcut
├── run.bat                  # Cross-platform master task runner
├── generate_logo.py         # Dot-matrix LED Eye of Providence generator script
├── illuminati.svg           # High-resolution transparent SVG logo (#33C09E mint dots)
├── backend/
│   ├── main.py              # Unified FastAPI server mounting all 4 engine routers + PTY WS
│   ├── terminal_bridge.py   # WebSocket PTY session manager, rate limiter & secret scrubber
│   ├── config.py            # Global configuration, budget thresholds & gateway endpoints
│   ├── database.py          # SQLite connection pool with WAL mode & busy timeout
│   ├── gateway/
│   │   ├── bifrost.py       # Bifrost model plane client, virtual keys & provider failover
│   │   └── tavily_client.py # Tavily knowledge plane client, domain filters & mock fixtures
│   └── modules/
│       ├── coding_agent/    # [Engine 1 · Bifrost PS 01] Token-Governed Coding Agent
│       │   ├── runner.py    # 3-phase cascade, AST parser, token budget gate & receipts
│       │   ├── router.py    # REST endpoints: /api/coding-agent/*
│       │   └── cli_ui.py    # Interactive terminal REPL, slash completer & banner art
│       ├── arena/           # [Engine 2 · Bifrost PS 02] AgentBench Chaos Arena
│       │   ├── lab_engine.py   # 12 chaos failure injection modes & fault generators
│       │   ├── metrics_engine.py # Mathematical ARS scoring formula (0–100)
│       │   ├── orchestrator.py # Multi-agent duel loop & what-if counterfactual replay
│       │   ├── arena_db.py     # SQLite persistence for benchmark runs and traces
│       │   ├── agents/         # ReAct, ReAct Retry, LangGraph, Custom JSON AST, Webhook
│       │   ├── tools/          # Sandbox executor, mock tools & Tavily adapter
│       │   └── routes/         # REST endpoints: /api/benchmarks/*, /api/lab/*
│       ├── staleguard/      # [Engine 3 · Tavily PS 05] Stale-Answer Drift Detector
│       │   ├── pipeline.py  # Claim extractor, volatility checker & word-level diff patcher
│       │   ├── scoring.py   # 0–100 Freshness score & domain decay factors
│       │   ├── search.py    # Real-time Tavily search with date & domain filtering
│       │   ├── spans.py     # Character offset locator & token boundary snapping
│       │   └── fixtures/    # Realistic test fixtures (Spotify, Anthropic, Apple, Nvidia)
│       └── briefing/        # [Engine 4 · Tavily PS 06] Pre-Meeting Briefing Agent
│           ├── research.py  # 30-day temporal research & leadership timeline
│           ├── verify.py    # Deterministic verbatim quote verification
│           ├── draft.py     # Executive brief compiler & source attribution
│           └── router.py    # REST endpoints: /api/briefing/*
├── frontend/
│   ├── index.html           # Unified Dark Glassmorphic Dashboard (Tailwind + Lucide)
│   ├── terminal.html        # Public Web-Based CLI Terminal canvas (xterm.js + PTY bridge)
│   ├── docs.html            # Comprehensive interactive OpenAPI documentation portal
│   └── illuminati.svg       # Brand asset for web navigation bar
├── tests/
│   ├── test_terminal.py     # PTY lifecycle, WebSocket relay, capacity cap & secret scrub tests
│   └── test_api_endpoints.py# REST API & engine regression verification tests
└── docs/
    └── assets/
        ├── banner.png       # High-resolution README hero banner
        ├── banner.svg       # Scalable vector banner
        └── screens/         # High-resolution CLI and GUI screenshots
            ├── cli-hero.png       # Interactive Rich REPL with Eye of Providence
            ├── cli-bench.png      # Terminal benchmark suites & ARS score output
            ├── gui-terminal.png   # Live Browser-Based CLI Terminal (/terminal)
            ├── gui-overview.png   # Unified Dashboard Overview
            ├── gui-arena-benchmarks.png # Arena comparison matrix
            ├── gui-resilience-suites.png# 12 Chaos fault suites monitor
            ├── gui-staleguard.png # Freshness detector & word diff
            ├── gui-briefing.png   # Pre-meeting briefing dossier
            └── gui-docs.png       # Interactive documentation portal
```

---

## 👤 Author & Developer

<table>
  <tr>
    <td width="96" align="center" valign="top">
      <img src="https://github.com/Aryanxp1.png" width="84" alt="Aryan Vishwakarma" style="border-radius:50%">
    </td>
    <td valign="top">
      <b>Aryan Vishwakarma</b> (<a href="https://github.com/Aryanxp1">@Aryanxp1</a>)<br>
      <i>Sole Creator, Architect &amp; Developer</i><br><br>
      Designed, built, and implemented the entire unified <b>Illuminati</b> platform for the Geek Room AI Global Hackathon:
      <ul>
        <li><b>Engine 1 (Token-Governed Coding Agent):</b> 3-phase cascade, self-healing AST repair, \$0.05 budget gate, and SHA-256 receipts.</li>
        <li><b>Engine 2 (AgentBench Chaos Arena):</b> 12 adversarial failure injection modes, mathematical ARS reliability scoring (94.6 / 100), and counterfactual replay.</li>
        <li><b>Engine 3 (StaleGuard Drift Engine):</b> Time-sensitive claim extraction, volatility scoring, real-time Tavily search, and word-level diff patcher.</li>
        <li><b>Engine 4 (Pre-Meeting Briefing Agent):</b> 30-day temporal research window, deterministic verbatim quote verification, and leadership transition tracking.</li>
        <li><b>Unified CLI &amp; Web Platform:</b> Interactive Rich terminal REPL with centered dot-matrix LED Eye of Providence, slash auto-completer, and modern dark glassmorphic web dashboard.</li>
      </ul>
      <b>Live Demo:</b> <a href="https://illuminati-u2kk.onrender.com/">https://illuminati-u2kk.onrender.com/</a> &nbsp;•&nbsp; <b>GitHub:</b> <a href="https://github.com/Aryanxp1/illuminati">https://github.com/Aryanxp1/illuminati</a> &nbsp;•&nbsp; <b>Email:</b> <a href="mailto:vishwakarmaaryan606@gmail.com">vishwakarmaaryan606@gmail.com</a>
    </td>
  </tr>
</table>

---

## 🙏 Credits & Hackathon Partners

- **Title Partner:** [Bifrost by Maxim AI](https://getbifrost.ai/) — Unified AI Gateway, Virtual Keys & Multi-Model Governance.
- **Track Partner:** [Tavily by Nebius](https://tavily.com/) — Search & Real-Time Knowledge Plane for AI Agents.
- **Event:** Geek Room AI Global Hackathon (November 2026).

<p align="center">
  <sub>Built with precision for the Geek Room AI Global Hackathon 2026 · <b>Governed tokens first. Proof every time.</b></sub>
</p>
