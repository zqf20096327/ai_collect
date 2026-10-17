# hermes-chinese-workflows

> Hermes Agent 中文实战工作流合集 — 一人公司自动化模板
>
> 用 Hermes Agent 搭建属于你的 AI 自动化系统：公众号运营、产品调研、社群运营、内容创作...

[![Skills](https://img.shields.io/badge/Hermes_Skills-10+-blue)](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
[![Cron Templates](https://img.shields.io/badge/Cron_Templates-8+-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 这是什么？

这是一套基于 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 的中文实战工作流模板。

不是教程，不是翻译文档 — 是**可以直接用的完整配置**。

每个工作流都经过真实业务验证，包含：
- Skill 配置文件（直接放入 `~/.hermes/skills/`）
- Cron 任务配置（直接导入 Hermes）
- 辅助脚本（Python/Shell）
- 完整的 README（含安装步骤和效果说明）

## 包含的工作流

### 1. 微信公众号自动化

| 组件 | 说明 |
|------|------|
| Skill | 公众号文章写作、排版、发布全流程 |
| Cron | 每日自动选题 + 自动写作 + 自动排版 + 定时发布 |
| 辅助脚本 | 文章调度器、发布状态管理、数据读取 |

**效果**：每天 2 篇原创深度长文（3000-6000字），全自动。

### 2. 产品调研团队

| 组件 | 说明 |
|------|------|
| Skill | 市场侦察、竞品分析、用户心声采集、报告生成 |
| Cron | 每日 2 次信息扫描 + 每周汇总报告 |
| 辅助脚本 | RSS 扫描脚本（基于 blogwatcher-cli） |
| 模板 | App 深度分析模板、机会评分卡模板、周报模板 |

**效果**：10 个 RSS 源自动监控，每日筛选新发现，每周生成调研周报。

### 3. 社群运营自动化

| 组件 | 说明 |
|------|------|
| Skill | 选题研究、早安速报、互动话题、精华推送 |
| Cron | 每日 4 次自动推送 + 每周 Skill 推荐 + 运营周报 |
| 模板 | FAQ 库、互动话题池、选题库 |

**效果**：社群日常运营 80% 自动化，每天只需 30 分钟人工介入。

### 4. 内容创作流水线

| 组件 | 说明 |
|------|------|
| Skill | 封面图生成、文章插图、信息图卡片、Markdown 转 HTML |
| 模板 | 文章排版模板、SEO 关键词布局 |

**效果**：从选题到配图到排版到发布，全流程 AI 化。

### 5. 行业动态监控

| 组件 | 说明 |
|------|------|
| Skill | RSS 监控、Web 文章研究、博客追踪 |
| Cron | 每日 AI Agent 行业动态简报 |

**效果**：自动追踪 10+ 信息源，每日生成中文简报。

## 快速开始

### 前提条件

- 已安装 [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- 已完成基础配置（`hermes setup`）

### 安装工作流

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/hermes-chinese-workflows.git
cd hermes-chinese-workflows

# 2. 安装 Skills（选择你需要的工作流）
# 微信公众号自动化
cp -r skills/wechat-official/* ~/.hermes/skills/

# 产品调研团队
cp -r skills/product-research/* ~/.hermes/skills/

# 社群运营
cp -r skills/community-ops/* ~/.hermes/skills/

# 3. 安装辅助脚本
cp scripts/*.sh ~/.hermes/scripts/
cp scripts/*.py ~/.hermes/scripts/
chmod +x ~/.hermes/scripts/*.sh

# 4. 导入 Cron 模板
# 在 Hermes 中使用 cronjob 工具，参考 templates/cron/ 中的配置

# 5. 重启 Hermes
# CLI: 退出后重新运行 hermes
# Gateway: /restart
```

## 目录结构

```
hermes-chinese-workflows/
├── README.md                    # 你正在看的文件
├── skills/                      # Skill 文件（直接复制到 ~/.hermes/skills/）
│   ├── wechat-official/         # 公众号自动化
│   ├── product-research/        # 产品调研
│   ├── community-ops/           # 社群运营
│   └── content-creation/        # 内容创作
├── scripts/                     # 辅助脚本
│   ├── app-scout.sh             # RSS 扫描脚本
│   ├── hermes-scout.sh          # Hermes 生态扫描
│   └── wechat-article-scheduler.py  # 文章调度
├── templates/                   # 模板文件
│   ├── cron/                    # Cron 任务配置模板
│   ├── research/                # 调研模板
│   └── community/               # 社群模板
└── docs/                        # 详细文档
    ├── wechat-setup.md          # 公众号配置教程
    ├── research-setup.md        # 调研团队配置教程
    └── community-setup.md       # 社群运营配置教程
```

## 预览效果

### 公众号自动化 — 每日输出

```
[09:00] 工作日上午文章 → 自动选题 → 写作 → 配图 → 排版 → 发布
[15:00] 工作日下午文章 → 自动选题 → 写作 → 配图 → 排版 → 发布
[21:00] 非工作日文章 → 预产 → 排期 → 周末发布
```

### 产品调研 — 每日简报

```
📰 2026-04-27 产品调研简报

新发现（3个）：
⭐ Notion Calendar - 日历类新品，评分 ★★★★☆
⭐ AutoPilot - 自动化工具，评分 ★★★☆☆
⭐ ...

用户痛点 TOP 5：
1. "I wish there was an app that..." — Reddit r/productivity
2. ...
```

### 社群运营 — 每日节奏

```
[09:00] ☀️ 早安速报 — Hermes 每日动态
[12:00] 🤔 互动话题 — "你用 Hermes 最长做的一件事是什么？"
[18:00] 💡 每日精选 — 技巧/文章推荐
```

## 适用人群

- 一人公司 / 独立开发者 — 用 AI 自动化运营
- 内容创作者 — 公众号/小红书/B站自动发文
- 产品经理 — 自动化竞品调研和用户反馈收集
- 社群运营 — 付费社群自动化运营

## 技术栈

| 组件 | 技术 |
|------|------|
| AI Agent | [Hermes Agent](https://github.com/NousResearch/hermes-agent) |
| 消息平台 | 飞书 / Telegram / Discord |
| RSS 监控 | [blogwatcher-cli](https://github.com/JulienTant/blogwatcher-cli) |
| 笔记系统 | Obsidian |
| 内容发布 | 微信公众号 API |
| 图片生成 | OpenAI DALL-E / Midjourney |

## 常见问题

<details>
<summary>Hermes 是什么？</summary>

Hermes Agent 是 Nous Research 开源的一款 AI Agent 框架，运行在终端中，支持 20+ LLM 提供商，可以接入 Telegram/Discord/飞书等 10+ 消息平台。类似于 Claude Code（Anthropic）或 Codex（OpenAI），但更加开放和可定制。

项目地址：https://github.com/NousResearch/hermes-agent
</details>

<details>
<summary>这些工作流需要什么成本？</summary>

主要成本是 LLM API 调用费。以 GLM-4 为例，生成一篇 4000 字的文章约 ¥0.05。每日 2 篇文章 + 调研简报 + 社群推送，月成本约 ¥10-30。
</details>

<details>
<summary>可以自定义吗？</summary>

完全可以。所有 Skill 都是 Markdown 文件，可以直接编辑。Cron 任务也可以随时调整频率和内容。建议 fork 后按需修改。
</details>

## 贡献

欢迎提交 PR！如果你有自己打磨的 Hermes 工作流，欢迎分享。

贡献指南：
1. Fork 本仓库
2. 创建你的工作流目录（`skills/your-workflow/`）
3. 包含 SKILL.md + README + 效果截图
4. 提交 PR

## 许可证

MIT License

## 相关链接

- [Hermes Agent 官方文档](https://hermes-agent.nousresearch.com/docs/)
- [Hermes GitHub](https://github.com/NousResearch/hermes-agent)
- [Hermes Skill Hub](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)

---

**⭐ 觉得有用？来我的 [Hermes 中文用户社群](https://your-link.com) 获取更多 Skill 和配置帮助！**
