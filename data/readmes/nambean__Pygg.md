<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="branding/pygg-logo-dark.svg">
  <img src="branding/pygg-logo.svg" alt="Pygg — One Flow. Many Agents." width="380">
</picture>
</p>

<h3 align="center">Run your coding agents on cheaper models without losing the answers.</h3>

<p align="center">Pygg is a local gateway that routes each request to a model you connected, and measures what it saved:<br><b><a href="#measured-not-claimed">88% less per solved task</a></b> in our benchmark, with every task still solved.</p>

<p align="center">
<a href="https://github.com/nambean/Pygg/actions/workflows/ci.yml"><img src="https://github.com/nambean/Pygg/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
<a href="https://www.npmjs.com/package/@pygg/cli"><img src="https://img.shields.io/npm/v/@pygg/cli/dev?label=npm%20%40pygg%2Fcli" alt="npm: @pygg/cli (dev)"></a>
<img src="https://img.shields.io/badge/licence-MIT-green" alt="Licence: MIT">
<img src="https://img.shields.io/badge/app-Windows%20x64-blue" alt="Desktop app: Windows x64">
<img src="https://img.shields.io/badge/CLI-Windows%20%C2%B7%20macOS%20%C2%B7%20Linux-blue" alt="CLI: Windows, macOS and Linux">
<a href="https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.1"><img src="https://img.shields.io/github/v/release/nambean/Pygg?include_prereleases&label=release" alt="Release: v0.1.0-dev.1"></a>
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

