# Video Transcript

**[访问展示网站与完整配置教程 →](https://perpperqaq.github.io/video-transcript/)**

> 把视频链接，变成一份结构化、可回溯的文案总结。
> An Agent Skill that turns a video link (Douyin / Bilibili) into a timestamped transcript and a structured summary.

---

## 这是什么

一个 **Agent Skill**（兼容 HanaAgent / Claude Code 等支持 Skill 的 Agent）。给它一条视频链接，它会：

1. 按平台选链路，把视频语音转成文字：
   - **抖音**：调用本地 **Traffic Compass** 服务（Playwright 抓直链 + 阿里云百炼批量 ASR）
   - **B 站**：`scripts/bili_asr.py`（音频直链下载 → 转码切段 → 百炼实时 ASR 并发），产出**带 `[mm:ss]` 时间轴**的逐句文案
2. 通读全文，生成一份**结构化总结**（核心观点 / 详细观点拆解 / 原文金句 / 关键结论）
3. 存成 Markdown（**上半是总结、下半是完整原文**），便于归档与二次引用

它能处理长视频：B 站链路实测把 **96 分 58 秒**（10 段并发）的视频在 **3–4 分钟**内转完，产出 2.8 万字文案。

---

## ⚠️ 前置依赖

| 依赖 | 抖音 | B 站 |
|---|---|---|
| Traffic Compass 服务 | 必需 | 不需要 |
| 抖音登录态 Cookie | 必需（会过期） | 不需要 |
| 阿里云百炼密钥（`BAILIAN_KEY`） | 必需 | 必需 |
| `dashscope>=1.27` | 必需 | 必需 |
| `ffmpeg` / `ffprobe` | 必需 | 必需 |

Traffic Compass 项目：https://github.com/code-wahaha/traffic-compass
部署步骤见 `references/setup.md`（含抖音 Cookie 授权脚本）。

---

## 安装本 Skill

**方式一（推荐）**：下载 `video-transcript.skill`，在 HanaAgent 里「设置 → 技能」将它拖入安装。

**方式二**：把整个 `video-transcript/` 目录放进技能目录（HanaAgent 为 `~/.hanako/skills/`）。

装好后，确认该 Skill 在你的 Agent 上处于**启用**状态。

---

## 使用

把链接发给 Agent，并说「帮我提取这个视频的文案」「转录一下」「分析一下这个视频」，Agent 会自动触发本 Skill。

也可以直接跑脚本：

```bash
# B 站（不需要服务）
<项目>/.venv/bin/python scripts/bili_asr.py "BV1GyEU6GE7z" -o ./out

# 抖音（自动探活并拉起本地服务）
bash scripts/douyin_extract.sh "https://v.douyin.com/xxxx/"
```

---

## 配置

配置项**都有默认值**，一般不用改（首次使用时 Agent 会确认）：

| 配置项 | 默认值 | 覆盖方式 |
|---|---|---|
| Traffic Compass 项目 | `~/Documents/Playground/traffic-compass` | `TC_PROJECT` |
| 服务地址 | `http://127.0.0.1:8900` | `TC_ADDR` |
| 输出目录 | 当前工作目录 | `-o` 参数 |
| `BAILIAN_KEY` | 读项目内 `webapp/_data/apikeys.json` | 环境变量 |
| `douyin_cookies.json` | 项目内 `webapp/_data/chrome_data/` | `DOUYIN_COOKIE_BASE` |

详细的配置与获取方式见 **`references/setup.md`**。

---

## 工作原理

```
抖音分享链接
  → Playwright + 抖音登录态 Cookie 抓视频直链
  → 阿里云百炼 Paraformer（批量 ASR）
  → Agent 通读全文，生成结构化总结
  → 存成 Markdown（总结 + 原文）

B 站链接
  → view API 取 cid → playurl 取 dash.audio 直链
  → 带 Referer 下载 → ffmpeg 转 16k 单声道 → 切 600s 段
  → 百炼实时 ASR 并发（4 路）→ 按句时间戳 + 段偏移合并
  → Agent 通读全文，生成结构化总结
```

---

## 目录结构

```
video-transcript/
├── SKILL.md                 # 核心：触发条件 + 平台矩阵 + 提取 + 总结 + 保存
├── scripts/
│   ├── bili_asr.py          # B 站：直链 → 转码 → 切段 → 并发 ASR → 时间轴文案
│   ├── douyin_extract.sh    # 抖音：调本地服务提取
│   └── ensure_service.sh    # 探活本地服务，没起就拉起来
└── references/
    ├── setup.md             # 首次安装与配置（含抖音 Cookie 授权脚本）
    ├── fallback.md          # 故障排查 + ASR 报错码 + 已知不可行路径
    └── platforms.md         # 平台矩阵、各链路细节与实测数据
```

> 采用**渐进式披露**：`SKILL.md` 只保留核心工作流（触发即加载），安装、排错与平台细节按需从 `references/` 读取——日常使用不会为用不到的内容付费。

---

## 常见问题

**Q：装好 Skill 了，但提取一直失败？**
抖音链路多半是服务没跑起来、或 Cookie 过期——先 `bash scripts/ensure_service.sh`，再对照 `references/fallback.md`。

**Q：B 站视频能处理多长？要等多久？**
没有硬上限。96 分钟的实测 3–4 分钟出全稿（下载 + 转码 + 10 段 4 并发识别）。段结果有缓存，重跑只补失败段。

**Q：B 站能直接下官方字幕吗？**
不指望。多数视频没有可用字幕，本 Skill 直接走音频识别，稳定得多。

**Q：抖音视频已下架，抓不到怎么办？**
先向用户要其他来源；有 B 站搬运就直接走 B 站链路。注意：百炼**批量**识别只接受公网 `http(s)` 直链，本地音频/上传文件的几种写法实测都会报 `DECODE_ERROR` 或 `SERVER_ERROR`；但**实时**识别可以吃本地文件，切段并发即可（详见 `references/fallback.md`）。

**Q：需要 DeepSeek Key 吗？**
不需要。本 Skill 只做提取 + 总结，不依赖 Traffic Compass 核心审核所用的 DeepSeek。

---

## 致谢

- 视频提取链路基于开源项目 **Traffic Compass**（作者 code-wahaha，MIT）。
- 本 Skill 仅做流程编排与总结规范，不重复实现底层提取能力。

## License

MIT
