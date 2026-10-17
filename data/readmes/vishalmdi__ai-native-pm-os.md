# AI-Native PM OS
### Your Complete Product Management Operating System — Built with Claude Code

---

> **Not a tutorial. A real, deployable work infrastructure.**
> By the time you finish, you won't just know Claude Code — you'll have a working PM command center you use every day.

---

## What This Course Is

Most AI courses teach you to prompt. This course teaches you to **operate**.

The **AI-Native PM OS** is a structured, hands-on program that transforms Claude Code into your personal product management infrastructure — a living system that handles research synthesis, PRD generation, stakeholder prep, data analysis, and team handoffs, all within a single command-line environment.

**Format:** Interactive modules inside Claude Code + reference guides + weekly community challenges  
**Time:** ~40–50 hours total | 30-min lessons | 100% self-paced  
**Stack:** Claude Code (required) | Meridian (your practice B2B SaaS company)

---

## The Agents & Workflows You Will Build

By Module 10, your Claude Code environment won't just be a chatbot. You will have built a suite of **specialized, autonomous PM agents and workflows**, including:

- 🕵️ **The Competitive Intelligence Agent:** Runs daily sweeps of competitor pricing pages and documentation, dropping a formatted threat-analysis memo into your Slack.
- 📊 **The "Peep-Free" Analytics Agent:** Enforces disciplined A/B test analysis, refusing to output metrics until your pre-registered sample size is reached.
- 📝 **The PRD-to-Jira Pipeline Agent:** Reads your 6-page PRD, identifies edge cases you missed, and automatically generates Jira epics and stories directly into your backlog via MCP.
- 🗣️ **The Customer Voice Synthesizer:** Reads 500 Zendesk tickets via Google Workspace/Notion MCP, clusters the complaints by Jobs-to-be-Done, and generates a prioritized discovery brief.
- 🎨 **The "Vibe Coder" Prototyper:** Takes a half-baked PRD flow and instantly spins up a clickable HTML prototype you can send to your CTO on Vercel.
- 🛡️ **The Board-Level Executive Agent:** Audits your OKR updates against the "Anti-Slop" guidelines, aggressively cutting PM jargon to produce a crisp narrative the CEO will actually read.

You aren't just learning to prompt. You are building these agents.

---

## The Meridian Company

Throughout this course, you'll work with **Meridian** — a fictional but richly detailed B2B SaaS company. Meridian sells a workflow orchestration platform to mid-market operations teams. It has:

- A defined product strategy, OKRs, and roadmap
- Realistic user research data, support tickets, and analytics
- Stakeholder personas: skeptical CTO, growth-obsessed CEO, cautious CFO
- A sales motion, competitive landscape, and pricing model

Everything you build in this course will be grounded in Meridian's context. By Module 10, your deliverables will look like they came from a senior PM at a real company.

---

## Course Map

| Module | Title | Hours | Core Skill |
|--------|-------|-------|-----------|
| 0 | Setup & Orientation | 3–4h | Environment, mental model |
| 1 | CLAUDE.md Mastery | 3–4h | Context engineering |
| 2 | File & Memory Operations | 3–4h | Workspace architecture |
| 3 | PRDs & Specs | 4–5h | Document generation |
| 4 | Data & Analytics | 4–5h | Metrics workflows |
| 5 | Research & Discovery | 4–5h | Synthesis at scale |
| 6 | Stakeholder & Strategy | 4–5h | Executive artifacts |
| 7 | MCP & Tool Integrations | 5–6h | Real-stack connections |
| 8 | Team Workflows | 3–4h | Collaboration systems |
| 9 | Vibe Coding for PMs | 5–6h | Prototype + deploy |
| 10 | Capstone Project | 6–8h | Portfolio artifact |

---

## Prerequisites

