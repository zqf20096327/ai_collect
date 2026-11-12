# Awesome-AI-Memory

<p align="center">
    【中文 | <a href="README_en.md">English</a>】
</p>

<div align="center">
    <img src="assets/Gemini_Generated_Image_hretabhretabhret.png" alt="Survey Framework" width="82%">
</div>

[![Awesome](https://awesome.re/badge.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/PRs-Welcome-red)
[![Papers](https://img.shields.io/badge/Papers-1478-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
[![Open Source Projects](https://img.shields.io/badge/Open%20Source%20Projects-111-green.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/projects)


## 👋 简介
大语言模型（LLM）已迅速发展为强大的通用推理与生成引擎。然而，尽管其能力不断提升，LLM 仍然受到一个根本性限制的约束：上下文窗口（Context Window）长度有限。这一限制决定了模型在单次推理过程中能够直接访问的信息范围，使其在本质上仅具备短期记忆能力，难以支持长期对话、个性化交互、持续学习以及复杂的多阶段任务。

为突破上下文窗口的固有限制，面向大模型的记忆与记忆系统（AI Memory & Memory Systems for LLMs）逐渐成为一个重要且活跃的研究与工程方向。通过为模型引入参数之外的外部、可持久化且可控的记忆结构，记忆系统使大模型能够在生成过程中存储、检索、压缩和管理历史信息，从而在有限上下文中持续利用长期经验，实现跨会话的一致性与连续推理能力。

Awesome-AI-Memory 是一个围绕 AI 大模型记忆与记忆系统构建的资源汇编仓库，系统性地收集相关的研究论文、框架工具与实践经验。该仓库致力于梳理并呈现大模型记忆领域快速发展的研究脉络，连接自然语言处理、信息检索、智能体系统与认知科学等多个研究方向。

---

## 🎯 仓库目标
本仓库的目标是构建一个集中、持续演进的知识库，为研究者与工程实践者提供参考，助力构建能够长期记忆、持续推理并随时间不断适应的智能系统。

---

## 📏 项目范围
本仓库聚焦 **Agent Memory 与语言模型内部记忆机制**。记忆必须是论文的核心研究问题，并有明确的语言模型或多模态语言模型研究对象。

- **收录**：智能体的长期、情节、语义、共享及经验形成的流程记忆；语言模型中的存储、保持、寻址、召回与遗忘；直接针对这些机制的评测、安全研究及综述。
- **流程技能**：须具体研究从执行经验形成持久记录、跨任务复用及验证/维护的过程。静态技能包、提示词优化或通用自演化不因出现 skill/memory 关键词而收录。
- **排除**：纯视觉或低层机器人状态、硬件/KV 缓存效率、泛化的 RAG/长上下文/工具路由，以及仅声称能迁移到 LLM 的相邻工作。高层语言智能体的具身/多模态记忆仍可收录。
- **证据不足先待复核**：核实记忆使用者、内容、存取机制、核心贡献与验证依据；准确说明阅读范围，不将摘要核验称为全文核验。

详见 [论文筛选规则与发布检查](SCREENING.md)。

---

<!-- ## 🗂️ AI-Memory Taxonomy

To systematically organize the diverse research and practical resources in the field of AI large model memory, this repository categorizes memory systems across multiple orthogonal dimensions, reflecting variations in storage methods, temporal scales, content forms, operational processes, and system architectures.
1. Memory by Storage Location
- Parametric Memory
  - Knowledge implicitly encoded within model weights
  - Static and not directly editable during inference
- External / Explicit Memory
  - Memory stored outside model parameters
  - Readable, writable, and dynamically updatable
2. Memory by Temporal Scope
- Short-Term Memory
  - Entirely dependent on context window
  - Session-level, temporary information
- Long-Term Memory
  - Persistent memory across sessions and time scales
  - Supports long-term consistency and personalization
3. Memory by Content Type
- Episodic Memory
  - Event-based historical interaction memory
  - Preserves temporal sequence and contextual relationships
- Semantic Memory
  - Facts, rules, and preferences abstracted from multiple experiences
  - Typically derived from compression or induction of episodic memory
- Procedural Memory
  - Memory related to action patterns, skills, and task execution strategies
4. Memory Operations
- Writing: Determining which information should be stored
- Retrieval: Selecting relevant memories for current tasks
- Updating: Correcting or merging existing memories
- Forgetting: Removing or weakening low-value information
- Compression: Summarizing historical information to fit context windows
5. Memory Mechanisms & Architectures
- Retrieval-Augmented Generation (RAG)
- Summary-based memory mechanisms
- Vectorized semantic retrieval
- Symbolic-neural hybrid memory systems
- Event-driven and trigger-based memory mechanisms
- Reinforcement learning-based memory strategy optimization
6. Memory in Agent Systems
- Single-agent memory
- Multi-agent shared memory
- Tool-augmented memory
- Planning-aware memory
- Personality and emotion-related memory
7. Evaluation & Benchmarks
- Long-term consistency evaluation
- Continuous interaction and long-term task benchmarks
- Memory recall and utilization efficiency metrics
- Personalization and user preference retention evaluation

--- -->

## 🔔 近期热点研究与新闻
+ 2026-11-12 - 🎉 更新 38 篇论文，其中方法类与框架类论文 28 篇，数据集和评估基准类论文 7 篇，模型和系统类论文 3 篇
+ 2026-11-09 - 🎉 更新 24 篇论文，其中方法类与框架类论文 14 篇，数据集和评估基准类论文 7 篇，模型和系统类论文 3 篇
+ 2026-11-05 - 🎉 更新 72 篇论文，其中方法类与框架类论文 49 篇，数据集和评估基准类论文 15 篇，模型和系统类论文 8 篇
+ 2026-11-01 - 🎉 更新 39 篇论文，其中方法类与框架类论文 31 篇，数据集和评估基准类论文 5 篇，模型和系统类论文 3 篇
+ 2026-10-27 - 🎉 更新 34 篇论文，其中综述 2 篇，方法类与框架类论文 26 篇，数据集和评估基准类论文 5 篇，模型和系统类论文 1 篇
+ 2026-10-23 - 🎉 更新 109 篇论文，其中综述 1 篇，方法类与框架类论文 70 篇，数据集和评估基准类论文 28 篇，模型和系统类论文 10 篇
+ 2026-10-18 - 🎉 更新 32 篇论文，其中综述 2 篇，方法类与框架类论文 22 篇，数据集和评估基准类论文 6 篇，模型和系统类论文 2 篇
+ 2026-10-14 - 🎉 更新 47 篇论文，其中方法类与框架类论文 33 篇，数据集和评估基准类论文 11 篇，模型和系统类论文 3 篇
+ 2026-10-11 - 🎉 更新 53 篇论文，其中综述 1 篇，方法类与框架类论文 40 篇，数据集和评估基准类论文 10 篇，模型和系统类论文 2 篇
+ 2026-10-06 - 🎉 更新 67 篇论文，其中方法类与框架类论文 43 篇，数据集和评估基准类论文 15 篇，模型和系统类论文 9 篇
+ 2026-10-03 - 🎉 更新 69 篇论文，其中综述 1 篇，方法类与框架类论文 51 篇，数据集和评估基准类论文 11 篇，模型和系统类论文 6 篇
+ 2026-09-29 - 🎉 更新 67 篇论文，其中综述 1 篇，方法类与框架类论文 37 篇，数据集和评估基准类论文 17 篇，模型和系统类论文 12 篇
+ 2026-09-26 - 🎉 更新 17 篇论文，其中方法类与框架类论文 12 篇，数据集和评估基准类论文 2 篇，模型和系统类论文 3 篇
+ 2026-09-23 - 🎉 更新 34 篇论文，其中方法类与框架类论文 19 篇，数据集和评估基准类论文 7 篇，模型和系统类论文 8 篇
+ 2026-09-20 - 🎉 更新 11 篇论文，其中方法类与框架类论文 8 篇，数据集和评估基准类论文 2 篇，模型和系统类论文 1 篇
+ 2026-09-15 - 🎉 更新 222 篇论文，其中综述 3 篇，方法类与框架类论文 153 篇，数据集和评估基准类论文 32 篇，模型和系统类论文 34 篇
+ 2026-07-06 - 🎉 更新25篇论文，数据集和评估基准类5篇，方法类与框架类23篇
+ 2026-06-21 - 🎉 更新27篇论文，模型和系统类9篇，数据集和评估基准类5篇，方法类与框架类13篇
+ 2026-06-14 - 🎉 更新24篇论文，综述类2篇，模型和系统类4篇，数据集和评估基准类2篇，方法类与框架类16篇
+ 2026-06-06 - 🎉 更新45篇论文，综述类1篇，模型和系统类6篇，数据集和评估基准类12篇，方法类与框架类26篇
+ 2026-05-10 - 🎉 更新16篇论文，系统&模型类3篇，Benchmark类1篇，方法类12篇；并新增1个开源系统项目
+ 2026-05-06 - 🎉 更新16篇论文，系统&模型类2篇，Benchmark类2篇，方法类12篇
+ 2026-04-27 - 🎉 更新15篇论文，综述类2篇，系统与模型类3篇，方法类10篇
+ 2026-04-17 - 🎉 更新46篇论文，综述类1篇，系统与模型类5篇，Benchmark类3篇，方法类37篇
+ 2026-04-07 - 🎉 更新16篇论文，方法类15篇，Benchmark类1篇
+ 2026-03-15 - 🎉 更新14篇论文，方法类14篇
+ 2026-03-08 - 🎉 更新15篇论文，综述类3篇, 系统&模型类2篇，Benchmark类5篇，方法类5篇。
+ 2026-03-02 - 🎉 新增一个代码agent到仓库中
+ 2026-02-27 - 🎉 更新20篇论文，综述类1篇, 系统&模型类2篇，Benchmark类2篇，方法类15篇。
+ 2026-02-26 - 🎉 更新14篇论文，方法类14篇
+ 2026-02-14 - 🎉 更新15篇论文，综述类1篇，方法类12篇，benchmark类1篇，系统与模型类1篇
+ 2026-02-09 - 🎉 更新15篇论文
+ 2026-02-01 - 🎉 更新16篇论文，方法类9篇，benchmark类4篇，系统与模型类3篇
+ 2025-12-24 – 🎉 发布仓库-V(1.0)
+ 2025-12-10 – 🎉 仓库初始化

---

🗺️ 目录表
- [Awesome-AI-Memory](#awesome-ai-memory)
  - [👋 简介](#-简介)
  - [🎯 仓库目标](#-仓库目标)
  - [📏 项目范围](#-项目范围)
  - [🔔 近期热点研究与新闻](#-近期热点研究与新闻)
  - [🧠 核心概念](#-核心概念)
  - [📚 论文列表](#-论文列表)
  - [🧰 仓库资源](#-仓库资源)
    - [📊 测试基准](#-测试基准)
    - [💻 开源系统](#-开源系统)
    - [🎥 多媒体资源](#-多媒体资源)
    - [🧠 Adam 框架](#-adam-框架)
  - [🤝  如何贡献](#--如何贡献)
  - [💬 社区和支持](#-社区和支持)
  - [🌟 仓库关注量](#-仓库关注量)

---

## 🧠 核心概念

- 大模型记忆: LLM的记忆机制融合了隐性知识（通过训练过程内化于模型参数中）与显式存储（运行时可检索的外部存储），这种双重架构使模型突破token处理的局限，具备类似人类"记忆过往、认知当下、预见未来"的认知能力。

- **记忆系统**：为大语言模型实现记忆功能的完整技术架构，包含四大核心组件：
  - **记忆存储层**：向量数据库（如 Chroma、Weaviate）、图数据库或混合存储方案
  - **记忆处理层**：嵌入模型、摘要生成器与记忆分割器
  - **记忆检索层**：多阶段检索器、重排序模块与上下文注入器
  - **记忆控制层**：记忆优先级管理器、遗忘控制器与一致性协调器

- **记忆操作**：通过记忆系统工具调用执行的原子级记忆操作：
  - **写入**：将对话内容转换为向量进行存储，通常结合摘要生成以减少噪声信息
  - **检索**：根据当前上下文生成查询语句以获取Top-K相关记忆
  - **更新**：通过向量相似度找到相关记忆并进行替换或增强
  - **删除**：基于用户指令或自动策略（如隐私数据过期）删除特定记忆
  - **压缩**：将多个相关记忆合并为摘要以释放存储空间

- **记忆管理**：在记忆系统内实施记忆管控的方法论，包含以下机制：
  - **记忆生命周期**：从创建、活跃使用、冷启动访问到归档/删除的全周期管理
  - **冲突解决**：矛盾信息仲裁机制（如时间戳优先级、来源可信度加权）
  - **资源预算**：为不同用户/任务分配内存配额以防止资源滥用
  - **安全治理**：自动检测和去标识化个人身份信息（PII）

- **记忆分类**：记忆系统特有的多维度分类体系：
  - **按访问频率**：工作记忆（当前任务）、常用记忆（个人偏好）、归档记忆（历史记录）
  - **按结构化程度**：结构化记忆（数据库记录）、半结构化记忆（对话摘要）、非结构化记忆（原始对话文本）
  - **按共享范围**：个人记忆（单用户）、团队记忆（协作空间）、公共记忆（共享知识库）
  - **按时效属性**：永久记忆（核心事实）、临时记忆（对话上下文）、时效性记忆（如"用户今天心情不好"）

- **记忆机制**：驱动记忆系统功能的核心技术组件：
  - **检索增强生成（RAG）**：通过从知识库中检索相关信息来增强生成能力
  - **记忆反思循环**：模型定期"回顾"对话历史以生成高层次摘要
  - **记忆路由**：根据查询类型（个人记忆/公共知识库）自动选择检索源

- **显式记忆**：以原始文本形式存储在模型外部的记忆，通过融合混合索引策略的向量数据库实现：
  - **稠密向量索引**：处理语义相似性查询
  - **稀疏关键词索引**：处理精确匹配查询
  - **多向量索引**：将长文档切分为多个部分，每个部分独立索引

- **参数化记忆**：存储于语言模型固定权重中的知识与能力，具有以下特征：
  - 作为模型的核心长期语义记忆载体
  - 无需外部检索或显式上下文支持即可激活
  - 提供零样本推理、通用响应与语言生成的基础能力

- **长期记忆**：设计用于持久存储的关键信息，通常通过外部知识库实现，包含以下功能：
  - **自动摘要生成**：将多轮对话提炼为结构化记忆
  - **上下文绑定**：记录记忆上下文以防止错误泛化
  - **多模态存储**：同时保存文本、图像、音频等多种模态记忆

- **短期记忆**：受限于注意力机制的大语言模型上下文窗口中的活跃信息，包含以下关键技术：
  - **KV缓存管理**：复用键值缓存以减少冗余计算
  - **上下文压缩**：使用摘要替代详细历史（如："前5轮对话讨论了项目预算"）
  - **滑动窗口注意力机制**：仅关注最近N个token，同时保留特殊标记
  - **记忆摘要注入**：将长期记忆摘要动态插入短期上下文

- **情景记忆**：记录特定用户交互历史的记忆类型，是个性化AI的基础：
  - **用户身份识别**：跨会话识别同一用户
  - **交互轨迹记录**：保存用户决策路径与反馈
  - **情绪状态追踪**：记录用户情绪变化规律
  - **偏好演化建模**：捕捉用户兴趣长期变化

- **记忆遗忘**：大模型中刻意设计的遗忘机制，包含以下技术实现：
  - **选择性遗忘（机器遗忘）**：移除训练数据中特定信息的影响，例如通过遗忘层覆盖特定知识
  - **隐私保护遗忘**：自动识别并删除个人身份信息（PII），或设置自动过期策略
  - **记忆衰减**：根据使用频率自动降低低频访问记忆的优先级
  - **冲突驱动遗忘**：当新证据与旧记忆冲突时，策略性更新或淘汰旧记忆

- **记忆检索**：从海量记忆库中精确定位相关信息的复杂过程：
  - **语义预过滤**：通过向量相似度匹配获取Top-100候选结果
  - **上下文重排序**：根据当前查询上下文重新排序结果
  - **时间过滤**：优先选择最新相关数据

- **记忆压缩**：在资源受限条件下最大化记忆效用的技术体系：
  - **内容级压缩**：提取核心信息并舍弃冗余细节
  - **表征级压缩**：向量量化（如乘积量化编码）、维度约简
  - **组织级压缩**：聚类相似记忆、构建分层记忆结构
  - **知识蒸馏**：将外部记忆中的关键模式迁移至参数化记忆

---

## 📚 论文列表
以下论文按发表日期排列：

<details>
  <summary><strong>综述</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Learning to Remember: Advances in Memory Mechanisms for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.35089"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从记忆生命周期、存储载体和系统作用三个维度梳理语言模型记忆研究。<br>
        • 区分非参数记忆、参数记忆与智能体演化记忆，并覆盖构建、维护、检索、整合、遗忘和治理。<br>
        • 提供贯通机制、评测与部署的研究路线图；属于文献综述，不提供新系统的性能验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-23</td>
      <td style="width: 55%;"><strong>Agentic Memory Management Is the Next Frontier of Information Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.32464"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将智能体记忆管理提出为信息检索的重要研究方向。<br>
        • 给出系统级框架，以常量、函数和算子区分记忆对象与检索语义，并联系结构、存储、检索和使用。<br>
        • 提出基准、记忆效用与参数/非参数混合优化议程；属于观点与概念分析，未提供新的系统性能实证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23319"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从范围与持久性两个视角梳理长程 VLA 模型的记忆范式。<br>
        • 按范围及持久性组织五类范式与一个新前沿，对比结构复杂度、开源成熟度和维护挑战。<br>
        • 提出架构复杂度与开源成熟度的权衡；属于综述分析，不是新方法优越性的实验证明。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21165"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以选择性记忆管理综述语言模型压缩，将上下文与长期存储纳入共同生命周期。<br>
        • 统一写入、卸载、召回、注入、物化、淘汰、巩固、遗忘的状态及成本。<br>
        • 指出评测缺口和治理问题；这是概念与文献综合，不是新系统的性能保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19366"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以形成表示与管理适应两个轴综述多模态代理记忆。<br>
        • 区分静态、固定策略动态更新与管理策略自演化，分析保真、抽象、时间有效性及来源追溯。<br>
        • 总结设计原则与开放问题；属于分析性综述，不把分类框架当作新的实证性能结论。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>Towards In-Parameter Memory Augmentation for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.08630"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 综述参数内记忆增强：将预训练后获得的事实、偏好、文档或经验编码为可用于推理的参数对象。<br>
        • 按嵌入、注意力、FFN 或混合位置，以及部署前后获得记忆两个正交轴整理方法与边界。<br>
        • 提出干扰、安全、上下文协同和自我改进方向；这是方法综述，不提供统一新模型的实测优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-30</td>
      <td style="width: 55%;"><strong>The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.39661"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将注意力演化视为模型内部上下文记忆的表示、更新、访问、读取与整合问题。<br>
        • 梳理 59 个发布记录与 11 个开放端点，比较显式缓存、循环状态、稀疏访问及跨层复用。<br>
        • 提出多维有状态记忆路由假设；属于机制综述与架构归纳，不是统一受控性能实验。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-25</td>
      <td style="width: 55%;"><strong>Machine Unlearning for Large Language Models: Foundations, Advances, and Agentic Extensions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.30909"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 综述模型参数及智能体外部状态中的遗忘。<br>
        • 使用五层系统框架和六类证据维度比较移除主张及恢复测试。<br>
        • 指出仅评测模型不足以证明记忆、工具和后续更新中的影响已移除。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-09-08</td>
      <td style="width: 55%;"><strong>Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Experience%20%2F%20Skills-blue" alt="Experience / Skills">
        <img src="https://img.shields.io/badge/Personal%20Memory-blue" alt="Personal Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2609.08599"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 综述长期个性化智能体的图记忆。<br>
        • 围绕表示、演化、检索和评测组织研究。<br>
        • 比较设计选择，并梳理可靠性与可控性挑战。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-28</td>
      <td style="width: 55%;"><strong>Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory">
        <img src="https://img.shields.io/badge/Memory%20Architecture-blue" alt="Memory Architecture">
        <img src="https://img.shields.io/badge/Survey-blue" alt="Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.25380"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从模型架构视角综述大语言模型记忆。<br>
        • 按表示形式、更新动态及持久性组织记忆机制。<br>
        • 综合分析写入、路由、固化、效率权衡及评测方向。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-07-20</td>
      <td style="width: 55%;"><strong>The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Organization%20%2F%20Use-blue" alt="Memory Organization / Use"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2607.19433"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分类梳理有状态智能体中的时间持久攻击。<br>
        • 分析记忆注入、延迟欺骗及工作流级威胁模型。<br>
        • 综合轨迹监控、形式验证及可信记忆等防御方向。
      </td>
    </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-25</td>
        <td style="width: 55%;"><strong>Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/综述-4A90E2" alt="Survey">
          <img src="https://img.shields.io/badge/Agent%20隐私-F5A623" alt="Agent Privacy">
          <img src="https://img.shields.io/badge/数据治理-7ED321" alt="Data Governance">
          <img src="https://img.shields.io/badge/记忆风险-D0021B" alt="Memory Risk">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.26627v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从数据中心视角综述 LLM Agent 的隐私问题，关注智能体查询、存储、记忆、交换并据此行动的数据，而不只是按攻击类型分类。<br>
          • 论文围绕数据库、文档集合、API、跨会话记忆、中间工作流状态和多智能体通信组织风险，指出敏感信息可能在最终回答生成前就通过多种路径泄露。<br>
          • 该综述强调 Agent 隐私需要覆盖记忆写入、检索、委托、日志和工具调用的全生命周期控制，因此持久状态与数据治理是安全部署的核心问题。
        </td>
      </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-06-23</td>
        <td style="width: 55%;"><strong>Are We Ready For An Agent-Native Memory System?</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Memory%20System-green" alt="Memory System">
          <img src="https://img.shields.io/badge/Evaluation-orange" alt="Evaluation">
          <img src="https://img.shields.io/badge/Data%20Management-purple" alt="Data Management">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.24775v1">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从数据管理视角研究 Agent Memory，指出面向 LLM Agent 的记忆不应只被视作检索增强组件，而应作为支持持久化存储、检索、更新、整合与生命周期治理的系统来评估。<br>
          • 论文将 Agent 原生记忆系统拆解为四个模块：表示与存储、提取、检索与路由、维护，并在这一框架下评估了 12 个代表性记忆系统和 2 个基线，覆盖 5 类基准工作负载与 11 个数据集。<br>
          • 实验表明不存在一种在所有场景下都占优的记忆架构，效果高度依赖记忆结构与工作负载瓶颈的匹配；细粒度消融进一步量化了表示保真度、检索精度、更新正确性和长程稳定性等因素，成本分析也显示局部维护通常比全局重组更高效。
        </td>
      </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-06-10</td>
        <td style="width: 55%;"><strong>Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Agents-F5A623" alt="LLM Agents">
          <img src="https://img.shields.io/badge/Environment%20Modeling-7ED321" alt="Environment Modeling">
          <img src="https://img.shields.io/badge/Synthesis-D0021B" alt="Synthesis">
          <img src="https://img.shields.io/badge/Evaluation-9013FE" alt="Evaluation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.12191">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文系统梳理了LLM代理环境的全生命周期框架，覆盖建模、合成、评估与应用四个核心环节。<br>
          • 提出了符号与神经两类环境合成范式，并从结构属性与能力维度分析了环境设计的演化路径。<br>
          • 强调代理与环境的协同演化机制（记忆、工作流、轨迹与探索），并指出未来将走向环境即服务与多代理生态。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-09</td>
        <td style="width: 55%;"><strong>Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/LLM%20Security-%2350E3C2" alt="LLM Security">
          <img src="https://img.shields.io/badge/Attacks-%23F8E71C" alt="Attacks">
          <img src="https://img.shields.io/badge/Defenses-%23FF6FB5" alt="Defenses">
          <img src="https://img.shields.io/badge/Evaluation-%239B9B9B" alt="Evaluation">
        </td>
        <td style="width: 15%;">
          <a href="https://arxiv.org/pdf/2606.10749">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
          </a>
        </td>
      </tr>
      <tr>
        <td colspan="3">
          • 本文从生命周期视角系统刻画LLM代理的安全风险，并统一建模信息流、授权委托与持久状态三类关键交互。<br>
          • 通过综述247篇研究，归纳攻击面、防御机制与评估体系，揭示当前安全方法整体仍偏脆弱且不完整。<br>
          • 强调需要构建可信边界清晰、权限控制原则化、且贴近真实环境的长期状态安全评估框架。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-04</td>
        <td style="width: 55%;"><strong>Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/LLM-orange" alt="LLM">
          <img src="https://img.shields.io/badge/Memory%20Systems-green" alt="Memory Systems">
          <img src="https://img.shields.io/badge/Long--Horizon%20Tasks-red" alt="Long-Horizon Tasks">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2606.06448">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 将 Agent Memory 定位为长程有状态工作负载，而不只是检索增强模块。<br>
          • 提出系统导向分类法和阶段感知 profiling 工具，用于拆解构建、检索和生成成本。<br>
          • 分析十个代表性系统，并总结面向规模化部署、新鲜度与延迟权衡的系统建议。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-23</td>
        <td style="width: 55%;"><strong>MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/多模态记忆-blue" alt="Multimodal Memory">
          <img src="https://img.shields.io/badge/视觉Benchmark-red" alt="Visual Benchmark">
          <img src="https://img.shields.io/badge/评估框架-green" alt="Evaluation Framework">
          <img src="https://img.shields.io/badge/长期记忆-orange" alt="Long-term Memory">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.15128">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 MemEye，一个以视觉为中心的基准测试，用于评估多模态 Agent 的长期记忆能力，避免文本主导的"捷径"问题。<br>
          • 设计了二维评估矩阵（X轴：场景/区域/实例/像素粒度；Y轴：原子检索/关系关联/演化合成推理深度）。<br>
          • 引入三阶段验证闸门，确保问题无法通过文本上下文、简短字幕或超出 VLM 能力的方式被解决。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-06-01</td>
        <td style="width: 55%;"><strong>EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/长期记忆-blue" alt="Long-term Memory">
          <img src="https://img.shields.io/badge/Memory%20OS-orange" alt="Memory OS">
          <img src="https://img.shields.io/badge/自组织-green" alt="Self-Organizing">
          <img src="https://img.shields.io/badge/语义整合-red" alt="Semantic Consolidation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2601.02163">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 提出 EverMemOS，一个三阶段记忆生命周期（情景记忆形成 → 语义整合 → 重构式回忆），将碎片化对话组织为结构化、可演化的记忆单元（MemCell/MemScene）。<br>
          • 引入 MemCell 作为原子记忆单元，包含 Episode + Atomic Facts + Foresight + Metadata；MemScene 用于场景级整合，支持长期用户画像演化。<br>
          • 设计重构式检索范式，包含 MemScene 引导检索、前瞻有效性过滤和充分性验证，实现长期推理中"必要且充分"的上下文获取。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-05-19</td>
        <td style="width: 55%;"><strong>An Agent-Oriented Pluggable Experience-RAG Skill for Experience-Driven Retrieval Strategy Orchestration</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Experience--RAG-yellow" alt="Experience-RAG">
          <img src="https://img.shields.io/badge/Retrieval%20Strategy-orange" alt="Retrieval Strategy">
          <img src="https://img.shields.io/badge/Skill%20Orchestration-green" alt="Skill Orchestration">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2605.03989">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 识别了流水线式检索的三个工程问题：策略逻辑不可复用、路由决策不可观测、工作流耦合导致不可演进。<br>
          • 提出 Experience-RAG Skill，包含六个模块（统一接口、场景分析、经验记忆、策略路由、检索器池、结果打包），将检索策略选择封装为可插拔的 Agent skill。<br>
          • 规则路由（0.8924）优于学习路由（0.8778/0.8627），经验记忆记录 (scene_features, score_vector, best_margin) 为未来升级到学习路由奠定基础。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Human Cognition in Machines: A Unified Perspective of World Models</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/World%20Models-brightgreen" alt="World Models">
          <img src="https://img.shields.io/badge/Cognitive%20Architecture-yellow" alt="Cognitive Architecture">
          <img src="https://img.shields.io/badge/Meta--cognition-teal" alt="Meta-cognition">
          <img src="https://img.shields.io/badge/Structured%20Knowledge-orange" alt="Structured Knowledge">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16592">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 从认知架构视角统一梳理世界模型中的记忆、感知、语言、推理、想象、动机与元认知等能力。<br>
          • 提出面向科学发现的 Epistemic World Models 类别，并给出跨视频、具身与认知世界模型的分类和未来方向。
        </td>
      </tr>
      <tr>
        <td rowspan="2" style="width: 15%;">2026-04-17</td>
        <td style="width: 55%;"><strong>Agentic Frameworks for Reasoning Tasks: An Empirical Study</strong></td>
        <td style="width: 15%;">
          <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
          <img src="https://img.shields.io/badge/Context%20Management-brightgreen" alt="Context Management">
          <img src="https://img.shields.io/badge/Agentic%20Framework-yellow" alt="Agentic Framework">
          <img src="https://img.shields.io/badge/Orchestration-teal" alt="Orchestration">
          <img src="https://img.shields.io/badge/Memory%20Control-orange" alt="Memory Control">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.16646">
          <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
      </tr>
      <tr>
        <td colspan="3">
          • 对 22 种常用 Agentic 框架在 BBH、GSM8K 与 ARC 上进行统一评测，比较准确率、耗时、成本与跨基准一致性。<br>
          • 结果表明性能差异主要来自编排质量，尤其是记忆控制、上下文增长和失败重试机制会显著影响效率与成本。
        </td>
      </tr>
<tr>
        <td rowspan="2" style="width: 15%;">2026-04-09</td>
        <td style="width: 55%;"><strong>Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Survey-red" alt="Survey">
            <img src="https://img.shields.io/badge/Externalization-teal" alt="Externalization">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/abs/2604.08224">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 从“外化”视角综述 LLM Agent 的记忆、技能、协议与 harness 工程。<br>
            • 指出记忆外化跨时间状态，技能外化程序能力，协议外化交互结构，harness 负责统一协调这些模块。<br>
            • 梳理了从模型参数到上下文再到外部基础设施的演进路径，并讨论其中的关键权衡与开放问题。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-05</td>
        <td style="width: 55%;"><strong>Beyond the Context Window: A Cost-Performance Analysis of Fact-Based Memory vs. Long-Context LLMs for Persistent Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Long%20Context-blue" alt="Long Context">
            <img src="https://img.shields.io/badge/Cost%20Analysis-brightgreen" alt="Cost Analysis">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.04814">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 解决业界关于长上下文模型与外部记忆系统在构建持久化代理时的效能与成本优劣之争。<br>
            • 在三大主流记忆基准上，从准确率与累计 API 推理成本双重维度，系统交叉评测长上下文与事实型外部记忆方案。<br>
            • 长上下文在事实召回上具有优势，但成本随轮次递增；在 100k 上下文长度下，记忆系统在约 10 轮交互后即可实现成本反超，为实际工程选型提供了量化依据。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>Modular Memory is the Key to Continual Learning Agents</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Continual%20Learning-blue" alt="Continual Learning">
            <img src="https://img.shields.io/badge/Architecture-brightgreen" alt="Architecture">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01761">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 传统基础模型在持续学习时依赖权重更新，极易导致灾难性遗忘，难以实现大规模经验积累。<br>
            • 提出一种结合上下文学习与权重内学习的模块化记忆架构路线图。<br>
            • 该架构利用上下文学习实现快速适应，通过权重更新实现能力固化，为构建真正意义上的终身学习智能体提供了理论指引。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-03-02</td>
        <td style="width: 55%;"><strong>Emerging Human-like Strategies for Semantic Memory Foraging in Large Language Models</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Cognitive%20Alignment-blue" alt="Cognitive Alignment">
            <img src="https://img.shields.io/badge/Interpretability-brightgreen" alt="Interpretability">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2603.01822">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 旨在探究大语言模型内部在处理海量语义记忆时，是否具备类似人类的高效策略性访问机制。<br>
            • 借助机械可解释性技术分析语义流畅性任务，严密剖析模型内部收敛性与发散性的记忆搜索模式。<br>
            • 证实 LLM 不同层级中存在类人的策略性记忆搜寻行为，为认知对齐研究及强化人机协作奠定了可解释性基础。
        </td>
    </tr>
    <tr>
        <td rowspan="2" style="width: 15%;">2026-02-26</td>
        <td style="width: 55%;"><strong>Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and Future Directions</strong></td>
        <td style="width: 15%;">
            <img src="https://img.shields.io/badge/Personalized%20Agents-blue" alt="Personalized Agents">
            <img src="https://img.shields.io/badge/User%20Adaptation-brightgreen" alt="User Adaptation">
            <img src="https://img.shields.io/badge/Evaluation-yellow" alt="Evaluation">
        </td>
        <td style="width: 15%;"><a href="https://arxiv.org/pdf/2602.22680.pdf">
            <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a></td>
    </tr>
    <tr>
        <td colspan="3">
            • 本论文探讨了个性化LLM驱动代理的基础、评估和未来方向，对个性化 LLM 驱动代理的基础、评估及未来方向进行了能力导向的系统性综述。<br>
            • 论文围绕用户画像建模、记忆、规划和行动执行这四个相互依赖的核心组件构建了分类法。<br>
            • 本文综合分析了用户信号的表示、传播与利用方式，并探讨了从通用辅助到专业领域的应用场景及设计权衡。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-01-14</td>
      <td style="width: 55%;">
      <strong>Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
        <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2602.06052">
        <img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 从存储介质、认知机制和服务主体三个维度构建了统一的分类框架，系统化地定义了基础智能体记忆的分类学。<br>
          • 深入剖析了记忆在单智能体与多智能体系统中的动态操作机制，并归纳了提示词学习、参数微调和强化学习三种主流的学习策略。<br>
          • 全面梳理了现有的评价指标与基准测试体系，并结合多领域应用现状，提出了提升记忆效率、安全性及多模态能力的未来研究方向。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-12-15</td>
      <td style="width: 55%;">
      <strong>Memory in the Age of AI Agents: A Survey</strong></td>
      <td style="width: 15%;">
        <img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory">
        <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
        <img src="https://img.shields.io/badge/Forms--Functions--Dynamics-purple" alt="Forms-Functions-Dynamics">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2512.13564">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 提供了一个全面且最新的智能体记忆全景图，明确将其与 LLM 记忆、RAG 和上下文工程等相关概念区分开来。<br>
          • 引入了一个统一的分类体系，通过三个视角审视记忆：<strong>形式</strong>（Token 级、参数化、潜在）、<strong>功能</strong>（事实性、经验性、工作）和<strong>动态</strong>（形成、演变、检索）。<br>
          • 探讨了新兴的研究前沿，如面向自动化的记忆设计、强化学习集成和可信度，同时汇编了具有代表性的基准和框架。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-18</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/full/10.1145/3749987">
        <img src="https://img.shields.io/badge/ACM-paper-black?labelColor=blue" alt="Paper Badge">
        </a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 深入探讨了机器遗忘的概念和背景，强调了其在现代机器学习中的重要性。<br>
          • 机器遗忘旨在使学习算法能够有效地消除特定数据的影响，而无需进行完整的模型重新训练。<br>
          • 论文分析了机器遗忘的必要性、挑战和设计要求，回顾了当前的研究进展，并强调了该领域在算法有效性、公平性和隐私保护方面的复杂性和多样性。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-09-02</td>
      <td style="width: 55%;">
      <strong>A Survey on the Memory Mechanism of Large Language Model based Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms Badge">
      <img src="https://img.shields.io/badge/Memory%20Modules-orange" alt="Memory Modules Badge">
      <td style="width: 15%;">
        <a href="https://dl.acm.org/doi/pdf/10.1145/3748302">
        <img src="https://img.shields.io/badge/ACM-paper-black?labelColor=blue" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨了基于 LLM 的智能体的记忆机制，强调了记忆在智能体自我进化和复杂交互中的关键作用。<br>
          • 系统总结和分类了现有的记忆模块设计和评估方法，并分析了它们在不同应用场景中的作用和局限性。<br>
          • 此类智能体能够改善决策制定和任务执行。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-31</td>
      <td style="width: 55%;">
      <strong>A Survey of Machine Unlearning in Large Language Models: Methods, Challenges and Future Directions</strong></td>
      <td style="width: 15%;">
      <img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting"></td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2503.01854v2">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 论文调查了大语言模型（LLM）中的机器遗忘，旨在有效消除不良数据（如敏感或非法信息）的影响，无需完全重新训练，同时保留整体模型效用。<br>
          • 它定义了 LLM 遗忘的目标和范式，并建立了一个全面的分类体系。<br>
          • 论文回顾了现有方法，评估了它们的优势和局限性，并讨论了未来的研究机会。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-05-27</td>
      <td style="width: 55%;">
      <strong>Rethinking Memory in AI Taxonomy, Operations, Topics, and Future Directions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      <img src="https://img.shields.io/badge/Memory%20Operations-brightgreen" alt="Memory Operations">
      <img src="https://img.shields.io/badge/Memory%20Integration-purple" alt="Memory Integration">
      <img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Contextual%20Memory-cyan" alt="Contextual Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2505.00675">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探索了人工智能（AI）中关于记忆的多维研究，特别关注大语言模型（LLM）中的记忆操作和管理。<br>
          • 对各种类型的记忆表示和操作（包括整合、更新、索引、遗忘、检索和压缩）进行了分类，并系统分析了记忆在 AI 中的重要性及其实现方式。<br>
          • 通过广泛的文献回顾，论文确定了四个关键研究主题：长期记忆、参数化记忆、长上下文记忆和多源记忆整合。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-24</td>
      <td style="width: 55%;">
      <strong>Cognitive Memory in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      <img src="https://img.shields.io/badge/Memory%20Taxonomy-lightgrey" alt="Memory Taxonomy">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.02441">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 对大语言模型（LLM）中的记忆机制进行了全面考察，特别关注不同类型的记忆及其在模型中的作用。<br>
          • 虽然 LLM 在信息检索和交互总结方面表现出色，但其长期记忆仍然不稳定。<br>
          • 将记忆集成到 AI 系统中对于提供上下文丰富的响应、减少幻觉、提高数据处理效率以及实现 AI 系统的自我进化至关重要。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-23</td>
      <td style="width: 55%;"><strong>From Human Memory to AI Memory A Survey on Memory Mechanisms in the Era of LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Human%20Memory-red" alt="Human Memory">
      <img src="https://img.shields.io/badge/Memory%20Mechanisms-yellowgreen" alt="Memory Mechanisms">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2504.15965">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 探讨了人类记忆与基于 LLM 的人工智能（AI）系统的记忆机制之间的关系。<br>
          • 主要贡献包括系统定义了 LLM 驱动的 AI 系统中的记忆，及其与人类记忆的概念联系。<br>
          • 论文提出了一个基于对象、形式和时间的三维记忆分类体系，并总结了当前个人记忆和系统记忆研究中的关键开放问题。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-04-02</td>
      <td style="width: 55%;"><strong>Digital Forgetting in Large Language Models: A Survey of Unlearning Methods</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Machine%20Forgetting-grey" alt="Machine Forgetting">
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2404.02062">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 论文探讨了大语言模型（LLM）中的数字遗忘及相应的遗忘方法，重点是解决与隐私、版权和社会伦理相关的问题。<br>
          • 它分析了不同类型的模型架构和训练过程，以及数字遗忘的实际方法，包括数据重新训练、机器遗忘和提示工程。<br>
          • 通过引入“遗忘保证”的概念，论文强调了精确遗忘和近似遗忘的有效机制。
        </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2025-01-12</td>
      <td style="width: 55%;"><strong>Human-inspired Perspectives: A Survey on AI Long-term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Long--Term%20Memory-gold" alt="Long-Term Memory">
      <img src="https://img.shields.io/badge/Parametric%20Memory-pink" alt="Parametric Memory">
      <img src="https://img.shields.io/badge/Non--Parametric%20Memory-green" alt="Non-Parametric Memory">
      <img src="https://img.shields.io/badge/Sensory%20Memory-brown" alt="Sensory Memory">
      <img src="https://img.shields.io/badge/Working%20Memory-blueviolet" alt="Working Memory">
      </td>
      <td style="width: 15%;">
        <a href="https://arxiv.org/pdf/2411.00489">
        <img src="https://img.shields.io/badge/arXiv-paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a>
      </td>
    </tr>
    <tr>
        <td colspan="3">
          • 本文系统地考察了人类长期记忆机制与 AI 长期记忆之间的相互作用，并提出了一种自适应长期记忆认知架构（SALM）。<br>
          • 它介绍了人类记忆的结构，包括感官记忆、工作记忆以及不同类型的长期记忆（情景记忆、语义记忆和程序记忆）。<br>
          • 论文分析了 AI 长期记忆的分类——参数化记忆和非参数化记忆——及其存储和检索机制。
        </td>
    </tr>
  </table>
</details>



<details>
  <summary><strong>方法类与框架类论文</strong></summary>

  <table style="width: 100%;">
    <tr>
      <td><strong>时间</strong></td>
      <td><strong>论文与摘要</strong></td>
      <td><strong>标签</strong></td>
      <td><strong>链接</strong></td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>On Private Knowledge Retrieval and Private Inference for secure multi-agent systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.13696"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将语义记忆投毒与检索隐私结合考虑，为智能体记忆提供签名和私密访问设计。<br>
        • 本地 Prolog 式推理器访问外部签名知识库，给出 k 匿名及信息论私密检索等 Python 实现。<br>
        • 证据主要是架构与实现方案；所读摘要未报告大规模攻击成功率，签名机制不能自动保证原始知识真实。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>Recursive memory for prediction and generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.13760"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 理论区分有限状态用于预测未来与递归生成未来时的记忆需求。<br>
        • 对正转移隐马尔可夫源分析贝叶斯滤波舍入与 KL 链式累积，并研究滑动历史统计的维护成本。<br>
        • 预测可需 O(log(1/ε)) 位，而长度 T 生成可需 log(T/ε) 量级；额外 log T 依赖误差度量和私有随机性假设，未报告真实 LLM 基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.13946"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TreeAgent 针对长层级数据组织结构感知记忆，减少逐层压缩造成的信息丢失。<br>
        • 按子树和相邻片段分工，保存字段及结构路径，并通过子到父残差链接传递未保留的证据。<br>
        • 四种智能体、八类检索聚合任务覆盖 8K–1M 输入，摘要报告平均 3.61% 提升；收益取决于所测结构与任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.14017"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PMR 用个性化记忆 rubric 学习每位用户应保留什么，避免统一评分掩盖个体需要。<br>
        • 将终局问答反馈分配到记忆更新 token，联合通用与用户 rubric，并对经验证成功进行放大、失败使用标准 RL。<br>
        • 四个基准报告一致改善，部署时不调用评分器；摘要未提供统一增益，rubric 与策略共同演化仍需防止循环自证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with Dynamic Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.14220"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SHARP 通过动态轨迹记忆保持较早出行模式并追踪变化，支持层级位置预测。<br>
        • 新签到与统计信息修订既有长期画像，再生成近期上下文；类别预测结合该记忆与时间感知转移图。<br>
        • 去除记忆使三数据集 Acc@10 下降 4.05/4.85/6.32 个百分点；最长用户轨迹的更新输入维持约 6–7k token，节省结果不代表全用户分布。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>Don&#39;t Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.14320"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • WikiTrace 用可下钻的证据链接减少错误经验造成的后续性能退化。<br>
        • 把教训连接到结果摘要和原始轨迹；新任务遇到缺证、冲突或来源失败时逐层核查，再决定是否采纳。<br>
        • 五个基准上优于比较记忆方法及相同教训的无证据版本；摘要未给统一数值，证据可追溯不代表教训总是正确。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-10</td>
      <td style="width: 55%;"><strong>When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.14326"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • FGSE 将经验记忆视作需要检验的假设，研究何时应准入、修订或拒绝。<br>
        • 记录前提、建议行为与预期验证结果，先做临时迁移证伪，再运行归档回归探针，控制对旧任务的伤害。<br>
        • 报告 WebArena 39.8、AppWorld 78.8 及其他任务结果，但有害提交仍为 3.6%；验证门控降低风险而非保证无害。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>Can LLM Agents Organize Their Own Memory?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.11929"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SoMem 让智能体以普通链接文档自行组织持久记忆，而不是使用固定记录结构。<br>
        • 智能体决定总结、分组和主题修订，运行时验证更新并生成时间/关系视图；查询时自主搜索、读文档和追溯原始证据。<br>
        • LoCoMo、BEAM-100K、LongMemEval-S 较最强基线分别高 2.66/3.10/2.00 个百分点；另测跨模型复用，结果仍限于所测记忆任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>TANSAR: Editable and Attributable Correlation Matrix Memories under Correlated Keys, with Rule-Constrained Multi-Hop Knowledge Editing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.12374"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TANSAR 分析相关语义键下关联矩阵记忆的容量、精确删除与归因。<br>
        • 用框架相干性推导界，沿关联有向图检索并用 Horn 约束剪枝，只将核验路径注入冻结模型残差流。<br>
        • 多跳编辑矛盾率由 25.1% 至 0.5%；陈旧关联完全移除时 Hopfield 对照为 0%，说明收益取决于存储与约束条件，非无条件优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.12552"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SciMARS 区分共享记忆内容与使用策略，研究保留证据后如何改善记录、检索和分发。<br>
        • 独立记忆编辑器调整记录义务、过滤、限额与订阅，保持来源规则，通过隔离候选探针与固定策略对照选择更新。<br>
        • 科学发现 GPT-6-Astra 队列由 8/18 至 12/18，另测编程与交互任务；这是任务内适配及数据回放/数字孪生证据，不是新增湿实验或跨任务记忆证明。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.12825"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MaxIM 将增量记忆压缩作为容量受限的信息奖励问题，缓解终局奖励的信用分配困难。<br>
        • 总结策略递归更新有界文本记忆，训练 critic 用未来目标预测与历史一致性构造稠密奖励；冻结行动者读取，测试不调用 critic。<br>
        • 科学阅读和多轮对话比较支持任务效用与事实保真改善；依赖理论中目标中介等假设，部分指标来自自动评分而非人类偏好验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.12872"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HiVe-Mem 同时扩展相关记忆覆盖范围和每条记忆的证据形式。<br>
        • 用文本/视觉锚点构建情节关系图，横向扩展检索种子，再由可训练选择器纵向组合摘要、图像和原始历史。<br>
        • 三个多模态记忆基准跨模型改善，相对所比较的最省 token 多模态基线减少约 90% token；结果限于该比较集合与协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>World In-Context Learning for Agentic Robot Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.12885"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • World In-Context Learning 从世界反馈形成可复用任务记忆，用上下文学习补充参数训练。<br>
        • RoboScript 从单示范在模拟器演练，将步骤、角色和反馈写入记忆；部署前冻结，并通过数据隔离测试新场景及跨本体适配。<br>
        • RoboTwin 2.0 全部 50 任务平均成功率 83.4%，并展示实体双臂迁移；主要证据来自模拟任务，不能外推为所有现实操纵任务的可靠性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-09</td>
      <td style="width: 55%;"><strong>Activation-Guided Graph Retrieval for Cognitive Memory Reconstruction in Language Model Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.13127"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出以激活条件的记忆可用性补充查询相关性排序，将证据路径重建作为召回目标。<br>
        • 请求和目标线索激活授权图，传播与扇出衰减约束遍历，递归生成线索并重建类型化证据图。<br>
        • 提供成本分析、消融与可证伪协议，未报告基准测量；若等预算简单重排器达到相同因果/时间恢复表现，核心主张需收窄。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-08</td>
      <td style="width: 55%;"><strong>EASE-KV: Diagnosing the Gap Between Memory Availability and Effective Use</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.11299"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EASE-KV 诊断记忆可访问但未被有效利用的差距，分离编码、证据分配与监督。<br>
        • 固定候选记忆比较因果与块对角编码，再对相同存储状态进行证据导向分配及结果监督。<br>
        • 因果编码的组合任务准确率高约 25 个百分点，LongMemEval 分配实验由 31.2% 至 38.4%；这些诊断条件不等同于可直接部署的通用提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-08</td>
      <td style="width: 55%;"><strong>Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.11509"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SimplEvo 将单示范任务记忆与从训练情节修订的有界工作记忆结合，使冻结 MLLM 在新布局执行。<br>
        • 从单示范生成无坐标任务记忆，回顾执行结果提炼程序、完成条件与恢复教训；测试阶段冻结两类记忆。<br>
        • EBench 上成功率由 46.7% 提升至 81.7%，RoboDojo 成功率为 69.63%；记忆可迁移至较弱模型，但测试冻结限制了结论的在线适应范围。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-08</td>
      <td style="width: 55%;"><strong>Self-Indexing Latent Memories for Access-Aware Continual Instruction Tuning of LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.11684"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TILA-CT 将持续学习中的记忆保存和任务寻址联合建模，减少知识已保留却无法访问的问题。<br>
        • 冻结主干，构建任务私有潜在记忆与适配器，从因果前缀聚合信息并注入任务上下文，以提示路由选择记忆。<br>
        • 八任务流程中最终分数 63.98、遗忘 1.38，路由准确率 93.9%；oracle 路由仍高 1.21 分，结果限于所测任务顺序与骨干。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>TimeTraveler: Temporal Strategy Planning with Time Dictionary for Streaming Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10337"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TimeTraveler 用时间字典保留流式视频细节，将回忆与未来观察纳入时间策略。<br>
        • 持续写入结构化时间戳描述，查询时规划过去检索、当前读取或等待未来证据。<br>
        • 在流式视频问答基准上报告改善；所读摘要未给统一增益，不能将记忆保留等同于所有视频事件均可正确召回。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>From Reflection to Co-Evolution: Self-Evolving Agents with Locally Verified Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10382"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Anchor 在存储反思前检验其局部因果价值，减少无效经验长期传播。<br>
        • 定位关键执行步骤，对同一上下文做有无记忆重放，以收益幅度和来源角色一致性筛选，准入后用于后续任务。<br>
        • ALFWorld/WebShop 报告最高 19.9% 成功率与 17.2% 分数提升，Qwen27B 记忆卡减少 41%；局部重放不能保证所有目标任务迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10439"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MixUA 研究执行经验应由谁记住及共享，在效用和隐私之间选择记忆作用域。<br>
        • 从独立用户—智能体轨迹提取教训，分配配对、用户、智能体或全局范围，供后续交互复用。<br>
        • CrossLearnBench 的五用户七智能体设置中通过率较无记忆高 16 点、较全局记忆高 5 点；报告隐私泄漏上限 0.02%，仅适用于所测协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10477"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PatternBloom 将执行中反复出现的推理路线外化为跨问题可复用的流程记忆。<br>
        • 从高信息奖励轨迹提炼、合并类型化图模式；第二阶段用模式奖励训练读取策略，并在该阶段与部署时冻结记忆。<br>
        • 7B 模型相对 R1-Searcher 的 OOD 平均 EM 高 15.0 分，去记忆消融和跨骨干迁移支持其作用；部署未在线更新模式库。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>EgoVeil: Personalized Privacy Reasoning for Egocentric Video</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10578"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EgoVeil 用显式用户偏好记忆支持视觉隐私的持续个性化，分离共享推理能力和个人证据。<br>
        • 检索先前确认的观察/动作记录，新反馈经关系判断去重、添加或停用冲突项，按时间顺序提供给后续决策。<br>
        • 十用户跨用户评测达到 91.93% 平衡准确率、84.42% 遮挡召回；基础推理器加入记忆由 74.59% 至 85.23%，样本规模和受控反馈限制外推。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>On the Geometric Bottlenecks of Cross-Lingual Knowledge Editing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10646"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析关联记忆编辑为何不能可靠跨语言传播，区分键对齐和目标值残差障碍。<br>
        • 对 ROME、MEMIT、AlphaEdit 的传播几何作平行/正交分解，并比较仅源语言修正与对比式键对齐。<br>
        • 结果支持较大的正交残差构成瓶颈；键对齐仅部分改善迁移，值不匹配仍存在，不能视为通用跨语言编辑解法。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>TransMem: Transition-Aware Retrieval for Evolving Personal Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10683"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TransMem 让个人记忆检索显式考虑偏好演化，避免只按语义相似度读取旧事实。<br>
        • 以主题图表示细化、矛盾和替代关系，先检索事实锚点，再自适应扩展被接受的转移记录。<br>
        • 在 PersonaMem、PersonaBench 与两种 Qwen 设置中优于比较方法，并检查时间顺序和固定跳数对照；摘要未提供统一数值增益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>Hallucination-Guided Unlearning: Using Hallucination Traces to Reveal Overfitted Memories</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10697"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HGU 用幻觉轨迹定位过拟合记忆，为选择性参数遗忘提供线索。<br>
        • 以证据共识识别无支持片段，定位高责任 MLP 神经元，通过紧凑门控与效用 KL 约束删除目标影响。<br>
        • TOFU forget05/10 平均指标为 0.7221/0.7699，并报告 WMDP 的遗忘与保留指标；遗忘收益需结合保留效用解释，非完全擦除保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10748"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • REINS 将经验证的语言规划承诺固化为未来场景可检索的规则记忆，减少重复调用 LLM。<br>
        • 缺配场景生成候选规则，按近期窗口校准并通过前向 rollout 验证后写入图数据库；按内容哈希合并重复项。<br>
        • 报告超过 98% 合规率及 1.9–4.6 ms 战术层延迟；准入依赖学习动力学，调用率递减论证带有分布平稳假设，不构成真实驾驶安全保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-07</td>
      <td style="width: 55%;"><strong>Remembering to Reason: Structured Memory for Scene and Workflow Understanding in Robot-Assisted Surgery</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10917"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemSurg 用结构化语义记忆支持手术场景与工作流理解，保留跨时间实体联系。<br>
        • 构建时间戳图及时间/实体链接，按任务检索并为冻结模型提供上下文，另评估匹配训练条件。<br>
        • 报告 GPT-4o 相对 SurgRAW 高 10.43 个百分点，匹配 Qwen3-VL 训练高 6.52 个百分点；这些是基准结果，不是临床安全或有效性验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-06</td>
      <td style="width: 55%;"><strong>ASCENT: Scale-Complementary External State for Frozen Long-Context Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.10175"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ASCENT 检验记忆容量与读取模型规模是否互补，避免把外部记忆收益归结为单一规模因素。<br>
        • 因果写入器维护嵌套类型状态，以有界查询读取；用记忆容量和读取器规模的因子设计比较准确率与负对数似然。<br>
        • BABILong 16K 上 0.5/1.5/3B 准确率分别增加 10.50/78.88/82.63 个百分点，但 3B 至 7B 的准确率互补减弱；结论受指标饱和与模型范围限制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-06</td>
      <td style="width: 55%;"><strong>HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.09355"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HiMEM 将 VLA 执行情节整理为可复用语义记忆，联合研究跨情节巩固、冗余剪枝和多级记忆组合。<br>
        • Qwen2-VL 提议子目标切分，模拟器或人工记录核验局部成败；从条件和操作抽象规则，剪枝保护稀有失败和来源账本，并以版本快照提供情节检索与语义约束。<br>
        • LIBERO 上 pi_0 平均成功率从 91.88% 提至 98.20%，并在 LIBERO-Plus 和多个骨干验证；结果依赖可核验的执行证据，不等同于任意真实场景下的自主经验正确性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-06</td>
      <td style="width: 55%;"><strong>ENGRAM: From Agent Experience to Weights through Verified Consolidation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.09472"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ENGRAM 将经验训练准入与外部记忆释放分离，避免未掌握技能被拒绝训练，或训练后过早丢弃仍有价值的指导。<br>
        • 用学生掌握程度或成功教师示例准入 ETG 轨迹训练；在预留探针上比较更新模型无情节检索与原模型有检索，仅对满足相对及绝对门槛的技能归档外部记录。<br>
        • 交互和推理实验优于冻结权重 ETG，受控比较中验证后释放接近全部保留、优于立即及等预算随机释放；失败验证的技能仍保留检索，摘要未给出统一幅度。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-06</td>
      <td style="width: 55%;"><strong>Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.09807"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以成对实验检验对话事实压缩是否优于保留转录的检索增强生成，直接分析记忆保留内容与丢失措辞的取舍。<br>
        • 在 LoCoMo 的 1,985 个问题上固定存储、生成器与裁判，逐行配对两种答案，并对 512 个不一致样本进行 McNemar 精确检验。<br>
        • 常用四类问题得分为 71.4% 对 64.6%，提示 token 少 34%；加入对抗类后优势仅 2 点且不显著，长措辞答案反而更差，另报告四项负结果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-06</td>
      <td style="width: 55%;"><strong>BEV3SR: Evidence-Aware 3D Spatial Reasoning from Video</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.09816"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • BEV3SR 将逐帧、局部视角的视频观察转为可查询的度量鸟瞰场景记忆，为 VLM 空间问答提供持续可用的对象记录。<br>
        • 问题形式化器确定参考坐标系、空间约束和证据需求；几何分支直接读取 BEV 记录，视觉分支按对象索引检索支撑 RGB 帧供 VLM 判断。<br>
        • 在多个三维场景问答基准和 VLM 骨干上，16 帧预算下均优于对比设置；方法依赖 RGB-D 与相机参数，摘要未给出统一数值增益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>The Gating Mechanism of KV Cache Eviction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.07605"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析可学习记忆淘汰门为何在语言建模损失下降时仍收敛于近常数评分：密集训练骨干偏好不改变原注意力。<br>
        • 通过限制可分配门质量并蒸馏密集模型输出打破无操作解；把被淘汰历史的质心放入同一 softmax 读取，以恢复外置记忆难以校准的注意力质量。<br>
        • Qwen3-8B 在 75% KV 压缩时 RULER 8K 为 90.14、LongBench 为 46.03，仍比完整缓存低 3.72/1.36 点；质心不能替代必须保留的精确证据。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.07631"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MEMOIR 联合管理压缩前证据保护与使用后重要性更新，防止合并丢失证据和静态优先级持续偏爱过时记忆。<br>
        • 周期离线合并前由裁判门检查可答性，查询后用置信门控归因更新召回优先级，并以 UCB 式探索补偿曝光不足的记录。<br>
        • 1,905 个 LoCoMo 问题上完整检索栈 recall@5 比余弦高 11.92 点，部署可用反馈增加 1.50 点；合并仅缩库 1.42%，100 次独立审计零损失对应的单侧 95% 上界仍为 2.95%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>ReConMem: A Graph-Based Dual Memory System for Repository-Oriented Conversations</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.07759"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ReConMem 用相互关联的语义和结构双图协调代码助手的对话历史与仓库上下文。<br>
        • 持续维护蒸馏对话及代码实体的跨图联系，通过代码草稿对齐查询、图内及跨图扩展，再按结构粒度压缩召回代码。<br>
        • LoCoEval 单跳/多跳 Pass@1 较最强基线提高 7.917/7.292 点；CodeAssistBench 正确与部分正确率分别为 27.61% 和 44.03%，证据限两类仓库对话基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.07820"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Axis-LoRA 发现冻结嵌入对个人记忆的时间、地点等变化不敏感，输出端投影也无法恢复缺失信号。<br>
        • 分析四个记忆轴各自的注意力头模式，在嵌入模型内加入四个 LoRA 分支，并用查询门组合，从小规模轴反事实样本学习。<br>
        • 三个嵌入模型在 LongMemEval、ATM-Bench 和 LoCoMo 等评测上，论文报告四项评测平均 R@10 提高 1.28–1.56 点；这是检索收益，未等同于最终问答准确率改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>Enhancing Local and Global Structure in Compressed AI Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.08341"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究智能体记忆向量压缩只保留近邻却破坏全局结构的问题，关注其对归并、删除和主题比较的影响。<br>
        • 同时测量局部与全局保真度，从近远排序违例界导出 LAQ 的 hinge 目标，仅优化 OPQ 码本并保持字节、旋转和搜索设置一致。<br>
        • 52 次留出实验中全局保真度均提高，13 个记忆-编码器组的符号检验 p=8.5×10⁻⁴，并保持证据召回；这些结构与操作指标不等于所有下游代理任务的端到端收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.08433"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MedGraph 针对长期医疗对话记忆的三类错误：陈旧状态、混入他人事实和遗漏必要安全信息。<br>
        • 从会话提取带日期和人物归属的事实，保留状态链；按查询时点读取患者链并补入原始对话，同时每次提供完整已记录安全事实档案。<br>
        • MedMemoryBench 上 GPT 与 Qwen 骨干分别超过五种基线中最强者 10.5 和 10.4 点；结果是基准问答准确率，不能视为真实临床有效性或安全性验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>Decision Context: Persistent Behavioral Learning for AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.08644"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Forge Decision Context 将跨会话的人类纠正和工具失败转化为行为规则，研究表示、触发与注入位置如何影响后续执行。<br>
        • 编译纠正链为带前置条件的 RULE，去重合并并覆盖同用户旧规则；跨用户冲突按主体或多数决解决，无多数时弃权，在决策节点渐进注入。<br>
        • DC-Bench 的 71 场景、九个维度上合规率为 95%，朴素检索为 55%，每查询注入 token 约少十倍；累积架构比较未隔离各组件作用，基准只覆盖两个领域。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.08718"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将长期记忆作为会话推荐架构的核心，使跨会话意图影响 LLM 路由和语义查询，而不是每轮独立推荐。<br>
        • 编排器协调意图细化、查询构造和交互流，通过跨会话记忆、多轮模拟及监督交互实验评估，并用 SCS 衡量语义一致性。<br>
        • Amazon Reviews 实验中记忆恢复显式查询差距的最高 63%，监督编排使接受率增加 28.9 点；LLM 重排未改善 Hit@K，候选检索到展示之间仍有瓶颈。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>Jacobian-Causal Memory Control for Persistent Memory in Language Model Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.08779"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • JCMC 将持久记忆选择定义为对当前推理行为的受控干预，而不仅是相关记录检索。<br>
        • 在共享行为测量空间预测干预影响，以目标效果及副作用预算选择记忆，再比较预测与实测效果来保留或回滚。<br>
        • 在光滑性和有界估计假设下给出局部近似、可达效果、选择遗憾与记忆交互界；论文无基准实测，只提出成对反事实估计与等预算比较协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-05</td>
      <td style="width: 55%;"><strong>Aligning, Fast and Slow: A Control-Theoretic Oversight Framework for Long-Horizon Trajectories and Maintained Deployments</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.08781"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出快慢双环监督：即时检查动作，同时审查会被后续任务继承的持久记忆变化。<br>
        • 慢环在记忆更新准入前核对章程和已批准版本，与动作门及周期校正协同；理论保证需要误差、检查间变化和可执行干预的显式假设。<br>
        • 编码压力测试严重度由 0.325 降至 0.117，解决问题 33/120 对无门控的 35/120；交易改善伴随拒绝全部记忆更新，实验仅验证组件，未建立完整部署保证或普适选择性学习。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-04</td>
      <td style="width: 55%;"><strong>FlyHash for LLM Agent Memory: An Empirical Validation and a New Application</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05791"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将FlyHash应用于语言智能体记忆检索并审查比较协议。<br>
        • 以匹配位数、多种子和真实相关性标签比较随机投影竞争编码、SimHash及HNSW。<br>
        • 质量优势成立，但常规规模下HNSW的延迟和存储更优；不把每比特质量误当实际效率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-04</td>
      <td style="width: 55%;"><strong>Can LLM Agents Learn to Test? Maintaining Scoped Experience as Testing Evidence for Mobile GUI Testing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05873"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出AdaptiTest的经验维护契约，强调回忆仅是建议。<br>
        • 为执行经验保留范围和轨迹来源，规定确认、重验证及撤回，并限制持久写入角色。<br>
        • 小型内部子集为18/18对3/18，但控制条件与跨会话探针存在限制，部分机制未端到端实现，不能推断通用优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-04</td>
      <td style="width: 55%;"><strong>Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized Retrieval-Augmented Generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05900"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Weaver，处理分散且条件化的历史偏好记忆。<br>
        • 双层图连接意图依赖与检索轨迹，按信息缺口继续查找，并区分互补证据、替代支持和同范围冲突。<br>
        • 在PersonaMem等个性化基准改善证据完整性与回答质量；未据摘要断言跨部署普适性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-04</td>
      <td style="width: 55%;"><strong>Reglos: A Self-Evolving Personal Memory Agent with Recursive Self-Improvement</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.06049"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Reglos，结合演化个人记忆与受控harness改进。<br>
        • 每轮追加用户记录并处理偏好替代，由跨模型家族批评器筛查补丁，冻结评测器决定后续接纳。<br>
        • Qwen配置在PersonaMem-v2和LongMemEval-S得61.3%与84.0%；结果是整体系统比较，非所有组件的独立收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-04</td>
      <td style="width: 55%;"><strong>SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.06445"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出SumOne，用轨迹自身学习可移植摘要记忆。<br>
        • 冻结重建器根据摘要恢复随机遮蔽的原轨迹，以重建质量和长度惩罚训练独立摘要器。<br>
        • 搜索与软件工程任务的估算推理成本降低约78%和75%，伴随小幅性能下降；同一模型可跨harness迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-04</td>
      <td style="width: 55%;"><strong>PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.06768"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出PyRUA-REAL，将真实物理探索沉淀为持久经验和程序技能。<br>
        • 分层保存条件、尝试结果和代码；研究员记录适用限制，工程师在新环境检索、改写并重新测试。<br>
        • 八任务迁移对照由21.3%升至40.0%，仅五项受益；整体系统成功率不能全部归因于记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>Anchor: Augmented Cross-Layer Recurrent State for Long-Context Retrieval in Test-Time Training</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.04327"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Anchor，利用检索能力集中于少数层的现象。<br>
        • 只在锚点层布置TTT记忆，跨层共享一次写入的状态，再通过各层学习到的映射读取。<br>
        • Llama与Mistral上召回提高2.3–3.1倍且状态缩小十倍；结果针对所测线性化混合模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>Sketchpad: certified exact arithmetic with a small vision-language model</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.04434"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Sketchpad，以受限工作记忆访问获得任意长度算术的可证明性。<br>
        • 模型每步读取三格视图并写数字及进位；Lean证明把全输入正确性化为有限视图集检查。<br>
        • 设备上2,446种视图全部通过；保证依赖固定运行协议和验证条件，不代表一般推理正确。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>CogniLife: Continuous Cognitive Distillation for Deployed Multi-Expert Agent Marketplaces</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.04483"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出CogniLife的跨专家记忆归属与持续修订设计。<br>
        • 区分Creator Profiles与Expert Journals；已部署部分支持有范围抽取、有效期、来源记录和可逆整合。<br>
        • 跨专家路由尚未实现或评测；85任务的整体配置分数不能证明冷启动缓解、跨专家迁移或长期蒸馏。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>The Right Source Is Not Enough: Understanding History Interference in Speech-LLM Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05124"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究无关历史音频为何在目标证据仍存在时干扰回答。<br>
        • 通过屏蔽来源访问及低维因果干预，区分直接读取、候选状态传播、来源角色与答案值。<br>
        • 开放问答与选择题呈不同干扰路径，联合角色和值干预恢复最多；证据来自MOSS-Audio及MiMo-Audio。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05313"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MDSKILL，减少技能记忆内化中的噪声、冲突与冗余。<br>
        • 按状态定位、行动规划和执行控制分解记忆，动态筛选技能，再把分支知识自蒸馏到共享策略。<br>
        • ALFWorld与WebShop报告最高7.1%和8.1%提升，消融支持内化作用；结论限于三项智能体基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05319"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出HARP，补齐双侧画像记忆及后续反馈同步。<br>
        • 构建物品画像，在检索侧使用画像同质性信号，并通过单次反思更新用户描述。<br>
        • 四个数据集Hit@1相对最强公布基线提高6.9–24.0%；反思有额外权衡，检索门控贡献最大。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>A Circuit for In-Context Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05344"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 识别上下文学习的门控键值记忆电路。<br>
        • 中层头向标签位置写类别键，上层头匹配并读出标签；通过激活补丁、消融和转向检验门控及近因抑制。<br>
        • 三个3–4B模型出现共同电路，并报告扩展检验；主要结论针对所设少样本分类任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>Route to Remember: Adaptive Memory Selection for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05636"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究把权重记忆作为低上下文开销的长期事实存储。<br>
        • 用记忆条件教师进行在策略自蒸馏，再以验证后重生成路由结合文本与权重记忆。<br>
        • HaluMem上达到或超过强文本基线且减少读入token；证据限于所测事实记忆协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-03</td>
      <td style="width: 55%;"><strong>Prospective Memory for Proactive LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.05731"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Pro-Memory，区分记住意图与适时行动。<br>
        • 把待办目标关联证据和激活条件，随新观察判断介入，并按实际动作或解决证据更新意图状态。<br>
        • 两个主动协助基准上跨骨干提高表现并限制多余介入；结论来自所测延迟意图场景。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02361"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将智能体记忆形式化为受容量约束的递归过滤。<br>
        • 以可执行权限策略和成对历史比较全文、检索及显式状态，分开模型解析与规则更新。<br>
        • 256事件下解析加规则过滤达80–89%，有效时域随读者能力改变；依赖选择检索可匹配部分结果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>EvoMemState: Evolving Memory State for Personal Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.03743"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出EvoMemState，使个人记忆从独立事实转向演化状态。<br>
        • 用本体提取事实及有效范围关系，再通过强化学习生成请求特定推理状态，指导事实使用。<br>
        • 在长期对话和记忆使用基准改善检索完整性与回答准确率；证据范围为所报告实验。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>RecGroupMemory: Feedback-Aware Cohort Memory for E-Commerce Recommendation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02453"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出RecGroupMemory，分离群体记忆构建和反馈修订。<br>
        • 用前一天结果更新决策指导，通过验证保留选定源值，供编排语言模型后续使用。<br>
        • 特定低购买力用户比较中，无反馈和有反馈记忆分别增加1.58%及1.78%的引导交易用户；不外推至全部用户。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>Chain on Demand: Deferred Evidence Organization for Long-Term Conversational Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02480"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Chain on Demand，将证据组织推迟到查询时。<br>
        • 在固定锚点预算中结合相关性、词法多样性和新覆盖词项，再确定性恢复同会话邻域。<br>
        • LoCoMo非对抗题准确率82.2%、全量76.3%，LongMemEval-S为86.6%；底层记忆保持不变。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02660"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出HeLM，以显式语言保存非马尔可夫操作所需历史。<br>
        • 分解事件检测与事件触发记忆更新，按层组织语言状态并跨任务边界保持上下文。<br>
        • 10类真实任务、56变体中情节内成功率提高12.8个百分点；组合任务子目标成功率78%，限于所测机器人场景。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02912"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出StateGraph，修订事实时同步检查依赖结论。<br>
        • 从历史恢复依赖边，用反事实验证区分支持关系和语义相关，仅在严格依赖失效且无替代支持时使状态失效。<br>
        • 50个人工构造案例中级联越深优势越大；属于初步受控证据，公开记忆基准多数结果相近或更高。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>Top-$k$ Retrieval Leaves Memory Value Undetermined</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.03289"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 证明常见top-k检索日志未必能确定单条记忆的价值。<br>
        • 根据各记忆及成对共同检索计数分析可识别性，LEDGER只估计可确定的Shapley值并主动改善日志信息。<br>
        • 55种标准基准配置均不能确定记忆价值；主动检索提高可识别性，但HotpotQA准确率下降2.6个百分点。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.03826"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析检索与患者轨迹记忆在不同时间转变中的作用。<br>
        • 按持续、新增和复发诊断分解评测，LONGINUS保留双视图共识并对分歧作盲来源裁决。<br>
        • 四个LLM在MIMIC数据上多数转变指标改善；重复上次就诊的启发式仍很强，不能据此证明临床有效。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>From Benchmarks to Behaviors: A Framework for Auditing AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.03939"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以TRACE框架审计用户记忆如何影响智能体引用来源。<br>
        • 固定问题及搜索结果，操纵简短用户记忆，并记录输入、执行和输出以隔离来源选择变化。<br>
        • 出版者偏好使前三引用出现率增加33–39个百分点；特定不信任记忆也提高错误信息来源引用，效应随模型变化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-02</td>
      <td style="width: 55%;"><strong>WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.04003"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出WASP-Mem，让智能体将执行经验整理为互链程序记忆。<br>
        • 从成功与失败轨迹及反馈持续整合wiki，受控比较摄入范围、整理方式、反馈和迭代轮次。<br>
        • TheAgentCompany通过率提高4.6–6.1%、存储减少57–61%；人工诊断价值高于额外自评轮次，限于该任务环境。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>Can Large Language Model Agents Learn by Watching Tutorial Videos?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01460"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出TAL，将教学视频变成可持续扩展的tutorialbook记忆。<br>
        • 用视频问题挖掘和对抗式修订维护结构化记录，按目录树结合推理检索。<br>
        • 在72段棋类教学视频及另一领域验证，棋局开局比较中69%占优；结论限于所测任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>Meta-memorization and memorization scaling laws in transformers</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01564"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究Transformer为何随规模增加而更快记住新序列，提出元记忆效应。<br>
        • 在随机二进制序列上分析注意力头传递位置无关信息、MLP存储序列及注意力瓶颈。<br>
        • 复现容量和学习速度规律；随机序列证据不能直接等同自然语言知识泛化。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01695"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出SPAR，把销售经验维护为可检验策略假设。<br>
        • 内环以情节记忆适应商户，外环通过因果归因和假设驱动更新共享手册，区分策略错误与外部因素。<br>
        • 超过20万商户的线上A/B测试报告转化提升15.8%；结果属于特定平台整体系统，非所有记忆组件的独立因果效果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>Evolving Memory, Learning to Meta-Control: Test-Time Adaptation for Experience-augmented LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01747"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出OMCE，同时演化经验记忆和使用控制策略。<br>
        • 上下文bandit根据检索信号选择直接执行、情节、指导或蒸馏，并用任务反馈更新记忆库与路由。<br>
        • 四骨干四基准首次成功率最高提高20.5个百分点；相对ACE的token节省依赖报告配置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>MemRole: From Memories to Decisions for Long-Horizon Reasoning in Role-Playing Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01778"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MemRole，显式连接历史经历、动机与当前决策。<br>
        • 将推理分为情境理解、记忆激活和策略规划，用角色及时间约束记忆池训练，再以自批评蒸馏改进。<br>
        • 32B模型的记忆角色扮演分数提升15.2个百分点，并改善动机识别；证据来自小说衍生及角色基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>Hippocampal consolidation without replay in fully fine-tuned networks</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01952"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出DeltaHippo，用训练期海马式索引保护持续学习中的知识。<br>
        • 保存输入子空间、能量及残差，在优化器前后限制更新方向；推理时移除记忆索引。<br>
        • 语言模型的方向旋转和断读消融显示内容决定保持；TACRED收益不代表一般生成能力全面保留。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>SurgStream: A Workflow-Anchored Proactive Streaming Framework and Benchmark for Real-Time Surgical Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.01982"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出SurgStream，以工作流锚定多模态事件记忆。<br>
        • 稳定事件变化触发三元组记录，阶段结束时压缩为摘要，结合期限感知监督控制何时响应。<br>
        • 11.7K交互基准显示记忆和前瞻问答改善；基于视频任务评测，不构成临床部署有效性验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>TrackMem: Tracking Evolving Beliefs in Long-Horizon Financial Dialogue</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02001"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出TrackMem，跟踪长期对话中的信念演化。<br>
        • 按说话者建图，保留数值版本、实体分析视角和行为顺序，并引入FinLoCoMo测试失败类型。<br>
        • 15段对话765题上，失败模式宏平均73.9%对69.4%；数据规模有限，不代表投资决策质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>Do Embodied VLMs Actually Use Their Scene-Graph Memory?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02056"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出图交换诊断，检验VLM是否真正使用场景图记忆。<br>
        • 以另一情节的图替换当前记忆，比较文本输入、图编码及逐节点token融合对回答的因果影响。<br>
        • 文本记忆使路线题提高30个百分点，逐节点图输入恢复8.3个百分点；冗余文本会让模型忽略图。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>Do agents need to sleep?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02216"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出借鉴睡眠选择机制的智能体记忆整合论点。<br>
        • 将ringing、resonance和renormalization映射到数字记忆操作，针对漂移、错误传播与容量饱和提出预测。<br>
        • 属于概念性、可证伪假说；尚未通过实验证明比其他整合机制更有效。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-01</td>
      <td style="width: 55%;"><strong>When the Text Is Silent: Memory Shortcuts and the Validity of LLM Annotation under Evidence Insufficiency</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.02273"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究证据缺失时参数记忆取代当前文本的捷径。<br>
        • 995名公众人物及匹配控制构成反事实文本，操纵证据、奖励与评估压力，并测试姓名提醒和遮蔽。<br>
        • 捷径主要在证据缺失而非冲突时出现；事实正确的标签仍可能无文本依据，缓解有属性相关权衡。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-31</td>
      <td style="width: 55%;"><strong>Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.00779"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MemSidecar，把记忆调度从主智能体任务执行中分离。<br>
        • Hooks按事件条件交付绑定记忆，Foresight并行预测查询并缓存经匹配和有效性检查的结果。<br>
        • 两种模式在MCP-Persona分别得41.23%和44.34%，并减少成本与延迟；两者可独立选择。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-31</td>
      <td style="width: 55%;"><strong>Pulse: Long-Horizon Tasks Need Streaming Personalization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.00988"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Pulse，让个性化记忆随长任务执行持续介入。<br>
        • 独立轻量记忆智能体监测新需求和偏好冲突，并通过强化学习优化介入时机与内容。<br>
        • 在π-Bench与MCP-Persona分别得71.9%和46.4%，并改善执行效率；收益限定于报告基准。
      <