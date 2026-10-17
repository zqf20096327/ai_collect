<div align="center">

# Mini Claude Code in Python

**逐模块拆解 Coding Agent 核心机制，独立实现，逐层对比。**

[中文](./README.md) · [English](./README_EN.md)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![DeepSeek API](https://img.shields.io/badge/DeepSeek_API-low--cost_ready-4D6BFE?style=flat-square)](https://api-docs.deepseek.com/guides/anthropic_api)
[![Progress](https://img.shields.io/badge/Modules-11%2F12_complete-22C55E?style=flat-square)](./chapters/11-sub-agent.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](./LICENSE)

[开始阅读](./chapters/01-agent-loop.md) ·
[查看参考代码](./examples/) ·
[致谢](#致谢)

![Coding Agent demo](./assets/demo.gif)

</div>

---

## 这个项目做了什么

不依赖 LangChain / LangGraph 等框架，用 Python 独立实现 Coding Agent 的 11 个核心模块，每个模块配套设计分析文档：

```text
Agent Loop → Tool Use → System Prompt → CLI & Session → Streaming
→ Permissions → Context Engineering → Memory → Skills → Plan Mode → Sub-Agent
```

每个模块回答四件事：

1. **生产级 Coding Agent 为什么需要这一层**：缺少它时，长任务会在哪里失效？
2. **消息怎么流动**：模型、Harness 和工具之间的数据流。
3. **最小可运行实现**：先跑通核心路径，再理解生产级复杂度。
4. **设计决策对比**：Claude Code / Kimi Code / Codex 在这一层的架构差异。

## 模块总览

| # | 模块 | 核心机制 | 状态 |
|---|------|---------|:---:|
| 01 | [Agent Loop](./chapters/01-agent-loop.md) | 多轮对话、消息历史、thinking block 过滤 | ✅ |
| 02 | [Tool Use](./chapters/02-tools.md) | 工具调用、结果回传、两层 Agent Loop | ✅ |
| 03 | [System Prompt](./chapters/03-system-prompt.md) | 静态规则、运行时上下文、`CLAUDE.md` 项目指令 | ✅ |
| 04 | [CLI & Session](./chapters/04-cli-session.md) | async Agent、REPL 命令、会话保存与恢复 | ✅ |
| 05 | [Streaming](./chapters/05-streaming.md) | 流式输出、spinner、transient error 重试 | ✅ |
| 06 | [Permissions](./chapters/06-permissions.md) | 危险命令检测、用户确认、会话内白名单 | ✅ |
| 07 | [Context Engineering](./chapters/07-context.md) | 4 层分级压缩：截断 → Budget → 去重 → LLM 摘要 | ✅ |
| 08 | [Memory](./chapters/08-memory.md) | 文件系统记忆、`MEMORY.md` 索引、跨会话持久化 | ✅ |
| 09 | [Skills](./chapters/09-skills.md) | 技能发现、system prompt 注入、斜杠命令 | ✅ |
| 10 | [Plan Mode](./chapters/10-plan-mode.md) | 只读探索、active plan 文件、权限拦截 | ✅ |
| 11 | [Sub-Agent](./chapters/11-sub-agent.md) | 受限工具集、输出 buffer、父子上下文隔离 | ✅ |
| 12 | MCP | 外部工具服务器连接 | 计划中 |

## 项目规模

- **11,000+** 行实现代码（11 个模块，逐章独立可运行）
- **7,500+** 行设计分析文档
- **13** 个版本 tag，每个模块一个可回溯的里程碑

## 低成本运行

代码使用 Anthropic Python SDK，通过 DeepSeek 的 Anthropic 兼容接口即可运行，无需购买 Claude API。

```bash
git clone https://github.com/Xiaxia1997/mini-claude-code-python.git
cd mini-claude-code-python

python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .

export DEEPSEEK_API_KEY="your-api-key"
cd examples/chapter-11
python agent.py
```

> [!IMPORTANT]
> 代码通过环境变量读取 API Key，不要把真实密钥写进代码或 Git 历史。

## 适合谁

- 正在使用 Claude Code / Kimi Code / Cursor，想理解底层机制的开发者
- 想从零搭建 Coding Agent，不想被框架抽象淹没的人
- 准备 AI Agent 相关岗位面试，需要深入理解 Agent Loop / Tool Use / Context Engineering 的求职者

## 致谢

本项目的学习路径受到 [claude-code-from-scratch](https://github.com/Windy3f3f3f3f/claude-code-from-scratch) 启发。在实践过程中重新组织了讲解结构，并加入了独立的设计分析和跨工具对比。感谢 [@Windy3f3f3f3f](https://github.com/Windy3f3f3f3f) 及原项目贡献者的开源工作。

## License

[MIT](./LICENSE)
