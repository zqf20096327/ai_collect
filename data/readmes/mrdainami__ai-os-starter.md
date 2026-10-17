# AI OS Starter

**The folder you talk to.** A tiny starter cockpit for building your own AI OS: a system that does real work in your voice, one piece at a time. It ships almost empty on purpose. You open it with an AI coding tool, run one command, answer a few questions, and walk away with a working part of your business you actually own.

Built on the **FRAME** method, and made so the AI model in the middle is a **swappable slot**. When a better model ships, you drop it in and the whole system levels up for free.

> The companion to the video **[How To Build Your Own AI OS (Layer by Layer)](https://dainami.ai/resources/ai-os-blueprint)** by [Dainami AI](https://dainami.ai). Grab the free guide there and follow along.

---

## What is an AI OS?

An AI OS is just a **folder you talk to.** It holds three things:

- **Context** (the *Resources*): plain-text files that make the AI sound like you and know your work.
- **Tools** (the *Skills*): small, repeatable recipes that do a job.
- **Connections** (the *Access*): the apps and data it can reach.

You build it up one piece at a time. Most people collect tools: a new app every week, forty tabs, and a business that still lives in their head. An AI OS is the opposite. One system the tools plug into, that you keep even as the tools churn underneath it.

---

## Quick start (about 20 minutes)

### 1. Get an IDE

An IDE is just a workspace to hold your files and run your OS. Nothing scary. Pick one, both are free:

- **[VSCode](https://code.visualstudio.com)** — simple, the safe default.
- **[Cursor](https://cursor.com)** — the same idea, more AI built in.

### 2. Get Claude, then Claude Code

- Make a free account at **[claude.ai](https://claude.ai)**.
- Add **[Claude Code](https://docs.claude.com/en/docs/claude-code)**, the tool that lets Claude work right inside your folder with the context of your files.

> This starter is **tool-neutral**. Claude Code is what we use and what the guide is written for, but Codex, Cursor's agent, or any other AI coding tool can run it too. Each just needs to open this folder and read `AGENTS.md` first.

### 3. Get this folder

**Use this template** (green button, top of this repo) or clone it:

```bash
git clone https://github.com/mrdainami/ai-os-starter.git
cd ai-os-starter
```

Or hit **Code → Download ZIP** and unzip it. Then open that folder in your IDE.

### 4. Build your first OS

Open your AI tool **inside this folder** (this is the one rule, see below), then type:

```
/build-os
```

It interviews you, works out what your OS needs, sets everything up in the right place, builds your first skill, and tests it with you. You answer in plain language. You do not need to understand the folders.

### 5. See it as a workspace (optional)

```
/obsidian-view
```

This turns your OS into a clean, clickable workspace in [Obsidian](https://obsidian.md) (a free app): a dashboard, and a board where it makes sense. Your OS works fine without it. This is just the nice visual layer.

---

## The one rule: always launch inside this folder

Open your AI tool **inside this folder** (the cockpit), never above it and never inside a sub-folder.

- **Claude Code:** open a terminal, `cd` into this folder, run `claude`.
- **Cursor:** *Open Folder* → pick this folder → open the chat.

Everything (skills, connections, keys) lives at this root so it is all reachable. Launch somewhere else and nothing loads. That is the whole trick.

---

## The two skills

Both live in `.claude/skills/` and are plain markdown, so you can read and edit exactly what they do.

### `build-os` — build or extend your OS

The one you come back to again and again. Each run it reads what already exists, then builds the next piece with that context:

- **New OS:** scopes the one job, scaffolds the brain from `_template/`, gathers what it needs to know, and builds a first working skill, showing you a plan and getting your yes before it builds anything.
- **Extend an OS:** adds another skill, connects a tool, or adds knowledge to one you already have.
- **Connects tools safely:** if a job needs an app or live data, it finds the right tool, wires it into `.mcp.json`, and walks you through adding the API key to `.env.local` (never into a shared file).

Run it any time: *"build me an OS"*, *"add a skill"*, *"connect a tool"*, or just describe a job you want done.

### `obsidian-view` — see your OS as a workspace

Turns any OS in the cockpit into a navigable Obsidian workspace: a HOME dashboard, a per-OS dashboard, light frontmatter on your notes, and a live board (an Obsidian Base) when an OS produces a stream of similar items (posts, leads, briefs). Optional and re-runnable any time to refresh. It helps you install and open Obsidian if you do not have it.

---

## The FRAME method

Every OS you build is one folder that spells **FRAME**. This is the structure that makes it survive model changes instead of breaking on them:

| Letter | Part | What it is | Lives in |
|---|---|---|---|
| **F** | **Focus** | The one job, and what "done" looks like. One OS, one job. | `FOCUS.md` |
| **R** | **Resources** | Your voice, rules, and examples as plain text you own. The part that lasts. | `resources/` |
| **A** | **Access** | The tools and apps it can reach, keys kept private. | `ACCESS.md` + `.mcp.json` |
| **M** | **Make** | The skills and agents that do the work. | `.claude/` at the cockpit root |
| **E** | **Engine** | How it runs. Start by hand, then automate once it is trusted. | `ENGINE.md` |

**Make** is the only tool-specific part, on purpose. It lives in your AI tool's folder (`.claude/` for Claude Code). Swap the tool and you re-point Make. The other four parts are plain files that come with you, unchanged. That is what makes a FRAME OS portable.

---

## The five layers (don't automate on day one)

Building an OS that lasts means going one layer at a time. Rushing straight to full automation is how you end up with AI slop.

1. **Do it manually.** Figure out your own flow and voice first. You cannot hand off what you cannot define.
2. **Find the bottleneck.** Spot the one piece that costs you the most and is worth handing off.
3. **Semi-automate.** Build that one piece with a human in the loop. You only learn what to fix by using it.
4. **Expand.** Connect the working piece to the next one, part by part.
5. **Hand it off.** Once a part is proven, let it run on its own. This is the step you earn, not the one you start on.

---

## What's in this folder

```
ai-os-starter/
├── START-HERE.md      First thing to read. The 3-step getting started.
├── AGENTS.md          The cockpit brain. Any AI tool reads this first.
├── CLAUDE.md          Points Claude Code at AGENTS.md.
├── .claude/
│   ├── skills/        The tools. build-os + obsidian-view (yours grow here).
│   └── agents/        Specialist agents (empty to start).
├── _template/         The blank OS skeleton build-os copies for each new OS.
│   ├── FOCUS.md  · ACCESS.md · ENGINE.md · AGENTS.md · CLAUDE.md
│   └── resources/
├── .mcp.json          Where app connections (MCP servers) are stored.
├── .env.example       Documents which API keys are needed.
└── .gitignore         Keeps your secrets (.env.local) out of git.
```

Your OS folders (e.g. `content-os/`, `sales-os/`) appear here as you create them.

---

## Keeping your keys safe

Some connections need an API key. Your keys live in **`.env.local`**, which is **gitignored and never committed**.

- Copy `.env.example` to `.env.local` and fill in real values there.
- Launch with `source .env.local && claude` so the keys load.
- `build-os` tells you the exact line to add whenever a tool needs one.

Never paste a raw key into `.mcp.json` or any file that gets committed. `build-os` references keys by name, not value.

---

## Want your AI OS built with you?

This starter is free and yours to keep. If your team wants a custom AI OS built for you, [work with Dainami AI](https://dainami.ai/work-with-us).

Made by [Dainami AI](https://dainami.ai) · Built on FRAME · Focus · Resources · Access · Make · Engine

## License

[MIT](LICENSE). Use it, fork it, build your business on it.
