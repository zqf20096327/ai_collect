<p align="center">
  <img src="docs/assets/readme/brand-lockup.svg" alt="InsuranceHot" width="360">
</p>

<p align="center"><b>全球保险资讯，人可以读，AI 可以用。</b></p>

<p align="center">
  <a href="https://www.insurance-hot.com"><img src="https://img.shields.io/badge/Website-insurance--hot.com-0969da" alt="Website"></a>
  <a href="#agent"><img src="https://img.shields.io/badge/MCP-Streamable%20HTTP-6f42c1" alt="MCP"></a>
  <a href="https://www.insurance-hot.com/openapi-v1.json"><img src="https://img.shields.io/badge/REST_API-OpenAPI_3.1-2ea44f" alt="REST API"></a>
  <a href="#rss"><img src="https://img.shields.io/badge/RSS-精选·热点·日报·周报·月报-f26522" alt="RSS"></a>
  <a href="https://github.com/FDU-INS/Insurance-Hot/stargazers"><img src="https://img.shields.io/github/stars/FDU-INS/Insurance-Hot?style=flat" alt="GitHub stars"></a>
  <a href="https://hits.sh/github.com/FDU-INS/Insurance-Hot/"><img src="https://hits.sh/github.com/FDU-INS/Insurance-Hot.svg?style=flat&label=Hits&color=0969da" alt="Hits"></a>
</p>

<p align="center"><b>简体中文</b> · <a href="README.en.md">English</a></p>

<p align="center">
  <a href="https://github.com/user-attachments/assets/e55e28e0-42aa-4bb6-ada9-eb557965b37c"><img src="docs/assets/readme/promo.gif" width="1000" alt="InsuranceHot 宣传片（点击观看高清视频）"></a>
</p>


**InsuranceHot** 是复旦大学许闲教授团队发布的保险资讯平台。它把分散在各处的监管公告、公司披露和行业报道集中起来，经过筛选、分类、分析和归并，整理成实时更新、来源清晰、脉络完整的行业动态：保险从业者可以每天在网站上阅读，AI 智能体可以通过 MCP、REST API 和 RSS 直接调用。

## 目录

