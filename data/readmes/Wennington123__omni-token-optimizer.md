<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" alt="omni-token-optimizer" width="220">
  </picture>
</p>

# Omni-Token Optimizer Suite

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-1a7f37?style=flat-square"></a>
  <img alt="Release" src="https://img.shields.io/github/v/release/Wennington123/omni-token-optimizer?style=flat-square&color=1a7f37&v=2">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8%2B-1a7f37?style=flat-square&logo=python&logoColor=white">
  <a href="https://ko-fi.com/wenningtondaquino"><img alt="Ko-fi" src="https://img.shields.io/badge/Ko--fi-Support-FF5E5B?style=flat-square&logo=kofi&logoColor=white"></a>
  <a href="#installation--integration-guide"><img alt="Install" src="https://img.shields.io/badge/install-curl_%7C_bash-3fb950?style=flat-square&logo=gnu-bash&logoColor=white"></a>
</p>

A universal, high-performance suite for **strict LLM token optimization**, built for both **software development** and **general-purpose work** (research, writing, data analysis and workflow automation).

The repo merges the philosophy of 3 reference projects (**Caveman**, **Punisher Mode** and **Ponytail**) with the empirical evidence and algorithms of **6 cutting-edge scientific papers** on context compression and agent reasoning.

## Quick Start

```bash
curl -fsSL https://raw.githubusercontent.com/Wennington123/omni-token-optimizer/main/install.sh | bash
```

