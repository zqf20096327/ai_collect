<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="branding/pygg-logo-dark.svg">
  <img src="branding/pygg-logo.svg" alt="Pygg — One Flow. Many Agents." width="380">
</picture>
</p>

<h3 align="center">Keep your coding agent moving when your plan hits its limit.</h3>

<p align="center">Pygg is a local gateway for Claude Code, Codex, OpenCode and any OpenAI- or Anthropic-format tool.<br>When one provider says no, the next model you connected answers, with the whole conversation.<br>Hand a well-defined change to a cheaper agent, and Pygg checks it before you review it.</p>

<p align="center">
<a href="https://github.com/nambean/Pygg/actions/workflows/ci.yml"><img src="https://github.com/nambean/Pygg/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
<a href="https://www.npmjs.com/package/@pygg/cli"><img src="https://img.shields.io/npm/v/@pygg/cli/dev?label=npm%20%40pygg%2Fcli" alt="npm: @pygg/cli (dev)"></a>
<img src="https://img.shields.io/badge/licence-MIT-green" alt="Licence: MIT">
<img src="https://img.shields.io/badge/app-Windows%20x64-blue" alt="Desktop app: Windows x64">
<img src="https://img.shields.io/badge/CLI-Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-blue" alt="CLI: Windows, macOS and Linux">
<a href="https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.9"><img src="https://img.shields.io/github/v/release/nambean/Pygg?include_prereleases&label=release" alt="Release: v0.1.0-dev.9"></a>
<img src="https://img.shields.io/badge/status-developer%20preview-orange" alt="Status: developer preview">
</p>

https://github.com/user-attachments/assets/85708783-8be3-4292-955c-783cc066bbd1

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/usage-dark.svg">
  <img src="docs/images/usage-light.svg" alt="A terminal installs the pygg command line from npm, checks that Pygg's gateway answers on 127.0.0.1:8741, sets up Claude Code and starts it through Pygg with the model auto; the gateway routes each request to free and cheap models, your plans, local models or opt-in web sessions" width="100%">
</picture>
</p>

**Every day, the gateway.** Pygg runs on your computer. Connect the providers you already have (API keys, coding plans, a local Ollama), point your coding tool at `127.0.0.1:8741` and choose the model **`auto`**. Each request goes to an eligible model you connected, within the limits you set. When a provider answers with a rate limit, an exhausted quota, no credit or an overload, the next eligible model in the route takes the request before your agent sees an error, and the session stays on it while that model can serve. Every attempt lands in a ledger with what it cost and where that figure came from.

**When you delegate, Smart Tasks (experimental).** Hand a subtask from your agent to Pygg (over MCP) or type a goal into the app. Cheaper agents try it in a Git worktree, cheapest first, and the next step starts when one fails: its checks fail, it changes nothing, or it stops. A result no check ran on is marked **not ready** instead of looking done. Paid steps wait for your approval, and the cap you approve holds at the gateway.

