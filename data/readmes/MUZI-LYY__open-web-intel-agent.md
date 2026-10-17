<p align="center">
  <img src="docs/assets/logo.svg" width="96" alt="Open-Web-Intel logo">
</p>

<h1 align="center">👁️ Open-Web-Intel</h1>

<p align="center"><strong>给 AI Agent 装上网能力 —— 零登录、零 Cookie、零第三方数据服务，数据不出本机。</strong></p>

AI Agent 能写代码、改文档、管项目，但让它上网找点东西就抓瞎：看不了 YouTube 字幕、搜不了公开讨论、网页抓回来一堆 HTML 标签。市面上的解决方案要么要付费 API，要么要你交出账号 Cookie，要么把内容转发给第三方服务。

`Open-Web-Intel` 走另一条路：**只读公开内容，直接从源头抓取，不经任何第三方中转，永不接触你的账号。**

---

## 三条原则

| 原则 | 说明 |
|------|------|
| 🔒 **零 Cookie** | 不支持、也不需要任何登录态。没有 Cookie 提取、没有浏览器会话桥接，没有封号风险 |
| 🏠 **数据不出本机** | 网页由标准库 `urllib` 本地抓取并转 Markdown，内容不经过任何第三方阅读/搜索服务 |
| 🆓 **零成本零密钥** | 全开源、全免费、无需 API Key。唯一可选的是官方 GitHub Token（提升 gh 限额） |

> 我们明确**不支持**需要登录的平台（Twitter、Reddit、小红书、Facebook、Instagram 等）。
> 这是故意的：把「安全」当卖点，而不是把「功能少」当短板。

---

## 支持的平台

全部**装好即用**，无需任何配置：

| 平台 | 工具 | 能力 |
|------|------|------|
| 🌐 网页 | 本地抓取（urllib） | 读任意公开网页，转 Markdown |
| 📺 YouTube | yt-dlp | 字幕、视频信息、搜索、评论 |
| 📦 GitHub | gh CLI（官方） | 仓库、代码搜索、Issue、PR |
| 📺 B站 | bili-cli | 搜索、热门、排行、视频详情 |
| 💻 V2EX | 公开 API | 热门主题、节点、帖子、用户 |
| 📡 RSS | feedparser | 读任意 RSS/Atom 源 |

## 定位

`Open-Web-Intel` 是**能力层（capability layer），不是包装层**。它负责三件事：

1. **选型** — 每个平台挑一个最稳的免费/官方工具
2. **安装** — 替你装好这些上游工具
3. **体检** — `open-web-intel doctor` 一条命令告诉你哪个通、哪个不通、怎么修

装完之后，Agent **直接调用上游工具**（yt-dlp、gh、bili、feedparser），不经过中转。

---

## 快速上手

复制这句话给你的 AI Agent（Claude Code、OpenClaw、Cursor 等）：

```
帮我安装 Open-Web-Intel：https://raw.githubusercontent.com/liyongyan129-maker/open-web-intel-agent/main/docs/install.md
```

就这一步。Agent 会自己完成剩下的所有事情。

> 🛡️ **默认安全：** `open-web-intel install` 默认只检查环境，不自动装系统包、不写配置。
> 只有显式 `--system` 才安装系统依赖和注册 skill。

### 命令速览

```bash
open-web-intel install --env=auto              # 只读检查（默认）
open-web-intel install --env=auto --system     # 显式授权后安装
open-web-intel doctor                          # 体检，看每个渠道状态
open-web-intel doctor --json                   # 机器可读输出
open-web-intel check-update                    # 检查新版本
open-web-intel uninstall                       # 卸载
```

### 装好就能用

```bash
# 读任意公开网页（本地抓取，转 Markdown）
python3 -c "from open_web_intel.channels.web import WebChannel; print(WebChannel().read('URL'))"

# YouTube 字幕
yt-dlp --write-sub --write-auto-sub --skip-download -o "/tmp/%(id)s" "URL"

# GitHub 搜索
gh search repos "query" --sort stars --limit 10

# B站搜索（无需登录）
bili search "query" --type video -n 5

# V2EX 热门
curl -s "https://www.v2ex.com/api/topics/hot.json" -H "User-Agent: open-web-intel/1.0"
```

**不需要记命令。** Agent 读了 SKILL.md 之后自己知道该调什么。

---

## 安全设计

| 措施 | 说明 |
|------|------|
| 🔒 凭据本地存储 | 配置存 `~/.open-web-intel/config.yaml`，权限 600，只存可选的 GitHub Token / 代理 |
| 🛡️ 默认安全 | `install` 默认只读；只有显式 `--system` 才改系统 |
| 👀 完全开源 | 代码透明，随时可审查 |
| 🔍 SSRF 防护 | 本地抓取拒绝内网 IP、localhost、云 metadata 地址等，防止被诱导读取内部资源 |
| 🧩 可插拔 | 不信任某个渠道？换掉对应的 channel 文件即可 |

---

## 安装 / 卸载

```bash
# 安装（推荐 pipx）
pipx install https://github.com/liyongyan129-maker/open-web-intel-agent/archive/main.zip

# 卸载
open-web-intel uninstall
pip uninstall open-web-intel
```

详见 [docs/install.md](docs/install.md) 和 [docs/update.md](docs/update.md)。

---

## License

[MIT](LICENSE)
