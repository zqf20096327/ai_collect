# GenAI development techniques

A comparison of ways to organize and direct AI coding agents, for developers, tech leads, and engineering managers choosing an approach.

## Start here

**[Choosing Your Approach](techniques/choosing-your-approach.md)** — Match a technique to your team size, project type, industry, and development activity.

**[Overview and comparison matrix](overview.md)** — How the approaches differ, with a comparison table and category summaries.

## What this site covers

Compare workflows, reusable skills, and governance controls using dated research findings. Models and runtimes appear only where they help explain a technique. This is not a ranking or an adoption survey.

---

## Detailed guides

See [Research Methodology](methodology.md) for sources, inclusion criteria, evidence labels, and update policy.

### Spec-driven development

Star counts are snapshots observed on October 27, 2026. They are awareness signals, not adoption evidence.

| Technique | Description | Stars |
|-----------|-------------|-------|
| [GSD (Get Shit Done)](techniques/gsd.md) | Spec-driven workflow continued as GSD Core after the original repository was archived | ~10.9K* |
| [Spec Kit](techniques/spec-kit.md) | GitHub's official toolkit for spec-driven development — specs → plans → tasks | ~143K |
| [OpenSpec](techniques/openspec.md) | Change-centric SDD with delta specs, broad multi-tool support, and a vendor-neutral skills target | ~73K |

\* GSD migrated from an archived repository with ~64.7K stars to `open-gsd/gsd-core`; the successor repository started its own count.

### Multi-agent orchestration

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Squad](techniques/squad.md) | Coordinator-based multi-agent orchestration with persistent memory, casting, and ceremonies | ~3.3K |
| [BMAD](techniques/bmad.md) | AI-driven agile framework with specialized roles, structured phases, and modular workflows | ~55K |

### Skill-based development

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Superpowers](techniques/superpowers.md) | Mandatory skills methodology — TDD, subagent-driven development, and review enforcement | ~306K |

### Autonomous iteration

| Technique | Description | Stars |
|-----------|-------------|-------|
| [Ralph](techniques/ralph.md) | Autonomous bash-loop methodology — tests as backpressure, git as memory, tool-agnostic | Community |

### Enterprise AI-native SDLC

| Technique | Description | Stars |
|-----------|-------------|-------|
| [HVE](techniques/hve.md) | Microsoft ISE's RPI workflow with constraint-based governance and a growing repository-level skills inventory | ~1.6K |

### Cross-cutting

| Technique | Description |
|-----------|-------------|
| [Context Engineering](techniques/context-engineering.md) | The practice of structuring project context via rules files across an 8-layer model |

### Skills and agent frameworks

These pages cover the infrastructure and libraries that support the techniques above. Superpowers is listed under skill-based development because it adds a mandatory workflow.

| Document | Description |
|----------|-------------|
| [State of the Skills Market](techniques/skills-ecosystem.md) | Market overview, taxonomy, and the shift toward versioned, managed skill packages |
| [Skill Libraries](techniques/skills-libraries.md) | `mattpocock/skills`, `addyosmani/agent-skills`, `anthropics/skills`, `vercel-labs/agent-skills`, and watchlist collections |
| [Orchestrating Modes](techniques/skills-orchestrating-modes.md) | `pstack/poteto-mode`, canonical-source and port-drift caveats |
| [Distribution and Governance](techniques/skills-management.md) | Agent Skills specification, marketplaces vs. vendored installs, provenance, permissions, and rollout guidance |
| [Choosing a Skills Approach](techniques/skills-choosing.md) | Decision guide across libraries, orchestrating modes, methodologies, and native runtimes |

---

The [Decision Guide](overview.md#4-decision-guide) provides a short selection table.

## Building the site

Install `requirements-docs.txt`, run `python scripts/build_docs.py`, then `mkdocs build --strict`.

Diagram sources live in `diagrams/` as standalone HTML files with inline SVG and CSS. A standalone Markdown link labeled `Diagram: ...` embeds that file's `<figure>` during staging; use `diagrams/name.html` from root pages or `../diagrams/name.html` from technique pages. The original Markdown remains readable outside MkDocs. Figures follow the site's light/dark theme and scroll locally on narrow screens.

Run `python -m unittest discover -s scripts -p 'test_*.py'` to check diagram embedding.
