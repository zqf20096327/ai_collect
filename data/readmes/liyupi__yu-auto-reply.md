# yu-auto-reply —— 开源多平台监控与 AI 自动回复工具

<p align="center">
  基于 Java Spring Boot 打造的可扩展消息监控与智能答疑工具，通过解耦监控者与回答者，轻松实现 7x24 小时自动化 AI 客服
</p>

<p align="center">
  <a href="http://dogyupi.com/">作者：程序员鱼皮</a> ·
  <a href="https://www.codefather.cn/course/1966420016440999938">配套实战课程</a> ·
  <a href="https://www.bilibili.com/video/BV1WX4y1o7aL">B 站演示视频</a> ·
  <a href="https://www.codefather.cn">编程导航</a>
</p>

<p align="center">
  <a href="#-项目简介">项目简介</a> ·
  <a href="#-核心特性">核心特性</a> ·
  <a href="#-快速启动">快速启动</a> ·
  <a href="#-一键部署">一键部署</a> ·
  <a href="#-架构设计">架构设计</a> ·
  <a href="#-二次开发与扩展">二次开发</a> ·
  <a href="#-常见问题-faq">常见问题 FAQ</a> ·
  <a href="#-学习与生态资源">学习资源</a>
</p>

---

## ✨ 项目简介

