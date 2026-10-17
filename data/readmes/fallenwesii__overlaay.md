# Overlaay

A fast, minimal quick-access AI overlay for window managers.

It exists to answer questions faster than opening a browser or desktop AI client — a global-hotkey launcher that appears, answers, and gets out of the way.

## Screenshots

![overlaay](/screenshots/preview.png)

## Features

- **Blazing Fast**: Resident Python daemon keeps persistent TLS connections to providers.
- **Hyprland Native**: Built on Quickshell layer-shell (`WlrLayershell`) with screen-capture exclusion (`noscreenshare layyerrule`).
- **Two States**: Compact pill input when summoned, expanding smoothly when tokens arrive.
- **Provider Choice**: Groq, Cerebras, OpenRouter, Anthropic Claude, Ollama and OpenAI via user-supplied API keys.
- **Opt-in Search**: Instant `/w <query>` or `@web <query>` DuckDuckGo web search via `ddgr` with zero overhead on normal queries.
- **Rich Markdown**: Fast HTML markdown rendering powered by `rich` and `pygments` with inline CSS styles and remote image sanitization.
- **Theming**: Ships with Tokyo Night default; fully extensible via JSON (`~/.config/overlaay/themes/*.json`) for `matugen`, `pywal` and other theme generators.

## Quick Start

### 1. Installation

Run the setup script:

```bash
./setup.sh
```

Ensure `~/.local/bin` is in your `$PATH` and reload Hyprland, if you are not using hyprland add the keybind `SUPER + ALT + O` for launching overlaay to your config:

### 2. Set API Keys

Add your provider API key to `~/.bashrc` or your shell environment:

```bash
export GROQ_API_KEY="gsk_..."
# or
export ANTHROPIC_API_KEY="sk-ant-..."
# or
export OPENAI_API_KEY="sk-..."
```

### 3. Usage

- **Toggle Overlay**: Press `SUPER + ALT + O` (or run `overlaay`).
- **Ask Query**: Type your question and press `Enter`.
- **New Query**: Press `Ctrl + Enter` to clear the response and start fresh.
- **Search Web**: Prefix with `/w ` or `@web ` (e.g. `/w latest Hyprland release notes`).
- **Dismiss**: Press `Esc` .

### 4. CLI Usage

Direct terminal queries without UI:

```bash
overlaay query "explain goroutines in one paragraph"
```

### 5. Configuration

Config file is at `~/.config/overlaay/config.toml`:

```toml
default_provider = "groq"
theme = "tokyonight"
```

change provider and model to your preferences
