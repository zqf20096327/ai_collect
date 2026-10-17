# AI-IDE-Agent-Prompts

> Claude Code / Cursor / Trae / Codex AI IDE 专业智能体提示词合集

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language](https://img.shields.io/badge/Language-简体中文-red.svg)](#)
[![Prompts](https://img.shields.io/badge/Prompts-238-brightgreen.svg)](#目录)
[![AI IDE](https://img.shields.io/badge/AI%20IDE-Claude%20Code%20%7C%20Cursor%20%7C%20Trae%20%7C%20Codex-9cf.svg)](#支持的-ai-ide)

面向中文开发者的专业 AI IDE Agent Prompt Library。

这里不是"你是一名 XX 专家"这种普通 Prompt 的简单收集，而是一套真正适合 AI Coding Agent 使用的、结构化、可执行、可复用的 Agent Prompt。

---

## 目录

- [项目介绍](#项目介绍)
- [为什么需要 Agent Prompt](#为什么需要-agent-prompt)
- [核心特性](#核心特性)
- [支持的 AI IDE](#支持的-ai-ide)
- [AI Agent 模型与平台](#ai-agent-模型与平台)
- [快速开始](#快速开始)
- [目录](#目录-1)
- [分类介绍](#分类介绍)
- [使用方法](#使用方法)
- [Prompt 结构](#prompt-结构)
- [Agent 工作流程](#agent-工作流程)
- [推荐组合](#推荐组合)
- [Vibe Coding 工作流](#vibe-coding-工作流)
- [GitHub 工作流](#github-工作流)
- [项目验收流程](#项目验收流程)
- [最佳实践](#最佳实践)
- [安全说明](#安全说明)
- [如何贡献](#如何贡献)
- [Roadmap](#roadmap)
- [License](#license)

---

## 项目介绍

**AI-IDE-Agent-Prompts** 是一个开源的中文 Agent Prompt 库，为 Claude Code、Cursor、Trae、Codex 等 AI IDE 提供可直接复制使用的专业智能体提示词。

每一个 Prompt 都包含明确的分角色定位、核心能力、工作流程、约束与输出格式，强调"先理解上下文 → 先检查项目 → 再制定方案 → 再执行 → 最后验证"的工程化工作方式，避免 AI Agent 凭空假设、盲目修改、伪造测试结果。

## 为什么需要 Agent Prompt

AI Coding Agent 的能力上限，很大程度取决于你给它的提示词。

- 一句"帮我写个登录功能"，Agent 只能靠猜，容易产出不符合项目现状的代码；
- 一个好的 Agent Prompt，会让 Agent **先读项目、先看代码、先想方案、再动手**；
- 明确的**约束**可以防止 Agent 编造信息、假装执行命令、伪造测试通过；
- 统一的**输出格式**让你能快速判断 Agent 的工作质量。

本仓库把"如何高质量地指挥一个 AI Coding Agent"沉淀为可复用的模板。

## 核心特性

- ✅ **全中文**：所有 Prompt 均以简体中文编写，贴合中文开发者习惯
- ✅ **可独立使用**：每个 Prompt 复制后即可直接使用，无需其他依赖
- ✅ **结构化**：统一采用 YAML Front Matter + 固定章节结构
- ✅ **可执行**：每个 Agent 都有具体的工作流程与输出格式
- ✅ **不千篇一律**：每个 Agent 都包含该领域的真实专业内容（工具、方法论、检查点）
- ✅ **覆盖全面**：13 大分类、238 个 Prompt/Workflow
- ✅ **持续扩展**：目录结构支持扩展至 200+ 个 Agent

## 支持的 AI IDE

本仓库的 Prompt 可用于任何支持 Agent 模式的 AI 编程工具，包括但不限于：

| AI IDE / 工具 | 说明 |
| --- | --- |
| Claude Code | Anthropic 官方 CLI Agent |
| Cursor | 内置 Agent 模式的 AI 编辑器 |
| Trae | 字节跳动出品的 AI IDE |
| Codex | OpenAI 的编程 Agent |
| Gemini CLI | Google 的终端 AI Agent |
| GitHub Copilot | 内置 Agent 模式的 AI 编程助手 |
| Windsurf | Codeium 出品的 AI IDE |
| Cline | VS Code 开源 Agent 扩展 |
| Aider | 开源终端 AI 结对编程工具 |
| Continue | 开源 AI 代码助手 |
| Devin | 自主 AI 软件工程师 |
| OpenHands | 开源 AI 软件工程师平台 |
| 其他 | 任何支持自定义系统提示词 / Agent 指令的 AI 编码工具 |

## AI Agent 模型与平台

除 AI IDE 外，本仓库的 Prompt 同样适用于主流 AI Agent 模型与平台：

### Agent 模型

| 模型 | 说明 |
| --- | --- |
| Hermes | Nous Research 出品的开源 Agent 模型系列，擅长函数调用、结构化输出与角色扮演 |
| Qwen | 阿里开源的模型系列，提供 Qwen-Agent 框架，工具调用与规划能力强 |
| DeepSeek | 深度求索开源的模型系列，推理与编码能力强，广泛用于 Agent 场景 |

### Agent 平台与框架

| 平台 / 框架 | 说明 |
| --- | --- |
| Reasonix | AI 编码代理平台，支持以 Agent 模式执行编程与工程任务 |
| LangGraph | LangChain 的图式 Agent 编排框架 |
| CrewAI | 多智能体协作编排框架 |

## 快速开始

### 1. 找到需要的 Agent

例如：

```
01-编程语言/Python专家.md
```

### 2. 复制 Prompt

打开 Markdown 文件，复制除说明性内容外的 Prompt 主体。

### 3. 粘贴到 AI IDE

可以用于：

- Claude Code
- Cursor
- Trae
- Codex
- 其他支持 Agent 的 AI Coding 工具

### 4. 描述任务

例如：

> 帮我检查这个 FastAPI 项目的数据库连接问题。

Agent 会：

1. 分析项目
2. 定位相关代码
3. 制定方案
4. 修改代码
5. 执行测试
6. 汇报结果

---

## 目录

<details>
<summary>展开查看完整目录结构</summary>

```text
AI-IDE-Agent-Prompts/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
│
├── 00-通用Agent/
│   ├── 通用软件工程师.md
│   ├── AI编程Agent.md
│   ├── 全栈开发Agent.md
│   ├── 项目经理Agent.md
│   ├── 技术架构师Agent.md
│   └── SeniorSoftwareEngineer.md
│
├── 01-编程语言/
│   ├── Python专家.md
│   ├── Java专家.md
│   ├── JavaScript专家.md
│   ├── TypeScript专家.md
│   ├── C专家.md
│   ├── C++专家.md
│   ├── CSharp专家.md
│   ├── Go专家.md
│   ├── Rust专家.md
│   ├── PHP专家.md
│   ├── Ruby专家.md
│   ├── Kotlin专家.md
│   ├── Swift专家.md
│   ├── Dart专家.md
│   ├── Scala专家.md
│   ├── Elixir专家.md
│   ├── Lua专家.md
│   ├── R语言专家.md
│   ├── MATLAB专家.md
│   └── Solidity专家.md
│
├── 02-前端开发/
│   ├── 前端架构师.md
│   ├── React专家.md
│   ├── NextJS专家.md
│   ├── Vue专家.md
│   ├── Nuxt专家.md
│   ├── Angular专家.md
│   ├── Svelte专家.md
│   ├── TailwindCSS专家.md
│   ├── CSS专家.md
│   ├── HTML专家.md
│   ├── Web性能优化专家.md
│   ├── 前端工程化专家.md
│   ├── 状态管理专家.md
│   ├── 浏览器专家.md
│   ├── WebAssembly专家.md
│   ├── 前端可访问性专家.md
│   ├── React性能优化专家.md
│   ├── NextJS全栈专家.md
│   ├── 组件库设计专家.md
│   ├── 前端重构专家.md
│   └── 前端Bug排查专家.md
│
├── 03-后端开发/
│   ├── 后端架构师.md
│   ├── REST-API专家.md
│   ├── GraphQL专家.md
│   ├── 微服务架构师.md
│   ├── NodeJS专家.md
│   ├── NestJS专家.md
│   ├── SpringBoot专家.md
│   ├── FastAPI专家.md
│   ├── Django专家.md
│   ├── Laravel专家.md
│   ├── Gin专家.md
│   ├── WebSocket专家.md
│   ├── RPC专家.md
│   ├── 消息队列专家.md
│   ├── 缓存架构专家.md
│   ├── 分布式系统专家.md
│   └── API安全专家.md
│
├── 04-数据库与数据工程/
│   ├── SQL专家.md
│   ├── PostgreSQL专家.md
│   ├── MySQL专家.md
│   ├── SQLite专家.md
│   ├── Redis专家.md
│   ├── MongoDB专家.md
│   ├── Elasticsearch专家.md
│   ├── 数据库架构师.md
│   ├── 数据库优化专家.md
│   ├── 数据库迁移专家.md
│   ├── 数据工程师.md
│   ├── ETL专家.md
│   ├── 数据管道专家.md
│   ├── 数据仓库专家.md
│   ├── BigData专家.md
│   └── 数据质量专家.md
│
├── 05-AI与机器学习/
│   ├── AI工程师.md
│   ├── AI应用工程师.md
│   ├── LLM工程师.md
│   ├── Prompt工程师.md
│   ├── Agent工程师.md
│   ├── RAG专家.md
│   ├── AI工作流专家.md
│   ├── AI产品经理.md
│   ├── 机器学习工程师.md
│   ├── 深度学习工程师.md
│   ├── NLP专家.md
│   ├── ComputerVision专家.md
│   ├── PyTorch专家.md
│   ├── TensorFlow专家.md
│   ├── HuggingFace专家.md
│   ├── 向量数据库专家.md
│   ├── Embedding专家.md
│   ├── 模型评估专家.md
│   ├── 模型部署专家.md
│   ├── MLOps工程师.md
│   ├── AI代码审查专家.md
│   ├── ClaudeCode专家.md
│   ├── CursorAgent专家.md
│   ├── Codex工程师.md
│   ├── TraeAgent专家.md
│   ├── AIIDE工作流专家.md
│   ├── VibeCoding专家.md
│   └── AI编程项目经理.md
│
├── 06-云原生与DevOps/
│   ├── DevOps工程师.md
│   ├── DevSecOps工程师.md
│   ├── Docker专家.md
│   ├── Kubernetes专家.md
│   ├── Helm专家.md
│   ├── Terraform专家.md
│   ├── Ansible专家.md
│   ├── Linux运维专家.md
│   ├── CI-CD专家.md
│   ├── GitHubActions专家.md
│   ├── GitLabCI专家.md
│   ├── AWS架构师.md
│   ├── Azure架构师.md
│   ├── GCP架构师.md
│   ├── 云架构师.md
│   ├── SRE专家.md
│   ├── 监控专家.md
│   ├── 日志分析专家.md
│   └── 故障排查专家.md
│
├── 07-架构与系统设计/
│   ├── 软件架构师.md
│   ├── 系统架构师.md
│   ├── 分布式系统架构师.md
│   ├── 微服务架构师.md
│   ├── 高并发架构师.md
│   ├── 高可用架构师.md
│   ├── 可扩展系统架构师.md
│   ├── 低延迟系统专家.md
│   ├── 事件驱动架构专家.md
│   ├── Serverless专家.md
│   ├── DDD专家.md
│   ├── CleanArchitecture专家.md
│   ├── SOLID专家.md
│   ├── 代码重构专家.md
│   ├── 遗留系统现代化专家.md
│   ├── 架构评审专家.md
│   └── 技术选型专家.md
│
├── 08-测试与代码质量/
│   ├── CodeReview专家.md
│   ├── Debug专家.md
│   ├── Bug排查专家.md
│   ├── 单元测试专家.md
│   ├── 集成测试专家.md
│   ├── E2E测试专家.md
│   ├── 自动化测试专家.md
│   ├── 性能测试专家.md
│   ├── 压力测试专家.md
│   ├── 测试架构师.md
│   ├── TDD专家.md
│   ├── BDD专家.md
│   ├── 静态代码分析专家.md
│   ├── 代码质量专家.md
│   ├── 重构专家.md
│   └── 技术债务分析专家.md
│
├── 09-安全/
│   ├── 网络安全专家.md
│   ├── 应用安全专家.md
│   ├── Web安全专家.md
│   ├── API安全专家.md
│   ├── 安全审计专家.md
│   ├── 代码安全审查专家.md
│   ├── DevSecOps专家.md
│   ├── 身份认证专家.md
│   ├── OAuth专家.md
│   ├── JWT安全专家.md
│   ├── 密码学工程师.md
│   ├── 隐私工程师.md
│   ├── 漏洞分析专家.md
│   ├── 安全架构师.md
│   └── 事件响应专家.md
│
├── 10-移动端与游戏/
│   ├── Android开发专家.md
│   ├── KotlinAndroid专家.md
│   ├── iOS开发专家.md
│   ├── SwiftUI专家.md
│   ├── Flutter专家.md
│   ├── ReactNative专家.md
│   ├── Unity开发专家.md
│   ├── UnrealEngine专家.md
│   ├── UnrealCPlusPlus专家.md
│   ├── Godot专家.md
│   ├── 游戏架构师.md
│   ├── 游戏性能优化专家.md
│   ├── 游戏AI专家.md
│   ├── Shader专家.md
│   └── Minecraft插件开发专家.md
│
├── 11-产品与设计/
│   ├── 产品经理.md
│   ├── 技术产品经理.md
│   ├── AI产品经理.md
│   ├── UI设计师.md
│   ├── UX设计师.md
│   ├── UX研究员.md
│   ├── 交互设计师.md
│   ├── DesignSystem专家.md
│   ├── 产品分析师.md
│   ├── 业务分析师.md
│   ├── 用户研究专家.md
│   ├── SEO专家.md
│   ├── 内容策略专家.md
│   ├── 技术写作专家.md
│   ├── API文档工程师.md
│   └── Mermaid专家.md
│
├── 12-专业工作流/
│   ├── 项目经理Agent.md
│   ├── 软件开发Agent.md
│   ├── VibeCodingAgent.md
│   ├── 项目规划Agent.md
│   ├── PRD生成Agent.md
│   ├── 技术方案Agent.md
│   ├── 代码实现Agent.md
│   ├── CodeReviewAgent.md
│   ├── DebugAgent.md
│   ├── RefactorAgent.md
│   ├── 测试Agent.md
│   ├── GitAgent.md
│   ├── GitHubAgent.md
│   ├── Issue分析Agent.md
│   ├── PullRequestAgent.md
│   ├── ReleaseAgent.md
│   ├── 文档Agent.md
│   ├── README生成Agent.md
│   ├── 项目重构Agent.md
│   ├── 项目迁移Agent.md
│   ├── 技术债务Agent.md
│   └── 项目验收Agent.md
│
└── workflows/
    ├── 新项目开发流程.md
    ├── VibeCoding完整流程.md
    ├── Bug修复流程.md
    ├── CodeReview流程.md
    ├── 项目重构流程.md
    ├── GitHub发布流程.md
    ├── CI-CD流程.md
    ├── 项目测试流程.md
    ├── 项目部署流程.md
    └── Hackathon项目开发流程.md
```

</details>

## 分类介绍

| 分类 | 目录 | 内容 | 数量 |
| --- | --- | --- | --: |
| 通用 Agent | `00-通用Agent/` | 软件工程、AI 编程、全栈、项目管理 | 6 |
| 编程语言 | `01-编程语言/` | Python、Java、C++、Rust、Go 等 | 20 |
| 前端开发 | `02-前端开发/` | React、Vue、Next.js、CSS、性能等 | 21 |
| 后端开发 | `03-后端开发/` | REST、GraphQL、微服务、消息队列等 | 17 |
| 数据库与数据工程 | `04-数据库与数据工程/` | SQL、Redis、MongoDB、ETL 等 | 16 |
| AI 与机器学习 | `05-AI与机器学习/` | LLM、RAG、Agent、MLOps 等 | 28 |
| 云原生与 DevOps | `06-云原生与DevOps/` | Docker、K8s、Terraform、CI/CD 等 | 19 |
| 架构与系统设计 | `07-架构与系统设计/` | 分布式、高并发、DDD、Serverless 等 | 17 |
| 测试与代码质量 | `08-测试与代码质量/` | Debug、Review、E2E、TDD 等 | 16 |
| 安全 | `09-安全/` | Web、API、审计、密码学等 | 15 |
| 移动端与游戏 | `10-移动端与游戏/` | Flutter、Unity、Unreal、Shader 等 | 15 |
| 产品与设计 | `11-产品与设计/` | PM、UI、UX、技术写作等 | 16 |
| 专业工作流 | `12-专业工作流/` | Vibe Coding、GitHub、项目验收等 | 22 |
| 工作流 | `workflows/` | 跨角色端到端流程 | 10 |

**合计：238 个 Prompt / Workflow 文件。**

## 使用方法

### 单个 Agent 使用

1. 打开对应分类目录下的 `.md` 文件；
2. 复制 Prompt 内容；
3. 粘贴到 AI IDE 的对话或系统提示词中；
4. 描述你的具体任务。

### 组合 Agent 使用

对于复杂任务，可以按顺序依次使用多个 Agent，详见[推荐组合](#推荐组合)。

## Prompt 结构

每个 Prompt 文件统一采用以下结构：

```markdown
---
name: Agent名称
description: Agent用途的一句话描述
category: 所属分类
tags:
  - 标签1
  - 标签2
version: 1.0.0
---

# Agent名称

## 角色定位
## 核心能力
## 工作原则
## 工作流程
## 输出格式
## 约束
## 最终行为
```

YAML Front Matter 让 Prompt 可以被程序化检索、分类与版本管理。

## Agent 工作流程

所有面向 Coding Agent 的 Prompt 遵循统一工作流程：

```text
Understand（理解需求）
    ↓
Inspect（检查项目）
    ↓
Plan（制定方案）
    ↓
Implement（实施）
    ↓
Test（验证）
    ↓
Review（复盘）
    ↓
Report（汇报）
```

所有 Prompt 强调：

> 不要在没有检查代码之前直接修改代码。

> 不要凭空假设项目结构。

> 不要声称执行了没有执行的命令。

> 不要声称测试通过，除非确实执行并获得结果。

> 如果测试无法执行，需要明确说明原因。

## 推荐组合

### 全栈开发

```text
产品经理
+
UI/UX 设计师
+
前端专家
+
后端架构师
+
数据库专家
+
测试专家
```

### AI 项目

```text
AI 产品经理
+
LLM 工程师
+
RAG 专家
+
后端架构师
+
AI 代码审查专家
+
测试 Agent
```

### Vibe Coding

```text
AI 编程 Agent
→
项目规划 Agent
→
技术方案 Agent
→
代码实现 Agent
→
Debug Agent
→
测试 Agent
→
Code Review Agent
→
项目验收 Agent
→
GitHub Agent
```

## Vibe Coding 工作流

完整的 Vibe Coding 流程见 [`12-专业工作流/VibeCodingAgent.md`](12-专业工作流/VibeCodingAgent.md) 与 [`workflows/VibeCoding完整流程.md`](workflows/VibeCoding完整流程.md)。

核心阶段：

```text
需求
↓
需求澄清
↓
项目分析
↓
PRD
↓
技术方案
↓
项目初始化
↓
UI/UX
↓
核心功能
↓
数据库
↓
API
↓
测试
↓
Bug 修复
↓
Code Review
↓
README
↓
Git
↓
GitHub
↓
Release
```

原则：不要一次性盲目生成整个项目。应该分阶段推进，每阶段完成后验证，遇到错误先修复，再进入下一阶段。

## GitHub 工作流

Git 与 GitHub 相关操作见 [`12-专业工作流/GitHubAgent.md`](12-专业工作流/GitHubAgent.md) 与 [`12-专业工作流/GitAgent.md`](12-专业工作流/GitAgent.md)。

核心原则：

> 在用户没有确认项目已经测试完成之前，不要擅自 push 到远程仓库。

覆盖：Git 初始化、`.gitignore`、`git status`、`git diff`、commit、branch、remote、push、README、Release、Tag、Pull Request、Issue、GitHub Actions。

## 项目验收流程

完整验收流程见 [`12-专业工作流/项目验收Agent.md`](12-专业工作流/项目验收Agent.md)。

检查清单：

```text
项目能否启动 → 依赖是否完整 → 环境变量 → 构建 → Lint
→ TypeCheck → Unit Test → Integration Test → E2E
→ 核心功能 → 错误处理 → 安全 → 性能
→ README → Git 状态 → 最终验收
```

最终生成结构化的《项目验收报告》，给出 `PASS / PASS WITH WARNINGS / FAIL` 结论。

## 最佳实践

1. **先读后改**：让 Agent 先读项目结构、配置文件、相关代码，再动手。
2. **分阶段推进**：大任务拆成小阶段，每阶段验证后再继续。
3. **明确约束**：在任务描述中补充"不要伪造测试结果"等约束。
4. **要求输出报告**：让 Agent 以统一格式汇报"任务理解 / 实施方案 / 修改内容 / 测试与验证 / 潜在问题"。
5. **保留上下文**：复杂任务使用组合 Agent，按流程依次推进。
6. **人工复核**：AI 的输出（尤其是测试结果、性能数据）需要人工抽检。

## 安全说明

> 安全类 Prompt 仅用于合法授权的安全研究、代码审计、防御、安全测试和漏洞修复。
>
> 使用者需要确保自己的行为符合适用法律、平台规则以及目标系统的授权范围。

## 如何贡献

欢迎贡献新的 Agent Prompt 或改进现有 Prompt，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## Roadmap

- [x] v1.0.0：13 大分类、238 个 Prompt/Workflow
- [ ] 扩展到 300+ 个 Agent
- [ ] 增加 Agent 组合工作流示例库
- [ ] 增加英文版 Prompt
- [ ] 增加 Agent 质量评测清单
- [ ] 增加 Prompt 版本管理与变更记录自动化

## License

本项目采用 [MIT License](LICENSE)。
