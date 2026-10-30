<div align="center">

<h2 id="claude-code-community-guide">Claude Code Guide</h2>

_For reference and contributions, visit the [official Claude Code documentation](https://code.claude.com/docs/en/overview)_

_Commands and provider model mappings change quickly; the linked official references remain authoritative._

![Claude Code](https://img.shields.io/npm/v/@anthropic-ai/claude-code?label=Claude%20Code&logo=anthropic)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/anthropics/claude-code)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

</div>

<div align="center">

<kbd>

| Section                               | Status | Other Resources                                                                                         |
| ------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| Getting Started                       | ✅   | **Claude-Code** [Docs](https://code.claude.com/docs/en/overview)                                    |
| Configuration & Environment Variables | ✅   | **Claude-Code via** [**Discord**](https://github.com/zebbern/claude-code-discord)                       |
| Commands & Usage                      | ✅   | 70+ [Skills](https://github.com/zebbern/claude-code-guide/tree/main/skills) & [Agent pack](https://github.com/zebbern/claude-code-guide/tree/main/agents)               |
| Interface & Input                     | ✅   | Goal Creator [SKILL.md](https://github.com/zebbern/skills)                          |
| Advanced Features                     | ✅   | 1,900+ Agent [Skills](https://github.com/zebbern/antigravity-awesome-skills)                              |
| Automation & Integration              | ✅   | No cost ai [resources](https://github.com/zebbern/no-cost-ai)                                           |
| Help & Troubleshooting                | ✅   | 240+ Mermaid [templates](https://github.com/zebbern/mermaid-templates)                                  |
| Third-Party Integrations              | ✅   | Discord Communication [MCP](https://github.com/zebbern/discord-mcp-agent)                               |


</kbd>

</div>

---

<h3 id="content">Contents</h3>

**Fast paths:** [Install](#quick-start) · [Commands](#claude-commands) · [Config](#configuration--environment) · [MCP](#mcp-integration) · [Agents](#sub-agents) · [Troubleshoot](#help--troubleshooting)

| Area | Start here | Also useful |
| --- | --- | --- |
| [Getting Started](#getting-started) | [Quick Start](#quick-start) | [Initial Setup](#initial-setup), [System Requirements](#system-requirements) |
| [Configuration](#configuration--environment) | [Environment Variables](#environment-variables) | [Configuration Files](#configuration-files) |
| [Commands](#commands--usage) | [Slash Commands](#claude-commands) | [Command Line Flags](#command-line-flags), [CLI Quick Reference](#cheat-sheet) |
| [Interface](#interface--input) | [Keyboard Shortcuts](#keyboard-shortcuts) | [Vim Mode](#vim-mode) |
| [Advanced Features](#advanced-features) | [Plan Mode](#plan-mode), [Auto Mode](#auto-mode), [MCP](#mcp-integration) | [Sub Agents](#sub-agents), [Skills](#skills), [Hooks](#hooks-system) |
| [Security](#security--permissions) | [Security & Permissions](#security--permissions) | [Dangerous Mode](#dangerous-mode), [Best Practices](#security-best-practices-main) |
| [Automation](#automation--integration) | [Automation & Scripting](#automation--scripting-with-claude-code) | [PR Review](#auto-pr-review-inline-comments), [Issue Triage](#issue-triage-suggest-labels--severity) |
| [Help](#help--troubleshooting) | [Troubleshooting](#help--troubleshooting) | [Best Practices](#best-practices), [Monitoring](#monitoring--alerting) |
| [Third-Party Integrations](#third-party-integrations) | [DeepSeek Integration](#deepseek-integration) | [Provider Setup Examples](#provider-setup-examples), [Cloud Providers and Gateways](#cloud-providers-and-gateways) |

<details>
<summary>Full content map</summary>

- **[Getting Started](#getting-started)**
  - [Quick Start](#quick-start)
  - [System Requirements](#system-requirements)
  - [Initial Setup](#initial-setup)

- **[Configuration & Environment](#configuration--environment)**
  - [Environment Variables](#environment-variables)
  - [Global Config Options](#global-config-options)
  - [Configuration Files](#configuration-files)

- **[Commands & Usage](#commands--usage)**
  - [Slash Command Reference](#claude-commands)
  - [Command Line Flags](#command-line-flags)
  - [CLI Quick Reference](#cheat-sheet)

- **[Interface & Input](#interface--input)**
  - [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Vim Mode](#vim-mode)
  - [Command History](#command-history)

- **[Advanced Features](#advanced-features)**
  - [Thinking Mode](#thinking-keywords)
  - [Effort Levels](#effort-levels)
  - [Advisor Tool](#advisor-tool)
  - [Fast Mode](#fast-mode)
  - [Auto Mode](#auto-mode)
  - [Plan Mode](#plan-mode)
  - [Background Tasks](#background-tasks)
  - [Workflows & Scheduling](#workflows--scheduling)
  - [Cloud Sessions](#remote-sessions)
  - [Claude in Chrome](#claude-in-chrome)
  - [Desktop and IDEs](#desktop-and-ides)
  - [Sandbox Mode](#sandbox-mode)
  - [LSP Tool](#lsp-tool)
  - [Sub Agents](#sub-agents)
  - [Agent Teams](#agent-teams)
  - [Skills](#skills)
  - [Plugin System](#plugin-system)
  - [Worktree Isolation](#worktree-isolation)
  - [Native Installer](#native-installer)
  - [Authentication CLI](#claude-auth)
  - [Agent Management CLI](#claude-agents-cli)
  - [Remote Control](#remote-control)
  - [Managed Settings](#managed-settings)
  - [Model Updates](#model-updates)
  - [Theming & Customization](#theming--customization)
  - [Code Review](#code-review)
  - [Insights](#insights)
  - [Artifacts](#artifacts)
  - [MCP Integration](#mcp-integration)
  - [Hooks System](#hooks-system)

- **[Security & Permissions](#security--permissions)**
  - [Dangerous Mode](#dangerous-mode)
  - [Security Best Practices](#security-best-practices-main)

- **[Automation & Integration](#automation--integration)**
  - [Automation & Scripting](#automation--scripting-with-claude-code)
  - [Auto PR Review](#auto-pr-review-inline-comments)
  - [Security Review on Every PR](#security-review-on-every-pr)
  - [Issue Triage](#issue-triage-suggest-labels--severity)

- **[Help & Troubleshooting](#help--troubleshooting)**
  - [Debug Quick Commands](#debug-quick-commands)
  - [Path Temp Fix](#linuxpath)
  - [Windows Path Perm Fix](#windowspath)
  - [Installation Issues](#installation--nodejs-issues)
  - [Authentication Issues](#authentication-issues)
  - [Permission Issues](#permission--allowed-tools-issues)
  - [MCP Issues](#mcp-model-context-protocol-issues)
  - [Repair or Reinstall](#full-clean-reinstall-windows--powershell)
  - [One-Shot Health Check](#one-shot-health-check-copypaste)
  - [Useful Paths](#appendix-useful-paths)
  - [Best Practices](#best-practices)
  - [Effective Prompting](#effective-prompting)
  - [Performance Tips](#performance-tips)
  - [Monitoring & Alerting](#monitoring--alerting)
  - [Collaboration Best Practices](#collaboration-best-practices)
  - [Common Pitfalls to Avoid](#common-pitfalls-to-avoid)

- **[Third-Party Integrations](#third-party-integrations)**
  - [Provider Setup Examples](#provider-setup-examples)
  - [Cloud Providers and Gateways](#cloud-providers-and-gateways)
  - [DeepSeek Integration](#deepseek-integration)

</details>

---

<h1 id="getting-started">Getting Started</h1>

**Enable completion alerts:** Ghostty, Kitty, and iTerm2 (once its alert settings are on) show desktop notifications by default. Elsewhere, choose **Terminal bell** under `/config` → **Local notifications**, or set `"preferredNotifChannel": "terminal_bell"` in `~/.claude/settings.json`.

<h2 id="quick-start">Quick Start</h2>

> [!TIP]
> **Run <mark>claude</mark> in a project directory to start the interface.**
>
> **Go to [Help & Troubleshooting](#help--troubleshooting) to fix issues...**

**Native installer (recommended; no Node.js required)**

macOS, Linux, or WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Windows CMD:

```bat
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Supported package managers (manual updates by default):

```bash
brew install --cask claude-code          # stable channel; claude-code@latest tracks latest
winget install Anthropic.ClaudeCode
```

npm distribution (supported; Node.js 22+ is required to install):

```bash
npm install -g @anthropic-ai/claude-code
```

> [!Warning]
> npm 12 skips Claude Code's postinstall step by default, leaving a placeholder `claude` that prints `Error: claude native binary not installed.` (on Windows, the shell can't run it at all). Use the native installer, or allow the step as shown in [Installation / Node.js Issues](#installation--nodejs-issues). The binary ships as an optional dependency, so don't use `--omit=optional` or `optional=false` in `.npmrc`.

Verify the installation, then start Claude Code:

```bash
claude --version
claude doctor
claude
```

Native installs update themselves. Homebrew, WinGet, and the signed `apt`, `dnf`, and `apk` repositories follow their package manager's update flow; set `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1` to let Claude Code run the Homebrew or WinGet upgrade itself. See the [official setup guide](https://code.claude.com/docs/en/setup) for channels, version pinning, Linux repository setup, and signature verification. For an npm install, upgrade with `npm install -g @anthropic-ai/claude-code@latest`; do not use `sudo npm install -g`.

---

> [!Tip]
> <ins>**Open Project Via Terminal Into VS Code / Cursor**</ins>
>
> ### $ - <kbd>cd /path/to/project</kbd>
>
> ### $ - <kbd>code .</kbd>
>
> **Make sure you have the <mark>(Claude Code extension)</mark> installed in your VS Code / Cursor**

---

<h2 id="system-requirements">System Requirements</h2>

> - OS: macOS 13+, Windows 10 1809+/Windows Server 2019+, Ubuntu 20.04+, Debian 10+, or Alpine Linux 3.19+. Native Windows, WSL 1, and WSL 2 are supported.

> - Hardware: 4 GB+ RAM and an x64 or ARM64 processor

> - Shell: Bash, Zsh, PowerShell, or CMD

> - Software: Git is optional on native Windows; without Git for Windows, Claude uses the PowerShell tool instead of Bash, and the Monitor tool is unavailable. Node.js 22+ is required only to install through npm; the installed CLI is a native binary.

> - Alpine/musl: run `apk add bash curl libgcc libstdc++ ripgrep` (ripgrep is in the community repository), then set `"USE_BUILTIN_RIPGREP": "0"` under `env` in `settings.json`.

> - Internet: Connection for API calls from an [Anthropic supported region](https://www.anthropic.com/legal/supported-regions)

---

<h2 id="initial-setup">Initial Setup</h2>

Claude Code requires a Pro, Max, Team, Enterprise, or Console account, or access through Amazon Bedrock, Google Cloud's Agent Platform (Vertex AI), or Microsoft Foundry; the free Claude.ai plan does not include Claude Code. The normal first-party flow is browser sign-in:

```bash
claude auth login             # Claude subscription
claude auth login --console   # Anthropic Console/API billing
claude auth status            # Verify the active login
```

At the `/login` prompt, Console users can pick **Sign in with your Console account** to skip creating an API key; Bedrock and Agent Platform users can pick **3rd-party platform** (or run `/setup-bedrock` / `/setup-vertex`) for a setup wizard.

For API automation or a provider/gateway deployment, inject credentials from an OS key store or secret manager instead of committing them:

```bash
export ANTHROPIC_API_KEY="$SECRET_FROM_YOUR_STORE" # bash/zsh: current process only
```

```powershell
$env:ANTHROPIC_API_KEY = $secretFromYourStore # PowerShell: current process only
```

To run CI or scripts on a Pro, Max, Team, or Enterprise subscription, run `claude setup-token` once and store the one-year token it prints (it is not saved) as `CLAUDE_CODE_OAUTH_TOKEN`. It only makes model requests (no Remote Control or claude.ai connectors), and `--bare` ignores it; see [Authentication CLI](#claude-auth).

> [!Important]
> `ANTHROPIC_AUTH_TOKEN`, an approved `ANTHROPIC_API_KEY`, `apiKeyHelper`, and `CLAUDE_CODE_OAUTH_TOKEN` take precedence over your `/login` sign-in. Interactive sessions ask once before using `ANTHROPIC_API_KEY` (change the answer with **Use custom API key** in `/config`); `-p` always uses it. While an API key, auth token, or credential helper is in use, subscription-only features such as Remote Control, `/schedule`, claude.ai MCP connectors, and notification preferences remain unavailable. [Authentication Issues](#authentication-issues) lists the full precedence order; run `/status` to see which credential is active. Do not commit credentials; use your platform's secret storage.

---

<h1 id="configuration--environment">Configuration & Environment</h1>

<h2 id="environment-variables">Environment Variables</h2>

> **Environment values can also be stored as strings under the `env` key in a `settings.json` file. The [official environment-variable reference](https://code.claude.com/docs/en/env-vars) is the exhaustive source.**

> [!Important]
> **On PowerShell, use `$env:NAME = "value"` for the current process. Persist secrets through an OS key store or secret manager, not a checked-in settings file.**

```bash
# Authentication and routing: set only when API/provider billing is intentional
export ANTHROPIC_API_KEY="$SECRET_FROM_YOUR_STORE"
export ANTHROPIC_AUTH_TOKEN="$TOKEN_FROM_YOUR_STORE"
export ANTHROPIC_BASE_URL="https://gateway.example.com"
export ANTHROPIC_CUSTOM_HEADERS="X-Trace-Id: 12345"

# Model selection and provider alias overrides
export ANTHROPIC_MODEL="sonnet" # Wins over the model setting and a saved /model choice
# export ANTHROPIC_DEFAULT_MODEL="sonnet" # Alternative: starting model only; any model setting or saved /model choice wins
export ANTHROPIC_DEFAULT_FABLE_MODEL="<provider-fable-model-id>"
export ANTHROPIC_DEFAULT_OPUS_MODEL="<provider-opus-model-id>"
export ANTHROPIC_DEFAULT_SONNET_MODEL="<provider-sonnet-model-id>"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="<provider-haiku-model-id>"

# Third-party provider selection (enable one deployment path; only Bedrock and Mantle combine)
# export CLAUDE_CODE_USE_BEDROCK=1
# export ANTHROPIC_BEDROCK_REGION_PREFIX=eu # Prefer eu/us/apac/jp/au/global cross-region inference on Bedrock
# export CLAUDE_CODE_USE_MANTLE=1 # Amazon Bedrock Mantle endpoint; may be combined with CLAUDE_CODE_USE_BEDROCK
# export CLAUDE_CODE_USE_ANTHROPIC_AWS=1 # Claude Platform on AWS; also set ANTHROPIC_AWS_WORKSPACE_ID and AWS_REGION
# export CLAUDE_CODE_USE_VERTEX=1 # Google Cloud's Agent Platform (formerly Vertex AI)
# export CLAUDE_CODE_USE_FOUNDRY=1
# export CLAUDE_CODE_MODEL_CATALOG=off # Cloud providers: don't fetch signed model settings from downloads.claude.ai
# export CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0 # Full system prompt on any model, including custom deployment names/ARNs

# Timeouts, retries, and output budgets, in milliseconds/tokens
export API_TIMEOUT_MS=1200000
export BASH_DEFAULT_TIMEOUT_MS=120000
export BASH_MAX_TIMEOUT_MS=600000
export MCP_TIMEOUT=30000
export MCP_TOOL_TIMEOUT=600000 # Overall MCP tool limit (default ~28h); above 60000 it also raises remote servers' 60 s per-request limit
export MAX_MCP_OUTPUT_TOKENS=25000
export MAX_THINKING_TOKENS=0 # 0 disables thinking on the Anthropic API, except Opus/Sonnet/Haiku 5.5 and Fable; adaptive models ignore a positive budget (use effort)
# export CLAUDE_CODE_RETRY_WATCHDOG=1 # Unattended runs (CI, workers): keep retrying 429/529 capacity errors
# export CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS=1800000 # Cap each request's 429/529 wait under the watchdog

# Session, context, agents, and accessibility
# export CLAUDE_CODE_SIMPLE=1
# export CLAUDE_CODE_SAFE_MODE=1
export CLAUDE_CODE_DISABLE_1M_CONTEXT=1 # Clamp native-1M models to 200K via autocompaction; warns if the clamp is not enforced
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1 # Opt out of enforcing the assumed context window for unknown model IDs
export CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=20
export CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=3
export CLAUDE_CODE_FORWARD_SUBAGENT_TEXT=1
export CLAUDE_AX_SCREEN_READER=1

# Feature and administration controls
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
export CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1
export ENABLE_CLAUDEAI_MCP_SERVERS=false

# Network routing
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="http://proxy.example.com:8080"
export NO_PROXY="localhost,127.0.0.1"
export NODE_EXTRA_CA_CERTS="/path/to/corporate-ca.pem" # Only if a TLS-inspecting proxy's CA isn't in the OS trust store (or npm installs on Node < 22.15)

# Privacy/network reduction: these are presence-based; unset them to turn them off
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
export DISABLE_TELEMETRY=1
export DISABLE_ERROR_REPORTING=1
```

The block is a catalog, not a recommended profile—do not enable mutually exclusive provider variables together. Boolean variables usually accept `1`/`true` and `0`/`false`, but the three presence-based variables shown at the end treat any non-empty value, including `0`, as enabled. `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` and `DISABLE_TELEMETRY` also stop [feature-flag fetching](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching), which disables `/import`, the advisor tool, claude.ai skill and plugin sync, and idle compaction; the first also turns off Remote Control, auto-updates, and `/feedback`.

An `env` value in `settings.json` replaces the shell's value; set it to `""` to cancel a stale shell export (removing the key takes effect at the next launch). Most values from `.claude/settings.json` and `.claude/settings.local.json` apply only after you trust the workspace, and those files cannot set variables a repository shouldn't control, such as `CLAUDE_CONFIG_DIR`, `TMPDIR`, OpenTelemetry exporter variables, or `CLAUDE_AX_SCREEN_READER`; put those in your shell, user, or managed settings (`claude --debug` logs any it drops). Sessions launched by the Claude Desktop app keep the app's launch value for variables it sets.

<h2 id="global-config-options">Global Config Options</h2>

Use `/config` for interactive settings, or pass one or more `key=value` pairs. Run `/config --help` for the keys supported by your installed build.

```bash
/config                         # Open the settings UI
/config theme=dark model=sonnet # Update supported keys directly
```

For version-controlled or managed configuration, edit JSON settings files directly:

| Scope | File |
| :---- | :--- |
| User | `~/.claude/settings.json` |
| Project (shared) | `.claude/settings.json` |
| Project (private) | `.claude/settings.local.json` |
| Managed | macOS: `/Library/Application Support/ClaudeCode/`<br />Linux/WSL: `/etc/claude-code/`<br />Windows: `C:\Program Files\ClaudeCode\` |

```json
{
  "model": "sonnet",
  "theme": "dark",
  "autoUpdatesChannel": "stable",
  "permissions": {
    "defaultMode": "default"
  }
}
```

Settings-file precedence is **managed policy → `--settings` → local → project → user**. Other flags and environment variables are not levels in this stack; each key decides whether they win (`--model` and `ANTHROPIC_MODEL` beat any `model` setting, even a managed one, which is only a starting default). List keys such as `permissions.allow` merge across files, so read [settings precedence](https://code.claude.com/docs/en/settings#settings-precedence) before relying on last-writer-wins behavior; [All settings](https://code.claude.com/docs/en/settings-reference) lists every key. With no permission mode configured, interactive sessions start in auto mode; `permissions.defaultMode` overrides that, but `auto` and `bypassPermissions` apply only from user or managed settings (or `--settings` / `--permission-mode`). `~/.claude.json` stores global state, session/trust data, and local/user MCP configuration; it is not the user settings file.

To hide all commit and PR attribution, set `"attribution": false`. Versions before v2.1.281 skip a settings file that contains it, so in files they also read use `"attribution": { "commit": "", "pr": "", "sessionUrl": false }`.

<h2 id="configuration-files">Configuration Files</h2>

Claude Code combines human-authored instructions from several locations:

| Memory Type                | Location                                                                                                                                                | Purpose                                             | Use Case Examples                                                    | Shared With                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
| **Enterprise policy**      | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br />Linux: `/etc/claude-code/CLAUDE.md`<br />Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization       |
| **Project memory**         | `./CLAUDE.md` or `./.claude/CLAUDE.md`                                                                                                                  | Team-shared instructions for the project            | Project architecture, coding standards, common workflows             | Team members via source control |
| **User memory**            | `~/.claude/CLAUDE.md`                                                                                                                                   | Personal preferences for all projects               | Code styling preferences, personal tooling shortcuts                 | Just you (all projects)         |
| **Project memory (local)** | `./CLAUDE.local.md`                                                                                                                                     | Personal project preferences (add to `.gitignore`)  | Your sandbox URLs, preferred test data, personal overrides           | Just you (current project)      |
| **Project rules**          | `.claude/rules/**/*.md`                                                                                                                                 | Modular project rules (loaded alongside CLAUDE.md)  | Linting rules, API conventions, path-scoped standards                 | Team members via source control |
| **User rules**             | `~/.claude/rules/**/*.md`                                                                                                                               | Personal rules, loaded before project rules         | Preferred tools, personal workflow conventions                       | Just you (all projects)         |

> Instruction files are concatenated rather than overriding one another. User and ancestor-project files load at startup; `CLAUDE.md` files in subdirectories load lazily when Claude works there. In monorepos, skip other teams' or unrelated ancestor files with the `claudeMdExcludes` setting (glob patterns; a managed `CLAUDE.md` can't be excluded). `CLAUDE.md` is context, not an enforcement boundary. Run `/doctor prompt-audit` for a report of outdated, broken, or conflicting instructions; it edits nothing until you approve.

Use `@path` to import another file. When no `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` exists in the working directory or above it, Claude Code reads `AGENTS.md` instead; user and managed `CLAUDE.md` files and `.claude/rules/` still load. If any of those project files exists (even just `CLAUDE.local.md`), `AGENTS.md` is skipped: import it with `@AGENTS.md`, or set **Project instructions** to `claude-md-and-agents-md` in `/config` to load both.

#### `.claude/rules/` Directory

The `.claude/rules/` directory lets you break project instructions into separate Markdown files instead of one large `CLAUDE.md`. Markdown files are discovered recursively. Add `paths` frontmatter with glob patterns when a rule should load only for matching files. This is useful for:

- **Modular organization**: Separate concerns (e.g., `api-conventions.md`, `testing-rules.md`)
- **Per-directory scoping**: `paths`-scoped rules and rules in a subdirectory's `.claude/rules/` load on demand when Claude reads, writes, or edits files they cover, adding to other rules rather than overriding them
- **Team collaboration**: Different team members can own different rule files via PR review

#### Auto-Memory

Claude can save useful working context under `~/.claude/projects/<project>/memory/`. It loads the first 200 lines or 25 KB of `MEMORY.md`; use `/memory` to inspect, edit, disable, or remove saved memories. Auto-memory is machine-local and shared across worktrees for the same repository. Turn it off for one project with `"autoMemoryEnabled": false` in that project's settings, or everywhere with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`; `autoMemoryDirectory` moves where it is stored.

Auto-memory is most useful for context you would otherwise repeat across sessions:

- Preferred build, test, and lint commands
- Local conventions that are not obvious from code alone
- Architecture decisions that influence future edits
- Team preferences that should shape how Claude proposes changes

Keep durable team rules in `CLAUDE.md` or `.claude/rules/`. Treat auto-memory as helpful working context, not as the only source of truth.

---

<h1 id="commands--usage">Commands & Usage</h1>

<h2 id="claude-commands">Slash Command Reference</h2>

Type `/` to see what your installed build, plan, platform, plugins, MCP servers, and skills actually provide. The table below is a high-value snapshot; use the [official command reference](https://code.claude.com/docs/en/commands) for the live list.

| Command | Purpose |
| :------ | :------ |
| `/add-dir <path>` | Grant this session access to another working directory |
| `/advisor [model\|off]` | Configure the experimental second-model advisor, save the selection, or turn it off |
| `/agents` | Explain how to create or edit subagents; hidden from the `/` menu, and the old interactive wizard was removed in v2.1.198 |
| `/artifacts` | List artifacts you own or that are shared with you; attach one to the session, open it, or copy its link |
| `/auto-mode-setup` | Draft `autoMode.environment` entries from your project and recent sessions, then review and save them to user settings |
| `/autocompact [auto\|tokens]` | Set the auto-compact window per model (e.g. `/autocompact 200k` if your gateway stops at 200K); `auto` restores the default |
| `/background [prompt]` | Detach the current conversation as a background session (`/bg` alias) |
| `/batch <instruction>` | Decompose a large change into worktree-isolated background units (bundled skill) |
| `/branch [name]` | Switch into a new branch of the current conversation while preserving the original |
| `/btw [question]` | Ask an ephemeral side question without adding it to conversation history |
| `/cd <path>` | Move the current session to another working directory; its project settings, hooks, skills, agents, and `.mcp.json` servers (after approval) apply immediately |
| `/clear [name]` | Start a new conversation with empty context while preserving project memory |
| `/code-review [level] [--fix] [--comment] [--max-findings n\|all\|default] [target]` | Run a local background review, or use level `ultra` for cloud review; levels run from `low` through `max`. `--comment` posts to a GitHub PR or GitLab MR; a `--max-findings` choice sticks until you pass `default` |
| `/compact [instructions]` | Summarize the conversation to free context |
| `/config [key=value ...]` | Open settings or update supported keys directly (`/settings` alias) |
| `/context [all]` | Visualize what is using the context window |
| `/copy [N]` | Copy the last (or Nth-latest) response; a picker selects single code blocks, and `w` writes to a file instead (useful over SSH) |
| `/diff` | Open the interactive current/per-turn diff viewer; in fullscreen mode, toggle a panel of uncommitted changes beside the conversation |
| `/doctor [prompt-audit [path]]` | Diagnose setup, configuration, hooks, memory, plugins, and MCP; can offer fixes (`/checkup` alias). `prompt-audit` checks CLAUDE.md, skills, agents, and commands for stale paths and prompting patterns written for older models |
| `/effort [level\|auto\|status\|ultracode [on\|off]]` | Set model-dependent effort (`low` to `xhigh` save per model; `max`, or `s` in the picker, is session-only). `status` prints the level; `ultracode [on\|off]` toggles ultracode at any effort level |
| `/fast [on\|off]` | Toggle fast mode where the selected Opus model and plan support it |
| `/focus` | Toggle focus view (fullscreen rendering only): your last prompt, a one-line tool summary, and the final response |
| `/fork [prompt]` | Copy this conversation into a worktree-isolated background session and keep working here |
| `/goal [condition\|clear]` | Keep working across turns until a completion condition is met |
| `/hooks` | Inspect configured hooks in the read-only hook browser |
| `/import [codex\|gemini\|cursor] [--dry-run] [--yes]` | Bring instruction files, MCP servers, commands, subagents, and skills over from OpenAI Codex, Gemini CLI, or Cursor; `--dry-run` previews and `--yes` skips the picker |
| `/init` | Generate a starter `CLAUDE.md` for the project |
| `/keybindings` | Open `~/.claude/keybindings.json` to customize shortcuts (see [Keyboard Shortcuts](#keyboard-shortcuts)) |
| `/loop [interval] [prompt]` | Run a prompt repeatedly while the session remains open |
| `/mcp [reconnect\|enable\|disable] [server\|all]` | Inspect, authenticate, enable, disable, or reconnect MCP servers; `/mcp reconnect all` retries every server that failed or needs authentication |
| `/memory` | Manage `CLAUDE.md`, rules, and auto-memory |
| `/model [model]` | Switch model and normally save it as the default; press `s` in the picker for session-only selection |
| `/output-style [style]` | List output styles or switch to one, such as `/output-style concise` |
| `/permissions` | Manage allow, ask, and deny rules (`/allowed-tools` alias) |
| `/plan [description]` | Enter plan mode, optionally with a task |
| `/plugin [subcommand]` | Discover, install, enable, disable, and manage plugins |
| `/reload-plugins [--force]` | Apply plugin changes without restarting when safe |
| `/remote-control [name]` | Expose this local session to claude.ai/code or the Claude mobile app |
| `/resume [session]` | Resume by ID/name or open the session picker |
| `/review ...` | Alias for `/code-review` as of v2.1.223 |
| `/rewind` | Restore or summarize code and conversation from a checkpoint; Bash edits such as `sed -i` are not checkpointed unless Claude already edited that file with its file tools (`/undo` alias) |
| `/sandbox` | View and configure OS-level filesystem/network sandboxing for Bash, PowerShell, and Monitor commands on supported platforms |
| `/schedule [description]` | Create, update, list, or run cloud scheduled tasks, formerly routines (`/routines` alias) |
| `/security-review` | Review the current branch diff for security vulnerabilities |
| `/simplify` | Review changed code for reuse, quality, and efficiency improvements |
| `/skill-doctor` | Show what each skill costs in context and how often it is used, so you can turn off unused ones |
| `/skills` | List skills; press `t` to sort by token cost and `Space`/`Enter` to change a skill's visibility |
| `/status` | Show version, model, account, and connectivity on the Settings Status tab; works while Claude is responding |
| `/statusline [description]` | Configure the status line from a description, or from your shell prompt when run without arguments |
| `/subtask [prompt]` | Run the former in-session fork behavior as a subagent that reports back here |
| `/tasks` | List the current session's background shells, subagents, and tool calls |
| `/teleport [session]` | Pull a cloud session's branch and conversation into this terminal (`/tp` alias) |
| `/tui [default\|fullscreen]` | Switch the terminal renderer and relaunch with the conversation intact; with no argument, print the active renderer |
| `/usage` | Show session cost and prompt-cache hits, plan usage limits, and activity stats, with one-line fixes for warnings (`/cost`, `/stats` aliases) |
| `/usage-credits` | Configure usage credits, or on Team/Enterprise request them from your admin, when you hit a limit (formerly `/extra-usage`) |
| `/verify` | Build, run, and observe your app to confirm a change works beyond tests and type checks (bundled skill; Claude runs it only when you invoke it) |
| `/voice [hold\|tap\|off]` | Toggle voice dictation or choose its mode; needs a Claude.ai login |
| `/workflows` | Inspect dynamic workflow runs and background orchestration |

<h2 id="command-line-flags">Command Line Flags</h2>

| Flag / Command                                       | Description                                                                                                                                                  | Example                                                                                |
| :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| `-d, --debug`                                        | Enable debug mode (shows detailed debug output).                                                                                                             | `claude -d -p "query"`                                                                 |
| `--include-partial-messages`                         | Include partial streaming events; requires print mode and `stream-json`.                                                                                     | `claude -p --output-format stream-json --verbose --include-partial-messages "query"`   |
| `--include-hook-events`                              | Include hook lifecycle events in `stream-json` output.                                                                                                       | `claude -p --output-format stream-json --verbose --include-hook-events "query"`        |
| `--forward-subagent-text`                            | Forward subagent text/thinking with `parent_tool_use_id` in `stream-json`.                                                                                   | `claude -p --output-format stream-json --verbose --forward-subagent-text "query"`      |
| `--verbose`                                          | Override verbose mode setting from config (shows expanded logging / turn-by-turn output).                                                                    | `claude --verbose`                                                                     |
| `-p, --print`                                        | Print response and exit (useful for piping output).                                                                                                          | `claude -p "query"`                                                                    |
| `--output-format <format>`                           | Output format (only works with `--print`): `text` (default), `json` (single result), or `stream-json` (realtime streaming; requires `--verbose`).            | `claude -p "query" --output-format json`                                               |
| `--input-format <format>`                            | Input format (only works with `--print`): `text` (default) or `stream-json` (realtime streaming input).                                                      | `claude -p --verbose --output-format stream-json --input-format stream-json`           |
| `--replay-user-messages`                             | Re-emit user messages from stdin back to stdout for acknowledgment — **only works with** print mode plus `stream-json` input and output.                    | `claude -p --verbose --input-format stream-json --output-format stream-json --replay-user-messages` |
| `--allowedTools`, `--allowed-tools <tools...>`       | Comma/space-separated permission rules to allow.                                                                                                              | `claude --allowed-tools "Bash(git *)" "Edit"`                                        |
| `--disallowedTools`, `--disallowed-tools <tools...>` | Comma/space-separated permission rules to deny.                                                                                                               | `claude --disallowed-tools "Edit"`                                                     |
| `--mcp-config <configs...>`                          | Load MCP servers from JSON files or strings (space-separated).                                                                                               | `claude --mcp-config ./mcp-servers.json`                                               |
| `--strict-mcp-config`                                | Only use MCP servers from `--mcp-config`, ignoring other MCP configurations; exits at startup if a `managed-mcp.json` is deployed.                                                                                 | `claude --mcp-config ./a.json --strict-mcp-config`                                     |
| `--append-system-prompt <prompt>`                    | Append a system prompt to the default system prompt (useful in print mode).                                                                                  | `claude -p --append-system-prompt "Do X then Y"`                                       |
| `--autocompact <auto\|tokens>`                       | Override the auto-compaction window for this session.                                                                                                        | `claude --autocompact 500k`                                                           |
| `--ax-screen-reader`                                 | Use a flat, screen-reader-friendly renderer without decorative borders or animations.                                                                         | `claude --ax-screen-reader`                                                           |
| `--bare`                                             | Minimal scripted mode: skip discovered hooks, skills, plugins, MCP, auto-memory, and `CLAUDE.md`.                                                             | `claude --bare -p "query"`                                                           |
| `--permission-mode <mode>`                           | Start in `default`/`manual`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, or `plan`.                                                               | `claude --permission-mode plan`                                                        |
| `--permission-prompt-tool <tool>`                    | Specify an MCP tool to handle permission prompts in non-interactive mode; pass the full `mcp__<server>__<tool>` name of a tool on an MCP server the run loads. | `claude -p --mcp-config ./mcp.json --permission-prompt-tool mcp__permissions__approve "query"` |
| `--permission-prompts <host\|none>`                  | Print mode: `host` (default) sends prompts to the SDK host or `--permission-prompt-tool`; `none` denies anything that would prompt, while the permission mode decides the rest. | `claude -p --permission-mode auto --permission-prompts none "query"`                   |
| `--fallback-model <models>`                          | Comma-separated fallback chain for when the primary model is overloaded or unavailable (interactive or print mode); the primary is retried each turn. Overrides `fallbackModel`. | `claude --fallback-model sonnet,haiku`                                                 |
| `--effort <level>`                                   | Set effort to `low`, `medium`, `high`, `xhigh`, or `max`; `ultracode` starts at `xhigh` with ultracode turned on.                                              | `claude --effort high`                                                                |
| `--model <model>`                                    | Model for the current session. Accepts aliases like `sonnet`/`opus` or a full model ID when pinning.                                                         | `claude --model sonnet`                                                                |
| `--advisor <model>`                                  | Set the experimental advisor for this session without changing `advisorModel`; intentionally omitted from `claude --help`.                                  | `claude --advisor opus`                                                                |
| `--settings <file-or-json>`                          | Load additional settings from a JSON file or a JSON string.                                                                                                  | `claude --settings ./settings.json`                                                    |
| `--add-dir <directories...>`                         | Additional directories to allow tool access to. Most network paths (UNC shares, `/net` automounts) are refused; on Windows, use a mapped drive letter.       | `claude --add-dir ../apps ../lib`                                                      |
| `--ide`                                              | Automatically connect to an IDE on startup if exactly one valid IDE is available.                                                                            | `claude --ide`                                                                         |
| `-c, --continue`                                     | Continue the most recent conversation in the current directory.                                                                                              | `claude --continue`                                                                    |
| `-r, --resume [id\|name]`                            | Resume by session ID, name, or `.jsonl` transcript path, or open the picker; resuming a still-running background session attaches to it.                     | `claude -r auth-refactor`                                                              |
| `--session-id <uuid>`                                | Use a specific session ID for the conversation (must be a valid UUID).                                                                                       | `claude --session-id 123e4567-e89b-12d3-a456-426614174000`                             |
| `--agents <json\|file>`                              | Define custom subagents dynamically via inline JSON or, with `-p`, a path to a JSON file (see subagent docs for format).                                     | `claude --agents '{"reviewer":{"description":"Reviews code","prompt":"..."}}'`         |
| `--agent <name>`                                     | Specify a specific agent for the current session.                                                                                                            | `claude --agent my-custom-agent`                                                       |
| `--bg`                                               | Start or continue work as a background session that can be viewed from `claude agents`.                                                                      | `claude --bg "fix failing tests"`                                                      |
| `--bg --exec <command>`                              | Run a shell command as an attachable background session.                                                                                                     | `claude --bg --exec "npm test"`                                                        |
| `-n, --name <name>`                                  | Set a display name for any session (prompt box, `/resume` picker, terminal title); resume it later with `claude --resume <name>`.                            | `claude -n auth-refactor`                                                              |
| `--chrome`                                           | Enable Chrome browser integration for web automation and testing.                                                                                            | `claude --chrome`                                                                      |
| `--no-chrome`                                        | Disable Chrome browser integration for this session.                                                                                                         | `claude --no-chrome`                                                                   |
| `--cloud [description\|session\|url]`               | Create a cloud session on claude.ai; with `-p` and a session ID or URL, queue a message into an existing one.                                                | `claude --cloud "Fix the login bug"`                                                   |
| `--remote`                                           | Deprecated alias for `--cloud`.                                                                                                                              | `claude --remote "Fix the login bug"`                                                  |
| `--remote-control`, `--rc`                           | Start an interactive local session that can also be controlled from claude.ai or the Claude app.                                                            | `claude --remote-control "My Project"`                                                 |
| `--teleport [session]`                               | Pull a cloud session into your local terminal; with no ID it opens a picker.                                                                                 | `claude --teleport <session-id>`                                                       |
| `--fork-session`                                     | When resuming, create a new session ID instead of reusing the original.                                                                                      | `claude --resume abc123 --fork-session`                                                |
| `--json-schema <schema>`                             | Get validated JSON output matching a JSON Schema after agent completes (print mode only).                                                                    | `claude -p --json-schema '{"type":"object",...}' "query"`                              |
| `--max-budget-usd <amount>`                          | Maximum dollar amount to spend on API calls before stopping (print mode only).                                                                               | `claude -p --max-budget-usd 5.00 "query"`                                              |
| `--max-turns <n>`                                    | Limit the number of agentic turns (print mode only). Exits with error when limit reached.                                                                    | `claude -p --max-turns 3 "query"`                                                      |
| `--betas <headers>`                                  | Beta headers to include in API requests (API key users only).                                                                                                | `claude --betas interleaved-thinking`                                                  |
| `--tools <tools>`                                    | Restrict which built-in tools Claude can use. Use "" to disable all, "default" for all, or specific tool names.                                              | `claude --tools "Bash,Edit,Read"`                                                      |
| `--system-prompt <prompt>`                           | Replace the entire system prompt with custom text (works in interactive and print modes).                                                                    | `claude --system-prompt "You are a Python expert"`                                     |
| `--system-prompt-file <file>`                        | Load a system prompt from a file, replacing the default in interactive or print mode.                                                                         | `claude --system-prompt-file ./custom-prompt.txt`                                      |
| `--append-system-prompt-file <file>`                 | Load additional system-prompt text from a file in interactive or print mode; can be combined with `--append-system-prompt` (the file's text comes first).    | `claude --append-system-prompt-file ./extra-rules.txt`                                 |
| `--system-prompt-snapshot <on\|off>`                 | `on` (default) reuses the prompt recorded on the first request, even after `--resume`/`--continue`, until compaction; `off` rebuilds it each request (for iterating on prompt flags). | `claude -c --append-system-prompt "Draft rules" --system-prompt-snapshot off`          |
| `--plugin-dir <path>`                                | Load a plugin directory, a `.zip`, or a folder of plugins (each child with a manifest loads) for this session only (repeatable).                             | `claude --plugin-dir ./my-plugin --plugin-dir ./other.zip`                             |
| `--plugin-url <url>`                                 | Fetch a plugin `.zip` URL for this session only (repeatable).                                                                                                 | `claude --plugin-url https://example.com/plugin.zip`                                  |
| `--setting-sources <sources>`                        | Comma-separated list of setting sources to load (user, project, local).                                                                                      | `claude --setting-sources user,project`                                                |
| `--no-session-persistence`                           | Disable session persistence so sessions are not saved to disk (print mode only).                                                                             | `claude -p --no-session-persistence "query"`                                           |
| `--disable-slash-commands`                           | Disable all skills and slash commands for this session.                                                                                                      | `claude --disable-slash-commands`                                                      |
| `--dangerously-skip-permissions`                     | Skip normal permission prompts, subject to non-bypassable safety checks and managed policy.                                                                  | `claude --dangerously-skip-permissions`                                                |
| `--allow-dangerously-skip-permissions`               | Add bypass mode to the `Shift+Tab` cycle without starting in it.                                                                                             | `claude --permission-mode plan --allow-dangerously-skip-permissions`                   |
| `--safe-mode`                                        | Disable customizations (CLAUDE.md, skills, plugins and installed mods, hooks, MCP servers, and more) for troubleshooting; authentication, models, built-in tools, permissions, and managed policy still apply.                       | `claude --safe-mode`                                                                  |
| `--restricted`                                       | Locked-down session (also `CLAUDE_CODE_RESTRICTED=1`): removes built-in tools that run commands or code, and WebFetch, unless named in `--tools`; confines file tools to the working directories; ignores user/project/local settings; refuses `bypassPermissions`. | `claude --restricted -p "query"`                                                       |
| `--worktree [name]`, `-w [name]`                     | Start in `<repo>/.claude/worktrees/<name>`; omit the name to generate one, or pass `#<number>` or a GitHub PR / GitLab MR URL to branch from it. Add `--tmux` for a tmux session. | `claude -w feature-auth`                                                               |
| `--from-pr [value]`                                  | Filter/resume sessions by PR number or GitHub/GitLab/Bitbucket PR/MR URL, or open the picker.                                                                | `claude --from-pr 123`                                                                |
| `--init`                                             | Run Setup hooks with the `init` matcher before a print-mode session.                                                                                         | `claude -p --init "query"`                                                            |
| `--init-only`                                        | Run Setup and `SessionStart` hooks, then exit without starting a conversation.                                                                               | `claude --init-only`                                                                   |
| `--maintenance`                                      | Run Setup hooks with the `maintenance` matcher before a print-mode session.                                                                                  | `claude -p --maintenance "query"`                                                     |
| `-v, --version`                                      | Show the installed `claude` CLI version.                                                                                                                     | `claude --version`                                                                     |
| `-h, --help`                                         | Display help / usage.                                                                                                                                        | `claude --help`                                                                        |

> This table highlights common and recently changed options; `claude --help` and the [live CLI reference](https://code.claude.com/docs/en/cli-reference) are authoritative. `--output-format json` is useful for one-shot automation; use `stream-json` for event-level integrations.

For programmatic integrations, the former **Claude Code SDK** is now the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview): TypeScript uses `@anthropic-ai/claude-agent-sdk`, and Python uses `claude-agent-sdk` / `claude_agent_sdk`. Use `claude -p` for headless CLI calls; `--bare` removes discovered customization and keychain/OAuth access for low-overhead API/provider automation.

<h2 id="cheat-sheet">CLI Quick Reference & Configuration Examples</h2>

```md
## Claude Cheat Sheet

# Start and resume

claude # Start interactive REPL
claude "explain this project" # Start REPL seeded with a prompt
claude -p "summarize README.md" # Non-interactive headless print mode
cat logs.txt | claude -p "explain" # Pipe input to Claude and exit
claude -c # Continue most recent conversation
claude -r "<session-id>" "finish this" # Resume by ID or name
claude --model sonnet # Pick the Sonnet alias for this run
claude --model opus # Pick the Opus alias for harder tasks

# Install, update, and auth

claude update # Manually update Claude Code
claude doctor # Diagnose install/version & setup
claude install stable # Install/reinstall the native binary on the stable channel
claude auth login # Log in to your Anthropic account
claude auth status # Check authentication status
claude auth logout # Log out
claude setup-token # Generate a long-lived OAuth token for CI and scripts (subscription)

# Background, cloud, and Remote Control sessions

claude agents # Open the live session dashboard: running, blocked, completed
claude agents --json # Scriptable JSON list of live/background sessions
claude --bg "run the integration suite and summarize failures" # Start a background session
claude --bg --exec "npm test" # Run a shell command as an attachable background session
claude attach <id|name> # Attach to a background session (part of its name works)
claude logs <id|name> # Print recent background-session output
claude stop <id> # Stop a background session
claude rm <id> # Remove it from agent view and delete its worktree; transcript remains resumable
claude remote-control # Serve local sessions to web/mobile while this process stays alive
claude --cloud "Fix the bug" # Start a cloud session on claude.ai
claude --teleport <session-id> # Pull a cloud session into this terminal

# Config essentials

/config # Interactive settings
/config model=sonnet # Set a supported key directly
/config theme=dark
/config --help # Show settable keys and values
# For shared or managed settings, edit the appropriate settings.json file.

# MCP essentials

claude mcp list # List configured MCP servers
claude mcp get <name> # Show details for a server
claude mcp add <name> -- <command> [args...] # Add local stdio server; `--` separates Claude's options from the server's
claude mcp add --transport http <name> <url> # Add remote HTTP server
claude mcp login <name> # Complete OAuth without opening /mcp
claude mcp logout <name> # Clear saved OAuth credentials
claude mcp reset-project-choices # Reset approvals for project .mcp.json servers
claude mcp serve # Run Claude Code itself as an MCP stdio server

# High-value flags

claude --add-dir ../apps ../lib # Add additional working directories
claude --allowed-tools "Bash(git log *)" "Read" # Allow listed tools without permission prompts
claude --disallowed-tools "Edit" # Deny listed tools
claude -p "query" --output-format json # Structured one-shot output
claude --verbose # Verbose logging (turn-by-turn)
claude --dangerously-skip-permissions # Skip permission prompts (use with caution)
claude --permission-mode plan # Start in plan mode without source edits
claude --effort high # Set reasoning effort for this session
claude --bare -p "query" # Fast scripted call without discovered customization
claude --safe-mode # Troubleshoot with user/project customization disabled
claude --ax-screen-reader # Use the accessible flat-text renderer
claude --max-turns 3 -p "query" # Limit agentic turns (print mode only)
claude --json-schema '{"type":"object"}' -p "query" # Get validated JSON output
claude --chrome # Enable Chrome browser integration
claude --agent code-reviewer # Run this session with a named agent
claude ultrareview 123 --trust-workspace --json # Non-interactive cloud review of PR 123; in scripts/CI, --trust-workspace trusts an untrusted folder for this run

# Slash shortcuts

claude --fork-session -r abc123 # Fork instead of reusing original
claude -w feature-auth "implement feature" # Start in an isolated git worktree
/rename auth-refactor # Name current session
/resume # Open session picker
/export output.md # Export conversation to file
/branch experiment-name # Branch the current conversation
/fork "investigate the flaky test" # Copy conversation into a background session
/subtask "trace the regression" # Fork a subagent that reports back here
/cd ../other-project # Move the current session to another directory, keeping the conversation
/review high --fix # Run /code-review via its current alias
/goal "all tests pass and README is updated" # Keep working until the completion condition is met
/loop 30m "check deploy health and summarize anomalies" # Schedule recurring work
/workflows # View dynamic workflows and background orchestration

# Settings precedence: managed policy > CLI/--settings > local > project > user.
```

---

<h1 id="interface--input">Interface & Input</h1>

<h2 id="keyboard-shortcuts">Keyboard Shortcuts</h2>

| Shortcut                     | Description                        | Context                                  |
| :--------------------------- | :--------------------------------- | :--------------------------------------- |
| `Ctrl+C`                     | Interrupt, or clear input          | Interrupts a running operation; when idle, clears the prompt (`Up` restores it), and a second press exits |
| `Ctrl+D`                     | Exit Claude Code session           | Press twice on an empty prompt; with text, deletes the next character |
| `Ctrl+G`                     | Open in default text editor        | Edit your prompt or custom response      |
| `Ctrl+L`                     | Redraw the screen                  | Keeps your input and conversation; `/clear` starts a new conversation |
| `Ctrl+O`                     | Toggle transcript viewer           | Shows detailed tool usage, timestamps, and model |
| `Ctrl+R`                     | Reverse search command history     | Search through previous commands         |
| `Ctrl+V` (`Cmd+V` in iTerm2); `Alt+V` on Windows/WSL | Paste image from clipboard | Inserts an image chip at the cursor |
| `Ctrl+B`                     | Background running tasks           | Backgrounds bash commands and agents     |
| `Ctrl+X`, then `Ctrl+K`      | Stop all background agents         | Press the chord twice within 3 seconds to confirm |
| `Ctrl+T`                     | Toggle task checklist              | Stays empty on models newer than Opus 4.7/Sonnet 4.6/Haiku 4.5 unless `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`; `/tasks` is the background-work view |
| `Ctrl+S`                     | Stash or restore the current prompt | Preserves text, cursor, and pasted content |
| `Ctrl+Enter` or `Ctrl+X Ctrl+S` | Send queued messages now           | Sends queued messages and your draft now; running shells and subagents move to the background, otherwise the turn is interrupted; use `Ctrl+X Ctrl+S` if `Ctrl+Enter` arrives as Enter |
| `Ctrl+Z`                     | Suspend Claude Code                | Unix only; `fg` resumes (undo is `Ctrl+_`) |
| `Up/Down arrows`             | Navigate command history           | Recall previous inputs                   |
| `Left/Right arrows`          | Cycle through dialog tabs          | Navigate between tabs in dialogs         |
| `←` on an empty prompt       | Open agent view                    | Backgrounds the session and opens `claude agents`; detaches an attached session |
| `Esc`                        | Interrupt Claude, or close a dialog | Stops the current response or tool call, keeping work so far; declines a permission prompt |
| `Esc` + `Esc`                | Clear the draft, or rewind         | With text, clears it (`Up` recalls it); on an empty prompt, opens the rewind menu to restore or summarize code and conversation |
| `Shift+Tab` (or `Alt+M`)     | Cycle enabled permission modes     | Includes Manual, Accept Edits, Plan, and enabled Auto/Bypass modes; `Alt+M` is a Windows fallback |
| `Option+P` (macOS) / `Alt+P` | Switch model                       | Switch models without clearing prompt    |
| `Option+T` (macOS) / `Alt+T` | Toggle extended thinking           | No effect on Opus 5.5, Sonnet 5.5, Haiku 5.5, or Fable models, which always think; works on macOS without Option as Meta |
| `Option+O` (macOS) / `Alt+O` | Toggle fast mode                   | Enable/disable supported fast mode       |

> [!Tip]
> **Custom shortcuts:** run `/keybindings` to open `~/.claude/keybindings.json`, whose `bindings` array holds blocks like `{ "context": "Chat", "bindings": { "ctrl+e": "chat:externalEditor", "ctrl+s": null } }` (`null` unbinds). Changes apply without a restart; `Ctrl+C`/`Ctrl+D` are reserved and vim keys can't be remapped.

> [!Note]
> **Fullscreen rendering** (flicker-free, with mouse support) is the default for most new installs. Switch with `/tui fullscreen` or `/tui default` (`/tui` alone shows the active renderer), or set `CLAUDE_CODE_NO_FLICKER=1`/`0` per launch. In its transcript viewer, `?` lists the extra keys.

<h3 id="text-editing">Text Editing</h3>

| Shortcut               | Description                  | Context                               |
| :--------------------- | :--------------------------- | :------------------------------------ |
| `Ctrl+K`               | Delete to end of line        | Stores deleted text for pasting       |
| `Ctrl+U`               | Delete to start of line      | Stores deleted text; repeat to clear across lines in multiline input |
| `Ctrl+W`               | Delete back to whitespace    | Removes a whole path or `--flag=value` in one press |
| `Ctrl+Y`               | Paste deleted text           | Pastes text last deleted with Ctrl+K/U/W or Alt+D |
| `Alt+Y` (after Ctrl+Y) | Cycle paste history          | Cycle through previously deleted text |
| `Alt+B`                | Move cursor back one word    | Requires Option as Meta on macOS      |
| `Alt+F`                | Move cursor forward one word | Stops at word end (`_`, `.`, `/` separate words); requires Option as Meta on macOS |
| `Alt+D`                | Delete to end of word        | Stores deleted text; requires Option as Meta on macOS |
| `Ctrl+_`               | Undo last input edit         | Also `Ctrl+Shift+-` |

<h3 id="multiline-input">Multiline Input</h3>

| Method           | Shortcut       | Context                           |
| :--------------- | :------------- | :-------------------------------- |
| Quick escape     | `\` + `Enter`  | Works in all terminals            |
| Option key       | `Option+Enter` | macOS, after enabling Option as Meta (see tip below) |
| Shift+Enter      | `Shift+Enter`  | Native in iTerm2, WezTerm, Ghostty, Kitty, Warp, Apple Terminal, and Windows Terminal; see tip below for others |
| Control sequence | `Ctrl+J`       | Line feed character for multiline |
| Paste mode       | Paste directly | For code blocks, logs             |

> [!Tip]
> Run `/terminal-setup` once for Shift+Enter in VS Code, Cursor, Zed, and Alacritty before 0.16 (foot, Alacritty 0.16+, and other kitty-protocol terminals work natively); gnome-terminal and JetBrains terminals have none, so use `Ctrl+J`. In tmux, add `set -s extended-keys on` and `set -as terminal-features 'xterm*:extkeys'` to `~/.tmux.conf`. `Option+` shortcuts on macOS need Option as Meta (Terminal.app: Settings → Profiles → Keyboard; iTerm2: Option keys to "Esc+"; VS Code: `"terminal.integrated.macOptionIsMeta": true`).

<h3 id="quick-commands">Quick Commands</h3>

| Shortcut     | Description       | Notes                                 |
| :----------- | :---------------- | :------------------------------------ |
| `/` at start | Command or skill  | See built-in commands and skills      |
| `!` at start | Shell mode        | Runs the command and Claude responds to its output; `"respondToBashCommands": false` only adds it to context |
| `@`          | File or session mention | Autocompletes file paths; after a letter, also suggests your other live sessions for Claude to message |
| `?` on empty input | Shortcut help     | Toggles the shortcut help panel |

> [!Tip]
> **PDF Page Ranges:** For PDFs over 10 pages, the Read tool takes one page or range per call in its `pages` parameter (e.g., `pages: "1-5"`, up to 20 pages; comma lists like `"6,9,15"` error). Page reads need `pdftoppm` (`brew install poppler` / `apt-get install poppler-utils`). Large PDFs (>10 pages) return a lightweight reference when @-mentioned instead of being inlined.

> [!Tip]
> **Voice and spelling:** `/voice` turns on dictation (hold `Space` to record, or `/voice tap` to tap to start and again to send); it needs a Claude.ai login and a local mic, so not API-key/Bedrock/Agent Platform/Foundry auth, SSH, or cloud sessions. `"spellcheck": { "enabled": true }` in `~/.claude/settings.json` underlines misspellings (needs `aspell`, `hunspell`, or `ispell`).

<h2 id="vim-mode">Vim Mode</h2>

> [!Note]
> Enable vim-style editing from `/config` -> Editor mode, or set `"editorMode": "vim"` in `~/.claude/settings.json`. Add `"vimInsertModeRemaps": { "jj": "<Esc>" }` to make a two-key INSERT sequence act as Escape (ignored in project settings).

<h3 id="vim-mode-switching">Vim Mode Switching</h3>

| Command | Action                      | From mode |
| :------ | :-------------------------- | :-------- |
| `Esc` or `Ctrl+[` | Enter NORMAL mode           | INSERT, VISUAL |
| `i`     | Insert before cursor        | NORMAL    |
| `I`     | Insert at beginning of line | NORMAL    |
| `a`     | Insert after cursor         | NORMAL    |
| `A`     | Insert at end of line       | NORMAL    |
| `o`     | Open line below             | NORMAL    |
| `O`     | Open line above             | NORMAL    |
| `v` / `V` | Visual selection (character / line); `d`, `y`, `c`, `p`, `>`/`<`, `~`/`u`/`U`, `J` act on it | NORMAL |

<h3 id="vim-navigation">Vim Navigation</h3>

| Command         | Action                    |
| :-------------- | :------------------------ |
| `h`/`j`/`k`/`l` | Move left/down/up/right   |
| `w`             | Next word                 |
| `e`             | End of word               |
| `b`             | Previous word             |
| `0`             | Beginning of line         |
| `$`             | End of line               |
| `^`             | First non-blank character |
| `gg`            | Beginning of input        |
| `G`             | Beginning of last line    |
| `f`/`F`/`t`/`T` + char | Jump to, or just before/after, a character on the line; `;` / `,` repeat / reverse |
| `%`             | Matching `()`, `[]`, or `{}` bracket (also with `d`/`c`/`y`) |
| `/`             | Reverse history search (same as `Ctrl+R`) |

<h3 id="vim-editing">Vim Editing</h3>

| Command        | Action                  |
| :------------- | :---------------------- |
| `x`            | Delete character        |
| `dd`           | Delete line             |
| `D`            | Delete to end of line   |
| `dw`/`de`/`db` | Delete word/to end/back |
| `cc`           | Change line             |
| `C`            | Change to end of line   |
| `cw`/`ce`/`cb` | Change word/to end/back |
| `r{char}`, `s`/`S` | Replace character; substitute character/line |
| `yy`/`Y`, `yw`/`ye`/`yb` | Yank line, word/to end/back |
| `p` / `P`      | Paste after / before cursor |
| `>>` / `<<`, `J` | Indent / dedent line; join lines |
| `ciw`, `di"`, `ya(` … | Text objects: `i`/`a` + `w`, `W`, `"`, `'`, `(`, `[`, or `{`, with `d`/`c`/`y` |
| `u` / `.`      | Undo / repeat last change |

> [!Tip]
> Enter still submits your prompt in INSERT mode, unlike standard Vim. Use `o`/`O` in NORMAL mode, or `Ctrl+J`, to insert a newline.

<h2 id="command-history">Command History</h2>

Claude Code keeps a history of the prompts you type (in `~/.claude/history.jsonl`), and Up-arrow recall also reaches earlier sessions of the same project:

* History is stored per working directory
* `/clear` doesn't erase history; recall lists the new session's prompts first, then earlier ones
* Up/Down (or `Ctrl+P`/`Ctrl+N`) first move the cursor within a multiline prompt, then step through history
* **Ctrl+R** is built in and works in any terminal: the inline search covers all projects (`Ctrl+R` again for older matches, `Tab`/`Esc` to accept, `Enter` to accept and run). In fullscreen it opens a dialog where `Ctrl+S` cycles the scope (session, project, all projects)
* **Drafts cleared with `Ctrl+C`** come back with `Up`; the last ten, with pasted text and images, are kept until you exit
* History expansion with `!` is disabled by default

---

<h1 id="advanced-features">Advanced Features</h1>

<h2 id="thinking-keywords">Thinking Keywords</h2>

> [!Note]
> **`ultrathink` is the only documented prompt keyword for a one-turn request for deeper reasoning.** Phrases such as `think`, `think hard`, and `think harder` are ordinary prompt text; they are not graduated Claude Code controls.

Use `/effort` for an explicit session setting. `ultrathink` adds an in-context instruction for that turn without changing your saved effort level. Typed at the terminal prompt on Opus 5.5, Sonnet 5.5, Haiku 5.5, or Fable 5.1 through Anthropic's API (v2.1.311+), it can also raise that turn to `xhigh`; the word turns rainbow-colored when it can. Elsewhere, such as on Bedrock, set `/effort` instead.

```md
Ultrathink. Propose a step-by-step strategy to fix flaky payment tests and add guardrails.
```

<h2 id="effort-levels">Effort Levels</h2>

Use `/effort` to tune how much reasoning the selected model applies before answering. Higher effort levels are best for planning-heavy work, deep reviews, and long-context tasks.

```bash
/effort            # Slider: Enter saves for this model, s = this session only, Tab toggles Ultracode
/effort low        # Faster, lighter reasoning
/effort medium     # Balanced; default on Opus 5.5, Sonnet 5.5, and Haiku 5.5
/effort high       # Deeper planning and review; default on most other models
/effort xhigh      # Deeper reasoning at higher token spend; default on Opus 4.7
/effort max        # Session-only maximum; test for diminishing returns
/effort ultracode  # Workflow orchestration for this session at the current level ("off" to stop)
/effort auto       # Clear the saved level and return to the model's default
```

Available levels depend on the model. `/effort` saves a level per model (under `modelSettings`); the `effortLevel` setting accepts `low` through `xhigh` as the fallback for models without one, though a top-level `effortLevel` in user settings doesn't apply to Opus 5.5. `max` normally applies only to the current session, although `CLAUDE_CODE_EFFORT_LEVEL=max` can force it for sessions launched with that environment variable. `maxEffortLevel` caps effort on every provider. Ultracode is a toggle, not an effort level: with it on, Claude orchestrates dynamic workflows for substantive tasks at the session's current level. Set `"ultracode": true` in settings to start every session with it; `claude --effort ultracode` turns it on and also sets `xhigh`. It requires workflows and an xhigh-capable model. Prefer the lowest effort that reliably solves the task because higher effort increases latency and token use.

<h2 id="advisor-tool">Advisor Tool (Experimental)</h2>

The advisor pairs the main model with a second, at-least-as-capable model that Claude may consult at important planning, debugging, or completion decisions. Each consultation sends the full conversation, including tool calls and results; it counts toward subscription usage or is billed at the advisor model's API rates.

```bash
/advisor             # Open the picker and save the user default
/advisor opus        # Save Opus as the advisor
/advisor off         # Clear the saved advisorModel setting
claude --advisor opus # Use Opus for this session without changing the saved default
```

The feature runs through the first-party Anthropic API, for subscription or API-billed accounts; it is unavailable on Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, and opt-in on Claude Platform on AWS (v2.1.300+), where no advisor runs until you pick one. Claude decides when to consult it. `advisorModel` is the persistent settings key, while the intentionally hidden `--advisor` launch flag is session-only; `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` turns the tool off entirely. With Fable access you can pick Fable as the advisor (the only advisor a Fable main model accepts); where Fable bills to usage credits, accept that once with `/model fable` first. See the [advisor guide](https://code.claude.com/docs/en/advisor) for supported main/advisor pairings.

<h2 id="fast-mode">Fast Mode</h2>

> [!Note]
> **Fast mode runs the same Opus model and capabilities up to 2.5× faster at a higher price per token, without trading model quality for speed. It is generally available on Opus 5.5 and in research preview on Opus 5 and Opus 4.8.**

```bash
/fast          # Space toggles, Enter confirms and saves your fastMode default
/fast on       # Turn it on directly (session-only in cloud sessions)
# Option+O on macOS or Alt+O on Windows/Linux also toggles it
```

Fast mode supports **Opus 5.5** (the default fast-mode model), **Opus 5**, and **Opus 4.8**, at \$8/\$40 per MTok input/output on Opus 5.5 and \$10/\$50 on the other two. It is unavailable for Sonnet, Haiku, and Opus 4.7, and on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and Claude Platform on AWS. VS Code has a **Toggle fast mode** command, and claude.ai/code has a Fast mode switch in the model menu. Subscription users need usage credits; Team and Enterprise also require Owner enablement. Use it for latency-sensitive interactive work, and standard mode for cost-sensitive or long autonomous tasks. Lower `/effort` is the separate control that may trade reasoning depth for speed.

<h2 id="auto-mode">Auto Mode</h2>

Auto mode lets Claude evaluate and approve lower-risk actions automatically while still blocking or asking on higher-risk operations. It is useful for trusted development loops where repeated permission prompts slow down work.

```bash
# Start in auto mode, or cycle to it with Shift+Tab
claude --permission-mode auto

# Inspect the built-in and effective classifier configuration
claude auto-mode defaults
claude auto-mode config
claude auto-mode critique    # AI feedback on your custom rules

# Remove a cached/custom classifier config and return to defaults
claude auto-mode reset       # Add --yes to skip confirmation
```

```json
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: github.example.com/acme-corp and all repos under it"
    ],
    "hard_deny": [
      "$defaults",
      "Never send repository contents to third-party code-review APIs"
    ]
  }
}
```

Key points:

- Auto mode is available on every supported provider (on Bedrock, Agent Platform, and Foundry only with Sonnet 5+, Opus 4.7+, Haiku 5.5, and Fable models); `CLAUDE_CODE_ENABLE_AUTO_MODE` is a no-op compatibility variable. With no mode configured, interactive terminal and VS Code sessions start in auto mode where it's available (otherwise Manual), while `claude -p` and Agent SDK runs start in `default` (Manual). Choose another starting mode with `--permission-mode` or `permissions.defaultMode`; `disableAutoMode: "disable"` in managed settings removes auto mode.
- The classifier trusts the working directory and current repository remotes by default. Add organization infrastructure under `autoMode.environment` only when needed; `/auto-mode-setup` drafts entries from your project and recent sessions, and `/permissions` has an **Auto mode** tab for viewing and editing rules.
- Put `autoMode` in user settings, managed settings, or `--settings`. Repository `.claude/settings.json` and `.claude/settings.local.json` cannot inject classifier policy.
- Include `"$defaults"` in `allow`, `soft_deny`, `hard_deny`, or `environment` to extend the built-in rules. An array without it replaces that section's built-in list, so an empty `hard_deny` drops the built-in data-exfiltration rule.
- Where supported, classifier checks run server-side at no extra charge (`/status` shows an **Auto mode server** row). Behind a gateway or proxy that blocks them, Claude Code makes its own classifier requests, which count toward usage; `CLAUDE_CODE_AUTO_MODE_SERVER=0` forces that.
- Explicit `permissions.deny` and content-scoped `permissions.ask` rules are evaluated before the classifier. Use those for non-negotiable blocks or human checkpoints.

<h2 id="plan-mode">Plan Mode</h2>

> [!Note]
> **Plan Mode tells Claude to research and propose changes without editing your source, and is designed for exploration, planning, and review. It permits read-only shell exploration; when auto mode is available and `useAutoModeDuringPlan` is on (the default), the classifier reviews other commands instead of prompting.**

Plan Mode is a workflow mode, not a hard isolation boundary. In interactive terminal sessions where bypass permissions is available (such as with `--dangerously-skip-permissions`), its blocks aren't enforced: Claude is still told not to edit, but edits and commands it attempts run without prompting (explicit ask rules and critical-path `rm`/`rmdir` removals still prompt). Use sandboxing plus explicit deny/ask rules or managed policy when command execution must be technically constrained.

When the plan is ready, choose **Yes, and use auto mode** (**Yes, auto-accept edits** without auto mode), **Yes, manually approve edits**, or **No, keep planning**; `Ctrl+G` opens it in your editor first.

**When to use Plan Mode:**

- **Multi-step implementation**: When your feature requires making edits to many files
- **Code exploration**: When you want to research the codebase thoroughly before changing anything
- **Interactive development**: When you want to iterate on the direction with Claude

**How to enable Plan Mode:**

```bash
# Start a new session in Plan Mode
claude --permission-mode plan

# Or toggle during session with Shift+Tab
# (cycles through Manual, Accept Edits, Plan, and any other enabled modes)

# Enter plan mode from the prompt
/plan

# Run headless queries in Plan Mode
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

**Configure Plan Mode as default:**

In `.claude/settings.json`:

```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

---

<h2 id="background-tasks">Background Tasks</h2>

> [!Note]
> **Claude Code supports background commands and full background sessions, allowing you to continue working while long-running processes or agents execute.**

**How to use background tasks:**

| Method | Description |
| :----- | :---------- |
| Prompt Claude | Ask Claude to run a shell command or subagent in the background |
| `Ctrl+B` | Move a running Bash tool invocation or agent to the background (tmux users press twice) |
| `/background` (`/bg`) | Detach this entire conversation and free the terminal |
| `←` on an empty prompt | Background this session and open agent view (`leftArrowOpensAgents` in `/config` turns this off) |
| `/fork` | Copy this conversation into a worktree-isolated background session while you stay here |
| `claude --bg` | Launch a new background Claude session; it cannot be combined with `-p` |
| `! <command>` in `claude agents` | Start an attachable background shell session from agent view |

**Key features:**

- Output is buffered and can be read from the persisted background output file path
- The Monitor tool lets Claude stream a background script's output line by line instead of polling with `sleep`
- In unattended sessions (`-p`, Agent SDK, CI, cloud), background shell commands stop at their `timeout` (default 30 minutes, or 10 in a `-p` run given a text prompt; max 2 hours); interactive sessions have no limit
- Background tasks have unique IDs for tracking and output retrieval
- `/tasks` shows background shells, subagents, and long-running tool calls owned by the current session
- Background sessions appear in `/resume` and the `claude agents` dashboard, marked with `bg`; use `claude attach/logs/stop/rm/respawn <id>` to manage them
- Use `claude agents --json` for scripts, status bars, session pickers, and tmux integrations
- Background sessions preserve completed work with commits/pushes, and open a draft PR only when the task calls for one

**Common backgrounded commands:**

- Build tools (webpack, vite, make)
- Package managers (npm, yarn, pnpm)
- Test runners (jest, pytest)
- Development servers
- Long-running processes (docker, terraform)

**Bash mode with `!` prefix:**

```bash
# Run bash commands directly without Claude interpretation
! npm test
! git status
! ls -la

# Run a command as an attachable background session
claude --bg --exec "npm test"

# Name a background session
claude --bg --name nightly-check "run the full verification suite"

# Detach or copy the current conversation
/background "finish the verification and report back"
/fork "investigate the flaky integration test" # Runs in its own worktree
```

**Disable background tasks:**

```bash
# Remove run_in_background and Ctrl+B for shells and subagents
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1

# Also turn off background sessions: claude agents, --bg, /background
export CLAUDE_CODE_DISABLE_AGENT_VIEW=1   # or "disableAgentView": true in settings
```

---

<h2 id="workflows--scheduling">Workflows & Scheduling</h2>

Dynamic workflows coordinate many background agents for larger work than a single foreground turn can comfortably handle. Ask for one in your own words ("use a workflow to…") or include `ultracode` in your prompt, then use `/workflows` to inspect runs and status. `/deep-research <question>` is built in, and pressing `s` on a run in `/workflows` saves its script (to `.claude/workflows/` or `~/.claude/workflows/`) as a reusable `/<name>` command. On Pro, turn workflows on in `/config` first.

```bash
/workflows
/goal "the migration is implemented, tested, and documented"
/loop 15m "check the deployment dashboard and summarize any incidents"
```

| Feature      | Purpose                                                                                 |
| :----------- | :-------------------------------------------------------------------------------------- |
| `/workflows` | View workflow runs that orchestrate many agents in the background                       |
| `/goal`      | Give Claude a completion condition and let it continue across turns until it is reached |
| `/loop`      | Run a prompt or slash command on an interval, or omit it to let Claude self-pace        |
| `/schedule`  | Create and manage cloud scheduled tasks that run without your machine                   |

Use workflows for broad, decomposable efforts. Use `/goal` for a single outcome that may require several turns. Use `/loop` for monitoring within an open session; loops expire after 7 days, `Esc` stops a self-paced loop while it waits, and you ask Claude to cancel a fixed-interval one. Use `/schedule` or Desktop scheduled tasks for schedules that must run without an open session.

The default `workflowSizeGuideline` is **medium** (fewer than 10 agents), or **small** (fewer than 5) on Pro; `large` aims for fewer than 50, and `unrestricted` lets Claude decide. It is advice, not a cap; the runtime separately limits a run to 16 concurrent agents by default (`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, 1–256) and 1,000 in total. Change it through `/config` only when the work genuinely benefits from a smaller or larger fan-out.

---

<h2 id="remote-sessions">Cloud Sessions</h2>

> [!Note]
> **For eligible subscribers: use `--cloud` to start a cloud session on claude.ai and `--teleport` to copy a cloud session into a local checkout. `--remote` remains only as a deprecated alias for `--cloud`.**

**Start a cloud session:**

```bash
# Create a new cloud session on claude.ai with task description
claude --cloud "Fix the login bug"
```

The cloud VM clones your GitHub remote at the current branch, not your local checkout, so push local commits first. With no git remote, or when the Claude GitHub App isn't installed on the GitHub repository, Claude Code uploads a bundle of your local repository instead (untracked files are left out; `CCR_FORCE_BUNDLE=1` forces a bundle, for example for a GitLab or Bitbucket repository). Queue a follow-up into a running cloud session with `claude -p "next step" --cloud <session-id>`. `--cloud` and `--teleport` need a claude.ai sign-in (`claude auth login`) and an organization that allows cloud sessions; they aren't available through Bedrock, Google Cloud's Agent Platform, or other third-party providers.

**Resume a cloud session locally:**

```bash
# Resume a cloud session in your local terminal (omit the ID for a session picker)
claude --teleport <session-id>

# Or, inside a running session, use the slash command (alias /tp)
/teleport
```

Teleport needs a clean working tree (it offers to stash), a checkout of the same repository (not a fork), the session's branch pushed to the remote, and the same claude.ai account. The terminal gets its own copy of the session: local work doesn't sync back, and a compacted cloud session arrives as its summary.

**Cloud environments and PR auto-fix:** each cloud session runs in a [cloud environment](https://code.claude.com/docs/en/cloud-environments) that sets its network access (default **Trusted**: package registries and other allowlisted domains only), environment variables, and a setup script that runs before Claude starts. If an install or WebFetch fails in a cloud session, check the network level first; `/remote-env` picks the default environment for `--cloud`. On a PR's branch, `/autofix-pr` starts a cloud session that watches the PR and pushes fixes for CI failures and review comments (needs `gh` and the Claude GitHub App on the repository).

Team and Enterprise organizations can also run cloud sessions on infrastructure they control (self-hosted environments, public beta, off by default). An Owner turns on **Allow self-hosted environments** on the claude.ai **Cloud environments** admin page and creates an environment, then starts a runner on a Linux or macOS host with `claude self-hosted-runner setup` (guided) or `claude self-hosted-runner --environment-secret-file <file> --base-dir <dir>`. Developers pick the environment in claude.ai/code or dispatch with `claude -p "your task" --environment ccpool_...`; see the [self-hosted environments guide](https://code.claude.com/docs/en/self-hosted-environments).

---

<h2 id="claude-in-chrome">Claude in Chrome</h2>

With the [Claude in Chrome extension](https://code.claude.com/docs/en/chrome), Claude Code can drive browser-based testing and UI verification from the CLI.

**Setup:**

```bash
claude --chrome                    # Launch with Chrome integration
/chrome                            # Status, reconnect, site permissions, browser choice, "Enabled by default"
```

**Capabilities:**

- Navigate to URLs, click elements, fill forms
- Take screenshots and analyze page content
- Execute JavaScript in the browser context
- Interact with web applications for testing
- Read console errors and DOM state for live debugging
- Upload local files to page upload fields (up to 10 MB per upload; files denied to `Read` are refused)
- Record interactions as GIFs and save screenshots to disk

> [!NOTE]
> Requires Chrome, Edge, or another Chromium browser (Brave, Arc, Vivaldi, Opera), the Claude in Chrome extension v1.0.36+, and a claude.ai subscription sign-in (API keys and `claude setup-token` tokens keep it off). It is unavailable through WSL and third-party model providers, and an organization admin can turn it off. Project settings files can't turn it on; use `--chrome` or **Enabled by default** in `/chrome`, a setting shared with the VS Code extension. Review the extension's site permissions before granting access; in auto mode, classifier-approved browser calls skip the extension's per-site check, so add permission deny rules for sites Claude must never act on.

---

<h2 id="desktop-and-ides">Desktop and IDEs</h2>

The Claude Desktop Code tab supports macOS, Windows (including sessions inside a WSL 2 distribution), and a Linux beta for Ubuntu/Debian. It provides parallel local or cloud sessions, worktrees, diffs, an editor, terminal, and browser; SSH execution is also available. Desktop and the CLI share CLAUDE.md files, settings, hooks, skills, and MCP servers from `~/.claude.json` and `.mcp.json`, but each keeps its own session list. Desktop's local Code tab sessions also load MCP servers from `claude_desktop_config.json`, which the CLI ignores; on macOS and WSL, `claude mcp add-from-claude-desktop` copies them into `~/.claude.json`. Agent teams are not supported in Desktop.

Run `/desktop` to move the current terminal session into the app, or `claude --desktop` (v2.1.285+) to open Desktop from your shell on the current directory, or on a session with `--continue` or `--resume <session-id>`. Both need macOS or x64 Windows and a Claude subscription sign-in.

**Computer use** (research preview, Pro and Max plans) lets Claude open native apps, click, type, and take screenshots when no MCP server, shell command, or Claude in Chrome can reach a tool. Turn it on in Desktop Settings (macOS and Windows) or, in the macOS CLI, enable the built-in `computer-use` server in `/mcp` and grant Accessibility and Screen Recording. Claude asks before controlling each app; it needs an interactive session and isn't available through third-party providers.

The VS Code extension requires VS Code 1.94+ and bundles a CLI for its panel; install the standalone CLI separately for terminal use. Cursor and compatible Open VSX forks are supported. Its Focus view hides tool calls, tool results, and thinking behind expandable rows (`Ctrl+Alt+F`, or `Ctrl+Option+F` on Mac). Its settings include **Enable Remote Control for all sessions**, and `claudeCode.attachSelection` and `claudeCode.attachOpenFile` control whether your editor selection and open file are added to messages. The JetBrains plugin (IntelliJ IDEA, PyCharm, WebStorm, GoLand, Android Studio, and others) doesn't bundle the CLI: install `claude` separately and run it in the IDE's integrated terminal, or connect from an external terminal with `/ide`. For JetBrains Remote Development, install the plugin on the remote host.

**Slack:** Team and Enterprise organizations bring @Claude into Slack channels with [Claude Tag](https://claude.com/docs/claude-tag/overview) (public beta), which works as the organization's shared identity with admin-configured access to repositories, connectors, and skills, under an organization spend limit. On Pro and Max, in a workspace no organization has connected to Claude Tag, the earlier [Claude Code in Slack](https://code.claude.com/docs/en/slack) app (`/install-slack-app`) turns @Claude coding requests into cloud sessions under your own account and plan limits.

See the current [Desktop](https://code.claude.com/docs/en/desktop), [VS Code](https://code.claude.com/docs/en/vs-code), [JetBrains](https://code.claude.com/docs/en/jetbrains), and [computer use](https://code.claude.com/docs/en/computer-use) documentation for platform-specific setup.

---

<h2 id="sandbox-mode">Sandbox Mode</h2>

Sandboxing is an OS-enforced boundary for the shell commands Claude runs (Bash, PowerShell, and Monitor) and the processes they start; Claude's file tools, MCP servers, and hooks run outside it, and it is separate from Claude Code's tool-permission rules. It is off by default: turn it on with `/sandbox` or `"sandbox": { "enabled": true }` in `~/.claude/settings.json`, then pick **auto-allow** (sandboxed commands run without prompting) or **regular permissions** on the `/sandbox` Mode tab. With default settings, sandboxed commands can write inside the working directory and temporary directories, read broadly except for denied paths, and reach the network only through a hostname-filtering proxy.

```bash
/sandbox # Inspect dependencies and configure filesystem/network isolation
```

Platform support:

- macOS uses Seatbelt.
- Linux and WSL 2 use bubblewrap plus socat (`sudo apt-get install bubblewrap socat` on Ubuntu/Debian). On Ubuntu 24.04+, if `sysctl kernel.apparmor_restrict_unprivileged_userns` returns `1`, AppArmor stops bubblewrap from creating user namespaces; add an AppArmor profile for `bwrap` (`/sandbox` and the startup warning explain how).
- Native Windows and WSL 1 do not support sandboxing.

Useful hardening settings include `sandbox.failIfUnavailable: true` to fail closed, `sandbox.allowUnsandboxedCommands: false` (**Strict sandbox mode** on the `/sandbox` Overrides tab) to remove the unsandboxed retry path, `sandbox.network.strictAllowlist: true` for an exact network allowlist, and credential rules with `mode: "deny"` or `mode: "mask"`. Commands you type at the `!` prompt run outside the sandbox even in strict mode, except in background sessions and Linux sessions with `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` set. Put tools that can't run sandboxed, such as `docker`, in `sandbox.excludedCommands` (for example `"docker compose *"`); they run with your full access, so keep patterns narrow. On Linux, `sandbox.allowNestedUserNamespaces: true` in `~/.claude/settings.json` (v2.1.305+) lets Chromium's or Electron's own sandbox, a nested bubblewrap, or `unshare` run inside the sandbox, but it turns off a security boundary; it isn't enough for rootless Podman or Buildah, which need `sandbox.excludedCommands` instead.

Masking credential files works on Linux and WSL 2; on macOS a masked file is blocked like `deny`. Every `mask` entry needs `sandbox.network.tlsTerminate`, or the placeholder reaches the server unchanged and authentication fails (`claude doctor` warns `TLS termination is unavailable`). Masks can also extract structured values, mask selected JWT claims, and re-sign AWS SigV4 requests. `mask` entries, `network.tlsTerminate`, `credentials.allowPlaintextInject`, `awsPairs`, and `sigv4` are honored only from user, managed, or `--settings` configuration, never from a repository's `.claude/settings.json` or `.claude/settings.local.json`. Sandboxing reduces the impact of shell commands; it is not a substitute for reviewing permissions and secrets exposure.

---

<h2 id="lsp-tool">LSP Tool (Language Server Protocol)</h2>

Claude Code integrates with language servers to provide IDE-level code intelligence:

- **Diagnostics after edits** — Type errors and warnings go back to Claude automatically after each file edit (`Found N new diagnostic issues`; Ctrl+O expands them)
- **Go to Definition** — Jump to where a symbol is defined
- **Find References** — Find all usages of a symbol across the codebase
- **Hover Information** — Get type information and documentation
- **Symbols and call hierarchy** — List file or workspace symbols, find implementations, and trace call hierarchies

LSP support is provided by plugins. Install the language-server binary separately, then install its LSP plugin from the official marketplace with `/plugin`; for TypeScript, run `npm install -g typescript-language-server typescript`, then `/plugin install typescript-lsp@claude-plugins-official`. A server merely being present on `PATH` is not enough, though Claude Code may then offer the matching plugin. This enables Claude to navigate codebases more precisely than text search alone. Plugin language servers don't start in cloud sessions, so the LSP tool is inactive there.

> Large tool results are saved to a file, and Claude gets a preview plus the path. This applies to successful Bash output over about 30,000 characters (adjustable up to 128,000 with the `bashOutputMaxChars` setting) and to MCP results over the limits described under [MCP Integration](#mcp-integration).

---

<h2 id="sub-agents">Sub Agents</h2>

> Sub‑Agents are purpose‑built helpers with their **own prompts, tools, and isolated context windows**. Treat this like a "mixture‑of‑experts" you **compose** per repo.

<h3 id="built-in-subagents">Built-in Subagents</h3>

Claude Code includes built-in subagents that Claude automatically uses when appropriate:

| Subagent | Model | Tools | Purpose |
| :------- | :---- | :---- | :------ |
| **Explore** | Inherits the parent model (Opus under a Fable parent, except on Bedrock, Agent Platform, Foundry, and similar providers) | Read-only | File discovery, code search, and codebase exploration |
| **Plan** | Inherits the parent model | Read-only | Planning complex changes without making edits |
| **General-purpose** | Inherits the parent model | Inherited | General task delegation |

> Claude delegates to **Explore** when it needs to search or understand a codebase without making changes, keeping exploration results out of your main conversation context.

Explore and Plan start without your `CLAUDE.md` files or git status and can't be resumed. Set `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` to remove both, or deny one with `Agent(Explore)` in `permissions.deny`.

**When to use subagents:**

> - You need high signal responses (plans, reviews, diffs) without side quests.
> - You want version‑controlled prompts and tool policies alongside the codebase.
> - You work in PR‑driven teams and want scoped edits by role.
> - The task produces verbose output you don't need in your main context.

<h3 id="each-sub-agent-has-its-own-context">Each Sub‑Agent Has Its Own Context</h3>

**Design rules for your lineup**

> - Define **one clear responsibility** per agent.
> - Keep the **minimum** tool set needed for that role.
> - Prefer **read‑only** agents for analysis/review tasks.
> - Give edit powers to as few agents as possible.

<h3 id="configure-agents">Configure Agents</h3>

> Keep agents **in the project** so they're versioned with the repo and evolve via PRs.

<h3 id="agents-quick-start">Quick start</h3>

> Ask Claude to create an agent, mention one with `@agent-name`, or edit its Markdown definition directly. `/agents` now prints this guidance; it no longer opens the old wizard.

```bash
claude update
# Project agent: .claude/agents/<name>.md
# Personal agent: ~/.claude/agents/<name>.md

claude --agent code-reviewer "review the current branch"
```

`claude agents` is a separate agent-view dashboard for running, blocked, completed, and background **sessions**. It does not list or configure subagent definitions.

<h3 id="agent-scopes">Subagent Scopes</h3>

| Location | Scope | Priority |
| :------- | :---- | :------- |
| M