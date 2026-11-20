<p align="center">
  <a href="https://fyrr.dev"><img src="docs/assets/banner.png" alt="fyrr: serverless context layer for software factories and AI agents. No database. Just a bucket. The logo over a dithered sea chart of knowledge islands named after the apps it indexes." width="100%"></a>
</p>

<p align="center"><b>Blazing-fast, serverless context layer for software factories and AI agents. No database. Just a bucket.</b></p>

<p align="center">
  <a href="https://fyrr.dev">Website</a> ·
  <a href="https://fyrr.dev/docs/quickstart">Docs</a> ·
  <a href="https://fyrr.dev/use-cases">Use cases</a> ·
  <a href="https://fyrr.dev/compare">Compare</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="License: Apache-2.0"></a>
  <a href="rust-toolchain.toml"><img src="https://img.shields.io/badge/rust-1.97%2B-orange.svg" alt="Rust 1.97+"></a>
</p>

> **Pre-1.0.** Cloud connectors are tested against synthetic APIs only.

## For coding agents

**Coding agents know your code. fyrr gives them everything else.** An agent
that writes code on its own sees only the repository. It does not know why
the ticket exists, what the team agreed in chat or what was already tried.
fyrr lets it look that up.

- **Understand: it reads the ticket and the discussion first.** Before it
  writes code, the agent searches your tickets, chats, pull requests and docs
  for what was asked, agreed and already tried
  ([MCP tools](docs/mcp-tools.md)).
