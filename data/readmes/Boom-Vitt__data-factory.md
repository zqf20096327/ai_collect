<p align="center"><img src="assets/banner.svg" alt="data-factory: every AI conversation you have ever had, in one factory on your own disk" width="100%"></p>

# data-factory

[![test](https://github.com/Boom-Vitt/data-factory/actions/workflows/test.yml/badge.svg)](https://github.com/Boom-Vitt/data-factory/actions/workflows/test.yml)

### One factory for every AI conversation you have ever had.

You talk to Claude Code, Codex, Gemini, Antigravity, ChatGPT, Grok and a dozen other agents. Every question, every answer and every piece of finished work is scattered across hidden folders in a dozen formats, or locked in someone else's cloud.

`data-factory` pulls all of it into one plain JSONL store on your own disk: searchable today, ready to fine-tune your own local model tomorrow.

- **One file, zero dependencies.** `factory.py` is plain Python standard library (3.9 or newer) and runs on macOS, Linux and Windows.
- **Nothing leaves your machine.** No account, no server, no telemetry.
- **You choose what is collected.** Name a folder and it is never read again.
- **No hooks to install.** It reads the transcripts your agents already write.
- **One MCP server**, connected to all your agents with one command.
- **One page** that shows your whole factory, popped up in your browser whenever an agent uses it.

## Quick start

```bash
git clone https://github.com/Boom-Vitt/data-factory
```

```bash
python3 data-factory/factory.py collect
```

```text
claude-code    3125 sessions found,   3006 updated,    39325 messages written
codex            62 sessions found,     62 updated,     1343 messages written
gemini            2 sessions found,      0 updated,        0 messages written
antigravity      12 sessions found,     12 updated,      751 messages written
```

Run it again any time. Only sessions that changed are rewritten, so it is safe to put on a timer:

```bash
(crontab -l 2>/dev/null; echo "0 * * * * python3 $PWD/data-factory/factory.py collect") | crontab -
```

On Windows, the same with Task Scheduler:

```bash
schtasks /create /sc hourly /tn data-factory /tr "python C:\path\to\data-factory\factory.py collect"
```

### Choose what is collected

Keep a folder out of the factory, for example client work:

```bash
python3 data-factory/factory.py exclude ~/work/client-project
```

This deletes the conversations already stored from that folder (and everything inside it) together with the images and files pasted into them, rebuilds the training files without them, and skips the folder on every later collect. `exclude` with no folder shows the list, and `exclude FOLDER --remove` takes one off again. The list is a plain file, `~/.data-factory/exclude.txt`.

It works for agents that record which folder a conversation happened in: Claude Code and Codex. Gemini CLI, Antigravity, web exports and `factory_log` entries carry no folder, so they cannot be excluded this way.

To stop the factory page opening in your browser, set `DATA_FACTORY_NO_OPEN=1` for the MCP server.

### Connect your agents

One command connects the factory to every AI client it finds on your machine:

```bash
python3 data-factory/factory.py install
```

```text
Claude Code     connected. Start a new session to use it.
Codex           connected. Start a new session to use it.
Gemini CLI      connected. Start a new session to use it.
Claude desktop  connected. Quit and reopen the app to load it. (previous config saved as claude_desktop_config.json.bak)
```

Clients that are not installed are skipped. To connect just one, name it: `factory.py install codex`.

Each client then has three tools: `factory_log`, `factory_search` and `factory_show`. Clients load MCP servers when a session starts, so open a new session before you look for them.

| Client | Where to see it |
| --- | --- |
| Claude Code | type `/mcp` in a new session |
| Codex | `codex mcp list` |
| Gemini CLI | `gemini mcp list` |
| Claude desktop app | with the app's local MCP servers, after a restart |

The first tool call in each agent session opens the factory page (`~/.data-factory/index.html`) in your browser: a 3D factory floor you can drag to turn, with one machine per agent, conveyor belts carrying conversations in and crates of training pairs coming out, plus tables of totals and your latest sessions. Under the floor it lists what your data can train (search, a test set, a prompt router, report writing, summaries, a Thai assistant, OCR, speech), how many examples you have for each, and which open model to start from. Every later call refreshes it, and the open tab reloads itself. It is a local file; nothing is served or uploaded.

<details>
<summary>Set it up by hand, or in another MCP client</summary>

Any client that can launch a local (stdio) MCP server works. The command is `python3 /path/to/data-factory/factory.py mcp`.

```bash
claude mcp add --scope user data-factory -- python3 /path/to/data-factory/factory.py mcp
```

```bash
codex mcp add data-factory -- python3 /path/to/data-factory/factory.py mcp
```

```bash
gemini mcp add -s user data-factory python3 /path/to/data-factory/factory.py mcp
```

For clients configured with JSON (Claude desktop's `claude_desktop_config.json`, Cursor, and others):

```json
{ "mcpServers": { "data-factory": { "command": "python3", "args": ["/path/to/data-factory/factory.py", "mcp"] } } }
```

</details>

**Why is it not under Connectors in Claude?** Connectors are remote servers on the internet that Claude's cloud calls. The factory is a local program that reads files on your own disk, which is the point: your conversations never leave your machine. Turning it into a Connector would mean publishing your store at a public address.

### Ask your agent

- "Show me the factory."
- "Search the factory for how we fixed the Supabase auth bug last month."
- "Save this question and your answer to the factory."

### Use the terminal

```bash
python3 factory.py show
```

```bash
python3 factory.py search "docker compose"
```

```bash
python3 factory.py import ~/Downloads/chatgpt-export.zip
```

```bash
python3 factory.py ocr ~/my-ocr-dataset
```

```bash
python3 factory.py export
```

`ocr` indexes every `{"image": ..., "text": ...}` record in the JSONL manifests under a folder, as image + correct-text pairs for training an OCR model. It records where each image is rather than copying it, and keeps anything under a `test` path apart as a held-out test set.

`export` writes two files in the chat `messages` format that fine-tuning tools (MLX, Unsloth, Axolotl, llama.cpp) accept, one prompt and its full answer per line. It also runs at the end of every `collect`, so they are always current.

| File | What is in it |
| --- | --- |
| `train.jsonl` | Requests you typed yourself (60 characters or longer) |
| `train_briefs.jsonl` | Briefs one AI wrote for another, with the report that came back. Kept apart because both sides are machine-written |

Left out of both: short steers ("done?", "continue"), agent-to-agent messages, context summaries, automated OCR calls, and exact repeats of a prompt. The sorting is by keyword rules, so check a sample before training on it.

## What gets collected

| Agent | How | Where it is read from |
| --- | --- | --- |
| Claude Code (CLI, desktop, IDE, Orca workers) | `collect` | `~/.claude/projects` |
| Codex (CLI, app, Orca workers) | `collect` | `~/.codex/sessions` |
| Gemini CLI | `collect` | `~/.gemini/tmp/*/chats` |
| Antigravity | `collect` | `~/.gemini/antigravity/brain` |
| ChatGPT | `import` | your data export (`.zip`) |
| Claude.ai chat | `import` | your data export (`conversations.json`) |
| Grok, Cowork, anything else with MCP | `factory_log` tool | the agent saves its own turns |

## How it works

Every message becomes one line:

```json
{"source": "codex", "session": "rollout-…", "role": "user", "text": "…", "ts": "2026-11-14T09:42:06Z", "model": "…", "cwd": "/path/to/project"}
```

Stored as `~/.data-factory/sessions/<source>/<session>.jsonl` (set `DATA_FACTORY_HOME` to move it). Tool calls, tool output and harness chatter are dropped, so what remains is what you asked and what the agent told you.

Images and files you pasted into a chat are kept too (Claude Code and Codex). Each is saved once under `~/.data-factory/media/`, named by its content hash, and the message that carried it gains a `"media": ["ab/abcd….png"]` field. Images an agent read by itself through a tool, such as screenshots, are tool output and are not stored.

## Privacy

Your conversations contain your code, your clients and your keys. So:

- The store lives **outside** this repository and is never committed.
- Common secret shapes (API keys, tokens, JWTs, private keys) are replaced with `[REDACTED]` on the way in. This is a safety net, not a guarantee: run a real scanner before you share or train on the data.
- Pasted images and files are stored exactly as they were. Nothing inside a picture is redacted, so a screenshot of a password stays a screenshot of a password.
- Only collect conversations you have the right to keep, and `exclude` the folders you should not.
- Some AI providers restrict using their models' output to train other models. Check the terms of the services you use before you train on this data.

## FAQ

**Does it capture a prompt the moment I send it?** No. It sweeps the transcripts agents already save, so schedule `collect` hourly. That means no hooks inside your agents and nothing to break when they update.

**Why JSONL files and not a database?** `grep`, `jq`, pandas and every training tool read them directly. Add a database when a real query needs one.

**An agent is missing.** A source is one glob and one ~6-line parser in `SOURCES` in `factory.py`. Pull requests welcome; please include a line in `test_factory.py`.

**Is the format stable?** The seven fields above are, plus the optional `media` list. Agent transcript formats are not, and they change without notice: if a source suddenly collects nothing, open an issue.

## Contributing

```bash
python3 test_factory.py
```

It runs against a temporary fake home and touches none of your data. The same check runs on Linux, macOS and Windows for every pull request.

## License

MIT
