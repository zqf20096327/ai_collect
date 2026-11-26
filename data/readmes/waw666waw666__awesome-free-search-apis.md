<h1 align="center">Awesome Free Search APIs</h1>

<p align="center">
  <b>免费搜索 API 额度合集——每一条都亲手注册、实测到账</b><br>
  <i>Free search / fetch / embedding API credits, curated and verified by hand.</i>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-22272e.svg?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/badge/Verified-2026--11--24-brightgreen.svg?style=flat-square" alt="Verified">
  <img src="https://img.shields.io/badge/Providers-8-blue.svg?style=flat-square" alt="Providers">
  <img src="https://img.shields.io/badge/Credit%20Card-Not%20Required-success.svg?style=flat-square" alt="No credit card">
</p>

<p align="center">
  <a href="./README.md">简体中文</a> | <a href="./README_EN.md">English</a>
</p>

---

## 这是什么

**给不能上网搜索的 AI，配一把能搜的钥匙。**

很多 AI 和智能体本身不会联网：问它今天的新闻、最新的文档、某个报错的新解法，它都答不上来。这个清单把能给它们补上搜索能力的 API 集中到一处——搜索、抓网页正文、做嵌入/重排——每家写清免费额度、领取步骤和实测踩过的坑，全部亲手注册、亲眼在控制台看到额度到账才收进来。失效的优惠明确标注失效，不删，省得后来人再踩一遍。

**能干什么**

- 给你的智能体、机器人、AI 应用接一个搜索接口，它就能自己上网查资料、读网页。
- 接进自己的项目：做 RAG 知识库、研究助手、数据抓取、竞品监控。
- 先用免费额度把流程跑通、把效果验完，量不够再考虑付费——每家大约能调用多少次，总表里都换算好了。

**收录标准**：免费、不绑卡、亲手实测到账。没验过的传闻不收，抄来的名单不收。

---

## 目录

