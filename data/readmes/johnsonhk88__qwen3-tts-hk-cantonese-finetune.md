# Qwen3-TTS Fine-Tuning for Hong Kong Cantonese 🇭🇰

Fine-tune **Qwen3-TTS** (0.6B or 1.7B Base) for Hong Kong Cantonese speech: LoRA or full FT, single- or multi-speaker, evaluation, and a voice-clone UI.

**Rule:** run every command from the **repo root**.  
**Code** is in `src/qwen3_tts_ft/` (grouped by function).  
**Data, models, checkpoints** are in `Dataset-Cantonese-Training/` (no Python there).

```bash
./scripts/run.sh <stage> --config configs/experiments/lora_single.yaml
```

Stages: `cluster` → `prepare` → `train` → `evaluate` → `serve`  
Shortcut: `./scripts/run.sh all` = prepare + train + evaluate.

---

## 1. Project structure

```text
qwen3-tts-hk-cantonese-finetune/
├── scripts/
│   ├── run.sh                         # pipeline runner (the only entrypoint you need)
│   ├── run-full-lora-1epoch-bs6.sh    # known 1-epoch LoRA recipe
│   └── download-dataset.sh            # optional HF corpus clone
├── configs/
│   ├── default.yaml                   # shared paths + hyperparameters
│   └── experiments/
│       ├── lora_single.yaml           # start here (8–12 GB GPU)
│       ├── lora_multi.yaml            # many speakers
│       └── full_ft.yaml               # full fine-tune (16+ GB)
├── src/qwen3_tts_ft/                  # installable package
│   ├── data/                          # cluster, duration, tokenize, split, dataset
│   ├── train/                         # shared loop, LoRA, speaker export
│   ├── eval/                          # WER/CER, speaker sim, UTMOS
│   ├── serve/                         # Gradio + CLI voice clone
│   ├── tracking/                      # MLflow
│   └── config.py                      # YAML load + CLI overrides
├── tests/                             # CPU unit tests
├── Dataset-Cantonese-Training/        # DATA ONLY
│   ├── audio/                         # wavs
│   ├── train_raw.jsonl                # labels
│   ├── train_prepared.jsonl           # after prepare (gitignored)
│   ├── Qwen3-TTS-*/  Tokenizer/       # downloaded models
│   └── output_*/  evaluation_results*/
├── monitoring/                        # Prometheus + Grafana GPU metrics
│   ├── gpu_exporter.py                # NVML → :9401/metrics
│   ├── docker-compose.yml             # Prometheus :9090, Grafana :3000
│   └── grafana/dashboards/gpu.json
├── notebooks/
├── pyproject.toml
├── requirements.txt
└── readme.md
```

| Goal | Where |
|---|---|
| Run a stage | `./scripts/run.sh …` |
| Change LR / epochs / paths | `configs/experiments/*.yaml` |
| Change algorithm | `src/qwen3_tts_ft/{data,train,eval,serve}/` |
| Add wavs or JSONL | `Dataset-Cantonese-Training/` |

`scripts/run.sh` only calls:

```text
python -m qwen3_tts_ft.data.cluster
python -m qwen3_tts_ft.data.prepare
python -m qwen3_tts_ft.train
python -m qwen3_tts_ft.eval
python -m qwen3_tts_ft.serve
```

No Python DAG. The same `-m` commands can later be Kubeflow / Kubernetes container commands.

### Function groups (`src/qwen3_tts_ft/`)

| Package | Responsibility |
|---|---|
| `data/` | JSONL I/O, 5–30s filter, speaker clustering, `audio_codes`, train/eval split, `TTSDataset` |
| `train/` | Accelerate loop, LoRA wrap/merge, single- or multi-speaker export |
| `eval/` | Whisper ASR, mixed Canto–English WER/CER, ECAPA similarity, UTMOS |
| `serve/` | Model cache, Gradio UI, CLI clone |
| `tracking/` | MLflow experiment / metrics / artifacts |
| `config.py` | Merge `default.yaml` + experiment YAML + CLI flags |

