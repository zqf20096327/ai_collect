<div align="center">

<img src="docs/banner.svg" alt="omp-skill — give any AI agent a real coding body" width="880">

# omp-skill

**Teach your AI agent to drive [omp](https://omp.sh) — the terminal coding agent with LSP code intelligence, live debugging, plan mode and subagents.**

One skill. Any agent. No context shuttling.

[Install](#-install) · [What your agent learns](#-what-your-agent-learns) · [30-second demo](#-30-second-demo) · [Compatibility](#-compatibility)

**English** · [Русский](README.ru.md) · [Deutsch](README.de.md) · [中文](README.zh.md)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![verified](https://img.shields.io/badge/verified%20on-omp%2018.1.18-brightgreen.svg)](references/cli-reference.md)
[![skill format](https://img.shields.io/badge/format-SKILL.md-purple.svg)](SKILL.md)

</div>

---

## 🧠 The problem this solves

Your chat agent writes a decent patch. Then reality hits:

| Without omp-skill | With omp-skill |
|---|---|
| "Rename this function" → regex horror across 14 files | **Semantic rename via LSP** — same-named symbols distinguished, imports updated |
| "Why does it hang?" → guesses and print-statements | **Attaches a real DAP debugger** — breakpoints, stack traces, live locals |
| One model, one slow pass | **Parallel subagents** — scout, reviewer, security-reviewer fan out |
| Agent forgets everything between messages | **Resumable omp sessions** — project knowledge accumulates and continues with `omp -c` |
| Risky big-bang edits | **Plan mode first**, review the plan, then implement |

[omp](https://omp.sh) already has all of this. Your agent just doesn't know the headless patterns to drive it — `-p` one-shots, session continuation, JSON event parsing, `--plan-yolo`, read-only tool lockouts, approval semantics. **This skill is that knowledge, distilled and battle-tested.**

## 📦 What's inside

```
omp-skill/
├── SKILL.md                      # the playbook your agent loads on demand
├── references/
│   ├── cli-reference.md          # full flag/subcommand reference (from omp 18.1.18 --help)
│   └── capabilities.md           # deep-dive: sessions, plan, subagents, LSP, DAP,
│                                 #   web, GitHub, approvals, providers, MCP, RPC/SDK
├── install.sh                    # multi-agent installer (no sudo)
└── docs/banner.svg
```

Everything is plain Markdown — no code executes on install, nothing phones home.

## 🚀 Install

**One-liner** (auto-detects your agents and installs everywhere relevant):

```sh
curl -fsSL https://raw.githubusercontent.com/zaharenok/omp-skill/main/install.sh | sh
```

**Or pick targets explicitly:**

```sh
curl -fsSL https://raw.githubusercontent.com/zaharenok/omp-skill/main/install.sh | sh -s -- --hermes --omp --claude
```

**Or manual** — it's just files:

```sh
git clone https://github.com/zaharenok/omp-skill.git
cd omp-skill
./install.sh --hermes   # or --omp --claude --codex --opencode --agent ... / --all
```

Requires [omp](https://omp.sh/docs/quickstart) installed and at least one provider authenticated (`omp models` to check).

## ⏱ 30-second demo

Ask your agent anything like this:

> *Use omp to find why the user-session test hangs, fix the root cause, run the smallest relevant test, and explain what changed.*

With the skill loaded, the agent runs:

```console
$ omp -p --max-time 600 'Find why the user-session test hangs, fix the root cause, run the smallest relevant test.'
✗  test user-session — timeout after 30s
🔎 read src/session/manager.ts
🔎 lsp → references of SessionStore.refresh (7 hits)
✎  edit src/session/manager.ts (+2 −1)
✓  test user-session — pass in 1.2s

Root cause: refresh() re-scheduled the idle timer without cancelling the
previous one, so callbacks piled up until the test exceeded its timeout.
```

*(illustrative transcript — real output streams to stdout)*

Coming back tomorrow? The session kept the context:

```sh
omp -c -p 'Now apply the same fix pattern to the workspace timer.'
```

## 📖 What your agent learns

| Lesson | Where |
|---|---|
| Headless one-shots that can't hang (`-p`, `--max-time`, `--no-session` semantics) | SKILL.md |
| Session continuation for projects with accumulated knowledge (`-c`, `-r`) | SKILL.md |
| NDJSON event parsing — final answer, usage, cost per turn (`--mode json`) | SKILL.md |
| Plan-then-execute for risky changes (`--plan-yolo`, reviewable two-step) | SKILL.md |
| omp's own subagents: scout / reviewer / security-reviewer fan-out | SKILL.md |
| Safety: default `yolo` approvals, read-only lockouts (`--tools read,grep,glob`) | SKILL.md |
| Model routing: `--smol`/`--slow`/`--plan`, fuzzy `--model`, thinking levels | SKILL.md |
| Full CLI flag + subcommand reference | [references/cli-reference.md](references/cli-reference.md) |
| Every capability: LSP, DAP, browser, GitHub, MCP, providers, RPC/SDK | [references/capabilities.md](references/capabilities.md) |

## 💼 Compatibility

The skill is plain `SKILL.md` + Markdown references. Installers provided for:

| Agent | Location | Explicit invocation |
|---|---|---|
| **Hermes Agent** | `~/.hermes/skills/…/omp/` | auto-matched by description |
| **omp itself** | `~/.omp/agent/skills/omp/` | `/skill:omp …` |
| **Claude Code** | `~/.claude/skills/omp/` | `/skill:omp …` (also auto-imported by omp) |
| **Codex** | `~/.codex/skills/omp/` | compatible dir |
| **OpenCode** | `~/.config/opencode/skills/omp/` | compatible dir |
| **Any AGENTS.md-style agent** | `~/.agent/skills/omp/` | compatible dir |

Verified against **omp 18.1.18** on macOS. CLI drift is documented in [references/cli-reference.md](references/cli-reference.md) — PRs welcome when omp changes.

## 🤝 Contributing

Found a pattern that should be in the skill? A flag that changed?

- ⭐ **Star this repo** if it saved you a context-shuttle session — it helps others find it
- 🐛 [Open an issue](https://github.com/zaharenok/omp-skill/issues) with the omp version and what broke
- 🔀 PRs welcome — the skill gets better with every real-world correction
- 📢 Share it with someone still pasting diffs between an editor, a shell, and a chat window

## 📄 License

[MIT](LICENSE) © Oleg Zakharchenko

Not affiliated with omp — just a skill for driving it well. omp itself: [omp.sh](https://omp.sh) / [github.com/can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)
