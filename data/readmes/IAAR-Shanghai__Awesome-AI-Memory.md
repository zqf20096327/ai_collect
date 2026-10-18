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
[![Papers](https://img.shields.io/badge/Papers-1162-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
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
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21091"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemComposer 学习当前问题应使用哪些经验、多少条及何种顺序。<br>
        • 利用完整代理交互的成功反馈，以 ExPO/GRPO 训练记忆组装策略。<br>
        • 三个 τ²-bench 领域、两个执行器上优于各自最强基线，记忆 token 减少 16.9% 和 4.9%；迁移结果限于所测领域、执行器和记忆库。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21126"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • RoPERelay 研究选取记忆之后的地址几何如何影响保留证据读取。<br>
        • 固定内容选择和容量，压紧保序 RoPE 坐标、重定位 key 相位并同步后续 query。<br>
        • 两模型六选择器三记忆任务的 36 个比较中 32 个改善；LongMemEval-S 一组从 23.6% 升至 35.4%，请求时间开销约 1%–3%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21147"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • AiO-Mem 联合优化记忆搜索、写入和停止决策。<br>
        • 把历史编译为可溯源事件，独立过程奖励模型经监督和 DPO 训练，用动作平衡奖励驱动 PA-DAPO。<br>
        • 报告优于静态及 RL 记忆代理；摘要没有统一数值效应量，结论限于所测长期记忆基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>MemScope: Evolving Agent Memory Architectures through Localized Code Repair</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21170"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemScope 通过局部代码修复维护代理记忆架构，减少粗反馈导致的大规模重写。<br>
        • 联合检查轨迹、记忆状态和代码，在身份及记忆兼容约束下定位并修改。<br>
        • GAIA 轨迹加记忆反馈为 86.67%，仅轨迹为 70%；ALFWorld 未见任务从 50.75% 升至 71.64%，证据限于所测架构快照。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>An Agentic Framework for Proactive Robots with Procedural Assistance Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21211"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Procedural Assistance Memory 记录用户例行活动，支持高层 VLM 判断何时主动帮助。<br>
        • 预测器读观察和流程状态机，反思模型每天依据轨迹修订规则；VLA 执行任务，权重保持冻结。<br>
        • 五天桌面实验首次触发延迟由约 5 秒降到 1 秒，一次更新可修复习惯错配；证据来自小规模评估。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Memorilla: Latent Semantic Memory for LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21375"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Memorilla 将累积文档与交互历史压成潜在语义记忆供冻结模型使用。<br>
        • 文档编码一次，按查询检索组合为输入嵌入空间的 16 个记忆 token。<br>
        • 八个基准中五个最佳；FactKG 达 84.33%，TextWorld 成功率由全历史上下文的 18.6% 升至 24.2%，并非所有设置都获益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Writability and the Pathway: A Controlled Study of Knowledge Injection into Addressed Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21553"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究条件记忆知识写入、问题迁移和非目标行为保持的区别。<br>
        • GPT-2 对比行更新、投影更新与残差锚定，结合 Qwen 梯度写入及 DeepSeek 零阶实验。<br>
        • GPT-2 各组可复现训练补全但严格答案得分仍为零；Qwen 首 token 排名改善不等于完整答案成功，不能推出通用可写性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Reliable Knowledge Acquisition for Continual Learning Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21739"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • RIKA 将经验知识抽取与后续记忆准入分离，研究有害经验的可靠性。<br>
        • 四类知识经来源证据准入；推断主张等待后续支持，持续反对证据触发修订或遗忘，文件供后续任务复用。<br>
        • 六类任务流、四骨干上总体分最高，较最强基线高 0.046–0.081；收益随任务流变化，未证明高风险应用安全性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>TEM: Temporal State Tracking Memory for Large Language Model Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.21900"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TEM 保留变化事实的多个版本，使更新后仍能回答历史问题。<br>
        • 检索版本按来源排序并标记历史状态，用事件和原始对话补充结构事实。<br>
        • 420 道问题上历史标签使实体命中率提高 17.14–55.95 个百分点；两个骨干在 LoCoMo 优于会话 RAG，需结合指标和证据预算理解。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Memory as Weights: Internalizing Long-Term History for Streaming Videos</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22070"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MaLoW 将视频历史内化为参数记忆，使历史与当前观察不争用输入上下文。<br>
        • 递归 HyperNetwork 把新观察整合为固定 LoRA 权重，配套构建 56K 视频、381K 问答训练数据。<br>
        • OVO-Bench 回顾子集较已有记忆方法提高 3.9%–11.8%，同时有延迟开销；结论限于所测骨干与基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>EvoWeave: Composing Reusable Agent Experience through Operation Level Graphs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19381"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EvoWeave 保存操作级经验图，使历史片段按当前任务依赖组合复用。<br>
        • 反思分离实际证据与抽象操作，经过结构、能力及契约验证后更新；任务流从空记忆起步并跨后续任务复用。<br>
        • AppWorld Normal/Challenge 完成度为 51.91/27.99，较无记忆高 6.99/4.99 个百分点；检索开销和复用前提仍构成限制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19386"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • STRATA 把经验保存为技能、流程、元框架三级记忆图，针对任务增长退化与负迁移。<br>
        • 结果反思写入，按操作目标检索，结合社区归纳、垃圾回收及对比边维护跨任务经验。<br>
        • 四类交互基准和两骨干中平均分最佳；同系统内对比边使 ScienceWorld 从 78.7 升至 96.7，收益依赖所测协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>MemCode: Discrete Semantic Representations for Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19472"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemCode 将对话转为独立原子记忆，以离散语义关联补充向量检索。<br>
        • 通过可学习码本和同构语义量化建立共现召回路径，分离在线写入与异步整合。<br>
        • 在两个骨干的 LongMemEval-S、LoCoMo 实验中总体准确率最佳；每段对话构建约 40–130 秒，结论限于所测配置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19474"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合源证据访问与事件聚合，解决代理历史问题不能只靠相似检索回答的困难。<br>
        • Trajectory Memory 保留轨迹并构造可寻址阅读视图；TallyMem 增加事件账本、模型生成规范和确定性执行。<br>
        • 776 道 MINTEval 问题上 Qwen3-32B 精确匹配由 35.2% 升至 49.0%；AMA-Bench 增益仅 1.3 个百分点，受事件规范错误限制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>StateCraft: Augmenting Video World Models with Abstract-State Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19795"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • StateCraft 用语言模型维护可更新语义状态，保存画面外变化并条件化视频生成。<br>
        • VLM 读取当前节点、动作与历史，预测新建保持再访问和图差分，持续维护可编辑实体记录。<br>
        • 文件管理器实验验证再访问及编辑；采用首次访问初始化，3D 仅概念验证，微调存在域外泛化代价。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>EGCForest: Structured Agent Memory Organization for Enterprise Group Chats</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19836"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EGCForest 按工作流、说话者语境和产物生命周期组织企业群聊记忆。<br>
        • 从原始日志建立三种森林，用位置映射和稀疏桥连接视角，联合消息相关性与层级摘要召回证据。<br>
        • 三个聊天基准中优于所测 RAG 和记忆基线，较 MemOS 最多高 20.85 个百分点；最大增益不是平均收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19849"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DeltaStreamer 在问题出现前记录视觉变化，保留未知未来问题需要的证据。<br>
        • 持续观察写入记忆，查询规划器检索记录并按需重放帧，补充描述遗漏。<br>
        • OVO-Bench、StreamingBench 分别为 66.07%、59.53%，优于所比较方法；主动补证仍依赖历史帧可访问。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>MemDuet: Learning Dual-Process Memory for Long-Context Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.19928"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemDuet 将快速选证与慢速验证更新结合，协调长文档记忆准确率和效率。<br>
        • 小模型并行选取块证据，大模型按文档顺序更新记忆，经过监督、GRPO 和联合训练。<br>
        • 三个基准评估设置中较 RL-MemAgent 平均加速 9.74 倍、输出 token 少 73.91%；结果需与准确率效率权衡一同理解。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>Reflect After Failure: Brain-Inspired Self-Evolving Agents for Embodied Spatial Intelligence</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.20312"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HiMeco 从失败轨迹形成可维护策略和流程记忆，区分感知、探索与规划失误。<br>
        • 比较执行尝试并抽象技能，用证据契约和执行验证决定保留复用，仅在轮次间更新记忆。<br>
        • 报告 ESI-Bench 最佳表现，未再演化时 EmbSpatial-Bench 高 3.94 个百分点；结论针对所测空间任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>Cortex: Consolidating Context into Parametric Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.20399"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Cortex 研究移除上下文后如何保留其收益，同时保护非目标能力。<br>
        • 生成预期查询，将上下文输出蒸馏为低秩或结构化前馈更新，测试单次、批量和顺序巩固。<br>
        • 多数配置位于巩固保持经验前沿；14B 模型 50 次事实编辑后恢复 88.9% 上下文收益并保留 99.8% 非目标表现，不能外推所有任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>Continuum Attention</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.20586"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Continuum Attention 以连续记忆曲线积分替代离散键值寻址。<br>
        • 查询诱导指数相关密度，用闭式矩计算归一化读取和梯度，保留二次序列复杂度。<br>
        • 验证损失较 softmax、focal 分别低 0.0200、0.0480 nats/byte；额外切片支持收益，但大规模泛化未确立。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-14</td>
      <td style="width: 55%;"><strong>Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.20902"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ChainGraph 将安全分析发现保存为结构化图记忆，支持依赖链推理和证据追溯。<br>
        • MCP 暴露 Neo4j 类型节点和前后条件边，查询只返回决策相关子图，分离文档记录与推理状态。<br>
        • 合成 Active Directory 单次示例显示链式严重度变化和约 98% token 代理载荷减少；并非通用基准证明。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17544"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析把多步推理压缩为记忆复用后，事实变化如何导致陈旧回答。<br>
        • 以似然比监测失败、对实时推理验证效用，在变化时重启证书或使记忆失效，并给出安全复用的条件性界。<br>
        • 五种 LLM 的事实编辑实验中，常用计数器产生更多陈旧回答；安全收益依赖可验证结果和变化检测假设。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>MemAct: Streaming Spatial Understanding with Memory and Active Exploration</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17640"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemAct 将流式空间记忆与主动获取新证据纳入同一 VLM 推理循环。<br>
        • 模型增量写入结构化历史，按需检索记录和旧帧，再通过移动或转向补充证据并决定回答或继续探索。<br>
        • 约百万训练样例及 20,000 项主要问答评测支持效果，另有 2,000 项时机问题；作者报告优于所比流式基线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Keep Your Receipts: Trustworthy Cleanup of Agent-Built Knowledge Graphs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17719"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PolyGraph 研究来源撤回后如何可靠清理代理知识图谱记忆。<br>
        • 构造每项合并、边及摘要时保存证据组合收据，再用删除证据后的重新推导审计收据可信度。<br>
        • 细粒度收据优于整段平铺来源；在受控语料中污染查询降至 0.4%/0.8%，但模型自报收据并非天然可靠。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Explore with Memory, Learn without It: In-Context Exploration and Self-Distillation for LLM Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17734"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LEAF 用问题特定记忆改进强化学习探索。<br>
        • 每次验证后保存最近回答、奖励与反馈，在下一 rollout 前读取；通过自蒸馏将策略更新与有记忆探索分开。<br>
        • 四项基准和两个模型上探索约加速四倍，未见测试集准确率提升 1.59 和 1.83 个百分点；记忆主要作用于训练期。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17763"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 定义 Memory Echo：同源历史经反复检索回写获得过量证据权重。<br>
        • MEchoBench 测试产生、持续和纠错抵抗，FPA 按来源族去重、限制旧记录资格并以权威证据约束回答。<br>
        • 190 个问题的配对回放中，两种模型准确率分别从 0.825/0.782 升至 0.920/0.916；结论限于该受控协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Learning How to Remember: Memory Modality Selection for GUI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17928"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SwitchMem 研究 GUI 代理历史记忆模态为何应随步骤变化。<br>
        • 在每个交互步骤动态选择文字或视觉经验表示，取代全程固定的一种记忆模态。<br>
        • 在三个 GUI 基准上优于固定模态记忆基线；结果支持按步骤选择，而非任何模态普遍最优。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Provenance and Authorization in Autobiographical Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17935"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 把自传语言模型记忆中的来源混淆和授权误用表述为安全问题。<br>
        • 使用带类型记录、认证证明、独立策略通道与允许视图，分析完整性、非干扰及精确保留决策的摘要条件。<br>
        • 提供显式假设下的论证，以及 32 个合成案例的 576 个配对条件试验；不是现实人群心理结论。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Heading Hierarchy Reconstruction for Complex and Long Documents with Level-Wise Multimodal Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.18238"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为长文档标题层级重建引入按层保存的多模态记忆。<br>
        • 逐页处理时保留各层最近标题锚点及其视觉、文本和布局模式，作为后续页面判断依据。<br>
        • 新增含 250 份文档、11,212 页的人工核验基准，并在四个基准验证有效性；任务范围为文档层级一致性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.18427"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • RBC 用随机实验判断代理自行写入的教训是否真正有助于后续任务。<br>
        • 把相关教训成组随机纳入或排除，估计对成功率的影响，再在新练习任务上选择整理版、完整版或无手册。<br>
        • 两个记忆系统、三种模型及三个基准的平均成功率达 66.9%，完整手册为 55.5%；仍依赖练习任务代表性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-13</td>
      <td style="width: 55%;"><strong>MemoryVLN: From Ego-Aware Memory Representation to Cross-Context Memory Reuse in Vision-Language Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.18478"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoryVLN 围绕空间接地记忆构造和跨上下文复用设计导航系统。<br>
        • 用时间采样压缩历史，联合语义、几何与位姿表示，并通过分层记忆库、置信写回及 Top-K 检索维护经验。<br>
        • 在 R2R-CE 与 RxR-CE 上报告成功率约提升 2% 和 6.5%；证据限于所测导航基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-12</td>
      <td style="width: 55%;"><strong>Recall Begets Recall: Recurrent Memory Ranking for Personalized LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.16137"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ReMind 将个性化记忆排序改为可自行停止的循环召回。<br>
        • 每次召回的记忆扩充下一轮查询线索，充足性预测器判断是否已经积累足够证据。<br>
        • 在公开基准中优于所比记忆排序方法；效果体现查询适应的互补证据选择，摘要未提供统一增益数值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-12</td>
      <td style="width: 55%;"><strong>Error Correction in Trained TTT Layers</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.16268"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 剖析已训练 TTT 层的预测误差项如何参与快权重记忆更新。<br>
        • 推导不同目标的更新结构，并通过保留雅可比、匹配更新范数等干预区分代数形式与实际行为贡献。<br>
        • 在 100,303 个文学文本词元上移除预测项使困惑度约增 2.8–2.9%，冻结全部更新则增至 4.2–4.5 倍；证据范围有限。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-12</td>
      <td style="width: 55%;"><strong>Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.16414"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Purpose IR 区分任务证据可访问性与持久记忆保存授权。<br>
        • 把用户目的编译为有类型的语义数据流，仅允许经验证输出进入可复用状态，并在显式执行契约下分析隐私边界。<br>
        • 1,200 个案例上隐私达 99.6%、隐私合规成功率 83.3%；493 条 PrivacyLens 轨迹的安全行动率 77.3%，不代表无条件保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-12</td>
      <td style="width: 55%;"><strong>Scaling Unified Multimodal Models to Long-Horizon Interleaved Generation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17080"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以持久视觉参考扩展统一多模态模型的长程交错生成。<br>
        • 保存完整语义历史，选择检索场景相关视觉状态，并通过短程自回放适应不完美的生成历史。<br>
        • 在 LongMIG-Bench 上展示更长轨迹的角色和场景一致性；摘要未给出统一数值增益，结论依所测生成设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-12</td>
      <td style="width: 55%;"><strong>When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.17365"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究共享会话记忆中的客户目标如何串扰其他客户决策。<br>
        • 在受控双客户环境中探测 KV 缓存目标归属，并对特定注意力头的目标表示作因果消融。<br>
        • 20 个场景中 22% 的适用决策偏离当前目标；定向消融强于随机干预，但证据限于一个模型和合成环境。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-11</td>
      <td style="width: 55%;"><strong>EvolvAttack: Backdooring self Evolving VLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.15244"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EvolvAttack 研究只有在代理记忆演化后才激活的潜伏后门。<br>
        • 把视觉触发器与特定演化记忆状态耦合，使干净初始记忆下的静态扫描难以暴露攻击。<br>
        • 三种 VLM、四类代理流程和三种记忆演化策略下，攻击成功率从初始 0.5% 在百次交互内升至超过 95%；属受控攻击结果。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-11</td>
      <td style="width: 55%;"><strong>Recall What Is Missing: Composing Evidence from Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.15642"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemPursuit 把长期记忆读取定义为互补证据组合。<br>
        • 以稀疏凸查询重建的残差表示尚缺的信息，复用已有嵌入逐步形成嵌套上下文，避免逐对调用语言模型评分。<br>
        • LoCoMo 固定预算下 Top-10/20 准确率提升 7.2/5.5 个百分点，重排中位延迟比批量 BGE-v2-m3 快 32.9 倍；不等同全流程加速。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-11</td>
      <td style="width: 55%;"><strong>History Replays Itself: Unleashing Long-Context Capability in Linear Attention</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.15715"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • NoteBank 将循环计算状态与稀疏情节存储分离。<br>
        • 在未知未来查询时归档文本，用背骨原生特征写入和寻址，再通过原生前向回放读取证据，无需独立检索模型训练。<br>
        • 百万词元下六项 RULER 召回平均准确率从 1.7% 升至 70.3%，并扩展到多个模型和长期记忆基准；资源比值依匹配条件。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-11</td>
      <td style="width: 55%;"><strong>Engram Injection: A Study of Temporal Validity in Parametric Language-Model Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.15882"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Engram Injection 检验参数记忆能否同时存储事实并判断其时间有效性。<br>
        • 以 LoRA 存储事实、FiLM 提供时钟，与加性时钟、全历史提示和四条记录检索比较，并审计训练时间泄漏。<br>
        • 62 对更新前后问题中两类适配器均无完整正确对，全历史为 59/62、检索为 62/62；事实存储成功不等于时态选择成功。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14495"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究视频程序代理如何将修订经验转为持久教训和可执行规则。<br>
        • 对代码快照与修复差异建立对应，为规则保存通过及失败样例，并以人工决定和留出评估控制记忆更新。<br>
        • 111 个视频的研究发现教训能缩短修订循环，但未持续累积质量收益；还揭示评审顺序偏差，不能把偏好票数直接当改进。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14515"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出以任务依赖图统一协作与流程记忆演化的 SEPM。<br>
        • 共享黑板记录执行证据，验证后的动作和依赖形成可复用程序，并按效用创建、细化、特化或退役。<br>
        • 在两个协作框架的六个评测设置中均领先；AutoGen 下三项任务分数提升 29.85、25.86 和 13.00 个百分点。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>A Self-Defining Operator for Distributed Applications</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14547"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出能从故障处置中形成持久流程记忆的自定义运维代理。<br>
        • 将成功调查蒸馏为诊断手册和遥测检测器，检测器触发后检索适用手册并调用 LLM。<br>
        • 在 11 个开源微服务应用中，重复故障解决时间降低 52%；结论限于所测故障与应用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>GateSight: Recurrent Memory Anticipates Attention Memory for Query-Agnostic KV Eviction in Hybrid LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14754"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • GateSight 研究循环记忆能否提前预测注意力记忆的未来内容效用。<br>
        • 从 Gated DeltaNet 写入门、衰减与写入幅度预测 KV 保留价值，并按注意力输出门配置层间预算。<br>
        • 在两种混合模型和两项召回基准上，十分之一缓存下多数设置优于所比查询无关方法；不保证任意任务或压缩率下无损。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>How Should a Camera-First AI Agent Work?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14772"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出将短暂视觉证据的记忆截止期与较慢推理解耦。<br>
        • 用有界快路径暂存感知，再主动提交持久记忆，由多模态模型和工具延后推理。<br>
        • 以 MOT17 轨迹窗口和实测模型延迟做一致性检验；属于架构与有限验证，尚非完整真实交互系统证明。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>Representation Drift in Continual Learning: LoRA versus N-gram Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14921"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 比较持续更新原生 N-gram 记忆与 LoRA 对语言模型表示的干扰。<br>
        • 在相同七任务数据与预算下，仅更新记忆表、共享 LoRA 或逐任务合并 LoRA，逐层追踪通用及已学任务表示。<br>
        • 记忆表使通用表示漂移更小且稳定，但新任务获取较弱、存储任务仍互相干扰；不能把主干稳定等同完全不遗忘。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-10</td>
      <td style="width: 55%;"><strong>What Survives When Activation Steering Is Used as Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.14958"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 检验激活偏移作为跨会话记忆能保留哪些用户事实和偏好。<br>
        • 将经验引发的晚层状态变化存成偏移，以白化主题键选择召回，并比较不同写入参考。<br>
        • 无关回答约 98% 不变，但事实干净使用率至多 15%，远低于上下文的 96–98%；偏好方向还可能被参考选择反转。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-09</td>
      <td style="width: 55%;"><strong>Time Delay System for Sequence Modeling</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.12864"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以语义相似度决定历史延迟，构造可解释的内容感知时间召回。<br>
        • 结合可微语义延迟估计、对角状态空间和模糊语义调制；正文使用 256 维隐状态与最大延迟 30。<br>
        • 在 IMDB 分类和 CNN/DailyMail 生成实验中取得较好结果；正文承认评测范围有限且对超参数更敏感。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-09</td>
      <td style="width: 55%;"><strong>Temporal Evidence Forests for Long-Horizon Multi-Party Conversational Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.12874"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • T-Mem 用时间证据森林组织多方长期对话记忆。<br>
        • 先利用时间邻近性找回遗漏证据，再建模状态转换与支持关系，压缩低信息片段并序列化供回答使用。<br>
        • 在两个长期多方记忆基准上跨模型、领域及查询类型改善表现；结果限于所测交互设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-09</td>
      <td style="width: 55%;"><strong>DP-MIND: Differentially private memory-guided Long context Inference</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.13132"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DP-MIND 用可学习的紧凑记忆支持差分隐私长上下文推理。<br>
        • 对本地扰动输入分块处理，以答案正确性及记忆一致性训练构造策略，再本地修复受噪声影响的答案片段。<br>
        • 提供条件性隐私分析，并在最长百万词元的评测中改善效用；结论依赖所设隐私机制和测试环境。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-09</td>
      <td style="width: 55%;"><strong>Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.13267"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DREAM 以选择性功能遗忘修复 LLM 代理的被投毒记忆。<br>
        • 通过扰动重激活、异常诊断和动态抑制有害记忆，同时强化正常记忆，无需额外训练。<br>
        • 作者报告后门攻击成功率降低超过 95%，相对 A-MemGuard 最多加速 2.13 倍并节省 37.7% 词元；防御不等同完整删除保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-09</td>
      <td style="width: 55%;"><strong>Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.13277"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过词元级证据匹配改善助手对存储会话和文档的记忆检索。<br>
        • 把稀疏词元匹配聚合为记忆分数，并结合整段相似度；可选查询适配器保持编码器与记忆表示不变。<br>
        • 八项检索评测及长期记忆问答均有提升；Qwen3-Embedding-4B 查询适配后平均 Recall@10 和 NDCG@10 提升 13.3 与 14.3 个百分点。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-09</td>
      <td style="width: 55%;"><strong>Test-Time Memory Construction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.13348"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • T²Mem 将查询特定记忆构造推迟到推理阶段。<br>
        • 离线仅保存轻量事件元数据与原始对话链接，回答时逐步检索并组织跨会话证据。<br>
        • 在 LoCoMo 和 LongMemEval 的多个模型上优于强基线，同时降低离线构造开销；结果为作者报告的基准表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.12793"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • GAMMA 将机器人高层情节记忆分为 VLM 写入与推理两类代理。<br>
        • 结合空间检测、追加式文本记忆和机械视觉核验，对每条断言接受、延迟、纠正或拒绝，再生成接地子目标。<br>
        • 在 16 项记忆操作任务中接近固定策略的预言机上界，部分任务达到上界；结果仍依赖检测和核验接口。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>What to Admit and How to Present: Governing Persistent Memory in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11188"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将哪些记忆进入工作上下文与如何呈现它们分离，研究准入和呈现对安全性的独立作用。<br>
        • 整条记忆或类型化单元经属性裁定与确定性策略筛选，比较匹配准入预算和固定呈现的条件。<br>
        • 外部基准失败率下降 6.7、8.8 个百分点，但个性化失败增加，预注册条件未全部满足；安全收益具有任务依赖性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Gated Memory: Admission-Controlled Memory Formation for Conversational AI</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11270"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Gated Memory 在事实提取之前设置准入边界，保留原话中的临时性、条件和隐私语境。<br>
        • 通过准入与条件化补全两阶段生成带来源、类别、适用范围及时空信息的原子事实，禁止凭空新增实体。<br>
        • 固定检索和生成条件下，LoCoMo-10 的裁判准确率相对提高 2.6%；样本情绪密度特殊，外推需谨慎。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>REMORY: Learning Residual Memory for Context Compaction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11287"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • REMORY 在文本摘要后补充有界软记忆 token，保存后续决策可能需要的残差信息。<br>
        • 记忆网络同时读取历史和摘要，学习使冻结 LLM 的续写逼近完整历史条件下的行为。<br>
        • SummHay 用 5.2% 输入位置接近完整上下文联合分数，并减少代理重复工具输出；结果限于所测模型和任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11314"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CogMem 用人物、事件、概念、主张和事实分离来源归属与客观记录。<br>
        • 增量构建有出处的记忆图，巩固事实并协调有时间范围的矛盾主张，通过锚定、遍历、交集和证据落地重建上下文。<br>
        • LoCoMo 和 LongMemEval 上多跳、时间与更新任务表现较强，消融支持各组件互补；摘要无统一效应量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Beyond Sequences: Distilling Structured Decision Memory for LLM Recommendation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11501"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MARI 将用户以往决策中的目标、约束和权衡存为可解释的结构化决策记忆。<br>
        • 离线从异质行为和用户内容蒸馏记录，在线检索相关记忆增强 LLM 决策，分离构建和推理成本。<br>
        • 下一物品预测和困难选择任务优于所测基线；依据是离线推断的决策理由，不等同于已知用户真实动机。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Memory Type Varies: Empowering LLM Agents for Long-Term Memory with Diverse Strategies</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11573"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoType 通过区分记忆类型和查询类型，避免多类语料共用一种检索策略。<br>
        • TriMEM 提供类型标注，学习路由器选择对应记忆和检索方案，并分析统一策略的精度上界。<br>
        • 三个数据集上最高 Recall@1 改善 16.18%；类型划分和路由质量仍限定该方法的适用条件。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>DeltaReplay: Task-Relative Memory Reuse for Mobile GUI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11707"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DeltaReplay 将轨迹记忆的可用性定义为相对当前任务的逐步关系，而非整条轨迹是否匹配。<br>
        • 保存页面和动作转移图，把动作拆成通用操作与任务参数，再决定照用、替换参数或交还基础代理。<br>
        • AndroidWorld 和 SPA-Bench 成功率最高分别提高 10.3、25.0 个百分点；主要验证部分匹配轨迹复用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>MemTrial: Learning When to Trust Memory in LLM Portfolio Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11732"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemTrial 按经验对同日决策的边际改变赋予记忆信用，减少市场共同波动造成的错误归因。<br>
        • 用八种经验组合估计 Banzhaf 值，跨日期和相似经验做层级贝叶斯汇聚，并经未见日期验证后才采信。<br>
        • 五种设置的平均效用比最强经验学习代理高 21.2%；无效时保守锚定仍可能亏损，不能解释为投资收益保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>DPPM: Dual-Path Parametric Memory for Personalized Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11776"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DPPM 将参数记忆中的早期证据保持和顺序偏好更新分为互补路径。<br>
        • Evidence 路径汇聚历史表征，Delta 路径递归更新联想状态，融合生成与用户历史对应的 LoRA 适配器。<br>
        • 多骨干实验中 PersonaMem-v2 为 54.22%、PrefEval 为 86.79%；证据针对所测个性化任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11794"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Memento 3 把可修订环境假设存为自然语言规则簿，使语义记忆成为显式世界模型。<br>
        • 将规则编译成可执行代码，预测误差驱动修订；只有模型忠实性检查和逐格转移回放通过才接受更新。<br>
        • ARC-AGI-3 的 25 个公开游戏全部通关，Pong 仅测试三局；公开游戏和有限案例不足以证明通用自我改进。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.11920"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • QGMem 用事件中心的原子记忆和动态轨迹保存个人经历、状态变迁及当前状态。<br>
        • 混合召回与查询重排激活紧凑工作记忆，再构造局部图并编码为图 token 供 LLM 结合文本使用。<br>
        • 六个基准报告检索、多跳证据组合和冲突解决改善；摘要仅给定性汇总，未提供统一幅度。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Look Back, Think Ahead: Visual Memory on Demand for Efficient Multimodal Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.12060"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ViMoD 在紧凑视觉上下文之外保留可恢复细节，支持推理阶段变化时按需回看。<br>
        • 粗粒度组与原始细粒度 token 建立链接，路由器根据解码历史选择、保留或替换活跃细节组。<br>
        • 20% 视觉 token 预算下在八个推理基准胜过所测基线，平均归一化分数高 39%；实验主体为 Qwen3-VL-4B。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-08</td>
      <td style="width: 55%;"><strong>Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.12124"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Hippocam 按嵌套意图组织正在进行的工作，将已完成任务逐步巩固为持久经验。<br>
        • 递归压缩较早历史但保留原始交互，按需逐层恢复；被重新使用的经验与新经验共同巩固、补充和更新。<br>
        • 提出无需参数更新的记忆与学习架构；所读摘要未提供定量实验，效果不应视为已充分验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>Relevance Is Not Sufficiency: What Actually Closes the Evidence Gap in Long-Term Memory QA</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.09348"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • BFR 将召回目标从单条相关性改为能共同回答问题的充分证据集合。<br>
        • 固定平面记忆库下，按问题信息需求选择初始子集，再通过更深文本搜索、实体和会话视角补齐未见记录。<br>
        • LongMemEval-S 裁判准确率从 72.4% 提升至 82.2%，Turn Hit 为 91.4%；结论依赖固定存储和既定预算比较。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.09358"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • COOL 从长期人物—物体交互记忆推断所有权，支持带归属条件的机器人服务。<br>
        • 两个语言代理共享位置与事件记录，一个检索证据推断归属，另一个按信息价值和陈旧程度探索并刷新记忆。<br>
        • 离线、消融及真实机器人实验支持方法；不确定归属可标记共享或未知，效果受感知和跨时间身份关联影响。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>Learning Situation-Conditioned Thinking Policies for Long-Term LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.09590"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将历史推理经验转为情境条件的思考记忆，预测当前应激活何种思考而不不断扩充显式上下文。<br>
        • 跨独立情节分析临时经验，发现长程规律并巩固为新知识，由轻量策略调用、LLM 完成具体推理。<br>
        • 报告 DeepSeek 推理 F1 从 0.789 提升至 0.868；部分受控指标达 1.000，不能外推为开放任务完美表现。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.09832"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SkillForge 将技能视为可过时的流程记忆，以试用、激活、稳定和退役管理其生命周期。<br>
        • 基础模型回放先剔除低适应度技能，随后在 RL 中持续验证、稳定、变异和退役，与策略共同演化。<br>
        • 多个交互基准成功率相对最强基线最高改善 7.8%，并提供 5,000 余条生命周期记录；证据主要在训练期技能库中取得。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>HGP:An on-device personalized agent memory via hybrid graph storage</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.10071"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HGP 为异质长期记录建立混合图记忆，保留情节、语义和流程的类型与关系差异。<br>
        • 轻量分类器路由不同记忆图，以工作记忆状态轨迹表示当前约束，并增量更新用户档案。<br>
        • 两个基准中，PAL-Set 的 S-score 为 35.58，比最强基线高近 7 点；设备端通用性未由摘要充分展开。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>ExperienceIndex: Artifact-Grounded Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.10091"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ExperienceIndex 把以前任务发现的文档贡献和文档间关系保存为面向材料的持久经验。<br>
        • 单文档与文档对两类记录来自推理轨迹，经验检索帮助新任务找到完整相关材料，并可从强模型传给弱模型。<br>
        • 答案质量最高提高 11.0 点、在线费用最高下降 50.5%；跨任务转移在相同材料语料上验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>VideoEvolve: Co-Evolving Memory and Retrieval for Long Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.10183"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • VideoEvolve 联合改进记什么和如何召回，避免固定视频记忆与动态问题检索不匹配。<br>
        • 从低帧率概览出发，记忆与检索 Evolver 交替强化学习；瓶颈和能力反馈决定补充证据与训练方向。<br>
        • 多个长视频基准显示有效，正文明确语言/多模态模型承担记忆写入和检索；摘要未给统一效应量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.10533"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EngramEdit 把条件记忆作为独立可编辑知识接口，更新事实时保持 Transformer 骨干固定。<br>
        • 计算跨表达一致的目标记忆表征，联合修改共享 n-gram 嵌入，并对频繁复用项施加更强保护。<br>
        • 实验报告近乎完美编辑成功及多跳收益，同时大体保留无关知识；结论依赖所测条件记忆架构。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.10538"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Ledger 保持离开视野的物体位置、历史和文字细节，使助手可回答事先未知的空间问题。<br>
        • 按稳定停留位置组织带时间观察，多次证据才确认移动；语言模型读取保存的文本记录，无需重新观看原始视频。<br>
        • HD-EPIC 准确率从 29.7% 提升至 42.6%；跨场景串接仍暴露构建和召回失败，离线记录实验不等于实时部署。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-07</td>
      <td style="width: 55%;"><strong>MemoWM: How World Models Change What Agents Need to Remember</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.10778"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemoWM 按世界模型能够重建的内容分配经验记忆，只保留具有额外任务价值的信息。<br>
        • 以重建误差对后续任务的影响权衡存储成本，用共享预测补回省略内容，并计入模型参数成本。<br>
        • 五个基准平均准确率 42.42%，比最强基线高 2.62 个百分点，经验存储比 MIRIX 少 53.9%；总成本仍取决于模型容量与经验量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>AgentMemGate: Addressing Speculation Contamination in Conversational Assistant Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.07707"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • AgentMemGate 针对把未决计划写成既成事实的推测污染，控制用户档案记忆的写入边界。<br>
        • 将语句分为推测、完成事件、纠正及其他，推测须满足条件后才提升为记忆，并支持删除。<br>
        • 困难留出集污染率为 3.4%–5.7%，任务准确率提高 9–13 个百分点；档案字段匹配仍是主要瓶颈。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.07984"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PixelTriage 在记忆检索后决定哪些图像值得传入原始像素，而非一律用图片或文字代理。<br>
        • 小模型依据对话、笔记和缩略图预测像素的边际回答价值，以冻结 27B 模型的有无像素对照生成监督。<br>
        • 三个基准用 11%–23% 视觉 token 且无显著准确率损失，DMV 快 2.9 倍；该结果依赖所测回答模型和预算。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.08048"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DAEDALUS 无需预设任务或 oracle，从自生成练习构建可复用流程记忆。<br>
        • 探索者生成任务，求解者从失败提炼启发式，只有反复成功验证后才接受并巩固到测试时记忆库。<br>
        • 三个交互基准平均成功率最高提高 15.9 点、pass^5 最高为 2.2 倍；启发式可跨模型迁移，仍依赖探索预算与环境反馈。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>Test-Time Agent Evolution for Long-Horizon Legal Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.08138"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将部署时的案例经验召回、适配与巩固作为持续记忆演化，支持长程法律推理。<br>
        • 记忆更新配合按程序与行为规则校验的角色协作，在不更新模型参数的条件下复用先前经验。<br>
        • 五个基础模型在 J1-EVAL 和 LegalWorld 持续改善，消融显示记忆与协作互补；基准收益不等于现实法律决策可靠性保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>DeltaTTT: Layerwise Optimization for Nonlinear Recurrent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.08553"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DeltaTTT 针对非线性记忆单遍优化困难，说明串行状态依赖并不自动优于固定基点并行更新。<br>
        • 把两层记忆网络的联合内循环优化改为逐层局部预测目标和状态依赖 delta 更新，同时支持分块并行。<br>
        • DeltaNet 与 LaCT 骨干上的语言建模和检索优于循环基线；因果解释仍来自探索性优化实验。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.08586"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MINDSET 将记忆视为受约束的版本化状态管理，保留不可变情节及当前和历史图式。<br>
        • 最小能量转移在强化、覆盖、分裂与创建间选择，平衡冲突、历史损伤和碎片化，并用滞后避免过早重写。<br>
        • 850 个问题上报告较强回答和检索指标；MemoryAgentBench 差距较小，跨模型检查另使用 700 问题样本。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-06</td>
      <td style="width: 55%;"><strong>When Forgetting is not Catastrophic: On the Mechanics of Spurious Forgetting</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.08718"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将表面遗忘拆成共享方向导致的可逆访问丢失与个别事实的真实侵蚀。<br>
        • 最小联想记忆解释动态，并用合成 Transformer 的公共偏移扣除和预训练模型更新方向移除做干预。<br>
        • 去除共享方向可恢复旧事实，表明召回崩塌不必然等于存储消失；长期事实特异变化仍可能造成真实遗忘。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;"