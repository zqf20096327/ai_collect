# Origami Box Pleating (`bp_pipeline`)

Automated Box-Pleating Origami Packing, Crease Pattern Solving, 3D Shaping, and
Global Flat-Foldability Verification.

**Paper:** [**COrigami: An AI Pipeline for Co-Designing Flat-Foldable Visually Recognisable Origami**](https://arxiv.org/abs/2606.26299) (`arXiv:2606.26299`)

**Studio:**
[COrigami Studio](https://google-deepmind.github.io/origami-design/) folds and
unfolds the showcase models below in the browser, next to their crease
patterns, packings and stick figures. It also opens the `shaped_3d.fold` that
`bp-pipeline -o` writes for a design of your own.

## Showcase

Precomputed showcase models; each opens in the studio.

> **Reproducibility note:** The ten bundled showcase models under `docs/models/`
> are precomputed snapshots produced in earlier interactive shaping sessions
> whose tool-call histories were **not recorded**. They **cannot be
> regenerated** by running `bp-pipeline` on their `stick_figure.json` files
> alone. (One model, `wyrmlord-dragon`, also had a single missing corner face —
> 1 vertex, 2 border edges, 0.41% of the sheet — patched to close a 0.001-unit
> border gap in its source crease pattern.) Fresh designs written by
> `bp-pipeline FIGURE -o out/` produce a compatible `shaped_3d.fold` that the
> studio loads directly.

<!-- disableFinding(LINE_OVER_80) -->

| [![Golden Eagle](docs/models/golden-eagle/preview.png)<br>Golden Eagle](https://google-deepmind.github.io/origami-design/?model=golden-eagle) | [![Winged Pegasus](docs/models/winged-pegasus/preview.png)<br>Winged Pegasus](https://google-deepmind.github.io/origami-design/?model=winged-pegasus) | [![Triceratops](docs/models/triceratops/preview.png)<br>Triceratops](https://google-deepmind.github.io/origami-design/?model=triceratops) | [![Western Dragon](docs/models/wyrmlord-dragon/preview.png)<br>Western Dragon](https://google-deepmind.github.io/origami-design/?model=wyrmlord-dragon) | [![King Cobra](docs/models/king-cobra/preview.png)<br>King Cobra](https://google-deepmind.github.io/origami-design/?model=king-cobra) |
| :---: | :---: | :---: | :---: | :---: |
| [![Emperor Scorpion](docs/models/emperor-scorpion/preview.png)<br>Emperor Scorpion](https://google-deepmind.github.io/origami-design/?model=emperor-scorpion) | [![Boxer Crab](docs/models/boxer-crab/preview.png)<br>Boxer Crab](https://google-deepmind.github.io/origami-design/?model=boxer-crab) | [![Bull Moose](docs/models/bull-moose/preview.png)<br>Bull Moose](https://google-deepmind.github.io/origami-design/?model=bull-moose) | [![Indian Peacock](docs/models/indian-peacock/preview.png)<br>Indian Peacock](https://google-deepmind.github.io/origami-design/?model=indian-peacock) | [![Crested Hoopoe](docs/models/crested-hoopoe/preview.png)<br>Crested Hoopoe](https://google-deepmind.github.io/origami-design/?model=crested-hoopoe) |

<!-- enableFinding(LINE_OVER_80) -->

The studio is the static site under [`docs/`](docs/). A showcase model is a
directory `docs/models/<slug>/` with three files:

-   `shaped_3d.fold`, in the extended [FOLD](https://github.com/edemaine/fold)
    v1.1 layout that `bp-pipeline -o` writes (`file_frames[0]` plus the `bp:`
    keys; see the canonical schema in
    [`src/bp_pipeline/render_3d.py`](src/bp_pipeline/render_3d.py)
    `mesh_to_fold_dict`);
-   `stick_figure.json`, the stick figure it was designed from;
-   `preview.png`, a 4:3 picture for the gallery.

To add one, also give it an entry in
[`docs/models/catalog.json`](docs/models/catalog.json) with what the files do
not say: `slug`, `title`, `subtitle`, `summary`, `techniques`, the paper
colors `colorTop` and `colorBottom`, and the `camera` angles of the opening
view. Run `python3 -m http.server -d docs` to try the site locally.

## Overview

`bp_pipeline` (`bp`) is a standalone Python library and CLI accompanying the
[COrigami paper](https://arxiv.org/abs/2606.26299) for converting metric 3D tree
skeletons (`StickFigure`) into globally flat-foldable box-pleated origami crease
patterns (`CreasePattern`) and shaded 3D shaped models:

1.  **Unified Pipeline Bus, CLI & Visual Suite (`bp-pipeline` / `import bp_pipeline as bp`)**:
    -   Immutable stage records (`DesignTree` -> `PackedCreasePattern` ->
        `SolvedCreasePattern` -> `ShapedCreasePattern`), one-call `bp.fold()`,
        modular `bp.prepare()` / `bp.pack()` / `bp.solve()` /
        `bp.solve_best()` / `bp.shape()`, out-of-the-box 2D/3D turnaround and
        stage-summary visualizers (`bp.save_stick_figure_views()`,
        `bp.save_pipeline_summary()`, `bp.save_3d_turnaround()`,
        `bp.render_packing_grid()`), lossless JSON serialization (`bp.dumps()` /
        `bp.loads()`), and the `bp-pipeline` command-line tool.
2.  **Stick Figures (`bp_pipeline.stick_figures`)**:
    -   Tree validation, linear-chain merging, symmetry detection, and 47
        canonical example stick figures (`bp.list_examples()`,
        `bp.load_example()`).
3.  **Box-Pleating Packing (`bp_pipeline.packing`)**:
    -   Constraint-guided backtracking search for flap circles and river routing
        on an integer square grid.
4.  **Crease Pattern Solving (`bp_pipeline.solving`)**:
    -   Partition-ordered hinge assignment and mountain/valley flat-foldable
        crease pattern synthesis (`hinges.SolverConfig`) with streaming solution
        discovery (`bp.solve()`).
5.  **Global Flat-Foldability Simulator
    (`bp_pipeline.third_party.flat_folder`)**:
    -   Pure-Python global flat-foldability verification ported from Jason S.
        Ku's MIT-licensed
        [Flat-Folder](https://github.com/origamimagiro/flat-folder) software.
6.  **3D Origami Shaping, Pose Recipes & Bundled Agent Design Skills**:
    -   3D geometric simple-fold and river-bend shaping (`bp.shape()`),
        closed-loop automatic posing (`bp.pose()`, `bp.PoseConfig`), a 19-tool
        stateful shaping toolbox (`bp.ShapingState`, `bp.apply_shaping_tool()`,
        `bp.list_shaping_tools()`), quantitative pose fidelity scoring
        (`bp.evaluate_fidelity()`), dihedral hinge-mesh folding
        (`bp.build_folded_mesh_3d()`), and portable AI agent skills under
        `.agents/`.

### Pipeline Architecture & Immutable Bus

```
StickFigure / JSON / Example Name ('human', 'scorpion', 'cat', 'spider')
        │
        ▼  bp.prepare(...)
   DesignTree                 (source + merged StickFigure, symmetry, grid bounds)
        │
        ├──► bp.save_stick_figure_views(design, ...) ──► stick_figure_views.png
        │
        ▼  bp.pack(...)  or  bp.stack(...)
PackedCreasePattern           (integer grid_size, Flaps, Rivers, Hinges)
        │
        ▼  bp.solve_best(...)  or  bp.solve_sweep(...)
SolvedCreasePattern           (flat-foldable MV CreasePattern, SolveStats)
        │
        ├──► bp.to_svg(...) / solved.to_svg()        ──► .svg
        ├──► bp.to_fold(solved)                      ──► .fold (FOLD v1.2)
        ├──► bp.to_bp_studio(packed)                 ──► .bps.json
        ├──► bp.render_packing_grid([solved])        ──► contact_sheet.html
        ├──► solved.flat_fold()                      ──► FOLD dict (uniaxial base)
        │
        ▼  bp.shape(...)
ShapedCreasePattern           (3D geometric simple folds and river bends)
        │
        ├──► shaped.to_svg()                         ──► .svg
        ├──► bp.to_fold(shaped)                      ──► .fold
        ├──► bp.save_3d_turnaround(shaped, ...)      ──► shaped_3d_views.png
        └──► bp.save_pipeline_summary(..., shaped=.) ──► pipeline_stages.png
```

## Installation

Requires **Python 3.14+**. Visualization dependencies (`matplotlib`, `plotly`)
and the `bp-pipeline` CLI are installed by default to support the full visual
design loop out of the box.

With [`uv`](https://docs.astral.sh/uv/) (automatically downloads a standalone
Python 3.14 runtime if `python3.14` is not installed on your system):

```bash
git clone https://github.com/google-deepmind/origami-design.git
cd origami-design
uv sync --python 3.14
uv run pytest
```

Or with standard `venv` and `pip` (if your OS ships an older system Python,
install Python 3.14 first via `pyenv install 3.14`, Homebrew `brew install
python@3.14`, Ubuntu/Debian `ppa:deadsnakes/ppa` `python3.14-venv`, or official
installers from [python.org](https://www.python.org/downloads/)):

```bash
git clone https://github.com/google-deepmind/origami-design.git
cd origami-design
python3.14 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

## Usage

### 1. End-to-End `bp-pipeline` CLI & Visual Design Workflow

Run `bp-pipeline` (or `python -m bp_pipeline`) on any of the 47 built-in
examples or on a custom `StickFigure` JSON file:

```bash
# List all 47 built-in stick-figure examples:
bp-pipeline --list-examples

# Run packing, solving, 3D shaping, and visual rendering on a built-in example:
bp-pipeline cat -o outputs/cat

# Validate bilateral symmetry and run end-to-end on a custom StickFigure JSON:
bp-pipeline .agents/skills/stick-figure-design/examples/cat.json \
  -o outputs/cat \
  --check-symmetry

# Automatically pose, refine with actuators, and score fidelity:
bp-pipeline pose outputs/cat --mode auto
bp-pipeline actuate outputs/cat --tool fold_spine --args '{"fold_percent": 0.65}'
bp-pipeline score outputs/cat
```

When `-o` / `--output-dir` is provided, `bp-pipeline` automatically renders the
full visual inspection suite alongside `.bps.json`, `.fold`, `shaped_3d.fold`,
`.svg`, and `report.json` (pass `--no-viz` for headless export-only runs):

-   `stick_figure_views.png` — 4-view (`top`, `side`, `front`, `isometric`)
    skeleton projection sheet for verifying limb geometry before packing.
-   `pipeline_stages.png` — 5-panel overview comparing Packed CP, Solved Base
    CP, Uniaxial Folded Base, Shaped CP, and Isometric 3D Shaped Figure.
-   `shaped_3d_views.png` — **4-angle shaded 3D origami turnaround** (`Iso`,
    `Side`, `Front`, `Top`) folded at partial dihedral angles (`fold_percent *
    ±180°`), recommended as the primary visual check when iterating on 3D poses.
-   `contact_sheet.html` — Self-contained interactive HTML contact sheet with
    layer toggles for flaps, rivers, hinges, labels, circle centers, and grid.

### 2. Tier 1 Python API — One-Call Fold & Visual Inspection (`bp.fold`)

```python
import bp_pipeline as bp

result = bp.fold('cat', preset='demo', shape=True)
print('Packed grid size:', result.packed.grid_size)
print('Globally flat-foldable:', result.solved.is_globally_flat_foldable)

# Render shaded 3D turnaround PNG, 5-panel stage summary, or HTML contact sheet:
result.save_3d_turnaround('outputs/cat/shaped_3d_views.png')
result.save_pipeline_summary('outputs/cat/pipeline_stages.png')
grid_html = bp.render_packing_grid([result.solved])

# Export to SVG, FOLD dictionary, or lossless JSON:
svg_str = result.solved.to_svg()
fold_dict = result.solved.flat_fold()
json_str = bp.dumps(result.solved)
restored = bp.loads(json_str)
```

### 3. Tier 2 Python API — Modular Pipeline (`bp.prepare` -> `bp.pack` -> `bp.solve_best` -> `bp.shape`)

```python
import bp_pipeline as bp

design = bp.prepare('human')
bp.save_stick_figure_views(design, 'outputs/human/stick_figure_views.png')

packed = bp.pack(design)
solved = bp.solve_best(packed)
shaped = bp.shape(solved)

# Inspect the 3D folded pose and full pipeline progression:
bp.save_3d_turnaround(shaped, 'outputs/human/shaped_3d_views.png')
bp.save_pipeline_summary(
    'outputs/human/pipeline_stages.png',
    packed=packed,
    solved=solved,
    shaped=shaped,
)

# Or stream candidate crease patterns as the solver discovers them:
for candidate in bp.solve(packed):
  if candidate.is_globally_flat_foldable:
    break
```

### 4. Bundled Agent Design Skills

Five portable AI agent skills and an end-to-end designer agent definition are
bundled under `.agents/` for automatic discovery in coding-agent harnesses when
working inside a repository checkout:

-   [`.agents/agents/origami-designer.md`](.agents/agents/origami-designer.md):
    End-to-end workflow orchestrating design, solving, posing, actuation, and
    critique.
-   [`.agents/skills/stick-figure-design/SKILL.md`](.agents/skills/stick-figure-design/SKILL.md):
    Canonical workflow, schema, archetypes, and `bp-pipeline` CLI
    validation/rendering loop for authoring 3D `StickFigure` JSONs.
-   [`.agents/skills/stick-figure-generation/SKILL.md`](.agents/skills/stick-figure-generation/SKILL.md):
    Spherical coordinate math, programmatic Python validation, and river
    equivalence-class heuristics.
-   [`.agents/skills/origami-solving-pipeline/SKILL.md`](.agents/skills/origami-solving-pipeline/SKILL.md):
    Reference for `bp.prepare`, `bp.pack`, `bp.solve_best`,
    `bp.solve_sweep`, `bp.fold`, and export formats.
-   [`.agents/skills/origami-shaping/SKILL.md`](.agents/skills/origami-shaping/SKILL.md): Guide
    to automatic posing (`bp.pose`), the 19-tool shaping toolbox
    (`bp.apply_shaping_tool`), one-shot shaping (`bp.shape`), and 3D limb
    subdivision (with `references/tools.md` and `references/pose.md`).
-   [`.agents/skills/origami-critique/SKILL.md`](.agents/skills/origami-critique/SKILL.md):
    Quantitative 0–10 fidelity rubric (`bp.evaluate_fidelity`), hard fold/pose
    gates, and visual turnaround defect remedies.

## Evaluation on Large Stick-Figure Benchmarks

Across a 2,676-tree synthetic stick-figure benchmark suite spanning branched
bases, multi-limb symmetric layouts, and high-complexity models (up to 45
sticks, branching degree 14, and grid sizes $G \in [28, 82]$):

-   **Built-in examples (`bp.list_examples()`, 47 trees)**: All canonical tree
    examples can be loaded directly with `bp.load_example(name)` for unit
    testing, benchmarking, and visual inspection.
-   **Global flat-foldability verification**: Every solved crease pattern
    returned with `check_global_flat_foldability=True` is independently verified
    for valid non-self-intersecting layer ordering via the bundled Flat-Folder
    port.
-   **Stress scalability**: Under a combined 900s per-tree budget on the 200
    highest-complexity stick figures (15–45 sticks, degree 6–14), the reference
    backtracking pipeline packs `82.5%` (`165 / 200`) and produces globally
    flat-foldable crease patterns on `36.5%` (`73 / 200`).

## Citing this work

If you use this library in your research, please cite:

```
@misc{zahavy2026corigami,
  title={COrigami: An AI Pipeline for Co-Designing Flat-Foldable Visually Recognisable Origami},
  author={Tom Zahavy and Shaobo Hou and Thomas Tumiel and James Doran and Francesco Faccio and Xidong Feng and Alex Havrilla and Igor Khytryi and Chenglei Li and Lisa Schut and Vivek Veeriah and Arijan Abrashi and Micha{\l} Kosmulski and Robert J. Lang and Nick Robinson and Brandon Wong and Marcus Chiam and Gloria Fang and Satinder Singh},
  year={2026},
  eprint={2606.26299},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2606.26299}
}
```

## License and disclaimer

Copyright 2026 Google LLC

All software is licensed under the Apache License, Version 2.0 (Apache 2.0);
you may not use this file except in compliance with the Apache 2.0 license.
You may obtain a copy of the Apache 2.0 license at:
https://www.apache.org/licenses/LICENSE-2.0

`src/bp_pipeline/third_party/flat_folder/` contains a Python port of the
MIT-licensed [Flat-Folder](https://github.com/origamimagiro/flat-folder)
software by Jason S. Ku (see
[`src/bp_pipeline/third_party/flat_folder/LICENSE`](src/bp_pipeline/third_party/flat_folder/LICENSE)
and
[`src/bp_pipeline/third_party/flat_folder/README.md`](src/bp_pipeline/third_party/flat_folder/README.md)).

All other materials are licensed under the Creative Commons Attribution 4.0
International License (CC-BY). You may obtain a copy of the CC-BY license at:
https://creativecommons.org/licenses/by/4.0/legalcode

Unless required by applicable law or agreed to in writing, all software and
materials distributed here under the Apache 2.0 or CC-BY licenses are
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the licenses for the specific language governing
permissions and limitations under those licenses.

This is not an official Google product.
