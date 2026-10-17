# 👁️ NetReach — no-login 版

> 给你的 AI Agent 一键装上互联网「只读 + 搜索」能力 —— 只收录**无需登录、爬虫风险低**的公开数据源。

---

## 支持的平台（全部零配置，无需登录）

| 平台 | 能力 | 后端 |
|------|------|------|
| 🌐 网页 | 读任意网页 → Markdown | Jina Reader（`curl r.jina.ai/URL`） |
| 📺 YouTube | 字幕提取 + 视频搜索 | yt-dlp |
| 📡 RSS | 解析任意 RSS/Atom 源 | feedparser |
| 📦 GitHub | 公开仓库 + 代码搜索 | gh CLI（公开数据无需登录） |
| 💻 V2EX | 热门/节点/帖子详情+回复/用户 | 公开 API |
| 📺 B站 | 搜索 + 视频详情（无需登录） | bili-cli ▸ 搜索 API |
| 🔍 全网搜索 | AI 语义搜索 | Exa（mcporter MCP，免费无需 Key） |

> ⚠️ 注意：B站**字幕**需要浏览器登录态，不在本版本范围内（不登录只能搜视频、看详情）。

---

## 设计理念

**NetReach 是一个能力层（capability layer），不是又一个工具。**

它负责**选型、安装、体检、路由**，不负责底层读取本身。读取由 Agent 直接调用上游工具（yt-dlp、gh、feedparser、bili-cli 等）完成，没有包装层。

每个平台 = **首选 + 备选的有序后端列表**。换接入方式 = 调整列表顺序，不是重写代码。`agent-reach doctor` 会告诉你每个平台**当前在用哪个后端**。

```
channels/
├── web.py          → Jina Reader
├── youtube.py      → yt-dlp
├── rss.py          → feedparser
├── github.py       → gh CLI
├── v2ex.py         → V2EX 公开 API（直接 HTTP 实现）
├── bilibili.py     → bili-cli ▸ B站搜索 API
├── exa_search.py   → Exa via mcporter
└── __init__.py     → 渠道注册
```

每个渠道文件按序**真实探测**各候选后端（不只是看命令存不存在），第一个完整可用的当选；坏掉的会给出修复处方。

---

## 快速上手

```bash
# 安装（默认安全检查，只读不改系统）
agent-reach install --env=auto

# 显式授权安装系统依赖 + 注册 skill
agent-reach install --env=auto --system

# 体检：一条命令看每个渠道通不通、走哪个后端
agent-reach doctor
```

安装完直接告诉 Agent 就行，不用记命令：

- "看看这个链接" → `curl https://r.jina.ai/URL`
- "这个 GitHub 仓库是干嘛的" → `gh repo view owner/repo`
- "这个 YouTube 视频讲了什么" → `yt-dlp` 提取字幕
- "B站搜一下 AI 教程" → `bili search "AI 教程"`
- "全网搜 LLM 框架对比" → Exa 语义搜索
- "订阅这个 RSS" → `feedparser`

Agent 读取 SKILL.md 后自己知道该调什么。

---

## 安装的系统依赖

`install --system` 会安装以下外部工具（`--safe`/默认模式只检查、不安装）：

| 工具 | 用途 |
|------|------|
| gh CLI | GitHub 读取/搜索 |
| Node.js | yt-dlp JS runtime + mcporter |
| mcporter + Exa | 全网语义搜索 |
| bili-cli | B站搜索/详情（可选） |

---

## 安全性

| 措施 | 说明 |
|------|------|
| 🔒 **无凭据** | 本版本不需要 Cookie/Token，配置仅存一个可选的网络代理 |
| 🛡️ **默认安全** | `install` 默认只检查不改系统；显式 `--system` 才安装工具 |
| 👀 **完全开源** | 代码透明，随时可审查 |
| 🔍 **Dry Run** | `install --dry-run` 预览所有操作，不做任何改动 |
| 🧩 **可插拔** | 不信任某个组件？换掉对应 channel 文件即可 |

---

## 命令参考

```bash
agent-reach install --env=auto [--system | --safe] [--dry-run] [--proxy=...]
agent-reach doctor [--json]
agent-reach version
```

---

## License

[MIT](LICENSE)

---

## 致谢

[yt-dlp](https://github.com/yt-dlp/yt-dlp) · [Jina Reader](https://github.com/jina-ai/reader) · [feedparser](https://github.com/kurtmckee/feedparser) · [gh CLI](https://cli.github.com) · [bili-cli](https://github.com/public-clis/bilibili-cli) · [Exa](https://exa.ai) · [mcporter](https://github.com/nicobailon/mcporter)
