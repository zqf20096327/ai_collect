<a id="llm-workshop"></a>

# 动手学习大模型系统

<div align="center">

[![GitHub 星标](https://img.shields.io/github/stars/tylerelyt/llm-sys-workshop.svg?style=social&label=Star)](https://github.com/tylerelyt/llm-sys-workshop)
[![GitHub 分叉](https://img.shields.io/github/forks/tylerelyt/llm-sys-workshop.svg?style=social&label=Fork)](https://github.com/tylerelyt/llm-sys-workshop)
[![许可证：MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)

**通过 8 章、41 项练习，学习大模型应用与系统的构建方法。**

[项目介绍](#项目介绍) · [配套课程](#配套课程) · [快速开始](#快速开始) · [课程目录](#课程目录) · [参与贡献](#参与贡献)

</div>

<a id="-who-should-join-this-workshop"></a>

## 项目介绍

面向具备 Python 基础的开发者，通过模型服务与会话、推理、检索、上下文、多模态、智能体、数据构建与模型适配练习，学习大模型系统的构建方法。每课提供中文讲义、代码、动手任务和验收条件，建议按“运行示例 → 修改输入或策略 → 核对结果”的顺序学习。

聊天模型通过兼容 OpenAI Chat Completions 的接口配置选择；各课注明工具调用、多模态、嵌入和重排等能力要求。

<a id="课程资源"></a>

## 配套课程

本项目可配合以下两门极客时间课程学习。

| 课程 | 学习重点 | 本仓库中的学习方向 |
| --- | --- | --- |
| [大模型系统实战](https://time.geekbang.org/column/intro/100613101) | AI 系统基础、模型原理、系统架构与工程方法 | 第 4、6、7、8 章：上下文、智能体、数据与模型适配 |
| [前沿模型实战课](https://time.geekbang.org/column/intro/100828301) | 模型能力、多轮对话与推理、检索增强、多智能体 | 第 1、2、3、6 章：对话、推理、检索与智能体 |

各章练习按主题关联课程。图像与文档处理、知识图谱、NL2SQL、MCP、CLI Skill 和 Pi 等内容作为扩展练习，纳入相关章节。

<a id="-quick-start"></a>

## 快速开始

使用 Python 3.11 或 3.12。下面以 Python 3.12 为例：

```bash
git clone https://github.com/tylerelyt/llm-sys-workshop.git
cd llm-sys-workshop
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-deepseek.lock
cp .env.example .env
```

按[模型配置说明](README-DEEPSEEK.md#setup)填写 `.env` 或导出环境变量，然后从[第 1.1 课](chapter1/lesson1/README.md)开始。各课所需的模型、额外依赖和授权步骤见对应讲义。

## 课程目录

每项练习有独立说明、运行入口和验收要求。点击章名查看概念与先修关系，点击练习进入代码与讲义。

### [第 1 章：会话智能](chapter1/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [1.1 开源大模型入门](chapter1/lesson1/README.md) | MaaS 接口、Token/NTP、Completion/Chat 与 Session |
| [1.2 构建工具调用 Agent](chapter1/lesson2/README.md) | 从地点查询到天气工具的数据传递 |
| [1.3 LLM 推理流程编排](chapter1/lesson3/README.md) | 累积上下文、交接任务与中间结果检查 |
| [1.4 基础提示方法](chapter1/lesson4/README.md) | 零样本解释与少样本分类 |

### [第 2 章：高级推理](chapter2/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [2.1 对话历史管理](chapter2/lesson1/README.md) | 最近轮次窗口与事实摘要 |
| [2.2 自一致性](chapter2/lesson2/README.md) | 多次求解与多数投票 |
| [2.3 ReAct Agent](chapter2/lesson3/README.md) | 工具动作、实际观察与答案 |
| [2.4 顺序工作流](chapter2/lesson4/README.md) | 方案生成、评估、深化与排序 |

### [第 3 章：检索与知识工程](chapter3/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [3.1 检索与重排](chapter3/lesson1/README.md) | 召回候选、重排片段与回答引用 |
| [3.2 轻量向量检索问答](chapter3/lesson2/README.md) | Chroma 索引、命中文档与有据回答 |
| [3.3 知识图谱构建](chapter3/lesson3/README.md) | 从原文抽取实体与关系并可视化 |
| [3.4 企业 NL2SQL](chapter3/lesson4/README.md) | 依据表结构生成只读查询，缺少依据时拒答 |
| [3.5 语义去重](chapter3/lesson5/README.md) | 发现重复、归档原文与维护来源映射 |
| [3.6 切块质量反馈](chapter3/lesson6/README.md) | 复核问题与片段的关系，保留人工确认依据 |
| [3.7 跨语言检索](chapter3/lesson7/README.md) | 按语种路由并比较检索命中 |
| [3.8 迭代图检索](chapter3/lesson8/README.md) | 沿关系扩展并保留证据链 |
| [3.9 检索服务接入 Harness](chapter3/lesson9/README.md) | 通过 MCP 检索，核对引用与语料版本 |

### [第 4 章：上下文工程](chapter4/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [4.1 面向缓存的提示设计](chapter4/lesson1/README.md) | 稳定提示前缀与实际缓存使用量 |
| [4.2 工具遮罩与动态行为控制](chapter4/lesson2/README.md) | 随任务状态调整可用工具 |
| [4.3 文件系统上下文与外部记忆](chapter4/lesson3/README.md) | 保存观察结果并恢复上下文 |
| [4.4 目标复述与任务管理](chapter4/lesson4/README.md) | 保持目标和待办可见 |
| [4.5 错误保留与失败学习](chapter4/lesson5/README.md) | 记录失败并比较恢复与重试策略 |

### [第 5 章：多模态与文档处理](chapter5/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [5.1 多模态图像分析](chapter5/lesson1/README.md) | 对照原图理解与 OCR 后的文字分析 |
| [5.2 文档提取与问答](chapter5/lesson2/README.md) | 按页提取原文，检查引用与证据缺口 |
| [5.3 法律文书分析](chapter5/lesson3/README.md) | 围绕一份合同回答问题并逐条核对原文 |

### [第 6 章：智能体与工具集成](chapter6/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [6.1 计算工具 Agent](chapter6/lesson1/README.md) | 让模型调用计算器，核对实际计算结果 |
| [6.2 手写函数调用](chapter6/lesson2/README.md) | 实现模型决策、函数执行与结果反馈循环 |
| [6.3 框架工具调用](chapter6/lesson3/README.md) | 用 AutoGen 管理同一个数列与统计任务 |
| [6.4 MCP 工具发现与调用](chapter6/lesson4/README.md) | 发现独立进程中的工具并核对实际结果 |
| [6.5 飞书远程 MCP](chapter6/lesson5/README.md) | 准备用户凭证，发现工具并搜索文档 |
| [6.6 CLI Skill 与扫码授权](chapter6/lesson6/README.md) | 扫码后列出文档，复用授权并封装技能脚本 |
| [6.7 Pi SDK 与技能加载](chapter6/lesson7/README.md) | 在相同文档与问题下比较加载技能前后的读取 |
| [6.8 代码转换](chapter6/lesson8/README.md) | 将 Python 转为 JavaScript 并检查行为一致性 |
| [6.9 代码解释器](chapter6/lesson9/README.md) | 生成程序并检查约束与执行结果 |
| [6.10 反思与改进](chapter6/lesson10/README.md) | 评审草稿、改写内容并保存可复用经验 |
| [6.11 持久记忆](chapter6/lesson11/README.md) | 保存角色记忆并在后续会话中加载 |

### [第 7 章：微调数据构建](chapter7/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [7.1 Few-shot 指令数据](chapter7/lesson1/README.md) | 把结构化示例转换为指令样本 |
| [7.2 Self-Instruct 数据](chapter7/lesson2/README.md) | 生成任务与实例并过滤结果 |
| [7.3 Alpaca 数据格式](chapter7/lesson3/README.md) | 转换与校验 instruction、input、output |
| [7.4 偏好数据](chapter7/lesson4/README.md) | 生成候选答案对并复核排序 |

### [第 8 章：模型适配基础](chapter8/README.md)

| 练习 | 学习内容 |
| --- | --- |
| [8.1 冻结嵌入与线性分类](chapter8/lesson1/README.md) | 训练分类器，检查指标与误分类样本 |

<a id="-contributing"></a>

## 参与贡献

欢迎通过 Pull Request 补充练习、修复代码与完善中文讲义，修改时同步更新运行命令和验收条件。遇到问题请在 [Issues](https://github.com/tylerelyt/llm-sys-workshop/issues) 附上课时、运行命令及已去除密钥的错误信息。

<a id="-contributors"></a>

### 贡献者

<a href="https://github.com/tylerelyt/llm-sys-workshop/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tylerelyt/llm-sys-workshop" alt="项目贡献者" />
</a>

<a id="-license"></a>

**许可证**

本项目采用 [MIT License](LICENSE)。
