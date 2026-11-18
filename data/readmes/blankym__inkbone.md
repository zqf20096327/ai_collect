# InkBone（墨骨）

**给大模型配一本不会忘事的账本和一把改稿尺子，用来写中文长篇连载小说。**

[![test](https://github.com/blankym/inkbone/actions/workflows/test.yml/badge.svg)](https://github.com/blankym/inkbone/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Node.js ≥ 18](https://img.shields.io/badge/Node.js-%E2%89%A518-brightgreen.svg)](https://nodejs.org)
[![依赖: 0](https://img.shields.io/badge/%E4%BE%9D%E8%B5%96-0-orange.svg)](package.json)
[![版本: 1.2](https://img.shields.io/badge/%E7%89%88%E6%9C%AC-1.2-lightgrey.svg)](package.json)

[English](README.en.md) · **[在线试跑（纯浏览器本地运算）](https://blankym.github.io/inkbone/)** · 9 个题材包 · 19 条命令 · 51 项测试 · 零第三方依赖

用大模型写长篇连载，头三章看着还行，写到十几章毛病就全出来了：

- 前面埋的伏笔写到第 40 章自己忘了，或者把第 60 章才揭的底提前漏在旁白里；
- 仙侠文里突然冒出“降维打击”“寅时十刻”，每章必来一遍“瞳孔骤缩”“空气凝固”；
- 上一句主语是配角，下一句省了主语直接写动作，读者读成配角动的手；
- 让模型自己审稿，它张口就编一段原文里找不到的引文，顺手劝你“多加五感描写和形容词”。

这些问题靠把提示词写长管不住，模型自己写完就忘了。InkBone 把流程拆开：写之前靠分阶段提示词把规矩和节拍对齐，写完以后交给本地 Node 脚本按词表、台账和上下文逐行检查。

---

## 30 秒看它能抓出什么

> **不想装环境？** 直接打开 **[在线试跑台](https://blankym.github.io/inkbone/)** —— 纯前端 ES Module 在浏览器本地运行，你的正文、台账与审稿 JSON 绝不上传任何服务器，内置《药园》《宫闱》等样例与 `packet` / `verify-review` 实时演示。

<!-- 录制终端演示后保存为 docs/assets/demo.gif 并取消下行注释：
![InkBone 20 秒命令行实测演示](docs/assets/demo.gif)
-->

准备一段 9 行的测试稿 `ch01.md`：

```markdown
子时三刻，药园的木门被人拍响。

陆青瞳孔骤缩，起身去开门。

门外站着执事孙岳，雨水落到他身上就散成白雾。孙岳没进门，把一块铁牌丢在桌上：

“寅时十刻之前，把渠里的符拔干净。”

孙岳转身靠在门柱上，合上了眼。从袖子里摸出一把小刀，挑开了渠边的泥。
```

再写一份只有人名的台账 `ledger.json`：

```json
{ "characterNames": ["陆青", "孙岳"] }
```

本地直接运行（无需联网，无需 `npm install`）：

```bash
node bin/inkbone.mjs doctor ch01.md --genre classical-xianxia --ledger ledger.json --skip-length
```

终端输出：

```markdown
## ch01.md
- **L3**: `cliche_pupil_shrink` (瞳孔骤缩)
- **L7**: `reg_impossible_ke_count` (寅时十刻)
- **L9**: `subject_ambiguity` (previous actor 孙岳: 从袖子里摸出一把小刀，挑开了渠边的泥。)
```

- **第 3 行**：常见套话，只扫描引号外叙述（角色台词里正常说话不误报）；
- **第 7 行**：古代一个时辰只有八刻，“寅时十刻”直接标出历法穿帮；
- **第 9 行**：上一句开头是“孙岳”，这一句没写主语就接着写动作，程序顺着主语链往回读一遍，标出“这里读者会以为摸刀的是孙岳”。

### 顺手看一段实际改稿效果

```markdown
改前（常见 AI 起手）：
周建民今年四十三岁，退伍后一直守在老城区外卖站，心里盘算着月底前必须把差评压下去。他深吸一口气，嘴角露出一丝苦笑，推开玻璃门走了出去，免得被人看出异样。

改后（砍掉履历旁白、微动作套词和解释尾巴）：
屏幕右上角差评率挂在 0.62%，离片区红线还高一截。周建民把退单申诉表按平，扯下挂钩上的黄雨衣套上。门外胡飞正蹲在雨棚下抽烟，手机接单声刚响了两下就按了挂起。
```

---

## 安装与上手

需要 **Node.js 18+**，无第三方依赖。

### 方式一：装成 Agent Skill（推荐）

`skills/inkbone/` 是一个自包含目录，里面带着 `SKILL.md`、CLI 工具、全部配置和 7 个阶段提示词。把它复制到你所用 Agent（Claude Code、Codex、Antigravity 等）的 skills 目录就能用：

```bash
git clone https://github.com/blankym/inkbone.git
cp -R inkbone/skills/inkbone <你的 skills 目录>/inkbone
```

装好以后，在对话里直接按平常说话的方式提需求就行，例如：
- **开新书**：“我要写一本悬疑民俗长篇，先帮我定语体和世界观规则，建好 `novel.json` 和 `ledger.json`。”
- **写新章**：“按台账排第 12 章的节拍表，先给我确认再动笔。”
- **接手半截书稿**：“帮我给 `chapters/` 建台账，跑一遍体检，把逻辑漏洞和 AI 味重的段落标出来。”

> 如果所用平台禁用了命令行执行，提示词部分（`prompts/` 与 `resources/`）仍可照常使用，只需注意脚本类检查不会自动运行。

### 方式二：只跑本地命令行

```bash
git clone https://github.com/blankym/inkbone.git
cd inkbone
node bin/inkbone.mjs --help
```

全局安装（可选）：

```bash
npm install -g .
inkbone --help
```

三条最常用的起步路径：

1. **不想建台账？单章 30 秒快检**
   ```bash
   node bin/inkbone.mjs audit ch01.md --genre urban-realism --no-project --no-ledger --skip-length
   ```
2. **新书开局**
   ```bash
   node bin/inkbone.mjs init ./my-novel --genre classical-xianxia --title "书名"
   # 写第 N 章前组装上下文（未到 revealChapter 的设定真相会自动隐去）
   node bin/inkbone.mjs packet --ledger ./my-novel/ledger.json --chapter 4 --prev ./my-novel/ch03.md
   ```
3. **存量书稿接管与批量清洗**
   ```bash
   # 扫描已有章节（支持中文/阿拉伯数字章号与分卷目录），无损生成台账骨架
   node bin/inkbone.mjs import-ledger ./my-novel/chapters --out ./my-novel/ledger.json --title "书名"
   # 整本递归体检
   node bin/inkbone.mjs doctor ./my-novel/chapters
   # 零 token 清理误留的 **加粗**、--- 分隔线和规范省略号（保留对话破折号和白名单）
   node bin/inkbone.mjs normalize ./my-novel/chapters --strip-bold
   ```

---

## 工作流与核心设计

完整写作流程放在 `prompts/`（00～06），CLI 在各环节之间做确定性检查：

1. **定语体（`00-style-architect.md`）**：根据大纲定下题材包、人物三层声口矩阵和禁用词，写入小说目录里的 `novel.json`。
2. **排节拍（`01-beat-planner.md`）**：用 `packet` 取本章边界，把信息分配表和分幕节拍列出来，**先停下给作者确认，再写正文**。可用 `check-outline` 查细纲有没有留 `[待补充]` 或缺核心要素。
3. **写正文（`02-paratactic-renderer.md`）**：承接上一章末尾状态往下推进，检查是否有抄细纲原句。
4. **本地检查（`audit` / `doctor`）**：查出 `error` 级硬伤和 `warning` 级文风/逻辑隐患。
5. **审读与引文核验（`04`、`05` + `verify-review` / `review-save`）**：
   - `04-evidence-reviewer.md` 查剧情因果、时间线、物理常识和主角动机；
   - `05-reader-simulator.md` 分两次代入“零背景初读者”和“类型老读者”逐行挑卡壳点；
   - 两条审读输出 JSON 后，必须过一遍 `verify-review`：**引文不在正文里找得到的直接拒收，包含“五感/形容词/提升画面感”这类改文风评语的直接拒收**。
6. **局部修改（`03-targeted-rewriter.md`）**：只改标出来的行号和核验通过的问题，改完重查。
7. **定稿记录（可选 `detect`）**：每章最多测一次外部检测，结果存档，不拿检测分反复改稿。

### 它查哪些问题？

| 类别 | 具体检查项 | 级别 |
| :--- | :--- | :--- |
| 台账边界 | 必达事实锚点遗漏、未解锁真相提前剧透、废弃旧词残留、复述上章结尾 | `error`（阻断） |
| 格式与造假 | 残留 `**星号**`、文内括号账本注记（如 `(余13滴)`/`（尚余八滴）`）、字数宣称与相邻引号实际字数不符 | `error`（阻断） |
| 模型退化 | 邻行/长句复读、章末无标点截断、乱码、AI 拒答/自指词、工程结构词泄漏（Tier 1 阻断 / Tier 2 提示） | `error` / `warning` |
| 主语连续性 | 省略主语后动作落在前句别的角色头上；连续 3 段用同一种方式起头 | `warning` |
| 题材语域 | 古风里的现代热词、超过八刻的伪时辰、都市文里的半文言、科幻里的武侠腔等 | `warning`（高频升级 `error`） |
| 套话与密度 | 预制套话、对称骨架（`不是A而是B` 等）、否定排比、比喻/微动作/感叹号/省略号密度过高、电报体反向守卫 | `warning`（高频升级 `error`） |
| 统计指纹 | MATTR-50 词汇熵、句长变异系数、长定语与 `的` 字链密度等 20+ 项指标（对照人类样本区间） | `info`（仅诊断） |

只有客观错误（`error`）和高频泛滥的阻断项会让退出码非零，普通文风提示（`warning`）和统计指标（`info`）默认只打印行号供人判断，想全量卡死可以加 `--strict`。

### 三层规则：自己的书自己说了算

规则按三层合并，项目配置从章节所在目录自动向上查找 `novel.json`：

- **通用层**（`configs/zh-linguistics.json`、`configs/genres.json`）：跨题材成立的套话、对话标点、水话与句式检查；
- **题材层**（`configs/genres.json`）：9 个内置题材包，各自管各自容易串味的词汇与口吻；
- **项目层**（书目录的 `novel.json` + `.inkbone-whitelist`）：只属于这本书的禁忌词、文风要求和豁免白名单，还能用 `disabledRuleIds` 关掉不想用的上层规则。

新规则拿不准该放哪一层时，跑一次 `rule-stats --human <人类文本> --ai <AI稿>`，看看人类作者平时是不是也这么写。如果人类作品里每万字命中也很高，说明那是个人文风偏好，只放项目层，放进通用层只会把文章越改越僵。

---

## 内置网文写作与改稿方法库（`resources/`）

InkBone 不只做字面质检，还随 Skill 附带了一套面向长篇连载的实战写作手册（由经典作品拆解与一线网文编辑审稿口径提纯而成，仅在对应阶段按需读取，不浪费上下文）：

- **[微技法与大修反查表](resources/micro_techniques.md)**：把“好不好看”拆成可执行的动作公式，包括动作—反应“两压一扬”单元、强对抗“二八烘托”法则（80% 笔墨写环境异变与旁观标尺失态，20% 落致命招式）、伏笔“一物多用”与换地图前置坐标、高潮余韵与“战利品三件套”、防“闷坑”与“高级注水”纪律，以及针对拖沓、爽感不足、主角降智等 9 类卡壳症状的改稿对查表。
- **[8 组改稿正反例对照](resources/bad_vs_good_cases.md)**：直接对照展示“砍七步动作流水账”“台词晚进早出”“用眼前人下场融设定”“单段单主体对白潜文本”以及“不删成干瘪电报体”的具体改法。
- **[9 份流派剧本卡](resources/genre_playbooks/)**：针对仙侠、历史权谋、武侠、悬疑推理、现代都市、科幻废土、轻小说、言情和通用文，给出各自的核心驱动逻辑、常见避雷清单、落地道具颗粒和章尾钩子写法。

---

## 内置题材包与命令速查

<details>
<summary>9 个内置题材包（运行 <code>node bin/inkbone.mjs genres</code> 查看详情）</summary>

- `classical-xianxia`：古典仙侠 / 硬派修真 / 东方玄幻
- `historical-court`：历史权谋 / 严肃古风 / 古言正剧
- `wuxia-jianghu`：传统新武侠 / 庙堂江湖
- `mystery-thriller`：悬疑刑侦 / 民俗诡秘 / 无限流智斗
- `urban-realism`：现代都市 / 职场商战 / 现实言情
- `scifi-wasteland`：科幻废土 / 星际赛博 / 末日求生
- `light-fantasy`：轻小说 / 脑洞欢脱 / 反套路系统
- `romance-emotional`：古言女强 / 现代言情 / 双线情感拉扯
- `general-clean`：通用洁净叙事（跨题材默认基座）

</details>

| 分组 | 命令 | 作用 |
| :--- | :--- | :--- |
| 建账与备料 | `genres` | 列出内置 9 个题材包与默认预设 |
| | `init` | 在目标目录生成 `novel.json` 和 `ledger.json` 骨架 |
| | `import-ledger` | 扫描存量章节（支持中文数字章号与分卷），无损合并台账 |
| | `packet` | 装配下一章写作上下文，自动遮蔽未到揭露章的 `fullTruth` |
| 排版与检查 | `normalize` | 零 token 清理 Markdown 星号、分隔线和省略号/破折号 |
| | `check-outline` | 检查单章节拍细纲（Stage 1）是否遗漏要素或留有 `[待补充]` |
| | `audit` | 审计单章（台账边界、抄纲、语域、密度、退化与主语连续性） |
| | `doctor` | 递归扫描整个小说目录，按章号排序体检并自动匹配项目配置 |
| 审读与盲测 | `verify-review` | 核对审读 JSON 里的原句是否真在正文里，拦截越权文评 |
| | `review-save` | 校验后按正文 SHA-256 哈希与模型名归档审读记录 |
| | `review-stats` | 对比多次审读的跳读点与问题条数变化趋势 |
| | `eval-pack` | 将 A/B 两版稿件洗成匿名 X/Y 盲读包（附独立 `key.json`） |
| | `eval-score` | 汇总真人读者选票，计算胜率、符号检验 `p` 值与跳读分布 |
| 校准与记录 | `profile` | 输出单章 20+ 项语言学指纹指标 |
| | `calibrate` | 基于人类样本生成纯统计参考区间（p10 / 中位数 / p90） |
| | `rule-stats` | 统计每条规则在人类文本与 AI 稿中的命中率对比 |
| | `mine` | 从 AI 稿与人类文本中挖掘高频过度搭配候选 |
| | `detect` | 单次缓存调用朱雀检测（需自备 `.env` 密钥），仅作记录 |
| | `benchmark` | 运行基准语料指标对比 |

完整参数与选项请运行 `node bin/inkbone.mjs --help`。

---

## 目录与开发

```text
bin/  src/         CLI 入口与核心检查引擎（纯 Node，零依赖）
configs/           通用规则、9 个题材包、预设门禁与违规分级
docs/              浏览器纯前端静态试跑台（核心引擎零依赖运行）
prompts/           7 个分阶段写作与审读提示词（00–06）
resources/         正反例对照、微技法、9 份题材手册、盲读说明
benchmarks/        4 组盲读评估种子 + 第 1 章多版本实测记录（不含私有正文）
evals/             跨运行时 Skill 触发评测集
skills/inkbone/    自包含 Skill 发布目录（由脚本生成，勿直接修改）
tests/             51 项单元测试
```

```bash
npm test               # 运行 51 项测试（含代码零汉字字面量检查、docs 与 skill 同步检查；一项私有语料回归在公开仓库自动跳过）
npm run build:skill    # 修改 bin/src/configs/prompts/resources 后重新生成 skills/inkbone
npm run check:skill    # 检查 skills/inkbone 同步状态（CI 强制检查）
npm run build:docs     # 修改 src/core 或 configs 后同步静态试跑台 docs/vendor
npm run check:docs     # 检查 docs/vendor 同步状态（CI 强制检查）
```

## 致谢与许可

- 上下章边界隔离与“审读必须附原文引文”参考 [EthanYoQ/Pagekin](https://github.com/EthanYoQ/Pagekin)
- 中文主干与对称句式清理思路参考 [LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei)
- 修辞密度分级、退化及工程词泄漏检测参考 [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)
- 社区交流与反馈：[LINUX DO](https://linux.do/)

采用 [MIT](LICENSE) 协议开源。规则文件同样使用 MIT，可直接复制改造为自己的题材规则包。
