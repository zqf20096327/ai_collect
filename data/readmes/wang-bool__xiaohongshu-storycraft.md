<div align="center">
  <img src="docs/images/hero.png" alt="xiaohongshu-storycraft，让内容决定构图" width="100%">
</div>

<p align="center">
  <a href="README_EN.md">English</a> ·
  <a href="LICENSE">Apache-2.0</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

<p align="center">
  <a href="https://skills.sh/wang-bool/xiaohongshu-storycraft/xiaohongshu-storycraft"><img src="https://skills.sh/b/wang-bool/xiaohongshu-storycraft" alt="skills.sh 安装量"></a>
</p>

# 小红书叙事工坊

把想法、文章、研究资料、截图或照片，制作成可直接发布的小红书图文。它会交付标题、正文、标签和逐页图片，不只给提纲或提示词。

这里没有预设的左右布局、上下布局或固定卡片库。每一页先确定读者需要理解什么，再根据真实素材的比例、焦点、信息密度和证据作用推导构图。

## 快速开始

### 安装

推荐使用通用的 Skills CLI 一键安装：

```bash
npx skills add wang-bool/xiaohongshu-storycraft
```

也可以下载整个仓库，将 `xiaohongshu-storycraft` 目录放进你的 Agent 可发现的 Skill 目录：

```bash
git clone https://github.com/wang-bool/xiaohongshu-storycraft.git
cp -R xiaohongshu-storycraft /path/to/your/agent/skills/
```

不同 Agent 的 Skill 目录和刷新方式并不相同，请以你所用工具的文档为准。目录内的相对结构需要完整保留：

