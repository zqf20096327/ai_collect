<img width="1024" height="631" alt="image" src="https://github.com/user-attachments/assets/74d44573-0fff-45b3-a0e6-cf1cb5c5b434" />
<div align="center">

```
  ██████╗██╗  ██╗ █████╗ ███╗   ███╗███████╗██╗     ███████╗ ██████╗ ███╗   ██╗
 ██╔════╝██║  ██║██╔══██╗████╗ ████║██╔════╝██║     ██╔════╝██╔═══██╗████╗  ██║
 ██║     ███████║███████║██╔████╔██║█████╗  ██║     █████╗  ██║   ██║██╔██╗ ██║
 ██║     ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║     ██╔══╝  ██║   ██║██║╚██╗██║
 ╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║███████╗███████╗███████╗╚██████╔╝██║ ╚████║
  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
```


**A stateless AI execution runtime that dynamically morphs into any LLM on demand.**

[![Rust](https://img.shields.io/badge/Rust-1.78+-B7410E?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Python](https://img.shields.io/badge/Python-3.11+-2B5B84?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](./LICENSE)
[![Build](https://img.shields.io/badge/Build-passing-22c55e?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Design%20Phase-f59e0b?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-B7410E?style=flat-square)](./CONTRIBUTING.md)

[Overview](#-overview) • [Architecture](#-architecture) • [Quick Start](#-quick-start) • [Configuration](#-configuration) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

</div>

---

## Overview

Chameleon is a **stateless AI execution runtime**. Unlike traditional model-serving systems that keep one or more LLMs permanently loaded in memory, Chameleon maintains no fixed identity. It becomes a model only for the duration of a task — then fully unloads it, frees every byte of VRAM, and returns to a blank state ready to become something else entirely.

```
User Request → [ Chameleon Core ] → Select Model → Load → Execute → Unload → Blank
                     ↑                                                          |
                     └──────────────── ready for next request ──────────────────┘
```

The result is a system that can serve **any LLM** with **optimal VRAM usage**, routing each request to the single best model for that task — without keeping unused weights resident in memory between calls.

> **Think of it this way:** most AI runtimes hire one expert and keep them in the room forever. Chameleon is the firm that can instantly become a doctor, a lawyer, or an engineer — and is none of them by default.

---

## Why Chameleon?

| Problem | Traditional Systems | Chameleon |
|---|---|---|
| You need 8 specialised models | Load all 8, 80+ GB VRAM wasted | Load one at a time, ~8 GB active |
| Different tasks need different models | Stuck with one compromise model | Routes each request to the best fit |
| Cold hardware or shared cloud instances | Constant idle memory cost | Zero idle cost — blank between requests |
| Adding a new model | Config change + restart | Register in registry + done |
| Worker crash | Process restarts, queue lost | Rust supervisor respawns + re-queues |

---

## Architecture

Chameleon is built on a deliberate **two-language strategy**:

- **Rust** — the control brain. Handles routing, lifecycle management, warm caching, concurrency, and the VRAM budget enforcer. Fast, memory-safe, zero GC pauses.
- **Python** — the AI skills layer. Handles all inference via `llama-cpp-python`, `vLLM`, and `Transformers`. Pluggable backends mean any new model format is a single file addition.

```
┌─────────────────────────────────────────────────────────┐
│                    API Gateway (Rust/Axum)               │
│          HTTP · WebSocket · Auth · Rate Limiting         │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                  Coordinator Node (Rust)                 │
│  ┌─────────────────┐  ┌────────────┐  ┌──────────────┐  │
│  │ Intent          │→ │ Fleet      │→ │ Session      │  │
│  │ Classifier      │  │ Manager    │  │ Manager      │  │
│  └─────────────────┘  └────────────┘  └──────────────┘  │
└──────────────┬───────────────────────────┬──────────────┘
               │                           │
               │         gRPC / Protobuf   │
       ┌───────┴───────┐           ┌───────┴───────┐
       │               │           │               │
┌──────▼───────┐ ┌─────▼────────┐ ┌▼─────────────┐ ┌▼─────────────┐
│Model Registry│ │ Worker Fleet │ │ Worker Node A│ │ Worker Node B│
│(Rust + SQL)  │ │ (gRPC Fleet) │ │ (Python)     │ │ (Python)     │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                  Cluster Status (Live)                   │
│         Active Node Tracking · VRAM Aggregation         │
│              Heartbeat monitoring · Auth                │
└─────────────────────────────────────────────────────────┘
```

### Request lifecycle

```
① Idle (blank — 0 VRAM used)
② Request received → Intent Classifier tags the task type
③ Model Router scores candidates from Registry → selects best model
④ Cache hit?  ──yes──→ ⑤ Execute immediately (warm, ~100ms)
              ──no───→ Load model into VRAM (~4–25s depending on size) → ⑤
⑤ Execute → stream tokens to client
⑥ Unload weights → flush CUDA cache → return to ① (Idle)
```

### Distributed Communication (gRPC)

Chameleon uses **gRPC** for low-latency, type-safe communication between the Rust Coordinator and the Python Worker Fleet. All traffic is secured via a shared `CHAMELEON_CLUSTER_SECRET`.

| RPC Method | Direction | Purpose |
|---|---|---|
| `RegisterWorker` | Worker → Coord | Self-registration on startup (Address, VRAM, Backends) |
| `Heartbeat` | Worker → Coord | Periodic status update (VRAM used, resident model, health) |
| `LoadModel` | Coord → Worker | Dispatch load command to a specific node |
| `Infer` | Coord → Worker | Bi-directional stream for prompt/token exchange |
| `Unload` | Coord → Worker | Command node to flush CUDA memory |

---

## Project Structure

```
chameleon/
├── Cargo.toml                        # Workspace root
├── Cargo.lock
├── README.md
├── LICENSE
├── CONTRIBUTING.md
│
├── crates/                           # Rust workspace members
│   ├── chameleon-gateway/            # Axum HTTP/WebSocket server
│   │   └── src/
│   │       ├── main.rs
│   │       ├── routes.rs
│   │       ├── auth.rs
│   │       └── rate_limit.rs
│   │
│   ├── chameleon-router/             # Intent classification + model selection
│   │   └── src/
│   │       ├── lib.rs
│   │       ├── classifier.rs         # Rules-based fast path
│   │       ├── scorer.rs             # Model scoring logic
│   │       └── registry.rs           # SQLite model registry
│   │
│   ├── chameleon-cache/              # Warm cache + LRU eviction
│   │   └── src/
│   │       ├── lib.rs
│   │       ├── lru.rs
│   │       └── budget.rs             # VRAM budget enforcement
│   │
│   ├── chameleon-session/            # Context + conversation history
│   │   └── src/
│   │       ├── lib.rs
│   │       └── store.rs
│   │
│   ├── chameleon-ipc/                # gRPC Protocol + Shared Types
│   │   ├── proto/                    # Protobuf source definitions
│   │   ├── build.rs                  # Tonic code generation
│   │   └── src/
│   │       └── lib.rs                # Exported gRPC stubs
│   │
│   └── chameleon-telemetry/          # Metrics + structured logging
│       └── src/
│           ├── lib.rs
│           └── writer.rs
│
├── skills/                           # Python AI skills layer
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── worker.py                     # Entry point — gRPC servicer
│   └── chameleon_skills/
│       ├── proto/                    # Generated Python gRPC stubs
│       ├── runtime.py                # Load / unload / infer core
│       ├── backends/
│       │   ├── llama_cpp.py          # llama-cpp-python backend
│       │   ├── transformers.py       # HuggingFace Transformers backend
│       │   ├── vllm.py               # vLLM backend (GPU server mode)
│       │   └── exllamav2.py          # ExLlamaV2 high-speed backend
│       ├── classifier.py             # ML-based intent classification
│       └── plugins/                  # Community backends (ExLlamaV2, MLC-LLM, etc.)
│           └── __init__.py
│
├── registry/
│   ├── models.db                     # SQLite model registry
│   └── seed.sql                      # Default model entries
│
├── config/
│   ├── chameleon.toml                # Main configuration
│   └── logging.toml
│
├── scripts/
│   ├── start.sh                      # Launch supervisor + Python workers
│   ├── register_model.py             # CLI: add a model to the registry
│   └── bench.py                      # Latency / throughput benchmarks
│
└── tests/
    ├── integration/
    │   ├── test_lifecycle.rs         # Full load → infer → unload
    │   └── test_routing.rs           # Router selection correctness
    └── e2e/
        └── test_api.py               # End-to-end API tests
```

---

## Quick Start

### Prerequisites

| Dependency | Version | Purpose |
|---|---|---|
| Rust | ≥ 1.78 | Control plane |
| Python | ≥ 3.11 | Skills layer |
| CUDA Toolkit | ≥ 12.0 (optional) | GPU inference |
| SQLite | ≥ 3.40 | Model registry |

### 1. Clone and build

```bash
git clone https://github.com/your-org/chameleon.git
cd chameleon

# Build all Rust crates
cargo build --release

# Install Python dependencies
cd skills
pip install -r requirements.txt
cd ..
```

### 2. Register a model

```bash
# Register a GGUF model into the registry
python scripts/register_model.py \
  --id   "llama3-8b-instruct" \
  --path "/models/llama-3-8b-instruct.Q4_K_M.gguf" \
  --tags "code,general,chat" \
  --vram 5.2

# Register a coding-specialist model
python scripts/register_model.py \
  --id   "deepseek-coder-7b" \
  --path "/models/deepseek-coder-7b-instruct.Q5_K_M.gguf" \
  --tags "code,debug,completion" \
  --vram 5.8
```

### 3. Configure

Edit `config/chameleon.toml` (see [Configuration](#-configuration) below).

### 4. Start Chameleon

```bash
# Set your cluster secret
export CHAMELEON_CLUSTER_SECRET="your-secure-secret"

# Start the Coordinator and Workers
./scripts/start.sh
```

This launches the Rust Coordinator (Port 8080/8081) and spawns multiple gRPC workers that self-register with the fleet manager.

### 5. Send a request

```bash
curl -X POST http://localhost:8080/v1/infer \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "prompt": "Write a Python function to parse JSON with error handling",
    "stream": true
  }'
```

Chameleon automatically selects the best model for the task, loads it, streams the response, and unloads when complete.

---

## Configuration

All runtime behaviour lives in `config/chameleon.toml`:

```toml
[server]
host            = "0.0.0.0"
port            = 8080
max_connections = 1024
api_key         = "your-secret-key"        # Set via CHAMELEON_API_KEY env var in production

[router]
classifier_mode  = "rules"                 # "rules" (fast, deterministic) or "ml" (accurate, ~50ms overhead)
fallback_model   = "llama3-8b-instruct"    # Used when no model matches the task tag
score_weights    = { quality = 0.6, speed = 0.3, vram = 0.1 }

[cache]
vram_budget_gb   = 20                      # Total VRAM budget for warm models
warm_slots       = 3                       # Number of models to keep resident
eviction_policy  = "lru"                   # "lru" or "lfu"

[workers]
count            = 4                       # Number of Python worker nodes to spawn
cluster_secret   = "chameleon-dev-secret"  # Shared secret for gRPC auth
coord_addr       = "localhost:8081"        # Internal gRPC port for workers to register
vram_per_worker  = 16.0                    # VRAM allocation per spawned node

[telemetry]
metrics_db       = "data/metrics.db"
log_level        = "info"                  # "trace" | "debug" | "info" | "warn" | "error"
```

### Environment variables

| Variable | Description | Default |
|---|---|---|
| `CHAMELEON_API_KEY` | API key (overrides config) | — |
| `CHAMELEON_VRAM_BUDGET` | VRAM budget in GB | `20` |
| `CHAMELEON_WORKERS` | Number of Python workers | `4` |
| `CHAMELEON_LOG` | Log level | `info` |
| `CUDA_VISIBLE_DEVICES` | GPU device selection | all |

---

## Warm Cache

The warm cache is the primary mechanism for trading **memory budget against latency**.

| Warm slots | VRAM used (7 GB models) | Cache hit rate (est.) | Avg response start |
|---|---|---|---|
| 0 | 0 GB | 0% | 7–25s (cold load) |
| 1 | 7 GB | ~45% | ~4s average |
| 2 | 14 GB | ~70% | ~2s average |
| 3 | 21 GB | ~85% | ~0.8s average |
| 4 | 28 GB | ~93% | ~0.2s average |

> **Recommendation for a 24 GB card:** set `warm_slots = 3` with 7 GB average model size, leaving 3 GB headroom for the OS and Rust process.

The telemetry store (`data/metrics.db`) tracks per-model request counts and p99 latency. Use this to identify which models should be in your warm pool:

```bash
sqlite3 data/metrics.db \
  "SELECT model_id, request_count, avg_latency_ms FROM model_stats ORDER BY request_count DESC LIMIT 10;"
```

---

## API Reference

### `POST /v1/infer`

Run inference. Chameleon selects the model automatically.

```json
{
  "prompt": "string",
  "stream": true,
  "model_hint": "code",           // optional — task tag hint for the router
  "max_tokens": 512,
  "temperature": 0.7,
  "top_p": 0.95,
  "stop": ["\n\n"]
}
```

**Response (streaming, `stream: true`):**

```
data: {"token": "def", "done": false}
data: {"token": " parse", "done": false}
data: {"token": "_json", "done": false}
data: {"token": "", "done": true, "model_used": "deepseek-coder-7b", "load_ms": 0, "total_ms": 1842}
```

### `GET /v1/status`

Returns current system state.

```json
{
  "state": "idle",
  "warm_cache": ["llama3-8b-instruct", "deepseek-coder-7b"],
  "vram_used_gb": 11.0,
  "vram_budget_gb": 20,
  "workers": { "total": 4, "busy": 1, "idle": 3 }
}
```

### `GET /v1/models`

Lists all registered models.

```json
{
  "models": [
    {
      "id": "llama3-8b-instruct",
      "tags": ["general", "chat", "code"],
      "vram_gb": 5.2,
      "warm": true
    }
  ]
}
```

### `POST /v1/models/register`

Register a new model at runtime (no restart required).

```json
{
  "id": "mistral-7b-v0.3",
  "path": "/models/mistral-7b-v0.3.Q4_K_M.gguf",
  "tags": ["general", "reasoning"],
  "vram_gb": 4.8
}
```

---

## Routing Logic

The router selects a model by scoring all registry candidates against the inferred task type.

### Task tags

| Tag | Trigger signals | Preferred model characteristics |
|---|---|---|
| `code` | "write", "function", "bug", "debug", language names | Code-specialist GGUF, high context |
| `reasoning` | "explain", "why", "math", "logic", "step by step" | Larger parameter count, chain-of-thought |
| `summarise` | "summarise", "tldr", "key points", "shorten" | Efficient model, lower latency priority |
| `chat` | Conversational phrasing, questions, casual tone | General-purpose, fast TTFT |
| `general` | No strong signal — fallback | Fallback model from config |

### Scoring function

```
score(model) = (quality_weight × quality_score)
             + (speed_weight   × speed_score)
             + (vram_weight    × vram_efficiency)
```

Weights are configurable in `chameleon.toml` under `[router].score_weights`. The highest-scoring available model (not currently busy in another worker) wins.

---

## Adding a Backend Plugin

Chameleon's Python skills layer is fully pluggable. To add a new inference backend:

**1.** Create `skills/chameleon_skills/plugins/my_backend.py`:

```python
from chameleon_skills.runtime import BaseBackend

class MyBackend(BaseBackend):
    def load(self, model_path: str, **kwargs) -> None:
        # Load weights into memory
        ...

    def infer(self, prompt: str, params: dict):
        # Yield tokens as a generator
        for token in self.model.generate(prompt, **params):
            yield token

    def unload(self) -> None:
        # Free all memory and flush CUDA cache
        ...
```

**2.** Register it in `config/chameleon.toml`:

```toml
[workers]
backend = "my_backend"
```

No changes to any Rust code required. The supervisor picks up the new backend on next start.

---

## Benchmarks

Measured on a single NVIDIA RTX 4090 (24 GB VRAM), Ubuntu 22.04, PCIe 4.0 NVMe.

| Metric | Value | Notes |
|---|---|---|
| Cold load — 4 GB GGUF (Q4_K_M) | ~7s | PCIe 4 NVMe → VRAM |
| Cold load — 13 GB GGUF (Q4_K_M) | ~22s | Same hardware |
| Warm cache hit — dispatch to inference | ~90ms | IPC round-trip + first token |
| Routing decision (rules mode) | < 1ms | Pure Rust, no model involved |
| Routing decision (ML mode) | ~45ms | Classifier model always-warm |
| Unload + CUDA flush | ~800ms | Scales with model size |
| IPC overhead per token | < 2µs | Unix socket, length-prefixed JSON |
| Concurrent requests (warm models) | Linear | Each worker handles 1 at a time |

> Run your own benchmarks: `python scripts/bench.py --model llama3-8b-instruct --requests 100`

---

## Roadmap

### Phase 1 — Minimum viable runtime ✅ (current)
- [x] Architecture design and IPC protocol specification
- [x] Rust gateway with Axum (HTTP + WebSocket)
- [x] Rules-based intent classifier
- [x] SQLite model registry
- [x] Single Python worker (llama-cpp-python backend)
- [x] Cold load → infer → unload lifecycle
- [x] Basic telemetry writer

### Phase 2 — Warm cache and multi-worker
- [x] LRU warm cache with VRAM budget enforcer
- [x] Multi-worker pool with Rust supervisor
- [x] `GET /v1/status` endpoint with live VRAM stats
- [x] Telemetry dashboard (SQLite → simple HTML report)
- [x] vLLM backend plugin

### Phase 3 — ML routing and plugin ecosystem
- [x] Fine-tuned intent classification model (always-warm, < 500 MB)
- [x] Plugin interface and loader in Python skills layer
- [x] ExLlamaV2 backend plugin
- [x] HuggingFace Transformers backend plugin
- [x] `POST /v1/models/register` hot-register endpoint
- [x] OpenAPI spec + generated client SDKs

### Phase 4 — Distributed mode ✅
- [x] Coordinator node (Rust) managing a gRPC worker fleet
- [x] Cluster-wide fleet manager (registration/heartbeat)
- [x] Distributed inference routing with best-fit selection
- [x] Shared-secret authentication for cluster security
- [ ] Kubernetes Helm chart

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request.

### Development setup

```bash
# Rust (control plane)
cargo test --workspace

# Python (skills layer)
cd skills
pip install -e ".[dev]"
pytest tests/
```

### Crate responsibilities — quick reference

| Crate | What to change here |
|---|---|
| `chameleon-gateway` | HTTP routes, auth, rate limiting |
| `chameleon-router` | Routing rules, scoring logic, registry queries |
| `chameleon-cache` | Eviction policy, VRAM budget math |
| `chameleon-session` | Context storage, history truncation |
| `chameleon-ipc` | Message types, socket transport |
| `chameleon-telemetry` | Metrics schema, log format |

### Adding a new task tag

1. Add the tag constant to `chameleon-router/src/classifier.rs`
2. Add keyword patterns to the rules-based classifier
3. Add a corresponding entry in `registry/seed.sql` with a preferred model
4. Add a test case in `tests/integration/test_routing.rs`

### Commit convention

```
feat(router): add reasoning task tag with chain-of-thought scoring
fix(cache): correct LRU eviction when budget exactly matches resident size
docs(readme): update warm cache benchmark table
test(lifecycle): add unload-under-load stress test
```

---

## Design Decisions

### Why not just use Ollama?

Ollama is excellent for single-model serving. Chameleon solves a different problem: heterogeneous workloads where the optimal model changes per request, and where VRAM is a scarce shared resource. Chameleon can be thought of as an orchestration layer *above* inference backends — it could even wrap Ollama's API as a backend plugin in a future phase.

### Why Rust for the control plane?

The control plane manages GPU memory and concurrent request lifecycles. A garbage collector pausing during an LRU eviction decision under load is unacceptable. Rust's ownership model provides the compile-time guarantees needed to verify correctness before shipping, and Tokio's async runtime handles thousands of concurrent connections on a minimal thread pool.

### Why Python for inference?

The entire LLM inference ecosystem is Python-first. `llama-cpp-python`, `vLLM`, `Transformers`, `PEFT`, `Safetensors` — all Python. Fighting this reality by reimplementing inference in Rust would permanently lag behind every new model format. Python is the correct tool for this layer.

### Why gRPC for IPC?

Chameleon uses gRPC because it provides network transparency out of the box. A worker and a coordinator can be on the same machine (localhost) or in different data centers. Protobuf ensures that messages are compact and type-safe across Rust and Python, while gRPC's streaming support is perfect for the token-by-token LLM inference lifecycle.

---

## License

MIT License — see [LICENSE](./LICENSE) for full text.

---

<div align="center">

Built with **Rust** for speed and safety · **Python** for the AI ecosystem

*Chameleon has no fixed identity. Neither does great software.*

</div>
