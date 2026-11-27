# Atlas

A factory of Claude Code agents, supervised by an orchestrating AI and steered by the master (you).

You hand a piece of work to the orchestrator (a ticket, a merge request to review, a free task); it
assembles a workflow for the agent from a catalogue of bricks (Qualification, Plan validated by
you, Implementation, Tests, Review by a fresh agent, Correction, Ship...) and launches it in a
dedicated worktree, on an existing branch or in the folder you name. The agent pulls its work from
a local MCP server. The orchestrator does not do the work: it assembles, follows, restarts, and
warns you when an agent needs you.

## Requirements

- Stable Rust: 1.89 or newer for the daemon, 1.90 for the desktop application
- Node 22.13 or newer and pnpm 12, only to build the front: nothing runs on Node
- On Linux, the libraries Tauri builds against (Debian and Ubuntu names):
  `libwebkit2gtk-4.1-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev libxdo-dev pkg-config`,
  and `git` at run time
- Claude Code installed and signed in to your subscription (`claude`); no API key is used
- The MCP servers of your forges (GitLab, Jira...) configured in Claude Code: the agents use them
  to read tickets and open merge requests

## Getting started

```sh
git clone <repository-url> atlas && cd atlas/front
pnpm install
pnpm dev            # opens Atlas in its window, the front hot-reloaded
pnpm build          # builds the installable application, daemon included
```

Atlas is a desktop application (Tauri): there is no web version. The shell carries the front,
starts the daemon when none runs, waits for it to answer, then gives its page the address of the
daemon and the token it asks for. The daemon serves no page: opened in a browser, it answers
nothing useful.

The daemon is a process separate from the window: closing it does not kill the running agents.
Atlas stays in the menu bar (or the notification area), from which you can:

- bring the window back;
- quit the interface while the daemon and its agents keep working;
- stop Atlas for good, which closes the agents' sessions.

The daemon started by the shell writes to `~/.atlas/daemon.log`.

On first run, Atlas creates `~/.atlas/` (or `$ATLAS_HOME`):

| File | Role |
| --- | --- |
| `config.yml` | Port, orchestrator model, allowed repositories, agent arguments, default workflow, branch names |
| `bricks/` | The catalogue: one `.yml` file per brick (instructions, model, threshold, dependencies), validated by the `brick.schema.json` the daemon writes there |
| `skills/` | Skills a brick can hand its sessions (`skills: [name]`), one folder per skill holding its `SKILL.md` |
| `subagents/` | Subagents a brick can hand its sessions (`subagentTypes: [name]`), one `<name>.md` each |
| `atlas.db` | SQLite registry: agents, the workflow of each with duration and tokens per step, sessions, chat, broadcasts, projects and their notes |
| `worktrees/` | The worktrees Atlas created, kept after the MR |
| `agents/<id>/` | What Atlas hands to an agent's sessions: its MCP configuration, its hooks and the plugin holding its brick's skills and subagents |
| `orchestrator/` | The system prompt and the MCP configuration of the orchestrator |
| `token` | Secret shared between the daemon, the desktop application, the hooks and the agents' MCP clients |
| `daemon.log` | Output of the daemon started by the shell |

The shipped catalogue holds ten bricks: `qualification`, `plan`, `implementation`, `tests`,
`review`, `correction`, `ship`, `review-mr` (reviewing someone else's merge request), `tache` (free
task) and `rapport` (report). An agent launched without a specific workflow follows `defaultSteps`.

A brick added or edited in `bricks/` is taken into account without restarting Atlas, from the next
step on. If the edited catalogue is invalid, Atlas says so in the chat and keeps the previous one.
A shipped brick you have not edited follows the updates of Atlas; a brick you have edited is never
touched again.

A brick is never deleted, it is disabled: list its id in `bricks/.disabled.json` (for example
`["rapport"]`). It leaves the orchestrator's catalogue and no new workflow may take it, while the
agents that already have it keep it; a shipped brick stays disabled through the updates. Atlas
refuses to disable a brick that a brick in service needs (`requires`, `fixedBy`).

The orchestrator can change the catalogue for you: ask it to add, edit, disable or re-enable a
brick, or to install a skill or a subagent, or give it a link or a path (a repository, a folder, a
file) to install. It explores the source and proposes each item in a card of the chat that shows the
files it would write; nothing is written until you validate the card, and Atlas checks the change
again at that moment. A repository of bricks to share is laid out like `~/.atlas`: `bricks/*.yml`,
`skills/<name>/SKILL.md` with its files, `subagents/<name>.md`.

A brick names the skills and subagents its sessions need in `skills` and `subagentTypes`; they
are read from `skills/` and `subagents/` and handed to that session only, as a plugin, on top of
what Claude Code already loads from `~/.claude`. In the session, a subagent is called
`atlas:<name>`, and a skill or subagent reaches the skill's own files through
`${CLAUDE_PLUGIN_ROOT}/skills/<skill>/`. Atlas ships the `deep-review` skill and the `minos`
subagent the review bricks use; like a brick, a shipped file follows the updates until you edit it.

Declare your repositories in `config.yml` so the orchestrator can launch agents in them:

```yaml
repos:
  - name: atlas
    path: /path/to/the/repository
    setup: pnpm install --frozen-lockfile   # run in each new worktree
```

The orchestrator can also add a repository at your request, from the chat. Each project has its
memory: notes (the host of an API, an install command, an access) every agent of the project reads
at the start of its session. An agent that learns such a thing offers you to keep it.

The other settings of `config.yml`:

