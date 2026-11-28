# job-hunt-skill

> An end-to-end Claude Code skill pipeline that turns one master CV + an experience bank into tailored applications, semi-automatically. Built originally for a UK AI startup job hunt, open-sourced as a framework.

English · [简体中文](README.zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-skill-blueviolet)](https://docs.anthropic.com/claude/docs/claude-code)

---

## What it does

You paste a job description URL or text. Claude:

1. Picks the right CV bullet variants for that role (from your **experience bank**)
2. Writes a 1-page tailored CV PDF
3. Writes a 250–400 word cover letter PDF
4. Writes a ≤60-word LinkedIn cold DM
5. Writes 3 bullets for "why I fit" application-form fields
6. Walks you through the actual submission field by field
7. Logs the submission to a tracker
8. Learns from your feedback so the next application starts better

All outputs live under `applications/<company>-<role>-<date>/`. Your master CV is canonical and never modified by per-application work.

## Architecture — 8 phases, 2 skills

```
job-hunt   (orchestrator) ────────────────────────────────┐
   ├─ Phase 0  Bootstrap        (one-time setup)          │
   ├─ Phase 1  Research         (sub-agent → companies + salaries)
   ├─ Phase 2  Tailor           ───── delegates to ─────► cv-tailor
   ├─ Phase 3  Pre-submission Review                      │
   ├─ Phase 4  Submission Walkthrough                     │
   ├─ Phase 5  Track            (tracker.md)              │
   ├─ Phase 6  Outreach         (LinkedIn / cold email)   │
   └─ Phase 7  Learn + Backport (feedback → memory rules)
```

`cv-tailor` is the tactical sub-skill that produces materials for ONE role.
`job-hunt` is the orchestrator that decides which phase to enter from your input.

See [`docs/architecture.md`](docs/architecture.md) for the full design rationale.

## Who this is for (and who it isn't)

✅ **Good fit:**
- Junior / new-grad / first-full-time job seekers
- Targeting startups (where portfolio + ship-evidence > credentials)
- Comfortable with LaTeX (or willing to switch to Markdown/Pandoc; see customization)
- Want to apply to 10+ companies with real per-role tailoring rather than mass-blast

🟡 **Will need adaptation:**
- Senior IC / EM (need different cover-letter angle; the "junior, no internship" defaults won't fit)
- Career-changers (some role-fit logic assumes degree → first job, not pivot stories)
- Non-tech industries (consulting / banking / academic — sample templates are tech-flavoured)
- Markets outside UK / US / EU (visa logic + salary bands need replacement)

🔴 **Probably not for you:**
- You only need to apply to 1–3 places (overhead > value)
- You don't use Claude Code or any LLM-orchestrating CLI
- You want a one-click "auto-apply to 100 jobs" tool — this is the opposite philosophy

See [`docs/customization.md`](docs/customization.md) for what to change for your context.

## Quick start

```bash
# 1. Clone
git clone https://github.com/<your-username>/job-hunt-skill.git
cd job-hunt-skill

# 2. Copy the skill files into your Claude Code skills directory
cp -r skills/job-hunt   ~/.claude/skills/
cp -r skills/cv-tailor  ~/.claude/skills/

# 3. Copy the workspace template to wherever you want your job-hunt working dir
cp -r workspace-template ~/job-hunt-workspace

# 4. Open the workspace, edit config.yaml with your paths + context
$EDITOR ~/job-hunt-workspace/config.yaml

# 5. Install Tectonic (LaTeX engine)
brew install tectonic   # mac
# or apt install tectonic, etc.

# 6. Bootstrap your master CV — start a Claude Code session and say:
#     "Build my master CV from scratch — I'll feed you my background"
#    This triggers Phase 0 of the job-hunt skill.
```

Detailed setup: [`docs/setup.md`](docs/setup.md).

## What you get vs what you have to write

| Provided by this repo | You write yourself |
|---|---|
| 8-phase orchestration logic (job-hunt SKILL.md) | Your master CV (after Phase 0 helps you) |
| Per-role tailoring logic (cv-tailor SKILL.md) | Your experience bank: real bullet variants per project |
| Cover letter / DM / why-I-fit templates | Your memory file: profile snapshot + writing rules |
| Sample fictional persona ("Alex Chen") | Your real config.yaml: paths, market, visa context |
| Example experience-bank entry | Per-role JD analysis happens at runtime |
| Tracker template | Phase 7 backports learn what YOU specifically need |

## Hard rules (built into the skill)

1. **Never auto-submit.** The Submit button is always yours to click.
2. **Never invent metrics.** No retention %, MRR, MAU unless you confirmed the number.
3. **1 page CV always.** If it overflows, the skill drops a bullet, not the page break.
4. **Master CV is canonical.** Per-application work copies and edits a copy.
5. **Tracker is source of truth.** Every submission logged.
6. **Visa honesty.** Form questions about sponsorship are answered honestly.
7. **Sub-agent for research, not serial WebFetch.** Glassdoor / LinkedIn block scrapers; multi-source triangulation needs parallel agents.

## Built with

- [Claude Code](https://docs.anthropic.com/claude/docs/claude-code) — Claude as a CLI agent
- [Tectonic](https://tectonic-typesetting.github.io/) — LaTeX engine (single binary, auto-fetches packages)
- [Pandoc](https://pandoc.org/) — optional, for Markdown → PDF cover letters
- [Ashby](https://www.ashbyhq.com/) / [Greenhouse](https://www.greenhouse.com/) / [Lever](https://www.lever.co/) / [Workable](https://www.workable.com/) — common ATS systems handled in Phase 4

## Status

**v1.0 — reference implementation.** Built originally for one user's UK AI startup job hunt. Generalized for fork-and-adapt use.

Roadmap (driven by community PR, not maintainer pre-emption):
- [ ] `config.yaml` parser that auto-substitutes paths / market / visa across files
- [ ] US OPT / Canada PGWP / EU Blue Card visa modules
- [ ] Industry variants: consulting / banking / academic
- [ ] Senior IC / EM playbooks
- [ ] Markdown / Word output paths (currently LaTeX-only)

PRs welcome. Issues welcome. No promises on timelines.

## License

MIT — see [`LICENSE`](LICENSE).

## Credits

Designed iteratively over a real job-hunt session. The 8-phase model and the "learn + backport" loop in particular came from observing what actually saved time vs felt productive. If the skill saves you 20 hours over your job hunt, please open an issue saying so — that's the one signal worth tracking.
