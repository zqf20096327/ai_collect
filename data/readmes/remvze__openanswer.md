# OpenAnswer

OpenAnswer is a small AI utility for asking questions from the terminal. Its output is plain text, so it composes naturally with other command-line tools.

## Requirements

- Node.js 20+
- An OpenAI API key

## Installation

```bash
npm install --global openanswer
answer config
```

You can also set `OPENAI_API_KEY` instead of storing a key in the config.

## Usage

```bash
answer "Why is the sky blue?"
cat text.txt | answer "Summarize this"
cat error.log | answer "Explain the likely cause" | copy
cat question.txt | answer
```

Start a multi-turn conversation:

```bash
answer chat
```

Chat mode remembers the conversation until you type `exit`, `quit`, or `q`.
It does not have permission to run commands; use `answer run` for that.

Allow OpenAnswer to run commands for a request:

```bash
answer run "Do I have Python installed?"
answer run --yes "Check whether Python and Node are installed"
```

Commands require confirmation by default. `--yes` (or `-y`) permits all commands
for that request without prompting. When stdin is piped, use `--yes` because the
terminal input is not available for confirmation:

```bash
cat error.log | answer run --yes "Investigate this error"
```

OpenAnswer tells the model which operating system, architecture, shell, terminal,
working directory, and Node.js version it is running with. Commands are executed
with that same detected shell.

## Configuration

```bash
answer config
answer config show
answer config key sk-...
answer config key --clear
answer config model gpt-5.3-codex
answer config reset
```

## Development

```bash
pnpm install
pnpm build
```

## License

MIT. See [LICENSE](./LICENSE).
