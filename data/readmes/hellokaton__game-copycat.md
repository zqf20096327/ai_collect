<div align="center">

# 🐾 game-copycat

**看见一款游戏，交付一款游戏。**

一个复刻小游戏的 Agent Skill：给它一个名字、一条推文或一张截图，它还你一款精致、完全原创的 web 小游戏。不是 demo，是成品。支持 Claude Code、Codex、Cursor 及一切认 `SKILL.md` 的 agent。

[简体中文](README.md) · [English](README.en.md)

![License](https://img.shields.io/badge/license-MIT-teal) ![Agent Skill](https://img.shields.io/badge/Agent-skill-8A2BE2) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

<img src="docs/pourlab-board.png" width="31%" alt="PourLab 倒倒乐" /> <img src="docs/sweetpop-board.png" width="31%" alt="SweetPop 甜甜消" /> <img src="docs/pourlab-win.png" width="31%" alt="PourLab 通关" />

*两款示例游戏，各由一句 prompt 端到端产出，源码就在本仓库*

</div>

---

## 这是什么？

你一定刷到过这种帖子：*"我用 AI 一个晚上复刻了一款爆火小游戏。"* game-copycat 就是把那个晚上打包成可复用的 [Agent Skill](https://agentskills.io)——并补上了从"勉强能玩"到"真的有人玩"之间缺的那些工程纪律。

对你的 agent 说一句：

```
复刻 Water Sort
```

……它会跑完整条流水线：调研原作规则 → 和你确认范围 → 搭脚手架 → 构建**可证明正确的游戏内核** → 做原创品牌的精致 UI 和真实手感 → **在真实浏览器里亲手玩通一局**来验收 →（可选）部署到 Cloudflare Workers。

## 快速开始

对你的 agent 说一句：

```
帮我安装 hellokaton/game-copycat 这个 skill
```

就装好了。想自己动手也行：

```bash
npx skills add hellokaton/game-copycat
```

**依赖**：任意支持 skills 的 agent、Node 18+。可选：[wrangler](https://developers.cloudflare.com/workers/wrangler/)（部署用）、[agent-browser](https://www.npmjs.com/package/agent-browser)（浏览器自验用）。

然后直接说：

```
复刻 2048
做一个像 NYT Connections 的游戏
Clone LinkedIn Queens
[贴一张截图] 能做一个这个吗？
```

## 案例一：PourLab 倒倒乐

从一句 *"复刻 Water Sort"* 开始产出的倒水排序解压谜题：

| 试管棋盘 | 通关结算 | 移动端（9 色每日挑战） |
|:---:|:---:|:---:|
| ![board](docs/pourlab-board.png) | ![win](docs/pourlab-win.png) | ![mobile](docs/pourlab-mobile.png) |

- **60 关（3 色 → 9 色），每关都经求解器验证可解、解长达标才收录**——DFS + 状态规范化记忆求解器给发牌生成器把关
- **提示不是看广告，是内置求解器实时算出的下一步**；结算页展示"你的步数 vs 求解器参考步数"
- 每日挑战、连胜、最佳步数、死局检测横幅、集满一管小庆祝 + 通关彩带
- 中英双语、合成音效、触觉反馈、`prefers-reduced-motion` 全覆盖

源码在 [`examples/pourlab/`](examples/pourlab/)。运行：`cd examples/pourlab && npm install && npm run dev`。

## 案例二：SweetPop 甜甜消

从一句 *"复刻消消乐"* 开始产出的经典三消：

| 糖果棋盘 | 目标达成 | 移动端 |
|:---:|:---:|:---:|
| ![board](docs/sweetpop-board.png) | ![win](docs/sweetpop-win.png) | ![mobile](docs/sweetpop-mobile.png) |

- **每关的目标分由贪心机器人构建期实跑同一副牌标定（取其得分 70%）——"可过关"不是拍脑袋，是机器打出来的**
- 完整三消内核：交换回弹不计步、重力下落补块、连锁逐层翻倍、死局自动洗牌，全部有属性测试把关
- 步数限制 + 三星评级 + 每日挑战 + 连胜；提示按钮 = 机器人视角的最优交换

源码在 [`examples/sweetpop/`](examples/sweetpop/)。运行：`cd examples/sweetpop && npm install && npm run dev`。

## 工作原理

八个阶段，每个阶段有硬性出口门禁——门禁不绿，skill 拒绝进入下一步：

| 阶段 | 做什么 | 门禁 |
|---|---|---|
| ① 调研 | 抓取原作规则与参考截图，写成规则说明书 | 说明书完整 + 参考截图落盘 |
| ② 确认 | 一段话汇报：目标游戏、原创名提案、验收标准 | 规则零歧义 |
| ③ 脚手架 | `new-game.mjs` 复制久经实测的 Vite + React + TS 模板 | 空壳通过 `npm run check` |
| ④ 内核先行 | 纯函数内核、种子随机、唯一解求解器、构建期固化关卡、属性测试 | 全部关卡可证明正确，内核零 DOM |
| ⑤ UI + 手感 | 从参考图提取设计令牌（原创配色/品牌）、多主题可切换、FLIP 动画、完整手感清单 | 布局对应参考、品牌完全原创 |
| ⑥ 自验审计 | agent 真实玩到赢也玩到输，移动端自适应与 UI/UX 全清单审计，控制台干净 | 审计四组全绿 |
| ⑦ 部署（可选） | `wrangler deploy` 上 workers.dev——**先和你确认目标账号** | 线上 URL 可玩 |
| ⑧ 交付 | README 带出处声明与差异清单，实证式汇报 | 你点开就能玩 |

模板预置了枯燥但致命的部分：种子化 PRNG、版本化 localStorage、Web Audio 合成音效、带 reduced-motion 门禁的彩带/触感封装、emoji 分享、中英 i18n。创造性的部分——内核与 UI——每款游戏现写，由四篇从真实复刻实战中提炼的参考文档引导。

## 仓库结构

```
skills/game-copycat/
├── SKILL.md                 # 八阶段流水线与出口门禁
├── references/
│   ├── research.md          # 从链接/截图/名字提取规则的方法
│   ├── engineering.md       # 内核分层、求解器、关卡固化、属性测试
│   ├── juice.md             # demo→成品的手感清单
│   └── deploy.md            # Cloudflare Workers 静态资产部署与护栏
├── scripts/new-game.mjs     # 模板 → 安装 → 自检，一条命令
└── assets/template/         # 可跑的 Vite+React+TS 空壳，枯燥部分已就绪
examples/                    # skill 产出的游戏，作为活的证据
```

## 关于版权

游戏*机制*不受版权保护，游戏*表达*受。game-copycat 默认执行这条边界：

- 机制忠实复刻；**名称、品牌、美术、配色、关卡数据与代码永远原创**
- 原作截图只作本地对照参考，绝不进入产物或仓库
- 每款生成的游戏 README 都注明灵感来源并列出已知差异

不要用它把别人游戏的 1:1 复制品当作自己的作品发布。用它做致敬、原型和"机制熟悉但表达全新"的原创。

## FAQ

**哪类游戏效果最好？** 益智休闲：网格逻辑（Queens、Zip、数织、数独变体）、文字（Wordle、Connections）、合成（2048）、消除、纸牌。DOM + CSS 能做精致的都行。3D / 实时对战 / 重物理不在范围内——skill 会直说，而不是硬做。

**必须部署吗？** 不。部署是可选项，且 skill 会先和你确认 Cloudflare 账号。默认交付本地 `npm run dev`。

**"可证明正确的内核"是什么意思？** 谜题游戏的生死在关卡质量。game-copycat 先写求解器再写生成器，任何不达标的关卡（解不唯一、不可解）直接拒收——而且这个校验每次构建都会跑。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hellokaton/game-copycat&type=Date)](https://star-history.com/#hellokaton/game-copycat&Date)

## 许可

MIT。如果它帮你交付了一款游戏，点个 ⭐、发帖晒出你的作品，就是最好的感谢。
