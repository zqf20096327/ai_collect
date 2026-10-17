# Camelot.skill

**简体中文** | [English](README.en.md)

<div align="center">
  <img src="https://img.shields.io/github/stars/barinfo/Camelot.skill?style=social&label=Stars" alt="GitHub Stars" />
  <img src="https://img.shields.io/github/forks/barinfo/Camelot.skill?style=social&label=Forks" alt="GitHub Forks" />
  <img src="https://img.shields.io/github/watchers/barinfo/Camelot.skill?style=social&label=Watchers" alt="GitHub Watchers" />
  <img src="https://img.shields.io/github/license/barinfo/Camelot.skill?color=blue" alt="License: MIT" />
  <img src="https://img.shields.io/github/repo-size/barinfo/Camelot.skill" alt="Repo Size" />
  <img src="https://img.shields.io/github/commit-activity/m/barinfo/Camelot.skill?color=green" alt="Commit Activity" />
</div>

<p align="center">
  <img src="assets/camelot.png" alt="Camelot.skill — 圣剑 logo (original by Barinfo)" width="220" />
</p>

<div align="center" style="background-color: #1a1a2e; color: #eaeaea; border-radius: 12px; padding: 24px 16px; border: 1px solid #3a3a5e;">

# ⚔️ 圣剑的裁决！

**Pull the Sword — or pull your request.**

*The Sword of Judgment renders its verdict — code either proves itself worthy, or it does not.*

</div>

