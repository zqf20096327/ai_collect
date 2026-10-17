# Awesome Agent Memory

A curated taxonomy of **agent memory systems**, organized along four axes: (1) memory system architectures — from flat sequential context, to structural topological graphs/trees, to multi-paradigm hybrid containers; (2) reference baselines for comparison; (3) benchmarks for evaluation; and (4) surveys on agent memory.

## 📣 Get Involved

- 📊 **Looking for a testbed to evaluate agent memory systems?** See our companion repo [OpenDataBox/MemoryData](https://github.com/OpenDataBox/MemoryData) — an integrated platform of memory systems and datasets.
- 📌 **Missing a paper, method, or benchmark?** [Open an issue](https://github.com/OpenDataBox/awesome-agent-memory/issues/new) to request it.
- 🤝 **Want to contribute directly?** [Submit a Pull Request](https://github.com/OpenDataBox/awesome-agent-memory/compare) — community PRs are warmly welcomed!

![](AgentMemory.png)

## Table of Contents

- [1. Memory Systems and Methods](#1-memory-systems-and-methods)
  - [1.1 Sequential Memory Systems](#11-sequential-memory-systems)
    - [1.1.1 Discrete Textual Memory](#111-discrete-textual-memory)
    - [1.1.2 Parameter and Latent Memory](#112-parameter-and-latent-memory)
  - [1.2 Structured Topological Memory Systems](#12-structured-topological-memory-systems)
    - [1.2.1 Graph-Based Memory](#121-graph-based-memory)
    - [1.2.2 Hierarchical Memory](#122-hierarchical-memory)
  - [1.3 Composite Memory Systems](#13-composite-memory-systems)
  - [1.4 Baselines and Supporting Methods](#14-baselines-and-supporting-methods)
- [2. Benchmarks and Datasets](#2-benchmarks-and-datasets)
  - [2.1 Effectiveness Evaluation](#21-effectiveness-evaluation)
  - [2.2 Retrieval Evaluation](#22-retrieval-evaluation)
  - [2.3 Robustness Evaluation](#23-robustness-evaluation)
  - [2.4 Efficiency Evaluation](#24-efficiency-evaluation)
- [3. Surveys, Tutorials, and Position Papers](#3-surveys-tutorials-and-position-papers)
- [4. Frameworks, Products, and Resources](#4-frameworks-products-and-resources)
- [Citation](#citation)

## 1. Memory Systems and Methods

### 1.1 Sequential Memory Systems

#### 1.1.1 Discrete Textual Memory

Memory represented as a flat sequence, textual summary, note, trajectory, or experience record without an explicit graph or tree topology.

1. **Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval**\
   Yingyi Zhang, Junyi Li, Wenlin Zhang, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2603.09250)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization**\
   Zeyuan Liu, Jeonghye Kim, Xufang Luo, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2602.23008)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Distilling Feedback into Memory-as-a-Tool**\
   Víctor Gallego. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2601.05960)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context**\
   Xiaoyuan Liu, Tian Liang, Dongyang Ma, et al. *ICLR 2026*. [[Paper](https://openreview.net/forum?id=GymjF88oGQ)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Real-Time Procedural Learning From Experience for AI Agents**\
   Dasheng Bi, Yubin Hu, Mohammed N. Nasir. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2511.22074)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory**\
   Siru Ouyang, Jun Yan, I-Hung Hsu, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2509.25140)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent**\
   Hongli Yu, Tinghong Chen, Jiangtao Feng, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2507.02259)] [[Code](https://github.com/BytedTsinghua-SIA/MemAgent)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents**\
   Qirui Mi, Zhijian Ma, Mengyue Yang, et al. *ICML 2026*. [[Paper](https://arxiv.org/abs/2602.01869)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-RL_based-orange)

1. **EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle**\
   Rong Wu, Xiaoman Wang, Jianbiao Mei, et al. *ICML 2026*. [[Paper](https://arxiv.org/abs/2510.16079)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **History-Aware Reasoning for GUI Agents**\
   Ziwei Wang, Leyang Yang, Xiaoxuan Tang, et al. *AAAI 2026*. [[Paper](https://arxiv.org/abs/2511.09127)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning**\
   Juyuan Wang, Rongchen Zhao, Wei Wei, et al. *AAAI 2026*. [[Paper](https://arxiv.org/abs/2508.10419)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **MemSearcher: Training LLMs to Reason, Search and Manage Memory via End-to-End Reinforcement Learning**\
   Qianhao Yuan, Jie Lou, Zichao Li, et al. *ACL 2026*. [[Paper](https://arxiv.org/abs/2511.02805)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **AutoMem: Automated Learning of Memory as a Cognitive Skill**\
   Shengguang Wu, Hao Zhu, Yuhui Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2607.01224)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management**\
   Guangyi Liu, Gao Wu, Congxiao Liu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.19926)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents**\
   Jiaqi Chen, Yongqin Zeng, Shaoshen Chen, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.18406)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **TokenPilot: Cache-Efficient Context Management for LLM Agents**\
   Buqiang Xu, Zirui Xue, Dianmou Chen, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.17016)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **HiMPO: Hindsight-Informed Memory Policy Optimization for Less-Entangled Credit in Long-Horizon Agents**\
   Jiangze Yan, Yi Shen, Wenjing Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.16285)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-RL_based-orange)

1. **T-Mem: Memory That Anticipates, Not Archives**\
   Weidong Guo, Dakai Wang, Zixuan Wang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.15405)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemRefine: LLM-Guided Compression for Long-Term Agent Memory**\
   Minjae Kim, Jinheon Baek, Soyeong Jeong, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.13177)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Multi-Turn Reasoning When Context Arrives in Pieces: Scalable Sharding and Memory-Augmented RL**\
   Shu Tong Luo, Wenqin Liu, Rui Liu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.12941)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-RL_based-orange)

1. **PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents**\
   Ripon Chandra Malo, Tong Qiu. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.12329)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory**\
   Suozhao Ji, Baodong Wu, Zehao Wang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.10677)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Rosetta Memory: Adaptive Memory for Cross-LLM Agents**\
   Hao Yang, Shiqi Shen, Haoxuan Li, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.07711)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory**\
   Ziming Wang. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.06240)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **EMBER: Efficient Memory via Budgeted Evidence Retention for Long-Horizon Agents**\
   Yilong Li, Suman Banerjee, Tong Che. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.05894)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Forgetting-orange)

1. **RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation**\
   Nikodem Tomczak. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.04628)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Training-Free Lexical-Dense Fusion for Conversational-Memory Retrieval**\
   Christian Lysenstøen. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.04194)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **DMF: A Deterministic Memory Framework for Conversational AI Agents**\
   Matteo Stabile, Enrico Zimuel. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.03463)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Forgetting-orange)

1. **InfoMem: Training Long-Context Memory Agents with Answer-Conditioned Information Gain**\
   Tiancheng Han, Yong Li, Wuzhou Yu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.03329)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-RL_based-orange)

1. **MemTrain: Self-Supervised Context Memory Training**\
   Ziheng Li, Xingrun Xing, Haoqing Wang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.03197)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Memory Retrieval for Changing Preferences**\
   Yuehan Qin, Li Li, Linxin Song, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.02976)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Joint Agent Memory and Exploration Learning via Novelty Signals**\
   Shizuo Tian, Xiaohong Weng, Rui Kong, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.01528)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemPro: Agentic Memory Systems as Evolvable Programs**\
   Qingshan Liu, Guoqing Wang, Wen Wu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.00619)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **CASCADE: Case-Based Continual Adaptation for Large Language Models During Deployment**\
   Siyuan Guo, Yali Du, Hechang Chen, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.06702)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval**\
   Chunyu Li, Mengyuan Zhang, Jingyi Kang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.06132)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Belief Memory: Agent Memory Under Partial Observability**\
   Junfeng Liao, Qizhou Wang, Jianing Zhu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.05583)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents**\
   Jiayi Chen, Yingcong Li, Guiling Wang. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.03312)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory**\
   Derong Xu, Shuochen Liu, Pengfei Luo, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.00702)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents**\
   Tianyu Hu, Weikai Lin, Weizhi Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.00356)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction**\
   Alex Petrov, Alexander Gusak, Denis Mukha, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.27906)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents**\
   Seyed Moein Abtahi, Rasa Rahnema, Hetkumar Patel, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.22085)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Gated Memory Policy**\
   Yihuai Gao, Jinyun Liu, Shuang Li, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.18933)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemSearch-o1: Empowering Large Language Models with Reasoning-Aligned Memory Growth in Agentic Search**\
   Sheng Zhang, Junyi Li, Yingyi Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.17265)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Trust Your Memory: Verifiable Control of Smart Homes through Reinforcement Learning with Multi-dimensional Rewards**\
   Kai-Yuan Guo, Jiang Wang, Renjie Zhao, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.10110)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Constraint-Aware Corrective Memory for Language-Based Drug Discovery Agents**\
   Maochen Sun, Youzhi Zhang, Gaofeng Meng. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.09308)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **MT-OSC: Path for LLMs that Get Lost in Multi-Turn Conversation**\
   Jyotika Singh, Fang Tu, Miguel Ballesteros, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.08782)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Artifacts as Memory Beyond the Agent Boundary**\
   John D. Martin, Fraser Mince, Esra'a Saleh, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.08756)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **TSUBASA: Improving Long-Horizon Personalization via Evolving Memory and Self-Learning with Context Distillation**\
   Xinliang Frederick Zhang, Lu Wang. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.07894)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Personalization-green)

