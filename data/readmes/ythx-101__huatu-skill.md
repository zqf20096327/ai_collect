# 画图 Skill

画图 Skill（huatu-skill）是一个面向 Codex 等支持 `SKILL.md` 的 AI Agent 的视觉叙事 Skill：帮内容创作者把长文、研究笔记和草稿，做成可编辑、可验证的小红书图文轮播（1080×1350 PNG 信息卡片），或一个自包含的 ELI5 一页式 HTML 视觉解释器；本地渲染，交付前有 fail-closed 质检。

English: an agent skill (`SKILL.md`) that turns articles and research into Xiaohongshu (RedNote) carousel PNGs or self-contained ELI5 visual explainers, with local Playwright rendering and fail-closed QA.

> Constraints keep the page safe. Interpretation makes it meaningful.

![画图 Skill 示例](docs/preview/slide-01.png)

## 它解决什么

画图 Skill 先理解论点、关系与情绪，再选择两种产品路径之一：小红书轮播输出可编辑 JSON、HTML 预览、1080×1350 PNG 与 QA；ELI5 Visual Explainer 输出一个自包含响应式 HTML 与浏览器验证证据。**轮播的最终产品是 PNG；解释器的最终产品是 HTML。`--check-only` 对两者都只是预检**。

- 将长文章、研究笔记或已有草稿改写成 6–10 页轮播叙事
- 用可检查的 `designManifest` 记录视觉命题、隐喻、节奏与构图意图
- 支持 editorial、mixed、image-led、photo-diary、object-study、poetic-poster 六种视觉模式
- 知识型内容默认走 image-led / mixed 图文交替路径，并可复用 6 种 diagram SVG 模板表达流程、步骤、层级、时间、象限与对比关系
- 支持本地 PNG、JPEG、WebP、SVG，并赋予 hero、evidence、atmosphere 等语义角色
- 检查溢出、低对比度、重复构图、弱图像节奏与近期设计相似度
- 生成本地 HTML 预览和逐页 PNG，并用 fail-closed delivery checker 阻止缺图、陈旧渲染或 BLOCKED QA 被当成成品
- 生成 3–7 幕、低文案、大视觉的 ELI5 HTML 解释器，明确来源与简化边界
- 在真实 Chromium 的 390×844 与 1365×768 视口检查外部请求、横向溢出、小字和浏览器错误
- 把最终审美判断、手机验收与发布权留给人

## 适用场景与区别

| | 说明 |
|---|---|
| 适合 | 知识型、研究型、机制型的小红书图文；把一篇文章拆成 6–10 页的叙事；需要一页式、手机和桌面都能看的解释页 |
| 不适合 | 自动发帖或排期（本项目不做）；纯照片修图；需要 JavaScript 交互的网页 |

和其他做法的区别：

- 对比「直接让 AI 生图」：文字由 HTML/CSS 排版，产出可编辑的 JSON 源文件，再确定性渲染，所以中文排版可以修改、可以复现。
- 对比「手工套模板」：先写叙事和设计意图（`designManifest`），再按内容选择构图。
- 对比「普通 HTML 转图片工具」：多了溢出 / 对比度检查，以及 fail-closed 的交付门槛。

## 设计原则

1. 先写每页的叙事任务，再开始排版。
2. 图像必须承担意义，而不是给文字加一层装饰。
3. 规则是护栏，不是模板；内容变化应该带来构图变化。
4. 自动检查只能证明页面没有坏，不能证明它好看。
5. `--check-only` 不是交付；最后一次修改后必须重新渲染并逐页检查。
6. 不复制其他创作者的文字、水印、头像或标志性身份元素。

## 快速开始

1. 克隆到 skills 目录并安装渲染依赖：

```bash
git clone https://github.com/ythx-101/huatu-skill.git ~/.codex/skills/huatu-skill
cd ~/.codex/skills/huatu-skill
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
```

已经装了 Chrome/Chromium 的，可以用 `--browser <路径>` 或环境变量 `CHROME_BIN` 指定浏览器。其他支持 `SKILL.md` 的 Agent（例如 Claude Code 的 `~/.claude/skills/`）按各自的 skills 目录放置即可。

2. 在 Agent 里说一句话。轮播：

```text
使用 $huatu-skill，把这篇文章做成 8 页小红书图文。
先提出三种真正不同的视觉方向，选择后再渲染；加入有语义作用的图像，最后检查每一页和整组节奏。
```

ELI5 解释器：

```text
使用 $huatu-skill，用 ELI5 HTML 模式把这篇文章做成 5 幕的一页式视觉解释器。
```

