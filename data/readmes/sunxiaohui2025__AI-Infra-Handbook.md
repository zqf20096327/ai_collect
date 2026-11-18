<div align="center">

# AI Infra-HandBook

**用大模型逐讲编写的一套 AI 基础设施（LLM 推理）交互式课程**

从「为什么模型要把一切变成数字」讲到「能跑起来的迷你推理引擎」，
每讲只讲一个技术点，按依赖顺序排列——读到任何一讲，它用到的概念都已在前面讲过。

[![框架](https://img.shields.io/badge/框架-Astro%205-blue)](https://astro.build)
[![技术](https://img.shields.io/badge/技术-MDX%20·%20LaTeX-purple)](https://mdxjs.com)
[![课程规模](https://img.shields.io/badge/课程-153%20讲-brightgreen)](https://ai-infra-handbook.sunxiaohui2022.workers.dev/)
[![篇章结构](https://img.shields.io/badge/结构-6%20章%20·%2020%20篇-9cf)](https://ai-infra-handbook.sunxiaohui2022.workers.dev/)
[![交互组件](https://img.shields.io/badge/交互组件-150%20个-orange)](https://ai-infra-handbook.sunxiaohui2022.workers.dev/)
[![语言](https://img.shields.io/badge/语言-简体中文-green)](#)
[![GitHub Stars](https://img.shields.io/github/stars/sunxiaohui2025/AI-Infra-Handbook?style=social)](https://github.com/sunxiaohui2025/AI-Infra-Handbook)
[![GitHub Forks](https://img.shields.io/github/forks/sunxiaohui2025/AI-Infra-Handbook?style=social)](https://github.com/sunxiaohui2025/AI-Infra-Handbook)

> **在线阅读：** [在线阅读](https://ai-infra-handbook.sunxiaohui2022.workers.dev/) 　 | 　**下载 PDF：** [下载 PDF](https://raw.githubusercontent.com/sunxiaohui2025/AI-Infra-Handbook/main/release/AI-Infra-HandBook.pdf)

</div>

---

## 目录

- [下载与在线阅读](#下载与在线阅读)
- [这是什么](#这是什么)
- [课程结构](#课程结构)
- [案例模型](#全文用到的案例模型数字从哪来)
- [学习路线](#学习路线)
- [本地运行](#本地运行)
- [参考与致谢](#参考与致谢)
- [许可](#许可)

---

## 下载与在线阅读

- [在线阅读](https://ai-infra-handbook.sunxiaohui2022.workers.dev/)
- [下载 PDF](https://raw.githubusercontent.com/sunxiaohui2025/AI-Infra-Handbook/main/release/AI-Infra-HandBook.pdf)（单文件约 1342 页，含书封、目录与页码）

在线阅读站点提供：

- 首页 6 章横排成学习路线图，「完整路线 / Infra 快速路线」可切换，选择会记在浏览器里。
- 顶栏 `⌘K` 或 `/` 全局搜索：按讲名 / 问题 / 编号 / 小节即时过滤。
- 每篇、每讲都有自动生成的前置知识链接与上下讲导航。

---

## 这是什么

这是一套**由大模型逐讲编写**的 AI 基础设施（LLM 推理）课程，共 **6 章、20 篇、153 讲**，
用 **Astro 5 + MDX** 建成一个可交互的静态网站：公式用 LaTeX 渲染，交互做成一个个可复用组件直接嵌进文章。

一条主线贯穿全站：用 **一个玩具模型** 理解原理（手算、交互看得见每一步），
用 **真实模型** 算工程账（显存、速度、成本）。这是 infra 视角和普通科普的区别——
每讲都会落到它对显存、速度、成本的影响。

章节主线：**数学基础 → 大模型基础 → 单机推理 → 分布式推理 → 推理引擎实践 → 芯模适配和调优**。
前两章打基础，后四章是推理优化的主体。

## 课程结构

共 **6 章、20 篇、153 讲**：**136 讲主线** + **17 讲选读**（其中第 6 篇「训练全流程」整篇为轻量线），
**31 讲**被标为重点 ⭐；按「Infra 快速路线」阅读共 **127 讲**。

### 章节总览

| 章 | 篇 | 讲 | 主题 |
| --- | --- | --- | --- |
| 一 数学基础 | 1 数学基础 | 01–11 | 真正会用到的数学：向量、矩阵、softmax、浮点数、FLOPs |
| 二 大模型基础 | 2 神经网络基础 | 12–20 | 感知机、线性层、激活函数、反向传播、训练循环 |
| 二 大模型基础 | 3 从文本到向量 | 21–24 | 分词 BPE、词嵌入、预测下一个 token、自回归生成 |
| 二 大模型基础 | 4 Transformer 核心 | 25–35 | 位置编码、自注意力、多头注意力、FFN、完整前向 |
| 二 大模型基础 | 5 现代 LLM 架构 | 36–44 | RMSNorm、RoPE、GQA、MLA、MoE、架构演进对照 |
| 二 大模型基础 | 6 训练全流程（轻量线） | 45–51 | 预训练、Scaling Laws、SFT、RLHF/DPO、LoRA、评测 |
| 二 大模型基础 | 7 从零实现一个 GPT | 52–59 | g0–g7：在讲义语料上从零训练一个 GPT |
| 三 单机推理 | 8 硬件与性能基础 | 60–67 | GPU 架构、存储层级、Roofline、低精度、互联、超节点 |
| 三 单机推理 | 9 推理基础 | 68–73 | Prefill/Decode、KV Cache、TTFT/TPOT、显存账本、成本模型 |
| 三 单机推理 | 10 推理引擎与调度 | 74–82 | Continuous Batching、PagedAttention、Prefix Cache、压测 |
| 三 单机推理 | 11 算子与 Kernel | 83–89 | 算子融合、FlashAttention、CUDA、Triton、CUDA Graph |
| 三 单机推理 | 12 模型压缩与加速 | 90–98 | 量化、GPTQ/AWQ、FP8/FP4、KV 量化、投机解码 |
| 四 分布式推理 | 13 分布式与集合通信 | 99–109 | All-Reduce、张量并行、流水并行、MoE 专家并行、拓扑映射 |
| 四 分布式推理 | 14 分布式推理与集群 | 110–116 | 张量并行推理、PD 分离、KV Cache 传输、SLO 容量规划 |
| 五 推理引擎实践 | 15 手写迷你推理引擎 | 117–125 | 从带 KV Cache 的生成到 vLLM 对比，逐版实现 |
| 五 推理引擎实践 | 16 解读 nano-vllm | 126–128 | 读一个千行级的引擎源码，并动手改造 |
| 五 推理引擎实践 | 17 主流推理引擎 | 129–133 | vLLM、SGLang 等架构与源码阅读方法 |
| 六 芯模适配和调优 | 18 适配原理 | 134–141 | 换一块卡要重做什么：软件栈、硬件差异、CUDA 迁移、精度对齐、算子缺口 |
| 六 芯模适配和调优 | 19 调优原理 | 142–147 | 新硬件上的性能分析、矩阵与注意力适配、自定义 kernel、通信库、硬件插件 |
| 六 芯模适配和调优 | 20 案例：海光 DCU | 148–153 | 用前两篇的框架拆开一块真实国产卡，并逐步读它的 vLLM 插件源码 |

### 全部课程（点击讲标题即可读对应 .mdx） 

#### 第一章 数学基础

> 只讲后面真正会用到的数学。标「重点」的是推理优化会反复用到的点。


**第 1 篇 · 数学基础**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [01 · 向量](./src/content/lectures/01-vector.mdx) | 为什么模型要把一切变成一串数字 | 在平面上拖动向量，看坐标变化 |
| [02 · 点积与余弦相似度](./src/content/lectures/02-dot-product.mdx) | 怎么衡量两个向量“像不像” | 拖动两个向量，实时显示点积和夹角 |
| [03 · 矩阵与矩阵乘法](./src/content/lectures/03-matrix-multiplication.mdx) | 怎么一次对一批向量做同一种变换 | 矩阵步进器：逐格高亮“行 × 列”，算出结果 |
| [04 · 线性变换的几何意义](./src/content/lectures/04-linear-transformation.mdx) | 矩阵乘法对空间做了什么 | 改矩阵元素，看网格被拉伸、旋转、剪切 |
| [05 · 张量与形状](./src/content/lectures/05-tensors-and-shapes.mdx) | [b, s, d] 这样的形状到底代表什么 | 形状追踪器：每步运算后形状怎么变 |
| [06 · 指数、对数与 softmax](./src/content/lectures/06-exp-log-softmax.mdx) | 怎么把任意分数变成概率 | 输入一组分数，调温度看分布变尖或变平 |
| [07 · 概率分布与采样](./src/content/lectures/07-probability-sampling.mdx) | 模型输出概率，怎么从中选一个词 | 按分布抽样 100 次，看直方图 |
| [08 · 导数、偏导与链式法则](./src/content/lectures/08-derivatives-chain-rule.mdx) | 函数变化有多快，多个变量、多层嵌套时怎么算 | 拖动曲线上的点看切线斜率；链式相乘的分步演示 |
| [09 · 三角函数与旋转](./src/content/lectures/09-trig-rotation.mdx) （选读） | 为位置编码和 RoPE 做准备 | 在单位圆上旋转向量，看 sin、cos 变化 |
| [10 · 浮点数与数值精度](./src/content/lectures/10-floating-point.mdx) ⭐ | 为什么 FP16、BF16、FP8、FP4 会影响速度和精度 | 位级查看器：同一个数在不同格式下的比特和误差 |
| [11 · 计算量与 FLOPs](./src/content/lectures/11-flops.mdx) ⭐ | 怎么估算一次运算要算多少 | 输入矩阵尺寸，算出乘加次数 |

#### 第二章 大模型基础

> 从感知机一路讲到现代大模型架构；第 6 篇是轻量线，可与主线并行；第 7 篇从零写一个 GPT，在讲义上训练它。


**第 2 篇 · 神经网络基础**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [12 · 感知机](./src/content/lectures/12-perceptron.mdx) | 最早的神经网络长什么样，能做什么、不能做什么 | 拖动分界线做二分类，看异或问题为什么分不开 |
| [13 · 神经元与线性层](./src/content/lectures/13-neuron-linear-layer.mdx) | 最小的可学习单元是什么 | 调权重和偏置，看输出怎么变 |
| [14 · 激活函数](./src/content/lectures/14-activation-functions.mdx) | 为什么只靠线性层不够 | 切换 ReLU、GELU、SiLU，看曲线和拟合效果 |
| [15 · 多层感知机](./src/content/lectures/15-mlp.mdx) | 层叠起来为什么能拟合复杂函数 | 小网络拟合一条曲线，看每层的作用 |
| [16 · 损失函数](./src/content/lectures/16-loss-functions.mdx) | 怎么衡量预测错了多少（MSE、交叉熵、困惑度） | 调预测概率，看 loss 和困惑度变化 |
| [17 · 梯度与梯度下降](./src/content/lectures/17-gradient-descent.mdx) | 参数该往哪个方向改、改多少 | 在 loss 曲面上一步步下降，调学习率看效果 |
| [18 · 反向传播](./src/content/lectures/18-backpropagation.mdx) | 梯度怎么从 loss 传回每个参数 | 计算图上前向算值、反向算梯度 |
| [19 · 优化器](./src/content/lectures/19-optimizers.mdx) | SGD、Momentum、Adam 有什么区别 | 同一曲面上对比三种优化器的轨迹 |
| [20 · 完整的训练循环](./src/content/lectures/20-training-loop.mdx) | batch、epoch、学习率是什么 | 在浏览器里训练一个小网络，实时看 loss 曲线 |

**第 3 篇 · 从文本到向量**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [21 · 分词与 BPE](./src/content/lectures/21-tokenization-bpe.mdx) | 文字怎么变成模型能处理的编号 | 输入一句话，看 BPE 逐步合并 |
| [22 · 词嵌入 Embedding](./src/content/lectures/22-embedding.mdx) | 编号怎么变成有含义的向量 | 查表动画：token id 对应嵌入矩阵的一行；在二维投影里看相近的词 |
| [23 · 预测下一个 token](./src/content/lectures/23-next-token-prediction.mdx) | 大模型到底在学什么 | 给一句前缀，看下一个词的概率排行 |
| [24 · 自回归生成](./src/content/lectures/24-autoregressive-generation.mdx) | 一个词一个词怎么生成一整段 | 逐步生成，每步把新词接回输入 |

**第 4 篇 · Transformer 核心**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [25 · 位置编码](./src/content/lectures/25-positional-encoding.mdx) | 注意力本身不懂词序 | 调位置，看正余弦编码的波形 |
| [26 · 自注意力](./src/content/lectures/26-self-attention.mdx) | 每个词怎么看到上下文 | Q·K 打分 → softmax → 加权 V，逐步计算 |
| [27 · 因果掩码](./src/content/lectures/27-causal-mask.mdx) ⭐ | 生成时为什么不能偷看后面 | 掩码矩阵叠加到注意力热力图上 |
| [28 · 多头注意力](./src/content/lectures/28-multi-head-attention.mdx) | 为什么要从多个角度看 | 切换不同的头，看各自的注意力模式 |
| [29 · 残差连接](./src/content/lectures/29-residual-connection.mdx) | 网络深了为什么还能训练 | 开关残差，对比梯度在层间的衰减 |
| [30 · LayerNorm](./src/content/lectures/30-layernorm.mdx) | 为什么要把每层输出拉回统一尺度 | 输入一组数，逐步算均值、方差、归一化 |
| [31 · FFN 前馈网络](./src/content/lectures/31-ffn.mdx) | 注意力之后每个词各自做什么 | 升维 → 激活 → 降维，看形状变化 |
| [32 · Transformer Block](./src/content/lectures/32-transformer-block.mdx) | 这些部件怎么组合成一层 | 可展开的结构图，点部件跳到对应的讲 |
| [33 · 输出层](./src/content/lectures/33-output-layer.mdx) | 最后一层怎么变成词表上的概率 | lm_head 投影 + softmax，看概率排行 |
| [34 · 完整前向传播](./src/content/lectures/34-full-forward-pass.mdx) | 一句话进去、下一个词出来，中间发生了什么 | 用玩具模型走完全程，每步可查看数值 |
| [35 · 参数量与计算量](./src/content/lectures/35-params-and-flops.mdx) ⭐ | 一个模型有多少参数、算一次要多少 FLOPs | 输入模型配置，逐层统计参数和 FLOPs |

**第 5 篇 · 现代 LLM 架构**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [36 · Pre-Norm 与 RMSNorm](./src/content/lectures/36-prenorm-rmsnorm.mdx) | 现代模型为什么换了归一化的位置和方式 | 对比 LayerNorm 与 RMSNorm 的计算步骤 |
| [37 · RoPE 旋转位置编码](./src/content/lectures/37-rope.mdx) | 怎么让注意力直接感知相对位置 | 看 Q、K 随位置旋转，点积只和距离有关 |
| [38 · SwiGLU 与门控 FFN](./src/content/lectures/38-swiglu.mdx) | 为什么门控结构效果更好 | 调门控值，看信息被放行多少 |
| [39 · MQA 与 GQA](./src/content/lectures/39-mqa-gqa.mdx) ⭐ | 怎么减少 KV 头数来省显存 | 切换 MHA、GQA、MQA，看 KV cache 大小变化 |
| [40 · MLA 多头潜在注意力](./src/content/lectures/40-mla.mdx) ⭐ | 怎么进一步压缩 KV | 低秩压缩与还原的投影动画 |
| [41 · MoE 混合专家](./src/content/lectures/41-moe.mdx) ⭐ | 怎么让参数很多但每次只算一部分 | 路由器为每个 token 选专家，看负载分布 |
| [42 · 长上下文技术](./src/content/lectures/42-long-context.mdx) （选读） | 怎么把上下文从几千扩到百万级 | 滑动窗口与位置插值示意 |
| [43 · 架构演进对照](./src/content/lectures/43-architecture-evolution.mdx) | GPT-2、Llama、DeepSeek 到底改了什么 | 三列结构图，点差异处展开 |
| [44 · 混合架构与线性注意力](./src/content/lectures/44-linear-attention-hybrid.mdx) （选读） | 有没有比注意力更省的结构 | 复杂度曲线对比 O(n²) 与 O(n) |

**第 6 篇 · 训练全流程**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [45 · 预训练与数据](./src/content/lectures/45-pretraining-data.mdx) （选读） | 模型的知识从哪里来 | 数据清洗流水线示意 |
| [46 · Scaling Laws](./src/content/lectures/46-scaling-laws.mdx) （选读） | 模型多大、数据多少才划算 | 调算力预算，看最优参数量和数据量 |
| [47 · 监督微调 SFT](./src/content/lectures/47-sft.mdx) （选读） | 怎么让模型学会对话和遵循指令 | 对比微调前后的回答 |
| [48 · RLHF 与 DPO](./src/content/lectures/48-rlhf-dpo.mdx) （选读） | 怎么让回答符合人的偏好 | 偏好对比打分示意 |
| [49 · 推理模型与强化学习](./src/content/lectures/49-reasoning-rl.mdx) （选读） | 模型怎么学会“先想再答” | 多次采样、按奖励排名示意 |
| [50 · LoRA 参数高效微调](./src/content/lectures/50-lora.mdx) （选读） | 怎么只训练很少的参数 | 调秩 r，看参数量变化 |
| [51 · 模型评测](./src/content/lectures/51-evaluation.mdx) （选读） | 怎么判断一个模型好不好 | 基准题目示例与评分方式 |

**第 7 篇 · 从零实现一个 GPT 模型**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [52 · g0 · 语料与分词器](./src/content/lectures/52-g0-corpus-tokenizer.mdx) | 把一门课的讲义变成模型能读的编号 | 对应原理讲 21 |
| [53 · g1 · 数据加载器与嵌入](./src/content/lectures/53-g1-dataloader-embedding.mdx) | 一长串 token 怎么切成训练样本，编号怎么变成向量 | 对应原理讲 22–25 |
| [54 · g2 · 因果多头注意力](./src/content/lectures/54-g2-causal-attention.mdx) ⭐ | 从打分、掩码到多头，一次矩阵乘算完所有头 | 对应原理讲 26–28 |
| [55 · g3 · 组装 GPT](./src/content/lectures/55-g3-assemble-gpt.mdx) | LayerNorm、GELU、FFN、残差拼成一个能生成文字的模型 | 对应原理讲 29–35 |
| [56 · g4 · 预训练](./src/content/lectures/56-g4-pretraining.mdx) ⭐ | 在讲义上训练，让模型学会预测下一个 token | 对应原理讲 16–20、45 |
| [57 · g5 · 解码与存档](./src/content/lectures/57-g5-decoding-checkpoint.mdx) | 温度、Top-k、Top-p 怎么改变生成；训练怎么存档、续训 | 对应原理讲 73 |
| [58 · g6 · 装进 GPT-2 的权重](./src/content/lectures/58-g6-load-gpt2.mdx) | 同一份代码换上公开的权重，怎么确认装对了 | 对应原理讲 43 |
| [59 · g7 · 指令微调](./src/content/lectures/59-g7-instruction-tuning.mdx) | 只在回答上算 loss，让模型学会按格式回答问题 | 对应原理讲 47、50 |

#### 第三章 单机推理

> 推理优化的主体：先讲硬件怎么决定上限，再讲推理基础、引擎、算子和压缩。


**第 8 篇 · 硬件与性能基础**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [60 · GPU 架构：SM 与 Tensor Core](./src/content/lectures/60-gpu-architecture.mdx) | GPU 为什么比 CPU 适合矩阵运算 | GPU 结构图，点部件看说明 |
| [61 · 存储层级：HBM 与 SRAM](./src/content/lectures/61-memory-hierarchy.mdx) ⭐ | 数据在哪里、搬一次要多久 | 搬运动画：各层级的容量和带宽对比 |
| [62 · Roofline 模型](./src/content/lectures/62-roofline.mdx) ⭐ | 一个运算卡在算力还是带宽 | 拖动算术强度，看落在哪个瓶颈区 |
| [63 · 低精度计算](./src/content/lectures/63-low-precision-compute.mdx) | 为什么精度越低越快 | 不同精度的理论算力与显存占用对比 |
| [64 · 互联：PCIe、NVLink、InfiniBand、RoCE](./src/content/lectures/64-interconnect.mdx) ⭐ | 卡与卡、机与机之间怎么通信 | 拓扑图：切换互联方式看带宽与延迟 |
| [65 · scale-up、scale-out 与超节点](./src/content/lectures/65-scale-up-scale-out.mdx) ⭐ | 为什么要把更多卡放进一个高带宽域 | 同一次通信在两种拓扑下的耗时对比 |
| [66 · 性能分析与 Profiling](./src/content/lectures/66-profiling.mdx) | 怎么找到真正的瓶颈 | 读懂一张 Profiler 时间线 |
| [67 · 理论值对上实测值](./src/content/lectures/67-theory-vs-measurement.mdx) | 手算的速度和实际跑出来差多少 | 以 DGX Spark 为例，把实测点叠到 Roofline 上 |

**第 9 篇 · 推理基础**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [68 · Prefill 与 Decode](./src/content/lectures/68-prefill-decode.mdx) | 为什么第一个词和后面的词瓶颈不同 | 时间线：prefill 一次并行，decode 逐步进行 |
| [69 · KV Cache](./src/content/lectures/69-kv-cache.mdx) ⭐ | 怎么避免重复计算历史 token | 有缓存和无缓存的计算量对比动画 |
| [70 · TTFT、TPOT 与吞吐](./src/content/lectures/70-ttft-tpot-throughput.mdx) | 怎么衡量“快” | 调并发数，看三项指标此消彼长 |
| [71 · 显存账本](./src/content/lectures/71-memory-ledger.mdx) ⭐ | 权重、KV cache、激活各占多少 | 显存计算器：输入模型和并发，看占用条 |
| [72 · 推理成本模型](./src/content/lectures/72-cost-model.mdx) ⭐ | 怎么手算理论速度和每 token 成本 | 速度与成本计算器 |
| [73 · 解码策略](./src/content/lectures/73-decoding-strategies.mdx) | 贪心、Top-k、Top-p、温度怎么选词 | 调参数，看候选词范围变化 |

**第 10 篇 · 推理引擎与调度**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [74 · Continuous Batching](./src/content/lectures/74-continuous-batching.mdx) | 怎么让 GPU 不空等 | 甘特图：静态批处理与连续批处理对比 |
| [75 · PagedAttention](./src/content/lectures/75-paged-attention.mdx) | 怎么解决 KV 显存碎片 | 块分配模拟器：请求进出、block table 更新 |
| [76 · Prefix Cache](./src/content/lectures/76-prefix-cache.mdx) | 怎么跨请求复用相同前缀 | 命中模拟器：改一个 token，看命中率变化 |
| [77 · Chunked Prefill](./src/content/lectures/77-chunked-prefill.mdx) | 长 prompt 怎么不卡住其他请求 | 时间线：切块前后 decode 延迟对比 |
| [78 · 调度与抢占](./src/content/lectures/78-scheduling-preemption.mdx) | 显存不够时先服务谁 | 请求队列模拟 |
| [79 · 多 LoRA 服务](./src/content/lectures/79-multi-lora-serving.mdx) （选读） | 一台机器怎么同时服务几百个微调版本 | 显存里放几百个 LoRA，看一步 batch 怎么混着算 |
| [80 · 结构化输出与约束解码](./src/content/lectures/80-constrained-decoding.mdx) （选读） | 怎么保证输出是合法的 JSON | 每步屏蔽非法 token 的示意 |
| [81 · 一个请求的完整生命周期](./src/content/lectures/81-request-lifecycle.mdx) | vLLM、SGLang 内部各模块怎么协作 | 架构图：请求流经各模块 |
| [82 · 推理压测实践](./src/content/lectures/82-inference-benchmark.mdx) | 怎么做一次可信的 benchmark | 吞吐-延迟曲线示例 |

**第 11 篇 · 算子与 Kernel**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [83 · 算子融合](./src/content/lectures/83-kernel-fusion.mdx) | 为什么少搬一次数据就快 | 融合前后的显存读写次数对比 |
| [84 · FlashAttention](./src/content/lectures/84-flashattention.mdx) | 注意力的访存瓶颈怎么解决 | 分块计算动画：数据留在 SRAM |
| [85 · Decode 阶段的注意力 Kernel](./src/content/lectures/85-decode-attention-kernel.mdx) | 怎么读分散在各个块里的 KV | 按 block table 读取的动画 |
| [86 · CUDA 编程模型](./src/content/lectures/86-cuda-programming-model.mdx) | 线程、块、网格是什么 | 线程网格映射到矩阵的示意 |
| [87 · 矩阵乘法 Kernel 与 Tensor Core](./src/content/lectures/87-gemm-tensor-core.mdx) ⭐ | 模型里最多的运算，GPU 上怎么算到接近峰值 | 调分块大小，看数据复用、算术强度和 Tensor Core 利用率 |
| [88 · Triton 入门](./src/content/lectures/88-triton-intro.mdx) | 怎么用 Python 写 GPU kernel | 代码与分块示意并排 |
| [89 · CUDA Graph 与调度开销](./src/content/lectures/89-cuda-graph.mdx) （选读） | 小算子多时 CPU 为什么成了瓶颈 | 启动开销时间线对比 |

**第 12 篇 · 模型压缩与加速**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [90 · 量化基础](./src/content/lectures/90-quantization-basics.mdx) | 怎么用更少的比特表示一个数 | 量化与反量化步进器，看误差 |
| [91 · 权重量化：GPTQ 与 AWQ](./src/content/lectures/91-gptq-awq.mdx) | 怎么量化权重又不掉太多精度 | 离群值对量化误差的影响 |
| [92 · 激活量化与 SmoothQuant](./src/content/lectures/92-smoothquant.mdx) | 激活值的离群点怎么处理 | 平滑缩放前后的分布对比 |
| [93 · FP8 与 FP4](./src/content/lectures/93-fp8-fp4.mdx) ⭐ | 新硬件上的低精度格式怎么用 | 格式对比与分组缩放示意 |
| [94 · KV Cache 量化](./src/content/lectures/94-kv-cache-quantization.mdx) | 怎么压缩缓存来提升并发 | 精度与可容纳 token 数的对比 |
| [95 · KV Cache 压缩与驱逐](./src/content/lectures/95-kv-cache-eviction.mdx) （选读） | 上下文很长时，哪些 KV 可以丢掉 | 调缓存预算，看注意力汇聚点、H2O、SnapKV 留下哪些 token |
| [96 · 投机解码](./src/content/lectures/96-speculative-decoding.mdx) | 怎么一次验证多个 token | 草稿-验证动画，调接受率看加速比 |
| [97 · EAGLE 与 Medusa](./src/content/lectures/97-eagle-medusa.mdx) （选读） | 怎么不用单独的小模型来猜 | 多头预测示意 |
| [98 · 蒸馏与剪枝](./src/content/lectures/98-distillation-pruning.mdx) （选读） | 怎么得到更小的模型 | 剪枝前后结构对比 |

#### 第四章 分布式推理

> 从互联和通信的角度讲推理，是全站最有差异化的一章。


**第 13 篇 · 分布式与集合通信**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [99 · 为什么需要多卡](./src/content/lectures/99-why-multi-gpu.mdx) | 一张卡放不下、算不完时怎么办 | 模型大小与单卡显存的对比 |
| [100 · 集合通信原语](./src/content/lectures/100-collective-communication.mdx) | All-Reduce、All-Gather、Reduce-Scatter、All-to-All 是什么 | 每种原语的数据流动动画 |
| [101 · Ring 与 Tree All-Reduce](./src/content/lectures/101-ring-tree-allreduce.mdx) | 通信怎么组织才最高效 | 环形传递的分步动画 |
| [102 · 通信代价模型](./src/content/lectures/102-communication-cost-model.mdx) ⭐ | 怎么估算一次通信要多久 | α-β 计算器：调带宽、延迟和数据量 |
| [103 · 数据并行与 ZeRO/FSDP](./src/content/lectures/103-data-parallel-zero.mdx) | 怎么把训练状态切到多卡 | 切分示意：参数、梯度、优化器状态 |
| [104 · 混合精度训练与激活重计算](./src/content/lectures/104-mixed-precision-recompute.mdx) | 训练时激活值占了多少显存，怎么省 | 调序列长度和重计算策略，看显存和计算量的此消彼长 |
| [105 · 张量并行](./src/content/lectures/105-tensor-parallel.mdx) | 怎么把一个矩阵乘法拆到多卡 | 按行、按列切分矩阵的步进演示 |
| [106 · 流水并行](./src/content/lectures/106-pipeline-parallel.mdx) | 怎么把不同层放到不同卡 | 流水线甘特图与气泡 |
| [107 · 序列并行与上下文并行](./src/content/lectures/107-sequence-context-parallel.mdx) （选读） | 超长序列怎么拆 | 序列切分示意 |
| [108 · 专家并行与 All-to-All](./src/content/lectures/108-expert-parallel.mdx) ⭐ | MoE 的专家怎么分布、token 怎么分发 | token 路由到不同卡的动画 |
| [109 · 并行策略与拓扑映射](./src/content/lectures/109-parallelism-topology.mdx) ⭐ | 哪种并行该放在哪一层互联上 | 把并行维度拖到拓扑上，看通信时间 |

**第 14 篇 · 分布式推理与集群**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [110 · 推理中的张量并行](./src/content/lectures/110-tp-in-inference.mdx) | 多卡推理时延迟和吞吐怎么变 | 并行度与延迟的关系曲线 |
| [111 · MoE 推理与大规模专家并行](./src/content/lectures/111-moe-inference-ep.mdx) ⭐ | 为什么 MoE 推理的瓶颈常在网络 | 调互联带宽，看吞吐变化 |
| [112 · PD 分离](./src/content/lectures/112-pd-disaggregation.mdx) | 为什么把 prefill 和 decode 拆到不同机器 | 两种部署方式的时间线对比 |
| [113 · KV Cache 传输与分层存储](./src/content/lectures/113-kv-transfer-tiered-storage.mdx) | 缓存怎么在机器之间、显存和内存之间流动 | 存储层级与传输路径动画 |
| [114 · 缓存感知路由与负载均衡](./src/content/lectures/114-cache-aware-routing.mdx) | 请求该发给哪台机器 | 路由模拟：随机分发与按前缀分发对比 |
| [115 · 超节点上的推理](./src/content/lectures/115-supernode-inference.mdx) ⭐ | 高带宽域对哪类负载收益最大 | 基于公开资料的场景对比 |
| [116 · SLO 与容量规划](./src/content/lectures/116-slo-capacity-planning.mdx) | 给定流量和延迟要求，需要多少卡 | 容量计算器 |

#### 第五章 推理引擎实践

> 先手写一个迷你推理引擎（每讲一个能跑的版本），再读 nano-vllm，最后读 vLLM、SGLang 等主流引擎。


**第 15 篇 · 手写迷你推理引擎**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [117 · 总览 · 一个推理引擎由哪些部分组成](./src/content/lectures/117-engine-overview.mdx) | 从输入文字到输出文字，经过哪些模块 | 对应原理讲 68、81 |
| [118 · v0 · 从权重文件到第一个 token](./src/content/lectures/118-v0-forward.mdx) | 不借助任何框架，自己写出 Qwen3 的前向 | 对应原理讲 33–39 |
| [119 · v1 · KV Cache](./src/content/lectures/119-v1-kv-cache.mdx) ⭐ | 生成第 N 个 token 时，不再重算前面的 N − 1 个 | 对应原理讲 68–69 |
| [120 · v2 · Continuous Batching](./src/content/lectures/120-v2-continuous-batching.mdx) ⭐ | 让多个请求共享一次前向，随到随走 | 对应原理讲 66 |
| [121 · v3 · 分页 KV 管理](./src/content/lectures/121-v3-paged-kv.mdx) ⭐ | KV 按块按需分配，同样的显存放下更多请求 | 对应原理讲 75、78 |
| [122 · v3+ · 前缀缓存](./src/content/lectures/122-v3-prefix-cache.mdx) | 相同的前缀只算一次 | 对应原理讲 68 |
| [123 · v4 · 权重量化](./src/content/lectures/123-v4-quantization.mdx) | 用四分之一的内存放下权重 | 对应原理讲 90–91 |
| [124 · v5 · 投机解码](./src/content/lectures/124-v5-speculative.mdx) | 一次前向验证多个 token | 对应原理讲 96–97 |
| [125 · 复盘 · 时间花在哪里](./src/content/lectures/125-review.mdx) | 和工业级引擎差在哪里 | 对应原理讲 66、82、89 |

**第 16 篇 · 解读 nano-vllm**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [126 · nano-vllm 的整体结构](./src/content/lectures/126-nano-vllm-overview.mdx) | 一个一千多行的引擎是怎么组织的 | 对应第 15 篇各讲 |
| [127 · nano-vllm 多做了什么](./src/content/lectures/127-nano-vllm-gpu.mdx) | FlashAttention、CUDA Graph、张量并行怎么接进来 | 对应原理讲 84、85、89、105 |
| [128 · 动手改 nano-vllm](./src/content/lectures/128-nano-vllm-spec.mdx) | 把我们的投机解码移植过去 | 对应第 124 讲 |

**第 17 篇 · 主流推理引擎**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [129 · vLLM 的架构](./src/content/lectures/129-vllm-architecture.mdx) ⭐ | 一个请求在 vLLM 里怎么走一圈 | 对应原理讲 74–81 |
| [130 · vLLM 的分布式服务](./src/content/lectures/130-vllm-distributed-serving.mdx) | 一条请求在多节点、多副本的 vLLM 里怎么走一圈：数据并行、负载均衡、PD 分离的 KV 搬运 | 对应原理讲 111–114 |
| [131 · SGLang 的架构](./src/content/lectures/131-sglang-architecture.mdx) | RadixAttention 与零开销调度 | 对应原理讲 76、80、89 |
| [132 · 其他引擎与规模化部署](./src/content/lectures/132-other-engines-at-scale.mdx) | TensorRT-LLM、LMDeploy、llama.cpp，以及大规模 EP 的实现 | 对应原理讲 108–116 |
| [133 · 怎么读大型引擎的源码](./src/content/lectures/133-reading-engine-source.mdx) | 从哪里读起、怎么定位、怎么压测和贡献 | 对应原理讲 66、82 |

#### 第六章 芯模适配和调优

> 把模型搬到一块新芯片上的通用原理：要重做哪几层、硬件路线有什么不同、代码和框架怎么迁、精度怎么对齐、性能怎么调；最后以海光 DCU 为案例逐条落地。


**第 18 篇 · 适配原理：把模型跑通**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [134 · 总览：换一块卡要重做什么](./src/content/lectures/134-porting-overview.mdx) | 从模型到芯片中间有哪几层，哪些能复用、哪些要重写 | 软件栈分层图：切换 NVIDIA / 兼容 GPGPU / NPU，看每层对应什么 |
| [135 · 国产与非 NVIDIA 加速器的硬件差异](./src/content/lectures/135-accelerator-differences.mdx) ⭐ | GPGPU 和 NPU 两条路线的计算单元、线程组、片上存储有什么不同 | 选一款卡的参数，看拐点和各类算子落在哪个区 |
| [136 · 编程模型与 CUDA 迁移](./src/content/lectures/136-cuda-migration.mdx) | CUDA 代码哪些能自动迁、哪些必须手改 | CUDA 片段逐行翻译，标出要手改的地方 |
| [137 · 框架怎么接入新硬件](./src/content/lectures/137-framework-backend.mdx) | PyTorch 怎么认识一块新卡，算子怎么分发、缺了怎么回退 | 一次 x @ w 的分发路径 |
| [138 · 图模式与编译](./src/content/lectures/138-graph-mode-compile.mdx) | 为什么有的硬件更依赖整图下发，torch.compile 怎么接新后端 | 逐算子与整图两种模式的下发次数对比 |
| [139 · 精度对齐](./src/content/lectures/139-precision-alignment.mdx) ⭐ | 换卡后输出不一致怎么查 | 逐层误差曲线：从哪一层开始偏离 |
| [140 · 算子缺口：盘点、组合、自写](./src/content/lectures/140-operator-gap.mdx) | 一个模型要用哪些算子，缺了怎么办 | 模型算子清单：已支持、可组合、需自写 |
| [141 · 实操：把 miniinfer 移植到非 CUDA 后端](./src/content/lectures/141-port-miniinfer.mdx) | 在 Apple MPS 上真实走一遍移植 | 真实运行结果与 CPU 版逐 token 比对 |

**第 19 篇 · 调优原理：把模型跑快**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [142 · 在新硬件上做性能分析](./src/content/lectures/142-profiling-new-hardware.mdx) | 厂商 profiler 的时间线怎么读，按什么顺序找瓶颈 | 带标注的时间线：点每段看属于哪类瓶颈 |
| [143 · 矩阵乘法与注意力的适配](./src/content/lectures/143-gemm-attention-adaptation.mdx) ⭐ | 矩阵单元的形状、对齐和数据排布怎么影响 kernel | 调分块和对齐，看矩阵单元利用率 |
| [144 · 用 Triton 与厂商语言写 kernel](./src/content/lectures/144-writing-kernels.mdx) | 同一个 kernel 在不同后端上怎么写 | 同一个 RMSNorm 的几种写法并排对照 |
| [145 · 低精度与量化的取舍](./src/content/lectures/145-low-precision-tradeoffs.mdx) | 硬件不原生支持某种精度时怎么办 | 选硬件和精度，看能否直接用、怎么替代 |
| [146 · 集合通信库与多卡互联](./src/content/lectures/146-collective-libraries.mdx) | NCCL 之外的通信库和拓扑怎么影响多卡 | 切换拓扑，看 All-Reduce 耗时 |
| [147 · 推理引擎的硬件插件](./src/content/lectures/147-engine-hardware-plugin.mdx) ⭐ | 不改上游代码，怎么把一块新卡接进推理引擎 | 插件接口图：每个接口替换了引擎里的哪个模块 |

**第 20 篇 · 案例：海光 DCU**

| 讲 | 标题 | 解决什么问题 | 示例交互 |
| --- | --- | --- | --- |
| [148 · 海光 DCU 的软硬件栈](./src/content/lectures/148-hygon-dcu-stack.mdx) | 用前两篇的框架拆开一块真实的国产卡 | 海光软件栈与 CUDA 栈逐层对照 |
| [149 · 从 CUDA 到 DCU：迁移与版本矩阵](./src/content/lectures/149-cuda-to-dcu.mdx) | HIP、PyTorch DCU 版和版本对应 | 版本矩阵检查 |
| [150 · 读 vllm-plugin-das：平台类与运行时补丁](./src/content/lectures/150-reading-vllm-plugin-das.mdx) | 海光的 vLLM 插件是怎么组织的 | 对应第 147 讲 |
| [151 · DCU 上的矩阵乘：hipBLASLt、MMAC 与小 M kernel](./src/content/lectures/151-dcu-gemm-kernel.mdx) | 为什么库选的分块不适合 decode，专用 kernel 怎么写 | 对应第 143 讲 |
| [152 · DCU 上的注意力、量化与通信](./src/content/lectures/152-dcu-attention-quant-comm.mdx) | 插件怎么选注意力后端、量化方法和通信方式 | 对应第 143–146 讲 |
| [153 · 复盘：一个模型上线 DCU 的完整清单](./src/content/lectures/153-dcu-launch-checklist.mdx) | 从拿到卡到上线，每一步的验收标准 | 可勾选的适配清单 |


## 全文用到的案例模型：数字从哪来

全站只用两套例子，读者在不同讲里反复见到同一组数字，前后就能对上。

**玩具模型 TinyLM**（用于第一、二章的手算和交互，矩阵小到能在屏幕上完整展示）：

| 参数 | 取值 |
| --- | --- |
| 词表 | 6 个 token：我、爱、学、AI、推理、`<eos>` |
| 隐藏维度 d | 4 |
| 注意力头数 | 2（每头维度 2） |
| FFN 隐藏维度 | 8 |
| 层数 | 2 |
| 序列长度 | 最长 4 |

同一组权重从「03 矩阵乘法」一直用到「34 完整前向传播」。所有数值由 `tinylm/tinylm.py` 算出，文章和组件都读取它的输出。

**真实模型**（用于第 5 篇和第三至五章的参数、显存、速度计算）：

| 模型 | 类型 | 关键配置 |
| --- | --- | --- |
| Llama-3-8B | 稠密、GQA | 32 层、隐藏 4096、32 个 Q 头、8 个 KV 头、head_dim 128、FFN 14336、词表 128256 |
| DeepSeek-V3 | MoE、MLA | 总参数约 671B、每 token 激活约 37B |

**硬件**：一张数据中心 GPU（如 H100）作主参照，DGX Spark 作实测机器；两者带宽相差约十倍，正好用来讲 Roofline。


## 学习路线

网站提供两条路线，可随时切换（记在浏览器里）：

- **完整路线**：按 01 → 153 顺序学。第三到第六章按每周 2 天约 28 周。
- **Infra 快速路线**（共 127 讲）：第一章只读 03、05、06、10、11；第二章跳过 16–20（训练相关）和第 6 篇整篇；其余照常。适合已有基础、想尽快进入推理优化的读者。

## 本地运行

```bash
npm install
npm run dev      # 打开 http://localhost:4321
npm run build    # 生成静态站点到 dist/
npm run preview  # 本地预览构建结果
```

**导出 PDF**：`npm run pdf:book` 一键生成**全书合订本**（封面 + 总目录 + 每篇扉页 + 各讲 + 页码），输出到 `exports/AI-Infra-HandBook-全书.pdf`（构建临时区，被 `.gitignore` 忽略）。合订本会自动带上**导航目录**：侧边栏书签（篇 → 讲）＋目录页每一行可点击直达对应章节/讲。其它几种形式：

- `npm run pdf`：默认导出前 4 讲（01–04）合成一本
- `npm run pdf:all`：按「篇」分组，每篇一册（封面 + 篇目录 + 各讲）
- `node scripts/export-pdf.mjs 1 2 3 4`（或 `1,2,3,4`）：指定若干讲合成一本
- `node scripts/export-pdf.mjs book --no-build`：跳过 `astro build`，直接用现有 `dist/`

**发布下载版**：`npm run pdf:release` 把《全书》压缩后发布到仓库 `release/AI-Infra-HandBook.pdf`——也就是 README 顶部「PDF 下载」链接指向的那个文件。这个目录**单独管理、随仓库版本走**；而 `exports/` 只是被 `.gitignore` 忽略的构建临时区。

原理：先 `astro build` 生成静态 HTML，再用系统里已装的无头 Chrome（playwright）逐讲渲染，注入 `@media print` 样式去掉站点导航、按 A4 分页，拼上程序生成的封面与目录页，用 pdf-lib 合成并加页码；随后用 `scripts/add-pdf-nav.py`（python3 + PyMuPDF）写入侧边栏书签与目录可点击链接。压缩/发布用的是 Ghostscript（`brew install ghostscript`），会完整保留这些导航。（本机需装有 Google Chrome、python3 + PyMuPDF 与 Ghostscript。）

`scripts/check_lecture.py N` 会运行第 N 讲里的代码，并和贴出的输出逐字比对。

**目录结构**

```
site/
  src/
    data/course.ts            课程结构（6 章 20 篇 153 讲、快速路线规则）
    content/lectures/*.mdx    每讲一篇（本 README 的课程列表即链接到这里）
    components/               可复用交互组件
    pages/                    首页、篇页、文章页、搜索索引
    layouts/  styles/         布局与设计系统
  scripts/                    同步镜像、逐讲校验等
  release/                    发布的《全书》PDF 成品（README 顶部下载链接指向这里）
  tinylm/  minigpt/           玩具模型 / 迷你 GPT（数字与代码的来源）
```

> 网站构建读的是镜像 `site/miniinfer/`、`site/minigpt/`：文章新引用这些目录下的文件后，在 `site/` 下运行 `python3 scripts/sync_miniinfer.py` 同步。

## 参考与致谢

- 实践参考：miniinfer（手写迷你推理引擎 v0–v5）、nano-vllm、vLLM、SGLang，以及海光 DCU 的 vLLM 插件 vllm-plugin-das 等开源项目源码；第六章的可动手部分用本机 Apple MPS 真实运行。也向李博杰《深入理解 AI Infra》这类优秀的开源课程/图书致意。

---

> **在线阅读：** [在线阅读](https://ai-infra-handbook.sunxiaohui2022.workers.dev/) 　　 示例由大模型逐讲生成，若有笔误或建议欢迎在仓库提 Issue。

---

## 许可

本课程原创正文、配图及配套代码采用 Apache License 2.0 许可。Copyright © 2026 扶摇Sun（孙晓辉）。

仓库中的第三方代码、字体、模板与参考资料保留各自的版权和许可声明，不因收录于本仓库而改用 Apache-2.0；具体来源和使用条件见相应目录。