Restart your agent session — the skill loads by itself. Prefer to delegate? Paste the [ready-to-use prompt block](#2-paste-into-your-ai-agent-claude-code-cursor-command-code-etc) into your agent.

![Demo in OpenCode](assets/demo-opencode.gif)

*A real OpenCode session: one-line install, `seq 1 3000` going through the local filter, and the resulting context.*

---

## Table of Contents
1. [Overview & Philosophy](#overview--philosophy)
2. [Architecture (Hooks + Skills)](#architecture-hooks--skills)
3. [Theoretical Background & References](#theoretical-background--references)
4. [Visual Dashboard & Performance Charts](#visual-dashboard--performance-charts)
5. [Mathematical Modeling & Activation ROI](#mathematical-modeling--activation-roi)
6. [Numeric Savings Matrix by Layer](#3-numeric-example-in-a-typical-15-turn-session)
7. [File Structure](#file-structure)
8. [Installation & Integration Guide](#installation--integration-guide)
9. [TODO & Roadmap](#todo--roadmap)
10. [License & Contributing](#license--contributing)

---

## Overview & Philosophy

As AI agents take on long-horizon tasks, **uncontrolled context growth** drives up inference cost, increases latency and degrades the model's attention.

**Omni-Token Optimizer** works on two complementary fronts:
1. **Zero-Token Local Middleware (Hooks)**: filters and truncates raw tool output (terminal, CSVs, JSON responses) on the local machine before the data reaches the model API. Execution cost = **0 tokens**.
2. **Behavioral System Prompts (Skills)**: shapes the model's behavior to produce ultra-concise answers, apply surgical *diffs* to code, adopt role framing (*Responsibility Tuning*) and keep a structured state memory (`VARS`, `TODO`, `GUARDRAILS`).

---

## Architecture (Hooks + Skills)

![How it works](assets/arch-flow.gif)

<details>
<summary><b>Text diagram (for screen readers and copy/paste)</b></summary>

```text
[User request / Tool command]
                      │
                      ▼
 ┌──────────────────────────────────────────────────────────────┐
 │ LAYER 1: LOCAL HOOKS (Python / Local CPU - COST: 0 TOKENS)   │
 │  • observation_trimmer.py: Truncates logs/CSVs (CoACT/Cave.) │
 │  • context_monitor.py: Watches the session token ceiling     │
 └────────────────────────────┬─────────────────────────────────┘
                              │ (Sends the filtered observation)
                              ▼
 ┌──────────────────────────────────────────────────────────────┐
 │ LAYER 2: MASTER SKILL & SUBSKILLS (Prompt / LLM Reasoning)   │
 │  • SKILL.md (Universal Orchestrator)                         │
 │  • subskills/01-terse-communication.md (Caveman + Punisher)  │
 │  • subskills/02-lazy-execution.md (Ponytail + Refactoring)   │
 │  • subskills/03-observation-trimmer.md (TRC + CoACT Rules)   │
 │  • subskills/04-state-compactor.md (ACON + TRACE Checkpoint) │
 │  • subskills/05-prompt-budgeting.md (LLMLingua Allocation)   │
 └──────────────────────────────────────────────────────────────┘
```

</details>

| Subskill | Focus | Basis |
|---|---|---|
| [01 — Terse Communication](subskills/01-terse-communication.md) | Dry answers, zero ceremony | Caveman + Punisher |
| [02 — Lazy Execution](subskills/02-lazy-execution.md) | Smallest diff that works, YAGNI | Ponytail |
| [03 — Observation Trimmer](subskills/03-observation-trimmer.md) | Cutting logs and API outputs | CoACT + TRC |
| [04 — State Compactor](subskills/04-state-compactor.md) | Structured state memory | ACON + TRACE |
| [05 — Prompt Budgeting](subskills/05-prompt-budgeting.md) | Initial context budget | LLMLingua |

---

## Theoretical Background & References

The repo is built strictly on 9 sources of knowledge:

<details>
<summary><b>3 repositories + 6 scientific papers — click to expand</b></summary>

### Open-Source Repositories

1. **JuliusBrussee/caveman** — *"Why use many token when few token do trick."*
   - **Repository**: GitHub JuliusBrussee/caveman
   - **Contribution**: Ultra-concise communication style (*Caveman Voice*) and local tool-output compression proxies. Cuts CSV and log returns by up to **98.9%**.
2. **Wennington123/punisher-mode** — *High-autonomy, low-friction operational mode for Command Code.*
   - **Repository**: GitHub Wennington123/punisher-mode
   - **Contribution**: Autonomous operating mode. Removes courtesy preambles ("Sure, I'll help...") and unnecessary confirmation *loops*, reducing latency and consumption in multi-turn conversations.
3. **DietrichGebert/ponytail** — *Makes your AI agent think like the laziest senior dev in the room.*
   - **Repository**: GitHub DietrichGebert/ponytail
   - **Contribution**: YAGNI (*You Aren't Gonna Need It*) philosophy. Forces changes through short patches/diffs instead of re-emitting whole files, cutting **token consumption by 45%** and **written code by 53%**.

### Empirical Scientific Papers

4. **Code Smells & Chain of Thought Token Consumption** (2025)
   - **Citation**: *Investigating Token Efficiency in Automated Software Engineering via Chain of Thought Reasoning.* (arXiv:2504.15989)
   - **Contribution**: Empirical proof that polluted code (*code smells*) inflate the model's CoT reasoning steps. Prior refactoring and role framing (*Responsibility Tuning*) reduce tokens per complexity unit from `0.1015` to `0.0576` (**49.7% cut in CoT**).
5. **CoACT: Observation Compression via Next-Action Preservation** (2026)
   - **Citation**: *CoACT: Frame-guided Observation Compression for Long-Horizon Agent Workflows.* (arXiv:2607.02911)
   - **Contribution**: Observation compression algorithm based on next-action preservation. Cuts tool output tokens by **55.9%** without hurting the success rate (*PASS@1*).
6. **Tool-Result Clearing (TRC) & Context Compression Policy** (2026)
   - **Citation**: *Context Compression Tradeoffs in Long-Horizon AI Agent Workflows.* (arXiv:2609.32961)
   - **Contribution**: Shows that replacing old tool results with placeholders (`[output cleared]`) preserves *KV-cache reuse* and lowers accumulated cost to **0.57x of the baseline**.
7. **TRACE: Boundary-Local Execution Verifier** (2026)
   - **Citation**: *TRACE: Recurrent Context Compression with Boundary Execution Verification.* (arXiv:2608.06503)
   - **Contribution**: Prevents loss of local execution state inside long summaries. Eliminates repetitive re-exploration *loops* and cuts peak tokens by **31% to 54%**.
8. **ACON: Agent Context Optimization** (2025)
   - **Citation**: *Agent Context Optimization via Contrastive Task Feedback & Compressor Distillation.* (arXiv:2510.00615)
   - **Contribution**: Structures context into state tables (`VARS`, `TODO`, `GUARDRAILS`) and distills lightweight compressor models (99% cheaper).
9. **LLMLingua: Compressing Prompts for Accelerated Inference** (EMNLP 2023)
   - **Citation**: *LLMLingua: Compressing Prompts for Accelerated Inference via Small Language Models.* (arXiv:2023.emnlp-main.825)
   - **Contribution**: Entropy-based budget allocation. Preserves 100% of the core instruction and compresses redundant *few-shot* demonstrations by up to **5x**.

</details>

---

## Visual Dashboard & Performance Charts

### Chart 1: Percentage Token Savings per Optimization Layer
![Percentage Token Reduction](assets/chart_token_savings.png)

### Chart 2: Accumulated Context Growth Across 15 Turns
![Context Growth](assets/chart_context_growth.png)

---

## Mathematical Modeling & Activation ROI

### 1. Activation Cost Adjusted for Prompt Caching
When the Master Skill and its Subskills are loaded into the system prompt ($N_{skill} \approx 1{,}200 \text{ tokens}$), the accumulated cost over a session of $T$ turns with *Prompt Caching* discount ($d_{cache} \approx 0.90$) is:

$$C_{activation} = N_{skill} + (T - 1) \times N_{skill} \times (1 - d_{cache})$$

For a 15-turn session:
$$C_{activation} = 1{,}200 + (14 \times 1{,}200 \times 0.10) = 2{,}880 \text{ input tokens.}$$

### 2. Net Savings Equation
$$\Delta \text{Tokens}_{net} = \Delta \text{Output} + \Delta \text{Obs} + \Delta \text{CoT} + \Delta \text{State} - C_{activation}$$

### 3. Numeric Example in a Typical 15-Turn Session

| Metric / Layer | Without optimization | With Omni-Token Optimizer | Net savings |
| :--- | :---: | :---: | :---: |
| **Response Tokens (Output)** | 6,000 (400/turn) | 1,200 (80/turn) | **-4,800 tokens** (~4x more valuable) |
| **Tools / Observations** | 60,000 (5 calls) | 7,500 (CoACT/TRC/Hook) | **-52,500 tokens** |
| **History Accumulation (Peak)** | 22,600 tokens | 7,200 tokens (ACON/TRACE) | **-15,400 tokens** |
| **Skill Activation Cost** | 0 tokens | 2,880 tokens | +2,880 tokens |
| **SESSION TOTAL** | **140,000 tokens** | **58,000 tokens** | **-82,000 tokens (-58.5%)** |

> These numbers are a **projection** composed from the per-layer figures in CoACT/TRC, not a controlled benchmark of this repo. A same-model A/B test with pass rate and retry cost is tracked in the [TODO & Roadmap](#todo--roadmap).

**Return Factor (ROI)**: for every 1 token spent keeping the suite active, the session saves **28.4 API tokens**.

---

## File Structure

```text
omni-token-optimizer/
├── SKILL.md                          # Master Skill (universal orchestrator)
├── AGENTS.md                         # Lean behavioral rules for agent files
├── README.md                         # Full docs, theory and empirical basis
├── install.sh                        # One-line installer (curl | bash)
├── assets/
│   ├── logo-light.svg                # Logo (light theme)
│   ├── logo-dark.svg                 # Logo (dark theme)
│   ├── arch-flow.gif                 # Animated architecture diagram
│   ├── demo-opencode.gif             # Real demo: install + trim in OpenCode
│   ├── chart_token_savings.png       # Per-layer savings chart
│   └── chart_context_growth.png      # Context growth curve chart
├── subskills/
│   ├── 01-terse-communication.md     # Terse style and autonomy (Caveman + Punisher)
│   ├── 02-lazy-execution.md          # Lean development and roles (Ponytail + Refactoring)
│   ├── 03-observation-trimmer.md     # Observation trimming rules (CoACT + TRC)
│   ├── 04-state-compactor.md         # Structured state memory (ACON + TRACE)
│   └── 05-prompt-budgeting.md        # Prompt budget allocation (LLMLingua)
├── hooks/
│   ├── observation_trimmer.py        # Local Python hook (zero tokens) to truncate logs/APIs
│   └── context_monitor.py            # Local Python hook (zero tokens) to watch the context ceiling
└── plugins/
    └── opencode/
        ├── index.ts                  # OpenCode v2 plugin: wires the hooks through the plugin API
        └── trim.ts                   # Pure trim/token-estimation logic (testable)
```

---

## Installation & Integration Guide

### 1. One-line install (Linux/macOS)

```bash
curl -fsSL https://raw.githubusercontent.com/Wennington123/omni-token-optimizer/main/install.sh | bash
```

The script auto-detects your agent's skills folder (`~/.commandcode/skills`, `~/.claude/skills` or `~/.config/opencode/skills`), installs the skill + subskills + hooks, copies the hooks to `~/.commandcode/hooks/` if it exists and prints the activation snippet. If `~/.config/opencode/` exists, it also installs the skill into `~/.config/opencode/skills/` and the hook plugin into `~/.config/opencode/plugins/` — even when the detected root is a different one. Options: `--dir DIR` (alternative skills root) and `--uninstall`.

Restart the agent session and the skill loads automatically.

### 2. Paste into your AI agent (Claude Code, Cursor, Command Code, etc.)

Copy the block below, paste it into your agent and ask it to run:

```text
Install and activate the omni-token-optimizer skill from the repo
https://github.com/Wennington123/omni-token-optimizer

Steps:
1. Clone the repo (shallow) into a temporary directory.
2. Copy SKILL.md, AGENTS.md, subskills/ and hooks/ into your agent's
   skills folder, creating the omni-token-optimizer/ subdirectory (e.g.
   ~/.claude/skills/omni-token-optimizer/ — if ~/.commandcode/skills
   exists, use it).
3. chmod +x every hooks/*.py.
4. If ~/.commandcode/hooks exists, copy hooks/*.py there too.
5. List the installed files to confirm and explain how to activate the
   skill in a new session.
Do not modify any other file on my system.
```

### 3. Manual installation

```bash
git clone --depth 1 https://github.com/Wennington123/omni-token-optimizer.git
cp -r omni-token-optimizer ~/.claude/skills/omni-token-optimizer   # adjust to your agent
chmod +x ~/.claude/skills/omni-token-optimizer/hooks/*.py
```

### 4. Per-agent integration

- **Claude Code / Command Code**: the skill is auto-discovered from the skills folder; for `context_monitor.py` (which speaks the JSON hooks protocol and injects the subskill 04 compaction warning), use the tested config printed by `install.sh` — threshold adjustable via `OMNI_TOKEN_THRESHOLD`. `observation_trimmer.py` has **no** wiring in those agents: PreToolUse hooks cannot replace the output the model actually sees (they only inject extra context), so wiring it would increase tokens instead of reducing them — it exists for the case below.
- **OpenCode (v2)**: full support via skill + local plugin — see [OpenCode Integration](#5-opencode-integration-v2).
- **Cursor / VS Code Agent**: add the contents of `AGENTS.md` to your `.cursorrules` or `system_prompt.md`.
- **Custom Python agents**: wire `hooks/observation_trimmer.py` into your tool-return handler (where the output can be replaced before the API call) and `hooks/context_monitor.py` into your session loop.

### 5. OpenCode Integration (v2)

Tested on OpenCode **2.4.1**. The integration uses two native mechanisms: the auto-discovered skill and a server plugin (v2 plugin API). Unlike Claude Code/Command Code, in OpenCode `observation_trimmer` gets real wiring: the `tool.execute.after` hook replaces the output the model sees, so log trimming actually works.

#### Manual installation

```bash
git clone --depth 1 https://github.com/Wennington123/omni-token-optimizer.git
cd omni-token-optimizer

# 1. Global skill (auto-discovered)
mkdir -p ~/.config/opencode/skills/omni-token-optimizer
cp SKILL.md AGENTS.md ~/.config/opencode/skills/omni-token-optimizer/
cp -r subskills hooks ~/.config/opencode/skills/omni-token-optimizer/

# 2. Plugin (local hooks)
mkdir -p ~/.config/opencode/plugins
cp -r plugins/opencode ~/.config/opencode/plugins/omni-token-optimizer
```

In `~/.config/opencode/opencode.json` (OpenCode reloads skill and plugin on save, no restart needed):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "~/.config/opencode/skills/omni-token-optimizer/SKILL.md"
  ],
  "plugins": [
    "/home/YOUR_USER/.config/opencode/plugins/omni-token-optimizer"
  ]
}
```

- `instructions` keeps the Master Skill **always on** (equivalent to auto-load). Without it, the skill is still available on demand (mention `@omni-token-optimizer` in your prompt).
- Without the `plugins` key the skill still works, but the local hooks stay off.
- The plugin is also loaded from `.opencode/plugins/` (per project) if you prefer a local scope.

#### What the plugin does (0 LLM tokens)

| Hook | Subskill | Behavior |
| --- | --- | --- |
| `tool.execute.after` | 03 — Observation Trimmer | Truncates long `shell` output above **160 lines and 6,000 characters**: keeps the first 40 lines, error lines from the middle and the last 30, with a `[... omni-token-optimizer: N lines / M chars trimmed ...]` marker. Never touches results carrying attachments (images/PDFs). |
| `session.context` | 04 — State Compactor | Estimates the history (~4 chars/token) and, above the threshold, injects the `[TOKEN_WARNING]` notice into the system prompt — **once**, repeating only if the context grows ≥25% or after 2 min. |

#### Options

Through `options` on the plugin entry in `opencode.json`, or environment variables (fallback):

```jsonc
"plugins": [
  {
    "package": "/home/YOUR_USER/.config/opencode/plugins/omni-token-optimizer",
    "options": { "contextThreshold": 120000, "debug": true }
  }
]
```

| Option | Env | Default | Description |
| --- | --- | --- | --- |
| `contextThreshold` | `OMNI_TOKEN_THRESHOLD` | `120000` | Token threshold for the compaction notice |
| `contextRewarnRatio` | — | `1.25` | Re-warn once the context grows by this fraction since the last notice |
| `contextRewarnMs` | — | `120000` | Minimum window (ms) between notices |
| `trimTools` | `OMNI_TRIM_TOOLS` | `"shell"` | Tools whose output may be truncated (comma-separated list) |
| `trimMaxChars` | `OMNI_TRIM_MAX_CHARS` | `6000` | Character trigger for trimming |
| `trimMaxLines` | `OMNI_TRIM_MAX_LINES` | `160` | Line trigger for trimming |
| `debug` | `OMNI_DEBUG=1` | `false` | Logs estimates and trims to the server stdout |

#### Verification

Save `opencode.json` and, in an agent session, run `seq 1 3000`: above the triggers the output becomes head + trim marker + tail. To check the context monitor, lower the threshold (`"contextThreshold": 100`) and watch the `[TOKEN_WARNING]` notice enter the system prompt on the next call.

#### Expected logs (not a bug)

The server log shows `msg="loading plugin"` **four times** at boot, always in two pairs: the global plugin is resolved in two locations (global and project) and re-resolved on the `config.updated` event that merges the project config. `PluginSupervisor` deduplicates by `id` and caches the module by `revision`, so `setup` runs **once** and each hook fires **once** per event — verified with a probe plugin: 1 `SETUP`, 1 `tool.execute.after` per call and 1 `[TOKEN_WARNING]` per request. Cost of the extra lines: a few ms, zero tokens.

Saving `index.ts` or `trim.ts` makes the watcher dispose the previous instance before creating the new one — hot reload without restart and without handler accumulation.

### 6. Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/Wennington123/omni-token-optimizer/main/install.sh | bash -s -- --uninstall
```

In OpenCode, also remove the `instructions`/`plugins` entries from `~/.config/opencode/opencode.json` (the script removes the skill and the plugin, but does not edit that file).

---

## TODO & Roadmap

- [ ] **Controlled A/B benchmark of the savings** — the **-58.5%** in [Mathematical Modeling](#mathematical-modeling--activation-roi) is a **projection** from the per-layer CoACT/TRC figures, not our own measurement. Still to measure: same model, same tasks (fixed and versioned in the repo), with and without skill + plugin, reporting (a) input/output tokens, (b) success rate (pass@1) and (c) **retry cost** — how many times the agent re-runs a command whose output was trimmed. Publish the harness and results together.
- [ ] **Instrument retries in the plugin** — count re-runs after a trim, to detect over-compression instead of assuming it does not happen.

---

## License & Contributing

This project is distributed under the **MIT** license. Feel free to contribute new hooks or empirical improvements via Pull Requests!

Enjoying it? Buy me a coffee: [ko-fi.com/wenningtondaquino](https://ko-fi.com/wenningtondaquino) ☕
