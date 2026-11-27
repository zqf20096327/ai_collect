<p align="center">
  <img alt="rsibox" src="assets/rsibox-logo.svg" width="360">
</p>

<h3 align="center">Live Hot-Reload Sandbox &amp; Multi-Agent GPU Pool for ML Engines</h3>

<p align="center"><b>Keeping Weights Warm While AI Agents Optimize Production ML Engines</b></p>

<p align="center">
  <a href="#quick-start"><img alt="Quick Start" src="https://img.shields.io/badge/Quick%20Start-Guide-0f766e.svg"></a>
  <a href="core/livelab/formal/"><img alt="TLA+ Verified" src="https://img.shields.io/badge/Protocol-TLA%2B%20Verified-1d4ed8.svg"></a>
  <a href="pyproject.toml"><img alt="Python 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-3776ab.svg"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/License-Apache%202.0-green.svg"></a>
</p>

<p align="center">
  <a href="#why-rsibox"><b>Why RSIBox</b></a> ·
  <a href="#how-it-works"><b>How It Works</b></a> ·
  <a href="#supported-engines--results"><b>Engines &amp; Results</b></a> ·
  <a href="#quick-start"><b>Quick Start</b></a> ·
  <a href="#roadmap--documentation-map"><b>Roadmap &amp; Docs</b></a> ·
  <a href="https://github.com/hao-ai-lab"><b>Hao AI Lab</b></a>
</p>

`rsibox` adds safe live hot-reload and multi-agent GPU sharing to existing ML serving, training, and RL engines without rewriting them from scratch. Instead of paying a multi-minute cold restart on every edit to reload weights and recapture CUDA graphs, coding agents swap Python, Triton kernels, CUDA graphs, and C++/CUDA directly into the warm running engine — with execution proof and instant bit-exact rollback.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/rsibox-dynamo-4bar-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="assets/rsibox-dynamo-4bar-light.png">
    <img alt="RSIBox live hot-reload and NVIDIA Dynamo GMS and Snapshot latency comparison on NVIDIA B200" src="assets/rsibox-dynamo-4bar-light.png" width="100%">
  </picture>
</p>

## Why RSIBox

- **Every small edit forces a multi-minute cold restart:** Changing one scheduling line or kernel in a running ML engine normally tears down the worker, reloads tens of gigabytes of weights, and re-captures CUDA graphs (`66–298 s` per iteration).
- **Silent no-ops & stale CUDA graphs mislead optimization loops:** Naively monkey-patching Python fails silently when code never executes (`zero_witness`), or when `@triton.jit` binaries and captured `CUDAGraph` nodes continue replaying stale device pointers.
- **Concurrent agents contend & poison shared GPUs:** Running multiple coding agents against a fixed GPU budget serializes teams behind full restarts and lets one crashing edit stall or poison sibling workers.
- **Teams shouldn't have to rewrite production engines to get safe live iteration:** Engine teams need a drop-in runtime boundary (`install`, `check`, `reset`, `uninstall`, `status`) that composes with existing engines, launchers, and recovery backends like NVIDIA Dynamo GMS & Snapshot.

## How It Works

- **Keep GPU weights and states warm while swapping only what changed:** RSIBox applies each edit at the lowest safe tier — runtime flags, Python functions, `@triton.jit` kernels, selective CUDA graphs, or `.cu` side-libraries — with pre-warmed fork server and NVIDIA Dynamo GMS & Snapshot fallback when an edit crosses a process boundary or crashes a worker.
- **Atomic step-gap commit with execution proof and rollback:** Edits stage while the engine runs, commit atomically across all GPU ranks between steps, record per-rank call counts (`witness`) to prove the new code executed, and reverse bit-for-bit via a per-mutation journal (`~0.05 s` undo).
- **Formally verified protocols & sandbox verification suite:** Core swap, multi-rank coordinator, pool, standby shadow, and autoscaler protocols are specified in TLA+ ([`core/livelab/formal/`](core/livelab/formal/)) and validated against the growing **sandbox verification suite** (`rsibox conformance`, [`core/livelab/conformance/README.md`](core/livelab/conformance/README.md)).
- **Multi-agent GPU pool (`SandboxPool`):** Concurrent coding agents share warm GPUs via priority scheduling, anti-starvation aging, elastic role borrowing, per-agent fault isolation, and **`114/114`** verified tamper-evident traces (`43.7×–54.4×` faster than restarting; [study](docs/agent-teams-and-contention.md)).

