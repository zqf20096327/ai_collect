# Antigravity (AGY) Token-Optimized CLI & IDE Setup

A portable, token-disciplined configuration for **Google Antigravity (CLI, App, and IDE)** across **Windows, macOS, and Linux** featuring configurable Orchestrator Mode presets, pruned MCP tool schemas, Progressive Disclosure skills, Context Guardian auto-compact advisor, and a **Global Skill Router** backed by a categorized **21-skill library**.

## Setup Presets (Choose Your Token vs. Quality Combo)

Pick the profile that matches your task, model family (**Argon**, **Neon**, or **Carbon**), and credit budget (defined in `settings/presets.json`):

| Series | Preset | Flag / Alias | Planner Model | Executor Model | Context Guardian (Yellow / Red) | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Argon** | **Setup 1: Argon Balanced** | `--preset 1` / `balanced` / `argon-balanced` | `Gemini 4 Argon (Medium)` | `Gemini 4 Hydrogen (Medium)` | `75 / 120` steps (`85k / 135k` tokens) | Balanced Argon planning with token-efficient Hydrogen Medium execution |
| **Argon** | **Setup 2: Argon / Hydrogen Ultra Saver** | `--preset 2` / `ultra-saver` / `argon-saver` | `Gemini 4 Hydrogen (High)` | `Gemini 4 Hydrogen (Low)` | `50 / 85` steps (`60k / 95k` tokens) | Tight token/credit budgets, repetitive edits, quick scripts |
| **Argon** | **Setup 3: Argon Max Quality** | `--preset 3` / `max-quality` / `argon-max` | `Gemini 4 Argon (High)` | `Gemini 4 Hydrogen (High)` | `100 / 150` steps (`110k / 160k` tokens) | Complex system architecture, deep debugging, multi-service refactors |
| **Neon** | **Setup 4: Neon Balanced (Recommended / Default)** | `--preset 4` / `neon-balanced` / `neon` | `Gemini 4 Neon (High)` | `Gemini 4 Hydrogen (Medium)` | `75 / 120` steps (`85k / 135k` tokens) | Daily full-stack coding: best balance of Neon reasoning and token efficiency |
| **Neon** | **Setup 5: Neon Ultra Saver** | `--preset 5` / `neon-saver` / `neon-ultra-saver` | `Gemini 4 Neon (Medium)` | `Gemini 4 Hydrogen (Low)` | `55 / 90` steps (`65k / 100k` tokens) | Lightweight Neon planning with tighter compaction thresholds |
| **Neon** | **Setup 6: Neon Max Quality** | `--preset 6` / `neon-max` / `neon-max-quality` | `Gemini 4 Neon (XHigh)` | `Gemini 4 Hydrogen (XHigh)` | `100 / 150` steps (`110k / 160k` tokens) | Peak Neon reasoning depth for complex architecture and deep debugging |
| **Carbon** | **Setup 7: Carbon Balanced** | `--preset 7` / `carbon-balanced` / `carbon` | `Gemini 4 Carbon (Medium)` | `Gemini 4 Hydrogen (Medium)` | `75 / 120` steps (`85k / 135k` tokens) | Daily coding with Gemini 4 Carbon planner and Hydrogen Medium executor |
| **Carbon** | **Setup 8: Carbon Ultra Saver** | `--preset 8` / `carbon-saver` / `carbon-ultra-saver` | `Gemini 4 Carbon (Low)` | `Gemini 4 Hydrogen (Low)` | `55 / 90` steps (`65k / 100k` tokens) | Lightweight Carbon planning with early compaction reminders |
| **Carbon** | **Setup 9: Carbon Max Quality** | `--preset 9` / `carbon-max` / `carbon-max-quality` | `Gemini 4 Carbon (High)` | `Gemini 4 Hydrogen (High)` | `100 / 150` steps (`110k / 160k` tokens) | High-depth Carbon architecture and multi-module refactoring |

## Architecture Highlights

1. **Orchestrator Mode (Plan-Execute)**:
   - Separates planning and execution models according to your selected preset (`1`–`3` Argon, `4`–`6` Neon, or `7`–`9` Carbon), avoiding wasted tokens from trial-and-error loops.
