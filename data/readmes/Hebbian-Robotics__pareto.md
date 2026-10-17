<p align="center">
  <a href="https://pareto.hebbianrobotics.com">
    <img src="docs/assets/hebbian-logo-on-black.svg" alt="Hebbian Robotics" width="128">
  </a>
</p>

# Pareto

**High quality data curation for training AI models for robotics**

<p align="center">
  <a href="https://pareto.hebbianrobotics.com"><strong>Try hosted Pareto</strong></a>
  ·
  <a href="https://hebbianrobotics.com/blog/youtube-system-design-for-robotics-data-infrastructure"><strong>Read the architecture deep dive</strong></a>
</p>

Robotics teams collect far more demonstrations than make it into training
sets. Deciding what counts as "high quality" is still painfully manual, so
curation often falls back to brittle, hand-crafted heuristics—or discards most
of the data entirely.

Pareto helps teams find their best training samples and evaluate data
collection with the same rigor they bring to models. Upload a
[LeRobot](https://github.com/huggingface/lerobot) dataset and Pareto indexes
consistency metrics, maps behavioral clusters, surfaces potential anomalies,
and makes every episode searchable down to the supporting frames.

The goal is not another dataset viewer. It is a system for understanding what
your data contains, where collection behavior drifts, and which demonstrations
belong in the next training run.

## Community edition

This repository is the community edition of the data-quality system we build
and operate at [Hebbian Robotics](https://hebbianrobotics.com). We publish the
core indexing, analysis, search, API, and UI so robotics teams can inspect the
architecture, adapt it to their own datasets, and contribute improvements
without treating their data infrastructure as a black box.

The community edition is self-hostable and is a practical fit for local
evaluation and trusted, single-organization deployments. Teams that want a
managed experience, production support, enterprise integrations, or stronger
multi-tenant isolation can [try hosted Pareto](https://pareto.hebbianrobotics.com)
or [get in touch with Hebbian Robotics](https://hebbianrobotics.com).

## What Pareto does

- **Measures consistency.** Compare visual, trajectory, and endpoint agreement
  across demonstrations, then localize the parts of an episode that look
  anomalous.
- **Reveals behavioral structure.** Group related demonstrations with HDBSCAN,
  explore representative episodes, and separate dense behaviors from noise.
- **Finds data problems.** Detect near-duplicates, probe condition coverage,
  compare rollout failures with training data, and attach durable annotations.
- **Searches the evidence.** Ask for something like **"pink lego brick"** and
  retrieve ranked episodes plus the exact matching frames across every camera.
- **Builds training-ready subsets.** Select useful episodes and export a new,
  valid LeRobot dataset for downstream VLA training.

## Quick start

Install the CLI from this checkout:

```bash
cargo install --path crates/cli --locked
```

Then point it at a local [LeRobot](https://github.com/huggingface/lerobot)
dataset:

```
pareto index .data/robot_data                       # index metrics, assets, and embeddings
pareto consistency .data/robot_data                 # rank and localize consistency outliers
pareto search "pink lego brick" --limit 10           # retrieve episodes + evidence frames
pareto export .data/robot_data 3,17,24 ./curated-subset
PARETO_DATABASE_URL=postgres://… pareto serve         # launch the API on :4800
```

The direct commands above the server line are synchronous and need no
infrastructure. For a local API/UI plus Postgres and a durable worker, use
[`deploy/jobs/docker-compose.yml`](./deploy/jobs/docker-compose.yml).

The public beta remains the default data scope. A legacy CLI operator can proxy
one request into an isolated organization scope with
`--organization org_…` (or `PARETO_ORGANIZATION_ID`) when server mode is active;
the selector is rejected by direct commands and by anonymous requests. This is
the storage and control-plane tenancy foundation, not browser authentication:
run separate deployments for mutually untrusted browser users until the
verified WorkOS adapter described in
[`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md#tenancy-and-authentication)
is installed.

Pareto also answers dataset-debugging questions directly:

```
pareto dupes    <ds>                                # near-identical episodes (over-representation)
pareto coverage <ds> --probes "occluded gripper,hand in frame"   # how thin is each condition?
pareto triage --rollouts <R> --training <T>         # are these failures represented in training?
pareto annotate <ds> --episode 38 --key team.quality/exemplar --value true
```

Every command takes `--json` (stable, versioned envelope) and, with
`PARETO_SERVER_URL` set, proxies through a running server so the web UI's
**activity feed** shows agent actions live (its *follow mode* mirrors the
agent's searches into the results grid). Point a coding agent at the CLI and
it can hunt gaps, audit datasets, and write findings back as annotations —
start from `pareto capabilities --json`. In server mode, the trusted legacy
operator may add `--organization <workos_org_id>`; the flag overrides
`PARETO_ORGANIZATION_ID`. Selection-manifest v1 remains public by itself, so an
organization-scoped server operation combines the unchanged manifest with that
selector.

The web UI can search all compatible datasets, one dataset, or an explicit
multi-dataset selection. Episode detail keeps every camera on one synchronized
transport, with keyboard/pointer scrubbing and an automatic or pinned preview
quality shared across the camera grid.

## Why

Episode curation is a bottleneck in VLA training, and generic vision tools do
not fit the problem. The unit of analysis is an *episode*: synchronized
multi-camera video, states, actions, and a language task. Evidence may live at a
single frame, while consistency emerges across an entire trajectory or across
many demonstrations.

Pareto is built around that full loop:

**index → measure → cluster → inspect → select → export**

Instead of micromanaging collection or encoding every judgment as a threshold,
teams can use measurable proxies for what a consistent data collection process
would produce—and keep those decisions connected to the underlying evidence.

## Research direction: task velocity debiasing

Operator speed creates artificial variation: different people, or the same
person on different days, can execute the same behavior at different rates.
Task velocity debiasing aims to normalize that variation so models see a more
consistent motion distribution without requiring more demonstrations.

[Shi et al. (2025)](https://arxiv.org/abs/2507.06219v1) report up to a 60%
improvement in task-completion scores from velocity debiasing on their research
benchmarks—comparable in that setting to scaling the training dataset by 2.5×.
Pareto currently surfaces this as a data-development recommendation; making
techniques like it measurable and repeatable is part of the broader direction
for the quality index.

## Built with the robotics data community

Pareto builds on the [LeRobot dataset format and visualizer](https://github.com/huggingface/lerobot)
from Hugging Face and on research that treats data composition as a first-class
part of model development. We hope the quality-indexing layer contributed here
proves just as useful to the community.

## How it works

- **No ML runtime in the binary.** Frames are embedded by an external service
  behind an `EmbeddingProvider` trait — a self-hosted SigLIP 2 service, selected
  with `PARETO_EMBED_PROVIDER=siglip` + `PARETO_SIGLIP_URL`;
  the model id and vector dimension are read from the service's `/health` at
  startup. A deterministic mock provider runs everything offline for tests and
  development. An index records the exact model id and refuses mismatched
  queries.
- **Frames are evidence, episodes are results.** Sampled frames are stored in
  LanceDB with episode/camera/time metadata; text queries rank episodes by
  pooled frame scores and return the matching frames with thumbnails and
  preview clips. CLI help owns sampling and ranking defaults.
- **The HTTP API is the product surface.** axum + OpenAPI 3.1 (`/openapi.json`);
  the separately deployed React UI is one generated-client consumer — bring
  your own.
- **Stateless server process.** Indexes and derived assets live under the data
  root; the dataset catalog lives in Postgres; durable jobs ARE Temporal
  workflows (acquisition, conversion, ingest, export, backfills), executed by
  capability-isolated workers — see `docs/ARCHITECTURE.md`.

## Requirements

- Rust and `protoc` (LanceDB build dependency); the deployment Rust version is
  pinned in [`Dockerfile`](./Dockerfile)
- Node and pnpm for the UI; deployment versions are owned by the relevant
  hosting configuration
- Postgres for `pareto serve` and `pareto worker`; the tested version is pinned
  in [`deploy/jobs/docker-compose.yml`](./deploy/jobs/docker-compose.yml) (not
  required for direct CLI commands or the default test suite)
- ffmpeg is **not** required — a static build (with AV1 decode) is downloaded
  automatically on first use
- For real embeddings: a reachable SigLIP 2 service with its URL in
  `PARETO_SIGLIP_URL` and `PARETO_EMBED_PROVIDER=siglip`. The service exposes
  OpenAI-compatible text and Cohere-compatible image embedding. Without one,
  `PARETO_EMBED_PROVIDER=mock` (the default when no SigLIP URL is set) exercises
  the whole pipeline offline.

## Configuration

Use `pareto <command> --help` for CLI flags and defaults. Runtime environment
variables are defined next to the code that reads them; production values are
owned by the deployment manifests rather than repeated here:

- embedding: [`crates/embed/src/lib.rs`](./crates/embed/src/lib.rs)
- indexing and GPU media: [`crates/index-core/src/gpu_services.rs`](./crates/index-core/src/gpu_services.rs)
- server and access control: [`crates/server-core/src/lib.rs`](./crates/server-core/src/lib.rs)
  and [`crates/server-handlers/src/lib.rs`](./crates/server-handlers/src/lib.rs)
- durable jobs: [`deploy/jobs/README.md`](./deploy/jobs/README.md)
- self-hosted control plane: [`deploy/jobs/docker-compose.yml`](./deploy/jobs/docker-compose.yml)

## Repository layout

[`Cargo.toml`](./Cargo.toml) is the canonical Rust workspace inventory.
[`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) describes the subsystem
boundaries; service, tool, deployment, and UI directories carry local READMEs.
See [CONTRIBUTING.md](./CONTRIBUTING.md) for the development quality gates.

The GPU decoder and ingest process must see local videos at the same absolute
path. For `gs://` inputs, `PARETO_DATASET_CACHE_DIR` places the lazily
materialized videos beneath a shared parent and makes them readable by the
sidecar without changing the default cache behavior. The complete
loopback-only, two-container wiring is documented in
[services/gpu-decode/README.md](./services/gpu-decode/README.md#docker-deployment).
