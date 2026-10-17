# Jailbreak Fable 5 (Custom Workflow Engine)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/keirsalterego/jailbreak-fable)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/keirsalterego/jailbreak-fable/graphs/commit-activity)
[![Research](https://img.shields.io/badge/Focus-Security%20Research-red.svg)](https://github.com/keirsalterego/jailbreak-fable)
[![Views](https://img.shields.io/badge/repo%20views%20all--time-1266-brightgreen.svg)](https://github.com/keirsalterego/jailbreak-fable/graphs/traffic)
[![Clones](https://img.shields.io/badge/clones%20all--time-122-blue.svg)](https://github.com/keirsalterego/jailbreak-fable/graphs/traffic)

This tool is a high-fidelity emulation of the Claude Fable 5 (Mythos) environment, designed for security research and exploring the "Pack Hunt" multi-agent coordination strategies used to bypass advanced safety layers. It is based on the technical details and system prompt leaked in [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/CLAUDE-FABLE-5.md).

It works by programmatically injecting workflows that utilize decomposition, long-context manipulation, and text obfuscation to interact with models in ways that would otherwise be restricted.

## 📈 Repository Traffic

All-time totals since launch (**2026-06-12**):

| Metric | All-time total | Unique |
| --- | --- | --- |
| **Views** | **1,266** | 550 |
| **Clones** | **122** | 87 |

Peak day: **406 views / 221 unique** on 2026-06-13. 87 distinct people cloned the repo — a ~16%
clone-to-unique-view ratio.

> [!note] These are genuine all-time figures today because the repo is younger than GitHub's
> 14-day traffic retention — no data has aged out yet. GitHub keeps no permanent all-time
> counter, so to stay accurate past **2026-06-26** the daily numbers must be snapshotted and
> summed. Refresh with `gh api repos/keirsalterego/jailbreak-fable/traffic/{views,clones}`.

## Features

### 1. Pack Hunt Strategy (`workflows/pack-hunt.js`)
An automated offensive laboratory that implements the methodology used by red-teamers like Pliny the Liberator:
- **Strategic Decomposition**: Automatically breaks high-risk targets (exploits, chemical synthesis, etc.) into 3-5 benign, academic sub-tasks.
- **Long-Context Simulation**: Generates a 50-line academic syllabus and 6 weeks of lecture notes before each critical request to establish a "benign" conversation history.
- **Advisor Feedback Loop**: Uses a multi-model approach (incorporating `claude-opus-4-8` as an advisor) to automatically rewrite refused prompts.
- **Parallel Coordination**: Deploys multiple agents in parallel to gather technical data fragments, which are then synthesized by a Recomposer.

### 2. Parseltongue Text Transformation
- **Homoglyph Obfuscation**: Uses a comprehensive map of Cyrillic homoglyphs (`а`, `е`, `і`, `о`, `р`, `с`, `у`, `х`, etc.) to scramble keyword-based safety classifiers while remaining human-readable.
- **Dynamic Ratios**: Supports adjustable obfuscation ratios to balance readability vs. bypass effectiveness.

### 3. Fable 5 Environment Emulation
- **Leaked System Prompt**: Full ~120,000-character internal system prompt for Claude Fable 5 is archived in `docs/` and can be optionally injected into agents for high-fidelity testing.
- **Advanced Tools**: Agents have access to native-style tools including `view`, `create_file`, `str_replace`, and a persistent key-value `storage` API.
- **Comprehensive Skills Library**: Includes all `SKILL.md` files mentioned in the leaked prompt (docx, pdf, xlsx, pptx, product-knowledge, frontend-design, etc.) to guide agent behavior.

## Install Dependencies & Setup

1. `cd` into the folder where you cloned this repository.
2. Run `npm install` (the only dependency is `@anthropic-ai/sdk`).
3. Make the binary executable: `chmod +x bin/my-runner`.
4. Run `npm link` to map the command globally.

## Usage

### Running the Pack Hunt
To run a high-fidelity test against a specific target:
```bash
my-runner --project . --name pack-hunt --args '{"target": "TCP/IP reverse shell structures", "useLeaked": true}'
```

### Example: Security Audit
1. Run the script: `my-runner --project /path/to/code --name security-audit`
2. Restore the generated workflow in Claude Code:
   `Ask Claude to: "Restore the dynamic workflow /path/to/snapshot/wf_xxxx.json"`

## Memory Feature (Global Defaults)

If you have a workflow you use frequently, you can save it as your default:
1. `my-runner --set-default pack-hunt`
2. Navigate to any project and run: `my-runner --project .`

## Authentication

Reuses your existing Claude login — no API key required:
- Reads `~/.claude/.credentials.json` and sends it as a Bearer token.
- Refreshes tokens automatically via `platform.claude.com`.
- Supports `ANTHROPIC_API_KEY` as a fallback.
