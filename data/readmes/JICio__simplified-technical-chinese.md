# Simplified Technical Chinese (STC) · 简明技术中文

**Writing rules for Chinese text that people and LLMs can read once and understand once.**
**一套写给人、也写给 LLM 的中文写作规则：读一次，只有一种理解。**

STC takes the principles of [ASD-STE100](https://www.asd-ste100.org/), the controlled English of aerospace maintenance, and rebuilds them for Chinese grammar.

STC 参照航空维修用的受控英语 ASD-STE100，按中文语法重建。

> **Unofficial.** STC is an independent draft (STC-0.1) by JIC School. It is not a translation of ASD-STE100. ASD does not endorse it, and it has no connection with ASD.
>
> **非官方。** STC 是极客学校编写的独立草案（STC-0.1），不是 ASD-STE100 的译本，未经 ASD 认可，与 ASD 无隶属关系。

## Why · 为什么

AI now does more of the work, and people do more of the review. Reading becomes the bottleneck. Clear output lets you judge it fast. You can put clarity into rules, and an LLM follows rules well.

执行越来越多交给 AI，人的工作上移到监督和理解，读懂成为瓶颈。清晰可以写成规则，而 LLM 很擅长遵守规则。

## What is in this repository · 仓库内容

| Path · 路径 | Content · 内容 |
| --- | --- |
| [`spec/STC-zh-Hans.md`](spec/STC-zh-Hans.md) | Full spec, Simplified Chinese · 完整规范（简体） |
| [`spec/STC-zh-Hant.md`](spec/STC-zh-Hant.md) | Full spec, Traditional Chinese (Taiwan usage) · 完整规范（繁体，台湾用语） |
| [`prompts/`](prompts/) | Three LLM prompt templates per script: strict, 80%, rewrite · 三份提示模板（严格版、80% 版、改写版），简繁各一套 |
| [`claude/`](claude/) | Drop-in rules for `CLAUDE.md` or any system prompt, in English, Simplified and Traditional · 可直接放进 `CLAUDE.md` 或 system prompt 的规则（英文、简体、繁体） |

## The spec at a glance · 规范一览

8 parts, 60 rules. Each rule is MUST (【必】) or SHOULD (【宜】). Use it 100% strict for manuals and SOPs, and about 80% strict for replies and handouts (all MUST rules, relaxed SHOULD rules).

8 个部分，60 条规则，每条标【必】或【宜】。正式手册按 100% 执行；日常回复和讲义按约 80% 执行：【必】全部遵守，【宜】可以放宽。

| Part · 部分 | Key rules · 要点 |
| --- | --- |
| 1 Words · 词汇 | One word, one meaning; no vague words, classical particles or catch-all verbs · 一词一义；不用模糊词、文言虚词、万能动词 |
| 2 Noun phrases · 名词短语 | No more than 2 的; no more than 3 stacked nouns; state quantity · 最多 2 个“的”；名词堆叠最多 3 个；写清数量 |
| 3 Verbs · 动词 | Active voice; no nominalization; only 4 modal words · 主动表达；不名词化；只用 4 个情态词 |
| 4 Sentences · 句子 | 30 / 40 characters; 2 commas; condition first; new subject, new sentence · 30 / 40 字；最多 2 个逗号；条件在前；主语换了就换句 |
| 5 Procedures · 操作程序 | Numbered steps, one action each; results on their own line · 编号步骤，一步一个动作；结果另起一行 |
| 6 Descriptive writing · 说明性文字 | Conclusion first; facts, not praise · 结论先行；写事实，不写评价 |
| 7 Safety · 安全提示 | Instruction first, consequence second, before the step · 先指令后后果，放在步骤前 |
| 8 Format · 格式 | Full-width punctuation, units, code format, mixed text · 全角标点、单位、代码格式、中英混排 |

**Example · 示例**

| Before · 原文 | STC |
| --- | --- |
| 为确保系统稳定运行，请用户在进行升级操作之前对相关数据加以备份。<br>*To ensure stable operation, users are requested to carry out a backup of relevant data prior to performing the upgrade operation.* | 升级前，备份数据库和 `uploads/` 目录。<br>*Before the upgrade, back up the database and the `uploads/` folder.* |

## Use it with an LLM · 和 LLM 一起用

1. Copy one file from [`claude/`](claude/) into your `CLAUDE.md`, system prompt or project instructions. · 把 [`claude/`](claude/) 里的一份文件复制进 `CLAUDE.md`、system prompt 或项目说明。
2. For a formal document, use [`prompts/strict.zh-Hans.txt`](prompts/strict.zh-Hans.txt). · 正式文档用严格版模板。
3. To fix existing text, use [`prompts/rewrite.zh-Hans.txt`](prompts/rewrite.zh-Hans.txt). It marks missing facts as 【待补】 ("to add") instead of guessing. · 改写已有文字用改写版模板：缺失的事实标【待补】，不猜。

## Contributing · 参与

Issues and pull requests are welcome, especially word-list entries for your field and test results for the sentence-length limits. The 30 / 40 character limits are estimates (about 1.5 characters per English word), not measured values.

欢迎提 issue 和 PR，特别是你所在领域的词表条目，以及句长上限的实测结果。30 / 40 字是估计值（约 1.5 字对 1 个英文词），不是实测值。

## License · 许可

[CC BY 4.0](LICENSE). You can share and adapt it, including for commercial use. Give credit to “JIC School · Simplified Technical Chinese (STC)” and link to this repository.

[CC BY 4.0](LICENSE)。可以分享和改编，包括商用。请署名“极客学校 JIC School · 简明技术中文（STC）”并附本仓库链接。

ASD-STE100 is a trademark of ASD (AeroSpace and Defence Industries Association of Europe). · ASD-STE100 是 ASD（欧洲航空航天与防务工业协会）的商标。
