<div align="center">

# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Language models that read, edit and write the weights of other neural networks directly, without gradient descent.**

[![Last commit](https://img.shields.io/github/last-commit/SajjadPSavoji/awesome-weight-space-programming?color=green)](https://github.com/SajjadPSavoji/awesome-weight-space-programming/commits/main)
![Entries](https://img.shields.io/badge/entries-596-blue)
![Updated](https://img.shields.io/badge/updated-daily-orange)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

*Weight-space programming* was named in the MIT CSAIL report [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (2026-11-02). A general LLM is given another network's weights, sometimes with code and a budget of forward passes, and changes the numbers to explain, repair or build behavior. This list tracks the papers, code, benchmarks and critiques that follow, grouped by the kind of network being programmed. The [Foundations](#-foundations-weight-programming-before-wsp) section traces the eighty years of earlier work, from McCulloch and Pitts (1943) to 2025, that read, edited or wrote weights under other names. It is rebuilt from [`data/entries.json`](data/entries.json).

## 🔥 Recently Added

- **2026-11-13** · [jazzpher/qwen35-ramble-edit](https://github.com/jazzpher/qwen35-ramble-edit) (Analyses and Critiques)
- **2026-11-12** · [Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](https://github.com/JensLehmann/weight-space-programming-games) (Games)
- **2026-11-12** · [wsp-qwen-tools: weight edits for tool use in Qwen3.5-0.8B](https://github.com/mrtpk/wsp-qwen-tools) (Repairing behavior)
- **2026-11-12** · [wsp-yolo-eel: weight-space programming on a YOLO26n eel detector](https://github.com/mrtpk/wsp-yolo-eel) (Other Domains)
- **2026-11-12** · [sudorian/weight-space-implants](https://github.com/sudorian/weight-space-implants) (Writing networks from scratch)
- **2026-11-12** · [Weight Whisperer](https://github.com/Prayas-Agrawal/weight-whisperer) (Repairing behavior)
- **2026-11-12** · [Weight-space programming on EuroSAT](https://github.com/waliddev23/weight_space_programming_for_remote_sensing_a_small_case_study) (Other Domains)
- **2026-11-12** · [suayptalha/wsr](https://github.com/suayptalha/wsr) (Tools, Harnesses and Agent Skills)
- **2026-11-12** · [Weight-Space Programming research pack](https://github.com/vimuttilabs/weight-space-research) (Analyses and Critiques)
- **2026-11-11** · [ianbruton/weight-space-programming-followup](https://github.com/ianbruton/weight-space-programming-followup) (Analyses and Critiques)
- **2026-11-11** · [waliddev23/weight_space_programming_for_remote_sensing_a_small_case](https://github.com/waliddev23/weight_space_programming_for_remote_sensing_a_small_case) (Other Domains)
- **2026-11-11** · [Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210) (Repairing behavior)

## 🧭 Milestones

| Date | Milestone | Who | Work |
|:--|:--|:--|:--|
| 2026-11-02 | Term coined | MIT CSAIL | [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/) |
| 2026-11-04 | First robot policies | Lingxiao Guo, Angchen Xie | [Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424) |
| 2026-11-05 | First Claude edit of a robot policy | Shanghai Innovation Institute, SJTU, HKU | [Opus 5.5 makes π0.5 move faster and smoother by editing its weights](https://cuzyoung.github.io/robotics-weight-editing/en/) |

## Contents

- [🌟 The Original Report](#-the-original-report) (1)
- [💬 Language Models](#-language-models) (26)
  - [Repairing behavior](#repairing-behavior) (18)
  - [Reading and predicting from weights](#reading-and-predicting-from-weights) (2)
  - [Writing networks from scratch](#writing-networks-from-scratch) (6)
- [🦾 Robotics and Control](#-robotics-and-control) (14)
  - [Vision-language-action models](#vision-language-action-models) (6)
  - [RL control policies](#rl-control-policies) (8)
- [🧩 Other Domains](#-other-domains) (24)
  - [Classical NLP models](#classical-nlp-models) (1)
- [🎮 Games](#-games) (7)
- [🧪 Quantum Circuits](#-quantum-circuits) (2)
- [📊 Benchmarks and Evaluations](#-benchmarks-and-evaluations) (4)
- [🛠️ Tools, Harnesses and Agent Skills](#-tools-harnesses-and-agent-skills) (15)
- [🔍 Analyses and Critiques](#-analyses-and-critiques) (20)
- [📜 Foundations: Weight Programming Before WSP](#-foundations-weight-programming-before-wsp) (188)
  - [Hand-set and compiled weights](#hand-set-and-compiled-weights) (16)
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
- [📖 Surveys and Reviews](#-surveys-and-reviews) (295)
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
- [Legend](#legend)
- [How This List Is Maintained](#how-this-list-is-maintained)
- [Related Lists](#related-lists)
- [Contributing](#contributing)
- [Citation](#citation)

## 🌟 The Original Report

*Where the term comes from.*

- **[Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/)**  
  MIT CSAIL · *Blog report* · 2026-11-02 · `💻 code / results`  
  [[Post](https://rikiyat.github.io/blog/weight-space-programming/)] [[Thread](https://x.com/rikiyatakehi/status/2117313742891327994)] [[Code](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs?style=social)  
  GPT-6 Astra names what networks were trained on from their weights alone, repairs a stuck Kinetix car policy (0% to 100%, 3.5% of weights, one reply, no tools), writes MinAtar and 9x9 Go networks from zero, and lifts Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1% by removing a loop direction (0.016% of weights). Edits removed a blocker; they did not add a missing ability (Gemma 3 270M: no gain).

## 💬 Language Models

*Reading, repairing and writing the weights of language models.*

### Repairing behavior

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

### Reading and predicting from weights

- **[Can GPT-6 Astra read and write GPT-2's weights?](https://github.com/AlexBodner/wsp-scaling)**  
  Alex Bodner · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/AlexBodner/wsp-scaling)] ![GitHub stars](https://img.shields.io/github/stars/AlexBodner/wsp-scaling?style=social)  
  Asks GPT-6 Astra to find induction heads in scrambled GPT-2 small (124M) weights. With Python and no hint it picked all five induction heads in both runs (10 of 10 picks); with no tools, 0 of 10. Silencing the five heads cuts repeat accuracy from 98.6% to 28.9%. One model, few runs, no size sweep.

- **[Weight-space programming autoresearch](https://github.com/csinva/weight-space-programming-autoresearch)**  
  csinva · *GitHub* · 2026-11 · `💻 code / results`  
  [[Code](https://github.com/csinva/weight-space-programming-autoresearch)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch?style=social)  
  Claude, running as a coding agent, hand-writes transformer weights: 959 programs, and all 10 algorithmic tasks reach 100% within three attempts. A second test is mostly negative: Claude Opus 5.5 reading Qwen3.5-0.8B weights predicts the effects of 420 edits only slightly better than without the numbers (+0.06 correlation).

### Writing networks from scratch

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

## 🦾 Robotics and Control

*Weight edits on robot policies, VLAs, world action models and controllers.*

### Vision-language-action models

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

### RL control policies

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

- **[Policy Surgery](https://github.com/latentpaths/policy-surgery)**  
  latentpaths · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/latentpaths/policy-surgery)] [[Project](https://www.latentpaths.com/projects/policy-surgery)] ![GitHub stars](https://img.shields.io/github/stars/latentpaths/policy-surgery?style=social)  
  GPT-OSS-120B edits a 4,996-parameter LunarLander PPO actor after its dynamics change. Reversed thrusters: 0 to 226 of 256 held-out episodes. Crosswind and reduced thrust gain 3 to 6 points, and only one of those intervals excludes zero. Separate selection, approval and test seeds, with every failure kept.

## 🧩 Other Domains

*Classifiers, small decision networks and anything else.*

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

### Classical NLP models

- **[AryaGPT2022/weight-space-programming](https://github.com/AryaGPT2022/weight-space-programming)**  
  AryaGPT2022 · *GitHub* · 2026-11-09 · `💻 code / results`  
  [[Code](https://github.com/AryaGPT2022/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AryaGPT2022/weight-space-programming?style=social)  
  Applies weight-space programming to the BERT cross-encoder ms-marco-MiniLM-L-6-v2 used as a RAG reranker. Claude Opus 5.5 in Claude Code reads the weights and runs the network for at most 25 forward passes. It writes edits such as pruning, layer drop and direction projection, with no gradients. Evaluated on MS MARCO and BEIR with an audit script and data-free baselines.

## 🎮 Games

*Weight programming of game-playing networks and board-game policies.*

- **[Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](https://github.com/JensLehmann/weight-space-programming-games)**  
  JensLehmann · *GitHub* · 2026-11-12 · `💻 code / results`  
  [[Code](https://github.com/JensLehmann/weight-space-programming-games)] ![GitHub stars](https://img.shields.io/github/stars/JensLehmann/weight-space-programming-games?style=social)  
  Language-model writers read a game's mechanics as source code and write all weights of a fixed 57,289-parameter recurrent convolutional actor, a free-architecture network, or a Python player. Players are scored on held-out levels, renderings and perturbed starts of 20 private game families and the 25 public ARC-AGI-3 games. Code and result data released.

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

## 🧪 Quantum Circuits

*LLMs writing the parameters of variational quantum circuits directly.*

- **[Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](https://github.com/DebarshiKunduPSU/Quantum-Weight-Space-Programming)**  
  The Pennsylvania State University · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Code](https://github.com/DebarshiKunduPSU/Quantum-Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/DebarshiKunduPSU/Quantum-Weight-Space-Programming?style=social)  
  GPT-6 Astra writes the angles of parameterized quantum circuits directly, with no optimizer or feedback, for VQE, QAOA and quantum machine learning. VQE is within 0.007 of the optimizer on the normalized energy scale on all 11 problem–ansatz pairs. QAOA depth-1 angles are optimal on all six graphs. A warm-started optimizer reaches its best value after a median of 1 evaluation.

- **[Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](https://arxiv.org/abs/2611.11537)**  
  Debarshi Kundu, Swaroop Ghosh, Vasant G Honavar · *Preprint* · 2026-11-08 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.11537)]  
  A frontier LLM writes circuit angles for digit classification, VQE and MaxCut QAOA across 139 requests, compared with random weights and classical optimization. It reaches 95–100% of the energy spectrum on every VQE problem and 93–96% accuracy on digits 3 vs 8 with 12–18 weights; accuracy drops to chance above 30 fixed weights.

## 📊 Benchmarks and Evaluations

*Controlled tests of whether weight access helps.*

- **[IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection](https://arxiv.org/abs/2611.08647)**  
  Chris von Csefalvay, Pranav Doma, Achyuthan Unni Krishnan, Tamás Földi · *Preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.08647)]  
  Benchmark of a large editor model modifying the weights of a smaller target model (typically Gemma 3 4B IT) for ten text-editing objectives. Editors get four weight read/write tools and a fixed rollout budget. A validator applies each patch and compares it with the unmodified target. A few models lead far ahead; structured response was never solved.

- **[Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers](https://arxiv.org/abs/2611.05798)**  
  Sungguk Cha, Mintae Kim, Youngsub Han, Byoung-Ki Jeon, Sangyeob Lee · *Preprint* · 2026-11-04 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.05798)]  
  Tests whether readers recognize what shallow ReLU neural fields encode from their weights (480 shape fields, 1,000 MNIST fields), using hidden-neuron permutations and positive rescalings that leave the function unchanged. Compares statistics, set and language-model readers, with 1,920 scored reasoning-model sessions, and separates accuracy, agreement across transformed copies and disagreement on fresh identical prompts.

- **[GPT-AGI/Weight-Space-Programing](https://github.com/GPT-AGI/Weight-Space-Programing)**  
  GPT-AGI · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/GPT-AGI/Weight-Space-Programing)] ![GitHub stars](https://img.shields.io/github/stars/GPT-AGI/Weight-Space-Programing?style=social)  
  WSP-Bench plants a known defect in Qwen3.5-0.8B and scores an LLM's repair against ground truth, on hidden prompts with a collateral-change penalty. Model and Agent tracks, public traces, no-LLM baselines. A review of the post's logs reads its headline gain as finish rate 7% to 65% with finished-answer accuracy 93% to 71%.

- **[WSPBench](https://github.com/alexcarterhq/wspbench)**  
  alexcarterhq · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/alexcarterhq/wspbench)] [[Project](https://wspbench.com)] ![GitHub stars](https://img.shields.io/github/stars/alexcarterhq/wspbench?style=social)  
  Does weight access help an agent diagnose and repair a model? GPT-6.1 Sol repaired 30/32 faults with behavior probes plus weights, against 14/32 with probes alone and 5/32 for a scripted solver at the same probe budget. All three kept 8 clean controls intact.

## 🛠️ Tools, Harnesses and Agent Skills

*Libraries and agent skills for reading and editing weights.*

- **[suayptalha/wsr](https://github.com/suayptalha/wsr)**  
  suayptalha · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/suayptalha/wsr)] ![GitHub stars](https://img.shields.io/github/stars/suayptalha/wsr?style=social)  
  Toolkit for weight-space reading and programming. 'wsr read' has a sandboxed agent predict from the weights alone how an edit changes behaviors. 'wsr write' has an agent write an edit without training. 'wsr program' returns a checkpoint of edits that pass held-out and guard suites. Works with open or API agents. Evaluation harness of 'Weight-Space Reading' (Kocabay, 2026).

- **[Ahmedn1/wsplab](https://github.com/Ahmedn1/wsplab)**  
  Ahmedn1 · *GitHub* · 2026-11-09 · `💻 code / results`  
  [[Code](https://github.com/Ahmedn1/wsplab)] ![GitHub stars](https://img.shields.io/github/stars/Ahmedn1/wsplab?style=social)  
  Python library that runs weight-space programming sessions: an LLM editor gets a sandboxed kernel and a forward-pass budget, edits are scored on hidden evaluation with paired statistics and a same-size random-edit control, and saved as patches that rebuild the edited model from the public base. Works on language models and other PyTorch networks.

- **[fus3r/wspserve](https://github.com/fus3r/wspserve)**  
  fus3r · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Code](https://github.com/fus3r/wspserve)] ![GitHub stars](https://img.shields.io/github/stars/fus3r/wspserve?style=social)  
  Forward-pass server for weight-space programming sessions, plus measurements of the released Sparks of WSP Experiment 8 logs. All 88 edits are channel scalings or rank-one projections. A single session keeps a dedicated GPU 51 to 78% busy. The server applies each edit as a per-row delta in one resident model.

- **[IyadhKhalfallah/weight-space-programming](https://github.com/IyadhKhalfallah/weight-space-programming)**  
  IyadhKhalfallah · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/IyadhKhalfallah/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/IyadhKhalfallah/weight-space-programming?style=social)  
  Experiments editing and writing models without gradient descent, plus a wsl CLI that applies reversible weight patches with per-slice regression checks. A hand-written XGBoost model reached AUC 0.809 on rain forecasting with zero labels (0.839 when trained on 2.5 years). On a 0.8B LLM, the author's edit did not reproduce the published effect.

- **[ZeroTang05/WSP-toolkit](https://github.com/ZeroTang05/WSP-toolkit)**  
  ZeroTang05 · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/ZeroTang05/WSP-toolkit)] ![GitHub stars](https://img.shields.io/github/stars/ZeroTang05/WSP-toolkit?style=social)  
  Toolkit to read, edit and evaluate open-weight language model weights: safetensors WeightStore, activation patching, a ProgrammingSession workspace for a model as programmer, TIES merging and SparseGPT reconstruction. On the 1,319-question GSM8K test set, Qwen3-0.6B went from 485 correct (36.77%) to 600 (45.49%) after a scaled TIES merge of three trained updates.

- **[Weight-Space Programming (wsp-kit)](https://github.com/AuremHQ/weight-space-programming)**  
  Aurem · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/AuremHQ/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AuremHQ/weight-space-programming?style=social)  
  Tool that tries to fix small open-weight models by editing weights directly, with an eval gate deciding whether an edit ships. Reports its own CPU runs on Qwen3-0.6B and GPT2-124M: in 60-item list-looping tests no edit passed the gate, so 0 weights shipped. Only the smoke-test pipeline passed (failing score 64.14 → 75.43).

- **[wsp: LLM as an optimiser - weight space programming](https://github.com/desmondzee/wsp)**  
  desmondzee · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/desmondzee/wsp)] ![GitHub stars](https://img.shields.io/github/stars/desmondzee/wsp?style=social)  
  Autoresearch-style harness where an agent reads and edits network weights with a metered budget of forward passes and no optimiser. Tasks are pluggable. Reported: IFEval on Qwen2.5-0.5B-Instruct held-out 0.351 to 0.406; one network written from zero weights for chess and 9x9 Go, held-out win rate 0.244 to 0.980.

- **[weightspace](https://github.com/leofmarciano/weightspace)**  
  Leo Marciano · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/leofmarciano/weightspace)] ![GitHub stars](https://img.shields.io/github/stars/leofmarciano/weightspace?style=social)  
  Apache-2.0 Python library: read, fix, write and improve any torch.nn.Module with an LLM, using budgeted probes, tracked edits and sparse patches. Its own rerun of the Qwen experiment did not beat the original edit.

- **[weight-space-programming-skill](https://github.com/di37/weight-space-programming-skill)**  
  di37 · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/di37/weight-space-programming-skill)] ![GitHub stars](https://img.shields.io/github/stars/di37/weight-space-programming-skill?style=social)  
  Claude Code skill for improving a small open LLM by editing its weights directly, with no training.

- **[weights-lab](https://github.com/oumi-ai/weights-lab)**  
  Oumi · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/oumi-ai/weights-lab)] ![GitHub stars](https://img.shields.io/github/stars/oumi-ai/weights-lab?style=social)  
  Agent skill for editing LLM weights.

- **[pi-weight-space-programming](https://github.com/felipepenha/pi-weight-space-programming)**  
  Felipe Penha · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/felipepenha/pi-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/felipepenha/pi-weight-space-programming?style=social)  
  Extension for the Pi coding agent with skills for reading and editing weights.

- **[OpenWiSH: Open Weight-Space Harness](https://github.com/Alexander-Aghili/OpenWiSH)**  
  Alexander Aghili · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Alexander-Aghili/OpenWiSH)] ![GitHub stars](https://img.shields.io/github/stars/Alexander-Aghili/OpenWiSH?style=social)  
  An agent-agnostic harness (claude -p, Codex or the Anthropic API) where agents inspect and edit weights through a Rust edit gate. Already runs Kinetix and MinAtar tasks.

- **[Praneeth16/dspy-weightspace](https://github.com/Praneeth16/dspy-weightspace)**  
  Praneeth16 · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Praneeth16/dspy-weightspace)] ![GitHub stars](https://img.shields.io/github/stars/Praneeth16/dspy-weightspace?style=social)  
  A DSPy optimizer in which a frontier model reads a small model's weights, writes patch scripts, and GEPA keeps the best. On Qwen3.5-0.8B the best run scores 60.6% on MATH-500 against 53.3% for the published edit; the worst run scores 32%. A difference-in-means direction scores 29.8%.

- **[weight-surgery](https://github.com/lorenzofamiglini/weight-surgery)**  
  Lorenzo Famiglini · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/lorenzofamiglini/weight-surgery)] ![GitHub stars](https://img.shields.io/github/stars/lorenzofamiglini/weight-surgery?style=social)  
  Open agent skill that reads weights first, keeps a fixed forward-pass budget and proves fixes on held-out data. On a BERT NER model, a fitted control beat the hand edit (+0.109 vs +0.032 F1).

- **[weight-space-programming (agent skill)](https://github.com/xero00000/weight-space-programming)**  
  xero00000 · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/xero00000/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/xero00000/weight-space-programming?style=social)  
  Agent skill for reasoning-driven weight inspection, targeted edits and small-network construction.

## 🔍 Analyses and Critiques

*Audits, replications of claims and critical takes.*

- **[ianbruton/weight-space-programming-followup](https://github.com/ianbruton/weight-space-programming-followup)**  
  ianbruton · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/ianbruton/weight-space-programming-followup)] ![GitHub stars](https://img.shields.io/github/stars/ianbruton/weight-space-programming-followup?style=social)  
  Reproduces the MIT CSAIL weight-space edit of Qwen3.5-0.8B and compares base and edited models under three sampling settings, including perplexity, tool use and an agent task. Applies the same recipe to a 4B citation edit with a random-direction control, and to a 27B tool-reflex edit, reported as a negative result.

- **[Weight-Space Programming research pack](https://github.com/vimuttilabs/weight-space-research)**  
  vimuttilabs · *GitHub* · 2026-11-11 · `💻 code / results`  
  [[Code](https://github.com/vimuttilabs/weight-space-research)] ![GitHub stars](https://img.shields.io/github/stars/vimuttilabs/weight-space-research?style=social)  
  Sourced notes on weight-space programming, compiled from a Claude research session and re-checked against primary sources. Chapters cover the MIT edit of Qwen3.5-0.8B, an independent toy-task replication, loop detection, decision models, low-bit models, speech models and behavior transplant. Facts are tagged by source status and kept apart from analysis.

- **[jazzpher/qwen35-ramble-edit](https://github.com/jazzpher/qwen35-ramble-edit)**  
  jazzpher · *GitHub* · 2026-11-10 · `💻 code / results`  
  [[Code](https://github.com/jazzpher/qwen35-ramble-edit)] ![GitHub stars](https://img.shields.io/github/stars/jazzpher/qwen35-ramble-edit?style=social)  
  Rebuilds Astra's rank-1 down_proj edit of Qwen3.5-0.8B hash-for-hash. Finds its own rambling direction and edits 64 columns in layers 15 and 19 without training. On 12 GSM8K test problems, accuracy is 25% for both unedited and edited, verbatim loops fall from 42% to 17%, and Astra's edit scores 8%.

- **[Weight-space programming with Claude Opus 5.5](https://cenrax.github.io/weight-space-programming-claude/)**  
  Cenrax · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Post](https://cenrax.github.io/weight-space-programming-claude/)] [[Code](https://github.com/Cenrax/weight-space-programming-claude)] ![GitHub stars](https://img.shields.io/github/stars/Cenrax/weight-space-programming-claude?style=social)  
  Independent replication of Sparks of Weight-Space Programming with Claude Opus 5.5 instead of GPT-6 Astra, on Gymnasium, ALE and PettingZoo environments. Probes: reading Atari policies (3/4 games read), fixing failing policies (MountainCar 0% to 100%, LunarLander 0% to 85.6%), writing policies zero-shot, writing a 9x9 Go network, and identifying a sycophantic Gemma 3 270M finetune (6/6).

- **[Gradient-Free Weight Editing Reduces Overthinking in Qwen3.8-27B](https://github.com/conceptcountry/weight-space-programming)**  
  conceptcountry · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Code](https://github.com/conceptcountry/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/conceptcountry/weight-space-programming?style=social)  
  Norm-matched controlled replication of weight-space programming. A nine-layer gradient-free edit to Qwen3.8-27B cuts thinking tokens by up to 54% while accuracy rises. An equal-norm random edit on the same layers does nothing. Statistics are generated from released artifacts; bootstrap seed check flags the IFBench control interval as borderline.

- **[aner-lang/aner-weight-space-programming](https://github.com/aner-lang/aner-weight-space-programming)**  
  aner-lang · *GitHub* · 2026-11-08 · `💻 code / results`  
  [[Code](https://github.com/aner-lang/aner-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/aner-lang/aner-weight-space-programming?style=social)  
  Replays the stored weight changes of MIT's Qwen3.5-0.8B repair through Aner. Both edited BF16 tensor hashes match the manifest, 130,188 entries changed, and rollback restores the original checkpoint hash. Local inference pilots showed no accuracy gain: base 1/8 correct and edited 1/8 on eight prompts with a 2,048-token cap.

- **[Can a language model repair a network's weights by reading them?](https://github.com/hamley241/wsp-harness-public)**  
  hamley241 · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/hamley241/wsp-harness-public)] ![GitHub stars](https://img.shields.io/github/stars/hamley241/wsp-harness-public?style=social)  
  Code, frozen decision rules and run records for an extended abstract on language-model weight repair. In an unconstrained pilot, two editor models reached the task ceiling by writing a replacement network. Under a bounded numeric-edit budget, neither repaired the trained network beyond the threshold, while projected gradient descent did on every seed. One task, one architecture, five seeds.

- **[Weight-Space Programming: an independent reproduction](https://github.com/goddoe/weight-space-programming)**  
  goddoe · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/goddoe/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/goddoe/weight-space-programming?style=social)  
  Reruns two experiments from the original report with the same prompts and gpt-6-astra, tools off. Breakout: a fresh answer scores 416.8 ± 6.9 over 1,000 games (original weights re-scored 502.9 ± 7.7). Car: 1 of 4 independent answers works, 0 to 1,024 of 1,024 test games.

- **[The Astra weight edit on Qwen3.5-0.8B: a GSM8K rerun with transformers and a 16K budget](https://github.com/clavis-systems/astra-gsm8k-transformers-16k)**  
  Emanuele Rizzan · *GitHub* · 2026-11-07 · `💻 code / results`  
  [[Code](https://github.com/clavis-systems/astra-gsm8k-transformers-16k)] ![GitHub stars](https://img.shields.io/github/stars/clavis-systems/astra-gsm8k-transformers-16k?style=social)  
  Reruns the Astra edit of Qwen3.5-0.8B (130,188 weights) on 100 GSM8K problems with transformers and a 16,384-token limit. Thinking on: 7 to 50 correct; thinking off: 47 to 43. Verdict rule written before generation; independent recheck included.

- **[Does Claude have it too? Replicating 'Sparks of Weight-Space Programming'](https://github.com/dhaneshnm/wsp-replication)**  
  dhaneshnm · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/dhaneshnm/wsp-replication)] ![GitHub stars](https://img.shields.io/github/stars/dhaneshnm/wsp-replication?style=social)  
  Replication of the MinAtar write-from-scratch experiment with Claude Opus 5.5, using the same prompts and scorer. In each game one of three one-shot replies reached 87%, 97% and 86% of GPT-6 Astra's score; median replies reached 51%, 14% and 62%. Claude beats PPO at 100M steps in every game.

- **[MaceTenth/weight-space-programming-replication](https://github.com/MaceTenth/weight-space-programming-replication)**  
  MaceTenth · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/MaceTenth/weight-space-programming-replication)] ![GitHub stars](https://img.shields.io/github/stars/MaceTenth/weight-space-programming-replication?style=social)  
  Replicates the post with Claude models, then extends it. Claude Opus changed 7,684 of GPT-2's 124M weights to insert a new fact, which held on 6 of 7 unseen wordings. A web-agent repair raised 37 to 46 of 48 tasks, while an 8-minute LoRA fine-tune reached 48 of 48.

- **[Rethinking Weight-Space Programming](https://github.com/ZhangYiqun018/rethinking-weight-space-programming)**  
  Yiqun Zhang · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/ZhangYiqun018/rethinking-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/ZhangYiqun018/rethinking-weight-space-programming?style=social)  
  Re-runs the report's experiments with baselines and controls. Tuned PPO reaches 99.2–114.4 on Seaquest vs Astra's 53.1. Unedited Qwen3.5-0.8B with thinking off scores 44.2% on MATH-500. A difference-of-means direction with no LLM reaches 41.9%. Without simulator source in the prompt, Seaquest median falls to 0.8.

- **[Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070)**  
  Nazmus Sakib Ahmed · *Preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.08070)]  
  Tests Claude Opus 5.5 reading raw weights, given as plain text without tools, of ~125,000-parameter CNNs trained on five image datasets. Finds accurate local arithmetic but reliance on dataset priors: with CIFAR-10 labels permuted, every class pair the model interprets is wrong. Exploratory, mostly single runs; provides an auditing protocol.

- **[Weight-Space Programming Replication](https://github.com/MatinKhajavi/Weight-Space-Programming)**  
  Matin Khajavi · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/MatinKhajavi/Weight-Space-Programming)] ![GitHub stars](https://img.shields.io/github/stars/MatinKhajavi/Weight-Space-Programming?style=social)  
  Replicates all eight experiments of Sparks of Weight-Space Programming with Claude Opus 5.5 and Claude Fable 5.1, using a rebuilt harness checked against Astra's released results. Experiment 1: Opus 4/4, Fable 3/4. Breakout mean score 483.6 (Opus), 38.4 (Fable), 517.4 (Astra).

- **[Weight-space horizon: re-evaluating the released MinAtar networks](https://github.com/hamley241/weight-space-horizon)**  
  hamley241 · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/hamley241/weight-space-horizon)] ![GitHub stars](https://img.shields.io/github/stars/hamley241/weight-space-horizon?style=social)  
  A pre-registered re-evaluation finds 51.6% of the released Breakout episodes still running at the 10K-step cap; a 30K cap adds 405.3 reward. Episode caps are a way to misread WSP scores.

- **[The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading)**  
  Matthew Honnibal · *Blog* · 2026-11-03 · `💬 post only`  
  [[Post](https://honnibal.dev/blog/astra-read-write-misleading)]  
  Separates reading weights directly from repairing a model with code and practice feedback: raw-weight reading without tools appears only on the smallest networks, and the language-model results used Python and forward passes.

- **[MIT team says GPT-6 Astra can improve other AI models by editing their weights. Critics say its biggest result relied on standard ML engineering.](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/)**  
  R&D World · *News* · 2026-11-03 · `💬 post only`  
  [[Post](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/)]  
  News coverage of the claims and the methodological pushback.

- **[Sparks of Weight-Space Programming — Complete Reproduction & Interactive Guide (EN / KO)](https://github.com/statsleelab/weight_space_programming)**  
  statsleelab · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/statsleelab/weight_space_programming)] [[Project](https://statsleelab.github.io/weight_space_programming/)] ![GitHub stars](https://img.shields.io/github/stars/statsleelab/weight_space_programming?style=social)  
  Reproduction of all 8 experiments of the MIT report from the released weights, prompts and logs, with standalone NumPy/SciPy verification scripts. Reports max tensor difference 0.0 and a full run of about 3.5 seconds on CPU. Includes a bilingual (English/Korean) interactive web report and a separate Drosophila connectome weight-edit page.

- **[Flecart/weight-programming](https://flecart.github.io/posts/2026-11-03-i-tried-to-break-weight-programming/)**  
  Xuanqiang Angelo Huang · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Post](https://flecart.github.io/posts/2026-11-03-i-tried-to-break-weight-programming/)] [[Code](https://github.com/Flecart/weight-programming)] ![GitHub stars](https://img.shields.io/github/stars/Flecart/weight-programming?style=social)  
  Replication and stress tests of 'Sparks of Weight Space Programming'. Hand-written MinAtar networks match published scores; the Kinetix car fix succeeds in 1,024/1,024 episodes. A Breakout network scores 517 versus 534 for a Python script with the same algorithm. Tests obfuscation (156/156 correct) and Claude Opus 5.5 writing networks.

- **[The Mathematics of Weight-Space Programming](https://doi.org/10.5281/zenodo.23933590)**  
  Miquel Noguer Alonso · *Zenodo preprint* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://doi.org/10.5281/zenodo.23933590)]  
  Gives conditions under which a selective edit to a transformer's final feed-forward module is possible, minimum-cost edits under explicit preservation constraints, and certificates of infeasibility. The editors are explicit algorithms, not LLMs; on GPT-2 CounterFact edits, interval constraints improved neighbor retention by about 20 points.

## 📜 Foundations: Weight Programming Before WSP

*Eighty years of work that read, edited or wrote network weights under other names, oldest first, in fourteen lineages; plus recent related work that does not use a language model as the editor.*

### Hand-set and compiled weights

- **[A logical calculus of the ideas immanent in nervous activity](https://doi.org/10.1007/BF02478259)**  
  U. Illinois College of Medicine / U. Chicago · *Bulletin of Mathematical Biophysics* · 1943 · `📄 peer-reviewed` · 18.6k citations (OA)  
  [[Paper](https://doi.org/10.1007/BF02478259)]  
  Proves that nets of threshold units with hand-chosen excitatory and inhibitory connections can realise any finite logical expression: the first networks whose weights are programmed by hand.

- **[Representation of events in nerve nets and finite automata](https://doi.org/10.1515/9781400882618-002)**  
  S.C. Kleene · *Automata Studies, Princeton UP* · 1956 · `📄 peer-reviewed` · 2k citations (S2)  
  [[Paper](https://doi.org/10.1515/9781400882618-002)]  
  Proves that nets of threshold units are equivalent to finite automata and introduces regular expressions, the theoretical root of compiling automata into networks.

- **[Non-Holographic Associative Memory](https://doi.org/10.1038/222960a0)**  
  D. J. Willshaw, O. P. Buneman, H. C. Longuet-Higgins · *Nature* · 1969 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://doi.org/10.1038/222960a0)]  
  Introduces a clipped outer-product associative memory whose connection matrix is written in one shot from the patterns to be stored, following Hebb's correlation rule.

- **[Correlation Matrix Memories](https://doi.org/10.1109/TC.1972.5008975)**  
  Teuvo Kohonen · *IEEE Transactions on Computers* · 1972 · `📄 peer-reviewed` · 1k citations (S2)  
  [[Paper](https://doi.org/10.1109/TC.1972.5008975)]  
  Presents a correlation-matrix memory whose matrix is written in one shot as a sum of outer products of the patterns to be stored.

- **[Neural networks and physical systems with emergent collective computational abilities](https://doi.org/10.1073/pnas.79.8.2554)**  
  Caltech / Bell Laboratories · *PNAS* · 1982 · `📄 peer-reviewed` · 20.5k citations (S2)  
  [[Paper](https://doi.org/10.1073/pnas.79.8.2554)]  
  Writes the weights of a symmetric recurrent network in one pass with the outer-product rule T_ij = Σ_s (2V_i^s−1)(2V_j^s−1) over the stored patterns, with no training.

- **["Neural" computation of decisions in optimization problems](https://doi.org/10.1007/BF00339943)**  
  Caltech / AT&T Bell Laboratories · *Biological Cybernetics* · 1985 · `📄 peer-reviewed` · 3.4k citations (S2)  
  [[Paper](https://doi.org/10.1007/BF00339943)]  
  Derives a continuous Hopfield network's weights analytically from an energy function that encodes the Travelling Salesman Problem, with no learning. Moves from storing memories to compiling a task into the network.

- **[Collective computational properties of neural networks: New learning mechanisms](https://doi.org/10.1103/PhysRevA.34.4217)**  
  ESPCI Paris · *Physical Review A* · 1986 · `📄 peer-reviewed` · 325 citations (S2)  
  [[Paper](https://doi.org/10.1103/PhysRevA.34.4217)]  
  Gives a closed-form pseudo-inverse rule, W = X X⁺, that computes the weights of an associative network directly from the patterns to be stored.

- **[On the computational power of neural nets](https://doi.org/10.1006/jcss.1995.1013)**  
  Rutgers University · *J. Computer and System Sciences* · 1995 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://doi.org/10.1006/jcss.1995.1013)]  
  Proves, by explicit weight construction, that a finite recurrent network with rational weights simulates any Turing machine. Appeared at COLT 1992 and in the Journal of Computer and System Sciences in 1995.

- **[A neural compiler](https://doi.org/10.1016/0304-3975(94)00200-3)**  
  LIP, ENS Lyon; CEA Grenoble · *Theoretical Computer Science* · 1995 · `📄 peer-reviewed` · 45 citations (S2)  
  [[Paper](https://doi.org/10.1016/0304-3975(94)00200-3)]  
  Presents a neural compiler that translates programs in a high-level, Pascal-like language into networks whose weights and topology are fully determined by the program.

- **[Constructing deterministic finite-state automata in recurrent neural networks](https://doi.org/10.1145/235809.235811)**  
  NEC Research Institute / RPI · *Journal of the ACM* · 1996 · `📄 peer-reviewed` · 210 citations (S2)  
  [[Paper](https://doi.org/10.1145/235809.235811)]  
  Gives a provably stable way to program a second-order recurrent network so that it implements any given deterministic finite-state automaton.

- **[Thinking Like Transformers](https://arxiv.org/abs/2106.06981)**  
  Technion, Bar-Ilan University / AI2 · *ICML 2021* · 2021-06 · `📄 peer-reviewed` · 222 citations (S2)  
  [[Paper](https://arxiv.org/abs/2106.06981)]  
  Proposes RASP, a programming language whose primitives map transformer-encoder attention and feed-forward computation. Provides RASP programs for histograms, sorting and Dyck-languages, relates task difficulty to required layers and heads, and shows a transformer can be trained to mimic a RASP solution.

- **[What learning algorithm is in-context learning? Investigations with linear models](https://arxiv.org/abs/2211.15661)**  
  Ekin Akyürek et al. · *ICLR 2023* · 2022-11 · `📄 peer-reviewed` · 833 citations (S2)  
  [[Paper](https://arxiv.org/abs/2211.15661)]  
  Proves by construction that transformers can implement gradient descent and closed-form ridge regression for linear models. Shows trained in-context learners match gradient descent, ridge and least-squares predictors, with preliminary evidence of shared algorithmic features in late layers.

- **[Transformers Learn In-Context by Gradient Descent](https://arxiv.org/abs/2212.07677)**  
  ETH Zürich / Google Research · *ICML 2023* · 2022-12 · `📄 peer-reviewed` · 932 citations (S2)  
  [[Paper](https://arxiv.org/abs/2212.07677)]  
  Gives a simple weight construction showing a single linear self-attention layer matches gradient descent on a regression loss. Shows empirically that self-attention-only Transformers trained on regression tasks match gradient-descent models or the construction's weights.

- **[Looped Transformers as Programmable Computers](https://arxiv.org/abs/2301.13196)**  
  UW–Madison and others · *ICML 2023* · 2023-01 · `📄 peer-reviewed` · 319 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.13196)] [[Code](https://github.com/yuedajiong/looped-transformer)] ![GitHub stars](https://img.shields.io/github/stars/yuedajiong/looped-transformer?style=social)  
  Programs transformers with specific weights and places them in a loop, with the input sequence acting as a punchcard. Emulates a small instruction-set computer, mapping iterative algorithms to programs run by a looped, 13-layer transformer.

- **[Tracr: Compiled Transformers as a Laboratory for Interpretability](https://arxiv.org/abs/2301.05062)**  
  David Lindner et al. · *NeurIPS 2023* · 2023-01-12 · `📄 peer-reviewed` · 125 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.05062)] [[Code](https://github.com/google-deepmind/tracr)] ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/tracr?style=social)  
  Compiles RASP programs into transformer weights with known structure.

- **[Learning Transformer Programs](https://arxiv.org/abs/2306.01128)**  
  Dan Friedman, Alexander Wettig, Danqi Chen · *NeurIPS 2023* · 2023-06 · `📄 peer-reviewed` · 60 citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.01128)]  
  Trains modified Transformers that are then converted into discrete, human-readable programs, building on RASP. Learns programs for in-context learning, sorting, Dyck languages, named entity recognition and text classification, performing on par with standard Transformers of comparable size.

### Rule insertion and extraction

- **[Connectionist expert systems](https://doi.org/10.1145/42372.42377)**  
  Northeastern University · *Communications of the ACM* · 1988 · `📄 peer-reviewed` · 715 citations (S2)  
  [[Paper](https://doi.org/10.1145/42372.42377)]  
  Builds an expert system on a connectionist network (MACIE) and explains its conclusions by inspecting which weighted inputs determined each unit's output.

- **[Medical diagnostic expert system based on PDP model](https://doi.org/10.1109/ICNN.1988.23855)**  
  NTT · *Proc. IEEE ICNN'88* · 1988 · `📄 peer-reviewed` · 250 citations (S2)  
  [[Paper](https://doi.org/10.1109/ICNN.1988.23855)]  
  Extracts if-then rules from a backpropagation network trained for medical diagnosis, at NTT. Presents a diagnostic expert system built on a parallel distributed processing model, with rules read from the trained network.

- **[A distributed connectionist production system](https://doi.org/10.1207/s15516709cog1203_4)**  
  Carnegie Mellon University · *Cognitive Science* · 1988 · `📄 peer-reviewed` · 330 citations (S2)  
  [[Paper](https://doi.org/10.1207/s15516709cog1203_4)]  
  Implements rule matching and variable binding in a distributed connectionist production system, a network built to carry out symbolic rules.

- **[Interpreting neural-network connection weights](https://doi.org/10.5555/129449.129452)**  
  G.D. Garson · *AI Expert* · 1991 · `📄 peer-reviewed` · 1.5k citations (OA)  
  [[Paper](https://doi.org/10.5555/129449.129452)]  
  Proposes a weight-product measure of each input's importance, computed from the connection weights alone with no data.

- **[Rule induction through integrated symbolic and subsymbolic processing](https://proceedings.neurips.cc/paper_files/paper/1991/hash/cf67355a3333e6e143439161adc2d82e-Abstract.html)**  
  U. Colorado Boulder · *NIPS 1991* · 1992 · `📄 peer-reviewed` · 65 citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1991/hash/cf67355a3333e6e143439161adc2d82e-Abstract.html)]  
  Describes RuleNet, which alternates learning with projecting the network's weights onto explicit rules and re-inserting those rules into the network.

- **[Extraction, insertion and refinement of symbolic rules in dynamically driven recurrent neural networks](https://doi.org/10.1080/09540099308915703)**  
  NEC Research Institute / RPI; OpenAlex lists U. Maryland and RPI · *Connection Science* · 1993 · `📄 peer-reviewed` · 110 citations (S2)  
  [[Paper](https://doi.org/10.1080/09540099308915703)]  
  Inserts known DFA transitions into second-order recurrent networks by programming a subset of weights to large values (±H), trains the network, then extracts refined automata by clustering hidden states, all in one paper.

- **[Extracting refined rules from knowledge-based neural networks](https://doi.org/10.1007/BF00993103)**  
  U. Wisconsin–Madison · *Machine Learning* · 1993 · `📄 peer-reviewed` · 760 citations (OA)  
  [[Paper](https://doi.org/10.1007/BF00993103)]  
  Extracts rules from trained knowledge-based networks by clustering weights and rewriting each unit as an 'M of these N antecedents' rule. Together with KBANN, it closes the knowledge-to-weights-to-knowledge loop.

- **[Knowledge-based artificial neural networks](https://doi.org/10.1016/0004-3702(94)90105-8)**  
  U. Wisconsin–Madison · *Artificial Intelligence* · 1994 · `📄 peer-reviewed` · 900 citations (S2)  
  [[Paper](https://doi.org/10.1016/0004-3702(94)90105-8)]  
  Turns each propositional Horn clause into a unit whose weights (±ω) and bias are set analytically, adds low-weight links, then refines the network by backpropagation: a compiler from knowledge to weights.

- **[Rule generation from neural networks](https://doi.org/10.1109/21.299696)**  
  University of Florida · *IEEE Trans. Systems, Man, and Cybernetics* · 1994 · `📄 peer-reviewed` · 410 citations (S2)  
  [[Paper](https://doi.org/10.1109/21.299696)]  
  Introduces the KT algorithm, which generates rules from a trained neural network by searching subsets of each unit's incoming weights.

- **[Survey and critique of techniques for extracting rules from trained artificial neural networks](https://doi.org/10.1016/0950-7051(96)81920-4)**  
  Queensland University of Technology · *Knowledge-Based Systems* · 1995 · `📄 peer-reviewed` · 1.4k citations (S2)  
  [[Paper](https://doi.org/10.1016/0950-7051(96)81920-4)]  
  Surveys techniques for extracting rules from trained networks and fixes the decompositional versus pedagogical taxonomy: read individual weights and units, or treat the network as a black box.

- **[Extracting tree-structured representations of trained networks](https://proceedings.neurips.cc/paper_files/paper/1995/hash/45f31d16b1058d586fc3be7207b58053-Abstract.html)**  
  U. Wisconsin–Madison · *NIPS 1995* · 1996 · `📄 peer-reviewed` · 434 citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1995/hash/45f31d16b1058d586fc3be7207b58053-Abstract.html)]  
  Extracts tree-structured representations (TREPAN) from trained networks by querying the network as an oracle rather than reading its weights.

- **[The truth will come to light: directions and challenges in extracting the knowledge embedded within trained artificial neural networks](https://doi.org/10.1109/72.728352)**  
  QUT / ANU · *IEEE Trans. Neural Networks* · 1998 · `📄 peer-reviewed` · 470 citations (S2)  
  [[Paper](https://doi.org/10.1109/72.728352)]  
  Reviews directions and open challenges in extracting the knowledge embedded in trained neural networks, following the decompositional and pedagogical split.

### Weight surgery and pruning

- **[Skeletonization: A technique for trimming the fat from a network via relevance assessment](https://proceedings.neurips.cc/paper_files/paper/1988/hash/07e1cd7dca89a1678042477183b7ac3f-Abstract.html)**  
  U. Colorado Boulder · *NIPS 1988* · 1989 · `📄 peer-reviewed` · 540 citations (OA)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1988/hash/07e1cd7dca89a1678042477183b7ac3f-Abstract.html)]  
  Introduces skeletonization, which assesses the relevance of units in a trained network and deletes the least relevant ones. The aim is a minimal network that is more interpretable.

- **[Optimal brain damage](https://proceedings.neurips.cc/paper_files/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html)**  
  AT&T Bell Laboratories · *NIPS 1989* · 1990 · `📄 peer-reviewed` · 5.6k citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html)]  
  Ranks weights by a saliency computed from a diagonal approximation of the Hessian and deletes the lowest-ranked ones. Bell Labs authors present it as a way to prune trained networks.

- **[A simple procedure for pruning back-propagation trained neural networks](https://doi.org/10.1109/72.80236)**  
  IBM Haifa Research · *IEEE Trans. Neural Networks* · 1990 · `📄 peer-reviewed` · 750 citations (S2)  
  [[Paper](https://doi.org/10.1109/72.80236)]  
  Proposes a simple procedure for pruning back-propagation trained networks by estimating the sensitivity of the error to each weight and removing low-sensitivity weights.

- **[Creating artificial neural networks that generalize](https://doi.org/10.1016/0893-6080(91)90033-2)**  
  Defence Science and Technology Organisation · *Neural Networks* · 1991 · `📄 peer-reviewed` · 690 citations (S2)  
  [[Paper](https://doi.org/10.1016/0893-6080(91)90033-2)]  
  Studies how to build networks that generalize, pruning hidden units whose outputs are constant or duplicate other units.

- **[Second order derivatives for network pruning: Optimal Brain Surgeon](https://proceedings.neurips.cc/paper_files/paper/1992/hash/303ed4c69846ab36c2904d3ba8573050-Abstract.html)**  
  Stanford University / Ricoh California Research Center · *NIPS 1992* · 1993 · `📄 peer-reviewed` · 2.2k citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1992/hash/303ed4c69846ab36c2904d3ba8573050-Abstract.html)]  
  Uses the full inverse Hessian to choose which weight to delete and to compute a closed-form update for all remaining weights. The update is commonly written δw = −(w_q/[H⁻¹]_qq) H⁻¹ e_q.

- **[Pruning algorithms — a survey](https://doi.org/10.1109/72.248452)**  
  University of Washington · *IEEE Trans. Neural Networks* · 1993 · `📄 peer-reviewed` · 1.9k citations (S2)  
  [[Paper](https://doi.org/10.1109/72.248452)]  
  Surveys pruning algorithms for neural networks, from sensitivity-based weight removal to penalty terms, consolidating the field as of 1993.

- **[Net2Net: Accelerating Learning via Knowledge Transfer](https://arxiv.org/abs/1511.05641)**  
  Google · *ICLR 2016* · 2015-11 · `📄 peer-reviewed` · 825 citations (S2)  
  [[Paper](https://arxiv.org/abs/1511.05641)]  
  Transfers the information in a trained network into a wider or deeper network through function-preserving transformations, so the new network starts with the same function. Reports a new state-of-the-art ImageNet accuracy after adding depth to Inception modules.

- **[Network Morphism](https://arxiv.org/abs/1603.01670)**  
  Microsoft Research Asia + SUNY Buffalo · *ICML 2016* · 2016-03 · `📄 peer-reviewed` · 207 citations (S2)  
  [[Paper](https://arxiv.org/abs/1603.01670)]  
  Studies how to morph a trained network into a new one that completely preserves its function. Introduces network morphism equations and algorithms for changes of depth, width, kernel size and subnet, plus parametric activations for non-linearities.

- **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)**  
  Jonathan Frankle, Michael Carbin · *ICLR 2019* · 2018-03 · `📄 peer-reviewed` · 4.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/1803.03635)]  
  Proposes that dense, randomly initialized networks contain subnetworks that reach comparable test accuracy when trained in isolation. Finds winning tickets under 10-20% of the size of fully-connected and convolutional networks on MNIST and CIFAR10.

- **[Are Sixteen Heads Really Better than One?](https://arxiv.org/abs/1905.10650)**  
  CMU + Facebook AI Research · *NeurIPS 2019* · 2019-05 · `📄 peer-reviewed` · 1.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/1905.10650)] [[Code](https://github.com/pmichel31415/are-16-heads-really-better-than-1)] ![GitHub stars](https://img.shields.io/github/stars/pmichel31415/are-16-heads-really-better-than-1?style=social)  
  Observes that a large percentage of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Also examines greedy pruning algorithms.

- **[Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning](https://arxiv.org/abs/2208.11580)**  
  IST Austria · *NeurIPS 2022* · 2022-08 · `📄 peer-reviewed` · 461 citations (S2)  
  [[Paper](https://arxiv.org/abs/2208.11580)] [[Code](https://github.com/ist-daslab/obc)] ![GitHub stars](https://img.shields.io/github/stars/ist-daslab/obc?style=social)  
  Introduces a framework covering weight pruning and quantization in the one-shot, post-training setting. It is built on an exact and efficient realization of the Optimal Brain Surgeon framework, extended to quantization.

- **[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774)**  
  IST Austria · *ICML 2023* · 2023-01 · `📄 peer-reviewed` · 1.7k citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.00774)] [[Code](https://github.com/ist-daslab/sparsegpt)] ![GitHub stars](https://img.shields.io/github/stars/ist-daslab/sparsegpt?style=social)  
  Prunes GPT-family models in one shot without retraining. Runs on OPT-175B and BLOOM-176B in under 4.5 hours, reaching 60% unstructured sparsity with negligible perplexity increase, ignoring more than 100 billion weights.

- **[A Simple and Effective Pruning Approach for Large Language Models (Wanda)](https://arxiv.org/abs/2306.11695)**  
  CMU, Meta AI, Bosch Center for AI · *ICLR 2024* · 2023-06 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.11695)] [[Code](https://github.com/locuslab/wanda)] ![GitHub stars](https://img.shields.io/github/stars/locuslab/wanda?style=social)  
  Prunes pretrained LLMs by weight magnitude multiplied by input activation on a per-output basis. Requires no retraining or weight update, and is evaluated on LLaMA and LLaMA-2 against magnitude pruning.

### Fast weights and self-modifying networks

- **[The correlation theory of brain function](https://doi.org/10.1007/978-1-461