- [总表](#总表)
- [怎么选](#怎么选)
- [Keenable](#keenable) · [Exa](#exa) · [Tavily](#tavily) · [Tabstack](#tabstack) · [cloro](#cloro) · [Voyage AI](#voyage-ai) · [Mixedbread](#mixedbread) · [SocialCrawl](#socialcrawl)
- [配套区：嵌入与重排（不搜网页）](#配套区嵌入与重排不搜网页)
- [配套区二：数据抓取（不搜网页）](#配套区二数据抓取不搜网页)
- [配套区三：语音（转写与合成）](#配套区三语音转写与合成)
- [本清单的规矩](#本清单的规矩)
- [贡献](#贡献)

---

## 总表

| 服务 | 是什么 | 薅多少 | 绑卡 | 刷新 |
| :--- | :--- | :--- | :---: | :--- |
| [Keenable](#keenable) | 搜索 + 网页抓取 API | **每月 100,000 次请求** | 否 | 每月（21 日重置） |
| [Exa](#exa) | AI 搜索 API | **注册 $10 + 每月 $10 ≈ 每月约 1,400 次搜索（引导 $10 实测未发）** | 否 | 每月 $10 |
| [Tavily](#tavily) | AI 搜索 API | **每月 1,000 credits ≈ 约 1,000 次基础搜索** | 否 | 每月 |
| [Tabstack](#tabstack) | 网页访问 API（提取/研究） | **10,000 credits ≈ 约 1,000 次正文提取** | 否 | 一次性试用 |
| [cloro](#cloro) | 搜索 API（Google + AI 答案） | **每月 500 credits ≈ 约 166 次搜索** | 否 | 每月 |

---

## 怎么选

- **搜全网、量要大**：Keenable，每月 10 万次，首选。
- **搜全网、要质量**：Exa 或 Tavily，结果带相关性分数，适合喂给 AI。
- **抓某个网页的正文**：Tabstack 的 Extract。
- **让它自己上网查一圈再汇总**：Tabstack 的 Research。
- **做嵌入/重排**：在下面的[配套区](#配套区嵌入与重排不搜网页)，Voyage（每模型 2 亿 token，量最大）或 Mixedbread。

---

## Keenable

- **是什么**：给 AI 智能体用的网页搜索与页面抓取 API，一把 key 全包。
- **薅多少**：免费档每月 100,000 次搜索/抓取请求（约 100,000 次调用），每月 21 日重置；按超量价 $4/千次算，约值 $400/月。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://keenable.ai](https://keenable.ai) 用邮箱注册并验证。
  2. 打开控制台 [https://app.keenable.ai](https://app.keenable.ai)，创建 API key。
  3. 调用 `POST https://api.keenable.ai/v1/search`，请求头 `X-API-Key: <key>`。
- **坑**（2026-11-21 实测）：临时/隐私邮箱域名注册只给每月 1,000 次，要用正经邮箱；新 key 全值只显示一次且只能点复制，建完立刻存好；免费档限速 10 次/秒。

## Exa

- **是什么**：为 AI 智能体和 RAG 设计的搜索 API。
- **薅多少**：注册送 $10（2026-12-01 到期），之后每月免费 $10；按标准搜索 $7/千次算，$10 约够 1,400 次搜索。首页写的引导奖励 $10 实测不发（见坑）。我们领时（2026-11）兑换码 `EXA20FREEBUFF`、`EXA20FIRESHIP` 各加了 $20——这类码说没就没，领时实测，别信旧帖。
- **绑不绑卡**：不绑，邮箱验证码登录，无密码。
- **怎么领**：
  1. 在 [https://exa.ai](https://exa.ai) 注册。
  2. 新手引导可以走，但别指望那笔 $10 奖励（见坑）。
  3. 控制台建 key，并看清每笔额度的到期日。
- **坑**（2026-11-19 实测）：每笔额度有效期不同，我们有一笔 $10 在 2026-12-01 过期，其余还在——先花快到期的。另外这家会封号：我们一个领满 $60 的账号在 2026-11-22 被官方禁用，余额直接悬置——领到尽快用，别囤。引导奖励 $10 是挂名的，别为它花时间：2026-11-22 我们把能做的步骤全做了一遍——建 key、本人搜一次、发出邀请、被邀人接受邀请入队、被邀人再以成员身份搜一次——账单前后复查三次，始终只有注册的 $10，这笔奖励没发。

## Tavily

- **是什么**：给 AI 智能体用的搜索 / 提取 / 爬取 API。
- **薅多少**：Researcher 免费档每月 1,000 credits，每月重置——约 1,000 次基础搜索（1 次 1 credit），或约 500 次深度搜索（1 次 2 credits）。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://app.tavily.com](https://app.tavily.com) 用邮箱 + 密码注册，验证邮箱。
  2. 免费档自动生效，首页创建 key。
  3. 调用 `POST https://api.tavily.com/search`，请求头 `Authorization: Bearer <key>`。
- **坑**（2026-11-21 实测）：网传的 `GEEKROOM`（已过期）和 `GEEKROOM2`（已兑满）两个码**全废**，所谓 8,000 credits 是旧帖，别浪费时间试。

## Tabstack

- **是什么**：Mozilla 出品的网页访问 API（Research / Extract / Generate / Automate），免费额度约够 1,000 次正文提取或 40 次快速研究。
- **薅多少**：注册送 10,000 credits，控制台原文 "10,000 credits remaining"——约 1,000 次正文提取，或约 40 次快速研究。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://tabstack.ai](https://tabstack.ai) 用邮箱注册。
  2. 点邮件里的验证链接，再填组织名和密码。
  3. 控制台 [https://console.tabstack.ai/dashboard](https://console.tabstack.ai/dashboard) 看余额，要用时在里面建 API key。
- **坑**（2026-11-22 实测）：控制台只写 free trial，**不标注额度到期日**，别囤太久。

---

## cloro

- **是什么**：Google 搜索 + AI 答案引擎（ChatGPT / Perplexity / Gemini / Copilot 答案）的结构化 API，给智能体做联网搜索。
- **薅多少**：免费档每月 500 credits，每月刷新——异步 Google 搜索 3 credits/次（约 166 次/月），带 AI Overview 的搜索 5 credits/次（约 100 次/月）。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://cloro.dev](https://cloro.dev) 点 Sign up，用邮箱注册（邮箱验证码登录，没有密码步）。
  2. 打开控制台 [https://dashboard.cloro.dev](https://dashboard.cloro.dev)，在 API keys 页创建 key。
  3. 调用 `POST https://api.cloro.dev/v1/monitor/google`，请求头 `Authorization: Bearer <key>`。
- **坑**（2026-11-24 实测）：注册页有 Cloudflare 人机验证，某些网络环境点不过，换常用浏览器环境再试；同步（SYNC）请求另收 +2 credits 附加费，批量调用走异步才是 3 credits/次；每批 1 个并发任务，量小只够轻量用。

---

## 配套区：嵌入与重排（不搜网页）

下面两家**自己不搜网页**，单放一区，不混进上面的搜索名单。它们是搜索引擎内部的零件：把文字变成向量（嵌入）、把搜出来的结果重新排序（重排）。做 RAG、做自己的站内搜索时会用到，额度也是真的，所以收进来，但说清它们不是搜索引擎。

| 服务 | 是什么 | 薅多少 | 绑卡 | 刷新 |
| :--- | :--- | :--- | :---: | :--- |
| [Voyage AI](#voyage-ai) | 嵌入 + 重排 API | **每模型 2 亿 token ≈ 约 100 万次短文本嵌入** | 否 | 一次性（按账号） |
| [Mixedbread](#mixedbread) | 嵌入 + 重排 + 自有数据搜索 API | **$5 新手额度 ≈ 约 1,250 次语义搜索** | 否 | 一次性 |

### Voyage AI

- **是什么**：MongoDB 家的嵌入与重排模型（Voyage），搜索和 RAG 的检索层。
- **薅多少**：按模型、按账号的一次性额度：现行每个模型 2 亿 token（voyage-4、voyage-4-large、voyage-4-lite、voyage-context-4、voyage-code-4、rerank-3 等），领域模型（voyage-finance-2、voyage-law-2、voyage-code-2）各 5,000 万，多模态另有 2 亿文本 token + 1,500 亿像素。按每篇 200 token 估，2 亿 token 约够 100 万次短文本嵌入。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://dash.voyageai.com](https://dash.voyageai.com) 注册账号。
  2. 在 API keys 区创建 secret key，免费 token 自动先行抵扣。
- **坑**（2026-11-21 实测）：免费 token 不覆盖 Batch API；免费档限速低（实测 tier 0 为 3 RPM / 10k TPM），只适合测试；免费档内容默认可能用于训练，可在设置里退出。

### Mixedbread

- **是什么**：嵌入、重排与搜索 API（mxbai 系列模型、Toast 1）。
- **薅多少**：$5 一次性 Starter 额度，不绑卡，不续期，有效期未公布——按语义搜索 $4/千次算约 1,250 次，或按 Fast 索引 $0.25/百万 token 算约索引 2,000 万 token 内容。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://www.mixedbread.com](https://www.mixedbread.com) 注册（我们用的是 GitHub 登录）。
  2. 在平台控制台创建 API key。
  3. 调用 `https://api.mixedbread.com/v1`，请求头 `Authorization: Bearer <key>`。
- **坑**（2026-11-22 实测）：只有一次性 $5，我们实测余额 $4.98；厂商原文称免费档数据会被无限期保留。

---

## 配套区二：数据抓取（不搜网页）

这一家也不搜网页，它抓的是各平台现成的数据。做舆情、选品、找线索时会用到，单放一区，不混进搜索名单。

| 服务 | 是什么 | 薅多少 | 绑卡 | 刷新 |
| :--- | :--- | :--- | :---: | :--- |
| [SocialCrawl](#socialcrawl) | 社交 + 电商数据抓取 API | **100 credits ≈ 约 100 次调用，永不过期** | 否 | 一次性 |

### SocialCrawl

- **是什么**：社交与电商平台的数据抓取 API（X、Reddit、Hacker News、Product Hunt、LinkedIn 招聘、Amazon、小红书等）。
- **薅多少**：注册送 100 credits，永不过期；标准调用 1 credit/次，约够 100 次调用。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://socialcrawl.dev](https://socialcrawl.dev) 用邮箱注册并设密码。
  2. 点邮件里的验证链接（不验证不能登录）。
  3. 在控制台 [https://www.socialcrawl.dev/dashboard/api](https://www.socialcrawl.dev/dashboard/api) 创建 API key。
- **坑**（2026-11-22 实测）：量小，只有 100 次；注册后必须先完成邮箱验证才能进控制台。

---

## 配套区三：语音（转写与合成）

这几家也不搜网页，是语音 API：语音转文字和文字转语音。做转写、配音、语音应用时会用到，单放一区，不混进搜索名单。

| 服务 | 是什么 | 薅多少 | 绑卡 | 刷新 |
| :--- | :--- | :--- | :---: | :--- |
| [Speechmatics](#speechmatics) | 语音转文字 + TTS API | **注册 $100 额度** | 否 | 一次性 |
| [AssemblyAI](#assemblyai) | 语音转写 API | **注册 $50 额度，不过期** | 否 | 一次性 |
| [Deepgram](#deepgram) | 转写 / 合成 / 语音 Agent API | **注册 $200 额度，不过期** | 否 | 一次性 |
| [Gladia](#gladia) | 语音转文字 API | **注册 €50 ≈ 约 312 小时转写** | 否 | 一次性 |
| [Cartesia](#cartesia) | 语音 API（TTS / 语音代理） | **每月 20,000 credits + $1** | 否 | 每月 |
| [Fish Audio](#fish-audio) | TTS API | **S2.1 Pro 免费不限量（到 2026-11-30）** | 否 | 限时 |
| [HeyGen](#heygen) | TTS API（Voice Turbo） | **免费模型 $0/百万字符（到 2026-11-30）** | 否 | 限时 |

### Speechmatics

- **是什么**：语音转文字 + TTS API。
- **薅多少**：注册送 $100 额度。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://www.speechmatics.com](https://www.speechmatics.com) 用邮箱注册。
  2. 在控制台 [https://portal.speechmatics.com](https://portal.speechmatics.com) 创建 API key。
- **坑**（2026-11-17 实测）：别绑卡，绑卡会升级成付费档。

### AssemblyAI

- **是什么**：语音转写 API。
- **薅多少**：注册送 $50 额度，官方文档称永不过期。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://www.assemblyai.com](https://www.assemblyai.com) 用邮箱注册。
  2. 注册后自动生成 Default key，在控制台取用。
- **坑**（2026-11-17 实测）：LLM Gateway 不在免费范围里。

### Deepgram

- **是什么**：语音转写 / 合成 / 语音 Agent API。
- **薅多少**：注册送 $200 一次性额度，官方称永不过期。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://deepgram.com](https://deepgram.com) 用邮箱注册。
  2. 在控制台创建 API key。
- **坑**（2026-11-21 实测）：读余额要用 Admin 角色的 key，Default key 读余额会 403。

### Gladia

- **是什么**：语音转文字 API。
- **薅多少**：注册送 €50，约 312 小时异步转写，1 年有效。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://www.gladia.io](https://www.gladia.io) 用邮箱注册。
  2. 在控制台创建 API key。
- **坑**（2026-11-21 实测）：暂无大坑，额度按转写时长走，批量转写前先算好。

### Cartesia

- **是什么**：语音 API，主打 TTS 与语音代理。
- **薅多少**：免费版每月 20,000 credits + $1 语音代理额度，每月刷新。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://www.cartesia.ai](https://www.cartesia.ai) 用邮箱注册。
  2. 在控制台创建 API key。
- **坑**（2026-11-18 实测）：免费版无商用授权，商用前先看条款。

### Fish Audio

- **是什么**：TTS API，S2.1 Pro 是它家的旗舰合成模型。
- **薅多少**：模型 s2.1-pro-free 免费不限量调用（合理使用），**只到 2026-11-30**。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://fish.audio](https://fish.audio) 用邮箱注册。
  2. 在 API keys 页创建 key，调用时 model 填 `s2.1-pro-free`。
- **坑**（2026-11-24 实测）：模型名拼错会静默改走付费模型 s2.1-pro（$15/百万字节），填完务必核对；免费请求可能被用于改进模型。

### HeyGen

- **是什么**：数字人视频厂商，它的 Voice Turbo 是 TTS 模型。
- **薅多少**：模型 heygen-voice-1-turbo-free 免费调用（$0/百万字符），**只到 2026-11-30**，共享容量、忙时可能 429。
- **绑不绑卡**：不绑。
- **怎么领**：
  1. 在 [https://www.heygen.com](https://www.heygen.com) 用邮箱魔法链接注册（没有密码注册表单）。
  2. 在开发者平台 [https://platform.heygen.com](https://platform.heygen.com) 创建 API key。
  3. 调用 `POST https://api.heygen.com/v3/models/audio/tts`，请求头 `X-Api-Key: <key>`。
- **坑**（2026-11-24 实测）：建 key 强制手机验证，要先备一个能收短信的号码；output_format 必须带 encoding，只给 num_channels 会报 400。

---

## 本清单的规矩

- **只放来源和步骤**，不放任何账号、钥匙、邮箱。
- **实测才收录**：每条都写了实测日期，状态以控制台为准。
- **失效就标注**：码死了、活动结束了，在条目里写明，不删条目。

## 贡献

欢迎提 PR 补新的搜索类羊毛，或纠正失效信息。收录标准只有一条：**亲手注册、实测到账**。每条按固定格式写：是什么 / 薅多少（带大约能调用多少次）/ 绑不绑卡 / 怎么领 / 坑 / 实测日期。没验过的传闻和抄来的名单不收。

最近核实：2026-11-22。
