# XHS Topic Strategist Skill

> 一个纯 Markdown、跨 Agent、无代码依赖的小红书智能选题策划 Skill。  
> 用轻量账号画像，把热点、赛道规则、选题评分和风险审查组织成可复用的内容策划包。

![Markdown Only](https://img.shields.io/badge/Markdown-Only-111111)
![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-2563eb)
![No Dependencies](https://img.shields.io/badge/No-Dependencies-16a34a)
![Xiaohongshu](https://img.shields.io/badge/Xiaohongshu-Topic_Planning-ff2442)
![MIT License](https://img.shields.io/badge/License-MIT-green)

[English README](README.en.md) · [快速开始](docs/QUICKSTART.md) · [使用场景](docs/USE_CASES.md) · [贡献指南](CONTRIBUTING.md) · [安全说明](SECURITY.md)

## 30 秒开始

1. 下载或 clone 本仓库。
2. 把整个文件夹交给 Claude、Codex、Cursor Agent、Manus、ChatGPT Agent 或其他能读取 Markdown 的 Agent。
3. 让 Agent 先读取 `SKILL.md`。
4. 填写 `templates/account_profile_template.md` 里的轻量账号画像表。
5. 让 Agent 输出 Top 5 小红书选题策划包。

最小调用 Prompt：

```text
请使用 XHS Topic Strategist Skill。
请先读取 SKILL.md，并按轻量账号画像模式执行。
自动获取近期热点；如果无法联网，请进入 Evergreen Mode。
不要伪造热点、来源、平台排名或账号信息。
高风险赛道必须做风险审查。
请输出 Markdown report 和 JSON-like structured block。
```

无需安装。无需 API Key。无需 Python、Node、Shell 脚本或浏览器插件。

## 这个项目是什么

`xhs-topic-strategist-skill` 是一个面向 AI Agent 的小红书选题策划规则包。

它不是自动发帖工具，也不是爬虫或增长工具。它的目标是帮助创作者和内容团队，把一个轻量账号画像转化为：

- 可执行的小红书选题
- 热点与账号定位的匹配分析
- 选题评分和优先级
- 标题、封面、正文结构和标签建议
- 高风险内容的安全改写和人工审核提醒
- Markdown 报告和 JSON-like 结构化结果

## 适合谁

| 使用者 | 典型需求 |
| --- | --- |
| 个人博主 | 不知道今天写什么，需要稳定的选题输入 |
| MCN / 内容团队 | 需要统一多个账号的选题方法和风控口径 |
| AI Agent 用户 | 想让 Claude、Codex、Cursor Agent、Manus、ChatGPT Agent 使用同一套规则 |
| 营销顾问 | 需要为客户快速生成内容方向和选题解释 |
| 品牌内容运营 | 需要把活动、节点、热点转译为账号可用内容 |

## 它解决什么问题

| 常见问题 | 这个 Skill 的处理方式 |
| --- | --- |
| 热点很多，但不知道能不能追 | 用赛道规则判断热点是否适配账号 |
| 选题太泛，写出来像通用 AI 文 | 用账号画像、用户痛点和小红书语感约束输出 |
| 高风险赛道容易写过界 | 强制风险审查，标注人工审核项 |
| 账号主页不一定能访问 | 默认使用轻量账号画像，不依赖主页链接 |
| 不同 Agent 输出不一致 | 用 Markdown 规则文件统一输入、流程、评分和输出格式 |
| 没有联网能力 | 使用 Evergreen Mode，并明确标注非实时热点 |

## 为什么是跨 Agent

这个 Skill 的所有规则都写在 Markdown 文件里：

- `SKILL.md`：入口协议
- `WORKFLOW.md`：执行流程
- `INPUT_SCHEMA.md`：输入方式
- `OUTPUT_SCHEMA.md`：输出格式
- `SCORING_RULES.md`：评分标准
- `RISK_RULES.md`：风险审查
- `NICHE_TAXONOMY.md` 和 `niches/`：赛道规则

只要 Agent 能读取 Markdown，就可以使用这套规则。它不绑定某个模型、平台、插件、API 或运行环境。

## 默认输入：轻量账号画像表

默认推荐的输入不是账号主页链接，而是一张轻量账号画像表。

原因很简单：账号主页可能需要登录，公开信息可能不完整，也可能受验证码、反爬或权限限制影响。Agent 不应该绕过这些限制，也不应该伪造账号信息。

轻量账号画像至少包含：

- 账号主赛道和细分赛道
- 账号定位
- 目标用户
- 用户核心痛点
- 内容风格
- 账号阶段
- 商业化目标
- 内容禁区
- 最近表现好的内容
- 不想做的内容
- 可用素材

模板见：`templates/account_profile_template.md`

## Live Hotspot Mode vs Evergreen Mode

| 模式 | 适用情况 | 必须遵守 |
| --- | --- | --- |
| Live Hotspot Mode | Agent 有联网能力，且能访问公开或授权热点源 | 记录来源、时间和核实状态；不伪造热点和排名 |
| Evergreen Mode | Agent 无法联网，或用户只需要常青选题 | 标注 `非实时热点，基于常青需求生成` |
| User-Provided Hotspot Mode | 用户提供热点、截图、链接或关键词 | 无法核实时标注 `用户提供，待核实` |

Live Hotspot Mode 不代表官方榜单，也不代表平台排名。Evergreen Mode 不应被描述为实时热点。

## Demo 调用 Prompt

```markdown
请使用 XHS Topic Strategist Skill，并严格按 SKILL.md、WORKFLOW.md、SCORING_RULES.md、RISK_RULES.md、XHS_STYLE_GUIDE.md 和 OUTPUT_SCHEMA.md 执行。

默认输入模式：lightweight_account_profile。

要求：
- 优先使用我填写的轻量账号画像。
- 自动获取近期热点；如果无法联网，请进入 Evergreen Mode。
- 无联网时必须标注“非实时热点，基于常青需求生成”。
- 如果我提供热点，优先使用，但无法核实时标注“用户提供，待核实”。
- 不要伪造热点、来源、平台排名或账号信息。
- 不要自动发布内容。
- 高风险赛道必须做风险审查。
- 输出必须包含 Markdown report 和 JSON-like structured block。

# 小红书账号画像表

## 1. 基础信息
- 账号主赛道：
- 细分赛道：
- 账号定位：
- 账号阶段：
- 更新频率：

## 2. 目标用户
- 用户年龄/身份：
- 用户核心痛点：
- 用户想获得什么：
- 用户害怕什么/避开什么：

## 3. 内容风格
- 语气风格：
- 常用内容形式：
- 喜欢的表达方式：
- 不喜欢的表达方式：

## 4. 账号内容依据
- 最近表现好的 3-5 篇内容：
- 最近表现差的 3-5 篇内容：
- 想继续做的方向：
- 不想再做的方向：
- 可用素材：

## 5. 商业化与边界
- 商业化目标：
- 当前要推广的产品/服务：
- 禁区：
- 高风险表达：
- 风险偏好：

## 6. 本次任务
- 想生成几个选题：
- 是否需要图文/视频：
- 是否有特定节日、活动或产品：
- 是否有用户提供热点：
```

## 不同 Agent 如何使用

| Agent | 使用方式 |
| --- | --- |
| Claude | 上传整个仓库作为 Project Knowledge 或会话附件，要求先读 `SKILL.md` |
| Codex | 把仓库放进工作目录，要求按 `SKILL.md` 和轻量账号画像执行 |
| Cursor Agent | 放进项目目录，要求读取核心 Markdown 文件，不创建代码依赖 |
| Manus | 作为参考资料提供，要求无法联网时使用 Evergreen Mode |
| ChatGPT Agent | 上传或粘贴核心文件，要求输出 Markdown report + JSON-like block |

详细说明见：`AGENT_USAGE.md`

## 示例输出长什么样

```markdown
# 今日小红书智能选题策划包

## 账号画像分析
- 账号主赛道：护肤
- 细分赛道：敏感肌护理、换季护肤
- 画像置信度：user_provided_high

## 热点来源摘要
- 使用的热点模式：user_provided_hotspots + evergreen
- 热点核实状态：用户提供，待核实

## 今日 Top 5 选题

### 选题 1：换季敏感期先别乱叠护肤品
- Score：90
- Recommendation level：今日优先
- Risk level：high

#### 标题备选
1. 换季敏感期先别乱叠护肤品
2. 泛红爆皮时，我更建议先做减法

#### 内容结构
1. 场景钩子
2. 痛点共鸣
3. 具体方法
4. 风险提醒
5. 评论互动
```

完整示例见：`examples/sample_output.md`

## 支持赛道

当前包含 28 个小红书头部赛道：

美妆、护肤、香水香氛、医美轻医美、穿搭、珠宝配饰、家居家装、数码家电、食品饮料、美食烘焙、旅行、运动健身、健康养生、宠物、手作兴趣、读书成长、情绪心理、母婴育儿、亲子教育、K12 教育、留学语言、职场、商业创业、AI 工具效率、财商理财、本地生活、婚恋情感、摄影拍照。

详细规则见：`NICHE_TAXONOMY.md` 和 `niches/`

## 高风险内容如何风控

强制风险审查赛道包括：

- 医美轻医美
- 财商理财
- 母婴育儿
- 亲子教育
- K12 教育
- 健康养生
- 护肤功效类
- 职场收入类
- 婚恋情感冲突类

禁止或高风险表达包括：

- 医疗诊断
- 投资收益承诺
- 提分承诺
- 产品绝对功效
- 焦虑式育儿
- 攻击品牌或个人
- 伪造个人体验
- 伪造平台排名

高风险内容必须标注人工审核项。这个 Skill 不能替代法律、医疗、金融、教育、广告合规判断。

## 文件结构

```text
.
├── SKILL.md
├── README.md
├── README.en.md
├── INPUT_SCHEMA.md
├── OUTPUT_SCHEMA.md
├── WORKFLOW.md
├── SCORING_RULES.md
├── RISK_RULES.md
├── XHS_STYLE_GUIDE.md
├── HOTSPOT_SOURCES.md
├── NICHE_TAXONOMY.md
├── ACCOUNT_DISCOVERY.md
├── AGENT_USAGE.md
├── FINAL_AGENT_PROMPT.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── FAQ.md
├── docs/
├── assets/
├── niches/
├── templates/
└── examples/
```

## 如何贡献新赛道

欢迎贡献新的赛道规则、风险规则、热点源建议、示例输出和翻译版本。

新增赛道时请：

1. 在 `NICHE_TAXONOMY.md` 中新增赛道。
2. 在 `niches/` 下新增 Markdown 文件。
3. 参考现有赛道结构，写清楚用户、痛点、热点转译、标题模板、风险边界和示例选题。
4. 如果涉及健康、金融、教育、未成年人、法律、医美、功效、收入或关系冲突，同步更新 `RISK_RULES.md`。

贡献规范见：`CONTRIBUTING.md`

## 项目边界

本项目不会：

- 保证内容表现、流量或涨粉
- 自动发布或批量发布小红书内容
- 收集用户数据或要求 API Key
- 提供官方小红书榜单或平台排名
- 绕过登录、验证码、反爬或权限限制
- 伪造热点、账号信息、评论、互动或个人体验

创作者需要在发布前核实事实、价格、活动、产品信息、合作关系和高风险表达。

## License

MIT License. See `LICENSE`.
