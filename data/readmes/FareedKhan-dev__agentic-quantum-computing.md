# Agentic Quantum Computing: Quantum Anomaly Detection Engine

A local, end to end pipeline that brings together three pieces in one system:

1. **Quantum machine learning.** A PennyLane quantum kernel anomaly detector that runs on CPU (`lightning.qubit` / `default.qubit`) or on a local CUDA GPU (`lightning.gpu`, cuQuantum).
2. **A multi agent system.** A LangGraph agent that plans a run, executes the pipeline, evaluates the result, and writes a report.
3. **A local open weight LLM.** Qwen3-14B run on your own machine (no external API), driving the engine through tool calls and explaining the results in plain English.

The same engine detects anomalies across three very different domains, network intrusion (KDD), particle physics (the LHC Olympics dataset), and financial fraud, all on your local machine.

> **Honesty first.** A simulated quantum kernel running on a CPU or GPU is, by construction, a constrained classical model. This project makes no quantum supremacy claim. It is a rigorous, reproducible benchmark with strong classical baselines. The genuine, reproducible quantum result is the entanglement effect described below.

## Table of contents
- [Key results](#key-results)
- [How it works](#how-it-works)
- [Repository layout](#repository-layout)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quickstart on CPU](#quickstart-on-cpu)
- [Running on a local GPU](#running-on-a-local-gpu)
- [The local LLM agent](#the-local-llm-agent)
- [Configuration](#configuration)
- [Datasets](#datasets)
- [Reproducing the figures](#reproducing-the-figures)
- [Testing](#testing)
- [Honest framing](#honest-framing)
- [License](#license)

## Key results

Quantum kernel versus classical baselines, per domain (8 qubits, ROC-AUC):

| Domain | Quantum kernel | Best classical | Quantum win? |
|--------|---------------|----------------|--------------|
| Cybersecurity (KDD intrusion) | **0.99** | 0.96 | yes |
| Physics (LHC dijets) | 0.74 | 0.72 | marginal |
| Finance (credit card fraud) | 0.85 | 0.88 | competitive |

The headline finding is that **entanglement helps in every domain**. Comparing the entangled kernel against an identical no entanglement ablation gives a gain of **+0.15, +0.12, and +0.16 AUC** respectively. This is a genuine quantum mechanical effect doing measurable work.

![Entanglement helps in every domain](results/teaching/plots/entanglement_ablation.png)

The local LLM agent calls the quantum engine and judges the result on its own:
```
ROUND 1  the model emits a tool call:  run_pipeline(config_path=...)
TOOL     the PennyLane quantum kernel runs and returns the metrics
ROUND 2  the model: "Quantum AUC 0.9916 > classical 0.9580, so quantum WON. But a
         simulated quantum kernel is a constrained classical model and may not
         generalize to real quantum hardware."
```

The quantum feature map (RY data encoding plus CNOT entanglement, repeated twice):

![Quantum feature map](results/teaching/plots/circuit_dense_8q.png)

More figures, per sample traces, and a teaching guide are in [`results/teaching/`](results/teaching). The full write up is in [`REPORT.md`](REPORT.md).

## How it works

```
DomainAdapter.ingest/split  ->  Encoder (PCA or autoencoder)  ->  latent Z (about 8 dims)
   ->  QuantumKernel.gram  (PennyLane fidelity overlap)
   ->  Scorer (quantum One-Class SVM or quantum k-means)  ->  anomaly scores
   ->  metrics (ROC-AUC, average precision)  vs  classical baselines on the SAME Z
   ->  AnomalyEngine writes a reproducible run record (manifest, metrics, scores)
```
A local LLM agent (LangGraph) drives the engine through `@tool` functions, then evaluates and reports.

Two conventions hold throughout: labels are `0 = normal, 1 = anomaly`, and an anomaly score is always *higher = more anomalous*. One invariant is enforced: `encoder.latent_dim == quantum.n_qubits` (each latent value is encoded on exactly one qubit). The quantum backend is config driven, so the same code runs on a laptop CPU or a CUDA GPU.

## Repository layout

```
agentic-quantum-computing/
├── README.md                # this file
├── REPORT.md                # consolidated results report
├── PROJECT_STRUCTURE.md     # annotated, file by file guide
├── LICENSE                  # MIT
├── pyproject.toml           # package definition + optional extras
├── src/qadx/                # the package
│   ├── engine.py            #   AnomalyEngine: wires the whole pipeline + writes run records
│   ├── config.py            #   typed config (pydantic) + YAML loading
│   ├── interfaces.py        #   the DomainAdapter / Encoder / KernelBackend / Scorer contracts
│   ├── registry.py          #   name -> class registries; bootstrap.py populates them
│   ├── quantum/             #   feature maps, device, fidelity kernel, quantum OC-SVM / k-means
│   ├── adapters/            #   domain data loaders (fraud, kdd, lhc, sanity sets)
│   ├── encoders/            #   PCA and autoencoder compressors
│   ├── baselines/           #   classical opponents (RBF OC-SVM, IsolationForest, AE reconstruction)
│   ├── metrics/             #   scoring + the quantum-vs-classical comparison + the sweep driver
│   └── agents/              #   the LangGraph agent, local LLM client, tools, prompts, RAG
├── scripts/                 # run a sweep, run the LLM agent, the per sample demo, make plots
├── configs/                 # YAML run and scenario configs
├── tests/                   # pytest suite (kernel correctness, engine smoke, adapters, metrics)
└── results/                 # real run artifacts and the teaching pack
```
See [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md) for the purpose of every file.

## Requirements

- Python 3.11 or 3.12.
- A CPU is enough to run, test, and reproduce the full pipeline (the quantum circuits are simulated).
- A local NVIDIA CUDA GPU is optional and only needed for the `lightning.gpu` backend and for serving the local LLM. The results in this repository were produced on a local CUDA GPU; nothing here depends on any cloud provider.

## Installation

```bash
git clone https://github.com/FareedKhan-dev/agentic-quantum-computing.git
cd agentic-quantum-computing

python -m venv .venv
# Windows:
. .venv/Scripts/activate
# Linux / macOS:
# source .venv/bin/activate

pip install -e ".[local]"
```

Optional dependency groups (install only what you need):

| Extra | Adds | Use it for |
|-------|------|-----------|
| `local` | xgboost, torch (CPU), uproot, awkward, h5py, pytest | everything that runs on a laptop |
| `gpu` | pennylane-lightning-gpu, custatevec-cu12, catalyst | the `lightning.gpu` backend on a CUDA machine |
| `dl` | torch | the autoencoder encoders and the transformers LLM agent |
| `agents` | langgraph, langchain, llama-index, openai | the LLM agent layer |
| `physics` | uproot, awkward, h5py, tables, fastjet | the LHC jet clustering path |

## Quickstart on CPU

```bash
pytest -q                                         # validate the engine and the quantum kernel
qadx run --config configs/domain_fraud.yaml       # one end to end run on CPU (default.qubit)
```
The run prints a metrics table (quantum vs classical) and writes a reproducible record under `runs/`.

## Running on a local GPU

On a Linux machine with an NVIDIA CUDA GPU:

```bash
pip install -e ".[gpu,dl]"                         # PennyLane lightning.gpu + cuQuantum + torch
python scripts/smoke_lightning_gpu.py              # checks the GPU kernel equals the CPU kernel to < 1e-6
```
Then point any run at the GPU by setting the backend in a config (`quantum.backend: lightning.gpu`), or run the quantum win sweep:

```bash
python scripts/run_gpu_sweep.py --domain kdd --backend lightning.gpu \
    --qubits 4,8,12,16 --maps dense,dense_no_ent --out data/sweep_kdd.csv
```
This sweep is the scientific core: it records quantum vs classical AUC and the entanglement on/off ablation across qubit counts.

## The local LLM agent

Qwen3-14B runs on your own GPU and drives the engine. The simplest, most robust path loads the model in process with transformers:

```bash
pip install -e ".[agents,dl]"                      # langgraph/langchain + transformers
python scripts/run_llm_agent_hf.py --domain kdd --qubits 8
```
The agent asks the model to call `run_pipeline`, executes the quantum kernel, then asks the model to read the metrics and give an honest verdict.

You can also serve the model through any OpenAI compatible local server (for example vLLM or Ollama) and point the agent at it via `configs/serving_vllm.yaml` and `scripts/run_llm_agent.py`.

For a fully transparent, per sample walkthrough (raw features -> latent -> quantum score -> flag/ok verdict) plus a plain English explanation from the model:

```bash
python scripts/sample_demo.py --domain kdd --with-llm
```

## Configuration

Every run merges a YAML on top of `configs/base.yaml`, for example:
```yaml
quantum: { backend: lightning.gpu, n_qubits: 8, feature_map: dense, reps: 2, scorer: qsvm }
encoder: { kind: pca, latent_dim: 8 }
baselines: [rbf_ocsvm, isolation_forest]
```
Ready made scenarios live in `configs/`: `domain_fraud.yaml`, `domain_lhc.yaml`, and `sweep_quantum_win.yaml`.

## Datasets

- **KDD Cup '99** (network intrusion), fetched via `sklearn.datasets.fetch_kddcup99`.
- **LHC Olympics 2020** (dijet new physics search), Zenodo record 2629073, jets clustered with `fastjet` (see `scripts/lhc_prep.py`).
- **ULB credit card fraud**, fetched via OpenML (`data_id=1597`).
- Sanity sets: breast cancer and synthetic, offline, for fast tests.

`scripts/download_data.py` helps fetch them into a local `data/` directory.

## Reproducing the figures

```bash
python scripts/make_teaching_plots.py              # regenerates the 8 figures in results/teaching/plots
```

## Testing

```bash
pytest -q
```
The suite validates the fidelity kernel (symmetric, positive semi-definite, unit diagonal, and `default.qubit` equals `lightning.qubit`), the adapters, a full engine smoke run, and the metrics.

## Honest framing

A `lightning.gpu` simulated quantum kernel is a constrained classical model, so there is no runtime or accuracy supremacy claim. The defensible contributions are a reproducible, agentically orchestrated benchmark with strong classical baselines, an automated feature map and circuit search, and the reproducible entanglement effect. The quantum kernel does win in one regime (KDD at 8 qubits) and is competitive elsewhere, but classical methods remain the pragmatic production choice today.

## License

MIT. See [`LICENSE`](LICENSE).
