# agent-skills

![Demo](docs/demo.png)

*Demo: routing a task to the best-matching skill in the library.*

A library of **1,224 agent skills** across **42 domains**, with a deterministic router that
selects the right skill (and the right chain of skills) for any task — from everyday
assistant work down to single-step micro-tasks.

[![CI](https://github.com/gravion-ux/agent-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/gravion-ux/agent-skills/actions/workflows/ci.yml)
[![Secret Scan](https://github.com/gravion-ux/agent-skills/actions/workflows/secret-scan.yml/badge.svg)](https://github.com/gravion-ux/agent-skills/actions/workflows/secret-scan.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What this is, and what it is not

**It is**

- 1,224 hand-authored skills, each a complete nine-section playbook: purpose, when to use,
  when *not* to use, inputs, procedure, output contract, validation checklist, safety notes
  and related skills.
- A deterministic BM25 router (`agentskills route`) that ranks the catalogue against a
  free-form task description with no network calls, no model calls and no randomness.
- A master skill that uses that ranking plus the per-domain routers to pick one primary
  skill and up to three supporting skills, then sequences them.
- 42 domain routers, one per domain, listing every leaf skill in that domain with its
  "use when" clause so an agent can pick a chain without loading the whole catalogue.
- A zero-dependency Python package (`agentskills`) that ships the catalogue as a
  machine-readable index and exposes it through a CLI.

**It is not**

- Not a hosted service, not an API, not a marketplace.
- Not a prompt collection with one-line entries. Every skill has a full procedure, an
  output contract and a validation checklist.
- Not a runtime that executes anything for you. The skills are instructions for an agent;
  the Python package only lists, routes, exports and packs them.
- Not trained on, or tested against, any proprietary dataset. The catalogue is written in
  plain English in this repository.

## Domains

| Domain | Skills | Domain | Skills |
|---|---:|---|---:|
| `ai-agents` | 57 | `agent-tooling-meta` | 26 |
| `api-design` | 22 | `architecture-design` | 26 |
| `business-ops` | 30 | `code-quality` | 30 |
| `communication` | 26 | `content-creation` | 30 |
| `cooking-food` | 14 | `data-analysis` | 30 |
| `data-engineering` | 40 | `databases` | 33 |
| `design-ux` | 34 | `dev-experience` | 30 |
| `devops-cloud` | 48 | `documentation` | 30 |
| `education` | 22 | `finance-accounting` | 18 |
| `health-wellness` | 18 | `home-diy` | 18 |
| `hr-recruiting` | 18 | `image-visual` | 22 |
| `legal-compliance` | 18 | `learning-skills` | 15 |
| `llm-engineering` | 44 | `ml-model-training` | 34 |
| `mobile-desktop` | 22 | `networking` | 26 |
| `observability` | 26 | `personal-finance` | 12 |
| `productivity` | 35 | `project-management` | 26 |
| `relationships-social` | 11 | `research` | 27 |
| `sales-marketing` | 26 | `security` | 66 |
| `software-engineering` | 66 | `technical-writing` | 22 |
| `testing-qa` | 34 | `travel-lifestyle` | 18 |
| `video-audio` | 22 | `web-development` | 52 |
| **Total** | **1,224** | | |

The generated, always-current version of this table lives in
[`catalog/CATALOG.md`](catalog/CATALOG.md).

## Quick start

```bash
python -m pip install agentskills
```

```bash
# list the catalogue, or one domain
agentskills list
agentskills list --domain ai-agents
agentskills list --json

# rank skills against a task — deterministic, offline, instant
agentskills route "migrate a database to postgres" --top 5
agentskills route "set up a postgres migration" --top 5 --json

# read one skill as JSON
agentskills show migrate-postgres-schema

# check the repository (skills, routers, index, catalogue mirror)
agentskills validate
agentskills validate --json

# copy skills into another agent's skills directory
agentskills export --out ../my-agent/skills --domain security

# write a distributable zip
agentskills pack --out dist/agent-skills.zip
```

The package also works from source without installing:

```bash
export PYTHONPATH=src:.
python -m agentskills.cli route "plan a launch" --top 5
```

### Python API

```python
from agentskills import load_catalogue
from agentskills.router import route

catalogue = load_catalogue()
for hit in route(catalogue, "write a migration runbook", top=5):
    print(hit.score, hit.skill.name, hit.skill.domain)
```

## How routing works — three layers

1. **Deterministic scorer (`agentskills route`).** BM25 over five weighted fields —
   name 3, triggers 3, tags 2, description 2, domain 1 — with K1 = 1.5 and B = 0.75.
   Hyphenated compounds are matched whole *and* by part. The same query always produces
   the same ranking; ties break by skill name ascending. See [`docs/ROUTING.md`](docs/ROUTING.md).
2. **Master skill (`skills/master/SKILL.md`).** Restates the task, reads the scorer's
   shortlist, opens the routers for the shortlisted domains, drops any candidate whose
   "when NOT to use" clause rules it out, and selects one primary skill plus up to three
   supporting skills.
3. **Domain routers (`routers/<domain>/SKILL.md`).** One per domain, each listing every
   leaf skill in that domain with its "use when" clause, so an agent can pick a chain
   without reading the whole catalogue.

The three layers are complementary: the scorer narrows 1,224 skills to a shortlist, the
routers give structural context, and the master skill applies judgement.

## Skill file format

Every leaf skill is a `SKILL.md` with YAML frontmatter and nine sections in a fixed order:

```markdown
---
name: migrate-postgres-schema
description: Move a relational schema to PostgreSQL with a zero-downtime runbook. Use when the user needs to port MySQL, SQLite or SQL Server DDL to PostgreSQL.
domain: data-engineering
tags: [postgres, migration, schema]
triggers: ["migrate to postgres", "port database to postgres"]
---

# Move a relational schema to PostgreSQL

## Purpose
...
## When to use
...
## When NOT to use
...
## Inputs required
...
## Procedure
...
## Output contract
...
## Validation checklist
...
## Safety notes
...
## Related skills
...
```

Full rules and an annotated example: [`docs/SKILL_FORMAT.md`](docs/SKILL_FORMAT.md).

## Repository layout

```text
catalog/source/     hand-authored source of truth (one module per domain)
catalog/CATALOG.md  generated human-readable catalogue
skills/             generated leaf skills + the hand-written master skill
routers/            generated per-domain routers
src/agentskills/    the installable package (router, generator, validator, CLI)
scripts/            generation, validation and secret-scanning entry points
docs/               architecture, format, routing and contribution guides
```

`skills/` and `routers/` are **generated**. Edit `catalog/source/` and regenerate — never
hand-edit the generated files.

## Contributing a skill

```bash
git clone https://github.com/gravion-ux/agent-skills.git
cd agent-skills
python -m pip install -e ".[dev]"

# edit catalog/source/<domain>.py, then:
python scripts/generate_skills.py
python scripts/validate_skills.py
python -m pytest tests/ -q
python -m ruff check src tests scripts
python -m mypy src/agentskills
```

Full authoring rules, the `spec()` signature and a worked example:
[`docs/CONTRIBUTING_SKILLS.md`](docs/CONTRIBUTING_SKILLS.md). Contribution workflow:
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE).
