<div align="center">
  <img src="docs/public/banner.webp" width="100%" alt="机器人智能体：原理、仿真与实战" />
</div>

<h1 align="center">机器人智能体</h1>
<p align="center"><b>原理、仿真与实战</b></p>

<p align="center">
  <a href="https://datawhalechina.github.io/agentic-robotics/"><img alt="在线阅读" src="https://img.shields.io/badge/%E5%9C%A8%E7%BA%BF%E9%98%85%E8%AF%BB-datawhalechina-blue" /></a>
  <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="许可协议" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a>
  <img alt="状态" src="https://img.shields.io/badge/status-Alpha-orange" />
</p>

> [!CAUTION]
> Alpha 内测版：理论部分的 13 章已经完成，仿真实验和真机实战还在建设中。内容可能有错误，欢迎提 Issue 反馈。

## 项目介绍

由大模型（large language model，LLM）驱动的智能体（agent）已经能够读写文件、调用工具、编写和修改代码。这类智能体所依靠的一些条件，到了机器人上不再成立：工具返回成功，不等于物体已经放到位；大模型思考的时候，环境仍然在变化；机器人的动作执行以后，往往无法撤销。

《机器人智能体》是一份开源教程，介绍大模型怎样通过工具指挥机器人完成任务，任务完成得不好时怎样改进，以及怎样判断一次改进是否有效。本教程的出发点是两句话：智能体即是机器人，智能体改进机器人。

前一句说的是执行任务的时候。大模型、机器人本体和两者之外的 Harness 共同构成一个机器人智能体（agentic robot），其中 Harness 负责取得观测，把大模型的决定变成机器人的动作，并检查任务是否完成。后一句说的是任务之外。这时智能体根据执行记录修订技能（skill）、训练策略（policy）、整理数据、搭建仿真场景，使机器人下一次做得更好。执行的结果和改进的效果都要经过独立的评估（evaluation），这项要求贯穿各章。

两种角色合到同一个系统以后，智能体可以自己执行任务、发现失败、提出改动并发起验证。改进的办法如果也由它自己来改，而且改过以后更有效，就称为递归自我改进（recursive self-improvement，RSI）。本教程区分一次改进、持续改进和递归改进，说明每一种需要什么证据，以及哪些内容仍然要由人掌管。

各章介绍的是通用的做法，不依赖某一家的模型、框架或者机器人，引用的论文、文档和标准列在章末的参考文献里。

## 你将学到什么

理论部分介绍下面这些做法：

- 把机器人的能力做成大模型可以调用的工具，并在每次调用之前用代码检查（第 2 章）。
- 编排多步的任务，检查每一步的效果，在失败以后恢复或者及时停止（第 3、4 章）。
- 确定记忆里保存哪些内容，判断它们是否已经过时，并安排决策层、策略层和控制层之间的配合（第 5、6 章）。
- 把有效的做法整理成技能，写明适用范围，并根据失败的记录修订（第 7、8 章）。
- 写成功判据，把执行和评分分开，比较两个版本的结果（第 9 章）。
- 让智能体参与策略训练、数据采集和仿真场景的搭建，并分清其中要由人事先定好的内容（第 10 到 12 章）。
- 把执行和改进连成闭环，区分一次改进、持续改进和递归自我改进（RSI），规定智能体和人各自负责的步骤（第 13 章）。

## 适合谁读

- 从事大模型应用或者智能体开发的工程师和学生，想了解把智能体用到机器人上需要增加哪些内容。
- 从事机器人开发的工程师和学生，想在自己的系统里使用大模型。

阅读本教程需要会用 Python，并了解大模型的工具调用。机器人学和强化学习的知识不作要求，用到的概念在正文里说明，例如第 2 章说明单位和坐标系，第 10 章说明训练的基本过程。

## 在线阅读

https://datawhalechina.github.io/agentic-robotics/

## 内容导航

