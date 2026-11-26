# 一人公司 AI 出海清单 · Awesome OPC Chuhai

![一人公司 AI 出海路径示意](assets/cover.webp)

一人公司要把 AI 产品卖到海外，从大模型与 MCP、到建站收款与获客，先看这里。

整理：[橙哥出海](https://x.com/OPCchuhai) · 网站：[opcchuhai.com](https://opcchuhai.com/)

这是一份写给华人**一人公司 / 独立开发者**的出海清单。重点不是罗列所有 AI 套壳，而是一个人真正能做出来、卖出去的方向：AI SaaS、AI 网站、AI 游戏，以及搭建这些产品会用到的大模型 API、MCP、建站托管、跨境收款与获客渠道。每条都指向官方页面，并附一句适用场景。优先收录免费产品，或有公开文档可查的免费档。

价格、开通资格、模型能力和可用地区会变动，以各官网当时公布为准。本清单只整理公开资料，**不提供法律、税务或投资建议**。

## 🗺️ Start here / 建议路径

一个人从 0 到第一笔海外收入，可以按这个顺序读，不必一次看完全文：

1. 💡 **选定产品形态** → [Solo AI products](#solo-ai-products--一人公司可做的-ai-业务场景)（AI SaaS、网站或游戏）
2. 🧠 **接上模型与工具** → [LLMs & APIs](#llms--apis--大模型与-api) · [🔌 MCP](#mcp)
3. ☁️ **上线并收款** → [Hosting](#hosting--sites--建站与托管) · [💳 Payments](#global-payments--跨境收款) · [🏢 Company](#company--compliance--公司与合规)
4. 🚀 **发布与获客** → [Launch](#launch--directories--发布与目录) · [✍️ Content](#content--acquisition--内容与获客)

需要起步代码时，再看 [📦 开源模板](#open-source-templates--examples--开源模板与案例)。想先看看已经在向海外用户交付的 AI 产品，读 [🌏 AI 出海项目](#ai-出海项目--showcase)。欢迎通过 Pull Request 补充或修正条目，提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📚 Contents / 目录

- [💡 Solo AI products / 一人公司可做的 AI 业务场景](#solo-ai-products--一人公司可做的-ai-业务场景)
- [🧠 LLMs & APIs / 大模型与 API](#llms--apis--大模型与-api)
- [🔌 MCP](#mcp)
- [☁️ Hosting & sites / 建站与托管](#hosting--sites--建站与托管)
- [💳 Global payments / 跨境收款](#global-payments--跨境收款)
- [🏢 Company & compliance / 公司与合规](#company--compliance--公司与合规)
- [🚀 Launch & directories / 发布与目录](#launch--directories--发布与目录)
- [✍️ Content & acquisition / 内容与获客](#content--acquisition--内容与获客)
- [📦 Open-source templates & examples / 开源模板与案例](#open-source-templates--examples--开源模板与案例)
- [🌏 AI 出海项目 / Showcase](#ai-出海项目--showcase)
- [👤 作者 / 配套手册](#作者--配套手册)
- [📄 License / 许可](#license--许可)

<a id="solo-ai-products--一人公司可做的-ai-业务场景" name="solo-ai-products--一人公司可做的-ai-业务场景"></a>

## 💡 Solo AI products / 一人公司可做的 AI 业务场景

能支撑一种可售卖产品的框架、引擎和官方工具，而不是随机 AI 应用合集。常见路径：把模型做成订阅制 SaaS、用生成能力做网站产品，或用轻量引擎做能在网页 / itch.io 分发的 AI 游戏。

- [Vercel AI SDK](https://ai-sdk.dev/) — 在 TypeScript / Next.js 里接入多家模型、流式输出和工具调用的官方 SDK，适合做 AI SaaS 的应用层，而不是绑死一家供应商。
- [Next.js](https://nextjs.org/) — 全栈 Web 框架，适合一人同时做产品站、营销页和 API 路由，是常见的 AI 网站与 SaaS 起点。
- [v0](https://v0.app/) — Vercel 的 AI 界面生成工具，用自然语言先出 React 页面，适合快速搭 AI 产品的前端原型。
- [Bolt.new](https://bolt.new/) — 浏览器里的全栈 AI 开发环境，适合用一句话先跑通可演示的网站，再迁到自己的仓库和域名。
- [n8n](https://n8n.io/) — 开源工作流自动化，可把模型、表单和第三方服务串成可售卖的自动化或 Agent 流程，也可自托管。
- [Godot Engine](https://godotengine.org/) — 开源游戏引擎，授权宽松、体量适合单人开发，可用来做带 AI 角色或生成内容的独立游戏。
- [Phaser](https://phaser.io/) — 浏览器 2D 游戏框架，适合把 AI 玩法做成即点即玩的网页游戏，降低下载和分发成本。
- [Three.js](https://threejs.org/) — 网页 3D 渲染库，适合做可在浏览器里运行的 3D 场景、AI 角色展示或轻量 3D 游戏。
- [itch.io](https://itch.io/) — 独立游戏与数字内容分发平台，页面简单、起步门槛低，适合一人先把 AI 游戏或实验作品卖出去。
- [ElevenLabs](https://elevenlabs.io/) — 语音合成与克隆的官方平台，适合给 AI 网站、口播内容和游戏角色配多语言声音。
- [Black Forest Labs](https://bfl.ai/) — Flux 图像生成模型的官方平台，适合做 AI 生图网站，或给游戏与营销站提供可调用的出图能力。
- [Suno](https://suno.com/) — 文本生成完整歌曲的平台，适合做 AI 音乐类网站，或给游戏和短视频产品配原声。
- [Runway](https://runway.com/) — AI 视频生成与编辑工具，适合做短视频类 AI 网站，或给营销和游戏预告提供出片能力。

<a id="llms--apis--大模型与-api" name="llms--apis--大模型与-api"></a>

## 🧠 LLMs & APIs / 大模型与 API

先用官方 API 把产品跑通，再考虑自建推理。选型时不要只看单价，而要看一次合格结果的成本和能否切换供应商。只收录官方平台，不收录非官方中转。

- [OpenAI API](https://openai.com/api/) — 官方模型与 API 入口，适合做聊天、工具调用和多模态能力；文档见 [OpenAI for Developers](https://developers.openai.com/api/docs)。
- [Claude API](https://claude.com/platform/api) — Anthropic 的官方 API，适合做写作、编程和 Agent 类 SaaS；文档见 [Claude Docs](https://platform.claude.com/docs/en/home)。
- [Gemini API](https://aistudio.google.com/docs) — Google 官方模型 API，原生多模态和长上下文，适合做文档分析、研究助手和需要大窗口的产品。
- [DeepSeek API](https://api-docs.deepseek.com/) — 官方推理与对话 API，适合在控制成本的前提下，给海外产品接中英都可用的模型能力。
- [OpenRouter](https://openrouter.ai/) — 一个接口路由多家官方模型，适合早期验证和做供应商降级，而不是把业务逻辑写死在某一家 SDK 里。
- [Hugging Face](https://huggingface.co/) — 开源模型、数据集和推理服务的官方社区，适合选用开源权重，或在需要时再转到自托管。
- [Groq](https://groq.com/) — 低延迟推理 API，适合对响应速度敏感的对话和补全场景，先用公开免费档验证体验。
- [Replicate](https://replicate.com/) — 用 API 运行开源和社区模型，适合给生图、语音和垂直模型做按次调用，不必自己管 GPU。
- [Modal](https://modal.com/) — 面向 Python 的无服务器 CPU / GPU 平台，适合在 API 不够用时，把推理或微调任务按需跑起来。
- [RunPod](https://www.runpod.io/) — GPU 云与无服务器推理，适合已经确认自托管更划算、需要按卡型和时长租算力的阶段。

<a id="mcp" name="mcp"></a>

## 🔌 MCP

[Model Context Protocol（MCP）](https://modelcontextprotocol.io/) 让大模型通过标准服务器调用本地文件、代码仓库、浏览器、数据库和外部 API。一人公司最有用的用法，是在 Claude、Cursor 或 VS Code 里接上少量生产级服务器，而不是一次安装几十个。

下面只保留规范与文档、常用宿主，以及文件系统、GitHub、网页抓取 / 搜索、浏览器、数据库、收款和托管等官方或广泛使用的服务器。

### 📘 Spec, docs & SDKs / 规范、文档与 SDK

- [MCP 官方网站](https://modelcontextprotocol.io/) — 协议主页，含教程和概念说明；现行规范见 [2026-07-28 Specification](https://modelcontextprotocol.io/specification/2026-07-28)，更新说明见 [官方博客](https://blog.modelcontextprotocol.io/posts/2026-07-28/)，公开服务器目录见 [MCP Registry](https://registry.modelcontextprotocol.io/)。
- [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — 协议发布时的官方介绍，适合先建立「模型如何连工具」的背景。
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) / [Python SDK](https://github.com/modelcontextprotocol/python-sdk) — 官方 SDK，适合给自己的 AI 产品暴露工具，或在现有后端上接 MCP。

### 💻 Clients & hosts / 客户端与宿主

- [Claude](https://claude.com/download) — Anthropic 官方桌面端，适合在本机连接 MCP 服务器，处理文件、浏览器和日常研究，而不必先写宿主程序。
- [Claude Code](https://claude.com/product/claude-code) — Anthropic 官方编码 Agent / CLI，原生支持 MCP，适合一个人在终端里改仓库、跑测试和调用外部工具。
- [Cursor](https://cursor.com/) — AI 代码编辑器，可在项目里配置 MCP 服务器，适合边写产品边让模型读写仓库、查文档或操作外部服务。
- [Visual Studio Code: MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers) — VS Code 官方的 MCP 说明，适合已经在 VS Code / Copilot 里开发、想给编辑器接工具的人。
- [Codex](https://openai.com/codex/) — OpenAI 官方编码 Agent，可在云端或本地协助改代码，并作为 MCP 宿主接入外部工具。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) — 开源桌面客户端，图形界面配置 MCP 和多家模型，适合先在本地把工具链路跑通再接到产品里。

### 🛠️ Curated servers / 精选服务器

- [Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) — 官方参考实现，让模型在授权目录里读写本地文件，适合整理文档、改项目文件和做本地工作流。
- [Fetch MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) — 官方参考实现，把网页取回并整理成模型可消化的内容，适合做调研、抓取公开文档和核对官网说明。
- [GitHub MCP Server](https://github.com/github/github-mcp-server) — GitHub 官方服务器，用于查看仓库、议题和 Pull Request，适合一个人用自然语言处理日常协作。
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) — Microsoft 官方浏览器自动化服务器，适合让 Agent 打开页面、走通注册或结账路径，并做基本的端到端检查。
- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) — Cloudflare 官方服务器，用于管理 Workers、KV、R2 和 D1 等资源，适合已经把站和 API 放在 Cloudflare 上的一人团队。
- [Neon MCP Server](https://github.com/neondatabase/mcp-server-neon) — Neon 官方服务器，用于创建和管理 Serverless Postgres，适合给 AI SaaS 接数据库而不自己运维实例。
- [Supabase MCP](https://github.com/supabase/mcp) — Supabase 官方 MCP，用于查看项目配置、表结构和数据，适合在编辑器里直接操作后端，而不是反复进出控制台。
- [Brave Search MCP Server](https://github.com/brave/brave-search-mcp-server) — Brave 官方搜索服务器，给 Agent 补充带出处的网页检索，适合做调研型功能和核对公开信息。
- [Sentry Toolkit (MCP)](https://github.com/getsentry/toolkit) — Sentry 官方工具集（含 MCP），适合上线后让 Agent 直接查看报错和性能问题。
- [Stripe MCP](https://docs.stripe.com/mcp) — Stripe 官方 MCP 文档与托管服务，让 Agent 在授权范围内查询和操作收款相关 API，适合调试结账、订阅和退款，而不是把密钥写进提示词。

<a id="hosting--sites--建站与托管" name="hosting--sites--建站与托管"></a>

## ☁️ Hosting & sites / 建站与托管

把产品变成可访问的网址：域名、静态站、边缘函数、云主机、数据库和交易邮件。

- [Cloudflare Pages](https://www.cloudflare.com/products/pages/) — 静态站与前端应用的全球托管，适合文档站、营销站和 Jamstack 项目。
- [Cloudflare Workers](https://www.cloudflare.com/products/workers/) — 在边缘运行 API、表单和轻量后端，一个人也能把 AI 产品的接口和页面放到同一网络上。
- [Cloudflare R2](https://www.cloudflare.com/products/r2/) — 兼容 S3 的对象存储，适合放图片、模型产物、下载包和静态资源。
- [Cloudflare Registrar](https://www.cloudflare.com/domains/) — 按注册局成本价购买域名，并可把 DNS 放在同一账户里管理。
- [Cloudflare Email Service](https://developers.cloudflare.com/email-service/) — 用自己的域名转发来信，或从 Workers 发送交易邮件。
- [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) — 替代传统验证码，给注册、登录和「生成」按钮做机器人防护，避免免费额度被刷光。
- [Vercel](https://vercel.com/) — 面向前端与全栈框架的托管和预览部署，适合 Next.js 一类 AI 网站和 SaaS。
- [GitHub Pages](https://pages.github.com/) — 直接从 GitHub 仓库发布静态网站，适合开源项目主页、文档和简单落地页。
- [Netlify](https://www.netlify.com/) — 静态站与前端托管，带预览部署和表单等常用能力，适合营销站和简单全栈应用。
- [Fly.io](https://fly.io/) — 把容器应用部署到靠近用户的区域，适合需要常驻进程、后台队列或靠近数据库的服务。
- [Render](https://render.com/) — 用较少配置托管 Web 服务、后台任务和数据库，适合早期全栈应用。
- [DigitalOcean](https://www.digitalocean.com/) — 提供云主机、托管数据库和 App Platform，适合需要自己控制运行环境，又不想一开始就上大型公有云的人。
- [Supabase](https://supabase.com/) — 基于 PostgreSQL 的后端平台，认证、数据库和存储可以一起开通，适合给 AI SaaS 先搭好用户和数据层。
- [Porkbun](https://porkbun.com/) — 定价相对透明的域名注册商，适合比较常见顶级域的售价和续费。
- [ImprovMX](https://improvmx.com/) — 把 `you@yourdomain` 免费转发到个人邮箱，适合先有专业收件地址，再上交易邮件。
- [Resend](https://resend.com/) — 面向开发者的交易邮件 API，适合验证信、收据、用量告警和通知。

<a id="global-payments--跨境收款" name="global-payments--跨境收款"></a>

## 💳 Global payments / 跨境收款

只整理各产品公开介绍的能力与常见适用场景，不涉及具体商户开通条件、账户配置或费率谈判。能否开通以官网当时公布的国家 / 主体要求为准。卖 AI SaaS 时还要单独核算模型成本、退款和拒付，不要只比较支付手续费。

- [Stripe](https://stripe.com/) — 全球收款基础设施，适合已有支持国家主体、要自建结账、订阅或按量计费的产品。
- [Stripe Payment Links](https://docs.stripe.com/payment-links) — 不用先写结账页，用链接出售一次性商品或订阅，适合先验证付费意愿。
- [Stripe Managed Payments](https://docs.stripe.com/payments/managed-payments) — Stripe 的商户记录（Merchant of Record）方案，由 Stripe 处理部分市场的销售税 / 增值税与争议，适合卖软件、数字产品和 AI 订阅。
- [Airwallex](https://www.airwallex.com/) — 多币种收款与全球账户，适合把海外收入换汇，或付款给供应商和自己的本地账户。
- [Paddle](https://www.paddle.com/) — 面向软件与 SaaS 的商户记录平台，负责结账和部分税务合规，适合不想自己处理全球间接税的卖家。
- [Polar](https://polar.sh/) — 开源友好的结账与商户记录服务，适合给开源项目、数字产品和订阅变现。
- [Lemon Squeezy](https://www.lemonsqueezy.com/) — 曾常用的数字产品商户记录平台；**已停止新注册**，并将于 2027 年 3 月 31 日停止处理交易。现有卖家请看官网的 [停运说明](https://www.lemonsqueezy.com/blog/saying-goodbye-to-lemon-squeezy) 与 [迁移 FAQ](https://docs.lemonsqueezy.com/migration/faq)，新项目请改看其他 MoR。
- [Creem](https://www.creem.io/) — 面向独立软件与数字产品的商户记录平台，适合在评估主体和地区要求之后，作为 Stripe / Paddle 之外的收款选项。
- [FastSpring](https://fastspring.com/) — 面向软件与数字产品的商户记录平台，适合卖许可证、下载软件和订阅。
- [Gumroad](https://gumroad.com/) — 低门槛出售电子书、模板和课程，适合先验证信息产品或配套资料，不必自建整套商城。
- [PayPal](https://www.paypal.com/business) — 买家认知度高的国际收款方式，常作为补充支付选项，而不是唯一的账户体系。
- [Wise Business](https://wise.com/business) — 跨境转账与多币种商业账户，适合把已经收到的货款转到自己常用的银行账户。
- [Payoneer](https://www.payoneer.com/) — 面向跨境卖家和自由职业者的收款与付款账户，适合需要接收多平台打款的场景。

<a id="company--compliance--公司与合规" name="company--compliance--公司与合规"></a>

## 🏢 Company & compliance / 公司与合规

方便查找香港、新加坡、美国主体和向欧盟销售时的**官方公开资料**。设立主体、报税和跨境销售义务因个人情况而异，请以政府官网最新文本和持牌专业人士的意见为准。

- [GovHK: Business & Company Registration](https://www.gov.hk/en/business/registration/businesscompany/) — 香港政府关于商业登记与公司注册的总览入口。
- [Companies Registry: How to register a new company](https://www.cr.gov.hk/en/services/register-company.htm) — 香港公司注册处的官方注册说明，查流程和电子注册渠道。
- [InvestHK](https://www.investhk.gov.hk/en/) — 香港投资推广署，提供在港开业的公开介绍与联络渠道。
- [IRD: Profits Tax](https://www.ird.gov.hk/eng/tax/bus_pft.htm) — 香港税务局利得税公开说明，了解公司税务的官方口径。
- [GoBusiness: Register your business](https://www.gobusiness.gov.sg/resources/start-up-guide/register-your-business) — 新加坡政府创业指南中的注册步骤，从选择主体类型走到正式登记。
- [ACRA: Registering a business](https://www.acra.gov.sg/register/business/) — 新加坡会计与企业管制局（ACRA）的官方登记入口和主体结构说明。
- [IRAS: Corporate Income Tax](https://www.iras.gov.sg/taxes/corporate-income-tax) — 新加坡税务局公司所得税官方入口，含基础指南、申报和税率等公开说明。
- [Stripe Atlas](https://stripe.com/atlas) — 协助在美国设立公司并开通收款的公开产品，适合需要美国主体的出海团队（资格和范围以官网为准）。
- [IRS: Starting a Business](https://www.irs.gov/businesses/small-businesses-self-employed/starting-a-business) — 美国国税局给新企业的税务入门，设立美国主体后应先读的官方材料。
- [Delaware Division of Corporations](https://corp.delaware.gov/) — 特拉华州公司注册处官网，许多美国公司在此注册，用于查阅官方手续与文件。
- [EU VAT One Stop Shop](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) — 向欧盟消费者销售数字服务或 AI 订阅时，了解 VAT OSS 统一申报机制的官方说明。
- [European Commission: Data protection](https://commission.europa.eu/law/law-topic/data-protection_en) — 欧盟委员会的数据保护主题页，处理欧盟用户数据或模型输入前先看官方框架。
- [TermsFeed](https://www.termsfeed.com/) — 生成隐私政策与服务条款等网站文本的工具，适合先有一份可公开的页面草稿；生成结果仍需结合自身业务和法律意见修改。

<a id="launch--directories--发布与目录" name="launch--directories--发布与目录"></a>

## 🚀 Launch & directories / 发布与目录

把可试用的产品放到目标用户会浏览的目录和社区，按各平台现行规则提交，不要买票或组织刷赞。

- [Product Hunt](https://www.producthunt.com/) — 科技产品最常见的发布日平台；用个人账号即可提交，不要买票或组织刷赞。
- [Show HN](https://news.ycombinator.com/showhn.html) — 在 Hacker News 展示你自己做的东西，适合已有可试用产品、并愿意接受直接反馈的发布。
- [Indie Hackers](https://www.indiehackers.com/) — 独立开发者社区，适合分享构建过程、看收入案例和找早期用户，而不是只丢一条发布帖。
- [BetaList](https://betalist.com/) — 面向早期产品的目录；目前为付费提交、经审核后展示，适合预发布或刚上线的产品。
- [Peerlist Launchpad](https://peerlist.io/launchpad) — 面向开发者和设计师的每周发布窗口，需先完成个人主页和项目资料。
- [DevHunt](https://devhunt.org/) — 开发者工具目录，可先免费常驻展示；若要参加当周首页发布，以官网现行规则为准。
- [PoweredByAI](https://poweredbyai.app/) — 面向 AI 产品的展示目录，适合把刚上线的 AI SaaS 或网站提交到可被浏览的列表里（提交规则以官网为准）。
- [W2Solo](https://w2solo.com/) — 中文独立开发者社区，适合用中文讨论一人公司产品、收早期反馈，再把正式发布放到英文目录。
- [AlternativeTo](https://alternativeto.net/) — 软件替代品目录，适合已经有明确竞品、希望被比较搜索找到的工具。

<a id="content--acquisition--内容与获客" name="content--acquisition--内容与获客"></a>

## ✍️ Content & acquisition / 内容与获客

先把独立站内容、搜索收录和分析摆正，再按各社区规则做发布和讨论，而不是一上来就群发广告。

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) — Google 官方 SEO 入门，做独立站内容前先读这一份。
- [Google Search Console](https://search.google.com/search-console/about) — 查看网站在 Google 搜索中的展示、索引和问题，上线后应尽早验证域名。
- [Bing Webmaster Tools](https://www.bing.com/webmasters/about) — 向 Bing 提交站点并查看收录，也影响部分基于 Bing 的搜索产品。
- [Ahrefs SEO Course for Beginners](https://ahrefs.com/academy/seo-training-course) — 免费的系统 SEO 课程，适合把官方原则落实成选题和页面结构。
- [Google Trends](https://trends.google.com/trends/) — 查看关键词和主题的公开搜索趋势，适合在做 AI 产品选题和内容计划前先看需求是否稳定。
- [Plausible](https://plausible.io/) — 轻量、偏隐私友好的网站分析，适合早期独立站先看趋势、少埋一堆标签。
- [Umami](https://umami.is/) — 开源网站分析，可自托管，适合要把访问数据留在自己这边的人。
- [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/) — 站点已接入 Cloudflare 时可用的免费分析，先看访问趋势再上更重的工具。
- [Ghost](https://ghost.org/) — 面向出版的开源博客 / 会员系统，适合把内容站和付费订阅放在一起。
- [Hashnode](https://hashnode.com/) — 可绑定自己域名的技术博客平台，适合开发者先把教程和产品故事写起来，再视情况迁独立站。
- [Buttondown](https://buttondown.com/) — 面向独立创作者的电子报工具，适合用邮件把试用用户和读者留下来。
- [Hacker News Guidelines](https://news.ycombinator.com/newsguidelines.html) — 在 HN 发帖或回帖前必读的社区准则，避免被当成广告处理。
- [Reddit: Self-promotion guidelines](https://www.reddit.com/wiki/selfpromotion/) — Reddit 关于自我推广的约定，发产品帖前先读，并先参与讨论。
- [r/SideProject](https://www.reddit.com/r/SideProject/) — 分享副作用和独立项目的版块，发帖时注意版规和宣传比例。
- [X Rules and Policies](https://help.x.com/en/rules-and-policies) — X（Twitter）官方规则与政策入口，用它做内容获客前先了解平台规则。

<a id="open-source-templates--examples--开源模板与案例" name="open-source-templates--examples--开源模板与案例"></a>

## 📦 Open-source templates & examples / 开源模板与案例

可直接 fork 的官方或开源起步模板，先跑通登录、收款和部署，再换成自己的业务。

- [Next.js SaaS Starter](https://github.com/nextjs/saas-starter) — 可 fork 的 SaaS 起步模板，含登录、Stripe 订阅和后台，适合先跑通再换成自己的 AI 业务。
- [Stripe Samples](https://github.com/stripe-samples) — Stripe 官方示例集，按结账、订阅等场景抄可运行的代码。
- [Cloudflare Templates](https://github.com/cloudflare/templates) — Cloudflare 官方的 Workers / 全栈起步模板，适合在 Workers 上开新项目。
- [Open SaaS](https://github.com/wasp-lang/open-saas) — 开源 SaaS 模板，认证、支付、博客等模块较全；配套文档见 [docs.opensaas.sh](https://docs.opensaas.sh/)。
- [React Email](https://react.email/) — 用 React 编写交易邮件模板的开源方案，常与 Resend 等发送服务一起用。
- [WXT](https://wxt.dev/) — 浏览器扩展开发框架，适合一个人把 AI 能力做成 Chrome / Edge 插件并上架到海外商店。
- [Supabase Getting Started](https://supabase.com/docs/guides/getting-started) — 官方入门与示例入口，适合给出海产品加上认证、数据库和存储。

<a id="ai-出海项目--showcase" name="ai-出海项目--showcase"></a>

## 🌏 AI 出海项目 / Showcase

这里收录华人独立开发者已经做出来、面向海外用户或按美金收费的 AI 产品。读者可以照着找方向，编程 Agent 也可以把新项目补进来。

上面的「一人公司可做的 AI 业务场景」收框架和工具。这一节收已经能打开的产品：面向海外用户、核心能力是 AI。只服务国内用户的微信小程序、证件照、中文转写一类不在此列，也不收打不开的链接、非官方模型中转，以及大量彼此相似的「一个页面换多家模型」站点。同一类只留用户收益分得开的产品。链接在 2026 年 11 月核对过。收费方式和免费额度会变，以官网当时页面为准。

欢迎读者提交自己的项目，也欢迎编程 Agent 代为提交。发 Pull Request 或 Issue 都可以，一个条目只放一个产品。介绍怎么写、放进哪一类，见 [CONTRIBUTING.md](CONTRIBUTING.md#提交-ai-出海项目) 的「提交 AI 出海项目」。

每条的格式是：`[产品名](官网) — 作者 · [GitHub 用户名](https://github.com/用户名)：一句中文，写用户得到的具体好处。` 作者名和 GitHub 用户名相同时只写一次。不知道的作者不要编。

### 🖼️ 图像 / Image

- [Reletter](https://aiedittextinimage.com/) — Berry-hcy：只改截图、菜单或商品图里的某一行字，其余画面保持不动；需要时再重绘那一块。
- [unblurry](https://unblurry.tools) — edenSu · [edenSu-git](https://github.com/edenSu-git)：把手抖或失焦的照片丢进去，把糊掉的细节补回来，免注册可以先试。
- [TattooTryOn](https://tattootryon.app/) — [Yuzu-Peel](https://github.com/Yuzu-Peel)：把纹身图样放在自己手臂或小腿的照片上，先看它贴合肤色和光线之后的样子。
- [My Face Analyzer](https://myfaceanalyzer.com) — deepblue1991：一张正脸自拍就能在照片上看到脸型、对称和黄金比例，计算在浏览器里完成；详细报告里还有按这张脸生成的发型试戴。
- [Spaceora](https://spaceora.app/) — [Zin](https://github.com/zina26)：拍一张房间或院子的照片，预览换成真实家具之后的布置，院子则按当地气候挑选植物。

### 🎬 视频 / Video

- [blubiu](https://blubiu.ai) — [stimQQ](https://github.com/stimQQ)：角色和场景先存成资产，后面每条动画都沿用同一班人，不用每镜重新描述长相。
- [Textless](https://textless.video/) — Kuber · [iam-tin](https://github.com/iam-tin)：自动找出或框选画面里的字幕和水印，擦掉后把后面的背景补上，可以先不登录试一小段。
- [ShotTide](https://shottide.com/) — Jianyu Chen · [CJianYu](https://github.com/CJianYu)：写好脚本和分镜，补上旁白，导出一支短片。
- [Tapemoon](https://tapemoon.com) — [suio03](https://github.com/suio03)：上传一整首歌，按人声生成一支对得上歌词的音乐视频。
- [Captions Generator](https://captionsgenerator.app/) — [iaminyu](https://github.com/iaminyu)：丢进一条视频，得到跟每个词对齐的字幕，改字、换样式或译成别的语言后，导出成片或 SRT。

### 🎵 音乐 / Music

- [MemoTune](https://memotune.com) — [AlvyVV](https://github.com/AlvyVV)：写下一句想法、一段歌词或一个故事，生成一首带人声或纯配乐的完整歌曲。

### 🧊 三维 / 3D

- [Photo to 3D Model](https://phototo3dmodel.org/) — Jianyu Chen · [CJianYu](https://github.com/CJianYu)：拍一件物品的一张照片，在浏览器里转着看，并下载可以继续编辑的 GLB 模型。

### 🎨 设计 / Design

- [LogoAnimation](https://logoanimation.net/) — Miracle · [zhoulianbo](https://github.com/zhoulianbo)：上传现有标志，选一种出场或用文字描述动作，下载一段能当片头的视频。
- [LayerGrab](https://layergrab.com) — [stimQQ](https://github.com/stimQQ)：把一张成图拆成带名字的图层，补上被挡住的背景，导出 PNG 或 PSD。
- [Logent AI](https://logent.ai/) — 疯狂的小波（武汉）：写下产品名称和它做什么，生成可以直接当作品牌标志的方案。
- [Image Translate AI](https://imagetranslate.ai) — Corey Chiu（深圳） · [iamcorey](https://github.com/iamcorey)：把商品图、漫画或菜单上的文字换成另一种语言，原来的版式留在原处。
- [Kite](https://kite.new) — Loukman Nacik · [itsloukman](https://github.com/itsloukman)：让 Claude、ChatGPT、Cursor 或 Codex 通过托管 MCP 服务器直接在设计文件里画出可编辑的图层，团队同一文件实时修改，还能复制到 Figma 或导出 React 代码。

### 📝 写作与内容 / Writing

- [VibeCV](https://vibecv.com) — Rory · [Coiggahou2002](https://github.com/Coiggahou2002)：把经历聊出来，整理成可以投出去的一页简历，第一份免费。
- [UUScribe](https://scribe.uustudio.cc/) — UU Studio · [6a209](https://github.com/6a209)：上传录音或贴一条 YouTube 链接，得到可以校对的文字稿，区分说话人，再导出文档或字幕。

### 🧰 开发者向 / Developer

- [AI Game Makers](https://aigamemakers.com/) — cian · [a3011336204-cmyk](https://github.com/a3011336204-cmyk)：用一句中文或英文描述一款 Roblox 游戏，得到带地图、脚本和界面、能在 Roblox Studio 里打开的成品。
- [AppIconKitchen](https://www.appiconkitchen.com/) — Ricky Lee（深圳）：用一段话描述应用，导出 iOS、Android 和网页各自要的整套图标。

### ⚡ 效率 / Productivity

- [MomentSift](https://momentsift.com/) — AnshengHu · [zgaobai](https://github.com/zgaobai)：几千张照片里，模糊和闭眼的会先被标出来，原片留在自己的设备上。
- [Refto](https://refto.one) — [hehehai](https://github.com/hehehai)：把图片、视频和 PDF 收进 Mac 上的一个库，再用画面里的字或录音里的话找回来，识别在本机完成。
- [BayesChat](https://bayeschat.xyz) — [fan3cn](https://github.com/fan3cn)：在 iPhone 上用自己的模型密钥聊天，对话记忆留在手机里，需要时再接上 MCP 工具。
- [PetWaits](https://petwaits.com/) — ZHANG LINGQING：用一张自家猫狗的照片，做成会在桌面上唱歌、陪你工作的桌宠。
- [DisconfirmAI](https://disconfirmai.com/) — [tumingke0](https://github.com/tumingke0)：做一个判断之前，先整理可能推翻它的公开材料，并附上原文链接。

### 🎲 游戏 / Games

- [Gridku](https://www.gridku.com/) — Worldku 团队：在浏览器里和你的 AI 下国际象棋、中国象棋或五子棋，对面的每一步由它来走。

<a id="作者--配套手册" name="作者--配套手册"></a>

## 👤 作者 / 配套手册

这份清单由 [橙哥出海](https://x.com/OPCchuhai) 整理。网站：[opcchuhai.com](https://opcchuhai.com/)，一个人把产品卖到海外时会用到的方法、工具和案例都在这里。

我把这些坑写成了手册和工具包：[《出海赚美金》书+工具包](https://opcchuhai.com/books/zhuan-meijin/)。

<a id="license--许可" name="license--许可"></a>

## 📄 License / 许可

本作品采用 [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) 许可，完整文本见仓库中的 [LICENSE](LICENSE)。欢迎转载和衍生，请保留署名。
