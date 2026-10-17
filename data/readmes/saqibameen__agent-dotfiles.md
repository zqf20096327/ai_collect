<p align="center">
  <img src=".github/cover.svg" alt="agent-dotfiles" />
</p>

# agent-dotfiles

Write AI coding rules once, sync to every agent.

Most developers already have an `AGENTS.md` or `CLAUDE.md` in their projects. **agent-dotfiles** reads your existing rules and propagates them to every coding agent you use. No new directories, no config files, no lock-in.

## Supported Agents

| Agent | Rules | Skills | Detection |
|-------|-------|--------|-----------|
| Command Code | `AGENTS.md` | `.commandcode/skills/` | `~/.commandcode` |
| Claude Code | `CLAUDE.md` | `.claude/skills/` | `~/.claude` |
| Cursor | `AGENTS.md` | `.cursor/skills/` | `~/.cursor` |
| Copilot | `AGENTS.md` | `.github/skills/` | `~/.copilot` |
| Codex | `AGENTS.md` | `.agents/skills/` | `~/.codex` |
| OpenCode | `AGENTS.md` | `.opencode/skills/` | `~/.config/opencode` |

## Install

```sh
npx agent-dotfiles
```

## Usage

### Detect & Status

Run without arguments to see detected agents, found rules, and available commands:

```sh
npx agent-dotfiles
```

### Sync Rules

Sync your rules file to all agents:

```sh
npx agent-dotfiles sync rules --from AGENTS.md --to all
```

Sync to specific agents:

```sh
npx agent-dotfiles sync rules --from AGENTS.md --to claude,cursor
```

### Sync Skills

```sh
npx agent-dotfiles sync skills --from .claude/skills --to all
```

### Global Rules

Sync global rules across agents:

```sh
npx agent-dotfiles sync rules --from ~/.claude/CLAUDE.md --to all --global
```

### Dry Run

Preview what would happen without writing files:

```sh
npx agent-dotfiles sync rules --from AGENTS.md --to all --dry-run
```

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `--from <source>` | Source rules file or skills directory | required |
| `--to <agents>` | Target agents (comma-separated or `all`) | `all` |
| `--strategy <s>` | `skip`, `overwrite`, or `merge` | `skip` |
| `--method <m>` | `copy` or `symlink` | `copy` |
| `--global` | Sync global rules/skills | `false` |
| `--dry-run` | Preview without writing | `false` |

## Strategies

- **skip** (default) — never overwrites existing files
- **overwrite** — replaces existing files with source content
- **merge** — appends source content to existing files

## Config

Optional config at `~/.agents/agent-dotfiles.json`:

```json
{
  "mergeStrategy": "skip",
  "writeMethod": "copy"
}
```

## How It Works

`agent-dotfiles` is a **propagator**, not a creator. It reads your existing rules files and syncs them to agent-specific locations. Smart enough to skip agents that already natively read your source file.

For example, syncing from `AGENTS.md`:
- **Skips** Command Code, Cursor, Codex, OpenCode (they already read `AGENTS.md`)
- **Creates** `CLAUDE.md` for Claude Code (it only reads `CLAUDE.md`)

## Contributing

We welcome contributions — especially adding support for new coding agents! Check out the [Contributing Guide](CONTRIBUTING.md) for a step-by-step walkthrough.

## License

MIT

---

Built by [Saqib](https://saqibameen.com) with [Command Code](https://commandcode.ai)
