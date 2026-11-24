# awsquick-2api

> 把 AWS Quick 变成 OpenAI 兼容接口 —— 一条 `base_url` 接入任意支持 OpenAI 协议的客户端。

**作者：Trash-Makers** · MIT License · [GitHub](https://github.com/Trash-Makers/awsquick-2api)

![控制台界面](docs/dashboard.png)

> 可视化控制台：账号池、额度、成本与调用明细都在同一屏里，附带一个可以直接试号的对话窗口。


---

## 这是什么

`awsquick-2api` 是一个本地网关。它把 AWS Quick（原 Amazon QuickSight）的对话能力，转换成标准的 OpenAI Chat Completions 协议：

```
你的客户端 / 应用  ──▶  awsquick-2api  ──▶  AWS Quick
   (OpenAI SDK)         (本机 127.0.0.1)      (账号池)
```

自带的控制台提供账号池管理、密钥分发、成本账本、额度熔断，以及一个可选的注册机（半自动 / 全自动框架）。

## 功能

### 网关（主线）
- **OpenAI 兼容**：`/v1/models`、`/v1/chat/completions`，支持流式
- **多账号轮询**：按请求轮换，`401/403/429/5xx` 自动切号
- **失败退避**：指数退避 + 半开探测，单次抖动不会丢号
- **额度熔断**：账号用量达到阈值自动停用，不再分配请求
- **密钥分发**：`qk_…` 前缀的 API Key，可随时撤销
- **成本账本**：每次调用记录模型、tokens、成本、耗时，按小时/模型/账号汇总
- **出站代理**：反代侧可独立配置代理，与注册侧互不影响

### 控制台
八个页面：概览 / 账号池 / 密钥 / 调用 / 代理 / 注册任务 / 日志 / 设置。
全部数据本地存储，不经过任何第三方服务。

### 注册机（可选，附加）
- **半自动**：自动完成 邮箱 → 验证码 → 姓名 → 密码，注册完成后在面板里一键授权入池
- **手动邮箱池**：提前准备一批邮箱，逐条自动注册，验证码由你填入
- **全自动**：框架已就位（打码接口 + 授权自动化），需要自备打码服务与住宅代理

## 架构

```
┌──────────────┐   OpenAI 协议    ┌─────────────────┐
│ 你的应用      │ ───────────────▶ │  网关 :3426      │
│ (任意 SDK)    │ ◀─────────────── │  密钥 / 轮询 / 账本│
└──────────────┘                  └────────┬────────┘
                                           │ WebSocket
                                  ┌────────▼────────┐
                                  │  AWS Quick 账号池 │
                                  └────────┬────────┘
                                           │ 注册（可选）
┌──────────────┐    HTTP           ┌────────▼────────┐
│ 控制台 :8787  │ ───────────────▶ │ 注册机 / 邮箱池   │
└──────────────┘                   └─────────────────┘
```

## 快速开始

### 0. 环境要求

| 依赖 | 版本 | 用途 |
|---|---|---|
| Python | 3.10+ | 控制台 + 注册机 |
| Node.js | 18+ | 网关 |
| Chromium 内核浏览器 | 自动下载 | 注册（可选） |

### 1. 获取代码

```bash
git clone https://github.com/Trash-Makers/awsquick-2api.git
cd awsquick-2api
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
python -m patchright install chromium

cd vendor/quick-gateway && npm install && cd ../..
```

### 3. 配置

```bash
cp config.example.json config.json
```

打开控制台（下一步启动后）在 **设置 → 收信配置** 里填，或直接编辑 `config.json`。

### 4. 启动

```bash
# 终端 1：网关
cd vendor/quick-gateway
PORT=3426 GATEWAY_DIR=../../data/oauth DATA_DIR=../../data node bin/serve-oauth.mjs

# 终端 2：控制台
python3 app.py
```

打开 `http://127.0.0.1:8787`。

### 5. 授权第一个账号

两种方式，任选其一。

**⚡ 自动导入**（有桌面环境的机器）

1. 控制台 → **注册任务** → 已注册账号右侧点「⚡ 自动导入」
2. 点「开始」：程序自动打开授权页、填邮箱密码
3. 出现人机验证时，直接在弹窗里的画面上点击
4. 验证通过后自动捕获回调，账号直接进池

**手动导入**（VPS / 无桌面环境，或想用自己的浏览器）

1. 控制台 → **账号池** → 「授权 / 手动导入」（或注册任务里的「手动导入」）
2. 复制授权地址，在浏览器打开，用你的 AWS 账号登录
3. 登录完成后，把地址栏里带 `?code=` 的完整地址粘贴回弹窗
4. 点「完成授权」——账号进池，状态变为「可用」

> 部署在 VPS / 没有显示器的服务器上时，自动导入的实时画面会缺样式（浏览器无头渲染所致）。
> 这种情况下请用「手动导入」；想用自动导入，把项目跑在有桌面的电脑上，或在设置里打开
> 「导入号池时弹出真实浏览器窗口」。
>
> 首次进入会有四步引导，可勾选「以后不再自动显示」。

### 6. 生成密钥并调用

**密钥** → 生成 → 得到 `qk_…`（只显示一次）。

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:3426/v1",
    api_key="qk_xxxxxxxxxxxxxxxx",
)

