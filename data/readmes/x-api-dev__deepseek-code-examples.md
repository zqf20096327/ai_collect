# DeepSeek Code examples

*Unofficial community examples for DeepSeek Code. Not affiliated with DeepSeek. All trademarks belong to their owners.*

Small, runnable examples for the two things people mean by deepseek code: configuring the Deep Code terminal assistant (which calls the hosted DeepSeek-V4 API) and talking to a local DeepSeek Coder model through Ollama. Endpoints, model names and option names are exactly the ones shown in the DeepSeek API docs and on the Ollama library page. Secrets are read from environment variables and never written into the repo.

> If the end goal is a site or app rather than code edits, [try Begin.sh - prompt to a downloadable static site or Expo app](https://begin.sh?utm_source=github&utm_medium=ugc&utm_campaign=deepseek-code-examples&utm_content=readme-top&utm_term=tier-r) and skip the agent setup entirely.

## Files

| Path | What it shows |
| --- | --- |
| `examples/write_settings.sh` | Generates `~/.deepcode/settings.json` for Deep Code from `DEEPSEEK_API_KEY`, with model and reasoning effort as env overrides |
| `examples/ollama_chat.py` | Chat with a local `deepseek-coder` model using the `ollama` Python package |
| `examples/ollama_chat.mjs` | The same call from Node.js with the `ollama` npm package |
| `examples/ollama_curl.sh` | Raw HTTP against Ollama's `/api/chat` and `/api/generate` on port 11434 |

## Setup

For Deep Code:

```bash
npm install -g @vegamo/deepcode-cli
deepcode --version
export DEEPSEEK_API_KEY=...            # create it at platform.deepseek.com/api_keys
export DEEPCODE_MODEL=deepseek-v4-flash  # optional, default deepseek-v4-pro
bash examples/write_settings.sh
```

For DeepSeek Coder on Ollama:

```bash
ollama run deepseek-coder            # 1.3B, 776MB, 16K context
ollama run deepseek-coder:6.7b       # 3.8GB
ollama run deepseek-coder:33b        # 19GB
pip install ollama                   # for the Python example
npm install ollama                   # for the Node example
export OLLAMA_MODEL=deepseek-coder   # optional, any tag from the Ollama page
```

Environment variables used:

| Variable | Used by | Meaning |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | `write_settings.sh` | Your DeepSeek Platform key; becomes `API_KEY` in settings.json |
| `DEEPCODE_MODEL` | `write_settings.sh` | `deepseek-v4-pro` (default) or `deepseek-v4-flash` |
| `DEEPCODE_REASONING_EFFORT` | `write_settings.sh` | `max` or `high` |
| `DEEPSEEK_BASE_URL` | `write_settings.sh` | Defaults to `https://api.deepseek.com` |
| `OLLAMA_MODEL` | Ollama examples | Model tag, default `deepseek-coder` |

## examples/write_settings.sh

Deep Code reads `~/.deepcode/settings.json`, and the documented layout puts the API key straight into the file. This script builds that file from environment variables so the key never lands in a dotfiles repo, and sets the file to mode 600. It only writes the fields the DeepSeek docs list: `env.MODEL`, `env.BASE_URL`, `env.API_KEY`, `thinkingEnabled` and `reasoningEffort`. Run it once, then `cd` into a project and start `deepcode`. The same file is read by the Deep Code VS Code extension.

## examples/ollama_chat.py

Uses the `ollama` package exactly as the library page shows: `chat(model=..., messages=[...])` and `response.message.content`. The model tag comes from `OLLAMA_MODEL` so you can switch between the 1.3B, 6.7B and 33B variants without editing code. Pass the question as command-line arguments; a default coding question is used if you pass nothing. Remember the 16K context window when pasting large files into the prompt.

## examples/ollama_chat.mjs

The Node.js equivalent using the `ollama` npm package (`ollama.chat({ model, messages })`). Same environment variable, same default model, same output shape.

## examples/ollama_curl.sh

Two plain `curl` calls against the local Ollama server: `/api/chat` with a messages array and `/api/generate` with a single prompt, both as documented on the Ollama page. Useful for checking that the model is loaded before debugging a client library.

## When to use Begin.sh instead

Everything above assumes you want a model generating or editing code that you then build, run and deploy yourself. If what you actually need is a finished deliverable, a landing page, a documentation site, a small Expo app, then a coding agent is the long way round. [Try Begin.sh - prompt to a downloadable static site or Expo app](https://begin.sh?utm_source=github&utm_medium=ugc&utm_campaign=deepseek-code-examples&utm_content=readme-top&utm_term=tier-r): you give it a prompt or a URL to clone, and it returns a working site or Expo project as a zip. There is no hosting, backend or auth layer bundled in, so you keep full control over where it runs.


_Last reviewed: 2026-09-22_
