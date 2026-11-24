# AI Agent 从入门到实战

> 作者：青松与桑叶 | 理解本质，而非堆砌框架

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![check](https://github.com/2182977liu-bit/awesome-ai-agent-learning/actions/workflows/check.yml/badge.svg)](https://github.com/2182977liu-bit/awesome-ai-agent-learning/actions/workflows/check.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Updated](https://img.shields.io/badge/内容更新至-2026.11-brightgreen)

## 写在前面

2024 年到 2025 年，AI Agent 迎来了爆发式增长。而到了 2026 年，这个领域发生的变化比前两年加起来还大：MCP 成了工具连接的事实标准并搬进了 Linux Foundation，A2A 让不同厂商的 Agent 开始互相协作，AutoGen 归档、微软把两个框架合成了一个，"上下文工程"取代"提示词工程"成了新的核心话题。

**这个仓库的内容也跟着做了一次大更新。** 老版本停在 2024–2025 年的认知上，路线图里还有一半章节是空的。这次更新补齐了协议层、上下文工程、框架选型、多 Agent 协作和评估这五块，并把所有失效链接和过时推荐都清理了一遍。

我的教学理念没变：**先理解原理，再学框架；先动手写，再学理论。** 只有亲手用纯 Python 从零实现一个 Agent，你才能真正理解 LangGraph、Claude Agent SDK 这些框架在帮你做什么。否则，你只是在调 API，而不是在构建智能体。

2026 年发生的一件事更能说明这条路线的价值：**OpenAI 宣布 Agent Builder 于 2026 年 11 月 30 日退役**，官方建议需要继续以代码形式运行的工作流转用 Agents SDK。可视化平台会更迭，底层原理不会。

这个教程和其他教程最大的区别在于：它是**保姆级**的、**从零开始**的、**每一步都可运行**的中文内容。不会假设你已经懂了什么，不会跳过任何关键步骤，不会用一堆术语把你绕晕。每一行代码都有中文注释，每一个概念都有通俗的解释。

> **关于内容来源**：本项目主体为中文原创。2026-11 新增的第 9–13 章采用**转译 + 多来源整合**方式写作 —— 以英文一手资料为事实依据，用中文重新组织重写，并补充原创的解释、代码与练习。每一章章首都标注了来源，逐篇的来源、改动与原创部分说明见 **[SOURCES.md](SOURCES.md)**。

## 你将收获

- 🧠 理解 AI Agent 的核心原理（ReAct、工具调用、记忆系统、规划与反思）
- 💻 不依赖任何框架，用纯 Python 从零构建一个完整的 Agent
- 🔌 掌握 **MCP**，把工具做成即插即用、跨框架可复用的标准组件
- 🧮 掌握 **上下文工程**，让 Agent 连续工作几小时而不跑偏
- 🧭 看懂 **2026 框架全景**，按场景选型而不是背排行榜
- 🤝 理解 **A2A 协议**，让互相不透明的 Agent 安全协作
- 📊 建立 **评估与可观测性** 闭环，用 pass^k 而不是"感觉还行"来决定上线
- 🎯 每一步都有可运行的代码，跟着做就能学会

## 适合谁读

- 有基础 Python 能力的开发者（不需要 AI 背景）
- 想理解 Agent 原理但不想啃论文的工程师
- 想用 Agent 技术提升工作效率的产品经理/数据分析师
- 在校学生，想系统学习 AI Agent 技术
- **看过 2024–2025 年教程、想知道这两年到底变了什么的开发者**（直接从第 9 章开始读）

## 学习路线图

```
第一部分        第二部分        第三部分            第四部分          第五部分
 认知篇   ──→   构建篇   ──→  协议与上下文篇  ──→  框架与协作篇  ──→  评估与落地篇
理解本质      从零手写      MCP + 上下文工程     选型与多Agent      评估与综合项目
 1-3章         4-8章           9-10章             11-12章           13章及以后
```

### 第一部分：认知篇 —— 理解 Agent 的本质

| 章节 | 标题 | 核心内容 | 状态 |
|------|------|----------|------|
| 第1章 | [什么是 AI Agent](docs/01-what-is-agent/README.md) | Agent 的定义、与 RL Agent 的术语辨析、核心能力、发展历程（含 2026 更新） | ✅ |
| 第2章 | [LLM 基础入门](docs/02-llm-basics/README.md) | LLM 原理、API 调用、Prompt Engineering | ✅ |
| 第3章 | [Agent 的核心组件](docs/03-agent-components/README.md) | 大脑（LLM）、工具（Tools）、记忆（Memory）、规划（Planning） | ✅ |

### 第二部分：构建篇 —— 从零构建 AI Agent

| 章节 | 标题 | 核心内容 | 状态 |
|------|------|----------|------|
| 第4章 | [手写第一个 Agent](docs/04-first-agent/README.md) | 基础 LLM 调用 → 添加工具 → ReAct 循环 | ✅ |
| 第5章 | [让 Agent 拥有记忆](docs/05-agent-memory/README.md) | 短期记忆、长期记忆、上下文管理 | ✅ |
| 第6章 | [让 Agent 使用工具](docs/06-agent-tools/README.md) | Function Calling、自定义工具、工具链 | ✅ |
| 第7章 | [让 Agent 学会规划](docs/07-agent-planning/README.md) | Plan-and-Solve、反思机制、自我纠错 | ✅ |
| 第8章 | [Agent 行为工程](docs/08-agent-behavior-engineering/README.md) | 技能即代码、反合理化、门控系统、子代理架构 | ✅ |

### 第三部分：协议与上下文篇 —— 2026 的新基本功 🆕

| 章节 | 标题 | 核心内容 | 状态 |
|------|------|----------|------|
| 第9章 | [MCP：让工具即插即用](docs/09-mcp/README.md) | Host/Client/Server、Tools/Resources/Prompts、2026-07-28 无状态规范、MRTR | ✅ 转译整合 |
| 第10章 | [上下文工程](docs/10-context-engineering/README.md) | 注意力预算、工具结果清理、压缩、结构化记事、子代理隔离、跨窗口接力 | ✅ 转译整合 |

### 第四部分：框架与协作篇 —— 选型与落地 🆕

| 章节 | 标题 | 核心内容 | 状态 |
|------|------|----------|------|
| 第11章 | [2026 Agent 框架全景与选型](docs/11-frameworks-2026/README.md) | 主流框架对照、AutoGen 归档等生态变动、按场景选型、活跃度自检脚本 | ✅ 整合 |
| 第12章 | [多 Agent 协作与 A2A 协议](docs/12-multi-agent-a2a/README.md) | 四种协作模式、Agent Card、Task 生命周期、三种协议绑定、A2UI/AG-UI | ✅ 转译整合 |

### 第五部分：评估与落地篇 —— 上线前后的功课

| 章节 | 标题 | 核心内容 | 状态 |
|------|------|----------|------|
| 第13章 | [Agent 评估与可观测性](docs/13-agent-evals/README.md) | pass@k vs pass^k、轨迹硬约束、LLM 裁判、评测仪器误差、OTel GenAI | ✅ 整合 |
| 第14章 | [LangGraph 实战](docs/14-langgraph/README.md) | 图结构、状态管理、持久化、人机协作中断 | ⏳ 计划中 |
| 第15章 | [Dify 与低代码平台](docs/15-dify/README.md) | 低代码 Agent、工作流编排、与代码优先方案的取舍 | ⏳ 计划中 |
| 第16章 | [RAG 知识库 Agent](docs/16-rag-agent/README.md) | 文档解析、向量检索、知识问答 | ⏳ 计划中 |
| 毕业项目 | [智能研究助手](docs/17-capstone/README.md) | 综合运用所有技术，构建完整 Agent 应用 | ⏳ 计划中 |

> ✅ = 已完成 | 🚧 = 编写中 | ⏳ = 计划中（尚未创建文件，链接暂不可用）
>
> **诚实说明**：标 ⏳ 的章节目前只有规划，没有内容。本次更新没有为了"看起来完整"而放占位文件。

## 每章包含什么

每一章都遵循统一的教学结构：

- **概念讲解**：用通俗的语言解释核心概念，配合图解，不堆砌术语
- **完整代码**：每一步都有可运行的 Python 代码，附详细中文注释
- **运行演示**：展示代码的运行过程和预期输出
- **动手练习**：每章末尾有分难度的练习题
- **踩坑记录**：记录常见错误和排查方法
- **来源声明**（转译章节）：章首标注一手来源与用途

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/2182977liu-bit/awesome-ai-agent-learning.git
cd awesome-ai-agent-learning

# 2. 安装依赖（Python 3.11+，MCP SDK 要求）
pip install -r requirements.txt

# 3. 配置 API Key（全项目统一这三个变量，支持任何 OpenAI 兼容接口）
export API_KEY="your-api-key"
export BASE_URL="https://api.openai.com/v1"
export MODEL="gpt-4o-mini"

# 4. 开始学习！新手从第1章开始；有基础的可以直接跳到第9章看 2026 的新东西
```

**文档之外，还有一份能直接运行的代码。** [`code/`](code/README.md) 目录收录了 41 个示例脚本，由工具从各章 Markdown 中抽取生成，CI 保证两者永远一致：

```bash
# 不需要密钥就能跑的两个例子
python code/ch13_evals/pass_metrics.py      # 体会 pass@k 与 pass^k 的差距
python code/ch11_frameworks/check_repos.py  # 核查框架活跃度（需联网）

# 改完文档后的自检（无需安装任何依赖）
python tools/check_repo.py
```

## 2026 年，这几件事你必须知道

如果你上一次学 Agent 是在 2024–2025 年，下面五条会直接推翻旧认知。详细展开见对应章节。

| 变化 | 说明 | 详见 |
|------|------|------|
| **MCP 成了公共底座** | 2025-12 由 Anthropic 捐给 Linux Foundation 旗下 AAIF；2026-07-28 规范改为**无状态内核**，是诞生以来最大改版 | [第9章](docs/09-mcp/README.md) |
| **上下文工程取代提示词工程** | 更大的窗口解决不了注意力摊薄；清理、压缩、记事、隔离才是解法 | [第10章](docs/10-context-engineering/README.md) |
| **AutoGen 已归档** | 微软把 AutoGen 与 Semantic Kernel 合并为 Microsoft Agent Framework；新项目不要再选 AutoGen | [第11章](docs/11-frameworks-2026/README.md) |
| **A2A 让 Agent 互相协作** | 一周年时支持组织超 150 家；2026-08 加入 AAIF，与 MCP 成兄弟项目 | [第12章](docs/12-multi-agent-a2a/README.md) |
| **稳定性比能力上限更重要** | τ-bench 上平均成功率 >60% 的 Agent，pass^8 跌到 25% 以下 | [第13章](docs/13-agent-evals/README.md) |

## 推荐学习资源

以下资源均于 **2026-11-23** 通过 GitHub API 核实过状态（Star / 归档 / 最近推送）。

### 系统教程

| 项目 | 说明 | Star | 最近推送 | 链接 |
|------|------|------|---------|------|
| Datawhale Hello-Agents | 最系统的中文 Agent 教程 | 87.6k | 2026-11-13 | [GitHub](https://github.com/datawhalechina/hello-agents) |
| Microsoft AI Agents for Beginners | 微软官方 Agent 入门课程 | 80.8k | 2026-11-17 | [GitHub](https://github.com/microsoft/ai-agents-for-beginners) |
| GenAI Agents | 大量 Agent 实现合集 | 25.1k | 2026-11-02 | [GitHub](https://github.com/NirDiamant/GenAI_Agents) |
| AI Agents From Scratch | 从零构建 Agent，无框架依赖 | 4.9k | 2026-07-24 | [GitHub](https://github.com/pguso/ai-agents-from-scratch) |

### 协议与标准（2026 新增，优先读）

| 项目 | 说明 | Star | 最近推送 | 链接 |
|------|------|------|---------|------|
| MCP 规范 | 工具连接标准，2026-07-28 版 | 9.8k | 2026-11-22 | [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol) |
| MCP Python SDK | 官方 Python 实现（v2 API） | 24.9k | 2026-11-17 | [GitHub](https://github.com/modelcontextprotocol/python-sdk) |
| MCP Servers | 官方与社区 Server 合集 | 92.2k | 2026-11-19 | [GitHub](https://github.com/modelcontextprotocol/servers) |
| A2A 协议 | Agent 间互操作标准 | 26.6k | 2026-11-20 | [GitHub](https://github.com/a2aproject/A2A) |
| Agent Skills 规范 | 可复用 Agent 专长的开放格式 | 27.5k | 2026-11-04 | [GitHub](https://github.com/agentskills/agentskills) |
| AGENTS.md | 引导编码 Agent 的开放格式 | 25.7k | 2026-09-10 | [GitHub](https://github.com/agentsmd/agents.md) |
| Agentic AI Foundation | MCP / A2A / Agent Skills 的中立治理之家 | — | — | [官网](https://aaif.io/) |

### 框架

| 项目 | 说明 | Star | 最近推送 | 链接 |
|------|------|------|---------|------|
| LangGraph | 图编排 + 持久化，复杂有状态流程首选 | 45.3k | 2026-11-22 | [GitHub](https://github.com/langchain-ai/langgraph) |
| LangChain | 集成目录最广的 LLM 应用框架 | 150.0k | 2026-11-22 | [GitHub](https://github.com/langchain-ai/langchain) |
| Deep Agents | 长任务 harness，内置上下文管理 | 31.5k | 2026-11-22 | [GitHub](https://github.com/langchain-ai/deepagents) |
| OpenAI Agents SDK | 轻量原语 + handoffs + guardrails | 30.8k | 2026-11-23 | [GitHub](https://github.com/openai/openai-agents-python) |
| Claude Agent SDK | Claude Code 同款 agent loop | 8.6k | 2026-11-20 | [GitHub](https://github.com/anthropics/claude-agent-sdk-python) |
| CrewAI | 角色化多 Agent，原型最快 | 61.2k | 2026-11-21 | [GitHub](https://github.com/crewAIInc/crewAI) |
| Google ADK | 多语言、多模态、A2A 支持最深 | 22.3k | 2026-11-21 | [GitHub](https://github.com/google/adk-python) |
| Microsoft Agent Framework | AutoGen + Semantic Kernel 的官方继任者 | — | — | [官方文档](https://learn.microsoft.com/agent-framework/) · [Go 版](https://github.com/microsoft/agent-framework-go) |
| Pydantic AI | 类型安全 Python Agent | 21.3k | 2026-11-23 | [GitHub](https://github.com/pydantic/pydantic-ai) |
| smolagents | 极简 code-agent，适合读源码学习 | 30.5k | 2026-11-20 | [GitHub](https://github.com/huggingface/smolagents) |
| Mastra | TypeScript 全栈 Agent 框架 | 29.7k | 2026-11-23 | [GitHub](https://github.com/mastra-ai/mastra) |
| Dify | 开源 LLM 应用开发平台 | 161.7k | 2026-11-23 | [GitHub](https://github.com/langgenius/dify) |
| ⚠️ Microsoft AutoGen | **已归档（只读）**，新项目请改用 Microsoft Agent Framework | 62.0k | 2026-11-12 | [GitHub](https://github.com/microsoft/autogen) |
| MetaGPT | 多 Agent 元编程框架（更新已放缓） | 71.4k | 2026-01-21 | [GitHub](https://github.com/FoundationAgents/MetaGPT) |
| Langchain-Chatchat | 中文知识库问答（近一年未更新，谨慎选用） | 38.7k | 2025-11-10 | [GitHub](https://github.com/chatchat-space/Langchain-Chatchat) |

### 记忆、评估与可观测性（2026 新增）

| 项目 | 说明 | Star | 最近推送 | 链接 |
|------|------|------|---------|------|
| Mem0 | Agent 记忆层 | 69.4k | 2026-11-18 | [GitHub](https://github.com/mem0ai/mem0) |
| Letta | 有状态 Agent 服务 | 25.5k | 2026-10-18 | [GitHub](https://github.com/letta-ai/letta) |
| DeepEval | LLM / Agent 评测框架 | 19.6k | 2026-11-23 | [GitHub](https://github.com/confident-ai/deepeval) |
| Arize Phoenix | 追踪与评估 | 12.4k | 2026-11-22 | [GitHub](https://github.com/Arize-ai/phoenix) |
| OpenLLMetry | 基于 OpenTelemetry 的 LLM 埋点 | 7.5k | 2026-11-22 | [GitHub](https://github.com/traceloop/openllmetry) |
| τ²-bench | 多轮带政策约束的 Agent 基准 | 2.5k | 2026-11-21 | [GitHub](https://github.com/sierra-research/tau2-bench) |

**收录标准**：本表只收**公开可验证、对学习者有直接帮助**的教学项目或开源代码库——能读到源码、能复现、不是纯导流页。第三方 Skill/工具市场、需付费才能看到内容的平台、以推广为目的的投稿不在收录范围。如果你觉得有项目符合以上标准，欢迎提交 PR 说明它解决什么问题、怎么复现。

**状态标注约定**：Star 是历史累积，`archived` 和最近推送日期才反映当下状态。本表如实标注归档与停更项目，不做隐去。你可以用[第11章的脚本](docs/11-frameworks-2026/README.md)自己复查。

## 常见问题

**需要什么基础？**

只需要 Python 基础就够了。如果你能写简单的 Python 函数、理解列表和字典，就可以开始学习。不需要任何 AI 或机器学习背景。注意第 9 章的 MCP SDK 要求 **Python 3.11+**。

**需要付费 API 吗？**

不需要。教程支持多种 LLM 服务商，你可以使用 DeepSeek、通义千问等提供的免费额度来完成练习。有 OpenAI 的 API Key 也可以直接用。

**我看过 2024–2025 年的 Agent 教程，还需要从头读吗？**

不用。第 1–8 章是原理与手写实现，这部分知识没有过时。你可以直接从**第 9 章**开始，补上 MCP、上下文工程、框架选型、A2A 和评估这五块 2026 的新内容。

**代码能在本地运行吗？**

分两层说，不含糊：

- **有机制保障的部分**：CI 对全部 76 个文档代码块和 `code/` 下 41 个脚本做语法编译检查，并校验文档与代码同步、内部链接有效、配置约定统一。每次 push 和 PR 都会跑。
- **没有机制保障的部分**：CI **不会**真的调用 LLM API 或启动服务去执行这些脚本（那需要密钥和外部服务）。所以"在你的环境上一次跑通"仍需自己验证。

遇到跑不通的情况请提 Issue，附上章节、报错和你的环境 —— 我们不会把"未验证"说成"已验证"。配置约定见 [code/README.md](code/README.md)。

**为什么有的章节标 ⏳ 却点不开？**

因为那些章节确实还没写。我们宁可留空白，也不放占位文件充数。

**这里的"Agent"和"规划"跟强化学习里的是同一个意思吗？**

不是。RL 里的 agent 指 MDP 中与环境交互的抽象决策主体，planning 指在已知环境模型下搜索最优动作序列；本教程的 AI Agent 是"LLM 作为决策核心"的实现，规划指任务分解与步骤生成，没有显式环境模型、也不保证最优。完整辨析和术语对照表见[第1章 1.2 / 1.4 节](docs/01-what-is-agent/README.md)。

**转译的内容会不会失真？**

每章章首都列了一手来源，[SOURCES.md](SOURCES.md) 逐篇记录了来源、改动和原创部分。协议字段名、枚举值、版本号一律核对官方规范；二手来源与官方冲突时以官方为准，并在正文写明冲突（例如 A2A 版本号那处）。厂商观点会明确标注，不当作行业标准。

**如何参与贡献？**

欢迎提交 Issue 报告问题或建议，也欢迎直接提 PR。详见下方[贡献指南](#贡献指南)。

## 贡献指南

**完整的贡献规范见 [CONTRIBUTING.md](CONTRIBUTING.md)**，里面写清了本地自检、配置约定、代码同步机制和转译登记要求。最常用的几种方式：

- **提交 Issue**：发现错误、有改进建议、或想请求新内容（已有错误报告和资源推荐两套模板）
- **提交 PR**：修复 Bug、优化代码、补充内容、翻译文档
- **编写新章节**：先开 Issue 讨论大纲，确认后开始编写
- **补充踩坑记录与评测集**：这是对本项目最有价值的贡献之一
- **转译投稿**：请一并提交来源链接与许可说明，并在 [SOURCES.md](SOURCES.md) 登记

提交前跑一下自检，能省去大部分来回：

```bash
python tools/check_repo.py
```

## 更新日志

| 日期 | 内容 |
|------|------|
| 2026-11-23 | **工程化**：新增 `code/`（41 个可运行脚本，由文档自动生成）、CI 自检 workflow、`tools/` 检查脚本、`CONTRIBUTING.md`、Issue/PR 模板；修复第8–13章环境变量三套写法导致的运行失败，全仓库统一为 `API_KEY`/`BASE_URL`/`MODEL` |
| 2026-11-23 | 新增第 9–12 章与评估章（MCP / 上下文工程 / 框架全景 / A2A / 评估）；更新第1章发展历程至 2026；重排路线图并修复全部断链；按 GitHub API 实测更新资源表（标注 AutoGen 归档、移除失效链接）；新增 SOURCES.md 与 requirements.txt |
| 2025 及更早 | 第 8 章 Agent 行为工程；Agent 与 RL 的术语辨析、资源收录标准；重写为原创中文教程 |

## 致谢

感谢开源社区和所有优秀的教学项目。特别感谢 Datawhale、Microsoft、LangChain 社区在 AI 教育领域的持续投入，以及 Anthropic、Google、Linux Foundation / AAIF 在开放协议上的工作 —— 本次更新中第 9–13 章的事实依据大量来自他们公开的规范与工程博客，具体出处见 [SOURCES.md](SOURCES.md)。也感谢每一位阅读、提建议、提交贡献的你。

## 许可证

本项目基于 [MIT License](LICENSE) 开源，你可以自由使用、修改和分发。转译与整合部分的来源署名见 [SOURCES.md](SOURCES.md)。

## 关于作者

**青松与桑叶** —— 一个热爱 AI 技术的开发者，相信最好的学习方式是动手实践。写这个教程的初衷很简单：希望让每一个想学 Agent 的人都能找到一条清晰、可操作的学习路径。如果你在学习过程中有任何问题，欢迎通过 GitHub Issue 与我交流。