1. **MemReader: From Passive to Active Extraction for Long-Term Agent Memory**\
   Jingyi Kang, Chunyu Li, Ding Chen, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.07877)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **LightThinker++: From Reasoning Compression to Memory Management**\
   Yuqi Zhu, Jintian Zhang, Zhenjie Wan, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.03679)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **SelRoute: Query-Type-Aware Routing for Long-Term Conversational Memory Retrieval**\
   Matthew McKee. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2604.02431)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **MemRerank: Preference Memory for Personalized Product Reranking**\
   Zhiyuan Peng, Xuyang Wu, Huaixiao Tou, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.29247)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Memento-Skills: Let Agents Design Agents**\
   Huichi Zhou, Siyuan Guo, Anjie Liu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.18743)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-RL_based-orange)

1. **SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory**\
   Varun Pratap Bhardwaj. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.14588)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation**\
   Sydney Lewis. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.13017)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Trajectory-Informed Memory Generation for Self-Improving Agent Systems**\
   Gaodan Fang, Vatche Isahagian, K. R. Jayaram, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.10600)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Retrieval-green)

1. **TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA**\
   Mengwei Yuan, Jianan Liu, Jing Yang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.09297)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Retrieval-green)

1. **MemSifter: Offloading LLM Memory Retrieval via Outcome-Driven Proxy Reasoning**\
   Jiejun Tan, Zhicheng Dou, Liancheng Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.03379)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **According to Me: Long-Term Personalized Referential Memory QA**\
   Jingbiao Mei, Jinghong Chen, Guangyu Yang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.01990)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **MemPO: Self-Memory Policy Optimization for Long-Horizon Agents**\
   Ruoran Li, Xinghua Zhang, Haiyang Yu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.00680)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Towards Autonomous Memory Agents**\
   Xinle Wu, Rui Zhang, Mustafa Anis Hussain, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.22406)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Structurally Aligned Subtask-Level Memory for Software Engineering Agents**\
   Kangning Shen, Jingyuan Zhang, Chenxi Sun, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.21611)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Hippocampus: An Efficient and Scalable Memory Module for Agentic AI**\
   Yi Li, Lianjie Cao, Faraz Ahmed, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.13594)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **Scene-Aware Memory Discrimination: Deciding Which Personal Knowledge Stays**\
   Yijie Zhong, Mengying Guo, Zewei Wang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.11607)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory**\
   Yongshi Ye, Hui Jiang, Feihu Jiang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.10652)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **AMEM4Rec: Leveraging Cross-User Similarity for Memory Evolution in Agentic LLM Recommenders**\
   Minh-Duc Nguyen, Hai-Dang Kieu, Dung D. Le. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.08837)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Learning to Continually Learn via Meta-learning Agentic Memory Designs**\
   Yiming Xiong, Shengran Hu, Jeff Clune. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.07755)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Learning to Share: Selective Memory for Efficient Parallel Agentic Systems**\
   Joseph Fioresi, Parth Parag Kulkarni, Ashmal Vayani, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.05965)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents**\
   Haozhen Zhang, Quanyu Long, Jianzhu Bao, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.02474)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback**\
   Yaolun Zhang, Yiran Wu, Yijiong Yu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.02369)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution**\
   Hongze Mi, Yibo Feng, WenJie Lu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.22528)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **MAGNET: Towards Adaptive GUI Agents with Memory-Driven Knowledge Evolution**\
   Libo Sun, Jiwen Zhang, Siyuan Wang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.19199)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **Dep-Search: Learning Dependency-Aware Reasoning Traces with Persistent Memory**\
   Yanming Liu, Xinyue Peng, Zixuan Yan, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.18771)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Clustering-driven Memory Compression for On-device Large Language Models**\
   Ondrej Bohdal, Pramit Saha, Umberto Michieli, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.17443)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Chain-of-Memory: Lightweight Memory Construction with Dynamic Evolution for LLM Agents**\
   Xiucheng Xu, Bingbing Xu, Xueyun Tian, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.14287)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **LLM-as-RNN: A Recurrent Language Model for Memory Updates and Sequence Prediction**\
   Yuxing Lu, J. Ben Tamo, Weichen Zhao, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.13352)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Grounding Agent Memory in Contextual Intent**\
   Ruozhen Yang, Yucheng Jiang, Yueqi Jiang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.10702)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management**\
   Weitao Ma, Xiaocheng Feng, Lei Huang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.08435)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **AtomMem : Learnable Dynamic Agentic Memory with Atomic Memory Operation**\
   Yupeng Huo, Yaxi Lu, Zhong Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.08323)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents**\
   Miao Su, Yucan Guo, Zhongni Hou, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.07468)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Active Context Compression: Autonomous Memory Management in LLM Agents**\
   Nikhil Verma. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.07190)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences**\
   Qihao Wang, Ziming Cheng, Shuo Zhang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.06789)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards**\
   Zhiyu Shen, Ziming Wu, Fuming Lai, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.05488)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning**\
   Yuyang Hu, Jiongnan Liu, Jiejun Tan, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04726)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Beyond Static Summarization: Proactive Memory Extraction for LLM Agents**\
   Chengyuan Yang, Zequn Sun, Wei Wei, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.04463)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory**\
   Shengtao Zhang, Jiaqian Wang, Ruiwen Zhou, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.03192)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **CodeMEM: AST-Guided Adaptive Memory for Repository-Level Iterative Code Generation**\
   Peiding Wang, Li Zhang, Fang Liu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.02868)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **SimpleMem: Efficient Lifelong Memory for LLM Agents**\
   Jiaqi Liu, Yaofeng Su, Peng Xia, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.02553)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents**\
   Namyoung Kim, Kai Tzu-iunn Ong, Yeonjun Hwang, et al. *EMNLP 2025*. [[Paper](https://arxiv.org/abs/2509.17459)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Pre-Storage Reasoning for Episodic Memory: Shifting Inference Burden to Memory for Personalized Dialogue**\
   Sangyeop Kim, Yohan Lee, Sanghwa Kim, et al. *EMNLP 2025*. [[Paper](https://arxiv.org/abs/2509.10852)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Contextual Experience Replay for Self-Improvement of Language Agents**\
   Yitao Liu, Chenglei Si, Karthik Narasimhan, et al. *ACL 2025*. [[Paper](https://arxiv.org/abs/2506.06698)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents**\
   Zhen Tan, Jun Yan, I-Hung Hsu, et al. *ACL 2025*. [[Paper](https://arxiv.org/abs/2503.08026)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Improving Factuality with Explicit Working Memory**\
   Mingda Chen, Yang Li, Karthik Padthe, et al. *ACL 2025*. [[Paper](https://arxiv.org/abs/2412.18069)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Agent Workflow Memory**\
   Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig. *ICML 2025*. [[Paper](https://arxiv.org/abs/2409.07429)] [[Code](https://github.com/zorazrw/agent-workflow-memory)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Prompt_based-orange)

1. **Human-inspired Episodic Memory for Infinite Context LLMs**\
   Zafeirios Fountas, Martin A Benfeghoul, Adnan Oomerjee, et al. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2407.09450)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Towards Lifelong Dialogue Agents via Timeline-based Memory Management**\
   Kai Tzu-iunn Ong, Namyoung Kim, Minju Gwak, et al. *NAACL 2025*. [[Paper](https://arxiv.org/abs/2406.10996)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Hello Again! LLM-powered Personalized Agent for Long-term Dialogue**\
   Hao Li, Chenghao Yang, An Zhang, et al. *NAACL 2025*. [[Paper](https://arxiv.org/abs/2406.05925)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations**\
   Nuo Chen, Hongguang Li, Juhua Huang, et al. *COLING 2025*. [[Paper](https://arxiv.org/abs/2402.11975)] [[Code](https://github.com/nuochenpku/COMEDY)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Compression-orange)

1. **Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models**\
   Qingyue Wang, Yanhe Fu, Yanan Cao, et al. *Neurocomputing 2025*. [[Paper](https://arxiv.org/abs/2308.15022)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Compression-orange)

1. **SCM: Enhancing Large Language Model with Self-Controlled Memory Framework**\
   Bing Wang, Xinnian Liang, Jian Yang, et al. *DASFAA 2025*. [[Paper](https://arxiv.org/abs/2304.13343)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Verbatim Chunks Beat Extracted Artifacts: A Controlled Ablation of Memory Representations for Long LLM Conversations**\
   Tao An. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2601.00821)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Memento 2: Learning by Stateful Reflective Memory**\
   Jun Wang. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.22716)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **MemR³: Memory Retrieval via Reflective Reasoning for LLM Agents**\
   Xingbo Du, Loka Li, Duzhen Zhang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.20237)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **ABBEL: Learning Natural-Language Belief States for Memory-Efficient Interaction**\
   Aly Lidayan, Jakob Bjorner, Satvik Golechha, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.20111)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents**\
   Yiming Du, Baojun Wang, Yifan Xiang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.20092)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution**\
   Zouying Cao, Jiaji Deng, Li Yu, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.10696)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **LightSearcher: Efficient DeepSearch via Experiential Memory**\
   Hengzhi Lan, Yue Yu, Li Qian, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.06653)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Solving Context Window Overflow in AI Agents**\
   Anton Bulle Labate, Valesca Moura de Sousa, Sandro Rama Fiorini, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.22729)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Goal-Directed Search Outperforms Goal-Agnostic Memory Compression in Long-Context Memory Tasks**\
   Yicong Zheng, Kevin L. McKee, Thomas Miconi, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.21726)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Improving Language Agents through BREW: Bootstrapping expeRientially-learned Environmental knoWledge**\
   Shashank Kirtania, Param Biyani, Priyanshu Gupta, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.20297)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Episodic Memory in Agentic Frameworks: Suggesting Next Tasks**\
   Sandro Rama Fiorini, Leonardo G. Azevedo, Raphael M. Thiago, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.17775)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **A Simple Yet Strong Baseline for Long-Term Conversational Memory of LLM Agents**\
   Sizhe Zhou, Jiawei Han. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.17208)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance**\
   Genglin Liu, Shijie Geng, Sha Li, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.12997)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Experience-Guided Adaptation of Inference-Time Reasoning Strategies**\
   Adam Stein, Matthew Trager, Benjamin Bowman, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.11519)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Smarter Together: Creating Agentic Communities of Practice through Shared Experiential Learning**\
   Valentin Tablan, Scott Taylor, Gabriel Hurtado, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.08301)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Efficient On-Device Agents via Adaptive Context Management**\
   Sanidhya Vijayvargiya, Rahul Lokesh. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.03728)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **Dynamic Affective Memory Management for Personalized LLM Agents**\
   Junfeng Lu, Yueyan Li. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.27418)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **AgentFold: Long-Horizon Web Agents with Proactive Context Management**\
   Rui Ye, Zhongwang Zhang, Kuan Li, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.24699)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks**\
   Yuxiang Zhang, Jiangming Shu, Ye Ma, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.12635)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Preference-Aware Memory Update for Long-Term LLM Agents**\
   Haoran Sun, Zekun Zhang, Shaoning Zeng. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.09720)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Enabling Personalized Long-term Interactions in LLM-based Agents through Persistent Memory and User Profiles**\
   Rebecca Westhäußer, Wolfgang Minker, Sebatian Zepf. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.07925)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Scaling LLM Multi-turn RL with End-to-end Summarization-based Context Management**\
   Miao Lu, Weiwei Sun, Weihua Du, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.06727)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Improving Code Localization with Repository Memory**\
   Boshi Wang, Weijian Xu, Yunsheng Li, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.01003)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **ACON: Optimizing Context Compression for Long-horizon LLM Agents**\
   Minki Kang, Wei-Ning Chen, Dongge Han, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.00615)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents**\
   Yaorui Shi, Yuxin Chen, Siyuan Wang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.23040)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization**\
   Xixi Wu, Kuan Li, Yida Zhao, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.13313)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory**\
   Matthew Ho, Chen Si, Zhaoxiang Feng, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.04439)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning**\
   Sikuan Yan, Xiufeng Yang, Zuchao Huang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.19828)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memory Framework**\
   Zeyu Zhang, Quanyu Dai, Rui Li, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.16629)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Memento: Fine-tuning LLM Agents without Fine-tuning LLMs**\
   Huichi Zhou, Yihang Chen, Siyuan Guo, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.16153)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **Semantic Anchoring in Agentic Memory: Leveraging Linguistic Structures for Persistent Conversational Context**\
   Maitreyi Chatterjee, Devansh Agarwal. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.12630)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Memp: Exploring Agent Procedural Memory**\
   Runnan Fang, Yuan Liang, Xiaobin Wang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.06433)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management**\
   Mo Li, L. H. Xu, Qitai Tan, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.04664)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **SWE-Exp: Experience-Driven Software Issue Resolution**\
   Silin Chen, Shaoxin Lin, Yuling Shi, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.23361)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Calling in LLM Agent Multi-Turn Conversations**\
   Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.21428)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving**\
   Xiangru Tang, Tianrui Qin, Tianhao Peng, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.06229)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents**\
   Qizheng Zhang, Michael Wornow, Gerry Wan, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2506.14852)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents**\
   Yiming Du, Bingbing Wang, Yang He, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.20231)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Task-Core Memory Management and Consolidation for Long-term Continual Learning**\
   Tianyu Huai, Jie Zhou, Yuxuan Cai, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.09952)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory**\
   Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.07952)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemInsight: Autonomous Memory Augmentation for LLM Agents**\
   Rana Salama, Jason Cai, Michelle Yuan, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.21760)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Memory-augmented Query Reconstruction for LLM-based Knowledge Graph Reasoning**\
   Mufan Xu, Gewen Liang, Kehai Chen, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.05193)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Interpersonal Memory Matters: A New Task for Proactive Dialogue Utilizing Conversational History**\
   Bowen Wu, Wenqing Wang, Haoran Li, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2503.05150)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **On Memory Construction and Retrieval for Personalized Conversational Agents**\
   Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.05589)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Wormhole Memory: A Rubik's Cube for Cross-Dialogue Retrieval**\
   Libo Wang. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.14846)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **"My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents**\
   Yuki Hou, Haruki Tamoto, Homei Miyashita. *CHI 2024 Extended Abstracts*. [[Paper](https://arxiv.org/abs/2404.00573)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **ExpeL: LLM Agents Are Experiential Learners**\
   Andrew Zhao, Daniel Huang, Quentin Xu, et al. *AAAI 2024*. [[Paper](https://arxiv.org/abs/2308.10144)] [[Code](https://github.com/LeapLabTHU/ExpeL)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Training_free-orange)

