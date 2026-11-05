# aicmd

Turn plain English into a shell command without leaving your terminal.

<p>
  <a href="https://github.com/zazencodes/aicmd/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/zazencodes/aicmd/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/zazencodes/aicmd/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/zazencodes/aicmd?display_name=tag&sort=semver"></a>
  <a href="https://github.com/zazencodes/aicmd/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/zazencodes/aicmd/total"></a>
</p>

```
>>> aicmd <description of command...>
<ai-generated command>    <-- inserted into terminal, ready to execute

>>> aicmd spin down the app on 8080
pids=$(lsof -ti tcp:8080); [ -z "$pids" ] || kill $pids

>>> aicmd list js files recursively by date modified
find . -type f -name '*.js' -print0 | xargs -0 stat -f '%m %N' | sort -n
```

<p align="center">
  <img src="https://storage.googleapis.com/zazencodes-prod-public-assets/img/aicmd/aicmd-demo.gif" alt="aicmd demo" width="100%">
</p>

## Install

```sh
curl -fsSL https://github.com/zazencodes/aicmd/raw/refs/heads/main/install.sh | sh
```

MacOS and Linux are supported.

## Why aicmd

Stay in the terminal:

- **Be faster.**
- **Use your mouse less.**

Smart AI options:

- **CLI Agents** – AI that you already pay for.
- **Direct API** – Lower latency but higher cost per token.
- **Local LLM** – Completely free but less capable.

<p align="center">
  <a href="https://zazencodes.com/?utm_source=github&utm_medium=referral&utm_campaign=aicmd">
    <img
      src="docs/assets/zazencodes-banner.png"
      alt="ZazenCodes — Engineering for the Agentic Era"
      width="100%"
    >
  </a>
  <br>
  Created by <a href="https://zazencodes.com/">ZazenCodes</a>
</p>

## How it works

`aicmd` is very simple. It finds the best terminal command for your prompt.

The generated command appears on a new line, ready to send. You can review, modify and run it as you like.

It's powered by the CLI that you already pay for: Codex, Claude Code or Antigravity, e.g. `codex/gpt-5.6-terra/low`

Or you can use the APIs directly. This incurs some API costs but often has lower latency.

Under the hood, your `aicmd` request is dynamically injected into the following prompt, which is passed to the underlying LLM:

```
You convert natural language into a single shell command.

Environment:
- OS: <os>
- arch: <arch>
- shell: <shell>
- cwd: <cwd>

Rules:
- Output ONE single-line shell command and nothing else.
- No markdown, no backticks, no explanation, no leading `$` prompt.
- The command must run as-is in the environment above.

Request: <your request>
```


## Usage

```sh
aicmd <description of command...>
```

Flags:

| Flag | Meaning |
| --- | --- |
| `-m <spec>`, `--model <spec>` | model spec override: `provider/model/effort` (e.g. `codex/gpt-5.6-terra/low`) |
| `-x`, `--verbose` | show effective configuration, the model prompt, and available thinking to stderr |
| `-v`, `--version` | print version |
| `-h`, `--help` | print usage |

The generated command is placed at your prompt for review. When output is redirected, e.g. with a pipe command, the `aicmd` result is printed instead of being inserted into the terminal.

See the [usage guide](docs/usage.md) for a more detailed guide on input forms, flag placement, terminal injection, pipelines, provider errors, and safety behavior.

## Configuration

The installer creates a documented starting config in `~/.config/aicmd.toml`

```toml
model = "openai-api/gpt-5.6-luna/none"   # provider/model/effort
clipboard = false                   # also copy the command to the clipboard
```

Manage it with the `config` subcommand:

```
aicmd config list                            show all settings
aicmd config get model                       print one setting
aicmd config set model codex/gpt-5.6-terra/medium
aicmd config set clipboard on
```

API-backed providers use environment variables for credentials:

```sh
export OPENAI_API_KEY=...
aicmd -m openai-api/gpt-5.6/low <your request>

export GEMINI_API_KEY=...
aicmd -m gemini-api/gemini-3.7-flash/low <your request>

export ANTHROPIC_API_KEY=...
aicmd -m claude-api/claude-sonnet-4-6/low <your request>
```

Local models are available through Ollama and llama.cpp:

```sh
ollama serve
aicmd -m ollama/gemma4:e2b/none <your request>

llama-server -hf ggml-org/gemma-3-4b-it-GGUF --alias gemma-3-4b-it
aicmd -m llama/gemma-3-4b-it/none <your request>
```

See the [local LLM guide](docs/local-llms.md) for server setup, endpoint
overrides, authentication, and provider differences.

## Development

Go 1.24. API providers use the official OpenAI Go SDK, pinned to the final
release compatible with Go 1.24.

```sh
make build       # build ./aicmd
make test        # unit tests
make vet         # go vet
make build-all   # cross-compile all 4 targets into dist/
```

Releases are tag-triggered (`.github/workflows/release.yml`): pushing a `v*`
tag builds the 4 targets, packages `aicmd_<os>_<arch>.tar.gz` +
`checksums.txt`, and creates a GitHub release.

## Documentation

- [Requirements](docs/requirements.md) — supported platforms and CLI, hosted
  API, and local LLM inference options
- [Usage guide](docs/usage.md) — prompts, flags, output behavior, safety, and
  provider troubleshooting
- [Configuration guide](docs/configuration.md) — settings, model specs,
  provider differences, clipboard support, and config file format
- [Local LLMs](docs/local-llms.md) — Ollama and llama.cpp setup and configuration
- [Platform support](docs/portability.md) — terminal injection behavior on
  macOS, Linux, and Windows
- [Architecture decision records](docs/adr/README.md) — lasting design
  decisions and repository guardrails
- [Modular provider architecture](docs/modular-providers-spec.md) — the
  implemented design specification for provider integrations

## Release notes

Each [GitHub release](https://github.com/zazencodes/aicmd/releases) includes a
curated summary of user-visible changes. The Git history remains the detailed
engineering record.
