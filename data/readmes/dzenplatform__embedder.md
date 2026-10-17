# Dzen Embedder

Docker image: [mxen/dzen-embedder on Docker Hub](https://hub.docker.com/r/mxen/dzen-embedder).

## Quick start

```sh
git clone https://github.com/dzenplatform/embedder.git
cd embedder

# Linux CPU
docker compose up -d
```

The first start downloads the model. The API is available at
`http://127.0.0.1:8091`; check readiness with
`curl --fail http://127.0.0.1:8091/ready`.

For an NVIDIA GPU, install the host driver and
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html),
then use `docker compose -f compose.yaml -f compose.cuda.yaml up -d`
instead of the CPU command. See [Docker](#docker) for image tags and configuration.

**On macOS, run natively.** For Apple Silicon, run these commands from the checkout:

```sh
DEVICE=mps make setup
DEVICE=mps make run
```

On Intel Macs, use `DEVICE=cpu` instead. Apple GPU acceleration through MPS
requires a native macOS process and is unavailable in this Linux Docker image.

Standalone single-process embedding service for [Dzen Chat](https://dzen.dev/chat/). It loads one
SentenceTransformer model and exposes an OpenAI-compatible
`POST /v1/embeddings` endpoint. Realtime requests have strict priority over
batch requests.

Learn more: [Local Dzen Embedding for RAG](https://dzen.dev/blog/local-dzen-embedding-for-rag/).

## Deploy with an agent

Copy this prompt and give it to your coding agent:

```text
Read and follow the deployment instructions at:
https://raw.githubusercontent.com/dzenplatform/embedder/master/llm-setup.txt
```

## Local setup

```sh
make setup
make run
```

`make setup` installs dependencies and downloads the model to
`models/user-bge-m3`. That directory is ignored by Git, so it can be removed
together with the local checkout.

## Runtime device

The service accepts three explicit devices: `cpu`, `mps` (Apple Silicon Metal
Performance Shaders), and `cuda` (NVIDIA GPU). `mps` is the intended correction
for “mpl”; there is no PyTorch device named `mpl`.

Set the device in `local.yaml` before setup:

```yaml
device: cpu
```

`local.yaml` is optional and is merged over the tracked
`embedder/config.yaml`. For a one-off override, use the setting field name as
an environment variable:

```sh
DEVICE=mps make setup
DEVICE=mps make run
```

The service fails during model loading if the selected backend is unavailable.

`make setup` reads `device` from the merged YAML configuration. On Linux it installs the
CPU-only PyTorch wheel for `cpu`, and the CUDA wheel selected by
`pytorch_cuda_index` for `cuda` (default: `cu126`). On macOS, `mps` uses the
regular PyTorch wheel and verifies that MPS is available. Set the intended
device in `local.yaml` before the first `make setup` or after changing hardware.

`make run` only starts a prepared service. If the environment or model is
missing, it stops with the corresponding `make setup` instruction.

For Docker, use `DEVICE=cpu` without `--gpus all`, or `DEVICE=cuda` together
with `--gpus all`. MPS requires a native macOS Python process, so use
`DEVICE=mps make run`; Docker Desktop
does not expose the Metal backend to this Linux container.

## Configuration

`embedder/config.yaml` contains the defaults. Put local or deployment-specific
overrides in `local.yaml`; environment variables whose names match a settings
field case-insensitively override both YAML files. For example, `PORT=18091`
and `DASHBOARD_ENABLED=true` override those settings. `CUDA_VISIBLE_DEVICES`
selects the NVIDIA GPU only for the `cuda` device; run exactly one service
process per GPU.

Set `dashboard_enabled: true` in `local.yaml` only when the internal queue page
must be available. Otherwise `/dashboard` shows an unavailable page with a link
to Dzen Chat; its JSON data endpoint is not registered. Prometheus metrics are
always exposed at `/metrics` for scraping by the monitoring system.

## API

```sh
curl http://127.0.0.1:8091/v1/embeddings \
  -H 'content-type: application/json' \
  -d '{"model":"deepvk/USER-bge-m3","input":["hello"],"encoding_format":"float"}'
```

Use `X-Dzen-Embedding-Priority: batch` only for deferred document work.
Requests without it are realtime.

## Docker

Project images use the Docker Hub repository `mxen/dzen-embedder`.
These are publisher-maintained images, not Docker's curated “Docker Official Images”.

| Tags | Platforms | Backend |
| --- | --- | --- |
| `0.1.0-cpu`, `cpu`, `latest` | Linux amd64 and arm64 | CPU |
| `0.1.0-cu126`, `cu126` | Linux amd64 | NVIDIA CUDA 12.6, PyTorch 2.6.0 |

Versioned tags identify a release; `cpu`, `cu126`, and `latest` move with releases.
Use a versioned tag, or an image digest for immutable production deployments.
Docker selects amd64/arm64 automatically from the CPU image manifest.
The CUDA tag selects the software stack, not the GPU generation or fastest settings.
Do not assume that a CUDA version supports every NVIDIA card; new GPU generations
may need a separate, newer PyTorch/CUDA variant. Jetson and CUDA arm64 are not
included in this release.

MPS (Apple Metal) requires native macOS. Linux containers on a Mac run the CPU
variant; use `make run-mps` outside Docker to use the Apple GPU.
See [Docker GPU support](https://docs.docker.com/desktop/features/gpu/).

From a checkout (or a directory containing the supplied Compose files):

```sh
# CPU: pulls the image, downloads the model into a persistent volume, then starts.
docker compose up -d

# NVIDIA: use this command instead of the CPU command.
docker compose -f compose.yaml -f compose.cuda.yaml up -d

curl --fail http://127.0.0.1:8091/ready
```

The NVIDIA host needs a compatible driver and the
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
The Compose override explicitly reserves GPU 0; set `GPU_DEVICE_ID` to select
another GPU. A tag alone does not grant GPU access.
The driver is installed on the host, not inside the image. The CUDA PyTorch wheel
installs its matching runtime libraries inside the image.

`EMBEDDER_TAG`, `EMBEDDER_PORT`, and `MODEL_ID` can be set in `.env` or the shell.
For example, `EMBEDDER_TAG=0.1.0-cpu docker compose up -d`.
The model is downloaded on first use and reused from the `models` volume; changing
`MODEL_ID` uses a separate model directory. Internet access is required to fetch it.
The API binds to localhost by default. Containers in another Compose service can
use `http://embedder:8091`. For external access use an authenticated proxy, such as
`deploy/nginx/embedder.conf.example`.

Build locally:

```sh
docker build --build-arg VARIANT=cpu -t mxen/dzen-embedder:0.1.0-cpu .
docker build --platform linux/amd64 --build-arg VARIANT=cu126 -t mxen/dzen-embedder:0.1.0-cu126 .
```

The image pins PyTorch and the text inference dependencies under `deploy/docker/`.
It intentionally excludes torchvision and torchaudio: neither is needed for text
embeddings, and mixing their CPU/CUDA builds can break Transformers imports.
Each build checks dependency consistency and imports the real application.
The service runs as UID 10001 and does not silently switch CUDA requests to CPU.
Bind-mounted model directories must be readable by this user (writable when fetching).

### Publishing

Configure the GitHub repository secret `DOCKERHUB_TOKEN` with a Docker Hub access
token allowed to push `mxen/dzen-embedder`. Pushing a tag matching the package
version, such as `v0.1.0`, builds and publishes both variants through
`.github/workflows/docker.yml`. Pull requests and manual workflow runs build only.
Before tagging a release, test an actual embedding request on CPU and on a
supported NVIDIA host. A cross-build/import check does not verify GPU inference.
The workflow skips an already published version tag, so retries can complete a
partially published release without replacing its existing images. Bump the
package version for a new release.

## Systemd

The static Linux units are `deploy/systemd/embedder-cpu.service` and
`deploy/systemd/embedder-gpu.service`. Install or switch the active mode:

```sh
# local.yaml is in the repository root on the server
make setup
deploy/systemd/install.sh cpu
# Later, set `device: cuda` in local.yaml, then:
make setup
deploy/systemd/install.sh gpu
```

Each unit pins `DEVICE` independently from YAML. The units assume the checkout
is `/var/www/dzen-embedder` and run as `deploy`. MPS is macOS-only and therefore
has no systemd unit; use `DEVICE=mps make run`.

## Tests

```sh
make test
```

## Connection capacity

The service was measured with concurrent HTTP connections in realtime, batch,
and mixed-priority scenarios. The chart compares Apple M2 Max (MPS),
`dzen.dev` (NVIDIA GTX 1080), and `bear.infraforecast.com` (CPU) using the
same model and load shape. The red cross identifies the measured failure point,
not an unavailable environment.

![Connection-capacity benchmark](docs/benchmarks/connection-capacity.svg)

The complete method, results, and raw JSON are in
[the connection-capacity report](docs/benchmarks/2026-08-31-connection-capacity.md).

## License

[BSD 3-Clause](LICENSE) © 2026 Milkhail Kashkin <https://dzen.dev/>.
