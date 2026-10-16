<div align="center" id="trendradar">

<a href="https://github.com/sansan0/TrendRadar" title="TrendRadar">
  <img src="/_image/banner.webp" alt="TrendRadar Banner" width="80%">
</a>

最快<strong>30秒</strong>部署的热点助手 —— 告别无效刷屏，只看真正关心的新闻资讯

<a href="https://trendradar.sandev.cc/zh/" title="TrendRadar 官方网站"><strong>🌐 官方网站</strong></a> · <a href="https://trendradar.sandev.cc/zh/docs/quick-start/" title="TrendRadar 官网文档"><strong>📖 官网文档</strong></a> · <a href="https://trendradar.sandev.cc/zh/docs/self-hosted-sources/" title="AI 自建热榜数据源"><strong>AI 自建热榜数据源</strong></a>

<a href="https://trendshift.io/repositories/14726" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14726" alt="sansan0%2FTrendRadar | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>


[![GitHub Stars](https://img.shields.io/github/stars/sansan0/TrendRadar?style=flat-square&logo=github&color=yellow)](https://github.com/sansan0/TrendRadar/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/sansan0/TrendRadar?style=flat-square&logo=github&color=blue)](https://github.com/sansan0/TrendRadar/network/members)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-v6.11.0-blue.svg)](https://github.com/sansan0/TrendRadar)
[![MCP](https://img.shields.io/badge/MCP-v4.1.1-green.svg)](https://github.com/sansan0/TrendRadar)
[![Docker Pulls](https://img.shields.io/docker/pulls/wantcat/trendradar?style=flat-square&logo=docker&logoColor=white&label=TrendRadar%20Pulls&color=2496ED)](https://hub.docker.com/r/wantcat/trendradar)
[![Docker Pulls](https://img.shields.io/docker/pulls/wantcat/trendradar-mcp?style=flat-square&logo=docker&logoColor=white&label=MCP%20Pulls&color=2496ED)](https://hub.docker.com/r/wantcat/trendradar-mcp)
[![RSS](https://img.shields.io/badge/RSS-订阅源支持-orange.svg?style=flat-square&logo=rss&logoColor=white)](#rss-订阅源支持v450-新增)
[![AI翻译](https://img.shields.io/badge/AI-多语言推送-purple.svg?style=flat-square)](#ai-多语言翻译v520-新增)
[![MCP Support](https://img.shields.io/badge/MCP-AI分析支持-FF6B6B?style=flat-square&logo=ai&logoColor=white)](#-mcp-客户端)
[![AI分析推送](https://img.shields.io/badge/AI-分析推送-FF6B6B?style=flat-square&logo=openai&logoColor=white)](#ai-分析推送v500-新增)
[![AI智能筛选](https://img.shields.io/badge/AI-智能筛选新闻-9B59B6?style=flat-square&logo=openai&logoColor=white)](#ai-智能筛选新闻v650-新增)

[![企业微信通知](https://img.shields.io/badge/企业微信-通知-00D4AA?style=flat-square)](https://work.weixin.qq.com/)
[![个人微信通知](https://img.shields.io/badge/个人微信-通知-00D4AA?style=flat-square)](https://weixin.qq.com/)
[![Telegram通知](https://img.shields.io/badge/Telegram-通知-00D4AA?style=flat-square)](https://telegram.org/)
[![dingtalk通知](https://img.shields.io/badge/钉钉-通知-00D4AA?style=flat-square)](#)
[![飞书通知](https://img.shields.io/badge/飞书-通知-00D4AA?style=flat-square)](https://www.feishu.cn/)
[![邮件通知](https://img.shields.io/badge/Email-通知-00D4AA?style=flat-square)](#)
[![ntfy通知](https://img.shields.io/badge/ntfy-通知-00D4AA?style=flat-square)](https://github.com/binwiederhier/ntfy)
[![Bark通知](https://img.shields.io/badge/Bark-通知-00D4AA?style=flat-square)](https://github.com/Finb/Bark)
[![Slack通知](https://img.shields.io/badge/Slack-通知-00D4AA?style=flat-square)](https://slack.com/)
[![通用Webhook](https://img.shields.io/badge/通用-Webhook-607D8B?style=flat-square&logo=webhook&logoColor=white)](#)


[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-自动化-2088FF?style=flat-square&logo=github-actions&logoColor=white)](#-快速开始)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-部署-4285F4?style=flat-square&logo=github&logoColor=white)](https://sansan0.github.io/TrendRadar)
[![Docker](https://img.shields.io/badge/Docker-部署-2496ED?style=flat-square&logo=docker&logoColor=white)](#6-docker-部署)
[![本地部署](https://img.shields.io/badge/本地-部署-28A745?style=flat-square&logo=python&logoColor=white)](#local-deploy)
[![Cloudflare Pages](https://img.shields.io/badge/Cloudflare_Pages-部署-F38020?style=flat-square&logo=cloudflare&logoColor=white)](#cloudflare-deploy)

</div>

<div align="center">

**中文** | **[English](README-EN.md)**

</div>

> 本项目以轻量，易部署为目标

<br>

## 📑 快速导航

> 💡 **点击下方链接**可快速跳转到对应章节。部署推荐从「**快速开始**」入手，需要详细自定义请看「**配置详解**」

<div align="center">

|   |   |   |
|:---:|:---:|:---:|
| [🚀 **快速开始**](#-快速开始) | [AI 智能分析](#-ai-智能分析) | [⚙️ **配置详解**](#配置详解) |
| [Docker部署](#6-docker-部署) / [本地部署](#local-deploy) | [MCP客户端](#-mcp-客户端) | [📝 **更新日志**](#-更新日志) |
| [🎯 **核心功能**](#-核心功能) | [💬 **社区交流**](#community) | [📚 **项目相关**](#-项目相关) |

</div>

<br>

- 感谢**为项目点 star** 的观众们，**fork** 你所欲也，**star** 我所欲也，两者得兼😍是对开源精神最好的支持

<details>
<summary>👉 点击展开：<strong>致谢名单</strong> (天使轮荣誉榜 🔥73+🔥 位)</summary>

### 早期支持者致谢

> 💡 **特别说明**：
>
> 1. **关于名单**：下方表格记录了项目起步阶段（天使轮）的支持者。因早期人工统计繁琐，**难免存在疏漏或记录不全的情况，如有遗漏，实非本意，万望海涵**。
> 2. **未来规划**：为了将有限的精力回归代码与功能迭代，**即日起不再人工维护此名单**。
>
> 无论名字是否上榜，你们的每一份支持都是 TrendRadar 能够走到今天的基石。🙏

### 基础设施支持

感谢 **GitHub** 免费提供的基础设施，这是本项目得以**一键 fork**便捷运行的最大前提。

### 数据支持

本项目使用 [newsnow](https://github.com/ourongxing/newsnow) 项目的 API 获取多平台数据，特别感谢作者提供的服务。

经联系，作者表示无需担心服务器压力，但这是基于他的善意和信任。请大家：
- **前往 [newsnow 项目](https://github.com/ourongxing/newsnow) 点 star 支持**
- Docker 部署时，请合理控制推送频率，勿竭泽而渔

### 推广助力

> 感谢以下平台和个人的推荐(按时间排列)

- [小众软件](https://mp.weixin.qq.com/s/fvutkJ_NPUelSW9OGK39aA) - 开源软件推荐平台
- [LinuxDo 社区](https://linux.do/) - 技术爱好者的聚集地
- [阮一峰周刊](https://github.com/ruanyf/weekly) - 技术圈有影响力的周刊

### 观众支持

> 感谢**给予资金支持**的朋友们，你们的慷慨已化身为键盘旁的零食饮料，陪伴着项目的每一次迭代。
>
> **关于"一元点赞"的回归**：
> 随着 v5.0.0 版本的发布，项目迈入了一个新的阶段。为了支持日益增长的 API 成本和咖啡因消耗，"一元点赞"通道现已重新开启。你的每一份心意，都将转化为代码世界里的 Token 和动力。🚀 [前往支持](#-支持项目)

|           点赞人            |  金额  |  日期  |             备注             |
| :-------------------------: | :----: | :----: | :-----------------------: |
|           D*5          |  1.8 * 3 | 2025.11.24  |    | 
|           *鬼          |  1 | 2025.11.17  |    | 
|           *超          |  10 | 2025.11.17  |    | 
|           R*w          |  10 | 2025.11.17  | 这 agent 做的牛逼啊,兄弟    | 
|           J*o          |  1 | 2025.11.17  | 感谢开源,祝大佬事业有成    | 
|           *晨          |  8.88  | 2025.11.16  | 项目不错,研究学习中    | 
|           *海          |  1  | 2025.11.15  |    | 
|           *德          |  1.99  | 2025.11.15  |    | 
|           *疏          |  8.8  | 2025.11.14  |  感谢开源，项目很棒，支持一下   | 
|           M*e          |  10  | 2025.11.14  |  开源不易，大佬辛苦了   | 
|           **柯          |  1  | 2025.11.14  |     | 
|           *云          |  88  | 2025.11.13  |    好项目，感谢开源  | 
|           *W          |  6  | 2025.11.13  |      | 
|           *凯          |  1  | 2025.11.13  |      | 
|           对*.          |  1  | 2025.11.13  |    Thanks for your TrendRadar  | 
|           s*y          |  1  | 2025.11.13  |      | 
|           **翔          |  10  | 2025.11.13  |   好项目，相见恨晚，感谢开源！     | 
|           *韦          |  9.9  | 2025.11.13  |   TrendRadar超赞，请老师喝咖啡~     | 
|           h*p          |  5  | 2025.11.12  |   支持中国开源力量，加油！     | 
|           c*r          |  6  | 2025.11.12  |        | 
|           a*n          |  5  | 2025.11.12  |        | 
|           。*c          |  1  | 2025.11.12  |    感谢开源分享    | 
|           *记          |  1  | 2025.11.11  |        | 
|           *主          |  1  | 2025.11.10  |        | 
|           *了          |  10  | 2025.11.09  |        | 
|           *杰          |  5  | 2025.11.08  |        | 
|           *点          |  8.80  | 2025.11.07  |   开发不易，支持一下。     | 
|           Q*Q          |  6.66  | 2025.11.07  |   感谢开源！     | 
|           C*e          |  1  | 2025.11.05  |        | 
|           Peter Fan          |  20  | 2025.10.29  |        | 
|           M*n          |  1  | 2025.10.27  |      感谢开源  | 
|           *许          |  8.88  | 2025.10.23  |      老师 小白一枚，摸了几天了还没整起来，求教  | 
|           Eason           |  1  | 2025.10.22  |      还没整明白，但你在做好事  | 
|           P*n           |  1  | 2025.10.20  |          |
|           *杰           |  1  | 2025.10.19  |          |
|           *徐           |  1  | 2025.10.18  |          |
|           *志           |  1  | 2025.10.17  |          |
|           *😀           |  10  | 2025.10.16  |     点赞     |
|           **杰           |  10  | 2025.10.16  |          |
|           *啸           |  10  | 2025.10.16  |          |
|           *纪           |  5  | 2025.10.14  | TrendRadar         |
|           J*d           |  1  | 2025.10.14  | 谢谢你的工具，很好玩...          |
|           *H           |  1  | 2025.10.14  |           |
|           那*O           |  10  | 2025.10.13  |           |
|           *圆           |  1  | 2025.10.13  |           |
|           P*g           |  6  | 2025.10.13  |           |
|           Ocean           |  20  | 2025.10.12  |  ...真的太棒了！！！小白级别也能直接用...         |
|           **培           |  5.2  | 2025.10.2  |  github-yzyf1312:开源万岁         |
|           *椿           |  3  | 2025.9.23  |  加油，很不错         |
|           *🍍           |  10  | 2025.9.21  |           |
|           E*f           |  1  | 2025.9.20  |           |
|           *记            |  1  | 2025.9.20  |           |
|           z*u            |  2  | 2025.9.19  |           |
|           **昊            |  5  | 2025.9.17  |           |
|           *号            |  1  | 2025.9.15  |           |
|           T*T            |  2  | 2025.9.15  |  点赞         |
|           *家            |  10  | 2025.9.10  |           |
|           *X            |  1.11  | 2025.9.3  |           |
|           *飙            |  20  | 2025.8.31  |  来自老童谢谢         |
|           *下            |  1  | 2025.8.30  |           |
|           2*D            |  88  | 2025.8.13 下午 |           |
|           2*D            |  1  | 2025.8.13 上午 |           |
|           S*o            |  1  | 2025.8.05 |   支持一下        |
|           *侠            |  10  | 2025.8.04 |           |
|           x*x            |  2  | 2025.8.03 |  trendRadar 好项目 点赞          |
|           *远            |  1  | 2025.8.01 |            |
|           *邪            |  5  | 2025.8.01 |            |
|           *梦            |  0.1  | 2025.7.30 |            |
|           **龙            |  10  | 2025.7.29 |      支持一下      |


</details>

<br>

## 🪄 赞助商

> **[RapidProxy](https://www.rapidproxy.io/?ref=TrendRadar)** 提供全球住宅代理网络，面向多平台数据采集、AI 分析与自动化监控，支持智能轮换与粘性会话，灵活应对跨地区访问和持续数据获取需求。动态住宅 **\$0.55/GB 起**，静态住宅 **\$5/IP/月起**。
>
> 使用专属优惠码 **`RAPID10`**，享 **9 折优惠**。[立即免费试用](https://www.rapidproxy.io/?ref=TrendRadar)。

<a href="https://www.rapidproxy.io/?ref=TrendRadar"><img src="_image/banner-rapidproxy.webp" alt="RapidProxy 海外高质量代理IP服务，90M+ 真实住宅 IPs，流量永不过期，支持 HTTP(S)/SOCKS5 与智能IP轮换，免费测试" width="100%"></a>

<br>

> **[Swiftproxy](https://www.swiftproxy.net/?ref=sansan0)** 专注于提供高质量动态与静态住宅代理，支持灵活的 IP 轮换与粘性会话。适用于热点追踪、网页抓取与自动化数据采集，为你的项目提供更稳定可靠的网络访问支持。
>
> 使用优惠码 **`PROXY90`**，即可享受 **九折优惠**。

<!-- 赞助商横幅尺寸：1400 × 300 px（14:3），以 100% 宽度展示；参考 302.AI 的 992 × 250 px 与火山引擎的 1400 × 400 px，新版沿用 1400 px 宽度并缩短高度。 -->
<a href="https://www.swiftproxy.net/?ref=sansan0"><img src="_image/banner-swiftproxy.webp" alt="Swiftproxy 全球住宅代理" width="100%"></a>

[有意赞助？点击查看赞助与合作详情](https://trendradar.sandev.cc/zh/sponsors/)

<br>

### 🤝 二次开发与引用

如果你在项目中使用或借鉴了本项目的思路、核心代码，**非常欢迎**在 README 或文档中注明来源并附上本仓库链接。

这将有助于项目的持续维护和社区发展，感谢你的尊重与支持！❤️


<a name="community"></a>

### 💬 社区交流

- **GitHub Issues**：适合具体的技术问题。提问时请提供完整信息（截图、错误日志等），有助于快速定位。
- **公众号交流**：建议优先在相关文章下的留言区交流。若需后台提问，**先点赞/推荐**文章是最好的"敲门砖"，我在后台都能感受到这份心意哟 (´▽`ʃ♡ƪ)。
- **QQ 群交流**：无论你是 AI 小白还是硬核开发者，想求助技术问题还是分享折腾心得，这里都欢迎你。群里主打互助交流和灵感碰撞，入群请先看群公告；提问时描述清楚问题、附上截图，群友有空就会帮忙，大家的实战经验往往比我一个人更快更全面 🤝

> **友情提示**：
> 本项目为开源分享，非商业产品。把作者当朋友而非客服，沟通效率会更高哦！

<div align="center">

| 公众号关注 | QQ 群交流 |
| :---: | :---: |
| <img src="_image/weixin.png" width="500" title="硅基茶水间"/> | <img src="_image/qq-group.png" alt="TrendRadar QQ 群二维码，群号 1007671021" width="150"/> |

</div>

<br>

<a name="-支持项目"></a>

### 🧩 作者的另一款工具：SanFrame

<table role="presentation">
<tr>
<td width="96" align="center">
<a href="https://ocr.sandev.cc/zh/"><img src="_image/sanframe-icon.webp" alt="SanFrame" width="72" height="72"></a>
</td>
<td align="left">
<strong>多设备资料与剪贴板管理</strong><br>
集中管理文字、图片、文件与剪贴板，支持 Windows / macOS 与 Android 传输端局域网互传。桌面端支持按需同步、离线 OCR、截图标注和 PDF 处理，无需账号，本地优先。
<br><br>
<a href="https://ocr.sandev.cc/zh/"><strong>了解 SanFrame →</strong></a>
</td>
</tr>
</table>

<br>

## 📝 更新日志

> **📌 查看最新更新**：**[原仓库更新日志](https://github.com/sansan0/TrendRadar?tab=readme-ov-file#-更新日志)** ：
- **提示**：建议查看【历史更新】，明确具体的【功能内容】


### 2026/10/13 - v6.11.0

- **中英文配置编辑**：可视化编辑器支持中英文切换，并提供英文配置模板，方便按熟悉的语言设置运行参数、关键词和调度规则
- **更多部署选择**：可选配置 Cloudflare Pages 自动部署，抓取完成后自动发布网页报告；补充基于 `uv` 的本地部署说明，方便在本机运行
- **抓取与配置稳定性**：RSS 临时请求失败时仅立即重试一次；修复时间解析中的小数秒与时区偏移、全局过滤正则和 AI 自定义参数传递，并避免远程存储检查失败时误建空库

### 2026/02/09 - mcp-v4.0.0

- **🔥 AI 消息直推所有渠道**：让 AI 写好的内容一键推送到飞书、钉钉、Telegram、邮件等 9 个渠道，Markdown 自动适配各平台格式，不用操心格式差异
- **新增格式化策略指南**：新增 `get_channel_format_guide` 工具，告诉 AI 每个渠道支持什么格式、有什么限制，生成的内容排版更好看
- **智能分批发送**：超长消息自动按各渠道字节限制拆分（飞书 30KB、钉钉 20KB 等），配置读取自 config.yaml
- **修复渠道误检测**：ntfy 不再因为默认地址被误报为"已配置"
- **代码复用优化**：批次处理函数直接复用 trendradar 核心模块，不重复造轮子


<details>
<summary>👉 点击展开：<strong>历史更新</strong></summary>

### 2026/06/19 - v6.10.0

- **AI 翻译分批处理**：大量标题翻译时自动分批请求，避免单次请求超限导致翻译失败
- **模块拆分重构**：拆分 context.py 和 \_\_main\_\_.py，AI 筛选流水线独立为 filter_pipeline 模块，职责更清晰、维护更方便
- **修复飞书来源标签显示**：修复飞书卡片中来源标签和 AI 独立源点速览被 CommonMark 吞掉不显示的问题

### 2026/06/02 - v6.9.0

- **热榜域名安全校验**：新增 `expected_domain` 配置项，校验返回数据链接的域名合法性，不匹配时自动丢弃数据并警告，有效防范链接劫持或数据篡改
- **自定义热榜 API 地址**：支持自部署 newsnow 并配置 `api_url` 使用自己的数据源

### 2026/05/23 - v6.8.0

- **HTML 报告全面增强**：新增报告元数据展示（生成时间、数据来源、版本号）、暗色模式自动适配、Tab 栏交互优化、趋势箭头可视化，浏览器阅读体验大幅提升
- **版本检查 CDN 多源回退**：版本检查接口支持 GitHub → jsDelivr → Cloudflare 等多个 CDN 源自动回退，国内网络环境也能稳定获取更新提示
- **展示区域开关生效**：HTML 报告和邮件现在正确尊重 `display.regions.ai_analysis` 和 `display.regions.standalone` 开关，关闭即不渲染
- **导出按钮修复**：修复导出按钮点击后下拉菜单图标消失的问题
- **Markdown 导出修复**：修复 HTML 报告 Markdown 导出中 JS 换行符转义错误

### 2026/05/15 - v6.7.0

- **Markdown 导出**：报告导出下拉菜单新增 Markdown 格式，一键生成带链接的结构化文本，方便 LLM 二次加工和跨平台分享（[#1121](https://github.com/sansan0/TrendRadar/issues/1121)）
- **RSS guid 去重**：RSS 存储新增 guid 字段，去重优先级改为 guid > url，解决同一文章因 URL 变化导致重复入库的问题
- **空标题防护**：解析器、渲染层、翻译回填全链路增加空标题兜底逻辑，确保无标题条目也能正常显示
- **翻译质量增强**：翻译提示词要求保留编号顺序，空翻译结果不再覆盖原始标题

### 2026/03/28 - v6.6.0

- **HTML 报告浏览器增强**：在浏览器中打开报告可自动切换宽屏布局，关键词分组和独立展区均支持 Tab 快速切换，搜索框实时过滤新闻标题，邮件客户端仍显示原始窄屏布局，零回归
- **暗色模式**：一键切换深色主题，自动记住偏好，适合夜间阅读
- **一键复制新闻**：鼠标悬停新闻序号即可复制标题和链接，方便快速分享
- **导出优化**：整页截图和分段截图合并为下拉式导出按钮，截图时自动还原干净布局
- **快捷键系统**：支持 `W` 宽屏切换、`D` 暗色模式、`/` 搜索、`?` 查看快捷键提示
- **阅读进度条**：页面顶部实时显示阅读进度

### 2026/03/12 - v6.5.0

- **AI 智能筛选系统**：不用再手动设关键词！在 `ai_interests.txt` 里用日常语言写下你关注的方向（如"我想看 AI 和新能源相关新闻"），AI 会自动提取标签并对每条新闻打分，只推送真正和你相关的内容。万一 AI 筛选出了问题，会自动切回关键词匹配，推送不中断
- **每个时段支持不同的筛选方式和关注方向**：Timeline 中的每个时间段现在可以独立设置用什么方式筛选、看什么类型的新闻。比如：早上用"科技关键词"快速过滤，晚上换成"金融 AI 兴趣描述"做深度筛选——同一个系统，不同时段看不同内容
- **AI 分析范围独立于推送**：AI 分析的数据范围可以和推送内容不同。比如推送只发新增消息（避免重复打扰），但 AI 分析当天全部新闻（看完整趋势）。每个时段也能单独设置 AI 分析模式
- **AI 筛选智能省钱**：已分析过的新闻不会重复消耗 token；兴趣描述修改后，AI 自动判断变化幅度——小改动只更新受影响的标签，大改动才全量重新分类
- **多文件配置与标签隔离**：自定义关键词文件放 `config/custom/keyword/`，AI 兴趣文件放 `config/custom/ai/`，不同文件产生的标签各自独立、互不干扰
- **AI 翻译精准控制**：可分别控制热榜、RSS、独立展示区是否翻译，没开启显示的区域自动跳过，不浪费 token
- **远程存储批量上传**：多次写操作攒在一起统一提交云端，减少 API 调用次数
- **每组关键词/标签展示数量限制**：通过 `max_news_per_keyword` 控制每个分组最多显示多少条新闻，避免单个热门话题占满整条推送
- **时段冲突智能检测**：两个时间段如果有时间重叠，系统会自动报错提醒修改，避免配置冲突导致意外行为
- 修复若干bug

### 2026/02/09 - v6.0.0

> **Breaking Change**：配置文件升级（config.yaml 2.0.0），旧版 `push_window` 和 `analysis_window` 配置不再兼容，请参考新版 config.yaml 迁移

- **统一调度系统**：新增 `timeline.yaml`，用一套配置控制「什么时间采集 / 推送 / AI 分析」
- **5 种预设模板**：`always_on`（全天候，默认）、`morning_evening`（早晚汇总）、`office_hours`（办公时间）、`night_owl`（夜猫子）、`custom`（自定义）；也支持在 `presets:` 下新增自己的模板，只要 key 不重复，然后在 config.yaml 里填你的模板名即可
- **灵活的时间段配置**：支持工作日/周末差异化、跨午夜时间段、per-period once 去重
- **可视化配置编辑器**：
  - 新增 `timeline.yaml` 编辑标签页，与 config.yaml / frequency_words.txt 并列
  - 预设模式卡片选择：点击即切换，自动同步 config.yaml 的 `schedule.preset`
  - 周视图时间线：7 天 × 24 小时水平条，用颜色区分推送/分析/采集状态
  - 可交互控件：开关、下拉框、时间选择器，右侧修改实时同步到左侧 YAML
  - 周映射下拉选择：根据日计划动态填充，拖拉点击即可完成调度配置
- **AI 提示词稳定性优化**（ai_analysis_prompt.txt v2.0.0）：
  - 格式规范独立说明：将换行/标签/序号/禁止事项从 JSON value 中抽出，作为独立章节
  - JSON 模板简化：字段描述缩短为一句话 + 字数限制，减少 AI 输出格式混乱
  - 去除 system prompt 中的 Markdown 格式，与"禁止 Markdown"指令保持一致
  - 所有 JSON 字段声明为可选，缺少任何字段不会报错，增强容错性
- **新增独立展示区 AI 概括分析**（`ai_analysis.include_standalone`）：
  - 新增独立开关，开启后 AI 对每个 standalone 源生成核心概括
  - AI 分析与推送展示解耦：无需开启独立展示区的推送显示，AI 也可独立分析完整热榜数据
  - 支持热榜平台和 RSS 源，含排名/时间/轨迹数据
  - 轨迹分析与 `include_rank_timeline` 联动：开启时利用轨迹数据做深度趋势分析，关闭时基于排名做简要判断
  - 新增 `standalone_summaries` JSON 字段（独立源点速览），所有推送渠道均已适配渲染


### 2026/01/28 - v5.5.0

> 和 mcp 功能一样, 这个小工具我也不新开一个仓库维护了, 反正纯前端, 都搁一起吧

- 增加 trendradar 的可视化配置编辑器


### 2026/02/02 - mcp-v3.2.0

- **新增 read_article 工具**：通过 Jina AI Reader 读取单篇文章正文（Markdown 格式）
- **新增 read_articles_batch 工具**：批量读取多篇文章（最多 5 篇，自动限速）
- **推荐工作流**：`search_news(query="关键词", include_url=True)` → `read_article(url=...)` 读取正文
- **文档更新**：README-MCP-FAQ.md 和 README-MCP-FAQ-EN.md 新增 Q19-Q20 文章读取相关说明


### 2026/01/10 - mcp-v3.0.0~v3.1.5

- **Breaking Change**：所有工具返回值统一为 `{success, summary, data, error}` 结构
- **异步一致性**：所有 21 个工具函数使用 `asyncio.to_thread()` 包装同步调用
- **MCP Resources**：新增 4 个资源（platforms、rss-feeds、available-dates、keywords）
- **RSS 增强**：`get_latest_rss` 支持多日查询（days 参数），跨日期 URL 去重
- **正则匹配修复**：`get_trending_topics` 支持 `/pattern/` 正则语法和 `display_name`
- **缓存优化**：新增 `make_cache_key()` 函数，参数排序+MD5 哈希确保一致性
- **新增 check_version 工具**：支持同时检查 TrendRadar 和 MCP Server 版本更新


### 2026/01/23 - v5.4.0

- 增加 AI 分析模式的独立控制功能，可选 follow_report | daily | current | incremental 
- 新增 AI 分析时间窗口控制，支持自定义运行段及每日频次限制
- 增加配置文件版本管理功能
- 修复若干bug


### 2026/01/19 - v5.3.0

> **重大重构：AI 模块迁移至 LiteLLM**

- **统一 AI 接口**：使用 LiteLLM 替代手动实现，支持 100+ AI 提供商
- **简化配置**：移除 `provider` 字段，改用 `model: "provider/model_name"` 格式
- **新增功能**：自动重试 (`num_retries`)、备用模型 (`fallback_models`)
- **配置变更**：
  - `ai.provider` → 移除（已合并到 model）
  - `ai.base_url` → `ai.api_base`
  - `AI_PROVIDER` 环境变量 → 移除
  - `AI_BASE_URL` 环境变量 → `AI_API_BASE`
- **模型格式示例**：
  - DeepSeek: `deepseek/deepseek-chat`
  - OpenAI: `openai/gpt-4o`
  - Gemini: `gemini/gemini-2.5-flash`
  - Anthropic: `anthropic/claude-3-5-sonnet`

### 2026/01/17 - v5.2.0

> 主要见 config.yaml 描述

**🌐 AI 翻译功能**

- **多语言翻译**：支持将推送内容翻译为任意语言
- **批量翻译**：智能批量处理，减少 API 调用次数
- **自定义提示词**：支持自定义翻译风格

**🔧 配置架构优化**

- **AI 模型配置独立**：分析和翻译共享模型配置
- **区域开关统一**：统一管理推送区域显示
- **区域排序自定义**：支持自定义各区域的显示顺序

**✨ AI 分析增强**

- **AI 分析嵌入 HTML**：分析结果直接嵌入 HTML 报告，邮件通知直接使用
- **富样式 AI 区块**：渐变蓝色背景卡片式布局，清晰分隔各分析维度
- **排名时间线支持**：AI 可获取每条新闻在每个抓取时间点的精确排名
- **板块重组 (7→4)**：整合为核心热点态势、舆论风向争议、异动与弱信号、研判策略建议

**🔧 多模型适配**

- **通用参数透传**：支持向 API 透传任意高级参数
- **Gemini 适配**：原生参数支持，内置安全策略放宽

**🐛 Bug 修复**

- 修复若干已知问题，提升系统稳定性

### 2026/01/10 - v5.0.0

> **开发小插曲**：
> 致敬那个陪伴我两年多、却在刚续费后反手弹出 `"This organization has been disabled"` 的某 C 厂模型

**✨ 推送内容"五大板块"重构**

本次更新对推送消息进行了区域化重构，现在推送内容清晰地划分为五大核心板块：

1.  **📊 热榜新闻**：根据你的关键词精准筛选后的全网热点聚合。
2.  **📰 RSS 订阅**：你的个性化订阅源内容，支持按关键词分组。
3.  **🆕 本次新增**：实时捕捉自上次运行以来的全新热点（带 🆕 标记）。
4.  **📋 独立展示区**：指定平台的完整热榜或 RSS 源展示，**完全不受关键词过滤限制**。
5.  **✨ AI 分析板块**：由 AI 驱动的深度洞察，包含趋势概述、热度走势及**极其重要**的情感倾向分析。

**✨ AI 智能分析推送功能**

- **AI 分析集成**：使用 AI 大模型对推送内容进行深度分析，自动生成热点趋势概述、关键词热度分析、跨平台关联、潜在影响评估等
- **情感倾向分析**：新增深度情感识别，精准捕捉舆论的正负面、争议或担忧情绪
- **多 AI 提供商支持**：支持 DeepSeek（默认，性价比高）、OpenAI、Google Gemini 及任意 OpenAI 兼容接口
- **两种推送模式**：`only_analysis`（仅 AI 分析）、`both`（两者都推送）
- **自定义提示词**：通过 `config/ai_analysis_prompt.txt` 文件自定义 AI 分析角色和输出格式
- **多维度数据分析**：AI 可分析排名变化、热度持续时间、跨平台表现、趋势预测等

**📋 独立展示区功能**

- **完整热榜展示**：指定平台的完整热榜单独展示，不受关键词过滤影响
- **RSS 独立展示**：RSS 源内容可完整展示，适合内容较少的订阅源
- **灵活配置**：支持配置展示平台列表、RSS 源列表、最大展示条数

**📊 推送体验重构**

- **排版升级**：重新设计并统一各渠道统计头部，强化区块组织，消息层次一目了然
- **配置简化**：优化飞书等通知渠道的配置逻辑，上手更简单
- **热度趋势箭头**：新增 🔺(上升)、🔻(下降)、➖(持平) 趋势标识，直观展示热度变化
- **通用 Webhook**：支持自定义 Webhook URL 和 JSON 模板，轻松适配 Discord、Matrix、IFTTT 等任意平台

**🔧 配置优化**

- **频率词配置增强**：新增 `[组别名]` 语法，支持 `#` 注释行，配置更清晰（感谢 [@songge8](https://github.com/sansan0/TrendRadar/issues/752) 提出的建议）
- **环境变量支持**：AI 分析相关配置支持环境变量覆盖（`AI_API_KEY`、`AI_PROVIDER` 等）

> 💡 详细配置教程见 [让 AI 帮我分析热点](#12-让-ai-帮我分析热点)


### 2026/01/02 - v4.7.0

- **修复 RSS HTML 显示**：修复 RSS 数据格式不匹配导致的渲染问题，现在按关键词分组正确显示
- **新增正则表达式语法**：关键词配置支持 `/pattern/` 正则语法，解决英文子字符串误匹配问题（如 `ai` 匹配 `training`）[📖 查看语法详解](#关键词基础语法)
- **新增显示名称语法**：使用 `=> 备注` 给复杂的正则表达式起个好记的名字，推送消息显示更清晰（如 `/\bai\b/ => AI相关`）
- **不会写正则？** README 新增 AI 生成正则的引导，告诉 ChatGPT/Gemini/DeepSeek 你想匹配什么，让 AI 帮你写


### 2025/12/30 - mcp-v2.0.0

- **架构调整**：移除 TXT 支持，统一使用 SQLite 数据库
- **RSS 查询**：新增 `get_latest_rss`、`search_rss`、`get_rss_feeds_status`
- **统一搜索**：`search_news` 支持 `include_rss` 参数同时搜索热榜和 RSS


### 2026/01/01 - v4.6.0

- **修复 RSS HTML 显示**：将 RSS 内容合并到热榜 HTML 页面，按源分组显示
- **新增 display_mode 配置**：支持 `keyword`（按关键词分组）和 `platform`（按平台分组）两种显示模式


### 2025/12/30 - v4.5.0

- **RSS 订阅源支持**：新增 RSS/Atom 抓取，按关键词分组统计（与热榜格式一致）
- **存储结构重构**：扁平化目录结构 `output/{type}/{date}.db`
- **统一排序配置**：`sort_by_position_first` 同时影响热榜和 RSS
- **配置结构重构**：`config.yaml` 重新组织为 7 个逻辑分组（app、report、notification、storage、platforms、rss、advanced），配置路径更清晰


### 2025/12/26 - mcp-v1.2.0

  **MCP 模块更新 - 优化工具集，新增聚合对比功能，合并冗余工具:**
  - 新增 `aggregate_news` 工具 - 跨平台新闻去重聚合
  - 新增 `compare_periods` 工具 - 时期对比分析（周环比/月环比）
  - 合并 `find_similar_news` + `search_related_news_history` → `find_related_news`
  - 增强 `get_trending_topics` - 新增 `auto_extract` 模式自动提取热点
  - 修复若干bug
  - 同步更新 README-MCP-FAQ.md 文档的中英文版 (Q1-Q18)


### 2025/12/20 - v4.0.3

- 新增 URL 标准化功能，解决微博等平台因动态参数（如 `band_rank`）导致的重复推送问题
- 修复增量模式检测逻辑，正确识别历史标题


### 2025/12/17 - v4.0.1

- StorageManager 添加推送记录代理方法
- S3 客户端切换至 virtual-hosted style 以提升兼容性（支持腾讯云 COS 等更多服务）


### 2025/12/13 - mcp-v1.1.0

  **MCP 模块更新:**
  - 适配 v4.0.0，同时也兼容 v3.x 的数据
  - 新增存储同步工具：`sync_from_remote`、`get_storage_status`、`list_available_dates`


### 2025/12/13 - v4.0.0

**🎉 重大更新：全面重构存储和核心架构**

- **多存储后端支持**：引入全新的存储模块，支持本地 SQLite 和远程云存储（S3 兼容协议，例如 Cloudflare R2），适应 GitHub Actions、Docker 和本地环境。
- **数据库结构优化**：重构 SQLite 数据库表结构，提升数据效率和查询能力。
- **核心代码模块化**：将主程序逻辑拆分为 trendradar 包的多个模块，显著提升代码可维护性。
- **增强功能**：实现日期格式标准化、数据保留策略、时区配置支持、时间显示优化，并修复远程存储数据持久化问题，确保数据合并的准确性。
- **清理和兼容**：移除了大部分历史兼容代码，统一了数据存储和读取方式。


### 2025/12/03 - v3.5.0

**🎉 核心功能增强**

1. **多账号推送支持**
   - 所有推送渠道（飞书、钉钉、企业微信、Telegram、ntfy、Bark、Slack）支持多账号配置
   - 使用分号 `;` 分隔多个账号，例如：`FEISHU_WEBHOOK_URL=url1;url2`
   - 自动验证配对配置（如 Telegram 的 token 和 chat_id）数量一致性

2. **推送区域配置**
   - 通过 `display.region_order` 自定义各区域的显示顺序（v5.2.0 替代原 `reverse_content_order`）
   - 通过 `display.regions` 控制各区域是否显示（热榜、新增热点、RSS、独立展示区、AI 分析）

3. **全局过滤关键词**
   - 新增 `[GLOBAL_FILTER]` 区域标记，支持全局过滤不想看到的内容
   - 适用场景：过滤广告、营销、低质内容等

**🐳 Docker 双路径 HTML 生成优化**

- **问题修复**：解决 Docker 环境下 `index.html` 无法同步到宿主机的问题
- **双路径生成**：当日汇总 HTML 同时生成到两个位置
  - `index.html`（项目根目录）：供 GitHub Pages 访问
  - `output/index.html`：通过 Docker Volume 挂载，宿主机可直接访问
- **兼容性**：确保 Docker、GitHub Actions、本地运行环境均能正常访问网页版报告

**🐳 Docker MCP 镜像支持**

- 新增独立的 MCP 服务镜像 `wantcat/trendradar-mcp`
- 支持 Docker 部署 AI 分析功能，通过 HTTP 接口（端口 3333）提供服务
- 双容器架构：新闻推送服务与 MCP 服务独立运行，可分别扩展和重启
- 详见 [Docker 部署 - MCP 服务](#6-docker-部署)

**🌐 Web 服务器支持**

- 新增内置 Web 服务器，支持通过浏览器访问生成的报告
- 通过 `manage.py` 命令控制启动/停止：`docker exec -it trendradar python manage.py start_webserver`
- 访问地址：`http://localhost:8080`（端口可配置）
- 安全特性：静态文件服务、目录限制、本地访问
- 支持自动启动和手动控制两种模式

**📖 文档优化**

- 新增 [推送内容怎么显示？](#7-推送内容怎么显示) 章节：自定义推送样式和内容
- 新增 [什么时候给我推送？](#8-什么时候给我推送) 章节：设置推送时间段
- 新增 [多久运行一次？](#9-多久运行一次) 章节：设置自动运行频率
- 新增 [推送到多个群/设备](#10-推送到多个群设备) 章节：同时推送给多个接收者
- 优化各配置章节：统一添加"配置位置"说明
- 简化快速开始配置说明：三个核心文件一目了然
- 优化 [Docker 部署](#6-docker-部署) 章节：新增镜像说明、推荐 git clone 部署、重组部署方式

**🔧 升级说明**：
- **GitHub Fork 用户**：更新 `main.py`、`config/config.yaml`（新增多账号推送支持，无需修改现有配置）
- **多账号推送**：新功能，默认不启用，现有单账号配置不受影响


### 2025/11/26 - mcp-v1.0.3

  **MCP 模块更新:**
  - 新增日期解析工具 resolve_date_range,解决 AI 模型计算日期不一致的问题
  - 支持自然语言日期表达式解析(本周、最近7天、上月等)
  - 工具总数从 13 个增加到 14 个


### 2025/11/28 - v3.4.1

**🔧 格式优化**

1. **Bark 推送增强**
   - Bark 现支持 Markdown 渲染
   - 启用原生 Markdown 格式：粗体、链接、列表、代码块等
   - 移除纯文本转换，充分利用 Bark 原生渲染能力

2. **Slack 格式精准化**
   - 使用专用 mrkdwn 格式处理分批内容
   - 提升字节大小估算准确性（避免消息超限）
   - 优化链接格式：`<url|text>` 和加粗语法：`*text*`

3. **性能提升**
   - 格式转换在分批过程中完成，避免二次处理
   - 准确估算消息大小，减少发送失败率

**🔧 升级说明**：
- **GitHub Fork 用户**：更新 `main.py`，`config.yaml`


### 2025/11/25 - v3.4.0

**🎉 新增 Slack 推送支持**

1. **团队协作推送渠道**
   - 支持 Slack Incoming Webhooks（全球流行的团队协作工具）
   - 消息集中管理，适合团队共享热点资讯
   - 支持 mrkdwn 格式（粗体、链接等）

2. **多种部署方式**
   - GitHub Actions：配置 `SLACK_WEBHOOK_URL` Secret
   - Docker：环境变量 `SLACK_WEBHOOK_URL`
   - 本地运行：`config/config.yaml` 配置文件


> 📖 **详细配置教程**：[快速开始 - Slack 推送](#-快速开始)

- 优化 setup-windows.bat 和 setup-windows-en.bat 一键安装 MCP 的体验

**🔧 升级说明**：
- **GitHub Fork 用户**：更新 `main.py`、`config/config.yaml`、`.github/workflows/crawler.yml`


### 2025/11/24 - v3.3.0

**🎉 新增 Bark 推送支持**

1. **iOS 专属推送渠道**
   - 支持 Bark 推送（基于 APNs，iOS 平台）
   - 免费开源，简洁高效，无广告干扰
   - 支持官方服务器和自建服务器两种方式

2. **多种部署方式**
   - GitHub Actions：配置 `BARK_URL` Secret
   - Docker：环境变量 `BARK_URL`
   - 本地运行：`config/config.yaml` 配置文件

> 📖 **详细配置教程**：[快速开始 - Bark 推送](#-快速开始)

**🐛 Bug 修复**
- 修复 `config.yaml` 中 `ntfy_server_url` 配置不生效的问题 ([#345](https://github.com/sansan0/TrendRadar/issues/345))

**🔧 升级说明**：
- **GitHub Fork 用户**：更新 `main.py`、`config/config.yaml`、`.github/workflows/crawler.yml`

### 2025/11/23 - v3.2.0

**🎯 新增高级定制功能**

1. **关键词排序优先级配置**
   - 支持两种排序策略：热度优先 vs 配置顺序优先
   - 满足不同使用场景：热点追踪 or 个性化关注

2. **显示数量精准控制**
   - 全局配置：统一限制所有关键词显示数量
   - 单独配置：使用 `@数字` 语法为特定关键词设置限制
   - 有效控制推送长度，突出重点内容

> 📖 **详细配置教程**：[关键词配置 - 高级配置](#关键词高级配置)

**🔧 升级说明**：
- **GitHub Fork 用户**：更新 `main.py`、`config/config.yaml`


### 2025/11/18 - mcp-v1.0.2

  **MCP 模块更新:**
  - 优化查询今日新闻却可能错误返回过去日期的情况


### 2025/11/22 - v3.1.1

- **修复数据异常导致的崩溃问题**：解决部分用户在 GitHub Actions 环境中遇到的 `'float' object has no attribute 'lower'` 错误
- 新增双重防护机制：在数据获取阶段过滤无效标题（None、float、空字符串），同时在函数调用处添加类型检查
- 提升系统稳定性，确保在数据源返回异常格式时仍能正常运行

**升级说明**（GitHub Fork 用户）：
- 必须更新：`main.py`
- 建议使用小版本升级方式：复制替换上述文件


### 2025/11/20 - v3.1.0

- **新增个人微信推送支持**：企业微信应用可推送到个人微信，无需安装企业微信 APP
- 支持两种消息格式：`markdown`（企业微信群机器人）和 `text`（个人微信应用）
- 新增 `WEWORK_MSG_TYPE` 环境变量配置，支持 GitHub Actions、Docker、docker compose 等多种部署方式
- `text` 模式自动清除 Markdown 语法，提供纯文本推送效果
- 详见快速开始中的「个人微信推送」配置说明

**升级说明**（GitHub Fork 用户）：
- 必须更新：`main.py`、`config/config.yaml`
- 可选更新：`.github/workflows/crawler.yml`（如使用 GitHub Actions 部署）
- 建议使用小版本升级方式：复制替换上述文件

### 2025/11/12 - v3.0.5

- 修复邮件发送 SSL/TLS 端口配置逻辑错误
- 优化邮箱服务商（QQ/163/126）默认使用 465 端口（SSL）
- **新增 Docker 环境变量支持**：核心配置项（`enable_crawler`、`report_mode`、`push_window` 等）支持通过环境变量覆盖，解决 NAS 用户修改配置文件不生效的问题（详见 [🐳 Docker 部署](#-docker-部署) 章节）


### 2025/10/26 - mcp-v1.0.1

  **MCP 模块更新:**
  - 修复日期查询参数传递错误
  - 统一所有工具的时间参数格式


### 2025/10/31 - v3.0.4

- 解决飞书因推送内容过长而产生的错误，实现了分批推送


### 2025/10/23 - v3.0.3

- 扩大 ntfy 错误信息显示范围


### 2025/10/21 - v3.0.2

- 修复 ntfy 推送编码问题

### 2025/10/20 - v3.0.0

**重大更新 - AI 分析功能上线** ✨

- **核心功能**：
  - 新增基于 MCP (Model Context Protocol) 的 AI 分析服务器
  - 支持17种智能分析工具：基础查询、智能检索、高级分析、RSS 查询、系统管理
  - 自然语言交互：通过对话方式查询和分析新闻数据
  - 多客户端支持：Claude Desktop、Cherry Studio、Cursor、Cline 等

- **分析能力**：
  - 话题趋势分析（热度追踪、生命周期、爆火检测、趋势预测）
  - 数据洞察（平台对比、活跃度统计、关键词共现）
  - 情感分析、相似新闻查找、智能摘要生成
  - 历史相关新闻检索、多模式搜索

- **更新提示**：
  - 这是独立的 AI 分析功能，不影响现有的推送功能
  - 可选择性使用，无需升级现有部署


### 2025/10/15 - v2.4.4

- **更新内容**：
    - 修复 ntfy 推送编码问题 + 1
    - 修复推送时间窗口判断问题

- **更新提示**：
  - 建议【小版本升级】


### 2025/10/10 - v2.4.3

> 感谢 [nidaye996](https://github.com/sansan0/TrendRadar/issues/98) 发现的体验问题

- **更新内容**：
    - 重构"静默推送模式"命名为"推送时间窗口控制"，提升功能理解度
    - 明确推送时间窗口作为可选附加功能，可与三种推送模式搭配使用
    - 改进注释和文档描述，使功能定位更加清晰

- **更新提示**：
  - 这个仅仅是重构，可以不用升级


### 2025/10/8 - v2.4.2

- **更新内容**：
    - 修复 ntfy 推送编码问题
    - 修复配置文件缺失问题
    - 优化 ntfy 推送效果
    - 增加 github page 图片分段导出功能

- **更新提示**：
  - 建议使用【大版本更新】


### 2025/10/2 - v2.4.0

**新增 ntfy 推送通知**

- **核心功能**：
  - 支持 ntfy.sh 公共服务和自托管服务器

- **使用场景**：
  - 适合追求隐私的用户（支持自托管）
  - 跨平台推送（iOS、Android、Desktop、Web）
  - 无需注册账号（公共服务器）
  - 开源免费（MIT 协议）

- **更新提示**：
  - 建议使用【大版本更新】


### 2025/09/26 - v2.3.2

- 修正了邮件通知配置检查被遗漏的问题（[#88](https://github.com/sansan0/TrendRadar/issues/88)）

**修复说明**：
- 解决了即使正确配置邮件通知，系统仍提示"未配置任何webhook"的问题

### 2025/09/22 - v2.3.1

- **新增邮件推送功能**，支持将热点新闻报告发送到邮箱
- **智能 SMTP 识别**：自动识别 Gmail、QQ邮箱、Outlook、网易邮箱等 10+ 种邮箱服务商配置
- **HTML 精美格式**：邮件内容采用与网页版相同的 HTML 格式，排版精美，移动端适配
- **批量发送支持**：支持多个收件人，用逗号分隔即可同时发送给多人
- **自定义 SMTP**：可自定义 SMTP 服务器和端口
- 修复Docker构建网络连接问题

**使用说明**：
- 适用场景：适合需要邮件归档、团队分享、定时报告的用户
- 支持邮箱：Gmail、QQ邮箱、Outlook/Hotmail、163/126邮箱、新浪邮箱、搜狐邮箱等

**更新提示**：
- 此次更新的内容比较多，如果想升级，建议采用【大版本升级】

### 2025/09/17 - v2.2.0

- 新增一键保存新闻图片功能，让你轻松分享关注的热点

**使用说明**：
- 适用场景：当你按照教程开启了网页版功能后(GitHub Pages)
- 使用方法：用手机或电脑打开该网页链接，点击页面顶部的"保存为图片"按钮
- 实际效果：系统会自动将当前的新闻报告制作成一张精美图片，保存到你的手机相册或电脑桌面
- 分享便利：你可以直接把这张图片发给朋友、发到朋友圈，或分享到工作群，让别人也能看到你发现的重要资讯

### 2025/09/13 - v2.1.2

- 解决钉钉的推送容量限制导致的新闻推送失败问题(采用分批推送)

### 2025/09/04 - v2.1.1

- 修复docker在某些架构中无法正常运行的问题
- 正式发布官方 Docker 镜像 wantcat/trendradar，支持多架构
- 优化 Docker 部署流程，无需本地构建即可快速使用

### 2025/08/30 - v2.1.0

**核心改进**：
- **推送逻辑优化**：从"每次执行都推送"改为"时间窗口内可控推送"
- **时间窗口控制**：可设定推送时间范围，避免非工作时间打扰
- **推送频率可选**：时间段内支持单次推送或多次推送

**更新提示**：
- 本功能默认关闭，需手动在 config.yaml 中开启推送时间窗口控制
- 升级需同时更新 main.py 和 config.yaml 两个文件

### 2025/08/27 - v2.0.4

- 本次版本不是功能修复，而是重要提醒
- 请务必妥善保管好 webhooks，不要公开，不要公开，不要公开
- 如果你以 fork 的方式将本项目部署在 GitHub 上，请将 webhooks 填入 GitHub Secret，而非 config.yaml
- 如果你已经暴露了 webhooks 或将其填入了 config.yaml，建议删除后重新生成

### 2025/08/06 - v2.0.3

- 优化 github page 的网页版效果，方便移动端使用

### 2025/07/28 - v2.0.2

- 重构代码
- 解决版本号容易被遗漏修改的问题

### 2025/07/27 - v2.0.1

**修复问题**: 

1. docker 的 shell 脚本的换行符为 CRLF 导致的执行异常问题
2. frequency_words.txt 为空时，导致新闻发送也为空的逻辑问题
  - 修复后，当你选择 frequency_words.txt 为空时，将**推送所有新闻**，但受限于消息推送大小限制，请做如下调整
    - 方案一：关闭手机推送，只选择 Github Pages 布置(这是能获得最完整信息的方案，将把所有平台的热点按照你**自定义的热搜算法**进行重新排序)
    - 方案二：减少推送平台，优先选择**企业微信**或**Telegram**，这两个推送我做了分批推送功能(因为分批推送影响推送体验，且只有这两个平台只给一点点推送容量，所以才不得已做了分批推送功能，但至少能保证获得的信息完整)
    - 方案三：可与方案二结合，模式选择 current 或 incremental 可有效减少一次性推送的内容 

### 2025/07/17 - v2.0.0

**重大重构**：
- 配置管理重构：所有配置现在通过 `config/config.yaml` 文件管理（main.py 我依旧没拆分，方便你们复制升级）
- 运行模式升级：支持三种模式 - `daily`（当日汇总）、`current`（当前榜单）、`incremental`（增量监控）
- Docker 支持：完整的 Docker 部署方案，支持容器化运行

**配置文件说明**：
- `config/config.yaml` - 主配置文件（应用设置、爬虫配置、通知配置、平台配置等）
- `config/frequency_words.txt` - 关键词配置（监控词汇设置）

### 2025/07/09 - v1.4.1

**功能新增**：增加增量推送(在 main.py 头部配置 FOCUS_NEW_ONLY)，该开关只关心新话题而非持续热度，只在有新内容时才发通知。

**修复问题**: 某些情况下，由于新闻本身含有特殊符号导致的偶发性排版异常。

### 2025/06/23 - v1.3.0

企业微信 和 Telegram 的推送消息有长度限制，对此我采用将消息拆分推送的方式。开发文档详见[企业微信](https://developer.work.weixin.qq.com/document/path/91770) 和 [Telegram](https://core.telegram.org/bots/api)

### 2025/06/21 - v1.2.1

在本版本之前的旧版本，不仅 main.py 需要复制替换， crawler.yml 也需要你复制替换
https://github.com/sansan0/TrendRadar/blob/master/.github/workflows/crawler.yml

### 2025/06/19 - v1.2.0

> 感谢 claude research 整理的各平台 api ,让我快速完成各平台适配（虽然代码更多冗余了~

1. 支持 telegram ，企业微信，钉钉推送渠道, 支持多渠道配置和同时推送

### 2025/06/18 - v1.1.0

> **200 star⭐** 了, 继续给大伙儿助兴~近期，在我的"怂恿"下，挺多人在我公众号点赞分享推荐助力了我，我都在后台看见了具体账号的鼓励数据，很多都成了天使轮老粉（我玩公众号才一个多月，虽然注册是七八年前的事了哈哈，属于上车早，发车晚），但因为你们没有留言或私信我，所以我也无法一一回应并感谢支持，在此一并谢谢！

1. 重要的更新，加了权重，你现在看到的新闻都是最热点最有关注度的出现在最上面
2. 更新文档使用，因为近期更新了很多功能，而且之前的使用文档我偷懒写的简单（见下面的 ⚙️ frequency_words.txt 配置完整教程）

### 2025/06/16 - v1.0.0

1. 增加了一个项目新版本更新提示，默认打开，如要关掉，可以在 main.py 中把 "FEISHU_SHOW_VERSION_UPDATE": True 中的 True 改成 False 即可

### 2025/06/13+14

1. 去掉了兼容代码，之前 fork 的同学，直接复制代码会在当天显示异常（第二天会恢复正常）
2. feishu 和 html 底部增加一个新增新闻显示

### 2025/06/09

**100 star⭐** 了，写个小功能给大伙儿助助兴
frequency_words.txt 文件增加了一个【必须词】功能，使用 + 号

1. 必须词语法如下：  
   唐僧或者猪八戒必须在标题里同时出现，才会收录到推送新闻中

```
+唐僧
+猪八戒
```

2. 过滤词的优先级更高：  
   如果标题中过滤词匹配到唐僧念经，那么即使必须词里有唐僧，也不显示

```
+唐僧
!唐僧念经
```

### 2025/06/02

1. **网页**和**飞书消息**支持手机直接跳转详情新闻
2. 优化显示效果 + 1

### 2025/05/26

1. 飞书消息显示效果优化

<table>
<tr>
<td align="center">
优化前<br>
<img src="_image/before.jpg" alt="飞书消息界面 - 优化前" width="400"/>
</td>
<td align="center">
优化后<br>
<img src="_image/after.jpg" alt="飞书消息界面 - 优化后" width="400"/>
</td>
</tr>
</table>

</details>

<br>

## ✨ 核心功能

### **全网热点聚合**

- 知乎
- 抖音
- bilibili 热搜
- 华尔街见闻
- 贴吧
- 百度热搜
- 财联社热门
- 澎湃新闻
- 凤凰网
- 今日头条
- 微博

默认监控 11 个主流平台，也可自行增加额外的平台

> 💡 详细配置教程见 [配置详解 - 平台配置](#1-平台配置)

### **RSS 订阅源支持**（v4.5.0 新增）

支持 RSS/Atom 订阅源抓取，按关键词分组统计（与热榜格式一致）：

- **统一格式**：RSS 与热榜使用相同的关键词匹配和显示格式
- **简单配置**：直接在 `config.yaml` 中添加 RSS 源
- **合并推送**：热榜和 RSS 合并为一条消息推送
- **新鲜度过滤**：自动过滤超过指定天数的旧文章，避免重复推送。支持全局默认天数和单源独立设置

> 💡 RSS 使用与热榜相同的 `frequency_words.txt` 进行关键词过滤

### **可视化配置编辑器**

提供基于 Web 的图形化配置界面，无需手动编辑 YAML 文件，通过表单即可完成所有配置项的修改与导出。

支持中英文界面切换和英文配置模板，方便按熟悉的语言设置运行参数、关键词和调度规则。

👉 **在线体验**：[https://sansan0.github.io/TrendRadar/](https://sansan0.github.io/TrendRadar/)

<img src="/_image/editor.png" alt="可视化配置编辑器" width="80%">

### **智能推送策略**

**三种推送模式**：

| 模式 | 适用场景 | 推送特点 |
|------|---------|---------|
| **当日汇总** (daily) | 企业管理者/普通用户 | 按时推送当日所有匹配新闻（会包含之前推送过的） |
| **当前榜单** (current) | 自媒体人/内容创作者 | 按时推送当前榜单匹配新闻（持续在榜的每次都出现） |
| **增量监控** (incremental) | 投资者/交易员 | 仅推送新增内容，零重复 |

> 💡 **快速选择指南：**
> - 不想看到重复新闻 → 用 `incremental`（增量监控）
> - 想看完整榜单趋势 → 用 `current`（当前榜单）
> - 需要每日汇总报告 → 用 `daily`（当日汇总）
>
> 详细对比和配置教程见 [配置详解 - 推送模式详解](#3-推送模式详解)

**附加功能**（可选）：

| 功能 | 说明 | 默认 |
|------|------|------|
| **调度系统** | 按周一到周日逐日编排：为每天分配不同时间段、推送模式和 AI 分析策略。**每个时段可独立设置筛选方式（关键词/AI）和关注方向**，实现不同时间看不同类型新闻。内置 5 种预设（always_on / morning_evening / office_hours / night_owl / custom），也可自定义。支持工作日/周末差异化、跨午夜时段、per-period 去重、时段冲突检测（v6.0.0 + v6.5.0） | morning_evening |
| **内容顺序配置** | 通过 `display.region_order` 调整各区域（热榜、新增热点、RSS、独立展示区、AI 分析）的显示顺序；通过 `display.regions` 控制各区域是否显示（v5.2.0） | 见配置文件 |
| **显示模式切换** | `keyword`=按关键词分组，`platform`=按平台分组（v4.6.0 新增） | keyword |

> 💡 详细配置教程见 [推送内容怎么显示？](#7-推送内容怎么显示) 和 [什么时候给我推送？](#8-什么时候给我推送)

### **精准内容筛选**

设置个人关键词（如：AI、比亚迪、教育政策），只推送相关热点，过滤无关信息

> 💡 **基础配置教程**：[关键词配置 - 基础语法](#关键词基础语法)
>
> 💡 **高级配置教程**：[关键词配置 - 高级配置](#关键词高级配置)
>
> 💡 也可以不做筛选，完整推送所有热点（将 frequency_words.txt 留空）

### **AI 智能筛选新闻**（v6.5.0 新增）

用自然语言描述你的兴趣，AI 自动分类新闻，替代传统关键词匹配

- **自然语言兴趣描述**：在 `ai_interests.txt` 中用日常语言写下关注方向，无需学习关键词语法
- **两阶段智能处理**：AI 先从兴趣描述提取结构化标签，再对新闻按标签批量分类打分
- **分数阈值控制**：通过 `ai_filter.min_score` 精确控制推送质量，只推送高相关度新闻
- **自动回退保障**：AI 筛选失败时自动回退到关键词匹配，确保推送不中断
- **智能标签更新**：兴趣变更时 AI 自动评估变化幅度，决定增量或全量重分类
- **灵活切换**：`filter.method` 支持 `keyword`（默认）和 `ai` 两种模式，Timeline 可按时段覆盖
- **分时段个性化**：不同时间段可以使用不同的关键词文件或 AI 兴趣描述。例如早上用"科技词库"快速过滤，晚上换成"金融兴趣"做 AI 深度筛选

```yaml
# config.yaml 快速启用示例
filter:
  method: ai          # keyword（默认）| ai
ai_filter:
  min_score: 6         # 推送最低分数阈值（1-10）
```

> 💡 AI 筛选与 AI 分析/翻译共享模型配置，只需配置一次 `ai.api_key`

### **热点趋势分析**

实时追踪新闻热度变化，让你不仅知道"什么在热搜"，更了解"热点如何演变"

- **时间轴追踪**：记录每条新闻从首次出现到最后出现的完整时间跨度
- **热度变化**：统计新闻在不同时间段的排名变化和出现频次
- **新增检测**：实时识别新出现的热点话题，用🆕标记第一时间提醒
- **持续性分析**：区分一次性热点话题和持续发酵的深度新闻
- **跨平台对比**：同一新闻在不同平台的排名表现，看出媒体关注度差异

> 💡 推送格式说明见 [消息样式说明](#5-我收到的消息长什么样)

### **个性化热点算法**

不再被各个平台的算法牵着走，TrendRadar 会重新整理全网热搜

> 💡 三个比例可以调整，详见 [配置详解 - 热点权重调整](#4-热点权重调整)

### **多渠道多账号推送**

支持**企业微信**(+ 微信推送方案)、**飞书**、**钉钉**、**Telegram**、**邮件**、**ntfy**、**Bark**、**Slack**、**通用 Webhook**（可对接 Discord、IFTTT 等任意平台），消息直达手机和邮箱

> 💡 详细配置教程见 [推送到多个群/设备](#10-推送到多个群设备)

### **AI 多语言翻译**（v5.2.0 新增）

将推送内容翻译为任意语言，打破语言壁垒，无论是阅读国内热点还是通过 RSS 订阅海外资讯，都能以母语轻松获取

- **一键翻译**：在 `config.yaml` 中设置 `ai_translation.enabled: true` 和目标语言即可
- **多语言支持**：支持 English、Korean、Japanese、French 等任意语言
- **智能批量处理**：自动批量翻译，减少 API 调用次数，节省成本
- **自定义风格**：通过 `ai_translation_prompt.txt` 自定义翻译风格和术语
- **共享模型配置**：与 AI 分析功能共用 `ai` 配置段的模型设置

```yaml
# config.yaml 快速启用示例
ai_translation:
  enabled: true
  language: "English"  # 翻译目标语言
```

> 💡 翻译功能与 AI 分析功能共享模型配置，只需配置一次 `ai.api_key` 即可同时使用两个功能

**RSS 源参考**：以下是一些 RSS 订阅源合集，可按需选用
- [awesome-tech-rss](https://github.com/tuan3w/awesome-tech-rss) - 科技、创业、编程领域博客和媒体
- [awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) - 世界各国主流新闻媒体 RSS 合集

> ⚠️ 部分海外媒体内容可能涉及敏感话题，AI 模型可能拒绝翻译，建议根据实际需求筛选订阅源

### **HTML 报告浏览器增强**（v6.6.0 新增）

在浏览器中打开推送的 HTML 报告，自动解锁增强体验（邮件客户端不受影响）：

- **宽屏模式**：桌面端自动切换 1200px 宽屏布局，充分利用屏幕空间
- **Tab 快速切换**：关键词分组和独立展区均支持 Tab 导航，告别长页面翻滚
- **暗色模式**：一键切换深色主题，自动记住偏好
- **实时搜索**：按 `/` 唤起搜索框，即时过滤新闻标题
- **一键复制**：悬停新闻序号即可复制标题和链接
- **快捷键**：`W` 宽屏、`D` 暗色、`/` 搜索、`?` 查看所有快捷键

> 💡 所有增强功能基于渐进增强，邮件客户端仍显示原始 600px 布局，零回归

### **灵活存储架构**（v4.0.0 重大更新）

**多存储后端支持**：
- **远程云存储**：GitHub Actions 环境默认，支持 S3 兼容协议（R2/OSS/COS 等），数据存储在云端，不污染仓库
- **本地 SQLite 数据库**：Docker/本地环境默认，数据完全可控
- **自动后端选择**：根据运行环境智能切换存储方式

> 💡 详细说明见 [数据保存在哪里？](#11-数据保存在哪里)

### **多端部署**
- **GitHub Actions**：定时自动爬取 + 远程云存储（需签到续期）
- **Docker 部署**：支持多架构容器化运行，数据本地存储
- **本地运行**：Windows/Mac/Linux 直接运行


### **AI 分析推送（v5.0.0 新增）**

使用 AI 大模型对推送内容进行深度分析，自动生成热点洞察报告

- **智能分析**：自动分析热点趋势、关键词热度、跨平台关联、潜在影响
- **多提供商**：基于 LiteLLM 统一接口，支持 100+ AI 提供商（DeepSeek、OpenAI、Gemini、Anthropic、本地 Ollama 等），还支持备用模型自动切换
- **分析模式独立**：AI 的分析范围可以和推送不同——推送只发新增消息（避免打扰），但 AI 可以分析当天全部新闻（看完整趋势）
- **灵活推送**：可选仅原始内容、仅 AI 分析、或两者都推送
- **自定义提示词**：通过 `config/ai_analysis_prompt.txt` 自定义分析角度

> 💡 详细配置教程见 [让 AI 帮我分析热点](#12-让-ai-帮我分析热点)

### **独立展示区（v5.0.0 新增）**

为指定平台提供完整热榜展示，不受关键词过滤影响

- **完整热榜**：指定平台的热榜完整展示，适合想看完整排名的用户
- **RSS 独立展示**：RSS 源内容可完整展示，不受关键词限制
- **AI 深度分析**：可独立开启 AI 对完整热榜的趋势分析，无需在推送中展示
- **灵活配置**：支持配置展示平台、RSS 源、最大条数

> 💡 详细配置教程见 [推送内容怎么显示？ - 独立展示区](#7-推送内容怎么显示)

### **AI 智能分析（v3.0.0 新增）**

基于 MCP (Model Context Protocol) 协议的 AI 对话分析系统，让你用自然语言深度挖掘新闻数据

> **💡 使用提示**：AI 功能需要本地新闻数据支持
> - 项目自带测试数据，可立即体验功能
> - 建议自行部署运行项目，获取更实时的数据
>
> 详见 [AI 智能分析](#-ai-智能分析)

### **网页部署**

运行后根目录生成 `index.html`，即为完整的新闻报告页面。

> **部署方式**：点击 **Use this template** 创建仓库，可部署到 Cloudflare Pages 或 GitHub Pages 等静态托管平台。
>
> **💡 提示**：启用 GitHub Pages 可获得在线访问地址，进入仓库 Settings → Pages 即可开启。[效果预览](https://sansan0.github.io/TrendRadar/)
>
> ⚠️ 原 GitHub Actions 自动存储功能已下线（该方案曾导致 GitHub 服务器负载过高，影响平台稳定性）。

<a id="cloudflare-deploy"></a>

### ☁️ 自动部署到 Cloudflare Pages（可选 · 国内访问更快）

GitHub Pages 在国内访问较慢，[Cloudflare Pages](https://pages.cloudflare.com/) 的访问速度更友好。配置完成后，GitHub Actions 每次运行都会自动把最新的 `index.html` 推送到 Cloudflare Pages，无需任何手动操作。

> **前置条件**：已完成 [GitHub Actions 部署](#-快速开始) 并能正常生成网页报告。

**① 创建 Cloudflare Pages 项目**

登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Create** → **Pages** → 选择 **Upload assets（直接上传）**，填写一个项目名称（例如 `trendradar`，请记住它），随意上传一个文件完成首次创建（后续会被 Actions 自动覆盖）。

**② 获取 API Token 与 Account ID**

- **API Token**：右上角头像 → **My Profile** → **API Tokens** → **Create Token** → **Create Custom Token**，权限选择 `Account` → `Cloudflare Pages` → `Edit`，创建后复制 Token（仅显示一次）。
- **Account ID**：在 **Workers & Pages** 页面右侧栏即可找到（或任意域名 **Overview** 页面右下角）。

**③ 在 GitHub 仓库添加 3 个 Secrets**

进入仓库 `Settings` → `Secrets and variables` → `Actions` → `New repository secret`，依次添加：

| Name（名称） | Secret（值） |
|:---|:---|
| `CLOUDFLARE_API_TOKEN` | 上一步创建的 API Token |
| `CLOUDFLARE_ACCOUNT_ID` | 你的 Cloudflare Account ID |
| `CLOUDFLARE_PROJECT_NAME` | Cloudflare Pages 项目名（如 `trendradar`） |

配置完成后，下一次 GitHub Actions 运行即会自动部署，访问地址为 `https://<项目名>.pages.dev`。

> 💡 **说明**：三个 Secret 缺任意一个都会自动跳过 Cloudflare 部署，不会影响新闻推送等其它功能；如需绑定自定义域名，可在 Pages 项目的 **Custom domains** 中设置。

### **减少 APP 依赖**

从"被算法推荐绑架"变成"主动获取自己想要的信息"

**适合人群：** 投资者、自媒体人、企业公关、关心时事的普通用户

**典型场景：** 股市投资监控、品牌舆情追踪、行业动态关注、生活资讯获取


| 网页效果(邮箱推送效果) | 飞书推送效果 | AI 分析推送效果 |
|:---:|:---:|:---:|
| ![网页效果](_image/github-pages.png) | ![飞书推送效果](_image/feishu.jpg) | ![AI分析推送效果](_image/ai.jpg) |


<br>

## 🚀 快速开始

> **提醒**：建议先 **[查看最新官方文档](https://github.com/sansan0/TrendRadar?tab=readme-ov-file)**，确保配置步骤是最新的。

### 请选择适合你的部署方式

#### Ⓐ 方案一：Docker 部署（推荐 🔥）

* **特点**：比 GitHub Actions 更稳定，数据本地存储（无需配置云存储）
* **适用**：有自己的服务器、NAS 或长期运行的电脑
* **注意**：你需要阅读了解下方的基础配置流程，然后跳转到 Docker 教程进行部署。

#### Ⓑ 方案二：GitHub Actions 部署（本章节内容 ⬇️）

* **特点**：无服务器，数据存储在 **远程云存储**（推荐配置）
* **适用**：没有服务器的用户，利用 GitHub 免费资源
* **注意**：需配置云存储以获得完整体验，且需定期签到续期

<a id="local-deploy"></a>

#### Ⓒ 方案三：本地部署（uv）

* **特点**：直接在本机运行，无需 Docker，适合开发调试或无 Docker 环境的用户
* **适用**：Windows / Mac / Linux 用户（无需预装 Python，uv 会自动管理）
* **步骤**：

   **1. 安装 uv**（如已安装可跳过，无需预装 Python）

   ```bash
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   **2. 克隆并运行**

   ```bash
   git clone https://github.com/sansan0/TrendRadar.git
   cd TrendRadar
   uv sync          # 自动安装 Python 和项目依赖
   uv run python -m trendradar
   ```

   > 💡 **提示**：
   > - uv 会自动管理 Python 版本，无需手动安装 Python
   > - Windows 用户也可以双击 `setup-windows.bat` 一键安装依赖
   > - Mac 用户可使用 `bash setup-mac.sh`
   > - 运行前请先编辑 `config/config.yaml` 填写推送渠道等配置，参考下方的基础配置流程

### 1️⃣ 第一步：获取项目代码

   点击本仓库页面右上角的绿色 **[Use this template]** 按钮 → 选择 "Create a new repository"。

   > ⚠️ 提醒：
   > - 后续文档中提到的 "Fork" 均可理解为 "Use this template"
   > - 使用 Fork 可能导致运行异常，详见 [Issue #606](https://github.com/sansan0/TrendRadar/issues/606)

   <br>

### 2️⃣ 第二步：设置 GitHub Secrets

   在你 Fork 后的仓库中，进入 `Settings` > `Secrets and variables` > `Actions` > `New repository secret`

   **📌 重要说明（请务必仔细阅读）：**

   - **一个 Name 对应一个 Secret**：每添加一个配置项，点击一次"New repository secret"按钮，填写一对"Name"和"Secret"
   - **保存后看不到值是正常的**：出于安全考虑，保存后重新编辑时，只能看到 Name（名称），看不到 Secret（值）的内容
   - **严禁自创名称**：Secret 的 Name（名称）必须**严格使用**下方列出的名称（如 `WEWORK_WEBHOOK_URL`、`FEISHU_WEBHOOK_URL` 等），不能自己随意修改或创造新名称，否则系统无法识别
   - **可以同时配置多个平台**：系统会向所有配置的平台发送通知

   **配置示例：**

   <img src="_image/secrets.png" alt="GitHub Secrets 配置示例"/>

   如上图所示，每一行是一个配置项：
   - **Name（名称）**：必须使用下方展开内容中列出的固定名称（如 `WEWORK_WEBHOOK_URL`）
   - **Secret（值）**：填写你从对应平台获取的实际内容（如 Webhook 地址、Token 等）

   <br>

   <details>
   <summary>👉 点击展开：<strong>企业微信机器人</strong>（配置最简单最迅速）</summary>
   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`WEWORK_WEBHOOK_URL`（请复制粘贴此名称，不要手打，避免打错）
   - **Secret（值）**：你的企业微信机器人 Webhook 地址

   <br>

   **机器人设置步骤：**

   #### 手机端设置：
   1. 打开企业微信 App → 进入目标内部群聊
   2. 点击右上角"…"按钮 → 选择"消息推送"
   3. 点击"添加" → 名称输入"TrendRadar"
   4. 复制 Webhook 地址，点击保存，复制的内容配置到上方的 GitHub Secret 中

   #### PC 端设置流程类似
   </details>

   <details>
   <summary>👉 点击展开：<strong>个人微信推送</strong>（基于企业微信应用，推送到个人微信）</summary>
   <br>

   > 由于该方案是基于企业微信的插件机制，推送样式为纯文本（无 markdown 格式），但可以直接推送到个人微信，无需安装企业微信 App。

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`WEWORK_WEBHOOK_URL`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的企业微信应用 Webhook 地址

   - **Name（名称）**：`WEWORK_MSG_TYPE`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：`text`

   <br>

   **设置步骤：**

   1. 完成上方的企业微信机器人 Webhook 设置
   2. 添加 `WEWORK_MSG_TYPE` Secret，值设为 `text`
   3. 按照下面图片操作，关联个人微信
   4. 配置好后，手机上的企业微信 App 可以删除

   <img src="_image/wework.png" title="个人微信推送配置"/>

   **说明**：
   - 与企业微信机器人使用相同的 Webhook 地址
   - 区别在于消息格式：`text` 为纯文本，`markdown` 为富文本（默认）
   - 纯文本格式会自动去除所有 markdown 语法（粗体、链接等）

   </details>

   <details>
   <summary>👉 点击展开：<strong>飞书机器人</strong>（消息显示相对友好）</summary>
   <br>

   > **注意**：原「飞书机器人助手 (BotBuilder)」将于 2026 年 6 月 30 日下线，请使用下方的**群组自定义机器人**方式配置。已有的 BotBuilder webhook 地址将失效，需要重新配置。

   若启用 **AI 分析**，飞书推送偶发（约 5% 概率）会有数分钟延迟（推测为平台对 AI 生成内容的合规性审核）。

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`FEISHU_WEBHOOK_URL`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的飞书自定义机器人 Webhook 地址（格式：`https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxx`）

   **配置步骤：**

   1. 进入目标群组，在群组右上角点击 **更多** 按钮，并点击 **设置**。

   ![进入群设置](_image/feishu-bot/step1-group-settings.png)

   2. 在右侧 **设置** 界面，点击 **群机器人**。

   ![点击群机器人](_image/feishu-bot/step2-group-bot.png)

   3. 在 **群机器人** 界面点击 **添加机器人**。

   4. 在 **添加机器人** 对话框，找到并点击 **自定义机器人**。

   ![选择自定义机器人](_image/feishu-bot/step3-custom-bot.png)

   5. 设置自定义机器人的头像、名称（如"TrendRadar 热点监控"）与描述，并点击 **添加**。

   ![设置机器人信息](_image/feishu-bot/step4-set-name.png)

   6. 获取自定义机器人的 **webhook 地址**，并点击 **完成**。

   > ⚠️ 请妥善保存此 webhook 地址，不要公布在 GitHub、博客等可公开查阅的网站上，避免地址泄露后被恶意调用发送垃圾消息。

   ![复制 webhook 地址](_image/feishu-bot/step5-webhook-url.png)

   7. 将复制的 Webhook 地址配置到 GitHub Secrets 中的 `FEISHU_WEBHOOK_URL`。

   > 💡 配置完成后，你可以在群组名称右侧点击机器人图片，进入自定义机器人详情页，管理配置信息。
   >
   > 📖 官方文档：[自定义机器人使用指南](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot)

   </details>

   <details>
   <summary>👉 点击展开：<strong>钉钉机器人</strong></summary>
   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`DINGTALK_WEBHOOK_URL`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的钉钉机器人 Webhook 地址

   <br>

   **机器人设置步骤：**

   1. **创建机器人（仅 PC 端支持）**：
      - 打开钉钉 PC 客户端，进入目标群聊
      - 点击群设置图标（⚙️）→ 往下翻找到"机器人"点开
      - 选择"添加机器人" → "自定义"

   2. **配置机器人**：
      - 设置机器人名称
      - **安全设置**：
        - **自定义关键词**：设置 "热点"

   3. **完成设置**：
      - 勾选服务条款协议 → 点击"完成"
      - 复制获得的 Webhook URL
      - 将 URL 配置到 GitHub Secrets 中的 `DINGTALK_WEBHOOK_URL`

   **注意**：移动端只能接收消息，无法创建新机器人。
   </details>

   <details>
   <summary>👉 点击展开：<strong>Telegram Bot</strong></summary>
   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`TELEGRAM_BOT_TOKEN`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的 Telegram Bot Token

   - **Name（名称）**：`TELEGRAM_CHAT_ID`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的 Telegram Chat ID

   **说明**：Telegram 需要配置**两个** Secret，请分别点击两次"New repository secret"按钮添加

   <br>

   **机器人设置步骤：**

   1. **创建机器人**：
      - 在 Telegram 中搜索 `@BotFather`（大小写注意，有蓝色徽章勾勾，有类似 37849827 monthly users，这个才是官方的，有一些仿官方的账号注意辨别）
      - 发送 `/newbot` 命令创建新机器人
      - 设置机器人名称（必须以"bot"结尾，很容易遇到重复名字，所以你要绞尽脑汁想不同的名字）
      - 获取 Bot Token（格式如：`123456789:AAHfiqksKZ8WmR2zSjiQ7_v4TMAKdiHm9T0`）

   2. **获取 Chat ID**：

      **方法一：通过官方 API 获取**
      - 先向你的机器人发送一条消息
      - 访问：`https://api.telegram.org/bot<你的Bot Token>/getUpdates`
      - 在返回的 JSON 中找到 `"chat":{"id":数字}` 中的数字

      **方法二：使用第三方工具**
      - 搜索 `@userinfobot` 并发送 `/start`
      - 获取你的用户 ID 作为 Chat ID

   3. **配置到 GitHub**：
      - `TELEGRAM_BOT_TOKEN`：填入第 1 步获得的 Bot Token
      - `TELEGRAM_CHAT_ID`：填入第 2 步获得的 Chat ID
   </details>

   <details>
   <summary>👉 点击展开：<strong>邮件推送</strong>（支持所有主流邮箱）</summary>
   <br>

   - 注意事项：为防止邮件群发功能被**滥用**，当前的群发是所有收件人都能看到彼此的邮箱地址。
   - 如果你没有过配置下面这种邮箱发送的经历，不建议尝试

   > ⚠️ **重要配置依赖**：邮件推送需要 HTML 报告文件。请确保 `config/config.yaml` 中的 `storage.formats.html` 设置为 `true`：
   > ```yaml
   > storage:
   >   formats:
   >     sqlite: true
   >     txt: false
   >     html: true   # 必须启用，否则邮件推送会失败
   > ```
   > 如果设置为 `false`，邮件推送时会报错：`错误：HTML文件不存在或未提供: None`

   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`EMAIL_FROM`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：发件人邮箱地址

   - **Name（名称）**：`EMAIL_PASSWORD`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：邮箱密码或授权码

   - **Name（名称）**：`EMAIL_TO`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：收件人邮箱地址（多个收件人用英文逗号分隔，也可以和 EMAIL_FROM 一样，自己发送给自己）

   - **Name（名称）**：`EMAIL_SMTP_SERVER`（可选配置，请复制粘贴此名称）
   - **Secret（值）**：SMTP服务器地址（可留空，系统会自动识别）

   - **Name（名称）**：`EMAIL_SMTP_PORT`（可选配置，请复制粘贴此名称）
   - **Secret（值）**：SMTP端口（可留空，系统会自动识别）

   **说明**：邮件推送需要配置至少**3个必需** Secret（EMAIL_FROM、EMAIL_PASSWORD、EMAIL_TO），后两个为可选配置

   <br>

   **支持的邮箱服务商**（自动识别 SMTP 配置）：

   | 邮箱服务商 | 域名 | SMTP 服务器 | 端口 | 加密方式 |
   |-----------|------|------------|------|---------|
   | **Gmail** | gmail.com | smtp.gmail.com | 587 | TLS |
   | **QQ邮箱** | qq.com | smtp.qq.com | 465 | SSL |
   | **Outlook** | outlook.com | smtp-mail.outlook.com | 587 | TLS |
   | **Hotmail** | hotmail.com | smtp-mail.outlook.com | 587 | TLS |
   | **Live** | live.com | smtp-mail.outlook.com | 587 | TLS |
   | **163邮箱** | 163.com | smtp.163.com | 465 | SSL |
   | **126邮箱** | 126.com | smtp.126.com | 465 | SSL |
   | **新浪邮箱** | sina.com | smtp.sina.com | 465 | SSL |
   | **搜狐邮箱** | sohu.com | smtp.sohu.com | 465 | SSL |
   | **天翼邮箱** | 189.cn | smtp.189.cn | 465 | SSL |
   | **阿里云邮箱** | aliyun.com | smtp.aliyun.com | 465 | TLS |
   | **Yandex邮箱** | yandex.com | smtp.yandex.com | 465 | TLS |
   | **iCloud邮箱** | icloud.com | smtp.mail.me.com | 587 | SSL |

   > **自动识别**：使用以上邮箱时，无需手动配置 `EMAIL_SMTP_SERVER` 和 `EMAIL_SMTP_PORT`，系统会自动识别。
   >
   > **反馈说明**：
   > - 如果你使用**其他邮箱**测试成功，欢迎开 [Issues](https://github.com/sansan0/TrendRadar/issues) 告知，我会添加到支持列表
   > - 如果上述邮箱配置有误或无法使用，也请开 [Issues](https://github.com/sansan0/TrendRadar/issues) 反馈，帮助改进项目
   >
   > **特别感谢**：
   > - 感谢 [@DYZYD](https://github.com/DYZYD) 贡献天翼邮箱（189.cn）配置并完成自发自收测试 ([#291](https://github.com/sansan0/TrendRadar/issues/291))
   > - 感谢 [@longzhenren](https://github.com/longzhenren) 贡献阿里云邮箱（aliyun.com）配置并完成测试 ([#344](https://github.com/sansan0/TrendRadar/issues/344))
   > - 感谢 [@ACANX](https://github.com/ACANX) 贡献 Yandex 邮箱（yandex.com）配置并完成测试 ([#663](https://github.com/sansan0/TrendRadar/issues/663))
   > - 感谢 [@Sleepy-Tianhao](https://github.com/Sleepy-Tianhao) 贡献 iCloud 邮箱（icloud.com）配置并完成测试 ([#728](https://github.com/sansan0/TrendRadar/issues/728))

   **常见邮箱设置：**

   #### QQ邮箱：
   1. 登录 QQ邮箱网页版 → 设置 → 账户
   2. 开启 POP3/SMTP 服务
   3. 生成授权码（16位字母）
   4. `EMAIL_PASSWORD` 填写授权码，而非 QQ 密码

   #### Gmail：
   1. 开启两步验证
   2. 生成应用专用密码
   3. `EMAIL_PASSWORD` 填写应用专用密码

   #### 163/126邮箱：
   1. 登录网页版 → 设置 → POP3/SMTP/IMAP
   2. 开启 SMTP 服务
   3. 设置客户端授权码
   4. `EMAIL_PASSWORD` 填写授权码
   <br>

   **高级配置**：
   如果自动识别失败，可手动配置 SMTP：
   - `EMAIL_SMTP_SERVER`：如 smtp.gmail.com
   - `EMAIL_SMTP_PORT`：如 587（TLS）或 465（SSL）
   <br>

   **如果有多个收件人(注意是英文逗号分隔)**：
   - EMAIL_TO="user1@example.com,user2@example.com,user3@example.com"

   </details>

   <details>
   <summary>👉 点击展开：<strong>ntfy 推送</strong>（开源免费，支持自托管）</summary>
   <br>

   **两种使用方式：**

   ### 方式一：免费使用（推荐新手） 🆓

   **特点**：
   - ✅ 无需注册账号，立即使用
   - ✅ 每天 250 条消息（足够 90% 用户）
   - ✅ Topic 名称即"密码"（需选择不易猜测的名称）
   - ⚠️ 消息未加密，不适合敏感信息, 但适合我们这个项目的不敏感信息

   **快速开始：**

   1. **下载 ntfy 应用**：
      - Android：[Google Play](https://play.google.com/store/apps/details?id=io.heckel.ntfy) / [F-Droid](https://f-droid.org/en/packages/io.heckel.ntfy/)
      - iOS：[App Store](https://apps.apple.com/us/app/ntfy/id1625396347)
      - 桌面：访问 [ntfy.sh](https://ntfy.sh)

   2. **订阅主题**（选择一个难猜的名称）：
      ```
      建议格式：trendradar-{你的名字缩写}-{随机数字}
   
      不能使用中文
      
      ✅ 好例子：trendradar-zs-8492
      ❌ 坏例子：news、alerts（太容易被猜到）
      ```

   3. **配置 GitHub Secret（⚠️ Name 名称必须严格一致）**：
      - **Name（名称）**：`NTFY_TOPIC`（请复制粘贴此名称，不要手打）
      - **Secret（值）**：填写你刚才订阅的主题名称

      - **Name（名称）**：`NTFY_SERVER_URL`（可选配置，请复制粘贴此名称）
      - **Secret（值）**：留空（默认使用 ntfy.sh）

      - **Name（名称）**：`NTFY_TOKEN`（可选配置，请复制粘贴此名称）
      - **Secret（值）**：留空

      **说明**：ntfy 至少需要配置 1 个必需 Secret (NTFY_TOPIC)，后两个为可选配置

   4. **测试**：
      ```bash
      curl -d "测试消息" ntfy.sh/你的主题名称
      ```

   ---

   ### 方式二：自托管（完全隐私控制） 🔒

   **适合人群**：有服务器、追求完全隐私、技术能力强

   **优势**：
   - ✅ 完全开源（Apache 2.0 + GPLv2）
   - ✅ 数据完全自主控制
   - ✅ 无任何限制
   - ✅ 零费用

   **Docker 一键部署**：
   ```bash
   docker run -d \
     --name ntfy \
     -p 80:80 \
     -v /var/cache/ntfy:/var/cache/ntfy \
     binwiederhier/ntfy \
     serve --cache-file /var/cache/ntfy/cache.db
   ```

   **配置 TrendRadar**：
   ```yaml
   NTFY_SERVER_URL: https://ntfy.yourdomain.com
   NTFY_TOPIC: trendradar-alerts  # 自托管可用简单名称
   NTFY_TOKEN: tk_your_token  # 可选：启用访问控制
   ```

   **在应用中订阅**：
   - 点击"Use another server"
   - 输入你的服务器地址
   - 输入主题名称
   - （可选）输入登录凭据

   ---

   **常见问题：**

   <details>
   <summary><strong>Q1: 免费版够用吗？</strong></summary>

   每天 250 条消息对大多数用户足够。按 30 分钟抓取一次计算，每天约 48 次推送，完全够用。
   </details>

   <details>
   <summary><strong>Q2: Topic 名称真的安全吗？</strong></summary>

   如果你选择随机的、足够长的名称（如 `trendradar-zs-8492-news`），暴力破解几乎不可能：
   - ntfy 有严格的速率限制（1 秒 1 次请求）
   - 64 个字符选择（A-Z, a-z, 0-9, _, -）
   - 10 位随机字符串有 64^10 种可能性（需要数年才能破解）
   </details>

   ---

   **推荐选择：**

   | 用户类型 | 推荐方案 | 理由 |
   |---------|---------|------|
   | 普通用户 | 方式一（免费） | 简单快速，够用 |
   | 技术用户 | 方式二（自托管） | 完全控制，无限制 |
   | 高频用户 | 方式三（付费） | 这个自己去官网看吧 |

   **相关链接：**
   - [ntfy 官方文档](https://docs.ntfy.sh/)
   - [自托管教程](https://docs.ntfy.sh/install/)
   - [GitHub 仓库](https://github.com/binwiederhier/ntfy)

   </details>

   <details>
   <summary>👉 点击展开：<strong>Bark 推送</strong>（iOS 专属，简洁高效）</summary>
   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`BARK_URL`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的 Bark 推送 URL

   <br>

   **Bark 简介：**

   Bark 是一款 iOS 平台的免费开源推送工具，特点是简单、快速、无广告。

   **使用方式：**

   ### 方式一：使用官方服务器（推荐新手） 🆓

   1. **下载 Bark App**：
      - iOS：[App Store](https://apps.apple.com/cn/app/bark-给你的手机发推送/id1403753865)

   2. **获取推送 URL**：
      - 打开 Bark App
      - 复制首页显示的推送 URL（格式如：`https://api.day.app/your_device_key`）
      - 将 URL 配置到 GitHub Secrets 中的 `BARK_URL`

   ### 方式二：自建服务器（完全隐私控制） 🔒

   **适合人群**：有服务器、追求完全隐私、技术能力强

   **Docker 一键部署**：
   ```bash
   docker run -d \
     --name bark-server \
     -p 8080:8080 \
     finab/bark-server
   ```

   **配置 TrendRadar**：
   ```yaml
   BARK_URL: http://your-server-ip:8080/your_device_key
   ```

   ---

   **注意事项：**
   - ✅ Bark 使用 APNs 推送，单条消息最大 4KB
   - ✅ 支持自动分批推送，无需担心消息过长
   - ✅ 推送格式为纯文本（自动去除 Markdown 语法）
   - ⚠️ 仅支持 iOS 平台

   **相关链接：**
   - [Bark 官方网站](https://bark.day.app/)
   - [Bark GitHub 仓库](https://github.com/Finb/Bark)
   - [Bark Server 自建教程](https://github.com/Finb/bark-server)

   </details>

   <details>
   <summary>👉 点击展开：<strong>Slack 推送</strong></summary>
   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`SLACK_WEBHOOK_URL`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的 Slack Incoming Webhook URL

   <br>

   **Slack 简介：**

   Slack 是团队协作工具，Incoming Webhooks 可以将消息推送到 Slack 频道。

   **设置步骤：**

   ### 步骤 1：创建 Slack App

   1. **访问 Slack API 页面**：
      - 打开 https://api.slack.com/apps?new_app=1
      - 如果未登录，先登录你的 Slack 工作空间

   2. **选择创建方式**：
      - 点击 **"From scratch"**（从头开始创建）

   3. **填写 App 信息**：
      - **App Name**：填写应用名称（如 `TrendRadar` 或 `热点新闻监控`）
      - **Workspace**：从下拉列表选择你的工作空间
      - 点击 **"Create App"** 按钮

   ### 步骤 2：启用 Incoming Webhooks

   1. **导航到 Incoming Webhooks**：
      - 在左侧菜单中找到并点击 **"Incoming Webhooks"**

   2. **启用功能**：
      - 找到 **"Activate Incoming Webhooks"** 开关
      - 将开关从 `OFF` 切换到 `ON`
      - 页面会自动刷新显示新的配置选项

   ### 步骤 3：生成 Webhook URL

   1. **添加新的 Webhook**：
      - 滚动到页面底部
      - 点击 **"Add New Webhook to Workspace"** 按钮

   2. **选择目标频道**：
      - 系统会弹出授权页面
      - 从下拉列表中选择要接收消息的频道（如 `#热点新闻`）
      - ⚠️ 如果要选择私有频道，必须先加入该频道

   3. **授权应用**：
      - 点击 **"Allow"** 按钮完成授权
      - 系统会自动跳转回配置页面

   ### 步骤 4：复制并保存 Webhook URL

   1. **查看生成的 URL**：
      - 在 "Webhook URLs for Your Workspace" 区域
      - 会看到刚刚生成的 Webhook URL
      - 格式如：`https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`

   2. **复制 URL**：
      - 点击 URL 右侧的 **"Copy"** 按钮
      - 或手动选中 URL 并复制

   3. **配置到 TrendRadar**：
      - **GitHub Actions**：将 URL 添加到 GitHub Secrets 中的 `SLACK_WEBHOOK_URL`
      - **本地测试**：将 URL 填入 `config/config.yaml` 的 `slack_webhook_url` 字段
      - **Docker 部署**：将 URL 添加到 `docker/.env` 文件的 `SLACK_WEBHOOK_URL` 变量

   ---

   **注意事项：**
   - ✅ 支持 Markdown 格式（自动转换为 Slack mrkdwn）
   - ✅ 支持自动分批推送（每批 4KB）
   - ✅ 适合团队协作，消息集中管理
   - ⚠️ Webhook URL 包含密钥，切勿公开

   **消息格式预览：**
   ```
   *[第 1/2 批次]*

   📊 *热点词汇统计*

   🔥 *[1/3] AI ChatGPT* : 2 条

     1. [百度热搜] 🆕 ChatGPT-5正式发布 *[1]* - 09时15分 (1次)

     2. [今日头条] AI芯片概念股暴涨 *[3]* - [08时30分 ~ 10时45分] (3次)
   ```

   **相关链接：**
   - [Slack Incoming Webhooks 官方文档](https://api.slack.com/messaging/webhooks)
   - [Slack API 应用管理](https://api.slack.com/apps)

   </details>

   <details>
   <summary>👉 点击展开：<strong>通用 Webhook 推送</strong>（支持 Discord、Matrix、IFTTT 等）</summary>
   <br>

   **GitHub Secret 配置（⚠️ Name 名称必须严格一致）：**
   - **Name（名称）**：`GENERIC_WEBHOOK_URL`（请复制粘贴此名称，不要手打）
   - **Secret（值）**：你的 Webhook URL

   - **Name（名称）**：`GENERIC_WEBHOOK_TEMPLATE`（可选配置，请复制粘贴此名称）
   - **Secret（值）**：JSON 模板字符串，支持 `{title}` 和 `{content}` 占位符

   <br>

   **通用 Webhook 简介：**

   通用 Webhook 支持任意接受 HTTP POST 请求的平台，包括但不限于：
   - **Discord**：通过 Webhook 推送到频道
   - **Matrix**：通过 Webhook 桥接推送
   - **IFTTT**：触发自动化流程
   - **自建服务**：任何支持 Webhook 的自定义服务

   **配置示例：**

   ### Discord 配置

   1. **获取 Webhook URL**：
      - 进入 Discord 服务器设置 → 整合 → Webhooks
      - 创建新 Webhook，复制 URL

   2. **配置模板**：
      ```json
      {"content": "{content}"}
      ```

   3. **GitHub Secret 配置**：
      - `GENERIC_WEBHOOK_URL`：Discord Webhook URL
      - `GENERIC_WEBHOOK_TEMPLATE`：`{"content": "{content}"}`

   ### 自定义模板

   模板支持两个占位符：
   - `{title}` - 消息标题
   - `{content}` - 消息内容

   **模板示例**：
   ```json
   # 默认格式（留空时使用）
   {"title": "{title}", "content": "{content}"}

   # Discord 格式
   {"content": "{content}"}

   # 自定义格式
   {"text": "{content}", "username": "TrendRadar"}
   ```

   ---

   **注意事项：**
   - ✅ 支持 Markdown 格式（与企业微信格式一致）
   - ✅ 支持自动分批推送
   - ✅ 支持多账号配置（用 `;` 分隔）
   - ⚠️ 模板必须是有效的 JSON 格式
   - ⚠️ 不同平台对消息格式要求不同，请参考目标平台文档

   </details>

   <br>

### 3️⃣ 第三步：手动测试新闻推送

   > ⚠️ 提醒：
   > - 完成第 1-2 步后，请立即测试！测试成功后再根据需要调整配置（第 4 步）
   > - 请进入你自己的项目，不是本项目！

   **如何找到你的 Actions 页面**：

   - **方法一**：打开你 fork 的项目主页，点击顶部的 **Actions** 标签
   - **方法二**：直接访问 `https://github.com/你的用户名/TrendRadar/actions`

   **示例对比**：
   - ❌ 作者的项目：`https://github.com/sansan0/TrendRadar/actions`
   - ✅ 你的项目：`https://github.com/你的用户名/TrendRadar/actions`

   **测试步骤**：
   1. 进入你项目的 Actions 页面
   2. 找到 **"Get Hot News"**(必须得是这个字)点进去，点击右侧的 **"Run workflow"** 按钮运行 
      - 如果看不到该字样，参照 [#109](https://github.com/sansan0/TrendRadar/issues/109) 解决
   3. 3 分钟左右，消息会推送到你配置的平台

   <br>

   > ⚠️ 提醒：
   > - 手动测试不要太频繁，避免触发 GitHub Actions 限制
   > - 点击 Run workflow 后需要刷新浏览器页面才能看到新的运行记录

   <br>

### 4️⃣ 第四步：配置说明（可选）

   默认配置已可正常使用，如需个性化调整，了解以下文件即可：

   | 文件 | 作用 |
   |------|------|
   | `config/config.yaml` | 主配置文件：推送模式、时间窗口、平台列表、热点权重等 |
   | `config/frequency_words.txt` | 关键词文件：设置你关心的词汇，筛选推送内容 |
   | `config/ai_analysis_prompt.txt` | AI 提示词模板：自定义 AI 分析师的角色和分析维度 |
   | `.github/workflows/crawler.yml` | 执行频率：控制多久运行一次（⚠️ 谨慎修改） |

   👉 **详细配置教程**：[配置详解](#配置详解)

   <br>

### 5️⃣ 第五步：远程云存储 & 签到配置

   **v4.0.0 重要变更**：引入「活跃度检测」机制，GitHub Actions 需定期签到以维持运行。

   - **运行周期**：有效期为 **7 天**，倒计时结束后服务将自动挂起。
   - **续期方式**：在 Actions 页面手动触发 "Check In" workflow，即可重置 7 天有效期。
   - **操作路径**：`Actions` → `Check In` → `Run workflow`
   - **设计理念**：
     - 如果 7 天都忘了签到，或许这些资讯对你来说并非刚需。适时的暂停，能帮你从信息流中抽离，给大脑留出喘息的空间。
     - GitHub Actions 是宝贵的公共计算资源。引入签到机制旨在避免算力的无效空转，确保资源能分配给真正活跃且需要的用户。感谢你的理解与支持。

   ---

   **关于远程云存储配置（请根据部署方式选择）：**

   - **GitHub Actions 用户**：
     - **现状**：Actions 每次运行都是全新环境，不保存文件。如果不配置云存储，项目将运行在**轻量模式**（无增量推送、无历史追踪）。
     - **建议**：配置远程云存储以获得完整体验。

   - **Docker / 本地用户**：
     - **现状**：数据默认保存在本地硬盘。
     - **建议**：云存储为可选项，可作为异地备份。

   <details>
   <summary>👉 点击展开：<strong>远程云存储配置教程（以 Cloudflare R2 为例）</strong></summary>
   <br>

   **⚠️ 前置条件（重要）：**

   根据 Cloudflare 平台规则，开通 R2 需绑定支付方式。

   * **目的**：仅作身份验证（Verify Only），**不产生扣费**。
   * **支付**：支持双币信用卡或国区 PayPal。
   * **用量**：R2 的免费额度（10GB存储/月）足以覆盖本项目日常运行，无需担心付费。

   ---

   **GitHub Secret 配置（需添加 4 项）：**

   | Name（名称） | Secret（值）说明 |
   |-------------|-----------------|
   | `S3_BUCKET_NAME` | 存储桶名称（如 `trendradar-data`） |
   | `S3_ACCESS_KEY_ID` | 访问密钥 ID（Access Key ID） |
   | `S3_SECRET_ACCESS_KEY` | 访问密钥（Secret Access Key） |
   | `S3_ENDPOINT_URL` | S3 API 端点（如 R2：`https://<account-id>.r2.cloudflarestorage.com`） |

   **可选配置：**

   | Name（名称） | Secret（值）说明 |
   |-------------|-----------------|
   | `S3_REGION` | 区域（默认 `auto`，部分服务商可能需要指定） |

   > 💡 **更多存储配置选项**：参见 [数据保存在哪里？](#11-数据保存在哪里)

   <br>

   **详细操作步骤（获取凭据）：**

   1. **进入 R2 概览**：
      - 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)。
      - 在左侧侧边栏找到并点击 `R2对象存储`。

   2. **创建存储桶**：
      - 点击`概述`
      - 点击右上角的 `创建存储桶` (Create bucket)。
      - 输入名称（例如 `trendradar-data`），点击 `创建存储桶`。

   3. **创建 API 令牌**：
      - 回到 **概述**页面。
      - 点击**右下角** `Account Details `找到并点击 `Manage` (Manage R2 API Tokens)。
      - 同时你会看到 `S3 API`：`https://<account-id>.r2.cloudflarestorage.com`(这就是 S3_ENDPOINT_URL)
      - 点击 `创建 Account APl 令牌` 。
      - **⚠️ 关键设置**：
        - **令牌名称**：随意填写（如 `github-action-write`）。
        - **权限**：选择 `管理员读和写` 。
        - **指定存储桶**：为了安全，建议选择 `仅适用于指定存储桶` 并选中你的桶（如 `trendradar-data`）。
      - 点击 `创建 API 令牌`，**立即复制** 显示的 `Access Key ID` 和 `Secret Access Key`（只显示一次！）。

   </details>

   <br>

### 6️⃣ 第六步：开启 AI 分析推送

   这是 v5.0.0 的核心功能，让 AI 帮你总结和分析新闻，建议尝试。

   **配置方法：**
   在 GitHub Secrets (或 `.env` / `config.yaml`) 中添加：
   - `AI_API_KEY`: 你的 API Key（支持 DeepSeek、OpenAI 等）
   - `AI_PROVIDER`: 服务商名称（如 `deepseek`, `openai`）

   就这样，无需复杂部署，下次推送时你就会看到智能分析报告了。

   <br>

### 7️⃣ 第七步：🎉 部署成功！

   恭喜！现在你可以开始享受 TrendRadar 带来的高效信息流了。

   💬 **加入社区**：欢迎关注公众号「**[硅基茶水间](#-支持项目)**」，分享你的使用心得和高级玩法。

   <br>

### 8️⃣ 第八步：进阶：选择你的 AI 助手

   TrendRadar 提供了两种 AI 使用方式，满足不同需求：

   | 特性 | ✨ AI 分析推送 | 🧠 AI 智能分析 |
   | :--- | :--- | :--- |
   | **模式** | **被动接收** (每日日报) | **主动对话** (深度调研) |
   | **场景** | "今天有什么大事？" | "分析一下过去一周 AI 行业的变化" |
   | **部署** | 极简 (填 Key 即可) | 进阶 (需本地运行/Docker) |
   | **客户端** | 手机 |  电脑 |
  

   👉 **结论**：先用 **AI 分析推送** 满足日常需求；如果你是数据分析师或需要深度挖掘，再尝试 **[AI 智能分析](#-ai-智能分析)**。

<br>

<a name="配置详解"></a>

## ⚙️ 配置详解

> **📖 提醒**：本章节提供详细的配置说明，建议先完成 [快速开始](#-快速开始) 的基础配置，再根据需要回来查看详细选项。

### 1. 我要看哪些平台？

<details id="自定义监控平台">
<summary>👉 点击展开：<strong>选择资讯来源</strong></summary>
<br>

**配置位置：** `config/config.yaml` 的 `platforms` 部分

本项目的资讯数据来源于 [newsnow](https://github.com/ourongxing/newsnow) ，你可以点击[网站](https://newsnow.busiyi.world/)，点击[更多]，查看是否有你想要的平台。

具体添加可访问 [项目源代码](https://github.com/ourongxing/newsnow/tree/main/server/sources)，根据里面的文件名，在 `config/config.yaml` 文件中修改 `platforms` 配置：

```yaml
platforms:
  enabled: true                       # 是否启用热榜平台抓取
  sources:
    - id: "toutiao"
      name: "今日头条"
    - id: "baidu"
      name: "百度热搜"
    - id: "wallstreetcn-hot"
      name: "华尔街见闻"
    # 添加更多平台...
```

> 💡 **快捷方式**：如果不会看源代码，可以复制他人整理好的 [平台配置汇总](https://github.com/sansan0/TrendRadar/issues/95)

> ⚠️ **注意**：平台不是越多越好，建议选择 10-15 个核心平台。过多平台会导致信息过载，反而降低使用体验。

</details>

### 2. 我关心什么内容？

在 `frequency_words.txt` 文件中告诉机器人你想看什么，它就会帮你盯着。支持普通词、必须词、过滤词等多种玩法。

| 语法类型 | 符号 | 作用 | 示例 | 匹配逻辑 |
|---------|------|------|------|---------|
| **普通词** | 无 | 基础匹配 | `华为` | 包含任意一个即可 |
| **必须词** | `+` | 限定范围 | `+手机` | 必须同时包含 |
| **过滤词** | `!` | 排除干扰 | `!广告` | 包含则直接排除 |
| **数量限制** | `@` | 控制显示数量 | `@10` | 最多显示10条新闻（v3.2.0新增） |
| **全局过滤** | `[GLOBAL_FILTER]` | 全局排除指定内容 | 见下方示例 | 任何情况下都过滤（v3.5.0新增） |
| **正则表达式** | `/pattern/` | 精确匹配模式 | `/\bai\b/` | 使用正则表达式匹配（v4.7.0新增） |
| **显示名称** | `=> 备注` | 自定义显示文本 | `/\bai\b/ => AI相关