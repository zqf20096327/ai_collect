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
[![Papers](https://img.shields.io/badge/Papers-1612-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
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
+ 2026-11-24 - 🎉 更新 54 篇论文，其中综述 1 篇，方法类与框架类论文 38 篇，数据集和评估基准类论文 5 篇，模型和系统类论文 10 篇
+ 2026-11-19 - 🎉 更新 61 篇论文，其中方法类与框架类论文 45 篇，数据集和评估基准类论文 11 篇，模型和系统类论文 5 篇
+ 2026-11-16 - 🎉 更新 19 篇论文，其中方法类与框架类论文 13 篇，数据集和评估基准类论文 5 篇，模型和系统类论文 1 篇
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
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>Privacy Protection in Self-Evolving Personal Agents: Persistent Memory and Cross-Carrier Transfer</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26983"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 综述个人智能体持久记忆及跨载体复用的隐私保护。<br>
        • 按受保护变化、观察者和验证环境比较准入、维护、披露与撤回，并追踪私人事实的后代。<br>
        • 诊断实验揭示广泛删除和扩大保护范围的效用代价；不读取某条记忆不能证明已清除学习状态。
      </td>
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
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30011"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MORSE，用反复出现的流式记忆错误驱动自动研究。<br>
        • 按失败原因分组，检索论文、模型和代码，修改证据存取方式，并先验证准确率再优化速度。<br>
        • Qwen3-VL-8B在OVO-Bench达到75.1%准确率、平均0.30秒回答；结论基于固定骨干的留出流比较。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30148"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出STMemoLLM，用模式原型记忆增强LLM交通预测。<br>
        • 训练阶段学习固定推理原型，以传感器偏好控制读取和压缩，再筛选可靠残差补充变化。<br>
        • 八数据集报告鲁棒性，并在两数据集五种子消融；原型推理时固定，不应描述为在线跨会话记忆更新。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>Composing Independently Distilled Memory and Retrieval Policies for Long-Term Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30230"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究独立蒸馏的记忆写入和检索策略能否直接组合。<br>
        • 分别从教师行动轨迹训练3B专家，与固定回答器连接，并消融策略兼容性。<br>
        • LongMemEval设置达到73.1%，额外RL后75.2%；比较结果依专家组合和任务适配，不能归因于单个模块。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30287"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MMMem，将多模态原始记录与任务后经验共同保存。<br>
        • 建立源链接多视图，结合记忆预热和自训练；从完成任务提炼情境、结论及证据，再按任务检索和保留。<br>
        • Qwen3.5-9B在三个记忆基准相对最强基线提升36.9%、17.6%、15.2%；外部记忆与训练共同贡献收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>Seeing Together, Acting Apart: Shared Environmental Understanding for Multi-Robot Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30310"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出SEER，在决策前建立多机器人共享环境理解。<br>
        • 汇总局部观察为共享记忆，按时空相似性检索，并以预测世界模型编码为导航token。<br>
        • 对专用VLN和通用VLM导航均报告提升；证据限于所测导航设置，摘要未给统一数值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>DMC-5: Dual-Model Collaboration with Cache-aware Context Compression for Long-horizon Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30412"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出DMC-5，将完整轨迹维护与行动生成交给不同模型。<br>
        • 保留只追加的原始轨迹，以紧凑决策视图供智能体读取，并用YAMATO保留工具操作关键事实。<br>
        • 三个任务集上输入减少38.5%–57.0%、总成本减少14.5%–28.0%；效果依缓存价格、压缩模型和任务设置而定。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-23</td>
      <td style="width: 55%;"><strong>Doc-to-LoRA Analysis: Query Conditioning, Wrong Facts, and Distractor Interference</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.30825"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估将用户文档编译为LoRA记忆能否替代文本上下文。<br>
        • 通过事实问答、错误事实和逐层干预定位多文档干扰，并测试联合编译与适配器组合。<br>
        • D2L总体弱于上下文学习；PersonaMem-v2接近文本记忆时仍保留文本情节，节省有限且吞吐收益依模型与批量而变。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-22</td>
      <td style="width: 55%;"><strong>ContextFact: Remembering Facts in Context for Long-Term Conversational Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.29155"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出ContextFact，保留事实的解释上下文并连接跨会话实体。<br>
        • 回访源对话重建实体表示，分别重排事实/实体视图，再沿实体关联扩展证据。<br>
        • Qwen3.5-27B在LoCoMo/LongMemEval-S达到86.49%/91.00%，仅用最强对比方法21%的证据token；结果来自指定骨干。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-22</td>
      <td style="width: 55%;"><strong>DoppelVet: Comparative Safety Verification for Self-Evolving Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.29306"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出DoppelVet，在记忆或技能更新进入持久状态前进行比较验证。<br>
        • 构造与候选匹配既有验证信号的替代更新，从相同状态重放并双顺序比较行为。<br>
        • 九种验证器在Tool任务的平均有害更新AUC由0.681升至0.826；Grid十代循环退化轨迹降至0.43%，两场景不可混为同一指标。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-22</td>
      <td style="width: 55%;"><strong>MERIT: Experience-Guided Memory for Long-Horizon Persona-Specific Persuasive Dialogue</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.29679"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MERIT，面向持续多年交互的动态用户记忆。<br>
        • 将四类说服相关图记忆与个体策略成败理由库结合，按用户演变组合提示而不更新参数。<br>
        • 在60个策划persona的PERSIST上，两骨干说服吸引力评分为4.10/4.74；证据来自人工核验的构造情景。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-22</td>
      <td style="width: 55%;"><strong>How Should a Home Robot Update Its Memories When Human Routines Change?</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.29818"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究家庭日常模式改变后又恢复时，机器人记忆应如何更新。<br>
        • 在模拟疾病、康复、复发情景中比较完整目击历史、文字摘要和两者结合，并删除早期经历作对照。<br>
        • 保留历史优于仅摘要，额外摘要未显示可测收益；这是模拟家庭中的负结果，不能推广为所有摘要均无效。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-21</td>
      <td style="width: 55%;"><strong>EvoViM: Recursively Self-Evolving Visual Agents for Exploration with Deferred Queries</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.28574"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出EvoViM，在探索后才获知问题的设置中演化视觉记忆程序。<br>
        • 冻结模型从自身轨迹定位证据丢失或误用，修订存取操作以及指导后续修订的笔记和工具。<br>
        • 六任务、三模型相对AutoMem平均得分提升31.3–47.6点；证据来自留出回合，含三项延后查询任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-21</td>
      <td style="width: 55%;"><strong>Internalized Experience: How Training Data Shapes Memory Formation in LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.28613"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出FSMem，用状态转移数据研究LLM如何形成可复用规则记忆。<br>
        • 在合成世界、规划和代码中控制动作类型、覆盖度和轨迹深度，评测有效动作及执行结果预测。<br>
        • 更多动作类型增加内化难度，混合长短轨迹可优于仅长轨迹且更省token；规律限于所测训练任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-21</td>
      <td style="width: 55%;"><strong>HyperHarness: Learning to Generate Personalized Agent Harnesses from User Histories</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.29062"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出HyperHarness，从用户历史一次生成个性化记忆读取代码。<br>
        • 跨训练用户优化共享生成器，部署时为新用户合成检索与回答指导函数，无需逐用户任务评分搜索。<br>
        • 三基准三回答模型的九个设置中七个第一、两个第二；最高5.95点提升并非所有设置的统一收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>VideoJSON: A Minimal Harness Beats Purpose-Built Memory for Ultra-Long Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.28167"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出VideoJSON，用简单结构化记忆支持超长视频问答。<br>
        • VLM将每分钟视频写成含事件、实体、地点和语音的JSON，编码智能体用多步Python/Bash查询记录。<br>
        • 四基准优于所比方法，消融支持代码检索与结构字段；默认查询不访问原视频，结果依记录质量和策略模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>Epistemic Guard: Out-of-Process MCP Receipt Proxying, Post-Turn Prose Supervision, and Provenance-Gated Memory for Tool-Using Autonomous Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.27095"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Epistemic Guard，将工具执行收据与持久记忆写入资格绑定。<br>
        • 进程外签名和Merkle日志验证执行证据，以七类来源域门控SQLite写入，并检查后续文字陈述。<br>
        • 100次未授权写入测试全部阻止；真实代理轨迹误报率38.24%，不能以合规套件成功率代表实际安全保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>NavTTT: Adaptive Parametric Memory via Hierarchical Test-Time Training for Vision-and-Language Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.27219"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出NavTTT，用回合内快权重保存导航历史。<br>
        • 全局导航上下文筛选信息，融合语言指令和空间表示，各解码深度维护独立参数记忆以减少干扰。<br>
        • 在VLN-CE和真实机器人上报告有效导航与指令跟随；属于回合局部适应，不等于跨会话永久学习。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>VMSA: Video Memory Skill Agent for Long Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.27381"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出VMSA，联合设计视频证据记忆与可复用检索技能。<br>
        • 从成功轨迹提炼程序，按覆盖度增补/修订并定期合并，跨基准读取相关技能指导检索和验证。<br>
        • 七基准中三个周长视频任务领先，Ego-R1最高提升9.4%；技能来自目标组以外基准，部分长视频设置关闭原片检查。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.27689"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Embodied-Harness，将执行记录转为分层智能体记忆。<br>
        • Actor保留进展与详细反馈，Reflector累积任务经验并生成后续操作指导；设计包括跨任务知识抽象。<br>
        • RoboSPA-Long L5去掉长期记忆时成功率59.5%降至48.5%；跨任务和跨本体迁移仍待进一步验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>Video-as-Weights: Compiling a Video Once into Parametric and Token Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.28221"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Video-as-Weights，在未知问题时将视频编译为参数与token记忆。<br>
        • 编译器从各层生成冻结解释器的LoRA和可选前缀，支持同模型编译及大到小迁移。<br>
        • 六视频QA基准上0.8B解释器较完整上下文提升1.7或4.3点；机制分析区分有无前缀时权重的存取作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-20</td>
      <td style="width: 55%;"><strong>Evaluating Memanto on DolphinBench for AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.28231"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 评估Memanto在隐含记忆需求的DolphinBench工作任务中的表现。<br>
        • 用信息论相关性排序记忆，在Hermes与GPT-6-Luna中完成600项记忆依赖任务，每会话最多6轮。<br>
        • 完成503项即83.83%，总费用10.86美元；因骨干与迭代预算不同，与公开基线只能比较整套系统。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25583"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出DriftGuard，估计检索记忆对智能体行为漂移的因果风险。<br>
        • 离线成对重放原始与单条中和后的轨迹，训练在线模型从行动前信息预测多维漂移分数。<br>
        • 报告有效识别危险记忆并支持在线防御；在线估计依赖离线反事实标签，摘要未给统一效果数值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>KeyMem: Temporal Occupancy Control for Robust Streaming VideoLLM Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25649"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出KeyMem，限制单一时间片段对流式视觉记忆的占用。<br>
        • 归一化原有分数并按时间桶设置硬配额，可选秘密密钥采样，防止短片段驱逐长期证据。<br>
        • 小预算下最差准确率由42.2%升至73.3%–76.1%；密钥在自然压力下无明显优势，也不总胜过最佳确定性配额。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>From Geographic Memory to Spatial Generalization in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25703"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究地理记忆与空间泛化应如何分别评测。<br>
        • 将连续位置编码投影为空间token，在洛杉矶和伦敦数据上分开测试已见/未见位置描述，并探测各层表示。<br>
        • 连续表示改善未见地点描述并小幅提升下游定位；表征聚类与探测提供支持，但不证明任意地理推理能力。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>STARK: Moving towards Personalized Agents That Truly Learn and Remember</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25705"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出STARK，将情节记录与行为洞察组织为双图记忆。<br>
        • 情节图保存时间/因果/语义关系，洞察图以事件作证据边，直接检索行为知识并探索跨用户迁移。<br>
        • LongMemEval和LoCoMo特定子任务的judge分数提升1.48/0.93；跨用户结果来自LongLaMP稀疏设置，不代表普遍迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>MemMend: A Selective Revision Framework for Memory Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25721"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MemMend，选择性修订长期记忆问答而非重写所有答案。<br>
        • 路由疑似不完整答案，以可解析来源坐标约束精确文本替换；无合法编辑时保留原答案。<br>
        • LoCoMo开发集较验证链减少62.37%修订调用；跨数据迁移仍有完整性缺口，来源约束的独立质量收益未解决。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>HabitusMem: Belief Memory over Evolving User Preferences for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25855"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出HabitusMem，将用户记忆表示为可修订偏好信念。<br>
        • 训练写入器结合当前请求与历史，为冻结智能体生成含证据、范围和状态的文字记录。<br>
        • 两个智能体家族在PersonaMem-v2和VitaBench 2.0上优于所比记忆系统；消融区分请求条件化和辅助训练的作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25861"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出BiSpace，分离终身知识编辑中的记忆检索与注入。<br>
        • 在外部语义空间定位编辑，在LLM内部表示空间以稀疏紧凑更新注入知识。<br>
        • 每项存储约为原始10.2%，测试至16K编辑；更困难基准整体性能提升超过23%，依具体指标与基线定义。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>Thinking in Streams: Proactive Spatial Reasoning with Vision-Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25865"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出ProSpace任务与模型，评测流式视频中何时应回应空间条件。<br>
        • 因果估计几何编码注入VLM中间层，以KV作为空间记忆并选择空间token。<br>
        • 模型改善及时回应和正确拒答，但仍与人类有明显差距；相关分析限定于所测九类空间任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25868"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出StarTV-Agent，以持久工作流经验复用视觉工具编排。<br>
        • 从真实执行保存通用工具步骤，按执行反馈添加或修订，快路径绑定新任务参数，失败时转慢速推理。<br>
        • 三基准最高相对提升8.0%、token最多减少52.1%；完成不等于答案正确，记忆维护禁止保存具体答案并使用契约检查。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>EvoMem: Self-Evolving Skills for Time-Aware Long Video Memory Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25889"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出EvoMem，以时间对齐记忆和演化技能维持视频证据链。<br>
        • 从成败轨迹提炼带适用边界的检索程序，以独立验证奖励接纳有效技能并保存拒绝历史。<br>
        • 四视频QA基准平均60.1%，较先前最佳平均高8.6点；演化与最终评测问题分离，收益依训练和验证分布。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>SpatialMem: Building Quantitative Spatial Reasoning Agents with Hierarchical Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25925"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出SpatialMem，用层级经验记忆组织视觉工具。<br>
        • 任务记忆保存编排，场景记忆保存工具选择；双状态轨迹优化保留成功方案并修订次优经验。<br>
        • MetricBench上较无记忆智能体绝对提升9.1点，并测试另两空间基准；经验适用范围受场景和工具集约束。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26361"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究部署智能体应读取多少自蒸馏流程记忆。<br>
        • 每回合提炼1–3条经验，合并为带支持数的指南，再全部或选择性提供给后续任务。<br>
        • 强模型可受益于全部指南，弱模型小子集更好；文中报告来源丢失、指南反作用和评测混淆，不能假定记忆越多越好。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26427"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MemFolder，同时减少长期记忆记录数和读取上下文长度。<br>
        • RecordFolder按实体、语义和时间合并互补记录；ContextFolder压缩编码并用事实恢复反馈修订。<br>
        • Mem0在三个文本基准减少50%记录时保留99.0%平均性能；另有两个多模态基准，压缩收益依原始系统而定。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>MomentMem: Memorizing Key Moments for Robot Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26745"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MomentMem，以关键时刻视觉证据支持记忆依赖操作。<br>
        • VLM记忆器选取关键帧，独立执行器据此行动；VMBench测试位置、外观及关联保留。<br>
        • 平均成功率49.9%，较最强所比基线高31.7点；少量记忆标注的迁移结果不代表无需任务适配。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>Memorization and Generalization in Generative Models: A Perspective From Energy-based Modeling and Associative Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26797"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从关联记忆吸引域解释生成模型的记忆与泛化共存。<br>
        • 除图像扩散分析外，直接研究离散语言扩散模型中训练/未见句子的恢复域和条件熵。<br>
        • 随数据增加，训练样本域收缩而未见样本域扩展；证据针对所测扩散模型，不能直接推广到所有自回归LLM。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26902"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出Baton，将小VLM已感知的历史记忆交给大VLM。<br>
        • 从大模型答案蒸馏逐层线性KV映射，仅重编码当前帧；干预定位中间层的关键方向。<br>
        • RoboMME级联以少28%–47%计算接近重看历史的性能；复制KV最忠实不一定有效，结果跨八模型对测试。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>Self-Evolving Beyond Human-Crafted Experience for EDA Scripting</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.26912"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出ZhuLong-SE，从EDA脚本执行中学习跨任务知识。<br>
        • 将轨迹提炼为三层记忆，通过真值锚定、反证过滤、留出回滚和防泄漏检索治理复用。<br>
        • 困难实例分离测试上自演化达80.0%，对人工经验77.5%；92.4%主基准成绩来自关闭自演化的任务harness，不能混归记忆收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-19</td>
      <td style="width: 55%;"><strong>ActMem: From Latent Memory Reasoning to Grounded Robotic Action</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25461"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ActMem通过语言模型从交互历史推断当前子任务，将推理隐状态作为动作记忆条件。<br>
        • Memory CoT读取历史与当前画面，动作专家只接收该条件；重复子任务经验证后复用并重算状态。<br>
        • RoboMemArena任务成功率71.1%、完成率80.8%，真实任务均值68.8%；消融支持历史及隐状态通道，但仍限于所测操作任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Toaster: Nonlinear Memory from Cascaded Linear Memories and Target Propagation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23648"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Toaster以两层线性delta记忆加激活形成可训练的非线性状态。<br>
        • 目标传播把输出误差映射为隐藏目标，按块近似跨层信号并复用现有delta内核。<br>
        • 多个匹配规模语言实验降低损失，最大配置13任务均值51.84对KDA的50.52；速度比较依具体规模与实现，不能混为同一配置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Keep the Reasoning, Read the Image: On-Demand Visual KV for Multi-Turn Reasoning VLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23769"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ShelfKV直接研究长推理挤出图像证据造成的内部记忆遗忘。<br>
        • 保留CPU上的完整视觉KV，按当前查询召回高分视觉内容并替换低分文本槽，分离保留和访问。<br>
        • 相同GPU预算下相对DBTrimKV最高提高20.3个百分点；优于固定预留但结果依赖所测模型与任务，不能只以容量解释。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>PReMind: When Personal Memory Meets Visual Hazards</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23808"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PReMind研究视觉风险判断如何正确使用用户记忆，而非仅识别图中危险。<br>
        • 评测记忆访问、视觉关联和拒答，并以按需与强制调用两阶段强化学习训练。<br>
        • 4B模型联合成功率由12.9%升至28.6%，多种控制支持稳健性；这不是临床效果或完整安全性证明。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Weighing the Envelope: Component Weight and Arbitration in Envelope-Layer Defenses for a Single LLM Agent</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23844"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究长期记忆投毒如何与工具角色和授权表述共同影响防御。<br>
        • 控制预置恶意记录、验证标签和历史成功记忆，比较检查、降权与拒绝策略。<br>
        • 强制核验标签可减少语义违规，但成功记忆会侵蚀防御且仍有泄漏；软提示措施不能替代权限控制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Kernel Ridge Attention: Nonlinear Memory with Selective Forgetting</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23896"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • KRA以递归岭回归形成固定状态的非线性关联记忆。<br>
        • 学习键特征与协方差更新，用内容相关保留恢复不确定性，并给出时间核解释和并行训练形式。<br>
        • 受控语言预测与关联召回优于比较方法；证据限于论文规模与任务，未建立前沿通用模型优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>MIRAGE: A Framework for Multi-hop Reasoning under Dynamic Knowledge Injection</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24058"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MIRAGE区分参数记忆中的冲突旧知识与全新缺失知识对多跳推理的影响。<br>
        • NEXUS构造动态事实任务，CDR用双路径置信度选择信息来源并校正结构错误。<br>
        • 四模型家族、两基准支持方法收益；结果针对受控知识冲突，不构成任意检索证据都更可信的保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>ViStep-RL: Stepwise Reinforcement Learning for Long-Horizon Visual Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24170"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ViStep-RL把可持续使用的证据记忆纳入长程视觉任务学习。<br>
        • 验证依赖图中的子目标，按净进展奖励，并让智能体主动写入、检索和使失效证据的依赖项失效。<br>
        • Qwen2.5-VL-7B严格完成率60%，对比SFT的46.5%；主动写入较自动写入提高7.75个百分点，结论来自受控任务协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Allocentric Memory, Egocentric Acting: A Dual-Frame VLA for Urban Aerial Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24247"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CityNav-VLA以稳定全局地图记忆连接语言目标与变化的机载视角。<br>
        • 冻结CityBot-4B编码器，按指令、当前观察和运动历史查询空间记忆预测目的地，再由确定性控制器执行。<br>
        • 消融将导航地图特征识别为主要增益来源；固定时长控制和早期目标锁定限制停止与改目标能力，跨方法执行设置也不同。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Look Closer, Look Back, or Wait for Agentic Streaming Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24267"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ActiveForager将当前观察和历史证据读取分开，减少旧视频对当前决策的干扰。<br>
        • 主策略选择回答、放大、回看或等待，历史子智能体独立核验片段并返回紧凑证据。<br>
        • Qwen3-VL-8B在OVOBench由47.6升至65.9；整体训练同时包含其他工具，收益不能归因于历史记忆单独作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>OpenKAGE: Open-Ended Lifelong Learning in the Open World via Knowledge-Sharing Agent-Group Evolution</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24302"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • OpenKAGE区分个体处境记忆与可共享经验，支持群体跨世界持续学习。<br>
        • 反思生成条件化经验与技能，语义合并和修正文本；技能保留作者及成功失败记录，由作者修订或退役。<br>
        • 四骨干及新群组迁移支持经验共享的存活和探索收益；未证实通用环境保证，未确认经验仍可进入图中等待佐证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Resolution as Attention for Efficient Agent Memory Perception</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24422"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • RAA把历史读取的分辨率纳入记忆管理，而不只决定保留哪些条目。<br>
        • 将交互历史渲染成图像，由教师训练的轻量相关性估计器选择读取精度，并约束决策一致性。<br>
        • 所测任务和骨干中节省超过50%的token且保持表现；收益范围以论文实验为准，不能视作所有场景统一保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Beyond Appearance: Evidence-Guided Programmatic 3D Scene Reconstruction with Agentic Lighting Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.24565"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LightHarness以照明推理记忆维持生成器和验证器跨轮共享的场景证据。<br>
        • 保存光源状态与诊断历史，检查来源对应后追加修订，并用渲染、几何和光传输证据指导下一轮。<br>
        • 消融支持完整证据、评分约束和迭代设计；验证范围是图像到场景程序重建，不证明跨任务长期经验迁移。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25123"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • GrepMem以完整文本日志和正则搜索构建简约智能体记忆。<br>
        • 保留原始历史而不做嵌入或抽取，训练Qwen3.5-9B在需要时搜索日志并管理上下文。<br>
        • ContextBench达95%—97%，所测有损策略不超过21%；五任务呈现质量—token优势，但日志无损不保证搜索总能召回所需信息。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-18</td>
      <td style="width: 55%;"><strong>Some Memories Must Fade: Persistence and Decay of User Memories in Model Parameters</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.25235"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究参数用户记忆如何同时保留有效事实并让过期信息淡出。<br>
        • 在固定容量稀疏LoRA中结合时间衰减和学习式控制器，决定每条事件写入深度及保留时长。<br>
        • 受控长期用户轨迹上达到oracle平衡表现的86%；结果取决于衰减、容量和轨迹设定，不代表开放世界遗忘保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>EvoDisco: Strategy Discovery for Evolving Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22102"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EvoDisco学习何时及如何改变记忆，而非使用固定更新操作日程。<br>
        • 策略按当前记忆和近期任务选择抽象、细化、连接或重构，联合检索质量、复杂度及长期操作效用训练。<br>
        • ALFWorld在线和冻结迁移较MemP提升8.8与12.9分；消融支持双层信号及操作库，泛化证据限于所测环境。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>RegimeCouncil: Paired-Evidence Routing For Memory Conflict Governance In LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22113"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • RegimeCouncil研究过时记忆的负反馈应影响单一事实还是全局使用策略。<br>
        • 维护局部和全局顾问，比较记忆回答与无记忆锚点，仅在近期效用支持时切换到全局范围。<br>
        • 在30个留出设置和漂移任务上优于较好固定范围策略，主要分歧样本提升5.2—7.3分；理论保证依赖其延迟反馈设定。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn&#39;t</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22179"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • BRIDGE检验复杂记忆组件是否真正改善智能体行为，而不只提高召回分数。<br>
        • 以串联观察笔记、混合检索和时间排序建立最小记忆，再用五类对抗探针测试规则应用和模式归纳。<br>
        • 标准记忆基准接近或超过强基线，但探针中原子事实和块摘要各有胜负；100个探针场景不支持统一最优架构。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22274"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • GuardAgent把检测经验转为可追溯的规则记忆，以适应新的推荐推广攻击。<br>
        • 反思优先修订决策规则，将验证后的短期经验并入长期存储；推理时检索稳定示例并结合当前规则。<br>
        • 真实数据上的比较支持对新攻击的泛化；结果基于所测攻击与固定实验设置，不能证明开放部署中的全面防护。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22418"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CutAgent将制作失败后的可验证修正保存为后续视频任务的程序经验。<br>
        • VideoAgent在脚本规划前按品类和创意检索经验，渲染后独立反思、修订并把验证后的修正写回长期记忆。<br>
        • 完整系统在线CTR达到2.21%；结果同时包含创意模型训练与制作流程变化，不能归因于记忆单独作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22461"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DebateGraph发现把记忆矛盾显式交给辩论，可能优于提前合并为单一事实。<br>
        • 在统一读写快照接口和预算下逐项移除机制，并修正检索上限导致矛盾不可见的瓶颈。<br>
        • 保留冲突集合提高F1达0.340，投毒成功由22/122降至7/122；其他机制未过门槛，写入信任门甚至降低准确率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23346"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将记忆写入、巩固与恢复的状态转移边界纳入智能体安全审计。<br>
        • 生成最小哈希链转移记录，区分确定性与语义检查，并支撑授权、信息流和事务恢复控制。<br>
        • 240条多步故障注入轨迹能定位工具日志遗漏的跨边界违规；这是参考中间件验证，不代表所有harness均受保护。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>PlaceTally: A Test-Time Memory Model for Constructing Place Graphs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.22608"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PlaceTally用与问题无关的地点记忆减少重访视频中物体重复计数。<br>
        • 每段视频匹配既有地点或创建新地点，冻结VLM每地点读取至多128帧并计数一次。<br>
        • 真实重录房间测试及留出房间达62.5%和61.2%，高于整段输入的51.2%和44.3%；方法依赖地点区分和物体较少跨房移动的假设。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23010"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PhysScope针对物理推理中事实越出适用条件造成的连锁错误。<br>
        • 将观察绑定物理作用域，检查修订的来源和条件，并使被修改事实的注册依赖失效。<br>
        • 六个VLM均优于直接求解，Gemini-3.8-flash比Canvas-CoT高9.34个百分点；收益针对所测物理任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>Natural Language Programming: Rethinking Language, Memory, and Cognition in the Era of Generative AI</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23106"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出“对话工作记忆”视角，把提示和会话状态看作支持推理连续性的外部记忆。<br>
        • 以分布式认知和元认知理论描述目标、约束及验证标准，并将既有记忆架构映射到情节、语义和元认知层。<br>
        • 贡献为理论框架和架构解释，没有实证性能提升结果，不能把概念映射视作有效性验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>Stability Does Not Mirror Plasticity: A Module-Level View of Declarative and Procedural Learning in Transformers</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23427"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究Transformer的记忆稳定性为何不与学习可塑性镜像对应。<br>
        • 用合成声明性与程序任务、模块更新和重置恢复实验，区分内容存储与访问依赖。<br>
        • 更新QK可保留超过一半声明记忆，而更新VO约丢失五分之四；真实模型实验大体一致，但结论依任务和模块角色。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-17</td>
      <td style="width: 55%;"><strong>ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.23588"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ARISE把执行失败归因转化为可检索经验和可验证的跨任务规则。<br>
        • 从自身或教师轨迹提取微记忆，合成宏规则，只有提升留出准确率才接纳，保持模型权重和工具固定。<br>
        • 教师版本在SOPBench和tau2分别提升10.9和5.8个百分点；收益限于所测任务，教师归因不保证生产环境正确。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>AdMem: Expectation-Grounded Procedural Memory for Long-Horizon Task-Solving Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.20605"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • AdMem针对盲目累积经验反而损害任务完成的问题，显式管理程序记忆生命周期。<br>
        • 行动前记录期望，评论者按实现结果赋奖励和反思；效用与相似度联合检索，并驱动合并及驱逐。<br>
        • AgentBoard八领域707任务完成441个，对比ReAct的388和流程基线的312；收益集中在可迁移结构领域，文本记忆仍可受攻击。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>Instant Weight-Space Consolidation for Long-Term Memory in LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.20759"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CLAM以单次前向参数巩固补充文本情节记忆，让历史改变模型本身。<br>
        • 循环超网络把会话激活编译成低秩适配器，固定大小门控状态跨会话传递，缓冲保留逐字细节。<br>
        • 三种2B—7B模型在两个基准上优于所测对照，构建时间减少3—151倍；适配器和缓冲互补，范围不等同开放部署保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>LEDGER: Auditable Agent Memory Under Change</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.20927"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • LEDGER将事实更新、来源信任和删除显式化为可审计记忆规则。<br>
        • 语言模型提出事实，规则决定当前值；EP回退检索原始对话，并在删除时清理派生读取来源。<br>
        • 留出合成编码任务91.1%对完整回放83.3%；LongMemEval子集同为74.8%且仅1%上下文，强系统差异仍在置信区间内。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>ReAccess: Look Once, Stay Focused with Efficient Test Time Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.20936"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ReAccess用紧凑关联记忆保留与问题相关的视觉证据，避免反复看图。<br>
        • 在一次视觉prefill中构建记忆，逐步召回并同时引导注意力查询与隐藏表示。<br>
        • 所测通用视觉理解和细粒度感知改善，推理较多次处理方法更快；摘要未给统一量化幅度，效果范围以实验设置为限。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.21019"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemDoctor把多模态记忆错误定位到来源阶段，而不只修正最终答案。<br>
        • 定义四阶段九类错误，反向追踪所需事实，只接受能在记忆中找到引用证据的诊断并修复对应阶段。<br>
        • 4B骨干在Mem-Gallery和MemLens优于所测8B基线，也改善MuRAG及A-Mem；证据不足时早期错误仍可能伪装成可信来源。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>Out of Sight, Into Memory: Compact Visual Latents Retain Local Evidence in Ultra-High-Resolution Remote Sensing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.21457"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究紧凑视觉潜在记忆是否真正保留超高分辨率图像的局部证据。<br>
        • 为冻结Qwen-VL骨干编码64个记忆token，以替换、清零和恢复原裁剪隔离内容依赖。<br>
        • 保留token压缩7.6—9.9倍且准确率高2.5—4.8个百分点；错配记忆反而低于无记忆，结论特定于证据保留而非区域选择。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.21478"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Jetriever把记忆检索从表面相似度转为回答效用评分。<br>
        • 利用LLM衍生决策模型对完整记忆池估计有用概率并直接排序，检查知识识别与排名校准的区别。<br>
        • InMind的125任务中首位命中84.8%、应用76%；MAB仅抽样60问，完整池评分成本与扩展性仍需按场景衡量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-16</td>
      <td style="width: 55%;"><strong>Learning In-Context Adaptivity for LLMs through Continual Gameplay</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.21710"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究智能体虽准确记录对手，却不按记忆改变行动的“记忆—行动”缺口。<br>
        • 用配对有无记忆协议隔离经验收益，跨上下文片段联合训练摘要生成和整场回报。<br>
        • 9B强化学习策略在未见对手上使经验收益相对SFT翻倍或增至五倍；结果针对所测不完全信息博弈。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-15</td>
      <td style="width: 55%;"><strong>When Facts Change, Which Decisions Break? Dependency-Aware Context Graphs for Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.19859"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究事实改变后应修复哪些决策，以字段级依赖减少不必要的全量重算。<br>
        • 从模型实际读取轨迹构建依赖图，定位受影响步骤并保留未受影响的计划。<br>
        • 新鲜60工作流测试中，一个模型达到全上下文正确率且估算成本下降4%；另一模型仅84.8%对99.6%，遗漏替代项仍会破坏完整计划。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-15</td>
      <td style="width: 55%;"><strong>SAGE-VQA: A Training-Free, Self-Evolving Agentic Framework with Grounded Evidence for Knowledge-Based Visual Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.19933"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SAGE-VQA以可核验视觉证据和分层经验记忆支持无需训练的问答演进。<br>
        • 保存带来源的错误与修正，按反馈细化记录、合并同类经验；程序需适用性、输入和执行检查后才可使用。<br>
        • 在所测知识视觉问答任务上优于比较方法；记忆形成依赖参考答案等反馈，不能等同无监督部署中的持续改善。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-15</td>
      <td style="width: 55%;"><strong>A Matrix with Steps: An Episodic and Procedural Memory Method for Tool-Using Agents and Robots</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.20230"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将情节矩阵与可寻址的有序步骤结合，复用经外部验证的操作经验。<br>
        • 分离任务成功与模型自报，确定性巩固记录，并按执行结果晋升、降级和删除默认流程。<br>
        • 小语言模型四工具测试的正确调用率由46%升至54%；只复用曾成功的调用，实验未涉及真实机器人或用户。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-14</td>
      <td style="width: 55%;"><strong>Can an Agent Rethink What It Knows? Selective Scene Memory Updates in a Changing World</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.19227"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究参数场景记忆如何更新变化事实并摆脱旧值干扰。<br>
        • 在四事实合成场景中，将暴露次数、更新预算和历史准备方式分离，比较LoRA写入轨迹。<br>
        • 两种变化历史在32次更新后联合成功率达94.79%和91.15%，旧值错误归零；结论限于受控小型场景。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-14</td>
      <td style="width: 55%;"><strong>Read Boundaries in Agent Memory: Consistency, Completeness, and Repair</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.19264"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 指出记忆召回、补充和物化的多次读取可能跨越不同更新版本。<br>
        • 用整次读取锁、乐观epoch或共享快照维护兼容版本，并测试故障后的恢复。<br>
        • Cognee保护方案在24,020次默认读取中均保持兼容；epoch降低更新尾延迟却提高召回尾延迟，故障仍需原生重建修复。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-14</td>
      <td style="width: 55%;"><strong>Information Limits of Replay-Free Recurrent State Migration</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.19345"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析无需历史回放的循环状态迁移究竟需要多少额外记忆。<br>
        • 在线性时不变仿射模型下，用可达空间与旧锚点信息刻画局部迁移阶数的最低状态需求。<br>
        • 小语言模型中更精确的状态插值未带来有意义预测收益；结论受局部线性假设及受控实验范围限制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-14</td>
      <td style="width: 55%;"><strong>PathLoop: Self-Evolving Multi-Agent Reasoning for Evidence-Grounded Whole-Slide Image Analysis</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.19527"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • PathLoop把跨病例经验复用作为病理多智能体分析的核心组成，联合分子证据和切片审阅。<br>
        • 四层记忆执行选择、写入和管理，按结果优势强化条目，周期合并重复与移除过时内容。<br>
        • 四个TCGA队列及模块实验支持整体方法；结果不能归因于记忆单独作用，缺少真值时使用一致性反馈也限制可靠性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-11-13</td>
      <td style="width: 55%;"><strong>Self-Improvement Memory Enables Continual Recursive Self-Improvement</strong></td>
      <td style="width: 15%;"><img src="https://img.