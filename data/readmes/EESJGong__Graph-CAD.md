# Graph-CAD

<div align="center">

## Learning Hierarchical and Geometry-Aware Graph Representations for Text-to-CAD

[![Project Page](https://img.shields.io/badge/Project%20Page-TODO-6e7781.svg)](#)
[![Paper](https://img.shields.io/badge/Paper-OpenReview-b31b1b.svg)](https://openreview.net/pdf?id=oKMomThD6n)
[![GitHub Code](https://img.shields.io/badge/GitHub-Code-1f6feb.svg)](https://github.com/EESJGong/Graph-CAD)
[![Model](https://img.shields.io/badge/Model-ModelScope-ff8c00.svg)](https://modelscope.cn/models/JackeySmile/graph-cad)

**Shengjie Gong, Wenjie Peng, Hongyuan Chen, Gangyu Zhang, Yunqing Hu, Huiyuan Zhang, Shuangping Huang, Tianshui Chen**

[Overview](#overview) | [News](#news) | [Installation](#installation) | [Inference](#inference-pipeline) | [Evaluation](#evaluation) | [Citation](#citation)

</div>

<p align="center">
  <img src="assets/teaser_placeholder.png" alt="Graph-CAD teaser" width="92%">
</p>
<p align="center">
  <em>AI-generated schematic overview of the Graph-CAD pipeline, illustrating graph-mediated Text-to-CAD generation from natural language instructions to executable Blender code.</em>
</p>

## Overview

Graph-CAD is a graph-mediated Text-to-CAD framework for long-horizon CAD code generation. Instead of directly decoding natural language into executable `bpy` code, Graph-CAD first predicts a hierarchical and geometry-aware decomposition graph, then transforms the graph into operation sequences and finally into executable Blender code.

This design addresses a central challenge in Text-to-CAD: small early errors in long sequential generation can propagate and invalidate the final assembly. Graph-CAD reduces this fragility by explicitly modeling:

- product hierarchy through multi-level decomposition nodes
- geometric and assembly constraints through graph edges
- staged generation through `instruction -> graph -> CAD actions -> bpy code`
- increasingly difficult structures through progressive curriculum learning

## 📰 News

- `[2026-02]` Graph-CAD paper accepted to ICLR 2026.
- `[2026-03]` Pre-release codebase organized for public release, and Graph-CAD model weights are now available.
- `[TODO]` Add project webpage, organize the dataset release, and open-source the full evaluation code.

## ✨ Highlights

- **Graph-mediated generation**: a hierarchical, geometry-aware graph serves as the intermediate representation between text and CAD code.
- **Three-stage inference**: the system sequentially predicts decomposition graphs, CAD actions, and executable `bpy` programs.
- **Progressive curriculum learning**: Graph-CAD synthesizes boundary-difficulty examples to improve graph prediction on highly constrained assemblies.
- **BlendGeo dataset**: a 12K-scale dataset pairing instructions, decomposition graphs, action sequences, and executable Blender code.
- **Comprehensive evaluation**: the project evaluates graph quality, rendered output quality, and geometric constraint satisfaction.

## 🧩 Framework

Graph-CAD follows the same design described in the paper: it first builds a hierarchical geometry-aware graph, then converts that graph into executable CAD generation through a modular three-stage pipeline, and finally improves the graph modeling ability with structure-aware progressive curriculum learning.

### 1. Geometry-aware graph structure

<p align="center">
  <img src="assets/graph_structure.png" alt="Graph-CAD geometry-aware graph structure" width="96%">
</p>
<p align="center">
  <em>Figure 1-style illustration of Graph-CAD graph construction: top-down decomposition, geometric constraint connections, and structured text serialization.</em>
</p>

As in Figure 1 of the paper, Graph-CAD represents a target object as a hierarchical geometric decomposition graph. Starting from the whole object, the model performs top-down decomposition until each part can be realized by primitive Blender operators. The resulting parts and subcomponents become graph nodes, while spatial relations such as alignment and attachment are encoded as explicit geometric constraints on edges. The graph is then serialized as structured text, which preserves both hierarchy and constraints for downstream generation.

### 2. Three-stage inference

<p align="center">
  <img src="assets/three_stage_inference.png" alt="Graph-CAD three-stage inference pipeline" width="96%">
</p>
<p align="center">
  <em>Figure 2-style overview of the three-stage Graph-CAD inference pipeline: Geometry Decomposition, Action Planning, and Code Generation.</em>
</p>

As in Figure 2 of the paper, Graph-CAD decomposes Text-to-CAD generation into three sequential stages. In **Stage 1**, the Geometry Decomposition model predicts a hierarchical graph with geometric constraints from the user instruction. In **Stage 2**, the Action Planning model converts this graph into an ordered CAD action sequence that respects assembly structure and local dependencies. In **Stage 3**, the Code Generation model translates the planned actions into executable `bpy` code. This staged design reduces the search space compared with flat end-to-end decoding and improves both geometric fidelity and constraint satisfaction.

### 3. Structure-aware progressive curriculum learning

<p align="center">
  <img src="assets/sapcl_pipeline.png" alt="Graph-CAD SAPCL training mechanism" width="96%">
</p>
<p align="center">
  <em>Figure 3-style overview of SAPCL: alternating supervised fine-tuning and structure-aware progressive curriculum exploration.</em>
</p>

To improve robustness on highly constrained assemblies, Graph-CAD adopts the SAPCL mechanism described in Figure 3 of the paper. The method alternates between **Supervised Fine-Tuning (SFT)** and **Structure-aware Progressive Curriculum Exploration (SAPCE)**. SAPCE first samples seed instances and uses a problem generator to create graded variants ranging from easy edits to more challenging structural and category-level changes. A discriminator then estimates the model's capability boundary, and boundary data generation synthesizes new training samples near that frontier. These validated samples are merged back into training for the next SFT round, allowing the model to progressively master more complex decomposition graphs.

## 📁 Repository Layout

```text
Graph-CAD/
|- CADBench.jsonl          # benchmark input file adapted from BlenderLLM
|- infer_api.py
|- render_auto.py
|- evaluate_and_report.py
|- prompt_sft/
|- utils/
|- LlamaFactory/         # local clone, not committed
|- qwen3/                # local base model weights, not committed
|- checkpoints/
|  |- stage1/
|  |- stage2/
|  `- stage3/
`- output/               # generated outputs, renders, and evaluation files
```

## 🛠️ Installation

The intended setup flow for this repository is:

```bash
# 1. Clone Graph-CAD
git clone https://github.com/EESJGong/Graph-CAD.git
cd Graph-CAD

# 2. Clone LlamaFactory
git clone https://github.com/hiyouga/LlamaFactory

# 3. Create environment
conda create -n graphcad python=3.10 -y
conda activate graphcad

# 4. Install LlamaFactory and dependencies
cd LlamaFactory
pip install -e .
pip install -r requirements/metrics.txt
pip install openai
pip install modelscope
cd ..

# 5. Install Blender for bpy execution and rendering
wget https://download.blender.org/release/Blender4.4/blender-4.4.1-linux-x64.tar.xz
tar -xf blender-4.4.1-linux-x64.tar.xz

# 6. Prepare the base model directory
mkdir -p qwen3

# 7. Download Qwen3-8B into the repository-local folder
modelscope download --model Qwen/Qwen3-8B --local_dir ./qwen3

# 8. Prepare the Graph-CAD checkpoint directory
mkdir -p checkpoints

# 9. Download Graph-CAD weights from ModelScope into the local checkpoint folder
modelscope download --model JackeySmile/graph-cad --local_dir ./checkpoints
```

After setup, make sure the following local paths exist before running inference:

- `./qwen3`
- `./checkpoints/stage1`
- `./checkpoints/stage2`
- `./checkpoints/stage3`
- `./prompt_sft`
- `./output`
- `./blender-4.4.1-linux-x64`

## 🚀 Inference Pipeline

Graph-CAD uses a three-stage pipeline implemented in `infer_api.py`:

1. Predict a hierarchical geometric decomposition graph from the instruction.
2. Convert the graph into a CAD action sequence.
3. Generate executable Blender `bpy` code.

Run inference with default repository-local paths:

```bash
python infer_api.py
```

Important default local paths:

- base model: `./qwen3`
- adapters: `./checkpoints/stage1`, `./checkpoints/stage2`, `./checkpoints/stage3`
- prompts: `./prompt_sft`
- benchmark input: `./CADBench.jsonl`
- generated outputs: `./output/result_name`

## 🎨 Rendering

Before rendering, make sure Blender is installed locally. If you followed the installation section above, the executable path is `./blender-4.4.1-linux-x64/blender`.

After inference, render generated `bpy.txt` files with:

```bash
python render_auto.py \
  --base_dir output/result_name \
  --all \
  --blender_executable ./blender-4.4.1-linux-x64/blender
```

Important parameters:

- `--all`: render all subfolders under the target directory
- `--recursive`: recursively search subfolders when needed
- `--overwrite`: force re-render even if `.png` files already exist
- `--timeout`: set per-sample rendering timeout
- `--blender_executable`: specify a custom Blender executable path

## 📏 Evaluation

The evaluation script merges generation-time judging and final metric summarization into one entry point:

```bash
python evaluate_and_report.py \
  --api-base YOUR_BASE_URL \
  --api-key YOUR_API_KEY \
  --model YOUR_MODEL_NAME
```

You should configure at least these API-related arguments:

- `--api-base`: model service base URL
- `--api-key`: API key
- `--model`: model name used for evaluation

By default, the script uses repository-local input and output paths:

- configs: `./CADBench.jsonl`
- rendered sample folder: `./output/result_name`
- merged result file: `./output/result_name.jsonl`
- metrics file: `./output/result_name_metrics.json`

## 📊 Main Results

### 1. Comparison with existing methods

<p align="center">
  <img src="assets/baseline_results.png" alt="Qualitative comparison with baseline methods" width="95%" />
</p>
<p align="center">
  <em>Qualitative comparison on CADBench examples. Compared with direct end-to-end generation and existing text-to-CAD baselines, Graph-CAD produces more complete structures, more coherent part relations, and fewer execution errors on challenging multi-part objects.</em>
</p>

Table 2 in the paper shows that Graph-CAD consistently improves over both open-source text-to-CAD systems and strong proprietary LLM baselines. The SAPCL-trained version further improves the SFT model, with the largest gains on geometric constraint satisfaction and out-of-distribution CADBench-Wild prompts.

#### CADBench comparison (Table 2 in the paper)

| Models | CADBench-Sim Attr. | CADBench-Sim Spat. | CADBench-Sim Inst. | CADBench-Sim Avg. | CADBench-Sim E syntax | CADBench-Sim CLIP | CADBench-Sim GCS | CADBench-Wild Attr. | CADBench-Wild Spat. | CADBench-Wild Inst. | CADBench-Wild Avg. | CADBench-Wild E syntax | CADBench-Wild CLIP | CADBench-Wild GCS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| BlenderLLM | 0.6893 | 0.6953 | 0.3650 | 0.5832 | 2.4% | 0.6409 | 0.5513 | 0.6782 | 0.6363 | 0.4581 | 0.5909 | 5.3% | 0.6056 | 0.4983 |
| Text2CAD | 0.3278 | 0.2084 | 0.0446 | 0.1936 | 6.6% | 0.5707 | - | 0.4198 | 0.3082 | 0.1323 | 0.2868 | 14.0% | 0.5211 | - |
| CADFusion | 0.3566 | 0.2258 | 0.0674 | 0.2166 | 6.2% | 0.5578 | - | 0.3822 | 0.3716 | 0.1496 | 0.3011 | 11.5% | 0.5278 | - |
| Qwen-Plus | 0.3604 | 0.3777 | 0.2072 | 0.3151 | 48.4% | 0.3362 | 0.2379 | 0.2596 | 0.2722 | 0.1951 | 0.2423 | 61.0% | 0.2446 | 0.1305 |
| Llama-3.1-405b | 0.3302 | 0.3355 | 0.1537 | 0.2731 | 36.4% | 0.3943 | 0.3269 | 0.3331 | 0.3530 | 0.1943 | 0.2934 | 47.2% | 0.3242 | 0.2903 |
| Deepseek-r1 | 0.4124 | 0.4366 | 0.2179 | 0.3556 | 19.2% | 0.5011 | 0.5556 | 0.4814 | 0.5141 | 0.3735 | 0.4564 | 20.5% | 0.4858 | 0.4275 |
| Gemini-2.5-pro | 0.2173 | 0.2180 | 0.1565 | 0.1972 | 42.4% | 0.2050 | 0.4048 | 0.2002 | 0.1880 | 0.1667 | 0.1850 | 48.7% | 0.1750 | 0.2584 |
| GPT-5 | 0.7013 | 0.7347 | 0.4250 | 0.6203 | 2.8% | 0.6449 | 0.3846 | 0.6858 | 0.7091 | 0.5595 | 0.6515 | 5.5% | 0.6003 | 0.4017 |
| Claude-opus-4-1 | 0.7216 | 0.7368 | 0.5403 | 0.6662 | 7.4% | 0.6151 | 0.4932 | 0.6847 | 0.7218 | 0.5997 | 0.6687 | 14.5% | 0.5550 | 0.5062 |
| Graph-CAD (SFT) | 0.7295 | 0.7265 | 0.4733 | 0.6431 | 2.4% | 0.6544 | 0.7830 | 0.6944 | 0.7270 | 0.5861 | 0.6692 | 4.5% | 0.6358 | 0.8025 |
| **Graph-CAD (SAPCL)** | **0.7681** | **0.7423** | **0.5546** | **0.6883** | **2.0%** | **0.6693** | **0.9018** | **0.7695** | **0.7590** | **0.6057** | **0.7114** | **2.5%** | **0.6577** | **0.8943** |

### 2. Effect of the three-stage pipeline

<p align="center">
  <img src="assets/three_stage_ablation.png" alt="Ablation of the three-stage Graph-CAD pipeline" width="92%" />
</p>
<p align="center">
  <em>Ablation results for the graph-mediated pipeline. Removing graph decomposition often leads to unreasonable global structure, while removing action planning causes local part mistakes and lower executability. The full three-stage pipeline yields the most stable and faithful CAD programs.</em>
</p>

The ablation in Table 3 and the visual examples in Figure 5 show that both intermediate stages are important. Without graph decomposition, the model struggles to organize high-level part layouts. Without action planning, it can still drift when translating structure into executable operations. The complete Graph-CAD pipeline reduces assembly errors, unreasonable shapes, and syntax failures at the same time.

### 3. Progressive gains from SAPCL

<p align="center">
  <img src="assets/sapcl_visualization.png" alt="Visualization of SAPCL training progress" width="95%" />
</p>
<p align="center">
  <em>Visualization of structure-aware progressive curriculum learning (SAPCL). As the curriculum advances from the base model to supervised fine-tuning and later SAPCL iterations, the generated CAD programs become more structured, more complete, and more reliable on complex objects.</em>
</p>

Figure 6 in the paper visualizes how SAPCL improves generation step by step. Early models often miss global structure or collapse on long-horizon assemblies, while later curriculum iterations better preserve hierarchical decomposition, part coordination, and execution validity. This progressive improvement explains why Graph-CAD (SAPCL) achieves the strongest final results in Table 2.

## 💙 Acknowledgements

This project builds on:

- [LlamaFactory](https://github.com/hiyouga/LlamaFactory) for local model serving and finetuning workflows
- [Qwen/Qwen3-8B](https://modelscope.cn/models/Qwen/Qwen3-8B) as the base model in the current setup
- [BlenderLLM](https://github.com/FreedomIntelligence/BlenderLLM) for the CAD benchmark setup; `CADBench.jsonl` in this repository is derived from the BlenderLLM benchmark release
- Blender-based execution and rendering utilities for final CAD verification

## 📚 Citation

If you find Graph-CAD useful in your research, please consider citing:

```bibtex
@inproceedings{gonglearning,
  title={Learning Hierarchical and Geometry-Aware Graph Representations for Text-to-CAD},
  author={Gong, Shengjie and Peng, Wenjie and Chen, Hongyuan and Zhang, Gangyu and Hu, Yunqing and Zhang, Huiyuan and Huang, Shuangping and Chen, Tianshui},
  booktitle={The Fourteenth International Conference on Learning Representations}
}
```

## ✉️ Contact

For questions about the project, please open an issue in this repository or contact the authors listed in the paper.
