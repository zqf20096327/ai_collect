<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/media/brand/hero-zh-dark.svg">
    <img src="docs/media/brand/hero-zh-light.svg" width="860" alt="Covey：在飞书里带一支编程 Agent 小队">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/ericxk/covey/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/ericxk/covey/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green.svg"></a>
  <a href="pyproject.toml"><img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-blue.svg"></a>
  <a href="https://github.com/ericxk/covey/tags"><img alt="版本" src="https://img.shields.io/github/v/tag/ericxk/covey?label=version"></a>
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="https://ericxk.github.io/covey/">在线演示</a> ·
  <a href="#文档">文档</a> ·
  <a href="README.en.md">English</a>
</p>

你在飞书私聊里说一句话，管家把活分给 Claude Code、Codex、Antigravity 这些编程 Agent，在你自己的开发机上跑。每件事一个话题、一个会话，进度和结果都在卡片上。机器人重启、模型限流都接得上，要你拍板时才来找你。适合日常在飞书里工作、手上同时跑着几个编程 Agent 的人。

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/media/demo/flow-zh-dark.gif">
    <img src="docs/media/demo/flow-zh-light.gif" width="640" alt="演示：私聊里说一句话，管家开出话题，答完一道选择题，拿到答案和产物">
  </picture>
</p>

