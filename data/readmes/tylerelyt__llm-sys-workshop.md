# 动手学习大模型系统

**面向 AI 工程师的开源实践项目。通过理解原理、动手实验和构建系统，学习如何解决真实问题。**

调用模型只是起点。面对具体需求，你还需要定义任务、准备数据、设计运行机制，判断结果是否可信，并在效果、成本和复杂度之间做出选择。

这里把模型基础与工程实践连接起来：从一次请求、一个检索实验开始，逐步构建能引用原文的问答系统、能执行工具的工作流，以及能根据反馈持续工作的 Agent。你可以沿着学习路径建立基础，也可以带着工作中的问题，找到相关实验并把方法迁移回自己的项目。

项目持续更新模型原理、工程方法与实践案例。通用聊天调用使用 OpenAI 兼容接口；嵌入、重排、多模态和特定服务实验的要求在各练习中说明。

[开始学习](#开始学习) · [学习地图](#学习地图) · [练习索引](#练习索引) · [系统实践](#系统实践) · [配套专栏](#配套专栏) · [参考阅读](#参考阅读)

## 开始学习

需要具备 Python 基础，能够安装依赖、运行命令和阅读程序。不需要先熟悉某个 Agent 框架。

准备 Python 3.11 或 3.12，以及一个兼容 OpenAI Chat Completions 的模型服务：

```bash
git clone https://github.com/tylerelyt/llm-sys-workshop.git
cd llm-sys-workshop
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install 'openai>=2,<3'
cp .env.example .env
```

在 `.env` 中启用以下配置，填写服务地址、模型 ID 和密钥：

```dotenv
OPENAI_BASE_URL=https://api.example.com/v1
OPENAI_MODEL=your-model-id
OPENAI_API_KEY=your-api-key
```

运行第一次实验：

```bash
python chapter4/model_service/maas_session.py
```

程序记录一个工单号，再分别发起不带历史和携带历史的请求。打开两次请求的消息，找到工单号来自哪里，解释为什么同一个模型会给出不同回答。

接着进入[模型接口、Token 与 Session](chapter4/model_service/README.md)，理解 MaaS 怎样提供生成能力、Completion 与 Chat 怎样组织输入，以及无状态模型怎样由应用维护会话。[环境配置](README-DEEPSEEK.md#setup)说明其他模型服务和各类依赖的配置方式。

## 学习地图

模型与系统的学习相互支撑。下面按知识主题组织材料，每个主题提供独立实验、结果观察和进一步实践的入口。

| 主题 | 要建立的理解与能力 | 入口 |
| --- | --- | --- |
| 技术概述 | 辨析模型概念，理解技术演进和系统发展路径 | [专栏阅读指引](chapter1/README.md) |
| 产业发展 | 理解应用场景、商业化和产业落地 | [专栏阅读指引](chapter2/README.md) |
| 模型的学习机制 | 理解监督学习、表示与迁移，区分预训练能力和任务适配 | [冻结表示、分类头与评估](chapter3/README.md) |
| 语言模型与服务 | 理解 Token、NTP、生成接口、MaaS 与 Session | [模型输入、输出与状态](chapter4/README.md) |
| 后训练与数据 | 理解指令与偏好怎样表达任务要求，检查数据的正确性与覆盖 | [指令数据与偏好数据](chapter5/README.md) |
| 提示与外部知识 | 把资料变成可用证据，定位解析、检索、排序和生成中的问题 | [提示、RAG 与结构化查询](chapter6/README.md) |
| 推理与计算预算 | 比较推理编排与多次采样，核对正确性和额外开销 | [CoT 与自一致性](chapter7/README.md) |
| 工具、状态与记忆 | 实现动作执行和结果反馈，管理当前会话与跨会话状态 | [工具循环与记忆](chapter8/README.md) |
| 系统组织与接入 | 设计规划、失败恢复、上下文管理及工具协议 | [Harness、MCP、CLI 与 Skills](chapter9/README.md) |

第一次学习可以从模型服务出发，再进入下面的文档问答或工具执行实践。学习训练与数据时，结合分类头实验理解参数更新；学习 Agent 时，回到请求和状态管理解释运行机制。

每个实验都要留下自己的判断：预期会发生什么，实际改变了什么，结果支持哪项结论。固定输入和比较条件，保留失败案例，再决定下一步改数据、提示、模型还是程序。

## 练习索引

直接进入具体练习，查看任务、运行命令和结果核对方法；主题入口提供相关概念与阅读材料。

### [模型的学习机制](chapter3/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [冻结嵌入与线性分类](chapter3/frozen_classifier/README.md) | 冻结表示、分类头权重与留出集结果 |

### [语言模型与服务](chapter4/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [标记化、模型服务与无状态推理](chapter4/model_service/README.md) | Token、接口消息、输出预算与 Session |

### [后训练与数据](chapter5/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [Few-shot 指令数据](chapter5/fewshot_data/README.md) | 原始输入、配对示例与目标标签 |
| [Self-Instruct 数据](chapter5/self_instruct/README.md) | 种子扩展、实例生成与过滤决定 |
| [Alpaca 数据格式](chapter5/alpaca_data/README.md) | 指令、输入和答案的字段转换 |
| [偏好数据](chapter5/preference_data/README.md) | 同一提示的候选回答、来源与人工排序 |

### [提示与外部知识](chapter6/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [基础提示方法](chapter6/basic_prompting/README.md) | 任务说明和示例怎样改变回答 |
| [轻量向量检索问答](chapter6/vector_qa/README.md) | 原文、向量召回、引用与固定题集 |
| [检索与重排](chapter6/reranking/README.md) | 召回候选与重排后的入选证据 |
| [知识图谱构建](chapter6/knowledge_graph/README.md) | 实体、别名合并与关系出处 |
| [企业 NL2SQL](chapter6/nl2sql/README.md) | 表结构、只读 SQL 与实际查询结果 |
| [语义去重](chapter6/semantic_dedup/README.md) | 重复片段、版本冲突与来源保留 |
| [切块质量反馈](chapter6/chunk_feedback/README.md) | 回答反馈与片段证据的区别 |
| [跨语言检索](chapter6/cross_language/README.md) | 译文限制与跨语种召回 |
| [迭代图检索](chapter6/graph_search/README.md) | 实际访问的关系与完整证据链 |
| [多模态图像分析](chapter6/image_context/README.md) | 原图与 OCR 保留的信息 |
| [文档提取与问答](chapter6/document_qa/README.md) | 读取范围、页码与原文依据 |
| [法律文书分析](chapter6/legal_qa/README.md) | 条款冲突、原文更新与未知信息 |

### [推理方法](chapter7/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [CoT 与推理编排](chapter7/cot_workflows/README.md) | 多步求解、任务交接与约束保留 |
| [自一致性](chapter7/self_consistency/README.md) | 多次采样、投票、错误与弃权 |

### [工具、状态与记忆](chapter8/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [手写函数调用](chapter8/manual_tool_loop/README.md) | 模型动作、参数处理与实际函数执行 |
| [框架工具调用](chapter8/autogen_tool_loop/README.md) | 同一任务在框架中的执行与停止 |
| [ReAct Agent](chapter8/react_agent/README.md) | 动作、环境观察与后续决策 |
| [计算工具 Agent](chapter8/calculator_agent/README.md) | 计算参数、工具结果与独立复算 |
| [天气工具 Agent](chapter8/weather_agent/README.md) | 地点到天气查询的数据传递 |
| [对话历史管理](chapter8/conversation_memory/README.md) | 窗口裁剪、事实摘要与当前输入 |
| [持久记忆](chapter8/persistent_memory/README.md) | 记忆写入与新进程加载 |
| [文件系统上下文与外部记忆](chapter8/filesystem_memory/README.md) | 文件中的完整观察与恢复上下文 |
| [代码转换与行为校验](chapter8/code_translation/README.md) | 转换后代码的真实运行行为 |
| [代码解释器](chapter8/code_interpreter/README.md) | 生成、执行与独立结果校验 |

### [Harness 与系统接入](chapter9/README.md)

| 练习 | 动手观察 |
| --- | --- |
| [顺序工作流](chapter9/sequential_planning/README.md) | 阶段产物与原始约束 |
| [面向缓存的提示设计](chapter9/prefix_cache/README.md) | 稳定前缀与服务报告的缓存用量 |
| [工具遮罩与动态行为控制](chapter9/tool_masking/README.md) | 状态规则和执行入口的权限守卫 |
| [目标复述与任务管理](chapter9/task_recitation/README.md) | 任务状态与下一轮目标提醒 |
| [错误保留与失败学习](chapter9/error_recovery/README.md) | 失败轨迹、恢复与重试预算 |
| [反思与改进](chapter9/reflection/README.md) | 评审依据、改写与可复用经验 |
| [MCP 工具发现与调用](chapter9/mcp_tools/README.md) | 工具发现、参数结构与真实调用 |
| [飞书远程 MCP](chapter9/feishu_mcp/README.md) | 用户凭证、权限与远程文档搜索 |
| [CLI Skill 与扫码授权](chapter9/cli_skills/README.md) | 扫码授权、命令复用与技能封装 |
| [Pi SDK 与技能加载](chapter9/pi_skills/README.md) | SDK 会话和技能加载前后的行为 |
| [检索服务接入 Harness](chapter9/rag_mcp/README.md) | 工具返回的原文、版本与最终引用 |
| [用 MCP 实现 Agent Loop 与 Harness](chapter9/mcp_harness/README.md) | 上下文组装、工具执行、观察写回与循环接续 |

## 系统实践

独立实验帮助理解机制，系统实践把这些机制用于同一个问题。以下给出构建顺序和需要核对的结果；各练习保留独立运行入口，不需要先安装整套项目的依赖。

### 从标注数据构造训练候选

把同一批标注文本构造成指令记录，再转换为独立的任务输入，最后为同一提示生成并复核候选回答。[数据实践](chapter5/README.md#串联数据构造实践)提供完整命令与文件流向，Self-Instruct 则独立扩展种子任务。

沿每条记录回查原始文本与标签，检查转换有无丢失条件或混入答案，再依据明确标准复核偏好。格式有效、生成成功与数据可用于训练分别判断。

### 构建有据可查的文档问答

目标是回答一组真实问题，能追溯原文，并识别资料无法回答的情况。

1. 用[向量问答](chapter6/vector_qa/README.md)建立最小系统。先写问题和参考依据，再批量检查召回、回答与引用，得到基线。
2. 遇到漏答或误答时，沿原文到答案追踪原因。按问题选择[文档提取](chapter6/document_qa/README.md)、[切块反馈](chapter6/chunk_feedback/README.md)或[检索与重排](chapter6/reranking/README.md)，在固定题集上核对修改的收益与代价。
3. 用自己的语料和题集复跑。需要让 Agent 主动查询时，再参考[检索服务接入 Harness](chapter9/rag_mcp/README.md)，检查工具结果、语料版本和最终引用。

最终应能展示：哪些问题答对、哪些没有依据、失败发生在哪里，以及一次修改为什么值得保留。不同检索练习使用各自的教学语料，迁移时需要对齐文档结构和评估问题。

### 构建能正确执行的工具工作流

目标是让模型完成需要计算和外部操作的任务，并能追踪实际执行过程。

1. 从[手写工具循环](chapter8/manual_tool_loop/README.md)追踪决策、参数、执行和反馈，用独立计算核对结果。
2. 在[框架工具调用](chapter8/autogen_tool_loop/README.md)中完成同一个任务，比较框架承担了哪些工作，再结合[顺序工作流](chapter9/sequential_planning/README.md)判断哪些步骤适合由程序固定。
3. 通过[MCP 工具](chapter9/mcp_tools/README.md)学习协议接入。需要企业文档时，分别完成[飞书 MCP](chapter9/feishu_mcp/README.md)和[CLI Skill](chapter9/cli_skills/README.md)，比较真实授权、调用和结果。

最终应能解释：模型选择了什么、程序执行了什么、错误怎样传递，以及为什么选择当前的接入方式。协议、认证流程、技能说明和运行框架分别承担不同职责。

### 构建能根据反馈工作的编程 Agent

目标是让 Agent 读取代码、发现缺陷、修改实现并验证结果，同时控制权限和状态。

先理解[会话历史](chapter8/conversation_memory/README.md)与[文件系统记忆](chapter8/filesystem_memory/README.md)，再用[MCP Harness](chapter9/mcp_harness/README.md)运行一个完整编程任务。沿测试失败、工具观察、修改和复测检查结果，并用新的进程恢复任务。

这里可以直接观察 **Agent = Model + Harness**：Model 根据输入生成回答或动作，Harness 组织上下文、执行动作、保存状态并控制循环。分别更换模型和运行策略，检查权限、预算与任务结果怎样变化。

最终应能用实际代码与测试解释任务是否完成，并说明模型能力、运行机制和工具环境分别影响了什么。

![编程 Agent 的实际工具调用与测试结果](chapter9/mcp_harness/images/mcp-harness-tests.png)

*编程 Agent 随课示例：从真实工具调用和测试输出检查修复结果。*

## 配套专栏

- [大模型系统实战](https://time.geekbang.org/column/intro/100613101)：模型基础、系统架构与工程实践。
- [前沿模型实战课](https://time.geekbang.org/column/intro/100828301)：模型调用、推理、检索增强与智能体应用。

技术概述与产业背景通过专栏学习。模型与系统主题可结合实验阅读：用原理解释观察到的行为，再把实验结果带回方案设计。

## 参考阅读

结合实践阅读原始论文和工程文章，理解方法的假设与适用范围。各主题的阅读说明给出关注点，便于从实验回到原理。

- **模型原理**：[Attention Is All You Need](https://arxiv.org/abs/1706.03762)。继续阅读[预训练与迁移](chapter3/README.md#参考阅读)、[语言模型与推理服务](chapter4/README.md#参考阅读)。
- **数据与后训练**：[Self-Instruct](https://arxiv.org/abs/2212.10560)、[通过人类反馈训练语言模型遵循指令](https://arxiv.org/abs/2203.02155)。更多见[后训练阅读](chapter5/README.md#参考阅读)。
- **检索增强**：[RAG 原始论文](https://arxiv.org/abs/2005.11401)。更多见[检索、图谱与文档处理](chapter6/README.md#参考阅读)。
- **推理方法**：[CoT](https://arxiv.org/abs/2201.11903)、[Self-Consistency](https://arxiv.org/abs/2203.11171)。更多见[推理与搜索](chapter7/README.md#参考阅读)。
- **工具与记忆**：[ReAct](https://arxiv.org/abs/2210.03629)、[MemGPT](https://arxiv.org/abs/2310.08560)。更多见[智能体构建](chapter8/README.md#参考阅读)。
- **Harness 与上下文工程**：[构建 Manus 的上下文工程经验](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)。更多见[认知架构与交互协议](chapter9/README.md#参考阅读)。

## 一起完善

欢迎带着工程问题参与：修复代码、改进讲解、补充失败案例，或分享一种经过验证的实现。新增实践应说明解决的问题、运行方式与结果判断方法；涉及外部服务时写清依赖和授权。

[问题与建议](https://github.com/tylerelyt/llm-sys-workshop/issues) · [贡献代码](https://github.com/tylerelyt/llm-sys-workshop/pulls) · [贡献者](https://github.com/tylerelyt/llm-sys-workshop/graphs/contributors) · [MIT 许可证](LICENSE)
