# SENAR — Supervised Engineering & Normative AI Regulation

![Version](https://img.shields.io/badge/version-1.5-blue)
![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green)

**An open standard for harness engineering — the discipline of the scaffolding around a coding agent.** SENAR norms what a gate must prevent, where it must act, and what its verdict must be about.

[senar.tech](https://senar.tech) · [Читать на русском](README.ru.md)

## What is SENAR

SENAR is a practical engineering standard for teams where AI agents write code alongside human engineers. It defines roles, ceremonies, quality gates, and metrics — not abstract principles, but concrete rules you can adopt today. SENAR scales from a solo developer with an AI assistant to enterprise teams with dozens of agents. It is vendor-neutral and works with any AI coding tool: Cursor, Claude Code, Copilot, Windsurf, or custom setups.

## Start Here

New to SENAR? Start with **SENAR Core** — 8 essential rules you can adopt in 5 minutes:

**[SENAR Core (English)](core/en/senar-core.md)** | **[SENAR Core (Russian)](core/ru/senar-core.md)**

Then read the [Quick Start Guide](guide/00-quickstart.md) for a hands-on walkthrough.

## PDF Downloads

The PDFs below are the current **released** build, v1.5, and match the Markdown in this repository.

- [SENAR v1.5 — Full Document, English (PDF)](docs/SENAR-v1.5-en.pdf) — Core + Standard + Guide + Reference
- [SENAR v1.5 — Full Document, Russian (PDF)](docs/SENAR-v1.5-ru.pdf) — Core + Standard + Guide + Reference

## Documentation

| Document | Description | Link |
|----------|-------------|------|
| **Standard v1.5** | Full specification: roles, rules, quality gates, metrics, conformance | [standard/](standard/README.md) |
| **Guide** | Practical guide: philosophy, adoption, walkthroughs (EN + RU) | [guide/](guide/README.md) |
| **Reference** | Reference materials: glossary, scaling ratios, governance, tooling | [reference/](reference/README.md) |
| **Core v1.5** | 8 rules quick start for individual developers | [core/](core/README.md) |

## Key Concepts

- **Context-over-Code** — AI effectiveness depends on context quality, not prompt tricks
- **FPSR (First Pass Success Rate)** — primary metric: percentage of tasks done right on first attempt
- **Quality Gates** — automated checkpoints (QG-0 before work, QG-2 before merge)
- **15 Rules** — concrete engineering rules, not abstract principles
- **3 Configurations defined by the Standard** — Foundation, Team, Enterprise — entered from SENAR Core, which is governed by its own document (S13.3)


## Reference Implementation: TAUSIK

**[TAUSIK](https://github.com/Kibertum/tausik-core)** (Task Agent Unified Supervision, Inspection & Knowledge) is the open-source framework that enforces SENAR rules automatically.

Quality gates that physically block agents from skipping steps — not recommendations, but enforcement.

- **Cross-IDE:** Claude Code, Cursor, Windsurf
- **15 automated checks:** pytest, ruff, tsc, eslint, cargo, go vet
- **33 structured skills:** /plan, /ship, /review, /audit, /debug
- **80 MCP tools** for programmatic project memory access
- **6 automatic metrics:** FPSR, DER, throughput, lead time
- **Zero core dependencies:** Python 3.11+ standard library only

```bash
git submodule add https://github.com/Kibertum/tausik-core .tausik-lib
python .tausik-lib/bootstrap/bootstrap.py --smart --init my-project
# restart IDE — done
```

## Who Is This For

- Engineering teams using AI coding assistants (Cursor, Claude Code, Copilot, etc.)
- CTOs and engineering leaders building AI-native development processes
- Organizations seeking a structured approach to human-AI collaboration
- Solo developers who want reliable AI-assisted workflows

## License

[CC BY-SA 4.0](LICENSE) — use freely with attribution.

**Authors:** Andrey Yumashev, Vadim Soglaev