> 🏰 **认名不认亲声明**：本仓库的 Camelot 指的是亚瑟王的卡美洛宫——圆桌、石中剑、卡姆兰战役，跟 Python 圈那位 [提取 PDF 表格的 Camelot](https://github.com/camelot-dev/camelot) **没有丁点关系**。它读 PDF，我们审代码，各过各的桥，互不打扰。

> **⚔️ 亚瑟王审判之声的无慈悲代码审查。**
> 代码要么证明自己配得上——如同从石中拔出圣剑——要么被不带任何感情地拒绝。

面向 LLM agent 的专家级、以证据为锚的代码审查技能（Skill）。Camelot 按价值而非地位裁决代码：违规被分级为 **Exile（放逐）/ Dishonor（失荣）/ Counsel（谏言）**，真实亮点被授予 **Valour（勇武）**，每次审查都以 **Camlann 的裁决**收尾——具体、可执行的下一轮指令。

| | |
|---|---|
| 📄 格式 | Markdown 技能（frontmatter `SKILL.md`）+ `skill.json` 元数据 |
| 🧩 兼容 | Claude Code / Codex / DSH presets / 任何能加载 Markdown 技能的 agent |
| 🌏 语言 | 简体中文（README 默认）· 审查输出英文为主，可本地化 |
| ⚖️ 许可 | MIT |

---

## 为什么是 Camelot？

大多数"审查我的代码"式 AI 输出，要么是**披着批评外衣的奉承**，要么是**没有行号、含糊其辞的否定**。Camelot 立下不同的誓言：

- **无慈悲，但要有证据。** 每条发现都必须带 `文件:行号` 位置。没有位置的发现只是道听途说——不配被写下来。
- **最重的裁决针对根本性错误，而非普通 bug。** 过度工程、死代码、背叛自身宣称的架构——这些才配得到最多的笔墨，而不是那个 off-by-one。
- **真诚地表扬配得上的人。** 只谴责的审查没有可信度——所以真实优点会被记为 Valour，并附上证据。
- **先验证，再裁决。** Camelot 读代码、看 `git status`、检查构建产物与日志。它不信任提交信息或 agent 的摘要。
- **每次裁决都以指令收尾。** 不是"提高质量"——而是 *"接上方法 X → 跑测试 Y → 重跑实验；验收标准 = 这行日志"*。

## 十项试炼

Camelot 让代码通过**十项试炼**，每项只报告最有杀伤力的 1–3 条发现：

1. 构建与打包（零测试 = Exile）
2. 中央抽象是否在每一个调用点都被忠实执行？
3. 缓存与状态设计（miss 与 error 是否可区分、TTL、持久化、键归一化）
4. 错误处理惯例与静默失败
5. 字符串与国际化
6. 并发
7. 边界与硬编码
8. 可维护性
9. 运维（日志、配置）
10. 安全（涉及输入/网络时）

外加一道针对**进行中的产出 / agent 输出**的专项审查："差一步就完成"的缺口、打地鼠检测（→ *请教 Merlin：去读依赖源码*）、静默失败、与计划的漂移。

## 分级纹章

| 严重级 | 含义 | 裁决用语 |
|---|---|---|
| 🔴 **Exile（放逐）** | 不得通过审查——安全漏洞、静默失败、背叛自身宣称的架构 | *"Mordred 行走于城墙之内。"* |
| 🟡 **Dishonor（失荣）** | 合并前应当修复 | *"代码能编译；但它尚不配。"* |
| 🔵 **Counsel（谏言）** | 建议、打磨 | *"Merlin 献上智慧。"* |
| 🏆 **Valour（勇武）** | 有证据的真实优点 | *"此举拔出了圣剑。"* |

## 快速开始

**作为 Skill 安装**

```bash
# Claude Code
cp SKILL.md ~/.claude/skills/camelot/SKILL.md

# DSH 自定义 preset（把 <id> 换成你的 preset 名）
cp SKILL.md ~/.dsh/.agent-presets/<id>/skills/camelot/SKILL.md

# Codex / 其他：按其 skill 目录约定放置
```

**或作为提示词使用** —— 把 `SKILL.md` 全文粘进对话，然后说：

> Review this codebase/PR. No mercy.

**可重复、可接递归** —— Camelot 自己不跑循环、不设定时器。它是一个**无状态的单次裁决器**：想调用多少次都行，每次把*某一轮的改动文件*递给它，它审完返回一份裁决。若要循环驱动——长期目标、子代理分工、定时自醒、一轮轮把 Camelot 喂下去——交给 **Ouroboros**，它负责一直把下一个 diff 交给 Camelot。

## 推荐搭配：Ouroboros.skill

> **Camelot 裁决某一轮代码；[Ouroboros.skill](https://github.com/Barinfo/Ouroboros.skill)（衔尾蛇）驱动递归——它托住长期目标、把子任务拆给 sub-agent（需要代码裁决时派一个跑 Camelot 并把裁决接回）、并架设定时器让 agent 停了会自己醒。一个干净的裁判 + 一个不知疲惫的驱动，配合使用。**

Camelot 是**裁判**：给它任意 repo / PR / 某一轮改动，它返回 Exile/Dishonor/Counsel/Valour 裁决；它自己不跑循环。Ouroboros 是**驱动**：它决定这项任务要不要继续跑、让目标常存，并且在某轮代码需要裁决时——派一个运行 Camelot 的子代理，把返回的裁决接回后进入下一轮。

| | Camelot.skill | Ouroboros.skill |
|---|---|---|
| 角色 | 裁判（judge） | 驱动（driver） |
| 做什么 | 裁决一轮代码/ repo / PR | 驱动多轮递归：长期目标 + sub-agent + 定时自醒 |
| 自跑循环？ | 无——单次、无状态、可被反复调用 | 有——持目标、派子代理、到点叫醒自己 |
| 代码裁决 | 亲自做 | 委派：派 Camelot 子代理审，接回结果 |

**配起来用**：Camelot 定"这轮代码行不行"；Ouroboros 定"任务要不要继续跑 / 何时把下一轮交给 Camelot / 停了谁来叫醒"。两个都装：一个给判断、一个给持续。

## 推荐搭配：pre-delivery-selfcheck

> **Camelot 裁决你的*代码*是否配得上 Avalon；[pre-delivery-selfcheck](https://github.com/Chen-Clark/pre-delivery-selfcheck) 裁决你的*交付*是否配得上被发出。** 两者一起用。

Camelot 审查代码库，但它不管自己的裁决——或任何 agent 回复——是如何递交的。这正是 **[pre-delivery-selfcheck](https://github.com/Chen-Clark/pre-delivery-selfcheck)**（本地安装名为 `delivery-no-pseudoblock` 技能，闸门 **D1–D12**）要填补的缺口：在向用户交付*任何*结果之前（最终总结、结论、状态汇报，甚至一个问题），它必须被真正加载并跑过**整条消息（含结尾尾巴）**，拦截：

- **责任转嫁**（向用户索要 agent 本可自行取得的信息），
- **半途交付**（只诊断未修复，却当作"已完成"交付），
- **隐藏最优步**（把最好的下一步包装成"如果你想要，我可以…"），
- **伪阻断提问**（以 agent 自己能回答的问题收尾），
- **尾巴豁免**（宣称"闸门已过"，收尾句却把延后事项偷渡过去），
- 以及用一句声明替代真实检查的"先盖章后干活"模式。

为何搭配效果佳：

| | Camelot.skill | pre-delivery-selfcheck |
|---|---|---|
| 裁决对象 | 被审查的**代码 / PR** | **agent 自身的交付行为** |
| 裁决形态 | Camlann 裁决：🔴 Exile / 🟡 Dishonor / 🔵 Counsel / 🏆 Valour | D1–D12 闸门快照，全闸通过才算过 |
| 拦下的失败 | 不配的代码通过了审查 | 不配的*回复*到达了用户 |
| 最佳配合 | Camelot 决定*什么*必须重铸 | 交付闸门确保裁决被如实送达，尾巴不藏延后 |

**建议工作流** —— 在同一 agent 会话中同时安装两个技能。先跑 Camelot 审查，发出前再对审查消息本身跑一遍 `delivery-no-pseudoblock`。一份以*"把你的路径告诉我，我来修"*结尾的无慈悲审查，就是一份违背了自身誓言的审查——配套闸门正是为拦截这种情况而存在。

## 示例输出

一份完整的模拟 PR 审查（Camlann 裁决、分级发现、指令）见 [`examples/mock-pr-review.md`](examples/mock-pr-review.md)。

## 仓库结构

```
Camelot.skill/
├── README.md                    # 本文件（简体中文，默认）
├── README.en.md                 # English version
├── skill.json                   # 包元数据（name、triggers、author、license）
├── SKILL.md                     # 技能本体——复制此文件即完成安装
├── docs/
│   └── ARTHURIAN_VOICE.md       # 语气与隐喻扩展指南
├── examples/
│   └── mock-pr-review.md        # 裁决输出示例
├── assets/
│   └── camelot.png              # 圣剑 logo（Barinfo 原创）
├── LICENSE                      # MIT
└── .gitignore / .gitattributes
```

## 优点（为什么值得放进你的工具箱）

1. **天然以证据为锚** —— "无位置不写"规则与反幻觉誓言让审查可被审计，而非凭感觉。
2. **分级纪律** —— Exile/Dishonor/Counsel 强制排序；"每项试炼只写 1–3 条致命发现"让报告短到有人愿意读完。
3. **根本问题优先于表面问题** —— 它猎杀架构对自身宣称的背叛——那才是真正毁掉项目的东西——而不是逐行的吹毛求疵。
4. **无状态、可反复调用** —— 不自跑循环、不定时器；给它某一轮代码它就裁那一轮，多少次都行。多轮递归交给 Ouroboros，由它一轮轮把下一个 diff 喂给 Camelot。
5. **验证优先的姿态** —— 它拒绝相信声称，这正是评估另一个 agent 的"已完成"时你想要的。
6. **零依赖** —— 一个 Markdown 文件；无运行时、无 API、无安装。
7. **诚实的表扬** —— Valour 章节让批评保持可信。

## 诚实的局限（镜子也照我们自己）

1. **语气是把双刃剑。** 想要温和反馈的用户，或正在评估自己第一个项目的人，可能会觉得亚瑟王式的无慈悲腔调充满敌意。这些场景请用更柔和的技能——或剥掉风味、只留纪律。
2. **它要求素材。** 出色的审查需要代码、git 历史、日志。凭记忆或模糊描述"审查"只会产出空洞的报告——Camelot 会直说，而不是假装。
3. **按誓言只读。** 它不会修代码、跑测试或写补丁。它告诉你*确切*要做什么；活仍得你干。
4. **严重级取决于执行模型。** 弱模型可能产出戏剧化但浅薄的裁决。反幻觉誓言是刹车；高利害场景请人工复核审查本身。
5. **审查不是安全审计。** Trial X 覆盖常见的输入/网络问题，但 Camelot 不能替代真正的安全审查或工具（SAST/DAST）。
6. **审查输出以英文为主。** 设计如此；若你的团队用其他语言，请自行本地化审查输出。

## 什么时候别用它

- 你想要鼓励而非裁决 → 用一个温暖/导师型技能。
- 你只有 30 秒问"这样看着行不行？" → Camelot 是全套试炼，杀鸡用牛刀。
- 你不能或不愿提供代码/git 访问 → 技能无法验证，裁决必然空洞。
- 今晚必须上线、你需要橡皮图章 → Camelot 不会给你。

## 设计渊源

Camelot 的纪律核心（事实基线 → 试炼维度 → 分级输出 → 下一轮指令 → 反幻觉誓言）是 **`code-review-no-mercy`** 纪律的主题化移植，换上了亚瑟王纹章，并扩展出一套让发现保持机器可读的隐喻词汇。

## 许可

[MIT](LICENSE)。Fork 它、改写它的声音、让它更温和或更严酷——圆桌会议按价值裁决，而价值包含再创作。

© 2026 FuCube

*摩艾石像-石中剑 由作者 Barinfo 原创绘制，可随本技能自由使用。*
