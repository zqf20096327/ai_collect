# AI Dev Toolkit

> The best **skills, plugins, MCP servers and workflows** for AI coding agents (Claude Code, Codex, Cursor, Copilot, Gemini CLI and more), organized across the whole software development lifecycle, from planning to shipping, plus writing.
>
> Each entry says **what it does**, **when to use it** and **how to install it**. Within every section, the strongest picks come first.

<p align="center">
  <img src="https://img.shields.io/badge/last%20verified-2026--11--24-2ea44f?style=flat-square" alt="Last verified 2026-11-24">
  <a href="https://github.com/uveshm003/ai-dev-toolkit/actions/workflows/link-check.yml"><img src="https://img.shields.io/github/actions/workflow/status/uveshm003/ai-dev-toolkit/link-check.yml?style=flat-square&label=links" alt="Link check"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0-blue?style=flat-square" alt="License: CC0"></a>
</p>

<p align="center">
  <a href="#-top-10">Top 10</a> ·
  <a href="#-pick-your-stack">Pick your stack</a> ·
  <a href="#-andrej-karpathy">Karpathy</a> ·
  <a href="#1-full-workflows">Workflows</a> ·
  <a href="#2-plan-and-spec">Plan</a> ·
  <a href="#3-code">Code</a> ·
  <a href="#4-context-and-memory">Context</a> ·
  <a href="#5-design-and-ui">Design</a> ·
  <a href="#6-test-and-debug">Test</a> ·
  <a href="#7-review-and-ship">Review</a> ·
  <a href="#8-security">Security</a> ·
  <a href="#9-deploy-and-infrastructure">Deploy</a> ·
  <a href="#10-cost-and-usage">Cost</a> ·
  <a href="#11-docs-diagrams-and-visuals">Docs</a> ·
  <a href="#12-writing">Writing</a>
</p>

