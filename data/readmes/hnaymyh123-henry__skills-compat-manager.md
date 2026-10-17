<p align="center">
  <img src="docs/architecture.svg" alt="Skills Compat Manager" width="640"/>
</p>

<h1 align="center">Skills Compat Manager</h1>

<p align="center">
  <strong>Stop your AI agent from failing halfway through a skill.</strong><br/>
  One library for all your agent skills — with a pre-flight check built in.
</p>

<p align="center">
  <a href="#quick-start"><img src="https://img.shields.io/badge/Get_Started-2_min-blue?style=for-the-badge" alt="Quick Start"/></a>
  <img src="https://img.shields.io/badge/MCP-native-orange?style=for-the-badge" alt="MCP native"/>
  <img src="https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge" alt="Python 3.11+"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="MIT License"/>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#how-it-works">How It Works</a> ·
  <a href="#cli-reference">CLI</a> ·
  <a href="#mcp-server">MCP Server</a> ·
  <a href="README.zh-CN.md">中文文档</a>
</p>

---

## Why You'll Want This

You've built (or downloaded) a bunch of AI agent skills. They work on your machine — until they don't.

> *"It worked in Claude Code but Cursor can't run it."*
> *"The agent started the task, then died on `ModuleNotFoundError: pandas`."*
> *"I set `OPENAI_API_KEY` locally but the agent still returned an empty string."*

**Skills Compat Manager fixes this in two moves:**

🗂️ **One library, every agent.** Drop your skills into a single folder. Claude Code, Cursor, Codex CLI, OpenCode — they all read from the same place via MCP. No more copy-pasting skills across tool configs.

🛡️ **Pre-flight check before execution.** Every time an agent loads a skill, we scan your environment against the skill's declared dependencies (packages · CLI tools · env vars · platform capabilities) and inject a **hard compatibility protocol** at the top. Missing `pandas`? The agent stops and asks *before* burning 10k tokens.

Think of it as **`package.json` + a lockfile checker** — but for AI agent skills.

---

## See It In Action

```
Agent: loading skill "pdf-tools" via MCP...

⚠ COMPATIBILITY DELTA — pdf-tools @ claude_code
Status: BLOCKED

Code Dependencies:
  - pandas: missing → pip install pandas
  - pypdf: available (4.0.1)

External Services:
  - OPENAI_API_KEY: missing

─── AGENT PROTOCOL ───
If Status is BLOCKED:
  1. DO NOT execute the skill body below.
  2. Report the missing dependencies to the user, verbatim.
  3. Ask the user how to proceed.

Agent (to you): Before I run pdf-tools, I need two things installed:
  1. pandas (pip install pandas)
  2. OPENAI_API_KEY environment variable
How would you like to proceed?
```

**The agent knows what's missing before it writes a single line of code.**

<p align="center">
  <img src="docs/screenshots/ph-scan.png" alt="skills-compat scan output" width="860"/>
</p>

---

## What This Tool Does — and Doesn't

**Does**
- Detects presence of Python packages, CLI binaries, environment variables, and declared platform capabilities
- Surfaces missing deps to the agent *before* skill execution via a structured Delta
- Provides a standardized, agent-readable compatibility protocol (OK / DEGRADED / BLOCKED)
- Generates `COMPAT.yaml` via AI inference or static rules

**Doesn't (yet)**
- Validate package versions unless explicitly declared in `COMPAT.yaml`
- Verify API keys are valid, active, or have quota remaining
- Runtime-test platform capabilities — it trusts the platform's declared caps
- Prevent a non-compliant agent from ignoring the compatibility block

This is an **advisory layer with a hard protocol**, not a sandbox.

---

## The Problem, In Detail

AI agent "skills" are reusable instruction files (`SKILL.md`) that tell an agent how to perform a task — parse a PDF, manage an Obsidian vault, generate a frontend design.

A skill can silently depend on things that aren't always there:

| Dimension | Example | What goes wrong |
|---|---|---|
| Python packages | `pandas`, `python-docx` | `ModuleNotFoundError` mid-task |
| CLI tools | `pdftotext`, `ffmpeg` | Agent generates a command that doesn't exist |
| Env variables | `VAULT_PATH`, `OPENAI_API_KEY` | Silent empty-string fallback, corrupted output |
| Platform capabilities | `bash`, `web_search` | Agent tries to use a tool the platform doesn't have |

Without a pre-flight check, the agent loads the skill, starts working, and fails halfway through — wasting tokens, time, and user trust.

---

## The Solution

Skills Compat Manager scans your skills **before** the agent runs them, computes a structured **Delta** (gap analysis), and injects it into the skill content at load time.

