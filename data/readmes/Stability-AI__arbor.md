<div align="center">

# Arbor

**Explicit Geometric Conditioning for Controllable 3D Asset Generation**

<img src="docs/assets/arbor_teaser.jpg" alt="Arbor teaser" width="100%">

🌐 [Project Page](https://arbor.jdihlmann.com/) &nbsp;|&nbsp;
📄 [Paper](https://arbor.jdihlmann.com/downloads/arbor_paper.pdf) &nbsp;|&nbsp;
🤗 [Hugging Face Model](https://huggingface.co/StabilityLabs/arbor) &nbsp;|&nbsp;
🔌 [Blender Add-on](#blender-add-on) &nbsp;|&nbsp;
✍️ [Citation](https://github.com/Stability-AI/arbor#citation)

</div>

## About

Arbor is an inference-only release for text-to-3D generation with explicit geometry controls. You provide a prompt and constraint meshes; Arbor generates a 3D asset that follows those constraints while using the TRELLIS mesh decoder for the final output.

The release contains the public inference pipeline, model loading, mesh export, condition metrics, rendering utilities, and curated examples. Training code, dataset construction, benchmark launchers, and internal evaluation wrappers are not included.

Arbor uses three constraint signals:

| Signal | Color | Meaning |
| --- | --- | --- |
| `hull` | green | Geometry should occupy or follow this region. At least one hull mesh is required. |
| `avoidance` | red | Geometry should avoid this region. |
| `touch` | yellow | Geometry should stay touchable or contact-compatible here. |

Constraint meshes should be watertight or near-watertight triangle meshes in the same coordinate frame. The examples use PLY files in TRELLIS-style normalized object coordinates.

## Installation

The commands below install Arbor, download the public model files, and run a first example. Linux with an NVIDIA GPU is required. The reference setup uses Python 3.10, PyTorch 2.4.0, CUDA 11.8, `spconv`, and the vendored `o_voxel` extension.

### Packages

```bash
git clone https://github.com/Stability-AI/arbor.git
cd arbor

conda create -n arbor python=3.10 -y
conda activate arbor
conda install pytorch==2.4.0 torchvision==0.19.0 pytorch-cuda=11.8 -c pytorch -c nvidia -y

./setup.sh --basic --xformers --spconv
```

If your system needs a custom OpenSSL runtime, set `LD_LIBRARY_PATH` before running inference.

### Model

Model files are hosted at [StabilityLabs/arbor](https://huggingface.co/StabilityLabs/arbor). Authenticate if the repository is private or gated for your account:

```bash
hf auth login
hf auth whoami
```

For non-interactive shells, pass a token without saving it in shell history:

```bash
read -s HF_TOKEN
hf auth login --token "$HF_TOKEN"
unset HF_TOKEN
hf auth whoami
```

Download the Arbor model files:

```bash
python scripts/download_model_from_hf.py \
  --repo-id StabilityLabs/arbor \
  --output-dir artifacts/model
```

The inference CLI also downloads missing default artifacts on first use unless `--no-download` is passed.

### Quick Start

Run a curated example and render the public condition report:

```bash
python examples/run_manual_example.py \
  --example chair_080 \
  --output-root outputs/manual_examples \
  --steps 50 \
  --evaluate
```

Run Arbor directly with your own constraints:

```bash
arbor-infer \
  --prompt "A classic red double-decker bus with rounded edges and black rectangular windows." \
  --hull examples/constraints/bus__bus_013__19cbb410/hull_constraint.ply \
  --avoidance examples/constraints/bus__bus_013__19cbb410/avoidance_constraint.ply \
  --touch examples/constraints/bus__bus_013__19cbb410/touchable_constraint.ply \
  --output-dir outputs/bus_013 \
  --seed 1 \
  --steps 50
```

Use the Python API when you want to integrate Arbor into your own tool:

```python
from pathlib import Path
from arbor import ArborPipeline, ConstraintSet

pipeline = ArborPipeline(model_dir="artifacts/model")
result = pipeline.run(
    prompt="A small red toy piano with a rounded rectangular body.",
    constraints=ConstraintSet(
        hull=(Path("examples/constraints/piano__piano_038__8a941e90/hull_constraint.ply"),),
    ),
    output_dir="outputs/piano_038",
    seed=1,
)
print(result.mesh_path)
```

Curated examples use the seed stored in `examples/manual_examples.json`. `chair_080` uses seed 5 by default. Pass `--seed` if you want a different sample.

## Results

Arbor writes standard mesh outputs and optional inspection reports. The reports are meant to make the condition-following behavior easy to inspect without the internal training or benchmark code.

### Outputs

Each generation run writes:

- `mesh.ply`: final generated mesh when decoding succeeds.
- `ss_surface.npz`: generated sparse-structure occupancy grid.
- `generation_info.json`: prompt, seed, model names, sampler settings, token statistics, and signal statistics.

Reference meshes are not used for generation. They are only used by the evaluator when you want extra comparison metrics.

### Examples

The release includes four curated examples from the manual constraint set.

![Arbor demo examples](docs/assets/demo_examples.png)

```bash
python examples/run_manual_example.py --example bus_013 --output-root outputs/manual_examples --evaluate
python examples/run_manual_example.py --example chair_080 --output-root outputs/manual_examples --evaluate
python examples/run_manual_example.py --example piano_038 --output-root outputs/manual_examples --evaluate
python examples/run_manual_example.py --example sink_015 --output-root outputs/manual_examples --evaluate
```

Example constraint coverage:

- `bus_013`: hull, avoidance, and touch.
- `chair_080`: hull and touch.
- `piano_038`: hull.
- `sink_015`: hull and avoidance.

### Evaluation

`arbor-evaluate` computes public condition metrics and renders a labeled four-view panel.

```bash
arbor-evaluate \
  --prediction outputs/manual_examples/bus_013/mesh.ply \
  --hull examples/constraints/bus__bus_013__19cbb410/hull_constraint.ply \
  --avoidance examples/constraints/bus__bus_013__19cbb410/avoidance_constraint.ply \
  --touch examples/constraints/bus__bus_013__19cbb410/touchable_constraint.ply \
  --reference-mesh examples/constraints/bus__bus_013__19cbb410/gt_mesh.ply \
  --sparse-structure outputs/manual_examples/bus_013/ss_surface.npz \
  --output-dir outputs/manual_examples/bus_013/evaluation
```

`--reference-mesh` is optional. It adds reference metrics such as Chamfer distance and F-score. It is not required for inference and does not change the generated mesh.

Evaluation writes:

- `metrics.json`: nested condition metrics and command metadata.
- `metrics_flat.json`: flattened metrics for scripts or spreadsheets.
- `condition_panel.png`: prediction normals, signal-colored constraints, condition-obedience coloring, and metric summary.
- `condition_orbit.gif`: optional orbit render when `--save-gif` is passed.

The main metric groups are hull overlap, avoidance violations, touch contact, optional reference metrics, and optional sparse-structure metrics.

## Blender Add-on

Arbor can be used as a CLI, a Python library, or directly from Blender. The Blender workflow ships as part of this repository:

- Downloadable add-on zip: [tools/blender_addons/arbor_blender_bridge.zip](tools/blender_addons/arbor_blender_bridge.zip)
- Add-on source: [tools/blender_addons/arbor_blender_bridge](tools/blender_addons/arbor_blender_bridge)
- Bridge server entry point: `arbor-bridge-server`

There is only one canonical Blender install artifact in the repo: `tools/blender_addons/arbor_blender_bridge.zip`. The bridge server is part of Arbor itself and does not require a separate download.

Install the add-on in Blender:

1. Open `Edit > Preferences > Add-ons`.
2. Click `Install...`.
3. Select `tools/blender_addons/arbor_blender_bridge.zip`.
4. Enable `Arbor Blender Bridge`.

Start the matching bridge server from the same Arbor checkout:

```bash
arbor-bridge-server --host 127.0.0.1 --port 8765
```

If you prefer to launch it from the repo without installing console scripts:

```bash
./scripts/start_blender_bridge.sh --host 127.0.0.1 --port 8765
```

Typical Blender workflow:

1. Assign selected meshes to `Hull`, `Avoidance`, `Touchable`, or `None`.
2. Enter the prompt, base seed, and number of variants.
3. Use `Check Server` once to verify the bridge is reachable.
4. Submit the job.
5. Completed variants are downloaded and auto-imported into a dedicated Blender collection.

For a simple mesh-only workflow without the add-on, you can still import `outputs/<run>/mesh.ply` manually via `File > Import > Stanford (.ply)`.

### Best Practices

Use normalized object space. Arbor follows constraints inside the normalized TRELLIS object box; it does not generate in metric world units.

TRELLIS has a strong object prior: it tends to center the asset and make the asset use the available box. Treat constraints as relative shape controls inside that box. If one constrained region grows, another part can look smaller because the final object is still normalized to the same space. For example, a taller chair back may require lowering or shrinking the seat region, not only raising the back in absolute space.

Keep constraint meshes simple at first. Start with a hull, add avoidance only where empty space matters, then add touch surfaces where contact is important. Run `arbor-evaluate` after generation to see which constraints were followed and which regions need adjustment.

## License and Attribution

This code and model usage are subject to the Stability AI Community License terms. See `LICENSE` and the Hugging Face model card for details. Arbor builds on TRELLIS and TRELLIS.2 components; retained third-party notices are included under `third_party/o_voxel/`.

## Citation

```bibtex
@misc{dihlmann2026arbor,
  author = {Dihlmann, Jan-Niklas and Engelhardt, Andreas and Donne, Simon and Lensch, Hendrik and Boss, Mark},
  title = {Arbor: Explicit Geometric Conditioning for Controllable 3D Asset Generation},
  booktitle = {Preprint},
  year = {2026}
}
```
