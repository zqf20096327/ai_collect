# ☄️ LLM × 搜广推 × Agentic AI 技术知识库 (Collections)

> 一线算法工程师持续维护的 **大模型（LLM）、Agentic AI 与搜广推（搜索/广告/推荐）** 全栈技术知识库、论文精读与工业界落地总结。
>
> 🌐 **在线阅读（体验更佳）**：**[https://www.daiwk.net](https://www.daiwk.net)**  
> 🤖 **AI Agent 友好**：原生支持 [`llms.txt`](https://www.daiwk.net/llms.txt) 索引及 [MCP Server](https://www.daiwk.net/~gitbook/mcp) 接入，任意页面 URL 后加 `.md` 即可获取纯 Markdown。

如果这份知识库对你的日常研发、论文跟进或面试有帮助，欢迎点一个 ⭐ **Star** 支持！

---

## 🔥 近期配套开源实战项目

除了理论与论文梳理，近期还开源了两个配套的实战工程项目：

1. **[Auto Research](https://github.com/daiwk/auto-research)**（[在线站点](https://daiwk.github.io/auto-research/)）：**410+ 篇前沿论文（搜广推 / LLM / 后训练 / Agent / 多模态）的可执行代码复现、公开数据实验审计看板与四层精读问答库**。
2. **[Building Agents from Scratch](https://github.com/daiwk/building-agents-from-scratch)**（[在线站点](https://daiwk.github.io/building-agents-from-scratch/)）：从 0 到 1 手写实现 AI Agent 的核心机制。

---

## 🌟 核心必读章节推荐（建议先看这三篇）

* 📌 **[大模型 + 搜广推工业界落地总结 (`3.llm_rec_summary`)](https://www.daiwk.net/3.llm_rec_summary)**  
  脱离过度包装的概念，从工业界一线视角剖析生成式推荐（OneRec / HSTU / TIGER Semantic ID / MTGR / PinFM）与传统 ID 特征模型的真实博弈；总结将 LLM 结构、训练/推理范式（Pretrain+SFT+RL、KV Cache/PD 分离/MTP）和世界知识引入搜索、广告、推荐的靠谱路径。
* 📌 **[Agentic AI、Deep Research 与 Harness Engineering (`5.llm_agentic`)](https://www.daiwk.net/5.llm_agentic)**  
  涵盖 Agent 记忆/工具调用/规划三大核心机制、vLLM/OpenAI Function Calling 源码级解析、MCP 与 Google A2A 协议、自我进化智能体（AlphaEvolve / DGM / SEAL），以及 **Kimi-Researcher、Tongyi-DeepResearch** 等端到端 Agentic RL 架构拆解与 **Harness / Spec Engineering** 范式演进。
* 📌 **[LLM 与强化学习核心算法数学推导笔记 (`4.llm_note`)](https://www.daiwk.net/4.llm_note)**  
  图文+公式推导：LoRA/Prefix-Tuning 细节、LogSoftmax 的 Log-Sum-Exp 数值稳定推导、**DPO 损失函数与动态系数梯度公式推导**、各大解码策略（Speculative / Lookahead / DoLa）对比，以及强化学习（MDP / 贝尔曼方程 / MC vs TD($\lambda$) / REINFORCE 推荐纠偏）与 Adam vs AdamW 本质差异。

---

## 📚 完整知识库目录

### 一、大模型（LLM）全栈技术体系
* [00. 苦涩的教训 (The Bitter Lesson)](https://www.daiwk.net/00.bitter_lesson)
* [01. AI 知识可视化与科普视频精选](https://www.daiwk.net/01.ai_videos)
* [1.1 前大模型时代 (Pre-LLM)](https://www.daiwk.net/1.1.pre_llm)
* [1.2 大模型导论与全景介绍](https://www.daiwk.net/1.2.llm_intro)
* [1.3 大模型工程架构 (Tokenizer / Attention / MoE / 训推系统)](https://www.daiwk.net/1.3.llm_archs)
* [1.4 大模型监督微调与应用 (SFT & Usages)](https://www.daiwk.net/1.4.llm_sft_and_usages)
* [1.5 大模型对齐与强化学习 (RLHF / DPO / PPO / GRPO)](https://www.daiwk.net/1.5.llm_alignment)
* [1.6 多模态大模型 (VLM & Multimodal)](https://www.daiwk.net/1.6.llm_multimodal)
* [1.8 O1 类慢思考与推理大模型 (Reasoning LLMs)](https://www.daiwk.net/1.8.llm_o1)
* [1.9 大模型其他前沿话题](https://www.daiwk.net/1.9.llm_others)
* [4. 大模型与强化学习算法推导笔记](https://www.daiwk.net/4.llm_note)
* [6. 大模型数学推理 (LLM Math)](https://www.daiwk.net/6.llm_math)

### 二、搜广推（搜索 / 广告 / 推荐）与大模型融合
* [1.7 大模型与推荐系统论文追踪 (LLM for Recommendation)](https://www.daiwk.net/1.7.llm_recommend)
* [2. 推荐系统全链路体系 (召回 / 粗排 / 精排 / 重排)](https://www.daiwk.net/2.recommend)
* [3. 大模型 + 搜广推工业界个人深度总结](https://www.daiwk.net/3.llm_rec_summary)

### 三、Agentic AI 与上下文工程
* [5. 大模型 Agentic 全景 (Memory / Tool / Planning / RAG / Agentic RL / Deep Research / Harness)](https://www.daiwk.net/5.llm_agentic)

### 四、机器学习面试与历史技术合集
* [8. 机器学习与深度学习面试汇总 (ML Interview)](https://www.daiwk.net/8.int-ml)
* [9. 早年技术文章与总结归档](https://www.daiwk.net/9.collections)

---

## 📦 配套 PDF 资料归档

站点内涉及的论文与报告 PDF 汇总网盘：  
* 百度网盘：<https://pan.baidu.com/s/11YH16592t_SRTK2zFEDrrQ?pwd=8sgt> （提取码: `8sgt`）

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=daiwk/collections&type=Date)](https://star-history.com/#daiwk/collections&Date)