```
┌─────────────────────────────────┐
│  Agent loads "pdf" skill via MCP │
└────────────────┬────────────────┘
                 ▼
   ┌─────────────────────────────┐
   │  Scanner checks COMPAT.yaml │
   │  against runtime environment │
   └────────────────┬────────────┘
                    ▼
   ┌─────────────────────────────────────────────┐
   │  ⚠ Compatibility Delta — pdf @ claude_code  │
   │                                              │
   │  Code Deps:                                  │
   │    ✓ pypdf ........ installed (4.0.1)        │
   │    ✗ camelot-py ... missing [optional]       │
   │      → pip install camelot-py                │
   │                                              │
   │  System Tools:                               │
   │    ✗ pdftotext .... missing [optional]       │
   │      → brew install poppler                  │
   │                                              │
   │  Status: DEGRADED                            │
   │  Proceed with caution — optional deps missing│
   └─────────────────────────────────────────────┘
                    ▼
   ┌─────────────────────────────┐
   │  Agent sees the Delta BEFORE │
   │  the skill content begins    │
   │  → adapts or warns the user  │
   └─────────────────────────────┘
```

The agent now **knows what's missing** before it writes a single line of code.

---

## Architecture

<p align="center">
  <img src="docs/architecture.svg" alt="Skills Compat Manager architecture" width="860"/>
</p>

---

## The Four-Dimensional Framework

Every skill's dependencies are classified into four dimensions:

<p align="center">
  <img src="docs/fourdim.svg" alt="COMPAT.yaml four dimensions" width="720"/>
</p>

<p align="center">
  <img src="docs/screenshots/ph-compat.png" alt="COMPAT.yaml example" width="860"/>
</p>

Example `COMPAT.yaml`:

```yaml
schema_version: "2.0"
requires:
  code_deps:
    - name: pandas
      description: "Data manipulation and analysis"
      required: true
    - name: seaborn
      description: "Statistical visualization"
      required: false

  system_tools:
    - name: pdftotext
      required: false

  external_services:
    - name: VAULT_PATH
      description: "Obsidian vault location"
      required: true

  runtime_capabilities:
    - name: bash
      required: true
    - name: file_write
      required: true
```

> Don't want to write this by hand? Run `skills-compat infer <skill>` and AI generates it from your SKILL.md.

---

## Quick Start

### Install

```bash
pip install git+https://github.com/hnaymyh123-henry/skills-compat-manager.git

# Optional: enable AI-powered COMPAT.yaml inference
pip install "git+https://github.com/hnaymyh123-henry/skills-compat-manager.git#egg=skills-compat[ai]"
```

### Setup

```bash
# Auto-detect installed platforms (Claude Code, Cursor, etc.)
# and configure MCP server entries
skills-compat setup --skill-library ~/my-skills
```

### Scan

```bash
# Scan a single skill
skills-compat scan pdf

# Scan all skills in your library
skills-compat scan

# JSON output for automation
skills-compat scan --json
```

### Infer COMPAT.yaml with AI

```bash
# Let AI analyze your SKILL.md and generate COMPAT.yaml
skills-compat infer my-skill

# Infer for all skills that don't have COMPAT.yaml yet
skills-compat infer --all

# Choose AI provider: openai, claude, or rules (no API key needed)
skills-compat infer my-skill --provider rules
```

---

## How It Works

<p align="center">
  <img src="docs/screenshots/ph-howitworks.png" alt="How It Works — 4 steps" width="860"/>
</p>

### For AI Agents (MCP Server)

The MCP server is the primary runtime interface. When an agent calls `get_skill`:

1. **Reads** the original `SKILL.md` content
2. **Scans** the runtime environment (installed packages, CLI tools, env vars)
3. **Computes** a Delta against the platform's capability profile
4. **Injects** the Delta block at the top of the skill content
5. **Returns** the augmented content to the agent

The agent sees the compatibility status **before** the skill instructions begin, and can decide how to proceed.

### For Developers (CLI)

The CLI is your setup and diagnostic tool:

```
skills-compat setup     →  Auto-detect platforms, configure MCP
skills-compat status    →  Overview of library health
skills-compat scan      →  Run Delta analysis, see what's missing
skills-compat verify    →  CI-friendly status check (exit code = status)
skills-compat infer     →  AI-generate COMPAT.yaml from SKILL.md
skills-compat fix       →  Interactive fix: suggest → run → re-verify
skills-compat serve     →  Start the MCP server manually
skills-compat config    →  View/update configuration
```

`verify` returns exit code `0` (OK), `1` (DEGRADED), `2` (BLOCKED), `3` (UNSCANNED), or `4` (error) — drop it into CI with `skills-compat verify pdf && deploy`.

`fix` closes the loop: for every missing dep it asks the LLM for 2–3 fix paths (each tagged `SAFE`/`MANUAL` + `agent_or_user`/`user_only`), runs the SAFE ones through a sandbox allowlist, re-scans, and prints the status transition (e.g. `BLOCKED → DEGRADED`). Use `--auto` for CI, `--yes` to skip confirmation prompts.

---

## MCP Server

### Configuration

Add to your MCP client configuration:

**Claude Code** (`~/.claude/settings.json`):
```json
{
  "mcpServers": {
    "skills-compat": {
      "command": "skills-compat",
      "args": ["serve"],
      "env": {
        "SKILL_LIBRARY": "/path/to/your/skills"
      }
    }
  }
}
```

