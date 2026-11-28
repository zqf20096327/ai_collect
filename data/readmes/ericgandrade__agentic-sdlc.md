<h1 align="center">The Agentic SDLC Method</h1>

<p align="center"><b>v3.1.0</b> · Open source · MIT · Works in Claude Code, GitHub Copilot, Codex, Cursor, Gemini and 3 more tools</p>

<p align="center">
  <img alt="Version 3.1.0" src="https://img.shields.io/badge/version-3.1.0-blue.svg">
  <img alt="MIT License" src="https://img.shields.io/badge/license-MIT-green.svg">
  <img alt="23 skills" src="https://img.shields.io/badge/skills-23-brightgreen.svg">
  <img alt="8 AI tools" src="https://img.shields.io/badge/AI%20tools-8-1d3fbf.svg">
</p>

<p align="center"><img src="docs/assets/hero.svg" width="100%" alt="The definitive approach to AI-native software engineering. Agent-driven, human-governed, evidence-verified. 13 specialized agents, 23 integrated skills, 7 lifecycle stages."></p>

**A software delivery method for teams that build with AI coding agents.** Agents do the work, from the first spec to production. Named people approve each stage. Every requirement is proven with fresh evidence before anyone calls it done.

Coding agents can write a feature in minutes. What they do not give you is a reason to trust it: what exactly was asked, what proves it works, who checked it, and who approved it. The Agentic SDLC adds those answers to every change, and it sizes the ceremony to the change, so a one-line fix stays a one-line fix.

## The idea in one picture

![How the Agentic SDLC works: seven stages from idea to production, 13 specialized AI agents coordinated by a Scrum Master, and four human sign-offs](docs/assets/agentic-sdlc-overview.svg)

- **7 stages**, the standard software life cycle: Discover → Specify → Design → Build → Test → Release → Operate. Operate feeds the next Discover.
- **13 AI agents**, named by what they do. A Scrum Master agent runs the flow and calls a specialist only when the change needs one.
- **4 human sign-offs**: the Product Owner approves the spec, the Tech Lead the plan, a human reviewer the pull request, and the Release Owner the release.
- **3 paths** (Quick, Standard, Full), chosen from the size and risk of the change.

## Quick start

**1. Install** (Node 14 or later for the installer):

```bash
npx agentic-sdlc-method --bundle agentic-sdlc -y
```

This installs the skills into every supported AI tool it finds on your machine. For other options, open the section below.

<details>
<summary><b>Claude Code plugin, local install and other tools</b></summary>

**Claude Code plugin.** Run inside a `claude` session; skills then appear as `/agentic-sdlc:<name>`:

```text
/plugin marketplace add ericgandrade/agentic-sdlc
/plugin install agentic-sdlc@agentic-sdlc
```

**Without npm.** `git clone https://github.com/ericgandrade/agentic-sdlc && ./agentic-sdlc/scripts/local-install.sh`

