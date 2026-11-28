# memorable
[![M8ven Score](https://m8ven.ai/badge/mcp/constantine-kostikas-memorable-839xdh?v=42320f1ff41fe6a7f01f668e2553c9a2)](https://m8ven.ai/mcp/constantine-kostikas-memorable-839xdh?s=readme)


Persistent, searchable memory for Claude Code. **[Website and live demo](https://constantine-kostikas.github.io/memorable/)**

Claude Code forgets everything between sessions, and its built-in memory is Markdown files with no search index. memorable gives it a real memory store: Claude saves decisions, preferences, and project facts as it works, and finds them again later.

- **Proactive recall:** relevant memories appear on their own at session start and with each prompt.
- **Good search:** semantic plus keyword ranking, readable slugs like `infra/db-port`, tags, and links between memories.
- **Scoped:** separate contexts (say, `work` and `personal`) per directory, and per-project memories inside each.
- **Safe by default:** secrets are rejected, prompt injection is quarantined, and every change is versioned.
- **Local:** Postgres with pgvector in Docker and embeddings from Ollama, both on `127.0.0.1`.
- **CLI and web UI** to search, review, and edit what Claude remembers.

![Claude Code asked "how should we store money amounts?" calls memorable and answers from a saved project decision](site/assets/demo.gif)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="site/assets/ui-dark.png">
  <img src="site/assets/ui-light.png" alt="memorable web UI: a search for 'refund rounding' showing the score breakdown for the top result, with the memory open for editing">
</picture>

What Claude sees when you type "the refund total is off by a cent, can you look into it?":

```
<memory-recall search_id="..." count="1">
- 79% id=... slug=decisions/money-as-integer-cents | Store money as integer cents, never floats: Decided 2026-10-02: all amounts are int64 minor units (cents) with an ISO 4217 currency column. Floats caused a 1-cent rounding bug in refunds (incident INC-212)...
</memory-recall>
```

## Quick start

```sh
curl -fsSL https://raw.githubusercontent.com/constantine-kostikas/memorable/main/install.sh | sh
memorable setup
```

Then start a new Claude Code session. See [Requirements](#requirements) first.

- [Quick start](#quick-start)
- [Why memorable](#why-memorable)
- [Requirements](#requirements)
- [Install](#install)
- [Set up](#set-up)
- [Update](#update)
- [How Claude uses it](#how-claude-uses-it)
- [Command line](#command-line)
- [Web UI](#web-ui)
- [Configuration](#configuration)
- [Backups, export, and import](#backups-export-and-import)
- [Passwords](#passwords)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Development](#development)
- [License](#license)

## Why memorable

There are good alternatives, and the right one depends on what you want Claude to remember.

| | Claude Code built-in memory | [claude-mem](https://github.com/thedotmack/claude-mem) | memorable |
|---|---|---|---|
| Stores | Markdown notes per project | Compressed summaries of session activity | Individual facts, decisions, and preferences |
| Finding them | An index file loaded at session start; Claude reads the files | An index of relevant observations at session start, plus keyword and semantic search tools | Hybrid semantic and keyword search, plus per-prompt recall with a relevance score |
| Storage | Files under `~/.claude` | SQLite, with Chroma for semantic search | Postgres with pgvector |
| Scope | Per project | Per project | Contexts by directory, projects within them, and a shared profile |
| Safety | Plain files you can edit | `<private>` tags keep content out of storage | Versioning, soft deletes, secret scanning, prompt injection quarantine |
| Setup | None | `npx` installer or plugin (Node, Bun, and uv) | One binary and `memorable setup` (Docker and Ollama) |

Pick memorable when:

- You work across many projects and want facts found by meaning, not by file name.
- You want recall to be selective: most prompts get no pointers, and the ones that do come with a calibrated relevance score.
- You want to review and edit what Claude saved, see every version, and keep secrets and injected instructions out.
- You are fine running Docker and Ollama locally. If you are not, the built-in memory is the lighter choice.

## Requirements

- macOS or Linux
- [Docker](https://docs.docker.com/get-docker/) (Docker Desktop on macOS)
- [Ollama](https://ollama.com/download), installed natively so it can use your GPU
- [Claude Code](https://claude.com/claude-code)

## Install

| Method | Command |
|---|---|
| Install script | `curl -fsSL https://raw.githubusercontent.com/constantine-kostikas/memorable/main/install.sh \| sh` |
| Homebrew (macOS) | `brew install --cask constantine-kostikas/tap/memorable` |
| Manual | Download `memorable_<OS>_<arch>.tar.gz` from [Releases](https://github.com/constantine-kostikas/memorable/releases), check it against `checksums.txt`, and put `memorable` on your `PATH` |
| From source (Go 1.26) | `go install github.com/constantine-kostikas/memorable/cmd/memorable@latest`, or clone and run `make build` |

The install script:

- Installs the newest stable release, or the newest pre-release while there is no stable one.
- Checks the archive's sha256 against `checksums.txt`. GPG verification happens on `memorable update`.
- Installs to `~/.local/bin`. Set `MEMORABLE_INSTALL_DIR` to change it, or `MEMORABLE_VERSION=v0.1.0` to pin a release.

Source builds report version `dev`, so `memorable update` does not manage them.

## Set up

```sh
memorable setup --dry-run   # preview every change
memorable setup
```

Each step shows what it will change, as a diff for files, and asks before applying it:

1. Check Docker and Ollama.
2. Create the `memorable-postgres` container on `127.0.0.1:5434` with a generated admin password. **The admin password is shown once. Save it in your password manager.** Admin commands ask for it.
3. Map directories to contexts (for example `personal` and `work`) and write the config.
4. Create the database role and schemas, and store the app password in your OS keyring.
5. Pull the embedding model.
6. Register the MCP server with Claude Code (`claude mcp add --scope user`).
7. Add the memorable instructions to `~/.claude/CLAUDE.md`.
8. Add permission rules to `~/.claude/settings.json`, and optionally the [hooks](#how-claude-uses-it).
9. Optionally install a daily backup job (systemd user timer or launchd agent).
10. Optionally install tab completion for your login shell.
11. Run `memorable doctor`.

Start a new Claude Code session when it finishes.

### Manual setup

```sh
read -rs "PGPW?admin password: " && echo        # bash: read -rsp "admin password: " PGPW
docker run -d --name memorable-postgres --restart unless-stopped \
  -p 127.0.0.1:5434:5432 \
  -e POSTGRES_USER=memorable_admin -e POSTGRES_PASSWORD="$PGPW" -e POSTGRES_DB=memorable \
  -v memorable-pgdata:/var/lib/postgresql \
  pgvector/pgvector:0.8.7-pg18-trixie
unset PGPW
ollama pull embeddinggemma
memorable context add ~/code personal      # repeat per directory or context
memorable migrate                          # asks for the admin password
claude mcp add --scope user memorable -- "$(command -v memorable)" serve
```

Then:

- Append [`docs/claude-md-snippet.md`](docs/claude-md-snippet.md) to `~/.claude/CLAUDE.md`.
- Add the [permission rules](#permission-rules) to `~/.claude/settings.json`.
- Optionally add the [hooks](#hooks).

### Shell completion

`memorable setup` installs completion for your login shell. To install it by hand:

| Shell | Command |
|---|---|
| fish | `memorable completion fish > ~/.config/fish/completions/memorable.fish` |
| bash (Linux) | `memorable completion bash > ~/.local/share/bash-completion/completions/memorable` (needs `bash-completion`) |
| bash (macOS) | Install `bash-completion@2` with Homebrew (`bash-completion` for the stock bash 3.2), then source the script from `~/.bash_profile` |
| zsh | Write `memorable completion zsh` to a file and `source` it at the end of `~/.zshrc`, after `compinit` |

- The scripts call back into the binary, so updates never require reinstalling them.
- Completion never opens the database or keyring, so ids, slugs, and tags do not complete. Context names do.
- Release archives include the scripts under `completions/`.

## Update

```sh
memorable update --check   # show what would change
memorable update
```

The update verifies the GPG signature on the release's `checksums.txt` against the key built into the binary, then the archive's sha256. If either check fails, the installed binary is left untouched.

| Option | Effect |
|---|---|
| `--pre` | Include pre-releases. A pre-release install already sees newer pre-releases. |
| `--version v0.2.0` | Install a specific version, including a downgrade. |
| `--force` | Replace a development build, or reinstall the same version. |

- **Token:** not required. If `GH_TOKEN`, `GITHUB_TOKEN`, or `gh auth token` is available, it is used to raise the GitHub API rate limit.
- **Root-owned directories:** if the binary's directory is not writable, the update stages the verified binary and runs `sudo install` for you, or prints the command when there is no terminal. Do not run `sudo memorable update`.
- **Homebrew installs** are refused. Use `brew upgrade --cask memorable`.

Afterward, restart your Claude Code sessions, since running `memorable serve` processes keep the old binary. Then run `memorable doctor`, and `memorable migrate` if it reports schemas behind.

## How Claude uses it

Once setup is done, Claude searches and saves memories on its own, following the CLAUDE.md instructions.

### MCP tools

| Tool | Purpose |
|---|---|
| `memory_search` | Hybrid semantic and keyword search |
| `memory_get` | Fetch full memories by id or slug |
| `memory_list`, `memory_tags`, `memory_top` | Browse by filter, list tags in use, show pinned and most used |
| `memory_write`, `memory_update`, `memory_link` | Save, edit, and relate memories |
| `memory_feedback` | Mark a memory useful, wrong, or outdated |
| `memory_review` | List memories that need attention |
| `memory_history`, `memory_restore`, `memory_delete` | Version history, undelete or roll back, and soft delete |

### Hooks

Both hooks are optional and never fail a session.

- **SessionStart** (`memorable hook session-start`) gives Claude your pinned and most used memories, plus the tags in use.
- **UserPromptSubmit** (`memorable hook prompt-submit`) searches your memories for each prompt and gives Claude up to three pointers with a relevance percentage. Claude fetches the ones it needs.

A prompt recall pointer looks like this:

```
<memory-recall search_id="..." count="1">
- 86% id=... slug=memorable/db-port | Memorable database port: The memorable Postgres container listens on 127.0.0.1:5434...
</memory-recall>
```

Most prompts get no pointers. By default, recall:

- Shows only matches at 70% relevance or higher.
- Skips slash commands and prompts shorter than three words.
- Never repeats a memory within a session.
- Gives up silently after 1.5 seconds.

Change these under [`[recall]`](#configuration). If pointers feel noisy, raise `min_relevance` to `0.8`.

The percentage starts from a built-in fit for `embeddinggemma` and learns from your use: a pointer Claude fetches counts as relevant, and one it ignores for a day counts as irrelevant.

- `memorable calibrate --dry-run` shows the learned fit.
- `memorable calibrate` saves it once there are at least 20 of each.
- `memorable stats` shows how many prompts got pointers and how many were fetched.
- `memorable doctor` shows which calibration is active.

To add the hooks by hand, put this under `hooks` in `~/.claude/settings.json`:

```json
"SessionStart": [{"hooks": [{"type": "command", "command": "memorable hook session-start"}]}],
"UserPromptSubmit": [{"hooks": [{"type": "command", "command": "memorable hook prompt-submit"}]}]
```

## Command line

Commands act on the context and project of the current directory. Run `memorable <command> --help` for flags. Read commands accept `-o json`, and output is plain text when piped.

### Memory

| Command | What it does |
|---|---|
| `memorable search "database port"` | Hybrid search (`--tag`, `--type`, `--all-projects`, `-k`) |
| `memorable get infra/ports` | Show full memories by slug or id |
| `memorable list --status flagged` | Browse with filters, paginated |
| `memorable top` | Pinned and most used memories |
| `memorable tags` | Tags in use, with counts |
| `memorable edit infra/ports` | Edit in `$EDITOR`; the result is rescanned and re-embedded |
| `memorable review` | Work through flagged, expired, stale, and unverified memories |
| `memorable stats` | Counts, embedding coverage, and prompt recall activity |
| `memorable export` / `import` | See [Backups, export, and import](#backups-export-and-import) |
| `memorable ui` | Open the [web UI](#web-ui) |

### Admin

These ask for the admin password, except `backup`, `calibrate`, and `reembed` (which asks only for `--all` after a dimension change).

| Command | What it does |
|---|---|
| `memorable approve --list` | Review memories quarantined by the injection scanner, then `approve <id>` |
| `memorable profile add\|list\|edit\|delete` | Manage profile memories, which apply in every context |
| `memorable purge <id>` | Permanently erase a memory, its history, and its references |
| `memorable prune` | Delete access events older than the retention period |
| `memorable reembed` | Compute pending embeddings; `--all` after changing the model or dimensions |
| `memorable migrate` | Create roles and schemas and apply migrations |
| `memorable backup` | Dump the database |
| `memorable calibrate` | Fit recall relevance to your use |
| `memorable change-password --role admin\|app` | See [Passwords](#passwords) |

### Setup

| Command | What it does |
|---|---|
| `memorable setup` | Guided setup |
| `memorable doctor` | Check everything and print a fix for each failure |
| `memorable context` | Show the context and project for this directory |
| `memorable context add <path> <name>` | Map a directory to a context, creating it if needed |
| `memorable update` | Install the newest verified release |
| `memorable completion <shell>` | Print a completion script |
| `memorable version` | Print version information |

`memorable serve` (the MCP server) and `memorable hook` are started by Claude Code, not by you.

## Web UI

```sh
memorable ui            # current directory's context
memorable ui --admin    # also unlock admin actions
```

Options: `--context <name>`, `--port <n>` (random free port by default), and `--no-browser`.

What it offers:

- A two-pane workspace: the memory list on the left, the selected memory on the right.
- Each memory has a properties rail and Content, History, Links, and Activity tabs. History compares any two versions side by side.
- Filtering with tag suggestions, and search with a per-result score breakdown.
- Edit, flag, delete, restore, link, and supersede memories.
- Review and Stats pages, matching `memorable review` and `memorable stats`.

Keyboard shortcuts (press `?` to list them):

| Key | Action |
|---|---|
| Ctrl K or `/` | Jump to any memory or page |
| `j` / `k` | Next or previous memory |
| `e` | Edit the content |
| `F` | Expand or restore the editor |
| Ctrl S | Save |
| Ctrl B / Ctrl I | Bold or italic (Markdown) |
| Esc | Close a dialog or leave the expanded editor |

On macOS, use Cmd in place of Ctrl.

### Admin mode

`--admin` prompts for the admin password in the terminal and refuses to run without one. It adds approve, purge, prune, and profile writes.

- The unlock expires after 15 minutes without admin activity. Opening Review counts, because it reads the quarantine list as admin.
- Purge asks you to type the slug or id.

### How the UI is protected

- The server binds `127.0.0.1` only.
- The launch URL carries a single-use token, exchanged for an `HttpOnly`, `SameSite=Strict` cookie. The browser opens through a private redirect file, so the token never appears in a process list.
- Requests are checked for a CSRF token, the `Host` header, and cross-origin headers. A strict Content-Security-Policy applies.
- All assets are embedded. Nothing loads from a CDN.
- Setup denies Claude `Bash(memorable ui:*)`, so Claude cannot start it.

Limits:

- A link previewer or scanner that opens the launch URL first uses up the token. Restart `memorable ui` for a new link.
- While admin is unlocked, anyone holding the session cookie has admin rights. Cookies are not scoped by port.

## Configuration

The config file lives at:

- Linux: `~/.config/memorable/config.toml`
- macOS: `~/Library/Application Support/memorable/config.toml`

Override the path with `--config` or `MEMORABLE_CONFIG`.

```toml
fallback_context = "personal"   # read-only access from unmapped directories; omit to disable

[contexts.personal]
paths = ["~/code", "~/notes"]

[contexts.work]
paths = ["~/work"]
```

### Contexts

- Each context is a separate Postgres schema.
- A Claude Code session only sees the context of its directory.
- Writes from a directory that matches no context are refused.
- The `profile` context holds memories that apply everywhere, such as writing preferences. Every context can read it. Only you can write to it, with `memorable profile` or `memorable ui --admin`.

### Other settings

All optional. Defaults shown.

| Section | Keys |
|---|---|
| `[database]` | `host = "127.0.0.1"`, `port = 5434`, `name = "memorable"`, `app_user = "memorable_app"`, `admin_user = "memorable_admin"`, `container = "memorable-postgres"` |
| `[embedding]` | `provider = "ollama"`, `url = "http://127.0.0.1:11434"`, `model = "embeddinggemma"`, `dimensions = 768`, `allow_remote = false` |
| `[search]` | `min_similarity = 0.30`, `duplicate_threshold = 0.95`, `conflict_threshold = 0.75`, `half_life_days = 30` |
| `[preload]` | `max_items = 10`, `max_chars = 4000` (SessionStart hook) |
| `[recall]` | `min_relevance = 0.70`, `max_items = 3`, `min_words = 3`, `deadline_ms = 1500` (UserPromptSubmit hook) |
| `[limits]` | `writes_per_minute = 60` |
| `[retention]` | `access_events_days = 90`, `backups_keep = 14` |

### Environment variables

| Variable | Effect |
|---|---|
| `MEMORABLE_CONFIG` | Config file path |
| `MEMORABLE_DB_HOST`, `MEMORABLE_DB_PORT`, `MEMORABLE_DB_NAME` | Override `[database]` |
| `MEMORABLE_CONTEXT` | Force a context instead of matching the directory |
| `MEMORABLE_KEYRING=off` | Store passwords in `credentials.json` instead of the OS keyring |
| `MEMORABLE_LOG_LEVEL=debug` | Verbose logs |

## Backups, export, and import

**Backups.** `memorable backup` runs `pg_dump` inside the container and keeps the newest 14 dumps in `~/.local/share/memorable/backups` (change with `--dir`). To restore one:

```sh
docker exec -i memorable-postgres pg_restore -U memorable_admin -d memorable --clean --if-exists \
  < ~/.local/share/memorable/backups/memorable-YYYYMMDD-HHMMSS.dump
```

**Export.** `memorable export` writes the current context as JSON to stdout. Use `--out file.json`, or `--format md --out <dir>` for Markdown files.

**Import.** `memorable import` reads a JSON export, a Markdown file, or a directory of Claude Code memory files:

```sh
memorable import ~/.claude/projects/<project>/memory --dry-run
memorable import ~/.claude/projects/<project>/memory
```

Imports pass the same validation, secret scan, injection scan, and duplicate checks as anything Claude writes.

## Passwords

There are two database passwords:

- **Admin:** yours, kept in your password manager. Admin commands ask for it.
- **App:** generated and kept in your OS keyring. Claude Code and the UI use it.

| Command | Effect |
|---|---|
| `memorable change-password --role admin` | Asks for the current password, then the new one twice (at least 6 characters, terminal only) |
| `memorable change-password --role app` | Generates a new app password and stores it in the keyring. Restart Claude Code sessions and `memorable ui` afterward. |

## Troubleshooting

Start with `memorable doctor`. It checks the config, keyring, container, port, database login, extensions, schema versions, Ollama, the model, and the embedding dimensions, and prints a fix for each failure.

| Symptom | Fix |
|---|---|
| Tools say "memory store unavailable" | Start the container (`docker start memorable-postgres`), or restore the app password with `memorable migrate` |
| Search only matches keywords | Ollama is down or the model is missing. Pending embeddings catch up later, or run `memorable reembed` now. |
| Changed the embedding model or dimensions | `memorable reembed --all` |
| App cannot connect after `change-password --role app` | Restart Claude Code sessions and `memorable ui`. If that fails, `memorable migrate` resets the role to the keyring password. |
| Admin password rejected after `change-password --role admin` | The password `docker inspect` shows is the original one and no longer works. If you lost the new one, reset it below. |

Reset the admin password as the container superuser:

```sh
read -rs "PGPW?new admin password: " && echo     # bash: read -rsp "new admin password: " PGPW
docker exec -i memorable-postgres psql -U memorable_admin -d memorable -v pw="$PGPW" \
  <<<"ALTER ROLE memorable_admin PASSWORD :'pw';"
unset PGPW
```

## Security

- **Secrets** are rejected on every write, using the gitleaks rule set plus an entropy check.
- **Prompt injection:** text that looks like instructions to an agent is quarantined until you approve it, and Claude never sees quarantined content. Memories from tool output are marked unverified and never preloaded.
- **Isolation:** a session is bound to one context schema and cannot pick another.
- **Recoverable:** the app role cannot delete rows. Deletes are soft, every change is versioned, and only `memorable purge` (admin) erases data.
- **Local only:** Postgres and Ollama listen on `127.0.0.1`. Remote embedding providers need `allow_remote = true`.
- **Verified updates:** `memorable update` downloads over HTTPS from `api.github.com`, follows redirects only to `*.githubusercontent.com`, checks a detached GPG signature (key `D4A4DEE111ABA5ACBE1F49773B21B7770B4334A4`) before trusting any checksum, and fails closed.
- **Docker is a soft boundary:** anyone who can run `docker exec` has full database access. The deny rules below keep Claude out.

### Permission rules

Setup adds these to `~/.claude/settings.json`. On macOS, the credentials path is `~/Library/Application Support/memorable/credentials.json`.

```json
"allow": [
  "mcp__memorable__memory_search", "mcp__memorable__memory_get", "mcp__memorable__memory_list",
  "mcp__memorable__memory_tags", "mcp__memorable__memory_top", "mcp__memorable__memory_history",
  "mcp__memorable__memory_review", "mcp__memorable__memory_write", "mcp__memorable__memory_update",
  "mcp__memorable__memory_feedback", "mcp__memorable__memory_link"
],
"ask": ["mcp__memorable__memory_delete", "mcp__memorable__memory_restore"],
"deny": [
  "Bash(memorable purge:*)", "Bash(memorable approve:*)", "Bash(memorable profile:*)", "Bash(memorable ui:*)",
  "Bash(memorable change-password:*)", "Bash(docker exec memorable-postgres:*)", "Bash(docker inspect memorable-postgres:*)", "Bash(psql:*)",
  "Read(~/.config/memorable/credentials.json)"
]
```

## Development

```sh
make build              # bin/memorable
make test               # unit tests
make test-integration   # needs Docker
make test-eval          # search quality against a local Ollama
make lint vuln sec      # static checks
```

## License

[MIT](LICENSE)
