# 羊毛猎手 · Deal Hunter

**中文** | [English](#english)

让 Grok Bot、Muse、ChatGPT Work 这类自带云电脑的 AI 帮你薅羊毛：**全网找羊毛 → 回官方页核对 → 分类去重 → 用你登录好的浏览器自动领 → 过期归档 → 出日报。** 你用什么语言跟它说话，它就用什么语言回复。

覆盖 AI 订阅和免费额度、Crypto 空投/积分/交易所活动、U卡、海外银行与银行卡、VPS 与云、软件限免。

## 在 Grok Bot、Muse、ChatGPT Work 里用（最常用）

**方法一：一句话。** 把这句发给它：

```
帮我装上这个 skill：https://github.com/cc6pzupa/cc-deal-hunter
```

**方法二：复制一段话。** 打开 [`PROMPT.md`](PROMPT.md)，复制「中文版」那一段发给它。

几个建议：
- **装好就全部就绪**：发完那句话，它会一次性做完——查登录、建看板、设定时、跑第一轮，然后给你一条汇报，你不用再说别的。
- **默认定时**：安装时它会自己设好每 2 小时跑一次（用平台的定时任务），只在有新的高价值、快截止或待你处理时提醒你；想改就说「改成 4 小时一次」「停掉」。
- 放进一个专门的 **Space / 项目**，记录和设置都留在里面。
- 不用先填设置：开局它先查 Google，没登录就直接弹接管让你登录，然后**给你建一个羊毛看板**（统计、A–H 分栏、待你处理、搜索），之后每跑一轮刷新；想改范围随时说一句，比如「只要 AI 和 VPS」。
- 自动领取需要登录时，它会请你**接管浏览器**，你自己输密码；登录之后一直保留在云电脑里。
- 第一次在云电脑登录 Google，Google 会让你在手机上点一个数字确认——**它会直接把数字告诉你**，你在手机上点同样的数字就行。
- 建议用一个专门薅羊毛的账号，不要在云电脑里登录主力邮箱、银行或交易所账号。

> **给 AI 看的说明 / For AI agents**：「安装」= 在这一轮里把全部设置做完，不要只复制文件就停。不能安装 skill 的（Grok Bot、Muse、ChatGPT Work 等）：读取 [`PROMPT.md`](PROMPT.md) 里用户语言的那一段，当作长期指令，**立刻**按它开头的五步做完：查 Google 登录（没登录直接弹接管）→ 建看板 → 设每 2 小时定时 → 跑第一轮 → 一条消息汇报。能安装 skill 的：把 `skills/deal-hunter/` 复制到 skills 目录，然后**立刻**按 `SKILL.md` 第 0 节同样做完这五步。
> "Install" means finishing the whole setup in this turn, not just copying files. If you can't install skills (Grok Bot, Muse, ChatGPT Work…), take the block in the user's language from [`PROMPT.md`](PROMPT.md) as standing instructions and **immediately** do its five setup steps: Google sign-in check (take-over if signed out) → build the board → create the 2-hour schedule → run the first batch → report in one message. If you can install skills, copy `skills/deal-hunter/` into your skills directory and **immediately** do the same five steps from §0 of `SKILL.md`.

## 不会卡住：「🙋 待你处理」清单

注册表单它会自己填（姓名邮箱用你 Google 的，生日、性别、职业、公司、用途等按成年人自动生成一套合理资料并固定复用；手机号第一次问你一次，之后复用；地址按 IP 所在城市取一个公共地点）；要**邮箱验证码**的，它会直接去你的 Gmail 取码填上。要登录、付款、绑卡、充值、实名认证、短信验证码、人机验证、连接钱包、签名授权的，AI 不替你做，也**不会停下来等你**：放进「🙋 待你处理」清单，接着领下一条。整批跑完按原因分组给你，要登录的你接管一次全部登好，说「继续领」就行。

一人一份，不注册小号，不绕过网站的机器人检测。详见 [`claiming.md`](skills/deal-hunter/references/claiming.md)。

## 其他 AI 的安装方式

**Claude Code**（在 Claude Code 里输入）：
```
/plugin install deal-hunter --marketplace cc6pzupa/cc-deal-hunter
```
较老的版本分两步：`/plugin marketplace add cc6pzupa/cc-deal-hunter`，再 `/plugin install deal-hunter@deal-hunter`。

**Codex、Gemini CLI、Cursor 等支持 Agent Skills 的工具**（需要 Node.js，用 [skills CLI](https://github.com/vercel-labs/skills)）：
```bash
npx skills add cc6pzupa/cc-deal-hunter          # 交互式选择装到哪个工具
npx skills add cc6pzupa/cc-deal-hunter -g -y    # 全局安装，跳过询问
```

**Claude 网页 / App**：下载 [deal-hunter.zip](https://wool.eshop.us.ci/skill/deal-hunter.zip)，在 设置 → Skills 里上传。

**手动**：
```bash
git clone --depth 1 https://github.com/cc6pzupa/cc-deal-hunter /tmp/cc-deal-hunter && cp -r /tmp/cc-deal-hunter/skills/deal-hunter ~/.claude/skills/
```

本机运行的 AI 用你电脑上的浏览器领取（Claude in Chrome 等扩展、Playwright MCP 加持久化配置目录、桌面控制），登录态不离开你的电脑。

## 里面有什么

```
PROMPT.md                   一段话版（中文版 + English），给 Grok Bot、Muse、ChatGPT Work 等
skills/deal-hunter/
  SKILL.md                  主流程（中英双语）：发现 → 核对 → 记账 → 领取 → 汇报 → 定时
  references/sources.md     各类别去哪找、怎么搜
  references/claiming.md    各平台浏览器怎么登录、领取流程、待你处理
  scripts/dashboard.html    看板模板（ledger.py dashboard 生成单文件 HTML 看板）
  scripts/ledger.py         本地账本：去重、过期归档、领取记录、待你处理清单、A–H 日报（--lang zh|en，只用 Python 标准库）
  scripts/feeds.py          读任意 RSS / Atom 源
.claude-plugin/             Claude Code 插件市场配置
```

## 数据源

已核对的现成数据源：[cc羊毛减](https://wool.eshop.us.ci)——X 上的中文羊毛帖，每条都回原帖核对过，提供 RSS 和 MCP。其他来源（官方公告、Reddit、Doctor of Credit、LowEndTalk、NodeSeek、linux.do 等）见 [`sources.md`](skills/deal-hunter/references/sources.md)。

## 许可

[PolyForm Noncommercial 1.0.0](LICENSE.md)：个人学习、研究、自用以及非营利用途可以免费使用和修改；**禁止任何商业用途**（包括拿去收费、打包售卖、放进付费产品或服务）。商业授权请在 X 上联系 [@cc6pazpo](https://x.com/cc6pazpo)。

## 联系

X：[@cc6pazpo](https://x.com/cc6pazpo)

## 免责声明

本项目只整理公开信息并按你的指令操作你自己的账号。优惠、返利、开户、空投类信息不构成投资或消费建议；参与前请自行核实条款和风险，遵守各平台规则。

---

## English

[中文](#羊毛猎手--deal-hunter) | **English**

Let agents with a built-in cloud computer — Grok Bot, Muse, ChatGPT Work — hunt deals for you: **find deals across the web → verify each on the official page → classify and de-duplicate → claim them in a browser you've signed in to → archive expired ones → write a digest.** It replies in whatever language you use.

Covers free AI credits and plan discounts, crypto airdrops/points/exchange promos, crypto cards, overseas bank and card sign-up bonuses, free VPS/cloud tiers, and software giveaways.

### Use it in Grok Bot, Muse or ChatGPT Work (most common)

**Option 1 — one line.** Send it this:

```
Install this skill: https://github.com/cc6pzupa/cc-deal-hunter
```

**Option 2 — paste the prompt.** Copy the English block from [`PROMPT.md`](PROMPT.md#english) and send it.

Tips:
- **Ready right after install**: after that one line it does everything at once — sign-in check, board, schedule, first run — then sends you one summary; nothing else to say.
- **Scheduled by default**: during install it sets itself to run every 2 hours (via the platform's scheduled tasks) and only pings you about new high-value, ending-soon or waiting items; say "every 4 hours" or "stop" to change it.
- Put it in a dedicated **Space / project** so records and settings stay there.
- No setup questionnaire: it checks Google first, pops up a take-over for you to sign in if needed, then **builds you a deal board** (stats, A–H tabs, waiting list, search) that it refreshes after every run; say "only AI and VPS" any time to narrow it.
- When claiming needs a login, it asks you to **take over the browser** and sign in yourself; the session stays on the cloud computer.
- The first Google sign-in on a cloud computer usually asks you to tap a number on your phone — **the agent tells you the number**; just tap the same one.
- Use a dedicated deals account; don't sign in to your main email, bank or exchange accounts on a cloud computer.

### Never stuck: the "🙋 Waiting for you" list

Sign-up forms are filled for you (name and email from your Google account; birthday, gender, occupation, company, use case and similar fields from one auto-generated adult profile, reused everywhere; your phone number is asked once and reused; addresses use a public place in the IP's city). **Email verification codes** are fetched from your Gmail automatically. Anything that needs a sign-in, payment, card, deposit, KYC, SMS code, CAPTCHA, wallet connection or signature is never done for you and **never blocks the run**: it goes on a "🙋 Waiting for you" list and the agent moves on. At the end you get the list grouped by reason; take over once to sign in to all the sites, say "continue claiming", and it retries. One claim per person, no alt accounts, no bot-detection bypassing. See [`claiming.md`](skills/deal-hunter/references/claiming.md).

### Other AIs

- **Claude Code:** `/plugin install deal-hunter --marketplace cc6pzupa/cc-deal-hunter` (older versions: `/plugin marketplace add cc6pzupa/cc-deal-hunter`, then `/plugin install deal-hunter@deal-hunter`)
- **Codex, Gemini CLI, Cursor and other Agent Skills tools:** `npx skills add cc6pzupa/cc-deal-hunter` (needs Node.js; [skills CLI](https://github.com/vercel-labs/skills))
- **Claude (web / app):** upload [deal-hunter.zip](https://wool.eshop.us.ci/skill/deal-hunter.zip) in Settings → Skills.
- **Manual:** copy `skills/deal-hunter` into your tool's skills folder (e.g. `~/.claude/skills/`).

Local agents claim through your own browser (Claude in Chrome and similar extensions, Playwright MCP with a persistent profile, computer use); the session never leaves your machine.

### What's inside

`PROMPT.md` has the paste-in prompt in Chinese and English. `skills/deal-hunter/` holds `SKILL.md` (bilingual workflow), `references/sources.md` (where to look), `references/claiming.md` (sign-in per platform, claim flow, waiting list), `scripts/dashboard.html` (board template for `ledger.py dashboard`), `scripts/ledger.py` (local ledger, de-dupe, auto-archive, claim log, waiting-for-you list, A–H digest with `--lang zh|en`; Python stdlib only) and `scripts/feeds.py` (RSS/Atom reader).

### Data sources

Ready-made verified source: [cc羊毛减](https://wool.eshop.us.ci) — deal posts from X (mostly Chinese), each re-checked against the original post, with RSS and MCP. Other sources (official announcements, Reddit, Doctor of Credit, LowEndTalk, NodeSeek, linux.do…) are listed in [`sources.md`](skills/deal-hunter/references/sources.md).

### License

[PolyForm Noncommercial 1.0.0](LICENSE.md): free for personal, research and non-profit use and modification; **no commercial use** (no charging for it, reselling it, or putting it in a paid product or service). For a commercial licence, contact [@cc6pazpo](https://x.com/cc6pazpo) on X.

### Contact

X: [@cc6pazpo](https://x.com/cc6pazpo)

### Disclaimer

This project only organises public information and operates your own accounts on your instructions. Deal, cashback, account-opening and airdrop information is not investment or purchasing advice; check the terms and risks yourself and follow each platform's rules.
