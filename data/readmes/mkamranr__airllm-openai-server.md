# AirLLM OpenAI-compatible server

> **An OpenAI-compatible API wrapper around [AirLLM](https://github.com/lyogavin/airllm) by
> [@lyogavin](https://github.com/lyogavin).** All of the inference work — the layer-streaming
> technique that makes large models run on small GPUs — is AirLLM's. This project adds only the
> HTTP layer. **Please star and support [the upstream
> project](https://github.com/lyogavin/airllm).**

[AirLLM](https://github.com/lyogavin/airllm) runs large language models on small GPUs by streaming
one layer's weights at a time instead of holding the whole model in memory: a 70B model on a 4GB
card, 405B on 8GB, without quantization or distillation. This server wraps it in the API your
existing OpenAI clients already speak, so you can point any OpenAI SDK, LangChain app, or chat UI
at it by changing one URL.

```bash
pip install -e . && pip install airllm
airllm-server --doctor                      # check this machine first
airllm-server --model Qwen/Qwen2.5-7B-Instruct
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")
print(client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
).choices[0].message.content)
```

## Documentation

| | |
| --- | --- |
| **[Getting started](docs/getting-started.md)** | Install per platform, first request, choosing a model |
| **[How to run it](docs/running.md)** | **Every run mode**: venv/conda/uv/pipx, CPU-only, NVIDIA GPU, Apple silicon, Docker, Compose, Windows, WSL2 |
| **[Usage](docs/usage.md)** | Endpoints, parameters, streaming, client examples |
| **[Deployment](docs/deployment.md)** | Docker, Compose, Kubernetes, systemd, reverse proxies |
| **[Platforms](docs/platforms.md)** | Linux, Windows (CPU and NVIDIA), macOS, Docker |
| **[Configuration](docs/configuration.md)** | Every setting and flag |
| **[Troubleshooting](docs/troubleshooting.md)** | Symptom-first fixes |

New here? [Getting started](docs/getting-started.md) is the shortest path to a working endpoint;
[How to run it](docs/running.md) is the complete matrix of ways to run it.

## Read this first: AirLLM trades speed for memory

AirLLM reads **every layer's weights from disk for every token**. That is what makes a 70B model
fit in 4GB, and it means throughput is seconds per token, not tokens per second. Measured on this
project's CPU Docker image with Qwen2.5-0.5B: ~6 s/token warm, ~3 min for the first request
including download and re-split.

The server is built around that reality:

- **Generation is single-flight.** Concurrent generations would double disk traffic and peak VRAM
  while making both slower. Requests queue for one slot; past `--max-queue-size` the server sheds
  load with `503`.
- **`max_tokens` defaults to 256**, not the context window.
- **Disk is the binding constraint**, not VRAM. Budget ~2x the model size and use the fastest disk
  you have (`--layer-shards-path`).
- **The first request to a new model is slow.** `GET /health` reports `"loaded_model": null` until
  the download and split finish — that is the answer to "is it hung?". `--preload` moves the cost
  to startup.

If your model already fits in VRAM and you want throughput, use vLLM. Use this when it does not
fit.

## Platform support

| Platform | Backend | Notes |
| --- | --- | --- |
| Linux + NVIDIA | `torch` | Best supported |
| Linux CPU | `torch` | Works; small models only |
| Windows + NVIDIA | `torch` | **Install torch from the CUDA index**, or the GPU is silently unused |
| Windows CPU | `torch` | Enable long paths + Developer Mode |
| macOS Apple silicon | `torch` (MPS) or `mlx` | `pip install mlx` is required either way |
| macOS Intel | — | AirLLM cannot run; use `--backend mock` or Docker |
| Docker CPU / CUDA | `torch` | Mount `/cache`; `--gpus all` for CUDA |

Details and the reasoning behind each caveat: [platforms.md](docs/platforms.md).

## Docker

```bash
docker build -f docker/Dockerfile -t airllm-server:cpu .
docker run -d -p 8000:8000 -v airllm-cache:/cache \
  -e AIRLLM_MODEL=Qwen/Qwen2.5-0.5B-Instruct airllm-server:cpu
```

```bash
docker build -f docker/Dockerfile.cuda -t airllm-server:cuda .
docker run -d -p 8000:8000 --gpus all -v airllm-cache:/cache \
  -e AIRLLM_MODEL=meta-llama/Llama-3.3-70B-Instruct -e HF_TOKEN=hf_... \
  -e AIRLLM_COMPRESSION=4bit airllm-server:cuda
```

Or `docker compose -f docker/docker-compose.yml up airllm-cpu|airllm-cuda|airllm-mock`. The
`/cache` volume holds both the HuggingFace cache and the layer shards — without it, every restart
re-downloads the model. See [deployment.md](docs/deployment.md).

## Endpoints

| Endpoint | Notes |
| --- | --- |
| `POST /v1/chat/completions` | Streaming (SSE) and non-streaming, `n`, `stop`, `stream_options.include_usage` |
| `POST /v1/completions` | Legacy text completion; the right fit for base models |
| `GET /v1/models`, `/v1/models/{id}` | Model discovery |
| `GET /health` | Backend, loaded model, queue depth. Never needs an API key |
| `GET /health/platform` | The `--doctor` preflight over HTTP |
| `GET /docs` | Interactive OpenAPI docs |

Errors use OpenAI's envelope, so SDK error classes (`NotFoundError`, `BadRequestError`, …) map
correctly.

## OpenAI compatibility

Supported: `model`, `messages` (including array-of-text-parts content), `max_tokens` /
`max_completion_tokens`, `temperature`, `top_p`, `n`, `stop`, `stream`,
`stream_options.include_usage`, `seed`, `user`, accurate `usage`, `system_fingerprint`,
bearer-token auth, CORS. Unknown request fields are ignored, because real clients send them.

Extensions, exposed because transformers supports them natively: `top_k`, `min_p`,
`repetition_penalty`, `chat_template_kwargs`.

Rejected with `400` rather than silently ignored: `tools`/`functions`, `response_format`
(json_object/json_schema), `logprobs`, `presence_penalty`/`frequency_penalty` (transformers has no
equivalent — use `repetition_penalty`), `logit_bias`, `best_of`, and non-text content parts. A
client that asked for JSON-only output and got prose would fail much further from the cause.
Zero-valued penalties count as unset, and `--lenient-params` downgrades these to warnings.

Full table: [usage.md](docs/usage.md#parameter-support).

## Development

```bash
pip install -e '.[test]'
pytest -q                  # 81 tests
```

The `mock` backend needs no weights, torch or GPU, so the whole HTTP surface is testable anywhere —
including machines AirLLM cannot run on. `tests/test_torch_backend.py` additionally exercises the
real transformers generation plumbing (`TextIteratorStreamer`, per-token counting, `finish_reason`,
the abort path) against a tiny model, standing a faithful shim in for `AirLLMBaseModel`; it skips
when torch is absent.

```
airllm_server/
  config.py            AIRLLM_* settings
  platform_support.py  device/dtype detection and the --doctor preflight
  engine.py            model lifecycle, single-flight slot, stop handling, sync->async bridge
  stopping.py          streaming-safe stop-sequence filter
  schemas.py           OpenAI request/response models
  chat.py              message normalisation, base-model prompt fallback
  errors.py            OpenAI error envelope
  backends/
    base.py            the interface a backend implements (encode, decode, render, stream)
    torch_backend.py   CUDA / CPU / MPS via AirLLM + transformers
    mlx_backend.py     Apple silicon via AirLLM's MLX path
    mock_backend.py    no weights, for tests and client bring-up
  api/                 chat, completions, models, health, auth
docker/                CPU and CUDA images, Compose
docs/                  the documentation linked above
```

Adding a backend means implementing `encode`, `decode`, `render_chat_prompt` and `stream` in
`backends/base.py`. Stop sequences, usage accounting, admission control and the OpenAI response
shapes all live above that boundary.

## Credits

**This project is a wrapper. [AirLLM](https://github.com/lyogavin/airllm) does the hard part.**

Every bit of the inference technique this server depends on — splitting a checkpoint into per-layer
shards, holding the model on the `meta` device, streaming one layer's weights onto the accelerator
just before it runs and freeing it immediately after, prefetching the next layer, per-expert
streaming for sparse MoE models — is the work of AirLLM and its authors. This repository contributes
only an OpenAI-compatible HTTP layer on top: request validation, chat templating, streaming, stop
sequences, usage accounting, admission control, and packaging.

AirLLM does not vendor into this repository; it is installed from PyPI as a normal dependency, and
its code remains entirely upstream.

- **AirLLM** — https://github.com/lyogavin/airllm — by [Gavin Li](https://github.com/lyogavin) and
  contributors, Apache-2.0. Please star it.
- Built on [PyTorch](https://pytorch.org), [Transformers](https://github.com/huggingface/transformers),
  [Accelerate](https://github.com/huggingface/accelerate), [FastAPI](https://fastapi.tiangolo.com)
  and [Uvicorn](https://www.uvicorn.org).

See [NOTICE](NOTICE) for the full attribution and dependency licenses.

## License

Apache-2.0 — see [LICENSE](LICENSE). This matches AirLLM's license.

Model weights downloaded at run time carry their own licenses, which are the operator's
responsibility. Gated repositories such as `meta-llama/*` require accepting their terms on Hugging
Face first.

---

If this saved you some time, you can
[buy me a coffee](https://buymeacoffee.com/kamikhan05t) ☕ — and please send some of that goodwill
[upstream to AirLLM](https://github.com/lyogavin/airllm) too.
