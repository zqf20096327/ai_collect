# Cyber-Inference

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-00ff9f?style=for-the-badge&logo=python&logoColor=00ff9f" alt="Python">
  <img src="https://img.shields.io/badge/License-GPLv3-00ff9f?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/llama.cpp-Powered-00ff9f?style=for-the-badge" alt="llama.cpp">
  <img src="https://img.shields.io/badge/Transformers-Powered-00ff9f?style=for-the-badge" alt="Transformers">
  <img src="https://img.shields.io/badge/whisper.cpp-Powered-00ff9f?style=for-the-badge" alt="whisper.cpp">
  <img src="https://img.shields.io/badge/NVIDIA-Containers-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="NVIDIA containers">
</p>

<p align="center">
  <img src="cyber-inference.png" alt="Cyber-Inference UI">
  <strong>Edge inference server management with an OpenAI-compatible API</strong>
</p>

Cyber-Inference is a web GUI and API server for running local inference engines behind OpenAI-compatible `/v1` endpoints. It supports:
- `llama.cpp` for GGUF models
- `transformers` for full HuggingFace model directories
- `whisper.cpp` for transcription/translation

## Features

- OpenAI-compatible API (`/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/audio/*`)
- GGUF reranker support via `/v1/rerank`, with automatic model detection, rank-pooling serving, and scored document indices
- Native model context windows by default, with native, configured, and effective lengths in `/v1/models`
- Model download + registration from HuggingFace, including split GGUF shard sets
- Automatic MTP speculative decoding for detected GGUF models, with managed llama.cpp upgrade when needed
- Automatic lazy loading and idle unloading
- Web dashboard for model and resource management
- Optional admin auth (JWT)
- NVIDIA-only published container images for Linux AMD64 and Thor ARM64
- Native local startup paths for macOS Apple Silicon and non-container development

## Releases

- GitHub Releases are the canonical release surface for Cyber-Inference.
- `CHANGELOG.md` is the repo release log.
- Release notes are generated from commits since the previous release plus the core-functions summary in this README.
- Versioning is patch-by-default. Use `release:minor` or `feat:` to force a minor bump, and `release:major`, `BREAKING CHANGE`, or `type!:` to force a major bump.
- Container images publish from the GitHub release event and receive immutable versioned tags such as `v0.2.0-linux-amd64` and `v0.2.0-thor-arm64`, floating platform tags, and a multi-arch `latest` tag. Publishing never replaces a running Thor container; deployment is an explicit operator action using the commands below.

### v0.2.23 — GGUF reranker support

Adds GGUF reranker detection, download controls, and lazy-loaded `/v1/rerank` serving.
Publishing remains a separate release-workflow step.
Existing BGE rerankers incorrectly classified as embeddings are repaired on discovery; restart
Cyber-Inference (or unload and reload the model) to replace old embedding-only processes.
The llama.cpp updater skips metadata-only releases when selecting compatible binaries.
System-managed binaries and Thor-bundled CUDA runtimes remain operator-managed.
CLI model commands now honor configured storage directories and initialize/close their database
connections, including the documented reranker download workflow.

## Inference Engines

| Engine | Model Format | Typical Hardware | Primary Use |
| --- | --- | --- | --- |
| `llama.cpp` | GGUF | CPU / Apple Metal / CUDA | Quantized local chat, embeddings, and reranking |
| `transformers` | HuggingFace directory (`config.json`, safetensors, tokenizer) | CPU / CUDA / MPS | Full HF model inference |
| `whisper.cpp` | Whisper GGUF/bin | CPU / Apple Metal / CUDA | Speech transcription and translation |

## Quick Start

Choose the copy/paste block for your host:

