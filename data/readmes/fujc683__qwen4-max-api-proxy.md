# Qwen4 Max 中转 API — one key, Alipay, no overseas card

> What an API relay changes for Qwen4 Max: payment, network, keys and billing.

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**[👉 Use Qwen4 Max on APIMart](https://gola.apimart.ai/k-lLOd9O)**

`https://gola.apimart.ai/k-lLOd9O`

[💰 Pricing](https://gola.apimart.ai/k-EatwtP) · [🔑 Get an API key](https://gola.apimart.ai/k-xXzyXa)

---

## What a relay changes

| | Direct to vendor | Relay (APIMart) |
|---|---|---|
| Payment | foreign card, overseas account | **Alipay / WeChat / card** |
| Network | direct, sometimes throttled | **domestic-optimised relay** |
| Keys | one per vendor | **one key, all models** |
| Invoice | overseas | **domestic invoice** |
| Billing | per vendor | **one balance, per-token** |

## Endpoint

```bash
curl -X POST https://api.apimart.ai/v1/chat/completions \
  -H "Authorization: Bearer $APIMART_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen4-max","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

OpenAI-compatible: change `base_url` and `model`, keep the rest.

## Models behind the same key

| Category | Examples |
|---|---|
| LLM | Qwen4 Max, Qwen3.8 Max, DeepSeek V3.2 |
| Image | GPT Image 2.6, Nano Banana 2 / Pro, Seedream 5.0 |
| Video | Seedance 2.5 Flash, Kling 4.0, Wan 3.0, Veo 3 |

## Production notes

- Video and image calls are async (`task_id` + polling); chat is synchronous
- Streaming is on by default for chat — set `stream: false` for JSON
- Failed tasks are refunded automatically
- Keep a client-side retry with jitter; treat every call as idempotent

---

## Related

- All prompt collections: [fujc683 repositories](https://github.com/fujc683?tab=repositories)

## License

CC BY 4.0
