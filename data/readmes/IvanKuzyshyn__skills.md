# Skills

Agent skills in the open [Agent Skills](https://agentskills.io) format. Each skill lives in `skills/<name>/`.

## Skills

| Skill | What it does |
|---|---|
| [twelve-factor-app](skills/twelve-factor-app/SKILL.md) | Design a service, or evaluate an existing codebase, against the [Twelve-Factor App](https://12factor.net) methodology |
| [idiomatic-go](skills/idiomatic-go/SKILL.md) | Score a Go project 0–100 and report severity-ranked findings across error handling, concurrency, correctness, API design, testing, readability, and build hygiene |

## Install

Pick one route. Installing both the plugin and skills.sh gives you every skill twice.

### Claude Code

```bash
claude plugin marketplace add IvanKuzyshyn/skills
claude plugin install ivankuzyshyn-skills@ivankuzyshyn
```

### Codex

```bash
codex plugin marketplace add IvanKuzyshyn/skills
codex plugin add ivankuzyshyn-skills@ivankuzyshyn
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add IvanKuzyshyn/skills
copilot plugin install ivankuzyshyn-skills@ivankuzyshyn
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/IvanKuzyshyn/skills`.

### Gemini CLI

```bash
gemini skills install https://github.com/IvanKuzyshyn/skills.git --path skills
```

### Any other agent (skills.sh)

```bash
npx skills@latest add IvanKuzyshyn/skills
```

Add `--skill=<name>` to install a single skill. Run `npx skills@latest update` to update.

## Releasing

The repo has one [semver](https://semver.org) version, shared by the plugin and all skills, managed with [Changesets](https://changesets.dev).

1. Every PR adds a changeset: `npx changeset`, then pick `patch`, `minor` or `major` and describe the change. CI fails PRs without one. For changes that should not release (CI, README typos), use `npx changeset --empty`.
2. Merging to `main` opens or updates a "Version skills" PR that bumps `package.json` and `.claude-plugin/plugin.json` and updates `CHANGELOG.md`.
3. Merging that PR tags `vX.Y.Z` and creates a GitHub release. Managed plugin installs pick up the new version.

## Credits

`twelve-factor-app` is based on the [Twelve-Factor App](https://github.com/twelve-factor/twelve-factor) community manifesto, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The skill text is an adaptation, with violation signals and patterns added for codebase evaluation.

`idiomatic-go` is original work, informed by [Effective Go](https://go.dev/doc/effective_go), [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments), the [Go Proverbs](https://go-proverbs.github.io), and Dave Cheney's [Practical Go](https://dave.cheney.net/practical-go).
