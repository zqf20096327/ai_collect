[English](README.en.md) | **中文**

<p align="center">
  <img src="assets/banner.png" alt="写作风格炼金术 · Style Alchemy" width="100%">
</p>

# 写作风格炼金术 · Style Alchemy

![License](https://img.shields.io/badge/license-MIT-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-8A2BE2)
![Status](https://img.shields.io/badge/status-alpha-orange)
![Made with](https://img.shields.io/badge/made%20with-Python%20%2B%20YAML%20%2B%20Markdown-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

> **写作风格炼金术（Style Alchemy）是一个 [Claude Code](https://claude.com/claude-code) skill** —— 把一批文章样本自动炼化成可复用的写作风格档案，并生成一个按该风格写作的专属 Claude skill。

不只是写一段提示词 —— 而是把"风格"沉淀成**可编辑、可迁移、可校验**的结构化资产。

适用于任意中长文样本：博客、公众号、知乎、小红书、Twitter/X、学术期刊、个人散文……

### 输入 / 输出

```
输入：5-15+ 篇文章样本（.md / .txt / .html）

输出：
  1. <作者>风格分析报告.md     人读的深度报告（标题术、动词库、节奏、语气色板…）
  2. style_profile.yaml         机器读的结构化风格档案
  3. write-as-<id> Claude skill 一键生成的专属写作助手（可选）
```

---

## 这是什么

"风格"是个模糊的词 —— 你能感受到某个作者的文字"对味"，却没法直接复用。本 skill 做三件事：

1. **拆解** —— 把"风格"拆成 5 个通用维度（标题/开篇/节奏/语言/结尾）+ 若干场景增量维度（公众号/知乎/小红书…），每个维度都用样本原文做例证。
2. **固化** —— 把拆解结果浓缩成一份 `style_profile.yaml` 风格档案，机器可读、可编辑、可融合。
3. **再造** —— 把档案变成一个独立的 `write-as-<id>` skill，下次你需要按这种文体写作时直接调用。

---

## 适用场景

- **内容创作者**：研究公开文本的写作特征，沉淀自己的写作工具箱
- **公众号 / 自媒体团队**：拆解标杆账号的内容结构，建立团队风格规范
- **法律 / 学术写作**：把某种文体（如判决书摘要、学术摘要、研究综述）固化成可复用的写作助手
- **企业品牌方**：把 brand voice / tone guideline 编译成可执行的 skill，而不是一份永远没人看的 PDF
- **AI / Agent 开发者**：把"写作风格"作为可移植的资产 —— 一份 yaml 走天下
- **文体迁移研究**：同一个人在公众号和知乎的写法差异，可以分别建档对比

> ⚠️ **使用边界**：本工具用于提炼公开文本的写作特征以辅助创作或研究。生成内容若涉及商业用途、公开发布、或与在世真人/特定品牌产生混淆可能，请自行评估姓名权、商标、反不正当竞争等合规风险。Roadmap 中规划了"相似度检查"功能以辅助去重。

---

## Quick Start

### 1. 安装

把仓库 clone 到 Claude Code 的 skills 目录：

```bash
# Linux / macOS
cd ~/.claude/skills
git clone https://github.com/snowmays/style-alchemy.git

# Windows (PowerShell)
cd $env:USERPROFILE\.claude\skills
git clone https://github.com/snowmays/style-alchemy.git
```

> 也可以下载 zip 解压到 `~/.claude/skills/style-alchemy/`。

### 2. 准备样本

把目标作者的文章放到任意文件夹（支持 `.md` / `.txt` / `.html`）：

```
my_workspace/
└── raw/
    ├── article1.md
    ├── article2.html
    ├── article3.txt
    └── ...
```

样本数建议：

| 样本数 | 能做什么 |
|--------|----------|
| 5-9 篇 | 🟡 风格速写（不建议生成写作 skill） |
| 10-14 篇 | 🟢 标准分析 |
| 15+ 篇 | 🟢🟢 深度分析 + 生成写作 skill |

### 3. 启动 skill

在 Claude Code 里说人话即可：

```
分析 ./raw 里这些文章的写作特征，最后帮我生成一个同款文体的写作 skill。
```

Claude 会先跟你确认参数（路径、作者、平台、交付目标），然后按 9 步工作流执行：

```
[0] 接案确认  →  [1] 归一化样本  →  [2] 场景识别  →  [3] 素材分类
                                                          ↓
[8] 一键生成写作 skill ← [7] 对比分析 ← [6] 写报告+yaml ← [5] 场景增量维度 ← [4] 通用 5 维
```

### 4. 拿到产物

```
my_workspace/
├── raw/                           # 你给的原始素材（不动）
├── samples_normalized/            # 归一化后的统一格式样本
│   ├── 001-xxx.md
│   └── ...
├── 量子位风格分析报告.md            # 人读的深度报告
└── style_profile.yaml             # 机器读的风格档案

~/.claude/skills/
└── write-as-qbitai/               # 一键生成的新 skill（可选）
    ├── SKILL.md
    └── references/style_profile.yaml
```

之后任何对话里说"按这个风格写一篇关于 X 的文章"（或直接 `@write-as-qbitai`），新 skill 会自动触发。

---

## How it works

### 整体流程

```
        原始素材 (md / txt / html)
                │
                ▼
        [1] 归一化  ──→  scripts/normalize_samples.py
                │        统一 frontmatter + 极短句保留 + 噪音剔除
                ▼
        [2] 场景识别
                │  公众号 / 知乎 / 小红书 / Twitter / 博客 / 学术 / 散文 / 其他
                ▼
        [3] 通用 5 维 分析  ──┐
                │            │  标题术 / 开篇 / 节奏 / 语言 / 结尾
        [4] 场景增量维度  ──┤
                │            │  平台特有规则
                ▼            ▼
              ┌─────────────────────┐
              │  双产物             │
              │  ├─ 报告.md (人读)  │
              │  └─ profile.yaml    │
              └────────┬────────────┘
                       │ 可选
                       ▼
              [5] 一键生成 write-as-<id> skill
```

### 为什么要 yaml 中间产物？

`style_profile.yaml` 是本 skill 的"灵魂"。所有可量化的风格特征（标题公式、动词库、语气色板、口头禅、节奏模式…）都按标准 schema 落到这份 yaml。

**好处**：

- **人机分离** —— 报告给人读，yaml 给机器读，各司其职
- **人工可修** —— 分析难免有偏差，你可以编辑 yaml 修正某个字段再生成 skill
- **可融合** —— 把两份 yaml 合并 = 风格 A 60% + 风格 B 40%（roadmap）
- **可评估** —— 拿新写的稿子对照 yaml 算"风格匹配度"（roadmap）

完整 schema 见 [`references/style-profile-schema.md`](references/style-profile-schema.md)。

### 通用 5 维 + 场景增量维度

不同平台的写作"长得"完全不一样，但底层"语言肌理"是共通的。本 skill 这样分层：

**通用 5 维**（任何文章都跑）：
- 标题术（信息密度、标点策略、情绪词库、公式提炼）
- 开篇手法（钩子类型、第一句字数、人称偏好）
- 段落节奏（长短分布、极短句频率、图片节奏）
- **语言风格**（动词库 ×20+、语气色板、标点叙事、口头禅、自创词典）
- 结尾模式（类型分布、固定 CTA）

**场景增量维度**（按平台动态启用）：

| 场景 | 增量维度 |
|------|---------|
| 公众号 | 版头/版尾、社群命名、固定栏目、CTA 位置 |
| 知乎 | 答题开局策略、资历展示、辩论姿态 |
| 小红书 | emoji 密度、标签策略、人设植入、极短行 |
| Twitter/X | 推文串策略、单推句数、转推用法 |
| 严肃博客 | 论证结构、引用风格、段落长度 |
| 学术 | 引用格式、保留语密度、术语密度 |
| 个人散文 | 意象密度、感官词分布、时间处理 |

详见 [`references/analysis-framework.md`](references/analysis-framework.md)。

---

## 输出示例

### 分析报告片段（节选）

```markdown
## 五、语言风格深度拆解

### 5.1 动词选择

| 中性表达 | 该账号常用替代 | 强度 | 极性 |
|---------|---------------|------|------|
| 发布 | 炸出 / 甩出 / 放大招 | 5 | 正面狂热 |
| 批评 | 锤 / 喷 / 开怼 | 5 | 负面 |
| 很受欢迎 | 全网炸锅 / 直接封神 | 5 | 正面 |
| 失败 | 翻车 / 凉凉 | 4 | 负面调侃 |

> 原文例证："OpenAI 又炸出一个新模型" —— 用"炸出"替代"发布"，能量密度立刻起来。
```

### 风格档案片段

```yaml
schema_version: "1.0"
profile_id: qbitai
display_name: 量子位
sample_count: 15
sample_platforms: [公众号]

portrait: |
  量子位是一个以"硬核 AI 资讯 + 强烈情绪化语言"为特色的科技自媒体。
  标题信息密度极高，开篇必带震惊感，段落节奏快、极短句频繁。
  动词偏好"力量型"，语气在调侃和震惊之间快速切换。

title_craft:
  avg_length: 28
  info_density: high
  formulas:
    - id: f1
      pattern: "[主体]+[反常识动作]，[情绪反应]！"
      example: "OpenAI 收购 Astral，Python 包管理神器 uv 现在姓 O 了"
      when_to_use: 突发新闻、产品发布

language_style:
  power_verbs:
    - { verb: 炸出, replaces: 发布, intensity: 5, polarity: positive }
    - { verb: 锤,   replaces: 批评, intensity: 5, polarity: negative }
  signature_phrases:
    - { phrase: "怎么说呢", context: 引出评论 }
    - { phrase: "属实",    context: 强调判断 }

# ... 完整字段见 references/style-profile-schema.md
```

---

## 项目结构

```
style-alchemy/
├── SKILL.md                          # skill 主入口（Claude 读这个）
├── scripts/
│   └── normalize_samples.py          # 归一化脚本（md/txt/html → 统一 md）
├── references/
│   ├── sample-format.md              # 归一化样本格式定义
│   ├── analysis-framework.md         # 通用 5 维 + 场景增量维度方法论
│   ├── style-profile-schema.md       # yaml 风格档案 schema
│   └── writing-skill-template.md     # 写作 skill 生成模板
├── README.md                         # 你正在看的文件
├── README.en.md                      # 英文版
└── LICENSE                           # MIT
```

---

## Roadmap

- [ ] **原文相似度检查** —— 生成内容 vs 样本的去重比对，避免输出与样本出现高重合表达（合规 + 原创性双重保障）
- [ ] **URL 批量抓取** —— 给一个链接列表就能自动建样本（支持公众号/知乎/博客的优先级）
- [ ] **yaml schema 自动校验** —— 写完档案跑一遍 lint，避免占比不归一、字段缺失等
- [ ] **风格融合** —— 合并多个 yaml 生成混合文体 skill（"风格 A 60% + 风格 B 40%"）
- [ ] **docx / pdf 归一化** —— 当前需要先手动转 md
- [ ] **风格匹配度评估** —— 拿新稿子对照档案打分，看是否符合目标文体
- [ ] **更多场景增量维度** —— B 站文章、Substack、Newsletter、Reddit

---

## 贡献

欢迎 PR / Issue。特别欢迎的方向：
- 新的场景增量维度（如果你研究过某个垂直领域的写作风格）
- 归一化脚本支持更多输入格式
- 真实风格档案样例（脱敏后贡献到 `examples/`）

---

## License

[MIT](LICENSE) © snowmays

风格档案 yaml 和生成的写作 skill 归 **你自己** 所有 —— 本仓库只提供工具，不主张对你产出的档案有任何权利。
