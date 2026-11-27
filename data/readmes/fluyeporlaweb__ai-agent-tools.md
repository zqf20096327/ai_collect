<p align="center"><img src=".github/assets/logo.png" width="128" alt="ai-agent-tools logo"></p>

# Agent Tools

**A curated directory of open-source AI agent tools** for marketing and technical growth teams: **agent frameworks**, **coding agents and CLIs**, **MCP servers and clients**, browser automation and sandboxes, memory and RAG, observability, and **prospecting and SEO workflows**. Built and maintained by [fluyeporlaweb](https://fluyeporlaweb.com). Every link is checked; entries are chosen, not dumped.

English · [Español](README.es.md)

[![GitHub stars](https://img.shields.io/github/stars/fluyeporlaweb/ai-agent-tools?style=flat)](https://github.com/fluyeporlaweb/ai-agent-tools/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Links checked weekly](https://img.shields.io/badge/links-checked%20weekly-blue.svg)](.github/workflows/link-check.yml)

## Contents

- [What this is](#what-this-is)
- [Protocols and standards](#protocols-and-standards) (8)
- [Agent frameworks and SDKs](#agent-frameworks-and-sdks) (34)
- [Coding agents and IDEs](#coding-agents-and-ides) (28)
- [MCP SDKs, registry and tooling](#mcp-sdks-registry-and-tooling) (18)
- [MCP servers](#mcp-servers) (38)
- [MCP clients and hosts](#mcp-clients-and-hosts) (12)
- [Browser, computer use and sandboxes](#browser-computer-use-and-sandboxes) (24)
- [Data, scraping and search APIs](#data-scraping-and-search-apis) (14)
- [Memory, RAG and vector stores](#memory-rag-and-vector-stores) (19)
- [Observability, evals and tracing](#observability-evals-and-tracing) (16)
- [LLM APIs, routers and runtimes](#llm-apis-routers-and-runtimes) (27)
- [Workflow and orchestration](#workflow-and-orchestration) (14)
- [Voice, speech and realtime](#voice-speech-and-realtime) (15)
- [Guardrails and safety](#guardrails-and-safety) (12)
- [Agent skills and tool marketplaces](#agent-skills-and-tool-marketplaces) (13)
- [Marketing, SEO and prospecting](#marketing-seo-and-prospecting) (10)
- [Built by fluyeporlaweb](#built-by-fluyeporlaweb) (2)
- [Sponsors](#sponsors)
- [Related lists](#related-lists)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## What this is

This is a curated awesome list of **open-source AI agent tools for marketing and growth teams**: frameworks and SDKs, coding agents, MCP servers and clients, browser and sandbox runtimes, data and search APIs, memory and RAG, observability, LLM gateways, workflows, voice, guardrails, agent skills, and prospecting / SEO tools.

It is not a dump of every repo with “agent” in the name. Each entry has a one-line description and a working link. We also keep a small section for tools [built by fluyeporlaweb](#built-by-fluyeporlaweb).

Some entries use [affiliate links](https://fluyeporlaweb.com/legal/afiliacion/) that go through `fluyeporlaweb.com/go/`. They are marked with *affiliate*. You pay the same price. See [Sponsors](#sponsors) if you want your brand on this list.

## Protocols and standards

- [Model Context Protocol](https://modelcontextprotocol.io) - Open standard that lets AI apps talk to tools, data sources and services through a common interface.
- [MCP specification](https://github.com/modelcontextprotocol/modelcontextprotocol) - Official MCP specification and protocol documentation, maintained by the MCP steering group.
- [Agent Skills](https://agentskills.io) - Open format for packaging reusable instructions and scripts that coding agents can load into a repo.
- [Agent2Agent (A2A)](https://a2a-protocol.org) - Open protocol, started at Google, for agents from different vendors to discover each other and collaborate.
- [AG-UI](https://docs.ag-ui.com) - Open protocol for connecting agent backends to user-facing applications with a standard event stream.
- [llms.txt](https://llmstxt.org) - A proposed standard for a /llms.txt file that tells language models how to read a site or project.
- [OpenTelemetry GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - Semantic conventions for tracing generative AI and agent applications with OpenTelemetry.
- [Agent Communication Protocol (ACP)](https://agentcommunicationprotocol.dev) - Open protocol that lets agents discover and talk to each other through a shared message format (`Open Source`).

## Agent frameworks and SDKs

- [LangChain](https://www.langchain.com) - Widely used framework for composing LLM apps, tools and agents in Python and JavaScript.
- [LangGraph](https://www.langchain.com/langgraph) - Low-level orchestration framework for durable, stateful agents with cycles, persistence and human-in-the-loop.
- [LlamaIndex](https://www.llamaindex.ai) - Framework for connecting LLMs to your data, with agents, workflows and a strong RAG toolkit.
- [CrewAI](https://www.crewai.com) - Python framework for multi-agent crews with roles, tasks and a workflow engine.
- [AutoGen](https://microsoft.github.io/autogen/) - Microsoft's multi-agent framework for event-driven, conversable agents, now part of the Agent Framework line.
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) - Microsoft's unified SDK for building and running multi-agent systems in .NET and Python, documented on Microsoft Learn.
- [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/) - Microsoft SDK that embeds AI agents and plugins into C#, Python and Java applications.
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) - Official OpenAI SDK for building agents with tools, handoffs, guardrails and tracing.
- [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) - Google's code-first toolkit for building, evaluating and deploying agents, including on Vertex AI.
- [PydanticAI](https://ai.pydantic.dev) - Type-safe Python agent framework from the Pydantic team, with structured I/O and model-agnostic tooling.
- [Agno](https://github.com/agno-agi/agno) - Fast Python framework for agents with built-in memory, knowledge, tools and a reasoning loop.
- [Haystack](https://haystack.deepset.ai) - Open-source framework by deepset for RAG pipelines and tool-using agents, with a visual pipeline editor.
- [Mastra](https://mastra.ai) - TypeScript framework for agents, workflows and RAG, with evals and a local playground.
- [VoltAgent](https://voltagent.dev) - TypeScript framework for building and orchestrating AI agents, with memory, tools and observability.
- [smolagents](https://github.com/huggingface/smolagents) - Hugging Face's minimal Python library for agents that write and run code to use tools.
- [Letta](https://www.letta.com) - Framework and platform for agents with long-term memory, born from the MemGPT research.
- [Dify](https://dify.ai) - Open-source platform to build and operate LLM apps and agents, with a visual studio and RAG pipeline.
- [Langflow](https://www.langflow.org) - Open-source visual IDE for building agents and RAG flows, from the LangChain ecosystem.
- [Vercel AI SDK](https://ai-sdk.dev) - TypeScript toolkit for streaming AI UIs and agents across many model providers.
- [Spring AI](https://docs.spring.io/spring-ai/reference/) - Spring project's API for building AI applications and agents in Java, with portable model and tool support.
- [Strands Agents](https://github.com/strands-agents/sdk-python) - AWS's model-driven open-source SDK for building and deploying AI agents.
- [DSPy](https://dspy.ai) - Framework for programming—not prompting—LMs, with optimizable signatures that agents can use as modules.
- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) - Anthropic's SDK for building agents with Claude, tools and the same harness used by Claude Code.
- [Google Gen AI SDK](https://ai.google.dev) - Official Google SDK for Gemini, including function calling, thinking and live/multimodal APIs.
- [AstrBot](https://github.com/AstrBotDevs/AstrBot) - Open-source framework for AI assistants that plug into messaging platforms such as Telegram and Discord, with LLMs and plugins.
- [learnharness](https://github.com/amosblomqvist/learnharness) - An agent harness built for learning difficult topics, with an agent-native loop rather than a static tutor.
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) - Multi-agent LLM framework that models a trading desk, with agents that debate and analyse financial markets.
- [CopilotKit](https://www.copilotkit.ai) - SDK for adding AI copilots to apps, with hooks and UI components for in-app assistant flows (`Open Source`).
- [Flowise](https://flowiseai.com) - Visual builder for assembling LLM chains and agents from connected nodes, useful for quick prototypes (`Open Source`).
- [CAMEL](https://www.camel-ai.org) - Framework for multi-agent research and role-playing scenarios, used to study how agents cooperate on tasks (`Open Source`).
- [Langroid](https://langroid.github.io/langroid/) - Framework that turns LLM interactions into task-oriented agents with message passing and tool use (`Open Source`).
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - Library for building agents that compose MCP servers and tools with a clear orchestration model (`Open Source`).
- [Suna](https://github.com/kortix-ai/suna) - Open generalist agent that handles research, data and browser tasks from a conversation (`Open Source`).
- [BeeAI Framework](https://github.com/i-am-bee/bee-agent-framework) - Framework for building and running multi-agent workflows with portable agents and tooling (`Open Source`).

## Coding agents and IDEs

- [Claude Code](https://code.claude.com/docs/en/overview) - Anthropic's terminal-first coding agent, with MCP support, skills and repo-aware workflows.
- [Cursor](https://cursor.com) - AI-native code editor with agent mode, repo context, MCP support and inline edits.
- [GitHub Copilot](https://github.com/features/copilot) - GitHub's coding assistant and agent, available in VS Code, Visual Studio, the CLI and on github.com.
- [Windsurf](https://windsurf.com) - Codeium's agentic IDE with cascade flows, MCP support and deep repo context.
- [Aider](https://aider.chat) - Open-source terminal coding agent that edits your repo, commits and works with many LLMs.
- [Continue](https://www.continue.dev) - Open-source coding assistant and agent for VS Code and JetBrains, with MCP and customizable context.
- [Cline](https://github.com/cline/cline) - Open-source coding agent for VS Code that can use the browser, terminal and MCP tools.
- [OpenCode](https://opencode.ai) - Open-source terminal coding agent that works with many model providers, including local ones.
- [Goose](https://block.github.io/goose/) - Block's open-source, local-first coding and operations agent, with an extensible tool and MCP ecosystem.
- [Codex](https://openai.com/codex/) - OpenAI's coding agent, available as a CLI, IDE extension and in ChatGPT.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's open-source command-line agent for Gemini, with MCP support and built-in tools.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Open-source software-dev agent (formerly OpenDevin) that can edit code, run commands and browse.
- [Roo Code](https://github.com/RooCodeInc/Roo-Code) - Open-source VS Code coding agent (a Cline fork) with modes, MCP and a strong community.
- [Sourcegraph Amp](https://sourcegraph.com/amp) - Sourcegraph's coding agent, built on the same code intelligence that powers Cody and search.
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - AWS coding assistant and agent for the IDE, CLI and console, with AWS-aware tools.
- [Zed](https://zed.dev) - Fast open-source editor with an agent panel and MCP client support.
- [Warp](https://www.warp.dev) - Agentic terminal that can run workflows, edit commands and use MCP servers.
- [Grok Bot](https://grok.com) - Coding and operations agent from xAI that can use tools, browse and work across connected apps.
- [Devin](https://devin.ai) - Cognition's autonomous software engineer: a cloud agent that plans, codes and opens pull requests.
- [Augment Code](https://www.augmentcode.com) - Coding agent and context engine built for large codebases, with IDE and Slack integrations.
- [t3code](https://github.com/pingdotgg/t3code) - Remote control for Claude Code, Codex and other coding agents, so you can steer them from any computer or phone.
- [Crush](https://github.com/charmbracelet/crush) - Terminal coding agent that edits files, runs commands and helps with repository work from the CLI (`Open Source`).
- [Tabby](https://tabby.tabbyml.com) - Self-hosted code assistant that completes and explains code inside your editor while you work (`Open Source`).
- [Void](https://voideditor.com) - Open-source editor built around AI-assisted coding, with chat and inline edits in the same workspace (`Open Source`).
- [Qwen Code](https://github.com/QwenLM/qwen-code) - Command-line coding agent that reads a repository and helps implement changes with model assistance (`Open Source`).
- [JetBrains AI](https://www.jetbrains.com/ai/) - AI assistance built into JetBrains IDEs for code completion, refactoring and in-editor chat (`Freemium`).
- [Factory](https://factory.ai) - AI coding workspace where agents handle software tasks from a shared interface and repo context (`Freemium`).
- [Plandex](https://github.com/plandex-ai/plandex) - Coding agent that plans multi-file changes and applies them with reviewable steps in the terminal (`Open Source`).

## MCP SDKs, registry and tooling

- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Official TypeScript SDK for building MCP servers and clients.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK for building MCP servers and clients.
- [MCP Go SDK](https://github.com/modelcontextprotocol/go-sdk) - Official Go SDK for MCP servers and clients, maintained with Google.
- [MCP Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Official Java SDK for MCP, maintained with the Spring AI team.
- [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Official Rust SDK for the Model Context Protocol.
- [MCP C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Official C# SDK for MCP servers and clients, in collaboration with Microsoft.
- [MCP Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Official Kotlin SDK for MCP, maintained with JetBrains.
- [MCP PHP SDK](https://github.com/modelcontextprotocol/php-sdk) - Official PHP SDK for MCP, maintained with The PHP Foundation.
- [MCP Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Official Swift SDK for MCP, maintained with Apple.
- [MCP Ruby SDK](https://github.com/modelcontextprotocol/ruby-sdk) - Official Ruby SDK for MCP servers and clients.
- [FastMCP](https://github.com/jlowin/fastmcp) - High-level Python (and TypeScript) framework for writing MCP servers with minimal boilerplate.
- [MCP Registry](https://github.com/modelcontextprotocol/registry) - Official community registry service for discovering and publishing MCP servers.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) - Official visual tool for testing and debugging MCP servers.
- [MCPB](https://github.com/modelcontextprotocol/mcpb) - Desktop Extensions format for packaging and one-click installing MCP servers in desktop apps.
- [Reference MCP servers](https://github.com/modelcontextprotocol/servers) - Official monorepo of reference MCP servers (filesystem, memory, everything, and more).
- [Smithery](https://smithery.ai) - Registry and tooling for finding and running MCP servers with consistent configuration (`Freemium`).
- [PulseMCP](https://www.pulsemcp.com) - Directory of MCP servers and clients that helps discover integrations and follow ecosystem changes (`Free`).
- [Glama MCP](https://glama.ai/mcp) - Catalog of MCP servers with reviews and details, useful for comparing available integrations (`Free`).

## MCP servers

- [GitHub MCP Server](https://github.com/github/github-mcp-server) - Official GitHub MCP server for repos, issues, pull requests and Actions.
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - Microsoft's official MCP server that lets agents browse and automate pages with Playwright.
- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) - Official Cloudflare MCP server for Workers, KV, R2, D1, Observability and more.
- [Stripe Agent Toolkit](https://github.com/stripe/agent-toolkit) - Official Stripe toolkit with MCP and other agent integrations for payments.
- [Notion MCP](https://github.com/makenotion/notion-mcp-server) - Official Notion MCP server for reading and writing Notion pages and databases.
- [Linear MCP](https://linear.app/docs/mcp) - Official Linear MCP server for issues, projects and team workflows.
- [Sentry MCP](https://github.com/getsentry/sentry-mcp) - Official Sentry MCP server so agents can inspect errors, issues and traces.
- [Supabase MCP](https://github.com/supabase-community/supabase-mcp) - Official Supabase MCP server for projects, database, auth and edge functions.
- [Prisma MCP](https://www.prisma.io/mcp) - Prisma MCP server for talking to Prisma Postgres and your schema from an agent.
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) - Official Chrome DevTools MCP server for inspecting and debugging live pages.
- [Browserbase MCP](https://github.com/browserbase/mcp-server-browserbase) - MCP server that gives agents a cloud browser via Browserbase and Stagehand.
- [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) - MCP server for crawling, scraping and searching the web with Firecrawl.
- [Context7](https://fluyeporlaweb.com/go/context-dev/?p=github-readme) - MCP server that pulls up-to-date, version-specific library docs into your coding agent. *(affiliate)*
- [Apify MCP](https://fluyeporlaweb.com/go/apify/?p=github-readme) - Official way to run Apify Actors and tools from MCP-compatible agents. *(affiliate)*
- [Zernio MCP](https://fluyeporlaweb.com/go/zernio/?p=github-readme) - Hosted MCP server to schedule, publish and manage social and messaging accounts from an agent. *(affiliate)*
- [Monid](https://fluyeporlaweb.com/go/monid/?p=github-readme) - Gateway of 2,800+ tools for agents (they call it “OpenRouter for agent tools”), with MCP, a skill and a CLI. *(affiliate)*
- [Atlassian MCP](https://www.atlassian.com/platform/remote-mcp-server) - Official Atlassian remote MCP server for Jira and Confluence.
- [Figma MCP](https://developers.figma.com/docs/figma-mcp-server/) - Figma's official MCP integration so agents can read design context from files.
- [MongoDB MCP](https://github.com/mongodb-js/mongodb-mcp-server) - Official MongoDB MCP server for querying and managing clusters.
- [Neon MCP](https://neon.tech/docs/ai/neon-mcp-server) - Official Neon MCP server for managing serverless Postgres from an agent.
- [Hugging Face MCP](https://huggingface.co/settings/mcp) - Official Hugging Face MCP server for models, datasets, Spaces and papers.
- [Slack MCP](https://docs.slack.dev/ai/slack-mcp-server/) - Official Slack MCP server for searching and posting in workspaces.
- [Zapier MCP](https://zapier.com/mcp) - Zapier MCP that exposes thousands of app actions as tools for agents.
- [n8n MCP](https://docs.n8n.io/advanced-ai/accessing-n8n-mcp-server/) - Official n8n MCP server so agents can search, run and build workflows.
- [Exa MCP](https://github.com/exa-labs/exa-mcp-server) - MCP server for Exa's neural web search and contents API.
- [Tavily MCP](https://docs.tavily.com/documentation/mcp) - MCP server for Tavily's search and extract APIs, built for agents.
- [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) - Official Brave Search MCP server for web, image, news and video search.
- [Qdrant MCP](https://github.com/qdrant/mcp-server-qdrant) - Official Qdrant MCP server for storing and retrieving semantic memories.
- [AWS MCP Servers](https://github.com/awslabs/mcp) - Collection of MCP servers that connect agents to AWS services and infrastructure workflows (`Open Source`).
- [Terraform MCP Server](https://github.com/hashicorp/terraform-mcp-server) - MCP server that lets agents work with Terraform configurations and infrastructure definitions (`Open Source`).
- [Redis MCP](https://github.com/redis/mcp-redis) - MCP server that gives agents access to Redis for caching, keys and data operations (`Open Source`).
- [Pipedream MCP](https://mcp.pipedream.com) - MCP interface to app integrations so agents can trigger actions across connected SaaS tools (`Freemium`).
- [Serena](https://github.com/oraios/serena) - MCP server that gives coding agents semantic awareness of a codebase through language servers (`Open Source`).
- [Browser MCP](https://browsermcp.io) - MCP server that lets agents drive a real browser for clicking, filling forms and reading pages (`Open Source`).
- [21st.dev Magic MCP](https://21st.dev/magic) - MCP server that supplies UI components and design snippets to coding agents on request (`Freemium`).
- [PostgreSQL MCP](https://github.com/crystaldba/postgres-mcp) - MCP server that lets agents query and inspect PostgreSQL databases through a defined set of tools (`Open Source`).
- [Microsoft MCP servers](https://github.com/microsoft/mcp) - Microsoft's MCP servers for connecting agents to products, documentation and developer services (`Open Source`).
- [Docker MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) - Curated catalog of MCP servers distributed through Docker for easy setup and consistent runs (`Open Source`).

## MCP clients and hosts

- [Claude Desktop](https://claude.ai/download) - Anthropic's desktop app, one of the first MCP hosts, with local and remote server support.
- [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) - Visual Studio Code MCP host, used by GitHub Copilot and other chat agents.
- [LibreChat](https://www.librechat.ai) - Open-source ChatGPT-style UI with MCP, agents, and many model providers.
- [Open WebUI](https://openwebui.com) - Self-hosted web UI for local and remote models, with MCP and tool support.
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - Open-source desktop client for many LLM providers, with MCP support.
- [OpenBot](https://github.com/CopilotKit/OpenBot) - Self-hosted workspace for AI coworkers, as a desktop app or on Kubernetes: agents use the browser and tools, and wait for your approval before they act.
- [Jan](https://jan.ai) - Local AI client that runs models on your machine and supports tool and MCP integrations (`Open Source`).
- [AnythingLLM](https://anythingllm.com) - Client for chatting with your own documents and connecting them to tools and agents (`Open Source`).
- [DeepChat](https://github.com/ThinkInAIXYZ/deepchat) - Extensible chat client that supports multiple providers, tools and MCP connections in one interface (`Open Source`).
- [5ire](https://5ire.app) - AI client that brings multiple models, tools and an MCP marketplace into one desktop app (`Open Source`).
- [TypingMind](https://www.typingmind.com) - Chat interface for bringing your own model keys, prompts and tools together in one place (`Freemium`).
- [Raycast](https://www.raycast.com) - Launcher that extends into an app directory, including AI commands and MCP-powered actions (`Freemium`).

## Browser, computer use and sandboxes

- [Playwright](https://playwright.dev) - Microsoft's browser automation library, the base of many agent browser tools and MCP servers.
- [Puppeteer](https://pptr.dev) - Chrome team's Node library for driving Chromium, still widely used in scraping and agents.
- [Stagehand](https://github.com/browserbase/stagehand) - Browserbase's AI-friendly browser automation SDK, with an MCP server and a Playwright-like API.
- [Browser Use](https://github.com/browser-use/browser-use) - Open-source Python library that lets agents operate a real browser with high-level actions.
- [Browserbase](https://www.browserbase.com) - Cloud browsers for agents: stealth, sessions, Stagehand and an official MCP server.
- [E2B](https://e2b.dev) - Secure cloud sandboxes so agents can run code, install packages and use a desktop or browser.
- [Steel](https://steel.dev) - Open-source and hosted browser infrastructure made for AI agents.
- [Kernel](https://www.kernel.sh) - Cloud browser platform for agents, with stealth, sessions and an API/MCP.
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Open-source crawler built for LLM and agent pipelines, with clean markdown output.
- [Skyvern](https://skyvern.com) - Open-source and hosted browser agent that completes workflows from a goal or a workflow definition.
- [Daytona](https://www.daytona.io) - Secure, fast infrastructure for running AI-generated code and coding agents in isolated workspaces.
- [Modal](https://modal.com) - Serverless compute for running agent workloads, sandboxes and GPU jobs from Python.
- [Firecrawl](https://www.firecrawl.dev) - API and MCP for turning websites into clean markdown or structured data for agents.
- [Computer Use (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/computer-use) - Anthropic's official computer-use capability: Claude can operate a desktop via screenshots and actions.
- [Scrapybara](https://scrapybara.com) - Cloud Ubuntu desktops and browsers that agents can control through an SDK.
- [agent-browser](https://github.com/vercel-labs/agent-browser) - Vercel's browser automation CLI built for AI agents, so they can click, type and inspect pages from a terminal.
- [Crawlee](https://crawlee.dev) - Library for reliable web crawling and scraping, with queues and retries built in (`Open Source`).
- [Browserless](https://www.browserless.io) - Browser automation service that gives scripts a remote Chrome instance without managing infrastructure (`Freemium`).
- [Hyperbrowser](https://www.hyperbrowser.ai) - Browser infrastructure for agents that need headless sessions, scraping and automation at scale (`Freemium`).
- [Lightpanda](https://lightpanda.io) - Lightweight headless browser focused on fast automation and low resource use for agents (`Open Source`).
- [WebContainers](https://webcontainers.io) - Technology that runs a full development environment inside the browser for demos and agent sandboxes (`Open Source`).
- [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) - Isolated runtime for executing untrusted code from agents with defined limits and quick startup (`Freemium`).
- [Dagger](https://dagger.io) - Programmable CI engine that lets agents define and run reproducible pipelines as code (`Open Source`).
- [Selenium](https://www.selenium.dev) - Browser automation framework for testing web applications across browsers, platforms and screen sizes (`Open Source`).

## Data, scraping and search APIs

- [Apify](https://fluyeporlaweb.com/go/apify/?p=github-readme) - Platform and store of web-scraping and browser Actors that agents can run through the API or MCP. *(affiliate)*
- [DataForSEO](https://fluyeporlaweb.com/go/dataforseo/?p=github-readme) - Pay-as-you-go API for SERP, keywords, backlinks and LLM-visibility data that agents can call. *(affiliate)*
- [Tavily](https://tavily.com) - Search and extract API designed for agents, with an official MCP server.
- [Exa](https://exa.ai) - Neural web search and contents API, with an official MCP server for agents.
- [Jina AI](https://jina.ai) - Reader, search and embedding APIs that turn web pages and files into LLM-friendly context.
- [SerpAPI](https://serpapi.com) - Hosted real-time API for Google and other search-engine results.
- [Bright Data](https://brightdata.com) - Web data platform with unlocking, scraping APIs and agent-oriented datasets.
- [Perplexity API](https://docs.perplexity.ai) - Sonar API for grounded, cited web answers that agents can call as a research tool.
- [Scrapling](https://github.com/D4Vinci/Scrapling) - Python web-scraping framework that covers fetching, parsing and anti-bot cases in one toolkit an agent can call.
- [Scrapy](https://scrapy.org) - Python framework for crawling sites and extracting structured data from pages at scale (`Open Source`).
- [Serper](https://serper.dev) - Search API that returns Google results in a format that is easy to use inside agents (`Freemium`).
- [Brave Search API](https://brave.com/search/api/) - Search API that provides web and news results for agents and applications that need fresh context (`Freemium`).
- [Oxylabs](https://oxylabs.io) - Data collection API with proxies and parsers for scraped pages that need to stay reliable (`Freemium`).
- [Parallel](https://parallel.ai) - Search and extraction API that turns web pages into structured input for LLM workflows (`Freemium`).

## Memory, RAG and vector stores

- [Mem0](https://mem0.ai) - Memory layer for AI agents: extract, store and retrieve long-term user and agent memories.
- [Zep](https://www.getzep.com) - Memory and knowledge graph for agents, with temporal context and a Python/TypeScript SDK.
- [Chroma](https://www.trychroma.com) - Open-source embedding database popular for local and production RAG in agent apps.
- [Qdrant](https://qdrant.tech) - Open-source vector database with a strong filter story and an official MCP server.
- [Pinecone](https://www.pinecone.io) - Managed vector database used as the retrieval backend of many production agents.
- [Weaviate](https://weaviate.io) - Open-source vector database with hybrid search, collections and a cloud offering.
- [Milvus](https://milvus.io) - Open-source, scalable vector database from Zilliz, including the lighter Milvus Lite.
- [pgvector](https://github.com/pgvector/pgvector) - PostgreSQL extension for vector similarity search, the default for many self-hosted RAG stacks.
- [LanceDB](https://lancedb.com) - Embedded multimodal vector database built on Lance, good for local agent memory.
- [Graphiti](https://github.com/getzep/graphiti) - Zep's open-source framework for building real-time, temporally-aware knowledge graphs for agents.
- [claude-mem](https://github.com/thedotmack/claude-mem) - Persistent memory for coding agents: it captures what the agent does, compresses it and injects relevant context into later sessions.
- [GraphRAG](https://github.com/microsoft/graphrag) - Technique that builds knowledge graphs over documents so agents can answer questions across connected ideas (`Open Source`).
- [RAGFlow](https://github.com/infiniflow/ragflow) - Retrieval platform that prepares documents and embeddings for question answering over your own content (`Open Source`).
- [LightRAG](https://github.com/HKUDS/LightRAG) - Lightweight RAG framework that indexes documents and retrieves relevant context for agent answers (`Open Source`).
- [Cognee](https://www.cognee.ai) - Memory layer that turns data and conversations into a knowledge graph agents can query over time (`Open Source`).
- [txtai](https://github.com/neuml/txtai) - Library combining embeddings, search and workflows for building semantic applications on text data (`Open Source`).
- [FAISS](https://github.com/facebookresearch/faiss) - Library for fast similarity search over vectors, used to retrieve relevant passages in RAG systems (`Open Source`).
- [Vespa](https://vespa.ai) - Search and inference engine that serves vector, text and structured queries at scale for agents (`Open Source`).
- [MongoDB Atlas Vector Search](https://www.mongodb.com/products/platform/atlas-vector-search) - Vector search on documents in Atlas, useful for grounding agent answers in your own data (`Freemium`).

## Observability, evals and tracing

- [LangSmith](https://www.langchain.com/langsmith) - LangChain's platform for tracing, evaluating and monitoring agents and LLM apps.
- [Langfuse](https://langfuse.com) - Open-source LLM engineering platform: traces, prompts, evals and metrics, self-hosted or cloud.
- [Arize Phoenix](https://phoenix.arize.com) - Open-source tracing, evaluation and playground for LLM and agent applications.
- [Braintrust](https://www.braintrust.dev) - Eval and observability platform for AI products, with a strong experiment workflow.
- [Helicone](https://www.helicone.ai) - Open-source LLM gateway and observability: logs, costs, caching and prompt management.
- [Promptfoo](https://www.promptfoo.dev) - Open-source evals and red-teaming for prompts, agents and RAG, runnable in CI.
- [DeepEval](https://github.com/confident-ai/deepeval) - Open-source evaluation framework for LLM and agent outputs, with many built-in metrics.
- [Ragas](https://docs.ragas.io) - Open-source evaluation toolkit focused on RAG and agent pipelines.
- [Weights & Biases Weave](https://wandb.ai/site/weave) - W&B Weave for tracing, evaluating and iterating on LLM and agent applications.
- [Portkey](https://portkey.ai) - AI gateway with observability, guardrails, routing and a unified API across providers.
- [Opik](https://www.comet.com/site/products/opik/) - Platform for tracing LLM calls, evaluating outputs and debugging agent behavior over time (`Open Source`).
- [LangWatch](https://langwatch.ai) - Observability and evaluation workspace for teams shipping LLM features and monitoring their quality (`Freemium`).
- [AgentOps](https://www.agentops.ai) - Tool that records agent sessions, tool calls and failures so runs can be replayed and debugged (`Freemium`).
- [TruLens](https://www.trulens.org) - Library for evaluating retrieval and generation quality with feedback functions and trace inspection (`Open Source`).
- [OpenLLMetry](https://www.traceloop.com) - OpenTelemetry-based tracing for LLM apps and agents, compatible with existing observability stacks (`Open Source`).
- [Giskard](https://www.giskard.ai) - Testing library that scans LLM applications for vulnerabilities, bias and regressions before release (`Open Source`).

## LLM APIs, routers and runtimes

- [OpenAI API](https://platform.openai.com/docs) - Official API for GPT, reasoning, computer use, voice and the Agents SDK.
- [Anthropic API](https://docs.anthropic.com) - Official Claude API, including tool use, computer use, files, MCP connectors and the Agent SDK.
- [Google AI Studio / Gemini API](https://ai.google.dev) - Official Gemini API with function calling, thinking and multimodal live features.
- [xAI API](https://docs.x.ai) - Official API for Grok models, with tool use and live search.
- [Groq](https://groq.com) - Very fast inference API for open models, often used as a cheap, low-latency agent backend.
- [Together AI](https://www.together.ai) - Inference, fine-tuning and endpoints for open models, with an OpenAI-compatible API.
- [Fireworks AI](https://fireworks.ai) - Fast inference platform for open and compound AI models.
- [Mistral AI](https://mistral.ai) - European model lab with an API for chat, codestral, embeddings and agents.
- [Cohere](https://cohere.com) - API for Command models, embeddings, rerank and agent-style tool use.
- [DeepSeek](https://www.deepseek.com) - API for DeepSeek chat and reasoner models, widely used as a cost-efficient agent brain.
- [OpenRouter](https://openrouter.ai) - Unified API that routes to hundreds of models from many providers, with one key.
- [LiteLLM](https://www.litellm.ai) - Open-source proxy and Python SDK that speaks the OpenAI format to 100+ model providers.
- [Ollama](https://ollama.com) - The simplest way to run open models locally, with an API that many agents already speak.
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput open-source inference server for hosting models your agents can call.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - The standard C/C++ runtime for running GGUF models locally, with a server and bindings.
- [LM Studio](https://lmstudio.ai) - Desktop app and local server for discovering and running models, including as an OpenAI-compatible endpoint.
- [Hugging Face Inference](https://huggingface.co/docs/inference-providers) - Unified inference API and providers to run open models from the Hugging Face Hub.
- [Azure OpenAI](https://azure.microsoft.com/products/ai-services/openai-service/) - OpenAI models hosted on Azure, with enterprise networking, identity and regional options.
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) - AWS managed API for many foundation models, plus Bedrock Agents and Guardrails.
- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) - Inference and AI bindings that run at the edge, close to Workers and Agents.
- [Cerebras](https://www.cerebras.ai) - Very high-throughput inference API, useful when an agent loop needs low latency.
- [SGLang](https://github.com/sgl-project/sglang) - Serving framework for LLMs with structured generation and fast inference for high-throughput applications (`Open Source`).
- [LocalAI](https://localai.io) - Local inference server that runs open models on your hardware with an OpenAI-compatible API (`Open Source`).
- [Text Generation Inference](https://github.com/huggingface/text-generation-inference) - Inference server from Hugging Face optimized for serving large language models efficiently (`Open Source`).
- [LMDeploy](https://github.com/InternLM/lmdeploy) - Inference and serving toolkit for LLMs with compression and fast kernels for deployment (`Open Source`).
- [MiniMax API](https://platform.minimax.io) - Model API for text, voice and multimodal tasks, used when an agent needs hosted generation (`Freemium`).
- [SambaNova](https://sambanova.ai) - Inference platform for running open models on specialized hardware through an API (`Freemium`).

## Workflow and orchestration

- [n8n](https://n8n.io) - Open-source workflow automation with AI nodes, agents and an official MCP server. Self-host or cloud.
- [Make](https://www.make.com) - Visual automation platform that connects apps and can run AI steps and scenarios agents trigger.
- [Zapier](https://zapier.com) - Automation platform with a large app catalog and an MCP server that exposes actions to agents.
- [Temporal](https://temporal.io) - Durable execution platform often used as the backbone of long-running agent workflows.
- [Inngest](https://www.inngest.com) - Durable functions and event workflows in TypeScript, a common harness for agent steps.
- [Prefect](https://www.prefect.io) - Python workflow orchestrator used to schedule, retry and observe agent and data pipelines.
- [Pipedream](https://pipedream.com) - Integration and workflow platform with a huge catalog of APIs and MCP-oriented tools.
- [Trigger.dev](https://trigger.dev) - Open-source background jobs and durable workflows for TypeScript apps, including agent runs.
- [Activepieces](https://www.activepieces.com) - No-code automation platform with a growing set of connectors for building agent-assisted workflows (`Open Source`).
- [Windmill](https://www.windmill.dev) - Developer-focused workflow platform for running scripts as jobs, UIs and scheduled automations (`Open Source`).
- [Kestra](https://kestra.io) - Orchestration platform that defines data and agent workflows as code with visible execution history (`Open Source`).
- [Apache Airflow](https://airflow.apache.org) - Workflow platform for scheduling and monitoring pipelines, widely used in data engineering (`Open Source`).
- [Dagster](https://dagster.io) - Data orchestrator that makes assets, dependencies and failures visible across all your pipelines (`Open Source`).
- [Gumloop](https://www.gumloop.com) - Visual automation builder for teams that want to chain AI steps with everyday tools (`Freemium`).

## Voice, speech and realtime

- [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) - Official OpenAI API for low-latency speech-to-speech and multimodal agents.
- [Gemini Live](https://ai.google.dev/gemini-api/docs/live) - Gemini's live multimodal API for realtime voice and video agents.
- [ElevenLabs](https://elevenlabs.io) - Text-to-speech with high-quality voices, plus voice cloning and conversational-voice agents you can build on.
- [Deepgram](https://deepgram.com) - Streaming speech-to-text and voice-agent APIs with low latency.
- [AssemblyAI](https://www.assemblyai.com) - Speech-to-text and audio-understanding APIs, including streaming for voice agents.
- [Pipecat](https://www.pipecat.ai) - Open-source Python framework for building realtime voice and multimodal agents.
- [LiveKit](https://livekit.io) - Open-source realtime media stack, with Agents for voice, video and avatars.
- [Vapi](https://vapi.ai) - Platform for building and hosting voice AI agents over phone and web.
- [Retell AI](https://www.retellai.com) - Platform for phone and voice agents, with LLM, TTS and telephony already wired.
- [Cartesia](https://cartesia.ai) - Ultra-low-latency speech models and APIs for realtime voice agents.
- [Whisper](https://github.com/openai/whisper) - OpenAI's open-source speech-to-text model, still a default local STT for agents.
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - Optimized speech-to-text library that transcribes audio locally with lower resource use than comparable models (`Open Source`).
- [Piper](https://github.com/rhasspy/piper) - Fast local text-to-speech engine with downloadable voices for offline applications and embedded products (`Open Source`).
- [Gladia](https://www.gladia.io) - Speech API that transcribes and understands audio, useful for adding voice input to products (`Freemium`).
- [Daily](https://www.daily.co) - Real-time video and audio infrastructure for adding calls and voice rooms to applications (`Freemium`).

## Guardrails and safety

- [Guardrails AI](https://www.guardrailsai.com) - Open-source and commercial validators that structure and constrain LLM and agent outputs.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - NVIDIA's open-source toolkit for adding programmable rails around LLM applications.
- [LLM Guard](https://github.com/protectai/llm-guard) - Open-source scanner for prompt injection, PII and toxic or sensitive content.
- [Presidio](https://microsoft.github.io/presidio/) - Microsoft's open-source PII detection and anonymization, useful as an agent pre/post filter.
- [Lakera Guard](https://www.lakera.ai) - Security platform focused on prompt injection and runtime protection for AI apps.
- [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) - Managed content filters, denied topics and grounding checks for models on Bedrock.
- [Invariant](https://invariantlabs.ai) - Security and policy layer for agents: inspect traces, constrain tools and catch prompt injection.
- [SkillSpector](https://github.com/NVIDIA/SkillSpector) - NVIDIA's security scanner for agent skills: it looks for vulnerabilities, malicious patterns, prompt injection and supply-chain risk before you install them.
- [garak LLM scanner](https://github.com/NVIDIA/garak) - Scanner that probes LLM applications for prompt injection, leakage and other common weaknesses (`Open Source`).
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - Framework for evaluating AI models with structured tasks, scorers and reproducible logs (`Open Source`).
- [PyRIT](https://github.com/Azure/PyRIT) - Toolkit for red-teaming generative AI systems with automated adversarial prompts and scoring (`Open Source`).
- [LangKit](https://github.com/whylabs/langkit) - Toolkit for monitoring LLM inputs and outputs with metrics for safety, relevance and quality (`Open Source`).

## Agent skills and tool marketplaces

- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic's official Agent Skills: the format, docs and a set of reference skills for Claude.
- [obra/superpowers](https://github.com/obra/superpowers) - Widely used collection of skills that give coding agents a structured way to plan and ship work.
- [vercel-labs/skills](https://github.com/vercel-labs/skills) - CLI and registry (`npx skills`) for installing Agent Skills into a project.
- [Composio](https://composio.dev) - Managed tool marketplace and SDK so agents can call thousands of third-party APIs with auth handled.
- [Arcade](https://arcade.dev) - Tool and auth platform for agents, with a catalog of integrations and an MCP-friendly runtime.
- [impeccable](https://github.com/pbakaus/impeccable) - A design vocabulary for coding agents: skills to steer polish and critique, and to catch generic AI-made work before it ships.
- [hallmark](https://github.com/Nutlope/hallmark) - A design skill that helps Claude Code, Cursor and Codex avoid generic AI-looking interfaces.
- [claude-seo](https://github.com/AgriciDaniel/claude-seo) - Agent skill for technical SEO and AI-search (GEO/AEO) audits, with sub-skills for schema, citations, agent readiness and reports.
- [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill) - Official Cloudflare skill for multi-phase security audits, with independently verified, machine-readable findings.
- [instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) - A set of agent skills for running an Instagram account: research, hooks, captions and a more human publishing tone.
- [last30days-skill](https://github.com/mvanhorn/last30days-skill) - Agent skill that researches a topic across Reddit, X, YouTube, Hacker News, Polymarket and the web, then writes a sourced brief.
- [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) - Local FFmpeg tools with a machine-readable contract and an MCP server, so agents can cut, subtitle and export video without API keys.
- [mcp.so](https://mcp.so) - Directory of MCP servers that helps find connectors for tools and data sources before building your own (`Free`).

## Marketing, SEO and prospecting

APIs and platforms that agent workflows use to find leads, enrich accounts and research search demand. Open-source tools sit next to widely used products with a public page we can link.

- [Clay](https://www.clay.com) - Data enrichment and outreach workspace for building prospect lists from many sources in one flow (`Freemium`).
- [Apollo.io](https://www.apollo.io) - Prospecting platform with contact data and sequences for sales and growth teams (`Freemium`).
- [Hunter](https://hunter.io) - Tool for finding and verifying professional email addresses from a domain during outreach work (`Freemium`).
- [PhantomBuster](https://phantombuster.com) - Automation tool for social platforms that helps collect leads and run repetitive outreach tasks (`Freemium`).
- [Instantly](https://instantly.ai) - Outreach platform for managing cold email sequences, follow-ups and replies across several inboxes (`Freemium`).
- [Ahrefs](https://ahrefs.com) - SEO platform for keyword research, backlink analysis and tracking search visibility over time (`Freemium`).
- [Screaming Frog](https://www.screamingfrog.co.uk/seo-spider/) - Crawler that audits websites for broken links, redirects and on-page issues before launch or during maintenance (`Freemium`).
- [AlsoAsked](https://alsoasked.com) - Tool that maps related questions from search results to plan content around real user intent (`Freemium`).
- [BuiltWith](https://builtwith.com) - Tool that reveals the technologies behind a website, useful for market research and prospecting (`Freemium`).
- [People Data Labs](https://www.peopledatalabs.com) - Dataset provider for company and people records used to enrich prospecting and CRM workflows (`Freemium`).

## Built by fluyeporlaweb

- [prospectforge](https://github.com/fluyeporlaweb/prospectforge) - Open-source B2B lead pipeline: discover contacts, qualify them against your ICP and draft outreach. Dry-run by default. Never sends email.
- [Apify — fluyeporlaweb actors](https://fluyeporlaweb.com/go/apify-fluyeporlaweb/?p=github-readme) - Open actors we publish on Apify (jobs, RSS, BOE, public tenders) that an agent can run through the Apify API or MCP. *(affiliate)*

## Sponsors

This project is free and open source. Brands that want to appear here or collaborate with us can write to [colab@fluyeporlaweb.com](mailto:colab@fluyeporlaweb.com) or visit [fluyeporlaweb.com/patrocina](https://fluyeporlaweb.com/patrocina).

**[Your brand here](https://fluyeporlaweb.com/patrocina)**

## Related lists

This directory was curated from primary sources and from these lists, among others. We did not copy them: we selected, deduplicated and rewrote the descriptions.

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - A large, well-maintained directory of MCP servers.
- [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) - A companion list of MCP clients and hosts.
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - An early and influential survey of AI agent projects.
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - Open-source LLM apps, RAG systems and agent examples.
- [kyrolabs/awesome-langchain](https://github.com/kyrolabs/awesome-langchain) - A curated catalog around the LangChain ecosystem.
- [tensorchord/Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) - Tools for serving, observing and operating LLM systems.
- [modelcontextprotocol](https://github.com/modelcontextprotocol) - The official MCP organization: spec, SDKs, registry and inspector.

## Contributing

Suggestions and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening one, and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

If you work on this repo with a coding agent, point it to [AGENTS.md](AGENTS.md).

## License

[MIT](LICENSE) © fluyeporlaweb

## Links

- Website: [fluyeporlaweb.com](https://fluyeporlaweb.com)
- X: [@fluyeporlaweb](https://x.com/fluyeporlaweb)
- Telegram: [t.me/fluyeporlaweb](https://t.me/fluyeporlaweb)
- Email: [colab@fluyeporlaweb.com](mailto:colab@fluyeporlaweb.com)