- **Thor / DGX Spark (ARM64 NVIDIA):** [one-shot startup](#one-shot-startup) below.
- **Linux PC/server (AMD64 NVIDIA):** [Docker startup](#linux-amd64-nvidia).
- **macOS Apple Silicon or other native hosts:** [native latest release](#native-latest-release).

For Docker, install Docker Engine and NVIDIA Container Toolkit first. The `thor-arm64` and
`linux-amd64` tags track the latest published image for each platform; each block pulls it before
starting. Run commands from the directory where you want to keep `data/` and `models/`.
The UI/API is available at `http://<your-machine>:8337`. Keep it on a trusted network; admin
authentication is optional and disabled by default.

### One-shot startup

You have a NVIDIA Thor/DGX Spark ARM64 host and want to run Cyber-Inference.

> [!TIP] The latest llama.cpp is built natively on Thor and baked into the container image.

```bash
(
set -eu
mkdir -p data models

docker pull ghcr.io/ramborogers/cyber-inference:thor-arm64

docker run -d --name cyber-inference \
  --runtime nvidia \
  -p 8337:8337 \
  -v "$PWD/data:/app/data" \
  -v "$PWD/models:/app/models" \
  ghcr.io/ramborogers/cyber-inference:thor-arm64

curl --fail --retry 90 --retry-delay 2 --retry-connrefused \
  http://localhost:8337/health
)
```

Quick ⚡️ update for an existing container, preserving models and application state.
Run from the **same directory** as the original startup, and keep any custom environment, ports,
mounts, or restart policy you originally used. The block stops immediately if pulling fails.

```bash
(
set -eu
docker pull ghcr.io/ramborogers/cyber-inference:thor-arm64
docker rm -f cyber-inference

docker run -d --name cyber-inference \
  --runtime nvidia \
  -p 8337:8337 \
  -v "$PWD/data:/app/data" \
  -v "$PWD/models:/app/models" \
  ghcr.io/ramborogers/cyber-inference:thor-arm64

curl --fail --retry 90 --retry-delay 2 --retry-connrefused \
  http://localhost:8337/health
)
```

### Native latest release

Use this instead of Docker on macOS to retain Metal/MPS acceleration, or for a native Linux
installation. Requires Git, cURL, and Python 3.12+. Run in a parent directory that does not already
contain a `cyber-inference` checkout. This selects the latest **published release**, not unreleased
changes on `master`; `start.sh` installs dependencies and starts the service in the foreground.

```bash
(
set -eu
release="$(curl -fsSL https://api.github.com/repos/RamboRogers/cyber-inference/releases/latest \
  | python3 -c 'import json, sys; print(json.load(sys.stdin)["tag_name"])')"
git clone --depth 1 --branch "$release" https://github.com/RamboRogers/cyber-inference.git
cd cyber-inference
./start.sh
)
```

### Local development
```bash
git clone https://github.com/ramborogers/cyber-inference.git
cd cyber-inference
./start.sh
```

`start.sh` will:
1. Ensure `uv` is available.
2. Validate Python 3.12+.
3. Detect NVIDIA GPU/CUDA.
4. Run `uv sync`.
5. Verify CUDA-enabled PyTorch on NVIDIA machines.
6. Start `cyber-inference serve` with auto-restart.

### Manual setup

```bash
uv sync
uv run cyber-inference init
uv run cyber-inference serve --reload
```

Open the UI at `http://localhost:8337`.

## Model Download

![download.png](download.png)

Use the **Models** page in the UI or the CLI.

Cyber-Inference handles GGUF repositories that publish one model across multiple shard files such as
`Model-00001-of-00003.gguf`, `Model-00002-of-00003.gguf`, and `Model-00003-of-00003.gguf`.
The downloader presents the shard set as one logical model choice, downloads any missing shards,
skips complete shards on repeat runs, and registers one canonical model entry.

MTP-capable speculative GGUF repositories are detected automatically. Repos such as
`unsloth/Qwen3.6-27B-MTP-GGUF` and `unsloth/Qwen3.6-35B-A3B-MTP-GGUF` default to MTP text mode,
prefer the balanced `UD-Q4_K_XL` quantization when present, and launch llama.cpp with
`--parallel 1`, `--flash-attn on`, `--spec-type draft-mtp`, and `--spec-draft-n-max 2`.
Qwen3.6 MTP models also receive `--chat-template-kwargs '{"preserve_thinking":true}'`.
If a repo also publishes `mmproj` files, MTP takes priority and the projector is not downloaded
or launched unless explicitly selected; disable MTP in the model settings to use vision/projector mode.

GGUF rerankers are a separate model task from text embeddings. In **Models → Download Model**,
choose the **BGE Reranker v2 M3** tile or enter `gpustack/bge-reranker-v2-m3-GGUF`, fetch files,
and choose `bge-reranker-v2-m3-Q4_K_M.gguf`. The file picker identifies rerankers automatically;
for an unusual filename, choose **Model Task → Reranker (GGUF only)** explicitly.
Rerankers do not download vision projectors or MTP heads and use the same Load/Unload lifecycle
as other models. Their model-discovery capability is `capabilities.reranking: true`, not
`capabilities.embedding: true`.

## API Usage

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8337/v1", api_key="not-needed")

resp = client.chat.completions.create(
    model="Qwen3-4B-Q4_K_M",
    messages=[{"role": "user", "content": "hello"}],
)
print(resp.choices[0].message.content)
```

### cURL

```bash
curl http://localhost:8337/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-4B-Q4_K_M",
    "messages": [{"role": "user", "content": "hello"}]
  }'
```

### Reranking (GGUF / llama.cpp)

`POST /v1/rerank` is a Jina-style string-document API, not an OpenAI-standard endpoint.
`/v1/reranking` is an alias. Use HTTP directly rather than an invented OpenAI SDK rerank method.
Transformers reranking is not supported in this release; only GGUF rerankers served by llama.cpp
are supported.

```bash
uv run cyber-inference download-model gpustack/bge-reranker-v2-m3-GGUF \
  --engine gguf --filename bge-reranker-v2-m3-Q4_K_M.gguf

curl --fail-with-body http://localhost:8337/v1/rerank \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "bge-reranker-v2-m3-Q4_K_M",
    "query": "What is the capital of France?",
    "documents": [
      "Berlin is the capital of Germany.",
      "Paris is the capital of France."
    ],
    "top_n": 1,
    "return_documents": true
  }'
```

Use the exact registered model ID shown by `GET /v1/models`. A first request lazy-loads the
model with `--embedding --reranking --pooling rank`. The active binary must advertise those
flags and support the selected GGUF architecture. If capability checking fails, update through
Settings for a managed binary, use your package manager for a system binary, or pull/rebuild
the Thor image for its bundled CUDA runtime; public requests do not replace binaries.

The response has `object: "list"`, `model`, and `results`, ordered by descending relevance.
Each result contains the original zero-based `index` and a finite `relevance_score`; scores
are model-specific and are not guaranteed probabilities in the range 0–1. With
`return_documents: true`, each result also contains `document: {"text": "..."}` from the
original input. Actual backend token counts appear in `usage` when available; they are not estimated.

`model`, `query`, and each document must be nonblank strings. `documents` must be a nonempty
string array. `top_n` defaults to all documents, must be an integer >=1, and is capped at the
document count. `return_documents` defaults to false. Object documents, `texts`, streaming,
and other unlisted fields are rejected with 422. Duplicate document strings retain separate indices.

Errors: 404 for unavailable models; 400 for the wrong model task/engine; 503 for load failure;
504 for backend timeout; 502 for unavailable/malformed backend responses. Backend input-limit
errors retain 400/413/422. The model context window applies to query/document pairs including
model-specific special tokens; the proxy does not silently chunk or truncate long documents.

## Docker

Cyber-Inference publishes NVIDIA-only container images for the two supported deployment targets:

| Target | Image |
| --- | --- |
| Multi-arch default | `ghcr.io/ramborogers/cyber-inference:latest` |
| Linux AMD64 NVIDIA hosts | `ghcr.io/ramborogers/cyber-inference:linux-amd64` |
| Thor / DGX Spark ARM64 NVIDIA hosts | `ghcr.io/ramborogers/cyber-inference:thor-arm64` |

To pin this release rather than follow floating tags, replace the image in **both** the pull and
run commands with `ghcr.io/ramborogers/cyber-inference:v0.2.23-thor-arm64` or
`ghcr.io/ramborogers/cyber-inference:v0.2.23-linux-amd64`. Prefer pinned tags for reproducible
production deployments. Release notes: [latest GitHub release](https://github.com/RamboRogers/cyber-inference/releases/latest).

Both images expect durable host directories mounted into the container:

- `./data` → `/app/data` for the database and logs
- `./models` → `/app/models` for downloaded model files

The Linux AMD64 image does not ship bundled native inference servers; on demand, Cyber-Inference
installs compatible `llama-server` and `whisper-server` binaries into `/app/bin`, so the container
needs outbound network access on first boot and first transcription use. The Thor image bakes in the
current native CUDA `llama.cpp` build produced on `thor.lab` during the publish workflow and an
isolated native CUDA `whisper.cpp` runtime exposed through `/app/bin/whisper-server`, then
smoke-tests those binaries with the NVIDIA runtime enabled after the image is built. `transformers`
remains Python-managed in both images and relies on CUDA-capable PyTorch rather than a staged server
binary.

Docker is **not** the recommended path for macOS Apple Silicon MPS. On macOS, use the native local
startup flow above so Metal/MPS support is available directly from the host.

### Linux AMD64 NVIDIA

```bash
(
set -eu
mkdir -p data models

docker pull ghcr.io/ramborogers/cyber-inference:linux-amd64

docker run -d --name cyber-inference \
  --gpus all \
  -p 8337:8337 \
  -v "$PWD/data:/app/data" \
  -v "$PWD/models:/app/models" \
  ghcr.io/ramborogers/cyber-inference:linux-amd64

curl --fail --retry 90 --retry-delay 2 --retry-connrefused \
  http://localhost:8337/health
)
```

### Thor / DGX Spark ARM64 NVIDIA

```bash
(
set -eu
mkdir -p data models

docker pull ghcr.io/ramborogers/cyber-inference:thor-arm64

docker run -d --name cyber-inference \
  --runtime nvidia \
  -p 8337:8337 \
  -v "$PWD/data:/app/data" \
  -v "$PWD/models:/app/models" \
  ghcr.io/ramborogers/cyber-inference:thor-arm64

curl --fail --retry 90 --retry-delay 2 --retry-connrefused \
  http://localhost:8337/health
)
```

### Upgrade while preserving local state

Use the same host `data` and `models` directories when replacing a container. Pull the replacement
image before removing the running container so a failed pull does not interrupt the service.
These blocks use a subshell with `set -eu` to enforce that ordering without changing your interactive
shell. Preserve any custom environment variables, mounts, ports, and restart policy from your
existing deployment; the examples below use the default layout. Back up important data before upgrades.

#### Thor / DGX Spark ARM64 NVIDIA

```bash
(
set -eu
docker pull ghcr.io/ramborogers/cyber-inference:thor-arm64
docker rm -f cyber-inference

docker run -d --name cyber-inference \
  --runtime nvidia \
  -p 8337:8337 \
  -v "$PWD/data:/app/data" \
  -v "$PWD/models:/app/models" \
  ghcr.io/ramborogers/cyber-inference:thor-arm64

curl --fail --retry 90 --retry-delay 2 --retry-connrefused \
  http://localhost:8337/health
)
```

#### Linux AMD64 NVIDIA

```bash
(
set -eu
docker pull ghcr.io/ramborogers/cyber-inference:linux-amd64
docker rm -f cyber-inference

docker run -d --name cyber-inference \
  --gpus all \
  -p 8337:8337 \
  -v "$PWD/data:/app/data" \
  -v "$PWD/models:/app/models" \
  ghcr.io/ramborogers/cyber-inference:linux-amd64

curl --fail --retry 90 --retry-delay 2 --retry-connrefused \
  http://localhost:8337/health
)
```

## Configuration

![config.png](config.png)

Environment variables use the `CYBER_INFERENCE_` prefix, or you can just use the UI.

| Variable | Default | Description |
| --- | --- | --- |
| `CYBER_INFERENCE_HOST` | `0.0.0.0` | API bind host |
| `CYBER_INFERENCE_PORT` | `8337` | API bind port |
| `CYBER_INFERENCE_DATA_DIR` | `./data` | Database + logs directory |
| `CYBER_INFERENCE_MODELS_DIR` | `./models` | Model storage directory |
| `CYBER_INFERENCE_DEFAULT_CONTEXT_SIZE` | `8192` | Fallback context when native model metadata is unavailable |
| `CYBER_INFERENCE_MAX_CONTEXT_SIZE` | `32768` | Maximum explicit context override; native model windows may exceed it |
| `CYBER_INFERENCE_MODEL_IDLE_TIMEOUT` | `300` | Idle unload timeout in seconds |
| `CYBER_INFERENCE_MODEL_LOAD_TIMEOUT` | `300` | Startup readiness timeout in seconds |
| `CYBER_INFERENCE_PRE_MODEL_LOAD_COMMAND_ENABLED` | `false` | Run host command before model startup |
| `CYBER_INFERENCE_PRE_MODEL_LOAD_COMMAND` | `sudo sysctl -w vm.drop_caches=3` | Host command for pre-model load preparation |
| `CYBER_INFERENCE_PRE_MODEL_LOAD_COMMAND_TIMEOUT` | `15` | Pre-load command timeout in seconds |
| `CYBER_INFERENCE_MAX_LOADED_MODELS` | `1` | Max simultaneously loaded models |
| `CYBER_INFERENCE_MAX_MEMORY_PERCENT` | `80` | Memory pressure threshold |
| `CYBER_INFERENCE_LLAMA_GPU_LAYERS` | `-1` | llama.cpp GPU layer setting |
| `CYBER_INFERENCE_LLAMA_MTP_AUTO_ENABLE` | `true` | Auto-enable MTP for detected speculative GGUF models |
| `CYBER_INFERENCE_LLAMA_MTP_DEFAULT_DRAFT_N_MAX` | `2` | Default llama.cpp MTP draft token count |
| `CYBER_INFERENCE_ADMIN_PASSWORD` | unset | Enables admin auth when set |
| `CYBER_INFERENCE_HF_TOKEN` | unset | HuggingFace token for private repos |

When a model has no per-model context override, Cyber-Inference loads it with the native context
window discovered from its metadata. The global fallback is used only when native metadata is
unavailable. The maximum context setting limits explicit per-model and load-request overrides; it
does not reduce a known native window.

`GET /v1/models` reports the native capacity through `context_length`,
`max_context_length`, and `context_window`. `effective_context_length` reports the exact context
selected for a loaded backend, or the context that will be selected on its next load.

Large models can take several minutes before their backend server reports ready. The
`Model Load Timeout (seconds)` admin setting controls how long Cyber-Inference waits during model
startup before treating the load as failed. If startup times out, the launched backend process is
terminated and its port is released.

Thor/DGX Spark operators can enable `Run pre-model load command` in Admin Settings to clear Linux
disk/page cache before loading very large models. The default command is
`sudo sysctl -w vm.drop_caches=3`; configure passwordless sudo or run Cyber-Inference in a service
context that can execute the command without an interactive prompt. In this first release, public
`/v1` API lazy-loads skip the pre-load command; use the Admin UI load action when the host needs the
cache-clear hook before startup.

## Admin Endpoints

- `GET /admin/status`
- `GET /admin/resources`
- `GET /admin/models`
- `GET /admin/models/repo-files`
- `POST /admin/models/download`
- `POST /admin/models/download-transformers`
- `POST /admin/models/{model}/load`
- `POST /admin/models/{model}/unload`
- `DELETE /admin/models/{model}`
- `GET /admin/config`
- `PUT /admin/config/{key}`


## License
GPL-3.0