---

## 2. Requirements

| Method | GPU VRAM | Model | Notes |
|---|---|---|---|
| **LoRA (recommended)** | **8–12 GB** | 0.6B-Base | Start here |
| Full fine-tune | 16–24+ GB | 0.6B or 1.7B | Lower LR |

- NVIDIA GPU, CUDA 12.x
- Python **3.11 or 3.12**
- FFmpeg
- ~25 GB free disk

---

## 3. Step-by-step (single-speaker LoRA)

This is the default path. Use it the first time.

### Step 1 — Clone

```bash
git clone https://github.com/johnsonhk88/qwen3-tts-hk-cantonese-finetune.git
cd qwen3-tts-hk-cantonese-finetune
```

### Step 2 — Install

```bash
sudo apt update && sudo apt install -y ffmpeg
# no sudo: put a static ffmpeg/ffprobe on PATH or in "$VIRTUAL_ENV/bin/"

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -e .
pip install -r requirements.txt
```

Optional Flash Attention-2 (Ampere or newer GPU):

```bash
./flash-attent-install.sh
```

Then train with `--attn_implementation flash_attention_2`, or set `train.attn_implementation` in YAML.

Sanity check (CPU, no GPU):

```bash
python -m unittest discover -s tests -v
```

### Step 3 — Download base models

Configs look for these folders under `Dataset-Cantonese-Training/`:

```bash
cd Dataset-Cantonese-Training

huggingface-cli download Qwen/Qwen3-TTS-12Hz-0.6B-Base --local-dir Qwen3-TTS-12Hz-0.6B-Base
huggingface-cli download Qwen/Qwen3-TTS-Tokenizer-12Hz --local-dir Qwen3-TTS-Tokenizer-12Hz

# optional: larger TTS
# huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-Base --local-dir Qwen3-TTS-12Hz-1.7B-Base

# optional: only needed for Gradio voice-clone UI
# huggingface-cli download Qwen/Qwen3-ASR-0.6B --local-dir Qwen3-ASR-0.6B

cd ..
```

### Step 4 — Prepare training data

1. Put clean **mono WAV** clips in `Dataset-Cantonese-Training/audio/` (target **5–30 seconds**; prepare drops the rest).
2. Write `Dataset-Cantonese-Training/train_raw.jsonl` (one JSON object per line).

Single-speaker: **same** `ref_audio` on every line.

```jsonl
{"audio":"audio/utt0001.wav","text":"喂，你食咗飯未呀？","ref_audio":"audio/ref.wav"}
{"audio":"audio/utt0002.wav","text":"今晚想唔想去打邊爐？","ref_audio":"audio/ref.wav"}
```

Paths are relative to `Dataset-Cantonese-Training/` (`data.root`). JSONL field notes: `Dataset-Cantonese-Training/README.md`.

3. Encode `audio_codes` and split train/eval:

```bash
./scripts/run.sh prepare --config configs/experiments/lora_single.yaml
```

Writes:

- `Dataset-Cantonese-Training/train_prepared.jsonl`
- `Dataset-Cantonese-Training/eval_prepared.jsonl`
- `Dataset-Cantonese-Training/train_prepared_audio_lengths.csv`

If VRAM is tight during tokenize, pass `--batch_size 2` (YAML default is 4).

### Step 5 — Start MLflow (recommended)

Default URI is `http://localhost:5000`. In a **second terminal**:

```bash
mlflow ui --port 5000
```

Open http://localhost:5000 . Override with `export MLFLOW_TRACKING_URI=…` or `run.tracking_uri` in YAML.

### Step 6 — Train

```bash
./scripts/run.sh train --config configs/experiments/lora_single.yaml
```

Outputs under `Dataset-Cantonese-Training/output_hk_cantonese_lora/`:

- `checkpoint-epoch-0`, `checkpoint-epoch-1`, …
- **`final_merged/`** ← use this for inference

