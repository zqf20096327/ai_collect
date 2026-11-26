<p align="center"><strong>简体中文</strong> · <a href="README.en.md" lang="en">English</a></p>

<h1 align="center"><img src="media/pigeonhole-masthead.png" width="100%" alt="文件鸽 · Pigeonhole，下载时自动命名，按项目归档"></h1>

<p align="center">在 Chrome 或 Edge 下载论文、采购附件、报表或设计素材时，文件鸽会趁网页还没关，结合来源页面给文件起名，按规则、标签组或 AI 建议把它放进项目文件夹；隔几天忘了文件名，也能凭当时的网页线索找回来。</p>

<p align="center"><a href="https://chromewebstore.google.com/detail/pigeonhole/ikjdcjgnlbealhahlogjidahhhlbcdhp?hl=zh-CN"><img src="media/install-chrome.png" width="206" height="46" alt="在 Chrome 应用商店安装文件鸽"></a>&nbsp;&nbsp;<a href="https://microsoftedge.microsoft.com/addons/detail/pigeonhole/khbknbmdpigbjgojdodfelfgcnnjnljc?hl=zh-CN"><img src="media/install-edge.png" width="206" height="46" alt="在 Microsoft Edge 加载项安装文件鸽"></a><br>
<sub>无需注册 · 不上传文件内容 · 永不覆盖或删除文件 · 可试用内置 AI，也可填入自己的兼容 API Key 免费不限次直连</sub></p>

<p align="center"><a href="#功能一览">功能一览</a> · <a href="#用网页线索找回下载">找回下载</a> · <a href="#界面导览">界面导览</a> · <a href="#归档规则示例">规则示例</a> · <a href="#第一次下载">第一次下载</a> · <a href="#常见问题">常见问题</a> · <a href="docs/lite.md">Lite 版</a></p>

## 功能一览

| 下载时遇到的事 | 文件鸽能帮你做什么 |
| --- | --- |
| 同一页挂着好几个「附件」 | 结合每个下载链接附近的文字分别起名，把「附件1」「附件2」变成「采购需求书」「评分细则」「合同模板」。原名已经清楚的文件保持不动。 |
| 一个项目的资料散在好几个网站 | 用浏览器标签组把它们归进同一项目，也可以用规则固定去向，或让 AI 建议。没有匹配项目时，可按文件类型归类或放入待确认目录。 |
| 指定网站的原始编号必须保留 | 在「不改名的网站」中添加该站点。文件仍可归档，交材料时能对上对方的原始文件名。 |
| 想在下载网页上直接调整去向 | 网页右上角的下载卡片会实时显示进度、新文件名和目标文件夹。放错时，当场点「换个文件夹」或「撤销」即可恢复原样。 |
| 项目已经有自己的本机文件夹 | 编辑项目时选「改到电脑上的文件夹…」，在浏览器选择器中指定已有目录。例如，给展览项目选好存放印刷稿的文件夹，后续整理素材就能直接沿用。 |
| 隔了一阵子想不起文件名叫什么 | 在工具栏面板按网页标题、链接文字或「上周 PDF」等场景词本机秒搜，也可点「AI 帮我找」用大白话定位文件，并直接在浏览器只读打开。 |

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="media/download-demo-still.png">
  <img src="media/download-demo.gif" alt="下载整理示例：公告里的附件2.pdf 保存为青禾采购文件夹里的图书馆设备采购_评分细则.pdf">
</picture>

## 用网页线索找回下载

隔几天忘了文件名时，可以用下载当时的网页线索找回文件鸽处理过的记录。

比如，想找回上面那份图书馆采购附件，打开工具栏面板，在「最近」里输入 `评分` 就能找到评分细则。如果只记得「上周停车场招标的那份 PDF」，也可以搜 `上周 PDF 停车`。时间和类型会成为筛选条件，「停车」会匹配文件名、来源页标题或保存的下载链接文字。关键词搜索全程在本机离线完成，还可以按文件最后确认的位置筛选。

<p align="center"><a href="media/find-download.png"><img src="media/find-download.png" width="440" alt="在工具栏面板搜索「评分」，找到青禾采购的评分细则 PDF。面板也提供「AI 帮我找」。截图使用示例记录。"></a></p>

