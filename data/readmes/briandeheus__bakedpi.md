# bakedpi

Website: [bakedpi.dev](https://bakedpi.dev)

bakedpi is a self-hosted AI engineering department: a git server, an issue
tracker, and a team of AI coding agents, assembled from proven open-source
parts and brought up on your own hardware with one command. You work as the
lead engineer. The agents work as your team.

An agent here doesn't push code at you. It picks up the issue you assigned it,
reads the codebase, and posts a plan. You correct the plan, or you approve it.
Then the agent implements, opens a pull request, and answers your review the
way a colleague would. When you merge, the issue closes.

The premise is simple: LLMs write good code now, but they don't carry what a lead
engineer (that's you!) carries. The architecture, the history, the taste, the reasons behind
"no". bakedpi doesn't try to teach the model any of that. It keeps that
judgment where it always lived: with you, in review. Every checkpoint a good
team relies on (the design conversation before the code, the review before the
merge) is part of the protocol, not a hope about model behavior.

In other words: this is the opposite of vibe coding. Your agents ask before
they build, take correction, and answer for their work.

Under the hood there is nothing bespoke, and nothing to learn.
[Forgejo](https://forgejo.org) provides the git hosting and the issue
tracker. The
[pi coding agent](https://github.com/earendil-works/pi) provides the
engineers, with any configuration and extension that pi supports. 
Postgres holds the data. bakedpi is the thin daemon that turns them into a team. 
All communication happens in the issue tracker, in plain conversation. 
There is no dashboard, no new interface, and no magic approval keyword. 
From one agent to a fleet, each with its own model, it all runs on your infrastructure.

## How it works

- The daemon polls Forgejo on an interval, like a person who checks the issue
  tracker.
- The daemon works in every repository that the bot account can access. Add
  the bot as a collaborator with write access to enroll a repository.
- A work item is an open issue assigned to the bot, or an open pull request
  that the bot authored. All items go through one global queue: one piece of
  work at a time.
- The daemon derives whose turn it is from the timeline. The agent acts when
  a human event is newer than the stored cursor. Comparison by creation time
  also catches a comment that landed while the agent composed a reply.
- The cursor is a small local state file per work item, under the data
  directory. A lost state directory is not fatal: the agent re-reads old
  events once.
- The agent memory is a pi session per issue. The session survives a restart
  of the daemon. Feedback on a pull request resumes the session of the issue
  that the pull request closes.
- The agent interprets your comments. There is no magic approval keyword.
  When a comment needs no response, the agent does nothing.

## Quick start

Docker Compose brings up the whole department: Forgejo, a Postgres database, and two
example workers, `bananapi` and `applepi`.

```bash
export OPENROUTER_API_KEY=sk-or-...
docker compose up bootstrap
docker compose up -d
```

The workers need model credentials, in one of two ways. Export
`OPENROUTER_API_KEY` to share one key across the fleet, as above. Or give a
worker its own credentials: run `./bin/provision-agent.sh <name>.pi` and fill
in the `auth.json` skeleton it creates. A worker with an `auth.json` does not
use the shared key.

The bootstrap step creates the accounts and writes one env file per worker
into `config/`. Then open `http://localhost:3000`, log in as `bakedpi-admin`
with the password `changeme` (set `BAKEDPI_ADMIN_PASSWORD` to change it), and
create a repository. Add a worker account as a collaborator with write
access, then assign an issue to it.

To add a worker: run `./bin/provision-agent.sh <name>.pi` to create its pi
configuration directory, add a service block in `compose.yaml`, add the name
to the `WORKERS` list in the bootstrap service, and run both commands again.

The stack also contains a Forgejo Actions runner, so the pull requests from
your agents get CI verdicts. Put workflow files under `.forgejo/workflows/`
in a repository, with `runs-on: docker`. If the repository does not show an
Actions tab, enable Actions in the repository settings.

Each worker mounts `config/<name>.pi/` as its pi configuration directory. Put
a pi `settings.json` there to give the worker its own default model, and an
`auth.json` to give it its own provider credentials. This makes a mixed fleet
possible: each worker runs a different model. An `AGENTS.md` there gives the
worker its standing instructions, and `extensions/` and `skills/` give it
plugins. An empty directory means: pi defaults plus the shared key.

## Bring your own Forgejo

The daemon also connects to a Forgejo instance you operate, without Docker.
It needs Node 22.19 or newer, and git.

1. Create a bot account on your Forgejo instance.
2. Give the bot account write access to each repository it works in.
3. Create an API token for the bot with the scopes `write:repository`,
   `write:issue`, and `read:user`.
4. Copy `env.example` to `.env` and fill in the values. Export the values, or
   use a process manager that reads the file.
5. Set `OPENROUTER_API_KEY`, or configure a provider with the `pi` CLI as the
   daemon user.

Then run:

```bash
npm install
npm run build
npm start
```

## Configuration

| Variable | Default | Description |
| --- | --- | --- |
| `BAKEDPI_FORGEJO_URL` | required | Base URL of the Forgejo instance. |
| `BAKEDPI_TOKEN` | required | API token for the bot account. |
| `BAKEDPI_BOT_USER` | `pi` | Login name of the bot account. |
| `BAKEDPI_CLONE_HOST` | empty | SSH alias for git. Empty: git works over HTTP with the API token. |
| `BAKEDPI_POLL_SECONDS` | `10` | Seconds between polls. |
| `BAKEDPI_DATA_DIR` | `~/.bakedpi` | Root directory for workspaces, sessions, and cursors. |
| `BAKEDPI_GIT_NAME` | bot user | Git author name for the agent commits. |
| `BAKEDPI_GIT_EMAIL` | `<bot user>@bakedpi.local` | Git author email for the agent commits. |
| `BAKEDPI_LOG_STREAM` | `on` | Stream the agent output and thinking to stdout. Set `off` for one-line summaries only. |
| `BAKEDPI_PROVIDER` | `openrouter` | Provider for the model override. |
| `BAKEDPI_MODEL` | empty | Model override, for example `deepseek/deepseek-v4-flash-0731`. |

The model resolves in this order: the `BAKEDPI_MODEL` override, then
`settings.json` in the worker's pi directory, then the pi default. The pi
default is the first available catalog model, which is arbitrary: set one of
the first two. Provider credentials come from `auth.json` or a provider env
variable such as `OPENROUTER_API_KEY`. In the Docker stack, export
`BAKEDPI_MODEL` next to the key to pin one model for the whole fleet.

The stream makes the container log a live view of the agent at work:

```bash
docker compose logs -f bananapi
```

## Agent instructions and plugins

bakedpi adds nothing of its own here: the workers use the pi resource
system. Everything lives in the worker's pi configuration directory
(`~/.pi/agent`, or `config/<name>.pi/` in the Docker setup) and in the
enrolled repository.

- Standing instructions: an `AGENTS.md` file in the worker's pi directory.
  It applies to every task, in every repository.
- Repository instructions: an `AGENTS.md` file in the enrolled repository.
  It applies to tasks in that repository only.
- Plugins: pi extensions, skills, and prompt templates in the worker's pi
  directory (`extensions/`, `skills/`), or pi packages listed in its
  `settings.json`. A worker gains a capability because a file exists in its
  configuration, not because of an bakedpi release.

Project-local extensions from an enrolled repository do not load: the
repository is untrusted for that purpose, by pi's own default.

## Use

Work with an agent like you work with an engineer on your team.

1. Create an issue in an enrolled repository. Describe the task.
2. Assign the issue to the bot account.
3. Read the proposal that the agent posts. Reply with an approval or with
   changes.
4. The agent implements the change, pushes the branch `pi/issue-<n>`, and
   opens a pull request that closes the issue.
5. Review the pull request. The agent pushes fixes and answers your comments.
6. If the agent is stuck, it asks in a comment. Reply to continue.

## Security notes

- The agent executes shell commands with no sandbox beyond its process user,
  or beyond its container in the Docker setup. Do not enroll repositories you
  do not trust.
- In the Docker setup, the container user has passwordless sudo, because the
  agent installs its own tools per repository.
- Workers clone over HTTP with their API token. The token lands in the git
  remote URL inside the workspace. Treat workspaces as secret-bearing.
- CI jobs run inside a Docker-in-Docker sidecar, not on the host Docker
  daemon. A job gets root inside that sandbox only. The sidecar itself runs
  privileged, which nested Docker requires: an escape from it is a kernel
  exploit away, not an API call away. Delete the `dind-data` volume to reset
  the whole CI environment.

## License

MIT. See [LICENSE](LICENSE).
