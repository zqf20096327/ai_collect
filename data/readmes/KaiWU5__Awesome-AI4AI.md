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

<p><strong>Living catalog: 1462 papers</strong> · 668 benchmarks · 966 harness studies · 331 model studies<br><sub>Collections overlap. The original survey covers 223 papers.</sub></p>

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

- 📚 **2026-11-16 — 314 papers added.** Expanded Benchmarks, Harness Design, and Model Design with verified new and previously missed papers; rebuilt the full catalog and both ranking families.
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

> **Latest metric check: 2026-11-16.** Title-verified citations for 1417/1478 catalog records; 14 records retain prior verified counts and 47 records remain without a verified index count. GitHub stars refreshed for 409 records across 404 repositories. 3 configured GitHub repositories could not be refreshed; previous star counts are retained. Complete snapshot dates advance only when every relevant record is verified.

### Top Ranking Papers by Average Monthly Citations

| Paper | Venue | Date | Citations | Avg. cites/month | Code |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**Kimi K3: Open Frontier Intelligence**](https://arxiv.org/abs/2607.24653) | arXiv | <nobr>2026-07</nobr> | 384 | **128.0** | [GitHub](https://github.com/MoonshotAI/Kimi-K3) · ★ 9,093 |
| [**AlphaEvolve: A coding agent for scientific and algorithmic discovery**](https://arxiv.org/abs/2506.13131) | arXiv | <nobr>2025-06</nobr> | 1656 | **103.5** | — |
| [**Towards End-to-End Automation of AI Research**](https://doi.org/10.1038/s41586-026-10265-5) | Nature 2026 | <nobr>2026-03</nobr> | 542 | **77.4** | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) · ★ 7,512 |
| [**Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**](https://doi.org/10.3233/faia251160) | European Conference on Artificial Intelligence (ECAI) | <nobr>2025-04</nobr> | 1235 | **68.6** | [GitHub](https://github.com/mem0ai/mem0) · ★ 69,062 |
| [**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**](https://arxiv.org/abs/2601.11868) | arXiv | <nobr>2026-01</nobr> | 612 | **68.0** | [GitHub](https://github.com/harbor-framework/terminal-bench-1) · ★ 2,617 |
| [**Meta-Harness: End-to-End Optimization of Model Harnesses**](https://arxiv.org/abs/2603.28052) | arXiv | <nobr>2026-03</nobr> | 432 | **61.7** | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) · ★ 1,254 |
| [**Memory in the Age of AI Agents**](https://arxiv.org/abs/2512.13564) | arXiv preprint arXiv:2512.13564 | <nobr>2025-12</nobr> | 399 | **39.9** | — |
| [**The Berkeley Function Calling Leaderboard (BFCL): From tool use to agentic evaluation of large language models**](https://proceedings.mlr.press/v267/patil25a.html) | Proceedings of the 42nd International Conference on Machine Learning | <nobr>2025</nobr> | 634 | **39.6** | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,078 |
| [**RRSI: Regularized Recursive Self-Improvement of Agent Harnesses**](https://arxiv.org/abs/2609.24972) | arXiv | <nobr>2026-09</nobr> | 39 | **39.0** | [GitHub](https://github.com/google-research/rrsi) · ★ 1,777 |
| [**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models**](https://arxiv.org/abs/2510.04618) | arXiv | <nobr>2025-10</nobr> | 453 | **37.8** | [GitHub](https://github.com/ace-agent/ace) · ★ 1,460 |

### 🏆 Most-Cited Papers by Year

<details open markdown="1">
<summary><b>Top 12 of 2026</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**](https://arxiv.org/abs/2601.11868)<br><sub>arXiv</sub> | <nobr>2026-01</nobr> | 612 | [GitHub](https://github.com/harbor-framework/terminal-bench-1) · ★ 2,617 |
| [**Towards End-to-End Automation of AI Research**](https://doi.org/10.1038/s41586-026-10265-5)<br><sub>Nature 2026</sub> | <nobr>2026-03</nobr> | 542 | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) · ★ 7,512 |
| [**Meta-Harness: End-to-End Optimization of Model Harnesses**](https://arxiv.org/abs/2603.28052)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 432 | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) · ★ 1,254 |
| [**Kimi K3: Open Frontier Intelligence**](https://arxiv.org/abs/2607.24653)<br><sub>arXiv</sub> | <nobr>2026-07</nobr> | 384 | [GitHub](https://github.com/MoonshotAI/Kimi-K3) · ★ 9,093 |
| [**Self-Harness: Harnesses That Improve Themselves**](https://arxiv.org/abs/2606.09498)<br><sub>arXiv</sub> | <nobr>2026-06</nobr> | 148 | [GitHub](https://github.com/qzzqzzb/Self-Harness) · ★ 144 |
| [**Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering**](https://arxiv.org/abs/2604.08224)<br><sub>arXiv preprint arXiv:2604.08224</sub> | <nobr>2026-04</nobr> | 126 | — |
| [**DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks**](https://arxiv.org/abs/2607.07946)<br><sub>arXiv preprint arXiv:2607.07946</sub> | <nobr>2026-07</nobr> | 110 | [GitHub](https://github.com/datacurve-ai/deep-swe) · ★ 1,909 |
| [**Code as Agent Harness**](https://arxiv.org/abs/2605.18747)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 107 | [GitHub](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) · ★ 778 |
| [**PostTrainBench: Can LLM Agents Automate LLM Post-Training?**](https://arxiv.org/abs/2603.08640)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 105 | [GitHub](https://github.com/aisa-group/PostTrainBench) · ★ 623 |
| [**SkillOS: Learning Skill Curation for Self-Evolving Agents**](https://arxiv.org/abs/2605.06614)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 93 | — |
| [**Natural-Language Agent Harnesses**](https://arxiv.org/abs/2603.25723)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 88 | — |
| [**ProgramBench: Can Language Models Rebuild Programs From Scratch?**](https://arxiv.org/abs/2605.03546)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 85 | [GitHub](https://github.com/facebookresearch/ProgramBench) · ★ 980 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2025</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**AlphaEvolve: A coding agent for scientific and algorithmic discovery**](https://arxiv.org/abs/2506.13131)<br><sub>arXiv</sub> | <nobr>2025-06</nobr> | 1656 | — |
| [**Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**](https://doi.org/10.3233/faia251160)<br><sub>European Conference on Artificial Intelligence (ECAI)</sub> | <nobr>2025-04</nobr> | 1235 | [GitHub](https://github.com/mem0ai/mem0) · ★ 69,062 |
| [**A-MEM: Agentic Memory for LLM Agents**](https://arxiv.org/abs/2502.12110)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-02</nobr> | 1222 | [GitHub](https://github.com/WujiangXu/A-mem) · ★ 1,017 |
| [**Why Do Multi-Agent LLM Systems Fail?**](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-03</nobr> | 756 | [GitHub](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · ★ 438 |
| [**The Berkeley Function Calling Leaderboard (BFCL): From tool use to agentic evaluation of large language models**](https://proceedings.mlr.press/v267/patil25a.html)<br><sub>Proceedings of the 42nd International Conference on Machine Learning</sub> | <nobr>2025</nobr> | 634 | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,078 |
| [**Group-in-Group Policy Optimization for LLM Agent Training**](https://arxiv.org/abs/2505.10978)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-05</nobr> | 548 | [GitHub](https://github.com/langfengQ/verl-agent) · ★ 2,449 |
| [**LLMs Get Lost In Multi-Turn Conversation**](https://arxiv.org/abs/2505.06120)<br><sub>International Conference on Learning Representations</sub> | <nobr>2025-05</nobr> | 527 | [GitHub](https://github.com/microsoft/lost_in_conversation) · ★ 305 |
| [**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models**](https://arxiv.org/abs/2510.04618)<br><sub>arXiv</sub> | <nobr>2025-10</nobr> | 453 | [GitHub](https://github.com/ace-agent/ace) · ★ 1,460 |
| [**SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?**](https://arxiv.org/abs/2509.16941)<br><sub>arXiv</sub> | <nobr>2025-09</nobr> | 442 | [GitHub](https://github.com/scaleapi/SWE-bench_Pro-os) · ★ 565 |
| [**Memory in the Age of AI Agents**](https://arxiv.org/abs/2512.13564)<br><sub>arXiv preprint arXiv:2512.13564</sub> | <nobr>2025-12</nobr> | 399 | — |
| [**Darwin Godel Machine: Open-ended evolution of self-improving agents**](https://openreview.net/forum?id=pUpzQZTvGY)<br><sub>arXiv</sub> | <nobr>2025-05</nobr> | 394 | [GitHub](https://github.com/jennyzzt/dgm) · ★ 2,513 |
| [**PaperBench: Evaluating AI's ability to replicate AI research**](https://arxiv.org/abs/2504.01848)<br><sub>arXiv</sub> | <nobr>2025-04</nobr> | 342 | [GitHub](https://github.com/openai/frontier-evals) · ★ 1,342 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2024</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains**](https://arxiv.org/abs/2406.12045)<br><sub>arXiv</sub> | <nobr>2024-06</nobr> | 1502 | [GitHub](https://github.com/sierra-research/tau-bench) · ★ 1,509 |
| [**OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**](https://arxiv.org/abs/2404.07972)<br><sub>NeurIPS 2024</sub> | <nobr>2024-04</nobr> | 1356 | [GitHub](https://github.com/xlang-ai/OSWorld) · ★ 3,263 |
| [**Demystifying LLM-Based Software Engineering Agents**](https://doi.org/10.1145/3715754)<br><sub>Proceedings of the ACM on Software Engineering</sub> | <nobr>2024-07</nobr> | 876 | [GitHub](https://github.com/OpenAutoCoder/Agentless) · ★ 2,137 |
| [**Self-rewarding language models**](https://proceedings.mlr.press/v235/yuan24d.html)<br><sub>arXiv</sub> | <nobr>2024-01</nobr> | 774 | — |
| [**WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models**](https://arxiv.org/abs/2401.13919)<br><sub>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</sub> | <nobr>2024-01</nobr> | 568 | [GitHub](https://github.com/MinorJerry/WebVoyager) · ★ 1,130 |
| [**VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks**](https://arxiv.org/abs/2401.13649)<br><sub>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</sub> | <nobr>2024-01</nobr> | 512 | [GitHub](https://github.com/web-arena-x/visualwebarena) · ★ 489 |
| [**TravelPlanner: A Benchmark for Real-World Planning with Language Agents**](https://arxiv.org/abs/2402.01622)<br><sub>International Conference on Machine Learning</sub> | <nobr>2024-02</nobr> | 511 | [GitHub](https://github.com/OSU-NLP-Group/TravelPlanner) · ★ 570 |
| [**MLE-bench: Evaluating machine learning agents on machine learning engineering**](https://arxiv.org/abs/2410.07095)<br><sub>ICLR 2025</sub> | <nobr>2024-10</nobr> | 502 | [GitHub](https://github.com/openai/mle-bench) · ★ 1,799 |
| [**Agent Workflow Memory**](https://arxiv.org/abs/2409.07429)<br><sub>Forty-second International Conference on Machine Learning</sub> | <nobr>2024-09</nobr> | 495 | [GitHub](https://github.com/zorazrw/agent-workflow-memory) · ★ 484 |
| [**AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents**](https://arxiv.org/abs/2405.14573)<br><sub>International Conference on Learning Representations</sub> | <nobr>2024-05</nobr> | 486 | [GitHub](https://github.com/google-research/android_world) · ★ 1,014 |
| [**When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs**](https://arxiv.org/abs/2406.01297)<br><sub>Transactions of the Association for Computational Linguistics</sub> | <nobr>2024-06</nobr> | 471 | — |
| [**Automated design of agentic systems**](https://arxiv.org/abs/2408.08435)<br><sub>ICLR 2025</sub> | <nobr>2024-08</nobr> | 444 | [GitHub](https://github.com/ShengranHu/ADAS) · ★ 1,666 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2023</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Generative Agents: Interactive Simulacra of Human Behavior**](https://arxiv.org/abs/2304.03442)<br><sub>Proceedings of the 36th annual acm symposium on user interface software and technology</sub> | <nobr>2023-04</nobr> | 8273 | [GitHub](https://github.com/joonspk-research/generative_agents) · ★ 22,388 |
| [**Self-Refine: Iterative refinement with self-feedback**](https://arxiv.org/abs/2303.17651)<br><sub>NeurIPS 2023</sub> | <nobr>2023-03</nobr> | 6234 | [GitHub](https://github.com/madaan/self-refine) · ★ 851 |
| [**Toolformer: Language Models Can Teach Themselves to Use Tools**](https://arxiv.org/abs/2302.04761)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-02</nobr> | 6192 | — |
| [**Reflexion: language agents with verbal reinforcement learning**](https://arxiv.org/abs/2303.11366)<br><sub>NeurIPS 2023</sub> | <nobr>2023-03</nobr> | 6117 | [GitHub](https://github.com/noahshinn/reflexion) · ★ 3,433 |
| [**Tree of Thoughts: Deliberate Problem Solving with Large Language Models**](https://arxiv.org/abs/2305.10601)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-05</nobr> | 5152 | [GitHub](https://github.com/princeton-nlp/tree-of-thought-llm) · ★ 6,090 |
| [**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**](https://arxiv.org/abs/2310.06770)<br><sub>ICLR 2024</sub> | <nobr>2023-10</nobr> | 4403 | [GitHub](https://github.com/SWE-bench/SWE-bench) · ★ 6,200 |
| [**Voyager: An Open-Ended Embodied Agent with Large Language Models**](https://arxiv.org/abs/2305.16291)<br><sub>Transactions on Machine Learning Research</sub> | <nobr>2023-05</nobr> | 2787 | [GitHub](https://github.com/MineDojo/Voyager) · ★ 7,330 |
| [**ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs**](https://arxiv.org/abs/2307.16789)<br><sub>International Conference on Learning Representations</sub> | <nobr>2023-07</nobr> | 2466 | [GitHub](https://github.com/OpenBMB/ToolBench) · ★ 5,772 |
| [**WebArena: A Realistic Web Environment for Building Autonomous Agents**](https://arxiv.org/abs/2307.13854)<br><sub>ICLR 2024</sub> | <nobr>2023-07</nobr> | 2300 | [GitHub](https://github.com/web-arena-x/webarena) · ★ 1,645 |
| [**MemGPT: Towards LLMs as Operating Systems**](https://arxiv.org/abs/2310.08560)<br><sub>arXiv preprint arXiv:2310.08560</sub> | <nobr>2023-10</nobr> | 1910 | [GitHub](https://github.com/letta-ai/letta) · ★ 25,463 |
| [**Gorilla: Large Language Model Connected with Massive APIs**](https://arxiv.org/abs/2305.15334)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-05</nobr> | 1767 | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,078 |
| [**Mind2Web: Towards a Generalist Agent for the Web**](https://arxiv.org/abs/2306.06070)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-06</nobr> | 1554 | [GitHub](https://github.com/OSU-NLP-Group/Mind2Web) · ★ 1,038 |

</details>



## 🧪 Benchmarks

<p align="center">
  <img src="assets/benchmarks.png" width="92%" alt="Figure 3 from the companion survey: What Is AI4AI? A Taxonomy">
</p>

> **668 papers** · Survey-curated collection, newest first. Cross-collection papers may appear in more than one section.

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination**](https://arxiv.org/abs/2611.18514)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Smart Home Agents Make Capable but Unpredictable Grid Operators**](https://arxiv.org/abs/2611.18395)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Do Machines Learn Deviance From Their Peers? A Randomized Test of Differential Association With AI Agents**](https://arxiv.org/abs/2611.18098)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents**](https://arxiv.org/abs/2611.17955)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/McGill-NLP/webarena-pro) · ★ 1 |
| [**OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination**](https://arxiv.org/abs/2611.17933)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/adminblackjack/OutfitterBench) · ★ 3 |
| [**Can Agents Keep Up with Time? An Empirical Analysis of Temporal Adaptation After a Conversational Hiatus**](https://arxiv.org/abs/2611.17806)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/Adoreu2/session-rekindling-benchmark) · ★ 0 |
| [**What LLM Agents See and What Users Say**](https://arxiv.org/abs/2611.17639)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Generated Evaluation Suites as Diversity-Driven Search for Real Agent Regressions**](https://arxiv.org/abs/2611.17632)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs**](https://arxiv.org/abs/2611.17610)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/mahmoudsajjadi/pace) · ★ 0 |
| [**TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents**](https://arxiv.org/abs/2611.18493)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/tokencraftdata/agentic-compliance) · ★ 0 |
| [**Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation**](https://arxiv.org/abs/2611.18471)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent**](https://arxiv.org/abs/2611.17939)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration**](https://arxiv.org/abs/2611.17931)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Securing Multi-Agent Systems by Design**](https://arxiv.org/abs/2611.17883)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Agent-as-a-Judge**](https://arxiv.org/abs/2611.18067)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 36 | [GitHub](https://github.com/ModalityDance/Awesome-Agent-as-a-Judge) · ★ 157 |
| [**HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup**](https://arxiv.org/abs/2611.18443)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/BeeuniLab/pheragent) · ★ 1 |
| [**Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents**](https://arxiv.org/abs/2611.17539)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent**](https://arxiv.org/abs/2611.17515)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/harrisonm23-byte/HuggingFaceML1) · ★ 0 |
| [**Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent**](https://arxiv.org/abs/2611.17520)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**Interpreting Coding Agents Through Their Behavioral Trajectories**](https://arxiv.org/abs/2611.17440)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/SWE-rebench/trajectory-analyzer) · ★ 0 |
| [**Time-Consistent Evaluation of Hierarchical Code Graphs for SWE Agents**](https://arxiv.org/abs/2611.17388)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | — |
| [**AgentSSL: Can MLE Agents Leverage Unlabeled Data?**](https://arxiv.org/abs/2611.17323)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/akanksha-sarkar/AgentSSL) · ★ 0 |
| [**LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds**](https://arxiv.org/abs/2611.17267)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents**](https://arxiv.org/abs/2611.17167)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ZJU-REAL/decision-agents) · ★ 47 |
| [**AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design**](https://arxiv.org/abs/2611.16991)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents**](https://arxiv.org/abs/2611.16744)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Singularity-Bench: Can Agents Build Agents?**](https://arxiv.org/abs/2611.16591)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Infini-AI-Lab/singularity-bench) · ★ 9 |
| [**AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents**](https://arxiv.org/abs/2611.16590)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/flyingView/AstroMemBench-v1) · ★ 1 |
| [**ReA-Bench: Benchmarking Responsible Agent Auditing**](https://arxiv.org/abs/2611.16493)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments**](https://arxiv.org/abs/2611.16485)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/MinhThanghus/drydock-eval) · ★ 1 |
| [**How Should Planning Agents ReSHAPE Their Search Space?**](https://arxiv.org/abs/2611.16466)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection**](https://arxiv.org/abs/2611.16693)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Eliciting and Mitigating Specification Satisficing in Coding Agents**](https://arxiv.org/abs/2611.16289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SwarmSafe-Delta: Isolating Message Effects on LLM Agent Safety**](https://arxiv.org/abs/2611.16123)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments**](https://arxiv.org/abs/2611.17460)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | — | [GitHub](https://github.com/naver-ai/unfinished-bench) · ★ 0 |
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
| [**JustRUA: A Controlled Study of GPT-6 Robot-Use Agents**](https://arxiv.org/abs/2611.16009)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ZefanW/JustRUA) · ★ 2 |
| [**VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender**](https://arxiv.org/abs/2611.15789)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/vibeprevisbench/vibeprevisbench) · ★ 11 |
| [**GHAgentCI: A Dataset of Coding-Agent Invocations in CI Workflow Histories**](https://arxiv.org/abs/2611.15522)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration**](https://arxiv.org/abs/2611.15521)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents**](https://arxiv.org/abs/2611.15118)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making**](https://arxiv.org/abs/2611.14901)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents**](https://arxiv.org/abs/2611.14864)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Agents Relive Past Experiences? Diagnosing Event-Affect Decoupling in Affective-Episodic Retrospection**](https://arxiv.org/abs/2611.15655)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://anonymous.4open.science/r/A412/) |
| [**CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems**](https://arxiv.org/abs/2611.14980)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue**](https://arxiv.org/abs/2611.14925)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SynthCorp: A Platform for Creating Benchmarks for Data Agents**](https://arxiv.org/abs/2611.14765)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Cleaning an Agent's History Hurts When the World Still Holds the Error**](https://arxiv.org/abs/2611.14654)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**OverServe: Resource Amplification Attacks on SaaS Agents via Tool--Prompt Co-Design**](https://arxiv.org/abs/2611.14808)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Evaluators of AI Agents Disagree: An Empirical Study of Native Scoring, LLM Judges, and Commit-Boundary Checks on tau2-bench**](https://arxiv.org/abs/2611.14581)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents**](https://arxiv.org/abs/2611.14493)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents**](https://arxiv.org/abs/2611.14256)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents**](https://arxiv.org/abs/2611.13713)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agent Benchmarks Stop Ranking Before They Run Out of Tasks**](https://arxiv.org/abs/2611.13541)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving**](https://arxiv.org/abs/2611.13412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces**](https://arxiv.org/abs/2611.14364)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**BioMem: Agentic Memory for Biomedical LLM Agents**](https://arxiv.org/abs/2611.13426)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies**](https://arxiv.org/abs/2611.14488)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LEASH: Stay Safe in Agentic Robotics**](https://arxiv.org/abs/2611.14115)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
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
| [**ICLayout-Bench: Benchmarking LLM Agents for Custom Circuit Layout Design**](https://arxiv.org/abs/2611.12982)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lizhangmai/ICLayout-Bench) · ★ 6 |
| [**Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior**](https://arxiv.org/abs/2611.11581)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Safeguarding Agentic AI in Radiology Workflows: A Multimodel Evaluation of Rule-based and Large Language Model-based Verification**](https://arxiv.org/abs/2611.11541)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ibrarad/radiology-agent-safeguards) · ★ 0 |
| [**A Physical Testbed for Self-Driving Laboratories: Comparing Bayesian and Agentic Optimization in a Minimal Closed-Loop Color Formulation Task**](https://arxiv.org/abs/2611.11690)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models**](https://arxiv.org/abs/2611.11571)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/nawaralseelawi/untrusted-model-agentsec) · ★ 0 |
| [**On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents**](https://arxiv.org/abs/2611.11506)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding**](https://arxiv.org/abs/2611.11437)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://vitagent.github.io/) |
| [**Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces**](https://arxiv.org/abs/2611.11342)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/hopit-ai/harness-mistakes-artifacts) · ★ 1 |
| [**ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping**](https://arxiv.org/abs/2611.11306)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems**](https://arxiv.org/abs/2611.11266)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Replay Fidelity in LLM Agent Evaluation: Randomness, Hidden State, and Test Oracles in AppWorld**](https://arxiv.org/abs/2611.11216)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**BuySideFlow: A Point-in-Time Benchmark for LLM Agents in Investment Research**](https://arxiv.org/abs/2611.12966)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agent Architecture Cost-Success Trade-offs: A Controlled Evaluation across Enterprise-Style SOPs**](https://arxiv.org/abs/2611.12953)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DFT-Agent Bench: Scaffold Effects and Execution Provenance in Autonomous DFT**](https://arxiv.org/abs/2611.10629)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://anonymous.4open.science/r/231e31re91287h/README.md) |
| [**Towards Identity-Preserving LLM Agents under Model Transition**](https://arxiv.org/abs/2611.10628)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Agentic discrete-event simulation for manufacturing system design: an open 3D simulator, a benchmark and an industrial case**](https://arxiv.org/abs/2611.10602)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/simulean/SimuLean) · ★ 1 |
| [**InfoOrgBench: Can Agents Turn Scattered Information into Coherent Hierarchies?**](https://arxiv.org/abs/2611.10600)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Sampling Is Not Curiosity: Why LLM Agents Should Investigate**](https://arxiv.org/abs/2611.10501)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Represented but Not Used: Value-Policy Dissociation in LLM Agents**](https://arxiv.org/abs/2611.10457)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**TurnFlow: Benchmarking User-State Reasoning in Multi-Turn LLM Agents via Scene-Guided User Simulation**](https://arxiv.org/abs/2611.10412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Trustworthy Recursive Self-Improvement with Statistical Guarantees**](https://arxiv.org/abs/2611.10787)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**CyberBinGym: Can AI Agents Turn Binary Patches into Real Exploits?**](https://arxiv.org/abs/2611.10723)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors**](https://arxiv.org/abs/2611.10620)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mainul3195/collusion-probe-pitfalls) · ★ 0 |
| [**When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization**](https://arxiv.org/abs/2611.10542)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ventr1c/BadEvolve) · ★ 0 |
| [**EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery**](https://arxiv.org/abs/2611.12934)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ranranrannervous/EarthRecord) · ★ 3 |
| [**Knowing When to Intervene: Causal Evaluation of AI Agents**](https://arxiv.org/abs/2611.09792)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective**](https://arxiv.org/abs/2611.09326)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Nudging Decision Models: Do Digital Nudges Steer Fast, Generation-Free AI Agents?**](https://arxiv.org/abs/2611.09264)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents**](https://arxiv.org/abs/2611.08946)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [GitHub](https://github.com/flex-rsi/rsi-bench) · ★ 12 |
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
| [**AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents**](https://arxiv.org/abs/2611.06674)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Zero-Shot Coordination among LLM Agents**](https://arxiv.org/abs/2611.06409)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ahayler/zsc-llm-agents) · ★ 7 |
| [**The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models**](https://arxiv.org/abs/2611.06116)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mhuyut/harness-is-the-model) · ★ 0 |
| [**How Do AI Agents Waste Your Money?**](https://arxiv.org/abs/2611.07238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**{\tau}-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks**](https://arxiv.org/abs/2611.07203)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lilt/tau-bench-lilt) · ★ 4 |
| [**When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Handoff Summaries**](https://arxiv.org/abs/2611.06545)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Chuw1/handoff-audit) · ★ 0 |
| [**Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks**](https://arxiv.org/abs/2611.06414)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mbzuai-nlp/LExMem) · ★ 1 |
| [**TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration**](https://arxiv.org/abs/2611.05827)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lililibaohang/TandemBench) · ★ 0 |
| [**A Framework for Context Enrichment and Selective Robustness in LLM Social Agents**](https://arxiv.org/abs/2611.06914)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?**](https://arxiv.org/abs/2611.06483)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://rethinking-agentic-rl.github.io/) |
| [**Welfare Regard in Multi-Agent Systems**](https://arxiv.org/abs/2611.10017)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PAYWORTHY: Can LLMs Predict Which Freelance Jobs an AI Agent Will Complete?**](https://arxiv.org/abs/2611.05759)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PersonaCodeBench: Evaluating Coding Agents in Persona-driven Human-Interactive Sessions**](https://arxiv.org/abs/2611.05739)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Do Artificial Agents Make Decisions in Light of Visual Data?**](https://arxiv.org/abs/2611.05671)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge**](https://arxiv.org/abs/2611.05662)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard**](https://arxiv.org/abs/2611.05650)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories**](https://arxiv.org/abs/2611.05512)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [Project](https://huggingface.co/datasets/HuanzhiMao/SlackBench) |
| [**Towards Robust Long-Lived Agents: Benchmarking Experience Lifecycles in Evolving Environments**](https://arxiv.org/abs/2611.05450)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?**](https://arxiv.org/abs/2611.05108)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Artifact-to-Capability: Diagnosing Breaks in Capability Formation of Self-Evolving Agents in a Controlled Environment**](https://arxiv.org/abs/2611.04952)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud**](https://arxiv.org/abs/2611.04879)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/wuyoscar/scamworld-bench) · ★ 9 |
| [**AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests**](https://arxiv.org/abs/2611.04813)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems**](https://arxiv.org/abs/2611.04556)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Cooperative-AI-Foundation/inter-agent-influence) · ★ 5 |
| [**Signals: Continuous Diagnostics of AI Agents**](https://arxiv.org/abs/2611.04507)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Silent Instrument Errors Reorder Agent Leaderboards**](https://arxiv.org/abs/2611.04399)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/YangzeLiu/eval-instrument-disclosure) · ★ 0 |
| [**DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?**](https://arxiv.org/abs/2611.04228)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://dualworld.netlify.app/) |
| [**Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?**](https://arxiv.org/abs/2611.04203)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**OperAItor: An Agentic Framework for Fault-Tolerant Operation of Chemical Processes**](https://arxiv.org/abs/2611.05179)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents**](https://arxiv.org/abs/2611.04894)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**$\tau$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems**](https://arxiv.org/abs/2611.04459)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/nbharaths/tau-rec) · ★ 7 |
| [**Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents**](https://arxiv.org/abs/2611.04393)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation**](https://arxiv.org/abs/2611.04289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**When the Consumer Is an Agent: Execution-Grounded Service-Level Agreements**](https://arxiv.org/abs/2611.04182)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Prospective Memory for Proactive LLM Agents**](https://arxiv.org/abs/2611.05731)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis**](https://arxiv.org/abs/2611.05720)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents**](https://arxiv.org/abs/2611.05036)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition**](https://arxiv.org/abs/2611.04420)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects**](https://arxiv.org/abs/2611.03412)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents**](https://arxiv.org/abs/2611.03384)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents**](https://arxiv.org/abs/2611.03238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents**](https://arxiv.org/abs/2611.02797)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 2 | [GitHub](https://github.com/theseus-labs-rsi/SelfImprove-Bench) · ★ 5 |
| [**GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation**](https://arxiv.org/abs/2611.02698)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets**](https://arxiv.org/abs/2611.02484)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction**](https://arxiv.org/abs/2611.03223)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**WebHarbor: Docking Real Websites for Evolving GUI Agent Environments**](https://arxiv.org/abs/2611.03634)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/aiming-lab/WebHarbor) · ★ 77 |
| [**DiabAgent: Toward Agentic Physiological Control**](https://arxiv.org/abs/2611.03601)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Four Bridges: Measuring Deception Propensity in a Multi-Agent Game**](https://arxiv.org/abs/2611.03600)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Top-$k$ Retrieval Leaves Memory Value Undetermined**](https://arxiv.org/abs/2611.03289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures**](https://arxiv.org/abs/2611.02826)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/rxnminer/RxnMiner) · ★ 6 |
| [**Predictive Safety Guardrails Do Not Always Make LLM Agents Safer**](https://arxiv.org/abs/2611.02815)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings**](https://arxiv.org/abs/2611.02659)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/gNucleus-AI/freecad-validator) · ★ 22 |
| [**Measuring AI Agents as Teammates with Collaborative Intelligence**](https://arxiv.org/abs/2611.02633)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [Project](https://zou-group.github.io/collaborative-intelligence) |
| [**EEFA: A Framework for the Ethical Evaluation of AI Agents**](https://arxiv.org/abs/2611.02561)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MAGAR: Multimodal Agents for GUI-Based 3D Mechanical Assembly and Minimal Rework**](https://arxiv.org/abs/2611.02472)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents**](https://arxiv.org/abs/2611.02319)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study**](https://arxiv.org/abs/2611.03555)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL**](https://arxiv.org/abs/2611.03551)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Coding Agents Sustain Continual Evolution without Forgetting?**](https://arxiv.org/abs/2611.03219)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | [GitHub](https://github.com/THU-Agent/continual-harness-evolution) · ★ 9 |
| [**Beyond Accuracy: How Quantization Affects Coding Agents**](https://arxiv.org/abs/2611.02368)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 1 | — |
| [**MemShift: Separating Detection from Repair in LLM-Derived Personal Memory**](https://arxiv.org/abs/2611.02338)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/zichuanxu/memshift) · ★ 0 |
| [**VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably**](https://arxiv.org/abs/2611.03575)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ACTOR: Action-Centered Temporal Organization for Literary Role-Playing Agents**](https://arxiv.org/abs/2611.03184)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/SilentStar233/ACTOR) · ★ 5 |
| [**What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory**](https://arxiv.org/abs/2611.03930)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://chihhsuan-yang.github.io/AAMAS2027-ConditionalMemory/) |
| [**Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain**](https://arxiv.org/abs/2611.03853)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions**](https://arxiv.org/abs/2611.03765)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost**](https://arxiv.org/abs/2611.03852)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents**](https://arxiv.org/abs/2611.03754)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use**](https://arxiv.org/abs/2611.03982)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://geshijoker.github.io/slate/) |
| [**Peer Memory Changes Who LLM Agents Consult Without a Detected Gain in Answer Accuracy**](https://arxiv.org/abs/2611.09990)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents**](https://arxiv.org/abs/2611.01527)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging**](https://arxiv.org/abs/2611.01449)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LegoEnv: Self-Evolving Agentic Environments via Modular Recombination**](https://arxiv.org/abs/2611.01834)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks**](https://arxiv.org/abs/2611.01728)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**TriPhysBench: Evaluating Physical Intelligence for Embodied Agents**](https://arxiv.org/abs/2611.01934)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Delivered, Not Used: Evaluating Agent Memory at Its Point of Use**](https://arxiv.org/abs/2611.01718)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Just-in-Time Skill Retrieval via Long-Horizon State Tracking**](https://arxiv.org/abs/2611.01701)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents**](https://arxiv.org/abs/2611.01700)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Kirito14IT/MemHarmBench) · ★ 4 |
| [**Do Embodied VLMs Actually Use Their Scene-Graph Memory?**](https://arxiv.org/abs/2611.02056)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security**](https://arxiv.org/abs/2611.01976)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Better Answers, Weaker Evidence Control: Evidence Bypass in On-Policy Distillation**](https://arxiv.org/abs/2611.01967)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/RuoranXu/EP-OPD) · ★ 3 |
| [**Launder-Bench: Can Repository-Level Agentic Code Laundering Be Detected?**](https://arxiv.org/abs/2611.01966)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Step-Zero Attack: Agent Safety Before Observability**](https://arxiv.org/abs/2611.01953)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RECEIPT: Measuring and Repairing the Return Assumption of LLM Agents in Web Service Operations**](https://arxiv.org/abs/2611.01930)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**AgenticMobility: An Open-Source Platform for Multi-AI-Agent Mobility Dynamics**](https://arxiv.org/abs/2611.01918)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**An auditable agentic pipeline for variant-to-gene prioritisation, validated against orthogonal functional evidence**](https://arxiv.org/abs/2611.01461)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Large Language Model Agents Learn by Watching Tutorial Videos?**](https://arxiv.org/abs/2611.01460)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Decision Models as Policy Gates for Coding Agents: Explicit Policy Boundaries Improve Detection and Reduce False Alarms**](https://arxiv.org/abs/2611.02155)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/agentapprove/decision-policy-rules) · ★ 1 |
| [**Multi-Agent Collusion and the J-Space**](https://arxiv.org/abs/2611.02153)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks?**](https://arxiv.org/abs/2611.02017)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Miraclecsc/Switch-SWE) · ★ 26 |
| [**Decision-Centric Research: A Calibrated Decision Model and Benchmark for Scientific Agents**](https://arxiv.org/abs/2611.00774)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Designing Informative Actions: Action Construction for Long-Horizon Research Agents**](https://arxiv.org/abs/2611.00773)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When LLMs Modify Themselves: Convergence, Values, and Stopping in Iterative Self-Improvement**](https://arxiv.org/abs/2611.01304)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CivicBench: A Benchmark and Memory Framework for Web-Based Civic Data Analytics**](https://arxiv.org/abs/2611.01145)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Can Agentic AI Undermine Its Own Assurance Loop? Closed-Loop Dependency Assurance for Cognitive Network Digital Twins**](https://arxiv.org/abs/2611.00838)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Verifier Is Part of the Simulator: Evidence-View Gaming in Agentic Equation Discovery**](https://arxiv.org/abs/2611.01334)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/oroikono/kagamaya) · ★ 2 |
| [**CuriousTogether: Implications of Curiosity and Cultural Grounding in Multi-Agent LLM Interactions**](https://arxiv.org/abs/2611.01301)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Toward Bounding Coding-Agent Autonomy in Software Maintenance: A Pilot Study of Boundary Contracts**](https://arxiv.org/abs/2611.01265)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Dependable Agents Need Hard and Fuzzy Rules**](https://arxiv.org/abs/2611.01043)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AStockArena: Beyond Returns, Can We Entrust Real Capital to the Decisions of Financial Agents?**](https://arxiv.org/abs/2611.00515)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Do Social Influence Pressures Move LLM Agents? Evidence from Delegated Audit Judgment**](https://arxiv.org/abs/2611.00508)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CompSkill: Compiling Execution Experience for Skill Retrieval**](https://arxiv.org/abs/2611.01115)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/satoshinji2992/CompSkill) · ★ 1 |
| [**When 200 OK Is Not an Answer: Silent Fetch Failures in Agentic Web Content Acquisition**](https://arxiv.org/abs/2611.00884)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**MemU-Bench: Benchmarking GUI Agents on Long-Horizon User Interactions**](https://arxiv.org/abs/2611.00191)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents**](https://arxiv.org/abs/2610.42004)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents**](https://arxiv.org/abs/2610.41272)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Dependence-Aware Risk Assessment and Optimal Design of AI-Agent Safeguard Systems**](https://arxiv.org/abs/2611.00386)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Decentralized Multi-Agent Coordination and Communication in Shared Codebases**](https://arxiv.org/abs/2611.00314)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [Project](https://lingyunxiao18.github.io/ParallACT/) |
| [**Fidelity Collapses with Table Size, Not Turn Count: Delivery Architecture in a Deployed Tool-Using Agent**](https://arxiv.org/abs/2611.00442)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When AI Agents Act on Our Behalf: A Taxonomy of Human-Agent Interaction Failure**](https://arxiv.org/abs/2611.00291)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Real Computation or Merely Naming? A Pre-Registered Mechanism Audit of 25 Cognitive-Architecture Modules in an LLM-Based Agent System**](https://arxiv.org/abs/2610.41604)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Cross-Interface Authorization for AI Computer-Use Agents**](https://arxiv.org/abs/2610.41397)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Operon-S1: a fast decision controller for long-horizon biomedical agents**](https://arxiv.org/abs/2610.41350)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**ImplicitHop: Evaluating knowledge integration across context and memory**](https://arxiv.org/abs/2610.41169)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Confident Fools or Careful Searchers? A Behavioural Study of When LLMs Search Beyond Their Static Internal Memory**](https://arxiv.org/abs/2610.41124)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents**](https://arxiv.org/abs/2610.41482)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed?**](https://arxiv.org/abs/2610.41435)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization**](https://arxiv.org/abs/2610.41157)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/shangliy/lineage-is-memory) · ★ 1 |
| [**When Disclosure Is Compulsory: Evaluating Ride-Hailing Rebalancing Policies with Self-Interested LLM Driver Agents**](https://arxiv.org/abs/2610.41132)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents**](https://arxiv.org/abs/2610.41177)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents**](https://arxiv.org/abs/2610.41905)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces**](https://arxiv.org/abs/2610.41885)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/AI45Lab/PrivacyTrace) · ★ 1 |
| [**Benchmarking Forecasting Agents on Yesterday's Tomorrows**](https://arxiv.org/abs/2610.40940)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**More Rules, Longer Lists? Benchmarking Self-Evolving Agents on a Hidden-Rule Curriculum**](https://arxiv.org/abs/2610.40758)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**DynaRev: Benchmarking Web Agents under Dynamic Goal Revision**](https://arxiv.org/abs/2610.40133)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/zsq259/DynaRev) · ★ 0 |
| [**Bank-World: A Benchmark for Evaluating Agents on Banking Workflows**](https://arxiv.org/abs/2610.39733)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**From Intent to Improvement: Agentic Dataset Search for Better Model Training**](https://arxiv.org/abs/2610.39608)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/nju-websoft/AgenticDS) · ★ 2 |
| [**ATLAS-Bench: An Agentic Tool-Use Benchmark for Local Area Search**](https://arxiv.org/abs/2610.39438)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentDecept: Benchmarking Deceptive Behavior in Tool-Using LLM Agents under Pressure**](https://arxiv.org/abs/2610.39377)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Well-Specified and Well-Tested? Assessing SWE-bench-Style Datasets with a Self-Evolving Agent**](https://arxiv.org/abs/2610.39417)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection**](https://arxiv.org/abs/2610.39122)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/SaFo-Lab/Evolve-IPI) · ★ 3 |
| [**rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment**](https://arxiv.org/abs/2610.40488)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/ArtKanke/rTaste) · ★ 2 |
| [**How Specific Do I Need to Be? Effects of User Query Underspecification on Deep Research Agents**](https://arxiv.org/abs/2610.39413)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents**](https://arxiv.org/abs/2611.00138)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**BABA-Bench: Evaluating Long-Horizon Patient-Advocacy Agents**](https://arxiv.org/abs/2610.41076)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ReplayRCA: Measuring Post-hoc Diagnosis and Live Oversight of Agent Failures by Counterfactual Replay**](https://arxiv.org/abs/2610.41025)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/jeremy1392/RCAreplay) · ★ 1 |
| [**P-ContextBench: From Personal Fact Recall to Personalized Agent Behavior**](https://arxiv.org/abs/2610.40959)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Does Recursive Knowledge Construction Help Agents Verify Consensus Claims in Science?**](https://arxiv.org/abs/2610.40906)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**"Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents**](https://arxiv.org/abs/2610.40753)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Characterizing LLM Agent Behaviors in Module Shadowing Environments**](https://arxiv.org/abs/2610.40716)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**PrivacyFlow: Privacy in AI Agents through Information Flow Analysis and Consequence-Aware Risk Management**](https://arxiv.org/abs/2610.40714)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In**](https://arxiv.org/abs/2610.40588)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/leonidas1712/precrime-agents) · ★ 1 |
| [**VeriCUA: Verification as Agentic Exploration for Computer-Using Agents**](https://arxiv.org/abs/2610.40578)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success**](https://arxiv.org/abs/2610.40444)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation**](https://arxiv.org/abs/2610.40246)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry**](https://arxiv.org/abs/2610.39781)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Before the Next Rollout: Diagnosing Skill Utility Shifts from Policy Updates**](https://arxiv.org/abs/2610.39358)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**What Does "Now" Mean to Your Computer-Use Agent? Stale Screenshots, Page Loads, and Which Check to Run Before a Click**](https://arxiv.org/abs/2610.39282)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/multimodal-ai-engineering/preflight-bench) · ★ 0 |
| [**When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder**](https://arxiv.org/abs/2610.40611)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Gym-Anything for Robotics: Scaling physical simulations with digital agents**](https://arxiv.org/abs/2610.40565)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 2 | [Project](https://gym-anything.github.io/robotics) |
| [**Practical Assessment of Agentic Systems in Acoustics**](https://arxiv.org/abs/2610.39685)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy**](https://arxiv.org/abs/2610.39532)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering**](https://arxiv.org/abs/2610.39468)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Clean Sheets and Checkpoints: Evidence Complexity for Certifying Sequential Agent Risk**](https://arxiv.org/abs/2610.39124)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**HERA: Assessing an Autonomous Agent for Quantum Device Measurement**](https://arxiv.org/abs/2610.39074)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/sharpelab/hera-paper-data) · ★ 0 |
| [**HALO: Human-Grounded Granular Evaluation of Proactive Agents**](https://arxiv.org/abs/2610.39086)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers**](https://arxiv.org/abs/2610.39234)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Lzzzzzzzzzzy/AgentHeal) · ★ 2 |
| [**Training LLM Agents to Automate LLM Post-Training with RSI-Dojo**](https://arxiv.org/abs/2611.03698)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SideTaskBench: Measuring Unauthorized Side-Task Delivery in Coding Agents**](https://arxiv.org/abs/2611.14548)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/xywen97/SideTaskBench) · ★ 1 |
| [**Aligning Autoresearch: Co-Improvement between Agents and Humans**](https://arxiv.org/abs/2610.38882)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Beyond fabrication: Misattributed numbers in papers written by AI research agents**](https://arxiv.org/abs/2610.38691)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/mos3b-faqeeh/agent-integrity-analysis) · ★ 0 |
| [**An Alignment Benchmark for Enterprise Agents on Era by Eon**](https://arxiv.org/abs/2610.38544)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents**](https://arxiv.org/abs/2610.38392)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**DecompGym: Benchmarking LLM Agents on Designing Decomposition Algorithms**](https://arxiv.org/abs/2610.38175)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/SIKAI-C/DecompGym) · ★ 2 |
| [**SkillCT: A Multidimensional Benchmark and Execution-Free Baseline for Agent Skill Assessment**](https://arxiv.org/abs/2610.38147)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0**](https://arxiv.org/abs/2610.38617)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/snyk-labs/snyk-vulnbench) · ★ 10 |
| [**EPSBench: Benchmarking LLM Agents for Earnings Forecasting**](https://arxiv.org/abs/2610.38293)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**TreasuryQA Bench: Can AI Agents Work an Archive of Scanned Financial Records?**](https://arxiv.org/abs/2610.38924)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Where You Inject Matters: The Trust Region Effect in LLM Agents**](https://arxiv.org/abs/2610.38867)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?**](https://arxiv.org/abs/2610.38342)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems**](https://arxiv.org/abs/2610.38215)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/wangxiaoyang0412/disparity-laundering) · ★ 0 |
| [**Distilling the Shape of Uncertainty: What On-Policy Distillation Learns and How to Predict It**](https://arxiv.org/abs/2610.39020)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/maybenotime/opd-esc) · ★ 0 |
| [**WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video**](https://arxiv.org/abs/2610.38352)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Vendster: An Evaluation Arena to Investigate How Forecasting Tool Quality Affects LLM Agent Behaviors in Buyer-Vendor Negotiation**](https://arxiv.org/abs/2610.38292)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/amazon-science/Vendster) · ★ 1 |
| [**Precedent or Intent? What Coding Agents Follow When Evolving Existing Code**](https://arxiv.org/abs/2610.38244)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction**](https://arxiv.org/abs/2610.38209)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Repairs for Whom? Evaluator-Executor Mismatch in Selecting Repairs for Failed LLM Agents**](https://arxiv.org/abs/2610.38610)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents**](https://arxiv.org/abs/2610.37166)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents**](https://arxiv.org/abs/2610.37081)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 2 | — |
| [**AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations**](https://arxiv.org/abs/2610.36980)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents**](https://arxiv.org/abs/2610.36878)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments**](https://arxiv.org/abs/2610.36484)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/kiante-fernandez/CogArena) · ★ 3 |
| [**FeatureArc: Benchmarking Coding Agents on Evolving Features**](https://arxiv.org/abs/2610.37434)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements**](https://arxiv.org/abs/2610.36584)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization**](https://arxiv.org/abs/2610.36553)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Agentic Backdoors via Pretraining Poisoning**](https://arxiv.org/abs/2610.37741)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/safety-research/agentic-backdoor) · ★ 17 |
| [**Benchmarking Task Takeover Across Agent Handoffs**](https://arxiv.org/abs/2610.36523)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces**](https://arxiv.org/abs/2610.37255)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/2020-qqtcg/HRP) · ★ 1 |
| [**SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World**](https://arxiv.org/abs/2610.37919)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**FilingLoop: Evaluating and Evolving LLM Agents for Corporate Disclosure Review and Revision**](https://arxiv.org/abs/2610.37905)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Evaluating and improving AI agents for sequencing protocol understanding**](https://arxiv.org/abs/2610.37851)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening**](https://arxiv.org/abs/2610.37849)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis**](https://arxiv.org/abs/2610.37830)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs**](https://arxiv.org/abs/2610.37809)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**WebAnything: From the Wild Web to Scalable Agent Environments**](https://arxiv.org/abs/2610.37786)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/china-qijizhifeng/Web-Anything) · ★ 9 |
| [**Scan Before You Install: Detecting and Mitigating Local and Composite Vulnerabilities in Skills**](https://arxiv.org/abs/2610.37901)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files**](https://arxiv.org/abs/2610.37738)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills**](https://arxiv.org/abs/2610.37734)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions**](https://arxiv.org/abs/2610.37624)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information**](https://arxiv.org/abs/2610.37571)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Concordat: Typed Sessions for LLM Agents**](https://arxiv.org/abs/2610.37461)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/miladsikaroudi/concordat) · ★ 2 |
| [**M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents**](https://arxiv.org/abs/2610.37459)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/hannesill/m4) · ★ 50 |
| [**Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution**](https://arxiv.org/abs/2610.37201)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/valleysprings/BiPA) · ★ 4 |
| [**God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation**](https://arxiv.org/abs/2610.36623)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**InfraDev: Can Coding Agents Develop AI Infrastructure, and How Can We Tell?**](https://arxiv.org/abs/2610.36589)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents**](https://arxiv.org/abs/2610.36570)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors**](https://arxiv.org/abs/2610.36544)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents**](https://arxiv.org/abs/2610.36471)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://method-notes.github.io/ReCoF/) |
| [**Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure**](https://arxiv.org/abs/2610.36453)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation**](https://arxiv.org/abs/2610.36435)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents**](https://arxiv.org/abs/2610.37567)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 3 | — |
| [**Test-Time Communication in Trading Agent Swarms**](https://arxiv.org/abs/2610.37448)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?**](https://arxiv.org/abs/2610.37276)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Blindfold: Keeping the Audit Coin Secret from LLM Agents**](https://arxiv.org/abs/2610.37055)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance**](https://arxiv.org/abs/2610.36947)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents**](https://arxiv.org/abs/2610.36476)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue**](https://arxiv.org/abs/2610.36813)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**kw-bench: Breaking Frontier Harnesses on Real-World Tasks**](https://arxiv.org/abs/2610.36405)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/GSequist/kw-bench) · ★ 0 |
| [**Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses**](https://arxiv.org/abs/2610.36114)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents**](https://arxiv.org/abs/2610.35767)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams**](https://arxiv.org/abs/2610.35439)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization**](https://arxiv.org/abs/2610.35316)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites**](https://arxiv.org/abs/2610.35031)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ClinVerse: A Realistic Multi-Agent Diagnostic Environment for Training and Evaluating Medical Agents**](https://arxiv.org/abs/2610.34878)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory**](https://arxiv.org/abs/2610.34767)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SearchHorizonBench: A Benchmark for Search Value in AI Agents**](https://arxiv.org/abs/2610.34714)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SlowLab: Benchmarking Autonomous AI Agents on a Year of Experiments They Cannot Undo**](https://arxiv.org/abs/2610.34644)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/dingningpei/slowlab-benchmark) · ★ 0 |
| [**Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy**](https://arxiv.org/abs/2610.35832)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 4 | [Project](https://internrobotics.github.io/EBench-Astra-Tech-Report/) |
| [**SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills**](https://arxiv.org/abs/2610.35215)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Tasselszcx/SkillLifeBench) · ★ 1 |
| [**How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation**](https://arxiv.org/abs/2610.34938)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents**](https://arxiv.org/abs/2610.34763)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Quantifying Claim Smoothing by LLM Research Agents**](https://arxiv.org/abs/2610.35793)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/tiasa2/SmoothScor