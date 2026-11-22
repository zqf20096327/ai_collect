<div align="center">

# 书桌防线 · Desk Defense

**在书桌上用文具摆迷宫的塔防游戏，也可以让大模型来玩。**

**简体中文** · [English](README.en.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

[![在线试玩](https://img.shields.io/badge/%E5%9C%A8%E7%BA%BF%E8%AF%95%E7%8E%A9-jjjj.games-d4a73c)](https://jjjj.games)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LINUX DO](https://img.shields.io/badge/LINUX-DO-ffb003?labelColor=3f3f46)](https://linux.do/)

[在线试玩](https://jjjj.games) · [介绍页](https://jjjj.games/about) · [玩家指南](docs/guide/README.md) · [AI 参战](docs/10-Agent参战.md) · [参与开发](CONTRIBUTING.md)

本项目在 [LINUX DO](https://linux.do/) 社区发布与交流

<img src="public/og.png" alt="书桌防线" width="720">

</div>

## 这是什么

书桌防线是一款迷宫式塔防游戏。棋盘是一张 12×14 的书桌，铅笔、订书机、台灯、圆规这些文具就是塔；每座塔（包括墙）都会挡路，所以怎么摆塔，就是怎么修迷宫。

浏览器打开就能玩，手机、平板、电脑都支持，也可以装成 PWA，或者打包成 iOS / Android / 桌面应用。不用注册，进度保存在本机。

除了自己玩，还可以接入大模型：让 AI 替你打、给你出主意、给你出题，或者让两个模型对打。

<img src="docs/images/menu.jpg" alt="开始菜单" width="720">

## 玩法内容

- **3 种模式**：战役（3 章）、无尽（简单、普通、困难、噩梦、魔境 I～X）、自定义；另有每日挑战。
- **12 座塔、16 种敌人和 Boss、9 种精英词缀**：塔从 Lv1 升到 Lv10，Lv10 选传奇分支 A / B，之后还能进化到 ★3 解锁主动能力。
- **10 个主动技能、20 个局内增益、永久天赋**，相邻塔有组合技。
- **动态战场**：多点出怪、空降出生点、随机事件、随机杂物布局，每局地形都不一样。
- **全服排行榜**：无尽、每日、战役三个榜，外加 AI 榜和 AI 对战榜。核心逻辑完全确定性，成绩带完整指令日志，可以回放复现。
- **四种语言**：简体中文、繁体中文、English、日本語；浅色 / 深色主题。
- **原创美术和配乐**：塔和敌人都是 SVG 几何扁平风，背景音乐由 WebAudio 实时合成（4 套曲风）。

## AI 参战：让大模型来玩

主菜单「AI 参战」里有四种玩法：

| 玩法 | 说明 |
|---|---|
| AI 玩家 | 模型从第 1 波开始全程操作，你在旁边看它的思路和每一步操作 |
| AI 军师 | 你自己玩，模型只给建议，可以一键执行 |
| AI 出题 | 模型扮演进攻方，每波开始前改写下一波的敌人，你来防守 |
| AI 对战 | 两个模型同局对抗：一个出题进攻，一个建塔防守 |

- **模型来源**：Claude、OpenAI、Gemini、DeepSeek 等托管 API，OpenAI 兼容的中转服务，本机的 Ollama / LM Studio，或者不需要 Key 的离线演示。
- **中心策略**：开局可以指定「铅笔流」「范围流」「光束流」等打法，或者让 AI 自己选，也能中途用一句话改。
- **随时下指令**：对局中可以直接对 AI 说「多造防空」「先存钱」「把迷宫拉长」。
- **看得见的思路**：侧栏实时显示每次发给模型的局面、模型的思考、调用的工具和操作结果。
- **公平**：AI 的每个操作都和玩家点击走同一套校验，不能作弊；AI 成绩单独排名，不混进真人榜。
- **省钱**：上下文增量发送、前缀缓存、预算分级；按模型显示思考档位与费用估算（价格数据来自 [modelinfo.dev](https://modelinfo.dev)）。
- **Key 的安全**：API Key 默认只存在内存里，可选存到 sessionStorage（关标签页即清除）；只从你的浏览器直连模型服务，**不会发到本站服务器**。

除了网页，也可以用命令行或 MCP 接入：

```bash
npm run agent:play -- --provider scripted --max-waves 10
```

```bash
npm run mcp
```

`agent:play` 在终端里无头跑一整局并输出报告（上面这条用内置策略，不需要 Key；全部参数见 `scripts/agent-play.ts` 开头）；`mcp` 启动 MCP 服务，Claude Code、Claude Desktop 等客户端可以直接当玩家。详见 [文档 10](docs/10-Agent参战.md)。

## 快速开始

需要 Node.js 22.22 或更高版本。

```bash
git clone https://github.com/Owlbay/desk-defense.git
```

```bash
cd desk-defense && npm install
```

```bash
npm run dev
```

打开终端里显示的地址就能玩。手机和电脑在同一个局域网时，用手机打开终端里的 Network 地址，就能在手机上玩。

| 命令 | 作用 |
|---|---|
| `npm run dev` | 开发服务器（热更新） |
| `npm run build` | 类型检查并打包到 `dist/`（含 PWA，可以部署到任意静态托管） |
| `npm run preview` | 本地预览打包结果 |
| `npm run check` | 提交前检查：类型检查、ESLint、Prettier、单元测试（CI 同款） |
| `npm run dev:api` | 打包后用 wrangler 在本地起带排行榜接口的完整站点 |
| `npm run sim -- --scenario calib` | 平衡模拟：用机器人跑各难度，报告在 `scripts/out/report.html` |
| `npm run agent:eval` | AI 评测：同一批种子对比不同模型 / 配置 / 中心策略 |
| `npm run cap:ios` / `npm run cap:android` | 构建并同步到 Capacitor 原生工程 |
| `npm run tauri:dev` / `npm run tauri:build` | Tauri 桌面版开发 / 打包 |

## 自己部署

纯静态部分（`dist/`）可以放到任何静态托管。全服排行榜需要 Cloudflare Pages Functions + D1：

1. 创建数据库：`npx wrangler@4 d1 create desk-defense`，把输出的 `database_id` 填进 `wrangler.toml`。
2. 建表：`npm run db:migrate:remote`。
3. 设置机密：`npx wrangler@4 pages secret put HASH_SALT --project-name desk-defense`（随机长串，用来哈希 IP 和设备 ID）。
4. 部署：`npm run deploy`。

没有绑定数据库时，游戏显示「在线功能不可用」，其他功能照常。详见 [文档 12](docs/12-全服排行榜.md)。

原生应用（iOS / Android / 桌面）用同一份 `dist/` 套壳，步骤见 [文档 07 §2.3](docs/07-技术与多平台.md)。仓库里不含任何签名配置和商店账号。

## 代码结构

| 目录 | 内容 |
|---|---|
| `src/core/` | 纯游戏逻辑（不依赖浏览器，完全确定性）：世界状态、寻路、战斗、波次、技能、增益 |
| `src/config/` | 全部数值配置：塔、敌人、词缀、技能、增益、天赋、难度、地图、战役 |
| `src/render/` | Phaser 棋盘渲染、特效、棋盘上的触摸和鼠标输入 |
| `src/ui/` | HTML 界面：菜单、局内 HUD、图鉴、AI 侧栏、配乐 |
| `src/agent/` | AI 参战：观测、意图规划器、工具、中心策略、各家模型适配 |
| `src/meta/` | 存档、进度、解锁、排行榜、回放 |
| `src/shared/` | 前端和服务端共用的校验与编码 |
| `functions/` | Cloudflare Pages Functions（`/api/*` 排行榜接口） |
| `migrations/` | D1 数据库迁移 |
| `scripts/` | 平衡模拟、机器人、AI 评测、MCP 服务、文档和美术生成 |
| `tests/` | 单元测试（500+ 个，不需要网络） |
| `art/` | SVG 美术源文件（`art/gallery.html` 预览全部素材） |

技术栈：TypeScript、Phaser 3、Vite、Vitest；Cloudflare Pages + D1；Capacitor、Tauri。

## 设计文档

| 章节 | 内容 |
|---|---|
| [01 概述与玩法](docs/01-概述与玩法.md) | 核心循环、网格与寻路、操作方式、界面布局、新手引导 |
| [02 防御塔](docs/02-防御塔.md) | 12 座塔、Lv1–10 与 4 种形态、升级与出售、组合技 |
| [03 敌人](docs/03-敌人.md) | 12 种普通敌人、4 个 Boss、9 种精英词缀 |
| [04 模式与难度](docs/04-模式与难度.md) | 战役、无尽、自定义；难度参数、成长公式、波次生成 |
| [05 技能与能力](docs/05-技能与能力.md) | 主动技能、局内增益、永久天赋 |
| [06 美术与建模](docs/06-美术与建模.md) | 调色板、SVG 图层规范、动画、素材流程 |
| [07 技术与多平台](docs/07-技术与多平台.md) | 架构、多平台路线、性能预算、存档 |
| [08 实现约定](docs/08-实现约定.md) | core / render / ui 的边界与接口 |
| [09 动态战场](docs/09-动态战场.md) | 多点出怪、空降、随机事件、自动波次、随机地形 |
| [10 Agent 参战](docs/10-Agent参战.md) | 大模型接入、提示与上下文、意图规划器、评测、中心策略 |
| [11 传奇进化](docs/11-传奇进化.md) | 传奇分支与进化 |
| [12 全服排行榜](docs/12-全服排行榜.md) | 接口、防作弊、回放复核、部署 |
| [玩家指南](docs/guide/README.md) | 面向玩家的完整说明与自动生成的数据表 |

## 反馈与交流

- **Bug 和建议**：[提交 Issue](https://github.com/Owlbay/desk-defense/issues)。最好附上种子（暂停菜单里可以复制）、难度和浏览器；成绩自带回放，复现起来很快。
- **讨论和晒成绩**：欢迎在 [LINUX DO](https://linux.do/) 发帖交流，聊聊你的模型打到了第几波、哪种中心策略最好用。
- **用 AI 玩时报错**：截图或复制侧栏里的报错就行，**先把 Key 从截图和日志里去掉**。

## 参与贡献

欢迎提 Pull Request。开始之前请先读 [CONTRIBUTING.md](CONTRIBUTING.md)，里面有目录约定、确定性要求、国际化、测试与部署流程。提交前跑一遍 `npm run check`。

## 开源说明

- **完整开源**：游戏客户端、服务端接口（`functions/`）、数据库迁移、美术 SVG 源文件、配乐生成代码、AI 评测脚本全部在这个仓库里，没有闭源部分。
- **免费，不需要登录**：没有付费内容、没有广告、没有 AFF，也没有任何群组。
- **隐私**：进度只存在本机。上传成绩时只带昵称和哈希过的设备标识；AI 成绩只显示模型名和思考档位，不显示你用的是哪家服务或中转。
- **许可证**：[MIT](LICENSE)。

## 社区与友情链接

本项目积极参与并认可 [LINUX DO](https://linux.do/) 社区，感谢佬友们的反馈和支持。

- [LINUX DO - 新的理想型社区](https://linux.do/)
