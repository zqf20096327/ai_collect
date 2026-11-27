# WSMs: World Snapshot Models

[[Paper]](https://arxiv.org/abs/2611.24917) |
[[Project Page]](https://world-snapshot.github.io/WSMs/) |
[[Model]](https://huggingface.co/World-Snapshot/WSM_v1) |
[[Datasets]](https://huggingface.co/World-Snapshot/datasets) |
[[Post-training Materials]](https://huggingface.co/World-Snapshot/WSM_v1-Training-Resources) |
[[Documentation]](https://world-snapshot.github.io/doc/index.html) |
[[pip Install]](#installation) |
[[Python Pipeline]](#inference) |
[[Quickstart Notebook]](src/examples/WSM_Quickstart.ipynb) |
[[WebUI]](https://github.com/World-Snapshot/ControlWorld) |
[[World Snapshot Graphics]](https://github.com/World-Snapshot/wsg) |
[[Organization]](https://github.com/World-Snapshot) |
[[Live Demo]](https://huggingface.co/spaces/FangSen9000/WSM-ControlWorld)

World Snapshot Models (WSMs) are an ideal world model designed to **unify, expand, and ultimately transcend Computer Vision**. The first version is WSM v1, codename Augustus.

To train the world itself, we define world frames and design the [World Snapshot Graphics (`.wsg`)](https://github.com/World-Snapshot/wsg) format, encoding RGB, geometry, motion, pose, physics, materials, semantics, audio, and other information into a unified 256-channel image.

Then, at the end of 2024, we discovered the [Unified Law for Visual Tasks](https://github.com/World-Snapshot/Unified-Law-for-Visual-Tasks): **if all information can be encoded into the image itself, then two-dimensional image generation becomes lossless world generation.** This law is supported to some extent by the physical holographic principle. In detail:

| **Dimension of Comparison** | **World Snapshot Models** | **Large Language Models** |
|---|---|---|
| Field | Vision | Natural Language Processing |
| Methodology | Encode information into images | Predict the next Token |
| Main law/principle implemented | [Unified Law](https://github.com/World-Snapshot/Unified-Law-for-Visual-Tasks): all visual tasks take a generative form | [Scaling Laws](https://arxiv.org/abs/2001.08361): intelligence emerges from next-Token prediction |
| Can unify all tasks in the corresponding field | **Yes** | **Yes** |
| Can absorb other fields | **Yes** | **Yes** |
| Can enable multiplicative expansion of fields and tasks | **Yes** | **Yes** |
| Zero-shot / training-free / plug-and-play / scalable | **Yes** | **Yes** |
| Can transcend the original field and form new research | **Yes** | **Yes** |
| Chains of Visual Thought / Chains of Thought | **Yes** | **Yes** |

## News

- **2026.11.21:** We have consolidated WSM v1 into a single 43 GB model file with roughly 18 billion parameters. Training checkpoints, optimizer states, and logs are now hosted separately as [Post-training Materials](https://huggingface.co/World-Snapshot/WSM_v1-Training-Resources), and `wsms`, `WSMPipeline`, and ControlWorld have been updated. Please [report any migration issues](https://github.com/World-Snapshot/WSMs/issues).
- **2026.11.18:** 🎉🎉 We have fully open-sourced everything, including paper, code, data, documentation, WebUI, Live Demo, Training state file, one-click installation via Pip/Pipeline, evaluation scripts, and even training logs.  Enjoy it!

## WSM v1

WSM v1 is the first large-scale implementation of the Unified Law for Visual Tasks. The method can unify thousands of visual tasks; we validated **1,148 tasks in one generative model**, and provide a trained baseline for every task. Capabilities traditionally scattered across different models, datasets, and research communities coexist within the same system. Previously, 99.99% of visual models were used to perform one visual task.

Papers with Code recorded 1,477 visual or vision-related tasks, broadly representing the existing field of Computer Vision. All 1,477 tasks are compatible with WSM interfaces. Among the 1,148 tasks evaluated by WSM, an estimated **655–1,056 are entirely new visual tasks**. Therefore, WSM not only incorporates the existing visual-task space into the same generative system, but also **expands Computer Vision by 44.3–71.5%**. And this is only the beginning; more visual tasks will be created and unified in the future:

With only a few hundred samples and a few hours of training, we can obtain growth in multiple task capabilities. Moreover, our thousands and tens of thousands of tasks are like connected paths. These task paths share the same generator; each path adds only one 12.51M-parameter tunnel. With the complete task bank loaded, WSM v1 is an 18B-class model. Task capacity can grow by orders of magnitude without increasing the parameter count by thousands or tens of thousands of times.

## TunnelingNet

We achieve such powerful capabilities because of a new training technology named **TunnelingNet**.

While preserving the shared generative backbone, TunnelingNet (Trans: 隧穿网络) learns a compact path for each task (which can be implicit or explicit). These paths can be trained independently and in parallel, and then registered into the same model. They can be loaded together or separately; after all, an individual task should be able to flexibly continue training, improve, be separated out, or be newly added.

Compared with existing multimodal/vision/unified-model/video-generation methods with the same parameter count, TunnelingNet can reveal recognizable structure **77–100 times** earlier and reduce the number of optimizer updates by **19.0–38.5 times**. Just like quantum tunneling, our modes can be simultaneously generated and coexist through tunneling, influencing each other—a feat difficult to achieve in classical vision and requiring rigorous training.

This is also why we can easily unify thousands of tasks.

## Repository Structure

```text
WSMs/
├── WSM_v1/
│   ├── configs/              # Task graph and release configurations
│   ├── data/                 # Released latent-data workspace
│   ├── env/                  # WSM v1 environment submodule
│   ├── manual_processing/    # Dataset and latent-cache construction
│   ├── models/               # Shared backbone
│   ├── scripts/              # TunnelingNet training launch scripts
│   ├── src/
│   │   ├── dataset/
│   │   ├── evaluation/
│   │   └── pipelines/
│   ├── webui/                # ControlWorld plugin
│   └── wsg_reader/           # Official WSG visualization
├── assets/
├── LICENSE
└── README.md
```

Each major WSM version has an independent environment. `WSM_v1/env` is fixed for the current version; a future `WSM_v2/env` can use different versions without changing WSM v1.

## Installation

Use the Python training and inference pipeline:

```bash
pip install wsms
```

or

Run ALL in the [`WSM_Quickstart.ipynb`](src/examples/WSM_Quickstart.ipynb) notebook.

or

Use training and repository development, clone the complete repository:

```bash
git clone --recursive https://github.com/World-Snapshot/WSMs.git
git submodule update --init --recursive
cd WSMs

conda create -n WSM python=3.11 -y
conda activate WSM
pip install -r WSM_v1/env/requirements.txt
```

## Models and Data

Our backbone uses the fully open Apache 2.0-licensed FLUX.2 Klein 4B model. Place it at:

```text
WSM_v1/models/black-forest-labs/FLUX.2-klein-4B/
```

For inference, use the unified single-model release. `WSMPipeline` reads its
index and materializes only the shared runtime and the selected task:

- [[WSM v1 unified inference model]](https://huggingface.co/World-Snapshot/WSM_v1)

For continued training, retraining, or inspecting individual training runs,
download the released checkpoints, optimizer states, resolved configurations,
and training records to `WSM_v1/train_log/`, `WSM_v1/train_log_sparse/`, and
`WSM_v1/train_log_custom/`:

- [[WSM v1 post-training materials]](https://huggingface.co/World-Snapshot/WSM_v1-Training-Resources)

## Data and Training

We open-source the data, training states, optimizer, and training logs. If you want to train it yourself, download the released data to `WSM_v1/data/`:

- [[WSM v1 Latent PT / WSG v1.8 for FLUX.2]](https://huggingface.co/datasets/World-Snapshot/WSM_v1_Latent_PT_WSG_v1.8_for_Flux2)

This data contains latent representations of geometry, motion, human structure, object structure, physics, materials, PBR attributes, audio, language, semantics, and sparse observations. Training the released task paths does not require downloading all original source datasets.

Run under `WSM_v1/`:

```bash
# Train a dense task path, for example RGB → Normal.
WSG_CHANNEL_HEAD_INDEX=3 bash scripts/launch_scripts/train_dense_structure_models.sh

# Train the official sparse task set.
bash scripts/launch_scripts/train_sparse_structure_models.sh
```

![WSG task graph and the four generative interfaces.](assets/wsg_task_graph_v3.png)

*Figure: **WSG task graph and the four generative interfaces.** RGB is the center of the visual task space. Text enters from the bottom and generates RGB; WSG modalities surround RGB as target or condition nodes. Each directed arrow is a trainable Channel Head parsed from the WSG modality graph. Arrow color indicates the task type: visual generation, estimation/reconstruction, conditional control, text-guided conditional generation, or inverse rendering. Dashed arrows denote Chain of Visual, where text can reach non-RGB World Snapshot modalities through generated World Snapshots. Blue-outline nodes are dense WSG/visual targets, and orange-outline nodes are sparse digitized targets such as boxes, body parameters, skeletons, keypoints, or audio tokens. [Dense Task Graph](WSM_v1/configs/wsg_v1_modalities_dense.json) · [Sparse Task Graph](WSM_v1/configs/wsg_v1_modalities_sparse.json) · [Custom Task Graph](WSM_v1/configs/wsg_v1_modalities_custom.json)*

Model paths, data roots, GPU allocation, training steps, and validation intervals can all be set through environment variables.

## Custom Training

<details>
<summary><strong>Build your own task tunnel</strong></summary>

A Channel Head (Tunnel Head) is one directed task tunnel. Building a new one requires an aligned condition–target dataset, FLUX.2 VAE latents for both sides, and one entry in a task-graph JSON. The shared generator does not need to be retrained from scratch.

See the complete custom-Head example: [`train_custom_structure_example.sh`](WSM_v1/scripts/launch_scripts/train_custom_structure_example.sh).

### 1. Encode aligned variables

Place the latent cache under `WSM_v1/data/`. Each node has its own shard directory, while paired nodes share the same sample IDs, frame indices, crop, and train/validation split:

```text
data/my_task_latents/
└── shards/
    ├── surface_normal/
    │   ├── shard_00000_of_00008.pt
    │   └── ...
    └── custom_depth/
        ├── shard_00000_of_00008.pt
        └── ...
```

Each shard contains the VAE `latents` and aligned metadata such as `sample_ids`, `frame_indices`, and `sample_sources`. The released cache is a direct template. For variables already stored in `.wsg`, use [`precompute_wsg_flux_frame_multidataset_cache.sh`](WSM_v1/manual_processing/flux2_preprocessing/cache/precompute_wsg_flux_frame_multidataset_cache.sh) to normalize, crop, encode, and shard them with the same FLUX.2 VAE used by WSM.

### 2. Define the task tunnel

Add the task to the persistent custom graph at [`WSM_v1/configs/wsg_v1_modalities_custom.json`](WSM_v1/configs/wsg_v1_modalities_custom.json):

```json
{
  "normalization": {
    "default_mode": "linear",
    "channel_ranges": {}
  },
  "wsg_v1": {
    "Channel_Head_009999": {
      "task_type": "conditional_control",
      "pair_exists": true,
      "condition": "surface_normal",
      "condition_description": "Surface normal",
      "target": "custom_depth",
      "target_description": "Custom depth"
    }
  }
}
```

Node identifiers in the graph are strings. The official graph uses identifiers such as `0-2` and `36-38` because they bind directly to WSG channels 0–2 and 36–38. A pre-encoded custom cache may instead use descriptive identifiers such as `surface_normal`, provided the JSON identifier and shard-directory name match. Such a name is a graph/cache identifier; it does not consume or redefine one of the 256 WSG channels. Direct extraction from `.wsg` and official WSG Reader visualization still require a numeric channel range, or a custom extractor and reader for that node.

`condition` may be one string or a list of strings for a multi-condition tunnel. A single JSON may contain any number of `Channel_Head_XXXXXX` entries, so a user-defined modality set can generate an entire directed task graph rather than one isolated task.

### 3. Train the Channel Head

Run the standard queue launcher with the custom graph, cache, and Head index. The queue reads `task_type` from the JSON, applies the corresponding attention and trainability recipe, and then launches the single-Head trainer:

```bash
cd WSM_v1

MODALITY_CONFIG=configs/wsg_v1_modalities_custom.json \
WSG_DENSE_LATENT_CACHE_DIR=data/my_task_latents \
CHANNEL_HEAD_LIST=3 \
GPU_IDS=0 \
MAX_ACTIVE=1 \
WSG_QUEUE_SKIP_EXISTING=0 \
MAX_STEPS=1000 \
bash scripts/launch_scripts/train_all_dense_structure_models_queue.sh
```

The resulting run is written under `WSM_v1/train_log_custom/Channel_Head_000003/`. To train a task bank, add more entries to the same JSON and pass their comma-separated Head indices through `CHANNEL_HEAD_LIST`; the queue schedules them in parallel across `GPU_IDS`.

The task type does not by itself determine every loss. A target that is mostly black background with sparse foreground structure—such as a pose skeleton or thin boundary map—can minimize ordinary pixel/latent regression by predicting the background. Train such a Head separately with a gradient-domain loss:

```bash
MODALITY_CONFIG=configs/wsg_v1_modalities_custom.json \
WSG_DENSE_LATENT_CACHE_DIR=data/my_task_latents \
CHANNEL_HEAD_LIST=3 \
GPU_IDS=0 \
MAX_ACTIVE=1 \
WSG_QUEUE_SKIP_EXISTING=0 \
WSG_GRADIENT_DOMAIN_LOSS_WEIGHT=0.1 \
bash scripts/launch_scripts/train_all_dense_structure_models_queue.sh
```

For a recurring official or custom sparse-pose target, add its target identifier to `pose_map_targets` in `train_all_dense_structure_models_queue.sh`; the queue will then select the `pose-map-gradient` recipe automatically. Dense RGB and ordinary continuous targets should retain their normal loss unless an ablation demonstrates otherwise.

*We suggest trying custom example Head1 (similar to LayerDiffuse) and Head2 (similar to the ICLR full-score paper IC-Relight). We quickly went through these two well-known works in just a few hours as a demonstration of our capability. Although our reproduction wasn't perfect, we've shown that even the most outstanding works are merely two insignificant examples among thousands of features/tasks offered by WSM.*

</details>

## Inference

After installing `wsms`, a released task tunnel can be loaded directly by its
ordered input and output modalities:

```python
from wsms import WSMPipeline

pipe = WSMPipeline.from_pretrained(
    "World-Snapshot/WSM_v1",
    inputs=["0-2"],
    output="36-38",
    device="cuda:0",
)
result = pipe("input.png", num_inference_steps=10)
result.images[0].save("normal.png")
```

The Hub release is one `WSM_v1.wsm` checkpoint containing the complete frozen
backbone and its built-in, sparsely activated TunnelingNets. The pipeline reads
its index and caches only the shared backbone plus the selected task; legacy
local checkpoints remain supported by the same API, as do legacy split-layout
Hub repositories.

See the [complete pip and Pipeline guide](PYPI_README.md) for task discovery,
multi-input tunnels, private-model authentication, local loading, outputs, and
all command-line options.

<details>
<summary><strong>Command-line inference</strong></summary>

WSM provides two command-line inference paths at different stages of the input
pipeline. [`infer_TunnelingNet_Flux2_4B_wsg.py`](WSM_v1/scripts/infer_TunnelingNet_Flux2_4B_wsg.py)
is the public entry for raw user inputs: it validates RGB, WSG, and audio files,
applies the training-time crop and normalization contracts, performs VAE
encoding, restores the selected Head, and generates the target modality. In
contrast, `train_TunnelingNet_Flux2_4B_wsg.py --inference-only` starts from
samples that have already been aligned, normalized, and VAE-encoded in the
latent cache. It is intended for fixed-sample reproduction and quantitative
evaluation and does not accept arbitrary local input files.

The public inference entry restores the Head architecture, modality prompt,
attention routing, trainable branches, and optional refiners from the
configuration stored beside the checkpoint. The following example runs the
released RGB-to-normal Head on a local image:

```bash
cd WSM_v1

CUDA_VISIBLE_DEVICES=0 python scripts/infer_TunnelingNet_Flux2_4B_wsg.py \
  --checkpoint train_log/Channel_Head_000003/20260809_231823_q_20260809-161033/ckpt/0001780/pytorch_lora_weights.safetensors \
  --input 0-2=/absolute/path/to/rgb.png \
  --prompt "A person standing in a room" \
  --steps 10 \
  --seed 20260812 \
  --output-dir inference_output/rgb_to_normal
```

The selected output is saved as `result.png`. The same directory contains the
raw generated WSG snapshot, native pseudo-RGB decode, WSG Reader outputs,
refiner records when applicable, and `result_manifest.json`.

Pass one `--input TOKEN=PATH` for every condition required by the Head. Inputs
are reordered to the training-time condition order automatically. For example,
a Head using an edge condition and a native RGB reference is invoked with:

```bash
--input 40=/absolute/path/to/edge.wsg.npz \
--input Reference_IMG=/absolute/path/to/reference.png
```

RGB tokens accept PNG, JPEG, or WebP images as well as raw `.wsg`, `.npz`,
or `.npy` files containing channels 0–2. Non-RGB modalities require raw
`.wsg`, `.npz`, or `.npy` values; WSG Reader visualizations must not be used as
model inputs. WAV files are recognized as audio. The optional explicit form
`TOKEN:image=PATH`, `TOKEN:wsg=PATH`, or `TOKEN:audio=PATH` is available for
custom modality identifiers. Dense Head tokens and deployment checkpoints are listed in
[`wsm_v1_recommended_dense_channel_heads.json`](WSM_v1/configs/wsm_v1_recommended_dense_channel_heads.json). Because the sparse and custom graphs contain only a small number of Heads, each validated entry stores its own `recommended_checkpoint` directly in
[`wsg_v1_modalities_sparse.json`](WSM_v1/configs/wsg_v1_modalities_sparse.json) or
[`wsg_v1_modalities_custom.json`](WSM_v1/configs/wsg_v1_modalities_custom.json).

WSM can also act as its own condition preprocessor. If a user has an RGB image
but not the raw non-RGB modality required by the selected Head, replace that
input's `--input` argument with `--self-preprocess TOKEN=RGB_PATH`. The script
selects the official RGB-to-TOKEN Head, estimates the modality, saves its raw
`generated.wsg.npz`, and passes those values directly to the final Head. For
example, the following chain estimates curvature channel 39 from RGB before
running a curvature-conditioned Head:

```bash
CUDA_VISIBLE_DEVICES=0 python scripts/infer_TunnelingNet_Flux2_4B_wsg.py \
  --checkpoint train_log/Channel_Head_000349/20260809_231942_q_20260809-161033/ckpt/0001740/pytorch_lora_weights.safetensors \
  --self-preprocess 39=/absolute/path/to/rgb.png \
  --steps 10 \
  --output-dir inference_output/self_preprocessed_curvature
```

The same entry point exposes the complete Chain of Visual from text through a
generated RGB image to a non-RGB target. Select an RGB-to-modality Head and add
`--chain-of-visual` (an alias of `--text-to-modality`):

```bash
CUDA_VISIBLE_DEVICES=0 python scripts/infer_TunnelingNet_Flux2_4B_wsg.py \
  --checkpoint train_log/Channel_Head_000003/20260809_231823_q_20260809-161033/ckpt/0001780/pytorch_lora_weights.safetensors \
  --chain-of-visual \
  --prompt "A person standing in a room" \
  --steps 10 \
  --output-dir inference_output/text_to_normal
```

Both composed routes retain their intermediate RGB or WSG artifact and include
it in `result_manifest.json` beside the final output.

The cache-based `--inference-only` mode supports `--preview-sample-id`,
`--preview-sample-id-file`, and deterministic test-split sampling and is also
used by the internal quantitative evaluator. ControlWorld calls the public
raw-input inference entry through its JSON request mode, so command-line and
WebUI inference share the same input validation, encoding, routing, decoding,
and artifact generation code.

</details>

## Evaluation

Use the following command to evaluate the released tasks:

```bash
cd WSM_v1

python src/evaluation/evaluate_channel_heads.py \
  --head-source recommended \
  --all-heads \
  --samples-per-head 24 \
  --inference-steps 10 \
  --devices 0,1,2,3,4,5,6,7 \
  --experiment-name wsm_v1_release_evaluation
```

Results are saved in `WSM_v1/src/evaluation_output/`, including metrics, tables, logs, and generated samples.

## WebUI

[ControlWorld](https://github.com/World-Snapshot/ControlWorld) is the reference WebUI for WSM. It selects tasks from the WSG Task Graph, obtains the required conditions, loads the model, runs inference, and displays the results using the WSG Reader corresponding to the target modality.

Paper Demo publishes the qualitative examples from Figures 14–39 as scoped raw
`.wsg.npz` inputs. Each file contains only the channels consumed by its Head,
together with their global WSG channel IDs. The image at the top of each input
cell is a display-only WSG Reader visualization; the compact file card below it
is the input that is validated, cropped, normalized, and VAE-encoded when the
user runs the example. Outside Paper Demo, raw tensor uploads receive a fast
pseudo-RGB preview while the uploaded WSG/NPZ/NPY remains the model input.
For a non-RGB input that has a released RGB estimation Head, its input card
also provides a **WSM Self-Preprocessor** switch. Enabling it changes that card
to an RGB upload; ControlWorld passes the request to the same public inference
script described above, which estimates raw WSG values before running the
selected task. No external depth, edge, normal, pose, or segmentation
preprocessor is required.

## BibTex

```code
@misc{fang2026unifiedlawvisualtasks,
      title={Unified Law for Visual Tasks (The Four Laws of Computer Vision)}, 
      author={Sen Fang and Yalin Feng and Yancheng Zhang and Yanxin Zhang and Zonglin Lyu and Hongbin Zhong and Liwei Che and Rui Wu and Chen Chen and Dimitris N. Metaxas},
      year={2026},
      eprint={2611.24917},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2611.24917}, 
}
```

## License

**In short:** You are welcome to use, study, modify, and extend this project
for noncommercial purposes, including research, experimentation, development,
training, evaluation, education, and personal projects. Commercial use
requires separate permission from Rutgers; contact
**compliance@research.rutgers.edu** and reference **Rutgers Docket #2027-020**.
The [LICENSE](LICENSE) file contains the governing terms.

WSMs is available under the Rutgers Non-commercial Research License (RU-NCRL)
for academic, research, experimental, and personal noncommercial purposes.
For commercial-use rights, contact **compliance@research.rutgers.edu** and
reference **Rutgers Docket #2027-020**.

Any Rutgers-owned model artifacts distributed with this repository, including
trained or fine-tuned weights, checkpoints, adapters, and `.pth` files, are
covered by the same license. Third-party dependencies and model artifacts
retain their respective licenses.

---

Classification, localization, detection, segmentation, estimation, reconstruction, restoration, completion, registration, correspondence, tracking, retrieval, indexing, prediction, generation, editing, rendering, simulation, planning, and control... are all within the scope we unify. This is the emperor model of Computer Vision, hence the codename Augustus.

***A model that encompasses all and can do everything is gradually taking shape out of chaos; Computer Vision is therefore reborn.***
