<div align="center">

![标题图片](assets/pic/Title_Image(Second_Edition)_Compressed_version.jpg)

# 🌟 Stella

**一个依托记忆系统进行拟人化聊天的 QQ 群聊机器人**

*——为 8K 上下文窗口而设计，可以同时兼容本地小模型与在线 API*

[![CI](https://github.com/Eternal-Wanderer-Vegetable/Stella_project/actions/workflows/ci.yml/badge.svg)](https://github.com/Eternal-Wanderer-Vegetable/Stella_project/actions/workflows/ci.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NoneBot2](https://img.shields.io/badge/NoneBot-2-ea5252)](https://nonebot.dev/)
[![OneBot V11](https://img.shields.io/badge/OneBot-V11-black)](https://onebot.dev/)
[![Rust](https://img.shields.io/badge/Rust-1.88%2B-dea584?logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Tauri](https://img.shields.io/badge/Tauri-2-24C8DB?logo=tauri&logoColor=white)](https://tauri.app/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](docs/deployment-docker.md)

中文 | [English](README.en.md)

</div>

---

Stella 不只是把消息丢给大模型换一句回复。它把群聊里零散的信息**沉淀成可检索、可验证、会遗忘的记忆**，并在合适的时机主动开口了解你。

Stella 的设计前提是上下文窗口很小 —— 基准上限是 **8192 tokens**。人格、记忆、历史对话、工具结果要在这么小的预算里共存，靠堆 prompt 是不可能的。所以这个预算被拆开了：记忆在库里筛完才注入，工具在聊天上下文之外执行、只交回一句结论，滚出窗口的对话自动压缩成回顾。**插件装再多，占的也不是对话窗口。** 小窗口能跑，大窗口自然更宽裕；但反过来不成立——假设窗口无限的架构，换到 8K 上会直接失控。

模型从哪里来由你定。
- **全本地**：聊天用 GPU 上的模型，记忆整理用 CPU 上的小模型，互不抢占资源，没有任何一条群聊内容离开你的机器。
- **全在线**：填一个 OpenAI 兼容的 API 就能跑，不需要显卡。
- **混合**：把对话生成交给在线模型，记忆整合、会话压缩这类高频低难度的活留在本地，只有需要强推理的那一步出网。

> 注：选择全本地部署运行的模式时，数据不出网是彻底的。需要联网的工具（查天气、查番剧）由插件自己发送请求和返回实际的数据，而判断该不该用工具、把结果压缩成摘要、把插件卡片渲染成图片，全部在本地完成。

## ✨ 特性

### 在 **8192tokens** 的上下文预算里工作

- **🧰 工具能力与人格解耦** —— Router 先判断这句话需要什么能力，工具在**聊天上下文之外**执行，只把压缩后的一句结论交回给 Stella。工具描述与原始返回都不进人格 prompt，插件装再多也挤不掉对话窗口

- **🗜 长对话不断线** —— 滚出上下文窗口的早期对话自动压缩成回顾，三层上下文（会话摘要 / 原始尾巴 / 话题摘要）按消息 id 划分绝不重叠，且各自的预算分开可调

- **🎯 记忆分区注入** —— 聊天素材与行为约束严格分离，敏感信息（边界、忌口、冲突）永不作为聊天话题被提起。只注入筛过的那几条，不把全部记忆倒进 prompt

- **🧠 两层记忆过滤** —— 捕获宽松（允许不确定信息进入候选），晋升严格（置信度分档 + 交叉验证 + 每用户配额）。过滤发生在有数据、可审计、可回滚的那一层，而不是 prompt 里——在库里筛完才花窗口，候选与置信度不占对话预算

- **🔄 模型可替换** —— 对话、能力路由、插件借用、会话压缩、记忆整合、记忆提取、图片转述七个角色各自指定用哪个端点，本地与在线任意搭配；向量检索固定在本机。换模型不动记忆，换模式也不用重建库

- **🖼 能看图** —— 可选的图片转述角色：被 @ 的消息里带图片时，先用视觉模型把图翻译成一句文字描述再进对话。消费级本地模型大多没有可用的图像转述能力，因此**默认关闭**，绑一个确认可用的视觉端点（本地多模态或在线视觉模型）即点亮；没绑定时行为与不支持识图的旧版完全一致

- **💰 花了多少钱是可见的** —— 在线 token 用量按角色/端点/模型记日账，GUI 与 `deploy status` 里能看到今日用量、**厂商前缀缓存的命中率**（验证省钱手段真的生效的唯一手段）与预算余量；可设每日预算，撞破后默认只暂停记忆整理，**群里照常能说话**

### 记忆系统

- **🔍 记忆需要证据** —— 同一件事被反复提到才会累积置信度；用户直接对 Bot 说的话视为高密度证据，单次即可采信；长期无新证据的候选自动淘汰

- **💬 主动获取信息** —— 群聊被动摄入的信息密度极低，因此 Stella 会主动 @ 活跃用户搭话或确认记忆。有每日配额、用户级冷却与「连续无回应即退避」保护

- **🎭 表达跟着群体进化（默认关）** —— 社交学习闭环：从投递回执与回复效果里沉淀「哪句表达值得复用」与「群体黑话是什么意思」，先影子模式只记录不干预，转正后经预算受控的槽位注入，效果再回流修正。默认关闭，灰度开启（`SOCIAL_ENABLED` / `SOCIAL_MODE`，见[配置文档](docs/reference/configuration.md)）

- **🏠 多群共享空间** —— 多个 QQ 群可归入同一空间，共享用户画像、长期记忆与人格；而消息尾巴、话题状态、静音开关仍按群隔离，不会在 A 群回应 B 群的对话

- **🔎 混合检索** —— SQLite FTS5 全文索引 + 多维加权排序，可选接入本地 embedding 语义检索，服务不可用时自动降级

- **♻️ 会遗忘** —— 按记忆类型设定生命周期，低价值记忆自动归档，长记忆拆分为原子事实

### 工程

- **🔗 兼容 AstrBot 插件** —— 现成的 AstrBot 插件放进 `data/plugins/` 就能跑，不改源码。插件的卡片模板由**本地 Chromium** 出图，不依赖外部渲染服务

- **🔌 可扩展** —— Pipeline 前后置 Hook 机制，扩展目录自动加载

- **🧪 可验证** —— 单元与集成测试覆盖记忆晋升、跨用户隔离、两层归属、防编造护栏、路由降级与工具隔离；接在线端点后还多一层**厂商中立契约测试**（请求体多带一个字段就红、参数差异只许按错误措辞自适应而不许写厂商白名单）与前缀缓存守卫；另有探针脚本对真实模型做回归验证（含一个专门复现「噪音环境下漏掉信息」的用例），以及一份量化四类路由错误的基准

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
