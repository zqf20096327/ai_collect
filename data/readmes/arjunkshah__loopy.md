# Loopy — a local-first agent operating system

> **Loopy is a free, open-source, local-first AI coding tool** — an *agent operating system* for software teams. Put work in a workflow and a governed fleet of **agentic AI coding agents** watches it, does the work under policy, and produces reviewable evidence — looping until it ships. Runs on **your machine with your keys**, across **43 coding-agent CLIs** (Codex, Claude Code, Cursor, Gemini, Copilot, and more).

> Not to be confused with LOOPY (the systems-thinking sketch tool) or Loopy Pro (the audio looper). Loopy = the AI agent operating system at **[loopy.yachts](https://loopy.yachts)**.

**Keywords:** agent operating system · agentic coding tool · local-first AI coding tool · free AI coding agent · open-source coding agent · AI agent orchestration · autonomous coding agents

## TL;DR

Loopy is a local agent company on your laptop. You give it a product idea — it researches the market, plans the build, writes code with your coding agent, runs tests, syncs GitHub and Linear, and emails you progress updates. It keeps looping until the product is done or you tell it to stop. Everything runs on your machine with your API keys; nothing is uploaded to a hosted sandbox.

It plugs into **43 coding-agent CLIs** — Codex, Claude Code, Cursor, Copilot, Gemini, OpenClaw, Freebuff, and dozens more. Run **multiple projects in parallel**, split each turn across **two agents** (backend + frontend), or queue builds overnight. Default turn budget supports **up to ~9 hours** of unattended runtime.

Loopy stays on track with a **single source of truth**: Linear issues synced every turn, a durable build plan on disk, and Mem0 memory so long sessions don't drift. **Nebius** routes each turn from live tracker state — not vibes. You can **take over anytime** by queuing a steering message mid-run; Loopy injects it into the next agent turn. **Gmail** sends kickoff, per-turn progress, and completion emails so you don't have to watch the dashboard.

Integrations are deep, not decorative: **Tavily** and **Firecrawl** for research, **Mem0** + **SuperCompress** for memory, **Nebius** for planning and routing, **Composio** for GitHub, Linear, Gmail, and Firecrawl ops. When it's done, you get a **Ship Receipt** — repo URL, Linear project, email proof, sponsor ledger — copy-paste ready.

[![Website](https://img.shields.io/badge/website-loopy.yachts-e890b8)](https://loopy.yachts)
[![License: MIT](https://img.shields.io/badge/License-MIT-pink.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![CI](https://github.com/arjunkshah/loopy/actions/workflows/ci.yml/badge.svg)](https://github.com/arjunkshah/loopy/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-83%20passing-green.svg)](tests/)
[![Agents](https://img.shields.io/badge/coding%20CLIs-43-blueviolet.svg)](loopy/agents/registry.py)

**Live site:** [loopy.yachts](https://loopy.yachts) · **Source:** [github.com/arjunkshah/loopy](https://github.com/arjunkshah/loopy)

---

## Quick start

```bash
curl -fsSL loopy.yachts/install | bash
loopy serve
```

The installer adds a `loopy` command (via `pipx`, or an isolated env it manages for you) — **no repo clone, no source on disk.** The UI ships inside the package. If you already have `pipx`, `pipx install git+https://github.com/arjunkshah/loopy.git` does the same thing.

Already installed? Update in place — no reinstall:

```bash
loopy update
```

Developing on Loopy? Get the source instead:

```bash
git clone https://github.com/arjunkshah/loopy.git && cd loopy
./bootstrap.sh && source .venv/bin/activate && loopy serve
```

Open [http://127.0.0.1:8787](http://127.0.0.1:8787) → onboard → describe your idea → **Send**.

```bash
loopy run --idea "CLI that syncs Linear to markdown" --agent codex   # headless + live progress
loopy run --idea "Add OAuth login" --workdir ~/code/my-app           # build in place on an existing repo
loopy run --verbose                                                 # stream agent output
loopy run --demo                                                    # pipeline without live keys
loopy doctor                                                        # verify keys, Composio, agents
```

---

## Run on an existing repo

Loopy isn't greenfield-only — point it at **any directory** and it builds *in place* instead of scaffolding from scratch:

```bash
loopy run --workdir ~/code/my-app --idea "Add OAuth login and a settings page"
loopy run -C .         --idea "Fix the failing auth tests"   # -C is shorthand for --workdir
```

In the **dashboard**, click **Choose folder** under the prompt and pick the repo (leave it on **Default** for a fresh build under `~/.loopy`).

When the target directory already contains code, Loopy:

- **Detects the existing codebase** and tells the agent to read it and modify in place — no new scaffold, no overwriting unrelated files.
- **Skips template scaffolding** so your files are never clobbered (templates only seed empty workdirs).
- **Never deletes your repo** — Loopy's project cleanup only removes folders it manages under `~/.loopy/projects`.

Phrase the idea as a change request ("Add…", "Fix…", "Refactor…"). Loopy creates a safe `loopy/<slug>` branch, reuses your GitHub remote, and plans **surgical edits** instead of a greenfield MVP. Commit or branch first so each turn's push/PR has a clean baseline.

---

## Launch marketing (Resend + Ayrshare)

When a build completes, Loopy can auto-run a **launch campaign**:

| Channel | Provider | What it does |
|---------|----------|--------------|
| **Email** | [Resend](https://resend.com) | Launch email to your list or segment |
| **Social + video** | [Ayrshare](https://ayrshare.com) | One API call → X, LinkedIn, Instagram, TikTok, YouTube, Threads, Reddit, … |

In **Settings → Launch marketing**:

1. Enable **Marketing on ship**
2. **Resend** — API key + From address + recipients (or segment ID)
3. **Ayrshare** — API key + platforms (`twitter,linkedin,instagram` or `all`)
4. Optional **Media URL** — HTTPS video/image for Reels/TikTok/YouTube posts

Connect your social accounts once in the [Ayrshare dashboard](https://app.ayrshare.com). Gmail (Composio) still handles *your* build notifications; this handles *audience* launch.

---

## The loop

```text
 Idea ──► Tavily research ──► Firecrawl scrape
              │
              ▼
       Memory recall + SuperCompress
              │
              ▼
    Nebius plan · brand · route (reads Linear each turn)
              │
              ▼
   Coding agent(s) — 43 CLIs, optional parallel split
              │
              ▼
      pytest QA · browser review
              │
              ▼
  Composio: Linear kanban · GitHub · Gmail · Firecrawl
              │
              ▼
         Ship Receipt + proof ledger
```

---

## Integrations

Every partner is wired into the orchestrator — not a logo slide.

| Partner | Role in Loopy |
|---------|----------------|
| **Tavily** | Market research and ideation at kickoff |
| **Firecrawl** | Deep spec extraction from competitor URLs (via Composio) |
| **Memory stack** | Pluggable persistent memory — **Mem0** or **Supermemory** (auto-detected) |
| **SuperCompress** | Learned KV eviction — shows token savings % in the dashboard |
| **Nebius Token Factory** | Build plan, brand, and per-turn routing (Llama 3.3 70B) |
| **Composio** | OAuth for GitHub, Linear, Gmail, and Firecrawl |
| **43 coding CLIs** | Local terminal agents — auth stays on your machine |
| **Stripe / Qdrant / MotherDuck** | Optional SDK scaffolds in the template layer |

---

## Choose your memory stack

Already running a memory layer? Keep it. Loopy's persistent memory is **pluggable** — set it once at install and it carries forward to every run:

| Provider | What it is | How Loopy detects it |
|----------|------------|----------------------|
| **mem0** | Hosted semantic memory | `mem0_api_key` set |
| **supermemory** | Hosted memory API (`api.supermemory.ai`) | `supermemory_api_key` set |
| **off** | No persistent memory (SuperCompress still runs) | — |

```jsonc
// ~/.loopy/config.json
{
  "memory_provider": "auto",        // auto | mem0 | supermemory | off
  "mem0_api_key": "...",            // for mem0
  "supermemory_api_key": "..."      // for supermemory
}
```

- **Offered at first-install onboarding** with live detection — the wizard probes your machine (`GET /api/memory/status`) and tells you which stacks it found, defaulting to `auto`.
- **`auto`** (default) probes your machine and picks the first stack it finds (mem0 → supermemory), so existing users keep their own memory with zero config.
- Pin a specific provider to override auto-detection; `off` disables persistent recall entirely.
- The `MemoryBridge` interface is pluggable, so additional backends can be added without touching the orchestrator.
- Every backend **fails closed**: a memory outage never breaks a build turn.

```bash
loopy doctor   # shows your memory setting, the resolved provider, and which stacks are detected
```

---

## Run autonomously for hours

Loopy is built for **unattended, overnight builds**:

- **200-turn default budget** (configurable per project, max 200) — Nebius receives this from turn one and sizes the plan accordingly
- **~9 hours typical** at average turn pace (research/setup once, then agent + QA + ops per turn)
- **Overnight queue** — `loopy queue-add <project>` + `loopy queue-run` or `loopy schedule --enable`
- **Concurrent portfolio** — run up to 10 projects at once; extras wait in queue
- **Agent failover** — auto-switches coding CLIs when usage limits hit (Codex ↔ Claude ↔ …)

Kick back. Loopy keeps looping until done or budget exhausted.

---

## Auto-branch safety

Point Loopy at one of **your existing repos** and it won't touch your `main`. Before
the first build turn, Loopy detects an existing git repo with commits and checks out a
dedicated working branch — `loopy/<slug>` (derived from the product/repo slug or idea) —
so every commit lands on the safety branch and your current branch stays clean. Review
the loop's work, then merge (or open a PR) on your terms.

- **Best-effort and safe** — if git is missing, the path isn't a repo, or it has no
  commits, Loopy skips the step silently and never crashes a run.
- **Idempotent** — re-running on an existing `loopy/` branch keeps you there; an existing
  branch is checked out rather than recreated.
- **Opt-out** — set `auto_branch: false` in `~/.loopy/config.json` (or via the
  `/api/secrets` endpoint) to build on whatever branch is currently checked out.

The chosen branch is emitted on the live timeline (`working_branch` event) and included
in the Ship Receipt.

---

## Single source of truth

Agents drift when context is scattered. Loopy keeps one durable thread:

| Layer | What it tracks |
|-------|----------------|
| **Linear issues** | Plan issues created at kickoff; statuses synced after every turn — Todo / In Progress / Done |
| **Nebius routing** | Reads live Linear state + QA results + build plan to decide the next follow-up (or stop) |
| **Workdir artifacts** | `RESEARCH.md`, `BUILD_PLAN.md`, `PRODUCT.md`, turn lessons — written to disk each phase |
| **Memory stack** | Recalls product decisions and prior turns before SuperCompress trims context (mem0 / supermemory) |
| **GitHub** | Source of truth for code — pushed or PR'd after every turn |

Nebius never reruns full research unless explicitly refreshed. Each turn gets compressed context + fresh Linear snapshot — so the agent stays aligned with what actually shipped.

---

## Manual takeover

You don't have to babysit — but you can steer anytime:

1. Start a loop from the dashboard or CLI
2. While the run is **active**, open **Manual takeover** in the live build view
3. Queue a message (e.g. “Drop Stripe, focus on CLI only” or “Fix the auth bug first”)
4. Loopy injects it into the **next agent turn** as highest-priority steering

Messages are stored in the local SQLite ledger and appear in the SSE timeline. Take over when you care; let it run when you don't.

---

## Gmail updates

Connect Gmail via Composio and set **Gmail notify to** in settings. Loopy emails you:

| When | Subject pattern | Contents |
|------|-----------------|----------|
| **Kickoff** | `[Loopy] Started — {product}` | Idea, plan excerpt, Linear + GitHub links |
| **Each turn** | `[Loopy] Turn N — {product}` | Agent summary, QA results, kanban snapshot, repo link |
| **Completion** | `[Loopy] Complete — {product}` | Final status, Ship Receipt summary, links |

Nebius drafts the email body — not a static template. Every message reflects what actually happened that turn.

---

## Parallel agents

Need speed? Enable **Parallel agents** in settings:

- **Primary agent** — backend, APIs, data layer, CLI, server tests
- **Secondary agent** — frontend, UI, components, client code
- Both run the same turn concurrently via thread pool; outputs merge into one result

Pick any two registered CLIs (e.g. Codex + Claude). Loopy disables parallel mode automatically if the secondary agent hits usage limits.

---

## 43 coding-agent CLIs

Loopy orchestrates terminal-native coding agents — not a hosted runtime. Bring whatever CLI you already use:

**Popular:** `codex` · `claude` · `cursor` · `copilot` · `gemini` · `openclaw` · `opencode` · `kimi` · `freebuff` · `qwen`

**Full registry (43):** `aider`, `amazon_q`, `amp`, `antigravity`, `backboard`, `claude`, `cline`, `codebuff`, `codex`, `command_code`, `continue`, `copilot`, `coro`, `crab`, `crush`, `cto`, `cursor`, `devon`, `droid`, `everycode`, `factory`, `forge`, `freebuff`, `gemini`, `goose`, `gptme`, `kilo`, `kimi`, `letta`, `logicoal`, `neovate`, `openclaw`, `opencode`, `openhands`, `openharness`, `pi`, `plandex`, `qwen`, `roo`, `swe_agent`, `trae`, `vibe`, `warp`

```bash
loopy doctor          # see which agents are on your PATH
loopy run --agent claude --idea "…"
```

Agent auth (Codex, Claude Code, etc.) stays local — Loopy never stores those credentials.

---

## Dashboard

| Capability | Details |
|------------|---------|
| **Compose** | Describe your product; optional per-project turn budget |
| **Live build** | SSE timeline, agent log, tests, diff, browser shots |
| **Manual takeover** | Queue steering messages during an active run |
| **Ship Receipt** | Copy-paste proof: GitHub, Linear, Gmail, sponsor ledger |
| **Projects** | Sidebar history, concurrent builds, per-project limits |
| **Settings** | Keys, agents, parallel mode, concurrent slots, Gmail notify |

---

## CLI

| Command | Purpose |
|---------|---------|
| `loopy serve` | Local UI at `:8787` |
| `loopy run --idea "…" --agent codex` | Headless full loop with live phase output |
| `loopy run --verbose` | Stream agent CLI lines during the build |
| `loopy run --demo` | Full pipeline without live API keys |
| `loopy doctor` | Verify keys, Composio connections, 43 agents on PATH |
| `loopy projects` | List local projects |
| `loopy portfolio` | Portfolio health summary |
| `loopy queue-add <id>` | Queue project for batch / overnight run |
| `loopy queue-run` | Run next queued project |
| `loopy schedule --enable` | Enable periodic scheduler (default every 24h) |
| `loopy pitch` | Advanced: Stripe SDK preset via CLI (12 turns) |

---

## Onboarding

1. Add **Tavily**, **Nebius**, and **Composio** API keys + a stable Composio user ID.
2. In [Composio dashboard](https://dashboard.composio.dev), create Auth Configs for GitHub, Linear, Gmail, Firecrawl.
3. Paste each `ac_…` ID into Loopy → **Connect** each toolkit.
4. Set **Gmail notify to** (your email) for kickoff / turn / completion messages.
5. Pick your coding agent — authenticate locally (Codex, Claude Code, etc.).
6. **Send**.

Copy `.env.example` for reference — all secrets end up in `~/.loopy/config.json`.

---

## Repository layout

```text
loopy/
├── loopy/
│   ├── orchestrator.py       # Main build loop
│   ├── server.py             # FastAPI — dashboard, SSE, REST API
│   ├── cli.py                # Typer CLI
│   ├── cli_progress.py       # Live progress for headless runs
│   ├── manual_takeover.py    # Mid-run steering messages
│   ├── agents/               # 43-agent registry + execution
│   ├── integrations/         # Composio, Linear, GitHub, Gmail
│   ├── memory/               # Mem0 + SuperCompress bridge
│   ├── research/             # Tavily + Firecrawl
│   ├── review/               # pytest + Playwright QA
│   ├── work/                 # Work graph: missions, tickets, agents, triggers, evals, playbook
│   ├── preflight.py          # Pre-build gate (integrations + clarifying questions)
│   ├── inbound.py            # Email/Linear replies → steering (human-in-the-loop)
│   ├── templates/            # Project scaffolds
│   ├── app/                  # Dashboard + onboarding UI (bundled in the wheel)
│   └── ship_receipt.py       # Proof-of-ship payload
├── web/                      # Marketing site (loopy.yachts) — deployed to Vercel
├── tests/                    # pytest suite · CI on every push
├── install.sh                # One-line installer (pipx / isolated env, no clone)
└── bootstrap.sh              # Dev environment setup (from a source checkout)
```

---

## Development

```bash
git clone https://github.com/arjunkshah/loopy.git && cd loopy
./bootstrap.sh && source .venv/bin/activate
python -m pytest tests/ -q          # 83 tests
loopy serve --port 8787
loopy run --idea "…" --agent codex  # headless with live progress
```

Requirements: Python 3.10+, a coding agent CLI on PATH for live builds. Playwright optional (HTTP fallback for browser QA).

Contributing? See [CONTRIBUTING.md](CONTRIBUTING.md), the house rules in [AGENTS.md](AGENTS.md), and [SECURITY.md](SECURITY.md) for reporting vulnerabilities.

Note: I DO NOT CONSENT to Ayush Rout (github.com/ayushrout12) to use this Github repo IN ANY WAY, SHAPE, OR FORM for inspiration or direct reference. I DO NOT CONSENT to him forking, or cloning this repo and using it to build his own project. I DO NOT CONSENT to him building a parallel/similar project that uses my code in ANY WAY, SHAPE, OR FORM.

---

## License

MIT — see [LICENSE](LICENSE).
