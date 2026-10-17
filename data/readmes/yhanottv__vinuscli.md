<div align="center">

<br>

<img src="https://vinuscli.dev/banner.png" alt="VinusCLI" width="760" />

<br>
<br>

### The AI coding agent that lives in your terminal.

**One key. Every model. Your plan.**

Plan, write, refactor, debug and ship — without leaving the shell.

<br>

[![Node](https://img.shields.io/badge/Node-%E2%89%A5%2018-1E6B4F?style=flat-square&logo=nodedotjs&logoColor=white)](https://nodejs.org)
&nbsp;
[![Version](https://img.shields.io/badge/Version-2.3.0-1E6B4F?style=flat-square)](package.json)
&nbsp;
[![License](https://img.shields.io/badge/License-Proprietary-4B5563?style=flat-square)](LICENSE)
&nbsp;
[![Website](https://img.shields.io/badge/vinuscli.dev-1E6B4F?style=flat-square)](https://vinuscli.dev)

<br>

```
npm install -g vinuscli   →   vinus
```

</div>

<br>

---

## Why VinusCLI

A hands-on coding **agent**, not a chatbot. It reads and writes your files, runs
commands, previews every change as a diff, and improves itself by writing its own
skills — all in a fast, beautiful terminal UI.

One **Vinus key** unlocks every frontier model through a single hosted endpoint,
billed as a flat subscription with fair-use credits — **never per token**.

<br>

| | |
|---|---|
| 🧠 &nbsp;**Any model, one key** | GPT, Claude, Gemini, Llama, Mistral… one hosted endpoint, with an automatic fallback chain. |
| 🛠️ &nbsp;**Real tools** | Read/write files, run shell, `web_search`, `github_search`, `fetch_url`. |
| 🎚️ &nbsp;**Autonomy dial** | Plan · Manual · Auto — switch at any time. |
| 📚 &nbsp;**Smart skills** | 21 curated coding packs (debugging, TDD, GitHub, design, RE…), auto-suggested for the task at hand — and the agent writes its own so it never forgets. |
| 🔌 &nbsp;**Connectors** | GitHub, Canva, Notion, Linear, IDA Pro over MCP. |
| 🔍 &nbsp;**Reverse engineering** | First-class IDA Pro / Ghidra workflow. |
| 🖍️ &nbsp;**Visual diffs** | Green/red previews before anything touches disk. |
| 🎨 &nbsp;**Themes** | Aurora · Graphite · Phosphor · Ember. |

<br>

## What's new in 2.3.0

- **Skills that behave** — a curated 21-pack coding bundle; the right skill is suggested to the agent automatically for each request, and `/skills install` now pulls complete packs (scripts, references, templates).
- **Security hardening** — API keys are redacted from every output; shell access to credential stores (`~/.ssh`, config dirs…) is blocked.
- **Stability** — `/run` and `/shell` can no longer freeze the terminal; project memory survives `/clear` and auto-compact.
- **First test suite** — the guards above are covered by automated tests.

Full history: `/release-notes` inside the CLI.

<br>

## Get started

```bash
# 1 — install (requires Node.js ≥ 18)
npm install -g vinuscli

# 2 — launch
vinus

# 3 — sign in — opens your browser, creates a key automatically
/login        # → "1) Sign in with browser"

# 4 — just talk to it
Build me a REST API in Express with a health route and tests.
```

The agent creates files, runs your tests, and iterates — showing a diff before
each write.

<br>

## Plans

<div align="center">

| | **Free** | **Pro** | **Pro+** | **Ultra** |
|---|:---:|:---:|:---:|:---:|
| **Price** | €0 | €20 / mo | €100 / mo | €200 / mo |
| **Models** | Hosted free | + paid (Claude, GPT, Gemini…) | + top-tier | all frontier |
| **Included usage** | 40 msg / mo | Generous | Higher | ~4× Pro+ |
| **Credit top-ups** | — | ✓ | ✓ | ✓ |
| **Priority support** | — | — | ✓ | ✓ |

</div>

Manage your plan and keys at **[vinuscli.dev/dashboard](https://vinuscli.dev/dashboard)** — fair-use credits, never per-token billing.

<br>

## Operating modes

| Mode | Command | Behaviour |
|------|---------|-----------|
| ◇ &nbsp;**Plan** | `/plan` | Read-only. Investigates and returns a numbered plan — never writes or runs. |
| ◈ &nbsp;**Manual** | `/manual` | Acts, but asks your approval **every time**. |
| ◆ &nbsp;**Auto** | `/auto` | Full autonomy — pauses only when genuinely unsure. |

The current mode is always visible in the prompt.

<br>

## Skills & connectors

Skills are progressive-disclosure knowledge packs — light in the prompt, deep on
demand. Connectors plug external services in over MCP; their tools become the
agent's tools.

```bash
/skills              # list bundled skills, grouped by category
/skills install all  # pull the official set
/connect github      # OAuth in the browser → repos, PRs, issues
/mcp                 # add any MCP server
```

Built-in connectors: **GitHub · Canva · Notion · Linear · IDA Pro**.

<br>

## Commands

| Command | Description |
|---------|-------------|
| `/mode` · `/plan` · `/manual` · `/auto` | Set agent autonomy |
| `/model` · `/effort` | Choose model / thinking power (1–5) |
| `/theme` | Switch theme |
| `/skills` · `/connect` · `/mcp` | Skills, connectors, MCP servers |
| `/file` · `/run` · `/diff` · `/commit` | Load files, run shell, git |
| `/resume` · `/save` · `/sessions` | Session management |
| `/status` · `/cost` · `/usage` | Health, tokens, account |
| `/update` | Check for a new version on npm |
| `/help` | Everything |

<br>

## Configuration

Config lives in `~/.vinuscli/config.json`. Set values from inside the CLI:

```bash
/login
/config agent.mode auto
/effort
```

<br>

---

<div align="center">

Proprietary — © 2026 Yhano. All rights reserved. &nbsp;·&nbsp; The source is closed; the published package is a runnable build only.

<sub>Built for the terminal. Powered by Vinus.</sub>

</div>
