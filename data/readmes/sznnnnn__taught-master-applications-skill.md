<div align="center">

# Study Abroad Applications Skill

![GitHub stars](https://img.shields.io/github/stars/sznnnnn/taught-master-applications-skill?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Skill](https://img.shields.io/badge/Skill-Agent-111111?style=flat-square)
![Agent](https://img.shields.io/badge/Agent-Supported-222222?style=flat-square)
![Local First](https://img.shields.io/badge/Local--first-Application%20OS-2D6CDF?style=flat-square)
![Bilingual](https://img.shields.io/badge/Bilingual-中文%20%2B%20English-2F8F5B?style=flat-square)

一个中英文可用、本地优先的留学申请工作流 Skill：选校、申请画像、Evidence map、SOP/PS/CV、时间线、申请追踪和 application pack。

当前最完整路线：**授课型硕士申请**。同时支持 undergraduate、research master、PhD、offer comparison 的轻量分流。

![留学申请工作流 Skill 封面](assets/readme/hero.svg)

![30 秒工作流演示](assets/readme/demo.gif)

[30 秒开始](#30-秒开始) · [效果示例](#效果示例) · [核心能力](#核心能力) · [路线分流](#路线分流) · [安装](#安装) · [Examples](#examples) · [信息来源边界](#信息来源边界)

</div>

---

## 30 秒开始

装好后直接对 Agent 说：

```text
帮我规划 2027 Fall 留学申请
```

或者用英文：

```text
Help me plan my 2027 Fall study abroad applications.
```

或者更具体一点：

```text
我不确定该申请授课硕、research master 还是 PhD，先帮我做 route triage。
```

Skill 的第一轮不会问长问卷。它会先给一版可用计划，标出 `已知 / 假设 / 待确认`，再只问一个关键问题。

默认会跟随用户语言输出：中文提问用中文规划，英文提问用英文规划。SOP / PS / CV / motivation letter 等正式申请材料可以按目标学校要求切到英文。

## 效果示例

```text
用户  ❯ 我想申请 2027 Fall，方向可能是 HCI / UX / AI design，但不确定。

Skill ❯ Route Triage
        - Likely route: Taught Master's
        - Why: 你提到的是专业型/跨学科 master 方向
        - What this changes: 先做 Evidence map，再做项目池和文书策略

        First Plan
        已知：2027 Fall；HCI / UX / AI design
        假设：先按授课硕处理
        待确认：目标地区、当前背景、材料来源

        我先只确认一个问题：
        你想优先看英国/港新/欧洲/澳洲/北美，还是先全部开放搜索？
```

```text
用户  ❯ 我已经有几个 offer，帮我比较去哪一个更值。

Skill ❯ 切换到 Offer Comparison
        - 不继续做选校搜索
        - 比较 cost / curriculum / career / visa-work route / deposit deadline
        - 标出不可逆 deadline 和待官网确认项
```

## 为什么做这个 Skill

多数申请卡住，不是因为少一个提示词，而是这些东西散落在不同地方：

- 背景资料：成绩、语言、预算、地区、经历、项目、材料状态
- 项目信息：官网要求、deadline、学费、语言、文书、作品集
- 申请判断：值不值得申、风险在哪里、下一步做什么
- 执行进度：文书、CV、推荐信、portfolio、提交状态

这个 skill 的目标是把它们连成一条可检查、可更新、可导出的申请线。

```text
Route -> Profile -> Evidence map -> Program pool -> Documents -> Timeline -> Tracker -> Application pack
```

它现在按一个轻量 Application OS 来设计：申请画像、证据地图、项目池、文书计划、时间线和 application pack 会互相联动。上游信息变化时，skill 会提醒哪些下游材料需要刷新，而不是让每次对话变成孤立答案。

![申请工作流地图](assets/readme/workflow-map.svg)

## 核心能力

| 模块 | 它会产出什么 |
|---|---|
| Bilingual workflow | 中文规划、英文申请材料、双语对照表 |
| Route triage | 判断本科、授课硕、研究型硕士、PhD、offer comparison 该走哪条逻辑 |
| 本地资料表 | 一份可填写的 Markdown intake，减少来回问答 |
| 申请画像 | 方向、地区、预算、GPA、语言、材料状态、风险点 |
| Evidence map | 把课程、项目、实习、research、writing sample、portfolio 转成申请证据 |
| 项目筛选 | longlist / shortlist / A-B-C 优先级、官网链接、风险、下一步 |
| 文书策略 | SOP、PS、motivation letter、study plan、CV、推荐信素材 |
| CV 生成工作流 | 从通用模板、证据地图到项目定制 CV，支持隐私安全版本 |
| 时间线 | 按 deadline 倒排每周任务，区分官网截止和内部截止 |
| Tracker | 本地 Markdown / CSV / Notion-ready 申请追踪表 |
| Agent-ready pack | 为后续网申辅助准备官网入口、材料清单、表单字段和人工确认点 |

## 低门槛入口

你可以先填一份本地资料表。空白和“不确定”都可以保留，skill 会把缺口变成下一步任务，而不是继续追问十几轮。

![从资料表到申请输出](assets/readme/intake-to-output.svg)

也可以直接对话式开始：

```text
帮我规划 2027 Fall 留学申请
```

Skill 会先给两个入口：

1. 生成本地 Markdown 资料表，推荐
2. 继续对话式一步步问

## 路线分流

| Route | 适合什么时候 | 核心输出 |
|---|---|---|
| Undergraduate | UCAS / Common App / foundation / bachelor | activity/evidence map, school list, essay plan, deadline tracker |
| Taught Master's | MSc / MA / MDes / MFA / MEd / MPP / professional master's | program scout, SOP/PS/CV strategy, tracker, application pack |
| Research Master's | MRes / MPhil / proposal / thesis route | research fit brief, proposal plan, supervisor/program shortlist |
| PhD | supervisor / PI / lab / funding / doctoral application | ability network, PI/lab fit, funding checks, outreach plan |
| Offer Comparison | 已经拿到 offer，需要做选择 | cost, curriculum, career, visa/work route, risk, deposit deadline |

当前最成熟的是 **Taught Master's**。其他 route 的目标是先把逻辑分清，不把不同申请系统混成一锅。

## 会产出什么

一次完整使用后，它通常会产出这些内容：

- 申请画像：你的方向、优势、风险、材料缺口
- Route triage：本科 / 授课硕 / 研究型硕士 / PhD / offer comparison 的分流判断
- Evidence map：哪些经历能支撑哪些申请方向
- 项目表：longlist / shortlist / A-B-C 优先级
- 文书策略：每个项目的 SOP/PS 角度和证据选择
- CV 工作流：生成通用模板、申请基础版、项目定制版或隐私安全版 CV
- 时间规划：本周、未来两周、关键 deadline 和内部截止
- 申请追踪：材料状态、owner、风险、下一步
- Application pack：单个项目的材料清单、官网链接、文书提示和提交前检查

![证据驱动的申请包](assets/readme/evidence-pack.svg)

## 安装

### 方式一：把这句话发给 AI Agent

```text
帮我安装这个 skill：https://github.com/sznnnnn/taught-master-applications-skill
```

### 方式二：手动安装到本地 skills 目录

下面以 `~/.codex/skills` 为示例路径；如果你的 Agent 使用其他 skills 目录，把目标路径替换掉即可。

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/sznnnnn/taught-master-applications-skill.git /tmp/study-abroad-applications-skill
cp -R /tmp/study-abroad-applications-skill/taught-master-applications ~/.codex/skills/
```

如果你已经在本仓库根目录：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/taught-master-applications
cp -R taught-master-applications ~/.codex/skills/
```

重启你的 AI Agent / CLI 工具后即可使用。

## 推荐用法

### 从零开始

```text
帮我规划 2027 Fall 留学申请。目前方向还不确定，可能是 HCI / UX / AI design / education technology。
```

```text
Help me plan my 2027 Fall study abroad applications. I am considering HCI, UX, AI design, or education technology.
```

### 先判断路线

```text
我不确定该申请授课硕、research master 还是 PhD，先帮我做 route triage。
```

### 已有项目清单

```text
帮我比较这些授课硕项目，按 A/B/C 优先级给出申请策略、材料缺口和下一步。
```

### 比较 offer

```text
我已经有几个 offer，帮我按费用、课程、职业路径、签证/工作机会和风险做比较。
```

### 先整理经历

```text
我还不知道自己适合申请什么。先帮我把这些课程、项目、实习整理成 Evidence map。
```

### 准备文书

```text
帮我为这个项目做 SOP 策略，要求不要编经历，只用我已有材料。
```

```text
Help me create an SOP strategy for this program. Use only my existing evidence and do not invent experience.
```

### 生成申请 CV

```text
帮我生成一版授课硕申请 CV。先用通用 STEM 模板，不要暴露隐私，也不要编经历。
```

```text
Help me create a program-specific CV for this MSc. Use only verified evidence and show me the gaps first.
```

### 做时间线

```text
帮我按 2026-12-15 的 deadline 倒排申请任务，本周先做最小可执行计划。
```

## Examples

- [First run](examples/01-first-run.md)
- [Evidence map](examples/02-evidence-map.md)
- [Program scout](examples/03-program-scout.md)
- [Application pack](examples/04-application-pack.md)
- [Offer comparison](examples/05-offer-comparison.md)
- [CV generation preview](examples/06-cv-generation-preview.md)

## 输出示例

```markdown
## 今日结论

你现在更适合先用 Evidence map 确定 2-3 个申请方向，再做项目 longlist。当前最大风险不是项目数量，而是材料证据还没有被整理成清晰叙事。

## 快速决策表

| Fit | Program | Country | Key Materials | Deadline | Evidence Status | Checked At | Why |
|---|---|---|---|---|---|---|---|
| A | MSc Human-Computer Interaction | UK | SOP, CV, transcript, portfolio optional | 待官网确认 | 待官网确认 | 2026-05-30 | 与项目/设计/AI evidence 匹配 |

## Next Actions

- [ ] 2026-05-31 前整理 CV、成绩单、2-3 个项目材料
- [ ] 2026-06-02 前核查 A 类项目官网 deadline 和材料要求
- [ ] 2026-06-05 前完成第一版 SOP narrative spine
```

## 信息来源边界

Skill 会区分不同来源的可信度：

| 标签 | 含义 |
|---|---|
| `官网已核查` | 来自学校、项目、admissions、官方政策页 |
| `二级来源-仅参考` | 来自 student work、Issuu、Behance、Pinterest、小红书等 |
| `待官网确认` | 还没有在官方页面确认，不能当成最终要求 |

非官网内容只能用于表达参考、案例拆解和风险提醒，不能直接当成申请要求。

## 语言策略

| 场景 | 默认语言 |
|---|---|
| 申请规划、选校、时间线 | 跟随用户语言，中文或英文都可以 |
| Evidence map / tracker | 可中文、英文或双语对照 |
| SOP / PS / motivation letter / CV | 默认按学校要求输出英文，可保留中文 planning notes |
| 官网信息摘录 | 保留英文原意，必要时给中文解释 |
| 不确定性标签 | 中文场景用 `已知 / 假设 / 待确认`，英文场景用 `Known / Assumption / To Verify` |

## 适合 / 不适合

**适合**

- 正在申请或准备申请留学项目，尤其是授课型硕士
- 目标方向还不完全确定，需要先做定位
- 想比较英国、港新、欧洲、澳洲、北美等地区项目
- 需要整理 SOP / PS / CV / 推荐信素材 / portfolio / writing sample
- 希望资料优先保存在本地，只在需要时导出到 Notion 或表格

**不适合**

- 保证录取或预测精确录取概率
- 编经历、分数、奖项、项目成果或推荐信
- 替代官网核查 deadline、学费、语言和材料要求
- 把本科、授课硕、research master、PhD 的逻辑混在一起
- 代替用户完成最终网申提交、付款、法律声明确认或推荐信发送

## 文件结构

```text
taught-master-applications/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── templates/
│       ├── 授课硕申请资料表.md
│       ├── cv-template-stem.docx
│       ├── cv-preview-stem.md
│       └── academic-recommendation-letter-template.docx
└── references/
    ├── workflow-map.md
    ├── system-architecture.md
    ├── degree-routes.md
    ├── language-policy.md
    ├── cv-generation-workflow.md
    ├── recommendation-letter-workflow.md
    ├── profile-intake.md
    ├── evidence-map.md
    ├── output-schema.md
    ├── document-guidance.md
    ├── timeline-planner.md
    ├── execution-tracker.md
    ├── reference-scout.md
    └── agent-ready-pack.md
assets/
└── readme/
    ├── demo.gif
    ├── demo.mp4
    ├── demo.html
    ├── demo-storyboard.md
    ├── hero.svg
    ├── workflow-map.svg
    ├── intake-to-output.svg
    └── evidence-pack.svg
examples/
├── 01-first-run.md
├── 02-evidence-map.md
├── 03-program-scout.md
├── 04-application-pack.md
├── 05-offer-comparison.md
└── 06-cv-generation-preview.md
```

## 设计原则

1. **先给可用草稿**，再问一个关键问题
2. **事实分层**：`已知 / 假设 / 待确认` 分开写
3. **日期具体**：用 `2026-12-15`，不只说“下周”“这个月”
4. **建议可追溯**：每个建议都要追到用户证据、官网信息或待核查任务
5. **本地优先**：用户资料默认留在本机，Notion 只是可选导出
6. **不制造焦虑**：不承诺录取，不用中介式话术

## Roadmap

- Taught master's route: mature
- Undergraduate route: intake, essay, activity list, school-list strategy
- Research master's route: proposal and supervisor-fit support
- PhD route: ability network, PI/lab fit, funding checks, outreach plan
- Offer comparison route: cost, curriculum, visa/work path, career fit, deposit timing
- More import/export formats for local trackers and application packs
