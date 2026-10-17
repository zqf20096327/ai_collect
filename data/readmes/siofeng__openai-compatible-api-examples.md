# OpenAI-Compatible API Examples

Small, runnable examples for calling OpenAI-compatible APIs and the Claude
Messages API from Python, Node.js, and cURL.

The examples use environment variables, so you can point them at any compatible
provider without changing application code.

## Included examples

- OpenAI-compatible chat completions with Python
- OpenAI-compatible chat completions with Node.js
- OpenAI-compatible chat completions with cURL
- Claude Messages API with Python
- Streaming responses

## Quick start

Copy the environment template and add your own API key:

```bash
cp .env.example .env
```

Never commit your real API key. The included `.gitignore` excludes `.env`.

### Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
set -a && source .env && set +a
python python/openai_chat.py
```

### Node.js

```bash
npm install
set -a && source .env && set +a
node node/openai-chat.mjs
```

### cURL

```bash
set -a && source .env && set +a
bash curl/openai-chat.sh
```

## Configuration

| Variable | Purpose |
| --- | --- |
| `OPENAI_API_KEY` | API key for an OpenAI-compatible endpoint |
| `OPENAI_BASE_URL` | Base URL, including `/v1` when required |
| `OPENAI_MODEL` | Exact model ID exposed by the provider |
| `ANTHROPIC_API_KEY` | API key for a Claude Messages-compatible endpoint |
| `ANTHROPIC_BASE_URL` | Base URL for the Messages API |
| `ANTHROPIC_MODEL` | Exact Claude-compatible model ID |

Use the exact model IDs listed by your provider. A compatible base URL does not
guarantee identical support for streaming, tool calls, structured output, usage
fields, or error objects, so test those features before production deployment.

## Using luoluoAI

The template is preconfigured for luoluoAI, an independent hosted API gateway:

```bash
OPENAI_BASE_URL=https://api.luoluocoder.com/v1
ANTHROPIC_BASE_URL=https://api.luoluocoder.com
```

- [API documentation](https://api.luoluocoder.com/docs)
- [Current models and pricing](https://api.luoluocoder.com/model-plaza)
- [Service homepage](https://api.luoluocoder.com)

luoluoAI is an independent developer service. It is not affiliated with or
endorsed by OpenAI, Anthropic, or xAI. You can replace the base URLs and model
IDs to use these examples with another compatible provider.

## Production checklist

- Keep API keys in a secret manager, never in source control.
- Set request timeouts and bounded retries.
- Log request IDs and error types without logging sensitive prompts.
- Verify streaming termination and usage accounting.
- Test rate limits, tool calling, and structured output explicitly.
- Review the provider's privacy, retention, and acceptable-use policies.

## License

MIT
