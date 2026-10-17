<sub>🌐 English · <a href="README.zh.md">中文</a></sub>

# CC Harness Skills

> *"The parts that separate a fun demo from a stable toolchain: memory, compression, verification, routing, proactive jobs."*

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-6%20bundles-blueviolet)](#skill-pack)
[![skills.sh](https://skills.sh/b/LearnPrompt/cc-harness-skills)](https://skills.sh/LearnPrompt/cc-harness-skills)
[![Multi-Runtime](https://img.shields.io/badge/Runtime-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20OpenClaw-green)](#quick-start)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portable agent skills distilled from a publicly mirrored `CC` coding-agent codebase, then rewritten so they can be installed in `Claude Code`, `Codex`, and `OpenClaw` without depending on private runtime internals.

## Quick Start

One-line install (any skills-compatible agent):

```bash
# all six skills
npx skills add LearnPrompt/cc-harness-skills -g

# or a single skill
npx skills add LearnPrompt/cc-harness-skills -s verification-gate -g
```

Run the basic bundle checks first:

```bash
bash ./skills/check_all.sh
```

Or copy one skill into a host runtime manually:

```bash
mkdir -p ~/.claude/skills
cp -R ./skills/dream-memory ~/.claude/skills/
```

Then invoke it in `Claude Code`:

```text
Use /dream-memory to consolidate the memory directory before we continue.
```

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/dream-memory ~/.codex/skills/
```

Then invoke it in `Codex`:

```text
Use /dream-memory and consolidate recent memory files into one stable index.
```

```bash
mkdir -p ~/.openclaw/workspace/skills
cp -R ./skills/dream-memory ~/.openclaw/workspace/skills/
```

Then check it in `OpenClaw`:

```bash
openclaw skills info dream-memory
```

Publish to ClawHub after checks:

```bash
bash ./skills/publish_all.sh 0.1.0
```

This repo is not a source dump. It is a cleaned skill pack:

- prompts extracted into reusable templates
- host-agnostic helper scripts
- portable `SKILL.md` bundles
- release and smoke-test docs for public distribution

If you are building with coding agents, these are the parts that usually separate a fun demo from a stable toolchain:

- memory that stays useful instead of rotting
- compression that preserves user corrections
- verification that does not trust "done"
- multi-agent routing that does not pollute the main context
- proactive jobs with explicit limits

This repo packages those patterns into six installable skills.

## Why This Exists

Most agent repos share the same hard problems:

- how to keep memory useful without storing stale code facts
- how to compress long conversations without losing user corrections
- how to verify claimed completion instead of trusting it
- how to coordinate multiple agents without turning the main context into garbage
- how to add lightweight proactive behavior without building a dangerous daemon

The six skills in this repo package those patterns into download-ready bundles.

## Who This Is For

- builders who want better agent behavior without forking a full agent product
- teams using `Claude Code`, `Codex`, or `OpenClaw` and wanting a shared skill layer
- people studying `CC`-style harness design but needing something publishable and portable
- anyone who wants prompts plus scripts, not prompts alone

## Skill Pack

| Public name | Slug | What it does | Best hosts |
| --- | --- | --- | --- |
| CC Dream Memory | `dream-memory` | Consolidates logs, recent sessions, and topic memories into a short durable memory index. | Claude Code, Codex, OpenClaw |
| CC Memory Extractor | `memory-extractor` | Extracts durable `user`, `feedback`, `project`, and `reference` memories from recent turns. | Claude Code, Codex, OpenClaw |
| CC Verification Gate | `verification-gate` | Runs a read-only challenge pass after implementation to distinguish verified from merely claimed done. | Claude Code, Codex |
| CC Swarm Coordinator | `swarm-coordinator` | Splits large work into research, synthesis, implementation, and verification with bounded workers. | Claude Code, Codex, OpenClaw |
| CC Context Compressor | `structured-context-compressor` | Produces a nine-part continuation summary for long sessions and handoffs. | Claude Code, Codex, OpenClaw |
| CC Kairos Lite | `kairos-lite` | Adds lightweight proactive jobs with schedule, sleep, brief, and expiry rules. | Claude Code, OpenClaw |

Each bundle lives in [`skills/`](/Users/carl/Downloads/codegod/skills/README.md) and includes:

- `SKILL.md`
- `references/prompt-template.md`
- `references/source-notes.md`
- `scripts/...`
- `README.md`

## Start Here

If you only try three things, try these first:

1. install `dream-memory`
2. install `verification-gate`
3. install `structured-context-compressor`

That gives you one memory workflow, one quality gate, and one continuation artifact. It is the fastest way to feel whether this repo is useful.

## Release Docs

- Publisher guide: [`skills/README.md`](/Users/carl/Downloads/codegod/skills/README.md)
- Release order and copy: [`skills/RELEASE_PLAN.md`](/Users/carl/Downloads/codegod/skills/RELEASE_PLAN.md)
- Smoke-test report: [`skills/TEST_REPORT.md`](/Users/carl/Downloads/codegod/skills/TEST_REPORT.md)

## Naming

Recommended public GitHub repo name: `cc-harness-skills`

Good alternatives:

- `cc-agent-skills`
- `cc-harness-kit`
- `cc-portable-skills`

The public naming uses `CC` on purpose: it signals the origin of the ideas without hard-coding a full vendor product name into the repo identity.

## What Is Verified

Latest smoke-test status:

- `Claude Code`: six skills load successfully
- `OpenClaw`: six skills resolve as `Ready`
- `Codex`: bundle structure is verified; runtime smoke test is pending local auth

Full report: [`skills/TEST_REPORT.md`](/Users/carl/Downloads/codegod/skills/TEST_REPORT.md)

## Project Layout

```text
skills/
  dream-memory/
  memory-extractor/
  verification-gate/
  swarm-coordinator/
  structured-context-compressor/
  kairos-lite/
```

Internal working notes and non-publishable local experiments still live under `.codex/skills/`, but the public release surface for this project is the root `skills/` directory.

---

<div align="center">

**更多好用 Skill · More Skills** → [learnprompt.pro/skills](https://learnprompt.pro/skills/)

[鲁班·Skill打磨](https://github.com/LearnPrompt/luban-skill) · [庖丁·博主蒸馏](https://github.com/LearnPrompt/paoding-skill) · [蔡伦·对话造纸](https://github.com/LearnPrompt/cailun-skill) · [阿福·LLM Todo](https://github.com/LearnPrompt/afu-llm-todo) · [愚公·Loop工程](https://github.com/LearnPrompt/loop-engineering) · [搭子·结对开发](https://github.com/LearnPrompt/partner-skill) · [AI雷达·零API资讯](https://github.com/LearnPrompt/ai-news-radar)

[淘金小镇·ClawHub日榜](https://github.com/LearnPrompt/skillrush-town) · [Irasutoya·正文配图](https://github.com/LearnPrompt/carl-irasutoya-illustrations) · [Humanize PPT·演讲系统](https://github.com/LearnPrompt/humanize-ppt) · [CC Harness·六件套](https://github.com/LearnPrompt/cc-harness-skills) · [微信读书教练](https://github.com/LearnPrompt/carl-weread) · [X Article发布](https://github.com/LearnPrompt/x-article-publisher-skill)

<sub>**[LearnPrompt](https://github.com/LearnPrompt) 出品** · 公众号「卡尔的AI沃茨」 · [X @aiwarts](https://x.com/aiwarts)</sub>

</div>
