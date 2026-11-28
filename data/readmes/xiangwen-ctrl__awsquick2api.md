# AWSQuick2API

[![CI](https://github.com/xiangwen-ctrl/awsquick2api/actions/workflows/ci.yml/badge.svg)](https://github.com/xiangwen-ctrl/awsquick2api/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=xiangwen-ctrl_awsquick2api&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=xiangwen-ctrl_awsquick2api)
[![Release](https://img.shields.io/github/v/release/xiangwen-ctrl/awsquick2api)](https://github.com/xiangwen-ctrl/awsquick2api/releases)
[![Docker](https://img.shields.io/badge/Docker-GHCR-2496ED?logo=docker&logoColor=white)](https://github.com/xiangwen-ctrl/awsquick2api/pkgs/container/awsquick2api)
[![Go](https://img.shields.io/badge/Go-1.26.11%2B-00ADD8?logo=go&logoColor=white)](./go.mod)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

**AWSQuick2API** 是一个纯 Go 编写的轻量自托管网关，可将 Amazon Quick 账号封装为标准的 **OpenAI**、**Anthropic（Claude Code）** 与 **OpenAI / Codex Responses** 兼容 API，并内置单页 Web 运维面板。单二进制零外部依赖，开箱即用。

[3 分钟快速上手](#3-分钟快速上手) · [面板功能一览](#面板功能一览) · [多密钥与安全设计](#多密钥访问控制与隐私安全) · [API 与模型](#api-端点与模型) · [配置与环境变量](#配置说明) · [常见问题](#常见问题-faq)

![AWSQuick2API 总览与账号池](./docs/images/panel-overview.png)
> *以上为脱敏演示数据界面截图（版本 `v0.2.0`），支持明/暗主题切换。*

---

## 核心特性

- **三协议全兼容**：原生支持 OpenAI (`/v1/chat/completions`、`/v1/models`、`/v1/models/{id}`)、Anthropic (`/v1/messages` 及 `count_tokens`) 与 Codex Responses (`/v1/responses`)，完整支持流式输出、思考链（Reasoning）、工具调用、按请求动态联网搜索（`web_search`）、JSON 模式与图片输入。
- **原生 OAuth PKCE 登录**：在面板中发起个人 / 企业账号官方授权；本机自动接收回调，远程服务器或 Docker 容器支持直接粘贴回调地址完成登录，无需抓包或提取 Cookie。
- **多账号池与高可用容错**：支持按剩余额度加权 / 轮询 / 顺序调度，自动续期令牌、按官方恢复时间自动冷却与异常熔断、5 分钟滑动窗口上游劣化监测，并支持单客户端多轮线程复用。
- **轻量多密钥访问控制**：主推理密钥 `api_key` 开箱即用，同时支持在面板创建带 **模型白名单 / 过期时间 / 日请求上限 / 总 Token 上限** 的子密钥（Scoped API Keys）；本地仅保存 SHA-256 哈希，且与管理面板严格隔离。
- **内嵌单页 Web 运维面板**：无需额外前端部署，一个二进制即可管理账号池、创建访问密钥、在线测试（Playground）、通过快捷表单热改配置、查看元数据统计与一键导出脱敏运行日志 ZIP。
- **跨平台单文件 & Docker 镜像**：`CGO_ENABLED=0` 静态编译，提供 Windows（系统托盘版 / 控制台版）、Linux（`amd64` / `arm64`）、macOS 二进制，以及 `ghcr.io` 多架构 Docker 镜像与 `docker-compose.yml`。

---

## 3 分钟快速上手

### 第 1 步：启动服务（任选一种方式）

#### 方式 A：直接运行预编译程序（最适合本机体验）

从 [GitHub Releases](https://github.com/xiangwen-ctrl/awsquick2api/releases) 下载对应平台文件：

- **Windows（推荐）**：双击 `awsquick2api-windows-amd64.exe` 启动，常驻系统托盘，首次启动会自动打开管理面板（需命令行运行可选 `awsquick2api-windows-amd64-console.exe`）。
- **macOS（Apple Silicon / Intel）**：
  ```bash
  chmod +x awsquick2api-darwin-arm64
  ./awsquick2api-darwin-arm64
  ```
  > Intel Mac 请下载 `awsquick2api-darwin-amd64`。
- **Linux（x86-64 / ARM64）**：
  ```bash
  chmod +x awsquick2api-linux-amd64
  ./awsquick2api-linux-amd64
  ```
  > ARM64 设备请下载 `awsquick2api-linux-arm64`。

首次启动会自动在当前目录生成 `config.json`（内置随机生成的 `api_key` 和 `admin_key`）以及本地加密密钥 `data/encryption.key`。

#### 方式 B：Docker Compose 一键部署（推荐服务器使用）

```bash
# 1. 创建目录并下载 docker-compose.yml
mkdir -p awsquick2api/storage && cd awsquick2api
curl -fsSLO https://raw.githubusercontent.com/xiangwen-ctrl/awsquick2api/main/docker-compose.yml

# 2. 以当前宿主机用户权限启动（自动拉取 ghcr.io 多架构镜像，免 sudo / chown）
PUID=$(id -u) PGID=$(id -g) docker compose up -d

# 3. 查看生成的初始配置与日志
docker compose logs -f
```

> - 首次启动会在 `./storage/` 自动生成 `config.json`、`auths/` 与 `data/`，无需提前手工创建文件；若省略 `PUID`/`PGID`，容器默认以 `10001:10001` 运行（需先执行 `sudo chown -R 10001:10001 storage`）。
> - 默认仅映射宿主机 `127.0.0.1:8045`，避免服务意外暴露到公网；如需局域网直接访问可修改 `docker-compose.yml` 中的端口映射。
> - 如需 Linux `systemd` 原生常驻部署，请参阅 [Linux 部署指南](./docs/LINUX.md)。

---

### 第 2 步：解锁面板并添加账号

1. **打开管理面板**
   - **本机运行**：直接访问 `http://127.0.0.1:8045/panel/`。
   - **远程服务器（已配置反代域名）**：通过 Nginx / Caddy 等反向代理直接访问 `https://你的域名/panel/`（需在 `server.trusted_hosts` 或环境变量 `AWSQUICK_TRUSTED_HOSTS` 中加入你的域名）。
   - **远程服务器（未配域名 / 不想将面板暴露公网，推荐）**：先在本机建立 SSH 端口转发，再访问 `http://127.0.0.1:8045/panel/`：
     ```bash
     ssh -L 8045:127.0.0.1:8045 user@YOUR_SERVER
     ```
2. **输入 `admin_key` 解锁**
   - 打开生成的 `config.json`（Docker 位于 `./storage/config.json`），复制其中的 `admin_key`（`qka_` 开头）输入登录框；Windows 托盘版可右键托盘图标一键复制。
   - 个人常用设备可勾选 **「记住登录状态」**，公共设备建议保持不勾选（关闭标签页即退出）。
3. **添加 Amazon Quick 账号**
   - 点击右上角 **「+ 添加账号」** → 选择账号类型（个人 / 企业）→ 点击 **「生成一次性授权链接」**。
   - 在浏览器中打开登录链接并完成授权：
     - **本机部署**：浏览器跳转 `http://localhost:18080/...` 后由本地回调端口自动接管并完成入池。
     - **远程服务器 / Docker**：浏览器停在无法访问的 `http://localhost:18080/...` 或 `http://127.0.0.1:18080/...` 时，直接**复制地址栏完整 URL**，粘贴到弹窗底部的手动回调框提交即可（第 1 步发现与第 2 步授权均在此处粘贴）。
4. **验证连通性**
   - 入池后点击账号行的 **「测试」** 或顶栏 **「在线测试」**（Playground），看到正常回复即说明网关已就绪。

> 如需添加多个不同账号，可切换浏览器配置文件或新窗口，避免浏览器自动复用上一个账号的登录态。

---

### 第 3 步：接入你的 AI 客户端

客户端统一填写 `config.json` 中的推理密钥 `api_key`（或在面板「访问密钥」页新建独立子密钥，**不要填写 `admin_key`**）。面板「模型与接入」页也提供了一键复制片段。以下示例以本机地址 `http://127.0.0.1:8045` 为例；如部署在远程服务器并配置了反代域名，替换为 `https://你的域名` 即可。

#### 1. Cherry Studio / OpenCode / ChatBox / OpenAI SDK

- **Base URL**：`http://127.0.0.1:8045/v1`
- **API Key**：你的 `api_key` 或子密钥（`qk_...`）
- **常用模型**：`amazon-smart`（最强）、`amazon-balanced`（均衡）、`amazon-fast`（极速）
- **思考强度后缀**：直接填 `amazon-smart-high`、`amazon-balanced-medium`、`amazon-smart-low`

#### 2. Claude Code（Anthropic Messages 协议）

内置自动将 `claude-opus-*` / `claude-sonnet-*` / `claude-haiku-*` 映射到对应的 Amazon Quick 档位，无需额外改模型名：

```bash
# Linux / macOS
export ANTHROPIC_BASE_URL="http://127.0.0.1:8045"
export ANTHROPIC_AUTH_TOKEN="你的 api_key 或子密钥"
claude
```

```powershell
# Windows PowerShell
$env:ANTHROPIC_BASE_URL = "http://127.0.0.1:8045"
$env:ANTHROPIC_AUTH_TOKEN = "你的 api_key 或子密钥"
claude
```

#### 3. Codex CLI（OpenAI Responses 协议）

编辑 `~/.codex/config.toml`：

```toml
model_provider = "awsquick"
model = "amazon-smart"

[model_providers.awsquick]
name = "AWSQuick2API"
base_url = "http://127.0.0.1:8045/v1"
env_key = "AWSQUICK_API_KEY"
wire_api = "responses"
```

启动前设置环境变量 `AWSQUICK_API_KEY="你的 api_key 或子密钥"` 即可运行 `codex`。

> Responses 支持 HTTP POST 和 SSE 流式输出，并支持 Codex MCP 工具按命名空间记录和续传；多轮续聊需在 `input` 中携带完整历史（`previous_response_id` 会返回错误提示）。

#### 4. `curl` 一行验证

```bash
curl http://127.0.0.1:8045/v1/chat/completions \
  -H "Authorization: Bearer 你的_api_key" \
  -H "Content-Type: application/json" \
  -d '{"model":"amazon-smart","messages":[{"role":"user","content":"你好，请简短自我介绍"}]}'
```

---

## 面板功能一览

> 以下截图均来自脱敏演示环境（示例账号邮箱与密钥均已打码处理）。

### 模型映射、隐私脱敏与客户端一键接入
支持在线控制各模型可见性、自定义对外模型 ID、一键开关 Claude 别名与严格隐私脱敏（`strict_privacy_dlp`），并提供三端接入配置一键复制（默认隐藏明文密钥）：

![模型与接入](./docs/images/panel-models.png)

### 多访问密钥管理（Scoped API Keys）
按客户端或使用者分发独立子密钥，支持限制可用模型、过期时间、每日请求数与总 Token 上限；明文仅在创建瞬间展示一次，磁盘仅留存 SHA-256 哈希与掩码：

![访问密钥管理](./docs/images/panel-keys.png)

### 常用配置快捷表单与 JSON 热生效
高频项（出站代理、默认模型、思考策略与强度、选号策略、反代信任 Host、CORS 白名单、线程复用与默认联网搜索）提供可视化表单，保存即热生效，并与下方完整 JSON 编辑器实时同步：

![常用配置快捷表单](./docs/images/panel-config.png)

### 请求元数据统计（无对话内容留存）
仅记录时间、入口协议、请求/实际模型、归属密钥、调度账号、状态码、TTFB/总耗时与 Token 用量，**绝不记录任何提示词或回复正文**；同时支持在「运行日志」页一键导出全量脱敏日志 ZIP：

![请求统计](./docs/images/panel-requests.png)

---

## 多密钥访问控制与隐私安全

### 三类密钥职责分离

| 密钥类型 | 前缀 / 位置 | 允许访问范围 | 适用场景 |
| --- | --- | --- | --- |
| **管理面板密钥 (`admin_key`)** | `qka_...`（`config.json`） | **仅 `/panel/api/*`** | 仅运维人员本人解锁 Web 面板，切勿分发给客户端 |
| **主推理密钥 (`api_key`)** | `qk_...`（`config.json`） | 所有推理接口（`/v1/*`、`/messages`、`/responses`），**不可访问面板** | 本人单机快速接入，100% 向后兼容旧版配置 |
| **访问子密钥 (Scoped API Keys)** | `qk_...`（面板创建，`data/api-keys.json` 仅存哈希） | 仅推理接口 + 可选模型白名单 / 有效期 / 限额，**绝不可访问面板** | 按工具隔离（Cherry Studio / Codex / Claude Code）或临时分享测试 |

### 内置隐私与安全边界

- **本地凭据加密**：Amazon Quick 账号令牌默认使用 AES-256-GCM 加密落盘（密钥位于 `data/encryption.key`，权限 `0600`）。
- **零对话内容归档**：请求统计与本地归档仅包含元数据（耗时、模型、Token 计数），不保存聊天内容。
- **严格隐私脱敏（`strict_privacy_dlp`）**：默认开启，在流式正文与工具参数中自动拦截账号邮箱、姓名、ID 及其拆字 / 倒序 / 混淆变体（如 `[at]`），防止共享密钥时泄露账号身份。
- **日志全链路脱敏**：终端日志、轮转日志文件与面板一键导出的 ZIP 日志包均经过凭据脱敏处理。
- **网络防护**：默认仅监听 `127.0.0.1:8045`；面板开启同源校验、防 DNS 重绑定（`server.trusted_hosts`）与 `admin_key` 失败限流；可选 CORS 白名单（`server.cors_allowed_origins`）仅对推理路径生效，绝不放行 `/panel/*`。

---

## API 端点与模型

| 方法 | 路径 | 说明 | 鉴权方式 |
| --- | --- | --- | --- |
| `POST` | `/v1/chat/completions` | OpenAI Chat Completions（支持流式、工具、视觉、思考链） | `Bearer <api_key 或子密钥>` |
| `GET` | `/v1/models` | 获取可用模型列表（含 `reasoning_options` / `supported_reasoning_levels`，按子密钥白名单过滤） | `Bearer` 或 `x-api-key` |
| `GET` | `/v1/models/{id}` | 获取单个模型详情（不存在 / 隐藏 / 无权限返回 `404`） | `Bearer` 或 `x-api-key` |
| `POST` | `/v1/messages`（及 `/messages`） | Anthropic Messages（声明 `web_search*` 工具时按请求动态开启联网搜索） | `x-api-key` 或 `Bearer` |
| `POST` | `/v1/messages/count_tokens` | Anthropic Token 估算 | `x-api-key` 或 `Bearer` |
| `POST` | `/v1/responses`（及 `/responses`） | OpenAI / Codex Responses（声明 `web_search*` 工具时按请求动态开启联网搜索） | `Bearer` |
| `GET` | `/healthz` | 服务与账号池健康探针（供 Docker / 监控调用） | 无 |
| `GET` | `/panel/` | 内嵌 Web 管理面板（接口位于 `/panel/api/*`） | 仅 `admin_key` |

### 内置模型映射

支持在模型名后追加 `-off` / `-low` / `-medium` / `-high` 控制思考强度（如 `amazon-smart-high`），并自动剥离 `aws-quick/` 与 `qw/` 前缀：

| 对外模型 ID | 上游档位 | 内置别名 | 说明 |
| --- | --- | --- | --- |
| `amazon-smart` | `smart` | `smart`, `qw-smart`, `aws-quick/smart` | 旗舰推理档位（支持思考链 / 视觉 / 工具） |
| `amazon-balanced` | `balanced` | `balanced`, `qw-balanced`, `aws-quick/balanced` | 速度与质量均衡档位 |
| `amazon-fast` | `fast` | `fast`, `qw-fast`, `aws-quick/fast` | 轻量极速响应档位 |
| `amazon-auto` | `auto` | `auto`, `qw-auto`, `aws-quick/auto` | 由 Amazon Quick 自动选择档位 |
| `amazon-advanced` | `advanced` | `advanced`, `qw-advanced`, `aws-quick/advanced` | 仅在池中至少有一个开通 Advanced 的账号时可见；否则请求返回 `400` |

> 三个推理入口均校验输出上限（`max_tokens` / `max_completion_tokens` / `max_output_tokens`，允许省略或 `null`）。流式输出保持实时推送与 SSE 心跳保活；超过请求上限时会保留已生成内容并以各协议的长度截断状态结束。图片支持符合大小限制的 base64 PNG / JPEG / GIF / WebP（需开启附件且账号支持）。

---

## 配置说明

完整配置模板见 [config.example.json](./config.example.json)。通过面板修改配置后绝大多数选项**即时热生效**；修改 `listen`、`auth_dir`、`data_dir` 或服务端超时与请求体预算时，面板会自动提示需要重启生效的字段。

> 若手动复制 `config.example.json` 使用，请先替换占位值 `replace_with_your_api_key` 与 `replace_with_your_admin_key`（或通过环境变量注入），否则会拒绝启动以防误用默认密钥。

### 高频配置项说明

| 配置项 | 默认值 | 说明 |
| --- | --- | --- |
| `upstream.proxy_url` | `""` | 可选出站代理（支持 `http://`、`https://`、`socks5://`、`socks5h://`），日志自动脱敏代理凭据 |
| `upstream.web_search` | `false` | 全局默认是否开启 Amazon Quick 联网搜索（即使关闭，`/v1/responses` 与 `/v1/messages` 声明 `web_search*` 工具时也会按请求动态开启） |
| `upstream.single_client_thread_reuse` | `false` | 单一可信客户端专用实例可开启，配合 `X-Aws-Quick-Conversation` 请求头复用上游会话线程 |
| `upstream.max_frame_bytes` | `63000` | 单帧最大字节数（最小 `8192`），用于上下文拟合与超限重试 |
| `pool.selection_strategy` | `"weighted"` | 多账号选号策略：`weighted`（按剩余额度加权）/ `round_robin`（轮询）/ `sequential`（顺序优先） |
| `features.strict_privacy_dlp` | `true` | 严格隐私脱敏，防止共享推理密钥时泄露上游账号身份 |
| `server.max_payload_bytes` | 24 MiB | 单请求体上限（8 MiB–512 MiB）；超限时先有界排空再返回 JSON `413`，避免客户端连接重置 |
| `server.max_inflight_payload_bytes` | 32 MiB | 并发请求体总预算（8 MiB–512 MiB），chunked 请求按实际字节递增预留，防 OOM 同时兼容高并发流式 |
| `server.trusted_hosts` | `[]` | 本机回环监听 + Nginx/Caddy 反代访问面板时放行的 `Host` 域名白名单（支持热生效） |
| `server.cors_allowed_origins` | `[]` | 可选的浏览器前端 CORS 允许来源（如 `["https://chat.example.com"]` 或 `["*"]`），**仅作用于推理接口**（支持热生效） |

### 命令行参数

| 参数 | 说明 |
| --- | --- |
| `-config <path>` | 指定 `config.json` 路径（默认当前目录或程序同目录）；相对路径的 `auth_dir` / `data_dir` 以此目录为基准 |
| `-no-tray` | 禁用 Windows 系统托盘与弹窗（无头 / 服务模式），等同 `AWSQUICK_NO_TRAY=1` |
| `-open` | 启动监听后自动打开浏览器访问面板 |
| `-export-encrypted <file>` | 将全部账号导出为口令加密迁移包（AES-256-GCM + scrypt）后退出 |
| `-import-encrypted <file>` | 从加密迁移包导入账号后退出（配合 `-overwrite` 覆盖同 UID 账号） |

### 环境变量（优先于 `config.json`）

| 环境变量 | 说明 |
| --- | --- |
| `AWSQUICK_LISTEN` | 监听地址（默认 `127.0.0.1:8045`；Docker 镜像内默认 `0.0.0.0:8045`） |
| `AWSQUICK_API_KEY` | 覆盖主推理密钥（不会写回 `config.json`） |
| `AWSQUICK_ADMIN_KEY` | 覆盖管理面板密钥（不会写回 `config.json`） |
| `AWSQUICK_TRUSTED_HOSTS` | 逗号分隔的面板反代信任 `Host` 白名单（对应 `server.trusted_hosts`） |
| `AWSQUICK_CORS_ORIGINS` | 逗号分隔的推理接口 CORS 白名单（对应 `server.cors_allowed_origins`） |
| `AWSQUICK_PROXY_URL` | 出站代理地址 |
| `AWSQUICK_AUTH_DIR` / `AWSQUICK_DATA_DIR` | 覆盖账号目录 / 数据目录 |
| `AWSQUICK_ENCRYPTION_KEY` | 自定义本地凭据加密密钥 |
| `AWSQUICK_CALLBACK_PORT` | 本地 OAuth 回调端口（默认 `18080`） |
| `AWSQUICK_NO_TRAY` | 设为 `1` / `true` 禁用 Windows 托盘 |
| `AWSQUICK_DEFAULT_REGION` / `AWSQUICK_STAGE` / `AWSQUICK_APP_VERSION` | 高级：覆盖默认 AWS 区域（`us-east-1`）、环境（`prod`）或客户端版本 |

---

## 升级与跨机迁移

- **从旧版原地升级**：先停止服务，备份原程序、`config.json`、`auths/` 和 `data/`，替换新二进制后重启即可；原有 `api_key`、账号凭据与请求归档均自动兼容。
- **跨机器迁移账号**（如本机登录后迁到 Linux 服务器）：
  - 推荐直接在面板点击 **「导出」** 设置 ≥ 12 位加密口令下载 `.enc.json`，再到目标服务器面板点击 **「导入」**。
  - 或使用离线命令行（迁移前请先停止源端进程，避免两端同时轮换同一份 `refresh_token`）：
    ```bash
    ./awsquick2api -export-encrypted ./accounts.enc.json
    ./awsquick2api -import-encrypted ./accounts.enc.json
    ```

---

## 常见问题 (FAQ)

<details>
<summary><strong>1. 部署在无桌面的 Linux 服务器或 Docker 中如何登录账号？</strong></summary>

无需映射或开放 `18080` 端口。通过反代域名或 SSH 转发打开面板后，在本机浏览器中点击授权链接；登录完成跳转到打不开的 `http://localhost:18080/...` 时，复制地址栏完整 URL 粘贴到面板弹窗底部的「远程 / 无头服务器手动粘贴回调」提交即可（也可在本机登录后加密导出再导入服务器）。
</details>

<details>
<summary><strong>2. 配置了 Nginx / Caddy 反代访问面板，却收到 403 <code>host not allowed</code>？</strong></summary>

服务监听本机回环地址时默认开启防 DNS 重绑定校验。请在 `config.json` 的 `server.trusted_hosts`（或环境变量 `AWSQUICK_TRUSTED_HOSTS`）中加入你的反代域名（例如 `quick.example.com`），支持面板内热保存生效。
</details>

<details>
<summary><strong>3. 浏览器 WebUI（如 NextChat / LobeChat 纯前端直连）报跨域 CORS 错误？</strong></summary>

在面板「配置（热生效）」→「常用配置快捷表单」中填写 **推理 CORS 白名单**（如 `https://chat.example.com` 或 `*`），或设置环境变量 `AWSQUICK_CORS_ORIGINS`。该配置仅对 `/v1/*`、`/messages*`、`/responses*` 生效，不会影响管理面板安全。
</details>

<details>
<summary><strong>4. 顶栏出现「上游劣化」提示或调用异常怎么排查？</strong></summary>

顶栏会在最近 5 分钟样本慢响应或 5xx 偏高时自动预警。可先点击顶栏 **「在线测试」** 验证单账号与模型是否正常；需要反馈排查时，可在「运行日志」页点击 **「导出脱敏日志 (ZIP)」** 获取已自动脱敏的诊断日志包。
</details>

---

## 从源码构建

需要 **Go 1.26.11+**：

```bash
# Linux / macOS
CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o awsquick2api ./cmd/awsquick2api

# 交叉编译 Linux amd64 + arm64
./scripts/build-linux.sh        # Windows PowerShell: .\scripts\build-linux.ps1

# 运行全量单元测试
CGO_ENABLED=0 go test -count=1 ./...
```

Windows 系统托盘版（PowerShell）：

```powershell
$env:CGO_ENABLED = "0"
go build -trimpath -ldflags="-s -w -H=windowsgui" -o awsquick2api.exe ./cmd/awsquick2api
```

---

## 注意事项与许可

- 本项目为非官方协议适配工具，与 Amazon / AWS 无隶属关系，仅供个人学习与自有账号在本地或私有网络中使用。
- 请勿公开或提交 `config.json`、`data/encryption.key`、`auths/`、`data/` 与 `*.enc.json`；安全策略见 [SECURITY.md](./SECURITY.md)。
- 基于 [MIT License](./LICENSE) 开源。
