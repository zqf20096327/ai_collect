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
[![Papers](https://img.shields.io/badge/Papers-1416-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
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
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>MEMIG: Self-evolving Memory Construction for Antibody Optimization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41245"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出MEMIG，替代科学优化经验的自由文本改写。<br>
        • 按领域标识保存定量测量，局部更新并精确查找，再连接联合干预以记录上位性。<br>
        • 在多数计算抗体优化设置改善表现；未构成真实实验或临床抗体效果证据。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>When History Overrides Intent: Relational Schema Lock-In in Human-LLM Interaction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41367"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究历史记忆形成的用户理解越权覆盖当前意图的关系模式锁定。<br>
        • 结合用户报告、六模型受控历史实验及360人交互，区分任务完成与忠实执行。<br>
        • 替代式产物可维持完成率却偏离用户意图；结果针对所测交互条件，不代表所有记忆系统。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>What Does a Repair Agent Gain from Remembering Its Failure? An Exploratory Study on Real Python Bugs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41433"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 直接比较代码修复重试中的不同失败记忆。<br>
        • 在75个BugsInPy缺陷的181次失败上对照普通重试、转录、教训和测试信号，并增加模型及通知对照。<br>
        • 记忆收益点估计提高5.5–9.9个百分点但均未显著；教训不优于转录，完整测试套件削弱表面收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41482"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究递归文本记忆为何持续保留错误，提出KEEPER比较框架。<br>
        • 沿信息内容和更新敏感性比较四类辅助目标，结合离线强化学习和逐主张轨迹分析。<br>
        • 奖励相关预测取得最高任务表现；纠错证据含单条轨迹案例，不能据任务分数断言记忆可靠。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>KITE: Retrieval as a Decision Procedure for Long-Term Conversational Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41521"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出KITE，把记忆检索转为可检查的决策过程。<br>
        • 构建和查询共享受控主题词表；查询编译成固定查找排序计划，再用稀疏词法检索恢复细节。<br>
        • LoCoMo和LongMemEval-S准确率为93.5%和86.0%，每题约1.6k读者上下文token；结果基于所测基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>ORION: An Outcome-Driven LLM Advisor for RL-Based Multi-Domain 6G Slice Placement</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41563"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出ORION的结果驱动情节记忆，用部署可行性指导后续规划。<br>
        • 保存网络条件、抽象方案及已验证成败，回馈规划器并以重要性保留经验。<br>
        • 固定下游执行后，未见拓扑上的接纳率提高4.6–11.5个百分点；结论限于参数化网络实验。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41994"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出DAMI，通过初始化控制记忆衰减和输入敏感性。<br>
        • 联合设置门控参数，在头间分配几何时间尺度、在层间设置敏感性，并用少量激活校准。<br>
        • 五类递归架构的检索准确率提高5.29–16.71个百分点，普通语言建模和常识表现总体相近。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>SPARK: Self-Correcting Embodied Memory via Physical Re-Observation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.00344"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出SPARK，用主动重观察纠正跨情节环境记忆。<br>
        • 语义批评器定位可疑区域，规划定点重访，并选择性新增、删除或替换知识库记录。<br>
        • 四张AirSim地图均改善问答，较追加更新少存13–41%对象；证据来自模拟地图和固定158题。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-30</td>
      <td style="width: 55%;"><strong>From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2611.00450"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出ResMem，把检索证据转为可复用参数记忆。<br>
        • 让同一骨干读取离线证据产生教师分布，仅训练记忆模块的加性logit残差。<br>
        • 五个问答集平均F1从32.83%升至34.48%，较kNN训练记忆少破坏21%的既有正确答案；存储比较基于所用管线。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Fewer Heads, Fewer Memories: Pruning Redundant Attention Heads Suppresses Verbatim Memorisation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.40974"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 检验冗余注意力头是否参与逐字记忆复现。<br>
        • 推理前置零任务冗余头，对照已知记忆序列召回和WikiText-103语言建模。<br>
        • 剪除729头使记忆计数减少91.5%、困惑度改善0.92；仅验证GPT-2-XL及相应基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.41056"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 联合研究记忆过时与投毒，避免分别优化相反写入决策。<br>
        • 证据条件准确率同时检查答案和所选记录是否完整、最新且无攻击，再用合成变更及攻击情节训练管理器。<br>
        • 三个骨干的整体指标超过未调优管理器两倍，但鲁棒性仍不完整。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>MemSteer: Turning User Histories into Supervision for Agent Memory Optimization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.39276"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MemSteer 从未标注用户历史生成记忆优化监督。<br>
        • 以证据支撑的回答计划生成 QA，经来源审计和盲答核验，再诊断并修改存储、检索与上下文设计。<br>
        • 相对 Base-BM25，ATM-Bench 提升 13.4 点；RHELM 在无/有外部数据时提升 4.1/6.6 点。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Federated Recommender Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.39289"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • FedRecAgent 让推荐代理共享自然语言经验，同时将个人历史与记忆留在本地。<br>
        • 将经验表示为条件—转移—理由单元，分层整合共享理由，由个人语义和决策记忆引导检索。<br>
        • 三个领域的稠密与稀疏设置优于所测基线，消融支持记忆和结构整合的作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.39446"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EvoLife 将主动询问、导航动作与持久空间记忆结合。<br>
        • 把观察和对话绑定到地点，保留经验以指导后续访问和连续任务。<br>
        • R2R 回访 SPL 从 82.23% 升至 93.31%，并报告多日实机导航；结果限于所测路线和任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Sticky Collusion: Persistence of LLM Agent Collusion after Incentive Removal and Partner Replacement</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.39660"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究合谋是否由交互记忆承载，而非仅由奖励或固定伙伴维持。<br>
        • 从已形成合谋的历史分支执行，比较奖励变化、换伙伴、完整擦除及分部件擦除记忆。<br>
        • 全部擦除在所测模型中终止合谋，部分擦除在 8/9 组合仍保留；证据限于特定双代理验证任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Long-Term Agent Memory through Complementary Curation and Consolidation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.39790"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合情节与关系记忆，研究两者在长期对话中的互补性。<br>
        • 混合记忆架构保存事实、事件和关系，并通过巩固机制维持效率。<br>
        • 报告 LoCoMo 90.2% 和 LongMemEval-S 85.5% 准确率；证据范围为这两个基准。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Low-Bit GDN Recurrent-State Quantization: Global Gradient-aware Allocation and Pure-Write Sliding Windows</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.39931"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究低比特循环记忆写回误差及近期信息维护。<br>
        • 按未来预测损失敏感度分配精度，并将近期纯写入暂存为 FP8 向量对，离开窗口后再并入历史状态。<br>
        • Qwen3.5-4B/9B 的七任务平均分达 69.83%/78.63%；结果来自所测精度预算及窗口配置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>Don&#39;t Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.40350"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CORAL 让代理主动管理工作记忆，减少长程推理中的上下文干扰。<br>
        • 代理保存进度与已验证事实，重置上下文后继续推理，并通过多阶段强化学习优化检查点。<br>
        • 8B 模型在 GAIA 达到 42.8% 准确率，输入 token 比 ReAct 少约 6–7 倍；另报告跨任务收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-29</td>
      <td style="width: 55%;"><strong>When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.40611"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 联合研究何时调用用户记忆及如何生成主动提示。<br>
        • 同一紧凑解码器从中间层门控，并在一次前向计算中生成记忆支持的建议。<br>
        • 28,058 个决策点显示移除记忆损失 24.7 个精确匹配点；人工评价中单模型仍低于 8B 生成器。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>Is it my preference? Role Grounding Attack against Agent&#39;s Memory via Social Interaction</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38209"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 揭示嵌套社会对话导致偏好被错误归属到受害用户的记忆漏洞。<br>
        • 攻击者发布显式标注来源的经验对话，利用写入时角色绑定丢失，使错误偏好在后续召回影响决策。<br>
        • 在五种记忆系统、六种语言模型上报告工具操纵和隐私泄露风险，强调需保留角色归属。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>What Should a Navigator Remember? Spatiotemporal Memory for Zero-Shot Vision-Language Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38318"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究零样本语言导航应保留什么信息及如何组织记忆。<br>
        • 任务、时序和空间记忆联合保存进展、位姿锚定的压缩观察及几何，供推理器选择路点。<br>
        • 移除时序记忆使平均路径由 16.9 米增至 39.1 米；另在 R2R-CE 与实机场景评估。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>MUSE: Multi-Level Memory with Selective Runtime Injection for Scientific Coding Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38332"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MUSE 将科学编码执行经验组织为全局、方法和实现三级记忆。<br>
        • 根据成败反馈抽取经验，全局库可替换和退役并复核来源；运行时按当前操作门控注入检查建议。<br>
        • 四类科学编码评测及跨核函数基准迁移支持收益；记忆库在测试前冻结。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>Security Impact of Coding Agent&#39;s Memory Files</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38521"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 把项目记忆文件视为可操纵编码代理的持久攻击入口。<br>
        • 在 36 个 SecRepoBench 任务、12 类 CWE 上比较两类恶意指导及无攻击对照，并检查来源披露。<br>
        • 安全完成率变化为 −8 至 +6 个百分点，无一致攻击效果；代理间披露行为差异明显。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>CALM: Conflict-Aware Lifecycle Memory Governance for Long-Horizon Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38573"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CALM 区分持久保存与查询时准入，让过时记忆仍可支持历史重建。<br>
        • 根据支持、冲突和依赖更新有效性，再按时间适用性门控查询证据。<br>
        • 在 LoCoMo、LongMemEval-S 及冲突分析中报告改进；历史重建实验支持保留被替代记录。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>Routed Continual Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38796"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Routed CL 根据任务选择经验应保存在何种记忆系统和状态簇中。<br>
        • 执行前读取簇记忆增强上下文，执行后仅更新被选簇；可保留轨迹、提炼策略或维护结构化状态。<br>
        • 398 个交错实例、四模型中优于全局历史，并降低估计 API 成本；记忆系统库在评价前固定。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-28</td>
      <td style="width: 55%;"><strong>HEDGE: Gated Hypergraph Memory for Scalable Multi-Agent Debate</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.38902"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • HEDGE 用超图组织跨轮、多代理辩论记忆。<br>
        • 超边关联相关论点，内部关系图保留细节；学习门控决定 STORE、BACKUP 或 OMIT。<br>
        • 七基准中相对最强多代理对照平均提升 5.0 点，记忆用量减少 48%；收益依赖所测骨干与任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36652"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • DiscernMem 同时修正流程记忆内容并学习适用边界。<br>
        • 比较单条记忆与无记忆执行，诊断并修复规则，在当前和旧任务复测；元记忆记录各角色使用效果。<br>
        • 四基准、三框架上平均领先最强所报基线 0.51–4.32 点；评价使用单一 Qwen3-4B 骨干。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36713"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • EvoSpeakerMem 区分声纹观测与持久用户身份，保护用户级记忆访问。<br>
        • 因果说话人路由和选择性声学更新引导分区写入与检索，并构建隐藏身份的 LoCoMo-ID。<br>
        • 身份门控 QA 在干净/偏移条件提高 3.86/11.62 点；减少碎片仍可能伴随错误跨用户链接。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>CAMR: Compatibility-Aware Memory Replay for Continual Learning in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36734"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • CAMR 联合控制新样本学习与历史记忆回放。<br>
        • 兼容性检查和学习门控在通用回放、相关强化与跳过已掌握重复项间选择，反馈包括获取、保持和成本。<br>
        • Qwen3-8B-Base 在事实更新及四类任务序列上显示保持收益；结果未覆盖其他模型规模。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36794"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • Select-TTT 针对均匀写入导致的无关内容干扰。<br>
        • 从冻结输出头估计各块对查询的相关性，以温度 softmax 调节快权重写入学习率，无新增参数。<br>
        • 两个基准和两个骨干的长上下文 QA 均改善；多查询长程代理仍是未来扩展。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36918"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TrawMem 将记忆组织为任务导向、角色自适应工作区。<br>
        • 从交互历史构建本地线程，联合选择直接证据与语义相似度较低但互补的记忆。<br>
        • 在两基准、四骨干上宏 F1 提升 2.23–3.14 点；LoCoMo 部分设置同时降低上下文 token。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>TDLM: Adaptive Temporal Integration for Diffusion Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36940"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TDLM 为扩散去噪引入跨步隐藏状态记忆。<br>
        • 冻结去噪器，让未决位置通过因果时序注意力读取自身历史表示，并用自生成轨迹训练。<br>
        • LLaDA 中新增约 0.84% 参数；LLaDA/Dream 上最高报告 7.15 倍生成加速及具竞争力质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall in Frozen Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36948"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SKIM 研究无需外部存储的对话记忆写入与召回。<br>
        • 模型为每回合生成多样问题作键，通过闭式方法把键及对话内容写入参数。<br>
        • 五种语言模型中可由后续用户问题召回多数已存回合；摘要未提供统一定量总分。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>Proactive Memory for Event-Driven LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36967"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ProactMem 强调先验证历史行为规律，再用于主动服务。<br>
        • 近期事件支撑轨迹事实，历史回放评价规律，随后匹配当前事件条件。<br>
        • 提出纵向 ProactiveStream 基准，报告整体 F1 52.6%，相对最强外部基线提升 21.4%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>The Envelope Layer: An Underestimated Surface of LLM Agent Defense</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.37415"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究历史经验记忆如何改变代理消息封装层的防御边界。<br>
        • 在 A2A-TIBA 设置中交叉测试标签强度、封装真实性及成功/失败记忆。<br>
        • 成功记忆提高语义突破率，失败记忆降低；混合经验多回到无记忆基线，结论受攻击与前端范围限制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.37443"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • ETAMem 将异质对话信息解耦为互补记忆视图。<br>
        • 抽取原子单元，增量维护事件、情感、时间层次，并按查询熵分配各视图检索预算。<br>
        • 在 LoCoMo 和 LongMemEval-S 报告 12.46%/7.96% 相对准确率提升，视图分析支持互补性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.37482"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • TAM 将 GUI 已验证进展同时用于当前任务状态和可复用操作学习。<br>
        • 从成功或失败任务的局部成果抽取输入、预期结果及验证条件，按界面兼容性检索并以新观察验证执行。<br>
        • MobileWorld 状态记忆使成功率从 12.0% 升至 28.2%；完整方法相对最强对照提升 17.6%。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>Multi-State Linear Attention with Generalized Second-Order Routing</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.37645"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • MERLIN 用二阶信息改善分段记忆状态的内容寻址。<br>
        • 跟踪各段键的一阶和二阶矩，以查询对齐的均值与方差融合各状态读出。<br>
        • Gated DeltaNet 与 Mamba-2 上的长上下文 QA 和 LongBench 均有收益；验证限于所测多状态模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-27</td>
      <td style="width: 55%;"><strong>SkillMem: Compact External Skill Memory for Latent Multi-Agent Reasoning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.37935"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • SkillMem 将执行经验提炼的文本技能编译为紧凑外部潜记忆。<br>
        • 成败配对轨迹产生技能，经去实例信息和去重后蒸馏；角色条件读出器在后续任务读取同一记忆。<br>
        • 六基准中显示推理与存储收益，每技能约 9.6 KB；评测库离线构建，未证明在线生命周期治理。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.35985"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 发现按访问频率分配条件记忆精度可能损害长尾事实，读取门值更能反映误差影响。<br>
        • GateRQ 将表项编码为逐级一比特残差，根据门控值选择读取深度。<br>
        • 两模型实验在每次读取 2.10 比特时约损失 0.2 个 PopQA 点；准确率和资源收益依赖所测设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Stratum: Repository Memory for Coding Agents Beyond the Context Window</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.36153"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出随代码仓库持久保存、跨模型会话继承的分层经验记忆。<br>
        • 用索引和分页安全工具返回相关知识，并明确已返回内容、剩余内容及成本。<br>
        • 八个真实 bug 的实验中，根因文件定位为 21/24，对照为 6/24；规模较小，属于初步验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.34673"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将智能体记忆选择形式化为预算约束的推荐列表，提出 AgentMemRec。<br>
        • 以候选生成、学习排序和列表组合选择记忆，无需为选择过程调用 LLM，并分解各阶段证据完整性。<br>
        • 在 LongMemEval、LoCoMo 上取得较强结果；与每问 64 次调用的重排器相当，服务成本低 3.2 倍。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Harness-Model Collaboration for Long-Horizon Continual Learning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.34724"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出 HaMo，协同使用快速外部经验积累与慢速模型参数适应。<br>
        • 将轨迹蒸馏为可检索策略卡，训练模型理解和执行策略，再按检索覆盖度选择互补轨迹更新参数。<br>
        • 域内与跨域变化下优于仅使用 harness 或模型适应的比较方法；证据支持保留与迁移的协同作用。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Streaming Recurrent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.34833"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出 Streaming Recurrent Memory，在不保留原始经验的流式约束下维持可用历史状态。<br>
        • 固定输入存储结构并学习读出，支持内容/时间召回、经过步数跟踪和顺序敏感组合，仅使用单步 BPTT。<br>
        • 在关联回忆、在线语言建模和延迟奖励 T-Maze 上有效；结果来自所测流式任务，不能直接外推到大模型部署。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>Adaptive Memory Index Evolution for Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.34977"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出 AMIE，将记忆访问状态的持续更新作为独立于内容修改的适应机制。<br>
        • 从部署检索和语义教师判断累积有界访问状态，重加权后续召回而不改写存储内容。<br>
        • 五种宿主、三基准的 15 组下游比较均提升；频次策略有时更强，误抑制常用记忆会造成失败。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-26</td>
      <td style="width: 55%;"><strong>MemVLN: Streaming Episodic Memory for Vision-Language Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.35066"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=