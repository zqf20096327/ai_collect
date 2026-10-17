# Claude Code Cheat Sheet

> **Claude Code v2.1.81** · Last updated: March 24, 2026 · By [Wil Waldon](https://wilwaldon.com)

## Install

```bash
npm install -g @anthropic-ai/claude-code
```

Requires Node.js >= 18. Authenticate with `claude` on first run.

## Table of Contents

- [Recent Changes](#recent-changes)
- [Keyboard Shortcuts](#%EF%B8%8F-keyboard-shortcuts)
- [Slash Commands](#-slash-commands)
- [Memory & Files](#-memory--files)
- [MCP Servers](#-mcp-servers)
- [Workflows & Tips](#-workflows--tips)
- [Config & Env](#%EF%B8%8F-config--env)
- [Skills & Agents](#-skills--agents)
- [CLI & Flags](#%EF%B8%8F-cli--flags)
- [Permission Modes](#permission-modes)

---

## Recent Changes

- `--bare` flag — minimal headless mode (no hooks/LSP/plugins)
- `--channels` — permission relay & MCP push messages (preview)
- `effort` frontmatter for skills & slash commands
- `/fork` renamed to `/branch` (alias kept)
- `SendMessage` auto-resumes stopped agents

---

## ⌨️ Keyboard Shortcuts

### General Controls

| Shortcut | Action |
|----------|--------|
| `Ctrl C` | Cancel input/generation |
| `Ctrl D` | Exit session |
| `Ctrl L` | Clear screen |
| `Ctrl O` | Toggle verbose output |
| `Ctrl R` | Reverse search history |
| `Ctrl G` | Open prompt in editor |
| `Ctrl B` | Background running task |
| `Ctrl T` | Toggle task list |
| `Ctrl V` | Paste image |
| `Ctrl F` | Kill background agents (×2) |
| `Esc Esc` | Rewind / undo |

### Mode Switching

| Shortcut | Action |
|----------|--------|
| `Shift Tab` | Cycle permission modes |
| `Alt P` | Switch model |
| `Alt T` | Toggle thinking |

### Input

| Shortcut | Action |
|----------|--------|
| `\ Enter` | Newline (quick) |
| `Ctrl J` | Newline (control seq) |

### Prefixes

| Prefix | Action |
|--------|--------|
| `/` | Slash command |
| `!` | Direct bash |
| `@` | File mention + autocomplete |

### Session Picker

| Key | Action |
|-----|--------|
| `↑↓` | Navigate |
| `←→` | Expand/collapse |
| `P` | Preview |
| `R` | Rename |
| `/` | Search |
| `A` | All projects |
| `B` | Current branch |

---

## ⚡ Slash Commands

### Session

| Command | Action |
|---------|--------|
| `/clear` | Clear conversation |
| `/compact [focus]` | Compact context |
| `/resume` | Resume/switch session |
| `/rename [name]` | Name current session |
| `/branch [name]` | Branch conversation (`/fork` alias) |
| `/cost` | Token usage stats |
| `/context` | Visualize context (grid) |
| `/diff` | Interactive diff viewer |
| `/copy` | Copy last response |
| `/export` | Export conversation |

### Config

| Command | Action |
|---------|--------|
| `/config` | Open settings |
| `/model [model]` | Switch model (←→ effort) |
| `/fast [on\|off]` | Toggle fast mode |
| `/vim` | Toggle vim mode |
| `/theme` | Change color theme |
| `/permissions` | View/update permissions |
| `/effort [level]` | Set effort (low/med/high) |
| `/color [color]` | Set prompt-bar color |
| `/keybindings` | Customize keyboard shortcuts |
| `/terminal-setup` | Configure terminal keybindings |

### Tools

| Command | Action |
|---------|--------|
| `/init` | Create CLAUDE.md |
| `/memory` | Edit CLAUDE.md files |
| `/mcp` | Manage MCP servers |
| `/hooks` | Manage hooks |
| `/skills` | List available skills |
| `/agents` | Manage agents |
| `/chrome` | Chrome integration |
| `/reload-plugins` | Hot-reload plugins |
| `/add-dir <path>` | Add working directory |

### Special

| Command | Action |
|---------|--------|
| `/btw <question>` | Side question (no context) |
| `/plan [desc]` | Plan mode (+ auto-start) |
| `/loop [interval]` | Schedule recurring task |
| `/voice` | Push-to-talk voice (20 langs) |
| `/doctor` | Diagnose installation |
| `/rc` | Enable remote control |
| `/pr-comments [PR]` | Fetch GitHub PR comments |
| `/stats` | Usage streaks & prefs |
| `/insights` | Analyze sessions report |
| `/desktop` | Continue in Desktop app |
| `/remote-control` | Bridge terminal to claude.ai/code |
| `/usage` | Plan limits & rate status |
| `/schedule` | Cloud scheduled tasks |
| `/security-review` | Security analysis of changes |
| `/help` | Show help + commands |
| `/feedback` | Submit feedback (alias: `/bug`) |
| `/release-notes` | View full changelog |
| `/stickers` | Order stickers! 🎉 |

---

## 📁 Memory & Files

### CLAUDE.md Locations

| Path | Scope |
|------|-------|
| `./CLAUDE.md` | Project (team-shared) |
| `~/.claude/CLAUDE.md` | Personal (all projects) |
| `/etc/claude-code/` | Managed (org-wide) |

### Rules & Import

| Path / Syntax | Description |
|----------------|-------------|
| `.claude/rules/*.md` | Project rules |
| `~/.claude/rules/*.md` | User rules |
| `paths:` frontmatter | Path-specific rules |
| `@path/to/file` | Import in CLAUDE.md |

### Auto Memory

```
~/.claude/projects/<proj>/memory/
```

Contains `MEMORY.md` + topic files, auto-loaded per project.

---

## 🔌 MCP Servers

### Add Servers

| Flag | Transport |
|------|-----------|
| `--transport http` | Remote HTTP (recommended) |
| `--transport stdio` | Local process |
| `--transport sse` | Remote SSE |

### Scopes

| Scope | File |
|-------|------|
| Local | `.claude.json` (per project) |
| Project | `.mcp.json` (shared/VCS) |
| User | `~/.claude.json` (global) |

### Manage

| Command | Action |
|---------|--------|
| `/mcp` | Interactive UI |
| `claude mcp list` | List all servers |
| `claude mcp serve` | CC as MCP server |
| Elicitation | Servers request input mid-task |

---

## 🧠 Workflows & Tips

### Plan Mode

| Input | Action |
|-------|--------|
| `Shift Tab` | Normal → Auto-Accept → Plan |
| `--permission-mode plan` | Start in plan mode |

### Thinking & Effort

| Input | Action |
|-------|--------|
| `Alt T` | Toggle thinking on/off |
| `"ultrathink"` | Max effort for turn |
| `Ctrl O` | See thinking (verbose) |
| `/effort` | ○ low · ◐ med · ● high |

### Git Worktrees

| Input | Action |
|-------|--------|
| `--worktree name` | Isolated branch per feature |
| `isolation: worktree` | Agent in own worktree |
| `sparsePaths` | Checkout only needed dirs |
| `/batch` | Auto-creates worktrees |

### Voice Mode

| Input | Action |
|-------|--------|
| `/voice` | Enable push-to-talk |
| `Space` (hold) | Record, release to send |
| 20 languages | EN, ES, FR, DE, CZ, PL… |

### Context Management

| Input | Action |
|-------|--------|
| `/context` | Usage + optimization tips |
| `/compact [focus]` | Compress with focus |
| Auto-compact | Triggers at ~95% capacity |
| 1M context | Opus 4.6 (Max/Team/Ent) |
| `CLAUDE.md` | Survives compaction |

### Session Power Moves

| Input | Action |
|-------|--------|
| `claude -c` | Continue last conversation |
| `claude -r "name"` | Resume by name |
| `/btw question` | Side question, no context cost |

### SDK / Headless

| Input | Action |
|-------|--------|
| `claude -p "query"` | Non-interactive |
| `--output-format json` | Structured output |
| `--max-budget-usd 5` | Cost cap |
| `cat file \| claude -p` | Pipe input |

### Scheduling & Remote

| Input | Action |
|-------|--------|
| `/loop 5m msg` | Recurring task |
| `/rc` | Remote control |
| `--remote` | Web session on claude.ai |

---

## ⚙️ Config & Env

### Config Files

| File | Purpose |
|------|---------|
| `~/.claude/settings.json` | User settings |
| `.claude/settings.json` | Project (shared) |
| `.claude/settings.local.json` | Local only |
| `~/.claude.json` | OAuth, MCP, state |
| `.mcp.json` | Project MCP servers |

### Key Settings

| Setting | Description |
|---------|-------------|
| `modelOverrides` | Map model picker → custom IDs |
| `autoMemoryDirectory` | Custom memory dir |
| `worktree.sparsePaths` | Sparse checkout dirs |

### Key Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | API key |
| `ANTHROPIC_MODEL` | Default model |
| `CLAUDE_CODE_EFFORT_LEVEL` | low/med/high |
| `MAX_THINKING_TOKENS` | 0 = off |
| `ANTHROPIC_CUSTOM_MODEL_OPTION` | Custom `/model` entry |
| `CLAUDE_CODE_PLUGIN_SEED_DIR` | Multiple plugin seed dirs |
| `CLAUDECODE` | Detect CC shell (=1) |
| `IS_DEMO` | Demo mode (hide email/org) |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output tokens (default 32K) |
| `CLAUDE_CODE_DISABLE_CRON` | Disable scheduled tasks |

### Hooks

Hooks run user-defined commands at specific lifecycle events. Configure in settings or via `/hooks`.

| Event | Fires When |
|-------|------------|
| `PreToolUse` | Before a tool executes |
| `PostToolUse` | After a tool executes |
| `Notification` | When Claude sends a notification |
| `Stop` | When Claude finishes a response |
| `SubagentStop` | When a subagent finishes |

---

## 🔧 Skills & Agents

### Built-in Skills

| Command | Action |
|---------|--------|
| `/simplify` | Code review (3 parallel agents) |
| `/batch` | Large parallel changes (5–30 worktrees) |
| `/debug [desc]` | Troubleshoot from debug log |
| `/loop [interval]` | Recurring scheduled task |
| `/claude-api` | Load API + SDK reference |

### Custom Skill Locations

| Path | Scope |
|------|-------|
| `.claude/skills/<name>/` | Project skills |
| `~/.claude/skills/<name>/` | Personal skills |

### Skill Frontmatter

| Key | Description |
|-----|-------------|
| `description` | Auto-invocation trigger |
| `allowed-tools` | Skip permission prompts |
| `model` | Override model for skill |
| `effort` | Override effort level |
| `context: fork` | Run in subagent |
| `$ARGUMENTS` | User input placeholder |
| `${CLAUDE_SKILL_DIR}` | Skill's own directory |
| `` !`cmd` `` | Dynamic context injection |

### Built-in Agents

| Agent | Description |
|-------|-------------|
| Explore | Fast read-only (Haiku) |
| Plan | Research for plan mode |
| General | Full tools, complex tasks |
| Bash | Terminal separate context |

### Agent Frontmatter

| Key | Description |
|-----|-------------|
| `permissionMode` | default/acceptEdits/plan/dontAsk/bypass |
| `isolation: worktree` | Run in git worktree |
| `memory: user\|project` | Persistent memory |
| `background: true` | Background task |
| `maxTurns` | Limit agentic turns |
| `SendMessage` | Resume agents (replaces resume) |

---

## 🖥️ CLI & Flags

### Core Commands

| Command | Action |
|---------|--------|
| `claude` | Interactive |
| `claude "q"` | With prompt |
| `claude -p "q"` | Headless |
| `claude -c` | Continue last |
| `claude -r "n"` | Resume |
| `claude update` | Update |

### Key Flags

| Flag | Action |
|------|--------|
| `--model` | Set model |
| `-w` | Git worktree |
| `-n` / `--name` | Session name |
| `--add-dir` | Add dir |
| `--agent` | Use agent |
| `--allowedTools` | Pre-approve |
| `--output-format` | json/stream |
| `--json-schema` | Structured |
| `--max-turns` | Limit turns |
| `--max-budget-usd` | Cost cap |
| `--console` | Auth via Anthropic Console |
| `--verbose` | Verbose |
| `--bare` | Minimal headless (no hooks/LSP) |
| `--channels` | Permission relay / MCP push |
| `--remote` | Web session |
| `--effort` | low/med/high/max |
| `--permission-mode` | plan/default/… |
| `--dangerously-skip-permissions` | Skip all prompts ⚠️ |
| `--chrome` | Chrome |

---

## Permission Modes

`default` prompts · `acceptEdits` auto-accept edits · `plan` read-only · `dontAsk` deny unless allowed · `bypassPermissions` skip all · `--dangerously-skip-permissions` CLI flag
