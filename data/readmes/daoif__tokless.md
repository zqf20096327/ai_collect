<p align="left">
  <img src="./assets/logo.svg" width="60" height="60" alt="Tokless Logo" />
</p>

# Tokless

[![License: MIT](https://img.shields.io/badge/License-MIT-18181B.svg)](./LICENSE)
[![Node.js >= 18](https://img.shields.io/badge/Node.js-%3E%3D18.0.0-10B981.svg)](./package.json)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-18181B.svg)](./package.json)

简体中文 | [English](./README.en.md)

> **在不损失一行代码排查与修复质量的前提下，把 AI 编程工具里无意义的大文件盲读膨胀与滚雪球 Token 消耗砍掉一半以上。**

`tokless` 是面向主流 AI 编程 Agent（原生一键挂载 **Google Antigravity**、**Claude Code**、**Codex CLI**，通用支持 Cursor / Windsurf / Cline / Roo Code 等）的 **纯 Node.js（`>=18`）零外部依赖** 省流与账单透视套件：

1. **防盲读省探索（`tokless skeleton` / `tokless slice`）**：IDE 的 `@Codebase` 只管找到文件，不管怎么读；AI 拿到文件名后常把上千行源码整份塞进上下文，在多步循环中引发 `Cache Read` 复利滚雪球。`tokless` 毫秒级提取函数/类/宏/类型定义与 **`[L起-L止]` 行号骨架**，并支持按函数/类方法/章节名直接抗漂移精准切片（探索期单文件省流 **85%~97%**）。
2. **卸空载省底座（`tokless-coder` / `tokless-reviewer`）**：在纯写码/审码会话中剥离用不上的外部 MCP 与花哨工具 Schema，每步立省数千固定底座 Token。
3. **查真账捉黑洞（`tokless audit`）**：0 模型 Token 离线解剖本地会话账单，一眼定位最烧钱的 Top 5 步骤、跨模型切换/闲置引起的 Prefix Cache 断层，以及项目规则与 MCP 空载开销。

---

## 真实工程 A/B 实测效果（Tauri + Rust + React 全仓找 Bug 与修复）

同一生产级工程（Commit `3908815`）切出两个独立 Worktree，同一模型执行完全相同的深层 Bug 排查、修复与编译验证任务：

| 对比维度 | 对照组 (原生默认模式) | 实验组 (启用 `tokless`) | 真实节省 / 提升 |
| :--- | :--- | :--- | :--- |
| **总 Token 吞吐 (`input + cache_read + output`)** | 21,410,381 (2,141 万) | **10,029,592 (1,003 万)** | **净省 53.2% (-1,138 万 Tokens)** |
| **累计 Cache Read（滚雪球缓存消耗）** | 20,858,589 (2,086 万) | **9,627,700 (963 万)** | **净省 53.8% (-1,123 万 Tokens)** |
| **模型调用轮数 / 总步数** | 64 轮 / 220 步 | **42 轮 / 150 步** | **少跑 34.4% 轮次** |
| **`read_file` 调用（无行号盲读）** | 79 次（3 次盲读） | **51 次（0 次盲读）** | **读取减少 35.4%** |
| **峰值上下文水位** | 439,830 Tokens | **323,344 Tokens** | **峰值降低 26.5%** |
| **检出并修复的真实硬核 Bug 数** | 7 个（全部编译通过） | **7 个（全部编译通过）** | **0 质量损耗** |

> *注：上表完成于早期 `v0.1.0` 基线（仅含基础骨架提取与盲读拦截），后续版本已新增 `inheritMcp: false` 净身角色、C/C++ 深度解析与更精细的行号放行机制。完整报告见 [真实 Bug 修复对照账单](./benchmarks/real-world-bugfix-case.md) 与 [静态骨架基准测试](./benchmarks/static-skeleton-benchmark.md)。*

---

## 一行命令极速启用

自动检测并挂载本机已安装的 Antigravity、Claude Code（`~/.claude`）与 Codex CLI（`~/.codex`），默认纯增益安装技能、省流规则与净身角色（**默认不挂载 `PreToolUse` 子进程钩子**，零读文件延迟；`npx` 运行自动切换实体拷贝防软链悬空）：

```bash
npx tokless install
```

按需启用超大文件盲读护栏、指定宿主或一键干净卸载：

```bash
npx tokless install --with-guard       # 可选启用 PreToolUse 护栏（仅对 >800 行无行号盲读返回骨架，传行号一律放行）
npx tokless install --target agy       # 仅挂载 Google Antigravity（claude / codex / all 同理）
npx tokless uninstall --target all     # 一键卸载并无损还原宿主原有配置
```

不想切终端？直接把下面这句话发给你的 AI 编程助手即可：

```text
请运行 npx tokless install 帮我安装启用 tokless 省流套件，装好后确认技能与省流规则已生效。
```

> **使用 Cursor、Windsurf、Cline、Roo Code、Trae、OpenCode 等其他工具？**
> 运行 `npm i -g tokless`，再把 [`rules/AGENTS.md`](./rules/AGENTS.md) 复制到项目根目录（或对应编辑器的规则文件）即可立享核心省流能力。各宿主具体安装目录详见 [原理与各工具挂载说明](./docs/why-tokless.md)。

---

## 四大核心能力与常用命令

| 宿主工具 | 1. `tokless skeleton` 语法骨架 | 2. `PreToolUse` 盲读护栏（`--with-guard`） | 3. 净身角色 (`inheritMcp: false`) | 4. `tokless audit` 账单体检 |
| :--- | :---: | :---: | :---: | :---: |
| **Google Antigravity** | 原生 Skill + CLI + `rules/AGENTS.md` | 可选 `hooks.json` (`>800` 行无行号导航) | `tokless-coder` / `tokless-reviewer` | 全功能（`project` + `list / session / compare`） |
| **Claude Code** | `~/.claude/skills` + CLI | 可选无损合并 `~/.claude/settings.json` | — | 支持 `audit project` 规则与 MCP 账单 |
| **Codex CLI** | `~/.codex/skills` + CLI + `AGENTS.md` | — | — | 支持 `audit project` 规则账单 |
| **其他 AI 编程工具** | `npm i -g tokless` + 根 `AGENTS.md` | 欢迎参考 `targets/` 共创适配 | — | 支持 `audit project` 规则账单 |

### 日常高频 CLI 速查

```bash
# 1. 代码骨架提取与按符号切片（按需惰性加载 JS/TS、Vue/Svelte、Python、Go、Rust、Java、Kotlin、C/C++、C#、Markdown 解析器）
npx tokless skeleton . --map                                    # 全仓文件行数与字数鸟瞰图
npx tokless skeleton ./src --depth 3 --exclude third_party      # 目录级签名与 [L起-L止] 行号地图（自动排除常见构建产物）
npx tokless skeleton ./driver/hal_uart.c                        # 单文件或 C/C++ 大头文件函数/宏/typedef/结构体定位
npx tokless slice ./src/server.ts#Server.start --line-numbers   # 按类方法/函数/章节名精确切出源码（抗行号漂移，未命中返回候选建议）

# 2. 本地 0 Token 账单与底座透视
npx tokless audit project .                                     # [通用] 透视项目常驻规则、Skill 与 MCP 工具底座 Token 开销
npx tokless audit list --source cli                             # [Antigravity] 列出最近会话（支持 cli / app / ide / all）
npx tokless audit session latest                                # [Antigravity] 解剖最新会话 Top 5 烧钱步与缓存断层/模型切换归因
npx tokless audit compare latest~1 latest                       # [Antigravity] 优化前后双会话 A/B 账单对比
```

---

## 深入文档与扩展开发

- **[为什么 `@Codebase` / `repomix` 挡不住掉额度？原理与各宿主目录详解](./docs/why-tokless.md)**
- **[Node.js 编程接口（Programmatic API）与新增宿主/语言贡献指南](./docs/contributing-and-api.md)**
- **[仓库工程规范与变更联动地图（AGENTS.md）](./AGENTS.md)**

---

## 开源致谢（Acknowledgments）

`tokless` 基于 Node.js 标准库从零独立实现，特此感谢以下社区贡献者与开源灵感项目：

- **社区贡献者**：感谢 [@PXY000](https://github.com/PXY000)（跨平台 PowerShell 技能模板、钩子 Node 绝对路径解析、路径安全防护与单测）、[@Mr-PolarBear](https://github.com/Mr-PolarBear)（Java 嵌套类/泛型返回类型/匿名字段过滤与 JS 顶层 IIFE 骨架提取修复）、[@Jefferyu](https://github.com/Jefferyu)（模块化 C/C++ 嵌入式语法骨架解析器、Antigravity 多源 CLI 审计、Pure-Lazy MCP 底座校准与双模型/短窗口缓存断层归因）。
- **灵感致敬**：[HoangP8/tokless](https://github.com/HoangP8/tokless)、[ILoveMyJay/repocontext](https://github.com/ILoveMyJay/repocontext)、[pdavis68/RepoMapper](https://github.com/pdavis68/RepoMapper) 与 [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp)。

如果 `tokless` 切实帮你省下了周额度，欢迎点一颗 **Star** 支持，或关注作者技术手记公众号 **【织歌AI笔记】** 交流实战经验。

## License

[MIT](./LICENSE)
