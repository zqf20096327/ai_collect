<div align="center">

# AI Paper Writing Skill

### 从「这一段写什么」到「这一句凭什么成立」

**面向 AI / AI＋图形学的论文写作 Skill：可填写模板 × 论文溯源 × 全文论证链**

[快速开始](#快速开始) · [模板预览](#模板长什么样) · [论文依据](#这些模板从哪里来) · [English](#english)

</div>

实验做完了，Introduction 还停在第一段？Method 像模块说明书，Experiments 像把表格念了一遍？

这个开源 skill 帮你把研究材料组织成论文：先厘清 **核心主张 → 关键困难 → 设计 → 证据**，再选择章节、段落和句子功能，完成起草、修订与检查。

你可以直接阅读这些 Markdown，也可以安装到 Codex，让写作助手按同一套有来源、可检查的流程工作。

| 当前包含 | 数量 |
|---|---:|
| 论文来源卡 | 36 篇 |
| 章节模板文件 | 7 个 |
| 可填写段落模块 | 74 个 |
| 句子功能槽位 | 289 个 |
| 论文功能定位记录 | 105 条 |
| 已核对原文短搭配 / 独立编写表达变体 | 42 / 60 条 |

**觉得有用，欢迎 Star ⭐。更欢迎提交一处有论文依据的修正，或分享模板在哪类研究上不适用。**

## 能帮你做什么

- **从材料起草正文**：给研究说明、方法和真实结果，按贡献类型组织英文论文；解释默认用中文。
- **逐段逐句规划**：每段解决什么问题，每句承担什么功能，需要什么事实支持。
- **选择适合的方法写法**：数学算法、架构、量化与系统、预训练、数据集与基准、神经图形学等按实际贡献选择。
- **丰富表达**：按任务界定、设计解释、结果比较、推断、局限等功能选句式，并区分 `suggest`、`show empirically`、`prove` 的强度。
- **检查论证断链**：困难有没有依据？设计如何回应困难？证据是否测到了主张？结论有没有扩大范围？
- **修改现有草稿**：保留技术含义、引用键与有效结构，避免为了套模板重写整篇。

适用于一般 AI 及 AI＋图形学；CAD 是可选应用。资源主要为中文说明＋英文填写句式。

## 快速开始

### 直接阅读

从 [SKILL.md](SKILL.md) 了解流程，或直接打开 [章节模板](references/templates.md)、[论证链](references/argument-chain.md)、[表达库](references/expressions.md)。

### 安装到 Codex

需要 Git。将仓库克隆到个人 skills 目录；下面按默认目录示例。已有同名安装时，先保留本地修改，再更新版本。

**macOS / Linux**

```bash
git clone https://github.com/Fasuiker/ai-graphics-paper-writing.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/ai-graphics-paper-writing"
```

**Windows PowerShell**

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex\skills' }
git clone https://github.com/Fasuiker/ai-graphics-paper-writing.git (Join-Path $skillRoot 'ai-graphics-paper-writing')
```

安装后重新打开 Codex 会话，使用 `$ai-graphics-paper-writing` 调用。仓库以 Markdown 指令和参考资料构成，安装后即可由助手加载使用。

### 复制这段就能开始

```text
使用 $ai-graphics-paper-writing 帮我起草论文。

研究任务与输入输出：[…]
最接近的工作及具体不足：[…，附引用或资料]
核心设计与直觉：[…]
已完成实验、表格及结果：[…]
适用范围与已知失败：[…]
本次希望完成：Introduction / Method / 全文等

先建立“核心主张→关键困难→设计→证据”的精简论证链，
再选择适合的模板并完成正文。
缺失证据用[待补]标记，分别列出已完成结果和计划实验。
```

还没有完整材料也能使用：保留占位符先规划；有局部草稿则直接请求局部修订，无需每次做整篇分析。

## 模板长什么样

以**大模型低比特量化论文的 Introduction** 为例：你希望降低 LLM 的部署成本，同时保持模型质量。Skill 会帮你把“做了一个量化方法”展开成读者能跟上的论证。

| 句子承担的工作 | 大模型写作模板 |
|---|---|
| 建立部署需求 | Deploying large language models on [target devices] requires reducing [memory usage / inference latency] while preserving [task performance]. |
| 定位量化困难 | At [target bit width], existing quantization methods suffer from [accuracy degradation / implementation overhead] under [evaluation conditions]. |
| 引出关键观察 | Our analysis of [activation statistics] identifies [weight channels] whose quantization has a disproportionate effect on [model output]. |
| 解释方法设计 | Guided by this observation, we apply [channel-wise scaling strategy] to reduce the quantization error of [the identified channels]. |
| 连接实际部署 | We implement [weight packing / fused kernels / dequantization strategy] to translate the reduced model size into lower inference latency on [hardware]. |
| 概括验证结果 | Across [model families and tasks], our method achieves [quality result] with [memory reduction and measured speedup] relative to [baseline]. |

**填完后，主线就清楚了：部署需求 → 低比特难点 → 激活统计观察 → 通道缩放设计 → 推理实现 → 质量与效率证据。**

这个例子使用 [X-I2 引言模块](references/chapter-templates/introduction.md) 的组织方式，结合已有大模型样本中的写作功能：

- [AWQ · MLSys 2024](references/expansion/cards/E06.md)：从重要权重的观察引出缩放策略，再用 TinyChat 连接算法与实测加速。
- [SmoothQuant · ICML 2023](references/expansion/cards/E05.md)：围绕量化精度和硬件效率建立问题，并分别交代质量、内存与延迟收益。

根据你的方法替换方括号中的内容；段落长度和句子组合随实际贡献调整。接着用 [X-M2 方法模块](references/chapter-templates/method.md) 解释设计，用 [X-E2 实验模块](references/chapter-templates/experiments.md) 展开质量与真实效率的验证。

## 用一条论证链串起全文

```mermaid
flowchart LR
    C[核心主张：要读者接受什么] --> H[关键困难：为什么难]
    H --> D[设计：如何回应困难]
    D --> E[证据：什么实际结果支持]
    E --> C
```

同一条主线在各章节承担不同任务：引言建立问题，方法解释设计，实验检验主张，讨论交代边界，结论回收得到支持的发现。

[论证链工具](references/argument-chain.md) 提供可填写表格、章节分工与断链检查，区分 **已有支持 / 部分支持 / 待验证 / 反证或冲突**。待验证的想法以假设或待补项保留，随研究进展更新。

## 每章一个文件

| 章节 | 内容入口 |
|---|---|
| Abstract | [问题、资源、结构洞察、质量与成本](references/chapter-templates/abstract.md) |
| Introduction | [工作流程、瓶颈、表示、监督、系统、基准、迁移](references/chapter-templates/introduction.md) |
| Related Work | [主题分类、最近工作、资源覆盖、算法与系统定位](references/chapter-templates/related-work.md) |
| Method | [总览、表示、学习、数学推导、可部署设计、数据构造](references/chapter-templates/method.md) |
| Experiments | [受控比较、质量与效率、机制消融、泛化、用户研究](references/chapter-templates/experiments.md) |
| Discussion | [失败、依赖、推断、适用范围](references/chapter-templates/discussion.md) |
| Conclusion | [方法、算法与系统、资源与发现收束](references/chapter-templates/conclusion.md) |

另附 [表达与用词库](references/expressions.md) 和 [写作检查清单](references/checklist.md)。

## 这些模板从哪里来

语料包括 NeurIPS、ICML、ICLR、CVPR、ICCV、ECCV、SIGGRAPH Conference Papers、ACM MM、MLSys，以及 TOG、TPAMI、TIP、TVCG 等发表渠道的论文及其对应公开作者稿。

语料选取了刘利刚、高林、朱军、韩松、吴佳俊、张国锋／崔兆鹏等作者参与的研究线，以及其他团队的代表性工作，按具体论文的论证功能整理。

- [基础语料：22 篇](references/exemplars.md)，其中 10 篇形成 58 条定位记录。
- [五年扩充：14 篇](references/expansion/index.md)，形成 47 条定位记录。
- [基础模板映射](references/fillable-template-map.json) / [扩充模板映射](references/expansion/modules.json)：连接填写模块与来源记录。
- [基础原文定位](references/template-evidence.md) / [扩充原文定位](references/expansion/evidence.md)：记录实际阅读版本、PDF 页码及文本块。

最近一次整理：**2026-09-10**。扩充检索窗口为 2022—2026 自然年，新增论文实际出版年份为 2022—2025；出版年与作者稿上传年分别记录。

来源库包含36篇论文卡；其中24篇支撑105条功能定位记录。模板分别标注单篇实例或跨论文归纳，并保留实际阅读范围。

## 怎样用得更好

提供研究说明、方法细节、实验表图和关键引用，能帮助 Skill 把模板落实成具体正文。起草后，结合实验记录核对数字与主张，并按目标会议或期刊的当年要求调整篇幅和格式。

当前已完成资源结构、来源定位和链接检查。下一阶段将通过真实稿件评估模板选择、全文连贯性和表达质量，欢迎分享使用反馈。

## 参与改进

欢迎提交 Issue 或 PR，尤其是：

- 带有公开论文链接、版本和页码的模板修正。
- 当前分支覆盖不到的研究类型，以及具体不适配原因。
- 经授权、已去除未公开信息的使用反馈。

新增表达时请标注“原文短搭配”或“独立抽象句式”，附公开来源及定位。使用反馈可提供已获授权、适合公开的段落和具体修改建议。

如果它让你少卡住一个段落，欢迎点个 **Star**，也欢迎把它分享给一起写论文的同学。

## License & attribution

本项目原创的指令、模板、分析和文档采用 [MIT License](LICENSE)。第三方材料按各自许可证及权利归属使用，详见[第三方来源说明](THIRD_PARTY_NOTICES.md)。

论文资料以来源链接、版本信息、写作卡和功能定位的形式提供。

## English

**An evidence-linked writing skill for AI and AI + graphics research papers.**

Plan, draft, revise, and check manuscripts with 7 section files, 74 fillable paragraph modules, and 289 sentence-function slots. A claim–challenge–design–evidence workflow keeps the manuscript's argument connected. The expression library distinguishes observations, hypotheses, empirical findings, and theoretical guarantees.

The source collection contains 36 paper cards, with 24 papers supporting 105 rhetorical evidence records. Fillable templates organize the writing functions observed in these papers; sentence structure and paragraph length adapt to your contribution. Each resource records its source and reading scope. Instructions are primarily in Chinese; fillable prose is in English.

Clone this repository into your Codex skills directory and invoke `$ai-graphics-paper-writing`, or read the Markdown resources directly. Supply your research notes, method details, results, and references to turn the templates into concrete prose. Check the draft against your evidence and target venue requirements. MIT-licensed original materials; third-party rights are reserved.
