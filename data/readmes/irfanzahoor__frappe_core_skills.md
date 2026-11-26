# frappe-best-skill

[![Frappe v14 | v15 | v16](https://img.shields.io/badge/Frappe-v14%20%7C%20v15%20%7C%20v16-0089FF)](https://frappeframework.com)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-white)](https://code.claude.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-black)](LICENSE)

The best parts of **frappe-code-standards** (code placement, standard APIs) and
**Frappe_Claude_Skill_Package** (Server Script sandbox, v14–v16 changes, errors, testing, ops),
split into focused **branches**. Each task loads only its own branch.

## Why this exists

AI assistants can write Frappe code that *works* but doesn't *belong*: form logic
dumped into `hooks.py`, `raise Exception` instead of `frappe.throw`, validation
only in JavaScript, queries inside loops, Server Scripts with `import` statements
that can never run. This package gives the assistant the rules a senior Frappe
developer would enforce — in the right file, with the framework's own APIs — and
only loads the rules for the task at hand.

**Tokens:** at session start only 22 one-line descriptions load. A skill's body loads only when
its task comes up.

> [!NOTE]
> Skills guide the assistant; they don't guarantee correct output. Review the
> result the way you would review a teammate's code, and run the review
> checklist in `frappe-core` before finishing a task.

## Skills

| Skill | Use for |
|---|---|
| `frappe-core` | All Frappe coding: placement, controllers, JS, hooks, permissions, review |
| `frappe-server-scripts` | Server Scripts in the UI (sandbox, no imports) |
| `frappe-reports-print` | Script/Query reports, print formats, Jinja |
| `frappe-performance` | Slow code, N+1, caching, enqueue |
| `frappe-upgrade` | v14 -> v15 -> v16 API changes, upgrades |
| `frappe-debug` | Error -> cause -> fix, with worked examples in `references/common-errors.md` |
| `frappe-testing` | Unit/integration tests, CI |
| `frappe-ops` | bench, deploy, backup/restore, Frappe Cloud |
| `frappe-architect` | Plan features/apps, data model, customize vs build |
| `frappe-workflow` | Workflows, approvals |
| `frappe-notifications` | Email, Notification rules, realtime |
| `frappe-integrations` | REST API, webhooks, OAuth, Data Import |
| `frappe-website` | Website, portal, Web Forms |
| `frappe-ui` | Workspaces, dashboards, Pages, dialogs, Vue SPA |
| `frappe-permissions` | Roles, User Permissions, `has_permission`, sharing, 403s |
| `frappe-scheduler` | Scheduler events, background jobs, queues, job health |
| `frappe-erpnext-modules` | Selling, buying, stock, manufacturing, accounts, HRMS, CRM, Helpdesk, Projects, Assets flows |
| `frappe-studio` | Studio visual app builder (v16.60): apps, pages, blocks |
| `frappe-flow` | Frappe Flow AI workflows (v16.60): triggers, agents, safety |
| `frappe-insights` | Insights BI: workbooks, queries, charts, dashboards |
| `frappe-security` | Security audit: injection, XSS, permissions, secrets, files |
| `frappe-data` | Data Import, bulk updates, migration, cleanup, exports |

## Version compatibility

| Feature | v14 | v15 | v16 |
|---|:---:|:---:|:---:|
| Type annotations | ❌ | ✅ | ✅ |
| UUID autoname | ❌ | ✅ | ✅ |
| Data masking (`mask` on fields) | ❌ | ❌ | ✅ |
| `extend_doctype_class` hook | ❌ | ❌ | ✅ |
| `has_permission` must return explicit `True` | ❌ | ❌ | ✅ |
| DB commit inside document hooks | ✅ | ✅ | ❌ |
| Server Scripts enabled by default | ✅ | ❌ | ❌ |
| `/app` URL | ✅ | ✅ | ❌ (now `/desk`) |
| PDF via wkhtmltopdf | ✅ | ✅ | ❌ (Chrome renderer) |
| Studio (visual app builder) | ❌ | ❌ | ✅ (v16.60) |
| Frappe Flow (AI workflows) | ❌ | ❌ | ✅ (v16.60) |

Full version-change tables live in the `frappe-upgrade` skill.

## Agents and commands

Available when the plugin is installed in Claude Code (not with a manual copy):

| Agent / command | Does |
|---|---|
| `frappe-reviewer` (agent) | Reviews Frappe code against the `frappe-core` rules, outputs a severity-ordered findings table |
| `frappe-migrator` (agent) | Plans a v14 -> v15 -> v16 upgrade: deprecated APIs, patches, backup, test plan |
| `/frappe-review` | Review a file or folder (defaults to git-changed files) |
| `/frappe-upgrade-check` | Scan the project for removed APIs for a target version (default v16) |
| `frappe-builder` (agent) | Builds a full feature from one prompt: DocType, fields, code, tests |
| `frappe-doctor` (agent) | Read-only site health check: jobs, scheduler, slow queries, disk |
| `/frappe-new-field` | Add fields to a DocType with the field-layout rules |

## Install

### Claude Code — plugin marketplace

```bash
claude plugin marketplace add irfanzahoor/frappe_core_skills
claude plugin install frappe-best-skill@irfanzahoor
```

Keep it up to date with `/plugin` in Claude Code → **Marketplaces** → `irfanzahoor`
→ **Enable auto-update**. If the marketplace command is rejected, use the manual
install below — it works the same way. To validate a local copy, run
`claude plugin validate` in the repo.

### Claude Code — manual

Copy all folders inside `skills/` to `~/.claude/skills/` (or `.claude/skills/` in a project).
To install a subset, keep `frappe-core` and add the branches you need.

### Codex / Cursor / Gemini / Copilot

Copy the folder into the repo and keep `AGENTS.md` at the root.
Or copy or symlink it as `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/frappe.md` or `.github/copilot-instructions.md`.

### Claude.ai Projects

Upload `frappe-core/SKILL.md` plus the branches you need as knowledge.

## Use in a project

Copy [`templates/CLAUDE.md`](templates/CLAUDE.md) into the root of your Frappe project
and fill in the project facts: Frappe version, which apps are yours, your site name
and the prefix you use for custom fields. Claude reads this file at the start of
every session, which tells it which DocTypes it can edit directly and which ones
must be extended through hooks — and which skill branch to load for each task.

Spot a mistake Claude keeps making in that one project? Add a line under
**Project-specific rules**.

## Examples

**Errors — wrong vs right:**

```python
# Wrong: generic exception, no translation
raise Exception("Qty cannot be negative")

# Right: framework error, translated, stops the save
frappe.throw(_("Row {0}: Qty cannot be negative").format(row.idx))
```

**New fields — wrong vs right:**

```python
# Wrong: 8 fields dumped in one block — the form scrambles
# Right: read the form first, group under a Section Break,
# max 2 fields per row with a Column Break, child table under
# its own section — see `frappe-core/references/field-layout.md`
```

## What's inside

```
.
├── AGENTS.md                          Rules for any AI assistant (Claude, Codex, Cursor, ...)
├── CHANGELOG.md                       Version history
├── CONTRIBUTING.md                    How to add or fix a skill
├── templates/
│   └── CLAUDE.md                      Project template — copy into your Frappe project
├── .claude-plugin/
│   ├── plugin.json                    Claude Code plugin (v2.3.0)
│   └── marketplace.json               Plugin marketplace entry
├── .github/workflows/
│   └── quality.yml                    Validates skill frontmatter, JSON, README links, relative links, markdown style
├── agents/
│   ├── frappe-reviewer.md             Code-review agent
│   ├── frappe-migrator.md             Upgrade-planning agent
│   ├── frappe-builder.md              Full-feature builder agent
│   └── frappe-doctor.md               Site health-check agent
├── commands/
│   ├── frappe-review.md               /frappe-review
│   ├── frappe-upgrade-check.md        /frappe-upgrade-check
│   └── frappe-new-field.md            /frappe-new-field
└── skills/
    ├── frappe-core/                   Core rules + references (placement, patterns, review)
    │   └── references/
    │       ├── code-placement.md
    │       ├── server-patterns.md
    │       ├── client-patterns.md
    │       ├── hooks-and-customization.md
    │       ├── review-checklist.md
    │       └── field-layout.md
    ├── frappe-debug/
    │   └── references/
    │       └── common-errors.md       Debug workflow + worked fixes
    ├── frappe-permissions/
    │   └── references/
    │       └── permission-debugging.md
    ├── frappe-testing/
    │   └── references/
    │       └── test-patterns.md
    ├── frappe-performance/
    │   └── references/
    │       └── query-index-guide.md
    ├── frappe-ops/
    │   └── references/
    │       └── backup-restore-runbook.md
    ├── frappe-upgrade/
    │   └── references/
    │       └── upgrade-v15-v16.md
    └── frappe-server-scripts/ ...     19 more focused branches
```

The skills are plain Markdown. They run no scripts, make no network calls and collect no data.

## What's new in v2.3.0

- New skills: `frappe-studio` (visual app builder in v16.60), `frappe-flow`
  (AI workflow builder), `frappe-insights` (BI dashboards and queries),
  `frappe-security` (security audit) and `frappe-data` (Data Import, bulk
  updates, migration).
- New agents: `frappe-builder` (full feature from one prompt) and
  `frappe-doctor` (read-only site health check); new command
  `/frappe-new-field` (adds fields with the field-layout rules).
- `frappe-upgrade` now has a v15 → v16 breaking-changes reference
  — see `skills/frappe-upgrade/references/upgrade-v15-v16.md`.
- `frappe-erpnext-modules` now covers HRMS, CRM, Helpdesk, Projects and Assets.
- Reference files for thin skills: testing patterns, query/index guide,
  backup/restore runbook.
- README examples, FAQ and comparison table; CI now checks relative links
  and markdown style; issue and PR templates.

## What's new in v2.2.0

- New skills: `frappe-permissions` (roles, User Permissions, sharing, 403 debugging),
  `frappe-scheduler` (scheduler events, queues, job health) and `frappe-erpnext-modules`
  (selling, buying, stock, manufacturing, accounts flows).
- New agents: `frappe-reviewer` and `frappe-migrator`; new commands `/frappe-review`
  and `/frappe-upgrade-check`.
- `CHANGELOG.md`, `CONTRIBUTING.md` and a CI quality workflow (`.github/workflows/quality.yml`).
- LICENSE copyright fixed to Muhammad Irfaan.
- README version-compatibility table (v14/v15/v16).

## What's new in v2.1.0

- `templates/CLAUDE.md` — project setup with per-task branch routing.
- Plugin marketplace install (`claude plugin marketplace add ...`).
- `frappe-debug/references/common-errors.md` — debug workflow plus worked fixes
  for `DoesNotExistError`, `PermissionError`, `TimestampMismatchError`,
  `DuplicateEntryError`, slow queries and jobs that never run.

## FAQ

**Does it work with AIs other than Claude?**
Yes. Skills are plain Markdown and the repo ships a root `AGENTS.md`, so Codex
uses it natively, Cursor/Gemini/Copilot pick it up from the paths in
[Install](#codex--cursor--gemini--copilot), and chatbots take the SKILL.md files
as knowledge. Agents and slash commands are Claude Code–only.

**Which Frappe/ERPNext versions?**
v14, v15 and v16 — see the compatibility table above.

**Does it guarantee correct output?**
No. Skills guide the assistant; review the result like a teammate's code and
run the `frappe-core` review checklist.

**How do I update?**
Plugin install: `/plugin` in Claude Code → Marketplaces → `irfanzahoor` →
Enable auto-update. Manual install: copy `skills/` again.

**Can I contribute?**
Yes — see [CONTRIBUTING.md](CONTRIBUTING.md). One change per PR, against `develop`.

## Comparison

|  | This repo | NexTash frappe-code-standards | Impertio Frappe Claude Skill Package |
|---|---|---|---|
| Skills | 22, branched | 1 | 61 |
| Token-light (loads only the task's branch) | ✅ | ✅ | ❌ (one big skill) |
| Agents / slash commands | 4 / 3 | — | — |
| CI quality checks | ✅ | — | — |
| Studio / Flow / Insights (v16.60) | ✅ | — | — |
| License | MIT | MIT | MIT |

Stars/forks as of Nov 2026: NexTash 3 stars; Impertio 210 stars, 61 forks;
this repo is new (0 stars).

## Credits

Core placement rules and reference files come from
[NexTash/frappe-code-standards](https://github.com/NexTash/frappe-code-standards)
(MIT). Breadth — Server Script sandbox, version changes, errors, testing, ops —
is distilled from
[Impertio-Studio/Frappe_Claude_Skill_Package](https://github.com/Impertio-Studio/Frappe_Claude_Skill_Package)
(MIT). This package re-organises both into one branched set.

## License

[MIT](LICENSE) © Muhammad Irfaan
