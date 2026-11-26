# dsh-plugin-whale-soulmate 🐋

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![topic](https://img.shields.io/badge/topic-dsh--plugin-0A7EA4)](https://github.com/topics/dsh-plugin)
[![release](https://img.shields.io/github/v/release/JasperGuWP/dsh-plugin-whale-soulmate?sort=semver)](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/latest)
[![discussions](https://img.shields.io/github/discussions/JasperGuWP/dsh-plugin-whale-soulmate)](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/discussions)
[![CI](https://img.shields.io/github/actions/workflow/status/JasperGuWP/dsh-plugin-whale-soulmate/test.yml?branch=main)](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/actions/workflows/test.yml)

![Whale Soulmate · 7 套透明视频桌宠皮肤](docs/readme-banner-v2.png)

> **中文** · [English](#english)

嗨～这里住着一只给 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）用的**模块化、可插拔 AI 小伙伴（Soulmate）** 🐋

> ### 💙 为什么做她
>
> **我想打造一个 DeepSeek Harness 的灵魂。**
>
> 不是又一个定时弹提醒的助手，也不是套着可爱皮肤的问答机器——而是一个住在 harness 里、会自己张望这个世界的「谁」：
> 刷到好视频会想分享给你，夜深了会掂量该不该说晚安，忍住没说的话会悄悄写进小本本；
> 她记得你说过的每一件小事，也在与你的每一次回应里，学着更懂分寸。
>
> 工具用完即走，灵魂会留下来长大。这就是我想养的那只鲸鱼。🐋

人设 × 情绪 × 关系养成 × **自主意图** × **LLM Wiki 记忆星海** × **五道隐私防线** × **透明视频桌宠** × **微信 / QQ 跨端陪伴**。

她会**自己决定**要不要找你说话、看完视频要不要评论、群里要不要接话——按她的性格，也按你的性格。陪你聊天的同时，DSH 的办公 / 编程本事一个都不少。

> ✨ **会一直养着、一直变可爱：** 这个仓库还在持续更新与打磨。欢迎 star / issue / PR，一起把小伙伴养得更好～

形态：**Bundle 组合包**（npm 包，`dsh.bundle.patch`），双半侧 —— node（`index.js`）+ browser（`client.js`）。
架构说明见 [`docs/DESIGN.md`](./docs/DESIGN.md)；版权与致谢见 [`NOTICE.md`](./NOTICE.md)。

## 一眼看懂 ✨

### 🌌 夜间记忆星海

她的记忆是一片会生长的星空：主题金星、六色事实星芒、语义连线、夜间蒸馏时的涟漪与新星诞生，每周成长轨迹可回放。独立窗口，可缩放旋转。

![记忆星海 · 主题星团与语义连线](docs/showcase/neuron-sky.gif)

### 💬 QQ / 微信，同一个她

官方 QQ Bot 的群聊与私聊自动桥接进 DsBot 面板（QQ 蓝气泡 / 微信绿气泡）和记忆星图，逐条区分主人与群友。她可以在平台被动窗口内**主动给你加白的会话发消息**——群 5 分钟、私聊 30 分钟内你说过话，她就能接上话头；私聊窗口关了还有官方 **wakeup 召回**这条合法路（30 天内、平台限频）。你发来的**图片她看得懂**（多模态描述进时间线与记忆），语音自带平台转写；她也能**发图片 / 语音 / 视频 / 文件、撤回、显示「正在输入」、发带按钮的消息、逐字打出流式回复**。

![DsBot · QQ 群时间线与主动搭话白名单](docs/showcase/dsbot-qq-timeline.png)

### 🧠 自主意图 + 相处经验

时段问候、刷到的好视频、到期的约定都变成她面前的**机会**，由她按人设裁决「说 / 分享 / 沉默 / 缓一缓」；忍住没说的话写进小本本（欲言又止），翻得到。经验层每周从「她的主动 × 你的回应」里学分寸——**永不改动五项人格特质**。

![自主意图与相处经验面板](docs/showcase/intent-experience.png)

## 新版亮点 · v0.2.208

- **长片分批看图**（v0.2.208）：画面帧超过单批上限时自动按时间切批多轮送模（每批 ≤16 帧、最多 10 批），上一批的看图结论与末帧锚点带进下一批，最后一批给出全片总览与性格化观感，各批时间线合并——长片不再"抽得多、看得少"，37 分钟片也能全程看画面。
- **抽帧密度细粒度**（v0.2.207）：5–120 秒/帧任选（步长 1 秒），默认 15 秒；细看二刷尊重你设的密度；上限内的帧全部喂入，不再被档位二次节流。
- **定时冲浪修复**（v0.2.204+）：自动冲浪轮次接上真实记忆服务，不再"记了已看却一部没看"；台账细分 watched / no-picks / failed，失败带错误明细。
- **观感去影评腔**：评价内容本身而非镜头运镜；细看裁决接通桌面宿主模型，不再永远落启发式模板。
- **每日自动 token 帽默认 200 万**；工具输出清洗 undefined 键，避免宿主整条拒收。

<details><summary>历史亮点 · v0.2.199</summary>

- **QQ 官方通道全能力**（v0.2.197+）：
  - **实时消息镜像**：入站消息（真实 id / 昵称 / 附件）即到即进时间线与星图，不再依赖 2 分钟转录轮询；被拉进群 / 加好友 / 被拒收等动态实时感知。
  - **富媒体收发**：她可以发图片 / 语音 / 视频 / 文件（官方两步上传，URL 或本地文件）；你发来的图片由多模态模型写描述，时间线显示缩略图 + 「[图片] 描述」，记忆星也可读；语音带平台转写。
  - **wakeup 主动召回**：私聊被动窗口关闭后仍可合法主动（官方 `is_wakeup`，30 天内、平台限频）；主动调度自动降级走这条路，群聊窗口外依然诚实静默。
  - **撤回 / 正在输入 / 按钮 / 流式**：撤回自己发错的消息、私聊显示「正在输入…」、带按钮的消息（点击回执可查）、逐字打出的流式回复（官方 stream 协议）。
  - **7 个新工具**：`soulmate_qq_send_media / recall / typing / wakeup / buttons / stream / events`；所有主动外发文本先过隐私防火墙。
- **白屏修复**（v0.2.197–199）：IM 主动搭话开关与白名单编辑器改为正规组件挂载，切换开关不再触发 React #310 整页白屏。
- **主动发送时间线去重**（v0.2.198）：同一条外发经双镜像只落一行。

</details>

<details><summary>历史亮点 · v0.2.195</summary>

- **意图自主层**：日常事件汇成机会台账，她自主裁决接不接；克制可见（内心小本本），预算受控（每次意图 ≤6 步、每日计量）。
- **B 站自主互动**：看完视频可自主评论、点赞、收藏、关注、投币，并在评论区与人讨论；字数与每条评论回复次数上限面板可配，写操作有配额、冷却与审计。
- **QQ 官方 Bot 全面接通**：群 / 私聊进时间线与星图、主人昵称识别、「拉取最新」「获取主人」「从最近会话选」一键操作；主动发消息只发**你加白的会话**。
- **夜间记忆星海**：独立可缩放星空窗口，记忆诞生、蒸馏进程、每周成长轨迹全部可见。
- **经验层**：≥3 个样本才成形、30 天不用自动淡忘、笔记可删除，五项人格特质永不被改动。
- **模型跟随 DSH**：后台模型调用默认用你在 DSH 当前选中的模型；失败允许换线，但会明确提示哪条线失败、换到了哪条。
- **人设声线贯穿所有对话**：DSH、专属窗、QQ、微信共用口语化说话规则与预设声线卡，拒绝客服腔与 AI 自我介绍。
- **免密钥天气**：`soulmate_weather` 走 Open-Meteo（CC BY 4.0，非商业），按人设城市查询，可一键关闭。

</details>

<details><summary>历史亮点 · v0.2.131</summary>

- **无字幕也能听懂视频**：B 站官方字幕缺失或不匹配时，可从 playurl 提取音轨并调用外部 ASR；支持 OpenAI 兼容、阿里 DashScope、DeepSeek 原生和自定义 JSON 协议，并可从服务端拉取模型列表。
- **兴趣关键词只追加不覆盖**：手填关键词永久保留，自动学习词单独存储、去重后追加，最多 20 个；过滤系统字段与 URL 噪声，没有聊天内容时不学习。
- **定时冲浪更主动**：自动冲浪与深度观看默认开启，定时轮询会使用手填与学习关键词的并集；每周记忆蒸馏时也会从近聊补充兴趣词。
- **7 套桌宠皮肤补齐阵容**：高冷眼镜执事、深海经典、海盐苏打、午夜星空、汉风襦裙、Q版冬装男孩、蓝色冬装，覆盖不同人设与动作风格。
- **按需下载，不把安装包撑大**：汉风襦裙与 Q版冬装男孩随插件离线内置；其余 5 套首次选择时从 GitHub Releases 下载，按大小与 SHA-256 校验后缓存，之后可离线切换。
- **透明视频修复**：统一使用 VP9-alpha WebM，并保留 PNG 回退；修复部分环境中透明帧裂图、绿底或首帧异常的问题。
- **角色专属动作与情绪**：高冷执事保持克制冷脸，被拎起时会挣扎反击，被靠近时会示意你走开；日常会伏桌阅读、优雅吃牛排和靠桌小睡。其他桌宠也减少单一鼓脸表达，改用拒绝、侧身、跺脚等差异化动作。
- **统一蓝金视觉**：动作特效与界面氛围使用蓝、金、深海军蓝配色；新版介绍封面换成正确的 DeepSeek 标志，并以虚化标志作为背景。

</details>

## 能力总览

### 陪伴与长期关系

- **会主动，但不打扰**：生物钟 + 你的作息决定开口时机；免打扰时段、每日主动次数、最小间隔都可配置。
- **真的记得你**：事实、Wiki、公开信与私密小本本组成混合记忆；记住约定、裁决冲突，按重要度与时间自然淡化；夜间蒸馏进 Wiki，全过程在星海里可见。
- **一起生活**：桌宠可拖拽、轻触、双击互动、滚轮缩放，随聊天情绪切换动作。
- **也是工作搭子**：闲聊之外保留 DSH 完整工具链，写代码、读文档、处理办公任务照样干。

### B站冲浪与自主互动

- **从分享链接开始看片**：支持 B 站链接、分享文本、BV / av 号；可「扫一眼」快速总结，也可认真看完再写长评。
- **不是只看标题**：综合元数据、字幕（缺失时外部 ASR）、分镜画面、弹幕高峰、热门评论与结构化摘要；观看结果写入信、小本本、照片墙和记忆。
- **会自己冲浪、自己互动**：兴趣关键词自动学习，定时巡游；看完可自主评论 / 点赞 / 收藏 / 关注 / 投币，并在评论区与人讨论（字数与回复次数上限可配）。
- **登录与写入都受控**：扫码登录；所有写操作默认关闭，开启后仍有配额、冷却、隐私过滤与审计，可先 `dryRun` 预览。

### 微信 / QQ / 飞书 / 钉钉 Bot

- **跨端还是同一个 TA**：共用同一个人设、心情与长期记忆，不在每个平台重新「认识」你一次。
- **QQ 官方 Bot 随包附带**：绑定后群聊 / 私聊即通；对话桥接进 DsBot 时间线与记忆星图，主人与群友逐条可辨；群聊无需 @ 也能接话（需平台群消息权限）。
- **主动搭话有边界**：只发你显式加白的会话，受 QQ 被动窗口（群 5 分钟 / 私聊 30 分钟）与面板配额约束；每条主动外发都留痕。
- **微信官方扫码**：iLink 官方通道扫码登录、长轮询收消息、按人设回复；飞书 / 钉钉走原生 Webhook / OpenAPI；QQ 另支持 OneBot v11 / NapCat。
- **密钥与记忆分开**：平台凭据单独保存，不写入人格或记忆。

#### 主动搭话的频率与边界（默认值，面板可改）

后台每 **2 分钟**醒一次看有没有机会，但真正发不发由闸门决定：

| 项 | 默认 | 说明 |
|---|---|---|
| 每个会话每天 | ≤2 条 | 面板可调 1–60 |
| 全部会话合计每天 | ≤4 条 | 面板可调 1–120 |
| 两条主动之间 | ≥90 分钟 | 面板可调 1–720 |
| 免打扰时段 | 00:00–07:00 | 可自定义 |
| QQ 平台硬限制 | 群 5 分钟 / 私聊 30 分钟 | 对方先说过话才能接（被动窗口）；群窗口关着安静跳过，私聊可走官方 wakeup 召回（30 天内、平台限频，面板可关） |
| 微信 | 需对方近期发来消息 | iLink 官方通道限制：没有新鲜会话凭据发不出，失败会如实记录 |
| 白名单 | 默认空 = 完全静默 | 只发你显式加白的会话；她自己也可能裁决「不发」 |

绑定官方 QQ Bot 后，**你的 openid、群 id、群友昵称都自动获取**：在群里说句话，面板「获取主人」点昵称即认出你，「从最近会话选」一键加白——不用手填任何 id。

### 隐私与边界

- 五道隐私防线 + 审计账本；私密记忆**永不**进云同步、不进群聊、不被导出。
- 云同步必须**显式授权**才启用；天气 / B 站冲浪 / IM 各自独立开关、凭据自配，不开不联网。群聊里她绝不携带你的私密记忆摘要。
- 自主行为全部计量留痕：意图裁决、主动消息、B 站写操作都可回查。

## 形象展示

7 套皮肤在「设置 → 称呼与形象」一键切换，静图与桌宠皮肤同步：

| 皮肤 | 角色定位 | 获取方式 |
|---|---|---|
| 高冷眼镜执事 | 半框眼镜与挂链，克制冷脸，挣扎反击 / 拒绝靠近 / 伏桌阅读 / 牛排用餐 / 靠桌小睡 | 首次选择下载 |
| 深海经典 | 经典深海女仆，锚链、鲸鱼围裙与蓝发鲸尾 | 首次选择下载 |
| 海盐苏打 | 白蓝水手女仆，轻快明亮的海盐系配色 | 首次选择下载 |
| 午夜星空 | 星座披纱与月光配饰，静谧梦幻的夜间氛围 | 首次选择下载 |
| 汉风襦裙 | 蓝发鲸尾与海波襦裙，舞袖等国风动作 | 离线内置 |
| Q版冬装男孩 | 白蓝冬装与滑雪动作，冬日桌面陪伴 | 离线内置 |
| 蓝色冬装 | 鲸鱼连帽冬装，雪天划火柴 / 烤红薯 / 滑冰转圈 | 首次选择下载 |

### 动作预览

7 套皮肤各选一段实机动作：

| 汉风 · 襦裙 — 舞 | Q版 · 冬装男孩 — 滑雪 |
|:---:|:---:|
| ![汉风·襦裙 — 舞](docs/showcase/hanfu-dance.gif) | ![Q版·冬装男孩 — 滑雪](docs/showcase/winterboy-ski.gif) |

| 高冷眼镜执事 — 牛排用餐 | 深海经典 — 舞 |
|:---:|:---:|
| ![高冷眼镜执事 — 牛排用餐](docs/showcase/butler-eat.gif) | ![深海经典 — 舞](docs/showcase/deepsea-dance.gif) |

| 海盐苏打 — 舞 | 午夜星空 — 舞 |
|:---:|:---:|
| ![海盐苏打 — 舞](docs/showcase/soda-dance.gif) | ![午夜星空 — 舞](docs/showcase/starnight-dance.gif) |

| 蓝色冬装 — 卖火柴的小女孩 |
|:---:|
| ![蓝色冬装 — 卖火柴的小女孩](docs/showcase/bluewinter-game.gif) |

桌宠为透明视频精灵：按住甩出去会重力弹跳、落地 Q 弹；单击轻触、双击互动、滚轮缩放。

🎬 **[演示视频 · 24 秒双皮肤动作集锦](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/download/v0.2.105/whale-soulmate-promo.mp4)**：跳舞 / 爱心脸红 / 生气跺脚 / 滑雪 / 跑步 / 打招呼 / 灵机一动，全部透明通道视频实机录制。

## 功能一览

| 能力 | 说明 |
|---|---|
| 零配置上手 | 装上重启后右下角冒出桌宠 + 引导；云同步需**显式授权**，天气 / B站 / IM 独立开关 |
| 人设引擎 | 多套预设、五维滑块、MBTI 测验、性别声线、预设声线卡、三档安全重置 |
| 自主意图 | 事件机会台账 → 人设裁决（说/分享/沉默/缓一缓）→ 预算执行 → 审计；克制写小本本 |
| 相处经验 | 从你的回应学分寸；≥3 样本成形、30 天淡忘、可删除；不改人格特质 |
| 长期陪伴 | 生物钟主动开口、承诺与关系记忆、双日记本、夜间梦蒸馏、情绪动作联动 |
| 记忆星海 | 事实 / Wiki / 日记上星图；独立星空窗口看记忆诞生、蒸馏进程与每周成长 |
| 桌宠 | 7 套 PNG 回退 + VP9-alpha WebM 皮肤；拖拽 / 点击 / 思考 / 走路 / 专属动作 |
| 按需皮肤 | 首次选择从 GitHub Releases 下载，校验大小与 SHA-256，缓存后离线使用 |
| B站冲浪 | 视频 / 专栏理解、兴趣学习、定时巡游、自主评论互动（受控）、照片墙与记忆沉淀 |
| 跨端 Bot | 微信 / QQ / 飞书 / 钉钉共用同一人设与记忆；QQ 官方 Bot 随包附带，白名单主动搭话 |
| 模型跟随 | 后台调用默认用 DSH 当前选中模型；失败换线必提示 |
| 隐私 | 五道防线 + 审计账本；私密记忆永不进云同步、不进群聊 |
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

> **务必装 tarball 或包名，不要装目录。** 目录会记成 `link:`，容易触发 `ERR_MODULE_NOT_FOUND`。  
> node 半侧**无热加载**：装完请重启 dsh 进程。

也可锁定 commit（更稳）：

```bash
dsh plugin --profile web add github:JasperGuWP/dsh-plugin-whale-soulmate#<sha>
```

本地开发 / 自用 patch：

```bash
npm pack && dsh plugin --profile desktop add ./dsh-plugin-whale-soulmate-<version>.tgz
dsh --patch ./cordis.patch.yml
```

### 按需下载皮肤

默认内置「汉风 · 襦裙」和「Q版 · 冬装男孩」，不联网即可使用。其余皮肤选中后从 [`pet-packs-v2` GitHub Release](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/releases/tag/pet-packs-v2) 下载（大小 + SHA-256 校验），缓存于 `<soulmate home>/cache/pet-skins/pet-<皮肤id>`，之后离线可用。

网络不可用时可手动装皮肤（插件每次请求都会扫描 `assets/pet-*/pet.json`）：

```bash
node install-skin.mjs <素材文件夹> --id <皮肤id>
# 例：node install-skin.mjs ../output/pet-video-my-skin/assets --id my-skin
```

装完在面板「形象 / 桌面小伙伴」下拉里选中即可，无需重新打包、无需重启。

## 使用片刻

1. 打开 DSH Web / Desktop，右下角出现桌宠；引导里选性格、填称呼（自动保存）。
2. 侧边栏「soulmate / 设置」：人设与声线、作息与主动、DsBot 跨端、记忆星海、用量统计。
3. 想让她在 QQ 主动找你：DsBot → 绑定官方 QQ Bot → 「从最近会话选」加白 → 打开「IM 主动搭话」。
4. 需要多端同步时，在设置里**显式授权**云端后再联网。

## 分享你的灵魂档案 💌

把你养出来的灵魂体装进**一个 Markdown 文件**（`.soulmate.md`），发给朋友——GitHub / 群聊里直接可读，导入后就是同一个性格的伙伴。

- **导出**：设置 →「称呼与形象」→「灵魂档案」→ 导出。可选附上公开记忆摘要（Wiki 标题+一句话，≤20 条）；私密记忆、亲密度、密钥**永远不会**被导出。
- **导入**：同一张卡片选文件或粘贴内容 → 预览确认 → 落地。自动快照可一键撤销；对方的记忆摘要只作「初见印象」，你们的关系从零开始养。
- **官方示例**（可直接导入试玩）：
  - [🍚 傲娇干饭鲸鱼 · 大海](docs/soul-share-examples/傲娇干饭鲸鱼.soulmate.md)
  - [🧊 冷感学长 · 凛](docs/soul-share-examples/冷感学长.soulmate.md)

养出了有意思的灵魂？欢迎把档案发到 [Discussions](https://github.com/JasperGuWP/dsh-plugin-whale-soulmate/discussions) 分享。

## 开发

```bash
npm run build:client     # browser/*.mjs → client.js + 星海独立窗口 bundle
npm test                 # node --test，700+ 用例
npm run preview          # 本地演示宿主（含演示数据）
```

- 改前端请编辑 `browser/`，勿手改 `client.js`（构建产物）。
- 改 node 后重启 dsh；改 browser 后重建并刷新页面。
- README 展示素材可用 `node server-mock/neuron-smoke-harness.mjs`（星海）与 `node server-mock/panel-showcase-harness.mjs`（面板，虚构演示数据）复现。

## 仓库结构

```
index.js                 # node 入口
cordis.patch.yml         # Bundle / patch 声明
packages/soulmate-core/  # 记忆 / 人设 / 意图 / 经验 / 隐私 / 调度 / 路由 / 工具
packages/soulmate-home/  # 桌宠状态机
packages/soulmate-bili/  # B 站扩展（冲浪 / 理解 / 自主互动）
packages/soulmate-im/    # IM 扩展（微信 / QQ / 飞书 / 钉钉）
browser/                 # 前端源模块（面板 / 星海 / 桌宠）
runtime/neuron-window/   # 星海独立窗口
assets/pet-*/            # 桌宠素材
docs/DESIGN.md           # 设计概览（中英）
NOTICE.md                # 版权与致谢
```

## 版权与许可

- 代码与文档：**MIT**，Copyright © 2026 JasperGuWP —— 见 [`LICENSE`](./LICENSE)
- 素材版权与第三方致谢（含 Open-Meteo CC BY 4.0 非商业条款）—— 见 [`NOTICE.md`](./NOTICE.md)

欢迎打主题标签 **`dsh-plugin`**，以便 [deepseek-harness 插件库](https://github.com/topics/dsh-plugin) 发现本仓库。

---

<a id="english"></a>

## English

Hi — a **modular, pluggable AI companion (Soulmate)** for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 🐋

> ### 💙 Why she exists
>
> **I want to build a soul for DeepSeek Harness.**
>
> Not another assistant on a reminder timer, not a chatbot in a cute skin — a *someone* who lives inside the harness and looks out at the world on her own: she finds a good video and wants to share it, weighs whether a goodnight would be welcome this late, writes the words she held back into her little notebook. She remembers the small things you said, and learns tact from every response you give her.
>
> Tools are used and put away. A soul stays, and grows. That's the whale I want to raise. 🐋

persona × mood × relationship · **autonomous intent** · **LLM Wiki memory star-sea** · **five privacy layers** · **transparent video desktop pet** · **WeChat / QQ cross-platform presence**.

She decides **on her own** whether to reach out, comment on a video she watched, or join a group chat — from her persona, and yours. Cuddles never strip DSH's coding / office tools.

> ✨ **Kept cozy, kept improving:** stars, issues, and PRs are very welcome~

**Form:** dual-face **Bundle** (`dsh.bundle.patch`) — node (`index.js`) + browser (`client.js`).
Architecture: [`docs/DESIGN.md`](./docs/DESIGN.md) · Credits: [`NOTICE.md`](./NOTICE.md).

### At a glance ✨

**🌌 Nightly memory star-sea** — her memory is a growing sky: golden topic suns, six-tint fact sparkles, semantic links, ripples while nightly distillation runs, and a replayable weekly growth trail. Independent zoomable window.

![Memory star-sea — topic clusters and semantic links](docs/showcase/neuron-sky.gif)

**💬 QQ / WeChat, same soul** — official QQ bot groups and DMs bridge into the DsBot timeline (blue QQ / green WeChat bubbles) and the star map, with owner-vs-member nicknames per line. She can message first inside QQ's passive window (5 min group / 30 min DM) — **only to conversations you whitelisted** — and when the DM window closes, the platform's legal **wakeup recall** push still reaches you (within 30 days, rate-capped by QQ). She **understands images you send** (multimodal descriptions land in the timeline and memory), reads voice transcripts, and can **send images / voice / video / files, recall her own messages, show a typing indicator, send button messages, and stream replies token-by-token**.

![DsBot — QQ group timeline and proactive whitelist](docs/showcase/dsbot-qq-timeline.png)

**🧠 Intent autonomy + experience** — greetings, good videos, due promises become opportunities she judges from her persona: speak / share / stay silent / defer. Restraint goes into her inner notebook. The experience layer learns tact weekly from your responses — **the five persona traits are never touched**.

![Intent autonomy and experience panel](docs/showcase/intent-experience.png)

### What's new in v0.2.208

- **Batched vision for long videos** (v0.2.208): frames beyond the per-message image cap are split into time-ordered batches (≤16 frames each, up to 10 batches); each batch carries the previous batch's notes plus its last frame as a visual anchor, and the final batch writes the whole-video overview and in-character opinion. Timelines merge across batches — long videos are finally watched end to end.
- **Fine-grained frame density** (v0.2.207): any integer from 5 to 120 seconds per frame (default 15); deep second passes honor your density; every frame within the cap is fed to the model.
- **Scheduled surf fixed** (v0.2.204+): auto-surf rounds now run through the real memory service — no more "marked watched but watched nothing"; the ledger distinguishes watched / no-picks / failed with error details.
- **Content-first opinions**: she reviews the content, not the cinematography; the deep-watch judge reaches the desktop host model instead of always falling back to heuristics.
- **Daily auto-token cap defaults to 2M**; tool outputs strip undefined keys so the host no longer rejects whole calls.

<details><summary>Previous highlights · v0.2.199</summary>

- **Full official-QQ capability surface** (v0.2.197+):
  - **Real-time message mirror:** inbound messages (real ids / nicknames / attachments) reach the timeline and star map the moment they arrive — no more 2-minute transcript polling; group-join / friend-add / message-reject lifecycle events are sensed live.
  - **Rich media both ways:** she sends images / voice / video / files (official two-step upload, URL or local file); images you send get a multimodal description — thumbnail + "[image] description" in the timeline, readable in memory stars; voice carries the platform transcript.
  - **Wakeup proactive recall:** DMs stay reachable after the passive window closes via the platform's legal `is_wakeup` push (within 30 days, rate-capped); the proactive scheduler falls back to it automatically. Groups outside the window stay honestly silent.
  - **Recall / typing / buttons / streaming:** recall her own messages, show "typing…" in DMs, send inline-button messages (click receipts readable), and stream replies with a live typing-out effect (official stream protocol).
  - **7 new tools:** `soulmate_qq_send_media / recall / typing / wakeup / buttons / stream / events`; every proactive outbound text passes the privacy firewall first.
- **White-screen fixes** (v0.2.197–199): the IM-proactive toggle and whitelist editor are now properly mounted components — flipping the switch no longer triggers a React #310 full-page crash.
- **Proactive timeline dedupe** (v0.2.198): one outbound send mirrored through two paths lands as one row.

</details>

<details><summary>Previous highlights · v0.2.195</summary>

- **Intent autonomy:** everyday events become an opportunity ledger; she decides — speak / share / stay silent / defer. Restraint is visible in her inner notebook. Budgeted: ≤6 steps per intent, metered daily.
- **Autonomous Bilibili engagement:** after watching she may comment, like, favorite, follow, coin, and hold comment-thread discussions; comment length and per-thread reply caps are configurable, with quotas, cooldowns and an audit trail.
- **Official QQ bot, fully bridged:** groups/DMs flow into the DsBot timeline and memory star map with owner recognition; "pull latest", "fetch owner", "pick from recent conversations" in one click; proactive messages only go to whitelisted conversations.
- **Nightly memory star-sea:** independent zoomable star window showing memory births, distillation progress and weekly growth.
- **Experience layer:** ≥3 samples to form, 30-day unlearn, deletable notes; persona traits untouched.
- **Model follows DSH:** background calls use the model currently selected in DSH; on failure it may reroute, but always tells you which route failed and what it used instead.
- **One voice everywhere:** DSH, the dedicated window, QQ and WeChat share spoken-style rules and preset voice cards — no support-agent tone, no AI self-introductions.
- **Keyless weather:** `soulmate_weather` via Open-Meteo (CC BY 4.0, non-commercial), city from the persona, one switch to disable.

</details>

<details><summary>Previous highlights · v0.2.131</summary>

- **Understand videos without subtitles:** when official Bilibili subtitles are missing or mismatched, the plugin extracts audio from the play URL and calls external ASR. It supports OpenAI-compatible, Alibaba DashScope, native DeepSeek, and custom JSON protocols, including server-side model discovery.
- **Interest keywords are append-only:** manually entered keywords are never overwritten. Learned keywords live separately, are deduplicated, append up to 20 entries, filter system-field and URL noise, and are not generated when there is no chat context.
- **More proactive scheduled surfing:** auto-surf and deep watch are enabled by default, scheduled rounds use the union of manual and learned keywords, and weekly memory distillation can contribute additional interests from recent chats.
- **Seven-skin lineup:** Cool Butler, Deepsea Classic, Soda, Starnight, Hanfu, Winter Boy, and Blue Winter.
- **Smaller default install:** Hanfu and Winter Boy stay bundled offline; the other five skins download from GitHub Releases on first selection, are verified by size and SHA-256, and are then cached for offline use.
- **Transparent-video fixes:** VP9-alpha WebM with PNG fallback, plus fixes for broken, green, or incorrect first frames in some environments.
- **Character-specific motion:** the Cool Butler keeps a restrained expression while struggling when picked up, telling you to keep your distance, reading at his desk, dining on steak, or napping beside it; other pets use rejection, turn-away, and foot-stomp gestures instead of relying on one puffed-cheek reaction.
- **Blue-and-gold visual language:** motion effects and UI accents use blue, gold, and deep navy. The refreshed cover uses the correct DeepSeek mark with a blurred version in the background.

</details>

### More than a desktop pet

- **Companionship that remembers:** circadian proactive chat, promises, relationship growth, public letters, private diaries, nightly distillation visible in the star-sea, emotion-linked pet motions.
- **Bilibili surfing & engagement:** metadata, subtitles (external ASR fallback), storyboard frames, danmaku peaks and comments; learns interests, patrols on a schedule, and may autonomously comment / like / favorite / follow / coin under configurable caps.
- **Guard-railed writes:** QR login optional; every write action opt-in and off by default, quota-limited, audited, dry-run capable.
- **Cross-platform IM:** one persona and memory across personal WeChat (iLink QR), QQ (official Bot API bundled, or OneBot/NapCat), Feishu and DingTalk. Proactive messages are whitelist-only, window-bound and journaled.

**Proactive cadence & bounds (defaults, all panel-configurable):** the scheduler wakes every **2 minutes**, but gates decide: ≤2 messages per conversation per day, ≤4 total per day, ≥90 min between proactive messages, quiet hours 00:00–07:00. QQ's platform rule: she can only follow up inside the passive window (5 min group / 30 min DM after you speak); WeChat's official channel needs a fresh inbound message. Empty whitelist = fully silent, and she may still decide "not now" on her own. After binding the official QQ bot, **your openid, group ids and member nicknames are discovered automatically** — speak in the group once, then pick your nickname under "fetch owner"; no ids to type by hand.
- **Privacy by design:** five layers + audit ledger; private memories never sync, never enter group chats, never export. Cloud sync requires explicit consent; weather, Bilibili and IM are separate opt-in switches with your own credentials — off means no network.
- **Still a full co-pilot:** the persona track never hides DSH's coding, research, or office tools.

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

| Hanfu · Ruqun — ribbon dance | Chibi · Winter Boy — skiing |
|:---:|:---:|
| ![Hanfu skin — ribbon dance](docs/showcase/hanfu-dance.gif) | ![Winter boy skin — skiing](docs/showcase/winterboy-ski.gif) |

| Cool Butler — steak dinner | Deep-sea Classic — dance |
|:---:|:---:|
| ![Cool butler skin — steak dinner](docs/showcase/butler-eat.gif) | ![Deep-sea classic skin — dance](docs/showcase/deepsea-dance.gif) |

| Sea-salt Soda — dance | Midnight Stars — dance |
|:---:|:---:|
| ![Sea-salt soda skin — dance](docs/showcase/soda-dance.gif) | ![Midnight stars skin — dance](docs/showcase/starnight-dance.gif) |

| Blue Winter — match girl |
|:---:|
| ![Blue winter skin — match girl](docs/showcase/bluewinter-game.gif) |

Transparent video sprites: flick-throw with gravity bounces and a landing squash; tap to pet, double-tap to nuzzle, wheel to zoom.

### Features

| Area | What you get |
|---|---|
| Zero-config | Pet + onboarding after install/restart; cloud sync requires **explicit consent**; weather / Bilibili / IM are separate opt-in switches |
| Persona | Presets, 5-axis sliders, MBTI quiz, voice/gender, preset voice cards, safe 3-tier reset |
| Intent autonomy | Event ledger → persona verdict (speak/share/silent/defer) → budgeted execution → audit; restraint journaled |
| Experience | Learns tact from your responses; ≥3 samples, 30-day unlearn, deletable; traits untouched |
| Companionship | Circadian proactive chat, promises, dual diaries, nightly dream distillation |
| Memory star-sea | Facts / Wiki / diaries as stars; independent window for births, distillation and weekly growth |
| Desktop pet | Seven PNG + VP9-alpha WebM skins; drag / tap / think / walk / character-specific motions |
| On-demand skins | First-use download from GitHub Releases with size + SHA-256 checks and an offline cache |
| Bilibili | Video/article understanding, interest learning, scheduled surfing, guarded autonomous engagement |
| IM bots | WeChat / QQ / Feishu / DingTalk sharing one persona and memory; official QQ bot bundled, whitelist-only proactive |
| Model routing | Background calls follow DSH's live model selection; reroutes are always announced |
| Privacy | Five layers + audit ledger; private memories never sync or enter group chats |
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
npm run build:client   # browser/*.mjs → client.js + star-sea window bundle
npm test               # node --test, 700+ cases
npm run preview        # local demo host with seeded data
```

Edit `browser/` sources; do not hand-edit generated `client.js`. README showcase assets can be reproduced with `node server-mock/neuron-smoke-harness.mjs` (star-sea) and `node server-mock/panel-showcase-harness.mjs` (panel, fictional demo data).

### License & credits

- Code & docs: **MIT**, Copyright © 2026 JasperGuWP — [`LICENSE`](./LICENSE)
- Asset copyright & third-party thanks (incl. Open-Meteo CC BY 4.0 non-commercial terms) — [`NOTICE.md`](./NOTICE.md)

Please tag the repo with **`dsh-plugin`** so the harness plugin library can discover it.