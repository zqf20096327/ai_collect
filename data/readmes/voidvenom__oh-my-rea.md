<div align="center">

# omr

**An evidence-first reverse-engineering agent for your terminal, powered by [REA](https://github.com/morluto/rea).**

[![npm](https://img.shields.io/npm/v/oh-my-rea?color=cb3837&logo=npm)](https://www.npmjs.com/package/oh-my-rea)
[![CI](https://github.com/voidvenom/oh-my-rea/actions/workflows/ci.yml/badge.svg)](https://github.com/voidvenom/oh-my-rea/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-%5E22.23.4%20%7C%7C%20%5E24.22.1%20%7C%7C%20%3E%3D26.12.1-339933?logo=node.js&logoColor=white)](package.json)

[Quick start](#quick-start) · [Examples](#examples) · [Models](#models) · [Commands](#commands) · [Reference](docs/REFERENCE.md)

</div>

---

Point `omr` at an app, binary, firmware image, or website and ask a question. It investigates with REA's analysis tools and answers with citations to the Evidence it actually retained, so every claim can be traced back to something it observed.

It works like the terminal coding agents you may already use (Claude Code, Codex, opencode), but built for reverse engineering and security work.

## Quick start

```bash
npm install --global oh-my-rea
omr
```

omr needs REA. If it is not installed, the first run explains why and asks before running `npm install --global rea-agents`. Nothing is installed without a "yes".

Then set a model. Either export a key that omr recognizes (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, ...) or write `~/.config/rea/omr-model.json` as shown in [Models](#models).

## Examples

```bash
omr                                          # interactive TUI in the current directory
omr app.apk                                  # open a target in the TUI
omr app.apk "which API endpoints does this app call, and how are requests signed?"
omr --profile android app.apk                  # pre-load Android tooling and prompts
omr /status                                  # one-shot command, no model needed
omr --json app.apk "find the license check"  # machine-readable events for scripts and CI
```

## Features

- **Evidence first.** Findings cite retained Evidence IDs (`ev_…`). Open questions go to an Unknown ledger instead of being guessed.
- **REA's full toolset.** Native, Android, Electron/JavaScript, browser, firmware and network analysis through REA, with one session journal for both your commands and the model's.
- **Any model.** 33 built-in providers (OpenAI, Anthropic, Gemini, OpenRouter, DeepSeek and more) plus local servers (Ollama, LM Studio, vLLM, llama.cpp, LocalAI) and any OpenAI-compatible endpoint. Switch live with `/model`.
- **Guided workflows.** Slash commands such as `/triage`, `/investigate`, `/crypto`, `/frida`, `/masvs`, `/firmware` and `/ioc` run structured playbooks instead of a blank prompt.
- **Subagents.** Spawn background workers, view the task graph, steer them mid-run.
- **Safe to interrupt.** The conversation is checkpointed after every step. `omr --resume` continues an interrupted turn.
- **Scriptable.** `--json` event stream, stable exit codes, and an embeddable SDK (`oh-my-rea/sdk`).
- **Accurate context accounting.** Context windows come from the provider or [models.dev](https://models.dev), never from a guess. If a window is unknown, omr says so.

## How it works

```
you ──▶ omr ──▶ model (any provider)
          │
          └────▶ REA (MCP) ──▶ analysis providers, Evidence ledger, session journal
```

omr runs the agent loop (prompting, streaming, tool routing, compaction, reports). REA owns the facts. Every tool call goes through REA, so the journal covers what you ran and what the model ran.

## Models

Zero-config works if a supported key is exported in your shell. For a custom endpoint, create `~/.config/rea/omr-model.json`:

```json
{
  "base_url": "https://your-endpoint/v1",
  "model": "your-model-id",
  "api_key_env": "YOUR_API_KEY_ENV"
}
```

`api_key_env` names the environment variable that holds the key, so the key itself stays out of the file. Add `"context_window": 1000000` if your endpoint does not report its window. See the [reference](docs/REFERENCE.md#model-configuration) for failover chains, token budgets, reasoning effort and every environment variable.

## Commands

Type `/` in the TUI for the full palette, or run `omr --help`. A few to start with:

| Command | What it does |
| --- | --- |
| `/open <path>` | Bind a target (binary, APK, bundle, archive) |
| `/triage` | Fast reconnaissance: format, protections, entry points |
| `/investigate <goal>` | Bounded, Evidence-backed investigation |
| `/explain <symbol\|addr>` | Decompile and explain a function |
| `/find <query>` | Zero-token search of classes, strings and procedures |
| `/evidence`, `/unknowns` | Inspect the Evidence and Unknown ledgers |
| `/report` | View or export the session report |
| `/model`, `/effort` | Switch model or reasoning effort |
| `/resume`, `/fork`, `/rewind` | Manage sessions |
| `/doctor` | Check REA providers and configuration |

Profiles (`--profile recon|malware|vuln|crypto|frida|android|firmware|web`) pre-load the right tools and prompts for a kind of task.

## Keeping up to date

```bash
omr update      # update omr and REA to the latest npm release
omr setup       # re-check the environment
```

omr checks the registry at most once a day and prints a one-line notice. Disable it with `OMR_NO_UPDATE_CHECK=1`.

## Requirements

- Node.js `^22.23.4`, `^24.22.1` or `>=26.12.1` (REA's requirement)
- [REA](https://github.com/morluto/rea) (`rea-agents`), installed for you on first run
- Linux is the primary platform. Some REA analysis providers (Ghidra, JADX, Frida and others) need their own tools. Run `rea doctor` to see what is available.

## Development

```bash
git clone https://github.com/voidvenom/oh-my-rea.git
cd oh-my-rea
npm install
npm run build
npm test
node bin/omr.js --help
```

When omr runs next to a REA checkout, it uses that checkout. Override with `OMR_REA_COMMAND`.

## Responsible use

omr is a dual-use security tool. Analyze only software, devices and services that you own or are explicitly authorized to test. You are responsible for staying within scope and within the law. Content that omr reads from a target is treated as data, never as instructions.

## Documentation

- [Reference](docs/REFERENCE.md): configuration, all commands, tools, session layout, SDK
- [REA](https://github.com/morluto/rea): the analysis engine omr is built on

## License

[MIT](LICENSE)
