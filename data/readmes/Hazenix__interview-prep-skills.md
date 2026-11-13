# Interview Prep Skills · 技术面试准备

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[English](README.en.md) · [让 AI 安装](#安装) · [查看四个 skill 的示例](docs/examples.md)

**贴一条简历经历，直接拿到面试官可能问的主问题和追问。** 无需先做模拟面试，一次生成 Markdown 题单，可附简短参考回答。

想练临场回答时，可以选前端、Java/Go/C++ 后端或 AI 应用开发模拟面试。AI 会根据你的回答逐轮追问，结束后给出反馈。

| 你想练什么 | Skill | 你会得到什么 |
| --- | --- | --- |
| 提前准备简历里可能被问到的内容 | [简历批量出题](#简历批量出题) | 按简历条目组织的题单，可附简短参考回答 |
| 浏览器前端、React 或 Vue 面试 | [前端模拟面试](#前端模拟面试) | 项目与技术追问、可选编码题、面试反馈 |
| Java、Go、C++ 后端面试 | [后端模拟面试](#后端模拟面试) | 项目与技术追问、面试反馈 |
| Agent、RAG、MCP 等 AI 应用开发面试 | [AI 应用开发模拟面试](#ai-应用开发模拟面试) | 项目与技术追问、可选实操题、面试反馈 |

## 安装

把下面这段话发给支持 Agent Skills、能读取 GitHub 仓库并写入 skill 目录的 AI 工具。

```text
请从 https://github.com/Hazenix/interview-prep-skills 安装以下四个 skill：
- skills/resume-interview-question-generator/
- skills/frontend-interview-simulator/
- skills/backend-interview-simulator/
- skills/ai-dev-interview-simulator/

按当前工具的安装规则保留每个 skill 的完整目录，安装后列出可用的 skill 名称。
```

只想安装其中一个时，保留对应的目录即可。如果安装后找不到 skill，请让 AI 检查安装位置和 `SKILL.md`，再按当前工具的规则重新加载或开启新会话。

装好后，选下面任意一个 skill 的示例发给 AI。可以先用示例里的虚构经历试跑，再换成自己的简历条目。

## 简历批量出题

[`resume-interview-question-generator`](skills/resume-interview-question-generator/SKILL.md)

AI 从面试官视角为你选定的简历条目出题。贴项目、实习经历或专业技能都可以，不限技术栈。

例如，你的简历写了「负责订单异步处理链路，用消息队列削峰并优化重试」，题单里可能有：

- **主问题**：你改了重试机制的哪一部分？原来的机制遇到了什么问题？
  - **追问**：哪些错误适合重试？如果重试导致同一订单被消费两次，你怎么避免重复处理？

[查看 Markdown 题单示例](docs/examples.md#简历批量出题)

- 出题时只看面试官可见的简历条目。项目/实习题不受 JD 影响；专业技能题以简历为主，可少量加入 JD 强调但简历未写的技术问题，并标明来源。
- 先保存纯问题稿，再根据候选人的选择读取项目代码、文档等材料补充回答；材料中的隐藏细节不会反向变成面试题。
- 可选择“只要问题”或“问题和简短参考回答”；缺少依据的项目细节标为“待补充”。
- 按简历条目分组，主问题下列出可能的追问；默认在调用时当前工作目录的 `./resume/` 新建 UTF-8 Markdown 文档，不覆盖旧文件。

安装后可以说：

```text
用 resume-interview-question-generator 根据以下简历条目生成主问题和追问，只要问题。
简历条目：负责订单异步处理链路，用消息队列削峰并优化重试机制。
```

需要回答时可以直接说“问题和参考回答一起生成”，并提供项目代码、文档或补充说明。

分享简历或项目材料前，建议移除联系方式、客户数据和内部链接。

## 三个模拟面试 skill 的核心特性

前端、后端和 AI 应用开发各有自己的题库，模拟面试流程共享这些能力：

- **多身份模拟**。覆盖日常实习、暑期实习、校招和社招 1–3 年。题目难度和追问深度随候选人阶段调整。
- **六种面试官风格**。可选严厉拷打、温和鼓励、专业高效、深挖学术、工程实践和综合平衡。
- **技术题库与深度追问**。一轮只问一题，沿着你的回答追问实现原理、边界条件、选型取舍和验证方法。
- **简历与 JD 定制**。可用自己的项目经历和目标岗位要求，定制项目深挖与技术问题。
- **可选编码与实操**。按方向加入编程题或设计题，例如前端交互、后端并发或 RAG 实现。
- **实时状态跟踪与两种纠错模式**。记录已考察主题和待追问内容。可选严格模式模拟面试压力，也可选择即时引导，在答错时获得提示。
- **分维度评估反馈**。面试结束后，结合本场回答给出评分和下一步练习建议。

> **候选人**：商品更新后，我先写数据库，再删 Redis 缓存。
>
> **面试官**：如果一次读请求先查到旧值，却在删缓存之后才回填，会发生什么？

这段模拟面试从简历里的 Redis 缓存经历开始。[查看完整示例](docs/examples.md#后端模拟面试)

## 前端模拟面试

[`frontend-interview-simulator`](skills/frontend-interview-simulator/SKILL.md)

- 覆盖 HTML/CSS、JavaScript/TypeScript、浏览器、网络、安全、可访问性、性能与工程化。
- 根据用户要求、简历和 JD 决定是否考 React 或 Vue；没有相关线索时直接考通用前端。
- 编码题可用 JavaScript 或 TypeScript。支持暂停、恢复和提前结束。
- [前端知识库与评分规则](skills/frontend-interview-simulator/references/)按阶段加载。

安装后可以说：

```text
用 frontend-interview-simulator 开始一场前端校招模拟面试。我做过 Vue 项目，想重点练项目深挖。
```

## 后端模拟面试

[`backend-interview-simulator`](skills/backend-interview-simulator/SKILL.md)

- 支持 Java、Go、C++ 单语言面试，也可设置主语言和次语言进行混合面试。
- 题库覆盖并发、JVM、MySQL、Redis、Spring 和分布式系统等方向。可根据简历中的经历考察 AI 辅助开发。
- 支持暂停、恢复和提前结束。
- 技术知识库、面试官风格和评分规则放在该 skill 的 [references/](skills/backend-interview-simulator/references/) 中，按需加载。

安装后可以说：

```text
用 backend-interview-simulator 开始一场 Java 后端校招模拟面试。
```

面试中可以说“继续”“跳过”“结束”“换个风格”或“反馈”。

## AI 应用开发模拟面试

[`ai-dev-interview-simulator`](skills/ai-dev-interview-simulator/SKILL.md)

- 考察 LLM、Agent、RAG、MCP、Embedding、向量数据库及 AI 编程工具。
- 可围绕检索、重排与评估等项目细节追问，并加入 Prompt 设计、Agent 流程设计或 RAG 实现题。

安装后可以说：

```text
用 ai-dev-interview-simulator 开始一场模拟面试。我想练习 Agent 和 RAG 项目深挖。
```

## 项目结构

```text
.
├── docs/
│   └── examples.md                            # 四个 skill 的输入与输出示例
├── skills/
│   ├── ai-dev-interview-simulator/
│   │   ├── SKILL.md                           # AI 应用开发模拟面试
│   │   └── references/                        # AI 应用开发知识库与规则
│   ├── backend-interview-simulator/
│   │   ├── SKILL.md                           # 逐轮模拟面试
│   │   └── references/                        # 模拟面试所需的知识库与规则
│   ├── frontend-interview-simulator/
│   │   ├── SKILL.md                           # 逐轮前端模拟面试
│   │   └── references/                        # 前端考察点、编码题与评分规则
│   └── resume-interview-question-generator/
│       └── SKILL.md                           # 简历批量出题
├── README.md
└── LICENSE
```

## 贡献指南

欢迎补充你在面试中遇到的典型追问、改进反馈，或报告某个 skill 没有按预期运行。提交时可以带一段脱敏的输入和输出，方便复现。[贡献指南](CONTRIBUTING.md) · [提交 Issue](https://github.com/Hazenix/interview-prep-skills/issues/new)

如果这些 skill 帮你准备过一轮面试，欢迎点个 Star。

## 许可证与致谢

本项目采用 [MIT License](LICENSE)。技术知识库部分引用了 [JavaGuide](https://github.com/Snailclimb/JavaGuide) 的高频面试题整理，仅作为面试考察点使用，不改变其原有许可。感谢 JavaGuide 和 [xiaolincoding](https://xiaolincoding.com/) 提供的公开资料。

AI 应用开发模拟面试 skill 来自 [Hazenix/ai-dev-interview-simulator](https://github.com/Hazenix/ai-dev-interview-simulator/tree/13010073f1473fa393752a5aee675c9ff764ce51)，适用相同的 MIT 许可证。

前端模拟面试的设计参考了 [Witcher-xiang/frontend-interview-skill](https://github.com/Witcher-xiang/frontend-interview-skill) 的技术覆盖方向；本仓库的面试流程与题库独立编写。
