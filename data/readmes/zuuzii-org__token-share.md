<div align="center">

<img src="app/TokenShareIcon-preview.png" alt="Token Share Icon" width="120" height="120" />

<h1>Token Share</h1>

**macOS 原生菜单栏 LLM API 网关**
<br>
在本地完成 OpenAI 与 Anthropic 协议间的实时互译与流式转发

<br>

![Swift 6.1](https://img.shields.io/badge/Swift-6.1-F05138?logo=swift&logoColor=white)
![macOS 14+](https://img.shields.io/badge/macOS-14.0+-000000?logo=apple&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

简体中文 | [English](README.en.md)

</div>

<br>

<div align="center">
<img src="docs/images/token-share-1.png" alt="" width="30%"/>
<img src="docs/images/token-share-2.png" alt="" width="30%"/>
<img src="docs/images/token-share-3.png" alt="" width="30%"/>
</div>


## 特性

- **协议互译** — OpenAI Chat Completions · OpenAI Responses · Anthropic Messages，任意方向
- **流式透传** — SSE 逐事件转换，覆盖文本增量、工具调用与流式中断
- **多服务商** — 任意数量上游配置，一键热切换
- **模型同步** — 自动拉取上游模型列表，支持手动刷新
- **纯本地** — 全部流量走 localhost，无注册、无遥测

## 快速开始

> 要求 macOS 14+、Xcode 16+、Swift 6+

> 从 GitHub Release 下载的包未做 Apple 公证。首次打开如果被系统拦截，可在终端执行：
> `xattr -dr com.apple.quarantine /Applications/TokenShare.app`

```bash
git clone https://github.com/leemysw/token-share.git
cd token-share
swift build && swift run TokenShare
```

或用 Xcode 打开 `TokenShare.xcodeproj` 直接运行。

## 端点

启动后默认监听 `localhost:9091`：

| 路径 | 协议 |
|------|------|
| `/v1/chat/completions` | OpenAI Chat Completions |
| `/v1/responses` | OpenAI Responses |
| `/v1/messages` | Anthropic Messages |
| `/v1/models` | 模型列表 |
| `/health` | 健康检查 |

## 工作原理

```
                         localhost:9091
                              │
┌─────────────┐    ┌──────────┴──────────┐    ┌──────────────┐
│             │───▶│                     │───▶│              │
│  AI Client  │    │     Token Share     │    │ LLM Provider │
│             │◀───│                     │◀───│              │
└─────────────┘    └─────────────────────┘    └──────────────┘
  OpenAI 协议         协议识别 → 翻译 → 转发        Anthropic 协议
  Anthropic 协议       SSE 逐事件流式转换          OpenAI 协议
```

## 许可

[Apache-2.0](LICENSE)
