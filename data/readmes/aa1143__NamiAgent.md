<div align="center">

<img src="assets/logo.png" alt="NamiAgent logo" width="120">

# NamiAgent

**零基础入门 AI Agent 的基础教程**<br>
不只是教程，也是一个能在本地跑起来的 Agent，自带网页端，每一步都看得见

[![test](https://github.com/aa1143/NamiAgent/actions/workflows/test.yml/badge.svg)](https://github.com/aa1143/NamiAgent/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Code License](https://img.shields.io/badge/Code-MIT-green)](LICENSE)
[![Docs License](https://img.shields.io/badge/Docs-CC%20BY--NC%204.0-lightgrey)](LICENSE-docs)
[![教程](https://img.shields.io/badge/%E5%9B%BE%E6%96%87%E6%95%99%E7%A8%8B-namiai.tech-FFD84D)](https://namiai.tech/agent/)
[![GitHub stars](https://img.shields.io/github/stars/aa1143/NamiAgent?style=social)](https://github.com/aa1143/NamiAgent/stargazers)
[![X](https://img.shields.io/badge/@antiAIvo-000000?logo=x&logoColor=white)](https://x.com/antiAIvo)

[图文教程](https://namiai.tech/agent/) · [快速开始](#快速开始) · [在线可视化](https://namiai.tech/matrix/agent/) · [作者 𝕏](https://x.com/antiAIvo)

<table>
<tr>
<td width="50%"><img src="assets/web-hello.gif" alt="NamiAgent 网页端：写 hello.py 并运行。左边是每一步的思考和工具调用，右边是这一次发给模型的完整上下文" width="100%"></td>
<td width="50%"><img src="assets/web-memory.gif" alt="新会话里说一句你好，我是纳米：长期记忆在 system 里，模型的思考过程里能看到它用上了这条记忆" width="100%"></td>
</tr>
<tr>
<td align="center"><sub>写 hello.py 并运行：写文件、跑命令前弹窗确认</sub></td>
<td align="center"><sub>长期记忆：新会话里它还记得你是谁</sub></td>
</tr>
</table>

</div>

Agent 没有什么神秘的，核心就是一个 while 循环：调模型、执行工具、把结果写回上下文，再调模型。

**它是教程**：从 100 行的最小循环开始，一课加一个能力：工具、权限、上下文管理、Skills、MCP、子 Agent、计划、记忆。最后拆解 Claude Code、Codex 等主流 Agent 是怎么做的。内容是我自己一步步学习、动手实践后整理出来的。

**它也是一个能用的本地 Agent**：在你指定的工作区里读写文件、执行命令、接入 MCP、记住你是谁；写文件、跑命令前都会先问你。`python web/app.py` 打开网页端，左边看它每一步怎么想、调了什么工具，右边看每次发给模型的完整上下文。

- **每课一个可运行的快照**：`lessons/lesson-01` 到 `lesson-11`，每个目录都是学完这一课时的完整代码，可以直接运行，也可以对比相邻两课的差异
- **不绑定厂商**：使用 OpenAI 兼容接口，默认用 DeepSeek，换模型只需要改两个环境变量
- **测试不花钱**：第 3 课起每课都有测试，第 11 课共 49 个，用假模型跑，不需要 API Key
- **只依赖 `openai` 一个包**：没有任何 Agent 框架
- **本地网页端**：在浏览器里看每一步，上下文怎么变长、模型怎么想、调了什么工具，一目了然（[见下文](#网页端在浏览器里看-agent-的每一步)）

> 先学 [NamiGPT](https://github.com/aa1143/NamiGPT) 搞懂模型本身，再学 NamiAgent 搞懂模型外面那一圈。

## 课程目录

### 第一部分：手写核心

| 课 | 文章 | 代码 | 这一课新增 |
|---|---|---|---|
| 01 | [最小循环](docs/01-minimal-loop.md) | [lesson-01](lessons/lesson-01/) | `agent.py`：三个工具 + 一个 while 循环 |
| 02 | [工具系统](docs/02-tools.md) | [lesson-02](lessons/lesson-02/) | `tools.py`：注册表、统一执行器 |
| 03 | [权限](docs/03-permissions.md) | [lesson-03](lessons/lesson-03/) | `permissions.py`：硬规则 → 风险分级 → 人工确认 |
| 04 | [上下文管理](docs/04-context.md) | [lesson-04](lessons/lesson-04/) | `context.py`：截断 → 清理 → 摘要，会话持久化 |
| 05 | [Skills](docs/05-skills.md) | [lesson-05](lessons/lesson-05/) | `skills.py`：AGENTS.md 常驻，技能按需加载 |
| 06 | [接入聊天软件](docs/06-chat-apps.md) | [lesson-06](lessons/lesson-06/) | `telegram.py`、`bot.py`：常驻、聊天确认、白名单 |
| 07 | [定时任务与心跳](docs/07-scheduler-heartbeat.md) | [lesson-07](lessons/lesson-07/) | `scheduler.py`：无人值守的预授权、心跳 |

### 第二部分：补上主流能力

| 课 | 文章 | 代码 | 这一课新增 |
|---|---|---|---|
| 08 | [MCP](docs/08-mcp.md) | [lesson-08](lessons/lesson-08/) | `mcp_client.py`：stdio MCP 客户端 |
| 09 | [子 Agent 与多 Agent](docs/09-subagents.md) | [lesson-09](lessons/lesson-09/) | `subagent.py`：独立上下文，并行只读 |
| 10 | [计划](docs/10-planning.md) | [lesson-10](lessons/lesson-10/) | `planning.py`：待办清单、由代码强制只读的计划模式 |
| 11 | [记忆](docs/11-memory.md) | [lesson-11](lessons/lesson-11/) | `memory.py`：长期记忆（每条确认）、会话检索 |

### 第三部分：拆解主流 Agent（只有文章，没有新代码）

| 课 | 文章 |
|---|---|
| 12 | [拆解 Claude Code](docs/12-claude-code.md) |
| 13 | [拆解 Codex](docs/13-codex.md) |
| 14 | [拆解 Pi](docs/14-pi.md) |
| 15 | [拆解 Grok Bot](docs/15-grok-bot.md) |
| 16 | [拆解 DeepSeek Harness](docs/16-deepseek-harness.md) |
| 17 | [拆解 OpenClaw 与 Hermes](docs/17-openclaw-hermes.md) |
| 18 | [总对照表](docs/18-comparison.md) |

> 第三部分写的是截至 2026 年 10 月的情况。这些产品更新很快，细节请以各自官方文档为准。

## 配套可视化

[Agent 是怎么工作的](https://namiai.tech/matrix/agent/)：10 章逐格播放，看上下文每转一圈怎么变长、在哪里出问题，以及各种 Agent 技巧到底在上下文里做了什么。下面是其中第 3 章，配合第 1 课看效果最好：

<p align="center"><img src="assets/agent-loop.gif" alt="逐格播放 Agent Loop：左边是代码跑到哪一行，右边是此刻的上下文" width="100%"></p>

## 快速开始

需要 Python 3.10+。

```bash
git clone https://github.com/aa1143/NamiAgent.git
cd NamiAgent
pip install -r requirements.txt

export API_KEY=你的模型密钥
# 默认用 DeepSeek；换其他 OpenAI 兼容模型：
# export BASE_URL=https://...   MODEL=模型名

export NAMI_WORKSPACE=~/agent-workspace   # 第 3 课起，Agent 只能操作这个目录
mkdir -p $NAMI_WORKSPACE

cd lessons/lesson-05
python agent.py
```

跑测试（不需要 API Key）：

```bash
cd lessons/lesson-11 && pytest -q
```

## 网页端：在浏览器里看 Agent 的每一步

页首的两张动图就是网页端的真实运行录屏。

```bash
python web/app.py --demo    # 演示模式：脚本化的假模型，不需要 API Key，先看看效果
python web/app.py           # 用真实模型，和命令行版一样读 API_KEY / BASE_URL / MODEL
```

macOS 也可以直接双击 `web/start.command`：自动建虚拟环境、装依赖、让你粘贴 API Key（直接回车就是演示模式），然后打开浏览器。Agent 的工作区默认是 `~/agent-workspace`。

然后打开 http://localhost:8765 ：

- **左边**：每一次调用模型、模型的思考过程、调用了什么工具、工具返回了什么
- **右边**：这一次发给模型的完整上下文。每一块是谁写的、大概占多少 token，转一圈就长一截
- **权限确认**：写文件、跑命令这类有副作用的操作会弹窗，要你点头才执行（第 3 课的规则）
- 开头写 `/plan ` 让它先出计划，批准后再动手（第 10 课）

网页端直接导入 `lessons/lesson-11` 的 Agent，**没有改课程代码**，只换了三个接口：模型客户端（把每次发出去的上下文推给浏览器）、`handle_call`（把工具调用推给浏览器）、权限确认的 `ask`（终端 `input()` 换成弹窗）。只用 Python 标准库，不需要装 Web 框架。

DeepSeek 默认开启思考模式，模型返回的思考过程（`reasoning_content`）会单独显示。带工具调用时，这段思考要原样放回上下文再发给 API，右边的上下文面板里也能看到它。界面里展示的思考只是模型写出来的文字，不等于模型内部真实的计算过程。

## 环境变量

| 变量 | 作用 | 默认值 |
|---|---|---|
| `API_KEY` | 模型密钥 | 必填 |
| `BASE_URL` | OpenAI 兼容接口地址 | `https://api.deepseek.com` |
| `MODEL` | 模型名 | `deepseek-flash` |
| `NAMI_WORKSPACE` | Agent 的工作区（第 3 课起） | 启动时所在的目录 |
| `NAMI_STATE_DIR` | 会话记录、定时任务等状态（第 4 课起），放在工作区之外 | `~/.nami-agent` |

第 6 课起的 `bot.py` 还需要 `TG_BOT_TOKEN` 和 `TG_ALLOWED_USERS`，见第 6 课。第 8 课起可以接入 MCP 服务器，配置放在 `~/.nami-agent/mcp.json`，格式见第 8 课。

## 安全提醒

这是教学代码，Agent 会真的执行命令、读写文件。第 3 课的权限机制能挡住误操作和低成本的越界，**挡不住有意的攻击**（第 3 课第八节专门讲了它防不住什么）。

请在专门的工作区目录里运行，不要把工作区指向你的主目录。

## 这个仓库不是什么

NamiAgent 是一个**看得懂的最小 Agent**，不是生产级框架，也不打算和 Claude Code、Codex 比功能。目标是让你读完之后，再看任何 Agent 产品，都知道它在上下文里做了什么。

## 相关

- [NamiGPT](https://github.com/aa1143/NamiGPT)：从零手写 GPT-2
- [图解大模型](https://namiai.tech/matrix/)：推理、训练、Agent 三部分逐格可视化
- [从零手写 Agent 图文版](https://namiai.tech/agent/)

## License

代码采用 [MIT](LICENSE)，`docs/` 下的文章采用 [CC BY-NC 4.0](LICENSE-docs)。
