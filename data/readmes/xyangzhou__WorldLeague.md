<div align="center">

<h1 align="center">
  <img src="assets/worldleague-title.png" width="45%" alt="WorldLeague"><br>
  <sub>Benchmarking Physical Agency</sub>
</h1>

<p>
  <a href="LICENSE">
    <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-4E94CE.svg">
  </a>
  <a href="https://arxiv.org/abs/2611.30989">
    <img src="assets/badges/arxiv.svg" alt="WorldLeague paper on arXiv">
  </a>
  <a href="https://github.com/xyangzhou/WorldHarness">
    <img src="https://img.shields.io/badge/WorldHarness-Interfaces-28736D.svg" alt="WorldHarness interfaces">
  </a>
  <a href="https://xyangzhou.github.io/WorldLeague/#leaderboard">
    <img src="assets/badges/leaderboard.svg" alt="View the WorldLeague leaderboard">
  </a>
  <a href="https://huggingface.co/datasets/xyangzhou/WorldLeague">
    <img src="https://img.shields.io/badge/HuggingFace-Dataset-FFB000.svg" alt="Hugging Face dataset">
  </a>
</p>

<p><strong>WorldLeague evaluates what an embodied agent can accomplish in 60 interactive household tasks.</strong></p>

</div>

<table align="center">
<tr><td width="698">

https://github.com/user-attachments/assets/e22fa981-7c53-4d74-8ece-945eb483fb38

</td></tr>
</table>

