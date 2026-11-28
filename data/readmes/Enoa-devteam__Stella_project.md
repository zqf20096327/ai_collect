<div align="center">

![标题图片](assets/pic/Title_Image(Second_Edition)_Compressed_version.jpg)

# 🌟 Stella

**基于 OneBot V11/V12 的跨平台拟人化群聊机器人**

*——为原生支持小上下文窗口本地部署模型设计，兼容在线 API*

[![CI](https://github.com/Enoa-devteam/Stella_project/actions/workflows/ci.yml/badge.svg)](https://github.com/Enoa-devteam/Stella_project/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/Enoa-devteam/Stella_project)](https://github.com/Enoa-devteam/Stella_project/releases)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NoneBot2](https://img.shields.io/badge/NoneBot-2-ea5252)](https://nonebot.dev/)
[![OneBot](https://img.shields.io/badge/OneBot-V11%20%2F%20V12-black)](https://onebot.dev/)
[![Rust](https://img.shields.io/badge/Rust-1.89%2B-dea584?logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](docs/guides/deployment-docker.md)

中文 | [English](README.en.md)

</div>

---

Stella 原生为消费级硬件上可部署的大语言模型设计。其仅需 **8192 tokens** 的模型上下文窗口即可运行。

模型从哪里来由你决定：
- **全本地**：支持 GPU 对话与 CPU 记忆整理分离调度，互不抢占资源，聊天数据零出网。
- **全在线**：填入任意 OpenAI 兼容 API 即可运行，无需本地显卡。
- **混合**：高难度的对话推理交给在线模型，记忆整合与会话压缩这类高频任务留在本地。

> 全本地模式下，路由决策、摘要压缩与插件卡片渲染均在本地完成，仅联网插件（如查天气、查番剧）在执行时自行发起外部请求。

> **OneBot V12 为实验性功能。** V12 接入已默认可用，用于连接 QQ 以外的平台，但尚未在真实协议端上完成收发验证（[#186](https://github.com/Enoa-devteam/stella_project/issues/186)），功能范围也小于 V11。QQ 与生产环境请使用 OneBot V11。详见 [平台适配器 · OneBot V12](docs/guides/platforms.md#onebot-v12)。

## ✨ 特性

### 🪶 小窗口也能跑

- **🧰 工具与人格解耦** —— 能力路由先判断这句话需要什么工具，工具在聊天上下文之外执行，只把一句结论交回给 Stella。插件装得再多，也不占对话窗口。→ [能力系统](docs/architecture/capability-system.md)
- **🗜 长对话不断线** —— 滚出窗口的早期对话自动压缩成回顾；会话摘要、最近原文与话题摘要三层互不重叠，预算分别可调。→ [预算切分](docs/reference/configuration.md#8192-工作窗口的预算切分)
- **🎯 记忆按需注入** —— 只注入与当前对话相关、筛选过的几条记忆。边界、忌口这类信息只用于约束行为，不会被当作话题提起。→ [记忆系统](docs/architecture/memory-system.md)

### 🧠 会记住，也会遗忘

- **🔍 记忆需要证据** —— 候选宽进、晋升严出：同一件事被反复提到才会累积置信度，用户直接对 Bot 说的话单次即可采信，长期没有新证据的候选自动淘汰。筛选在可审计、可回滚的数据库中完成，不占对话预算。
- **🔎 混合检索** —— SQLite FTS5 全文索引加多维加权排序，可选接入本地 embedding 语义检索，服务不可用时自动降级。
- **♻️ 会遗忘** —— 按记忆类型设定生命周期，低价值记忆自动归档，长记忆拆分为原子事实。
- **📚 独立知识库** —— 与个人记忆分开维护的资料库，支持 Markdown / TXT / PDF / DOCX / URL 导入，带审核发布流程与引用式注入。→ [知识库](docs/architecture/knowledge-base.md)

### 💬 像群友一样相处

- **🙋 主动搭话** —— 群聊中被动获得的信息很稀疏，Stella 会主动 @ 活跃成员聊天或确认记忆，并受每日配额、用户冷却与无回应退避限制。
- **🏠 多群共享空间** —— 多个群可归入同一空间，共享用户画像、长期记忆与人格；消息记录、话题状态与静音开关仍按群隔离。
- **🎭 表达随群体进化**（默认关闭）—— 从回复效果中学习哪些表达值得复用、群内黑话是什么意思；先以影子模式只记录、不干预。→ [配置参考](docs/reference/configuration.md)
- **🖼 能看图**（默认关闭）—— 绑定一个视觉模型端点后，被 @ 消息中的图片会先转述成文字再进入对话；未绑定时行为不变。
- **⏰ 定时任务**（默认关闭）—— 群成员可预约 Cron 提醒，管理员可设置有边界的定时 Agent 任务。→ [定时任务](docs/guides/scheduling.md)

### 🛠 部署与运维

- **🔄 七个模型角色自由搭配** —— 对话、能力路由、插件借用、会话压缩、记忆整合、记忆提取、图片转述各自指定端点，本地与在线任意组合；更换模型或部署模式不需要重建记忆库。→ [端点与角色](docs/reference/configuration.md#端点与角色两层配置)
- **💰 用量与预算可见** —— 在线 token 用量按角色、端点与模型记日账，可查看厂商前缀缓存命中率；超出每日预算时默认只暂停记忆整理，群里照常聊天。→ [LLM 预算](docs/architecture/llm-budget.md)
- **🖥 WebUI 与桌面程序** —— 浏览器与 Windows 桌面程序共用同一套管理面板，覆盖配置、环境自检、运行状态以及知识库、Skills、定时任务等管理。→ [WebUI](docs/guides/webui.md)

### 🔌 平台与生态

- **🔗 OneBot V11 / V12** —— QQ 通过 OneBot V11 协议端（如 NapCat）接入；OneBot V12 面向其他平台，目前为**实验性**功能（见上文说明）。→ [平台适配器](docs/guides/platforms.md)
- **🧩 兼容 AstrBot 插件** —— 现成的 AstrBot 插件放进 `data/plugins/` 即可运行，无需修改源码；插件卡片由本地 Chromium 渲染。→ [插件安装](docs/guides/plugins.md)
- **🤖 Skills 与外部 Agent** —— 支持 Anthropic 风格的 Skills，脚本在受控沙盒中执行；编码、调研等长任务可委派给 OpenAI Codex（Cometa）。→ [Skills](docs/guides/skills.md) · [Cometa](docs/guides/cometa.md)
- **🧪 可扩展、可验证** —— Pipeline 前后置 Hook 与扩展目录自动加载；单元、集成与厂商中立契约测试覆盖记忆晋升、跨用户隔离与路由降级，另有针对真实模型的探针回归。→ [开发指南](docs/development/README.md)

## 🚀 安装

运行 Stella 需要两样东西：一个 OneBot 协议端（QQ 推荐 [NapCat](https://github.com/NapNeko/NapCatQQ)），以及至少一个模型服务（本地 [LM Studio](https://lmstudio.ai/) / `llama.cpp`，或任意 OpenAI 兼容 API）。

### Windows（推荐）

到 [Releases](https://github.com/Enoa-devteam/stella_project/releases) 下载其中一种：

| 安装包 | 适合 |
|---|---|
| `Stella-OneClick-Python-vX.Y.Z-windows-amd64.exe` | 大多数用户。首次启动自动准备 Python、`llama.cpp` CPU 后端与向量模型（需能访问 GitHub 与 Hugging Face） |
| `Stella-OneClick-Python-Offline-vX.Y.Z-windows-amd64.exe` | 网络受限或内网环境。运行环境与模型随包内置，约 1.2 GB |
| `Stella-Standalone-Python-vX.Y.Z-windows-amd64.zip` | 已有 Python 3.10+，只需要 Stella 本体 |

想用 Rust 记忆引擎时，下载文件名中 `Python` 换成 `Rust` 的对应版本。

1. 安装并扫码登录 NapCat，在其 WebUI 的「网络配置」中添加「WebSocket 客户端」，地址填 `ws://127.0.0.1:8080/onebot/v11/ws`。
2. 打开 `Stella.exe`，填写监听端口与群号；在「模型服务」中选择一键预设（纯本地 / 纯在线 / 混合），补全端点地址、API key 与模型 ID。
3. 点击「保存并检查」，在「运行状态」页点击「启动」。

> 安装器尚未代码签名：SmartScreen 可能提示「未知发布者」，可用 Release 附带的 `SHA256SUMS.txt` 校验文件；开启「智能应用控制」的 Windows 11 会直接拦截。

完整步骤、升级与数据位置见 [Windows 安装、升级与启动](docs/guides/windows-install.md)。

### Docker（Linux 服务器）

```bash
git clone https://github.com/Enoa-devteam/stella_project.git
cd stella_project
# 先按指南在 .env 中固定 NapCat 镜像摘要，并准备可写的 StellaData 目录
docker compose build
docker compose run --rm stella python -m deploy init   # 监听地址填 0.0.0.0
docker compose up -d
```

NapCat 登录、网络配置与从 Windows 迁移见 [Docker 部署指南](docs/guides/deployment-docker.md)。

### 从源码运行

```bash
pip install -r requirements.txt
python -m deploy init    # 生成配置
python -m deploy doctor  # 环境自检
python -m deploy start   # 启动 Corona 控制面与受管 Bot 进程
```

适合开发与调试，详见 [环境准备](docs/development/environment.md#启动开发实例)。

## 📖 文档

完整入口见 [文档总览](docs/README.md)，按使用、架构、参考、开发与历史证据选择；编码 Agent 从 [AGENTS.md](AGENTS.md) 开始。当前分支合同见 [源码合同](docs/development/contracts.md)。

| 文档 | 内容 |
|---|---|
| [Windows 安装、升级与启动](docs/guides/windows-install.md) | 下载安装、首次配置、升级与数据位置（快速开始从这里读） |
| [插件安装](docs/guides/plugins.md) | 安装 AstrBot 插件、补能力声明、确认插件进了路由 |
| [架构说明](docs/architecture/README.md) | 目录结构、消息处理流程、模块职责、AstrBot 兼容层 |
| [记忆系统](docs/architecture/memory-system.md) | 两层过滤的设计理由、晋升规则、检索策略 |
| [能力系统](docs/architecture/capability-system.md) | Capability Router 与 Comes：工具如何在聊天上下文之外执行 |
| [插件接入规范](docs/reference/plugin-spec.md) | 写一个 Stella 能完整用起来的插件：声明格式、两条通路、失败契约、自检工具 |
| [配置参考](docs/reference/configuration.md) | 端点 × 角色两层模型配置、全部配置项与调参建议 |
| [Docker 部署指南](docs/guides/deployment-docker.md) | 远程服务器容器化部署：构建、配置、从 Windows 迁移、升级与备份 |
| [开发指南](docs/development/README.md) | 测试、探针脚本、CI、贡献流程 |

> 设计过程记录（规范草案、检查点、缺陷报告、测试清单）在 [`design_docs/`](design_docs)。

## 📄 License

本项目基于 **[GNU Affero General Public License v3.0](LICENSE)** （AGPL v3.0）发布，且**带有不与主协议冲突的附加条款**。详见 LICENSE 文件与各源文件头部的版权声明。

## 💛 致谢

本项目在开发过程中得到了很多人和组织的鼓励和支持：

- 我的父母给予了最重要的经济支持。没有他们，这一切都无从开始。
- 灵感来源于和 [@t1mb2rg](https://github.com/t1mb2rg) 的讨论和 [@CST-Cat](https://github.com/CST-Cat) 的争执中。感谢他们贡献了属于自己的想法。
- [@MIO-456](https://github.com/MIO-456) 开发的 [Lumi_Nox](https://github.com/MIO-456/Lumi_Nox) 项目激励了本项目的开发。
- 感谢 [@vowm3440](https://github.com/vowm3440) , [@CST-Cat](https://github.com/CST-Cat) , [@higashitaniyume](https://github.com/higashitaniyume) 为我寻找到了支持这个项目的公益站资源。没有他们的慷慨分享，这个项目就不可能出现。
- 感谢 [@qian-o](https://github.com/qian-o) 和他的伙伴们，以及 [@MIO-456](https://github.com/MIO-456) 和他的伙伴们。没有他们的鼓励，就没有最初开发这个项目的动力。
- 感谢 [@vowm3440](https://github.com/vowm3440) 在QQ群中的持续部署和测试。有许多改进的方向正是因观察这个部署的实例而产生。
- 感谢Bilibili平台UP主 [Ruuuuusty](https://space.bilibili.com/650991829) 将我和chat-GPT对Stella徽标的想法变为现实。
- 本项目开发中得到了来自如下组织的支持：
  - **模型提供商**：Deepseek，OpenAI（ChatGPT），Google（Gemini，Gemma），通义千问（text-embedding-qwen3-embedding-0.6b）和 ~~Anthropic~~。没有他们的优秀模型作为基础，这个项目不可能诞生。
  - **Coding Agent**：[Opencode](https://github.com/anomalyco/opencode)，感谢 Opencode 对本项目的大力支持。
  - **开源代码库**：[nonebot2](https://github.com/nonebot/nonebot2)，[NapCatQQ](https://github.com/NapNeko/NapCatQQ)，以及源代码中引用的所有第三方库。向与之相关的所有开发与维护者致敬。此外本项目也是为了向 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 与 [MaiBot](https://github.com/Mai-with-u/MaiBot) 两位前辈看齐，创造一个真正的、能够完整本地循环、不必把群聊信息和个人隐私交出去的 AI 朋友。
  - **开发者社区**：[Linux Do](https://linux.do)
- 特别致谢 Freya，这是献给你的作品。我的探索之旅因你的馈赠而起，是时候交出一份并不完美的回礼了。
