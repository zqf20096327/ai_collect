# claude-code-kit

**A complete Claude Code setup in one install: 139 skills, plugins, MCP servers, memory, token savers and a way of working that gets more out of the model.**

It covers coding, design, video, marketing, research and security. Most of it also works in **Codex**, **Google Antigravity**, **Gemini CLI**, **Cursor**, **Windsurf** and **Cline**, so it runs on free plans too.

You don't install anything by hand: you hand [`INSTALL.md`](INSTALL.md) to your agent and it does the work, asking before it touches anything.

## Written for this kit

| Skill | The problem it solves |
|---|---|
| [`delegate`](skills/delegate) | Claude doing bulk work you could get for free. Hands it to Codex, Antigravity or DeepSeek, blocks secrets, reviews the result |
| [`skill-profiles`](skills/skill-profiles) | 100+ skills overflowing the context. Turns groups on or off for the day's work |
| [`handoff`](skills/handoff) | Long sessions getting slow and expensive. Saves the thread to a file so a fresh session picks it up |
| [`weekly-update`](skills/weekly-update) | Not knowing what's outdated. Weekly read-only report; updates only what you approve |
| [`prelaunch-audit`](skills/prelaunch-audit) | Shipping a site that looks vibe-coded. Bugs, security, legal, SEO, load test and 20 tell-tale signs |
| [`render-qa`](skills/render-qa) | Sending a broken render. Checks duration, borders, cut-off text and numbers on a contact sheet |
| [`anti-slop`](skills/anti-slop) | Generic AI-sounding output. Checks every deliverable for generic, padded or invented content and tells you what it found |

Install just these 7 in one line (Claude Code, Codex, Antigravity and other agents):

```bash
npx skills add sant1jmnz/claude-code-kit -g -s anti-slop delegate skill-profiles handoff weekly-update prelaunch-audit render-qa
```

Plus **131 skills by 13 other authors** (design, marketing, video with HyperFrames, Three.js, Instagram, research, security...), bundled unchanged with their author, source and license: see [`CREDITS.md`](CREDITS.md).

## Quick start

1. Clone this repo or download it as a ZIP.
2. Open your agent **inside the repo folder**.
3. Paste this:

   > Read `INSTALL.md` and apply it on my computer. Ask me before changing any global file.

4. Restart the agent when it finishes (skills and plugins load at startup).

The agent backs up your config, shows what it will change and waits for your OK. It installs a small base set, not all 139: too many skills fill the context.

## What you get

- **A weekly update check**: a scheduled task makes your agent look for updates of everything installed and report, never changing anything without your OK.
- **A way of working** that gets much more out of the model: skill-first, plan → build → verify, short answers, no invented data, no generic "AI look".
- **Skills** for coding, design, marketing, video, documents, research, security and more.
- **Working habits** in the global instructions: review intent not lines, prove it before saying "done", scope before big work, ask before spending paid credits.
- **Plugins and MCPs**: a full dev workflow (`superpowers`), design systems, docs lookup (Context7), browser testing (Playwright, Chrome DevTools).
- **A no-AI-slop rule** so deliverables don't read as generic.
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
| [`CREDITS.md`](CREDITS.md) | Author, source and license of every third-party skill |
| [`templates/`](templates) | Global instructions, `settings.json` fragment, memory templates |
| [`skills/`](skills) | 7 skills written for the kit + 132 bundled third-party skills |

## What it does NOT include

Plugins and MCP servers are installed from their original repos. Third-party skills are only bundled when their license allows it (MIT or Apache-2.0); skills without a license are not included. No keys or personal data are included. Paid or key-based tools (e.g. Firecrawl) are optional and you add the key yourself.

## Requirements

Node.js 18+, git, and one agent. Works on Windows, macOS and Linux.

## Disclaimer

Shared as-is. Every skill is text that tells your AI what to do: read what it installs before accepting. MIT license for what's written here; bundled skills keep their own license.
