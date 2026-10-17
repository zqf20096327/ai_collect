# AI博主账号商业化分析师

一个用于拆解自媒体账号定位、内容策略、增长逻辑与商业化潜力的 Codex Skill。

它可以基于账号主页截图、内容样本、链接或运营数据，分析：

- 账号定位、目标用户与差异化
- 内容方向、选题结构与传播机制
- 起号方式、增长逻辑与关键指标
- 内容优势、制作门槛与账号护城河
- 可直接借鉴、需要改造和不宜照搬的部分
- 广告、带货、课程、咨询、会员、版权与 IP 等变现路径
- AI 内容账号的工具测评、教程、热点依赖、交付能力与合规风险

## 核心原则

- 区分可确认事实、合理推断和未知信息
- 不虚构起号天数、收入、播放量、转粉率或团队规模
- 不混用点赞、收藏、播放、曝光等不同统计口径
- 区分单条爆款、稳定内容模型和可持续生意
- 从用户价值、生产成本、转化链路和商业风险进行判断

## 安装

```bash
git clone https://github.com/Daguo94/ai-blogger-commercialization-analyst.git
mkdir -p ~/.codex/skills
cp -R ./ai-blogger-commercialization-analyst/ai-blogger-commercialization-analyst ~/.codex/skills/
```

安装后，可在 Codex 中调用：

```text
使用 $ai-blogger-commercialization-analyst，分析这个账号的定位、内容策略、增长逻辑与商业化潜力。
```

## 适用场景

- 分析 AI 类内容账号、知识博主或个人 IP
- 拆解品牌号、媒体号、电商号或项目型内容 IP
- 对比多个竞品账号的复制门槛和变现能力
- 输出指定字数的账号商业分析
- 判断一个账号值得借鉴什么、不应照搬什么

## 仓库结构

```text
ai-blogger-commercialization-analyst/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── analysis-framework.md
```

## License

MIT