**Per tool.** See [Supported AI tools](#supported-ai-tools) below and the [installation guide](docs/INSTALLATION.md).

</details>

**2. Set up your project.** Open your AI tool in the repository and ask:

> *"Set up the Agentic SDLC here."*

The agent reads your build and CI files and writes a short `AGENTS.md` block with your Definition of Done (lint, types, tests, coverage floor). It also installs the CI checks and copies the check scripts into `.agentic-sdlc/bin/`. It shows you everything and waits for your "yes" before writing.

**3. Make your first change:**

> *"Fix issue #142 with the Agentic SDLC."*

**What you should see:** the agent scores the change (for example `Path: Quick · S=3 · R=0`), writes one acceptance criterion, runs a failing test before it touches the code, and stops to ask for your approval at the end. If it writes code without a failing test first, or approves its own work, something is wrong: see [Troubleshooting](#troubleshooting).

The [quickstart](skills/agentic-sdlc/references/quickstart.md) walks through this first change step by step.

## See it in action

A Quick-path bug fix, condensed. The lines in grey boxes are what the agent prints.

> **You:** Fix issue #142 with the Agentic SDLC. The orders page shows dates in UTC.

```text
Path: Quick · S=3 · R=0 (no risk trigger)
AC-1  Given a user in America/Sao_Paulo, when they open /orders,
      then each date shows in their time zone.
```

> **Agent:** Wrote the test `#142 AC-1 shows dates in the user's time zone`. It fails (expected `09:00`, got `12:00`). Fixing `src/format-date.ts` now.

```text
PASS  lint · typecheck · test · coverage 81.2 ≥ 78.4   fingerprint 3f9c2a7d1e04
Reviewer (fresh context): lenses L1 spec, L2 correctness — 0 Critical, 1 Minor
```

> **Agent:** The PR is ready. Its Verification table shows each command, its exit code and the fingerprint of the tested files. Do you approve it (Test sign-off)?
>
> **You:** Approved.

```text
Agentic SDLC · Quick · #142
Discover ✅ ▸ Build ✅ ▸ Test ✅ Test sign-off ▸ Release ⏳
```

A feature goes the same way, with more stages: a spec and a plan that each get approved, acceptance tests written from the spec before any code, task-by-task Build, four review lenses, and a rehearsed rollback before release. The whole feature, file by file: [worked example](skills/agentic-sdlc/examples/worked-example/).

## Pick your path

The Analyst agent scores every change. **Size** counts files, components and iterations. **Risk** counts triggers: authentication, personal or health data, money, public API, schema change, irreversible action, regulated work. The path is the higher of the two.

| Path | Typical change | Human sign-offs | What gets written |
|---|---|---|---|
| **Quick** | A bug or small task, no risk trigger | Test (plus Release when it goes to production) | The issue with its acceptance test, and the PR with evidence |
| **Standard** | A feature, or one risk trigger | Specify, Design, Test, Release | `spec.md`, `plan.md`, acceptance tests, PR, release notes, retro |
| **Full** | An epic, legacy modernization, regulated work, two or more risk triggers, personal data or an irreversible action | All four, plus a second human reviewer | Standard set plus ADRs, threat model, constraints and runbook |

When a change turns out bigger or riskier than scored, the path goes up. It never goes down silently.

## The 7 stages

| Stage | The question | Lead agent | What it leaves behind | Sign-off |
|---|---|---|---|---|
| **1 · Discover** | Is it worth doing? How big and risky is it? | Analyst | Scored issue | |
| **2 · Specify** | What exactly must it do? | Analyst | `spec.md` with numbered acceptance criteria and non-goals | **Product Owner** |
| **3 · Design** | How will we build it? | Planner, Architect | `plan.md` with tasks, dependencies and decisions | **Tech Lead** |
| **4 · Build** | Does each task pass its test? | Developer | Commits traced to tasks and criteria | |
| **5 · Test** | Does it do what was asked, and nothing else? | Reviewer, Test Engineer | PR with fresh evidence and review findings | **Human reviewer** |
| **6 · Release** | Can we ship it and undo it? | Release Engineer | Release notes, rehearsed rollback | **Release Owner** |
| **7 · Operate** | Is it working, and what did we learn? | SRE | Ops record, incidents, retrospective actions | |

A sign-off counts only when a person answers in a later turn. Silence is never approval, and editing an approved spec or plan voids its sign-off.

## Meet the agents

The core agents (in bold) take part in most changes. The others join only when the change needs them.

| Agent | What it does | Joins when |
|---|---|---|
| **Scrum Master** | Reads the state of the work from the repository, picks the path, calls the right agent, asks people for sign-offs | Always |
| **Analyst** | Scores size and risk; writes the spec and its acceptance criteria | Always |
| Product Manager | Defines the problem, the expected outcome and the success indicator | New capability or unclear value |
| UX Designer | Designs journeys, screen states and accessibility | A user-facing screen changes |
| **Planner** | Splits the work into tasks of at most a day, with a dependency graph | Standard and Full paths |
| Architect | Records hard-to-reverse decisions as ADRs | New component, data model or integration |
| **Developer** | Writes the test first, then the code; one task per fresh context | Always |
| **Test Engineer** | Designs acceptance tests from the spec, without seeing the code | Standard and Full paths |
| **Reviewer** | Reviews in a fresh context, never edits code; the default verdict is NO-GO | Always |
| Security Auditor | Writes the threat model and runs the security review | Auth, personal data, money, public API |
| Tech Writer | Writes user docs and release notes | Users or operators see a change |
| Release Engineer | Rehearses the rollback, runs go/no-go and deploys | The change ships |
| SRE | Watches alerts, runs incidents and postmortems | The change runs in production |

## The skills

Each agent works through skills: Markdown workflows your AI tool loads when they apply. You rarely call them by name. Ask in plain language, and the `agentic-sdlc` router picks the right one.

<details>
<summary><b>All 23 skills, by stage</b></summary>

| Stage | Skill | Use it to |
|---|---|---|
| Router | `agentic-sdlc` | Run any change end to end; ask "what's next?" |
| Discover | `issue-triage` | Turn a request into a scored, decision-ready issue |
| Discover | `project-context` | Set up or adopt a repository: `AGENTS.md` block, Definition of Done, code map, CI checks |
| Discover | `brainstorming` | Shape an idea before any spec |
| Specify | `spec-driven-development` | Write `spec.md` with numbered acceptance criteria |
| Specify | `grill-me` | Stress-test a spec, plan or design with hard questions |
| Specify, Design | `codebase-modernization` | Change legacy code safely: inventory, characterization tests, migration slices |
| Specify, Test | `security-hardening` | Threat model, secure-build rules and security review |
| Design | `senior-solution-architect` | C4 diagrams, ADRs and design reviews |
| Design | `writing-plans` | Write `plan.md` as a task graph |
| Build | `executing-plans` | Run plan tasks one per fresh context, test first |
| Build | `test-driven-development` | Red, then green, then refactor |
| Build | `systematic-debugging` | Find a root cause with bounded hypotheses |
| Test | `test-strategy` | Design acceptance tests from the spec |
| Test | `verification-gate` | Turn "done" into fresh, fingerprinted evidence |
| Test | `multi-axis-code-review` | Review through four independent lenses |
| Release | `deployment-pipeline` | Enforce the checks in CI; staged rollout and rehearsed rollback |
| Release | `shipping-and-handover` | Pre-ship checklist, PR body, release notes, runbook |
| Operate | `operations-and-incidents` | Alerts, incidents and postmortems |
| Operate | `retrospective` | A retro whose actions change files |
| Support | `skill-creator` | Build and test new skills |
| Support | `agent-skill-discovery` | List the skills, agents and tool servers installed |
| Support | `agent-skill-orchestrator` | Plan a task across installed resources |

Bundles and the full catalog: [skills library](docs/skills-library.md).

</details>

## Why you can trust the output

![Two panels: an evidence chain from acceptance criterion to human sign-off, and the loop limits, budgets and authority limits that bound the agents](docs/assets/guardrails.svg)

| Without a method | With the Agentic SDLC |
|---|---|
| The agent builds what it guessed you meant | A spec with numbered acceptance criteria, approved before any code |
| "Done" means the agent says so | Each criterion has a test that was seen failing, then passing, on the exact files that ship |
| The agent checks its own work | Acceptance tests come from the spec alone, and a reviewer in a fresh context starts from NO-GO |
| Approval is a thumbs-up in chat | Four named sign-offs, each bound to a hash of the approved version |
| The agent loops on the same failure | Numeric limits (3 red-green tries, 5 build-test rounds, 3 review rounds), then a person decides |
| Every change gets the same heavy process | Three paths sized by size and risk |

The rules are backed by dependency-free Node scripts with 195 automated tests: `spec-lint`, `plan-graph`, `preflight`, `run-ledger`, `dod-gate`, `status`, `doctor`, `ext-check` and `budget-check`. The same checks run in CI from the day a team adopts the method. Without Node, the method runs from the Markdown rules, and the pull request says so (`enforcement: prompt-only`).

## How it compares

We scored the method against nine well-known approaches under a scoring methodology that was written and locked before any scoring.

![Bar chart of baseline scores for ten methods: Agentic SDLC 88.5 in first place, AWS AI-DLC 68.6, Agile V 67.0, BMad Method 66.8, Addy Osmani agent-skills 57.6, Superpowers 56.0, AWS Kiro 44.4, Matt Pocock skills 43.8, GitHub Spec Kit 43.2, OpenSpec 38.8](docs/assets/scores.svg)

| Method | Score | Strongest at | Where it is lighter |
|---|---:|---|---|
| **Agentic SDLC** | **88.5** | Spec quality, verification, review, loop control, release and operations | Ease of adoption, portability |
| [AWS AI-DLC](https://github.com/awslabs/aidlc-workflows) | 68.6 | Evidence bound to commits, context management | Heavy to start, needs its own runtime |
| [Agile V](https://agile-v.org) | 67.0 | Verification, portability, human governance | Little on release and learning |
| [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) | 66.8 | Easiest to adopt | Security opt-in, ends at a local commit |
| [Addy Osmani agent-skills](https://github.com/addyosmani/agent-skills) | 57.6 | TDD and code-quality guidance | No retrospective loop, thin review |
| [Superpowers](https://github.com/obra/superpowers) | 56.0 | Context discipline, TDD | Stops at the pull request |
| [AWS Kiro](https://kiro.dev) | 44.4 | Easy start (scored from documentation) | Tests optional, approvals not recorded |
| [Matt Pocock skills](https://github.com/mattpocock/skills) | 43.8 | Sharp context hygiene | No Definition of Done |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | 43.2 | Three commands to start, 40+ agents | Tests optional, weak review |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 38.8 | Precise change specs | Little traceability or security |

![Dot plot of the 16 criteria: the Agentic SDLC leads on 8, ties on 5 and is behind on ease of adoption, human governance and portability](docs/assets/criteria.svg)

**How to read these numbers.** It is our own evaluation: 16 criteria with evidence-based levels, five weightings, two AI scorers per method and a red-team audit. It compares documented and shipped mechanisms, not productivity in the field. The score above was measured on an earlier build of the method. This is how the numbers were produced:

![How we built it: research, a frozen scoring method, a failed first round at 53.2, gap closure, a second round at 88.5, and an end-to-end trial](docs/assets/journey.svg)

Methodology, every scorecard and the audits: [research](docs/research/) · [results](docs/research/scoring/results.md).

## Supported AI tools

| Tool | Installed to | Invoke |
|---|---|---|
| Claude Code | plugin, or `~/.claude/skills/` | `/agentic-sdlc:agentic-sdlc`, or ask in plain language |
| GitHub Copilot CLI | `~/.copilot/skills/` | Ask in plain language |
| OpenAI Codex | `~/.codex/skills/` | `Use agentic-sdlc to …` |
| Gemini CLI | `~/.gemini/skills/` | `Use agentic-sdlc to …` |
| Cursor IDE | `~/.cursor/skills/` | `@agentic-sdlc` in chat |
| OpenCode | `~/.agent/skills/` | `opencode run @agentic-sdlc` |
| Antigravity | `~/.gemini/antigravity/skills/` | Agent mode: `Use agentic-sdlc to …` |
| AdaL CLI | `~/.adal/skills/` | Loads on demand |

## Troubleshooting

| You see | Do this |
|---|---|
| Not sure what comes next | `node .agentic-sdlc/bin/status.mjs`: the current state, the evidence and the next step |
| Setup looks wrong after install or upgrade | `node .agentic-sdlc/bin/doctor.mjs`: seven checks, each with the command that fixes it |
| The PR says `enforcement: prompt-only` | Node or a host permission config is missing locally. CI still runs the checks; see [platforms](skills/agentic-sdlc/references/platforms.md) |
| Evidence marked stale | A file changed after the test run. Run the commands again (`dod-gate`); old output never counts |
| A check blocks a correct change | Ask for a waiver (owner ≠ requester, expiry ≤ 30 days). Never delete the check |
| An extension was refused | `ext-check --json` names the rule; see the [extension interface](skills/agentic-sdlc/references/extension-interface.md) |
| Upgrading from 3.0 | Follow [upgrading.md](skills/agentic-sdlc/references/upgrading.md) |

## Learn more

| | |
|---|---|
| [Quickstart](skills/agentic-sdlc/references/quickstart.md) | Your first change, step by step |
| [Worked example](skills/agentic-sdlc/examples/worked-example/) | One feature from spec to retrospective |
| [Method guide](docs/guides/agentic-sdlc.md) | The whole method, plus mappings to ISO/IEC/IEEE 12207, IEC 62304 and NIST SSDF |
| [Skills library](docs/skills-library.md) | Bundles, every platform and the catalog |
| [Changelog](CHANGELOG.md) | What changed in each release |

<details>
<summary><b>Terms used on this page</b></summary>

| Term | Meaning |
|---|---|
| Acceptance criterion (AC-1, AC-2…) | One numbered, testable statement of what the change must do, written before code |
| Sign-off | A person's explicit approval that closes a stage, recorded with the exact version approved |
| Path: Quick, Standard, Full | How much process a change gets, chosen from its size and risk |
| Red, then green | A test is run and seen to fail before the code is written, then seen to pass |
| Definition of Done | The project's own checks (lint, types, tests, coverage floor) that must pass |
| Fingerprint | A hash of the exact files that were tested; any later edit makes the evidence stale |
| Fresh context | A new agent session that has not seen the author's reasoning |
| Review lenses | Separate review passes, each with one focus: spec, correctness and design, security, adversarial |
| NO-GO | The reviewer's default verdict until every check passes |
| ADR | Architecture decision record: a short note on a hard-to-reverse choice |
| Skill, router, bundle | A skill is a Markdown workflow an AI tool loads; the router skill picks the right one; a bundle installs a set |

</details>

## Contributing and license

Issues and pull requests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Maintained by [Eric Andrade](https://github.com/ericgandrade).

MIT. Ideas adapted from other open-source projects are credited in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

---

*Version 3.1.0 | November 2026*
