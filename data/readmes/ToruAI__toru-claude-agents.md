# Toru Claude Agents

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](#quick-start)
[![Always-on context: ~1.1k tokens](https://img.shields.io/badge/always--on%20context-~1.1k%20tokens-brightgreen)](#what-it-costs-you)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A dev workflow for [Claude Code](https://code.claude.com/docs/en/overview) that won't call your work done until your tests, linter and build exit zero — and won't call it mergeable until a security audit passes.** Seven specialists run it. Install is two commands.

Built by [ToruAI](https://toruai.com) — this is how we work with Claude Code, packaged as we actually use it.

## Quick Start

Inside Claude Code:

```
/plugin marketplace add ToruAI/toru-claude-agents
/plugin install toru-claude-agents@toru-claude-agents
```

Then **restart Claude Code** so the new agents and skills load. That's the whole install — memory comes with the plugin, and your own `settings.json`, agents and skills are untouched.

```
/scout what does this codebase do?          ← try it first, read-only
/dev-cycle implement user authentication    ← the actual workflow
```

### Three things to know before you install

- **It costs ~1.1k tokens of always-on context.** Seven agent descriptions plus fourteen skill descriptions. Nothing else loads until you invoke it. Don't take our word for it — `claude plugin details toru-claude-agents` prints the measured number.
- **It blocks `git push`.** Agents commit as much as they like; publishing stays your decision, because it's the one thing an agent can't take back. [How to remove it](#the-two-session-hooks).
- **These agents aren't built to agree with you.** Sentinel doesn't soften findings — "this is exploitable", not "this could potentially be a concern". Bob says so before building when the spec is contradictory. Scout reports that your premise was wrong rather than answering the question you asked. If you want an assistant that nods, install something else.

<details>
<summary><b>Prefer symlinks into <code>~/.claude/</code>? Use the installer instead.</b></summary>

```bash
git clone https://github.com/ToruAI/toru-claude-agents.git
cd toru-claude-agents
./install.sh              # Global install to ~/.claude/
./install.sh --local      # Local install to ./.claude/ (current project only)
./install.sh --dry-run    # Preview exactly what it would change — read this first
```

For people who want to read and edit the agents in place, or install into one project only. **It writes into `~/.claude/` and replaces some of what's there** — see [What the installer overwrites](#what-the-installer-overwrites) before running it. Pick one route, not both: the same agents registered twice is just noise.

</details>

## Why this instead of a bigger collection

Most collections hand you a hundred agents and leave the orchestration to you. This is the opposite bet: a small roster wired into one pipeline with objective exit conditions.

```
/dev-cycle   →   /dev-qa   →   /dev-security   →   /dev-rc   →   /dev-finish
  plan+build     tests,lint    Sentinel audit     last gate    commit+learnings
```

Exit conditions are machine-checked, not vibes: tests pass, lint clean, types clean, audit green. If they don't, the loop goes back to work. Session state lives in a file, so closing your terminal doesn't lose the thread.

That's the trade: fewer agents, but they run a process. If you want breadth, the big collections are genuinely better at breadth.

## The Team

Four agents do the development work:

| Agent | Role | What they do | Model |
|-------|------|--------------|-------|
| **Garry** | Chief of Staff | Plans, delegates, argues with the plan before Bob builds it | `opus` |
| **Bob** | Technical Builder | Writes code and tests; says so when the spec can't work | `sonnet` |
| **Sentinel** | Security Specialist | Audits for vulnerabilities; won't soften a severity | `opus` |
| **Scout** | Codebase Explorer | Read-only reconnaissance; reports when your premise is wrong | `haiku` |

<details>
<summary>Three more, for work that isn't code: <b>Arlo</b> (data), <b>Luna</b> (design), <b>Maya</b> (client-facing writing)</summary>

| Agent | Role | What they do | Model |
|-------|------|--------------|-------|
| **Arlo** | Data & Patterns | Finds the pattern, says which parts the numbers support | `inherit` |
| **Luna** | Design | Interfaces that remove decisions instead of adding controls | `inherit` |
| **Maya** | Client-facing | Pitches, proposals and hard emails, pressure-tested | `inherit` |

They cost context whether or not you use them — about 110 tokens for all three. If you want them gone, delete the three files from the plugin's `agents/` directory, or use the installer route and don't link them.

</details>

Models are *aliases*, so each agent picks up the current generation of its tier as new ones ship: `opus` for judgement, `sonnet` for building, `haiku` for fast reads, `inherit` to match your main conversation. Change any of them in the agent's frontmatter.

**How to use them:**
- **Automatic** — skills like `/dev-cycle` delegate to agents internally
- **Direct** — "have Bob review this code", "let Sentinel audit the auth flow"
- **Explicit** — the Task tool with `subagent_type: "toru-claude-agents:bob"` (plugin components are namespaced; on the installer route it's just `bob`)

## The Dev Workflow

```
/dev-cycle      →  plan and build, interactively — you approve the plan
/dev-full-auto  →  same pipeline, no check-ins: spec in, working software out
/dev-qa         →  tests, lint, types, build
/dev-security   →  Sentinel audit
/dev-rc         →  last gate before merge
/dev-finish     →  commit, capture what was learned
```

**The loop**: build → check → pass? → done. If not, fix and repeat. `/dev-cycle` asks before it plans; `/dev-full-auto` doesn't ask at all and stops only at a real blocker.

**Honest limit:** the gates are instructions to Claude, enforced by Claude running your actual test and lint commands and reading the exit codes — not by CI. It will tell you a suite failed; it can't stop you overruling it. The one gate enforced mechanically is the push guard below.

## All Skills

| Skill | What it does |
|-------|--------------|
| `/dev-cycle` | Run a feature end to end, with a session file that survives a closed terminal |
| `/dev-full-auto` | Hand over a spec and walk away; stops only at a real blocker |
| `/dev-qa` | Run the project's own tests, linter, type checker and build |
| `/dev-security` | Audit for vulnerabilities, leaked secrets, risky dependencies |
| `/dev-rc` | Last gate before merge: QA, security, review, changelog |
| `/dev-finish` | Close out: summarise, capture learnings, prepare the commit |
| `/scout` | Map unfamiliar code or research an approach, read-only |
| `/branch-workflow` | Branch and commit conventions that keep agent work reviewable |
| `/openspec-workflow` | Write the spec first, then check the built thing against it |
| `/megg-learn` | Save a fact, decision or gotcha so the next session knows it |
| `/megg-state` | Hand off an unfinished session: done, next, blocked |
| `/cc-docs` | Look up how Claude Code works, from the current official docs |
| `/claude-code-mastery` | Design better agents, skills and hooks |
| `/self-improvement` | Turn friction you just hit into a workflow change |

## What it costs you

**~1.1k tokens of always-on context** — the 7 agent and 14 skill descriptions above, and nothing else until you invoke something. Verify with `claude plugin details toru-claude-agents`, which prints the measured number and the per-component breakdown.

## Requirements

- **Claude Code** — [install first](https://code.claude.com/docs/en/overview)
- **jq** — required for the push guard. Without it the guard **blocks every Bash command** rather than silently letting pushes through, so install it: `brew install jq`
- **Node.js 20+** — only if you want memory (below)

## The Two Session Hooks

These are the opinionated part of the package, so here is exactly what they do:

| Hook | What it does | Why |
|------|--------------|-----|
| `SessionStart` | Loads your project memory via megg | Agents start knowing the project instead of blank |
| `PreToolUse` | **Blocks `git push`** | Agents commit freely; publishing stays your decision |

The push guard is a real script ([`hooks/push-guard.sh`](hooks/push-guard.sh)) with [its own test suite](hooks/push-guard.test.sh), not a regex you have to trust. It catches `git push`, `git -C /elsewhere push` and `git -c x=y push`; it deliberately allows `git push --dry-run` and any command that merely *mentions* pushing, like `git commit -m "fix the push hook"`. Run `./hooks/push-guard.test.sh` to see the cases. Determined bypasses exist (`bash -c '…'`) — it's a guardrail against accidents, not a security control.

**To turn it off.** On the installer route, delete the `PreToolUse` block from your `~/.claude/settings.json`. On the plugin route you can't remove one hook from an installed plugin — either disable the whole plugin (`/plugin disable toru-claude-agents`) or use the installer route. If you want the *opposite* — a harder block that doesn't depend on this plugin at all — put this in your own settings and skip our hook entirely:

```json
{ "permissions": { "deny": ["Bash(git push:*)"] } }
```

**A note on the memory hook.** It reads `.megg/` from the project you open. Treat that like any file in a repo you cloned: if you open an untrusted repository that ships a `.megg/` directory, its contents reach the session as project context. Delete `.megg/` from repos you don't trust.

## Memory: megg (optional)

[megg](https://github.com/ToruAI/megg) is the memory layer behind `/megg-learn`, `/megg-state` and the session-start hook. **It's optional.** Without it every skill still works — you lose cross-session memory, and `/dev-cycle` won't recall earlier decisions.

On the plugin route it's declared in the plugin's `.mcp.json`, so it wires itself up — Claude Code starts it with `npx megg@1.1.0 mcp` (pinned, so you get the version this was tested against). **Don't want it?** Remove the `megg` entry from `.mcp.json` in the plugin directory, or don't install Node — the server simply fails to start and everything except cross-session memory keeps working.

On the installer route, the installer offers to set it up (both prompts default to *no*, so pressing Enter declines). Either way you can register it by hand:

```bash
claude mcp add --transport stdio --scope user megg -- npx megg mcp
```

## How It Works

**Plugin route** — Claude Code reads `agents/`, `skills/` and the hooks from the plugin's own copy. Nothing is written into your `~/.claude/` config: your settings, agents and skills are untouched. Update with `/plugin update toru-claude-agents@toru-claude-agents`, and restart afterwards.

**Installer route** — symlinks into `~/.claude/` (or `./.claude/` with `--local`) and copies `config/settings.json`. Your clone stays editable; `./update.sh` pulls changes and refreshes the symlinks (it targets `~/.claude/` only — for a `--local` install, re-run `./install.sh --local`).

### What the installer overwrites

`./install.sh --dry-run` prints this for your machine. In short, it takes a timestamped backup to `~/.claude/.backups/<timestamp>/` first, then:

| Path | What happens |
|------|--------------|
| `~/.claude/settings.json` | **Never overwritten.** If you already have one, the hooks are *not* installed — merge `config/settings.json` yourself, or you get no push guard and no memory hook |
| `~/.claude/CLAUDE.md` | **Replaced** with this repo's `config/CLAUDE.md` |
| `~/.claude/docs/`, `~/.claude/scripts/` | **Replaced** by symlinks — anything you keep in those directories moves to the backup |
| `~/.claude/agents/`, `~/.claude/skills/` | Symlinked per item; **a same-named agent or skill of yours is replaced** |

Everything above is recoverable with `./uninstall.sh --restore`. The plugin route touches none of it — which is why it's the recommended one.

Pick one route. Running both registers the same agents twice.

## The Philosophy

**Iterate until the checks pass.** Not "looks done" — tests pass, lint clean, types clean, audit green. State lives on disk (git commits, test output, session files), so progress survives a closed terminal.

**Why specialists?** One generic assistant optimises for *helpful*, and helpful drifts toward agreeable. A specialist optimises for its domain: Sentinel cares about your attack surface, not your timeline. Scout would rather tell you the question was wrong than answer it neatly. Bob argues once, then builds.

## Uninstall

Plugin route:
```
/plugin uninstall toru-claude-agents
```

Installer route:
```bash
./uninstall.sh              # Remove symlinks, keep your modifications
./uninstall.sh --restore    # Remove and restore previous state from backup
./uninstall.sh --list-backups  # See available backups
```

## Documentation

- **[Getting Started](docs/guides/GETTING-STARTED.md)** - First 15 minutes walkthrough
- **[Concepts](docs/guides/CONCEPTS.md)** - Agents, skills, megg, MCP explained
- **[Troubleshooting](docs/guides/TROUBLESHOOTING.md)** - Common issues and fixes

## License

[MIT](LICENSE)

---

Built by [ToruAI](https://toruai.com) | [Report issues](https://github.com/ToruAI/toru-claude-agents/issues) | [Changelog](CHANGELOG.md)
