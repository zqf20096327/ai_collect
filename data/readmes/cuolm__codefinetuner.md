# CodeFinetuner
![Logo](docs/readme-assets/codefinetuner-logo.png)
[![PyPI](https://img.shields.io/pypi/v/codefinetuner.svg)](https://pypi.org/project/codefinetuner/)
[![License](https://img.shields.io/github/license/cuolm/codefinetuner.svg)](/LICENSE.txt)
[![Release](https://github.com/cuolm/codefinetuner/actions/workflows/release.yaml/badge.svg)](https://github.com/cuolm/codefinetuner/actions/workflows/release.yaml)
[![Tests](https://github.com/cuolm/codefinetuner/actions/workflows/tests.yaml/badge.svg)](https://github.com/cuolm/codefinetuner/actions/workflows/tests.yaml)

CodeFinetuner fine-tunes a local code autocomplete model on your own repository for use in editors like VS Code or Vim/Neovim.
It trains a Low-Rank Adapter ([LoRA](https://arxiv.org/abs/2106.09685)) on Structure-Aware Fill-in-the-Middle ([FIM](https://arxiv.org/abs/2207.14255)) examples so the model learns the structure and patterns of your codebase.

The result is an autocomplete model specialized on your codebase that runs entirely on your machine. If you have the hardware to fine-tune locally, this keeps your source code fully private, it never leaves your system, no cloud service, no external API.

## Table of Contents
- [Demo](#demo)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [How Training Examples Are Created](#how-training-examples-are-created)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [MLflow Tracking](#mlflow-tracking)
- [Evaluation](#evaluation)
- [Fine-tuned Model Usage](#fine-tuned-model-usage)
- [Docker Image](#docker-image)
- [Tree-sitter Customization](#tree-sitter-customization)
- [Tests](#tests)
- [Resources](#resources)
- [License](#license)

## Demo
https://github.com/user-attachments/assets/d4fe8709-5b3a-4aec-bc4b-898ca3d66bd0

## Architecture
CodeFinetuner follows a simple pipeline. First, raw code is parsed and turned into FIM examples. These examples are then used to train a LoRA adapter and evaluate the fine-tuned model using multiple metrics. Finally, the model is converted into GGUF format for deployment.

```text
Raw Code Files
     |
     v
[Preprocess]  -- tree-sitter parsing -> FIM examples -> tokenized jsonl datasets
     |
     v
[Finetune]    -- LoRA adapter training -> merged safetensors model
     |
     v
[Evaluate]    -- CodeBLEU, SentenceBLEU, edit similarity, exact match, line match, perplexity
     |
     v
[Convert]     -- GGUF conversion -> GGUF model for local inference
```

## Project Structure
```text
.
├── src/
│   └── codefinetuner/           # Core packages
│       ├── preprocess/
│       ├── finetune/
│       ├── evaluate/
│       └── convert/             
├── config/                      # User configuration
│   └── codefinetuner_config.yaml
├── data/                        # Default data directory 
├── outputs/                     # Pipeline outputs
├── scripts/                     # Utility scripts
├── tests/                       # Tests 
├── third_party/                 # External submodules 
└── docs/                        # Documentation 
```

## How Training Examples Are Created
CodeFinetuner builds FIM examples from real code structure. It first extracts blocks such as functions or classes, then masks smaller sub-blocks like statements or expressions for the model to predict. This approach helps the model learn the logical structure of your codebase instead of unrelated fragments.

![Example Diagram](docs/readme-assets/example-diagram.png)

Additionally, config parameters are available to include randomly split FIM examples in your dataset, which can sometimes improve fine-tuning results.

## Quick Start

### 1. Installation
Install CodeFinetuner globally to run the pipeline anywhere on your system:
```bash
uv tool install codefinetuner
```

### 2. Configuration
Download the default configuration file and adjust the parameters as needed:
```bash
curl -L -O https://raw.githubusercontent.com/cuolm/codefinetuner/master/config/codefinetuner_config.yaml
```
*Alternatively, create one manually according to the [Configuration](#configuration) section.*

### 3. Adding Your Data
Prepare your training data directory:
```bash
mkdir -p data
```
Place your target code files inside the `data/` directory.

*For manual dataset splitting, place your files into `data/train/`, `data/eval/`, and `data/test/`, then update `split_mode: "manual"` in `codefinetuner_config.yaml` (default is `"auto"`).*

### 4. Execution
Run the pipeline:
```bash
codefinetuner --config="codefinetuner_config.yaml"
```

## Installation

### As a Global CLI Tool
```bash
uv tool install codefinetuner
```

### As a Library Dependency
```bash
# Using uv
uv add codefinetuner

# Using pip
pip install codefinetuner
```

### From Source
```bash
git clone --recurse-submodules https://github.com/cuolm/codefinetuner
cd codefinetuner

# Using uv (Recommended)
uv sync

# Using pip
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

> **Note:** See [MLflow Tracking](#mlflow-tracking) to install with MLflow tracking support (`codefinetuner[mlflow]`).

> **Note:** For NVIDIA GPU training, your driver and the installed PyTorch build must be compatible. See the [NVIDIA GPU / CUDA Compatibility Guide](/docs/nvidia-gpu/nvidia-gpu-compatibility.md) if training falls back to CPU or stops with a GPU error.

## Configuration
The pipeline uses a single-source-of-truth YAML configuration file. It utilizes YAML anchors (`&globals`) to share core parameters across all stages (`preprocess`, `finetune`, `evaluate`, `convert`), ensuring consistency and reducing redundancy.

### Configuration Structure

Create `codefinetuner_config.yaml` using the template below. For the full parameter list, see the [Configuration Reference Guide](/docs/configuration/config-file.md).

```yaml
# globals contain all the mandatory parameters.
globals: &globals
  workspace_path: null  # null: defaults to current working directory (CWD)
  model_name: "unsloth/Qwen2.5-Coder-3B" 
  fim_prefix_token: "<|fim_prefix|>"
  fim_middle_token: "<|fim_middle|>"
  fim_suffix_token: "<|fim_suffix|>"
  fim_pad_token: "<|fim_pad|>"
  eos_token: "<|endoftext|>"
  label_pad_token_id: -100
  max_token_sequence_length: 1024
  data_language: "c"
  data_extensions: [".c", ".h"]
  use_unsloth: False  # True enables Unsloth optimizations, requires CUDA

preprocess:
  <<: *globals  # inherits all global parameters
  split_mode: "auto"
  # ... (preprocess specific settings)

finetune:
  <<: *globals
  lora_r: 32
  trainer_num_train_epochs: 1
  # ... (finetune specific settings)

evaluate:
  <<: *globals
  benchmark_sample_size: 250
  # ... (evaluate specific settings)

convert:
  <<: *globals
  # ... (convert specific settings)
```
> **Note:** See [`config/codefinetuner_config.yaml`](/config/codefinetuner_config.yaml) for a full production example.

### Data Preparation
Place source files in your `raw_data_path` (default: `workspace_path/data`).
- **Auto Split:** Place files directly in the directory.
- **Manual Split:** Create `train`, `eval`, and `test` subfolders inside `raw_data_path` and assign files according to your manual split preferences.

## Usage

### CLI Usage
If installed via `uv tool install`:
```bash
codefinetuner --config="codefinetuner_config.yaml"
```

If running within the source repository cloned from GitHub:
```bash
# Installed via uv (Recommended)
uv run codefinetuner --config="config/codefinetuner_config.yaml"

# Installed via pip
python3 -m codefinetuner.pipeline --config="config/codefinetuner_config.yaml"
```

**Pipeline flags**
- `--config`: Use a different config file.
- `--skip-preprocess`: Skip preprocessing.
- `--skip-finetune`: Skip fine-tuning.
- `--skip-evaluate`: Skip evaluation.
- `--skip-convert`: Skip conversion.

### Python Module Usage
```python
import codefinetuner

# Full pipeline
codefinetuner.run_pipeline("codefinetuner_config.yaml")

# Skip stages
codefinetuner.run_pipeline(
    "codefinetuner_config.yaml",
    skip_preprocess=True,
    skip_convert=True
)
```
## Evaluation
After the `evaluate` stage runs, results are saved under `outputs/evaluate`. This shows how the fine-tuned model compares to the base model across metrics such as CodeBLEU, SentenceBLEU, edit similarity, exact match, line match, and perplexity.

For full example runs, see:
- [TinyUSB Example](/docs/example-runs/tinyusb-example/finetuning-example-tinyusb.md)
- [ST Example](/docs/example-runs/st-example/finetuning-example-st.md)

> **Note:** The `evaluate` stage's benchmark scores use greedy decoding, so they're reproducible and comparable across runs. [llama.vim](https://github.com/ggml-org/llama.vim) and [llama.vscode](https://github.com/ggml-org/llama.vscode) instead sample with `top_k` and `top_p`, so completions in your editor won't exactly match the benchmark numbers. Treat the benchmark as a way to compare fine-tuning runs against each other — the real measure of usefulness is how the model performs in your editor.

## MLflow Tracking
CodeFinetuner can track metrics and artifacts for each pipeline stage using [MLflow](https://mlflow.org/). It is an optional extra, not installed by default.

### Enable MLflow

**As a Global CLI Tool**
```bash
uv tool install "codefinetuner[mlflow]"
```

**As a Library Dependency**
```bash
# Using uv
uv add "codefinetuner[mlflow]"

# Using pip
pip install "codefinetuner[mlflow]"
```

**From Source**
```bash
git clone --recurse-submodules https://github.com/cuolm/codefinetuner
cd codefinetuner

# Using uv (Recommended) — mlflow is already included via the dev dependency group
uv sync

# Using pip
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e ".[mlflow]"
```

### View Tracked Runs
Tracking data is stored locally in a SQLite backend under `outputs/mlflow`. Launch the UI to inspect runs:
```bash
uv run mlflow ui --backend-store-uri sqlite:///outputs/mlflow/mlflow.db
```

### Model Artifact Logging
Use the `mlflow_model_logging_strategy` config parameter to control which model artifacts (LoRA adapters, merged GGUF models) get logged, since GGUF exports can be large. See the [Configuration Reference Guide](/docs/configuration/config-file.md) for all options.

## Fine-tuned Model Usage
The `convert` stage exports the final model to [GGUF](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) format for local inference. The resulting file is saved at `outputs/convert/results/<model_name>-lora-merged.gguf`, where `<model_name>` is the last segment of your configured `model_name` (e.g. `model_name: "unsloth/Qwen2.5-Coder-3B"` produces `Qwen2.5-Coder-3B-lora-merged.gguf`).

For setup instructions with Vim/Neovim, see [llama.vim](https://github.com/ggml-org/llama.vim).
For setup instructions with the VS Code extension [llama.vscode](https://github.com/ggml-org/llama.vscode), see the [inference-vscode](/docs/inference-llama-vscode/inference-vscode.md) guide.

## Docker Image
Docker images are automatically built and published using GitHub Actions. Separate images are available for GPU and CPU usage. The built images can be found in the project's [GitHub Container Registry](https://ghcr.io/cuolm/codefinetuner). Images are tagged `:cpu`/`:gpu` (always pointing to the latest release) and by version. Containers start an SSH service automatically, useful for remote GPU providers like RunPod (see the [RunPod Setup Guide](/docs/runpod-setup/setup-runpod.md)).

### Manual Build

#### 1. Build the Docker Image
GPU Image:
```bash
docker build -f Dockerfile.gpu -t codefinetuner:gpu-local .
```
CPU Image:
```bash
docker build -f Dockerfile.cpu -t codefinetuner:cpu-local .
```

#### 2. Prepare Data and Run the Container
To allow the container to access your data for fine-tuning, use a bind mount to link your host machine's `data` directory to the container.  
On your host machine (where you run Docker), create a folder named `data` if it does not already exist. Put all files you want to use for fine-tuning inside the `data` directory. For manual mode, include `train`, `eval`, and `test` subfolders with the split you want to use.  

#### NVIDIA GPU (Recommended)
Use this command to enable CUDA support for `torch` and `bitsandbytes`. Requires the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) installed on the host machine. See the [NVIDIA GPU Setup Guide](/docs/nvidia-gpu/nvidia-gpu-compatibility.md) for driver and PyTorch build compatibility.
```bash
docker run --gpus all -it --rm \
  -v $(pwd)/data:/app/data \
  codefinetuner:gpu-local /bin/bash
```
#### CPU Only
Use this if you do not have a compatible GPU. Fine-tuning will be much slower.
```bash
docker run -it --rm \
  -v $(pwd)/data:/app/data \
  codefinetuner:cpu-local /bin/bash
```

## Tree-sitter Customization
Tree-sitter turns source code into structural blocks used to generate FIM examples. Use this section to add new languages or build missing parsers.

- [Add Language Definitions](/docs/tree-sitter-customization/tree-sitter-customization.md#add-new-language-block-definitions): define `block_types` and `subblock_types` in JSON.
- [Build Custom Parser](/docs/tree-sitter-customization/tree-sitter-customization.md#build-custom-parser): compile a parser from source, for example for Mojo.

## Tests
Run the test suite with:
```bash
pytest tests
```

## Resources
- [Qwen2.5-Coder Technical Report](https://arxiv.org/pdf/2409.12186)
- [Structure-Aware Fill-in-the-Middle Pretraining for Code](https://arxiv.org/pdf/2506.00204)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/pdf/2106.09685)
- [Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/pdf/2207.14255)
- [From Output to Evaluation: Does Raw Instruction-Tuned Code LLMs Output Suffice for Fill-in-the-Middle Code Generation?](https://arxiv.org/pdf/2505.18789)
- [CodeBLEU: a Method for Automatic Evaluation of Code Synthesis](https://arxiv.org/pdf/2009.10297)
- [HF LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
- [llama.vim](https://github.com/ggml-org/llama.vim)
- [llama.vscode](https://github.com/ggml-org/llama.vscode)

## License
Licensed under the [Apache License 2.0](/LICENSE.txt).