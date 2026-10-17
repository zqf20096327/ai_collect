<p align="center">
  <img src="https://img.shields.io/npm/v/wechat-dev-mcp.svg" alt="npm version" />
  <img src="https://img.shields.io/badge/node-%3E%3D18-brightgreen.svg" alt="node" />
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="license" />
</p>

<h1 align="center">微信开发者工具 MCP</h1>

<p align="center"><b>用大白话让 AI 帮你调试微信小程序 / 小游戏。</b></p>

<p align="center">
  <a href="README_EN.md">🇺🇸 English</a> · 🇨🇳 中文
</p>

---

你只要对 AI 说人话，剩下的它自己连、自己查报错、自己截图验证：

> 🗣️ 「打开我的小程序 → 跳到首页 → 点登录按钮 → 截图看效果」
>
> 🎮 「打开小游戏 → 在第 2 行第 10 列落子 → 截张图 → 导出日志」

兼容 WorkBuddy、Claude Code、Cursor、Cline、Zed 等任意 MCP 客户端。

---

## 🚀 3 步上手

**1. 安装**
```bash
npx -y wechat-dev-mcp
```

**2. 接进你的客户端**（命令都一样，只差配置文件位置）

以 Cursor 为例，编辑 `~/.cursor/mcp.json`：
```json
{
  "mcpServers": {
    "wechat-devtools": {
      "command": "npx",
      "args": ["-y", "wechat-dev-mcp"]
    }
  }
}
```
> 仓库已附带 `.cursor/mcp.json` / `.mcp.json`，也可直接用 [`examples/cursor-mcp-config.json`](examples/cursor-mcp-config.json)。其它客户端（Claude Code / Desktop、Codex、Windsurf、Cline、Zed）配置方式见各自文档，命令相同。

**3. 开干 —— 直接用自然语言跟 AI 说**

> 「帮我打开 `/Users/你/项目` 这个小程序，跳到首页，点登录，然后截图给我看」

就这么简单。

---

## ✅ 准备工作（一次就好）

- 装好 **微信开发者工具**，并开启**服务端口**：`设置 → 安全设置 → 服务端口`
- 本机 **Node.js ≥ 18**

> ⚠️ 没开「服务端口」会报 `Connection refused`。

---

## 🧩 配套 Skill（可选，但推荐）

[wechat-dev-skill](https://github.com/jiawei686/wechat-dev-skill) 把"扫 build / devtools / output / networks 四来源报错"做成一句话流程。装上后直接对 AI 说「调试一下这个项目」即可，它会自动定位报错。

---

## 🛠 能做什么（节选）

- 📸 **截图**：小程序页面 / 小游戏画布实时截图
- 🖼 **画布导出**：`export_canvas` 把页面里 `<canvas>` 的**真实内容**导出成 PNG
- 👆 **触控**：模拟点击、长按、滑动（小游戏落子自动坐标补偿，落点精准）
- 📜 **读日志**：console / vConsole / 网络请求，定位报错
- 🔄 **重开**：一键重开并重新编译（不用易崩的 `Page.reload`）
- 🧪 **功能验证**：自动连模拟器、跑流程、核对 UI

> ⚠️ **截图看不到 `<canvas>`**。automator 的页面截图只合成普通节点，画布区域会显示成一块纯底色。
> 实测：把整块画布涂成纯红再截图，前后两张 PNG **逐字节完全相同**。
> 所以凡是往 canvas 里画的页面（相册预览、美化、增强、马赛克……），
> 别用截图判断「画出来没有」，要用 `export_canvas`。

小游戏完整文档见 [docs/MINIGAME_GUIDE.md](docs/MINIGAME_GUIDE.md)。

---

## ❓ 常见问题

| 问题 | 解决 |
|------|------|
| `Connection refused` | 开发者工具在跑 + 「服务端口」已开 |
| 启动报 `make sure http port is open` | 冷启动竞态：第一次 `cli auto` 拉起 IDE 后自己退出了。手动开一次项目再重试；或先 `cli auto --project <路径> --auto-port 9420`，再用 `connect` 直连 |
| 截图里 canvas 区域是纯色 | 正常现象，见上方说明；改用 `export_canvas` 看画布内容 |
| `get_console_logs` 说没有日志 | 日志只从**连接那一刻**开始收集。要抓启动期的报错，先连上再重启项目 |
| 小游戏点不动 | 先让游戏进入可交互界面（如说"开始游戏"），再让 AI 触控 |
| 落子位置偏了 | 用 `game_tap_grid`（已含补偿）；仍偏再标定 |
| 游戏卡死 | 让 AI 用 `restart_project` 重开，**别**用 `Page.reload` |
| `evaluate` 返回 undefined | 脚本是按**函数体**编译的（`new Function`），必须显式 `return`：写 `return 1+1`，不是 `1+1` |
| 连发几个有状态调用（`navigate_to` / `tap_element` / `input_text`）只有第一个生效 | 这类调用**一条消息只发一个**，等返回再发下一个。并行发出会互相覆盖 —— 而且**每个都回报成功**，状态被静默丢弃，只有查 `get_page_stack` 才发现落点不对 |

---

[MIT License](LICENSE) © CuiJiawei · 欢迎 Issue / PR