Explore the interactive map in [`docs/architecture.html`](docs/architecture.html) or read the layer breakdown in [`docs/concepts.md`](docs/concepts.md):

```text
+---------------------------------------------------------------------------------------------------+
| Layer 1 · Control Plane               core/livelab/rsibox/                                        |
|   rsibox CLI & HTTP Box (cli/server) · SandboxPool & PoolAutoScaler · BaseLab / LabUnderTest      |
+---------------------------------------------------------------------------------------------------+
| Layer 2 · Hot-Reload Kernel (stdlib)  core/livelab/kernel/                                        |
|   Coordinator & Session (2PC) · swap & jit (R0 / Triton) · witness & Journal · findings/identity  |
+---------------------------------------------------------------------------------------------------+
| Layer 3 · Warm Recovery & Substrate   core/livelab/rsibox/warm/, forksafe.py                      |
|   forksafe & IPC · Zygote + CUDA IPC Holder · Dynamo GMS Standby Shadow & CRIU Snapshot           |
+---------------------------------------------------------------------------------------------------+
| Layer 4 · Thin Engine Adapters        repos/<engine>/livelab/ (10 engines)                        |
|   vLLM · SGLang · TRT-LLM · Transformers · Megatron-LM · FastVideo · veRL/miles/NeMo-RL/TorchTitan|
+===================================================================================================+
| Cross-Cutting Plane · core/livelab/{formal,conformance}/ & .agents/plugins/rstack/                |
|   TLA+ Protocol & Pool Models · Sandbox Verification Suite (c0-c10) · rstack PR & CI Gates        |
+---------------------------------------------------------------------------------------------------+
```

| Hot-Reload / Recovery Tier | What Changes | Typical Latency |
| :--- | :--- | ---: |
| **Live runtime config** | Scheduler & batching flags (`max_num_seqs`, policy) in process | `~4.3 ms` |
| **Python & Triton hot-swap** | Python functions & `@triton.jit` kernels across all ranks (`~0.05 s` undo) | `~58–92 ms` |
| **Selective CUDA graph recapture** | Only CUDA graphs affected by an edited forward path | `0.50–3.69 s` |
| **C++/CUDA (`.cu`) side-library reload** | Compiled native kernels rebound into `torch.ops._C` + selective recapture | `7.3–19.2 s` |
| **Dynamo GMS Standby Shadow / Snapshot** | Parked GPU-weight-resident failover (`0.10–0.37 s` SGLang / `0.31–1.86 s` vLLM) or CRIU + `cuda-checkpoint` restore | `0.10–6.96 s` |

## Supported Engines & Results

| Engine | Category | Supported Hot-Reload | Restart (Before) | `rsibox` Live (After) | Speedup |
| :--- | :--- | :--- | ---: | ---: | ---: |
| **`vLLM`** | Serving | Python, Triton, selective CUDA graphs, `.cu`, live reconfig, Dynamo GMS/Snapshot & Shadow | `228 s` | **`2.4–23.6 s`** (`~0.08 s` swap) | **up to 95×** |
| **`SGLang`** | Serving | Python, Triton, CUDA graphs, warm fork server, CUDA IPC, Dynamo GMS/Snapshot & Shadow | `66.4 s` | **`0.38–1.77 s`** | **up to 176×** |
| **`TRT-LLM`** | Serving | PyTorch backend live Python swaps, KV-cache quiesce/resume (`23.6 GiB` freed) | `26.7 s` / `12.4 s` | **`0.107 s`** (`56.4 ms` install) | **up to 249×** |
| **`Transformers`** | Inference | Persistent worker multi-module swaps, pinned-CPU weight quiesce/resume | `7.75 s` | **`0.61 s`** (`0.31 s` H2D resume) | **12.8×** |
| **`Megatron-LM`** | Training | Multi-GPU parallel live swaps, pre-warmed fork server | `57.5 s` / `266.7 s` | **`0.50 s`** / **`8.0–17.0 s`** | **up to 115×** |
| **`FastVideo`** | Video Gen | Sequence-parallel live swaps, FlashInfer preload, IPC weight holder | `206 s` | **`2.3–6.4 s`** | **up to 92×** |
| **`veRL`** | RL Post-Training | 21 Ray actors (eager & FSDP CUDA graphs) + coupled state reset | `298 s` | **`36.4 s`** (`12.6 ms` replay) | **8.2×** |
| **`miles`** | RL Post-Training | Ray rollout + trainer actors + coupled state reset (`38 ms` median commit) | `82.4 s` | **`0.89 s`** | **up to 93×** |
| **`TorchTitan`** | Training (FSDP2) | PyTorch FSDP2 (`1` & `2` GPU NCCL) + 2-rank CPU sandbox, state & RNG reset | `2.69 s` / `5.52 s` | **`0.083 s`** / **`0.255 s`** (`2`-rank cycle) | **32.5× / 21.6×** |
| **`NeMo-RL`** | RL Post-Training | AutoModel FSDP2 + SGLang GRPO (`1×/2×` B200 Ray actors + coupled `S0` reset; `c8` `731.5 s`, pre-fix `c0–c7, c9–c10`) | `186.8 s` / `151.5 s` | **`19.0 s`** / **`34.7 s`** (`4.6–4.8 s` install) | **9.8× / 4.4×** |

