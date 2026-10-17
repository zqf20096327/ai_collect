&nbsp;
# mini-coding-agent-eino

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Go Version](https://img.shields.io/badge/go-1.27-00ADD8.svg)](go.mod)

**A minimal local coding agent built on the
[CloudWeGo eino](https://github.com/cloudwego/eino) framework — the framework-variant
sibling of [mini-coding-agent-go](https://github.com/aiongo/mini-coding-agent-go), using
native tool-calling instead of a hand-rolled text protocol.**

**English** | [简体中文](README.zh-CN.md)

> **Two variants of the same agent.** This repo rebuilds it on eino's ADK
> (`ChatModelAgent` + native tool-calling). Its sibling
> **[mini-coding-agent-go](https://github.com/aiongo/mini-coding-agent-go)** is the
> framework-free port — faithful to the Python original down to the code structure and
> agent flow.

This repo contains a small standalone coding agent:

- code: a single `main` package (`agent.go`, `tools.go`, `model.go`, ...)
- CLI: `mini-coding-agent-eino`

It is a minimal local agent loop with:

- workspace snapshot collection
- stable prompt plus turn state
- structured tools
- approval handling for risky tools
- transcript and memory persistence
- bounded delegation

The model backend is currently based on Ollama.

<a href="https://magazine.sebastianraschka.com/p/components-of-a-coding-agent">
  <img src="https://substack-post-media.s3.amazonaws.com/public/images/49b97718-57f4-4977-99c8-8ad5c4d32af3_1548x862.png" width="500px">
</a>

<br>

**[The detailed tutorial: Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)**
— both variants trace back to the Python original component by component.

&nbsp;
## Differences from mini-coding-agent-go

The agent's shape — six components, seven tools, approval gates, sessions, REPL — is the
same as the framework-free [mini-coding-agent-go](https://github.com/aiongo/mini-coding-agent-go).
What changes is the engine:

- **Native tool-calling**: the model calls tools through the provider's tool-call API
  (`/api/chat` + tools), not by emitting `<tool>...</tool>` / `<final>...</final>` text.
  The model must therefore support tool calling.
- **adk ChatModelAgent**: the ReAct loop (model → tool → model) is driven by
  `eino/adk.ChatModelAgent` with the system prompt injected as its `Instruction`, instead
  of a hand-written ask() loop with tolerant parsing.
- **eino-ext components**: the Ollama `ChatModel`, the local filesystem `Backend`
  (read/write/edit/grep), and `utils.InferTool` for deriving tool JSON schemas from Go
  structs.
- **Error folding**: recoverable tool errors are returned to the model as
  `"error: ..."` results instead of aborting the turn, so the model can react and retry.
- **Sequential tool execution**: multiple tool calls in one turn run one at a time,
  eliminating same-file write races.
- **Extra tool — `python_execute`**: run Python code through a backend-shared executor
  (`--python-cmd`; empty disables the tool).
- **Debug**: `MC_EINO_DEBUG=1` prints each step (role / tool name / content excerpt) to
  stderr; request/response traffic is appended to `.mini-coding-agent/agent.log`.
- `--max-steps` defaults to `12` (the framework loop benefits from more headroom).

&nbsp;
## Six Core Components

<a href="https://magazine.sebastianraschka.com/p/components-of-a-coding-agent">
  <img alt="Six core components of a coding agent" src="https://sebastianraschka.com/images/github/mini-coding-agent/six-components.webp" width="500px">
</a>

This coding harness is organized around six practical building blocks:

1. **Live repo context**
   The agent collects stable workspace facts upfront, such as repo layout, instructions, and git state.
2. **Prompt shape and cache reuse**
   A stable prompt prefix, which is separate from the changing request, transcript, and memory so repeated model calls can reuse the static parts efficiently.
3. **Structured tools, validation, and permissions**
   The model works through named tools with checked inputs, workspace path validation, and approval gates instead of free-form arbitrary actions.
4. **Context reduction and output management**
   Long outputs are clipped, repeated reads are deduplicated, and older transcript entries are compressed to keep prompt size under control.
5. **Transcripts, memory, and resumption**
   The runtime keeps both a full durable transcript and a smaller working memory so sessions can be resumed while preserving important state via working memory.
6. **Delegation and bounded subagents**
   Scoped subtasks can be delegated to helper agents that inherit enough context to help (but operate within limits).

&nbsp;
## Requirements

You need:

- Go 1.27+
- Ollama installed
- an Ollama model pulled locally (with tool-calling support)

&nbsp;
## Install Ollama

Install Ollama on your machine so the `ollama` command is available in your shell.

Official installation link: [ollama.com/download](https://ollama.com/download)

Then verify:

```bash
ollama --help
```

Start the server:

```bash
ollama serve
```

In another terminal, pull the default model used by this project:

```bash
ollama pull gemma4:cloud
```

The agent talks to Ollama's `/api/chat` endpoint with tools attached, so the model must
support tool calling; any tool-calling model exposed by your Ollama instance works.

&nbsp;
## Project Setup

Clone the repo or your fork and change into it:

```bash
git clone https://github.com/aiongo/mini-coding-agent-eino.git
cd mini-coding-agent-eino
```

Build the binary:

```bash
go build        # produces ./mini-coding-agent-eino
```

Or install it directly into your `GOBIN`:

```bash
go install github.com/aiongo/mini-coding-agent-eino@latest
```

&nbsp;
## Basic Usage

Start the interactive REPL:

```bash
./mini-coding-agent-eino
```

Run a single prompt without entering the REPL:

```bash
./mini-coding-agent-eino prompt "Inspect this repo and summarize the layout"
```

(`prompt` has the alias `p`.)

By default it uses:

- model: `gemma4:cloud`
- approval: `ask`

For a concrete usage example, see [EXAMPLE.md](EXAMPLE.md).

&nbsp;
## Approval Modes

Risky tools such as shell commands and file writes are gated by approval.

- `--approval ask`
  prompts before risky actions (default and recommended)
- `--approval auto`
  allows risky actions automatically, including arbitrary command execution and file writes by the model; use only with trusted prompts and trusted repositories
- `--approval never`
  denies risky actions

Example:

```bash
./mini-coding-agent-eino --approval auto
```

&nbsp;
## Resume Sessions

The agent saves sessions under the target workspace root in:

```text
.mini-coding-agent/sessions/
```

Resume the latest session:

```bash
./mini-coding-agent-eino --resume latest
```

Resume a specific session:

```bash
./mini-coding-agent-eino --resume 20260401-144025-2dd0aa
```

&nbsp;
## Interactive Commands

Inside the REPL, slash commands are handled directly by the agent instead of
being sent to the model as a normal task.

- `/help`
  shows the list of available interactive commands
- `/memory`
  prints the distilled session memory, including the current task, tracked files, and notes
- `/session`
  prints the path to the current saved session JSON file
- `/reset`
  clears the current session history and distilled memory but keeps you in the REPL
- `/exit`
  exits the interactive session
- `/quit`
  exits the interactive session; alias for `/exit`

&nbsp;
## Main CLI Flags

```bash
./mini-coding-agent-eino --help
```

CLI flags are passed before the agent starts. Use them to choose the workspace,
model connection, resume behavior, approval mode, and generation limits.

Important flags:

- `--cwd`
  sets the workspace directory the agent should inspect and modify; default: `.` (current directory)
- `--model`
  selects the Ollama model name (must support tool calling); default: `gemma4:cloud`
- `--host`
  points the agent at the Ollama server URL (usually not needed); default: `http://127.0.0.1:11434`
- `--ollama-timeout`
  controls how long the client waits for an Ollama response (usually not needed); default: `300` seconds
- `--resume`
  resumes a saved session by id or uses `latest`; default: start a new session
- `--approval`
  controls how risky tools are handled: `ask`, `auto`, or `never`; default: `ask`
- `--max-steps`
  limits how many model and tool turns are allowed for one user request; default: `12`
- `--max-new-tokens`
  caps the model output length for each step; default: `4096`
- `--temperature`
  controls sampling randomness; default: `0.2`
- `--top-p`
  controls nucleus sampling for generation; default: `0.9`
- `--python-cmd`
  sets the Python interpreter used by the `python_execute` tool (as the backend's env sees it); empty disables the tool; default: `python3`

&nbsp;
## Example

See [EXAMPLE.md](EXAMPLE.md)

&nbsp;
## Notes & Tips

- The model must support native tool calling — this variant does not parse any
  `<tool>`/`<final>` text protocol.
- Different Ollama models follow tool-calling instructions with different reliability.
- `MC_EINO_DEBUG=1` prints every step (role / tool name / content excerpt) to stderr.
- Debug traffic (prompts and raw responses) is appended to `.mini-coding-agent/agent.log`
  under the workspace root.
- The agent is intentionally small and optimized for readability, not robustness.

&nbsp;
## License

The code in this repository is licensed under the [MIT License](LICENSE).

It is a Go port of [rasbt/mini-coding-agent](https://github.com/rasbt/mini-coding-agent),
which is licensed under Apache 2.0; that license is retained in
[LICENSE-APACHE](LICENSE-APACHE) for the portions derived from the original.

&nbsp;
## Credits

- Original Python implementation and design write-up:
  [Sebastian Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)
- Original repo: [rasbt/mini-coding-agent](https://github.com/rasbt/mini-coding-agent)
- Framework-free sibling: [aiongo/mini-coding-agent-go](https://github.com/aiongo/mini-coding-agent-go)
- eino framework: [cloudwego/eino](https://github.com/cloudwego/eino)
