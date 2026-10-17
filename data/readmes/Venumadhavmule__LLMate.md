# LLMate

**The LiteLLM for the JVM — one REST API for every LLM provider.**

Stop juggling SDKs. LLMate is a Spring Boot gateway that unifies OpenAI, Anthropic, Google Gemini, Ollama, and 12 more providers behind a single `/api/v1/chat` endpoint. Switch models with a config change. Get automatic fallbacks, retry logic, and Prometheus metrics for free.

*Looking for a UI? Check out the **[LLMate Chat](https://github.com/Venumadhavmule/LLMate-Chat)** companion frontend.*

---

## See It In Action

### Backend API
```bash
# One command to ask any model
curl -X POST http://localhost:8080/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"fast","messages":[{"role":"user","content":"What is a record in Java 21?"}]}'
```

```json
{
  "id": "3f8a2b1c",
  "provider": "openai",
  "model": "gpt-4o-mini",
  "content": "A record in Java 21 is a special kind of class...",
  "usage": { "promptTokens": 28, "completionTokens": 95, "totalTokens": 123 }
}
```

Change `"fast"` to `"smart"` and the same request routes to Claude. Change it to `"local"` and it hits your local Ollama. Zero code changes.

### Frontend UI
Prefer a visual interface? Use **[LLMate Chat](https://github.com/Venumadhavmule/LLMate-Chat)** — the official React frontend for this gateway. It supports real-time SSE streaming, theme switching, and multi-model selection out of the box.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Venumadhavmule/LLMate-Chat/blob/main/docs/llmate-interface-dark.png?raw=true">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/Venumadhavmule/LLMate-Chat/blob/main/docs/llmate-interface-light.png?raw=true">
  <img alt="LLMate Chat Preview" src="https://github.com/Venumadhavmule/LLMate-Chat/blob/main/docs/llmate-interface-light.png?raw=true" width="600">
</picture>

---

## Features

- **16 LLM providers** behind one unified REST API (OpenAI, Anthropic, Google Gemini, Ollama, Groq, DeepSeek, Mistral, Perplexity, NVIDIA, HuggingFace, Cohere, and more)
- **Named aliases** — map `"fast"`, `"smart"`, `"local"` to any provider/model in config
- **Automatic fallback chain** — if OpenAI is down, route to Anthropic, then Ollama
- **SSE streaming** with both plain-text and structured JSON chunk formats
- **Multimodal endpoints** — embeddings, image generation (DALL-E 3), audio transcription (Whisper), TTS, and content moderation
- **RAG pipeline** — built-in document ingestion and retrieval-augmented generation via PGVector
- **Resilience4j** retry + circuit breaker baked into the request pipeline
- **Prometheus + Grafana** metrics at `/actuator/prometheus` with per-provider latency, token usage, and error rates

---

## Supported Providers

| Provider   | Chat | Stream | Embed | Image | Audio | Moderation | Multimodal | Notes                        |
|------------|------|--------|-------|-------|-------|------------|------------|------------------------------|
| OpenAI     | ✅   | ✅     | ✅    | ✅    | ✅    | ✅         | ✅         | gpt-4o, dall-e-3, whisper    |
| Anthropic  | ✅   | ✅     | —     | —     | —     | —          | ✅         | claude-3-5-sonnet            |
| Google     | ✅   | ✅     | —     | —     | —     | —          | ✅         | gemini-2.5-flash-lite        |
| Ollama     | ✅   | ✅     | ✅    | —     | —     | —          | —          | Local, free, no API key      |
| Mistral    | ✅   | ✅     | —     | —     | —     | ✅         | —          | mistral-large, codestral     |
| Groq       | ✅   | ✅     | —     | —     | —     | —          | —          | LPU-accelerated inference    |
| DeepSeek   | ✅   | ✅     | —     | —     | —     | —          | —          | deepseek-chat, reasoner      |
| Perplexity | ✅   | ✅     | —     | —     | —     | —          | —          | Search-augmented (sonar-pro) |
| NVIDIA NIM | ✅   | ✅     | —     | —     | —     | —          | —          | Nemotron, Llama on NIM       |
| HuggingFace| ✅   | ✅     | —     | —     | —     | —          | —          | Inference Endpoints           |
| Cohere     | ✅   | ✅     | —     | —     | —     | —          | —          | command-r-plus               |
| MiniMax    | ✅   | ✅     | —     | —     | —     | —          | —          | abab6.5-chat                 |
| Moonshot   | ✅   | ✅     | —     | —     | —     | —          | —          | moonshot-v1-128k             |
| ZhiPu AI   | ✅   | ✅     | —     | —     | —     | —          | —          | glm-4-plus                   |
| QianFan    | ✅   | ✅     | —     | —     | —     | —          | —          | ERNIE 4.0                    |
| OCI GenAI  | ✅   | ✅     | —     | —     | —     | —          | —          | Oracle Cloud                 |

Providers marked with `—` do not expose that capability. Groq through OCI GenAI use the **OpenAI-compatible adapter** — any provider with an OpenAI-compatible API can be added with zero code.

---

## Quick Start

### Prerequisites

| Tool  | Version | Link                                 |
|-------|---------|--------------------------------------|
| Java  | 21+     | https://adoptium.net                 |
| Maven | 3.8+    | https://maven.apache.org             |

At least one API key is needed. Google Gemini is the default and is free to start with.

### 1. Set API Keys

```bash
# Pick the providers you want (at minimum one)
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
# Google Gemini key is pre-configured for quick testing
```

Or edit `src/main/resources/application.properties`:

```properties
spring.ai.openai.api-key=sk-your-key-here
spring.ai.anthropic.api-key=sk-ant-your-key-here
```

### 2. Build

```bash
mvn clean package -DskipTests
```

### 3. Run

```bash
mvn spring-boot:run
# or
java -jar target/llmate.jar
```

LLMate starts at **http://localhost:8080**. You should see:

```
+======================================================+
|         LLMate - Universal AI Gateway                 |
|         The LiteLLM for Java                          |
|         Starting on http://localhost:8080             |
+======================================================+
```

### 4. Verify

```bash
curl http://localhost:8080/api/v1/health
```

Expected output:

```json
{
  "status": "UP",
  "application": "LLMate",
  "availableProviders": 3,
  "totalProviders": 4
}
```

---

## API Reference

### POST /api/v1/chat — Blocking Chat

```bash
curl -X POST http://localhost:8080/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fast",
    "messages": [
      {"role": "system",  "content": "You are a helpful Java tutor."},
      {"role": "user",    "content": "What is a record in Java 21?"}
    ]
  }'
```

**Model routing formats:**

| `model` value                           | Routes to                            |
|-----------------------------------------|--------------------------------------|
| `"fast"`                                | alias → `openai/gpt-4o-mini`          |
| `"smart"`                               | alias → `anthropic/claude-3-5-sonnet` |
| `"local"`                               | alias → `ollama/llama3.2`            |
| `"openai/gpt-4o"`                       | LiteLLM shorthand (explicit)         |
| `"gpt-4o"` (no provider prefix)         | Auto-detected → `openai`            |
| `"gemini-2.0-flash"` (no prefix)        | Auto-detected → `googlegenai`       |
| `null` / omitted                        | uses global default                  |

### POST /api/v1/chat/stream — SSE Plain Text

```bash
curl -N -X POST http://localhost:8080/api/v1/chat/stream \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"model":"smart","messages":[{"role":"user","content":"Tell me a short story"}]}'
```

Output: `data: Once\ndata:  upon\ndata:  a\ndata:  time...`

### POST /api/v1/chat/stream/json — SSE with JSON Metadata

Each SSE event includes provider, model, and done flag:

```
data: {"id":"abc123","provider":"openai","model":"gpt-4o-mini","delta":"Hello","done":false}
data: {"id":"abc123","provider":"openai","model":"gpt-4o-mini","delta":"!","done":true}
```

### POST /api/v1/embed — Text Embeddings

```bash
curl -X POST http://localhost:8080/api/v1/embed \
  -H "Content-Type: application/json" \
  -d '{"provider":"openai","model":"text-embedding-3-small","inputs":["Hello world"]}'
```

### POST /api/v1/images/generate — Image Generation

```bash
curl -X POST http://localhost:8080/api/v1/images/generate \
  -H "Content-Type: application/json" \
  -d '{"provider":"openai","prompt":"a cat in space","size":"1024x1024"}'
```

### POST /api/v1/audio/tts — Text-to-Speech

```bash
curl -X POST http://localhost:8080/api/v1/audio/tts \
  -H "Content-Type: application/json" \
  -d '{"provider":"openai","input":"Hello from LLMate","voice":"alloy"}' \
  --output speech.mp3
```

### POST /api/v1/moderation — Content Safety

```bash
curl -X POST http://localhost:8080/api/v1/moderation \
  -H "Content-Type: application/json" \
  -d '{"provider":"openai","input":"some text to check"}'
```

### POST /api/v1/rag/ingest — Document Ingestion (RAG)

```bash
curl -X POST http://localhost:8080/api/v1/rag/ingest \
  -H "Content-Type: application/json" \
  -d '{"documentId":"doc-1","title":"My Document","content":"Full text here..."}'
```

### GET /api/v1/providers — List Active Providers

### GET /api/v1/models — Routing Table (aliases, defaults, fallbacks)

### GET /api/v1/health — Gateway Health Summary

---

## Configuration

All settings live in `src/main/resources/application.properties`.

### Model Aliases

Map friendly names to any provider/model. No code changes needed:

```properties
llmate.routing.aliases.fast=openai/gpt-4o-mini
llmate.routing.aliases.smart=anthropic/claude-3-5-sonnet-20241022
llmate.routing.aliases.local=ollama/llama3.2
llmate.routing.aliases.powerful=openai/gpt-4o
llmate.routing.aliases.code=ollama/codellama
llmate.routing.aliases.deepseek=deepseek/deepseek-chat
```

### Default Routing

```properties
llmate.routing.default-provider=googlegenai
llmate.routing.default-model=gemini-2.5-flash-lite
```

### Fallback Chain

```properties
llmate.routing.fallbacks[0]=openai/gpt-4o-mini
llmate.routing.fallbacks[1]=anthropic/claude-3-5-haiku-20241022
llmate.routing.fallbacks[2]=ollama/llama3.2
```

### Provider Toggles

```properties
llmate.providers.openai.enabled=true
llmate.providers.anthropic.enabled=true
llmate.providers.ollama.enabled=true
llmate.providers.mistral.enabled=false
llmate.providers.groq.enabled=false
llmate.providers.googlegenai.enabled=true
```

### Resilience

```properties
llmate.resilience.retry-max-attempts=3
llmate.resilience.retry-wait-duration=PT1S
llmate.resilience.circuit-breaker-enabled=true
llmate.resilience.failure-rate-threshold=50
llmate.resilience.wait-duration-in-open-state=PT30S
```

### Environment Variables

| Variable             | Required | Description                          |
|----------------------|----------|--------------------------------------|
| `OPENAI_API_KEY`     | If using OpenAI | OpenAI API key                |
| `ANTHROPIC_API_KEY`  | If using Anthropic | Anthropic API key          |
| `GROQ_API_KEY`       | If using Groq | Groq API key                    |
| `DEEPSEEK_API_KEY`   | If using DeepSeek | DeepSeek API key            |
| `MISTRAL_API_KEY`    | If using Mistral | Mistral API key              |
| `PERPLEXITY_API_KEY` | If using Perplexity | Perplexity API key        |
| `NVIDIA_API_KEY`     | If using NVIDIA | NVIDIA NIM API key            |
| `HUGGINGFACE_API_KEY`| If using HuggingFace | HuggingFace token        |

---

## Using Ollama (Free Local Models)

```bash
# 1. Install
brew install ollama           # macOS
# or download from https://ollama.ai

# 2. Start
ollama serve

# 3. Pull models
ollama pull llama3.2          # 3B — fast, great for most tasks
ollama pull nomic-embed-text  # Embeddings (for /api/v1/embed)
ollama pull codellama         # Code-focused
ollama pull phi3              # Microsoft 3.8B — small but capable

# 4. Use it
curl -X POST http://localhost:8080/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Hello from Ollama!"}]}'
```

Or use Docker:

```bash
docker compose up -d
# Automatically pulls llama3.2 + nomic-embed-text on first start
```

---

## Architecture

```
                     ┌──────────────────────────┐
  HTTP Request ────> │     LlmController        │  REST API endpoints
                     │     /api/v1/*             │
                     └─────────┬────────────────┘
                               │
                     ┌─────────▼────────────────┐
                     │      LlmGateway           │  Central orchestrator
                     │  (pre-filters → route →   │
                     │   retry → call → post)    │
                     └─────────┬────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐ ┌──────▼──────┐ ┌───────▼──────┐
     │ AuditLogging  │ │   Metrics   │ │    Retry     │
     │   Filter      │ │   Filter    │ │   Filter     │
     │  (order=5)    │ │  (order=10) │ │  (order=50)  │
     └────────┬──────┘ └──────┬──────┘ └───────┬──────┘
              └────────────────┼────────────────┘
                               │
                     ┌─────────▼────────────────┐
                     │       LlmRouter           │  Alias → Shorthand →
                     │  (5-step resolution)      │  Explicit → Fallback →
                     │                           │  Default
                     └─────────┬────────────────┘
                               │
                     ┌─────────▼────────────────┐
                     │   ProviderRegistry        │  Auto-discovers all
                     │   (Spring IoC)            │  @Component adapters
                     └─────────┬────────────────┘
                               │
       ┌──────────┬────────────┼──────────┬──────────┐
       │          │            │          │          │
   ┌───▼───┐ ┌───▼────┐ ┌────▼───┐ ┌────▼───┐ ┌───▼────────┐
   │OpenAI │ │Anthropic│ │Ollama  │ │Google  │ │OpenAI-Compat│
   │Adapter│ │Adapter  │ │Adapter │ │GenAI   │ │(Groq, etc.) │
   └───────┘ └────────┘ └────────┘ └────────┘ └─────────────┘
```

### Request Pipeline

1. **Pre-filters** run in order: audit logging (MDC context), metrics start, retry setup
2. **LlmRouter** resolves the `model` field through 5 steps: LiteLLM shorthand → named alias → explicit provider/model → fallback chain → global default
3. **Smart auto-detection** deduces provider from model name (`"gpt-4o"` → openai, `"claude-3"` → anthropic, `"gemini"` → googlegenai)
4. **Resilience4j Retry** wraps the provider call with configurable retry + circuit breaker
5. **Provider adapter** makes the actual API call (Spring AI for native providers, HTTP client for OpenAI-compatible)
6. **Post-filters** record latency, token counts, and completion status
7. **Streaming** uses Project Reactor `Flux<LlmStreamChunk>` with automatic fallback on stream failure

### Project Structure

```
src/main/java/com/llmate/
├── LLMateApplication.java          @SpringBootApplication entry point
├── controller/
│   └── LlmController.java          REST API (all /api/v1/* endpoints)
├── gateway/
│   └── LlmGateway.java             Central orchestrator — inject this bean
├── routing/
│   ├── LlmRouter.java              5-step model resolution
│   └── ProviderResolution.java      Resolution result (adapter + provider + model)
├── provider/
│   ├── LlmProviderAdapter.java      SPI interface — implement to add providers
│   ├── ProviderRegistry.java        Auto-discovers @Component adapters
│   ├── openai/                      Native Spring AI: OpenAI
│   ├── anthropic/                   Native Spring AI: Anthropic
│   ├── ollama/                      Native Spring AI: Ollama
│   ├── mistral/                     Native Spring AI: Mistral
│   ├── googlegenai/                 OpenAI-compat: Google Gemini
│   ├── groq/                        OpenAI-compat: Groq
│   ├── deepseek/                    OpenAI-compat: DeepSeek
│   ├── perplexity/                  OpenAI-compat: Perplexity
│   ├── nvidia/                      OpenAI-compat: NVIDIA NIM
│   ├── huggingface/                 OpenAI-compat: HuggingFace
│   ├── cohere/                      OpenAI-compat: Cohere
│   └── openaicompat/                Base class for OpenAI-compatible providers
├── filter/
│   ├── LlmRequestFilter.java        Filter interface (ordered pipeline)
│   ├── AuditLoggingFilter.java       MDC + structured logging (order=5)
│   ├── MetricsFilter.java            Micrometer/Prometheus metrics (order=10)
│   └── RetryFilter.java              Resilience4j retry wrapper (order=50)
├── model/                            Unified request/response types (18 classes)
├── dto/                              JSON API shapes (12 classes)
├── config/
│   ├── LlmateProperties.java         All llmate.* config bindings
│   ├── LlmateHealthIndicator.java     /actuator/health integration
│   └── CorsConfig.java               CORS for frontend
├── memory/
│   └── LlmChatMemoryService.java      In-memory chat session management
├── tool/
│   └── LlmToolCallingService.java     Function/tool calling support
├── rag/
│   └── LlmRagService.java             PGVector-based RAG pipeline
├── mcp/
│   └── LlmMcpClientConfig.java        Model Context Protocol integration
├── exception/                          Typed exceptions (auth, rate-limit, no-provider)
└── advice/
    └── GlobalExceptionHandler.java     @ControllerAdvice error mapping
```

---

## Adding a Custom Provider

Implement `LlmProviderAdapter`, annotate with `@Component`, done:

```java
@Component
@ConditionalOnProperty(name = "llmate.providers.myai.enabled", havingValue = "true")
public class MyAiAdapter implements LlmProviderAdapter {

    @Override public String providerId()  { return "myai"; }
    @Override public String displayName() { return "My Custom AI"; }
    @Override public Set<LlmCapability> capabilities() {
        return Set.of(LlmCapability.CHAT);
    }
    @Override public LlmChatResponse chat(LlmChatRequest request) {
        String content = callMyApi(request.messages());
        return new LlmChatResponse(/* ... */);
    }
}
```

```properties
llmate.providers.myai.enabled=true
llmate.routing.aliases.mymodel=myai/my-model-v1
```

For providers with an OpenAI-compatible API, extend `OpenAiCompatibleProviderAdapter` — streaming and chat are handled automatically.

---

## Observability

### Prometheus Metrics

All metrics available at `GET /actuator/prometheus`:

```promql
# Requests per second by provider
rate(llmate_chat_requests_total[5m])

# P99 latency
histogram_quantile(0.99, rate(llmate_chat_latency_seconds_bucket[5m]))

# Total tokens today
increase(llmate_tokens_prompt_total[24h]) + increase(llmate_tokens_completion_total[24h])

# Error rate
rate(llmate_errors_total[5m])
```

### Structured Logging

Every request/response logs with MDC context:

```
10:15:30.421 INFO  com.llmate.filter.AuditLoggingFilter -- LLMate > Request  | provider=unresolved model=fast messages=2
10:15:31.883 INFO  com.llmate.filter.AuditLoggingFilter -- LLMate < Response | provider=openai model=gpt-4o-mini tokens=123 duration=1462ms
```

### Actuator Endpoints

| Endpoint               | Description                         |
|------------------------|-------------------------------------|
| `/actuator/health`     | Full health with provider status    |
| `/actuator/prometheus` | Prometheus scrape target            |
| `/actuator/metrics`    | Spring Boot metrics explorer        |
| `/actuator/env`        | Environment properties              |
| `/actuator/loggers`    | Runtime log level management        |

---

## Running Tests

```bash
# All tests (no API keys needed — providers disabled in test profile)
mvn test

# Specific test class
mvn test -Dtest=LLMateApplicationTests
```

---

## Deployment

```bash
# Build the fat JAR
mvn clean package -DskipTests

# Run anywhere with Java 21+
java -jar target/llmate.jar
```

The JAR is self-contained with an embedded Tomcat server. Set environment variables for API keys and override any `llmate.*` property via standard Spring Boot mechanisms (`--server.port=9090`, env vars, external config files).

---

## Tech Stack

| Layer        | Technology                              |
|--------------|-----------------------------------------|
| Runtime      | Java 21, Spring Boot 3.3.4              |
| AI Framework | Spring AI 1.0.0-M6 (OpenAI, Anthropic, Ollama, Mistral starters) |
| Streaming    | Project Reactor (Flux)                  |
| Resilience   | Resilience4j 2.2.0 (retry + circuit breaker) |
| Metrics      | Micrometer + Prometheus Registry        |
| RAG          | PGVector Store (optional)               |
| Build        | Maven, single module                    |

---

## Known Limitations

- PGVector RAG requires a PostgreSQL database with the `pgvector` extension. Excluded by default via `@SpringBootApplication(exclude = ...)`.
- Ollama must be running locally (or via Docker) before LLMate starts for `ollama` provider to report as available.
- MCP (Model Context Protocol) integration is experimental.
- No built-in authentication. Add Spring Security or an API gateway in front for production use.

---

## License

Apache 2.0 — free to use, modify, and redistribute.

---

*LLMate — https://llmate.com*
