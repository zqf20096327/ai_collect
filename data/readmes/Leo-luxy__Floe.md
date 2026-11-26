<p align="center">
  <img src="static/icons/floe_icon_bull.png" alt="Floe Bull Icon" width="92">
  &nbsp;&nbsp;&nbsp;
  <img src="static/icons/floe_icon_bear.png" alt="Floe Bear Icon" width="92">
</p>

<h1 align="center">Floe（原 GP_ANA）</h1>

<p align="center">
  <b>适合中国宝宝体质的 A 股选股与 AI 量化工作台</b><br>
  <sub>当前版本：<b>v2.1.0</b> ｜ <b>中文</b> · <a href="README_EN.md">English</a></sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-v2.1.0-2563eb.svg" alt="Version">
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-0f172a.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Distribution-Desktop%20%7C%20Homebrew%20%7C%20npm%20%7C%20Source-059669.svg" alt="Distribution">
  <img src="https://img.shields.io/badge/AI-DeepSeek%20%2F%20OpenAI%20API%20%7C%20Ollama-ea580c.svg" alt="AI">
  <img src="https://img.shields.io/badge/Python-3.9--3.12-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## 📖 这是什么

**Floe**（前身 **GP_ANA**）是一套运行在你自己电脑上的 **A 股趋势选股与多维 AI 投资决策软件**。

它把散落在各处的股票信息——全市场日线筛选、前复权行情、财报质量、主力资金流、融资融券、股东筹码、机构研报——自动拉取并做严格时效与指纹校验，再通过 **云端大模型 API（默认推荐 DeepSeek，兼容任意 OpenAI 接口）** 或 **本地 Ollama 模型** 进行五维交叉核验，结合你的真实持仓成本生成可执行的情景交易计划。

**一句话概括：用量化纪律管住手，把原本要翻十几个网页、看几十页财报才能拼出的判断，浓缩进一个干净顺手的桌面工作台。**

