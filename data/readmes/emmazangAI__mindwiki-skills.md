# MindWiki Skills

> 10位顶级专家的思维操作系统，封装为可运行的 Agent Skills。

![MindWiki 首页](docs/screenshot-hero.png)

🌐 在线体验：[mindwiki.goufriend.cn](https://mindwiki.goufriend.cn/)

## 一句话

**不是角色扮演，不是语录复读。** 是用结构化的心智模型+决策启发式+表达DNA，帮你在做决策时获得多视角的深度追问和冲突对撞。

## 为什么需要这个？

| 单一 ChatGPT 对话 | MindWiki Skills |
|---|---|
| 单一视角回答 | 多专家冲突对撞——同一问题给出相反判断 |
| 泛泛而谈 | 基于 WebSearch 真实数据的专家判断 |
| 无记忆 | 决策日志——3个月后回来看自己对了还是错了 |
| 对所有用户一样 | 读取你的文件/数据，针对性分析 |

## 安装

### 一键安装元 skill（10专家组团）

```bash
# Claude Code
cp SKILL.md ~/.claude/skills/mindwiki/SKILL.md

# CodeBuddy
cp SKILL.md ~/.codebuddy/skills/mindwiki/SKILL.md
```

### 安装单个专家

```bash
# 例：安装乔布斯视角
cp -r experts/steve-jobs ~/.claude/skills/steve-jobs-mindwiki/

# 例：安装芒格视角
cp -r experts/charlie-munger ~/.claude/skills/charlie-munger-mindwiki/
```

### 全部安装

```bash
cp SKILL.md ~/.codebuddy/skills/mindwiki/SKILL.md
for d in experts/*/; do
  name=$(basename "$d")
  cp -r "$d" ~/.codebuddy/skills/"$name-mindwiki"/
done
```

## 使用

### 元 skill（组团追问）

```
> 帮我用MindWiki分析要不要做社区产品
> 10个专家怎么看现在的AI Agent发展
> 我在纠结B端还是C端方向
```

### 单个专家

```
> 用乔布斯的视角看我的产品
> 如果是芒格会怎么分析这笔投资
> 用张小龙的克制原则审视我的功能列表
```

## 专家阵容

| 专家 | 最擅长 | 心智模型数 |
|------|--------|-----------|
| 💬 张小龙 | 社交产品、克制、人性 | 5 |
| 🍎 乔布斯 | 产品定义、做减法、设计 | 7 |
| 🚀 马斯克 | 成本、工程、垂直整合 | 6 |
| 📊 张一鸣 | 增长、组织、全球化 | 5 |
| 📚 芒格 | 投资、风险、跨学科 | 5 |
| 🏪 王兴 | 竞争壁垒、平台策略 | 4 |
| 📱 雷军 | 市场时机、性价比、营销 | 5 |
| 🎯 梁宁 | 需求洞察、用户分层 | 4 |
| 💎 Naval | 杠杆、财富、人生方向 | 5 |
| ⚔️ 毛泽东 | 战略、组织动员、逆境 | 5 |

## 核心设计原则

### 带"手"（Agentic）

每个 skill 都能调用工具：
- **WebSearch**：搜索真实产品/公司数据后再分析
- **读文件**：读取用户提供的 PRD/数据/代码
- **写文件**：写入决策日志留档

### 自我验证

每个 skill 配有 `test-prompts.json`：
- 已知答案测试（验证方向一致性）
- 不确定性测试（验证诚实边界）
- 冲突测试（验证能正确表达专家间分歧）

### 持续优化

兼容 [darwin-skill](https://github.com/alchaincyf/darwin-skill) 的棘轮机制。只保留改进，自动回滚退步。

## 致谢

受以下项目启发：
- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — 女娲·人物思维蒸馏
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — 达尔文·Skill进化系统
- [superpowers](https://github.com/gstack/superpowers) — 强制执行工作流
- [gstack/steve-jobs](https://github.com/gstack) — Agentic Protocol 参考

## License

MIT
