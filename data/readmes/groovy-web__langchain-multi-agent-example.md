# LangChain Multi-Agent Example

[![Built by Groovy Web](https://img.shields.io/badge/Built%20by-Groovy%20Web-0f3460?logo=github&logoColor=white)](https://www.groovyweb.co/?utm_source=github&utm_medium=readme&utm_campaign=langchain-multi-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Comprehensive tutorial and code examples for building multi-agent systems with LangChain

## 🚀 Overview

This repository provides a complete, production-ready example of building multi-agent systems using LangChain. It demonstrates how to create specialized AI agents that can collaborate to solve complex tasks through orchestration patterns.

## 🎯 What You'll Learn

- **Agent Architecture**: Design patterns for AI agents
- **Multi-Agent Orchestration**: Coordinate multiple agents effectively
- **Tool Integration**: Equip agents with external tools and APIs
- **Memory Management**: Implement conversation and context memory
- **Error Handling**: Build robust multi-agent systems
- **Performance Optimization**: Optimize for cost and speed

## ✨ Features

- **Complete Working Examples**: Copy-paste ready code
- **Step-by-Step Tutorials**: From basic to advanced patterns
- **Production Best Practices**: Security, testing, deployment
- **Real-World Use Cases**: Practical applications
- **TypeScript**: Full type safety
- **Jest Tests**: Comprehensive test coverage

## 📋 Prerequisites

- Node.js 18+ installed
- Basic knowledge of TypeScript
- Understanding of async/await patterns
- API keys for OpenAI and/or Anthropic

## 🚦 Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/groovy-web/langchain-multi-agent-example.git
cd langchain-multi-agent-example
npm install
```

### 2. Set Up Environment

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
TAVILY_API_KEY=tvly-your-tavily-key  # For search
SERPER_API_KEY=your-serper-key        # For Google search
```

### 3. Run Basic Example

```bash
npm run basic-example
```

## 📚 Tutorial Structure

### Part 1: Foundation (Beginner)

**1. Single Agent Setup**
```typescript
// examples/01-single-agent.ts
import { ChatOpenAI } from "@langchain/openai";
import { AgentExecutor, createReactAgent } from "langchain/agents";

const llm = new ChatOpenAI({ temperature: 0 });
const agent = await createReactAgent({
  llm,
  tools: [],
  prompt: "You are a helpful assistant.",
});

const agentExecutor = new AgentExecutor({
  agent,
  tools: [],
});

const result = await agentExecutor.invoke({
  input: "What is the capital of France?",
});
```

**2. Adding Tools to Agents**
```typescript
// examples/02-agent-with-tools.ts
import { SerperAPI } from "@langchain/community/tools";

const searchTool = new SerperAPI();
const calculator = new CalculatorTool();

const agent = await createReactAgent({
  llm,
  tools: [searchTool, calculator],
  prompt: "You are a research assistant.",
});
```

### Part 2: Multi-Agent Patterns (Intermediate)

**3. Sequential Agent Chain**
```typescript
// examples/03-sequential-agents.ts
import { AgentChain } from "../lib/agent-chain";

const researcher = createAgent({
  role: "Researcher",
  goal: "Find information on {topic}",
  tools: [searchTool],
});

const writer = createAgent({
  role: "Writer",
  goal: "Write a blog post about {topic}",
  tools: [],
});

const chain = new AgentChain([researcher, writer]);
const result = await chain.run({ topic: "AI agents" });
```

**4. Parallel Agent Execution**
```typescript
// examples/04-parallel-agents.ts
import { ParallelExecutor } from "../lib/parallel-executor";

const agents = [
  createTranslatorAgent({ language: "Spanish" }),
  createTranslatorAgent({ language: "French" }),
  createTranslatorAgent({ language: "German" }),
];

const executor = new ParallelExecutor();
const translations = await executor.executeAll(agents, {
  text: "Hello, world!",
});
```

**5. Hierarchical Agent Teams**
```typescript
// examples/05-hierarchical-agents.ts
import { ManagerAgent } from "../lib/manager-agent";

const manager = new ManagerAgent({
  name: "Project Manager",
  subAgents: [
    { name: "Researcher", agent: researchAgent },
    { name: "Writer", agent: writerAgent },
    { name: "Editor", agent: editorAgent },
  ],
  coordination: "sequential", // or "parallel"
});

const report = await manager.coordinate({
  task: "Create a market research report",
  topic: "Electric Vehicles",
});
```

### Part 3: Advanced Patterns (Advanced)

**6. Agent with Memory**
```typescript
// examples/06-agent-with-memory.ts
import { BufferMemory } from "langchain/memory";

const memory = new BufferMemory({
  memoryKey: "chat_history",
  returnMessages: true,
});

const agent = await createReactAgent({
  llm,
  tools: [searchTool],
  prompt: "You are a helpful assistant with memory.",
  memory,
});

// First interaction
await agentExecutor.invoke({
  input: "My name is Alice",
});

// Agent remembers!
await agentExecutor.invoke({
  input: "What is my name?",
});
```

**7. Self-Correction Agent**
```typescript
// examples/07-self-correcting-agent.ts
import { ReviewAgent } from "../lib/review-agent";

const writer = createWriterAgent();
const reviewer = new ReviewAgent({
  criteria: ["accuracy", "clarity", "style"],
  maxIterations: 3,
});

const content = await reviewer.improveWithFeedback({
  contentGenerator: writer,
  topic: "Quantum Computing",
});
```

**8. Multi-Agent Debate**
```typescript
// examples/08-agent-debate.ts
import { AgentDebate } from "../lib/agent-debate";

const debate = new AgentDebate({
  protagonist: createAgent({ stance: "pro-ai" }),
  antagonist: createAgent({ stance: "skeptic" }),
  moderator: createAgent({ stance: "neutral" }),
  rounds: 3,
});

const summary = await debate.conduct({
  topic: "Will AI replace human workers?",
});
```

## 🛠️ Real-World Examples

### Example 1: Content Creation Pipeline

```typescript
// real-world/content-pipeline.ts
const pipeline = new AgentPipeline([
  {
    agent: seoResearcher,
    outputKey: "keywords",
  },
  {
    agent: contentWriter,
    inputKeys: ["keywords"],
    outputKey: "draft",
  },
  {
    agent: humanEditor,
    inputKeys: ["draft"],
    outputKey: "edited",
  },
  {
    agent: publisher,
    inputKeys: ["edited"],
    outputKey: "published",
  },
]);

const result = await pipeline.execute({
  topic: "Best practices for API design",
});
```

### Example 2: Customer Support System

```typescript
// real-world/customer-support.ts
const triageAgent = new TriageAgent({
  categories: ["billing", "technical", "feature-request"],
});

const routingMap = {
  billing: billingAgent,
  technical: technicalSupportAgent,
  "feature-request": productTeamAgent,
};

const supportSystem = new SupportSystem({
  triageAgent,
  routingMap,
  escalation: humanAgent,
});

const response = await supportSystem.handleTicket({
  customerQuery: "I was charged twice!",
  customerHistory: customerData,
});
```

### Example 3: Research Assistant

```typescript
// real-world/research-assistant.ts
const researchTeam = new ResearchTeam({
  leader: leadResearcher,
  members: [
    dataCollector,
    dataAnalyzer,
    reportWriter,
  ],
});

const research = await researchTeam.conductResearch({
  question: "What is the impact of remote work on productivity?",
  sources: ["arxiv", "google-scholar", "news"],
  depth: "comprehensive",
});
```

## 🧪 Testing

```bash
# Run all tests
npm test

# Run specific test suite
npm test -- single-agent.test.ts

# Watch mode
npm run test:watch

# Coverage
npm run test:coverage
```

## 📖 Documentation

- [LangChain Documentation](https://js.langchain.com/)
- [API Reference](./docs/api-reference.md)
- [Architecture Guide](./docs/architecture.md)
- [Best Practices](./docs/best-practices.md)
- [Troubleshooting](./docs/troubleshooting.md)

## 🎓 Learning Path

1. **Start Here**: Run `npm run basic-example`
2. **Read Tutorials**: Follow `examples/01-` through `08-`
3. **Study Real-World**: Check `real-world/` examples
4. **Build Your Own**: Use patterns learned
5. **Optimize**: Read best practices and optimize

## 🔧 Customization

All examples are modular. Mix and match patterns:

```typescript
import { AgentChain, ParallelExecutor, ManagerAgent } from './lib';

const customSystem = new ManagerAgent({
  subAgents: [
    new AgentChain([agent1, agent2]),
    new ParallelExecutor([agent3, agent4]),
  ],
});
```

## 🤝 Contributing

We welcome improvements! See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

MIT License - see [LICENSE](./LICENSE)

## 🔗 Resources

- [LangChain GitHub](https://github.com/langchain-ai/langchainjs)
- [LangChain Discord](https://discord.gg/6ADWatUYXR)
- [Groovy Web - AI-First Engineering](https://www.groovyweb.co/?utm_source=github&utm_medium=readme&utm_campaign=langchain-multi-agent)

## ⭐ Support

If you find this helpful, please give us a star!

---

Made with ❤️ by Groovy Web

---

## Related Repositories

Explore more open-source tools from [Groovy Web](https://www.groovyweb.co/?utm_source=github&utm_medium=readme&utm_campaign=cross-link):

- **[langchain-multi-agent-example](https://github.com/groovy-web/langchain-multi-agent-example)** -- Multi-agent systems tutorial with LangChain
- **[rag-system-pgvector](https://github.com/groovy-web/rag-system-pgvector)** -- Production RAG with PostgreSQL + pgvector
- **[rag-systems-production](https://github.com/groovy-web/rag-systems-production)** -- Enterprise-grade RAG systems
- **[ai-testing-mcp](https://github.com/groovy-web/ai-testing-mcp)** -- AI testing via Model Context Protocol
- **[edge-computing-starter](https://github.com/groovy-web/edge-computing-starter)** -- Cloudflare Workers + Hono template
- **[claude-code-workflows](https://github.com/groovy-web/claude-code-workflows)** -- Workflows for Claude Code
- **[groovy-web-ai-agents](https://github.com/groovy-web/groovy-web-ai-agents)** -- Production AI agent configs
- **[groovy-web-examples](https://github.com/groovy-web/groovy-web-examples)** -- Groovy/Grails examples
