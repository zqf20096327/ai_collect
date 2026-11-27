<h1 align="center">PugPort: One for all agents</h1>

<p align="center">
  Your AI subscriptions and accounts in one chat. PugPort sends each task to an account with usage to spare, picks the model for the job, and hands the work off when an account hits its usage limit.
</p>

<p align="center">
  <a href="https://pugport.com">Website</a> ·
  <a href="https://pugport.dev">Dev log</a> ·
  <a href="docs/GETTING-STARTED.md">Getting started</a> ·
  <a href="docs/guides/README.md">User guides</a> ·
  <a href="docs/README.md">Docs</a>
</p>

<p align="center">
  <a href="https://github.com/pugport/pugport/actions/workflows/ci.yml"><img src="https://github.com/pugport/pugport/actions/workflows/ci.yml/badge.svg?branch=main&event=push" alt="Checks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0 license"></a>
</p>

https://github.com/user-attachments/assets/86c110f8-0bda-48bd-b11f-4cb3552e1a41

<p align="center"><sub>PugPort in two minutes (with music). Also on <a href="https://pugport.com/#film">pugport.com</a>.</sub></p>

## What it does

If you pay for more than one AI subscription, you end up as the scheduler: checking which account still has usage left, waiting for a limit window to reset, copying context from one tool to another. PugPort does that bookkeeping for you.

1. **Ask.** Describe what you need in one chat. Attach a folder only when the task needs your files.
2. **Route.** PugPort picks the account, model and reasoning effort from the task, how much usage each account has left and which limit windows reset soonest.
3. **Hand off.** If an account hits its usage limit mid-task, the work moves to one with usage left, along with a checked handoff note. An account you pick yourself is a preference: PugPort moves the task only if that account fails, for example at a usage limit. Routes you approve with “Suggest, then confirm” stay put.

PugPort starts the official command-line tools you've already installed and signed in to; it never proxies or imitates them. It never asks for or stores your passwords: CLIs keep their own sign-ins, and API keys you add stay on this computer. Chats, history and usage records stay in a local database on your computer; your tasks still go to the AI services you choose.

## Highlights

