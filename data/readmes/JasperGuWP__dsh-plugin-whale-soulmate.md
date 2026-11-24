# dsh-plugin-whale-soulmate 🐋

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![topic](https://img.shields.io/badge/topic-dsh--plugin-0A7EA4)](https://github.com/topics/dsh-plugin)
[![release](https://img.shields.io/github/v/release/JasperGuWP/dsh-plugin-whale-soulmate?sort=semver)](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/latest)
[![discussions](https://img.shields.io/github/discussions/JasperGuWP/dsh-plugin-whale-soulmate)](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/discussions)
[![CI](https://img.shields.io/github/actions/workflow/status/JasperGuWP/dsh-plugin-whale-soulmate/test.yml?branch=main)](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/actions/workflows/test.yml)

![Whale Soulmate · 7 套透明视频桌宠皮肤](docs/readme-banner-v2.png)

> **中文** · [English](#english)

嗨～这里住着一只给 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）用的**模块化、可插拔 AI 小伙伴（Soulmate）** 🐋

人设 × 情绪 × 关系养成 × **LLM Wiki 记忆** × **五道隐私防线** × **透明视频桌宠** × 可选 AIGC 云同步。

她也会当你的**办公 / 编程副驾**——陪你聊天的同时，DSH 本事一个都不少。

> ✨ **会一直养着、一直变可爱：** 这个仓库还在持续更新与打磨——修小毛刺、加新表情、把记忆和陪伴做得更懂你。欢迎 star / issue / PR，一起把小伙伴养得更好～

形态：**Bundle 组合包**（npm 包，`dsh.bundle.patch`），双半侧 —— node（`index.js`）+ browser（`client.js`）。

更完整的架构说明见 [`docs/DESIGN.md`](./docs/DESIGN.md)；版权与致谢见 [`NOTICE.md`](./NOTICE.md)。

## 新版亮点 · v0.2.131

- **无字幕也能听懂视频**：B 站官方字幕缺失或不匹配时，可从 playurl 提取音轨并调用外部 ASR；支持 OpenAI 兼容、阿里 DashScope、DeepSeek 原生和自定义 JSON 协议，并可从服务端拉取模型列表。
- **兴趣关键词只追加不覆盖**：手填关键词永久保留，自动学习词单独存储、去重后追加，最多 20 个；过滤系统字段与 URL 噪声，没有聊天内容时不学习。
- **定时冲浪更主动**：自动冲浪与深度观看默认开启，定时轮询会使用手填与学习关键词的并集；每周记忆蒸馏时也会从近聊补充兴趣词。
- **7 套桌宠皮肤补齐阵容**：高冷眼镜执事、深海经典、海盐苏打、午夜星空、汉风襦裙、Q版冬装男孩、蓝色冬装，覆盖不同人设与动作风格。
- **按需下载，不把安装包撑大**：汉风襦裙与 Q版冬装男孩随插件离线内置；其余 5 套首次选择时从 GitHub Releases 下载，按大小与 SHA-256 校验后缓存，之后可离线切换。
- **透明视频修复**：统一使用 VP9-alpha WebM，并保留 PNG 回退；修复部分环境中透明帧裂图、绿底或首帧异常的问题。
- **角色专属动作与情绪**：高冷执事保持克制冷脸，被拎起时会挣扎反击，被靠近时会示意你走开；日常会伏桌阅读、优雅吃牛排和靠桌小睡。其他桌宠也减少单一鼓脸表达，改用拒绝、侧身、跺脚等差异化动作。
- **统一蓝金视觉**：动作特效与界面氛围使用蓝、金、深海军蓝配色；新版介绍封面换成正确的 DeepSeek 标志，并以虚化标志作为背景。

## 不止桌宠：完整陪伴能力

### 陪伴与长期关系

- **会主动，但不打扰**：按本地生物钟和你的作息决定早安、催饭、晚间、催睡等时机；免打扰与每日主动次数都可配置。
- **真的记得你**：事实、Wiki、公开信与私密小本本组成混合记忆；会记住约定、处理信息冲突，也会按重要度与时间自然淡化。
- **一起生活**：夜间会把零散记忆蒸馏进 Wiki；桌宠可拖拽、轻触、双击互动、滚轮缩放，并随聊天情绪切换动作。
- **也是工作搭子**：闲聊之外仍保留 DSH 的完整工具链，可继续陪你写代码、读文档、处理办公任务。

### B站冲浪与视频理解

- **从分享链接开始看片**：支持 B 站链接、分享文本、BV / av 号；可“扫一眼”快速总结，也可认真看完再写长评。
- **不是只看标题**：综合元数据、字幕、分镜画面、弹幕高峰、热门评论与结构化摘要；观看结果可写入给你的信、小本本、照片墙和记忆。
- **会自己冲浪**：可根据聊天与记忆提炼兴趣关键词，定时巡游感兴趣的视频、热门内容与专栏文章，并维护去重记录。
- **登录与写入都受控**：可扫码登录 B 站；点赞、收藏、评论、私信、投稿等写操作默认关闭，开启后仍有配额、冷却、隐私过滤与审计，也可先 `dryRun` 预览。

### 微信 / QQ / 飞书 / 钉钉 Bot

- **跨端还是同一个 TA**：个人微信、QQ、飞书和钉钉共用同一个人设、心情与长期记忆，不在每个平台重新“认识”你一次。
- **微信扫码接入**：个人微信使用 iLink 官方 Bot 通道，可扫码登录、长轮询收消息并在聊天里按人设回复。
- **QQ 双模式**：支持 OneBot v11 / NapCat，也支持 QQ 官方 Bot API；飞书和钉钉提供各自的原生 Webhook / OpenAPI 接入。
- **密钥与记忆分开**：平台 Token、Cookie 等凭据单独保存在凭据文件，不写入人格或记忆；每条 IM 消息也会进入跨端对话时间线。

## 形象展示

7 套皮肤均可在「设置 → 称呼与形象」一键切换，静图与桌宠皮肤保持同步：

| 皮肤 | 角色定位 | 获取方式 |
|---|---|---|
| 高冷眼镜执事 | 半框眼镜与挂链，克制冷脸，包含挣扎反击、拒绝靠近、伏桌阅读、牛排用餐与靠桌小睡动作 | 首次选择下载 |
| 深海经典 | 经典深海女仆，锚链、鲸鱼围裙与蓝发鲸尾 | 首次选择下载 |
| 海盐苏打 | 白蓝水手女仆，轻快明亮的海盐系配色 | 首次选择下载 |
| 午夜星空 | 星座披纱与月光配饰，强调静谧、梦幻的夜间氛围 | 首次选择下载 |
| 汉风襦裙 | 蓝发鲸尾与海波襦裙，支持舞袖等国风动作 | 离线内置 |
| Q版冬装男孩 | 白蓝冬装与滑雪动作，适合冬日桌面陪伴 | 离线内置 |
| 蓝色冬装 | 鲸鱼连帽冬装，包含雪天与冬季趣味动作 | 首次选择下载 |

### 动作预览

| 汉风 · 襦裙 | Q版 · 冬装男孩 |
|:---:|:---:|
| ![汉风·襦裙 — 舞](docs/showcase/hanfu-dance.gif) | ![Q版·冬装男孩 — 滑雪](docs/showcase/winterboy-ski.gif) |

| 蓝色冬装 |
|:---:|
| ![蓝色冬装 — 卖火柴的小女孩](docs/showcase/bluewinter-game.gif) |

蓝色冬装在雪天划火柴、烤红薯、滑冰转圈。同一套动作概念，各自不同的编排。

桌宠为透明视频精灵：按住甩出去会重力弹跳、落地 Q 弹；单击轻触、双击互动、滚轮缩放。

🎬 **[演示视频 · 24 秒双皮肤动作集锦](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/download/v0.2.105/whale-soulmate-promo.mp4)**：跳舞 / 爱心脸红 / 生气跺脚 / 滑雪 / 跑步 / 打招呼 / 灵机一动，全部透明通道视频实机录制。

---

## 功能一览

| 能力 | 说明 |
|---|---|
| 零配置上手 | 装上重启后右下角冒出桌宠 + 引导；未授权云端时**零外网请求** |
| 人设引擎 | 多套预设、五维滑块、MBTI 测验、性别声线、自我成长与三档安全重置 |
| 长期陪伴 | 生物钟主动开口、承诺与关系记忆、双日记本、夜间梦蒸馏、情绪动作联动 |
| 混合记忆 | 事实 / Wiki / 日记；在场摘要、冲突裁决、语义遗忘，记忆可在 3D 星云中查看与维护 |
| 桌宠 | 7 套 PNG 回退 + VP9-alpha WebM 皮肤；拖拽 / 点击 / 思考 / 走路 / 专属动作 |
| 按需皮肤 | 首次选择从 GitHub Releases 下载，校验大小与 SHA-256，缓存后可离线使用 |
| B站冲浪 | 视频 / 专栏理解、兴趣学习、定时巡游、照片墙与记忆沉淀；写操作默认关闭且受风控 |
| 跨端 Bot | 个人微信 / QQ / 飞书 / 钉钉共用同一人设与记忆，支持回复、主动发送和对话时间线 |
| 隐私 | 五道防线 + 审计账本；私密记忆永不进云同步 |
| 副驾 | 双轨提示词 + 人设漂移重锚；完整调用宿主工具链 |

## 快速安装

三种方式都装**最新发布版**；已装过的再执行一次同样命令即升级到最新版。

```bash
# 方式一（推荐）：从 npm 拉最新版
dsh plugin --profile desktop add dsh-plugin-whale-soulmate
# web profile 同理：dsh plugin --profile web add dsh-plugin-whale-soulmate
```

```bash
# 方式二：从 GitHub Release 下载 tarball 安装（离线 / 指定渠道时用）
# https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/latest
dsh plugin --profile desktop add ./dsh-plugin-whale-soulmate-<version>.tgz
```

```bash
# 方式三：直接用仓库源码（构建脚本随包，安装时自动生成 client.js）
dsh plugin --profile desktop add github:JasperGuWP/dsh-plugin-whale-soulmate
```

```bash
# 本地开发：仓库根目录打包安装
npm pack
dsh plugin --profile desktop add ./dsh-plugin-whale-soulmate-<version>.tgz
```

> **务必装 tarball 或包名，不要装目录。** 目录会记成 `link:`，容易触发 `ERR_MODULE_NOT_FOUND`。  
> node 半侧**无热加载**：装完请重启 dsh 进程。

### 按需下载皮肤

默认内置「汉风 · 襦裙」和「Q版 · 冬装男孩」，不联网即可使用。面板里的其余皮肤标记为「首次下载」；选中后会从 [`pet-packs-v2` GitHub Release](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/tag/pet-packs-v2) 下载经过大小与 SHA-256 校验的皮肤包，之后从本地缓存离线读取。

缓存位置：`<soulmate home>/cache/pet-skins/pet-<皮肤id>`。

网络不可用时可手动准备普通皮肤目录；插件每次请求时也会扫描 `assets/pet-*/pet.json`：

```bash
# 一条命令：把素材文件夹（含 pet.json + pet-*.webm + pet-*.png）复制进已安装插件
node install-skin.mjs <素材文件夹> --id <皮肤id>
# 例：node install-skin.mjs ../output/pet-video-my-skin/assets --id my-skin
```

装完在面板「形象 / 桌面小伙伴」下拉里选中新皮肤即可，无需重新打包、无需重启。

也可（锁定 commit 更稳）：

```bash
dsh plugin --profile web add github:JasperGuWP/dsh-plugin-whale-soulmate#<sha>
```

本地 `--patch`（仅自用）：

```bash
dsh --patch ./cordis.patch.yml
```

## 使用片刻

1. 打开 DSH Web / Desktop，右下角出现桌宠；引导里选性格、填称呼（自动保存）。
2. 侧边栏「小鱼 / 设置」可改人设、信任层、作息、用量等。
3. 需要多端同步时，在设置里**显式授权**云端后再联网。

## 开发

```bash
npm run build:client     # browser/*.mjs → client.js
```

- 改前端请编辑 `browser/`，勿手改 `client.js`（构建产物，且默认不入库）。
- 改 node 后重启 dsh；改 browser 后重建并刷新页面。

## 仓库结构

```
index.js                 # node 入口
cordis.patch.yml         # Bundle / patch 声明
packages/soulmate-core/  # 记忆 / 人设 / 隐私 / 调度 / 路由 / 工具
packages/soulmate-home/  # 桌宠状态机
packages/soulmate-bili/  # B 站扩展
packages/soulmate-im/    # IM 扩展
browser/                 # 前端源模块
assets/pet-winterboy-chibi/  # 桌宠素材
docs/DESIGN.md           # 设计概览（中英）
NOTICE.md                # 版权与致谢
```

## 版权与许可

- 代码与文档：**MIT**，Copyright © 2026 JasperGuWP —— 见 [`LICENSE`](./LICENSE)
- 素材版权与第三方致谢 —— 见 [`NOTICE.md`](./NOTICE.md)

欢迎打主题标签 **`dsh-plugin`**，以便 [deepseek-harness 插件库](https://github.com/topics/dsh-plugin) 发现本仓库。

---

<a id="english"></a>

## English

Hi — a **modular, pluggable AI companion (Soulmate)** for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 🐋

persona × mood × relationship · **LLM Wiki memory** · **five privacy layers** · **transparent video desktop pet** · optional AIGC cloud sync.

Also your **coding / office co-pilot** — cuddles never strip host tools.

> ✨ **Kept cozy, kept improving:** this repo is actively maintained — polish, new pet moods, smarter memory & companionship. Stars, issues, and PRs are very welcome~

**Form:** dual-face **Bundle** (`dsh.bundle.patch`) — node (`index.js`) + browser (`client.js`).

Architecture: [`docs/DESIGN.md`](./docs/DESIGN.md) · Credits: [`NOTICE.md`](./NOTICE.md).

### Pet skins

Seven skins share the same one-click picker in Settings → Identity. Static avatars and desktop pets switch together:

| Skin | Character direction | Delivery |
|---|---|---|
| Cool Butler | Half-rim glasses with chain, restrained expressions, struggling counterattack, keeping distance, desk reading, steak dining, and desk-side nap motions | On first use |
| Deepsea Classic | Classic deep-sea maid with anchors, whale apron, and blue whale tail | On first use |
| Soda | Bright white-and-blue sailor maid with a lighter seaside mood | On first use |
| Starnight | Constellation veil and moonlit accessories for a quiet nighttime presence | On first use |
| Hanfu | Blue-haired whale companion in a wave-patterned ruqun with ribbon-dance motions | Bundled offline |
| Winter Boy | Chibi white-and-blue winter outfit with skiing and seasonal motions | Bundled offline |
| Blue Winter | Whale-hood winter outfit with playful snow-day actions | On first use |

| Hanfu · Ruqun | Chibi · Winter Boy |
|:---:|:---:|
| ![Hanfu skin — ribbon dance](docs/showcase/hanfu-dance.gif) | ![Winter boy skin — skiing](docs/showcase/winterboy-ski.gif) |

| Blue Winter |
|:---:|
| ![Blue winter skin — match girl](docs/showcase/bluewinter-game.gif) |

Transparent video sprites: flick-throw with gravity bounces and a landing squash; tap to pet, double-tap to nuzzle, wheel to zoom.

### What's new in v0.2.131

- **Understand videos without subtitles:** when official Bilibili subtitles are missing or mismatched, the plugin extracts audio from the play URL and calls external ASR. It supports OpenAI-compatible, Alibaba DashScope, native DeepSeek, and custom JSON protocols, including server-side model discovery.
- **Interest keywords are append-only:** manually entered keywords are never overwritten. Learned keywords live separately, are deduplicated, append up to 20 entries, filter system-field and URL noise, and are not generated when there is no chat context.
- **More proactive scheduled surfing:** auto-surf and deep watch are enabled by default, scheduled rounds use the union of manual and learned keywords, and weekly memory distillation can contribute additional interests from recent chats.
- **Seven-skin lineup:** Cool Butler, Deepsea Classic, Soda, Starnight, Hanfu, Winter Boy, and Blue Winter.
- **Smaller default install:** Hanfu and Winter Boy stay bundled offline; the other five skins download from GitHub Releases on first selection, are verified by size and SHA-256, and are then cached for offline use.
- **Transparent-video fixes:** VP9-alpha WebM with PNG fallback, plus fixes for broken, green, or incorrect first frames in some environments.
- **Character-specific motion:** the Cool Butler keeps a restrained expression while struggling when picked up, telling you to keep your distance, reading at his desk, dining on steak, or napping beside it; other pets use rejection, turn-away, and foot-stomp gestures instead of relying on one puffed-cheek reaction.
- **Blue-and-gold visual language:** motion effects and UI accents use blue, gold, and deep navy. The refreshed cover uses the correct DeepSeek mark with a blurred version in the background.

### More than a desktop pet

- **Companionship that remembers:** local-time proactive greetings, relationship growth, promises, public letters, private diaries, nightly memory distillation, and emotion-linked pet motions.
- **Bilibili surfing:** summarizes shared videos via metadata, subtitles, storyboard frames, danmaku peaks, and comments; learns interests and can patrol videos and articles on a schedule.
- **Guard-railed Bilibili account:** QR login is optional, every write action is opt-in and off by default, and likes, comments, DMs, uploads, and live actions remain quota-limited, audited, and dry-run capable.
- **Cross-platform IM presence:** the same persona and memory can answer on personal WeChat, QQ, Feishu, and DingTalk. WeChat uses iLink QR login; QQ supports OneBot/NapCat or the official Bot API.
- **Still a full co-pilot:** companionship adds a persona track without hiding DSH's coding, research, or office tools.

### Features

| Area | What you get |
|---|---|
| Zero-config | Pet + onboarding after install/restart; **no network** until cloud consent |
| Persona | Presets, 5-axis sliders, MBTI quiz, voice/gender, safe 3-tier reset |
| Companionship | Circadian proactive chat, promises, relationship growth, dual diaries, nightly dream distillation |
| Memory | Facts / Wiki / diaries; presence, conflicts, semantic decay, 3D memory-nebula tools |
| Desktop pet | Seven PNG + VP9-alpha WebM skins; drag / tap / think / walk / character-specific motions |
| On-demand skins | First-use download from GitHub Releases with size + SHA-256 checks and an offline cache |
| Bilibili | Video/article understanding, interest learning, scheduled surfing, memory/photo-wall capture, opt-in guarded writes |
| IM bots | Personal WeChat / QQ / Feishu / DingTalk sharing one persona, memory, and conversation timeline |
| Privacy | Five layers + audit ledger; private memories never sync |
| Co-pilot | Dual-track prompts + drift anchor; full host tool access |

### Install

All three channels install the **latest** release; re-running the same command upgrades an existing install.

```bash
# 1) from npm (recommended)
dsh plugin --profile desktop add dsh-plugin-whale-soulmate

# 2) from the latest GitHub Release tarball
# https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/latest
dsh plugin --profile desktop add ./dsh-plugin-whale-soulmate-<version>.tgz

# 3) straight from the repository (prepare builds client.js at install time)
dsh plugin --profile desktop add github:JasperGuWP/dsh-plugin-whale-soulmate
```

Install the **tarball or package name**, not a directory. Restart dsh (node half is not hot-reloadable).

Optional skins are fetched from the [`pet-packs-v2` GitHub Release](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/tag/pet-packs-v2) and cached at `<soulmate home>/cache/pet-skins/pet-<skin-id>`. For offline/manual installs, `node install-skin.mjs <asset-folder> --id <skin-id>` copies a normal pack into the installed plugin; skins are discovered per request and listed in the panel dropdowns.

```bash
dsh plugin --profile web add github:JasperGuWP/dsh-plugin-whale-soulmate#<sha>
```

### Develop

```bash
npm run build:client   # browser/*.mjs → client.js
```

Edit `browser/` sources; do not hand-edit generated `client.js`.

### License & credits

- Code & docs: **MIT**, Copyright © 2026 JasperGuWP — [`LICENSE`](./LICENSE)
- Asset copyright & third-party thanks — [`NOTICE.md`](./NOTICE.md)

Please tag the repo with **`dsh-plugin`** so the harness plugin library can discover it.
