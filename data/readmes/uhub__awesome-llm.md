# awesome-llm

A curated list of awesome LLM frameworks, libraries and software.

* Learning and Reference
	* [Tutorials and Books](#tutorials-and-books)
	* [Examples and Exercises](#examples-and-exercises)
	* [Awesome Lists and Collections](#awesome-lists-and-collections)
* Language and Tooling
	* [Editor and IDE Support](#editor-and-ide-support)
	* [Version Control](#version-control)
* Web
	* [Frontend and UI Components](#frontend-and-ui-components)
	* [Scraping and Crawling](#scraping-and-crawling)
* Data and Storage
	* [Databases](#databases)
	* [Serialization and Formats](#serialization-and-formats)
* Machine Learning and AI
	* [LLM and Inference](#llm-and-inference)
	* [Machine Learning Frameworks](#machine-learning-frameworks)
	* [Computer Vision](#computer-vision)
	* [Natural Language Processing](#natural-language-processing)
	* [Data Science and Analytics](#data-science-and-analytics)
* AI Agents
	* [Agent Frameworks and Runtimes](#agent-frameworks-and-runtimes)
	* [Agent Skills and Tooling](#agent-skills-and-tooling)
	* [Memory and Context](#memory-and-context)
	* [Evaluation and Benchmarks](#evaluation-and-benchmarks)
* User Interface
	* [Applications and End User Tools](#applications-and-end-user-tools)
* Graphics and Media
	* [Image and Video](#image-and-video)
* Security
	* [Security Tools](#security-tools)
* Concurrency and Performance
	* [Performance and Optimization](#performance-and-optimization)
* Utilities
	* [Command Line Tools](#command-line-tools)
* Business and Domain
	* [Finance and Trading](#finance-and-trading)
	* [Business and Productivity](#business-and-productivity)
* [Other](#other)

## Learning and Reference

### Tutorials and Books

* [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) - Implement a ChatGPT-like LLM in PyTorch from scratch, step by step
* [mlabonne/llm-course](https://github.com/mlabonne/llm-course) - Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks.
* [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) - 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程
* [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) - Bash is all you need - A nano claude code–like 「agent harness」, built from 0 to 1
* [jingyaogong/minimind](https://github.com/jingyaogong/minimind) - 🧠 Train a 64M-parameter LLM from scratch in just 2h!
* [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) - Learn it. Build it. Ship it for others.
* [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) - 《动手学大模型Dive into LLMs》系列编程实践教程
* [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) - 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
* [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) - In-depth tutorials on LLMs, RAGs and real-world AI agent applications.
* [karpathy/LLM101n](https://github.com/karpathy/LLM101n) - LLM101n: Let's build a Storyteller *(archived)*
* [datawhalechina/happy-llm](https://github.com/datawhalechina/happy-llm) - 📚 从零开始构建大模型
* [datawhalechina/self-llm](https://github.com/datawhalechina/self-llm) - 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程
* [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) - This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. Each technique has a detailed notebook tutorial.
* [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) - Official code repo for the O'Reilly Book - "Hands-On Large Language Models"
* [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) - What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?
* [liguodongiot/llm-action](https://github.com/liguodongiot/llm-action) - 本项目旨在分享大模型相关技术原理以及实战经验（大模型工程化、大模型应用落地）
* [datawhalechina/llm-cookbook](https://github.com/datawhalechina/llm-cookbook) - 面向开发者的 LLM 入门教程，吴恩达大模型系列课程中文版
* [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) - 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.
* [AccumulateMore/CV](https://github.com/AccumulateMore/CV) - ✅（已完结）超级全面的 深度学习 笔记【土堆 Pytorch】【李沐 动手学深度学习】【吴恩达 深度学习】【大飞 大模型Agent】
* [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) - End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.
* [liyupi/ai-guide](https://github.com/liyupi/ai-guide) - 程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程，分享 OpenClaw 保姆级教程、大模型玩法（DeepSeek / GPT / Gemini / Claude / GLM）、最新 AI 资讯、Prompt 提示词大全、AI 知识百科（Agent Skills / RAG / MCP / A2A）、AI 编程教程（Harness Engineering）、AI 工具用法（Cursor / Claude Code / TRAE / Codex / Copilot）、AI 开发框架教程（Spring AI / LangChain）、AI 产品变现指南，帮你快速掌握 AI 技术，走在时代前沿。本项目为开源文档 aiguide，已升级为鱼皮 AI 导航网站
* [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) - 💻 vibe coding 101｜The first course for AI-native product builders.
* [stas00/ml-engineering](https://github.com/stas00/ml-engineering) - Machine Learning Engineering Open Book
* [ZJU-LLMs/Foundations-of-LLMs](https://github.com/ZJU-LLMs/Foundations-of-LLMs) - A book for Learning the Foundations of LLMs
* [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) - Harness engineering beginner tutorial, from 0 to 1
* [datawhalechina/llm-universe](https://github.com/datawhalechina/llm-universe) - 本项目是一个面向小白开发者的大模型应用开发教程，在线阅读地址：https://datawhalechina.github.io/llm-universe/
* [halfrost/Halfrost-Field](https://github.com/halfrost/Halfrost-Field) - ✍🏻 Source Code Deep Dives, System Design & Engineering Blogs | Halfrost-Field 冰霜之地：源码解析、系统设计与工程实践笔记
* [The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) - Pocket Flow: Codebase to Tutorial
* [RUCAIBox/LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) - The official GitHub page for the survey paper "A Survey of Large Language Models".
* [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) - Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.
* [datawhalechina/all-in-rag](https://github.com/datawhalechina/all-in-rag) - 🔍大模型应用开发实战一：RAG 技术全栈指南，在线阅读地址：https://datawhalechina.github.io/all-in-rag/
* [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) - A straightforward method for training your LLM, from downloading data to generating text.
* [adongwanai/AgentGuide](https://github.com/adongwanai/AgentGuide) - https://adongwanai.github.io/AgentGuide | AI Agent开发指南 | LangGraph实战 | 高级RAG | 转行大模型 | 大模型面试 | 算法工程师 | 面试题库 | 强化学习｜数据合成
* [poloclub/transformer-explainer](https://github.com/poloclub/transformer-explainer) - Transformer Explained Visually: Learn How LLM Transformer Models Work with Interactive Visualization
* [liyupi/codefather](https://github.com/liyupi/codefather) - 程序员鱼皮的编程宝典 ⭐️ 2026年最全编程学习路线图！包含Java学习路线、前端学习路线、Python学习路线、C++学习路线、算法学习路线、计算机基础学习路线、AI应用开发学习路线、AI Agent开发学习路线等。提供编程入门教程、AI大模型应用开发教程、RAG开发实战、MCP开发教程、Prompt工程指南、LLM应用开发、技术知识分享、学习资源推荐、项目实战教程、热门面试题、求职经验、简历优化、编程自学指南等内容，适用于所有零基础学编程、学习AI开发、转行程序员、计算机专业学生、求职找工作的同学 💎 编程学习，就来编程导航！
* [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) - 22 prompt engineering techniques with hands-on Jupyter Notebook tutorials, from fundamental concepts to advanced strategies for leveraging LLMs.
* [ed-donner/llm_engineering](https://github.com/ed-donner/llm_engineering) - Repo to accompany my mastering LLM engineering course
* [luhengshiwo/LLMForEverybody](https://github.com/luhengshiwo/LLMForEverybody) - 每个人都能看懂的大模型知识分享，LLMs春/秋招大模型面试前必看，让你和面试官侃侃而谈
* [DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) - LLM Zoomcamp - a free online course about real-life applications of LLMs. In 10 weeks you will learn how to build an AI system that answers questions about your knowledge base. Register here 👇🏼
* [nndl/llm-beginner](https://github.com/nndl/llm-beginner) - 《大模型与智能体》电子书与 6 个编程任务：Transformer、mini-GPT、SFT/DPO、RAG、工具调用与编程智能体。
* [ashishps1/learn-ai-engineering](https://github.com/ashishps1/learn-ai-engineering) - Learn AI and LLMs from scratch using free resources
* [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) - The most comprehensive Claude Code guide: agentic workflows, hooks, skills, MCP servers, quizzes, and production-ready templates. 430K+ lines.
* [bbycroft/llm-viz](https://github.com/bbycroft/llm-viz) - 3D Visualization of an GPT-style LLM
* [PacktPublishing/LLM-Engineers-Handbook](https://github.com/PacktPublishing/LLM-Engineers-Handbook) - The LLM's practical guide: From the fundamentals to deploying advanced LLM and RAG apps to AWS using LLMOps best practices
* [rasbt/reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch) - Implement a reasoning LLM in PyTorch from scratch, step by step
* [sgl-project/mini-sglang](https://github.com/sgl-project/mini-sglang) - A compact implementation of SGLang, designed to demystify the complexities of modern LLM serving systems.
* [changyeyu/LLM-RL-Visualized](https://github.com/changyeyu/LLM-RL-Visualized) - 🌟100+ 原创 LLM / RL 原理图📚，《大模型算法》作者巨献！💥（100+ LLM/RL Algorithm Maps ）
* [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) - Demystify AI agents by building them yourself. Local LLMs, no black boxes, real understanding of function calling, memory, and ReAct patterns.
* [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) - 🚀 2026 最系统的 AI Agent 速成指南｜智能体实战教程 · 完整学习路径 + 实战项目 + 面试题库 · 对标大模型应用开发工程师岗位 · 覆盖LangChain / LangGraph / Coze / Dify / MCP / skills / LLM / RAG / 提示词 · 企业级部署与微调 · 从0到企业级落地 + 从学习到上线项目 + 面试准备一体化
* [trigaten/Learn_Prompting](https://github.com/trigaten/Learn_Prompting) - Prompt Engineering, Generative AI, and LLM Guide by Learn Prompting | Join our discord for the largest Prompt Engineering learning community
* [origin-brain/beat-ai](https://github.com/origin-brain/beat-ai) - 不玩晦涩不搞少数派的 AI 入门圣经，从学生到工程师都能轻松掌握。涵盖神经网络到大模型、顶层设计到微观原理、工程实现到算法基础。 学完后，大家能彻底看懂为什么下一 token 预测这个看似不起眼的能力可以改变世界，也能发现原来 AI 并没有想象中那么神秘、那么高不可攀。 Let's just beat it !
* [TingsongYu/PyTorch-Tutorial-2nd](https://github.com/TingsongYu/PyTorch-Tutorial-2nd) - 《Pytorch实用教程》（第二版）无论是零基础入门，还是CV、NLP、LLM项目应用，或是进阶工程化部署落地，在这里都有。相信在本书的帮助下，读者将能够轻松掌握 PyTorch 的使用，成为一名优秀的深度学习工程师。
* [Hoper-J/AI-Guide-and-Demos-zh_CN](https://github.com/Hoper-J/AI-Guide-and-Demos-zh_CN) - 这是一份入门AI/LLM大模型的逐步指南，包含教程和演示代码，带你从API走进本地大模型部署和微调，代码文件会提供Kaggle或Colab在线版本，即便没有显卡也可以进行学习。项目中还开设了一个小型的代码游乐场🎡，你可以尝试在里面实验一些有意思的AI脚本。同时，包含李宏毅 (HUNG-YI LEE）2024生成式人工智能导论课程的完整中文镜像作业。
* [skyzh/tiny-llm](https://github.com/skyzh/tiny-llm) - learn LLM inference system on Apple Silicon for systems engineers: build a tiny vLLM + Qwen
* [LLMBook-zh/LLMBook-zh.github.io](https://github.com/LLMBook-zh/LLMBook-zh.github.io) - 《大语言模型》作者：赵鑫，李军毅，周昆，唐天一，文继荣
* [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) - 🚀 An open-source, hands-on curriculum bridging the gap from basic RL concepts to LLM alignment, RLVR, and advanced Agentic systems.
* [decodingai-magazine/llm-twin-course](https://github.com/decodingai-magazine/llm-twin-course) - 🤖 𝗟𝗲𝗮𝗿𝗻 for 𝗳𝗿𝗲𝗲 how to 𝗯𝘂𝗶𝗹𝗱 an end-to-end 𝗽𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻-𝗿𝗲𝗮𝗱𝘆 𝗟𝗟𝗠 & 𝗥𝗔𝗚 𝘀𝘆𝘀𝘁𝗲𝗺 using 𝗟𝗟𝗠𝗢𝗽𝘀 best practices: ~ 𝘴𝘰𝘶𝘳𝘤𝘦 𝘤𝘰𝘥𝘦 + 12 𝘩𝘢𝘯𝘥𝘴-𝘰𝘯 𝘭𝘦𝘴𝘴𝘰𝘯𝘴
* [datawhalechina/llms-from-scratch-cn](https://github.com/datawhalechina/llms-from-scratch-cn) - 仅需Python基础，从0构建大语言模型；从0逐步构建GLM4\Llama3\RWKV6， 深入理解大模型原理
* [ray-project/llm-numbers](https://github.com/ray-project/llm-numbers) - Numbers every LLM developer should know
* [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) - 《御舆：解码 Agent Harness》42万字拆解 AI Agent 的Harness骨架与神经 —— Claude Code 架构深度剖析，15 章从对话循环到构建你自己的 Agent Harness。在线阅读网站：
* [GiovanniPasq/agentic-rag-for-dummies](https://github.com/GiovanniPasq/agentic-rag-for-dummies) - A modular Agentic RAG built with LangGraph — learn Retrieval-Augmented Generation Agents in minutes.
* [bragai/bRAG-langchain](https://github.com/bragai/bRAG-langchain) - Everything you need to know to build your own RAG application
* [hemansnation/AI-Engineer-Headquarters](https://github.com/hemansnation/AI-Engineer-Headquarters) - A collection of scientific methods, processes, algorithms, and systems to build stories & models.
* [Windy3f3f3f3f/how-claude-code-works](https://github.com/Windy3f3f3f3f/how-claude-code-works) - Deep dive into Claude Code internals — architecture, agent loop, context engineering, and more. / 深入解析 Claude Code 源码：架构、Agent 循环、上下文工程、工具系统等
* [wyf3/llm_related](https://github.com/wyf3/llm_related) - 复现大模型相关算法及一些学习记录
* [iusztinpaul/hands-on-llms](https://github.com/iusztinpaul/hands-on-llms) - 🦖 𝗟𝗲𝗮𝗿𝗻 about 𝗟𝗟𝗠𝘀, 𝗟𝗟𝗠𝗢𝗽𝘀, and 𝘃𝗲𝗰𝘁𝗼𝗿 𝗗𝗕𝘀 for free by designing, training, and deploying a real-time financial advisor LLM system ~ 𝘴𝘰𝘶𝘳𝘤𝘦 𝘤𝘰𝘥𝘦 + 𝘷𝘪𝘥𝘦𝘰 & 𝘳𝘦𝘢𝘥𝘪𝘯𝘨 𝘮𝘢𝘵𝘦𝘳𝘪𝘢𝘭𝘴 *(archived)*
* [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch)
* [raiyanyahya/how-to-train-your-gpt](https://github.com/raiyanyahya/how-to-train-your-gpt) - Build a modern LLM from scratch. Every line commented. Explained like we are five.
* [ombharatiya/ai-system-design-guide](https://github.com/ombharatiya/ai-system-design-guide) - AI system design guide for engineers building production AI systems and evals.
* [wquguru/harness-books](https://github.com/wquguru/harness-books) - 📚 Two books on harness engineering — the design philosophies behind Claude Code & Codex: constraints, query loops, context governance, multi-agent verification. harness-books.agentway.dev
* [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) - A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。
* [decodingai-magazine/second-brain-ai-assistant-course](https://github.com/decodingai-magazine/second-brain-ai-assistant-course) - Learn to build your Second Brain AI assistant with LLMs, agents, RAG, fine-tuning, LLMOps and AI systems techniques.
* [datawhalechina/hugging-llm](https://github.com/datawhalechina/hugging-llm) - HuggingLLM, Hugging Future.
* [bbruceyuan/Hands-On-Large-Language-Models-CN](https://github.com/bbruceyuan/Hands-On-Large-Language-Models-CN) - 中文翻译的 Hands-On-Large-Language-Models (hands-on-llms)，动手学习大模型
* [MLNLP-World/LLMs-from-scratch-CN](https://github.com/MLNLP-World/LLMs-from-scratch-CN) - LLMs-from-scratch项目中文翻译
* [loveunk/deep-learning-llm-agent-notes](https://github.com/loveunk/deep-learning-llm-agent-notes) - 机器学习、深度学习的学习路径及知识总结
* [automata/aicodeguide](https://github.com/automata/aicodeguide) - AI Code Guide is a roadmap to start coding with AI
* [Windy3f3f3f3f/claude-code-from-scratch](https://github.com/Windy3f3f3f3f/claude-code-from-scratch) - Build your own Claude Code from scratch. 🔍 Claude Code 开源了 50 万行代码，读不动？用 ~5000 行 TypeScript / Python 从零复现核心架构，11 章分步教程带你理解 coding agent 精髓
* [echonoshy/cgft-llm](https://github.com/echonoshy/cgft-llm) - Practice to LLM.
* [athina-ai/rag-cookbooks](https://github.com/athina-ai/rag-cookbooks) - This repository contains various advanced techniques for Retrieval-Augmented Generation (RAG) systems.
* [datawhalechina/handy-ollama](https://github.com/datawhalechina/handy-ollama) - 动手学Ollama，CPU玩转大模型部署，在线阅读地址：https://datawhalechina.github.io/handy-ollama/
* [howl-anderson/unlocking-the-power-of-llms](https://github.com/howl-anderson/unlocking-the-power-of-llms) - 使用 Prompts 和 Chains 让 ChatGPT 成为神奇的生产力工具！Unlocking the power of LLMs.
* [hamzafarooq/building-llm-applications-from-scratch](https://github.com/hamzafarooq/building-llm-applications-from-scratch) - Code and Slides
* [adithya-s-k/AI-Engineering.academy](https://github.com/adithya-s-k/AI-Engineering.academy) - Mastering Applied AI, One Concept at a Time
* [hesamsheikh/ml-retreat](https://github.com/hesamsheikh/ml-retreat) - Machine Learning Journal for Intermediate to Advanced Topics.

### Examples and Exercises

* [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) - Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data. 🐳Docker-friendly.⚡Always in sync with Sharepoint, Google Drive, S3, Kafka, PostgreSQL, real-time data APIs, and more.
* [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) - Sample code and notebooks for Generative AI on Google Cloud, with Gemini Enterprise Agent Platform
* [wdndev/llm_interview_note](https://github.com/wdndev/llm_interview_note) - 主要记录大语言大模型（LLMs） 算法（应用）工程师相关的知识及面试题
* [e2b-dev/fragments](https://github.com/e2b-dev/fragments) - Open-source Next.js template for building apps that are fully generated by AI. By E2B.
* [liyupi/mianshiya](https://github.com/liyupi/mianshiya) - 持续维护的企业面试题库网站，帮你拿到满意 offer！⭐️ 2026年最新Java面试题、前端面试题、AI大模型面试题、AI Agent面试题、RAG面试题、C++面试题、Go面试题、Python面试题、测试面试题、运维面试题、后端面试题、操作系统面试题、计算机网络面试题、Redis面试题、MySQL数据库面试题、算法面试题、Spring面试题、JVM面试题、Java并发面试题、Linux面试题、LLM面试题、Prompt工程面试题、系统设计面试题等1万多道高频程序员求职必备八股文。面试刷题就选面试鸭 💎 React 前端 + Node 后端 + 云开发全栈项目 by 程序员鱼皮
* [WeThinkIn/AIGC-Interview-Book](https://github.com/WeThinkIn/AIGC-Interview-Book) - 【三年面试五年模拟】AIGC/LLM/AI Agent算法工程师面试资源平台。涵盖AIGC、LLM大模型、AI Agent、具身智能、传统深度学习、计算机视觉、自然语言处理、自动驾驶、机器学习、强化学习、大数据挖掘、世界模型、元宇宙、AGI等AI行业面试笔试干货经验与核心跨周期知识。
* [FareedKhan-dev/all-agentic-architectures](https://github.com/FareedKhan-dev/all-agentic-architectures) - 35 production-grade agentic AI architectures (Reflexion, LATS, GraphRAG, MemGPT, Voyager, BrowserAgent, ...) — a Python library and runnable textbook with multi-provider LLM support and a 17-task benchmark leaderboard.
* [daveebbelaar/ai-cookbook](https://github.com/daveebbelaar/ai-cookbook) - Examples and tutorials to help developers build AI systems
* [NVIDIA/GenerativeAIExamples](https://github.com/NVIDIA/GenerativeAIExamples) - Generative AI reference workflows optimized for accelerated infrastructure and microservice architecture.
* [datawhalechina/daily-interview](https://github.com/datawhalechina/daily-interview) - Datawhale成员整理的面经，内容包括机器学习，CV，NLP，推荐，开发等，欢迎大家star
* [NVIDIA/ChatRTX](https://github.com/NVIDIA/ChatRTX) - A developer reference project for creating Retrieval Augmented Generation (RAG) chatbots on Windows using TensorRT-LLM *(archived)*
* [amitshekhariitbhu/ai-engineering-interview-questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions) - Your Cheat Sheet for AI Engineering Interview – Questions and Answers.
* [pinecone-io/examples](https://github.com/pinecone-io/examples) - Jupyter Notebooks to help you get hands-on with Pinecone vector databases
* [ashishpatel26/LLM-Finetuning](https://github.com/ashishpatel26/LLM-Finetuning) - LLM Finetuning with peft
* [315386775/DeepLearing-Interview-Awesome-2024](https://github.com/315386775/DeepLearing-Interview-Awesome-2024) - AIGC-interview/CV-interview/LLMs-interview面试问题与答案集合仓，同时包含工作和科研过程中的新想法、新问题、新资源与新项目
* [km1994/LLMs_interview_notes](https://github.com/km1994/LLMs_interview_notes) - 该仓库主要记录 大模型（LLMs） 算法工程师相关的面试题
* [Exorust/TorchLeet](https://github.com/Exorust/TorchLeet) - LeetCode for PyTorch — 65 ML/AI interview problems from real interviews at Google, Meta, Anthropic. Jupyter notebooks, an auto-grader, and an MCP AI tutor.
* [milvus-io/bootcamp](https://github.com/milvus-io/bootcamp) - Dealing with all unstructured data, such as reverse image search, audio search, molecular search, video analysis, question and answer systems, NLP, etc.

### Awesome Lists and Collections

* [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
* [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) - Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.
* [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins
* [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - Awesome-LLM: a curated list of Large Language Model
* [mikeroyal/Self-Hosting-Guide](https://github.com/mikeroyal/Self-Hosting-Guide) - Self-Hosting Guide. Learn all about locally hosting (on premises & private web servers) and managing software applications by yourself or your organization. Including Cloud, LLMs, WireGuard, Automation, Home Assistant, and Networking.
* [AiHubCN/Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM) - 整理开源的中文大语言模型，以规模较小、可私有化部署、训练成本较低的模型为主，包括底座模型，垂直领域微调及应用，数据集与教程等。
* [davideuler/architecture.of.internet-product](https://github.com/davideuler/architecture.of.internet-product) - 互联网公司技术架构，微信/淘宝/微博/腾讯/阿里/美团点评/百度/OpenAI/Google/Facebook/Amazon/eBay的架构，欢迎PR补充
* [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) - A collection of projects showcasing RAG, agents, workflows, and other AI use cases
* [jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) - Collection of leaked system prompts
* [eugeneyan/open-llms](https://github.com/eugeneyan/open-llms) - 📋 A list of open LLMs available for commercial use.
* [steven2358/awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) - A curated list of modern Generative Artificial Intelligence projects and services
* [KalyanKS-NLP/llm-engineer-toolkit](https://github.com/KalyanKS-NLP/llm-engineer-toolkit) - A curated list of 120+ LLM libraries category wise.
* [Mooler0410/LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) - A curated list of practical guide resources of LLMs (LLMs Tree, Examples, Papers)
* [kyrolabs/awesome-langchain](https://github.com/kyrolabs/awesome-langchain) - 😎 Awesome list of tools and projects with the awesome LangChain framework
* [yzhao062/anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources) - Anomaly detection related books, papers, videos, and toolboxes. Last update late 2025 for LLM and VLM works!
* [WangRongsheng/awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) - 🧑‍🚀 全世界最好的LLM资料总结（多模态生成、Agent、辅助编程、AI审稿、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources.
* [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) - The paper list of the 86-page SCIS cover paper "The Rise and Potential of Large Language Model Based Agents: A Survey" by Zhiheng Xi et al.
* [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) - List of Permanent Free LLM API (API Keys)
* [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) - A trilingual (繁中 / English / 简中) learning roadmap for agentic AI: from LLM basics to multi-agent systems, with 240+ curated resources and hands-on examples. 中文 AI agent 學習地圖。
* [hijkzzz/Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) - A collection of LLM papers, blogs, and projects, with a focus on OpenAI o1 🍓 and reasoning techniques.
* [fr0gger/Awesome-GPT-Agents](https://github.com/fr0gger/Awesome-GPT-Agents) - A curated list of GPT agents for cybersecurity
* [georgezouq/awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) - 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
* [wgwang/awesome-LLMs-In-China](https://github.com/wgwang/awesome-LLMs-In-China) - 中国大模型
* [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) - Tutorials, Guides and Agent Skills Directories
* [ikaijua/Awesome-AITools](https://github.com/ikaijua/Awesome-AITools) - Collection of AI-related utilities. Welcome to submit pull requests /收藏AI相关的实用工具，欢迎提交pull requests
* [tensorchord/Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) - An awesome & curated list of best LLMOps tools for developers
* [lonePatient/awesome-pretrained-chinese-nlp-models](https://github.com/lonePatient/awesome-pretrained-chinese-nlp-models) - Awesome Pretrained Chinese NLP Models，高质量中文预训练模型&大模型&多模态模型&大语言模型集合
* [xlite-dev/Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) - 📚A curated list of Awesome LLM/VLM Inference Papers with Codes: Flash-Attention, Paged-Attention, WINT8/4, Parallelism, etc.🎉
* [0xeb/TheBigPromptLibrary](https://github.com/0xeb/TheBigPromptLibrary) - A collection of prompts, system prompts and LLM instructions
* [SylphAI-Inc/LLM-engineer-handbook](https://github.com/SylphAI-Inc/LLM-engineer-handbook) - A curated list of Large Language Model resources, covering model training, serving, fine-tuning, and building LLM applications.
* [mlabonne/llm-datasets](https://github.com/mlabonne/llm-datasets) - Curated list of datasets and tools for post-training.
* [alvinreal/awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai) - Curated list of the best truly open-source AI projects, models, tools, and infrastructure. Daily updated.
* [luban-agi/Awesome-AIGC-Tutorials](https://github.com/luban-agi/Awesome-AIGC-Tutorials) - Curated tutorials and resources for Large Language Models, AI Painting, and more.
* [GT-RIPL/Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) - A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites
* [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) - 🇨🇳 OpenClaw中文用例大全 | 50个真实场景 | 国内特色 + 海外案例的国内适配 | 自动化办公·内容创作·运维·AI助理·知识管理 | 新手友好
* [HuaizhengZhang/AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) - 🚀 Awesome System for Machine Learning ⚡️ AI System Papers and Industry Practice. ⚡️ System for Machine Learning, LLM (Large Language Model), GenAI (Generative AI). 🍻 OSDI, NSDI, SIGCOMM, SoCC, MLSys, etc. 🗃️ Llama3, Mistral, etc. 🧑‍💻 Video Tutorials.
* [eseckel/ai-for-grant-writing](https://github.com/eseckel/ai-for-grant-writing) - A curated list of resources for using LLMs to develop more competitive grant applications.
* [walkinglabs/awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) - 🛠️ Awesome tools & guides for harness engineering.
* [killop/anything_about_game](https://github.com/killop/anything_about_game) - A wonderful list of Game Development resources.
* [billmei/every-chatgpt-gui](https://github.com/billmei/every-chatgpt-gui) - Every front-end GUI client for ChatGPT, Claude, and other LLMs
* [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - 162 production-ready AI agent templates for OpenClaw. SOUL.md configs across 19 categories. Submit yours!
* [eosphoros-ai/Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) - Curated tutorials and resources for Large Language Models, Text2SQL, Text2DSL、Text2API、Text2Vis and more.
* [cbamls/AI_Tutorial](https://github.com/cbamls/AI_Tutorial) - 大厂发布的AI落地实践、顶尖实验室的最新论文、工业界的真实踩坑记录
* [atfortes/Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) - From Chain-of-Thought prompting to OpenAI o1 and DeepSeek-R1 🍓
* [filipecalegario/awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) - A curated list of Generative AI tools, works, models, and references
* [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) - [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets.
* [DSXiangLi/DecryptPrompt](https://github.com/DSXiangLi/DecryptPrompt) - 总结Prompt&LLM论文，开源数据&模型，AIGC应用
* [Zjh-819/LLMDataHub](https://github.com/Zjh-819/LLMDataHub) - A quick guide (especially) for trending instruction finetuning datasets
* [Sumanth077/ai-engineering-toolkit](https://github.com/Sumanth077/ai-engineering-toolkit) - A curated list of 100+ libraries and frameworks for AI engineers building with LLMs
* [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) - 🔥 Comprehensive survey on Context Engineering: from prompt engineering to production-grade AI systems. hundreds of papers, frameworks, and implementation guides for LLMs and AI agents.
* [yunlong10/Awesome-LLMs-for-Video-Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding) - 🔥🔥🔥 [IEEE TCSVT] Latest Papers, Codes and Datasets on Vid-LLMs.
* [taishi-i/awesome-ChatGPT-repositories](https://github.com/taishi-i/awesome-ChatGPT-repositories) - A curated list of open source GitHub repositories related to ChatGPT, the OpenAI API, and Codex. Searchable via Claude Code skills.
* [zjunlp/LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) - Must-read Papers on LLM Agents.
* [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) - 134+ free LLM APIs & AI API keys from 40+ providers. Google Gemini, NVIDIA NIM, Groq, OpenRouter & more. One-click setup for Claude Code, Cursor and Codex.
* [Paitesanshi/LLM-Agent-Survey](https://github.com/Paitesanshi/LLM-Agent-Survey)
* [FreedomIntelligence/Awesome-AI4Med](https://github.com/FreedomIntelligence/Awesome-AI4Med) - A curated list of medical LLMs, multimodal systems, datasets, benchmarks, and more. 🏥
* [rafska/awesome-local-llm](https://github.com/rafska/awesome-local-llm) - A curated list of awesome platforms, tools, practices and resources that helps run LLMs locally
* [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) - [Up-to-date] Large Language Model Agent: A Survey on Methodology, Applications and Challenges
* [underlines/awesome-ml](https://github.com/underlines/awesome-ml) - Curated list of useful LLM / Analytics / Datascience resources
* [InterviewReady/ai-engineering-resources](https://github.com/InterviewReady/ai-engineering-resources) - Research papers and blogs to transition to AI Engineering
* [RManLuo/Awesome-LLM-KG](https://github.com/RManLuo/Awesome-LLM-KG) - Awesome papers about unifying LLMs and KGs
* [guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) - Awesome Deep Learning papers for industrial Search, Recommendation and Advertisement. They focus on Embedding, Matching, Pre-Ranking, Ranking, Post Ranking, Relevance, LLM and RL. Please cite our paper "Deep Learning to Rank in Industrial Search Engines, Recommender Systems, and Online Advertising - An Overview and New Perspectives" (TOIS 2026).
* [luban-agi/Awesome-Domain-LLM](https://github.com/luban-agi/Awesome-Domain-LLM) - 收集和梳理垂直领域的开源模型、数据集及评测基准。
* [mbzuai-oryx/Awesome-LLM-Post-training](https://github.com/mbzuai-oryx/Awesome-LLM-Post-training) - Awesome Reasoning LLM Tutorial/Survey/Guide
* [TsinghuaC3I/Awesome-RL-for-LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) - A Survey of Reinforcement Learning for Large Reasoning Models
* [XiaoxinHe/Awesome-Graph-LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) - A collection of AWESOME things about Graph-Related LLMs.
* [AGI-Edgerunners/LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) - A repo lists papers related to LLM based agent

## Language and Tooling

### Editor and IDE Support

* [voideditor/void](https://github.com/voideditor/void) - *(archived)*
* [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) - ✨ AI Coding, Vim Style
* [PawanOsman/OpenCursor](https://github.com/PawanOsman/OpenCursor) - Open-source Cursor-like AI coding agent for VS Code - agentic chat, multi-provider LLMs (OpenAI, Ollama, llama.cpp), semantic search, and MCP support
* [kodu-ai/claude-coder](https://github.com/kodu-ai/claude-coder) - Kodu is an autonomous coding agent that lives in your IDE. It is a VSCode extension that can help you build your dream project step by step by leveraging the latest technologies in automated coding agents
* [karthink/gptel](https://github.com/karthink/gptel) - A simple, extensible LLM client for Emacs
* [SilasMarvin/lsp-ai](https://github.com/SilasMarvin/lsp-ai) - LSP-AI is an open-source language server that serves as a backend for AI-powered functionality, designed to assist and empower software engineers, not replace them.
* [nicepkg/aide](https://github.com/nicepkg/aide) - Conquer Any Code in VSCode: One-Click Comments, Conversions, UI-to-Code, and AI Batch Processing of Files! 在 VSCode 中征服任何代码：一键注释、转换、UI 图生成代码、AI 批量处理文件！💪

### Version Control

* [alibaba/open-code-review](https://github.com/alibaba/open-code-review) - Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.
* [idosal/git-mcp](https://github.com/idosal/git-mcp) - Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project
* [di-sukharev/opencommit](https://github.com/di-sukharev/opencommit) - top #1 and most feature rich GPT wrapper for git — generate commit messages with an LLM in 1 sec — works with Claude, GPT and every other provider, supports local Ollama models too
* [jnsahaj/lumen](https://github.com/jnsahaj/lumen) - Beautiful git diff viewer, generate commits with AI, get summary of changes, all from the CLI
* [zurawiki/gptcommit](https://github.com/zurawiki/gptcommit) - A git prepare-commit-msg hook for authoring commit messages with LLMs.

## Web

### Frontend and UI Components

* [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) - The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more. Makers of the AG-UI Protocol
* [Chainlit/chainlit](https://github.com/Chainlit/chainlit) - Build Conversational AI in minutes ⚡️
* [thesysdev/openui](https://github.com/thesysdev/openui) - The Open Standard for Generative UI
* [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) - TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code, Codex) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically.
* [neomjs/neo](https://github.com/neomjs/neo) - Neo.mjs is a self-evolving software organism: a professional end-to-end AI engineering team whose cross-model swarm inhabits live apps via Neural Link, Active Hybrid GraphRAG, DreamService, and self-healing loops.
* [CommandCodeAI/langui](https://github.com/CommandCodeAI/langui) - UI for your AI. Open Source Tailwind components tailored for your GPT, generative AI, and LLM projects.
* [Simon-He95/markstream-vue](https://github.com/Simon-He95/markstream-vue) - Multi-framework streaming Markdown renderers for AI apps: Vue/Nuxt, React/Next.js, Svelte, and Angular, with Mermaid, KaTeX, stream-diffs code blocks, safe HTML, and low-jitter updates.
* [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) - A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native
* [lobehub/lobe-icons](https://github.com/lobehub/lobe-icons) - 🥨 Lobe Icons - Brings AI/LLM brand logos to your React & React Native apps — static SVG/PNG/WebP, no dependencies.

### Scraping and Crawling

* [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) - The web data API to search, scrape, and interact at scale. 🔥
* [browser-use/browser-use](https://github.com/browser-use/browser-use) - Agents that use the browser.
* [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN
* [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) - Python scraper based on AI
* [apify/crawlee](https://github.com/apify/crawlee) - Crawlee—A web scraping and browser automation library for Node.js to build reliable crawlers. In JavaScript and TypeScript. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works with Puppeteer, Playwright, Cheerio, JSDOM, and raw HTTP. Both headful and headless mode. With proxy rotation.
* [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) - Automate browser based workflows with AI
* [browser-use/browser-harness](https://github.com/browser-use/browser-harness) - Browser Harness | Self-healing harness that enables LLMs to complete any task.
* [nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser) - Open-Source Chrome extension for AI-powered web automation. Run multi-agent workflows using your own LLM API key. Alternative to OpenAI Operator.
* [jina-ai/reader](https://github.com/jina-ai/reader) - Convert any URL to an LLM-friendly input with a simple prefix https://r.jina.ai/
* [apify/crawlee-python](https://github.com/apify/crawlee-python) - Crawlee—A web scraping and browser automation library for Python to build reliable crawlers. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works with Parsel, BeautifulSoup, Playwright, and raw HTTP. Both headful and headless mode. With proxy rotation.
* [steel-dev/steel-browser](https://github.com/steel-dev/steel-browser) - 🔥 Open Source Browser API for AI Agents & Apps. Steel Browser is a batteries-included browser sandbox that lets you automate the web without worrying about infrastructure.
* [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) - 🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.
* [mishushakov/llm-scraper](https://github.com/mishushakov/llm-scraper) - Turn any webpage into structured data using LLMs
* [adbar/trafilatura](https://github.com/adbar/trafilatura) - Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML
* [any4ai/AnyCrawl](https://github.com/any4ai/AnyCrawl) - AnyCrawl 🚀: A Node.js/TypeScript crawler that turns websites into LLM-ready data and extracts structured SERP results from Google/Bing/Baidu/etc. Native multi-threading for bulk processing.
* [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) - Allow LLMs to control a browser with Browserbase and Stagehand *(archived)*
* [oxylabs/oxylabs-ai-studio-py](https://github.com/oxylabs/oxylabs-ai-studio-py) - Structured data gathering from any website using AI-powered scraper, crawler, and browser automation. Scraping and crawling with natural language prompts. Equip your LLM agents with fresh data. AI Studio python SDK for intelligent web data gathering. *(archived)*
* [itsOwen/CyberScraper-2077](https://github.com/itsOwen/CyberScraper-2077) - A Powerful web scraper powered by LLM | OpenAI, Gemini & Ollama
* [keon/browser-control](https://github.com/keon/browser-control) - A tiny, fast Rust CLI that drives a real browser over the Chrome DevTools Protocol — built for coding agents.
* [spider-rs/spider](https://github.com/spider-rs/spider) - Foundational low latency web data collecting in Rust
* [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) - A powerful Model Context Protocol (MCP) server that provides an all-in-one solution for public web access.
* [lmnr-ai/index](https://github.com/lmnr-ai/index) - The SOTA Open-Source Browser Agent for autonomously performing complex tasks on the web *(archived)*

## Data and Storage

### Databases

* [milvus-io/milvus](https://github.com/milvus-io/milvus) - Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search
* [activeloopai/deeplake](https://github.com/activeloopai/deeplake) - Deeplake is AI Data Runtime for Agents. It provides serverless postgres with a multimodal datalake, enabling scalable retrieval and training.
* [postgresml/postgresml](https://github.com/postgresml/postgresml) - Postgres with GPUs for ML/AI apps.
* [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) - A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation. Our goal is to provide the best Knowledge Graph for LLM (GraphRAG).
* [timescale/pgai](https://github.com/timescale/pgai) - A suite of tools to develop RAG, semantic search, and other AI applications more easily with PostgreSQL *(archived)*
* [infiniflow/infinity](https://github.com/infiniflow/infinity) - The AI-native database built for LLM applications, providing incredibly fast hybrid search of dense vector, sparse vector, tensor (multi-vector), and full-text.
* [spiceai/spiceai](https://github.com/spiceai/spiceai) - Add a real-time analytics node to your operational database. Spice is a portable, accelerated SQL query, search, and LLM-inference engine in Rust for data-grounded AI apps and agents.
* [supabase-community/database-build](https://github.com/supabase-community/database-build) - In-browser Postgres sandbox with AI assistance (formerly postgres.new)
* [georgia-tech-db/evadb](https://github.com/georgia-tech-db/evadb) - Database system for AI-powered apps *(archived)*
* [openlake-project/openlake](https://github.com/openlake-project/openlake) - OpenLake is a high performance storage engine for efficient LLM inference and GPU Training
* [lealone/Lealone](https://github.com/lealone/Lealone) - 能安全适用于氛围编程和企业应用的全栈自进化通用智能体

### Serialization and Formats

* [toon-format/toon](https://github.com/toon-format/toon) - 🎒 Token-Oriented Object Notation (TOON) – compact, human-readable serialization of JSON data for LLM prompts. TypeScript SDK, CLI, benchmarks.
* [The-Vibe-Company/megaparse](https://github.com/The-Vibe-Company/megaparse) - File Parser optimised for LLM Ingestion with no loss 🧠 Parse PDFs, Docx, PPTx in a format that is ideal for LLMs.
* [mangiucugna/json_repair](https://github.com/mangiucugna/json_repair) - Repair malformed JSON from LLMs, APIs, logs, and user input in Python.
* [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) - A Model Context Protocol server for Excel file manipulation
* [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) - The /llms.txt file, helping language models use your website

## Machine Learning and AI

### LLM and Inference

* [ollama/ollama](https://github.com/ollama/ollama) - Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.
* [f/prompts.chat](https://github.com/f/prompts.chat) - f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
* [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) - LLM inference in C/C++
* [vllm-project/vllm](https://github.com/vllm-project/vllm) - A high-throughput and memory-efficient inference and serving engine for LLMs
* [infiniflow/ragflow](https://github.com/infiniflow/ragflow) - RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
* [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) - GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use.
* [unslothai/unsloth](https://github.com/unslothai/unsloth) - Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4, MiniMax-H3, Gemma 4, FLUX and more.
* [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) - Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)
* [BerriAI/litellm](https://github.com/BerriAI/litellm) - The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]
* [run-llama/llama_index](https://github.com/run-llama/llama_index) - LlamaIndex is the document processing platform for AI
* [mudler/LocalAI](https://github.com/mudler/LocalAI) - LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.
* [QuantumNous/new-api](https://github.com/QuantumNous/new-api) - A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatible, Claude-compatible, or Gemini-compatible formats. A centralized gateway for personal and enterprise model management.
* [microsoft/BitNet](https://github.com/microsoft/BitNet) - Official inference framework for 1-bit LLMs
* [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) - [EMNLP2025] LightRAG: Simple and Fast Retrieval-Augmented Generation
* [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr) - Opiniated RAG for integrating GenAI in your apps 🧠 Focus on your product rather than the RAG. Easy integration in existing products with customisation! Any LLM: GPT4, Groq, Llama. Any Vectorstore: PGVector, Faiss. Any Files. Anyway you want.
* [songquanpeng/one-api](https://github.com/songquanpeng/one-api) - LLM API 管理 & 分发系统，支持 OpenAI、Azure、Anthropic Claude、Google Gemini、DeepSeek、字节豆包、ChatGLM、文心一言、讯飞星火、通义千问、360 智脑、腾讯混元等主流模型，统一 API 适配，可用于 key 管理与二次分发。单可执行文件，提供 Docker 镜像，一键部署，开箱即用。LLM API management & key redistribution system, unifying multiple providers under a single API. Single binary, Docker-ready, with an English UI.
* [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) - Hundreds of models & providers. One command to find what runs on your hardware.
* [sgl-project/sglang](https://github.com/sgl-project/sglang) - SGLang is a high-performance serving framework for large language models and multimodal models.
* [microsoft/graphrag](https://github.com/microsoft/graphrag) - A modular graph-based Retrieval-Augmented Generation (RAG) system
* [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) - 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG
* [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) - An AI prompt optimizer for writing better prompts and getting better AI results.
* [lyogavin/airllm](https://github.com/lyogavin/airllm) - AirLLM 70B inference with single 4GB GPU
* [p-e-w/heretic](https://github.com/p-e-w/heretic) - Fully automatic censorship removal for language models
* [decolua/9router](https://github.com/decolua/9router) - Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits.
* [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) - 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only.
* [Tencent/WeKnora](https://github.com/Tencent/WeKnora) - Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
* [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) - Distribute and run LLMs with a single file.
* [mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm) - Universal LLM Deployment Engine with ML Compilation
* [jundot/omlx](https://github.com/jundot/omlx) - LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar
* [QwenLM/Qwen](https://github.com/QwenLM/Qwen) - The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud.
* [huggingface/peft](https://github.com/huggingface/peft) - 🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning.
* [kvcache-ai/ktransformers](https://github.com/kvcache-ai/ktransformers) - A Flexible Framework for Experiencing Heterogeneous LLM Inference/Fine-tune Optimizations
* [mlc-ai/web-llm](https://github.com/mlc-ai/web-llm) - High-performance In-browser LLM Inference Engine
* [ymcui/Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) - 中文LLaMA&Alpaca大语言模型+本地CPU/GPU训练部署 (Chinese LLaMA & Alpaca LLMs)
* [xming521/WeClone](https://github.com/xming521/WeClone) - 🚀 One-stop solution for creating your AI twin from chat history 💡 Fine-tune LLMs with your chat logs to capture your unique style, then bind to a chatbot to bring your digital self to life.
* [deepseek-ai/Janus](https://github.com/deepseek-ai/Janus) - Janus-Series: Unified Multimodal Understanding and Generation Models
* [modelscope/ms-swift](https://github.com/modelscope/ms-swift) - Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.6, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 300+ MLLMs (Qwen3-VL, Qwen3-Omni, InternVL3.5, Ovis2.5, GLM4.5v, Gemma4, Llava, Phi4, ...) (AAAI 2025).
* [zai-org/ChatGLM2-6B](https://github.com/zai-org/ChatGLM2-6B) - ChatGLM2-6B: An Open Bilingual Chat LLM | 开源双语对话语言模型
* [GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm) - Nano vLLM
* [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) - Universal provider proxy for OpenAI Codex & Claude Code — use any LLM (Claude, Gemini, Grok, DeepSeek, Ollama…) with Codex CLI, App, SDK, and Claude Code
* [llmware-ai/llmware](https://github.com/llmware-ai/llmware) - Unified framework for building enterprise RAG pipelines with small, specialized models
* [LlamaChinese/Llama-Chinese](https://github.com/LlamaChinese/Llama-Chinese) - Llama中文社区，实时汇总最新Llama学习资料，构建最好的中文Llama大模型开源生态，完全开源可商用
* [BlinkDL/RWKV-LM](https://github.com/BlinkDL/RWKV-LM) - RWKV (pronounced RwaKuv) is an RNN with great LLM performance, which can also be directly trained like a GPT transformer (parallelizable). We are at RWKV-7 "Goose". So it's combining the best of RNN and transformer - great performance, linear time, constant space (no kv-cache), fast training, infinite ctx_len, and free sentence embedding.
* [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way.
* [567-labs/instructor](https://github.com/567-labs/instructor) - structured outputs for llms
* [Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt) - 20+ high-performance LLMs with recipes to pretrain, finetune and deploy at scale.
* [zai-org/ChatGLM3](https://github.com/zai-org/ChatGLM3) - ChatGLM3 series: Open Bilingual Chat LLMs | 开源双语对话语言模型
* [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) - A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.
* [cocktailpeanut/dalai](https://github.com/cocktailpeanut/dalai) - The simplest way to run LLaMA on your local machine
* [bentoml/OpenLLM](https://github.com/bentoml/OpenLLM) - Run any open-source LLMs, such as DeepSeek and Llama, as OpenAI compatible API endpoint in the cloud.
* [simonw/llm](https://github.com/simonw/llm) - Access large language models from the command-line
* [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Go ahead and axolotl questions
* [LMCache/LMCache](https://github.com/LMCache/LMCache) - LMCache: Supercharge Your LLM with the Fastest KV Cache Layer
* [cactus-compute/needle](https://github.com/cactus-compute/needle) - Automation foundation model for tiny devices: 2-bit, 8-29 MB, tool calls, structured extraction and embeddings on phones, wearables, smart homes, robots, cars and microcontrollers.
* [microsoft/promptflow](https://github.com/microsoft/promptflow) - Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring.
* [OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) - MiniCPM5: SOTA on-device LLMs, small yet powerful.
* [artidoro/qlora](https://github.com/artidoro/qlora) - QLoRA: Efficient Finetuning of Quantized LLMs
* [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) - Official inference library for Mistral models *(archived)*
* [bigscience-workshop/petals](https://github.com/bigscience-workshop/petals) - 🌸 Run LLMs at home, BitTorrent-style. Fine-tuning and inference up to 10x faster than offloading
* [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) - Production ready toolkit to run AI locally
* [Tiiny-AI/PowerInfer](https://github.com/Tiiny-AI/PowerInfer) - High-speed Large Language Model Serving for Local Deployment
* [xorbitsai/inference](https://github.com/xorbitsai/inference) - Swap GPT for any LLM by changing a single line of code. Xinference lets you run open-source, speech, and multimodal models on cloud, on-prem, or your laptop — all through one unified, production-ready inference API.
* [nlpxucan/WizardLM](https://github.com/nlpxucan/WizardLM) - LLMs build upon Evol Insturct: WizardLM, WizardCoder, WizardMath
* [oumi-ai/oumi](https://github.com/oumi-ai/oumi) - Easily fine-tune, evaluate and deploy Qwen, Gemma, or any open weight LLM!
* [FMInference/FlexLLMGen](https://github.com/FMInference/FlexLLMGen) - Running large language models on a single GPU for throughput-oriented scenarios. *(archived)*
* [coaidev/coai](https://github.com/coaidev/coai) - 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Support for 200+ Models And 35+ Providers, Load Balacing w/ Priority-base Routing, Cost Management, Chat Share, Cloud Sync, Credit/Subscription Billing, All File Parsing, Web Search, Built-in Model Cache.
* [bentoml/BentoML](https://github.com/bentoml/BentoML) - The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more!
* [intel/ipex-llm](https://github.com/intel/ipex-llm) - Accelerate local LLM inference and finetuning (LLaMA, Mistral, ChatGLM, Qwen, DeepSeek, Mixtral, Gemma, Phi, MiniCPM, Qwen-VL, MiniCPM-V, etc.) on Intel XPU (e.g., local PC with iGPU and NPU, discrete GPU such as Arc, Flex and Max); seamlessly integrate with llama.cpp, Ollama, HuggingFace, LangChain, LlamaIndex, vLLM, DeepSpeed, Axolotl, etc. *(archived)*
* [microsoft/TypeChat](https://github.com/microsoft/TypeChat) - TypeChat is a library that makes it easy to build natural language interfaces using types.
* [THUDM/slime](https://github.com/THUDM/slime) - slime is an LLM post-training framework for RL Scaling.
* [bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) - Accessible large language models via k-bit quantization for PyTorch.
* [qualcomm/GenieX](https://github.com/qualcomm/GenieX) - Run frontier LLMs and VLMs locally on Qualcomm devices across NPU, GPU, and CPU with a few lines of code
* [maximhq/bifrost](https://github.com/maximhq/bifrost) - Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS.
* [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) - LMDeploy is a toolkit for compressing, deploying, and serving LLMs.
* [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) - A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU.
* [PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE) - The official repository for ERNIE 4.5 and ERNIEKit – its industrial-grade development toolkit based on PaddlePaddle.
* [EricLBuehler/mistral.rs](https://github.com/EricLBuehler/mistral.rs) - Fast, flexible LLM inference
* [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) - Adding guardrails to large language models.
* [arcee-ai/mergekit](https://github.com/arcee-ai/mergekit) - Tools for merging pretrained large language models.
* [InternLM/InternLM](https://github.com/InternLM/InternLM) - Official release of InternLM series (InternLM, InternLM2, InternLM2.5, InternLM3).
* [mit-han-lab/streaming-llm](https://github.com/mit-han-lab/streaming-llm) - [ICLR 2024] Efficient Streaming Language Models with Attention Sinks
* [deepseek-ai/DeepSeek-LLM](https://github.com/deepseek-ai/DeepSeek-LLM) - DeepSeek LLM: Let there be answers
* [zai-org/GLM-5](https://github.com/zai-org/GLM-5) - GLM-5: From Vibe Coding to Agentic Engineering
* [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems.
* [ymcui/Chinese-LLaMA-Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2) - 中文LLaMA-2 & Alpaca-2大模型二期项目 + 64K超长上下文模型 (Chinese LLaMA-2 & Alpaca-2 LLMs with 64K long context models)
* [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) - Run LLMs with MLX
* [katanemo/plano](https://github.com/katanemo/plano) - Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routing, observability, agent orchestration, and guardrails so you stay focused on your agents core logic.
* [tbphp/gpt-load](https://github.com/tbphp/gpt-load) - Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription accounts, scheduling, failover, request logs and usage. 自托管 AI 网关：多渠道多凭据统一接入，含密钥与订阅账号、调度容错、日志与用量。
* [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup) - Fine-tune LLMs from one YAML. Layer streaming trains an 8B model on a 4 GB laptop GPU.
* [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) - Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook
* [microsoft/LLMLingua](https://github.com/microsoft/LLMLingua) - [EMNLP'23, ACL'24] To speed up LLMs' inference and enhance LLM's perceive of key information, compress the prompt and KV-Cache, which achieves up to 20x compression with minimal performance loss.
* [yangjianxin1/Firefly](https://github.com/yangjianxin1/Firefly) - Firefly: 大模型训练工具，支持训练Qwen2.5、Qwen2、Yi1.5、Phi-3、Llama3、Gemma、MiniCPM、Yi、Deepseek、Orion、Xverse、Mixtral-8x7B、Zephyr、Mistral、Baichuan2、Llma2、Llama、Qwen、Baichuan、ChatGLM2、InternLM、Ziya2、Vicuna、Bloom等大模型
* [linkedin/Liger-Kernel](https://github.com/linkedin/Liger-Kernel) - Efficient Triton Kernels for LLM Training
* [kvcache-ai/Mooncake](https://github.com/kvcache-ai/Mooncake) - Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI.
* [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) - The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC payments on Base & Solana via x402.
* [flashinfer-ai/flashinfer](https://github.com/flashinfer-ai/flashinfer) - FlashInfer: Kernel Library for LLM Serving
* [Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel) - The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.
* [rustformers/llm](https://github.com/rustformers/llm) - [Unmaintained, see README] An ecosystem of Rust libraries for working with large language models *(archived)*
* [princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) - [NeurIPS 2023] Tree of Thoughts: Deliberate Problem Solving with Large Language Models
* [cactus-compute/cactus](https://github.com/cactus-compute/cactus) - Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.
* [vllm-project/semantic-router](https://github.com/vllm-project/semantic-router) - A programmable Mixture-of-Models router for heterogeneous LLM inference
* [rllm-org/rllm](https://github.com/rllm-org/rllm) - Democratizing Reinforcement Learning for LLMs
* [areal-project/AReaL](https://github.com/areal-project/AReaL) - The RL Bridge for LLM-based Agent Applications. Made Simple & Flexible.
* [lemonade-sdk/lemonade](https://github.com/lemonade-sdk/lemonade) - Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk
* [google-deepmind/gemma](https://github.com/google-deepmind/gemma) - Gemma open-weight LLM library, from Google DeepMind
* [gpustack/gpustack](https://github.com/gpustack/gpustack) - A GPU cluster manager for high-performance AI model serving (vLLM, SGLang) and on-demand SSH-accessible GPU instances.
* [huggingface/alignment-handbook](https://github.com/huggingface/alignment-handbook) - Robust recipes to align language models with human and AI preferences
* [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) - MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) on your Mac using MLX.
* [lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM) - A framework for serving and evaluating LLM routers - save LLM costs without compromising quality
* [PeterGriffinJin/Search-R1](https://github.com/PeterGriffinJin/Search-R1) - Search-R1: An Efficient, Scalable RL Training Framework for Reasoning & Search Engine Calling interleaved LLM based on veRL
* [winfunc/deepreasoning](https://github.com/winfunc/deepreasoning) - A high-performance LLM inference API and Chat UI that integrates DeepSeek R1's CoT reasoning traces with Anthropic Claude models.
* [looplj/axonhub](https://github.com/looplj/axonhub) - ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-end tracing.
* [InternLM/xtuner](https://github.com/InternLM/xtuner) - A Next-Generation Training Engine Built for Ultra-Large MoE Models
* [h2oai/h2o-llmstudio](https://github.com/h2oai/h2o-llmstudio) - H2O LLM Studio - a framework and no-code GUI for fine-tuning LLMs. Documentation: https://docs.h2o.ai/h2o-llmstudio/
* [salesforce/CodeGen](https://github.com/salesforce/CodeGen) - CodeGen is a family of open-source model for program synthesis. Trained on TPU-v4. Competitive with OpenAI Codex.
* [hiyouga/EasyR1](https://github.com/hiyouga/EasyR1) - EasyR1: An Efficient, Scalable, Multi-Modality RL Training Framework based on veRL
* [AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) - An easy-to-use LLMs quantization package with user-friendly apis, based on GPTQ algorithm. *(archived)*
* [microsoft/poml](https://github.com/microsoft/poml) - Prompt Orchestration Markup Language
* [facebookresearch/lingua](https://github.com/facebookresearch/lingua) - Meta Lingua: a lean, efficient, and easy-to-hack codebase to research LLMs.
* [promptslab/Promptify](https://github.com/promptslab/Promptify) - Prompt Engineering | Prompt Versioning | Use GPT or other prompt based models to get structured output. Join our discord for Prompt-Engineering, LLMs and other latest research
* [turboderp-org/exllamav2](https://github.com/turboderp-org/exllamav2) - A fast inference library for running LLMs locally on modern consumer-class GPUs
* [llm-d/llm-d](https://github.com/llm-d/llm-d) - Achieve state of the art inference performance with modern accelerators on Kubernetes
* [fixie-ai/ultravox](https://github.com/fixie-ai/ultravox) - A fast multimodal LLM for real-time voice
* [microsoft/LMOps](https://github.com/microsoft/LMOps) - General technology for enabling AI capabilities w/ LLMs and MLLMs
* [mosaicml/llm-foundry](https://github.com/mosaicml/llm-foundry) - LLM training code for Databricks foundation models
* [zai-org/GLM-4.5](https://github.com/zai-org/GLM-4.5) - GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models
* [crmne/ruby_llm](https://github.com/crmne/ruby_llm) - The Ruby-native AI framework. Chats, agents, tools, images, audio, and video through one consistent API, in plain Ruby or Rails.
* [Instruction-Tuning-with-GPT-4/GPT-4-LLM](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM) - Instruction Tuning with GPT-4
* [algorithmicsuperintelligence/optillm](https://github.com/algorithmicsuperintelligence/optillm) - Optimizing inference proxy for LLMs
* [ModelTC/LightLLM](https://github.com/ModelTC/LightLLM) - LightLLM is a Python-based LLM (Large Language Model) inference and serving framework, notable for its lightweight design, easy scalability, and high-speed performance.
* [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) - AdalFlow: The library to build & auto-optimize LLM applications.
* [mshumer/gpt-llm-trainer](https://github.com/mshumer/gpt-llm-trainer)
* [OpenManus/OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) - A live stream development of RL tunning for LLM agents
* [OpenCSGs/csghub](https://github.com/OpenCSGs/csghub) - CSGHub is a brand-new open-source platform for managing LLMs, developed by the OpenCSG team. It offers both open-source and on-premise/SaaS solutions, with features comparable to Hugging Face. Gain full control over the lifecycle of LLMs, datasets, and agents, with Python SDK compatibility with Hugging Face. Join us! ⭐️
* [defog-ai/sqlcoder](https://github.com/defog-ai/sqlcoder) - SoTA LLM for converting natural language questions to SQL queries
* [QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) - Qwen3-omni is a natively end-to-end, omni-modal LLM developed by the Qwen team at Alibaba Cloud, capable of understanding text, audio, images, and video, as well as generating speech in real time.
* [predibase/lorax](https://github.com/predibase/lorax) - Multi-LoRA inference server that scales to 1000s of fine-tuned LLMs
* [SciSharp/LLamaSharp](https://github.com/SciSharp/LLamaSharp) - A C#/.NET library to run LLM (🦙LLaMA/LLaVA) on your local device efficiently.
* [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) - The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool parsers, prompt cache, reasoning separation, cloud routing. Drop-in OpenAI replacement. Works with Claude Code, Cursor, Aider.
* [PaddlePaddle/FastDeploy](https://github.com/PaddlePaddle/FastDeploy) - High-performance Inference and Deployment Toolkit for LLMs and VLMs based on PaddlePaddle
* [NExT-GPT/NExT-GPT](https://github.com/NExT-GPT/NExT-GPT) - Code and models for ICML 2024 paper, NExT-GPT: Any-to-Any Multimodal Large Language Model
* [pytorch/torchchat](https://github.com/pytorch/torchchat) - Run PyTorch LLMs locally on servers, desktop and mobile *(archived)*
* [LC1332/Luotuo-Chinese-LLM](https://github.com/LC1332/Luotuo-Chinese-LLM) - 骆驼(Luotuo): Open Sourced Chinese Language Models. Developed by 陈启源 @ 华中师范大学 & 李鲁鲁 @ 商汤科技 & 冷子昂 @ 商汤科技
* [zhaoyingjun/chatbot](https://github.com/zhaoyingjun/chatbot) - Chatbot继续沿着LLM前进，近期更新小参数量SLM的和训练脚本，支持本地训练。新增ChatAgent,实现各种有实际场景价值的Agent实现。
* [HanaokaYuzu/Gemini-API](https://github.com/HanaokaYuzu/Gemini-API) - ✨ Reverse-engineered Python API for Google Gemini web app
* [MiniMax-AI/MiniMax-01](https://github.com/MiniMax-AI/MiniMax-01) - The official repo of MiniMax-Text-01 and MiniMax-VL-01, large-language-model & vision-language-model based on Linear Attention
* [arman-bd/guppylm](https://github.com/arman-bd/guppylm) - A ~9M parameter LLM that talks like a small fish.
* [superlinked/sie](https://github.com/superlinked/sie) - Open-source inference server and production cluster for all the models your agent needs.
* [MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) - MiniMax-M1, the world's first open-weight, large-scale hybrid-attention reasoning model.
* [tekaratzas/RustGPT](https://github.com/tekaratzas/RustGPT) - An transformer based LLM. Written completely in Rust
* [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) - Switchyard lets LLM applications route traffic across models and providers while preserving native OpenAI and Anthropic API compatibility - enabling flexible model selection, benchmarking, and cost/performance optimization.
* [TanStack/ai](https://github.com/TanStack/ai) - 🤖 Type-safe, provider-agnostic TypeScript AI SDK for streaming chat, tool calling, agents, and multimodal apps across OpenAI, Anthropic, Gemini, React, Vue, Svelte, and Solid.
* [ridgerchu/matmulfreellm](https://github.com/ridgerchu/matmulfreellm) - Implementation for MatMul-free LM.
* [salesforce/CodeT5](https://github.com/salesforce/CodeT5) - Home of CodeT5: Open Code LLMs for Code Understanding and Generation *(archived)*
* [b4rtaz/distributed-llama](https://github.com/b4rtaz/distributed-llama) - Distributed LLM inference. Connect home devices into a powerful cluster to accelerate LLM inference. More devices means faster inference.
* [containers/ramalama](https://github.com/containers/ramalama) - RamaLama is an open-source developer tool that simplifies the local serving of AI models from any source and facilitates their use for inference in production, all through the familiar language of containers.
* [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) - Turn Windsurf / Devin Desktop's 100+ AI models (Claude, GPT, Gemini, DeepSeek, Kimi, GLM, SWE) into OpenAI-, Anthropic- & Gemini-compatible APIs. Zero-dependency self-hosted reverse proxy for Claude Code, Cline & Cursor. 把 Windsurf/Devin 云端 100+ 模型变成三套兼容 API。
* [thu-pacman/chitu](https://github.com/thu-pacman/chitu) - High-performance inference framework for large language models, focusing on efficiency, flexibility, and availability.
* [signerless/llm-checker](https://github.com/signerless/llm-checker) - Advanced CLI tool that scans your hardware and tells you exactly which LLM or sLLM models you can run locally, with full Ollama integration.
* [michaelfeil/infinity](https://github.com/michaelfeil/infinity) - Infinity is a high-throughput, low-latency serving engine for text-embeddings, reranking models, clip, clap and colpali
* [FreedomIntelligence/LLMZoo](https://github.com/FreedomIntelligence/LLMZoo) - ⚡LLM Zoo is a project that provides data, models, and evaluation benchmark for large language models.⚡
* [ax-llm/ax](https://github.com/ax-llm/ax) - The pretty much "official" DSPy framework for Typescript
* [zjunlp/EasyEdit](https://github.com/zjunlp/EasyEdit) - [ACL 2024] An Easy-to-use Knowledge Editing Framework for LLMs.
* [ulab-uiuc/LLMRouter](https://github.com/ulab-uiuc/LLMRouter) - LLMRouter: An Open-Source Library for LLM Routing
* [Luce-Org/lucebox](https://github.com/Luce-Org/lucebox) - LLM speculative inference server for heterogeneous hardware & consumer GPUs
* [vllm-project/vllm-ascend](https://github.com/vllm-project/vllm-ascend) - Community maintained hardware plugin for vLLM on Ascend
* [spcl/graph-of-thoughts](https://github.com/spcl/graph-of-thoughts) - Official Implementation of "Graph of Thoughts: Solving Elaborate Problems with Large Language Models"
* [OpenPipe/OpenPipe](https://github.com/OpenPipe/OpenPipe) - Turn expensive prompts into cheap fine-tuned models
* [mll-lab-nu/RAGEN](https://github.com/mll-lab-nu/RAGEN) - Agent RL framework for LLM agents: multi-turn reinforcement learning with StarPO and reasoning-collapse diagnostics
* [Alpha-VLLM/LLaMA2-Accessory](https://github.com/Alpha-VLLM/LLaMA2-Accessory) - An Open-source Toolkit for LLM Development
* [wenge-research/YAYI2](https://github.com/wenge-research/YAYI2) - YAYI 2 是中科闻歌研发的新一代开源大语言模型，采用了超过 2 万亿 Tokens 的高质量、多语言语料进行预训练。(Repo for YaYi 2 Chinese LLMs) *(archived)*
* [PhoebusSi/Alpaca-CoT](https://github.com/PhoebusSi/Alpaca-CoT) - We unified the interfaces of instruction-tuning data (e.g., CoT data), multiple LLMs and parameter-efficient methods (e.g., lora, p-tuning) together for easy use. We welcome open-source enthusiasts to initiate any meaningful PR on this repo and integrate as many LLM related technologies as possible. 我们打造了方便研究人员上手和使用大模型等微调平台，我们欢迎开源爱好者发起任何有意义的pr！
* [FasterDecoding/Medusa](https://github.com/FasterDecoding/Medusa) - Medusa: Simple Framework for Accelerating LLM Generation with Multiple Decoding Heads
* [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) - Find, benchmark and install in CLI 170+ FREE coding LLM models across 15+ providers in real time
* [OpenDCAI/DataFlex](https://github.com/OpenDCAI/DataFlex) - Data-centric LLM training with dynamic sample selection, domain mixture optimization, and example reweighting inside the LLaMA-Factory training loop.
* [ZHZisZZ/dllm](https://github.com/ZHZisZZ/dllm) - dLLM: Simple Diffusion Language Modeling
* [JIA-Lab-research/LongLoRA](https://github.com/JIA-Lab-research/LongLoRA) - Code and documents of LongLoRA and LongAlpaca (ICLR 2024 Oral)
* [stochasticai/xTuring](https://github.com/stochasticai/xTuring) - Build, personalize and control your own LLMs. From data pre-processing to fine-tuning, xTuring provides an easy way to personalize open-source LLMs. Join our discord community: https://discord.gg/TgHXuSJEk6
* [bestruirui/octopus](https://github.com/bestruirui/octopus) - One Hub All LLMs For You | 为个人打造的 LLM API 聚合网关
* [MiniMax-AI/MiniMax-M2](https://github.com/MiniMax-AI/MiniMax-M2) - MiniMax-M2, a model built for Max coding & agentic workflows.
* [wenge-research/YAYI](https://github.com/wenge-research/YAYI) - 雅意大模型：为客户打造安全可靠的专属大模型，基于大规模中英文多领域指令数据训练的 LlaMA 2 & BLOOM 系列模型，由中科闻歌算法团队研发。(Repo for YaYi Chinese LLMs based on LlaMA2 & BLOOM) *(archived)*
* [young-geng/EasyLM](https://github.com/young-geng/EasyLM) - Large language models (LLMs) made easy, EasyLM is a one stop solution for pre-training, finetuning, evaluating and serving LLMs in JAX/Flax.
* [xusenlinzy/api-for-open-llm](https://github.com/xusenlinzy/api-for-open-llm) - Openai style api for open large language models, using LLMs just as chatgpt! Support for LLaMA, LLaMA-2, BLOOM, Falcon, Baichuan, Qwen, Xverse, SqlCoder, CodeLLaMA, ChatGLM, ChatGLM2, ChatGLM3 etc. 开源大模型的统一后端接口
* [google/tunix](https://github.com/google/tunix) - A Lightweight LLM Post-Training Library
* [jackmpcollins/magentic](https://github.com/jackmpcollins/magentic) - Seamlessly integrate LLMs as Python functions
* [prism-php/prism](https://github.com/prism-php/prism) - A unified interface for working with LLMs in Laravel
* [AI-Hypercomputer/maxtext](https://github.com/AI-Hypercomputer/maxtext) - A simple, performant, and scalable Jax LLM!
* [Jittor/JittorLLMs](https://github.com/Jittor/JittorLLMs) - 计图大模型推理库，具有高性能、配置要求低、中文支持好、可移植等特点
* [dvmazur/mixtral-offloading](https://github.com/dvmazur/mixtral-offloading) - Run Mixtral-8x7B models in Colab or consumer desktops

### Machine Learning Frameworks

* [huggingface/transformers](https://github.com/huggingface/transformers) - 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
* [karpathy/llm.c](https://github.com/karpathy/llm.c) - LLM training in simple, raw C/CUDA
* [microsoft/unilm](https://github.com/microsoft/unilm) - Large-scale Self-supervised Pre-training Across Tasks, Languages, and Modalities
* [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) - The absolute trainer to light up AI agents.
* [alibaba/MNN](https://github.com/alibaba/MNN) - MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs and Edge AI.
* [ludwig-ai/ludwig](https://github.com/ludwig-ai/ludwig) - Low-code framework for building custom LLMs, neural networks, and other AI models
* [gorse-io/gorse](https://github.com/gorse-io/gorse) - AI powered open source recommender system engine supports classical/LLM rankers and multimodal content via embedding
* [nebuly-ai/optimate](https://github.com/nebuly-ai/optimate) - A collection of libraries to optimise AI model performances
* [haifengl/smile](https://github.com/haifengl/smile) - Statistical Machine Intelligence & Learning Engine
* [amazon-science/chronos-forecasting](https://github.com/amazon-science/chronos-forecasting) - Chronos: Pretrained Models for Time Series Forecasting
* [higgsfield-ai/higgsfield](https://github.com/higgsfield-ai/higgsfield) - Fault-tolerant, highly scalable GPU orchestration, and a machine learning framework designed for training models with billions to trillions of parameters
* [SwanHubX/SwanLab](https://github.com/SwanHubX/SwanLab) - ⚡️SwanLab - an open-source, modern-design AI training tracking and visualization tool. Supports Cloud / Self-hosted use. Integrated with PyTorch / Transformers / verl / LLaMA Factory / ms-swift / Ultralytics / MMEngine / Keras etc.
* [Nixtla/nixtla](https://github.com/Nixtla/nixtla) - TimeGPT-2.1: production ready pre-trained Time Series Foundation Model for forecasting and anomaly detection. Generative pretrained transformer for time series trained on over 100B data points. It's capable of accurately predicting various domains such as retail, electricity, finance, and IoT with just a few lines of code 🚀.
* [fnnx-ai/scikit-llm](https://github.com/fnnx-ai/scikit-llm) - Seamlessly integrate LLMs into scikit-learn.
* [towhee-io/towhee](https://github.com/towhee-io/towhee) - Towhee is a framework that is dedicated to making neural data processing pipelines simple and fast.
* [alpa-projects/alpa](https://github.com/alpa-projects/alpa) - Training and serving large-scale neural networks with auto parallelization. *(archived)*
* [microsoft/torchscale](https://github.com/microsoft/torchscale) - Foundation Architecture for (M)LLMs
* [KimMeen/Time-LLM](https://github.com/KimMeen/Time-LLM) - [ICLR 2024] Official implementation of " 🦙 Time-LLM: Time Series Forecasting by Reprogramming Large Language Models"
* [ailia-ai/ailia-models](https://github.com/ailia-ai/ailia-models) - The collection of pre-trained, state-of-the-art AI models for ailia SDK

### Computer Vision

* [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.
* [opendatalab/MinerU](https://github.com/opendatalab/MinerU) - Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.
* [allenai/olmocr](https://github.com/allenai/olmocr) - Toolkit for linearizing PDFs for LLM datasets/training
* [zai-org/CogVideo](https://github.com/zai-org/CogVideo) - text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023)
* [OpenGVLab/InternVL](https://github.com/OpenGVLab/InternVL) - [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-4o. 接近GPT-4o表现的开源多模态对话模型
* [om-ai-lab/VLM-R1](https://github.com/om-ai-lab/VLM-R1) - Solve Visual Understanding with Reinforced VLMs
* [joanrod/star-vector](https://github.com/joanrod/star-vector) - StarVector is a foundation model for SVG generation that transforms vectorization into a code generation task. Using a vision-language modeling architecture, StarVector processes both visual and textual inputs to produce high-quality SVG code with remarkable precision.
* [lumina-ai-inc/chunkr](https://github.com/lumina-ai-inc/chunkr) - Vision infrastructure to turn complex documents into RAG/LLM-ready data
* [NVlabs/Eagle](https://github.com/NVlabs/Eagle) - Eagle: Frontier Vision-Language Models with Data-Centric Strategies
* [OpenGVLab/InternGPT](https://github.com/OpenGVLab/InternGPT) - InternGPT (iGPT) is an open source demo platform where you can easily showcase your AI models. Now it supports DragGAN, ChatGPT, ImageBind, multimodal chat like GPT-4, SAM, interactive image editing, etc. Try it at igpt.opengvlab.com (支持DragGAN、ChatGPT、ImageBind、SAM的在线Demo系统)
* [CatchTheTornado/text-extract-api](https://github.com/CatchTheTornado/text-extract-api) - Document (PDF, Word, PPTX ...) extraction and parse API using state of the art modern OCRs + Ollama supported models. Anonymize documents. Remove PII. Convert any document or picture to structured JSON or Markdown
* [SkyworkAI/Skywork-R1V](https://github.com/SkyworkAI/Skywork-R1V) - Skywork-R1V is an advanced multimodal AI model series developed by Skywork AI, specializing in vision-language reasoning.
* [Filimoa/open-parse](https://github.com/Filimoa/open-parse) - Improved file parsing for LLM’s
* [SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera) - Open-Source AI Camera Skills Platform, AI NVR & CCTV Surveillance. Local VLM video analysis with Qwen, DeepSeek, SmolVLM, LLaVA, YOLO26. LLM-powered agentic security camera agent — watches, understands, remembers & guards your home via Telegram, Discord or Slack. Pluggable AI skills. OpenAI, Google, Anthropic or local AI. Runs on Mac Mini & AI PC.
* [Dicklesworthstone/llm_aided_ocr](https://github.com/Dicklesworthstone/llm_aided_ocr) - Enhances Tesseract OCR output using LLMs (local or API) for error correction, smart chunking, and markdown formatting of scanned PDFs
* [sherlockchou86/VideoPipe](https://github.com/sherlockchou86/VideoPipe) - A cross-platform video structuring (video analysis) framework based on CV models & mLLM.
* [InternLM/InternLM-XComposer](https://github.com/InternLM/InternLM-XComposer) - InternLM-XComposer2.5-OmniLive: A Comprehensive Multimodal System for Long-term Streaming Video and Audio Interactions
* [JIA-Lab-research/LISA](https://github.com/JIA-Lab-research/LISA) - Project Page for "LISA: Reasoning Segmentation via Large Language Model"

### Natural Language Processing

* [2noise/ChatTTS](https://github.com/2noise/ChatTTS) - A generative speech model for daily dialogue.
* [google/langextract](https://github.com/google/langextract) - A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization.
* [PaddlePaddle/PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) - Easy-to-use and powerful LLM and SLM library with awesome model zoo.
* [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) - Retrieval and Retrieval-augmented LLMs
* [karpathy/minbpe](https://github.com/karpathy/minbpe) - Minimal, clean code for the Byte Pair Encoding (BPE) algorithm commonly used in LLM tokenization.
* [fishaudio/Bert-VITS2](https://github.com/fishaudio/Bert-VITS2) - vits2 backbone with multilingual-bert
* [canopyai/Orpheus-TTS](https://github.com/canopyai/Orpheus-TTS) - Towards Human-Sounding Speech
* [huggingface/text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference) - A blazing fast inference solution for text embeddings models
* [SakuraLLM/SakuraLLM](https://github.com/SakuraLLM/SakuraLLM) - 适配轻小说/Galgame的日中翻译大模型
* [JohnSnowLabs/spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) - State of the Art Natural Language Processing
* [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - An open-source model family for long-form speech, dialogue synthesis, voice design, sound effects, and real-time streaming TTS
* [marcelroed/gigatoken](https://github.com/marcelroed/gigatoken) - Language model tokenization at GB/s
* [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) - Hypergraph is more powerful. Transform unstructured text into structured knowledge with LLMs. Graphs, hypergraphs, and spatio-temporal extractions — with one command.
* [dongrixinyu/JioNLP](https://github.com/dongrixinyu/JioNLP) - 中文 NLP 预处理、解析工具包，准确、高效、易用 A Chinese NLP Preprocessing & Parsing Package www.jionlp.com
* [robert-mcdermott/ai-knowledge-graph](https://github.com/robert-mcdermott/ai-knowledge-graph) - AI Powered Knowledge Graph Generator
* [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) - Translate full-length books and documents with Ollama, OpenAI-compatible, Gemini, Mistral, DeepSeek, Poe or OpenRouter. Preserves formatting. Resumes where you left off. No file size limits.

### Data Science and Analytics

* [pathwaycom/pathway](https://github.com/pathwaycom/pathway) - Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.
* [vanna-ai/vanna](https://github.com/vanna-ai/vanna) - 🤖 Chat with your SQL database 📊. Accurate Text-to-SQL Generation via LLMs using Agentic Retrieval 🔄. *(archived)*
* [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) - Chat with your database or your datalake (SQL, CSV, parquet). PandasAI makes data analysis conversational using LLMs and RAG.
* [huggingface/datasets](https://github.com/huggingface/datasets) - 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
* [eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT) - open-source agentic AI data assistant for the next generation of AI + Data products.
* [Canner/WrenAI](https://github.com/Canner/WrenAI) - GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data sources, such as BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks and more.
* [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) - Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models. Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding.
* [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) - A powerful tool for creating datasets for LLM fine-tuning 、RAG and Eval
* [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) - Incremental engine for long horizon agents 🌟 Star if you like it!
* [Netflix/metaflow](https://github.com/Netflix/metaflow) - Build, Manage and Deploy AI/ML Systems
* [apache/seatunnel](https://github.com/apache/seatunnel) - SeaTunnel is a multimodal, high-performance, distributed, massive data integration tool.
* [OpenDCAI/DataFlow](https://github.com/OpenDCAI/DataFlow) - [SIGMOD'27] Easy Data Preparation with latest LLMs-based Operators and Pipelines.
* [flyteorg/flyte](https://github.com/flyteorg/flyte) - Dynamic, resilient AI orchestration. Coordinate data, models, and compute as you build AI workflows.
* [Zipstack/unstract](https://github.com/Zipstack/unstract) - LLM-Driven Extraction of Unstructured Data — Built for API Deployments & ETL Pipeline Workflows
* [datajuicer/data-juicer](https://github.com/datajuicer/data-juicer) - Data processing for and with foundation models! 🍎 🍋 🌽 ➡️ ➡️🍸 🍹 🍷
* [dataease/SQLBot](https://github.com/dataease/SQLBot) - 🔥 基于大模型和 RAG 的智能问数系统，对话式数据分析神器。Text-to-SQL Generation via LLMs using RAG.
* [zenml-io/zenml](https://github.com/zenml-io/zenml) - ZenML 🙏: One AI Platform from Pipelines to Agents. https://zenml.io.
* [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) - My Python scripts to make high-quality figures for publications in top AI conferences and journals.
* [katanaml/sparrow](https://github.com/katanaml/sparrow) - Structured data extraction, instruction calling and agentic workflows with ML, LLM and Vision LLM
* [argilla-io/argilla](https://github.com/argilla-io/argilla) - Argilla is a collaboration tool for AI engineers and domain experts to build high-quality datasets
* [tencentmusic/supersonic](https://github.com/tencentmusic/supersonic) - SuperSonic is the next-generation AI+BI platform that unifies Chat BI (powered by LLM) and Headless BI (powered by semantic layer) paradigms.
* [ruc-datalab/DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) - DeepAnalyze is the first agentic LLM for autonomous data science. 🎈你的AI数据分析师，自动分析大量数据，一键生成专业分析报告！
* [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) - 🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis.
* [StructuredLabs/preswald](https://github.com/StructuredLabs/preswald) - Preswald is a WASM packager for Python-based interactive data apps: bundle full complex data workflows, particularly visualizations, into single files, runnable completely in-browser, using Pyodide, DuckDB, Pandas, and Plotly, Matplotlib, etc. Build dashboards, reports, and notebooks that run offline, load fast, and share like a document.
* [ucbepic/docetl](https://github.com/ucbepic/docetl) - A system for agentic LLM-powered data processing and ETL
* [microsoft/lida](https://github.com/microsoft/lida) - Automatic Generation of Visualizations and Infographics using Large Language Models
* [Zafer-Liu/Data-Analysis-Agent](https://github.com/Zafer-Liu/Data-Analysis-Agent) - 🚀你的私人数据分析助手。通过对话式交互，自动生成可视化报表与商业洞察，让数据决策变得像聊天一样简单。 🚀 Your personal data analysis assistant. Say goodbye to complex SQL and Excel formulas. An LLM-powered data analysis agent. Chat with your data to instantly generate visualizations and business insights. Making data-driven decisions has never been easier.
* [pingcap/ossinsight](https://github.com/pingcap/ossinsight) - Analysis, Comparison, Trends, Rankings of Open Source Software, you can also get insight from more than 10 billion with natural language (powered by LLM). Follow us on Twitter: https://twitter.com/ossinsight
* [hitsz-ids/synthetic-data-generator](https://github.com/hitsz-ids/synthetic-data-generator) - SDG is a specialized framework designed to generate high-quality structured tabular data.
* [DeepInsight-AI/DeepBI](https://github.com/DeepInsight-AI/DeepBI) - LLM based data scientist, AI native data application. AI-driven infinite thinking redefines BI.
* [refuel-ai/autolabel](https://github.com/refuel-ai/autolabel) - Label, clean and enrich text datasets with LLMs.

## AI Agents

### Agent Frameworks and Runtimes

* [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) - The agent that grows with you
* [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.
* [langgenius/dify](https://github.com/langgenius/dify) - Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
* [langchain-ai/langchain](https://github.com/langchain-ai/langchain) - The agent engineering platform.
* [earendil-works/pi](https://github.com/earendil-works/pi) - AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
* [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) - 🙌 OpenHands: AI-Driven Development
* [bytedance/deer-flow](https://github.com/bytedance/deer-flow) - An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
* [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) - 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming
* [aaif-goose/goose](https://github.com/aaif-goose/goose) - an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM
* [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) - Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-agent, multi-model, multi-channel. Lightweight, extensible, one-line install. (formerly chatgpt-on-wechat)
* [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) - Build resilient agents.
* [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) - AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨
* [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) - OpenHuman is an open source agent harness with local-first memory, agent orchestration, and workflows
* [reworkd/AgentGPT](https://github.com/reworkd/AgentGPT) - 🤖 Assemble, configure, and deploy autonomous AI Agents in your browser. *(archived)*
* [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) - DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.
* [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) - ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration
* [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) - Build and run agents you can see, understand and trust.
* [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) - ⌥ Coding agent with the IDE wired in
* [stanford-oval/storm](https://github.com/stanford-oval/storm) - An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations.
* [labring/FastGPT](https://github.com/labring/FastGPT) - FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.
* [openai/openai-agents-python](https://github.com/openai/openai-agents-python) - A lightweight, powerful framework for multi-agent workflows
* [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) - An autonomous agent that conducts deep research on any data using any LLM providers
* [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) - Integrate cutting-edge LLM technology quickly and easily into your apps
* [mastra-ai/mastra](https://github.com/mastra-ai/mastra) - Mastra is the modern TypeScript framework for AI-powered applications and agents.
* [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) - An open-source AI coding agent that lives in your terminal.
* [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) - Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity.
* [vercel/ai](https://github.com/vercel/ai) - The AI Toolkit for TypeScript. From 