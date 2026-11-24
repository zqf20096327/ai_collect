<div align="center">

<p>
  <img src="assets/cover.png" width="88%" alt="Towards AI that improves AI — the plan, execute, feedback, repair loop">
</p>

<h1>🚀 Awesome AI4AI</h1>

<h3>🔄 Updated weekly — until humanity achieves AI4AI.</h3>

<p><strong>Follow the journey: <a href="https://github.com/KaiWU5/Awesome-AI4AI">Star ⭐</a> · <a href="https://github.com/KaiWU5/Awesome-AI4AI/subscription">Watch 👀 for weekly updates</a> · <a href="#weekly-news">Read this week's picks →</a></strong></p>

<p><strong><em>AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement</em></strong><br>
<sub>Definitions, Reliable Horizons, and Open Problems · 23 authors · 7 institutions</sub></p>

<p>
  Top AI-for-AI papers, releases, and blogs — curated every week. <strong>Stay tuned 🔥</strong>
</p>

<p><strong>Living catalog: 1885 papers</strong> · 836 benchmarks · 1217 harness studies · 437 model studies<br><sub>Collections overlap. The original survey covers 223 papers.</sub></p>

<p>
  <a href="assets/AI4AI-Survey.pdf"><img src="https://img.shields.io/badge/-Paper_(nice_layout)-B31B1B.svg?style=flat-square" alt="Paper, nice layout"></a>
  <a href="https://www.preprints.org/manuscript/202608.2108/v1"><img src="https://img.shields.io/badge/-Paper_on_Preprints.org-8B5CF6.svg?style=flat-square" alt="Paper on Preprints.org"></a>
  <a href="https://kaiwu5.github.io/Awesome-AI4AI/"><img src="https://img.shields.io/badge/-Project_Site-D76712.svg?style=flat-square" alt="Project Site"></a>
  <a href="https://github.com/simple-agent-lab/RSIHub"><img src="https://img.shields.io/badge/-RSIHub_Harness-24292F.svg?style=flat-square" alt="RSIHub Harness"></a>
  <a href="https://simpleagentlab.com/ai4ai/"><img src="https://img.shields.io/badge/-Blog-0A7EA4.svg?style=flat-square" alt="Blog"></a>
  <a href="https://doi.org/10.20944/preprints202608.2108.v1"><img src="https://img.shields.io/badge/DOI-10.20944%2Fpreprints202608.2108.v1-0A7EA4.svg?style=flat-square" alt="DOI"></a>
</p>

</div>

<br>

## Why This Repo

<table>
<tr>
<td width="33%" align="center">
  <strong>🔄 Refreshed rankings</strong><br>
  <sub>Citations, GitHub stars, and rankings refresh with maintainer updates.</sub>
</td>
<td width="33%" align="center">
  <strong>🗞️ Weekly update</strong><br>
  <sub>New papers added to the catalog, plus source-verified papers and releases selected every week.</sub>
</td>
<td width="33%" align="center">
  <strong>🧭 Survey-grounded map</strong><br>
  <sub>From long-horizon agents to recursive self-improvement.</sub>
</td>
</tr>
</table>

<p align="center">
  <strong>Star ⭐ to save the map · Watch 👀 for weekly updates · Share 🔁 with your lab</strong>
</p>

## What's New

