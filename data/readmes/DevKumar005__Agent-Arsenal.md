# Agent Arsenal

> **Equip the right skill, not the whole armory.**  
> A curated, bloat-free reference for selecting, installing, and using AI agent skills across **Antigravity**, **Claude Code**, **OpenAI Codex CLI**, **Cursor**, **GitHub Copilot**, and **local LLMs**.  
> **Canonical Source & Upstream Updates:** https://github.com/DevKumar005/Agent-Arsenal

---

## ⚡ Which Path Should You Take?

> **Tip:** You can read and run commands manually, **or simply ask your AI agent to read this hub and install what you need** — letting the agent do it saves your time and avoids wasting tokens on trial-and-error.

| Who You Are | What to Do | Token Cost |
|:---|:---|:---|
| **Experienced / Know what you want** | Tell your agent which skill to install (or grab the command from [quick-install.md](quick-install.md)). **No intake, no brief, no loop.** | Minimal |
| **New / Unsure / Stuck on a project** | Use [skill-matcher.md](skill-matcher.md) — answer 5 quick questions (or let your agent scan manifest files) to save `.agents/project-brief.md` and match the best 1–3 skills. | ~250 tokens |

---

## 🚦 Agent & User Entry Workflow (Start Here!)

**Before reading the other files in this folder (to save tokens):**

1. **Agents MUST ask the user first** how they want to proceed:
   - **Check & Update first:** Ask if the user has any new skill/plugin link(s) to add to `[TO BE ADDED]` in `sources.txt` right now. If yes, add them first, then process `[TO BE ADDED]`, verify `[ADDED]` source links for command/doc changes, and check locally installed skills for updates before starting work.
   - **Work / Install directly:** Skip update checks and go straight to the task or installing skills.
