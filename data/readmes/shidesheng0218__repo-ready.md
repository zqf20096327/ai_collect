# RepoReady

[![npm](https://img.shields.io/npm/v/@shidesheng0218/repo-ready?color=111827&label=npm)](https://www.npmjs.com/package/@shidesheng0218/repo-ready)
[![CI](https://img.shields.io/github/actions/workflow/status/shidesheng0218/repo-ready/repoready.yml?branch=main&label=ci)](https://github.com/shidesheng0218/repo-ready/actions)
![Stars](https://img.shields.io/github/stars/shidesheng0218/repo-ready?style=flat)
![License](https://img.shields.io/badge/license-MIT-10b981)
![Node](https://img.shields.io/badge/node-%3E%3D20-339933)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-blue)

> **Make your repo ready for Codex, Claude Code, Cursor, and contributors.**
>
> **一行命令检查你的仓库是否适合 AI 编程代理协作。**

```bash
npx @shidesheng0218/repo-ready@latest
```

![RepoReady CLI preview](marketing-assets/launch-cli-hero.png)

RepoReady is a **CLI-first AI coding agent readiness checker and fixer**. It scans your repository, explains why agents may fail, and generates a reviewable fix plan. No server, no login, no AI API key, and no repository scripts are executed.

---

## Quick Start

### macOS / Linux / Windows

```bash
npx @shidesheng0218/repo-ready@latest
```

Windows PowerShell:

```powershell
npx.cmd @shidesheng0218/repo-ready@latest
```

### Chinese report

```bash
npx @shidesheng0218/repo-ready@latest --lang zh
```

### Screenshot-friendly output

```bash
npx @shidesheng0218/repo-ready@latest --compact
```

### v0.7.0: Agent Simulation, Doctor Mode, and CI Gate

```bash
# Predict where AI coding agents may fail before they touch code
npx @shidesheng0218/repo-ready@latest simulate

# Guided diagnosis and fix workflow
npx @shidesheng0218/repo-ready@latest doctor
npx @shidesheng0218/repo-ready@latest doctor --write

# Generate AGENTS.md, CLAUDE.md, and Cursor rules
npx @shidesheng0218/repo-ready@latest init-agent --dry-run
npx @shidesheng0218/repo-ready@latest init-agent --write

# Use RepoReady as a CI readiness gate
npx @shidesheng0218/repo-ready@latest --ci --min-score 80 --fail-on high,dangerous-script

# Check readiness for specific coding agents
npx @shidesheng0218/repo-ready@latest --profile codex
npx @shidesheng0218/repo-ready@latest --profile claude
npx @shidesheng0218/repo-ready@latest --profile cursor
```

### Fix plan and dry run

```bash
npx @shidesheng0218/repo-ready@latest fix --plan
npx @shidesheng0218/repo-ready@latest fix --dry-run
```

---

## Example output

```text
RepoReady Report - my-repo

Overall Score        82/100
Agent Ready          70/100
Safety               92/100

Agent Failure Risk
HIGH     Validation Gap
MEDIUM   Scope Drift
LOW      Safety Boundary

Evidence Chain
PASS     AGENTS.md detected
PASS     Test command detected
REVIEW   README contribution section missing

PR-ready Fixes
+ AGENTS.md
+ README.md
+ .github/workflows/repoready.yml

Next
npx @shidesheng0218/repo-ready@latest fix --dry-run
```

---

## What RepoReady checks

| Area | Checks |
|---|---|
| Agent instructions | `AGENTS.md`, `CLAUDE.md`, `.cursor/rules` |
| Validation | test, build, lint, typecheck commands |
| README quality | install, usage, test, contribution, demo signals |
| CI / workflow | GitHub Actions and verification workflow |
| Context quality | generated files, caches, large files, ignored folders |
| Safety | dangerous scripts, force push, DB reset, production deploys |
| Code quality | tests, checks, lockfiles, CI, source structure |

---

## Why developers use it

| Capability | What it gives you |
|---|---|
| **Agent Failure Risk** | Predicts why Codex, Claude Code, Cursor, or similar agents may fail in your repo. |
| **Audit Evidence Chain** | Shows the signals behind every score, not just a black-box number. |
| **Fix PR Plan** | Groups generated fixes into safe, review-required, and manual-only work. |

---

## Fix workflow

RepoReady is conservative by default. It previews changes before writing.

```bash
npx @shidesheng0218/repo-ready@latest fix --plan
npx @shidesheng0218/repo-ready@latest fix --dry-run
npx @shidesheng0218/repo-ready@latest fix --apply-safe
npx @shidesheng0218/repo-ready@latest fix --write
npx @shidesheng0218/repo-ready@latest fix --branch
npx @shidesheng0218/repo-ready@latest fix --pr --base main
```

Fix groups:

| Group | Meaning |
|---|---|
| Safe automatic fixes | Low-risk files such as `AGENTS.md`, `.gitignore`, `.env.example` |
| Review-required fixes | README, CI, templates, workflow changes |
| Manual-only boundaries | database, auth, payment, deployment, secrets, destructive scripts |

---

## Output formats

```bash
npx @shidesheng0218/repo-ready@latest --json
npx @shidesheng0218/repo-ready@latest --markdown
```

---

## Safety and privacy

- RepoReady does **not** execute repository scripts.
- Local scans do **not** upload private source code by default.
- Files are only written when you explicitly use write/apply commands.
- Dangerous scripts are flagged, not executed.
- AI enhancement is optional. No API key means no AI call and no AI cost.

---

## GitHub Action

```yaml
name: RepoReady

on:
  pull_request:
  push:

jobs:
  repoready:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./packages/action
        with:
          language: en
          min-score: 70
```

---

## Optional web reports

RepoReady is CLI-first. The web report is optional and can be self-hosted.

You do **not** need a domain, server, database, OAuth, or GitHub App to use RepoReady locally.

Optional web capabilities:

```text
/r/[owner]/[repo]
/badge/[owner]/[repo].svg
/share-card/[owner]/[repo].svg
/api/fix-pr
```

---

---

## FAQ

### Why does my repo score low?

Common reasons:
- No `AGENTS.md`, `CLAUDE.md`, or `.cursor/rules` files
- No test, build, or lint commands detected
- README is missing install, usage, or test sections
- Large generated files or caches in the repository
- Dangerous scripts in `package.json` (deploy, db reset, force push)

Run `npx @shidesheng0218/repo-ready@latest fix --plan` to see what RepoReady suggests.

### Is RepoReady safe for private repositories?

RepoReady does **not** upload your source code by default. Local scans stay on your machine. The optional AI enhancement requires an API key and only sends metadata, not source files.

### Does RepoReady execute my scripts?

No. RepoReady uses static analysis only. It reads files and parses configuration, but never executes repository scripts, test commands, or build commands.

### Does RepoReady need an AI API key?

No. RepoReady works fully offline by default. AI enhancement is optional and requires an API key (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`).

### How do I contribute new detection rules?

See `CONTRIBUTING.md`. Good first issues are listed in the README.

### Windows: `npx` command not found or blocked

Use `npx.cmd` instead of `npx`:

```powershell
npx.cmd @shidesheng0218/repo-ready@latest
```

If PowerShell blocks scripts, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### How do I create a Fix PR?

```bash
npx @shidesheng0218/repo-ready@latest fix --plan
npx @shidesheng0218/repo-ready@latest fix --dry-run
npx @shidesheng0218/repo-ready@latest fix --pr --base main
```

`fix --pr` requires a git repository, a remote named `origin`, and GitHub CLI authenticated with `gh auth login`.

---

## Troubleshooting

### `npx` downloads an old version

Use `@latest` to always get the newest release:

```bash
npx @shidesheng0218/repo-ready@latest
```

### Report shows "No test command detected" but I have tests

RepoReady detects common test frameworks (Jest, Mocha, Vitest, Go test, pytest, etc.). If your test command is not detected, open an issue with your `package.json` scripts.

### Chinese output shows garbled text

Use `--lang zh` flag:

```bash
npx @shidesheng0218/repo-ready@latest --lang zh
```

If your terminal still shows garbled text, try Windows Terminal or set your terminal encoding to UTF-8.

## Looking for contributors

Good first issues:

- Add Python framework detection rules
- Add Rust readiness checks
- Add Go project detection
- Improve dangerous script detection
- Improve README scoring for non-English projects

See `CONTRIBUTING.md` and `docs/launch-pack.md` for contribution and launch details.

---

## Local development

```bash
git clone https://github.com/shidesheng0218/repo-ready.git
cd repo-ready
node packages/cli/bin/repoready.js
node packages/cli/bin/repoready.js --compact
node packages/cli/bin/repoready.js fix --dry-run
```

Run checks:

```bash
node --test
npm run lint
npm run web:build
```

---

## Roadmap

- [x] CLI repository scanner
- [x] English and Chinese reports
- [x] Agent Failure Risk
- [x] Audit Evidence Chain
- [x] Fix plan and dry-run patches
- [x] Screenshot-friendly CLI output
- [x] GitHub Action wrapper
- [x] Optional self-hosted web report
- [x] Launch pack and marketing assets
- [ ] More language-specific rules
- [ ] More framework detection
- [ ] Public Agent Ready Index
- [ ] GitHub App Fix PR production flow
- [ ] Organization dashboard

---

## Links

- GitHub: https://github.com/shidesheng0218/repo-ready
- npm: https://www.npmjs.com/package/@shidesheng0218/repo-ready

---



## FAQ

### Does RepoReady execute my scripts?

No. RepoReady never executes repository scripts, build commands, test commands, or any user-defined code.

### Does RepoReady upload my source code?

No. Local scans do not upload private source code by default.

### Do I need an AI API key?

No. RepoReady works without any AI API key. AI enhancement is optional.

### Do I need a server or domain?

No. RepoReady is CLI-first. The web report is optional and can be self-hosted.

### Windows: `npx` is blocked by PowerShell execution policy?

Use `npx.cmd` instead of `npx`:

```powershell
npx.cmd @shidesheng0218/repo-ready@latest
```

Or run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Why is my score low?

RepoReady checks whether your repository has:

- Agent instructions (AGENTS.md, CLAUDE.md, Cursor rules)
- Test, build, and lint commands
- A clear README with install, usage, test, and contribution sections
- Clean context (no large generated files, caches, or ignored folders)
- Safe scripts (no dangerous deployment, database reset, or force push commands)

Missing any of these will lower your score.

### Can I contribute new rules?

Yes. See [CONTRIBUTING.md](CONTRIBUTING.md) and the Good First Issues section.

### How do I fix issues found by RepoReady?

Run:

```bash
npx @shidesheng0218/repo-ready@latest fix --dry-run
npx @shidesheng0218/repo-ready@latest fix --plan
```

This will show you what RepoReady can generate and which changes need human review.

## License

MIT