- **回到原网页找附件。** 再次打开下载过文件的网页，工具栏面板顶部的「这个网页下载过」会列出来自这一页的记录。
- **只记得大意时，用「AI 帮我找」。** 你主动点按钮并在首次使用时确认后，AI 才会收到你的描述（支持「上周三」「十天前」等相对时间）和本机选出的最多 30 条脱敏候选摘要，推荐最多 3 份文件并说明理由。「不使用 AI 的网站」及敏感站点会被自动排除，请求不包含文件内容、完整网址或本机路径。
- **找到后直接打开。** 对能定位并读取的 PDF、常见图片、纯文本及浏览器支持的音视频，可以从结果中点「在浏览器打开」只读查看。已移动到获授权项目文件夹的文件同样适用。
- **看清大文件究竟放在哪。** 外部归档通过流式分块校验确保大文件完整无损。记录会清晰区分已经放进目标文件夹、仍暂存在下载管理目录，以及位置待核对的状态，方便一键补放。

此外，在「项目与规则」中还支持**用一句话起草规则**——例如输入「把 arXiv 的论文放到毕业论文/文献」，检查 AI 生成的条件和目标文件夹后再保存（可在内置 AI 试用额度内使用，或填入自己的 API Key 免费不限次使用）。扩展在后台静默更新后，仅在打开面板时展示一次新版要点，绝不自动弹窗打扰，也可在设置中回看更新记录或关闭提示。

## 界面导览

以下界面使用示例文件和项目。点开图片可查看原图。

### 同一份公告，每个附件都有自己的名字

采购公告页上同时挂着采购需求书、评分细则和合同模板。文件鸽能利用网页提供的附件线索，把项目名和材料名一起保留下来。开会前在「青禾采购」里搜「评分细则」，就能直接找到要讨论的 PDF。

<details>
<summary>展开商店原图，看公告中的三个附件与保存结果</summary>

[![同一份公告下的三份附件分别带上项目名和材料名](media/store-attachments.png)](media/store-attachments.png)

</details>

### 在下载当场换文件夹

下载完成时，网页右上角的卡片会显示新文件名和去向。比如下面这份评分细则被归进「青禾采购」，点「在文件夹中显示」就能找到它，点「换个文件夹」可以另选项目。无法注入卡片的浏览器内置页仍可从工具栏查看记录。

如果项目资料已经放在电脑上的某个目录，可以在「换个文件夹」里选「选择电脑上的文件夹…」。浏览器会要求授权访问文件鸽的下载管理目录和目标文件夹；授权未完成前，文件安全留在下载管理目录。

<details>
<summary>查看网页上的下载卡片和换文件夹入口</summary>

<p align="center"><a href="media/download-controls.png"><img src="media/download-controls.png" width="420" alt="评分细则已归入青禾采购，卡片上可以在文件夹中显示、换个文件夹或撤销。"></a></p>

</details>

### 从最近记录找回与撤销下载

打开工具栏里的文件鸽即可查看近期下载。图中三份附件都进了「青禾采购」，第一行还保留着「撤销」入口。这一批都需要还原时，可以用「撤销本批」。需要在本机移动文件时，浏览器会按需提示授权。

<p align="center"><a href="media/recent-history.png"><img src="media/recent-history.png" width="440" alt="完整版最近记录示例，三份采购附件可逐项撤销，也可撤销本批"></a></p>

### 把这次的去向记成下次的规则

一次采购可能持续好几周。在归得合适的那条记录上选「更多 → 以后同类都这样」，来源、文件类型和项目就会带入规则编辑器。下面这条规则只收指定来源的 PDF，同网站的其他文件仍按各自的情况处理。检查后点「保存」，后续匹配的下载才会使用它。

<details>
<summary>看规则编辑器里的来源、文件类型和目标项目</summary>

<p align="center"><a href="media/filing-controls.png"><img src="media/filing-controls.png" width="420" alt="从一条示例下载生成的规则：指定来源网站的 PDF 放到青禾采购"></a></p>

</details>

## 归档规则示例

在「项目与规则」里先建一个项目，例如把「论文文献」放到 `毕业论文/文献`。项目文件夹最多支持两层，还可以填写相关网站、标签组和给 AI 参考的一句话描述。

点「新建规则」手动组合条件，或直接用一句话让 AI 起草规则草稿。多条规则重叠时，列表中排在前面的先匹配，可用「上移」「下移」调整优先级。

| 如果你在做这件事 | 可以这样设 |
| --- | --- |
| **写文献综述**，把论文和同站的其他下载分开 | 选「来源网站是」填 `arxiv.org`，再加「文件类型是」填 `pdf`，归入自己的「论文文献」项目。 |
| **筹备展览或收集 AI 创作素材**，参考图、平面图和印刷规格来自不同网站 | 给这些网页建一个「春季展览」标签组，使用「标签组是」来匹配。以后从组内网页下载，文件就有共同的去向。 |
| **整理月报与票据**，回头要按业务名称和日期查找 | 对标题或网址包含「客流月报」的下载指定「经营月报」项目，并在这条规则的「文件名」中选「日期在前」。 |
| **投标或交付**，文件要归档但不能丢掉对方的交付编号 | 在对应的来源规则里指定项目，把「文件名」选成「不改名」。同样适合需要按原编号提交的报名表或办事材料。 |