> [!NOTE]
> **Developer preview (2026-11-23).** The gateway and the Windows desktop app are built and verified live, from first launch to "my coding tool uses `auto`". The Windows installer is the [prerelease `v0.1.0-dev.9`](https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.9), **not code-signed**, so Windows SmartScreen warns before it runs. The `pygg` command line is [on npm](https://www.npmjs.com/package/@pygg/cli) for Windows, macOS and Linux. Spending limits rest on prices and token estimates, a clean Windows machine and long-running use have not been tried yet, and no outside user has run it, so Pygg is **not yet for unattended or financially critical use**. What is built and how each part was verified: [Implementation Status](docs/IMPLEMENTATION-STATUS.md).

## Why Pygg

### The gateway

- **Your agent keeps going.** A 429, an exhausted quota, a 402, an account's spend limit or Anthropic's 529 overload moves the request to the next eligible model in its route, before the agent gets its first byte, with every earlier message, tool call and tool result. A route needs a second model for that: `auto`, a combo or a pool. In 20 staged limit events on Chat Completions, Messages and Responses sessions, 20 resumed ([report](benchmark/reports/2026-11-23-continuity.md)). The status line shows the model a session is on now.
- **No request billed twice.** A timeout, a dropped connection or a 5xx other than an overload stops instead of trying elsewhere, since the provider may already have run it. Each attempt is written to disk **before** it is sent.
- **`auto` that you can read.** Rules over the models you connected, not a classifier: an eligible model at or above your key's minimum tier, at most five in a route and two from one connection. Every response says why it chose what it chose, and **How auto chooses** simulates a route before you send anything. When nothing qualifies, Pygg says why and what to change.
- **Cost you can trace.** Each attempt is recorded with its cost and that cost's source: **actual** (the provider said), **estimated** (a price you or a catalog set) or **unknown**, never shown as $0. Each part of an estimate is rounded up to the micro-dollar; a provider's own bill can still differ (7.5% above the ledger at one provider, [report](benchmark/reports/2026-11-23-smart-task-proofs.md)).
- **Limits that hold.** Per Pygg API key: a monthly limit, and per session or UTC day a limit that refuses the next request with 402 once reached. A request already running is never cut. A strict limit holds what each request could cost at most, at list price and its output limit, so concurrent requests cannot pass it together.
- **The provider's cache keeps working.** A session stays on the model and key that answered it while they can serve. Anthropic requests from Claude Code pass through unchanged; for OpenAI-format agents such as Codex, Pygg turns on Anthropic's prompt cache (30% less in all, 68% less on input, [report](benchmark/reports/2026-11-14-codex-claude-prompt-cache.md)).
- **A receipt for every launch.** When a tool started by `pygg run` exits, Pygg prints what that launch cost, how much came from the cache, which models answered and what changed in the repository. `pygg launches --by-repo` sums it per repository and week.
- **Several accounts, used in turn.** A key ring holds API keys of separate accounts on one connection; each key cools down on its own.
- **Local, with your own accounts.** The gateway listens on 127.0.0.1 only and needs a Pygg API key; provider keys stay in the OS credential store. Each tool's set-up is backed up first, and Remove puts it back. Pygg does not carry your Claude or ChatGPT plan's sign-in into other tools; the opt-in web sessions, which use a site's own page as you, are the one place your sign-in is used, with an account-risk warning.

### Smart Tasks (experimental)

- **Checked delegation.** Your agent hands a subtask to Pygg with `pygg_run_task` (MCP, or the Claude Code plugin). Agents run it in a Git worktree; your checkout is not touched until you keep the result as a branch.
- **Cheap first.** Each step is an agent and model, fixed when the task starts; the next one starts when a step fails its checks, changes nothing or stops. On six hard cases with half their tests hidden from the agent, cheap first passed 16 of 16 recorded runs (2 were lost to a launch error) at about a sixth of the strong model's list cost per solved run ([report](benchmark/reports/2026-11-23-smart-task-proofs.md)).
- **Not ready means not ready.** No check ran, a check failed, or the result changed the file that defines a check: a plain keep is refused, and **Keep Without Checks…** asks you first. Each check shows its exact command, exit and time ([report](benchmark/reports/2026-11-23-checks-gate.md)).
- **Checks for thin repositories.** Pygg suggests checks your repository already has (package scripts, TypeScript, `node --test`, Python, Go, make, .NET, Maven, Gradle), each saying what it covers; you approve them. **Check This Result** runs an approved check on a waiting result without running the agent again ([report](benchmark/reports/2026-11-23-check-suggestions.md)).
- **Caps that hold.** The cap you approve for a paid step is held at the gateway: each request holds the most it could cost at list price inside what is left, its output limit lowered to fit, and a model without a price is not used. 0 violations in 10 × 1,000 adversarial requests ([report](benchmark/reports/2026-11-23-step-cap.md)). An agent that does not go through Pygg is checked after the step instead, and the approval says so.
- **A narrow planner.** Type a goal into the app, or send it to the model `pygg/brain`: a planner splits it into small cards, each with a check you can edit before you approve the plan. A free or local planner, or one you picked before, runs at once; another paid one waits for your pick ([BRAIN.md](docs/design/BRAIN.md)).

**Also there, opt-in:** AI websites as providers (web sessions: unofficial, with account risk, behind a per-site guard), the Kanban board that runs an approved plan's cards under WIP limits, and role aliases (`auto/code`, `auto/plan`…) ranked by a weekly signed feed of public benchmark facts. They work and are documented, but are not where the project is going next ([ROADMAP](docs/ROADMAP.md)).

## A look at the app

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/home.png">
  <img src="docs/images/home-light.png" alt="Home: the gateway running on 127.0.0.1:8741, estimated savings against a chosen model, where the answers came from, and the last 24 hours of requests" width="760">
</picture>
</p>

| Providers | Usage | CLI Tools |
| :---: | :---: | :---: |
| <img src="docs/images/providers.png" alt="Providers: each connection with its health over 24 hours, its billing and how many models auto may use" width="260"> | <img src="docs/images/usage.png" alt="Usage: estimated savings, known cost by its source, and cost per day" width="260"> | <img src="docs/images/cli-tools.png" alt="CLI Tools: one-click set-up for Claude Code, OpenCode and Codex" width="260"> |

<sub>The browser preview with demo data (`pnpm dev`).</sub>

## How a request flows

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/request-flow-dark.svg">
  <img src="docs/images/request-flow-light.svg" alt="One request through Pygg: agent, gateway, route, policy and budget, journal; the key ring's key 1 answers 429 and key 2 answers 402, both cool down; the route's next target, Ollama, answers 200; the answer streams back and each attempt is settled in the ledger" width="100%">
</picture>
</p>

1. **Gateway.** The agent calls `127.0.0.1:8741` with its own Pygg API key, in OpenAI Chat Completions, OpenAI Responses (Codex) or Anthropic Messages, streamed, with tool calls.
2. **Route.** The model name is `auto` or `auto/cheap`, a role alias, a **combo** (your ordered list, or cheapest first per request), `<connection>/<model>`, or `pygg/brain`, which answers with a plan instead of running the request.
3. **Policy and budget.** The key's allowed connections, health and cooldowns; a key with a limit holds the attempt's estimated cost first, and a strict limit or a task step's cap holds what it could cost at most, so concurrent requests cannot pass it together.
4. **Journal.** The attempt is written to disk before it is sent, and settled with its ledger entry in one transaction.
5. **Send and fall back.** Same format passes through untouched; other pairs are translated and say what they dropped. A limit cools that key or model down for as long as the provider says, a rejected key waits until you replace it, and the next key or target is tried.

The diagrams are generated by [`scripts/readme-diagrams.mjs`](scripts/readme-diagrams.mjs) and checked against `apps/desktop/src-tauri/src/gateway/`. More in [Architecture](docs/ARCHITECTURE.md).

## Install

**Desktop app (Windows 10/11 x64).** It runs the gateway, holds your connections and shows usage. Download `Pygg_0.1.0_x64-setup.exe` (or the MSI) and `SHA256SUMS.txt` from the [`v0.1.0-dev.9` prerelease](https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.9), then check the download before running it:

```powershell
Get-FileHash .\Pygg_0.1.0_x64-setup.exe -Algorithm SHA256   # compare with the line in SHA256SUMS.txt
```

The installer is **not code-signed**, so SmartScreen says "Windows protected your PC": choose **More info → Run anyway**. It installs for the current user, with `pygg-cli.exe` next to the app. To build it yourself instead, see [Development](#development).

**Command line (`pygg`), from [npm (`@pygg/cli`)](https://www.npmjs.com/package/@pygg/cli):**

```bash
npm install -g @pygg/cli@dev
```

Published under the tag `dev` for **Windows x64**, **macOS** (Apple silicon and Intel) and **Linux x64** (glibc). On Windows the CLI uses the desktop app's store and gateway; on macOS and Linux, where there is no app yet, `pygg gateway serve` runs the gateway in a terminal of its own.

## Quick start

Open Pygg, then **Providers → Connect Provider** and paste a key (Gemini, OpenRouter and Groq have free tiers; Ollama is local). Without the app, `pygg gateway add-connection --preset gemini --key-env GEMINI_API_KEY` reads the key from an environment variable and tries to list the connection's models. Then point your tool at Pygg:

**Claude Code** keeps your Claude sign-in; Pygg starts it through the gateway one launch at a time.

```bash
pygg setup claude          # a Pygg key of its own, kept in the credential store; no file changes
pygg run claude            # this launch through Pygg, model auto; a receipt when it exits
pygg run --statusline claude   # the same, with cost and the model answering in Claude Code's status line
```

**Codex CLI** gets a `pygg` provider and profile, after a backup; its default model is not changed.

```bash
pygg setup codex
pygg run codex             # or: codex --profile pygg -m auto/cheap
```

**OpenCode** gets a Pygg provider listing the auto aliases and your enabled models, kept current.

```bash
pygg setup opencode
pygg run opencode          # then /models → Pygg → auto
```

**Editors and SDKs** (Cline, Continue, Roo Code, the OpenAI or Anthropic SDKs): base URL `http://127.0.0.1:8741/v1`, a key from **Endpoint → API Keys**, model `auto`.

**Only local models?** They are tier T0, under a new key's minimum T2, so `auto` has nothing to choose until you allow it: Home → **Let Auto Use Lower Tiers…**, or `pygg gateway client --name NAME --auto-min-tier T0`. Ollama serves 4,096 tokens of context unless a model sets `num_ctx`, too little for a coding agent: raise `OLLAMA_CONTEXT_LENGTH`, then tell Pygg with `pygg gateway model --model ollama/M --context N` ([Providers](docs/PROVIDERS.md)).

**Smart Tasks from Claude Code** (experimental): Pygg's MCP server and two skills, as a plugin. It asks for a key with **May start tasks** on, and needs the app (or `pygg gateway serve --tasks yes`) running. Approve your repository's checks in the app first.

```text
/plugin install pygg --marketplace nambean/Pygg
```

On Claude Code before 2.1.275: `/plugin marketplace add nambean/Pygg`, then `/plugin install pygg@pygg`.

**Keep spending in bounds** and see where it went:

```bash
pygg gateway client --name "Claude Code (launcher)" --session-usd 5 --day-usd 20   # or Endpoint → API Keys → Limits…
pygg launches --by-repo    # cost, commits and cost per commit, per repository and week
pygg usage --days 7        # requests, known and unknown cost, by client, model and kind of request
```

Each `setup` takes `--dry-run` to show what would change and `--remove` to undo it. The same set-up is one click in **CLI Tools**. Step by step, with troubleshooting: [Getting started](docs/GETTING-STARTED.md).

## Measured, not claimed

Every run below is the maintainer's own, with its method, raw results and what it does not show in the linked report: read it before quoting a number. Everything else, including model rankings, sponsored runs and web sessions: [BENCHMARKS.md](docs/BENCHMARKS.md).

**What Pygg promises, tested** (2026-11-23; the gateway over HTTP with a fake provider, or the task engine with fake agents, unless said):

| What was measured | Result | Report |
| --- | --- | --- |
| A session's quota runs out mid-conversation: 20 staged limits on Chat Completions, Messages and Responses, with tool calls | **20 / 20** resumed on the fallback with the whole conversation; 18 / 20 before Anthropic's 529 fell back | [Continuity](benchmark/reports/2026-11-23-continuity.md) |
| A paid step's cap under 10 × 1,000 adversarial requests: oversized output limits, two keys at once, cancelled streams, restarts | **0 violations**; found and fixed a 1–2 micro-dollar overshoot from rounding | [Step caps](benchmark/reports/2026-11-23-step-cap.md) |
| 80 delegated results, 50 of them with no check run | **50 / 50** not ready (plain keep refused); 30 / 30 checked ones show every check's command and exit | [Checks gate](benchmark/reports/2026-11-23-checks-gate.md) |
| Check suggestions on 20 small public repositories, read only | A check for **20 / 20** (10 before), each naming what it covers; whether people accept them is not measured yet | [Check suggestions](benchmark/reports/2026-11-23-check-suggestions.md) |
| Cheap first (DeepSeek V4.1 Flash, then Qwen 3.8 Max) against Qwen 3.8 Max alone, 6 hard cases × 3 with half their tests hidden, real agents | **16 / 16** recorded runs (2 lost) against 17 / 18, no hidden-test miss in either; about 1/5.6 the list cost per solved run and 1/4 the time | [Six proofs](benchmark/reports/2026-11-23-smart-task-proofs.md) |
| From `npm install -g @pygg/cli@dev` to a first answer, clean profile, local Ollama, following Pygg's own messages | **17.4 s** on dev.9 (never on dev.8); not yet with a fresh user or the desktop app | [First request](benchmark/reports/2026-11-23-first-request.md) |

**What a cheaper model saved** (real agents and providers):

| What was measured | Result | Report |
| --- | --- | --- |
| OpenCode on 12 small Node tasks × 3, the whole session on Claude Haiku 5.5 instead of Sonnet 5.5 | **88% less per solved task**; 36/36 passed against 34/36 | [N2](benchmark/reports/2026-11-12-n2-savings.md) |
| Claude Code on six tasks from a real production repository (Express + Prisma) | Haiku 6/6 for $1.50, Sonnet 4/5 for $1.19; on the 4 both solved, Haiku **about 40% less**; `auto/cheap` 2/6 | [CCHT](benchmark/reports/2026-11-13-ccht-real-repository.md) |
| OpenCode on 36 cases, one attempt each, 15 routes | 36/36 on four routes, Gemini 4 Hydrogen at **$0.072 per solved task**; local 8B models 3/36 and 0/36 | [Every model](benchmark/reports/2026-11-20-all-models.md) |
| The gateway's own overhead, against a local fake provider | **About 4 ms** per short request; about 230 requests/s with 16 clients | [Overhead](benchmark/reports/2026-11-14-gateway-overhead.md) |

Not claimed: a quality ranking of models, a provider's bill (costs are the ledger at list prices), or savings on large refactors, migrations or other languages, which no run has measured. The 88% is small tasks pinned to a cheaper model; on the real repository it narrowed to about 40%.

### Help measure it on your work

One person's runs are a start, not proof. Two ways to help:

- **The paired study:** 6 tasks from your own backlog, 3 with your usual set-up and 3 through Pygg, compared blind; your code stays on your machine ([how it works](benchmark/study/README.md)). Everyone who finishes is credited under [Sponsors](#sponsors).
- **The harness:** run the [benchmark](benchmark/README.md) on the cases here or on your own repositories and open a pull request with the report ([how](CONTRIBUTING.md#benchmark-runs)). A run where the cheaper model loses is as welcome as one where it wins.

## Compared with other routers

All five sit between your coding tools and the model providers. Pygg and LiteLLM were run against the same fake provider and requests (**M**); the others are read from their own documentation and source (**D**: 9router and OmniRoute on 2026-11-14 and again on 2026-11-20, LiteLLM 1.106.2 and OpenRouter on 2026-11-14). ✅ yes · ⚠️ partly, opt-in, or with a catch · ❌ no · — not documented where we looked, which is not proof it is absent.

| Feature | **Pygg** (this project) | [9router](https://github.com/decolua/9router) | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | [LiteLLM](https://github.com/BerriAI/litellm) proxy | [OpenRouter](https://openrouter.ai) |
| --- | --- | --- | --- | --- | --- |
| Runs on your computer, open source | ✅ desktop app (Windows) and headless gateway; MIT | ✅ Node.js server; MIT | ✅ Node.js or Electron; MIT | ✅ Python or Docker; MIT except `enterprise/` | ❌ hosted service |
| Falls back when a provider is rate-limited, out of credit or rejects the key | ✅ 100% served, **1.04** provider requests each, ~70 ms (M) | ✅ on 401, 402, 403, 429 and 5xx (D) | ⚠️ on rate limits, 5xx and timeouts, not on auth errors (D) | ✅ 100% served, 4 provider requests each, ~4.6 s (M) | ✅ with a `models` list (D) |
| Never re-sends a request the provider may already have run (5xx, dropped connection, timeout) | ✅ by default; one 5xx retry can be allowed (M) | ❌ moves to the next model (D) | ❌ up to 3 attempts (D) | ❌ 3 attempts at the failing provider (M) | — |
| Waits as long as `Retry-After` says | ✅ up to 7 days (M) | ❌ fixed cooldowns (D) | ✅ on 429 (D) | ⚠️ between retries, up to 60 s (M) | ⚠️ passes it to the client (D) |
| A session stays on one key, so the provider's cache keeps working | ✅ by default, 60 / 60 sessions (M) | ⚠️ with its `smart` strategy (D) | ⚠️ with its `cache-optimized` strategy (D) | ⚠️ opt-in; 0 / 60 by default (M) | ✅ by default (D) |
| Prompt cache for OpenAI-format agents (Codex) on Claude | ✅ automatic, **89.5%** of the prompt read from cache (M) | — | — | ⚠️ once configured: 89.5% Chat Completions, 39.7% Responses; 0% by default (M) | ⚠️ the client must send `cache_control` (D) |
| Every attempt in a ledger, with where its cost came from | ✅ fallbacks and failures included; unknown never shown as $0 (M) | ⚠️ cost "for tracking only" (D) | ✅ audit trail and cost headers (D) | ⚠️ spend logs; per-attempt rows not documented (D) | ⚠️ usage per key (D) |
| Spending limits | ✅ per key and month, session or day, and per delegated step; strict limits and step caps hold each request's most possible cost at list price (M) | ⚠️ "per provider" in its FAQ, mechanism not described (D) | ✅ per-key USD quotas (D) | ✅ budgets per key, user and team (D) | ✅ a credit limit per key (D) |
| Changes checked by your repository's own checks before you review them | ✅ Smart Tasks: worktree, cheap first, not ready without a check (M) | — | — | — | — |
| Choosing the model for you | ✅ `auto` (tier floor), `auto/cheap` (expected cost), role aliases, each choice explained (M) | ⚠️ ordered combos you build (D) | ✅ `auto` with 16-factor scoring, `auto/cheap`, `auto/coding` (D) | ⚠️ cost-based routing; a complexity router in beta (D) | ✅ `openrouter/auto` (D) |
| One-command setup of coding tools | ✅ Claude Code, Codex, OpenCode; backed up first, `--remove` restores (M) | ⚠️ OpenClaw from its dashboard; others by hand (D) | ✅ `run` and `configure` for 15 tools (D) | — | — |
| Uses your Claude, Codex or Copilot plan's sign-in from other tools (account risk) | ❌ no OAuth bridging; ⚠️ opt-in web sessions use a site's page as you, with a warning | ✅ OAuth bridges into Claude, Codex, Copilot, Cursor (D, 2026-11-23) | — | ❌ | ❌ |
| Throughput | ⚠️ about 230 requests/s on one PC, 4 ms added per request (M) | — | — | ✅ 1,170 requests/s on 4 instances, its own test (D) | — |

**Where Pygg is worse:** throughput is for one person's tools, not a team's traffic; a provider that hangs gets no timeout fallback; by default a 5xx other than an overload, or a dropped connection, reaches your agent as an error, where LiteLLM served 100% after re-sending; and a limit assumes the provider honours the request's output limit (a thinking model that writes past it can pass the limit by what it overran). Details and sources: [BENCHMARKS.md](docs/BENCHMARKS.md#pygg-next-to-other-gateways), [resilience](benchmark/reports/2026-11-14-resilience.md).

**Is Pygg a fork of 9router?** No. 9router, a local router for the providers you already have, was one of the inspirations for building the gateway first (ADR-016). Pygg is written from scratch in Rust; the one part that follows 9router is the Muse web-session recipe, credited under MIT in [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md).

## What's inside

```text
Coding agents ──HTTP──► Gateway 127.0.0.1:8741 (axum) ──► OpenAI- and Anthropic-compatible APIs, coding plans,
  Claude Code, Codex,     auth · route · policy · journal       local runtimes (Ollama …), web sessions (WebView2
  OpenCode, SDKs          translate · fall back · settle         windows behind the guard)
                                   │
       React UI ◄── Tauri ──► Rust core ──► SQLite store (ledger, journal, connections) · OS credential store
       pygg CLI ──────────────┘   └──► task engine: Git worktrees · agent CLIs · approved checks
```

- **One Rust crate** (Tauri 2): the gateway (axum), the SQLite store, the OS credential store, the task engine, web-session windows, and the headless programs (`pygg-cli`, `gateway`, `pygg-mcp`) built from the same library.
- **Interface:** React 19, Vite and TypeScript, with a layout check over every screen in CI (`pnpm ui-check`).
- **[`@pygg/cli` on npm](https://www.npmjs.com/package/@pygg/cli):** a Node launcher with one optional package per platform (ADR-037). Pygg's MCP server is in the MCP Registry as `io.github.nambean/pygg`.
- **Smart Tasks:** agent CLIs (OpenCode, Codex, Claude Code, Gemini CLI) run in Git worktrees against the repository's approved checks; the cap of a paid step holds at the gateway for steps on Pygg's models ([AGENTS.md](docs/AGENTS.md)). Proofs: the six gap-study items, step caps, the checks gate and check suggestions, on 2026-11-23.
- **Skills & Prompts:** one library of skills in the Agent Skills format, installed into Claude Code's, Codex's and OpenCode's own skills folders (ADR-039).

## Documentation

| | |
| --- | --- |
| **Use** | [Getting started](docs/GETTING-STARTED.md) · [Providers](docs/PROVIDERS.md) · [Agents and Smart Tasks](docs/AGENTS.md) · [Benchmarks](docs/BENCHMARKS.md) · [Security](docs/SECURITY.md) |
| **Understand** | [Architecture](docs/ARCHITECTURE.md) · [Decisions](docs/DECISIONS.md) · [The planner, the facts feed and the board](docs/design/BRAIN.md) · [Schema](docs/SCHEMA.md) · [Screens](docs/design/SCREENS.md) · [Command line](docs/design/CLI.md) |
| **Track** | [Implementation status](docs/IMPLEMENTATION-STATUS.md) · [Roadmap](docs/ROADMAP.md) · [Benchmark reports](benchmark/reports) |
| **Contribute** | [Contributing](CONTRIBUTING.md) · [The paired study](benchmark/study/README.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Every document, indexed](docs/README.md) |

Only the app's data folder (`app.smarttaskrouter.desktop`) and its credential service name keep the engineering name SmartTaskRouter, so existing data stays readable. Brand assets are in [branding](branding/README.md).

## Development

Requirements: Node.js LTS with pnpm 9 (`corepack enable`), stable Rust through rustup, and on Windows the Visual Studio C++ Build Tools and WebView2 (built into Windows 11).

```powershell
pnpm install
pnpm dev                                              # the interface at http://127.0.0.1:1431 with demo data (?empty for a first run, ?local for Ollama only)
pnpm --filter @pygg/desktop tauri:dev     # the desktop app with the real gateway
pnpm typecheck
pnpm --filter @pygg/desktop tauri:build   # the installers, under apps/desktop/src-tauri/target/release/bundle
pnpm ui-check                                         # every screen at several window sizes, nothing overflowing
cd apps/desktop/src-tauri; cargo test --lib --tests   # core, gateway, web-session and task engine tests
node scripts/readme-diagrams.mjs                      # regenerate the README's animated diagrams
```

`PYGG_DATA_DIR` points the app at another store, for trying it without touching your own; that app runs beside the installed one, with its own window profile, and needs a gateway port of its own (Endpoint → Configure…).

## Sponsors

- **[MixAICloud](https://us.mixaicloud.com)** ([TheoZhang3321 on X](https://x.com/TheoZhang3321)), the project's first sponsor: API credit, given on 2026-11-20 for a benchmark of how Pygg routes the work MixAICloud's users send to DeepSeek and Qwen (coding) and to GLM and Kimi (lighter and conversation tasks): [the report](benchmark/reports/2026-11-20-mixaicloud.md).
- **Study participants:** each person who finishes the [paired study](benchmark/study/README.md) is listed here, with a link of their choice.

A sponsor's credit pays for traffic, not for results. A sponsored run is published like any other, with its method, raw results, spend and every route where Pygg's choice lost ([BENCHMARKS.md](docs/BENCHMARKS.md)), and its report names who paid for it.

## Licence

MIT, see [LICENSE](LICENSE). Third-party code and data are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
