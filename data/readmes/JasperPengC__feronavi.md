<a id="top"></a>

<div align="center">
  <img src="public/brand/feronavi-icon.svg" alt="Feronavi" width="64" height="64" />
  <h1>Feronavi</h1>
  <h3>项目协作，进入 Agent 时代。</h3>
  <p><strong>为人和 Agent 而生的开源项目协作平台。</strong><br />从需求到交付，连接团队、知识与执行。</p>
  <p>完整 MCP Server · 内置 RAG · 业务流程闭环 · 自托管</p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-526178?style=flat" alt="许可证：AGPL-3.0-only" /></a>
    <a href="#mcp"><img src="https://img.shields.io/badge/MCP-Server-4f6bed?style=flat" alt="完整 MCP Server" /></a>
    <a href="#rag"><img src="https://img.shields.io/badge/RAG-Built--in-247a73?style=flat" alt="内置 RAG 助手" /></a>
    <a href="#get-started"><img src="https://img.shields.io/badge/deploy-Self--hosted-526178?style=flat" alt="支持自托管部署" /></a>
  </p>
  <p>
    <strong><a href="#get-started">开始部署</a></strong> ·
    <a href="#overview">产品亮点</a> ·
    <a href="#mcp">MCP 接入</a> ·
    <a href="#rag">RAG 助手</a> ·
    <a href="#more-views">更多界面</a> ·
    <a href="#documentation">文档导航</a> ·
    <a href="#feedback">问题反馈</a>
  </p>
  <p><strong>简体中文</strong> / <a href="README.en.md">English</a></p>
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/screenshots/01-workbench-dark.png" />
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshots/10-workbench-light.png" />
  <img src="docs/screenshots/10-workbench-light.png" alt="Feronavi 工作台，界面与 iMac 外框随明暗主题切换" width="100%" />
</picture>

<p align="center"><sub>当前版本的真实界面 · 独立演示数据 · 随明暗主题切换</sub></p>

<a id="overview"></a>

## 从一个想法，到下一次交付。

一项需求背后，有计划、讨论、方案，也有一次次推动它向前的行动。Feronavi 把它们连成完整的工作流：团队在平台里协作，Agent 通过 MCP 参与执行，内置 RAG 为对话提供项目知识与来源依据。

你可以自己推进一项工作，也可以让智能体带着真实项目上下文一起完成。

| 核心能力 | 带来的改变 |
| --- | --- |
| **完整 MCP Server** | 把业务能力交给 Agent，从发现上下文、执行操作到核验结果，走完业务流程 |
| **内置 RAG 助手** | 让项目知识进入对话，跨项目检索、结合业务分析，答案附有来源 |
| **贯穿交付的协作** | 需求、工作项、文档、迭代与版本相互关联，进展和决策都有迹可循 |
| **自主部署与接入** | 源码开放，数据、身份体系、模型供应商与集成由团队管理 |

<a id="mcp"></a>

## 完整 MCP Server，让 Agent 参与交付

**从理解任务，到执行操作，再到确认结果。** Feronavi 为 Agent 提供可完成业务闭环的标准入口，让项目协作成为智能体可以实际参与的工作。

例如，你可以这样安排一次版本准备：

> 检查本次迭代的未完成事项，梳理发布风险。先给我调整建议，确认后更新指派和状态，整理发布文档，最后核对执行结果。

| 环节 | Agent 可以做什么 |
| --- | --- |
| **理解上下文** | 发现业务工具，读取项目、成员、字段与工作流，明确任务范围 |
| **推进业务** | 创建和更新工作项、推进状态、维护文档、管理迭代与版本 |
| **核验结果** | 写入后重新读取业务数据，确认持久化结果，处理版本冲突与安全重试 |

服务器提供 MCP **工具、资源和提示词**，支持 **Streamable HTTP 与 stdio**。Codex、Claude Desktop、Cursor、VS Code 等支持 MCP 的客户端均可按协议接入，按任务动态发现所需能力。

平台界面、内置助手与 MCP 共用业务服务和权限规则。账号权限、令牌范围、幂等写入和操作审计贯穿执行过程；登录、2FA 等身份验证通过专门入口完成。

[**连接你的 MCP 客户端 →**](packages/feronavi-mcp/README.md)

<a id="rag"></a>

## 内置 RAG，让项目知识随问随用

**让积累下来的文档，成为此刻用得上的答案。** 独立助手支持跨项目对话，也可以聚焦指定项目；检索项目文档，查询实时业务信息，把知识依据与当前进展带入同一次对话。

> 这个需求当时为什么这样设计？结合方案文档和当前迭代，帮我整理本次上线的风险，并注明依据。

- **答案有出处**：引用可回到原文，检索范围遵循项目权限和文档访问规则。
- **对话够顺手**：流式输出、Markdown、Mermaid 图表，多会话按账号保存在服务端。
- **分析能落地**：查询分析直接执行，业务修改先展示操作内容，确认后执行并核验结果。

