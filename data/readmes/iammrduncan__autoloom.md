[Join Discord](https://discord.gg/VVt9qmkcnr) -- [Website: thresher.sh](https://thresher.sh)

# autoloom

Autoloom is a tiny self-learning autonomous agent wrapper built on top of `tinyloom`.

The core runtime is only about **~225** lines of code. The entire core library is **~900** lines of code and the entire plugins and all is about **~1500** lines of code.

It keeps its state in `~/.autoloom`, uses plain files for sessions/tasks/memories, manages heartbeat runs with cron, and ships a minimal Textual TUI plus a small webhook server.

![autoloom demo](./docs/images/demo.gif)

## Safety

Autoloom inherits tinyloom's ability to run shell commands and edit files. It is not a sandbox by itself.

If you want isolation, run it inside a container or microVM. See the sandbox docs below.

If you run it on your root machine you risk destroying it, do not run it outside an isolated environment. You have been warned!

## Install

End user (after the first PyPI release):

```bash
uv tool install autoloom # or pip install autoloom
autoloom setup
```

Developer (from source):

```bash
git clone <repo-url>
cd autoloom
uv sync --extra dev
```

End-user examples in this README use `autoloom` directly. Developers should prefix with `uv run` (e.g. `uv run autoloom setup`).

## Quick start

```bash
autoloom setup
autoloom
autoloom "review pending work and update tasks"
autoloom heartbeat run
autoloom webhook serve
```

Update your heartbeat:

```bash
tinyloom "update my heartbeat.md with ... <whatever you want>"
```

Create a new scheduled task:
```bash
tinyloom "create a new cron job with <interval> and launch yourself on that cron job for a task of <whatever your task is>"
```

## Files

Autoloom stores its data in:

- `~/.autoloom/SOUL.md`
- `~/.autoloom/heartbeat.md`
- `~/.autoloom/tasks/`
- `~/.autoloom/skills/`
- `~/.autoloom/knowledgegraph/memories/`
- `~/.autoloom/sessions/`

## Commands

- `autoloom` opens the TUI
- `autoloom "..."` runs a persisted headless session and streams JSONL events
- `autoloom setup` walks an interactive setup that configures agent identity, model provider/credentials/tuning, safety limits, compaction, heartbeat schedule, plugins, and webhook — the API key is written to `~/.autoloom/.env`, never `config.yaml`
- `autoloom heartbeat run` executes one heartbeat session
- `autoloom cron install|show|remove` manages the heartbeat cron block
- `autoloom webhook serve` runs the local-first webhook server

## Docs

- [Getting Started](docs/getting-started.md)
- [State and Heartbeats](docs/state-and-heartbeats.md)
- [Self-Learning](docs/self-learning.md)
- [Plugins](docs/plugins.md)
- [Webhooks](docs/webhooks.md)
- [Design Decisions](docs/design-decisions.md)
- [Docker Sandbox Guide](docs/sandbox-docker.md)
- [Podman Sandbox Guide](docs/sandbox-podman.md)
- [microsandbox Guide](docs/sandbox-msb.md)
- [Kata Containers Guide](docs/sandbox-kata.md)
- [Docker Sandbox microVM Guide](docs/sandbox-sbx.md)

## Verification

```bash
uv run ruff check
uv run pytest
```

# Case Study - tinyloom auto plugin development

I have a autoloom that is running ever 10 minutes in a vps. It's goal is to research popular trends and identify plugins for tinyloom or autoloom and then plan, implement, and test them.

it... just... works...

It's ran for 24 hours and it's built 15 plugins... all passing tests...

Now a lot of them are throw away... but this is with one line of "direction". 

After starting up, the TUI detected that `git` was missing, so it automatically installed it before proceeding to clone repositories.

![Autoloom TUI console](./docs/images/tui.png)

Within two heartbeat cycles, it cloned the repo, began planning plugins, and started building its own knowledge graph.

![Autoloom memory tree](./docs/images/memory.png)

The system self learns, self directs, and has full autonomy. 