On `Megatron-LM`, an autonomous agent ran an **82-iteration** live hill-climb with **zero restarts** and found **+5.1% tokens/s/GPU** ([walkthrough](repos/megatron/examples/codex-hillclimb/README.md)). See **[`docs/concepts.md`](docs/concepts.md)** for core concepts, **[`docs/mechanisms.md`](docs/mechanisms.md)** for restart boundaries and Dynamo benchmarks, and **[`docs/engines.md`](docs/engines.md)** for full engine tables and per-tier costs.

<details>
<summary><b>More Results &amp; Safety Guarantees</b> (Dynamo GMS &amp; Snapshot alignment, multi-agent pool study, and safety table)</summary>

<p>
  <img alt="Matched 3-engine NVIDIA Dynamo Snapshot and RSIBox latency alignment on NVIDIA B200" src="assets/dynamo-3engine-4case-benchmark.svg" width="100%">
</p>

<p>
  <img alt="Multi-agent SandboxPool full-stack integration and rogue-agent blast radius containment on NVIDIA B200" src="assets/agent-teams-fullstack-and-blast-radius.svg" width="100%">
</p>

| Guarantee | What It Enforces |
| :--- | :--- |
| **[Atomic step-gap swap](docs/mechanisms.md)** | Stages edits while the engine runs and commits across all ranks together between steps. |
| **[Execution check](core/livelab/INTERFACE.md)** | Counts calls on every rank so silent no-op edits (`zero_witness`) fail instead of passing. |
| **[Journaled rollback](docs/mechanisms.md)** | Logs every mutation's inverse; `uninstall` restores exact code objects and verifies base identity. |
| **[Explicit restart boundaries](docs/kernels-and-graphs.md)** | Refuses unsafe edits before touching state and names the cheapest warm tier (Triton, CUDA graph recapture, `.cu` reload, or pre-warmed fork server + CUDA IPC). |
| **[Sandbox verification suite](core/livelab/conformance/README.md)** | Verifies repeatability, parity with fresh restart, crash/hang fault handling, and repeated undo stability. |

See [`docs/mechanisms.md`](docs/mechanisms.md) for all restart boundaries and CPU tests, and [`core/agents/`](core/agents/) for ready-to-use agent prompts.

</details>

## Use with Your Coding Agent

*Paste this prompt into Claude Code, Codex, Cursor, or Antigravity — zero manual setup:*

```text
Install https://github.com/hao-ai-lab/rsibox.git and read core/agents/livelab_overview.md.
Whenever we edit or benchmark an ML engine, use rsibox to hot-reload and verify changes in-place instead of restarting.
```

**Or install it as a reusable agent skill** ([`core/agents/livelab_overview.md`](core/agents/livelab_overview.md) already ships with `SKILL.md` frontmatter):

```bash
git clone https://github.com/hao-ai-lab/rsibox.git
mkdir -p ~/.claude/skills/rsibox && ln -sf "$(pwd)/rsibox/core/agents/livelab_overview.md" ~/.claude/skills/rsibox/SKILL.md
```

