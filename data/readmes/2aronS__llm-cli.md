# llm-cli

![license](https://img.shields.io/badge/license-MIT-blue)
![status](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-3.8+-blue)
![pypi](https://img.shields.io/badge/pypi-v0.1.0-orange)
![downloads](https://img.shields.io/badge/downloads-1k%2Fmonth-green)

> Command-line interface for querying large language models

## table of contents

- [install](#install)
- [usage](#usage)
- [api](#api)
- [contributing](#contributing)
- [license](#license)

## install

```
pip install llm-cli
```

## usage

```bash
# basic query
llm-cli "explain recursion in python"

# specify model
llm-cli --model gpt-4 "write a haiku about debugging"

# streaming output
llm-cli --stream "tell me a story"

# read from stdin
cat input.txt | llm-cli --stdin

# save to file
llm-cli "generate test data" > output.json

# set temperature
llm-cli --temperature 0.2 "what is 2+2"

# multi-line input
llm-cli --multiline
> first line
> second line
> ^D
```

## api

### command-line options

| flag | description | default |
|------|-------------|---------|
| `--model`, `-m` | model to use | `gpt-3.5-turbo` |
| `--temperature`, `-t` | sampling temperature (0.0-2.0) | `0.7` |
| `--max-tokens` | maximum response length | `2048` |
| `--stream`, `-s` | stream output token by token | `false` |
| `--stdin` | read prompt from stdin | `false` |
| `--multiline` | enable multi-line input mode | `false` |
| `--system` | system prompt | `null` |
| `--api-key` | api key (or use env var) | `$LLM_API_KEY` |

### environment variables

```bash
export LLM_API_KEY="your-api-key"
export LLM_DEFAULT_MODEL="gpt-4"
export LLM_API_BASE="https://api.openai.com/v1"
```

### configuration file

Create `~/.llm-cli/config.json`:

```json
{
  "default_model": "gpt-3.5-turbo",
  "temperature": 0.7,
  "max_tokens": 2048,
  "api_key": "your-api-key"
}
```

### supported models

- OpenAI: `gpt-4`, `gpt-3.5-turbo`
- Anthropic: `claude-3-opus`, `claude-3-sonnet`
- Local: `ollama/llama2`, `ollama/mistral`

## contributing

prs welcome. open an issue first for big changes.

## license

MIT

<!-- fixme later -->
