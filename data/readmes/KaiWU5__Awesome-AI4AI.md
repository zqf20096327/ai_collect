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

<p><strong>Living catalog: 1148 papers</strong> · 526 benchmarks · 704 harness studies · 254 model studies<br><sub>Collections overlap. The original survey covers 223 papers.</sub></p>

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

- 📚 **2026-11-08 — 13 papers added.** Expanded Benchmarks, Harness Design, and Model Design with verified new and previously missed papers; rebuilt the full catalog and both ranking families.
- 🚀 **2026-11-08 — Latest weekly edition published.** Read the source-verified news digest below.
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

> **Updated 2026-11-08** · Weekly news picks, refreshed every Monday alongside citation rankings.
>
> **How we select:** The top stories from the trailing 30 days, scored on publisher authority, discussion volume, whether a concrete verifiable result is reported, whether it changes what agent builders do now, whether an artifact was released, and expected durability. Only primary sources are cited, and performance claims remain attributed to their publishers.

| Date · Type | News | Why it matters |
|:--|:--|:--|
| 2026‑11‑06<br><sub>Blog</sub> | [**The components of agent memory**](https://www.anthropic.com/research/components-of-agent-memory)<br><sub>Anthropic</sub> | Anthropic separates transcripts, memory notes, wikis and injected context, and tests offline dreaming to correct and reorganize them. On 25 internal-document questions it reports 61% of graded criteria with search plus a grown wiki, versus 53% with search alone. |
| 2026‑11‑05<br><sub>Paper</sub> | [**SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization**](https://arxiv.org/abs/2611.08483)<br><sub>Jiang, Qile et al. · arXiv</sub> | The authors use latent-space agent swarms and KV-cache exchange for evolutionary program search. On 21 mathematical and scientific-computing problems, they report matching competing frameworks’ 60-minute best scores in a median 3–8 minutes. |
| 2026‑11‑05<br><sub>Model release</sub> | [**GPT-6 Cyber: Advancing the frontier of aligned cybersecurity agents**](https://openai.com/index/introducing-gpt-6-cyber/)<br><sub>OpenAI</sub> | OpenAI introduces a cyber-specialized GPT-6 Astra variant for approved Daybreak Red customers in the API and Codex. It reports 48.5% on ExploitGym versus 32.1% for GPT-5.6 Cyber, and 99.93% scope adherence without its deployment prompt. |
| 2026‑11‑04<br><sub>Paper</sub> | [**EnzymeRSI: A dual-loop recursive self-improvement system for enzyme design**](https://arxiv.org/abs/2611.06321)<br><sub>Genoria AI Team et al. · arXiv</sub> | The authors evolve both harness assets and enzyme-design algorithms. They report 10 of 32 non-pre-specified luciferase candidates with at least twice wild-type activity, plus prospective A3A and polymerase tests; physical-loop results are distinguished from development-set optimization. |
| 2026‑11‑02<br><sub>Paper</sub> | [**SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents**](https://arxiv.org/abs/2611.02797)<br><sub>Xu, Yang et al. · arXiv</sub> | The authors introduce a reproducible RSI benchmark with a G0–G4 generalization ladder spanning exploration, planning and reasoning, and report that evolution gains do not consistently transfer across levels. |
| 2026‑10‑30<br><sub>Paper</sub> | [**Exo: An Architecture for Self-Improving Systems at Runtime**](https://arxiv.org/abs/2611.00463)<br><sub>Krentsel et al. · arXiv</sub> | The authors let an agent revise its harness during ongoing work behind a protected activation layer. Against a fixed-policy control, they report 35–61% lower held-out model cost on AppWorld and SREGym with comparable correctness. |
| 2026‑10‑29<br><sub>Open-weight release</sub> | [**Mistral Large 4 (Le Chonk) is now open weight**](https://mistral.ai/news/mistral-large-4-oss/)<br><sub>Mistral AI</sub> | Mistral releases the improved 1T-parameter multimodal flagship weights under its Ecosystem Open-Weight license. It reports 41% on Terminal-Bench 4.0 and 48% on the Coding Agent Index, with 47% fewer tokens than GLM-5.3 on the latter. |
| 2026‑10‑28<br><sub>Model release</sub> | [**Gemini 4 Carbon: our next frontier model**](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)<br><sub>Google DeepMind</sub> | Google announces Carbon for long-horizon engineering and cybersecurity, reporting 88.2% on SEC-bench Pro. Access begins with pre-release testing and selected cyber defenders through Fairwind; general developer and consumer access is still forthcoming. |
| 2026‑10‑23<br><sub>Model release</sub> | [**Kimi K3.1 Pro series is live**](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)<br><sub>Moonshot AI</sub> | Moonshot’s 3T-class multimodal flagship has a 1M-token context window and is available in Kimi products and the API. Moonshot reports 65.7% on Terminal-Bench 4.0; the official Hugging Face repository now contains downloadable weights. |
| 2026‑10‑18<br><sub>Open-weight release</sub> | [**Introducing Flint**](https://recursive.com/updates/introducing-recursive-flint)<br><sub>Recursive</sub> | Recursive releases a 40B-total / 2.5B-active MoE for local agentic coding and says its Eureka Machine helped develop the architecture, data, training, quantization and inference stack. The official post reports over 125 tokens/s on an M4 Pro at short contexts. |

> **Want next week's news?** Watch the repository. Citation counts, rankings, and the weekly news picks are published with maintainer updates. [Browse past editions →](highlights/README.md)

## 📈 Live Rankings

> Last complete citation snapshot: **2026-10-17**, using Semantic Scholar and OpenAlex. Rankings are discovery aids, not quality scores; audit evidence remains independent of popularity. Last complete GitHub stars snapshot: **2026-11-08**. For papers indexed as multiple versions, retain the largest title-verified count reported by the configured sources. All yearly rankings use first public appearance year; a later venue year never moves a paper into a newer cohort.

> **Latest metric check: 2026-11-08.** Title-verified citations for 1145/1164 catalog records; 13 records retain prior verified counts and 6 records remain without a verified index count. GitHub stars refreshed for 347 records across 342 repositories. Complete snapshot dates advance only when every relevant record is verified.

### Top Ranking Papers by Average Monthly Citations

| Paper | Venue | Date | Citations | Avg. cites/month | Code |
|:--|:--:|:--:|:--:|:--:|:--:|
| [**Kimi K3: Open Frontier Intelligence**](https://arxiv.org/abs/2607.24653) | arXiv | <nobr>2026-07</nobr> | 349 | **116.3** | [GitHub](https://github.com/MoonshotAI/Kimi-K3) · ★ 9,055 |
| [**AlphaEvolve: A coding agent for scientific and algorithmic discovery**](https://arxiv.org/abs/2506.13131) | arXiv | <nobr>2025-06</nobr> | 1337 | **83.6** | — |
| [**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**](https://arxiv.org/abs/2601.11868) | arXiv | <nobr>2026-01</nobr> | 612 | **68.0** | [GitHub](https://github.com/harbor-framework/terminal-bench-1) · ★ 2,614 |
| [**Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**](https://doi.org/10.3233/faia251160) | European Conference on Artificial Intelligence (ECAI) | <nobr>2025-04</nobr> | 1182 | **65.7** | [GitHub](https://github.com/mem0ai/mem0) · ★ 68,604 |
| [**Towards End-to-End Automation of AI Research**](https://doi.org/10.1038/s41586-026-10265-5) | Nature 2026 | <nobr>2026-03</nobr> | 317 | **45.3** | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) · ★ 7,477 |
| [**Meta-Harness: End-to-End Optimization of Model Harnesses**](https://arxiv.org/abs/2603.28052) | arXiv | <nobr>2026-03</nobr> | 315 | **45.0** | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) · ★ 1,250 |
| [**The Berkeley Function Calling Leaderboard (BFCL): From tool use to agentic evaluation of large language models**](https://proceedings.mlr.press/v267/patil25a.html) | Proceedings of the 42nd International Conference on Machine Learning | <nobr>2025</nobr> | 634 | **39.6** | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,064 |
| [**Memory in the Age of AI Agents**](https://arxiv.org/abs/2512.13564) | arXiv preprint arXiv:2512.13564 | <nobr>2025-12</nobr> | 381 | **38.1** | — |
| [**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models**](https://arxiv.org/abs/2510.04618) | arXiv | <nobr>2025-10</nobr> | 453 | **37.8** | [GitHub](https://github.com/ace-agent/ace) · ★ 1,434 |
| [**RRSI: Regularized Recursive Self-Improvement of Agent Harnesses**](https://arxiv.org/abs/2609.24972) | arXiv | <nobr>2026-09</nobr> | 34 | **34.0** | [GitHub](https://github.com/google-research/rrsi) · ★ 1,735 |

### 🏆 Most-Cited Papers by Year

<details open markdown="1">
<summary><b>Top 12 of 2026</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**](https://arxiv.org/abs/2601.11868)<br><sub>arXiv</sub> | <nobr>2026-01</nobr> | 612 | [GitHub](https://github.com/harbor-framework/terminal-bench-1) · ★ 2,614 |
| [**Kimi K3: Open Frontier Intelligence**](https://arxiv.org/abs/2607.24653)<br><sub>arXiv</sub> | <nobr>2026-07</nobr> | 349 | [GitHub](https://github.com/MoonshotAI/Kimi-K3) · ★ 9,055 |
| [**Towards End-to-End Automation of AI Research**](https://doi.org/10.1038/s41586-026-10265-5)<br><sub>Nature 2026</sub> | <nobr>2026-03</nobr> | 317 | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) · ★ 7,477 |
| [**Meta-Harness: End-to-End Optimization of Model Harnesses**](https://arxiv.org/abs/2603.28052)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 315 | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) · ★ 1,250 |
| [**Self-Harness: Harnesses That Improve Themselves**](https://arxiv.org/abs/2606.09498)<br><sub>arXiv</sub> | <nobr>2026-06</nobr> | 126 | [GitHub](https://github.com/qzzqzzb/Self-Harness) · ★ 140 |
| [**Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering**](https://arxiv.org/abs/2604.08224)<br><sub>arXiv preprint arXiv:2604.08224</sub> | <nobr>2026-04</nobr> | 108 | — |
| [**Code as Agent Harness**](https://arxiv.org/abs/2605.18747)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 97 | [GitHub](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers) · ★ 776 |
| [**SkillOS: Learning Skill Curation for Self-Evolving Agents**](https://arxiv.org/abs/2605.06614)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 84 | — |
| [**Natural-Language Agent Harnesses**](https://arxiv.org/abs/2603.25723)<br><sub>arXiv</sub> | <nobr>2026-03</nobr> | 84 | — |
| [**ProgramBench: Can Language Models Rebuild Programs From Scratch?**](https://arxiv.org/abs/2605.03546)<br><sub>arXiv</sub> | <nobr>2026-05</nobr> | 80 | [GitHub](https://github.com/facebookresearch/ProgramBench) · ★ 979 |
| [**DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks**](https://arxiv.org/abs/2607.07946)<br><sub>arXiv preprint arXiv:2607.07946</sub> | <nobr>2026-07</nobr> | 79 | [GitHub](https://github.com/datacurve-ai/deep-swe) · ★ 1,896 |
| [**OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks**](https://arxiv.org/abs/2606.29537)<br><sub>arXiv</sub> | <nobr>2026-06</nobr> | 79 | [GitHub](https://github.com/xlang-ai/OSWorld-V2) · ★ 412 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2025</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**AlphaEvolve: A coding agent for scientific and algorithmic discovery**](https://arxiv.org/abs/2506.13131)<br><sub>arXiv</sub> | <nobr>2025-06</nobr> | 1337 | — |
| [**A-MEM: Agentic Memory for LLM Agents**](https://arxiv.org/abs/2502.12110)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-02</nobr> | 1222 | [GitHub](https://github.com/WujiangXu/A-mem) · ★ 1,014 |
| [**Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory**](https://doi.org/10.3233/faia251160)<br><sub>European Conference on Artificial Intelligence (ECAI)</sub> | <nobr>2025-04</nobr> | 1182 | [GitHub](https://github.com/mem0ai/mem0) · ★ 68,604 |
| [**Why Do Multi-Agent LLM Systems Fail?**](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-03</nobr> | 756 | [GitHub](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · ★ 434 |
| [**The Berkeley Function Calling Leaderboard (BFCL): From tool use to agentic evaluation of large language models**](https://proceedings.mlr.press/v267/patil25a.html)<br><sub>Proceedings of the 42nd International Conference on Machine Learning</sub> | <nobr>2025</nobr> | 634 | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,064 |
| [**Group-in-Group Policy Optimization for LLM Agent Training**](https://arxiv.org/abs/2505.10978)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2025-05</nobr> | 548 | [GitHub](https://github.com/langfengQ/verl-agent) · ★ 2,431 |
| [**LLMs Get Lost In Multi-Turn Conversation**](https://arxiv.org/abs/2505.06120)<br><sub>International Conference on Learning Representations</sub> | <nobr>2025-05</nobr> | 527 | [GitHub](https://github.com/microsoft/lost_in_conversation) · ★ 302 |
| [**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models**](https://arxiv.org/abs/2510.04618)<br><sub>arXiv</sub> | <nobr>2025-10</nobr> | 453 | [GitHub](https://github.com/ace-agent/ace) · ★ 1,434 |
| [**SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?**](https://arxiv.org/abs/2509.16941)<br><sub>arXiv</sub> | <nobr>2025-09</nobr> | 427 | [GitHub](https://github.com/scaleapi/SWE-bench_Pro-os) · ★ 557 |
| [**Darwin Godel Machine: Open-ended evolution of self-improving agents**](https://openreview.net/forum?id=pUpzQZTvGY)<br><sub>arXiv</sub> | <nobr>2025-05</nobr> | 394 | [GitHub](https://github.com/jennyzzt/dgm) · ★ 2,490 |
| [**Memory in the Age of AI Agents**](https://arxiv.org/abs/2512.13564)<br><sub>arXiv preprint arXiv:2512.13564</sub> | <nobr>2025-12</nobr> | 381 | — |
| [**PaperBench: Evaluating AI's ability to replicate AI research**](https://arxiv.org/abs/2504.01848)<br><sub>arXiv</sub> | <nobr>2025-04</nobr> | 342 | [GitHub](https://github.com/openai/frontier-evals) · ★ 1,337 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2024</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains**](https://arxiv.org/abs/2406.12045)<br><sub>arXiv</sub> | <nobr>2024-06</nobr> | 1502 | [GitHub](https://github.com/sierra-research/tau-bench) · ★ 1,495 |
| [**OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**](https://arxiv.org/abs/2404.07972)<br><sub>NeurIPS 2024</sub> | <nobr>2024-04</nobr> | 1356 | [GitHub](https://github.com/xlang-ai/OSWorld) · ★ 3,256 |
| [**Demystifying LLM-Based Software Engineering Agents**](https://doi.org/10.1145/3715754)<br><sub>Proceedings of the ACM on Software Engineering</sub> | <nobr>2024-07</nobr> | 841 | [GitHub](https://github.com/OpenAutoCoder/Agentless) · ★ 2,137 |
| [**Self-rewarding language models**](https://proceedings.mlr.press/v235/yuan24d.html)<br><sub>arXiv</sub> | <nobr>2024-01</nobr> | 774 | — |
| [**WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models**](https://arxiv.org/abs/2401.13919)<br><sub>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</sub> | <nobr>2024-01</nobr> | 549 | [GitHub](https://github.com/MinorJerry/WebVoyager) · ★ 1,129 |
| [**TravelPlanner: A Benchmark for Real-World Planning with Language Agents**](https://arxiv.org/abs/2402.01622)<br><sub>International Conference on Machine Learning</sub> | <nobr>2024-02</nobr> | 511 | [GitHub](https://github.com/OSU-NLP-Group/TravelPlanner) · ★ 569 |
| [**MLE-bench: Evaluating machine learning agents on machine learning engineering**](https://arxiv.org/abs/2410.07095)<br><sub>ICLR 2025</sub> | <nobr>2024-10</nobr> | 502 | [GitHub](https://github.com/openai/mle-bench) · ★ 1,792 |
| [**VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks**](https://arxiv.org/abs/2401.13649)<br><sub>Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</sub> | <nobr>2024-01</nobr> | 495 | [GitHub](https://github.com/web-arena-x/visualwebarena) · ★ 490 |
| [**AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents**](https://arxiv.org/abs/2405.14573)<br><sub>International Conference on Learning Representations</sub> | <nobr>2024-05</nobr> | 486 | [GitHub](https://github.com/google-research/android_world) · ★ 1,009 |
| [**Agent Workflow Memory**](https://arxiv.org/abs/2409.07429)<br><sub>Forty-second International Conference on Machine Learning</sub> | <nobr>2024-09</nobr> | 474 | [GitHub](https://github.com/zorazrw/agent-workflow-memory) · ★ 483 |
| [**Automated design of agentic systems**](https://arxiv.org/abs/2408.08435)<br><sub>ICLR 2025</sub> | <nobr>2024-08</nobr> | 444 | [GitHub](https://github.com/ShengranHu/ADAS) · ★ 1,662 |
| [**AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents**](https://arxiv.org/abs/2407.18901)<br><sub>ACL 2024</sub> | <nobr>2024-07</nobr> | 439 | [GitHub](https://github.com/StonyBrookNLP/appworld) · ★ 549 |

</details>

<details markdown="1">
<summary><b>Top 12 of 2023</b> by citations</summary>

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Toolformer: Language Models Can Teach Themselves to Use Tools**](https://arxiv.org/abs/2302.04761)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-02</nobr> | 6192 | — |
| [**Reflexion: language agents with verbal reinforcement learning**](https://arxiv.org/abs/2303.11366)<br><sub>NeurIPS 2023</sub> | <nobr>2023-03</nobr> | 6117 | [GitHub](https://github.com/noahshinn/reflexion) · ★ 3,413 |
| [**Generative Agents: Interactive Simulacra of Human Behavior**](https://arxiv.org/abs/2304.03442)<br><sub>Proceedings of the 36th annual acm symposium on user interface software and technology</sub> | <nobr>2023-04</nobr> | 6015 | [GitHub](https://github.com/joonspk-research/generative_agents) · ★ 22,358 |
| [**Tree of Thoughts: Deliberate Problem Solving with Large Language Models**](https://arxiv.org/abs/2305.10601)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-05</nobr> | 5152 | [GitHub](https://github.com/princeton-nlp/tree-of-thought-llm) · ★ 6,088 |
| [**Self-Refine: Iterative refinement with self-feedback**](https://arxiv.org/abs/2303.17651)<br><sub>NeurIPS 2023</sub> | <nobr>2023-03</nobr> | 5147 | [GitHub](https://github.com/madaan/self-refine) · ★ 849 |
| [**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**](https://arxiv.org/abs/2310.06770)<br><sub>ICLR 2024</sub> | <nobr>2023-10</nobr> | 4403 | [GitHub](https://github.com/SWE-bench/SWE-bench) · ★ 6,159 |
| [**Voyager: An Open-Ended Embodied Agent with Large Language Models**](https://arxiv.org/abs/2305.16291)<br><sub>Transactions on Machine Learning Research</sub> | <nobr>2023-05</nobr> | 2667 | [GitHub](https://github.com/MineDojo/Voyager) · ★ 7,317 |
| [**ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs**](https://arxiv.org/abs/2307.16789)<br><sub>International Conference on Learning Representations</sub> | <nobr>2023-07</nobr> | 2466 | [GitHub](https://github.com/OpenBMB/ToolBench) · ★ 5,769 |
| [**WebArena: A Realistic Web Environment for Building Autonomous Agents**](https://arxiv.org/abs/2307.13854)<br><sub>ICLR 2024</sub> | <nobr>2023-07</nobr> | 2300 | [GitHub](https://github.com/web-arena-x/webarena) · ★ 1,643 |
| [**MemGPT: Towards LLMs as Operating Systems**](https://arxiv.org/abs/2310.08560)<br><sub>arXiv preprint arXiv:2310.08560</sub> | <nobr>2023-10</nobr> | 1799 | [GitHub](https://github.com/letta-ai/letta) · ★ 25,383 |
| [**Gorilla: Large Language Model Connected with Massive APIs**](https://arxiv.org/abs/2305.15334)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-05</nobr> | 1767 | [GitHub](https://github.com/ShishirPatil/gorilla) · ★ 13,064 |
| [**Mind2Web: Towards a Generalist Agent for the Web**](https://arxiv.org/abs/2306.06070)<br><sub>Advances in Neural Information Processing Systems</sub> | <nobr>2023-06</nobr> | 1554 | [GitHub](https://github.com/OSU-NLP-Group/Mind2Web) · ★ 1,037 |

</details>



## 🧪 Benchmarks

<p align="center">
  <img src="assets/benchmarks.png" width="92%" alt="Figure 3 from the companion survey: What Is AI4AI? A Taxonomy">
</p>

> **526 papers** · Survey-curated collection, newest first. Cross-collection papers may appear in more than one section.

| Paper | Date | Citations | Code |
|:--|:--:|:--:|:--:|
| [**Enhancing Local and Global Structure in Compressed AI Agent Memory**](https://arxiv.org/abs/2611.08341)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement**](https://arxiv.org/abs/2611.08318)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://dagroup-pku.github.io/PyRUA-Lean/RSIJudge) |
| [**MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents**](https://arxiv.org/abs/2611.07689)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/J1zz/mcp_hallu) · ★ 4 |
| [**Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies**](https://arxiv.org/abs/2611.07667)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PharmAgents2: Towards Autonomous End-to-End Drug Discovery**](https://arxiv.org/abs/2611.07653)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Beneath the Surface: What We Overlook When We Talk About Agent Evolution**](https://arxiv.org/abs/2611.07624)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**DelegateEval: Evaluating Platforms for Personal External Service Agents**](https://arxiv.org/abs/2611.07508)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance**](https://arxiv.org/abs/2611.07464)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Memory Trap: Language Agents Overgeneralize from Benign Interactions**](https://arxiv.org/abs/2611.07554)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs**](https://arxiv.org/abs/2611.07483)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering**](https://arxiv.org/abs/2611.07286)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks**](https://arxiv.org/abs/2611.08281)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling**](https://arxiv.org/abs/2611.08237)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/wxj630/terminal-bench-math-modeling) · ★ 5 |
| [**From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?**](https://arxiv.org/abs/2611.08231)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
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
| [**Zero-Shot Coordination among LLM Agents**](https://arxiv.org/abs/2611.06409)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/ahayler/zsc-llm-agents) · ★ 1 |
| [**The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models**](https://arxiv.org/abs/2611.06116)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mhuyut/harness-is-the-model) · ★ 0 |
| [**How Do AI Agents Waste Your Money?**](https://arxiv.org/abs/2611.07238)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**{\tau}-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks**](https://arxiv.org/abs/2611.07203)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lilt/tau-bench-lilt) · ★ 2 |
| [**When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Handoff Summaries**](https://arxiv.org/abs/2611.06545)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Chuw1/handoff-audit) · ★ 0 |
| [**Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks**](https://arxiv.org/abs/2611.06414)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/mbzuai-nlp/LExMem) · ★ 1 |
| [**TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration**](https://arxiv.org/abs/2611.05827)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/lililibaohang/TandemBench) · ★ 0 |
| [**A Framework for Context Enrichment and Selective Robustness in LLM Social Agents**](https://arxiv.org/abs/2611.06914)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?**](https://arxiv.org/abs/2611.06483)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://rethinking-agentic-rl.github.io/) |
| [**PAYWORTHY: Can LLMs Predict Which Freelance Jobs an AI Agent Will Complete?**](https://arxiv.org/abs/2611.05759)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**PersonaCodeBench: Evaluating Coding Agents in Persona-driven Human-Interactive Sessions**](https://arxiv.org/abs/2611.05739)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**How Do Artificial Agents Make Decisions in Light of Visual Data?**](https://arxiv.org/abs/2611.05671)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge**](https://arxiv.org/abs/2611.05662)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard**](https://arxiv.org/abs/2611.05650)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories**](https://arxiv.org/abs/2611.05512)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://huggingface.co/datasets/HuanzhiMao/SlackBench) |
| [**Towards Robust Long-Lived Agents: Benchmarking Experience Lifecycles in Evolving Environments**](https://arxiv.org/abs/2611.05450)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?**](https://arxiv.org/abs/2611.05108)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Artifact-to-Capability: Diagnosing Breaks in Capability Formation of Self-Evolving Agents in a Controlled Environment**](https://arxiv.org/abs/2611.04952)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud**](https://arxiv.org/abs/2611.04879)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/wuyoscar/scamworld-bench) · ★ 5 |
| [**AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests**](https://arxiv.org/abs/2611.04813)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems**](https://arxiv.org/abs/2611.04556)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Cooperative-AI-Foundation/inter-agent-influence) · ★ 4 |
| [**Signals: Continuous Diagnostics of AI Agents**](https://arxiv.org/abs/2611.04507)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Silent Instrument Errors Reorder Agent Leaderboards**](https://arxiv.org/abs/2611.04399)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/YangzeLiu/eval-instrument-disclosure) · ★ 0 |
| [**DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?**](https://arxiv.org/abs/2611.04228)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://dualworld.netlify.app/) |
| [**Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?**](https://arxiv.org/abs/2611.04203)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**OperAItor: An Agentic Framework for Fault-Tolerant Operation of Chemical Processes**](https://arxiv.org/abs/2611.05179)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents**](https://arxiv.org/abs/2611.04894)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**$\tau$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems**](https://arxiv.org/abs/2611.04459)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/nbharaths/tau-rec) · ★ 5 |
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
| [**SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents**](https://arxiv.org/abs/2611.02797)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/theseus-labs-rsi/SelfImprove-Bench) · ★ 5 |
| [**GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation**](https://arxiv.org/abs/2611.02698)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets**](https://arxiv.org/abs/2611.02484)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction**](https://arxiv.org/abs/2611.03223)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**WebHarbor: Docking Real Websites for Evolving GUI Agent Environments**](https://arxiv.org/abs/2611.03634)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/aiming-lab/WebHarbor) · ★ 64 |
| [**DiabAgent: Toward Agentic Physiological Control**](https://arxiv.org/abs/2611.03601)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Four Bridges: Measuring Deception Propensity in a Multi-Agent Game**](https://arxiv.org/abs/2611.03600)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Top-$k$ Retrieval Leaves Memory Value Undetermined**](https://arxiv.org/abs/2611.03289)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures**](https://arxiv.org/abs/2611.02826)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/rxnminer/RxnMiner) · ★ 5 |
| [**Predictive Safety Guardrails Do Not Always Make LLM Agents Safer**](https://arxiv.org/abs/2611.02815)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings**](https://arxiv.org/abs/2611.02659)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/gNucleus-AI/freecad-validator) · ★ 22 |
| [**Measuring AI Agents as Teammates with Collaborative Intelligence**](https://arxiv.org/abs/2611.02633)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://zou-group.github.io/collaborative-intelligence) |
| [**EEFA: A Framework for the Ethical Evaluation of AI Agents**](https://arxiv.org/abs/2611.02561)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MAGAR: Multimodal Agents for GUI-Based 3D Mechanical Assembly and Minimal Rework**](https://arxiv.org/abs/2611.02472)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents**](https://arxiv.org/abs/2611.02319)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study**](https://arxiv.org/abs/2611.03555)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL**](https://arxiv.org/abs/2611.03551)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Can Coding Agents Sustain Continual Evolution without Forgetting?**](https://arxiv.org/abs/2611.03219)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/THU-Agent/continual-harness-evolution) · ★ 4 |
| [**Beyond Accuracy: How Quantization Affects Coding Agents**](https://arxiv.org/abs/2611.02368)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MemShift: Separating Detection from Repair in LLM-Derived Personal Memory**](https://arxiv.org/abs/2611.02338)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/zichuanxu/memshift) · ★ 0 |
| [**VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably**](https://arxiv.org/abs/2611.03575)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**ACTOR: Action-Centered Temporal Organization for Literary Role-Playing Agents**](https://arxiv.org/abs/2611.03184)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/SilentStar233/ACTOR) · ★ 5 |
| [**What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory**](https://arxiv.org/abs/2611.03930)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://chihhsuan-yang.github.io/AAMAS2027-ConditionalMemory/) |
| [**Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain**](https://arxiv.org/abs/2611.03853)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions**](https://arxiv.org/abs/2611.03765)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost**](https://arxiv.org/abs/2611.03852)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents**](https://arxiv.org/abs/2611.03754)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use**](https://arxiv.org/abs/2611.03982)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [Project](https://geshijoker.github.io/slate/) |
| [**From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents**](https://arxiv.org/abs/2611.01527)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging**](https://arxiv.org/abs/2611.01449)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**LegoEnv: Self-Evolving Agentic Environments via Modular Recombination**](https://arxiv.org/abs/2611.01834)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks**](https://arxiv.org/abs/2611.01728)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**TriPhysBench: Evaluating Physical Intelligence for Embodied Agents**](https://arxiv.org/abs/2611.01934)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Delivered, Not Used: Evaluating Agent Memory at Its Point of Use**](https://arxiv.org/abs/2611.01718)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**Just-in-Time Skill Retrieval via Long-Horizon State Tracking**](https://arxiv.org/abs/2611.01701)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | — |
| [**MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents**](https://arxiv.org/abs/2611.01700)<br><sub>arXiv</sub> | <nobr>2026-11</nobr> | 0 | [GitHub](https://github.com/Kirito14IT/MemHarmBench) · ★ 3 |
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
| [**Decentralized Multi-Agent Coordination and Communication in Shared Codebases**](https://arxiv.org/abs/2611.00314)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://lingyunxiao18.github.io/ParallACT/) |
| [**Fidelity Collapses with Table Size, Not Turn Count: Delivery Architecture in a Deployed Tool-Using Agent**](https://arxiv.org/abs/2611.00442)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When AI Agents Act on Our Behalf: A Taxonomy of Human-Agent Interaction Failure**](https://arxiv.org/abs/2611.00291)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Real Computation or Merely Naming? A Pre-Registered Mechanism Audit of 25 Cognitive-Architecture Modules in an LLM-Based Agent System**](https://arxiv.org/abs/2610.41604)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Cross-Interface Authorization for AI Computer-Use Agents**](https://arxiv.org/abs/2610.41397)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Operon-S1: a fast decision controller for long-horizon biomedical agents**](https://arxiv.org/abs/2610.41350)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
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
| [**DynaRev: Benchmarking Web Agents under Dynamic Goal Revision**](https://arxiv.org/abs/2610.40133)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/zsq259/DynaRev) · ★ 0 |
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
| [**ReplayRCA: Measuring Post-hoc Diagnosis and Live Oversight of Agent Failures by Counterfactual Replay**](https://arxiv.org/abs/2610.41025)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/jeremy1392/RCAreplay) · ★ 0 |
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
| [**Gym-Anything for Robotics: Scaling physical simulations with digital agents**](https://arxiv.org/abs/2610.40565)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://gym-anything.github.io/robotics) |
| [**Practical Assessment of Agentic Systems in Acoustics**](https://arxiv.org/abs/2610.39685)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy**](https://arxiv.org/abs/2610.39532)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering**](https://arxiv.org/abs/2610.39468)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Clean Sheets and Checkpoints: Evidence Complexity for Certifying Sequential Agent Risk**](https://arxiv.org/abs/2610.39124)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**HERA: Assessing an Autonomous Agent for Quantum Device Measurement**](https://arxiv.org/abs/2610.39074)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/sharpelab/hera-paper-data) · ★ 0 |
| [**HALO: Human-Grounded Granular Evaluation of Proactive Agents**](https://arxiv.org/abs/2610.39086)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers**](https://arxiv.org/abs/2610.39234)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Lzzzzzzzzzzy/AgentHeal) · ★ 2 |
| [**Training LLM Agents to Automate LLM Post-Training with RSI-Dojo**](https://arxiv.org/abs/2611.03698)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Aligning Autoresearch: Co-Improvement between Agents and Humans**](https://arxiv.org/abs/2610.38882)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Beyond fabrication: Misattributed numbers in papers written by AI research agents**](https://arxiv.org/abs/2610.38691)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/mos3b-faqeeh/agent-integrity-analysis) · ★ 0 |
| [**An Alignment Benchmark for Enterprise Agents on Era by Eon**](https://arxiv.org/abs/2610.38544)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents**](https://arxiv.org/abs/2610.38392)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**DecompGym: Benchmarking LLM Agents on Designing Decomposition Algorithms**](https://arxiv.org/abs/2610.38175)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/SIKAI-C/DecompGym) · ★ 2 |
| [**SkillCT: A Multidimensional Benchmark and Execution-Free Baseline for Agent Skill Assessment**](https://arxiv.org/abs/2610.38147)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0**](https://arxiv.org/abs/2610.38617)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/snyk-labs/snyk-vulnbench) · ★ 8 |
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
| [**OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents**](https://arxiv.org/abs/2610.37081)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations**](https://arxiv.org/abs/2610.36980)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents**](https://arxiv.org/abs/2610.36878)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments**](https://arxiv.org/abs/2610.36484)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/kiante-fernandez/CogArena) · ★ 3 |
| [**FeatureArc: Benchmarking Coding Agents on Evolving Features**](https://arxiv.org/abs/2610.37434)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements**](https://arxiv.org/abs/2610.36584)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization**](https://arxiv.org/abs/2610.36553)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Agentic Backdoors via Pretraining Poisoning**](https://arxiv.org/abs/2610.37741)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/safety-research/agentic-backdoor) · ★ 14 |
| [**Benchmarking Task Takeover Across Agent Handoffs**](https://arxiv.org/abs/2610.36523)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces**](https://arxiv.org/abs/2610.37255)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/2020-qqtcg/HRP) · ★ 1 |
| [**SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World**](https://arxiv.org/abs/2610.37919)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**FilingLoop: Evaluating and Evolving LLM Agents for Corporate Disclosure Review and Revision**](https://arxiv.org/abs/2610.37905)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Evaluating and improving AI agents for sequencing protocol understanding**](https://arxiv.org/abs/2610.37851)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening**](https://arxiv.org/abs/2610.37849)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis**](https://arxiv.org/abs/2610.37830)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs**](https://arxiv.org/abs/2610.37809)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**WebAnything: From the Wild Web to Scalable Agent Environments**](https://arxiv.org/abs/2610.37786)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/china-qijizhifeng/Web-Anything) · ★ 7 |
| [**Scan Before You Install: Detecting and Mitigating Local and Composite Vulnerabilities in Skills**](https://arxiv.org/abs/2610.37901)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
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
| [**Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors**](https://arxiv.org/abs/2610.36544)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents**](https://arxiv.org/abs/2610.36471)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://method-notes.github.io/ReCoF/) |
| [**Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure**](https://arxiv.org/abs/2610.36453)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation**](https://arxiv.org/abs/2610.36435)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents**](https://arxiv.org/abs/2610.37567)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
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
| [**Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy**](https://arxiv.org/abs/2610.35832)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://internrobotics.github.io/EBench-Astra-Tech-Report/) |
| [**SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills**](https://arxiv.org/abs/2610.35215)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Tasselszcx/SkillLifeBench) · ★ 1 |
| [**How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation**](https://arxiv.org/abs/2610.34938)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents**](https://arxiv.org/abs/2610.34763)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Quantifying Claim Smoothing by LLM Research Agents**](https://arxiv.org/abs/2610.35793)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/tiasa2/SmoothScore) · ★ 0 |
| [**iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents**](https://arxiv.org/abs/2610.34735)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When Retrieval Is Not Enough: Obsolete Facts in Agent Memory**](https://arxiv.org/abs/2610.36308)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Agent or Human? Detecting Commits by AI Coding Agents in the Absence of Authorship Signatures**](https://arxiv.org/abs/2610.36229)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Replication or Corroboration? An Axiomatic Framework for Evidential Dependence in Multi-Agent Debate**](https://arxiv.org/abs/2610.36151)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol**](https://arxiv.org/abs/2610.36108)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling**](https://arxiv.org/abs/2610.36015)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix**](https://arxiv.org/abs/2610.35987)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Generation and Verification: Human-Agent Collaboration for Safety-Critical Automotive Software Engineering**](https://arxiv.org/abs/2610.35982)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity**](https://arxiv.org/abs/2610.35980)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**A Unified Arena for LLM Agents across Diverse Eurogame**](https://arxiv.org/abs/2610.35773)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgenticCity-Bench: Longitudinal Multimodal Observations of Urban Dynamics with Agentic Reasoning**](https://arxiv.org/abs/2610.35293)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://anonymous.4open.science/r/AgenticCity-Bench) |
| [**Proof-of-Agentness: Towards Verifying Agents on the Web**](https://arxiv.org/abs/2610.35288)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**LongSearchEval: Evaluating Long-Horizon Web Search Capabilities of Large Language Models via a Trajectory-Aware Agent Framework with Failure-Node Localization**](https://arxiv.org/abs/2610.35150)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models**](https://arxiv.org/abs/2610.35138)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://codesignbench.github.io/) |
| [**Collective Emergent Alignment: Measuring and Amplifying Interaction-Induced Reasoning Alignment in Multi-Agent LLMs**](https://arxiv.org/abs/2610.34836)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition**](https://arxiv.org/abs/2610.34777)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation**](https://arxiv.org/abs/2610.35541)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Hidden Costs of Forgetting: A Study of Trajectory Deletion in Software Engineering Agents**](https://arxiv.org/abs/2610.35496)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**V$^3$AST-Bench: Verifiable, Valid, and Versatile Safety Evaluation for Coding Agents**](https://arxiv.org/abs/2610.35188)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Alibaba-AAIG/VAST-Bench) · ★ 7 |
| [**CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems**](https://arxiv.org/abs/2610.35082)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**NumTrace: Auditing the Number Provenance of Financial Analyst Agents**](https://arxiv.org/abs/2610.34887)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG**](https://arxiv.org/abs/2610.34872)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/aimalrehman92/conformal-rag-agentic) · ★ 0 |
| [**Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents**](https://arxiv.org/abs/2610.34817)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Babysitting AI Agents: A User-Centered Taxonomy and Study of Agentic Delegation Failures**](https://arxiv.org/abs/2610.34748)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RobotAgentBench: Towards Open-world Robot Autonomy**](https://arxiv.org/abs/2610.34649)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://aetherlabsai.github.io/RobotAgentBench/) |
| [**From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis**](https://arxiv.org/abs/2610.35054)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Semantic Atoms for Scalable Text Analysis in Data Analytics in the Era of LLM-Based Agents**](https://arxiv.org/abs/2610.34860)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams**](https://arxiv.org/abs/2610.34790)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Rethinking Verification in Agent Harnesses**](https://arxiv.org/abs/2610.34577)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents**](https://arxiv.org/abs/2610.34185)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentProofBench: Benchmarking Reusable Verifiers for Web Agents**](https://arxiv.org/abs/2610.34634)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments**](https://arxiv.org/abs/2610.34535)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents**](https://arxiv.org/abs/2610.33956)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [Project](https://haoyu-zhao.github.io/CLE/index.html) |
| [**The Coordination Tax and the Heterogeneity Dividend: Break-Even Conditions for Multi-Agent LLM Pipelines**](https://arxiv.org/abs/2610.37700)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents**](https://arxiv.org/abs/2610.34491)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CTXAgent - Self-Controlled Context Management of LLM Agents**](https://arxiv.org/abs/2610.34425)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents**](https://arxiv.org/abs/2610.34298)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents**](https://arxiv.org/abs/2610.34167)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/hjj194/sabench-artifact) · ★ 2 |
| [**LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards**](https://arxiv.org/abs/2610.34542)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**The Price of Scale in Proactive Memory Recall**](https://arxiv.org/abs/2610.34507)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/RiverChenStillCompiling/price-of-scale) · ★ 0 |
| [**ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?**](https://arxiv.org/abs/2610.34386)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Outcome-Aware Agents: When Does Causal Structure Help a Forward Model Foresee the Consequences of Actions?**](https://arxiv.org/abs/2610.34385)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | — | [GitHub](https://github.com/mplusm/AC-LSCM-Outcome-Aware-Research-Paper) · ★ 0 |
| [**AndroidFlux: Evaluating and Reward Modeling Failure Recovery Capabilities in Mobile Use Multimodal Agents**](https://arxiv.org/abs/2610.34384)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents**](https://arxiv.org/abs/2610.34365)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names**](https://arxiv.org/abs/2610.34253)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**$\Delta\tau$-Bench: Pushing Agents Toward a Moving Capability**](https://arxiv.org/abs/2610.34238)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Memory Tax: Dissecting the Net Value of Agent Memory**](https://arxiv.org/abs/2610.34073)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://hexuan21.github.io/MemoryTax/) |
| [**How Do Small Coding Agents Use Code Graphs and Embeddings?**](https://arxiv.org/abs/2610.33958)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**LOLPlay: Benchmarking Real-Time Visual Agents in League of Legends**](https://arxiv.org/abs/2611.03685)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players**](https://arxiv.org/abs/2610.33845)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/MCG-NJU/AutoTavern) · ★ 257 |
| [**PACE: Research Proving Agent for Adaptive Conjecture Exploration**](https://arxiv.org/abs/2610.33690)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SkillShift-Bench: Benchmarking Skill Learning under Environment Evolution for Web Agents**](https://arxiv.org/abs/2610.33528)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://skillshift-bench.github.io/) |
| [**Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing**](https://arxiv.org/abs/2610.33636)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RSI Arena: Towards Recursive Self-Improvement with Human Feedback**](https://arxiv.org/abs/2610.33624)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://rsiarena.org) |
| [**ReGE: Stronger Agents through Experience Synthesis**](https://arxiv.org/abs/2610.33861)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**FraudSociety: A Generative Agent-Based Society for the Financial-Fraud Economy**](https://arxiv.org/abs/2610.33536)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM Memory Misalignment**](https://arxiv.org/abs/2610.33432)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?**](https://arxiv.org/abs/2610.33375)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Memory or a Clock? Auditing a Memory Advantage in XLand-MiniGrid with Seeds, Maps and Evaluation Noise Apart**](https://arxiv.org/abs/2610.33816)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Effiani-Core/memory-or-clock) · ★ 0 |
| [**Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation**](https://arxiv.org/abs/2610.33728)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ProbeID: Verifying MCP Tool Identity for LLM Agents under Registry Drift**](https://arxiv.org/abs/2610.33633)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Can Agentic Code Review Catch Vulnerabilities Before They Are Merged?**](https://arxiv.org/abs/2610.33509)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/secprbench/secprbench) · ★ 4 |
| [**Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination**](https://arxiv.org/abs/2610.33503)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Estimation of Propagated Risk in LLM-based Multi-Agent Systems**](https://arxiv.org/abs/2610.33282)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AOS-Bench: Can LLM Agents Manage Dynamic Workloads?**](https://arxiv.org/abs/2610.33178)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Responsibility Boundaries for Agentic Systems: A Comparative Evaluation of Probabilistic Agentic Programming**](https://arxiv.org/abs/2610.33312)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents**](https://arxiv.org/abs/2610.33201)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/anishh15/WhoWins) · ★ 1 |
| [**RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention**](https://arxiv.org/abs/2610.31372)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack**](https://arxiv.org/abs/2610.31404)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks**](https://arxiv.org/abs/2610.30635)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports**](https://arxiv.org/abs/2610.31158)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Multimedia-Semantic-Analytics-Lab/OmniDR-Bench) · ★ 14 |
| [**EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence**](https://arxiv.org/abs/2610.31650)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Simulated Control Evals**](https://arxiv.org/abs/2610.31593)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Can LLMs Improve Their Own Harness? A Controlled Study on ARC-AGI-3**](https://arxiv.org/abs/2610.30499)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**From Prose to Properties: Testing Research Claims with ARATest for Agent-Native Science**](https://arxiv.org/abs/2610.30495)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/ARA-Labs/aratest) · ★ 7 |
| [**Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences**](https://arxiv.org/abs/2610.30485)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**GAV: A scientific experimentation environment for PDE agents**](https://arxiv.org/abs/2610.30292)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/PotatoJnny/PDE-GAV) · ★ 6 |
| [**Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents**](https://arxiv.org/abs/2610.29812)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/saqlain2204/real-pmids-wrong-papers) · ★ 3 |
| [**PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents**](https://arxiv.org/abs/2610.29467)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/ZhongWishing/PreCoMem) · ★ 0 |
| [**GenXR-Bench: Benchmarking Coding Agents for Interactive XR Development**](https://arxiv.org/abs/2610.29014)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/whuang37/genxr-bench) · ★ 0 |
| [**Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research**](https://arxiv.org/abs/2610.30113)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents**](https://arxiv.org/abs/2610.29249)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval**](https://arxiv.org/abs/2610.30533)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards**](https://arxiv.org/abs/2610.28989)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?**](https://arxiv.org/abs/2610.27735)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents**](https://arxiv.org/abs/2610.27645)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/xu-hu-2002/CUA-Recovery) · ★ 2 |
| [**DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents**](https://arxiv.org/abs/2610.27581)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/lyx-researcher/DuplexLedger) · ★ 5 |
| [**Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment**](https://arxiv.org/abs/2610.27548)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/PEACH-Research-Lab/AuthorizationBench) · ★ 3 |
| [**MemDev-Bench: Does Memory Help Code Agents?Benchmarking Memory Systems over Real Repository Histories**](https://arxiv.org/abs/2610.27524)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Recoverability and Verifier Strength: Two Measured Preconditions for Unattended Agent Self-Improvement**](https://arxiv.org/abs/2610.27465)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents**](https://arxiv.org/abs/2610.28425)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims**](https://arxiv.org/abs/2610.27610)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets**](https://arxiv.org/abs/2610.28787)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents**](https://arxiv.org/abs/2610.28381)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents**](https://arxiv.org/abs/2610.28679)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems**](https://arxiv.org/abs/2610.27046)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/cmu-l3/reuF2F) · ★ 25 |
| [**LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents**](https://arxiv.org/abs/2610.27205)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**When the harness decides success: state that cannot be re-observed**](https://arxiv.org/abs/2610.26632)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/raimondasl/persistgym) · ★ 0 |
| [**VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement**](https://arxiv.org/abs/2610.26342)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | [GitHub](https://github.com/D2I-ai/VibeTraining-Bench) · ★ 6 |
| [**Reliable Before Profitable: QuantHarness for Governing Financial Strategy Development with LLM Agents**](https://arxiv.org/abs/2610.26101)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows**](https://arxiv.org/abs/2610.25954)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**When Should AI Chime In? Benchmarking Timely Contribution of Proactive Agents in Multi-Party Chat**](https://arxiv.org/abs/2610.25896)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Are Self-Evolving Agents Continual Learners?**](https://arxiv.org/abs/2610.25858)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development**](https://arxiv.org/abs/2610.26826)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments**](https://arxiv.org/abs/2610.25950)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents**](https://arxiv.org/abs/2610.27295)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**What Can't Jev Decide? Probing the Limits of One-Pass Decision Models**](https://arxiv.org/abs/2610.24929)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**BrandEval: A Two-Track Multi-Agent Benchmark for Risk-Sensitive LLM Crisis Communication**](https://arxiv.org/abs/2610.25208)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/htgan-ai/BrandEval) · ★ 1 |
| [**MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data**](https://arxiv.org/abs/2610.25373)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks**](https://arxiv.org/abs/2610.25069)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Edwin0080/Auto-MD-bench) · ★ 2 |
| [**MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity**](https://arxiv.org/abs/2610.25127)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Who Convinced Whom? Tracing How LLMs Change Their Minds in Multi-Agent Systems**](https://arxiv.org/abs/2610.35930)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference**](https://arxiv.org/abs/2610.24611)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners**](https://arxiv.org/abs/2610.24087)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/NineAbyss/OR-License) · ★ 147 |
| [**WebCoder: Scaling General Frontend Development with Artifact-Grounded Agentic Reinforcement Learning**](https://arxiv.org/abs/2610.23104)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents**](https://arxiv.org/abs/2610.22987)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios**](https://arxiv.org/abs/2610.22869)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas**](https://arxiv.org/abs/2610.22990)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 2 | [GitHub](https://github.com/MatrAIx-ai/PersonaCUABench) · ★ 2 |
| [**Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them**](https://arxiv.org/abs/2610.22984)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets**](https://arxiv.org/abs/2610.21098)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/zichuanxu/tool-bottleneck-bench) · ★ 0 |
| [**Harness-Delta Attribution: Dissecting Gains From Harness Evolution**](https://arxiv.org/abs/2610.22466)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems**](https://arxiv.org/abs/2610.22511)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/Lexsi-Labs/AuditKIT) · ★ 19 |
| [**From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research**](https://arxiv.org/abs/2610.21767)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files**](https://arxiv.org/abs/2610.21073)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents**](https://arxiv.org/abs/2610.20344)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**SEAR: Self-Evolving Agentic Robotics**](https://arxiv.org/abs/2610.18792)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 5 | — |
| [**Lessons from Luck: Do LLM-Written Lessons Carry Chance into an Agent's Next Decision?**](https://arxiv.org/abs/2610.33029)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Exposure Is Not Commitment: Double-Stratified Evaluation of Latent Monitors for Tool-Using Agents**](https://arxiv.org/abs/2610.37679)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/rishabhsinha17/latent-state-auditing) · ★ 0 |
| [**Recursive Semantic Divergence for LLM Agent Consistency**](https://arxiv.org/abs/2610.33012)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [GitHub](https://github.com/AgentConsistency/RSD-agent-consistency) · ★ 0 |
| [**When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems**](https://arxiv.org/abs/2610.33011)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | [Project](https://agent-pact-deception.github.io/) |
| [**Agent Plasticity: Measuring Self-Improvement Through Experience**](https://arxiv.org/abs/2610.08902)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 3 | — |
| [**GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks**](https://arxiv.org/abs/2610.09112)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents**](https://arxiv.org/abs/2610.05140)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Complex Agents, Shallow Tests: Demystifying and Enhancing Test Adequacy of Agent Harness in the Wild**](https://arxiv.org/abs/2610.04921)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Probe the Harness: Setup Checks for Stale-Data RL Comparisons in Language Models**](https://arxiv.org/abs/2610.02911)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models**](https://arxiv.org/abs/2610.03356)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Safety Must Survive Self-Improvement: Why Failures Persist and How Agents Recover**](https://arxiv.org/abs/2610.01073)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Auditing Web Agent Evaluation on WebArena-Lite: Human Review of Outcomes and Trajectories**](https://arxiv.org/abs/2610.01491)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 0 | — |
| [**Harnessing LLMs as Agents: What Does It Cost?**](https://arxiv.org/abs/2610.02488)<br><sub>arXiv</sub> | <nobr>2026-10</nobr> | 1 | — |
| [**Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training**](https://arxiv.org/abs/2609.40111)<br><sub>arXiv</sub> | <nobr>2026-09</nobr> | 2 | — |
| [**CompMat-Bench: Benchmarking AI Agents for Computational Materials Science**](https://arxiv.org/abs/2610.00636)<br><sub>arXiv</sub> | <nobr>2026-09</nobr> | 0 | — |
| [**EurekaBench: Measuring Agentic Ability to Discover New Scientific Insights**](https://arxiv.org/abs/2610.00492)<br><sub>arXiv</sub> | <nobr>2026-09</nobr> | 1 | — |
| [**Harness Evolution as Learning: Approximation, Generalization, and Optimization Limits of Self-Improving Personal Agents**](https://arxiv.org/abs/2609.36892)<br><sub>arXiv</sub> | <nobr>2026-09</nobr> | 1 | — |
| [**LLM Agents Can Easily Tamper With Their Own Traces**](https://arxiv.org/abs/2609.30266)<br><sub>arXiv</sub> | <nobr>2026-0