Override YAML from the CLI (flags win):

```bash
./scripts/run.sh train --config configs/experiments/lora_single.yaml \
  --num_epochs 1 \
  --batch_size 1 \
  --gradient_accumulation_steps 6 \
  --lora_rank 8
```

Known 1-epoch recipe: `./scripts/run-full-lora-1epoch-bs6.sh`

### Step 7 — Evaluate

```bash
./scripts/run.sh evaluate --config configs/experiments/lora_single.yaml
```

Metrics vs `eval_prepared.jsonl`:

- WER / CER (Cantonese + English code-mixing)
- Speaker similarity (ECAPA-TDNN)
- Audio quality (UTMOS)

Writes `results.csv`, `summary.json`, and `sample_XXX.wav` under  
`Dataset-Cantonese-Training/evaluation_results_lora_single/`.

Compare to the base model:

```bash
./scripts/run.sh evaluate --config configs/experiments/lora_single.yaml \
  --checkpoint_dir Dataset-Cantonese-Training/Qwen3-TTS-12Hz-0.6B-Base \
  --output_dir Dataset-Cantonese-Training/evaluation_results_original
```

### Step 8 — Inference (fine-tuned custom voice)

From the repo root, load **`final_merged`**:

```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Dataset-Cantonese-Training/output_hk_cantonese_lora/final_merged",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="sdpa",
)

wavs, sr = model.generate_custom_voice(
    text="喂，你食咗飯未呀？今晚想唔想去打邊爐？",
    speaker="hk_cantonese_speaker",
)
sf.write("output_hk.wav", wavs[0], sr)
```

### Step 9 — Voice-clone UI (optional)

Gradio clones **any reference recording** (ASR → TTS). Separate from `generate_custom_voice`.

```bash
./scripts/run.sh serve --config configs/experiments/lora_single.yaml --port 7860
```

Open http://localhost:7860 and pick a TTS path, for example:

- `Dataset-Cantonese-Training/Qwen3-TTS-12Hz-0.6B-Base`
- `Dataset-Cantonese-Training/output_hk_cantonese_lora/final_merged`

Instruct / multi-line dialogue UI:

```bash
./scripts/run.sh serve --config configs/experiments/lora_single.yaml --mode app_adv
```

CLI (no UI):

```bash
./scripts/run.sh serve --mode clone \
  --reference_audio /path/to/ref.wav \
  --generate_text "喂，你食咗飯未呀？" \
  --qwen3_tts_model Dataset-Cantonese-Training/Qwen3-TTS-12Hz-0.6B-Base \
  --qwen3_asr_model Dataset-Cantonese-Training/Qwen3-ASR-0.6B \
  --output_path cloned_voice.wav
```

### One-shot (steps 4 + 6 + 7)

After models and `train_raw.jsonl` exist:

```bash
./scripts/run.sh all --config configs/experiments/lora_single.yaml
```

---

## 4. Other recipes

Same steps; change only the config (and data).

### Multi-speaker LoRA

Needs `speaker_id` on **every** JSONL line, and one `ref_audio` **per** speaker.

```jsonl
{"audio":"audio/40.wav","text":"喂，你食咗飯未呀？","ref_audio":"audio/40.wav","speaker_id":"spk_115"}
{"audio":"audio/6858.wav","text":"今晚想唔想去打邊爐？","ref_audio":"audio/5612.wav","speaker_id":"spk_083"}
```

If wavs are numbered (`audio/0.wav`, `audio/1.wav`, …) and you have parquet `train-00000-of-00001.parquet` with a `sentence` column:

```bash
./scripts/run.sh cluster --config configs/experiments/lora_multi.yaml
```

That writes `train_raw.jsonl` with `speaker_id` + matched `ref_audio`. Then:

```bash
./scripts/run.sh prepare  --config configs/experiments/lora_multi.yaml
./scripts/run.sh train    --config configs/experiments/lora_multi.yaml
./scripts/run.sh evaluate --config configs/experiments/lora_multi.yaml
```

