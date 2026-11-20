# QwenWork2API

把**千问办公**（QwenWork）的办公积分变成标准的 **OpenAI 兼容 API**，自带实时控制台。
零第三方依赖，一个 `node server.mjs` 就能跑。

> Turn QwenWork office credits into an OpenAI-compatible API with a built-in console.
> Zero dependencies — just `node server.mjs`.

---

## 为什么用它

- **一个 Base URL 打通全部档位**：`/v1/chat/completions` 直接用，Claude Code、Codex、Chatbox、DSH、OpenWebUI 都能接。
- **零依赖**：不用 Node 之外的任何东西，不用 Docker，不用数据库，账号与用量都是本地 JSON。
- **密码登录的控制台**：默认密码 `147369qAz`（`PANEL_PASSWORD` 可覆盖，登录后在「设置」里改），不用再复制长令牌。
- **六个页面**：数据看板 / 用量分析 / 调用日志 / 账号 / 密钥 / 设置，5 秒自动刷新，日志页单独 8 秒轮询。
- **积分与钱包实时读取**：账号卡直接显示 `balance` 与各钱包余额（含有效期），刷新余额时一起更新。
- **模型可用性自检**：设置页一键逐个真实打一条，记录每个模型在当前套餐下是否放行（`Model is not available for this user` 一眼分清是套餐问题还是链路问题）。
- **导入已有登录态**：`POST /admin/api/import {access, refresh?, uid?}` 可直接把客户端解出来的 token 灌进来，不用重新授权。
- **每日免费积分**：接口存在时每账号每天自动领一次；**prod 主栈没有这个路由时面板会明确写「该环境无此接口」**，不会误报账号失效。
- **客户端指纹可切换**：一号一盐一 `machineId`，平台/架构稳定派生，客户端版本永远跟运行时一致；控制台可单号换指纹。
- **多账号轮转**：号池按剩余积分优先挑，401 自动续期、5xx 换号重试，已向客户端写字节后绝不重试（不会重复输出）。上游 429 只冷却「该账号 × 该模型」（`QW_MODEL_COOLDOWN_MS`，默认 60s），不会把整个账号标成额度耗尽，也不影响同账号的其它档位。
- **响应模型名改写**：上游返回内部档位名，转发时改回你请求的模型名，客户端只看到自己选的那个。

## 支持的档位

档位名来自官方客户端 **2.1.0** 的 `modelSelector` 枚举；中文标签取自客户端 `dynamic-text` 文案。

| 对外模型名 | 上游档位 | 官方标签 |
|---|---|---|
| `qwenwork-lite` | `qwork-lite` | 经济 |
| `qwenwork-standard` | `qwork-auto` | 标准 |
| `qwenwork-advanced` | `qwork-advanced` | 高级 |
| `qwenwork-ultimate` | `qwork-ultimate` | 旗舰 |
| `qwenwork-enterprise` | `safety` | 企业专属 |
| `qwen3.8-max` | `qmodel_latest` | Qwen3.8-Max |
| `qwen3.8-max-preview` | `qwen3.8-max-preview` | Qwen3.8-Max（预览） |
| `qwen3.6-plus` | `q35model_preview` | Qwen3.6-Plus-DogFooding |
| `deepseek-v4-pro` | `dmodel_latest` | DeepSeek V4 Pro |
| `glm-5.3` | `gmodel_latest` | GLM-5.3 |
| `qwen3.8max` / `qwen3.8` | `qwork-advanced` | —（兼容旧调用） |

模型名大小写不敏感（`Qwen3.8-Max` 也能用）。**具体能用哪几个由账号套餐决定**，没有权限的上游会回 403。

## 快速开始

```bash
git clone https://github.com/jianhx189/qwenwork2api.git
cd qwenwork2api

# 1) 取签名组件（唯一硬依赖，从官方 Linux 包提取）
curl -LO https://assets.qwenwork.cn/release/latest/qwenworkcn-linux-amd64.deb
dpkg-deb -x qwenworkcn-linux-amd64.deb unpack
cp unpack/opt/apps/QwenWorkCN/resources/qoder-auth-wasm/qoder_auth_wasm_bg.wasm ./
rm -rf unpack qwenworkcn-linux-amd64.deb

# 2) 起服务
node server.mjs
```

打开 `http://<你的地址>:4021/admin`，输密码进控制台 → 「添加账号」→ 浏览器里完成一次设备授权 → 新建令牌 → 客户端填：

```
Base URL : http://<你的地址>:4021/v1
API Key  : sk-qw-...        # 控制台新建的那个
Model    : qwenwork-advanced
```

## 控制台

| 页面 | 内容 |
|---|---|
| 数据看板 | 今日调用 / 成功率 / 平均耗时（含 P95）/ 剩余积分，24 小时堆叠柱，模型分布，账号积分条，账号调用量，最近调用 |
| 用量分析 | 近 7 / 14 / 30 天切换，每日趋势 + 按天明细 + 按模型 + 按密钥 |
| 调用日志 | 全部 / 成功 / 失败 / 系统四档筛选 + 关键词搜索 |
| 账号 | 单号领取积分 / 刷新余额 / 换指纹 / 删除；批量全部刷新、批量全部领取 |
| 密钥 | 掩码展示、复制完整 Key、停用启用、删除；新建时只显示一次 |
| 设置 | 改密码、每日领取开关、运行信息、退出登录 |

