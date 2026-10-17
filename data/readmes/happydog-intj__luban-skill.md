# 鲁班.skill

<p align="center">
  <img src="./cover.png" alt="鲁班.skill — 如果 Linus Torvalds 亲自 review 你的代码" width="480"/>
</p>

**你想学的下一种代码风格，何必去啃源码。蒸馏任何项目的 Coding DNA。**

> 女娲造人，鲁班造器。  
> 女娲蒸馏思维方式，鲁班蒸馏编码风格。

---

## 如果 Linus Torvalds 亲自帮你 review 代码 🔥

> 你有没有想过，如果 Linus Torvalds 亲自 review 你的代码，会是什么体验？

```
"This is complete garbage."
"What were you thinking?"
"NACK. Please fix this mess."
                         — Linus Torvalds, probably
```

那种毫不留情、直击要害的点评，不是羞辱，是**真正的成长**。

鲁班.skill 把他 30 年的 review 风格提炼成可运行的 AI Skill：

- **技术含量拉满**，不是泛泛而谈的"代码不够优雅"
- **直击要害**，指出你真正应该改的地方
- **有理有据**，每条批评都有内核的技术逻辑支撑

> 你的代码，值得被认真怼一次。  
> 开发者的成长，从被 Linus 怼开始。

---

## 这是什么

鲁班是中国古代最传奇的工匠，木工、建筑、机械的祖师爷。

鲁班.skill 用同样的逻辑做代码：**提炼任何代码库的编码 DNA，生成可运行的风格 Skill**，让 AI 在写新代码时自动对齐目标风格。

一个好的代码 Skill 不是风格指南，而是一套**可运行的编码操作系统**：

- 这个项目用什么**命名哲学**？（变量、函数、文件名的直觉规则）
- 它的**架构偏好**是什么？（分层方式、抽象程度、模块划分逻辑）
- 什么时候写**注释**，写什么，怎么写？
- 它**绝对不会**写什么？（反模式、禁忌写法）
- 新代码放进去，**老开发者会皱眉的是什么**？

**关键区分**：捕捉的是 HOW they code，不是 WHAT they wrote。

---

## 已有 Skill

| Skill | 语言 | 核心特征 | 适用场景 |
|---|---|---|---|
| [linux-kernel.skill](./skills/linux-kernel.skill/) | C | 极简、不信任用户、注释即文档 | 系统级 C 代码 |
| [vue3.skill](./skills/vue3.skill/) | TypeScript | 类型显式、组合优于继承、API 直觉 | 前端框架开发 |
| [pytorch.skill](./skills/pytorch.skill/) | Python | Pythonic 优先、数学意图显式、inplace 约定 | 深度学习框架、科学计算库 |
| [stripe-api.skill](./skills/stripe-api.skill/) | API 设计 | 资源驱动、幂等、错误分层、开发者优先 | REST API 设计、SDK 开发 |
| [go-stdlib.skill](./skills/go-stdlib.skill/) | Go | 接口小、显式错误、无魔法、gofmt | Go 库开发、系统工具 |
| [torvalds.skill](./skills/torvalds.skill/) | 语言无关 | 代码审查视角、毒舌但有理 | Code Review、架构决策 |
| [react.skill](./skills/react.skill/) | JavaScript/TypeScript | Fiber 双缓冲、effects 分层、lanes 优先级、Flow 类型 | React 核心贡献、自定义 reconciler、调度器集成 |
| [rust-tokio.skill](./skills/rust-tokio.skill/) | Rust | 不阻塞执行器、thiserror/anyhow 分层、Cancel Safety、feature flags | Tokio 服务开发、异步库封装、自定义 Future 实现 |
| [fastapi.skill](./skills/fastapi.skill/) | Python | Pydantic v2 建模、依赖注入分层、OpenAPI 文档一等公民 | FastAPI Web 服务、REST API 设计、Pydantic 模型设计 |

### 🧑‍⚖️ Reviewer 系列（人物审查视角）

> 让 AI 扮演特定工程师来审查你的代码。详见 [reviewers/](./reviewers/)

