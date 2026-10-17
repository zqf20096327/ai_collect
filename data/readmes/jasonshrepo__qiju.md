# Qiju · 起居

<div align="center">
  <img src="https://raw.githubusercontent.com/jasonshrepo/qiju/main/assets/logo.svg" alt="Qiju logo" width="440">
</div>

<p align="center">
  <strong>Your coding agent forgot. Qiju kept the record.</strong>
</p>

<p align="center">
  Local-first, structured session records that let Claude Code, Codex, Kiro,
  Cursor, and future agents continue from verifiable development history.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11%2B-216C83.svg" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-475A60.svg" alt="Platform: macOS | Linux">
  <a href="LICENSE"><img src="https://img.shields.io/pypi/l/qiju.svg" alt="License: Apache-2.0"></a>
  <img src="https://img.shields.io/badge/status-developer%20preview-C8553D.svg" alt="Status: developer preview">
  <a href="https://discord.com/channels/1529020921518624950/1529020922734968884"><img src="https://img.shields.io/badge/discord-community-5865F2.svg" alt="Discord community"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a> ·
  <a href="#how-to-use">How to Use</a> ·
  <a href="#common-scenarios">Common Scenarios</a> ·
  <a href="docs/overview.md">In Depth</a> ·
  <a href="README.zh.md">中文</a>
</p>

Qiju is your secretary. You are the boss — you run the projects and make the
calls; say what's worth keeping: history, handoffs, where the docs live. Qiju
never copies what's already in your files — the code says what the project is;
Qiju records how it grew from nothing into something great. Ask later, and Qiju
remembers everything — no matter which agent you are using.

**What Qiju can do:**

- **One sentence becomes a record** — say "record the handoff" and a structured
  record (title, tags, next steps, the full story) is written for you.
- **Answers like it was there** — "what did we do yesterday?", "why didn't we
  use xyz?" — ask in plain words, get back the actual record, not a guess.
- **Memory across projects** — search this project, another project by name, or
  everything you have ever recorded; a feature you built last month is one
  question away from being reused.
- **Finds the gold** — `/qiju-review` turns last week's records into concrete
  improvements for the next round of development.

**The trait that matters most:** your records outlive everything — the session,
the compacted context window, even the agent vendor. They are plain local files
on your machine: no cloud, no embeddings, no lock-in.

**Across platforms:** one record store, every agent. Qiju installs the same
three skills into Claude Code, Codex, Kiro, and Cursor — record in one, ask in
another, and nothing is lost when you switch.

> [!NOTE]
> Curious about the design, the record format, the storage architecture, and the
> current status? Read [Qiju in depth](docs/overview.md).

## RAG, CAG, or Qiju?

RAG fetches context when you ask. CAG carries it in the prompt. Qiju keeps a
verifiable record of what happened across sessions, projects, and agents.

