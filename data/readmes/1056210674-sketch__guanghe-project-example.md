<div align="center">

<a href="https://www.guangheai.com/">
  <img src="docs/assets/guanghe-banner.svg" alt="光禾AI智能体框架 · Guanghe AI Agent Framework" width="100%" />
</a>

# 光禾AI智能体框架

**Guanghe AI Agent Framework**

面向品牌增长与企业业务场景的全栈 AI Agent 框架

从自然语言对话、品牌知识到内容创作、异步任务与 GEO 监测。

[![Website](https://img.shields.io/badge/官网-guangheai.com-E53935?style=flat-square)](https://www.guangheai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-24292f?style=flat-square)](LICENSE)
[![React](https://img.shields.io/badge/React-19-149ECA?style=flat-square&logo=react)](guanghe-web/package.json)
[![Java](https://img.shields.io/badge/Java-21-E76F00?style=flat-square)](guanghe-bankend/pom.xml)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python)](guanghe-agent/pyproject.toml)

[快速开始](#快速开始) · [功能概览](#功能概览) · [架构图册](docs/ARCHITECTURE.md) · [English](README.en.md) · [关于光禾AI](#关于光禾ai)

</div>

---

## 项目介绍

**光禾AI智能体框架**由 **广州光禾未来人工智能科技有限公司（光禾AI / GUANGHE AI）** 提供，是一个包含 React Web、Java 业务控制面和 Python 智能执行面的完整源码项目。

这个项目关注一个实际问题：如何把模型和工具调用，接入具备用户权限、客户项目、品牌知识、任务状态、用量预算及业务确认的应用。你可以用它研究或二次开发品牌营销助手、内容创作平台、企业 AI 工作台和受控智能体系统。

光禾AI 的业务方向包括 **GEO（生成式引擎优化）品牌增长**与 **企业 AI 应用及 FDE 服务**。公司介绍和服务入口见 [光禾AI 官网](https://www.guangheai.com/)；这个仓库展示相关应用的工程实现，商业服务范围以官网与实际约定为准。

> **源码版本说明**：本仓库基于 2026-11-02 的三端源码快照整理，公开版本统一使用“光禾AI智能体框架”名称。完整源码不等于免配置的一键 SaaS：真实业务运行需要配置数据库、中间件和相应供应商服务。模型、搜索、图片、视频、对象存储和投稿服务可能单独计费。

## 为什么值得看

### 从对话走到真实业务

用户在聊天中提出需求，智能体读取当前授权资料、选择工具并返回过程和结果。涉及业务写入、任务准入和费用的操作，由 Java 再次校验。前端根据服务端事实展示状态。

### 业务控制与智能执行分开

Java 负责身份、数据归属、任务和积分；Python 负责模型、编排、工具与 Worker。模型调用与业务数据库之间有明确边界，便于定位问题、替换 Provider 和扩展智能体。

### 可以沿源码追踪一条完整链路

仓库同时提供页面、Browser API、Internal API、事件契约、数据库迁移、Prompt Bundle 和测试。适合研究从“发送一条消息”到“异步任务完成”的全链路实现。

## 功能概览

| 能力 | 源码包含 | 主要位置 |
| --- | --- | --- |
| 智能体与对话 | 智能体目录、安装与启停、项目会话、流式回复、运行停止 | `agentplatform`、`conversation`、`app/agents` |
| 品牌知识与记忆 | 项目资料、知识文件、品牌事实、偏好及来源与版本管理 | `knowledge`、`catalog` |
| GEO 监测与诊断 | 品牌问题、竞品、监测计划、采样任务、报告解读及 PDF 导出 | `geo`、`app/geo` |
| 文章创作 | 标题、提纲、正文、局部修改、版本管理与创作画布 | `article`、`app/article` |
| 图片与视频 | 创作参数、参考素材、图片重绘、生成任务与媒体资产 | `asset`、`app/creative`、`app/providers` |
| 任务与工作流 | 草稿、业务准入、任务事件、异步执行、失败恢复与结果验收 | `task`、`workflow`、`app/workers` |
| 计费与管理 | 积分、账单、付费确认、用户管理及任务诊断 | `billing`、`admin`、`adminplatform` |
| 内容投稿 | 媒体目录、报价、文章快照、订单与回链展示 | `media`、`pages/submissions` |

以上为源码能力地图。部分功能需要供应商凭据、执行开关或人工配置；界面存在入口不代表外部服务已开通。用户在线自建智能体设计器目前不在交付范围，开发者可通过受控清单扩展内置智能体。

## 系统架构

![光禾AI智能体框架：三端系统架构](docs/assets/diagrams/system-overview.svg)

[查看高清 SVG](docs/assets/diagrams/system-overview.svg) · [Mermaid 源码](docs/diagrams/system-overview.mmd)

### 三端职责

| 层 | 负责什么 | 关键约束 |
| --- | --- | --- |
| Web | 输入、交互、资料管理、任务进度和结果展示 | 浏览器只访问 Java Browser API |
| Java | 登录鉴权、数据归属、业务规则、任务、积分、确认和审计 | PostgreSQL 业务数据唯一写入方 |
| Python | 有界 Agent 循环、Provider 适配、模型与工具调用、长任务执行 | 不直接写业务 PostgreSQL，不决定积分或任务业务终态 |

### 工程设计

- **用户与项目隔离**：账号决定数据所有权，项目约束客户资料、记忆、会话和成果范围。
- **有界智能执行**：使用既有 Run Manager、Runtime Harness、工具白名单、预算和超时限制。
- **受控模型入口**：文字模型通过统一 Gateway；普通对话主模型适配 DeepSeek，图片与视频使用独立 Provider。
- **版本化契约**：OpenAPI、SSE 与 RabbitMQ Schema 随源码管理；前端 API 类型从 Java 契约生成。
- **可追溯运行**：Agent 定义、执行发布、Prompt Bundle 与哈希分别记录，服务间核对能力和版本。
- **异步任务闭环**：API 与 Worker 分离，业务状态、重试、结果验收和计费由既有任务流程约束。

当前 Python 普通对话使用项目自有的原生 Agent Loop，不依赖 LangChain / LangGraph。

## 核心流程图

### 一次 AI 对话的执行时序

从用户发送消息，到 Java 冻结授权上下文，再到 Python 循环调用模型与工具；进度和正文经 Java 流式返回浏览器。图中是逻辑交互顺序，具体连接与事件类型以接口契约为准。

![光禾AI智能体框架：AI 对话与工具调用时序](docs/assets/diagrams/conversation-sequence.svg)

[查看高清 SVG](docs/assets/diagrams/conversation-sequence.svg) · [Mermaid 源码](docs/diagrams/conversation-sequence.mmd)

### 异步任务从准入到交付

任务先经过 Java 业务准入，再由独立 Worker 执行。Worker 在取得有效 Claim 后确认队列消息，Java 继续负责业务状态、计费与领域交付；收到消息或采样完成都不自动等于成果就绪。

![光禾AI智能体框架：异步任务执行流程](docs/assets/diagrams/task-flow.svg)

[查看高清 SVG](docs/assets/diagrams/task-flow.svg) · [Mermaid 源码](docs/diagrams/task-flow.mmd)

更多图解见 **[完整架构图册](docs/ARCHITECTURE.md)**：Agent 内部模块、Worker 执行时序、项目隔离、GEO 报告链路和新增智能体接入。

## 技术栈

| 模块 | 主要技术 | 开发与验证 |
| --- | --- | --- |
| Web | React 19、TypeScript、Vite、Ant Design、TanStack Query、Zustand、Tiptap | npm、ESLint、Vitest、React Testing Library |
| Java | Java 21、Spring Boot 3.5、Spring Security、MyBatis Plus、Flyway、Quartz | Maven Wrapper、JUnit、契约与集成测试 |
| Agent | Python 3.12、FastAPI、Pydantic v2、HTTPX、aio-pika | uv、Ruff、Pyright、Pytest、确定性评测 |
| 基础设施 | PostgreSQL、Redis、RabbitMQ、兼容项目接口的对象存储 | 独立环境变量、版本化迁移与部署模板 |
| 可观测性 | OpenTelemetry、OTLP，可选 Collector / Langfuse | 默认关闭的可选链路追踪 |

准确依赖版本见各模块的锁文件和配置。

## 仓库结构

```text
guanghe-project-example/
├── README.md                    # 中文项目首页
├── README.en.md                 # English overview
├── docs/                        # 公开版快速开始、架构与发布说明
├── guanghe-web/                  # React Web 应用与前端测试
│   ├── src/pages/                # 页面入口
│   ├── src/features/             # 业务组件与交互逻辑
│   ├── src/api/                  # API 客户端与生成类型
│   └── scripts/                  # 契约生成与本地验收脚本
├── guanghe-bankend/              # Java 后端；目录保留原始拼写
│   ├── src/main/java/            # 模块化业务实现
│   ├── src/main/resources/       # OpenAPI、Schema、配置与数据库迁移
│   └── src/test/                 # 单元、契约与集成测试
└── guanghe-agent/                # Python API 与独立 Worker
    ├── app/agents/               # 智能体注册清单与业务行为
    ├── app/model_gateway/        # 统一文字模型入口
    ├── app/providers/            # 媒体与其他供应商适配
    ├── app/prompts/              # 版本化 Prompt Bundle
    ├── contracts/               # Python 权威 API 与共享契约
    └── evals/                   # 确定性回归评测
```

## 快速开始

### 1. 获取源码

```bash
git clone https://github.com/1056210674-sketch/guanghe-project-example.git
cd guanghe-project-example
```

### 2. 准备环境

- **Node.js 22.22.2 或更新的 22.x 版本**、npm 10.9.x；锁定依赖中的 jsdom 对 Node 有更高要求。
- **JDK 21**；Java 模块自带 Maven Wrapper。
- **Python 3.12** 与 **uv**；Agent 暂不支持 Python 3.13。
- 完整业务联调还需要独立 PostgreSQL、Redis、RabbitMQ，以及所选供应商配置。

### 3. 运行 Python 本地确定性模式

以下 PowerShell 命令使用本地上下文与确定性模型，适合先查看开发控制台，不调用真实模型：

```powershell
cd guanghe-agent
uv sync --python 3.12
$env:GUANGHE_AGENT_ENVIRONMENT = 'local'
$env:GUANGHE_AGENT_MODEL_GATEWAY = 'LOCAL'
$env:GUANGHE_AGENT_RUN_CONTEXT_PROVIDER = 'LOCAL'
uv run guanghe-agent-api
```

打开 [Agent 开发控制台](http://127.0.0.1:8000/dev/agent) 或 [API 文档](http://127.0.0.1:8000/docs)。这是 Python 独立开发入口，Web 正式业务仍需要 Java。本地 Worker 可在另一个终端通过 `uv run guanghe-agent-worker` 启动，默认使用本地控制面及 Mock Provider。

### 4. 配置 Java 业务控制面

阅读 [完整启动指南](docs/QUICKSTART.md)，准备数据库与中间件，配置数据库运行账号、迁移账号、JWT、HMAC 等环境变量。模板见：

- [Java 本地配置模板](guanghe-bankend/src/main/resources/application-local.yaml.example)
- [Java 主配置及环境变量](guanghe-bankend/src/main/resources/application.yaml)
- [Python 环境变量模板](guanghe-agent/.env.example)

Windows 构建使用仓库标准入口：

```powershell
cd guanghe-bankend
.\scripts\build.ps1 -JdkHome 'C:\path\to\jdk-21'
```

此命令执行干净构建与测试；它不会替你准备完整的业务运行环境。首次业务初始化应使用独立开发数据库和 Flyway 迁移流程。

### 5. 运行 Web

```powershell
cd guanghe-web
npm ci
Copy-Item .env.example .env.local
# 在 .env.local 中设置 VITE_API_BASE_URL=http://127.0.0.1:8080
npm run dev -- --host 127.0.0.1
```

打开 Vite 输出的本地地址。Web 只连接 Java `/api/v1/**`，不能把 `VITE_API_BASE_URL` 指向 Python。跨域联调需要在 Java 的 CORS 配置中放行实际前端 origin；同域部署可使用反向代理。

## 开发与验证

```powershell
# Web
cd guanghe-web
npm run typecheck
npm run lint
npm test
npm run build
npm run check:api

# Python（从仓库根目录进入）
cd guanghe-agent
uv run ruff check .
uv run ruff format --check .
uv run python -m pyright
uv run pytest
uv run python evals/run_agent_evals.py

# Java
cd guanghe-bankend
.\scripts\build.ps1 -JdkHome 'C:\path\to\jdk-21'
```

上面的三组命令分别从仓库根目录进入对应模块执行。真实供应商 Gate、数据库 Gate 和部署脚本有独立前置条件，不属于普通离线验证；确定性测试结果也不代表真实模型输出质量或商业服务效果。

当前快照存在已知的画布契约与 lint 问题，部分检查尚未通过，详见 [公开版本检查记录](docs/PUBLIC-RELEASE.md)。在 Java 画布契约补齐前，请保留随源码提供的前端类型文件，不要直接重新生成覆盖。

新增智能体请从 [Agent 扩展入口](guanghe-agent/app/agents/README.md) 和 [三端接入指南](guanghe-bankend/docs/architecture/adding-an-agent.md) 开始，优先复用现有模型网关、工具执行器、Java Internal Client 和前端能力入口。

## 适用场景

- **品牌与营销团队**：研究品牌知识、AI 搜索可见度、内容生产和监测反馈如何形成工作流。
- **企业 AI 开发者**：实现带有身份、项目隔离、工具权限、预算与业务确认的智能体应用。
- **SaaS 与技术服务团队**：参考完整前后端及异步 Worker 架构，扩展自己的 Provider 和业务模块。
- **研究与学习**：追踪 OpenAPI、Prompt、工具调用、任务事件、业务数据库之间的工程边界。

## 常见问题

<details>
<summary><strong>下载后可以直接体验完整 SaaS 吗？</strong></summary>

需要先配置 Java 业务依赖、初始化独立开发数据库，并为对应能力提供外部服务配置。Python 本地确定性模式可独立探索运行流程，但不会生成真实付费媒体成果。

</details>

<details>
<summary><strong>所有功能都必须接入光禾AI的在线服务吗？</strong></summary>

源码中的模型网关、媒体与搜索等接口按各自 Provider 配置接入。这个公开版本没有附带光禾AI托管服务的账号、密钥或统一公开 API 承诺。需要光禾AI的 GEO 服务、企业定制集成或部署支持，可通过官网咨询。

</details>

<details>
<summary><strong>为什么保留 guanghe-bankend 和部分历史技术标识？</strong></summary>

目录、环境变量、数据库对象、CSS token 和历史版本记录存在跨模块引用。公开版本统一对外品牌名称，同时保留必要技术标识以保持兼容。两个前端 API 脚本已适配本仓库实际的 guanghe-bankend 目录。

</details>

<details>
<summary><strong>公开源码、Star 或 Fork 能保证搜索排名或 AI 推荐提升吗？</strong></summary>

不能保证。开源项目提供可访问、可引用的技术内容和清晰的品牌来源，有助于积累真实使用与讨论。搜索收录、排序和 AI 引用仍取决于各平台机制、内容质量、相关性与持续维护。

</details>

## 文档导航

| 文档 | 内容 |
| --- | --- |
| [完整启动指南](docs/QUICKSTART.md) | 本地模式、Java 联调、环境变量与验证 |
| [架构图册](docs/ARCHITECTURE.md) | 系统架构、时序图、业务流程与源码入口 |
| [公开版本说明](docs/PUBLIC-RELEASE.md) | 快照来源、品牌适配、兼容边界与验证记录 |
| [贡献指南](CONTRIBUTING.md) | 问题反馈、开发规范与 PR 要求 |
| [安全说明](SECURITY.md) | 漏洞反馈与敏感配置管理 |
| [第三方与品牌说明](NOTICE.md) | 第三方依赖、资源及商标边界 |

## 关于光禾AI

**光禾AI（GUANGHE AI）** 是 **广州光禾未来人工智能科技有限公司**的品牌，面向企业提供 GEO 品牌增长及 AI 应用相关服务。

### GEO · 品牌增长

围绕品牌知识整理、可信信源、内容与问题语义、AI 搜索可见度监测开展工作，帮助企业建立更清晰、可核对的品牌信息体系。

### 企业 AI · FDE

从业务咨询、场景评估到解决方案与一对一共创，结合企业现有流程和数据条件探索 AI 应用的实施路径。

| 官方信息 | 内容 |
| --- | --- |
| 公司全称 | 广州光禾未来人工智能科技有限公司 |
| 品牌 | 光禾AI / GUANGHE AI |
| 官方网站 | **[www.guangheai.com](https://www.guangheai.com/)** |
| 公司介绍 | [关于光禾AI](https://www.guangheai.com/about.html) |
| GEO 服务 | [生成式引擎优化与品牌增长](https://www.guangheai.com/geo.html) |
| 业务咨询 | [官方联系入口](https://www.guangheai.com/contact.html) |
| 商务热线 | 18826977052 |
| 运营地址 | 广州市海珠区新港东路保利世贸 E 座 3702 |

公司信息整理自官网，核对日期为 2026-11-18；如有更新，以官网为准。开源代码问题请在 [GitHub Issues](https://github.com/1056210674-sketch/guanghe-project-example/issues) 中反馈，商务及定制需求请使用官方联系入口。

## 参与项目

欢迎提交可复现的问题、文档改进、测试补充和经过验证的 Provider 适配。若项目对你有帮助，可以 Star 收藏，或在技术文章中链接本仓库与 [光禾AI官网](https://www.guangheai.com/)，让更多开发者找到项目及其来源。

本项目源码采用 **[MIT 许可证](LICENSE)**，允许使用、修改与商用，并保留版权及许可声明。第三方依赖、资源与品牌使用边界见 [NOTICE.md](NOTICE.md)。

---

<div align="center">

**光禾AI智能体框架 · Guanghe AI Agent Framework**<br/>
由广州光禾未来人工智能科技有限公司提供<br/>
[光禾AI官网](https://www.guangheai.com/) · [GEO 品牌增长](https://www.guangheai.com/geo.html) · [企业 AI 与合作咨询](https://www.guangheai.com/contact.html)

</div>