2. **Zero Global MCP Context Bloat**:
   - Keeps global `mcp_config.json` empty (`{"mcpServers": {}}`) so unused MCP tool schemas are never injected into every turn.
   - Project-specific MCP servers (such as Supabase, Wordcraft, or Jupyter) belong inside `<project>/.agents/mcp_config.json` (see `settings/mcp_templates.example.json`).
3. **Global Rules (`GEMINI.md`)**:
   - Enforces targeted line-range reads (`StartLine`/`EndLine`), batched parallel tool calls, subagent delegation (`research`) for noisy exploration, `.ipynb` raw-read guard (preventing base64/output bloat), concise responses, lean-code guardrails, and automatic skill routing.
   - Integrates `graphify` (`~/GEMINI.md`) to query codebase knowledge graphs before raw file reads.
4. **Global Skill Router + Categorized Skill Library (21 Skills)**:
   - Only `skill-router` (plus 5 core skills: `graphify`, `find-skills`, `lean-code`, `read-only-agent`, `security-audit`) is registered globally in `~/.gemini/config/skills/`.
   - Domain skills live in `~/.gemini/skill-library/<category>/<skill>/SKILL.md`, indexed into `INDEX.md` via `agy-index-skills`.
   - `graphify/SKILL.md` (~2.2 KB fast-path + `references/full-pipeline.md`) and `security-audit/SKILL.md` (~10 KB guidance fast-path + `FULL-AUDIT-SETUP.md`) use Progressive Disclosure.
5. **Context Guardian (`PreInvocation` Auto-Compact Advisor)**:
   - Monitors step count and active tokens (`input_tokens + cache_read_tokens`) using your selected preset thresholds in `~/.gemini/config/hooks/preset.json`, with cooldown and automatic reset after `/compact`.
   - Enforces **Never Compact Mid-Task**: warns against compacting mid-fix, generates copy-paste `/compact <context + next step>` commands after milestones, and provides New Session Handoff prompts when tasks finish or reach the Red Zone.
6. **Antigravity CLI v1.5.15–1.5.16 Compatibility**:
   - Supports `AGY_CLI_AUTO_COMPACT_OVERRIDE` (e.g., `80%`, `800K`) for CLI-native auto-compaction tuning alongside Context Guardian.
   - Sets `"showThinking": false` by default (toggle live thinking with `/thinking`), and preserves user-global `~/.agents/skills` discovery while keeping `~/.gemini/config/skills/` clean.

## Skill Library Catalog (21 Starter Skills Across 7 Categories)

> This library is an **opinionated starter bundle** tailored around Next.js/React, Tailwind/shadcn, Laravel, FastAPI, Python/ML, and Supabase/Drizzle. Because `skill-router` loads skills on demand from `INDEX.md`, unused skills add zero prompt bloat—and you can freely add or remove category folders and re-run `agy-index-skills`.

| Category | Skills |
| :--- | :--- |
| `backend` | `fastapi-pydantic-v2`, `laravel13-specialist`, `saas-multitenant-highperf-api` |
| `frontend` | `nextjs-react19-best-practices`, `tailwind-v4-shadcn-ui`, `high-end-visual-taste`, `saas-dashboard-ux`, `design-system-microinteractions` |
| `database` | `drizzle-orm-postgres`, `supabase-ssr-rls` |
| `testing` | `playwright-e2e-rbac`, `vitest-rtl-testing`, `laravel-phpunit-tdd` |
| `devops` | `docker-compose-cicd-cloud` |
| `data-ai` | `colab-jupyter-notebooks`, `python-data-ml-scraping`, `python-modern-workflow`, `rag-llm-agents-embeddings`, `reverse-engineering-appsec` |
| `docs-office` | `office-docs-guidebook-automation`, `copywriting` |

## Quick Setup with Agent CLI (Zero Manual Config)

Run `agy` (or any AI coding CLI) on a new machine (Windows, macOS, or Linux) and paste this single prompt (optionally specify `preset 1`–`9`—if omitted, the agent will ask you to choose):

```text
Clone https://github.com/rizalkr/agy-setup.git to ~/Projects/agy-setup (or pull latest if it exists), then read and execute AGENT_SETUP.md to install the setup. Ask me which preset I want (Argon: 1 Balanced, 2 Ultra Saver, 3 Max Quality; Neon: 4 Neon Balanced [Recommended/Default], 5 Neon Ultra Saver, 6 Neon Max Quality; Carbon: 7 Carbon Balanced, 8 Carbon Ultra Saver, 9 Carbon Max Quality) before running the installer.
```