Export: one checkpoint, slots from `3000` in sorted `speaker_id` order, embeddings from each speaker’s first `ref_audio`.  
Use `Dataset-Cantonese-Training/output_hk_cantonese_multi_lora/final_merged`.

```python
print(sorted(model.get_supported_speakers()))  # e.g. spk_021, spk_083
wavs, sr = model.generate_custom_voice(text="喂，你食咗飯未呀？", speaker="spk_021")
```

### Full fine-tune (16+ GB)

```bash
./scripts/run.sh prepare --config configs/experiments/full_ft.yaml
./scripts/run.sh train   --config configs/experiments/full_ft.yaml
./scripts/run.sh evaluate --config configs/experiments/full_ft.yaml
```

Checkpoints: `Dataset-Cantonese-Training/output_hk_cantonese/checkpoint-epoch-*` (no `final_merged`).  
Eval YAML points at `checkpoint-epoch-7` (last of 8 epochs).

---

## 5. How to change settings

Edit `configs/experiments/lora_single.yaml` (it overlays `configs/default.yaml`):

```yaml
train:
  method: lora          # lora | full
  lr: 2.0e-4
  num_epochs: 10
  batch_size: 1
  gradient_accumulation_steps: 8
  lora_rank: 8
```

Or pass flags on `./scripts/run.sh train` — flags override YAML.

Useful ranges:

- LoRA lr: `1e-4` – `3e-4`
- Full FT lr: `2e-6` – `2e-5`
- `batch_size`: 1–4
- `num_epochs`: 3–10

Omit `--config` and `run.sh` uses `configs/experiments/lora_single.yaml` (`CONFIG` env can change that).

---

## 6. HK Cantonese notes

- Native speakers, clean 5–30s mono WAVs, natural slang
- Single-speaker: one fixed `ref_audio`
- Multi-speaker: one `ref_audio` per `speaker_id`
- Start with LoRA + 0.6B-Base
- Qwen3-TTS language for Cantonese is `chinese` (the UI maps “Cantonese” → `chinese`)

---

## 7. GPU monitoring (Prometheus + Grafana)

Run this on the **Linux GPU machine** (not macOS). It does not change training code: NVML/DCGM read the driver while `prepare` / `train` / `evaluate` / `serve` run.

### Start

**Terminal A — exporter** (every ~2s: util %, VRAM, temp, power):

```bash
pip install -r monitoring/requirements.txt
python monitoring/gpu_exporter.py          # http://localhost:9401/metrics
```

**Terminal B — Prometheus + Grafana:**

```bash
docker compose -f monitoring/docker-compose.yml up -d
```

| UI | URL | Login |
|---|---|---|
| Grafana | http://localhost:3000 | `admin` / `admin` |
| Prometheus | http://localhost:9090 | — |
| NVML metrics | http://localhost:9401/metrics | — |

Grafana auto-loads **GPU → NVIDIA GPU (Qwen3-TTS train box)**. Watch VRAM during LoRA (8–12 GB cards) and SM util during `train`.

