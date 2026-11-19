# claude-code-kit

A complete, battle-tested setup for **Claude Code**: curated skills, plugins, MCP servers, token-saving habits, a file-based memory system and a proven way of working. Most of it ports to **Codex**, **Google Antigravity**, **Gemini CLI**, **Cursor**, **Windsurf**, **Cline** and other agents, so it also works on free plans.

You don't install anything by hand: you give [`INSTALL.md`](INSTALL.md) to your AI agent and it does the work, asking before it touches anything.

## Quick start (30 seconds)

1. Clone this repo or download it as a ZIP.
2. Open your agent (Claude Code, Codex, Antigravity, ...) **inside the repo folder**.
3. Paste this:

   > Read `INSTALL.md` and apply it on my computer. Ask me before changing any global file.

4. Restart the agent when it finishes (skills and plugins load at startup).

The agent backs up your config, shows what it will change and waits for your OK. Nothing is installed behind your back.

## What you get

- **Rule #1: no AI slop.** The agent must not produce generic, padded or invented output, and must tell you when something might look like it.
- **A weekly update check**: a scheduled task makes your agent look for updates of everything installed and report, never changing anything without your OK.
- **A way of working** that gets much more out of the model: skill-first, plan → build → verify, short answers, no invented data, no generic "AI look".
- **Skills** for coding, design, marketing, video, documents, research, security and more, installed from their original authors.
- **Plugins and MCPs**: a full dev workflow (`superpowers`), design systems, docs lookup (Context7), browser testing (Playwright, Chrome DevTools).
- **Token savers**: RTK, subagent rules, effort/model routing, handoffs, and community mods that cut usage automatically. Essential on trial and free plans.
- **A memory system** in plain Markdown so the agent doesn't forget you between sessions.
- **Portable instructions** (`AGENTS.md`-style) for other agents.

## What's inside

| Path | What it is |
|---|---|
| [`INSTALL.md`](INSTALL.md) | Step-by-step instructions **for the AI agent** |
| [`AGENTS.md`](AGENTS.md) | Tells any agent opened in this repo what to do |
| [`docs/01-workflow.md`](docs/01-workflow.md) | The workflow and habits that make the difference |
| [`docs/02-skills.md`](docs/02-skills.md) | Recommended skills, where they come from, how to install them |
| [`docs/03-plugins.md`](docs/03-plugins.md) | Claude Code plugins (superpowers, design, security, ...) |
| [`docs/04-mcp.md`](docs/04-mcp.md) | MCP servers: live docs, browser, scraping |
| [`docs/05-save-tokens.md`](docs/05-save-tokens.md) | How to spend less quota |
| [`docs/06-memory.md`](docs/06-memory.md) | File-based memory across sessions |
| [`docs/07-other-agents.md`](docs/07-other-agents.md) | Porting to Codex, Antigravity, Gemini CLI, Cursor and more |
| [`docs/08-token-saving-mods.md`](docs/08-token-saving-mods.md) | Mods that cut tokens automatically |
| [`plugins/skill-guide`](plugins/skill-guide) | Own mod: `/guide` skill cheat-sheet + skill suggestions as you type (EN/ES) |
| [`docs/09-weekly-updates.md`](docs/09-weekly-updates.md) | Rule #1 (no AI slop) and the weekly "check for updates" task |
| [`templates/`](templates) | Global instructions, `settings.json` fragment, memory templates |
| [`skills/`](skills) | Skills bundled here: `anti-slop`, `weekly-update`, `handoff`, `skill-profiles`, `youtube-scriptwriting` |

## What it does NOT include

Third-party skills and plugins are **not copied**: they are installed from their original repos (each with its own author and license). No keys or personal data are included. Paid or key-based tools (e.g. Firecrawl) are optional and you add the key yourself.

## Requirements

Node.js 18+, git, and one agent. Works on Windows, macOS and Linux.

## Disclaimer

Shared as-is. Every skill is text that tells your AI what to do: read what it installs before accepting. MIT license for what's written here.
