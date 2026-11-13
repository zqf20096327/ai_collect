# VellumVault

> 把互联网上的一切变成你自己的 Markdown 知识库

VellumVault 是一个**本地优先**的内容归档工具。粘贴一个链接（或拖入一个文件），它会自动完成抓取、下载、格式转换、AI 总结，最终输出干净的 Markdown 文件。

所有 AI 推理默认在你自己的机器上运行（通过 [LM Studio](https://lmstudio.ai/)），也支持接入 OpenAI / DeepSeek 等任意 OpenAI 兼容 API。

---

## 它能做什么

### 视频 → 字幕 + 摘要

粘贴 YouTube / B站 / 抖音 / TikTok / 微信视频号链接，自动：
1. 下载视频（yt-dlp）
2. 提取字幕或语音转文字（faster-whisper）
3. AI 生成结构化摘要（核心观点 + 关键要点 + 标签）

### 文章 → Markdown

粘贴微信公众号 / 知乎 / 小红书 / X (Twitter) / GitHub 或任意网页链接，自动：
1. 智能识别平台，用专属提取器拿到干净内容
2. 图片本地化，避免外链失效
3. AI 总结全文

小红书图文帖还会自动 OCR 图片中的文字；X Article 支持完整渲染。

### 文档 → Markdown

上传 PDF 或 DOCX 文件，自动：
1. **PDF 体裁识别** — 区分文档型、PPT 型、扫描件，选择最优处理策略
2. **视觉模型转写** — PPT/扫描件逐页渲染为图片，由 Vision LLM 转写（图表数据也能读）
3. **混合模式** — 文档型 PDF 中文字密集的页走文本提取，稀疏页走视觉模型
4. **DOCX 完整解析** — 保留表格结构和嵌入图片

### 统一归档

所有内容最终都存为相同结构：

```
~/VideoArchive/videos/2026-06-18_youtube_如何学习编程/
├── content.md        # 原文 / 字幕 Markdown
├── summary.md        # AI 摘要
├── metadata.json     # 元数据（来源、作者、时间、标签）
├── images/           # 本地化的图片
├── video.mp4         # 视频原件（如有）
├── transcript.txt    # 转写文本（如有）
└── original.pdf      # 原始文件备份（如有）
```

---

## 架构

```
                    ┌─────────┐  ┌──────────┐  ┌─────┐  ┌──────────┐
                    │  Web UI │  │ 飞书机器人 │  │ CLI │  │ HTTP API │
                    └────┬────┘  └─────┬─────┘  └──┬──┘  └────┬─────┘
                         └─────────────┼───────────┼───────────┘
                                       ▼
                              ┌─────────────────┐
                              │  SQLite 任务队列  │
                              └────────┬────────┘
                                       ▼
                            ┌──────────────────────┐
                            │  PipelineRunner 路由   │
                            └──┬─────────┬────────┬─┘
                               ▼         ▼        ▼
                    ┌──────────────┐ ┌────────┐ ┌──────────────┐
                    │ 视频 Pipeline │ │文章提取 │ │ 文档 Pipeline │
                    │              │ │        │ │              │
                    │ yt-dlp       │ │ 微信   │ │ PDF 体裁检测  │
                    │ faster-whisper│ │ 知乎   │ │ Vision LLM   │
                    │ LLM 总结     │ │ 小红书  │ │ pymupdf4llm  │
                    │              │ │ X/推特  │ │ DOCX reader  │
                    └──────┬───────┘ │ GitHub │ └──────┬───────┘
                           │         │ 通用   │        │
                           │         └───┬────┘        │
                           └─────────────┼─────────────┘
                                         ▼
                              ┌──────────────────┐
                              │  统一归档 + 总结    │
                              │  ~/VideoArchive/  │
                              └──────────────────┘
```

---

## 快速开始

### 环境要求

- macOS（Linux 理论可用，未充分测试）
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) — Python 包管理器
- ffmpeg — 音视频处理
- [LM Studio](https://lmstudio.ai/)（可选，本地 LLM 推理）

### 安装

```bash
# 安装系统依赖
brew install uv ffmpeg

# 克隆项目
git clone https://github.com/VectorLetter/VellumVault.git
cd vellumvault

# 安装 Python 依赖
uv sync

# 配置环境变量
cp .env.example .env
# 编辑 .env
```

或者用一键脚本：

```bash
bash scripts/install.sh
```

### 配置 LLM

VellumVault 使用 **OpenAI 兼容 API**，支持多种后端：

<details>
<summary><b>方案 A：本地部署（推荐，免费无限用）</b></summary>

1. 安装 [LM Studio](https://lmstudio.ai/)
2. 下载并加载模型：
   - **文本总结**：`qwen3-14b`（或任何你喜欢的模型）
   - **视觉转写**：`qwen3-vl-30b-a3b-instruct`（PDF/图片识别用）
3. 启动 LM Studio 的 API Server（默认 `localhost:1234`）
4. `.env` 无需额外配置，默认值即指向本地

</details>

<details>
<summary><b>方案 B：云端 API</b></summary>

在 `.env` 中配置：

```bash
# 文本总结（以 DeepSeek 为例）
SUMMARIZER_API_BASE=https://api.deepseek.com/v1
SUMMARIZER_API_KEY=sk-xxx
SUMMARIZER_MODEL=deepseek-chat

# 视觉转写（以 OpenAI 为例）
VISION_API_URL=https://api.openai.com/v1
VISION_API_KEY=sk-xxx
VISION_MODEL=gpt-4o
```

支持 OpenAI / DeepSeek / 硅基流动 / 零一万物 / 任何 OpenAI 兼容服务。

</details>

---

## 使用方式

### Web UI（最简单）

```bash
vellumvault web
# 浏览器自动打开 http://localhost:7860
```

Web UI 支持：
- 粘贴 URL 提交（支持批量，每行一个）
- 拖拽上传文件（PDF / DOCX / 音视频）
- 查看任务队列和处理状态
- 浏览归档内容和 AI 摘要

### CLI

```bash
# 提交 URL 并立即处理
vellumvault add https://www.youtube.com/watch?v=xxx

# 只下载，不转写不总结
vellumvault add <url> --download-only

# 下载+转写，跳过 AI 总结
vellumvault add <url> --no-summary

# 查看任务队列统计
vellumvault status

# 重试所有失败任务
vellumvault retry
```

### 守护进程（后台持续运行）

```bash
# 前台运行（Ctrl+C 退出）
vellumvault run

# macOS 开机自启动
bash scripts/install.sh  # 交互式引导安装 LaunchAgent
```

守护进程会持续轮询飞书消息 + 处理待办任务，处理完自动通过飞书消息通知。

### HTTP API

```bash
# 提交 URL（本地免认证）
curl -X POST http://localhost:7860/api/submit_url \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://www.youtube.com/watch?v=xxx"}'

# 查看任务列表
curl -X POST http://localhost:7860/api/tasks

# 健康检查
curl -X POST http://localhost:7860/api/health
```

完整 API 列表见 [docs/architecture.md](docs/architecture.md#八http-api-端点)。

---

## 公网访问（可选）

通过 [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) 可以把本地服务暴露到公网，无需公网 IP 或端口映射：

```bash
brew install cloudflared
cloudflared tunnel create vellumvault
cloudflared tunnel route dns vellumvault vault.example.com
```

配置 `~/.cloudflared/config.yml`：
```yaml
tunnel: <tunnel-id>
credentials-file: ~/.cloudflared/<tunnel-id>.json
ingress:
  - hostname: vault.example.com
    service: http://localhost:7860
  - service: http_status:404
```

在 `.env` 中启用密码保护：
```bash
VAULT_PASSWORD=your-password          # 外网访问需要输入密码
VAULT_PUBLIC_URL=https://vault.example.com  # 启动时打印公网地址
```

本地访问（localhost / 局域网）自动免密。

---

## 支持的平台

| 类型 | 平台 | 说明 |
|---|---|---|
| 视频 | YouTube, B站, 抖音, TikTok, 微信视频号 | yt-dlp 下载 + 字幕/转写 + AI 总结 |
| 文章 | 微信公众号 | 专属提取器，处理反爬 |
| 文章 | 知乎 | 专栏/回答/问题 |
| 文章 | 小红书 | 图文 OCR + 视频转写 |
| 文章 | X / Twitter | 推文 + X Article 全文渲染 |
| 文章 | GitHub | README / Issues / PR |
| 文章 | 通用网页 | trafilatura + readability 提取 |
| 文档 | PDF | 体裁检测 → 视觉模型 / 文本提取 / 混合模式 |
| 文档 | DOCX | 表格 + 嵌入图片完整保留 |
| 文件 | 音视频文件 | 上传后 faster-whisper 转写 |

---

## 技术栈

| 组件 | 技术 | 作用 |
|---|---|---|
| 视频下载 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | 支持 1000+ 视频平台 |
| 语音转写 | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 本地 GPU 推理，large-v3-turbo |
| 文本 LLM | [LM Studio](https://lmstudio.ai/) / OpenAI API | 内容总结，支持 map-reduce 长文本 |
| 视觉 LLM | LM Studio / OpenAI Vision API | PDF 转写、图片 OCR |
| 网页提取 | [trafilatura](https://github.com/adbar/trafilatura) + readability | 正文提取 + 平台专属适配 |
| PDF 解析 | [pymupdf4llm](https://github.com/pymupdf/pymupdf4llm) + Vision LLM | 混合模式：文本+视觉 |
| DOCX 解析 | [python-docx](https://github.com/python-openxml/python-docx) | 自研 reader，保留结构 |
| 任务队列 | SQLite | 轻量，无需额外服务 |
| Web 服务 | Python http.server | 零依赖，内置 JSON API |
| 公网穿透 | [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/) | 可选，免费 |

---

## 项目结构

```
src/vellumvault/
├── main.py                 # CLI 入口（typer）
├── web.py                  # Web UI + HTTP API
├── config.py               # 配置加载
├── db.py                   # SQLite 数据库
├── models.py               # 数据模型
├── pipeline/
│   ├── runner.py            # Pipeline 调度器
│   ├── convert_handler.py   # 文章/文档处理
│   ├── downloader.py        # yt-dlp 封装
│   ├── transcriber.py       # faster-whisper 封装
│   ├── summarizer.py        # LLM 总结（含 map-reduce）
│   ├── archiver.py          # 统一归档
│   └── wechat_downloader.py # 微信视频号专属下载
├── convert/
│   ├── convert.py           # 转换调度器
│   ├── vision.py            # Vision LLM 集成
│   ├── postprocess.py       # Markdown 后处理（10 步清洗）
│   ├── files.py             # PDF/DOCX 处理
│   ├── docx_reader.py       # 自研 DOCX 解析器
│   ├── wechat.py            # 微信公众号提取
│   ├── zhihu.py             # 知乎提取
│   ├── xiaohongshu.py       # 小红书提取
│   ├── x.py                 # X/Twitter 提取
│   └── web.py               # 通用网页提取
├── feishu/                  # 飞书机器人集成
└── utils/                   # 工具函数
```

---

## FAQ

**Q: 不装 LM Studio 能用吗？**

可以。配置云端 API（如 DeepSeek、OpenAI）即可。或者设置 `--no-summary` 跳过 AI 总结，只做下载/转换/归档。

**Q: 支持 Windows / Linux 吗？**

核心功能（下载、转写、转换、总结）跨平台。LaunchAgent 开机自启和 `open_folder` 是 macOS 专属，其他系统需要自行配置。

**Q: 如何添加新平台支持？**

在 `src/vellumvault/convert/` 下新建一个模块，实现 `convert(url, out_dir, *, uploader=None) -> Path` 接口，然后在 `convert.py` 的 `_pick_module()` 中添加 URL 匹配规则。

---

## 免责声明

本项目仅供个人学习和内容归档使用。使用者应遵守相关平台的服务条款及所在地区的法律法规。请勿将本工具用于批量抓取、商业用途或侵犯他人版权的行为。因使用本工具产生的一切后果由使用者自行承担。

## License

[MIT](LICENSE)