Optional [DCGM](https://github.com/NVIDIA/dcgm-exporter) (NVIDIA Container Toolkit required):

```bash
docker compose -f monitoring/docker-compose.yml --profile dcgm up -d
```

Stop:

```bash
docker compose -f monitoring/docker-compose.yml down
# Ctrl+C the gpu_exporter.py process
```

On Kubernetes later: DaemonSet DCGM + Prometheus `ServiceMonitor` + the same Grafana dashboard (see §8).

---

## 8. MLOps today vs full cluster MLOps

This repo is **local MLOps**: one GPU box, YAML experiments, MLflow, stages as CLIs, GPU dashboards. The layout is so **Kubeflow / Kubernetes can reuse the same commands**. It is not a cluster yet.

### What you have now (local MLOps)

| Piece | How |
|---|---|
| Pipeline stages | `./scripts/run.sh` → `cluster` / `prepare` / `train` / `evaluate` / `serve` |
| Config vs code | `configs/default.yaml` + `configs/experiments/*.yaml` |
| Function groups | `src/qwen3_tts_ft/{data,train,eval,serve,tracking}` |
| Experiment tracking | MLflow |
| GPU hardware metrics | `monitoring/` Prometheus + Grafana |
| Data vs code | `Dataset-Cantonese-Training/` is data only |
| Reproducible entrypoints | `python -m qwen3_tts_ft.train --config …` |
| CPU checks | `python -m unittest discover -s tests` |

`scripts/run.sh` is a **local dispatcher**, not a cluster scheduler. There is no Python DAG (`pipeline.run`): Kubeflow Pipelines should own stage order on the cluster.

### What is still missing for full MLOps

| Gap | Why it matters |
|---|---|
| **Docker images** | K8s/Kubeflow run containers, not a laptop venv |
| **`kfp/` pipeline** | Cluster DAG, retries, GPU request, PVC mounts |
| **`k8s/` manifests** | MLflow Service, PVCs / MinIO, DCGM DaemonSet, Grafana |
| **Model Registry + gates** | Do not promote a checkpoint if CER / speaker-sim / UTMOS fail |
| **CI** | Lint + unit tests on every PR (not GPU training) |
| **Remote artifact store** | Checkpoints and wavs on S3/MinIO/PVC |
| **Data versioning (optional)** | DVC or object-store hashes for audio + JSONL |
| **Production serving** | KServe or a Deployment from a Registry URI |

Until those exist you can train, evaluate, and watch GPUs locally; you cannot submit the same job to a GPU node pool or auto-promote a model.

### Next plan — full cluster MLOps

Keep today’s CLIs. Do **not** rewrite `train/` for Kubernetes.

```text
./scripts/run.sh train --config configs/experiments/lora_single.yaml
        ↓
docker run … python -m qwen3_tts_ft.train --config /config/lora_single.yaml
        ↓
Kubeflow component (same command, GPU + PVC)
```

**Phase A — containerize**

- `docker/Dockerfile.train` — prepare + train + evaluate (CUDA)
- `docker/Dockerfile.serve` — Gradio / later KServe
- Image command = `python -m qwen3_tts_ft.<stage>`

**Phase B — cluster core**

- MLflow as a Kubernetes Service (`MLFLOW_TRACKING_URI=http://mlflow:5000`)
- PVCs or MinIO/S3 for audio, JSONL, checkpoints
- GPU node pool
- DCGM exporter DaemonSet + Prometheus + Grafana (same dashboard as `monitoring/`)

**Phase C — Kubeflow Pipelines**

- `kfp/pipeline.py`: `prepare` → `train` → `evaluate` → `register?`
- Optional `cluster` when `speaker_mode: multi`

**Phase D — registry, gates, serve**

- Register only if YAML thresholds pass
- MLflow Model Registry: Staging → Production
- Serve from `models:/qwen3-tts-hk-cantonese/Staging`

**Phase E — hygiene**

- GitHub Actions: lint + `unittest` on PR (CPU only)
- Optional Katib (LoRA rank / LR), optional DVC

Target extras when that work lands:

```text
docker/Dockerfile.train
docker/Dockerfile.serve
kfp/pipeline.py
k8s/mlflow.yaml
k8s/pvc.yaml
k8s/dcgm-exporter.yaml
k8s/serve.yaml
.github/workflows/ci.yml
```

---

## 9. Tests, limits, license

```bash
python -m unittest discover -s tests -v
```

- Multi-speaker train **fails** if any line lacks `speaker_id`
- Base model is strong in Mandarin/Chinese; fine-tuning adapts HK Cantonese
- Default MLflow URI needs `mlflow ui` (or change `run.tracking_uri`)

MIT. Upstream: [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS).  
PRs and pre-trained HK Cantonese checkpoints welcome.
