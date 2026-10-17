# Coach — a portable Personal Trainer + Nutritionist for AI agents

A single, portable **AI coaching system** that turns your agent into a complete,
evidence-based **personal trainer _and_ nutritionist** for one athlete. It programmes
your training with RPE-based progressive overload, logs every session, tracks progress
and busts plateaus, calculates your calorie and macro targets, builds practical meal
plans, and **remembers all of it between conversations** by keeping your profile and
logs in files.

It is packaged two ways from the same knowledge base so it runs anywhere:

- as a **Claude Code / claude.ai skill** ([`personal-trainer/SKILL.md`](personal-trainer/SKILL.md)), and
- as a **cross-agent `AGENTS.md`** ([`AGENTS.md`](AGENTS.md)) read automatically by
  **Codex, opencode, Cursor, Gemini CLI, Jules** and other `AGENTS.md`-aware tools,
  plus a dedicated **opencode agent** ([`.opencode/agent/coach.md`](.opencode/agent/coach.md)).

Every recommendation is grounded in the strength-and-conditioning and nutrition
literature — the Coach is a *scientific lifter and nutritionist*, not bro-science.

---

## What's in this folder

```
.
├── README.md                       ← you are here
├── AGENTS.md                       ← cross-agent instructions (Codex, opencode, Cursor, Gemini CLI…)
├── .opencode/
│   └── agent/
│       └── coach.md                ← dedicated opencode agent definition
└── personal-trainer/               ← the shared knowledge base + Claude skill
    ├── SKILL.md                    ← Claude Code / claude.ai entry point
    ├── references/
    │   ├── evidence.md             ← scientific evidence base + citations + confidence grading
    │   ├── training.md             ← programming, logging, progression, periodisation
    │   ├── nutrition.md            ← TDEE/macros, meal planning, supplements, stalls
    │   └── prompts.md              ← ready-made prompt stack
    └── assets/                     ← blank fill-in templates (copied into coach-data/)
        ├── athlete-profile.md
        ├── exercise-library.md
        ├── lift-log.md
        ├── programme-template.md
        └── nutrition.md
```

### How it's designed

- **`AGENTS.md`** and **`personal-trainer/SKILL.md`** are two entry points into the
  *same* brain. Each defines the Coach's identity, the persistent-data rules, and the
  onboarding flow, then routes to the detailed reference files. `AGENTS.md` is the
  universal one (most agents load it automatically); `SKILL.md` adds Claude's skill
  frontmatter so Claude auto-activates it.
- **`personal-trainer/references/`** holds the detailed coaching logic and the science.
  The agent reads only the file relevant to the request (training vs nutrition vs
  evidence vs prompts) — **progressive disclosure** keeps the always-loaded context
  small while deep knowledge stays available on demand.
- **`personal-trainer/assets/`** holds blank templates. On first use the agent copies
  them into a working **`coach-data/`** folder, where your actual data lives and grows.

### Persistence — the important bit

What makes this a *coach* and not a *chatbot* is memory. Whenever it runs, it looks for
a `coach-data/` folder in the working directory and reads:

| File | Holds |
|------|-------|
| `coach-data/athlete-profile.md` | Stats, goals, schedule, equipment, injuries, dietary prefs |
| `coach-data/exercise-library.md` | Which exercises are YES / SUB / NO |
| `coach-data/lift-log.md` | Working weights + every logged session (append-only) |
| `coach-data/programme.md` | The active programme + block/week tracking |
| `coach-data/nutrition.md` | Calculated targets, macros, meal-plan history |

After every session log, target calculation, or programme change it writes the update
back — so the next conversation picks up where you left off. The lift log is
**append-only**: old entries are never deleted, because they are the source of truth
for progress.

---

## Installation & use

Any agent with file read/write gets full persistence. Pick your tool.

### Codex (OpenAI Codex CLI)

`AGENTS.md` is read automatically from the working directory.

1. Put this folder where you want your `coach-data/` to live (or copy `AGENTS.md` +
   `personal-trainer/` into an existing project). Codex also merges `~/.codex/AGENTS.md`
   if you want the Coach available globally.
2. Run `codex` in that folder and say: *"Be my coach — set me up."*
3. Codex reads `AGENTS.md`, runs onboarding, creates `coach-data/`, and reads/writes
   your files directly from then on.

### opencode

Two ways:

- **Automatic rules:** opencode reads `AGENTS.md` from the project root — just open
  opencode in this folder and talk to it.
- **Dedicated agent:** [`.opencode/agent/coach.md`](.opencode/agent/coach.md) defines a
  primary agent named **coach** (read/write/edit/bash enabled). Switch to it with the
  agent picker (Tab) or `@coach`. To make it global, copy that file to
  `~/.config/opencode/agent/coach.md`.

### Cursor / Gemini CLI / Jules / other AGENTS.md agents

Open the folder; these tools pick up `AGENTS.md` as project instructions. Anything with
file access maintains `coach-data/` automatically. Then use natural language or the
prompt stack in [`personal-trainer/references/prompts.md`](personal-trainer/references/prompts.md).

