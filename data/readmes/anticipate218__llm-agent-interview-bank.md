<div align="center">

<a href="https://anticipate218.github.io/llm-agent-interview-bank/"><img src="docs/images/banner.png" alt="大模型 &amp; Agent 面试题库" width="100%"></a>

### 2845 道原创面试题 · 每题都有讲解 · 在线刷题、错题本、模拟考试 · 开源免费

[![在线刷题](https://img.shields.io/badge/%E5%9C%A8%E7%BA%BF%E5%88%B7%E9%A2%98-%E7%82%B9%E8%BF%99%E9%87%8C%E5%BC%80%E5%A7%8B-6366f1?style=for-the-badge)](https://anticipate218.github.io/llm-agent-interview-bank/)

[![GitHub stars](https://img.shields.io/github/stars/anticipate218/llm-agent-interview-bank?style=social)](https://github.com/anticipate218/llm-agent-interview-bank/stargazers)
[![题目](https://img.shields.io/badge/%E9%A2%98%E7%9B%AE-2845-8b5cf6)](#coverage)
[![考点](https://img.shields.io/badge/%E8%80%83%E7%82%B9-861-ec4899)](docs/taxonomy.md)
[![validate](https://github.com/anticipate218/llm-agent-interview-bank/actions/workflows/validate.yml/badge.svg)](https://github.com/anticipate218/llm-agent-interview-bank/actions/workflows/validate.yml)
[![内容协议](https://img.shields.io/badge/%E5%86%85%E5%AE%B9-CC_BY--SA_4.0-lightgrey)](LICENSE-CONTENT)
[![代码协议](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-MIT-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-10b981)](CONTRIBUTING.md)

**[🚀 在线刷题](https://anticipate218.github.io/llm-agent-interview-bank/)** · **[🧭 备考路线](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks)** · **[📝 模拟考试](https://anticipate218.github.io/llm-agent-interview-bank/#/exam)** · **[📚 题库目录](docs/README.md)** · **[🤝 参与贡献](CONTRIBUTING.md)**

</div>

> [!TIP]
> 如果这个题库对你有帮助，欢迎点一个 ⭐ **Star**，让更多准备大模型、Agent 岗位实习和校招的同学看到它。

## 🎬 47 秒看懂

https://github.com/user-attachments/assets/b3d4361e-ddcd-4080-9606-dd4845673869

画面都是网站的真实操作录屏：答错时选项抖动并标出正确答案，答对时打勾、彩带飞出，多选题分别标出选错和漏选；还能按岗位一键组卷、模拟考试。

## ✨ 为什么选它

| | 常见的面经合集 | 本题库 |
|---|---|---|
| **答案与讲解** | 只有题目，或答案零散 | 每题都有讲解：客观题逐项点评，主观题给参考答案、评分要点与常见失分点 |
| **题型** | 以问答为主 | 12 种题型：选择、判断、填空、计算、代码输出 / 填空 / 改错、编程、简答、场景分析、系统设计 |
| **代码题** | 很少验证 | 全部实际运行：412 个代码任务在 CI 中自动执行，输出逐字核对 |
| **准确性** | 依赖作者个人 | 多轮质检：独立盲答复核，联网核实并注明出处，消除「选最长的」「多选选前三个」这类猜题规律 |
| **时效性** | 停在发布那一刻 | 覆盖 2025～2026 新热点：MCP 2026-07-28 无状态规范、GRPO 系列与训推不一致、Agent Skills、Harness 工程、国产 NPU 部署 |
| **练习方式** | 自己翻文档 | 在线刷题、错题本、收藏、模拟考试、学习统计；手机电脑都能用，可离线 |
| **开放程度** | 常见付费或闭源 | 开源免费，YAML / JSON / CSV 数据可二次开发 |

<a name="coverage"></a>

## 🗺️ 覆盖范围

<p align="center"><img src="docs/images/coverage.png" alt="覆盖 11 大领域、70 个小类、861 个考点" width="100%"></p>

<details>
<summary><b>题量统计与分类明细</b>（点击展开）</summary>

<!-- STATS:START -->
| 大类 | 小类数 | 题量 |
|---|---|---|
| FND 机器学习与深度学习基础 | 5 | 191 |
| LLM 大模型原理 | 9 | 356 |
| TRN 预训练与微调 | 7 | 295 |
| ALN 对齐与强化学习 | 6 | 252 |
| INF 推理与部署 | 7 | 278 |
| RAG 检索增强生成 | 7 | 245 |
| AGT 智能体 Agent | 12 | 556 |
| EVL 评测 | 2 | 91 |
| ENG 工程化与系统设计 | 4 | 160 |
| SEC 安全与可靠性 | 4 | 143 |
| CS 编程与计算机基础 | 7 | 278 |
| **合计** | **70** | **2845** |

题型分布：单选题 807，多选题 400，判断题 366，填空题 177，计算题 237，代码输出题 130，代码填空题 45，代码改错题 68，编程题 101，简答题 315，场景分析题 150，系统设计题 49。
难度分布：基础 714，进阶 1583，挑战 548。
<!-- STATS:END -->

<!-- TAXONOMY:START -->
| 大类 | 小类 |
|---|---|
| **FND** 机器学习与深度学习基础 | 数学基础 · 机器学习基础 · 深度学习基础 · 优化与训练技巧 · NLP 基础 |
| **LLM** 大模型原理 | Transformer 整体架构 · 注意力机制 · 位置编码与长上下文 · Tokenizer 与 Embedding · 混合专家 MoE · 解码与生成 · 主流模型与演进 · 多模态大模型 · 新架构与前沿 |
| **TRN** 预训练与微调 | 预训练与 Scaling Law · 数据工程 · 分布式训练 · 显存与混合精度 · 指令微调 SFT · 参数高效微调 · 领域适配与蒸馏 |
| **ALN** 对齐与强化学习 | 强化学习基础 · RLHF 与 PPO · 偏好优化 DPO 系列 · GRPO 与可验证奖励 · 奖励设计与奖励黑客 · 推理模型与测试时计算 |
| **INF** 推理与部署 | 推理流程与性能指标 · KV Cache 与显存管理 · 批处理与调度 · 算子与 FlashAttention · 量化与压缩 · 投机解码 · 推理服务与框架 |
| **RAG** 检索增强生成 | RAG 原理与选型 · 文档解析与切块 · Embedding 与向量索引 · 稀疏检索、混合检索与重排 · 查询理解与生成控制 · 高级 RAG 范式 · RAG 评测与运维 |
| **AGT** 智能体 Agent | Agent 基础与范式 · 提示工程与结构化输出 · 推理与规划 · 反思与自我改进 · 工具调用 · 智能体协议 · 记忆与上下文工程 · Agent 框架 · 多 Agent 与长程任务 · Harness 与编码 Agent 运行时 · Agent 应用 · Agentic RL 与自我进化 |
| **EVL** 评测 | 大模型评测 · Agent 评测 |
| **ENG** 工程化与系统设计 | 稳定性与容错 · 可观测性与 LLMOps · 成本与性能优化 · 系统设计 |
| **SEC** 安全与可靠性 | 提示注入与越狱 · Agent 安全 · 防御体系与治理 · 可靠性、幻觉与合规 |
| **CS** 编程与计算机基础 | Python · PyTorch · 算法与数据结构 · SQL 与数据库 · 计算机网络 · 操作系统与并发 · 分布式系统 |
<!-- TAXONOMY:END -->

每个小类下有 7～17 个考点，完整的考点清单与覆盖情况见 [docs/taxonomy.md](docs/taxonomy.md)。

</details>

## 🧭 实习与岗位备考路线

| 路线 | 内容 | 题量 | 入口 |
|---|---|---|---|
| 🌱 **实习必刷** | 高频必考（★★★）且难度为基础或进阶的题，覆盖全部方向，适合实习与校招的第一轮准备。 | 651 | [开始练习](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks?t=intern) |
| 🧠 **大模型算法岗** | 机器学习基础、Transformer 原理、预训练与微调、对齐与强化学习、大模型评测。 | 1035 | [开始练习](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks?t=algo) |
| 🤖 **Agent 应用开发岗** | Agent 范式、工具调用与协议、记忆与上下文工程、RAG、工程化、安全与 Agent 评测。 | 1099 | [开始练习](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks?t=agent) |
| ⚡ **推理与工程岗** | 推理优化与部署、分布式训练与显存、成本与性能、操作系统与分布式系统。 | 458 | [开始练习](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks?t=infra) |
| 💻 **手撕代码** | 代码输出、填空、改错与编程题，面试「手撕」环节的高频实现。 | 344 | [开始练习](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks?t=coding) |
| 🔥 **挑战题** | 难度为「挑战」的推导、多步计算、细节陷阱与复杂场景，冲刺高阶岗位。 | 548 | [开始练习](https://anticipate218.github.io/llm-agent-interview-bank/#/tracks?t=challenge) |

> 路线按岗位方向、考频与难度组织。题目均为原创，考点参考了字节跳动、阿里巴巴、腾讯、华为、美团等公司大模型与 Agent 岗位的公开面经，不是任何公司的真题。

## 📱 在线刷题

打开 **[https://anticipate218.github.io/llm-agent-interview-bank/](https://anticipate218.github.io/llm-agent-interview-bank/)** 就能开始，不用注册。

- ✅ **即时判分**：选择题点完就判，答错的题自动收进错题本；连对 5、10、20 题有里程碑庆祝
- 📝 **主观题自评**：简答、场景、设计、计算与编程题给出参考答案，对照评分要点逐条勾选，自动算分
- 🎯 **灵活练习**：按大类、小类、题型、难度筛选，顺序或随机，「只做新题」「只做错过的」，进度自动保存
- ⏱️ **模拟考试**：按岗位一键组卷，倒计时、答题卡，交卷自动判分（多选少选得一半、填空按空给分），逐题回顾
- 📊 **学习统计**：做题热力图、各领域正确率、连续打卡；数据只保存在本机浏览器，可导出备份
- 🌙 **好用的细节**：深色模式、键盘快捷键、手机滑动翻题、添加到主屏幕后离线可用

<p align="center"><a href="https://anticipate218.github.io/llm-agent-interview-bank/"><img src="docs/images/demo.gif" alt="刷题演示：答对彩带、多选标出漏选、键盘翻题" width="860"></a></p>

电脑上用 `A`–`E` 选择、`←` `→` 翻题，手机上左右滑动。

<p align="center"><img src="docs/images/practice.png" alt="电脑端刷题" width="100%"></p>
<p align="center"><img src="docs/images/mobile.png" alt="手机端：答对、答错与模拟考试" width="100%"></p>

## 📖 先试两题

**经典必考**　`LLM-ATTN-001` · 单选 · 基础 · ★★★

Scaled Dot-Product Attention 中，打分 $QK^\top$ 要除以 $\sqrt{d_k}$，最主要的目的是：

- **A.** 让注意力分布更尖锐，使每个 query 更集中地关注最相关的 token
- **B.** 防止点积随维度增大而变大，导致 Softmax 饱和、梯度过小
- **C.** 保证每一行注意力权重之和为 1，使输出成为对 V 的加权平均
- **D.** 使打分随 token 间距离增大而衰减，从而为模型注入相对位置信息

<details>
<summary><b>查看答案与解析</b></summary>

**答案：B**

**结论**：缩放是为了控制 Softmax 输入的数值范围，保持梯度健康。

设 $q$、$k$ 的各维独立、均值 0、方差 1，则点积 $q\cdot k=\sum_{i=1}^{d_k}q_ik_i$ 的方差为 $d_k$。$d_k=128$ 时标准差约 11，Softmax 会把几乎全部权重压到最大的一项上（接近 one-hot），其余位置梯度趋近于 0，训练困难。除以 $\sqrt{d_k}$ 后方差回到 1 左右。

- A 错：方向反了。除以大于 1 的 $\sqrt{d_k}$ 相当于升高 Softmax 温度，分布更平缓；缩放要防止的恰恰是分布过尖、接近 one-hot。
- C 错：权重和为 1 是 Softmax 归一化保证的，与是否缩放无关。
- D 错：$\sqrt{d_k}$ 是与位置无关的常数，对所有打分一视同仁；位置信息来自位置编码（如 RoPE，或 ALiBi 的距离偏置）。

</details>

**2026 新考点**　`AGT-PROTO-063` · 单选 · 进阶 · ★★★

MCP 2026-07-28 版移除了 `initialize` 握手和 `Mcp-Session-Id`，把协议改为无状态。某团队的远程 MCP Server 部署在负载均衡后面，共 8 个实例。对这个团队来说，这一变化最直接的好处是：

- **A.** Server 不再需要保存任何业务状态，购物车、浏览器上下文这类跨调用数据由协议自动在请求之间传递
- **B.** 取消握手后不再需要版本协商，Server 只需支持最新版本，连上来的旧版客户端会自动升级到新协议
- **C.** 每个请求自带版本与能力，任意实例都能处理任意请求，普通轮询负载均衡即可，无需粘性路由和共享会话存储
- **D.** 客户端与 Server 之间改为复用一条长连接，省去每次请求都重新做 TLS 握手和访问令牌校验的开销

<details>
<summary><b>查看答案与解析</b></summary>

**答案：C**

**结论**：无状态的核心收益是水平扩展。处理一个请求所需的协议上下文（版本、客户端能力、客户端标识）都在请求自身的 `_meta` 里，Server 不必依赖同一连接上之前的请求。

旧版中，`initialize` 协商的结果和 `Mcp-Session-Id` 通常保存在处理握手的那个实例的内存里：要么用粘性路由把同一会话的请求都送到这个实例，要么把会话状态放进共享存储，实例重启或扩缩容时会话还可能失效。新版中任何请求都可以落到任何实例上，普通的轮询负载均衡即可。连带的好处是：`tools/list` 等列表不再随会话变化，可以按 `ttlMs` 跨会话缓存。

- A 错：协议无状态不等于应用无状态。跨调用的业务状态仍由 Server 保存（放在各实例都能访问的存储里），只是改用 Server 签发的显式句柄（如 `basket_id`）作为普通工具参数在调用之间传递，而不是隐式挂在会话上。
- B 错：版本仍要协商，只是改为逐请求进行：请求在 `_meta` 中声明版本，Server 不支持时返回 `UnsupportedProtocolVersionError` 并列出支持的版本。只认新版的 Server 无法服务只会 `initialize` 的旧客户端，旧客户端也没有自动升级的机制。
- D 错：无状态说的是协议层不保留上下文，与 TCP/TLS 连接是否复用无关；每个 HTTP 请求仍要携带并校验访问令牌。

</details>

更多题目请到 **[在线刷题](https://anticipate218.github.io/llm-agent-interview-bank/)**，或在 GitHub 上按小类浏览 [docs/README.md](docs/README.md)。

## 🧩 题型

| 题型 | 代码 | 考查重点 | 组卷默认分值 |
|---|---|---|---|
| 单选题 | `single` | 概念辨析，4 个选项中只有 1 个正确 | 2 |
| 多选题 | `multiple` | 全面理解，2～4 个正确选项 | 3 |
| 判断题 | `judge` | 常见误解的辨别 | 1 |
| 填空题 | `fill` | 关键术语与关键数值 | 2 |
| 计算题 | `calc` | 显存、算力、复杂度、指标等量化估算 | 5 |
| 代码输出题 | `code_output` | 读代码、理解 API 行为 | 3 |
| 代码填空题 | `code_fill` | 关键实现细节 | 4 |
| 代码改错题 | `code_debug` | 找出并修正常见 bug | 6 |
| 编程题 | `coding` | 手撕实现（附参考实现与测试） | 12 |
| 简答题 | `short` | 原理阐述与方案比较 | 8 |
| 场景分析题 | `scenario` | 线上问题排查、方案取舍 | 12 |
| 系统设计题 | `design` | 端到端系统设计 | 15 |

难度分为 **基础 / 进阶 / 挑战** 三档；考频分为 ★（偶尔考）、★★（常考）、★★★（高频必考）三档。

## 🛠️ 其他用法

1. **在 GitHub 上直接阅读**：从 [docs/README.md](docs/README.md) 进入，按小类浏览；答案和解析默认折叠，也可以[按题型浏览](docs/README.md#按题型浏览)。
2. **生成模拟卷（Markdown）**：

   ```bash
   pip install pyyaml
   python scripts/make_exam.py --list                        # 查看预设：算法岗、Agent 应用岗、工程岗、编程基础、综合卷
   python scripts/make_exam.py --preset agent-app --seed 1   # 生成 exams/agent-app-s1.md 与参考答案
   ```

   也可以自定义范围和题量，例如 `--domains LLM,INF --single 20 --calc 3 --short 2`。[exams/](exams/) 中有每个预设的一套样例。
3. **使用数据**：`dist/questions.json`（结构化全量数据）、`dist/questions.csv`（表格，可导入 Anki 等工具）。
4. **本地运行刷题网站**：

   ```bash
   pip install pyyaml
   python scripts/build_site.py          # 生成 site/data/
   python -m http.server -d site 8000    # 浏览器打开 http://localhost:8000
   ```

<details>
<summary><b>📁 目录结构</b>（点击展开）</summary>

```text
├── taxonomy.yaml          分类体系：大类 → 小类 → 考点
├── questions/             题目源数据（YAML），按 大类/小类.yaml 组织
├── site/                  在线刷题网站（纯静态，无需构建工具）
├── docs/                  自动生成的浏览页面（练习页、题型索引、分类体系表）与设计文档
├── dist/                  自动生成的数据文件（JSON、CSV）
├── exams/                 模拟卷样例（每个预设一套，种子 1）
├── scripts/
│   ├── validate.py        校验：格式、答案合法性、代码运行、查重、覆盖与答案分布统计
│   ├── build.py           生成 docs/ 与 dist/，更新本页统计
│   ├── build_site.py      生成网站数据 site/data/
│   ├── make_exam.py       组卷
│   ├── blind_review.py    盲答复核：导出不含答案的客观题，比对作答结果
│   └── append_batch.py    把草稿批量追加到题目文件
├── .github/workflows/     CI：校验题目、检查生成文件、部署网站到 GitHub Pages
├── CONTRIBUTING.md        出题规范与贡献指南
└── docs/题库设计.md        题库设计说明
```

</details>

## 🤝 参与贡献

欢迎补充新题、修正错误、完善讲解，哪怕只是指出一个错别字。请先阅读 [出题规范](CONTRIBUTING.md)，提交前运行：

```bash
pip install pyyaml numpy torch  # 代码题按 Python 3.13 + PyTorch（CPU 版即可）核对，与 CI 一致
python scripts/validate.py      # 不能有 ERROR
python scripts/build.py         # 重新生成 docs/ 与 dist/
```

发现答案或讲解有误，欢迎直接提 [Issue](https://github.com/anticipate218/llm-agent-interview-bank/issues)，注明题目编号（如 `LLM-ATTN-004`）。网站上点一下题号就能复制。

## 🙏 致谢

考点调研参考了以下公开资料（只借鉴「考什么」，题目与讲解均为原创），感谢这些作者的分享：

- [wdndev / llm_interview_note](https://github.com/wdndev/llm_interview_note)
- [Lau-Jonathan / LLM-Agent-Interview-Guide](https://github.com/Lau-Jonathan/LLM-Agent-Interview-Guide)
- [datawhalechina / hello-agents（面试问题总结）](https://github.com/datawhalechina/hello-agents)
- [adongwanai / AgentGuide](https://github.com/adongwanai/AgentGuide)
- [Zchary1106 / agent-interview-hub](https://github.com/Zchary1106/agent-interview-hub)
- [llmgenai / LLMInterviewQuestions](https://github.com/llmgenai/LLMInterviewQuestions)
- [KalyanKS-NLP / LLM-Interview-Questions-and-Answers-Hub](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub)
- [ombharatiya / AI-Engineer-Interview-Questions](https://github.com/ombharatiya/AI-Engineer-Interview-Questions)
- [amitshekhariitbhu / ai-engineering-interview-questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)
- [keepkeen 的大模型与 Agent 面经汇总系列博客](https://keepkeen.github.io/blog/)
- [代码随想录笔记：Agent / 大模型面试题汇总](https://notes.kamacoder.com/interview/llm/agent_interview.html)
- [牛客网上公开的大模型、Agent 与推理岗面经](https://www.nowcoder.com/)
- [AI Engineering Insider：The 100 Questions That Haunt AI Engineering Interviews](https://aiengineeringinsider.substack.com/p/the-100-questions-that-haunt-ai-engineering)

## ⚠️ 声明

- 本题库的题目均为基于公开知识的原创整理，考点参考了字节跳动、阿里巴巴、腾讯、华为、美团等公司大模型与 Agent 岗位的公开面经，**不是任何公司的真题**，仅供学习与面试准备使用。
- 题目的编写与复核大量借助了 AI 工具，并经过自动校验、代码实际运行、联网核实与独立盲答复核，但仍可能存在错误。
- 大模型领域发展很快，个别内容可能过时，欢迎指正。涉及论文和产品的内容以原始论文与官方文档为准，出处见题目的 `source` 字段；题目中注明的时间（如「截至 2026 年 11 月」）是核实时的状态。

## 📄 许可证

- **题目与文档**（`questions/`、`taxonomy.yaml`、`docs/`、`exams/`、`dist/`）：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)，全文见 [LICENSE-CONTENT](LICENSE-CONTENT)。转载或改编请注明出处，并以相同协议共享。
- **代码**（`scripts/`、`site/`）：[MIT](LICENSE)。
- `site/assets/vendor/` 中的 [KaTeX](https://katex.org)（MIT）、[markdown-it](https://github.com/markdown-it/markdown-it)（MIT）与 [highlight.js](https://highlightjs.org)（BSD-3-Clause）保留各自的许可证。

---

<div align="center">

**如果这个题库帮到了你，请点一个 ⭐ Star 支持一下，这是对作者最大的鼓励！**

[![Star History Chart](https://api.star-history.com/svg?repos=anticipate218/llm-agent-interview-bank&type=Date)](https://star-history.com/#anticipate218/llm-agent-interview-bank&Date)

</div>