- **Scale: run as many agents as you like.** Every agent searches the same
  index straight from your S3 bucket. There is no server to grow when you add
  more agents ([topology](docs/deployment.md#topology)).
- **Protect: each agent sees only what it needs.** Let bug-fixing agents read
  engineering docs and nothing else. If a malicious issue tricks one into
  looking for salaries, it finds nothing ([security](docs/security.md)).
- **Trace: see what the agent had read.** Every search result says which
  version of your knowledge it came from. When a change goes wrong, you can
  check what the agent knew.

A software factory is a set of coding agents that turn tickets into pull
requests with nobody watching each step.
[Set one up with fyrr](docs/software-factory.md).

## For people and their AI

**Ask the whole company. Without asking the whole company.** The same context
layer answers the AI apps your people already use. Everyone asks in their own
words and gets only what they are allowed to read.

- **Find: works in the AI you already use.** Plug fyrr into Claude, Cursor or
  any MCP app. Ask there, and it searches your docs, chats, tickets and code
  over stdio or Streamable HTTP ([MCP tools](docs/mcp-tools.md)).
- **Protect: only what each person may read.** fyrr syncs each document's
  access rules with its content and checks them inside the search, before
  anything is ranked. A forbidden document looks exactly like one that does
  not exist, and missing permission data refuses rather than guesses
  ([how](docs/architecture.md#authorization), [security](docs/security.md)).
- **Scale: as many readers as you need.** Readers only read from the bucket
  and never coordinate, so you add more as you grow.
- **Own: your data stays yours.** It runs in your own cloud. Text leaves it
  only for the embedding model you choose.

Connectors for local files, Google Drive, Notion, GitHub, Slack and Jira; a
Python SDK lets you [write your own](docs/connectors/authoring.md).

## 16 milliseconds. Among the best results.

Fast enough for an agent to search at every step: a 16 ms median search, 25 ms
at p95. Accurate enough to trust what comes back: a 90+ score on
EnterpriseRAG-Bench, among the best of 43 systems tested. The
[open comparison](https://fyrr.dev/compare) measures quality, latency, ingest
and running cost against self-hosted alternatives, with its full protocol.

## No database. Just a bucket.

Everything fyrr knows lives as files in one S3 bucket, or in a private local
directory. Small teams run nothing around the clock; a whole company adds one
small service. The reader also runs on [AWS Lambda](docs/lambda.md)
(experimental): no always-on reader server, pay per request.

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/architecture-light.svg">
  <img src="docs/assets/architecture.svg" alt="Sources sync through the writer into S3 or local disk; the reader checks permissions before returning MCP results.">
</picture>

## From one laptop to the whole company.

| Way | What runs |
| --- | --- |
| **Just you** | Your files, notes and repos, searched by your coding agent. |
| **A team** | One shared index, no server. Each teammate's agent searches it directly. |
| **The company** | One index and one server, behind your company login. |
| **Training & evals** | A fixed index that changes only when you update it. Search it in parallel. |

Every way: no database. See [use cases](https://fyrr.dev/use-cases) and
[deployment](docs/deployment.md).

## Quick start

With Docker, the [published image](docs/quickstart.md#fastest-the-published-image)
indexes a Markdown folder and answers over MCP in a few commands, with no
build.

To build from source, follow the [quickstart](docs/quickstart.md) to search a Markdown folder from
Claude Code using a private local directory. It needs Linux x86-64 and the
tools git, curl, unzip, openssl, Python 3.11+, rustup, uv, a C compiler, jq,
binutils, network access and about 10 GiB free; no accounts
or embedding keys are needed. The guide also covers adding Slack and trying
Ada/Grace permissions. For shared deployments, see
[deployment](docs/deployment.md).

After setup in the quickstart:

```sh
fyrr writer namespace create
fyrr writer sync
fyrr writer commit
claude mcp add fyrr --scope user -- "$PWD/target/debug/fyrr" --config "$FYRR_CONFIG" reader serve
```

Start Claude Code from the same shell, so that the reader gets
`FYRR_IDENTITY_KEY`, and ask:

> Use fyrr search and fetch to answer: How do I restore a backup? Quote the handbook.

The example's top hit is `notes/backup.md`, with the answer:
"To restore a backup, run the restore job and verify the checksum."

## Limits

- **You need a stable release.** fyrr is pre-1.0: storage formats and the
  MCP schema may break before 1.0; data is then republished, not migrated.
  [Releases](https://github.com/fyrr-ai/fyrr/releases) carry binaries, images
  and the SDK wheel.
- **You need proven cloud connectors.** Google Drive, Notion, GitHub, Slack
  and Jira have been tested only against synthetic APIs, not real workspaces.
- **Your documents are not text.** There is no PDF, Office or image
  extraction.
- **You cannot send text to an embeddings service.** You provide an
  OpenAI-compatible `/embeddings` endpoint, and document and query text is
  sent to it.
- **You do not run Linux.** Linux (x86_64, aarch64) is the only supported
  platform, for builds, binaries and images.
- **You need phrase queries.** The full-text index stores no term positions.
- **You want TLS built in.** The HTTP listener speaks plain HTTP; outside
  loopback it needs a TLS-terminating proxy.

## Documentation

| Page | Content |
| --- | --- |
| [Quickstart](docs/quickstart.md) | Build, configure and search a local folder |
| [How fyrr works](docs/architecture.md) | Terms, publication, authorization and retrieval |
| [Security model](docs/security.md) | Trust boundaries, permissions and secrets |
| [HTTP login and users](docs/http-users.md) | Authenticate and enroll HTTP users |
| [Deployment](docs/deployment.md) | Production setup, images and scheduling |
| [AWS Lambda](docs/lambda.md) | Experimental reader deployment |
| [Operations](docs/operations.md) | Monitor, restore, retire and upgrade |
| [Software factories](docs/software-factory.md) | Context for a fleet of unattended coding agents |
| [Connect an agent](docs/connect.md) | Add fyrr to Claude Code, Codex or another MCP client |
| [Configuration](docs/configuration.md) | Storage, embeddings, sources and secrets |
| [Identity](docs/identity.md) | Users, directories, keys and OIDC |
| [Tuning](docs/tuning.md) | Namespace and retrieval settings |
| [Reader and writer settings](docs/reader-writer.md) | Serving, retention and maintenance settings |
| [CLI](docs/cli.md) | Commands, flags and exit statuses |
| [MCP tools](docs/mcp-tools.md) | Tool arguments, results and transport |
| [Connectors](docs/connectors/README.md) | Setup and limits per source |
| [Writing a provider](docs/connectors/authoring.md) | Connector SDK contract and example |

## Contributing

Bug reports, connector requests and pull requests are welcome; for larger
changes, open an [issue](https://github.com/fyrr-ai/fyrr/issues/new/choose)
first. [CONTRIBUTING.md](CONTRIBUTING.md) covers the build, `scripts/ci` and
the contract rules. Report vulnerabilities privately as described in
[SECURITY.md](SECURITY.md), and follow the
[code of conduct](CODE_OF_CONDUCT.md). Notable changes are listed in the
[changelog](CHANGELOG.md).

## License

fyrr is licensed under the [Apache License 2.0](LICENSE); see [NOTICE](NOTICE).