**Cursor** (`.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "skills-compat": {
      "command": "skills-compat",
      "args": ["serve"],
      "env": {
        "SKILL_LIBRARY": "/path/to/your/skills"
      }
    }
  }
}
```

Or let the CLI do it automatically:
```bash
skills-compat setup --skill-library /path/to/your/skills
```

### Available Tools

| Tool | Description |
|---|---|
| `list_skills` | List all skills in the library |
| `get_skill` | Load skill content with Delta block injected |
| `scan_skills` | Run compatibility scan across all skills |
| `get_skill_info` | Get metadata and COMPAT.yaml for a skill |
| `search_skills` | Search skills by keyword |
| `suggest_fix` | Get AI-powered fix suggestions (each path tagged with actor + safety) |
| `apply_fix` | Execute a SAFE fix command through a sandbox allowlist, then re-scan |
| `refresh_runtime` | Re-detect the runtime environment |

---

## Supported Platforms

<p align="center">
  <img src="docs/screenshots/ph-platforms.png" alt="Supported platforms" width="860"/>
</p>

| Platform | Capabilities | Confidence | Auto-detected |
|---|---|---|---|
| Claude Code | `bash` `file_read` `file_write` `web_search` `web_fetch` `python_runtime` `lsp` `notebook` `subagent` `monitor` | verified | ✓ |
| Cursor | `bash` `file_read` `file_write` `web_search` | partial | ✓ |
| Codex CLI | `bash` `file_read` `file_write` `python_runtime` | verified | ✓ |
| OpenCode | `bash` `file_read` `file_write` `web_search` `web_fetch` `python_runtime` `lsp` | verified | ✓ |
| Claude Desktop | `file_read` `file_write` | partial | ✓ |

Confidence levels reflect how well the capability list has been verified against official documentation (`verified` = sourced from official docs, `partial` = docs incomplete or inaccessible, `unverified` = best-effort estimate). See `data/platform_profiles.yaml` for sources and verification dates.

A few platform-specific notes worth knowing: Codex CLI has network blocked by default in all sandbox modes — there is no built-in `web_search`. Claude Desktop's native tool set is minimal; most capabilities (web, shell, full filesystem) come from user-installed MCP servers, not built-ins.

Platform detection happens automatically via the MCP handshake (`clientInfo.name`) — no manual configuration needed. **Adding a new platform** requires only editing `data/platform_profiles.yaml`. If your agent platform supports self-reporting via `capabilities.experimental["skills-compat:platform-tools"]` in the MCP `initialize` handshake, its capabilities are used directly and take priority over the static profile.

---

## AI Features

### Multi-Provider Inference

COMPAT.yaml inference supports three providers with automatic fallback:

```
OpenAI (gpt-4o) → Anthropic Claude → Rules-based (no API key)
```

The AI analyzes your SKILL.md content and produces a complete COMPAT.yaml with:
- **stdlib filtering** — Python standard library modules are automatically excluded
- **PyPI name resolution** — Import names are mapped to correct pip package names (`yaml` → `pyyaml`, `cv2` → `opencv-python`)
- **required/optional classification** — Each dependency is judged as required or optional based on its role in the skill

### Fix Suggestions

When the scanner finds a missing dependency, `suggest_fix` generates 2–3 actionable solution paths. Every path is classified on two axes so the agent knows exactly what it can do autonomously:

```
Path A: Install                     [SAFE · agent_or_user · low effort]
  → pip install camelot-py

Path B: Use alternative library    [MANUAL · user_only · medium effort]
  → Edit SKILL.md to use tabula-py instead

Path C: Mark as optional            [MANUAL · user_only · low effort]
  → Accept graceful degradation
```

- `SAFE` + `agent_or_user` → the agent may execute it via `apply_fix` (or `skills-compat fix --auto`), subject to the allowlist (`pip`/`npm`/`yarn`/`mkdir`/`touch`) and a hard denylist (`sudo`, `rm`, `|sh`, `>/etc`, `&&rm`, etc.).
- `MANUAL` or `user_only` → the agent surfaces the commands to the human, never runs them.

---

## Project Structure

```
skills-compat-manager/
├── app/
│   ├── cli.py                 # CLI entry point (9 commands)
│   ├── mcp_server.py          # MCP stdio server (8 tools)
│   ├── scanner.py             # Delta computation engine; reads COMPAT.yaml from central store
│   ├── ai_engine.py           # AI inference (OpenAI / Claude / rules)
│   ├── models.py              # Pydantic data models
│   ├── config.py              # Settings & paths; loads platform profiles from data/
│   ├── runtime_detector.py    # OS / pip / CLI / env detection
│   ├── skill_manager.py       # Skill discovery; writes COMPAT.yaml to central store
│   ├── platform_resolver.py   # MCP handshake resolution + experimental capability hook
│   ├── platform_detector.py   # Installed platform detection
│   ├── tool_registry.py       # MCP tool registry & platform capability lookup
│   └── mcp_configurator.py    # Auto-configure MCP entries for detected platforms
├── data/
│   └── platform_profiles.yaml # Platform capability definitions — edit to add/update platforms
└── tests/
    ├── test_scanner.py
    ├── test_mcp_server.py
    ├── test_ai_engine.py
    └── test_cli.py
```