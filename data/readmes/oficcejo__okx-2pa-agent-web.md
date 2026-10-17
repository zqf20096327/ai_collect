# okx-2pa-agent-web

`okx-2pa-agent-web` 是一个面向 OKX 的 AI 交易 Web 程序。程序从 OKX 获取加密货币及 OKX 已支持的 TradFi 产品行情，支持黄金、原油、美股等，通过 OpenAI 兼容 LLM 完成两阶段价格行为分析，并在通过数量、信号时效、持仓状态和实盘解锁等风控检查后提交订单。

> 风险提示：本项目不构成投资建议。自动交易可能造成实际资金损失，请先使用模拟盘验证，并从最小订单数量开始，如造成任何损失，请自行承担。
> <img width="1887" height="855" alt="image" src="https://github.com/user-attachments/assets/3fdcb1c5-3e8a-4452-8bda-75b8073fc9b0" />

**👉 [部署视频教程](https://www.bilibili.com/video/BV14hgx65EzR)**

**理论基础视频：**

- [ICT 2022理论终极拆解](https://www.bilibili.com/video/BV1pRAszYELi)
- [订单流交易实战](https://www.bilibili.com/video/BV152AHzGEA1)

**🎮 **Discord 交流群**：[https://discord.gg/jk4mnW53gK](https://discord.gg/jk4mnW53gK)**

- 已经使用rust重构并发布win11单文件运行版，无需复杂部署，无需环境支持，开箱即用。右侧releases可下载，或到rust仓库下载https://github.com/oficcejo/2pa-agent-rust
## 功能

- OKX 现货、永续合约及 TradFi 产品搜索
- OKX K 线与浏览器蜡烛图
- OpenAI 兼容 LLM 两阶段价格行为分析
- 支持 DeepSeek、LongCat 及其他 OpenAI 兼容服务
- 账户权益曲线、资产、仓位和挂单查询
- 手动 AI 分析及分析后按风控执行
- 后台自动分析与自动交易
- 决策记录、交易记录及单条删除
- 模拟盘、实盘多重解锁保护
  
## 环境要求

- Python 3.11 或更高版本
- 能访问 `https://www.okx.com` 和所配置的 LLM API
- 仅查看公共行情时可以不配置 OKX API；账户查询和交易必须配置

## 注册获取 OKX API

1. **注册 OKX**：[点击okx官网注册,佣金享5%优惠](https://www.gtohfmmy.com/join/6746503)
   - 使用上面邀请码注册并完成任务，最高获 100 USDT 奖励，交易佣金优惠 5%。具体奖励、地区限制和活动规则以 OKX 页面显示为准。
2. 登录 OKX，点击右上角个人中心，进入“API 管理”，创建 API。
3. API 权限至少需要“读取”；需要下单时增加“交易”权限。
4. **不要授予提现权限**。建议设置服务器公网 IP 白名单。
5. 妥善保存 `API Key`、`Secret Key` 和创建时填写的 `Passphrase`，关闭页面后部分信息可能无法再次查看。
6. 资金需要划转到交易账户后才能用于交易。模拟盘和实盘应分别创建对应环境的 API Key。

<img width="1635" height="795" alt="OKX API 创建示意图" src="https://github.com/user-attachments/assets/66a8685f-e428-4fb8-afc9-efde9053a223" />

## 安装（中国大陆用户本地部署要求科学上网环境，推荐购买美国虚拟vps部署）

### Windows

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

启动：

```powershell
.\venv\Scripts\python.exe -m pa_agent.web.main --host 127.0.0.1 --port 8088
```

也可以双击 `start_web.bat`。安装项目后还可以运行：

```powershell
python -m pip install -e .
okx-2pa-agent-web --host 127.0.0.1 --port 8088
```

浏览器打开 `http://127.0.0.1:8088`。

### Linux 快速安装

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
git clone <你的仓库地址> okx-2pa-agent-web
cd okx-2pa-agent-web
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
nano .env
```

本机测试启动：

```bash
./venv/bin/python -m pa_agent.web.main --host 127.0.0.1 --port 8088
```

服务器临时直接访问可以使用：

```bash
./venv/bin/python -m pa_agent.web.main --host 0.0.0.0 --port 8088
sudo ufw allow 8088/tcp
```

然后访问 `http://服务器IP:8088`。Linux 服务器推荐使用宝塔面板部署，详细步骤请查看本文开头的部署视频教程。公网使用时请同时配置访问保护和防火墙规则。

## `.env` 详细配置

复制示例文件后编辑：

```bash
cp .env.example .env
chmod 600 .env
```

`.env` 位于项目根目录。修改后必须重启服务。不要把 `.env` 提交到 Git、截图公开或发给其他人。

### LLM 配置

`.env.example` 参照当前环境，默认填写 LongCat 兼容接口、`LongCat-2.0` 和关闭思考模式；密钥保持为空。需要使用 DeepSeek 时可按下面示例替换。

DeepSeek 示例：

```dotenv
LLM_API_KEY=你的DeepSeek_API_Key
LLM_BASE_URL=https://api.deepseek.com
LLM_MODEL=deepseek-chat
LLM_THINKING=true
LLM_REASONING_EFFORT=high
LLM_CONTEXT_WINDOW=128000
LLM_STAGE_TIMEOUT_SECONDS=240
```

其他 OpenAI 兼容服务示例：

```dotenv
LLM_API_KEY=服务商提供的API_Key
LLM_BASE_URL=https://服务商提供的兼容接口地址
LLM_MODEL=服务商提供的模型ID
LLM_THINKING=true
LLM_REASONING_EFFORT=high
LLM_CONTEXT_WINDOW=128000
LLM_STAGE_TIMEOUT_SECONDS=240
```

| 参数 | 说明 |
| --- | --- |
| `LLM_API_KEY` | LLM 服务商的 API Key。 |
| `LLM_BASE_URL` | OpenAI 兼容接口根地址。是否包含 `/v1` 或其他路径以服务商文档为准。 |
| `LLM_MODEL` | 模型 ID，必须与当前 API Key 和接口地址匹配。 |
| `LLM_THINKING` | 是否请求思考模式。服务商不支持时设为 `false`。 |
| `LLM_REASONING_EFFORT` | 思考强度：`low`、`medium`、`high` 或 `max`。实际支持情况取决于模型。 |
| `LLM_CONTEXT_WINDOW` | 模型上下文窗口，用于控制提示词和输出预算。 |
| `LLM_STAGE_TIMEOUT_SECONDS` | 每个分析阶段最大等待秒数，范围 `30-1800`。网络较慢或思考模型可适当增加。 |

出现 `401` 时，优先检查 API Key、接口地址和模型 ID 是否属于同一服务商。出现超时时，可以增加 `LLM_STAGE_TIMEOUT_SECONDS`，同时检查服务商额度和网络。

### OKX API 凭据

```dotenv
OKX_API_KEY=你的OKX_API_Key
OKX_SECRET_KEY=你的OKX_Secret_Key
OKX_PASSPHRASE=创建API时填写的Passphrase
OKX_BASE_URL=https://www.okx.com
```

| 参数 | 说明 |
| --- | --- |
| `OKX_API_KEY` | OKX API Key。 |
| `OKX_SECRET_KEY` | OKX Secret Key，不是登录密码。 |
| `OKX_PASSPHRASE` | 创建 API 时自行设置的口令。 |
| `OKX_BASE_URL` | OKX REST API 地址，通常保持 `https://www.okx.com`。 |

三个凭据必须来自同一个模拟盘或实盘环境。若设置了 IP 白名单，Linux 服务器的公网出口 IP 必须在白名单中。

### 模拟盘配置

建议首次部署使用：

```dotenv
OKX_DEMO_TRADING=true
OKX_AUTO_TRADING_ENABLED=false
OKX_LIVE_TRADING_ACKNOWLEDGED=false
OKX_ENABLE_LIVE_TRADING=
```

确认行情、账户模式和订单数量后，在 Web“自动交易”页面输入 `ENABLE DEMO` 才能打开自动交易。

### 实盘配置

实盘执行必须同时满足服务端三重解锁条件：

```dotenv
OKX_DEMO_TRADING=false
OKX_LIVE_TRADING_ACKNOWLEDGED=true
OKX_ENABLE_LIVE_TRADING=YES
```

首次启动仍建议保持：

```dotenv
OKX_AUTO_TRADING_ENABLED=false
```

检查账户和品种后，在 Web 页面输入 `ENABLE LIVE`，再手动打开自动交易开关。仅把 `OKX_DEMO_TRADING` 改成 `false` 并不会自动下单。

### 订单与风控参数

```dotenv
OKX_DEFAULT_ORDER_SIZE=1
OKX_DEFAULT_LEVERAGE=3
OKX_TRADE_MODE=cross
OKX_POSITION_MODE=net
OKX_BLOCK_NEW_ENTRIES_WHEN_POSITION_OPEN=true
OKX_MAX_SIGNAL_AGE_SECONDS=120
OKX_AUTOMATION_POLL_SECONDS=20
OKX_AUTOMATION_SESSION_PRESET=always
```

| 参数 | 说明 |
| --- | --- |
| `OKX_AUTO_TRADING_ENABLED` | 服务启动时是否自动开启后台交易。生产环境建议保持 `false`，再从页面人工开启。 |
| `OKX_DEFAULT_ORDER_SIZE` | 固定下单数量。现货通常是基础币数量；SWAP/FUTURES 通常是合约张数，不是币的数量。 |
| `OKX_DEFAULT_LEVERAGE` | 新开 SWAP/FUTURES 仓位前设置的默认杠杆，范围不超过 `125`。不会主动修改已有仓位。 |
| `OKX_TRADE_MODE` | `cash` 为普通现货，`cross` 为全仓，`isolated` 为逐仓。衍生品常用 `cross` 或 `isolated`。 |
| `OKX_POSITION_MODE` | `net` 为单向持仓，`long_short` 为双向持仓，必须和 OKX 账户设置一致。 |
| `OKX_BLOCK_NEW_ENTRIES_WHEN_POSITION_OPEN` | 为 `true` 时，已有衍生品仓位会阻止继续加仓或反向开仓。 |
| `OKX_MAX_SIGNAL_AGE_SECONDS` | 从最新已收盘 K 线的收盘时间计算，超过该秒数的信号不得执行。 |
| `OKX_AUTOMATION_POLL_SECONDS` | 后台检查新收盘 K 线的间隔，最小为 5 秒；它不是固定下单频率。 |
| `OKX_AUTOMATION_SESSION_PRESET` | 自动分析时段预设：`always`、`us_regular`、`us_open`、`london`、`asia` 或 `custom`。 |
| `OKX_AUTOMATION_SESSION_TIMEZONE` | `custom` 模式使用的 IANA 时区，例如 `Asia/Shanghai` 或 `America/New_York`。 |
| `OKX_AUTOMATION_SESSION_START` / `END` | `custom` 模式每天的开始和结束时间，格式为 `HH:MM`。结束时间早于开始时间时按跨午夜时段处理。 |
| `OKX_AUTOMATION_SESSION_WEEKDAYS` | `custom` 模式运行日，逗号分隔；周一为 `0`，周日为 `6`。 |

`OKX_DEFAULT_ORDER_SIZE=1` 对不同品种代表的实际价值差异很大。实盘前必须查看 OKX 的 `ctVal`、`lotSz`、`minSz` 和账户可用余额。例如某些永续合约的 `1` 表示 1 张合约，而不是 1 个 BTC 或 ETH。

以 `ETH-USDT-SWAP` 为例，当前 1 张合约约等于 `0.1 ETH`。配置 `OKX_DEFAULT_ORDER_SIZE=0.04` 表示下单 `0.04` 张，即约 `0.004 ETH`；ETH 价格为 `1900 USDT` 时，名义价值约 `7.6 USDT`，3 倍杠杆预计占用约 `2.53 USDT` 保证金。实际数值以 OKX 当前合约规格、成交价格和账户保证金计算为准。

现货下单参数会根据交易模式自动生成：`cross` 模式携带报价币种 `ccy`；只有 `cash` 模式的现货市价单才携带 `tgtCcy=base_ccy`，避免 OKX `50014` 参数错误。

### 自动交易分析时段

自动交易页内置以下常用时段：

| 预设 | 当地时间 | 运行日 |
| --- | --- | --- |
| 全天候 | 24 小时 | 每天 |
| 美股常规盘 | `09:30-16:00`，`America/New_York` | 周一至周五 |
| 美股开盘窗口 | `09:30-11:30`，`America/New_York` | 周一至周五 |
| 伦敦时段 | `08:00-16:30`，`Europe/London` | 周一至周五 |
| 亚洲时段 | `09:00-16:00`，`Asia/Shanghai` | 周一至周五 |

美股和伦敦预设使用 IANA 时区，夏令时切换会自动生效。自定义时段可在 Web 页面选择时区、开始时间、结束时间和运行日；例如仅在北京时间周一至周五晚间到次日凌晨运行：

```dotenv
OKX_AUTOMATION_SESSION_PRESET=custom
OKX_AUTOMATION_SESSION_TIMEZONE=Asia/Shanghai
OKX_AUTOMATION_SESSION_START=21:00
OKX_AUTOMATION_SESSION_END=02:00
OKX_AUTOMATION_SESSION_WEEKDAYS=0,1,2,3,4
```

时段外，后台自动交易会在请求行情前退出，不调用 AI，也不会分析或提交订单。进入时段后只处理在该时段内收盘的新 K 线，避免开盘时处理时段外的旧信号。Web 页面会显示当前是否处于分析时段以及下一次开放时间。


### 高级分析配置

以下参数位于 `config/settings.json`，不包含 API 密钥：

```json
{
  "general": {
    "analysis_bar_count": 100,
    "decision_confidence_threshold": 40,
    "decision_stance": "balanced"
  }
}
```

- `analysis_bar_count`：每次分析使用的 K 线数量。
- `decision_confidence_threshold`：允许执行订单的最低置信度。
- `decision_stance`：`conservative`、`balanced`、`aggressive` 或 `extreme_aggressive`。

## Web 使用方法

1. 选择现货或永续/TradFi 产品。
2. 搜索品种并选择 K 线周期。
3. 点击“运行 AI 分析”获取两阶段决策。
4. 仅分析时不要勾选“分析后按风控执行”。
5. 在账户页检查总权益、资产、仓位和挂单。
6. 在自动交易页选择预设或自定义分析时段，点击“应用时段”。
7. 输入 `ENABLE DEMO` 或 `ENABLE LIVE` 后开启后台运行。

自动交易运行在服务器进程中。刷新或关闭浏览器不会停止它；服务重启后会根据 `.env` 的 `OKX_AUTO_TRADING_ENABLED` 和 `OKX_AUTOMATION_SESSION_*` 配置恢复初始状态。

## Linux 部署

Linux 服务器推荐使用宝塔面板部署，详细步骤请查看本文开头的部署视频教程。

## 日志与记录

- 订单审计：`logs/okx_orders.jsonl`
- 决策记录：`records/pending/`
- 账户权益历史：`logs/okx_equity_history.json`

这些文件可能包含账户或交易信息，不要上传到公开仓库。

## 常见问题

### Linux 启动后外部打不开

日志如果显示：

```text
Uvicorn running on http://127.0.0.1:8088
```

说明服务只允许本机访问。宝塔面板部署时请检查项目启动参数、服务器安全组和防火墙端口；需要直接通过服务器 IP 访问时，将启动参数设置为 `--host 0.0.0.0`。

### `WinError 10013`

通常是 Windows 防火墙、安全软件或运行账户禁止 Python 建立外网连接。允许当前虚拟环境中的 Python 访问 `www.okx.com:443`，并检查代理和出站网络策略。

### OKX 鉴权失败

检查 API Key、Secret Key、Passphrase 是否属于当前模拟盘/实盘环境；确认交易权限、IP 白名单、系统时间和 `OKX_DEMO_TRADING` 设置一致。

### OKX 下单失败

重点检查：

- `OKX_POSITION_MODE` 是否和 OKX 账户一致
- `OKX_TRADE_MODE` 是否适用于当前品种
- 下单数量是否满足 `lotSz` 和 `minSz`
- 是否已有仓位且启用了阻止加仓
- 账户是否有足够可用余额
- 信号是否已超过允许时效

### 修改 `.env` 没有生效

`.env` 只在服务启动时加载。修改后执行 `systemctl restart okx-2pa-agent-web`，Windows 则停止并重新启动 Web 服务。

## 测试

```bash
python -m pytest -q
python -m compileall -q pa_agent
```

测试使用模拟客户端，不会提交真实 OKX 订单。

## 项目结构

```text
pa_agent/             Python 内部包，保留该名称以兼容现有启动和导入路径
  ai/                 OpenAI 兼容 LLM 客户端与分析逻辑
  config/             配置模型与加载逻辑
  data/               OKX K 线和分析快照
  okx/                OKX REST、签名、下单与风控
  orchestrator/       两阶段分析编排
  records/            决策记录
  web/                FastAPI 服务和静态前端
prompt_engineering/   价格行为提示词与策略库
tests/                自动化测试
```

## License

[GNU Affero General Public License v3.0](LICENSE)

## 常见问题：有交易信号但显示 `signal expired`，订单未提交

当决策记录显示“做多”或“做空”，置信度也达到下单门槛，但自动交易记录显示 `signal expired`、`未提交` 时，通常不是 OKX 拒单，而是程序的信号时效保护生效。

程序从最新已收盘 K 线的收盘时间开始计算信号年龄。两阶段 AI 分析完成后，如果信号年龄已经超过 `OKX_MAX_SIGNAL_AGE_SECONDS`，程序会在调用 OKX 下单接口之前停止执行。此时通常会看到：

- `submitted=false`
- `reason=signal expired`
- 没有 OKX 订单 ID
- `error_code` 为空
- 订单请求为空或没有实际下单数量

### 两个超时参数的区别

```env
# 单个 AI 分析阶段允许等待的最长时间
LLM_STAGE_TIMEOUT_SECONDS=180

# 从 K 线收盘开始，交易信号允许存在的最长时间
OKX_MAX_SIGNAL_AGE_SECONDS=300
```

`LLM_STAGE_TIMEOUT_SECONDS` 只是单个 AI 阶段的超时上限，不会自动延长交易信号有效期。两阶段分析、校验和重试的总耗时可能大于单阶段超时时间。将该参数设置得很大，可能导致模型最终给出交易建议时，信号早已超过允许执行的时间。

对于 `15m` 周期，可先使用上面的 `180` 秒与 `300` 秒配置。不要为了确保下单而将信号有效期直接提高到 `1000` 秒以上，否则程序可能在下一根甚至更晚的 K 线才提交旧信号。模型仍然经常超过 5 分钟时，应优先缩短提示词、降低推理强度或更换响应更快的模型。

修改 `.env` 后必须重启服务：

```bash
sudo systemctl restart okx-2pa-agent-web
```

可通过 Web 页面或接口确认以下状态均为 `true`：

```text
auto_trading_enabled=true
live_execution_unlocked=true
can_execute=true
```

如果仍需分析 LLM 响应缓慢或多次出现 `LLM stage exceeded ... seconds`，只需导出问题时段的服务日志，不要上传 `.env`、API Key、Secret Key 或 Passphrase：

```bash
sudo journalctl -u okx-2pa-agent-web \
  --since "2026-07-24 05:20:00" \
  --until "2026-07-24 07:15:00" \
  --no-pager > okx-llm-delay.log
```
