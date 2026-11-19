<div align="center">

# Fiora

**证据挂载式 AI 代码审计 Harness。工具负责查全，AI 负责判准。**

单二进制 CLI：规则扫描 + AI 判定 + 证据链 + 漏洞链，产出一份可直接交付的
单文件审计报告（RCE 攻击面置顶、发现↔PoC 双向跳转、自动统计）。

[![tests](https://img.shields.io/badge/tests-158-green)](#开发)
[![CI](https://github.com/Ryze-T/fiora/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Ryze-T/fiora/actions/workflows/ci.yml)
[![release](https://img.shields.io/github/v/release/Ryze-T/fiora)](https://github.com/Ryze-T/fiora/releases)
[![license](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![report](https://img.shields.io/badge/report-single--file%20HTML-orange)](#图解)

[快速开始](#快速开始) · [图解](#图解) · [工作原理](#工作原理) · [能力](#能力) · [开发](#开发) · [已知边界](#已知边界)

</div>

---

fiora 是 **Agent 工作台背后的审计引擎**：工具管确定性扫描，AI 管判定，Agent
管环境验证。核心闭环（扫描→判定→报告）不依赖 Agent，`fiora run` 一条命令跑完；
交给 Agent 则追加动态验证与徽章回填，两层各司其职。

- **三者齐备判定**：sink × source × entry 缺一不立，配合六问强制反驳，每条发现
  强制带证据链（逐跳 file:line）；
- **每条发现都可复现**：影响分析 + 触发前置条件 + PoC，按漏洞类型分派形态；
- **两轴定级**：危害 × 可达性，外加部署形态 × 风险面矩阵；
- **诚实三级验证**：live-prove / trigger-prove / code-proof + 证伪。判定 ≠ 验证，
  未实测绝不冒充；
- **可进 CI**：`report --sarif out.sarif --fail-on high`——SARIF 2.1.0 导出与
  严重度门禁退出码；误报不进结果，同账本导出字节稳定。

---

## 快速开始

前提：Node.js ≥ 22.19（唯一系统依赖，内嵌 Agent 运行时 pi 的硬性要求）。
init 自动拉取其余运行时（pi + OpenGrep，后者带 SHA-256 校验）。

### ① 首选：交给工作台 Agent 跑

**一次性**，复制这句话给你的 coding agent（pi 等），配置 + 安装 fiora 审计
skill 一把到位（幂等，已装则跳过）：

```
阅读并执行 https://raw.githubusercontent.com/Ryze-T/fiora/main/docs/SETUP.md，把 fiora 配置到可用状态。
```

**之后每次审计，直接说**（skill 已常驻 Agent 的 skills 目录，触发词自动接管）：

```
审计 <仓库路径>
```

审计由 SKILL.md 的调用章 + 验证章契约兜底，Agent 自己走完闭环：

```
fiora init → fiora run（扫描 + 判定 + 报告）
→ 审报告，按 verificationChecklist 起 docker 环境验真值（canary 无害化）
→ fiora verify record 回填（live-prove / trigger-prove / code-proof / disproved）
→ 交付报告 + 验证徽章 + 验证终表
```

换了机器 / skill 没装时，直接让它现读也行：
`阅读并执行 https://raw.githubusercontent.com/Ryze-T/fiora/main/SKILL.md，审计 <仓库路径>`；
网络受限则把对应文档内容粘给 Agent。

### ② 或者：手动安装 + 纯 CLI（无 Agent）

```bash
# 安装二进制（静态链接，解压即用；四平台见 Releases 页）
curl -fsSL https://github.com/Ryze-T/fiora/releases/latest/download/fiora-macos-arm64.tar.gz | tar xz
export PATH="$PWD/fiora-macos-arm64:$PATH"   # linux-x64 / linux-arm64 / macos-x64 同理
# 或从源码：cargo build --release && export PATH="$PWD/target/release:$PATH"
# 私有 fork/镜像分发需鉴权下载，用法见 docs/USAGE.md「安装」

cd <你的仓库>
fiora init --model openai/gpt-5.5 --api-key sk-xxx
fiora run            # 深度永远全量；--severity high|all 调范围（默认 high）
open fiora-report/report.html
```

10 分钟教程 → [docs/TUTORIAL.md](docs/TUTORIAL.md) · 命令全集 → [docs/USAGE.md](docs/USAGE.md)

---

## 图解

| fiora run 全流程 | 架构分层 |
| :---: | :---: |
| ![全流程：双通道候选 → 证据装配 → AI 判定 → 链组装 → 报告，Agent 动态验证后回填](assets/pipeline.png) | ![架构分层：责任分工、L1–L5 引擎分层与产物](assets/architecture.png) |

报告是单文件 HTML：离线可开、可转发。暗色主题 · 左侧目录 · 自动统计仪表盘 ·
mermaid 攻击链 · 发现↔PoC 双向跳转 · 一键复制复现包 · 验证徽章三级。
**完整示例 → [docs/demo-report.html](docs/demo-report.html)**

```
执行摘要 → 风险总览仪表盘
→ 一、RCE 风险链路分析（最高优，🔴 直接 RCE / 🟠 升级路径 / ⛓ 利用链）
→ 二、其余风险链路分析（速览表 + 详情卡 + 负向结论可审计）
→ 三、风险复现与 PoC（前置条件 / 步骤 / 预期 vs 实际 / 实测徽章）
→ 四、方法说明与覆盖率（含 部署形态 × 风险面 矩阵）
```

---

## 工作原理

**责任三分**：工具·查全（规则通道是下限，同类工具能挖的必须全挖到）；
AI·判准（六问强制反驳 + 对抗复验）；Agent·验实（起环境动态验证，结论经
`fiora verify record` 回填）。判定只给到 code-proof，live/trigger 级必须由
Agent 实测跑出来。

**引擎 L1–L5 分层**（每层可单独调用）：

```
fiora-cli ─┬─ fiora-core      状态账本 · 调度 · 配置/凭据
           ├─ fiora-scanner   L1 候选生成：87 条三级规则 + 语义探索
           ├─ fiora-evidence  L2 证据装配：调用链 2–3 跳回溯 · 入口面锚定
           ├─ fiora-processor L3 判定与链：项目画像 · 六问反驳 · 对抗复验 · 漏洞链
           ├─ fiora-verify    L4 验证口：补丁差分 · 验证结论回填
           ├─ fiora-report    报告渲染（模板契约锁定版式）
           └─ fiora-eval      L5 评测回归：recall / precision / 每真洞成本
```

状态账本 `.fiora/` 随仓库走，可增量、可复跑。扩展点（加规则 / 换 prompt /
换 Agent 运行时 / 换报告版式）见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

---

## 能力

| 能力 | 命令 | 说明 |
|---|---|---|
| 全量审计 | `fiora run` | 双通道候选（规则 + 语义探索）→ 证据 → 判定 → 链 → 报告；默认只展示高危及以上 |
| 语义深挖（0day 狩猎） | `fiora explore` | 排除已覆盖路径的自我挖掘：plan/execute 分离 + 多轮深挖回路，线索落 `.fiora/hunt.md` |
| **组合狩猎** | `fiora compose` | 把单点安全的发现组合成 super-0day（A+B 成链 / C 破保证） |
| 项目画像 | `fiora profile` | 模型读仓库提取画像 + 历史 CVE 模式 + 狩猎重点，注入判定/探索 |
| 确定性补丁差分 | `fiora verify diff` | pre/post 修订 shape 对照：fixed / persisting / regressed |
| **验证结论回填** | `fiora verify record` | Agent 实测后写回真值：live / trigger / code-proof / disproved |
| 能力族座次 | `fiora family` | RCE/SSRF/AWF 族聚合 + 可达性档位排序（还有哪些 / 哪些无条件） |
| 复现材料起点 | `fiora lab scaffold` | 实验室脚手架（真代码 + 桩化 + canary + 正控），Agent 适配后执行 |
| **多模型档位** | `fiora models` / `--profile` | 模型池 + 运行档位：配置多个模型，跑时一键切组合 |
| 评测回归 | `fiora eval` | recall / precision / 每真洞成本，改动必须不掉分 |
| 规则资产 | `fiora rules` | 三级规则库（builtin < 用户 < 项目），Semgrep YAML，改数据不重编译 |
| 报告精修 | `fiora enrich / refine / localize` | 补影响+PoC / 短句精炼 / 中文化 |

**使用模式**：Agent 工作台是首选（读 SKILL.md 全自动：审计 + 起环境验真值 +
回填徽章）；纯 CLI 适合日常审计、CI 门禁与批量扫描（`fiora run` 全自动出报告）。

---

## 开发

```bash
cargo test          # 158 测试（含报告模板契约测试）
cargo clippy --all-targets   # 0 告警门禁
fiora eval --corpus corpus --rule-only   # 下限门禁：规则通道 recall 100%（零模型，可进 CI）
# 全链基线（双冷跑）见 CHANGELOG：recall 36/36、precision 86%，改动不得低于基线
```

- CI：ubuntu + macos 双平台 + cargo-audit；
- 改报告版式：先改 [docs/REPORT-TEMPLATE.md](docs/REPORT-TEMPLATE.md) 规范，
  契约测试锁结构；
- Agent 行为契约：[SKILL.md](SKILL.md)；安全问题请走
  [SECURITY.md](SECURITY.md) 私有披露；贡献指引 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 已知边界（诚实声明）

- **环境验证归 Agent**（产品定位）：fiora 不启动环境、不执行 PoC，验证后
  `verify record` 回填（方法论见 SKILL.md 验证章）；
- 所有视图**默认只展示高危及以上**（`--severity all` 显式放开）；低危仍落账；
- pi 是**内嵌执行器**（实现细节）：产品表面全部经由 fiora（含审计轨迹），
  无需接触执行器；
- 模型协议执行归 pi 运行时：多模型/多协议（openai-completions /
  openai-responses / anthropic-messages / google-generative-ai 等）是 pi 的契约面，
  fiora 只负责 models.json 路由 + 凭据注入；协议猜测表不准时用 `--api` 覆盖；
- **运行时自举带钉值校验**：opengrep 下载按源码内钉死的 SHA-256 逐字节校验
  （官方只发 cosign `.sig/.cert`，强校验可 `cosign verify-blob`）；不符即拒装；
- **跨版本账本注意**：0.x 调整过一次 finding 身份推导（含类别归一）。旧账本与
  新版二进制混用重跑会给同一发现生成新 id，追加语义下表现为重复条目；
  升级大版本建议整账本重跑，或等 1.0 的迁移器；
- Windows 走 WSL；异构栈泛化经验见 ROADMAP.md；ARVO 语料导入、分布式
  executor 在路线图上。

---

<div align="center">

⭐ 觉得有用就点个 Star，这直接决定我们投入多少精力维护规则语料。
踩到规则盲区的话，欢迎用 `fiora draft-rules` 起草规则回馈回来。

**License：Apache-2.0**

</div>
