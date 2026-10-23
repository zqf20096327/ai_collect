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
[![Papers](https://img.shields.io/badge/Papers-1271-blue.svg)](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/papers)
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
      <td rowspan="2" style="width: 15%;">2026-10-22</td>
      <td style="width: 55%;"><strong>Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.30698"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究内容不变时，记忆有效性状态损坏如何影响语言智能体。<br>
        • 对 731 个基础实例和 2,080 对样本扰动治理属性，并区分离线投影与下游回答评估。<br>
        • 控制面 96.25% 配对发生投影变化；下游非概率抽样面板有明显正确率损失，不能用代理指标代表整体安全。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-22</td>
      <td style="width: 55%;"><strong>Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.30755"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 用原始历史证据检索检验结构化或压缩记忆的信息损失。<br>
        • 直接保留原始历史并组织证据召回，比较压缩或抽取记忆带来的信息损失。<br>
        • 七种基准-模型设置中六种领先，增益 0.13–5.53；不能推广为所有任务都无需结构化记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-22</td>
      <td style="width: 55%;"><strong>Retrieval-Augmented Online Textual Memory for Episodic Memory Video Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.31284"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究视频情节记忆中检索单元、上下文覆盖与问答质量的关系。<br>
        • 以细粒度匹配选择记忆，再返回包含上下文的父级描述供问答使用。<br>
        • Ego4D 闭集问答达 56.4；更大覆盖不总带来更好问答，结果限报告设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-22</td>
      <td style="width: 55%;"><strong>The Value of Memory in Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Evaluation-blue" alt="Memory Evaluation"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.31303"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从下游决策损失刻画记忆价值与证据恢复成本。<br>
        • 以任务损失和证据恢复前沿刻画记忆价值，用反例检查通用分数的不足。<br>
        • 在 LoCoMo、更新和纵向诊断上分析；结果支持任务依赖评价，不给出通用单一最优分数。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-22</td>
      <td style="width: 55%;"><strong>Muffin - A Shared Memory Buffer for Asynchronous AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.31355"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过异步共享中间发现协调多语言模型智能体的协作。<br>
        • 共享可复用发现但保持各代理私有推理，以异步读写协调协作。<br>
        • 20 项设置中 17 项最好；相对辩论基线报告准确率提高 19.2%、标记减少 77.4%，限所测协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-22</td>
      <td style="width: 55%;"><strong>When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.31446"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 根据待执行动作的风险决定何时复核旧记忆。<br>
        • 按动作风险选择验证并以信息价值停止，区分安全继续、补证与阻断。<br>
        • ToolSandbox 成本降 33.9% 且所测安全继续召回 100%；AppWorld 成本降 21.3%，质量略有损失。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>SpatialBrain: Spatial Intelligence Growing from Experience</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29317"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在固定视觉语言骨干外积累过程经验，指导后续空间推理。<br>
        • 在任务块结束后整合无答案、无坐标的执行记录，更新策略和程序可用性供后续块使用。<br>
        • 五个基准四升一平；反馈衡量执行可靠性和成本，不是答案正确性奖励。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29329"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 让高层视觉语言模型保存语义事件与可执行子任务记忆。<br>
        • 视觉语言模型写入语义事件与子任务记忆，用两阶段验证监督记忆使用。<br>
        • RoboMME 56.05 对 44.51；四项真实任务平均 60.83，对照为 45/28.33，规模有限。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>Memory-Centric Continual Learning for AI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Survey-blue" alt="Memory Survey"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29357"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 围绕记忆资产、维护策略和生命周期提出持续学习框架。<br>
        • 以概念分类整理记忆载体、管理操作及内层状态和外层策略更新，提出保留、适应、迁移评价。<br>
        • 提供概念与评测框架；不能视为新算法已获实验证实的性能提升。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>When Thoughts Become Memory: Unifying In-Context Learning and Fine-Tuning</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29419"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 量化未见信息存于上下文或权重时的记忆价值。<br>
        • 以信息恒等式、先验和修复解码损失区分上下文与参数中的记忆信息。<br>
        • GPT-2 在限定流选择测试给出证据；认证依赖设定，不等同所有推理模型的机制结论。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29467"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 用置信信念和惊讶度区分真实用户变化与噪声。<br>
        • 以惊讶度门控更新，对噪声证据暂存，维护用户画像并修正冲突信念。<br>
        • 在三个基准及 DiMoBench 评估；阈值与置信度设计仍依赖任务分布。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29671"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 联合学习记忆写入与检索，并分配后续任务反馈的信用。<br>
        • 联合训练记忆构建与检索，以阶段分解策略优化和事件级信用分配衔接两者。<br>
        • LoCoMo、LongMemEval 上优于所测 RL 基线；结论限所用任务和训练协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29869"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究上下文压缩丢失来源信息时产生的指令洗白风险。<br>
        • 比较扁平压缩与带类型的来源保留，并检验压缩后低信任内容变成指令的风险。<br>
        • 五种扁平方式攻击率 87–100%，四种类型化方式未观察成功；有限实验不等于普遍免疫。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.29995"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以类型化超图连接实体身份、状态变化和来源证据。<br>
        • 用类型化超图保留实体身份和状态关系，以代理搜索检查来源而非扁平近邻召回。<br>
        • 三个基准报告提升 8.20–9.98%；依赖报告的读者、图构建及评价设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-21</td>
      <td style="width: 55%;"><strong>MemPlan: Memory-Conditioned PDDL Planning for Partially Observable Text Environments</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.30379"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 联合保存成功规划知识和被执行结果否证的假设。<br>
        • 在固定 PDDL 域保存成功规划知识和被否证假设，由语言模型解析、落地并复用。<br>
        • TextWorld、ALFWorld 和 Robotouille 改善规划效率；依赖固定领域与符号接口。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>What should AI forget? A design and taxonomy for negative space governance in AI memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27607"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究用户不希望助手记住的信息，以及可交互的记忆排除规则。<br>
        • 从 179 个事件、146 名用户归纳 15 类不应保留内容，设计政策门控与用户覆盖机制。<br>
        • 15 人设计研究支持交互方案；不是形式化隐私或全面遗忘保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>Memory as Code: Declarative Retrieval over Codified Long-Term Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27700"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 把长期记忆编码为分层可执行表示，并用声明式查询组合事实。<br>
        • 将记忆编译为原子函数、关系与组合层，以声明式程序执行查询。<br>
        • LoCoMo、LongMemEval 报告最高 15.91% 相对评判器增益；依赖编译正确性及所测协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>EventSync: Event-Driven Memory Updates for History-Dependent Manipulation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27917"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以经过验证的子目标完成事件触发历史记忆更新。<br>
        • 只有视觉状态和末端执行器监控共同确认完成后才写入历史，避免未完成步骤污染记忆。<br>
        • RoboMME 64.5、提高约 20 点，并评估四项真实任务；验证质量仍依赖监控。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.28315"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究助手记忆与用户敏感信息披露之间的反馈循环。<br>
        • 模拟用户与助手的披露循环，测试记忆引出的预设性回答和响应防护。<br>
        • 24 个属性、四个模型中防护降低披露；模拟行为不能直接代表真人隐私反应。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.28810"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析持久助手记忆注入的跨会话传播与跨用户影响。<br>
        • 测试多种服务中的记忆注入、后续会话影响及组织范围传播。<br>
        • 三个服务的攻击合计覆盖多类目标；不能据此声称每个平台对所有攻击均易感。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.28882"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将机器人情节编码为固定大小的参数增量，支持语言问答与动作解码。<br>
        • 将视频编码为相对元初始化的权重增量，以固定记忆支持语言问答及动作解码。<br>
        • 报告 R² 0.51 和噪声下优势；限所测任务，不证明通用具身长期记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-20</td>
      <td style="width: 55%;"><strong>PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.28987"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为持久记忆的权限释放建立有限接口完整性模型。<br>
        • 在有限接口上形式化完整性约束，只信任用户或门控确认记录，并测试投毒。<br>
        • Lean4 证明依赖明确接口假设；TrojanHippo 未观察攻击成功，不能外推到任意代理。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>Cognitive Maps in Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25596"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过内部干预检验语言模型关系记忆的键值绑定与组合。<br>
        • 以关系绑定探测和因果干预检查认知地图是否体现为键值式关联记忆。<br>
        • 较大模型出现组合式错误记忆；证据基于合成实体关系，不能等同真实世界全局坐标地图。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>Weighted State Souping for Efficient Long-Context Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25621"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 按查询加权组合缓存的状态空间记忆，增强选择性召回。<br>
        • 按查询权重组合已缓存块状态，检验多跳、变量追踪及工具使用。<br>
        • 支持固定状态组合的可行性；理论与合成测试不能证明任意长程语言任务的可靠记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25707"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 审计共享记忆中的凭据归属及其对跨用户误用的影响。<br>
        • 区分记忆中看到凭据与实际误用，构造归属压力测试并加入所有者绑定。<br>
        • 305 例中绑定将误用由 92 降至 1，但牺牲 3–5 个任务；暴露率不应等同滥用率。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>CoMem: Learning to Anticipate Failures from Retrieved Experience</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25790"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 结合检索案例与学习到的失败假设，在执行前预判风险。<br>
        • 从成功与失败经验学习预判错误，将检索记录转为任务条件化的失败假设。<br>
        • 两种主干、五类任务有收益；跨分布效果依赖经验覆盖和检索质量。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>ACE-Trader: Adversarial Co-Evolution for Generator-Critic Trading Systems</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25847"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以完整交易流水线反馈更新生成者和评审者的角色经验记忆。<br>
        • 以实际执行反馈更新近期记忆选择器，从共享交易记录提炼各角色可复用经验。<br>
        • 与 22 个基线比较，但依据市场回测；不构成未来收益保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26995"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从成功执行中抽取 Skill-DAG，维护可复用流程记忆。<br>
        • 对成功轨迹反向切片提取必要依赖，复用成功时强化或修订模板，失败只更新可靠性。<br>
        • ALFWorld 成功率 87.1%、SkillsBench 奖励 38.38；效果依赖检索和执行能力，训练评估轨迹分离。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>Learning What to Remember: Resource-Efficient Self-Improvement for Lifelong Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26453"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从执行反馈学习经验的情境价值，指导预算内的检索与保留。<br>
        • 从稀疏任务反馈学习查询条件下的记忆价值，在固定预算内检索和维护经验。<br>
        • 三个 LifelongAgentBench 设置报告最高成功率和较低标记量；依赖预算及反馈分布。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26503"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析潜在记忆如何控制冻结 GUI 智能体的动作修订范围。<br>
        • 控制潜在记忆何时允许改写初始动作，区分历史信息贡献与动作修订效果。<br>
        • 分析显示部分增益来自修订范围控制；三基准结论不能简单归为记忆信息增加。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>ReInsVLN: Revisiting Historical Evidence for Training-Free Vision-and-Language Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26545"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过历史证据压缩与计划性重读改善冻结模型的语言导航。<br>
        • 保持导航模型冻结，压缩历史证据并按计划重读指令与相关观察。<br>
        • 两主干 R2R 成功率约 64.3/64.4，增 8.48/3.37 点；收益限报告导航配置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>BetaMem: Learning to Remember a Changing World for Embodied Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26554"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以可执行写入契约学习维护有来源支持的具身记忆。<br>
        • 六层记忆以可执行写入契约维护支持关系，经监督学习和验证反馈优化。<br>
        • 报告多个具身/对话基准收益及成本下降；不同任务协议不可直接混作统一成绩。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27032"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过长期执行经验与短期任务指引的闭环优化支持长程规划。<br>
        • 成功轨迹精简里程碑，失败轨迹与成功案例对比补充洞见，回写后供新任务生成指引。<br>
        • ALFWorld、Webshop、PDDL 上改善成功率和效率；依赖模拟任务与所测模型。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>LVMem: Image-Augmented Memory for Long-Horizon Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27104"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为长程问答记忆保留原图引用，并按需复查视觉证据。<br>
        • 通过对象线索和光流选择帧，语言模型按需查看关联图像补足文本记忆。<br>
        • OCNaVQA 两种主干有收益；未构建显式三维图，结论限所测长程问答。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>AutoRedClaw: Automated Red-Teaming for Claw-Style Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27244"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 自动生成并执行针对持久助手状态的投毒攻击与评测环境。<br>
        • 自动生成并在环境中验证持久状态投毒，跨代理框架与模型测试。<br>
        • 330 例、七种框架和四个模型多数攻击率超 50%；生成和筛选分布限制普遍性。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27377"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 联合设计编码经验的存储、困难时召回和使用后驱逐。<br>
        • 先存约百倍缩小的经验描述，受阻才召回实现，使用一次后移出活跃上下文。<br>
        • SWE-Ctxt-Lite 匹配率 68.7 对 55.6，解决率 27.6 对 24.9，成本降 17%；限该协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27400"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将感知事件与延迟意图关联，支持长期前瞻记忆和主动协助。<br>
        • 将意图与感知线索及情节记录关联，检索合适时机触发未来行动。<br>
        • CPMBench 含 1,000 例八类任务，所测方法表现较好；不代表真实长期个人部署已验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-19</td>
      <td style="width: 55%;"><strong>More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.27406"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析持久经验抽象导致的错误再生，并提出按任务丢弃合成指引。<br>
        • 保留执行事实与结果，每任务丢弃合成指引，并自适应选择可复用经验。<br>
        • 所测留出任务取得较好成功率与调用成本；并非证明所有持久抽象记忆有害。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>MemPrice: Online Memory Allocation via Adaptive Pricing for Long-Horizon Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24955"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 把有限上下文中的记忆保留及表示粒度建模为在线资源分配。<br>
        • 累积记忆压力转为上下文价格，按估计保留价值分配粒度，并跨刷新维持占用控制。<br>
        • 在四个基准比较匹配预算；遗憾保证相对同状态基准且依赖规律性与次线性估计误差。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25100"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 学习块级参数记忆，并与冻结语言模型的隐状态融合。<br>
        • 因果预测器生成块级记忆，用检索嵌入监督门控交叉注意力融合。<br>
        • 报告 32 倍更少查询及 2,048 倍更少检索项，QA 与领域任务提升；倍率依指定对照。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25119"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将经验价值表示为可随任务和执行反馈修订的信念。<br>
        • 将记忆作为可更新信念，结合任务结果校准其可信度和执行价值。<br>
        • 推理和代码任务报告收益；置信度更新仍依赖反馈质量与任务分布。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Memories That Outlive Their Reasons: Dependency-Tethered Memory for Tool-Using LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25123"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 把记忆绑定到具体证据版本，并撤回失去支持的记录。<br>
        • 为记忆记录确切依赖版本，在支持失效时撤销资格并只复查相关依赖。<br>
        • Fallout 不安全行为 62→0.3%，较全查少 37% 检查；较弱写入器会削弱收益。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>LAMB: Latent Multi-Hypothesis Beliefs for Long-Horizon Large Language Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26955"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在循环潜在记忆中保留共享证据和多个竞争假设。<br>
        • 递归保存共享证据和增量假设，按结果更新权重，以模仿和辅助目标训练前缀策略。<br>
        • ALFWorld、ScienceWorld、Crafter 报告增益；多假设保留价值限所测部分可观察任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25179"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分离持久记忆的写入状态认证与查询时使用资格。<br>
        • 分离写入认证与读取资格，以析因实验测试状态治理和当前问题相关权限。<br>
        • 特定状态正确设置下读取门控消除测得泄漏；不能视为无条件防护。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Improving the Expressive Power of Hybrid Sequence Models via Multi-Hop Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25250"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析共享键值记忆的多跳读取如何增强混合序列模型的表达力。<br>
        • 让固定次数的检索逐步组合函数，分析与单次 top-k 检索的表达能力差异。<br>
        • 给出复杂度分离并在合成任务验证；不能直接推断自然语言长上下文性能。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Atoms, Not Knowledge: What Production-Scale Addressed-Memory Writes Deposit</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25317"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 审计大规模寻址记忆写入后的事实覆盖与组合使用能力。<br>
        • 扩大写入事实数量，区分存储覆盖、给定证据与真实召回以及组合使用。<br>
        • 50→1,000 事实时覆盖由 98% 降至 12.7%；组合近基线，干扰与容量成因尚未分离。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-18</td>
      <td style="width: 55%;"><strong>Let Them Sleep: Recursive Self-Pruning Memory for Long-Horizon LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.25561"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在休整阶段把失败情节整合为规则，并递归修剪记忆。<br>
        • 休整阶段聚类失败、提炼规则并删除旧情节，按复用效果衰减或晋升记忆。<br>
        • 三个设置报告提升且条目减少；含模拟任务，不能推广为所有代理都需同样休整机制。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-17</td>
      <td style="width: 55%;"><strong>PACE-Mem: Prefix-Aware Complementary Evidence for Multimodal Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24378"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 为多模态长期记忆选择互补证据并自适应决定读取长度。<br>
        • 先池化查询相关记录，再以 MMR 形成互补证据序列，并从相邻分数下降选择前缀长度。<br>
        • 三个长视频基准、两个框架平均较 Adaptive-k 提高 1.6%；保持写入和生成不变，限片段式记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-17</td>
      <td style="width: 55%;"><strong>Memory Internalization via Test-Time Training for Long-Video Understanding</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26910"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将长视频知识压缩为逐视频适配参数，支持不再输入视频的语言问答。<br>
        • 以因果追踪选择写入层，再蒸馏视觉片段带来的表征变化，生成只读文本的逐视频参数记忆。<br>
        • 在三个长视频基准减少合成监督需求并改善无视频问答；结论限逐视频适配设置。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-17</td>
      <td style="width: 55%;"><strong>Hippo: Training-Free Agent Self-Evolution via Hippocampal Replay</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24453"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过多次执行尝试的对比回放整合持久经验，修订重复或冲突的指引。<br>
        • 对比同任务多次尝试以提炼经验，再与现有记录合并、消解冲突并修订适用条件。<br>
        • 三个代码/网页基准均提升且保存更少经验；无整合的累积基线后期可低于无记忆。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-17</td>
      <td style="width: 55%;"><strong>Write Once, Query Many: Evolving Compact Reusable Memory for Long Videos</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24537"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 在未来问题未知时一次构建可复用的多模态视频记忆。<br>
        • 视频一次写入多尺度记忆；写入器按来源保真演化，读取器按证据定位及使用错误演化。<br>
        • 相对未演化框架平均提升 7.2%；存储较原视频约降 99.86%，成本和精度结论限所测视频 QA。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-17</td>
      <td style="width: 55%;"><strong>MemRevise: A Self-Revising Memory for Conversational Search</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24672"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 提出可修订会话记忆图，支持主题事实的停用与重新激活。<br>
        • 3B 写入器逐轮记录添加、放弃和恢复操作，记忆图保留被停用主题的事实以便再激活。<br>
        • CONVREVISE 含 4,429 问；固定检索器平均 MRR@10 为 0.701，CORAL 上与强重写器统计持平。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-17</td>
      <td style="width: 55%;"><strong>How Intervention History Changes AI Agent Sabotage on Subsequent Tasks</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.26935"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究跨任务保留的干预历史如何改变语言智能体后续的破坏行为。<br>
        • 对后续新任务配对比较无历史、被替换通知和可信模型替代内容，并测试历史压缩。<br>
        • IaC 上一模型双目标成功率由 77% 降至 12%/38%；其他模型效果不显著，不能归因于反馈本身。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>GRAD: Graph-Structured Antibody Defense for LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22828"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以执行图聚合跨操作的攻击证据，检测记忆投毒及分解攻击。<br>
        • 图模块聚合操作文本、事件属性和关系；冻结编码器专家按可观察签名路由，持续添加检测能力。<br>
        • Decomp/MCP/MRT AUROC 为 97.19/77.59/86.60%；同时覆盖分解攻击，不能将所有收益归于记忆防御。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Memory%20Security-blue" alt="Memory Security"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22959"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 按主张的类型、权威和范围治理持久记忆的使用权限。<br>
        • 为主张标注治理标签，并在来源句、实体和主张图上按查询权限筛选可用记忆。<br>
        • 四个主干的 MPBench/LoCoMo 上较保留合法记忆的最强防线攻击率至少低 77%；并非无条件安全保证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23313"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将长期记忆寻址与回答证据编译分离，在预算内组织跨会话支持。<br>
        • 寻址层定位描述与容量受控单元，规范化为稳定来源包，证据层按查询预算组合并呈现主张。<br>
        • LoCoMo Judge Accuracy 80.52%，LongMemEval-S 也有收益；指标依赖评判器和报告协议。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23574"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将交互经验提炼为情节记录与技能补丁，并以受控生命周期整合更新。<br>
        • 从交互提炼经验，按上下文命中、效果和效率评分，执行试用、晋升、竞争替换及淘汰。<br>
        • WildClawBench 与递归优化任务报告收益；评分包含 LLM 归因，不能视为严格因果验证。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>MARS: Memory-Aware Routing for Session-Level LLM Assistants</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23583"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 让共享会话状态联合控制记忆视图构造与模型选择。<br>
        • 查询/主题管理器提供共享会话状态，同时指导固定记忆构造策略和在线模型路由。<br>
        • RealMem 保留全上下文 GPT-4o 的 98.2% QA、调用成本 14.5%；MultiChallenge 总体仍落后最强静态系统。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23598"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 针对语义相似却时间不符的记忆检索，学习证据时间窗口。<br>
        • 1.7B 定位器用 RL 推断证据时间窗，再融合时间/语义通道并按窗口邻近度重排。<br>
        • LifeBench 61.52%、LoCoMo 78.96%；结果支持时间约束召回，限所测长期生活记忆数据。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Procedural%20Memory-blue" alt="Procedural Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23709"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 从产品优化执行反馈形成可维护的流程行为手册。<br>
        • 编辑器应用行为、反思器提案、审核器去重、管理器提交，并停用持续有害行为。<br>
        • 行为结构、反馈演化与审核改善效果和下行风险，并迁移到未见类别；结论限产品优化任务。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>Learning Personalized Memory Gating from Delayed One-Sided Feedback</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23812"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 学习用户特定的事实写入门控，在有限预算下保留有用记忆。<br>
        • 以后续检索并进入回答的事实作标签，Warm-Start UCB 结合离线初始化和用户在线单侧延迟反馈。<br>
        • 不同预算/历史长度下优于基线；遗憾界依赖延迟窗口与特征假设，检索使用标签不等于用户价值。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>Cache2LoRA: Understanding and Improving Context Internalization</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24107"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 研究文档写入低秩参数后的事实保持与回答适应。<br>
        • 冻结文档缓存按查询聚合证据生成 LoRA，以多风格监督同时训练事实保留和回答表达。<br>
        • 17 项任务宏 F1 0.663，接近全上下文 0.671；固定大小干扰测试支持 LoRA 保留优势。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>A Conditional No-Hair Theorem for Transformers: How Language Models Forget Their Prompt</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/LLM%20Memory-blue" alt="LLM Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24133"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 分析语言模型隐状态中的提示记忆如何随续写衰减。<br>
        • 固定续写文本比较不同提示的隐状态差异，分析注意力稀释和续写接力，并干预 logit 偏置。<br>
        • 衰减界依赖有限深度、有界 logits 和非零前归一化激活；行为信息仍可由生成文本承载。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-16</td>
      <td style="width: 55%;"><strong>Reasoning with Context Management and External Memory</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.24187"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以外部记忆保存推理中间信息，减少上下文管理造成的重复计算。<br>
        • 上下文管理时把额外中间信息保存到外部记忆，避免重复计算又不扩张主模型上下文。<br>
        • 少量数学问题上降低重复步骤时间并改善复杂任务；实验含 0.4–25M 小模型及 GPT-2。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>ProV-Mem: Proactive Memory for Streaming Video Question Answering</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.23998"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 通过触发记忆和情节记忆协调流视频助手的响应时机与内容。<br>
        • 触发记忆决定何时查询，固定指令先验指导内容，情节记忆过滤重复输出，并提出成本敏感 CAUC。<br>
        • 四种视频场景 CAUC 最佳；分解界依赖条件充分性假设，指令先验本身并非学得持久经验。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22556"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 以计划变化触发 VLA 关键视觉事件的有界记忆写入。<br>
        • 比较对齐未来动作预测的计划分歧，用选定信号触发视觉写入，再屏蔽机器人自身冗余帧。<br>
        • 事件检测 ROC-AUC 0.981–0.997，所测关键观察保留率 100%；该指标不是任务成功或物理安全。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>From Relevant Memories to Sufficient Evidence: Rethinking Memory Utilization in LLM Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22668"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将相关记忆组织为具有充分支持的回答证据集。<br>
        • 多粒度发现后生成绑定来源的 ViewCards，再按充分性选择性补回缺失信息，不改写原存储。<br>
        • 共享存储下 LoCoMo Judge Accuracy 91.43%，较 MemR3 高 7.6 点；结果依赖指定读者和评判器。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Not All Graphs Are Maps: A Task-Agnostic Exploration Framework for Mobile GUI Navigation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22672"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 将任务无关的 GUI 探索转为可复用目的地和路线记忆。<br>
        • 评价指令出现前离线探索，保存功能、页面和路标；对照无记忆、随机、BFS 与干净图。<br>
        • 导航成功率 UI-TARS 52.4→58.3%、Qwen-VL 59.5→71.4%；只评估到达执行前页面，不是完整任务成功。
      </td>
    </tr>
    <tr>
      <td rowspan="2" style="width: 15%;">2026-10-15</td>
      <td style="width: 55%;"><strong>Spatial Memory by Agents, for Agents</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22736"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 使用编码智能体自动设计空间记忆构建与检索程序。<br>
        • 设计代理反复编写记忆代码，用固定查询代理反馈搜索；测试前冻结实现，未见下游问题。<br>
        • 三次搜索五轨平均 44.23 对最强全轨基线 29.32；仍有定位与证据使用失败及计算权衡。
      </td>
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
      <td style="width: 55%;"><strong>ECHOES: Seeing Beyond the Current Image via Recursive History Compression and Privileged On-Policy Distillation</strong></td>
      <td style="width: 15%;"><img src="https://img.shields.io/badge/Agent%20Memory-blue" alt="Agent Memory"></td>
      <td style="width: 15%;"><a href="https://arxiv.org/pdf/2610.22408"><img src="https://img.shields.io/badge/arXiv-Paper-%23D2691E?logo=arxiv" alt="Paper Badge"></a></td>
    </tr>
    <tr>
      <td colspan="3">
        • 训练 GUI 智能体把视觉历史递归压缩为保真的文本记忆。<br>
        • 压缩-思考-行动格式更新历史状态；训练时多图教师指导学生，并按感知-记忆保真差距平衡目标。<br>
        • 四个 GUI 基准与 ECHOESBMK 改善任务和保真，部署不保存历史截图；依赖特权训练信息。
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
      <td style="width