![Animated comparison of RAG, CAG, and Qiju session continuity](https://raw.githubusercontent.com/jasonshrepo/qiju/main/assets/qiju-rag-cag-animation-en.gif)

## Try the demo

Two minutes, nothing to install — a simulated session where **Claude Code**
writes the record and **Codex** picks it up:

**[▶ Play the interactive demo](https://claude.ai/code/artifact/4394e12e-677b-4ccf-af11-477e38c3e0e7)** ·
[中文版演示](https://claude.ai/code/artifact/4802c293-90e2-48d6-94c9-e6684d3eb1d6)

## Installation

```bash
uv tool install qiju
qiju --version
```

For pipx/pip installs and the source install, see
[Qiju in depth](docs/overview.md#install-alternatives-and-source-install).

## Start with project

Run `qiju init` from the root of each project you want to record:

```bash
cd /path/to/your/project
qiju init --host claude,codex,kiro
```

What it sets up, `--host all`, and user-level defaults: see
[Qiju in depth](docs/overview.md#what-qiju-init-sets-up).

## Update Qiju

```bash
uv tool upgrade qiju
```

Installed with pipx or pip? See
[Qiju in depth](docs/overview.md#install-alternatives-and-source-install).

## Update projects

The CLI upgrade does not rewrite the skill files already installed in your
projects. One command brings every registered project up to date:

```bash
qiju update --dry-run   # preview what would change
qiju update             # refresh skills in all registered projects
```

`qiju update` is registry-first. If you have older Qiju projects that were
initialized before the registry existed, run `qiju update --scan-projects` once
to discover them and backfill the registry. Your records are never touched by an
update — only the skill files are refreshed.

## How to use

### `/qiju-log` — tell it what to record

Say what you want kept, the way you would tell a person:

```text
/qiju-log handoff record
/qiju-log sum up our discussion
/qiju-log record that we will do xyz tomorrow
```

The agent turns your words into a structured record — title, tags, search terms,
next steps, and a full Markdown body — and verifies it landed in the store.

Records may also carry the exact `model` and `model_effort` used for the session. Add
those optional JSON fields, or pass `--model <exact-model>` and
`--model-effort <exact-effort>` to `qiju log`; command-line values override the JSON
body. Use only authoritative session values, omit unknowns, and never infer them from a
host name or prose.

> [!TIP]
> Treat Qiju as your secretary: just tell it what you want to record, and Qiju
> will do it for you.

### `/qiju-search` — just ask

Anything that was recorded, you can get back by asking:

```text
/qiju-search what did we do yesterday?
/qiju-search why did we use (or not use) xyz?
/qiju-search I remember we developed this feature in my project Y — what are the related files?
```

Search works within the current project, across a project named in your question,
or across all your projects; a record id (`qiju show '<uuid>:1'`) retrieves one
exact record.

For exact metadata retrieval, use `qiju search --model <exact-model>` or
`--model-effort <exact-effort>`. Text search includes present metadata, and
`--fields model,model_effort` returns the optional fields. An explicit metadata filter
does not match older records that omit that field.

> [!TIP]
> Qiju is your secretary — if it was recorded, just ask. You can even ask:
> `/qiju-search I want to build project X, it is about Y — what existing features
> in my projects can be reused?`

### `/qiju-review` — find the gold mine in your records

A powerful skill: it reads your recent project and global records, extracts the
mistakes, lessons, and repeated friction hiding in them, and proposes concrete
improvements to how you work next. It only recommends — it does not edit any
files unless you ask.

```text
/qiju-review read the last 7 days of records — anything we can optimize in the
following development?
```

## Common scenarios

The fastest way to get value from Qiju is to make two moments a habit: the end
of a session and the start of the next one.

| Moment | What you say to the agent |
| --- | --- |
| Ending a working session | `/qiju-log Record what we did today, what we decided, and what's next.` |
| Starting the next morning | `/qiju-search What did we do yesterday, and what's still pending?` |
| Switching agents mid-task | In Codex: `$qiju-search token refresh decision` — same record store, different host. |
| Before retrying something | `/qiju-search Did we already try caching the auth token? What happened?` |
| After a release | `/qiju-log Record: released 0.7.0 to PyPI, all gates green, skills refreshed in all projects.` |
| Recording a decision | `/qiju-log Record the decision: keep 0.5.9, monitor record quality; R1/R2 rejected.` |
| Weekly self-improvement | `/qiju-review What lessons from this week should change how we work?` |
| Following up on a recorded change | `I just updated skill X — check record <uuid>:1, then test skill X in this project.` |

## Contributing

Qiju is small on purpose, but the handoff problem is large. Useful contributions
include broken host workflows, real handoff cases, Linux verification, docs
clarity, and tests for record durability.

Try Qiju on one real coding session. Switch agents, search the record, and tell
us where the handoff still breaks — in an issue, or on
[Discord](https://discord.com/channels/1529020921518624950/1529020922734968884).

## License

Licensed under the [Apache License 2.0](LICENSE). Copyright 2026 Jason Shen.