3. Skill 会先选择产品模式。轮播路径完成：内容契约 → 分页叙事 → JSON spec → 本地渲染 → 逐页视觉 QA → fail-closed 交付检查。解释器路径完成：3–7 幕叙事 → 单幕单概念 → 自包含 HTML → 双视口 Chromium QA → 人工检查。

## ELI5 Visual Explainer

从安全起始文件开始：

```bash
cp assets/eli5-explainer-starter.html explainer.html
python3 scripts/check_explainer.py explainer.html --check-only
python3 scripts/check_explainer.py explainer.html --output-dir explainer-qa
```

真实浏览器命令生成 `qa.json`、`preview-mobile.png` 和 `preview-desktop.png`。HTML 只允许内联 CSS/SVG；不允许 JavaScript、远程字体/CDN、分析代码、网络资源、凭据、私有标识或二维码。参见 `references/eli5-html-mode.md`，以及可复现示例 `examples/eli5-moshi-hook.html` 和 `examples/eli5-moshi-browser-preview.html`。

## 轮播本地渲染

先检查结构：

```bash
python3 scripts/render_carousel.py examples/mixed-carousel.json \
  --output-dir rendered --check-only
```

再生成 HTML 和 PNG：

```bash
python3 scripts/render_carousel.py examples/mixed-carousel.json \
  --output-dir rendered --no-history
```

输出包括：

- `carousel.html`：可编辑的本地预览
- `slide-01.png` 等：1080×1350 图片
- `qa.json`：尺寸、溢出与诊断结果
- `design-manifest.json`：可检查的设计意图

渲染 PNG 需要 Playwright 与本地 Chromium（见「快速开始」）；仅做 JSON 结构检查不需要浏览器，但结构检查不能替代成品验收。

最终逐页检查后，写入 `qa-summary.md`，再运行：

```bash
python3 scripts/check_delivery.py examples/mixed-carousel.json \
  --output-dir rendered \
  --qa-summary qa-summary.md
```

只有输出 `release_ready: true` 才满足机械交付门槛；它仍不授权自动发布。

## 目录

```text
SKILL.md                      Skill 工作流
agents/openai.yaml            Codex 展示信息
assets/                       轮播与 ELI5 HTML 起始模板
references/                   叙事、构图、图像、交付与 QA 规范
scripts/render_carousel.py    轮播校验与渲染器
scripts/check_delivery.py     轮播成品包 fail-closed 交付检查
scripts/check_explainer.py    ELI5 HTML 静态与双视口浏览器检查
scripts/compare_directions.py 候选方向差异检查
tests/                        单元测试
examples/                     可复现示例
```

## 测试

```bash
python3 -m unittest discover -s tests -v
```

CI 中不运行浏览器测试（未安装 Playwright 时这些测试会自动跳过）。

## FAQ

**能直接发布到小红书吗？**
不能。Skill 不登录、不上传、不自动发布，发布需要人工操作。

**需要 API Key 或联网吗？**
Skill 自身的脚本在本地渲染，不需要额外的 API Key；除首次安装 Playwright 与 Chromium 需要下载外，渲染和检查不依赖网络。图片只接受本地文件，远程 URL 会被拒绝。Agent 本身所用模型如何计费，不在本项目范围内。

**没装 Playwright / Chromium 能用吗？**
只能跑 `--check-only` 结构预检，这不算交付；要渲染 PNG 或做浏览器 QA，必须装上。

**支持哪些尺寸？**
默认 1080×1350（4:5）。单张 3:4 封面可以设 `canvas: {"width":1080,"height":1440}`；宽高允许范围 720–2160。

**能改配色吗？**
默认是 Kami 主题，可以在 spec 里用 `theme` 覆盖（六位 hex 色值），见 `references/kami-design.md` 与 `references/spec-format.md`。

**支持哪些视觉模式？**
editorial、mixed、image-led、photo-diary、object-study、poetic-poster。

**能在 Claude Code 或其他 Agent 里用吗？**
它是标准的 `SKILL.md` 结构，可以放进对应 Agent 的 skills 目录；本文示例按 Codex 编写。

**ELI5 HTML 里能放 JavaScript 或外链字体吗？**
不能，只允许内联 CSS/SVG。

**`release_ready: true` 是不是就代表图好看？**
不是。它只证明机械门槛通过，审美判断和发布权在人手里。

**可以用别人的图吗？**
只使用原创、已授权或公有领域的素材。

## 隐私与版权

- 图片只接受本地文件路径，远程 URL 会被拒绝。
- Skill 不登录、上传或自动发布小红书；发布是独立的人工动作。
- 请只使用原创、已授权或公有领域素材，并自行核对事实与来源。

## License

MIT © 2026 QingYue
