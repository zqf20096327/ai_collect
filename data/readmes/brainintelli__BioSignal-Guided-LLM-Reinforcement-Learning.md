<h1 align="center">Biosignal-Guided Reinforcement Learning for LLM Agents</h1>
<p align="center">Where does an LLM explorer go next when its policy and value network receive offline replay of organoid neural activity?</p>
<p align="center"><a href="paper.pdf">Read the preprint</a> · <a href="#gameplay">Watch gameplay</a> · <a href="original/">Game and training code</a> · <a href="docs/data-access.md">Raw data</a> · <a href="https://github.com/brainintelli/BioSignal-Guided-LLM-Reinforcement-Learning/releases/tag/research-artifacts-v1">Checkpoints &amp; evaluation logs</a> · <a href="README.zh-CN.md">中文</a></p>

**Paper**　*Language Model Exploration and Survival Behavior Under Offline Replay of Organoid Neural Signals*

**Author**　Brainintelli Research Lab · Brainintelli, Shanghai, China · [research@brainintelli.com](mailto:research@brainintelli.com)

A language-model agent in a survival game can spend a turn walking one cell, navigating to a landmark, or gathering supplies. Those choices use different amounts of game time. We asked whether an agent receiving a replay of organoid electrical activity would reveal more terrain **within the same time budget**, including from a low-health start. For severely thirsty or hungry characters, we asked whether the input scheme affected survival. Those are measurable questions about the character’s behavior. Its health bar and its decision to seek water do not measure a subjective feeling of fear.

## Gameplay

https://github.com/user-attachments/assets/6b501274-535f-4aa3-bf73-9e032d7c6809

Watch the character beside the lake and the action log on the right. The display tracks decisions and elapsed game time separately, alongside health, satiety and hydration. This 41-second recording illustrates the game interface; the comparisons below use matched runs across seeds and maps. [Video guide and timestamps](docs/video.md) · [Original MP4](media/gameplay.mp4)

## Get the code, recordings and model archives

To inspect the evidence behind a recorded decision, download the training trajectories, policy-update records and per-game evaluation receipts. The same release includes the 96 confirmatory checkpoints with optimizer states, the available historical weights, code and logs. The [archive guide](docs/archive-downloads.md) lists the files for each task and the steps for verifying them.