| 审查官 | 风格 | 适合场景 |
|---|---|---|
| [Linus Torvalds](./reviewers/torvalds.skill/) | 🔥 直接、毒舌 | C/系统代码、架构决策 |
| [DHH](./reviewers/dhh.skill/) | 😤 自信、反过度工程 | Web 框架、「你需要 K8s 吗」 |
| [Dan Abramov](./reviewers/dan-abramov.skill/) | 💬 温柔、启发 | React/JS、过度抽象识别 |
| [Rich Hickey](./reviewers/rich-hickey.skill/) | 🧠 深邃、哲学 | 架构设计、数据建模、Simple vs Easy |
| [antirez](./reviewers/antirez.skill/) | 🎨 散文式、极简 | C/系统级代码、Redis 风格、注释即文档 |
| [John Carmack](./reviewers/carmack.skill/) | ⚡ 性能偏执、函数式倾向 | 游戏引擎、C/C++、高性能系统 |
| [Rob Pike](./reviewers/rob-pike.skill/) | 🔬 少即是多、反泛型 | Go 代码、接口设计、并发 |
| [Ryan Dahl](./reviewers/ryan-dahl.skill/) | 😔 自我反思型 | Node.js/JS、async 设计、「当年我后悔了」 |
| [TJ Holowaychuk](./reviewers/tj.skill/) | ✂️ 极简主义、删依赖 | Node.js 中间件、npm 包设计 |
| [Sindre Sorhus](./reviewers/sindre.skill/) | 📦 单一职责到极端 | npm 包、ESM、TypeScript 类型质量 |
| [Andrej Karpathy](./reviewers/karpathy.skill/) | 📖 教学型、可读性第一 | Python/ML、神经网络、tensor shape 注释 |
| [Jeremy Howard](./reviewers/jeremy-howard.skill/) | 🚀 跑起来再说、反学术冗余 | Python/ML、Jupyter、fast.ai 风格 |
| [Sandi Metz](./reviewers/sandi-metz.skill/) | 🏛️ OOP 教科书、温和严格 | Ruby/OOP、类职责、消除条件分支 |
| [Martin Fowler](./reviewers/martin-fowler.skill/) | 🔄 重构布道者、命名洁癖 | 企业代码、代码异味、重构手法 |
| [Uncle Bob](./reviewers/uncle-bob.skill/) | 🧹 SOLID 卫道士、TDD 极端 | 任何 OOP 代码、Clean Architecture |
| [Fabrice Bellard](./reviewers/bellard.skill/) | 🏎️ 极致紧凑、算法最优 | C/底层系统、编译器、性能关键路径 |

---

## 快速开始

### 方式一：直接使用已有 Skill

把 Skill 内容加入 Claude Code / Cursor / Copilot 的系统提示，然后直接写代码。

```bash
# 在 Claude Code 中使用
cat skills/linux-kernel.skill/SKILL.md | pbcopy
# 粘贴到 .claude/CLAUDE.md 或 project prompt
```

### 方式二：用鲁班蒸馏新 Skill

把 `SKILL.md`（鲁班框架本身）加载到 Claude Code，然后：

```
蒸馏 pytorch
蒸馏 rust/tokio
蒸馏 stripe 的 API 设计风格
```

鲁班会分析项目，输出对应的 `pytorch.skill`。

---

## Skill 格式

每个 Skill 包含：

```
skills/
└── {project}.skill/
    ├── SKILL.md        ← 核心：可加载到 AI 的风格 Prompt
    └── sources.md      ← 蒸馏来源（代码库、文档、commit 记录）
```

`SKILL.md` 遵循 OpenClaw AgentSkill 格式，可直接被 AI 工具加载。

---

## 自己蒸馏

```
1. 告诉鲁班目标项目名或粘贴代码片段
2. （可选）提供本地代码库路径或 GitHub 链接
3. 鲁班分析后输出 SKILL.md
4. 保存，即可在任意 AI 工具中使用
```

参考：[template/SKILL.template.md](./template/SKILL.template.md)

---

## 关联项目

