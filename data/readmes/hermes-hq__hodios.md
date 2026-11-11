<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/brand/banner-light.png">
  <img alt="Hodios: open prompts for every AI tool" src="assets/brand/banner-dark.png" width="100%">
</picture>

### One open prompt library, native in every AI tool. Free forever.

<!-- stats:start -->
<b>10,241</b> entries &nbsp;·&nbsp; <b>22</b> domains &nbsp;·&nbsp; <b>182</b> categories &nbsp;·&nbsp; <b>307</b> personas &nbsp;·&nbsp; <b>222</b> workflows
<!-- stats:end -->

Prompts, personas and workflows for work, learning, creativity and everyday life.<br>
Each one is written once and installs in your AI tool's own format with one line.

[![GitHub stars](https://img.shields.io/github/stars/hermes-hq/hodios?style=flat&logo=github&label=stars&color=7c3aed)](https://github.com/hermes-hq/hodios/stargazers)
[![check](https://github.com/hermes-hq/hodios/actions/workflows/check.yml/badge.svg)](https://github.com/hermes-hq/hodios/actions/workflows/check.yml)
[![catalog](https://img.shields.io/github/v/release/hermes-hq/hodios?label=catalog&color=7c3aed)](https://github.com/hermes-hq/hodios/releases)
[![npm](https://img.shields.io/npm/v/@hermes-hq/hodios?label=npx%20%40hermes-hq%2Fhodios&color=cb3837)](https://www.npmjs.com/package/@hermes-hq/hodios)
[![content: CC0-1.0](https://img.shields.io/badge/content-CC0--1.0-green)](LICENSES/CC0-1.0.txt)
[![code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/anhaia)

[**Browse the library →**](https://hermes-ide.com/prompts) &nbsp;·&nbsp; [Try it in 10 seconds](#try-it-in-10-seconds) &nbsp;·&nbsp; [Where it stands](#where-it-stands) &nbsp;·&nbsp; [Suggest a prompt](https://github.com/hermes-hq/hodios/issues/new?template=new-prompt.yml) &nbsp;·&nbsp; [Contribute](CONTRIBUTING.md)

<sub>If Hodios saves you time, <a href="https://github.com/hermes-hq/hodios/stargazers">star the repo</a>. It is how other people find it.</sub>

</div>

---

<!-- tools:start -->
Works with **Claude Code** · **Codex** · **Cursor** · **GitHub Copilot** · **Gemini CLI** · **Antigravity** · **OpenCode** · **Windsurf** · **Zed** · **Continue** · **ChatGPT** · **claude.ai**.
<!-- tools:end -->

Anything else that reads Agent Skills or `AGENTS.md` works too. Coming soon as the built-in library of [Hermes IDE](https://hermes-ide.com) (the IDE, not Hermes Agent).

Every entry is written once and compiled to each tool's native format: Agent Skills, plugins, subagents, slash commands, rules files or plain paste-in text. Nothing to learn, nothing to run, no account, no API key.

<p align="center">
  <img src="assets/demo/cli-demo.svg" alt="A terminal in a Next.js project: hodios search &quot;pull request&quot; lists three review entries, hodios install review-pull-request --target claude-code writes .claude/skills/review-pull-request/SKILL.md, and the first lines of that skill file are shown." width="100%">
  <br><sub>Real output from the published CLI, recorded by <a href="tools/demo/record-cli.mjs"><code>tools/demo/record-cli.mjs</code></a>.</sub>
</p>

## Try it in 10 seconds

```sh
# Claude Code: a whole domain as one plugin
claude plugin marketplace add hermes-hq/hodios-dist
claude plugin install hodios-software-engineering@hodios

# Codex, Cursor, Copilot, OpenCode or any Agent Skills tool
npx skills add hermes-hq/hodios-dist --skill review-pull-request -a codex

# Search the whole catalog, ranked for the project you're in
npx @hermes-hq/hodios search
```

Using ChatGPT or claude.ai? Open any entry on [hermes-ide.com/prompts](https://hermes-ide.com/prompts), press Copy and paste it into a chat.

## Not just for code

A small taste. Every one of these is a single line to install.

| You want to… | Use |
|---|---|
| Get a pull request reviewed the way a careful senior engineer would | [`review-pull-request`](library/software-engineering/code-review/review-pull-request/) |
| Have a security subagent that only reports issues with a real attack path | [`security-auditor`](library/software-engineering/security/security-auditor/) |
| Find out whether an online shop is a scam before you pay | [`check-online-shop-legitimacy`](library/productivity/digital-safety/check-online-shop-legitimacy/) |
| Understand a scary error message and fix it safely | [`explain-error-message`](library/productivity/tech-help/explain-error-message/) |
| Ask for a raise with evidence, a number and a script | [`ask-for-raise`](library/career-hr/career-growth/ask-for-raise/) |
| Appeal a denied insurance claim against the policy wording | [`appeal-insurance-denial`](library/legal-admin/legal-correspondence/appeal-insurance-denial/) |
| Tell a child about a divorce, an illness or a death | [`explain-hard-topic-to-child`](library/parenting-family/parenting/explain-hard-topic-to-child/) |
| Plan a week of meals, with the shopping list grouped by aisle | [`plan-weekly-meals`](library/home-cooking/meal-planning/plan-weekly-meals/) |
| Build a training plan that progresses safely | [`build-training-plan`](library/health-wellbeing/fitness/build-training-plan/) |
| Budget a trip before you book it | [`plan-trip-budget`](library/travel/travel-logistics/plan-trip-budget/) |
| Compare a stack of papers for a literature review | [`build-literature-matrix`](library/research-science/literature-review/build-literature-matrix/) |
| Call an A/B test: ship, iterate or stop | [`analyze-ab-test-results`](library/data-analysis/statistics/analyze-ab-test-results/) |
| Balance a combat encounter for your tabletop party | [`balance-combat-encounter`](library/gaming-fun/tabletop-rpg/balance-combat-encounter/) |
| Rewrite a prompt for a reasoning model | [`adapt-prompt-for-reasoning-model`](library/prompting/prompt-engineering/adapt-prompt-for-reasoning-model/) |

[See every domain and category ↓](#whats-inside)

## What an entry looks like

One Markdown file with typed arguments, an explicit output contract and shared guardrails ([full file](library/software-engineering/code-review/review-pull-request/prompt.md)):

```markdown
---
id: review-pull-request
kind: prompt
title: Review a pull request
status: experimental
authorship: human
args:
  - {name: diff, type: text, required: true}
  - {name: focus, type: enum, enum: [correctness, security, performance, all], default: all}
output_contract: {format: markdown, sections: [Verdict, Findings, Missing tests]}
pairs_with: {personas: [code-reviewer, security-auditor]}
---
<task>
Review {{diff}}. If it is a PR URL or branch name, fetch the diff; if you cannot, ask for it once and stop.
1. Read the whole diff once before judging any hunk.
2. For each suspected defect, trace the input that triggers it. Drop it if you cannot construct one.
3. Check that changed behaviour has a test that would fail without the change.
</task>
```

Next to it sits an `evals.yaml`: realistic cases (here an off-by-one bug, an empty diff and a harmless comment fix) that set the entry against a plain one-line request, `Review this pull request: {{diff}}`, on models from two vendors, graded by a third. The compiler turns that one file into a Claude Code skill and slash command, a Codex skill, a Copilot prompt file, a Gemini command, a Cursor rule or paste-in text.

What the model gets, side by side:

| A plain request | The Hodios entry |
|---|---|
| `Review this pull request: <diff>` | Why the review matters and what a careful senior reviewer blocks on |
| | Three steps: read the whole diff, trace the input that triggers each defect, check for a test that would fail without the change |
| | Limits: at most 10 findings, no style comments, ask for anything missing instead of guessing |
| | A fixed output: Verdict, Findings as `path:line`, Missing tests |
| | One worked example of a good finding |

Run `npx @hermes-hq/hodios use review-pull-request` to see the full text your model receives.

## Why Hodios

- **Evals in the open.** Entries ship with eval cases that set them against a plain one-line request. An entry is marked stable only after it beats that request on models from two vendors, and every entry shows its status. [Where the library stands today ↓](#where-it-stands)
- **Native everywhere.** One source, compiled to each tool's real format and limits. No wrapper, no runtime, no lock-in.
- **The ones for you, not all of them.** Entries are tagged by stack, stage, needs and tool, so search puts what fits your project first.
- **Self-contained.** An installed entry never depends on another entry being installed.
- **Safe by construction.** Entries are text only: no scripts, no tool grants, no hidden characters, no download-and-run. Every change is linted and reviewed.
- **Free for any use.** Content is CC0: copy it into your repo, your product or your docs. A link back is appreciated, never required.
- **No telemetry in the library or the CLI.** They collect nothing. (The website, hermes-ide.com, uses analytics.)

## Install

Pick your tool. Each command was run against the published install tree in [hermes-hq/hodios-dist](https://github.com/hermes-hq/hodios-dist); swap the id or domain for any curated entry. The install tree holds the curated tier only (at most 2,000 entries, listed in [`curated.txt`](curated.txt)), because these installers download the whole repository. Every other entry installs with [the CLI](#use-the-cli).

| Tool | One line |
|---|---|
| **Claude Code** | `claude plugin marketplace add hermes-hq/hodios-dist && claude plugin install hodios-software-engineering@hodios` |
| **Codex, Cursor, Copilot, OpenCode and other Agent Skills tools** | `npx skills add hermes-hq/hodios-dist --skill review-pull-request -a codex` |
| **Gemini CLI** | `gemini skills install https://github.com/hermes-hq/hodios-dist --path skills/review-pull-request --consent` |
| **ChatGPT, claude.ai, anything else** | Copy `paste/<id>.md` from [hodios-dist](https://github.com/hermes-hq/hodios-dist/tree/main/paste), or run `npx @hermes-hq/hodios use <id>` for any entry |
| **Hermes IDE** | Coming soon: built in, in the Library tab. |

Claude Code installs a whole domain at a time: `hodios-software-engineering`, `hodios-education`, `hodios-travel` and so on, one plugin per domain. Then call an entry as `/hodios-software-engineering:review-pull-request`, or let Claude pick the subagents (`hodios-software-engineering:security-auditor`). For `npx skills`, `-a` takes `claude-code`, `codex`, `cursor`, `github-copilot`, `opencode`, `gemini-cli` and more; `--skill '*'` installs every curated entry.

### Use the CLI

The CLI searches the whole catalog, curated or not, ranks what fits your project and writes each tool's native files (rules and personas included, which the installers above do not cover). Run it with npx, or install it once to get the `hodios` command:

```sh
npx @hermes-hq/hodios install review-pull-request --target claude-code
npm install -g @hermes-hq/hodios                 # then use `hodios` directly

cd ~/my-project
hodios search                                    # what fits this project first, and why
hodios install review-pull-request python-style-rules --target cursor
hodios use review-pull-request --arg diff=@- < my-change.diff | claude -p
```

Targets: `claude-code`, `codex`, `cursor`, `copilot`, `gemini-cli`, `opencode`, `agents-md`, `paste`, `hermes` (Hermes IDE). `list` shows what is installed and `remove` takes it out again.

## Where it stands

Hodios is new, so here is exactly how far it has got. No eval results are published yet; they will be, entry by entry, as entries reach stable.

<!-- status:start -->
| Status | Entries | What it means |
|---|---:|---|
| Stable | 0 | Beat a plain one-line request on its own evals, on models from two vendors |
| Experimental | 139 | Has at least three eval cases (happy path, edge case, negative case); not yet promoted |
| Incubating | 10,102 | New; evals are optional at this stage |

- **10,236** of 10,241 entries ship with eval cases.
- Who wrote them: **2** by a person, **8,133** by a person with AI help, **2,077** drafted by AI.
- **1,995** entries are in the curated tier that the plugins and `npx skills` install. The CLI installs all 10,241.
<!-- status:end -->

The status and authorship of every entry are in its frontmatter. Every AI-assisted or AI-drafted entry names the contributor who reviewed it and signed it off, and every change goes through the same lint and review.

## What's inside

Five kinds of entry, each with one job. Use one on its own or combine them:

```mermaid
flowchart LR
    kPersona["🧑 <b>Persona</b><br/>who the AI is"] --> ai(("Your AI tool"))
    kRule["📏 <b>Rule</b><br/>what it always follows"] --> ai
    kPrompt["✅ <b>Prompt</b><br/>one task to do"] --> ai
    kWorkflow["🗺️ <b>Workflow</b><br/>several steps, in order"] --> ai
    kStyle["🎨 <b>Style</b><br/>how the answer reads"] --> ai
    ai --> result["Better result"]
```

| Kind | What it is | Becomes |
|---|---|---|
| **Prompt** | A task with typed inputs: review a PR, find a root cause, write a migration | Skill, slash command, Copilot prompt file, Gemini command |
| **Persona** | Who the agent is and how it works: security auditor, debugger, tech writer | Subagent, output style, custom agent, project instructions |
| **Workflow** | Ordered steps with approval gates: feature track, literature review | Skill with the steps inlined, Copilot prompt file, Gemini command, Hermes Track |
| **Rule** | Always-on project instructions: TypeScript strictness, commit conventions | AGENTS.md / CLAUDE.md / GEMINI.md section, Cursor rule, Copilot instructions |
| **Style** | An output modifier with 5 levels: concise, diff-only, beginner-friendly | Output style or appended instructions |

Entries are organised by domain and category, from **code review**, **debugging** and **testing** to **teaching**, **trip planning** and **statistics**. The full list is below.

### The ones for you, not all of them

Every entry is tagged with what it is for: the **stack** it targets (TypeScript, Django, Terraform…), the **stage** of work (plan, build, review, operate…), what it **needs** (repo access, shell, an MCP server) and which **tools** it works in. Hermes IDE, the site and the CLI use those tags to put the entries that match your project and your interests first, so you see a short, relevant list instead of the whole catalog. Stack-agnostic entries stay visible to everyone.

In a project folder, `npx @hermes-hq/hodios search` with no query does this on your machine: it reads the project's manifests and agent config folders, ranks what fits first and says why ("your project uses React"). Nothing is sent anywhere, and `--all` turns it off.

<!-- catalog:start -->
**10241 entries** (9572 prompts, 307 personas, 222 workflows, 104 rules, 36 styles).

<details><summary><b>Software engineering</b> · 2107</summary>

| Category | Entries | Try |
|---|---:|---|
| Implementation | 163 | [`add-feature-flag`](library/software-engineering/implementation/add-feature-flag/) · [`add-low-power-sleep-modes`](library/software-engineering/implementation/add-low-power-sleep-modes/) · [`add-rate-limiting`](library/software-engineering/implementation/add-rate-limiting/) |
| Migration | 104 | [`adopt-swift-6-strict-concurrency`](library/software-engineering/migration/adopt-swift-6-strict-concurrency/) · [`convert-class-components-to-hooks`](library/software-engineering/migration/convert-class-components-to-hooks/) · [`convert-infrastructure-between-iac-tools`](library/software-engineering/migration/convert-infrastructure-between-iac-tools/) |
| Debugging | 103 | [`bisect-regression`](library/software-engineering/debugging/bisect-regression/) · [`configure-ide-debugger`](library/software-engineering/debugging/configure-ide-debugger/) · [`debug-bus-communication`](library/software-engineering/debugging/debug-bus-communication/) |
| AI and ML engineering | 102 | [`add-ai-feature-to-app`](library/software-engineering/ai-ml/add-ai-feature-to-app/) · [`add-human-approval-to-agent-actions`](library/software-engineering/ai-ml/add-human-approval-to-agent-actions/) · [`add-llm-output-guardrails`](library/software-engineering/ai-ml/add-llm-output-guardrails/) |
| DevOps | 101 | [`add-quality-gates-to-ci`](library/software-engineering/devops/add-quality-gates-to-ci/) · [`automate-mobile-app-signing`](library/software-engineering/devops/automate-mobile-app-signing/) · [`automate-release-versioning`](library/software-engineering/devops/automate-release-versioning/) |
| Testing | 101 | [`add-characterization-tests`](library/software-engineering/testing/add-characterization-tests/) · [`add-regression-test`](library/software-engineering/testing/add-regression-test/) · [`automate-manual-test-cases`](library/software-engineering/testing/automate-manual-test-cases/) |
| Data engineering | 99 | [`add-foreign-keys-to-legacy-schema`](library/software-engineering/data/add-foreign-keys-to-legacy-schema/) · [`add-read-replicas`](library/software-engineering/data/add-read-replicas/) · [`automate-postgres-backups`](library/software-engineering/data/automate-postgres-backups/) |
| Security | 99 | [`add-csrf-protection`](library/software-engineering/security/add-csrf-protection/) · [`add-security-scanning-to-ci`](library/software-engineering/security/add-security-scanning-to-ci/) · [`adopt-strict-csp`](library/software-engineering/security/adopt-strict-csp/) |
| Refactoring | 93 | [`apply-design-pattern`](library/software-engineering/refactoring/apply-design-pattern/) · [`centralize-input-validation`](library/software-engineering/refactoring/centralize-input-validation/) · [`clean-up-ai-generated-code`](library/software-engineering/refactoring/clean-up-ai-generated-code/) |
| Architecture | 92 | [`align-architecture-with-teams`](library/software-engineering/architecture/align-architecture-with-teams/) · [`assess-technical-due-diligence`](library/software-engineering/architecture/assess-technical-due-diligence/) · [`choose-api-style`](library/software-engineering/architecture/choose-api-style/) |
| Code review | 92 | [`check-library-usage-against-docs`](library/software-engineering/code-review/check-library-usage-against-docs/) · [`check-pr-matches-design-doc`](library/software-engineering/code-review/check-pr-matches-design-doc/) · [`check-semver-impact-of-diff`](library/software-engineering/code-review/check-semver-impact-of-diff/) |
| Performance | 90 | [`analyze-load-test-results`](library/software-engineering/performance/analyze-load-test-results/) · [`compare-benchmark-runs`](library/software-engineering/performance/compare-benchmark-runs/) · [`diagnose-cpu-spike`](library/software-engineering/performance/diagnose-cpu-spike/) |
| Documentation | 89 | [`annotate-config-file`](library/software-engineering/docs/annotate-config-file/) · [`audit-documentation`](library/software-engineering/docs/audit-documentation/) · [`audit-readme-conversion`](library/software-engineering/docs/audit-readme-conversion/) |
| Git and version control | 88 | [`add-ticket-ids-to-commits`](library/software-engineering/git/add-ticket-ids-to-commits/) · [`address-review-with-fixup-commits`](library/software-engineering/git/address-review-with-fixup-commits/) · [`audit-repository-access`](library/software-engineering/git/audit-repository-access/) |
| Conventions | 68 | [`audit-lint-configuration`](library/software-engineering/conventions/audit-lint-configuration/) · [`configure-linter-and-formatter`](library/software-engineering/conventions/configure-linter-and-formatter/) · [`find-inconsistent-code-patterns`](library/software-engineering/conventions/find-inconsistent-code-patterns/) |
| Security operations | 67 | [`analyze-dns-logs-for-c2`](library/software-engineering/security-operations/analyze-dns-logs-for-c2/) · [`analyze-email-headers`](library/software-engineering/security-operations/analyze-email-headers/) · [`analyze-malicious-office-document`](library/software-engineering/security-operations/analyze-malicious-office-document/) |
| Open source maintenance | 66 | [`adopt-abandoned-project`](library/software-engineering/open-source/adopt-abandoned-project/) · [`announce-maintenance-pause`](library/software-engineering/open-source/announce-maintenance-pause/) · [`assess-cyber-resilience-act-impact`](library/software-engineering/open-source/assess-cyber-resilience-act-impact/) |
| Accessibility | 65 | [`add-accessible-keyboard-shortcuts`](library/software-engineering/accessibility/add-accessible-keyboard-shortcuts/) · [`add-live-region-announcements`](library/software-engineering/accessibility/add-live-region-announcements/) · [`assess-european-accessibility-act-readiness`](library/software-engineering/accessibility/assess-european-accessibility-act-readiness/) |
| Incident and operations | 65 | [`analyze-incident-logs`](library/software-engineering/incident/analyze-incident-logs/) · [`audit-postmortem-action-items`](library/software-engineering/incident/audit-postmortem-action-items/) · [`audit-runbook-library`](library/software-engineering/incident/audit-runbook-library/) |
| Localization (software) | 65 | [`add-hardcoded-string-lint-checks`](library/software-engineering/localization/add-hardcoded-string-lint-checks/) · [`audit-translation-keys`](library/software-engineering/localization/audit-translation-keys/) · [`automate-translation-file-sync`](library/software-engineering/localization/automate-translation-file-sync/) |
| Learning to code | 64 | [`coach-coding-kata`](library/software-engineering/learning/coach-coding-kata/) · [`create-coding-exercises`](library/software-engineering/learning/create-coding-exercises/) · [`decode-developer-jargon`](library/software-engineering/learning/decode-developer-jargon/) |
| Planning | 64 | [`assess-scope-change-request`](library/software-engineering/planning/assess-scope-change-request/) · [`assess-technical-debt`](library/software-engineering/planning/assess-technical-debt/) · [`assign-work-across-developers`](library/software-engineering/planning/assign-work-across-developers/) |
| Coding-agent operations | 62 | [`add-agent-friendly-dev-commands`](library/software-engineering/meta/add-agent-friendly-dev-commands/) · [`assess-coding-agent-impact`](library/software-engineering/meta/assess-coding-agent-impact/) · [`assess-task-for-agent-delegation`](library/software-engineering/meta/assess-task-for-agent-delegation/) |
| Developer writing | 58 | [`adapt-internal-doc-for-public-post`](library/software-engineering/writing/adapt-internal-doc-for-public-post/) · [`announce-technical-decision`](library/software-engineering/writing/announce-technical-decision/) · [`explain-cloud-bill-to-finance`](library/software-engineering/writing/explain-cloud-bill-to-finance/) |
| Product (engineering) | 47 | [`define-non-functional-requirements`](library/software-engineering/product/define-non-functional-requirements/) · [`document-existing-feature-behaviour`](library/software-engineering/product/document-existing-feature-behaviour/) · [`extract-requirements-from-notes`](library/software-engineering/product/extract-requirements-from-notes/) |

</details>

<details><summary><b>Learning and education</b> · 590</summary>

| Category | Entries | Try |
|---|---:|---|
| Teaching | 126 | [`adapt-text-reading-level`](library/education/teaching/adapt-text-reading-level/) · [`align-lesson-to-standards`](library/education/teaching/align-lesson-to-standards/) · [`analyze-class-assessment-results`](library/education/teaching/analyze-class-assessment-results/) |
| Tutoring | 116 | [`analyze-artwork-formally`](library/education/tutoring/analyze-artwork-formally/) · [`analyze-fieldwork-data`](library/education/tutoring/analyze-fieldwork-data/) · [`analyze-film-scene-for-coursework`](library/education/tutoring/analyze-film-scene-for-coursework/) |
| Studying | 106 | [`act-on-marked-feedback`](library/education/studying/act-on-marked-feedback/) · [`adapt-study-for-learning-difference`](library/education/studying/adapt-study-for-learning-difference/) · [`analyze-exam-mistakes`](library/education/studying/analyze-exam-mistakes/) |
| Exam preparation | 100 | [`analyze-past-papers`](library/education/exam-prep/analyze-past-papers/) · [`build-exam-pressure-practice`](library/education/exam-prep/build-exam-pressure-practice/) · [`coach-enem-essay`](library/education/exam-prep/coach-enem-essay/) |
| Course design | 70 | [`adapt-course-for-low-bandwidth`](library/education/course-design/adapt-course-for-low-bandwidth/) · [`analyze-course-evaluations`](library/education/course-design/analyze-course-evaluations/) · [`build-course-reading-list`](library/education/course-design/build-course-reading-list/) |
| Special education and inclusion | 37 | [`adapt-lesson-for-hearing-impaired-pupil`](library/education/special-education/adapt-lesson-for-hearing-impaired-pupil/) · [`adapt-lesson-for-visually-impaired-pupil`](library/education/special-education/adapt-lesson-for-visually-impaired-pupil/) · [`break-down-life-skill-task`](library/education/special-education/break-down-life-skill-task/) |
| Homeschooling | 35 | [`adapt-homeschool-for-learning-differences`](library/education/homeschooling/adapt-homeschool-for-learning-differences/) · [`build-homeschool-portfolio`](library/education/homeschooling/build-homeschool-portfolio/) · [`choose-homeschool-approach`](library/education/homeschooling/choose-homeschool-approach/) |

</details>

<details><summary><b>Languages</b> · 233</summary>

| Category | Entries | Try |
|---|---:|---|
| Language learning | 109 | [`adapt-coursebook-unit-to-learners`](library/languages/language-learning/adapt-coursebook-unit-to-learners/) · [`adapt-language-learning-for-dyslexia`](library/languages/language-learning/adapt-language-learning-for-dyslexia/) · [`adapt-language-study-for-hearing-loss`](library/languages/language-learning/adapt-language-study-for-hearing-loss/) |
| Conversation practice | 72 | [`ask-pharmacist-in-language`](library/languages/conversation-practice/ask-pharmacist-in-language/) · [`build-interview-answer-bank-in-language`](library/languages/conversation-practice/build-interview-answer-bank-in-language/) · [`decode-regional-speech-in-conversation`](library/languages/conversation-practice/decode-regional-speech-in-conversation/) |
| Translation | 52 | [`adapt-public-notice-for-many-languages`](library/languages/translation/adapt-public-notice-for-many-languages/) · [`adapt-regional-variant`](library/languages/translation/adapt-regional-variant/) · [`adapt-script-for-dubbing`](library/languages/translation/adapt-script-for-dubbing/) |

</details>

<details><summary><b>Content creation</b> · 372</summary>

| Category | Entries | Try |
|---|---:|---|
| Social media | 69 | [`adapt-post-across-platforms`](library/content-creation/social-media/adapt-post-across-platforms/) · [`apply-moderation-policy-to-comments`](library/content-creation/social-media/apply-moderation-policy-to-comments/) · [`brainstorm-brand-memes`](library/content-creation/social-media/brainstorm-brand-memes/) |
| Blogging | 55 | [`edit-blog-post-draft`](library/content-creation/blogging/edit-blog-post-draft/) · [`edit-transcript-into-article`](library/content-creation/blogging/edit-transcript-into-article/) · [`generate-blog-post-ideas`](library/content-creation/blogging/generate-blog-post-ideas/) |
| Video | 54 | [`adapt-script-for-teleprompter`](library/content-creation/video/adapt-script-for-teleprompter/) · [`adapt-trend-format`](library/content-creation/video/adapt-trend-format/) · [`analyze-video-retention`](library/content-creation/video/analyze-video-retention/) |
| Podcasting | 46 | [`build-episode-research-brief`](library/content-creation/podcasting/build-episode-research-brief/) · [`build-guest-booking-tracker`](library/content-creation/podcasting/build-guest-booking-tracker/) · [`choose-podcast-setup`](library/content-creation/podcasting/choose-podcast-setup/) |
| Newsletters | 40 | [`announce-newsletter-change`](library/content-creation/newsletters/announce-newsletter-change/) · [`audit-newsletter-performance`](library/content-creation/newsletters/audit-newsletter-performance/) · [`build-evergreen-issue-bank`](library/content-creation/newsletters/build-evergreen-issue-bank/) |
| Content strategy | 36 | [`analyze-competitor-channels`](library/content-creation/content-strategy/analyze-competitor-channels/) · [`analyze-content-performance`](library/content-creation/content-strategy/analyze-content-performance/) · [`assess-community-information-needs`](library/content-creation/content-strategy/assess-community-information-needs/) |
| Creator business | 36 | [`build-creator-rate-card`](library/content-creation/creator-business/build-creator-rate-card/) · [`design-creator-coaching-offer`](library/content-creation/creator-business/design-creator-coaching-offer/) · [`design-membership-tiers`](library/content-creation/creator-business/design-membership-tiers/) |
| Livestreaming | 36 | [`audit-stream-for-privacy-leaks`](library/content-creation/livestreaming/audit-stream-for-privacy-leaks/) · [`choose-first-streaming-setup`](library/content-creation/livestreaming/choose-first-streaming-setup/) · [`choose-stream-music-safely`](library/content-creation/livestreaming/choose-stream-music-safely/) |

</details>

<details><summary><b>Marketing and sales</b> · 539</summary>

| Category | Entries | Try |
|---|---:|---|
| Sales | 91 | [`analyze-sales-funnel-metrics`](library/marketing-sales/sales/analyze-sales-funnel-metrics/) · [`answer-price-shopper-calls`](library/marketing-sales/sales/answer-price-shopper-calls/) · [`ask-clients-for-referrals`](library/marketing-sales/sales/ask-clients-for-referrals/) |
| Copywriting | 77 | [`adapt-copy-for-segments`](library/marketing-sales/copywriting/adapt-copy-for-segments/) · [`analyze-competitor-copy`](library/marketing-sales/copywriting/analyze-competitor-copy/) · [`audit-landing-page-conversion`](library/marketing-sales/copywriting/audit-landing-page-conversion/) |
| SEO | 76 | [`add-seo-to-nextjs-app`](library/marketing-sales/seo/add-seo-to-nextjs-app/) · [`analyze-search-console-data`](library/marketing-sales/seo/analyze-search-console-data/) · [`analyze-serp-for-keyword`](library/marketing-sales/seo/analyze-serp-for-keyword/) |
| Advertising | 66 | [`analyze-ad-performance`](library/marketing-sales/advertising/analyze-ad-performance/) · [`analyze-competitor-ads`](library/marketing-sales/advertising/analyze-competitor-ads/) · [`analyze-creative-test-results`](library/marketing-sales/advertising/analyze-creative-test-results/) |
| Marketing strategy | 66 | [`analyze-channel-performance`](library/marketing-sales/marketing-strategy/analyze-channel-performance/) · [`analyze-competitors`](library/marketing-sales/marketing-strategy/analyze-competitors/) · [`brainstorm-guerrilla-marketing`](library/marketing-sales/marketing-strategy/brainstorm-guerrilla-marketing/) |
| Email marketing | 63 | [`analyze-email-campaign-report`](library/marketing-sales/email-marketing/analyze-email-campaign-report/) · [`announce-last-minute-openings`](library/marketing-sales/email-marketing/announce-last-minute-openings/) · [`audit-email-deliverability`](library/marketing-sales/email-marketing/audit-email-deliverability/) |
| E-commerce | 55 | [`audit-product-catalog-data`](library/marketing-sales/ecommerce/audit-product-catalog-data/) · [`audit-store-app-stack`](library/marketing-sales/ecommerce/audit-store-app-stack/) · [`audit-store-homepage-and-navigation`](library/marketing-sales/ecommerce/audit-store-homepage-and-navigation/) |
| Public relations | 45 | [`audit-online-newsroom`](library/marketing-sales/public-relations/audit-online-newsroom/) · [`build-crisis-comms-plan`](library/marketing-sales/public-relations/build-crisis-comms-plan/) · [`build-media-list`](library/marketing-sales/public-relations/build-media-list/) |

</details>

<details><summary><b>Product management</b> · 330</summary>

| Category | Entries | Try |
|---|---:|---|
| Product discovery | 58 | [`analyze-competitor-reviews`](library/product-management/product-discovery/analyze-competitor-reviews/) · [`audit-idea-evidence`](library/product-management/product-discovery/audit-idea-evidence/) · [`build-job-map`](library/product-management/product-discovery/build-job-map/) |
| Product metrics | 57 | [`analyze-conversion-funnel`](library/product-management/product-metrics/analyze-conversion-funnel/) · [`analyze-feature-adoption`](library/product-management/product-metrics/analyze-feature-adoption/) · [`analyze-free-to-paid-conversion`](library/product-management/product-metrics/analyze-free-to-paid-conversion/) |
| Roadmapping | 55 | [`align-roadmap-to-okrs`](library/product-management/roadmapping/align-roadmap-to-okrs/) · [`allocate-capacity-across-departments`](library/product-management/roadmapping/allocate-capacity-across-departments/) · [`answer-customer-roadmap-question`](library/product-management/roadmapping/answer-customer-roadmap-question/) |
| Product launch | 54 | [`brief-frontline-staff-on-release`](library/product-management/product-launch/brief-frontline-staff-on-release/) · [`build-launch-budget`](library/product-management/product-launch/build-launch-budget/) · [`build-launch-press-kit`](library/product-management/product-launch/build-launch-press-kit/) |
| Product strategy | 53 | [`apply-product-thinking-to-programme`](library/product-management/product-strategy/apply-product-thinking-to-programme/) · [`assess-ai-disruption-risk`](library/product-management/product-strategy/assess-ai-disruption-risk/) · [`assess-platform-dependency-risk`](library/product-management/product-strategy/assess-platform-dependency-risk/) |
| User feedback | 53 | [`analyze-ai-feature-feedback`](library/product-management/user-feedback/analyze-ai-feature-feedback/) · [`analyze-app-store-reviews`](library/product-management/user-feedback/analyze-app-store-reviews/) · [`analyze-cancellation-feedback`](library/product-management/user-feedback/analyze-cancellation-feedback/) |

</details>

<details><summary><b>Business and strategy</b> · 541</summary>

| Category | Entries | Try |
|---|---:|---|
| Customer support | 108 | [`analyze-support-tickets`](library/business/customer-support/analyze-support-tickets/) · [`answer-product-warranty-claim`](library/business/customer-support/answer-product-warranty-claim/) · [`audit-help-center-content`](library/business/customer-support/audit-help-center-content/) |
| Operations | 84 | [`audit-sop-library`](library/business/operations/audit-sop-library/) · [`audit-supplier-factory`](library/business/operations/audit-supplier-factory/) · [`automate-business-workflow`](library/business/operations/automate-business-workflow/) |
| Entrepreneurship | 73 | [`assess-founder-fit`](library/business/entrepreneurship/assess-founder-fit/) · [`build-pre-launch-waitlist`](library/business/entrepreneurship/build-pre-launch-waitlist/) · [`check-business-opportunity-for-red-flags`](library/business/entrepreneurship/check-business-opportunity-for-red-flags/) |
| Business strategy | 71 | [`analyze-business-case-study`](library/business/business-strategy/analyze-business-case-study/) · [`analyze-business-model`](library/business/business-strategy/analyze-business-model/) · [`analyze-competitor-financials`](library/business/business-strategy/analyze-competitor-financials/) |
| Farming | 55 | [`answer-farm-audit-findings`](library/business/farming/answer-farm-audit-findings/) · [`answer-neighbour-farm-complaint`](library/business/farming/answer-neighbour-farm-complaint/) · [`budget-winter-forage-stocks`](library/business/farming/budget-winter-forage-stocks/) |
| Restaurants and hospitality | 40 | [`answer-group-booking-enquiry`](library/business/hospitality/answer-group-booking-enquiry/) · [`build-allergen-matrix`](library/business/hospitality/build-allergen-matrix/) · [`build-restaurant-wine-list`](library/business/hospitality/build-restaurant-wine-list/) |
| Nonprofits and charities | 37 | [`answer-donor-service-queries`](library/business/nonprofit/answer-donor-service-queries/) · [`assess-charity-merger-options`](library/business/nonprofit/assess-charity-merger-options/) · [`build-board-skills-matrix`](library/business/nonprofit/build-board-skills-matrix/) |
| Real estate | 37 | [`abstract-property-lease`](library/business/real-estate/abstract-property-lease/) · [`analyze-property-comparables`](library/business/real-estate/analyze-property-comparables/) · [`analyze-rental-property`](library/business/real-estate/analyze-rental-property/) |
| Fundraising | 36 | [`build-investor-pipeline`](library/business/fundraising/build-investor-pipeline/) · [`calculate-safe-conversion`](library/business/fundraising/calculate-safe-conversion/) · [`choose-funding-instrument`](library/business/fundraising/choose-funding-instrument/) |

</details>

<details><summary><b>Data analysis</b> · 428</summary>

| Category | Entries | Try |
|---|---:|---|
| Spreadsheets | 84 | [`add-change-log-to-shared-sheet`](library/data-analysis/spreadsheets/add-change-log-to-shared-sheet/) · [`allocate-shared-costs`](library/data-analysis/spreadsheets/allocate-shared-costs/) · [`audit-spreadsheet-model`](library/data-analysis/spreadsheets/audit-spreadsheet-model/) |
| Data exploration | 83 | [`analyze-competitor-price-data`](library/data-analysis/data-exploration/analyze-competitor-price-data/) · [`analyze-contact-centre-data`](library/data-analysis/data-exploration/analyze-contact-centre-data/) · [`analyze-delivery-performance`](library/data-analysis/data-exploration/analyze-delivery-performance/) |
| Statistics | 71 | [`analyze-ab-test-results`](library/data-analysis/statistics/analyze-ab-test-results/) · [`analyze-likert-data`](library/data-analysis/statistics/analyze-likert-data/) · [`analyze-small-sample-data`](library/data-analysis/statistics/analyze-small-sample-data/) |
| Reporting | 70 | [`announce-metric-definition-change`](library/data-analysis/reporting/announce-metric-definition-change/) · [`announce-new-dashboard`](library/data-analysis/reporting/announce-new-dashboard/) · [`anticipate-report-questions`](library/data-analysis/reporting/anticipate-report-questions/) |
| Data visualisation | 64 | [`adapt-chart-for-mobile`](library/data-analysis/data-visualization/adapt-chart-for-mobile/) · [`animate-chart`](library/data-analysis/data-visualization/animate-chart/) · [`audit-dashboard`](library/data-analysis/data-visualization/audit-dashboard/) |
| Forecasting | 56 | [`add-event-adjustments-to-forecast`](library/data-analysis/forecasting/add-event-adjustments-to-forecast/) · [`adjust-forecast-for-weather`](library/data-analysis/forecasting/adjust-forecast-for-weather/) · [`build-driver-based-revenue-forecast`](library/data-analysis/forecasting/build-driver-based-revenue-forecast/) |

</details>

<details><summary><b>Research and science</b> · 316</summary>

| Category | Entries | Try |
|---|---:|---|
| Scientific writing | 62 | [`appeal-journal-rejection`](library/research-science/scientific-writing/appeal-journal-rejection/) · [`audit-manuscript-storyline`](library/research-science/scientific-writing/audit-manuscript-storyline/) · [`build-manuscript-tables`](library/research-science/scientific-writing/build-manuscript-tables/) |
| Literature review | 61 | [`appraise-study-quality`](library/research-science/literature-review/appraise-study-quality/) · [`assess-study-applicability`](library/research-science/literature-review/assess-study-applicability/) · [`audit-literature-review-draft`](library/research-science/literature-review/audit-literature-review-draft/) |
| Research methods | 61 | [`agree-authorship-order`](library/research-science/research-methods/agree-authorship-order/) · [`assess-validity-threats`](library/research-science/research-methods/assess-validity-threats/) · [`build-causal-diagram`](library/research-science/research-methods/build-causal-diagram/) |
| Fact-checking | 51 | [`analyze-spin-in-article`](library/research-science/fact-checking/analyze-spin-in-article/) · [`assess-breaking-news-reports`](library/research-science/fact-checking/assess-breaking-news-reports/) · [`assess-dataset-reliability`](library/research-science/fact-checking/assess-dataset-reliability/) |
| Peer review | 46 | [`anticipate-reviewer-objections`](library/research-science/peer-review/anticipate-reviewer-objections/) · [`assess-referee-report-quality`](library/research-science/peer-review/assess-referee-report-quality/) · [`assess-reproducibility`](library/research-science/peer-review/assess-reproducibility/) |
| Lab work | 35 | [`analyze-standard-curve`](library/research-science/lab-work/analyze-standard-curve/) · [`assess-lab-procedure-risks`](library/research-science/lab-work/assess-lab-procedure-risks/) · [`audit-lab-notebooks`](library/research-science/lab-work/audit-lab-notebooks/) |

</details>

<details><summary><b>Design</b> · 271</summary>

| Category | Entries | Try |
|---|---:|---|
| UI design | 61 | [`adapt-design-for-mobile`](library/design/ui-design/adapt-design-for-mobile/) · [`adapt-ui-for-localization-and-rtl`](library/design/ui-design/adapt-ui-for-localization-and-rtl/) · [`adapt-ui-for-older-adults`](library/design/ui-design/adapt-ui-for-older-adults/) |
| UX research | 57 | [`analyze-session-recordings`](library/design/ux-research/analyze-session-recordings/) · [`assess-ux-maturity`](library/design/ux-research/assess-ux-maturity/) · [`audit-past-research`](library/design/ux-research/audit-past-research/) |
| Design systems | 46 | [`audit-component-duplication`](library/design/design-systems/audit-component-duplication/) · [`audit-design-code-parity`](library/design/design-systems/audit-design-code-parity/) · [`audit-design-consistency`](library/design/design-systems/audit-design-consistency/) |
| Graphic design | 37 | [`adapt-key-visual-to-formats`](library/design/graphic-design/adapt-key-visual-to-formats/) · [`create-color-palette`](library/design/graphic-design/create-color-palette/) · [`create-mood-board`](library/design/graphic-design/create-mood-board/) |
| Branding | 35 | [`build-brand-guidelines`](library/design/branding/build-brand-guidelines/) · [`build-brand-platform`](library/design/branding/build-brand-platform/) · [`build-diy-brand-kit`](library/design/branding/build-diy-brand-kit/) |
| Interior design | 35 | [`blend-two-households-decor`](library/design/interior-design/blend-two-households-decor/) · [`choose-paint-colours`](library/design/interior-design/choose-paint-colours/) · [`choose-rug-size`](library/design/interior-design/choose-rug-size/) |

</details>

<details><summary><b>Creative arts</b> · 464</summary>

| Category | Entries | Try |
|---|---:|---|
| Performing arts | 37 | [`break-down-scene-for-actor`](library/creative-arts/performing-arts/break-down-scene-for-actor/) · [`build-costume-plot`](library/creative-arts/performing-arts/build-costume-plot/) · [`build-props-list`](library/creative-arts/performing-arts/build-props-list/) |
| Comics and graphic novels | 36 | [`adapt-story-into-comic`](library/creative-arts/comics/adapt-story-into-comic/) · [`convert-print-comic-to-vertical-scroll`](library/creative-arts/comics/convert-print-comic-to-vertical-scroll/) · [`critique-comic-page`](library/creative-arts/comics/critique-comic-page/) |
| Fiction | 36 | [`build-suspense-in-scene`](library/creative-arts/fiction/build-suspense-in-scene/) · [`check-story-continuity`](library/creative-arts/fiction/check-story-continuity/) · [`co-write-story-interactively`](library/creative-arts/fiction/co-write-story-interactively/) |
| Image generation | 36 | [`build-image-style-guide`](library/creative-arts/image-generation/build-image-style-guide/) · [`coach-image-prompting`](library/creative-arts/image-generation/coach-image-prompting/) · [`create-storyboard`](library/creative-arts/image-generation/create-storyboard/) |
| Music | 36 | [`analyze-song-structure`](library/creative-arts/music/analyze-song-structure/) · [`build-music-sound-kit`](library/creative-arts/music/build-music-sound-kit/) · [`critique-song-lyrics`](library/creative-arts/music/critique-song-lyrics/) |
| Poetry | 36 | [`analyze-poem`](library/creative-arts/poetry/analyze-poem/) · [`audit-poem-meter`](library/creative-arts/poetry/audit-poem-meter/) · [`critique-poem`](library/creative-arts/poetry/critique-poem/) |
| Screenwriting | 36 | [`adapt-story-for-screen`](library/creative-arts/screenwriting/adapt-story-for-screen/) · [`cut-script-page-count`](library/creative-arts/screenwriting/cut-script-page-count/) · [`develop-tv-series-concept`](library/creative-arts/screenwriting/develop-tv-series-concept/) |
| Worldbuilding | 36 | [`build-fictional-world`](library/creative-arts/worldbuilding/build-fictional-world/) · [`build-magic-system`](library/creative-arts/worldbuilding/build-magic-system/) · [`build-series-bible`](library/creative-arts/worldbuilding/build-series-bible/) |
| Life writing | 35 | [`break-genealogy-brick-wall`](library/creative-arts/life-writing/break-genealogy-brick-wall/) · [`build-life-timeline`](library/creative-arts/life-writing/build-life-timeline/) · [`caption-family-photos`](library/creative-arts/life-writing/caption-family-photos/) |
| Nonfiction books | 35 | [`answer-copyedit-queries`](library/creative-arts/nonfiction/answer-copyedit-queries/) · [`build-book-index`](library/creative-arts/nonfiction/build-book-index/) · [`build-story-bank`](library/creative-arts/nonfiction/build-story-bank/) |
| Photography | 35 | [`answer-photo-usage-request`](library/creative-arts/photography/answer-photo-usage-request/) · [`choose-camera-gear`](library/creative-arts/photography/choose-camera-gear/) · [`choose-camera-settings`](library/creative-arts/photography/choose-camera-settings/) |
| Video generation | 35 | [`animate-listing-photos`](library/creative-arts/video-generation/animate-listing-photos/) · [`animate-old-family-photo`](library/creative-arts/video-generation/animate-old-family-photo/) · [`build-video-prompt-template`](library/creative-arts/video-generation/build-video-prompt-template/) |
| Visual art | 35 | [`assess-reference-photo`](library/creative-arts/visual-art/assess-reference-photo/) · [`choose-art-supplies`](library/creative-arts/visual-art/choose-art-supplies/) · [`critique-artwork`](library/creative-arts/visual-art/critique-artwork/) |

</details>

<details><summary><b>Writing and communication</b> · 559</summary>

| Category | Entries | Try |
|---|---:|---|
| Business writing | 97 | [`ask-for-help-in-team-chat`](library/writing-communication/business-writing/ask-for-help-in-team-chat/) · [`build-company-glossary`](library/writing-communication/business-writing/build-company-glossary/) · [`plan-change-communications`](library/writing-communication/business-writing/plan-change-communications/) |
| Email | 97 | [`acknowledge-request-and-set-timeline`](library/writing-communication/email/acknowledge-request-and-set-timeline/) · [`announce-employee-departure`](library/writing-communication/email/announce-employee-departure/) · [`announce-event-cancellation`](library/writing-communication/email/announce-event-cancellation/) |
| Interpersonal communication | 96 | [`adapt-message-for-culture`](library/writing-communication/interpersonal-communication/adapt-message-for-culture/) · [`address-peer-not-pulling-weight`](library/writing-communication/interpersonal-communication/address-peer-not-pulling-weight/) · [`announce-unpopular-decision-to-family`](library/writing-communication/interpersonal-communication/announce-unpopular-decision-to-family/) |
| Editing | 88 | [`answer-grammar-usage-question`](library/writing-communication/editing/answer-grammar-usage-question/) · [`apply-brand-voice-to-copy`](library/writing-communication/editing/apply-brand-voice-to-copy/) · [`apply-title-case-to-headings`](library/writing-communication/editing/apply-title-case-to-headings/) |
| Presentations | 72 | [`adapt-deck-for-new-audience`](library/writing-communication/presentations/adapt-deck-for-new-audience/) · [`adapt-presentation-for-international-audience`](library/writing-communication/presentations/adapt-presentation-for-international-audience/) · [`add-sources-to-slides`](library/writing-communication/presentations/add-sources-to-slides/) |
| Public speaking | 55 | [`adapt-talk-for-new-audience`](library/writing-communication/public-speaking/adapt-talk-for-new-audience/) · [`build-speaking-practice-plan`](library/writing-communication/public-speaking/build-speaking-practice-plan/) · [`check-venue-before-talk`](library/writing-communication/public-speaking/check-venue-before-talk/) |
| Grant writing | 54 | [`adapt-proposal-for-new-funder`](library/writing-communication/grant-writing/adapt-proposal-for-new-funder/) · [`announce-grant-award`](library/writing-communication/grant-writing/announce-grant-award/) · [`answer-funder-clarification-questions`](library/writing-communication/grant-writing/answer-funder-clarification-questions/) |

</details>

<details><summary><b>Career and HR</b> · 466</summary>

| Category | Entries | Try |
|---|---:|---|
| Interview preparation | 67 | [`answer-ai-usage-interview-questions`](library/career-hr/interview-prep/answer-ai-usage-interview-questions/) · [`answer-greatest-strength`](library/career-hr/interview-prep/answer-greatest-strength/) · [`answer-greatest-weakness`](library/career-hr/interview-prep/answer-greatest-weakness/) |
| People management | 64 | [`address-high-performer-behaviour`](library/career-hr/people-management/address-high-performer-behaviour/) · [`address-negative-attitude`](library/career-hr/people-management/address-negative-attitude/) · [`address-offensive-remark-in-team`](library/career-hr/people-management/address-offensive-remark-in-team/) |
| Résumés | 64 | [`age-proof-resume`](library/career-hr/resumes/age-proof-resume/) · [`anonymize-resume-for-blind-hiring`](library/career-hr/resumes/anonymize-resume-for-blind-hiring/) · [`build-latex-resume`](library/career-hr/resumes/build-latex-resume/) |
| Career growth | 60 | [`ask-for-raise`](library/career-hr/career-growth/ask-for-raise/) · [`ask-for-stretch-assignment`](library/career-hr/career-growth/ask-for-stretch-assignment/) · [`ask-for-title-change`](library/career-hr/career-growth/ask-for-title-change/) |
| Job search | 60 | [`accept-job-offer-in-writing`](library/career-hr/job-search/accept-job-offer-in-writing/) · [`address-selection-criteria`](library/career-hr/job-search/address-selection-criteria/) · [`analyze-job-posting`](library/career-hr/job-search/analyze-job-posting/) |
| Hiring | 59 | [`audit-candidate-experience`](library/career-hr/hiring/audit-candidate-experience/) · [`audit-job-description`](library/career-hr/hiring/audit-job-description/) · [`break-tie-between-finalists`](library/career-hr/hiring/break-tie-between-finalists/) |
| HR operations | 50 | [`analyze-pay-equity`](library/career-hr/hr-operations/analyze-pay-equity/) · [`answer-employee-hr-question`](library/career-hr/hr-operations/answer-employee-hr-question/) · [`assess-flexible-working-request`](library/career-hr/hr-operations/assess-flexible-working-request/) |
| Freelancing | 42 | [`announce-freelance-availability`](library/career-hr/freelancing/announce-freelance-availability/) · [`brief-freelance-subcontractor`](library/career-hr/freelancing/brief-freelance-subcontractor/) · [`build-freelance-pipeline-routine`](library/career-hr/freelancing/build-freelance-pipeline-routine/) |

</details>

<details><summary><b>Finance</b> · 369</summary>

| Category | Entries | Try |
|---|---:|---|
| Taxes | 64 | [`appeal-tax-penalty`](library/finance/taxes/appeal-tax-penalty/) · [`calculate-cost-basis`](library/finance/taxes/calculate-cost-basis/) · [`calculate-home-office-deduction`](library/finance/taxes/calculate-home-office-deduction/) |
| Financial planning | 60 | [`build-financial-emergency-file`](library/finance/financial-planning/build-financial-emergency-file/) · [`build-lifetime-cash-flow-plan`](library/finance/financial-planning/build-lifetime-cash-flow-plan/) · [`build-net-worth-statement`](library/finance/financial-planning/build-net-worth-statement/) |
| Accounting | 56 | [`analyze-customer-profitability`](library/finance/accounting/analyze-customer-profitability/) · [`analyze-working-capital`](library/finance/accounting/analyze-working-capital/) · [`build-cash-flow-statement`](library/finance/accounting/build-cash-flow-statement/) |
| Budgeting | 52 | [`audit-subscriptions`](library/finance/budgeting/audit-subscriptions/) · [`budget-a-pay-rise`](library/finance/budgeting/budget-a-pay-rise/) · [`budget-for-holidays-and-gifts`](library/finance/budgeting/budget-for-holidays-and-gifts/) |
| Debt and credit | 51 | [`ask-card-issuer-to-cut-rate-or-fees`](library/finance/debt/ask-card-issuer-to-cut-rate-or-fees/) · [`break-payday-loan-cycle`](library/finance/debt/break-payday-loan-cycle/) · [`build-credit-history-from-zero`](library/finance/debt/build-credit-history-from-zero/) |
| Investing (education) | 50 | [`assess-risk-tolerance`](library/finance/investing/assess-risk-tolerance/) · [`build-bond-ladder`](library/finance/investing/build-bond-ladder/) · [`calculate-fee-drag`](library/finance/investing/calculate-fee-drag/) |
| Insurance | 36 | [`appeal-insurance-denial`](library/finance/insurance/appeal-insurance-denial/) · [`calculate-life-cover-need`](library/finance/insurance/calculate-life-cover-need/) · [`challenge-fault-decision`](library/finance/insurance/challenge-fault-decision/) |

</details>

<details><summary><b>Legal and admin</b> · 415</summary>

| Category | Entries | Try |
|---|---:|---|
| Paperwork | 59 | [`apply-for-adult-guardianship`](library/legal-admin/paperwork/apply-for-adult-guardianship/) · [`apply-for-building-permit`](library/legal-admin/paperwork/apply-for-building-permit/) · [`apply-for-child-passport`](library/legal-admin/paperwork/apply-for-child-passport/) |
| Contracts | 56 | [`assess-breach-of-contract`](library/legal-admin/contracts/assess-breach-of-contract/) · [`build-contract-negotiation-playbook`](library/legal-admin/contracts/build-contract-negotiation-playbook/) · [`build-contract-obligations-register`](library/legal-admin/contracts/build-contract-obligations-register/) |
| Legal correspondence | 54 | [`appeal-benefits-decision`](library/legal-admin/legal-correspondence/appeal-benefits-decision/) · [`appeal-dismissal`](library/legal-admin/legal-correspondence/appeal-dismissal/) · [`appeal-parking-ticket`](library/legal-admin/legal-correspondence/appeal-parking-ticket/) |
| Compliance | 51 | [`answer-security-questionnaire`](library/legal-admin/compliance/answer-security-questionnaire/) · [`assess-ai-act-obligations`](library/legal-admin/compliance/assess-ai-act-obligations/) · [`assess-childrens-privacy-obligations`](library/legal-admin/compliance/assess-childrens-privacy-obligations/) |
| Policies and terms | 48 | [`write-acceptable-use-policy`](library/legal-admin/policies/write-acceptable-use-policy/) · [`write-accessibility-statement`](library/legal-admin/policies/write-accessibility-statement/) · [`write-ai-transparency-notice`](library/legal-admin/policies/write-ai-transparency-notice/) |
| Renting and tenancy | 39 | [`ask-landlord-about-pet`](library/legal-admin/tenancy/ask-landlord-about-pet/) · [`challenge-rental-fees`](library/legal-admin/tenancy/challenge-rental-fees/) · [`check-jeonse-contract`](library/legal-admin/tenancy/check-jeonse-contract/) |
| Legal practice | 37 | [`analyze-statutory-provision`](library/legal-admin/legal-practice/analyze-statutory-provision/) · [`brief-court-case`](library/legal-admin/legal-practice/brief-court-case/) · [`build-damages-schedule`](library/legal-admin/legal-practice/build-damages-schedule/) |
| Intellectual property | 36 | [`agree-ownership-with-co-creators`](library/legal-admin/intellectual-property/agree-ownership-with-co-creators/) · [`apply-for-trademark`](library/legal-admin/intellectual-property/apply-for-trademark/) · [`assess-rights-in-ai-assisted-work`](library/legal-admin/intellectual-property/assess-rights-in-ai-assisted-work/) |
| Immigration | 35 | [`ask-employer-for-visa-sponsorship`](library/legal-admin/immigration/ask-employer-for-visa-sponsorship/) · [`calculate-absences-from-country`](library/legal-admin/immigration/calculate-absences-from-country/) · [`check-dual-citizenship-impact`](library/legal-admin/immigration/check-dual-citizenship-impact/) |

</details>

<details><summary><b>Health and wellbeing</b> · 372</summary>

| Category | Entries | Try |
|---|---:|---|
| Fitness | 63 | [`adapt-exercise-for-condition`](library/health-wellbeing/fitness/adapt-exercise-for-condition/) · [`adjust-week-after-missed-workouts`](library/health-wellbeing/fitness/adjust-week-after-missed-workouts/) · [`assess-fitness-baseline`](library/health-wellbeing/fitness/assess-fitness-baseline/) |
| Mental health | 63 | [`bounce-back-from-rejection`](library/health-wellbeing/mental-health/bounce-back-from-rejection/) · [`break-rumination-loop`](library/health-wellbeing/mental-health/break-rumination-loop/) · [`build-connection-plan`](library/health-wellbeing/mental-health/build-connection-plan/) |
| Medical visit preparation | 60 | [`access-healthcare-abroad`](library/health-wellbeing/medical-prep/access-healthcare-abroad/) · [`build-medication-list`](library/health-wellbeing/medical-prep/build-medication-list/) · [`build-symptom-log`](library/health-wellbeing/medical-prep/build-symptom-log/) |
| Nutrition | 55 | [`analyze-diet-log`](library/health-wellbeing/nutrition/analyze-diet-log/) · [`compare-diet-approaches`](library/health-wellbeing/nutrition/compare-diet-approaches/) · [`cut-back-ultra-processed-food`](library/health-wellbeing/nutrition/cut-back-ultra-processed-food/) |
| Clinical practice | 48 | [`draft-discharge-summary`](library/health-wellbeing/clinical-practice/draft-discharge-summary/) · [`plan-advance-care-planning-conversation`](library/health-wellbeing/clinical-practice/plan-advance-care-planning-conversation/) · [`plan-breaking-bad-news`](library/health-wellbeing/clinical-practice/plan-breaking-bad-news/) |
| Sleep | 46 | [`audit-bedroom-for-sleep`](library/health-wellbeing/sleep/audit-bedroom-for-sleep/) · [`beat-bedtime-procrastination`](library/health-wellbeing/sleep/beat-bedtime-procrastination/) · [`beat-jet-lag`](library/health-wellbeing/sleep/beat-jet-lag/) |
| Living with chronic conditions | 37 | [`adapt-hobby-for-condition`](library/health-wellbeing/chronic-conditions/adapt-hobby-for-condition/) · [`adapt-household-tasks-for-fatigue`](library/health-wellbeing/chronic-conditions/adapt-household-tasks-for-fatigue/) · [`adjust-to-life-with-stoma`](library/health-wellbeing/chronic-conditions/adjust-to-life-with-stoma/) |

</details>

<details><summary><b>Cooking and home</b> · 333</summary>

| Category | Entries | Try |
|---|---:|---|
| Home improvement | 45 | [`assemble-flat-pack-furniture`](library/home-cooking/home-improvement/assemble-flat-pack-furniture/) · [`assess-wall-cracks`](library/home-cooking/home-improvement/assess-wall-cracks/) · [`build-home-inventory`](library/home-cooking/home-improvement/build-home-inventory/) |
| Cooking | 37 | [`adapt-recipe`](library/home-cooking/cooking/adapt-recipe/) · [`adjust-recipe-for-altitude`](library/home-cooking/cooking/adjust-recipe-for-altitude/) · [`blend-spice-mix`](library/home-cooking/cooking/blend-spice-mix/) |
| Housekeeping and cleaning | 37 | [`adapt-cleaning-for-low-energy`](library/home-cooking/housekeeping/adapt-cleaning-for-low-energy/) · [`build-cleaning-kit`](library/home-cooking/housekeeping/build-cleaning-kit/) · [`clean-after-building-work`](library/home-cooking/housekeeping/clean-after-building-work/) |
| Baking | 36 | [`adapt-bake-to-different-tin`](library/home-cooking/baking/adapt-bake-to-different-tin/) · [`calibrate-home-oven`](library/home-cooking/baking/calibrate-home-oven/) · [`choose-baking-equipment`](library/home-cooking/baking/choose-baking-equipment/) |
| Drinks | 36 | [`blend-herbal-infusion`](library/home-cooking/drinks/blend-herbal-infusion/) · [`brew-masala-chai`](library/home-cooking/drinks/brew-masala-chai/) · [`brew-moka-pot-coffee`](library/home-cooking/drinks/brew-moka-pot-coffee/) |
| Gardening | 36 | [`build-garden-calendar`](library/home-cooking/gardening/build-garden-calendar/) · [`build-raised-bed-plan`](library/home-cooking/gardening/build-raised-bed-plan/) · [`clear-perennial-weeds`](library/home-cooking/gardening/clear-perennial-weeds/) |
| Vehicles | 36 | [`adjust-bike-gears`](library/home-cooking/vehicles/adjust-bike-gears/) · [`change-flat-tyre`](library/home-cooking/vehicles/change-flat-tyre/) · [`check-car-before-road-trip`](library/home-cooking/vehicles/check-car-before-road-trip/) |
| Meal planning | 35 | [`build-dinner-rotation`](library/home-cooking/meal-planning/build-dinner-rotation/) · [`build-grocery-list-from-recipes`](library/home-cooking/meal-planning/build-grocery-list-from-recipes/) · [`organise-potluck`](library/home-cooking/meal-planning/organise-potluck/) |
| Pet care | 35 | [`build-pet-emergency-plan`](library/home-cooking/pet-care/build-pet-emergency-plan/) · [`care-for-backyard-chickens`](library/home-cooking/pet-care/care-for-backyard-chickens/) · [`care-for-rabbits`](library/home-cooking/pet-care/care-for-rabbits/) |

</details>

<details><summary><b>Travel</b> · 180</summary>

| Category | Entries | Try |
|---|---:|---|
| Trip planning | 37 | [`choose-accommodation`](library/travel/trip-planning/choose-accommodation/) · [`choose-destination`](library/travel/trip-planning/choose-destination/) · [`choose-ethical-volunteer-trip`](library/travel/trip-planning/choose-ethical-volunteer-trip/) |
| Outdoors | 36 | [`assess-river-crossing`](library/travel/outdoors/assess-river-crossing/) · [`build-outdoor-first-aid-kit`](library/travel/outdoors/build-outdoor-first-aid-kit/) · [`choose-mountain-guide`](library/travel/outdoors/choose-mountain-guide/) |
| Relocation and settling in | 36 | [`brief-destination-relocation-agent`](library/travel/relocation/brief-destination-relocation-agent/) · [`brief-new-school-on-arriving-child`](library/travel/relocation/brief-new-school-on-arriving-child/) · [`build-social-circle-in-new-city`](library/travel/relocation/build-social-circle-in-new-city/) |
| Travel logistics | 36 | [`build-packing-list`](library/travel/travel-logistics/build-packing-list/) · [`build-trip-booking-timeline`](library/travel/travel-logistics/build-trip-booking-timeline/) · [`cancel-trip-bookings`](library/travel/travel-logistics/cancel-trip-bookings/) |
| Local culture | 35 | [`apologise-for-cultural-faux-pas`](library/travel/local-culture/apologise-for-cultural-faux-pas/) · [`check-gestures-and-body-language`](library/travel/local-culture/check-gestures-and-body-language/) · [`check-local-festivals-and-holidays`](library/travel/local-culture/check-local-festivals-and-holidays/) |

</details>

<details><summary><b>Parenting and family</b> · 218</summary>

| Category | Entries | Try |
|---|---:|---|
| Parenting | 38 | [`build-reading-routine-with-child`](library/parenting-family/parenting/build-reading-routine-with-child/) · [`choose-childcare`](library/parenting-family/parenting/choose-childcare/) · [`choose-extracurricular-activities`](library/parenting-family/parenting/choose-extracurricular-activities/) |
| Family logistics | 37 | [`audit-family-activity-load`](library/parenting-family/family-logistics/audit-family-activity-load/) · [`coordinate-family-calendar`](library/parenting-family/family-logistics/coordinate-family-calendar/) · [`create-chore-chart`](library/parenting-family/family-logistics/create-chore-chart/) |
| Caregiving | 36 | [`adapt-family-celebration-for-dementia`](library/parenting-family/caregiving/adapt-family-celebration-for-dementia/) · [`agree-care-cost-split`](library/parenting-family/caregiving/agree-care-cost-split/) · [`balance-partner-and-carer-roles`](library/parenting-family/caregiving/balance-partner-and-carer-roles/) |
| Kids' activities | 36 | [`build-den-with-kids`](library/parenting-family/kids-activities/build-den-with-kids/) · [`create-kids-craft`](library/parenting-family/kids-activities/create-kids-craft/) · [`create-puppet-show`](library/parenting-family/kids-activities/create-puppet-show/) |
| Relationships | 36 | [`assess-draining-friendship`](library/parenting-family/relationships/assess-draining-friendship/) · [`assess-early-dating-warning-signs`](library/parenting-family/relationships/assess-early-dating-warning-signs/) · [`build-couple-bucket-list`](library/parenting-family/relationships/build-couple-bucket-list/) |
| Pregnancy and new babies | 35 | [`check-safe-sleep-setup`](library/parenting-family/pregnancy/check-safe-sleep-setup/) · [`choose-antenatal-classes`](library/parenting-family/pregnancy/choose-antenatal-classes/) · [`choose-baby-doctor`](library/parenting-family/pregnancy/choose-baby-doctor/) |

</details>

<details><summary><b>Productivity and personal life</b> · 596</summary>

| Category | Entries | Try |
|---|---:|---|
| Summarisation | 65 | [`brief-manager-on-situation`](library/productivity/summarization/brief-manager-on-situation/) · [`brief-me-on-topic`](library/productivity/summarization/brief-me-on-topic/) · [`build-cast-of-characters`](library/productivity/summarization/build-cast-of-characters/) |
| Decision-making | 61 | [`apply-mental-models-to-problem`](library/productivity/decision-making/apply-mental-models-to-problem/) · [`build-decision-tree`](library/productivity/decision-making/build-decision-tree/) · [`check-decision-for-biases`](library/productivity/decision-making/check-decision-for-biases/) |
| Task management | 56 | [`audit-recurring-tasks`](library/productivity/task-management/audit-recurring-tasks/) · [`audit-time-use`](library/productivity/task-management/audit-time-use/) · [`batch-email-and-messages`](library/productivity/task-management/batch-email-and-messages/) |
| Note-taking | 55 | [`apply-progressive-summarization`](library/productivity/note-taking/apply-progressive-summarization/) · [`archive-finished-project-notes`](library/productivity/note-taking/archive-finished-project-notes/) · [`audit-notes-vault`](library/productivity/note-taking/audit-notes-vault/) |
| Meetings | 54 | [`adapt-meetings-for-access-needs`](library/productivity/meetings/adapt-meetings-for-access-needs/) · [`analyze-meeting-participation`](library/productivity/meetings/analyze-meeting-participation/) · [`build-action-item-tracker`](library/productivity/meetings/build-action-item-tracker/) |
| Tech help | 47 | [`automate-personal-routine`](library/productivity/tech-help/automate-personal-routine/) · [`check-used-device`](library/productivity/tech-help/check-used-device/) · [`choose-cloud-storage`](library/productivity/tech-help/choose-cloud-storage/) |
| Brainstorming | 42 | [`brainstorm-app-ideas`](library/productivity/brainstorming/brainstorm-app-ideas/) · [`brainstorm-community-project-ideas`](library/productivity/brainstorming/brainstorm-community-project-ideas/) · [`brainstorm-costume-ideas`](library/productivity/brainstorming/brainstorm-costume-ideas/) |
| Event planning | 38 | [`build-conference-programme`](library/productivity/event-planning/build-conference-programme/) · [`build-event-planning-timeline`](library/productivity/event-planning/build-event-planning-timeline/) · [`build-event-volunteer-rota`](library/productivity/event-planning/build-event-volunteer-rota/) |
| Habits and goals | 36 | [`add-more-joy-to-week`](library/productivity/habits/add-more-joy-to-week/) · [`beat-procrastination`](library/productivity/habits/beat-procrastination/) · [`break-bad-habit`](library/productivity/habits/break-bad-habit/) |
| Shopping decisions | 36 | [`buy-from-overseas-seller`](library/productivity/shopping/buy-from-overseas-seller/) · [`buy-open-box-or-refurbished`](library/productivity/shopping/buy-open-box-or-refurbished/) · [`buy-secondhand-safely`](library/productivity/shopping/buy-secondhand-safely/) |
| Religion and spirituality | 36 | [`answer-child-faith-questions`](library/productivity/spirituality/answer-child-faith-questions/) · [`check-spiritual-group-warning-signs`](library/productivity/spirituality/check-spiritual-group-warning-signs/) · [`choose-scripture-translation`](library/productivity/spirituality/choose-scripture-translation/) |
| Digital safety | 35 | [`check-data-breach-exposure`](library/productivity/digital-safety/check-data-breach-exposure/) · [`check-job-offer-scam`](library/productivity/digital-safety/check-job-offer-scam/) · [`check-marketplace-deal`](library/productivity/digital-safety/check-marketplace-deal/) |
| Personal style and grooming | 35 | [`adapt-wardrobe-to-new-climate`](library/productivity/personal-style/adapt-wardrobe-to-new-climate/) · [`assess-garment-quality`](library/productivity/personal-style/assess-garment-quality/) · [`build-capsule-wardrobe`](library/productivity/personal-style/build-capsule-wardrobe/) |

</details>

<details><summary><b>Gaming and fun</b> · 392</summary>

| Category | Entries | Try |
|---|---:|---|
| Simulations and play-along games | 37 | [`play-age-of-sail-voyage`](library/gaming-fun/simulations/play-age-of-sail-voyage/) · [`play-air-traffic-control`](library/gaming-fun/simulations/play-air-traffic-control/) · [`play-archaeology-dig`](library/gaming-fun/simulations/play-archaeology-dig/) |
| Crafts and making | 36 | [`calibrate-3d-printer`](library/gaming-fun/crafts/calibrate-3d-printer/) · [`chart-cross-stitch-pattern`](library/gaming-fun/crafts/chart-cross-stitch-pattern/) · [`choose-sewing-machine`](library/gaming-fun/crafts/choose-sewing-machine/) |
| Game design | 36 | [`analyze-playtest-notes`](library/gaming-fun/game-design/analyze-playtest-notes/) · [`balance-asymmetric-factions`](library/gaming-fun/game-design/balance-asymmetric-factions/) · [`calculate-game-probabilities`](library/gaming-fun/game-design/calculate-game-probabilities/) |
| Humour | 36 | [`adapt-joke-for-another-language`](library/gaming-fun/humor/adapt-joke-for-another-language/) · [`explain-joke-or-meme`](library/gaming-fun/humor/explain-joke-or-meme/) · [`fix-joke-that-fell-flat`](library/gaming-fun/humor/fix-joke-that-fell-flat/) |
| Films, books, music and fandom | 36 | [`build-reading-challenge`](library/gaming-fun/media-and-fandom/build-reading-challenge/) · [`catch-up-on-series-spoiler-free`](library/gaming-fun/media-and-fandom/catch-up-on-series-spoiler-free/) · [`check-film-for-children`](library/gaming-fun/media-and-fandom/check-film-for-children/) |
| Tabletop RPGs | 36 | [`adjudicate-rules-dispute`](library/gaming-fun/tabletop-rpg/adjudicate-rules-dispute/) · [`balance-combat-encounter`](library/gaming-fun/tabletop-rpg/balance-combat-encounter/) · [`build-rpg-character`](library/gaming-fun/tabletop-rpg/build-rpg-character/) |
| Hobbies and pastimes | 35 | [`assess-inherited-collection`](library/gaming-fun/pastimes/assess-inherited-collection/) · [`build-scale-model-kit`](library/gaming-fun/pastimes/build-scale-model-kit/) · [`catalog-collection`](library/gaming-fun/pastimes/catalog-collection/) |
| Puzzles | 35 | [`analyze-chess-game`](library/gaming-fun/puzzles/analyze-chess-game/) · [`build-chess-opening-repertoire`](library/gaming-fun/puzzles/build-chess-opening-repertoire/) · [`build-mini-crossword`](library/gaming-fun/puzzles/build-mini-crossword/) |
| Amateur sport | 35 | [`adapt-sport-for-mixed-ability`](library/gaming-fun/sports/adapt-sport-for-mixed-ability/) · [`break-down-sports-technique`](library/gaming-fun/sports/break-down-sports-technique/) · [`choose-team-formation`](library/gaming-fun/sports/choose-team-formation/) |
| Trivia and quizzes | 35 | [`adapt-quiz-for-audience`](library/gaming-fun/trivia/adapt-quiz-for-audience/) · [`create-custom-bingo`](library/gaming-fun/trivia/create-custom-bingo/) · [`create-party-game-cards`](library/gaming-fun/trivia/create-party-game-cards/) |
| Video games | 35 | [`audit-game-spending`](library/gaming-fun/video-games/audit-game-spending/) · [`build-aim-training-routine`](library/gaming-fun/video-games/build-aim-training-routine/) · [`calculate-production-ratios`](library/gaming-fun/video-games/calculate-production-ratios/) |

</details>

<details><summary><b>Prompting and assistants</b> · 150</summary>

| Category | Entries | Try |
|---|---:|---|
| Prompt engineering | 64 | [`adapt-prompt-for-reasoning-model`](library/prompting/prompt-engineering/adapt-prompt-for-reasoning-model/) · [`adapt-prompt-for-small-model`](library/prompting/prompt-engineering/adapt-prompt-for-small-model/) · [`anonymize-text-before-ai`](library/prompting/prompt-engineering/anonymize-text-before-ai/) |
| Assistant setup | 50 | [`audit-assistant-memory`](library/prompting/assistant-setup/audit-assistant-memory/) · [`build-project-instructions`](library/prompting/assistant-setup/build-project-instructions/) · [`choose-ai-tool`](library/prompting/assistant-setup/choose-ai-tool/) |
| Output styles | 36 | [`academic`](library/prompting/output-styles/academic/) · [`actionable`](library/prompting/output-styles/actionable/) · [`analogy-led`](library/prompting/output-styles/analogy-led/) |

</details>
<!-- catalog:end -->

## Contribute

**No git needed:** [suggest a prompt](https://github.com/hermes-hq/hodios/issues/new?template=new-prompt.yml). Describe the task and what a great result looks like in a short form, and say whether you want to write it yourself.

**Write one yourself** in about five minutes: copy an example folder, edit the frontmatter, write the body, run `npm run validate`, and open a pull request. [CONTRIBUTING.md](CONTRIBUTING.md) has the walkthrough, the quality bar and what we do not accept. Found a prompt that gives bad advice? [Report it](https://github.com/hermes-hq/hodios/issues/new?template=prompt-quality.yml). Questions and ideas go to [Discussions](https://github.com/hermes-hq/hodios/discussions).

**Share an entry:** every entry has its own page at `hermes-ide.com/prompts/<id>`, for example [hermes-ide.com/prompts/plan-weekly-meals](https://hermes-ide.com/prompts/plan-weekly-meals).

## Repository layout

```
library/<domain>/<category>/<id>/<kind>.md   entries (prompt.md, persona.md, workflow.md, rule.md or style.md)
partials/                            shared snippets included with {{> path}}
vocab/                               controlled vocabularies: domains, categories, roles, stacks... (see TAXONOMY.md)
schema/                              JSON Schemas for entries, evals and vocab
packages/schema  core  cli           @hermes-hq/hodios-schema, @hermes-hq/hodios-core, hodios (CLI)
ids.lock                             every released id, append-only
curated.txt                          the curated tier: the entries hodios-dist ships
```

The compiled install tree (the curated tier) and the searchable catalog (every entry, `catalog/v1`) live in [hermes-hq/hodios-dist](https://github.com/hermes-hq/hodios-dist), built by the release bot. How entries are picked for the curated tier: [TAXONOMY.md §6.1](TAXONOMY.md#61-tiers-and-the-curated-list).

## The name

*Hodios* (HO-dee-os) is an epithet of Hermes: the guide of travellers. This library is the guide for your agents.

## Support

Hodios is free and always will be. If it saves you time and you'd like to say thanks, you can [buy the maintainer a coffee](https://buymeacoffee.com/anhaia). Stars, good entries and honest bug reports help just as much.

## License

- **Content** (`library/`, `partials/`, `vocab/` and every generated export): [CC0-1.0](LICENSES/CC0-1.0.txt). No rights reserved.
- **Code** (`packages/`, `tools/`, `schema/`): [Apache-2.0](LICENSE).

[REUSE.toml](REUSE.toml) maps every path. Hodios is separate from Hermes IDE's own license. "Hodios" and "Hermes IDE" are trademarks; see [TRADEMARK.md](TRADEMARK.md).
