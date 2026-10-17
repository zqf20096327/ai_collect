<div align="center">

# AI Mentor

**A risk-ranked command center for university student mentoring —
deterministic scoring, AI narration, no black box.**

Built for the DIU AI Project Competition 2026 by team **Cortex Crew**.

`FastAPI` · `SQLAlchemy 2.0` · `Next.js 14` · `TypeScript` · `Tailwind` · `Azure OpenAI`

</div>

![Command center](docs/screenshots/command-center.png)

---

## The problem

A university mentor is typically responsible for 50+ students. The existing
mentoring portal shows each student's results, attendance, payments, and
meeting history — but only as **flat tables, one student at a time, across ~15
different screens**. Nothing answers the question a mentor actually has:

> *"Which of my students needs me **today**, and why?"*

So struggling students are noticed late, often after a failing semester —
when a dropping attendance curve had been visible in the data for months.

## The idea

AI Mentor sits **on top of** the existing portal (same API shapes, read-only)
and turns its raw data into decisions, in two strictly separated steps:

1. **A deterministic risk engine ranks** — every student gets a 0–100 risk
   score computed from 8 weighted signals. Pure arithmetic: auditable,
   reproducible, unit-tested. The contributor breakdown is shown in the UI and
   always sums to exactly the score.
2. **An LLM narrates** — Azure OpenAI (or a built-in offline mock) turns the
   already-computed numbers into plain language: a daily briefing, a per-student
   summary, meeting prep, grounded Q&A chat. **The model never invents, changes,
   or influences a score.**

That separation is the core design decision. The ranking can be defended
number-by-number in front of a dean; the prose makes it usable at 8 a.m.
before a mentoring session.

## Screenshots

The command center above shows the AI daily briefing, tier distribution, KPI
row, the risk-ranked roster with search and tier filters, and the systemic
insights panel ("12 students struggling in the same course").

**360° student profile** — risk gauge with the full contributor breakdown
(the bars sum to exactly the score), AI summary with the first question to
ask, SGPA trend, per-semester marks and attendance, grounded AI chat:

![Student profile](docs/screenshots/student-profile.png)

| Meeting preparation | Login |
|---|---|
| ![Meeting prep](docs/screenshots/meeting-prep.png) | ![Login](docs/screenshots/login.png) |
| AI-drafted agenda, questions and suggested actions; "expand my notes" turns two rough lines into a structured meeting record | Pre-filled demo account — one click to explore |

## Features

- **Risk-ranked roster** — 50 mentees sorted by computed risk, tiered
  **Critical / At-Risk / Needs Attention / On-Track** (cutoffs 72 / 52 / 28),
  with search and tier filter chips.
- **Explainable scoring** — every score decomposes into 8 signal bars
  (attendance, current-term marks, CGPA level, backlog & blocked courses,
  SGPA trend, attendance drop, dues, meeting recency). No hidden weights at
  runtime; the parts visibly add up.
- **AI daily briefing** — on login, a short "who needs you today and why"
  brief generated from the live cohort aggregate, cached until the data changes.
- **Per-student AI summary** — a 3–4 sentence diagnosis plus *the first
  question to ask*, with one-click regeneration.
- **Grounded chat** — "Why is this student at risk?" answered **only** from
  that student's stored data, streamed token-by-token.
- **Meeting workflow** — AI-drafted agenda/questions/actions before the
  meeting; after it, two lines of rough notes are expanded into a structured,
  saved meeting record.
