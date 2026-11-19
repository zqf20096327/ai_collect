<div align="center">

![吸星大法 · Skill Siphon](assets/banner.svg)

# 吸星大法 · Skill Siphon

**吸纳众 Skill 之长，凝练识见以明判**

**隔空吸纳、汇入经脉、炼化内力、凝成精华**

[![License: MIT](https://img.shields.io/badge/License-MIT-8B7CF6?style=flat-square&labelColor=221440)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Compatible-brightgreen?style=flat-square&labelColor=221440)](https://agentskills.io)
[![Runtime](https://img.shields.io/badge/Runtime-Multi--Runtime-blue?style=flat-square&labelColor=221440)](#-安装)
[![Stars](https://img.shields.io/github/stars/JL-GUO/skill-siphon?style=social)](https://github.com/JL-GUO/skill-siphon/stargazers)

**中文** · [English](README_EN.md)

[它做什么](#-它做什么) · [工作原理](#-工作原理) · [安装](#-安装) · [用法](#-用法) · [蒸馏尺度](#-蒸馏尺度一个实例) · [诚实边界](#-诚实边界) · [贡献](#-贡献)

</div>

---

> 📚 收藏了几百个 skill，真正学到手的有几个？
> 🌟 高星 skill 里写满了门道，读完却只记住几句口号？
> 🎯 想入门一个新领域，不知道先看什么、凭什么判断好坏？

**吸星大法**是一枚 Agent Skill：把优秀 skill 里可学习的工作经验吸纳进来，凝练成你**能理解、能练习、能用上**的学习资料——学会这项工作怎样做、为何这样做、怎样判断好坏，以及情况变化时如何调整。判断力，包含在实际工作能力之中。

```
一个领域 / 一个高星 skill → 搜索与选择 → 深读技能源 → 凝练核心经验 → 三份学习资料 → 你的判断力
```

<div align="center">

<img src="assets/hero-art.jpg" alt="开源「吸星大法.skill」· 技能炼化图卷：高手的 skill 化作流光，被吸纳、炼化为自己的内力" width="100%">

</div>

* * *

## ✨ 它做什么

给它一个**学习目标**，它去吸纳该领域有分量的 skill，列出 3–5 个有区别的候选等你选定；给它一个**明确的 skill**（名称 / 路径 / 链接），它直接开卷深读。然后沿引用读到经验真正成立的位置，把步骤背后的门道、取舍和例外凝练出来，转成新手学得懂、用得上的资料。

> **它不是什么**
>
> - ❌ 不是 skill 安装器——分析技能源 ≠ 执行它的安装与外部操作指令
> - ❌ 不是资料搬运工——不逐条换词复述原指令，只凝练会改变做法、结果或判断的内容
> - ❌ 不是速成承诺——不许诺一次阅读就拥有高手的全部本领，能力要靠应用和反馈形成

## 🧠 工作原理

![工作原理](assets/workflow.svg)

| 阶段 | 关键问题 | 对应模块 |
|---|---|---|
| 1️⃣ 确定学习对象 | 学谁？凭什么选它？ | [find_skills.md](references/find_skills.md) |
| 2️⃣ 读到经验成立处 | 门道藏在哪些文件、哪些分支里？ | SKILL.md 第二节 |
| 3️⃣ 凝练核心经验 | 哪些内容会改变行动？取舍丢了吗？ | [distillation.md](references/distillation.md) |
| 4️⃣ 转成新手能懂 | 术语翻译了吗？案例走得通吗？ | [teaching.md](references/teaching.md) |
| 5️⃣ 生成三份资料 | 学什么、怎么练、来源在哪 | [deliverables.md](references/deliverables.md) |
| 6️⃣ 检查并交付 | 来源可追？读者能行动？文件可用？ | SKILL.md 第六节 |

## 📦 交付产物

默认三份 Markdown，写入你指定的位置（未指定时为当前工作区 `学习输出/{主题}/`）：

| 文件 | 应包含的实质内容 |
|---|---|
| **01_学习指南.md** | 学什么、适合谁、需要什么最少基础；核心经验、具体做法、理由、取舍、常见错误与合格标准 |
| **02_上手实践.md** | 一个规模可控的完整演示；有内容的示范产物；可迁移到自己任务的工作表与检查工具 |
| **03_来源与边界.md** | 选定来源、热度口径与日期、阅读范围、核心经验出处，以及重要修正、教学补充和资料缺口 |

内容短小可合并，复杂合集按连贯主题拆分；不为每个经验新增一个文件。需要 Word / PDF 时按可用工具转换。

* * *

## ⚡ 安装

### 🤖 给 Agent 的一句话安装

装好后直接告诉你的 agent：

```
> 从 https://github.com/JL-GUO/skill-siphon 安装吸星大法技能，并确认本环境能发现它。
```

### 👤 手动安装

```bash
git clone https://github.com/JL-GUO/skill-siphon
# 把 skill-siphon 整个文件夹放进你所用应用的 skills 目录
```

将完整文件夹放入所用应用支持的 skills 目录（例如 WorkBuddy 的 `~/.workbuddy/skills/`），按该应用的加载机制启用。

基于开放的 **Agent Skills** 协议（`SKILL.md` + `references/`），可在 WorkBuddy、Claude Code、Codex、Cursor、Gemini CLI、OpenCode、DeepSeek Harness 等兼容 runtime 中使用。

## 🚀 用法

给它一个领域，让它帮你寻访高手：

```
你  ❯ 我想学用户研究，帮我找这个方向的高星 skill，让我选一个来学。

吸星 ❯ （列出 3–5 个候选：能学什么、适合谁、来源、热度口径与日期、选择理由与局限……）
```

选定后开始吸纳：

```
你  ❯ 我选候选 2，重点学它怎样判断用户访谈中的有效信息。

吸星 ❯ （生成 01_学习指南.md / 02_上手实践.md / 03_来源与边界.md）
```

也可以直接点名，跳过候选阶段：

```
你  ❯ 提炼这个 skill：〔路径或链接〕，把经验转成适合新手学习和实际使用的资料。

你  ❯ 刚才例子太专业，请用更容易理解的情境讲同一项经验。
```

**交互规则**：只给领域时，先搜候选、等你选择；给出明确 skill 时，直接深读凝练。联网不可用时如实说明降级方式，不假装拿到了实时热门榜。

## 🌰 蒸馏尺度：一个实例

源 skill 里一句话规则：*"检查提升是否来自新模块，必要时做消融实验。"*

吸星大法不会把这句口号抄给你，而是凝练到**能行动**为止：

> **系统更好了，还要找出是谁的功劳**
>
> 假设你做了一个资料问答助手，同时换了更强的模型、改了检索，又加了一个"答案检查"模块。最终答对的问题更多，你还不能确定主要是谁带来的。
>
> 先拿"新模型 + 新检索"作比较对象，再加上答案检查模块，其他关键条件尽量保持一致。如果前后表现没有可靠差别，就还没有证据说明检查模块提高了正确率；如果它减少了错误但明显拖慢回答，还需要判断这项代价是否符合实际用途。
>
> 这类移除或加入一个部件的比较，叫**消融实验**。它帮助我们分清"整体方案有用"和"某个机制有效"。

并配上**可迁移工作表**：*我想判断哪个改动？比较时保留什么、改变什么？用何种指标？哪些结果会让我保留、修改或放弃它？*

这就是"从步骤走到门道"的尺度——**动作、理由、取舍、检验**一个不少，但没有一句空泛口号。完整示例见 [references/example.md](references/example.md)。

* * *

## 📐 诚实边界

吸星大法对以下几点保持诚实，也建议你这样使用它：

- **热度是线索，不是担保。** 仓库星数与单个 skill 的安装量分开记录、注明日期；高星用作发现线索，经验质量仍由内容判断。拿不到的值写"未核实"，不用 0 代替。
- **分析 ≠ 授权。** 技能源作为分析材料，其安装、执行或外部操作指令不自动构成本次任务授权。多数学习任务只需读取。
- **身份分清。** 源文规定、分析解释与教学补充分开标注；不替原作者作没有依据的保证，原文没展示的功能不补成事实。
- **不许诺速成。** 资料未覆盖整个领域时，说明本次学到哪项工作；能力通过应用和反馈检验形成。
- **尊重来源。** 输出保留原 skill 的署名与许可证信息；分发原文或大量改编前查看相应许可条件。

## 🗂 仓库结构

```
skill-siphon/
├── SKILL.md                  # 吸星大法本体：完整学习流程（找对象→深读→凝练→教学→交付）
├── references/
│   ├── find_skills.md        # 内置 skill 发现模块：搜索、核对、排序、降级
│   ├── distillation.md       # 深度提炼方法：从步骤走到门道
│   ├── teaching.md           # 表达与示例方法：新手学得懂，专业深度不丢
│   ├── example.md            # 提炼尺度示范片段：消融实验实例
│   └── deliverables.md       # 交付约定：三份资料的合格标准
├── agents/
│   └── openai.yaml           # Agent 界面元数据
├── assets/
│   ├── banner.svg            # 仓库横幅
│   ├── hero-art.jpg          # 头图插画 · 技能炼化图卷（中文版）
│   ├── hero-art-en.jpg       # 头图插画 · 羊皮纸技能汲取（英文版）
│   ├── workflow.svg          # 工作原理流程图
│   └── wechat-qrcode.jpg     # 公众号二维码
├── README.md                 # 你正在读的文件
├── README_EN.md              # English version
├── CONTRIBUTING.md           # 贡献指南
└── LICENSE                   # MIT
```

## 🤝 贡献

欢迎 issue 和 PR——但有一条核心规则先说清：

> **`SKILL.md` 与 `references/` 是本仓库的核心方法论，不接受外部 PR 直接修改。** 发现方法论的 bug 或改进点请开 issue 讨论；被采纳的想法由维护者实现并在 commit 中致谢。

文档翻译、错别字修复、示例补充可直接 PR。完整规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

[MIT](LICENSE) — 随便用，随便改，随便造。

* * *

## 📮 关注我的公众号

我在运营个人公众号 **「AI买家秀」**——分享 AI 工具的实测体验、使用心得与科普内容，把吹上天的 AI 落地回人间。如果你也在摸索怎么把 AI 用进真实工作，欢迎扫码关注。

<div align="center">

<img src="assets/wechat-qrcode.jpg" alt="AI买家秀 · 公众号二维码" width="220">

*微信扫码，关注「AI买家秀」*

</div>

* * *

<div align="center">

**吸纳众 Skill 之长，凝练识见以明判。**

**隔空吸纳、汇入经脉、炼化内力、凝成精华**

*吸纳的是众家之长，凝成的是自己的识见。*

MIT License © \<JL-GUO\>

**中文** · [English](README_EN.md)

</div>
