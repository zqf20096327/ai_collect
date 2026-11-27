# Diderot

Diderot answers questions about what your organization has written down. It
ingests Slack, Discord, coding-agent sessions, Notion, Linear, Zendesk, and
folders of Markdown files into one Postgres event log, embeds everything into Qdrant, and runs an agent that
searches that corpus and answers with citations: in Slack, and as an MCP
server for your own agents and tools. You run one server, and administer it
in the browser at `/admin`.

Retrieval is vector-only: the question is embedded, Qdrant returns the nearest
chunks the caller is allowed to see, and results are deduplicated per event.
There is no reranker and no keyword index.

## Features

- **Sources.** Slack, with live Socket Mode events and a continuous sync that
  catches anything missed during restarts; image attachments are captioned and
  PDF, DOCX, and XLSX attachments are extracted to text. Coding-agent sessions
  (Antigravity, Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Pi,
  Polytoken, ATIF, Hugging Face STS), pushed over HTTP or polled from a
  session feed, summarized and expandable to the exact records behind a hit.
  Discord channels, threads and forum posts, over the gateway with a daily
  re-read. Notion page trees, Linear issues and comments, Zendesk tickets,
  comments, and Help Center articles, and the Markdown files in a mounted
  folder. A new
  source is one Go package and one registration line
  ([Adding a source](docs/adding-a-source.md)).
- **Permissions.** Every event carries a scope. Private Slack channels are
  visible only to their members, sessions can be owner-only, and a policy file
  grants groups access to restricted content. Every search is filtered to the
  caller's scopes.
- **Ask.** An agent that calls `retrieve`, `list`, and `expand` over the
  corpus and answers with inline citations. Mention `@diderot` in a Slack
  channel (each thread is one conversation) or DM it, or use the MCP `ask`
  tool or the HTTP API. Optional tools: web search (Tavily), code search
  (Sourcebot), and the read-only tools of any MCP servers you configure
  (deployment history, say), on Ask itself or on a delegated observability
  investigator.
- **MCP server.** `retrieve`, `list`, `expand`, `attachment`, and `ask` for
  your own agents at `/mcp`, on every install, with the same bearer token the
  HTTP API takes.
- **Slack extras.** Thread-summary message shortcuts, scheduled reports
  delivered to Slack, and optional investigations of PagerDuty alerts posted in
  the alert's thread.
- **Any model provider.** Add OpenAI, Anthropic, or any OpenAI-compatible
  endpoint (a gateway, a local vLLM or Ollama) in the admin UI; Diderot
  lists its models, and each job (embeddings, Ask, summaries, captions,
  document extraction) gets the one you choose, tested before it is saved.
- **Authentication.** OIDC bearer tokens from your IdP, static tokens, or a
  loopback-only no-auth mode for local use. The browser UI signs in through
  your IdP, sits behind an authenticating proxy, or signs in locally with a
  static token, and a fresh install has a bootstrap admin for first setup.
- **Admin UI.** Everything an administrator does is at `/admin`: setup,
  connectors and their channels, models, prompts, scheduled reports,
  operations, and every Ask session. A separate page lets people choose
  which of their agent sessions are private.

## Quickstart

[docs/quickstart.md](docs/quickstart.md) runs Diderot on one machine with
Docker Compose: Postgres, Qdrant, a local embedding model, and the server.
You need Docker and an OpenAI or Anthropic API key; Ask sends each question,
and the corpus text it reads to answer it, to that provider. To ingest your
own data, add a Linear API key, a Notion integration, a Slack app, or a
folder of Markdown files; out of the box it can index Diderot's own
documentation.

## Documentation

- [Quickstart](docs/quickstart.md): a working install with Docker Compose.
- [The `diderot` command](docs/cli.md): connecting coding agents to a
  server, and asking from the shell.
- [Setup](docs/setup.md): from the first sign-in to a live install.
- [Running in production](docs/production.md): what a deployment for a team
  needs, how replicas and leadership behave, and a Kubernetes example.
- [Upgrading](docs/upgrading.md): moving an existing install to a newer
  release.
- [Design](docs/design.md): how Diderot works, as built.
- [Configuration reference](docs/configuration.md): every environment
  variable.
- [Authentication and authorization](docs/auth.md): identity, scopes, the
  policy file, and each surface's authenticator.
- [Slack app setup](docs/slack-app.md): creating the Slack app from its
  manifest, connecting it, and what each permission is for.