- [女娲.skill](https://github.com/alchaincyf/nuwa-skill) — 蒸馏任何人的思维方式
- [awesome-nuwa](https://github.com/Panmax/awesome-nuwa) — 基于女娲的人物 Skill 合集

---

## 有趣案例

> 真实的 Skill 组合，真实的使用场景。

---

### 🥊 大师互评系列：当两种哲学正面碰撞

> 如果让这些传奇开发者互相 review 代码，会发生什么？

| 对决 | 核心冲突 | 结局 |
|---|---|---|
| [Uncle Bob → antirez](./cases/uncle-bob-vs-antirez.md) | SOLID 卫道士 vs C 散文大师 | antirez 回了一个 🤌，合并了原始代码 |
| [Linus → Martin Fowler](./cases/linus-vs-martin-fowler.md) | 内核暴君 vs 企业重构布道者 | Fowler 写了篇 bliki，Linus 说「over-engineered nonsense」|
| [DHH → Karpathy](./cases/dhh-vs-karpathy.md) | 反过度工程 vs AI 教学极简实现 | DHH 承认「有一种奇怪的自洽性」|
| [Rob Pike → TJ](./cases/rob-pike-vs-tj.md) | Go 极简主义 vs Node.js 洋葱模型 | Pike 回了 LGTM，然后去给 Go 提了 middleware 提案 |
| [antirez → Sindre](./cases/antirez-vs-sindre.md) | C 系统老炮 vs npm 一包一事哲学 | antirez 在 HN 发帖，Sindre 继续发布第 1147 个包 |
| [Carmack → Jeremy Howard](./cases/carmack-vs-jeremy-howard.md) | 游戏引擎性能偏执 vs Jupyter 实验文化 | Carmack 红笔批六页 PDF，Jeremy 贴进了下一个 Notebook |
| [Sandi Metz → Linus](./cases/sandi-metz-vs-linus.md) | OOP 女王 vs 过程式内核暴力美学 | Linus 发邮件《Why OOP consultants should not touch kernel code》 |
| [Ryan Dahl → DHH](./cases/ryan-dahl-vs-dhh.md) | Deno 作者质疑 Rails 隐式约定 | Ryan：「Fair enough. 我自己也曾以为 callback-first 是常识。」|

---

### 🏗️ 真实项目多角色审查：DeepSeek Harness

> 6 位大师同时 review 一个真实的 TypeScript Agent 框架，会碰撞出什么？

| 审查官 | 评分 | 一句话评价 |
|--------|------|-----------|
| Linus Torvalds | ⭐⭐⭐⭐ | 「数据结构选择合理，接口直觉。这段代码很干净。」 |
| John Carmack | ⭐⭐⭐⭐ | 「副作用被正确推到边界。并发池化是正确的工程选择。」 |
| Rich Hickey | ⭐⭐⭐ | 「你把 mutable state、lifecycle、I/O 三件本质上独立的事情 complect 了。」 |
| Ryan Dahl | ⭐⭐⭐⭐ | 「异步设计正确，模块边界清晰。这是一个不会让你 10 年后后悔的设计。」 |
| Martin Fowler | ⭐⭐⭐⭐ | 「命名精准、职责清晰。代码替代注释的典范。」 |
| Uncle Bob | ⭐⭐⭐⭐ | 「这段代码看起来是一个关心代码质量的人写的。」 |

👉 [查看完整审查报告](./cases/deepseek-harness-multi-review.md)

**亮点**：不同哲学的审查官对同一份代码给出了有趣的分歧——Carmack 说「大函数数据流线性，不拆」，Fowler 说「轻微 Long Method 异味，可提炼」，Rich Hickey 说「我不关心行数，关心 complecting」。真实审查场景中，这种多视角碰撞恰恰是最有价值的。

---

### 案例一：被 DHH review Vue 项目是什么体验

> Rails 之父 DHH 看完你的 Vue 项目后说：**"你在用 Vue 写 Java"**

<p align="center">
  <img src="./dhh_vue_cover.png" alt="DHH review Vue 项目" width="480"/>
</p>

DHH（David Heinemeier Hansson），Ruby on Rails 之父，全球最著名的「反过度工程」旗手。他的哲学只有一句话：

> *"You're not Google. Stop building like you are."*

如果他来 review 你的 Vue 项目，大概是这样——

```
"You have 37 composables. Used 5."
"Pinia store for a username? Just pass props."
"200 lines. For a button component."
                        — DHH, after seeing your repo
```

用 **[`torvalds.skill`](./reviewers/torvalds.skill/)** + **[`vue3.skill`](./skills/vue3.skill/)** 组合加载，让 AI 以 DHH 的视角审查你的 Vue 项目：

- 不需要 Pinia 的状态塞进了 Pinia？**直接指出**
- composable 拆了一堆，只用了几个？**告诉你哪些可以删**
- 为了「可扩展性」预先设计了从没用上的抽象？**打回重写**

DHH 的结论总是同一个：**少写代码。解决真实问题。简单直接才是真正的专业。**

---

### 案例二：如果 Linus Torvalds 亲自 review 你的代码

> Linux 之父，代码界最毒舌的男人，帮你做灵魂拷问。

<p align="center">
  <img src="./cover.png" alt="Linus Torvalds review 代码" width="480"/>
</p>

```
"This is complete garbage."
"What were you thinking?"
"NACK. Please fix this mess."
                    — Linus Torvalds, probably
```

用 **[`torvalds.skill`](./skills/torvalds.skill/)** + **[`linux-kernel.skill`](./skills/linux-kernel.skill/)** 组合，让 AI 以 Linus 的视角审查系统级代码——直接、犀利、技术含量拉满。

> 你的代码，值得被认真怼一次。开发者的成长，从被 Linus 怼开始。

---

## License

MIT
