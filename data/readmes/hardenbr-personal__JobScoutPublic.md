# job-scout

An AI job-search agent that deliberately does NOT apply for you.

job-scout automates the tedious half of a targeted job search — sweeping
company boards and remote-job feeds daily — while keeping every decision
that matters in human hands. Fetches
live postings from public ATS APIs (Greenhouse, Lever, Ashby) plus
remote-job aggregators, applies deterministic hard filters, runs LLM
triage with a code-enforced provenance rule, and emails a daily digest.
**Human-in-the-loop by design: it never applies, never contacts anyone.**

## Why no auto-apply?

Auto-apply agents optimize the wrong metric. Application volume is not
the bottleneck in a serious search — signal quality and channel quality
are. An agent that mass-submits generates slop for hiring teams and risk
for the candidate (an LLM filling free-text fields will eventually
fabricate something on your behalf). So this agent finds, filters,
verifies, and briefs. Applying stays a human act.

## Design principles

- **Provenance rule (enforced in code):** the LLM cannot disqualify a
  role for travel without a verbatim quote that actually appears in the
  JD. Inference becomes a screen question, never a filter.
- **Live-board verification:** aggregator finds are re-checked against
  the live ATS board; closed listings are detected by diffing the board,
  not trusting cached JD URLs.
- **Warm-path gate:** APPLY verdicts at companies with a referral route
  render with a "route via contact first" banner.
- **Auditable drops:** every filtered-out job is logged with a reason.

## Setup

Uses the Gemini API through Google's OpenAI-compatible endpoint (the
`openai` package is just the HTTP client). Default model:
`gemini-3.1-flash-lite`; override with `SCOUT_MODEL` (e.g.
`gemini-3.6-flash` for deeper triage reasoning).

macOS/Linux:
```bash
pip install -r requirements.txt
mkdir private
cp companies.example.yaml companies.yaml           # your target companies
cp profile.example.yaml private/profile.yaml       # edit
cp warm_paths.example.yaml private/warm_paths.yaml # edit
export GEMINI_API_KEY=your-key

python -m scout discover    # resolve ATS slugs in companies.yaml, then edit it
python -m scout dry-run     # fetch + filters only, no LLM cost
python -m scout run         # full pipeline
```

Windows (cmd):
```cmd
pip install -r requirements.txt
mkdir private
copy profile.example.yaml private\profile.yaml
copy warm_paths.example.yaml private\warm_paths.yaml
set GEMINI_API_KEY=your-key

python -m scout discover
python -m scout dry-run
python -m scout run
```

Email delivery (optional locally, on by default in CI): set `SMTP_HOST`,
`SMTP_PORT`, `SMTP_USER`, `SMTP_PASS` (Gmail App Password), `DIGEST_TO`.

## Scheduled runs (GitHub Actions)

`.github/workflows/scout.yml` runs weekdays at 7:00 AM Pacific. Add repo
secrets: `GEMINI_API_KEY`, `SMTP_USER`, `SMTP_PASS`, `DIGEST_TO`,
`PROFILE_YAML`, `WARM_PATHS_YAML` (paste the full file contents into the
last two). State persists between runs via the Actions cache.

## What it deliberately does not do

No form submission, no LinkedIn automation, no Workday scraping
(Workday companies get manual-check reminders on cadence), no outreach.
The public repo ships example configs only; real profile and contacts
live in gitignored `private/`.