添加账号的流程：`POST /admin/api/login/start` 拿设备授权链接 → 浏览器确认 → 控制台每 3 秒轮询 `login/poll?flowId=` → 授权完成自动入库。

## 环境变量

| 变量 | 默认 | 说明 |
|---|---|---|
| `PORT` | `4021` | 监听端口 |
| `PANEL_PASSWORD` | `147369qAz` | 控制台初始密码（首次启动写入 `data/panel.json`，scrypt 存储） |
| `ADMIN_TOKEN` | 随机生成 | 旧版管理令牌，脚本调用仍可用（`data/admin_token.txt`） |
| `QW_MAX_RETRIES` | `2` | 首次之外的额外尝试次数 |
| `QW_HEADER_TIMEOUT_MS` | `45000` | 首字节超时（会真正中断底层请求） |
| `QW_STREAM_IDLE_MS` | `60000` | 流式空闲超时 |
| `QW_MODEL_COOLDOWN_MS` | `60000` | 上游 429 时对「该账号 × 该模型」的冷却时长（不影响同账号其它模型，也不改账号状态） |
| `REFRESH_MS` | `600000` | 定时刷新余额间隔 |
| `QWENWORK_WASM_PATH` | 同目录 | 签名组件路径 |
| `QWENWORK_CLIENT_VERSION` | `2.1.0` | 伪装用的客户端版本 |

## 文件边界

```
server.mjs               HTTP / 账号池 / 重试 / 管理 API
admin.html               控制台（单文件，无外部资源）
panel_app2.html          控制台源码（panel_build.py 注入样式后生成 admin.html）
lib/                     协议层（账号、签名、聊天转发、指纹、积分、面板登录）
data/state.json          账号与令牌（首次运行自动生成，勿提交）
data/panel.json          控制台密码（scrypt，勿提交）
data/logs.jsonl          调用流水
qoder_auth_wasm_bg.wasm  签名组件（从官方包提取，勿提交）
```

## 常见问题

**上游回 403 / 没有权限**：账号套餐不含该档位，换档位或换号。

**每日领取报「该环境无此接口」**：说明这个账号所在的 prod 主栈（`gateway.qwenwork.cn`）没有
`/api/v1/adapter/user/daily-credit-notice/claim` 这条路由——实测它只存在于 daily 栈
（`daily.gateway.qwenwork.cn`），而那是另一套账号体系，prod 的 token 在那边是 `INVALID_TOKEN`。
这时余额与钱包仍然正常读取，只是拿不到每日赠送。

**每日领取报「登录已失效」**：access/refresh token 真的坏了，在控制台重新「添加账号」授权一次。

**`max_tokens` 报错**：千问办公上游硬上限 32000，超过要自己夹。

**报「模型 X 的全部 N 个账号正在限流冷却，约 M 秒后自动恢复」**：上游对**该档位**回了 429（典型是
DeepSeek 档位）。这是短时冷却，不是账号坏了、也不是额度耗尽：冷却按「账号 × 模型」记账，同账号的
Qwen 档位照常可用，账号状态也不会被改成 `quota_exhausted`。等 M 秒或换档位即可；嫌等待长可调
`QW_MODEL_COOLDOWN_MS`。

**首帧慢**：这个网关没有前缀缓存，长上下文由 prefill 决定；想要快就把上下文压小或改用带缓存的通道。

**忘记控制台密码**：删掉 `data/panel.json` 重启，密码回到 `PANEL_PASSWORD`（默认 `147369qAz`）。

**多个账号一起跑会怎样**：按剩余积分优先挑号，失败换号，不会同时压同一个号。

## AI 一键安装

把下面整段丢给 Claude Code / Codex / Cursor：

> 在远端 Linux 机器上帮我部署 qwenwork2api：
> 1. `git clone https://github.com/jianhx189/qwenwork2api.git && cd qwenwork2api`
> 2. 下载 `https://assets.qwenwork.cn/release/latest/qwenworkcn-linux-amd64.deb`，用 `dpkg-deb -x` 解开，把 `opt/apps/QwenWorkCN/resources/qoder-auth-wasm/qoder_auth_wasm_bg.wasm` 拷到项目根目录，删掉 deb 和解包目录
> 3. `node server.mjs`（Node ≥ 18.17），确认 `/health` 返回 `wasm:true`
> 4. 用 PM2 常驻：`pm2 start server.mjs --name qwenwork2api && pm2 save`
> 5. 打开 `/admin`，用默认密码 `147369qAz` 登录，改掉密码并点「添加账号」完成设备授权

## License

MIT。协议层来自 [tianyn1990/qwenwork-magpie](https://github.com/tianyn1990/qwenwork-magpie)（MIT），服务层与控制台由 [jianhx](https://github.com/jianhx189) 编写。

本项目只做账号自助接入，请遵守上游服务条款；签名组件不入库，需从官方安装包自行提取。
