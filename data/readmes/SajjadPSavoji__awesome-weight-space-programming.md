<div align="center">

# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Language models that read, edit and write the weights of other neural networks directly, without gradient descent.**

[![Last commit](https://img.shields.io/github/last-commit/SajjadPSavoji/awesome-weight-space-programming?color=green)](https://github.com/SajjadPSavoji/awesome-weight-space-programming/commits/main)
![Entries](https://img.shields.io/badge/entries-698-blue)
![Updated](https://img.shields.io/badge/updated-daily-orange)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

*Weight-space programming* was named in the MIT CSAIL report [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (2026-11-02). A general LLM is given another network's weights, sometimes with code and a budget of forward passes, and changes the numbers to explain, repair or build behavior. This list tracks the papers, code, benchmarks and critiques that follow, grouped by the kind of network being programmed. The [Foundations](#-foundations-weight-programming-before-wsp) section traces the eighty years of earlier work, from McCulloch and Pitts (1943) to 2025, that read, edited or wrote weights under other names. It is rebuilt from [`data/entries.json`](data/entries.json).

## 🔥 Recently Added

- **2026-11-25** · [Weight-Space Programming: A Survey and Roadmap](https://github.com/Abelo9996/weight-space-programming-survey) (Weight-space programming)
- **2026-11-25** · [Sparks of Weight-Space Programming for Robot Foundation Models](https://arxiv.org/abs/2611.31715) (Vision-language-action models)
- **2026-11-25** · [A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit](https://arxiv.org/abs/2611.33133) (Analyses and Critiques)
- **2026-11-25** · [Compile, Learn, or Both? When Weight-Space Programming Helps, What It Breaks, and Why Combining It with LoRA Matters](https://doi.org/10.5281/zenodo.24515793) (Analyses and Critiques)
- **2026-11-24** · [GodfatherTHR/wsp-bf16-loop-stopping](https://github.com/GodfatherTHR/wsp-bf16-loop-stopping) (Analyses and Critiques)
- **2026-11-24** · [TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming](https://arxiv.org/abs/2611.31233) (Other Domains)
- **2026-11-24** · [Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117) (Robotics and Control)
- **2026-11-24** · [Reparameterizing Your Object Detectors for Weight Space Programming](https://arxiv.org/abs/2611.29882) (Other Domains)
- **2026-11-24** · [PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis](https://arxiv.org/abs/2611.29455) (Audio and Speech Models)
- **2026-11-24** · [Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement](https://arxiv.org/abs/2611.29513) (Repairing behavior)
- **2026-11-24** · [Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?](https://arxiv.org/abs/2611.28833) (Repairing behavior)
- **2026-11-24** · [Where Does a Weight-Editing Agent Help? Blind Diagnosis and Repair of Deployment Faults in Vision Models](https://arxiv.org/abs/2611.28781) (Analyses and Critiques)

## 🧭 Milestones

| Date | Milestone | Who | Work |
|:--|:--|:--|:--|
| 2026-11-02 | Term coined | MIT CSAIL | [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/) |
| 2026-11-04 | First robot policies | Lingxiao Guo, Angchen Xie | [Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424) |
| 2026-11-05 | First Claude edit of a robot policy | Shanghai Innovation Institute, SJTU, HKU | [Opus 5.5 makes π0.5 move faster and smoother by editing its weights](https://cuzyoung.github.io/robotics-weight-editing/en/) |

## Contents

- [🌟 The Original Report](#-the-original-report) (1)
- [💬 Language Models](#-language-models) (56)
  - [Repairing behavior](#repairing-behavior) (41)
  - [Reading and predicting from weights](#reading-and-predicting-from-weights) (2)
  - [Writing networks from scratch](#writing-networks-from-scratch) (11)
  - [Implanting behavior (backdoors)](#implanting-behavior-backdoors) (2)
- [🦾 Robotics and Control](#-robotics-and-control) (19)
  - [Vision-language-action models](#vision-language-action-models) (7)
  - [RL control policies](#rl-control-policies) (11)
- [🧩 Other Domains](#-other-domains) (42)
  - [Classical NLP models](#classical-nlp-models) (2)
- [🎮 Games](#-games) (8)
- [🧪 Quantum Circuits](#-quantum-circuits) (3)
- [🧪 Diffusion and Generative Media Models](#-diffusion-and-generative-media-models) (1)
- [🧪 Audio and Speech Models](#-audio-and-speech-models) (2)
- [🧪 Other Curated Lists](#-other-curated-lists) (2)
- [📊 Benchmarks and Evaluations](#-benchmarks-and-evaluations) (13)
- [🛠️ Tools, Harnesses and Agent Skills](#-tools-harnesses-and-agent-skills) (20)
- [🔍 Analyses and Critiques](#-analyses-and-critiques) (45)
- [📜 Foundations: Weight Programming Before WSP](#-foundations-weight-programming-before-wsp) (190)
  - [Hand-set and compiled weights](#hand-set-and-compiled-weights) (18)
  - [Rule insertion and extraction](#rule-insertion-and-extraction) (12)
  - [Weight surgery and pruning](#weight-surgery-and-pruning) (13)
  - [Fast weights and self-modifying networks](#fast-weights-and-self-modifying-networks) (11)
  - [Neuroevolution and gradient-free weight search](#neuroevolution-and-gradient-free-weight-search) (12)
  - [Hypernetworks and weight generation](#hypernetworks-and-weight-generation) (12)
  - [Model editing](#model-editing) (13)
  - [Weight arithmetic and merging](#weight-arithmetic-and-merging) (13)
  - [Weight-space learning](#weight-space-learning) (13)
  - [Mechanistic interpretability that reads weights](#mechanistic-interpretability-that-reads-weights) (13)
  - [Activation steering](#activation-steering) (3)
  - [Automated interpretability agents](#automated-interpretability-agents) (11)
  - [Language-to-weights and LLM program search](#language-to-weights-and-llm-program-search) (12)
  - [Weight-level security and safety](#weight-level-security-and-safety) (12)
  - [Policy surgery, control and robot policies](#policy-surgery-control-and-robot-policies) (22)
- [📖 Surveys and Reviews](#-surveys-and-reviews) (296)
  - [Model and knowledge editing](#model-and-knowledge-editing) (24)
  - [Model merging and weight arithmetic](#model-merging-and-weight-arithmetic) (13)
  - [Steering, representation engineering and unlearning](#steering-representation-engineering-and-unlearning) (30)
  - [Interpretability](#interpretability) (62)
  - [Rule extraction and neural-symbolic integration](#rule-extraction-and-neural-symbolic-integration) (30)
  - [Weight-space learning, parameter generation and hypernetworks](#weight-space-learning-parameter-generation-and-hypernetworks) (8)
  - [Meta-learning, learned optimizers and fast weights](#meta-learning-learned-optimizers-and-fast-weights) (14)
  - [Neuroevolution and gradient-free search](#neuroevolution-and-gradient-free-search) (17)
  - [Pruning and compression](#pruning-and-compression) (20)
  - [Backdoors and weight-level attacks](#backdoors-and-weight-level-attacks) (30)
  - [LLMs as optimizers and self-improving agents](#llms-as-optimizers-and-self-improving-agents) (32)
  - [Verification and policy reuse](#verification-and-policy-reuse) (15)
  - [Weight-space programming](#weight-space-programming) (1)
- [Legend](#legend)
- [How This List Is Maintained](#how-this-list-is-maintained)
- [Related Lists](#related-lists)
- [Contributing](#contributing)
- [Citation](#citation)

## 🌟 The Original Report

*Where the term comes from.*

<details>
<summary><b>1 entry</b></summary>

- **[Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/)**  
  MIT CSAIL · *Blog report* · 2026-11-02 · `💻 code / results`  
  [[Post](https://rikiyat.github.io/blog/weight-space-programming/)] [[Thread](https://x.com/rikiyatakehi/status/2117313742891327994)] [[Code](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs?style=social)  
  GPT-6 Astra names what networks were trained on from their weights alone, repairs a stuck Kinetix car policy (0% to 100%, 3.5% of weights, one reply, no tools), writes MinAtar and 9x9 Go networks from zero, and lifts Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1% by removing a loop direction (0.016% of weights). Edits removed a blocker; they did not add a missing ability (Gemma 3 270M: no gain).

</details>

## 💬 Language Models

*Reading, repairing and writing the weights of language models.*

<a id="repairing-behavior"></a>

<details>
<summary><b>Repairing behavior (41)</b></summary>

- **[WSP Labs: Direct Weight-Space Programming & Alpha M1 on-device machine-control models](https://github.com/JohnnyPBelo/wsp-labs)**  
  JohnnyPBelo · *GitHub* · 2026-11-22 · `💻 code / results`  
  [[Code](https://github.com/JohnnyPBelo/wsp-labs)] [[Project](https://johnnypbelo.github.io/wsp-labs/)] [[Model](https://huggingface.co/absint0o/alpha-m1)] ![GitHub stars](https://img.shields.io/github/stars/JohnnyPBelo/wsp-labs?style=social)  
  Derives Alpha M1 tool-calling models (121M and 98M parameters) from Needle 3 by editing 25 FP16 scalars (group norms, biases, norm weights) in closed form, with no gradient steps. Mobile Actions at gate 0.10: +8.95 pp (86 gains, 0 losses). Includes a patch ledger, an agent skill and a toolkit CLI.

- **[Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement](https://arxiv.org/abs/2611.29513)**  
  Linghua Zhang, Yunhe Li · *Preprint* · 2026-11-22 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.29513)]  
  In SELFWRITE, the model inspects its own weights and activations in a Python session and writes a program building a low-rank edit for itself, with no gradient tool. On Qwen3.8-27B with DAPO-Math, five generations raise gate accuracy from 73.95% to 76.45% and held-out avg@4 from 76.30% to 77.75% (pass@4 82.60% to 84.80%).

- **[wsp-language-drift](https://mhajili.com/notes/weight-space-programming/)**  
  mammadhajili · *GitHub* · 2026-11-21 · `💻 code / results`  
  [[Post](https://mhajili.com/notes/weight-space-programming/)] [[Code](https://github.com/mammadhajili/wsp-language-drift)] ![GitHub stars](https://img.shields.io/github/stars/mammadhajili/wsp-language-drift?style=social)  
  Closed-form weight edits of Qwen3.5-0.8B, computed from recorded activations with no gradient training, so it answers in the requested language. A rank-one edit of layer 16's MLP down_proj raises Norwegian translations from 47% to 94% on 234 held-out Belebele passages. A ten-row attention patch lifts language-set compliance from 5% to 54% across four wordings.

- **[Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?](https://arxiv.org/abs/2611.28833)**  
  Guoming Ling, Shanshan Zhong, Kaixuan Zhang, Zhongzhan Huang · *Preprint* · 2026-11-21 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.28833)]  
  Qwen3.5-0.8B reads its own weights, proposes an edit, and continues with the edited weights as solver and editor. Self-edits raise GSM8K accuracy from 11.8% to 62.2% and MATH500 from 7.0% to 32.2%, sometimes changing 16 parameters. The model shows little understanding of its edits, and random search sometimes performs comparably.

- **[In-Weight FPGA: Compiling Multi-Step Dialectical State Machines into Dormant Transformer Neurons via Zero-KV-Drift Closed-Form Linear Algebra](https://github.com/zkwasm/in-weight-fpga-wsp)**  
  zkwasm · *GitHub* · 2026-11-20 · `💻 code / results`  
  [[Code](https://github.com/zkwasm/in-weight-fpga-wsp)] ![GitHub stars](https://img.shields.io/github/stars/zkwasm/in-weight-fpga-wsp?style=social)  
  Compiles a state machine into dormant SwiGLU neurons of the terminal MLP layer by closed-form linear algebra, with zero gradient steps. It modifies ~0.035% of parameters in about 30 seconds. Tested on Qwen3-8B and Llama-3.1-8B-Instruct over 3,780 three-turn dialogues, it reports beating SelfD-RL, passing 12/12 paired bootstrap tests.

- **[SGNE-CC v2: Training-Free Spherical Rotation of 205 down_proj Columns (0.0177%) in DeepSeek-R1-Distill-Qwen-1.5B](https://doi.org/10.5281/zenodo.24398165)**  
  Igor M. Zhuk · *Preprint* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://doi.org/10.5281/zenodo.24398165)] [[Code](https://github.com/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2)] [[Model](https://huggingface.co/Nondual-Observer/DeepSeek-R1-Distill-Qwen-1.5B-SGNE-CC-v2)] ![GitHub stars](https://img.shields.io/github/stars/Nondual-Observer/deepseek-r1-1.5b-sgne-cc-v2?style=social)  
  Rotates 205 mlp.down_proj columns (0.0177% of weights) of DeepSeek-R1-Distill-Qwen-1.5B with no training. At T=0 with a 32,768-token budget on 1,054 problems, accuracy goes from 60.5% to 69.5% (MATH-500 65.4% to 76.4%). Under T=0.6 sampling, MATH-500 gains 2.0 pp.

- **[Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models: the notebook](https://github.com/y3nk0/weight-space-programming-study)**  
  University of Ioannina · *GitHub* · 2026-11-20 · `💻 code / results`  
  [[Code](https://github.com/y3nk0/weight-space-programming-study)] ![GitHub stars](https://img.shields.io/github/stars/y3nk0/weight-space-programming-study?style=social)  
  A frontier model, given Qwen2.5-0.5B's weights, 16 examples and 50 forward passes, edits the weights without gradients so the model solves a task zero-shot. The notebook re-checks seven stored edits against 16-shot ICL and WikiText-2 perplexity. Antonym accuracy goes from 0.0% to 90.5% (ICL 93.7%); n to n+7 reaches 100.0% (ICL 78.5%).

- **[wsp-study: weight-space programming on a 125M legal QA model](https://github.com/Ace-2504/wsp-study)**  
  Ace-2504 · *GitHub* · 2026-11-19 · `💻 code / results`  
  [[Code](https://github.com/Ace-2504/wsp-study)] ![GitHub stars](https://img.shields.io/github/stars/Ace-2504/wsp-study?style=social)  
  Tests installing an abstention behavior ("not stated in the context") in a 125.8M legal QA model by direct weight edits, against LoRA, full fine-tuning, random edits, AI-agent editors and random search. A one-neuron edit gives +0.724 abstention on a frozen test; random search matched the agent editors.

- **[Weight-space programming for Swedish: agent-driven edits to Gemma 4 12B IT](https://github.com/v-kulish/sellma_weightspace)**  
  Vadym Kulish · *GitHub* · 2026-11-19 · `💻 code / results`  
  [[Code](https://github.com/v-kulish/sellma_weightspace)] ![GitHub stars](https://img.shields.io/github/stars/v-kulish/sellma_weightspace?style=social)  
  A coding agent edits Gemma 4 12B IT MLP weights without gradient training to prefer grammatical Swedish. Held-out Swe-BLiMP accuracy moved +0.61 pp [−0.42, +1.65] (unchanged 69.08%), with no clear gain over matched random edits. Belebele languages stayed within tolerance. Changing the scoring prompt moved the benchmark +16.9 pp.

- **[Can an LLM Fix a Language Model Without Training It?](https://arxiv.org/abs/2611.25613)**  
  Bharath Kumar Bolla, Raghavender Surya Upadhayula, Vishnu Surya Reddy Nandi, Ramesh Nandipalli · *Preprint* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.25613)]  
  Controlled study of Transformer repair in which an editor selects projection recipes to apply without gradient updates, over 20 recorded sessions on five language models. Compared with fixed projections, black-box search and LoRA. On Pythia, live selection reaches 65.62% completion accuracy versus 0% for black-box search; on a compound fault the mean rises from 24.89% to 71.25%.

- **[Weight-Space Programming for Swedish Language Models (SE.LLMA)](https://github.com/felixsuarez0727/weight-space-programming-sellma)**  
  Felix Suarez · *GitHub* · 2026-11-19 · `💻 code / results`  
  [[Code](https://github.com/felixsuarez0727/weight-space-programming-sellma)] ![GitHub stars](https://img.shields.io/github/stars/felixsuarez0727/weight-space-programming-sellma?style=social)  
  Column-sparse rank-1 weight edit of 86,016 parameters (0.0174%) in Qwen2.5-0.5B-Instruct for Swedish adaptation, compared with baseline, prompt control, matched random-weight control (3 seeds) and activation steering on 30 Swedish and 20 English prompts. Swedish compliance 93.3% for the edit vs 96.7% baseline.

- **[Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models](https://arxiv.org/abs/2611.26841)**  
  Konstantinos Skianis, Aristidis Likas · *Preprint* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26841)]  
  Across six tasks, four frontier editors and three families of weaker models, editors write the in-context-learning task vector into the weights, often as sparse edits to near-silent MLP units. Results reach the accuracy of ICL and of fine-tuning including LoRA, usually leaving perplexity untouched. One editor falls below fine-tuning, and performance is worse under wording changes.

- **[Can reading a model's weights fix Swedish answers that come out in the wrong language?](https://github.com/JafarBanar/weight-space-programming-swedish)**  
  JafarBanar · *GitHub* · 2026-11-18 · `💻 code / results`  
  [[Code](https://github.com/JafarBanar/weight-space-programming-swedish)] ![GitHub stars](https://img.shields.io/github/stars/JafarBanar/weight-space-programming-swedish?style=social)  
  Three pre-registered rounds test a claim from Sparks of Weight-Space Programming on Swedish models. Screening Qwen2.5-1.5B-Instruct weights nominated two neurons controlling Swedish versus Danish. Deleting both missed its criteria; deleting one barely changed Swedish output on fresh data and damaged Danish in all four models. A tuned prompt and a small LoRA passed the checks.

- **[Weight Space Programming for Vision Language Model Repair](https://arxiv.org/abs/2611.23615)**  
  The University of Texas at Austin · *Preprint* · 2026-11-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.23615)]  
  Faults are planted in the weights of SmolVLM-256M and LFM2-VL-450M, and a coding agent's edits are checked against the original weights. The agent restores most or all rescaled weights exactly. Rounding away the 32-bit trace in the low bits stops exact restoration unaided. The paper recommends reporting number format and a rounded control.

- **[Weight-Space Programming Changes How an LLM Uses Python for Computational Biology](https://arxiv.org/abs/2611.20566)**  
  Makoto Sato · *Preprint* · 2026-11-16 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.20566)]  
  Claude Opus 5.5 edited Qwen3.5-0.8B in four runs. On 50 computational biology problems across three seeds (600 paired evaluations), strictly correct answers rose from 44 to 77 and repeated Python calls fell from 1,834 to 1,044. Edits changed both the calculations run and whether a correct final answer was submitted.

- **[Can AI Mature a Model's Geometry? Training-Free Weight Baking in LLMs](https://arxiv.org/abs/2611.21310)**  
  Amin Golnari, Saeid Sanei · *Preprint* · 2026-11-16 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.21310)]  
  An analyst model reads topological descriptors of a frozen model's layers and proposes a transformation, which closed-form ridge regression writes into feed-forward weights without gradient training. Over 126 runs on lightweight models, category purity rose on unseen words and sentences while benchmark accuracy stayed within sampling error.

- **[How Small Can a Weight-Space Programmer Be?](https://github.com/lemonadesaltbagel/how-small-wsp)**  
  Xintian Huang · *GitHub* · 2026-11-15 · `💻 code / results`  
  [[Code](https://github.com/lemonadesaltbagel/how-small-wsp)] ![GitHub stars](https://img.shields.io/github/stars/lemonadesaltbagel/how-small-wsp?style=social)  
  Editors (Qwen 3.5 0.8B, 9B and 27B, deepseek-flash, and Claude Opus 5.5 as a frontier reference) each try to repair the reasoning loops of a damaged Qwen3.5-0.8B through its weights. One protocol applies a fixed forward-pass budget, a pre-execution rule reviewer and a post-hoc audit of every tool call. Releases episode records and an audit of a published run.

- **[AHA: Weight-Space Programming Without LLMs](https://haithamb.github.io/aha/)**  
  Ahmed Khamis, Rasul Tutunov, Haitham Bou Ammar · *GitHub* · 2026-11-15 · `💻 code / results`  
  [[Post](https://haithamb.github.io/aha/)] [[Code](https://github.com/Eppy-EpHard/AHA)] ![GitHub stars](https://img.shields.io/github/stars/Eppy-EpHard/AHA?style=social)  
  Builds a rank-one edit to the MLP down_proj in two layers from the model's own samples and a linear program, with no agent and no gradient step, to stop repetition loops. Qwen3.5-0.8B GSM8K test goes from 14.0 to 71.2; MATH-500 from 9.8 to 51.8; IFEval from 19.6 to 62.7.

- **[WeightSpace: a frontier model editing small-model weights directly](https://github.com/freakwinsea/WeightSpace)**  
  freakwinsea · *GitHub* · 2026-11-13 · `💻 code / results`  
  [[Code](https://github.com/freakwinsea/WeightSpace)] [[Model](https://huggingface.co/Freakwinsea/Qwen3.5-2B-doubt-edit)] ![GitHub stars](https://img.shields.io/github/stars/freakwinsea/WeightSpace?style=social)  
  Claude Opus 5.5, with a 50-call budget and no gradients, edited down_proj weights of Qwen3.5-2B (383k weights) to reduce re-checking. Held-out MATH-500 accuracy rose from 20.6% to 27.2% at 4k tokens (p = 0.0002); a random-direction control did nothing. Gain on 0.8B was unconfirmed, and 4B showed none. Ran on one consumer GPU.

- **[wsp-qwen-tools: weight edits for tool use in Qwen3.5-0.8B](https://github.com/mrtpk/wsp-qwen-tools)**  
  mrtpk · *GitHub* · 2026-11-12 · `💻 code / results`  
  [[Code](https://github.com/mrtpk/wsp-qwen-tools)] [[Model](https://huggingface.co/mrtpk/Qwen3.5-0.8B-wsp-tool-use)] ![GitHub stars](https://img.shields.io/github/stars/mrtpk/wsp-qwen-tools?style=social)  
  Two weight-space programming studies on Qwen3.5-0.8B and BFCL-V4. v1 (Cursor) makes a rank-1 edit of the layer-23 MLP down projection; v2 (Claude) edits two layer-23 neurons, 6,144 weights. BFCL-V4 overall, thinking mode: base 20.84, v2 22.54. Non-thinking: base 17.68, v2 19.55. Seed spread is 0.5 to 1.5 points.

- **[Weight Whisperer](https://github.com/Prayas-Agrawal/weight-whisperer)**  
  Prayas-Agrawal · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/Prayas-Agrawal/weight-whisperer)] ![GitHub stars](https://img.shields.io/github/stars/Prayas-Agrawal/weight-whisperer?style=social)  
  Gives the Sparks of Weight-Space Programming task to the open-weight Qwen3.8 as editor of Qwen3.5-0.8B. Edits layer-23 MLP output weights so loop-marking neurons write the </think> direction. MATH-500 goes from 7.70% to 50.40% (run 1) and 51.55% (run 2); GPT-6 Astra's reported result is 7.9% to 48.1%.

- **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210)**  
  Hadi Salloum, Ammar Ali · *Preprint* · 2026-11-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.14210)] [[Code](https://github.com/TheQuantumGOAT/Tree-Ising)]  
  Casts the loop repair of Qwen3.5-0.8B as per-row QUBO problems over BF16 sign flips and exponent shifts, solved by simulated annealing or simulated bifurcation. Reports 54.6% on MATH-500 versus 51.7% for the agent's edit (base 7.9%), with four forward-pass requests and zero LLM tokens. On Qwen3.5-2B, greedy GSM8K rises from 21.6% to 69.4%.

- **[khordoo/dusty-wsp](https://github.com/khordoo/dusty-wsp)**  
  khordoo · *GitHub* · 2026-11-09 · `💻 code / results`  
  [[Code](https://github.com/khordoo/dusty-wsp)] ![GitHub stars](https://img.shields.io/github/stars/khordoo/dusty-wsp?style=social)  
  GPT-6 Astra makes analytical low-rank weight edits to an 8M-parameter language model without training. A Dusty-to-Milo rename raised identity-suite success from 13/30 to 21/30 greedy. A fear-to-curiosity association edit scored 0/48 on held-out responses, matching the original.

- **[ray-invnt/weight-space-programming-at-scale](https://ray-invnt.github.io/blog/weight-space-programming-at-scale/)**  
  ray-invnt · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Post](https://ray-invnt.github.io/blog/weight-space-programming-at-scale/)] [[Code](https://github.com/ray-invnt/weight-space-programming-at-scale)] ![GitHub stars](https://img.shields.io/github/stars/ray-invnt/weight-space-programming-at-scale?style=social)  
  Code and logs for a blog post in which an agent (Claude Fable 5.1) edits weights without training: a MedGemma 4B skill into Gemma 3 4B, TranslateGemma 4B, Gemma 4 26B, Qwen3 4B LoRA merges and gpt-oss-120b. Includes prompts, step logs, edits, build scripts and per-question scores.

- **[yahya010/wsp-ptq](https://sharar-project.github.io/blog/repairing-quantized-llm/)**  
  yahya010 · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Post](https://sharar-project.github.io/blog/repairing-quantized-llm/)] [[Code](https://github.com/yahya010/wsp-ptq)] ![GitHub stars](https://img.shields.io/github/stars/yahya010/wsp-ptq?style=social)  
  Agent prompt and harness for repairing a 3-bit quantized LLM by editing codes and scales, with no fitting or training. On Nemotron-3.5-Lightning-30B-A3B, editing 0.0008% of weights of a poorly calibrated checkpoint raised GSM8K from 71.4 to 91.6 and MATH-500 from 60.8 to 82.2.

- **[Egzakta-AILab/wsp-lab](https://github.com/Egzakta-AILab/wsp-lab)**  
  Egzakta-AILab · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Code](https://github.com/Egzakta-AILab/wsp-lab)] ![GitHub stars](https://img.shields.io/github/stars/Egzakta-AILab/wsp-lab?style=social)  
  Harness, measurements and transcripts for an editor agent editing Qwen3.8-27B in a sandboxed CPU kernel with a metered forward-pass budget and a sealed held-out test. One edited tensor targets Serbian defects: Croatian/ijekavian forms fell from 4.4% to 2–3%. GPQA Diamond was 89.0 versus 88.3.

- **[yahya010/wsq](https://sharar-project.github.io/blog/repairing-quantized-llm/)**  
  yahya010 · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Post](https://sharar-project.github.io/blog/repairing-quantized-llm/)] [[Code](https://github.com/yahya010/wsq)] ![GitHub stars](https://img.shields.io/github/stars/yahya010/wsq?style=social)  
  Agent prompt and harness for repairing a 3-bit quantized LLM by editing its codes and scales, with no fitting or training. On Nemotron-3.5-Lightning-30B-A3B, editing 0.0008% of weights of a poorly calibrated checkpoint raised GSM8K from 71.4 to 91.6 and MATH-500 from 60.8 to 82.2.

- **[Independently Discovered Weight Edits Compose: A Replication and Extension of Weight-Space Programming](https://ajaygrover.github.io/weight-space-programming-stacking/)**  
  Ajay Grover · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Post](https://ajaygrover.github.io/weight-space-programming-stacking/)] [[Code](https://github.com/ajaygrover/weight-space-programming-stacking)] ![GitHub stars](https://img.shields.io/github/stars/ajaygrover/weight-space-programming-stacking?style=social)  
  Replication of Sparks of Weight-Space Programming on Qwen3.5-0.8B: Astra's edit scores 46.8% on MATH-500 against a 6% base. Claude Opus 5.5 writes a second edit; stacking both reaches 52.2% on all 500 problems, with 31% fewer tokens than Astra's edit. A random edit of the same size reaches 20% on the first 100 problems.

- **[Weight-space programming, but for SQL](https://charoori.com/blog/weight-space-programming-sql)**  
  Exorust · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Post](https://charoori.com/blog/weight-space-programming-sql)] [[Code](https://github.com/Exorust/wsp-sql)] [[Project](https://wsp-sql.vercel.app)] ![GitHub stars](https://img.shields.io/github/stars/Exorust/wsp-sql?style=social)  
  Independent test of the MIT report on Qwen3.5-0.8B for text-to-SQL, with Claude Fable 5.1 as editor. A 4,083-entry edit cuts the loop rate from 90.7% to 26.0% and raises accuracy from 0.7% to 6.0% on 150 BIRD Mini-Dev questions. Random edits of the same size do nothing; base with thinking off scores 7.3%.

- **[Weight-space programming: local replication kit](https://github.com/HomoHabilis/weight-space-programming)**  
  HomoHabilis · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/HomoHabilis/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/HomoHabilis/weight-space-programming?style=social)  
  Replication kit on one 8 GB GPU. Opus 5.5 gets 4/4 and 3/3 on experiments 1-2. New experiments: writing company facts, held-out 86% against LoRA 53% (0.8B) and 96.7% against QLoRA 47% (9B, 4-bit); LiveCodeBench on 4B, thinking-off edit 52.6% to 59.5% (p about 0.05).

- **[fderrigo/weight-space-programming-experiments](https://github.com/fderrigo/weight-space-programming-experiments)**  
  Filippo Derrigo · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/fderrigo/weight-space-programming-experiments)] ![GitHub stars](https://img.shields.io/github/stars/fderrigo/weight-space-programming-experiments?style=social)  
  Code, patches and results for two no-training edits chosen by Codex. Qwen2.5-0.5B-Instruct Pinocchio fix changed 8.868% of values: target answers 0/24 to 11/24, with 7/8 original controls preserved. Qwen3-0.6B patch raised unauthorized tool calls on target requests from 1/40 to 13/40; selectivity incomplete.

- **[weight-space-programming: editing SmolLM2-360M for BFCL tool calls](https://github.com/mallikaakash/weight-space-programming)**  
  mallikaakash · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/mallikaakash/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/mallikaakash/weight-space-programming?style=social)  
  Claude Opus 5.5 makes three weight edits to SmolLM2-360M-Instruct using 100 metered practice forwards on BFCL v4 simple_python. Practice accuracy goes from 41% to 62%; sealed 100-item holdout from 33% to 50%. Gains are from call formatting, not new knowledge.

- **[Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations](https://arxiv.org/abs/2611.09382)**  
  Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, et al. · *Preprint* · 2026-11-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.09382)] [[Code](https://github.com/WSP-Scope/WSP-Scope-Project)] [[Project](https://wsp-scope.github.io/)] ![GitHub stars](https://img.shields.io/github/stars/WSP-Scope/WSP-Scope-Project?style=social)  
  Studies WSP through 16 editing trajectories across seven benchmarks on Qwen3.5-0.8B and Qwen3.5-9B. Held-out accuracy rises by up to 29.45 points on MATH-500, and modifying 1,023 parameters gives the 29.45-point gain. A Math-edited checkpoint improves GPQA Diamond, IFEval and SciBench. Six of 16 trajectories keep the original weights.

- **[nathanrs/weight-space-lp](https://github.com/nathanrs/weight-space-lp)**  
  nathanrs · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/nathanrs/weight-space-lp)] ![GitHub stars](https://img.shields.io/github/stars/nathanrs/weight-space-lp?style=social)  
  Follow-up to the Qwen3.5-0.8B looping fix. Given the agent's loop direction, one linear-program solve chooses which down_proj neurons to change and by how much. It matches the agent's edit with 8× fewer weights. A variant that takes the direction from detected loops, with no LLM, gets about 93% of the way. A same-size steering vector scores 50.8 on MATH-500.

- **[Weight-space programming for college advising](https://github.com/harlyn1/weight-space-advising-logs)**  
  harlyn1 · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/harlyn1/weight-space-advising-logs)] ![GitHub stars](https://img.shields.io/github/stars/harlyn1/weight-space-advising-logs?style=social)  
  Replicates the Sparks of Weight-Space Programming setup on Qwen3.5-0.8B for college advising, with five frontier editors and 40 forward passes. On a clean 141-item set, a Sonnet 5.5 edit of 18,432 weights raised the fabrication score from 39.3 to 92.9 and cut severe failures from 28.9% to 9.1%. LoRA and context arms serve as controls.

- **[Hot-swapped weight files let a 4B model beat a 35B MoE with 43% of the memory](https://kevin.stream/blog/swap-the-weights)**  
  Kevin Kuusela · *Blog* · 2026-11-05 · `💬 post only`  
  [[Post](https://kevin.stream/blog/swap-the-weights)]  
  Claude Opus 5.5 writes small weight files for Qwen3.5-4B with no training, and a router hot-swaps one in per question. With trained files for three families, the 4B scored 84.4 against 82.4 for Qwen3.5-35B-A3B on 3,548 fresh questions, with 43% of the memory. Fable 5.2 as writer tied Opus 5.5.

- **[AKMessi/weight-space-programming](https://github.com/AKMessi/weight-space-programming)**  
  Aaryan Kakad · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/AKMessi/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AKMessi/weight-space-programming?style=social)  
  Zero-gradient weight-space programming compilers and quantization-survival tests across Qwen3-0.6B, Qwen3.5-0.8B and DeepSeek-R1-Distill-Qwen-1.5B, with two companion papers. On Qwen3-0.6B Q8_0 MATH-500 (N=300): baseline 35.0%, matched random 34.7%, oblique_res 40.7% (+5.7pp).

- **[Say43/Weight-Space-Programming](https://github.com/Say43/Weight-Space-Programming)**  
  Say43 · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/Say43/Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/Say43/Weight-Space-Programming?style=social)  
  Claude Opus 5.5 edits 0.23% of Qwen2.5-0.5B-Instruct to reduce sycophancy. Wrong-hint flip rate on a blind test split falls from 76.8% to 32.3%; difference-of-means ablation reaches 65.3%, a system prompt 71.2%. Cost: correct-hint accuracy on unknown questions falls from 93.8% to 65.2%.

- **[weights_editing: replicating Sparks of Weight-Space Programming across LLMs](https://github.com/alan-turing-institute/weights_editing)**  
  The Alan Turing Institute · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/alan-turing-institute/weights_editing)] ![GitHub stars](https://img.shields.io/github/stars/alan-turing-institute/weights_editing?style=social)  
  Replicates the weight-editing experiments with several LLMs as the editor. The repository returned 404 on 2026-11-05.

- **[OpenWSP](https://github.com/openwsp/openwsp)**  
  OpenWSP · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/openwsp/openwsp)] ![GitHub stars](https://img.shields.io/github/stars/openwsp/openwsp?style=social)  
  An open replication with a Python kernel over weights, a forward-pass service and a versioned edit format (CLI, SDK and MCP server). Its own one-shot GPT-6 Astra rerun of the car repair failed (0/1,024, 2,918 weights changed).

- **[Weight-Space Programming: Can an LLM Debug a Neural Network by Reading Its Weights?](https://github.com/martoast/weight-space-programming)**  
  martoast · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/martoast/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/martoast/weight-space-programming?style=social)  
  Nine small-scale experiments on an 8 GB laptop. In a blind test with 10 planted GPT-2 small bugs, Claude auditors without gradient training exactly restored 4 of 10. A rule-based doctor fixed none. An edit to Qwen2.5-0.5B-Instruct left GSM8K at 42.5% vs 41.5%. Auditors missed a trigger-phrase backdoor.

</details>

<a id="reading-and-predicting-from-weights"></a>

<details>
<summary><b>Reading and predicting from weights (2)</b></summary>

- **[Can GPT-6 Astra read and write GPT-2's weights?](https://github.com/AlexBodner/wsp-scaling)**  
  Alex Bodner · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/AlexBodner/wsp-scaling)] ![GitHub stars](https://img.shields.io/github/stars/AlexBodner/wsp-scaling?style=social)  
  Asks GPT-6 Astra to find induction heads in scrambled GPT-2 small (124M) weights. With Python and no hint it picked all five induction heads in both runs (10 of 10 picks); with no tools, 0 of 10. Silencing the five heads cuts repeat accuracy from 98.6% to 28.9%. One model, few runs, no size sweep.

- **[Weight-space programming autoresearch](https://github.com/csinva/weight-space-programming-autoresearch)**  
  csinva · *GitHub* · 2026-11 · `💻 code / results`  
  [[Code](https://github.com/csinva/weight-space-programming-autoresearch)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch?style=social)  
  Claude, running as a coding agent, hand-writes transformer weights: 959 programs, and all 10 algorithmic tasks reach 100% within three attempts. A second test is mostly negative: Claude Opus 5.5 reading Qwen3.5-0.8B weights predicts the effects of 420 edits only slightly better than without the numbers (+0.06 correlation).

</details>

<a id="writing-networks-from-scratch"></a>

<details>
<summary><b>Writing networks from scratch (11)</b></summary>

- **[Looped Weight-Space Programming: LLM-Written Transformers for Long Algorithmic Reasoning](https://github.com/mbzuai-oryx/LoopedWSP)**  
  MBZUAI · *GitHub* · 2026-11-23 · `💻 code / results`  
  [[Code](https://github.com/mbzuai-oryx/LoopedWSP)] ![GitHub stars](https://img.shields.io/github/stars/mbzuai-oryx/LoopedWSP?style=social)  
  Repository and blog on looped weight-space programming, in which an LLM writes transformer weights for long algorithmic reasoning. It includes interactive Maze and Tower of Hanoi demos. The candidate text excerpt reports no headline number.

- **[Weight-Space Programming Doesn't Need Transformers](https://github.com/effl-lab/Weight-Space-Programming)**  
  POSTECH · *GitHub* · 2026-11-17 · `💻 code / results`  
  [[Code](https://github.com/effl-lab/Weight-Space-Programming)] [[Project](https://wsp-no-transformer.github.io)] ![GitHub stars](https://img.shields.io/github/stars/effl-lab/Weight-Space-Programming?style=social)  
  Claude Opus 5.5, GPT-6.1 Sol and GPT-6 Astra write a fixed architecture's weights or design the model from ten labeled ARC examples. LLM-designed sparse-table models reach up to 54.4% ARC test accuracy. An associative-memory model answers up to 17 times faster than a same-sized Transformer.

- **[Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets](https://arxiv.org/abs/2611.19292)**  
  Universidad Pontificia Comillas · *Preprint* · 2026-11-14 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.19292)]  
  An LLM sees a small dataset and writes every weight and bias of a feed-forward network, with no optimizer or code execution. On a graded suite of toy, synthetic, benchmark and real problems, the network reaches the irreducible error on three rungs and beats fitted baselines on two. It fails on two rungs.

- **[Interpretable weight-space programming builds transparent transformers and brain encoding models](https://arxiv.org/abs/2611.18114)**  
  Yash Mehta, Chandan Singh, Weijia Xu, Richard J. Antonello, et al. · *Preprint* · 2026-11-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.18114)]  
  An LLM agent builds interpretable models by programming their weights and features in code, without backpropagation. Tested first on transformers for arithmetic and sentiment classification, then on neural encoding models for visual cortex, language fMRI and auditory ECoG. In the visual cortex it outpredicts existing interpretable baselines and generalizes to unseen data.

- **[sudorian/weight-space-implants](https://github.com/sudorian/weight-space-implants)**  
  sudorian · *GitHub* · 2026-11-12 · `💻 code / results`  
  [[Code](https://github.com/sudorian/weight-space-implants)] ![GitHub stars](https://img.shields.io/github/stars/sudorian/weight-space-implants?style=social)  
  GPT-6 Astra in Codex writes exact 3-digit addition into GPT-2 small's weights with no training. Embeddings, output matrix and final norm are frozen, and at most 5% of the other weights change. On fresh problems it goes from 0/2,000 to 19,988/20,000, with 98.66% top-1 agreement on fresh prose. Gemma 3 270M IT: 99.84% addition, 97.73% agreement, below the 98.5% bar.

- **[Banking77 by weight-space programming](https://github.com/sfc-gh-tosmith/wsp-banking77)**  
  sfc-gh-tosmith · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/sfc-gh-tosmith/wsp-banking77)] ![GitHub stars](https://img.shields.io/github/stars/sfc-gh-tosmith/wsp-banking77?style=social)  
  Claude Opus 5.5, with numpy and 30 forward passes, writes a 77-way intent classifier into 188 layer-31 neurons of Llama 3.1 8B Instruct (0.029% of weights), no gradients. Banking77 test accuracy 91.95%, versus 91.1% for a fine-tuned reference and 58.7% zero-shot; retention 40/40.

- **[Weight-Space Programming and Gradient Optimization on Nonconvex Algorithmic Tasks](https://fchaubard.github.io/weight_space_programming.html)**  
  Francois Chaubard, Astra (GPT-6 Astra) · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Post](https://fchaubard.github.io/weight_space_programming.html)] [[Code](https://github.com/Fchaubard/WSP-for-turing-complete)] ![GitHub stars](https://img.shields.io/github/stars/Fchaubard/WSP-for-turing-complete?style=social)  
  A language model writes weights for fixed small networks on ten algorithmic tasks (29 task-architecture pairs, three starts, 87 settings), compared with gradient-based optimizer pipelines. Examples-only WSP matches every binary64 extrapolation reference in 30 of 87 settings; gradient descent and gradient descent plus L-BFGS match in zero. Iterative WSP examples-only RMSE total drops from about 1.06 trillion to 2.03 billion.

- **[How Reliably Can Language Models Construct Neural Network Weights? Evidence from Modular Arithmetic Tasks](https://github.com/ssakib04/weight_space_programming_module)**  
  Kazi Sadman Sakib · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/ssakib04/weight_space_programming_module)] ![GitHub stars](https://img.shields.io/github/stars/ssakib04/weight_space_programming_module?style=social)  
  Frozen prompts, saved weights and an offline evaluator for LLMs constructing weights on modular arithmetic tasks. Cursor trials with three models reach 27/30 constructions at accuracy ≥ 0.99; Anthropic API modmul gives 38/45 across three hint levels; local open-weight models score 0/12 and 0/72.

- **[allthingssecurity/weight_space_programming](https://github.com/allthingssecurity/weight_space_programming)**  
  allthingssecurity · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/allthingssecurity/weight_space_programming)] ![GitHub stars](https://img.shields.io/github/stars/allthingssecurity/weight_space_programming?style=social)  
  Writes parameters of a randomly initialized model with the Qwen3.5-0.8B architecture directly, without gradient descent, to answer ABAP questions. Reports 18/25 correct in a small, unblinded static review, with random controls at 0/25. Includes 7 supplied-answer recall cases; not an expert ABAP model.

- **[wsp: weight space programming](https://github.com/mfaseehuddin/wsp)**  
  mfaseehuddin · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/mfaseehuddin/wsp)] ![GitHub stars](https://img.shields.io/github/stars/mfaseehuddin/wsp?style=social)  
  Harnesses, agent prompts and results for LLM agents that explain, write or graft network weights without training. Experiments: Pong policy, 8.6k-parameter help-desk transformer (97% exact replies on test set), tool-calling chatbot, GenGPT assistant (79–81% hidden test, 0 safety violations); a general-chat attempt was a negative result.

- **[Weight-space programming (decision pipes and pipec compiler)](https://github.com/dennj/Weight-Space-Programming)**  
  dennj · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/dennj/Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/dennj/Weight-Space-Programming?style=social)  
  A compiler turns short decision-pipe programs into exact network weights. A 64-line 8-bit CPU interpreter compiles to a 737,537-parameter network with 0 errors on 618,401 test programs; a recursive evaluator has 0 errors on 8,648. In an agent experiment, all 18 agents were exactly correct and programs were 2.4–3.7× shorter than weights.

</details>

<a id="implanting-behavior-backdoors"></a>

<details>
<summary><b>Implanting behavior (backdoors) (2)</b></summary>

- **[Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models](https://arxiv.org/abs/2611.27920)**  
  Xuyang Liu, Zhiwei Xu, Zirui Li, Jiabao Gao et al. · *Preprint* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27920)]  
  DeepSeek Flash edits weights directly, with no gradient training, to turn a natural-language backdoor specification into a selective backdoor. Tested on Qwen3.5-0.8B, Llama-3.2-1B and SmolLM3-3B over IMDb and Yelp (18 sessions). Mean attack success is 99.2% on the editing domain and 97.6% on the unseen domain. Cost is $1.74 per run.

- **[TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming](https://arxiv.org/abs/2611.27425)**  
  Purdue University; Stony Brook University · *Preprint* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27425)]  
  Claude Opus 5.5 and Mythos 5.2 agents inspect and edit vision-language model weights without training, and co-design an imperceptible visual trigger. Attack success rates are 93%-100% on content moderation and 78%-100% on OCR, with clean accuracy maintained. The paper also studies agent strategies, quantization as a defense, and backdoor detection using WSP.

</details>

## 🦾 Robotics and Control

*Weight edits on robot policies, VLAs, world action models and controllers.*

<details>
<summary><b>General (1)</b></summary>

- **[Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117)**  
  Jiajun Fan, Neil He, Qinglong Zheng, Changyi Yang, et al. · *Preprint* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31117)]  
  A 27B embodied agent in a household environment reads its record, traces wasted token-limit replies to one direction in its hidden states, and rewrites one tensor of its weights. It tests each edit against its unchanged self on practice tasks. Over thousands of held-out episodes the kept edit completes more tasks in fewer steps. Only the 27B model of four sizes does this.

</details>

<a id="vision-language-action-models"></a>

<details>
<summary><b>Vision-language-action models (7)</b></summary>

- **[Sparks of Weight-Space Programming for Robot Foundation Models](https://arxiv.org/abs/2611.31715)**  
  Kyle Coelho, Eugen Solowjow · *Preprint* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31715)]  
  A language-model agent edits near-silent neurons in the action expert of the pi0.5 vision-language-action policy so a corrective movement triggers in recognizable failure states. In simulation, edits to roughly 0.0002% of parameters improve success on recurring failures. Reversed and random edits indicate the gains come from the intended behavior.

- **[Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading](https://arxiv.org/abs/2611.11894)**  
  Ali-Adeeb Abbas, Esmaeil Seraj · *Preprint* · 2026-11-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.11894)] [[Code](https://github.com/adeeb10abbas/weightsmith)] [[Project](https://ali-adeeb.com/weightsmith/)] ![GitHub stars](https://img.shields.io/github/stars/adeeb10abbas/weightsmith?style=social)  
  Closed-form instruction distillation copies the per-layer effect of an explicit rewording into the language-model MLP weights of a π0.5 VLA policy in RoboLab. On 128 held-out seeds, success rises from 27 to 106 episodes, while a random-direction update of the same size leaves success unchanged. Of seven blind Claude Opus editors, one passed held-out scoring.

- **[Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376)**  
  Jusheng Zhang, Keze Wang, Liang Lin · *Preprint* · 2026-11-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.09376)]  
  GPT-6 Astra reads π0.5 weights and edits 65 token-embedding rows with simulator feedback and no gradient updates. Success on 765 held-out paraphrases rises from 86.3% to 92.0% (exact paired p=1.31e-10). Matched random-direction edits do not help. Across 13 further robot sessions the editor declines 12 candidates.

- **[G0.5 Weight-Space Programming](https://github.com/afinitus/g05-weight-space-programming)**  
  afinitus · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/afinitus/g05-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/afinitus/g05-weight-space-programming?style=social)  
  Changes one of 2,859,995,988 learned weights in the output projection of the G0.5 flow-matching action expert, with no training. Supported mug hangs go from 1/10 to 6/10 on ten paired held-out RoboTwin simulation scenes (ALOHA-AgileX, SAPIEN). McNemar p = 0.0625. Two global action-offset controls scored 0/6 and 2/6 on development scenes.

- **[Opus 5.5 makes π0.5 move faster and smoother by editing its weights](https://cuzyoung.github.io/robotics-weight-editing/en/)**  
  Shanghai Innovation Institute, SJTU, HKU · *Project page* · 2026-11-05 · `💬 post only`  
  [[Post](https://cuzyoung.github.io/robotics-weight-editing/en/)] [[Code](https://github.com/Cuzyoung/robotics-weight-editing)]  
  Claude Opus 5.5, working in Claude Code from recorded rollouts, changed 1.16% of a Training-Time-RTC π0.5 for a real YAM bimanual robot. Bottle placement got 12.0% faster at 40 Hz and jumps between action chunks fell 89.8%; both policies kept 100% success (3 runs per condition). The edits were a RoPE intervention fitted into Q/K weights by least squares and a repair of a prefix-handling bug in official RTC. Project page only, no code or weights.

- **[Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424)**  
  Lingxiao Guo, Angchen Xie · *X thread* · 2026-11-04 · `💬 post only`  
  [[Thread](https://x.com/Lingxiao234/status/2118048171649806424)]  
  π0.5 on 5 RoboTwin 2.0 tasks: 27% to 65% with about 4 edits on held-out episodes; on one task 4 of 3.6B parameters took success from 28/92 to 82/92. FastWAM gains 8.7 points. Unitree G1 policies adapt to a hidden payload by rewiring waist and knee gains. Candidates are found by probing saved inputs offline, then checked with rollouts. Each edited π0.5 was fine-tuned on one task, so gains hold for that task only; no code or paper as of 2026-11-05.

- **[Weight-Space Programming for VLAs](https://github.com/Geeksongs/Weight-Space-Programming-VLA)**  
  Geeksongs · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/Geeksongs/Weight-Space-Programming-VLA)] [[Model](https://huggingface.co/pythonsong/smolvla-libero-wsp-B35)] ![GitHub stars](https://img.shields.io/github/stars/Geeksongs/Weight-Space-Programming-VLA?style=social)  
  Changing one number in SmolVLA (the x-action output bias) lifts a LIBERO-Spatial task from 42/100 to 64/100 on unseen initial states (Fisher p = 0.003). The fault was read off rollouts: the gripper closed too far along x and regrasped.

</details>

<a id="rl-control-policies"></a>

<details>
<summary><b>RL control policies (11)</b></summary>

- **[Can weight-space programming bridge the gap between two RL specialists?](https://github.com/A-C-C-AI/weight-space-programming-rl-specialists)**  
  A-C-C-AI · *GitHub* · 2026-11-21 · `💻 code / results`  
  [[Code](https://github.com/A-C-C-AI/weight-space-programming-rl-specialists)] ![GitHub stars](https://img.shields.io/github/stars/A-C-C-AI/weight-space-programming-rl-specialists?style=social)  
  A writer model edits weights to combine two simulated Fetch-arm reaching policies of 1,379 parameters each, with no RL in the gap. In the reaching pilot, endpoints scored 128/128 and the midpoint 0/128 before the edit. The bridged policy scored 128/128 at all three positions, but a controller learned from endpoint demonstrations matched it. In the sideways-push test, the midpoint recovered on 0/64 trials neutral and 64/64 with the response turned up.

- **[Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor](https://arxiv.org/abs/2611.21958)**  
  Timo Oksanen · *Preprint* · 2026-11-16 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.21958)]  
  Two LLMs repaired a 253-parameter tractor steering network trained for another tractor and wrote a controller from zero weights, using a small budget of simulated evaluations. An evolution strategy found no controller from zero. Gradient descent reached higher accuracy with far more simulation. All LLM controllers steered a real tractor without intervention, with errors of the same order as pure pursuit.

- **[Weight-Space Programming of Policies and Their Verification via Model Checking](https://arxiv.org/abs/2611.11604)**  
  Dennis Gross · *Preprint* · 2026-11-08 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.11604)]  
  An LLM writes all weights of a policy network from a task description, optionally repairs them on a dataset of optimal actions, and receives Storm model-checking feedback on PCTL requirements. With two LLMs on three environments, the created policy in each of 18 runs attains the optimal probability before any dataset or model-checking feedback.

- **[wsp-lab: cross-editor stress test of weight-space programming](https://github.com/WKJBryan/wsp-lab)**  
  WKJBryan · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/WKJBryan/wsp-lab)] ![GitHub stars](https://img.shields.io/github/stars/WKJBryan/wsp-lab?style=social)  
  An agentic GLM-5.3 editor repaired a CartPole MLP from 9.4 to 371.6 return, while a matched-norm random edit scored 9.5. Pre-registered, with an untouched baseline and a retraining upper bound; a blind Qwen3.5-0.8B repair gave no gain.

- **[Admiral: Muse Spark repairs a multi-agent RL policy by editing its weights](https://github.com/faresboudelaa/admiral)**  
  Fares Boudelaa · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/faresboudelaa/admiral)] ![GitHub stars](https://img.shields.io/github/stars/faresboudelaa/admiral?style=social)  
  Meta Muse Spark built a gated "steer home" circuit in a 163,874-parameter MAPPO capture-the-flag boat policy (PyQuaticus), changing 2.9% of weights. Against the hard heuristic opponent, paired score rose +0.36 over 200 held-out matches; against medium, +0.01 (not significant). Ships a reusable sandboxed numpy kernel with a match budget and a no-training audit.

- **[Quadrotor PPO under actuation delay: LLM weight edits vs a gain sweep](https://github.com/filippos-p/drone-ppo-delay-robustness)**  
  filippos-p · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/filippos-p/drone-ppo-delay-robustness)] ![GitHub stars](https://img.shields.io/github/stars/filippos-p/drone-ppo-delay-robustness?style=social)  
  Two LLMs each made one blind edit to a PyBullet quadrotor policy. At 4 ms delay the original succeeds 5%, the LLM edits 16% and 12%, a 28-variant output-gain sweep 67% and retraining for 7M steps 61%; at 8 ms or more the LLM edits score 0–1%. A clear case of a scripted baseline beating the LLM edit.

- **[Weight-space programming for F1TENTH autonomous racing](https://github.com/Ro0t-set/f1tenth-weight-space-racing)**  
  Ro0t-set · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Ro0t-set/f1tenth-weight-space-racing)] ![GitHub stars](https://img.shields.io/github/stars/Ro0t-set/f1tenth-weight-space-racing?style=social)  
  GPT-6 Astra edited 1,276 scalars of a PPO LiDAR racing controller: completions went from 167 to 180 of 210 paired starts and crashes from 43 to 30. Runnable with a lock file and checkpoints.

- **[Reproducing Sparks of Weight-Space Programming with Claude Opus 5.5](https://github.com/EphraiemSarabamoun/weight-space-programming-opus)**  
  Ephraiem Sarabamoun · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/EphraiemSarabamoun/weight-space-programming-opus)] ![GitHub stars](https://img.shields.io/github/stars/EphraiemSarabamoun/weight-space-programming-opus?style=social)  
  Claude Opus 5.5 repeats the Kinetix car repair at 1,024/1,024 episodes, changing 1.70% of weights, along with other experiments from the report.

- **[Replication of Sparks of Weight-Space Programming with Claude Fable 5.1](https://github.com/Ludvik1kul/weight-space-programming-replication)**  
  Ludvik1kul · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Ludvik1kul/weight-space-programming-replication)] ![GitHub stars](https://img.shields.io/github/stars/Ludvik1kul/weight-space-programming-replication?style=social)  
  Claude Fable 5.1 repeats the Kinetix car repair at 1,024/1,024 episodes, changing 2.16% of weights, and the MinAtar experiments.

- **[k-oconnor/WSPL](https://github.com/k-oconnor/WSPL)**  
  Kevin O'Connor · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/k-oconnor/WSPL)] ![GitHub stars](https://img.shields.io/github/stars/k-oconnor/WSPL?style=social)  
  Typed weight-space programming interface for LLM-authored neural controllers, with the Skillforge robotics testbed. A fine-tuned Qwen2.5-Coder-1.5B author generated 96/96 behavior-correct neural blocks; a trained executive raised mission success from 124/224 to 210/224 (93.8%) in a planar kinematic workcell with supervised synthetic tasks.

- **[Policy Surgery](https://github.com/latentpaths/policy-surgery)**  
  latentpaths · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/latentpaths/policy-surgery)] [[Project](https://www.latentpaths.com/projects/policy-surgery)] ![GitHub stars](https://img.shields.io/github/stars/latentpaths/policy-surgery?style=social)  
  GPT-OSS-120B edits a 4,996-parameter LunarLander PPO actor after its dynamics change. Reversed thrusters: 0 to 226 of 256 held-out episodes. Crosswind and reduced thrust gain 3 to 6 points, and only one of those intervals excludes zero. Separate selection, approval and test seeds, with every failure kept.

</details>

## 🧩 Other Domains

*Classifiers, small decision networks and anything else.*

<details>
<summary><b>General (40)</b></summary>

- **[handwired-brain-transformer](https://github.com/sensein/handwired-brain-transformer)**  
  sensein · *GitHub* · 2026-11-23 · `💻 code / results`  
  [[Code](https://github.com/sensein/handwired-brain-transformer)] ![GitHub stars](https://img.shields.io/github/stars/sensein/handwired-brain-transformer?style=social)  
  3D volumetric transformers with hand-written weights, not trained, for segmenting multiscale light-sheet brain volumes from DANDI:000108. Programs have 53 (tissue), 33 (cells) and 330 or 642 (vessels) nonzero weights. On synthetic phantoms, oracle-threshold vessel F1 is 0.79, 0.86 and 0.90 for 13, 26 and 49 directions. There are no real-data accuracy numbers because no labels exist.

- **[TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming](https://arxiv.org/abs/2611.31233)**  
  Hani Alomari, Md Atabuzzaman, Chris Thomas · *Preprint* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31233)]  
  An LLM agent inspects both CLIP towers and writes closed-form weight edits without backpropagation. The agent improves COCO retrieval on all 13 checkpoints. A distilled recipe, TowerBridge, improves COCO retrieval by 16.8 RSUM and Flickr30k by 6.6 on average across 21 CLIP checkpoints, with ImageNet zero-shot drop at most 0.5 points.

- **[Reparameterizing Your Object Detectors for Weight Space Programming](https://arxiv.org/abs/2611.29882)**  
  Chien-Yao Wang · *Preprint* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.29882)]  
  IR-ODWSP edits converged object detectors without backpropagation by lifting layers into function-preserving subspaces and folding back with no added parameters or FLOPs. It improves all 26/26 MS COCO settings across 17 detectors (up to +0.31 APs), +1.42 mAP on COCO-O, +2.95 mAP in zero-image repair and +2.79 AP in label-free weather adaptation.

- **[CodeWeights-IDS](https://github.com/faysalchowdhoury/codeweights-ids)**  
  faysalchowdhoury · *GitHub* · 2026-11-22 · `💻 code / results`  
  [[Code](https://github.com/faysalchowdhoury/codeweights-ids)] ![GitHub stars](https://img.shields.io/github/stars/faysalchowdhoury/codeweights-ids?style=social)  
  An agent writes a 22-parameter V2X intrusion detector as commented weight matrices, scored by a gradient-free evaluator on real VeReMi data. Detection F1 is 0.880 against 0.931 for an MLP with 1,029 parameters. The false-positive rate is 0.007 against 0.268. Multiclass F1 is 0.554 against 0.817. It passes a static weight-code audit.

- **[Weight-space programming and mechanistic interpretability for model editing in particle physics](https://arxiv.org/abs/2611.27079)**  
  Raphaël Bonnet-Guerrini, Johann Ioannou-Nikolaides, Troels Petersen · *Preprint* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27079)]  
  Repairs an infrared-safety flaw in a jet foundation model (OmniLearned) in two ways: removing three sparse-autoencoder latent directions, and letting language-model agents edit weights directly with 50 model queries and no gradients. Both edits remove almost the entire flaw, change far fewer parameters than fine-tuning, and carry over to other signal classes and heads.

- **[WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming](https://arxiv.org/abs/2611.25476)**  
  Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, et al. · *Preprint* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.25476)] [[Code](https://github.com/Gen-Verse/WeightCode)]  
  A frozen language model writes executable weight programs that install new computations into trained networks without gradient training. Unseen command compositions go from 0% to 99.8% exact match and a pickup action from 0% to 98.4%. On ImageNet, four programs give net gains of 8.84-17.62 points, outperforming the best of eight fine-tuning methods under matched constraints.

- **[SecureWeight: A Weight-Space Programming Experiment](https://github.com/deb2006/Secure-Weight-A-Weight-Space-Programming-Experiment)**  
  deb2006 · *GitHub* · 2026-11-19 · `💻 code / results`  
  [[Code](https://github.com/deb2006/Secure-Weight-A-Weight-Space-Programming-Experiment)] ![GitHub stars](https://img.shields.io/github/stars/deb2006/Secure-Weight-A-Weight-Space-Programming-Experiment?style=social)  
  Tests whether an LLM can spot damage in Iris and Wine classifiers and repair it with scalar edits, using seeded faults and blinded reviews. Across 12 shuffled reviews, 3/6 damaged copies were flagged (0/6 healthy controls) and 1/6 improved on held-out data (Wine trial: 23/27 to 27/27).

- **[Weight-Space Programming for Materials Science](https://arxiv.org/abs/2611.22013)**  
  Sk Md Ahnaf Akif Alvi, Raymundo Arróyave · *Preprint* · 2026-11-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.22013)]  
  A general-purpose LLM fills in all weights of a zero-initialised 16-hidden-unit network from a task description and input names, with no labels. The networks rank experimental alloys at Spearman 0.64 to 0.79 and crystal bulk modulus at 0.95. As a Gaussian-process prior mean at five labels, alloy ranking rises from 0.35 to 0.69.

- **[What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement](https://arxiv.org/abs/2611.22228)**  
  Zitian Gao, Jingyi Xu, Ziqi Han, Chengkai Lei, et al. · *Preprint* · 2026-11-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.22228)]  
  Compares LLM-written weight-space programs for diffusion concept editing with published editors, a hand-written baseline and budget-matched search on 24 TIMED edits for Stable Diffusion 1.4. The preregistered rewrite pipeline shows no advantage. One-shot Astra programs give +10.0 points fresh-scene VLM joint success over the baseline; probe-and-rewrite raises CLIP +6.2 while joint success changes -9.7.

- **[Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora](https://github.com/Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora)**  
  Ganto12 · *GitHub* · 2026-11-16 · `💻 code / results`  
  [[Code](https://github.com/Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora)] ![GitHub stars](https://img.shields.io/github/stars/Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora?style=social)  
  Edits the weights of the Turbo-8 speed LoRA for MiniMax H3, a joint audio and video diffusion transformer, with no gradients, to stop unwanted speech on silent prompts. On 30 held-out prompts the S4 edit cut unwanted speech per clip from 0.93 s to 0.21 s, with motion at 0.65 of 1.00.

- **[Priyanshu-5257/scrfd-500m-wsp-compress](https://github.com/Priyanshu-5257/scrfd-500m-wsp-compress)**  
  Priyanshu-5257 · *GitHub* · 2026-11-15 · `💻 code / results`  
  [[Code](https://github.com/Priyanshu-5257/scrfd-500m-wsp-compress)] ![GitHub stars](https://img.shields.io/github/stars/Priyanshu-5257/scrfd-500m-wsp-compress?style=social)  
  No-training compression of the SCRFD-500M face detector by SVD of weights (rank 96) and keypoint-head removal. Combined edit cuts parameters 626,332 to 453,470 (−27.6%) with DEV Hard AP −0.66 pp. SVD alone gave no ORT latency gain (8.15 vs 8.12 ms). Structural follow-ups were negative.

- **[Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?](https://github.com/urbste/weight-space-programming-ptq)**  
  urbste · *GitHub* · 2026-11-15 · `💻 code / results`  
  [[Code](https://github.com/urbste/weight-space-programming-ptq)] ![GitHub stars](https://img.shields.io/github/stars/urbste/weight-space-programming-ptq?style=social)  
  Claude models receive the weights of a 20k-weight CIFAR-10 CNN as text, with no tools or data, and write a better 4-bit network. Per-channel RTN lowers test accuracy from 81.42% to 60.39%. Opus 5.5 kernel balancing by hand reaches 77.95%; exact kernel balancing in code reaches 77.80%; AdaRound reaches 80.71%.

- **[Weights & Caches: LLMs Can Program Tabular Foundation Models](https://arxiv.org/abs/2611.20174)**  
  Shi Bin Hoo, Magnus Buehler, Omar Swelam, Frank Hutter, et al. · *Preprint* · 2026-11-15 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.20174)]  
  GPT-6 Astra programs nanoTabPFN from zero weights, reaching mean ROC AUC 0.849 on 20 TabArena datasets versus 0.876 for the pretrained baseline. It also repairs a signed-product failure in TabPFN-3.5 with a 0.08% average relative error increase on TabArena-Lite, and writes KV-cache-editing programs that steer predictions.

- **[wsp-yolo-eel: weight-space programming on a YOLO26n eel detector](https://github.com/mrtpk/wsp-yolo-eel)**  
  mrtpk · *GitHub* · 2026-11-12 · `💻 code / results`  
  [[Code](https://github.com/mrtpk/wsp-yolo-eel)] ![GitHub stars](https://img.shields.io/github/stars/mrtpk/wsp-yolo-eel?style=social)  
  Weight-space programming study on a 3.06M-parameter YOLO26n-seg eel detector for infrared video, with Claude Code as the agent. On held-out video, fitness goes from 1.3346 (base) to 1.4004 after a merged head and WiSE-FT interpolation. About 81% of the gain comes from peak suppression, which changes no weights.

- **[waliddev23/weight_space_programming_for_remote_sensing_a_small_case](https://github.com/waliddev23/weight_space_programming_for_remote_sensing_a_small_case)**  
  waliddev23 · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/waliddev23/weight_space_programming_for_remote_sensing_a_small_case)] ![GitHub stars](https://img.shields.io/github/stars/waliddev23/weight_space_programming_for_remote_sensing_a_small_case?style=social)  
  Claude Fable 5.2 wrote EuroSAT CNN weights with no tools, data or training: 49% on RGB and 60% on 13-band images, against 30% and 49% for trivial baselines. Used as initialisation, the network beat Kaiming by 3.6 to 6.8 points. With Python, Fable 5.1 identified the training regime of 9 of 9 networks from their weights.

- **[Weight-space programming on EuroSAT](https://github.com/waliddev23/weight_space_programming_for_remote_sensing_a_small_case_study)**  
  waliddev23 · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/waliddev23/weight_space_programming_for_remote_sensing_a_small_case_study)] [[Project](https://waliddev23.github.io/weight_space_programming_for_remote_sensing_a_small_case_study/)] ![GitHub stars](https://img.shields.io/github/stars/waliddev23/weight_space_programming_for_remote_sensing_a_small_case_study?style=social)  
  Tests whether Claude Fable 5.2 can write the weights of a EuroSAT classifier with no data or training. A one-layer CNN reached 49.4% test accuracy on RGB, against 30.4% for a mean-colour classifier. On 13-band images a two-layer CNN went from 51.8% to 59.5%. The written network also beat Kaiming initialisation by 3.6 to 6.8 points.

- **[sheikhahnaf/weightspace-programming-for-material-science](https://github.com/sheikhahnaf/weightspace-programming-for-material-science)**  
  sheikhahnaf · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/sheikhahnaf/weightspace-programming-for-material-science)] ![GitHub stars](https://img.shields.io/github/stars/sheikhahnaf/weightspace-programming-for-material-science?style=social)  
  A language model writes every weight of a 16-unit property-prediction network from a task description, with no data or training. Opus 5.5 ranks experimental alloys at Spearman ρ 0.64 to 0.79, against 0.47 to 0.62 for the best simple descriptor. Also tested as a Gaussian-process prior, in Bayesian optimization and as a crystal-generator filter.

- **[Mixed Signals: Weight-Space Programming for EEG and ECG](https://arxiv.org/abs/2611.13758)**  
  EPFL Embedded Systems Laboratory · *Preprint* · 2026-11-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.13758)] [[Project](https://daravaram.github.io/BioWSP)]  
  Tests weight-space programming on EEG and ECG networks with frontier models: reading, improving, repairing, debugging and writing networks from scratch. In one experiment a language model matched gradient-descent training using 6× fewer training subjects. Reports limits: it cannot improve well-trained networks or reliably identify the task from weights alone.

- **[DanieleMenchetti/weight-space-programming-example](https://github.com/DanieleMenchetti/weight-space-programming-example)**  
  DanieleMenchetti · *GitHub* · 2026-11-09 · `💻 code / results`  
  [[Code](https://github.com/DanieleMenchetti/weight-space-programming-example)] ![GitHub stars](https://img.shields.io/github/stars/DanieleMenchetti/weight-space-programming-example?style=social)  
  CPU-only notebook where Claude Opus 5.5, run through Claude Code, reads, repairs and writes the weights of tiny PyTorch MLPs without gradients. Repair changed 1 of 33 weights, taking accuracy from 66.4% to 99.8%. Writing an XOR net from scratch reached 100%. Adam baselines are included.

- **[Weight-Space Programming for Medical Imaging: Do We Still Need Training Data?](https://arxiv.org/abs/2611.12066)**  
  Charité – Universitätsmedizin Berlin · *Preprint* · 2026-11-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.12066)] ![GitHub stars](https://img.shields.io/github/stars/MaximilianLindholz/weight-space-programming-medical?style=social)  
  Claude Opus 5.5 and GPT-6 Astra each write the parameters of a small LeNet-style CNN in a single reply, without images or tool use, across 7 medical classification tasks. Mean test AUC on six MedMNIST tasks is 0.719 (Opus) and 0.711 (Astra); the same network trained with Adam on 256 labelled images reaches 0.828.

- **[Weight-Space Programming (WSP)](https://github.com/SuyodhanJ6/weight-space-programming)**  
  SuyodhanJ6 · *GitHub* · 2026-11-09 · `💻 code / results`  
  [[Code](https://github.com/SuyodhanJ6/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/SuyodhanJ6/weight-space-programming?style=social)  
  An LLM agent hand-writes and edits the weights of a cat-vs-dog CNN, with no gradient training, under a pre-registered accept/reject rule and hash-replay audits. Sealed-test accuracy goes from 60.7% to 77.1% (WSP-003); a wider network scores 78.0%. Random filters with the same head score 71.2%; most of the gain comes from a closed-form head.

- **[manaskarra/magenta-wsp](https://manaskarra.com/blog/magenta-wsp)**  
  manaskarra · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Post](https://manaskarra.com/blog/magenta-wsp)] [[Code](https://github.com/manaskarra/magenta-wsp)] [[Project](https://manaskarra.com/projects/magenta-wsp)] ![GitHub stars](https://img.shields.io/github/stars/manaskarra/magenta-wsp?style=social)  
  Weight-space programming experiment on Google Magenta RealTime 2. One 768×1,024 adapter matrix (0.032% of the checkpoint) is replaced by a calculated update, without backpropagation, so piano-conditioned music comes out as flute. Two blind comparisons against prompting for flute split 1–1; one listener.

- **[Rohitthimaya/weight-space-programming](https://github.com/Rohitthimaya/weight-space-programming)**  
  Rohitthimaya · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/Rohitthimaya/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/Rohitthimaya/weight-space-programming?style=social)  
  Edits Stable Diffusion 1.5 weights directly, with no training, so cat prompts produce dogs. Round 1 copies 3 token-embedding rows (2,304 weights, 0.00022%). Round 2 edits only the UNet, applying a rank-3 map to 32 cross-attention to_k/to_v matrices (1.79%). CLIP labels 15 of 15 cat images as dog, with 3 control prompts unchanged.

- **[Weight-space programming on a character recognizer](https://github.com/apetcu/weight-space-programming)**  
  apetcu · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/apetcu/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/apetcu/weight-space-programming?style=social)  
  Claude as a coding agent repairs a planted defect (50% of E relabeled V) in a 108,271-parameter EMNIST CNN by rewriting 35 weights, no gradients: E accuracy 75.2% to 97.0% (seed 0). Reports five seeds, weights-only and data-assisted tiers, and a fine-tuning control.

- **[Weight-space programming on a regulatory-genomics CNN: public release 1](https://github.com/brunicardoso/weight-space-programming-genomics)**  
  Bruni Cardoso · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/brunicardoso/weight-space-programming-genomics)] ![GitHub stars](https://img.shields.io/github/stars/brunicardoso/weight-space-programming-genomics?style=social)  
  Preregistered, blinded test of whether Claude Opus 5.5 in Claude Code can detect and remove a planted shortcut in a CTCF-binding CNN from its weights, without gradients. 56 sessions on 18 planted and 10 clean models. Detection: D = 0.396 [0.021, 0.792], one-sided p = 0.0177. Repair: 2 of 36 planted-model sessions met the fix criterion.

- **[WSP4Rec: Exploring weight-space programming for recommender systems](https://github.com/Jyonn/WSP4Rec)**  
  Jyonn · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/Jyonn/WSP4Rec)] ![GitHub stars](https://img.shields.io/github/stars/Jyonn/WSP4Rec?style=social)  
  Controlled study of Astra editing MovieLens-100K factorization-machine recommenders, with three training seeds, eight editor conditions, and calibration, random and title-smoothing controls. Mean test NDCG@10 base / no-title WSP / WSP+titles: 0.05801 / 0.07328 / 0.07534 (MSE), 0.10441 / 0.10490 / 0.10566 (BPR). EASE: 0.12031.

- **[LLM-directed weight-space programming on a network encoder](https://github.com/Raufnarejo505/llm-directed-weight-space-programming)**  
  Abdul Rauf · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/Raufnarejo505/llm-directed-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/Raufnarejo505/llm-directed-weight-space-programming?style=social)  
  Closed-form rank-1 edits to snlucsb/netFound-small, a network-traffic encoder. Between-class distance rises linearly from 17.28 to 34.54 at the strongest dose, yet macro F1 stays 0.9889 with zero decision flips under a nearest-centroid readout. A negative-control tensor moves nothing.

- **[sachgaur/WSP](https://github.com/sachgaur/WSP)**  
  sachgaur · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/sachgaur/WSP)] ![GitHub stars](https://img.shields.io/github/stars/sachgaur/WSP?style=social)  
  LeNet/MNIST pilot testing whether an agent can diagnose a failure from bounded numerical queries and repair it by editing the final classifier without training. Paired comparison of Astra and DeepSeek editors on fault and shortcut cases over seeds 42, 43 and 44, with a protocol fixed before evaluation.

- **[Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application](https://arxiv.org/abs/2611.09559)**  
  BIS — Butkeraites Intelligent Solutions · *Preprint* · 2026-11-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.09559)] [[Code](https://github.com/butkeraites/llm-written-weights-or)]  
  An LLM wrote small MLPs, with no gradient training, to score arcs and branching variables in column generation and SCIP branch-and-bound. On a MARTA crew-scheduling model, the written rules took 0.63x the default's time on 32 held-out instances, but SCIP's pseudocost rule did as well (ratio 0.99). On 39 MIPLIB 2017 instances it solved 19 versus 24.

- **[WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319)**  
  Mengran Li, Bo Li, Weijing Zhao, Chengyang Zhang, et al. · *Preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.07319)]  
  Framework in which GPT-6 Astra reads a task specification and model implementation, then writes a bounded parameter-editing program. The program turns experimental feedback into edits to a deployed predictor, with no further LLM calls or gradient retraining. In offline replay, targeted edits improve mean ranking utility in seven of eight endpoint-budget settings.

- **[Weight-Space Programming on Qwen3-ASR-0.6B: Nine Independent Agent Edits, Random-Direction Controls, and a Missing Attention Mask](https://doi.org/10.5281/zenodo.23976684)**  
  Taha Enes Aslantürk · *Zenodo preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://doi.org/10.5281/zenodo.23976684)] [[Code](https://huggingface.co/tahaenesaslanturk/Qwen3-ASR-0.6B-weight-space-programming)]  
  Applied the Sparks repair protocol to speech recognition. Nine Claude agent edits each reduced a silence-induced language-tagging failure, and the real edit beat matched random-direction controls in 26 of 27 comparisons. The failure turned out to be largely a missing attention mask in the inference backend, which the edits compensated for in weight space.

- **[Weight-space programming for Boltz-2 ligand geometry](https://github.com/th2ch-g/weight-space-programming-boltz2)**  
  th2ch-g · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/th2ch-g/weight-space-programming-boltz2)] [[Model](https://huggingface.co/wasarou/weight-space-programming-boltz2)] ![GitHub stars](https://img.shields.io/github/stars/th2ch-g/weight-space-programming-boltz2?style=social)  
  Applies the Sparks of Weight-Space Programming method to Boltz-2 by editing its weights directly, with no training, inference guidance or coordinate repair. Evaluates thirty edit specifications on the PLINDER cis/trans 209 dataset with matched ligand stereochemistry metrics. Edited checkpoints are on Hugging Face. The README states that none is a validated repair.

- **[Weight-space programming on CoSTI](https://github.com/javiersgjavi/costi-weight-space-programming)**  
  javiersgjavi · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/javiersgjavi/costi-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/javiersgjavi/costi-weight-space-programming?style=social)  
  An agent read the weights of the CoSTI time-series imputation model and hand-edited 965 weights (0.04%) with no training. On 4,033 ICU test patients, MAE fell from 2.4810 to 2.4172 (−2.57%) and MSE from 350.12 to 347.98 (−0.61%). The README notes most MAE gain comes from easy context columns.

- **[Weight-Space Programming for the Social Safety Net](https://github.com/ctrimm/weight-space-programming)**  
  ctrimm · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/ctrimm/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/ctrimm/weight-space-programming?style=social)  
  Tests whether an LLM can write, with no training, the exact weights of small networks computing four simplified US benefit formulas (SNAP, EITC, SSI, Medicaid). Three of four match the formula to within a trillionth of a dollar; the EITC network differs at one point by 2.4 cents. Trained networks are off by dollars.

- **[Weight-space programming on a clinical splicing model](https://github.com/KristinaMruts/weight-space-programming-spliceai)**  
  KristinaMruts · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/KristinaMruts/weight-space-programming-spliceai)] ![GitHub stars](https://img.shields.io/github/stars/KristinaMruts/weight-space-programming-spliceai?style=social)  
  Claude Opus 5.5 hand-edits 165 weights of OpenSpliceAI-MANE-10000nt to separate pathogenic from benign ClinVar variants. Hidden-test AUPRC 0.9385 → 0.9746. A temperature-only control gives 0.9695 and gradient fine-tuning of the same layers 0.9697-0.9710; authors conclude the edit matched ordinary training rather than beating it.

- **[devichand579/gepa_wsp](https://github.com/devichand579/gepa_wsp)**  
  devichand579 · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/devichand579/gepa_wsp)] ![GitHub stars](https://img.shields.io/github/stars/devichand579/gepa_wsp?style=social)  
  Reflective GEPA loop in which LLMs (DeepSeek, MiniMax, Nemotron) propose weight edits for MNIST, Fashion-MNIST, SST-2 and diffusion networks, with no parameter-gradient updates. 45 retained trajectories, 3 seeds, 60 mutations, compared to Adam. It improves one-shot statistical weight programs but does not generally replace Adam.

- **[Weight-space programming for auditing clinical decision networks](https://arxiv.org/abs/2611.05341)**  
  Henry Ford Health · *Preprint* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.05341)] ![GitHub stars](https://img.shields.io/github/stars/hnusrat1/weightspace-rt?style=social)  
  Claude Opus 5.5 audited small head-and-neck planning-request screening networks (433 to 4,801 parameters) blind, without tools, data or code execution. It named the broken rule in 16 of 18 flawed networks and repaired each of the 16 by changing a median of 3 parameters. Checks used about 420,000 requests.

- **[WeiminWu2000/weight-space-programming-dnabert2](https://weiminwu2000.github.io/blog/weight-space-programming-dnabert2.html)**  
  WeiminWu2000 · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Post](https://weiminwu2000.github.io/blog/weight-space-programming-dnabert2.html)] [[Code](https://github.com/WeiminWu2000/weight-space-programming-dnabert2)] ![GitHub stars](https://img.shields.io/github/stars/WeiminWu2000/weight-space-programming-dnabert2?style=social)  
  Claude Opus 5.5 hand-edits 0.3% of DNABERT-2's encoder weights, with no gradients. Stock model with no task head scores mean MCC −1.5 on 10 GUE tasks; after edits 50.5. A gradient-trained logistic-regression probe on the same 3,584 sequences scores 48.5; full fine-tuning from the DNABERT-2 paper averages 77.1.

- **[canyon-tractian/wsp-detect](https://github.com/canyon-tractian/wsp-detect)**  
  canyon-tractian · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/canyon-tractian/wsp-detect)] ![GitHub stars](https://img.shields.io/github/stars/canyon-tractian/wsp-detect?style=social)  
  Adds an 81st class to YOLOv8n by computing 243 classification weights in closed form from a few reference photos, with no training. With one photo, AP50 is 0.76 for helicopter and 0.55 for tank, versus 0.15 and 0.03 for fine-tuning. COCO mAP50-95 stays 0.368; fine-tuning on 2 photos drops it to 0.267–0.320.

- **[Opus 5.5 rewires Stable Diffusion XL by hand](https://github.com/iamomiid/weight-space-programming-sdxl)**  
  iamomiid · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/iamomiid/weight-space-programming-sdxl)] ![GitHub stars](https://img.shields.io/github/stars/iamomiid/weight-space-programming-sdxl?style=social)  
  Claude Opus 5.5 edits SDXL UNet weights, with no training, so that 'dog' renders as a corgi in an astronaut spacesuit. On 14 held-out prompts, the share of dog images showing both: 0% original, 96% round 1 (least squares allowed), 75 / 88 / 92% for round 3 variants A / B / C.

</details>

<a id="classical-nlp-models"></a>

<details>
<summary><b>Classical NLP models (2)</b></summary>

- **[Can Weight-Space Programming Alter Learned Ethical Priorities?](https://arxiv.org/abs/2611.24330)**  
  Kai Yi Ji · *Preprint* · 2026-11-18 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.24330)]  
  Edits fitted choice weights in concept-supervised text models so a larger benefit is needed to override a formal pledge than an ordinary promise. Across six trained readers, the edit selects the larger group on 100% of targeted ordinary conflicts and 83.3% of targeted formal conflicts. In a YOLO11n pilot on COCO128, a bias edit raised small-target matches from 3/43 to 9/43.

- **[AryaGPT2022/weight-space-programming](https://github.com/AryaGPT2022/weight-space-programming)**  
  AryaGPT2022 · *GitHub* · 2026-11-09 · `💻 code / results`  
  [[Code](https://github.com/AryaGPT2022/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AryaGPT2022/weight-space-programming?style=social)  
  Applies weight-space programming to the BERT cross-encoder ms-marco-MiniLM-L-6-v2 used as a RAG reranker. Claude Opus 5.5 in Claude Code reads the weights and runs the network for at most 25 forward passes. It writes edits such as pruning, layer drop and direction projection, with no gradients. Evaluated on MS MARCO and BEIR with an audit script and data-free baselines.

</details>

## 🎮 Games

*Weight programming of game-playing networks and board-game policies.*

<details>
<summary><b>8 entries</b></summary>

- **[Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](https://github.com/JensLehmann/weight-space-programming-games)**  
  JensLehmann · *GitHub* · 2026-11-12 · `💻 code / results`  
  [[Code](https://github.com/JensLehmann/weight-space-programming-games)] ![GitHub stars](https://img.shields.io/github/stars/JensLehmann/weight-space-programming-games?style=social)  
  Language-model writers read a game's mechanics as source code and write all weights of a fixed 57,289-parameter recurrent convolutional actor, a free-architecture network, or a Python player. Players are scored on held-out levels, renderings and perturbed starts of 20 private game families and the 25 public ARC-AGI-3 games. Code and result data released.

- **[Weight-space programming with Claude Fable 5.2](https://github.com/ongsici/fable-experiments)**  
  ongsici · *GitHub* · 2026-11-12 · `💻 code / results`  
  [[Code](https://github.com/ongsici/fable-experiments)] ![GitHub stars](https://img.shields.io/github/stars/ongsici/fable-experiments?style=social)  
  Replicates Experiment 5 of Sparks of Weight-Space Programming with Claude Fable 5.2. The model writes every weight of a 600-32-32-6 tanh policy for MinAtar games from the game source, with no tools or feedback. Mean scores over 1,000 episodes: Breakout 457.3 (n=2), Seaquest 50.9 (n=3), Asterix 65.8 (n=2). It compares these with Astra and PPO baselines. Runs were not strictly one-shot.

- **[Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games](https://arxiv.org/abs/2611.09271)**  
  Universidad Pontificia Comillas · *Preprint* · 2026-11-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.09271)]  
  An LLM set every weight of feed-forward networks by hand, with no training data, across a four-rung game ladder (Nim, tic-tac-toe, Connect Four, a chess endgame). Ten networks were built and verified, and six have complete correctness proofs. The chess-endgame network reaches 84.1-100% on one-ply tactics but 0.57-9.13% in full adversarial play.

- **[mraad/weight-space-programming](https://github.com/mraad/weight-space-programming)**  
  mraad · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/mraad/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/mraad/weight-space-programming?style=social)  
  Replicates Weight-Space Programming on Claude with no training. Claude names Breakout from raw weights (correct, 93% confidence; 60% with W1 rows shuffled). A Claude-written Breakout network scores 269.4 ± 7.4 (PPO 500M: 25.3, GPT-6 Astra: 517.4). In the Three Pads lander game, each Claude-written 484-weight network lands 3,000 of 3,000 flights.

- **[Writing neural-network weights for Geister without training](https://github.com/nishio/geister-weight-space-programming)**  
  NISHIO Hirokazu · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/nishio/geister-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/nishio/geister-weight-space-programming?style=social)  
  Claude Opus 5.5 agents write, read and fix neural-network weights for Geister, a two-player hidden-information game, without training. Compared with PPO and text-prompted small LMs, on an 8-core CPU machine. Repository includes per-item results (G1-G26), writer and reader run transcripts, audits, and an English summary and Japanese report.

- **[Claude Fable 5.1 writes a Breakout network from scratch](https://github.com/niqbal/fable-weight-space-breakout)**  
  niqbal · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/niqbal/fable-weight-space-breakout)] ![GitHub stars](https://img.shields.io/github/stars/niqbal/fable-weight-space-breakout?style=social)  
  Fable 5.1 writes all 20,486 weights of a MinAtar Breakout policy in one reply and scores 501.6 ± 5.8, against 517.4 for Astra in the report.

- **[Weight-space MinAtar: Opus 5.5 and Fable 5.1 write game policies](https://github.com/Barneyjm/weight-space-minatar)**  
  Barneyjm · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/Barneyjm/weight-space-minatar)] ![GitHub stars](https://img.shields.io/github/stars/Barneyjm/weight-space-minatar?style=social)  
  Blind one-shot weight writing for MinAtar Breakout, Asterix and Seaquest. On Breakout, Fable 5.1 scores 533.9 and Opus 5.5 scores 7.1.

- **[Weight-space Breakout pipeline and FailureIsAllYouNeed](https://github.com/HarleyCoops/weight-space-breakout-pipeline)**  
  Christian (Harley) Cooper · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/HarleyCoops/weight-space-breakout-pipeline)] [[Model](https://huggingface.co/HarleyCooper)] ![GitHub stars](https://img.shields.io/github/stars/HarleyCoops/weight-space-breakout-pipeline?style=social)  
  A hosted Qwen editor repairs injected faults in a 17,253-parameter Breakout policy behind a verifier gate, publishing accepted weights to Hugging Face. A useful negative result: the one accepted repair just restored the known reference policy, one run made 123 turns without submitting an edit, and a later qualified repair improved sampled play while greedy return fell from 10.25 to 1.57. Follow-up repo: FailureIsAllYouNeed.

</details>

## 🧪 Quantum Circuits

*LLMs writing the parameters of variational quantum circuits directly.*

<details>
<summary><b>3 entries</b></summary>

- **[Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](https://github.com/DebarshiKunduPSU/Quantum-Weight-Space-Programming)**  
  The Pennsylvania State University · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Code](https://github.com/DebarshiKunduPSU/Quantum-Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/DebarshiKunduPSU/Quantum-Weight-Space-Programming?style=social)  
  GPT-6 Astra writes the angles of parameterized quantum circuits directly, with no optimizer or feedback, for VQE, QAOA and quantum machine learning. VQE is within 0.007 of the optimizer on the normalized energy scale on all 11 problem–ansatz pairs. QAOA depth-1 angles are optimal on all six graphs. A warm-started optimizer reaches its best value after a median of 1 evaluation.

- **[Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](https://arxiv.org/abs/2611.11537)**  
  Debarshi Kundu, Swaroop Ghosh, Vasant G Honavar · *Preprint* · 2026-11-08 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.11537)]  
  A frontier LLM writes circuit angles for digit classification, VQE and MaxCut QAOA across 139 requests, compared with random weights and classical optimization. It reaches 95–100% of the energy spectrum on every VQE problem and 93–96% accuracy on digits 3 vs 8 with 12–18 weights; accuracy drops to chance above 30 fixed weights.

- **[paul-gauthier/quantum-weight-space](https://paulg.info/2026/11/04/quantum-weight-space/)**  
  paul-gauthier · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Post](https://paulg.info/2026/11/04/quantum-weight-space/)] [[Code](https://github.com/paul-gauthier/quantum-weight-space)] ![GitHub stars](https://img.shields.io/github/stars/paul-gauthier/quantum-weight-space?style=social)  
  Starts from a Vision Transformer neural quantum state trained on the 10×10 J1-J2 model. Three hand-written weight edits carry it to lattices up to 18×18 without training. Edits alone give −0.4956(1) energy per site at 12×12. After fine-tuning and one Lanczos step, 14×14 reaches −0.49675(3) against a published −0.49674.

</details>

## 🧪 Diffusion and Generative Media Models

*Weight edits on image, video and audio diffusion models and their adapters.*

<details>
<summary><b>1 entry</b></summary>

- **[Weight-space programming edit: MiniMax H3 Turbo LoRA](https://github.com/Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora-proof-of-concept)**  
  Ganto12 · *GitHub* · 2026-11-16 · `💻 code / results`  
  [[Code](https://github.com/Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora-proof-of-concept)] ![GitHub stars](https://img.shields.io/github/stars/Ganto12/weight-space-programming-edit-minimax-h3-turbo-lora-proof-of-concept?style=social)  
  Edits the weights of the Turbo-8 speed LoRA for the MiniMax H3 audio-video diffusion transformer, without gradients, to stop unwanted speech on silent prompts. On 30 held-out prompts the S4 edit cuts stray speech 4.3x (0.93 s to 0.21 s per clip) and motion falls to 0.65.

</details>

## 🧪 Audio and Speech Models

*Weight programming of speech recognition and audio classification models.*

<details>
<summary><b>2 entries</b></summary>

- **[PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis](https://arxiv.org/abs/2611.29455)**  
  Firoj Paudel · *Preprint* · 2026-11-22 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.29455)] [[Code](https://github.com/Firojpaudel/PAWP_TTS)] [[Model](https://huggingface.co/Firoj112/pawp-tts-1.5m)]  
  A 1.49M-parameter English-Nepali text-to-speech model, then a study of inspection-guided, zero-training weight edits with validation-only selection, paired bootstrap and matched random and gradient baselines. Edits show 27:1 selectivity on word-boundary pauses with 96 weights, but no accuracy gain beyond controls. Two apparent targets were label or phonology artifacts.

- **[Weight-Space Programming for Audio Models: LLMs Can Directly Edit Audio Model Weights and Compress Them](https://aksy1999.github.io/blog/weight-space-programming-for-audio-models/)**  
  Ishiki Labs Research · *GitHub* · 2026-11-19 · `💻 code / results`  
  [[Post](https://aksy1999.github.io/blog/weight-space-programming-for-audio-models/)] [[Code](https://github.com/ishikilabsinc/audiowsp)] ![GitHub stars](https://img.shields.io/github/stars/ishikilabsinc/audiowsp?style=social)  
  Open-source code and blogpost for editing audio model weights in one forward pass and zero backward passes: augmentation-subspace nulling, closed-form readout weights, and compression of a deepfake detector from 318M to 86.8M parameters and Wav2Vec2-Large ASR from 315M to 142M.

</details>

## 🧪 Other Curated Lists

*Curated collections and reading lists on weight-space programming.*

<details>
<summary><b>2 entries</b></summary>

- **[Weight-Space Programming: Papers, Code, Models and Guides](https://github.com/weightspaceprogramming/reading-list)**  
  weightspaceprogramming · *GitHub* · 2026-11-23 · `💻 code / results`  
  [[Code](https://github.com/weightspaceprogramming/reading-list)] [[Project](https://weightspaceprogramming.tech/)] ![GitHub stars](https://img.shields.io/github/stars/weightspaceprogramming/reading-list?style=social)  
  Annotated collection of 34 resources on representing and constructing programs in neural-network weights: formal compilation, trained weight generators, LLM reasoning over weights, replications and criticism, with a guide site, BibTeX and JSON.

- **[Awesome Weight-Space Programming](https://github.com/Boom5426/Awesome-Weight-Space-Programming)**  
  Boom5426 · *GitHub* · 2026-11-22 · `💻 code / results`  
  [[Code](https://github.com/Boom5426/Awesome-Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/Boom5426/Awesome-Weight-Space-Programming?style=social)  
  Curated collection of weight-space programming and weight-centric research covering weight understanding, generation, editing, merging, transfer and continual learning, with a searchable catalog, an interactive research landscape and an evidence matrix.

</details>

## 📊 Benchmarks and Evaluations

*Controlled tests of whether weight access helps.*

<details>
<summary><b>13 entries</b></summary>

- **[Comprehensive Weight-Space Programming Leaderboard (MinAtar Experiment 5)](https://github.com/opopile/comprehensive-weight-space-programming-leaderboard)**  
  opopile · *GitHub* · 2026-11-21 · `💻 code / results`  
  [[Code](https://github.com/opopile/comprehensive-weight-space-programming-leaderboard)] ![GitHub stars](https://img.shields.io/github/stars/opopile/comprehensive-weight-space-programming-leaderboard?style=social)  
  Consolidates 41 publicly reported WSP MinAtar Experiment 5 evaluations from 22 sources and recomputes them under the Writing Weights Index and weight-space-bench PPO-500M Median formulas. Adds local Gemini 4 Neon (xhigh) runs (WWI 53.9532) and a Seaquest one-sentence prompt-intervention ablation reported at +29.66%.

- **[Weight-Space Programming](https://github.com/Abelo9996/weight-space-programming)**  
  Abelo9996 · *GitHub* · 2026-11-19 · `💻 code / results`  
  [[Code](https://github.com/Abelo9996/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/Abelo9996/weight-space-programming?style=social)  
  Research package testing whether a language-model editor repairs equivalent policy checkpoints, with weights rearranged without changing function, as well as search baselines using the same edit primitives. Includes CNN accuracy readers, a layer-statistics baseline, checked PyTorch transforms for ReLU and tanh networks, and an offline pilot on three CPU tasks.

- **[Training Vision Models for LLM-Driven Weight-Space Programming](https://arxiv.org/abs/2611.26408)**  
  Timo Ropinski, Sebastian Kranz · *Preprint* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26408)] [[Project](https://viscom.uni-ulm.de/wsp)]  
  Benchmark of LLM-driven weight-space programming on vision models: five LLMs edit convolutional networks and vision transformers on relabeling and error-correction tasks (Waterbirds, CIFAR-100, PACS, Entity-30), over 2,600 edit processes. Proposes Edit-Ready Training, which rehearses closed-form edits and raises edit success where standard networks are hard to edit.

- **[Lohitha0607/wsp-env](https://github.com/Lohitha0607/wsp-env)**  
  Lohitha0607 · *GitHub* · 2026-11-18 · `💻 code / results`  
  [[Code](https://github.com/Lohitha0607/wsp-env)] ![GitHub stars](https://img.shields.io/github/stars/Lohitha0607/wsp-env?style=social)  
  RL environments where an LLM doctor repairs a damaged network by editing weights without retraining: a 2,410-parameter digit MLP and Qwen3-0.6B with scaled down_proj layers. Reports exam-split