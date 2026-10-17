# ai-toolbox

Open-source [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills — packaged, reusable agent workflows you can drop into any project. Each skill is a self-contained folder (`SKILL.md` + any scripts) that teaches the agent a repeatable job: how to do it, what to reuse, and where the guardrails are.

Built and maintained by [promptmechanic](https://github.com/promptmechanic).

## What's a skill?

A skill is a Markdown file (`SKILL.md`) with YAML frontmatter — a `name` and a `description` that tells the agent *when* to reach for it — followed by the instructions the agent should follow. Some skills ship helper scripts alongside so the deterministic work (parsing, rendering, transforms) is done by code, and only the judgement is left to the model. Claude Code auto-discovers skills placed in `~/.claude/skills/` (global) or `<repo>/.claude/skills/` (per-project) and offers them as `/<skill-name>`.

## Skills

The full catalogue lives in **[`skills/`](skills/README.md)** — one folder per skill. Quick summary:

| Skill | What it does |
|-------|--------------|
| [`week-in-review`](skills/week-in-review) | End-of-week reflection: mines your Claude Code transcripts (last 7 days, all projects) into a self-contained HTML report — the topics you explored, distilled key learnings with live web-searched further-reading links, and a token / slash-command / skill / `ctx`-stack usage summary. Stay in the flow all week; learn later. |
| [`resume-review`](skills/resume-review) | Critical, prioritised resume/CV review against ATS parsing rules, the 7-second recruiter skim, and keyword alignment with a target job description. Scored findings ranked by how likely each is to cost an interview — a tough reviewer, not a rewrite. |
| [`humanize-text`](skills/humanize-text) | Rewrite AI-sounding prose so it reads as considered human writing — cuts em-dash pile-ups, "it's not X, it's Y" antitheses, inflated vocabulary and robotic rhythm while preserving every fact, claim and the author's own voice. Ships a stdlib scanner that flags the mechanical tells with line numbers. |

## Install

**One skill, globally** (available in every project):

```bash
git clone https://github.com/promptmechanic/ai-toolbox.git
cp -r ai-toolbox/skills/week-in-review ~/.claude/skills/
```

**One skill, for a single project** (travels with the repo, committed to version control):

```bash
mkdir -p .claude/skills
cp -r /path/to/ai-toolbox/skills/resume-review .claude/skills/
```

Then run it in Claude Code with `/week-in-review` or `/resume-review`, or just describe the task — the `description` frontmatter lets the agent pick the right skill automatically.

## Requirements

- Claude Code (CLI, desktop, or IDE extension).
- `week-in-review` and `humanize-text` run their helper scripts with **Python 3** (standard library only — no pip installs).
- `week-in-review`'s "further reading" step uses web search; it degrades gracefully offline (learnings without links).

## Contributing

Each skill lives in `skills/<name>/` with a `SKILL.md` at its root. Keep skills self-contained, put deterministic work in scripts, and document the guardrails. PRs welcome.

## License

[MIT](LICENSE) © 2026 William Foster
