# AI SDLC Factory

**AI SDLC Factory** is an AI software factory built around a git host (Forgejo or GitHub), Temporal and disposable agent containers. You label a ticket on the host; role agents analyse it, write the code (or the fix, or the
incident advice) in isolated sandboxes, and the factory hands you a **reviewed pull request**. A person reviews and merges; the factory never merges.

![System overview](docs/images/architecture.svg)

## What it does

| Label the ticket | You get |
| --- | --- |
| `feature` | analysis, a check that it is not already built, an optional design review, the implementation, the project's own checks, code/security/UX review and an acceptance check, then a pull request |
| `bug` | a pull request with a fix **proven by a test that failed before and passes after**; the factory runs that proof itself |
| `docs` | a pull request that writes or updates `AGENTS.md`, `README.md` and `docs/` from the code, checked by the reviewers |
| `incident` | an assessment, ranked likely causes (every cited file and commit is verified) and mitigation options, driven by `/option`, `/hotfix` and `/resolved`; a draft postmortem on request. It never touches production |

On top of the labels, people steer with comments on a ticket or pull request (the [commands and labels cheat sheet](docs/commands.md) says what to type where): `/fix` (revise the pull request), `/update` (merge the base branch into it, resolving conflicts), `/review` (have the reviewers read any pull request and post findings), `/ask` (ask a question about the repository on any ticket or pull request; a read-only agent answers from the code), `/retry` (run a ticket again from the last good stage, or `/retry restart` from the beginning), `/qa` (test the running application, with `/qa full` and `/fix qa`), and `/option`, `/hotfix` and `/resolved` on incidents. The [alert intake](https://github.com/ai-sdlc-factory/ai-sdlc-factory-alert-intake) shows the incident side: a monitoring alert opens a ticket by itself and the factory starts on it.

Everything is deterministic where it matters: agents only advise with one validated JSON verdict, and code decides every next step. Each agent runs in a throwaway container with no route to the
internet except an allowlisting proxy. See [Architecture](docs/architecture.md) and [Workflows](docs/workflows.md).

## What you need, and where it stands

- Docker (Compose v2) on Linux, or Windows with WSL 2; about 10 GB of disk and 8 GB of RAM for Docker; a **ChatGPT Plus/Pro account** for the agents' model access. The full list is in [Getting started](docs/getting-started.md#what-you-need).
- It is built and tested on WSL 2 with a **ChatGPT sign-in**; an OpenAI API key or another model provider [may work but is untested](docs/opencode-login.md#other-ways-to-sign-in). **Forgejo** and **GitHub** have both been run live; other git hosts are not built (see [ideas](docs/ideas.md)).
- It is young software: expect rough edges, and read [Operations](docs/operations.md) for what is not built yet ("Known limitations"). It runs agents next to a Docker daemon, so read the [security notes](docs/operations.md#security-notes) before pointing it at repositories you do not trust.

## Quick start

1. [Set up the factory](docs/getting-started.md): configure `deploy/.env`, `docker compose up -d --build`, build the sandbox images, create the bot account, sign the agents in. About 30 minutes, once.
2. [Connect a repository](docs/project-setup.md): bot access, a webhook, labels, and a small `.factory/project.json`. About 5 minutes per repository.
3. Create a ticket, add the `feature` label, and watch the comments appear.

## Documentation

Start at the [documentation index](docs/README.md).

| Guide | Covers |
| --- | --- |
| [Getting started](docs/getting-started.md) | Installing and configuring the factory, step by step |
| [Setting up a project](docs/project-setup.md) | Webhook, labels, `.factory/project.json` (required and optional settings), `AGENTS.md` |
| [Workflows](docs/workflows.md) | Routing, every workflow (feature, bug, incident, plan, docs, revisions, updates, QA, reviews, the weekly report), quick mode, `/retry`, statuses, limits (with diagrams) |
| [Architecture](docs/architecture.md) | The parts, trust boundaries, where data lives |
| [Configuration](docs/configuration.md) | Every setting: `.env`, service variables, agents and models |
| [Operations](docs/operations.md) | Watching runs, troubleshooting, cleaning up, backups, security notes |
| [Design and decisions](docs/design.md) | Why it is built this way, and findings from running it |
| [Deployment](deploy/README.md) | Compose services, local addresses, the bot account |
| [Agents](agents/README.md) | The role files, permissions and models |
| [OpenCode login](docs/opencode-login.md) | Signing the agents in with a ChatGPT account |

## Repository

- [`deploy/`](deploy/README.md): Docker Compose and environment settings.
- [`src/`](src/): the code, one folder per service with its own Dockerfile and README, and the library they share; their tests are in [`tests/`](tests/), one folder per service. [`src/api/`](src/api/README.md): webhook intake. [`src/controller/`](src/controller/README.md): workflows, agent prompts and parsers, workspace and git host handling.
  [`src/sandbox-launcher/`](src/sandbox-launcher/README.md): the only service with Docker access. [`src/egress-proxy/`](src/egress-proxy/README.md): the proxy that decides what sandboxes may reach, with its [allowlist](src/egress-proxy/ALLOWLIST.md) (`profiles.json`).
- Next to the factory, in repositories of their own: [`ai-sdlc-factory-alert-intake`](https://github.com/ai-sdlc-factory/ai-sdlc-factory-alert-intake) (turns monitoring alerts into tickets) and [`ai-sdlc-factory-demo`](https://github.com/ai-sdlc-factory/ai-sdlc-factory-demo) (a production with monitoring around it, to see the whole loop). [`deploy/forgejo/`](deploy/forgejo/README.md) is a Forgejo to try the factory on.
- [`agents/`](agents/README.md): one Markdown file per agent role, plus shared OpenCode settings.
- [`templates/`](templates/README.md): working starter projects (.NET, Python, React, .NET + React) to copy, with every feature switched on.
- [`sandboxes/`](src/sandbox-launcher/README.md#images): Dockerfiles for the images agents run in (`dotnet`, `python`, `node`, and the combined `dotnet-node`, `python-node`, `full`, plus `browser` for end-to-end UI tests).
- [`src/contracts/`](src/contracts/Contracts.cs): the library the services share: wire types, with the git host list, triggers and webhook adapters in `Hosts/`.
- [`tools/`](tools/README.md): `check-docs.py` (the documentation check), `run-scenarios.py` (the workflow scenarios in parallel), `usage-report.py` (token totals from the usage log), `onboard-repo.py` (labels and webhook for a Forgejo or GitHub repository) and `check-clock.py`.

All services are C# on .NET 10; open [ai-sdlc-factory.slnx](ai-sdlc-factory.slnx) (it holds `src/` and `tests/`) in your IDE. Build settings live in [`Directory.Build.props`](Directory.Build.props) and NuGet versions in
[`Directory.Packages.props`](Directory.Packages.props); change a package version there, not in a project file.

## License

[MIT](LICENSE).
