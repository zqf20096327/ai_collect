# Wills' Mineral Processing Technology — Chinese Translation Project

An open, continuously-updated unofficial Chinese translation of *Wills' Mineral Processing Technology (8th Edition)*. It is built for human reading and, at the same time, for use as vectorised domain knowledge inside a mineral-processing AI Agent.

---

## Why This Project Exists

Undergraduate mineral-processing (ore-dressing) programmes in mainland China have long been taught from textbooks that trace back, directly or indirectly, to Soviet-era teaching material written decades ago. Those textbooks suffer from three problems that have become increasingly hard to ignore:

- They are hard to read — dense, convoluted prose that treats students as passive readers instead of future engineers.
- They are out of date — written before the modern wave of large-scale equipment, process automation, sensor-based sorting, advanced process control, and geometallurgy.
- They are narrow in outlook — with little connection to the industrial practice and commercial equipment that a practising engineer actually meets on the job.

While searching for a better foundation, I came across **Wills' Mineral Processing Technology**, by Barry A. Wills and James A. Finch (8th Edition, Elsevier). It is lucid, rigorously structured, richly illustrated, and tightly connected to how modern processing plants are really designed and operated. It is, in my view, an excellent textbook — and it deserved to be read in Chinese, and read properly.

That is why I began translating it: chapter by chapter, faithfully, using the terminology that a Chinese mineral-processing engineer actually uses.

## Beyond a Translation: A Step Toward a Domain AI Agent

The mineral-processing industry is underserved by specialised artificial intelligence. A genuinely useful domain Agent must be grounded in real, structured professional knowledge — and **vectorising authoritative technical literature is a large part of that foundation**.

This project therefore treats the translation as more than just a document:

- The source textbook is converted from scanned pages into **structured Markdown via OCR**;
- The translation preserves the **heading hierarchy, equations, tables, and figure placeholders**, so the text stays cleanly chunkable and embeddable;
- A generated **master table of contents** keeps the entire book navigable and indexable.

In this way, the repository is intended to become part of the **base knowledge database for a mineral-processing AI Agent** — and the project itself will keep being updated and improved as that effort progresses.

## What's Inside

| Path | Content |
| :-- | :-- |
| `Wills Mineral Processing Technology 矿物加工技术/` | One folder per chapter / appendix, each holding the original PDF, the OCR'd Markdown, and the Chinese translation file (`（中文版）.md`) |
| `…/（中文版）.md` files | The full Chinese translations — front matter, 17 chapters, and 5 appendices (23 units in total) |
| `《Wills矿物加工技术》全书中译本·结构化总目录.md` | An auto-generated master index of 600+ headings, multi-level, with cross-file jump links |
| `_翻译规范_中译本说明.md` | An internal style guide that keeps future chapters consistent — terminology, formula syntax, and layout rules |

## Status

- ✅ Front matter, Chapters 1–17, and Appendices I / III / IV / V / VI are translated and committed.
- ✅ Translation style: standard professional Chinese mineral-processing terminology; English terms given on first occurrence; equations rewritten so they render cleanly in Typora / MathJax; every original figure flagged with a `【插图位置 · 图 N.M】` marker so images can be inserted later.
- 🚧 This is a living project. Content will be reviewed, polished, corrected, and extended over time.

## How to Use

- Open any `（中文版）.md` in **Typora** (or VS Code, Obsidian) for comfortable reading with maths rendering.
- Use the master `…结构化总目录.md` as the entry point — every heading links back to its source chapter.
- For AI / Agent use: the structured Markdown is ready to be fed into chunking and embedding pipelines.

## Notes

- This is an **unofficial, non-commercial, educational** translation. The original work and all rights belong to **Elsevier Ltd. and the authors**. Please do not redistribute it for commercial purposes.
- OCR inevitably introduces noise. Each chapter is cleaned during translation, but errors remain — corrections and contributions are very welcome.

---

# 《Wills 矿物加工技术》中文译本项目

这是一个开放、持续更新的《Wills 矿物加工技术（第 8 版）》非官方中文译本。它既为专业读者阅读而译，同时也准备用作选矿专业 AI Agent 内部的向量化领域知识。

---

## 项目缘起

