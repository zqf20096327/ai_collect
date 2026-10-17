# 网页版大模型反向适配网关

把「网页版大模型」包装成标准 OpenAI 兼容接口的三件套，方便接入自建中转、客户端或自动化脚本。

三个子项目相互独立，可单独部署：

| 子项目 | 上游 | 对外协议 | 默认端口 | 模型名 |
| --- | --- | --- | --- | --- |
| `doubao-gateway` | 豆包网页版 | Chat Completions | `8787` | `doubao-web` |
| `deepseek-gateway` | DeepSeek 网页版 | Chat Completions / Responses | `8788` | `deepseek-web` |
| `kimi-gateway` | Kimi 网页版 | Chat Completions / Responses | `8789` | `kimi-web` |
| `workbuddy-bridge` | WorkBuddy CLI | Responses | `18088` | `dsv4.1flash`、`glmv5.3flash` |

## 共同思路

三者都不做协议破解，而是复用**已经人工登录好的浏览器/CLI 会话**：

1. 容器内跑一个独立的 Chromium（或第三方 CLI）；
2. 通过 noVNC 人工登录一次，登录态持久化到 Docker 卷；
3. 网关把这层会话包装成 HTTP 接口，上游返回的 SSE 再翻译成标准响应格式。

Cookie 与令牌始终留在容器内的浏览器配置目录里，不会被导出。

其中 Kimi 走 Connect RPC（protobuf over HTTP），响应为 5 字节信封头加 JSON 载荷；
网关在页面上下文内旁路留存原始响应字节，不解析也不复制鉴权头。

## 快速开始

每个子目录都有自己的 README，按需进入对应目录执行即可。

```sh
cd doubao-gateway   && docker compose up -d --build
cd deepseek-gateway && cp .env.example .env && docker compose up -d --build
cd kimi-gateway     && cp .env.example .env && docker compose up -d --build
cd workbuddy-bridge && docker compose up -d --build
```

## 安全约定

- 所有管理端口（CDP / noVNC）只绑定 `127.0.0.1`，通过 SSH 隧道访问，不要直接暴露公网。
- 登录面板没有密码保护，务必保持回环绑定。
- 各服务的密钥通过 `.env` 或配置文件注入，仓库内只提供占位示例。

## 目录结构

```text
web-llm-gateways/
├── doubao-gateway/     # 豆包网页版网关
├── deepseek-gateway/   # DeepSeek 网页版网关
├── kimi-gateway/       # Kimi 网页版网关
└── workbuddy-bridge/   # WorkBuddy CLI 到 Responses API 的桥接
```

## 限制

- 全部为单并发设计，同时请求返回 429。
- 仅支持文本对话，不支持工具调用、附件、图片、视频。
- 依赖上游网页前端结构，对方改版后适配层需要同步更新。
- `workbuddy-bridge` 需要自行准备第三方 CLI 产物，本仓库不包含。

## 许可

MIT License，详见 [LICENSE](LICENSE)。

本项目只做协议适配，不绕过任何付费或鉴权机制。使用前请自行确认符合各上游服务的条款。
