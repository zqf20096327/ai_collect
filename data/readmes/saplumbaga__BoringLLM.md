# BoringLLM

A tiny, stateless API that gives OpenAI, Claude, Gemini, xAI and Ollama one simple
text-in/text-out contract.

Send a text message to a model, get text back. The provider is picked from the model name.
That is the whole product.

```http
POST /v1/chat
```

## What it deliberately does not do

No streaming. No conversation history. No system prompts. No tool calling. No structured output.
No images, audio or embeddings. No temperature, max tokens or other generation options. No retries,
fallbacks or routing. No caching, rate limiting, usage tracking or dashboard. No database. No
authentication.

BoringLLM is a compatibility layer, not an AI gateway. If you need those things, put them in front
of it or use something bigger.

It also stores nothing: requests and responses are never written to disk or memory beyond the life
of the request. What each provider does with the text it receives is governed by that provider's
own data handling and retention policy.

## Supported providers

| Prefix | Provider | Credential |
| --- | --- | --- |
| `openai` | OpenAI | `OPENAI_API_KEY` |
| `anthropic` | Anthropic / Claude | `ANTHROPIC_API_KEY` |
| `gemini` | Google Gemini | `GEMINI_API_KEY` |
| `xai` | xAI | `XAI_API_KEY` |
| `ollama` | Ollama | `OLLAMA_BASE_URL` |

Only the providers you actually call need to be configured.

## Model naming

```
<provider>/<model>
```

The part before the first `/` selects the provider; everything after it is sent to that provider
unchanged, so model names containing slashes or tags still work.

```
openai/gpt-5
anthropic/claude-sonnet-4-5
gemini/gemini-2.5-pro
xai/grok-4
ollama/qwen3
ollama/hf.co/user/model:q4_k_m
```

## Quick start

Requires Node.js 24 or newer.

```bash
npm install
cp .env.sample .env    # add at least one key
npm run dev            # or: npm run build && npm start
```

## Environment variables

| Variable | Default | Notes |
| --- | --- | --- |
| `PORT` | `3000` | HTTP port |
| `OPENAI_API_KEY` | — | Required for `openai/*` |
| `ANTHROPIC_API_KEY` | — | Required for `anthropic/*` |
| `GEMINI_API_KEY` | — | Required for `gemini/*` |
| `XAI_API_KEY` | — | Required for `xai/*` |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Required for `ollama/*` |

## Docker

```bash
cp .env.sample .env
docker compose up --build
```

Compose reads your `.env`. Ollama is not bundled: set `OLLAMA_BASE_URL` to an Ollama instance you
already run. From inside the container use `http://host.docker.internal:11434` rather than
`localhost`.

## Request

```bash
curl -s localhost:3000/v1/chat \
  -H 'Content-Type: application/json' \
  -d '{"model":"anthropic/claude-sonnet-4-5","input":"Explain dependency injection in one paragraph."}'
```

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "input": "Explain dependency injection in one paragraph."
}
```

## Response

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "output": "Dependency injection is ..."
}
```

Errors use one small shape, whichever provider failed:

```json
{
  "error": {
    "code": "UNSUPPORTED_PROVIDER",
    "message": "Unsupported model provider: example"
  }
}
```

| Code | Status |
| --- | --- |
| `INVALID_REQUEST` | 400 (413 if the body exceeds 1 MB) |
| `UNSUPPORTED_PROVIDER` | 400 |
| `NOT_FOUND` | 404 |
| `PROVIDER_NOT_CONFIGURED` | 500 |
| `INTERNAL_ERROR` | 500 |
| `PROVIDER_ERROR` | 502 |

`GET /health` returns `{"status":"ok"}`.

## Security

There is no authentication, by design. Run BoringLLM as an internal service, bound to a private
network, and add authentication in front of it if you expose it publicly.

## License

MIT
