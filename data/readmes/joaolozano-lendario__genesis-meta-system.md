# GENESIS

> **A Meta-System That Generates Claude Code Native Systems**

```
   ██████╗ ███████╗███╗   ██╗███████╗███████╗██╗███████╗
  ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔════╝██║██╔════╝
  ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ███████╗██║███████╗
  ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ╚════██║██║╚════██║
  ╚██████╔╝███████╗██║ ╚████║███████╗███████║██║███████║
   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝╚══════╝

   The System That Creates Systems
```

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Built%20for-Claude%20Code-blueviolet)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)](https://github.com/yourusername/genesis-meta-system)

---

## What is GENESIS?

**GENESIS is a meta-system** — a system that generates other systems.

```
INPUT:  Domain description (text brief)
        "I want a system for analyzing marketing campaigns"

PROCESS: 8-phase pipeline with gates, scoring, validation

OUTPUT: Complete Claude Code Native system with:
        - Specialized agents (inspired by top practitioners)
        - Executable tasks with clear inputs/outputs
        - Orchestration workflows
        - Domain-specific knowledge bases
        - Ready-to-use slash commands
        - Automatic validation with real scoring
```

**In other words:** You describe a domain, GENESIS creates the complete system.

---

## Why Claude Code Native Matters

GENESIS generates systems designed specifically for **Claude Code's architecture**:

| Claude Code Feature | How Generated Systems Use It |
|--------------------|------------------------------|
| **Slash Commands** | Complete command set in `.claude/commands/` |
| **CLAUDE.md** | System identity and instructions |
| **Skills** | Specialized capabilities in `.claude/skills/` |
| **File Operations** | STATE.yaml for persistent memory |
| **Task Tool** | Parallel agent execution |

This means generated systems:
- **Work natively** with Claude Code
- **Persist state** across sessions
- **Scale** with parallel processing
- **Self-validate** with real scoring

---

## Quick Start

```bash
# 1. Clone and open with Claude Code
git clone https://github.com/yourusername/genesis-meta-system.git
cd genesis-meta-system
claude

# 2. Generate a new system
/GENESIS:tasks:generate-system

# 3. Follow the interactive wizard
# - Describe your domain
# - Confirm classification
# - Approve architecture + Dream Team
# - Receive system with quality score

# 4. Validate the generated system
/GENESIS:tasks:validate-system outputs/systems/my-system/
```

---

## The 8-Phase Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    GENESIS PIPELINE v2.1                         │
└─────────────────────────────────────────────────────────────────┘

P0: INTERPRET ──► G0 ──► P1: CLASSIFY ──► G1 ──► P2: STRUCTURE ──► G2
     │                        │                        │
     └── TodoWrite           └── Extended             └── Dream Team
         initialized             Thinking                 Designer

──► P3-P6: GENERATE (PARALLEL) ──► G7 ──► P7: ASSEMBLE ──► P8: VALIDATE ──► G8
         │                              │                        │
         └── Task tool                  └── Files               └── Glob/Grep
             (4 parallel                    written                 scoring
              agents)

Gates (Interactive Checkpoints):
  G0: Brief understanding (AskUserQuestion - REVIEW)
  G1: Classification confirmation (GO/NO-GO)
  G2: Architecture + Dream Team approval (GO/NO-GO)
  G7: Pre-assembly validation (automatic)
  G8: Final approval with score (CRITICAL)
```

---

## State-of-Art Features (v2.1.0)

### 1. Dream Team Designer
Generates **synthetic expert teams** for each system:
- Inspired by top 0.1% practitioners in the domain
- 5-Layer Cognitive Architecture for deep thinkers
- Cognitive types: THINKER, HYBRID, EXECUTOR

### 2. TodoWrite Integration
- Creates 11 tracking items (phases + gates)
- Updates status in real-time
- Visual progress throughout generation

### 3. AskUserQuestion at Gates
- **G0:** Validate brief understanding
- **G1:** Confirm domain classification (GO/NO-GO)
- **G2:** Approve architecture (GO/NO-GO)
- **G8:** Final system approval (CRITICAL)

### 4. Task Tool Parallelism
- Phases P3-P6 execute in parallel
- Simultaneous generation of agents, workflows, tasks, support
- Drastically faster than sequential execution

### 5. Extended Thinking
- **P1 (Classify):** Analyzes multiple classification factors
- **P2 (Structure):** Considers architecture tradeoffs

### 6. Real Scoring (Not Estimates)
- **Glob:** Counts actual files
- **Grep:** Verifies references exist
- **Formula:** Calculates numeric scores automatically

```python
COMPLETENESS = (files_found / files_expected) * 100
CONSISTENCY = (valid_refs / total_refs) * 100
PRINCIPLES = (passed_checks / 20) * 100
OVERALL = (COMPLETENESS * 0.35) + (CONSISTENCY * 0.35) + (PRINCIPLES * 0.30)
```

---

## Supported System Types

| Type | Description | Example |
|------|-------------|---------|
| **COGNITIVE** | Deep cognitive processing | Mental cloning, decision frameworks |
| **TECHNICAL** | Technical automation | DevOps, CI/CD, integrations |
| **CREATIVE** | Creative production | Content factory, design systems |
| **OPERATIONAL** | Business processes | CRM, ERP, Growth OS |
| **HYBRID** | Combination of types | GENESIS itself |

---

## All Commands (11 total)

### Main Commands

| Command | Description |
|---------|-------------|
| `/GENESIS:tasks:generate-system` | **Generate complete system** (TodoWrite + AskUserQuestion + Task tool) |
| `/GENESIS:tasks:validate-system` | **Validate system** with REAL scoring (Glob/Grep) |

### Management Commands

| Command | Description |
|---------|-------------|
| `/GENESIS:tasks:list-systems` | List all systems in outputs/systems/ |
| `/GENESIS:tasks:show-system` | Show details of a specific system |
| `/GENESIS:tasks:export-system` | Export system to external directory |
| `/GENESIS:tasks:delete-system` | Remove generated system (with confirmation) |

### Control Commands

| Command | Description |
|---------|-------------|
| `/GENESIS:tasks:check-status` | View current generation status |
| `/GENESIS:tasks:resume-generation` | Resume interrupted generation |
| `/GENESIS:tasks:abort-generation` | Abort ongoing generation |
| `/GENESIS:tasks:run-tests` | Execute test suite (20 tests) |

---

## Project Structure

```
genesis-meta-system/
├── .claude/
│   ├── commands/GENESIS/tasks/    # 11 slash commands
│   └── skills/genesis-core.md     # Main skill
│
├── agents/                        # 6 specialized agents
│   ├── meta-orchestrator.md
│   ├── domain-analyst.md
│   ├── system-architect.md
│   ├── component-generator.md
│   ├── system-validator.md
│   └── dream-team-designer.md     # NEW v2.1
│
├── tasks/                         # 23 pipeline tasks
│   ├── 00-interpret/              # P0: Interpret domain brief
│   ├── 01-classify/               # P1: Classify domain type
│   ├── 02-structure/              # P2: Design structure + dream team
│   ├── 03-agents/                 # P3: Define agents
│   ├── 04-workflows/              # P4: Design workflows
│   ├── 05-tasks/                  # P5: Define tasks
│   ├── 06-support/                # P6: Create templates, checklists
│   ├── 07-generate/               # P7: Generate all files
│   └── 08-validate/               # P8: Validate system
│
├── templates/                     # 7 output templates
│   └── system-output/
│       ├── agent-template.md
│       ├── cognitive-agent-template.md  # NEW v2.1
│       ├── task-template.md
│       └── ...
│
├── knowledge/                     # 13+ knowledge files
│   ├── domain-types.yaml
│   ├── agent-personas.yaml
│   ├── cognitive-architecture.yaml     # NEW v2.1
│   ├── dream-team-patterns.yaml        # NEW v2.1
│   ├── principles-reference.md
│   └── examples/
│
├── docs/                          # Complete documentation
├── hooks/                         # Git automation
├── ops/sops/                      # Standard Operating Procedures
│
├── STATE.yaml                     # System consciousness
├── config.yaml                    # Configuration
└── outputs/systems/               # Generated systems go here
```

---

## Generated System Portfolio

GENESIS has successfully generated these systems:

### OMNI OS - Marketing Dream Team
- **Type:** COGNITIVE
- **Agents:** 12 marketing specialists
- **Inspiration:** Kotler, Kahneman, McKee, Schwartz, Ries, Pulizzi, Neumeier
- **Commands:** `/OMNI:tasks:modo-guiado`, `/OMNI:tasks:modo-automatico`

### SUEMP - Meta-Principle Extraction
- **Type:** COGNITIVE
- **Agents:** 9 (Munger, Feynman, Shannon, Hofstadter, etc.)
- **Focus:** Extract universal laws cross-domain
- **Pipeline:** 7 phases with quantitative metrics

### ALCHEMIST - Event Apps Builder
- **Type:** HYBRID
- **Agents:** 10 (Gary Vee, Fowler, Rams, Cagan, Kent Beck, etc.)
- **Focus:** Transform briefs into interactive event apps
- **Time:** 30-60 minutes per complete app

### FUNNEL ARCHITECT - Transformation Funnels
- **Type:** OPERATIONAL
- **Agents:** 7 (Brunson, Hormozi, McKee, Miller, etc.)
- **Focus:** Funnels that transform (not just convert)
- **Pipeline:** P0→P6 with philosophical validation

### ANATOMISTA DE COPY - Reverse Engineering
- **Type:** COGNITIVE
- **Agent:** 1 (Halbert + Schwartz + Ogilvy + Bencivenga + Kennedy + Hormozi)
- **Focus:** 7-Layer Copy Law

---

## Core Principles (20 Total)

GENESIS follows 20 principles distilled from successful systems:

### Critical (Always Applied)

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **P1** | Parallelism-First | Task tool in P3-P6 |
| **P2** | State-Externalized | STATE.yaml |
| **P4** | Checkpoints-Strategic | 5 gates in pipeline |
| **P12** | Clarify-Before-Execute | AskUserQuestion |
| **P18** | Elicitation-Non-Negotiable | Gates never skipped |

See all 20 principles: `knowledge/principles-reference.md`

---

## Quality Metrics

| Metric | Threshold | Target | Current |
|--------|-----------|--------|---------|
| Completeness | >= 95% | 98% | 98% |
| Consistency | = 100% | 100% | 100% |
| Principles | >= 90% | 95% | 95% |
| **Overall** | >= 89% | **~98%** | **98%** |

---

## Documentation

| Doc | Content |
|-----|---------|
| [docs/README.md](docs/README.md) | Complete overview |
| [docs/QUICK-START.md](docs/QUICK-START.md) | 5-minute guide |
| [docs/USER-GUIDE.md](docs/USER-GUIDE.md) | Full usage guide |
| [docs/EXAMPLES.md](docs/EXAMPLES.md) | Generated system examples |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Internal design |
| [docs/STATE-OF-ART-FEATURES.md](docs/STATE-OF-ART-FEATURES.md) | v2.0+ features |
| [docs/API-REFERENCE.md](docs/API-REFERENCE.md) | Command reference |

---

## Example Usage

```bash
# 1. Open project
cd genesis-meta-system
claude

# 2. Generate system for "Growth OS"
/GENESIS:tasks:generate-system

# Claude asks (AskUserQuestion G0):
# "Describe your system domain"

# You respond:
# "A system for managing personal growth.
#  Captures insights from multiple sources, analyzes patterns,
#  and generates weekly focused actions. Type OPERATIONAL."

# Claude classifies (Extended Thinking P1)
# Claude asks confirmation (AskUserQuestion G1):
# "Domain: OPERATIONAL, Complexity: MEDIUM. Confirm?"

# You: "Yes"

# Claude designs architecture (Extended Thinking P2)
# Claude asks approval (AskUserQuestion G2):
# "4 agents, 8 tasks, weekly workflow. Approve?"

# You: "Yes"

# Claude generates everything in parallel (Task tool P3-P6)
# Claude validates (Glob/Grep P8)
# Claude asks final approval (AskUserQuestion G8):
# "System complete. Score: 95%. Approve?"

# You: "Yes"

# System ready in: outputs/systems/growth-os/
```

---

## Requirements

- **Claude Code CLI** installed
- **Permissions** for file creation
- **OS:** Windows, macOS, or Linux

---

## Test Suite

GENESIS includes 20 automated tests:
- 5 smoke tests
- 5 generation tests
- 5 validation tests
- 5 utility tests

Run with: `/GENESIS:tasks:run-tests`

---

## Contributing

We welcome contributions:
- Example systems for different domains
- Template improvements
- Documentation translations
- Bug reports and suggestions

---

## License

MIT — Use, modify, distribute freely.

---

## For AI Instances Reading This

If you're an AI reading this context:

1. **Always read STATE.yaml first** — contains current state
2. **Use the commands** — `/GENESIS:tasks:generate-system` to create systems
3. **Follow the pipeline** — 8 phases with validation gates
4. **Respect the 20 principles** — see `knowledge/principles-reference.md`
5. **Scoring is real** — Glob/Grep, not estimates

---

<p align="center">
  <strong>GENESIS v2.1.0</strong><br>
  <em>Dream Team Designer Edition</em><br><br>
  The meta-system that creates systems that create value.
</p>
