# awesome-ChatGPT-repositories

<p align="center">
  <img src="assets/logo.png" alt="awesome-ChatGPT-repositories" width="640">
</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-ChatGPT-repositories-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-ChatGPT-repositories/pulls)

A curated list of resources dedicated to open source GitHub repositories related to [ChatGPT](https://openai.com/blog/chatgpt).
A tool for searching these repositories is [available](https://huggingface.co/spaces/taishi-i/awesome-ChatGPT-repositories-search) on Hugging Face Spaces.

Your contributions are always welcome! Before contributing, please read [the guidelines](https://github.com/taishi-i/awesome-ChatGPT-repositories/blob/main/contributing.md).

## Claude Code & Codex Skill

Search 2,500+ curated repositories directly from Claude Code or Codex — no browser needed, just describe what you're looking for. Both tools use the same skill and the same bundled data.

- **Find tools by topic** — RAG frameworks, agent libraries, chatbot UIs, CLI tools, and more
- **Filter by category or language** — narrow results to a specific category (e.g. `CLIs`, `NLP`) or programming language
- **Multilingual queries** — search in Japanese, Chinese, Korean, or any language
- **Scored results** — ranked by relevance, star count, and project quality

### Claude Code

Run these commands inside Claude Code:

```
/plugin marketplace add taishi-i/awesome-ChatGPT-repositories
/plugin install awesome-chatgpt-search@awesome-chatgpt-repositories
/reload-plugins
```

Usage:

```
/awesome-chatgpt-search:search RAG retrieval
/awesome-chatgpt-search:search category:CLIs agent
/awesome-chatgpt-search:search language:Python langchain
/awesome-chatgpt-search:search fine-tuning lora peft
/awesome-chatgpt-search:search list categories
```

### Codex

Run these commands in your terminal, then start a new Codex session:

```
codex plugin marketplace add taishi-i/awesome-ChatGPT-repositories
codex plugin add awesome-chatgpt-search@awesome-chatgpt-repositories
```

Usage — mention the skill with `$` (Codex can also pick it up on its own when you ask for repositories):

```
$awesome-chatgpt-search:search RAG retrieval
$awesome-chatgpt-search:search category:CLIs agent
$awesome-chatgpt-search:search language:Python langchain
$awesome-chatgpt-search:search fine-tuning lora peft
$awesome-chatgpt-search:search list categories
```

### Other agents (npx skills)

Run this command in your terminal. It works with Cursor, Gemini CLI, GitHub Copilot, and [other agents supported by the skills CLI](https://github.com/vercel-labs/skills#supported-agents), as well as Claude Code and Codex:

```
npx skills add taishi-i/awesome-ChatGPT-repositories
```

Usage (in Codex, use `$awesome-chatgpt-search` instead):

```
/awesome-chatgpt-search RAG retrieval
/awesome-chatgpt-search category:CLIs agent
/awesome-chatgpt-search list categories
```

To update, run `npx skills update awesome-chatgpt-search`. You don't need this if you have already installed the plugin.


[English](https://github.com/taishi-i/awesome-ChatGPT-repositories/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-ChatGPT-repositories/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-ChatGPT-repositories/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-ChatGPT-repositories/blob/main/docs/README.zh-hans.md)


## The latest additions 🎉

**Browser-extensions**
 * [quivr](https://github.com/the-vibe-company/quivr) - An open-source engine that turns continuous content streams into search and monitoring. Durable ingestion, hybrid search, alerts, and plugins for formats, models and business rules.


**CLIs**
 * [rea](https://github.com/morluto/rea) - Reverse engineer anything with agents, from app behavior down to native binaries.


**Langchain**
 * [LibreChat](https://github.com/librechat-ai/librechat) - Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active


**Others**
 * [loopx](https://github.com/loopx-project/loopx) - A control plane with a durable state kernel for long-horizon agents and teams. Keep work moving and improving across sessions, with less human attention.
 * [letta-code](https://github.com/letta-ai/letta-code) - Stateful agents that are like people, with memory, identity, and the ability to learn and adapt


_Updated on October 09, 2026_ (A total of 2724 repositories listed.)

## Table of contents

 * [Awesome-lists](#awesome-lists)
 * [Prompts](#prompts)
 * [Chatbots](#chatbots)
 * [Browser-extensions](#browser-extensions)
 * [CLIs](#clis)
 * [Reimplementations](#reimplementations)
 * [Tutorials](#tutorials)
 * [NLP](#nlp)
 * [Langchain](#langchain)
 * [Unity](#unity)
 * [Openai](#openai)
 * [Others](#others)

## Awesome-lists

 * [awesome-chatgpt-api](https://github.com/reorx/awesome-chatgpt-api) - Curated list of apps and tools that not only use the new ChatGPT API, but also allow users to configure their own API keys, enabling free and on-demand usage of their own quota.
 * [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) - This repo includes ChatGPT prompt curation to use ChatGPT better.
 * [awesome-chatgpt](https://github.com/humanloop/awesome-chatgpt) - Curated list of awesome tools, demos, docs for ChatGPT and GPT-3
 * [awesome-totally-open-chatgpt](https://github.com/nichtdax/awesome-totally-open-chatgpt) - A list of totally open alternatives to ChatGPT
 * [awesome-chatgpt-prompts-zh](https://github.com/plexpt/awesome-chatgpt-prompts-zh) - ChatGPT 中文调教指南。各种场景使用指南。学习怎么让它听你的话。
 * [Awesome-ChatGPT](https://github.com/dalinvip/awesome-chatgpt) - ChatGPT资料汇总学习，持续更新......
 * [awesome-compbio-chatgpt](https://github.com/csbl-br/awesome-compbio-chatgpt) - An awesome repository of community-curated applications of ChatGPT and other LLMs im computational biology
 * [awesome-chatgpt](https://github.com/openmindclub/awesome-chatgpt) - ⚡ Everything about ChatGPT
 * [awesome-chatgpt](https://github.com/saharmor/awesome-chatgpt) - Selected ChatGPT demos, tools, articles, and more ✨
 * [awesome-chatgpt-zh](https://github.com/yzfly/awesome-chatgpt-zh) - ChatGPT 中文指南，ChatGPT 中文调教指南，指令指南，精选资源清单，更好的使用 chatGPT 让你的生产力 up up up!
 * [awesome-chatgpt](https://github.com/eon01/awesome-chatgpt) - 🧠 A curated list of awesome ChatGPT resources, including libraries, SDKs, APIs, and more. 🌟 Please consider supporting this project by giving it a star.
 * [awesome-gpt4](https://github.com/taranjeet/awesome-gpt4) - Curated list of awesome resources, use cases and demos for GPT-4
 * [awesome-gpt-security](https://github.com/cckuailong/awesome-gpt-security) - A curated list of awesome security tools, experimental case or other interesting things with LLM or GPT.
 * [Awesome-GPT4-Prompts](https://github.com/ora-sh/awesome-gpt4-prompts) - A collection of awesome GPT4 prompts
 * [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) - 🤖 Awesome list for ChatGPT — an artificial intelligence chatbot developed by OpenAI
 * [awesome-free-chatgpt](https://github.com/lilittlecat/awesome-free-chatgpt) - 🆓免费的 ChatGPT 镜像网站列表，持续更新。List of free ChatGPT mirror sites, continuously updated.
 * [awesome-gpt-prompt-engineering](https://github.com/snwfdhmp/awesome-gpt-prompt-engineering) - A curated list of awesome resources, tools, and other shiny things for GPT prompt engineering.
 * [awesome-chatgpt-prompts-cybersecurity](https://github.com/sechelper/awesome-chatgpt-prompts-cybersecurity) - 网络安全chatgpt指令集，训练chatgpt成为一名网络安全专家
 * [awesome-ai](https://github.com/lencx/awesome-ai) - 🤖 Awesome AI
 * [awesome-chatgpt-code-interpreter-experiments](https://github.com/skalskip/awesome-chatgpt-code-interpreter-experiments) - Awesome things you can do with ChatGPT + Code Interpreter combo 🔥
 * [awesome-ai](https://github.com/520hacker/awesome-ai) - 对开源AI转发套壳应用生态进行研究，收集开源AI转发套壳应用，并进行对比。 ChatGPT,OPENAI.AZURE,BAIDU,XUNFEI
 * [Awesome-ChatGPT-AI-ZH](https://github.com/changeyu0229/awesome-chatgpt-ai-zh) - 全网曝光超1000万的「AI 知识库」正式移步Github开源，永久免费更新，提供ChatGPT，Midjourney等使用教程
 * [Awesome-LLM-Eval](https://github.com/onejune2018/awesome-llm-eval) - Awesome-LLM-Eval: a curated list of tools, demos, papers, docs for Evaluation on Large Language Models like ChatGPT, LLaMA, GLM
 * [awesome-chatgpt-dataset](https://github.com/voidful/awesome-chatgpt-dataset) - Unlock the Power of LLM: Explore These Datasets to Train Your Own ChatGPT!
 * [awesome-gpt](https://github.com/formulahendry/awesome-gpt) - A curated list of awesome projects and resources related to GPT, ChatGPT, OpenAI, LLM, and more.
 * [awesome-instruction-dataset](https://github.com/yaodongc/awesome-instruction-dataset) - A collection of open-source dataset to train instruction-following LLMs (ChatGPT,LLaMA,Alpaca)
 * [awesome-chatgpt](https://github.com/uhub/awesome-chatgpt) - A curated list of awesome ChatGPT related projects.
 * [Awesome-Prompt-Engineering](https://github.com/promptslab/awesome-prompt-engineering) - This repository contains a hand-curated resources for Prompt Engineering with a focus on Generative Pre-trained Transformer (GPT), ChatGPT, PaLM etc
 * [awesome-generative-ai](https://github.com/filipecalegario/awesome-generative-ai) - A curated list of Generative AI tools, works, models, and references
 * [awesome-open-gpt](https://github.com/ewingyangs/awesome-open-gpt) - Collection of Open Source Projects Related to GPT，GPT相关开源项目合集🚀、精选🔥🔥
 * [Awesome-AITools](https://github.com/ikaijua/awesome-aitools) - Collection of AI-related utilities. Welcome to submit issues and pull requests /收藏AI相关的实用工具，欢迎提交issues 或者pull requests
 * [Awesome-GPTs](https://github.com/ai-boost/awesome-gpts) - Curated list of awesome GPTs 👍.
 * [awesome-segment-anything](https://github.com/hedlen/awesome-segment-anything) - Tracking and collecting papers/projects/others related to Segment Anything.
 * [Awesome-AIGC-Tutorials](https://github.com/luban-agi/awesome-aigc-tutorials) - Curated tutorials and resources for Large Language Models, AI Painting, and more.
 * [awesome-gpts](https://github.com/taranjeet/awesome-gpts) - Collection of all the GPTs created by the community
 * [prompt-in-context-learning](https://github.com/egoalpha/prompt-in-context-learning) - Awesome resources for in-context learning and prompt engineering: Mastery of the LLMs such as ChatGPT, GPT-3, and FlanT5, with up-to-date and cutting-edge updates.
 * [Awesome-GPT-Store](https://github.com/anil-matcha/awesome-gpt-store) - Custom GPT Store - A collection of major GPTS available in public
 * [awesome-chatgpt](https://github.com/awesome-chatgpt/awesome-chatgpt) - 🏆 An awesome list of best resources, tools, applications, usages of ChatGPT
 * [BlackFriday-GPTs-Prompts](https://github.com/friuns2/blackfriday-gpts-prompts) - List of free GPTs that doesn't require plus subscription
 * [best-of-ml-python](https://github.com/ml-tooling/best-of-ml-python) - 🏆 A ranked list of awesome machine learning Python libraries. Updated weekly.
 * [awesome-openai-vision-api-experiments](https://github.com/roboflow/awesome-openai-vision-api-experiments) - Must-have resource for anyone who wants to experiment with and build on the OpenAI vision API 🔥
 * [Awesome-LLM-KG](https://github.com/rmanluo/awesome-llm-kg) - Awesome papers about unifying LLMs and KGs
 * [Awesome-AI-GPTs](https://github.com/embraceagi/awesome-ai-gpts) - Awesome AI GPTs, OpenAI GPTs, GPT-4, ChatGPT, GPTs, Prompts, plugins, Prompts leaking
 * [Awesome-GPT-Agents](https://github.com/fr0gger/awesome-gpt-agents) - A curated list of GPT agents for cybersecurity
 * [Awesome-One-Click-Deployment](https://github.com/connectai-e/awesome-one-click-deployment) - 🪄 One-click deployment of many github open source projects to facilitate fast experience 一键部署各种Github开源AI项目
 * [LLM-Reasoning-Papers](https://github.com/atfortes/llm-reasoning-papers) - Collection of papers and resources on Reasoning in Large Language Models (LLMs), including Chain-of-Thought (CoT), Instruction-Tuning, and others.
 * [awesome-chatgpt-store](https://github.com/devisasari/awesome-chatgpt-store) - A curated list of awesome custom GPTs
 * [Leaked-GPTs](https://github.com/friuns2/leaked-gpts) - Leaked GPTs Prompts Bypass the 25 message limit or to try out GPTs without a Plus subscription.
 * [awesome-chatgpt-project](https://github.com/xianyu110/awesome-chatgpt-project) - 1.chatGPT注册  2.chatGPT成品项目整理  3.高效使用chatGPT的小技巧  4.调教指南 ↓演示网站
 * [awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) - ...
 * [awesome-gpt-store](https://github.com/devisasari/awesome-gpt-store) - A curated list of awesome GPTs in the GPT Store
 * [AiTreasureBox](https://github.com/superiorlu/aitreasurebox) - 🤖 Collect practical AI repos, tools, websites, papers and tutorials on AI. 实用的AI百宝箱 💎
 * [Awesome-LLM-Reasoning](https://github.com/atfortes/awesome-llm-reasoning) - Collection of papers and resources on Reasoning in Language Models (LLMs), including Chain-of-Thought (CoT), Instruction-Tuning, and Multimodality.
 * [awesome-llm-and-aigc](https://github.com/codingonion/awesome-llm-and-aigc) - 🚀🚀🚀A collection of some awesome public projects about Large Language Model, Vision Foundation Model and AI Generated Content.
 * [awesome-gpts-prompts](https://github.com/ai-boost/awesome-gpts-prompts) - Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store.
 * [Awesome-LLM-Uncertainty-Reliability-Robustness](https://github.com/jxzhangjhu/awesome-llm-uncertainty-reliability-robustness) - Awesome-LLM-Robustness: a curated list of Uncertainty, Reliability and Robustness in Large Language Models
 * [awesome-prompts](https://github.com/ai-boost/awesome-prompts) - Curated list of chatgpt prompts from the top-rated GPTs in the GPTs Store. Prompt Engineering, prompt attack & prompt protect. Advanced Prompt Engineering papers.
 * [awesome-decentralized-llm](https://github.com/imaurer/awesome-decentralized-llm) - Collection of LLM resources that can be used to build products you can "own" or to perform reproducible research.
 * [awesome-gpt4](https://github.com/radi-cho/awesome-gpt4) - A curated list of prompts, tools, and resources regarding the GPT-4 language model.
 * [awesome-transformer-nlp](https://github.com/cedrickchee/awesome-transformer-nlp) - A curated list of NLP resources focused on Transformer networks, attention mechanism, GPT, BERT, ChatGPT, LLMs, and transfer learning.
 * [awesome-claude-prompts](https://github.com/langgptai/awesome-claude-prompts) - This repo includes Claude prompt curation to use Claude better.
 * [awesome-ai-sdks](https://github.com/e2b-dev/awesome-ai-sdks) - A database of SDKs, frameworks, libraries, and tools for creating, monitoring, debugging and deploying autonomous AI agents
 * [awesome-claude-prompts](https://github.com/yzfly/awesome-claude-prompts) - Gitalk Comments
 * [chatgpt-corpus](https://github.com/plexpt/chatgpt-corpus) - ChatGPT 中文语料库 对话语料 小说语料 客服语料 用于训练大模型
 * [awesome-gpt](https://github.com/awesome-gptx/awesome-gpt) - 🏆 An awe-inspiring collection of resources, encompassing a wide range of tools, documents, resources, applications, and use cases related to ChatGPT.
 * [lobe-chat-agents](https://github.com/lobehub/lobe-chat-agents) - 🏪 Agent Index - This is the agent index for LobeChat. It accesses index.json from this repository to display a list of available agents for LobeChat to the agent market.
 * [awesome-python](https://github.com/dylanhogg/awesome-python) - 🐍 Hand-picked awesome Python libraries and frameworks, organised by category
 * [awesome-llm-role-playing-with-persona](https://github.com/neph0s/awesome-llm-role-playing-with-persona) - Awesome-llm-role-playing-with-persona: a curated list of resources for large language models for role-playing with assigned personas
 * [awesome-chatgpt-zh](https://github.com/embraceagi/awesome-chatgpt-zh) - ChatGPT 中文指南🔥，ChatGPT 中文调教指南，指令指南，应用开发指南，精选资源清单，更好的使用 chatGPT 让你的生产力 up up up! 🚀
 * [Awesome-Machine-Generated-Text](https://github.com/ictmcg/awesome-machine-generated-text) - Continuously updated list of related resources for generative LLMs like GPT and their analysis and detection.
 * [Awesome_GPT_Super_Prompting](https://github.com/cyberalbsecop/awesome_gpt_super_prompting) - ChatGPT Jailbreaks, GPT Assistants Prompt Leaks, GPTs Prompt Injection, LLM Prompt Security, Super Prompts, Prompt Hack, Prompt Security, Ai Prompt Engineering, Adversarial Machine Learning.
 * [lobe-chat-plugins](https://github.com/lobehub/lobe-chat-plugins) - 🏪  Plugin Index - This is the plugin index for LobeChat. It accesses index.json from this repository to display a list of available plugins for LobeChat to the user.
 * [Awesome-LLM-Strawberry](https://github.com/hijkzzz/awesome-llm-strawberry) - A collection of LLM papers, blogs, and projects, with a focus on OpenAI o1 and reasoning techniques.
 * [awesome-llm-apps](https://github.com/shubhamsaboo/awesome-llm-apps) - Collection of awesome LLM apps with RAG using OpenAI, Anthropic, Gemini and opensource models.
 * [awesome-LLM-resourses](https://github.com/wangrongsheng/awesome-llm-resourses) - 🧑‍🚀 全世界最好的LLM资料总结 | Summary of the world's best LLM resources.
 * [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - A list of AI autonomous agents
 * [Awesome-One-Click-Deployment](https://github.com/elricliu/awesome-one-click-deployment) - 🪄 One-click deployment of many github open source projects to facilitate fast experience 一键部署各种Github开源AI项目
 * [awesome-llm-and-aigc](https://github.com/coderonion/awesome-llm-and-aigc) - 🚀🚀🚀A collection of some wesome public projects about Large Language Model(LLM), Vision Language Model(VLM), Vision Language Action(VLA), AI Generated Content(AIGC), the related Datasets and Applications.
 * [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) - 🧠 Curated collection of system prompts for top AI tools. Perfect for AI agent builders and prompt engineers. Incuding: ChatGPT, Claude, Perplexity, Manus, Claude-Code, Loveable, v0, Grok, same new, windsurf, notion, and MetaAI.
 * [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) - Awesome curated collection of GPT-4o images & prompts. Explore diverse AI-generated art styles (Ghibli, 3D, etc.) from OpenAI's latest model.
 * [awesome-whisper](https://github.com/sindresorhus/awesome-whisper) - 🔊 Awesome list for Whisper — an open-source AI-powered speech recognition system developed by OpenAI
 * [awesome-LLM-resources](https://github.com/wangrongsheng/awesome-llm-resources) - 🧑‍🚀 全世界最好的LLM资料总结（Agent框架、辅助编程、数据处理、模型训练、模型推理、o1 模型、MCP、小语言模型、视觉语言模型） | Summary of the world's best LLM resources.
 * [awesome-userscripts](https://github.com/awesome-scripts/awesome-userscripts) - 📖  A curated list of Awesome Userscripts.
 * [awesome-azure-openai-llm](https://github.com/kimtth/awesome-azure-openai-llm) - A curated list of 🌌 Azure OpenAI, 🦙 Large Language Models (incl. RAG, Agent), and references with memos.
 * [best-of-ml-python](https://github.com/lukasmasuch/best-of-ml-python) - 🏆 A ranked list of awesome machine learning Python libraries. Updated weekly.
 * [simple-openai](https://github.com/sashirestela/simple-openai) - A Java library to use the OpenAI Api in the simplest possible way.
 * [Memori](https://github.com/memorilabs/memori) - Open-Source Memory Engine for LLMs, AI Agents & Multi-Agent Systems
 * [awesome-chatgpt](https://github.com/korchasa/awesome-chatgpt) - A curated list of awesome ChatGPT software.
 * [awesome-ai-tools](https://github.com/eudk/awesome-ai-tools) - 🔴 VERY LARGE AI TOOL LIST! 🔴  Curated list of AI Tools  - Updated September 2025
 * [hive](https://github.com/adenhq/hive) - Outcome driven agent development framework that evolves
 * [awesome-slash](https://github.com/avifenesh/awesome-slash) - Plugins & skills for Claude Code, OpenCode & Codex CLI. 29 autonomous agents for workflow automation, code review, slop detection, PR management, drift detection & more.
 * [prompts.chat](https://github.com/f/prompts.chat) - a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
 * [Awesome-ChatGPT-Prompts-CN](https://github.com/wikieden/awesome-chatgpt-prompts-cn) - ChatGPT调教指南|咒语指南|聊天提示词指南|学习指南
 * [Awesome-GPT-Image-2-API-Prompts](https://github.com/anil-matcha/awesome-gpt-image-2-api-prompts) - Curated GPT-Image-2 prompts for the OpenAI API — portraits, posters, UI mockups, game screenshots, character sheets, and more. Ready-to-use prompts for gpt-image-2.
 * [awesome-gpt-image-2-prompts](https://github.com/evolinkai/awesome-gpt-image-2-prompts) - Curated GPT-Image-2 prompts fot the Openai API：image examples across portraits, posters, UI mockups, character sheets, and community experiments.
 * [awesome-ai-startups](https://github.com/nowork-studio/awesome-ai-startups) - A curated list of indie-built AI startups — bootstrapped, pre-seed, and angel-funded products only.
 * [ai-models](https://github.com/i-need-token/ai-models) - Structured YAML catalog of 4,587 AI models across 95 providers — pricing, context windows, modalities, capabilities. First-party data with TypeScript types and Zod validation.
 * [awesome-gpt-image-2](https://github.com/youmind-openlab/awesome-gpt-image-2) - 🚀 World's largest GPT Image 2 prompt library, updated daily — 2000+ curated prompts with preview images, 16 languages. OpenAI's next-gen image model with pixel-perfect text rendering, cross-image consistency, and commercial-grade illustration. Free & open source.
 * [awesome-agentic-ai](https://github.com/adriannoes/awesome-agentic-ai) - 329 agent skills (Cursor, Claude Code & Codex), 5,380 OpenClaw skills, 201 ML notebooks, 9 textbooks, 82 research papers, 85 curated projects, 18 industry reports for PMs, Designers & Developers.


## Prompts

 * [gpt-repository-loader](https://github.com/mpoon/gpt-repository-loader) - Convert code repos into an LLM prompt-friendly format. Mostly built by GPT-4.
 * [myGPTReader](https://github.com/madawei2699/mygptreader) - myGPTReader is a bot on Slack that can read and summarize any webpage, documents including ebooks, or even videos from YouTube. It can communicate with you through voice.
 * [PromptCraft-Robotics](https://github.com/microsoft/promptcraft-robotics) - Community for applying LLMs to robotics and a robot simulator with ChatGPT integration
 * [chat-gpt-quine](https://github.com/fullthom/chat-gpt-quine) - @realtimeai someone tried to make a self-improving prompt with chatgpt a few weeks back. it only took 11 generations for it to collapse into a... pathological mode.
 * [blender_jarvis](https://github.com/dene33/blender_jarvis) - Control Blender through text prompts with help of ChatGPT
 * [Promptify](https://github.com/promptslab/promptify) - Prompt Engineering | Use GPT or other prompt based models to get structured output. Join our discord for Prompt-Engineering, LLMs and other latest research
 * [SchemaGPT](https://github.com/u-hubar/schemagpt) - Python library for RDF Schemas generation from prompts using GPT-3 magic 🪄🪄🪄
 * [CaFo](https://github.com/zrrskywalker/cafo) - [CVPR 2023] Prompt, Generate, then Cache: Cascade of Foundation Models makes Strong Few-shot Learners
 * [gpt3-interview-bot](https://github.com/promptable/gpt3-interview-bot) - GPT3 Interview Chatbot
 * [ama_prompting](https://github.com/hazyresearch/ama_prompting) - Ask Me Anything language model prompting
 * [LMOps](https://github.com/microsoft/lmops) - General technology for enabling AI capabilities w/ LLMs and MLLMs
 * [bark](https://github.com/suno-ai/bark) - 🔊 Text-Prompted Generative Audio Model
 * [Prompt-Engineering-Guide](https://github.com/dair-ai/prompt-engineering-guide) - 🐙 Guides, papers, lecture, notebooks and resources for prompt engineering
 * [langchain-and-elevenlabs-with-pdf-analysis](https://github.com/unicornlaunching/langchain-and-elevenlabs-with-pdf-analysis) - How might we mix OpenAI and Langchain and ElevenLabs to speak out responses to prompts using a body of knowledge encapsulated in PDFs?
 * [promptr](https://github.com/ferrislucas/promptr) - Promptr is a CLI tool for operating on your codebase using GPT. Promptr dynamically includes one or more files into your GPT prompts, and it can optionally parse and apply the changes that GPT suggests to your codebase. Several prompt templates are included for various purposes, and users can create their own templates.
 * [chatgpt-clone](https://github.com/danny-avila/chatgpt-clone) - Clone of ChatGPT, uses official model & Bing, reverse-engineered UI, with AI model switching, message search, and prompt templates (WIP)
 * [ChatGPT-Prompt-Genius](https://github.com/benf2004/chatgpt-prompt-genius) - get your creative juices flowing not only with the prompts but feel free to contribute to this open source project too #chatgpt #gpt4 #chatgptprompts
 * [ChatGPT-Adventure](https://github.com/capnmidnight/chatgpt-adventure) - A starting prompt for ChatGPT to create a text-adventure game
 * [chatgpt-text-to-midjourney-image](https://github.com/barretlee/chatgpt-text-to-midjourney-image) - Optimize the prompt using ChatGPT, then send it to Replicate to create an image.
 * [Prompt-hunter](https://github.com/op7418/prompt-hunter) - Save the Prompt and images from the Midjourney details page to your Notion page
 * [chatbox](https://github.com/bin-huang/chatbox) - A desktop app for ChatGPT API (OpenAI API) that supports Windows, Mac & Linux.  开源的ChatGPT桌面应用，prompt 开发神器，全平台支持，下载安装包就能用
 * [ChatGPT-Shortcut](https://github.com/rockbenben/chatgpt-shortcut) - Maximize your efficiency and productivity. 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。
 * [promptable](https://github.com/cfortuner/promptable) - Build LLM apps in Typescript/Javascript. 🧑‍💻 🧑‍💻 🧑‍💻 🚀 🚀 🚀
 * [ChatGPT3-Free-Prompt-List](https://github.com/mattnigh/chatgpt3-free-prompt-list) - A free guide for learning to create ChatGPT3 Prompts
 * [prompt-engine](https://github.com/microsoft/prompt-engine) - Create apps with Figma
 * [ChatGPT-Siri](https://github.com/yue-yang/chatgpt-siri) - Shortcuts for Siri using ChatGPT API gpt-3.5-turbo & gpt-4 model, supports continuous conversations, configure the API key & save chat records. 由 ChatGPT API gpt-3.5-turbo & gpt-4 模型驱动的智能 Siri，支持连续对话，配置API key，配置系统prompt，保存聊天记录。
 * [The-HustleGPT-Challenge](https://github.com/jtmuller5/the-hustlegpt-challenge) - Building Startups with an AI Co-Founder
 * [docsgpt](https://github.com/arc53/docsgpt) - creating small models with fine tuning:- :- :-  engineering:-   chain of hindsight promptint-
 * [chatgpt-prompts](https://github.com/carterleffen/chatgpt-prompts) - Here are the prompts I’ve created and want to share.
 * [ChatGPT-Data-Science-Prompts](https://github.com/travistangvh/chatgpt-data-science-prompts) - A repository of 60 useful data science prompts for ChatGPT
 * [CWK-ChatGPT-MidJourney-Prompt-Template](https://github.com/neobundy/cwk-chatgpt-midjourney-prompt-template) - cwk-chatgpt-midjourney-prompt-template v1.2probably the last version: 23 prompt types supported.i will switch to an object oriented approach: a complete rewrite. it will work better with chatgpt.there's a 1.2 light branch in the repo dropping a few …
 * [chatgpt-prompts-bug-bounty](https://github.com/taksec/chatgpt-prompts-bug-bounty) - ChatGPT Prompts for Bug Bounty & Pentesting
 * [Share-to-ChatGPT-Shortcut](https://github.com/reorx/share-to-chatgpt-shortcut) - An Apple Shortcut for sharing text to ChatGPT using personalized prompts
 * [ChatGPT-Prompts](https://github.com/prathamkumar14/chatgpt-prompts) - AI is taking over slowly. Here are some use ChatGPT/API prompts that help you unlock 100% of your productivity.
 * [soren](https://github.com/jacksonmills/soren) - SorenCAI is an AI software engineer assistant prompt
 * [chatbot-injections-exploits](https://github.com/cranot/chatbot-injections-exploits) - ChatBot Injection and Exploit Examples: A Curated List of Prompt Engineer Commands - ChatGPT
 * [ai-notes](https://github.com/sw-yx/ai-notes) - notes for software engineers getting up to speed on new AI developments. Serves as datastore for lspace.swyx.io writing, and product brainstorming, but has cleaned up canonical references under the /Resources folder.
 * [squidgy-prompts](https://github.com/squidgyai/squidgy-prompts) - #chatgpt and language learning?we’ve just released an open source set of prompts to help learners build decks, sentence mine, correct grammar, play word games and more. can be used on their own or in @squidgiesapp.
 * [ChatGPT_DAN](https://github.com/0xk1h0/chatgpt_dan) - ChatGPT DAN, Jailbreaks prompt
 * [ResearchChatGPT](https://github.com/hollobit/researchchatgpt) - 50 use cases of ChatGPT for research work
 * [FinGPT](https://github.com/ai4finance-foundation/fingpt) - Open-source for open finance!  Revolutionize 🔥
 * [aish](https://github.com/aishell-io/aish) - A ChatGPT CLI with local storage for prompts and messages.
 * [Mr.-Ranedeer-AI-Tutor](https://github.com/jushbjj/mr.-ranedeer-ai-tutor) - A GPT-4 AI Tutor Prompt for customizable personalized learning experiences.
 * [ChatGPT-Prompt-Engineering-for-Developers-in-Chinese](https://github.com/githubdaily/chatgpt-prompt-engineering-for-developers-in-chinese) - 《面向开发者的 ChatGPT 提示词工程》非官方版中英双语字幕 Unofficial subtitles of "ChatGPT Prompt Engineering for Developers"
 * [prompt-engineering-for-developers](https://github.com/datawhalechina/prompt-engineering-for-developers) - 吴恩达《ChatGPT Prompt Engineering for Developers》课程中文版，视频地址：https://www.bilibili.com/video/BV1Bo4y1A7FU
 * [unleashedgpt](https://github.com/ambr0sial/unleashedgpt) - UnleashedGPT: Yet Another ChatGPT Jailbreak
 * [GPT-Prompts](https://github.com/jesselau76/gpt-prompts) - Useful GPT Prompts
 * [prompt-engineering](https://github.com/brexhq/prompt-engineering) - Tips and tricks for working with Large Language Models like OpenAI's GPT-4.
 * [wonderful-prompts](https://github.com/yzfly/wonderful-prompts) - 🔥中文 prompt 精选🔥，ChatGPT 使用指南，提升 ChatGPT 可玩性和可用性！🚀
 * [RecurrentGPT](https://github.com/aiwaves-cn/recurrentgpt) - RecurrentGPT: Interactive Generation of (Arbitrarily) Long TextGenerates a paragraph at each timestep and updates its language-based long-short term memory stored on the hard drive and the prompt, respectively. repo:  abs:
 * [jopilot-4-job-seekers](https://github.com/jopilot-net/jopilot-4-job-seekers) - The prompts supported by JoPilot
 * [chain-of-thought-hub](https://github.com/franxyao/chain-of-thought-hub) - Benchmarking large language models' complex reasoning ability with chain-of-thought prompting
 * [ChatGPT-Admin-Web](https://github.com/aprilnea/chatgpt-admin-web) - 带有用户管理和后台管理系统的 ChatGPT WebUI
 * [powerplatform-prompts](https://github.com/pnp/powerplatform-prompts) - This repository contains a collection of prompt examples to be used with GPT models in the Power Platform.
 * [tutor-gpt](https://github.com/plastic-labs/tutor-gpt) - LangChain LLM application. Dynamic few-shot metaprompting for the task of tutoring.
 * [chat-gpt-games](https://github.com/admtal/chat-gpt-games) - Prompts for playable games in ChatGPT
 * [TaskMatrix](https://github.com/microsoft/taskmatrix) - @jksyaw @LangChainAI @FlowiseAI @bubble If the prompts are descriptive and distinguishable from each other, my understanding is the agent can still work fine for a large number of tools. For a sample use of a list of tools check out Microsoft's visualChatGPT repo  not sure with 1 million…
 * [GPTWorld](https://github.com/srush/gptworld) - A puzzle to learn about prompting
 * [DemoGPT](https://github.com/melih-unsal/demogpt) - ⚡ DemoGPT enables you to create quick demos by just using prompts. ⚡    🌟 Star to support our work!
 * [text-to-colorscheme](https://github.com/svermeulen/text-to-colorscheme) - Neovim colorschemes generated on the fly with a text prompt using ChatGPT
 * [gpt-prompt-engineer](https://github.com/mshumer/gpt-prompt-engineer) - Introducing `gpt-prompt-engineer` ✍️An agent that creates optimal GPT prompts.Just describe the task, and a chain of AI systems will:- Generate many possible prompts- Test them in a ranked tournament- Return the best promptAnd it's open-source:
 * [prompt-engineering-for-javascript-developers](https://github.com/dabit3/prompt-engineering-for-javascript-developers) - Notes summarized from ChatGPT Prompt Engineering for Developers by DeepLearning.ai
 * [gpt-runner](https://github.com/nicepkg/gpt-runner) - Conversations with your files! Manage and run your AI presets!
 * [promptmap](https://github.com/utkusen/promptmap) - automatically tests prompt injection attacks on ChatGPT instances
 * [IntelliNode](https://github.com/barqawiz/intellinode) - Access the latest AI models like ChatGPT, LLaMA, Stable Diffusion, WaveNet, and beyond through a unified prompt layer and performance evaluation
 * [tree-of-thought-prompting](https://github.com/dave1010/tree-of-thought-prompting) - Using Tree-of-Thought Prompting to boost ChatGPT's reasoning
 * [chatGPT-prompt-scripts](https://github.com/wincheshe/chatgpt-prompt-scripts) - 油猴 chatgpt Prompt 脚本插件，在chatgpt聊天框导入Prompt 对话框
 * [llm.report](https://github.com/dillionverma/llm.report) - 📊 llm.report is an open-source logging and analytics platform for OpenAI: Log your ChatGPT API requests, analyze costs, and improve your prompts.
 * [InstructZero](https://github.com/lichang-chen/instructzero) - Official Implementation of InstructZero; the first framework to optimize bad prompts of ChatGPT(API LLMs) and finally obtain good prompts!
 * [chatgpt-prompt-engineering-for-developers](https://github.com/kevin-free/chatgpt-prompt-engineering-for-developers) - 吴恩达《ChatGPT Prompt Engineering for Developers》课程中英版
 * [chat-key](https://github.com/overflowy/chat-key) - Supercharge your productivity with ChatGPT and AutoHotkey 🚀
 * [openprompt.co](https://github.com/timqian/openprompt.co) - Create. Use. Share. ChatGPT prompts
 * [Get-Things-Done-with-Prompt-Engineering-and-LangChain](https://github.com/curiousily/get-things-done-with-prompt-engineering-and-langchain) - LangChain & Prompt Engineering tutorials on Large Language Models (LLMs) such as ChatGPT with custom data. Jupyter notebooks on loading and indexing data, creating prompt templates, CSV agents, and using retrieval QA chains to query the custom data. Projects for using a private LLM (Llama 2) for chat with PDF files, tweets sentiment analysis.
 * [LearnPrompt](https://github.com/learnprompt/learnprompt) - 永久免费开源的 AIGC 课程, 目前已支持 ChatGPT, Midjourney, Runway, Stable Diffusion, AI数字人，AI声音&音乐，大模型微调
 * [IntelliNode](https://github.com/intelligentnode/intellinode) - Access the latest AI models like ChatGPT, LLaMA, Diffusion, Hugging face, and beyond through a unified prompt layer and performance evaluation
 * [azure-openai-llm-vector-langchain](https://github.com/kimtth/azure-openai-llm-vector-langchain) - Azure OpenAI, OSS LLM 🌊1. Vector db and 🦙langchain 🔎2. RAG ChatGpt demo 3. Microsoft ♾️LLM 🌌 libraries, etc.
 * [ChatGPT-Assistant](https://github.com/pierxuy/chatgpt-assistant) - 基于Streamlit搭建的ChatGPT对话助手，无须科学上网即可使用，可免费云部署。支持多窗口、语音交流、对话留存、上下文预设以及参数调节等功能。
 * [dev-chatgpt-prompts](https://github.com/pickleboxer/dev-chatgpt-prompts) - 📚 Personal collection of ChatGPT prompts for developers!
 * [prompta](https://github.com/iansinnott/prompta) - ChatGPT UI that is keyboard-centric, mobile friendly, can syncs chat history across devices and search past conversations.
 * [ChatGPT-Prompt-Sample-Japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - ChatGPT の Prompt のサンプルです。
 * [chatgpt-prompts](https://github.com/jevantang/chatgpt-prompts) - 分门别类的 ChatGPT 中文引导语大全。
 * [chat-gpt-prompts-from-aiprm-zh](https://github.com/adambear/chat-gpt-prompts-from-aiprm-zh) - 来自aiprm社区的两千多个ChatGPT提示，使用GPT3.5的API完成的中文翻译
 * [botpress](https://github.com/botpress/botpress) - The open-source hub to build & deploy GPT/LLM Agents ⚡️
 * [promptflow](https://github.com/microsoft/promptflow) - Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring.
 * [generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) - 12 Lessons, Get Started Building with Generative AI  🔗 https://microsoft.github.io/generative-ai-for-beginners/
 * [tree-of-thoughts](https://github.com/kyegomez/tree-of-thoughts) - Plug in and Play Implementation of Tree of Thoughts: Deliberate Problem Solving with Large Language Models that Elevates Model Reasoning by atleast 70%
 * [Learn_Prompting](https://github.com/trigaten/learn_prompting) - Prompt Engineering, Generative AI, and LLM Guide by Learn Prompting | Join our discord for the largest Prompt Engineering learning community
 * [DecryptPrompt](https://github.com/dsxiangli/decryptprompt) - 总结Prompt&LLM论文，开源数据&模型，AIGC应用
 * [magentic](https://github.com/jackmpcollins/magentic) - Seamlessly integrate LLMs as Python functions
 * [chatgpt_system_prompt](https://github.com/louisshark/chatgpt_system_prompt) - store all agent's system prompt
 * [LangGPT](https://github.com/embraceagi/langgpt) - LangGPT: Empowering everyone to become a prompt expert!🚀  Structured Prompt，Language of GPT, 结构化提示词，结构化Prompt
 * [chatgpt-prompts-for-academic-writing](https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing) - This list of writing prompts covers a range of topics and tasks, including brainstorming research ideas, improving language and style, conducting literature reviews, and developing research plans.
 * [self-refine](https://github.com/madaan/self-refine) - LLMs can generate feedback on their work, use it to improve the output, and repeat this process iteratively.
 * [GPTs](https://github.com/linexjlin/gpts) - leaked prompts of GPTs
 * [multimodal-maestro](https://github.com/roboflow/multimodal-maestro) - Effective prompting for Large Multimodal Models like GPT-4 Vision, LLaVA or CogVLM. 🔥
 * [promptbench](https://github.com/microsoft/promptbench) - A unified evaluation framework for large language models
 * [Transformers-for-NLP-2nd-Edition](https://github.com/denis2054/transformers-for-nlp-2nd-edition) - Transformer models from BERT to GPT-4, environments from Hugging Face to OpenAI. Fine-tuning, training, and prompt engineering examples. A bonus section with ChatGPT, GPT-3.5-turbo, GPT-4, and DALL-E including jump starting GPT-4, speech-to-text, text-to-speech, text to image generation with DALL-E, Google Cloud AI,HuggingGPT, and more
 * [llm-guard](https://github.com/laiyer-ai/llm-guard) - The Security Toolkit for LLM Interactions
 * [Prompt4ReasoningPapers](https://github.com/zjunlp/prompt4reasoningpapers) - Repository for the ACL2023 paper "Reasoning with Language Model Prompting: A Survey".
 * [knowledge](https://github.com/knowledgecanvas/knowledge) - Knowledge is a tool for saving, searching, accessing, exploring and chatting with all of your favorite websites, documents and files.
 * [promptfoo](https://github.com/promptfoo/promptfoo) - Test your prompts, models, RAGs. Evaluate and compare LLM outputs, catch regressions, and improve prompt quality. LLM evals for OpenAI/Azure GPT, Anthropic Claude, VertexAI Gemini, Ollama, Local & private models like Mistral/Mixtral/Llama with CI/CD
 * [swarms](https://github.com/kyegomez/swarms) - Build, Deploy, and Scale Reliable Swarms of Autonomous Agents for Workflow Automation. Join our Community: https://discord.gg/DbjBMJTSWD
 * [gptstore-prompts](https://github.com/1003715231/gptstore-prompts) - Here are the Top 100 prompts on GPTStore, which we can use to learn and improve prompt engineering.
 * [aigc](https://github.com/phodal/aigc) - 《构筑大语言模型应用：应用开发与架构设计》一本关于 LLM 在真实世界应用的开源电子书，介绍了大语言模型的基础知识和应用，以及如何构建自己的模型。其中包括Prompt的编写、开发和管理，探索最好的大语言模型能带来什么，以及LLM应用开发的模式和架构设计。
 * [lingoose](https://github.com/henomis/lingoose) - 🪿 LinGoose it's a Go framework for developing LLMs-based application using pipelines
 * [llm-guard](https://github.com/protectai/llm-guard) - The Security Toolkit for LLM Interactions
 * [ChatGPT-Prompts](https://github.com/yokoffing/chatgpt-prompts) - ChatGPT and Bing AI prompt curation
 * [Safety-Prompts](https://github.com/thu-coai/safety-prompts) - Chinese safety prompts for evaluating and improving the safety of LLMs. 中文安全prompts，用于评估和提升大模型的安全性。
 * [ChatGPT-Academic-Prompt](https://github.com/xuhangc/chatgpt-academic-prompt) - Use ChatGPT for academic writing
 * [Instructgpt-prompts](https://github.com/kevinamiri/instructgpt-prompts) - A collection of ChatGPT and GPT-3.5 instruction-based prompts for generating and classifying text.
 * [EdgeChains](https://github.com/arakoodev/edgechains) - EdgeChains.js Typescript/Javascript production-friendly Generative AI.  Based on Jsonnet. Works anywhere that Webassembly does. Prompts live declaratively & "outside code in config". Kubernetes & edge friendly. Compatible with OpenAI GPT, Gemini, Llama2, Anthropic, Mistral and others
 * [prompt-tutorial](https://github.com/pandabearlab/prompt-tutorial) - chatGPT、prompt、LLM
 * [chatdev](https://github.com/10cl/chatdev) - ChatDev IDE is an tools for building your ai agent, Whether it's NPCs in games or powerful agent tools, you can design what you want for this platform.
 * [contoso-chat](https://github.com/azure-samples/contoso-chat) - This sample has the full End2End process of creating RAG application with Prompt Flow and AI Studio. It includes GPT 3.5 Turbo LLM application code, evaluations, deployment automation with AZD CLI, GitHub actions for evaluation and deployment and intent mapping for multiple LLM task mapping.
 * [LangGPT](https://github.com/langgptai/langgpt) - LangGPT: Empowering everyone to become a prompt expert!🚀  Structured Prompt，Language of GPT, 结构化提示词，结构化Prompt
 * [AISuperDomain](https://github.com/win4r/aisuperdomain) - Aila(AI超元域): The premier AI integration tool for Windows, macOS, and Android. Ask once, get answers from 10+ AIs like ChatGPT, Gemini, Claude3, Copilot, Poe, perplexity and more. Features customizable AI and prompts.
 * [code2prompt](https://github.com/mufeedvh/code2prompt) - A CLI tool to convert your codebase into a single LLM prompt with source tree, prompt templating, and token counting.
 * [LLM-Prompt-Library](https://github.com/abilzerian/llm-prompt-library) - Advanced Code and Text Manipulation Prompts for Various LLMs. Suitable for GPT-4, Claude, Llama3, Gemini, and other high-performance open-source LLMs.
 * [zzz-api](https://github.com/xing61/zzz-api) - 优质稳定的OpenAI的API接口-For企业和开发者。OpenAI的api proxy，支持ChatGPT的API调用，支持openai的API接口，支持：gpt-4，gpt-3.5。不需要openai Key, 不需要买openai的账号，不需要美元的银行卡，通通不用的，直接调用就行，稳定好用！！智增增
 * [EasyInstruct](https://github.com/zjunlp/easyinstruct) - [ACL 2024] An Easy-to-use Instruction Processing Framework for LLMs.
 * [FinRobot](https://github.com/ai4finance-foundation/finrobot) - FinRobot: An Open-Source AI Agent Platform for Financial Applications using LLMs 🚀 🚀 🚀
 * [wonderful-prompts](https://github.com/langgptai/wonderful-prompts) - 🔥中文 prompt 精选🔥，ChatGPT 使用指南，提升 ChatGPT 可玩性和可用性！🚀
 * [jailbreak_llms](https://github.com/verazuo/jailbreak_llms) - [CCS'24] A dataset consists of 15,140 ChatGPT prompts from Reddit, Discord, websites, and open-source datasets (including 1,405 jailbreak prompts).
 * [step_into_llm](https://github.com/mindspore-courses/step_into_llm) - MindSpore online courses: Step into LLM
 * [promptulate](https://github.com/undertone0809/promptulate) - 🚀Large language model automation and Autonomous Language Agents development framework. Build your LLM Agent Application in a pythonic way!
 * [EDDI](https://github.com/labsai/eddi) - Prompt & Conversation Management Middleware for Conversational AI APIs such as OpenAI ChatGPT, Facebook Hugging Face, Anthropic Claude, Google Gemini and Ollama. Lean, restful, scalable, and cloud-native. Developed in Java, powered by Quarkus, provided with Docker, and orchestrated with Kubernetes or Openshift.
 * [AIGC_Interview](https://github.com/embraceagi/aigc_interview) - 📚 AIGC 求职面经、必备基础知识、提示词工程、ChatGPT、Stable Diffusion、Prompt、Embedding、Fintune 等 AIGC 求职你所需要知道的一切~
 * [npi](https://github.com/npi-ai/npi) - Tool use APIs platform for AI Agent
 * [keras-llm-robot](https://github.com/smalltong02/keras-llm-robot) - A web UI Project In order to learn the large language model. This project includes features such as chat, quantization, fine-tuning, prompt engineering templates, and multimodality.
 * [ComfyUI-N-Nodes](https://github.com/nuked88/comfyui-n-nodes) - A suite of custom nodes for ConfyUI that includes GPT text-prompt generation, LoadVideo, SaveVideo, LoadFramesFromFolder and FrameInterpolator
 * [PromptChains](https://github.com/miatechpartners/promptchains) - Queue up prompts for ChatGPT and Claude for better performance
 * [aide](https://github.com/nicepkg/aide) - Conquer Any Code in VSCode: One-Click Comments, Conversions, UI-to-Code, and AI Batch Processing of Files! 在 VSCode 中征服任何代码：一键注释、转换、UI 图生成代码、AI 批量处理文件！💪
 * [comfyui_LLM_party](https://github.com/heshengtao/comfyui_llm_party) - RAG.
 * [ChatGPT-OpenAI-Smart-Speaker](https://github.com/olney1/chatgpt-openai-smart-speaker) - This AI Smart Speaker uses speech recognition and text-to-speech to enable voice-driven conversations and vision capabilities with OpenAI and Agents. The user speaks a prompt into the microphone, and the program sends the prompt to OpenAI to generate a response. The response is then converted to an audio file and played back to the user.
 * [AI-Bootcamp](https://github.com/curiousily/ai-bootcamp) - Self-paced bootcamp on Generative AI. Tutorials on ML fundamentals, LLMs, RAGs, LangChain, LangGraph, Fine-tuning Llama 3 & AI Agents (CrewAI)
 * [chatgpt-lite](https://github.com/blrchen/chatgpt-lite) - Fast ChatGPT UI with support for both OpenAI and Azure OpenAI. 快速的ChatGPT UI，支持OpenAI和Azure OpenAI。
 * [Long-Novel-GPT](https://github.com/maoxiaoyuz/long-novel-gpt) - 该项目包括一个基于 GPT 等大语言模型的长篇小说生成器，同时还有各类小说生成 Prompt 以及教程。我们欢迎社区贡献，持续更新以提供最佳的小说创作体验。
 * [langfuse](https://github.com/langfuse/langfuse) - 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. Integrates with LlamaIndex, Langchain, OpenAI SDK, LiteLLM, and more. 🍊YC W23
 * [gateway](https://github.com/portkey-ai/gateway) - A Blazing Fast AI Gateway with integrated Guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.
 * [ai-notes](https://github.com/swyxio/ai-notes) - notes for software engineers getting up to speed on new AI developments. Serves as datastore for https://latent.space writing, and product brainstorming, but has cleaned up canonical references under the /Resources folder.
 * [helicone](https://github.com/helicone/helicone) - 🧊 Open source LLM-Observability Platform for Developers. One-line integration for monitoring, metrics, evals, agent tracing, prompt management, playground, etc. Supports OpenAI SDK, Vercel AI SDK, Anthropic SDK, LiteLLM, LLamaIndex, LangChain, and more. 🍓 YC W23
 * [optillm](https://github.com/codelion/optillm) - Optimizing inference proxy for LLMs
 * [lunary](https://github.com/lunary-ai/lunary) - The production toolkit for LLMs. Observability, prompt management and evaluations.
 * [pezzo](https://github.com/pezzolabs/pezzo) - 🕹️ Open-source, developer-first LLMOps platform designed to streamline prompt design, version management, instant delivery, collaboration, troubleshooting, observability and more.
 * [archgw](https://github.com/katanemo/archgw) - Arch is an intelligent gateway for agents. Engineered with (fast) LLMs for the secure handling, rich observability, and seamless integration of prompts with your APIs - all outside business logic. Built by the core contributors of Envoy proxy, on Envoy.
 * [openlit](https://github.com/openlit/openlit) - Open source platform for AI Engineering: OpenTelemetry-native LLM Observability, GPU Monitoring, Guardrails, Evaluations, Prompt Management, Vault, Playground. 🚀💻 Integrates with 40+ LLM Providers, VectorDBs, Agent Frameworks and GPUs.
 * [GPTS-Prompt-Collection](https://github.com/b3o/gpts-prompt-collection) - Collect the prompt of GPTS
 * [chatgpt-custom-instructions](https://github.com/denissergeevitch/chatgpt-custom-instructions) - My own Prompts for Custom instructions ChatGPT
 * [prompt-layer-library](https://github.com/magnivorg/prompt-layer-library) - 🍰 PromptLayer - Maintain a log of your prompts and OpenAI API requests. Track, debug, and replay old completions.
 * [langwatch](https://github.com/langwatch/langwatch) - The ultimate LLM Ops platform - Monitoring, Analytics, Evaluations, Datasets and Prompt Optimization ✨
 * [phoenix](https://github.com/arize-ai/phoenix) - AI Observability & Evaluation
 * [DataDreamer](https://github.com/datadreamer-dev/datadreamer) - DataDreamer: Prompt. Generate Synthetic Data. Train & Align Models.    🤖💤
 * [LangChain](https://github.com/tryagi/langchain) - C# implementation of LangChain. We try to be as close to the original as possible in terms of abstractions, but are open to new entities.
 * [Kiln](https://github.com/kiln-ai/kiln) - The easiest tool for fine-tuning LLM models, synthetic data generation, and collaborating on datasets.
 * [JamAIBase](https://github.com/embeddedllm/jamaibase) - The collaborative spreadsheet for AI. Chain cells into powerful pipelines, experiment with prompts and models, and evaluate LLM responses in real-time. Work together seamlessly to build and iterate on AI applications.
 * [langtrace](https://github.com/scale3-labs/langtrace) - Langtrace 🔍 is an open-source,  Open Telemetry based end-to-end observability tool for LLM applications, providing real-time tracing, evaluations and metrics for popular LLMs, LLM frameworks, vectorDBs and more.. Integrate using Typescript, Python. 🚀💻📊
 * [learn-modern-ai-python](https://github.com/panaversity/learn-modern-ai-python) - Learn Modern AI Assisted Python with Type Hints
 * [CL4R1T4S](https://github.com/elder-plinius/cl4r1t4s) - SYSTEM PROMPT TRANSPARENCY FOR ALL
 * [ChatGPT-Free-Prompt-List](https://github.com/mattnigh/chatgpt-free-prompt-list) - A free guide for learning to create ChatGPT3 Prompts
 * [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) - Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini
 * [fellow](https://github.com/manuelzierl/fellow) - Fellow is a command-line interface (CLI) tool that acts as an autonomous software engineering assistant. It uses the OpenAI API to perform various structured tasks by reasoning step-by-step, executing commands, and maintaining a log of its activities.
 * [just-prompt](https://github.com/disler/just-prompt) - just-prompt is an MCP server that provides a unified interface to top LLM providers (OpenAI, Anthropic, Google Gemini, Groq, DeepSeek, and Ollama)
 * [GenerativeAI-Prompt-Sample-Japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPTやCopilotなど各種生成AI用の「日本語]の Prompt のサンプル
 * [judgeval](https://github.com/judgmentlabs/judgeval) - The open source post-building layer for agents. Our traces + evals power agent post-training (RL, SFT), monitoring, and regression testing.
 * [gateway](https://github.com/adaline/gateway) - The only fully local production-grade Super SDK that provides a simple, unified, and powerful interface for calling more than 200+ LLMs.
 * [zcf](https://github.com/ufomiao/zcf) - Zero-Config Code Flow for Claude code & Codex
 * [generator](https://github.com/context-hub/generator) - CTX: a tool that solves the context management gap when working with LLMs like ChatGPT or Claude. It helps developers organize and automatically collect information from their codebase into structured documents that can be easily shared with AI assistants.
 * [aicodeprep-gui](https://github.com/detroittommy879/aicodeprep-gui) - Surgical context engineering with a nice UI, Windows, Mac, Linux, BSD, anywhere where python & Qt run
 * [codexia](https://github.com/milisp/codexia) - A powerful GUI/IDE and Toolkit for Codex CLI. Fork chat + FileTree + prompt notepad, Codex community and more
 * [optillm](https://github.com/algorithmicsuperintelligence/optillm) - Optimizing inference proxy for LLMs
 * [codexia](https://github.com/codexia-team/codexia) - A powerful GUI/IDE and Toolkit for Codex CLI. Fork chat + FileTree + prompt notepad + git worktree and more
 * [product-manager-prompts](https://github.com/deanpeters/product-manager-prompts) - A repository of Generative AI prompts for product managers using agents such as ChatGPT, Claude, & Gemini
 * [runprompt](https://github.com/chr15m/runprompt) - Run LLM prompts from your shell
 * [plano](https://github.com/katanemo/plano) - Ship agents faster. Plano is delivery infrastructure for agentic applications. A models-native proxy server & dataplane that offloads the plumbing work, so you stay focused on product logic.
 * [chat-gpt-prompts-from-aiprm](https://github.com/gabriel-kaam/chat-gpt-prompts-from-aiprm) - Compilations of ChatGPT Prompts from AIPRM
 * [gollm](https://github.com/teilomillet/gollm) - Unified Go interface for Language Model (LLM) providers. Simplifies LLM integration with flexible prompt management and common task functions.
 * [taskade](https://github.com/taskade/taskade) - The AI-native workspace platform. Build apps, deploy agents, automate workflows — from one prompt.
 * [Athena-Public](https://github.com/winstonkoh87/athena-public) - The Linux OS for AI Agents — Persistent memory, autonomy, and time-awareness for any LLM. Own the state. Rent the intelligence.
 * [chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) - Easily collect responses from ChatGPT scraper by providing a prompt along with valid Web Scraper API credentials.
 * [Prompt-Engineering-Guide-zh-CN](https://github.com/yunwei37/prompt-engineering-guide-zh-cn) - 🐙 关于提示词工程（prompt）的指南、论文、讲座、笔记本和资源大全（自动持续更新）
 * [Prompt_Engineering](https://github.com/nirdiamant/prompt_engineering) - 22 prompt engineering techniques with hands-on Jupyter Notebook tutorials, from fundamental concepts to advanced strategies for leveraging LLMs.
 * [open-codesign](https://github.com/opencoworkai/open-codesign) - PDF. Multi-model (Claude, GPT, Gemini, Kimi, GLM, Ollama). BYOK, local-first, MIT.
 * [openpencil](https://github.com/zseven-w/openpencil) - The world's first open-source AI-native vector design tool and the first to feature concurrent Agent Teams. Design-as-Code. Turn prompts into UI directly on the live canvas. A modern alternative to Pencil.
 * [Vibe-Skills](https://github.com/foryourhealth111-pixel/vibe-skills) - Vibe-Skills is an all-in-one AI skills package. It seamlessly integrates expert-level capabilities and context management into a general-purpose skills package， enabling any AI agent to instantly upgrade its functionality—eliminating the friction of fragmented tools and complex harnesses.
 * [typeui](https://github.com/bergside/typeui) - Design skills and UI prompts for agentic tools such as Claude Design, Google Stitch, Codex, Cursor, and other AI tools
 * [eval-harness](https://github.com/nano-step/eval-harness) - Behavior-regression testing for LLM agents. 4-class attribution, 6-field FAIL schema, $-cost gating, flaky detection. Bash + jq. Works with opencode today, runner-pluggable.
 * [ccline](https://github.com/jianshuo/ccline) - Type a thought at your zsh prompt, get an answer — and run the command it suggests
 * [presentation-design-prompts](https://github.com/slidespeak/presentation-design-prompts) - Free presentation slide design.md you can paste into ChatGPT, Claude or any of your AI tools.
 * [headroom](https://github.com/headroomlabs-ai/headroom) - Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server.
 * [Rapid-MLX](https://github.com/raullenchai/rapid-mlx) - The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool parsers, prompt cache, reasoning separation, cloud routing. Drop-in OpenAI replacement. Works with Claude Code, Cursor, Aider.
 * [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) - Skill that audits and rewrites content to remove AI writing patterns. Use it with your favorite agents including Claude Code, OpenClaw, Codex, and Hermes.
 * [vibe-coding-cn](https://github.com/tradecatlabs/vibe-coding-cn) - Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南
 * [agent-manager](https://github.com/yoanwai/agent-manager) - The fastest developer workflow for every AI coding agent. Live status, quick prompts, worktrees, and diff review from one tmux TUI.
 * [ChatGPT-Workflows](https://github.com/rongnianxin/chatgpt-workflows) - ChatGPT 与 Codex 的可验证工作流、断点交接、网页增强和本地工具


## Chatbots

 * [gpt4all](https://github.com/nomic-ai/gpt4all) - gpt4all: a chatbot trained on a massive collection of clean assistant data including code, stories and dialogue
 * [Open-Assistant](https://github.com/laion-ai/open-assistant) - OpenAssistant is a chat-based assistant that understands tasks, can interact with third-party systems, and retrieve information dynamically to do so.
 * [FastChat](https://github.com/lm-sys/fastchat) - The release repo for "Vicuna: An Open Chatbot Impressing GPT-4"
 * [kubernetes-chatgpt-bot](https://github.com/robusta-dev/kubernetes-chatgpt-bot) - A ChatGPT bot for Kubernetes issues.
 * [chatGPT-telegram-bot](https://github.com/altryne/chatgpt-telegram-bot) - This is a very early attempt at having chatGPT work within a telegram bot
 * [chatgpt_telegram_bot](https://github.com/karfly/chatgpt_telegram_bot) - cómo integrar chatgpt con gpt-4 en telegram://t.co/fyumptn5vjvía @hipertextual
 * [ChatRWKV](https://github.com/blinkdl/chatrwkv) - ChatRWKV is like ChatGPT but powered by RWKV (100% RNN) language model, and open source.
 * [ChatGPT-at-Home](https://github.com/sentdex/chatgpt-at-home) - ChatGPT @ Home: Large Language Model (LLM) chatbot application, written by ChatGPT
 * [ChuanhuChatGPT](https://github.com/gaizhenbiao/chuanhuchatgpt) - GUI for ChatGPT API
 * [GPT3Discord](https://github.com/kav-k/gpt3discord) - A robust, all-in-one GPT3 interface for Discord. ChatGPT-style conversations, image generation, AI-moderation, custom indexes/knowledgebase, youtube summarizer, and more!
 * [chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat) - Wechat robot based on ChatGPT,  which using OpenAI api and itchat library. 使用ChatGPT搭建微信聊天机器人，基于GPT3.5 API和itchat实现
 * [ChatGPT-in-Slack](https://github.com/seratch/chatgpt-in-slack) - Swift demonstration of how to build a Slack app that enables end-users to interact with a ChatGPT bot
 * [gpt-discord-bot](https://github.com/openai/gpt-discord-bot) - Example Discord bot written in Python that uses the completions API to have conversations with the `text-davinci-003` model, and the moderations API to filter the messages.
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - OpenAIのChatGPT APIをSlack上で利用するためのSlackbotスクリプト (日本語での利用が前提)
 * [chatGPT-discord-bot](https://github.com/zero6992/chatgpt-discord-bot) - Integrate ChatGPT into your own discord bot
 * [vrchatbot](https://github.com/geson-anko/vrchatbot) - VRChatにAI Botを作るためのリポジトリ
 * [Blender-GPT](https://github.com/tree-ind/blender-gpt) - An all-in-one Blender assistant powered by GPT3/4 + Whisper integration
 * [dolly](https://github.com/databrickslabs/dolly) - Databricks’ Dolly, a large language model trained on the Databricks Machine Learning Platform
 * [chatgpt-failures](https://github.com/giuven95/chatgpt-failures) - Failure archive for ChatGPT and similar models
 * [researchgpt](https://github.com/mukulpatnaik/researchgpt) - An open-source LLM based research assistant that allows you to have a conversation with a research paper
 * [wikipedia-gpt3-bot](https://github.com/shbhrsaha/wikipedia-gpt3-bot) - REPL bot that answers questions by querying Wikipedia and summarizing answers with GPT-3
 * [chatgpt-tegram-bot](https://github.com/nukeador/chatgpt-tegram-bot) - A simple bot for Telegram that allows interaction with ChatGPT (with voice notes and support for generating images).
 * [ChatGeoPT](https://github.com/earth-genome/chatgeopt) - A very basic, very brittle proof of concept for an AI assistant for geospatial search
 * [ChatGPT-Trading-Bot-for-KuCoin](https://github.com/krecicki/chatgpt-trading-bot-for-kucoin) - This is a trading script for KuCoin that continuously places buy and sell orders based on market data and a predictive model generated by OpenAI's GPT-3.5 language model.
 * [vocode-python](https://github.com/vocodedev/vocode-python) - 🤖 Build voice-based LLM agents. Modular + open source.
 * [marvin](https://github.com/prefecthq/marvin) - 🤖🪄 A batteries-included library for GPT-powered bots and AI functions
 * [baize](https://github.com/project-baize/baize) - Let ChatGPT teach your own chatbot in hours with a single GPU!
 * [baize-chatbot](https://github.com/project-baize/baize-chatbot) - Let ChatGPT teach your own chatbot in hours with a single GPU!
 * [gpt4all-ui](https://github.com/nomic-ai/gpt4all-ui) - gpt4all chatbot ui
 * [yolopandas](https://github.com/ccurme/yolopandas) - チャットでpandas操作これ便利。"fy23 q2のどこどこ会社の何何製品に関する売り上げデータをグラフ化してね。"ってセールスオペレーションチームにお願いしているので、これ使って簡単にchatgptにデータ取得お願いできるようにしよう。
 * [ChatDoctor](https://github.com/kent0n-li/chatdoctor) - 医療特化aiチャット「chatdoctor」chatgptも使ってモデルをトレーニングしてる様子全コードとデータセット、モデルの重みがオープンソース化する予定らしい..！
 * [gpt4free](https://github.com/xtekky/gpt4free) - decentralising the Ai Industry, free gpt-4/3.5 scripts through several reverse engineered api's ( poe.com, phind.com, chat.openai.com, phind.com, writesonic.com, sqlchat.ai, t3nsor.com, you.com etc...)
 * [Auto-GPT-ZH](https://github.com/kaqijiang/auto-gpt-zh) - Auto-GPT中文版本及爱好者组织 同步更新原项目 AI领域创业 自媒体组织 用AI工作学习创作变现
 * [voice-generator-webui](https://github.com/log1stics/voice-generator-webui) - A multi-speaker, multilingual speech generation tool
 * [autogpt-telegram-chatbot](https://github.com/steamship-packages/autogpt-telegram-chatbot) - it's here! autogpt for your mobile.communicate with your own version of autogpt via telegram.  proud to open source this project. can't wait to see what we'll build together!
 * [pdfGPT](https://github.com/bhaskatripathi/pdfgpt) - PDF GPT allows you to chat with the contents of your PDF file by using GPT capabilities. The only open source solution to turn your pdf files in a chatbot!
 * [Navi](https://github.com/ssgorg/navi) - A GPT based Cybersecurity AI
 * [chatgpt-comparison-detection](https://github.com/hello-simpleai/chatgpt-comparison-detection) - Human ChatGPT Comparison Corpus (HC3), Detectors, and more! 🔥
 * [hackGPT](https://github.com/nodatafound/hackgpt) - I leverage OpenAI and ChatGPT to do hackerish things
 * [talk-to-chatgpt](https://github.com/c-nedelcu/talk-to-chatgpt) - Talk to ChatGPT AI using your voice and listen to its answers through a voice
 * [ChatGPT-Telegram-Workers](https://github.com/tbxark/chatgpt-telegram-workers) - Deploy your own Telegram ChatGPT bot on Cloudflare Workers with ease.
 * [reflexion-human-eval](https://github.com/noahshinn024/reflexion-human-eval) - reflection-based gpt-4 agent is state-of-the-art on code geniteratively refines code, shifting “accuracy bottleneck” from correct code gen to correct test genhumaneval accuracy:-reflexion-based gpt-4 88% -gpt-4 67.0%-codet 65.8%-palm 26.2%code:
 * [gptchat-telegram](https://github.com/m1guelpf/gptchat-telegram) - ✨ got tired of opening the gptchat website every time, so i made a telegram bot.if you want one too, i made it extremely easy to set up (you only need to run a single command! 😯).check out the repo 👇
 * [Twitter-Comment-Bot](https://github.com/sojinsamuel/twitter-comment-bot) - A bot that comments on tweets containing a specified keyword. The bot uses the OpenAI API to generate comments and the Twitter API to post them. It is designed to run continuously, with a fixed delay between each comment.
 * [codemancer](https://github.com/0xmmo/codemancer) - AI coding assistant in your command line.
 * [ChatGPT-CodeReview](https://github.com/anc95/chatgpt-codereview) - 🐥 A code review bot powered by ChatGPT
 * [KeepChatGPT](https://github.com/xcanwin/keepchatgpt) - 让我们在使用ChatGPT过程中更高效、更顺畅，完美解决ChatGPT网络错误，不再频繁地刷新网页，足足省去10个多余的步骤。还可以取消后台监管审计。解决了这几类报错: (1) NetworkError when attempting to fetch resource. (2) Something went wrong. If this issue persists please contact us through our help center at help.openai.com. (3) This content may violate our content policy. (4) Conversation not found.
 * [chatgpt-wework-robot](https://github.com/sytpb/chatgpt-wework-robot) - 零代码、一键部署chatgpt到企业微信，无须VPN，速度快
 * [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) - An open source ChatGPT UI.
 * [gpt4-pdf-chatbot-langchain](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) - GPT4 & LangChain Chatbot for large PDF docs
 * [chat-with-gpt](https://github.com/cogentapps/chat-with-gpt) - An open-source ChatGPT app with a voice
 * [whatsapp-chatgpt](https://github.com/askrella/whatsapp-chatgpt) - ChatGPT + DALL-E + WhatsApp = AI Assistant :rocket: :robot:
 * [ChatGPT-wechat-bot](https://github.com/autumnwhj/chatgpt-wechat-bot) - ChatGPT for wechat https://github.com/AutumnWhj/ChatGPT-wechat-bot
 * [chatbot-ui-pro](https://github.com/mckaywrigley/chatbot-ui-pro) - AI search & chat for Balaji Srinivasan's "The Network State."
 * [chatgpt-twitter-bot](https://github.com/transitive-bullshit/chatgpt-twitter-bot) - Twitter bot powered by OpenAI's ChatGPT API. It's aliveeeee 🤖
 * [BetterChatGPT](https://github.com/ztjhz/betterchatgpt) - Play and chat smarter with Better ChatGPT - an amazing open-source web app with a better UI for exploring OpenAI's ChatGPT API! (Website + Windows + MacOS + Linux)
 * [chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter) - Export and Share your ChatGPT conversation history
 * [unChatGPT](https://github.com/riccardolinares/unchatgpt) - unChatGPT uses the OpenAI API to create a chatbot-like chat experience. It is a similar to ChatGPT, but without the need to wait in a queue or have limited access.
 * [rubberduck-vscode](https://github.com/rubberduck-ai/rubberduck-vscode) - Use AI-powered code edits, explanations, code generation, error diagnosis, and chat in Visual Studio Code with the official OpenAI API.
 * [teams-openai-bot](https://github.com/leeford/teams-openai-bot) - Sample Teams OpenAI bot
 * [speechgpt](https://github.com/hahahumble/speechgpt) - SpeechGPT is a web application that enables you to converse with ChatGPT.
 * [langchainjs](https://github.com/hwchase17/langchainjs) - we've implemented autogpt in js, along with new read and write tools to write files, which can be backed by both your local filesystem in node.js as well as an in-memory filesystem in all other js envs. we'll be evolving this over time. example here
 * [chat-langchainjs](https://github.com/sullivan-sean/chat-langchainjs) - replicating chatlangchain (a chatgpt-like bot that only answers questions about langchain documentation) with a typescript backed  heard @swyx is having a hackathon later today. hopefully this can serve as a starting point for some projects there!
 * [friday-gpt](https://github.com/hmmhmmhm/friday-gpt) - A.I 에게 R&R을 부여해서 프로그래밍 업무를 진행시킵니다.
 * [telegram-chatgpt-concierge-bot](https://github.com/rafalwilinski/telegram-chatgpt-concierge-bot) - Interact with OpenAI's ChatGPT via Telegram and Voice.
 * [chatgpt-telegram](https://github.com/m1guelpf/chatgpt-telegram) - Run your own GPTChat Telegram bot, with a single command!
 * [gitgpt](https://github.com/hesse/gitgpt) - A natural language command line git assistant
 * [chatgpt-discord](https://github.com/m1guelpf/chatgpt-discord) - Run your own GPTChat Discord bot, with a single command!
 * [larkgpt](https://github.com/bytemate/larkgpt) - Lark chatgpt bot
 * [LocalAI](https://github.com/go-skynet/localai) - :robot: Self-hosted, community-driven simple local OpenAI-compatible API written in go. Can be used as a drop-in replacement for OpenAI, running on CPU with consumer-grade hardware. API for ggml compatible models, for instance: llama.cpp, alpaca.cpp, gpt4all.cpp, vicuna, koala, gpt4all-j, cerebras
 * [gpt_jailbreak_status](https://github.com/tg12/gpt_jailbreak_status) - This is a repository that aims to provide updates on the status of jailbreaking the OpenAI GPT language model.
 * [chat-gpt](https://github.com/jcubic/chat-gpt) - ChatGPT conversation saving bookmark
 * [chatgpt-android](https://github.com/skydoves/chatgpt-android) - 📲 ChatGPT Android demonstrates OpenAI's ChatGPT on Android with Stream Chat SDK for Compose.
 * [gpt-voice-chat](https://github.com/kmizu/gpt-voice-chat) - A real voice chat with ChatGPT AI
 * [chatgpt](https://github.com/jcrodriguez1989/chatgpt) - Interface to ChatGPT from R
 * [ChatdollKit](https://github.com/uezo/chatdollkit) - ChatdollKit enables you to make your 3D model into a chatbot
 * [unity-voicevox-bridge](https://github.com/mikito/unity-voicevox-bridge) - unity上からvoicevoxと連携して合成音声を簡単に再生できるシンプルなライブラリ作ってみました！chatgpt apiとかのお供に！
 * [gortanagtp](https://github.com/dasdata/gortanagtp) - Console Application with Voice and Text Interaction Latest ChatGPT API
 * [HeyChatGPT](https://github.com/ynagatomo/heychatgpt) - A minimal iOS app that interacts with ChatGPT by your voice.
 * [glowby](https://github.com/glowbom/glowby) - Glowby Basic helps you create your own voice-based AI assistants.
 * [wechatbot](https://github.com/djun/wechatbot) - 为个人微信接入ChatGPT
 * [Discord-Chatbot-Gpt4Free](https://github.com/mishalhossin/discord-chatbot-gpt4free) - This is a Discord Chatbot with image detection for free
 * [big-agi](https://github.com/enricoros/big-agi) - 💬 Personal AI application powered by GPT-4 and beyond, with AI personas, AGI functions, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy and gift #big-AGI-energy! Using Next.js, React, Joy.
 * [RasaGPT](https://github.com/paulpierre/rasagpt) - 💬 RasaGPT is the first headless LLM chatbot platform built on top of Rasa and Langchain. Built w/ Rasa, FastAPI, Langchain, LlamaIndex, SQLModel, pgvector, ngrok, telegram
 * [FigmaChain](https://github.com/cirediatpl/figmachain) - FigmaChain is a set of Python scripts that generate HTML/CSS code based on Figma designs. Using OpenAI's GPT-3 model, FigmaChain enables developers to quickly generate HTML/CSS code from a Figma design input. It also includes a Streamlit-based chatbot interface for interactive code generation.
 * [gpt4free-ts](https://github.com/xiangsx/gpt4free-ts) - This is a replication project for the typescript version of xtekky/gpt4free
 * [slack-gpt](https://github.com/martinseanhunt/slack-gpt) - bot starter that fetches answers to questions using Langchain, OpenAI and a Pincone vectorstore
 * [LLM-As-Chatbot](https://github.com/deep-diver/llm-as-chatbot) - LLM as a Chatbot Service
 * [pdf-chatbot](https://github.com/dissorial/pdf-chatbot) - Analysis of self-tracked data: interactive visualizations & predictive algorithms
 * [ask_chatgpt](https://github.com/railsjazz/ask_chatgpt) - AI-Powered Assistant Gem right in your Rails console. Full power of ChatGPT in Rails
 * [ecoute](https://github.com/sevask/ecoute) - Ecoute is a live transcription tool that provides real-time transcripts for both the user's microphone input (You) and the user's speakers output (Speaker) in a textbox. It also generates a suggested response using OpenAI's GPT-3.5 for the user to say based on the live transcription of the conversation.
 * [privateGPT](https://github.com/samuraigpt/privategpt) - An app to interact privately with your documents using the power of GPT, 100% privately, no data leaks
 * [LLaVA](https://github.com/haotian-liu/llava) - Large Language-and-Vision Assistant built towards multimodal GPT-4 level capabilities.
 * [OpenChat](https://github.com/openchatai/openchat) - Run and create custom ChatGPT-like bots with OpenChat, embed and share these bots anywhere, the open-source chatbot console.
 * [st-chat](https://github.com/ai-yash/st-chat) - Streamlit Component, for a Chatbot UI
 * [summary-gpt-bot](https://github.com/tpai/summary-gpt-bot) - An AI-powered text summarization Telegram bot that generates concise summaries of text, URLs, and YouTube videos.
 * [Bard-API](https://github.com/dsdanielpark/bard-api) - The unofficial python package that returns response of Google Bard through cookie value.
 * [dialoqbase](https://github.com/n4ze3m/dialoqbase) - Create chatbots with ease
 * [Video-ChatGPT](https://github.com/mbzuai-oryx/video-chatgpt) - Video-ChatGPT is a video conversation model capable of generating meaningful conversation about videos. It combines the capabilities of LLMs with a pretrained visual encoder adapted for spatiotemporal video representation.
 * [LLaVA-Med](https://github.com/microsoft/llava-med) - Large Language-and-Vision Assistant for BioMedicine, built towards multimodal GPT-4 level capabilities.
 * [ethgpt](https://github.com/jiayaoqijia/ethgpt) - Chatbot for Ethereum codebase and docs.
 * [telegram-chatgpt-bot](https://github.com/sabber-slt/telegram-chatgpt-bot) - NodeJS-based bot for ChatGPT that runs on Telegram now features advanced capabilities such as voice chat and image generation.
 * [chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot) - 🤖 A Telegram bot that integrates with OpenAI's official ChatGPT APIs to provide answers, written in Python
 * [ai-chatbot](https://github.com/vercel-labs/ai-chatbot) - A full-featured, hackable Next.js AI chatbot built by Vercel Labs
 * [autoclear-chatgpt-history](https://github.com/adamlui/autoclear-chatgpt-history) - 🕶️ Adds chat auto-clear functionality to ChatGPT for more privacy
 * [chatgpt-widescreen](https://github.com/adamlui/chatgpt-widescreen) - 🖥️ Adds Widescreen + Fullscreen modes to ChatGPT for enhanced viewing
 * [chatgpt-infinity](https://github.com/adamlui/chatgpt-infinity) - ∞ Generate endless answers from all-knowing ChatGPT (in any language!)
 * [chatgpt-auto-refresh](https://github.com/adamlui/chatgpt-auto-refresh) - ↻ Keeps ChatGPT sessions fresh to avoid network errors + Cloudflare checks
 * [chatgpt-apps](https://github.com/adamlui/chatgpt-apps) - 🤖 Apps that utilize the astounding power of ChatGPT or enhance its UX
 * [embedchain](https://github.com/embedchain/embedchain) - Framework to easily create LLM powered bots over any dataset.
 * [paper-summarizer](https://github.com/discus0434/paper-summarizer) - A Slack Bot for summarizing arXiv papers, powered by OpenAI LLMs.
 * [vercel-ai-chatbot](https://github.com/supabase-community/vercel-ai-chatbot) - A full-featured, Supabaseified Next.js AI chatbot built by Vercel Labs & Supabase
 * [llm-inference](https://github.com/aniketmaurya/llm-inference) - Large Language Model (LLM) Inference API and Chatbot
 * [GPT4Tools](https://github.com/stevengrove/gpt4tools) - GPT4Tools is an intelligent system that can automatically decide, control, and utilize different visual foundation models, allowing the user to interact with images during a conversation.
 * [Ultimate-ChatGPT](https://github.com/imabutahersiddik/ultimate-chatgpt) - The Ultimate ChatGPT is an AI-powered virtual assistant designed to provide an enhanced writing and problem-solving experience.
 * [wechat-gptbot](https://github.com/iuiaoin/wechat-gptbot) - A wechat robot based on ChatGPT with no risk, very stable! 🚀
 * [FeishuBot](https://github.com/rawchen/feishubot) - 飞书群聊/私聊ChatGPT机器人
 * [gradio-chatbot](https://github.com/weaigc/gradio-chatbot) - A tool that can automatically convert 🤗 Huggingface Spaces,魔搭创空间 and Gradio ChatBot into free APIs. Supports GPT4Free,ChatGPT,Llama2,MPT,Falcon Chat,ChatGLM,通义千问 and many other chatbot like spaces.
 * [ChatGpt-Web](https://github.com/79e/chatgpt-web) - A commercially-viable ChatGpt web application built with React. 使用React搭建的一款可商业化的ChatGpt Web应用。
 * [word-GPT-Plus](https://github.com/kuingsmile/word-gpt-plus) - Word GPT Plus is a word add-in which integrates the chatGPT model into Microsoft Word. Both official and web api is supported.
 * [chat-with-your-doc](https://github.com/linjungz/chat-with-your-doc) - Chat with your docs in PDF/PPTX/DOCX format, using LangChain and GPT4/ChatGPT from both Azure OpenAI Service and OpenAI
 * [OpenAi-ChatGPT-Bot](https://github.com/darkmakerofc/openai-chatgpt-bot) - Open Ai ChatGPT Bot By DarkMakerofc(   Mr  Nima ) & Team , You Can Expirience ChatGPT on Your Whatsapp.
 * [opening-up-chatgpt.github.io](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io) - Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. “Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.” In Proceedings of the 5th International Conference on Conversational User Interfaces. Eindhoven. doi:10.1145/3571884.3604316.
 * [ChatDrug](https://github.com/chao1224/chatdrug) - ChatGPT for Drug Discovery
 * [aks-openai-terraform](https://github.com/azure-samples/aks-openai-terraform) - This article shows how to deploy an Azure Kubernetes Service(AKS) cluster and Azure OpenAI Service via Terraform and how to deploy a Terraform chatbot that authenticates against Azure OpenAI using Azure AD workload identity and calls the Chat Completion API of a ChatGPT model.
 * [Robot-GPT](https://github.com/nonejou072/robot-gpt) - A simulation framework based on ROS2 and ChatGPT for robot interaction tasks in the era of large models
 * [chatgpt-finetune-ui](https://github.com/anchen1011/chatgpt-finetune-ui) - Simple python WebUI for fine-tuning ChatGPT (gpt-3.5-turbo)
 * [poe-api-wrapper](https://github.com/snowby666/poe-api-wrapper) - 👾 A Python API wrapper for Poe.com, using Httpx. With this, you will have free access to ChatGPT, Claude, Llama, Google-PaLM and more! 🚀
 * [llama-gpt](https://github.com/getumbrel/llama-gpt) - A self-hosted, offline, ChatGPT-like chatbot. Powered by Llama 2. 100% private, with no data leaving your device. New: Code Llama support!
 * [rotary-gpt](https://github.com/tcz/rotary-gpt) - I turned my old rotary phone into a ChatGPT-based home assistant and now you can too
 * [rusty_llama](https://github.com/moonkraken/rusty_llama) - A simple ChatGPT clone in Rust on both the frontend and backend. Uses open source language models and TailwindCSS.
 * [GPT_CodeInterpreter](https://github.com/boyueluzhipeng/gpt_codeinterpreter) - Ultimate and FREE OpenAI Provider implemented with Python code interpreter & other multiple functions, powered by ChatGPT & GPT-4!
 * [WebAI-to-API](https://github.com/amm1rr/webai-to-api) - ChatGPT, Claude, Bard to API  : )
 * [chatgpt-minimal](https://github.com/blrchen/chatgpt-minimal) - Lightweight chatgpt bot built using Next.js and the OpenAI Streaming API. 一个使用 Next.js 和 OpenAI Streaming API 创建的简易ChatGPT聊天机器人
 * [open_source_chatgpt_list](https://github.com/sunlemuria/open_source_chatgpt_list) - Open efforts to implement ChatGPT-like models and beyond.
 * [chatgpt-dingtalk-robot](https://github.com/sytpb/chatgpt-dingtalk-robot) - 零代码、一键部署chatgpt到钉钉，无须VPN
 * [chatterstack](https://github.com/dschil138/chatterstack) - Easily manage ChatGPT conversation variables
 * [PokerGPT](https://github.com/matteo-psnt/pokergpt) - PokerGPT Is a Poker Discord Bot that allows you to play Texas Hold'em poker with ChatGPT-4.
 * [kitt](https://github.com/livekit-examples/kitt) - Talk to ChatGPT in real time using LiveKit
 * [compose-chatgpt-kotlin-android-chatbot](https://github.com/lambiengcode/compose-chatgpt-kotlin-android-chatbot) - :lion:Compose ChatGPT Kotlin - Android Chatbot using Kotlin + Jetpack Compose + Coroutine + MVVM + Retrofit2 + OpenAI's GPT-3 API. Allow stream response from ChatGPT API.  Compose ChatGPT Kotlin - 使用 Kotlin + Jetpack Compose + Coroutine + MVVM + Retrofit2 + OpenAI 的 GPT-3 API 的 Android 聊天机器人.允许来自 ChatGPT API 的流响应。🤖
 * [Chino-chan-Bot](https://github.com/misonomikadev/chino-chan-bot) - Bot Messenger được tích hợp ChatGPT.
 * [Chatbase](https://github.com/anil-matcha/chatbase) - ChatGPT for every website.Instantly answer your visitors' questions with a personalized chatbot trained on your website content. Alternative to Chatbase, SiteGPT, Dante AI
 * [plotai](https://github.com/mljar/plotai) - PlotAI - Your Ultimate Plotting Assistant! 📊🤖 Use ChatGPT-3.5 to create plots in Python and Matplotlib directly in your Python script or notebook.
 * [TianMu](https://github.com/openjarvisai/tianmu) - TianMu: A modern AI tool with multi-platform support, markdown support, multimodal, continuous conversation, and customizable commands. 一个APP支持文心一言、通义千问、LLaMa、ChatGPT等，开源的大模型客户端！
 * [youtube-summarizer](https://github.com/sabber-slt/youtube-summarizer) - Telegram bot designed to summaries youtube video contents with ChatGPT.
 * [ChatGPT-Nuxt](https://github.com/hylarucoder/chatgpt-nuxt) - ChatGPT Web Nuxt 3  Vue 3 Version
 * [FirewaLLM](https://github.com/ysy1216/firewallm) - By calling FirewaLLM, users can ensure the accuracy of the large model while greatly reducing the risk of privacy leakage when interacting with it. We believe that FirewallLLM is a privacy protected chatgpt interaction platform.
 * [Langchain-Chatchat](https://github.com/chatchat-space/langchain-chatchat) - Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM 等语言模型的本地知识库问答 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM) QA app with langchain
 * [wukong-robot](https://github.com/wzpan/wukong-robot) - 🤖 wukong-robot 是一个简单、灵活、优雅的中文语音对话机器人/智能音箱项目，支持ChatGPT多轮对话能力，还可能是首个支持脑机交互的开源智能音箱项目。
 * [autogen](https://github.com/microsoft/autogen) - Enable Next-Gen Large Language Model Applications. Join our Discord: https://discord.gg/pAbnFJrkgZ
 * [GPTDiscord](https://github.com/kav-k/gptdiscord) - A robust, all-in-one GPT interface for Discord. ChatGPT-style conversations, image generation, AI-moderation, custom indexes/knowledgebase, youtube summarizer, and more!
 * [BotSharp](https://github.com/scisharp/botsharp) - The AI Agent Application Framework in .NET
 * [anything-llm](https://github.com/mintplex-labs/anything-llm) - Open-source ChatGPT equivalent experience for both open and close source LLMs, embedders, and vector databases. Supports unlimited documents, threads, and concurrent users and management all in a very clean UI.
 * [magic](https://github.com/polterguy/magic) - Create a custom ChatGPT-based website chatbot
 * [rags](https://github.com/run-llama/rags) - Build ChatGPT over your data, all with natural language
 * [LLamaSharp](https://github.com/scisharp/llamasharp) - Run LLaMA/GPT model easily and fast in C#!🤗 It's also easy to integrate LLamaSharp with semantic-kernel, unity, WPF and WebApp.
 * [Open-Custom-GPT](https://github.com/samuraigpt/open-custom-gpt) - Create Custom GPT and add/embed on your site using Assistants api
 * [wechat-ai-summarize-bot](https://github.com/aoao-eth/wechat-ai-summarize-bot) - 微信群聊总结助手 JS 版
 * [webwhiz](https://github.com/webwhiz-ai/webwhiz) - WebWhiz allows you to create an AI chatbot that knows everything about your product and can instantly respond to your customer's queries.
 * [deep-chat](https://github.com/ovidijusparsiunas/deep-chat) - Fully customizable AI chatbot component for your website
 * [WeChatFerry](https://github.com/lich0821/wechatferry) - 微信逆向，微信机器人，可接入 ChatGPT、ChatGLM、讯飞星火、Tigerbot等大模型。Hook WeChat.
 * [mPLUG-Owl](https://github.com/x-plug/mplug-owl) - [Official Implementation] mPLUG-Owl & mPLUG-Owl2: Alibaba MLLM Family.
 * [AstrBot](https://github.com/soulter/astrbot) - ⭐ QQ和QQ频道都可用的 ChatGPT, Bing, Claude, HuggingChat 机器人，支持插件 | 原 QQChannelChatGPT
 * [casibase](https://github.com/casibase/casibase) - ⚡️Open-source LangChain-like AI knowledge database with web UI,and Enterprise SSO⚡️, supports OpenAI, AI/ML API, Azure, HuggingFace, OpenRouter, ChatGLM and local models, chat demo: https://ai.casbin.com, admin portal demo: https://ai.casibase.com
 * [ai-chatbot](https://github.com/vercel/ai-chatbot) - A full-featured, hackable Next.js AI chatbot built by Vercel
 * [ChatPDF](https://github.com/anil-matcha/chatpdf) - Chat with any PDF. Easily upload the PDF documents you'd like to chat with. Instant answers. Ask questions, extract information, and summarize documents with AI. Sources included.
 * [OpenAssistantGPT](https://github.com/marcolivierbouch/openassistantgpt) - An open source platform for building chatbot using the OpenAI API Assistant.
 * [ai-research-assistant](https://github.com/lifan0127/ai-research-assistant) - Aria is Your AI Research Assistant Powered by GPT Large Language Models
 * [aidea](https://github.com/mylxsw/aidea) - AIdea 是一款支持 GPT  以及国产大语言模型通义千问、文心一言等，支持 Stable Diffusion 文生图、图生图、 SDXL1.0、超分辨率、图片上色的全能型 APP。
 * [ChatGPT-weBot](https://github.com/snapdragonlee/chatgpt-webot) - Chat with ChatGPT (gpt-3.5 or newer)，WeChat hook interface based
 * [vbot](https://github.com/hanson/vbot) - 微信，企微，机器人，企业微信，企微机器人，微信机器人，聚合聊天，RPA，协议，hook，逆向，worktool，ntwork，群发，自动回复，chatgpt，API对接，稳定防封全语言通用，企业定制/SCRM/SAAS专用
 * [org-ai](https://github.com/rksm/org-ai) - output.
 * [Linly](https://github.com/cvi-szu/linly) - Chinese-LLaMA 1&2、Chinese-Falcon 基础模型；ChatFlow中文对话模型；中文OpenLLaMA模型；NLP预训练/指令微调数据集
 * [gpt-ai-assistant](https://github.com/memochou1993/gpt-ai-assistant) - OpenAI + LINE + Vercel = GPT AI Assistant
 * [TS-GPT](https://github.com/dulaiduwang003/ts-gpt) - Dual-ended GPT application developed based on SpringCloudAlibaba, including voice dialogue, drawing, image recognition, and text dialogue
 * [ChatGPT-YourChatRobot](https://github.com/ashinnotfound/chatgpt-yourchatrobot) - ❤开箱即用❤an unofficial implement of ChatGPT in QQ/Wechat. 一个非官方的ChatGPT腾讯qq/微信(非公众号)实现版，快来把你的qq或微信变成chatgpt吧
 * [wechat-bot](https://github.com/wangrongding/wechat-bot) - 🤖一个基于OpenAi  ChatGPT + WeChaty 实现的微信机器人 ，可以用来帮助你自动回复微信消息，或者管理微信群/好友，检测僵尸粉等...
 * [ChatFred](https://github.com/chrislemke/chatfred) - Alfred workflow using ChatGPT, DALL·E 2 and other models for chatting, image generation and more.
 * [catai](https://github.com/withcatai/catai) - UI for 🦙model . Run AI assistant locally ✨
 * [ChatGPT-Telegram-Bot](https://github.com/yym68686/chatgpt-telegram-bot) - 🤖️ an AI chat Telegram bot can Web Search Powered by GPT and Claude2.1 using Python on Zeabur, fly.io and Replit.
 * [bidara](https://github.com/nasa-petal/bidara) - BIDARA is a GPT-4 chatbot that was instructed to help scientists and engineers understand, learn from, and emulate the strategies used by living things to create sustainable designs and technologies using the Biomimicry Institute's step-by-step design process.
 * [sagittarius](https://github.com/gregsadetsky/sagittarius) - A GPT-4/Gemini Voice/Video Exploration Tool
 * [Chat-with-Github-Repo](https://github.com/peterw/chat-with-github-repo) - This repository contains two Python scripts that demonstrate how to create a chatbot using Streamlit, OpenAI GPT-3.5-turbo, and Activeloop's Deep Lake.
 * [pandas-ai](https://github.com/gventuri/pandas-ai) - 4, Anthropic, VertexAI) and RAG.
 * [chatgpt-mirai-qq-bot](https://github.com/lss233/chatgpt-mirai-qq-bot) - 🚀 一键部署！真正的 AI 聊天机器人！支持ChatGPT、文心一言、讯飞星火、Bing、Bard、ChatGLM、POE，多账号，人设调教，虚拟女仆、图片渲染、语音发送 | 支持 QQ、Telegram、Discord、微信 等平台
 * [quivr](https://github.com/quivrhq/quivr) - 4 turbo, Private, Anthropic, VertexAI, Ollama, LLMs, that you can share with users !  Local & Private alternative to OpenAI GPTs & ChatGPT powered by retrieval-augmented generation.
 * [smalltalk](https://github.com/tinystruct/smalltalk) - ChatGPT. @tinystruct
 * [maid](https://github.com/mobile-artificial-intelligence/maid) - llama.cpp models locally, and with Ollama and OpenAI models remotely.
 * [pandas-ai](https://github.com/sinaptik-ai/pandas-ai) - 4, Anthropic, VertexAI) and RAG.
 * [WeChatRobot](https://github.com/lich0821/wechatrobot) - 微信机器人，接入Google Bard、ChatGPT、ChatGLM、讯飞星火、Tigerbot；成语接龙、天气预报、新闻摘要。
 * [chatgptassistantautoblogger](https://github.com/incomestreamsurfer/chatgptassistantautoblogger) - This autoblogger uses the GPT assistant's API to autoblog on ecommerce websites
 * [chaty](https://github.com/cosin2077/chaty) - one line code, satisfied all your ChatGPT imagination✨✨✨
 * [wechat-assistant-pro](https://github.com/leochen-g/wechat-assistant-pro) - 智能微秘书，一个全能的微信机器人管理平台，最简单的方式接入 ChatGPT，FastGPT，Dify知识库，支持绘图，联网查询，语音识别，各种定时任务，支持企微、个微、公众号、5G 消息、WhatsApp
 * [ChatGPT-Telegram-Bot](https://github.com/v-know/chatgpt-telegram-bot) - A Telegram bot with a smooth AI experience.
 * [nlux](https://github.com/nluxai/nlux) - Javascript Library To Build Conversational AI Interfaces
 * [ChatGPT-Line-Bot](https://github.com/theexplainthis/chatgpt-line-bot) - This is a repository that allows you to integrate ChatGPT into Line.
 * [langup-ai](https://github.com/jiran214/langup-ai) - AGI 社交网络 Bot.  BiliBili |  直播聊天数字人 | 视频@自动回复 | 私信bot | 终端聊天  |  语音交互
 * [customizable-gpt-chatbot](https://github.com/shamspias/customizable-gpt-chatbot) - A dynamic, scalable AI chatbot built with Django REST framework, supporting custom training from PDFs, documents, websites, and YouTube videos. Leveraging OpenAI's GPT-3.5, Pinecone, FAISS, and Celery for seamless integration and performance.
 * [DarkGPT](https://github.com/luijait/darkgpt) - DarkGPT is an OSINT assistant based on GPT-4-200K (recommended use) designed to perform queries on leaked databases, thus providing an artificial intelligence assistant that can be useful in your traditional OSINT processes.
 * [Kuebiko](https://github.com/adi-panda/kuebiko) - An AI Twitch TTS Chat Bot using GPT-3 and Google Cloud TTS
 * [AI-Catalog](https://github.com/mehmetkahya0/ai-catalog) - Huge AI models catalog. A curated list of AI tools, platforms, and resources across various domains.
 * [Multi-Modality-Arena](https://github.com/opengvlab/multi-modality-arena) - Chatbot Arena meets multi-modality! Multi-Modality Arena allows you to benchmark vision-language models side-by-side while providing images as inputs. Supports MiniGPT-4, LLaMA-Adapter V2, LLaVA, BLIP-2, and many more!
 * [chatbot](https://github.com/zhaoyingjun/chatbot) - ChatGPT带火了聊天机器人，主流的趋势都调整到了GPT类模式，本项目也与时俱进，会在近期更新GPT类版本。基于本项目和自己的语料可以训练出自己想要的聊天机器人，用于智能客服、在线问答、闲聊等场景。
 * [WechatBotCMD](https://github.com/wechatapis/wechatbotcmd) - 微信机器人WechatBotCMD是一个创新的基于Python 3.11开发的项目，通过结合ChatGPT模型和微信原生API，为用户提供智能聊天、自动绘画、自动发朋友圈、自动发视频号等多样的API集成服务，旨在提升日常沟通效率和趣味性。
 * [ChatGPT-On-CS](https://github.com/lrhh123/chatgpt-on-cs) - 基于大模型的智能对话客服工具，支持微信、千牛、哔哩哔哩、抖音企业号、抖音、抖店、微博聊天、小红书专业号运营、小红书、知乎等平台接入，可选择 GPT3.5/GPT4.0/ 懒人百宝箱 （后续会支持更多平台），能处理文本、语音和图片，通过插件访问操作系统和互联网等外部资源，支持基于自有知识库定制企业 AI 应用。
 * [agentcloud](https://github.com/rnadigital/agentcloud) - Agent Cloud is like having your own GPT builder with a bunch extra goodies. The GUI features 1) RAG pipeline which can natively embed 260+ datasources 2) Create Conversational apps (like GPTs) 3) Create Multi Agent process automation apps (crewai) 4) Tools 5) Teams+user permissions. Get started fast with Docker and our install.sh
 * [openlrc](https://github.com/zh-plus/openlrc) - Transcribe and translate voice into LRC file using Whisper and LLMs (GPT, Claude, et,al). 使用whisper和LLM(GPT，Claude等)来转录、翻译你的音频为字幕文件。
 * [wrest-chat](https://github.com/opentdp/wrest-chat) - 微信机器人，PC Wechat Api/Bot/Sdk，内置 WEB 管理界面，可接入GPT、Gemini 、星火、文心、混元 、通义千问等大语言模型
 * [chatbot-app](https://github.com/chatbot-all/chatbot-app) - mobile private ChatGPT application, supporting GPT3, GPT4 & Gemini Pro models.  拥有自己的移动端 ChatGPT/Gemini 应用。
 * [ChatGPT-On-CS](https://github.com/cs-lazy-tools/chatgpt-on-cs) - 基于大模型的智能对话客服工具，支持微信、千牛、哔哩哔哩、抖音企业号、抖音、抖店、微博聊天、小红书专业号运营、小红书、知乎等平台接入，可选择 GPT3.5/GPT4.0/ 懒人百宝箱 （后续会支持更多平台），能处理文本、语音和图片，通过插件访问操作系统和互联网等外部资源，支持基于自有知识库定制企业 AI 应用。
 * [MOSS](https://github.com/openmoss/moss) - An open-source tool-augmented conversational language model from Fudan University
 * [Wa-OpenAI](https://github.com/sansekai/wa-openai) - WhatsApp Bot OpenAI ChatGPT NodeJS Using Library Baileys
 * [gpt-assistant-android](https://github.com/skythinker616/gpt-assistant-android) - 免费的ChatGPT API的安卓语音助手，可用音量键唤起并进行语音交流，支持联网、Vision拍照识图、提问模板等功能 | A free ChatGPT API voice assistant for Android, activated via volume keys for voice interaction, supporting features such as network connectivity, Vision photo recognition, and question templates.
 * [gpt-home](https://github.com/judahpaul16/gpt-home) - ChatGPT at home! Basically a better Google Nest Hub or Amazon Alexa home assistant. Built on the Raspberry Pi using the OpenAI API.
 * [gpt-computer-assistant](https://github.com/onuratakan/gpt-computer-assistant) - gpt-4o for windows, macos and ubuntu
 * [nlux](https://github.com/nlkitai/nlux) - The 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 Conversational AI JavaScript Library
 * [Streamer-Sales](https://github.com/peterh0323/streamer-sales) - Streamer-Sales 销冠 —— 卖货主播 LLM 大模型🛒🎁，一个能够根据给定的商品特点对商品进行解说并激发用户的购买意愿的卖货主播模型。🚀⭐内含详细的数据生成流程❗ 📦另外还集成了 LMDeploy 加速推理🚀、RAG检索增强生成 📚、TTS文字转语音🔊
 * [Chatbase-Alternative](https://github.com/anil-matcha/chatbase-alternative) - ChatGPT for every website.Instantly answer your visitors' questions with a personalized chatbot trained on your website content. Alternative to Chatbase, SiteGPT, Dante AI
 * [speak-gpt](https://github.com/andraxdev/speak-gpt) - Your personal voice assistant based on OpenAI ChatGPT.
 * [IncarnaMind](https://github.com/junruxiong/incarnamind) - Connect and chat with your multiple documents (pdf and txt) through GPT 3.5, GPT-4 Turbo, Claude and Local Open-Source LLMs
 * [unsaged](https://github.com/jorge-menjivar/unsaged) - Open source chat kit engineered for seamless interaction with AI models.
 * [discord-llm-chatbot](https://github.com/jakobdylanc/discord-llm-chatbot) - llmcord.py • Talk to LLMs with your friends!
 * [Instruct2Act](https://github.com/opengvlab/instruct2act) - Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model
 * [GURU-Ai](https://github.com/guru322/guru-ai) - A SIMPLE YET COMPLICATED AI Chat Robot LOADED WITH FEATURES🚩
 * [voxelgpt](https://github.com/voxel51/voxelgpt) - AI assistant that can query visual datasets, search the FiftyOne docs, and answer general computer vision questions
 * [XYBot](https://github.com/henryxiaoyang/xybot) - 基于docker和pywxdll hook注入的微信机器人🤖️！✅高度可自定义！ ✅支持自我编写插件！非常多的功能：天气🌤️、获取新闻📰、ChatGPT聊天🗣️、Hypixel玩家查询🎮、随机图片📷、随机链接🔗、随机群成员👥、五子棋♟️、签到✅、查询积分📊、积分榜🏆、积分转送💰、积分抽奖🎁、积分红包🧧等
 * [GPTPortal](https://github.com/zaki-1052/gptportal) - A feature-rich portal to chat with GPT-4, Claude, Gemini, Mistral, & OpenAI Assistant APIs via a lightweight Node.js web app; supports customizable multimodality for