> **WorldLeague: Benchmarking Physical Agency**  
> [Xinyang Zhou](mailto:xinyangzhou@u.nus.edu), [Qi Li](mailto:liqi@u.nus.edu), [Xinchao Wang](mailto:xinchao@nus.edu.sg)  
> [xML Lab](https://sites.google.com/view/xml-nus), National University of Singapore

---

<a id="updates"></a>

## ⭐ Updates

- **Nov 24, 2026** · The benchmark dataset is available on [Hugging Face](https://huggingface.co/datasets/xyangzhou/WorldLeague). Our Code and WorldHarness is available on [WorldLeague](https://xyangzhou.github.io/WorldLeague) and is available on [WorldHarness](https://xyangzhou.github.io/WorldHarness)

---

<a id="highlights"></a>

## 💪 Highlights

- **60 household tasks across six dimensions.** Find a target, stack a stable tower, or clear an obstruction that returns after delivery. WorldSeek, WorldShape and WorldShift group tasks by the physical challenge the robot faces.
- **Three types of embodied AI system.** WorldHarness lets vision-language models (VLMs) act through our [WorldHarness](https://xyangzhou.github.io/WorldHarness). Vision-language-action models (VLAs) and world-action models (WAMs) send continuous commands through their native robot interfaces.
- **WorldHarness.** A VLM chooses a target or motion from the robot’s camera views. After each command, it sees what changed and receives feedback, such as an arm reaching its joint limit. It can use that feedback and revisit earlier views to choose its next move.
- **Credit for progress and a separate success rate.** The Interactive Score credits individual goal items. Physical success requires the entire goal and its constraints to hold. For example, a robot can stack two boxes and still miss the release requirement.

<div align="center">
  <img src="assets/tasks.png" width="93%" alt="Example household tasks arranged by track and physical capability">
  <br>
  <em>Examples from WorldSeek (blue), WorldShape (green) and WorldShift (red).</em>
</div>

---

## 📚 Table of Contents

- [💡 Introduction](#introduction)
- [💻 Benchmark](#benchmark)
- [🤖 WorldHarness](#worldharness)
- [🚀 Quick Start](#quick-start)
- [🔧 Installation](#installation)
- [🔥 Policy Integration](#policy-integration)
- [⚡ Evaluation](#evaluation)
- [🔍 Trajectory Visualization](#trajectory-visualization)
- [🤝 Contributing](#contributing)
- [☀️ Acknowledgement](#acknowledgement)
- [📖 Citation](#citations)

---

<a id="introduction"></a>

## 💡 Introduction

Which physical goals can today’s AI systems achieve on their own? WorldLeague compares VLMs, VLAs and WAMs on 60 simulated robot tasks. Agents explore scenes to gather evidence in **WorldSeek**, rearrange objects in **WorldShape**, and adapt to changes in **WorldShift**. VLMs issue commands through WorldHarness, while VLAs and WAMs use their native controls. Across six capability dimensions, we score the robot’s trajectory in two ways: how far it gets toward the goal (Interactive Score) and how often it completes the goal (physical success rate). Together, these form its **Physical Agency Profile**.

Among the 13 systems evaluated in the paper, Claude Fable 5.2 completed 13 of 60 goals and earned the highest mean Interactive Score (28.58/100). Of the 347 VLM episodes with every terminal question answered correctly, 249 (71.8%) earned zero Interactive Score.

WorldLeague gives Embodied AI, Physical AI, and Agentic AI a shared basis for comparing what AI systems achieve autonomously, from partial progress toward a physical goal to full goal completion.

<div align="center">
  <img src="assets/task-construction.png" width="94%" alt="Three panels showing the task instruction, initial scene and physical checks for an ordered pickup task">
  <br>
  <em>Building T07. The instruction specifies which rooms to visit and what to collect. The scene sets the robot and objects in place. The evaluator checks the visit and pickup order, then verifies that the objects are released and stable on the tray.</em>
</div>

---

<a id="models-and-dataset"></a>
<a id="benchmark"></a>

## 💻 Benchmark

| Track | Primary dimensions | Tasks |
| --- | --- | ---: |
| 📊 WorldSeek | D1 Navigation (5), D2 Grounding (17) | 22 |
| 📊 WorldShape | D3 Geometry (17), D4 Physics (7) | 24 |
| 📊 WorldShift | D5 Memory (8), D6 Control (6) | 14 |

The dataset includes task and scene configurations and 73 terminal questions. Select a task by its catalogue alias, such as `T04`. All 60 tasks support R1. The continuous-control evaluation covers 59 tasks. [🤗 Our Benchmark](https://huggingface.co/datasets/xyangzhou/WorldLeague)

TODO: Add a public scene-generator entry point for selecting templates, instance counts and candidate budgets.

---

<a id="worldharness"></a>

## 🤖 WorldHarness

WorldHarness connects a vision-language model to the R1 robot. On each turn, the model reads the camera views and feedback from the previous action, then chooses a command. The simulator keeps running while the model decides, so an object released on one turn can still move before the next observation. The model can revisit earlier camera views to see what changed.

<div align="center">
  <img src="assets/worldharness.png" width="50%" alt="WorldHarness observation, command execution, feedback and scoring loop">
  <br>
  <em>WorldHarness executes the model’s commands and returns camera views and robot feedback. The evaluator scores physical outcomes and terminal answers separately.</em>
</div>

---

<a id="quick-start"></a>

## 🚀 Quick Start

```bash
python -m pip install -e .
git clone https://huggingface.co/datasets/xyangzhou/WorldLeague benchmark
worldleague tasks
```

If you already have the dataset, set `WORLDLEAGUE_BENCHMARK` to its root and run `worldleague tasks`. The global option `worldleague --benchmark /path/to/dataset tasks` selects it for a single command.

---

<a id="installation"></a>

## 🔧 Installation

1. Set up OmniGibson 3.7.1 with Isaac Sim 4.5.0, NVIDIA rendering support and the licensed [BEHAVIOR-1K assets](https://behavior.stanford.edu/). Run the remaining commands in that simulator environment from the WorldLeague checkout.
2. Install WorldLeague and download the benchmark as shown in Quick Start. WorldLeague includes the scene builders, continuous policy interfaces and evaluation presets.

   ```bash
   python -m pip install -e '.[simulation]'
   export OMNIGIBSON_DATA_PATH=/path/to/behavior
   export WORLDLEAGUE_BENCHMARK="$PWD/benchmark"
   ```

3. For PandaOmron, build its local assets with the matching robosuite asset directory.

   ```bash
   export WORLDLEAGUE_ROBOT_ASSETS=/path/to/prepared-robot-assets
   python -m worldleague.prepare_robot native --gpu 0 --robot-assets "$WORLDLEAGUE_ROBOT_ASSETS" \
     --robosuite-assets /path/to/robosuite/robosuite/models/assets
   python -m worldleague.prepare_robot compound --gpu 0 --robot-assets "$WORLDLEAGUE_ROBOT_ASSETS"
   ```

4. For R1 scene inspection or VLM evaluation, install the sibling WorldHarness checkout in the same environment. For a model run, set the API key named by the preset.

   ```bash
   python -m pip install -e '../WorldHarness[simulation]'
   ```

---

<a id="policy-integration"></a>

## 🔥 Policy Integration

| Interface | How to use it |
| --- | --- |
| A multimodal Chat Completions endpoint | Set the base URL, model, supported reasoning level and API key environment variable in [the example configuration](configs/chat.example.yaml). |
| WorldHarness prompts, tools and provider caching | Pass `--config sol-medium`, `luna-medium` or `deepseek-low`. Use `deepseek-low-smoke` for a run capped at two decisions. OpenAI presets use `OPENAI_API_KEY`, and DeepSeek uses `AI_GATEWAY_API_KEY`. Custom YAML paths are also accepted. |
| A VLM policy using WorldHarness | Pass `--policy package.module:factory`. Implement `act(observation, actions, notes)` and `answer(observation, questions, notes)`. |
| An external R1 harness | Pass `--harness package.module:play`. The generator receives a public turn, yields a decision and returns terminal answers. |
| A continuous VLA or WAM | Use `--url` for a WebSocket policy server or `--plugin module:factory` for a local Python policy. Choose the preset matching the policy’s robot and command layout. |

The reference VLM client can recall prior camera images with `read_historical_rgb(decision_step, camera)` from the second decision onward. Each decision allows up to four historical images in four tool rounds. Recorded preludes are delivered before the first decision on tasks that use them. [Plugin specification and runnable examples](docs/plugins.md)

---

<a id="evaluation"></a>

## ⚡ Evaluation

### 1. Open a scene

```bash
worldleague scene T04 --seed 0 --gpu 0 --port 8615 --output outputs/scene-T04
```

Open `http://127.0.0.1:8615` to inspect the scene. Scene inspection and VLM evaluation use the same R1 initialization, variant, controller and cameras. Use a fresh output directory per run. GPU indices correspond to the physical devices shown by `nvidia-smi`.

### 2. Run a policy

**VLM.** Choose a preset and set its API key, then run one episode. Physics continues while the policy selects actions or retrieves historical views. The budget counts decisions. The default action mode accepts motion distances and angles. For fixed actions, pass `--action-mode fixed-repeat`. External R1 harnesses can request 1, 2, 4 or 8 repetitions per action in this mode.

```bash
worldleague eval T04 --config luna-medium --gpu 0 --seed 0 --output outputs/vlm/T04
worldleague profile outputs/vlm
```

**VLA or WAM.** Start the policy server with its checkpoint, then pass its WebSocket address. The five presets are `pi0.5`, `GR00T-N1.5-RoboCasa365`, `Xiaomi-XR-1-RoboCasa365`, `Awomo-0.5I-RoboCasa365` and `OpenWAM-Alpha-RoboCasa365`. PandaOmron takes 12-dimensional commands at 20 Hz. R1Pro takes 23-dimensional commands at 30 Hz.

```bash
worldleague continuous pi0.5 T04 --url ws://127.0.0.1:8000 --gpu 0 --seed 0 --output outputs/pi05/T04
worldleague continuous OpenWAM-Alpha-RoboCasa365 T04 --url ws://127.0.0.1:8001 --gpu 0 --seed 0 --output outputs/openwam/T04
worldleague profile outputs/pi05
```

### 3. Read the Physical Agency Profile

- ✅ **Interactive Score (0–100).** Multiply the mean credit across a task’s physical goal items by 100.
- ✅ **Physical success rate (0–1).** An episode succeeds when every required goal item and constraint holds. The profile averages repeated episodes within each task, then weights measured tasks equally.
- ✅ **Terminal QA (0–100, VLMs).** Score the terminal answers separately. Each profile metric reports its measured task count. Missing measurements appear as `null`.

The current instruction protocol, `task_instructions_v3`, gives policies the task goals and terminal questions. Earlier instruction protocols disclosed grading rules. To compare runs, use the following command for task coverage, termination reasons by physical outcome, timing and cost. [Scoring rules](docs/scoring.md) · [Analysis fields and cost definitions](docs/analysis.md)

```bash
worldleague analyze --system vlm=outputs/vlm --system pi05=outputs/pi05 > comparison.json
```

---

<a id="trajectory-visualization"></a>

## 🔍 Trajectory Visualization

<div align="center">
  <img src="assets/trajectories.png" width="95%" alt="Three sequences showing mirror-guided rearrangement, tower construction and an obstructed delivery">
  <br>
  <em>Top to bottom: repositioning an object using its reflection, completing a tower after an arm joint-limit stop, and clearing an obstruction that returns after delivery.</em>
</div>

Add `--record-trajectory` to an `eval` or `continuous` run to save RGB observations. In the episode directory, `trajectory_frames.jsonl` maps each recorded observation to its camera images in `trajectory_frames/`. [Trajectory and reference material](docs/analysis.md)

---

<a id="contributing"></a>

## 🤝 Contributing

We welcome contributions that bring new **interfaces, models, robots and harnesses** to WorldLeague. You can add an observation or action interface, connect a VLM, VLA or WAM, bring a new robot into the simulator, or build a harness that turns public observations into robot commands.

See the [contribution guide](docs/contributing.md) for the existing plugin interfaces, runnable examples and robot integration steps. Open an issue to discuss an idea, or send a pull request with a short example showing how to run your contribution on a benchmark task.

---

<a id="acknowledgement"></a>

## ☀️ Acknowledgement

We thank [BEHAVIOR-1K](https://behavior.stanford.edu/) for the household environments and object assets, and [ESI-Bench](https://github.com/ESI-Bench/ESI-Bench) and [InteractiveWorld](https://github.com/facebookresearch/InteractiveWorld) for work that informed nine WorldLeague challenges. The R1 interface builds on [Show-Harness-Explore](https://github.com/XuanCheg/Show-Harness-Explore), and PandaOmron uses assets from [robosuite](https://github.com/ARISE-Initiative/robosuite).

The demo video features an edited mix of [“Tears in Rain” by Scott Buckley](https://www.scottbuckley.com.au/library/tears-in-rain/), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The [evaluation code](LICENSE) and [WorldLeague-authored benchmark materials](https://huggingface.co/datasets/xyangzhou/WorldLeague/blob/main/LICENSE) are licensed under the MIT License. Third-party assets retain their upstream terms.

---

<a id="citations"></a>

## 📚 Citation

If you use the WorldLeague benchmark or WorldHarness, please cite [our paper](https://arxiv.org/abs/2611.30989).

```bibtex
@misc{zhou2026worldleague,
  title         = {{WorldLeague}: Benchmarking Physical Agency},
  author        = {Zhou, Xinyang and Li, Qi and Wang, Xinchao},
  year          = {2026},
  eprint        = {2611.30989},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO},
  url           = {https://arxiv.org/abs/2611.30989}
}
```
