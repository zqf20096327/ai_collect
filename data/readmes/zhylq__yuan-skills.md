# yuan-skills

一个面向 OpenCode、Claude Code 等 AI 编码工具的 Agent Skills 仓库，适配：

```bash
npx skills add <repo> --skill <name>
```

本仓库包含 1 个主写作 skill 和 3 个可选辅助 skill。

## Prerequisites

在使用这些 skills 之前，建议先确认以下环境：

- 已安装支持 `SKILL.md` 的 agent 工具，例如 OpenCode、Claude Code 等
- 已安装 Node.js `>= 16`
- 能正常使用 `npx skills add ...` 安装 skills
- 如果要使用 `zhy-article-illustrator` 或 `zhy-wechat-publish` 的自动封面能力，建议本机可用 `bun`
- 如果要使用 `zhy-wechat-publish`，运行机器的公网 IP 需要加入微信公众号后台 IP 白名单

## Common Commands

安装单个 skill：

```bash
npx skills add https://github.com/zhylq/yuan-skills --skill zhy-wechat-writing
```

列出仓库中的 skill：

```bash
npx skills add https://github.com/zhylq/yuan-skills --list
```

安装到指定 agent：

```bash
npx skills add https://github.com/zhylq/yuan-skills --skill zhy-wechat-writing -a opencode
```

如果某个 skill 提供 `.env.example`，请先复制为本地 `.env`：

```bash
cp .env.example .env
```

Windows PowerShell 可用：

```powershell
Copy-Item .env.example .env
```

## Included Skills

- `zhy-wechat-writing` - 主写作 skill，负责公众号文章的检索、证据池、初稿、审稿、润色与可选后处理编排
- `zhy-article-illustrator` - 可选辅助 skill，为文章生成配图与插图版 Markdown
- `zhy-markdown2wechat` - 可选辅助 skill，将 Markdown 转为微信公众号可用的内联 HTML
- `zhy-wechat-publish` - 可选辅助 skill，将 HTML 上传到微信公众号草稿箱

## Installation

安装单个主 skill：

```bash
npx skills add https://github.com/zhylq/yuan-skills --skill zhy-wechat-writing
```

安装主 skill 与全部辅助 skill：

```bash
npx skills add https://github.com/zhylq/yuan-skills \
  --skill zhy-wechat-writing \
  --skill zhy-article-illustrator \
  --skill zhy-markdown2wechat \
  --skill zhy-wechat-publish
```

列出仓库中可发现的 skills：

```bash
npx skills add https://github.com/zhylq/yuan-skills --list
```

安装到指定 agent，例如 OpenCode：

```bash
npx skills add https://github.com/zhylq/yuan-skills --skill zhy-wechat-writing -a opencode
```

## Recommended Usage Modes

### Mode 1: 只装主写作 skill

适合只需要：

- 检索资料
- 生成公众号文章
- 审稿与润色
- 输出 Markdown 成稿

此模式下不依赖其他 3 个辅助 skill。

### Mode 2: 装主 skill + 转 HTML

适合想额外得到公众号 HTML 的场景：

- `zhy-wechat-writing`
- `zhy-markdown2wechat`

### Mode 3: 装完整链路

适合一条龙完成：

- 写作
- 配图
- 转 HTML
- 保存到公众号草稿箱

需要安装全部 4 个 skill。

## Environment Setup

本仓库不包含任何真实密钥。

- `zhy-wechat-writing` 本身不强制要求 `.env`
- `zhy-markdown2wechat` 不需要 `.env`
- `zhy-article-illustrator` 需要图像生成配置；如启用上传图床，还需要七牛云配置
- `zhy-wechat-publish` 需要微信公众号 API 凭据；如启用自动封面，还需要可用的生图环境

如果某个 skill 目录中存在 `.env.example`：

1. 复制为本地 `.env`
2. 填入你自己的配置
3. 不要将真实 `.env` 提交回 GitHub

### WeChat 相关前置配置

如果你要使用草稿箱发布能力，通常需要准备：

- `WECHAT_APP_ID`
- `WECHAT_APP_SECRET`
- 可选：`WECHAT_DEFAULT_THUMB_MEDIA_ID`
- 可选：`WECHAT_DEFAULT_AUTHOR`

如果你要自动生成封面并发布，还需要额外准备可用的生图配置。

### 图像生成相关前置配置

如果你要使用自动配图或自动封面，通常需要准备至少一种图像生成通道：

- `IMAGE_PROVIDER` / `IMAGE_MODEL` / `IMAGE_BASE_URL` / `IMAGE_API_KEY`
- 或 `XIAOMI_API_KEY` / `XIAOMI_BASE_URL`
- 或 `GEMINI_API_KEY` / `GOOGLE_API_KEY`
- 或 `OPENAI_API_KEY`

如果你要把图片上传到七牛云，还需要：

- `QINIU_ACCESS_KEY`
- `QINIU_SECRET_KEY`
- `QINIU_BUCKET`
- `QINIU_DOMAIN`
- 可选：`QINIU_REGION`

## Repository Layout

```text
skills/
  zhy-wechat-writing/
  zhy-article-illustrator/
  zhy-markdown2wechat/
  zhy-wechat-publish/
```

每个 skill 目录至少包含一个 `SKILL.md`。脚本、主题文件、参考文档等资源都放在各自 skill 子目录中。

## Security Notes

- 请勿提交真实 `.env`
- 请勿提交生成产物（文章、图片、HTML、测试封面）
- 请勿提交公众号 AppID / AppSecret / media_id / 图床密钥
- 如果你曾经误提交过密钥，请在公开仓库前先轮换
