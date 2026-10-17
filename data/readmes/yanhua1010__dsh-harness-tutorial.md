# DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent

一个完整可运行的 VitePress 中文教学站点，把 DeepSeek Harness（「一切皆插件」的 Agent 框架）拆解成一套适合计算机本科毕业生的渐进式教程：先懂原理，再用 8 个真实可运行的 Demo 掌握机制，最后亲手实现一个教学版目标项目（React 前端 + Node.js TypeScript 后端）。

## 仓库结构

```text
dsh-harness-tutorial/
├── docs/                 # VitePress 教程站点（中文）
│   ├── guide/            #   原理篇（8 章）
│   ├── source/           #   源码拆解篇（6 章）
│   ├── demos/            #   实战 Demo 篇（8 个 Demo 教程页）
│   ├── project/          #   教学版项目篇（8 章）
│   └── appendix/         #   术语表 / 常见错误 / 参考资料
├── demos/                # 渐进式 Demo 代码（基于真实 dsh 包，已验证）
│   ├── 01-first-plugin/ … 08-profile/
└── final-project/        # 教学版目标项目 mini-harness
    ├── packages/mini-harness/   # 核心库（约 900 行 TS，零运行时依赖）
    ├── apps/server/             # Node 后端（Express + SSE）
    └── apps/web/                # React 前端（聊天 + 实时事件面板）
```

## 快速开始

```sh
# ① 教程站点
npm install
npm run docs:dev          # http://localhost:5173/dsh-harness-tutorial/

# ② 渐进式 Demo（在 demos/ 下）
cd demos && npm install
npm run demo:1            # Demo 1–4
# Demo 5–8 见 demos/README.md（dsh headless overlay，无需 API Key）

# ③ 教学版项目（在 final-project/ 下）
cd final-project && npm install
npm run demo              # 核心库冒烟测试
npm run dev:server        # 终端 A：后端 http://127.0.0.1:4317
npm run dev:web           # 终端 B：前端 http://localhost:5174
```

## 在线阅读

站点已通过 GitHub Actions 部署到 GitHub Pages：

**https://yanhua1010.github.io/dsh-harness-tutorial/**

## 版本锁定

- DeepSeek Harness（开发者预览）：`0.1.0-rc.6`
- Cordis：`4.0.1`
- Node.js：≥ 20.19（推荐 22+）

所有 Demo 均在该版本上实际运行验证。项目处于快速迭代期，架构思想稳定，API 细节请以[官方文档](https://deepseek-harness.github.io/deepseek-harness/guide/quickstart)最新版为准。

## 许可证

教程内容与代码均为教学用途，遵循 MIT 协议精神。DeepSeek Harness 本身以 [MIT](https://github.com/deepseek-ai/deepseek-harness/blob/master/LICENSE) 开源。