resp = client.chat.completions.create(
    model="fast",              # fast | balanced | smart | advanced
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

命令行：

```bash
curl http://127.0.0.1:3426/v1/chat/completions \
  -H "Authorization: Bearer qk_xxxxxxxxxxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{"model":"fast","messages":[{"role":"user","content":"hi"}]}'
```

## 模型档位与成本

| 档位 | 实际模型 | 单次成本量级 | 适用 |
|---|---|---|---|
| `fast` | claude-haiku | ~$0.005 | 日常对话、批量任务（**默认建议**） |
| `balanced` | claude-sonnet | 中等 | 需要更强推理 |
| `smart` | claude-opus | ~$0.20 | 复杂任务，**成本约为 fast 的 45 倍** |
| `advanced` | 最高档 | 更高 | 极端场景 |

> 每次请求都会带上完整的助手上下文（约 6.8 万 tokens），缓存命中率很高，所以单次成本远低于按满额计费。控制台的「调用」页可以看到每一笔实际花费。

## 收信配置（注册机需要）

四种方式，任选其一：

### 方式 A：Cloudflare Email Routing + Worker（推荐）

1. 域名托管到 Cloudflare，开启 Email Routing
2. 新增 catch-all 规则 → 指向 Worker
3. 部署 Worker：

```bash
python3 tools/deploy_mail_worker.py \
  --token-file ./cf_token \
  --subdomain your-worker-name \
  --api-token your-secret-token
```

4. 控制台 → 设置 → 填 Worker 地址与同一串 Token

### 方式 B：任意邮箱项目的 HTTP 接口

任何能返回 `{"code": "123456"}` 的接口都可以：

```
https://your-mail-api/latest?to={to}&token={token}
```

控制台里填入这个模板，`{to}` 会替换成收件地址，`{token}` 替换成你填的密钥。

### 方式 C：IMAP 直连（全自动，任意邮箱）

不需要域名、不需要转发。在设置里选「IMAP 自动取信」，填：

```
alice@gmail.com,abcd efgh ijkl mnop
bob@qq.com,xxxxxxxxxxxxxxxx
```

第二列是**应用专用密码**，不是登录密码：Gmail 需开启两步验证后生成，QQ/163 需在设置里开启 IMAP 并获取授权码。

IMAP 服务器可留空自动识别（Gmail / Outlook / QQ / 163 / Yahoo / iCloud 都认），也可手填。
程序只读未读邮件取 6 位码；取不到会自动回退成「面板手动填码」，不会卡死。

### 方式 D：手动邮箱池

不接任何收信服务。在设置里逐行填邮箱：

```
alice@your-domain.com,Passw0rd!
bob@your-domain.com
```

注册跑到验证码那步会停下，任务行会**高亮并显示已等待时间**，你在那一行填入 6 位码即可继续。
等待上限 5 分钟，期间页面标题会提示 `(1) 等待验证码`。

> ⚠️ 公共临时邮箱域名会被 AWS 拒绝（`ERR-837`），必须使用自有域名。

## 配置项

`config.json`（**不要提交到仓库**）：

| 字段 | 说明 |
|---|---|
| `panel.port` | 控制台端口，默认 8787 |
| `gateway.port` | 网关端口，默认 3426 |
| `mail.provider` | `cloudflare` / `custom` / `imap` / `manual` |
| `mail.domain` | 注册用的邮箱域名 |
| `mail.worker_url` / `mail.api_token` | 方式 A 的 Worker 地址与口令 |
| `mail.custom_url` | 方式 B 的取信接口模板 |
| `mail.manual_mails` | 方式 C / D 的邮箱池（IMAP 模式第二列是应用密码） |
| `mail.imap` | 方式 C 的 IMAP 服务器与端口（留空自动识别） |
| `registration.concurrency` | 注册并发（建议 1~2） |
| `registration.target` | 单批目标数量 |
| `registration.task_timeout_s` | 单任务超时 |
| `registration.retries_per_task` | 失败重试次数 |
| `registration.headless` | 无头模式 |
| `quota.warn_percent` / `quota.stop_percent` | 额度预警 / 熔断阈值 |
| `gateway_behavior.default_model` | 请求未指定模型时的默认档位 |
| `gateway_behavior.max_tokens` | 单次最大 tokens |
| `proxy.registration` / `proxy.gateway` | 两侧独立的代理开关与列表 |

## 目录结构

```
.
├── app.py              控制台（Flask）
├── engine.py           注册执行引擎（半自动 / 全自动框架）
├── db.py               SQLite：任务、日志、资源池
├── config.py           配置加载
├── flows/
│   ├── quick_signup.py 注册流程定义与失败原因
│   ├── captcha.py      打码接口（CapSolver，可选）
│   └── auto_oauth.py   全自动授权框架
├── static/             控制台前端 + 思源宋体子集
├── tools/              注册、登录、邮件桥等独立脚本
├── worker/             Cloudflare Email Worker
├── vendor/quick-gateway 网关运行时（含第三方组件，遵循其许可证）
└── data/               运行时数据（会话、密钥、账本）—— 已忽略
```

## 常见问题

**Q：注册时报 `ERR-837`？**
域名信誉不足。公共临时邮箱域名一律被拒，建议用已注册一段时间的自有域名。

**Q：授权时卡在人机验证？**
这是 AWS WAF Captcha。半自动模式下需要人工完成一次；全自动需要打码服务（见 `flows/captcha.py`）。

**Q：成本怎么控制？**
默认档位设成 `fast`；`smart`（Opus）单价约是它的 45 倍。控制台「调用」页有逐笔账本。

**Q：账号能跑多久？**
免费额度约每月 10 小时 agent 时长，用尽后网关会自动熔断该账号。

**Q：能不能放到公网？**
默认只监听 `127.0.0.1`。若确需外露，请自行加反向代理 + 鉴权，否则任何人都能用你的额度。

## 路线图

- [ ] 全自动注册（打码 + 授权全链路）
- [ ] 密钥级配额与限速
- [ ] 多机部署与账号同步
- [ ] 英文文档

## 安全须知

`data/` 目录包含账号会话、API 密钥、邮箱密码、调用账本，**已在 `.gitignore` 中排除**。
部署时请确认：

- `config.json` 不提交、不外发
- `data/` 不进入任何备份或同步目录
- 网关与控制台默认只绑 `127.0.0.1`

## 免责声明

本项目仅供个人学习与技术研究使用。使用前请自行确认符合 AWS 服务条款与当地法律法规。
因使用本项目产生的账号限制、费用或其它后果，由使用者自行承担。

## License

[MIT](./LICENSE) © Trash-Makers

第三方组件与其许可证见 [NOTICE](./NOTICE)。