| Key | Default | Role |
| --- | --- | --- |
| `port` | `4317` | Port of the daemon, on `127.0.0.1` |
| `orchestratorModel` | `sonnet` | Model of the orchestrator (`claude -p`) |
| `claudeCommand` | `claude` | Command that starts Claude Code |
| `agentArgs` | `[]` | Arguments added to every agent session |
| `defaultSteps` | the seven bricks from qualification to ship | Workflow of an agent launched without a specific one |
| `branchPattern` | `{type}/{ticket}/{name}` | Name of a new branch |
| `supervisorIntervalSeconds` | `30` | Delay between two supervisor passes |
| `approvalTimeoutSeconds` | `180` | Wait for a validation by the orchestrator before the step is approved as it stands |
| `orchestratorTimeoutSeconds` | `600` | Time after which a run of the orchestrator is given up |
| `orchestratorMaxContextTokens` | `60000` | Context size past which the chat moves to a fresh session |

The agents run with `--permission-mode bypassPermissions`, each in its own worktree. When the first
agent is launched in a repository, Atlas marks that repository as trusted in `~/.claude.json` (or
`$CLAUDE_CONFIG_DIR/.claude.json`): Claude Code files the trust of worktrees under their main
repository, so no agent stops on the trust question. The settings Atlas hands each session also
skip the warning of bypassPermissions, which would otherwise stop it before it starts.

The orchestrator runs `claude -p` in `--permission-mode auto`, with `Read`, `Glob`, `Grep`, `Bash`
and `WebFetch` to explore the machine for context: Claude Code's classifier turns down what the
master did not ask for, and its prompt tells it to change nothing unless he asks.

The review starts each pass with `/deep-review`: that skill can only be triggered as a command, not
by the model. It ships with Atlas in `~/.atlas/skills/deep-review`, with the `minos` subagent it
launches.

## Systems

| OS | Specifics |
| --- | --- |
| macOS | Native notifications |
| Linux | Packaged as `.deb` and `.rpm` (no AppImage: the daemon outlives the shell, an AppImage's mount does not). Notifications through `notify-send` (package `libnotify-bin`). Closing the window quits the interface, the daemon and its agents carry on: a desktop without a tray (stock GNOME) would have no way to bring a hidden window back. A `setup` command runs under `sh`, which is `dash` on Debian and Ubuntu: no `source`, no `[[ ]]`. Started from the desktop menu, Atlas may not see the `PATH` of your terminal: give `claudeCommand` an absolute path if `claude` is not found |
| Windows | Terminal through ConPTY; `claude.exe` (native installer) is started directly, a `claude.cmd` (npm) goes through `cmd.exe` |

## Layout

| Folder | Content |
| --- | --- |
| `crates/atlas-daemon` | The daemon: HTTP and WebSocket API, SQLite registry, PTY sessions, supervisor, orchestrator, MCP servers, Claude Code `hook` command |
| `crates/atlas-link` | How a local program finds and reaches the daemon: folder, port, token, local HTTP requests |
| `crates/foundry-git` | Git working folders (worktrees), a crate shared by the Cairn Foundry suite |
| `crates/foundry-pty` | Processes on a pseudo-terminal and screen mirror, a crate shared by the Cairn Foundry suite |
| `crates/atlas-desktop` | Tauri desktop shell: the native window that carries the front, the menu bar icon and the start of the daemon |
| `front` | React, Vite and shadcn/ui front, shown by the shell: the factory, the orchestrator's chat, the agents' terminal |

All the Rust lives in `crates/` (a single Cargo workspace), all the TypeScript in `front/`. The
Rust is the only description of the contract between the two: the daemon's tests write
`front/src/lib/contract.ts` (the types the front compiles) from `contract.rs`, and the daemon
derives `brick.schema.json` from its `Brick` type. After a contract change:

```sh
cd crates && ATLAS_UPDATE_CONTRACT=1 ATLAS_UPDATE_CONTRACT_SAMPLE=1 cargo test contract
```

## Checking

```sh
cd front && pnpm lint && pnpm typecheck && pnpm test                                          # front
cd crates && cargo fmt --all -- --check && cargo clippy --all-targets -- -D warnings && cargo test   # daemon and crates
cd crates && cargo clippy -p atlas-desktop --all-targets -- -D warnings && cargo test -p atlas-desktop   # shell
```

The shell is outside the default members of the workspace: it needs the system webview libraries,
so it is checked apart. The CI (`.github/workflows/ci.yml`) replays these commands, builds the
front and compiles the daemon with the oldest Rust promised (1.89).

To run Atlas without touching your real factory, point `ATLAS_HOME` at a throwaway folder whose
`config.yml` sets another `port`.

The rules to follow when contributing, as a human or as an agent, are in [AGENTS.md](AGENTS.md);
the sign-off and the license of a contribution are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

The daemon only listens on `127.0.0.1`. It refuses requests whose host is not local (DNS
rebinding) and all those, HTTP as well as WebSocket, sent by another page than the application's.
Every route but the health check `/api/health` asks for the token of `~/.atlas/token`, readable by
its owner only like the files that copy it: a browser or another local program that does not hold
it gets nothing. The shell gives it to its own page only.

## License

Atlas is distributed under the [GNU Affero General Public License v3.0](LICENSE), or any later
version (`AGPL-3.0-or-later`).

## Trademark

Cairn Foundry(TM) is a trademark of Benjamin Bonneton. The license covers the source code, not the
name or the logo. See [TRADEMARK.md](TRADEMARK.md).

## Copyright

Copyright (C) 2026 Benjamin Bonneton and the Cairn Foundry contributors. See [AUTHORS](AUTHORS).