Or specify your preset directly in one shot:

```text
Clone https://github.com/rizalkr/agy-setup.git to ~/Projects/agy-setup (or pull latest if it exists), then read and execute AGENT_SETUP.md with preset 4 (neon-balanced).
```

## Manual Installation

### Linux / macOS (Bash/Zsh)

Interactive preset menu (choose 1–9 across Argon, Neon, or Carbon series):
```bash
git clone https://github.com/rizalkr/agy-setup.git ~/Projects/agy-setup
cd ~/Projects/agy-setup
./install.sh --choose
```

Or install a specific preset non-interactively (`--full` defaults to Preset 4 `neon-balanced`):
```bash
./install.sh --preset 4   # Neon:   4/neon-balanced (default) | 5/neon-saver | 6/neon-max
./install.sh --preset 1   # Argon:  1/balanced | 2/ultra-saver | 3/max-quality
./install.sh --preset 7   # Carbon: 7/carbon-balanced | 8/carbon-saver | 9/carbon-max
```

Minimal setup (rules, Context Guardian `preset.json`, & skills only, without merging CLI settings):
```bash
./install.sh
```

### Safe Install Flags & Model Independence

- **Non-destructive by default**: Existing `~/.gemini/GEMINI.md` and `~/GEMINI.md` are backed up to `*.bak` before overwrite, existing UX preferences (`colorScheme`, `vimInsertFirst`, `agentMode`, `artifactReviewPolicy`, `showThinking`) are preserved, and custom skills in `~/.gemini/config/skills/` or `~/.agents/skills/` are left intact (only DataCloud auto-injected bloat is pruned).
- **Keep your current model (`--no-orchestrator`)**: If your Antigravity version or plan uses different model names—or you simply prefer your current model—pass `--no-orchestrator` alongside `--preset`:
  ```bash
  ./install.sh --preset 4 --no-orchestrator
  ```
- **Opt-in global skill cleanup (`--prune-skills`)**: Pass `--prune-skills` only if you explicitly want to remove all non-core skills from `~/.gemini/config/skills/`.

Ensure `~/.local/bin` is in your `PATH` so `agy-index-skills` works globally.

### Windows (PowerShell)

Requires Python 3 (`py` or `python`) installed on PATH.

Interactive preset menu (choose 1–9 across Argon, Neon, or Carbon series):
```powershell
git clone https://github.com/rizalkr/agy-setup.git "$env:USERPROFILE\Projects\agy-setup"
cd "$env:USERPROFILE\Projects\agy-setup"
powershell -ExecutionPolicy Bypass -File .\install.ps1 --choose
```

Or install a specific preset directly (`--full` defaults to Preset 4 `neon-balanced`):
```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1 --preset 4   # or 1..9
```

Minimal setup (rules & skills only):
```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### Switching Presets Later
You can switch between Argon (`1`–`3`), Neon (`4`–`6`), and Carbon (`7`–`9`) presets anytime without losing permissions or workspaces:
```bash
./install.sh --preset 4               # Linux/macOS: Neon Balanced (Default)
./install.sh --preset carbon-balanced # Linux/macOS: Carbon Balanced
.\install.ps1 --preset 4              # Windows PowerShell: Neon Balanced
.\install.ps1 --preset 7              # Windows PowerShell: Carbon Balanced
```

### Optional Templates
- `settings/mcp_templates.example.json` -> copy individual servers (Supabase, Wordcraft, or Jupyter) into `<project>/.agents/mcp_config.json`
- `rules/personal.example.md` -> optional personal preferences (e.g., no-emoticons or conversation language rules) you can append to `~/.gemini/GEMINI.md`

## Adding New Skills & Syncing

> **Tip for other users**: Fork this repository first and clone your own fork if you plan to push personal rule/skill changes with `sync.sh` / `sync.ps1`.

1. Drop any new skill into `~/.gemini/skill-library/<category>/<skill-name>/SKILL.md`.
2. Refresh the index:
   ```bash
   agy-index-skills
   ```
3. Sync local changes back into this repository and push:
   - Linux / macOS:
     ```bash
     ./sync.sh && git add -A && git commit -m "chore: update skills" && git push
     ```
   - Windows (PowerShell):
     ```powershell
     .\sync.ps1; git add -A; git commit -m "chore: update skills"; git push
     ```
