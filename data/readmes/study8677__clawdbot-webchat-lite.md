# Clawdbot WebChat Lite

[English](./README_en.md)

<p align="center">
  <img src="./assets/banner.svg" alt="Clawdbot WebChat Lite" width="800" />
</p>

**一个轻量、可自部署、国内可用的 Clawdbot 聊天客户端。**  
不造新频道，只做“对话这件事”。

---

## 第一性原理
- **对话是核心**：一切功能围绕“稳定对话”而不是功能堆叠。
- **连接即价值**：直连 Gateway WS，避免中间层与复杂依赖。
- **最小维护成本**：不造新 channel、不改 Clawdbot 内核。
- **国内可用优先**：可自部署、可反向代理、可控网络链路。

---

## 功能亮点
- 连接 Gateway（URL + token/password）
- 会话列表（`sessions.list`）
- 消息历史与发送（`chat.history` / `chat.send`）
- 实时 WS 通知
- 认证预设（本地保存）

---

## 快速开始
```bash
cd clawdbot-webchat-lite
npm install
npm run dev
```

---

## 使用说明
- 客户端直接连接 Gateway WebSocket。
- 若 Gateway 需要 header 认证，可用反向代理注入 header，或在 WS URL 中携带 token。

---

## 适合谁用
- 想要**更友好国内网络环境**的 Clawdbot 用户
- 想要**极简开源客户端**的开发者

---

## 路线图
- PWA（离线缓存 / 桌面安装）
- 会话搜索与收藏
- 多 Gateway 切换

---

如果你喜欢这个项目，欢迎 Star / PR。
