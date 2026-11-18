# Qwen4 Max API — endpoint, streaming, reasoning tokens

> How to call Qwen4 Max on APIMart: chat completions, streaming defaults and reasoning output.

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**[👉 Use Qwen4 Max on APIMart](https://gola.apimart.ai/k-SBK4VP)**

`https://gola.apimart.ai/k-SBK4VP`

[💰 Pricing](https://gola.apimart.ai/k-ByHVuT) · [🔑 Get an API key](https://gola.apimart.ai/k-4oLVrz)

---

## Endpoint

OpenAI-compatible chat completions:

```bash
curl -X POST https://api.apimart.ai/v1/chat/completions \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen4-max","messages":[{"role":"user","content":"explain vector databases"}]}'
```

## Streaming

The endpoint streams by default. Parse `data:` lines, or pass `"stream": false`
for a single JSON body.

```python
from openai import OpenAI
client = OpenAI(base_url="https://api.apimart.ai/v1", api_key=KEY)

for chunk in client.chat.completions.create(
        model="qwen4-max",
        messages=[{"role": "user", "content": "write a haiku"}],
        stream=True):
    print(chunk.choices[0].delta.content or "", end="")
```

## Reasoning output

Qwen4 Max can emit a separate `reasoning_content` field alongside `content`.
Treat it as chain-of-thought: useful for debugging, not for showing to end users.

```json
{"delta": {"role": "assistant", "content": "", "reasoning_content": "..."}}
```

`usage.completion_tokens_details.reasoning_tokens` tells you how many tokens were
spent thinking — that part is billed as output.

## Parameters that matter

| Field | Notes |
|---|---|
| `messages` | standard role/content array |
| `stream` | true by default on this endpoint |
| `max_tokens` | cap output; reasoning tokens count toward it |
| `temperature` | 0-2; lower for extraction, higher for ideation |
| `tools` | function calling, OpenAI schema |

## Pricing

| | Per 1M tokens |
|---|---:|
| Input | **$1.4286** |
| Output | **$4.2857** |

## Gotchas

- Streaming is on unless you pass `stream: false`
- Reasoning tokens are billed as output — budget for 2-3x on hard tasks
- Very long prompts benefit from prompt caching; cached tokens are cheaper

---

## Related

- All prompt collections: [fujc683 repositories](https://github.com/fujc683?tab=repositories)

## License

CC BY 4.0
