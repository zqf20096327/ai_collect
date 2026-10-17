# AI Data-Analyst Agent — 方法论 + 模板

> 🌐 Language: **中文** · [English](README.en.md)

一套把「数据分析师」工作流固化进 AI agent（Claude Code / Cursor / 任意支持 system prompt + skill 的 harness）的方法论与可复用模板。

这个仓库**不包含任何业务数据、内部表名、口径或个人信息**。它开源的是「骨架」——让一个 AI agent 做数据分析时**可信、可追溯、随用随长**的机制；业务「填充」（你的表、你的指标口径、你的踩坑库）由你按模板自己积累。

---

## 为什么是这三件事

大多数人给 agent 写 prompt 是「告诉它怎么做」。真正让数据 agent 可用的，是三个工程化机制：

### 1. 口径先行（Metric Store / 语义层）
出任何一个数比口径定义优先。指标只有**单一权威定义**，agent 出数前先查 registry，而不是凭对话上下文临时拼。
→ `methodology/metric-store.md`

### 2. 独立校验（Self-assessment is unreliable）
agent 自己写的 SQL / 报告，**不能自己判断对不对**。校验必须交给一个**物理只读、无写权限、独立加载规则**的 validator agent。这条直接对应 Anthropic 的 harness 设计原则：自评有偏差，验证必须分离。
→ `skills/data-validator/`

### 3. 随用随长的规则库（Correction → Rule）
每被纠正一次错误，就**追加一条带编号的规则**，下次自动命中。规则库不是一次写死，而是随着踩坑单调增长。配合「覆盖盲区检测」——每次校验都主动报告「规则库没覆盖的新场景」让人决策是否沉淀。
→ `skills/data-validator/SKILL.md` 的维护机制

外加一条贯穿全程的产出纪律：

### 4. 数据溯源 Footer（Provenance）
每个交付的数字都要能回答「口径来自哪一层、数据多新、源表是什么、谁校验的」。
→ `methodology/provenance-footer.md`

---

## 仓库结构

```
.
├─ README.md                          # 本文件
├─ persona/
│  └─ CLAUDE.template.md              # 数据 agent 人设 + 方法论框架模板（全占位符）
├─ skills/
│  └─ data-validator/
│     ├─ SKILL.md                     # 独立校验 agent 框架（可直接用）
│     └─ rules/
│        ├─ INDEX.md                  # 规则总索引 + 编号约定 + 严重等级
│        ├─ sanity-check.md           # 通用：SQL 结果合理性（与业务无关）
│        ├─ abtest-rules.md           # 通用：AB 实验方法论 + 显著性检验
│        ├─ report-style.md           # 通用：分析报告写作纪律
│        ├─ _TEMPLATE.md              # 规则模板：教你怎么加自己的规则
│        └─ examples/
│           ├─ field-trap.example.md  # 1 条脱敏示例（字段坑类）
│           └─ domain-metric.example.md # 1 条脱敏示例（业务口径类）
└─ methodology/
   ├─ metric-store.md                 # 口径先行 / 语义层设计
   └─ provenance-footer.md            # 数据溯源 footer 规范
```

---

## 怎么用（落地三步）

1. **填人设**：复制 `persona/CLAUDE.template.md` 成你的 `CLAUDE.md`，把 `{{...}}` 占位符替换成你自己的身份/产品/工具。
2. **装校验**：把 `skills/data-validator/` 整个搬进你的 agent skill 目录。通用规则（sanity / abtest / report-style）开箱即用；业务规则（字段坑、口径）按 `_TEMPLATE.md` + `examples/` 自己积累。
3. **建口径**：照 `methodology/metric-store.md` 给你最常用的 5–10 个指标建 registry，出数前强制查。

---

## 这个仓库刻意**不给**什么

- **不给具体表名 / 字段名 / 库名** —— 这些是你的数仓资产，用占位符 `<your_fact_table>` 代替。
- **不给业务口径** —— 收入怎么算、留存怎么定义，每家不同。给的是「口径要单一权威」这个机制和模板。
- **不给已踩过的具体坑** —— 字段坑、ETL bug 回归这些是高度业务相关的；给的是「踩坑后怎么固化成规则」的格式（`_TEMPLATE.md`）和 1 条脱敏示例。

换句话说：你抄走的是方法论和骨架，不是别人的表。

---

## License

MIT。随便用、改、商用，出问题自己负责。
