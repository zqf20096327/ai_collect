<a id="top"></a>

<div align="center">
  <img src="public/brand/feronavi-icon.svg" alt="Feronavi" width="64" height="64" />
  <h1>Feronavi</h1>
  <h3>让团队与 Agent，一起推进项目。</h3>
  <p><strong>开源项目协作平台，连接需求、知识与交付。</strong><br />多人一起写文档，项目知识随问随用，Agent 直接参与业务执行。</p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-526178?style=flat" alt="许可证：AGPL-3.0-only" /></a>
    <a href="#mcp"><img src="https://img.shields.io/badge/MCP-Server-4f6bed?style=flat" alt="完整 MCP Server" /></a>
    <a href="#rag"><img src="https://img.shields.io/badge/RAG-Built--in-247a73?style=flat" alt="内置 RAG 助手" /></a>
    <a href="#collaboration"><img src="https://img.shields.io/badge/CRDT-Collaboration-7861a8?style=flat" alt="CRDT 多人文档协作" /></a>
    <a href="#get-started"><img src="https://img.shields.io/badge/deploy-Self--hosted-526178?style=flat" alt="支持自托管部署" /></a>
  </p>
  <p>
    <a href="https://feronavi.com/zh/">官网</a> ·
    <a href="https://feronavi.com/zh/docs/overview/">使用文档</a> ·
    <strong><a href="#get-started">开始部署</a></strong> ·
    <a href="#overview">产品亮点</a> ·
    <a href="#collaboration">多人协作</a> ·
    <a href="#mcp">Agent 接入</a> ·
    <a href="#feedback">反馈</a>
  </p>
  <p><strong>简体中文</strong> / <a href="README.en.md">English</a></p>
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/screenshots/01-workbench-dark.png" />
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshots/10-workbench-light.png" />
  <img src="docs/screenshots/10-workbench-light.png" alt="Feronavi 工作台，界面与自绘窄边外框随明暗主题切换" width="100%" />
</picture>

<p align="center"><sub>真实界面 · 演示数据 · 明暗自适应 · <a href="#more-views">更多界面&nbsp;→</a></sub></p>

<a id="overview"></a>

## 从一个想法，到下一次交付。

从需求拆解、迭代推进，到方案沉淀与版本发布，Feronavi 把项目工作放在一个空间。团队在平台里协作，Agent 带着真实项目上下文参与执行，积累下来的知识随时可查、可引用。

| 核心能力 | 带来的改变 |
| --- | --- |
| **完整 MCP Server** | 让 Agent 读取上下文、执行业务操作并核验结果 |
| **内置 RAG 助手** | 跨项目检索知识，结合当前业务回答，引用可回到原文 |
| **多人实时协作** | 一起编辑文档、自动合并修改，短时断网后恢复同步 |
| **自主部署与接入** | 数据留在自己的环境，模型与身份体系由团队选择 |

<a id="mcp"></a>

## 完整 MCP Server，让 Agent 参与交付

**读取上下文、执行操作、核验结果。** Agent 可以创建工作项、调整指派与状态、维护文档、管理迭代和版本，并在操作后重新读取数据，确认执行结果。

例如，你可以这样安排一次版本准备：

> 检查本次迭代的未完成事项，梳理发布风险。先给我调整建议，确认后更新指派和状态，整理发布文档，最后核对执行结果。

服务器提供 MCP **工具、资源和提示词**，支持 **Streamable HTTP 与 stdio**。Codex、Claude Desktop、Cursor、VS Code 等支持 MCP 的客户端均可按协议接入，按任务动态发现所需能力。

平台界面、内置助手与 MCP 共用业务服务、权限和审计规则。Agent 的操作受账号权限与令牌范围约束，并支持幂等执行和版本冲突处理。