```text
xiaohongshu-storycraft/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

如果你的 Agent 没有固定的技能安装机制，也可以直接让它读取本仓库的 [`SKILL.md`](SKILL.md)，并按其中的“按需读取参考”使用其他文件。

### 调用

不需要先挑模板。把材料交给 Agent，说明你准备发什么：

```text
请使用 xiaohongshu-storycraft，把这篇文章改造成一组可以直接发布的小红书图文。
保留原文中的技术事实，先给我看逐页命题，再生成图片。
```

```text
请使用 xiaohongshu-storycraft，根据这个照片目录整理一篇旅行记录。
不要编造我没有提供的经历，路线图和地点信息需要保留来源。
```

```text
请使用 xiaohongshu-storycraft，把测试记录、截图和结论做成小红书图文。
截图承担证据作用，不要用 AI 重绘。
```

## 案例，不是模板

下面三组图来自真实测试。产品叙事、技术实测和旅行记录之间没有固定的共同版式。它们放在一起，只为证明同一个 Skill 能根据不同内容重新组织视觉关系。输入也不限于这三类。

![三个实测案例，展示不同内容如何生成不同构图](docs/images/showcase.webp)

## 它会完成什么

- 区分事实、用户经历、图片可见内容和编辑性表达
- 把整篇材料拆成逐页命题，避免一页承担多个阅读任务
- 读取图片比例、焦点、信息密度和最小可读尺寸
- 判断每页由图片还是文字承担主要理解任务
- 从内容推导空间关系，不枚举或套用固定版式
- 使用 HTML 生成 1080×1440 的逐页图片
- 检查溢出、断行、图片比例、空白和画布边缘碰撞
- 交付标题、正文、标签、图片故事与来源说明

## 三条设计原则

### 少就是多

一个好 prompt 更像提示，不是密密麻麻的布局指令。模型已经具备构图能力，Skill 需要补充的是专业判断：图片是否已经把事情讲清楚，哪些内容必须完整保留，文字应当补充什么，读者的注意力该落在哪里。

自由度需要边界。这个 Skill 约束事实、图片完整性、配色角色、文字可读性和画布质量，但不规定图片必须放左边还是上面。约束负责守住底线，构图仍由本页内容决定。

### Loop Engineering

生成图片不是流程终点。HTML 会先经过浏览器 DOM 检查，再渲染成 PNG，并继续检查比例、分辨率、连续空白和边缘碰撞。可以描述清楚的错误交给程序检测，模型根据结果修改后再次运行。

### Human in the Loop

尺寸和溢出可以自动测量，审美、事实边界、隐私与版权不能交给一个分数决定。Skill 会尽量替用户完成日常判断，但当页面命题存在多种实质解释时，会先确认方向。最终图片仍需要人看一遍。

![从素材理解到人工确认的制作循环](docs/images/workflow.svg)

## 内容如何变成页面

1. 从材料中划出事实边界，避免补造体验、效果、数字和出处。
2. 为整组图片安排叙事顺序，每页只保留一个主要阅读任务。
3. 逐张分析图片，让真实比例和视觉焦点参与空间计算。
4. 选择一套视觉宪法。宪法管理色彩、字体和空间气质，不提供页面骨架。
5. 把真实文字和图片放进 HTML，根据实际剩余空间继续调整。
6. 运行浏览器渲染、DOM QA 和 PNG QA，再逐页人工查看。

## 本地依赖

- Python 3.10 或更高版本
- Pillow
- Google Chrome 或 Chromium，用于 HTML 渲染和 DOM QA

安装 Python 依赖：

```bash
python3 -m pip install -r requirements.txt
```

把 deck HTML 渲染为逐页 PNG：

```bash
python3 scripts/render_deck.py path/to/deck.html -o path/to/rendered
```

单独检查图片目录：

```bash
python3 scripts/qa_deck.py path/to/rendered
```

分析素材中的候选主色：

```bash
python3 scripts/field_color.py path/to/image.png
```

## 自定义视觉风格

现有视觉宪法位于 [`references/styles/`](references/styles/)，包含纸感编辑、墨色信息图、清新生活方式、极简黑白、波普海报和暗调电影氛围。

增加新风格时，请写一部新的视觉宪法，并在 [`references/visual-constitutions.md`](references/visual-constitutions.md) 注册。风格文件应该描述色域、字体关系、空间气质和适用判断，不应保存某张成品的坐标、容器尺寸或固定版式。

## 项目结构

```text
.
├── SKILL.md                     # Agent 执行入口
├── agents/openai.yaml           # 可选的界面元数据
├── assets/deck-template.html    # 视觉 Token 与语义原子
├── references/                  # 内容、构图、配色和制作规则
│   └── styles/                  # 可扩展的视觉宪法
├── scripts/
│   ├── render_deck.py           # HTML 分页渲染
│   ├── qa_deck_html.py          # 浏览器 DOM 检查
│   ├── qa_deck.py               # PNG 检查
│   └── field_color.py           # 素材色彩分析
└── tests/                       # 单元测试与发布契约
```

## 边界

- 不自动发布到小红书。发布需要独立的平台连接、账号授权和最终确认。
- 不把未提供的经历、数据、引语或来源写成事实。
- 不用 AI 重绘包含关键文字、按钮、数据或界面关系的截图来充当证据。
- 没有图片生成能力时仍可使用 HTML、真实素材、拼图、调色和文字页完成制作。
- 自动 QA 只能发现可测量的问题，不能证明一张图在审美上成立。

## 展示素材说明

README 展示图片来自作者的实测项目。图片中出现的产品名、商标、界面与第三方素材归各自权利人所有，仅用于说明该 Skill 的实际输出，不表示任何品牌背书。

## 参与贡献

欢迎提交问题、修复、质量检查规则和新的视觉宪法。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。成品版式不会被收录为可复用模板，但从真实失败中提炼出的构图原则和检查方法很有价值。

## License

Copyright 2026 [wang-bool](https://github.com/wang-bool)

Licensed under the [Apache License 2.0](LICENSE).

## 关注与交流

如果你对 AI、AI Coding、Agent 架构，或这个 Skill 的使用与改进有想法，欢迎关注公众号“王不二丶bOol”或加入交流群。

| 微信公众号 | AI Agent 交流群 |
| :---: | :---: |
| <img src="docs/images/wechat-official-account.jpg" alt="王不二丶bOol 微信公众号二维码" width="300"> | <img src="docs/images/wechat-group.png" alt="AI Agent 交流群二维码" width="300"> |

> 群二维码可能过期。如果无法识别，请关注公众号获取最新入群方式，或添加作者微信 `wang_bool`。
