<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="branding/pygg-logo-dark.svg">
  <img src="branding/pygg-logo.svg" alt="Pygg — One Flow. Many Agents." width="380">
</picture>
</p>

<h3 align="center">Run your coding agents on cheaper models without losing the answers.</h3>

<p align="center">Pygg is a local gateway that routes each request to a model you connected, and measures what it saved.<br>Our own first runs: <b><a href="#measured-not-claimed">88% less per solved task</a></b> on 12 small coding tasks, about 40% on a real repository.<br>A small sample: <a href="#benchmark-it-on-your-work">help benchmark it on your work</a>.</p>

<p align="center">
<a href="https://github.com/nambean/Pygg/actions/workflows/ci.yml"><img src="https://github.com/nambean/Pygg/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
<a href="https://www.npmjs.com/package/@pygg/cli"><img src="https://img.shields.io/npm/v/@pygg/cli/dev?label=npm%20%40pygg%2Fcli" alt="npm: @pygg/cli (dev)"></a>
<img src="https://img.shields.io/badge/licence-MIT-green" alt="Licence: MIT">
<img src="https://img.shields.io/badge/app-Windows%20x64-blue" alt="Desktop app: Windows x64">
<img src="https://img.shields.io/badge/CLI-Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-blue" alt="CLI: Windows, macOS and Linux">
<a href="https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.3"><img src="https://img.shields.io/github/v/release/nambean/Pygg?include_prereleases&label=release" alt="Release: v0.1.0-dev.3"></a>
<img src="https://img.shields.io/badge/status-developer%20preview-orange" alt="Status: developer preview">
</p>

https://github.com/user-attachments/assets/85708783-8be3-4292-955c-783cc066bbd1

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/usage-dark.svg">
  <img src="docs/images/usage-light.svg" alt="A terminal installs the pygg command line from npm, checks that Pygg's gateway answers on 127.0.0.1:8741, sets up Claude Code and starts it through Pygg with the model auto; the gateway routes each request to free and cheap models, your plans, local models or opt-in web sessions" width="100%">
</picture>
</p>

Pygg runs on your computer. Connect your providers once (API keys, coding plans, a local Ollama, even an AI website without an API), point Claude Code, Codex, OpenCode, an editor or an SDK at `127.0.0.1:8741`, and choose the model **`auto`**. Each request goes to an eligible model you connected, free and cheap ones first where they qualify, within the limits you set; when a provider says no, the next one answers. Every attempt lands in a ledger with what it cost and where that figure came from.

Since the router sees every model you connected and what each one did on your own work, it can also be the brain: name the model **`pygg/brain`** and type a requirement, and Pygg has a planner split it into cards with a role each (plan, code, test, review), picks a model per card by rule from public benchmark facts and your own kept results, and shows the proposal in the app, where you approve it into a Kanban board run one card at a time under limits you set.