<sub>卡片示意：由 Covey 的卡片 JSON 和演示数据画成，不是真实客户端截图，实际样子以飞书里为准。想自己点着走一遍：[在线演示](https://ericxk.github.io/covey/)，或在检出里用浏览器打开[三步演示页](docs/demo/index.html)（派到话题 → 回答一道题 → 看答案和产物）。</sub>

## 快速开始

前提：Linux 或 macOS，Python 3.10+，Node.js 和 npm（`./install` 没有 `lark-cli` 时用 npm 装它；没有 npm 时安装器会停下，告诉你去装 Node.js）；这台机器上装好并登录了 Claude Code、Codex 或 Antigravity 里的任一个；一个飞书账号（用手机扫码）。

```bash
git clone https://github.com/ericxk/covey.git && cd covey
./install        # 终端里出现二维码时，用飞书手机端扫一次
```

安装器替你建好飞书应用，补齐权限、事件和菜单，注册后台服务，然后等你在飞书私聊里发第一句话、拿到回答才结束。常用选项：

| 选项 | 做什么 |
| --- | --- |
| `--showcase` | 演示套餐：在默认之外再开话题之间的协作（开发中） |
| `--web` | 在这台机器上自托管网页工作台（要 Node 22+ 和 npm） |
| `--web-public ADDR` | 网页再开公网 HTTPS 直连，`ADDR` 是 IP 或域名（隐含 `--web`） |

没有 Claude Code 也能装：管家自动用调通的 Codex 或 Antigravity，专项照常开，见[安装 · 没有 Claude Code 时](docs/install.md#没有-claude-code-时)。全部选项和常见问题见[安装](docs/install.md)。

## 一句话派活，之后少操心

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/media/brand/workflow-zh-dark.svg">
    <img src="docs/media/brand/workflow-zh-light.svg" width="860" alt="工作流：私聊说一句话，管家开话题，话题在各自的会话里做，要你拍板时发问题卡，做完把结论带回私聊">
  </picture>
</p>

你说一句 → 管家接话分派 → 话题各自去做，长活有专项负责人跟进 → 要你拍板时发问题卡 → 结论带回私聊。

同时跑好几个 Agent 以后，卡住你的往往不是模型，而是你自己：开终端、选目录、记住哪个会话在做什么、在会话之间抄上下文，还要隔一会儿去看它停没停。Covey 把这些接过去。

- **一句话派活。** 私聊里只跟管家说话。能马上答的它直接答；要查、要改的，它开一个话题去做，话题挂在你那句话下面。每个话题是独立的会话，有自己的 Harness、模型和工作区；做完了，结论带回聊天里，前后脚做完的几个合成一张卡。
- **交出去就能走开。** 每个任务在自己的进程里跑，机器人重启、升级都不打断它。撞上限流或模型服务临时故障，自动等到能用再接着做，最久约 3 小时。要等 CI、训练出结果的话题，约好时间自己回来看，没变化就不打扰你。
- **只在要你拍板时找你。** 要你定的事出一张问题卡：点一个选项就交，没有默认答案，不回答不算同意。菜单「看板」一张卡看清谁在等你、谁停住了、谁有结果没看、谁在做。
- **长活有人负责到底。** 跨几天、要几个话题配合的事交给专项：一个负责人话题拆活、派话题、跟进、汇报。话题里的选择题先由它过一遍，专项停住了发卡问你继续、收尾还是停。话题多了，整理专项会提议“建个专项？”，你点了才建。
- **记得住你说的，也分得清是谁说的。** 你说过的长期要求、让它“记一下”的事、专项里定下的约定，合成一块记忆跟着每一轮走。每条写明管哪儿、是你说的还是它总结的；记错了，在答案卡上点「不对」。
- **换模型不用重开，换一家来复核。** 一个机器人接 Claude Code、Codex、Antigravity 和 DeepSeek Harness（dsh）；管家和专项负责人能跑在前三个里的任一个上，不绑死某一家。话题聊到一半可以换 Harness、模型或工作区，接着聊。改了代码的答案卡上点「独立复核」，换一家的模型只读地查一遍。
- **就在飞书里，也敢放进公司。** 不用另装 App：手机、电脑、网页上的飞书都能用，扫一次码就装好。机器人只服务你一个人；群要你在私聊里确认才启用，还能设成群成员只读。敏感词在请求离开本机前换成替身词（Claude 的模型）；遇到官方拒绝就停下，不硬试。

### 和别的做法不一样在哪

- **聊天遥控器**把一句话转成一次 Agent 调用，一个聊天大致就是一个会话，会话一关就断。Covey 管的是这之上的事：谁去做、做到哪、谁在等你、结果有没有送到。
- **Agent IDE 和桌面工作台**以电脑前的编辑器为家，手机和聊天是外延。Covey 不跟编辑器抢位置，你离开电脑时它替你盯着。
- **全能个人助手**管的面很宽，要装它自己的客户端。Covey 只管编程 Agent 这一件事，用的是团队已经在用的飞书。

## 卡片一览

<table>
<tr>
<td width="33%"><img src="docs/media/screenshots/02-task-card.png" width="100%" alt="任务卡：状态、输入输出、执行过程，随时补充、换配置或停止"><br><sub>任务卡：执行过程实时更新，随时补充、换配置或停止</sub></td>
<td width="33%"><img src="docs/media/screenshots/06-question-card.png" width="100%" alt="问题卡：选项是按钮，点一个就交；可以自己写，也可以不回答此题"><br><sub>问题卡：点一个选项就交，没有默认答案</sub></td>
<td width="33%"><img src="docs/media/screenshots/03-answer-card.png" width="100%" alt="答案卡：结论、产物和改动、输入输出，下面是独立复核"><br><sub>答案卡：结论、产物和改动，改了代码的可以点「独立复核」</sub></td>
</tr>
</table>

<details>
<summary>还有 5 张：停住了、换配置、看板、启动卡、脱敏</summary>

<table>
<tr>
<td width="50%"><img src="docs/media/screenshots/07-stopped-card.png" width="100%" alt="停住了的回带卡：用人话说原因和下一步，按钮是换个模型"><br><sub>停住了：说清原因和下一步，额度用完就「换个模型」</sub></td>
<td width="50%"><img src="docs/media/screenshots/08-switch-card.png" width="100%" alt="换配置卡：从 Claude Code 换到 Codex，改过的行标蓝"><br><sub>换配置：聊到一半换 Harness、模型或工作区</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/media/screenshots/09-board.png" width="100%" alt="看板：要你处理几件事，等你、停住了、有结果、专项"><br><sub>看板：要你处理几件事、先看哪件</sub></td>
<td width="50%"><img src="docs/media/screenshots/04-launch-card.png" width="100%" alt="启动卡：选模型、思考预算、脱敏、工作区和运行方式"><br><sub>启动卡：没有管家时，每个新话题先选模型和工作区</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/media/screenshots/05-settings-redaction.png" width="100%" alt="设置卡的脱敏页：填词即可，替身词自动生成"><br><sub>设置卡的「脱敏」页：填词即可，替身词自动生成</sub></td>
<td width="50%"></td>
</tr>
</table>

</details>

## 网页工作台（开源，可选）

在电脑上看长回答、翻历史时更顺手：私聊里的专项、话题、每一轮和等你回答的问题都在网页上，也能在网页上说话、答题、停话题、开新话题、改设置。它和飞书读写同一份记录，飞书照旧管提醒和快速回复。

<img src="docs/media/screenshots/10-web-board.png" width="100%" alt="网页看板：两件事要你处理，等你、停住了、在做、有结果没看，右边是专项和本周用量">

<details>
<summary>专项页、大厅、手机上</summary>

<table>
<tr>
<td width="40%"><img src="docs/media/screenshots/11-web-project.png" width="100%" alt="网页专项页：和负责人的对话，右边是记忆，标着你说的和它总结的"><br><sub>专项页：负责人的对话，记忆按“你说的 / 它总结的”分开</sub></td>
<td width="40%"><img src="docs/media/screenshots/12-web-hall.png" width="100%" alt="网页大厅：你、管家和负责人在一条时间线上"><br><sub>大厅：你、管家和各专项的负责人在一条时间线上</sub></td>
<td width="20%"><img src="docs/media/screenshots/13-web-phone.png" width="100%" alt="手机上的网页看板"><br><sub>手机上</sub></td>
</tr>
</table>

</details>

<sub>网页截图：自托管版装上演示数据后截的，不含真实数据。</sub>

网页工作台的源码就在 [`web/`](web/README.md)，两种部署：

- **一键部署到飞书的全栈应用平台**：飞书企业开通了能建全栈应用的平台时，一条命令部署到你自己的应用里，网址、加密和飞书登录都由平台提供，人在外面用手机飞书点开就能用，见 [web/README.md 的「部署」](web/README.md#部署)。
- **没有这样的平台，或想让数据只留在自己机器上**：`./install --web` 在这台机器上自托管；`./install --web-public <IP 或域名>` 再开公网 HTTPS 直连，云主机或家里有公网地址的机器都能从外面直接打开。第一次登录时，飞书私聊里点「允许」。见 [docs/install.md](docs/install.md#网页工作台可选) 和 [web/deploy/selfhost](web/deploy/selfhost/README.md)。

## 装好以后

1. **第一句话**：私聊机器人发一句话，管家直接回答，或开一个话题去做。一页纸的用法见[五分钟上手](docs/quickstart.md)，再照[使用指南 · 第一次使用](docs/usage.md#第一次使用)走一遍。
2. **默认开着的**：管家、专项、整理专项（只提议）、菜单「看板」、独立复核、到点回来看、记忆和知识条目。撤回或编辑消息后，任务跟着停或收到补充；任务在跑时在话题里发的话，直接补充给它。还能开什么、怎么开，见[配置 · 开关速查](docs/configuration.md#开关速查)；已经装好的机器人想一次打开演示套餐，见[演示套餐](docs/configuration.md#演示套餐)。
3. **升级**：在检出里跑 `scripts/upgrade.sh`（先加 `--dry-run` 看会做什么）。它取上游的新提交，照服务清单原样部署成固定的 release，机器人重启只要几秒，在跑的任务不中断，由新进程接管。不要在服务运行的检出里直接 `git pull`。见[升级与部署 · 日常升级](docs/deploy.md#日常升级)。

## 文档

**上手与使用**

| 文档 | 内容 |
| --- | --- |
| [安装](docs/install.md) | `./install` 的前提、过程、选项、网页工作台、验收、常见问题 |
| [五分钟上手](docs/quickstart.md) | 一页纸：第一句话、日常怎么用、常被问到的（看板在哪、怎么开记忆、怎么升级）；管家被问到用法时先读它 |
| [使用指南](docs/usage.md) | 第一次使用、开任务、补充、回答、换配置、任务卡、管家、看板、群聊、代答 |
| [使用参考](docs/reference.md) | 使用指南各节的细节：启动卡和设置卡各项、任务卡状态行、补充的送达状态、问题卡、答案卡、看板和汇总、代答卡、自动重试 |
| [管家](docs/butler.md) | 私聊管家是什么、一轮怎么走、开话题和回带、工具、原则、知识库、记忆、设置卡 |
| [专项](docs/projects.md) | 分几个话题、跨几天推进的事：专项卡、负责人、问题分流、整理专项 |
| [网页工作台](docs/web.md) | 怎么部署（一键部署到飞书的应用平台、本机自托管）、网页上能做什么、给前端的数据契约 |
| [代答](docs/proxy.md) | 替你回复白名单里的人：前置条件、怎么开、实现 |
| [排障](docs/troubleshooting.md) | 先找到数据根和 APP_ID，再按现象查：安装、没反应、服务、按钮、模型、任务、代答、飞书应用 |

**部署与配置**

| 文档 | 内容 |
| --- | --- |
| [配置](docs/configuration.md) | 开关速查（默认已开、推荐打开、按需打开、演示套餐）、改开关三步、`harnesses.json`、全部环境变量 |
| [Harness 说明](docs/harnesses.md) | 支持哪些 Harness、谁能当管家和负责人、安装登录、选模型、各 Harness 的参数、模型网关 |
| [运维指南](docs/operations.md) | 你是谁看哪里、服务组成、数据目录、日常操作、扩展的装和卸、日志、备份、服务托管、开机恢复 |
| [升级与部署](docs/deploy.md) | 日常升级 `scripts/upgrade.sh`、改设置后重新注册、升级与回滚、`deploy_bridge.sh` 部署新版本 |
| [飞书应用配置](docs/feishu-app.md) | 机器人应用要有的权限、事件和菜单，自动补齐和在开发者后台手动配置 |
| [手工安装](docs/manual-install.md) | 不用 `./install` 时：旧安装脚本、确定 owner、启动、首次验收 |
| [改名与兼容](docs/compat.md) | 改名 Covey 后旧导入、旧变量、旧入口和旧单元名照常可用；新旧版本混跑 |
| [已下线的功能与旧配置](docs/legacy.md) | 升级老部署时看：已下线的功能现在会怎样，哪些变量不再读 |
| [官方拒绝与停止](docs/policy-stop.md)、[本机运行锁](docs/runtime-locks.md) | 两个专门的话题 |

**开发**

| 文档 | 内容 |
| --- | --- |
| [架构与开发说明](docs/architecture.md) | 分层、任务生命周期、锁、状态、投递、扩展机制 |
| [管家的实现细节](docs/butler-internals.md) | 改管家代码时看：放置表、工具通道、各开关功能的实现 |
| [卡片与事件](docs/cards.md)、[界面规范](docs/ui.md) | 卡片、按钮、执行过程；界面用词、颜色、组件 |
| [测试与验收](docs/testing.md) | 怎么挑测试、金样、跨版本检查、卡片示意图、网页的测试、真实客户端验收 |
| [名词表](docs/glossary.md) | 管家、话题、专项等名词的中文名和英文名，界面和提示词只用表里的词 |
| [AGENTS.md](AGENTS.md)、[CONTRIBUTING.md](CONTRIBUTING.md) | 代码地图和最容易改坏的规则；怎么参与 |

## 扩展

核心不按名字引用任何一个 Harness 之外的东西。扩展是一个带清单（`manifest` 模块）的包，放在运行的代码的 `extensions/` 下（固定 release 由 `scripts/deploy_bridge.sh --ext-repo` 拼进去），通过清单把 Harness、供应商、模型网关、菜单项和钩子并进核心的表。装好后用 `python3 -B bin/covey_plugins.py list`、`enable <包>`、`disable <包>` 管，改完 `covey_service.py restart` 生效，见[扩展的装和卸](docs/operations.md#扩展的装和卸)；接口和规则见[架构](docs/architecture.md#扩展)。带扩展的安装照扩展自己的说明做。

## 参与

见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可证：[MIT](LICENSE)。
