<div align="center">

<img src="assets/banner.svg" alt="Claude-Detection — Claude API 中转 / 代理掺水检测" width="100%">

<br>

[![selfcheck](https://github.com/wxmb01/Claude-Detection/actions/workflows/selfcheck.yml/badge.svg)](https://github.com/wxmb01/Claude-Detection/actions/workflows/selfcheck.yml)
![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-stdlib%20only-2ea44f)
![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-E8845F)
![Version](https://img.shields.io/badge/version-v1.3-8B5CF6)
[![License](https://img.shields.io/badge/license-MIT-64748B)](LICENSE)

**用服务端不可伪造的行为取证，判断一个 Claude 端点是不是"满血原装"。**

[快速开始](#-快速开始) · [**详细使用说明**](docs/USAGE.md) · [能检测什么](#-能检测什么) · [证据评分](#-六维证据评分) · [阳性对照](#-阳性对照) · [完整手册](skills/claude-detection/reference/MANUAL.md) · [单文件版](dist/Claude-skills.md)

</div>

---

## ◆ 为什么需要它

中转能任意伪造的东西，本项目**一律不采信**：模型自报身份、回答风格、响应速度、`model` 字段、响应头、`/v1/models` 列表。

它只看中转**改不动或很难改**的证据：

| | 证据 | 为什么难以伪造 |
|:---:|---|---|
| 🔏 | **thinking 签名校验** | 篡改签名必须返回 400，跨模型读取遵循官方规则。READ 不会凭空出现 |
| 🧊 | **缓存阈值** | 缓存只在**真实**前缀达到最小长度时触发，隐藏注入会让临界点提前 |
| 🧬 | **参数规则指纹** | 每个模型对参数组合的 400 / 200 规则不同，便宜模型冒充会露馅 |
| 🐤 | **尾部金丝雀** | 让模型报告"标记之后"的内容，被追加又从 usage 扣掉的文本无处可藏 |
| 🧮 | **程序判分新题** | 题目随机生成、答案由程序计算，与已验证基线逐题对比 |

> 本项目与 Anthropic 无关，不是官方工具。检测结论只适用于测试时段和被测的 Key / 分组，不构成对任何服务商的保证或指控。

## ◆ 能检测什么

| 掺水手法 | 主要方法 | 检测力 |
|---|---|:---:|
| 用便宜的同代模型冒充（如 Sonnet 5.5 冒充 Opus 5.5） | S14 替换指纹 · S3 读取矩阵（只用强证据） | **强** |
| 用旧一代或非 Claude 模型冒充 | S14 参数规则 + 缓存最小长度 · S15 tokenizer 向量 · S3 | **强** |
| 部分请求偷换 | S11 多样本逐条审计，给出偷换比例的 95% 上界 | 随 n 增长 |
| 注入提示词（含从 usage 扣掉的隐藏注入） | S1 差分记账 · S2 缓存阈值法 · S18 前置内容自报 | **强** |
| 条件注入 / 按轮注入 / 尾部注入 | S18 注入条件矩阵：UA、system、流式、多轮、工具、尾部断点、金丝雀 | **强** |
| 压低推理强度 | S8 effort 阶梯 · S7 与已验证基线逐题对比 | **强** |
| 截断上下文 / 输出、静默断流 | S5 九点书签 + usage 对账 · S6 流式时间线 | **强** |
| 改写参数、工具定义、输出，剥离 thinking | S4 参数指纹 · S17 工具完整性 · S19 输出纯净度 · S3 | 中～强 |
| 渠道不透明：借 IDE 代理账号（Kiro 等）、订阅号池、云平台或多层网关转手 | S20 渠道识别：响应头、错误体、注入的系统提示、usage 形态、ID 风格多维打分，输出渠道链 | 中～强 |

完整的检测力矩阵（18 种手法，含每种方法的盲区）见手册第 3A 节。

## ◆ 六维证据评分

<img src="assets/layers.svg" alt="六维证据评分" width="100%">

- 跑完检测会生成 `SCORE.md`，按 6 个维度汇总成 **100 分制证据评分**。
- 没测的项计 0 分，并单独报告**覆盖率**，不会被当成满分。覆盖不足时等级为 **I**，而不是 D。
- 发现换模型、隐藏注入、偷换等情况时**一票否决封顶**。
- 这是**规则化的证据汇总，不是"为真的概率"**。
- 总分之外还有**结论画像**，给出三个独立结论：上游是否 Anthropic 原生、中间是否有转换层 / 注入层、模型型号是否被验证。像"真 Claude，但经过 Kiro 转换层，型号未验证"这样的情况，也能如实写出来。

<details>
<summary><b>SCORE.md 输出示例</b>（诚实端点，quick 档）</summary>

```text
总分 57.0 / 100（原始得分 57.0，封顶 100）  I 覆盖不足：只完成了 60 分的检测项，已测项得分率 95.0%

| 维度                     | 检测项             | 得分 / 满分 | 状态 | 说明
| A 模型身份（29/35）       | S3 签名与读取矩阵  | 12 / 15     | 部分 | 强证据排除 8 个候选
| A 模型身份（29/35）       | S14 替换指纹       | 12 / 12     | 通过 | 仍一致的其他候选 ['claude-fable-5-1']
| A 模型身份（29/35）       | S15 tokenizer 向量 |  5 / 5      | 通过 | 与参考向量逐项一致
| C 注入与请求完整性（18/20）| S1 可见注入        |  6 / 6      | 通过 | usage 显示额外 0 token
| C 注入与请求完整性（18/20）| S2 隐藏注入        |  6 / 6      | 通过 | 隐藏注入区间 [0, 0]
| C 注入与请求完整性（18/20）| S18 注入条件矩阵   |  4 / 4      | 通过 | 可判定 10 项，异常 []
| D 上下文与输出（2/10）     | S19 输出纯净度     |  2 / 2      | 通过 | 逐字一致 4/4
| F 服务可靠性（5/5）        | 错误率             |  5 / 5      | 通过 | 0/158 次 5xx / 超时 / 空流
  …（未测的项计 0 分，run --tier standard 可补齐）
```

</details>

## ◆ 阳性对照

<img src="assets/positive-control.svg" alt="阳性对照：10 种作弊 + 5 种渠道模拟" width="100%">

检测工具自己也要被检验。`scripts/fake_relay.py` 是一个本地"作弊中转"，可以把请求转发到真实端点，同时做 10 种已知作弊中的一种。`scripts/positive_control.py` 会逐个模式运行对应检测。

- **10 种作弊全部检出，不作弊时 0 误报。**
- 另有 **5 种渠道模拟**（Kiro、Bedrock、Vertex、new-api 网关、官方对照组），渠道识别全部正确，官方对照组没有被误报成任何反代。
- 每种方法的盲区都如实标出。例如尾部隐藏注入能骗过所有基于 token 计数的方法，只有金丝雀能抓到。所以检测必须多种方法叠加。

## ◆ 快速开始

> 📘 **完整的分步教程见 [docs/USAGE.md](docs/USAGE.md)**：Windows / macOS 环境配置、四种使用方式、每个子命令的作用、输出文件说明、怎样看结果、常见问题排错。

### 第 1 步：下载并自检

```bash
git clone https://github.com/wxmb01/Claude-Detection.git
cd Claude-Detection/skills/claude-detection
python scripts/selfcheck.py          # 离线自检：不发请求、不花钱，显示"自检全部通过"即可
```

只需要 Python 3.9+，**不用安装任何依赖**。

### 第 2 步：配置端点和 Key（只放在环境变量里）

<table>
<tr><th>macOS / Linux / Git Bash</th><th>Windows PowerShell</th></tr>
<tr><td>

```bash
export BASE="https://your-endpoint.example"
export K="<YOUR_API_KEY>"
export AUTH=both
export OUT=./probe_out/run1
```

</td><td>

```powershell
$env:BASE = "https://your-endpoint.example"
$env:K    = "<YOUR_API_KEY>"
$env:AUTH = "both"
$env:OUT  = ".\probe_out\run1"
$env:PYTHONIOENCODING = "utf-8"
```

</td></tr>
</table>

- `BASE` 只填根地址，不要带 `/v1/messages`。
- `AUTH`：中转一般用 `both`，官方 API 用 `xapikey`。
- `OUT`：每次检测换一个新目录。

### 第 3 步：选一种方式运行

| 方式 | 适合谁 | 怎么做 |
|---|---|---|
| **① Claude Code Skill** | 用 Claude Code 的人 | `cp -r skills/claude-detection ~/.claude/skills/`，重开 Claude Code，说"帮我检测这个中转的 opus-5-5 是不是真的、有没有注入" |
| **② 其他 AI 助手** | Codex、Cursor、Gemini CLI、Cline 等能执行命令的工具 | 让它"阅读 `skills/claude-detection/SKILL.md` 并按流程执行"，或者写进它的 `AGENTS.md` / `GEMINI.md` / rules。[提示词模板](docs/USAGE.md#52-在其他能执行命令的-ai-助手中使用) |
| **③ 单文件版** | 任意 AI，包括网页聊天 | 把 [`dist/Claude-skills.md`](dist/Claude-skills.md) 发给它。它内嵌全部源码，可以用 `extract.py` 一键提取 |
| **④ 命令行** | 想自己掌控的人 | 运行下面这一条 |

```bash
python scripts/claude_probe.py run --tier quick --model claude-opus-5-5
```

不管用哪种方式，**评分都由脚本计算**，写在 `$OUT/SCORE.md` 里，与执行它的 AI 是谁无关。

### 第 4 步：看结果

| 输出文件 | 内容 |
|---|---|
| `SCORE.md` | 100 分制证据评分：等级、覆盖率、封顶原因、每项得分 |
| `results.json` | 每项检测的结构化结论与数值 |
| `raw.jsonl` | 每一个请求和响应的完整记录，所有数字都能追溯（含端点地址，不含 Key，不要公开） |

等级 **A / B / C / D** 按总分评定。**I** 表示覆盖不足：只是没测完，不代表有问题。怎样读各项结论见 [USAGE 第 9 节](docs/USAGE.md#9-怎样看结果)。

### 档位与成本

| 档位 | 内容 | 官方价目下的大致成本 | 耗时 |
|---|---|:---:|:---:|
| `quick` | 身份（S3 / S14 / S15）· 注入（S1 / S2 / S18）· 输出（S19）· 参数（S4）· 渠道（S20） | $1～2 | 约 10～30 分钟 |
| `standard` | quick + 多样本抽检 · effort · 能力基准 · 工具 · 上下文 · 流式 · 单 token 分布 | $8～15 | 约 1～2 小时 |
| `deep` | standard + 750K 上下文 · 困难档 · 60 条抽检 · 长时间流式 | $30～60 | 数小时 |

也可以单独运行各子命令：`baseline` `substitution` `thinking` `tokenizer` `cachegate` `injection` `purity` `params` `channel` `audit` `effort` `bench` `context` `stream` `tools` `onetoken`，最后运行 `score` 重新评分；检测进行中可以运行 `status` 查看进度。每个子命令的作用和常用参数见 [USAGE 第 7 节](docs/USAGE.md#7-单独运行某一项检测)。

## ◆ 目录

```
skills/claude-detection/
├── SKILL.md                     Skill 入口：何时使用、执行流程、关键判读、报告规则
├── reference/MANUAL.md          完整手册：维度、证据等级、证据评分、19 个 Skill、模式库、外部研究、规则表、模板
├── scripts/
│   ├── claude_probe.py          命令行入口
│   ├── probe_lib.py             HTTP、日志、规则表、统计
│   ├── probe_tasks.py           固定种子题库（程序判分）
│   ├── probe_extra.py           替换指纹、tokenizer、单 token 分布、工具完整性
│   ├── probe_inject.py          注入条件矩阵（含尾部金丝雀、前置内容自报）、输出纯净度
│   ├── probe_score.py           100 分制证据评分、结论画像、run 一键执行与 status
│   ├── probe_channel.py         S20 渠道识别
│   ├── channel_signatures.json  渠道识别特征库（每条规则带来源与核对日期）
│   ├── fake_relay.py            阳性对照：本地作弊中转（10 种作弊 + 5 种渠道模拟）
│   ├── positive_control.py      阳性对照：逐模式运行检测并汇总
│   └── selfcheck.py             离线自检
└── data/baseline_verified_20260929.json   已验证的 Opus 5.5 逐题基线
dist/Claude-skills.md            单文件版（内嵌源码与基线）
docs/USAGE.md                    详细使用说明
assets/                          README 插图
```

## ◆ 重要限制

<details>
<summary>展开</summary>

- **没有官方 Key 对照时**，"与官方逐题一致"只是推断。最直接的证明是把中转返回的 thinking 回传给官方 API 校验，这一步还**没有验证**。欢迎有官方 Key 的人补充。
- **规则表会过期**：缓存最小长度、跨模型读取规则、参数 400 规则来自官方文档，并在 9 个模型上实测核对过（2026-10-01）。模型更新后需要重新核对。v1.2 就更正过一条读取规则（手册 M23）。
- **双前提**：中转如果同时剥离 thinking、又清洗参数，身份只能靠行为证据，结论必须降级为"行为一致 / 不一致"。
- **只覆盖检测者发出的请求**：要覆盖真实使用流量，需要在业务请求中抽检。
- **还没有独立复现**：部分方法（缓存阈值法、替换指纹矩阵、尾部金丝雀、用 tokenizer 区分 Fable）是本项目提出的，只在作者的测试端点和本地作弊中转上验证过。
- **评分分值未经大规模校准**：证据评分的分值和封顶线是人为设定的。

</details>

## ◆ 致谢与参考

<details>
<summary>借鉴了以下项目的思路（代码全部重写），详见手册第 8 节</summary>

- [Model Equality Testing](https://github.com/i-gao/model-equality-testing)
- [IRIS-audit](https://github.com/Photen/IRIS-audit)
- [KBF](https://github.com/Ooo0ption/KBF)
- [fpverify](https://github.com/Mohamed7415/fpverify)
- [llm-api-audit](https://github.com/sunblaze-ucb/llm-api-audit)
- [veridrop](https://github.com/canarybyte/veridrop)
- [llm-probe](https://github.com/telagod/llm-probe)
- [ai-model-verifier](https://github.com/unorouter/ai-model-verifier)
- [which-llm](https://github.com/ictchenbo/which-llm)
- 中转软件源码：[new-api](https://github.com/QuantumNous/new-api)、[sub2api](https://github.com/Wei-Shaw/sub2api)、[claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service)、[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)

</details>

## ◆ 参与贡献

欢迎提交：

- 官方端点上的基线数据；
- 新模型的规则表更新；
- 独立复现的结果，无论成功还是失败；
- 新的作弊模式（给 `fake_relay.py` 加一种，并附上能抓到它的检测）。

请注意：

- 提交的检测数据请先脱敏，去掉 Key、域名和账号；
- 报告里只写现象和证据，不要对具体服务商下定性结论。

## License

[MIT](LICENSE)
