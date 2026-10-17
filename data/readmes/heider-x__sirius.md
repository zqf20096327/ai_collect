<div align="center">

# Sirius — LLM 驱动的币安合约 AI 交易机器人

**AI Crypto Trading Bot for Binance USDⓈ-M Futures · LLM Agent · 趋势跟踪 · 自动风控**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-package_manager-black?logo=uv)](https://docs.astral.sh/uv/)
[![pytest](https://img.shields.io/badge/pytest-passing-green?logo=pytest)](tests/)
[![ruff](https://img.shields.io/badge/ruff-lint-orange?logo=ruff)](https://docs.astral.sh/ruff/)
[![mypy strict](https://img.shields.io/badge/mypy-strict-blue)](https://mypy-lang.org/)

*LLM 只做决策，代码做风控——让 AI 炒币，但不许它乱来。*

[快速开始](#-快速开始) · [核心特性](#-核心特性) · [架构](#%EF%B8%8F-架构) · [配置](#%EF%B8%8F-关键配置env) · [文档](#-文档) · [常见问题](#-常见问题-faq)

[English](README_EN.md)

</div>

> ⚠️ **风险提示**：本项目是实盘交易机器人，连接交易所真实 API，下单即花真钱。请先在测试网 / 小资金上充分验证，再考虑实盘。作者不对任何交易亏损负责。

## ✨ 核心特性

| 能力 | 说明 |
|---|---|
| 🔍 **AI 选股扫描** | 定时遍历候选池，主流币 + TradFi 股票永续双线；R:R≥3 才 LIMIT 试探开仓，同轮必挂整仓 STOP |
| 🛡️ **保护哨兵** | 常驻 WebSocket 用户数据流，成交后缺保护单自动按 2×ATR 补 STOP；灰尘 ATR 拒绝挂自杀单 |
| 📊 **持仓/挂单管理** | 有仓调保护单、有单清僵尸单，无仓无单直接跳过不烧 token |
| 🕰️ **TradFi 交易时段感知** | 美/韩/港/沪现货时段表 + 交易所 underlying 映射，非交易时段、平线、停牌自动跳过 |
| 💰 **手续费优化** | 系统级 maker 优先（LIMIT 挂单），TradFi 零 maker 费率红利照单全收 |
| 📒 **真相同步 + 对账** | 每分钟订单/成交/资金费落库，FIFO 重算账本；交易所 vs 本地三路比对，差异即告警 |
| 📲 **飞书推送** | 只推 WS 执行确认（挂单/成交/撤单/平仓）+ 账户总览卡片 + 安全告警，例行扫描零打扰 |
| 🔒 **Fail-closed 风控** | 杠杆、保证金模式、单笔上限全部由代码硬执行，LLM 想绕也绕不过 |

## 🏗️ 架构

```
tools/      37 个 LLM 可调工具（行情只读可并行，下单串行）+ 硬风控
brain/      有界 LLM/tool 循环（最多 64 步，防重复调用，配额错误秒级失败）
sync/       真相 ledger：拉取 → 去重 → FIFO → 落库
scheduler/  通用间隔调度（防重叠 + 单 tick 看门狗超时，卡死自动熔断）
notify/     飞书卡片/文本/账户总览（与业务解耦）
infra/      币安 REST/WS、MySQL 池（读写超时）、令牌桶限频
application/ jobs 编排 + 保护哨兵 + 对账 + Runtime 组装
```

LLM 看到的每一句话都由代码生成、可审计：[`docs/PROMPTS.md`](docs/PROMPTS.md)（改英文改源码，改中文改 `scripts/dump_prompts.py`，然后重跑生成脚本）。

## 🚀 快速开始

```bash
uv sync
cp .env.example .env   # 填 key，见下表
uv run python -m sirius doctor   # 四路自检：db / binance / llm / feishu
uv run sirius                    # 启动主循环
```

其他入口：`sirius-sync`（手动真相回放）、`sirius-feishu-setup`（飞书绑定二维码）。

## ⚙️ 关键配置（`.env`）

| 变量 | 说明 |
|---|---|
| `BINANCE_API_KEY` / `BINANCE_API_SECRET` | 合约 API（建议只开合约权限、关闭提现、绑定 IP） |
| `OPENAI_API_KEY` / `OPENAI_BASE_URL` / `OPENAI_MODEL` | OpenAI 兼容 LLM |
| `SIRIUS_MIN_AVG_TRADE_VALUE_USD` | 选币池流动性下限，默认 50 |
| `SIRIUS_TRADFI_ENABLED` | TradFi 通道总开关，默认 true |
| `SIRIUS_SCAN_INTERVAL_SECONDS` 等 | 各任务间隔，见 [`.env.example`](.env.example) |

## 📚 文档

- [`docs/PRD.md`](docs/PRD.md) — 产品需求
- [`docs/FUNCTIONAL_MAP.md`](docs/FUNCTIONAL_MAP.md) — 功能唯一来源
- [`docs/DEV_PLAN.md`](docs/DEV_PLAN.md) — 开发计划
- [`docs/PROMPTS.md`](docs/PROMPTS.md) — LLM 提示词总览（代码生成）

## ❓ 常见问题 FAQ

**Q: 策略逻辑是什么？**
A: 趋势跟踪 + 试探加仓：只做趋势不做震荡，首仓试探、浮盈才加、绝不补亏；每单 R:R≥3，止损在真支撑阻力外约 1.5–2 倍 ATR；不设固定止盈，STOP 先保本再跟随。详见 `docs/PROMPTS.md` 的资金原则。

**Q: LLM 会不会乱下单？**
A: 不会。LLM 只能调工具，所有硬约束（杠杆上限、保证金模式、单笔名义上限、开仓必跟 STOP）都在工具层 fail-closed 执行，不满足直接拒绝并返回结构化错误。

**Q: 支持哪些市场？**
A: 币安 U 本位永续（主流币 + TradFi 股票/指数永续，可一键开关）。TradFi 自带美/韩/港/沪交易时段感知。

**Q: 需要多少资金起步？**
A: 单笔只冒总资金一小部分（可在风控配置里调）。建议先测试网或小资金跑至少一个月，观察 sync 对账零差异后再加仓。

**Q: 飞书推送会很吵吗？**
A: 不会。例行扫描/管理只记日志不推送；你只会收到成交执行确认、账户总览和安全告警。

## 🛠️ 开发

```bash
uv run pytest -q        # 全量测试
uv run ruff check src tests && uv run ruff format --check src tests
uv run mypy src/sirius  # strict
uv run python scripts/dump_prompts.py   # 改 prompt 后重跑
```

---

*关键词：AI trading bot, crypto trading bot, Binance futures bot, LLM agent, quantitative trading, 量化交易, 合约机器人, AI 炒币, TradFi, 飞书推送*
