# AgentMeter

<p align="center">
  <img src="./assets/branding/agentmeter-logo.svg" alt="AgentMeter Logo" width="160" />
</p>

<p align="center">
  一个本地 AI Coding 使用分析工具，帮你看清每天和过去一个月的模型、Token、成本、工具分布与项目投入。
</p>

<p align="center">
  <a href="./CONTRIBUTING.md">贡献与开发说明</a>
</p>

---

## 产品简介

AgentMeter 是一个面向开发者的本地桌面工具，用于汇总和展示电脑上 AI Coding 工具的使用情况。它关注的不只是“用了多少”，还包括：

- 今天一共发了多少请求、开了多少会话
- 输入、输出、reasoning、缓存等 Token 分布
- 不同工具和模型的使用占比与成本
- 哪些代码项目消耗了最多 AI 资源
- 过去 30 天的趋势变化与报告导出

它的目标是把分散在不同工具、不同日志和不同项目里的 AI 使用记录，整理成一个可持续查看、复盘和导出的本地仪表盘。

## 适合谁用

- 同时使用 Codex、Claude Code、Cursor 等多种 AI Coding 工具的开发者
- 想知道自己每天到底用了多少 Token、花了多少钱的人
- 希望把 AI 使用成本映射回真实项目和仓库的人
- 需要按时间范围复盘 AI 使用强度、模型选择和工具价值的人

## 核心能力

### 实时总览

- 查看今日总请求数、总会话数、总 Token 和估算成本
- 快速识别今天主要使用了哪些工具、涉及了哪些项目
- 适合作为每天打开后的第一屏

### Token 趋势监控

- 查看今日 Token 使用曲线
- 区分输入、输出、缓存、reasoning 等不同消耗
- 观察当前小时消耗和最近一次请求的变化

### 工具与模型分布

- 对比 Codex、Claude Code、Cursor 等工具的使用占比
- 查看不同模型的请求数、Token、成本和平均单次消耗
- 帮助判断是否过度依赖高成本模型

### 项目维度分析

- 按代码仓库查看 Token 和成本投入
- 展示项目名称、路径、主要工具、主要模型和最近使用时间
- 让 AI 花费能够映射到真实开发工作

### 月度报告

- 汇总过去 30 天的总会话数、总请求数、总 Token、总成本
- 查看每日趋势、最高消耗日、活跃项目数和工具分布
- 支持按工具、模型、项目做月度复盘

### 报告导出

- 支持导出月度使用报告
- 目标格式包括 Markdown、CSV、HTML
- 可根据需要控制是否包含项目路径、会话摘要或原始记录

## 当前状态

当前项目还处于第一阶段，重点是把本地采集、统一存储和报表查询链路搭起来，为后续接入更多 AI Coding 数据源做准备。

目前已经具备：

- Tauri 2 + React + TypeScript 桌面工程骨架
- Overview / Reports / Settings 页面结构
- Rust 命令层与前端调用打通
- SQLite 初始化能力
- 使用报告查询接口占位
- Collector 扩展目录预留

## 计划支持的数据来源

- Codex
- Claude Code
- Cursor
- Continue
- OpenRouter
- Copilot

## 技术栈

- Tauri 2
- React 19
- TypeScript
- Vite
- SQLite (`rusqlite`)
- React Query
- Zustand

## 本地启动

```bash
pnpm install
pnpm dev:tauri
```

常用命令：

- `pnpm dev`：启动前端开发服务器
- `pnpm dev:tauri`：启动 Tauri 桌面开发模式
- `pnpm build`：构建前端产物
- `pnpm tauri:build`：构建桌面应用
- `pnpm check`：执行 TypeScript 类型检查
- `pnpm lint`：执行 ESLint

## 文档

- [用户故事](./用户故事.md)
- [贡献与开发说明](./CONTRIBUTING.md)
- [协作约束](./AGENT.md)
