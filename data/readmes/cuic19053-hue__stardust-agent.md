# Stardust Agent｜大学生申报材料一站式工作台

<img align="right" src="./assets/logo.png" width="72" height="72" alt="Stardust Agent">

**大学生申报材料（申报书、申请书、商业计划书、实践报告、个人陈述）一站式工作台。**

**Stardust Agent** 是面向大学生的开源 AI Agent 工作台，帮助整理大创申报书、挑战杯申报书、中国国际大学生创新大赛商业计划书、奖学金申请书、保研材料和三下乡实践材料。学生可以在项目中整理学校通知和已有资料，让 Agent 检索依据、协助起草，再逐章编辑并导出 Word。

项目提供 35 个领域指南。后端使用 Python 和 FastAPI，支持 Ollama 本地模型和 OpenAI 兼容接口。这里的覆盖指指南与赛道目录，各赛道的模型写作、模板、图表和导出支持程度不同，尚未完成全部场景的端到端验收。仓库改动不代表已经在线上部署。

[![GitHub stars](https://img.shields.io/github/stars/cuic19053-hue/stardust-agent?style=social)](https://github.com/cuic19053-hue/stardust-agent/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE) [![Python 3.12+](https://img.shields.io/badge/Python-3.12+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) [![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-blue.svg)](https://modelcontextprotocol.io/) [![Online Platform](https://img.shields.io/badge/Online-agent.stardust.website-7952CC.svg)](https://agent.stardust.website)
[![cuic19053-hue/stardust-agent MCP server](https://glama.ai/mcp/servers/cuic19053-hue/stardust-agent/badges/score.svg)](https://glama.ai/mcp/servers/cuic19053-hue/stardust-agent)

[打开在线工作台](https://agent.stardust.website) · [用微调模型提取自己的口述](https://agent.stardust.website/student-intake/local) · [看 7B 微调回放](https://agent.stardust.website/student-intake) · [查看大创 Word 样例](./examples/demos/demo_innovation_research.docx) · [Agent 设计说明](./docs/design/AGENT_REFACTOR.md) · [English](./README_EN.md)

[下载桌面客户端](https://github.com/cuic19053-hue/stardust-agent/releases/latest) · [桌面版使用说明](./desktop/README.md)

## 快速上手

1. 打开 [在线工作台](https://agent.stardust.website)，登录后创建项目。
2. 描述申报目标，上传学校通知、项目记录等材料，并核对确认提取出的信息。
3. 在对话中查找依据、起草内容，预览并保存章节草稿，逐章编辑后导出 Word。

例如，可以先问：“我想申报大创创新训练项目，课题是校园无人机巡检。请帮我梳理申报书结构，还需要准备哪些材料？”

在线入口无需安装 Python 或使用命令行。使用平台模型无需自备 API Key，账号额度、模型可用性与费用以工作台提示为准。未知事实应保留待补充；用户确认只代表其提供或认可了信息，不代表系统完成独立核验。

## 学生口述转结构化档案

### 在自己的浏览器里提取口述

微调后的 **Qwen2.5-0.5B** 可以直接处理你输入的中文口述。用支持 WebGPU 半精度运算的浏览器（如兼容的桌面 Chrome 或 Edge）打开端侧页面，无需登录，也不扣工作台积分。[打开端侧口述提取](https://agent.stardust.website/student-intake/local)

1. 点击「加载端侧模型」。首次约需下载 320 MB。下载中断或刷新后，在同一设备、同一浏览器再点加载，页面会显示已恢复的底座分片数，只补缺失或损坏的分片。
2. 模型就绪后，输入或粘贴自己的口述（最多 600 字、12 行），点击「提取口述」。此时可以断网，推理和原话核对都在设备上完成。
3. 对照每条候选的字段、状态和原话，勾选核对无误的条目，再点「复制已核对的条目」。复制的 JSON 包含对应的发言回合和引文。刷新或关闭页面会清空本页口述和候选。

> 我准备做一套校园树皮标本卡，还没开始制作。

输入这段口述后，页面会把“一套校园树皮标本卡”列为 **预期成果 · 计划**，并引用“我准备做一套校园树皮标本卡”。在国奖申请口述中，页面会略去家庭收入，并单独核对学生自述的专业。

在一台 **MacBook Pro** 的桌面 Chrome 上实测，模型就绪后，点击「提取口述」到首条短口述结果出现的中位耗时由 **24.67 秒降至 2.05 秒**。新旧版在 44 段合成回归口述上的字段、状态、引文和追问逐条一致。两版都漏掉了一段 600 字口述末尾的计划。[提速与质量实测](./docs/reports/STUDENT_INTAKE_BROWSER_LATENCY_2026-11-26.md) · [模型来源与使用条件](./server/static/intake-0p5b-v1/MODEL.md)

### 在工作台确认入档

在项目对话里写下成绩、经历或计划，再打开 **事实矩阵 → 学生口述档案 → 提取本项目口述**。这里使用工作台当前配置的模型，平台默认使用 DeepSeek V4 Flash，按工作台积分计费。系统从 41 个字段中提取候选，每条附有发言回合和学生原话。核对自述、模糊、计划或否定条目后，点击「我已核对，按此状态入档」，该条才会按原状态存入项目。未知、拒答和未解决的冲突留在核对区。

例如，你说“我的专业是文物保护”，工作台会用这句话核对候选的字段和值。如果同一项目出现两个预算，工作台会列出能核实的两处原话，请你确认本次申报用哪一个。部分信息需要手动核对时，你可以先确认其余通过校验的条目。

### 查看 7B 微调回放与评测

免登录的免费演示回放了 Qwen2.5 7B 在五段合成口述上微调前后的真实回答。选「两份预算」可以看到，微调模型只提取了 8400 元，来源校验找回了另一回合的 4800 元，保留两处原话并请学生核对。[查看演示与评测](https://agent.stardust.website/student-intake)

在另行封存的 20 段合成对话上，使用同一 MLX 底座和来源校验规则，LoRA 微调使字段 F1 从 13.6% 升至 55.07%，整例通过数从 2/20 升至 3/20。历史 Ollama 配置加相同规则通过了 8/20。最初的 24 例只用于开发回归。[训练与评测说明](./server/evals/student_intake_pilot/README.md)

## 支持哪些大学生申报材料？

| 申报场景 | 可以整理的材料 | 样例与指南 |
| --- | --- | --- |
| **大创与科研立项** | 大创创新训练、创业训练和校院级科研立项申报书 | [大创 Word 样例](./examples/demos/demo_innovation_research.docx) · [创新训练指南](./subskills/innovation-research/SKILL.md) |
| **挑战杯与创新大赛** | 挑战杯申报书、大学生创新大赛（原互联网+）商业计划书 | [挑战杯样例](./examples/demos/demo_challenge_cup.docx) · [商业计划书样例](./examples/demos/demo_internet_plus.docx) |
| **奖学金与评优** | 国家奖学金、国家励志奖学金、校级奖学金及评优申请材料 | [国家奖学金样例](./examples/demos/demo_national_scholarship.docx) · [申请指南](./subskills/national-scholarship/SKILL.md) |
| **升学与留学** | 保研推免个人陈述、交流项目和国家公派留学申请材料 | [保研样例](./examples/demos/demo_graduate_recommendation.docx) · [推免指南](./subskills/graduate-recommendation/SKILL.md) |
| **三下乡与社会实践** | 社会调研、支教、政策宣讲和科技服务等实践申报材料 | [社会调研指南](./subskills/social-survey/SKILL.md) |

样例使用示例数据，供了解材料结构和排版，不是已授权入库的真实学生范文。具体栏目、字数及提交要求请以所在学校的最新通知为准。[查看全部 35 个领域指南](./subskills/README.md) · [查看全部 Word 样例](./examples/demos/)

每个赛道的工作台支持等级和冒烟范围见[赛道目录](./subskills/README.md)。核对线上工作台实际运行的源码版本时，可查看公开存活接口返回的 `commit_sha` 和 `commit_url`。[线上版本接口](https://agent.stardust.website/api/ping) · [发布验证说明](./docs/DEPLOYMENT_AND_ROLLBACK.md#四线上健康检查与验证清单-post-deployment-verification)

## 常见问题

**不会编程，可以使用吗？** 可以直接使用在线工作台，按提示创建项目并填写或上传材料。本地部署和 MCP 接入面向需要自行配置环境的用户。

**可以用自己的材料吗？** 可以上传学校通知、项目记录等资料，核对并确认提取结果后，再让 Agent 在项目资料中检索依据。现有数字、来源和完整性检查范围有限，模型仍可能遗漏、误解或编造；回答中的事实、引文及其适用性仍需要本人逐项检查。

**需要付费或配置模型吗？** 浏览器端口述提取无需 API Key 或工作台积分。在线工作台的平台模型有试用额度，按积分计费。使用自己的 API Key 时，费用按服务商规则计算。本机 Ollama 也不扣工作台积分，需自行准备运行环境。项目代码按 MIT 协议开源。[模型与服务配置](./server/README.md)

当前仓库实现中，国奖基础起稿可不调用模型；明确要求字数、风格或重点经历时使用所选模型。是否已在线上提供以部署版本为准。

## 跟着一次工具调用读代码

> 请查一下已确认材料，告诉我样本量和记录的观察指标。

测试项目里有一份已确认的观察记录。本机实测中，Qwen2.5 7B 选择了 `search_project_materials`。服务端在当前项目中检索，将命中的段落交还给模型。下面是这次回答的节选。

> 根据已确认的观察记录，团队观察了12株番茄苗，并记录了土壤含水量和病斑面积。

评测会同时核对工具名和答复内容。如果回答引入记录里没有的“准确率达到 92%”，这条用例就会失败。[用例与原始材料](./server/evals/cases.json) · [评测脚本](./server/evals/run.py)

| 工程问题 | 实现方式 | 源码 |
| --- | --- | --- |
| 模型怎样选工具，何时结束？ | 同步答复与 SSE 流式答复共用对话循环。一轮对话最多迭代 6 次，工具调用预算为 8 次。服务端执行前再次检查工具授权，并绑定当前项目。 | [运行时](./server/proposal/chat_runtime.py) · [工具路由](./server/proposal/chat_tools.py) |
| 回答里的材料从哪里来？ | 项目资料经用户确认后分段索引。RAG 检索结合关键词和可用的同版本向量，返回来源文件和段落位置。官方通知另按学校、年度和适用范围查找。 | [项目检索](./server/proposal/retrieval.py) · [知识来源与覆盖](./docs/rag-status.md) |
| 聊天怎样变成 Word？ | 学生从对话中预览并选取章节草稿，编辑后保存。导出使用项目里已保存的正文，提交前仍可核对学校模板和引用。 | [对话草稿](./server/proposal/chat_drafts.py) · [Word 导出](./server/proposal/exporter.py) |
| 长任务中途断开怎么办？ | 材料任务按项目入队并检查写回版本。网页聊天持久化已完成的模型和工具步骤；用原请求标识恢复时复用已知结果，未知调用不会自动重发。浏览器保留请求标识，换设备需重新提供该标识和模型配置。 | [对话执行记录](./server/proposal/agent_journal.py) · [任务队列](./server/proposal/material_jobs.py) |
| 大创草稿预审如何执行和计费？ | LangGraph 保存草稿快照，围绕具体断言召回材料，核算预算并区分计划、成果和学校规定。尚无可验证支持的 AI 判断单列为待人工判断的线索。云端保存队列和检查点，实际模型调用绑定积分预留及用量结算。 | [预审图](./server/proposal/review_graph.py) · [云端设计与恢复机制](./docs/design/LANGGRAPH_REVIEW_CLOUD.md) |
| 补资料后如何继续？ | 确认保存聊天草稿或生成章节后自动提交免费规则预审。报告列出待补项，支持跳转修改或确认资料，再从新快照接续检查；旧报告保留，AI 检查仍须主动勾选。 | [流程衔接](./server/proposal/review_workflow.py) · [修复与验收记录](./docs/reports/AGENT_REVIEW_LOOP_2026-11-18.md) |

## 预审效果怎样验证？

预审评测使用同一批合成草稿，对比免费规则、单次模型直接预审、现有 LangGraph 预审流程。同一模型摘要、提示词、输出结构及生成参数下，记录误报、漏检、引用原文匹配、耗时与 Token；原始响应和逐项复核依据保留，失败运行不被成功重试替换。模型不会读取预期问题标签。

当前试点覆盖预算冲突、无依据成果、正确研究计划、材料注入、空章节和外校旧通知六类样例。样例由 Agent 编写，语义指标区分 Agent 辅助复核与独立人工复核；程序测试通过数和引文逐字匹配率不作为模型准确率。它用于检查规则、检索和输出约束的作用，不能外推为全部赛道的质量结论。

按下文安装锁定依赖并启动本机 Ollama 后运行。

```bash
uv run --no-sync python server/evals/review_benchmark.py --output outputs/evals/review-pilot
```

[首轮 Qwen 本机试点](./docs/reports/REVIEW_BENCHMARK_2026-11-17.md)：按 Agent 辅助复核口径，直接模型命中 5 个目标问题中的 3 个，现有流程命中 5 个；两条路径各有 13 条误报（含重复提醒）。独立人工校准尚未完成，结果不代表线上模型效果。原始请求、响应和判定依据均可核对。

必过 CI 在固定的本地模型上重新推理口述和草稿样例，并回放预审的真实模型输出。[质量门禁的指标与复现命令](./server/evals/CI_QUALITY.md)

[对比方法、指标口径与复现步骤](./server/evals/REVIEW_BENCHMARK.md) · [合成样例和预期问题](./server/evals/review_cases.json) · [逐项结果与原始模型记录](./server/evals/baselines/review_pilot_20261117.json)

[后续提示词实验](./docs/reports/REVIEW_CALIBRATION_2026-11-18.md) 固定候选并增加四个合成回归样例。候选减少了输出条数，却增加了误报，并出现新的学校规则漏检。仓库保留失败候选、原始响应和可复现比较：核对实际输入与参数，同时检查误报、漏检和具体漏掉的问题，避免用单一汇总指标掩盖退化。

## 本地运行与复现

先安装 [uv](https://docs.astral.sh/uv/getting-started/installation/)。以下命令按 `.python-version` 安装 Python 3.12，并按 `uv.lock` 安装工作台和测试依赖。

```bash
git clone https://github.com/cuic19053-hue/stardust-agent.git
cd stardust-agent
uv python install
uv sync --locked --extra full --extra review --group test
uv run --no-sync uvicorn server.app:app --host 127.0.0.1 --port 8765
```

打开本机工作台即可整理材料。需要本机模型时，启动 Ollama，运行 `ollama pull qwen2.5:7b` 和 `ollama pull bge-m3`，再在「模型配置」中选择 Ollama。点击「开始新对话」描述申报目标，上传并核对资料后即可提问。本机模式使用 SQLite，数据保存在 `.agent-data/`。云端使用 Supabase 按账号管理项目。平台模型使用工作台积分，自带 API Key 时按模型服务商规则计费。[本机工作台](http://127.0.0.1:8765) · [模型、存储和服务配置](./server/README.md)

在仓库根目录运行下面的命令，可以用本机模型复现上面的提问。脚本使用临时项目，输出实际调用的工具、答复片段和各用例的通过情况。

```bash
uv run --no-sync python server/evals/run.py
```

## 场景、样例与扩展

35 个申报场景以 Skills 形式提供领域指南。网页按选定赛道加载经过滤的指南，并支持按需分页读取该 Skill 已链接的参考资料；指南及示例不能当作官方规则或学生事实。Word 输出是供编辑核对的草稿，自动图形需要构建器支持、有效图片或节点数据及绘图依赖；数据不足或渲染失败时可能留下待补充提示，不能据此推定全部赛道图表已接通。[全部场景](./subskills/README.md) · [挑战杯样例](./examples/demos/demo_challenge_cup.docx) · [奖学金样例](./examples/demos/demo_national_scholarship.docx) · [全部 Word 样例](./examples/demos/)

仓库公共语料包含 **42 篇正式高校官方通知及 1 篇院级科创活动报道**，检索需匹配学校、年度与适用对象，并回源核验。**已获授权、脱敏并审核通过的真实范文当前为 0 篇**；详见 [RAG 状态说明](./docs/rag-status.md)。

开发者可以从 Codex、Cursor 或其他 MCP 客户端连接本机项目工具，也可以直接加载某一赛道的 `SKILL.md`。本机项目 MCP 与网页共享项目和材料，使用 stdio 启动的命令为 `uv run --no-sync python server/mcp_server.py --transport stdio`。[项目 MCP 实现](./server/mcp_server.py) · [Skills 入口](./SKILL.md)

<details>
<summary><b>展开 35 个领域指南及文件大小</b></summary>

以下是指南目录与内容量，不表示各赛道已通过相同的写作、排版或线上交付验收。

**🔬 科研与竞赛 · 9 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 1 | 大创 · 创新训练项目 | `innovation-research` | 64 KB |
| 2 | 大创 · 创业训练项目 | `entrepreneurship-training` | 47 KB |
| 3 | 大创 · 创业实践项目 | `entrepreneurship-practice` | 53 KB |
| 4 | 校级科研立项 | `university-research` | 62 KB |
| 5 | 院级科研立项 | `college-research` | 80 KB |
| 6 | 挑战杯 · 课外学术科技作品 | `challenge-cup` | 82 KB |
| 7 | 互联网+ · 商业计划书 | `internet-plus` | 76 KB |
| 8 | 互联网+ · 红旅赛道 | `internet-plus-red-tour` | 65 KB |
| 9 | 国家级项目立项逻辑评测 | `national-project-eval` | 44 KB |

**🏆 评优与资助 · 12 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 10 | 国家奖学金（10000 元） | `national-scholarship` | 38 KB |
| 11 | 国家励志奖学金（6000 元） | `motivation-scholarship` | 48 KB |
| 12 | 校级奖学金 | `university-scholarship` | 44 KB |
| 13 | 企业专项奖学金 | `enterprise-scholarship` | 50 KB |
| 14 | 单项奖学金 | `single-scholarship` | 46 KB |
| 15 | 国家助学金 | `grant-application` | 14 KB |
| 16 | 优秀毕业生 | `outstanding-graduate` | 46 KB |
| 17 | 优秀学生 / 三好学生 / 优秀团员 | `outstanding-student` | 61 KB |
| 18 | 优秀学生干部 | `outstanding-cadre` | 72 KB |
| 19 | 文明大学生 | `civilized-student` | 62 KB |
| 20 | 优秀班集体 | `class-collective` | 57 KB |
| 21 | 优秀毕业设计 / 论文 | `outstanding-thesis` | 65 KB |

**🌾 活动类 · 5 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 22 | 三下乡 · 社会调查 | `social-survey` | 47 KB |
| 23 | 三下乡 · 支教 | `volunteer-teaching` | 53 KB |
| 24 | 三下乡 · 政策宣讲 | `policy-lecture` | 56 KB |
| 25 | 三下乡 · 科技服务 | `tech-service` | 67 KB |
| 26 | 西部计划 | `western-plan` | 65 KB |

**🚩 政治身份类 · 3 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 27 | 入团申请书 | `youth-league-application` | 62 KB |
| 28 | 阶段汇报 / 思想汇报 | `summary-report` | 30 KB |
| 29 | 转正申请书 | `youth-league-conversion` | 30 KB |

**🎓 升学类 · 2 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 30 | 保研推免申请 | `graduate-recommendation` | 46 KB |
| 31 | 选调生申请 | `selected-graduate` | 64 KB |

**✈️ 公派留学 / 交流类 · 2 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 32 | CSC 国家公派留学 | `csc-scholarship` | 61 KB |
| 33 | 交流项目申请 | `exchange-program` | 74 KB |

**📋 其他 · 2 个**

| # | 赛道 | 编码 | 内容量 |
|---|---|---|---|
| 34 | 转专业申请 | `major-transfer` | 67 KB |
| 35 | 应征入伍申请书 | `military-enlistment` | 62 KB |

</details>

## 项目与社区

项目源自团队参加挑战杯、反复修改申报书的实践。同时感谢 [@richyhu](https://github.com/richyhu) 的帮助。欢迎通过 Issue 提供学校模板的差异、更新的申报要求和能够复现的问题。[项目演示视频](https://www.douyin.com/video/7692700167341985051) · [贡献指南](./CONTRIBUTING.md)

### 交流与合作

- **大学生科创交流群**：交流大创、挑战杯、大学生创新大赛备赛与申报材料准备。
- **合作咨询**：交流立项思路、技术路线、商业计划书等具体需求。

<div align="center">
  <img src="./assets/contact_qr.png" width="200" alt="作者微信二维码">
  <p>👉 扫码加微信（进群备注 <b>进群</b> ｜ 合作私聊 <b>合作+具体需求</b>）</p>
</div>

<details>
<summary>社区路线图</summary>

> 「学创杯 / 创青春 / 三创赛」已进入开发队列（已达成 100 ⭐ 里程碑）。

| 里程碑 | 解锁赛道 |
|---|---|
| ⭐ 100 | 学创杯、创青春、三创赛（已解锁，开发中） |
| ⭐ 300 | 节能减排大赛、生命科学竞赛（学科专项类） |
| ⭐ 500 | 服务外包大赛、商业精英挑战赛（商科类） |
| ⭐ 1000 | 师范生教学技能、英语类竞赛 |

</details>

<details>
<summary>使用说明与免责声明</summary>

**本项目按「现状」提供，仅供学习和参考。**

1. **非官方出品**：与任何高校、教育主管部门、评审委员会无关。评审标准与格式规范基于公开信息和社区经验整理，不构成官方指导意见。
2. **真实性由使用者负责**：生成的申报材料，其真实性和准确性由使用者本人承担全部责任。虚假申报可能面临学籍处分乃至法律责任。
3. **不保证结果**：不承诺通过评审、获得立项或拿到奖学金。
4. **格式以学校模板为准**：各校模板在栏目顺序、字数、排版上可能不同，提交前请对照本校要求逐项检查。
5. **政治类文书的特殊性**：参考内容不构成政治立场建议，政治表述的准确性由申请人承担全部责任。
6. **责任豁免**：在法律允许的最大范围内，作者及贡献者不对因使用或无法使用本项目产生的任何直接、间接或后果性损害承担责任。
7. **合规使用**：请遵守所在国家/地区及学校的法律法规。如使用行为违反相关规定，请立即停止并删除本项目。

**使用本项目即表示你已阅读、理解并同意上述声明。**

</details>

本项目采用 MIT 许可，使用与分发时请保留原作者署名和许可声明。[LICENSE](./LICENSE)