2. **Start with [sources.txt](sources.txt):**
   - Check `[TO BE ADDED]`. If any links exist, research and document them in `skills.md`, `agents.md`, `quick-install.md`, `README.md`, and `best-practices.md` (following each file's existing format), then move those links to `[ADDED]`.
   - Only after `[TO BE ADDED]` is clear should you read the specific guides needed for your task.
3. **Respect the user's experience level:**
   - If the user already named a skill or profile, install/explain it **immediately** — never force `skill-matcher.md` on them.
   - Only use `skill-matcher.md` when the user is unsure or stuck.
4. **Keep sources & installed skills fresh:**
   - Periodically re-check links in `[ADDED]` for updated install commands or breaking changes.
   - Periodically update installed skills (e.g., `npx skills update`, `agy plugin list`) so your active skill set stays current and safe.

---

## What Are Agent Skills?

Agent Skills are structured instruction packages (centered on a `SKILL.md` file) that teach AI coding assistants *how* to perform specialized tasks — from React performance optimization to security auditing. They follow the [Agent Skills Open Standard](https://agentskills.io/) and work across 18+ platforms.

**How they work (Progressive Disclosure):**

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Discovery (~30-50 tokens per skill)           │
│  Agent loads only name + description at startup         │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Activation (on-demand)                        │
│  Full SKILL.md instructions loaded when task matches    │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Execution (just-in-time)                      │
│  Scripts, references, assets pulled only when needed    │
└─────────────────────────────────────────────────────────┘
```

## 📂 Folder Structure

```
Agent-Arsenal/
├── README.md               ← You are here
├── skills.md               ← Complete catalog of all skills with details
├── skill-matcher.md        ← Guided intake & `project-brief.md` (for when you're stuck)
├── agents.md               ← Platform-specific installation & usage guides
├── best-practices.md       ← How to avoid skill bloat & keep agents sharp
├── quick-install.md        ← Copy-paste install commands by profile
├── sources.txt             ← Master list of all source links ([ADDED] / [TO BE ADDED])
├── CONTRIBUTING.md         ← Feature & skill request policy (Issues only)
├── LICENSE                 ← CC BY 4.0 (Attribution required)
└── .gitignore              ← Keeps local skill installs out of this repo
```

## 🎯 First-Time Setup in a Separate Project (4 Steps)

**Do NOT copy this folder into every project**, and **do NOT install all skills globally at once.** Keep this folder in one central place as your catalog, then follow these steps when working on any separate project:

1. **Find the 1–3 skills that fit your project:**
   - **Quick lookup:** Check the [Skill Selection Matrix](skills.md#skill-selection-matrix) at the bottom of `skills.md`.
   - **Stuck or unsure?** Use [skill-matcher.md](skill-matcher.md) — let your agent scan your manifest files or ask 5 short questions and save a compact `.agents/project-brief.md` inside *your project* to match the exact right skill (saves tokens across sessions).
2. **Install only those skills inside your project folder:**
   ```bash
   cd path/to/your-project
   npx skills add <owner/repo> --skill <skill-name>
   ```
   *(New to the CLI? See [quick-install.md](quick-install.md) for copy-paste commands per profile and MCP setup.)*
3. **Tag & use on demand (zero idle bloat):**
   - **Antigravity:** Mention the skill name or `/skill-name` in chat; for heavy plugins, install globally and keep them **disabled** (`agy plugin disable <name>` or Plugins UI) until needed — or keep `SKILL.md` files in a cold folder and `@`-mention the file path in chat.
   - **Claude Code / Cursor:** Invoke explicitly with `/skill-name`.
   - **Codex CLI:** Tag explicitly with `$skill-name` (and set `allow_implicit_invocation: false` in `agents/openai.yaml` to block auto-triggering).
   - **LM Studio:** Attach via `@skill-name` in chat.
4. **Update periodically:** Run `npx skills update` inside projects where skills are installed, and sync `sources.txt` when new links are added.

## 🗂️ Skill Collections at a Glance

| Collection | Author | Category | Skills |
|:---|:---|:---|:---:|
| Vercel Agent Skills | Vercel Labs | Frontend / React / Next.js / Design | 6 |
| Anthropic Skills | Anthropic | Document creation + Skill Creator meta-tool | 5+ |
| Elephant-Goldfish Model | Google | Spec-Driven Development / Architecture | 7 |
| Modern Web Guidance | Google Chrome | Web Platform / Standards / A11y | 100+ guides |
| Lighthouse | Google Chrome | Performance / SEO / Accessibility Audits | Tooling |
| Stitch Skills | Google Labs | UI Design / Code-to-Design / Components | 12+ |
| Red Hat ProdSec Skills | Red Hat | Security / AI Guardrails / Container Hardening | 100+ |
| Trail of Bits Skills | Trail of Bits | Security Auditing / Static Analysis / Smart Contracts | 20+ |
| Playwright MCP | Microsoft | Browser Testing / Automation / Self-Healing Tests | MCP Server |
| Impeccable | Paul Bakaus | Anti-Slop Design / UI Critique / Accessibility | 10+ commands |
| gstack | Garry Tan (YC) | Full-Stack Lifecycle / Product / QA | 20+ commands |

## ⚠️ Don't Carry the Whole Armory

> **More skills ≠ smarter agent.** Loading too many skills at once weighs down your agent's context, blurs tool routing, and causes the "Lost in the Middle" problem where instructions get ignored.

**Read [best-practices.md](best-practices.md) for the full guide**, but the core rules are:

1. **Start with zero skills** — add one only when the agent repeatedly fails a specific task
2. **Never exceed 8-12 active skills** at once for cloud models (3-5 for local LLMs)
3. **Scope skills to projects** — a React project doesn't need security audit skills
4. **Use role-based profiles** — different skill sets for different types of work

## 📖 Detailed Guides

| Guide | What You'll Learn |
|:---|:---|
| [**skills.md**](skills.md) | Every skill from every collection — what it does, when to use it, install command |
| [**skill-matcher.md**](skill-matcher.md) | Guided intake & `project-brief.md` workflow when you're stuck or unsure which skill fits |
| [**agents.md**](agents.md) | Platform-by-platform setup for Antigravity, Claude Code, Codex, Cursor, Copilot, local LLMs |
| [**best-practices.md**](best-practices.md) | Context window management, skill profiles, audit strategies, anti-bloat patterns |
| [**quick-install.md**](quick-install.md) | Copy-paste install commands organized by profile and platform |

## 🔗 Adding New Sources & Checking Updates

All source links live in [**sources.txt**](sources.txt) under `[ADDED]` and `[TO BE ADDED]`.

1. Add any new link under `[TO BE ADDED]` in `sources.txt`
2. Document it in `skills.md`, `agents.md`, `quick-install.md`, `README.md`, and `best-practices.md` matching their format
3. Move the link to `[ADDED]` in `sources.txt`
4. Periodically run `npx skills update` (and check source links) to keep commands and installed skills up to date and safe

## 💬 Requesting Skills or Features

Pull requests are currently closed so this hub stays clean and consistent. Want a new skill added or found an outdated command? Open an issue via [CONTRIBUTING.md](CONTRIBUTING.md) and I'll review and add it.

---

*Original project by Dev Kumar Sharma — https://github.com/DevKumar005/Agent-Arsenal | Last updated: November 2026*