<p align="center">
  <img src="https://img.shields.io/badge/skills-20-6366f1?style=for-the-badge&logo=robotframework&logoColor=white" alt="20 Skills">
  <img src="https://img.shields.io/badge/endpoints-984-22c55e?style=for-the-badge&logo=fastapi&logoColor=white" alt="984 Endpoints">
  <img src="https://img.shields.io/badge/license-MIT--0-f59e0b?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="MIT-0 License">
  <img src="https://img.shields.io/badge/version-3.8.0-ec4899?style=for-the-badge&logo=semver&logoColor=white" alt="v3.8.0">
</p>

<h1 align="center">🌐 MaxHub Skills</h1>

<p align="center">
  <strong>让 AI Agent 轻松接入 20 个主流平台数据 - 一行指令，数据直达</strong>
</p>

<br />

<p align="center">
  <a href="https://www.aconfig.cn">🔑 获取 API Key</a> ·
  <a href="https://agentskills.io">📖 Agent Skills 标准</a>
</p>

***

## ✨ 为什么选择 MaxHub Skills？

| 特性             | 说明                                                      |
| -------------- | ------------------------------------------------------- |
| 🎯 **开箱即用**    | 20 个 Skill 覆盖国内外主流平台，安装即用                               |
| 🔗 **统一 API**  | 一套 `MAXHUB_API_KEY` 打通所有平台，无需逐个对接                       |
| 🧠 **AI 原生**   | 遵循 [Agent Skills](https://agentskills.io) 标准，渐进式加载，语义路由 |
| 📡 **984 端点** | 覆盖视频、用户、搜索、直播、评论、创作者等全场景                                |
| 🌍 **全球覆盖**    | 国内（抖音/B站/小红书）+ 海外（TikTok/YouTube/Instagram）全覆盖           |
| 🔒 **安全合规**    | 每个引用文件附带安全声明，高风险端点已移除                              |

***

## ⚖️ 法律合规

> **使用本项目前，请务必阅读以下文件：**

| 文档 | 说明 |
|---|---|
| 📋 [DATA_USAGE_POLICY.md](./DATA_USAGE_POLICY.md) | 数据使用政策：合法/禁止场景、平台 ToS 冲突提示、PIPL/GDPR 合规指引 |
| ✅ [COMPLIANCE_CHECKLIST.md](./COMPLIANCE_CHECKLIST.md) | 合规审查清单：使用前必检的合法性、数据保护、平台授权检查项 |

**关键提示**：
- 本项目通过第三方数据服务（MaxHub API）获取平台数据，**未获得各平台官方授权**
- 所有合规责任由使用者自行承担，使用前请完成合规审查清单
- 抖音/TikTok 的高风险端点（刷量操控、反爬绕过、会话伪造等）已从本项目中**移除**
- LinkedIn、微信、Instagram/Meta 为**高风险平台**，存在显著法律风险

***

## 🚀 快速开始

```bash
# 1. 获取 API Key
open https://www.aconfig.cn

# 2. 设置环境变量
export MAXHUB_API_KEY="your-api-key"

# 3. 在 AI Agent 中安装 Skill
# 打开 SkillHub，搜索平台名称（如「抖音」），一键安装
```

安装后，直接对 Agent 说：

> *"帮我分析这个抖音账号最近 30 天的粉丝增长趋势"*

Agent 会自动激活 `maxhub-douyin` Skill 并调用对应 API。

***

## 📦 技能矩阵

### 🎬 短视频 & 视频

| Skill                                    | 平台      |  端点 | 核心能力                  |
| ---------------------------------------- | ------- | :-: | --------------------- |
| 📺 [maxhub-bilibili](./maxhub-bilibili/) | B站      |  42 | 视频详情、弹幕、直播、UP主画像      |
| 🎵 [maxhub-douyin](./maxhub-douyin/)     | 抖音      | 275 | 视频/用户/搜索/热榜/直播/星图/创作者 |
| 🎬 [maxhub-kuaishou](./maxhub-kuaishou/) | 快手      |  38 | 视频、用户、直播、评论           |
| 🎶 [maxhub-tiktok](./maxhub-tiktok/)     | TikTok  | 154 | 视频/用户/广告/电商/创作者       |
| ▶️ [maxhub-youtube](./maxhub-youtube/)   | YouTube |  39 | 视频、频道、搜索、评论           |
| 🍉 [maxhub-xigua](./maxhub-xigua/)       | 西瓜视频    |  8  | 视频、用户                 |
| 🎥 [maxhub-sora2](./maxhub-sora2/)       | Sora2   |  18 | AI 视频、创作者、工具          |

### 📱 社交媒体 & 社区

| Skill                                          | 平台        |  端点 | 核心能力            |
| ---------------------------------------------- | --------- | :-: | --------------- |
| 📕 [maxhub-xiaohongshu](./maxhub-xiaohongshu/) | 小红书       |  44 | 笔记、用户、搜索、商品     |
| 🐦 [maxhub-weibo](./maxhub-weibo/)             | 微博        |  65 | 博文、用户、热搜、评论     |
| 💡 [maxhub-zhihu](./maxhub-zhihu/)             | 知乎        |  41 | 内容、用户、搜索、热榜     |
| 📰 [maxhub-toutiao](./maxhub-toutiao/)         | 今日头条      |  8  | 内容、用户           |
| 💬 [maxhub-wechat](./maxhub-wechat/)           | 微信        |  24 | 视频号、公众号、搜索      |
| 🦐 [maxhub-pipixia](./maxhub-pipixia/)         | 皮皮虾       |  17 | 内容、用户、热榜        |
| 📸 [maxhub-instagram](./maxhub-instagram/)     | Instagram |  88 | 帖子、用户、搜索、评论     |
| 𝕏 [maxhub-twitter](./maxhub-twitter/)         | Twitter/X |  13 | 推文、搜索、趋势        |
| 🤖 [maxhub-reddit](./maxhub-reddit/)           | Reddit    |  29 | 帖子、用户、Subreddit |
| 🧵 [maxhub-threads](./maxhub-threads/)         | Threads   |  12 | 帖子、用户           |
| 🍋 [maxhub-lemon8](./maxhub-lemon8/)           | Lemon8    |  15 | 内容、用户、发现        |

### 💼 职场 & 工具

| Skill                                      | 平台       |  端点 | 核心能力        |
| ------------------------------------------ | -------- | :-: | ----------- |
| 💼 [maxhub-linkedin](./maxhub-linkedin/)   | LinkedIn |  50 | 用户、公司、职位、内容 |
| 📧 [maxhub-temp-mail](./maxhub-temp-mail/) | 临时邮箱     |  4  | 临时邮箱生成与收件   |



## 🏗️ 项目结构

```
maxhub-skills/
├── SKILL.md                    # 聚合入口（Agent 发现用）
├── README.md                   # 本文件
├── LICENSE                     # MIT-0
├── DATA_USAGE_POLICY.md        # 数据使用政策
├── COMPLIANCE_CHECKLIST.md     # 合规审查清单
│
├── maxhub-bilibili/            # 每个平台一个独立 Skill
│   ├── SKILL.md                #   技能入口：路由表、交互流程
│   ├── README.md               #   英文文档
│   ├── README_CN.md            #   中文文档
│   ├── DATA_USAGE_POLICY.md    #   平台专属数据使用政策
│   ├── _meta.json              #   发布元数据
│   └── references/             #   按需加载的 API 引用
│       ├── api-video.md
│       ├── api-user.md
│       ├── api-search.md
│       └── param-mappings.md
│
├── maxhub-douyin/
│   └── ...                     # 同上结构
│
└── maxhub-zhihu/
    └── ...
```

### 设计原则

- **渐进式披露** — Agent 只加载当前任务需要的引用文件，避免上下文污染
- **语义路由** — 文件名即语义（`api-video.md` = 视频接口），无需全文扫描
- **链式引导** — 常见多步操作（如「搜用户 → 查作品 → 分析评论」）已文档化

***

## 🔧 开发

### 新增 Skill

```bash
# 1. 复制模板
cp -r _template maxhub-new-platform

# 2. 编辑 SKILL.md（frontmatter + 路由表）
# 3. 添加 references/ 下的 API 引用文件
# 4. 更新 _meta.json 版本号
# 5. 提交 PR
```

### 文件规范

| 文件                             |  必需 | 说明                            |
| ------------------------------ | :-: | ----------------------------- |
| `SKILL.md`                     |  ✅  | 技能入口，含 frontmatter、路由表、交互协议   |
| `_meta.json`                   |  ✅  | 发布元数据（ownerId, slug, version） |
| `README.md`                    |  ✅  | 英文说明                          |
| `README_CN.md`                 |  ✅  | 中文说明                          |
| `references/param-mappings.md` |  ✅  | 参数映射规则                        |
| `references/api-*.md`          |  ✅  | 按功能分类的 API 引用                 |

***

## 🤝 贡献

欢迎提交 Issue 和 Pull Request。

- 📖 贡献指南：遵循现有 Skill 目录结构，确保 `SKILL.md` frontmatter 完整

***

## 📄 许可

[MIT-0](./LICENSE) © 2026 MaxHub API

***

<p align="center">
  <sub>Made with ❤️ by MaxHub Team · Powered by <a href="https://www.aconfig.cn">aconfig.cn</a></sub>
</p>
