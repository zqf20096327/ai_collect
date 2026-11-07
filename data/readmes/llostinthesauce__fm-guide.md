# fm-guide

A practical guide to **`fm`**, the Foundation Models command-line tool that ships with macOS 27. `fm` runs Apple's on-device language model from the terminal, and with `fm serve` it becomes a local OpenAI-compatible endpoint: offline, no API key, no per-token cost.

Apple's built-in help covers the flags. This guide covers what you only find out by using the tool: the limits, the gotchas, and the parts that are broken.

**Tested on:** macOS 27.0 (`26A5425a`), `FoundationModels` 2.0.68, Apple silicon, 2026-09-06. Behavior changes between betas, so check against your build.

## Before you start

`fm` refuses every command, `--help` included, until an admin accepts Apple's terms:

```sh
sudo fm license
fm license --status
```

## The short version

| | |
|---|---|
| **Context** | 8,192 tokens, of which **8,132** can be prompt. About **54** go to a hidden system prompt on every call, which leaves roughly 6,000 words of your own text. |
| **Speed** | About 42–46 tokens/s generation, and about 1,000–1,900 tokens/s prefill. A near-full prompt takes about 7 s to the first token. |
| **Structured output** | `fm respond --schema` constrains the output exactly, but every object needs an `x-order` key or the schema is rejected with an unhelpful error. `fm serve`'s `response_format: json_schema` accepts plain JSON Schema. |
| **`fm serve`** | Chat Completions with streaming, vision, and JSON-schema output. `temperature: 0` is deterministic. `max_tokens` is accepted and **ignored**. `stop`, `n`, and `reasoning_effort` return 400. |
| **Tool calling** | **Broken on 2.0.68.** Tool arguments come back as plain `content` with no `tool_calls`. Turn tool calling off in any agent framework. |
| **Security** | `fm serve` has no authentication. Keep it on `127.0.0.1` or a Unix socket. |

## Guides

| Guide | What's in it |
|---|---|
| [CLI reference](docs/cli-reference.md) | Every command and flag, chat slash commands, exit codes, and a bug in Apple's own help text |
| [Serve API](docs/serve-api.md) | Endpoints, which parameters actually do something, structured output, vision, the tool-calling regression, CORS, errors, and wiring up clients (OpenAI SDK, opencode) |
| [Guided generation](docs/guided-generation.md) | The `x-order` rule, what JSON Schema features are supported, arrays of objects, and extraction recipes |
| [Limits & performance](docs/limits-and-performance.md) | Measured context ceiling, latency and throughput, determinism, guardrail levels |

## Quick start: `fm` as a local OpenAI endpoint

```sh
fm serve                       # http://127.0.0.1:1976
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1976/v1", api_key="unused")
print(client.chat.completions.create(
    model="system",
    messages=[{"role": "user", "content": "Name two colors."}],
    temperature=0.0,
).choices[0].message.content)
```

## How this was made

Everything here comes from running the shipped `fm` tool and its HTTP server, and from measuring what they return. Nothing is decompiled, extracted, or redistributed from Apple software. Read the [disclaimer](DISCLAIMER.md).

## License

The writing is MIT licensed. See [LICENSE](LICENSE). `fm`, Foundation Models, and Apple Intelligence belong to Apple.
