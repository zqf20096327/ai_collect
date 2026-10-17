# kev-onnx

[![Build and push multi-arch image](https://github.com/aleskxyz/kev-onnx/actions/workflows/build.yml/badge.svg)](https://github.com/aleskxyz/kev-onnx/actions/workflows/build.yml)

Self-hosted, TypeSafe-compatible API server for **KEV**, a *decision model*: instead of generating
text, you hand it a `state` (a document, a support ticket, any piece of context) plus one or more
typed `questions`, and it hands back a calibrated probability for every possible answer — in one
forward pass, no parsing required.

- **Drop-in compatible.** Speaks the same [`/v1/systemone`](https://docs.typesafe.ai/api)
  wire format as TypeSafe's own hosted API, so any client, SDK, or benchmark built for it works
  against this self-hosted server unchanged.
- **CPU-only, no GPU needed.** Runs a quantized ONNX build of KEV via `onnxruntime`.
- **One container.** Pull the published image, point `docker compose` at it, done.

## Contents

- [System requirements](#system-requirements)
- [Quick start](#quick-start)
- [Using the API](#using-the-api)
- [Configuration](#configuration)
- [About the KEV model](#about-the-kev-model)
- [Running at scale](#running-at-scale)
- [Building from source](#building-from-source)
- [License](#license)

## System requirements

- **Docker Engine + Docker Compose v2** (or Python 3.10+ and `pip` if [running without Docker](#building-from-source))
- **CPU only — no GPU required.** ~4 cores recommended (matches the default `ONNX_NUM_THREADS=4`;
  it runs with fewer, just with less intra-op parallelism)
- **~4 GB RAM.** A single loaded `model_q4.onnx` instance measures ~2.8 GB resident; leave headroom
  for the OS and Docker itself
- **~3 GB free disk on first run** — ~700 MB for the image plus ~2.5 GB to download the default
  `model_q4.onnx` variant into the `model-cache` volume (more if you cache multiple `KEV_MODEL_FILE`
  variants in the same volume)
- **Outbound internet access to huggingface.co** on first startup, to download the model and
  tokenizer — not needed afterward, since both are cached in the `model-cache` volume

## Quick start

Only the compose file and env template are needed — the image itself is pulled from GHCR:

```bash
mkdir kev-onnx && cd kev-onnx
curl -fsSL https://raw.githubusercontent.com/aleskxyz/kev-onnx/main/docker-compose.yml -o docker-compose.yml
curl -fsSL https://raw.githubusercontent.com/aleskxyz/kev-onnx/main/.env.example -o .env
# adjust KEV_MODEL_FILE etc. in .env if needed

docker compose pull
docker compose up -d

# Wait for the model to download and load (~30-60s on first run)
docker compose logs -f
```

Check it's up:

```bash
curl http://localhost:8008/health
# {"status": "ok", "model": "loaded", "threads": 4}
```

That's it — the server is ready at `http://localhost:8008`.

## Using the API

Every request is a `POST` to `/v1/systemone` with a `state` and one or more named `questions`.
There are three question types, depending on what kind of answer you want back.

### `choice` — pick one option out of a set

```bash
curl -X POST http://localhost:8008/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kev-onnx",
    "state": "I was billed twice for the same order",
    "questions": {
      "routing": {
        "type": "choice",
        "instructions": "Which team should handle this?",
        "criteria": { "billing": "Payments", "tech": "Support", "sales": "Sales" }
      }
    }
  }'
```

```json
{
  "model": "kev-onnx",
  "id": "uuid",
  "answers": {
    "routing": {
      "type": "choice",
      "choice": "billing",
      "confidence": 0.705,
      "probabilities": { "billing": 0.705, "tech": 0.194, "sales": 0.100 }
    }
  },
  "usage": { "input_tokens": 50, "output_tokens": 1 }
}
```

### `noul` — a calibrated yes/no

```bash
curl -X POST http://localhost:8008/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kev-onnx",
    "state": "I was billed twice for the same order",
    "questions": {
      "urgent": { "type": "noul", "instructions": "Does this need urgent attention?" }
    }
  }'
```

```json
{ "model": "kev-onnx", "id": "uuid", "answers": { "urgent": { "type": "noul", "noul": 0.93 } }, "usage": { "input_tokens": 44, "output_tokens": 1 } }
```

`noul` returns `P(yes)` directly (`0.93` above). Pass a custom `criteria: {"true": "...", "false": "..."}` to reword the yes/no framing.

### `score` — rate against ordered levels

```bash
curl -X POST http://localhost:8008/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kev-onnx",
    "state": "I was billed twice for the same order",
    "questions": {
      "severity": {
        "type": "score",
        "instructions": "How severe is this?",
        "criteria": ["None", "Minor", "Moderate", "Critical"]
      }
    }
  }'
```

```json
{
  "model": "kev-onnx",
  "id": "uuid",
  "answers": {
    "severity": {
      "type": "score",
      "score": 1.8,
      "confidence": 0.41,
      "legend": { "0": "None", "1": "Minor", "2": "Moderate", "3": "Critical" },
      "probabilities": { "0": 0.05, "1": 0.29, "2": 0.41, "3": 0.25 }
    }
  },
  "usage": { "input_tokens": 47, "output_tokens": 1 }
}
```

`score` returns both the probability-weighted expected level (`score`) and the full distribution
— use whichever your application needs. `criteria` takes 2-10 ordered levels.

### `GET /v1/models`

TypeSafe-compatible model listing. This server serves exactly one model, `kev-onnx`, so the
response always has one entry; send that name in a request's `model` field.

```json
{
  "models": [
    {
      "name": "kev-onnx",
      "description": "Self-hosted KEV decision model (onnx-community/kev-4b-ONNX), served via ONNX Runtime on CPU.",
      "release_date": "2026-09-20"
    }
  ]
}
```

`release_date` is fetched from `KEV_MODEL`'s Hugging Face repo metadata at startup, so it tracks
whatever model repo you actually configure.

### `GET /health`

```json
{ "status": "ok", "model": "loaded", "threads": 4 }
```

Returns `503` while the model is still loading or if it failed to load. This is a Docker
healthcheck convenience, not part of the TypeSafe spec.

## Configuration

All configuration is via environment variables, normally set in `.env` (copy `.env.example` to
get started — `docker-compose.yml` loads it via `env_file`).

| Env Var | Default | Description |
|---|---|---|
| `KEV_MODEL` | `onnx-community/kev-4b-ONNX` | Hugging Face model repo. Special token IDs and token/option limits are auto-discovered from the repo's `config.json` `"kev"` block, falling back to the original KEV-4B defaults for repos that don't publish one. |
| `KEV_MODEL_DIR` | `/app/models` | Local directory to download/cache the model into (mounted as the `model-cache` volume). |
| `KEV_MODEL_FILE` | `model_q4.onnx` | Exact `onnx/*.onnx` filename to load. Validated against the repo's file listing at startup — there is no auto-selection, only this default. The default is the plain `q4` variant, not `q4f16`: this server only runs `CPUExecutionProvider`, and `q4f16` targets WebGPU's fp16 shader path, which onnxruntime's CPU backend doesn't fully support. |
| `ONNX_NUM_THREADS` | `4` | CPU threads for ONNX Runtime's intra-op thread pool. |
| `PORT` | `8008` | Host port `docker-compose.yml` publishes the server on (container always listens on `8008` internally). |
| `KEV_MAX_TOTAL_TOKENS` | `8192` | Max total input tokens per request, across all questions — matches the model's native context window. |
| `KEV_MIN_SCORE_LEVELS` | `2` | Minimum criteria levels for a `score` question. |
| `KEV_MAX_SCORE_LEVELS` | `10` | Maximum criteria levels for a `score` question. |

## About the KEV model

The default model is [`onnx-community/kev-4b-ONNX`](https://huggingface.co/onnx-community/kev-4b-ONNX)
on Hugging Face (Apache-2.0), downloaded and cached at startup. This repository contains only the
serving code — no model weights are vendored or redistributed here.

**How it compares.** From the [`jaredpalmer/kev-4b` model card](https://huggingface.co/jaredpalmer/kev-4b),
on the same frozen decision-suite items for every row (Kev-4B is the checkpoint this server uses by default):

| | Kev-0.5B | Kev-0.6B | **Kev-4B** | Jev (TypeSafe) |
|---|---|---|---|---|
| In-distribution accuracy | 0.712 | 0.801 | **0.854** | 0.845 |
| Out-of-domain accuracy | 0.561 | 0.620 | **0.790** | 0.857 |
| Out-of-domain Brier (lower is better) | 0.50 | 0.536 | **0.328** | 0.211 |
| Confident errors out of domain | – | 10.8% | 8.2% | 3.7% |

Kev-4B is the largest open checkpoint in the family and the closest of the three to Jev on
in-distribution accuracy, but it trails Jev out-of-domain on calibration (Brier) and confident-error
rate — see the model card for the full results table, per-source breakdown, and known limits.

## Running at scale

The server handles concurrent requests safely (async FastAPI + a shared, thread-safe ONNX
`InferenceSession`), but it's a single process with a fixed-size compute pool
(`ONNX_NUM_THREADS`) — concurrent requests are queued and interleaved over that pool rather than
scaled linearly. For more throughput, run multiple replicas behind a load balancer rather than
relying on one instance's concurrency.

**Measured latency** — single request at a time (no concurrency), `POST /v1/systemone` over HTTP,
`model_q4.onnx`, `ONNX_NUM_THREADS=4`, on a 14-core Intel Core Ultra 7 265U:

| Question type | Options/levels | Input tokens | Mean | p50 | p95 |
|---|---|---|---|---|---|
| `noul` | 2 | 38 | 1000ms | 998ms | 1028ms |
| `score` | 4 | 49 | 1287ms | 1287ms | 1323ms |
| `choice` | 4 | 64 | 1622ms | 1635ms | 1687ms |

Latency scales with input length (`usage.input_tokens` in the response) — `noul`'s fixed 2-option
yes/no branch is shortest and fastest, `choice` with longer option descriptions has the most
tokens and is slowest. This is CPU-only, single-instance, single-request latency; expect it to
vary with your hardware and to degrade under concurrent load per the note above.

## Building from source

Published images live at [`ghcr.io/aleskxyz/kev-onnx`](https://github.com/aleskxyz/kev-onnx/pkgs/container/kev-onnx),
built and pushed by [`.github/workflows/build.yml`](.github/workflows/build.yml) — a multi-arch
(`linux/amd64`, `linux/arm64`) image on every published GitHub release (tagged `X.Y.Z`, `X.Y`, `X`,
and `latest`) and on manual dispatch (tagged `<ref>-<sha>`).

`docker-compose.yml` references `image: ghcr.io/aleskxyz/kev-onnx:latest` directly, so
`docker compose pull && docker compose up -d` never needs a local build. If you're changing the
server itself, build the image directly from the local `Dockerfile`:

```bash
docker build -t kev-onnx .
docker run --rm -p 8008:8008 --env-file .env kev-onnx
```

To run without Docker at all, using the checked-in virtualenv conventions:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export KEV_MODEL_FILE=model_q4.onnx
export KEV_MODEL_DIR=./models
uvicorn src.server:app --reload --port 8008
```

### Running the tests

The test suite mocks the tokenizer/ONNX session boundary, so it runs in under a second with no
model download or network access needed:

```bash
pip install -r requirements.txt
pytest
```

Project layout:

```
kev-onnx/
├── src/                          # Server application
│   ├── server.py                # FastAPI endpoints
│   ├── models.py                # Pydantic schemas
│   ├── inference.py             # Model loading & inference
│   └── validation.py            # Request validation
├── tests/                         # Unit tests
├── .github/workflows/             # CI: build & publish to GHCR
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## License

Apache License 2.0 — see [LICENSE](LICENSE). This covers the serving code in this repository only;
the [KEV model weights](https://huggingface.co/onnx-community/kev-4b-ONNX) are separately licensed
(also Apache-2.0) by their authors on Hugging Face.
