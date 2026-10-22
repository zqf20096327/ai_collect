# pd-portfolio-review

An AI skill that reviews product designer portfolios (and UX / UI portfolios) the way a busy hiring reviewer would. It is informed by [UXfolio’s State of UX Portfolios 2026](https://uxfol.io/state-of-ux-portfolios-2026) research.

It also incorporates principles from Karl Koch’s [hiring-manager-bar](https://github.com/kemiljk/skills/tree/main/skills/hiring-manager-bar) skill ([karlkoch.me](https://karlkoch.me)): treating the hiring manager as the user, tagging evidence carefully, and keeping fixes small and checkable. That skill is MIT-licensed; see `skills/pd-portfolio-review/evals/LICENSE-hiring-manager-bar`.

Not affiliated with UXfolio. The scoring weights are this skill’s own.

This repository is a **monorepo**: the installable skill lives under `skills/`, and the marketing landing site lives under `apps/web` (Next.js). Install the skill with `npx skills add`; run or deploy the website from the same repo. Live site: [pd-portfolio-review.vercel.app](https://pd-portfolio-review.vercel.app/).

| Path | What it is |
| --- | --- |
| [`skills/pd-portfolio-review`](skills/pd-portfolio-review) | The installable agent skill, references, and evals |
| [`apps/web`](apps/web) | Public landing page: install command, how it works, score, Claude.ai upload path, FAQ |

## How it works

1. You ask for a review and give a portfolio URL (optional: target role, password).
2. The skill opens the site like a reviewer: home, work list, case studies, About, contact. It notes what is clear in the first ~30 seconds, then reads deeper.
3. You get a scored report: strengths, problems, a red-flag check, open checks, questions only you can answer, and at most five fixes in priority order, each with a done-check.

Evidence on every finding:

- **Rendered**: seen on the live page
- **Source**: in HTML / metadata / text, not confirmed visually
- **Unverified**: likely but unconfirmed (listed under Open checks; costs no points)

## Score

Out of 100. Maths stay visible in the report.

| Area | Points |
| --- | --- |
| Access and format (opens, loads, no download, website) | 15 |
| First scan (clear who, what, where to click) | 15 |
| Project choice and cards (relevance, 3 or 4, card context) | 15 |
| Thinking and decisions | 20 |
| Outcomes and ownership | 15 |
| Voice, AI use, visual quality | 10 |
| About, consistency, NDA handling | 10 |

Overrides: broken or locked link with no password scores **0** and stop. Each present red flag (Rendered or Source only) takes **3** points off the area total.

Verdict bands: **80+** ready to send · **60 to 79** send after fixes · **40 to 59** needs work first · **under 40** rebuild.

## Criteria

Checks follow UXfolio 2026 chapters (first 30 seconds, format and access, finding the right project, inside a case study, NDA work, AI use), including the eight ranked red flags. Figures are cited as “UXfolio 2026, ch. X.Y”, not rounded or invented.

Fairness rules built into the skill:

- Do not infer seniority from visual polish
- A famous employer is not proof of quality
- A style is not proof of AI use
- Do not demand longer case studies when the thinking is already clear
- Name distinctive choices so fixes do not push the site toward a generic template

Principles shared with hiring-manager-bar include the reviewer path, evidence labels, separating “missing” from “hard to find”, and implementable fixes with acceptance checks.

## Evals

[`skills/pd-portfolio-review/evals`](skills/pd-portfolio-review/evals) holds 27 invented review requests (plus local fixtures). Cases and fixtures come from Karl Koch’s hiring-manager-bar evals (MIT); expected outcomes are rewritten for this skill’s score, verdict bands, red flags, and evidence tags.

Run them by hand with any agent that can load the skill. See [evals/README.md](skills/pd-portfolio-review/evals/README.md). Rerun after you change `SKILL.md` or the references. These check behaviour, not hiring outcomes.

## Install

Needs Node.js 22+. Uses the [skills](https://www.npmjs.com/package/skills) CLI from [skills.sh](https://skills.sh).

```sh
npx skills add leonardobetti/pd-portfolio-review@pd-portfolio-review
```

Skip the prompts:

```sh
# This project, Claude Code only
npx skills add leonardobetti/pd-portfolio-review@pd-portfolio-review -a claude-code -y

# All projects (user level), Cursor and Codex
npx skills add leonardobetti/pd-portfolio-review@pd-portfolio-review -g -a cursor -a codex -y
```

### Manual

Agents look for a folder named `pd-portfolio-review` with `SKILL.md` inside. Keep `references/` next to it.

| Tool | User-level path |
| --- | --- |
| Claude Code | `~/.claude/skills/pd-portfolio-review/` |
| Cursor | `~/.cursor/skills/pd-portfolio-review/` |
| Codex / `.agents` | `~/.agents/skills/pd-portfolio-review/` |

```sh
git clone https://github.com/leonardobetti/pd-portfolio-review /tmp/pd-portfolio-review
cp -R /tmp/pd-portfolio-review/skills/pd-portfolio-review ~/.claude/skills/pd-portfolio-review
```

Restart the tool or open a new chat so it picks up the skill.

## Use

```
Review this portfolio: https://example.com
```

Or call it by name: `/pd-portfolio-review` in Claude Code and Cursor, or `$pd-portfolio-review` in Codex.

## Landing page (local)

Package manager: **Bun** (`packageManager` pinned to `bun@1.4.3`). Lint/format: **Biome**.

```sh
bun install
bun run dev
```

```sh
bun run lint    # biome check
bun run format  # biome format --write
bun run check   # biome check --write
```

Opens the site in `apps/web` (default http://localhost:3000). Agent overview: [`llms.txt`](llms.txt) (also served at `/llms.txt` on the site).

### Deploy (Vercel)

Create a project from this repo with **Root Directory** `apps/web`, and allow access to files outside that directory so the root `bun.lock` is used. Framework: Next.js. Install/build: leave default (or `bun install` / `bun run build` from the monorepo root via filter). Target host: `pd-portfolio-review.vercel.app`.

## Licence

MIT

