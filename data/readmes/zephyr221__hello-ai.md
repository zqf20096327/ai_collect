# Hello, AI · 人工智能导论

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE) [![Content: CC BY-NC-SA 4.0](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

> 在线地址：https://ai4edu.sjtu.edu.cn/helloai/ ·「AI+教育」平台的第一门课

一本写给所有人的 AI 入门书，附十二个在浏览器里运行的实验、十四章各一套的 HTML 幻灯片，以及 2026 年春季学期的随课幻灯片与讲义。
2026-09-02 由 Claude Fable 5.1 重写：正文、术语表、「此刻」页、站点设计与代码；实验保留自 2026 年 2–6 月的版本。

## 许可与开源

代码 MIT（`LICENSE`）；课程内容（正文、专题、术语、示意图、插画与提示词）CC BY-NC-SA 4.0（`LICENSE-CONTENT.md`）；
随课讲义与十四章讲义版幻灯片同样 CC BY-NC-SA；2026 年春的随课图片幻灯片与课堂 PDF 属于主讲教师，不在公开仓库内。公开仓库：https://github.com/zephyr221/hello-ai 。从工作副本导出公开版本：`bash scripts/export_public.sh`。

## 内容结构

```
content/
├── course.yaml          站点与课程元数据：四个部分、三种读法、署名
├── chapters/NN-slug.md  十三章正文 + tNN-slug.md 拓展专题（number 从 101 起，part: topics）
├── glossary.yaml        95 条术语，按章归属，related 互链 → 术语表 + 概念地图
├── labs.yaml            12 个实验的元数据（标题、时长、所属章、路由名）
├── lectures.yaml        随课六讲的元数据（讲义文件、幻灯片 slug、PDF）
├── lectures/*.md        随课讲义（2026 春，Claude Opus 4.6 撰写；---SECTION--- 分节）
├── now.md               「此刻」：会过时的内容，顶部标日期
└── about.md             关于页
```

没有数据库。`apps/reader/content.py` 在首次请求时解析全部内容并缓存；`DEBUG=True` 时按文件 mtime 自动刷新。

### 章节 Markdown 的自定义块

都以 `::: 类型 参数` 开头、单独一行 `:::` 结束，可嵌套：

| 块 | 用途 |
|---|---|
| `::: deep 标题` | 「深入」段落：主线模式折叠、全文模式展开；自动计入深入时长与目录 |
| `::: note 标题` / `::: warn 标题` / `::: aside` | 旁注、提醒、边注 |
| `::: check` | 自测：编号列表，每题下用 `>` 写答案，渲染成可展开的答案 |
| `::: lab 实验slug` | 嵌入实验卡片，块内可写一句引导语 |
| `::: snapshot 2026-09` | 带日期的时效内容 |
| `::: figure 说明` | 居中的图 / ASCII 示意 |
| `::: svg 名字 \| 图注` | 内联 `content/figures/名字.svg`，继承站点变量（深色模式可用） |
| `::: img 文件 \| 图注` | `static/images/book/` 下的位图，块内可写来源；文件不存在时静默跳过 |

正文里的 `## ` 标题进入本章目录；阅读时长按每分钟 300 字估算（主线 / 深入分开），自测按每题一分钟。

### 三种读法

- **主线**：只读正文段落，深入块折叠（`localStorage` 记住选择，`?mode=core|full` 可指定）。
- **全文**：展开所有深入块 + 自测 + 实验。
- **随课**：`/lectures/` 六讲讲义 + `/slides/` 幻灯片（带逐页讲者备注与 AI 伴学）。
- **放映**：`/slides/<章 slug>/` 讲义版幻灯片，见下。

## 页面

| URL | 说明 |
|---|---|
| `/` | 首页：首屏是从本站正文统计的字级二元模型现场生成文字（`/api/bigram.json`） |
| `/read/` · `/read/<slug>/` | 目录与章节 |
| `/glossary/` · `/graph/` | 术语表 · 概念地图（术语为节点、related 为边，纯 SVG 力导向） |
| `/now/` · `/about/` | 此刻 · 关于 |
| `/slides/` · `/slides/<章 slug>/` | 幻灯片索引 · 讲义版幻灯片（十四套） |
| `/lectures/` · `/lectures/<slug>/` · `/slides/<讲次 slug>/` | 随课（讲义与春季图片版幻灯片） |
| `/demos/` · `/demos/<lab>/` | 实验室（12 个实验，模板沿用 Tailwind 运行时，外壳为 `lab_base.html`） |
| `/api/chat/` | 伴读：SSE 流式，OpenAI 兼容上游（默认交大 models.sjtu.edu.cn），带当前章节上下文 |
| `/paths/...` | 旧学习路径地址，301 → `/lectures/` |

## 技术

Django 5.2（无数据库、无 admin、无 session）· python-markdown · KaTeX（本地）· 自托管字体（Noto Serif SC / Inter / JetBrains Mono）· 站点样式 `static/css/site.css`，实验页保留 `tailwindcss.js` 运行时与 `ai_labs.css`。所有资源本地托管，无 CDN。

## 幻灯片

两套并存，共用 `/slides/<slug>/` 这一个地址：slug 是章节 slug 就走**讲义版**（2026 秋），是讲次 slug 就走**随课版**（2026 春的图片版，原样保留）。

讲义版每章一个模板 `templates/decks/<章 slug>.html`，继承 `templates/decks/_base.html`（自动生成封面页与「这一章留下什么」小结页），样式 `static/css/deck.css`，控制 `static/js/deck.js`。页面是固定的 1280×720，靠 `--k` 整体缩放，所以在任何屏幕上都是同一份排版。配图与示意图直接引用正文那一批：位图用 `static/images/book/`，SVG 用 `{% svgfig "名" %}` 内联 `content/figures/` 下的同一个文件，因此会继承每一部分的主色。

| 键 | |
|---|---|
| `← → 空格` | 翻页，一次一整页（页内元素依次淡入） |
| 数字 + 停顿 | 跳到第 N 页 |
| `O` / `N` | 缩略总览 / 讲者备注抽屉 |
| `F` / `P` | 全屏 / 打印或导出 PDF（每页一张） |
| `S` | 改成一步一点（`.step` 逐个揭开），选择记在 localStorage |

手机上也能放：竖屏窄屏时 `deck.js` 给 `<body>` 加 `is-rot`，`.cell` 的 transform 里 `--rot` 变成 `90deg`，整张 16:9 的纸转过来铺满屏幕（`--k` 从 0.30 涨到 0.53，字大一倍）；控制条、备注、总览不跟着转。点右半边或沿幻灯片自己的水平方向上滑翻页——转过来之后那个方向就是屏幕的上下，所以 `deck.js` 里按 `rotated` 换算 `along`/`across`。底下窄控制条里的「转向」可以手动切回横排，转动手机会回到自动判断。窄屏时讲者备注改成底部推上来的一层（`#stage` 收成 `54dvh`），总览两列。

内容特别多的页面加 `class="slide dense"`，整页收一档，不要单独改某一处的字号。改完模板要**重启 runserver**（`--noreload` 不会重读模板），再用无头 Chrome 逐页量一遍有没有压到页脚。

## PDF 版

```bash
.venv/bin/python scripts/build_pdf.py     # → static/book/hello-ai.pdf + hello-ai.json（页数等元数据）
```

用 `templates/print/book.html` + `static/css/print.css` 渲染印刷版，无头 Chrome 打印，PyMuPDF 加页码、页眉、书签、目录页码并做字体子集。内容改动后重新跑一次再部署。

## 本地开发

```bash
cd helloai
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
DJANGO_SETTINGS_MODULE=config.settings.development .venv/bin/python manage.py runserver 8765
```

改 `content/` 下任何文件，刷新即生效。

## 部署

服务器 `pj2-ext`，路径 `/opt/helloai/`，虚拟环境 `/opt/helloai_env/`，socket `/run/helloai.sock`，systemd `helloai.service`，环境文件 `/etc/helloai.env`（`DJANGO_SECRET_KEY`、`AI_API_*`）。nginx 片段在 `deploy/nginx-helloai.conf`（线上 `helloai-location.conf`，用 `APPLY=1 bash scripts/sync-nginx-snippets.sh` 推送）。

```bash
# 打包（在仓库根目录）
COPYFILE_DISABLE=1 tar czf /tmp/helloai.tar.gz \
    --exclude='.venv' --exclude='venv' --exclude='__pycache__' --exclude='*.pyc' \
    --exclude='.mnist_cache' --exclude='static_collected' --exclude='db.sqlite3*' \
    --exclude='teachingsource_new' --exclude='.claude' --exclude='.DS_Store' \
    helloai/
scp /tmp/helloai.tar.gz pj2-ext:/opt/
ssh pj2-ext 'set -e; cd /opt && cp -a helloai helloai.bak-$(date +%Y%m%d-%H%M) && tar xzf helloai.tar.gz && find helloai -name "._*" -delete && rm -rf helloai/static_collected && cd helloai && set -a && . /etc/helloai.env && set +a && export DJANGO_SETTINGS_MODULE=config.settings.production && /opt/helloai_env/bin/python manage.py check && /opt/helloai_env/bin/python manage.py collectstatic --noinput && systemctl restart helloai'
```

两处别省：macOS 的 tar 会把扩展属性写成 AppleDouble，Linux 上解出来就是一堆 `._xxx.md`，`_load_chapters()` 读到就抛 `UnicodeDecodeError`，整站 500——所以打包要 `COPYFILE_DISABLE=1`，解包后再 `find helloai -name "._*" -delete` 兜一道。

`check` 与 `collectstatic` 都要先 `. /etc/helloai.env`（production 设置里没有 `DJANGO_SECRET_KEY` 会直接报 `ImproperlyConfigured`），并带 `DJANGO_SETTINGS_MODULE=config.settings.production`（否则没有 `STATIC_ROOT`）。

## 实验室（沿用）

12 个实验的算法都是真实实现：K 近邻、曲线拟合与梯度下降、网约车全流程、数据陷阱、神经网络 Playground、MNIST 卷积网络（纯 JS 推理，99.6%）、Tokenizer（GPT-2 / cl100k / o200k 真实词表的 BPE）、词向量、Attention、下一个词预测、A*、Q 学习迷宫。训练与导出脚本在 `scripts/`。
