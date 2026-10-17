<div align="center">

# DocOps

### The Kanban board that runs your AI coding agents

[![GitHub stars](https://img.shields.io/github/stars/Oak-AN/DocOps?style=for-the-badge&logo=github&color=f5cd47)](https://github.com/Oak-AN/DocOps/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-579dff?style=for-the-badge)](LICENSE)
![Django](https://img.shields.io/badge/Django-6.1-4bce97?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-Vite-9f8fef?style=for-the-badge&logo=react&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-6cc3e0?style=for-the-badge&logo=docker&logoColor=white)

Drop a card on the board, pick **Claude Code**, **Codex CLI**, **OpenCode** or the **Hermes agent**,
and watch it work in its own git branch and worktree — then review, test and merge from one screen.

**⭐ If you find it useful, a [star](https://github.com/Oak-AN/DocOps) would be appreciated. ⭐**

</div>

> [!NOTE]
> **This project is sunsetting.** DocOps is no longer actively developed, but it remains a great
> starting point for anyone who wants to run and build their own framework for parallel AI coding agents.
>
> It was built by working developers who use it day to day at their company. It is not super polished,
> but it does the hard parts for you: **the AI agents manage the git worktrees entirely**, and
> **cards and boards are created automatically**. Fork it, run it, and build from there.

<p align="center">
  <img src="docs/images/board.png" alt="DocOps Kanban board with labeled AI agent tasks" width="100%" />
</p>

---

## Table of contents

- [Why DocOps](#why-docops)
- [Features](#features)
- [Screenshots](#screenshots)
- [Quick start](#quick-start)
- [Development](#development)
- [Configuration](#configuration)
- [How it works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Why DocOps

Coding agents are great at focused tasks, but juggling several of them means juggling terminals,
branches, half-finished diffs and "wait, which session was that?". DocOps turns every piece of work
into a **card**: a card is a thread, a branch and an isolated worktree. Agents run in parallel, report
progress on the board, ask you questions when a decision is genuinely yours, and land their work in a
review queue with a running preview and a test plan.

## Features

- 🗂️ **Kanban board per project** — Backlog → In Progress → Human Review → Done → Merged, with drag &
  drop, colorful labels, checklists, due dates, custom boards and live agent activity on every card.
- 🌿 **Thread = branch = worktree** — every task gets its own branch and worktree inside the project
  (`<project>/.docops/worktrees/`). Follow-up messages resume the same CLI session in the same workspace.
- 🤖 **Bring your own agent** — run Claude Code, Codex CLI or OpenCode directly, or let the Hermes agent
  orchestrate while you still choose the CLI, model and reasoning effort per task.
- 🧑‍✈️ **Manager agents** — hand over your notes (typed, pasted or a photo) and a manager writes the cards,
  runs them in parallel, verifies the results with your test suite, and reports back.
- 🔌 **Built-in MCP server** — agents drive the board through `kanban` tools (`get_card`, `move_card`,
  `check_item`, `ask_user`, …) instead of fragile text markers.
- 🙋 **Agents can ask you** — a card parks and glows when an agent needs a decision; your answer resumes
  the exact same thread.
- ✅ **Review queue** — finished work arrives with a running preview, the diff and a generated test plan.
  Ship it or send it back in one keystroke.
- 💻 **VS Code page** — changed files, commit box, commit graph, Monaco diff, a real terminal and the
  agent thread side by side. **Alt+C** flips to the running app.
- 🔀 **One-click AI merge** — conflict preview via `git merge-tree`; clean branches merge instantly,
  conflicted ones can be resolved by you or delegated to any agent.
- 🚀 **Workspace slots & previews** — a pool of warm worktrees with one-click app previews (commands or
  Docker Compose), shared services and live logs.
- 💸 **Token and cost visibility** — per-task and per-batch usage, split across Hermes, Claude and Codex.
- 🧰 **And more** — GitHub issue import, agent profiles and pipeline templates, ideation chat → task,
  animated changelog, embedded terminal and browser-based CLI logins.

## Screenshots

<table>
  <tr>
    <td width="50%">
      <img src="docs/images/task.png" alt="Task page with checklist, labels and agent conversation" />
      <p align="center"><b>Task page</b> — thread, checklist, labels and live agent logs</p>
    </td>
    <td width="50%">
      <img src="docs/images/vscode.png" alt="VS Code style review workspace" />
      <p align="center"><b>VS Code page</b> — diff, terminal and agent thread on one screen</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <img src="docs/images/agents.png" alt="Agent profiles and pipeline templates" />
      <p align="center"><b>Agent profiles</b> — engineering team and BMAD method templates</p>
    </td>
  </tr>
</table>

## Quick start

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) with Compose
- A folder containing the git repositories you want agents to work on
- An account for at least one coding CLI (Claude Code, Codex or OpenCode)

### 1. Clone

```bash
git clone https://github.com/Oak-AN/DocOps.git
cd DocOps
```

### 2. Point DocOps at your projects

Create a `.env` file next to `docker-compose.yml`:

```env
PROJECTS_DIR=/home/you/code
KANBAN_HOST_PATH_MAP=/home/you/code=>/projects
KANBAN_SUPERUSER_USERNAME=admin
KANBAN_SUPERUSER_PASSWORD=change-me-to-something-long
```

On Windows use paths such as `PROJECTS_DIR=D:\Code` and `KANBAN_HOST_PATH_MAP=D:\Code=>/projects`.

### 3. Run

```bash
python local_build_run.py
# or
docker compose up -d --build
```

Open **http://localhost:40000**, sign in to your coding CLIs on the **Connections** page, add a
project, and create your first card.

## Development

### Docker with hot reload

```bash
docker compose -f docker-composeDEV.yaml up -d --build
```

- App (Vite dev server): http://localhost:5001
- Django admin: http://localhost:8002/admin

The code is bind-mounted, so saving a file on the host reloads the app.

### Bare metal

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python -m uvicorn backend.asgi:application --port 8000
```

```bash
cd frontend
bun install
bun run dev
```

Then open http://localhost:5173.

### Tests

```bash
cd backend
python manage.py test api
```

### `local_build_run.py`

| Command                                        | What it does                                               |
| ---------------------------------------------- | ---------------------------------------------------------- |
| `python local_build_run.py`                    | build → start → wait until ready → open the browser         |
| `… --dev`                                      | the same for the hot-reload stack                           |
| `… --clis claude`                              | bake in only the CLIs you use for a smaller image           |
| `… --size`                                     | image size and the heaviest layers                          |
| `… --logs` / `--down` / `--status`             | follow logs / stop the stack / show containers              |
| `… --no-build` / `--foreground` / `--prune`    | skip the build / attach to logs / drop orphaned images      |

## Configuration

All state lives in `./runtime` next to the compose file (override with `RUNTIME_DIR`):

| Host path        | Container path | Holds                                                          |
| ---------------- | -------------- | -------------------------------------------------------------- |
| `runtime/auth/`  | `/opt/auth`    | CLI accounts, session state, GitHub credentials, git config     |
| `runtime/data/`  | `/opt/data`    | Hermes config and sessions, the SQLite database and run logs    |
| `PROJECTS_DIR`   | `/projects`    | Your repositories and their `.docops/worktrees/`                |

| Variable                               | Default              | Purpose                                                            |
| -------------------------------------- | -------------------- | ------------------------------------------------------------------ |
| `KANBAN_DATA_DIR`                      | `backend/.data`      | Run logs and SQLite                                                 |
| `KANBAN_DEBUG`                         | `1`                  | Django debug mode                                                   |
| `KANBAN_SECRET_KEY`                    | _(dev key)_          | Django secret key — set this for any shared deployment              |
| `KANBAN_SUPERUSER_USERNAME`            | `admin`              | Admin account created on startup                                    |
| `KANBAN_SUPERUSER_PASSWORD`            | `admin12345`         | Its password (existing accounts are never overwritten)              |
| `KANBAN_MAX_PARALLEL_RUNS`             | `6`                  | Cap on concurrent agent processes                                   |
| `KANBAN_HOST_PATH_MAP`                 | _(empty)_            | `HOST=>CONTAINER;…` path translations                               |
| `KANBAN_PROJECTS_ROOT`                 | _(any)_              | Restrict where projects may be registered                           |
| `KANBAN_WORKTREES_ROOT`                | _(unset)_            | Keep worktrees outside the projects instead                         |
| `KANBAN_MCP_PORT`                      | `8765`               | Port of the `kanban` MCP server agents connect to                   |
| `KANBAN_ASK_WAIT_SECONDS`              | `0`                  | How long `ask_user` may block waiting for an answer                  |
| `KANBAN_HERMES_POLL_SECONDS`           | `15`                 | Hermes board sync interval (`0` disables it)                        |
| `KANBAN_PREVIEW_PORT_BASE`             | `5100`               | First port of the command-mode preview band                         |
| `KANBAN_COMPOSE_PORT_BASE`             | `5200`               | First port of the compose-mode preview band                         |
| `KANBAN_CODEX_SANDBOX`                 | _(empty)_            | e.g. `danger-full-access` where bubblewrap is unavailable           |
| `KANBAN_HOST_UID` / `KANBAN_HOST_GID`  | _(auto)_             | Linux owner for bind-mounted projects                               |
| `KANBAN_GIT_USER_NAME`                 | `DocOps Agent`       | Git author for agent commits                                        |
| `KANBAN_GIT_USER_EMAIL`                | `agent@docops.local` | Git author email for agent commits                                  |

> **Security note:** DocOps runs coding agents with access to your repositories and credentials.
> Run it on a trusted machine or private network, change the default admin password, and set
> `KANBAN_SECRET_KEY` and `KANBAN_DEBUG=0` before exposing it anywhere.

## How it works

```text
┌───────────────────────────┐     docker exec       ┌────────────────────────┐
│  DocOps app container     │ ────────────────────▶ │  Hermes agent sidecar  │
│  Django + ninja API       │ ◀──────────────────── │  (nousresearch image)  │
│  React UI (Vite build)    │     CLI proxies       └────────────────────────┘
│  Claude/Codex/OpenCode    │
│  kanban MCP server        │ ◀── agents call board tools (move_card, ask_user, …)
└────────────┬──────────────┘
             │ /projects
             ▼
   your repos + .docops/worktrees/slot-*, t<id>-*
```

- **Backend:** Django, django-ninja, SQLite, uvicorn, FastMCP
- **Frontend:** React, Vite, Tailwind, shadcn/ui, Zustand, Monaco, xterm.js
- **Runtime:** a lightweight app image beside the official
  [Hermes agent](https://hermes-agent.nousresearch.com/docs/user-guide/docker) image

Design notes live in [`.docops/ARCHITECTURE.md`](.docops/ARCHITECTURE.md) and
[`.docops/FEATURES.md`](.docops/FEATURES.md).

## Contributing

Contributions are welcome!

1. Fork the repository and create a branch: `git checkout -b feat/my-feature`
2. Make your change and run the backend tests and `bun run lint`
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, …)
4. Open a pull request describing what changed and why

Found a bug or have an idea? [Open an issue](https://github.com/Oak-AN/DocOps/issues).

## License

Released under the [MIT License](LICENSE).

<div align="center">

**⭐ If DocOps was a useful starting point for you, a [star](https://github.com/Oak-AN/DocOps) would be appreciated. ⭐**

</div>