> [!NOTE]
> **Developer preview (2026-11-14).** The gateway and the Windows desktop app are built and verified live, from first launch to "my coding tool uses `auto`". The Windows installer is a [prerelease, `v0.1.0-dev.1`](https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.1), **not code-signed**, so Windows SmartScreen warns before it runs. The `pygg` command line is [on npm](https://www.npmjs.com/package/@pygg/cli) for Windows, macOS and Linux. Spending limits rest on prices and token estimates, and clean-machine installs and long-running behaviour still need validation, so Pygg is **not yet for unattended or financially critical use**. What is built and how each part was verified: [Implementation Status](docs/IMPLEMENTATION-STATUS.md).

## Why Pygg

- **`auto` that you can read.** Rules over the models you connected, not a classifier: the lowest eligible tier at or above your key's minimum, at most five models in a route and at most two from one connection, so one empty account cannot end a request. Every response says why it chose what it chose, and **How auto chooses** simulates a route before you send anything.
- **Cost you can trace.** Each attempt is recorded with its cost and that cost's source: **actual** (the provider said), **estimated** (a price you or a catalog set) or **unknown**, never shown as $0. Estimated savings compare the same tokens at a model you choose, and say what they left out.
- **Fallback that does not double-bill.** A 429, 402 or rejected key moves on to the next key or target, only before the agent got its first byte. A timeout stops instead, since the provider may already have billed it. Each attempt is written to disk **before** it is sent.
- **The provider's cache keeps working.** Anthropic requests from Claude Code pass through unchanged; for OpenAI-format agents such as Codex, Pygg turns on Anthropic's prompt cache. Measured: 30% less in all, 68% less on input ([below](#measured-not-claimed)).
- **Several accounts, used in turn.** A key ring holds API keys of separate accounts on one connection (in order, round robin, least used or quota aware); a pool groups connections of one provider. Each key cools down on its own.
- **AI websites as providers, carefully.** Web sessions (Muse, ChatGPT, Perplexity, DeepSeek, Grok) are opt-in and unofficial, signed in by you in Pygg's own window, and held behind a per-site guard: one request at a time, rests between them, a daily cap, longer rests after the site's own warnings.
- **Local, with your own accounts.** The gateway listens on 127.0.0.1 only and needs a Pygg API key; provider keys stay in the OS credential store. Each tool's setup is backed up first, and Remove puts it back.

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
2. **Route.** The model name is `auto` or `auto/cheap`, a **combo** (a name for an ordered list, or cheapest first per request), a pool, or `<connection>/<model>`.
3. **Policy and budget.** The key's allowed connections, health and cooldowns, quota-group holds; a key with a monthly limit holds the attempt's estimated cost first, so concurrent requests cannot pass the limit together.
4. **Journal.** The attempt is written to disk before it is sent, and settled with its ledger entry in one transaction.
5. **Send and fall back.** Same format passes through untouched; other pairs are translated and say what they dropped. A 429 or 402 cools that key or model down for as long as the provider says, a rejected key (401) waits until you replace it, and the next key or target is tried.

The diagrams are generated by [`scripts/readme-diagrams.mjs`](scripts/readme-diagrams.mjs) and checked against `apps/desktop/src-tauri/src/gateway/`. More in [Architecture](docs/ARCHITECTURE.md).

## Install

**Desktop app (Windows 10/11 x64).** It runs the gateway, holds your connections and shows usage. Download `Pygg_0.1.0_x64-setup.exe` (or the MSI) and `SHA256SUMS.txt` from the [`v0.1.0-dev.1` prerelease](https://github.com/nambean/Pygg/releases/tag/v0.1.0-dev.1), then check the download before running it:

```powershell
Get-FileHash .\Pygg_0.1.0_x64-setup.exe -Algorithm SHA256   # compare with the line in SHA256SUMS.txt
```

The installer is **not code-signed**, so SmartScreen says "Windows protected your PC": choose **More info → Run anyway**. It installs for the current user, with `pygg-cli.exe` next to the app. To build it yourself instead, see [Development](#development).

**Command line (`pygg`), from [npm (`@pygg/cli`)](https://www.npmjs.com/package/@pygg/cli):**

```bash
npm install -g @pygg/cli@dev
```

`0.1.0-dev.7` under the tag `dev`, for **Windows x64**, **macOS** (Apple silicon and Intel) and **Linux x64** (glibc). On Windows the CLI uses the desktop app's store and gateway; on macOS and Linux, where there is no app yet, `pygg gateway serve` runs the gateway in a terminal of its own.

## Quick start

Open Pygg, then **Providers → Connect Provider** and paste a key (Gemini, OpenRouter and Groq have free tiers; Ollama is local). Without the app, `pygg gateway add-connection --preset gemini --key-env GEMINI_API_KEY` reads the key from an environment variable. Then point your tool at Pygg:

**Claude Code** keeps your Claude sign-in; Pygg starts it through the gateway one launch at a time.

```bash
pygg setup claude          # a Pygg key of its own, kept in the credential store; no file changes
pygg run claude            # this launch through Pygg, model auto
```

**Codex CLI** gets a `pygg` provider and profile, after a backup; its default model is not changed.

```bash
pygg setup codex
pygg run codex             # or: codex --profile pygg -m auto/cheap
```

**OpenCode** gets a Pygg provider listing `auto`, `auto/cheap` and your enabled models, kept current.

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

Each `setup` takes `--dry-run` to show what would change and `--remove` to undo it. The same set-up is one click in **CLI Tools**. Step by step, with troubleshooting: [Getting started](docs/GETTING-STARTED.md).

## Measured, not claimed

Real agents, real models, checks the agent cannot edit, about $16.7 of a $20 budget in all. Each report gives its method, raw results and what it does not show; read it before quoting a number. Summary: [BENCHMARKS.md](docs/BENCHMARKS.md).

| What was measured | Result | Report |
| --- | --- | --- |
| OpenCode on 12 harder coding tasks × 3, through Pygg to Claude Haiku 5.5 instead of Sonnet 5.5 | **88% less per solved task** (95% CI 87–90%); 36/36 solved against 34/36 | [N2](benchmark/reports/2026-11-12-n2-savings.md) |
| Claude Code on the same tasks, Haiku 5.5 instead of Sonnet 5.5 | **79% less per solved task** (95% CI 74–84%); `auto/cheap` with OpenCode: 34/36 at $0.0129 per solved task | [P0](benchmark/reports/2026-11-12-p0-optimization.md) |
| Claude Code on six tasks from a real production repository | Haiku 5.5: **6/6 for $1.50**, 96% of input read from cache; Sonnet 5.5: 4/5 for $1.19; OpenCode with `auto/cheap`: 2/6 for $0.35 | [CCHT](benchmark/reports/2026-11-13-ccht-real-repository.md) |
| Codex on Claude Haiku 5.5, Pygg's prompt caching off vs on | 16/16 either way; **30% less in all, 68% less on input** | [Prompt cache](benchmark/reports/2026-11-14-codex-claude-prompt-cache.md) |
| The gateway's own overhead, against a local fake provider | **About 4 ms** per short request, 5 ms per 400 kB prompt; about 230 requests/s with 16 clients | [Overhead](benchmark/reports/2026-11-14-gateway-overhead.md) |
| Web sessions on five sites, 48 short tasks | **47/48 correct**, about 18 s each, $0 | [Web sessions](benchmark/reports/2026-11-13-web-sessions.md) |

Not claimed: a quality ranking of models (a handful of tasks each), a provider's bill (costs are the ledger at list prices), or "60–95% fewer tokens". A longer web-session run on coding tasks got the owner's DeepSeek account suspended for three days ([report](benchmark/reports/2026-11-13-web-coding.md)); the guard has been stricter since.

**Next to LiteLLM**, measured with the same fake provider and requests (LiteLLM 1.106.2, defaults plus fallbacks; other projects compared from their docs in [BENCHMARKS.md](docs/BENCHMARKS.md#pygg-next-to-other-gateways)):

| When the primary provider… | Pygg | LiteLLM proxy |
| --- | --- | --- |
| is rate-limited, out of credit or unreachable | 100% served, **1.04** provider requests each, ~70 ms | 100% served, 4 provider requests each, ~4.6 s (88 s with `Retry-After: 30`) |
| fails with 500 or drops the connection | 96% / 0% served: never re-sent unless you allow it (100% for a 500 with one retry allowed) | 100% served, after 3 attempts at the failing provider each |
| is Claude, reached by an OpenAI-format agent | **89.5%** of the prompt read from cache, automatically | 0% by default; 89.5% (Chat Completions) or 39.7% (Codex's Responses API) with injection points configured |
| sits behind a key ring of several accounts | sessions stay on one key: 60 / 60 | 0 / 60 by default, 60 / 60 with affinity on |

Where Pygg is worse: about 230 requests/s on one PC (LiteLLM publishes 1,170 on four instances), no timeout fallback for a hung provider, and a 5xx or dropped connection reaches your agent as an error by default. Reports: [resilience](benchmark/reports/2026-11-14-resilience.md), [tokens and cost](benchmark/reports/2026-11-14-token-savings.md), [web guard](benchmark/reports/2026-11-14-web-guard.md).

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
- **Smart tasks** (experimental, on hold): IDE agents hand subtasks to Pygg over MCP; agent CLIs run them in Git worktrees against approved checks ([AGENTS.md](docs/AGENTS.md)).

## Is Pygg a fork of 9router?

No. Pygg is the same kind of tool as [9router](https://github.com/decolua/9router): a local router that points your coding agents at the providers you already have. 9router was one of the inspirations for building the gateway first (ADR-016). Pygg's code is written from scratch in Rust; the one part that follows 9router is the Muse web-session recipe, credited under MIT in [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md).

Where they differ, read from 9router's documentation and source (not run here):

- **Re-sending.** 9router moves to the next model on a 5xx or a timeout; Pygg does not re-send a request the provider may already have run, unless you allow one retry.
- **`Retry-After`.** 9router uses fixed cooldowns; Pygg waits as long as the provider says.
- **Prompt cache.** Pygg keeps each session on one key by default (9router with its `smart` strategy) and adds Anthropic's cache marker for OpenAI-format agents such as Codex.
- **Cost.** 9router's cost is "for tracking only"; Pygg records every attempt, fallbacks included, with where its cost came from.
- **Web sessions.** Both drive AI websites; Pygg holds each site behind a guard (one request at a time, rests, a daily cap) that cannot be switched off.

The full table, with LiteLLM, OpenRouter, OmniRoute and claude-code-router: [BENCHMARKS.md](docs/BENCHMARKS.md#pygg-next-to-other-gateways).

## Documentation

| | |
| --- | --- |
| **Use** | [Getting started](docs/GETTING-STARTED.md) · [Providers](docs/PROVIDERS.md) · [Benchmarks](docs/BENCHMARKS.md) · [Security](docs/SECURITY.md) |
| **Understand** | [Architecture](docs/ARCHITECTURE.md) · [Decisions (ADR-001 to ADR-039)](docs/DECISIONS.md) · [Schema](docs/SCHEMA.md) · [Screens](docs/design/SCREENS.md) · [Command line](docs/design/CLI.md) |
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
```

`PYGG_DATA_DIR` points the app at another store, for trying it without touching your own.

## Licence

MIT, see [LICENSE](LICENSE). Third-party code and data are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