- **Systemic insights** — course-level patterns across the cohort ("12 of
  your students are weak in Theory of Computing"), computed in Python, not by
  the model.
- **Live alerts** — Critical/At-Risk students pushed to the navbar bell over
  Server-Sent Events.
- **Privacy by design** — names and student IDs are replaced with
  placeholders (`STUDENT_A`, `ID_A`) *before* any text is sent to the LLM and
  swapped back after the response returns. The cloud model never sees who a
  student is.
- **Runs fully offline** — a deterministic mock AI provider mirrors every AI
  feature with the same validated schemas, so the whole system works with no
  API key and no network.

## How the risk engine works

`backend/app/risk/engine.py` — a pure function (`dicts in → dict out`), no DB,
14 unit tests.

| Signal | Weight | What it measures |
|---|---|---|
| Attendance | 0.19 | Worst-course attendance rate in the active semester |
| Current-term marks | 0.18 | Credit-weighted shortfall in continuous assessment so far |
| CGPA level | 0.18 | Distance below a 3.0 baseline |
| Backlog & blocked | 0.16 | Failed/withheld credits and registration-blocked courses |
| SGPA trend | 0.09 | Least-squares slope of the last three semesters |
| Attendance drop | 0.07 | Recent attendance vs. earlier in the term |
| Financial | 0.07 | Outstanding dues relative to total payable |
| Meeting recency | 0.06 | Days since the last mentoring meeting (60-day grace) |

Each signal returns a 0–1 severity; the score is the weighted sum × 100. The
per-signal contributions are stored as JSON, rendered as the profile's
breakdown panel, and sum to the displayed score by construction.

Grades themselves are internally consistent: letter grades derive from
component marks via the DIU grade scale (`app/academics.py`), and SGPA/CGPA
are credit-weighted means of those derived grade points — so a grade can never
contradict the transcript it came from.

## Architecture

```
   legacy portal API (read-only)      offline synthetic fixtures (default)
                  └────────────────┬─────────────────┘
                                   ▼
                ingestion → single normaliser → SQLite / Postgres
                                   ▼
              deterministic risk engine — 8 weighted signals
                  → score, tier, contributor breakdown
                                   ▼
          AI narrator — Azure OpenAI or offline mock; PII scrubbed,
          schema-validated, cached on an input hash so it only
                    regenerates when the data changes
                                   ▼
                       FastAPI (REST + SSE)  :8000
                                   ▼
                Next.js 14 dashboard (proxies /api/*)  :3000
```

Both data sources implement one `DataSource` interface — switching from the
committed synthetic fixtures to a live portal is a `.env` change, not a code
change. The AI layer is provider-agnostic the same way: `AI_PROVIDER=mock`
(default) and `AI_PROVIDER=azure` return the same validated Pydantic objects,
and any Azure error falls back to the mock so the app never hard-fails.

Full detail in [`docs/`](docs/README.md): [architecture](docs/architecture.md) ·
[risk engine](docs/risk-engine.md) · [AI layer](docs/ai-layer.md) ·
[data model](docs/data-model.md) · [API reference](docs/api.md) ·
[setup](docs/setup.md) · [deployment](docs/deployment.md)

## Quick start

Requires Python 3.12+ and Node 20+. The repo ships a **pre-seeded database**
(50 synthetic students with their AI summaries already generated), so the
first run needs no API key and no seeding — just install and start.

```bash
git clone https://github.com/kawsher-hridoy/DIU-AI-Mentor.git
cd DIU-AI-Mentor

# backend
cd backend
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env
cd ..

# frontend
cd frontend && npm install && cd ..

# run both (foreground; or ./start.sh to run detached, ./stop.sh to stop)
./run_demo.sh
```

Open **http://localhost:3000** and sign in with the pre-filled demo account
(`71000000` / `123456`).

To use live AI instead of the offline mock, set `AI_PROVIDER=azure` and the
`AZURE_OPENAI_*` values in `backend/.env` — see [docs/setup.md](docs/setup.md).

## The demo data

The 50-student Software Engineering cohort is **fully synthetic** — no real
student data anywhere in this repository. It is generated deterministically by
`backend/tools/gen_se_cohort.py`, which models the real DIU assessment
structure per course (three quizzes + makeup, midterm + improvement,
presentation/assignment, continuous + final) and derives every grade, SGPA and
CGPA from component marks, so the academic records are internally consistent.
The JSON fixture shapes mirror the university portal's actual API responses,
which is what makes the live-portal switch a config flip.

Resulting spread: **7 Critical · 3 At-Risk · 18 Needs Attention · 22 On-Track**.

## Repository layout

```
├── backend/                 # FastAPI + SQLAlchemy (Python 3.12)
│   ├── app/
│   │   ├── main.py          #   REST + SSE routes
│   │   ├── models.py        #   11 tables (SQLite now, Postgres-portable)
│   │   ├── academics.py     #   DIU grade scale + credit-weighted GPA
│   │   ├── risk/            #   deterministic 8-signal engine + tests
│   │   ├── ai/              #   narrator, prompts, PII scrub, schemas, chat
│   │   ├── ingest/          #   DataSource interface: fixtures | live client
│   │   └── pipeline.py      #   ingest → score → narrate (CLI + API share it)
│   ├── tools/gen_se_cohort.py  # deterministic synthetic-cohort generator
│   ├── fixtures/            #   the generated demo data (committed)
│   └── ai_mentor.db         #   pre-seeded demo DB (committed)
├── frontend/                # Next.js 14 + TypeScript + Tailwind + Recharts
│   ├── app/                 #   /login · / (command center) · /student/[id] · …/meeting
│   ├── components/          #   RiskRing, RiskBreakdown, AiBriefing, AskAiChat, …
│   └── lib/                 #   typed API client, tier config
├── docs/                    # as-built documentation
└── run_demo.sh / start.sh / stop.sh
```

## Running the tests

```bash
cd backend && .venv/bin/pytest app/risk    # 14 risk-engine tests
cd frontend && npx next build              # type-checks every route
```

## Team

**Cortex Crew** — Daffodil International University, Software Engineering.
Built for the DIU AI Project Competition 2026.