> [!NOTE]
> **Developer preview (2026-11-20).** The gateway and the Windows desktop app are built and verified live, from first launch to "my coding tool uses `auto`". The Windows installer is the [prerelease `v0.1.0-dev.3`](https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.3) of 2026-11-20, **not code-signed**, so Windows SmartScreen warns before it runs. The `pygg` command line is [on npm](https://www.npmjs.com/package/@pygg/cli) for Windows, macOS and Linux. Spending limits rest on prices and token estimates, and clean-machine installs and long-running behaviour still need validation, so Pygg is **not yet for unattended or financially critical use**. What is built and how each part was verified: [Implementation Status](docs/IMPLEMENTATION-STATUS.md).

## Why Pygg

- **`auto` that you can read.** Rules over the models you connected, not a classifier: the lowest eligible tier at or above your key's minimum, at most five models in a route and at most two from one connection, so one empty account cannot end a request. Every response says why it chose what it chose, and **How auto chooses** simulates a route before you send anything.
- **Cost you can trace.** Each attempt is recorded with its cost and that cost's source: **actual** (the provider said), **estimated** (a price you or a catalog set) or **unknown**, never shown as $0. Estimated savings compare the same tokens at a model you choose, and say what they left out.
- **Fallback that does not double-bill.** A 429, 402 or rejected key moves on to the next key or target, only before the agent got its first byte. A timeout stops instead, since the provider may already have billed it. Each attempt is written to disk **before** it is sent.
- **The provider's cache keeps working.** Anthropic requests from Claude Code pass through unchanged; for OpenAI-format agents such as Codex, Pygg turns on Anthropic's prompt cache. Measured: 30% less in all, 68% less on input ([below](#measured-not-claimed)).
- **Limits that stop a session, not only a month.** Each Pygg API key can have a monthly limit and, per routing session and per UTC day, a limit that refuses the next request with 402 once reached. A request already running is never cut, and concurrent requests cannot pass a strict limit together.
- **A receipt for every launch.** When a tool started by `pygg run` exits, Pygg prints what that launch cost, how much came from the cache, which models answered, and what changed in the Git repository it ran in. `pygg launches --by-repo` sums it per repository and week. For Claude Code, cost is split by kind of request (main, subagent, compaction…).
- **Several accounts, used in turn.** A key ring holds API keys of separate accounts on one connection (in order, round robin, least used or quota aware); a pool groups connections of one provider. Each key cools down on its own.
- **AI websites as providers, carefully.** Web sessions (Muse, ChatGPT, Perplexity, DeepSeek, Grok, Gemini) are opt-in and unofficial, signed in by you in Pygg's own window, and held behind a per-site guard: one request at a time, rests between them, a daily cap, longer rests after the site's own warnings. Pictures, videos and files a site makes come back with the reply.
- **Local, with your own accounts.** The gateway listens on 127.0.0.1 only and needs a Pygg API key; provider keys stay in the OS credential store. Each tool's setup is backed up first, and Remove puts it back.
- **The router as the brain, with a board.** A requirement typed into your own coding agent becomes a proposal: cards with a role, a done criterion and dependencies, each on the model that measured best for that role (Terminal-Bench, SWE-bench Verified, the Arena dataset, in a weekly signed feed) and, from ten of your own runs on, on the model your kept results favour. You pick, change or drop, then approve; the board pulls cards into Running under a WIP limit, holds a finished run while Checking is full, blocks a card that waits for your approval or an answer, and measures cycle time and money per kept result. No step that costs money starts without your click ([BRAIN.md](docs/design/BRAIN.md), ADR-040 to ADR-042).

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

| The board | Its measures | Brain Storming |
| :---: | :---: | :---: |
| <img src="docs/images/brain/board-live.png" alt="The board of a workspace: Discovery, Ready, Running with its limit, Checking, Blocked, Review and Done; the first card of an approved brainstorm in Review after its fallback model ran" width="260"> | <img src="docs/images/brain/board-measures.png" alt="The same board at five done cards, with cycle time median, cards done today, time blocked today and money per kept result by role" width="260"> | <img src="docs/images/brain/brain-own-evidence.png" alt="Brain Storming: models by role, the code role ranking a model first on the user's own ten kept runs above the benchmark feed, and the defaults for a new brainstorm" width="260"> |

<sub>The desktop app on a copy of the maintainer's store, as it ran on 2026-11-19 (about $0.5 of real requests in all).</sub>

## How a request flows

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/request-flow-dark.svg">
  <img src="docs/images/request-flow-light.svg" alt="One request through Pygg: agent, gateway, route, policy and budget, journal; the key ring's key 1 answers 429 and key 2 answers 402, both cool down; the route's next target, Ollama, answers 200; the answer streams back and each attempt is settled in the ledger" width="100%">
</picture>
</p>

1. **Gateway.** The agent calls `127.0.0.1:8741` with its own Pygg API key, in OpenAI Chat Completions, OpenAI Responses (Codex) or Anthropic Messages, streamed, with tool calls.
2. **Route.** The model name is `auto` or `auto/cheap`, a role alias (`auto/plan`, `auto/code`, `auto/test`, `auto/review`, ranked by your own kept results, then public benchmark facts, then the tier table), a **combo** (a name for an ordered list, or cheapest first per request), a pool, `<connection>/<model>`, or `pygg/brain`, which answers with a proposal instead of running the request.
3. **Policy and budget.** The key's allowed connections, health and cooldowns, quota-group holds; a key with a monthly limit holds the attempt's estimated cost first, so concurrent requests cannot pass the limit together.
4. **Journal.** The attempt is written to disk before it is sent, and settled with its ledger entry in one transaction.
5. **Send and fall back.** Same format passes through untouched; other pairs are translated and say what they dropped. A 429 or 402 cools that key or model down for as long as the provider says, a rejected key (401) waits until you replace it, and the next key or target is tried.

The diagrams are generated by [`scripts/readme-diagrams.mjs`](scripts/readme-diagrams.mjs) and checked against `apps/desktop/src-tauri/src/gateway/`. More in [Architecture](docs/ARCHITECTURE.md).

## Install

**Desktop app (Windows 10/11 x64).** It runs the gateway, holds your connections and shows usage. Download `Pygg_0.1.0_x64-setup.exe` (or the MSI) and `SHA256SUMS.txt` from the [`v0.1.0-dev.3` prerelease](https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.3), then check the download before running it:

```powershell
Get-FileHash .\Pygg_0.1.0_x64-setup.exe -Algorithm SHA256   # compare with the line in SHA256SUMS.txt
```

The installer is **not code-signed**, so SmartScreen says "Windows protected your PC": choose **More info → Run anyway**. It installs for the current user, with `pygg-cli.exe` next to the app. To build it yourself instead, see [Development](#development).

**Command line (`pygg`), from [npm (`@pygg/cli`)](https://www.npmjs.com/package/@pygg/cli):**

```bash
npm install -g @pygg/cli@dev
```

Published under the tag `dev` (the npm badge above shows the version) for **Windows x64**, **macOS** (Apple silicon and Intel) and **Linux x64** (glibc). On Windows the CLI uses the desktop app's store and gateway; on macOS and Linux, where there is no app yet, `pygg gateway serve` runs the gateway in a terminal of its own.

## Quick start

Open Pygg, then **Providers → Connect Provider** and paste a key (Gemini, OpenRouter and Groq have free tiers; Ollama is local). Without the app, `pygg gateway add-connection --preset gemini --key-env GEMINI_API_KEY` reads the key from an environment variable. Then point your tool at Pygg:

**Claude Code** keeps your Claude sign-in; Pygg starts it through the gateway one launch at a time.

```bash
pygg setup claude          # a Pygg key of its own, kept in the credential store; no file changes
pygg run claude            # this launch through Pygg, model auto; a receipt when it exits
pygg run --statusline claude   # the same, with the launch's cost in Claude Code's status line
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

**Chat in the terminal** with any connected model, through the same router, fallbacks and ledger:

```bash
pygg chat --model muse/muse                 # a conversation; /model, /new, /cost, /exit; nothing is kept
pygg ask --model auto/cheap "Explain git worktree in two sentences"
```

**Editors and SDKs** (Cline, Continue, Roo Code, the OpenAI or Anthropic SDKs): base URL `http://127.0.0.1:8741/v1`, a key from **Endpoint → API Keys**, model `auto`.

**Claude Code plugin** (experimental): Pygg's MCP server and two skills, for handing subtasks to cheaper agents from inside Claude Code. It asks for a key with **May start tasks** on, and needs the app (or `pygg gateway serve --tasks yes`) running.

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

Every run below is the maintainer's own check: real agents, real models, checks the agent cannot edit, about $16.7 of a $20 budget for the runs to 2026-11-16 and $23.31 of the $50 set for the larger benchmark; the sponsored run was paid with its sponsor's credit. Each report gives its method, raw results and what it does not show; read it before quoting a number. Summary: [BENCHMARKS.md](docs/BENCHMARKS.md).

| What was measured | Result | Report |
| --- | --- | --- |
| OpenCode on 12 small Node tasks × 3 (3 bug fixes, 8 features, 1 three-file refactor; 20 to 211 lines each), through Pygg to Claude Haiku 5.5 instead of Sonnet 5.5 | **88% less per solved task** (95% CI 87–90%); one attempt per run, no retry: 36/36 passed against 34/36 | [N2](benchmark/reports/2026-11-12-n2-savings.md) |
| Claude Code on the same tasks, Haiku 5.5 instead of Sonnet 5.5 | **79% less per solved task** (95% CI 74–84%); `auto/cheap` with OpenCode: 34/36 at $0.0129 per solved task | [P0](benchmark/reports/2026-11-12-p0-optimization.md) |
| Claude Code on six tasks from a real production repository (Express + Prisma API, features across API, reports and Excel export, 124-check end-to-end suite) | Haiku 5.5: **6/6 for $1.50**, one attempt each; Sonnet 5.5: 4/5 for $1.19; on the 4 both solved, Haiku cost **about 40% less**, in 2 to 3 times the requests. OpenCode with `auto/cheap`: 2/6 for $0.35 | [CCHT](benchmark/reports/2026-11-13-ccht-real-repository.md) |
| Codex on Claude Haiku 5.5, Pygg's prompt caching off vs on | 16/16 either way; **30% less in all, 68% less on input** | [Prompt cache](benchmark/reports/2026-11-14-codex-claude-prompt-cache.md) |
| An OpenAI-format agent on Claude Haiku 5.5 through OpenRouter, with Pygg's cache marker | After each session's first turn, **99.7% of every prompt read from cache**; $0.0066 in all | [OpenRouter cache](benchmark/reports/2026-11-16-openrouter-cache-live.md) |
| The gateway's own overhead, against a local fake provider | **About 4 ms** per short request, 5 ms per 400 kB prompt; about 230 requests/s with 16 clients | [Overhead](benchmark/reports/2026-11-14-gateway-overhead.md) |
| OpenCode on all 36 fixture cases, one attempt each, on 15 routes: four Gemini models, five Alibaba plan models, two local 8B models, `auto`, `auto/cheap`, `auto/code` | **36/36 on four routes**: DeepSeek V4.1 Flash, Qwen 3.8 Max and `auto/cheap` on a monthly plan (quota, no metered money), and Gemini 4 Hydrogen at **$0.072 per solved task**; `auto/code` picked Gemini 4 Carbon, 33/36 at $0.115; local 8B models 3/36 and 0/36; nearly every miss a `hard-*` feature | [Every model](benchmark/reports/2026-11-20-all-models.md) |
| OpenCode on the 17 hardest cases, three attempts each, five routes | **DeepSeek V4.1 Flash 51/51** on a plan; Gemini 4 Hydrogen 50/51 at **$0.106 per solved run**; `auto/cheap` 49/51 on quota; `auto/code` on Hydrogen 18/20, then on GLM 5.3 (21/31) after the Gemini credit ran out mid-run, with no error reaching the agent | [Hard × 3](benchmark/reports/2026-11-20-hard-repeat.md) |
| Sponsored by MixAICloud: DeepSeek, Qwen and Kimi through MixAICloud, 17 hard cases × 3 and 40 light tasks × 3 | Coding: **DeepSeek V4 Flash climbing to Qwen 3.8 Max, 49/51 at $0.034 per solved run**; light tasks: `auto/cheap`, now learning each model's real answer length and cache use, **$0.23 per 1,000 correct answers instead of $1.91** | [MixAICloud](benchmark/reports/2026-11-20-mixaicloud.md) |
| A real website from a one-page spec: a strong model alone, a cheap model alone, and the cheap model through **Brain Storming** (sponsored by MixAICloud) | Qwen 3.6 Flash alone: **0/37** hidden API checks in three runs; through Brain: **37/37 API, 20/21 UI**, as DeepSeek V4 Pro alone scores (36–37, 17–20); blind reviews 7 vs 7 (Codex) and 5 vs 8 (Opus); it cost **$5.78 against $0.20–0.41**, as the cheap model got no prompt cache | [Website](benchmark/reports/2026-11-21-stockroom-brain.md) |
| Web sessions on five sites, 48 short tasks | **47/48 correct**, about 18 s each, $0 | [Web sessions](benchmark/reports/2026-11-13-web-sessions.md) |

Not claimed: a quality ranking of models (a handful of tasks each, or one attempt per task in the largest run), a provider's bill (costs are the ledger at list prices), "60–95% fewer tokens", or savings on large refactors, database migrations or other languages, which no run has measured yet. The 88% is the whole session pinned to a cheaper model on small tasks; on the real repository the saving narrowed to about 40%, and a cost-first `auto/cheap` over free models solved 2 of 6. A longer web-session run on coding tasks got the owner's DeepSeek account suspended for three days ([report](benchmark/reports/2026-11-13-web-coding.md)); the guard has been stricter since.

### Benchmark it on your work

One person's runs on a few dozen tasks are a start, not proof. The benchmark needs the community: run the [harness](benchmark/README.md) on the cases here or on your own repositories (they can stay private; only the result lines are published, as in [CCHT](benchmark/reports/2026-11-13-ccht-real-repository.md)), add cases the runs above lack, such as large refactors, database migrations and other languages, and open a pull request with the report and its raw results ([how](CONTRIBUTING.md#benchmark-runs)). A run where the cheaper model loses is as welcome as one where it wins.

## Compared with other routers

All five sit between your coding tools and the model providers. Pygg and LiteLLM were run against the same fake provider and requests (**M**); the others are read from their own documentation and source (**D**: 9router and OmniRoute on 2026-11-14 and again on 2026-11-20, LiteLLM 1.106.2 and OpenRouter on 2026-11-14). ✅ yes · ⚠️ partly, opt-in, or with a catch · ❌ no · — not documented where we looked, which is not proof it is absent.

| Feature | **Pygg** (this project) | [9router](https://github.com/decolua/9router) | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | [LiteLLM](https://github.com/BerriAI/litellm) proxy | [OpenRouter](https://openrouter.ai) |
| --- | --- | --- | --- | --- | --- |
| Runs on your computer, open source | ✅ desktop app (Windows) and headless gateway; MIT | ✅ Node.js server; MIT | ✅ Node.js or Electron; MIT | ✅ Python or Docker; MIT except `enterprise/` | ❌ hosted service |
| Falls back when a provider is rate-limited, out of credit or rejects the key | ✅ 100% served, **1.04** provider requests each, ~70 ms (M) | ✅ on 401, 402, 403, 429 and 5xx (D) | ⚠️ on rate limits, 5xx and timeouts, not on auth errors (D) | ✅ 100% served, 4 provider requests each, ~4.6 s (M) | ✅ with a `models` list (D) |
| Never re-sends a request the provider may already have run (5xx, dropped connection, timeout) | ✅ by default; one 5xx retry can be allowed (M) | ❌ moves to the next model (D) | ❌ up to 3 attempts (D) | ❌ 3 attempts at the failing provider (M) | — |
| Waits as long as `Retry-After` says | ✅ up to 7 days (M) | ❌ fixed cooldowns (D) | ✅ on 429 (D) | ⚠️ between retries, up to 60 s (M) | ⚠️ passes it to the client (D) |
| Keys of several accounts, each cooling down on its own | ✅ key ring, each key confirmed as another account (M) | ✅ round robin or priority (D) | ✅ key pools with fair-share quotas (D) | ⚠️ one deployment per key, no account concept (M) | ⚠️ your own keys in priority order (D) |
| A session stays on one key, so the provider's cache keeps working | ✅ by default, 60 / 60 sessions (M) | ⚠️ with its `smart` strategy (D) | ⚠️ with its `cache-optimized` strategy (D) | ⚠️ opt-in; 0 / 60 by default (M) | ✅ by default (D) |
| Prompt cache for OpenAI-format agents (Codex) on Claude | ✅ automatic, **89.5%** of the prompt read from cache (M) | — | — | ⚠️ once configured: 89.5% Chat Completions, 39.7% Responses; 0% by default (M) | ⚠️ the client must send `cache_control` (D) |
| Every attempt in a ledger, with where its cost came from | ✅ fallbacks and failures included; unknown never shown as $0 (M) | ⚠️ cost "for tracking only" (D) | ✅ audit trail and cost headers (D) | ⚠️ spend logs; per-attempt rows not documented (D) | ⚠️ usage per key (D) |
| Spending limits | ✅ per key and month, session or day; strict limits hold each request's maximum, so concurrent requests cannot pass them (M) | ⚠️ "per provider" in its FAQ, mechanism not described (D) | ✅ per-key USD quotas (D) | ✅ budgets per key, user and team (D) | ✅ a credit limit per key (D) |
| Choosing the model for you | ✅ `auto` (tier floor), `auto/cheap` (expected cost learned from your own answers), `auto/code` and other roles (benchmark facts, then your kept results), each choice explained (M) | ⚠️ ordered combos you build (D) | ✅ `auto` with 16-factor scoring, `auto/cheap`, `auto/coding` (D) | ⚠️ cost-based routing; a complexity router in beta (D) | ✅ `openrouter/auto` (D) |
| One-command setup of coding tools | ✅ Claude Code, Codex, OpenCode; backed up first, `--remove` restores (M) | ⚠️ OpenClaw from its dashboard; others by hand (D) | ✅ `run` and `configure` for 15 tools (D) | — | — |
| AI chat websites as providers | ✅ 6 sites, opt-in, behind a per-site guard that cannot be switched off (M) | ⚠️ 6 sites; no pacing or prompt cap found in its code (D) | ⚠️ 3 sites; pacing not documented (D) | ❌ | ❌ |
| Throughput | ⚠️ about 230 requests/s on one PC, 4 ms added per request (M) | — | — | ✅ 1,170 requests/s on 4 instances, its own test (D) | — |

**Where Pygg is worse:** throughput is for one person's tools, not a team's traffic; a provider that hangs gets no timeout fallback; by default a 5xx or a dropped connection reaches your agent as an error, where LiteLLM served 100% after re-sending; and a strict limit assumes the provider honours the request's output limit (a thinking model that writes past it can pass the limit by what it overran). Details, sources and the measured runs: [BENCHMARKS.md](docs/BENCHMARKS.md#pygg-next-to-other-gateways), [resilience](benchmark/reports/2026-11-14-resilience.md), [tokens and cost](benchmark/reports/2026-11-14-token-savings.md), [web guard](benchmark/reports/2026-11-14-web-guard.md).

**Is Pygg a fork of 9router?** No. 9router, a local router for the providers you already have, was one of the inspirations for building the gateway first (ADR-016). Pygg is written from scratch in Rust; the one part that follows 9router is the Muse web-session recipe, credited under MIT in [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md).

## What's inside

```text
Coding agents ──HTTP──► Gateway 127.0.0.1:8741 (axum) ──► OpenAI- and Anthropic-compatible APIs, coding plans,
  Claude Code, Codex,     auth · route · policy · journal       local runtimes (Ollama …), web sessions (WebView2
  OpenCode, SDKs          translate · fall back · settle         windows behind the guard)
                                   │
       React UI ◄── Tauri ──► Rust core ──► SQLite store (ledger, journal, connections) · OS credential store
       pygg CLI ──────────────┘
```

- **One Rust crate** (Tauri 2): the gateway (axum), the SQLite store, the OS credential store, web-session windows, and the headless programs (`pygg-cli`, `gateway`, `pygg-mcp`) built from the same library.
- **Interface:** React 19, Vite and TypeScript, with a layout check over every screen in CI (`pnpm ui-check`).
- **Skills & Prompts:** one library of skills in the Agent Skills format, installed into Claude Code's, Codex's and OpenCode's own skills folders, and a count of what each agent sends with every request from its global files (ADR-039).
- **[`@pygg/cli` on npm](https://www.npmjs.com/package/@pygg/cli):** a Node launcher with one optional package per platform (ADR-037).
- **Smart tasks** (experimental): IDE agents hand subtasks to Pygg over MCP, or send a requirement to `pygg/brain`; agent CLIs run the tasks in Git worktrees against the repository's approved checks, paid steps wait for your approval, and the board (ADR-042) runs an approved brainstorm's cards under WIP limits with the Brain Storming screen holding the picks and defaults for every project ([AGENTS.md](docs/AGENTS.md), [BRAIN.md](docs/design/BRAIN.md)). The model facts feed behind the role ranks is built weekly by [`scripts/model-facts.py`](scripts/model-facts.py) from sources with open licences, signed, and verified by the app before use (ADR-040). Each part has run live once on the maintainer's store, not under the benchmark harness.

## Documentation

| | |
| --- | --- |
| **Use** | [Getting started](docs/GETTING-STARTED.md) · [Providers](docs/PROVIDERS.md) · [Benchmarks](docs/BENCHMARKS.md) · [Security](docs/SECURITY.md) |
| **Understand** | [Architecture](docs/ARCHITECTURE.md) · [Decisions (ADR-001 to ADR-042)](docs/DECISIONS.md) · [The brain, the facts feed and the board](docs/design/BRAIN.md) · [Schema](docs/SCHEMA.md) · [Screens](docs/design/SCREENS.md) · [Command line](docs/design/CLI.md) |
| **Track** | [Implementation status](docs/IMPLEMENTATION-STATUS.md) · [Roadmap](docs/ROADMAP.md) · [Benchmark reports](benchmark/reports) |
| **Contribute** | [Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Every document, indexed](docs/README.md) |

Only the app's data folder (`app.smarttaskrouter.desktop`) and its credential service name keep the engineering name SmartTaskRouter, so existing data stays readable. Brand assets are in [branding](branding/README.md).

## Development

Requirements: Node.js LTS with pnpm 9 (`corepack enable`), stable Rust through rustup, and on Windows the Visual Studio C++ Build Tools and WebView2 (built into Windows 11).

```powershell
pnpm install
pnpm dev                                              # the interface at http://127.0.0.1:1431 with demo data (?empty for a first run)
pnpm --filter @pygg/desktop tauri:dev     # the desktop app with the real gateway
pnpm typecheck
pnpm --filter @pygg/desktop tauri:build   # the installers, under apps/desktop/src-tauri/target/release/bundle
pnpm ui-check                                         # every screen at several window sizes, nothing overflowing
cd apps/desktop/src-tauri; cargo test --lib --tests   # core, gateway, web-session and task engine tests
node scripts/readme-diagrams.mjs                      # regenerate the README's animated diagrams
python scripts/model-facts.py selftest                # the model facts builder on its fixtures (build, sign, verify: see the script)
```

`PYGG_DATA_DIR` points the app at another store, for trying it without touching your own; that app runs beside the installed one, with its own window profile, and needs a gateway port of its own (Endpoint → Configure…).

## Sponsors

- **[MixAICloud](https://us.mixaicloud.com)** ([TheoZhang3321 on X](https://x.com/TheoZhang3321)), the project's first sponsor: API credit, given on 2026-11-20 for a benchmark of how Pygg routes the work MixAICloud's users send to DeepSeek and Qwen (coding) and to GLM and Kimi (lighter and conversation tasks): [the report](benchmark/reports/2026-11-20-mixaicloud.md).

A sponsor's credit pays for traffic, not for results. A sponsored run is published like any other, with its method, raw results, spend and every route where Pygg's choice lost ([BENCHMARKS.md](docs/BENCHMARKS.md)), and its report names who paid for it.

## Licence

MIT, see [LICENSE](LICENSE). Third-party code and data are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
