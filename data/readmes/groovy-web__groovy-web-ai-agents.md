# Groovy Web AI Agents

[![Built by Groovy Web](https://img.shields.io/badge/Built%20by-Groovy%20Web-0f3460?logo=github&logoColor=white)](https://www.groovyweb.co/?utm_source=github&utm_medium=readme&utm_campaign=ai-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Production-ready AI agent configurations for Groovy Web ecosystem

## 🚀 Overview

A comprehensive collection of AI agent configurations, prompts, and orchestration patterns for building intelligent web applications. This repository provides reusable agent templates for various use cases including content generation, data analysis, code review, and customer support.

## ✨ Features

- **Modular Agent System**: Pre-configured agent templates for common tasks
- **Multi-Agent Orchestration**: Patterns for agent collaboration and communication
- **Prompt Engineering**: Battle-tested prompts with examples
- **Integration Ready**: Works seamlessly with LangChain, OpenAI, and Anthropic APIs
- **TypeScript Support**: Full type definitions for agent configurations
- **Testing Suite**: Unit and integration tests for agent behaviors

## 📦 Installation

```bash
npm install @groovy-web/ai-agents
# or
yarn add @groovy-web/ai-agents
# or
pnpm add @groovy-web/ai-agents
```

## 🎯 Quick Start

```typescript
import { ContentAgent, AnalysisAgent } from '@groovy-web/ai-agents';

// Initialize a content generation agent
const contentAgent = new ContentAgent({
  model: 'gpt-4',
  temperature: 0.7,
  maxTokens: 2000,
});

const blogPost = await contentAgent.generate({
  topic: 'The Future of Web Development',
  tone: 'professional',
  length: 'medium',
});

console.log(blogPost);
```

## 🤖 Available Agents

### ContentAgent
Generate blog posts, social media content, marketing copy, and documentation.

```typescript
import { ContentAgent } from '@groovy-web/ai-agents';

const agent = new ContentAgent();
const content = await agent.generateBlogPost({
  title: 'Building Scalable APIs',
  keywords: ['REST', 'GraphQL', 'Performance'],
});
```

### AnalysisAgent
Analyze data, generate reports, and provide insights.

```typescript
import { AnalysisAgent } from '@groovy-web/ai-agents';

const agent = new AnalysisAgent();
const insights = await agent.analyzeData({
  data: userData,
  metrics: ['engagement', 'retention', 'conversion'],
});
```

### CodeReviewAgent
Review code for best practices, security, and performance issues.

```typescript
import { CodeReviewAgent } from '@groovy-web/ai-agents';

const agent = new CodeReviewAgent();
const review = await agent.reviewCode({
  language: 'typescript',
  code: sourceCode,
  rules: ['security', 'performance', 'style'],
});
```

### SupportAgent
Handle customer support queries with context-aware responses.

```typescript
import { SupportAgent } from '@groovy-web/ai-agents';

const agent = new SupportAgent({
  knowledgeBase: faqData,
  companyInfo: companyDetails,
});

const response = await agent.handleQuery({
  query: userQuery,
  context: ticketHistory,
});
```

## 🔧 Configuration

### Base Agent Options

```typescript
interface AgentConfig {
  model: string;              // Model identifier (gpt-4, claude-3, etc.)
  temperature?: number;       // 0-1, default: 0.7
  maxTokens?: number;         // Max response tokens
  apiKey?: string;            // API key (or use env variable)
  timeout?: number;           // Request timeout in ms
  retries?: number;           // Retry attempts
  memory?: boolean;           // Enable conversation memory
}
```

### Custom Agent Creation

```typescript
import { createAgent } from '@groovy-web/ai-agents';

const customAgent = createAgent({
  name: 'SEOOptimizer',
  systemPrompt: 'You are an SEO expert...',
  tools: [keywordAnalyzer, contentOptimizer],
  config: {
    model: 'claude-3-opus',
    temperature: 0.5,
  },
});
```

## 🌐 Multi-Agent Patterns

### Sequential Execution

```typescript
import { AgentOrchestrator } from '@groovy-web/ai-agents';

const orchestrator = new AgentOrchestrator();

const result = await orchestrator.sequential([
  { agent: researchAgent, input: topic },
  { agent: contentAgent, input: '$previous.research' },
  { agent: seoAgent, input: '$previous.content' },
]);
```

### Parallel Execution

```typescript
const results = await orchestrator.parallel([
  { agent: translatorAgent, input: text, locale: 'es' },
  { agent: summarizerAgent, input: text },
  { agent: sentimentAgent, input: text },
]);
```

### Hierarchical Orchestrator

```typescript
const manager = new ManagerAgent({
  subAgents: [researcher, writer, editor],
  decisionStrategy: 'consensus', // or 'majority', 'manager-decides'
});

const output = await manager.coordinate({
  task: 'Create technical documentation',
  requirements: docs,
});
```

## 🧪 Testing

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test suite
npm test -- content-agent.test.ts
```

## 📖 Documentation

- [Agent Configuration Guide](./docs/agent-configuration.md)
- [Multi-Agent Patterns](./docs/multi-agent-patterns.md)
- [Prompt Engineering](./docs/prompt-engineering.md)
- [Integration Examples](./docs/integration-examples.md)
- [API Reference](./docs/api-reference.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) for details.

## 📄 License

MIT License - see [LICENSE](./LICENSE) for details.

## 🔗 Links

- [Groovy Web - AI-First Engineering](https://www.groovyweb.co/?utm_source=github&utm_medium=readme&utm_campaign=ai-agents)
- [Examples Repository](https://github.com/groovy-web/groovy-web-examples)
- [Issue Tracker](https://github.com/groovy-web/groovy-web-ai-agents/issues)

## ⭐ Show Your Support

Give us a star on GitHub if you find this project helpful!

---

Made with ❤️ by the Groovy Web Team

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