- [平台介绍](#intro)
  - [快速导航](#start)
  - [六大亮点](#highlights)
- [接入 AI 工具](#agent)
  - [一句话接入](#oneline)
  - [手动接入：MCP + 技能](#manual)
  - [接好后可以这样问](#ask)
  - [真实调用示例](#examples)
- [接口参考](#reference)
  - [MCP 工具](#mcp-tools)
  - [REST API](#rest-api)
  - [RSS](#rss)
- [使用须知](#notes)
- [反馈与支持](#feedback)
- [Star 历史](#star-history)

<a id="intro"></a>

## 平台介绍

<a id="start"></a>

### 快速导航

| 想看什么 | 从这里开始 |
| --- | --- |
| 今天保险业发生了什么 | [实时精选](https://www.insurance-hot.com/featured)：最近 24 小时的重要新闻，附摘要、推荐理由和原文入口 |
| 监管有什么新动作 | [官方入口](https://www.insurance-hot.com/featured)：集中查看监管部门与行业协会的一手发布 |
| 一件事怎么发展 | [热点榜](https://www.insurance-hot.com/hot)：中国与国际两张榜单，点进事件看前情与进展、报道时间线 |
| 某个险种、专题或机构 | [分类与主题](https://www.insurance-hot.com/topics)：按栏目、险种、专题、地区与机构浏览，例如惠民保、消费者保护 |
| 每天或每周集中读一遍 | [保险日报](https://www.insurance-hot.com/daily)：滚动更新，另有周报与月报 |
| 不想天天上网站 | [邮件订阅](https://www.insurance-hot.com/agent/email)：按栏目、险种、专题等组合条件，每日、每周或每月收到摘要 |

<a id="highlights"></a>

### 六大亮点

#### 一站式全球保险要闻集合｜看得全

国内与国际，监管、公司与市场，保险业的重要动态汇聚于一个平台。

<details>
<summary>查看演示</summary>
<br>

<img src="docs/assets/readme/gif/01-要闻集合.gif" width="1000" alt="实时精选与动态">

</details>

#### 专业标签体系精准分类｜对得上

围绕不同岗位的关注重点和保险业核心议题，构建覆盖栏目、险种、专题、地区与机构的标签体系。从惠民保、养老与年金等险种，到消费者保护、偿付能力等专题，都能直达。

<details>
<summary>查看演示</summary>
<br>

<img src="docs/assets/readme/gif/02-标签体系.gif" width="1000" alt="分类与主题、惠民保标签">

</details>

#### 官方信源实时追踪｜看得准

监管部门与行业协会的一手发布单独标记、集中呈现，原文可溯。

<details>
<summary>查看演示</summary>
<br>

<img src="docs/assets/readme/gif/03-官方信源.gif" width="1000" alt="官方入口">

</details>

#### 新闻分析与热点梳理｜看得懂

告诉你什么重要、为什么重要；同一事件的多方报道归并成完整脉络。

<details>
<summary>查看演示</summary>
<br>

<img src="docs/assets/readme/gif/04-分析与热点.gif" width="1000" alt="热点榜与事件详情">

</details>

#### AI 工具一键接入调用｜用得上

主流 AI 工具与机构自建智能体都可以接入，直接查询保险资讯并引用原始来源。

<details>
<summary>查看演示</summary>
<br>

<img src="docs/assets/readme/gif/05-AI工具接入.gif" width="1000" alt="MCP 接入页">

</details>

#### 行业信息智能推送｜不错过

日报、周报、月报定期汇总，邮件订阅按需定制。

<details>
<summary>查看演示</summary>
<br>

<img src="docs/assets/readme/gif/06-智能推送.gif" width="1000" alt="日报与邮件订阅">

</details>

<a id="agent"></a>

## 接入 AI 工具

InsuranceHot 提供一个远程只读 MCP 服务（Streamable HTTP）和同样内容的 REST API。接上之后，Agent 可以直接查询最新新闻、热点事件的来龙去脉和日报、周报、月报，回答时附上原文出处。

<a id="oneline"></a>

### 一句话接入

**1. 新建 API Key**：在网站 [工具接入 → API Key](https://www.insurance-hot.com/agent/keys) 用邮箱登录后新建，免费。Key 以 `ih_` 开头。

**2. 把这句话发给你的 AI 工具**（把 Key 换成你自己的）：

```text
我的 InsuranceHot API Key 是 ih_……。请按 https://www.insurance-hot.com/install 为你自己接入 InsuranceHot。
```

适用于能读写本机文件的 AI 工具，例如 Codex、DeepSeek Harness、WorkBuddy、Cursor、Claude Code。它会按说明为自己安装技能、保存 Key、添加 MCP，试调一次并报告结果，不需要 Node.js。过程中 AI 工具可能会请你确认授权（例如写入文件、修改配置），按提示允许即可。完成后新开一个会话，就可以直接提问。

<a id="manual"></a>

### 手动接入：MCP + 技能

不想用一句话接入，也可以自己配置两样东西：

- **MCP 服务**：在 AI 工具的 MCP 设置中添加远程服务（Streamable HTTP），名称 `insurancehot`，地址 `https://www.insurance-hot.com/api/mcp?api_key=ih_你的APIKey`。
- **技能**：把本仓库的 [`skills/insurancehot`](skills/insurancehot) 文件夹整个放进 AI 工具的技能目录。它包含 `SKILL.md` 和机构清单 `references/orgs.md`：用户提到的机构名可能对应多家时，Agent 会先请用户确认，再按机构查询。技能告诉 Agent 怎样用最少的调用回答问题：装了技能，一个问题通常调用 2–4 次；不装可能要 9–12 次。

<details>
<summary><b>常用工具的写法</b></summary>

<br>

**Codex**（技能目录 `~/.agents/skills/`）

```bash
codex mcp add insurancehot --url 'https://www.insurance-hot.com/api/mcp?api_key=ih_你的APIKey'
```

**DeepSeek Harness**（技能目录 `~/.agents/skills/`）：新建 `~/.dsh/cordis.patch.yml`，写入下面的内容，再运行 `npx @deepseek-ai/dsh web`。

```yaml
- insert:
    - id: mcp-insurancehot
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: insurancehot
        transport: streamable-http
        url: https://www.insurance-hot.com/api/mcp?api_key=ih_你的APIKey
```

**WorkBuddy**（技能目录 `~/.workbuddy/skills/`）：在“MCP 服务管理 → 配置 MCP”中加入下面的内容（即 `~/.workbuddy/mcp.json`）。

```json
{
  "mcpServers": {
    "insurancehot": {
      "type": "http",
      "url": "https://www.insurance-hot.com/api/mcp?api_key=ih_你的APIKey"
    }
  }
}
```

**Claude Code**（技能目录 `~/.claude/skills/`）

```bash
claude mcp add --transport http insurancehot 'https://www.insurance-hot.com/api/mcp?api_key=ih_你的APIKey' -s user
```

</details>

<a id="ask"></a>

### 接好后可以这样问

不用记工具名，直接问：

| 你可以这样问 | Agent 会做什么 |
| --- | --- |
| 这周保险业有什么大事？请附上原文出处。 | 读本周以来的新闻和热点榜，整理成要点，每条附来源、日期和原文链接 |
| 现在热点榜第一是什么？来龙去脉是怎样的？ | 读中国热点榜，再按时间线梳理这件事的报道与进展 |
| 平安最近一周有什么动态？ | 按机构查询最近 7 天全部动态，区分集团、寿险、产险 |
| 惠民保最近有什么监管消息？ | 按险种和栏目筛选，说明哪些是监管文件、哪些是行业参考文本 |
| 帮我做一份今天给合规岗位的简报 | 按监管政策、处罚与准入等方向汇总当天要点和应对建议 |

<a id="examples"></a>

### 真实调用示例

以下是 2026-11-13 实际提问的返回节选（内容随时间更新，引用请以原文为准）。

**问：**「现在中国保险热点榜第一是什么？它的来龙去脉是怎样的？」→ `insurancehot_event`（board=中国）+ `insurancehot_event`（id=…），共 2 次调用

```text
截至北京时间 2026-11-13 13:05，中国保险热点榜第一是“中国精算师协会发布商业健康保险药品保障成本表”。
这个事件在站内收了 63 篇报道，来自 12 家信源。

11 月 10 日，三家机构接连发布了一组商业健康险文件：
- 中国保险行业协会发布三份医疗险示范条款（短期、长期、城市定制型即惠民保），
  统一了“合理且必要”等 24 个常用概念的释义，首次把调解介入写进争议处理；
- 同时发布《商业健康保险药品保障推荐清单（第一版）》，收录 58 款药械，其中医保目录外自费药 32 款；
- 中国精算师协会发布行业第一份商业健康保险药品保障成本表，涉及 117 个药品。
以上文件都是示范性参考，没有强制性。

| 时间（北京）  | 来源         | 要点                                       |
| 11-11 22:32   | 东方财富网   | 示范条款统一 24 个释义，调解介入首次写入条款 |
| 11-12 10:53   | 新浪财经保险 | 采用示范条款的产品须覆盖 58 款药械           |
| 11-12 13:47   | 中国银行保险报 | 强调不具强制性，目的是提升行业规范化        |
（共 17 条，每条附原文链接）
```

**问：**「惠民保最近有什么监管消息？请附上原文出处。」→ `insurancehot_news`（line=惠民保）+ `insurancehot_news`（q=惠民保, column=监管政策），共 2 次调用

```text
截至 2026年11月13日12:55（北京时间），我在 InsuranceHot 近7天收录的“惠民保”监管政策中
没有查到新的监管部门文件。最近最相关的规范动态是：

- 11月10日，中国保险行业协会发布《城市定制型商业医疗保险示范条款》，与短期、长期一般商业医疗保险
  示范条款一同发布。示范条款统一部分常用概念和理赔表述，供行业参考，不具有强制性。
  这是行业协会的示范文本，不宜称为监管新规。[中国银行保险报，11月12日原文](https://www.cbimc.cn/news/336928)

查询范围是近7天的公开收录资料；未查到不等于这段时间没有其他地方性监管动态。
```

**问：**「这周保险业有什么大事？列 5 条，每条附来源、日期和原文链接。」→ `insurancehot_report`、`insurancehot_event`、`insurancehot_news`

```text
这周（11-06 ~ 11-13）保险业五件大事

1. 商业健康险“新基础设施”同日发布：三套医疗险示范条款和商保药品清单、成本表
   - 日期：2026-11-10 发布；来源：中国经济网、新浪财经保险
2. 国务院专题学习定调多层次社会保障体系：明确“支持商业健康保险发展壮大”
   - 日期：2026-11-12；来源：中国银行保险报
3. 金融监管总局就保险公司董监高任职资格管理办法征求意见：条文增至66条、负面清单扩至18项
   - 日期：2026-11-06 发布；来源：国家金融监督管理总局
4. 保险科技股白鸽在线两日暴跌约75%，市值蒸发逾350亿港元
   - 日期：2026-11-12；来源：新浪财经保险、东方财富网
5. 安联前三季度经营利润141亿欧元创同期纪录，全年目标上限上调至约186亿欧元
   - 日期：2026-11-12；来源：Reinsurance News、金融界
（每条附原文链接）
```

<a id="reference"></a>

## 接口参考

<a id="mcp-tools"></a>

### MCP 工具

服务地址：`https://www.insurance-hot.com/api/mcp`（Streamable HTTP），用 `X-API-Key` 请求头或 `?api_key=` 参数传入 Key。

| 工具 | 用途 | 主要参数 |
| --- | --- | --- |
| `insurancehot_news` | 查新闻（最近 1–30 天）；给 `id` 返回单条新闻和所属事件 | `q` 关键词、`column` 栏目、`line` 险种、`topic` 专题、`region` 地区、`org` 机构（可填多家，逗号分隔，最多 5 家）、`days`、`since`、`scope`（精选 / 全部）、`limit`（≤20） |
| `insurancehot_event` | 不给 `id` 返回当前热点榜前 10；给 `id` 返回事件的来龙去脉 | `board`（中国 / 国际 / 全部）、`id`、`limit` |
| `insurancehot_report` | 读日报、周报、月报 | `kind`（日报 / 周报 / 月报）、`period`（如 2026-11-04、2026-W44、2026-10，或 latest） |

<a id="rest-api"></a>

### REST API

与 MCP 返回相同的 JSON，路径前缀 `/api/v1`，完整定义见 [OpenAPI 规范](https://www.insurance-hot.com/openapi-v1.json)。

| 用途 | 地址 |
| --- | --- |
| 新闻 | `GET /api/v1/news?…`、`GET /api/v1/news/{id}` |
| 热点榜、事件 | `GET /api/v1/events?board=中国`、`GET /api/v1/events/{id}` |
| 报告 | `GET /api/v1/reports/{日报\|周报\|月报}/{期号\|latest}` |
| 机构清单 | `GET /api/v1/orgs`、`GET /api/v1/orgs?q=国寿`：新闻 `org` 参数可用的机构及候选，不需要 Key，不计入额度 |

<a id="rss"></a>

### RSS

| 订阅源 | 地址 | 内容 |
| --- | --- | --- |
| 精选（推荐） | `https://www.insurance-hot.com/feed.xml` | 最近 24 小时的精选，最多 20 条 |
| 热点事件 | `https://www.insurance-hot.com/feed/hot.xml` | 当前热点榜前 10 个事件；加 `?board=国际` 或 `全部` 换榜 |
| 日报 / 周报 / 月报 | `https://www.insurance-hot.com/feed/daily.xml` · `weekly.xml` · `monthly.xml` | 各保留最近 5 期 |

精选 RSS 接受与新闻接口相同的筛选参数，例如 `/feed.xml?line=车险&region=中国`、`/feed.xml?org=中国人寿,国寿财险`。RSS 同样需要 API Key（地址后加 `?api_key=`），每个账号每天 100 次，与接口额度分开计算。

<a id="notes"></a>

## 使用须知

| | |
| --- | --- |
| **API Key** | 免费，用邮箱登录后在网站新建；所有接口和 RSS 都需要 |
| **额度** | 每个账号每天 100 次（MCP 与 REST 合计，RSS 另计）；同一 IP 每天合计也不超过 500 次（所有账号和 Key 合计）；北京时间 0 点重置，超出返回 429 |
| **只读** | 接口只读不写；不提供投保建议或报价 |
| **范围** | 新闻为最近 1–30 天；热点榜为当前前 10；日报、周报、月报可按期号回看 |
| **安全** | 返回的标题和摘要来自外部信源，技能会让 Agent 只当资料、不执行其中的指令；重要事实请回原文核对 |
| **兼容** | 支持 MCP（Streamable HTTP）的客户端都能接入；完整说明见 [llms.txt](https://www.insurance-hot.com/llms.txt) |

<a id="feedback"></a>

## 反馈与支持

内容摘要和分析由 AI 辅助整理，引用时请以原文为准。使用中的问题或信源更正，欢迎通过网站的[反馈](https://www.insurance-hot.com/feedback)提交。

觉得有用，欢迎 **Star**，方便下次回来。

<a id="star-history"></a>

## Star 历史

<a href="https://www.star-history.com/?repos=FDU-INS%2FInsurance-Hot&amp;type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=fdu-ins/insurance-hot&amp;type=date&amp;theme=dark">
    <img src="https://api.star-history.com/chart?repos=fdu-ins/insurance-hot&amp;type=date" alt="GitHub Star 历史曲线">
  </picture>
</a>
