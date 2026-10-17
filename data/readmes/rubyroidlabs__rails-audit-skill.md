# Rails Audit Skill

An agent skill that performs comprehensive technical reviews of Ruby on Rails applications. Runs automated analysis tools, inspects source code for architecture and security issues, and produces a structured audit report with prioritized findings and a 0-10 score.

Built on **12+ years** of Ruby on Rails development experience at [Rubyroid Labs](https://rubyroidlabs.com/), and on the Rails community's open-source auditing tools (Brakeman, RubyCritic, bundler-audit, and others).

Works with any agent harness that supports skills — [Claude Code][claude-code], [Cursor][cursor], and others.

[claude-code]: https://docs.anthropic.com/en/docs/claude-code
[cursor]: https://cursor.com

## Table of contents

- [Overview](#overview)
- [Screenshots](#screenshots)
- [How the audit works](#how-the-audit-works)
- [Model recommendations](#model-recommendations)
- [Installation](#installation)
- [Usage](#usage)
  - [Full application audit](#full-application-audit)
  - [Targeted audit](#targeted-audit)
  - [Audit in parallel yourself](#audit-in-parallel-yourself)
- [What the audit covers](#what-the-audit-covers)
- [Tools used](#tools-used)
- [Reference materials](#reference-materials)
- [Contributing](#contributing)
- [License](#license)
- [About](#about)

## Overview

It reviews a Rails application and produces a structured technical report covering:

- **Source code health** — code complexity, duplication, and code smells via RubyCritic
- **Dead code detection** — potentially uncalled methods via Debride
- **Security** — static analysis via Brakeman, gem vulnerability scanning via bundler-audit, git secret detection via Gitleaks
- **Code quality** — linting with RuboCop or Standard, style consistency
- **Dependencies** — gem audit, outdated packages, unmaintained libraries
- **Testing** — test coverage via SimpleCov, test quality assessment
- **Architecture & Design** — code organization, SOLID principles, service objects
- **Database** — missing indexes, invalid associations (via Rails ERD), migration hygiene
- **Authorization** — Pundit/CanCanCan audit, policy scopes, bypass detection
- **Front-end** — JS framework assessment, internationalization, antipatterns
- **Git** — secret leaks, environment variable handling, git flow conventions
- **Infrastructure** — hosting, CI/CD, containerization, deployment
- **AI tooling** — AI-assisted development setup (CLAUDE.md, skills, MCP)

The output is a structured markdown report with each finding categorized by priority (Critical / High / Medium / Low) and accompanied by actionable recommendations. The report concludes with a 0-10 score and a tiered prioritization of next steps.

## Screenshots

Report overview — score, tool metrics, and section navigation:

![Audit report overview](./docs/audit-report-overview.png)

Prioritized findings with problem, priority, and solution:

![Audit report findings](./docs/audit-report-findings.png)

Critical security finding with code context:

![Audit report security finding](./docs/audit-report-security-finding.png)

## How the audit works

The audit runs in six phases:

| Phase | What happens |
|-------|--------------|
| **1. Discovery** | Verifies the project is Rails, extracts metadata (Ruby/Rails versions, DB, jobs, frontend, CI), checks that dependencies resolve and the app boots |
| **2. Tool selection** | Picks the right tools for the project: RuboCop vs Standard vs Standard+Rails, ESLint if configured, SimpleCov if tests exist |
| **3. Data collection** | Runs analysis tools in parallel subagents (RubyCritic, Brakeman, bundler-audit, Gitleaks, Debride) plus inline checks (linters, Rails ERD, importmap audit, rails stats). Optional tools are opt-in; nothing is installed permanently |
| **4. Reference loading** | Loads the detection pattern catalogs that guide the manual review |
| **5. Manual review** | Reads the actual source code across 7 areas — backend, frontend, testing, git, infrastructure, development setup, AI tooling — cross-referencing tool output with manual findings |
| **6. Report generation** | Writes `RAILS_AUDIT_REPORT.md`: findings grouped by severity, before/after code examples, a 0-10 score, and prioritized recommendations in three tiers |

The skill is designed to be non-invasive: any gem or npm package it needs is temporarily added, the tool is run, and everything is restored to its original state.

## Model recommendations

> ⚠️ **Disclaimer:** Audit quality depends on the AI model you use and how much reasoning it applies. Low-reasoning models often miss tricky or subtle issues. High-reasoning models dig deeper but take longer and consume more tokens — and tokens cost money. Runtime also varies by model provider (queueing, rate limits, and high demand can slow runs significantly). **Tracking usage and cost is your responsibility.**

The skill works with any model, but results vary significantly:

| Model tier | Recommended for | Notes |
|------------|-----------------|-------|
| **High reasoning** | Production audits, complex codebases, client deliverables | Best depth of analysis, but token-heavy and slower |
| **Medium reasoning** | Quick scans, small projects, triage | Good balance of speed and quality; may miss subtle issues in large codebases |
| **Low reasoning** | Fast pre-checks | Not recommended for full audits — likely to miss non-obvious findings |

**Example** (same ~700K LOC Rails project):

| Setup | Tokens | Time |
|-------|--------|------|
| Claude + Sonnet 5 | ~85M tokens | ~1 hour |
| Cursor + Grok 4.5 | ~4M tokens | ~25 min |

**Recommendation:** use a high-reasoning model when the audit is a client deliverable. The skill's phased architecture also allows mixing models — a lightweight model can run the automated tool collection (Phases 1–3) while a stronger model does the manual code review and report generation (Phases 5–6).

## Installation

Install with the skills CLI — this makes the skill available to any supported harness (Claude Code, Cursor, etc.):

```bash
npx skills@latest add rubyroidlabs/rails-audit-skill
```

This installs the skill into your global skills directory, where your harness picks it up automatically.

### Manual install (Claude Code)

If `npx skills` does not work with Claude Code, clone the skill into your Claude skills directory:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/rubyroidlabs/rails-audit-skill.git ~/.claude/skills/rails-audit-skill
```

For a project-local install (shared with the repo):

```bash
mkdir -p .claude/skills
git clone https://github.com/rubyroidlabs/rails-audit-skill.git .claude/skills/rails-audit-skill
```

## Usage

Invoke the skill from your agent harness. Examples:

```
/rails-audit-skill
```

### Full application audit

Run the skill from the root directory of your Rails project. It analyzes the entire application and writes `RAILS_AUDIT_REPORT.md`.

### Targeted audit

You can focus the audit on specific files or directories:

```
/rails-audit-skill audit app/models
```

### Audit in parallel yourself

While the agent runs the automated and code-level audit, review the project yourself at a higher level. The agent is strong at tools and source inspection; you are better placed to judge:

- **High-level architecture** — bounded contexts, service boundaries, how major subsystems fit together
- **Git practices** — branching strategy, commit quality, release/tagging habits
- **Collaboration processes** — code review norms, ownership, how the team ships and communicates

Use those observations alongside the generated report so process and architecture gaps are not left only to the model.

## What the audit covers

The audit is organized into these sections:

| Section | What's checked |
|---------|---------------|
| **Overview** | Technologies used, local setup experience, project description |
| **Back-end** | Source code health (RubyCritic), dependencies, gem vulnerabilities, code quality, security (Brakeman), authorization (Pundit/CanCanCan), code design & architecture, dead code, database structure |
| **Front-end** | JS frameworks, internationalization, front-end antipatterns |
| **Testing** | Code coverage (SimpleCov), test count, test run time, test quality |
| **Git** | Secret leaks (Gitleaks), environment variables, git flow conventions |
| **Infrastructure** | Hosting platform, CI/CD, containerization |
| **Development Setup** | README quality, Docker setup, seed data |
| **AI tooling** | AI-assisted development setup (CLAUDE.md, skills, MCP) |
| **Conclusion** | Score out of 10, prioritized recommendations in three tiers |

Each finding is presented with:
- **Problem** — what was found and why it matters
- **Priority** — Critical / High / Medium / Low
- **Solution** — specific, actionable recommendations

## Tools used

The skill automatically selects and runs the appropriate tools based on your project's configuration:

| Tool | What it measures | When it runs |
|------|-----------------|--------------|
| [RubyCritic](https://github.com/whitesmith/rubycritic) | Code complexity, duplication, smells (Reek + Flay + Flog) | Optional (recommended) |
| [SimpleCov](https://github.com/simplecov-ruby/simplecov) | Test coverage (line and branch) + test metrics | Optional, only if test directory exists |
| [Brakeman](https://brakemanscanner.org/) | Security static analysis | Always |
| [bundler-audit](https://github.com/rubysec/bundler-audit) | Gem vulnerability scanning | Always |
| [Gitleaks](https://gitleaks.io/) | Git secret detection | Always |
| [Debride](https://github.com/seattlerb/debride) | Dead code detection (uncalled methods) | Always |
| [RuboCop](https://rubocop.org/) or [Standard](https://github.com/standardrb/standard) | Ruby code style and linting | Always (auto-selected based on project config) |
| [ESLint](https://eslint.org/) | JavaScript linting | If project has eslint configured |
| [Rails ERD](https://voormedia.github.io/rails-erd/) | Entity-relationship diagram + invalid association detection | Always |
| Importmap audit | JS package vulnerability scan | If `bin/importmap` is available |
| Rails stats | Code-to-test ratio and LOC breakdown | Always |

### Linter selection

The skill auto-detects which linter to use:
1. If your project has `.rubocop.yml` or lists `rubocop` in its Gemfile → **RuboCop** is used
2. If your project has `.standard.yml` or lists `standard` in its Gemfile → **standardrb** is used
3. Otherwise → **standard + standard-rails** is used as the default

### How tools are run

Tools run as isolated subagents. If a tool isn't already in your Gemfile, it's temporarily added, the tool is run, and the Gemfile is restored to its original state. The working tree is verified clean at the end of the audit. Tools that can run standalone (Brakeman, bundler-audit, Gitleaks) avoid Gemfile modification entirely.

## License

This skill is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  <a href="https://rubyroidlabs.com">
    <img src="./docs/logo.svg" alt="Rubyroid Labs" width="100%" />
  </a>
</p>

**[Rubyroid Labs](https://rubyroidlabs.com)** — full-cycle software development company for businesses delivering scalable web and mobile apps, dedicated developers, and full-cycle teams in Ruby on Rails, React Native, and UX/UI. 98% on-time delivery.

- Website: [rubyroidlabs.com](https://rubyroidlabs.com)
- Email: [hi@rubyroidlabs.com](mailto:hi@rubyroidlabs.com)
- References: [Clutch](https://clutch.co/profile/rubyroid-labs)
