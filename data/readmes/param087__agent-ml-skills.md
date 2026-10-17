# agent-ml-skills

**Production-grade Machine Learning, Data Science & MLOps skills for AI coding agents.**

[![CI](https://github.com/param087/agent-ml-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/param087/agent-ml-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
![Skills](https://img.shields.io/badge/skills-15-success)
![Node](https://img.shields.io/badge/node-%3E%3D18-43853d)
![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

Coding agents are great generalists but make the same **ML mistakes over and over**: leaking preprocessing into cross-validation, scoring imbalanced data with accuracy, forgetting `model.eval()`, building RAG with dense-only retrieval. `agent-ml-skills` is a curated pack of **15 battle-tested skills** that teach your agent how an experienced ML engineer actually works — so it stops guessing.

Works with **Codex, Claude Code, Cursor, and OpenCode**.

---

## Quick start

Install all skills into your agent with one command — **no install, no dependencies**:

```bash
# Codex
npx agent-ml-skills install --target codex

# Claude Code
npx agent-ml-skills install --target claude

# Cursor
npx agent-ml-skills install --target cursor --scope project

# OpenCode
npx agent-ml-skills install --target opencode

# Everything, everywhere
npx agent-ml-skills install --target all
```

Browse what's inside first:

```bash
npx agent-ml-skills list
```

Then restart your agent (or start a new session) and it will pick the right skill up automatically when your task matches.

---

## What's a "skill"?

A skill is a single Markdown file with YAML frontmatter telling the agent **when** to use it and **how** to do the task well:

```markdown
---
name: sklearn-pipelines
description: Use when building scikit-learn models that must not leak preprocessing...
---

# scikit-learn Pipelines
...workflow, code patterns, pitfalls, hand-off...
```

Agents that support skills load the `description` up front and pull in the full body only when the task matches — so you get expert guidance **without bloating every prompt**.

---

## The skills

### Data prep & exploration
| Skill | Use when… |
|---|---|
| **exploratory-data-analysis** | Starting on a new dataset — profiling, distributions, correlations, leakage & viz. |
| **data-cleaning** | Handling missing values, duplicates, types, outliers — with train-only imputation. |
| **feature-engineering** | Encoding, scaling, datetime/text/aggregation features, leakage-safe target encoding. |
| **pandas-patterns** | Writing idiomatic, vectorized, memory-efficient pandas (no `SettingWithCopyWarning`). |
| **imbalanced-data** | The target is rare (fraud/churn/disease) — metrics, SMOTE, class weights, thresholds. |

### Modeling
| Skill | Use when… |
|---|---|
| **sklearn-pipelines** | Building scikit-learn models that must not leak preprocessing into CV. |
| **pytorch-training-loop** | Writing/reviewing a PyTorch loop — eval modes, AMP, checkpointing, devices. |
| **model-evaluation** | Choosing metrics, validating, calibration, confusion-matrix analysis. |
| **hyperparameter-tuning** | Optimizing params — random vs Optuna, leakage-safe CV, early stopping, budget. |

### LLMs & GenAI
| Skill | Use when… |
|---|---|
| **llm-finetuning** | Fine-tuning an LLM — full vs LoRA/QLoRA, data formatting, transformers/PEFT/TRL. |
| **rag-pipeline** | Building RAG — chunking, embeddings, hybrid + reranking retrieval, eval. |

### MLOps & reliability
| Skill | Use when… |
|---|---|
| **experiment-tracking** | Experiments need comparing/reproducing — MLflow/W&B, what to log, registry. |
| **reproducible-ml** | A result must be reproducible — seeds, env pinning, data versioning, CUDA determinism. |
| **ml-debugging** | A model won't learn, loss is NaN, or metrics look too good — a diagnosis decision tree. |
| **model-serving** | Deploying behind an API — FastAPI, safe artifact loading, batching, ONNX, monitoring. |

---

## Usage

```
npx agent-ml-skills <command> [options]

Commands
  list                       List available skills
  install                    Install skills into an agent

Options
  -t, --target <name>        codex | claude | opencode | cursor | all
      --scope <scope>        global (default) | project
      --skills <a,b,c>       comma-separated subset (default: all)
      --dir <path>           install into a custom directory (overrides target)
  -f, --force                overwrite existing skills
  -h, --help                 show this help
```

**Examples**

```bash
# Just the LLM skills, into the current project
npx agent-ml-skills install --target claude --skills rag-pipeline,llm-finetuning --scope project

# Into a custom agent directory
npx agent-ml-skills install --dir ./my-agent/skills

# Re-install and overwrite
npx agent-ml-skills install --target codex --force
```

### Where skills get installed

| Target | Global | Project |
|---|---|---|
| Codex | `~/.codex/skills` | `.codex/skills` |
| Claude Code | `~/.claude/skills` | `.claude/skills` |
| OpenCode | `~/.config/opencode/skills` | `.opencode/skills` |
| Cursor | — | `.cursor/rules` (flat `.md` rules) |

---

## Design principles

- **Leakage-safe by default.** Every data skill fits transforms on train only.
- **Concrete over abstract.** Real code patterns, not vague advice.
- **Pitfalls included.** Each skill ends with the mistakes agents actually make.
- **Composable.** Skills hand off to each other (EDA → cleaning → features → pipeline → eval → serving).
- **Zero-dependency installer.** Pure Node, nothing to install, nothing to trust.

---

## Contributing

New skills and improvements are very welcome — see **[CONTRIBUTING.md](./CONTRIBUTING.md)**. Every skill is validated in CI:

```bash
node scripts/validate-skills.mjs
```

Open a [skill request](https://github.com/param087/agent-ml-skills/issues/new?template=skill_request.md) if there's an ML workflow you want your agent to master.

---

## Author

Built by **[Param Bhavsar](https://github.com/param087)** — Google Summer of Code '19 @ TensorFlow, ex-HSBC. If this saves you a debugging session, a ⭐ helps others find it.

## License

[MIT](./LICENSE)