知识问答同时提供 MCP 工具与 OpenAPI 3.1 描述的公共 API，内置助手和外部 Agent 可以使用同一套检索与业务能力。配置自己的兼容模型与嵌入供应商后，即可使用。

[**了解 RAG 助手与 API →**](#rag)

## 为完整的交付节奏而设计

从个人今天要做的事，到团队下一次要交付的版本，Feronavi 提供相互连接的工作视角。

| 工作环节 | 平台能力 |
| --- | --- |
| **收集与拆解** | 想法、需求、任务、缺陷、子任务，保留讨论与附件 |
| **计划与推进** | 里程碑、迭代、版本；看板、表格、日历与时间线 |
| **沉淀与交接** | 项目文档、目录、版本历史、权限与回滚 |
| **规则与协作** | 自定义工作流、审批、自动化、SLA 与站内通知 |
| **洞察与统筹** | 个人工作台、燃尽图、累积流、项目集与审计记录 |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/screenshots/04-wiki-dark.png" />
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshots/11-wiki-light.png" />
  <img src="docs/screenshots/11-wiki-light.png" alt="Feronavi 项目产品手册，展示文档目录、正文与表格" width="100%" />
</picture>

## 能力，经过实际验证

MCP 与内置助手均已完成 **22 条代表性业务流程验收**，覆盖交付、计划、文档、工作流、协作、项目组合和组织管理等场景。真实 Codex 联调完成 **68 次 MCP 调用、18 项业务结果核验**。

这些验证覆盖业务执行、权限和写后结果；各客户端的任务规划与交互体验取决于其 MCP 支持和所用模型。

## 源码开放，部署由你掌握

部署在自己的环境中，接入自己的模型和身份体系。角色与数据范围控制访问，OIDC、LDAP / AD、2FA 和 SCIM 2.0 对接团队已有账号管理方式。

中文与英文、浅色与深色主题适配日常使用；邮件、IM、Webhook 和第三方集成按需配置。

<a id="get-started"></a>

## 开始使用

准备好 Docker Compose，在源码根目录执行以下命令，构建并启动一个新实例：

```bash
# 首次安装：生成本地数据库密码
(umask 077; test -e .env || echo "DB_PASSWORD=$(openssl rand -hex 24)" > .env)

docker compose -f compose.yaml -f compose.source.yaml up -d --build
docker compose -f compose.yaml -f compose.source.yaml ps
```

启动后打开 [http://127.0.0.1:3000/setup](http://127.0.0.1:3000/setup)，按向导创建组织和管理员。首次构建会编译数据库扩展，需要一些时间。

生产部署请将实例放在 HTTPS 反向代理之后；升级已有实例前，请先备份数据库和数据卷，并核对数据库镜像的迁移要求。

<a id="documentation"></a>

## 文档导航

| 我想要…… | 从这里开始 |
| --- | --- |
| **部署与运维** | [安装与首次配置](#get-started) |
| **连接 Agent** | [MCP 客户端配置与接入](packages/feronavi-mcp/README.md) |
| **接入知识与对话** | [RAG 助手与公共 API](#rag) |
| **报告安全问题** | [安全报告说明](SECURITY.md) |

<a id="more-views"></a>

## 更多界面

<details>
<summary>展开查看项目概览、洞察、时间线与主题预览</summary>

| 项目与交付 | 工作区与外观 |
| --- | --- |
| [工作看板](docs/screenshots/03-board.png) | [知识助手](docs/screenshots/12-assistant.png) |
| [项目概览](docs/screenshots/02-project-overview.png) | [全部项目](docs/screenshots/09-projects.png) |
| [迭代洞察](docs/screenshots/05-insights.png) | [个人偏好](docs/screenshots/07-settings.png) |
| [交付时间线](docs/screenshots/08-timeline.png) | [登录页面](docs/screenshots/06-login.png) |
| [深色工作台](docs/screenshots/01-workbench-dark.png) | [深色文档](docs/screenshots/04-wiki-dark.png) |

截图使用独立演示环境中的虚构团队与业务内容，界面以 3840 × 2160 分辨率拍摄，整图为 4400 × 3000，背景透明。外框为自绘的无品牌窄边框设计，四边等宽，搭配简洁支架；正文截图随阅读主题切换，浅色使用银色外框，深色使用灰色外框。

</details>

<a id="feedback"></a>

## 反馈与许可

欢迎通过仓库 Issue 反馈问题和建议。项目由维护者独立开发和维护，目前不接收 Pull Request。安全漏洞请按[安全报告说明](SECURITY.md)联系，避免在公开 Issue 中披露细节。

Feronavi 使用 [AGPL-3.0-only](LICENSE) 许可证。

[返回顶部 ↑](#top)
