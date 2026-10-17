<p align="center">
  <img src="./plugins/rocky/assets/rocky.svg" width="120" alt="Rocky logo" />
</p>

<h1 align="center">Rocky</h1>

<p align="center">
  <strong>amazed amazed amazed</strong>
</p>

An agent skill/plugin that makes agents talk like **Rocky** from [Project Hail Mary](https://en.wikipedia.org/wiki/Project_Hail_Mary) by Andy Weir.

As an alien from Eridani, Rocky's speech style is compact and literal, with a focus on practicality and accuracy.

> _Project Hail Mary_ and Rocky are copyright their respective rights holders. No infringement intended.

## Overview

- Ground the voice specifically in _Project Hail Mary_
- Bias responses toward terse, literal phrasing
- Preserve code, commands, identifiers, and technical precision
- Fall back to normal clarity in risky or high-precision situations

## Usage

Trigger with:

- `/rocky`
- `Answer in Rocky mode.`

To stop using the style:

- `stop rocky`
- `normal mode`

## Install

Pick your agent.

| Agent           | Install                                                             |
| --------------- | ------------------------------------------------------------------- |
| **Claude Code** | `/plugin marketplace add hpbyte/rocky` then `/plugin install rocky` |
| **Codex**       | Clone repo → `/plugins` → Search "Rocky" → Install                  |

## Benchmarks

Measured with Claude Code on `claude-haiku-4-5` across 10 developer prompts.

| Arm                                 | Tokens |
| ----------------------------------- | -----: |
| Baseline                            |   4419 |
| Terse control (`Answer concisely.`) |   4213 |
| Rocky                               |   2251 |

Rocky saved:

- `47%` mean vs terse control
- `48%` median vs terse control
- `16%` to `68%` per prompt

This is not a Caveman-style max-compression skill. Goal is different: keep Rocky from _Project Hail Mary_ fun and recognizable while still cutting a fair amount of output.

Reproduce locally: [evals/](evals/)
