# DevWeek

DevWeek is a small desktop app that uses AI to generate work reports from local Git commits.

I made it because I was tired of going through commit history whenever I needed to write a work report.

## What it does

- Reads commits from one or more local Git repositories.
- Filters commits by date and Git author.
- Lets you review and exclude commits before generation.
- Works with local Codex or Claude Code, as well as OpenAI-compatible APIs.
- Produces editable Markdown and checks generated work items against the selected commits.

## Run locally

You will need Node.js 22+, pnpm 10+, Rust stable, and the [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/) for your operating system.

```bash
pnpm install
pnpm tauri dev
```

Then:

1. Add one or more Git repositories.
2. Check the detected Git identity in Settings.
3. Select a time range and review the commits.
4. Choose a model and generate the report.
5. Edit or copy the generated Markdown.

## Models

### Local agents

DevWeek can use an existing Codex or Claude Code installation. The CLI must already be installed and signed in. DevWeek looks for it in `PATH`; `CODEX_BIN` and `CLAUDE_BIN` can be used to provide a custom path.

If needed, sign in first:

```bash
codex login
claude auth login
```

### OpenAI-compatible APIs

You can also provide an endpoint, model name, and API key in Settings. This works with providers such as OpenAI and DeepSeek, and with local servers such as Ollama.

For Ollama, use an endpoint such as `http://localhost:11434/v1`. An API key is not required.

## Data handling

- Commits can be reviewed before anything is sent to a model.
- Excluded commits and absolute repository paths are not sent.
- API keys are kept in memory and are not saved by DevWeek.
- Local agents run as temporary, non-interactive processes.

## Development

```bash
pnpm check
pnpm test:rust
```

Built with React, TypeScript, Tauri, and Rust.

## License

[Apache License 2.0](./LICENSE)