1. **MemoryBank: Enhancing Large Language Models with Long-Term Memory**\
   Wanjun Zhong, Lianghong Guo, Qiqi Gao, et al. *AAAI 2024*. [[Paper](https://arxiv.org/abs/2305.10250)] [[Code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Semantic-green)

1. **Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control**\
   Longtao Zheng, Rundong Wang, Xinrun Wang, Bo An. *ICLR 2024*. [[Paper](https://arxiv.org/abs/2306.07863)] [[Code](https://github.com/ltzheng/Synapse)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Self-evolving Agents with reflective and memory-augmented abilities**\
   Xuechen Liang, Yangfan He, Yinghui Xia, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.00872)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Generative Agents: Interactive Simulacra of Human Behavior**\
   Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, et al. *UIST 2023*. [[Paper](https://arxiv.org/abs/2304.03442)] [[Code](https://github.com/joonspk-research/generative_agents)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Reflection-yellowgreen)

1. **MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation**\
   Junru Lu, Siyu An, Mingbao Lin, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2308.08239)] [[Code](https://github.com/LuJunru/MemoChat)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-SFT-orange)

1. **RET-LLM: Towards a General Read-Write Memory for Large Language Models**\
   Ali Modarressi, Ayyoob Imani, Mohsen Fayyaz, Hinrich Schütze. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2305.14322)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Textual-blue) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Read_Write-orange)

[⬆️ top](#table-of-contents)

#### 1.1.2 Parameter and Latent Memory

Memory stored in model parameters, learned memory modules, hidden states, attention key-values, or other continuous latent representations.

1. **TokMem: One-Token Procedural Memory for Large Language Models**\
   Zijun Wu, Yongchang Hao, Lili Mou. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2510.00444)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents**\
   Zijian Zhou, Ao Qu, Zhaoxuan Wu, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2506.15841)] [[Code](https://github.com/MIT-MI/MEM1)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-RL_based-orange)

1. **User as Engram: Internalizing Per-User Memory as Local Parametric Edits**\
   Bojie Li. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.19172)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **Scaling Self-Evolving Agents via Parametric Memory**\
   Tao Ren, Weiyao Luo, Hui Yang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.04536)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories**\
   Ali Behrouz, Farnoosh Hashemi, Adel Javanmard, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.03979)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Do Language Models Need Sleep? Offline Recurrence for Improved Online Inference**\
   Sangyun Lee, Sean McLeish, Tom Goldstein, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.26099)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MeMo: Memory as a Model**\
   Ryan Wei Heng Quek, Sanghyuk Lee, Alfred Wei Lun Leong, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.15156)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **δ-mem: Efficient Online Memory for Large Language Models**\
   Jingdi Lei, Di Zhang, Junxian Li, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2605.12357)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent**\
   Yuri Kuratov, Matvey Kairov, Aydar Bulatov, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2603.13875)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Memory Caching: RNNs with Growing Memory**\
   Ali Behrouz, Zeman Li, Yuan Deng, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.24281)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **ParamMem: Augmenting Language Agents with Parametric Reflective Memory**\
   Tianjun Yao, Yongqiang Chen, Yujia Zheng, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.23320)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Tell Me What To Learn: Generalizing Neural Memory to be Controllable in Natural Language**\
   Max S. Bennett, Thomas P. Zollo, Richard Zemel. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.23201)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Field-Theoretic Memory for AI Agents: Continuous Dynamics for Context Preservation**\
   Subhadip Mitra. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.21220)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Forgetting-orange)

