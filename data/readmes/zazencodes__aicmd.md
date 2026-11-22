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

macOS and Linux are supported.

## Recommended setup

Use an [OpenAI API key](https://platform.openai.com/api-keys) with GPT-6 Luna
and reasoning effort set to `none`.

```sh
export OPENAI_API_KEY='your-openai-api-key'
aicmd config set model openai-api/gpt-6-luna/none
aicmd list the ten largest files
```

New installs already select this model. Run `config set` to switch an existing
config to it.

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

`aicmd` supports hosted APIs, local models, and authenticated agent CLIs such
as Codex, Claude Code, and Antigravity. Direct API calls are billed by the
provider and avoid agent startup time.

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
| `-m <spec>`, `--model <spec>` | Override `provider/model/effort` for one request (e.g. `codex/gpt-6.2-sol/low`) |
| `-x`, `--verbose` | show effective configuration, the model prompt, and available thinking to stderr |
| `-v`, `--version` | print version |
| `-h`, `--help` | print usage |

The generated command is placed at your prompt for review. When output is redirected, e.g. with a pipe command, the `aicmd` result is printed instead of being inserted into the terminal.

See the [usage guide](docs/usage.md) for a more detailed guide on input forms, flag placement, terminal injection, pipelines, provider errors, and safety behavior.

## Configuration

The installer creates a documented starting config in `~/.config/aicmd.toml`

```toml
model = "openai-api/gpt-6-luna/none"  # provider/model/effort
clipboard = false                    # also copy the command to the clipboard
```

Manage it with the `config` subcommand:

```
aicmd config list                            show all settings
aicmd config get model                       print one setting
aicmd config set model codex/gpt-6.2-sol/low
aicmd config set clipboard on
```

Gemini and Claude also support direct API access through environment variables.

```sh
export GEMINI_API_KEY='your-gemini-api-key'
aicmd -m gemini-api/gemini-4-hydrogen/low list the ten largest files

export ANTHROPIC_API_KEY='your-anthropic-api-key'
aicmd -m claude-api/claude-sonnet-5-5/low list the ten largest files
```

Local models are available through Ollama and llama.cpp:

```sh
ollama serve
```

In another terminal, pull the model and run `aicmd`.

```sh
ollama pull gemma4:e2b
aicmd -m ollama/gemma4:e2b/none list the ten largest files
```

For llama.cpp, start the server and run `aicmd` in another terminal.

```sh
llama-server -hf ggml-org/gemma-4-E2B-it-GGUF:Q4_0 --alias gemma-4-e2b-it
aicmd -m llama/gemma-4-e2b-it/none list the ten largest files
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
