# 🕷️ CogniScrape

[![npm version](https://badge.fury.io/js/cogniscrape.svg)](https://www.npmjs.com/package/cogniscrape)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Intelligent Web Scraping with LLMs** - A TypeScript library that combines traditional web scraping with Large Language Models for intelligent, structured data extraction.

## ✨ Features

- 🤖 **Dual LLM Support**: Ollama (free/local) + Google Gemini (cloud)
- 📊 **Graph-Based Architecture**: Composable, reusable node pipelines
- 🚀 **Production-Ready**: Built-in caching, retries, rate limiting, and proxy rotation
- 🎯 **Smart Parsing**: Automatic HTML→Markdown conversion and intelligent chunking
- ✅ **Schema Validation**: Zod integration for type-safe outputs
- 📝 **Multiple Formats**: JSON, CSV, XML, PDF support
- 🌐 **Browser Automation**: Playwright for dynamic content
- 🧠 **RAG Integration**: Retrieval-Augmented Generation for better accuracy

## 📦 Installation

```bash
npm install cogniscrape
```

## 🚀 Quick Start

### Basic Web Scraping with Gemini

```typescript
import { SmartScraperGraph } from 'cogniscrape';

const scraper = new SmartScraperGraph({
  prompt: 'Extract all product names and prices',
  source: 'https://example.com/products',
  config: {
    llm: {
      provider: 'gemini',
      model: 'gemini-2.0-flash-exp',
      apiKey: process.env.GEMINI_API_KEY,
    },
    verbose: true,
  },
});

const result = await scraper.run();
console.log(result);
```

### Using Ollama (100% Free & Local)

```typescript
import { SmartScraperGraph } from 'cogniscrape';

const scraper = new SmartScraperGraph({
  prompt: 'List all article titles and summaries',
  source: 'https://news.example.com',
  config: {
    llm: {
      provider: 'ollama',
      model: 'llama2',  // or 'mistral', 'codellama', etc.
      baseUrl: 'http://localhost:11434',
    },
  },
});

const result = await scraper.run();
```

## 🎯 Available Graphs

| Graph | Purpose | Use Case |
|-------|---------|----------|
| `SmartScraperGraph` | Basic scraping | Extract data from single URL |
| `SmartScraperMultiGraph` | Multi-URL scraping | Scrape multiple sources (parallel/sequential) |
| `SearchGraph` | Internet search + scrape | Search engines + content extraction |
| `DepthSearchGraph` | Deep analysis | Search + reasoning + comprehensive analysis |
| `CSVScraperGraph` | CSV export | Scrape data → export to CSV |
| `JSONScraperGraph` | JSON export | Schema-validated JSON output |

## 📚 Examples

### Multi-URL Scraping

```typescript
import { SmartScraperMultiGraph, createLLM } from 'cogniscrape';

const llm = createLLM({
  provider: 'gemini',
  model: 'gemini-2.0-flash-exp',
  apiKey: process.env.GEMINI_API_KEY,
});

const scraper = new SmartScraperMultiGraph(
  'Extract company names and descriptions',
  [
    'https://company1.com',
    'https://company2.com',
    'https://company3.com',
  ],
  { llm },
  llm,
  true // parallel execution
);

const result = await scraper.run();
```

### CSV Export with Schema Validation

```typescript
import { CSVScraperGraph } from 'cogniscrape';
import { z } from 'zod';

const schema = z.object({
  products: z.array(z.object({
    name: z.string(),
    price: z.number(),
    rating: z.number().optional(),
  })),
});

const scraper = new CSVScraperGraph(
  'Extract all products with their prices',
  'https://shop.example.com',
  {
    llm: {
      provider: 'gemini',
      model: 'gemini-2.0-flash-exp',
      apiKey: process.env.GEMINI_API_KEY,
    },
    schema,
  },
  llm,
  'products.csv'
);

await scraper.run();
```

### Internet Search Graph

```typescript
import { SearchGraph, createLLM } from 'cogniscrape';

const llm = createLLM({
  provider: 'gemini',
  model: 'gemini-2.0-flash-exp',
  apiKey: process.env.GEMINI_API_KEY,
});

const searchGraph = new SearchGraph(
  'Latest news about AI developments in 2026',
  {
    llm,
    searchEngine: 'duckduckgo',
    maxDepth: 3,
  },
  llm
);

const result = await searchGraph.run();
```

## ⚙️ Configuration Options

```typescript
interface ScraperConfig {
  llm: LLMConfig;
  verbose?: boolean;          // Enable logging
  headless?: boolean;         // Headless browser mode
  timeout?: number;           // Request timeout (ms)
  cut?: boolean;              // Enable HTML minification
  htmlMode?: boolean;         // Skip parsing (use raw HTML)
  
  // Production features
  proxy?: ProxyConfig;        // Proxy configuration
  retry?: RetryConfig;        // Retry with backoff
  rateLimit?: RateLimitConfig; // Rate limiting
  cache?: CacheConfig;        // Response caching
  
  // Advanced
  schema?: any;               // Zod schema for validation
  additionalInfo?: string;    // Extra context for LLM
  reasoning?: boolean;        // Enable reasoning mode
}
```

## 🔧 Production Features

### Proxy Rotation

```typescript
const config = {
  llm: { /* ... */ },
  proxy: {
    enabled: true,
    proxies: [
      'http://proxy1.com:8080',
      'http://proxy2.com:8080',
    ],
  },
};
```

### Retry with Exponential Backoff

```typescript
const config = {
  llm: { /* ... */ },
  retry: {
    maxRetries: 3,
    initialDelay: 1000,
    maxDelay: 10000,
    backoffMultiplier: 2,
  },
};
```

### Rate Limiting

```typescript
const config = {
  llm: { /* ... */ },
  rateLimit: {
    maxRequests: 10,
    windowMs: 1000,
    minDelay: 100,
  },
};
```

### Caching

```typescript
const config = {
  llm: { /* ... */ },
  cache: {
    enabled: true,
    ttl: 3600000, // 1 hour
    maxSize: 1000,
  },
};
```

## 🧪 Testing

```bash
npm test
```

## 🛠️ Development

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Watch mode
npm run dev

# Run examples
npx ts-node examples/smart-scraper-gemini.ts
```

## 📖 API Reference

### Models
- `OllamaModel` - Local LLM support
- `GeminiModel` - Google Gemini integration
- `createLLM(config)` - Factory function

### Graphs
- `SmartScraperGraph` - Basic web scraping
- `SmartScraperMultiGraph` - Multi-URL scraping
- `SearchGraph` - Search + scrape
- `DepthSearchGraph` - Deep search with reasoning
- `CSVScraperGraph` - Export to CSV
- `JSONScraperGraph` - Export to JSON

### Nodes
- `FetchNode` - Fetch content
- `ParseNode` - Parse & chunk
- `GenerateAnswerNode` - LLM answer generation
- `RAGNode` - Retrieval-Augmented Generation
- `SearchNode` - Internet search
- `MergeNode` - Merge results
- `PDFScraperNode` - PDF extraction
- `XMLScraperNode` - XML parsing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see LICENSE file for details

## 📬 Support

- 📧 Email: bonderiddhish@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/Riddhish1/cogniscrape/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/Riddhish1/cogniscrape/discussions)

---

**Made with ❤️ for the TypeScript community**