> **🚀 想直接开箱即用？** 跳到 **[快速安装（桌面版 / Homebrew / npm）](#-快速安装与启动四种方式任选)**，下载安装包或一行命令即可启动，**无需折腾 Python 环境**。
>
> **🛠️ 想从源码部署或二次开发？** 跳到 **[方式 D：从源码完整部署](#方式-d从源码完整部署适合二次开发与脚本定制)**，10 步手把手跑通。
>
> **📐 想了解内部架构与算法细节？** 阅读 **[Introduction.md](Introduction.md)** —— 五维权重、两层冲突推理、选股快照隔离、回测身份校验与完整 API 文档。

---

## ✨ 核心特性（v2.0.0 全新升级）

### 1️⃣ 三步主线量化闭环：选股 → 关注池 → 回测监控

告别松散脚本堆砌，工作台围绕实盘每日复盘动线重构为清晰的三步流水线：

```
01 市场选股                      02 关注股票池                      03 策略回测与监控
──────────────────────          ──────────────────────            ──────────────────────
Tushare 全市场 5000+ 扫描  ──▶   沉淀核心自选标的            ──▶    默认简化版 (MA5 > MA20)
整批冻结唯一交易日快照             实时同步回测信号徽章                 对称入离场 + 3 日冷却期
仅展示「当日新入场」标的           行内改名 · 一键跳图表/研判/记账       本机历次选股表现追踪
```

- **只看真信号**：`01 市场选股` 默认严格过滤 `入场日期 == 数据截止日` 的**当日新触发标的**，自动剔除早期入场的存量持仓副产物与北交所股票；每次成功批次自动归档至 `selection_history/<YYYYMMDD>/` 供随时复盘。
- **贴合实战的默认策略**：`03 策略回测与监控` 默认启用胜率响应更敏捷的**简化版趋势策略（`MA5 > MA20`）**，保留完整版四线多头一键切换；新增**「本机历次选股表现追踪」**，自动统计你在这台电脑上筛出的每只新入场股票自首次入选日起的真实回测累计收益。

### 2️⃣ 五维研判 + 两层 AI 冲突决策 —— 先“吵架”，再下单

单看 K 线容易踩基本面暗雷，单看财报又容易买在下跌中继。Floe 同时评估五个维度，每个维度先产出标准化的结构化 JSON 摘要：

| 维度 | 默认权重 | 核心回答的问题 |
|:---|--:|:---|
| 📈 **技术趋势** | **40%** | 当前是否处于确认上升趋势？是否超买超卖？关键支撑/阻力位在哪？ |
| 💰 **财务质量** | 25% | 利润含金量（经营现金流）如何？ROE 与增长可持续吗？负债率危险吗？ |
| 🌡️ **情绪估值** | 15% | 主力资金在净流入还是撤退？PE/PB 处于历史什么分位？ |
| 🏢 **股东结构** | 10% | 股东户数在集中还是发散？北向与长线机构在增持还是减仓？ |
| 📰 **研报观点** | 10% | 近期机构评级分布如何？一致预期盈利是上修还是下调？ |

在此之上采用独创的**「技术为主、其他避雷」+ 两层 LLM 推理机制**：

```
第一层：多维冲突检测（角色：对冲基金风险经理）
  专门把五个维度中【相互矛盾】的结论拎出来推理，拒绝和稀泥式的全文摘要
          ↓ 仅向下传递核心冲突结论 + 你的真实 FIFO 持仓成本与浮盈亏
第二层：情景交易计划（角色：交易教练）
  硬性约束：禁止给模棱两可的套话，必须输出“如果……就……”的可执行风控价格树
```

### 3️⃣ 云端 DeepSeek / OpenAI API + 本地 Ollama 双模驱动

- **零显卡门槛（推荐）**：在「系统设置 → AI 与数据源」中填入 **DeepSeek**、硅基流动（SiliconFlow）、通义千问、Moonshot 或任意 OpenAI 兼容接口的 API Key，点击**「连接并拉取模型列表」**通过两步真实验证后即可保存，全项目 20+ 个分析脚本自动无缝接管，无需改动任何代码。
- **全本地隐私模式**：同样支持一键切回本机 **Ollama**（`http://localhost:11434`），数据 100% 留在本机内存。

### 4️⃣ 三位小数（`0.001` 元）FIFO 实盘买卖台账

- 完整支持 ETF、可转债及低价 A 股的**分厘级（三位小数，如 `15.825` 元）**成交价录入与展示。
- 按 **FIFO（先进先出）** 逐手自动配对历史平仓手次与当前未平仓底仓，顶部实时汇总**账户累计总收益、已落袋实现盈亏、当前持仓浮动盈亏**，点击任意股票行即可展开查看每一手买卖明细，并自动将真实持仓均价注入第二层 AI 决策。

### 5️⃣ 原生跨平台桌面体验与贴心细节

- **独立窗口 + 菜单栏常驻**：基于 `pywebview` 原生系统渲染引擎打包（无臃肿 Chromium 内核），macOS 配备黑白极简小企鹅菜单栏状态图标，Windows / Linux 配备系统托盘。
- **红涨 / 绿跌双企鹅应用图标**：内置「📈 红涨昂首瞭望款」与「📉 绿跌委屈闭眼款」两套高清无边框圆角图标，可在设置中一键切换（同步更新左上角、网页 Favicon 及 macOS Dock 图标）。
- **中英双语 + 浅色/深色主题**：支持 `简体中文 / English` 即时切换；切为英文后，后续新生成的 AI 个股与板块研报也会自动以专业英文输出。
- **自动端口避让 + 离线静态资源 + 一键 ZIP 备份**：默认安全监听 `127.0.0.1:3130`（被占用时自动顺延至 `3131+`）；内置离线前端依赖包，无外网 CDN 阻塞；支持配置、自选股与台账一键导出/导入备份。

---

## 🖥️ 软件运行截图（v2.0.0 实机展示）

> 以下截图均采自 **Floe v2.0.0** 隔离演示环境（公开蓝筹合成示例数据）。

### 01 市场选股筛查台 & 02 关注股票池指挥台
<p align="center">
  <img src="assets/screenshots/01_market_screener.png" alt="01 市场选股筛查台" width="49%">
  <img src="assets/screenshots/02_watchlist_pool.png" alt="02 关注股票池指挥台" width="49%">
</p>

### 03 策略回测实时监控 & 个股五维两层 AI 研判中心
<p align="center">
  <img src="assets/screenshots/03_strategy_backtest.png" alt="03 策略回测与实时监控" width="49%">
  <img src="assets/screenshots/04_ai_research_hub.png" alt="个股五维两层 AI 研判中心" width="49%">
</p>

### 三位小数 FIFO 买卖记录台账 & 系统设置（双企鹅图标 · 语言 · 权限体检）
<p align="center">
  <img src="assets/screenshots/05_trading_ledger_fifo.png" alt="三位小数 FIFO 买卖记录台账" width="49%">
  <img src="assets/screenshots/06_settings_and_icons.png" alt="系统设置与双图标切换" width="49%">
</p>

### 深色英文工作台（Dark + EN） & 趋势回测信号 K 线图
<p align="center">
  <img src="assets/screenshots/07_dark_en_workbench.png" alt="深色英文工作台模式" width="49%">
  <img src="assets/screenshots/08_backtest_kline_chart.png" alt="趋势跟踪回测信号与资金曲线图" width="49%">
</p>

---

## 🚀 快速安装与启动（四种方式任选）

### 方式 A：直接下载桌面安装包（最省心 · 零环境依赖）

前往 **[GitHub Releases](https://github.com/Leo-luxy/Floe/releases)** 下载对应系统的安装包，双击即可运行，**无需安装 Python 或 TA-Lib**：

| 操作系统 | 安装包格式 | 安装与首次打开说明 |
|:---|:---|:---|
| **macOS**（Apple Silicon / Intel） | `Floe-v2.1.0-macos-*.dmg` | 打开 DMG 将 `Floe.app` 拖入「应用程序」。若首次打开提示“无法验证开发者”，在终端执行一次：<br>`xattr -cr /Applications/Floe.app` |
| **Windows 10 / 11**（x64） | `Floe-v2.1.0-windows-x64.zip` | 解压后运行目录内的 `Floe.exe`（可右键发送到桌面快捷方式） |
| **Linux**（Ubuntu 22.04+ 等 x64） | `Floe-v2.1.0-linux-x86_64.AppImage` | 赋予可执行权限后直接运行：<br>`chmod +x Floe-*.AppImage && ./Floe-*.AppImage` |

> 💾 **升级不丢数据**：桌面打包版的个人配置、自选股、交易台账与行情缓存全部自动隔离存储在系统用户数据目录（macOS 为 `~/Library/Application Support/Floe`，Windows 为 `%APPDATA%\Floe`，Linux 为 `~/.local/share/floe`），覆盖升级安装包绝不丢失数据。

---

### 方式 B：Homebrew 一行安装（macOS 推荐）

```bash
brew tap Leo-luxy/tap
brew install --cask floe
```

升级版本只需 `brew upgrade --cask floe`（若提示未公证拦截，可加 `--no-quarantine` 参数安装）。

---

### 方式 C：npm 全局命令行安装（跨平台开发者推荐）

电脑装有 Node.js（`>= 18`）即可一键安装 `floe` 全局命令，自动拉取对应系统架构的预编译桌面运行时：

```bash
npm install -g @leo-luxy/floe

# 启动原生桌面窗口
floe

# 或以纯本地浏览器模式启动（支持自定义端口）
floe --web --port 3130

# 运行环境与权限自检
floe --doctor
```

---

### 方式 D：从源码完整部署（适合二次开发与脚本定制）

> 全程约 10–15 分钟，适合希望直接修改策略代码、调参或用命令行跑批处理的开发者。

#### 第 0 步：确认系统与 Python 版本

| 项目 | 要求 | 说明 |
|:---|:---|:---|
| **操作系统** | macOS / Linux / Windows | 三端均完整支持 |
| **Python** | **3.9 ~ 3.12**（推荐 **3.10 / 3.11**） | ⚠️ `numpy==1.26.3` 暂不提供 Python 3.13 预编译包 |
| **内存** | ≥ 8 GB | 使用云端 DeepSeek API 仅需 8 GB；跑本地 32B 模型建议 ≥ 32 GB |
| **网络** | 能直连国内财经站点 | 东方财富 / 新浪财经 / akshare / Tushare（内置直连守护自动绕过系统代理） |

如果系统默认 Python 版本不合适，推荐用 Conda 或 `venv` 创建独立 Python 3.10 环境：

```bash
conda create -n floe python=3.10 -y
conda activate floe
```

#### 第 1 步：克隆仓库

```bash
git clone https://github.com/Leo-luxy/Floe.git
cd Floe
```

#### 第 2 步：安装 TA-Lib C 语言底层库（源码部署关键一步）

`utils.py` 优先调用 `TA-Lib` 高速计算 40+ 项技术指标，**必须先装系统级 C 库，再装 Python 依赖**：

- **macOS**：
  ```bash
  brew install ta-lib
  ```
- **Ubuntu / Debian**：
  ```bash
  sudo apt-get update && sudo apt-get install -y build-essential wget
  wget https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib-0.6.4-src.tar.gz
  tar -xzf ta-lib-0.6.4-src.tar.gz && cd ta-lib-0.6.4
  ./configure --prefix=/usr && make && sudo make install && cd ..
  ```
- **Windows**：从 [cgohlke/talib-build Releases](https://github.com/cgohlke/talib-build/releases) 下载对应 Python 版本与位数的 `.whl` 安装：
  ```bash
  pip install TA_Lib-0.6.8-cp310-cp310-win_amd64.whl
  ```

验证安装成功：
```bash
python -c "import talib; print(talib.__version__)"
```

#### 第 3 步：安装 Python 依赖

```bash
pip install -r requirements.txt
```

> 如希望在源码环境下也使用独立原生窗口启动（`python floe_app.py`），可额外安装桌面壳可选依赖：`pip install pywebview pystray`。

#### 第 4 步：启动 Floe 工作台

```bash
# 方式 1：启动 Web 服务（默认仅本机安全监听 http://127.0.0.1:3130）
python web_ui.py

# 方式 2：启动原生桌面窗口（需已装 pywebview，未装会自动在默认浏览器打开）
python floe_app.py
```

启动时如果仓库内尚无 `config.py`、`data/`、`log/`，系统会**自动用 `config.example.py` 初始化并建好所需目录**；如果 `3130` 端口恰好被其它程序占用，会自动向后顺延到 `3131` 等空闲端口并在终端打印实际访问地址。

打开浏览器访问：**`http://127.0.0.1:3130`**

#### 第 5 步：在界面「⚙️ 系统设置」完成一键配置（无需手改代码！）

首次打开界面会自动弹出引导，你也可以随时点击左下角 **「⚙️ 系统设置 → AI 与数据源」**：

1. **配置 AI 大模型（二选一）**：
   - **推荐 · 云端 API（DeepSeek / OpenAI 兼容）**：选择预设服务商（如 DeepSeek），粘贴你的 API Key → 点击 **「1. 连接并拉取模型列表」** → 在下拉框选择模型（如 `deepseek-chat`）→ 点击 **「2. 保存 AI 配置」**。
   - **备选 · 本地 Ollama**：先在终端执行 `ollama serve` 与 `ollama pull qwen3:8b`，在设置中切到「本地 Ollama」检测连接并选择模型保存即可。
2. **配置 Tushare Token（仅「01 市场选股」需要）**：
   - 注册登录 [tushare.pro](https://tushare.pro/) 获取接口 Token（全市场日线 `pro.daily()` 需 **120 积分以上**）。
   - 直接粘贴到设置页「Tushare Pro 数据源配置」点击「验证并保存 Token」（支持填写多个备用 Token，主 Token 限流时自动无缝切换；保存在本地忽略的 `user_settings.json` 中，绝不会污染 Git 仓库）。

---

## 🧭 日常复盘与功能使用指南

| 模块 | 核心用途 | 预计耗时 | 使用要点 |
|:---|:---|:---|:---|
| **01 · 市场选股** | 全市场 5000+ 股票趋势扫描 | 3–5 分钟 | 需配置 Tushare Token。18:00 前按上一交易日快照，18:00 后按当日；列表仅聚焦展示**当日新入场标的**，可一键加入关注池 |
| **02 · 关注股票池** | 核心自选股信号总览与调度 | 即时 | 自动同步最新回测信号（`可入场` / `持有` / `观望`），点击名称旁的 `✎` 可直接改名，一键直达回测图、AI 研判或记账 |
| **03 · 策略回测与监控** | 关注池趋势回测与纪律监控 | 1–2 分钟 | 默认启用**简化版（`MA5 > MA20`）**；支持查看实时监控报告、**本机历次选股表现追踪**及逐股 K 线买卖点图表（支持键盘 `←` `→` 翻图） |
| **⚡ 个股 AI 研判** | 快速技术复盘 / 五维完整排雷 | ~30 秒 / 3–5 分钟 | 日常盯盘选「快速技术研判」（支持短/中/长周期视角）；重仓建仓前选「五维两层完整决策」做全量基本面排雷与持仓计划 |
| **🌐 板块与指数 AI** | 大盘与申万/东财行业轮动研判 | 2–3 分钟 | 首次使用先点「⬇ 更新数据」（约 1 分钟），随后即可对大盘指数、行业板块、港股指数做超额收益与趋势研判 |
| **📝 买卖记录台账** | 三位小数实盘记账与 FIFO 核算 | 即时 | 录入每笔实盘买入/卖出（精确到 `0.001` 元），自动计算已落袋收益与实时持仓浮盈，并为 AI 第二层决策提供真实成本 |
| **📚 报告归档中心** | 历史 Markdown 研报检索阅读 | 即时 | 按股票分组归档历次五维决策、技术趋势、财务、估值、股东与研报分析报告 |
| **⚙️ 系统设置** | AI / Token / 图标 / 语言 / 备份 | 即时 | 切换红涨/绿跌企鹅图标、中英双语、桌面通知权限与网络策略体检、一键导出/导入全量个人数据 `.zip` 备份 |

---

## 💻 命令行速查（供进阶与自动化定时任务使用）

```bash
# 1. 启动服务与桌面端
python web_ui.py                                              # 启动 Web 服务 (默认 127.0.0.1:3130，冲突自动顺延)
GP_ANA_WEB_PORT=8090 python web_ui.py                         # 指定自定义端口启动
python floe_app.py                                            # 启动原生桌面独立窗口
python floe_app.py --doctor                                   # 命令行打印运行环境与目录诊断 JSON

# 2. 单股 / 批量数据更新检查（严格核验内容日期与 SHA256 指纹）
python check_data_updates.py --mode daily    --ticker 300750.SZ   # 日更数据（行情/资金流/两融/估值/指标）
python check_data_updates.py --mode periodic --ticker 300750.SZ   # 低频数据（公司信息/财报/股东/北向）

# 3. 批量多维分析
python batch_analyze.py --mode daily    --ticker 300750.SZ        # 日更维度（6 步）
python batch_analyze.py --mode periodic --ticker 300750.SZ        # 低频维度（3 步）
python batch_analyze.py --mode all      --ticker 300750.SZ        # 完整全维度流程（14 步）

# 4. 趋势跟踪回测与实时监控
python backtest_all_stocks.py --mode simple                       # 关注池简化版策略回测 + 监控报告
python backtest_all_stocks.py --mode full                         # 关注池完整版四线多头回测 + 监控报告

# 5. 全市场四步选股流水线
python stocks_filter/step1_daily.py                               # Step 1: 全市场日线
python stocks_filter/step2_daily_basic.py                         # Step 2: 合并换手率/市值/PE/PB
python stocks_filter/step3_filter.py                              # Step 3: 多条件初筛
python stocks_filter/batch_backtest_filter.py                     # Step 4: 隔离快照批量回测精筛 → final_holdings.csv

# 6. 运行全套回归单元测试（309 项）
python -m unittest discover -s tests -t .
```

---

## 🔧 常见问题排查（FAQ）

<details>
<summary><b>Q1: macOS 首次打开 Floe.app 提示“已损坏”或“无法验证开发者”怎么办？</b></summary>

这是因为开源免费分发包未购买 Apple 付费企业公证签名，macOS Gatekeeper 默认会拦截首次从浏览器下载的应用。只需打开「终端」执行一行命令移除隔离属性即可永久正常双击打开：
```bash
xattr -cr /Applications/Floe.app
```
</details>

<details>
<summary><b>Q2: 默认端口 3130 如果在别的电脑上被占用了怎么办？</b></summary>

**完全不用手动处理。** Floe 内置了双阶段套接字可用性探测（`pick_available_port`）：若 `3130` 已被其它软件监听或受权限限制，会自动向后顺延绑定 `3131`、`3132`……并在控制台打印真实 URL，桌面窗口也会自动打开实际绑定的端口。如需固定端口，可设置环境变量 `GP_ANA_WEB_PORT=端口号`。
</details>

<details>
<summary><b>Q3: 为什么我配置了 AI API Key 却不能直接点“保存”？</b></summary>

为了彻底杜绝因模型名拼写错误或余额不足导致跑了 5 分钟采集后在最后一步报错，Floe 采用**两步强制校验**：粘贴 API Key 后请先点 **「1. 连接并拉取模型列表」**，真实连通网关并从下拉框选中可用模型后，「2. 保存 AI 配置」按钮会自动解锁。
</details>

<details>
<summary><b>Q4: 市场选股提示 Tushare 权限或积分不足？</b></summary>

全市场日线接口 `pro.daily()` 要求 Tushare 账号达到 **120 积分以上**。请登录 [tushare.pro](https://tushare.pro/) 完善个人资料或完成积分任务后再试；若有多个账号，可在「系统设置」的备用 Token 栏每行填一个，触发限流时会自动无缝切换。
</details>

<details>
<summary><b>Q5: 开着 VPN / 科学上网软件时抓取国内行情超时？</b></summary>

Floe 内置了 `net_guard.py` 网络守护，默认对东方财富、新浪财经、Tushare 等国内数据源走**直连模式**（自动忽略进程级系统代理环境变量）。若使用了 TUN/全局网卡接管模式导致国内站点不通，建议将 `eastmoney.com`、`sina.com.cn`、`tushare.pro` 加入代理软件的直连白名单，或在「系统设置 → 语言·权限·更新」中切换网络连接策略。
</details>

<details>
<summary><b>Q6: 源码安装 `pip install TA-Lib` 报错找不到 `ta_lib.h`？</b></summary>

这是因为尚未安装底层 C 库。请先按上方 [第 2 步](#第-2-步安装-ta-lib-c-语言底层库源码部署关键一步) 安装对应系统的 `ta-lib` 系统库，再执行 `pip install TA-Lib==0.6.8`。
</details>

---

## 🔒 安全与隐私设计

1. **默认仅本机回环监听，零局域网暴露**：`web_ui.py` 与桌面端默认绑定 `127.0.0.1:3130` 且强制 `debug=False`，不向局域网其他设备开放端口，也不暴露 Werkzeug 调试器。
2. **敏感凭据与持仓本地隔离**：通过界面配置的 API Key、Tushare Token、自选股与实盘交易记录均保存在被 `.gitignore` 严格排除的本地文件（或系统级用户数据目录）中；备份恢复采用 AST 白名单字面量语法树解析，杜绝恶意代码注入。
3. **最小系统权限原则**：Floe **不请求**摄像头、麦克风、通讯录、定位或辅助功能等任何隐私权限，仅需本地数据目录读写、出站行情网络请求及可选的任务完成桌面通知。

---

## 📮 反馈与联系

使用过程中遇到问题、发现 Bug，或者有新策略与功能建议，欢迎随时联系作者：

- **📧 作者邮箱**：**[luleo856@gmail.com](mailto:luleo856@gmail.com)**
- **🐙 GitHub Issues**：**[https://github.com/Leo-luxy/Floe/issues](https://github.com/Leo-luxy/Floe/issues)**

来信或提 Issue 时附上操作系统版本、功能模块截图及报错末尾日志（或运行 `floe --doctor` 的输出），能帮助更快定位问题。

---

## 📄 版本历史

| 版本 | 日期 | 主要变更 |
|:---|:---|:---|
| **v2.1.0** | 2026-11 | 新增前后端全局单任务运行互斥保护与 `/api/active_task` 实时状态接口；运行中任务按钮动态显示「正在进行……」加载态，点击其他任务即时弹出实时进度条与快捷跳转弹窗（刷新自动恢复）；修复 Homebrew Cask `arch` 声明被哈希脚本误覆盖的问题；**343 项**回归测试 |
| **v2.0.3** | 2026-11 | 强制子进程与启动器全局 UTF-8 标准流及 UTF-8/GB18030 双编码解码兜底，彻底修复 Windows 版选股中文乱码与 `batch_backtest_filter.py` 预检编码崩溃（退出码 3）；加固打包态 `config.py` 自动模板兜底；**339 项**回归测试 |
| **v2.0.2** | 2026-11 | 新增统一数据中心 `data_hub`（35 项能力路由、能力级源熔断、全市场共享缓存与多源降级）；两融改单股直查（0.2s）及非标的 7 日跳过；前复权 4 级兜底与 `mini-racer` 依赖修正；修复云端 API 长响应 3s 超时截断与股东季度时效误判；**336 项**回归测试 |
| **v2.0.1** | 2026-11 | 修复跨平台桌面安装包 HTTPS 根证书链校验（内置并自动挂载 `certifi` 与系统 CA 证书束）；新增检查 GitHub 更新与境外 API 的无污染局部系统代理回退；新增 Windows 受控目录（`WinError 5`）自动便携目录降级；311 项回归测试 |
| **v2.0.0** | 2026-11 | **品牌焕新为 Floe**；全新三步闭环量化工作台；跨平台独立桌面应用（macOS / Windows / Linux）与 Homebrew / npm 分发；DeepSeek / OpenAI 云端 API 两步校验接入 + Ollama 双引擎；三位小数（`0.001`）FIFO 买卖台账；本机历次选股表现追踪；红涨/绿跌双企鹅图标、中英双语界面与英文研报输出、自动端口顺延（`3130`）与一键 ZIP 备份；309 项回归测试 |
| **v1.6.0** | 2026-11 | 选股整批统一交易日与每日留存、回测产物身份校验（参数/来源/内容指纹）、失败可观测与降级闭环、Tushare 主备 Token 自动切换、策略参数单一来源 |
| **v1.5.0** | 2026-09 | 文档体系重构为 README + Introduction 两册、回测页默认显示最新报告、任务状态持久化、依赖清单修正 |
| **v1.4.0** | 2026-06 | 市场选股 + 自选股管理、标准 9 日 EMA KDJ 与板块时效性修复、回测增强 |
| **v1.3.0** | 2026-06 | 板块与指数 AI 分析：四大类型板块研判、新浪财经数据源、sector API |
| **v1.2.0** | 2026-05 | 架构重构：统一批量入口、`Process/` 五维引擎、两层冲突决策、快速分析、趋势回测系统 |
| **v1.1.0** | 2026-03 | Web 界面、12 个新采集器、5 个新分析引擎 |
| **v1.0.1** | 2026-02 | 初版数据采集与基础分析框架 |

完整变更细节见 **[CHANGELOG.md](CHANGELOG.md)**。

---

## 👥 贡献者与相关文档

- **作者 / 维护者**：**[Leo-luxy](https://github.com/Leo-luxy)**（产品设计、量化策略、全栈工程实现与验证）
- **相关文档**：
  - [**Introduction.md**](Introduction.md) —— 系统架构、五维决策算法、模块档案、数据字典与全量 REST API 参考
  - [**README_EN.md**](README_EN.md) —— English Documentation
  - [**CHANGELOG.md**](CHANGELOG.md) —— 版本演进日志
  - [**packaging/PUBLISH_GUIDE.md**](packaging/PUBLISH_GUIDE.md) —— 桌面端多平台打包与 Homebrew / npm 发布指南
  - [**CONTRIBUTING.md**](CONTRIBUTING.md) ｜ [**SECURITY.md**](SECURITY.md) ｜ [**CODE_OF_CONDUCT.md**](CODE_OF_CONDUCT.md)

---

## 📜 许可证与免责声明

本项目采用 **[MIT License](LICENSE)** 开源。

**⚖️ 免责声明**：本软件及文档仅为**个人量化研究与技术学习工具**。软件内生成的所有选股名单、回测绩效、AI 分析报告及交易计划**均不构成任何证券投资建议**。股市有风险，入市需谨慎，使用者依据本软件做出的任何投资决策及盈亏后果均由使用者本人独立承担。

<p align="center">
  <sub>Made with ❤️ for A-Share quantitative investors · <b>Floe v2.1.0</b></sub>
</p>