- 📚 **2026-11-23 — 423 papers added.** Expanded Benchmarks, Harness Design, and Model Design with verified new and previously missed papers; rebuilt the full catalog and both ranking families.
- 🚀 **2026-11-16 — Latest weekly edition published.** Read the source-verified news digest below.
- 🤝 **2026-10-26 — Community contributions integrated.** Added ReCreate, Meta-Team, Agon, EvoRepair, and Harness Engineering for Language Agents to Harness Design, and PerspectiveGap to Benchmarks. Related Lists now links to three complementary community resources.
- 📄 **2026-08-30 — [Companion survey now online.](https://www.preprints.org/manuscript/202608.2108/v1)** Read *AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems*.
- 🔄 **Maintainer refresh.** Citations, GitHub stars, and recent-paper/yearly rankings are rebuilt from the catalog.

<details open markdown="1">
<summary><b>🗂️ Explore the full collection</b></summary>

- [📅 Weekly News · Top 10](#weekly-news)
- [📈 Live Rankings](#-live-rankings)
  - [Top Ranking Papers by Average Monthly Citations](#top-ranking-papers-by-average-monthly-citations)
  - [🏆 Most-Cited Papers by Year](#-most-cited-papers-by-year)
- [🧪 Benchmarks](#-benchmarks)
- [🛠️ Harness Design](#-harness-design)
- [🧠 Model Design](#-model-design)
- [📚 How We Curate](#-how-we-curate)
- [🔗 Related Lists](#-related-lists)
- [📄 Citation](#-citation)
- [🤝 Contributing](#-contributing)

</details>

<br>

<a id="monthly-news"></a>
<a id="weekly-news"></a>

## 📅 Weekly News · Top 10

> **Updated 2026-11-16** · Weekly news picks, refreshed every Monday alongside citation rankings.
>
> **How we select:** The top stories from the trailing 30 days, scored on publisher authority, discussion volume, whether a concrete verifiable result is reported, whether it changes what agent builders do now, whether an artifact was released, and expected durability. Only primary sources are cited, and performance claims remain attributed to their publishers.

| Date · Type | News | Why it matters |
|:--|:--|:--|
| 2026‑11‑16<br><sub>Model release</sub> | [**Qwen4-Max: Your new teammate has arrived**](https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max)<br><sub>Alibaba / Qwen</sub> | Alibaba releases its 2.4T-parameter multimodal flagship with a 1M-token context window. On its proprietary Work360 benchmark, Alibaba reports 35% fewer tokens and about 60% lower cost per task than Qwen3.8-Max at High effort. |
| 2026‑11‑13<br><sub>Paper</sub> | [**ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL**](https://arxiv.org/abs/2611.18533)<br><sub>He et al. · arXiv</sub> | The authors learn and evolve executable compression and steering programs alongside agentic RL, validating candidates by execution and trajectory replay. On CodeSearch, ALFWorld and BIRD SQL with 1.5B–8B models, they report better held-out performance than fixed harnesses in most settings. |
| 2026‑11‑13<br><sub>Paper</sub> | [**AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning**](https://arxiv.org/abs/2611.17790)<br><sub>Tang et al. · arXiv</sub> | The authors automate ongoing RL supervision with training-state perceptors, diagnostic proposers and an orchestrator that applies hot updates or resumes checkpoints. Experiments on Qwen3 and LongCat-Flash-Lite outperform static recipes and a general agent; unattended supervision is distinguished from discovering fundamental new methods. |
| 2026‑11‑12<br><sub>Paper</sub> | [**Singularity-Bench: Can Agents Build Agents?**](https://arxiv.org/abs/2611.16591)<br><sub>Zhou et al. · arXiv</sub> | The authors benchmark six AI-development tasks from pre-training through cluster orchestration against human-built systems on identical hardware. Across 11 agents, their best configuration scores a 1.25 Singularity-Index; Breakwater blocks all reward-hacking attacks tested, without establishing that unrestricted recursive improvement has been achieved. |
| 2026‑11‑12<br><sub>Paper</sub> | [**Discovering Effective Agent Memory Designs through Program Evolution**](https://arxiv.org/abs/2611.17068)<br><sub>Ding et al. · arXiv</sub> | The authors release MAPE, which evolves whole memory programs through diagnosis and proposal. On LoCoMo and LongMemEval they report up to 12 percentage points higher accuracy at 35% of baseline serving cost, and show that transplanting an evolved composition module improves five existing memory systems. |
| 2026‑11‑09<br><sub>Model release</sub> | [**Introducing Claude Fable 5.2 and Claude Mythos 5.2**](https://www.anthropic.com/claude-fable-and-mythos-5-2)<br><sub>Anthropic</sub> | Anthropic reports 49.1% on FrontierCode 2.0 and 74.6% on Terminal-Bench-Science for Fable 5.2, plus a 30-hour formalization of Fermat’s Last Theorem. Fable is broadly available with cyber/bio safeguards; Mythos, the same underlying model with different safeguards, requires verified access. |
| 2026‑11‑05<br><sub>Model release</sub> | [**GPT-6 Cyber: Advancing the frontier of aligned cybersecurity agents**](https://openai.com/index/introducing-gpt-6-cyber/)<br><sub>OpenAI</sub> | OpenAI introduces a cyber-specialized GPT-6 Astra variant for approved Daybreak Red customers in the API and Codex. It reports 48.5% on ExploitGym versus 32.1% for GPT-5.6 Cyber, and 99.93% scope adherence without its deployment prompt. |
| 2026‑11‑04<br><sub>Paper</sub> | [**EnzymeRSI: A dual-loop recursive self-improvement system for enzyme design**](https://arxiv.org/abs/2611.06321)<br><sub>Genoria AI Team et al. · arXiv</sub> | The authors evolve both harness assets and enzyme-design algorithms. They report 10 of 32 non-pre-specified luciferase candidates with at least twice wild-type activity, plus prospective A3A and polymerase tests; physical-loop results are distinguished from development-set optimization. |
| 2026‑10‑29<br><sub>Open-weight release</sub> | [**Mistral Large 4 (Le Chonk) is now open weight**](https://mistral.ai/news/mistral-large-4-oss/)<br><sub>Mistral AI</sub> | Mistral releases the improved 1T-parameter multimodal flagship weights under its Ecosystem Open-Weight license. It reports 41% on Terminal-Bench 4.0 and 48% on the Coding Agent Index, with 47% fewer tokens than GLM-5.3 on the latter. |
| 2026‑10‑28<br><sub>Model release</sub> | [**Gemini 4 Carbon: our next frontier model**](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)<br><sub>Google DeepMind</sub> | Google reports 88.2% on SEC-bench Pro for its long-horizon engineering and cybersecurity model. After the October 28 preview, the official November 10 update confirms access for paying developers and enterprises via the API and a rollout to Google AI Ultra users; this item retains the original announcement date. |

> **Want next week's news?** Watch the repository. Citation counts, rankings, and the weekly news picks are published with maintainer updates. [Browse past editions →](highlights/README.md)

## 📈 Live Rankings

> Last complete citation snapshot: **2026-10-17**, using Semantic Scholar and OpenAlex. Rankings are discovery aids, not quality scores; audit evidence remains independent of popularity. Last complete GitHub stars snapshot: **2026-11-08**. For papers indexed as multiple versions, retain the largest title-verified count reported by the configured sources. All yearly rankings use first public appearance year; a later venue year never moves a paper into a newer cohort.

> **Latest metric check: 2026-11-23.** Title-verified citations for 1821/1901 catalog records; 17 records retain prior verified counts and 63 records remain without a verified index count. GitHub stars refreshed for 491 records across 486 repositories. 3 configured GitHub repositories could not be refreshed; previous star counts are retained. Complete snapshot dates advance only when every relevant record is verified.

### Top Ranking Papers by Average Monthly Citations

| Paper | Venue | Date | Citations | Avg. cites/month | Code |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**Kimi K3: Open Frontier Intelligence**](https://arxiv.org/abs/2607.24653) | arXiv | <nobr>2026-07</nobr> | 531 | **177.0** | [GitHub](https://github.com/MoonshotAI/Kimi-K3) · ★ 9,114 |
| [**AlphaEvolve: A coding agent for scientific and algorithmic discovery**](https://arxiv.org/abs/2506.13131) | arXiv | <nobr>2025-06</nobr> | 1656 | **103.5** | — |
| [**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**](https://arxiv.org/abs/2601.11868) | arXiv | <nobr>2026-01</nobr> | 777 | **86.3** | [GitHub](https://github.com/harbor-framework/terminal-bench-1) · ★ 2,624 |
| [**Towards End-to-End Automation of AI Research**](https://doi.org/10.1038/s41586-026-10265-5) | Nature 2026 | <nobr>2026-03</nobr> | 577 | **82.4** | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) · ★ 7,547 |
| [**Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**](https://doi.org/10.3233/faia251160) | European Conference on Artificial Intelligence (ECAI) | <nobr>2025-04</nobr> | 1347 | **74.8** | [GitHub](https://github.com/mem0ai/mem0) · ★ 69,374 |
| [**Meta-Harness: End-to-End Optimization of Model Harnesses**](https://arxiv.org/abs/2603.28052) | arXiv | <nobr>2026-03</nobr> | 450 | **64.3** | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) · ★ 1,255 |
| [**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models**](https://arxiv.org/abs/2510.04618) | arXiv | <nobr>2025-10</nobr> | 576 | **48.0** | [GitHub](https://github.com/ace-agent/ace) · ★ 1,471 |
| [**RRSI: Regularized Recursive Self-Improvement of Agent Harnesses**](https://arxiv.org/abs/2609.24972) | arXiv | <nobr>2026-09</nobr> | 47 | **47.0** | [GitHub](https://github.com/google-research/rrsi) · ★ 1,814 |
| [**Memory in the Age of AI Agents**](https://arxiv.org/abs/2512.13564) | arXiv preprint arXiv:2512.13564 | <nobr>2025-12</nobr> | 439 | **43.9** | — |
| [**DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks**](https://arxiv.org/abs/2607.07946) | arXiv preprint arXiv:2607.07946 | <nobr>2026-07</nobr> | 121 | **40.3** | [GitHub](https://github.com/datacurve-ai/deep-swe) · ★ 1,925 |

### 🏆 Most-Cited Papers by Year

<details open markdown="1">
<summary><b>Top 12 of 2026</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**](https://arxiv.org/abs/2601.11868)<br><sub>arXiv</sub> | <nobr>2026-01</nobr> | 777 | [GitHub](https://github.com/harbor-framework/terminal-bench-1) · ★ 2,624 |
| [**Towards End-to-End Automation of AI Research**](https://doi.org/10.1038/s41586-026-10265-5)<br><sub>Nature 2026</sub> | <nobr>2026-03</nobr> | 577 | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) · ★ 7,547 |
| [**Kimi K3: Open Frontier Intelligence**](https://arxiv.org/abs/2607.24653)<br><sub>arXiv</sub> | <nobr>2026-07</nobr> | 531 | [GitHub](https://github.com/MoonshotAI/Kimi-K3) · ★ 9,114 |
| [**Meta-Harness: End-to-End Optimization of Model Harnesses**](https://arxiv.org/abs/2603.28052)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 450 | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) · ★ 1,255 |
| [**Self-Harness: Harnesses That Improve Themselves**](https://arxiv.org/abs/2606.09498)<br><sub>arXiv</sub> | <nobr>2026-06</nobr> | 148 | [GitHub](https://github.com/qzzqzzb/Self-Harness) · ★ 148 |
| [**Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering**](https://arxiv.org/abs/2604.08224)<br><sub>arXiv preprint arXiv:2604.08224</sub> | <nobr>2026-04</nobr> | 126 | — |
| [**DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks**](https://arxiv.org/abs/2607.07946)<br><sub>arXiv preprint arXiv:2607.07946</sub> | <nobr>2026-07</nobr> | 121 | [GitHub](https://github.com/datacurve-ai/deep-swe) · ★ 1,925 |
| [**Code as Agent Harness**](https://arxiv.org/abs/2605.18747)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 107 | [GitHub](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) · ★ 784 |
| [**PostTrainBench: Can LLM Agents Automate LLM Post-Training?**](https://arxiv.org/abs/2603.08640)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 105 | [GitHub](https://github.com/aisa-group/PostTrainBench) · ★ 627 |
| [**SkillOS: Learning Skill Curation for Self-Evolving Agents**](https://arxiv.org/abs/2605.06614)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 93 | — |
| [**Natural-Language Agent Harnesses**](https://arxiv.org/abs/2603.25723)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 88 | — |
| [**ProgramBench: Can Language Models Rebuild Programs From Scratch?**](https://arxiv.org/abs/2605.03546)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 85 | [GitHub](https://github.com/facebookresearch/ProgramBench) · ★ 986 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2025</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**AlphaEvolve: A coding agent for scientific and algorithmic discovery**](https://arxiv.org/abs/2506.13131)<br><sub>arXiv</sub> | <nobr>2025-06</nobr> | 1656 | — |
| [**A-MEM: Agentic Memory for LLM Agents**](https://arxiv.org/abs/2502.12110)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-02</nobr> | 1457 | [GitHub](https://github.com/WujiangXu/A-mem) · ★ 1,018 |
| [**Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**](https://doi.org/10.3233/faia251160)<br><sub>European Conference on Artificial Intelligence (ECAI)</sub> | <nobr>2025-04</nobr> | 1347 | [GitHub](https://github.com/mem0ai/mem0) · ★ 69,374 |
| [**Why Do Multi-Agent LLM Systems Fail?**](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-03</nobr> | 916 | [GitHub](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · ★ 441 |
| [**Group-in-Group Policy Optimization for LLM Agent Training**](https://arxiv.org/abs/2505.10978)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-05</nobr> | 642 | [GitHub](https://github.com/langfengQ/verl-agent) · ★ 2,457 |
| [**The Berkeley Function Calling Leaderboard (BFCL): From tool use to agentic evaluation of large language models**](https://proceedings.mlr.press/v267/patil25a.html)<br><sub>Proceedings of the 42nd International Conference on Machine Learning</sub> | <nobr>2025</nobr> | 634 | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,085 |
| [**LLMs Get Lost In Multi-Turn Conversation**](https://arxiv.org/abs/2505.06120)<br><sub>International Conference on Learning Representations</sub> | <nobr>2025-05</nobr> | 606 | [GitHub](https://github.com/microsoft/lost_in_conversation) · ★ 311 |
| [**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models**](https://arxiv.org/abs/2510.04618)<br><sub>arXiv</sub> | <nobr>2025-10</nobr> | 576 | [GitHub](https://github.com/ace-agent/ace) · ★ 1,471 |
| [**Darwin Godel Machine: Open-ended evolution of self-improving agents**](https://openreview.net/forum?id=pUpzQZTvGY)<br><sub>arXiv</sub> | <nobr>2025-05</nobr> | 539 | [GitHub](https://github.com/jennyzzt/dgm) · ★ 2,539 |
| [**SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?**](https://arxiv.org/abs/2509.16941)<br><sub>arXiv</sub> | <nobr>2025-09</nobr> | 442 | [GitHub](https://github.com/scaleapi/SWE-bench_Pro-os) · ★ 570 |
| [**Memory in the Age of AI Agents**](https://arxiv.org/abs/2512.13564)<br><sub>arXiv preprint arXiv:2512.13564</sub> | <nobr>2025-12</nobr> | 439 | — |
| [**PaperBench: Evaluating AI's ability to replicate AI research**](https://arxiv.org/abs/2504.01848)<br><sub>arXiv</sub> | <nobr>2025-04</nobr> | 412 | [GitHub](https://github.com/openai/frontier-evals) · ★ 1,347 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2024</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains**](https://arxiv.org/abs/2406.12045)<br><sub>arXiv</sub> | <nobr>2024-06</nobr> | 1844 | [GitHub](https://github.com/sierra-research/tau-bench) · ★ 1,516 |
| [**OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**](https://arxiv.org/abs/2404.07972)<br><sub>NeurIPS 2024</sub> | <nobr>2024-04</nobr> | 1555 | [GitHub](https://github.com/xlang-ai/OSWorld) · ★ 3,277 |
| [**HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models**](https://arxiv.org/abs/2405.14831)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2024-05</nobr> | 1185 | [GitHub](https://github.com/OSU-NLP-Group/HippoRAG) · ★ 4,139 |
| [**VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks**](https://arxiv.org/abs/2401.13649)<br><sub>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</sub> | <nobr>2024-01</nobr> | 926 | [GitHub](https://github.com/web-arena-x/visualwebarena) · ★ 489 |
| [**WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models**](https://arxiv.org/abs/2401.13919)<br><sub>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</sub> | <nobr>2024-01</nobr> | 893 | [GitHub](https://github.com/MinorJerry/WebVoyager) · ★ 1,129 |
| [**Demystifying LLM-Based Software Engineering Agents**](https://doi.org/10.1145/3715754)<br><sub>Proceedings of the ACM on Software Engineering</sub> | <nobr>2024-07</nobr> | 876 | [GitHub](https://github.com/OpenAutoCoder/Agentless) · ★ 2,138 |
| [**Self-rewarding language models**](https://proceedings.mlr.press/v235/yuan24d.html)<br><sub>arXiv</sub> | <nobr>2024-01</nobr> | 819 | — |
| [**MLE-bench: Evaluating machine learning agents on machine learning engineering**](https://arxiv.org/abs/2410.07095)<br><sub>ICLR 2025</sub> | <nobr>2024-10</nobr> | 633 | [GitHub](https://github.com/openai/mle-bench) · ★ 1,803 |
| [**AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents**](https://arxiv.org/abs/2405.14573)<br><sub>International Conference on Learning Representations</sub> | <nobr>2024-05</nobr> | 549 | [GitHub](https://github.com/google-research/android_world) · ★ 1,021 |
| [**AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents**](https://arxiv.org/abs/2407.18901)<br><sub>ACL 2024</sub> | <nobr>2024-07</nobr> | 546 | [GitHub](https://github.com/StonyBrookNLP/appworld) · ★ 557 |
| [**TravelPlanner: A Benchmark for Real-World Planning with Language Agents**](https://arxiv.org/abs/2402.01622)<br><sub>International Conference on Machine Learning</sub> | <nobr>2024-02</nobr> | 544 | [GitHub](https://github.com/OSU-NLP-Group/TravelPlanner) · ★ 574 |
| [**Automated design of agentic systems**](https://arxiv.org/abs/2408.08435)<br><sub>ICLR 2025</sub> | <nobr>2024-08</nobr> | 540 | [GitHub](https://github.com/ShengranHu/ADAS) · ★ 1,670 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2023</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Generative Agents: Interactive Simulacra of Human Behavior**](https://arxiv.org/abs/2304.03442)<br><sub>Proceedings of the 36th annual acm symposium on user interface software and technology</sub> | <nobr>2023-04</nobr> | 8273 | [GitHub](https://github.com/joonspk-research/generative_agents) · ★ 22,405 |
| [**Reflexion: language agents with verbal reinforcement learning**](https://arxiv.org/abs/2303.11366)<br><sub>NeurIPS 2023</sub> | <nobr>2023-03</nobr> | 6890 | [GitHub](https://github.com/noahshinn/reflexion) · ★ 3,439 |
| [**Toolformer: Language Models Can Teach Themselves to Use Tools**](https://arxiv.org/abs/2302.04761)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-02</nobr> | 6837 | — |
| [**Self-Refine: Iterative refinement with self-feedback**](https://arxiv.org/abs/2303.17651)<br><sub>NeurIPS 2023</sub> | <nobr>2023-03</nobr> | 6446 | [GitHub](https://github.com/madaan/self-refine) · ★ 854 |
| [**Tree of Thoughts: Deliberate Problem Solving with Large Language Models**](https://arxiv.org/abs/2305.10601)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-05</nobr> | 5420 | [GitHub](https://github.com/princeton-nlp/tree-of-thought-llm) · ★ 6,087 |
| [**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**](https://arxiv.org/abs/2310.06770)<br><sub>ICLR 2024</sub> | <nobr>2023-10</nobr> | 5058 | [GitHub](https://github.com/SWE-bench/SWE-bench) · ★ 6,234 |
| [**Voyager: An Open-Ended Embodied Agent with Large Language Models**](https://arxiv.org/abs/2305.16291)<br><sub>Transactions on Machine Learning Research</sub> | <nobr>2023-05</nobr> | 2932 | [GitHub](https://github.com/MineDojo/Voyager) · ★ 7,340 |
| [**ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs**](https://arxiv.org/abs/2307.16789)<br><sub>International Conference on Learning Representations</sub> | <nobr>2023-07</nobr> | 2675 | [GitHub](https://github.com/OpenBMB/ToolBench) · ★ 5,774 |
| [**WebArena: A Realistic Web Environment for Building Autonomous Agents**](https://arxiv.org/abs/2307.13854)<br><sub>ICLR 2024</sub> | <nobr>2023-07</nobr> | 2566 | [GitHub](https://github.com/web-arena-x/webarena) · ★ 1,647 |
| [**AgentBench: Evaluating LLMs as Agents**](https://arxiv.org/abs/2308.03688)<br><sub>International Conference on Learning Representations</sub> | <nobr>2023-08</nobr> | 2503 | [GitHub](https://github.com/THUDM/AgentBench) · ★ 3,831 |
| [**MemGPT: Towards LLMs as Operating Systems**](https://arxiv.org/abs/2310.08560)<br><sub>arXiv preprint arXiv:2310.08560</sub> | <nobr>2023-10</nobr> | 1931 | [GitHub](https://github.com/letta-ai/letta) · ★ 25,520 |
| [**Gorilla: Large Language Model Connected with Massive APIs**](https://arxiv.org/abs/2305.15334)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-05</nobr> | 1907 | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,085 |

</details>



## 🧪 Benchmarks

<p align="center">
  <img src="assets/benchmarks.png" width="92%" alt="Figure 3 from the companion survey: What Is AI4AI? A Taxonomy">
</p>

> **836 papers** · Survey-curated collection, newest first. Cross-collection papers may appear in more than one section.

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Benchmarks' Last Exam**](https://arxiv.org/abs/2611.27622)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/ZekkiCat/Benchmarks-Last-Exam) · ★ 17 |
| [**$\gamma$-Scape: An Agent-Centric World for Mobile Embodied Intelligence**](https://arxiv.org/abs/2611.27306)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?**](https://arxiv.org/abs/2611.27116)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/AlibabaResearch/CoEvoBench) · ★ 4 |
| [**Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions**](https://arxiv.org/abs/2611.27046)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**CodeReviewBench: An Automated Benchmark for Evaluating the Software Factory**](https://arxiv.org/abs/2611.26942)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**TEA-Bench-BR: Can Coding Agents Turn a Branching Clinical Specification into Correct Code?**](https://arxiv.org/abs/2611.27895)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks**](https://arxiv.org/abs/2611.27860)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Potential emergence in LLM agents: a statistical physics perspective**](https://arxiv.org/abs/2611.27618)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material**](https://arxiv.org/abs/2611.27139)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/jxtse/ri-bench) · ★ 0 |
| [**Schema-Validated LLM Workflows: A Benchmark Protocol and Comparative Evaluation Across Six Python Implementations**](https://arxiv.org/abs/2611.27106)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/ULDataProfessor/schema-validated-llm-workflows) · ★ 0 |
| [**Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation**](https://arxiv.org/abs/2611.27094)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes**](https://arxiv.org/abs/2611.27090)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering**](https://arxiv.org/abs/2611.27734)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/VinyehShaw/AutoOntologyBench) · ★ 0 |
| [**Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation**](https://arxiv.org/abs/2611.27166)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/NJU-R-L-Group-Embodied-Lab/Mem-X) · ★ 2 |
| [**Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models**](https://arxiv.org/abs/2611.26944)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress**](https://arxiv.org/abs/2611.26910)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments**](https://arxiv.org/abs/2611.26897)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**What Helps Language-Model Agents Review Violent Video? A Controlled Comparison with a Human Evidence Reference**](https://arxiv.org/abs/2611.26776)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/amine0110/evidence-graph-agents) · ★ 0 |
| [**ClosureBench: A Benchmark for Reasoning under Closure Assumptions**](https://arxiv.org/abs/2611.26335)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs**](https://arxiv.org/abs/2611.26248)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ZJUSCL/TwinLab-Bench) · ★ 6 |
| [**The FrontierOR Challenge: Agentic Algorithm Design for Operations Research**](https://arxiv.org/abs/2611.26171)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Agents Play Differently: Localizing Human--Agent Behavioral Divergence with Conditional Distributional Testing**](https://arxiv.org/abs/2611.26012)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations**](https://arxiv.org/abs/2611.26003)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Validation-driven Deployment of LLM Inference Platforms for Agentic Workloads**](https://arxiv.org/abs/2611.25905)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks**](https://arxiv.org/abs/2611.25673)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SiliconGym: A Versatile Reinforcement Learning Environment for Agentic EDA**](https://arxiv.org/abs/2611.25658)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Feedback-Free Self-Evolution Reshapes Agent Skills: A Systematic Study**](https://arxiv.org/abs/2611.25534)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/LitaoGuo/How-Self-Evolution-Reshapes-Skills) · ★ 1 |
| [**When Should a Voice Agent Speak? End-of-Turn Detection in Turkish**](https://arxiv.org/abs/2611.25489)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AppSci-Bench: Can LLMs Build AI Agents and Make Them Better?**](https://arxiv.org/abs/2611.25360)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/sanjari-orb/appsci-bench) · ★ 3 |
| [**Pandora's Toolbox Or Why Agent Safety Cannot Be Verified**](https://arxiv.org/abs/2611.25325)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)**](https://arxiv.org/abs/2611.26553)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://rogue-ai.surge.sh) |
| [**Backtracking Agent Applications Security Incidents**](https://arxiv.org/abs/2611.26525)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation**](https://arxiv.org/abs/2611.26444)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature**](https://arxiv.org/abs/2611.25845)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Harnessing Medical Visual-Language Models with Agentic Evidence Management**](https://arxiv.org/abs/2611.25840)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Characterizing and Detecting Unfaithful Work Reports by Coding Agents**](https://arxiv.org/abs/2611.25760)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development**](https://arxiv.org/abs/2611.25582)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From FIPS to FPGA with LLM Agents: Measuring What Tests and Reviews Miss in Post-Quantum Cryptographic Hardware**](https://arxiv.org/abs/2611.25339)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction**](https://arxiv.org/abs/2611.26875)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**SkillPrivus: Uncovering PRIVacy of USe Harms in Agentic Skills**](https://arxiv.org/abs/2611.26747)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control**](https://arxiv.org/abs/2611.26613)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/cxcscmu/AgentRoboCritic) · ★ 4 |
| [**PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity**](https://arxiv.org/abs/2611.26565)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agentic Scaling of Embodied Tasks in Simulation for Synthetic Data Collection and Policy Evaluation**](https://arxiv.org/abs/2611.26046)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://huggingface.co/datasets/jimmy-zhou/AgenticTask-Kitchen-50) |
| [**MKA: Evaluating Multimodal Knowledge Agents on end-to-end professional tasks**](https://arxiv.org/abs/2611.25228)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DVBench: End-to-End Benchmark for Real-World UVM Design Verification Agents**](https://arxiv.org/abs/2611.25066)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Local AI Agents in Power Electronics Simulation: Deployment, Measurements and Costs**](https://arxiv.org/abs/2611.24880)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Choosing What to Observe: Budget-Paired Counterfactual Audits for Credible Evaluation of Visual Agents**](https://arxiv.org/abs/2611.24867)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchmarking LLM abilities on postdoc-level natural science problems**](https://arxiv.org/abs/2611.24321)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games**](https://arxiv.org/abs/2611.24073)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises**](https://arxiv.org/abs/2611.24039)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop**](https://arxiv.org/abs/2611.23855)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ghadinehme/RoboBuilder) · ★ 1 |
| [**Openhagen Worlds: Calibrated Environments for Measuring and Training Scientific Discovery Agents**](https://arxiv.org/abs/2611.24711)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://eval.openhagen.ai) |
| [**Probing agent overeagerness in realistic settings with continuation audits**](https://arxiv.org/abs/2611.24491)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents**](https://arxiv.org/abs/2611.24362)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents**](https://arxiv.org/abs/2611.24313)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/stevendamianakis/autopi) · ★ 6 |
| [**VideoACE: Benchmarking Agentic Video Understanding through High-Frame-Rate Actions**](https://arxiv.org/abs/2611.24184)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Complete Must an Environment Be to Train a Capable GUI Agent?**](https://arxiv.org/abs/2611.23946)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Safe Personal RSI: Evaluating and Repairing Personal-Agent Updates**](https://arxiv.org/abs/2611.23651)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Teaching VLMs What to Say, Not How to Reason: Rethinking Counterfactual Reasoning in Autonomous Driving**](https://arxiv.org/abs/2611.24376)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/OPhD-hahao/Rethink-CF) · ★ 3 |
| [**Assessing Vision-Language Models for Early Prediction of Unsafe Situations in Robotics**](https://arxiv.org/abs/2611.24146)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ExecGap: Exploiting Command-Execution Gap for Patch Attacks on Vision-Language-Action Models**](https://arxiv.org/abs/2611.23714)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Diagnostic Accuracy and Navigation Behavior of Vision-Language Model Agents Reading Emergency CT and MRI Examinations**](https://arxiv.org/abs/2611.23480)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Where the Tokens Go: Heat, Entropy and Error in Agentic Coding**](https://arxiv.org/abs/2611.23375)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain**](https://arxiv.org/abs/2611.23613)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Idempotency Is Not Recovery: A Fault-Injection Study of Language-Model Agent Tool Actions**](https://arxiv.org/abs/2611.23353)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements**](https://arxiv.org/abs/2611.23068)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://lineshogan.github.io/resolution-hypothesis/) |
| [**Values Shape What Self-Improving Coding Agents Build**](https://arxiv.org/abs/2611.23067)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents**](https://arxiv.org/abs/2611.23045)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing**](https://arxiv.org/abs/2611.22991)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VITAL: A Framework for Validating Agentic AI in Pharmaceutical Drug Development and Clinical Trial Operations**](https://arxiv.org/abs/2611.22973)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Done, But Still Working: Anytime Evaluation of When Coding Agents Should Stop**](https://arxiv.org/abs/2611.22901)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Verifying Agents in Rubric-Graded Environments**](https://arxiv.org/abs/2611.22841)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | — |
| [**CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training**](https://arxiv.org/abs/2611.22777)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Agent Skills Go Stale: Runtime Behavior and Selective Maintenance in Evolving Environments**](https://arxiv.org/abs/2611.22525)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SciWorkBench: A Benchmark for Real Scientific Workflows**](https://arxiv.org/abs/2611.22490)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Reliable Evaluation of AI Agents for Investment Research: A Framework for Performance and Validity Assessment**](https://arxiv.org/abs/2611.22338)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Learning to Edit IFC Building Models: Verifiable Checkers as the Training Signal for Dependency-Aware Editing Agents**](https://arxiv.org/abs/2611.22307)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents**](https://arxiv.org/abs/2611.22245)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Context Has a Price: Adding and Removing Context for LLM Coding Agents under Prefix Caching**](https://arxiv.org/abs/2611.22238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't**](https://arxiv.org/abs/2611.22179)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News**](https://arxiv.org/abs/2611.22177)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Not All Evidence Is Admissible: Evidence Governance for Tool-Augmented Medical Agents**](https://arxiv.org/abs/2611.22169)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ATLAS-Finance: Benchmarking AI Agents in Realistic Banking Environments**](https://arxiv.org/abs/2611.22085)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents**](https://arxiv.org/abs/2611.22033)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models, Skill Access Modes and Memory**](https://arxiv.org/abs/2611.22017)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Higher-Scoring Coding Models Did Not Get More Work Done**](https://arxiv.org/abs/2611.23216)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Inference after coding agents**](https://arxiv.org/abs/2611.23174)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Web Research Agents Interpret User Priorities**](https://arxiv.org/abs/2611.22989)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway**](https://arxiv.org/abs/2611.22971)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Yuxuan2003/SEAM) · ★ 2 |
| [**Stopping Is Not the Limit: Understanding and Eliciting Agent Capability in Long-Horizon Vulnerability Exploitation**](https://arxiv.org/abs/2611.22888)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding**](https://arxiv.org/abs/2611.22790)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agent Trajectories as Evidence for Software Quality Assurance**](https://arxiv.org/abs/2611.22323)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**OfficePrism: Benchmarking Agents on Single-Domain Operations Across Enterprise Business Functions**](https://arxiv.org/abs/2611.22262)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time**](https://arxiv.org/abs/2611.22138)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Passing Checks Do Not Establish Completion: Evidence Interpretation in Coding Agents**](https://arxiv.org/abs/2611.22835)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Where Does Hindsight Enter Clinical Agent Benchmarks? An Audit of Simulators and Case Construction**](https://arxiv.org/abs/2611.22241)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate**](https://arxiv.org/abs/2611.22461)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models**](https://arxiv.org/abs/2611.22453)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Network-Exposed Configuration Attacks on LLM-Controlled Social Robots**](https://arxiv.org/abs/2611.22761)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/akingbolastanley1998-byte/reachy-personality-injection) · ★ 0 |
| [**DiagTrace: An Interactive Benchmark for Clinical Decision Making**](https://arxiv.org/abs/2611.22009)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Eight in Ten LLMs Leak System-Prompt Secrets: Nevan, an Agentic Capture-the-Flag Study**](https://arxiv.org/abs/2611.21956)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**EmbedGym: Letting Coding Agents Develop and Debug Embedded Firmware Without Physical Hardware**](https://arxiv.org/abs/2611.21845)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Coding Agents Write and Transpile Unit Tests**](https://arxiv.org/abs/2611.21797)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Revisiting the Survival of Agent-Attributed Code: How Measurement Choices Decide the Verdict**](https://arxiv.org/abs/2611.21784)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Bookkeeping Is Not Judgement: EJBench, an Engineering Judgement Benchmark Built from a Conjugate Heat Transfer Design Campaign**](https://arxiv.org/abs/2611.21707)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents**](https://arxiv.org/abs/2611.21541)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Btwestyo/sciresearch-eval) · ★ 0 |
| [**Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety**](https://arxiv.org/abs/2611.21520)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses from 0.75B to 4.7B**](https://arxiv.org/abs/2611.21407)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchleaking Is Accelerating: Benchmark contamination has worsened sharply in the past month -- from post-training down to pre-training base models**](https://arxiv.org/abs/2611.21315)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/GAIR-NLP/Benchleaking) · ★ 2 |
| [**CAE-Bench: Benchmarking AI Agents for Reusable CAE Solver Development**](https://arxiv.org/abs/2611.21273)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Language-model agents' beliefs can be manipulated via truthful evidence in open channel**](https://arxiv.org/abs/2611.21235)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Accelerate Bench: Evaluating Agents for Application-Level Program Optimization**](https://arxiv.org/abs/2611.20882)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/AdAstraAbyssoque/accelerate-bench) · ★ 5 |
| [**DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds**](https://arxiv.org/abs/2611.20844)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/DatagridsAI/DetourBench) · ★ 1 |
| [**AgentFaultBench: State-Verified Evaluation of Tool-Fault Recovery**](https://arxiv.org/abs/2611.20711)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VAHBench: A Harness Benchmark for Agentic Long-Video Generation**](https://arxiv.org/abs/2611.20535)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**EVIDENT: Evaluating Evidence Grounding in GUI Agents**](https://arxiv.org/abs/2611.20488)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**FinVerify: A Verification Framework for Financial Agents**](https://arxiv.org/abs/2611.20423)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents**](https://arxiv.org/abs/2611.21577)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Scientific Coding with Large Language Models: Evidence from Finite Element Analysis**](https://arxiv.org/abs/2611.21176)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SWE-WhatIf: Simulating Real Users of Coding Agents from Recorded Session**](https://arxiv.org/abs/2611.21095)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Experience Rot: Experienced Agents Fail Where Novices Succeed**](https://arxiv.org/abs/2611.20922)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Re-Reading Is Not Free: Token Traces and Cache-Aware Energy Estimation for LLM Agents in Software Engineering**](https://arxiv.org/abs/2611.20873)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Instrumenting Failure: Scoring Language Model Agents at Every Decision Node in Imperfect-Information Games**](https://arxiv.org/abs/2611.20644)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mkingopng/instrumenting-failure) · ★ 0 |
| [**Corrupting Ties: Investigating Robustness to Bias Injection Across Multi-Agent Network Topologies**](https://arxiv.org/abs/2611.21804)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop**](https://arxiv.org/abs/2611.21152)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory**](https://arxiv.org/abs/2611.21019)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Navital Gym: Rule-Graded Agent Environments for Indian Workflows**](https://arxiv.org/abs/2611.20924)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Navitallabs/navital-gym) · ★ 3 |
| [**Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures**](https://arxiv.org/abs/2611.20595)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Sajib-006/silentguard) · ★ 1 |
| [**A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents**](https://arxiv.org/abs/2611.21376)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Instructions Before Actions: Prospective and Retrospective Language Supervision for Driving Vision-Language-Action Data**](https://arxiv.org/abs/2611.20631)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**HydroMind: A Checkable Agent for Autonomous Hydrological Research**](https://arxiv.org/abs/2611.23323)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**HEAMS: Holistic Evaluation of Agent Memory Systems**](https://arxiv.org/abs/2611.20144)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/milatechtransfer/heams) · ★ 7 |
| [**Interactive Structured Environment Scaling for Large Language Model Agentic Reasoning**](https://arxiv.org/abs/2611.19871)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Facts Change, Which Decisions Break? Dependency-Aware Context Graphs for Agents**](https://arxiv.org/abs/2611.19859)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations**](https://arxiv.org/abs/2611.20218)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning**](https://arxiv.org/abs/2611.20045)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Recovery Gone Too Far: Understanding and Repairing Risky Fallback in LLM Agents**](https://arxiv.org/abs/2611.19886)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix**](https://arxiv.org/abs/2611.19752)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/thenexuslab/stalebench-release) · ★ 0 |
| [**A Hierarchical Statistical Framework for Evaluating Agent Reliability**](https://arxiv.org/abs/2611.19614)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Behavioral Assurance for Socially Deployed AI Agents**](https://arxiv.org/abs/2611.19564)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LLM Trading Agents Earn Beta, Not Alpha: A Look-Ahead-Free Benchmark**](https://arxiv.org/abs/2611.19530)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/jackson-cmd/risk-aware-trading-agents) · ★ 447 |
| [**Does a completed simulation run mean a usable urban wind result for AI agents?**](https://arxiv.org/abs/2611.19385)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**One Run Is Not Enough: Reminding a small Gemma 4 coding agent of its last finding made no measurable difference in a paired test**](https://arxiv.org/abs/2611.19359)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/renorai/gemma4-memory-study) · ★ 0 |
| [**Macro Control and Capability Evaluation of Black-Box World Models: A Two-Regime Framework for LLM-Agent Markets**](https://arxiv.org/abs/2611.19311)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns**](https://arxiv.org/abs/2611.19244)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Auditable Authorization for LLM Agents: Empirical Evidence Across Model, Harness, and Workflow Layers**](https://arxiv.org/abs/2611.19237)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Can an Agent Rethink What It Knows? Selective Scene Memory Updates in a Changing World**](https://arxiv.org/abs/2611.19227)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VAST: Compiling Grounded Vulnerability Scenarios into Verifiable, Multi-Step Environments for Evaluating LLM Red-Team Agents**](https://arxiv.org/abs/2611.19465)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**HospitalBench: Diagnosing Where and Why Embodied Agents Fail on Long Hospital Task Chains**](https://arxiv.org/abs/2611.19274)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Beyond Plain MCP: Do Decision Models and Code Mode Make Tool Use Cheaper and Faster?**](https://arxiv.org/abs/2611.19123)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/abhishek085/mcp-decision-layer) · ★ 0 |
| [**Latency, Speech Recognition and Turn-Taking in Voice Agents for Spanish Phone Negotiation: An Externally Measured Comparison of Pipecat, LiveKit and GPT-Live**](https://arxiv.org/abs/2611.19118)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/AILabFr8tech/voice-negotiation-agents) · ★ 0 |
| [**Can Agentic LLMs Write Task-Based Parallel Code? A Study of OpenMP Tasking, HPX, StarPU and TTG**](https://arxiv.org/abs/2611.19105)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Omni-Workspace: Benchmarking Omni-Modal AI Assistants on Multimodal Workspace Tasks**](https://arxiv.org/abs/2611.19202)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination**](https://arxiv.org/abs/2611.18514)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Smart Home Agents Make Capable but Unpredictable Grid Operators**](https://arxiv.org/abs/2611.18395)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Do Machines Learn Deviance From Their Peers? A Randomized Test of Differential Association With AI Agents**](https://arxiv.org/abs/2611.18098)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents**](https://arxiv.org/abs/2611.17955)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/McGill-NLP/webarena-pro) · ★ 15 |
| [**OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination**](https://arxiv.org/abs/2611.17933)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/adminblackjack/OutfitterBench) · ★ 5 |
| [**Can Agents Keep Up with Time? An Empirical Analysis of Temporal Adaptation After a Conversational Hiatus**](https://arxiv.org/abs/2611.17806)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Adoreu2/session-rekindling-benchmark) · ★ 0 |
| [**What LLM Agents See and What Users Say**](https://arxiv.org/abs/2611.17639)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Generated Evaluation Suites as Diversity-Driven Search for Real Agent Regressions**](https://arxiv.org/abs/2611.17632)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**](https://arxiv.org/abs/2611.17610)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mahmoudsajjadi/pace) · ★ 3 |
| [**TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents**](https://arxiv.org/abs/2611.18493)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/tokencraftdata/agentic-compliance) · ★ 0 |
| [**Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation**](https://arxiv.org/abs/2611.18471)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent**](https://arxiv.org/abs/2611.17939)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration**](https://arxiv.org/abs/2611.17931)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Securing Multi-Agent Systems by Design**](https://arxiv.org/abs/2611.17883)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agent-as-a-Judge**](https://arxiv.org/abs/2611.18067)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 36 | [GitHub](https://github.com/ModalityDance/Awesome-Agent-as-a-Judge) · ★ 159 |
| [**HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup**](https://arxiv.org/abs/2611.18443)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/BeeuniLab/pheragent) · ★ 1 |
| [**MemeEconomy: Do LLM Agents Trade Ethics for Survival?**](https://arxiv.org/abs/2611.18908)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://syed-nazmus-sakib.github.io/MemeEconomy/) |
| [**Benchmark Factory: Agentic Benchmark Creation via Dataset Curation and Label-Free Quality Anchors**](https://arxiv.org/abs/2611.18890)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**We Have All the Cards: Securing Agent Cards at the Operational Trust Boundary of the Agent2Agent Protocol**](https://arxiv.org/abs/2611.18887)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents**](https://arxiv.org/abs/2611.17539)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent**](https://arxiv.org/abs/2611.17515)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/harrisonm23-byte/HuggingFaceML1) · ★ 0 |
| [**Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent**](https://arxiv.org/abs/2611.17520)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Interpreting Coding Agents Through Their Behavioral Trajectories**](https://arxiv.org/abs/2611.17440)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/SWE-rebench/trajectory-analyzer) · ★ 1 |
| [**Time-Consistent Evaluation of Hierarchical Code Graphs for SWE Agents**](https://arxiv.org/abs/2611.17388)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AgentSSL: Can MLE Agents Leverage Unlabeled Data?**](https://arxiv.org/abs/2611.17323)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/akanksha-sarkar/AgentSSL) · ★ 0 |
| [**LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds**](https://arxiv.org/abs/2611.17267)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents**](https://arxiv.org/abs/2611.17167)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/ZJU-REAL/decision-agents) · ★ 50 |
| [**AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design**](https://arxiv.org/abs/2611.16991)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents**](https://arxiv.org/abs/2611.16744)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Singularity-Bench: Can Agents Build Agents?**](https://arxiv.org/abs/2611.16591)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Infini-AI-Lab/singularity-bench) · ★ 19 |
| [**AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents**](https://arxiv.org/abs/2611.16590)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/flyingView/AstroMemBench-v1) · ★ 1 |
| [**ReA-Bench: Benchmarking Responsible Agent Auditing**](https://arxiv.org/abs/2611.16493)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments**](https://arxiv.org/abs/2611.16485)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/MinhThanghus/drydock-eval) · ★ 3 |
| [**How Should Planning Agents ReSHAPE Their Search Space?**](https://arxiv.org/abs/2611.16466)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection**](https://arxiv.org/abs/2611.16693)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Eliciting and Mitigating Specification Satisficing in Coding Agents**](https://arxiv.org/abs/2611.16289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SwarmSafe-Delta: Isolating Message Effects on LLM Agent Safety**](https://arxiv.org/abs/2611.16123)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments**](https://arxiv.org/abs/2611.17460)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/naver-ai/unfinished-bench) · ★ 1 |
| [**HEIR: Harness Egocentric Intent for Human-Robot Interactions**](https://arxiv.org/abs/2611.17238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Reward-Driven Collider Physics Challenges for Self-Improving Agentic AI via Reinforcement Learning**](https://arxiv.org/abs/2611.15885)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Before AI Agents Negotiate for Us: A Competitive Tournament of Rule-Based, Search, Optimization, Learned, and Language-Model Negotiators Under Scarcity**](https://arxiv.org/abs/2611.15838)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/AILabFr8tech/wehaveadeal) · ★ 0 |
| [**NIBench: benchmarking autonomous AI agents for execution, skill evolution and scientific judgment in neuroimaging**](https://arxiv.org/abs/2611.15831)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Read and Ignore: What Self-Directed LLM Agents Do in Public Service Scenarios**](https://arxiv.org/abs/2611.15460)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**guardscope: Measuring Which Actions Runtime Controls Check in LLM Agent Systems**](https://arxiv.org/abs/2611.15223)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/VulcanLab/guardscope) · ★ 1 |
| [**WordInferBench: Can Agents Infer How to Edit from Word Document Context?**](https://arxiv.org/abs/2611.15189)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Termination Lag: Coding Agents Solve Early but Stop Late**](https://arxiv.org/abs/2611.14960)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving**](https://arxiv.org/abs/2611.14949)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Trained on What Screen Readers Cannot Read: Accessibility Debt in the GUI Corpora Behind Computer-Use Agents**](https://arxiv.org/abs/2611.16107)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**JustRUA: A Controlled Study of GPT-6 Robot-Use Agents**](https://arxiv.org/abs/2611.16009)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ZefanW/JustRUA) · ★ 7 |
| [**VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender**](https://arxiv.org/abs/2611.15789)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/vibeprevisbench/vibeprevisbench) · ★ 26 |
| [**GHAgentCI: A Dataset of Coding-Agent Invocations in CI Workflow Histories**](https://arxiv.org/abs/2611.15522)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration**](https://arxiv.org/abs/2611.15521)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents**](https://arxiv.org/abs/2611.15118)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making**](https://arxiv.org/abs/2611.14901)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents**](https://arxiv.org/abs/2611.14864)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Can Agents Relive Past Experiences? Diagnosing Event-Affect Decoupling in Affective-Episodic Retrospection**](https://arxiv.org/abs/2611.15655)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://anonymous.4open.science/r/A412/) |
| [**CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems**](https://arxiv.org/abs/2611.14980)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue**](https://arxiv.org/abs/2611.14925)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Repository-Grounded Rubrics for Execution-Free Evaluation of Coding Agents**](https://arxiv.org/abs/2611.23309)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/faros-ai/repository-grounded-rubrics) · ★ 0 |
| [**SynthCorp: A Platform for Creating Benchmarks for Data Agents**](https://arxiv.org/abs/2611.14765)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Cleaning an Agent's History Hurts When the World Still Holds the Error**](https://arxiv.org/abs/2611.14654)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**OverServe: Resource Amplification Attacks on SaaS Agents via Tool--Prompt Co-Design**](https://arxiv.org/abs/2611.14808)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Evaluators of AI Agents Disagree: An Empirical Study of Native Scoring, LLM Judges, and Commit-Boundary Checks on tau2-bench**](https://arxiv.org/abs/2611.14581)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents**](https://arxiv.org/abs/2611.14493)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents**](https://arxiv.org/abs/2611.14256)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents**](https://arxiv.org/abs/2611.13713)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Agent Benchmarks Stop Ranking Before They Run Out of Tasks**](https://arxiv.org/abs/2611.13541)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving**](https://arxiv.org/abs/2611.13412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces**](https://arxiv.org/abs/2611.14364)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**BioMem: Agentic Memory for Biomedical LLM Agents**](https://arxiv.org/abs/2611.13426)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies**](https://arxiv.org/abs/2611.14488)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LEASH: Stay Safe in Agentic Robotics**](https://arxiv.org/abs/2611.14115)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Dependency Fabrication in Repository Deployment Agents**](https://arxiv.org/abs/2611.23305)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**No finite rulebook can certify every safe program: an impossibility theorem for gatekeeping AI agents**](https://arxiv.org/abs/2611.13367)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic AI**](https://arxiv.org/abs/2611.13333)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them**](https://arxiv.org/abs/2611.13254)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases**](https://arxiv.org/abs/2611.13246)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://huggingface.co/datasets/ExpertCrowd/ec-swe) |
| [**From Questions to Decisions: Benchmarking How LLM Agents Acquire Decision-Relevant Information from Human Beings**](https://arxiv.org/abs/2611.13015)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AgentScript-Eval: Benchmarking LLMs and Agents for Code Generation in an Enterprise DSL**](https://arxiv.org/abs/2611.13183)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Compile-Gated Lean Proof Refactoring with Enterprise Agent Practices: A Model per Step under a US\$3 Cap, Followed by Programmatic Rewrite Rules**](https://arxiv.org/abs/2611.13011)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AutoBuddy: Evaluating Proactive, Always-On Agents on Task Discovery and Execution in a Simulated Workplace**](https://arxiv.org/abs/2611.12393)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Detecting Shadow AI: Unsanctioned LLM Agents on Enterprise Endpoints: A Taxonomy, an Open Detector and a Controlled Evaluation**](https://arxiv.org/abs/2611.12377)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/jeremy1392/IntuneAgentDetector) · ★ 0 |
| [**AMSchem: Automated Schematic Visualization of AMS Circuits via Verifiable Agentic Generation**](https://arxiv.org/abs/2611.12333)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://www.amschem.com/benchmark) |
| [**Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding**](https://arxiv.org/abs/2611.12128)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Joi-Bench-Task: Benchmarking Task Coordination in Full-duplex Voice Agents through Interactive Simulation**](https://arxiv.org/abs/2611.12118)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Evaluating AI Agents for Industrial-Level Chip Floorplanning: A Framework and Empirical Study**](https://arxiv.org/abs/2611.12048)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchmarking language models and agents for scientific reasoning in evolving materials laboratories**](https://arxiv.org/abs/2611.12014)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization**](https://arxiv.org/abs/2611.11995)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LEGION: Benchmarking Language Agents on Sparse-Signal Investigation Under Adversarial Noise**](https://arxiv.org/abs/2611.11896)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Correct Answers from Insufficient Histories: A Controlled Study of Agent Memory Evaluation**](https://arxiv.org/abs/2611.11840)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You**](https://arxiv.org/abs/2611.12705)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks**](https://arxiv.org/abs/2611.12386)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Harness Matters: Measuring and Dissecting Security Resilience in Web Agents**](https://arxiv.org/abs/2611.11971)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Publications as benchmarks: auditing AI agents on spatial transcriptomics alignment**](https://arxiv.org/abs/2611.11796)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems**](https://arxiv.org/abs/2611.12856)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://lab.einsia.ai/workflowarena) |
| [**Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension**](https://arxiv.org/abs/2611.12412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Third Eye: Beyond Immediate Gains in Recursive Self-Improvement**](https://arxiv.org/abs/2611.12988)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ICLayout-Bench: Benchmarking LLM Agents for Custom Circuit Layout Design**](https://arxiv.org/abs/2611.12982)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/lizhangmai/ICLayout-Bench) · ★ 8 |
| [**Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior**](https://arxiv.org/abs/2611.11581)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Safeguarding Agentic AI in Radiology Workflows: A Multimodel Evaluation of Rule-based and Large Language Model-based Verification**](https://arxiv.org/abs/2611.11541)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ibrarad/radiology-agent-safeguards) · ★ 0 |
| [**A Physical Testbed for Self-Driving Laboratories: Comparing Bayesian and Agentic Optimization in a Minimal Closed-Loop Color Formulation Task**](https://arxiv.org/abs/2611.11690)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models**](https://arxiv.org/abs/2611.11571)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/nawaralseelawi/untrusted-model-agentsec) · ★ 0 |
| [**On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents**](https://arxiv.org/abs/2611.11506)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding**](https://arxiv.org/abs/2611.11437)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://vitagent.github.io/) |
| [**Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces**](https://arxiv.org/abs/2611.11342)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/hopit-ai/harness-mistakes-artifacts) · ★ 1 |
| [**ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping**](https://arxiv.org/abs/2611.11306)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems**](https://arxiv.org/abs/2611.11266)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Replay Fidelity in LLM Agent Evaluation: Randomness, Hidden State, and Test Oracles in AppWorld**](https://arxiv.org/abs/2611.11216)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**BuySideFlow: A Point-in-Time Benchmark for LLM Agents in Investment Research**](https://arxiv.org/abs/2611.12966)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agent Architecture Cost-Success Trade-offs: A Controlled Evaluation across Enterprise-Style SOPs**](https://arxiv.org/abs/2611.12953)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DFT-Agent Bench: Scaffold Effects and Execution Provenance in Autonomous DFT**](https://arxiv.org/abs/2611.10629)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://anonymous.4open.science/r/231e31re91287h/README.md) |
| [**Towards Identity-Preserving LLM Agents under Model Transition**](https://arxiv.org/abs/2611.10628)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agentic discrete-event simulation for manufacturing system design: an open 3D simulator, a benchmark and an industrial case**](https://arxiv.org/abs/2611.10602)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/simulean/SimuLean) · ★ 3 |
| [**InfoOrgBench: Can Agents Turn Scattered Information into Coherent Hierarchies?**](https://arxiv.org/abs/2611.10600)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Sampling Is Not Curiosity: Why LLM Agents Should Investigate**](https://arxiv.org/abs/2611.10501)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Represented but Not Used: Value-Policy Dissociation in LLM Agents**](https://arxiv.org/abs/2611.10457)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**TurnFlow: Benchmarking User-State Reasoning in Multi-Turn LLM Agents via Scene-Guided User Simulation**](https://arxiv.org/abs/2611.10412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Trustworthy Recursive Self-Improvement with Statistical Guarantees**](https://arxiv.org/abs/2611.10787)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**CyberBinGym: Can AI Agents Turn Binary Patches into Real Exploits?**](https://arxiv.org/abs/2611.10723)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors**](https://arxiv.org/abs/2611.10620)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mainul3195/collusion-probe-pitfalls) · ★ 0 |
| [**When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization**](https://arxiv.org/abs/2611.10542)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ventr1c/BadEvolve) · ★ 0 |
| [**EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery**](https://arxiv.org/abs/2611.12934)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ranranrannervous/EarthRecord) · ★ 3 |
| [**Knowing When to Intervene: Causal Evaluation of AI Agents**](https://arxiv.org/abs/2611.09792)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective**](https://arxiv.org/abs/2611.09326)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Nudging Decision Models: Do Digital Nudges Steer Fast, Generation-Free AI Agents?**](https://arxiv.org/abs/2611.09264)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents**](https://arxiv.org/abs/2611.08946)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [GitHub](https://github.com/flex-rsi/rsi-bench) · ★ 13 |
| [**I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents**](https://arxiv.org/abs/2611.08811)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents**](https://arxiv.org/abs/2611.09802)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents**](https://arxiv.org/abs/2611.09768)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory**](https://arxiv.org/abs/2611.09721)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Much Conversation History Does an AI Agent Need?**](https://arxiv.org/abs/2611.09662)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses**](https://arxiv.org/abs/2611.09088)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use**](https://arxiv.org/abs/2611.09036)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://tooluse-dataset.github.io/) |
| [**A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics**](https://arxiv.org/abs/2611.09030)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making**](https://arxiv.org/abs/2611.08971)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DRAFT-Bench: Evaluating Frontier Agents Across the Professional Design Lifecycle**](https://arxiv.org/abs/2611.08933)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PACE: Keeping the Right Tokens in the KV Cache Is Not Enough for Long-Horizon LLM Agents**](https://arxiv.org/abs/2611.10240)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchmarking Speaker Embedders in the Sub-Second Regime for Real-Time Voice AI Agents**](https://arxiv.org/abs/2611.09516)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Enhancing Local and Global Structure in Compressed AI Agent Memory**](https://arxiv.org/abs/2611.08341)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement**](https://arxiv.org/abs/2611.08318)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [Project](https://dagroup-pku.github.io/PyRUA-Lean/RSIJudge) |
| [**MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents**](https://arxiv.org/abs/2611.07689)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/J1zz/mcp_hallu) · ★ 5 |
| [**Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies**](https://arxiv.org/abs/2611.07667)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PharmAgents2: Towards Autonomous End-to-End Drug Discovery**](https://arxiv.org/abs/2611.07653)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Beneath the Surface: What We Overlook When We Talk About Agent Evolution**](https://arxiv.org/abs/2611.07624)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**DelegateEval: Evaluating Platforms for Personal External Service Agents**](https://arxiv.org/abs/2611.07508)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance**](https://arxiv.org/abs/2611.07464)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Memory Trap: Language Agents Overgeneralize from Benign Interactions**](https://arxiv.org/abs/2611.07554)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs**](https://arxiv.org/abs/2611.07483)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering**](https://arxiv.org/abs/2611.07286)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks**](https://arxiv.org/abs/2611.08281)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling**](https://arxiv.org/abs/2611.08237)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/wxj630/terminal-bench-math-modeling) · ★ 5 |
| [**From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?**](https://arxiv.org/abs/2611.08231)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SPRING-5: Measuring Tool Documentation Repair for LLM Agents by Efficiency**](https://arxiv.org/abs/2611.10040)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Toward Safety-Aware AI Agents in Realistic Social Engineering Attack Scenarios**](https://arxiv.org/abs/2611.10037)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MetaPI: Constructing Prompt Injection Benchmarks from LLM Agent Benchmark**](https://arxiv.org/abs/2611.10026)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate**](https://arxiv.org/abs/2611.08756)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Verification Is Not Agreement: Cross-Agent LLM-to-Dafny Formalization**](https://arxiv.org/abs/2611.07073)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Closed-Loop Agent Evaluation: Layered Measurement and Self-Calibration**](https://arxiv.org/abs/2611.07051)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Trust Responsive Runtime Authorization for Agentic AI with Empirical Characterization of Policy Behavior and Parameter Sensitivity**](https://arxiv.org/abs/2611.06996)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Autonomous AI Agents Systematically Diverge From Human Preferences in Proof Formalization**](https://arxiv.org/abs/2611.06995)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record**](https://arxiv.org/abs/2611.06989)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/curiosityexplorer/two-ledger-model) · ★ 0 |
| [**Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?**](https://arxiv.org/abs/2611.07166)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://multistepswe.com) |
| [**More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty**](https://arxiv.org/abs/2611.07140)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**FrontierPhysics: Evaluating Agents for End-to-End Physics Research**](https://arxiv.org/abs/2611.06910)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**CompressionBench: How can your coding agents compress LLMs?**](https://arxiv.org/abs/2611.06858)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ServerBench: How can your coding agents design specialized LLM serving systems?**](https://arxiv.org/abs/2611.06841)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Task-Efficient Agent Evaluation Using Cached Traces**](https://arxiv.org/abs/2611.06803)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks**](https://arxiv.org/abs/2611.06687)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification**](https://arxiv.org/abs/2611.06662)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**FlyHash for LLM Agent Memory: An Empirical Validation and a New Application**](https://arxiv.org/abs/2611.05791)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mohanji/flyhash-agent-memory) · ★ 1 |
| [**AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents**](https://arxiv.org/abs/2611.06674)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Zero-Shot Coordination among LLM Agents**](https://arxiv.org/abs/2611.06409)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [GitHub](https://github.com/ahayler/zsc-llm-agents) · ★ 8 |
| [**The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models**](https://arxiv.org/abs/2611.06116)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/mhuyut/harness-is-the-model) · ★ 0 |
| [**How Do AI Agents Waste Your Money?**](https://arxiv.org/abs/2611.07238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**{\tau}-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks**](https://arxiv.org/abs/2611.07203)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lilt/tau-bench-lilt) · ★ 5 |
| [**When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Handoff Summaries**](https://arxiv.org/abs/2611.06545)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Chuw1/handoff-audit) · ★ 0 |
| [**Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks**](https://arxiv.org/abs/2611.06414)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mbzuai-nlp/LExMem) · ★ 0 |
| [**TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration**](https://arxiv.org/abs/2611.05827)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lililibaohang/TandemBench) · ★ 1 |
| [**A Framework for Context Enrichment and Selective Robustness in LLM Social Agents**](https://arxiv.org/abs/2611.06914)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?**](https://arxiv.org/abs/2611.06483)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://rethinking-agentic-rl.github.io/) |
| [**Welfare Regard in Multi-Agent Systems**](https://arxiv.org/abs/2611.10017)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Code Works but the License Doesn't: Evaluating License Constraint Handling in Coding Agents**](https://arxiv.org/abs/2611.23299)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PAYWORTHY: Can LLMs Predict Which Freelance Jobs an AI Agent Will Complete?**](https://arxiv.org/abs/2611.05759)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PersonaCodeBench: Evaluating Coding Agents in Persona-driven Human-Interactive Sessions**](https://arxiv.org/abs/2611.05739)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Do Artificial Agents Make Decisions in Light of Visual Data?**](https://arxiv.org/abs/2611.05671)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge**](https://arxiv.org/abs/2611.05662)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard**](https://arxiv.org/abs/2611.05650)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | — |
| [**SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories**](https://arxiv.org/abs/2611.05512)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [Project](https://huggingface.co/datasets/HuanzhiMao/SlackBench) |
| [**Towards Robust Long-Lived Agents: Benchmarking Experience Lifecycles in Evolving Environments**](https://arxiv.org/abs/2611.05450)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?**](https://arxiv.org/abs/2611.05108)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Artifact-to-Capability: Diagnosing Breaks in Capability Formation of Self-Evolving Agents in a Controlled Environment**](https://arxiv.org/abs/2611.04952)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud**](https://arxiv.org/abs/2611.04879)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/wuyoscar/scamworld-bench) · ★ 9 |
| [**AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests**](https://arxiv.org/abs/2611.04813)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems**](https://arxiv.org/abs/2611.04556)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Cooperative-AI-Foundation/inter-agent-influence) · ★ 6 |
| [**Signals: Continuous Diagnostics of AI Agents**](https://arxiv.org/abs/2611.04507)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Silent Instrument Errors Reorder Agent Leaderboards**](https://arxiv.org/abs/2611.04399)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/YangzeLiu/eval-instrument-disclosure) · ★ 0 |
| [**DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?**](https://arxiv.org/abs/2611.04228)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://dualworld.netlify.app/) |
| [**Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?**](https://arxiv.org/abs/2611.04203)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**OperAItor: An Agentic Framework for Fault-Tolerant Operation of Chemical Processes**](https://arxiv.org/abs/2611.05179)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents**](https://arxiv.org/abs/2611.04894)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**$\tau$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems**](https://arxiv.org/abs/2611.04459)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/nbharaths/tau-rec) · ★ 8 |
| [**Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents**](https://arxiv.org/abs/2611.04393)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation**](https://arxiv.org/abs/2611.04289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When the Consumer Is an Agent: Execution-Grounded Service-Level Agreements**](https://arxiv.org/abs/2611.04182)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Prospective Memory for Proactive LLM Agents**](https://arxiv.org/abs/2611.05731)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis**](https://arxiv.org/abs/2611.05720)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents**](https://arxiv.org/abs/2611.05036)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition**](https://arxiv.org/abs/2611.04420)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects**](https://arxiv.org/abs/2611.03412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents**](https://arxiv.org/abs/2611.03384)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents**](https://arxiv.org/abs/2611.03238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents**](https://arxiv.org/abs/2611.02797)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [GitHub](https://github.com/theseus-labs-rsi/SelfImprove-Bench) · ★ 6 |
| [**GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation**](https://arxiv.org/abs/2611.02698)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets**](https://arxiv.org/abs/2611.02484)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction**](https://arxiv.org/abs/2611.03223)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**WebHarbor: Docking Real Websites for Evolving GUI Agent Environments**](https://arxiv.org/abs/2611.03634)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/aiming-lab/WebHarbor) · ★ 79 |
| [**DiabAgent: Toward Agentic Physiological Control**](https://arxiv.org/abs/2611.03601)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Four Bridges: Measuring Deception Propensity in a Multi-Agent Game**](https://arxiv.org/abs/2611.03600)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Top-$k$ Retrieval Leaves Memory Value Undetermined**](https://arxiv.org/abs/2611.03289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures**](https://arxiv.org/abs/2611.02826)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/rxnminer/RxnMiner) · ★ 6 |
| [**Predictive Safety Guardrails Do Not Always Make LLM Agents Safer**](https://arxiv.org/abs/2611.02815)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings**](https://arxiv.org/abs/2611.02659)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/gNucleus-AI/freecad-validator) · ★ 22 |
| [**Measuring AI Agents as Teammates with Collaborative Intelligence**](https://arxiv.org/abs/2611.02633)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [Project](https://zou-group.github.io/collaborative-intelligence) |
| [**EEFA: A Framework for the Ethical Evaluation of AI Agents**](https://arxiv.org/abs/2611.02561)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MAGAR: Multimodal Agents for GUI-Based 3D Mechanical Assembly and Minimal Rework**](https://arxiv.org/abs/2611.02472)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents**](https://arxiv.org/abs/2611.02319)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study**](https://arxiv.org/abs/2611.03555)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL**](https://arxiv.org/abs/2611.03551)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Coding Agents Sustain Continual Evolution without Forgetting?**](https://arxiv.org/abs/2611.03219)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [GitHub](https://github.com/THU-Agent/continual-harness-evolution) · ★ 9 |
| [**Beyond Accuracy: How Quantization Affects Coding Agents**](https://arxiv.org/abs/2611.02368)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**MemShift: Separating Detection from Repair in LLM-Derived Personal Memory**](https://arxiv.org/abs/2611.02338)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/zichuanxu/memshift) · ★ 0 |
| [**VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably**](https://arxiv.org/abs/2611.03575)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ACTOR: Action-Centered Temporal Organization for Literary Role-Playing Agents**](https://arxiv.org/abs/2611.03184)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/SilentStar233/ACTOR) · ★ 5 |
| [**What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory**](https://arxiv.org/abs/2611.03930)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://chihhsuan-yang.github.io/AAMAS2027-ConditionalMemory/) |
| [**Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain**](https://arxiv.org/abs/2611.03853)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions**](https://arxiv.org/abs/2611.03765)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost**](https://arxiv.org/abs/2611.03852)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents**](https://arxiv.org/abs/2611.03754)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use**](https://arxiv.org/abs/2611.03982)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [Project](https://geshijoker.github.io/slate/) |
| [**Peer Memory Changes Who LLM Agents Consult Without a Detected Gain in Answer Accuracy**](https://arxiv.org/abs/2611.09990)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents**](https://arxiv.org/abs/2611.01527)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging**](https://