- [Discord](docs/discord.md): creating the Discord bot, inviting it, and
  choosing the channels to index and who may read them.
- [Agent-session ingest](docs/session-ingest.md): accepted formats, the push
  protocol, and the session feed.
- [Tool connections](docs/mcp-servers.md): giving Ask the tools of your MCP
  servers, such as Grafana and Sentry.
- [Prompts](docs/prompts.md): where the model instructions live and how to
  change them.
- [Adding a source](docs/adding-a-source.md): writing a source of your own,
  with the Markdown folder source as the worked example.
- [Contributing](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md), for people and
  coding agents working on Diderot.

## Install, use, administer

**Install** by running the server: the [quickstart](docs/quickstart.md) with
Docker Compose, or [in production](docs/production.md) from the container
image.

**Use** it from Slack (`@diderot`, or a DM) and over MCP. On your own
machine, the [`diderot` command](docs/cli.md) connects your coding agents
(Claude Code, Codex, Cursor, OpenCode, Pi) to a server, installs the agent
skill, and asks questions from the shell:

```sh
diderot setup https://diderot.example.com --harness claude-code
diderot ask "What did we decide about the billing migration?"
```

Any other MCP client points at `https://<your-diderot>/mcp` with a bearer
token the server accepts (step 5 of the
[quickstart](docs/quickstart.md#from-zero-to-a-first-answer)).

Its tools are `retrieve` (semantic search), `list` (enumeration by source,
person, Slack channel, and time), `expand` (the fuller source behind one
hit, and its attachments), `attachment` (one image or document), and `ask`
(a cited answer; pass its `session_id` back to ask a follow-up). The same
token works on the plain HTTP API: `POST /v1/ask`, `/v1/retrieve`,
`/v1/list`, and `/v1/expand-chunk`.

[`skills/diderot`](skills/diderot/SKILL.md) is the agent skill that teaches a
coding agent when and how to use those tools; `diderot setup` installs it.

**Administer** it in the browser at `/admin`, the one place an install is
set up and run from.

## What the `diderot` binary does

The container image holds one binary, `diderot`: the server, its
maintenance commands, and the client commands `setup`, `doctor`, `ask`, and
`sessions`.
[Releases](docs/cli.md#install) carry a small `diderot` for people's
machines with the client commands alone, which reach a server over MCP and
can ship the machine's coding-agent sessions to it
([The `diderot` command](docs/cli.md)). The server commands below run where
the server runs (`docker compose exec diderot diderot ...`,
`kubectl exec deploy/diderot -- diderot ...`) because they read the server's
own configuration.

| Command | What it does | When to run it |
| --- | --- | --- |
| `diderot serve` | Runs the server: the API, `/mcp`, the admin UI, and every background worker. It applies pending database migrations as it starts. | Always; it is the container's command. |
| `diderot probe <healthz\|readyz>` | Asks the local server whether it is up, or ready, and exits non-zero if not. | As a container health check or a Kubernetes exec probe ([production](docs/production.md)). |
| `diderot qdrant-audit` | Compares the vector index with the database and queues what is missing or wrong for the server's workers to repair. | After changing the embedding model, restoring a backup, or losing the Qdrant volume. |
| `diderot reset-admin` | Turns the bootstrap admin sign-in (`admin` / `admin`) back on. | When no administrator can sign in any more. Turn it off again from the setup checklist. |

Two more commands, `ui-dev` and `session-dev`, serve parts of the UI from
fixtures for people working on Diderot itself
([CONTRIBUTING.md](CONTRIBUTING.md)).

## Status

Diderot is under active development, and compatibility across versions is
not guaranteed: the MCP tools, the HTTP API, schemas, and settings change
together, and breaking changes are called out in the release notes
([Upgrading](docs/upgrading.md)).

## Security

Please report security issues privately, as described in
[SECURITY.md](SECURITY.md): email `security@bsky.app`. Don't open a public
issue.

## License

This project is dual-licensed under MIT and Apache 2.0 terms:

- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)
- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)

Downstream projects and end users may choose either license individually, or both together, at their discretion. The motivation for this dual-licensing is the additional software patent assurance provided by Apache 2.0.

Bluesky Social PBC has committed to a software patent non-aggression pledge. For details see [the original announcement](https://bsky.social/about/blog/10-01-2025-patent-pledge).