我国矿物加工工程专业的本科教学，长期以来使用的教材大多直接或间接源于几十年前苏联时代编写的教学内容。这些教材存在三个日益难以回避的问题：

- **晦涩难懂。** 行文繁复拗口，把学生当作被动的阅读者，而不是未来的工程师。
- **严重过时。** 它们写成于大型化装备、过程自动化、传感器分选、先进过程控制与地质冶金学等现代技术浪潮之前。
- **视野狭窄。** 与现场工程师真正接触到的工业实践和商业设备之间，缺少应有的联系。

在寻找更好的专业基础时，我读到了 **Wills《Mineral Processing Technology》**——Barry A. Wills 与 James A. Finch 合著，Elsevier 出版，第 8 版。这本书行文清晰、结构严谨、图文并茂，并且与现代选矿厂真实的设计与运行方式紧密相连。在我看来，它是一本非常优秀的教材——它值得被译成中文，并且译得规范、译得用心。

这正是我开始翻译它的原因：逐章推进、忠实于原文，并使用中国矿物加工工程师真正使用的专业术语。

## 不止于翻译：走向领域 AI Agent 的一步

选矿行业目前缺少真正专业的专用人工智能。一个真正能胜任工作的领域 Agent，必须建立在真实、结构化的专业知识之上——而**对权威技术文献进行向量化，正是这项基础工作中很大的一部分**。

因此，本项目并不把这份译本仅仅当作一份文档：

- 原书经扫描后，先通过 **OCR 转化为结构化的 Markdown**；
- 翻译时完整保留**标题层级、公式、表格与插图占位**，使文本能够被干净地分块（chunking）与向量化（embedding）；
- 另生成一份**全书结构化总目录**，使整本书始终可导航、可索引。

这样一来，本仓库拟作为**选矿专业 AI Agent 的基础知识库**的一部分——而项目本身也会随着这项工作不断更新与完善。

## 仓库内容

| 路径 | 内容 |
| :-- | :-- |
| `Wills Mineral Processing Technology 矿物加工技术/` | 每章 / 每附录一个文件夹，内含原书 PDF、OCR 后的 Markdown，以及中文译本文件（`（中文版）.md`） |
| `…/（中文版）.md` | 完整的中文译本——封面目录、17 章正文与 5 个附录，共 23 个单元 |
| `《Wills矿物加工技术》全书中译本·结构化总目录.md` | 自动生成的 600 余条多级标题总索引，含跨文件跳转链接 |
| `_翻译规范_中译本说明.md` | 内部体例规范，使后续章节在术语、公式语法与排版上保持一致 |

## 当前进度

- ✅ 封面目录、第 1–17 章、附录 I / III / IV / V / VI 已全部译出并归档。
- ✅ 翻译规范：采用规范的中国选矿专业术语；术语首次出现处附英文原词；公式改写为可在 Typora / MathJax 中正常渲染的写法；原书每处插图均以 `【插图位置 · 图 N.M】` 标记，便于日后插入图片。
- 🚧 这是一个持续更新的项目。内容将不断审校、打磨、修正与扩充。

## 使用方法

- 用 **Typora**（或 VS Code、Obsidian）打开任一 `（中文版）.md`，即可舒适阅读并正常渲染数学公式。
- 以 `…结构化总目录.md` 作为入口——每个标题均可跳转回对应的章节原文。
- 面向 AI / Agent 用途：这份结构化 Markdown 已可直接接入分块与向量化流程。

## 声明

- 本译本为**非官方、非商业、学习用途**的翻译。原书及其一切权利归 **Elsevier Ltd. 及原作者**所有，请勿用于商业传播。
- OCR 不可避免地会引入噪声。每个章节在翻译过程中均已清理，但错误仍在所难免——欢迎指正与贡献。

---

## License / 许可

The original textbook *Wills' Mineral Processing Technology*, 8th Edition (© Elsevier Ltd.), and all rights therein belong to their respective owners. This repository hosts an unofficial Chinese translation produced for educational and research purposes only.

原书《Wills' Mineral Processing Technology》第 8 版（© Elsevier Ltd.）及其一切权利归各权利人所有。本仓库所载为其非官方中文译本，仅供学习与研究使用。
