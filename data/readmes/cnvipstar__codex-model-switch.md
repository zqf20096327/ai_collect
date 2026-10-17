# codex-model-switch

> One command to toggle the **OpenAI Codex** CLI/App between a **local model** (Ollama / any OpenAI‑compatible provider) and the **native cloud model** — with an interactive menu, surgical config edits, and automatic backups.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Shell](https://img.shields.io/badge/shell-bash-1f425f.svg)

**[中文说明 / Chinese README →](README.zh-CN.md)**

<p align="center">
  <img src="assets/menu.png" alt="codex-model interactive menu" width="640">
</p>

---

## Why this exists

The Codex desktop App's model picker only lists the models on your **cloud** account — local Ollama models never appear in that dropdown. The model Codex actually uses is driven by `~/.codex/config.toml` (`model` + `model_provider`).

Editing that by hand is easy to get wrong. The classic failure is leaving `model = "gpt-5.5"` while pointing `model_provider` at Ollama:

```
unexpected status 404 Not Found: model 'gpt-5.5' not found, url: http://localhost:11434/v1/responses
```

`codex-model-switch` flips exactly the right keys for you — and nothing else.

## Features

- 🧭 **Interactive menu** — lists your installed local models *and* your cloud models; pick a number.
- ⚡ **Scriptable** — `local` / `native` / `status` subcommands for one-liners and automation.
- 🔒 **Surgical edits** — only the top-level `model` / `model_provider` / `oss_provider` keys are rewritten. Your projects, MCP servers, plugins and desktop settings are left untouched.
- 💾 **Safe** — atomic write + a timestamped backup on every switch.
- ✅ **Pre-flight checks** — warns if the local endpoint is down or the chosen model isn't installed.

## Background — Codex OSS mode & local providers

Based on the official guide: **[Codex → Advanced configuration → OSS mode & local providers](https://developers.openai.com/codex/config-advanced#oss-mode-local-providers)**.

Codex can talk to local OpenAI-compatible servers (Ollama, LM Studio). The minimal `config.toml` for the built-in Ollama provider:

```toml
model = "gpt-oss:20b"
model_provider = "ollama"   # built-in provider → http://localhost:11434/v1
oss_provider   = "ollama"   # used by the `--oss` flag
```

For a custom endpoint, define a provider table (per the docs):

```toml
[model_providers.local_ollama]
name     = "Ollama"
base_url = "http://localhost:11434/v1"
wire_api = "chat"   # "chat" = Chat Completions (most compatible); "responses" = Responses API
```

**Hard-won notes:**
- That `404 ... not found` is almost always a **model-name mismatch** (your `model` value isn't installed locally), **not** a broken endpoint.
- Recent Ollama serves both `/v1/chat/completions` and `/v1/responses`; the `gpt-oss` family pairs well with `model_reasoning_effort = "high"`.
- Each Codex conversation stores **its own** `model` + `model_provider`, so your old cloud threads keep working after you change the global default — only *new* conversations follow the default.

## Requirements

- macOS or Linux, with `bash`, `python3`, `curl`
- [OpenAI Codex](https://developers.openai.com/codex) CLI or desktop App (so `~/.codex/config.toml` exists)
- A local provider for local mode — e.g. [Ollama](https://ollama.com) with at least one model pulled (`ollama pull gpt-oss:20b`)

## Install

```bash
git clone https://github.com/cnvipstar/codex-model-switch.git
cd codex-model-switch
chmod +x codex-model.sh

# Option A — quick alias (zsh)
echo "alias codex-model=\"$PWD/codex-model.sh\"" >> ~/.zshrc && source ~/.zshrc

# Option B — installer (symlinks into ~/.local/bin)
./install.sh
```

## Usage

```bash
codex-model                  # interactive menu
codex-model local            # local default (gpt-oss:20b)
codex-model local gpt-oss:120b
codex-model native           # cloud default (gpt-5.5)
codex-model native gpt-5.4
codex-model status           # show current mode
```

Interactive menu looks like:

```
════════════ Codex model switch ════════════
current: ☁️  NATIVE  (cloud, model=gpt-5.5)

── 🖥  Local (http://localhost:11434/v1) ──
   1) gpt-oss:120b
   2) gpt-oss:20b
   3) qwen3-coder:30b
── ☁️  Codex native (cloud) ──
   4) gpt-5.4
   5) gpt-5.5
  ───────────────
   m) ✍️  enter a model name manually
   q) cancel

Select a number:
```

> ⚠️ **Codex reads `config.toml` at startup.** After switching, **restart the Codex App (or open a new conversation)** for it to take effect.

## Configuration (environment variables)

| Variable | Default | Meaning |
|---|---|---|
| `CODEX_HOME` | `~/.codex` | Codex home directory (where `config.toml` lives) |
| `CODEX_MODEL_DEFAULT_LOCAL` | `gpt-oss:20b` | default model for `local` |
| `CODEX_MODEL_DEFAULT_NATIVE` | `gpt-5.5` | default model for `native` |
| `CODEX_MODEL_PROVIDER_ID` | `ollama` | value written to `model_provider` (set to your `[model_providers.<id>]`) |
| `CODEX_MODEL_OSS_PROVIDER` | `ollama` | value written to `oss_provider` |
| `CODEX_MODEL_LOCAL_API` | `http://localhost:11434/v1` | OpenAI-compatible endpoint used to list/verify local models |

Example for LM Studio:

```bash
export CODEX_MODEL_LOCAL_API="http://localhost:1234/v1"
export CODEX_MODEL_PROVIDER_ID="lmstudio"
export CODEX_MODEL_OSS_PROVIDER="lmstudio"
```

## How it works

1. Reads `config.toml`, splits off the **preamble** (everything before the first `[table]` header).
2. Removes any existing top-level `model` / `model_provider` / `oss_provider` lines.
3. Prepends the new keys — for `local` it writes all three; for `native` it writes only `model` (so Codex falls back to its built-in cloud provider).
4. Writes to a temp file and `os.replace()`s it (atomic), after copying a `.bak-codex-model-<timestamp>`.

## FAQ

### Does this work with the Responses API (`wire_api`)?

Yes — and it's handled at the **provider** level, not by this tool. `wire_api = "responses"` uses `/v1/responses`; `wire_api = "chat"` uses `/v1/chat/completions`.

**Recent Ollama supports the Responses API**, and Codex's built-in `ollama` provider uses it — `gpt-oss` models run fine over `/v1/responses` (tested). Nothing to configure.

If your local server doesn't implement `/v1/responses` (older Ollama, LM Studio, llama.cpp, …), define a provider with `wire_api = "chat"`:

```toml
[model_providers.local]
name     = "Local"
base_url = "http://localhost:11434/v1"
wire_api = "chat"
```

…then point the switcher at it: `export CODEX_MODEL_PROVIDER_ID=local`.

`codex-model-switch` only rewrites `model` / `model_provider` / `oss_provider`; `wire_api` is set once in the provider block, so both protocols are supported.

## Caveats

- The Codex **App dropdown will not show local models** — that's cosmetic; `config.toml` is the source of truth.
- A **restart** is required after switching.
- If you pick a *cloud* model from the App dropdown while the provider is still local, you may hit the same `404`; just re-pick the model.

## License

[MIT](LICENSE) © 2026 laosun ([@cnvipstar](https://github.com/cnvipstar))