| Tool | Required | Install |
|------|----------|---------|
| An AI coding CLI | ✅ Yes | Claude Code, Codex CLI, Gemini CLI, Aider, or Cursor — see [agent compatibility](#agent-compatibility) below |
| Active LLM subscription/API key | ✅ Yes | Anthropic / OpenAI / Google / your provider |
| Python 3.8+ | Optional | https://python.org/downloads — only needed for the progress dashboard |
| Git | Optional | https://git-scm.com — installer falls back to ZIP download if absent |

## Agent compatibility

The course was originally written for **Claude Code** and that is still the most polished experience (slash commands work natively). It now also runs in any agent that respects the `AGENTS.md` convention or can be pointed at the project's architectural contract.

| Agent | Reads first | Slash commands | Notes |
|---|---|---|---|
| Claude Code | `CLAUDE.md` | Native | Recommended — full lesson map + model recommendations |
| Codex CLI | `AGENTS.md` | As natural language | Use phrasings like "load lesson 0-1" or "I'm done" |
| Gemini CLI | `GEMINI.md` → `AGENTS.md` | As natural language | Same as Codex |
| Aider | `AGENTS.md` (must `/read` it explicitly at session start — Aider does not auto-discover) | As natural language | Same as Codex once loaded |
| Cursor | `.cursor/rules/ai-native-pm-os.mdc` | As natural language | Auto-loads on project open |
| Continue / Cline / generic LLM agent | `AGENTS.md` | As natural language | Same as Codex |
| Custom agent (Anthropic SDK, OpenAI Agents SDK, LangChain) | Pass `AGENTS.md` + `ai-native-pm-os.speq` into the system prompt | n/a | Full example in the [wiki](./wiki/How-To-Use-Different-Agent.md) |

The architectural source of truth for **all** agents is [`ai-native-pm-os.speq`](./ai-native-pm-os.speq) — a closed-world, machine-readable contract that pins down the course's vocabulary, layers, contracts, and flows so every agent produces identical behavior.

---

## Why this matters (and how it works)

The course's whole premise is **context engineering** — that one great `CLAUDE.md` is worth more than 50 prompts. Modules 0–2 teach this directly: a well-written briefing file is the most leveraged thing a PM can build.

That premise has a hidden assumption: the briefing file is in **natural language**. Natural-language briefings work because LLMs are fluent, but they have a known failure mode — **drift**. The same paragraph means slightly different things to Claude Sonnet 4.6, GPT-5, and Gemini 2.5 Pro. They infer different defaults from the same words. On a small project that's tolerable. On a 63-lesson course with a fixed practice company (Meridian), strict folder layout, and progress state, drift compounds fast.

This course closes the gap with two complementary additions:

### 1. A `.speq` file as the architectural source of truth

[`ai-native-pm-os.speq`](./ai-native-pm-os.speq) is a machine-readable, **closed-world** contract for the course's architecture. It uses [SpeQ](https://github.com/speq-ai), a small DSL whose entire premise is "anything not declared does not exist." It pins down:

- **Vocabulary** — the canonical name for every concept (`Lesson`, `Module`, `Meridian`, `ProgressLedger`, `ClaudeOutputs`, `Capstone`, `McpConnector`, `CourseGuide`, `PmVault`, `AgentContextFile`, `CourseMode`). Synonyms become contract violations.
- **Layers** — `COURSE_CONTENT`, `AGENT_RUNTIME` (the only `BOUNDARY external`), `PROGRESS_LEDGER`, `CLAUDE_OUTPUTS`, `PROGRESS_DASHBOARD`. Each layer has explicit `OWNS`, `CALLS`, and `NEVER` rules.
- **Contracts** — `lesson.completion REQUIRES user-confirmation`, `progress_ledger.write ALWAYS atomic`, `course_mode.outputs ALWAYS matches-active-mode`, etc. These are invariants every agent must honor.
- **Flows** — `lesson_completion`, `course_setup`, `capstone_graduation` with explicit step ordering, rollback, and timeouts.
- **Secrets** — env-var names scoped to `AGENT_RUNTIME`, never committed, never logged.

The result: two agents reading the same spec produce architecturally equivalent output. Concrete bugs the spec prevents:

| Without the spec | With the spec |
|---|---|
| Agent invents new entities ("let me create a `study_plan` for you") | `ENTITY` is closed-world; non-listed entities don't exist |
| Module 1 says "node", Module 5 says "step" — for the same concept | `VOCABULARY` makes synonym use a contract violation |
| Agent auto-marks a lesson complete after a checklist passes | `lesson.completion REQUIRES user-confirmation` blocks it |
| Agent edits a lesson file to "fix" student misunderstanding | `AGENT_RUNTIME NEVER modify_lesson_files_silently` blocks it |
| Test-mode artifacts pollute student outputs folder | `course_mode.outputs ALWAYS matches-active-mode` blocks it |
| Dashboard accidentally writes to `progress.json` | `PROGRESS_DASHBOARD NEVER write_to_progress_ledger` blocks it |

Crucially, **the course is about context engineering** — adding a `.speq` is the course walking the talk. Students learning about CLAUDE.md hierarchy in Module 1 can read the repo's own spec to see the next level of rigor.

### 2. Five entry-point files so any agent works

Different agents look for different files. The course ships one file per convention, all of which delegate to the spec and to `AGENTS.md`:

| File | Read by | Purpose |
|---|---|---|
| [`CLAUDE.md`](./CLAUDE.md) | Claude Code | Canonical for Claude Code; full lesson-ID map, slash commands, model recommendations |
| [`AGENTS.md`](./AGENTS.md) | Codex, Aider, Cursor, OpenAI Agents SDK, Continue, Cline, generic | Universal agent-neutral guide; slash commands ↔ natural language |
| [`GEMINI.md`](./GEMINI.md) | Gemini CLI | Thin pointer to `AGENTS.md` plus Gemini model picker notes |
| [`.cursor/rules/ai-native-pm-os.mdc`](./.cursor/rules/ai-native-pm-os.mdc) | Cursor | Auto-loads on project open; points at `AGENTS.md` |
| `AIDER.md` (not present) | Aider | Aider falls back to `AGENTS.md` automatically |

The behavior is **identical** across all agents. Only the entry point differs. `install.sh` and `setup.sh` auto-detect which CLI the student has installed (Claude Code, Codex, Gemini, Aider, or Cursor) and tailor the final-step instructions accordingly.

### How to dig deeper

The full system is documented in the **[wiki](./wiki/Home.md)**:

- [Why a `.speq` file](./wiki/Why-Speq.md) — extended rationale, drift modes, course-specific fit
- [Multi-agent support](./wiki/Multi-Agent-Support.md) — routing diagram, what differs per agent, onboarding new agents
- [Architecture overview](./wiki/Architecture-Overview.md) — layer diagram, flows, file system layout, secrets handling
- [How to update the spec](./wiki/How-To-Update-Spec.md) — when to bump the spec vs. just edit content; common validation errors
- [How to use a different agent](./wiki/How-To-Use-Different-Agent.md) — step-by-step setup for Claude Code, Codex, Gemini, Aider, Cursor, custom SDK
- [Troubleshooting](./wiki/Troubleshooting.md) — symptoms → causes → fixes
- [Glossary](./wiki/Glossary.md) — every binding term, with the synonyms each replaces

The shorter rationale lives at [`docs/SPEQ-RATIONALE.md`](./docs/SPEQ-RATIONALE.md).

### Continuous integration

Every PR runs [`.github/workflows/validate.yml`](./.github/workflows/validate.yml) which checks:

- **Spec validity** — `speq check ai-native-pm-os.speq` must pass
- **Shell script syntax** — `bash -n` on `install.sh`, `setup.sh`, `start-lesson.sh`, `test-mode.sh`, `scripts/*.sh`
- **Lesson parity** — every lesson ID in `progress.json` (when present), `CLAUDE.md` map, `AGENTS.md` lesson order, and `setup.sh` JSON template must match the files actually on disk in `module-X/`
- **Markdown links** — internal cross-references in `README.md`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `docs/`, and `wiki/` must resolve

A weekly cron and manual-trigger workflow [`vocabulary-drift.yml`](./.github/workflows/vocabulary-drift.yml) audits lesson markdown for forbidden synonyms of the canonical vocabulary. Run it on demand with `gh workflow run vocabulary-drift.yml`.

---

## How to Install

### Option A — One-liner (recommended)

Paste this into your terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/vishalmdi/ai-native-pm-os/main/install.sh | bash
```

This checks prerequisites, clones the repo into `~/ai-native-pm-os`, and runs first-time setup automatically.

---

### Option B — Manual install

```bash
git clone https://github.com/vishalmdi/ai-native-pm-os.git
cd ai-native-pm-os
bash setup.sh
```

---

### Start your first lesson

```bash
cd ~/ai-native-pm-os   # or wherever you installed it
```

Then launch your AI CLI in this directory and trigger lesson 0-1.

**Claude Code** (recommended):
```bash
claude
```
Then type:
```
/lesson 0-1
```

**Codex CLI / Gemini CLI / Aider / Cursor / other**:
```bash
codex   # or: gemini, aider, cursor .
```
Then ask in natural language:
```
load lesson 0-1
```

The `install.sh` and `setup.sh` scripts auto-detect which CLI is on your `PATH` and tell you the exact command to use. See the [wiki page on switching agents](./wiki/How-To-Use-Different-Agent.md) for per-tool details.

---

### Optional: progress dashboard

In a separate terminal window:

```bash
python3 course-server.py
```

Then open **http://localhost:4242** in your browser.

---

## Slash Command Reference

| Command | What it does |
|---------|-------------|
| `/lesson 0-1` | Load a specific lesson (replace `0-1` with any lesson ID) |
| `/next` | Continue from where you left off |
| `/complete` | Mark the current lesson done and update your progress |
| `/progress` | View a completion table across all 11 modules |
| `/context-check` | Audit your CLAUDE.md health |
| `/meridian` | Load the Meridian company context |

---

## Principles of This Course

1. **You build, not watch.** Every lesson has a hands-on deliverable.
2. **Real context, not toy examples.** Meridian is designed to reflect real B2B PM work.
3. **Cumulative.** Each module's output feeds the next.
4. **Yours to keep.** Every file you create is production-ready for real use.
5. **Cost-conscious.** We teach you to use the right model at the right time.

---

## Community Challenges

Each module ends with an optional community challenge:
- Share your output in the course community thread
- Review two peers' CLAUDE.md setups
- Vote on the best research synthesis of the week

---

*AI-Native PM OS — Original curriculum. All company names, data, and scenarios are fictional and created for educational purposes.*
