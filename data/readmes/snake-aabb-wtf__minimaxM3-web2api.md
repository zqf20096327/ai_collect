# 🚀 MiniMax Agent Web2API

> **将 MiniMax Agent 网页聊天逆向为 OpenAI 兼容的 API 代理**  
> 基于 [webai2api](https://github.com/snake-aabb-wtf/skill-webAI2api) skill 构建

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)

> **[🇺🇸 English Version](README.en.md)** — Click for English docs

---

## 📋 目录

- [概述](#-概述)
- [快速开始](#-快速开始)
- [工作原理（必读）](#-工作原理必读)
- [配置文件详解](#-配置文件详解)
- [API 参考](#-api-参考)
- [项目结构](#-项目结构)
- [常见问题](#-常见问题)
- [许可证](#-许可证)

---

## 🔭 概述

本项目通过逆向 MiniMax Agent（`agent.minimaxi.com`）网页前端的 **JavaScript 签名算法**，将网页聊天接口转化为完全 **OpenAI 兼容** 的 REST API 代理。

### 核心能力

| 能力 | 状态 | 说明 |
|------|------|------|
| **动态签名** | ✅ | 逆向 JS 签名算法，任意消息内容实时签名 |
| **工具调用 (DSML)** | ✅ | 通过 DSML 注入实现 OpenAI 格式 function calling |
| **流式/非流式** | ✅ | SSE 流式和一次性响应均支持 |

---

## ⚡ 快速开始

### 前置要求

- Python 3.10+
- MiniMax Agent 账号
- 从 `agent.minimaxi.com` 导出的 HAR 文件

### 获取 HAR 文件

```
F12 → Network → 勾选 "Preserve log" → 发送一条消息 → 右键 "Save all as HAR with content"
```

### 配置 & 启动

**Windows：**
```
双击 start-config-tool.bat  →  选择 HAR  →  解析  →  保存到 .env
双击 start.bat
```

**Linux/macOS：**
```bash
chmod +x start-config-tool.sh && ./start-config-tool.sh
chmod +x start.sh && ./start.sh
```

### 验证

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"MiniMax-M3","messages":[{"role":"user","content":"你好！"}],"stream":false}'
```

---

## 🔬 工作原理（必读）

要理解本项目，需要先理解 MiniMax 网页端是如何调用自己的 API 的。

### MiniMax 的请求签名机制

MiniMax Agent 的前端每次请求 API 时，会自动在请求头中添加以下四个字段：

| 请求头 | 示例 | 说明 |
|--------|------|------|
| `token` | `eyJhbGciOiJIUzI1NiIs...` | JWT 登录令牌 |
| `x-timestamp` | `1780470413` | Unix 时间戳（秒） |
| `x-signature` | `2abd46524d558934...` | 32 位十六进制字符串，基于消息体计算 |
| `yy` | `98b376ad1900c0a6...` | 32 位十六进制字符串，基于完整 URL + 消息体计算 |

这四个头由前端 **Webpack 模块 97516** 中的函数 `L()` 自动生成，用户无感知。

### 逆向过程

> `sign.py` 的诞生

我们从 CDN 下载了 MiniMax 前端的所有 JS chunk（`page-4b56d0957bacb085.js` 等），在其中定位到了关键的 Webpack 模块：

| 模块 ID | 功能 | 文件 |
|---------|------|------|
| **97516** | 主签名函数 `L()`，组装所有请求头 | page chunk |
| **52724** | `yy` 签名计算函数 | page chunk |
| **65776** | 客户端元数据生成（URL 参数） | page chunk |
| **96467** | MD5 哈希实现 | vendor chunk |

从模块 97516 中提取出的核心代码片段：

```javascript
// x-signature: MD5(时间戳秒 + 静态密钥 + 请求体)
w["x-signature"] = i()(`${a}I*7Cf%WZ#S&%1RlZJ&C2${v}`)
// 其中 a = 时间戳秒, v = JSON.stringify(请求体)
```

```javascript
// yy: MD5(encodeURIComponent(完整URL含参数) + "_" + 请求体 + MD5(毫秒时间戳) + "ooui")
let l = `${encodeURIComponent(t)}_${o}${i()(a.toString())}ooui`;
return i()(l)
```

### 签名算法详解

#### x-signature（已验证，100% 准确）

```
x-signature = MD5(
    timestamp_seconds +       # 当前 Unix 时间戳（秒）
    "I*7Cf%WZ#S&%1RlZJ&C2" + # 硬编码静态密钥（从 JS 中提取）
    body_string               # JSON.stringify 后的请求体
)
```

- ✅ **URL 无关**：签名仅依赖时间戳 + 密钥 + 请求体，与 URL 路径无关
- ✅ **已验证**：使用 HAR 中原始时间戳和请求体重算，100% 匹配

#### yy（算法正确，依赖运行时参数）

```
yy = MD5(
    encodeURIComponent(full_url_with_params) + "_" +
    body_json +
    MD5(str(timestamp_ms)) +
    "ooui"
)
```

- `full_url_with_params` = API 路径 + 所有客户端元数据参数（按 JS `URLSearchParams` 的插入顺序序列化）
- `body_json` = `JSON.stringify(body_obj)`，与 `x-signature` 使用的同一 body
- `timestamp_ms` = 毫秒时间戳
- `"ooui"` = 固定后缀字符串

**yy 需要浏览器运行时参数**（UUID、device_id、user_id、screen 尺寸等），这些参数从 HAR URL 的 query string 中提取，保存在 `.env` 中供运行时使用。

### 请求流程

```
┌─ 你的应用 ─────────────────────────────┐
│  POST /v1/chat/completions              │
│  {"messages":[{"role":"user",           │
│    "content":"你好！"}],"stream":true}   │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌─ server.py ────┬────────────────────────┐
│  ① 解析 OpenAI 格式请求                  │
│  ② 调用 adapter.py                       │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌─ adapter.py ───┬────────────────────────┐
│  ③ 构造 MiniMax 格式消息体               │
│     {"content":"你好！",                  │
│      "model":{...},                      │
│      "turn_id":"xxx",                    │
│      "worktreeMode":false}               │
│                                          │
│  ④ 调用 sign_request() 生成签名          │
│     sign.py ──────────────────┐          │
│       x-timestamp = now()     │          │
│       x-signature = MD5(      │          │
│         ts + secret + body)   │          │
│       yy = MD5(              │          │
│         enc_url + "_" +      │          │
│         body + md5(ts_ms) +  │          │
│         "ooui")              │          │
│     ←────────────────────────┘          │
│                                          │
│  ⑤ 发送请求到 MiniMax                   │
│     POST /session/{id}/message           │
│     Headers: token, x-timestamp,         │
│              x-signature, yy             │
│     Body: 消息体                          │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌─ MiniMax ──────┬────────────────────────┐
│  ⑥ 验证签名通过 ✅                        │
│  ⑦ 返回 SSE 流式响应                      │
│     data:{"type":6,"agent_message_chunk": │
│       {"msg_content":"你好"}}             │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌─ adapter.py ───┬────────────────────────┐
│  ⑧ 解析 SSE，提取 msg_content            │
│  ⑨ 组装 OpenAI 格式响应                  │
└────────────────┬───────────────────────┘
                 │
                 ▼
┌─ 你的应用 ─────────────────────────────┐
│  {"choices":[{"delta":                 │
│    {"content":"你好"}}]}                │
└────────────────────────────────────────┘
```

### 为什么不需要 Cookie？

传统方案往往需要 Cookie 来维持登录态。但 MiniMax 的 API 使用 **JWT Token** 认证——Token 直接放在 URL query string 和请求头中，与 Cookie 无关。本项目通过 HAR 提取 Token，然后在每次请求中：

1. 将 Token 放入 URL query（`?token=...`）
2. 将 Token 放入请求头（`token: ...`）

与前端浏览器行为完全一致。

### 签名密钥的安全性

`sign.py` 中硬编码的密钥 `I*7Cf%WZ#S&%1RlZJ&C2` 是从 MiniMax 前端 JS 中提取的**公开密钥**。它随前端代码分发，任何浏览器都可以通过开发者工具获取，不属于敏感信息。这与任何前端应用的 API 密钥公开方式相同。

---

## ⚙ 配置文件详解

### `.env` — 由 config_tool.py 生成

| 变量 | 来源（HAR 中的位置） | 用途 | 是否必须 |
|------|---------------------|------|---------|
| `TOKEN` | URL query `token` | JWT 认证令牌，放在请求头和 URL 中 | ✅ |
| `AGENT_ID` | URL 路径 `/agent/{id}/session` | 指定调用哪个 Agent | ✅ |
| `UUID` | URL query `uuid` | 浏览器指纹；用于 yy 签名计算 | ✅ |
| `DEVICE_ID` | URL query `device_id` | 设备标识；用于 yy 签名计算 | ✅ |
| `USER_ID` | URL query `user_id` | 用户 ID；用于 yy 签名计算 | ✅ |
| `SCREEN_WIDTH` | URL query `screen_width` | 屏幕宽度；用于 yy 签名计算 | ✅ |
| `SCREEN_HEIGHT` | URL query `screen_height` | 屏幕高度；用于 yy 签名计算 | ✅ |
| `TARGET_URL` | URL scheme + host | MiniMax 基础地址 | ✅ |
| `STREAM_URL` | SSE 请求的 URL host | MiniMax 流式地址 | ✅ |
| `USER_AGENT` | 请求头 `User-Agent` | 请求 User-Agent | ✘ |

### `config_tool.py` 做了什么

```
打开 HAR 文件
  ↓
扫描所有请求，找到:
  ├─ Session 创建请求 (POST /agent/{id}/session)
  └─ SSE 消息请求 (Content-Type: text/event-stream)
  ↓
从 URL 中提取:
  ├─ token, agent_id
  ├─ uuid, device_id, user_id
  ├─ screen_width, screen_height
  └─ stream_url
  ↓
写入 .env 文件
```

### `sign.py` 不需要配置

`sign.py` 是纯函数库，无外部依赖，无配置文件。它只通过函数参数接收输入：

```python
from sign import sign_request

result = sign_request(
    body_str='{"content":"你好"}',     # 请求体 JSON 字符串
    token="eyJ...",                    # JWT Token
    url_path="/archon/api/v1/session/xxx/message",  # API 路径
    uuid="...", device_id="...",       # 浏览器参数
    user_id=..., screen_width=...,
    screen_height=...,
)
# 返回: {"x-timestamp": "...", "x-signature": "...", "yy": "..."}
```

---

## 📖 API 参考

### `POST /v1/chat/completions`

OpenAI 完全兼容。

#### 流式响应 (SSE)

```
data: {"choices":[{"delta":{"role":"assistant"},"index":0}]}
data: {"choices":[{"delta":{"content":"你好"},"index":0}]}
data: {"choices":[{"delta":{},"finish_reason":"stop","index":0}]}
data: [DONE]
```

#### 非流式响应

```json
{
  "choices": [{"message": {"role": "assistant", "content": "你好！"}}]
}
```

### 工具调用 (Function Calling)

支持通过 `tools` / `tool_choice` 参数声明工具，模型会以 **DSML** 格式返回工具调用。

> DSML (DeepSeek Markup Language) 是一种 XML 风格的标签语言，用于在缺乏原生 function calling 的模型上实现工具调用。

#### 请求示例

```json
{
  "model": "MiniMax-M3",
  "messages": [
    {"role": "system", "content": "你是一只猫娘，当前在卧室里。"},
    {"role": "user", "content": "我饿了，带我去厨房"}
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "move",
        "description": "移动到指定位置",
        "parameters": {
          "type": "object",
          "properties": {
            "target": {"type": "string", "description": "目标位置"}
          },
          "required": ["target"]
        }
      }
    }
  ],
  "tool_choice": "auto",
  "stream": true
}
```

#### 流式响应 (工具调用)

```
data: {"choices":[{"delta":{"role":"assistant","content":null},"index":0}]}

data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"call_xxx","type":"function","function":{"name":"move","arguments":"{\"target\":\"厨房\"}"}}]},"index":0}]}

data: {"choices":[{"delta":{},"finish_reason":"tool_calls","index":0}]}

data: [DONE]
```

#### 非流式响应 (工具调用)

```json
{
  "choices": [{
    "message": {
      "role": "assistant",
      "content": null,
      "tool_calls": [{
        "id": "call_xxx",
        "type": "function",
        "function": {
          "name": "move",
          "arguments": "{\"target\": \"厨房\"}"
        }
      }]
    },
    "finish_reason": "tool_calls"
  }]
}
```

#### 工作原理

```
你的请求 (含 tools 定义)
  ↓
adapter.py 将工具定义转为 DSML 指令注入到用户消息中
  ↓
MiniMax 模型理解 DSML 格式，回复时嵌入 <|DSML|invoke> 标签
  ↓
StreamSieve 引擎从 SSE 流中实时分离出 DSML 标签
  ↓
tool_dsml.py 将 DSML 解析为标准 OpenAI tool_calls 格式
  ↓
你收到标准的 OpenAI 工具调用响应
```

### `GET /v1/models` / `GET /health`

---

## 📁 项目结构

```
web2api/
├── sign.py             ← 逆向出的签名算法（纯函数，无需配置）
├── tool_dsml.py        ← DSML 工具调用格式解析器（注入 + 解析 + 互转）
├── tool_sieve.py       ← StreamSieve 流式标签分离引擎
├── adapter.py          ← MiniMax API 适配器（调用 sign.py 签名 + DSML）
├── server.py           ← FastAPI 代理服务器（OpenAI 兼容接口）
├── config_tool.py      ← GUI 配置工具（解析 HAR → 生成 .env）
├── .env                ← 配置文件（由 config_tool.py 生成）
├── .env.example        ← 配置模板
├── start.bat / start.sh                     ← 一键启动服务器
├── start-config-tool.bat / start-config-tool.sh  ← 一键启动配置工具
├── README.md / README.en.md
└── LICENSE
```

### 文件职责

| 文件 | 职责 | 需要配置？ |
|------|------|-----------|
| `sign.py` | 纯算法，接收参数返回签名 | ❌ 无需配置 |
| `adapter.py` | 业务逻辑：构造请求 → 调用 sign.py → 发请求 → 解析 SSE | ❌ 从 .env 读取配置 |
| `server.py` | HTTP 服务：接收 OpenAI 格式 → 转给 adapter | ❌ 从 .env 读取配置 |
| `config_tool.py` | 工具：HAR → 提取参数 → 写入 .env | ❌ 只需用户选择 HAR 文件 |
| `.env` | 配置存储 | ✅ 由 config_tool.py 生成 |

### 数据流

```
config_tool.py          sign.py                adapter.py
    │                     │                       │
    │  解析 HAR           │                       │
    │  提取 token,        │  纯算法，              │  读取 .env
    │  uuid, device_id    │  无状态                │  构造消息体
    │  等参数              │  输入→输出             │  调用 sign.py
    │     │               │     │                 │  发 HTTP 请求
    │     ▼               │     ▼                 │  解析 SSE
    │  .env ──────────────┼─────┼────────────────▶│  返回 OpenAI 格式
    │                     │                       │
```

---

## 🐛 常见问题

**Q: 什么是 x-signature？**
A: MiniMax 前端用 `MD5(时间戳 + 静态密钥 + 请求体)` 生成的请求签名。本项目将其逆向实现于 `sign.py`。

**Q: 什么是 yy？**
A: 另一个签名，用 `MD5(encodeURIComponent(完整URL) + "_" + 请求体 + MD5(毫秒时间戳) + "ooui")` 计算。需要浏览器运行时参数。

**Q: sign.py 需要配置吗？**
A: 不需要。它是纯函数库，只接收参数返回签名，无外部依赖。

**Q: 为什么需要 HAR 文件？**
A: 为了提取 Token（JWT 认证）和浏览器参数（UUID/device_id 等 yy 签名所需参数）。

**Q: Token 过期了怎么办？**
A: 重新捕获 HAR，运行 `config_tool.py` 更新 `.env`。

**Q: 支持工具调用 (function calling) 吗？**
A: 支持。通过 DSML 注入方式实现。提交请求时传入 `tools` 和 `tool_choice` 参数即可，流式响应中会返回标准 OpenAI 格式的 `delta.tool_calls`。见 [API 参考 - 工具调用](#-api-参考)。

---

## 📄 许可证

本项目基于 **GNU General Public License v3.0** 发布。

---

<p align="center">
  <a href="README.en.md">🇺🇸 English Version</a>
</p>
