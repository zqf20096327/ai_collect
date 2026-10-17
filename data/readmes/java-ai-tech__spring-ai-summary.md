<p align="left">
  <a href="README.md" target="_blank"><img src="https://img.shields.io/badge/lang-中文-red?logo=googletranslate" alt="中文" style="vertical-align:middle; margin-right:4px;"/></a>
  <a href="README_EN.md" target="_blank"><img src="https://img.shields.io/badge/lang-English-blue?logo=googletranslate" alt="English" style="vertical-align:middle; margin-right:4px;"/></a>
  <a href="https://github.com/java-ai-tech/spring-ai-summary/wiki" target="_blank"><img src="https://img.shields.io/badge/doc-wiki-blue?logo=readthedocs" alt="document" style="vertical-align:middle; margin-right:4px;"/></a>
  <img src="https://img.shields.io/badge/spring--ai--summary-v1.0.0-blue.svg" alt="Spring AI Summary" style="vertical-align:middle; margin-right:4px;"/>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=java-ai-tech.spring-ai-summary" alt="Visitors" style="vertical-align:middle; margin-right:4px;"/>
</p>

**Spring AI Summary** 是基于原生 **Spring AI** 框架的模块化示例工程集合，通过清晰的代码示例和详细文档，帮助开发者快速掌握 Spring AI 的核心功能。

### 👥 适合人群
Spring AI Summary 面向对 Spring AI 框架感兴趣的开发者，无论是初学者还是有经验的工程师，都可以通过本项目快速了解框架的核心功能，并将其应用到实际项目中。 通过 Spring AI Summary，你可以：

- 掌握 Spring AI 的核心概念和功能。
- 学习如何构建高效的 AI 应用。
- 获取最新的技术动态和实践经验。

**加入社区** 🎯 扫码加群主微信（备注：Spring AI），一起探索 Spring AI 的无限可能！

<p align="center">
  <img width="189" alt="社区交流群" src="docs/statics/my_chat.png" />
</p>

## 📖 学习路径

