<div align="center">

# 🐟 MiroFish-Explorer

**探索者版本 · 群体智能引擎 · 预测万物**

*An Explorer Edition of [MiroFish](https://github.com/666ghj/MiroFish) — Accelerating What's Next*

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Forked from](https://img.shields.io/badge/Forked%20from-666ghj%2FMiroFish-ff69b4.svg)](https://github.com/666ghj/MiroFish)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Vue.js 3](https://img.shields.io/badge/Vue.js-3.x-brightgreen.svg)](https://vuejs.org/)
[![Flask 3](https://img.shields.io/badge/Flask-3.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Node.js 18+](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
[![Tauri 2](https://img.shields.io/badge/Tauri-2.0-orange.svg)](https://tauri.app/)
[![Under Active Development](https://img.shields.io/badge/Status-Active%20Development-yellow.svg)](#-开发状态)

[English](README-EN.md) | 简体中文

</div>

---

> **⚠️ 本项目是 [MiroFish](https://github.com/666ghj/MiroFish) 的探索者版本（Explorer Edition）fork。**
>
> 它在上游基础上**新增 Command Workflow（命令工作流）**等探索能力，并正在**加速迭代**中。本仓库**不是** MiroFish 官方版本，所有正式功能请以 [666ghj/MiroFish](https://github.com/666ghj/MiroFish) 为准。
>
> 🤝 **致谢上游**：本项目基于盛大集团孵化的开源项目 [MiroFish](https://github.com/666ghj/MiroFish) 开发，遵循 AGPL v3 协议。模拟引擎能力由 [OASIS (CAMEL-AI)](https://github.com/camel-ai/oasis) 提供。

---

## 📖 这是什么？

**MiroFish-Explorer** 是对 [MiroFish](https://github.com/666ghj/MiroFish) 的**探索性增强版本**。

MiroFish 是一个简洁通用的群体智能引擎：上传种子材料（新闻、报告、小说等）后，它会**自动构建一个高保真的平行数字世界**，让成千上万具备独立人格、长期记忆和行为逻辑的智能体在其中自由交互和演化，从而推演未来的轨迹。

我们 fork 出这个 **Explorer 版本**，专注于在上游核心引擎之上，**探索更主动、更可控、更具交互性**的使用方式——比如新增的 **Command Workflow** 让用户能以命令式指令直接驱动推演流程。

> 💡 **上游优先原则**：本仓库**不会**复制上游已经做得很好的功能。我们的目标是在上游框架上**做加法**，并把稳定的改进回馈给上游。

---

## ✨ 与上游 [MiroFish](https://github.com/666ghj/MiroFish) 的差异（诚实对比）

> ⚠️ **先看这里**：上游 MiroFish 是个**极简的核心引擎**（后端 12 个 service、前端 7 个 view），只提供"基础仿真 + 报告生成"能力。本 fork 在**保留上游核心引擎思想**的基础上，**自行扩展了大量新能力**。"探索者版本"的"探索"二字，主要指在本分支上**新增的 Command Workflow**。
>
> 想要核对？用 `gh api repos/666ghj/MiroFish/contents/{backend/app/services,frontend/src/views}` 直接列上游目录即可验证。

### 三档分类（最关键的一段）

| 档位 | 含义 | 包含什么 |
|------|------|---------|
| 🟢 **真正继承自上游** | 上游代码 / 设计思想**直接复用**，本 fork 未做实质修改 | OASIS 多智能体核心设计、知识图谱构建（graph_builder）、报告生成（report_agent）、Docker 部署思路 |
| 🟡 **本 fork 自行扩展**（**非上游提供**） | 上游没有，本 fork 自行开发 | 圆桌推演、政策推演、因果推断（DoWhy / EconML）、博弈论求解器（Gambit / OpenSpiel / Network Game）、影响传播模拟、意见动力学模拟、Tauri 桌面端（macOS / Windows）、因果桥接、智能体辩论、流式推演管线 等 |
| 🔵 **Explorer 分支独有** | 在本 fork 的所有扩展之上，本分支（Explorer）唯一真正新增的能力 | **Command Workflow（命令工作流）** |

### 规模对比（最直观的数字）

| 维度 | 上游 [MiroFish](https://github.com/666ghj/MiroFish) | **本仓库 MiroFish-Explorer** |
|------|----------------------|-------------------------------|
| 后端 service 文件数 | **~12** | **~80+**（约 **6.7×**） |
| 前端 view 文件数 | **~7** | **~25**（约 **3.5×**） |
| 后端代码总行数 | 较小 | 较大 |
| 桌面端 | ❌ 无 | ✅ Tauri 2.0（macOS + Windows） |

### 能力对比表（按档位组织）

#### 🟢 真正继承自上游

| 能力 | 上游是否提供 | 本 fork 现状 |
|------|------|---------------|
| OASIS 多智能体核心仿真 | ✅ | ✅ 保持设计原貌 |
| 知识图谱构建（Neo4j） | ✅ | ✅ 保持设计原貌 |
| 报告生成（report_agent） | ✅ | ✅ 保持设计原貌 |
| Docker 一键部署 | ✅ | ✅ 沿用思路 |

#### 🟡 本 fork 自行扩展（上游**没有**，本 fork 自行开发）

| 能力 | 本 fork 状态 | 备注 |
|------|------------|------|
| **圆桌推演**（双模式 LLM + 博弈论） | ✅ | 完整功能，含多轮推演、流式输出 |
| **政策推演**（Policy Deduction） | ✅ | 单/双模式 LLM + 数学博弈论 |
| **因果推断**（DoWhy / EconML） | ✅ | 包括因果桥接、稳定性分析 |
| **博弈论求解器** | ✅ | Gambit / OpenSpiel / Network Game / Cooperative / Stackelberg / Reputation Game |
| **影响传播模拟** | ✅ | Influence Propagation / Cascade |
| **意见动力学模拟** | ✅ | Opinion Dynamics |
| **Tauri 桌面端** | ✅ | macOS + Windows，自带 Neo4j + JRE |
| **因果桥接 / 智能体辩论 / 策略解释** | ✅ | 高级分析能力 |
| **流式推演管线** | ✅ | token 级 SSE 输出 |

#### 🔵 Explorer 分支真正独有

| 能力 | 说明 |
|------|------|
| **Command Workflow（命令工作流）** | 面向研究者的结构化命令驱动推演（详见下节） |

### 🎯 Explorer 分支真正的独有能力：Command Workflow（命令工作流）

在所有上述扩展之上，**Explorer 分支的真正新增**只有 **Command Workflow** 一项。

Command Workflow 是**面向研究者的探索式交互范式**：

- 用户可通过**结构化命令**直接编排推演流程
- 示例命令：
  - `reset` — 重置数字世界
  - `inject <event>` — 向世界注入事件
  - `pause` / `resume` — 暂停/恢复推演
  - `snapshot export` — 导出推演快照
  - `sweep <param> <range>` — 参数扫描
- 与本 fork 的**自然语言驱动**圆桌推演形成互补
- 适合实验性场景：批量推演、参数扫描、教学演示、复现论文
- 后端实现：`backend/app/services/command_engine.py` / `command_models.py` / `command_session_manager.py`
- 前端视图：`frontend/src/views/CommandWorkflow.vue`

> 详细 API 与命令规范见 `docs/command-workflow.md`（**即将发布**）

### 与上游的实际关系（最后澄清）

> 在实际工作中，**本 fork 与上游已经大幅分叉**。短期内不太可能把所有差异都合并回上游（部分功能与上游"简洁"理念冲突）。**Command Workflow 是少数设计上"上游兼容"的新增能力**，是我们优先回馈上游的候选。
>
> 如果你只想用最简的核心仿真，直接用上游 [MiroFish](https://github.com/666ghj/MiroFish) 即可；本仓库适合需要更丰富能力（推演、对抗、桌面端、批量化研究）的用户。

---

## 🚀 快速开始

### 前置要求

| 工具 | 版本 | 用途 | 检查 |
|------|------|------|------|
| **Node.js** | 18+ | 前端运行 | `node -v` |
| **Python** | ≥3.11, ≤3.12 | 后端运行 | `python --version` |
| **uv** | Latest | Python 包管理 | `uv --version` |
| **Neo4j** | 5.x | 图数据库（可选 Docker 启动） | `neo4j --version` |

### 方式一：源码部署（推荐开发者）

#### 1. 克隆并配置环境

```bash
git clone https://github.com/jjy1000/MiroFish-Explorer.git
cd MiroFish-Explorer
cp .env.example .env
# 编辑 .env，至少填入 LLM_API_KEY / LLM_BASE_URL / LLM_MODEL_NAME
```

#### 2. 安装依赖

```bash
# 一键安装（前端 + 后端）
npm run setup:all

# 或分步
npm run setup          # 前端依赖
npm run setup:backend  # 后端依赖（uv sync）
```

#### 3. 启动 Neo4j（图数据库）

```bash
# 方式 A：使用 Docker Compose（推荐）
docker compose up -d neo4j

# 方式 B：本地已安装的 Neo4j，URI 用 bolt://localhost:7687
```

#### 4. 启动应用

```bash
npm run dev
```

- 前端：http://localhost:**5288**
- 后端 API：http://localhost:**5103**
- Neo4j 浏览器：http://localhost:7474

### 方式二：Docker 一键部署

```bash
docker compose up -d
```

服务端口：前端 **5288** / 后端 **5103** / Neo4j 7687。

详见 [DOCKER.md](DOCKER.md)。

---

## 🏗️ 技术架构

### 前端
- **Vue 3** + Composition API + Vite
- **Element Plus** + 原生 HTML（按视图优化）
- **ECharts** / **vis-network** 图谱与可视化
- **Pinia** 状态管理 + **Vue Router**
- **Vitest** 单元测试

### 后端
- **Flask 3** + **gunicorn**（生产）
- **Neo4j 5** 图数据库 + **Cypher** 查询
- **Zvec** 本地向量数据库（语义检索）
- **OASIS**（[camel-ai/oasis](https://github.com/camel-ai/oasis)）多智能体仿真
- **OpenSpiel / pygambit** 博弈论求解
- **tiktoken** 精确 token 计数
- **uv** Python 包管理

### 桌面端
- **Tauri 2.0**（macOS / Windows）
- 内嵌 Neo4j + JRE 自启动
- 端到端离线运行

### 端口与数据隔离

为避免与上游 MiroFish 冲突，本版本使用独立端口与数据目录：

| 服务 | 上游端口 | **本版本端口** | 数据目录 |
|------|---------|---------------|---------|
| 前端 | 3000 | **5288** | — |
| 后端 | 5001 | **5103** | — |
| Neo4j Bolt | 7687 | 7687 | — |
| 上传/项目 | `uploads/` | **`uploads-explorer/`** | 隔离 |

> ✅ 因此本版本**可与上游 MiroFish 在同一台机器上并存运行**。

---

## 📂 项目结构

```
MiroFish-Explorer/
├── backend/                 # Flask 后端
│   ├── app/
│   │   ├── api/            # REST API 路由
│   │   ├── services/       # 业务服务（含 command_engine.py 等探索模块）
│   │   ├── models/         # 数据模型
│   │   ├── config.py       # 配置中心
│   │   └── utils/          # 工具
│   ├── tests/              # pytest
│   ├── pyproject.toml
│   └── gunicorn.conf.py
├── frontend/                # Vue 3 前端
│   ├── src/
│   │   ├── views/          # 页面视图（含 CommandWorkflow.vue）
│   │   ├── components/     # 通用组件
│   │   ├── composables/    # 组合式函数
│   │   ├── store/          # Pinia stores
│   │   ├── api/            # API 客户端
│   │   └── router/         # 路由
│   └── package.json
├── src-tauri/              # Tauri 桌面端配置
│   ├── src/main.rs
│   ├── icons/
│   └── tauri.conf.json
├── docs/                   # 项目文档
│   ├── roundtable-architecture.md
│   └── architecture-view.html
├── scripts/                # 构建/部署脚本
├── static/                 # 静态资源
├── docker-compose.yml
├── Dockerfile
├── LICENSE                 # AGPL v3（继承上游）
├── README.md               # 本文件
└── README-EN.md            # 英文版
```

---

## 🚧 开发状态

> **🔧 本项目正在加速开发中（Under Active Development）**

- **当前阶段**：Command Workflow MVP 已完成，正在**稳定性打磨 + API 文档化**
- **近期路线**：
  - [ ] 完善 Command Workflow API 规范与文档
  - [ ] 增加结构化推演回放（replay）能力
  - [ ] 命令模板市场（Command Templates）
  - [ ] 实验性参数扫描 UI
  - [ ] 上游同步策略优化（定期 merge 上游 main）

> 💡 **本项目承诺**：会**保持与上游的协议一致（AGPL v3）**，并**优先将稳定改进以 PR 形式回馈上游**。

### 同步上游

```bash
# 添加上游为 remote
git remote add upstream https://github.com/666ghj/MiroFish.git

# 定期同步上游 main 分支
git fetch upstream
git merge upstream/main
```

---

## 🤝 贡献

欢迎通过 Issue 提交 bug 报告、功能建议，或通过 Pull Request 贡献代码。

**贡献方向**：
- Command Workflow 命令扩展
- 智能体交互增强
- 推演可视化新视图
- 性能优化（特别是大规模推演）
- 文档与教学案例

**请注意**：
- 所有贡献将以 **AGPL v3** 协议发布
- 优先将改进反馈给上游 [MiroFish](https://github.com/666ghj/MiroFish)
- 重大改动请先开 Issue 讨论

---

## 📜 许可证

本项目基于 **GNU Affero General Public License v3.0 (AGPL-3.0)** 协议开源。

```
Copyright (C) 2026 jjy1000

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.
```

完整协议见 [LICENSE](LICENSE) 文件。本项目作为 MiroFish 的衍生作品，**全部派生代码同样受 AGPL v3 约束**。

---

## 🙏 致谢

- **[666ghj/MiroFish](https://github.com/666ghj/MiroFish)** — 上游项目，盛大集团孵化
- **[CAMEL-AI / OASIS](https://github.com/camel-ai/oasis)** — 多智能体仿真引擎
- **[OpenSpiel](https://github.com/deepmind/open_spiel)** — 博弈论求解框架
- 所有上游贡献者与社区

---

## 🔗 相关链接

- 上游项目：https://github.com/666ghj/MiroFish
- 模拟引擎：https://github.com/camel-ai/oasis
- 本项目仓库：https://github.com/jjy1000/MiroFish-Explorer
- Issue 反馈：https://github.com/jjy1000/MiroFish-Explorer/issues

---

<div align="center">

**🐟 Explore. Simulate. Predict.**

*MiroFish-Explorer · 探索者版本 · 加速开发中*

</div>