| 章节 | 关键内容 | 状态 |
| ---- | ---- | ---- |
| **导论** | | |
| [第 1 章 导论](docs/theory/chapter-01.md) | 机器人智能体是什么，Harness，从执行到改进 | 已完成 |
| **第一部分 执行** | | |
| [第 2 章 能力接口与门控](docs/theory/chapter-02.md) | 原子能力与工具，调用契约，入口门控，能力适配 | 已完成 |
| [第 3 章 编排](docs/theory/chapter-03.md) | 任务与步骤，由代码还是由大模型编排，控制权交接 | 已完成 |
| [第 4 章 监控与恢复](docs/theory/chapter-04.md) | 受理、执行与效果，超时与未知结果，恢复与放弃 | 已完成 |
| [第 5 章 记忆](docs/theory/chapter-05.md) | 历史、状态和经验，来源与时效，更新与检索 | 已完成 |
| [第 6 章 分层系统](docs/theory/chapter-06.md) | 决策层、策略层和控制层，时间尺度，策略作为工具 | 已完成 |
| **第二部分 改技能** | | |
| [第 7 章 技能与技能库](docs/theory/chapter-07.md) | 文本技能与可执行技能，技能包，适用范围，入库与复用 | 已完成 |
| [第 8 章 技能与 Harness 的演化](docs/theory/chapter-08.md) | 从失败的记录提出修订，候选版本，回归与留出评估，保留与回滚 | 已完成 |
| **第三部分 改权重** | | |
| [第 9 章 评估与验证](docs/theory/chapter-09.md) | 成功判据，执行和评分分开，假成功与评分漏洞，结果比较 | 已完成 |
| [第 10 章 智能体驱动的机器人策略训练](docs/theory/chapter-10.md) | 模仿学习与强化学习，智能体承担的工作，固定预算循环，大模型的微调 | 已完成 |
| [第 11 章 智能体采集与整理机器人数据](docs/theory/chapter-11.md) | 数据的来源，采集的循环，标注与质量检查，数据版本 | 已完成 |
| [第 12 章 智能体搭建仿真场景与任务](docs/theory/chapter-12.md) | 场景与资产，任务配置，生成方式，可用性检查 | 已完成 |
| **收尾 闭环与证据** | | |
| [第 13 章 闭环：递归自我改进与证据](docs/theory/chapter-13.md) | 选择改进对象，改进记录，人与智能体的分工，递归自我改进（RSI）的含义与边界 | 已完成 |
| **动手部分** | | |
| 仿真实验 | 在仿真环境里实现各章的做法 | 建设中 |
| 真机实战 | 在真实的机器人上完成任务并改进 | 建设中 |

[理论目录](docs/theory/index.md)列出了各章要回答的问题和各节的内容。

## 如何学习

建议按顺序阅读这 13 章。第 1 章给出全教程的框架，第 2 到 6 章介绍怎样完成一个任务，第 7、8 章介绍怎样保存和修订有效的做法，第 9 到 12 章介绍评估、训练、数据和仿真场景，第 13 章说明怎样把执行和改进连成闭环。后面的章节会引用前面的内容，不按顺序阅读时，可以通过文中的链接查看被引用的小节。

每章的开头说明这一章要解决的问题，末尾有小结和参考文献。例子里的数字多数只是示意，由实际运行得到的数字在文中另有说明，并给出脚本的位置。

阅读时发现错误或者讲得不清楚的地方，欢迎提 Issue。

## 参与贡献

- 发现问题时，可以提 Issue 反馈。如果没有人回复，可以联系[保姆团队](https://github.com/datawhalechina/DOPMC/blob/main/OP.md)的同学跟进。
- 想参与贡献时，可以提 Pull Request。如果没有人回复，可以联系[保姆团队](https://github.com/datawhalechina/DOPMC/blob/main/OP.md)的同学跟进。
- 对 Datawhale 感兴趣、想发起新项目的读者，可以参考 [Datawhale 开源项目指南](https://github.com/datawhalechina/DOPMC/blob/main/GUIDE.md)。

## 贡献者名单

| 姓名 | 职责 |
| :---- | :---- |
| 罗如意 | |
| 康博 | |
| 周鸿章 | |

## 引用

如果这份教程对你的研究或者工作有帮助，欢迎引用：

```bibtex
@misc{agentic_robotics2026,
  title  = {机器人智能体：原理、仿真与实战},
  author = {罗如意 and 康博 and 周鸿章},
  year   = {2026},
  url    = {https://github.com/datawhalechina/agentic-robotics},
  note   = {GitHub repository}
}
```

## 关注我们

<div align=center>
<p>扫描下方二维码关注公众号：Datawhale</p>
<img src="https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/res/qrcode.jpeg" width = "180" height = "180">
</div>

## LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。
