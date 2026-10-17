# 千里马个人 Harness

[中文] | [English](README.en.md)

本地优先、可恢复、可验证的个人任务 Agent Harness。Amazon 运营是其中一个场景包，而不是系统的全部定位。

亚马逊运营能力仍是千里马的核心业务场景之一，继续覆盖广告、Listing、关键词、选品、库存、利润、供应链和复盘；变化只在于这些能力运行在统一的个人 Harness 之上，而不是反过来定义整个系统。

[![CI](https://github.com/Brian-dai694/qianlima/actions/workflows/qianlima-verify.yml/badge.svg)](https://github.com/Brian-dai694/qianlima/actions/workflows/qianlima-verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v2.10.0-blue.svg)](CHANGELOG.md)

> 当前版本：`v2.10.0`

千里马不是聊天机器人外壳，也不是企业运营控制平台。它把个人任务组织成可恢复、可验证的执行闭环，让 Agent 能够：

```text
理解意图 -> 路由场景 -> 创建任务会话 -> 选择上下文和 Skill
-> 执行受限工具 -> 验证证据 -> 记录回执 -> 恢复或关闭
```

Codex、Claude Code 等负责交互和推理；千里马负责任务路由、业务口径、记忆选择、权限边界、执行回执和结果核验。

## 先看结论

- 普通问答和同主题续问走快速路径，不启动复杂运行时。
- 学习、研究、报表和文件分析按需加载相关上下文，不读取整库历史。
- Skill 会先检查能力和风险，再在受限范围内使用；不会悄悄扩大文件、网络或写入权限。
- 低风险改进可以自动测试、自动收敛；高风险改进会冻结旧版本，不把权限变化混进自进化。
- 高影响动作会给出影响范围、依据和回退信息，再进入受控执行。
- 默认本地优先。公开仓不包含真实账号、凭据、运营数据或生产端点。

## 新架构：任务是唯一主线

千里马不再把记忆、Skill、工具和自进化做成彼此平行的隐式能力。所有复杂任务都围绕一个 `task_id` 组织：

```text
薄入口
-> 任务路由与断点
-> 最小上下文
-> 受限能力
-> 证据与验证
-> 低风险学习候选
```

六个平面各自只有一个职责：入口负责快答，任务控制负责状态和续办，上下文负责相关性筛选，能力负责唯一的工具边界，证据负责完成判定，学习负责版本化候选。记忆和 Skill 永远没有授权能力。

低风险习惯不会每次打断用户：同一模式至少出现 3 次，离线回放和独立检查都通过后，才自动进入表达、排序或默认建议版本；版本可查看、编辑、停用、删除、撤销和恢复。权限、网络、文件范围、删除、外发、预算、采购和安全规则永远不会由学习改变。

架构合同：`.qianlima/specifications/personal-architecture-contract.json`。

### 自进化实验场

`experiments/personal-learning-release/` 提供一组完全合成、可重复的策略回放，用来比较手动确认与低风险自动释放：至少 3 次一致行为、离线回放和独立检查全部通过后，表达、排序和默认建议可自动生效；网络、写入、删除、预算和权限等边界始终冻结。实验不联网、不安装 Skill、不读取真实用户数据，也不写入生产记忆。

```powershell
.\experiments\personal-learning-release\run-personal-learning-experiment.ps1 -RunId plr-replay
```

### Hugging Face Space

个人学习实验的只读演示位于 `space/`，目标 Space 为 [`brian147/qianlima`](https://huggingface.co/spaces/brian147/qianlima)。演示只加载合成实验结果，不调用模型、不联网、不安装 Skill、不读取真实用户数据，也不写入生产记忆。

### 个人执行骨架

复杂任务使用四个可替换的本地适配器，全部绑定 `task_id`，不自动联网、不安装 Skill、不启动后台循环，也不授予权限：

```text
快速路由
-> 任务状态与 checkpoint
-> 选择性上下文
-> 本地 DataFlow / CodeGraph
-> 结构化产物与验证
```

- `route-personal-task.ps1`：L0/L1 快答和续问短路；L2/L3 只进入最小任务链，L4 保留受控确认。
- `invoke-personal-task.ps1`：保存步骤、工具归属、结果摘要和验证状态；未验证不能完成，终态不可修改。
- `invoke-personal-dataflow.ps1`：在本地处理 CSV/JSON/JSONL，输出来源哈希、聚合摘要、警告和产物哈希，不覆盖原文件。
- `invoke-personal-codegraph.ps1`：在明确目录内做符号/引用候选检索；结果明确标注为文本证据，不冒充完整语义调用图。
- `manage-personal-skill-card.ps1`：把重复成功沉淀为版本化方法卡，自动释放低风险卡片，按任务返回步骤、输入、输出和质量门禁摘要。
- `invoke-personal-knowledge.ps1`：把本地资料做编码检查、去重、分块、哈希和轻量检索；不联网、不安装 Embedding、不覆盖来源。

L2/L3 任务只选择一个主专家画像；L3 另加独立检查者。专家之间只共享被选中的摘要，不共享完整记忆或权限。

这四个适配器只产生候选结果和证据，不拥有业务写入、网络、预算或权限授予能力。

## 能做什么

千里马的个人版业务目录覆盖一个 Amazon 店铺从判断机会到复盘的完整周期：

| 领域 | 能力 |
|---|---|
| 经营分析 | 日报、周报、月报、季报、年报；月度、季度、年度计划 |
| 利润与合规 | 日/周/月/季/年利润口径；税务、海关、产品合规检查 |
| 市场与选品 | 选品、市场、竞争、关键词、定价、VOC 和机会判断 |
| Listing | 标题、主图、五点、长描述；事实、关键词和合规校验 |
| 供应链 | 采购、厂家合作、包装、海运、物流、交期与补货判断 |
| 库存 | 入仓、上架、本地库存、亚马逊库存、库存风险和清货建议 |
| 流量与广告 | 流量、广告、转化、活动、关键词排名和竞价诊断 |
| 售后与复盘 | 售后、退货、清货、利润变化和问题根因复盘 |

结果不是一段无法复核的结论。业务结果可以附带来源、时间范围、公式、假设、不确定性、待验证项和可重跑入口。

## 使用方式

你不需要记住 Skill 名称、MCP 参数或内部脚本。直接描述目标、资料位置和权限即可：

```text
帮我看这 14 天广告数据，先告诉我利润和 ACoS 的主要变化，只读，不改预算。

分析这批竞品，给出适合我的产品机会，列出证据和未知项。

优化这个 Listing，先检查产品事实和关键词，再给标题、五点和长描述候选。

管理技能：检查现有 Skill 的健康度，按风险和收益分组，自动处理低风险项。
```

千里马按任务风险选择路径：

| 路径 | 典型任务 | 行为 |
|---|---|---|
| 快速 | 普通问答、解释、续问 | 直接回答，不启动复杂流程 |
| 只读 | 学习、研究、报表、文件分析 | 读取最小资料，输出证据和结论 |
| 受控执行 | 本地计算、生成报告、整理文件 | 先预检，限定目录和步骤，留下回执 |
| 高影响 | 改价、竞价、预算、采购、发布、外发、删除 | 明确影响范围，保留快照和回退路径 |

## V1 广告异常诊断闭环

个人版先把一个高频生产闭环做实：

```text
本地广告 CSV
-> 异常诊断
-> 结构化行动卡
-> 证据回执
-> 后续导出回读
-> 3 天 / 7 天复盘
```

输入至少包括广告活动、广告组、搜索词、花费、销售额、订单、预算和时间范围。每张行动卡都说明：

- 哪个 Campaign / Target 出现什么问题；
- 原始文件、时间范围、行号和指标证据；
- 暂停、降价、升价、调整预算或保持的候选建议；
- 预期影响、预算暴露和风险；
- 当前只读权限、是否需要后续确认；
- 原始出价/预算回滚基线；
- 执行后 3 天和 7 天需要回读的指标。

运行入口为 `.qianlima/scripts/invoke-personal-ad-ops-loop.ps1`。它只处理本地 CSV，不联网、不改广告、不改预算、不外发，也不启动多 Agent。真正的业务写入不属于个人版闭环。

## 自进化怎么工作

个人版会持续变得更顺手，但不会把一次偶然行为变成永久权限：

```text
任务轨迹 / 用户纠正
        -> 习惯或 Skill 改进候选
        -> 本地回放与失败注入
        -> 独立检查
        -> 低风险自动收敛，风险升高则冻结
        -> 记录版本、依据和回滚路径
```

个人版 Governed Loop 将写入和检查分开：

- `Builder` 只修改任务指定范围。
- `Checker` 只有读取和检查能力，不能顺手改代码。
- 编排器保留检查器的原始输出，不替它粉饰失败。
- 最多运行 5 轮；全绿结束。
- 同一失败连续两次、出现回归、连续两轮没有实质进展、超时或越权时自动冻结。
- 重试不会自动增加 Grant、预算、数据范围、网络权限或业务写入权限。

低风险候选可以在独立检查通过后自动进入下一版本；涉及权限、数据分类、外部访问或攻击面的候选保持旧版本并冻结，避免“自进化”变成自我扩权。

## 记忆与边界

千里马记住的是工作方式，不是无限保存你的全部资料：

| 记忆层 | 示例 | 规则 |
|---|---|---|
| 当前任务 | 当前文件、目标、未完成结论 | 任务结束后自动降权 |
| 稳定偏好 | 中文、先结论、简洁或详细 | 可查看、编辑、删除和回退 |
| 观察习惯 | 常用工作流顺序、常用展示方式 | 先影子验证，不直接改变重要行为 |
| 已验证模式 | 多次成立且没有被纠正的工作方式 | 只影响表达、排序和默认建议 |
| 敏感资料 | 凭据、原始业务数据、单次附件 | 默认不进入长期记忆，只保留必要引用 |

记忆不能增加工具权限、网络权限、文件范围、预算、删除权限或外发权限。撤销和清除必须能让后续读取立即失效。

### 记忆检索分层

个人记忆按使用时效分为三层：

- `hot`：当前任务和最近频繁使用的内容，优先从快速本地层读取。
- `warm`：已验证偏好和近期工作习惯，从本地工作层读取。
- `cold`：长期、可复现的本地经验，按需从低成本存储读取。

运行时先按 Grant、任务相关性、状态、分类和时效过滤，再按任务匹配、层级、最近使用和访问频次排序；不会把全部记忆扫描后塞进上下文。

## 执行与 MCP

个人版只预留显式启动的本地 `stdio` 模式。用户不需要配置端口、URL 或公开 Agent Card。

当前唯一的本地证据工具是：

```text
qianlima_readonly_evidence_task
```

它必须绑定当前任务匹配、未过期、未撤销的最小 Grant，并且强制：

- 无网络
- 无业务写入
- 不读凭据
- 不删除或覆盖原始文件
- 不直接委派其他 Agent
- 返回 Artifact 和 Evidence Receipt

MCP 端口和业务适配器只作为能力合同预留。具体连接是否可用，仍由当前任务、数据范围和运行时策略决定。

涉及外部 API、付费工具或远程 Agent 时，调用前必须显示提供方、用途、数据范围、预计成本、成本来源和确认状态。未知成本按 `0` 记录并标记为未知；默认网络仍关闭。

## 专业工具学习模式

个人版可以学习专业 MCP 工具的设计，但不会安装或运行这类工具。当前只对经过脱敏的工具清单做离线模拟：

| Profile | 学习内容 | 个人版模拟结果 |
|---|---|---|
| `reverse-readonly` | 函数、字符串、调用关系、反编译和数据流等只读能力 | 可标记为受限模拟 |
| `reverse-triage` | 函数、字符串、导入导出和交叉引用等初筛能力 | 可标记为受限模拟 |
| `reverse-edit` | 重命名、注释和类型修改 | 学习模式阻断 |
| `reverse-debug` | 补丁、调试、内存写入和 `py_eval` | 学习模式阻断 |

每次模拟都要求 `stdio` 设计、引用式目标和最小能力清单；URL、端口、绝对路径、网络、安装、运行时启动和权限授予都会被拒绝。适配器只返回结构化决策，不连接 IDA、不打开监听器、不执行工具。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-professional-tool-governance.ps1'
```

## 个人版 Harness 验收

个人版只覆盖轻量的 `T/C/L`，并保留基础 `O/V`：工具最小授权、记忆先过滤后召回、任务状态可暂停/回放/停止，以及最小轨迹和证据核验。企业租户、企业审批和车队治理不属于个人版。

普通任务先走本地低成本筛选；只有 L2+、证据冲突、必填字段缺失或用户主动要求深度复核时，才进入受预算和原 Grant 约束的复核阶段。L0/L1 默认不启动复核。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-harness-acceptance.ps1'
```

## 个人项目价值

个人版衡量的是“每个人能稳定创造更多可复核价值”，不是用“减少人员”作为默认 ROI。项目候选优先满足：高频、规则相对稳定、有历史样本、结果可度量、错误可回退、风险可隔离，并保留人工核验点。

评估必须同时记录质量、效率、成本、风险和组织复用指标，并使用本地基线与受控对照；行业通用数字、模型自评分和命令成功都不能直接证明业务价值。合格候选只能进入只读、小范围、可回退试点。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-project-value.ps1'
```

## 安装与启动

### Windows

```powershell
git clone https://github.com/Brian-dai694/qianlima.git
Set-Location qianlima
powershell -NoProfile -ExecutionPolicy Bypass -File '.\start-qianlima.ps1'
```

### macOS / Linux

需要 PowerShell 7：

```bash
git clone https://github.com/Brian-dai694/qianlima.git
cd qianlima
bash ./start-qianlima.sh
```

普通用户只需要使用自然语言。脚本、合同和回归测试是开发与排查入口，不是日常操作界面。

## 验证

提交前运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\verify-qianlima.ps1'
```

个人版关键回归：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-learning-boundary.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-skill-gate.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-memory-chunks.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-governed-loop.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-readonly-evidence-task.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-task-manager.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-router.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-dataflow.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-codegraph.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-skill-card.ps1'
powershell -NoProfile -ExecutionPolicy Bypass -File '.\.qianlima\scripts\test-personal-knowledge.ps1'
```

CI 会检查启动骨架、公开安全、运行时边界、记忆、Skill、证据和 Governed Loop。校验不安装 Docker，不访问生产系统，也不获取真实凭据。

## 仓库结构

```text
AGENTS.md                 Codex 最小入口和工作规则
start-qianlima.ps1       Windows 启动入口
start-qianlima.sh        macOS/Linux 启动入口
.qianlima/
├── task-cards/           任务卡
├── workflows/            业务工作流
├── specifications/       执行、证据、记忆和权限合同
├── scripts/              运行时、校验和回归脚本
├── working/              本地偏好与受限 Skill 工作区
├── run-traces/           本地执行轨迹，默认不提交
└── templates/            报告和回执模板
```

## Git-safe 规则

本项目的唯一提交和推送工作副本是：

```text
C:\Users\UEFR\Desktop\Work Space\千里马计划-git-safe
```

所有千里马提交都在该目录的 `main` 分支完成并推送到 `origin/main`。另一个工作目录只作为迁移或参考来源，不在其中提交、不创建分支、不 fork。

## 隐私

公开仓只保存脱敏模板、合同、规则和测试。禁止提交：

- API key、Token、密码、Cookie、私钥或真实 URL
- Amazon、ERP、广告后台、税务和海关原始导出
- 客户信息、账号信息、真实成本和利润台账
- usage ledger、decision log、运行日志、截图和本机绝对路径

运行产生的索引、报告、轨迹和本地配置默认由 `.gitignore` 排除。发现凭据或敏感资料时，先停止提交并清除 Git 暂存区。

## 版本

当前版本为 `v2.10.0`。详细变更见 [CHANGELOG.md](CHANGELOG.md)。

## 许可证

MIT
