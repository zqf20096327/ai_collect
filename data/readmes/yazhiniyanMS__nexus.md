<h1 align="center">NEXUS</h1>

<p align="center"><b>Understand a codebase on your own machine — then change it only through you.</b></p>

<p align="center">
An open-source desktop workspace for macOS, Windows and Linux. It maps any local project without AI,<br>
and lets AI agents propose changes in an isolated copy that reach your files only after you approve the diff.
</p>

<p align="center">
<a href="https://yazhiniyanms.github.io/nexus/">Website</a> ·
<a href="https://github.com/yazhiniyanMS/nexus/releases">Download</a> ·
<a href="docs/GETTING_STARTED.md">Get started</a> ·
<a href="docs/README.md">Documentation</a> ·
<a href="docs/ROADMAP.md">Roadmap</a> ·
<a href="https://github.com/yazhiniyanMS/nexus/issues/new/choose">Report a problem</a>
</p>

<p align="center">
<a href="https://github.com/yazhiniyanMS/nexus/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/yazhiniyanMS/nexus?include_prereleases&label=release"></a>
<a href="https://github.com/yazhiniyanMS/nexus/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/yazhiniyanMS/nexus/actions/workflows/ci.yml/badge.svg"></a>
<a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-blue"></a>
</p>

<p align="center"><img src="docs/assets/demo/nexus-tour.gif" alt="A tour of NEXUS: welcome, project overview, architecture map, codebase report, Git diff, a task waiting for approval, execution settings and agents" width="900"></p>
<p align="center"><sub>Real screenshots of NEXUS analysing its own repository. <b><a href="https://yazhiniyanms.github.io/nexus/#demo">Watch the 50-second screen recording</a></b>.</sub></p>

---

## Why NEXUS

Most AI coding tools start with the agent. NEXUS starts with **understanding**, and puts every change behind your approval.

- **See the shape of a codebase in seconds, with no AI and no API key.** Modules and the imports between them, dependency cycles, the most-imported files, symbols and references, search across all your projects.
- **Share it without sharing the code.** One click makes a self-contained HTML report — architecture graph, hotspots, dependencies, findings — with file paths and names but no source code. [See a real one](docs/assets/demo/nexus-report.html) (download it and open it in a browser). The map also copies as a Mermaid diagram that GitHub renders in READMEs and issues, and Model Lab results copy as a Markdown table — names and numbers, never code or prompts.
- **Agents that ask first.** An agent researches, plans, writes in a separate Git worktree, runs tests and reviews its own diff. You approve the plan, each command and the final diff; nothing touches your files before that. Commands can run sandboxed, and credentials in the files an agent edits are sent to the model as placeholders.
- **Your models, measured on your hardware.** Use Ollama, llama.cpp, LM Studio or any OpenAI-compatible server locally, or Anthropic and OpenAI. Model Lab benchmarks them side by side on your machine.
- **A real workspace around it.** Git status, diffs, staging and commits; your own shell in tabs and splits; approval-gated task lists.

NEXUS is **not an editor**. Keep writing code in VS Code, Zed or your IDE; use NEXUS to understand a project, review what changed and run controlled AI work on it. How it compares with Claude Code, Cursor, Aider and others: [docs/COMPARISON.md](docs/COMPARISON.md).

## Screenshots

| | |
| --- | --- |
| ![Overview of a project](docs/assets/screenshots/overview.png) **Overview** — repository state, findings and recent work for one project. | ![Architecture map](docs/assets/screenshots/architecture-map.png) **Architecture map** — modules, imports and cycles, built from the code index. |
| ![Codebase report](docs/assets/screenshots/report.png) **Codebase report** — a shareable HTML file with no source code in it. | ![Git](docs/assets/screenshots/git.png) **Git** — changes, diffs, staging and commits. |
| ![Task waiting for approval](docs/assets/screenshots/tasks.png) **Tasks** — every command waits for approval and says how it will run. | ![Execution settings](docs/assets/screenshots/execution-settings.png) **Execution** — Trusted, Restricted (sandboxed) or Isolated, described as enforced on your machine. |

## Install

