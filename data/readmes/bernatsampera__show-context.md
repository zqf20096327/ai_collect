# show-context

**See what fills your Claude Code context window, and where each answer came from.**

```text
npx show-context
```

Run it inside any Claude Code session (as `! npx show-context`). It opens one local page with the whole conversation and every file, search, MCP result, skill and web page the session read, sized by real token use.

<p align="center">
  <img src="docs/demo.webp" alt="show-context: select an answer, trace it to its source, see every read and its token size" width="400">
</p>

## Why

I asked Claude Code a simple question about the Express codebase. Before it read a single line of code, the session already held **33,003 tokens**: 12k of tool definitions, 7.8k of skill descriptions, 6.4k of MCP instructions. The file reads that answered the question? **1,873 tokens.**

You can't see any of that from the chat. show-context makes it visible, so you know what to trim and which answers to trust.

## What you get

**Where did this come from?** Select any sentence Claude wrote and ask. A split view links it, with numbered lines, to the exact passages in the files it read. Select text inside a tool call to ask why the call was made.

![Where did this come from: an answer linked to the exact lines in server.js, todos.js and storage.js](docs/screenshot-ask.png)

**Show context mode.** What loaded at session start (system prompt, tools, CLAUDE.md, skills, MCP), then each read in order. Block height grows with token size, colors mark File, Explore, MCP, Skill and Web reads. A size filter hides the small stuff (under 2,000 tokens by default). Click a row to see its full text.

![Show context mode: start load parts and session reads](docs/screenshot.png)

## Install

```text
npm install -g show-context
```

Or run it without installing: `npx show-context`. Requires Node.js 22 or later. No dependencies.

## Use

Inside Claude Code:

```text
! show-context
```

From a terminal, pick a session by ID or prefix:

```text
show-context <session-id-or-prefix>
```

| Option | What it does |
| --- | --- |
| `--no-open` | Print the live URL, don't open the browser |
| `--static` | Write a static page, no local server |
| `--help` | Show all options and environment variables |

Environment variables: `SHOW_CONTEXT_OUT` (output file, default `~/.cache/show-context/show-context.html`), `SHOW_CONTEXT_PROJECTS` (Claude projects folder), `SHOW_CONTEXT_PORT`, `SHOW_CONTEXT_IDLE_MS` (server idle timeout, default 30 minutes), `SHOW_CONTEXT_CLAUDE_BIN` (Claude Code binary).

## Privacy and how it works

- It reads one local session transcript and never changes it.
- The page is a single self-contained HTML file. The optional server binds to `127.0.0.1` only, and every route needs a random 32-byte token.
- Token counts come from the real input token use of each model call. When several items enter one call together, the increase is split by their character count.
- Reads are files, shell reads and searches, MCP reads, skills and web results. Writes, edits and commands that run things are not reads.
- **Only *Where did this come from?* uses the network.** It runs your local Claude Code CLI on a fork of the session with no tools, and costs tokens like any Claude Code call. The fork is not saved, and your session stays untouched.

## Limits

- It depends on the Claude Code transcript format, which can change.
- Subagent reads are not shown yet.
- *Where did this come from?* works with Claude Code only.

## Contributing

Issues and PRs are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [good first issues](https://github.com/bernatsampera/show-context/labels/good%20first%20issue).

## License

MIT
