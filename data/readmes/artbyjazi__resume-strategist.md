# resume-strategist

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An open-source, model-agnostic "resume strategist" skill for students and early-career candidates. It does what an $800–1,000 resume-writing package does — strategy conversation, tailored resume, cover letter, quality review — as a single instruction file any LLM can follow. Every rule is tied to recruiter eye-tracking studies, ATS recruiter interviews, or 2025–26 hiring surveys (see [`references/evidence.md`](references/evidence.md)).

## Quickstart

**Claude (claude.ai / desktop app)** — Settings → Skills → upload `SKILL.md`. It triggers automatically when you share a resume or job posting.

**Claude Code** — clone straight into your skills directory:

```bash
git clone https://github.com/artbyjazi/resume-strategist.git ~/.claude/skills/resume-strategist
```

**ChatGPT, Gemini, or any other chat** — open [`PROMPT.md`](PROMPT.md), copy all of it, paste it as your first message (or into custom instructions / a custom GPT / a Gem). Then paste your resume and the job posting.

**Ollama / local models** — use `PROMPT.md` as the system prompt.

## What it does

1. Intake — works from a resume, a posting, or both
2. Strategy conversation — 3–5 pointed questions, not a questionnaire
3. Job-posting decode — must-haves, exact vocabulary, knockout filters
4. Tailored one-page resume — built for the 7-second F-pattern scan, parse-clean for ATS search
5. Cover letter — paragraph or skills-match-table format, cliché-banned
6. Anti-AI-tell pass + quality gate — six-axis score and three next actions

## What it refuses to do

Invent metrics, titles, tools, or experience. It asks for numbers instead of making them up, and won't pad a skills section the bullets don't back.

## Repo structure

```
SKILL.md                   the skill — frontmatter + instructions
PROMPT.md                  generated from SKILL.md, frontmatter stripped, paste anywhere
references/evidence.md     the sources behind each rule
scripts/sync_prompt.py     regenerates PROMPT.md; --check fails on drift
scripts/check_frontmatter.py  validates the SKILL.md frontmatter
```

`PROMPT.md` is generated — edit `SKILL.md` and run `python scripts/sync_prompt.py`. CI enforces it.

## Roadmap

- Role vocabulary packs (SWE, finance, consulting, marketing)
- Country-specific norms (Canadian co-op vs US vs UK/EU)
- Before/after example resumes
- A companion edition for mid-level and executive candidates

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The short version: never hand-edit `PROMPT.md`, every rule needs a source in `references/evidence.md`, and no individual coaches or services get named.

## License

MIT — see [LICENSE](LICENSE).
