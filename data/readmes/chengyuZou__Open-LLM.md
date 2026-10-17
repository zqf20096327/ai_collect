# 🌌 LLM 学习指南与资源导航 (LLM Learning & Resources)

一个持续更新的 LLM / Agent / RAG / 多模态 学习与开源项目导航仓库。  
目标不是“堆链接”，而是尽量帮助你快速回答这些问题：

- 我该先学什么？
- 当前主流的开源 Agent / RAG 框架有哪些？
- 哪些项目适合拿来复现、读源码、做 Demo、做二开？
- 哪些网站 / 平台适合持续跟进这个领域？

如果这个仓库对你有帮助，欢迎点个 **Star ⭐️**！

---

## 🔍 说明

- **排名不分先后**：资源主要按方向整理，而不是按优劣排名。
- **偏工程与实战**：优先收录能真正上手、能看源码、能做项目的资源。
- **持续更新**：会逐步加入更好的教程、框架、评测集与项目模板。
- **免责声明**：内容来源于互联网公开资源，如有侵权请联系删除。

---

## 📚 目录 (Table of Contents)

- [1. 🛣️ 学习路线总览](#1-️-学习路线总览)
- [2. 🧠 基础与理论 (Foundations)](#2--基础与理论-foundations)
  - [数学、机器学习、深度学习](#数学机器学习深度学习)
  - [LLM 理论与综述](#llm-理论与综述)
- [3. ⚔️ 核心实战与复现 (Core Implementation)](#3-️-核心实战与复现-core-implementation)
  - [从零手写 / 复现 LLM](#从零手写--复现-llm)
  - [模型微调 (Fine-tuning)](#模型微调-fine-tuning)
  - [开发者教程与手册](#开发者教程与手册)
- [4. 🏗️ 应用开发架构 (Application Engineering)](#4-️-应用开发架构-application-engineering)
  - [Agent 框架](#agent-框架)
  - [RAG / Agentic RAG](#rag--agentic-rag)
  - [Memory / 长短期记忆](#memory--长短期记忆)
  - [Code Agent / 软件工程智能体](#code-agent--软件工程智能体)
  - [工作流 / 可视化应用平台](#工作流--可视化应用平台)
- [5. 📏 评测、观测与对齐](#5--评测观测与对齐)
  - [RAG 评测](#rag-评测)
  - [Agent / LLM 评测](#agent--llm-评测)
  - [Tracing / Observability](#tracing--observability)
- [6. 🧩 多模态与垂直领域](#6--多模态与垂直领域)
- [7. 🛠️ 工具链与生态 (Tools & Ecosystem)](#7-️-工具链与生态-tools--ecosystem)
  - [核心框架与官网](#核心框架与官网)
  - [MCP 与工具调用生态](#mcp-与工具调用生态)
  - [IDE 与开发工具](#ide-与开发工具)
  - [算力与炼丹平台](#算力与炼丹平台)
  - [API 服务与聚合](#api-服务与聚合)
- [8. 🌐 社区、资讯与资源聚合](#8--社区资讯与资源聚合)
  - [Awesome / 导航仓库](#awesome--导航仓库)
  - [博主 / 博客 / 资讯](#博主--博客--资讯)
- [9. 🎮 DLC](#9--dlc)
  - [算法](#算法)
  - [Others](#others)

---

# 1. 🛣️ 学习路线总览

给新手或转方向同学一个简洁路线参考：

## 路线 A：想系统学习 LLM 原理
1. 数学 / 机器学习 / 深度学习基础
2. NLP 基础（词向量、RNN/LSTM、Attention、Transformer）
3. LLM 预训练、SFT、RLHF / DPO
4. 从零手写 mini-LLM / 复现训练流程
5. 模型微调、推理部署、评测

## 路线 B：想做 LLM 应用开发
1. Prompt、Function Calling、Tool Use
2. RAG 基础：切分、索引、召回、重排、生成
3. Agent 框架：LangGraph / AutoGen / CrewAI / LlamaIndex
4. 记忆系统、工作流编排、日志追踪、评测
5. 生产化部署：鉴权、监控、成本控制、缓存、数据治理

## 路线 C：想做 Agent / Research
1. ReAct / Tool Use / Planning / Reflection
2. Multi-Agent 协作
3. Agent Memory / Persona / World Model
4. Agentic RAG / Long-horizon tasks
5. Benchmark、Reward、RL / Preference Optimization

---

# 2. 🧠 基础与理论 (Foundations)

## 数学、机器学习、深度学习

| 资源名称 | 作者/组织 | 链接 | 备注 |
|---------|----------|------|------|
| ML-For-Beginners | Microsoft | [GitHub](https://github.com/microsoft/ML-For-Beginners) | 机器学习入门 |
| 动手学深度学习 2.0 | 李沐等 | [在线阅读](https://zh.d2l.ai/) | 深度学习经典教材 |
| machine_learning_notebook | 583 | [GitHub](https://github.com/583/machine_learning_notebook) | 机器学习笔记 |
| CS224n-Reading-Notes | LooperXX | [GitHub](https://github.com/LooperXX/CS224n-Reading-Notes) | Stanford CS224n 笔记 |
| Book-Mathematical-Foundation-of-RL | MathFoundationRL | [GitHub](https://github.com/MathFoundationRL/Book-Mathematical-Foundation-of-Reinforcement-Learning) | 强化学习数学基础 |
| stanford-cs336-a1 | Spectual | [GitHub](https://github.com/Spectual/stanford-cs336-a1) | CS336 作业 |

## LLM 理论与综述

| 资源名称 | 作者/组织 | 链接 | 备注 |
|---------|----------|------|------|
| Foundations-of-LLMs | ZJU-LLMs | [GitHub](https://github.com/ZJU-LLMs/Foundations-of-LLMs) | 大模型基础电子书 |
| Foundations of LLMs | 肖桐老师等 | [Arxiv](https://arxiv.org/abs/2501.09223) | LLM 基础综述 |
| so-large-lm | Datawhale | [GitHub](https://github.com/datawhalechina/so-large-lm) | 大模型知识梳理 |
| Awesome-LLM | Hannibal046 | [GitHub](https://github.com/Hannibal046/Awesome-LLM) | LLM 论文/框架/课程大合集 |
| awesome-llm-pretraining | RUCAIBox | [GitHub](https://github.com/RUCAIBox/awesome-llm-pretraining) | 预训练资源整理 |
| Agentic Design Patterns | ginobefun | [GitHub](https://github.com/ginobefun/agentic-design-patterns-cn) | Agent 设计模式中文翻译 |

---

# 3. ⚔️ 核心实战与复现 (Core Implementation)

## 从零手写 / 复现 LLM

| 资源名称 | 作者/组织 | 链接 | 备注 |
|---------|----------|------|------|
| MiniMind | jingyaogong | [GitHub](https://github.com/jingyaogong/minimind) | 大模型全阶段复现，极适合入门 |
| MiniMind-in-Depth | hans0809 | [GitHub](https://github.com/hans0809/MiniMind-in-Depth) | MiniMind 深入解析 |
| transformers-code | zyds | [GitHub](https://github.com/zyds/transformers-code) | Transformers 代码实践 |
| Hands-On-Large-Language-Models-CN | bbruceyuan | [GitHub](https://github.com/bbruceyuan/Hands-On-Large-Language-Models-CN) | 《动手学习大模型》中文版 |
| llm-course | mlabonne | [GitHub](https://github.com/mlabonne/llm-course) | 系统性 LLM 学习课程 |

## 模型微调 (Fine-tuning)

| 资源名称 | 作者/组织 | 链接 | 备注 |
|---------|----------|------|------|
| LLaMA-Factory | hiyouga | [GitHub](https://github.com/hiyouga/LLaMA-Factory) | 微调 / 推理 / WebUI，一站式 |
| self-llm | Datawhale | [GitHub](https://github.com/datawhalechina/self-llm) | 开源大模型食用指南 |
| Awesome-Chinese-LLM | HqWu-HITCS | [GitHub](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM) | 中文模型/微调/数据集整理 |

## 开发者教程与手册

| 资源名称 | 作者/组织 | 链接 | 备注 |
|---------|----------|------|------|
| llm-universe | Datawhale | [GitHub](https://github.com/datawhalechina/llm-universe) | 面向小白的 LLM 应用开发教程 |
| llm-cookbook | Datawhale | [GitHub](https://github.com/datawhalechina/llm-cookbook) | 面向开发者的大模型手册 |
| tiny-universe | Datawhale | [GitHub](https://github.com/datawhalechina/tiny-universe) | 大模型白盒构建指南 |
| happy-llm | Datawhale | [GitHub](https://github.com/datawhalechina/happy-llm) | 从零开始的原理与实践 |
| ModelScope Classroom | ModelScope | [GitHub](https://github.com/modelscope/modelscope-classroom) | 魔搭教程 |

---

# 4. 🏗️ 应用开发架构 (Application Engineering)

## Agent 框架

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| LangGraph | LangChain | [GitHub](https://github.com/langchain-ai/langgraph) | 适合构建有状态、长流程 Agent |
| AutoGen | Microsoft | [GitHub](https://github.com/microsoft/autogen) | 经典多智能体框架 |
| CrewAI | CrewAI | [GitHub](https://github.com/crewAIInc/crewAI) | 多 Agent 协作框架 |
| LlamaIndex | run-llama | [GitHub](https://github.com/run-llama/llama_index) | 数据 + Agent + RAG 生态非常完整 |
| Haystack | deepset | [GitHub](https://github.com/deepset-ai/haystack) | 生产级 AI 编排框架 |
| DSPy | Stanford NLP | [GitHub](https://github.com/stanfordnlp/dspy) | 强调“编程而不是调 Prompt” |

## RAG / Agentic RAG

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| RAGFlow | InfiniFlow | [GitHub](https://github.com/infiniflow/ragflow) | 近两年非常火的开源 RAG 引擎 |
| LlamaIndex | run-llama | [GitHub](https://github.com/run-llama/llama_index) | 文档索引 / 检索 / Query Engine |
| Haystack | deepset | [GitHub](https://github.com/deepset-ai/haystack) | 模块化 Pipeline + RAG + Agent |
| rag_techniques | NirDiamant | [GitHub](https://github.com/NirDiamant/rag_techniques) | 高质量 RAG 技术笔记和示例 |
| RAGHub | Andrew-Jang | [GitHub](https://github.com/Andrew-Jang/RAGHub) | RAG 工具与项目目录 |
| RAG-Anything | HKUDS | [GitHub](https://github.com/HKUDS/RAG-Anything) | 多模态 RAG 方向 |

## Memory / 长短期记忆

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| Mem0 | mem0ai | [GitHub](https://github.com/mem0ai/mem0) | 当前很有代表性的 Agent Memory 层 |
| awesome-lifelong-llm-agent | qianlima-lab | [GitHub](https://github.com/qianlima-lab/awesome-lifelong-llm-agent) | 终身学习 / Memory / Continual Agent 综述整理 |
| mem0-mcp | mem0ai | [GitHub](https://github.com/mem0ai/mem0-mcp) | Memory + MCP 结合示例 |

## Code Agent / 软件工程智能体

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| OpenHands | All-Hands-AI | [GitHub](https://github.com/OpenHands/OpenHands) | 代码智能体热门项目，前身 OpenDevin |
| MetaGPT | FoundationAgents | [GitHub](https://github.com/FoundationAgents/MetaGPT) | 软件公司流程化多智能体 |
| OpenManus | FoundationAgents | [GitHub](https://github.com/FoundationAgents/OpenManus) | 开源版 Manus 路线 |
| DM-Code-Agent | hwfengcs | [GitHub](https://github.com/hwfengcs/DM-Code-Agent) | 面向软件开发的 Code Agent |

## 工作流 / 可视化应用平台

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| Dify | LangGenius | [GitHub](https://github.com/langgenius/dify) | 应用平台非常成熟，适合快速搭建产品 |
| FastGPT | labring | [GitHub](https://github.com/labring/FastGPT) | 国内常见的知识库 / Flow / Agent 平台 |
| Coze | ByteDance | [文档](https://www.coze.com/open/docs/zh_cn/) | 低代码 Agent 平台 |
| Langchain-Chatchat | chatchat-space | [GitHub](https://github.com/chatchat-space/Langchain-Chatchat) | 本地知识库 / RAG / Agent |
| NagaAgent | xxiii8322766509 | [GitHub](https://github.com/Xxiii8322766509/NagaAgent) | 智能对话助手系统 |

---

# 5. 📏 评测、观测与对齐

## RAG 评测

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| RAGAS | explodinggradients | [GitHub](https://github.com/explodinggradients/ragas) | RAG 评测标准工具 |
| DeepEval | confident-ai | [GitHub](https://github.com/confident-ai/deepeval) | LLM / RAG / Agent 评测工具 |
| promptfoo | promptfoo | [GitHub](https://github.com/promptfoo/promptfoo) | Prompt / RAG / 安全评测 |

## Agent / LLM 评测

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| OpenAI Evals | OpenAI | [GitHub](https://github.com/openai/evals) | 经典评测框架 |
| lm-evaluation-harness | EleutherAI | [GitHub](https://github.com/EleutherAI/lm-evaluation-harness) | 语言模型基准评测 |
| awesome-llm-apps | Shubhamsaboo | [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps) | 大量 Agent / RAG / 应用案例可做“横向参考” |

## Tracing / Observability

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| LangSmith | LangChain | [官网](https://www.langchain.com/langsmith) | LangChain / LangGraph 生态常用 |
| Phoenix | Arize AI | [GitHub](https://github.com/Arize-ai/phoenix) | LLM tracing / evaluation |
| Weave | Weights & Biases | [官网](https://wandb.ai/site/weave/) | LLM 应用追踪与分析 |

---

# 6. 🧩 多模态与垂直领域

## 多模态 (CV / Audio / OCR)

| 资源名称 | 作者/组织 | 链接 | 备注 |
|---------|----------|------|------|
| GPT-SoVITS | RVC-Boss | [GitHub](https://github.com/RVC-Boss/GPT-SoVITS) | 语音克隆 / TTS |
| DeepSeek-OCR | DeepSeek | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) | OCR 模型 |
| awesome-pretrained-chinese | lonePatient | [GitHub](https://github.com/lonePatient/awesome-pretrained-chinese-nlp-models) | 中文预训练/多模态模型集合 |

## 垂直行业模型

| 资源名称 | 领域 | 链接 | 备注 |
|---------|------|------|------|
| DISC-LawLLM | 法律 | [GitHub](https://github.com/FudanDISC/DISC-LawLLM) | 法律领域模型 |
| DoctorGLM | 医疗 | [GitHub](https://github.com/xionghonglin/DoctorGLM) | 医疗问诊方向 |

---

# 7. 🛠️ 工具链与生态 (Tools & Ecosystem)

## 核心框架与官网

| 名称 | 类别 | 链接 |
|------|------|------|
| PyTorch | 深度学习框架 | [官网](https://pytorch.org) |
| TensorFlow | 深度学习框架 | [官网](https://www.tensorflow.org) |
| Hugging Face | 模型 / 数据 / Space | [官网](https://huggingface.co) |
| ModelScope | 国内模型社区 | [官网](https://modelscope.cn) |
| LangChain | LLM 应用框架 | [官网](https://www.langchain.com) |
| OpenAI | 模型与 API | [官网](https://openai.com) |
| Anthropic | 模型厂商 | [官网](https://www.anthropic.com) |
| Google AI / Gemini | 模型厂商 | [官网](https://ai.google.dev) |

## MCP 与工具调用生态

| 名称 | 链接 | 备注 |
|------|------|------|
| Model Context Protocol | [GitHub](https://github.com/modelcontextprotocol) | MCP 官方组织 |
| MCP Servers | [GitHub](https://github.com/modelcontextprotocol/servers) | 官方服务器示例集合 |
| MCP TypeScript SDK | [GitHub](https://github.com/modelcontextprotocol/typescript-sdk) | TS SDK |
| MCP Python SDK | [GitHub](https://github.com/modelcontextprotocol/python-sdk) | Python SDK |

## IDE 与开发工具

| 名称 | 厂商/作者 | 链接 | 备注 |
|------|----------|------|------|
| Cursor | Cursor | [官网](https://cursor.com) | AI IDE |
| Windsurf | Codeium | [官网](https://windsurf.com) | AI IDE |
| 通义灵码 | 阿里云 | [官网](https://lingma.aliyun.com/lingma/) | 智能开发工具 |
| Trae | 字节 | [官网](https://www.trae.ai/) | AI IDE / 编辑器 |
| AntiGravity | Google | [官网](https://antigravity.google/) | Agent 编程 IDE 方向产品 |

## 算力与炼丹平台

| 平台名称 | 链接 | 备注 |
|---------|------|------|
| AutoDL | [官网](https://www.autodl.com/home) | 国内常用算力平台 |
| OpenBayes | [官网](https://openbayes.com) | 云端训练平台 |
| 阿里云百炼 | [官网](https://www.aliyun.com/) | 大模型服务平台 |
| ModelScope Notebook | [官网](https://modelscope.cn) | 社区与实验环境 |

## API 服务与聚合

| 平台名称 | 链接 | 备注 |
|---------|------|------|
| OpenAI Platform | [官网](https://platform.openai.com/) | OpenAI API |
| Anthropic Console | [官网](https://console.anthropic.com/) | Anthropic API |
| DeepSeek 开放平台 | [官网](https://platform.deepseek.com/) | DeepSeek API |
| 阿里云 Model Studio | [官网](https://help.aliyun.com/zh/model-studio/) | 阿里 API |
| OpenRouter | [官网](https://openrouter.ai/) | 多模型聚合 |
| 硅基流动 SiliconFlow | [官网](https://siliconflow.cn/) | 国内常见聚合服务 |

---

# 8. 🌐 社区、资讯与资源聚合

## Awesome / 导航仓库

| 项目 | 作者/组织 | 链接 | 备注 |
|------|-----------|------|------|
| Awesome-LLM | Hannibal046 | [GitHub](https://github.com/Hannibal046/Awesome-LLM) | LLM 总导航 |
| awesome-llm-agents | kaushikb11 | [GitHub](https://github.com/kaushikb11/awesome-llm-agents) | Agent 框架整理 |
| awesome-ai-agents | ARUNAGIRINATHAN-K | [GitHub](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents) | 2026 向 Agent 资源集合 |
| awesome-llm-apps | Shubhamsaboo | [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps) | 各类 LLM App 项目合集 |
| AI-Resources-Central | CoderSJX | [GitHub](https://github.com/CoderSJX/AI-Resources-Central) | AI 开源资源总表 |

## 博主 / 博客 / 资讯

### 博主

| 平台 | 博主 | 链接 | 备注 |
|------|------|------|------|
| B站 | 东川路第一可爱猫猫虫 | [空间](https://space.bilibili.com/675505667) | - |
| B站 | happy魇 | [空间](https://space.bilibili.com/478929155) | - |
| B站 | 偷星九月333 | [空间](https://space.bilibili.com/349950942) | - |
| B站 | 堂吉诃德拉曼查的英豪 | [空间](https://space.bilibili.com/341376543) | - |
| B站 | chaofa用代码打点酱油 | [空间](https://space.bilibili.com/12420432) | - |
| CSDN | v_JULY_v | [博客](https://blog.csdn.net/v_JULY_v?type=blog) | 算法/NLP 老牌作者 |
| 知乎 | 锦恢 | [主页](https://www.zhihu.com/people/can-meng-zhong-de-che-xian) | Agent/RAG 入门文较多 |

### 博客 / 文章

| 文章标题/主题 | 作者 | 链接 | 备注 |
|--------------|------|------|------|
| Agent 基本概念与分类 | 锦恢 | [知乎](https://zhuanlan.zhihu.com/p/1962274523752691074) | Agent 小白教程 |
| 深度解析 LightRAG | 老顾聊技术 | [知乎](https://zhuanlan.zhihu.com/p/4821793882) | RAG 技术解析 |
| 互联网优质资源分享 | 零一猴子 | [知乎](https://www.zhihu.com/question/3946118527/answer/1919046825337398459) | 资源汇总 |

---

# 9. 🎮 DLC

## 算法

| 名称 | 类别 | 链接 | 备注 |
|---------|------|------|------|
| LeetCode (灵茶山艾府) | 算法博主 | [主页](https://leetcode.cn/u/endlesscheng/) | - |
| Hello算法 | 书籍 | [网站](https://www.hello-algo.com/) | 动画图解算法 |
| Deep-ML | 练习平台 | [网站](https://www.deep-ml.com/) | AI 向刷题平台 |
| codeforces-go | 代码库 | [GitHub](https://github.com/EndlessCheng/codeforces-go/tree/master) | - |
| LC-Rating工具 | 工具 | [网站](https://huxulm.github.io/lc-rating/zen) | 力扣周赛工具 |

## Others

| 名称 | 类别 | 链接 | 备注 |
|---------|------|------|------|
| build-your-own-x | 项目合集 | [GitHub](https://github.com/codecrafters-io/build-your-own-x) | 手搓各种技术轮子 |
| Learn-by-projects | 项目合集 | [GitHub](https://github.com/ckissi/Learn-by-projects) | 一边做项目一边学编程 |

---

# ⭐ 更新建议

后续可以继续补充这些板块：

- **Benchmark 专题**：SWE-bench、AgentBench、GAIA、RAGBench、LongBench
- **Research 专题**：Reasoning、Memory、Persona、World Model、Tool Learning
- **中文生态专题**：Qwen、GLM、InternLM、DeepSeek 相关项目
- **部署专题**：vLLM、SGLang、TGI、Ollama、LM Studio
- **数据工程专题**：切分、清洗、去重、Embedding、Reranker、知识图谱

---

# 📌 维护原则

本仓库更偏向收录以下类型的资源：

- 仍在维护、仍有社区讨论的项目
- 有明确定位、不是“套壳拼盘”的项目
- 对学习 / 实战 / 二开真的有帮助的资源
- 尽量优先官方仓库、官方文档、原始论文

欢迎提 Issue / PR，一起把这个仓库做得更好。
