# goai

> A simple, modern, and reliable Go library for interacting with multiple LLM providers

## Features

- **Simple API** - One client, one method: `client.Chat(ctx, prompt)`
- **Context Support** - Built-in timeout and cancellation handling
- **7 Providers** - OpenAI, Anthropic, Google, xAI, Mistral, Perplexity, Ollama
- **Options Pattern** - Flexible configuration with sensible defaults
- **Zero Dependencies** - Standard library only
- **Type-Safe Errors** - Custom error types with provider context
- **Automatic Registration** - Providers self-register via init()

## Installation

```bash
go get github.com/dariubs/goai
```

## Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/dariubs/goai"
)

func main() {
    // Create a client for OpenAI
    client, err := goai.New("openai", "gpt-4o",
        goai.WithAPIKey(os.Getenv("OPENAI_API_KEY")),
    )
    if err != nil {
        log.Fatal(err)
    }

    // Create a context with timeout
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    // Send a prompt
    response, err := client.Chat(ctx, "What is the capital of France?")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(response.Content)
    fmt.Printf("Tokens used: %d\n", response.TokensUsed)
    fmt.Printf("Latency: %dms\n", response.LatencyMs)
}
```

## Supported Providers

### OpenAI
- **Provider:** `openai`
- **Models:** `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `gpt-3.5-turbo`
- **API Key:** `OPENAI_API_KEY`

```go
client, _ := goai.New("openai", "gpt-4o",
    goai.WithAPIKey(os.Getenv("OPENAI_API_KEY")),
)
```

### Anthropic
- **Provider:** `anthropic`
- **Models:** `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`, `claude-3-opus-20240229`
- **API Key:** `ANTHROPIC_API_KEY`

```go
client, _ := goai.New("anthropic", "claude-3-5-sonnet-20241022",
    goai.WithAPIKey(os.Getenv("ANTHROPIC_API_KEY")),
)
```

### Google Gemini
- **Provider:** `google`
- **Models:** `gemini-2.0-flash-exp`, `gemini-1.5-pro`, `gemini-1.5-flash`
- **API Key:** `GOOGLE_API_KEY`

```go
client, _ := goai.New("google", "gemini-2.0-flash-exp",
    goai.WithAPIKey(os.Getenv("GOOGLE_API_KEY")),
)
```

### xAI
- **Provider:** `xai`
- **Models:** `grok-2-1212`, `grok-beta`
- **API Key:** `XAI_API_KEY`

```go
client, _ := goai.New("xai", "grok-2-1212",
    goai.WithAPIKey(os.Getenv("XAI_API_KEY")),
)
```

### Mistral
- **Provider:** `mistral`
- **Models:** `mistral-large-latest`, `mistral-small-latest`, `pixtral-12b-2409`
- **API Key:** `MISTRAL_API_KEY`

```go
client, _ := goai.New("mistral", "mistral-large-latest",
    goai.WithAPIKey(os.Getenv("MISTRAL_API_KEY")),
)
```

### Perplexity
- **Provider:** `perplexity`
- **Models:** `llama-3.1-sonar-large-128k-online`, `llama-3.1-sonar-small-128k-online`
- **API Key:** `PERPLEXITY_API_KEY`

```go
client, _ := goai.New("perplexity", "llama-3.1-sonar-large-128k-online",
    goai.WithAPIKey(os.Getenv("PERPLEXITY_API_KEY")),
)
```

### Ollama
- **Provider:** `ollama`
- **Models:** `llama3.2`, `qwen2.5`, `deepseek-r1` (any Ollama model)
- **Endpoint:** `OLLAMA_HOST` (default: `http://localhost:11434`)

```go
client, _ := goai.New("ollama", "llama3.2",
    goai.WithEndpoint("http://localhost:11434"),
)
```

## Configuration Options

### WithAPIKey
Set the API key for the provider:

```go
goai.WithAPIKey("your-api-key")
```

### WithEndpoint
Set a custom API endpoint:

```go
goai.WithEndpoint("https://custom-endpoint.com/v1/chat")
```

### WithTimeout
Set the request timeout (default: 60s):

```go
goai.WithTimeout(30 * time.Second)
```

### WithMaxTokens
Set the maximum tokens in the response (default: 500):