[**连接你的 MCP 客户端 →**](https://feronavi.com/zh/docs/mcp/)

<a id="rag"></a>

## 内置 RAG，让项目知识随问随用

**让积累下来的文档，成为此刻用得上的答案。** 独立助手支持跨项目对话，也可以聚焦指定项目；检索项目文档，查询实时业务信息，把知识依据与当前进展带入同一次对话。

> 这个需求当时为什么这样设计？结合方案文档和当前迭代，帮我整理本次上线的风险，并注明依据。

- **答案有出处**：引用可回到原文，检索范围遵循项目权限和文档访问规则。
- **对话够顺手**：流式输出、Markdown、Mermaid 图表，多会话按账号保存在服务端。
- **分析能落地**：查询分析直接执行，业务修改先展示操作内容，确认后执行并核验结果。

配置兼容的聊天模型与嵌入模型后，即可使用知识助手；检索与问答也通过 MCP 和公共 API 开放给外部应用。

<a id="rag-integration"></a>

<details>
<summary>接入 RAG：模型配置、MCP 与 API</summary>

1. **在平台内使用**：按[知识助手使用指南](https://feronavi.com/zh/docs/assistant/)配置聊天模型与嵌入模型，发布需要检索的项目文档并确认索引完成，再到知识助手选择项目范围提问。
2. **通过 Agent 使用**：按 [MCP 接入说明](https://feronavi.com/zh/docs/mcp/)连接实例，使用 `rag.projects` 查看可访问项目、`rag.search` 检索资料、`rag.chat` 获取带引用的回答。
3. **接入自己的应用**：从实例的 `GET /api/v1/openapi.json` 获取 OpenAPI 3.1 描述。使用平台 API 令牌进行 Bearer 认证，通过 `POST /api/v1/rag/search` 检索、`POST /api/v1/rag/chat` 问答；请求与响应结构、会话及流式接口见该描述。

OpenAPI 描述覆盖 RAG 公共 API。检索与引用遵循当前身份、令牌项目范围和文档权限。

</details>

<a id="collaboration"></a>

## 同一份文档，一起写；同一个项目，一起推进

一起完善方案、记录讨论、准备交付手册，也让 Agent 同时整理工作项、推进迭代。

- **多人一起写**：同时编辑项目文档，修改自动合并，历史版本可查看、可回滚。
- **断网后接着写**：已加载的文档可以在短时断网时继续编辑，修改暂存在当前浏览器，恢复连接后同步合并。
- **人与 Agent 一起推进**：业务修改遵循同一套权限和版本规则；出现冲突时，明确反馈，供操作者核对最新状态后重试。
- **进展自动到达**：业务变更和站内通知自动更新，跨标签、跨服务实例同步。

<details>
<summary>了解协作机制与离线条件</summary>

文档正文使用 Yjs CRDT 合并并发编辑。工作项、排期、审批等结构化业务通过版本校验、幂等执行、事务和提交后事件协同；同步与通知遵循各自的访问权限。

文档首次打开需要联网。离线修改暂存在当前浏览器；关闭页面后的恢复依赖站点本地存储可用，浏览器同时禁用 IndexedDB 和 localStorage 时无法保留这些记录。

</details>

## 为完整的交付节奏而设计

从今天要完成的任务，到下一次要发布的版本，每一步都有对应的工作视图。

| 工作环节 | 平台能力 |
| --- | --- |
| **收集与拆解** | 想法、需求、任务、缺陷、子任务，保留讨论与附件 |
| **计划与推进** | 里程碑、迭代、版本；看板、表格、日历与时间线 |
| **沉淀与交接** | 多人文档编辑、断网恢复、目录、版本历史、权限与回滚 |
| **规则与协作** | 自定义工作流、审批、自动化、SLA 与站内通知 |
| **洞察与统筹** | 个人工作台、燃尽图、累积流、项目集与审计记录 |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/screenshots/04-wiki-dark.png" />
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshots/11-wiki-light.png" />
  <img src="docs/screenshots/11-wiki-light.png" alt="Feronavi 项目产品手册，展示文档目录、正文与表格" width="100%" />
</picture>

## 能力，经过实际验证

多人编辑与断网恢复、真实 Codex 的业务操作、Docker 部署与备份恢复，均已有执行验证。相关自动化脚本随源码提供，可在自己的环境中复验。

<details>
<summary>查看验证范围</summary>

- **协作验证**：多人并发编辑、离线恢复、多标签与跨实例同步，以及权限隔离。
- **Agent 验证**：MCP 业务流程、操作确认、幂等执行与写后复读，并已通过真实 Codex 客户端执行验证。
- **部署验证**：Docker 全新安装、服务重启、备份恢复，以及源码与镜像构建产物的一致性。

这些验证针对业务行为和数据一致性；各客户端的任务规划与交互体验取决于其 MCP 支持和所用模型。

</details>

## 源码开放，部署由你掌握

部署在自己的环境中，接入自己的模型和身份体系。角色与数据范围控制访问，OIDC、LDAP / AD、2FA 和 SCIM 2.0 对接团队已有账号管理方式。

中文与英文、浅色与深色主题适配日常使用；邮件、IM、Webhook 和第三方集成按需配置。

<a id="get-started"></a>

## 开始使用

准备好 Docker Compose，下载编排文件即可启动一个新实例，无需安装 Node.js 或编译源码：

```bash
mkdir feronavi && cd feronavi
curl -fL https://raw.githubusercontent.com/JasperPengC/feronavi/v0.2.1/compose.yaml -o compose.yaml

# 首次安装：生成本地数据库密码
(umask 077; test -e .env || echo "DB_PASSWORD=$(openssl rand -hex 24)" > .env)

docker compose pull
docker compose up -d --wait
docker compose ps
```

启动后打开 [http://127.0.0.1:3000/setup](http://127.0.0.1:3000/setup)，按向导创建组织和管理员。

默认拉取应用 `ghcr.io/feronavi/feronavi-app:0.2.1` 与数据库 `ghcr.io/feronavi/feronavi-db:16-0.2.0`。本版预构建镜像支持并验证了 **Linux x86-64（amd64）**；其他架构尚未完成验收。

给团队开放访问前，请按[生产部署指南](https://feronavi.com/zh/docs/deployment/)配置 HTTPS 反向代理；升级已有实例前，请按[备份与升级指南](https://feronavi.com/zh/docs/operations/)备份数据库和数据卷，并核对数据库镜像的迁移要求。远程服务器的首次访问和启动排查见[快速开始](https://feronavi.com/zh/docs/quick-start/)。

<details>
<summary>从源码构建</summary>

需要修改源码时，可单独克隆本版并构建：

```bash
git clone --branch v0.2.1 --depth 1 https://github.com/JasperPengC/feronavi.git feronavi-source
cd feronavi-source
(umask 077; test -e .env || echo "DB_PASSWORD=$(openssl rand -hex 24)" > .env)
docker compose -f compose.yaml -f compose.source.yaml up -d --build --wait
```

首次构建会编译数据库扩展，需要一些时间。已有实例请继续使用原有目录、项目名和数据卷；版本升级时可在 `.env` 中显式设置 `FERONAVI_VERSION` 与 `FERONAVI_DB_VERSION`。

</details>

第一次使用，可以从这三步开始：

1. 创建项目、邀请成员，把第一项需求拆成可执行的工作项。
2. 发布一篇项目文档，按[知识助手使用指南](https://feronavi.com/zh/docs/assistant/)完成模型配置与索引，再让知识助手回答一个需要引用资料的问题。
3. 创建 API 令牌，按 [MCP 接入说明](https://feronavi.com/zh/docs/mcp/)连接 Agent，让它检查项目进展并给出下一步建议。

<a id="documentation"></a>

## 接入与帮助

[使用文档](https://feronavi.com/zh/docs/overview/)覆盖安装、日常协作、Agent 接入与运维，可按当前目标直接阅读：

| 我想要…… | 从这里开始 |
| --- | --- |
| **安装新实例** | [快速开始与首次配置](https://feronavi.com/zh/docs/quick-start/) |
| **给团队开放访问** | [生产部署与反向代理](https://feronavi.com/zh/docs/deployment/) |
| **管理项目与任务** | [项目与计划](https://feronavi.com/zh/docs/projects/) · [工作项与视图](https://feronavi.com/zh/docs/work-items/) |
| **编写与协作文档** | [项目文档](https://feronavi.com/zh/docs/documents/) |
| **连接 Agent** | [MCP 客户端配置与接入](https://feronavi.com/zh/docs/mcp/) |
| **使用知识助手** | [模型配置、检索与对话](https://feronavi.com/zh/docs/assistant/) |
| **管理成员与权限** | [权限与身份](https://feronavi.com/zh/docs/permissions/) |
| **备份或升级实例** | [备份、迁移与升级](https://feronavi.com/zh/docs/operations/) |
| **排查使用问题** | [常见问题](https://feronavi.com/zh/docs/faq/) |
| **报告安全问题** | [安全报告说明](SECURITY.md) |

开发接入可继续查看 [RAG 工具与公共 API](#rag-integration)，以及 [MCP stdio 桥接包说明](packages/feronavi-mcp/README.md)。

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

截图来自独立演示环境，使用虚构团队与业务数据。透明背景搭配自绘无品牌外框，正文截图随明暗主题切换。

</details>

<a id="acknowledgments"></a>

## 致谢

感谢以下支持方为 Feronavi 的开发提供模型 API 服务与额度支持。

### 友情赞助

- [Xlinks](https://api.xlinks.site/)

### LINUX DO 社区公益支持

- [Agent Router](https://agentrouter.org/)
- [Any Router](https://anyrouter.top/)
- [千刀佬](https://linux.do/u/andrew-hh)

*以上排名不分先后。*

## 社区

本项目在 [LINUX DO](https://linux.do) 社区推广。

<a id="feedback"></a>

## 反馈与许可

欢迎通过仓库 Issue 反馈问题和建议。项目由维护者独立开发和维护，目前不接收 Pull Request。安全漏洞请按[安全报告说明](SECURITY.md)联系，避免在公开 Issue 中披露细节。

Feronavi 使用 [AGPL-3.0-only](LICENSE) 许可证。

[返回顶部 ↑](#top)