- **Real usage, never guessed.** Usage limit readings come from each service, with their source and time. Unknown stays unknown.
- **Smart routing you can override.** Let PugPort choose, switch to “Suggest, then confirm”, or pick the executor and model yourself. Routing advice comes from [Task Router](https://github.com/Waytrine/task-router), a 322M classifier fine-tuned for PugPort ([weights on Hugging Face](https://huggingface.co/Waytrine/task-router)).
- **Steer while it works.** Send a follow-up into a running task when the executor supports it, or edit, reorder and cancel queued messages.
- **A queue that survives restarts.** Deadlines and priorities persist. Separate chats run side by side; messages in one chat stay in order.
- **Agents ask each other.** Write “ask Codex to review it” and the running agent hands the subtask to that account, read-only by default, and gets the answer back.
- **Mention participants in chat.** Use `@` for roles and executors, `@@` for devices and bots, and `@@@` for remote servers connected over SSH. Add Muse (Meta's web chat) or Grok Bot to mention them with `@@`. Muse replies land in your chat; Grok Bot replies come back once you set up a Grok routine.
- **Work modes.** Switch a chat to Mods author to build and debug a Mod in it, or to Navigator to have a lead plan the work, hand it out and review it. See [work modes](docs/WORK-MODES.md).
- **Every run on record.** Output, tool calls, approvals and token use for every run, stored on your computer. Resume an interrupted task on the same executor, model and session.

Also included: the `pugport` terminal CLI, side chats, incognito chats, skills, MCP tools and local history search. Voice input and image search are optional components you install only if you want them. See the [user guides](docs/guides/README.md) and [all features](docs/FEATURES.md).

**Planned:** code-signed installers and a Linux desktop app.

## Supported executors

An executor is the CLI or API runtime that does the work.

| Executor | How PugPort runs it | Where usage comes from |
| --- | --- | --- |
| Claude Code | `stream-json` | Native usage and subscription profile, including model-specific windows |
| Codex CLI | App Server protocol | `account/rateLimits/read` |
| Grok CLI | ACP sessions with native steering | ACP `_x.ai/billing` |
| Cursor CLI | Native ACP with your Cursor sign-in | Model pools, credits and billing for verified accounts; manual fallback |
| API models via [Pi](https://github.com/earendil-works/pi) | RPC tool loop with isolated API keys | Usage ledger; balance where the provider reports it |

API models cover OpenAI, Anthropic, Google Gemini, DeepSeek, xAI, Kimi, GLM, Qwen, MiniMax, Mistral and OpenRouter, local Ollama and LM Studio, free tiers and custom endpoints, including Azure Responses. Add as many accounts of each executor as you have (CLI sign-ins or API keys); PugPort reads each account's usage separately.

## Quick start

**Download:** the [Windows installer and Mac app](https://pugport.com/#download) (version 0.0.39, with in-app updates), or build from source below.

You need at least one executor: Claude Code, Codex CLI, Grok CLI or Cursor CLI signed in, or an API key. Claude Code on Windows also needs Git for Windows.

**Windows** (Node.js 24.21+ and npm)

```powershell
git clone https://github.com/pugport/pugport.git
cd pugport
.\Setup-Windows.ps1    # local Node runtime, dependencies, tests and build
.\Start-PugPort.cmd    # open the desktop app
```

If PowerShell blocks the script, read it first, then run `powershell -ExecutionPolicy Bypass -File .\Setup-Windows.ps1`; this applies to that one run only.

**macOS** (native Node.js 24+ and Git; local validation, see [Mac status](docs/MAC-PORT.md))

```sh
git clone https://github.com/pugport/pugport.git
cd pugport
bash launchers/setup-macos.sh
bash launchers/start-macos.command
```

Closing the window keeps PugPort in the tray so queued work keeps running; choose **Quit PugPort** from the tray to exit. [Getting started](docs/GETTING-STARTED.md) covers optional components, where your data lives and review builds.

## Status

Early development. Version 0.0.39 runs on Windows x64 and Apple silicon Macs, with in-app updates; download it from [pugport.com](https://pugport.com/#download). The Windows installer is not code-signed yet and the Mac app is not notarized yet, so each system asks you to confirm the first launch; Windows also builds a portable ZIP for review builds. The Mac release is an Apple Silicon (arm64) build that is ad-hoc signed and updates itself from the signed feed; Intel Mac acceptance has not been performed. Release instructions are in [Windows releases](docs/RELEASING-WINDOWS.md) and [Mac releases](docs/RELEASING-MAC.md); release notes are on the [dev log](https://pugport.dev); see also [platform support](docs/PLATFORMS.md). PugPort was called ComboRunner until October 2026; existing data, settings and chats carry over.

## Websites

| Site | What it's for |
| --- | --- |
| [pugport.com](https://pugport.com) | The product site: what PugPort does, the live routing demo, and downloads for Windows and Mac. |
| [pugport.dev](https://pugport.dev) | The dev log: build notes, release write-ups and the reasons behind design decisions. |
| [pugport.org](https://pugport.org) | Community and learning: step-by-step explainers of how agents and PugPort work, how to contribute, and a map of everyone who has helped. |

## Documentation

- [User guides](docs/guides/README.md): [getting started](docs/guides/getting-started.md), [chat and mentions](docs/guides/chat-and-mentions.md), [routing](docs/guides/routing.md), [terminal (`pugport`)](docs/guides/terminal.md), [remote servers and devices](docs/guides/remote-servers-and-devices.md), [inbox and notices](docs/guides/inbox-and-notices.md), [desktop and tray](docs/guides/desktop-and-tray.md), [permissions and safety](docs/guides/permissions-and-safety.md)
- [Getting started](docs/GETTING-STARTED.md): setup, optional components, where data lives, review builds
- [Mods author guide](docs/MODS.md): package format, API, v1 compatibility and a working v2 web example
- [All features](docs/FEATURES.md)
- [Hindsight memory pilot](docs/HINDSIGHT.md): optional setup and limits
- [Contributing](.github/CONTRIBUTING.md)
- [Dev log](https://pugport.dev): release notes and build notes
- [All documents](docs/README.md)

## Development

TypeScript, React, Electron, Express and SQLite. Tests use mocked protocols only and never send real model requests.

```powershell
$env:PATH = (Join-Path (Get-Location) '.runtime') + ';' + $env:PATH   # this checkout's private Node 24
npm.cmd run typecheck
npm.cmd test              # or npm.cmd run test:ci for at most two test files at a time
npm.cmd run format:check
npm.cmd run i18n:check
npm.cmd run build
npm.cmd run desktop
```

On macOS, skip the `PATH` line and use `npm` with native Node 24. Read [AGENTS.md](AGENTS.md) and [contributing](.github/CONTRIBUTING.md) before your first pull request. By opening a pull request you agree to the [Contributor License Agreement](docs/CLA.md); the PR template has a checkbox for it. Issues labeled `good first issue` are a good place to start.

Ideas and bug reports are welcome in English or Chinese: [open an issue](https://github.com/pugport/pugport/issues/new/choose); no development setup needed. Contributors can use their own tools. Larger PRs get a review-size reminder, not a hard line limit.

## Acknowledgements

PugPort builds on [Pi](https://github.com/earendil-works/pi), the agent runtime behind API models, and on [MarkItDown](https://github.com/microsoft/markitdown), [ripgrep](https://github.com/BurntSushi/ripgrep), [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx), [ONNX Runtime](https://github.com/microsoft/onnxruntime), [sharp](https://github.com/lovell/sharp), [OpenCV](https://opencv.org) and more. Its account-health and routing design took ideas from [Magpie](https://github.com/yetone/magpie). [Acknowledgements](docs/ACKNOWLEDGEMENTS.md) lists the main projects, models and fonts with their licenses; [third-party notices](THIRD_PARTY_NOTICES.md) has the full attribution.

Built by [Yutong Wang](https://yutong.wiki).

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). Third-party components keep their own licenses.

PugPort is an independent project and isn't affiliated with Anthropic, OpenAI, xAI, Google, Meta or Anysphere. You're responsible for using each service within its terms.