```go
goai.WithMaxTokens(1000)
```

### WithTemperature
Set the temperature for randomness (default: 0.7):

```go
goai.WithTemperature(0.9)
```

## Error Handling

goai provides typed errors for better error handling:

```go
response, err := client.Chat(ctx, "Hello!")
if err != nil {
    // Check for specific error types
    var goaiErr *goai.Error
    if errors.As(err, &goaiErr) {
        fmt.Printf("Provider: %s\n", goaiErr.Provider)
        fmt.Printf("Status: %d\n", goaiErr.StatusCode)
        fmt.Printf("Message: %s\n", goaiErr.Message)
    }
    
    // Check for sentinel errors
    if errors.Is(err, goai.ErrNoAPIKey) {
        log.Fatal("API key is required")
    }
    if errors.Is(err, goai.ErrProviderNotFound) {
        log.Fatal("Provider not registered")
    }
}
```

### Sentinel Errors

- `ErrNoAPIKey` - API key is required but not provided
- `ErrNoResponse` - Provider returned no response
- `ErrProviderNotFound` - Provider is not registered
- `ErrInvalidModel` - Model identifier is invalid

## Advanced Usage

### Multiple Providers

```go
providers := []struct {
    name  string
    model string
    key   string
}{
    {"openai", "gpt-4o", os.Getenv("OPENAI_API_KEY")},
    {"anthropic", "claude-3-5-sonnet-20241022", os.Getenv("ANTHROPIC_API_KEY")},
    {"google", "gemini-2.0-flash-exp", os.Getenv("GOOGLE_API_KEY")},
}

for _, p := range providers {
    client, err := goai.New(p.name, p.model, goai.WithAPIKey(p.key))
    if err != nil {
        continue
    }
    
    response, err := client.Chat(ctx, "Hello!")
    if err != nil {
        continue
    }
    
    fmt.Printf("%s: %s\n", p.name, response.Content)
}
```

### Context Cancellation

```go
ctx, cancel := context.WithCancel(context.Background())

go func() {
    time.Sleep(5 * time.Second)
    cancel() // Cancel after 5 seconds
}()

response, err := client.Chat(ctx, "Long running prompt...")
if err != nil {
    if ctx.Err() == context.Canceled {
        fmt.Println("Request was cancelled")
    }
}
```

### List Available Providers

```go
providers := goai.ListProviders()
fmt.Println("Available providers:", providers)
// Output: Available providers: [openai anthropic google xai mistral perplexity ollama]
```

## Response Structure

```go
type Response struct {
    Content    string                 // The response text
    TokensUsed int                    // Number of tokens used (if available)
    LatencyMs  int64                  // Response latency in milliseconds
    Model      string                 // Model identifier
    Provider   string                 // Provider name
    Metadata   map[string]interface{} // Additional metadata
}
```

## Adding New Providers

To add a new LLM provider:

1. Create a new file (e.g., `newprovider.go`)
2. Implement the internal `Provider` interface
3. Register in `init()` function

```go
package goai

import (
    "context"
    "time"
)

func init() {
    register("newprovider", newNewProvider)
}

type newProvider struct {
    apiKey string
    model  string
}

func newNewProvider(model string, opts Options) (Provider, error) {
    if opts.APIKey == "" {
        return nil, fmt.Errorf("%w: newprovider", ErrNoAPIKey)
    }
    
    return &newProvider{
        apiKey: opts.APIKey,
        model:  model,
    }, nil
}

func (p *newProvider) chat(ctx context.Context, prompt string, opts Options) (*Response, error) {
    start := time.Now()
    
    // Make API request here
    // ...
    
    return &Response{
        Content:    "response content",
        TokensUsed: 100,
        LatencyMs:  time.Since(start).Milliseconds(),
        Model:      p.model,
        Provider:   "newprovider",
    }, nil
}

func (p *newProvider) name() string {
    return "newprovider"
}

func (p *newProvider) model() string {
    return p.model
}
```

## Design Principles

1. **Simplicity** - Minimal API surface, easy to understand
2. **Reliability** - Proper error handling, context support
3. **Flexibility** - Options pattern for configuration
4. **Zero Dependencies** - Only standard library
5. **Consistency** - All providers work the same way

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

