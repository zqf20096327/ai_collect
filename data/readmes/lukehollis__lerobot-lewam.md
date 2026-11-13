# LeRobot-WAM

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![PyTorch 2.7+](https://img.shields.io/badge/pytorch-2.7%E2%80%932.11-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![LeRobot 0.6.1](https://img.shields.io/badge/LeRobot-0.6.1-FFD21E?logo=huggingface&logoColor=black)](https://github.com/huggingface/lerobot)
[![MuJoCo 3.11+](https://img.shields.io/badge/MuJoCo-3.11%2B-00A6D6)](https://github.com/google-deepmind/mujoco)
[![SO-101](https://img.shields.io/badge/robot-SO--101-1c1c1c)](https://github.com/TheRobotStudio/SO-ARM100)
[![License Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)


https://github.com/user-attachments/assets/176f83f8-e8dd-4977-80d7-033755140a15


**A small World Action Model, trained from scratch, so you can see how every piece works.**

LeRobot-WAM is a 31.5M parameter World Action Model packaged as a [LeRobot](https://github.com/huggingface/lerobot)
policy plugin. It learns to pick up a cube with an SO-101 arm in MuJoCo starting from random
weights. There is no pretrained VAE, ResNet, video model, or VLM anywhere in the stack. You can
read the whole model in an afternoon and train the laptop preset in a few hours.

This is a work in progress for studying and understanding the emerging family of world action
models. The design follows the joint video and action diffusion recipe from
[Unified World Models](https://arxiv.org/abs/2504.02792) with every pretrained component
replaced by one that starts from scratch. For the wider landscape, the 2026 survey
[World Action Models: A Survey](https://arxiv.org/abs/2606.20781) and its companion list
[awesome-world-action-models](https://github.com/world-action-models/awesome-world-action-models)
are good places to start, as is the [Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM)
collection from OpenMOSS. Expect the numbers, figures, and rollouts here to keep changing as
the study continues. Trained checkpoints are not on Hugging Face yet and are on the way.

---

## The idea

![LeRobot-WAM architecture](docs/lerobot-wam-architecture.svg)

Most generalist robot policies today are Vision-Language-Action models. Take a pretrained
vision-language model, attach an action head, and fine-tune on demonstrations. What comes out
learns a single conditional distribution, `p(action | observation, instruction)`, and whatever
it knows about how the world reacts to a push or a grasp is buried inside that action head.
There is nowhere in the architecture to ask what happens if the gripper closes here.

![SO-101 picking up the cube in MuJoCo](docs/assets/so101-expert-pick-lift.gif)

A World Action Model asks the same network to also predict the future observation. Here one
diffusion transformer denoises an action chunk and a pair of future frames together, and each
of those two streams runs on its own noise clock. Where you park the two clocks decides which
question the weights answer.

| query | distribution | action clock | world clock |
| --- | --- | --- | --- |
| policy | `p(a \| o)` | denoise `T → 0` | held at `T` |
| video prediction | `p(o' \| o)` | held at `T` | denoise `T → 0` |
| forward dynamics | `p(o' \| o, a)` | held at `0` | denoise `T → 0` |
| inverse dynamics | `p(a \| o, o')` | denoise `T → 0` | held at `0` |

One set of weights gives you four distributions with no extra heads and no retraining. People
care because action-labeled robot data is scarce while video is everywhere, because predicting
thousands of pixels is a far denser training signal than regressing six joint targets, and
because a forward model you can query lets you score a candidate chunk before executing it.
None of that is automatic, though. A future-prediction loss can be satisfied by learning
appearance alone, which is exactly what the evaluation tools further down are built to catch.

---



https://github.com/user-attachments/assets/572fa72f-0156-4d0b-bebd-9cc3b9c2e200



## The task

An [SO-101](https://github.com/TheRobotStudio/SO-ARM100) has to find a 30 mm cube on a table,
close its jaws on it, and lift it. The cube spawns anywhere in a 70 by 110 mm region, so the
policy has to read its position from pixels rather than memorize it.

| | |
| --- | --- |
| simulator | MuJoCo, `robotstudio_so101` from [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) |
| action | 6 absolute joint targets in radians at 30 Hz |
| observation | `front` and `wrist` RGB at 224 by 224, resized to 96 by 96, plus 6 joint angles |
| demonstrations | 200 successful scripted episodes, roughly 26k frames |
| success | cube centre held above 12 cm for 5 consecutive steps |

Demonstrations come from a scripted waypoint controller that reads the cube pose straight out
of the simulator. It stands in for a human teleoperator and nothing more, since the policy only
ever sees pixels and joint angles. The SO-101 gripper has one moving jaw, so the grasp point is
offset toward that jaw and the moving pad sweeps the cube against the fixed one as it closes.
That small piece of geometry is what makes the task forgiving enough for a learned policy to
solve, and [docs/so101-sim-pick-lift.md](docs/so101-sim-pick-lift.md) walks through it.

---

## The model

Every training sample is centred on frame `t`. The current observation is frames `t-1` and `t`,
the action chunk runs from `t` through `t+15`, and the world-model target is frames `t+15`
and `t+16`.

A 4.9M parameter VAE compresses each 96 by 96 frame into a `4×12×12` latent. It trains first,
has its latent statistics recalibrated with the encoder frozen, and then never moves again so
the denoiser is chasing a stationary target. A separate residual CNN turns the two current
frames from both cameras and the joint angles into a single conditioning vector. That vector is
summed with sinusoidal embeddings of both clocks and modulates every transformer block through
AdaLN-Zero, whose zero-initialised gates let an eight-block transformer train stably from
random weights on 26k frames.

The denoiser is 26.6M parameters across eight blocks at width 384 with six heads. Its sequence
is 56 tokens long, made of 16 noisy action tokens, 32 noisy future-latent tokens from a
`(2,3,3)` spatiotemporal patchify over both cameras, and 8 learned register tokens. Two small
heads read the sequence back out and predict noise for the actions and for the future latents,
with equal-weight MSE on both. At deployment the controller predicts 16 actions, executes 8, and
replans, which is about a quarter second of committed motion at 30 Hz.

---

## Run it

You need Python 3.12 and the LeRobot commit this plugin is pinned to.

```bash
git clone https://github.com/huggingface/lerobot.git
git -C lerobot checkout 0d383d09f2051444de211739196a28cc94736861
pip install -e './lerobot[training]'
pip install -e '.[sim]'
```

Check that LeRobot found the plugin.

```bash
python -c 'from lerobot.utils.import_utils import register_third_party_plugins; register_third_party_plugins(); from lerobot.configs import PreTrainedConfig; print("wam" in PreTrainedConfig.get_known_choices())'
```

Record demonstrations. The scripted expert succeeds about nine times in ten and the failed
takes are discarded, the same way you would re-record a fumbled teleop episode.

```bash
python -m lerobot_policy_wam.sim.record --root data/so101_sim_pick_lift --episodes 200
```

Train everything from scratch. The script trains the VAE, calibrates it, trains the coupled
denoiser, and finishes with held-out diagnostics.

```bash
./scripts/sim/train_from_scratch.sh outputs/so101_sim
```

It picks CUDA when it sees a GPU and falls back to Apple silicon or CPU otherwise. The default
step counts are sized for a coffee break rather than convergence, so on a real GPU raise
`WAM_AE_STEPS` and `WAM_WORLD_STEPS` substantially.

Roll the policy out and watch it.

```bash
python -m lerobot_policy_wam.sim.rollout --policy-path outputs/so101_sim/world_model/checkpoints/last/pretrained_model --output-dir outputs/so101_sim/rollout --episodes 20 --video-episodes 3 --expert-baseline
```

That writes MP4s of the arm plus an imagination strip captured just before the jaws close. The
strip puts the decoded `p(o' | o, a)` prediction next to the frame the simulator actually
produced 16 steps later.

---

## Does the world model actually help?

A future-prediction loss is easy to lower by learning table texture and the arm's own
silhouette without ever learning that actions move things. When that happens the predicted
frames look great and the policy is no better than a plain diffusion policy. This repo ships
four checks that tell the cases apart.

Shuffled-action coupling predicts the future with the correct action chunk and then again with
another sample's chunk. If the error barely changes, the model is not conditioning on actions
and its forward dynamics is video autocomplete. Shuffled-future coupling runs the same
intervention on inverse dynamics. The action-only control in `scripts/train_action_only.sh`
trains the identical architecture from the identical calibrated VAE with the future tokens
replaced by learned nulls, so a WAM that cannot beat it in closed loop gained nothing from the
world objective. The last check is closed-loop success on randomized cube positions, scored
against the scripted expert on the very same positions.

```bash
lerobot-wam-eval-world --policy-path outputs/so101_sim/world_model/checkpoints/last/pretrained_model \
  --dataset-repo-id lerobot_wam/so101_sim_pick_lift --root data/so101_sim_pick_lift \
  --output-dir outputs/so101_sim/world_eval
```

[docs/experiments.md](docs/experiments.md) explains how to read the output, including the case
where a coupling gap exists but is not yet useful for control.

---

## Checkpoints

Trained weights are not published yet. They will go up on Hugging Face once the current runs
settle, together with the rollout videos and offline metrics that belong to them.

---

## Going deeper

The `docs` folder holds the long-form notes. [architecture.md](docs/architecture.md) covers the
design decisions, the endpoint semantics of the diffusion schedule, why the EMA horizon has to
fit the run, and why the sampler step count is a task-tolerance decision rather than a speed
knob. [so101-sim-pick-lift.md](docs/so101-sim-pick-lift.md) is the full write-up of the MuJoCo
task, and [experiments.md](docs/experiments.md) is the evaluation protocol. If you have real
hardware, [so101-wrist-block-pick.md](docs/so101-wrist-block-pick.md) is the wrist-camera
runbook, and [dgx-spark.md](docs/dgx-spark.md) covers the containerised PushT run on a DGX
Spark.

---

## Credits

The robot description in `src/lerobot_policy_wam/sim/assets/so101/` is vendored from
[MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) (`robotstudio_so101`,
Apache-2.0), which is itself derived from [The Robot Studio](https://github.com/TheRobotStudio/SO-ARM100)'s
SO-101. The task scene, expert, environment, and everything else under `src/lerobot_policy_wam/`
are this project's own, under the terms in [LICENSE](LICENSE).
