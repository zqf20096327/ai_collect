# 产品经理竞品分析 Skill

`analyze-product-competitors` 是一个面向产品经理的 Codex Skill，用于对指定竞品或功能领域进行基于证据的产品分析。它从目标用户、核心场景和关键任务出发，比较产品能力、使用体验、定价包装与产品定位，并将差异转化为可验证的产品机会假设。

## 核心能力

- **完整竞品对比**：比较指定产品的用户、场景、任务、能力、体验、定价和定位。
- **单一功能拆解**：分析功能入口、配置成本、核心流程、能力边界和完成质量。
- **产品体验拆解**：比较首次使用、Time-to-Value、任务路径、反馈、容错和效率。
- **定价包装分析**：比较计费单位、套餐、额度、功能门槛、试用与实际使用成本。
- **定位分析**：比较目标用户、用户问题、品类、价值主张、差异化表达和证明材料。

这个 Skill 不用于市场格局扫描、销售赢单或丢单分析、销售话术、竞品监控或产品路线图制定。

## 分析特点

- 从用户任务建立比较维度，不按功能数量判断产品优劣。
- 区分“强、可用、弱、缺失、未知、不适用”，避免把没有证据误判为没有功能。
- 优先使用实际产品体验和官方一手资料，并记录来源、日期与可信度。
- 如实呈现竞品优势，同时识别基础能力、体验、包装、定位和差异化机会。
- 不直接照抄竞品功能，而是形成包含用户影响和待验证问题的产品机会假设。

## 目录结构

```text
.agents/skills/analyze-product-competitors/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── comparison-frameworks.md
    ├── output-template.md
    └── research-and-evidence.md
```

## 安装

### 项目级安装

将 Skill 目录复制到目标项目：

```bash
mkdir -p /path/to/project/.agents/skills
cp -R .agents/skills/analyze-product-competitors /path/to/project/.agents/skills/
```

项目级安装只在对应项目及其子目录中生效，适合团队随仓库共享。

### 用户级安装

将 Skill 目录复制到用户技能目录：

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/analyze-product-competitors ~/.agents/skills/
```

用户级安装可在该用户的不同项目中使用。如果 Codex 没有立即识别新 Skill，请重启 Codex。

## 使用方式

### 显式触发

在提示词中使用 Skill 名称：

```text
$analyze-product-competitors 对比 Notion AI 和飞书智能伙伴的知识问答功能
```

### 自然语言触发

Skill 的描述包含“帮我做竞品分析”，因此也可以直接输入：

```text
帮我做竞品分析，对比 Cursor 和 Windsurf 的首次使用体验。
```

当请求明确匹配完整竞品对比、功能拆解、体验拆解、定价包装或定位分析时，Codex 也可以自动选择该 Skill。显式写出 `$analyze-product-competitors` 最可靠。

## 推荐输入模板

```text
$analyze-product-competitors

我方产品：<可选，如需识别我方差距>
竞品：<至少一个明确竞品>
目标用户：<用户角色或细分群体>
核心场景：<用户需要完成的任务>
分析模式：<完整对比 / 功能 / 体验 / 定价包装 / 定位>
重点问题：<本次最需要回答的问题>
地区与平台：<市场、设备、版本或套餐>
资料截止日期：<日期>
```

示例：

```text
$analyze-product-competitors

竞品：Notion AI、飞书智能伙伴
目标用户：需要检索团队知识的产品与运营人员
核心场景：从多份内部文档中获得有来源的答案
分析模式：单一功能拆解 + 产品体验拆解
重点问题：回答质量、引用溯源、权限边界和首次配置成本
地区与平台：中国大陆，Web 端
```

## 输出内容

Skill 会根据请求裁剪输出，完整结构包括：

1. 结论摘要
2. 分析范围与证据说明
3. 用户场景与关键任务
4. 竞品对比表
5. 关键差距与产品机会
6. 待验证假设与下一步研究
7. 局限、未知项和来源

## 证据原则

资料优先级如下：

1. 相同任务下的实际产品体验
2. 官方产品页、帮助中心、开发文档、定价页和更新记录
3. 应用商店、评论网站、社区讨论和用户反馈
4. 可信第三方测评、媒体和行业资料

营销文案只能证明产品声称具备某项能力，不能单独证明实际能力质量。无法访问的功能会标记为“未知”，不会直接判定为“缺失”。

## 主要文件

- [`SKILL.md`](.agents/skills/analyze-product-competitors/SKILL.md)：触发范围、执行流程和质量检查。
- [`comparison-frameworks.md`](.agents/skills/analyze-product-competitors/references/comparison-frameworks.md)：五种分析模式、评分规则和差距分类。
- [`research-and-evidence.md`](.agents/skills/analyze-product-competitors/references/research-and-evidence.md)：来源优先级、研究记录与可信度规范。
- [`output-template.md`](.agents/skills/analyze-product-competitors/references/output-template.md)：标准报告结构与对比表模板。
- [`openai.yaml`](.agents/skills/analyze-product-competitors/agents/openai.yaml)：Codex UI 展示信息与默认提示词。
