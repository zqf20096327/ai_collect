<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/brand/continuity-logo-dark.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset=".github/brand/continuity-logo.svg">
    <img src=".github/brand/continuity-motion.gif" alt="Continuity" width="560">
  </picture>
</p>

# Continuity

**[中文](README.zh-CN.md)** | English

Continuity gives AI coding agents a shared handoff. A new session can read what you asked for,
where work stopped, what passed its last check, and what to do next. Claude Code, Codex, Cursor
and other tools can open the same project folder.

The handoff lives in Markdown under `docs/state/`, alongside the project's verification records.
The core tool runs on Python 3.9 or newer using only its standard library. Unzip the release into an empty folder,
open it in your agent and say “Read AGENTS.md and start.” [Download the latest release](https://github.com/yourhoneypomelo-cell/Continuity/releases/latest)

## Why

AI agents lose track of long projects. They forget requirements, re-do finished work, propose
features the user already rejected, and claim tasks are done without proof. The next agent can
look up recorded requirements and decisions, inspect the last verification, and rerun the
product check when its evidence is out of date.

### What it is for

- **Long projects that span many sessions.** The agent re-reads the goal, the current task, the
  exact stop point and the next step before touching any code — not just a summary it wrote itself.
- **Context compaction.** After a host shortens a conversation, the agent can recover saved
  requirements, prohibitions and decisions from disk. With chat import enabled on a supported
  host, `ws reconcile` lists captured user messages that still need an entry or an explanation.
- **Switching windows or tools.** Point the next agent at the same project. The handoff card gives
  it the stop point and next action. The evidence files show which product checks ran. Transcript
  capture and automatic startup vary by host. [Host guide](.agents/guides/HOSTS.md)
- **Changing requirements.** Every requirement has a permanent ID. Replacing one lists the open
  tasks and features that cite it, so the follow-up work is updated instead of silently building
  the old behavior. Removed features stay visible with their reason, so they are not re-proposed.
- **Proof of completion.** Each task carries its own acceptance command. `ws verify` runs it,
  stores the output, and marks the task done only when it passed — zero tests, skipped tests and
  stale evidence are all reported, never silently accepted.
- **Parallel agent windows.** Sessions claim tasks by file path and resource name; overlapping
  claims are refused. A taken-over window cannot keep writing, and the workspace lock is a system
  file lock that ends with the process holding it.
- **Credentials.** You decide once whether credentials are kept as written in files you name,
  or kept out of files; until then the agent asks. Everything else the tool writes, chat
  transcripts included, is redacted.

A handoff shows adopted decisions ahead of an older next step. For a delivery, the agent can bind
the approved file to a receipt and compare it with the file about to ship. A stopped batch can
leave its last passing check and its remaining work in the same brief. [Examples](.agents/guides/QUICKSTART.md)

## Architecture

Every agent tool loads one root contract, `AGENTS.md`, through a thin adapter. The agent runs
`ws.py` to record and verify; the tool reads and writes the Markdown files under `docs/`. At the
next session the agent re-reads those files, so the memory survives windows, compaction and tool
switches.

```mermaid
flowchart TB
    subgraph H[" "]
        direction LR
        CLAUDE["Claude Code"]
        CODEX["Codex"]
        CURSOR["Cursor"]
        KIMI["Kimi Code"]
        KIRO["Kiro"]
        DSH["DeepSeek Harness"]
        MORE["Qwen · Grok ·<br/>CodeBuddy · Gemini…"]
    end

    AGENTS["AGENTS.md<br/>the root contract"]
    ADAPTERS["Thin adapters<br/>CLAUDE.md · .gemini/settings.json<br/>.kiro/steering/workspace.md"]
    WS["ws.py<br/>validate · assign IDs · verify · checkpoint"]

    subgraph S[" "]
        direction LR
        HANDOFF["HANDOFF<br/>stop · next"]
        REQ["REQUIREMENTS"]
        PREF["PREFERENCES"]
        FEAT["FEATURES"]
        TASKS["TASKS"]
        ARCH["ARCHITECTURE"]
        DESIGN["DESIGN<br/>decisions"]
    end

    REST["logs/ · chats/ · archive/<br/>history · transcripts · evidence · checkpoints"]

    H -->|loads| AGENTS
    AGENTS -.->|loaded through| ADAPTERS
    AGENTS -->|protocol| WS
    WS <-->|read · write · verify| S
    WS -->|append · capture · seal| REST
    S -->|re-read at start| H
```

Top to bottom: the **agent tools**, the shared **`AGENTS.md` contract** with its thin adapters,
the **`ws.py` tool**, and the **`docs/` memory** — the current facts in `state/` plus the
`logs/`, `chats/` and `archive/` history. The loop closes when the state files are re-read at
the start of the next session.

## Repository layout

```text
Continuity/
├── AGENTS.md                     the root contract every agent reads first
├── CLAUDE.md                     Claude Code adapter: the line "@AGENTS.md"
├── CODEBUDDY.md                  CodeBuddy / WorkBuddy adapter
├── DESIGN.md                     why the structure is the way it is
├── README.md · README.zh-CN.md   this file, in English and Chinese
├── LICENSE                       MIT
├── .gemini/settings.json         Gemini CLI / Antigravity adapter
├── .kiro/steering/workspace.md   Kiro adapter
├── .trae/rules/workspace.md      Trae adapter
├── .agents/                      system files, identical in every project
│   ├── guides/                   QUICKSTART · PROTOCOL · STRUCTURE · HOSTS
│   ├── skills/                   workflows loaded on demand
│   ├── template/                 spec & trial templates, test-result parsers
│   │   ├── spec/                 requirements.md · design.md · tasks.md
│   │   └── examples/             unittest_json · pytest_junit · go_json
│   └── tools/                    the CLI
│       ├── ws.py                 the tool every agent runs
│       ├── ws / ws.cmd           launchers that find python3 or python
│       ├── wslib/                its modules (core, locks, permits, evidence, …)
│       └── tests/                the template's self-tests (not installed)
├── docs/                         the project's memory — created in each project
│   ├── state/                    current facts, read at every session start
│   │   ├── HANDOFF.md            stop point · next step · ownership
│   │   ├── REQUIREMENTS.md       what the user wants, with acceptance
│   │   ├── PREFERENCES.md        stable user preferences
│   │   ├── FEATURES.md           current and retired capabilities
│   │   ├── TASKS.md              work items · acceptance · evidence
│   │   ├── ARCHITECTURE.md       entry points · commands · environment
│   │   └── DESIGN.md             decisions · rejected options
│   ├── logs/                     history tables written by the tool
│   ├── chats/                    transcripts from hooks, and from host stores once you agree
│   ├── archive/                  checks/ · checkpoints/ · closed/ · snapshots/
│   └── specs/<slug>/             detail for one large requirement
└── dist/                         release zips (attached to GitHub Releases)
```

Installing the template into a project writes only the runtime files: the adapters, the guides,
skills and templates, `ws.py` and its modules, and the generated `docs/` skeleton. The maintainer
files — `MAINTAINING.md`, `DESIGN_REQUIREMENTS.md`, `FIXES.md`, the self-tests, the folder previews — stay in
this repository and are never copied into a project, so a business agent's search never finds the
template's own history.

## Quick start

1. **Download** the latest release ZIP from
   [Releases](https://github.com/yourhoneypomelo-cell/Continuity/releases)
   and unzip it into an empty project folder.

2. **Open the project** in your agent tool and say:

   > Read AGENTS.md and start.

3. **State your goal** in one sentence when the agent asks. It records the goal and creates the
   state files. It also asks once whether chats from the AI tools on this machine may be copied
   into `docs/chats/`; chats from before that moment stay out. In a git project it asks whether
   git should ignore `docs/chats/`.

4. **Optional: enable hooks** so the tool saves chat transcripts and injects the workspace brief
   at session start:

   ```bash
   .agents/tools/ws hooks enable claude
   ```

   Replace `claude` with `codex`, `cursor`, `gemini`, `copilot`, `kiro`, `grok`, `qwen`, or
   `codebuddy` for your tool.

## How it works

```text
Session start:  brief → read state → start → work and record → verify → checkpoint
Next session:     ↑                                                              |
                  └──────────────────────────────────────────────────────────────┘
```

- **AGENTS.md** is the root contract every agent reads. It defines the session protocol, the
  state file format, and the rules that keep the workspace consistent.
- **`docs/state/`** holds seven Markdown files: the handoff card, requirements, preferences,
  features, tasks, architecture, and design decisions. These are the source of truth.
- **`docs/logs/`** records what happened: session history, requirement changes, feature changes.
- **`docs/chats/`** holds chat transcripts copied by the hooks, and, once you agree at the start,
  this project's chats from the AI tools on this machine. Chats from before the workspace was
  set up are not imported.
- **`ws.py`** is the CLI tool that validates writes, assigns IDs, runs acceptance tests, and seals
  checkpoints. It is the only thing the agent needs to run.

## Key features

- **Record first, act second.** Every user message is checked for new requirements, decisions
  and preferences before any work begins.
- **Verified completion.** A task is done only when its acceptance command passes in the current
  session. The tool runs the test, stores the evidence, and marks it done.
- **Parallel sessions.** Multiple agent windows can work on the same project. Task claims use
  file paths and resource names to prevent conflicts. The workspace lock ends with the process
  that holds it, so a crashed window never leaves it behind.
- **Credential safety.** The tool asks how the project handles credentials (kept as written in
  files you name, or kept out of files) and redacts them everywhere else it writes.
- **Host adapters.** AGENTS.md is the single contract. Adapters for Claude Code, Codex, Cursor,
  Gemini, Kiro, Kimi Code, Grok, DeepSeek Harness, CodeBuddy and Qwen Code load it natively.
- **Compaction survival.** State files are on disk, not in the agent's context window. After
  compaction, the agent re-reads them and continues.

## Install into an existing project

```bash
# From the template folder:
python .agents/tools/ws.py install --target /path/to/your/project --merge

# Or unzip a release into the project root.
```

`--merge` preserves your existing AGENTS.md by appending it under "Project rules".

## Design

[DESIGN.md](DESIGN.md) explains the reasoning behind the structure: why files instead of a
database, why record-before-act, how evidence works, and which alternatives were rejected.

## Guides

| Guide | Use |
| --- | --- |
| [Quickstart](.agents/guides/QUICKSTART.md) | Installation, first session, daily use |
| [Protocol](.agents/guides/PROTOCOL.md) | Formats, ownership, evidence and recovery |
| [Structure](.agents/guides/STRUCTURE.md) | Folders, naming, document size and writing style |
| [Hosts](.agents/guides/HOSTS.md) | Per-tool entry files and hooks |

## Requirements

**Runtime**

- **Python 3.9** or newer on the PATH as `python3` or `python` (macOS often has only `python3`). No
  packages to install — the tool uses only the standard library. Prefer `.agents/tools/ws` (or
  `.\.agents\tools\ws.cmd` on Windows) so you need not name the interpreter.
- Windows, macOS or Linux. Windows notes (Git Bash vs PowerShell, UTF-8, hook commands) are in
  [HOSTS.md](.agents/guides/HOSTS.md).
- The agent needs file access to read `AGENTS.md` and shell access to run the workspace checks.
- Git is recommended for the project, but not required. The workspace itself never runs git.

**Host integration (optional)**

- Without hooks the workspace still works; the agent just runs `ws brief` itself. Hooks automate
  transcript capture and the session-start brief. One command sets them up per tool:
  `.agents/tools/ws hooks enable <host>` for `claude`, `codex`, `cursor`, `gemini`,
  `copilot`, `antigravity`, `kiro`, `codebuddy`, `qoder`, `qwen` or `grok`.
- Some hosts ask you to trust the project or its hooks first (Codex `/hooks`, Qwen Code, Kiro,
  Qoder, WorkBuddy). [HOSTS.md](.agents/guides/HOSTS.md) lists the entry file and the trust step
  for each one.
- Importing DeepSeek Harness session history needs **Python 3.14+** or the `backports.zstd`
  package, because its store is zstd-compressed. Everything else works on **Python 3.9**.

**Disk**

The template is under 1 MB. A project's `docs/` grows with its history and chat transcripts;
`ws compact` archives closed rows and `ws check` warns before files get too large for a host to
read.

The [quality review of 70 owner requirements](.github/reviews/2026-11-18-requirements.zh-CN.md)
records which behaviors were exercised and which handoffs still need a trial with two independent tools.

## License

[MIT](LICENSE)
