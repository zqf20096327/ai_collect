<div align="center">

# lecture-to-hw

<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Codex-Skill-7C3AED" alt="Codex Skill">
  <img src="https://img.shields.io/badge/Multi--Agent-Workflow-2563EB" alt="Multi-Agent Workflow">
  <img src="https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-22C55E" alt="README 中文">
</p>

<p>
  <a href="README.md">中文</a> | <a href="README_EN.md">English</a>
</p>

<p><strong>从课程课件到可交付 Markdown 作业的一站式 Codex skill。</strong></p>

</div>

大学生最大的悲哀，莫过于把时间浪费在某些水课的作业里。

你可能需要花时间整理材料，把问题发给大模型，review大模型给的答案，再去尝试理解某些晦涩的概念，并判断大模型的回答是否足够可信。忙完以上的一切，还要忙着去除人机味

日复一日，你重复完成上述的流程，收获的可能不是知识，而仅仅是prompt工程熟练度、无限的疲惫，以及“我怎么又把晚上浪费在这里了”的愧疚！

于是本人痛定思痛，把自己长期以来完成课程作业的工作流整理成了一个 skill：

**lecture-to-hw**

`lecture-to-hw` 的目标很简单：**把全流程交给 agent，从课件到可交付 Markdown 文本，一站式、端到端、尽量高鲁棒地完成课程作业。**

从此，上面那套无趣、无味、无聊的循环，可以被压缩成：

```text
lecture-to-hw，给我干活！ --> 喝杯咖啡  --> 验收并提交
```

## 它会做什么

`lecture-to-hw` 会在当前课程目录里自动寻找：

- 作业题面：PDF、DOCX、Markdown、HTML、图片、notebook 等；
- 课程材料：课件、课堂 demo、实验代码、数据文件；
- 历史答案：例如 `作业/hw*_solution/*.md`。

然后它会把这些东西串起来：

```text
读题 -> 找课件 -> 找课堂中讲授的方法 -> 拆解题目 -> 解题/跑代码 -> 组装 Markdown -> 助教agent执行review -> 交付
```

它不是单纯的 homework solver，而是一个懂你意思的作业流水线工厂！

## 为什么选择lecture-to-hw

### 1. 从课件到作业成品

普通大模型解题通常是直接读题开写。  
`lecture-to-hw` 会先找对应课件和课堂代码，尽量使用课上讲过的公式、术语、算法和记号。

能用课堂代码复现实验结果，就不凭空写；能从课件里找到方法，就不乱引入课程外的高级技巧。

### 2. 多格式题面

支持常见课程材料格式：

- PDF
- DOCX / DOC
- Markdown / TXT
- HTML
- notebook
- 图片题面
- 压缩包里的作业文件

如果公式、表格、图片或版面识别不稳，它会先标出不确定点并请求确认，而不是一口气乱写下去。

### 3. 多 agent 并行加速

主 agent 负责当 controller：

```text
读题 -> 拆题 -> 调度 -> 验收 -> 组装
```

当作业能按题目、实验模块或课件章节清楚拆开时，默认最多同时开启 4 个子代理。子代理负责边界清楚的局部任务，例如：

- 某一道题的解题草稿；
- 某个实验或代码结果复现；
- 某份课件与题目的对应关系确认；
- 某个模块的独立验算。

当然，当题目很短、强耦合时，会退回单 agent 模式，不为了并行而并行

### 4. 助教 review agent

当解题的文本组装完成后，如果题目复杂、工程量大、或主 agent 自己把握不足，可以再开一个专门挑刺的**助教 Agent**

它会专门检查：

- 是否漏题或漏采分点；
- 公式、数值、逻辑有没有明显错误；
- 是否用了不符合课件的方法；
- 是否有太重的 AI 味；
- 是否像一个正常大学生会交的答案。

### 5. 参考往期作业风格，降低人机味

众所周知，大学生的普遍习惯是，只踩得分点，有问必答，没问坚决不答，而Agent的习惯总是反复补一些解释性文字，希望能“稳稳地接住你”，却在无意中害苦了作者。

而**lecture-to-hw**是一个可以检测你作业风格的skill。他会读取你的历史作业、学习你的格式习惯，包括：

- 标题和姓名/学号/班级行；
- 小标题层级如何排布
- 公式、表格、图片如何引用
- 答案的详略

### 6. 交付时给可信度

**lecture-to-hw**在完成整个解题流程后，最终回复会告诉你：

- 生成了哪些文件；
- 跑了哪些验证
- review 后改了什么；
- 当前作业可信度：高 / 中 / 低
- 哪些地方建议你手动复核

## 安装

把仓库放到 Codex skills 目录下：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/vect-G/lecture-to-hw.git ~/.codex/skills/lecture-to-hw
```

或者直接把整个 `lecture-to-hw` 文件夹复制到：

```text
~/.codex/skills/lecture-to-hw
```

然后开启新的 Codex 会话，skill 会被自动发现！

## 快速开始

进入课程目录后，直接说：

```text
用 lecture-to-hw 帮我完成这次作业，输出 Markdown格式的文档
```

如果你想明确允许并行子代理：

```text
用 lecture-to-hw 完成这次作业，允许开并行子代理，最后开一个助教agent辅助review
```

## 推荐配置

作者亲测：

```text
Codex + GPT-5.5 + reasoning high + lecture-to-hw + 允许并行子代理
```

在作业能拆分的情况下，这套配置能比较高效地完成“读材料、拆题、写答案、review、交付”的完整流程。

如果题面质量差、DOCX 公式复杂、或图片题目很多，建议先手动输出为pdf后再进入解题流程。

## 仓库内容

```text
lecture-to-hw/
├── SKILL.md
├── README.md
├── README_EN.md
└── agents/
    └── openai.yaml
```

## 负责任使用

最后，还请诸位在提交作业前，尽可能做一次简单的人工review，毕竟尽管skill承担绝大多数工作，但课程成绩仍属于诸位自己。

希望对你有帮助！

## License

MIT License.
