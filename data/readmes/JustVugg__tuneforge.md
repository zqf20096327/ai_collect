<p align="center">
  <img src="tuneforge.png" alt="TuneForge Logo" width="500"/>
</p>

**An MCP server that lets coding agents generate datasets, fine-tune, and evaluate LLMs — without leaving the chat.**

TuneForge exposes a small, sharp set of tools over the [Model Context Protocol](https://modelcontextprotocol.io/) so any MCP-capable agent (Claude Desktop, Claude Code, Cursor, Windsurf, Zed, Continue, …) can:

- generate SFT datasets from a product description and optional source text, with LLM-judge quality filtering
- run LoRA SFT on any Hugging Face causal LM
- continue with policy-gradient RL using an Ollama-hosted teacher as the judge
- merge adapters, evaluate models on held-out data, poll job status

Long-running operations are scheduled as **background jobs** with SQLite-backed state, so a tool call returns immediately with a `job_id` and the agent polls for progress. The MCP transport never blocks.

---

## Why

Fine-tuning is commoditized. Unsloth, TRL, Axolotl, Together, Modal, Replicate all exist. What is *not* commoditized: making the whole loop — data → training → eval → merge → redeploy — drivable from inside the agent you already talk to.

TuneForge is that loop, packaged as an MCP server. You say "fine-tune a small model on this FAQ" and your agent orchestrates the rest.

---

## Quickstart

```bash
pip install -e '.[train]'        # all extras
# or, minimal (dataset gen + MCP server without training deps):
pip install -e .

cp .env.example .env
# edit .env: point TUNEFORGE_OLLAMA_BASE_URL at your Ollama instance

ollama pull llama3.1:8b           # the teacher used for judging
tuneforge                         # starts the MCP server over stdio
```

### Wire it into Claude Desktop

`~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "tuneforge": {
      "command": "tuneforge",
      "env": {
        "TUNEFORGE_OLLAMA_BASE_URL": "http://127.0.0.1:11434",
        "TUNEFORGE_TEACHER_MODEL": "llama3.1:8b",
        "TUNEFORGE_WORKSPACE": "/absolute/path/to/workspace"
      }
    }
  }
}
```

See [`examples/claude_desktop_config.json`](examples/claude_desktop_config.json) and [`examples/agent_session.md`](examples/agent_session.md).

---

## Tools exposed

| Tool               | Purpose                                                                 | Blocking? |
|--------------------|-------------------------------------------------------------------------|-----------|
| `generate_dataset` | Synthetic instruction dataset from a description (+ optional source)    | Async     |
| `train_sft`        | LoRA SFT on a Hugging Face base model                                   | Async     |
| `train_rl`         | REINFORCE-style update on top of an SFT adapter, using an LLM judge     | Async     |
| `merge_adapter`    | Merge a LoRA adapter into the base weights                              | Async     |
| `evaluate_model`   | Grade a base-model (optionally + adapter) on a JSON eval set            | Async     |
| `list_jobs`        | List recent jobs by kind / status                                       | Sync      |
| `get_job_status`   | Poll a single job                                                       | Sync      |
| `cancel_job`       | Cooperatively cancel a running job                                      | Sync      |
| `wait_for_job`     | Block until a job reaches a terminal state (or timeout)                 | Sync      |
| `estimate_vram`    | Pre-flight VRAM check for a base model + LoRA config                    | Sync      |
| `list_ollama_models` | Enumerate locally available Ollama models                             | Sync      |
| `health`           | Workspace + Ollama reachability + config snapshot                       | Sync      |

Each tool's schema is published via `list_tools` on server startup; agents auto-discover argument shapes.

### Cancellation, VRAM safety, and streaming

- **`cancel_job`** sets a flag the worker checks at every progress tick; long jobs exit cleanly within a second of the request.
- **`estimate_vram`** and the SFT pre-flight read the model's safetensors metadata from the Hugging Face Hub and compare against `torch.cuda.mem_get_info()`. A doomed run is rejected before weights download.
- **`wait_for_job`** lets agents await a final state without busy-polling. For tools that prefer streaming, use it with a short `poll_interval_sec`; the MCP transport stays unblocked because the server uses `asyncio.sleep` between polls.

## Direct CLI

The same operations are exposed as a Typer CLI for scripts, CI, and demos. It shares the SQLite job store with the MCP server.

```bash
tuneforge-cli health
tuneforge-cli estimate-vram --base-model meta-llama/Llama-3.2-1B-Instruct
tuneforge-cli generate-dataset --description "HR support bot" --target 200
tuneforge-cli train-sft --base-model meta-llama/Llama-3.2-1B-Instruct --dataset workspace/datasets/.../foo.json
tuneforge-cli list-jobs
tuneforge-cli cancel <job_id>
```

A runnable end-to-end demo lives at [`examples/demo.sh`](examples/demo.sh). To capture a GIF of the agent flow, record `examples/agent_session.md` being executed in Claude Desktop with [`vhs`](https://github.com/charmbracelet/vhs) or `peek` and place the file at `docs/demo.gif`.

---

## Workflow example (told from the agent's side)

> *You:* "Build me a support bot from the attached FAQ."
>
> *Agent calls `generate_dataset`* → `{"job_id": "b3e1…", "status": "queued"}`
>
> *Agent polls `get_job_status`* → `progress: 0.42, message: "collected 84/200"`
>
> *Agent calls `train_sft`* on the resulting dataset → new `job_id`
>
> *Agent calls `evaluate_model`* on a 20-sample held-out set → side-by-side base-vs-adapter scores

Nothing leaves your machine unless you point the base model at a remote HF repo or the judge at an external endpoint.

---

## Architecture

```
tuneforge/
├── server.py         # MCP server + tool routing
├── jobs.py           # ThreadPool-backed job scheduler
├── state.py          # SQLite persistence (WAL-mode)
├── dataset.py        # Seed→batch→judge→filter generation loop
├── eval.py           # LLM-judge evaluation harness
├── training/
│   ├── sft.py        # LoRA SFT (Transformers + PEFT + bitsandbytes)
│   ├── rl.py         # Policy-gradient w/ Ollama-judge reward
│   ├── merge.py      # Adapter → full weights merge
│   └── types.py      # SFTConfig / RLConfig / MergeConfig
└── providers/
    └── ollama.py     # Thin HTTP client
```

Key design decisions:

- **Jobs, not streams.** Training takes minutes to hours; MCP stdio isn't the right channel for a stream. We return a `job_id` instantly and the agent polls. Jobs are crash-resilient — on restart any `running` or `queued` job is marked failed so the agent sees a clear state.
- **Ollama by default for the judge.** Local, cheap, zero API key. You can swap in any OpenAI-compatible endpoint by replacing the provider module.
- **4-bit by default.** Enables 7B training on a 16 GB consumer GPU. Toggle `use_4bit: false` when you have the VRAM.
- **No hidden state.** Every run writes its config, metrics, and dataset slice next to the adapter so runs are reproducible and auditable.

---

## Configuration

All knobs via `.env` (see `.env.example`):

| Variable                         | Default                          | Meaning                                        |
|----------------------------------|----------------------------------|------------------------------------------------|
| `TUNEFORGE_OLLAMA_BASE_URL`      | `http://127.0.0.1:11434`         | Where Ollama listens                           |
| `TUNEFORGE_TEACHER_MODEL`        | `llama3.1:8b`                    | Default generator / judge model                |
| `TUNEFORGE_WORKSPACE`            | `./tuneforge_workspace`          | Root for datasets, runs, models, SQLite        |
| `HF_TOKEN`                       | *(unset)*                        | For private/gated HF models                    |
| `TUNEFORGE_MAX_CONCURRENT_JOBS`  | `1`                              | How many long-running jobs run in parallel     |
| `TUNEFORGE_LOG_LEVEL`            | `INFO`                           | Log verbosity (written to `workspace/…log`)    |

---

## Installing only what you need

```bash
pip install -e .              # MCP server + dataset generation
pip install -e '.[train]'     # + torch, transformers, peft, bitsandbytes
pip install -e '.[dev]'       # + pytest, ruff
```

Training extras are optional because you may only want dataset generation on machines without a GPU.

---

## Development

```bash
pip install -e '.[dev]'
pytest                                  # runs the test suite
ruff check tuneforge tests              # lint
```

Tests cover state persistence, job lifecycle, and JSON parsing. Training modules are exercised via smoke runs in CI with a tiny model.

---

## Limits and non-goals

- **Not a platform.** No multi-tenant auth, no UI, no cloud queue. Runs locally next to your agent.
- **Not a replacement for Unsloth/TRL.** The trainers are correct and useful, but Unsloth wins on throughput for standalone batch training. TuneForge's value is the MCP integration, not raw tok/s.
- **Needs a teacher.** Dataset generation and RL both call an Ollama model as teacher/judge. Tiny teachers produce tiny datasets — use 7B+ if you want quality.

---

## License

MIT. See [LICENSE](LICENSE).