| Material | Access |
|---|---|
| Paper, game, training source and paired outcomes | [Preprint PDF](paper.pdf) · [Source guide](docs/original-source.md) · [Per-game table](data/exploration.csv) · [Reproduction commands](docs/reproduction-guide.md). No GitHub sign-in required. |
| 182 raw H5 electrophysiology files | [Open the Quark Drive share](https://pan.quark.cn/s/3f2e5122ab68) and enter **`mFFv`**. Verify your download against the [file list and SHA-256 digests](docs/data-access.md). |
| Model checkpoints, optimizer states and historical archives | [Public release](https://github.com/brainintelli/BioSignal-Guided-LLM-Reinforcement-Learning/releases/tag/research-artifacts-v1) · [Choose a collection and verify its SHA-256](docs/archive-downloads.md). |
| Original training and per-game evaluation receipts | [Training and evaluation records](docs/data-access.md#training-evidence-and-parameters) · [Download the receipts volume](https://github.com/brainintelli/BioSignal-Guided-LLM-Reinforcement-Learning/releases/download/research-artifacts-v1/receipts.zip.part001). It includes the training batches, updates and game-level decisions. |

## From an electrode recording to a game action

1. **Read one second of activity.** A microelectrode array (MEA) records spike times and channel identities. For each one-second window, we computed four quantities: log-transformed spikes per selected channel, the fraction of channels that fired, the concentration of spikes in time, and the entropy of their distribution across channels. Silent selected channels count towards the denominator. A calibration median and median absolute deviation put each quantity on a common bounded scale.
2. **Give the agent a choice.** Qwen3.5-0.8B received the four readouts in its prompt alongside terrain, landmarks, inventory and resource levels. Its value network received the same readouts. In the all-zero control we masked all four values **after** calibration in both branches. The game fed the outcome of each action back to the model. The recorded activity followed its own replay schedule; game actions sent no feedback to the tissue.
3. **Keep track of what was trained.** The language-model base stayed frozen during PPO updates to the policy adapter. The value network was updated separately. Each model in the short trials collected four batches of 12 decisions, with eight policy and 64 value updates in total. On chip 22021 the additional reward weight was zero, and each group retained its input scheme during evaluation. A difference between these groups therefore combines training and evaluation under that scheme.
4. **Compare like starts under two clocks.** We paired agents by training seed and map. First we counted newly revealed cells after six decisions. Then we truncated those same trajectories post hoc at game tick six. For the adverse-start experiment we used a fixed game-time limit from the outset, with endpoints for exploration under low health and survival under severe thirst or hunger.

![A recorded movement and a longer navigation action occupy different amounts of game time. A separate panel shows how the adverse-start comparison matches maps, seeds and input conditions.](figures/fig03.svg)

*Figure 3.* Two agents can take the same number of decisions and finish at different game ticks. A comparison conditioned on decisions and a comparison conditioned on elapsed time answer different questions. [Full-size figure](figures/fig03.svg) · [Signal processing and policy update, Figures 1–2](figures/)

## Which comparisons answer which question?

| Experiment | Inputs and matching | What we can learn |
|---|---|---|
| Short exploration trial, first organoid on chip 22021 | Each of 16 training seeds was evaluated on the same 48 maps. **Intact** used a pre-stimulation recording. **Unstimulated** used a later recording taken during zero commanded stimulation, after possible prior exposure. **All-zero** supplied a constant vector. | How much newly revealed terrain changes on these maps under each input scheme. The later recording also differs in biological time and exposure history. |
| Adverse starts, second organoid on chip 22021 | 32 seeds × 64 maps per group per start. **Intact** replayed the recorded order, **shuffled** reordered two-second blocks within trials, and **all-zero** masked the readouts. The 96 frozen models played 18,432 games. | Whether preserving order changes exploration from low health or survival from severe thirst and hunger by tick 60. Matching holds the initial scenario and map constant. |
| Separate recording on chip 22554 | The two MEA groups differed in their *training-trial pairings* and received the same ordered input during evaluation. A native game-reward-only agent provided a third comparison. | Whether short-horizon exploration recurs on another chip under this implementation. Its shuffle tests a different intervention from the within-trial shuffle on 22021. |

## What the measurements tell us

On the first organoid’s 48 maps, after six decisions the intact group revealed **1.99 more cells per game on average** than the all-zero group (fixed-map 95% interval **1.18 to 2.73**). Of the 768 matched games, **101** revealed more cells, **615** tied and **52** revealed fewer. The median difference was **zero**. Most trajectories thus gave the same exploration count. Readers can identify the seed–map pairs that contributed to the mean and compare the selected action categories in the [action records](data/actions.csv).

At equal elapsed time, intervals that resampled both seeds and maps crossed zero. Exploration did not replicate on chip 22554. All six primary adverse-start intervals crossed zero, and the two acquisition days yielded no reproducible exploration or score benefit from regular or random stimulation. In a first-day subtrial, action duration accounted for **84.3%** of the intact group’s and **95.9%** of the unstimulated group’s score difference from the all-zero group. Taken together, these measurements show **why the clock and the endpoint matter** when studying an agent with variable-duration actions. A larger score alone cannot identify better survival decisions. The current comparisons also leave open whether a matched synthetic input would behave similarly, and how much of a difference arises at inference time.

![Figure 5 shows paired exploration differences with intervals and the number of game pairs with more, equal and fewer newly revealed cells.](figures/fig05.svg)

*Figure 5.* For the three six-decision comparisons, intervals resample training seeds on the fixed maps (95%). For the two low-health comparisons, they resample seeds and maps (99.167%). The lower panel gives the distribution of paired outcomes for the first organoid. [Full-size figure](figures/fig05.svg) · [Paired outcomes](data/exploration.csv)

**Audit trail.** All 64 adverse-start maps and eight seeds had been used in pilot work. Design identifiers on 18,720 receipts were updated after evaluation; 99 earlier copies were available for comparison. The registered audit-game source was unavailable at evaluation, and the scenario-verification hash differed from the registration. Sections 5 and 8 and Appendix B distinguish these deviations from the later replay checks. [Manuscript](paper.pdf) · [Source notes](docs/source-notes.md)

## Run the analyses or inspect the project

From the repository root, with Python 3.12:

```sh
python -m src.reproduce smoke
python -m src.reproduce exploration
```

Both commands run offline on the included paired outcomes. Each writes a fresh run directory with results and input hashes. For interval estimation, the other endpoints, and figure generation, follow the [reproduction guide](docs/reproduction-guide.md).

| To inspect… | Start here |
|---|---|
| The game, agent, training tools, acquisition programs and historical source snapshots | [Original project](original/) · [Source inventory and scope](docs/original-source.md) |
| Paper-specific training, evaluation and PPO code | [Historical entry points](historical/README.md) · [Analysis source](src/) |
| Raw electrophysiology | [Quark Drive archive](https://pan.quark.cn/s/3f2e5122ab68) · extraction code **`mFFv`** · [Acquisition index, checksums and access instructions](docs/data-access.md) |
| Original paired-game and aggregate tables, model indexes and derived measurements | [Upstream tables](data/upstream/) · [Data dictionary](data/data_dictionary.csv) · [Dataset card](data/datasheet.md) |
| Which results can be regenerated, and what requires additional assets | [Result-by-result matrix](docs/reproduction_matrix.csv) · [Environment](docs/environment.md) · [Project contents and remaining dependencies](docs/project-contents.md) |
| Figures, figure sources and editable manuscript | [Figures and plotting code](figures/) · [Manuscript source](manuscript/) · [Word edition](manuscript/paper.docx) |

[Code terms](LICENSE) · [Data terms](LICENSE-DATA) · [Training artifact terms](LICENSE-TRAINING) · [Citation](CITATION.cff)
