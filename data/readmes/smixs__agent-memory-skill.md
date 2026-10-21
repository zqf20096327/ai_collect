# agent-memory-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-green.svg)](https://python.org)
[![No Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)](#)

**Memory system for AI agents based on the Ebbinghaus forgetting curve.**

One Python file. Zero dependencies. Works with any directory of markdown files.

```
  Memory Strength
  1.0 ┤████████████████████████████████████████████████  ← just accessed
      │ ╲
  0.9 ┤   ╲                                              ← Day 7: active
      │     ╲
  0.8 ┤       ╲
      │         ╲
  0.7 ┤           ╲                                       ← Day 21: warm
      │             ╲
  0.6 ┤               ╲
      │                 ╲
  0.5 ┤                   ╲                               ← Day 33: cold
      │                     ╲
  0.4 ┤                       ╲
      │                         ╲
  0.3 ┤                           ╲
      │                             ╲
  0.2 ┤                               ╲
      │                                 ╲
  0.1 ┤─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─floor  ← Day 60+: archive
      │
  0.0 ┤
      └──┬──────┬──────────────┬────────────┬──────────→  Days
         0      7              21           60

         active    warm          cold         archive
```

---

## The Problem

AI agents forget everything between sessions. Two common solutions — and why they don't work:

**"Dump everything into context"** — Loads entire knowledge bases per turn. Burns 20K+ tokens before the conversation starts. No prioritization: a 2-month-old contact gets the same weight as yesterday's hot lead.

**"Vector search everything"** — Retrieves by semantic similarity but has no temporal awareness. A card accessed yesterday and a card untouched for 90 days look identical. No concept of "fading" or "forgetting." No serendipity.

Human memory does something different: it **decays over time**, **strengthens with use**, and occasionally **surprises you** with random connections. This skill brings that to AI agents.

---

## The Solution — 3-Layer Memory

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: HOT CONTEXT              always loaded, <4KB  │
│  └── State file — active focus, blockers, reminders     │
├─────────────────────────────────────────────────────────┤
│  Layer 2: SEARCHABLE VAULT          on-demand, unlimited │
│  └── Cards with YAML frontmatter — one file per entity  │
│      Tiers: core → active → warm → cold → archive       │
├─────────────────────────────────────────────────────────┤
│  Layer 3: ARCHIVE                   deep/creative only   │
│  └── Old logs, completed projects, cold contacts         │
│      Still searchable, excluded from default queries     │
└─────────────────────────────────────────────────────────┘
```

**Rule:** Each fact lives in ONE place. If it's in a card, don't duplicate it in the state file.

See [docs/architecture.md](docs/architecture.md) for full design rationale.

---

## Forgetting Curve

Inspired by Hermann Ebbinghaus (1885). Each card has a `relevance` score (0.0–1.0) that decays linearly:

```
relevance = max(0.1, 1.0 - days × 0.015)
```

### Tier Assignment

| Tier | Days Since Access | Relevance | Behavior |
|------|-------------------|-----------|----------|
| **core** | manual | 1.0 | Never auto-demoted. Identity, security, pricing. |
| **active** | 0–7 | 1.0–0.90 | Searched in all modes. Hot context. |
| **warm** | 8–21 | 0.89–0.69 | Default search. Gradually fading. |
| **cold** | 22–60 | 0.68–0.10 | Deep search only. Mostly forgotten. |
| **archive** | 60+ | 0.10 (floor) | Creative mode or explicit recall. |

### Graduated Touch (Spaced Repetition)

Unlike a simple "reset to top," `touch` promotes **one tier at a time**:

```
archive → cold → warm → active → active (refresh)
```

Multiple reads = stronger memory. Natural spaced repetition without manual scheduling.

---

## Search Modes

| Mode | Tiers Searched | When to Use | Token Cost |
|------|---------------|-------------|------------|
| **heartbeat** | core + active | Quick status checks, monitoring | ~2K |
| **normal** | active + warm | Most questions, task execution | ~5K |
| **deep** | all tiers | Strategy, "find everything about X" | ~15K |
| **creative** | random cold+archive | Brainstorming, ideation, "what if" | ~3K |

### Creative Mode — The Highlight Feature

Human creativity comes from random associations — shower thoughts, serendipitous encounters, dreams. Creative mode simulates this by pulling **random forgotten cards** back into working memory.

```bash
python3 memory-engine.py creative 5 vault/
```

```
  creative recall — 5 random cards:
    [cold] Cloud Migration Strategy
           projects/cloud-migration.md (r=0.25, last=2026-01-05)
    [archive] React Native Performance Notes
           notes/rn-performance.md (r=0.1, last=2025-11-20)
    ...

  read these cards and look for unexpected connections to your current task
```

The randomness is the feature, not a bug.

See [docs/search-protocols.md](docs/search-protocols.md) for detailed protocols.

---

## Quick Start

```bash
# 1. Copy to your project
curl -O https://raw.githubusercontent.com/smixs/agent-memory-skill/main/memory-engine.py

# 2. Scan your vault
python3 memory-engine.py scan vault/

# 3. Initialize cards (add YAML frontmatter)
python3 memory-engine.py init vault/ --dry-run   # preview first
python3 memory-engine.py init vault/              # apply

# 4. Run decay (update relevance scores)
python3 memory-engine.py decay vault/

# 5. Creative recall (surface forgotten cards)
python3 memory-engine.py creative 5 vault/
```

---

## All Commands

| Command | Description | Example |
|---------|-------------|---------|
| `scan` | Analyze files, report stats (no changes) | `memory-engine.py scan vault/` |
| `init` | Add YAML frontmatter to files missing it | `memory-engine.py init vault/ --dry-run` |
| `decay` | Update relevance scores and tiers | `memory-engine.py decay vault/` |
| `touch` | Promote card one tier up (graduated recall) | `memory-engine.py touch vault/crm/acme.md` |
| `creative` | Random N cards from cold/archive tiers | `memory-engine.py creative 5 vault/` |
| `daily` | Bootstrap and decay daily files (YYYY-MM-DD.md) | `memory-engine.py daily vault/daily/` |
| `stats` | Show tier distribution and health metrics | `memory-engine.py stats vault/` |
| `config` | Generate default `.memory-config.json` | `memory-engine.py config vault/` |

### Global Options

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview changes without writing files |
| `--verbose` | Show per-file details |
| `--config <path>` | Custom config file path |

---

## YAML Schema

### Required Fields

```yaml
---
type: crm                         # crm | lead | contact | project | personal | daily | note
description: >-                   # One-line search snippet
  Cloud provider, enterprise tier
tags: [cloud, enterprise]          # 2-5 freeform tags
status: active                    # active | draft | pending | done | inactive
---
```

### Auto-Managed Fields (by memory-engine.py)

```yaml
last_accessed: 2026-02-20         # When card was last read/touched
relevance: 0.85                   # 0.0-1.0, decays over time
tier: active                      # core | active | warm | cold | archive
```

### Full Example

```yaml
---
type: crm
description: >-
  Cloud infrastructure provider, enterprise tier, renewal Q2 2026
tags: [cloud, enterprise, renewal]
status: active
industry: IT
region: US
created: 2026-01-15
updated: 2026-02-20
last_accessed: 2026-02-20
relevance: 0.85
tier: active
---

# Acme Cloud Corp

## Overview
- **Industry:** Cloud Infrastructure
- **Contact:** Jane Smith, VP Sales
```

See [docs/yaml-schema.md](docs/yaml-schema.md) for the full schema reference.

---

## Configuration

Generate a default config:

```bash
python3 memory-engine.py config vault/
```

Creates `.memory-config.json`:

```json
{
  "tiers": {"active": 7, "warm": 21, "cold": 60},
  "decay_rate": 0.015,
  "relevance_floor": 0.1,
  "skip_patterns": ["_index.md"],
  "type_inference": {"crm/": "crm", "leads/": "lead"},
  "use_git_dates": true
}
```

### Domain-Specific Tuning

| Domain | Active | Warm | Cold | Rate | Why |
|--------|--------|------|------|------|-----|
| Sales/CRM | 3 | 10 | 30 | 0.025 | Fast-moving, deals expire quickly |
| Default | 7 | 21 | 60 | 0.015 | Balanced for general use |
| Research | 14 | 45 | 120 | 0.008 | Knowledge stays relevant longer |

### Config Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `tiers.active` | int | 7 | Days threshold for active tier |
| `tiers.warm` | int | 21 | Days threshold for warm tier |
| `tiers.cold` | int | 60 | Days threshold for cold tier |
| `decay_rate` | float | 0.015 | Relevance loss per day |
| `relevance_floor` | float | 0.1 | Minimum relevance (never reaches 0) |
| `skip_patterns` | list | `["_index.md"]` | Glob patterns to skip |
| `type_inference` | object | `{}` | Path → type mapping for auto-inference |
| `use_git_dates` | bool | true | Use git log for date resolution |

---

## Integration with Claude Code

### As a Skill

Copy the files into your project's skill directory:

```
.claude/skills/agent-memory/
├── SKILL.md              # Skill definition (Claude reads this)
├── scripts/
│   └── memory-engine.py  # Engine
└── references/
    ├── architecture.md
    ├── search-protocols.md
    └── yaml-schema.md
```

Claude Code will automatically discover and use the skill based on `SKILL.md`.

### Daily Decay via Cron

Add to your crontab for automatic forgetting:

```bash
# Run decay every day at midnight
0 0 * * * cd /path/to/vault && python3 memory-engine.py decay .
```

Or via systemd timer for more reliability.

### Full System

For the complete voice-first AI assistant (Telegram → Obsidian + Todoist), see [agent-second-brain](https://github.com/smixs/agent-second-brain).

---

## How It Compares

| | Dump All | Vector DB | **agent-memory** |
|---|---|---|---|
| **Context cost** | High (all cards every turn) | Medium (top-K results) | Low (tiered loading) |
| **Temporal awareness** | None | None | Built-in (decay + tiers) |
| **Serendipity** | None | None | Creative mode |
| **Dependencies** | None | Embedding model + DB | None (pure Python) |
| **Setup** | Copy files | Deploy infra | Copy one file |
| **Spaced repetition** | No | No | Graduated touch |
| **Works offline** | Yes | Needs model API | Yes |

---

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| Load all cards into context | Search on demand, filter by tier |
| Store same fact in 3 files | One card per entity, reference via links |
| Delete old files to "save space" | Let tier decay handle visibility |
| Touch every card during bulk ops | Only touch on meaningful read/update |
| Build elaborate review systems | Let decay handle it — unused = fades |

---

## License

[MIT](LICENSE)

---

## Star History

<a href="https://www.star-history.com/?repos=smixs%2Fagent-memory-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=smixs/agent-memory-skill&type=date&theme=dark&legend=top-left&sealed_token=QkXOx4v6E30RTARsgYU70MEBmqy7LnT40AEB4SclgCk9Sg1kWtiJdzdhwVz5uLkAcR4TXEGc1t1osFubxNF4OQAfK1CHU0lSzz9KyLubFm9ndpYbIThJrfxeDqcZUiYVvSx7JoUO8GLVSfnY5TQfEqP2N-Lu9KNYomHhtWm5uUmMSWqkgL61FU_px0Ul" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=smixs/agent-memory-skill&type=date&legend=top-left&sealed_token=QkXOx4v6E30RTARsgYU70MEBmqy7LnT40AEB4SclgCk9Sg1kWtiJdzdhwVz5uLkAcR4TXEGc1t1osFubxNF4OQAfK1CHU0lSzz9KyLubFm9ndpYbIThJrfxeDqcZUiYVvSx7JoUO8GLVSfnY5TQfEqP2N-Lu9KNYomHhtWm5uUmMSWqkgL61FU_px0Ul" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=smixs/agent-memory-skill&type=date&legend=top-left&sealed_token=QkXOx4v6E30RTARsgYU70MEBmqy7LnT40AEB4SclgCk9Sg1kWtiJdzdhwVz5uLkAcR4TXEGc1t1osFubxNF4OQAfK1CHU0lSzz9KyLubFm9ndpYbIThJrfxeDqcZUiYVvSx7JoUO8GLVSfnY5TQfEqP2N-Lu9KNYomHhtWm5uUmMSWqkgL61FU_px0Ul" />
 </picture>
</a>
