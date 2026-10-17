> **致谢与上游**
> 本项目向 [Tauric Research](https://github.com/TauricResearch) 致敬并表示支持。
> ITF（Invest the Future / TradingAgents A 股特供版）**源自上游** [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)（论文：[arXiv:2412.20138](https://arxiv.org/abs/2412.20138)），在其多智能体投研框架之上演进为面向 A 股的桌面端实现。

---

# Invest the Future（ITF）

**A 股多智能体投研框架 · 桌面版**（基于 [TradingAgents](https://github.com/TauricResearch/TradingAgents) 演进）

中文 · [English](README_EN.md)

面向 **A 股** 的桌面端分析系统：多智能体辩论 → 量化评分 → 信号过滤 → 可选追问。本地包名：`invest_the_future`。

- **仅 A 股**：上交所 `.SS`、深交所 `.SZ`；输入 `.SH` 会自动归一为 `.SS`。示例标的：`600519.SS` 贵州茅台。
- **A 股口径**：红涨绿跌；行情/基本面走东方财富、Baostock、AKShare；情绪看中文社媒与股吧；新闻看国内资讯。
- **主入口是桌面端**（NiceGUI + PyWebView），CLI 与 Docker 为可选。

## 近期更新（本仓库）

- **买门（开仓门槛）真因子**：开仓前要求技术面、基本面等"真因子"数据齐全才放行——OHLCV（开盘/最高/最低/收盘/成交量）行情代理不能冒充基本面数据。
- **基本面可观测**：`.SH`→`.SS` 代码归一、因子缓存预热（提前拉取并缓存）、数据缺失原因（miss reason）直接显示在过滤提示里。
- **底部追问栏**：分析结束后可 `@` 指定角色继续追问，默认 **财富船长**；修复了工具被重复封装导致的追问调用失败。
- **新闻权重分摊**：没有有效新闻源时跳过新闻维度，其权重按比例分给其余维度，避免总分被拉低。
- **评级中文**：买入 / 增持 / 持有 / 减持 / 卖出（沿用券商研报用语）。

上游 TradingAgents 版本说明见 [CHANGELOG.md](CHANGELOG.md)。

> 本框架仅供研究与学习。分析结果受模型、温度、区间、数据质量等影响，**不构成投资建议**。详见 [免责声明](https://tauric.ai/disclaimer/)。

<div align="center">

🚀 [和上游差在哪](#和上游-tradingagents-差在哪) · 🧭 [和 CN 差在哪](#和-tradingagents-cn-差在哪) · 🛡️ [数据不全不开仓](#数据不全不开仓数据门) · 💬 [分析完还能追问](#分析完还能追问) · 🚀 [框架介绍](#框架介绍) · 🖥️ [桌面端](#桌面端-nicegui) · ⚡ [安装（一页过）](#安装) · 📦 [代码调用](#代码调用) · 🤝 [贡献](#贡献) · 📄 [引用](#引用)

</div>

## 和上游 TradingAgents 差在哪

本仓是上游 [TradingAgents](https://github.com/TauricResearch/TradingAgents) 的 **A 股桌面演进版**，不是原版镜像。10 秒对照：

| 维度 | 上游 TradingAgents | ITF（本仓） |
|------|-------------------|------------|
| 市场 | 美股为主 | **仅 A 股**（`.SS` / `.SZ`；`.SH` 自动归一为 `.SS`） |
| 数据 | FinnHub / yfinance 等 | **东财 / Baostock / AKShare**，无需美股数据 Key |
| 入口 | CLI / Docker 优先 | **桌面端** `python main.py`（CLI / Docker 可选） |
| 展示与评级 | 英文语境为主 | **红涨绿跌**；五档评级中文（买入/增持/持有/减持/卖出） |
| 本仓增强 | — | **数据不全不开仓**、**分析完还能追问**、新闻权重分摊 |

本仓**不做**短线短卡 / 纸面追踪等实验管线；公开协作请以本 GitHub 桌面分析版为准。

## 和 TradingAgents-CN 差在哪

[TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) 是中文社区里很强的 **Web 投研平台**（多市场、Docker、文档生态完整）。ITF 不跟它对打广度，只做更窄的桌面工具：

| 维度 | TradingAgents-CN | ITF（本仓） |
|------|------------------|-------------|
| 定位 | 多市场 Web 投研平台（A/港/美，前后端 + Docker 部署） | **仅 A 股** 的 Windows **桌面工具**，`python main.py` 即用 |
| 安装 | Docker 编排、多组件、配置项多 | 单 `requirements`、无强制 Docker / 数据库，约 10 分钟出窗口 |
| 使用成本 | 需自备多种数据/LLM 配置 | 数据走免费公开源；LLM **任选一家**（侧栏可换） |
| A 股深度 | 三市场之一 | 唯一市场：桌面里把 A 股分析跑通并可持续追问 |
| 防幻觉 | 各 agent 直接给结论为主 | **数据门**：基本面/技术面等真因子不齐则拒绝开仓，缺失原因可见 |
| 交互 | 偏「提交任务 → 出报告」 | **底部追问**：分析结束后 `@` 角色继续聊，默认财富船长 |

简单说：**想部署一套平台选 CN；只想几分钟装好、在桌面上把 A 股问清楚，用 ITF。**

## 数据不全不开仓（数据门）

多智能体 LLM 常见翻车是「数据没拉到，报告仍写得很像真的」。ITF 用 **数据门** 主动拒答，而不是硬编：

- **买门 / 真因子**：开仓门槛要求技术面、基本面等「真因子」齐全；OHLCV 行情代理不能冒充基本面。
- **缺失可见（miss reason）**：过滤提示里直接写清缺哪一类数据，便于你决定重跑或换日。
- **新闻权重分摊**：没有有效新闻源时跳过新闻维度，把权重分给其余维度，避免总分被噪声拖垮。

原则就一句：**宁可说「现在不能开仓 / 数据不够」，也不让模型瞎编表格。**

<p align="center">
  <img src="assets/data-gate-example.png" alt="数据门示例：情绪源无效时标 low 置信度并写明中性=数据不可用" width="90%">
</p>

<p align="center"><sub>示例：多源无效 / 接口报错时标 <code>confidence: low</code>，并写明「中性 = 数据不可用」而非假装读到了市场情绪。</sub></p>

## 分析完还能追问

很多多智能体仓是「跑完出一篇长文就结束」。ITF 把研报做成**可继续聊**：

- 一轮分析结束后，底部可直接追问；用 `@成员` 点名角色（默认 **财富船长**）。
- 追问带着本轮辩论与结论上下文，适合问「为什么是持有？」「最大风险是什么？」「若跌破某价怎么看？」这类跟进问题。
- 这是桌面工具路径：装上就是想把一只票问清楚，而不是部署完就走人。

一句话：**不是一次性交卷，是分析完还能当场问。**

## 框架介绍

ITF / TradingAgents 用多智能体协作模拟一支投研团队：分析师分头研究，多空研究员辩论，交易员给出建议，风控多视角评估，最终由投资组合经理（财富船长）给出五档评级。

<p align="center">
  <img src="assets/schema.png" style="width: 100%; height: auto;">
</p>

复杂的投研任务被拆成专职角色：

### 分析师团队

- **市场/技术分析师**：用 MACD、RSI、均线等指标研判 A 股趋势与动量。
- **情绪分析师**：汇总雪球、东方财富股吧等中文社媒情绪，刻画短期市场热度。
- **新闻分析师**：跟踪财联社、同花顺快讯、东财快讯等国内宏观与产业资讯，解读事件对行情的影响。
- **基本面分析师**：评估财务与经营质量（ROE、毛利率、现金流等），并参考龙虎榜、北向资金等 A 股特色数据。

<p align="center">
  <img src="assets/analyst-ashare.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

> 图中与界面均按 A 股习惯**红涨绿跌**展示，仅为视觉约定，不构成任何收益暗示。

### 研究员团队

- **多头 / 空头研究员**：对分析师结论做结构化辩论——多头评估上行空间（品牌护城河、北向资金关注、业绩稳健性），空头评估估值与下行风险（估值偏高、消费承压、政策与流动性不确定性），权衡收益与风险。

<p align="center">
  <img src="assets/researcher-ashare.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### 交易员

- 综合分析师与研究员报告，形成交易建议（时机与仓位量级）。仓位提示会顾及 A 股交易规则：整手 100 股、印花税与佣金等交易成本（仅作提示，点到为止）。

<p align="center">
  <img src="assets/trader-ashare.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### 风控与投资组合经理

- 风控团队从激进 / 中立 / 保守三种视角评估波动、流动性等风险。
- **财富船长（投资组合经理）** 基于全链路分析给出最终五档评级：买入 / 增持 / 持有 / 减持 / 卖出。

<p align="center">
  <img src="assets/risk-ashare.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## 桌面端（NiceGUI）

本仓库主入口为桌面应用（NiceGUI + PyWebView 原生窗口）：

```powershell
# Windows PowerShell（先完成下方「安装」并激活虚拟环境）
python main.py
```

```bash
# Linux / macOS
python main.py    # 或 ./launch.sh
```

功能概览：

- 聊天室流式展示多智能体辩论与最终决策
- 侧边栏配置模型、自选股、历史回放
- 分析结束后底部追问：可 `@成员`，默认财富船长（见上节「分析完还能追问」）
- 量化评分、信号过滤，以及 **数据门（数据不全不开仓）** 提示

## 安装

**目标：按下面抄命令，约 10～20 分钟内弹出桌面窗口。**  
成功标准：出现 ITF 主窗口（左侧配置 / 右侧聊天或分析区）。能看到窗口 = 安装成功；再在侧栏选标的点分析即可。

<p align="center">
  <img src="assets/desktop-success.png" alt="ITF 桌面端启动成功示意" width="90%">
</p>

<p align="center"><sub>上图即为成功状态示例（无需先跑完一整轮分析）。</sub></p>

要求：Python ≥ 3.10、Git（也可用 GitHub **Download ZIP**，解压后从「建虚拟环境」那一步开始）。

### Windows（PowerShell，推荐）

```powershell
git clone https://github.com/cms19859230182-lang/TradingAgents-AGu-Edition-ITF.git
cd TradingAgents-AGu-Edition-ITF
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
notepad .env
# 任选一家 LLM，取消注释并填入对应 API Key（见 .env.example）
# 保存关闭记事本后：
python main.py
```

> PowerShell 若提示「无法加载，因为在此系统上禁止运行脚本」，先执行一次：  
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`  
> 再重新 `.\venv\Scripts\Activate.ps1`。

### Linux / macOS（bash）

```bash
git clone https://github.com/cms19859230182-lang/TradingAgents-AGu-Edition-ITF.git
cd TradingAgents-AGu-Edition-ITF
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env：任选一家 LLM，填入对应 API Key
python main.py    # 或 ./launch.sh
```

> 可选：自建 Gitea 镜像可从镜像 clone；公开协作请以本 GitHub 仓库为准。

### 所需 API（最少填一项）

打开 `.env`，**任选一家** LLM 提供商写入对应 Key 即可（通义 / 智谱 / Kimi / DeepSeek / OpenAI / Gemini 等），变量名见 `.env.example` 注释。也可用本机 Ollama（无需 Key）或 OpenAI 兼容端点。桌面端侧栏也可改提供商与模型。

示例（只是举例，不是指定某家）：

```bash
# 任选其一，不要多填互相冲突也可以，以你在 UI/配置里选的提供商为准
DASHSCOPE_CN_API_KEY=sk-xxxxxxxx
# 或 OPENAI_API_KEY=...
# 或 DEEPSEEK_API_KEY=...
```

**数据 API**：A 股行情与基本面默认走东方财富 / Baostock / AKShare 等公开源，**不用美股数据 Key**。

### 常见翻车

| 现象 | 处理 |
|------|------|
| `Activate.ps1` 被禁止 | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 后重开终端再激活 |
| `python` / `pip` 找不到 | 安装 [Python 3.10+](https://www.python.org/downloads/)，安装勾选 **Add python.exe to PATH** |
| 窗口没出来、终端一片红 | 把完整报错贴到 [Issues](https://github.com/cms19859230182-lang/TradingAgents-AGu-Edition-ITF/issues)；先确认已 `Activate` 且 `pip install -r requirements.txt` 成功 |
| 能开窗口但分析失败 | 检查 `.env` 是否已保存、所用提供商 Key 有无多余空格/引号；侧栏所选提供商是否与 Key 对应 |

### CLI（可选）

桌面端不需要 CLI；喜欢终端交互的可以用：

```bash
tradingagents              # 随 requirements 安装后即可用
python -m cli.main         # 或源码直接跑
```

### Docker（可选，上游兼容）

Docker 是上游 TradingAgents 沿袭下来的运行方式，**不是本仓主入口**；桌面端请直接用上面的 `python main.py`。

```bash
cp .env.example .env
docker compose run --rm tradingagents
# 本地 Ollama：
docker compose --profile ollama run --rm tradingagents-ollama
```

### 市场与代码

本仓库为 **A 股特供版**，仅支持 A 股代码：

| 市场 | 示例 |
|------|------|
| **A 股** | 上交所 `.SS`（如 `600519.SS` 贵州茅台），深交所 `.SZ`（如 `000858.SZ` 五粮液）；输入 `.SH` 会归一为 `.SS` |

A 股行情优先东方财富 / Baostock；基本面评分依赖因子缓存或 AKShare 个股信息。预热示例：

```powershell
# Windows PowerShell
python scripts/warm_factors.py --date (Get-Date -Format yyyy-MM-dd) --from-watchlist
```

```bash
# Linux / macOS
python scripts/warm_factors.py --date $(date +%F) --from-watchlist
```

## 代码调用

基于 LangGraph，包路径为 `invest_the_future`：

```python
from invest_the_future.graph.trading_graph import InvestTheFutureGraph
from invest_the_future.default_config import DEFAULT_CONFIG

ta = InvestTheFutureGraph(debug=True, config=DEFAULT_CONFIG.copy())
_, decision = ta.propagate("600519.SS", "2026-07-10")  # 贵州茅台，A 股交易日
print(decision)
```

自定义模型与辩论轮数（在桌面端侧栏或代码里任选提供商；以下仅为示例）：

```python
from invest_the_future.graph.trading_graph import InvestTheFutureGraph
from invest_the_future.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "dashscope"             # 示例；也可 deepseek / zhipu / ollama / openai_compatible 等
config["deep_think_llm"] = "qwen-plus"           # 深度推理模型（研究员辩论、最终决策）
config["quick_think_llm"] = "qwen-turbo"         # 快速模型（常规分析）
config["max_debate_rounds"] = 2
config["output_language"] = "中文"

ta = InvestTheFutureGraph(debug=True, config=config)
_, decision = ta.propagate("600519.SS", "2026-07-10")
print(decision)
```

> 用其它提供商时，把 `llm_provider` 与两个模型名换成对应值，并在 `.env` 配好该家 Key 即可；全部配置项见 `invest_the_future/default_config.py`。

## 持久化与恢复

### 决策日志

每次完成分析会追加到 `~/.tradingagents/memory/trading_memory.md`。同标的下次运行会注入近期决策与反思。路径可用 `TRADINGAGENTS_MEMORY_LOG_PATH` 覆盖。

> 说明：`~/.tradingagents/` 是沿用上游 TradingAgents 的目录名，本仓（ITF）继续共用，看到它不是装错了项目。

### 检查点续跑

可选开启 LangGraph checkpoint（检查点）：崩溃后从最近成功节点恢复。库文件在 `~/.tradingagents/cache/checkpoints/`。

```python
config = DEFAULT_CONFIG.copy()
config["checkpoint_enabled"] = True
```

## 可复现性说明

LLM 采样与实时新闻/社媒会导致同标的、同日期两次结果不完全一致，属研究工具常态。可降低 `temperature`（或 `TRADINGAGENTS_TEMPERATURE`）；推理模型往往忽略温度。回测收益不保证与任何公开数字一致，请将本系统视为多智能体研究脚手架，而非固定收益策略。

## 贡献

欢迎提交缺陷修复、文档与功能建议。

- **装上了 / 装不上 / 用法疑问**：优先来 [Discussions](https://github.com/cms19859230182-lang/TradingAgents-AGu-Edition-ITF/discussions) 报一声（成功失败都欢迎）。
- **明确 Bug / 功能请求**：用 [Issues](https://github.com/cms19859230182-lang/TradingAgents-AGu-Edition-ITF/issues/new/choose) 里的模板（**勿粘贴 API Key**）。
- 维护者向 GitHub 推送前请跑 `.\scripts\check_public_push.ps1`，并遵守 [公开仓边界](docs/PUBLIC_REPO_BOUNDARY.md)（公开仓只收桌面分析版，不含短卡/MCP 实验管线）。
- 也欢迎直接联系作者交流，微信号：`seteiro`。

## 引用

若本工作对你有帮助，请引用上游论文：

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework},
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138},
}
```