1. **Language Model Memory and Memory Models for Language**\
   Benjamin L. Badger. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.13466)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Learning to Forget Attention: Memory Consolidation for Adaptive Compute Reduction**\
   Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.12204)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Forgetting-orange)

1. **Towards Compressive and Scalable Recurrent Memory**\
   Yunchong Song, Jushi Kai, Liming Lu, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.11212)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **When to Memorize and When to Stop: Gated Recurrent Memory for Long-Context Reasoning**\
   Leheng Sheng, Yongtao Zhang, Wenchang Ma, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.10560)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling**\
   Ning Ding, Fangcheng Liu, Kyungrae Kim, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2602.03359)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics**\
   Tao Lin. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.16531)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models**\
   Xin Cheng, Rui Tian, Wangding Zeng, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.07372)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Fast-weight Product Key Memory**\
   Tianyu Zhao, Llion Jones. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2601.00671)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Nested Learning: The Illusion of Deep Learning Architectures**\
   Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, et al. *NeurIPS 2025*. [[Paper](https://arxiv.org/abs/2512.24695)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts**\
   Subhajit Chaudhury, Payel Das, Sarathkrishna Swaminathan, et al. *ACL 2025*. [[Paper](https://aclanthology.org/2025.acl-long.574/)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Ultra-Sparse Memory Network**\
   Zihao Huang, Qiyang Min, Hongzhi Huang, et al. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2411.12364)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Self-Updatable Large Language Models by Integrating Context into Model Parameters**\
   Yu Wang, Xinshuang Liu, Xiusi Chen, et al. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2410.00487)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation**\
   Hongjin Qian, Zheng Liu, Peitian Zhang, et al. *WWW 2025*. [[Paper](https://arxiv.org/abs/2409.05591)] [[Code](https://github.com/qhjqhj00/MemoRAG)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Hybrid-purple) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **MemLoRA: Distilling Expert Adapters for On-Device Memory Systems**\
   Massimo Bini, Ondrej Bohdal, Umberto Michieli, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2512.04763)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models**\
   Xinlei Yu, Chengming Xu, Guibin Zhang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2511.11007)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **Continual Learning via Sparse Memory Finetuning**\
   Jessy Lin, Luke Zettlemoyer, Gargi Ghosh, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.15103)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **Auto-scaling Continuous Memory for GUI Agent**\
   Wenyi Wu, Kun Zhou, Ruoxin Yuan, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.09038)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **Memory Retrieval and Consolidation in Large Language Models through Function Tokens**\
   Shaohua Zhang, Yuan Lin, Hang Li. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.08203)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Pretraining with hierarchical memories: separating long-tail and common knowledge**\
   Hadi Pouransari, David Grangier, C Thomas, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2510.02375)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MemGen: Weaving Generative Latent Memory for Self-Evolving Agents**\
   Guibin Zhang, Muxin Fu, Shuicheng Yan. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.24704)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation**\
   Hao Shi, Bin Xie, Yingfei Liu, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.19236)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models**\
   Jiaqi Cao, Jiarui Wang, Rubin Wei, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.09874)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MLP Memory: A Retriever-Pretrained Memory for Large Language Models**\
   Rubin Wei, Jiaqi Cao, Jiarui Wang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2508.01832)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Towards General Continuous Memory for Vision-Language Models**\
   Wenyi Wu, Zixuan Song, Kun Zhou, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2505.17670)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **Memorization and Knowledge Injection in Gated LLMs**\
   Xu Pan, Ely Hahami, Zechen Zhang, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2504.21239)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Echo: A Large Language Model with Temporal Episodic Memory**\
   WenTao Liu, Ruohua Zhang, Aimin Zhou, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.16090)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **R³Mem: Bridging Memory Retention and Retrieval via Reversible Compression**\
   Xiaoqiang Wang, Suyuchen Wang, Yun Zhu, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.15957)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **MoM: Linear Sequence Modeling with Mixture-of-Memories**\
   Jusen Du, Weigao Sun, Disen Lan, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.13685)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Consolidation-orange)