### 先测试一条规则，再用它收文件

打开「项目与规则 → 试一试」。选一条最近的下载，或填入网址和文件名，点「测试」就能看到哪条规则命中、其余规则为什么没命中。图中用 `paper-demo.pdf` 试算，结果显示「命中规则『arXiv 论文』」，预计放进 `下载/文件鸽/论文文献`。如果去向不对，可以改完条件再测，全程无需重新下载文件。

[![完整版规则测试示例，查看一份 PDF 会命中哪条规则](media/rule-preview.png)](media/rule-preview.png)

<details>
<summary>同一个网站同时服务两个项目，该按网站还是按标签组归档？</summary>

比如你正准备两门课，讲义都出自同一教务网站。可以把网页分别放进「统计学」「城市规划」两个浏览器标签组，各建一条按组匹配的规则。如果还有一条覆盖整个教务网站的规则，把两条更具体的规则移到它上面。分别从两个标签组各下载一份文件，再到工具栏面板核对去向。

</details>

## 第一次下载

1. 从 [Chrome 应用商店](https://chromewebstore.google.com/detail/pigeonhole/ikjdcjgnlbealhahlogjidahhhlbcdhp?hl=zh-CN) 或 [Microsoft Edge 加载项](https://microsoftedge.microsoft.com/addons/detail/pigeonhole/khbknbmdpigbjgojdodfelfgcnnjnljc?hl=zh-CN) 安装文件鸽，在欢迎页点击「开始使用」授予网页读取权限（用于区分同一页上的多个附件）。
2. 打开任意带「附件1」或编号式 PDF 的网页，像平常一样点击下载——在网页右上角卡片或工具栏面板查看改好的文件名与去向，不满意点一下「撤销」即可还原。
3. 遇到满意的归档结果，可在记录菜单里点「以后同类都这样」，或到规则页用一句话把规则固定下来。

## 常见问题

<details>
<summary><strong>能先看看论文、公告和图片会怎么命名吗？</strong></summary>

可以。在「命名与 AI」的命名示例中切换「论文」「公告」「图片」，对照原名和处理后的名字。例如，论文详情页的题目能给编号式 PDF 提供线索，作品页的标题能给相机流水号或 `image.png` 提供线索。

</details>

<details>
<summary><strong>哪些信息会发给 AI？会上传 PDF、图片或表格内容吗？</strong></summary>

文件内容绝不上传，扩展也永不覆盖、永不删除任何本地文件，不申请浏览历史（`history`）权限。下载起名与归档仅使用网页标题、脱敏网址、原文件名及授权后的链接附近少量文字；只有当你主动点击「AI 帮我找」并确认后，才会发送你的查找描述与最多 30 条本机候选摘要（不含文件内容、完整网址和本机路径）。网银、支付、医疗等敏感网站默认跳过 AI。设置、记录与下载现场均保存在本机，匿名次数统计可在设置中随时关闭。[文件鸽隐私政策](https://pigeonhole.tmlab.top/privacy?lang=zh)

</details>

<details>
<summary><strong>我只想临时停用，或少收一点通知，怎么设置？</strong></summary>

在「通用」里把「结果通知」改成「只在要确认时」。临时下载一批无需整理的文件时，可以选择「暂停 1 小时」或「暂停到今天结束」。

</details>

<details>
<summary><strong>需要注册或购买 API Key 吗？能用自己的模型服务吗？</strong></summary>

无需注册即可直接试用内置 AI（设体验与每日上限）。如果在设置中填入你自己的 DeepSeek、硅基流动等 OpenAI 兼容 API Key 或接入本地模型，AI 起名、AI 帮我找和一句话建规则全部免费且不限次数，请求直接发往你选择的服务商，不经过文件鸽服务器。

</details>

---

本仓库公开[文件鸽 Lite 版](docs/lite.md)源码；完整版可从 [Chrome 应用商店](https://chromewebstore.google.com/detail/pigeonhole/ikjdcjgnlbealhahlogjidahhhlbcdhp?hl=zh-CN) 或 [Microsoft Edge 加载项](https://microsoftedge.microsoft.com/addons/detail/pigeonhole/khbknbmdpigbjgojdodfelfgcnnjnljc?hl=zh-CN) 免费安装。<br>
问题反馈与交流：[加入用户群 / Discord](https://pigeonhole.tmlab.top/community?l=zh) · [在线反馈](https://pigeonhole.tmlab.top/feedback?l=zh) · [GitHub Issues](https://github.com/welsir/pigeonhole-lite/issues)
