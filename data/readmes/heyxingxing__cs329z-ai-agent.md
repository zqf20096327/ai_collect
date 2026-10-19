# 🧠 cs329z-ai-agent

**把 Agent 拆开看清楚，再用实验把它改好。**

[![CI](https://github.com/xingxing-dev/cs329z-ai-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/xingxing-dev/cs329z-ai-agent/actions/workflows/ci.yml)
![Status: Experimental](https://img.shields.io/badge/status-experimental-orange)
![Python 3.11–3.13](https://img.shields.io/badge/python-3.11%E2%80%933.13-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

这是一个围绕 [Stanford CS329Z · Engineering AI Agents](https://cs329z.stanford.edu/) 主题展开的个人自学项目。我们把模型接口、检索、工具、记忆、Agent 循环和评测写成一套可以阅读、组合、运行的小型组件库 `agentkit`，再通过真实任务的执行轨迹，寻找长程 Agent 为什么会成功、卡住或过早结束。

如果你也想弄明白「工具结果怎样回到模型」「记忆到底有没有用上」「代码已经写好了，Agent 为什么还不停」，欢迎从这里一起动手。

> 🌱 当前是 **v0.1 实验版**。核心组件已有实现，长程可靠性仍在迭代。这里的讲义、练习和学习路线是个人整理，项目与 Stanford 无隶属关系，也不是官方课程仓库或官方作业答案。课程安排请以课程网站为准。

## 🚀 先跑起来：不需要 API key

准备好 Git、[uv](https://docs.astral.sh/uv/getting-started/installation/) 和 Python 3.12。仓库固定使用 3.12 开发；包声明支持 3.11–3.13。下列命令面向 macOS / Linux，Windows 建议使用 WSL。

```bash
git clone https://github.com/xingxing-dev/cs329z-ai-agent.git
cd cs329z-ai-agent
uv python install 3.12
uv sync --locked --extra rag --extra tools

# 假模型 + 本地语料：检索 → 工具 → Agent → 评分 → trace
uv run --no-sync python examples/quickstart.py --dry-run

# 看刚才发生了什么
uv run --no-sync agentkit traces
```

成功时会看到四个任务的 `PASS` 和 `mean score = 1.00`，报告写入 `runs/evals/`，调用轨迹写入 `runs/traces/`。离线示例使用脚本化模型验证接线，**不代表真实模型的准确率**；首次安装依赖需要网络，示例本身不调用模型服务。

想检查代码也很简单：

```bash
uv run --no-sync ruff check .
uv run --no-sync pytest tests --ignore=tests/live
```

`rag` 和 `tools` 是可选依赖；上面的安装方式同时覆盖分词和本地 MCP 测试。只想阅读核心组件，也可以使用 `uv sync --locked`。

### 接入自己的模型

先复制配置模板，然后用编辑器填写你有权限使用的模型、端点和密钥：

```bash
cp .env.example .env
```

常用配置是 `AGENTKIT_DEFAULT_MODEL`、对应厂商的 API key，以及检索所需的 `AGENTKIT_EMBEDDING_MODEL`。聊天与 embedding 可以使用不同服务；具体示例在 [.env.example](.env.example)。

```bash
# 读取 .env，运行真实模型示例；这一步会产生 API 费用
uv run --no-sync python examples/quickstart.py
```

`.env` 和 `runs/` 已加入 Git 忽略规则。分享 trace 前请检查其中的提示词、文件内容和工具输出。模型名称、可用权限和计费会变化，先从少量任务开始比较合适。

## 🧩 这里有哪些积木？

| 想研究什么 | 从哪里开始 | 已有实现 |
| --- | --- | --- |
| 模型如何接进系统 | [`agentkit/llm/`](agentkit/llm/) | 统一接口、重试、结构化输出、token 估算与上下文裁剪 |
| 工具怎样设计和执行 | [`agentkit/tools/`](agentkit/tools/) | 函数转 schema、参数检查、错误回填、子进程、MCP stdio |
| Agent 怎样决定下一步 | [`agentkit/agents/`](agentkit/agents/) | ReAct、Plan-and-Execute、Reflection、组合工作流 |
| 如何记住和找回信息 | [`agentkit/memory/`](agentkit/memory/) · [`agentkit/rag/`](agentkit/rag/) | 文件/摘要/向量记忆，分块、embedding 缓存、BM25 与混合检索 |
| 多个 Agent 怎样合作 | [`agentkit/multiagent/`](agentkit/multiagent/) | Worker 工具化、Handoff、Orchestrator |
| 怎样知道结果好不好 | [`agentkit/evals/`](agentkit/evals/) | 任务与评分器、代码验收、LLM Judge、重复采样指标 |
| 怎样从运行中改进 | [`agentkit/tracing/`](agentkit/tracing/) · [`agentkit/data/`](agentkit/data/) · [`agentkit/optimize/`](agentkit/optimize/) | 调用轨迹、样本提取、数据筛选、示例与 Prompt 优化 |
| 怎样约束工具使用 | [`agentkit/safety/`](agentkit/safety/) | 权限策略、工具输出检查、规则/模型注入检测 |

各组件可以单独阅读和测试，**不会因为存在于目录中就自动参与某次 Agent 运行**。例如长程 benchmark 的默认路径是 ReAct；摘要记忆、多 Agent 和 Prompt 优化需要另行组装。架构与数据流见 [ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 🔬 用六个任务研究长程执行

[`benchmarks/long_horizon/`](benchmarks/long_horizon/) 提供四道编码题、一个退款流程和一个多文档检索任务，用来观察预算、验证、重复操作与停止行为。它是本地实验集，不是官方榜单的复现或排名。

```bash
# 不调用真实模型：参考解验证工作区、工具和评分管线
uv run --no-sync python -m benchmarks.long_horizon.run --oracle

# 配好 .env 后，从一个真实任务开始；会产生 API 费用
uv run --no-sync python -m benchmarks.long_horizon.run --tasks csv_report

# 比较另一种执行方式
uv run --no-sync python -m benchmarks.long_horizon.run --harness plan --tasks refund_queue
```

2026-09-08 的一次 `ReAct / zai/glm-5.3` 运行，给了我们一个很有用的发现：**产物正确与受控完成是两件都需要测量的事。**

| 任务 | 正式运行评分 | 最终产物检查 |
| --- | --- | --- |
| CSV 报表 | 通过 | 11/11 测试 |
| Textstats 修复 | 超时 | 12/12 测试 |
| LRU + TTL 缓存 | 超时 | 13/13 测试 |
| Markdown 目录 | 超时 | 11/11 测试 |
| ORCHID 文献检索 | 通过 | 5/5 目标与指标正确，无多报 |
| 退款请求队列 | 通过 | 12/12 正确，0 违规 |

正式预算内通过为 **3/6**。超时后的产物重新验收通过，不改变原来的运行成绩。一些编码版本在早期就已满足现有验收，后续仍持续改写，甚至引入回归——因此接下来优先改进完成判定、预算管理和任务状态，而不是只增加模型调用。

实验口径、版本差异和记录限制见 [EXPERIMENTS.md](docs/EXPERIMENTS.md)。没有发布私人原始对话或完整运行轨迹；你可以用仓库中的任务生成自己的 trace。

## 🧭 按你的兴趣逛一逛

- **第一次接触 Agent**：跑 quickstart，再顺着 [`react.py`](agentkit/agents/react.py) 看一次「模型 → 工具 → 结果」循环。
- **想设计自己的 harness**：读 [架构](docs/ARCHITECTURE.md) 和 [已知问题](docs/KNOWN_ISSUES.md)，挑一个失败模式写最小复现。
- **想系统学习**：从 [`modules/README.md`](modules/README.md) 进入 17 个主题；`notes.md` 和 `labs/` 留给自己的理解与实验。
- **想动手贡献**：看 [CONTRIBUTING.md](CONTRIBUTING.md)。一个清楚的失败案例、一次可复现的小修复，都很有帮助。
- **用 Cursor、Codex 等代码助手协作**：仓库约定放在 [AGENTS.md](AGENTS.md)，方便助手知道如何检查代码和解释实验。

```text
agentkit/                 可组合的 Python 组件库
examples/                 离线入门与真实模型示例
benchmarks/long_horizon/   六题实验、评分器和参考解
tests/                    离线测试；live/ 需要显式开启
docs/                     架构、实验记录、限制与术语
modules/                  17 个学习主题、笔记和练习
homework/ · project/      自学项目脚手架
runs/                     本机生成的报告与轨迹，不提交
```

## 🌱 首版边界与接下来的方向

目前的 Shell 执行器有工作目录和命令过滤，**没有操作系统级文件或网络隔离**，请在受控环境中运行代码生成实验。超时取消、验证状态传播、记忆更新和上下文裁剪也有已知缺口；完整清单及验收方向见 [KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md)。

我们接下来最关心三件事：让“完成”绑定验收证据，让预算与运行状态可以恢复，让上下文保留真正重要的信息。欢迎通过 [Issues](https://github.com/xingxing-dev/cs329z-ai-agent/issues) 分享复现步骤和实验结果。

## 📝 来源、AI 协作与许可

学习主题参考 CS329Z 的公开课程安排，延伸阅读见 [READINGS.md](docs/READINGS.md)。代码和文档的开发使用了 AI 助手；组件实现、单元测试、真实模型表现分别提供不同层次的证据，仍需要审查与验证。自学讲义和练习不应当作官方教材。

仓库原创代码与文档使用 [MIT License](LICENSE)。外链论文、课程资料及第三方依赖保留各自的权利与许可。