## Quick Start

Requires Python 3.11+ (CPU-only, zero third-party dependencies for core and toy labs):

```bash
git clone https://github.com/hao-ai-lab/rsibox.git && cd rsibox
python3 -m venv .venv && . .venv/bin/activate && pip install -e .

# 1. Start a live sandbox and wait until warm
rsibox up --launcher local --lab toy --state /tmp/rsibox-toy
export RSIBOX=/tmp/rsibox-toy/box.json
rsibox wait

# 2. Fetch live source, edit 1 line, hot-reload, verify, and roll back
rsibox source toy.ops > /tmp/ops.py
sed -i.bak 's/return x + 1/return x + 100/' /tmp/ops.py
rsibox install --file toy.ops=/tmp/ops.py
rsibox check          # proves the edited function ran and shows the new output
rsibox uninstall      # instant journaled rollback to base
rsibox down --state /tmp/rsibox-toy
```

For real GPU engines (local, Docker, gVisor, or Slurm), pass `--real` and see [`core/livelab/rsibox/README.md`](core/livelab/rsibox/README.md) or `rsibox conformance <engine> --real -- --help`:

```bash
rsibox up --launcher local --lab vllm --real --state /tmp/rsibox-vllm \
  --env RSIBOX_VLLM_MODEL=Qwen/Qwen3-8B
```

## Roadmap & Documentation Map

| Milestone | Status | Scope |
| :--- | :---: | :--- |
| **v0** | ✅ Done | Core hot-reload runtime (`install` / `check` / `reset` / `uninstall` / `status`), 10 engine adapters, TLA+ formal suite (`SwapLifecycle`, `Coordinator`, `SandboxPool`, `StandbyShadow`, `PoolAutoScaler`) |
| **v1** | ✅ Done | NVIDIA Dynamo GMS & Snapshot recovery ([`rsibox.warm`](core/livelab/rsibox/warm/README.md)), `SandboxPool` multi-agent resilience (`114/114` verified traces), in-repo `rstack` gates |
| **v2** | 🚧 Roadmap | `NeMo-RL` post-fix `11/11` `--real` conformance (`#325`) & `TorchTitan` Llama3, `Tier-A` `cuGraphExecKernelNodeSetParams` generalization, NVIDIA Dynamo & Omni engine onboarding |

- **[`docs/concepts.md`](docs/concepts.md)** — Plain-English overview of `rsibox`, hot-reload tiers, execution proof (`witness`), and journaled rollback.
- **[`docs/engines.md`](docs/engines.md)** — Full 10-engine summary, measured speedups, and repository layout.
- **[`docs/mechanisms.md`](docs/mechanisms.md)** — Restart-boundary table, NVIDIA Dynamo GMS & Snapshot alignment benchmarks, and CPU tests.
- **[`docs/kernels-and-graphs.md`](docs/kernels-and-graphs.md)** — Deep dive into Python bytecode swaps, Triton `@jit` rebuilds, and CUDA graph replay / `Tier-A` patching.
- **[`docs/agent-teams-and-contention.md`](docs/agent-teams-and-contention.md)** — Multi-agent `SandboxPool` contention, Standby Shadow failover, rogue isolation, and elastic scaling study.
- **[`core/livelab/conformance/README.md`](core/livelab/conformance/README.md)** — The sandbox verification suite (`rsibox conformance`) and CPU toy lab guide.
- **[`CONTRIBUTING.md`](CONTRIBUTING.md)** & **[`.agents/plugins/rstack/README.md`](.agents/plugins/rstack/README.md)** — Contributor guidelines and deterministic `rstack` workflow gates.

## Contributors

<p>
  <a href="https://github.com/GindaChen"><img src="https://github.com/GindaChen.png?size=112" width="56" alt="Junda Chen" title="Junda Chen (@GindaChen)"></a>
</p>

## Citation

```bibtex
@misc{rsibox2026,
  title        = {rsibox: Live Hot-Reload Sandbox for ML Engines},
  author       = {Hao AI Lab},
  year         = {2026},
  howpublished = {\url{https://github.com/hao-ai-lab/rsibox}}
}
```

## License

Apache License 2.0 — see [`LICENSE`](LICENSE).
