# Free LLM Intel · LLM 免费额度与活动情报

> 国内外 LLM 厂商的免费 API 额度、永久免费模型与限时活动情报，**每天由脚本对照官方页面自动更新、每条可复核**：
> 不提供、不分发任何 API Key；所有数字均来自巡检脚本对**官方页面**的实时抓取，每条情报附官方链接，
> 无法在官方页复核的旧说法一律标注「不予采信」。

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![365 开源计划 #038](https://img.shields.io/badge/365%20%E5%BC%80%E6%BA%90%E8%AE%A1%E5%88%92-%23038-1f6feb)](https://github.com/rockbenben/365opensource)

- 🎯 不知道先注册谁？直接看下文「[白嫖攻略](#白嫖攻略)」
- ⚡ 客户端一键接入？直达「[OpenAI 兼容端点速查表](#一键接入)」
- 📊 免费额度总表：**Part 1–4**（见「快速开始」之后，每次巡检自动生成）
- 📡 订阅厂商动态：导入 [llm-news-feeds.opml](llm-news-feeds.opml) 一次订全（官方原生源 + 自建源 + 聚合流 + 英文镜像）；[网页一键订阅](https://free-llm-intel.aishort.top/) ｜ [合并流](https://free-llm-intel.aishort.top/feeds/llm-news-all.xml) ｜ [英文合并流](https://free-llm-intel.aishort.top/feeds/llm-news-all.en.xml) ｜ 单厂商源 `…/feeds/llm-news-<厂商 id>.xml`（英文加 `.en.xml`）；博文明细：[llm-news-feeds.md](llm-news-feeds.md)（全量归档在 [`llm-news/`](llm-news/)）
- 🛰 订阅额度 / 活动变化（「哪家的白嫖政策刚变了」）：[llm-intel-changes.xml](https://free-llm-intel.aishort.top/feeds/llm-intel-changes.xml)——巡检采纳的额度调整（前值 → 后值）与新活动逐条入流
- 🤖 自己跑巡检 / 二次开发：`pip install -r requirements.txt && python crawler_llm_intel.py`（详见[快速开始](#快速开始)）

![免费额度速览：懒人首选的 5 家厂商](docs/images/intel-top5.png)

<!-- LLM-GUIDE:BEGIN  本章节由 crawler_llm_intel.py 自动生成，请勿手工修改 -->
---

<a id="白嫖攻略"></a>

## 🎯 白嫖攻略

> 本章节与下方厂商总表同源，每次巡检自动重建；免费政策随时变化（活动到期、限速调整、模型下架），注册 / 充值前请点进对应厂商的官方链接复核。

### 0. 懒人首选：不知道选谁，先注册这 5 个

> 五家都**免绑信用卡**，注册即得（国内的需手机号实名，海外的邮箱即可——都属常规注册）；覆盖日常对话、写代码、向量/重排、画图等绝大多数免费用法。

1. [智谱 GLM](#3-智谱-glm) —— **4.x 代 Flash 长期 0 元**（4.7/4-Flash/4V + 画图/视频），国内中文场景首选；但新旗舰 5.3-Flash 已收费，免费模型有独立并发限速
2. [硅基流动](#13-硅基流动-siliconflow) —— 0 元模型矩阵最适合工具链：bge 向量/重排、OCR、Kolors 画图长期免费，注册再送 14 元券试旗舰
3. [Google Gemini](#25-google-gemini-google-ai-studio) —— **邮箱注册免信用卡**，免费额度每日滚动重置；Gemini Flash 旗舰能力，海外平台首选
4. [Groq Cloud](#28-groq-cloud-lpu-推理) —— 极速推理 + **无需付款方式的永久免费层**：30 RPM / 1,000 RPD，写代码与 Agent 调用的海外主力
5. [OpenRouter](#30-openrouter-模型统一网关) —— **一个账号免费用 25+ 模型**：带 `:free` 后缀即免费、无需付款方式，最适合懒得逐家注册

### 1. 先认清四类「免费」——按能否白嫖排序

> 排序逻辑是**新用户视角**：先看要不要绑卡（实名 / 邮箱都只是常规注册，不算门槛），再看额度会不会过期。A 类注册即用且不会过期，C 类额度最大但要先冒绑卡的风险。
>
> ⚠️ 表里混着两类完全不同的额度：**大模型开放平台**发 API Key、可在自己程序里调用；**AI 编程工具**（Trae、Copilot 等，见文末 Part 4）只给编辑器内使用的积分 / Credits，**不发可外带的 API Key**——想接自己的应用别选它们。

| 类型 | 特点与正确用法 | 代表平台（点击跳下方档案） |
|---|---|---|
| **A. 无条件 · 长期可用** | 注册即得（邮箱 / GitHub / Google 或手机号实名均可，**无需付款方式**），不过期或按日/月滚动重置；可当长期主力，注意 RPM/RPD 限速与商用条款 | 国内：[智谱 GLM](#3-智谱-glm)（4.x 代 Flash 0 元（新旗舰 5.3 付费）+ 2000 万 tokens 新用户包）、[商汤 日日新](#10-商汤-日日新-sensenova)（Token Plan 公测：每 5 小时 6 万积分）、[科大讯飞星火](#11-科大讯飞星火-spark-api)（星火 Lite 支持免费使用（需产品页领取））、[硅基流动](#13-硅基流动-siliconflow)（bge/OCR/画图等 0 元模型 + 注册送 14 元券）、[腾讯云 CodeBuddy / WorkBuddy](#63-腾讯云-codebuddy-workbuddy-ai-编程-应用构建-agent)（国内体验版 0 元：500 积分/月 + 限免全模型；国际版 Free $0：100 积分/月 + 每日 30 积分 + 注册送 250）、[Trae](#64-trae-字节跳动-ai-ide-中国版为主)（免费版每月 500 积分、所有功能均可免费使用（云端任务并发限 2））、[通义灵码 / Qoder CN](#65-通义灵码-qoder-cn-阿里云)（个人体验版免费：有限体验额度（含 2 周 Pro 试用 + 300 Credits））、[文心快码 Comate](#66-文心快码-comate-百度智能云)（个人标准版长期免费：智能补全免费 + 首次赠 5000 积分（7天有效））<br>海外：[Google Gemini](#25-google-gemini-google-ai-studio)（AI Studio：Gemini 3.x Flash 全系免费层）、[Mistral AI](#27-mistral-ai)（免费**端点**：Mistral Moderation 2（Free）+ Labs 实验模型（无新用户赠金））、[Groq Cloud](#28-groq-cloud-lpu-推理)（gpt-oss 免费层 30 RPM / 1,000 RPD）、[Hugging Face](#29-hugging-face-inference-providers)（Inference Providers 每月 $0.10）、[OpenRouter](#30-openrouter-模型统一网关)（:free 模型 20 RPM / 50 RPD（充值 $10 升至 1,000 RPD））、[Cloudflare Workers AI](#31-cloudflare-workers-ai)（86 个模型共享每日 1 万 Neurons）、[Cohere](#32-cohere)（Trial Key 免费（每月 1,000 次，限非商用））、[NVIDIA NIM](#33-nvidia-nim-api-catalog)（免费推理约 40 RPM，不按 token 计费）、[Jina AI](#42-jina-ai-reader-embeddings-reranker)（每 Key 1,000 万 tokens，GitHub 登录免卡）、[Morph Labs](#43-morph-labs)（每月 200 次请求 + 工具附带 $10/月算力）、[Relace](#44-relace)（编程 Agent 专用模型免费套餐）、[Poolside](#45-poolside)（代码模型限时免费（官方未公布截止日））、[Mancer](#46-mancer)（页面标 FREE 的角色扮演向模型 0 元调用）、[无问芯穹 Infini AI](#52-无问芯穹-infini-ai-genstudio)（嵌入 / 重排接口长期免费 + 网页 Playground 全模型免费体验）、[IBM watsonx.ai](#57-ibm-watsonxai-free-toolbox)（Free Toolbox/Lite 免卡：30 万 tokens + 20 CUH/月）、[Modal](#59-modal-serverless-ai-云平台)（$30 / 月免费算力，按月重置）、[Modular](#60-modular-原-bentocloudbentoml)（共享端点免费测试 + 开源自托管永久免费）、[Qoder](#62-qoder-agentic-coding-platform-国际版)（每日可领 100 Credits + 2 周 Pro 试用送 300 Credits，Free 层不限时用基础模型）、[GitHub Copilot Free](#67-github-copilot-free)（Free 层每月 2,000 次代码补全 + 50 次聊天请求（含 Copilot Edits））、[Cursor](#68-cursor-ai-代码编辑器-hobby-免费层)（免费层：智能体与 Grok 聊天/Imagine 请求次数有限，额度每周重置）、[Kiro](#69-kiro-aws-背景-agentic-ide)（官方明写长期 Free 层：每月 50 Credits，可用开源模型 + Claude Sonnet 4.5）、[Zed](#70-zed-编辑器-ai-托管额度)（Personal 档 $0 forever：2,000 次 accepted edit predictions；自带 Key 不限次） |
| **B. 无条件 · 一次性限时** | 注册即到账、**无需付款方式**，但有有效期、不可重置；先想好用量再开通，薅完即走 | 国内：[通义千问](#2-通义千问-阿里云)（大部分模型各 100 万 Token / 90 天，文本类累计超 7000 万）、[Kimi](#4-kimi-月之暗面)（实名送 15 元代金券（可抵 kimi-k3，上下文 1,048,576））、[小米 MiMo](#7-小米-mimo)（TTS 系列限时免费 + 新用户注册赠金（40 天））、[文心 ERNIE](#9-文心-ernie-百度千帆)（17 个模型各 100 万 / 3 个月 + 20 元券）、[美团 LongCat](#12-美团-longcat)（LongCat-2.0 资源包（1M 上下文，30 天有效））、[StreamLake](#14-streamlake-快手万擎)（注册开通后分批送免费调用次数（仅基础模型推理））、[云知声 Token Hub](#15-云知声-token-hub)（认证礼包：U2/U2-Med/U1-OCR/U1-OCR-Med/U2 Flash/RadiMed 各 500 万、ASR 5 小时、TTS 5 万字、TTS-Clone/Design 各 2 万字）、[中国电信](#18-中国电信-天翼云-息壤智算)（实名最高 2,000 元试用体验金）、[数眼智能](#21-数眼智能-数言-ai-shuyanai)（注册即领 50 万 tokens（第三方中转，注意风险））<br>海外：[Fireworks AI](#37-fireworks-ai)（Muse Glimmer 30B SFT 限时免费训练（新号 $1 额度已下线））、[Stability AI](#40-stability-ai)（新号 25 积分；开源权重年营收 < $100 万免费）、[AI21 Labs](#41-ai21-labs)（$10 credits，邮箱注册免卡）、[InceptionLabs](#48-inceptionlabs)（新号 1 亿 free tokens，免信用卡）、[Baseten](#58-baseten)（新账户试用额度（官方未公开金额，以控制台为准）） |
| **C. 需绑卡 · 大额云试用金** | 需信用卡或身份验证（可能有验证扣款）；额度最大，但**注册后立刻设预算告警**，记下到期日并主动关停 | 国内：[腾讯云混元](#8-腾讯云混元-tokenhub)（8款模型共享 100万 tokens + Embedding 100万）<br>海外：[Cerebras Inference](#35-cerebras-inference-晶圆级推理)（$5 赠金 / 30 天（需添加付款方式后发放））、[Nebius](#39-nebius-token-factory-ai-cloud)（无自动赠送；绑卡扣 $25 且转为余额，并非赠金）、[Anyscale](#47-anyscale)（$100 注册额度（需工作邮箱；无独立免费层，抵扣 Ray 算力））、[Amazon Bedrock](#53-amazon-bedrock-aws-free-tier)（开户立得 $100，6 个月内最高合计 $200 抵扣金（需信用卡））、[Azure OpenAI / Azure AI Foundry](#54-azure-openai-azure-ai-foundry)（$200 / 30 天（需信用卡或身份验证））、[Google Cloud Vertex AI](#55-google-cloud-vertex-ai)（$300 / 90 天 + Always Free（需绑卡））、[Oracle OCI Generative AI](#56-oracle-oci-generative-ai)（$300 / 30 天 + Always Free（需信用卡验证））、[DigitalOcean Inference Engine](#61-digitalocean-inference-engine)（$5 / 90 天通用试用金（非 LLM 免费层，需绑卡）） |
| **D. 开源权重 / 自托管** | 没有「额度」概念，自己出算力；也可走 A 类平台免费托管调用 | 国内：[小米 MiMo](#7-小米-mimo)（TTS 系列限时免费 + 新用户注册赠金（40 天））<br>海外：[Meta Llama](#34-meta-llama-开源权重)（Llama 4 Scout/Maverick 免版税权重（可经 Groq/Cloudflare 免费托管调用））、[Stability AI](#40-stability-ai)（新号 25 积分；开源权重年营收 < $100 万免费）、[Modular](#60-modular-原-bentocloudbentoml)（共享端点免费测试 + 开源自托管永久免费） |

### 2. 唯一的真门槛：要不要信用卡

- 除下列 **9 家需验证付款方式**外，其余平台注册即发 Key，无任何付款门槛；国内平台用手机号 + 实名（常规注册，人人可办），海外平台用邮箱 / GitHub / Google 登录。
- ⚠️ **需绑卡**（可能有验证扣款或最低首付，赠金到账后也请立即设预算告警）：[腾讯云混元](#8-腾讯云混元-tokenhub)、[Cerebras Inference](#35-cerebras-inference-晶圆级推理)、[Nebius](#39-nebius-token-factory-ai-cloud)、[Anyscale](#47-anyscale)、[Amazon Bedrock](#53-amazon-bedrock-aws-free-tier)、[Azure OpenAI / Azure AI Foundry](#54-azure-openai-azure-ai-foundry)、[Google Cloud Vertex AI](#55-google-cloud-vertex-ai)、[Oracle OCI Generative AI](#56-oracle-oci-generative-ai)、[DigitalOcean Inference Engine](#61-digitalocean-inference-engine)。
- 国内平台未完成实名时可能被限速（如 PPIO），但这是注册流程的一部分，不是额外门槛。

### 3. 按场景选

- **写代码 / 编程 Agent**：[智谱 GLM](#3-智谱-glm)（4.x 代 Flash 0 元（新旗舰 5.3 付费）+ 2000 万 tokens 新用户包）、[StreamLake](#14-streamlake-快手万擎)（注册开通后分批送免费调用次数（仅基础模型推理））、[Groq Cloud](#28-groq-cloud-lpu-推理)（gpt-oss 免费层 30 RPM / 1,000 RPD）、[OpenRouter](#30-openrouter-模型统一网关)（:free 模型 20 RPM / 50 RPD（充值 $10 升至 1,000 RPD））、[Cloudflare Workers AI](#31-cloudflare-workers-ai)（86 个模型共享每日 1 万 Neurons）、[Relace](#44-relace)（编程 Agent 专用模型免费套餐）、[Poolside](#45-poolside)（代码模型限时免费（官方未公布截止日））、[Qoder](#62-qoder-agentic-coding-platform-国际版)（每日可领 100 Credits + 2 周 Pro 试用送 300 Credits，Free 层不限时用基础模型）、[腾讯云 CodeBuddy / WorkBuddy](#63-腾讯云-codebuddy-workbuddy-ai-编程-应用构建-agent)（国内体验版 0 元：500 积分/月 + 限免全模型；国际版 Free $0：100 积分/月 + 每日 30 积分 + 注册送 250）、[Trae](#64-trae-字节跳动-ai-ide-中国版为主)（免费版每月 500 积分、所有功能均可免费使用（云端任务并发限 2））、[通义灵码 / Qoder CN](#65-通义灵码-qoder-cn-阿里云)（个人体验版免费：有限体验额度（含 2 周 Pro 试用 + 300 Credits））、[文心快码 Comate](#66-文心快码-comate-百度智能云)（个人标准版长期免费：智能补全免费 + 首次赠 5000 积分（7天有效））、[GitHub Copilot Free](#67-github-copilot-free)（Free 层每月 2,000 次代码补全 + 50 次聊天请求（含 Copilot Edits））、[Cursor](#68-cursor-ai-代码编辑器-hobby-免费层)（免费层：智能体与 Grok 聊天/Imagine 请求次数有限，额度每周重置）、[Kiro](#69-kiro-aws-背景-agentic-ide)（官方明写长期 Free 层：每月 50 Credits，可用开源模型 + Claude Sonnet 4.5）、[Zed](#70-zed-编辑器-ai-托管额度)（Personal 档 $0 forever：2,000 次 accepted edit predictions；自带 Key 不限次）。
- **免费体验旗舰通用模型**：[通义千问](#2-通义千问-阿里云)（大部分模型各 100 万 Token / 90 天，文本类累计超 7000 万）、[文心 ERNIE](#9-文心-ernie-百度千帆)（17 个模型各 100 万 / 3 个月 + 20 元券）、[Google Gemini](#25-google-gemini-google-ai-studio)（AI Studio：Gemini 3.x Flash 全系免费层）。
- **超长上下文（约 1M tokens）**：[Kimi](#4-kimi-月之暗面)（实名送 15 元代金券（可抵 kimi-k3，上下文 1,048,576））、[美团 LongCat](#12-美团-longcat)（LongCat-2.0 资源包（1M 上下文，30 天有效））。
- **图像 / 视频生成**：[智谱 GLM](#3-智谱-glm)（4.x 代 Flash 0 元（新旗舰 5.3 付费）+ 2000 万 tokens 新用户包）、[腾讯云混元](#8-腾讯云混元-tokenhub)（8款模型共享 100万 tokens + Embedding 100万）、[Stability AI](#40-stability-ai)（新号 25 积分；开源权重年营收 < $100 万免费）、[Cursor](#68-cursor-ai-代码编辑器-hobby-免费层)（免费层：智能体与 Grok 聊天/Imagine 请求次数有限，额度每周重置）。
- **Embedding / Rerank / OCR / 语音**：[小米 MiMo](#7-小米-mimo)（TTS 系列限时免费 + 新用户注册赠金（40 天））、[腾讯云混元](#8-腾讯云混元-tokenhub)（8款模型共享 100万 tokens + Embedding 100万）、[硅基流动](#13-硅基流动-siliconflow)（bge/OCR/画图等 0 元模型 + 注册送 14 元券）、[云知声 Token Hub](#15-云知声-token-hub)（认证礼包：U2/U2-Med/U1-OCR/U1-OCR-Med/U2 Flash/RadiMed 各 500 万、ASR 5 小时、TTS 5 万字、TTS-Clone/Design 各 2 万字）、[Jina AI](#42-jina-ai-reader-embeddings-reranker)（每 Key 1,000 万 tokens，GitHub 登录免卡）、[无问芯穹 Infini AI](#52-无问芯穹-infini-ai-genstudio)（嵌入 / 重排接口长期免费 + 网页 Playground 全模型免费体验）。
- **自建私有端点 / 跑任意开源模型**：[Fireworks AI](#37-fireworks-ai)（Muse Glimmer 30B SFT 限时免费训练（新号 $1 额度已下线））、[Baseten](#58-baseten)（新账户试用额度（官方未公开金额，以控制台为准））、[Modal](#59-modal-serverless-ai-云平台)（$30 / 月免费算力，按月重置）、[Modular](#60-modular-原-bentocloudbentoml)（共享端点免费测试 + 开源自托管永久免费）。
- **邀请返利 / 拉新奖励**：[智谱 GLM](#3-智谱-glm)（4.x 代 Flash 0 元（新旗舰 5.3 付费）+ 2000 万 tokens 新用户包）、[小米 MiMo](#7-小米-mimo)（TTS 系列限时免费 + 新用户注册赠金（40 天））、[美团 LongCat](#12-美团-longcat)（LongCat-2.0 资源包（1M 上下文，30 天有效））。
- **学生 / 高校师生扶持**：[智谱 GLM](#3-智谱-glm)（4.x 代 Flash 0 元（新旗舰 5.3 付费）+ 2000 万 tokens 新用户包）。
- **大额云厂商体验金（海外需绑卡，国内需实名）**：[中国电信](#18-中国电信-天翼云-息壤智算)（实名最高 2,000 元试用体验金）、[Amazon Bedrock](#53-amazon-bedrock-aws-free-tier)（开户立得 $100，6 个月内最高合计 $200 抵扣金（需信用卡））、[Azure OpenAI / Azure AI Foundry](#54-azure-openai-azure-ai-foundry)（$200 / 30 天（需信用卡或身份验证））、[Google Cloud Vertex AI](#55-google-cloud-vertex-ai)（$300 / 90 天 + Always Free（需绑卡））、[Oracle OCI Generative AI](#56-oracle-oci-generative-ai)（$300 / 30 天 + Always Free（需信用卡验证））、[DigitalOcean Inference Engine](#61-digitalocean-inference-engine)（$5 / 90 天通用试用金（非 LLM 免费层，需绑卡））。

### 4. 防扣费清单（白嫖最容易翻车的地方）

1. [通义千问](#2-通义千问-阿里云)：已认证用户需在权益页面手动开启「免费额度用尽即停」；仅抵扣实时推理，批量及联网工具会扣费。
2. [智谱 GLM](#3-智谱-glm)：0 元只限 4.x 代，GLM-5.3/5.3-Flash 要付费（2000 万资源包可抵）；免费模型会换代（旧版下线自动路由新版）；限速数值只在控制台显示。
3. [火山引擎](#6-火山引擎-火山方舟-豆包)：在控制台开启「安心体验模式」，超限即停，避免自动扣费。
4. [小米 MiMo](#7-小米-mimo)：语言模型按量计费（v2.6-pro ¥3/¥6 每百万 tokens），免费只覆盖 TTS 与缓存写入且官方标注「限时」；注册赠金 40 天过期、不可抵 Token Plan 订阅。
5. [腾讯云混元](#8-腾讯云混元-tokenhub)：默认耗尽不自动转后付费，如需后付费需手动在控制台开启
6. [StreamLake](#14-streamlake-快手万擎)：免费额度**分批发放**（初识/探索/首金礼包）、**仅限基础模型推理**、**不可抵扣 Batch 批量推理**，具体额度以活动说明为准 ——「Air 永久免费」与「Pro 送 2000 万 tokens/30 天」均无官方依据，不予采信。
7. [PPIO 派欧云](#17-ppio-派欧云-分布式大模型算力)：未实名认证用户有请求频率限制；历史“注册送 5 元”说法官方页无据。
8. [Mistral AI](#27-mistral-ai)：免费的是**端点**而非额度：无新用户赠金 / 免费实验层；`Leanstral` 属 Labs 限时收集反馈期，随时可能下线；商业模型（Medium 3.5 / Large 3 / Small 4 等）均按量付费；旧「€5 赠金 / 1 RPS 免费层」在现行定价页无据。
9. [Groq Cloud](#28-groq-cloud-lpu-推理)：旧 Llama-3.1-8b / 3.3-70b 已转 Enterprise 付费，勿按旧清单调用。
10. [OpenRouter](#30-openrouter-模型统一网关)：只有带 :free 后缀的模型免费；同名付费模型会按量扣费。
11. [Cloudflare Workers AI](#31-cloudflare-workers-ai)：超量按 $0.011 / 1,000 Neurons 计费，注意每日用量。
12. [Cohere](#32-cohere)：Trial Key 明确仅限非商业用途，商用需升级付费套餐。
13. [NVIDIA NIM](#33-nvidia-nim-api-catalog)：免费接口面向开发评估，不可用于生产环境。
14. [Fireworks AI](#37-fireworks-ai)：常规推理已转为预付费模式需绑卡充值，仅 Muse Glimmer 30B SFT 微调活动至 10/31 免信用卡
15. [无问芯穹 Infini AI](#52-无问芯穹-infini-ai-genstudio)：免费的是**嵌入 / 重排接口**与**网页体验**；GenStudio **API 推理不设试用额度**、按量付费（官方计费文档已明确），「注册送 200 万 token」是旧说法，不予采信。
16. [Baseten](#58-baseten)：试用额度**金额未公开**，以注册后控制台显示为准；Startup Program（最高 $25,000 算力 + $2,500 Model APIs）需申请审核，非注册即得。
17. [Qoder](#62-qoder-agentic-coding-platform-国际版)：每日 Credits 需**手动领取**（漏领当天作废）；领到手后 30 天内有效、未过期会结转；高级额度用尽自动降级基础模型而非断供
18. [腾讯云 CodeBuddy / WorkBuddy](#63-腾讯云-codebuddy-workbuddy-ai-编程-应用构建-agent)：「限免」条目（全模型 / 无限补全 / 99 任务）随时可能回收，以页面「限免生效中」标注为准
19. [通义灵码 / Qoder CN](#65-通义灵码-qoder-cn-阿里云)：已并入 Qoder CN 品牌（原通义灵码）；VSC 插件停止演进，团队版覆盖范围与个人版不同
20. [文心快码 Comate](#66-文心快码-comate-百度智能云)：首次赠送的 5000 积分仅 7 天有效；个人版额度体系已由代金券调整为积分制
21. [GitHub Copilot Free](#67-github-copilot-free)：免费层可选模型受限（白名单制），旗舰模型需付费订阅；在读学生 / 教师 / 热门 OSS 维护者可免费申 Copilot Pro
22. [Cursor](#68-cursor-ai-代码编辑器-hobby-免费层)：定价页仅标明「有限」未公布具体数值，用尽后可等待额度每周重置
23. [Kiro](#69-kiro-aws-背景-agentic-ide)：访问受速率限制；部分模型并非所有地区可用
24. [Zed](#70-zed-编辑器-ai-托管额度)：内置模型免费只覆盖编辑预测额度；跑对话/Agent 需 Pro 试用（$5 / 14 天）或 BYOK
25. 所有绑卡平台（见第 2 节名单）注册后立刻设置 **Budget 预算与用量告警**，记下赠金到期日，到期前关停资源、删除计费实例。
26. 永久免费层 RPM 普遍只有个位数到几十，批量任务请走大额试用金 / 月度重置额度或错峰。
27. 第三方聚合中转（DMXAPI、数眼智能等非官方平台）存在跑路风险，只放低敏测试流量，不要充大额余额。

### 5. 限时 / 易变信息（最容易过期，看到请先核对官方页）

- [小米 MiMo](#7-小米-mimo)：另有 MiMo Claw 限时特惠 ¥14.9 / 月
- [云知声 Token Hub](#15-云知声-token-hub)：官方页首横幅标注 U2 Flash 全新上线并限时免费无限量调用（2026.09.30-2026.10.31）
- [摩尔线程 MUSA Coding Plan](#16-摩尔线程-musa-coding-plan)：Free Trial 即左栏 30 天免费试用（每日限量 100 名），无独立注册赠金
- [中国电信](#18-中国电信-天翼云-息壤智算)：另有编程 Token Plan 3000/10000/25000/50000/100000 积分套餐（29–699 元/月，均为付费限时特惠）
- [DMXAPI](#22-dmxapi-大模型聚合转发)：mimo-v2.5-tts —— 小米精品音色 TTS，限时免费（固定价格 ￥0 / 次，上下文 8k）
- [Mistral AI](#27-mistral-ai)：Leanstral（Labs，labs-leanstral-2603，限时开放收集反馈）—— 免费端点
- [Fireworks AI](#37-fireworks-ai)：Muse Glimmer 30B SFT 限时免费（至 10/31，免信用卡）
- [Poolside](#45-poolside)：已从申请制转为开放注册，官方标注 “Free to use for a limited time”（限时免费，截止时间未公布，以官方后续公告为准）
- [Qoder](#62-qoder-agentic-coding-platform-国际版)：限时免费活动 —— Qwen3.8-Flash 限免已延长（结束时间待公布，调用不扣 Credits）、SOTA 模型限时免费体验（按轮领取、未用过轮作废）、「经济(Efficient)」档位对付费用户限免（官方 Events 页）
- [腾讯云 CodeBuddy / WorkBuddy](#63-腾讯云-codebuddy-workbuddy-ai-编程-应用构建-agent)：国内站体验版限时免费（¥0/月）：每月 500 积分、Auto 模型调度限免覆盖全模型、代码实时补全 5000 次限免无限次、自动任务 3 个限免 99 个

### 6. 免费额度用完之后

国内厂商的包月「编程套餐」（火山方舟 Coding Plan、智谱 GLM 套餐等）价格与档位调整频繁，本仓库不转抄未经官方页面核实的价格数字——请从下方对应厂商表格的「官方直达」进入定价页查看现行档位。挑选时重点对比三点：

1. **计费方式**：按请求次数（低频友好）还是按 token（长上下文 / 重度使用友好）；
2. **限速与并发**：套餐是否仍保留 RPM 上限，Batch / 夜间折扣是否可用；
3. **工具兼容**：是否支持你在用的 IDE / Agent 与 OpenAI 兼容端点。

<a id="一键接入"></a>

### 7. 常见免费 API · OpenAI 兼容端点与申请直达（一键接入）

> 适用于 NextChat、Cherry Studio、Chatbox、Dify、Cursor、Cline 等几乎所有支持自定义 OpenAI 格式的客户端：

| 平台名称 | 免费额度简述 | API Key 申请直达 | OpenAI 兼容 Base URL | 推荐填写的免费模型名称 |
|---|---|---|---|---|
| **通义千问** | 每模型 100 万 / 90 天（北京区） | [控制台申请](https://bailian.console.aliyun.com/?apiKey=1) | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen3.8-max`, `qwen-plus` |
| **智谱 GLM** | 4.x 代 Flash 0 元（新旗舰 5.3-Flash 付费）+ 2000万券 | [控制台申请](https://bigmodel.cn/usercenter/apikeys) | `https://open.bigmodel.cn/api/paas/v4` | `glm-4.7-flash`, `glm-4-flash-250414`, `glm-4v-flash` |
| **Kimi** | 实名送 15 元券（1M 长上下文） | [控制台申请](https://platform.kimi.com/console/api-keys) | `https://api.moonshot.cn/v1` | `kimi-k2.7-code`, `kimi-k2.6` |
| **MiniMax** | M Plan 订阅或积分包通过 API Key 接入 | [控制台申请](https://platform.minimax.cn/console/access?tab=api-keys) | `https://api.minimax.chat/v1` | `M3.1 Flash Preview`, `MiniMax-M3` |
| **小米 MiMo** | TTS 系列限时免费；语言模型按量计费 | [控制台申请](https://platform.xiaomimimo.com/#/console/api-keys) | `https://api.xiaomimimo.com/v1` | `mimo-v2.6-pro`, `mimo-v2.6-flash`, `mimo-v2.5-tts` |
| **文心 ERNIE** | 17 个模型各 100 万 / 3 个月 | [控制台申请](https://console.bce.baidu.com/qianfan/overview) | `https://qianfan.baidubce.com/v2` | `ERNIE-4.5-Turbo-128K`, `DeepSeek-V3.1-250821`, `Qwen3-Coder-30B-A3B-Instruct` |
| **硅基流动** | 众多 0 元模型 + 注册送 14 元券 | [控制台申请](https://cloud.siliconflow.cn/account/ak) | `https://api.siliconflow.cn/v1` | `Xing4.0-29B`, `PaddleOCR-VL-1.5`, `bge-m3`, `Kolors` |
| **Google Gemini** | 免费层每日滚动重置（免绑卡） | [AI Studio 申请](https://aistudio.google.com/apikey) | `https://generativelanguage.googleapis.com/v1beta/openai/` | `gemini-2.5-flash`, `gemini-3.8-flash` |
| **Groq Cloud** | 30 RPM / 1,000 RPD 高速推理（免绑卡） | [控制台申请](https://console.groq.com/keys) | `https://api.groq.com/openai/v1` | `openai/gpt-oss-120b`, `qwen/qwen3.6-27b` |
| **OpenRouter** | 20 RPM 免费层（免绑卡） | [控制台申请](https://openrouter.ai/keys) | `https://openrouter.ai/api/v1` | 选带 `:free` 后缀模型（如 `google/gemma-4-31b-it:free`、`nvidia/nemotron-3-super-120b:free`） |
| **InceptionLabs** | 新号 1 亿 free tokens，免信用卡 | [Dashboard 申请](https://platform.inceptionlabs.ai/dashboard/api-keys) | `https://api.inceptionlabs.ai/v1` | `mercury-2.5`, `mercury-2` |

<!-- LLM-GUIDE:END -->

## 快速开始

环境要求：Python 3.10+；依赖 `requests`、`PyYAML`、`playwright`（pip 包随 requirements 安装；浏览器内核用于 JS 渲染 / 403 页面兜底，未安装内核时自动降级为纯 HTTP 抓取并在报告中标注，GitHub Actions 已安装内核）。

```bash
pip install -r requirements.txt
# 可选（本地启用 JS 动态页面 / 403 页面的浏览器兜底）：playwright install chromium
python crawler_llm_intel.py
# Windows 终端若遇编码报错，CMD 执行：set PYTHONIOENCODING=utf-8 ；PowerShell 执行：$env:PYTHONIOENCODING="utf-8"

# 运行本地回归测试套件：
python -m unittest discover
```

常用参数：`--only <vendor_id>`（只巡检指定厂商，调试用，不覆盖全局 README）、`--no-news`（跳过博客 / RSS 归档）、`--no-browser`（禁用 playwright）、`--delay <秒>`（请求间隔，默认 0.3）、`--timeout <秒>`（超时，默认 20）、`--feeds-base <对外前缀>`（自建 RSS 的对外地址前缀；本地重建不带它会丢自定义域名与 `rel=self`，默认按仓库推导 GitHub Pages 地址）、`--stale-review-days <天>`（页面长期不变时的例行复查周期，见「更新机制」）、`--ai-review`（变化时调用 Google AI Studio 的 Gemini 做事实核查，详见「更新机制」）、`--ai-titles`（新收录文章的机翻标题交 LLM 润色一次）、`--rebuild-only`（不抓取，从磁盘归档重建全部动态产物）、`--backfill-dates`（维护模式：从文章页元数据回填归档缺失的发布日期）、`--review-export` / `--review-apply`（本地 AI 核查通道，见「更新机制」）、`--force-sources`（强制抓取已进入连续失败冷却的情报源）。

完整巡检耗时随厂商数与源数量变化（厂商数、深度抓取的页面数与各源抓取结果见「快速开始」之后自动生成区块的「核心特性」行；JS 空壳与 403 页面自动走浏览器兜底），结束后自动刷新 Part 1–4 表格、博客主文档、`llm-news/` 归档与 `docs/feeds/` 自建 RSS / JSON 索引。

> 想启用 `--ai-review`：到 [Google AI Studio](https://aistudio.google.com/apikey) 免费申请一个 API Key，设置环境变量 `GEMINI_API_KEY`（也兼容 `GOOGLE_API_KEY`）即可，默认模型 `gemini-3.8-flash`，可用 `AI_REVIEW_MODEL` 覆盖；无需安装任何额外软件。

<!-- LLM-INTEL:BEGIN  本章节由 crawler_llm_intel.py 自动生成，请勿手工修改 -->

> 实时追踪国内外大语言模型（LLM）厂商官方公开的**免费 API 额度**、**永久免费模型**与**限时活动调用**情报。
> 本区块由 `crawler_llm_intel.py` 在**每次运行时**实时巡检官方页面生成（非人工编辑、非服务端持续监控），最近一次巡检：**2026-10-16 08:29:52**；本地手动运行与 GitHub Actions 定时刷新的方法见文首「快速开始 / 更新机制」。
>
> 💡 **核心特性**：覆盖 **70 家厂商**（深度抓取 **133 个情报页 + 46 个动态页**）；海外一手情报自动汉化（品牌与型号名保留原文）；自动过滤页面抓取状态噪点，直接展示具体额度（Tokens/代金券/免费层）、可用模型、有效期与限制条件。
> 📡 **博客动态订阅**：各厂商官方技术博客与更新日志单独维护至 [`llm-news-feeds.md`](llm-news-feeds.md)（共 35 个厂商），可导入 [`llm-news-feeds.opml`](llm-news-feeds.opml) 至 RSS 阅读器跟踪官方动态。
> 📡 **自建 RSS**（官方没有原生订阅源的厂商也能订）：[网页浏览 / 一键订阅](https://free-llm-intel.aishort.top/) ｜ [中文合并流](https://free-llm-intel.aishort.top/feeds/llm-news-all.xml) ｜ [英文合并流](https://free-llm-intel.aishort.top/feeds/llm-news-all.en.xml) ｜ 单厂商源 `https://free-llm-intel.aishort.top/feeds/llm-news-{vendor_id}.xml`（英文加 `.en.xml`）。合并流与单厂商都带 `<content:encoded>` 全文（正文来自 `docs/articles/`），阅读器里就地读完；浏览页每条也带「读全文」抽屉，点开即就地读双语正文（`?read=` 深链可分享）；中英两版按语言偏好**二选一**订阅（同订会看到重复条目，`guid` 已用 `?li=1` 区分）。
> 🛰 **额度变化订阅**（新活动 / 额度调整，前值 → 后值）：[llm-intel-changes.xml](https://free-llm-intel.aishort.top/feeds/llm-intel-changes.xml)

---

## Part 1：国内主流大语言模型（免费额度与接入指南）

> 以下平台面向开发者与个人用户，注册/认证后可获得**实实在在的免费额度**或**永久免费调用模型**。

---

### 1. DeepSeek (深度求索)

| 字段 | 详情 |
|------|------|
| **平台名称** | [DeepSeek (深度求索)](https://www.deepseek.com/) |
| **免费模型与额度** | • **无免费模型层**，全量模型按量计费：`deepseek-flash`（DeepSeek-V4.1-Flash，支持图像理解与思考模式）、`deepseek-v4-pro`（DeepSeek-V4-Pro-0813）；上下文 1M（最大输出 384K）<br>• 峰谷定价（元/百万 tokens，高峰为工作日 9:00–12:00、14:00–18:00，空闲半价）：deepseek-flash 输出 8 高峰/4 空闲、缓存命中输入 0.04/0.02；deepseek-v4-pro 输出 27.0/13.5、缓存命中输入 0.30/0.15<br>• 旧模型名 `deepseek-v4-flash`、`deepseek-v4-flash-vision-exp` 对应模型已下线，调用自动由 DeepSeek-V4.1-Flash 提供服务并按 Flash 计费 |
| **注册福利 / 账户赠送** | **无公开赠送政策**：现行官方定价页与更新日志均无新用户赠送 token 政策（历史“500 万 tokens/30 天”无法复核，不予采信）；账户扣费顺序中存在“赠送余额”项，实际以注册后账户到账为准 |
| **额度有效期** | 以账户内余额标注为准 |
| **前置条件 / 限制** | 注册平台账号；按量计费，并发限制随账户充值等级（Tier）提升 |
| **邀请 / 特惠活动** | 实行**峰谷定价**（元/百万 tokens，高峰为工作日 9:00–12:00、14:00–18:00，空闲时段半价）：deepseek-flash 输出 8.0（高峰）/4.0（空闲），缓存命中 0.04/0.02；deepseek-v4-pro 输出 27.0/13.5，缓存命中 0.30/0.15。 |
| **实时巡检证据** | • 当充值余额与赠送余额同时存在时，优先扣减赠送余额。<br>• (3) 更多并发限制细节，请参考限速与隔离。 |
| **官方直达** | [定价文档（人民币峰谷价）](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) ｜ [API Key 管理](https://platform.deepseek.com/api_keys) ｜ [更新日志](https://api-docs.deepseek.com/zh-cn/updates/) ｜ [API 平台](https://platform.deepseek.com/) |
| **特别说明** | V3/R1 时代价格（缓存 0.5 元、输出 8 元）已作废；官方无 RSS，更新见 updates 页。 |

### 2. 通义千问 (阿里云)

| 字段 | 详情 |
|------|------|
| **平台名称** | [通义千问 (阿里云)](https://tongyi.aliyun.com/) |
| **免费模型与额度** | • `qwen-max` / `qwen3.7-max` 等大语言模型、多模态、向量、语音、视觉模型 —— 大部分模型**独立享有 100 万 Token** 免费额度，**有效期 90 天**，快照版本与最新版本额度独立计算，仅抵扣实时推理 |
| **注册福利 / 账户赠送** | 大部分模型自动获得独立免费额度（通常每模型 100 万 Token），文本类模型累计超 7000 万 Token；账号开通后新上线的模型亦会自动发放额度 |
| **额度有效期** | **90 天**（开通时已有模型自账号开通起算；新上线模型自发布起算） |
| **前置条件 / 限制** | 注册千问AI平台账号；如提示安全保障需前往权益页面完成认证后自动发放 |
| **免费层限制 / 注意事项** | • **额度按模型独立计算，不可合并或跨模型转移**：用完后系统不会自动切换模型，需手动修改 model 参数<br>• **快照版本独立**：带日期后缀版本（如 `qwen-max-2026-05-17`）与主版本独立享有额度<br>• **适用范围受限**：仅抵扣模型实时推理，不可抵扣批量调用、内置工具（联网搜索/图片搜索等）、微调与部署<br>• **扣费风险**：未认证用户默认开启「免费额度用尽即停」且不可关闭；已认证用户默认关闭，需前往权益页面手动开启以防超额按量扣费产生欠费<br>• **Key 类型限制**：Token Plan 专属 API Key 不消耗免费额度，须使用通用 API Key |
| **邀请 / 特惠活动** | “云大使”返利、知识库 720 小时试用等说法无法在当前官方免费额度页复核，不予采信。 |
| **邀请 / 拉新奖励** | **阿里云“云大使”官方页不可达**：第三方情报库所指 `k.aliyun.com/smarter/ai-distributor` 复核时无法访问；所称「推广返利 30%–45%」不予采信。 |
| **实时巡检证据** | • 免费额度的有效期通常为 90 天，但两类额度的起算时间不同：<br>• 该模型不提供免费额度：部分模型不参与新人免费额度发放，具体以权益页面显示为准。<br>• Token Plan模型服务Agent 开发API/SDK/CLI资源更新日志 |
| **官方直达** | [免费额度官方文档](https://help.aliyun.com/zh/model-studio/new-free-quota) ｜ [API Key 申请直达](https://bailian.console.aliyun.com/?apiKey=1) ｜ [模型服务控制台](https://bailian.console.aliyun.com/) ｜ [通义千问官网](https://tongyi.aliyun.com/) |
| **特别说明** | 账户欠费时即使其他模型有剩余免费额度也无法调用；工作台额度显示存在分钟级延迟。 |

### 3. 智谱 GLM

| 字段 | 详情 |
|------|------|
| **平台名称** | [智谱 GLM](https://bigmodel.cn/) |
| **免费模型与额度** | • **免费的是 4.x 代 Flash，不含 5.x 新旗舰**：`glm-4.7-flash`（30B 级、200K 上下文、Agentic Coding 强化；GLM-4.5-Flash 下线后自动路由至此）、`glm-4-flash-250414`（智谱首个免费大模型 API）、`glm-z1-flash`（推理）—— 0 元<br>• 视觉（4.x 代）：`glm-4v-flash`（首个免费图像理解模型）、`glm-4.6v-flash`、`glm-4.1v-thinking-flash` —— 0 元<br>• 多模态生成：`CogView-3-Flash`（图像）、`CogVideoX-Flash`（视频）—— 0 元<br>• **当前旗舰 `glm-5.3-flash`（1M 上下文、原生多模态）是付费模型**，定价为 GLM-5.3 的 1/10，免费层不覆盖；`glm-5.3` / `glm-5.2` 同为付费（可用 2000 万资源包抵扣） |
| **注册福利 / 账户赠送** | 新用户注册专享 **2000 万免费 Tokens 资源包 + 120 次图像/视频资源包**（官方定价页首页原文：“新用户注册得 2000 万 Tokens，新模型免费”）——资源包只能抵扣**付费模型**，免费模型另算；有效期以券面标注为准 |
| **额度有效期** | 免费模型长期 0 元但**会换代**：旧版下线后请求自动路由到新版（如 GLM-4.5-Flash 2026-01-30 下线后自动路由至 GLM-4.7-Flash），旧 model id 可能失效 |
| **前置条件 / 限制** | 注册并完成实名认证 |
| **免费层限制 / 注意事项** | • **版本代差**：0 元只覆盖 4.x 代，最新一代 5.x（GLM-5.3 / GLM-5.3-Flash）全部收费；想要最新模型只能用 2000 万资源包抵扣或付费<br>• **限速按模型独立设置且数值不公开**：官方速率限制文档未给统一 RPM/TPM 数值，需登录控制台「速率限制」页查看本账户额度；触发限流返回错误码 1302、平台过载返回 1305；可申请提并发（10 个工作日审核）<br>• **旧模型会下线**：GLM-4.5-Flash 已于 2026-01-30 下线（自动路由至 4.7-Flash）；调用方不应把免费 model id 写死，需关注官方下线公告<br>• 2000 万资源包与图像/视频 120 次包为一次性新用户福利，**有效期以券面为准**，不是永久额度 |
| **邀请 / 特惠活动** | 官方定价页原文：邀好友实名注册得 Tokens，**最高可领取总计 2 亿 Tokens 资源包**（活动规则与奖励以活动页公示为准）。 |
| **邀请 / 拉新奖励** | **官方邀请活动（已复核）**：成功邀请 1 名新用户完成**实名注册**，**邀请双方各得 2000 万 Tokens** 资源包；**每月可邀请 10 人，上限 2 亿 Tokens**；无需付费/充值，页面无截止日期，按月滚动。文案取自官方前端 bundle 的 i18n 原文（`inviteNewUser` / `placard`）—— 注意 bundle 自身不一致：`tips` 写 GLM-4-Air，其余字段写 GLM-4.5-Air。入口：`bigmodel.cn/special_area`（未登录可读）、`bigmodel.cn/invite`（完整规则在登录墙后）。 |
| **学生 / 高校扶持** | **原「智谱 AI 校园计划」官方页已下线**：`bigmodel.cn/university` 前端路由 redirect 至「活动已下线」页；`zhipu.ai/activity/campus` 经 302 跳转后目标 404。第三方情报库所称「学生认证送 200 万 tokens / 1 个月」无在架官方页，**不予采信**。**现存两处官方入口**：① 清言「开学季送会员卡」`chatglm.cn/activity/giftVip` —— 免费赠送价值 **399 元**智谱清言会员卡年卡，**在校学生与教职工**，每账号限领 1 次，需完成认证（消费端会员，非 API 额度）；② `bigmodel.cn/special_area` 教育专区 —— 高校师生专享低至 6 折**付费**资源包（页面文案未见「学生认证」字样，认证校验规则未公示）。 |
| **实时巡检证据** | • 2000万免费Tokens资源包<br>• 新用户免费赠送专享 2000万 tokens体验包！<br>• 邀请好友注册认证，狂得2亿最新模型Tokens！ |
| **官方直达** | [官方主页](https://bigmodel.cn/) ｜ [定价中心（新用户资源包与免费模型标注）](https://bigmodel.cn/pricing) ｜ [API Key 申请直达](https://bigmodel.cn/usercenter/apikeys) ｜ [免费模型 GLM-4.7-Flash 文档](https://docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash) ｜ [免费模型 GLM-4V-Flash 文档](https://docs.bigmodel.cn/cn/guide/models/free/glm-4v-flash) ｜ [速率限制说明（1302/1305 错误码）](https://docs.bigmodel.cn/cn/api/rate-limit) |
| **特别说明** | 免费模型清单与付费档位以 bigmodel.cn/pricing 实时标注为准。 |

### 4. Kimi (月之暗面)

| 字段 | 详情 |
|------|------|
| **平台名称** | [Kimi (月之暗面)](https://www.moonshot.cn/) |
| **免费模型与额度** | • `kimi-k2.7-code`（含 highspeed 版）、`kimi-k2.6`（256K）—— 付费模型，**可用 15 元代金券抵扣**<br>• `kimi-k3`（2.8 万亿参数、原生视觉理解、上下文 1,048,576 tokens；输入 ¥20/输出 ¥100 每百万、缓存命中 ¥2）—— 付费，且官方原文**“Kimi K3 不支持使用新用户代金券”**，需充值解锁<br>• 旧 `moonshot-v1` 全系列与 `kimi-k2.5` 已于 **2026-08-31 下线**（调用返回 404） |
| **注册福利 / 账户赠送** | 实名认证赠送 **15 元代金券**（官方账号与支付文档原文：“认证成功后会为您赠送 15 元代金券，可用于支持该代金券的模型”）；有效期官方未载明，以券面标注为准 |
| **额度有效期** | 以券面标注为准（官方文档未载明有效期） |
| **前置条件 / 限制** | 国内注册并完成实名认证 |
| **免费层限制 / 注意事项** | • 送的是 **15 元代金券而非免费模型**；`kimi-k3` 官方明确**不支持新用户代金券**，必须充值才能用<br>• 代金券有效期官方文档未载明，以券面标注为准；旧 moonshot-v1 全系列、kimi-k2.5 已下线 |
| **邀请 / 特惠活动** | 官方原文：**“Kimi K3 不支持使用新用户代金券”**，需充值后解锁；充值返券活动在官方财务文档中无记载。 |
| **邀请 / 拉新奖励** | **邀请活动官方页不存在**：第三方情报库所指 `platform.kimi.com/docs/guide/invite-rewards` 已 308 重定向到 `/docs/get-api-key`；所称「邀请双方各得 240 元」不予采信。 |
| **实时巡检证据** | • 认证成功后会为您赠送 15 元代金券，可用于支持该代金券的模型（Kimi K3 不支持使用新用户代金券，详见下方说明）。<br>• 模型推理接口对 Input 和 Output 均实行按量计费。对于 K3 系列模型，缓存写入按 TTL（5min / 1h）单独计费；缓存命中的输入仅按缓存命中价格计费，不再重复收取缓存写入费用。如果您上传并抽取文档内容，并将抽取的文…<br>• Kimi API 开放平台提供的模型推理服务是「按量计费」模式，不提供订阅制方案，请注意与 Kimi 会员、Kimi Code 等产品区分，查看产品差异。 |
| **官方直达** | [API Key 管理直达](https://platform.kimi.com/console/api-keys) ｜ [API Key 获取指南](https://platform.kimi.com/docs/get-api-key) ｜ [账号与支付（15 元代金券说明）](https://platform.kimi.com/docs/guide/account-and-payments) ｜ [模型列表](https://platform.kimi.com/docs/models) ｜ [K3 定价](https://platform.kimi.com/docs/pricing/chat-k3) |
| **特别说明** | 开放平台已统一至新域名 platform.kimi.com（moonshot.cn 入口均跳转至此）。 |

### 5. MiniMax (稀宇科技)

| 字段 | 详情 |
|------|------|
| **平台名称** | [MiniMax (稀宇科技)](https://www.minimax.cn/) |
| **免费模型与额度** | • **无免费 API 模型层**：Free 档不支持 API Key 接入（仅限 MiniMax Code 客户端与网页端有限可用 `M3.1 Flash Preview` 及图像声音模型）<br>• **API 付费与下线动态**：API 调用需订阅 M Plan（Go/Explore/Build）或购买积分包，支持文本模型 `M3.1 Flash Preview`、视频模型 `H3` 等；官方已发布 `MiniMax M2.5`、`M2.7` 系列模型下线通知 |
| **注册福利 / 账户赠送** | **无公开注册赠金**：现行官方文档目录中无注册赠送代金券页面（历史“注册送券/90 天”说法无法复核，不予采信），以控制台实际到账为准 |
| **额度有效期** | 以账户内券面标注为准 |
| **前置条件 / 限制** | 账号注册并完成实名认证 |
| **邀请 / 特惠活动** | **M Plan 订阅**：个人 AI 订阅方案，提供 Go（年付 ¥490/年）、Explore（Go 的 3 倍用量，年付 ¥1,190/年）、Build（Go 的 12 倍用量，年付 ¥4,690/年），支持通过 API Key 接入编程与 Agent 工具；**积分包**：入门版 ¥30（4,489 积分）、进阶版 ¥150（22,460 积分）、高级版 ¥500（74,900 积分），购买之日起 1 年内有效。 |
| **实时巡检证据** | • MiniMax Code · 官方推荐<br>• 积分包自购买之日起 1 年内有效，不会因套餐额度窗口刷新而重置有效期。 |
| **官方直达** | [API Key 申请直达](https://platform.minimax.cn/console/access?tab=api-keys) ｜ [模型介绍文档](https://platform.minimax.cn/docs/guides/models-intro) ｜ [Token Plan 定价](https://platform.minimax.cn/docs/guides/pricing-token-plan) ｜ [官方网站](https://www.minimax.cn/) |
| **特别说明** | “Builder 共建者邀请返券”在现行官方文档中无入口记载；开放平台文档站已统一至 platform.minimax.cn/docs（旧域名 platform.minimaxi.com 全站 301 跳转至此）。 |

### 6. 火山引擎 (火山方舟 / 豆包)

| 字段 | 详情 |
|------|------|
| **平台名称** | [火山引擎 (火山方舟 / 豆包)](https://www.volcengine.com/product/doubao) |
| **免费模型与额度** | • **豆包系列大语言模型（Doubao-Seed 等）** —— 分别提供 **50 万 tokens** 免费推理额度<br>• **Managed Agents（Agent 编排）** —— 赠送 **30 小时运行时长 + 500 次 web_search 工具调用，有效期 2 年** |
| **注册福利 / 账户赠送** | 豆包模型分别提供 **50 万 tokens** 免费推理额度；另提供 Managed Agents 免费运行时长包 |
| **额度有效期** | Agent 免费额度有效期 **2 年**；文本模型以开通页展示为准 |
| **前置条件 / 限制** | 注册火山引擎账号并完成实名认证 |
| **邀请 / 特惠活动** | Coding Plan 邀请活动、高校师生扶持等传闻额度无法在当前官方页复核，不予采信，以控制台活动页为准。 |
| **邀请 / 拉新奖励** | **Coding Plan 邀请有礼未找到官方活动页**：第三方情报库所指 `volcengine.com/docs/82379/1455310` 已 404；所称「邀请返 10% 代金券」不予采信。 |
| **学生 / 高校扶持** | **高校师生扶持未找到官方活动页**：第三方情报库所指 `volcengine.com/docs/82379/1340426` 已 404；现行免费额度文档为 `docs/82379/1522733`（原 1263512 亦 301 重定向至此），其中未见师生专属额度。所称「最高 1 亿 tokens」不予采信。 |
| **实时巡检证据** | • 大语言模型视频生成模型图像生成模型订阅服务语音大模型向量模型模型单元知识库服务组件库 |
| **官方直达** | [火山方舟产品页](https://www.volcengine.com/product/ark) ｜ [火山方舟控制台直达](https://console.volcengine.com/ark/) ｜ [免费额度官方文档](https://docs.volcengine.com/docs/82379/1263512?lang=zh) ｜ [计费说明文档](https://docs.volcengine.com/docs/82379/1099455?lang=zh) |
| **特别说明** | 方舟（Ark）为模型接入平台，豆包为自研模型系列；支持「安心体验模式」防止超额扣费。 |

### 7. 小米 MiMo

| 字段 | 详情 |
|------|------|
| **平台名称** | [小米 MiMo](https://mimo.xiaomi.com/) |
| **免费模型与额度** | • **语音合成 TTS 系列 —— 限时免费**：`mimo-v2.5-tts`、`mimo-v2.5-tts-voiceclone`（音色克隆）、`mimo-v2.5-tts-voicedesign`（音色设计）—— 官方定价页原文「限时免费」，且不消耗 Token Plan 套餐额度<br>• **缓存写入（Cache Write）—— 限时免费**（官方定价页原文）<br>• **语言模型与 ASR 均按量计费、无免费层**：`mimo-v2.6-pro` ¥0.025（缓存命中）/ ¥3.00 / ¥6.00 每百万 tokens；`mimo-v2.6-flash` ¥0.02 / ¥1.00 / ¥2.00；`mimo-v2.6-pro-ultraspeed` ¥0.25 / ¥30 / ¥60；`mimo-v2.5-asr` ¥0.5 / 小时<br>• **开源权重可自托管**：`MiMo-V2-Flash` 以 MIT 许可开源（GitHub / HuggingFace），支持 sglang 本地部署，不受 API 额度限制<br>• 网页体验：Xiaomi MiMo Studio（`aistudio.xiaomimimo.com`）可直接对话体验，无需 API Key |
| **注册福利 / 账户赠送** | 新用户注册可获**赠金（bonus credit）**（官方促销 FAQ 原文：“You can receive bonus credit through Refer & Earn or new user registration”），**有效期 40 天**、到期自动作废；只能抵扣按量计费 API 调用费、**不可抵扣 Token Plan 订阅**。具体金额随活动变动，以控制台账户页实际到账为准 |
| **额度有效期** | 注册赠金 **40 天**有效（自到账日起、先到期先扣）；TTS 系列与缓存写入为「**限时免费**」，官方未公布截止日 |
| **前置条件 / 限制** | 小米账号登录（国内手机号或微信 / 微博 / QQ / 支付宝 / Apple ID 授权；海外邮箱或 Google / Facebook）；充值 / 购买套餐需实名认证 |
| **免费层限制 / 注意事项** | • **平台按量计费，语言模型没有免费层**：免费只覆盖 TTS 系列与缓存写入（均标注「限时」）；`mimo-v2.6-pro` 等主力模型按 token 计费，或改走 Token Plan 订阅（个人版 ¥39 / ¥99 / ¥329 / ¥659 每月）<br>• **「限时免费」官方未公布截止日**，随时可能转正式计费 —— 接入前先看定价页「TTS 系列」那行是否仍写「限时免费」<br>• **注册赠金 40 天过期**（先到期先扣、赠金优先于现金），只能抵按量计费 API 费用，**不能抵 Token Plan 订阅**，不可提现 / 转让 / 找零<br>• **限速**：`mimo-v2.6-pro` / `mimo-v2.6-flash` 均为 **100 RPM / 10M TPM**（单账号所有 API Key 合计）；`mimo-v2.6-pro-ultraspeed` 的限速需联系商务定制<br>• 国内账号充值 / 购买套餐需**实名认证**；海外与国内按区域返回不同 Base URL 与 Key、**额度不互通**；`mimo-v2.5-pro` / `mimo-v2.5` 将于 **2026-10-21 10:00（北京时间）下线** |
| **邀请 / 特惠活动** | Refer & Earn 长期活动（官方 2026-08-13 更新）：好友经邀请码注册并完成首笔 **Token Plan** 付费订阅后，邀请人得实付金额 **10%** 返利（Standard / Pro 年付与 Max 订阅为 **20%**，无 30 单上限），好友首单 **9 折**；另有 MiMo Claw 限时特惠 ¥14.9 / 月。 |
| **邀请 / 拉新奖励** | 官方 6 位邀请码：**填码双方各得 API 体验金**（国内 ¥10 / 海外 $2，注册后自动填入，40 天有效）+ 首单 **9 折**；邀请人在好友首笔付费订阅后额外得 **10% 返利**（年付 / Max 为 20%，上限 30 单，订单完成 3 天后到账）。返利只能抵 API 调用费、**不可抵 Token Plan**。 |
| **实时巡检证据** | • ¥0.5 /小时<br>• 超 30 次后绑定的被邀请人仍享 Token Plan 套餐首单 9 折<br>• 到账：为确保奖励准确发放，付费赠金将在好友首单完成 3 天后到账（若好友在 3 天内退款，相应赠金不再发放） |
| **官方直达** | [官方主页](https://mimo.xiaomi.com/) ｜ [开放平台 / 控制台](https://platform.xiaomimimo.com/) ｜ [模型与定价总览](https://mimo.mi.com/) ｜ [按量计费定价（中文）](https://mimo.mi.com/docs/zh-CN/price/pay-as-you-go) ｜ [Token Plan 订阅定价](https://mimo.mi.com/docs/zh-CN/price/token-plan) ｜ [API 文档中心](https://mimo.mi.com/docs/welcome) ｜ [开源权重 GitHub](https://github.com/XiaomiMiMo) |
| **特别说明** | API 兼容 OpenAI（`https://api.xiaomimimo.com/v1`）与 Anthropic（`https://api.xiaomimimo.com/anthropic`）两种协议；Token Plan 使用独立 Base URL 与 `tp-` 前缀 Key。 |

### 8. 腾讯云混元 (TokenHub)

| 字段 | 详情 |
|------|------|
| **平台名称** | [腾讯云混元 (TokenHub)](https://hunyuan.tencent.com/) |
| **免费模型与额度** | • `Hunyuan-a13b` / `Hunyuan-role-latest` / `Hunyuan-translation` / `Hunyuan-translation-lite` / `Tencent HY Vision 1.5 Instruct` / `Hunyuan-turbos-vision` / `Hunyuan-t1-vision` / `Hunyuan-turbos-vision-video` —— 首次开通赠送 **共 100 万 tokens，共享消耗，有效期 1 年**；接口默认限制 **5 并发**<br>• `Hunyuan-embedding` —— 赠送 **100 万 tokens，有效期 1 年**<br>• 旗舰/其他模型：`Hy4 preview`、`Hy3` 等或额度耗尽后按 token 后付费 |
| **注册福利 / 账户赠送** | 首次开通免费赠送生文/多模态 **共 100 万 tokens**（8 款模型共享消耗）+ 文本嵌入模型 **100 万 tokens**，有效期均 **1 年**；默认资源包耗尽后不自动转入后付费 |
| **额度有效期** | 免费资源包有效期 **1 年**（官方文档原文） |
| **前置条件 / 限制** | 腾讯云注册并完成实名认证 |
| **免费层限制 / 注意事项** | • 免费额度分两类：8 款生文/视觉/翻译模型**合并共享** 100 万 tokens，以及 `Hunyuan-embedding` 独立 100 万 tokens，有效期均为 1 年<br>• 默认情况下，免费资源包耗尽或到期后**不会自动转入后付费**，未主动开通后付费将报错中断<br>• 混元生文接口默认限制 **5 个并发**，由主子账号共享 |
| **邀请 / 特惠活动** | 兼容 OpenAI 格式 API；模型接入统一在 TokenHub 调度台管理。 |
| **实时巡检证据** | • 在免费额度用完后，按如下价格进行后付费计费，每月1 - 3日系统会推送上个月账单并自动完成结算和扣费。<br>• 混元生文结算顺序为：赠送的免费资源包 > 付费资源包 > 后付费。<br>• 1. 影响模型输出多样性，模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。 |
| **官方直达** | [免费额度官方文档](https://cloud.tencent.com/document/product/1729/97731) ｜ [混元产品页](https://cloud.tencent.com/product/tclm) ｜ [TokenHub 说明](https://cloud.tencent.com/document/product/1729/111007) |
| **特别说明** | 赠送额度包含 a13b、角色扮演、翻译和视觉等多款模型（共享 100 万）以及 embedding（独立 100 万）；默认不自动转后付费。 |

### 9. 文心 ERNIE (百度千帆)

| 字段 | 详情 |
|------|------|
| **平台名称** | [文心 ERNIE (百度千帆)](https://cloud.baidu.com/product/qianfan.html) |
| **免费模型与额度** | • **17 个指定预置模型**（含 `ERNIE-4.5-Turbo` 系列、`ERNIE-X1-Turbo-32K`、`DeepSeek-R1/V3/V3.1`、`Kimi-K2-Instruct`、`Qwen3/Qwen3-Coder`、`bge-large` 等） —— 首次开通自动发放，**每个模型赠送 100 万 tokens，有效期 3 个月**（仅限在线推理，不支持批量推理）<br>• 旧 ERNIE-Speed/Lite/Tiny 永久免费模型**已下架**，平台当前无永久免费模型 |
| **注册福利 / 账户赠送** | 完成实名认证另送 **20 元代金券**（有效期 1 个月）；模型免费 tokens 见左栏（官方免费额度文档 cloud.baidu.com/doc/qianfan/s/Imi2rpirg） |
| **额度有效期** | 模型免费额度 **3 个月**；代金券 **1 个月** |
| **前置条件 / 限制** | 百度智能云注册并完成实名认证 |
| **免费层限制 / 注意事项** | • **17 个模型各 100 万 tokens / 3 个月**，额度按模型独立计算；仅支持抵扣预置模型服务在线推理，不支持批量推理<br>• 旧 ERNIE-Speed / Lite / Tiny **永久免费模型已下架**，平台当前无永久免费层，额度用尽需开通付费 |
| **邀请 / 特惠活动** | 不定期发放算力代金券，以控制台活动页为准。 |
| **实时巡检证据** | • 1、通过千帆控制台模型广场进入模型版本详情页可以查看免费额度剩余量以及剩余可用时间。<br>• Token Plan 个人版 |
| **官方直达** | [千帆免费额度官方文档](https://cloud.baidu.com/doc/qianfan/s/Imi2rpirg) ｜ [API Key / 控制台直达](https://console.bce.baidu.com/qianfan/overview) ｜ [千帆产品页](https://cloud.baidu.com/product/qianfan.html) ｜ [千帆控制台](https://console.bce.baidu.com/qianfan/) |
| **特别说明** | 免费额度直接扣减，剩余量可在控制台计费中心查看；额度用尽后需开通付费。 |

### 10. 商汤 日日新 (SenseNova)

| 字段 | 详情 |
|------|------|
| **平台名称** | [商汤 日日新 (SenseNova)](https://www.sensenova.cn/) |
| **免费模型与额度** | • `SenseNova 6.8 Flash Lite`（轻量文本）、`SenseNova U1 Fast`（多模态）等 —— **Token Plan 公测免费：每 5 小时 60,000 积分**（滚动刷新），单账号可创建 **20 个 API Key**；各模型按积分计量 |
| **注册福利 / 账户赠送** | **Token Plan 公测版免费**即左栏额度（无独立注册赠金）；正式商用定价以官方后续公告为准 |
| **额度有效期** | 公测期间滚动有效（每 5 小时自动刷新） |
| **前置条件 / 限制** | 注册商汤大装置（SenseCore）开放平台账号 |
| **免费层限制 / 注意事项** | • 免费仅限 **Token Plan 公测期**：每 5 小时 60,000 积分滚动刷新，**正式商用定价待官方公告**——公测结束后现有免费额度可能取消或改规则<br>• 按积分而非 token 计量，不同模型积分单价不同；单账号最多 20 个 API Key |
| **邀请 / 特惠活动** | 公测阶段 Token Plan 免费；正式商用定价以官方后续公告为准。 |
| **实时巡检证据** | • 公测期完全免费开放，付费档位即将上线 |
| **官方直达** | [Token Plan 官方页](https://www.sensenova.cn/token-plan) ｜ [官方主页](https://www.sensenova.cn/) ｜ [大装置控制台](https://console.sensecore.cn/) |
| **特别说明** | 按积分而非直接 token 计费，不同模型积分单价不同。 |

### 11. 科大讯飞星火 (Spark API)

| 字段 | 详情 |
|------|------|
| **平台名称** | [科大讯飞星火 (Spark API)](https://xinghuo.xfyun.cn/) |
| **免费模型与额度** | • **星火 Lite** —— 官方 HTTP 调用文档原文“具有更高的响应速度，**支持免费使用**”，免费额度在星火产品页领取（QPS/限速以领取页规则为准）<br>• 付费版本：Pro、Pro-128K、Max、Max-32K、**4.0 Ultra**（已升级至 X1.5 快思考模式），另有深度推理 **X2** 产品线；Max 套餐将于 **2026-03-10 下线**并合并至 Ultra |
| **注册福利 / 账户赠送** | **无独立注册赠金**；唯一免费项为星火 Lite（额度需在星火产品页领取，规则以领取页为准）；进阶版本无公开赠送额度记载 |
| **额度有效期** | Lite 免费额度以产品页领取规则为准（官方文档无“永久”字样） |
| **前置条件 / 限制** | 讯飞开放平台注册并实名认证 |
| **免费层限制 / 注意事项** | • 免费的只有**星火 Lite 一个模型**，且额度**必须先到星火产品页手动领取**（不是注册自动到账）；QPS / 限速以领取页规则为准<br>• 进阶版本（Pro/Max/4.0 Ultra 等）无公开免费额度 |
| **邀请 / 特惠活动** | 面向教育、政企与开发者提供专项适配；支持语音/多模态混合调用。 |
| **实时巡检证据** | • 输入1.60元/百万tokens<br>• 限时免费 |
| **官方直达** | [星火 API 产品页（免费额度领取）](https://xinghuo.xfyun.cn/sparkapi) ｜ [HTTP 调用文档（模型版本说明）](https://www.xfyun.cn/doc/spark/HTTP%E8%B0%83%E7%94%A8%E6%96%87%E6%A1%A3.html) ｜ [控制台](https://console.xfyun.cn/) |
| **特别说明** | 旧档案“Lite 1–3 QPS”“X2-VL”“V2.0/V3.5”等名称/数字在现行文档中无记载（V3.5 即 Max 的 model 参数 generalv3.5）。 |

### 12. 美团 LongCat

| 字段 | 详情 |
|------|------|
| **平台名称** | [美团 LongCat](https://longcat.chat/platform/) |
| **免费模型与额度** | • `LongCat-2.0`（2026-06-30 发布，1M 上下文）—— 调用消耗 token 资源包（新用户包数额以账户到账为准，**资源包有效期 30 天**）<br>• 旧 LongCat-Flash 系列已于 2026-05-29 下线 |
| **注册福利 / 账户赠送** | 新用户注册赠送 token 资源包，具体数额**公开页未公示**，以注册后账户实际发放为准（“1000 万/5000 万”等历史说法无法复核，不予采信） |
| **额度有效期** | 官方定价页标注 token 资源包有效期 **30 天** |
| **前置条件 / 限制** | 注册并登录开放平台（定价与资源包页需登录查看） |
| **免费层限制 / 注意事项** | • 新用户资源包**具体数额官方公开页不公示**（历史「1000 万 / 5000 万」说法无法复核），以注册后账户实际到账为准<br>• 资源包**30 天有效**，到期清零；定价与资源包页需登录才能查看；旧 LongCat-Flash 系列已下线 |
| **邀请 / 特惠活动** | 平台有“老带新”邀请活动入口，但奖励规则未在公开页面公示，以控制台内活动页为准。 |
| **邀请 / 拉新奖励** | 官方邀请返佣页：`longcat.chat/platform/referral` 与活动说明页 `longcat.chat/about`（均为前端渲染，巡检需浏览器抓取）；所称「邀请双方各 20% / 10%、被邀者额外 20%」等比例未能在静态页面复核，以页面公示为准。 |
| **官方直达** | [开放平台](https://longcat.chat/platform/) ｜ [定价页](https://longcat.chat/platform/pricing) |
| **特别说明** | 兼容 OpenAI 接口格式；缓存命中（Cache Hit）部分按更低费率计费。 |

### 13. 硅基流动 (SiliconFlow)

| 字段 | 详情 |
|------|------|
| **平台名称** | [硅基流动 (SiliconFlow)](https://siliconflow.cn/) |
| **免费模型与额度** | • 对话 `Xing4.0-29B`、`PaddleOCR-VL-1.5`、`Hunyuan-MT-7B` —— 定价页标注「免费」，**0 元调用**<br>• 向量 `bge-m3`、`bge-large-zh-v1.5`、`bge-large-en-v1.5` 与重排 `bge-reranker-v2-m3` —— **0 元免费**<br>• 图像 `Kolors`、语音 `SenseVoiceSmall` 与电信 `XingChenASR/GSR` 系列 —— **0 元免费**（TTS 语音合成按量收费）<br>• 付费旗舰（可用 14 元代金券抵扣）：DeepSeek-V4 系列、GLM-5.3/5.2、Kimi-K2.7-Code、LongCat-2.0、Qwen3.x 等 |
| **注册福利 / 账户赠送** | 注册即送 **14 元** 通用代金券（官方计费 FAQ 原文：“注册即送 14 元额度”），可抵扣付费模型 token 费用；有效期以账户内券面标注为准 |
| **额度有效期** | 0 元模型长期免费；代金券有效期以账户标注为准 |
| **前置条件 / 限制** | 手机号注册（免费模型无需付费即可调用） |
| **免费层限制 / 注意事项** | • **0 元只覆盖指定开源模型 / 向量 / 重排 / 画图 / 识别语音**（Xing4.0-29B、PaddleOCR-VL、Hunyuan-MT、bge 系列、Kolors、SenseVoice 等）；DeepSeek-V4、GLM-5.x、Kimi-K2.7 等旗舰全部按量计费，需使用 14 元代金券抵扣<br>• 免费模型清单随定价页「免费」标签调整，接入前以 pricing 页实时标注为准；免费模型有平台固定限速指标 |
| **邀请 / 特惠活动** | 官方有邀请返利活动，但具体奖励金额以控制台活动页公示为准（历史页面金额无法在当前官方页复核，不予采信）。 |
| **邀请 / 拉新奖励** | **未找到官方邀请活动页**：第三方情报库指向的 `siliconflow.cn/about/reward` 已 307 跳转回官网首页（该路径不存在）；所称「注册 + 推荐各得 16 元、可无限叠加」无法复核，**不予采信**。实际奖励以控制台活动页公示为准。 |
| **实时巡检证据** | • ¥0.7/1M tokens<br>• 月消费金额：包含充值金额消费和赠送金额在内的账户每个月的总 消费金额。<br>• 1. Rate Limits 概述 |
| **官方直达** | [官方主页](https://siliconflow.cn/) ｜ [定价 / 免费模型清单](https://siliconflow.cn/pricing) ｜ [API Key 申请直达](https://cloud.siliconflow.cn/account/ak) ｜ [计费 FAQ（额度说明）](https://docs.siliconflow.com/cn/faqs/billing-rules) |
| **特别说明** | 免费模型清单随平台调整，以定价页「免费」标签为准；旗舰模型按 token 计费，可用代金券抵扣。 |

### 14. StreamLake (快手万擎)

| 字段 | 详情 |
|------|------|
| **平台名称** | [StreamLake (快手万擎)](https://www.streamlake.com/) |
| **免费模型与额度** | • **基础模型推理** —— 注册开通后分批获得免费调用次数（不可抵扣 Batch 批量推理；具体次数以活动说明为准）<br>• 在架模型：自研 `KAT-Coder-Pro-V2.5`/`KAT-Coder-Air-V2.5`（均为 256K 上下文/80K 输出）及托管 DeepSeek-V4-Flash/Pro、GLM-5.x、MiniMax-M2.x、Kimi-K2.x、MiMo-V2-Pro、Qwen3、Keye-VL 等；KAT-Coder V1 已下线，“快意 KwaiYii”已不在模型列表 |
| **注册福利 / 账户赠送** | 免费资源包**分批发放**（初识礼包/探索礼包/首金礼包）：官方免费资源包文档原文“注册并开通服务，即可分批获得一定额度的免费调用模型推理服务的次数”“免费额度仅限基础模型推理使用”“具体发放额度以活动说明为准” |
| **额度有效期** | 各资源包有效期以活动说明为准（官方文档无“永久免费”表述） |
| **前置条件 / 限制** | 注册 StreamLake 账号并开通服务 |
| **免费层限制 / 注意事项** | • 免费额度**分批发放**（初识礼包 / 探索礼包 / 首金礼包），各资源包有效期以活动说明为准 —— 官方文档**无「永久免费」表述**<br>• 免费额度**仅限基础模型推理**，且**不可抵扣 Batch 批量推理**调用<br>• 具体发放额度官方文档未写明（原文「以活动说明为准」）；「Air 永久免费」「Pro 送 2000 万 tokens / 30 天」无官方依据，不予采信 |
| **邀请 / 特惠活动** | 免费额度不可抵扣批量推理（Batch）调用；快手旗下代码与推理模型平台。 |
| **实时巡检证据** | • 2 .免费额度无法抵扣批量推理调用产生的 token。<br>• 活动期间，可能会获得多个免费额度资源包，如「初识礼包」「探索礼包」「首金礼包」等，系统会按照如下优先级进行抵扣：失效时间 > 生效时间 |
| **官方直达** | [官方主页](https://www.streamlake.com/) ｜ [免费资源包说明](https://www.streamlake.com/document/WANQING/mdsor5767ob7s796sp6) ｜ [模型列表文档](https://www.streamlake.com/document/WANQING/mdrax1ixkgpgh1ms1na) |
| **特别说明** | “Air 永久免费”“Pro 送 2000 万 tokens/30 天”无官方依据（原活动说明页已 404），不予采信。 |

### 15. 云知声 Token Hub

| 字段 | 详情 |
|------|------|
| **平台名称** | [云知声 Token Hub](https://maas.unisound.com/) |
| **免费模型与额度** | • `Unisound U2`（通用）、`U2-Med`（医疗）、`U1-OCR`、`U1-OCR-Med`（医疗 OCR）、`U2 Flash`、`U2-RadiMed`（放射医疗）—— 完成实名认证即送**各 500 万 tokens**<br>• `U2-ASR`（语音识别）—— 赠送 **5 小时**；`U2-TTS`（语音合成）—— 赠送 **5 万字**<br>• `U2-TTS-Clone`（音色克隆）、`U2-TTS-Design`（音色设计）—— 各赠送 **2 万字** |
| **注册福利 / 账户赠送** | 新人礼包即左栏按模型/服务发放的额度（官方快速入门文档），实名认证后自动到账、**无需审核**；有效期官方未标注，以账户内资源包为准 |
| **额度有效期** | 以账户内资源包标注为准（官方文档未标注有效期） |
| **前置条件 / 限制** | 注册并完成实名认证（无需企业审核） |
| **免费层限制 / 注意事项** | • 额度**按模型/服务分散发放**，不是统一 token 池：U2 / U2-Med / U1-OCR / U1-OCR-Med / U2 Flash / U2-RadiMed 各 500 万 tokens、ASR 5 小时、TTS 5 万字、TTS-Clone / TTS-Design 各 2 万字，互不通兑<br>• 有效期官方文档未标注，以账户内资源包为准 |
| **邀请 / 特惠活动** | 平台聚焦语音与医疗场景，提供语音识别/合成与 OCR 全栈接口；官方页首横幅标注 `U2 Flash` 全新上线并限时免费无限量调用（2026.09.30-2026.10.31）；弹窗标注扫码加入交流群领取 5 亿 token。 |
| **实时巡检证据** | • U2 Flash 全新上线！限时免费无限量调用（2026.09.30-2026.10.31）！立即查看<br>• 模型Token Plan低至5.9折体验文档 |
| **官方直达** | [快速入门（新人礼包说明）](https://maas.unisound.com/docs/guide/quickstart) ｜ [平台文档总览](https://maas.unisound.com/docs/guide/overview) ｜ [Token Hub 主页](https://maas.unisound.com/) |
| **特别说明** | 开放平台已统一为 maas.unisound.com（Token Hub）。 |

### 16. 摩尔线程 MUSA Coding Plan

| 字段 | 详情 |
|------|------|
| **平台名称** | [摩尔线程 MUSA Coding Plan](https://code.mthreads.com/) |
| **免费模型与额度** | • `GLM-4.7`（代码场景，运行于摩尔线程 MUSA GPU 集群）—— 官网 Free Trial 标注 **¥0 免费试用、有效期 30 天**，每日限量 **100 名**开发者；核对时页面按钮显示“体验爆满，扩容中”（可能暂时无法开通） |
| **注册福利 / 账户赠送** | Free Trial 即左栏 30 天免费试用（每日限量 100 名），无独立注册赠金 |
| **额度有效期** | 试用期 **30 天** |
| **前置条件 / 限制** | 手机号注册开发者账号，每日名额有限 |
| **邀请 / 特惠活动** | 基于摩尔线程夸娥（KUAE）集群与 MUSA 软件栈的国产 GPU 推理服务。 |
| **实时巡检证据** | • 国产算力+国产模型，限时 30 天免费体验。<br>• 限时免费<br>• Claude Pro 套餐的 3倍 用量 |
| **官方直达** | [Coding Plan 官网](https://code.mthreads.com/) |
| **特别说明** | 能否开通以 code.mthreads.com 页面实时状态为准。 |

### 17. PPIO 派欧云 (分布式大模型算力)

| 字段 | 详情 |
|------|------|
| **平台名称** | [PPIO 派欧云 (分布式大模型算力)](https://ppio.com/) |
| **免费模型与额度** | • **无免费模型层**，全部按量付费：DeepSeek V4 Pro/Flash/Vision Exp、V3.2、DeepSeek OCR 2；Qwen3.8 Max/Flash、Qwen3.7 Max、Qwen3 Coder Next；GLM 5.3/5.2/5.1；Kimi K3/K2.7 Code/K2.6；MiniMax-M3/M2.7；小米 MiMo V2.5/Pro；Fusion 融合模型（Beta）。**清单中已无 Llama** |
| **注册福利 / 账户赠送** | **无公开注册赠金**：现行官方产品页、快速开始、计费文档与公告索引均无新用户赠金记载（历史“注册送约 5 元/500 万 tokens”无法复核）；官方公告原文：“邀请奖励”活动已于 **2025-11-30 结束** |
| **额度有效期** | 不适用（无公开赠送政策） |
| **前置条件 / 限制** | 注册账号并绑定手机号；按量付费 |
| **邀请 / 特惠活动** | 提供 Token Plan 订阅套餐（ppio.com/token-plan）；“初创扶持最高 10 万元”在官方页面无记载，不予采信。 |
| **实时巡检证据** | • 覆盖主流旗舰模型，含 DeepSeek、GLM、Qwen、Kimi、MiniMax 等厂商，符合折扣标准的新模型上线后会纳入套餐，无需额外开通。<br>• 每次 API 调用按「实际 Token 用量 × 该模型抵扣系数」从套餐融合 Token 余额中扣除，输入（命中/未命中缓存）和输出分别计算。 |
| **官方直达** | [大模型 API 定价与模型清单](https://ppio.com/ai-computing/llm-api) ｜ [官方公告（活动记录）](https://ppio.com/docs/announcement/announcement) ｜ [Token Plan](https://ppio.com/token-plan) |
| **特别说明** | 分布式 GPU 云，OpenAI 兼容接口，国内多节点加速。 |

### 18. 中国电信 (天翼云 / 息壤智算)

| 字段 | 详情 |
|------|------|
| **平台名称** | [中国电信 (天翼云 / 息壤智算)](https://www.ctyun.cn/) |
| **免费模型与额度** | • 星辰大模型专区托管 GLM、DeepSeek V4/V3.2、Qwen 系列 —— 专区设有 **50 万免费 tokens** 领取入口（以体验中心实际到账为准）<br>• 电信自研 `TeleChat3`（TeleChat3-36B-Thinking、TeleChat3-Coder-36B 等）由 Tele-AI 发布并开源在 Hugging Face，**非息壤在售清单**（可自行下载部署）<br>• 注意：**4000 万 tokens 对应的是 29.9 元/月付费套餐（畅享版），不是免费额度**；Token Plan 轻享版 9.9 元/月含 1000 万 tokens（限 DeepSeek V3.2）；另有编程 Token Plan 3000/10000/25000/50000/100000 积分套餐（29–699 元/月，均为付费限时特惠） |
| **注册福利 / 账户赠送** | 注册并完成实名认证，**最高可得 2000 元试用体验金**（天翼云试用中心官方原文）；有效期以试用中心规则为准 |
| **额度有效期** | 试用体验金与 tokens 有效期以试用中心规则为准 |
| **前置条件 / 限制** | 实名认证天翼云账号 |
| **免费层限制 / 注意事项** | • 「最高 2000 元」是试用中心**多档活动的上限、不是注册即得全额**，实际到账金额与有效期以试用中心规则为准<br>• 星辰大模型专区另有 50 万 tokens 领取入口；注意 **4000 万 tokens 对应的是 29.9 元/月付费畅享版**，不是免费额度 |
| **邀请 / 特惠活动** | Token Plan 订阅：轻享版 **9.9 元/月含 1000 万 tokens**（限 DeepSeek V3.2）、畅享版 29.9 元/4000 万、尊享版 49.9 元/8000 万。 |
| **实时巡检证据** | • 50万免费tokens<br>• 如您无法参与免费试用活动，可能是以下情况导致：（1）您已试用或购买过相应类型的天翼云产品（2）您名下同一用户账号（同一用户指：在天翼云注册、登录、使用过程中的实名认证信息、手机号、邮箱、设备或地址如果一样，则视为同一用户）已经参与过活…<br>• 涵盖免费试用、产品优惠等多重福利，全方位助您降本增效，让您的业务运营更加经济、高效！ |
| **官方直达** | [试用中心（2000 元体验金）](https://www.ctyun.cn/act/trial/central) ｜ [星辰大模型专区](https://www.ctyun.cn/act/AI/zhuanxiang) ｜ [Tele-AI 官方文档站](https://www.teleai.com.cn/docOverview) |
| **特别说明** | 旧档案“2500 万 tokens”说法有误：现行官方页畅享版 29.9 元/月对应 4000 万 tokens（2500 万已不在页面出现），均为付费套餐而非免费额度；免费入口仅 50 万 tokens 领取与试用中心体验金。 |

### 19. 中国移动 九天 (MoMA)

| 字段 | 详情 |
|------|------|
| **平台名称** | [中国移动 九天 (MoMA)](https://ecloud.10086.cn/) |
| **免费模型与额度** | • **需登录控制台核实**：平台在架模型清单无法从官方公开页确认（旧档案“九天·海云/九天·客服/MoMA”等名称无法从现行官方页证实；移动云 MoMA 产品页已 404 下线） |
| **注册福利 / 账户赠送** | 免费体验包政策**无法从官方公开页面核实**（九天门户为纯动态渲染页面），需登录九天平台控制台查看实际权益——宁缺毋假 |
| **额度有效期** | 需登录控制台核实 |
| **前置条件 / 限制** | 注册中国移动/移动云账号并完成实名认证 |
| **邀请 / 特惠活动** | 面向行业开发者的赋能计划以官方公告为准。 |
| **官方直达** | [九天人工智能平台门户](https://jiutian.10086.cn/portal/) ｜ [九天帮助中心](https://jiutian.10086.cn/portal/common-helpcenter) ｜ [移动云](https://ecloud.10086.cn/) |
| **特别说明** | 本条官方公开证据不足，宁缺毋假：额度与模型信息请以登录九天门户后的控制台内容为准。 |

### 20. 360 智脑

| 字段 | 详情 |
|------|------|
| **平台名称** | [360 智脑](https://ai.360.com/open/) |
| **免费模型与额度** | • **无公开免费模型层**：平台转为聚合模式，模型列表约 86 款（含第三方模型）；自研模型 `360zhinao-pro` 定价输入 ¥2/百万 tokens、输出 ¥5/百万 tokens（以定价页为准） |
| **注册福利 / 账户赠送** | 新用户注册赠送测试资源，**具体数额/有效期未在公开页公示**，以账户实际发放为准（“1000 万 tokens/30 天”说法无法复核，不予采信） |
| **额度有效期** | 以资源包标注为准 |
| **前置条件 / 限制** | 360 账号注册并完成实名认证 |
| **邀请 / 特惠活动** | 集成 360 搜索增强能力；模型与价格以 /open/models 页面实时列表为准。 |
| **实时巡检证据** | • 输入价格：¥0 / 1K 秒 |
| **官方直达** | [模型与定价页](https://ai.360.com/open/models) ｜ [开发者文档](https://ai.360.com/docs) |
| **特别说明** | 自研模型与第三方托管模型同页计费，注意区分。 |

### 21. 数眼智能 (数言 AI / ShuyanAI)

| 字段 | 详情 |
|------|------|
| **平台名称** | [数眼智能 (数言 AI / ShuyanAI)](https://www.shuyanai.com/) |
| **免费模型与额度** | • 聚合转发模型（价格页列出 `kimi-k3`、`deepseek-v4-pro`、`qwen3.8-max`、`glm-5.3-flash` 等，以站点实时列表为准）—— 共享新用户 **50 万免费 tokens** |
| **注册福利 / 账户赠送** | **注册即领 50 万免费 Tokens**（官方价格页 shuyanai.com/price 原文），用完即止；为非官方第三方中转，额度不属模型厂商承诺 |
| **额度有效期** | 免费 tokens 用完即止（有效期以账户标注为准） |
| **前置条件 / 限制** | 手机号或微信注册 |
| **免费层限制 / 注意事项** | • **第三方聚合中转，不是模型厂商官方平台**：50 万 tokens 的额度与稳定性都不属厂商承诺，存在跑路 / 改版风险<br>• 只建议放低敏测试流量，不要充大额余额；模型清单随上游调整 |
| **邀请 / 特惠活动** | 聚合 API 转发与按量计费；为非官方第三方中转，额度不属模型厂商承诺。 |
| **实时巡检证据** | • 注册即领 50 万免费 Tokens 额度。零成本验证顶尖模型能力，极速落地您的创新构想<br>• 注册并绑定手机号可免费领取 50 万 Tokens，邀请用户可再次获得 50 万 Tokens！<br>• 模型套餐编程计划联网搜索网页解析 |
| **官方直达** | [价格页（50 万 tokens 说明）](https://www.shuyanai.com/price) ｜ [官方主页](https://www.shuyanai.com/) |
| **特别说明** | 与 dataeye.com（营销数据分析公司）无关，官方域名为 shuyanai.com。 |

### 22. DMXAPI (大模型聚合转发)

| 字段 | 详情 |
|------|------|
| **平台名称** | [DMXAPI (大模型聚合转发)](https://www.dmxapi.cn/) |
| **免费模型与额度** | • `mimo-v2.5-tts` —— 小米精品音色 TTS，限时免费（固定价格 ￥0 / 次，上下文 8k）<br>• `mimo-v2.5-tts-voiceclone` —— 小米音色克隆，限时免费（固定价格 ￥0 / 次，上下文 8k）<br>• `mimo-v2.5-tts-voicedesign` —— 小米音色设计，限时免费（固定价格 ￥0 / 次，上下文 8k）<br>• `wan3.0-get` / `wan2.7-get` / `Tripo-P1.0-get` —— 视频及 3D 模型异步生成结果获取接口免费（固定价格 ￥0 / 次）<br>• **主流对话与多模态大模型** —— 无公开永久免费层，平台启用 531 个模型，涵盖 DeepSeek、阿里云 Qwen、小米 MiMO、Kimi 等，均按量计费 |
| **注册福利 / 账户赠送** | 新用户注册后可能发放测试额度，**数额未公开**，以账户内实际到账为准（历史“$1/8 元”说法无法在当前官方页复核，不予采信）；为非官方第三方中转，额度不属模型厂商承诺 |
| **额度有效期** | 测试额度用完即止 |
| **前置条件 / 限制** | 邮箱或手机号注册 |
| **邀请 / 特惠活动** | 支持人民币结算，多节点故障转移；为非官方第三方中转，额度与稳定性不属官方承诺。 |
| **实时巡检证据** | • 0.30 元/秒<br>• 面向高频企业场景兼顾性能与成本的均衡型模型，综合能力超越上一代Doubao-Seed-1.8。胜任非结构化信息处理、内容创作、搜索推荐、数据分析等生产型工作，支持长上下文、多源信息融合、多步指令执行与高保真结构化输出。在保障稳定效果的…<br>• KAT-Coder-Pro V2.5 是一款能将完整 issue 或整段业务工作流直接交给它、在真实仓库中自主定位修改并跑通全流程的旗舰级 Agentic Coding 模型，同时通过多专家融合完整延续了 V2 的前端美学生成能力。 |
| **官方直达** | [官方文档站（模型列表）](https://doc.dmxapi.cn/) ｜ [人民币价格表](https://www.dmxapi.cn/rmb) ｜ [官方主页](https://www.dmxapi.cn/) |
| **特别说明** | 聚合中转服务，适合统一接口调试；生产用途请评估上游合规性。 |

---

## Part 2：国际主流大模型与极速推理服务（免费层与调用配额）

> 以下平台包含官方提供的**永久免费层（Free Tier）**、**试用密钥（Trial Key）**或**注册赠送体验金**，部分海外模型支持免绑卡直接调用。

---

### 23. Anthropic Claude

| 字段 | 详情 |
|------|------|
| **平台名称** | [Anthropic Claude](https://claude.com/) |
| **免费模型与额度** | • **API 无免费模型层**：当前代际 `Claude Fable 5.1`、`Claude Opus 5.5`、`Claude Sonnet 5.5`、`Claude Haiku 4.5`（上下文最高 1M，随模型而异）均按量付费，`Sonnet 5`/`Opus 5`/`Fable 5` 等已移入 legacy models；新用户少量测试 credits 可抵扣<br>• 网页端 Claude 免费版（Free plan）—— 支持 `Sonnet` 与 `Haiku`（不支持 `Opus` 与 `Fable`），额度按 **5 小时滚动窗口**重置，上下文最高可达 1M（因模型而异）；**不含 Claude Code**（官方原文 “Claude Code is included in all paid plans”） |
| **注册福利 / 账户赠送** | API 新用户有**少量免费测试额度**（官方定价 FAQ 原文：“New users receive a small amount of free credits to test the API”，未公开金额，以账户到账为准）；网页端 Claude 免费版注册即可用，Pro 订阅 $20/月（年付 $17）含 Claude Code |
| **额度有效期** | 网页免费版额度每 5 小时滚动重置；API 测试额度以账户到账为准 |
| **前置条件 / 限制** | 网页端注册账号即可；API 需绑定付款方式；**免费版不含 Claude Code**（官方原文 “Claude Code is included in all paid plans”） |
| **邀请 / 特惠活动** | Pro 订阅 $20/月（年付 $17/月）含 Claude Code；Max 从 $100/月起，含每月 $100 至 $200 的 Claude Platform API 额度；Team 计划含最高 $500/月池化 API 额度；Batch 5 折、提示缓存读低至 0.1x。 |
| **实时巡检证据** | • 专业版计划为您提供免费计划中的所有内容，并且具有更多用途和 Claude 的更多功能。其中包括 Claude Code，以及用于组织聊天和文档的项目……<br>• 供学生学习的专用 API 学分和教育功能<br>• 每个计划都有使用限制，这些限制会在滚动的五小时会话窗口中重置，而付费计划则增加了每周限制。您在 Claude 上的网络、桌面、移动和 C 活动…… |
| **官方直达** | [官方主页](https://claude.com/) ｜ [定价中心](https://claude.com/pricing) ｜ [模型文档](https://platform.claude.com/docs/en/models/overview) ｜ [API 定价 FAQ](https://platform.claude.com/docs/en/about-claude/pricing) |
| **特别说明** | 官方页将 Opus 5.5 定位为日常智能体编码与企业工作的“Daily driver”，Fable 5.1 面向复杂推理与长程智能体任务（“Next generation intelligence for long-running agents”）；另有 Opus 5.5 fast mode（2 倍标准价、最快 2.5x）与 US-only 推理（1.1x 价）等付费选项。 |

### 24. OpenAI

| 字段 | 详情 |
|------|------|
| **平台名称** | [OpenAI](https://openai.com/) |
| **免费模型与额度** | • **API 无免费模型层**，当前代际均按量付费：旗舰 `GPT-6 Astra`（$10/$50 每百万 token）、`GPT-5.6 Sol/Terra/Luna`；最低价 `gpt-5-nano`（$0.05/$0.40）；`text-embedding-3-small` 仍在售 |
| **注册福利 / 账户赠送** | **API 无公开固定赠送额度**：官方快速开始文档仅提供一次免费测试请求（原文 “Congrats on running a free test API request!”），随后引导充值（“Add credits to keep building”）；旧“$5 测试积分”在现行文档已不再出现。网页端 ChatGPT 提供免费版（可用模型以官方说明为准） |
| **额度有效期** | 免费测试请求为注册后一次性体验；额度政策以官方定价页为准 |
| **前置条件 / 限制** | 注册 OpenAI 账号并绑定海外付款方式；按组织层级划分 RPM / TPM 配额 |
| **邀请 / 特惠活动** | Batch 批量推理约 5 折；提示缓存输入约 1–2.5 折；网页端 ChatGPT 提供免费版（可用模型以官方说明为准）。 |
| **实时巡检证据** | • 用于内置工具的令牌按所选模型的每个令牌费率计费。 GB 是指二进制千兆字节（也称为 gibibytes），其中 1 GB 为 2^30 字节。网络搜索公司…<br>• 用于强化微调中模型分级的代币按该模型的每个代币费率计费。如果您在创建时启用数据共享，则可以享受推理折扣…… |
| **官方直达** | [官方主页](https://openai.com/) ｜ [API 定价](https://developers.openai.com/api/docs/pricing) ｜ [模型列表](https://developers.openai.com/api/docs/models) ｜ [快速开始](https://developers.openai.com/api/docs/quickstart) |
| **特别说明** | 旧“$5 测试积分”说法在现行官方文档中已不再出现；“数据共享折扣”亦未见公开表述。 |

### 25. Google Gemini (Google AI Studio)

| 字段 | 详情 |
|------|------|
| **平台名称** | [Google Gemini (Google AI Studio)](https://ai.google.dev/) |
| **免费模型与额度** | • `Gemini 3.8 / 3.7 / 3.6 Flash`、Gemini 3.5 Flash/Flash-Lite、Gemini 3.1 Flash-Lite、Gemini 3 Flash Preview、`Gemini 2.5 Pro/Flash/Flash-Lite`、`Gemma 4`、Gemini Embedding 系列 —— **免费层可用**，按速率限额滚动（RPD 太平洋时间午夜重置；官方文档已不再公开各模型具体免费层数字，以 AI Studio 内 Rate Limit 页为准）<br>• `Gemini 4 Argon`、`Gemini 3.1 Pro Preview` 与 Nano Banana 图像系列 —— **无免费层** |
| **注册福利 / 账户赠送** | **AI Studio 免费层（Free Tier）长期存在**（官方计费文档原文 “New accounts begin on the Free Tier”），仅需 Google 账号、免绑信用卡；注意：**2026 年 3 月起 $300 Google Cloud 试用金不能用于支付 Gemini API / AI Studio 费用**；付费层需关联结算账户并预付最低 **$5** |
| **额度有效期** | 免费层按速率限额滚动（RPD 太平洋时间午夜重置） |
| **前置条件 / 限制** | 仅需 Google 账号即可生成 API Key，免绑信用卡；免费层数据可能用于产品改进 |
| **免费层限制 / 注意事项** | • **不是所有模型都有免费层**：3.x Flash / Gemma 4 / Embedding 系列可用；`Gemini 4 Argon`、`Gemini 3.1 Pro Preview`、Nano Banana 图像系列**无免费层**，调错模型会直接付费<br>• **隐私代价**：免费层输入/输出数据可能被用于改进 Google 产品；敏感数据不要走免费层<br>• 免费层限速官方已不再公开固定数值，以 AI Studio 内 Rate Limit 页为准；RPD 按太平洋时间午夜重置<br>• $300 Google Cloud 试用金**不能**用于 Gemini API / AI Studio（2026 年 3 月起）；付费层需关联结算账户并预付最低 $5 |
| **邀请 / 特惠活动** | 付费层预付 $5 起；与 Google Cloud Vertex AI 深度集成。 |
| **实时巡检证据** | • Pro 提供 10,000 RPD 免费额度。<br>• 当您首次注册 Cloud Billing 账号时，Google Cloud 免费试用即会开始，并且您会获得 300 美元的迎新赠金。<br>• 注意： Gemini API 贡献者层级以非公开预览版的形式提供，仅限受邀用户使用。速度和可靠性与标准层级推断相当。符合条件的用户会收到电子邮件邀请，并在 AI Studio 中看到醒目提示。 |
| **官方直达** | [API Key 申请直达 (AI Studio)](https://aistudio.google.com/apikey) ｜ [OpenAI 兼容端点快速入门](https://ai.google.dev/gemini-api/docs/openai) ｜ [AI Studio 官网](https://ai.google.dev/) ｜ [API 定价文档](https://ai.google.dev/gemini-api/docs/pricing) ｜ [计费与免费层说明](https://ai.google.dev/gemini-api/docs/billing) ｜ [速率限制说明](https://ai.google.dev/gemini-api/docs/rate-limits) |
| **特别说明** | 注意：**2026 年 3 月起，$300 Google Cloud 试用金不能用于支付 Gemini API / AI Studio 费用**（官方 billing 文档原文）；旧“Gemini 1.5 Flash/Pro、Gemma 2、15 RPM/1500 RPD”等型号与数字均已换代或下架。 |

### 26. xAI Grok

| 字段 | 详情 |
|------|------|
| **平台名称** | [xAI Grok](https://x.ai/) |
| **免费模型与额度** | • **API 无免费模型层**：`grok-4.6`（编码模型 Grok Build）、grok-4.5、grok-4.3、grok-4.20 系列（reasoning / non-reasoning / multi-agent，上下文最高 1M）均需充值；旧 `grok-2`/`grok-beta` 已退役 |
| **注册福利 / 账户赠送** | **API 无免费额度**：官方文档与定价页均未标注，快速开始要求注册后自行充值（原文 “load it with credits to start using the API”）；旧“$25 免费额度/30 天”说法无据。X Premium+ 订阅含网页端 Grok 对话 |
| **额度有效期** | 以官方控制台活动为准 |
| **前置条件 / 限制** | 注册 xAI 控制台并充值；X Premium+ 订阅含网页端 Grok 对话 |
| **邀请 / 特惠活动** | 部分模型 Batch 8 折；Priority Processing 2x；Grok Build 提供 API 与 CLI 智能体编码。 |
| **实时巡检证据** | • 在 console.x.ai 注册一个帐户，然后加载积分以开始使用 API。<br>• The 2x multiplier applies to all token types — input, output, cached, and reasoning. Prompt caching discounts are app…<br>• 请求不计入速率限制 |
| **官方直达** | [官方主页](https://x.ai/) ｜ [API 定价](https://docs.x.ai/developers/pricing) ｜ [快速开始](https://docs.x.ai/developers/quickstart) ｜ [开发者控制台](https://console.x.ai/) |
| **特别说明** | 旧“$25 免费额度/30 天”说法在现行官方页面无据。 |

### 27. Mistral AI

| 字段 | 详情 |
|------|------|
| **平台名称** | [Mistral AI](https://mistral.ai/) |
| **免费模型与额度** | • **`Leanstral`**（Labs，`labs-leanstral-2603`，限时开放收集反馈）—— 免费端点<br>• **Mistral Moderation 2（Free）** —— 免费端点<br>• 商业模型均付费：Mistral Medium 3.5、`Large 3`（$0.50/$1.50 每百万）、`Small 4`（$0.15/$0.60）、Ministral 3（3B/8B/14B）、Codestral v25.08、Voxtral 语音、OCR 4.1、Mistral Embed、Shieldstral 1.0、第三方 GLM 5.2；旧 open-mistral-7b / Mixtral / Pixtral-12B 已列入 deprecated/retired |
| **注册福利 / 账户赠送** | **无新用户赠金 / 免费实验层**（现行 API 定价页未提及；旧“€5 赠金 / 1 RPS 免费层”无据）；Vibe Pro 订阅套餐含 $25.5/月 API credits 属付费订阅权益 |
| **额度有效期** | 以官方定价页为准 |
| **前置条件 / 限制** | 邮箱注册并验证手机号 |
| **免费层限制 / 注意事项** | • 免费的是**端点**而非额度：官方定价页未提供新用户赠金或免费实验层（旧“€5 赠金 / 1 RPS 免费层”无据）<br>• `Leanstral` 属 Labs「限时开放收集反馈」，**随时可能下线**；`Mistral Moderation 2（Free）` 是常设免费端点<br>• 商业模型（Mistral Medium 3.5、Large 3、Small 4、Ministral 3、Codestral、Voxtral、OCR、Mistral Embed、Shieldstral）均按量付费<br>• 免费端点限速数值官方未公开，以控制台为准 |
| **邀请 / 特惠活动** | 开放权重模型可下载；提供企业私有化部署；2026-09 宣布完成 €3B 融资。 |
| **实时巡检证据** | • Yes, you can self-host our models anywhere. Open-weight models (e.g., Mistral 7B) are Apache 2.0 licensed for researc…<br>• 经过验证的学生可以每月 5.99 美元（通常为 14.99 美元）购买 Mistral Pro。<br>• 是的，Mistral Enterprise 计划包括自定义 SLA、专门支持和私有部署。联系我们了解更多详情。 |
| **官方直达** | [API Key 控制台直达](https://console.mistral.ai/api-keys/) ｜ [官方主页](https://mistral.ai/) ｜ [API 定价](https://mistral.ai/pricing/api/) ｜ [模型文档](https://docs.mistral.ai/getting-started/models/) ｜ [新闻动态](https://mistral.ai/news/) |
| **特别说明** | 旧“€5 赠金 / 1 RPS 免费层 / open-mistral-7b / Mixtral / Pixtral-12B”在现行官方页面无据或已列入 deprecated/retired 表。 |

### 28. Groq Cloud (LPU 推理)

| 字段 | 详情 |
|------|------|
| **平台名称** | [Groq Cloud (LPU 推理)](https://groq.com/) |
| **免费模型与额度** | • `openai/gpt-oss-120b`、`gpt-oss-20b` —— 免费层 **30 RPM / 1,000 RPD / 8K TPM**<br>• `qwen/qwen3.6-27b`、`qwen3.8-27b`（Preview）、`meta-llama/llama-prompt-guard-2`、`groq/compound`(-mini)、`whisper-large-v3`(-turbo)、Orpheus TTS —— 免费层可用（各模型限额见官方速率文档，按组织级计量，缓存命中 token 不计入限速）<br>• 旧 Llama-3.1-8b / Llama-3.3-70b 已转 Enterprise 付费（旧“30 RPM / 14,400 RPD / 6,000 TPM 统一限额”说法已过时） |
| **注册福利 / 账户赠送** | **Free Plan 免费层长期存在**（官方速率文档），邮箱注册即得 API Key、免信用卡；更高限额 / Batch / Flex 需升级付费 Developer plan |
| **额度有效期** | 限额按分钟与按天滚动重置 |
| **前置条件 / 限制** | 邮箱注册即可获取 API Key，免信用卡 |
| **免费层限制 / 注意事项** | • 免费层只覆盖 gpt-oss / Qwen / 部分工具模型（gpt-oss 为 30 RPM / 1,000 RPD / 8K TPM，组织级计量）；**旧 Llama-3.1-8b、Llama-3.3-70b 已转 Enterprise 付费**，按旧清单调用会扣费<br>• Batch、Flex、更高限额需付费 Developer plan；缓存命中的 token 不计入限速 |
| **邀请 / 特惠活动** | Developer plan 按 token 计费（gpt-oss-120b $0.15/$0.60 每百万）；自研 LPU 硬件推理速度快。 |
| **实时巡检证据** | • Example: Let's say your RPM = 50 and your TPM = 200K. If you were to send 50 requests with only 100 tokens within a m… |
| **官方直达** | [API Key 控制台直达](https://console.groq.com/keys) ｜ [快速开始文档](https://console.groq.com/docs/quickstart) ｜ [官方主页](https://groq.com/) ｜ [速率限制文档](https://console.groq.com/docs/rate-limits) ｜ [模型清单](https://console.groq.com/docs/models) ｜ [定价说明](https://groq.com/pricing/) |
| **特别说明** | 旧“30 RPM / 14,400 RPD / 6,000 TPM 统一限额”及 Mixtral-8x7B、Gemma-2-9B 模型均已过时/下架。 |

### 29. Hugging Face (Inference Providers)

| 字段 | 详情 |
|------|------|
| **平台名称** | [Hugging Face (Inference Providers)](https://huggingface.co/) |
| **免费模型与额度** | • 经 18 家 provider（Cerebras/Together/Fireworks/Groq/Novita 等）路由的开源模型：`openai/gpt-oss-120b`、`deepseek-ai/DeepSeek-V3/R1`、`FLUX.1-dev` 等 —— 共享免费用户 **$0.10/月** 额度（原 Serverless 社区集群免费层已调整为 hf-inference provider，2025 年 7 月起主要提供 CPU 推理） |
| **注册福利 / 账户赠送** | Inference Providers 免费用户**每月 $0.10** 额度（官方定价文档原文，标注 “subject to change”），注册生成 Access Token 即可、免信用卡；PRO 会员 **$9/月**含每月 **$2** 通用推理额度 |
| **额度有效期** | 免费额度**按月发放** |
| **前置条件 / 限制** | 注册 Hugging Face 账号并生成 Access Token，免信用卡 |
| **免费层限制 / 注意事项** | • 免费用户每月仅 **$0.10** 推理额度（官方标注 “subject to change”），只够极低频测试，不是长期主力额度<br>• 原 Serverless 社区免费集群 2025 年 7 月起已改为 hf-inference provider 且主要提供 CPU 推理；PRO $9/月也只含 $2 额度 |
| **邀请 / 特惠活动** | PRO 会员 **$9/月**，含每月 **$2** 通用推理额度（免费额度的 20 倍）。 |
| **实时巡检证据** | • 如果您想要简单并使用每月积分，请从 Routed by Hugging Face 开始<br>• 8× ZeroGPU 配额和最高队列优先级 |
| **官方直达** | [官方主页](https://huggingface.co/) ｜ [Inference Providers 定价](https://huggingface.co/docs/inference-providers/pricing) ｜ [会员定价](https://huggingface.co/pricing) |
| **特别说明** | 高并发生产场景建议使用 Dedicated Endpoints。 |

### 30. OpenRouter (模型统一网关)

| 字段 | 详情 |
|------|------|
| **平台名称** | [OpenRouter (模型统一网关)](https://openrouter.ai/) |
| **免费模型与额度** | • **`:free` 后缀模型**（实时目录约 16 个）—— **限速 20 RPM**；每日请求上限 **50 次**（累计购买不足 10 credits）或 **1,000 次**（购满 10 credits），官方 limits 文档常量 FREE_MODEL_RATE_LIMIT_RPM=20 / FREE_MODEL_NO_CREDITS_RPD=50 / FREE_MODEL_HAS_CREDITS_RPD=1000<br>• 当前 :free 实例：`google/gemma-4-31b-it:free`、`gemma-4-26b-a4b-it:free`、`nvidia/nemotron-3-super-120b:free`、`nemotron-3-ultra-550b:free`、`thinkingmachines/inkling:free`(-small)、`cohere/north-mini-code:free`、`poolside/laguna-s-2.1:free`、`liquid/lfm-2.5-2.6b:free` 等；旧 llama-3.3-70b / gemini-2.0-flash-exp / deepseek-r1 / qwen-2.5-72b :free ID 均已下架 |
| **注册福利 / 账户赠送** | 免费模型**无需充值**即可调用，邮箱或 GitHub 登录创建 API Key、免信用卡；购满 10 credits 可将免费模型日限从 50 次提升至 1,000 次 |
| **额度有效期** | 免费政策长期有效 |
| **前置条件 / 限制** | 邮箱或 GitHub 登录创建 API Key，免信用卡 |
| **免费层限制 / 注意事项** | • **只有带 `:free` 后缀的模型免费**，同名付费模型照常扣费；免费实例约 16 个且随上游厂商变动（旧 llama-3.3-70b / gemma-2 / deepseek-r1 等 :free ID 已下架）<br>• 限速 20 RPM；每日 50 次（累计充值不足 $10）或 1,000 次（购满 $10 credits 后） |
| **邀请 / 特惠活动** | 一个 API Key 统一切换全球多家模型厂商；购满 10 credits 可将免费模型日限提升至 1,000 次。 |
| **实时巡检证据** | • 帐户余额，您在整个帐户中的可用积分。如果您的帐户信用余额为负，您可能会看到错误，包括免费模型的错误。添加学分以放置 y...<br>• 我们在企业计划中提供 OpenRouter 费用折扣。 We do not discount inference.<br>• 不需要。推理按每个计划的提供商标价计费。 OpenRouter 的费用是在您购买积分时收取的，标准版为 5.5%，商业版为 8%，个人购买时不收取… |
| **官方直达** | [API Key 申请直达](https://openrouter.ai/keys) ｜ [官方主页](https://openrouter.ai/) ｜ [速率限制文档](https://openrouter.ai/docs/api_reference/limits) ｜ [免费模型列表](https://openrouter.ai/models?max_price=0) |
| **特别说明** | 旧举的 llama-3.3-70b / gemini-2.0-flash-exp / deepseek-r1 / qwen-2.5-72b :free ID 均已下架。 |

### 31. Cloudflare Workers AI

| 字段 | 详情 |
|------|------|
| **平台名称** | [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) |
| **免费模型与额度** | • 目录内可免费使用的模型共享 **每日 10,000 Neurons 免费额度**（官方