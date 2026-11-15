<div align="center">

<img src="https://github.com/jkjoker/datawork/blob/datawork/images/datawork_logo_new.png" alt="datawork" width="128" />

# datawork

**Local-First Personal AI Agent System**

*For anyone who encodes — 给每一个需要对信息进行编码的人*

<a href="https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout"><img src="https://img.shields.io/badge/Platform-Windows-blue?logo=windows" alt="Windows" /></a>
<a href="https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout"><img src="https://img.shields.io/badge/Built%20with-Python-3776AB?logo=python&logoColor=white" alt="Python" /></a>
<a href="https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Achangelog"><img src="https://img.shields.io/badge/Version-3.8.7f14.4.30-green" alt="Version" /></a>
<a href="https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout"><img src="https://img.shields.io/badge/License-Proprietary-red" alt="License" /></a>

[官方主页](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout) · [详细介绍](https://publish.obsidian.md/xm/wiki/%F0%9F%92%8E%20%E5%85%B3%E4%BA%8E/datawork) · [下载](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout) · [更新日志](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Achangelog)

---

[English](#english) | 简体中文

</div>

## 项目简介

datawork 是一个本地优先的个人 AI Agent 系统，以 Code Agent 为底层技术核心，将模型、工具、专业环境、长期记忆、任务和项目工作整合在同一个工作台中，让 AI 能围绕长期上下文持续协助工作。

通过桌面、终端与 Web 等入口使用，既能直接处理日常任务和软件开发，也能持续积累专业知识与工作方法，并支持直接在 datawork 构建可维护的 Agent 环境和业务应用。

工作台以人机协作为出发点，同时面向人的操作与 Agent 的执行来组织界面、文档、工具和长期积累。

## 核心能力

| 核心能力 | 说明 |
|---|---|
| Agent 内核与持续执行 | 以自研 Code Agent 为技术核心，整合模型调用、工具执行、上下文管理和会话持久化，支撑多步骤任务、长期工作与后续接续。 |
| 多模式与多 Agent 协作 | 支持内置 Agent、Workflow 与 ACP 外部 Agent；可派发内置 Code、ACP 和 Workflow 子 Agent，在独立会话中分工、并行与多轮协作。 |
| Workflow 专业环境 | 通过配置文件组织提示词、记忆、Skills、工具与运行设置，构建可由人和 Agent 持续维护的专业环境，可独立使用、承担子任务或供 APP 调用。 |
| 标准 API 与复杂 Web APP | 开放标准 API，涉及专业 Workflow、任务、工作区、Git、会话和独立存储等能力，支持结合自选前端与本机后端开发业务应用，并在 Web 工作台中使用。 |
| 长期记忆与知识积累 | 支持多记忆库、全文检索与 Agent 读写，将资料、经验、代码片段和研究结论积累为后续任务可调用的长期上下文。 |
| 任务与项目推进 | 清单、Todo、Task 三层任务结构，支持拆解、优先级、依赖与进度管理，让人和 Agent 围绕同一套任务记录持续推进工作。 |
| Skills、工具与 MCP | 以 Skills 复用专业方法，通过内置工具、Python 插件和标准 MCP 接入文件、命令、数据与外部服务，形成可扩展的执行能力。 |
| 模型与协议支持 | 统一管理多供应商、多协议和自定义模型，配置接口、推理深度、视觉与工具调用能力，按任务选择模型与运行方式。 |
| 桌面、终端与 Web 入口 | 提供桌面主面板、Coder、Mini Chat、内置命令行及 Web 工作台；支持从手机、平板或其他电脑的浏览器使用本机服务。 |
| 项目开发与代码研读 | 集成工作区、代码编辑、Git 差异查看与提交研读记录，结合 Agent 完成代码理解、开发、调试与审核，并保存项目演进中的判断。 |
| 人与 Agent 共用终端 | 内置命令行支持命令执行与 Agent 对话；Computer Use 终端提供共享的常驻 PowerShell，保留交互现场，支持部署、排障与远程运维。 |
| 本地优先、权限与隐私 | 工作数据默认在本地保存，无需 datawork 账号；提供安全护栏、文件白名单、工具审批、会话级权限与 Web 访问保护，第三方模型和外部服务按需连接。 |
| 调用记录与成本管理 | AI 调用账本记录模型用量、费用、耗时和来源，支持按模型、入口与会话查看，便于长期使用中的成本分析与复盘。 |

## 个人 Agent 系统如何落地

个人 Agent 系统围绕持续的个人工作组织能力：Agent 执行任务，记忆保存背景与经验，Skills 沉淀工作方法，工具连接实际操作，APP 提供业务界面。每次工作中经过验证的积累，都可以成为后续任务的基础。

**在 datawork 中，Skills、提示词、工具配置和使用规则，都像记忆一样被精细维护。** 需要持续维护的不仅是“知道什么”，还有“怎样判断、怎样工作、使用哪些工具”。这些专业积累可由人和 Agent 共同查看、修订与复用。

Workflow 将这些积累组织成专属的专业环境：集中管理一个领域的规则、记忆、Skills、工具范围与运行设置，让每类事项有明确的工作边界和积累归属。专业能力由此有了可以持续维护、独立使用和参与协作的载体。

| 使用方式 | 怎样落地 |
|---|---|
| 直接开始工作 | 配置模型，使用默认 Code Agent；明确项目工作区，维护项目的 `MEMORY.md`，即可开展日常任务和复杂项目开发。 |
| 拆分独立任务 | 直接使用内置 Code 子 Agent，分担分析、整理、开发或检查工作，无需预先创建专业档位。 |
| 建立专业环境 | 创建专属 Workflow，精细管理提示词、记忆、Skills、工具和运行设置，让长期事项在聚焦的环境中持续积累。 |
| 组织专业协作 | 将 Workflow 配置为专业子 Agent 的派发目标，由主 Agent 或其他 Workflow 调度；也可接入 ACP 外部 Agent，组织开发与自动化流程。 |
| 构建专属应用 | 在 Web 工作台开发自己的 APP，通过标准 API 复用已开放的平台能力与数据，按需增加前端和本机后端，把积累转化为日常工作入口。 |

**面向人，也面向 Agent。** 用户可以通过配置与管理界面查看、调整和确认，Agent 则有可直接查阅的内置教程、接口文档与配套工具，据此完成 Agent 与子 Agent 配置，以及插件、Workflow、APP 的开发和检查。双方围绕同一套项目资料、任务记录和专业环境协作，记忆、Skills 与工具配置可以共同维护，终端中的操作也可以由人接手或交给 Agent 继续。

界面便于人理解和控制，文档与工具便于 Agent 理解和执行，工作中的经验又能回到可持续维护的积累中。这构成了 datawork 的人机协作环境。各层能力按需采用，无需在开始使用前完成全部配置。

## 界面预览

<div align="center">
<img src="https://github.com/jkjoker/datawork/blob/datawork/images/Pasted%20image%2020260619221829.png" width="55%" />
<img src="https://github.com/jkjoker/datawork/blob/datawork/images/Pasted%20image%2020260619222051.png" width="35%" />
</div>

## 快速开始

```text
1. 下载安装包
2. 安装并启动 datawork
3. 设置工作路径与笔记保存路径
4. 在「模型管理」中添加模型
5. 发送一条消息确认 AI 联通状态
```

当前桌面版主要面向 **Windows 10 及以上系统**构建和测试。

## 文档

- [官方主页 / 下载](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout)
- [详细介绍](https://publish.obsidian.md/xm/wiki/%F0%9F%92%8E%20%E5%85%B3%E4%BA%8E/datawork)
- [更新日志](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Achangelog)

## 许可证

datawork 当前为**专有软件**，不是开源项目，源码未对外开放。Windows 桌面应用是目前唯一对外开放的产品形态。

若有分发授权、商业使用或其他对外合作需求，请联系作者沟通。

## 联系

**作者**：jk.zhou  
**Email**：1406584456@qq.com  
**个人网站**：[publish.obsidian.md/xm](https://publish.obsidian.md/xm)

---

<a name="english"></a>

<div align="center">

# datawork

**Local-First Personal AI Agent System**

*For anyone who encodes — For everyone who needs to encode information*

</div>

## About

datawork is a local-first personal AI Agent system built around the Code Agent runtime. It brings models, tools, professional environments, long-term memory, tasks, and project work into one workbench, enabling AI to provide ongoing assistance grounded in long-term context.

Desktop, terminal, and Web interfaces support everyday tasks and software development, the ongoing accumulation of professional knowledge and working methods, and the creation of maintainable Agent environments and business applications directly within datawork.

## Key Features

| Core capability | Description |
|---|---|
| Agent runtime and ongoing execution | The in-house Code Agent core integrates model invocation, tool execution, context management, and persistent sessions for multi-step tasks, ongoing work, and later continuation. |
| Multiple modes and Agent collaboration | Built-in Agents, Workflow, and external ACP Agents, with built-in Code, ACP, and Workflow sub-Agents for delegation, parallel work, and continued collaboration in independent sessions. |
| Professional Workflow environments | Organize prompts, memory, Skills, tools, and runtime settings through configuration files. People and Agents can maintain these environments for independent use, delegated tasks, or invocation from APPs. |
| Standard API and complex Web APPs | Standard APIs expose capabilities including professional Workflows, tasks, workspaces, Git, sessions, and independent storage, supporting business applications built with a chosen frontend and local backend for use in the Web workbench. |
| Long-term memory and knowledge | Multiple memory libraries, full-text search, and Agent read/write access turn materials, experience, code snippets, and research findings into reusable context for later work. |
| Task and project management | A three-level structure of lists, Todos, and Tasks supports decomposition, priorities, dependencies, and progress tracking, with people and Agents working from shared task records. |
| Skills, tools, and MCP | Reuse professional methods through Skills and extend execution with built-in tools, Python plugins, and standard MCP for files, commands, data, and external services. |
| Model and protocol support | Manage multiple providers, protocols, and custom models, including endpoints, reasoning depth, vision, and tool calling; select models and operating modes for each task. |
| Desktop, terminal, and Web interfaces | Desktop AI panel, Coder, Mini Chat, built-in command line, and Web workbench, with browser access to host services from phones, tablets, or other computers. |
| Project development and code review | Workspaces, code editing, Git diff views, and commit review notes combine with Agents for code understanding, development, debugging, and review while preserving decisions made as projects evolve. |
| Terminals shared by people and Agents | The built-in command line supports commands and Agent conversations. The Computer Use Terminal provides a shared, persistent PowerShell for interactive work, deployment, troubleshooting, and remote administration. |
| Local-first, permissions, and privacy | Work data is stored locally by default without a datawork account. Security guardrails, file whitelists, tool approval, session permissions, and Web access protection control access; third-party models and services connect as needed. |
| Call records and cost management | An AI call ledger records model usage, cost, latency, and source, with views by model, interface, and session for cost analysis and review over time. |

## Putting a Personal Agent System into Practice

A personal Agent system organizes capabilities around ongoing work: Agents carry out tasks, memory preserves context and experience, Skills capture working methods, tools connect Agents to actions, and APPs provide task-specific interfaces. Useful, validated outcomes from each task can inform the next.

**In datawork, Skills, prompts, tool configurations, and working rules are maintained with the same care as memory.** Ongoing work is not only about preserving what is known, but also how to make decisions, how to work, and which tools to use. People and Agents can review, refine, and reuse these professional assets together.

Workflow organizes these assets into dedicated professional environments. It brings a domain's rules, memory, Skills, tool scope, and runtime settings together, giving each area of work a clear boundary and a place to build its own knowledge. A Workflow makes professional capabilities maintainable, independently usable, and ready for collaboration.

| Stage | How it works |
|---|---|
| Start working | Configure a model and use the default Code Agent. Set the project workspace and maintain its `MEMORY.md` to support everyday work and complex project development. |
| Delegate a task | Use the built-in Code sub-Agent to handle analysis, organization, development, or review without first creating a specialized profile. |
| Build a professional environment | Create a dedicated Workflow to manage prompts, memory, Skills, tools, and runtime settings, so ongoing work can accumulate in a focused environment. |
| Organize specialized collaboration | Configure a Workflow as a professional sub-Agent target, coordinated by the primary Agent or another Workflow. ACP Agents can also be connected for external Agent capabilities and automation workflows. |
| Build a custom application | Develop an APP in the Web workbench. Use standard APIs to access platform capabilities and data, and add a custom frontend and local backend as needed to turn accumulated work into a daily workspace. |

**Designed for people and Agents.** People can review, adjust, and confirm settings through configuration and management interfaces. Agents can consult the built-in tutorials, API documentation, and supporting tools to configure Agents and sub-Agents, and to develop and check plugins, Workflows, and APPs. Both work with the same project materials, task records, and professional environments. Memory, Skills, and tool configurations can be maintained together, and terminal work can be taken over by a person or continued by an Agent.

Interfaces help people understand and control their work; documentation and tools help Agents understand and carry it out. Experience from that work can then return to a body of knowledge that can be maintained over time. This is the foundation of datawork's human-Agent collaboration environment. Each layer can be adopted as needed; none has to be configured before getting started.

## Screenshots

<div align="center">
<img src="https://github.com/jkjoker/datawork/blob/datawork/images/Pasted%20image%2020260619221829.png" width="55%" />
<img src="https://github.com/jkjoker/datawork/blob/datawork/images/Pasted%20image%2020260619222051.png" width="35%" />
</div>

## Quick Start

```text
1. Download the installer
2. Install and start datawork
3. Set the workspace and note paths
4. Add a model in Model Management
5. Send a message to verify AI connectivity
```

The current desktop version is built and tested mainly for **Windows 10 and later**.

## Documentation

- [Homepage / Download](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Aabout)
- [Detailed Introduction](https://publish.obsidian.md/xm/wiki/%F0%9F%92%8E%20%E5%85%B3%E4%BA%8E/datawork)
- [Changelog](https://publish.obsidian.md/xm/wiki/%E6%95%99%E7%A8%8B/datawork%EF%BC%9Achangelog)

## License

datawork is proprietary software. It is not open source, and the source code is not publicly available. The Windows desktop application is currently the only public product form.

For distribution authorization, commercial use, or other external cooperation, please contact the author.

## Contact

**Author**: jk.zhou  
**Email**: 1406584456@qq.com  
**Website**: [publish.obsidian.md/xm](https://publish.obsidian.md/xm)