### Claude Code

1. Copy `personal-trainer/` into a skills directory:
   - **Personal (all projects):** `~/.claude/skills/personal-trainer/`
     (Windows: `C:\Users\<you>\.claude\skills\personal-trainer\`)
   - **Project-scoped:** `<your-project>/.claude/skills/personal-trainer/`
2. Open Claude Code in the folder you want `coach-data/` to live in.
3. Say *"Be my coach. Let's set up my profile."* — Claude detects the skill, onboards
   you, and creates `coach-data/`. Confirm install with `/skills`.

(Claude Code will also honour the root `AGENTS.md` if you prefer not to install the
skill.)

### claude.ai Project (no install, no file writes)

1. **Projects → New Project**, name it (e.g. "Coach").
2. Paste the body of [`personal-trainer/SKILL.md`](personal-trainer/SKILL.md) (skip the
   YAML frontmatter) into the project **Instructions**, then append the `references/`
   files so the full logic is available (Projects can't lazy-load).
3. Upload your filled-in `assets/` templates into the project **Files**.
4. ⚠️ Projects can't write back to files — after each session, ask for the updated
   `lift-log.md` block and paste it into your uploaded file yourself.

### Any LLM API / Agent SDK

Load `AGENTS.md` (or `SKILL.md`) + the reference files as the system prompt and give
the model a filesystem tool scoped to a `coach-data/` directory. The data rules then
drive persistence exactly as above.

---

## A typical first session

1. **You:** "Be my coach — set me up."
2. **Coach:** creates `coach-data/`, interviews you for the essentials, walks the
   exercise library, saves everything, confirms what it knows and flags gaps.
3. **You:** "Build me a 4-day programme" → full Day 1 + structure for Days 2–4, saved
   to `programme.md`.
4. **You:** "Now calculate my fat-loss calories and protein" → shows the Mifflin-St
   Jeor working, sets targets, saves to `nutrition.md`.
5. **Day to day:** paste your sessions to log them, ask for the next workout, request
   meal plans, swap exercises, run a deload, or troubleshoot a stall.

---

## Evidence-based by design

The Coach is built as a **scientific lifter and nutritionist** — every protocol,
number, and claim is grounded in the strength-and-conditioning and nutrition
literature, not bro-science or fads. It carries its own evidence library in
[`personal-trainer/references/evidence.md`](personal-trainer/references/evidence.md),
which:

- maps each coaching rule back to its research basis (e.g. volume as the primary
  hypertrophy driver, proximity-to-failure governing the stimulus, energy balance for
  fat loss, protein at 1.6–2.2 g/kg);
- carries a short-form reference list (Morton et al. 2018, Schoenfeld et al. 2017,
  ACSM 2009, Kreider et al. 2017, ISSN position stands, etc.) the Coach cites from;
- tells the Coach to **grade its confidence** (strong / moderate / emerging), be
  honest when evidence is thin, **never fabricate a citation**, and reject
  pseudoscience (detoxes, fat burners, spot reduction, "metabolic damage" myths)
  outright.

Ask it *"why?"* or *"what's the source?"* on any recommendation and it pulls the
rationale and citation rather than hand-waving.

## Coaching principles baked in

**Training** — RPE-based loading (7–8 hypertrophy, 8–9 strength), never percentages off
a 1RM; progressive overload after 2 consecutive top-of-range sessions at target RPE
(+2.5 kg upper compounds, +5 kg lower compounds, reps-before-weight on accessories);
compounds first, accessories for weak points; Week 1 is calibration; deload every 4–6
weeks.

**Nutrition** — TDEE via Mifflin-St Jeor × activity factor, 300–500 kcal deficit for
steady fat loss; macro priority protein 0.8–1 g/lb (≈1.6–2.2 g/kg, non-negotiable), fat
≥0.35 g/lb, carbs fill the rest; whole-food, practical meal plans that respect every
restriction; evidence-backed supplements only.

**Style** — direct, concise, real numbers, tables for programmes and meal plans, metric
units, no moralising.

---

## Customising it

- Edit [`AGENTS.md`](AGENTS.md) / [`personal-trainer/SKILL.md`](personal-trainer/SKILL.md)
  to change the coach's personality, units (e.g. switch to lb/imperial), or default
  split. Keep the two in sync since they share a brain.
- Edit the `references/` files to adjust programming or nutrition rules (progression
  increments, deficit size, periodisation, evidence).
- Edit the `assets/` templates to change what data the coach collects.

---

## Disclaimer

The Coach is a tool, not a doctor or a registered dietitian. Train sensibly, and if you
have a diagnosed health condition or complex dietary needs, consult a qualified
professional. The system is built to flag this and defer on medical questions.

*Knowledge distilled from guides by [Hawks (@Hawks0x)](https://x.com/Hawks0x), grounded
in the literature cited in `personal-trainer/references/evidence.md`.*