**Tags:** 🏢 official (from the platform's own team or an established company) · 🔑 needs an API key or token · 🤖 agents it works with

---

## 🆕 What's new

- **2026-11-24:** Six new tools: [Open Code Review](#open-code-review) (Alibaba) and [Plannotator](#plannotator) for review, [Modern Web Guidance](#modern-web-guidance) (Chrome, Edge, Firefox and MDN), [Astryx](#astryx) (Meta's design system), [Marionette MCP](#marionette-mcp) for Flutter and [/brag](#brag) for launch videos. All existing repos re-checked: none archived or moved.
- **2026-11-19:** Tags on every entry, [Pick your stack](#-pick-your-stack) recipes, side-by-side comparisons of [workflows](#which-workflow), [spec tools](#which-spec-tool) and [browser tools](#which-browser-tool), and a weekly link check. Every link and install command re-verified.
- **2026-11-19:** Expanded into the AI Dev Toolkit: the full SDLC, writing and a [Karpathy](#-andrej-karpathy) section.
- **2026-11-18:** First version of the list.

---

## Contents

- [🆕 What's new](#-whats-new)
- [🏆 Top 10](#-top-10)
- [🧭 Pick your stack](#-pick-your-stack)
- [🐐 Andrej Karpathy](#-andrej-karpathy)
- [Before you install](#before-you-install)
- **The SDLC**
  1. [Full workflows](#1-full-workflows)
  2. [Plan and spec](#2-plan-and-spec)
  3. [Code](#3-code)
  4. [Context and memory](#4-context-and-memory)
  5. [Design and UI](#5-design-and-ui)
  6. [Test and debug](#6-test-and-debug)
  7. [Review and ship](#7-review-and-ship)
  8. [Security](#8-security)
  9. [Deploy and infrastructure](#9-deploy-and-infrastructure)
  10. [Cost and usage](#10-cost-and-usage)
  11. [Docs, diagrams and visuals](#11-docs-diagrams-and-visuals)
- **Beyond code**
  12. [Writing](#12-writing)
  13. [Mobile](#13-mobile)
  14. [Career](#14-career)
  15. [Learning](#15-learning)
- [Find more](#find-more)
- [Write your own skill](#write-your-own-skill)
- [Contributing](#contributing)

---

## 🏆 Top 10

If you install nothing else, start here.

| # | Tool | Why |
|---|---|---|
| 1 | [Superpowers](#superpowers) | Makes the agent ask, spec and plan before it codes. The biggest single upgrade. |
| 2 | [Karpathy Guidelines](#karpathy-guidelines) | One `CLAUDE.md` that stops wrong assumptions, bloat and drive-by edits. |
| 3 | [Matt Pocock's Skills](#matt-pococks-skills) | Real engineering habits on demand: `/tdd`, `/diagnosing-bugs`, `/to-spec`. |
| 4 | [Context7](#context7) | Up-to-date library docs, so no more hallucinated APIs. |
| 5 | [GSD Core](#gsd-core) | Discuss, plan, execute, verify and ship in fresh context windows. |
| 6 | [Spec Kit](#spec-kit) | GitHub's toolkit for spec-driven development. |
| 7 | [Impeccable](#impeccable) | Stops generic "AI-looking" UIs. |
| 8 | [Humanizer](#humanizer) | Makes AI-written text read like a person wrote it. |
| 9 | [SkillSpector](#skillspector) | NVIDIA's scanner: check a skill is safe *before* you install it. |
| 10 | [TokenEconomizer](#tokeneconomizer) | Microsoft Research plugin that cut agent costs 18–31% on SWE-Bench. |

---

## 🧭 Pick your stack

Not sure where to start? Pick the row that sounds like you and install those, nothing more.

| You are… | Install these | Why this mix |
|---|---|---|
| 🚀 **Solo builder** | [gstack](#gstack) · [Karpathy Guidelines](#karpathy-guidelines) · [Context7](#context7) · [Impeccable](#impeccable) · [ccusage](#ccusage) | A whole team's judgment, guardrails against bloat, real docs, a UI that doesn't look AI-made, and a check on what it all costs. |
| 💙 **Flutter dev** | [Flutter Agent Plugins](#13-mobile) · [Dart Skills](#13-mobile) · [Marionette MCP](#marionette-mcp) · [Context7](#context7) · [Matt Pocock's Skills](#matt-pococks-skills) | Official Flutter and Dart know-how, an agent that taps through your running app to check its own work, current package docs, and `/tdd` for widget tests. |
| 👥 **Team lead** | [Spec Kitty](#spec-kitty) · [Elephant-Goldfish Model](#elephant-goldfish-model) · [Claude Code Action](#claude-code-action) · [Claude Code Security Review](#claude-code-security-review) · [SkillSpector](#skillspector) | Shared specs whichever agent each teammate uses, fresh-eyes design review, an AI reviewer on every PR, and a safety scan before a skill goes team-wide. |
| ✍️ **Writer** | [Humanizer](#humanizer) · [Marketing Skills](#marketing-skills) · [Anthropic Document Skills](#anthropic-document-skills) · [Diagram Design](#diagram-design) | Text that sounds human, copy that converts, real Word and PDF files, and diagrams worth publishing. |
| 🎓 **Learning AI** | [Karpathy's learning path](#learn-how-llms-actually-work) · [LearnHarness](#learnharness) · [LLM Council](#llm-council) · [autoresearch](#autoresearch) | Build the models from scratch, learn with a tutor that tracks what you know, compare models, then let an agent run experiments. |

---

## 🐐 Andrej Karpathy

Karpathy coined "vibe coding," and much of how people work with LLMs today traces back to his posts and repos. Here's what's useful from his work, in order.

### Karpathy Guidelines

[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) ![stars](https://img.shields.io/github/stars/multica-ai/andrej-karpathy-skills?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Cursor, or any agent that reads a rules file

A single `CLAUDE.md` built from [Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on where LLMs go wrong when coding: silent wrong assumptions, 1,000 lines where 100 would do, and edits to code they don't understand. It turns those into four rules:

| Principle | Fixes |
|---|---|
| **Think before coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| **Simplicity first** | Over-engineering, bloated abstractions |
| **Surgical changes** | Touching code that's unrelated to the task |
| **Goal-driven execution** | No clear success criteria; it pushes tests first |

<details>
<summary>Install</summary>

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

</details>

**Best for:** everyone. This is the cheapest upgrade on the list: one file, always on.

### autoresearch

[karpathy/autoresearch](https://github.com/karpathy/autoresearch) ![stars](https://img.shields.io/github/stars/karpathy/autoresearch?style=flat-square&label=%E2%AD%90)

🤖 any coding agent · needs an NVIDIA GPU

Give an agent a small but real LLM training setup and let it experiment overnight. It edits `train.py`, trains for 5 minutes, keeps the change if validation improved, and repeats. You only edit `program.md`, the agent's instructions. It's a clean, tiny template for any "agent improves a metric in a loop" setup.

<details>
<summary>Install</summary>

```bash
uv run prepare.py   # one-time data + tokenizer
# then point your agent at program.md
```

</details>

### LLM Council

[karpathy/llm-council](https://github.com/karpathy/llm-council) ![stars](https://img.shields.io/github/stars/karpathy/llm-council?style=flat-square&label=%E2%AD%90)

🔑 OpenRouter API key · local web app

Ask several LLMs the same question. Each one then reviews and ranks the others' answers anonymously, and a "chairman" model writes the final answer. It's a quick way to compare models side by side and get a better answer on hard questions. Karpathy calls it a "vibe coded" Saturday hack.

### rendergit

[karpathy/rendergit](https://github.com/karpathy/rendergit) ![stars](https://img.shields.io/github/stars/karpathy/rendergit?style=flat-square&label=%E2%AD%90)

Flattens any GitHub repo into one static HTML page with syntax highlighting. It has a human view and an LLM view, so you can paste a whole repo into a chat.

<details>
<summary>Install</summary>

```bash
uv tool install git+https://github.com/karpathy/rendergit
rendergit https://github.com/karpathy/nanogpt
```

</details>

### reader3

[karpathy/reader3](https://github.com/karpathy/reader3) ![stars](https://img.shields.io/github/stars/karpathy/reader3?style=flat-square&label=%E2%AD%90)

A tiny self-hosted EPUB reader that shows one chapter at a time, so you can paste it into an LLM and read along together. It shows how small a useful LLM workflow tool can be.

### Learn how LLMs actually work

The best free path from zero to understanding the models your agent runs on:

| Repo | What you learn |
|---|---|
| [nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | Video course: neural nets from scratch up to GPT |
| [micrograd](https://github.com/karpathy/micrograd) | Backprop in about 100 lines; start here |
| [minbpe](https://github.com/karpathy/minbpe) | How tokenizers work (BPE) |
| [nanoGPT](https://github.com/karpathy/nanoGPT) | Train a GPT in a few hundred lines |
| [nanochat](https://github.com/karpathy/nanochat) | The full pipeline: tokenizer, pretraining, finetuning, eval and a chat UI on one GPU node |
| [llm.c](https://github.com/karpathy/llm.c) | LLM training in raw C/CUDA |

---

## Before you install

### What's what

| Thing | What it gives the agent | Example |
|---|---|---|
| **Skill** | Know-how: *how* to do a task well. A folder with a `SKILL.md` that loads only when relevant. | `/tdd` |
| **MCP server** | Tools: *access* to a system (browser, GitHub, docs) | Playwright MCP |
| **Plugin** | A bundle of skills, commands, hooks and MCP config | Superpowers |
| **Workflow / framework** | A whole process: phases, roles, artifacts | GSD, BMAD, Spec Kit |
| **CLAUDE.md / AGENTS.md** | Always-on project rules | Karpathy Guidelines |

### Reading the tags

| Tag | Means |
|---|---|
| 🏢 | Official: built by the platform's own team or an established company (Anthropic, GitHub, Google, Microsoft, NVIDIA…) |
| 🔑 | You need an API key or token on top of your agent. Marked *optional* when it only unlocks extras. |
| 🤖 | Agents it supports, as stated in the project's README. **Any skills agent** means it installs with `npx skills`, which works across 70+ agents. **Any MCP client** means Claude Code, Cursor, Codex, VS Code and the rest. |

No 🔑 means it's free to run with the agent you already have. Everything listed is open source.

### Three ways to install a skill

```bash
# 1. skills CLI: works across 70+ agents
npx skills add <owner>/<repo>        # this project
npx skills add <owner>/<repo> -g     # all projects

# 2. Claude Code plugin marketplace
/plugin marketplace add <owner>/<repo>
/plugin install <plugin>@<marketplace>

# 3. By hand
cp -r some-skill ~/.claude/skills/
```

Start a new session afterwards.

> [!IMPORTANT]
> **Skills run with your agent's permissions.** NVIDIA's research found vulnerabilities in 26% of 31,000 skills analyzed. Scan anything unfamiliar with [SkillSpector](#skillspector) first.

> [!TIP]
> **Don't install everything.** Pick one workflow, one design skill and Context7. Use them for a week, then add more. Overlapping skills make agents less predictable. Not sure which? See [Pick your stack](#-pick-your-stack).

---

## 1. Full workflows

End-to-end methods that run the whole cycle: idea, spec, plan, build, test, ship. **Pick one.** They overlap.

### Which workflow?

| | [Superpowers](#superpowers) | [GSD Core](#gsd-core) | [BMAD Method](#bmad-method) | [gstack](#gstack) |
|---|---|---|---|---|
| **Big idea** | Ask, spec and plan before any code | Beat context rot with a fresh context per task | Agile roles and documents for the whole product | A virtual team of specialists |
| **Loop** | Clarify → spec → plan → TDD with subagents | Discuss → Plan → Execute → Verify → Ship | Clarify → Plan → Build and verify → Learn and adjust | Think → Plan → Build → Review → Test → Ship → Reflect |
| **How you drive it** | Just talk; skills trigger on their own | `/gsd-*` commands, one phase at a time | `bmad-build`, and `bmad-help` when stuck | A command per role: `/office-hours`, `/review`, `/qa`, `/ship`… |
| **Agents** | 15, incl. Claude Code, Codex, Cursor, Gemini CLI | Claude Code, Codex, Cursor, Copilot, OpenCode +more | Any agent that supports skills | Claude Code; others via `./setup --host` |
| **Pick it if** | You want one solid default | Long sessions keep falling apart | You're building a product from zero and want docs at every phase | You're a founder who wants product, design and QA review too |

### Superpowers

[obra/superpowers](https://github.com/obra/superpowers) ![stars](https://img.shields.io/github/stars/obra/superpowers?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, Gemini CLI, Copilot CLI, OpenCode +more

The most popular agent methodology. When you start building, the agent doesn't jump to code. It asks what you're really trying to do, shows you a spec in short chunks you can actually read, writes a plan, then builds with TDD and subagents.

<details>
<summary>Install (Claude Code)</summary>

```
/plugin install superpowers@claude-plugins-official
```

Other agents: see the [install guide](https://github.com/obra/superpowers#installation).

</details>

**Best for:** anyone who wants one solid default process.

### GSD Core

[open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) ![stars](https://img.shields.io/github/stars/open-gsd/gsd-core?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, Copilot, OpenCode, Windsurf +more

**GSD**, the community home since the original `gsd-build/get-shit-done` repo was archived. It solves *context rot*: quality drops as a session fills up. Every milestone runs a five-step loop of **Discuss, Plan, Execute, Verify and Ship**, and each executor starts in a fresh 200k-token context.

<details>
<summary>Install</summary>

```bash
npx @opengsd/gsd-core@latest
# then: /gsd-new-project   or   /gsd-onboard (existing repo)
```

</details>

**Best for:** long projects where sessions fall apart halfway through.

### gstack

[garrytan/gstack](https://github.com/garrytan/gstack) ![stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square&label=%E2%AD%90)

🤖 Claude Code; Codex and others via `./setup --host`

Garry Tan's (CEO of Y Combinator) daily setup. It turns your agent into a virtual team with specialist roles: a CEO who rethinks the product, an eng manager who locks the architecture, a designer who catches AI slop, a reviewer who finds production bugs, plus QA and release. Every change carries its tests and review evidence.

<details>
<summary>Install</summary>

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack \
  && cd ~/.claude/skills/gstack && ./setup
```

</details>

**Best for:** founders and solo builders who want a whole team's judgment.

### BMAD Method

[bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) ![stars](https://img.shields.io/github/stars/bmad-code-org/BMAD-METHOD?style=flat-square&label=%E2%AD%90)

🤖 any agent that supports skills

Agile AI-driven development. It brings agile phases and documents (briefs, specs, architecture) to your agent, and sizes the process to the work: small changes go straight to build, complex work gets the full treatment. A separate Founder module covers pricing, fundraising and the business side.

<details>
<summary>Install</summary>

```bash
npx bmad-method install
```

</details>

**Best for:** building a whole product from zero, with documents at every phase.

### SuperClaude

[SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) ![stars](https://img.shields.io/github/stars/SuperClaude-Org/SuperClaude_Framework?style=flat-square&label=%E2%AD%90)

🤖 Claude Code (sister projects exist for Gemini and Qwen)

A configuration framework that adds 30 commands, 20 agents, 7 behavioral modes and 8 MCP server integrations to Claude Code.

<details>
<summary>Install</summary>

```
/plugin marketplace add SuperClaude-Org/superclaude-plugin-marketplace
/plugin install superclaude
```

</details>

### wshobson/agents

[wshobson/agents](https://github.com/wshobson/agents) ![stars](https://img.shields.io/github/stars/wshobson/agents?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, Copilot, OpenCode +more

The biggest catalog here: 93 plugins with about 200 agents, 185 skills and 100 commands for Python, JS, review, testing, infra and more. They're written once and adapted for each agent. Install only the plugins you need.

<details>
<summary>Install</summary>

```
/plugin marketplace add wshobson/agents
/plugin install python-development@claude-code-workflows
```

</details>

### Leo's Claude Starter

[leogodin217/leos_claude_starter](https://github.com/leogodin217/leos_claude_starter) ![stars](https://img.shields.io/github/stars/leogodin217/leos_claude_starter?style=flat-square&label=%E2%AD%90)

🤖 Claude Code

One developer's real setup of skills, agents and hooks, shared across many repos with symlinks so a fix lands everywhere. Read it to see how someone *actually* organizes this.

---

## 2. Plan and spec

Agree on **what** to build before the agent builds it.

### Which spec tool?

| | [Spec Kit](#spec-kit) | [OpenSpec](#openspec) | [Elephant-Goldfish](#elephant-goldfish-model) | [Spec Kitty](#spec-kitty) |
|---|---|---|---|---|
| **From** | 🏢 GitHub | Fission AI | 🏢 Google | Community |
| **Flow** | Constitution → specify → plan → tasks → implement → converge | Explore → propose → apply → archive | Elephant drafts, Goldfish reviewers check with no prior context | Spec → plan → tasks → next → review → accept → merge |
| **Weight** | Full process, plus bug-fix and idea-assessment extensions | Light, built for existing codebases | Light; reviews docs you already have | Heavy; built for teams |
| **Stands out for** | Templates, presets and extensions you can bend to your org | Low ceremony; plain Markdown specs | Catching blind spots and design-to-code drift | Governance, and parallel agents in isolated git worktrees |
| **Agents** | Many; pick with `--integration` | 30+ | Claude Code, Codex, Antigravity | Claude Code, Codex, Cursor, Copilot, Gemini +more |
| **Pick it if** | You want the reference implementation of SDD | You want specs without the overhead | You already have a design doc and want it torn apart | Several people and agents work on one repo |

### Spec Kit

[github/spec-kit](https://github.com/github/spec-kit) ![stars](https://img.shields.io/github/stars/github/spec-kit?style=flat-square&label=%E2%AD%90)

🏢 GitHub · 🤖 Copilot, Claude Code and many more (pick with `--integration`)

GitHub's open-source toolkit for spec-driven development. It gives agents structured processes with templates and documented outcomes: a feature goes from spec to plan, implementation and convergence. A bug goes from cause to scoped fix to verification.

<details>
<summary>Install</summary>

```bash
uv tool install specify-cli
specify init my-project --integration copilot   # use your agent's key
```

</details>

### Elephant-Goldfish Model

[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) ![stars](https://img.shields.io/github/stars/google/elephant-goldfish-model?style=flat-square&label=%E2%AD%90)

🏢 Google · 🤖 Claude Code, Codex, Antigravity

From Google: **design with an elephant, review with a goldfish.** The Elephant holds your project context and drafts the spec. Goldfish reviewers then check it *without* the earlier conversation, so they catch unstated assumptions and blind spots. It can also report where your design docs have drifted from the code.

<details>
<summary>Install (Claude Code)</summary>

```bash
claude plugin marketplace add google/elephant-goldfish-model
claude plugin install egm@egm
# try: /egm:egm-review docs/designs/my-design.md
```

</details>

**Best for:** design docs and PR plans that need a fresh-eyes review.

### OpenSpec

[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) ![stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=%E2%AD%90)

🤖 30+ agents

Lightweight spec-driven development. You and the agent agree on a change proposal first, then build against it. It's lighter than Spec Kit and works on existing codebases.

<details>
<summary>Install</summary>

```bash
npm install -g @fission-ai/openspec@latest
```

</details>

### Task Master

[eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) ![stars](https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=flat-square&label=%E2%AD%90)

🔑 model API key (not needed if it runs through Claude Code) · 🤖 any MCP client

A task-management system for AI-driven development. It breaks a project into tasks your agent works through one at a time. It runs as an MCP server in Claude Code, Cursor, Windsurf and others.

<details>
<summary>Install</summary>

```bash
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

</details>

### Spec Kitty

[spec-kitty/spec-kitty](https://github.com/spec-kitty/spec-kitty) ![stars](https://img.shields.io/github/stars/spec-kitty/spec-kitty?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, Copilot, Gemini, Windsurf, OpenCode +more

Spec-driven development with **team governance**. Specs say what to build, and a Charter enforces how, across whichever agent each teammate uses.

<details>
<summary>Install</summary>

```bash
pipx install spec-kitty-cli
```

</details>

---

## 3. Code

Skills that make day-to-day coding sharper.

### Matt Pocock's Skills

[mattpocock/skills](https://github.com/mattpocock/skills) ![stars](https://img.shields.io/github/stars/mattpocock/skills?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Copilot, Gemini CLI, or any agent by copying the files

"Skills for real engineers." Small, sharp tools you call by name:

- `/tdd`: red-green-refactor, one vertical slice at a time
- `/diagnosing-bugs`: a reproduce, minimize, hypothesize, instrument, fix loop
- `/to-spec` and `/to-tickets`: turn a chat into a spec, then into tickets
- `/implement`: build from tickets, then review before committing
- `/prototype`, `/domain-modeling`, `/retro` and more

<details>
<summary>Install (Claude Code)</summary>

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```

Run `/setup-matt-pocock-skills` once per repo.

</details>

### Ponytail

[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) ![stars](https://img.shields.io/github/stars/DietrichGebert/ponytail?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex and 18 more agents

"Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote." It steers the agent toward the smallest change that works.

<details>
<summary>Install (Claude Code)</summary>

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

</details>

**Best for:** agents that over-engineer or rewrite things nobody asked them to.

### Modern Web Guidance

[GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) ![stars](https://img.shields.io/github/stars/GoogleChrome/modern-web-guidance?style=flat-square&label=%E2%AD%90)

🏢 Google Chrome, with the Edge, Firefox and MDN teams · 🤖 Claude Code, Codex, Copilot CLI, Antigravity, or any skills agent

Models learned the web from years of legacy code, so they reach for heavy JavaScript and polyfills where the browser now has a native answer. This skill feeds the agent short, expert-written guides on 269 modern web features (popovers, anchor positioning, view transitions, container queries and more), with browser support data. It can also scan a codebase for legacy patterns: `legacy-scan .`

<details>
<summary>Install</summary>

```bash
npx modern-web-guidance@latest install   # interactive; needs Node 22+
```

In Claude Code you can use the plugin instead: `/plugin marketplace add GoogleChrome/modern-web-guidance`, then `/plugin install modern-web-guidance@googlechrome`.

</details>

**Best for:** front-end work: lighter, faster, more accessible pages.

**Heads-up:** it sends anonymous usage data to Google, including the search queries your agent makes. Turn it off with `export DISABLE_TELEMETRY=1`. If you installed it from Claude Code's built-in plugin directory, switch to the `googlechrome` marketplace above: the built-in copy is stuck on an old version ([details](https://github.com/GoogleChrome/modern-web-guidance-src/issues/3533)).

### Anthropic Skills

[anthropics/skills](https://github.com/anthropics/skills) ![stars](https://img.shields.io/github/stars/anthropics/skills?style=flat-square&label=%E2%AD%90)

🏢 Anthropic · 🤖 Claude Code, Claude.ai, Claude API

Anthropic's official skills. They include example skills (web-app testing, MCP server generation, art and more) and the **document skills** behind Claude's Word, PDF, PowerPoint and Excel features. It's the reference for how skills should be written.

<details>
<summary>Install</summary>

```
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

</details>

---

## 4. Context and memory

Give the agent the right information: current docs, your codebase and what happened last session.

### Context7

[upstash/context7](https://github.com/upstash/context7) ![stars](https://img.shields.io/github/stars/upstash/context7?style=flat-square&label=%E2%AD%90)

🏢 Upstash · 🔑 free key, *optional* (higher rate limits) · 🤖 any MCP client, or CLI + skills

LLMs are trained on year-old docs, so they hallucinate APIs. Context7 pulls **up-to-date, version-specific docs and code examples** straight from the source into your agent. Add "use context7" to a prompt.

<details>
<summary>Install</summary>

```bash
npx ctx7 setup
```

Signs you in, creates the key and installs the skill or MCP server for your agent.

</details>

**Best for:** anyone using fast-moving libraries (Next.js, Flutter, Supabase…).

### claude-mem

[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) ![stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, OpenCode +11 more

Persistent memory across sessions. A second agent takes notes while yours works, and the next session starts with a short index of what matters. Your second session in a project opens already knowing the first. Memory stays on your machine in `~/.claude-mem`.

<details>
<summary>Install</summary>

```bash
npx claude-mem install
```

</details>

**Heads-up:** the installer asks you to sign in and offers a paid "observer" with a 30-day trial (it asks for a payment method). To skip both and run memory on your own plan, install with `CLAUDE_MEM_ONLINE_OPTIN=false npx claude-mem install`. Anonymous analytics are on by default; turn them off with `npx claude-mem telemetry disable`.

### Graphify

[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) ![stars](https://img.shields.io/github/stars/Graphify-Labs/graphify?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Cursor, Codex, Gemini CLI, Copilot +20 more

Turns a codebase, along with its docs, SQL schemas, configs and PDFs, into a queryable knowledge graph. Code is parsed locally with tree-sitter: deterministic, no LLM, nothing leaves your machine. It explains every edge and needs no vector store.

<details>
<summary>Install</summary>

```bash
uv tool install graphifyy && graphify install
# then in your agent: /graphify .
```

</details>

**Best for:** joining a new project or contributing to a big open-source repo.

### Serena

[oraios/serena](https://github.com/oraios/serena) ![stars](https://img.shields.io/github/stars/oraios/serena?style=flat-square&label=%E2%AD%90)

🤖 any MCP client

"The IDE for your coding agent." An MCP toolkit with **symbol-level** code search, editing and refactoring, so the agent doesn't have to grep and edit line numbers. It helps most in large codebases.

<details>
<summary>Install</summary>

```bash
uv tool install -p 3.13 serena-agent
```

</details>

**Heads-up:** the authors say *not* to install it from MCP marketplaces, which have outdated commands.

### Repomix

[yamadashy/repomix](https://github.com/yamadashy/repomix) ![stars](https://img.shields.io/github/stars/yamadashy/repomix?style=flat-square&label=%E2%AD%90)

🤖 any agent or chat (CLI, or as an MCP server)

Packs an entire repo into one AI-friendly file you can paste into any chat. For a browsable version, see Karpathy's [rendergit](#rendergit).

<details>
<summary>Install</summary>

```bash
npx repomix@latest
```

</details>

---

## 5. Design and UI

Agents default to purple gradients and identical card grids. These skills fix that.

### Impeccable

[pbakaus/impeccable](https://github.com/pbakaus/impeccable) ![stars](https://img.shields.io/github/stars/pbakaus/impeccable?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Cursor, Codex, Copilot, Gemini CLI +more

"The design vocabulary for your coding agent." Steer with `polish` and `bolder`, review with `critique` and `audit`. It includes a CLI detector that catches AI-slop patterns and can run in CI.

<details>
<summary>Install</summary>

```bash
npx impeccable install
npx impeccable detect src/
```

</details>

### Taste Skill

[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) ![stars](https://img.shields.io/github/stars/Leonxlnx/taste-skill?style=flat-square&label=%E2%AD%90)

🤖 any skills agent

Art direction for agents. It works from reference images and checks the result in a real browser. Needs Node 22+ and Chrome, Edge or Chromium.

<details>
<summary>Install</summary>

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

</details>

### Hallmark

[Nutlope/hallmark](https://github.com/Nutlope/hallmark) ![stars](https://img.shields.io/github/stars/Nutlope/hallmark?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, OpenCode

An anti-AI-slop design skill with a `sloplint` checker.

<details>
<summary>Install</summary>

```bash
npx skills add nutlope/hallmark -g
```

</details>

### Emil Kowalski's Skills

[emilkowalski/skills](https://github.com/emilkowalski/skills) ![stars](https://img.shields.io/github/stars/emilkowalski/skills?style=flat-square&label=%E2%AD%90)

🤖 any skills agent

UI and animation craft from a design engineer who worked at Vercel and Linear. They fix small mistakes that add up, like `ease-in` on enter animations or solid borders where a soft shadow belongs.

<details>
<summary>Install</summary>

```bash
npx skills@latest add emilkowalski/skills
```

</details>

### Astryx

[meta/astryx](https://github.com/meta/astryx) ![stars](https://img.shields.io/github/stars/meta/astryx?style=flat-square&label=%E2%AD%90)

🏢 Meta · 🤖 any agent that reads `AGENTS.md` or `CLAUDE.md` · React 19+

Not a skill but a design system built for agents to use. It grew inside Meta over eight years and powers 13,000+ of its apps: 150+ accessible components, seven themes, dark mode and templates. `init` writes the Astryx guide into your `AGENTS.md`/`CLAUDE.md`, and the CLI serves component docs, so your agent builds from real components instead of inventing new ones. It's in beta.

<details>
<summary>Install</summary>

```bash
npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
npm install -D @astryxdesign/cli
npx @astryxdesign/cli init
```

</details>

**Best for:** new React apps where you want a consistent UI without designing every screen.

---

## 6. Test and debug

Let the agent see and drive the running app.

### Which browser tool?

| | [Chrome DevTools for Agents](#chrome-devtools-for-agents) | [Playwright CLI](#playwright-cli) | [Playwright MCP](#playwright-mcp) |
|---|---|---|---|
| **From** | 🏢 Chrome team | 🏢 Microsoft | 🏢 Microsoft |
| **Browsers** | Chrome only | Chrome, Edge, Firefox, WebKit | Chrome, Edge, Firefox, WebKit |
| **Runs as** | MCP server, CLI or skills | CLI + skills | MCP server |
| **Token use** | Depends on mode (MCP or CLI) | Lowest: no tool schemas or page trees in context | Higher: loads tool schemas and accessibility snapshots |
| **Stands out for** | Performance traces, network, console with source maps | Everyday coding: record tests, check selectors, screenshots | Long exploratory or self-healing test loops that keep browser state |
| **Pick it if** | You're chasing a front-end bug or a slow page | You want the default for coding agents | You run long autonomous browser sessions |

Microsoft itself recommends the CLI over MCP for coding agents because it's lighter on tokens.

### Chrome DevTools for Agents

[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ![stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=flat-square&label=%E2%AD%90)

🏢 Google (Chrome team) · 🤖 any MCP client, or CLI

Your agent controls and inspects a live Chrome browser: performance traces, network requests, console and screenshots. It's available as an MCP server, a CLI and skills.

<details>
<summary>Install (Claude Code)</summary>

```
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
/plugin install chrome-devtools-mcp@chrome-devtools-plugins
```

</details>

**Best for:** debugging front-end bugs and performance.

**Heads-up:** performance tools may send trace URLs to Google's CrUX API for real-user data. Turn that off with `--no-performance-crux`.

### Playwright CLI

[microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) ![stars](https://img.shields.io/github/stars/microsoft/playwright-cli?style=flat-square&label=%E2%AD%90)

🏢 Microsoft · 🤖 any coding agent

Microsoft's recommended way for coding agents to use Playwright: a CLI plus skills. It uses fewer tokens than MCP because it doesn't load big tool schemas or accessibility trees into context. It records and generates tests, inspects selectors and takes screenshots.

<details>
<summary>Install</summary>

```bash
npm install -g @playwright/cli@latest
```

</details>

### Playwright MCP

[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) ![stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=flat-square&label=%E2%AD%90)

🏢 Microsoft · 🤖 any MCP client

Browser automation over MCP using the accessibility tree, so no vision model is needed. Use it for long exploratory or self-healing test loops. For everyday coding, the CLI above is lighter.

<details>
<summary>Install</summary>

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

</details>

> For TDD and bug diagnosis skills, see [Matt Pocock's Skills](#matt-pococks-skills) (`/tdd`, `/diagnosing-bugs`).

---

## 7. Review and ship

Check what the agent built before it ships.

### Claude Code Action

[anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) ![stars](https://img.shields.io/github/stars/anthropics/claude-code-action?style=flat-square&label=%E2%AD%90)

🏢 Anthropic · 🔑 repo secret (the installer sets it up) · 🤖 GitHub Actions

Claude in your GitHub PRs and issues. Mention it to review a PR, answer questions about the code or implement fixes and features.

<details>
<summary>Install</summary>

```
# inside Claude Code (needs repo admin):
/install-github-app
```

</details>

### Open Code Review

[alibaba/open-code-review](https://github.com/alibaba/open-code-review) ![stars](https://img.shields.io/github/stars/alibaba/open-code-review?style=flat-square&label=%E2%AD%90)

🏢 Alibaba · 🔑 model API key, *optional* (not needed in delegation mode) · 🤖 Claude Code, Codex, Cursor, Kimi Code, or any skills agent

Alibaba's internal AI code reviewer, used by tens of thousands of its developers for two years, now open source. Plain code decides which files get reviewed and groups related ones, and the agent only does the reviewing, so it doesn't skip files on a big diff or point at the wrong line. On Alibaba's benchmark of 200 real PRs, it beat Claude Code on precision and F1 with the same model and used about 1/9 of the tokens. It finds fewer issues in total: it's tuned for less noise. It reviews diffs (`ocr review`) or whole folders (`ocr scan`).

<details>
<summary>Install</summary>

```bash
npx skills add alibaba/open-code-review
# or the CLI on its own:
npm install -g @alibaba-group/open-code-review
```

No API key? Pick the `open-code-review-delegate` skill: your own agent does the review, following OCR's pipeline. Needs Git 2.41+.

</details>

**Best for:** large PRs, and teams tired of noisy AI review comments.

### Plannotator

[backnotprop/plannotator](https://github.com/backnotprop/plannotator) ![stars](https://img.shields.io/github/stars/backnotprop/plannotator?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro, Droid, Amp, Pi

Review your agent's work in the browser, the way you'd review a teammate's. When the agent finishes a plan, it opens in a local page where you highlight lines, comment and send the feedback straight back. It does the same for diffs, GitHub PRs and GitLab MRs, HTML pages and even your running app on `localhost`. For a big diff, **Guide** sorts the change into chapters, the most important first.

<details>
<summary>Install (Claude Code)</summary>

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

Then in Claude Code: `/plugin marketplace add backnotprop/plannotator`, `/plugin install plannotator@plannotator`, and restart. Other agents: see the [setup table](https://github.com/backnotprop/plannotator#install).

</details>

**Best for:** reading a plan properly before the agent starts coding.

**Heads-up:** you can share a plan as a link. Large shares are uploaded encrypted and expire after 7 days, but anyone with the full link can read them. Turn sharing off with `PLANNOTATOR_SHARE=disabled`.

### GitHub MCP Server

[github/github-mcp-server](https://github.com/github/github-mcp-server) ![stars](https://img.shields.io/github/stars/github/github-mcp-server?style=flat-square&label=%E2%AD%90)

🏢 GitHub · 🔑 GitHub token · 🤖 any MCP client

GitHub's official MCP server. Agents can read repos, manage issues and PRs, check Actions runs, investigate failing builds and review Dependabot alerts.

<details>
<summary>Install</summary>

```bash
claude mcp add github -e GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_PAT -- \
  docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server
```

</details>

### Claude Code Security Review

[anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) ![stars](https://img.shields.io/github/stars/anthropics/claude-code-security-review?style=flat-square&label=%E2%AD%90)

🏢 Anthropic · 🔑 Claude API key · 🤖 GitHub Actions

A GitHub Action that security-reviews every PR. It reads only the changed files, comments its findings on the PR and filters out false positives. Setup is a workflow file; see the README.

---

## 8. Security

### SkillSpector

[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) ![stars](https://img.shields.io/github/stars/NVIDIA/SkillSpector?style=flat-square&label=%E2%AD%90)

🏢 NVIDIA · 🔑 *optional*, for the deeper LLM pass · 🤖 standalone CLI, scans skills for any agent

NVIDIA's security scanner for agent skills. Skills run with your agent's trust, and in NVIDIA's dataset **26.1% had vulnerabilities and 5.2% looked malicious.** SkillSpector checks 71 patterns in 17 categories, including prompt injection, data exfiltration, privilege escalation, supply chain and memory poisoning. It gives a 0–100 risk score with JSON, Markdown or SARIF output.

<details>
<summary>Install</summary>

```bash
uv tool install --python 3.13 git+https://github.com/NVIDIA/skillspector.git
skillspector scan ./some-skill/ --no-llm   # static scan, no API key needed
```

</details>

**Best for:** everyone. Run it before installing any skill from someone you don't know.

### Trail of Bits Skills

[trailofbits/skills](https://github.com/trailofbits/skills) ![stars](https://img.shields.io/github/stars/trailofbits/skills?style=flat-square&label=%E2%AD%90)

🏢 Trail of Bits · 🤖 Claude Code, Codex

Security research, vulnerability detection and audit workflows from one of the best-known security firms.

<details>
<summary>Install</summary>

```
/plugin marketplace add trailofbits/skills
/plugin menu
```

</details>

### Cloudflare Security Audit

[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) ![stars](https://img.shields.io/github/stars/cloudflare/security-audit-skill?style=flat-square&label=%E2%AD%90)

🏢 Cloudflare · 🤖 any skills agent

A multi-phase security audit with independently verified, machine-readable findings.

<details>
<summary>Install</summary>

```bash
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

</details>

### Claude Red

[SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) ![stars](https://img.shields.io/github/stars/SnailSploit/Claude-Red?style=flat-square&label=%E2%AD%90)

🤖 Claude Code

Offensive-security skills for pentesters, one per attack surface.

> [!WARNING]
> Only for systems you own or are explicitly authorized to test.

---

## 9. Deploy and infrastructure

Official skills from the platforms themselves. All 🏢, all install with `npx skills`, so they work in any skills agent.

| Tool | What it does | Install |
|---|---|---|
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | `vercel-optimize` audits cost, performance and caching from real metrics; `web-design-guidelines` reviews UI | `npx skills add vercel-labs/agent-skills` |
| [Supabase Agent Skills](https://github.com/supabase/agent-skills) | Supabase and Postgres best practices for 18+ agents | `npx skills add supabase/agent-skills` |
| [HashiCorp Agent Skills](https://github.com/hashicorp/agent-skills) | 16 Terraform and 4 Packer skills, including style guides | `npx skills add hashicorp/agent-skills` |

### AX (Agent Executor)

[google/ax](https://github.com/google/ax) ![stars](https://img.shields.io/github/stars/google/ax?style=flat-square&label=%E2%AD%90)

🏢 Google · runs on Kubernetes

Google's runtime for running large numbers of sandboxed agent tasks on Kubernetes. You declare a `Workspace`, a `Task` and a `Model` in YAML, then `ax apply`. It's for building agent platforms, not for everyday coding. It's in heavy development.

---

## 10. Cost and usage

### TokenEconomizer

[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer) ![stars](https://img.shields.io/github/stars/microsoft/TokenEconomizer?style=flat-square&label=%E2%AD%90)

🏢 Microsoft Research · 🤖 Claude Code, Codex, Copilot CLI, Pi (OpenCode, Cursor and more experimental)

From Microsoft Research and UC Berkeley. It makes agents cheaper in repos you work in often, without changing the agent. On SWE-Bench it cut mean cost by **18.4–30.9%** across five agent–model combinations, and Pass@1 went *up* in 4 of 5. It works in three ways:

- **Micro-skills** remember repo facts the agent keeps rediscovering (which test command works, what must build first).
- **Tool pruning** stops loading tools you never use.
- **A loop guard** steps in when a turn is stuck repeating the same failures.

Everything it learns stays local in `~/.tokeneconomizer`.

<details>
<summary>Install (Claude Code)</summary>

```bash
git clone https://github.com/microsoft/TokenEconomizer.git
claude plugin marketplace add "$PWD/TokenEconomizer"
claude plugin install tokeneconomizer@tokeneconomizer
```

Keep the clone in place: the plugin runs from it.

</details>

### ccusage

[ccusage/ccusage](https://github.com/ccusage/ccusage) ![stars](https://img.shields.io/github/stars/ccusage/ccusage?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, OpenCode, Copilot CLI, Gemini CLI

Daily, weekly, monthly and per-session token and cost reports from your agent CLIs' local data. You'll finally know where the money goes.

<details>
<summary>Install</summary>

```bash
npx ccusage@latest
```

</details>

---

## 11. Docs, diagrams and visuals

### Visual Explainer

[nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) ![stars](https://img.shields.io/github/stars/nicobailon/visual-explainer?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Cursor, OpenCode, Antigravity

Turns terminal walls of text into styled HTML pages: architecture diagrams, `/diff-review`, `/plan-review`, data tables and slide decks.

<details>
<summary>Install (Claude Code)</summary>

```
/plugin marketplace add nicobailon/visual-explainer
/plugin install visual-explainer@visual-explainer-marketplace
```

</details>

### Diagram Design

[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) ![stars](https://img.shields.io/github/stars/cathrynlavery/diagram-design?style=flat-square&label=%E2%AD%90)

🤖 any skills agent, incl. Claude Code, Cursor, Codex, Copilot, Gemini CLI

Editorial-quality diagrams: 45 types as self-contained HTML + SVG. "No Mermaid slop."

<details>
<summary>Install</summary>

```bash
npx skills add cathrynlavery/diagram-design
```

</details>

### Anatomy

[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) ![stars](https://img.shields.io/github/stars/wheresryan22/anatomy?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, OpenCode, Antigravity

Interactive isometric illustrations of machines and complex systems, rendered as SVG with optional WebGL effects.

<details>
<summary>Install</summary>

```bash
npx skills add wheresryan22/anatomy -g
```

</details>

### /brag

[latent-spaces/brag](https://github.com/latent-spaces/brag) ![stars](https://img.shields.io/github/stars/latent-spaces/brag?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, OpenCode, Antigravity, or any skills agent

"You built it. Now brag." Turns the project you just made into a short launch video, with music, motion and share copy, in one command. You get a `brag-output/` folder with the plan, the copy and `brag.mp4`. Steer the tone with `/brag --tone "..."`.

<details>
<summary>Install (Claude Code)</summary>

```
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
```

Other agents: `npx skills add https://github.com/latent-spaces/brag --skill brag`. Needs Node 22+, FFmpeg and the Hyperframes CLI (`npx hyperframes doctor` checks it).

</details>

**Best for:** launch posts for side projects.

---

## 12. Writing

### Humanizer

[blader/humanizer](https://github.com/blader/humanizer) ![stars](https://img.shields.io/github/stars/blader/humanizer?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, or any skills agent

Makes AI-written text sound like a person wrote it, without changing what it says. It's built on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide: it cuts the "I'm thrilled to announce 🚀" tone, the em-dash habit and the filler. In a blind test, judges preferred its rewrite 16 out of 16 times. It edits for readers and doesn't try to evade AI detectors.

<details>
<summary>Install (Claude Code)</summary>

```
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

Other agents: `npx skills add blader/humanizer --global --agent codex` (swap in your agent).

</details>

**Best for:** READMEs, PR descriptions, docs, emails and LinkedIn posts.

### Marketing Skills

[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) ![stars](https://img.shields.io/github/stars/coreyhaines31/marketingskills?style=flat-square&label=%E2%AD%90)

🤖 any skills agent

Copywriting, SEO, conversion optimization (CRO), analytics and growth skills for founders and technical marketers.

<details>
<summary>Install</summary>

```bash
npx skills add coreyhaines31/marketingskills --skill copywriting
```

</details>

### Anthropic Document Skills

[anthropics/skills](https://github.com/anthropics/skills) ![stars](https://img.shields.io/github/stars/anthropics/skills?style=flat-square&label=%E2%AD%90)

🏢 Anthropic · 🤖 Claude Code

The skills behind Claude's file creation: write and edit **Word, PDF, PowerPoint and Excel** files from your agent.

<details>
<summary>Install</summary>

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

</details>

---

## 13. Mobile

Official skills from the framework teams, plus a way for your agent to drive the running app.

| Tool | What it does | Install |
|---|---|---|
| 🏢 [Flutter Agent Plugins](https://github.com/flutter/agent-plugins) | From the Flutter team: widget and integration tests, responsive layouts, layout-overflow fixes, architecture, JSON serialization | [docs.flutter.dev/ai/get-started](https://docs.flutter.dev/ai/get-started) |
| 🏢 [Dart Skills](https://github.com/dart-lang/skills) | From the Dart team; pair them with the above | `npx skills add dart-lang/skills --skill '*' --agent universal --yes` |
| 🏢 [Expo Skills](https://github.com/expo/skills) | From the Expo team: build, deploy, upgrade and debug Expo and React Native apps | `npx skills@latest add expo/skills --skill '*'` |

### Marionette MCP

[leancodepl/marionette_mcp](https://github.com/leancodepl/marionette_mcp) ![stars](https://img.shields.io/github/stars/leancodepl/marionette_mcp?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Cursor, Codex, Gemini CLI, Copilot, or any MCP client

"If you know Playwright MCP: this is that, for Flutter." Your agent connects to the Flutter app you run in debug mode, then sees the screen, taps, types, scrolls, reads the logs and hot reloads. It can also reach system dialogs outside Flutter on Android and iOS, and turn a run that worked into [Patrol](https://github.com/leancodepl/patrol) tests. From LeanCode, the makers of Patrol.

<details>
<summary>Install (Claude Code)</summary>

```bash
flutter pub add marionette_flutter   # then call MarionetteBinding.ensureInitialized() in debug builds
dart pub global activate marionette_mcp
claude mcp add --transport stdio marionette -- marionette_mcp
```

Run the app with `flutter run` and give the agent the `ws://…/ws` URL it prints. Using your own design system instead of Flutter's widgets? It needs [one config step](https://marionette.leancode.co/docs/configure/) first.

</details>

**Best for:** letting the agent check its own UI changes instead of you tapping through the app.

---

## 14. Career

### career-ops

[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) ![stars](https://img.shields.io/github/stars/career-ops-hq/career-ops?style=flat-square&label=%E2%AD%90)

🤖 Claude Code, Codex, Gemini CLI, OpenCode +more; runs on free and local models too

An open-source job-search agent. It scans job boards, scores each role 1–5 against your CV, tailors an ATS-friendly resume and cover letter, preps you for interviews and tracks applications. You still press Submit.

<details>
<summary>Install</summary>

```bash
npx @santifer/career-ops init
```

</details>

### Multi-Claude career skills

🤖 Claude Code

Small skills by [alexyc9381](https://github.com/alexyc9381) that run a panel of Claudes:

| Skill | What it does |
|---|---|
| [hiring-panel](https://github.com/alexyc9381/hiring-panel-skill) | 7 Claudes try to reject your resume, then rebuild it |
| [mock-interview](https://github.com/alexyc9381/mock-interview-skill) | Interviews you from a real job post and grades every answer |
| [hunter](https://github.com/alexyc9381/hunter-skill) | Finds and scores jobs that fit you |
| [linkedin-roast](https://github.com/alexyc9381/linkedin-roast-skill) | Roasts your LinkedIn, then fixes it |
| [client-room](https://github.com/alexyc9381/client-room-skill) | Finds paying clients for freelancers |

---

## 15. Learning

### LearnHarness

[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness) ![stars](https://img.shields.io/github/stars/amosblomqvist/learnharness?style=flat-square&label=%E2%AD%90)

Desktop app · bring your own model: an API key, a supported subscription or your Claude Code CLI

An agent harness for learning hard things. It measures where your understanding ends, plans a path to your goal, teaches one reasoning step at a time and keeps a knowledge graph across sessions. Download it from [learnharness.ai](https://learnharness.ai).

To understand the models themselves, see [Karpathy's learning path](#learn-how-llms-actually-work).

---

## Find more

- [vercel-labs/skills](https://github.com/vercel-labs/skills) is the `npx skills` CLI. Search with `npx skills find`, or browse [skills.sh](https://skills.sh).
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) has Anthropic's own Claude Code plugins. Browse them in Claude Code with `/plugin` → Discover.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) is a large curated list of Claude Code resources.
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) and [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) are curated skill lists.

---

## Write your own skill

The fastest way to learn is to write one:

```markdown
---
name: commit-message
description: Write a conventional commit message for the staged changes. Use when the user asks to commit or write a commit message.
---

1. Run `git diff --staged` and read the changes.
2. Pick a type: feat, fix, docs, refactor, test or chore.
3. Write a subject under 72 characters in the imperative mood.
4. Add a body only if the *why* isn't obvious from the diff.
```

Save it as `~/.claude/skills/commit-message/SKILL.md` and start a new session.

- **The description is the trigger.** Say *what* the skill does and *when* to use it.
- **Keep `SKILL.md` short.** Move long references into separate files.
- **Write steps, not essays.** Agents follow checklists better than prose.
- **Study the best:** [anthropics/skills](https://github.com/anthropics/skills) and [mattpocock/skills](https://github.com/mattpocock/skills).

---

## Contributing

Found something that made your agent noticeably better? [Suggest a tool](https://github.com/uveshm003/ai-dev-toolkit/issues/new?template=suggest-a-tool.yml) or open a PR. Spotted a dead link or a wrong install command? [Report it](https://github.com/uveshm003/ai-dev-toolkit/issues/new?template=broken-link.yml). See [CONTRIBUTING.md](CONTRIBUTING.md).

Links are checked automatically every week, and archived repos get flagged.

If this helped you, a ⭐ helps others find it.

## License

[CC0 1.0](LICENSE). This list is in the public domain. Each linked project has its own license.
