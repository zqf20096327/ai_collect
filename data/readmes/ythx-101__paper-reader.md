# paper-reader

**把一篇学术论文，做成每个数字都有出处、普通人愿意读完的图解组图。**

一个给 Claude Code 等 AI agent 用的技能（skill）。你给它一篇论文和一个标题，它会合法地找到原文、整理带出处的事实表、按 PaperBanana 的五角色流程出图，再让强模型逐张评审忠实度，最后用 [Kami](https://github.com/tw93/Kami) 排版成可以直接发 X 或小红书的 PNG。适合做科普、在 X / 小红书讲论文的创作者，以及想把论文讲给普通人听的研究者和学生，用来做论文解读、论文图解和学术论文可视化。

![小红书封面示例：胜利者效应论文图解](examples/xhs-cover.jpg)

## 它做什么

- **合法获取原文**：Unpaywall / PMC / arXiv → 作者主页 → 免费补充材料 → 开放获取的评论与综述 → 学位论文 → 起草索取单行本的邮件。不使用 Sci-Hub、LibGen、Anna's Archive 等盗版站。
- **新闻稿只当线索**：上图的数字必须回到原文或补充材料核对。
- **带出处的事实表**：每行写明结论、数字（写成「9/10」这种只数）、出自哪张图或表、来源 URL。没有出处的说法不上图。
- **PaperBanana 五角色出图**：检索 → 规划 → 风格 → 出图 → 评审。数据图一律用代码画，示意图手写 SVG。
- **忠实度 P0 闸门**：编数字、箭头画反、说法超出原文都是 P0，不清零不交付。
- **类比要标注**：引申到人和生活的部分，明确标「我的引申，不是论文结论」。
- **按平台出成品**：X 发 4 张（平台上限）；小红书按内容定，一般 6–9 张，最多 18 张；封面上标题最大，配一组对比数字当钩子。

## 适用场景

| | 说明 |
|---|---|
| **适合** | 单篇实证论文（有图表和数字）；要发 X（4 张）或小红书（6–9 张）的图文；重视数字出处的科普 |
| **不适合** | 合法渠道拿不到全文时（技能只会帮你起草索取单行本的邮件，不替你发）；纯理论或纯综述、没有可核对数字的内容；想要全自动发布（技能不替用户发帖，成品交给你自己发） |

和「直接让大模型总结论文」或「让图像模型画信息图」相比，方法上的差别有三处：事实表里每个数字必须有出处；数据图一律用代码画，不让图像模型画坐标轴和数字；成图要过强模型评审，忠实度 P0 不清零不交付。

## English

**paper-reader** is an agent skill (for Claude Code and similar agents) that turns an academic paper into a faithful, readable illustrated carousel for X or Xiaohongshu. It obtains the full text through legal channels only (open-access APIs, author pages, free supplementary materials, OA commentaries; never shadow libraries), treats press releases as leads rather than data, builds a sourced fact table, follows the five-agent PaperBanana pipeline (Retriever → Planner → Stylist → Visualizer → Critic), draws every data chart in code, and blocks delivery until a strong reviewer model (e.g. Claude Opus) clears all faithfulness P0 issues. Final images are typeset with [Kami](https://github.com/tw93/Kami). Keywords: paper explainer, research paper to infographic / carousel, science communication, Claude Code skill, open-access only. Usage: ask your agent, e.g. "Read this paper and make an X carousel titled …". The skill itself is written in Chinese.

## 安装

1. 把 `SKILL.md` 放进你的 agent 的 skills 目录，例如 Claude Code：

   ```bash
   mkdir -p ~/.claude/skills/paper-reader
   curl -L -o ~/.claude/skills/paper-reader/SKILL.md \
     https://raw.githubusercontent.com/ythx-101/paper-reader/main/SKILL.md
   ```

   其他读取 `~/.agents/skills` 等目录的 agent 同理。

   也可以用 `git clone`（会连 `examples/` 一起带上，仓库根目录的 `SKILL.md` 直接就是 skill 目录）：

   ```bash
   git clone https://github.com/ythx-101/paper-reader ~/.claude/skills/paper-reader
   ```

   如果你的 agent 读的是 `~/.agents/skills`，换成那个目录。

2. 安装 Kami（出图依赖，见 [Kami 的安装说明](https://github.com/tw93/Kami#install)）：

   ```bash
   npx skills add tw93/kami -a claude-code codex cursor -g -y
   ```

3. 准备一个能当评审的强模型（如 Claude Opus）。有浏览器自动化工具会更顺利，因为很多期刊的补充材料需要在页面上点按钮下载。

然后对 agent 说：「读这篇论文，做成 X 组图，标题是……」。

## 快速开始

对 agent 说（任选一句）：

- 「读这篇论文 https://doi.org/10.1126/science.aak9726 ，做成 X 组图，标题是『赢过的人更容易再赢』」
- 「把这篇论文做成小红书图文，标题是……」
- 「用 PaperBanana 的方法把这篇论文做成图解：<论文链接或 DOI>」

agent 会在工作目录里依次生成：

- `fulltext/paths.md`：每一级获取原文途径的结果（成功、失败、原因）；
- `facts.md`：带出处的事实表；
- `plan.md`：每张图的画面描述；
- `reviews/`：每一轮强模型评审的结果；
- 最终的 PNG 成品图。

`facts.md` 里的一行大致是这样（结论 | 数字 | 出处 | URL）：

```text
被帮赢 6–20 次的小鼠保住名次 | 11/11 | Table S1 | https://doi.org/10.1126/science.aak9726
```

> 字体提示：Kami 默认的中文字体 TsangerJinKai02（仓耳今楷）仅限个人免费使用，商用需向 [tsanger.cn](https://tsanger.cn) 取得授权。

## 案例：胜利者效应（Science 2017）

论文：Zhou T, Zhu H, Fan Z, … Hu H. *History of winning remodels thalamo-PFC circuit to reinforce social dominance.* **Science 357:162–168 (2017).** DOI: [10.1126/science.aak9726](https://doi.org/10.1126/science.aak9726)。浙江大学胡海岚团队。

研究发现：小鼠在窄管里对推比赛，用光遗传激活背内侧前额叶（dmPFC），排名靠后的小鼠能赢过原先的强敌；被帮着赢得足够多次之后，即使撤掉帮助，新名次也能保住。被反复胜利强化的，是丘脑背内侧核 → 前额叶（MDT→dmPFC）这条通路。

| 1/4 钩子 | 2/4 实验 | 3/4 机制 | 4/4 结论与启发 |
|---|---|---|---|
| ![胜利者效应 X 组图 1/4：钩子页](examples/winner-effect-1.jpg) | ![胜利者效应 X 组图 2/4：实验页](examples/winner-effect-2.jpg) | ![胜利者效应 X 组图 3/4：机制页](examples/winner-effect-3.jpg) | ![胜利者效应 X 组图 4/4：结论与启发页](examples/winner-effect-4.jpg) |

### 忠实度：从 7 分改到 9 分

第一版四张图交给 Claude Opus 评审，忠实度都只有 7 分左右，共 10 条必改项。例如：

- 「1 条记住胜负的通路」：「1 条」不是论文的统计量，「记住」是拟人化；
- 「刺激前额叶后」太泛，没写清是光遗传激活 dmPFC；
- 步骤里写了「顶得更久」「按胜场排出稳定名次」，这些细节超出了原文。

逐条改完后第二轮评审，四张图忠实度都到了 9 分，没有必改项。

### 新闻稿写错了分组

但评审只能核对我们给它的事实表，而那份事实表一开始是照新闻稿整理的。新闻稿的说法是「被帮着赢 >6 次的保住名次、<5 次的退回」，读起来像是 5–6 次被单独留空。

后来从 Science 官方免费的补充材料（Table S1）和一篇开放获取的 Current Biology 评论（转载了原文 Fig. 4）里拿到真实数据，才发现原文的分组是 **2–5 次和 6–20 次两组，中间没有空档**：

- 被帮赢 2–5 次：13 只里 4 只保住名次；
- 被帮赢 6–20 次：11 只全部保住（p = 0.00048）。

同样，「90%」也不是逐场胜率，而是「相位 100 Hz 光激活方案下，10 只弱鼠里 9 只名次上升」。换一种刺激方案，数字就不同（持续 5 Hz 是 8/10，1 Hz 是 2/7）。

于是事实表按原始数据重写，每一行补上图表编号和来源，四张图重做，又跑了两轮评审：用真实数据的第一版评审出了新的 P0（比如把「推挤更多」这个自然赢家的结果错安到光激活组头上），全部修掉之后才定稿。这也是这个技能最重要的两条规矩的来历：**新闻稿只当线索；评审之外，事实表本身也要有出处。**

## 常见问题

**怎么让 Claude Code 把一篇论文做成图解或小红书图文？**
装好技能和 Kami（见上面的安装），然后对它说「读这篇论文，做成 X 组图（或小红书图文），标题是……」，并给出论文的链接或 DOI。它会依次取原文、整理事实表、出图、评审，最后交出 PNG。

**会用 Sci-Hub 吗？拿不到全文怎么办？**
不用。技能只走合法途径：开放获取聚合 → 作者渠道 → 免费补充材料 → 开放获取的评论与综述 → 学位论文 / 机构库。都拿不到时，它会起草一封给通讯作者索取单行本的邮件，交给你过目，不会替你发。

**只有新闻稿可以吗？**
不行。新闻稿只当线索，上图的数字必须回到原文、补充材料或转载原图的正式出版物核对（案例里就有新闻稿写错分组的例子）。

**除了 Claude Code，Codex / Cursor 等其他 agent 能用吗？**
读取 `~/.agents/skills` 等目录的 agent 同理安装；技能要求 agent 能读写文件、跑 Python。Kami 的安装命令里带了 `claude-code codex cursor`。

**需要哪些依赖？**
[Kami](https://github.com/tw93/Kami)（排版与出图）、能跑 Python 的 agent、一个当评审的强模型（如 Claude Opus）。浏览器自动化工具是可选的，但拿期刊补充材料时会顺利很多。

**图里的字体能商用吗？**
Kami 默认的中文字体 TsangerJinKai02（仓耳今楷）仅限个人免费使用，商用需向 [tsanger.cn](https://tsanger.cn) 取得授权。

**PaperBanana 是什么？是谷歌官方产品吗？**
PaperBanana / PaperVizAgent 是 Google Cloud AI Research 与北京大学的研究工作（arXiv [2601.23265](https://arxiv.org/abs/2601.23265)），不是 Google 官方支持的产品。本技能的五角色出图流程来自它。

## 致谢

- **PaperBanana / PaperVizAgent**：本技能的五角色出图流程来自这项工作。arXiv [2601.23265](https://arxiv.org/abs/2601.23265)，代码 https://github.com/google-research/papervizagent。它是 Google Cloud AI Research 与北京大学的研究，不是 Google 官方支持的产品。
- **Kami**：https://github.com/tw93/Kami ，作者 [@HiTw93](https://x.com/HiTw93)，MIT 协议。本技能的排版、配色和 PNG 输出都基于 Kami。
- 案例论文：Zhou et al., *Science* 357:162–168 (2017)，以及 Qu & Dreher, *Current Biology* 28:R167–R169 (2018)，[10.1016/j.cub.2018.01.018](https://doi.org/10.1016/j.cub.2018.01.018)。示例图只用于展示方法，数据版权归原作者与出版方。

## 作者

青月 · X [@YuLin807](https://x.com/YuLin807) · GitHub [ythx-101](https://github.com/ythx-101)

## 许可

[MIT](LICENSE)
