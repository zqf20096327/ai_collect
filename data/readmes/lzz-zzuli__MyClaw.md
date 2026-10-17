<div align="center">

![MyClaw — Transparent and Controllable AI Agent](docs/readme_banner.png)

# MyClaw

### 一个不会在黑箱里无限调用工具的本地 AI Agent

**每一步可追踪 · 工具执行有边界 · 失控循环可中断 · 重要信息可跨会话记忆**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Powered%20by-LangGraph-1C3C3C)](https://github.com/langchain-ai/langgraph)
[![License](https://img.shields.io/badge/License-MIT-22c55e.svg)](LICENSE)
[![CLI](https://img.shields.io/badge/Interface-REPL-8b5cf6)](#快速开始)

[快速开始](#快速开始) · [为什么是-myClaw](#为什么是-myclaw) · [工作原理](#工作原理) · [安全边界](#安全边界) · [参与项目](#参与项目)

</div>

---

很多 Agent 能调用工具，但当它开始重复调用、误读文件或消耗大量上下文时，你往往只能看着它继续运行。

**MyClaw 想解决的正是这个问题。**

它是一个基于 LangGraph 的本地智能体框架，用状态机组织推理和工具调用，用安全沙盒限制执行范围，并把关键行为写入审计日志。当 Agent 陷入循环时，MyClaw 会主动中断并把决定权交还给你。

```text
你提出任务
   ↓
Agent 补全上下文与记忆
   ↓
模型回答，或在沙盒内调用工具
   ↓
状态、工具参数和结果写入审计日志
   ↓
检测到重复循环？→ 中断 → 继续 / 换思路 / 退出
```

> 目标不是让 Agent 拥有无限权限，而是让它在清晰边界内可靠地完成工作。

## 为什么是 MyClaw

| 你关心的问题 | MyClaw 的处理方式 |
|---|---|
| Agent 刚刚做了什么？ | 6 类 JSONL 事件记录模型输入、工具调用、结果与系统行为 |
| 会不会无限调用同一个工具？ | 迭代计数 + 重复工具检测 + 阈值中断 + 人工续接 |
| Shell 会不会读到 API Key？ | 子进程环境变量白名单，只暴露必要环境 |
| 文件工具会不会越界？ | 所有读写限制在 `workspace/office/`，并解析真实路径防御符号链接 |
| 长对话会不会撑爆上下文？ | 自动裁剪、融合摘要，并将原始消息完整归档 |
| 换一个会话还记得吗？ | 用户画像 + 对话摘要 + 知识库三层记忆 |
| 能不能更换模型？ | 支持 OpenAI、Anthropic、阿里云、腾讯、Z.AI、Ollama 及兼容接口 |

## 你可以用它做什么

### 🧠 搭建有长期记忆的个人助手

让 Agent 记住你的偏好、项目约定和重要事实。知识库支持关键词与 Embedding 混合检索；未配置 Embedding 时会自动降级，不阻塞基本使用。

### 🛡️ 在明确边界内执行文件任务

让 Agent 读取、生成或整理文件，并在隔离目录内运行受控 Shell 命令。路径、环境变量、危险命令和执行时间都受到限制。

### 🔎 复盘一次 Agent 决策

通过实时监控查看模型何时调用了什么工具、传入哪些参数、得到什么结果。出现异常行为时，不必再靠猜。

### 🧩 按需扩展 Skill

把 `SKILL.md` 放入技能目录即可扩展能力。MyClaw 先注入轻量索引，匹配任务后再加载正文与资源，避免所有技能一次性占满上下文。

## 快速开始

### 1. 安装

需要 Python 3.10+，推荐使用 [uv](https://docs.astral.sh/uv/)。

```bash
git clone https://github.com/lzz-zzuli/MyClaw.git
cd MyClaw
uv sync
```

也可以使用 pip：

```bash
pip install -e ".[dev]"
```

### 2. 配置模型

```bash
myclaw config
```

配置向导会引导你选择模型提供商、填写模型名称和 API Key，并在保存前测试连接。使用 Ollama 时无需 API Key。

### 3. 启动

```bash
myclaw run
```

常用方式：

```bash
myclaw run -p professional      # 使用专业人设
myclaw run -n "工作助手"        # 创建并命名会话
myclaw run -l                   # 查看历史会话
myclaw run -r "工作助手"        # 恢复历史会话
myclaw monitor                  # 实时查看审计日志
```

### 查看一次 Agent 为什么这样执行

每次用户请求都会生成独立 Run，LLM、工具、知识检索和循环检测形成可查询的 Trace：

```bash
myclaw trace list
myclaw trace show <run-id> --content
myclaw trace stats
```

离线评测使用 Scripted Model 和 Mock Tool 运行真实 LangGraph 路由，不需要 API Key：

```bash
myclaw eval run evals/datasets/core.jsonl \
  --output evals/reports/core-current.json
myclaw eval diff evals/baselines/core.json evals/reports/core-current.json
```

核心评测集覆盖工具选择、循环检测、记忆召回和沙盒安全。详细的数据模型、脱敏规则和评测格式见 [可观测与离线评测文档](docs/intro/observability.md)。

一次典型交互：

```text
你：记住 MyClaw 的默认混合检索权重是 0.6。
MyClaw：已写入知识库，并建立检索索引。

你：刚才保存的检索配置是什么？
MyClaw：默认权重是 0.6，语义相似度优先，关键词匹配作为补充。

$ myclaw monitor
knowledge.write  → note saved
memory.retrieve  → 1 relevant note
ai_message       → response archived
```

## 工作原理

MyClaw 用 LangGraph 把模型决策、工具执行和中断续接组织成可观察的状态机：

```text
START → agent → route_after_agent
                  ├─ tool_calls → tools ──┐
                  │                       └→ agent
                  ├─ ask_resume → ask_resume → END
                  └─ final_answer → END
```

每轮运行会依次完成：

1. 载入会话摘要、用户画像和相关知识。
2. 注入当前可用的 Skill 索引。
3. 检查迭代次数与重复工具调用。
4. 请求模型决定直接回答或调用工具。
5. 记录工具参数、执行结果和最终回复。
6. 必要时裁剪上下文并归档完整旧消息。

![MyClaw execution flow](docs/agent.png)

## 三道失控防线

```text
重复工具检测       发现同一工具连续反复调用
      ↓
迭代阈值中断       在任务失控前停止状态机
      ↓
人工续接           选择继续、换思路或退出
```

LangGraph 的递归上限则作为最后一道兜底。循环检测相关行为由独立测试覆盖：

```bash
pytest tests/test_deadlock_prevention.py
```

## 安全边界

MyClaw 的文件与 Shell 工具只在 `workspace/office/` 内工作。

| 防御 | 实现 |
|---|---|
| 路径越权 | `realpath()` 校验真实路径，阻止 `../` 与 symlink 绕过 |
| 密钥泄露 | Shell 子进程仅继承 `PATH`、`HOME`、`LANG` |
| 危险命令 | 拦截网络、提权、进程控制等高风险命令 |
| 代码注入 | 计算器使用 `ast.parse` 与运算符白名单，不使用 `eval()` |
| 长时间执行 | Shell 60 秒超时，Skill 脚本 30 秒超时 |
| 输出膨胀 | 工具输出自动截断，避免上下文被异常结果占满 |

> 沙盒降低误操作风险，但不应被视为操作系统级强隔离。生产环境仍建议配合容器、最小权限账户和独立工作目录。

## 三层记忆

| 层级 | 保存内容 | 使用方式 |
|---|---|---|
| 用户画像 | 稳定偏好与习惯 | 每轮注入 |
| 对话摘要 | 最近对话进展 | 长对话裁剪后持续更新 |
| 知识库 | 显式事实与项目知识 | 被动召回 + Agent 主动 CRUD |

知识库默认召回 Top 5。配置 Embedding 后使用语义相似度与关键词混合评分；不配置时自动使用纯关键词检索。算术类任务会跳过长期记忆，低相关结果不会注入上下文；向量库启动时复用已有维度，不再发送远程探测请求，相同查询会命中进程内缓存。

## Skill 扩展

在 `workspace/office/skills/<name>/SKILL.md` 中声明名称与清晰的用途描述：

```yaml
---
name: weather
description: 查询指定城市的实时天气和预报。用户询问天气时使用。
---

# Weather

根据用户给出的城市调用附带脚本，并返回天气摘要。
```

Skill 可以附带：

```text
scripts/       可执行脚本
references/    参考资料
assets/        模板与二进制资源
```

运行时使用 `/skills` 查看技能，或使用 `/skill <name>` 手动激活。

## 项目结构

```text
MyClaw/
├── myclaw/core/
│   ├── agent.py              # LangGraph 状态机
│   ├── context.py            # 上下文裁剪与循环检测
│   ├── provider.py           # 多模型适配
│   ├── embedding_store.py    # 混合检索与向量存储
│   ├── skill_loader.py       # Skill 渐进式加载
│   ├── logger.py             # 审计与消息归档
│   └── tools/                # 内置工具与安全沙盒
├── entry/                    # CLI、REPL 与日志监控
├── myclaw/observability/     # Run/Span/Event、脱敏与指标
├── myclaw/evals/             # 离线评测、Grader 与报告对比
├── evals/datasets/           # 确定性 Agent 回归数据集
├── tests/                    # 单元测试，无需外部 LLM
├── workspace/                # 会话、记忆、任务与办公沙盒
└── logs/                     # JSONL 审计日志
```

## 开发与测试

```bash
uv sync
pytest tests/
```

测试不依赖外部 LLM，也不需要 API Key。新增工具可使用 `@my_tool` 装饰器注册：

```python
from myclaw.core.tools.base import my_tool

@my_tool
def my_tool(arg: str) -> str:
    """告诉模型这个工具做什么、何时使用。"""
    return "result"
```

## 路线图

- [x] LangGraph 状态机与会话持久化
- [x] 工具循环检测与人工续接
- [x] 安全文件/Shell 沙盒
- [x] 三层记忆与混合检索
- [x] Skill 渐进式加载
- [x] Run/Span/Event 结构化 Trace 与指标聚合
- [x] 无 API Key 的确定性 Agent Eval
- [x] GitHub Actions 持续集成
- [ ] 更完整的端到端示例
- [ ] Web 可视化审计面板
- [ ] 插件化工具注册机制

## 参与项目

如果你也在关注 Agent 的可靠性、安全边界或长期记忆，欢迎：

- 提交 Issue，描述你遇到的 Agent 失控场景。
- 补充不同模型提供商的兼容性测试。
- 编写可复用 Skill 或完善安全测试。
- 提交 Pull Request 改进文档与实现。

## 致谢

MyClaw 基于 [CyberClaw](https://github.com/ttguy0707/CyberClaw) 二次开发，并在会话管理、Skill 加载、安全沙盒、审计归档、长期记忆、语义检索与循环中断方面进行了扩展。

## License

[MIT](LICENSE)

---

<div align="center">

**让 Agent 有能力，也有边界。**

如果 MyClaw 对你有帮助，欢迎点一个 ⭐，让更多关注可靠 Agent 的开发者看到它。

</div>