**[Download NEXUS 0.2.1 for Mac (Apple Silicon)](https://github.com/yazhiniyanMS/nexus/releases/latest/download/NEXUS_0.2.1_aarch64.dmg)** · [all downloads](https://github.com/yazhiniyanMS/nexus/releases/latest). Each release has `SHA256SUMS.txt` to check the download against.

| System | File | Status |
| --- | --- | --- |
| macOS, Apple Silicon | `NEXUS_<version>_aarch64.dmg` | Reference platform, used daily |
| macOS, Intel | `NEXUS_<version>_x64.dmg` | Built and launch-checked under Rosetta; not run on an Intel Mac |
| Windows 10/11 x64 | `NEXUS_<version>_x64-setup.exe` or `.msi` | Built, installed and launch-checked in CI; little hands-on use |
| Linux x64 (Ubuntu 22.04+) | `.deb`, `.rpm` or `.AppImage` | Built, installed and launch-checked in CI; little hands-on use |

The beta installers are **not code-signed**. On macOS, open NEXUS once (macOS blocks it), then go to **System Settings → Privacy & Security**, click **Open Anyway** and confirm — right-click → Open no longer works since macOS 15; on Windows choose **More info → Run anyway**. Step-by-step instructions, requirements and uninstalling: [docs/INSTALLATION.md](docs/INSTALLATION.md).


## Try it in five minutes

1. **Install and open NEXUS.** The first-run guide explains what it does and asks for a project.
2. **Choose a folder with code in it.** NEXUS reads it (it never moves or changes your files) and builds an index of its symbols and imports — a few seconds for most projects.
3. **Open Intelligence → Map** to see the architecture, or **Overview → Share a report** to save the codebase report.
4. **Optional: connect a model.** If Ollama is installed, the guide can start and connect it; otherwise add a connection in **Settings → Model connections**.
5. **Optional: give an agent a small task** in **Agents**, and approve or reject each step.

More: [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md).

## Model providers

| Provider | Where it runs | Key needed |
| --- | --- | --- |
| Ollama | This computer | No |
| llama.cpp server | This computer | No |
| LM Studio and other OpenAI-compatible servers | This computer or your server | Optional |
| Anthropic | Anthropic's API | Yes |
| OpenAI | OpenAI's API | Yes |

API keys are kept in the macOS Keychain, Windows Credential Manager or the Linux Secret Service, never in a file. Before project content goes to a model that is not on your computer, NEXUS asks you to confirm it for that request. Setup: [docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## What works today

| Area | Status | Notes |
| --- | --- | --- |
| Projects, analysis, findings | Available | Languages, frameworks, dependencies (npm, Cargo, pip, Go), possible secrets, large files, missing tests/README/CI |
| Intelligence: map, symbols, references, docs | Available | Rust, TypeScript, JavaScript, Python, Go. Line-based extraction, not a full parser |
| Codebase report | Available | HTML, no source code; the map also copies as Mermaid |
| Ask about the code | Available, needs a model | Answers cite the files and lines they used |
| Search | Available | Text or regex across every project, respects `.gitignore` |
| Git | Available | Status, diffs, history, branches, stage, unstage, commit. No push, pull or branch switching |
| Terminal | Available | Your shell in real pseudo-terminals; tabs, splits, saved output, search |
| Tasks | Available | Step lists; every command needs approval |
| Agents | Experimental, needs a model | Research → plan → implement → test → review in an isolated worktree, approvals at each gate |
| Model Lab | Experimental | Runtimes, library, downloads you start, playground, benchmarks, comparison |

Known limits are listed in [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Privacy and security

- **Local-first.** No account, no telemetry, no analytics, no update checks. Your projects, index and history live in a folder on your computer. [What can leave your machine, and when](docs/PRIVACY.md).
- **Nothing runs without approval**, and approval is not presented as a sandbox. Each command runs at a level you choose — Trusted (as you), Restricted (sandboxed: writes only to the project, temp and caches; credential folders, NEXUS's data and the keychain hidden) or Isolated (Restricted without network) — using the macOS sandbox or bubblewrap on Linux. Windows currently offers Trusted only.
- **The webview cannot touch files or start programs**; it calls typed commands in the Rust core, which checks every path.
- Audits, threat model and known residual risks: [docs/audit/](docs/audit/). Report a vulnerability: [SECURITY.md](SECURITY.md).

## How it is built

A [Tauri 2](https://tauri.app) app: a Rust core (SQLite, Git, pseudo-terminals, process sandboxing, the code index and the agent engine) and a React 19 + TypeScript interface. No server and no bundled AI.

```
src/                 React UI — lib/api.ts is the only place that calls the core
src-tauri/src/       Rust core, one module per feature
  intel/             code index, graphs, codebase report
  agents/            agent pipeline, roles and permissions, isolated workspaces
  exec/              execution levels, environment policy, sandbox backends
  lab/               Model Lab: runtimes, downloads, inference, benchmarks
  platform/          everything that differs between macOS, Windows and Linux
```

Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Roadmap

Now: 0.2.1 is out; next, hands-on checks on Windows and Linux, fixes from the first users, and signed installers. Later: a Windows sandbox backend, incremental indexing, more languages in the index. The full list, and what is deliberately out of scope: [docs/ROADMAP.md](docs/ROADMAP.md).

## Feedback

Everything goes through public GitHub issues — no external forms and no tracking:
[it did not install](https://github.com/yazhiniyanMS/nexus/issues/new?template=installation_problem.yml) ·
[how it runs on my system](https://github.com/yazhiniyanMS/nexus/issues/new?template=platform_report.yml) ·
[something is broken](https://github.com/yazhiniyanMS/nexus/issues/new?template=bug_report.yml) ·
[something was confusing](https://github.com/yazhiniyanMS/nexus/issues/new?template=ux_feedback.yml) ·
[I need a feature](https://github.com/yazhiniyanMS/nexus/issues/new?template=feature_request.yml).
Reports from Windows and Linux are the most useful thing you can send right now.

## Contributing

Bug reports, platform testing (especially Windows and Linux) and pull requests are welcome. Start with [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) — it covers setup, the checks to run, and how the codebase is organised. Please follow the [code of conduct](CODE_OF_CONDUCT.md).

## Licence

[MIT](LICENSE).
