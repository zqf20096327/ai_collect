🇬🇧 English · 🇹🇷 [Türkçe](README.tr.md)

# Orchnes 360

[![validate](https://github.com/orchnesai/orchnes-360/actions/workflows/validate.yml/badge.svg)](https://github.com/orchnesai/orchnes-360/actions/workflows/validate.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Agent Skills](https://img.shields.io/badge/Agent%20Skills-spec%20compliant-6f42c1)](https://agentskills.io) ![skills](https://img.shields.io/badge/skills-26-success) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/orchnesai/orchnes-360/badge)](https://scorecard.dev/viewer/?uri=github.com/orchnesai/orchnes-360)

**End-to-end skills for AI agents — from idea to a running business, in any AI tool.**
Say what you want to achieve; your agents get the whole map, do the work, and ask you only for decisions and approvals.

Portable, token-efficient skills for AI agents. MIT licensed.

Each skill is a folder with a `SKILL.md` following the open **Agent Skills** format
(YAML frontmatter + Markdown instructions). Only a skill's name and description sit in the
model's context until the skill is needed, so installing many skills costs almost nothing.

## Skills

| Skill | What it does |
|---|---|
| [`agent-behavior`](skills/agent-behavior/SKILL.md) | Baseline for every session: short, evidence-backed, human answers; no false "done", no loops, no restarting; ask only for secrets, approvals and real decisions. |
| [`agent-orchestra`](skills/agent-orchestra/SKILL.md) | Run a team of agents: a top model decomposes, routes each task to the cheapest capable (free/local first) model, reviews against contracts, rejects bloat, teaches with playbooks, logs decisions and cost. |
| [`ai-integration`](skills/ai-integration/SKILL.md) | AI inside a product: model choice (LLM/SLM, hosted/local), RAG + tools so it knows the platform, scope guard and injection defence, one agent per job with a supervisor, lawful customer analytics, evals and monitoring. |
| [`analysis`](skills/analysis/SKILL.md) | Reproducible data analysis with honest uncertainty: business KPIs, cohorts and forecasts; stocks, crypto and health data with sourced context, risk warnings and no advice/diagnosis. |
| [`autonomous-loop`](skills/autonomous-loop/SKILL.md) | Goal-driven loop: a cheap worker model iterates, a top-ranked supervisor model only diagnoses, shows correct patterns, designs tests and signs off. Built-in stall detection and hard stops. |
| [`brand-ip`](skills/brand-ip/SKILL.md) | Protect the brand: name clearance, trademark strategy (classes, national/EU/US/Madrid), designs, patents/utility models, copyright ownership and assignments, domains/handles, marketplace brand registries, open-source licences, trade secrets. |
| [`codebase-analysis`](skills/codebase-analysis/SKILL.md) | Analyze any repo end to end: architecture map, quality & tech debt, security review, onboarding guide — cheap recon first, every finding with file:line evidence. |
| [`commerce-integrations`](skills/commerce-integrations/SKILL.md) | Payments by country/continent (merchant onboarding, local methods, instalments), PCI/SCA, webhooks, refunds, reconciliation; marketplace sync; shipping, customs, e-invoicing and VAT/sales tax — facts verified with dated sources. |
| [`company-setup`](skills/company-setup/SKILL.md) | Company setup by growth plan: entity choice, country checklists, tax/social security/bank/licences, privacy and e-commerce compliance by region (KVKK, GDPR, CCPA…), with every filing and signature left to the founder and professionals. |
| [`content-social`](skills/content-social/SKILL.md) | Social media like a senior human manager: strategy, brand voice, calendar, platform-native posts, official-API scheduling, community replies, crisis escalation, analytics — user only logs in and approves. |
| [`daily-assistant`](skills/daily-assistant/SKILL.md) | Everyday admin like a capable assistant: inbox triage and drafts, scheduling, tasks and reminders, meeting follow-ups, travel, shopping comparisons, bills and subscriptions — never sends, books or pays without approval. |
| [`diagrams-mapping`](skills/diagrams-mapping/SKILL.md) | Accurate diagrams as code from real evidence: context/architecture, sequence, flow, ERD, state, deployment, process, journey, timeline, mind maps — Mermaid templates validated by rendering. |
| [`growth-operations`](skills/growth-operations/SKILL.md) | Growth after launch: funnel and biggest leak, CRM lifecycle flows with consent, SEO, paid tests with CAC targets, localization (i18n, hreflang, currency), support operations and SLAs, A/B tests. |
| [`guided-discovery`](skills/guided-discovery/SKILL.md) | Say a goal, get the whole map instantly: every component in plain language, who does it, ≤ 3 decisions with defaults — then the agent drives. Packs: e-commerce, healthcare, SaaS + universal map for any sector. |
| [`infrastructure-planning`](skills/infrastructure-planning/SKILL.md) | Right-sized infrastructure: capacity math, VPS/VDS/cloud/SaaS choice, database admin/security/backup/PITR/tiers/failover, RPO/RTO, IaC & CI/CD, cost, modernization — staged plans with measurable triggers. |
| [`market-research`](skills/market-research/SKILL.md) | Decide with evidence: demand signals, bottom-up market size, behaviour-based customer research, competitor benchmarks and review mining, pricing and unit economics, risk register, cheap experiments, go/adjust/stop memo. |
| [`memory`](skills/memory/SKILL.md) | Persistent memory across sessions, agents and models: state, decisions, facts, user preferences — resume from the last open point, never restart. Works with CLAUDE.md, AGENTS.md and any tool. |
| [`planner`](skills/planner/SKILL.md) | End-to-end planning: frame → discover → decide → break down → de-risk → ship. |
| [`product-build`](skills/product-build/SKILL.md) | Build stores, platforms and apps: build-vs-buy first, then every role with artifacts (BA, DB analyst, architect, backend, frontend, admin, QA, DevOps, security, docs), Rust-first stack, e-commerce blueprint, full test layers. |
| [`research`](skills/research/SKILL.md) | Evidence-based research: asks for access when missing, searches globally in local languages, primary sources first, cross-checks key claims, reports conflicts, answers with cited, dated evidence and confidence. |
| [`root-cause-analysis`](skills/root-cause-analysis/SKILL.md) | Evidence-driven RCA: reproduce → evidence → ranked hypotheses → cause behind the cause → proven fix → report. Guides for bugs, performance and production incidents. |
| [`security-operations`](skills/security-operations/SKILL.md) | Defensive security for authorized systems: appsec/injection, CVE management, cloud, email (SPF/DKIM/DMARC), identity & passwords, social accounts, host/kernel hardening, incident response — read-only first, evidence-backed findings, approved fixes. |
| [`software-engineering`](skills/software-engineering/SKILL.md) | Universal engineering rules + architecture layers, with per-type guides: web, mobile, desktop, embedded/IoT, CLI/library, data/ML, games, distributed. |
| [`token-economy`](skills/token-economy/SKILL.md) | Cut token/context usage: targeted search, partial reads, filtered output, batching, delegation. |
| [`visual-design`](skills/visual-design/SKILL.md) | Original design that escapes generic AI looks: identity (logo, colour, type), brand guide, templates, UI/UX on proven design systems, tool paths for local GPU, cloud or free software; reference sites adapted only within licences. |
| [`workflow-automation`](skills/workflow-automation/SKILL.md) | Automations from plain language: short interview → spec → right platform (free/self-hosted first, or code) → built with idempotency, retries, alerts and approval steps → tested → runbook. |

### Roadmap
See [ROADMAP.md](ROADMAP.md) — vision, the full skill map (idea → company → brand → design → product → infrastructure → security → growth → AI), and the planned Rust orchestrator.

## Install

These are standard **Agent Skills** (agentskills.io spec), so most AI coding agents load them natively.
Full, sourced matrix: [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) (verified 2026-11-22).

### Quickest: one folder for most agents
Copy the skill folders into **`.agents/skills/`** — read by **OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI and Windsurf**:
```bash
git clone https://github.com/orchnesai/orchnes-360
mkdir -p .agents/skills && cp -r orchnes-360/skills/* .agents/skills/
```
For all your projects use `~/.agents/skills/` instead.

### Claude Code
Plugin (recommended):
```
/plugin marketplace add orchnesai/orchnes-360
/plugin install orchnes-360@orchnes-360
```
Or copy folders to `.claude/skills/` (project) or `~/.claude/skills/` (all projects). Cline also reads `.claude/skills/`.

### OpenAI Codex
Copy to `.agents/skills/` (project) or `~/.agents/skills/` (user). Invoke with `$skill-name`, `/skills`, or let Codex pick by description.
Optional always-on baseline: put the `agent-behavior` rules in `AGENTS.md`.

### Cursor · GitHub Copilot · Gemini CLI · Windsurf · Cline
Native skills paths (project / user):
| Tool | Project | User |
|---|---|---|
| Cursor | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` |
| GitHub Copilot | `.github/skills/` or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` (or `gemini skills install <repo-url> --consent`) | `~/.gemini/skills/` |
| Windsurf | `.agents/skills/` or `.windsurf/skills/` | `~/.agents/skills/` |
| Cline | `.cline/skills/` or `.claude/skills/` | `~/.cline/skills/` |

### Claude.ai / Claude apps
Zip a skill folder (folder name = skill name) and upload: Customize → Skills → + → Upload a skill.

### Tools without skills support (Aider, Continue, ChatGPT chat, any LLM API)
Use the instruction-file fallbacks in [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md): `AGENTS.md`, `CONVENTIONS.md` (Aider), `.continue/rules/`,
custom/project instructions (ChatGPT), or the system prompt (API). The [`orchnes`](https://github.com/orchnesai/orchnes-cli) CLI (Rust, companion repo) installs skills and generates these files for you.

## Design principles
1. **One skill, one job.** Focused descriptions trigger reliably.
2. **Lean `SKILL.md`.** Core procedure only; depth goes in `references/`, loaded on demand.
3. **Verifiable.** Every procedure ends in a checkable result, not "looks good".
4. **Vendor-neutral.** No dependency on a specific model or tool; tool-specific notes live in references.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md), the [code of conduct](CODE_OF_CONDUCT.md) and the [security policy](SECURITY.md). Changes are listed in [CHANGELOG.md](CHANGELOG.md). Run `python scripts/validate.py` before opening a PR.

## License
[MIT](LICENSE) © Ömer Faruk Alibal · [Orchnes](https://github.com/orchnesai)