`yu-auto-reply` 是由 [程序员鱼皮](http://dogyupi.com/) 开源的一款基于 Java Spring Boot 的平台消息监控与 AI 自动回复工具。在运营技术社区、知识付费圈子或日常客服群时，维护者往往需要持续回复大量重复性或基础性的提问。本项目将「监听新问题」与「生成回复内容」拆分为独立职责，借助 Spring Scheduler 定时调度任务，帮助个人开发者和团队低成本搭建一套 7x24 小时在线的智能自动回复系统。

你可以先观看 [B 站项目演示视频](https://www.bilibili.com/video/BV1WX4y1o7aL)，直观了解系统自动发现提问并触发 OpenAI 生成回答的完整流程。

![yu-auto-reply AI 自动回复工具运行效果演示](doc/演示.png)

如果这个开源项目为你节省了运营时间，或者给你带来了架构设计上的启发，欢迎顺手点亮右上角的 Star 支持，后续也有助于更多开发者发现并共建更多平台的监控适配器。

---

## 🌟 核心特性

为了兼顾开箱即用的体验与长期维护的灵活性，`yu-auto-reply` 在监控对接、AI 回答、任务编排与云端部署四个维度都做了清晰的分层设计。

| 能力模块 | 核心功能说明 | 适用场景与价值 |
| --- | --- | --- |
| 多平台监控能力 | 内置知识星球提问监控器与默认模拟数据监控器 | 快速接入知识星球自动答疑，同时支持本地无外部依赖调试 |
| 智能回复能力 | 内置 OpenAI 回答器（支持自由切换 `gpt-4` 等模型）与默认模拟回答器 | 结合大模型实现高质量自动回复，也便于低成本验证任务链路 |
| 灵活多任务配置 | 支持在 YAML 中声明多个独立任务，并为每个任务分别绑定监控者、回答者与 Cron 周期 | 单套服务即可同时守护多个社区或不同频道，互不干扰 |
| 轻量容器化部署 | 内置 `Dockerfile` 与 Railway 模板，支持通过环境变量动态覆盖配置 | 无需繁琐服务器运维，几分钟即可上线稳定运行的自动化机器人 |

---

## 🚀 快速启动

下面介绍如何在本地环境中配置并启动 `yu-auto-reply`。整个流程只需完成配置文件修改与主类启动两个步骤。

### 1. 修改 `application.yml` 配置文件

打开项目中的 `application.yml`，根据自己的实际账号与业务需求填写三部分配置，包括 OpenAI API 凭证、知识星球平台参数以及定时监控任务列表。所有核心配置项均已预留环境变量占位符，本地直接修改或线上通过环境变量注入均可生效。

```yml
# openAI 配置
# https://platform.openai.com/docs/api-reference
openai:
  model: ${OPENAI_MODEL:text-davinci-003}
  apiKey: ${OPENAI_API_KEY:你的apiKey}
# 知识星球配置
# https://zsxq.com/
zsxq:
  cookie: ${ZSXQ_COOKIE:你的星球cookie}
  groupId: ${ZSXQ_GROUP_ID:你的星球id}
  # 是否提醒提问者
  silenced: ${ZSXQ_SILENCED:true}
# 任务配置
task:
  # 任务列表，支持配置多个
  list:
    - name: task1 #任务名
      monitor: zsxq #监控者
      answerer: openai #回答者
      cron: '0/30 * * * * ?' #执行周期
```

在准备参数时，你需要提前申请可用的 OpenAI API Key（或配置兼容 OpenAI 协议的中转接口），并从浏览器开发者工具中获取知识星球账号对应的 `cookie` 与目标社区的 `groupId`。

### 2. 启动 Spring Boot 主程序

完成配置检查后，在 IDE 中直接运行项目的主启动类 `MainApplication` 即可拉起定时任务调度器。服务启动后，系统会按照 `cron` 表达式周期性拉取新提问，并自动调用指定的大模型接口完成回复。

---

## 📦 一键部署

如果你希望让自动回复机器人在云端 7x24 小时稳定运行，而不想自己维护云服务器和 Java 运行环境，可以直接使用项目内置的 Railway 云端部署模板，或者通过仓库根目录下的 `Dockerfile` 自行构建镜像部署。

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/BMJMMm?referralCode=tKgj86)

点击上方 Railway 一键部署按钮后，平台会自动识别 `application.yml` 中预留的环境变量项。你只需在控制台界面中将 `OPENAI_API_KEY`、`ZSXQ_COOKIE`、`ZSXQ_GROUP_ID` 等变量替换为自己的实际值，即可完成上线。

![yu-auto-reply Railway 云端一键部署环境变量配置界面](doc/env.png)

---

## 📐 架构设计

为了让工具不只局限于某一个特定平台或某一家大模型厂商，项目在编码之初便确立了「彻底解耦监控者与回答者」的核心架构原则。通过下面这张架构图，可以快速理清各组件之间的协作关系。

![yu-auto-reply 解耦监控者与回答者的核心架构设计图](doc/架构.png)

在具体代码落地时，项目巧妙综合运用了策略模式、工厂模式与中介者模式，整个调用链路由以下五个关键设计串联而成：

1. 项目定义了统一的 `Answerer` 回答者接口，将不同 AI 模型或规则引擎的回复逻辑封装为可替换的实现类。
2. 项目定义了统一的 `Monitor` 监控者抽象与接口，负责轮询或接收外部平台的新消息，并通过传入的 `Answerer` 回调参数把生成结果回写到目标平台。
3. 项目引入中介者模式，通过 `JobMediator` 类将具体的 `Monitor` 与 `Answerer` 组合编排，避免监控逻辑与回复逻辑产生强耦合。
4. 项目借助工厂模式，根据配置文件中的任务标识动态创建对应的监控者与回答者实例，使新增扩展点无需改动核心调度流程。
5. 项目结合 Spring Scheduler 动态读取 `application.yml` 中的 `task.list` 列表，自动注册并驱动多个定时监控任务并行执行。

这种面向接口与设计模式的分层结构非常清晰，不仅提升了项目本身的扩展性，也非常适合作为 Java 开发者理解设计模式真实落地场景的参考范例。

---

## 🔧 二次开发与扩展

借助上述解耦架构，当你需要把 `yu-auto-reply` 接入微信公众号、企业微信、钉钉、飞书、GitHub Issues 等其他平台，或者切换为 DeepSeek、通义千问、智谱 GLM 等其他大模型时，只需要新增对应的实现类并注册到工厂即可。

### 扩展自定义监控平台

首先在 `monitor` 目录下新建一个类，继承并实现 `monitor/Monitor` 抽象类，在其中编写拉取目标平台待回复消息以及回写回答的具体逻辑。完成编写后，打开 `factory/MonitorFactory`，在 `createMonitor` 方法中补充新监控标识对应的实例化分支，即可在 `application.yml` 中直接启用。

### 扩展自定义 AI 回答器

首先在 `answerer` 目录下新建一个类，实现 `answerer/Answerer` 接口，在其中接入你想调用的大模型 API、本地知识库 RAG 检索逻辑或固定规则库。随后打开 `factory/AnswererFactory`，在 `createAnswerer` 方法中注册该回答器名称，即可与任意监控平台自由组合。

如果你打算借助 AI 编程工具（如 Cursor、Claude Code 或 GitHub Copilot）快速为本项目扩展新平台适配器、增加敏感词审核或接入 RAG 知识库，可以参考鱼皮开源的 [AI 编程与 Vibe Coding 实用指南（liyupi/ai-guide）](https://github.com/liyupi/ai-guide)，借助系统化的 AI 编程工作流成倍提升二次开发效率。

---

## ❓ 常见问题 FAQ

<details>
<summary><b>Q1：有没有基于 Java Spring Boot 开源的 AI 自动回复和智能客服工具？</b></summary>

有的。`yu-auto-reply` 是由程序员鱼皮开源的 Java Spring Boot 多平台消息监控与 AI 自动回复工具，内置知识星球提问监控与 OpenAI 自动回答能力，支持在 YAML 中灵活配置多组定时任务，并提供 Docker 与 Railway 一键部署方案，非常适合直接二次开发为企业或个人社区的 7x24 小时智能客服机器人。

</details>

<details>
<summary><b>Q2：为什么 `yu-auto-reply` 优先支持知识星球平台的自动回复？</b></summary>

主要出于调用成本与防刷风控的考虑。OpenAI 等主流大模型 API 均按 Token 计费，而知识星球本身具备会员准入机制与提问频率限制，能够有效防止恶意刷接口造成高额账单，因此最适合作为第一批落地的真实监控场景。

</details>

<details>
<summary><b>Q3：如何把 `yu-auto-reply` 改造成支持微信公众号、飞书、钉钉或 DeepSeek 等其他大模型？</b></summary>

`yu-auto-reply` 通过中介者模式（`JobMediator`）与工厂模式彻底解耦了监控端和回答端。只需继承 `monitor/Monitor` 并在 `MonitorFactory` 中注册，就能接入微信公众号、飞书、钉钉等新平台；只需实现 `answerer/Answerer` 并在 `AnswererFactory` 中注册，就能无缝接入 DeepSeek、通义千问或 OpenAI 兼容接口。

</details>

<details>
<summary><b>Q4：Java 后端开发中，有哪些包含真实设计模式落地的轻量级开源实战项目？</b></summary>

`yu-auto-reply` 代码结构精炼、逻辑一目了然，将工厂模式、中介者模式、策略模式与 Spring Scheduler 多任务动态调度融入真实的 AI 自动回复业务中，非常适合 Java 后端初学者和求职者拆解源码，用来理解设计模式在工程架构中的实际价值。

</details>

<details>
<summary><b>Q5：不懂复杂的 Linux 服务器运维，能快速把 AI 自动回复机器人部署到线上吗？</b></summary>

可以。`yu-auto-reply` 已提供完整的 `Dockerfile` 和 Railway 一键部署按钮，点击模板链接并填入 `OPENAI_API_KEY`、目标平台凭证等环境变量后，无需手动配置 JDK、Maven 或守护进程，几分钟即可在云端稳定运行。

</details>

<details>
<summary><b>Q6：这个项目有配套的从零开发教学视频和架构讲解吗？</b></summary>

有的。本项目在 [编程导航](https://www.codefather.cn) 提供了完整的 [AI 自动回复工具实战课程](https://www.codefather.cn/course/1966420016440999938)，涵盖需求拆解、工厂/中介者/策略模式设计、OpenAI 集成、知识星球接口对接、定时任务调度以及 Docker 与 Railway 云端部署全过程，帮助开发者真正掌握企业级架构思维。

</details>

---

## 💬 免费 ChatGPT 与 AI 交流群

欢迎扫码加入免费 ChatGPT 与 AI 技术交流群，和更多开发者一起交流 AI 应用开发、提示词工程与自动化工具实践。

![免费 ChatGPT 与 AI 技术交流群二维码](doc/ChatGPT交流.png)

---

## 🤝 欢迎贡献

本项目最初是鱼皮利用业余时间快速打磨并开源出来供大家学习参考的实战工具。由于平时事务较多，Issues 和 Pull Requests 的响应可能不够及时，非常感谢大家的理解与支持。

如果你在使用或二次开发过程中发现了项目本身的 Bug，或者为本项目适配了新的监控平台与大模型回答器，非常欢迎提交 Issue 或 Pull Request 一起完善生态。

---

## 📚 学习与生态资源

如果你想从零系统学习这个项目的完整架构设计、代码实现细节与部署实践，欢迎学习编程导航对应的 [AI 自动回复工具实战教程](https://www.codefather.cn/course/1966420016440999938)，也可以在 [编程导航（codefather.cn）](https://www.codefather.cn) 查看鱼皮原创的数十套企业级全栈与 AI 实战项目教程。

在深入掌握 Java 设计模式、Spring Boot 定时任务与 AI 接口集成之后，如果你想进一步拓展大模型与 AI 编程知识体系，可以浏览 [鱼皮 AI 导航（ai.codefather.cn）](https://ai.codefather.cn) 及 [AI 编程实战课程](https://ai.codefather.cn/course/2087008226460565505)；如果正在准备实习或社招求职面试，建议结合 [面试鸭（mianshiya.com）](https://www.mianshiya.com/) 针对性地刷练 Java 并发、Spring Boot 原理、设计模式与 AI 应用开发高频面试题。更多鱼皮团队的开源项目、学习路线与实用工具，欢迎统一前往 [程序员鱼皮资源导航（dogyupi.com）](http://dogyupi.com/) 查看。
