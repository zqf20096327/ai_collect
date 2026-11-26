# rhebok

[![Stellenbosch-Technologies/rhebok MCP server](https://glama.ai/mcp/servers/Stellenbosch-Technologies/rhebok/badges/score.svg)](https://glama.ai/mcp/servers/Stellenbosch-Technologies/rhebok)
[![Listed on mcpservers.org](https://mcpservers.org/badge.svg)](https://mcpservers.org/servers/stellenbosch-technologies/rhebok)
[![CI](https://github.com/Stellenbosch-Technologies/rhebok/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Stellenbosch-Technologies/rhebok/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/Stellenbosch-Technologies/rhebok)](https://github.com/Stellenbosch-Technologies/rhebok/releases/latest)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue)](LICENSE)
[![Platform: macOS | Linux](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](#install)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-D97757)](docs/install.md)
[![MCP server](https://img.shields.io/badge/MCP-server-blue)](docs/usage.md)
[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-orange?logo=rust)](https://www.rust-lang.org)

Your coding agent starts every session knowing nothing you have not pasted in.
The decision you wrote up last month, the fix you found in yesterday's
session, the paper in your Downloads folder: it can use none of them unless
you find them and hand them over.

rhebok hands them over. It is local, semantic search over your own knowledge
base (notes, papers, web clippings and past agent sessions), and it adds what
is relevant to your coding agent's prompts automatically.

rhebok indexes the folders you point it at, embeds them with a small model
running on your own machine through [Ollama](https://ollama.com), and serves
the results two ways:

- **Automatic context.** A prompt hook adds the most relevant passages to
  every prompt, but only when they clear a confidence gate.
- **On-demand search.** An MCP tool lets the agent search your knowledge base
  whenever it decides to.

It works with Claude Code, Codex, Gemini CLI, Cursor and Claude Desktop. It
also keeps durable memories (lessons and facts that carry across sessions) and
has a local web dashboard for searching, exploring and configuring everything.

![rhebok answering a question from your notes: vector, keyword and graph results fused, and only what clears the confidence gate injected](docs/images/demo.gif)

Nothing leaves your machine unless you set it up to: embeddings run locally
and there is no telemetry. rhebok itself goes online only to check daily for a
newer release, to download its vector-search extension the first time it
builds an index, to fetch the OCR model the first time it reads a scanned PDF,
and to fetch pages you add with `rhebok add <url>`. If you turn them on, it
also sends text to an embedding endpoint you choose and backs up to your own
S3 bucket or Google Drive.

## Why rhebok?

- **Context arrives on its own.** Most memory and search tools for agents
  are an MCP tool the agent has to remember to call. In Claude Code, Codex
  and Gemini CLI, rhebok also injects context into every prompt
  automatically, but only what clears a calibrated confidence gate, so the
  agent isn't flooded with noise.
- **It remembers your past sessions.** Your Claude Code and Codex
  transcripts are indexed too, so "how did we fix this last time?" has an
  answer when the agent searches with `rhebok_search` or you run
  `rhebok search`. Finished sessions are also distilled into short episode
  memories. The automatic prompt context prefers your notes and keeps raw
  transcripts out by default.
- **Retrieval you can inspect.** Vector, keyword and link-graph results are
  fused, superseded decision records are demoted, and the dashboard shows
  exactly what each stage found and what reached the prompt.
- **Local and simple.** One Rust binary, embeddings through Ollama on your
  machine, no cloud API, no telemetry and no server to run.
- **One index for every agent.** Claude Code, Codex, Gemini CLI, Cursor and
  Claude Desktop all use the same knowledge base.

## How it compares

| | rhebok | claude-mem | mem0 | basic-memory | mcp-memory-service |
|---|:-:|:-:|:-:|:-:|:-:|
| Searches your notes on every message you send | ✅ ¹ | ❌ ² | ❌ ³ | ❌ ⁴ | ❌ ⁵ |
| Reads the notes you already have | ✅ | ❌ | ❌ | ✅ | ✅ ⁶ |
| Remembers your past chats with the agent | ✅ | ✅ | ✅ | ❌ ⁷ | ✅ |
| Works without a cloud account | ✅ | ✅ | ❌ | ✅ | ✅ |
| Tests how well it finds *your* notes | ✅ | ❌ | ❌ | ❌ ⁸ | ❌ |

1. It adds notes only when they are a good match, so most messages get none.
2. Only when a session starts, unless you switch it on.
3. Only on the first message.
4. Only when a session starts.
5. Only when a message sounds like it needs memory, such as "what did we
   decide".
6. Only files you add to it.
7. Only chats you export and import.
8. Its test kit is built for public datasets.

The others do things rhebok does not. claude-mem writes summaries of what
your agent did. mem0 can keep your memory in the cloud. basic-memory lets the
AI write your notes for you. [The full comparison](docs/comparison.md) has
the details and a source for every answer, checked on 2026-11-20.

## Install

You need a Mac with Apple silicon, or Linux on x86_64 or arm64 with glibc
2.39 or newer (Ubuntu 24.04 or newer), plus [Ollama](https://ollama.com)
running and a coding agent such as Claude Code. On Windows, use the Linux build
inside WSL. Intel Macs have no release build.

```bash
curl -fsSL https://github.com/Stellenbosch-Technologies/rhebok/releases/latest/download/install.sh | sh
```

The installer puts `rhebok` on your PATH, downloads the embedding model (about
640 MB, after asking), registers the Claude Code plugin, and offers to connect
the other agents it finds. It also offers the optional session distillation
model (about 2.5 GB). With [Homebrew](https://brew.sh), install it with
`brew install stellenbosch-technologies/tap/rhebok`, then run `rhebok install`.
Other ways to install, including building from source, are in the
[install guide](docs/install.md).

rhebok used to be called br8n. If you used br8n, install rhebok the same way:
`rhebok install` moves your br8n index, memories and config, and your agent
connections, to rhebok. A br8n binary cannot update itself to rhebok.

## Get started

1. **Choose what to search.** Run `rhebok dashboard` and follow the three-step
   setup, or do it from the terminal:

   ```bash
   rhebok config set sources '["~/notes", "~/Documents/papers"]'
   rhebok index
   ```

2. **Restart your agents** so they load rhebok.
3. **Check it works:**

   ```bash
   rhebok status                        # every install check should pass
   rhebok search "something in your notes"
   ```

Two lines are only information. The `ocr:` line says whether the optional
OCR libraries are installed; without them, text PDFs are still indexed and
only scanned pages are skipped. A missing distillation model is listed as
optional; without it, finished sessions are not turned into episode memories.

Then ask your agent about something from your notes. After the first index,
rhebok re-reads only what changed, and each new Claude Code session refreshes
the index in the background.

## Everyday commands

```bash
rhebok dashboard            # search, graph, memories, health and settings in the browser
rhebok app                  # the same dashboard as a native Mac app, Rhebok.app
rhebok search "query"       # search from the terminal
rhebok index                # pick up new or changed files
rhebok status               # index size, settings and any problems
rhebok connect codex        # connect another agent (see: rhebok agents)
rhebok update               # install the newest release
rhebok restart              # restart the dashboard and any running index on the installed binary
rhebok uninstall            # remove rhebok; keeps the config, index and memories
```

`rhebok uninstall --purge` also deletes the index, every memory, the config,
the golden set and the default backup key. The
[install guide](docs/install.md#uninstall) lists what to save first.

## Roadmap

- **Native Windows support** is planned. Until then, use the Linux build
  inside WSL.
- **Intel Macs** have no release build yet, because of an upstream library
  issue.

Ask a question, share an idea or show what you built in
[Discussions](https://github.com/Stellenbosch-Technologies/rhebok/discussions).
Report a bug in the
[issues](https://github.com/Stellenbosch-Technologies/rhebok/issues), and see
[CONTRIBUTING.md](CONTRIBUTING.md) to get started on the code. Please report
security problems privately, as [SECURITY.md](SECURITY.md) describes. Everyone
taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Documentation

- [Install guide](docs/install.md): every install option, building from
  source, updating, uninstalling and install problems
- [Using rhebok](docs/usage.md): indexing, memory, the dashboard, connecting
  agents and slash commands
- [Configuration and tuning](docs/configuration.md): the config file, quality
  tiers, ranking, remote embedding endpoints and scanned PDFs
- [Backups](docs/backups.md): encrypted backups of your config, memories and
  index to S3 or Google Drive
- [Security model](docs/security-model.md): what can reach your prompts, and
  how to limit it
- [How rhebok compares](docs/comparison.md) with claude-mem, mem0,
  basic-memory and mcp-memory-service
- [Troubleshooting](docs/troubleshooting.md)
- [Cutting a release](docs/releasing.md), for maintainers

## License

rhebok is licensed under the [GNU Affero General Public License v3.0](LICENSE)
(AGPL-3.0-only). You can use, modify and share it freely; if you distribute a
modified version, or run one as a service that others use over a network, you
must make your source code available under the same licence.

Copyright (C) 2026 Stellenbosch Technologies and rhebok contributors
