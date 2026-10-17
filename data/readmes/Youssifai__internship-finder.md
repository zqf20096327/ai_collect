# internship-finder

> An AI job-search command center built on Claude Code. Score offers, generate tailored CVs and cover letters, fill portal forms with a safety gate, and track everything — without ever turning into a mass-apply bot.

![Claude Code](https://img.shields.io/badge/Claude_Code-000?style=flat&logo=anthropic&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

---

## Why this exists

Most job-search "tools" optimize for volume — fire 200 résumés a week into ATS systems, hope one sticks. That approach disrespects the recruiters reading them and disrespects your own time.

**internship-finder is the opposite.** It is a filter, not a firehose. The pipeline forces you to score every role before generating any documents, skips anything below your fit threshold, and keeps a single human in the loop for every form submission. The point is to apply to fewer roles, with much better-matched documents, and never burn a relationship by sending something generic.

It runs as a Claude Code skill on your machine. Your CV, contact info, and notes stay local — only the JD and your prompts touch Anthropic's API.

---

## What it does

- **Scores offers** with a structured 5-dimension fit check (technical overlap, domain alignment, interview defensibility, language feasibility, career value) before you spend any time on documents
- **Generates full application packs** — tailored CV (LaTeX → PDF), cover letter (HTML → PDF), and optional reference letter, each rewritten per role
- **Scrapes portals** — company career pages and general job boards (Greenhouse, Lever, Ashby, custom), writing pending URLs to an inbox
- **Fills application forms** with Playwright behind a hard "BESTÄTIGT" confirmation gate — you always review the rendered form and approve before anything is submitted
- **Tracks everything** in a Notion database (with a legacy JSON tracker as a fallback for offline work)
- **Remembers rejections** so similar roles get flagged automatically next time
- **Drills interviews** with a generic playbook, story bank, and live German→English translator powered by Deepgram for non-native interview language practice

Out of the box it's tuned for German Pflichtpraktikum / Werkstudent applications in the automotive and engineering market (Bosch, Audi, MAHLE, Continental, ZF, and similar). The `/setup` wizard walks you through retargeting it for any role family, any market, any language.

---

## Quick start

```bash
# 1. Clone
git clone https://github.com/Youssifai/internship-finder.git
cd internship-finder

# 2. Install dependencies
npm install
npx playwright install chromium

# 3. Health check
npm run doctor

# 4. Open Claude Code and run /setup
claude
```

Inside Claude Code:

```
/setup
```

`/setup` is a guided onboarding flow. It asks who you are, what roles you're targeting, your logistics, your CV, your "narrative" (the human story behind your applications), and optionally walks you through configuring the portal scanner, technical reference materials, and integrations. It then writes:

- `cv.md` — your canonical CV
- `YOUNA.md` — your narrative, application rules, and verified skills
- `config/profile.yml` — structured profile data
- `modes/_profile.md` — AI personalization overlay (so system updates never overwrite your customizations)
- `portals.yml` (optional) — portal scanner config
- `.env` (optional) — credentials for Deepgram, etc.

When `/setup` finishes, the placeholder tokens scattered through the templates (`{{candidate.full_name}}`, `<your-anchor-project>`, etc.) get substituted with your real values, and the system is ready to evaluate jobs.

> **Tip:** if you skip `/setup` and try to run a command, the system will detect the missing pieces and offer to walk you through them before doing anything.

---

## How the pipeline works

```
You paste one or more job URLs (or run /career-ops scan)
                         │
                         ▼
              ┌──────────────────────┐
              │  Pass 1 — Scoring    │  Scrape + score → compact table → STOP
              │  (modes/score.md)    │
              └──────────┬───────────┘
                         │  You review and confirm which roles to proceed with
                         ▼
              ┌──────────────────────┐
              │  Pass 2 — Documents  │  Per approved role:
              │  (modes/bewerbung.md)│  CV plan → cover letter → reference letter
              │                      │  → required-docs check → report → tracker
              └──────────┬───────────┘
                         │
                  ┌──────┼──────┐
                  ▼      ▼      ▼
              Report  CV PDF  Tracker
               .md    .pdf    Notion / .json
```

Documents are **never** generated in the same pass as scoring. You always see the scores first. Anything below 3.0/5 is skipped automatically. The threshold is configurable in `modes/_shared.md`.

---

## Commands

Inside Claude Code:

| Command | What it does |
|---------|--------------|
| `/setup` | First-time onboarding (CV, narrative, target roles, portals, credentials) |
| `/career-ops` | Show the full menu |
| `/career-ops {URL or JD}` | Auto-route: brief fit review + generate full pack for a single role |
| `/career-ops pipeline` | Process all pending URLs from `data/pipeline.md` |
| `/career-ops scan` | Scan portals for new offers |
| `/career-ops apply {URL}` | Walk through a portal application form with Playwright + safety gate |
| `/career-ops tracker` | Application status overview |
| `/career-ops deep {company}` | Company research deep-dive |
| `/career-ops contacto {company}` | Find LinkedIn contacts and draft outreach |
| `/career-ops training {course}` | Evaluate a course or certification against your goals |
| `/career-ops project {idea}` | Evaluate a portfolio project idea |

You can also paste a job URL or JD directly into Claude — it auto-routes to the pipeline.

---

## Prerequisites

- **Node.js** 18+
- **Claude Code** — `npm install -g @anthropic-ai/claude-code`
- **pdflatex** — required for CV generation (`apt install texlive-full`, or MacTeX on macOS)
- **Playwright Chromium** — required for PDF generation and portal scraping (`npx playwright install chromium`)
- **Notion workspace** (optional but recommended) — used for the application tracker

---

## CV and cover letter generation

The CV builder compiles a one-page LaTeX CV from a JSON plan that Claude generates per role:

```bash
node build-cv.mjs <slug>
# Output: output/<company>/<role>/Lebenslauf.pdf
```

The cover letter builder renders an HTML template to PDF via Playwright:

```bash
node build-anschreiben.mjs <slug>
# Output: output/<company>/<role>/Anschreiben.pdf
```

Both templates are fully customizable:
- LaTeX template + sections → `cv-latex/`
- HTML cover-letter template → `templates/anschreiben-template.html`
- Reference letter template → `templates/empfehlung-template.html`

Edit the templates directly to change the visual design — they're plain HTML/CSS and LaTeX.

---

## Safety gate (the most important rule)

Before any portal submission, the system **must** display every form field with its exact value, every file path it will upload, and the exact submit button text, then ask:

```
--- GENEHMIGUNG ERFORDERLICH ---
Tippe 'BESTÄTIGT' zum Absenden oder 'ABBRUCH' zum Abbrechen.
```

Only `BESTÄTIGT` (case-insensitive) proceeds. Anything else stops completely.

This rule overrides everything else and applies to every portal, every session, every time. Prior approval in one session does NOT carry over.

---

## Project structure

```
internship-finder/
├── CLAUDE.md                    # Agent instructions (system layer)
├── cv.md                        # Your CV (written by /setup, edited by you)
├── YOUNA.md                     # Your narrative and application rules (written by /setup)
├── config/
│   ├── profile.example.yml      # Template for your profile
│   └── profile.yml              # Your profile (written by /setup, gitignored)
├── modes/                       # Skill modes Claude reads
│   ├── _shared.md               # System layer: scoring rules and framing
│   ├── _profile.md              # Your overlay (created by /setup, gitignored)
│   ├── score.md                 # Pass 1: fast scoring
│   ├── bewerbung.md             # Pass 2: full application pack
│   ├── apply.md                 # Portal form filling
│   ├── pipeline.md              # Batch URL processing
│   ├── scan.md                  # Portal scanning
│   ├── tracker.md               # Status overview
│   ├── de/                      # German-specific modes
│   └── fr/                      # French-specific modes
├── cv-latex/                    # LaTeX CV template and sections
├── templates/                   # HTML letter templates + portal config example
├── build-cv.mjs                 # LaTeX CV compiler
├── build-anschreiben.mjs        # Cover letter PDF generator
├── scripts/
│   ├── tracker.mjs              # Regenerates output/applications.xlsx
│   ├── live-translate.mjs       # Live German→English translator for interviews
│   └── batch-generate-docs.mjs  # Batch generator
├── interview-prep/              # Generic playbook, story bank, prep instructions
├── skills/                      # Drop your technical reference materials here (gitkept)
├── data/                        # Your tracking data (gitignored)
├── docs/docs/                   # Your supporting PDFs (gitignored)
├── reports/                     # Evaluation reports (gitignored)
└── output/                      # Generated PDFs (gitignored)
```

User data, generated artifacts, and credentials are all gitignored. The repo only tracks the system code and templates.

---

## Personalizing the system

This system is designed to be customized by Claude itself. You don't need to learn its internals — just ask.

- *"Change the scoring weights to prioritize hardware roles"* → edits `modes/_shared.md`
- *"Add these 5 companies to my portal scanner"* → edits `portals.yml`
- *"Update my availability to March 2027"* → edits `config/profile.yml`
- *"My target roles are now data engineering, not embedded"* → edits `modes/_profile.md` archetypes
- *"Translate the modes to Spanish"* → translates all `modes/*.md` files

**User data goes in:** `cv.md`, `YOUNA.md`, `config/profile.yml`, `modes/_profile.md`, `portals.yml`, `data/`, `docs/docs/`, `reports/`

**System code (auto-updatable, don't put personal data here):** `modes/_shared.md`, `modes/oferta.md` and other modes, `CLAUDE.md`, `*.mjs` scripts, `templates/`

Never put personal data in `modes/_shared.md` — it gets overwritten on updates. That's why `modes/_profile.md` exists.

---

## Languages

The system ships with three language packs:

- **English** (default) — `modes/`
- **German** (DACH market) — `modes/de/` with native vocabulary (Pflichtpraktikum, Probezeit, Tarifvertrag, AGG, etc.)
- **French** (Francophone market) — `modes/fr/` with native vocabulary (CDI/CDD, convention collective, RTT, mutuelle, intéressement, etc.)

`/setup` asks which you want as default; you can switch per session by saying *"use German modes for this evaluation."*

---

## Tracker

Source of truth: a Notion database called "Job Applications" (under your "Job Hunt" workspace). Set it up after `/setup` by saying *"set up the Notion tracker"*. Status options are: `Not Applied`, `Applied`, `Interview`, `Offer`, `Rejected`.

There's a legacy local JSON / Excel tracker (`data/applications.json` → `output/applications.xlsx`) kept around as a fallback for offline work, but Notion is the canonical store.

---

## Scripts reference

| Script | Purpose |
|--------|---------|
| `npm run doctor` | Check all prerequisites |
| `node build-cv.mjs <slug>` | Compile LaTeX CV to PDF |
| `node build-anschreiben.mjs <slug>` | Render cover letter to PDF |
| `node scripts/tracker.mjs` | Regenerate Excel tracker |
| `node scripts/live-translate.mjs` | Start live German→English transcription server for interviews |
| `node normalize-statuses.mjs` | Fix non-canonical status values |
| `node dedup-tracker.mjs` | Remove duplicate tracker entries |
| `node verify-pipeline.mjs` | Pipeline integrity check |
| `node check-liveness.mjs` | Check if URLs in pipeline are still live |
| `node update-system.mjs check` | Check for upstream system updates |

---

## Privacy and disclaimer

This is a local tool. Your CV, contact info, personal notes, and application history live on your machine and never leave it — except for the parts of a JD or prompt that get sent to Anthropic's API when Claude is invoked. There is no telemetry, no hosted backend, no analytics.

AI-generated content is a recommendation, not a guarantee. Always review every generated document before submitting. Always use this tool in accordance with the Terms of Service of any portal you interact with.

See [LEGAL_DISCLAIMER.md](LEGAL_DISCLAIMER.md) for full details.

---

## Credits

Originally built and used by [santifer](https://santifer.io) to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role. The two-pass pipeline, scoring methodology, safety gate, and overall architecture are theirs.

This fork has been converted into a public template (`/setup` flow, generic interview prep, market-agnostic placeholders, BMW-specific automation removed) so anyone can clone it and adapt the system to their own search.

Released under the [MIT License](LICENSE).