1. **LM2: Large Memory Models**\
   Jikun Kang, Wenqi Wu, Filippos Christianos, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.06049)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **M+: Extending MemoryLLM with Scalable Long-Term Memory**\
   Yu Wang, Dmitry Krotov, Yuanzhe Hu, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.00592)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Memory³: Language Modeling with Explicit Memory**\
   Hongkang Yang, Zehao Lin, Wenjin Wang, et al. *Journal of Machine Learning 2024*. [[Paper](https://arxiv.org/abs/2407.01178)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Hybrid-purple) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Explicit_Memory-purple)

1. **WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models**\
   Peng Wang, Zexi Li, Ningyu Zhang, et al. *NeurIPS 2024*. [[Paper](https://arxiv.org/abs/2405.14768)] [[Code](https://github.com/zjunlp/EasyEdit)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Parameter-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Model_Editing-orange)

1. **Online Adaptation of Language Models with a Memory of Amortized Contexts**\
   Jihoon Tack, Jaehyung Kim, Eric Mitchell, et al. *NeurIPS 2024*. [[Paper](https://arxiv.org/abs/2403.04317)] [[Code](https://github.com/jihoontack/MAC)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory**\
   Chaojun Xiao, Pengle Zhang, Xu Han, et al. *NeurIPS 2024*. [[Paper](https://arxiv.org/abs/2402.04617)] [[Code](https://github.com/thunlp/InfLLM)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Hybrid-purple) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Training_free-orange)

1. **MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding**\
   Bo He, Hengduo Li, Young Kyun Jang, et al. *CVPR 2024*. [[Paper](https://arxiv.org/abs/2404.05726)] [[Code](https://github.com/boheumd/MA-LMM)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multimodal-purple)

1. **Larimar: Large Language Models with Episodic Memory Control**\
   Payel Das, Subhajit Chaudhury, Elliot Nelson, et al. *ICML 2024*. [[Paper](https://arxiv.org/abs/2403.11901)] [[Code](https://github.com/IBM/larimar)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Model_Editing-orange)

1. **MEMORYLLM: Towards Self-Updatable Large Language Models**\
   Yu Wang, Yifan Gao, Xiusi Chen, et al. *ICML 2024*. [[Paper](https://arxiv.org/abs/2402.04624)] [[Code](https://github.com/wangyu-ustc/MemoryLLM)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Self_Updating-orange)

1. **Compressed Context Memory for Online Language Model Interaction**\
   Jang-Hyun Kim, Junyoung Yeom, Sangdoo Yun, Hyun Oh Song. *ICLR 2024*. [[Paper](https://arxiv.org/abs/2312.03414)] [[Code](https://github.com/snu-mllab/Context-Memory)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Compression-orange)

1. **Efficient Streaming Language Models with Attention Sinks**\
   Guangxuan Xiao, Yuandong Tian, Beidi Chen, et al. *ICLR 2024*. [[Paper](https://arxiv.org/abs/2309.17453)] [[Code](https://github.com/mit-han-lab/streaming-llm)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-KV_Cache-purple)

1. **Titans: Learning to Memorize at Test Time**\
   Ali Behrouz, Peilin Zhong, Vahab Mirrokni. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2501.00663)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Internal-orange) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **Augmenting Language Models with Long-Term Memory**\
   Weizhi Wang, Li Dong, Hao Cheng, et al. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2306.07174)] [[Code](https://github.com/Victorwz/LongMem)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-Hybrid-purple) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **Memorizing Transformers**\
   Yuhuai Wu, Markus N. Rabe, DeLesley Hutchins, Christian Szegedy. *ICLR 2022 Spotlight*. [[Paper](https://arxiv.org/abs/2203.08913)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Latent-purple) ![](https://img.shields.io/badge/-Working-purple) ![](https://img.shields.io/badge/-kNN_Memory-purple)

[⬆️ top](#table-of-contents)

### 1.2 Structured Topological Memory Systems

#### 1.2.1 Graph-Based Memory

Memory organized as entities, relations, notes, events, or episodes connected by explicit graph edges.

1. **Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents**\
   Shuo Ji, Yibo Li, Bryan Hooi. *ICML 2026*. [[Paper](https://arxiv.org/abs/2606.06036)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Retrieval-green)

1. **GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs**\
   Tao Feng, Haozhen Zhang, Zijie Lei, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2604.23626)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multi_Agent-purple)

1. **REMem: Reasoning with Episodic Memory in Language Agent**\
   Yiheng Shu, Saisri Padmaja Jonnalagedda, Xiang Gao, et al. *ICLR 2026*. [[Paper](https://arxiv.org/abs/2602.13530)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **MIRA: Memory-Integrated Reinforcement Learning Agent with Limited LLM Guidance**\
   Narjes Nourzad, Carlee Joe-Wong. *ICLR 2026*. [[Paper](https://openreview.net/forum?id=oWagByDNPc)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-RL_based-orange)

1. **MemRec: Collaborative Memory-Augmented Agentic Recommender System**\
   Weixin Chen, Yuhan Zhao, Jingyuan Huang, et al. *ACL 2026*. [[Paper](https://arxiv.org/abs/2601.08816)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Multi_Agent-purple)

1. **LOOM: Personalized Learning Informed by Daily LLM Conversations Toward Long-Term Mastery via a Dynamic Learner Memory Graph**\
   Justin Cui, Kevin Pu, Tovi Grossman. *AAAI 2026*. [[Paper](https://arxiv.org/abs/2511.21037)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Personalization-green)

1. **MemoTime: Memory-Augmented Temporal Knowledge Graph Enhanced Large Language Model Reasoning**\
   Xingyu Tan, Xiaoyang Wang, Qing Liu, et al. *WWW 2026*. [[Paper](https://arxiv.org/abs/2510.13614)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **DYNA : Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning**\
   Ali Sarabadani, Mahtab Tajvidiyan. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.15778)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge**\
   Pavan C Shekar, Abhishek H S, Aswanth Krishnan. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.14470)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Memory_Management-orange)

1. **G-Long: Graph-Enhanced Memory Management for Efficient Long-Term Dialogue Agents**\
   Minjun Choi, Yoonjin Jang, Sangwon Youn, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.13115)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Episodic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering**\
   Xiangjun Zai, Xingyu Tan, Chen Chen, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.10921)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Procedural-yellowgreen) ![](https://img.shields.io/badge/-Multi_Agent-purple)

1. **REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs**\
   Keer Lu, Liwei Chen, Guoqing Jiang, et al. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.10694)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Semantic-green) ![](https://img.shields.io/badge/-Lifecycle-orange)

1. **TokenMizer: Graph-Structured Session Memory for Long-Horizon LLM Context Management**\
   Shweta Mishra. *arXiv 2026*. [[Paper](https://arxiv.org/abs/2606.06337)]\
   ![](https://img.shields.io/badge/-Method-lightgrey) ![](https://img.shields.io/badge/-External-blue) ![](https://img.shields.io/badge/-Graph-purple) ![](https://img.shields.io/badge/-Episodic-g