# InkBone（墨骨）

**给大模型配一本不会忘事的活账本，和一把不靠玄学的中文长篇小说改稿尺子。**

[![npm version](https://img.shields.io/npm/v/inkbone?color=cb3837&label=npm)](https://www.npmjs.com/package/inkbone)
[![Online Playground](https://img.shields.io/badge/%E5%9C%A8%E7%BA%BF%E8%AF%95%E8%B7%91%E5%8F%B0-%E7%BA%AF%E6%B5%8F%E8%A7%88%E5%99%A8%E9%9B%B6%E4%B8%8A%E4%BC%A0-2ea44f)](https://blankym.github.io/inkbone/)
[![test](https://github.com/blankym/inkbone/actions/workflows/test.yml/badge.svg)](https://github.com/blankym/inkbone/actions/workflows/test.yml)
[![依赖: 0](https://img.shields.io/badge/%E4%BE%9D%E8%B5%96-0-orange.svg)](package.json)
[![Node.js ≥ 18](https://img.shields.io/badge/Node.js-%E2%89%A518-brightgreen.svg)](https://nodejs.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[English](README.en.md) · **[在线试跑台 / 整书体检](https://blankym.github.io/inkbone/)** · **[npm 包](https://www.npmjs.com/package/inkbone)** · **[社区讨论](https://github.com/blankym/inkbone/discussions)** · 9 个题材包 · 离线 280 字滑窗 AIGC 卫士 · 简繁自动识别 · 内投 `.docx` 导出 · MCP 三件套 · VS Code 实时扩展 · 80 项测试

---

## 10 秒选你的入口

不管你是只在网页里用 DeepSeek / Claude 写连载的作者，还是在 Claude Code / Cursor 里全流程跑 Agent 的重度用户，v2.1 都有一条零废话的上手路径：

| 你平常用什么写小说？ | 直接怎么开始 | 你能立刻拿到什么 |
| :--- | :--- | :--- |
| **网页端 DeepSeek / Claude / Gemini / 豆包**<br/>（不想装任何环境） | 打开 **[在线试跑台 & 整书体检](https://blankym.github.io/inkbone/)** | 拖入单章或整个 `chapters/` 文件夹（**纯浏览器本地运行，正文绝不上传**）→ 词级高亮**双击原地改稿** + 跨章回声榜 + **一键复制精准改稿 Prompt** + 起点/番茄/七猫/晋江纯净 `.txt` / **内投 Word `.docx`** / **分章 `.zip`** 一键导出 |
| **Claude Code / Codex / Antigravity / OpenCode** | `npx skills add blankym/inkbone` | 8 阶段完整写作工作流 + 离线 280 字滑窗 AIGC 结构卫士 + 活账本防剧透 + 本地自动质检 + 9 份题材剧本卡 |
| **Claude Desktop / Cursor / Windsurf（MCP）** | 配一段 `npx -y inkbone mcp` | 一个配置拿齐 **10 Tools + 8 Prompts + 11 Resources**，连 Skill 都免装 |
| **VS Code / Cursor 实时写手 & 终端 CLI** | `npx inkbone audit ch01.md` 或启用 [VS Code 扩展](editors/vscode-inkbone/) | 零克隆整书体检 / 安全拆书定风格 / 边写边划波浪线 + **悬停查看角色台账状态** + **状态栏字数差额** |

---

## 为什么做 InkBone？

用大模型写长篇连载，头三章看着还行，写到十几章毛病就全出来了：

- 前面埋的伏笔写到第 40 章自己忘了，或者把第 60 章才揭的底提前漏在旁白里，甚至第 12 章已经阵亡的配角在第 38 章又走出来说话；
- 仙侠文里突然冒出“降维打击”“寅时十刻”，每章必来一遍“瞳孔骤缩”“嘴角露出一丝苦笑”；
- 上一句主语是配角，下一句省了主语直接写动作，读者读成配角动的手；
- 让模型自己审稿，它张口就编一段原文里找不到的引文，顺手劝你“多加五感描写和形容词”，结果越改 AI 味越重。

靠把 Prompt 越写越长管不住这些毛病——模型自己写完就忘了。**InkBone 把“会忘事的生成”与“不会忘事的硬检查”拆开**：写前由脚本编排防剧透上下文与分阶段节拍，写完由零依赖本地引擎按词表、台账、历法与主语链逐行卡死。

### 纯浏览器零上传：打开即试单章高亮 & 整书多章体检

![InkBone 在线试跑台：原文词级高亮、段落节奏心电图与一键精准改稿 Prompt](docs/assets/playground-audit.png)

> **Tab 1 单章体检**支持本地 `.md`/`.txt` 拖入、简繁自动识别（含港台網文繁體規則）、原文词级 `<mark>` 高亮、**双击任意行原地改稿（实时重算高亮并自动保存到 `localStorage`）**、黄金三章首屏留存门禁开关、**离线 280 字滑窗 AIGC 结构卫士开关（`--aigc-guard`）**、段落节奏心电图，以及**一键复制精准改稿 Prompt**。

![InkBone Browser Doctor：整书多章排序体检、跨章回声率、Top 10 套话榜与自动角色台账](docs/assets/playground-book-doctor.png)

> **Tab 4 整书体检（Browser Doctor）**支持一次选入整个 `chapters/` 文件夹：自动按中/数字章号排序，测出每章跨章回声率与全书高频套话 Top 10，一键下载自动挖掘好人物名单的 `ledger.json`，并一键导出起点 / 番茄 / 七猫 / 晋江纯净投稿 `.txt`、**标准宋体内投 Word (`.docx`)** 与**分章 `.zip` 压缩包**（内置各平台内投达标字数校验）。

### 与纯 Prompt 去 AI 味工具的核心差异

| 维度 | 常见纯 Prompt 写作提示词 | InkBone v2.1 |
| :--- | :--- | :--- |
| **去 AI 味与语域检查** | 靠大模型自我约束，几千字后必然漂移 | **确定性代码引擎**逐行扫描，支持简繁自动识别、9 个题材包与项目级自定义规则 |
| **长篇防吃书与防剧透** | 把大纲全塞进上下文，越长越容易提前漏底 | **活账本闭环（`packet` + `settle` + `check-ledger`）**：未到 `revealChapter` 自动 `[REDACTED]`，已退场/阵亡角色再出场直接预警 |
| **AI 审读可靠性** | 容易编造原文里没有的句子，越权乱改文风 | **`verify-review` 硬核验**：原文找不到逐字引文直接拒收，劝你“多加五感形容词”直接拦截 |
| **使用门槛与隐私** | 往往绑死单一客户端或需要把整本书上传云端 | **纯浏览器静态站（零上传）** + `npx` 零克隆 + 零依赖 MCP 三件套 + VS Code 实时波浪线 |
| **评估标准** | 容易滑向“为了过 AIGC 检测器乱换同义词” | **绝不拿检测分反复改稿**，以内置盲读包（`eval-pack` / `eval-score`）的真人读感为唯一标准 |

---

## 30 秒看它具体怎么抓错

```mermaid
flowchart LR
    A["写前打包 packet<br/>遮蔽未揭露真相 / 提醒到期伏笔"] --> B["分幕写正文<br/>Stage 1-2"]
    B --> C["本地硬尺子 audit / doctor<br/>语域 / 套话 / 退化 / 主语链 / 防诈尸"]
    C --> D["举证审读 + verify-review<br/>拒收假引文 / 拦截越权改文风"]
    D --> E["局部手术 Stage 4<br/>只改命中行号"]
    E --> F["写后结算 settle + check-ledger<br/>无损更新快照与伏笔状态"]
    F --> A
```

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

无需克隆仓库，直接跑一行命令（Node.js 18+）：

```bash
npx inkbone doctor ch01.md --genre classical-xianxia --ledger ledger.json --skip-length
```

终端直接定位出 3 类肉眼极易漏掉的问题：

```markdown
## ch01.md
- **L3**: `cliche_pupil_shrink` (瞳孔骤缩)
- **L7**: `reg_impossible_ke_count` (寅时十刻)
- **L9**: `subject_ambiguity` (previous actor 孙岳: 从袖子里摸出一把小刀，挑开了渠边的泥。)
```

- **第 3 行**：常见 AI 套话，且只扫描引号外叙述层（人物台词里正常说话绝不误报）；
- **第 7 行**：古代一个时辰只有八刻，“寅时十刻”直接标出历法穿帮；
- **第 9 行**：上一句主语是“孙岳”，下一句省主语接动作，程序顺着主语链回溯，预警“读者会以为摸刀的是孙岳”。

### 顺手看一段实际改稿效果

```markdown
改前（常见 AI 起手）：
周建民今年四十三岁，退伍后一直守在老城区外卖站，心里盘算着月底前必须把差评压下去。他深吸一口气，嘴角露出一丝苦笑，推开玻璃门走了出去，免得被人看出异样。

改后（砍掉履历旁白、微动作套词和解释尾巴）：
屏幕右上角差评率挂在 0.62%，离片区红线还高一截。周建民把退单申诉表按平，扯下挂钩上的黄雨衣套上。门外胡飞正蹲在雨棚下抽烟，手机接单声刚响了两下就按了挂起。
```

### 公开可复现评测对比（4 题材原创种子）

使用完全原创、零版权风险的公开测试对 [benchmarks/eval-set/public-pairs.json](benchmarks/eval-set/public-pairs.json)（可运行 `node scripts/run-public-eval.mjs` 随时复现，完整报告见 [benchmarks/public-report.md](benchmarks/public-report.md)）：

| 原创测试种子 | 题材包 | 典型 AI 初稿（阻断 / 提示 / 行命中） | InkBone 修订稿（阻断 / 提示 / 行命中） |
| :--- | :--- | :---: | :---: |
| 药园沟渠 | `classical-xianxia` | 0 / 5 / 13 | 0 / 0 / 0 |
| 雾港夜班 | `mystery-thriller` | 1 / 5 / 12 | 0 / 0 / 0 |
| 城中村站长 | `urban-realism` | 0 / 4 / 8 | 0 / 0 / 0 |
| 冷静期最后一天 | `romance-emotional` | 0 / 3 / 14 | 0 / 0 / 0 |
| **合计（4 题材）** | — | **1 / 17 / 47** | **0 / 0 / 0** |

---

## 4 条上手路径详解

### 路径一：零安装纯浏览器使用（最适合网页 AI 写手）

直接打开 **[https://blankym.github.io/inkbone/](https://blankym.github.io/inkbone/)**：

1. **单章精修（Tab 1）**：把网页大模型刚生成的章节贴进去（或拖入 `.md`/`.txt`），选好题材（繁体稿自动切换繁体规则层），查看原文高亮和段落节奏条；
2. **局部手术**：点击**“生成精准改稿 Prompt”**一键复制，粘回 DeepSeek / Claude / Gemini，模型只会修改被点名的具体行号，不再整段乱润色；
3. **整书体检与发稿（Tab 4）**：把几十章的本地文件夹一次选进去，查看跨章回声与全书 Top 10 套话榜，一键导出 `ledger.json` 或按起点/番茄/七猫/晋江规范合并导出纯净 `.txt`。

### 路径二：一行安装成 Agent Skill（Claude Code / Codex / Cursor / Antigravity）

`skills/inkbone/` 遵循 `agentskills` 开放规范，自包含 `SKILL.md`、CLI、配置、8 个阶段提示词与实战写作方法库：

```bash
npx skills add blankym/inkbone
```

也可以离线手动拷贝：

```bash
git clone https://github.com/blankym/inkbone.git
cp -R inkbone/skills/inkbone <你的 skills 目录>/inkbone
```

装好以后直接用自然语言指挥 Agent 即可：
- **开新书**：“我要写一本悬疑民俗长篇，先帮我定语体和世界观规则，建好 `novel.json` 和 `ledger.json`。”
- **写新章**：“按台账排第 12 章的节拍表，先给我确认再动笔；定稿后帮我跑完结算更新台账。”
- **接手半截书稿**：“帮我给 `chapters/` 建台账并自动提取出场人物，跑一遍体检，把逻辑漏洞和 AI 味重的段落标出来。”

> 如所用平台禁用了命令行执行，提示词部分（`prompts/` 与 `resources/`）仍可照常工作，只是本地脚本检查不会自动执行。

### 路径三：接入零依赖 MCP 三件套、Hooks 与 VS Code 实时扩展

InkBone 内置**零第三方依赖**的完整 `stdio MCP Server`。挂载后无需重复安装 Skill，即可一次性获得：
- **10 个结构化 Tools**：`inkbone_audit`、`inkbone_doctor`、`inkbone_aigc_check`、`inkbone_packet`、`inkbone_settle`、`inkbone_check_ledger`、`inkbone_verify_review`、`inkbone_normalize`、`inkbone_style_profile`、`inkbone_export`；
- **8 个阶段 Prompts**：`inkbone/style-architect` 至 `inkbone/chapter-settler`，传入 `genre` 自动拼附对应题材剧本卡；
- **11 份只读写作知识 Resources**：`inkbone://playbooks/<genre>`（9 份流派卡）、微技法手册与 10 组正反例。

在 Claude Desktop / Cursor / Windsurf 的 MCP 配置中加入（完整样例见 [examples/mcp-config.json](examples/mcp-config.json)）：

```json
{
  "mcpServers": {
    "inkbone": {
      "command": "npx",
      "args": ["-y", "inkbone", "mcp"]
    }
  }
}
```

- **Claude Code 自动门禁**：修改章节后自动跑审计、有硬伤立即打回，见 [examples/claude-code-hooks.json](examples/claude-code-hooks.json)。
- **VS Code / Cursor 实时波浪线扩展**：像 ESLint 一样边写边标红/标黄，支持一键清理 `**星号**`、一键加白名单、一键复制改稿 Prompt 与平台导出，见独立零依赖扩展 [editors/vscode-inkbone/](editors/vscode-inkbone/)。

### 路径四：命令行直接运行（`npx` / 全局安装 / 离线克隆）

需要 **Node.js 18+**，无任何第三方依赖：

```bash
# 免安装直接试跑
npx inkbone --help

# 或全局安装后随时调用 inkbone
npm install -g inkbone

# 或离线克隆直接跑（同样无需 npm install）
git clone https://github.com/blankym/inkbone.git && cd inkbone
node bin/inkbone.mjs --help
```

四条最常用的实战命令（如已全局安装，可将 `npx inkbone` 简写为 `inkbone`）：

1. **单章 30 秒快检、离线 280 字滑窗 AIGC 预检 & 一键生成改稿 Prompt（简繁自动识别）**
   ```bash
   npx inkbone audit ch01.md --genre urban-realism --format md --no-project --no-ledger --skip-length
   npx inkbone aigc-check ch01.md
   npx inkbone rewrite-prompt ch01.md --genre urban-realism --aigc-guard --no-project --no-ledger --skip-length
   ```
2. **零版权安全拆书定风格 + 新书活账本闭环**
   ```bash
   # 只提取纯统计节奏画像与可直接写入 novel.json 的 customGates，绝不复制范文原句
   npx inkbone style-profile ./ref-samples --out ./my-novel/style.json
   npx inkbone init ./my-novel --genre classical-xianxia --title "书名"
   npx inkbone packet --ledger ./my-novel/ledger.json --chapter 4 --prev ./my-novel/ch03.md
   npx inkbone settle --ledger ./my-novel/ledger.json --patch ./my-novel/ch04-settlement.json
   npx inkbone check-ledger ./my-novel/ledger.json --current 4
   ```
3. **存量百章长篇接管、批量回填台账与增量体检**
   ```bash
   # 启发式挖掘角色候选填入 characterNames（激活主语歧义检测）
   npx inkbone import-ledger ./my-novel/chapters --auto-characters --out ./my-novel/ledger.json --title "书名"
   # 为尚未填写 coreSummary 的旧章节按每 5 章一批生成回填 Prompt，并批量合入台账
   npx inkbone backfill-prompt ./my-novel/chapters --ledger ./my-novel/ledger.json --batch-size 5 --limit 1
   npx inkbone settle --ledger ./my-novel/ledger.json --patch ./my-novel/batch-settlement.json --batch
   # 增量体检：仅扫指定章或 git 变动章，同时自动保留前章查跨章回声
   npx inkbone doctor ./my-novel/chapters --chapters 40-45
   npx inkbone doctor ./my-novel/chapters --changed
   ```
4. **一键清洗导出到网文平台后台 & 生成内投 Word (`.docx`) / 分章 `.zip`**
   ```bash
   npx inkbone export ./my-novel/chapters --platform qimao --out ./dist/qimao --merge-out ./dist/vol1.txt --docx-out ./dist/内投2万字.docx --zip-out ./dist/chapters.zip --outline ./my-novel/outline.md --title "书名"
   ```

---

## 工作流与核心引擎设计

完整写作流程放在 `prompts/`（00–07），CLI / MCP 在各环节之间做确定性检查与合账：

1. **定语体（`00-style-architect.md`）**：根据大纲或 `style-profile` 画像定下题材包、人物三层声口矩阵与禁用词，写入 `novel.json`。
2. **排节拍（`01-beat-planner.md`）**：用 `packet` 取本章防剧透上下文与到期伏笔提醒，列出信息分配表和分幕节拍，**先停下给作者确认再写正文**；可用 `check-outline` 查是否遗留 `[待补充]`。
3. **写正文（`02-paratactic-renderer.md`）**：承接上章末尾状态直接推进，禁止复述上章收尾或抄细纲原句。
4. **本地检查（`audit` / `doctor`）**：查出 `error` 级硬伤和 `warning` 级文风/逻辑隐患（默认中文报告，支持 `--lang en`、`--variant auto|zh-hans|zh-hant`）。
5. **举证审读与引文核验（`04`、`05` + `verify-review` / `review-save`）**：
   - `04-evidence-reviewer.md` 查因果、时间线、物理常识与主角动机；
   - `05-reader-simulator.md` 分两次代入“零背景初读者”与“类型老读者”挑卡壳点；
   - `verify-review` 强制核验：**引文不在正文里找得到的直接拒收，出现“多加五感/形容词/提升画面感”这类越权改文风评语的直接拒收**。
6. **局部手术（`03-targeted-rewriter.md`）**：只改标出来的行号和核验通过的问题，改完重查。
7. **写后结算与台账体检（`07-chapter-settler.md` + `settle` / `check-ledger`）**：将本章摘要、角色 8 字段快照增量与伏笔状态跃迁无损合入 `ledger.json`，排查逾期伏笔后再开下一章。
8. **定稿留档（可选 `detect`）**：每章最多测一次外部检测，仅作记录存档，不拿检测分反复改稿。

### 核心检查项一览

| 类别 | 具体检查项 | 级别 |
| :--- | :--- | :--- |
| 台账、短线道具与世界观铁律 | 必达事实锚点遗漏、未解锁真相提前剧透、废弃旧词残留、复述上章结尾；**已阵亡/退场角色在非回忆段落再次行动说话预警（`DECEASED_CHARACTER_APPEARANCE`）**；**短线战术道具到期未回收预警（`UNRESOLVED_TACTICAL_PROP`）**；**可执行世界观铁律门禁（`WORLD_RULE_VIOLATION`）**；**跨章可量化资源加减与期初/期末余额守恒（`RESOURCE_LEDGER_MISMATCH`）** | `error` / `warning` |
| 格式、字数与历法自洽 | 残留 `**星号**`、文内括号账本注记（如 `(余13滴)`/`（尚余八滴）`）、字数宣称与相邻引号实际字数不符；**同章内农历月日跨度与“半个月”宣称自相矛盾（`CALENDAR_SPAN_CONTRADICTION`）** | `error` / `warning` |
| 黄金三章开篇留存 | 开启 `--golden-three` 时，检查首屏（前 380 汉字）是否存在零对白且缺乏即时冲突动作信号的慢热铺垫（`GOLDEN_OPENING_SLOW_START`） | `warning` |
| 模型退化 | 邻行/长句复读、章末无标点截断、乱码、AI 拒答/自指词、工程结构词泄漏（Tier 1 阻断 / Tier 2 提示） | `error` / `warning` |
| 主语连续性 | 省略主语后动作落在前句别的角色头上；连续 3 段用同一种方式起头 | `warning` |
| 题材语域与简繁 | 古风里的现代热词、超过八刻的伪时辰、都市文里的半文言、科幻里的武侠腔；**繁體中文与港台網文跨語境詞/直角引號衛生自动适配** | `warning`（高频升级 `error`） |
| 套话与密度 | 预制套话、对称骨架（`不是A而是B` 等）、否定排比、面板说明书播报腔、比喻/微动作/感叹号/省略号密度过高、电报体反向守卫 | `warning`（高频升级 `error`） |
| 离线滑窗 AIGC 结构卫士 | `aigc-check` 或 `--aigc-guard` 扫描 280 字滑窗段落句式熵（`N/A/Q/S`）、连续夹心对话连击、双侧 U 型`的`字走廊、`这/那`指示词激增与五字实词砖块硬拼 | `warning` / `info` |
| 统计指纹 | MATTR-50 词汇熵、句长变异系数、段落句式熵、长定语与 `的` 字链密度等 20+ 项指标（对照人类样本区间） | `info`（仅诊断） |

只有客观错误（`error`）和高频泛滥的阻断项会让退出码非零，普通文风提示（`warning`）默认只打印行号供人判断；如需全量卡死可加 `--strict`。

### 三层规则：自己的书自己说了算

规则按三层合并，项目配置从章节目录自动向上查找 `novel.json`：

- **通用层**（`configs/zh-linguistics.json`、`configs/zh-traditional.json`）：跨题材成立的套话、水话、标点与简繁通用检查；
- **题材层**（`configs/genres.json`）：9 个内置题材包，各自管各自容易串味的词汇与口吻；
- **项目层**（书目录的 `novel.json` + `.inkbone-whitelist`）：本书专属禁用词、`customGates` 节奏门禁、白名单与 `disabledRuleIds`（随时关闭不合本书口味的上层规则）。

> 拿不准某条新规则该放哪一层？跑一次 `npx inkbone rule-stats --human <人类文本> --ai <AI稿>`，如果人类作品里每万字命中也很高，说明那是个人文风偏好，只放项目层，放进通用层只会把文章越改越僵。

---

## 内置网文写作与改稿方法库（`resources/`）

InkBone 不只做字面质检，还内置了一套由经典作品拆解与一线网文编辑口径提纯的实战手册（按阶段按需读取，不浪费上下文）：

- **[微技法与大修反查表](resources/micro_techniques.md)**：动作—反应“两压一扬”单元、强对抗“二八烘托”法则、伏笔“一物多用”与换地图前置坐标、高潮余韵与“战利品三件套”，以及针对拖沓、爽感不足、主角降智等 9 类卡壳症状的改稿反查表；
- **[10 组改稿正反例对照](resources/bad_vs_good_cases.md)**：直观演示“砍七步动作流水账”“台词晚进早出”“用眼前人下场融设定”“账目面板信息去说明书化”与“防强删‘的’字反弹电报体”；
- **[9 份流派剧本卡](resources/genre_playbooks/)**：覆盖仙侠、历史权谋、武侠、悬疑推理、现代都市、科幻废土、轻小说、言情与通用文的核心驱动、避雷清单、道具颗粒与章尾钩子。

---

## 内置题材包与 27 条命令速查

<details>
<summary>点击展开 9 个内置题材包（运行 <code>npx inkbone genres</code> 查看详情）</summary>

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
| 建账与活账本 | `genres` / `init` | 查看 9 个题材包 / 在目标目录生成 `novel.json` 与 `ledger.json` 骨架 |
| | `import-ledger` / `backfill-prompt` | 扫描存量章节挖掘角色候选并合并台账 / 为未填摘要的存量章节分批生成 `settle --batch` 回填 Prompt |
| | `packet` | 装配下一章写作上下文，自动遮蔽未揭露 `fullTruth`、过滤已收伏笔并按角色裁剪快照 |
| | `check-ledger` / `settle` | 校验台账健康度、短线道具与资源流水守恒 / 将单章或 `--batch` 批量写后结算 JSON 无损合入 `ledger.json` |
| 排版与质检 | `normalize` / `check-outline` | 零 token 清理星号与破折号 / 检查 Stage 1 细纲遗漏项与 `[待补充]` |
| | `audit` / `doctor` | 单章审计（支持简繁、防诈尸、世界观铁律、`--golden-three`、`--aigc-guard`）/ 整书或增量体检（`--chapters` / `--changed`） |
| | `aigc-check` / `rewrite-prompt` | 零 token 扫描 280 字滑窗 AIGC 结构与虚词失衡 / 审计单章并直接输出精准局部改稿 Prompt |
| 拆书与发稿 | `style-profile` / `export` | 零原文泄露安全拆书生成 `customGates` / 按起点、番茄、七猫、晋江规范导出 `.txt`、**内投 Word `.docx`** 与 **分章 `.zip`** |
| 协议集成 | `mcp` | 启动零第三方依赖 stdio MCP Server（10 Tools + 8 Prompts + 11 Resources） |

<details>
<summary>点击展开审读归档、盲读评测与规则校准命令（共 11 条研究/进阶命令）</summary>

| 分组 | 命令 | 作用 |
| :--- | :--- | :--- |
| 审读与盲测 | `verify-review` | 核对审读 JSON 里的原句是否真在正文里，拦截越权文评 |
| | `review-save` | 校验后按正文 SHA-256 哈希与模型名归档审读记录 |
| | `review-stats` | 对比多次审读的跳读点与问题条数变化趋势 |
| | `eval-pack` | 将 A/B 两版稿件洗成匿名 X/Y 盲读包（附独立 `key.json`） |
| | `eval-score` | 汇总真人读者选票，计算胜率、符号检验 `p` 值与跳读分布 |
| 校准与记录 | `profile` | 输出单章 20+ 项语言学指纹指标 |
| | `calibrate` | 基于人类样本生成纯统计参考区间（p10 / 中位数 / p90） |
| | `rule-stats` | 统计每条规则在人类文本与 AI 稿中的命中率对比 |
| | `mine` | 从 AI 稿与人类文本中挖掘高频过度搭配候选 |
| | `detect` | 单次缓存调用外部检测（需自备 `.env` 密钥），仅作留档不反刷 |
| | `benchmark` | 运行基准语料指标对比 |

</details>

日常高频参数运行 `npx inkbone --help`，全部 27 条命令运行 `npx inkbone --help-all`。

---

## 目录与本地开发

```text
bin/  src/         CLI 入口、零依赖核心引擎（含安全拆书/DOCX+ZIP导出/Browser Doctor）与 MCP 三件套
configs/           通用规则、9 个题材包、繁体中文规则层、4 平台导出预设、门禁与双语文案
docs/              纯前端静态试跑台（支持双击原地改稿）与整书多章体检台（支持一键导出 .docx / .zip）
editors/           零依赖 VS Code / Cursor 实时波浪线扩展（含角色台账 Hover 卡片与平台字数状态栏）
examples/          MCP 客户端配置与 Claude Code PostToolUse Hook 模板
prompts/           8 个分阶段写作、审读与写后结算提示词（00–07）
resources/         正反例对照、微技法、9 份题材剧本卡、盲读说明
benchmarks/        4 组原创评估种子、公开对照样本与可复现对比报告（不含私有正文）
evals/             跨运行时 Skill 触发评测集
skills/inkbone/    自包含 Skill 发布目录（由脚本生成，勿直接修改）
tests/             80 项单元测试
```

```bash
npm test               # 运行 80 项测试（含代码零汉字字面量、280 字滑窗 AIGC 卫士、MCP 三件套、繁简、DOCX/ZIP导出、VS Code 核、docs 与 skill 同步）
npm run build:skill    # 修改源码/配置/提示词后重新生成 skills/inkbone
npm run check:skill    # 检查 skills/inkbone 同步状态（CI 强制检查）
npm run build:docs     # 修改 src/core 或 configs 后同步静态试跑台 docs/vendor
npm run check:docs     # 检查 docs/vendor 同步状态（CI 强制检查）
```

## 参与共建、致谢与许可

欢迎拿你正在写的真实章节去 **[在线试跑台](https://blankym.github.io/inkbone/)** 测一测，如果抓到了误报、或者想补充你常写细分题材的语域规则，欢迎直接参与：

- **交流与晒单**：[GitHub Discussions](https://github.com/blankym/inkbone/discussions)
- **报告误报 / 提议新规则**：[提交表单](https://github.com/blankym/inkbone/issues/new/choose)
- **社区友链与认可**：本项目完整开源，认可并感谢 [LINUX DO](https://linux.do/) 社区的开源分享氛围与早期试跑建议（友链：[https://linux.do/](https://linux.do/)）
- **致谢启发**：
  - 上下章边界隔离与“审读必须附原文引文”参考 [EthanYoQ/Pagekin](https://github.com/EthanYoQ/Pagekin)
  - 中文主干与对称句式清理思路参考 [LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei)
  - 修辞密度分级、退化及工程词泄漏检测参考 [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode)

采用 [MIT](LICENSE) 协议开源。所有规则文件与流派剧本卡同样使用 MIT，欢迎直接复用或改造成自己的写作规则包。
