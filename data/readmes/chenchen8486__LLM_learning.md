# LLM 机制学习手册

　　中文 | [English](README_en.md)

　　[![GitHub stars](https://img.shields.io/github/stars/chenchen8486/LLM_learning?style=social)](https://github.com/chenchen8486/LLM_learning/stargazers)
　　[![章节数](https://img.shields.io/badge/章节-16%20章%20%2B%20附录-6d28d9)](#3-章节结构)

## 1. 项目简介

　　本项目是一套中文大语言模型（LLM）机制学习手册，内容覆盖训练数据、分词、词向量与位置编码、Transformer 架构、预训练、中间训练、后训练、推理部署、应用范式及多模态扩展。手册结合公式推导、原创 SVG 示意图与开源代码实现，对主要机制进行分章说明。

　　构建产物随仓库发布，支持在线阅读和本地浏览。在线阅读地址：<https://chenchen8486.github.io/LLM_learning/>。

![Transformer 注意力机制动画](assets/transformer-detailed-2.gif)

　　注意力机制动画示意（画面风格引自 3Blue1Brown《Attention in transformers》）。

## 2. 内容特点

- 生命周期主线：第 0 章至第 15 章依次介绍数据、分词、词向量与位置编码、模型架构、预训练、中间训练、后训练、推理与后处理、部署优化、应用范式及多模态扩展。
- 公式与图示结合：关键公式附符号说明，矩阵运算、注意力机制、KV Cache、量化和投机采样等内容配有示意图。
- 代码实现对照：部分机制说明参照开源项目 [minimind](https://github.com/jingyaogong/minimind) 的 PyTorch 实现，引用位置注明文件名与行号。
- 前置知识补充：附录共 15 节，涵盖向量与旋转、点积与余弦相似度、softmax 与温度、交叉熵与困惑度、反向传播、激活与归一化、幂律与对数坐标等内容。
- 本地阅读工具：支持文字高亮、标注导出与导入，以及单条本地书签。个人标注和书签仅保存在浏览器 localStorage 中，不上传至服务器，也不写入仓库。

## 3. 章节结构

```text
第 0 章  全景导论：LLM 流水线总览
第 1 章  训练数据：收集、清洗、去重、配比与合成数据
第 2 章  分词：文本如何变成 Token
第 3 章  词向量与位置编码（含长度外推）
第 4 章  Transformer 架构精讲
第 5 章  现代架构变体与效率改进（RMSNorm / SwiGLU / GQA / MLA / MoE 等）
第 6 章  预训练：目标、优化与 Scaling Law
第 7 章  预训练工程：分布式并行、混合精度、稳定性与算力估算
第 8 章  中间训练（Mid-training）：长上下文扩展与领域适配
第 9 章  后训练 I：监督微调与参数高效微调（SFT / LoRA）
第 10 章 后训练 II：偏好对齐（RLHF / PPO / DPO 家族 / 安全对齐）
第 11 章 后训练 III：推理能力训练（RLVR / GRPO / 长思维链）
第 12 章 推理机制与后处理：解码策略、停止条件、结构化输出
第 13 章 推理系统与部署：KV Cache、量化、蒸馏、投机采样、推理时扩展
第 14 章 应用范式：Prompt / CoT / RAG / Function Calling / Agent
第 15 章 多模态扩展：ViT、CLIP、连接器、VLM 训练流水线、统一架构
附录     数学与深度学习基础速览（A.1–A.15）
```

　　各章由若干独立页面组成，页面统一设置快速浏览、正文讲解、示意图、要点回顾和参考来源。第 4 章以 Attention 原论文译文为依据，其余章节以原始论文和官方技术报告为主要依据，并在页面末尾列明出处。

## 4. 阅读与构建

### 4.1 在线阅读

　　访问 <https://chenchen8486.github.io/LLM_learning/>，通过页面侧边栏按章节顺序阅读，无需克隆仓库或执行构建命令。

### 4.2 本地阅读

　　克隆仓库后，可用浏览器打开根目录 `index.html`，也可直接打开 `output/html/ch0_1_what_is_llm.html`。公式与字体通过 CDN 加载，首次阅读需要网络连接。

### 4.3 重新构建

　　修改 `output/html/pages/` 中的正文源文件后，执行以下命令：

```bash
python output/html/build.py
```

　　构建脚本将重新生成 `output/html/ch*.html`。源文件与构建产物均纳入版本管理，仅阅读手册时无需执行构建。

## 5. 仓库结构

```text
LLM_learning/
├── index.html              # 阅读入口与本地书签跳转
├── README.md               # 中文项目说明
├── README_en.md            # 英文项目说明
├── LICENSE                 # 正文许可（CC BY-NC-SA 4.0）
├── assets/                 # README 预览素材
├── docs/                   # 开发方案、编写规范与发布材料
├── ref_paper/              # 参考论文（只读素材）
├── minimind-master/        # 代码参考（Apache 2.0）
└── output/html/
    ├── build.py            # 构建脚本
    ├── template.html       # 页面模板
    ├── static/global.css   # 全局样式
    ├── static/annotate.js  # 页面标注工具
    ├── static/bookmark.js  # 本地书签工具
    ├── pages/              # 手册正文源文件
    └── ch*.html            # 构建产物
```

## 6. 素材与参考来源

- 第 4 章以 `ref_paper/2016_attention_is_all_you_need/` 中的论文译文为依据。
- 其余章节以原始论文（arXiv）和官方技术报告为主要依据，各页末尾附参考来源。
- 代码对照内容引用自 minimind（Apache 2.0），引用位置注明相关文件与行号。
- `ref_paper/` 与 `minimind-master/` 仅作为参考资料使用，保留其原有权利声明和许可证。

## 7. 鸣谢

　　感谢开源项目 [minimind](https://github.com/jingyaogong/minimind) 及其作者、贡献者。该项目提供了分词、RoPE、RMSNorm、SwiGLU、GQA、预训练与微调等机制的 PyTorch 实现，为本手册的代码对照提供了参考。`minimind-master/` 是上游仓库的只读副本，保留原始 `LICENSE`，相关权利归原作者所有。

## 8. 许可证

　　手册正文采用 CC BY-NC-SA 4.0（署名—非商业性使用—相同方式共享）许可协议，使用与再分发须遵守协议条款，协议全文见根目录 [LICENSE](LICENSE)。`minimind-master/` 遵循其原有 Apache 2.0 许可证，`ref_paper/` 中论文的著作权归原作者与出版方所有。
