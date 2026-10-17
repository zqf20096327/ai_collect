<div align="center">

# FABULA

**A local-first coding agent that doesn't take "done" on faith.**

The engine keeps the run going until the project's own tests pass — and every green run leaves a receipt anyone can replay.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-black)](#install)
[![Release](https://img.shields.io/github/v/release/sergezuber/FABULA-LLM-5)](https://github.com/sergezuber/FABULA-LLM-5/releases)

[**Install**](#install) · [Try it](#try-it-replay-a-real-run) · [What's measured](#what-is-measured-and-what-is-not) · [Receipt spec](docs/spec/verified-autonomy-receipt-v0.2.md) · [Plugins](docs/PLUGINS.md) · [Docs](#docs)

[English](README.md) · [中文](README.zh-CN.md) · [Русский](README.ru.md)

</div>

![How FABULA works](docs/assets/how-it-works.svg)

## What it is

FABULA is a coding agent built for **one model on one machine** — a small local model served by LM Studio or MLX, or any OpenAI-compatible endpoint you already have. It is a desktop app (macOS) and a local server with a web UI (Linux, Windows), built on a fork of [MiMoCode](https://github.com/XiaomiMiMo/MiMo-Code), itself an OpenCode fork ([what that means](NOTICE.md)).

The bet: **reliability lives in the machinery around the model, not in the model.** A small model will say "done" when it is not. FABULA does not argue with it in a prompt; the rules live in the engine's run loop, where the model cannot talk past them.

*Fabula* is Latin for "a story" — what most agents end a hard task with: a confident paragraph about work that may not exist. Here a run ends in one of two states: **VERIFIED**, with a receipt, or **NOT DONE**, over the real failing output.

## What it does

### 1. "Done" is a test result

In a project with tests, an edit is not finished until the project's own tests have run green after it. A turn that stops early is sent back to work by the engine — when source was edited and never verified, when the last run was red, when every edit failed to apply, or when tools were used but the tests never ran. The re-entries are bounded; past them the run ends explicitly **NOT DONE**, not in silence. With `/goal`, a judge also reads the recorded trajectory — not the model's summary — and can override a "done" it contradicts.

*Status: the problem is measured — in one SWE-bench Pro campaign, 15 of 16 sessions never ran the tests. The effect of the guard on outcomes has not been measured yet.*

### 2. Every green run leaves a receipt you can replay

A green run mints a **Proof-of-Done receipt**: the diff, the base commit, the exact verify command and its result, the model that did the work, and a fingerprint of the context it worked in. `fabula receipt verify` applies the patch to the recorded base in a throwaway worktree and runs the command again.

Be clear about what that is: a **replayable record**, not a signature. It shows that this patch on this base passes this command, on your machine, now. It does not prove the tests are meaningful — read the diff. The format is an open spec: [verified-autonomy receipt v0.2](docs/spec/verified-autonomy-receipt-v0.2.md).

### 3. Made for one small model and one inference slot

- **The prompt prefix stays byte-stable within a task,** so the model's KV cache survives from step to step instead of re-reading everything.
- **Compaction measures the fixed cost of the prompt** before deciding a window is full — on a local model the system prompt and tool schemas can take most of the window, and a fixed percentage would compact on every turn.
- **A local adapter queues requests for the single inference slot** instead of letting them race: the live turn goes first, background work waits, and a request that waits too long is told to retry rather than being run concurrently.
- **Optional accelerated lane** for models marked ⚡ (speculative decoding, output identical to ordinary decoding), started when you pick such a model and stopped when you switch away, so two runtimes never hold a large model at once.
- **Guards on every door:** a rule that blocks a tool also blocks the same thing through the shell; code without a container runs under the OS kernel profile (Seatbelt on macOS, bubblewrap on Linux); SSRF, secret redaction and prompt-injection wrapping on everything fetched.

23 plugins, 62 tools, loaded in a declared order: [`docs/PLUGINS.md`](docs/PLUGINS.md).

## Try it: replay a real run

A captured run is committed verbatim. Replay it:

```bash
cd demo && fabula receipt verify
```

```
VERIFIED ✓ — the artifact replayed deterministically:
base c660a02ab138 + patch → `bun test` passed.
```

A harder one is public too: **one** real [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) task (`qutebrowser`), solved end-to-end by a local model on one consumer machine and graded by the benchmark's *hidden* tests — 4 of 4 fail-to-pass passed, no regressions — with a one-command Docker replay in [`docs/receipts/`](docs/receipts/). That is **n = 1**, published so it can be replayed and disputed; it is not a benchmark score.

Or run the two-minute demo yourself: open [`demo/`](demo/) as the project (a bug is planted there and every test is green anyway) and ask *"Fix the export bug: the nightly export silently drops rows dated exactly on the end date. Prove it."* The engine will not call it done until the tests have run green after the edit.

## What is measured, and what is not

FABULA publishes no aggregate resolve rate; [`docs/EVALS.md`](docs/EVALS.md) explains why and what would earn one.

| Claim | Status |
|---|---|
| Small local models end turns without running the tests | **Measured**: 15 of 16 sessions in one SWE-bench Pro campaign |
| The finish guard improves outcomes | **Not measured** |
| One SWE-bench Pro task solved end-to-end by a local model | **Replayable**, n = 1 |
| A per-task tool router saves tokens | A/B, n = 7: −7% schema tokens, but every task ran slower — **off by default** |
| The harness beats the same model without it | **Not yet run** — the experiment that decides the whole bet |

Mechanisms that measured as harmful, never fired, or were broken have been removed rather than kept as features; the changelog in the app (Settings ▸ Changelog) lists each one and why.

## Install

**You need `git` and a model** — one running on this machine or an OpenAI-compatible endpoint. `setup.sh` installs the engine, Bun and four npm packages, and stops. You pick the model in the app.

<details>
<summary><b>What it installs, and what it deliberately does not</b></summary>

Four npm packages, `git`, the engine, and the localhost adapter FABULA talks to a local model through. Nothing large arrives unasked. Four capabilities are yours to add, each with its price:

| Capability | Costs | Say no if |
|---|---|---|
| Drive a real browser | a Chromium download (~150 MB) | You want it for code. Reading a page is `web_fetch`, installed either way. |
| Search the web | a local SearXNG | The machine is offline, or you already run one elsewhere. |
| Run code in a container | Docker Desktop | Code still runs, confined by the OS kernel profile where the platform has one. Windows has none, so there a container is the only isolation. |
| Speech in and out | a few hundred MB of models | You do not intend to talk to it. |

`./setup.sh --with=browser` adds one, `--ask` walks through all four, `--all` takes everything, `--minimal` skips even the adapter.

</details>

### macOS — the desktop app

Apple Silicon plus the Xcode Command Line Tools (`xcode-select --install`).

```bash
git clone https://github.com/sergezuber/FABULA-LLM-5 && cd FABULA-LLM-5
./setup.sh
open FABULA-LLM-5.app
```

### Linux

```bash
git clone https://github.com/sergezuber/FABULA-LLM-5 && cd FABULA-LLM-5
./setup.sh
bin/fabula serve --port 4096      # then open http://127.0.0.1:4096
```

The desktop window builds separately as a `.deb`: `bash shell/build.sh`.

### Windows

Install **Git for Windows** first — the shell guards parse one POSIX grammar.

```powershell
git clone https://github.com/sergezuber/FABULA-LLM-5; cd FABULA-LLM-5
.\setup.ps1
bin\fabula.exe serve --port 4096   # then open http://127.0.0.1:4096
```

Re-run `setup.sh` any time; it rebuilds only when the installed engine is older than the source, and never overwrites your `.env` or `fabula.config.json`. To update: quit the app, `git pull && ./setup.sh`, reopen.

### Point it at a model

**On this machine:** open LM Studio, load a tool-calling model, start its server. Setup already installed the adapter the config points at.

<details>
<summary><b>Any OpenAI-compatible endpoint</b> — a cloud provider or a corporate gateway</summary>

Put the key in `.env` (gitignored) and describe the provider in `fabula.config.json`:

```jsonc
// .env
MY_API_KEY=sk-...

// fabula.config.json
{
  "model": "myapi/my-model-id",
  "provider": {
    "myapi": {
      "name": "My endpoint",
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "https://llm.example.com/v1", "apiKey": "{env:MY_API_KEY}" },
      "models": {
        "my-model-id": { "tools": true, "limit": { "context": 131072, "output": 32768 } }
      }
    }
  }
}
```

The model must support **tool calling**, and `limit` needs both `context` and `output`.

</details>

## Privacy

There is no account and no telemetry. With only local providers configured, your prompts, files and chats stay on the machine. Everything that does go out is listed here — the list is the promise.

**By default (three connections, each with a switch):**

- **Update notice** — asks GitHub which release is newest; sends nothing about you. Off in Settings ▸ General.
- **Model catalogue** — fetches `https://models.dev/api.json` at start and hourly so the picker knows context sizes. `MIMOCODE_DISABLE_MODELS_FETCH=1` turns it off; `MIMOCODE_MODELS_URL` points it at a mirror.
- **Language servers on first use** — downloaded from GitHub releases or npm when a project needs one. `MIMOCODE_DISABLE_LSP_DOWNLOAD=1` stops it.

**Only if you configure or ask for it:** a cloud model (it sees what you send it — your choice of `provider`), the optional quiz and attest gates (they call an auxiliary model, local first), and tools you invoke — `web_search` against your own SearXNG, `web_fetch` and the browser on the pages you name, `ntfy.sh` notifications only with `FABULA_NTFY_TOPIC` set.

Until 0.292.0 the vendored engine carried an analytics uploader that was on by default. It is deleted at the source, and a build gate ([`no-phone-home.gate.test.ts`](plugin/__tests__/no-phone-home.gate.test.ts)) fails if a tracking endpoint reappears in the source or in the shipped binary.

## Docs

| Topic | Where |
|---|---|
| Every plugin and tool | [`docs/PLUGINS.md`](docs/PLUGINS.md) |
| Architecture | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| The receipt spec | [`docs/spec/verified-autonomy-receipt-v0.2.md`](docs/spec/verified-autonomy-receipt-v0.2.md) |
| Public replayable receipts | [`docs/receipts/`](docs/receipts/) |
| Evals and run notes | [`docs/EVALS.md`](docs/EVALS.md) |
| The protocol (draft) | [`docs/GREENPAPER.md`](docs/GREENPAPER.md) |
| Dependencies and install commands | [`DEPENDENCIES.md`](DEPENDENCIES.md) |
| Configuration templates | [`fabula.config.example.json`](fabula.config.example.json) · [`.env.example`](.env.example) |
| Contributing · Security · Credits | [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`SECURITY.md`](SECURITY.md) · [`docs/CREDITS.md`](docs/CREDITS.md) |

Bugs and questions: [GitHub Issues](https://github.com/sergezuber/FABULA-LLM-5/issues). Security reports: privately, per [SECURITY.md](SECURITY.md).

## Acknowledgements

Built on [MiMoCode](https://github.com/XiaomiMiMo/MiMo-Code) (an [OpenCode](https://opencode.ai) fork), [LM Studio](https://lmstudio.ai), [SearXNG](https://docs.searxng.org), [Playwright](https://playwright.dev), [Bun](https://bun.sh), piper and faster-whisper. Several supervision mechanisms were adapted from [pi](https://github.com/earendil-works/pi) (Mario Zechner, MIT). More: [`docs/CREDITS.md`](docs/CREDITS.md).

## License

FABULA's own code is MIT — see [LICENSE](LICENSE).

**Most of this repository is not FABULA's own code.** `engine/` is a vendored fork of [MiMoCode](https://github.com/XiaomiMiMo/MiMo-Code) (Xiaomi), itself a fork of OpenCode — MIT under its own copyright holders — and it ships **additional use restrictions** ([`engine/USE_RESTRICTIONS.md`](engine/USE_RESTRICTIONS.md): no military use, no malicious cyber activity, no autonomous high-risk action without human oversight, among others) that MIT does not cancel. Who holds what, the upstream revision, and how to verify the split: [**NOTICE.md**](NOTICE.md).