如果你是第一次接触 Spring AI，建议先阅读 [Spring AI 官方文档](https://spring.io/projects/spring-ai) 以了解框架的基本概念和使用方法。然后可以通过本项目的各个模块进行实践，逐步深入理解框架的核心功能。

**推荐学习顺序**：
1. 📚 [Spring AI 官方文档](https://spring.io/projects/spring-ai) - 了解基础概念
2. 💬 **spring-ai-chat** - 聊天应用开发（必选起点）
3. 🔧 **spring-ai-tool-calling** - 工具调用能力
4. 🧠 **spring-ai-vector** - 向量数据库集成
5. 🚀 **MCP/RAG/AGENT** - 高级应用模式

👇下面开启 Spring AI 之旅吧～

## 🚀 快速开始

### ⚙️ 环境要求

| 依赖项         | 版本/要求                 | 说明                 |
| -------------- |-----------------------|--------------------|
| SpringBoot     | 3.3.6                 | -                  |
| Spring AI      | 1.0.0                 | -                  |
| JDK            | 21+                   | -                  |
| Maven          | 3.6+                  | 强烈推荐使用 mvnd 代替 mvn |
| Docker         | （用于运行 Milvus、Nacos 等） |                    |

### 1. 🧬 克隆项目

```bash
# 克隆项目到本地
git clone https://github.com/java-ai-tech/spring-ai-summary.git
# 进入项目并编译
cd spring-ai-summary && mvn clean compile -DskipTests
```

> 如果遇到 Maven 依赖下载慢的问题，可以尝试使用国内的 Maven 镜像源，如阿里云、清华大学等；运行过程中如果有其他任何问题，可以扫码加入上面的微信群进行咨询交流～～～

### 2. 🛠️ 配置环境变量

对于每个模块的 resource 文件夹下的 `application.yml`/`application.properties` 文件，根据你的需求配置相应的 API 密钥。如 **spring-ai-chat-deepseek** 模块：

```properties
# 示例：deepseek 模块配置
spring.ai.deepseek.api-key=${spring.ai.deepseek.api-key}
spring.ai.deepseek.base-url=https://api.deepseek.com
spring.ai.deepseek.chat.completions-path=/v1/chat/completions
spring.ai.deepseek.chat.options.model=deepseek-chat
```
将你的 `spring.ai.deepseek.api-key` 替换为实际的 API 密钥即可启动运行。关于如何申请 api key ，可以移步项目 [Wiki 页面](https://github.com/java-ai-tech/spring-ai-summary/wiki)进行查看。

> 💡 **安全提示**：使用环境变量存储 API 密钥，避免代码泄露。[申请密钥指南](https://github.com/java-ai-tech/spring-ai-summary/wiki)

### 3. ▶️ 运行示例

完成上述步骤后，你可以选择运行不同的示例模块来体验 Spring AI 的功能。如启动运行 **spring-ai-chat-deepseek** 模块（具体端口可以根据你自己的配置而定）：

```bash
2025-06-04T14:18:43.939+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] c.g.ai.chat.deepseek.DsChatApplication   : Starting DsChatApplication using Java 21.0.2 with PID 88446 (/Users/glmapper/Documents/projects/glmapper/spring-ai-summary/spring-ai-chat/spring-ai-chat-deepseek/target/classes started by glmapper in /Users/glmapper/Documents/projects/glmapper/spring-ai-summary)
2025-06-04T14:18:43.941+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] c.g.ai.chat.deepseek.DsChatApplication   : The following 1 profile is active: "deepseek"
2025-06-04T14:18:44.469+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8081 (http)
2025-06-04T14:18:44.475+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2025-06-04T14:18:44.476+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.33]
2025-06-04T14:18:44.501+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2025-06-04T14:18:44.502+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 533 ms
2025-06-04T14:18:44.962+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] o.s.b.a.e.web.EndpointLinksResolver      : Exposing 14 endpoints beneath base path '/actuator'
2025-06-04T14:18:44.988+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8081 (http) with context path '/'
2025-06-04T14:18:44.997+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [           main] c.g.ai.chat.deepseek.DsChatApplication   : Started DsChatApplication in 1.215 seconds (process running for 1.637)
2025-06-04T14:18:45.175+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [on(2)-127.0.0.1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2025-06-04T14:18:45.175+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [on(2)-127.0.0.1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2025-06-04T14:18:45.176+08:00  INFO 88446 --- [spring-ai-chat-deepseek] [on(2)-127.0.0.1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 1 ms
```
如果出现上述类似的启动日志，那么恭喜你，启动成功啦 🎉🎉🎉🎉🎉....，你已经打开了 Spring AI 的大门，接下来就可以开始探索各种功能模块了；启动完成后，可以通过 cUrl、HTTPie 或 Postman 等工具进行测试。

```bash
curl localhost:8081/api/deepseek/chatWithMetric?userInput="你是谁?"
```
结果如下：

**成功标志** 🎉：看到类似响应即表示运行成功！

![运行结果](docs/statics/chat-ds-metrics.png)

```bash
# completion tokens
http://localhost:8081/actuator/metrics/ai.completion.tokens
# prompt tokens
http://localhost:8081/actuator/metrics/ai.prompt.tokens
# total tokens
http://localhost:8081/actuator/metrics/ai.total.tokens
```
以 `ai.completion.tokens` 为例，结果如下：

```json
{
   "name": "ai.completion.tokens",
   "measurements": [
      {
         "statistic": "COUNT",
         "value": 34
      }
   ],
   "availableTags": []
}
```

**关于其他模块的使用方法和配置，可以查看 [Wiki 页面](https://github.com/java-ai-tech/spring-ai-summary/wiki)或各模块的 `README.md` 文件。**

## 📚 学习资料(持续更新中)

以下是一些推荐的学习资源：

> 官方也有一个[学习资料汇总](https://github.com/spring-ai-community/awesome-spring-ai)，但主要是汇总的国外的一些资料，所以本项目更聚焦在汇总了一些国内的学习资源，供大家参考。

#### 技术社区
- [Spring AI 官方文档](https://spring.io/projects/spring-ai)
- [Spring AI Alibaba 官方文档](https://github.com/alibaba/spring-ai-alibaba)

#### 项目系列
- [MindMark（心印）是一款基于 SpringAI 的 RAG 系统](https://gitee.com/mumu-osc/mind-mark)
- [My AI Agent 是一个基于 Spring Boot 和 Spring AI 框架构建的智能代理服务](https://github.com/Cunninger/my-ai-agent)

#### 博客系列
- [码匠的流水账--Spring AI  系列专栏](https://cloud.tencent.com/developer/column/72423) 因为作者没有进行专栏管理，所以是链接到了主页；此外这个系列的文章用来学习 Spring AI 的一些设计思路和实现方式非常不错，但是他是基于 M 系列版本写作的，所以有些内容可能会和最新版本不一致。
- [深入解析 Spring AI 系列](https://www.cnblogs.com/guoxiaoyu/p/18666904) 
- [如何用Spring AI构建MCP Client-Server架构](https://spring.didispace.com/article/spring-ai-mcp.html)
- [Building Effective Agents with Spring AI](https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns) 🌟🌟🌟🌟🌟
- [Spring AI 大模型返回内容格式化源码分析及简单使用](https://juejin.cn/post/7378696051082199080)
- [Spring AI EmbeddingModel 概念与源码分析](https://my.oschina.net/u/2391658/blog/18534829)
- [全量RAG技术：更简单、更实用的实现方法 ✨](https://www.readme-i18n.com/FareedKhan-dev/all-rag-techniques?lang=zh)
- [Spring AI 框架原理与实战](https://juejin.cn/column/7375109287716372520) 🌟🌟🌟
- 大模型技术科普
  - [LLM 系列（一）：发展历程篇](https://mp.weixin.qq.com/s/72omFtMqinJs4MMX41MCyw)
  - [LLM 系列（二）：基础概念篇](https://mp.weixin.qq.com/s/Fg0bczAxejgKs_65kWxWSg)
  - [LLM 系列（三）：架构模式篇](https://mp.weixin.qq.com/s/d6Y76I_Vxfmj6wa5sAN3uQ)
  - [LLM 系列（四）：神奇数字篇](https://mp.weixin.qq.com/s/tEozMs4QWDYx5vrhitA9uQ)
  - [LLM 系列（五）：模型训练篇](https://mp.weixin.qq.com/s/TK8rTcrjS1pfigQxj2mq8A)
  - [LLM 系列（六）：模型推理篇](https://mp.weixin.qq.com/s/tjXme2CWnUxLmawDDiylWQ)
  - [LLM 系列（七）：数学概念篇](https://mp.weixin.qq.com/s/SBtmPoWtAoguWFUVPB1PGQ)
  - [LLM 系列（八）：RAG 篇](https://mp.weixin.qq.com/s/y4yAGqs6p4PhErPmRKtDkg)
  - [LLM 系列（九）：RAG 番外篇-从文档到向量](https://mp.weixin.qq.com/s/HojxR-tC5Gxn3tsxCz17Ow)
  - [LLM 系列（十）：RAG 番外篇-向量检索](https://mp.weixin.qq.com/s/QFnfBU2we_4UG6v4spEFgA)
  - [LLM 系列（十一）：模型精度篇](https://mp.weixin.qq.com/s/E_AeSOGYzoynm5hVicaKfw)
  - [LLM 系列（十二）：解读 Function Calling](https://mp.weixin.qq.com/s/RiILquzDnKZCaZG8nry2Eg)
  - [LLM 系列（十三）：解读 Context Engineering](https://mp.weixin.qq.com/s/o77X-ZKBbSwYq0qMqpTP4Q)
  - [LLM 系列（十四）：解读 Deep Research](https://mp.weixin.qq.com/s/t_CAsHp5cnFQIKFbbQqkLg)
  - [LLM 系列（十五）：解读 Transformer 位置编码](https://mp.weixin.qq.com/s/y4rDTx0BTNFTamem6S_WKw)
  - [LLM 系列（十六）：解读 Transformer 输出采样](https://mp.weixin.qq.com/s/daR0asrVN01nFjFA2JcsJQ)
  - [LLM 系列（十七）：解读 Transformer 残差连接](https://mp.weixin.qq.com/s/GEwu__TklVjBN0o9cildpA)
  - [LLM 系列（十八）：解读 Transformer 注意力机制](https://mp.weixin.qq.com/s/dttX6ODjnoyKfFfpyZGepQ)

#### 视频系列
- [How to Build Agents with Spring AI](https://www.youtube.com/watch?v=d7m6nJxfi0g)
- [Spring AI 系列视频教程](https://www.youtube.com/watch?v=yyvjT0v3lpY&list=PLZV0a2jwt22uoDm3LNDFvN6i2cAVU_HTH)
- [马克的技术工作坊](https://space.bilibili.com/1815948385) 🌟🌟🌟
- [大模型技术 AI 社区 EZ-Encoder](https://space.bilibili.com/3546829121652889?spm_id_from=333.788.upinfo.detail.click) 🌟🌟🌟🌟🌟

#### 优质论文
- 模型范式与核心算法
  - [Brook for GPUs（2004）](https://graphics.stanford.edu/projects/brookgpu/)
  - [ImageNet Classification with Deep CNNs（AlexNet）](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
  - [Sequence to Sequence Learning with Neural Networks（2014）](https://arxiv.org/abs/1409.3215)
  - [Neural Machine Translation by Jointly Learning to Align and Translate（2014）](https://arxiv.org/abs/1409.0473)
  - [Distilling the Knowledge in a Neural Network（2015）](https://arxiv.org/abs/1503.02531)
  - [Deep Residual Learning for Image Recognition（ResNet）（2015）](https://arxiv.org/abs/1512.03385)
  - [Outrageously Large Neural Networks: Mixture of Experts（2017）](https://arxiv.org/abs/1701.06538)
  - [Attention Is All You Need（Transformer）（2017）](https://arxiv.org/abs/1706.03762)
  - [Mastering the Game of Go without Human Knowledge（AlphaGo Zero）（2017）](https://www.nature.com/articles/nature24270)
  - [The Bitter Lesson（2018）](https://www.gwern.net/The-Bitter-Lesson)
  - [Chain-of-Thought Prompting（2022）](https://arxiv.org/abs/2201.11903)
  - [LoRA: Low-Rank Adaptation of LLMs（2021）](https://arxiv.org/abs/2106.09685)
  - [ReAct: Reasoning and Acting in Language Models（2022）](https://arxiv.org/abs/2210.03629)
- Infra 与数据
  - [ZeRO: Memory Optimization for Trillion-Parameter Models (2019)](https://arxiv.org/abs/1910.02054)
  - [Scaling Laws for Neural Language Models (2020) ](https://arxiv.org/abs/2001.08361)
  - [Training Compute-Optimal LLMs (Chinchilla) (2022) ](https://arxiv.org/abs/2203.15556)
  - [LAION-5B Dataset (2022) — Schuhmann](https://arxiv.org/abs/2210.08402)
  - [The RefinedWeb Dataset (2023)](https://arxiv.org/abs/2306.01116)
  - [MegaScale: Training on 10,000\+ GPUs (2024)](https://arxiv.org/abs/2402.15627)
- 语言模型发展
  - [Efficient Estimation of Word Representations（Word2Vec）（2013）](https://arxiv.org/abs/1301.3781)
  - [Google’s Neural Machine Translation System（2016）](https://arxiv.org/abs/1609.08144)
  - [Improving Language Understanding by Generative Pre-Training（GPT-1）](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
  - [BERT: Pre-training of Deep Bidirectional Transformers（2018）](https://arxiv.org/abs/1810.04805)
  - [Language Models are Unsupervised Multitask Learners（GPT-2）（2019）](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
  - [GPT-3: Language Models are Few-Shot Learners（2020）](https://arxiv.org/abs/2005.14165)
  - [Training Language Models with Human Feedback（InstructGPT）（2022）](https://arxiv.org/abs/2203.02155)
  - [Tulu 3 Technical Report（2024）](https://arxiv.org/abs/2411.15124)
- DeepSeek
  - [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
  - [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
  - [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism](https://arxiv.org/abs/2401.02954)
- Kimi
  - [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://arxiv.org/abs/2501.12599)
  - [Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534)
- Qwen
  - [Qwen Technical Report](https://arxiv.org/abs/2309.16609)
  - [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115)
  - [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

大家如果有好的文章或资源，也欢迎提交 PR 或 Issue 进行补充和完善。下面开发和贡献指南。

## 🔧 开发指南（代码、文档）

首先，非常欢迎各位提交任何形式的贡献，包括但不限于**代码、文档、测试、代码注释**等等。但在提交贡献之前请遵循如下流程：

### 贡献代码

1. **Fork 项目**

如下图所示， fork 仓库到你个人仓库
![how-to-fork.png](docs/statics/how-to-fork.png)

2. **Clone 你个人仓库代码**

   ```bash
   # 在 GitHub 上 Fork 项目
   # 克隆你的 Fork 仓库
   git clone https://github.com/your-username/spring-ai-summary.git
   cd spring-ai-summary
   ```

3. **创建特性分支**
   ```bash
   # 创建并切换到新的特性分支
   git checkout -b feature/your-feature-name
   ```

4. **开发规范**
   - 遵循项目的代码风格和命名规范
   - 确保代码通过所有测试（如有）
   - 更新相关文档

5. **提交代码**
   ```bash
   # 添加修改的文件
   git add .
   # 提交代码
   git commit -m "feat: add new feature"
   # 推送到你的 Fork 仓库
   git push origin feature/your-feature-name
   ```
   
6. **创建 Pull Request**
   - 在 GitHub 上创建 Pull Request
   - 填写 PR 描述，说明改动内容和原因
   - 等待代码审查和合并

## 📝 注意事项

1. **API 密钥安全**
   - 建议使用环境变量存储 API 密钥，避免泄露风险
   - 切勿在代码仓库中硬编码密钥
   - 定期轮换密钥，提升安全性

2. **Token 使用**
   - 持续监控 Token 消耗，避免超额
   - 设置合理的 Token 限制，防止滥用
   - 推荐实现缓存机制，提升响应速度与成本控制

## 📄 License & 说明

* 1、本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。 另外本项目仅供学习和研究使用，不适用于生产环境，请勿将样例工程直接用于生产环境。使用时请遵守相关模型的使用条款和条件。
* 2、本项目的所有代码和文档均由 [glmapper](https://github.com/glmapper) 独立开发和维护，欢迎大家提出意见和建议，如果对你有帮助，请给个 Star 支持一下哦！如果你有任何问题或建议，请在 GitHub 上提交 Issue 或 PR，或者通过[这里](http://www.glmapper.com/about)联系我。后续我将进一步将关于 **spring ai 的相关技术文章**同步发布到本仓库和个人微信公众号：**磊叔的技术博客**，也欢迎扫码关注。

<p align="center">
  <img src="docs/statics/wx-gzh.png" alt="微信公众号" width="200"/>
</p>

## 🙏 致谢

- [Spring AI](https://github.com/spring-projects/spring-ai) - 提供强大的 AI 集成框架
- [OpenAI](https://openai.com) - 提供 GPT 系列模型
- [通义千问](https://qianwen.aliyun.com) - 提供 Qwen 系列模型
- [豆包](https://www.volcengine.com/docs/82379) - 提供豆包系列模型
- [Milvus](https://milvus.io) - 提供向量数据库支持

本项目是一个完全开源项目，主要目的是汇聚更多优质的 Spring AI 相关的学习资源，当然**相关学习资源主要来源于网络，如有侵权，请联系删除！！！**；在此也对参与开源贡献和所有在技术社区分享技术的朋友们表示衷心的感谢！

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=java-ai-tech/spring-ai-summary&type=Date)](https://www.star-history.com/#java-ai-tech/spring-ai-summary&Date)