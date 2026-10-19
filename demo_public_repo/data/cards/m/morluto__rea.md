# morluto/rea

⭐ 303,126 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/morluto/rea) · [官网](https://rea.tools) · 个人维护 · 中文 README

**为 agent 接入逆向工程工具的 MCP 服务器，从应用行为到原生二进制**

REA 以 MCP 服务器形式将 agent 连接到逆向工程工具集，可检视原生二进制、JavaScript/Electron 应用、.NET 程序集、Android APK、网站、网络抓包等 20 类目标；返回结论附带证据与局限，分析在本地运行。原生深度分析需调用已有的 Hopper、Ghidra 或 IDA 安装；静态 JavaScript/.NET 检视无需原生引擎。通过 `npx rea-agents setup` 向 agent 注册并安装工作流说明，也提供 CLI（`rea`）在终端直接使用。要求 Node.js 22.19+/24.11+/26+ 与 npm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | npm 分发的服务器/CLI |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | npx 一条命令(需 Node 运行时);原生分析另需 Ghidra/IDA 等,属可选 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 0.1 天前发版(年发版 37),259 位贡献者,issue 中位当天关闭
- 涨星:近 2 天 **+25,460**(自 2026-10-16 起算,爆发中)
- 安装:npm 包 `rea-agents` 月下载 346,782
- 平台:Windows / Linux · 协议:MCP

## 能力要点

- 单一 MCP 服务器覆盖原生二进制、JS/Electron、.NET、APK、固件、抓包等约 20 类分析目标
- 支持 Claude Code、Codex、Cursor、Gemini CLI 等多种 agent，其他客户端可手动注册 MCP
- 原生分析可复用已有 Hopper/Ghidra/IDA 安装，也可配合 objdump、Rizin、JADX、pwntools 等
- 结果附带证据与局限说明，分析在本地运行

## 适用场景

- 想了解某应用功能如何实现，让 agent 检视无源码的应用并给出证据
- 分析 APK、固件或二进制的结构、符号与反编译结果
- 从 Electron 应用目录或 ASAR 提取模块、导入与 IPC 边界
- 在终端用 CLI 命令做快照与脚本化分析

## 场景标签

`逆向工程` `MCP服务器` `二进制分析` `CLI工具` `agent工具` · 领域:开发者工具/逆向工程

## 证据(README 行号)

> L6: ### One MCP for reverse engineering across binaries, applications, and runtime behavior.
> L41: REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and webs
> L43: Setup registers REA with your agent and installs matching workflow instructions. Native analysis can use an existing Hop
> L66: Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and

---
*卡片 v1 · prompt 1.0 · 生成 2026-10-18 · 置信度 high · 依据 README sha `05ecfe9c2cfd` · [字段定义](../../../DATASET.md)*
