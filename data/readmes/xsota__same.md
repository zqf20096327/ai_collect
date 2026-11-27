<p align="center">
  <img src="assets/brand/same-mascot.svg" alt="SAME mascot" width="160">
</p>

# SAME (Shared Agentic Multi-provider Environment)

A lightweight, local-first, multi-provider AI agent desktop workspace written in Rust.

## Features (v0.1)

- **ACP First, Not ACP Only**: Built-in Agent Client Protocol (ACP) v1 client over stdio, plus native CLI adapters for agents without a standalone ACP wrapper installed.
- **Multi-Provider Support**:
  - OpenCode (`opencode acp`)
  - Claude Code (`claude-agent-acp` or native `claude` CLI adapter over bidirectional `stream-json`)
  - Codex (`codex-acp` or native `codex app-server` adapter)
  - Antigravity (`agy acp`)
  - Custom ACP agents (configurable command, args, env, cwd)
- **Structured Workspace**: Organize work into `Workspace -> Project -> Quest -> Session` (with quick sessions supported without forcing hierarchy).
- **Streaming & Tool Visibility**: Real-time streaming responses, collapsible thinking/reasoning blocks, tool call cards, approval cards with diffs and keyboard answers for every provider, question and plan cards, OS notifications while in the background, and file/image attachments.
- **Usage Dashboard**: Plan limits of Claude Code and Codex (5-hour and weekly windows, share used and left, time until reset) in one place, read from the CLIs without spending tokens.
- **Local-First Storage**: All configuration (TOML) and conversation history (SQLite) are stored locally. Zero telemetry, no mandatory account.
- **Built-in Workspace Tools**: File browser, file viewer/editor, and optional Git status/diff viewer for software development projects.
- **Customizable & Bilingual UI**: 4 color themes (Ocean, Classic, Twilight, Sakura), each with dark and light variants, configurable UI/monospace fonts and font size, configurable submit key, and Japanese/English UI support.
- **In-App Updates**: Built-in updater that checks GitHub Releases and updates in place (`same --version` / `-V` to print the installed version).

## Windows + WSL

On Windows, agents run where the project lives. A project folder inside WSL (`\\wsl.localhost\<distro>\...`) runs its agents inside that distribution, with your Linux login shell's `PATH`, so the CLIs you installed and logged in to there are used. Other folders use the Windows CLIs. Override it per project from the `⚙` menu in the chat header (Auto / Windows / WSL).

## Keyboard Shortcuts

| Key | Action |
| --- | --- |
| `Enter` / `Shift+Enter` | Send prompt / insert newline (configurable to `Ctrl+Enter` / `Cmd+Enter` in Settings) |
| `Esc` | Stop the running agent (or cancel a rename) |
| `Ctrl+N` | New session |
| `Ctrl+S` | Save the file open in the file panel |
| `Ctrl+L` | Focus the prompt |
| `Ctrl+B` | Show / hide the Files · Git · Logs panel |
| `1`–`9` / `N` or `Esc` | On an approval card (when it has the focus ring): pick that option / deny |
| `1`–`9` / `Enter` / `Esc` | On a question card: pick an option / answer / skip |

## Usage Dashboard

The title bar shows a ring per Claude Code / Codex provider, filled to the limit closest to running out (amber at 80%, red at 95%). Hover a ring for its limits and reset times; click it for the **Usage** screen (click again to go back), which shows a bar per limit (5-hour, weekly, and any per-model limit), the share used and left, and the time until it resets.

- Claude Code: the `get_usage` control request of `claude -p --input-format stream-json`.
- Codex: `account/rateLimits/read` on `codex app-server`.
- ACP agents: shown as unavailable (ACP has no way to ask). Logins without plan limits (e.g. API keys) are shown as unavailable too; SAME never estimates a number.

No turn is run, so no tokens are spent. Limits are fetched at launch, every 10 minutes (every 5 while the Usage screen is open), after a turn of that provider ends (if older than a minute), and with **Refresh**. They belong to the CLI's login where the current project's agents run (Windows or WSL). Each fetch starts the CLI once, so its startup hooks (e.g. Claude Code `SessionStart` hooks) run too.

### Token usage

Below the limits, **Token usage** totals the tokens each CLI used today, over 7 days or over 30 days: per provider (split into input, output, cache read and cache write), per day (stacked bars) and per model. **Include cache** switches between all tokens and input + output only. The numbers come from the history each CLI keeps on the machine where the project's agents run, so use outside SAME counts too:

- Claude Code: `~/.claude/projects/**/*.jsonl` (or `$CLAUDE_CONFIG_DIR`), deduplicated by message and request id.
- Codex: `~/.codex/sessions/**/*.jsonl` (or `$CODEX_HOME`), deduplicated by response id.
- OpenCode: `opencode stats --json`, which also reports a cost (shown as is; SAME estimates no cost).

Antigravity keeps no history SAME can read.

## Picking the Agent and Model

The row under the prompt has an agent picker, a model picker, and a reasoning effort picker (when supported by the selected model). Models are discovered dynamically from each provider (ACP `session/new`, Claude Code `initialize`, and Codex `app-server`). You can also type `/model <name>` (or `/model default`) in the prompt; typing `/` lists the commands, and `/model ` lists the models.

## Approval Modes

Each session has an approval mode, picked under the prompt (the default for new sessions is in Settings). A change applies to a running reply right away (for Codex, sandbox and policy changes apply on the next turn).

| Mode | Claude Code | Codex | ACP agents |
| --- | --- | --- | --- |
| Plan | `--permission-mode plan` | read-only sandbox, plan collaboration mode | the agent's `plan` mode |
| Ask (default) | `default` | workspace-write sandbox, `on-request` approvals | the agent's default mode |
| Accept edits | `acceptEdits` | same as Ask | `acceptEdits`-like mode, else edits are allowed by SAME |
| Full access | `bypassPermissions` | no sandbox, `never` asks | `bypassPermissions`-like mode, else everything is allowed by SAME |

In plan mode the agent's questions (Claude Code's AskUserQuestion, Codex `request_user_input`) and its proposed plan show as cards; **Implement this plan** switches back to the mode the session had before and starts the work.

The Claude Code and Codex CLIs run as one process per session that lives across turns (so "Allow for this session" grants last), and stop after 10 minutes unused; the next turn resumes the conversation.

Settings open from the ⚙ next to the version at the bottom of the sidebar (click again, or pick a session, to go back). Double-click a session (in the sidebar or its title) to rename it. Delete buttons ask for a second click to confirm.

## Architecture

```
crates/
├── same-core/    # Domain models, SQLite storage, TOML config, EventBus
├── same-acp/     # ACP v1 stdio JSON-RPC 2.0 client & protocol types
├── same-agent/   # Provider-agnostic AgentRuntime, Capabilities, Provider adapters
└── same-app/     # Native GPU-accelerated desktop GUI (GPUI + gpui-component)
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.

## Quick Start

```bash
# Build and run SAME (optionally pass a project directory to open immediately)
cargo run -p same-app -- /path/to/your/project

# Run tests
cargo test --workspace
```

## License

Dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
