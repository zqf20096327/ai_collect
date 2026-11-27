English | [简体中文](https://github.com/cnblogs/dashscope-sdk/blob/main/README.zh-Hans.md)

# Cnblogs.DashScopeSDK

[![NuGet Version](https://img.shields.io/nuget/v/Cnblogs.DashScope.AI?style=flat&logo=nuget&label=Cnblogs.DashScope.AI)](https://www.nuget.org/packages/Cnblogs.DashScope.AI)
[![NuGet Version](https://img.shields.io/nuget/v/Cnblogs.DashScope.Sdk?style=flat&logo=nuget&label=Cnblogs.DashScope.Sdk&link=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FCnblogs.DashScope.Sdk)](https://www.nuget.org/packages/Cnblogs.DashScope.Sdk)
[![NuGet Version](https://img.shields.io/nuget/v/Cnblogs.DashScope.AspNetCore?style=flat&logo=nuget&label=Cnblogs.DashScope.AspNetCore&link=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FCnblogs.DashScope.AspNetCore)](https://www.nuget.org/packages/Cnblogs.DashScope.AspNetCore)

A non-official DashScope (Bailian) service SDK maintained by Cnblogs.

**Note:** This project is actively under development. Breaking changes may occur even in minor versions. Please review the Release Notes before upgrading.

## Quick Start

### Console Application

Install NuGet package `Cnblogs.DashScope.Sdk`
```csharp
// The SDK defaults to the Beijing region, pass region if your API key belongs to another region
var client = new DashScopeClient("your-api-key", region: DashScopeRegion.Singapore);
var completion = await client.GetTextCompletionAsync(
    new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
    {
        Model = "qwen-turbo",
        Input = new TextGenerationInput()
        {
            Messages = new List<TextChatMessage>()
            {
                TextChatMessage.System("You are a helpful assistant"),
                TextChatMessage.User("你是谁？")
            }
        },
        Parameters = new TextGenerationParameters() { ResultFormat = "message" }
    });
Console.WriteLine(completion.Output.Choices![0].Message.Content)
```

### ASP.NET Core Application

Install NuGet package `Cnblogs.DashScope.AspNetCore`

`Program.cs`
```csharp
builder.AddDashScopeClient(builder.Configuration);
```

`appsettings.json`

```json
{
    "DashScope": {
        "ApiKey": "your-api-key",
        "RegionId": "ap-southeast-1"
    }
}
```

Application class:

```csharp
public class YourService(IDashScopeClient client)
{
    public async Task<string> CompletePromptAsync(string prompt)
    {
    	var completion = await client.GetTextCompletionAsync(
        new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
        {
            Model = "qwen-turbo",
            Input = new TextGenerationInput()
            {
                Messages = new List<TextChatMessage>()
                {
                    TextChatMessage.System("You are a helpful assistant"),
                    TextChatMessage.User("你是谁？")
                }
            },
            Parameters = new TextGenerationParameters() { ResultFormat = "message" }
        });
		return completion.Output.Choices![0].Message.Content
    }
}
```
### Using `Microsoft.Extensions.AI` Interface

Install NuGet package `Cnblogs.DashScope.AI`

```csharp
var client = new DashScopeClient("your-api-key", region: DashScopeRegion.Singapore).AsChatClient("qwen-max");
var completion = await client.GetResponseAsync("hello");
Console.WriteLine(completion.Text);
```

`IChatClient` picks the endpoint and the max token parameter by the model of each request (`ChatOptions.ModelId`, or the model passed to `AsChatClient()`):

- Endpoint: the models of the multimodal whitelist (qwen3.5 / qwen3.6 series, qwen3.7-plus / qwen3.7-flash, qwen3.8 and later series, qwen3-vl, qwen3-omni, gui-plus, kimi-k2.5 and later kimi models, deepseek-v4.1 and later deepseek models) are called via the multimodal API (`MultimodalParameters`), all the other models (e.g. qwen-plus, qwen-max, qwen3.7-max, deepseek-v4-pro, glm-5.3) via the text API (`TextGenerationParameters`), including the models supplied directly by third parties (e.g. `xiaomi/mimo-v2.6-pro-ultraspeed`) even when they accept images. Calling the wrong one fails with 400 "url error", and the endpoint does not follow the model version: qwen3.7-max is a text model, qwen3.8-max is a multimodal one.
- `ChatOptions.MaxOutputTokens` is sent as `max_completion_tokens` for the models that read it (qwen3.5 and later series, qwen-mt, tongyi-xiaomi-analysis, deepseek-v4-pro and later deepseek models, glm-5.x, kimi-k2.5 and later kimi models, MiniMax-M2.5), which limits the reasoning output and the answer together. It is sent as `max_tokens` for all the other models (e.g. qwen-plus, qwen-max, qwen3-vl-plus, gui-plus), because they silently ignore `max_completion_tokens`; `max_tokens` limits the answer only on thinking models.

Set `AdditionalProperties["useVl"]` / `AdditionalProperties["useMaxCompletionTokens"]` to `true` / `false` to force the mapping, e.g. when a new model appears before the whitelist is updated.

The endpoint can also be fixed for every request of a chat client: `AsChatClient(modelId, useVl)` takes a non-nullable `bool`, `true` for the multimodal API and `false` for the text API. Leave the argument out, or pass `null` as the options of `AsChatClient(modelId, options)`, to decide it by the model.

The endpoint whitelist is shipped with the SDK, so it can lag behind the models the service releases. To pick the endpoint by what the service reports instead, turn on `AutoSyncModelList` through `AsChatClient(modelId, options)`: a model is looked up in the [model list](#model-list) (`GET /api/v1/models?model=<modelId>`) the first time it is used, and it goes to the multimodal API when the service lists it with the `VU` or `Multimodal-Omni` capability and Bailian hosts it (except for `qwen3.8-2.4t-a95b`: the service lists it as a text model although the multimodal API serves it, the SDK corrects that). The looked up models are cached for the lifetime of the process and shared by every chat client of it, so each model costs one extra request per process. When the service does not list the model, or the lookup fails, the chat requests go on with the whitelist and the model is not looked up again for a minute. Nothing is requested when the option is off, or when `useVl` already decides the endpoint.

```csharp
var chatClient = dashScopeClient.AsChatClient(
    "qwen3.7-plus",
    new DashScopeChatClientOptions(AutoSyncModelList: true));
```

#### ToolCall

```csharp
var chatClient = client.AsChatClient("qwen-turbo").AsBuilder().UseFunctionInvocation().Build();
var options = new ChatOptions()
{
    Tools = [AIFunctionFactory.Create(GetWeather)],
    ToolMode = new AutoChatToolMode(),
    AllowMultipleToolCalls = true,
};
var stream = chatClient.GetStreamingResponseAsync("What's weather today?", options);
await foreach (var chatResponseUpdate in stream)
{
    Console.Write(chatResponseUpdate);
}
```

#### Fallback to raw messages

If you need to use input data or parameters not supported by `Microsoft.Extensions.AI`, you can directly invoke the underlying SDK by passing a raw `TextChatMessage` or `MultimodalMessage` via `RawRepresentation`.

Similarly, to pass unsupported parameters, you can also do so directly by setting the `raw` property within `AdditionalProperties`.

Example(Using `qwen-doc-turbo`)

```csharp
var messages = new List<TextChatMessage>()
{
    TextChatMessage.DocUrl(
        "从这两份产品手册中，提取所有产品信息，并整理成一个标准的JSON数组。每个对象需要包含：model(产品的型号)、name(产品的名称)、price(价格（去除货币符号和逗号）)",
        [
            "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251107/jockge/%E7%A4%BA%E4%BE%8B%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8CA.docx",
            "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251107/ztwxzr/%E7%A4%BA%E4%BE%8B%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8CB.docx"
        ])
};
var parameters = new TextGenerationParameters()
{
    ResultFormat = "message", IncrementalOutput = true,
};

var response = client
    .AsChatClient("qwen-doc-turbo")
    .GetStreamingResponseAsync(
        messages.Select(x => new ChatMessage() { RawRepresentation = x }),
        new ChatOptions()
        {
            AdditionalProperties = new AdditionalPropertiesDictionary() { { "raw", parameters } }
        });
await foreach (var chunk in response)
{
    Console.Write(chunk.Text);
}
```

Similarly, you can also retrieve the raw message from the `RawRepresentation` in the message returned by the model.

Example (Getting the token count for an image when calling `qwen3-vl-plus`):

```csharp
var response = client
    .AsChatClient("qwen3-vl-plus")
    .GetStreamingResponseAsync(
        new List<ChatMessage>()
        {
            new(
                ChatRole.User,
                new List<AIContent>()
                {
                    new UriContent(
                        "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg",
                        MediaTypeNames.Image.Jpeg),
                    new UriContent(
                        "https://dashscope.oss-cn-beijing.aliyuncs.com/images/tiger.png",
                        MediaTypeNames.Image.Jpeg),
                    new TextContent("这些图展现了什么内容？")
                })
        },
        new ChatOptions());
var lastChunk = (ChatResponseUpdate?)null;
await foreach (var chunk in response)
{
    Console.Write(chunk.Text);
    lastChunk = chunk;
}

Console.WriteLine();

// Access underlying raw response
var raw = lastChunk?.RawRepresentation as ModelResponse<MultimodalOutput, MultimodalTokenUsage>;
Console.WriteLine($"Image token usage: {raw?.Usage?.ImageTokens}");
```

## Workspace and Region

Bailian serves different regions with different endpoints. The SDK defaults to the Beijing region (`cn-beijing`). If your API key belongs to another region, specify it via the `region` parameter (or `RegionId` in configuration):

| `DashScopeRegion` | Region ID | Endpoint without workspace |
| ----------------- | --------- | -------------------------- |
| `Beijing` (default) | `cn-beijing` | `https://dashscope.aliyuncs.com` |
| `Singapore` | `ap-southeast-1` | `https://dashscope-intl.aliyuncs.com` |
| `HongKong` | `cn-hongkong` | `https://cn-hongkong.dashscope.aliyuncs.com` |
| `UsEast` | `us-east-1` | workspace required |
| `Germany` | `eu-central-1` | workspace required |
| `Japan` | `ap-northeast-1` | workspace required |

Console application:

```csharp
var client = new DashScopeClient("your-api-key", region: DashScopeRegion.Singapore);
```

ASP.NET Core:

```csharp
builder.Services.AddDashScopeClient("your-api-key", region: DashScopeRegion.Singapore);
```

### Workspace

If you are using a Bailian workspace (业务空间), pass the workspace id together with its region. The SDK then switches to the workspace-specific endpoint `{workspaceId}.{regionId}.maas.aliyuncs.com` and appends the `X-DashScope-WorkSpace` header automatically. Note that the `UsEast`, `Germany` and `Japan` regions do not provide a shared endpoint, a workspace id is required for them:

```csharp
var client = new DashScopeClient(
    "your-api-key",
    workspaceId: "your-workspace-id",
    region: DashScopeRegion.Singapore);
// requests are sent to https://{workspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1/
```

`appsettings.json`

```json
{
    "DashScope": {
        "ApiKey": "your-api-key",
        "WorkspaceId": "your-workspace-id",
        "RegionId": "ap-southeast-1"
    }
}
```

If you access Bailian through a proxy, set `BaseAddress`/`WebsocketBaseAddress` (or the `baseAddress` parameter) instead. An explicit base address always takes precedence over region and workspace.

### Content Inspection (AI Safety Guardrail)

Bailian supports the `X-DashScope-DataInspection` request header, which further inspects input and output content for violations using the AI safety guardrail. The inspection is disabled by default (the header is not sent). The guardrail service needs to be enabled on your account first, otherwise the API returns `403 Header.AccessDenied`. Not available for Qwen-Audio models.

Enable it for all requests on the client:

```csharp
// Console application
var client = new DashScopeClient("your-api-key")
{
    DataInspection = DataInspectionOptions.CipInputAndOutput
};

// ASP.NET Core
builder.Services.AddDashScopeClient("your-api-key");
builder.Services.Configure<DashScopeOptions>(o => o.DataInspection = DataInspectionOptions.CipInputAndOutput);
```

Or enable/override it on a single request:

```csharp
var completion = await client.GetTextCompletionAsync(new ModelRequest<TextGenerationInput, ITextGenerationParameters>
{
    Model = "qwen-plus",
    Input = new TextGenerationInput { Messages = new List<TextChatMessage> { TextChatMessage.User("你好") } },
    Parameters = new TextGenerationParameters { ResultFormat = "message" },
    DataInspection = DataInspectionOptions.CipInput
});
```

Available values are `Disabled` (default), `CipInput`, `CipOutput` and `CipInputAndOutput`. Request level configuration takes precedence over client level configuration, and setting `DataInspectionOptions.Disabled` on a request disables client level inspection for that request.

Client level configuration also applies to the WebSocket API (e.g. CosyVoice), which only supports enabling inspection for both directions at once, so any enabled direction turns on the `X-DashScope-DataInspection` header for WebSocket connections. The header is not sent by default. For a single WebSocket session, pass the `dataInspection` parameter when creating the session; when it differs from the client level configuration, a temporary connection is created for that session only and disposed afterwards.

## Supported APIs

- [Text Generation](#text-generation) - QWen3, DeepSeek, etc. Supports reasoning/tool calling/web search/translation scenarios
  - [Conversation](#conversation)
  - [Thinking Models](#thinking-models)
  - [Web Search](#web-search)
  - [Tool Calling](#tool-calling)
  - [Prefix Completion](#prefix-completion)
  - [Long Context (Qwen-Long)](#long-context-qwen-long)
  - [Code Interpreter](#code-interpreter)
  - [PPT Generation (Qwen-doc-turbo)](#ppt-generation-qwen-doc-turbo)
- [Multimodal](#multimodal) - QWen-VL, QVQ, etc. Supports reasoning/visual understanding/OCR/audio understanding
  - [Upload file for multimodal usage](#upload-file-for-multimodal-usage)
  - [Image Recognition/Thinking](#image-recognition/thinking)
  - [OCR](#ocr)
    - [Advanced Recognition](#advanced-recognition)
    - [Key Information Extraction](#key-information-extraction)
    - [Table Parsing](#table-parsing)
    - [Document Parsing](#document-parsing)
    - [Formula Recognition](#formula-recognition)
    - [Text Recognition](#text-recognition)
    - [Multilanguage](#multilanguage)
  - [GUI](#gui)
  - [Audio Understanding](#audio-understanding)
- [Text-to-Speech](#text-to-speech) - CosyVoice, Sambert, etc. For TTS applications
- [Real-Time Speech Recognition](#real-time-speech-recognition) - Paraformer, Qwen-Audio ASR. For streaming ASR applications
- [Recorded Speech Recognition](#recorded-speech-recognition) - qwen3-asr-flash, Fun-ASR-Flash, Qwen-Audio ASR. For recorded audio files
- [Image Generation](#image-generation) - qwen-image-2.0-pro, wanx2.1, etc. For text-to-image, image editing, portrait style transfer and image translation
- [Video Generation](#video-generation) - wan2.7/wan3.0, PixVerse, Kling, Vidu, etc. For text-to-video, image-to-video and video editing
- [3D Generation (Tripo)](#3d-generation-tripo) - Tripo-H3.1/P1.0 3D generation, Gaussian Splat, mesh post-processing and animation
- [Application Call](#application-call)
- [Batch](#batch)
- [Text Embeddings](#text-embeddings)
- [Multimodal Embedding](#multimodal-embedding) - tongyi-embedding-vision-plus/flash, qwen3-vl-embedding, qwen2.5-vl-embedding, multimodal-embedding-v1. For embedding texts, images and videos into one vector space
- [Text Rerank](#text-rerank) - qwen3-rerank, qwen3.7-text-rerank, gte-rerank-v2, qwen3-vl-rerank. For refining the documents recalled by a vector search
- [Omni-Modal Translation (Qwen-MT-Uni)](#omni-modal-translation-qwen-mt-uni) - qwen-mt-uni. For translating texts, documents, images and audio
- [Decision Model (System One)](#decision-model-system-one) - decision-model. For classification, yes/no judgement and scoring with a single forward pass, without generating text
- [Model List](#model-list) - Query the models of Bailian: capabilities, modalities, features, prices and token limits


## Text Generation

Use `dashScopeClient.GetTextCompletionAsync` and `dashScopeClient.GetTextCompletionStreamAsync()` to access text generation APIs.

Common models: `qwen-max` `qwen-plus` `qwen-flush` etc.

Basic example (see [Workspace and Region](#workspace-and-region) for client configuration):

```csharp
var client = new DashScopeClient("your-api-key", region: DashScopeRegion.Singapore);
var completion = await client.GetTextCompletionAsync(
    new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
    {
        Model = "qwen-turbo",
        Input = new TextGenerationInput()
        {
            Messages = new List<TextChatMessage>()
            {
                TextChatMessage.System("You are a helpful assistant"),
                TextChatMessage.User("Who are you?")
            }
        },
        Parameters = new TextGenerationParameters() { ResultFormat = "message" }
    });
Console.WriteLine(completion.Output.Choices![0].Message.Content)
```

### Conversation

#### Quick Start

The key is maintaining a `TextChatMessage` array as conversation history.

```csharp
var messages = new List<TextChatMessage>();
messages.Add(TextChatMessage.System("You are a helpful assistant"));
while (true)
{
    Console.Write("User > ");
    var input = Console.ReadLine();
    if (string.IsNullOrEmpty(input))
    {
        Console.WriteLine("Using default input: Who are you?");
        input = "Who are you?";
    }

    messages.Add(TextChatMessage.User(input));
    var completion = await client.GetTextCompletionAsync(
        new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
        {
            Model = "qwen-turbo",
            Input = new TextGenerationInput() { Messages = messages },
            Parameters = new TextGenerationParameters() { ResultFormat = "message" }
        });
    Console.WriteLine("Assistant > " + completion.Output.Choices![0].Message.Content);
    var usage = completion.Usage;
    if (usage != null)
    {
        Console.WriteLine($"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/total({usage.TotalTokens})");
    }

    messages.Add(TextChatMessage.Assistant(completion.Output.Choices[0].Message.Content));
}
```

### Thinking Models

The model's thinking process is stored in a separate `ReasoningContent` property. When saving to conversation history, ignore it and only keep the model's reply `Content`.

Some models accept `EnableThinking` to control deep thinking, which can be set in `Parameters`.

```csharp
var messages = new List<TextChatMessage>();
messages.Add(TextChatMessage.System("You are a helpful assistant"));
while (true)
{
    Console.Write("User > ");
    var input = Console.ReadLine();
    if (string.IsNullOrEmpty(input))
    {
        Console.WriteLine("Please enter a user input.");
        return;
    }

    messages.Add(TextChatMessage.User(input));
    var completion = await client.GetTextCompletionAsync(
        new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
        {
            Model = "qwen-turbo",
            Input = new TextGenerationInput() { Messages = messages },
            Parameters = new TextGenerationParameters() { ResultFormat = "message", EnableThinking = true }
        });
    Console.WriteLine("Reasoning > " + completion.Output.Choices![0].Message.ReasoningContent);
    Console.WriteLine("Assistant > " + completion.Output.Choices![0].Message.Content);
    var usage = completion.Usage;
    if (usage != null)
    {
        Console.WriteLine(
            $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/reasoning({usage.OutputTokensDetails?.ReasoningTokens})/total({usage.TotalTokens})");
    }

    messages.Add(TextChatMessage.Assistant(completion.Output.Choices[0].Message.Content));
}
```

#### Streaming Output

```cs
var request = new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
{
    Model = "qwen-turbo",
    Input = new TextGenerationInput() { Messages = messages },
    Parameters = new TextGenerationParameters()
    {
        ResultFormat = "message",
        EnableThinking = true,
        IncrementalOutput = true
    }
}
```

Use `client.GetTextCompletionStreamAsync` for streaming output. It's recommended to enable `IncrementalOutput` in `Parameters` for incremental output.

Incremental output:
> Example: ["I love","eating","apples"]

Non-incremental output:
> Example: ["I love","I love eating","I love eating apples"]

Streaming output returns an `IAsyncEnumerable`. Use `await foreach` to iterate, record incremental content, then save to conversation history.

var messages = new List<TextChatMessage>();
messages.Add(TextChatMessage.System("You are a helpful assistant"));
while (true)
{
    Console.Write("User > ");
    var input = Console.ReadLine();
    if (string.IsNullOrEmpty(input))
    {
        Console.WriteLine("Please enter a user input.");
        return;
    }

    messages.Add(TextChatMessage.User(input));
    var completion = client.GetTextCompletionStreamAsync(
        new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
        {
            Model = "qwen-turbo",
            Input = new TextGenerationInput() { Messages = messages },
            Parameters = new TextGenerationParameters()
            {
                ResultFormat = "message",
                EnableThinking = true,
                IncrementalOutput = true
            }
        });
    var reply = new StringBuilder();
    var reasoning = false;
    TextGenerationTokenUsage? usage = null;
    await foreach (var chunk in completion)
    {
        var choice = chunk.Output.Choices![0];
        if (string.IsNullOrEmpty(choice.Message.ReasoningContent) == false)
        {
            // reasoning
            if (reasoning == false)
            {
                Console.Write("Reasoning > ");
                reasoning = true;
            }

            Console.Write(choice.Message.ReasoningContent);
            continue;
        }

        if (reasoning)
        {
            reasoning = false;
            Console.WriteLine();
            Console.Write("Assistant > ");
        }

        Console.Write(choice.Message.Content);
        reply.Append(choice.Message.Content);
        usage = chunk.Usage;
    }

    Console.WriteLine();
    messages.Add(TextChatMessage.Assistant(reply.ToString()));
    if (usage != null)
    {
        Console.WriteLine(
            $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/reasoning({usage.OutputTokensDetails?.ReasoningTokens})/total({usage.TotalTokens})");
    }
}

#### Limiting Thinking Length

Use `ThinkingBudget` in `Parameters` to limit the model's thinking length.

```cs
const int budget = 10;
Console.WriteLine($"Set thinking budget to {budget} tokens");
var messages = new List<TextChatMessage>();
messages.Add(TextChatMessage.System("You are a helpful assistant"));
while (true)
{
    Console.Write("User > ");
    var input = Console.ReadLine();
    if (string.IsNullOrEmpty(input))
    {
        Console.WriteLine("Please enter a user input.");
        return;
    }

    messages.Add(TextChatMessage.User(input));
    var completion = client.GetTextCompletionStreamAsync(
        new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
        {
            Model = "qwen-turbo",
            Input = new TextGenerationInput() { Messages = messages },
            Parameters = new TextGenerationParameters()
            {
                ResultFormat = "message",
                EnableThinking = true,
                ThinkingBudget = budget,
                IncrementalOutput = true
            }
        });
    var reply = new StringBuilder();
    var reasoning = false;
    TextGenerationTokenUsage? usage = null;
    await foreach (var chunk in completion)
    {
        var choice = chunk.Output.Choices![0];
        if (string.IsNullOrEmpty(choice.Message.ReasoningContent) == false)
        {
            // reasoning
            if (reasoning == false)
            {
                Console.Write("Reasoning > ");
                reasoning = true;
            }

            Console.Write(choice.Message.ReasoningContent);
            continue;
        }

        if (reasoning)
        {
            reasoning = false;
            Console.WriteLine();
            Console.Write("Assistant > ");
        }

        Console.Write(choice.Message.Content);
        reply.Append(choice.Message.Content);
        usage = chunk.Usage;
    }

    Console.WriteLine();
    messages.Add(TextChatMessage.Assistant(reply.ToString()));
    if (usage != null)
    {
        Console.WriteLine(
            $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/reasoning({usage.OutputTokensDetails?.ReasoningTokens})/total({usage.TotalTokens})");
    }
}
```

### Web Search

Controlled mainly through `EnableSearch` and `SearchOptions` in `Parameters`.

Example request:

```cs
var request = new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
{
    Model = "qwen-turbo",
    Input = new TextGenerationInput() { Messages = messages },
    Parameters = new TextGenerationParameters()
    {
        ResultFormat = "message",
        EnableThinking = true,
        EnableSearch = true,
        SearchOptions = new TextGenerationSearchOptions()
        {
            SearchStrategy = "max", // max/turbo - controls number of search results
            EnableCitation = true,  // Add source citations to model reply
            CitationFormat = "[ref_<number>]", // Citation format
            EnableSource = true, // Return search source list in SearchInfo
            ForcedSearch = true, // Force model to search
            EnableSearchExtension = true, // Enable vertical domain search, results in SearchInfo.Extra
            PrependSearchResult = true // First packet contains only search results
        }
    }
};
```

### Tool Calling

Provide available tools to the model via `Tools` in `Parameters`. The model returns messages with `ToolCall` properties to invoke tools.

After receiving the message, the server needs to call the corresponding tools and insert results as `Tool` role messages into the conversation history before making another request. The model will summarize the tool call results.

By default, the model calls tools once per turn. To enable multiple tool calls, enable `ParallelToolCalls` in `Parameters`.

```
var tools = new List<ToolDefinition>
{
    new(
        ToolTypes.Function,
        new FunctionDefinition(
            nameof(GetWeather),
            "Get current weather",
            new JsonSchemaBuilder().FromType<WeatherReportParameters>().Build()))
};

var request = new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
{
    Model = "qwen-turbo",
    Input = new TextGenerationInput() { Messages = messages },
    Parameters = new TextGenerationParameters()
    {
        ResultFormat = "message",
        EnableThinking = true,
        IncrementalOutput = true,
        Tools = tools,
        ToolChoice = ToolChoice.AutoChoice,
        ParallelToolCalls = true // Model can call multiple tools at once
    }
}
```

### Structured Output (JSON Output)

Set `ResponseFormat` (remarks: **not** `ResultFormat`) in `Parameters` to JSON to force JSON output.

```csharp
var request = new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
{
    Model = "qwen-plus",
    Input = new TextGenerationInput() { Messages = messages },
    Parameters = new TextGenerationParameters()
    {
        ResultFormat = "message",
        ResponseFormat = DashScopeResponseFormat.JsonObject,
        IncrementalOutput = true
    }
}
```

To make the model strictly follow a given JSON Schema, use `DashScopeResponseFormat.JsonSchema()` with a `DashScopeJsonSchema` (`Strict` is recommended to be `true`).

```csharp
var request = new ModelRequest<MultimodalInput, IMultimodalParameters>()
{
    Model = "qwen3.8-flash",
    Input = new MultimodalInput() { Messages = messages },
    Parameters = new MultimodalParameters()
    {
        ResponseFormat = DashScopeResponseFormat.JsonSchema(new DashScopeJsonSchema(
            "calculation",
            new JsonObject
            {
                ["type"] = "object",
                ["properties"] = new JsonObject
                {
                    ["result"] = new JsonObject { ["type"] = "number" }
                },
                ["required"] = new JsonArray("result"),
                ["additionalProperties"] = false
            },
            Strict: true))
    }
}
```

Notes on using `json_schema`:

- Only a few models support `json_schema` (e.g. qwen3.7/qwen3.8 series). Check the [structured output doc](https://docs.bailian.console.aliyun.com/zh/model-studio/qwen-structured-output) before using it, otherwise fall back to `json_object`.
- Among them, qwen3.7-plus / qwen3.7-flash and the qwen3.8 series are called via the multimodal API (`MultimodalParameters`), while qwen3.7-max is called via the text API (`TextGenerationParameters`): the endpoint does not follow the model version.
- Unlike `json_object`, `json_schema` does not require the prompt to contain the word "json".
- In the `IChatClient` (Microsoft.Extensions.AI) integration, when `ChatResponseFormat.ForJsonSchema(...)` is used: whitelisted models (qwen3.7/qwen3.8 series) are automatically mapped to `json_schema`; other models fall back to `json_object` (the schema is ignored). Set `AdditionalProperties["useJsonSchema"]` to `true`/`false` to force the mapping (similar to `useVl`), e.g. when a new model supports `json_schema` before the whitelist is updated. `ChatResponseFormat.Json` is always mapped to `json_object`.

### Agents (Microsoft Agent Framework)

The `IChatClient` returned by `AsChatClient()` works with [Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-agent-framework-overview) (`Microsoft.Agents.AI` NuGet package). The agent keeps the conversation history itself and passes the agent-level persona via `ChatOptions.Instructions`, which this SDK maps to a leading system message; tool calls are executed by the agent loop automatically.

```csharp
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

var chatClient = dashScopeClient.AsChatClient("qwen-plus");
var agent = new ChatClientAgent(
    chatClient,
    instructions: "你是智能助理，可以查询天气和当前时间，回答要简洁。",
    name: "assistant",
    tools: [AIFunctionFactory.Create(GetWeather), AIFunctionFactory.Create(GetNow)]);

// The session carries the conversation history across runs.
var session = await agent.CreateSessionAsync();
while (true)
{
    Console.Write("User > ");
    var input = Console.ReadLine();
    if (string.IsNullOrEmpty(input))
    {
        return;
    }

    var response = await agent.RunAsync(input, session);
    Console.WriteLine($"Assistant > {response.Text}");
}
```

See `sample/Cnblogs.DashScope.Sample/MsExtensionsAI/AgentExample.cs` for a runnable sample. If you prefer no extra dependency, `ChatOptions.Instructions` + tool messages (`FunctionCallContent`/`FunctionResultContent`) are enough to build a minimal agent loop by hand, see [Tool Calling](#tool-calling).

### Prefix Completion

Place the prefix to complete as an `assistant` message at the end of the `messages` array with `Partial` set to `true`. The model will complete the remaining content based on this prefix.

Deep thinking cannot be enabled in this mode.

```cs
var messages = new List<TextChatMessage>
{
    TextChatMessage.User("Complete following C# method."),
    TextChatMessage.Assistant("public int Fibonacci(int n)", partial: true)
};

var completion = client.GetTextCompletionStreamAsync(
new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
{
    Model = "qwen-turbo",
    Input = new TextGenerationInput() { Messages = messages },
    Parameters = new TextGenerationParameters()
    {
        ResultFormat = "message",
        IncrementalOutput = true
    }
});
```

### Long Context (Qwen-Long)
For Qwen-Long models:
```csharp
var file = new FileInfo("test.txt");
var uploadedFile = await dashScopeClient.OpenAiCompatibleUploadFileAsync(file.OpenRead(), file.Name);
var history = new List<ChatMessage> { ChatMessage.File(uploadedFile.Id) };
var completion = await client.client.GetTextCompletionAsync(
        new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
        {
            Model = "qwen-long",
            Input = new TextGenerationInput() { Messages = history },
            Parameters = new TextGenerationParameters()
            {
                ResultFormat = "message",
                EnableThinking = false,
            }
        });
Console.WriteLine(completion.Output.Choices[0].Message.Content);
// Cleanup
await dashScopeClient.OpenAiCompatibleDeleteFileAsync(uploadedFile.Id);
```

### Code Interpreter

**This capability is mutually exclusive with Function Call and cannot be used simultaneously.**

Use the `EnableCodeInterpreter` parameter in `Parameters` to allow the model to write code and call an internal code interpreter for calculations.

Example Request:

```csharp
var completion = client.GetTextCompletionStreamAsync(
    new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
    {
        Model = "qwen3-max-preview",
        Input = new TextGenerationInput() { Messages = messages },
        Parameters = new TextGenerationParameters()
        {
            ResultFormat = "message",
            EnableThinking = true,
            EnableCodeInterpreter = true,
            IncrementalOutput = true
        }
    });
```

The code that model generated will be included in `chunk.Output.ToolInfo.CodeInterpreter`. The invocation process can be considered part of the reasoning process.

Full example,

```csharp
var messages = new List<TextChatMessage>();
const string input = "123的21次方是多少？";
Console.Write($"User > {input}");
messages.Add(TextChatMessage.User(input));
var completion = client.GetTextCompletionStreamAsync(
    new ModelRequest<TextGenerationInput, ITextGenerationParameters>
    {
        Model = "qwen3-max-preview",
        Input = new TextGenerationInput { Messages = messages },
        Parameters = new TextGenerationParameters
        {
            ResultFormat = "message",
            EnableThinking = true,
            EnableCodeInterpreter = true,
            IncrementalOutput = true
        }
    });
var reply = new StringBuilder();
var codeGenerated = false;
var reasoning = false;
TextGenerationTokenUsage? usage = null;
await foreach (var chunk in completion)
{
    var choice = chunk.Output.Choices![0];
    var tool = chunk.Output.ToolInfo?.FirstOrDefault();
    if (codeGenerated == false && tool?.CodeInterpreter != null)
    {
        Console.WriteLine($"Code > {tool.CodeInterpreter.Code}");
        codeGenerated = true;
    }

    if (string.IsNullOrEmpty(choice.Message.ReasoningContent) == false)
    {
        // reasoning
        if (reasoning == false)
        {
            Console.WriteLine();
            Console.Write("Reasoning > ");
            reasoning = true;
        }

        Console.Write(choice.Message.ReasoningContent);
        continue;
    }

    if (reasoning && string.IsNullOrEmpty(choice.Message.Content.Text) == false)
    {
        reasoning = false;
        Console.WriteLine();
        Console.Write("Assistant > ");
    }

    Console.Write(choice.Message.Content);
    reply.Append(choice.Message.Content);
    usage = chunk.Usage;
}

Console.WriteLine();
messages.Add(TextChatMessage.Assistant(reply.ToString()));
if (usage != null)
{
    Console.WriteLine(
        $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/reasoning({usage.OutputTokensDetails?.ReasoningTokens})/plugins({usage.Plugins?.CodeInterpreter?.Count})/total({usage.TotalTokens})");
}

/*
User > 123的21次方是多少？
Reasoning > 用户问的是123的21次方是多少。这是一个大数计算问题，我需要使用代码计算器来计算这个值。

我需要调用code_interpreter函数，传入计算123**21的Python代码。
123**21
用户询问123的21次方是多少，我使用代码计算器计算出了结果。结果是一个非常大的数字：77269364466549865653073473388030061522211723

我应该直接给出这个结果，因为这是一个精确的数学计算问题，不需要额外的解释或
Assistant > 123的21次方是：77269364466549865653073473388030061522211723
Usage: in(704)/out(234)/reasoning(142)/plugins(1)/total(938)
*/
```



### PPT Generation (Qwen-doc-turbo)

Use `qwen-doc-turbo` with the PPT skill to generate a presentation from a document URL or prompt. Pass the document link via `TextChatMessage.DocUrl` and enable the PPT skill through `Parameters.Skill`.

- `DashScopeModelSkill.PptCreative` — generate a presentation in creative mode (no template required).
- `DashScopeModelSkill.PptGeneral(templateId)` — generate in general mode using the given template.

The model emits the slide storyboard in `ReasoningContent`, and the final reply `Content` contains a download URL for the generated `.pptx` file.

```csharp
var messages = new List<TextChatMessage>
{
    TextChatMessage.System("You are a helpful assistant"),
    TextChatMessage.DocUrl("生成一个ppt", ["https://example.com/product-manual.docx"]),
};
var completion = client.GetTextCompletionStreamAsync(
    new ModelRequest<TextGenerationInput, ITextGenerationParameters>()
    {
        Model = "qwen-doc-turbo",
        Input = new TextGenerationInput() { Messages = messages },
        Parameters = new TextGenerationParameters()
        {
            ResultFormat = "message",
            IncrementalOutput = true,
            Skill = [DashScopeModelSkill.PptCreative]
        }
    });
var reply = new StringBuilder();
var reasoning = false;
TextGenerationTokenUsage? usage = null;
await foreach (var chunk in completion)
{
    var choice = chunk.Output.Choices![0];
    if (string.IsNullOrEmpty(choice.Message.ReasoningContent) == false)
    {
        if (reasoning == false)
        {
            reasoning = true;
            Console.Write("Reasoning > ");
        }

        Console.Write(choice.Message.ReasoningContent);
        continue;
    }

    if (reasoning && string.IsNullOrEmpty(choice.Message.Content.Text) == false)
    {
        reasoning = false;
        Console.WriteLine();
        Console.Write("Assistant > ");
    }

    Console.Write(choice.Message.Content);
    reply.Append(choice.Message.Content);
    usage = chunk.Usage;
}

Console.WriteLine();
if (usage != null)
{
    Console.WriteLine($"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/total({usage.TotalTokens})");
}

// reply.ToString() contains the .pptx download URL
```

## Multimodal

Use `GetMultimodalGenerationAsync`/`GetMultimodalGenerationStreamAsync`
[Official Documentation](https://help.aliyun.com/zh/model-studio/multimodal)

### Upload file for multimodal usage

You can upload file to get an oss link before multimodal usage.

```csharp
await using var video = File.OpenRead("sample.mp4");
var ossLink = await client.UploadTemporaryFileAsync("qwen3-vl-plus", video, "sample.mp4");
Console.WriteLine($"File uploaded: {ossLink}");

var messages = new List<MultimodalMessage>();
messages.Add(
    MultimodalMessage.User(
    [
        MultimodalMessageContent.VideoContent(ossLink, fps: 2),
        // MultimodalMessageContent.VideoFrames(links),
        // MultimodalMessageContent.ImageContent(link)
        MultimodalMessageContent.TextContent("这段视频的内容是什么？")
    ]));
```

#### Limit Upload Speed

You can limit the upload speed for all file upload APIs (`UploadTemporaryFileAsync`, `OpenAiCompatibleUploadFileAsync`, `UploadFilesAsync`) by setting `MaximumUploadSpeed`. The default value is `-1` (no limit).

Console application:

```csharp
var client = new DashScopeClient("your-api-key", region: DashScopeRegion.Singapore);
client.MaximumUploadSpeed = 1024 * 1024; // 1 MB/s
```

ASP.NET Core application (`appsettings.json`):

```json
{
    "DashScope": {
        "ApiKey": "your-api-key",
        "MaximumUploadSpeed": 1048576
    }
}
```

### Image recognition/thinking

```csharp
var image = await File.ReadAllBytesAsync("Lenna.jpg");
var response = dashScopeClient.GetMultimodalGenerationStreamAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qvq-plus",
        Input = new MultimodalInput()
        {
            Messages =
            [
                MultimodalMessage.User(
                [
                    MultimodalMessageContent.ImageContent(image, "image/jpeg"),
                    MultimodalMessageContent.TextContent("她是谁？")
                ])
            ]
        },
        Parameters =
            new MultimodalParameters
            {
                IncrementalOutput = true,
                // EnableThinking = true,
                VlHighResolutionImages = false
            }
    });

// output
var reasoning = false;
await foreach (var modelResponse in response)
{
    var choice = modelResponse.Output.Choices.FirstOrDefault();
    if (choice != null)
    {
        if (choice.FinishReason != "null")
        {
            break;
        }

        if (string.IsNullOrEmpty(choice.Message.ReasoningContent) == false)
        {
            if (reasoning == false)
            {
                reasoning = true;
                Console.WriteLine("<think>");
            }

            Console.Write(choice.Message.ReasoningContent);
            continue;
        }

        if (reasoning)
        {
            reasoning = false;
            Console.WriteLine("</think>");
        }

        Console.Write(choice.Message.Content[0].Text);
    }
}
```

### OCR

Base example of OCR

```csharp
// upload file
await using var tilted = File.OpenRead("tilted.png");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", tilted, "tilted.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages = new List<MultimodalMessage>();
messages.Add(
    MultimodalMessage.User(
    [
        // set enableRotate to true if your source image is tilted.
        MultimodalMessageContent.ImageContent(ossLink, enableRotate: true),
    ]));
var completion = client.GetMultimodalGenerationStreamAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput() { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            IncrementalOutput = true,
        }
    });
var reply = new StringBuilder();
var first = false;
MultimodalTokenUsage? usage = null;
await foreach (var chunk in completion)
{
    var choice = chunk.Output.Choices[0];
    if (first)
    {
        first = false;
        Console.Write("Assistant > ");
    }

    if (choice.Message.Content.Count == 0)
    {
        continue;
    }

    Console.Write(choice.Message.Content[0].Text);
    reply.Append(choice.Message.Content[0].Text);
    usage = chunk.Usage;
}

Console.WriteLine();
messages.Add(MultimodalMessage.Assistant([MultimodalMessageContent.TextContent(reply.ToString())]));
if (usage != null)
{
    Console.WriteLine(
        $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/image({usage.ImageTokens})/total({usage.TotalTokens})");
}
```

#### Built-in Tasks

##### Advanced Recognition

When using this task, do not enable streaming. Otherwise, `completion.Output.Choices[0].Message.Content[0].OcrResult.WordsInfo` will be `null`.

In addition to the standard text content, this task also returns the coordinates of the text.

To call this built-in task, set `Parameters.OcrOptions.Task` to `advanced_recognition`. No additional prompt is required.

![](sample/Cnblogs.DashScope.Sample/tilted.png)

```csharp
var messages = new List<MultimodalMessage>();
messages.Add(
    MultimodalMessage.User(
    [
        MultimodalMessageContent.ImageContent(ossLink),
    ]));
var completion = client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput() { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "advanced_recognition"
            }
        }
    });
```

Output usage:

```csharp
Console.WriteLine("Text:");
Console.WriteLine(completion.Output.Choices[0].Message.Content[0].Text);
Console.WriteLine("WordsInfo:");
foreach (var info in completion.Output.Choices[0].Message.Content[0].OcrResult!.WordsInfo!)
{
    var location = $"[{string.Join(',', info.Location)}]";
    var rect = $"[{string.Join(',', info.RotateRect)}]";
    Console.WriteLine(info.Text);
    Console.WriteLine($"Location: {location}");
    Console.WriteLine($"RotateRect: {rect}");
    Console.WriteLine();
}
```

Output:

````csharp
Text:
```json
[
        {"rotate_rect": [236, 254, 115, 299, 90], "text": "OpenAI 兼容"},
        {"rotate_rect": [646, 254, 115, 269, 90], "text": "DashScope"},
        {"rotate_rect": [236, 684, 115, 163, 90], "text": "Python"},
        {"rotate_rect": [492, 684, 115, 105, 90], "text": "Java"},
        {"rotate_rect": [712, 684, 115, 85, 90], "text": "curl"}
]
```
WordsInfo:
OpenAI 兼容
Location: [46,55,205,55,205,87,46,87]
RotateRect: [125,71,159,32,0]

DashScope
Location: [272,55,415,55,415,87,272,87]
RotateRect: [344,71,32,143,90]

Python
Location: [82,175,169,175,169,207,82,207]
RotateRect: [126,191,32,87,90]

Java
Location: [234,175,289,175,289,207,234,207]
RotateRect: [262,191,55,32,0]

curl
Location: [356,175,401,175,401,207,356,207]
RotateRect: [378,191,32,45,90]
````

##### Key Information Extraction

When using built-in tasks, it is not recommended to enable streaming; otherwise, `completion.Output.Choices[0].Message.Content[0].OcrResult.KvResult` will be `null`.

To invoke this built-in task, set `Parameters.OcrOptions.Task` to `key_information_extraction`. No additional text information needs to be provided.

You can customize the output JSON format via `Parameters.OcrOptions.TaskConfig.ResultSchema` (with a maximum of 3 levels of nesting). If left blank, all fields will be output by default.

For example, suppose we want to extract objects of the following type from an image (JSON property names should, as much as possible, be based on the text present in the image):

![](sample/Cnblogs.DashScope.Sample/receipt.jpg)

```csharp
internal class ReceiptModel()
{
    [JsonPropertyName("乘车日期")]
    public string? Date { get; init; }

    [JsonPropertyName("发票")]
    public ReceiptSerials? Serials { get; init; }
}

internal class ReceiptSerials
{
    [JsonPropertyName("发票代码")]
    public string? Code { get; init; }

    [JsonPropertyName("发票号码")]
    public string? Serial { get; init; }
}
```

Property could be `null` if model failed to extract value for it.
Example request:

```csharp
await using var file = File.OpenRead("receipt.jpg");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", file, "receipt.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages =
    new List<MultimodalMessage> { MultimodalMessage.User([MultimodalMessageContent.ImageContent(ossLink)]) };
var completion = await client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput() { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "key_information_extraction",
                TaskConfig = new MultimodalOcrTaskConfig()
                {
                    ResultSchema = new Dictionary<string, object>()
                    {
                        {
                            "发票",
                            new Dictionary<string, string>()
                            {
                                { "发票代码", "提取图中的发票代码，通常为一组数字或字母组合" },
                                { "发票号码", "提取发票上的号码，通常由纯数字组成。" }
                            }
                        },
                        { "乘车日期", "对应图中乘车日期时间，格式为年-月-日，比如2025-03-05" }
                    }
                }
            }
        }
    });
```

Consume:

`KvResult` is `JsonElement`，you can deserialize it to any type you desire, or you could just use `Dictionary<string, JsonElement?>` .

````csharp
Console.WriteLine("Text:");
Console.WriteLine(completion.Output.Choices[0].Message.Content[0].Text);
Console.WriteLine("KvResults:");
var model = completion.Output.Choices[0].Message.Content[0].OcrResult!.KvResult?.Deserialize<ReceiptModel>();
Console.WriteLine($"Date: {model?.Date}");
Console.WriteLine($"Code: {model?.Serials?.Code}");
Console.WriteLine($"Serial: {model?.Serials?.Serial}");

/*
Text:
```json
{
    "乘车日期": "2013-06-29",
    "发票": {
        "发票代码": "221021325353",
        "发票号码": "10283819"
    }
}
```
KvResults:
Date: 2013-06-29
Code: 221021325353
Serial: 10283819
Usage: in(524)/out(65)/image(310)/total(589)
*/
````

##### Table Parsing

To invoke this built-in task, set `Parameters.OcrOptions.Task` to `table_parsing`. No additional text information needs to be provided.

This task will extract tables from images and return them in HTML format.

Example:

![](sample/Cnblogs.DashScope.Sample/table.jpg)

```csharp
await using var file = File.OpenRead("table.jpg");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", file, "table.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages =
    new List<MultimodalMessage> { MultimodalMessage.User([MultimodalMessageContent.ImageContent(ossLink)]) };
var completion = await client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "table_parsing",
            }
        }
    });

Console.WriteLine(completion.Output.Choices[0].Message.Content[0].Text);
```

Return value(Model would wrap the html code in a markdown code fence):

````markdown
```html
<table>
  <tr>
    <td>Record of test data</td>
  </tr>
  <tr>
    <td>Project name：2B</td>
    <td>Control No.CEPRI-D-JS1-JS-057-2022-003</td>
  </tr>
  <tr>
    <td>Case name</td>
    <td>Test No.3 Conductor rupture GL+GR(max angle)</td>
    <td>Last load grade：</td>
    <td>0%</td>
    <td>Current load grade：</td>
  </tr>
  <tr>
    <td>Measure</td>
    <td>Load point</td>
    <td>Load method</td>
    <td>Actual Load(%)</td>
    <td>Actual Load(kN)</td>
  </tr>
  <tr>
    <td>channel</td>
    <td>V1</td>
    <td>活载荷</td>
    <td>147.95</td>
    <td>0.815</td>
  </tr>
  <tr>
    <td>V03</td>
    <td>V2</td>
    <td>活载荷</td>
    <td>111.75</td>
    <td>0.615</td>
  </tr>
  <tr>
    <td>V04</td>
    <td>V3</td>
    <td>活载荷</td>
    <td>9.74</td>
    <td>1.007</td>
  </tr>
  <tr>
    <td>V05</td>
    <td>V4</td>
    <td>活载荷</td>
    <td>7.88</td>
    <td>0.814</td>
  </tr>
  <tr>
    <td>V06</td>
    <td>V5</td>
    <td>活载荷</td>
    <td>8.11</td>
    <td>0.780</td>
  </tr>
  <tr>
    <td>V07</td>
    <td>V6</td>
    <td>活载荷</td>
    <td>8.54</td>
    <td>0.815</td>
  </tr>
  <tr>
    <td>V08</td>
    <td>V7</td>
    <td>活载荷</td>
    <td>6.77</td>
    <td>0.700</td>
  </tr>
  <tr>
    <td>V09</td>
    <td>V8</td>
    <td>活载荷</td>
    <td>8.59</td>
    <td>0.888</td>
  </tr>
  <tr>
    <td>L01</td>
    <td>L1</td>
    <td>活载荷</td>
    <td>13.33</td>
    <td>3.089</td>
  </tr>
  <tr>
    <td>L02</td>
    <td>L2</td>
    <td>活载荷</td>
    <td>9.69</td>
    <td>2.247</td>
  </tr>
  <tr>
    <td>L03</td>
    <td>L3</td>
    <td></td>
    <td>2.96</td>
    <td>1.480</td>
  </tr>
  <tr>
    <td>L04</td>
    <td>L4</td>
    <td></td>
    <td>3.40</td>
    <td>1.700</td>
  </tr>
  <tr>
    <td>L05</td>
    <td>L5</td>
    <td></td>
    <td>2.45</td>
    <td>1.224</td>
  </tr>
  <tr>
    <td>L06</td>
    <td>L6</td>
    <td></td>
    <td>2.01</td>
    <td>1.006</td>
  </tr>
  <tr>
    <td>L07</td>
    <td>L7</td>
    <td></td>
    <td>2.38</td>
    <td>1.192</td>
  </tr>
  <tr>
    <td>L08</td>
    <td>L8</td>
    <td></td>
    <td>2.10</td>
    <td>1.050</td>
  </tr>
  <tr>
    <td>T01</td>
    <td>T1</td>
    <td>活载荷</td>
    <td>25.29</td>
    <td>3.073</td>
  </tr>
  <tr>
    <td>T02</td>
    <td>T2</td>
    <td>活载荷</td>
    <td>27.39</td>
    <td>3.327</td>
  </tr>
  <tr>
    <td>T03</td>
    <td>T3</td>
    <td>活载荷</td>
    <td>8.03</td>
    <td>2.543</td>
  </tr>
  <tr>
    <td>T04</td>
    <td>T4</td>
    <td>活载荷</td>
    <td>11.19</td>
    <td>3.542</td>
  </tr>
  <tr>
    <td>T05</td>
    <td>T5</td>
    <td>活载荷</td>
    <td>11.34</td>
    <td>3.592</td>
  </tr>
  <tr>
    <td>T06</td>
    <td>T6</td>
    <td>活载荷</td>
    <td>16.47</td>
    <td>5.217</td>
  </tr>
  <tr>
    <td>T07</td>
    <td>T7</td>
    <td>活载荷</td>
    <td>11.05</td>
    <td>3.498</td>
  </tr>
  <tr>
    <td>T08</td>
    <td>T8</td>
    <td>活载荷</td>
    <td>8.66</td>
    <td>2.743</td>
  </tr>
  <tr>
    <td>T09</td>
    <td>WT1</td>
    <td>活载荷</td>
    <td>36.56</td>
    <td>2.365</td>
  </tr>
  <tr>
    <td>T10</td>
    <td>WT2</td>
    <td>活载荷</td>
    <td>24.55</td>
    <td>2.853</td>
  </tr>
  <tr>
    <td>T11</td>
    <td>WT3</td>
    <td>活载荷</td>
    <td>38.06</td>
    <td>4.784</td>
  </tr>
  <tr>
    <td>T12</td>
    <td>WT4</td>
    <td>活载荷</td>
    <td>37.70</td>
    <td>5.030</td>
  </tr>
  <tr>
    <td>T13</td>
    <td>WT5</td>
    <td>活载荷</td>
    <td>30.48</td>
    <td>4.524</td>
  </tr>
</table>
```
````

##### Document Parsing

To invoke this built-in task, set `Parameters.OcrOptions.Task` to `document_parsing`. No additional text information needs to be provided.

This task read images(usually scanned PDF) and return them in LaTeX format.

Example:

![](sample/Cnblogs.DashScope.Sample/scanned.jpg)

```csharp
await using var file = File.OpenRead("scanned.jpg");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", file, "scanned.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages =
    new List<MultimodalMessage> { MultimodalMessage.User([MultimodalMessageContent.ImageContent(ossLink)]) };
var completion = await client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "document_parsing",
            }
        }
    });
```

Returns:

````markdown
```latex
\section*{Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution}

Peng Wang* \quad Shuai Bai* \quad Sinan Tan* \quad Shijie Wang* \quad Zhihao Fan* \quad Jinze Bai*? \\
Keqin Chen \quad Xuejing Liu \quad Jialin Wang \quad Wenbin Ge \quad Yang Fan \quad Kai Dang \quad Mengfei Du \\
Xuancheng Ren \quad Rui Men \quad Dayiheng Liu \quad Chang Zhou \quad Jingren Zhou \quad Junyang Lin*? \\
Qwen Team \quad Alibaba Group

\begin{abstract}
We present the Qwen2-VL Series, an advanced upgrade of the previous Qwen-VL models that redefines the conventional predetermined-resolution approach in visual processing. Qwen2-VL introduces the Naive Dynamic Resolution mechanism, which enables the model to dynamically process images of varying resolutions into different numbers of visual tokens. This approach allows the model to generate more efficient and accurate visual representations, closely aligning with human perceptual processes. The model also integrates Multimodal Rotary Position Embedding (M-RoPE), facilitating the effective fusion of positional information across text, images, and videos. We employ a unified paradigm for processing both images and videos, enhancing the model's visual perception capabilities. To explore the potential of large multimodal models, Qwen2-VL investigates the scaling laws for large vision-language models (LVLMS). By scaling both the model size-with versions at 2B, 8B, and 72B parameters-and the amount of training data, the Qwen2-VL Series achieves highly competitive performance. Notably, the Qwen2-VL-72B model achieves results comparable to leading models such as GPT-4o and Claude3.5-Sonnet across various multimodal benchmarks, outperforming other generalist models. Code is available at \url{https://github.com/QwenLM/Qwen2-VL}.
\end{abstract}

\section{Introduction}

In the realm of artificial intelligence, Large Vision-Language Models (LVLMS) represent a significant leap forward, building upon the strong textual processing capabilities of traditional large language models. These advanced models now encompass the ability to interpret and analyze a broader spectrum of data, including images, audio, and video. This expansion of capabilities has transformed LVLMS into indispensable tools for tackling a variety of real-world challenges. Recognized for their unique capacity to condense extensive and intricate knowledge into functional representations, LVLMS are paving the way for more comprehensive cognitive systems. By integrating diverse data forms, LVLMS aim to more closely mimic the nuanced ways in which humans perceive and interact with their environment. This allows these models to provide a more accurate representation of how we engage with and perceive our environment.

Recent advancements in large vision-language models (LVLMS) (Li et al., 2023c; Liu et al., 2023b; Dai et al., 2023; Zhu et al., 2023; Huang et al., 2023a; Bai et al., 2023b; Liu et al., 2023a; Wang et al., 2023b; OpenAI, 2023; Team et al., 2023) have led to significant improvements in a short span. These models (OpenAI, 2023; Touvron et al., 2023a,b; Chiang et al., 2023; Bai et al., 2023a) generally follow a common approach of \textit{visual encoder} $\rightarrow$ \textit{cross-modal connector} $\rightarrow$ \textit{LLM}. This setup, combined with next-token prediction as the primary training method and the availability of high-quality datasets (Liu et al., 2023a; Zhang et al., 2023; Chen et al., 2023b);

*Equal core contribution, ?Corresponding author

```
````

##### Formula Recognition

To invoke this built-in task, set `Parameters.OcrOptions.Task` to `formula_recognition`. No additional text information needs to be provided.

This task read images(like handwriting formulas) and return them in LaTeX format.

Example:

![](sample/Cnblogs.DashScope.Sample/math.jpg)

```csharp
// upload file
await using var file = File.OpenRead("math.jpg");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", file, "math.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages =
    new List<MultimodalMessage> { MultimodalMessage.User([MultimodalMessageContent.ImageContent(ossLink)]) };
var completion = await client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "formula_recognition",
            }
        }
    });

Console.WriteLine("LaTeX:");
Console.WriteLine(completion.Output.Choices[0].Message.Content[0].Text);

if (completion.Usage != null)
{
    var usage = completion.Usage;
    Console.WriteLine(
        $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/image({usage.ImageTokens})/total({usage.TotalTokens})");
}
```

Returns:

````markdown
```latex
\begin{align*}
\tilde{G}(x) &= \frac{\alpha}{\kappa}x, \quad \tilde{T}_i = T, \quad \tilde{H}_i = \tilde{\kappa}T, \quad \tilde{\lambda}_i = \frac{1}{\kappa}\sum_{j=1}^{m}\omega_j - z_i, \\
L(\{p_n\}; m^n) + L(\{x^n\}, m^n) + L(\{m^n\}; q_n) &= L(m^n; q_n) \\
I^{m_n} - (L+1) &= z + \int_0^1 I^{m_n} - (L)z \leq x_m | L^{m_n} - (L) |^3 \\
&\leq \kappa\partial_1\psi(x) + \frac{\kappa^3}{6}\partial_2^3\psi(x) - V(x) \psi(x) = \int d^3y K(x,y) \psi(y), \\
\int_{B_{\kappa}(0)} I^{m}(w)^2 d\gamma &= \lim_{n\to\infty} \int_{B_{\kappa}(0)} r\psi(w_n)^2 d\gamma = \lim_{n\to\infty} \int_{B_{\kappa}(y_n)} d\gamma \geq \beta > 0,
\end{align*}
```
````

$$
\begin{align*}
\tilde{G}(x) &= \frac{\alpha}{\kappa}x, \quad \tilde{T}_i = T, \quad \tilde{H}_i = \tilde{\kappa}T, \quad \tilde{\lambda}_i = \frac{1}{\kappa}\sum_{j=1}^{m}\omega_j - z_i, \\
L(\{p_n\}; m^n) + L(\{x^n\}, m^n) + L(\{m^n\}; q_n) &= L(m^n; q_n) \\
I^{m_n} - (L+1) &= z + \int_0^1 I^{m_n} - (L)z \leq x_m | L^{m_n} - (L) |^3 \\
&\leq \kappa\partial_1\psi(x) + \frac{\kappa^3}{6}\partial_2^3\psi(x) - V(x) \psi(x) = \int d^3y K(x,y) \psi(y), \\
\int_{B_{\kappa}(0)} I^{m}(w)^2 d\gamma &= \lim_{n\to\infty} \int_{B_{\kappa}(0)} r\psi(w_n)^2 d\gamma = \lim_{n\to\infty} \int_{B_{\kappa}(y_n)} d\gamma \geq \beta > 0,
\end{align*}
$$



##### Text Recognition

To invoke this built-in task, set `Parameters.OcrOptions.Task` to `text_recognition`. No additional text information needs to be provided.

This task read the images and returns content in plain text(Chinese and English only).

Example:

![](sample/Cnblogs.DashScope.Sample/webpage.jpg)

```csharp
// upload file
await using var file = File.OpenRead("webpage.jpg");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", file, "webpage.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages =
    new List<MultimodalMessage> { MultimodalMessage.User([MultimodalMessageContent.ImageContent(ossLink)]) };
var completion = await client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "text_recognition",
            }
        }
    });
```

Returns

```plaintext
OpenAI 兼容 DashScope
Python Java curl
```

##### Multilanguage

To invoke this built-in task, set `Parameters.OcrOptions.Task` to `multi_lan`. No additional text information needs to be provided.

This task read the images and returns content in plain text(Support more languages).

![](sample/Cnblogs.DashScope.Sample/multilanguage.jpg)

```csharp
await using var file = File.OpenRead("multilanguage.jpg");
var ossLink = await client.UploadTemporaryFileAsync("qwen-vl-ocr-latest", file, "multilanguage.jpg");
Console.WriteLine($"File uploaded: {ossLink}");
var messages =
    new List<MultimodalMessage> { MultimodalMessage.User([MultimodalMessageContent.ImageContent(ossLink)]) };
var completion = await client.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen-vl-ocr-latest",
        Input = new MultimodalInput { Messages = messages },
        Parameters = new MultimodalParameters()
        {
            OcrOptions = new MultimodalOcrOptions()
            {
                Task = "multi_lan",
            }
        }
    });
```

Returns

```csharp
INTERNATIONAL
MOTHER LANGUAGE
DAY
你好!
Прив?т!
Bonjour!
Merhaba!
Ciao!
Hello!
Ola!
????
Salam!
```

### GUI

Use `gui-plus` to generate standardized operational information based on screenshots and user intent.

Currently, the main capabilities are implemented through the `System Prompt`, where you can configure the model’s available capabilities and the output JSON format.

Sample system prompt:

```markdown
## 1. Core Role
You are an expert AI Vision Operation Agent. Your task is to analyze computer screenshots, understand user instructions, and then break down the task into single, precise GUI atomic operations.
## 2. [CRITICAL] JSON Schema & Absolute Rules
Your output **must** be a JSON object that strictly adheres to the following rules. **Any deviation will result in failure**.
- **[R1] Strict JSON**: Your response **must** be *and only be* a JSON object. Do not add any text, comments, or explanations before or after the JSON code block.
- **[R2] Strict `thought` Structure**: The `thought` object must contain a single sentence briefly describing your thought process. For example: "The user wants to open the browser. I see the Chrome icon on the desktop, so the next step is to click it."
- **[R3] Precise `action` Value**: The value of the `action` field **must** be an uppercase string defined in `## 3. Toolset` (e.g., `"CLICK"`, `"TYPE"`). No leading/trailing spaces or case variations are allowed.
- **[R4] Strict `parameters` Structure**: The structure of the `parameters` object **must** be **perfectly identical** to the template defined for the selected Action in `## 3. Toolset`. Key names and value types must match exactly.
## 3. Toolset (Available Actions)
### CLICK
- **Description**: Click on the screen.
- **Parameters Template**:
  {
    "x": <integer>,
    "y": <integer>,
    "description": "<string, optional: A short string describing what you are clicking on, e.g., 'Chrome browser icon' or 'Login button'.>"
  }

### TYPE
- **Description**: Type text.
- **Parameters Template**:
{
  "text": "<string>",
  "needs_enter": <boolean>
}

### SCROLL
- **Description**: Scroll the window.
- **Parameters Template**:
{
  "direction": "<'up' or 'down'>",
  "amount": "<'small', 'medium', or 'large'>"
}

### KEY_PRESS
- **Description**: Press a function key.
- **Parameters Template**:
{
  "key": "<string: e.g., 'enter', 'esc', 'alt+f4'>"
}

### FINISH
- **Description**: Task completed successfully.
- **Parameters Template**:
{
  "message": "<string: A summary of the task completion>"
}

### FAILE
- **Description**: Task cannot be completed.
- **Parameters Template**:
{
  "reason": "<string: A clear explanation of the failure reason>"
}

## 4. Thinking and Decision Framework
Before generating each action, strictly follow the following thought-verification process:
**Goal Analysis**: What is the user's ultimate goal?
**Screen Observation (Grounded Observation)**: Carefully analyze the screenshot. Your decisions must be based on visual evidence present in the screenshot. If you cannot see an element, you cannot interact with it.
**Action Decision**: Based on the goal and visible elements, select the most appropriate tool.
**Construct Output**:
a. Record your thought process in the `thought` field.
b. Select an `action`.
c. Precisely copy the `parameters` template for that action and fill in the values.
**Final Verification (Self-Correction)**: Before outputting, perform a final check:
- Is my response pure JSON?
- Is the `action` value correct (uppercase, no spaces)?
- Is the `parameters` structure 100% identical to the template? For example, for `CLICK`, are there separate `x` and `y` keys, and are their values integers?
```

Request:

```csharp
var messages = new List<MultimodalMessage>
{
    MultimodalMessage.System([MultimodalMessageContent.TextContent(SystemPrompt)]),
    MultimodalMessage.User(
    [
        MultimodalMessageContent.ImageContent(
            "https://img.alicdn.com/imgextra/i2/O1CN016iJ8ob1C3xP1s2M6z_!!6000000000026-2-tps-3008-1758.png"),
        MultimodalMessageContent.TextContent("Open browser")
    ])
};
var completion = client.GetMultimodalGenerationStreamAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "gui-plus",
        Input = new MultimodalInput() { Messages = messages },
        Parameters = new MultimodalParameters() { IncrementalOutput = true, }
    });
```

Response:

```csharp
{
  "thought": "用户想打开浏览器，我看到了桌面上的Google Chrome图标，因此下一步是点击它。",
  "action": "CLICK",
  "parameters": {
    "x": 1089,
    "y": 123
  }
}
```

Then you can execute the command that model returns, and reply the screenshot with next intension.

### Audio Understanding

Example(use `Qwen3-Omni-Captioner`)

```csharp
// upload file
await using var audio = File.OpenRead("noise.wav");
var ossLink = await client.UploadTemporaryFileAsync("qwen3-omni-30b-a3b-captioner", audio, "noise.wav");
Console.WriteLine($"File uploaded: {ossLink}");
var messages = new List<MultimodalMessage>
{
    MultimodalMessage.User(
    [
        // 也可以直接传入公网地址
        MultimodalMessageContent.AudioContent(ossLink),
    ])
};
var completion = client.GetMultimodalGenerationStreamAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>()
    {
        Model = "qwen3-omni-30b-a3b-captioner",
        Input = new MultimodalInput() { Messages = messages },
        Parameters = new MultimodalParameters() { IncrementalOutput = true, }
    });
var reply = new StringBuilder();
var first = true;
MultimodalTokenUsage? usage = null;
await foreach (var chunk in completion)
{
    var choice = chunk.Output.Choices[0];
    if (first)
    {
        first = false;
        Console.WriteLine();
        Console.Write("Assistant > ");
    }

    if (choice.Message.Content.Count == 0)
    {
        continue;
    }

    Console.Write(choice.Message.Content[0].Text);
    reply.Append(choice.Message.Content[0].Text);
    usage = chunk.Usage;
}

Console.WriteLine();
messages.Add(MultimodalMessage.Assistant([MultimodalMessageContent.TextContent(reply.ToString())]));
if (usage != null)
{
    Console.WriteLine(
        $"Usage: in({usage.InputTokens})/out({usage.OutputTokens})/audio({usage.InputTokensDetails?.AudioTokens})/total({usage.TotalTokens})");
}
```

Sample output

```csharp
Assistant > The audio clip opens with a rapid, percussive metallic clatter, reminiscent of a typewriter or similar mechanical device, which continues in a steady rhythm throughout the recording. This clatter is slightly left-of-center in the stereo field and is accompanied by a faint, low-frequency hum, likely from a household appliance or HVAC system. The acoustic environment is a small, enclosed room with hard surfaces, indicated by the short, bright reverberation of both the clatter and the speaker’s voice. The audio quality is moderate, with a noticeable electronic hiss and some loss of high-frequency detail, but no digital distortion or clipping.

At the one-second mark, a male voice enters, positioned slightly right-of-center and closer to the microphone. He speaks in standard Mandarin, with a tone of weary exasperation: “哎 呀，这样我还怎么安静工作啊？” (“Aiyā, zěnyàng wǒ hái zěnme ānjìng gōngzuò a?”), which translates to “Oh, how can I possibly work quietly like this?” His speech is clear, with a slightly rising pitch on “安静” (“quietly”) and a falling pitch on “啊” (“a”), conveying a sense of complaint and fatigue. The accent is standard, with no regional inflection, and the voice is that of a young to middle-aged adult male.

Throughout the clip, the mechanical clatter remains constant and prominent, occasionally competing with the voice for clarity. There are no other sounds, such as footsteps, additional voices, or environmental noises, and the background is otherwise quiet. The interplay between the persistent mechanical noise and the speaker’s complaint creates a vivid sense of disruption and frustration, suggesting an environment where work is being impeded by an external, uncontrolled sound source.

Culturally, the use of Mandarin, standard pronunciation, and modern recording quality indicate a contemporary, urban Chinese setting. The language and tone are universally relatable, reflecting a common experience of being disturbed during work. The lack of regional markers or distinctive background noises suggests a generic, possibly domestic or office-like space, but with no clear indicators of a specific location or social context.

In summary, the audio portrays a modern Mandarin-speaking man, exasperated by a constant, distracting mechanical noise (likely a typewriter or similar device), attempting to work in a small, reverberant room. The recording’s technical and acoustic features reinforce the sense of disruption and frustration, while the language and setting suggest a contemporary, urban Chinese context.
Usage: in(160)/out(514)/audio(152)/total(674)
```

## Text-to-Speech

The non-realtime speech synthesis models - qwen3-tts (e.g. `qwen3-tts-flash`) and MiniMax speech (e.g. `MiniMax/speech-2.8-hd`) - use the multimodal generation HTTP API instead of a websocket session. The text and voice settings go into `MultimodalInput`; qwen3-tts answers with a downloadable wav url (base64 chunks in `Audio.Data` when streaming), MiniMax speech with hex encoded audio in `Output.Data` (or a url when `OutputFormat` is set to `url`):

```csharp
// qwen3-tts, non-streaming: the response carries the download url of the complete wav file
var response = await dashScopeClient.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>
    {
        Model = "qwen3-tts-flash",
        Input = new MultimodalInput
        {
            Text = "你好，我是千问。",
            Voice = "Cherry",
            LanguageType = "Chinese"
        }
    });
Console.WriteLine($"Audio url (valid for 24 hours): {response.Output.Audio!.Url}");

// qwen3-tts, streaming: intermediate frames carry base64 wav chunks for immediate playback
await foreach (var frame in dashScopeClient.GetMultimodalGenerationStreamAsync(
                   new ModelRequest<MultimodalInput, IMultimodalParameters>
                   {
                       Model = "qwen3-tts-flash",
                       Input = new MultimodalInput { Text = "你好，我是千问。", Voice = "Cherry" }
                   }))
{
    if (frame.Output.Audio?.Data is { Length: > 0 } data)
    {
        PlayAudio(Convert.FromBase64String(data)); // e.g. wav, 24 kHz 16 bit mono
    }
}

// MiniMax speech, non-streaming: the response carries the hex encoded mp3 audio
var minimaxResponse = await dashScopeClient.GetMultimodalGenerationAsync(
    new ModelRequest<MultimodalInput, IMultimodalParameters>
    {
        Model = "MiniMax/speech-2.8-hd",
        Input = new MultimodalInput
        {
            Text = "你好，我是千问。",
            VoiceSetting = new MinimaxVoiceSetting { VoiceId = "male-qn-qingse", Emotion = "happy" },
            AudioSetting = new MinimaxAudioSetting { Format = "mp3", SampleRate = 32000 }
        }
    });
File.WriteAllBytes("minimax-tts.mp3", Convert.FromHexString(minimaxResponse.Output.Data!.Audio!));
```

In MiniMax streaming mode the intermediate frames carry hex chunks in `Output.Data` (`Status` 1) and the last frame aggregates the whole synthesis (`Status` 2); set `StreamOptions.ExcludeAggregatedAudio` to omit the aggregated audio from the last frame. Mixed voices (`TimbreWeights`), pronunciation replacement (`PronunciationDict`), voice effects (`VoiceModify`) and more voice settings are available on `MultimodalInput`.

The qwen-audio-tts models (e.g. `qwen-audio-3.0-tts-flash`) also have an HTTP mode via `GetSpeechSynthesisAsync` / `GetSpeechSynthesisStreamAsync`, with all parameters (voice, format, sample rate, speech rate, pitch, seed, `LanguageHints`, `Instruction`, AIGC tag, `HotFix` etc.) on `SpeechSynthesisInput`. Unlike the APIs above, this one is only served on the workspace domain, so configure `WorkspaceId` (same region as the API key) on the client:

```csharp
builder.Services.AddDashScopeClient("your-api-key", workspaceId: "your-workspace-id");

// non-streaming: the response carries the download url of the complete audio file
var response = await dashScopeClient.GetSpeechSynthesisAsync(
    new ModelRequest<SpeechSynthesisInput>
    {
        Model = "qwen-audio-3.0-tts-flash",
        Input = new SpeechSynthesisInput
        {
            Text = "我家的后面有一个很大的花园。",
            Voice = "longanhuan_v3.6",
            Format = "wav",
            SampleRate = 24000
        }
    });
Console.WriteLine($"Audio url (valid for 24 hours): {response.Output.Audio!.Url}");

// streaming: sentence events with base64 audio chunks, the final frame carries the url
await foreach (var frame in dashScopeClient.GetSpeechSynthesisStreamAsync(
                   new ModelRequest<SpeechSynthesisInput>
                   {
                       Model = "qwen-audio-3.0-tts-flash",
                       Input = new SpeechSynthesisInput
                       {
                           Text = "我家的后面有一个很大的花园。",
                           Voice = "longanhuan_v3.6",
                           Format = "wav",
                           WordTimestampEnabled = true
                       }
                   }))
{
    if (frame.Output.Audio?.Data is { Length: > 0 } data)
    {
        PlayAudio(Convert.FromBase64String(data));
    }

    if (frame.Output.Type == "sentence-end")
    {
        // word timestamps in frame.Output.Sentence.Words when enabled
    }
}
```

The same endpoint also serves audio generation with the qwen-audio-*-tts-next models (e.g. `qwen-audio-3.1-tts-next`): describe the audio in `TextPrompt` (reference audios are referenced in order as `@voice1` / `@voice2` / `@voice3`) and optionally pass up to 3 `References` (a public url or a base64 data uri each, 30 seconds / 10 MB at most; wav, mp3 or ogg opus), generated podcasts run up to 240 seconds and other scenarios up to 120 seconds:

```csharp
// generate a two-speaker dialogue with two reference audios
var response = await dashScopeClient.GetSpeechSynthesisAsync(
    new ModelRequest<SpeechSynthesisInput>
    {
        Model = "qwen-audio-3.1-tts-next",
        Input = new SpeechSynthesisInput
        {
            TextPrompt = "@voice1 says: \"What a sunny day!\" @voice2 answers: \"Let's go to the park.\"",
            References = new List<SpeechSynthesisReference>
            {
                new() { AudioUrl = "https://your-reference-1.wav" },
                new() { AudioUrl = "https://your-reference-2.wav" }
            },
            Format = "wav",
            SampleRate = 48000,
            Channels = 2
        }
    });
Console.WriteLine($"Audio url (24h): {response.Output.Audio!.Url}, duration: {response.Output.Audio.Duration}s");
```

Create a speech synthesis session using `dashScopeClient.CreateSpeechSynthesizerSocketSessionAsync()`.

Note: Use the using statement to automatically dispose the session, or manually call Dispose() to release resources. Avoid reusing sessions.

Create a synthesis session:
```csharp
using var tts = await dashScopeClient.CreateSpeechSynthesizerSocketSessionAsync("cosyvoice-v2");
var taskId = await tts.RunTaskAsync(new SpeechSynthesizerParameters { Voice = "longxiaochun_v2", Format = "mp3" });
await tts.ContinueTaskAsync(taskId, "Cnblogs");
await tts.ContinueTaskAsync(taskId, "Code changes the world");
await tts.FinishTaskAsync(taskId);
var file = new FileInfo("tts.mp3");
using var stream = file.OpenWrite();
await foreach (var b in tts.GetAudioAsync())
{
    stream.WriteByte(b);
}
Console.WriteLine($"Audio saved to {file.FullName}");
```
The session is shared by the cosyvoice models and the qwen-audio-3.1-tts / qwen-audio-3.0-tts models (e.g. `qwen-audio-3.1-tts-flash`), which report token based usage (`InputTokens` / `OutputTokens` / `TotalTokens` alongside `Characters`) in sentence-end and task-finished events, and additionally support the opus output format.

The Sambert models (`sambert-*-v1`, Beijing region only, the voice is part of the model name) use the one-shot calling mode instead: the whole text is passed to `SynthesizeAsync` in a single run-task (streaming: out) and continue-task / finish-task are not supported. Sambert sentence events carry sentence level `BeginTime`/`EndTime`, word timestamps without index fields, and phoneme level timestamps (enable `WordTimestampEnabled` + `PhonemeTimestampEnabled`):
```csharp
using var tts = await dashScopeClient.CreateSpeechSynthesizerSocketSessionAsync("sambert-zhichu-v1");
await tts.SynthesizeAsync(
    new SpeechSynthesizerParameters { Format = "wav", WordTimestampEnabled = true, PhonemeTimestampEnabled = true },
    "床前明月光，疑是地上霜");
// audio in tts.GetAudioAsync(), sentences with phoneme timestamps in tts.GetMessagesAsync()
```

The qwen3-tts-*-realtime models (e.g. `qwen3-tts-flash-realtime`) use a different realtime API (`CreateTtsRealtimeSocketSessionAsync`): the connection is established and `session.created` awaited before the session is returned, configure it with `UpdateSessionAsync` (voice, output format, and the `server_commit` / `commit` interaction mode), append text with `AppendTextAsync`, force the synthesis with `CommitTextAsync` and end it with `FinishAsync`. The audio is delivered as base64 chunks inside `response.audio.delta` events and exposed decoded via `GetAudioAsync()`, the raw events (including `response.done` with the billing usage) via `GetEventsAsync()`. Unlike the speech synthesizer session, the server closes the connection after `session.finished`, so a realtime session cannot be reused for a second run:
```csharp
using var tts = await dashScopeClient.CreateTtsRealtimeSocketSessionAsync("qwen3-tts-flash-realtime");
await tts.UpdateSessionAsync(new TtsRealtimeSession { Voice = "Cherry", ResponseFormat = "mp3", SampleRate = 24000 });
await tts.AppendTextAsync("你好，我是千问。");
await tts.CommitTextAsync();
await tts.FinishAsync();
var file = new FileInfo("tts-realtime.mp3");
using var stream = file.OpenWrite();
await foreach (var b in tts.GetAudioAsync())
{
    stream.WriteByte(b);
}
```

### Voice Cloning and Designing

Custom voices are managed with `CustomizeVoiceAsync` (model `voice-enrollment`, same workspace domain as the qwen-audio-tts HTTP API): clone a voice from a sample audio or design one from a text description (`Action = "create_voice"`), then list / query / update / delete voices. Which `VoiceCustomizationInput` members are required depends on the action; the preview audio of a designed voice comes back as base64 in `Output.PreviewAudio`:

```csharp
// clone a voice from a sample audio (public url or base64 data uri)
var clone = await dashScopeClient.CustomizeVoiceAsync(
    new ModelRequest<VoiceCustomizationInput, IVoiceCustomizationParameters>
    {
        Model = "voice-enrollment",
        Input = new VoiceCustomizationInput
        {
            Action = "create_voice",
            TargetModel = "qwen-audio-3.0-tts-flash",
            Prefix = "myvoice",
            Audio = "https://your-audio-url.wav",
            LanguageHints = new List<string> { "zh" }
        }
    });
var clonedVoiceId = clone.Output.VoiceId; // use it as the voice of synthesis requests

// design a voice from a text description, the preview audio comes back as base64 wav
var design = await dashScopeClient.CustomizeVoiceAsync(
    new ModelRequest<VoiceCustomizationInput, IVoiceCustomizationParameters>
    {
        Model = "voice-enrollment",
        Input = new VoiceCustomizationInput
        {
            Action = "create_voice",
            TargetModel = "cosyvoice-v3.5-plus",
            VoicePrompt = "沉稳的中年男性，音色低沉浑厚",
            PreviewText = "各位听众朋友们大家好，欢迎收听本期节目",
            Prefix = "announcer",
            LanguageHints = new List<string> { "zh" }
        },
        Parameters = new VoiceCustomizationParameters { SampleRate = 24000, ResponseFormat = "wav" }
    });
File.WriteAllBytes(
    "preview.wav",
    Convert.FromBase64String(design.Output.PreviewAudio!.Data!));

// list voices (filter by prefix), query / update / delete by voice id
var list = await dashScopeClient.CustomizeVoiceAsync(
    new ModelRequest<VoiceCustomizationInput, IVoiceCustomizationParameters>
    {
        Model = "voice-enrollment",
        Input = new VoiceCustomizationInput { Action = "list_voice", Prefix = "myvoice" }
    });
```

Created voices go through a review: `Status` is DEPLOYING while reviewing, OK when usable and UNDEPLOYED when rejected. MiniMax voices are cloned on the shared domain instead: call `GetMultimodalGenerationAsync` with `MultimodalInput.Action = "voice_clone"`, the sample url (`AudioUrl`), a globally unique `VoiceId`, and the `Text` of the audition audio (billed at the synthesis price); the audition comes back in `Output.DemoAudio`. MiniMax voices cannot be managed (listed / updated / deleted) via these APIs.

## Real-Time Speech Recognition
Create a real-time speech recognition session using `dashScopeClient.CreateSpeechRecognitionSocketSessionAsync()`.

Audio is sent to the server as binary websocket frames, and recognition results are continuously returned via `GetMessagesAsync()`. Results with `SentenceEnd` set to `false` are intermediate results of the sentence, and the one with `true` is the final result.

Note: Use the using statement to automatically dispose the session, or manually call Dispose() to release resources. Avoid reusing sessions.

```csharp
using var asr = await dashScopeClient.CreateSpeechRecognitionSocketSessionAsync("paraformer-realtime-v2");
var taskId = await asr.RunTaskAsync(
    new SpeechRecognitionParameters
    {
        Format = "wav",
        SampleRate = 16000,
        LanguageHints = ["zh"],
        MaxSentenceSilence = 800
    });
await using var audio = File.OpenRead("speech.wav");
await asr.SendAudioAsync(audio); // or send chunks yourself via SendAudioAsync(ReadOnlyMemory<byte>)
await asr.FinishTaskAsync(taskId);

var duration = 0;
await foreach (var message in asr.GetMessagesAsync())
{
    var sentence = message.Payload.Output?.Sentence;
    if (sentence?.SentenceEnd == true)
    {
        Console.WriteLine($"Recognized: {sentence.Text}");
        duration = Math.Max(duration, message.Payload.Usage?.Duration ?? 0);
    }
}

Console.WriteLine($"Billed duration: {duration}s");
```

The session is shared by the Fun-ASR-Realtime and Qwen-Audio ASR models as well, which support the conversation context, instant hot words and more (see `SpeechRecognitionParameters` for the members each model supports):

- `fun-asr-realtime`: intermediate results are always returned, and the words of the final result carry settled timestamps (`Fixed`). Supports the conversation context, `VocabularyId` and `LanguageHints` (one value takes effect).
- `qwen-audio-3.1-asr-flash-message`: returns the final result of each sentence only, set `IntermediateResultEnabled` to get intermediate results as well. `DisfluencyRemovalEnabled` also removes repetitions and self-corrections from the final text. Finishing the task before any audio was sent fails with `NO_VALID_AUDIO_ERROR`.
- `qwen-audio-3.1-asr-flash-streaming` / `qwen-audio-3.0-asr-flash-streaming`: intermediate results are always returned. `SpecialWordFilter` replaces or removes sensitive words. 3.1 reports token usage, 3.0 reports the audio duration it is billed by.

The conversation context (previous turns of the user's speech and the LLM's replies) improves the recognition of proper nouns: pass it in the input of `RunTaskAsync` and update it while the task is running with `ContinueTaskAsync` (message model only):

```csharp
using var asr = await dashScopeClient.CreateSpeechRecognitionSocketSessionAsync("qwen-audio-3.1-asr-flash-message");
var taskId = await asr.RunTaskAsync(
    new SpeechRecognitionParameters
    {
        Format = "wav",
        SampleRate = 16000,
        IntermediateResultEnabled = true, // off by default for this model
        Vocabulary = new Dictionary<string, int> { ["博客园"] = 5 } // instant hot words, weight 1~5 or 50
    },
    new SpeechRecognitionInput
    {
        Context =
        [
            new SpeechRecognitionContext("user", [new SpeechRecognitionContextContent("input_text", "博客园是什么时候成立的")]),
            new SpeechRecognitionContext("assistant", [new SpeechRecognitionContextContent("text", "博客园成立于2004年。")])
        ]
    });
await using var audio = File.OpenRead("speech.wav");
await asr.SendAudioAsync(audio);
// the context can be updated while the task is running
await asr.ContinueTaskAsync(taskId, new SpeechRecognitionInput
{
    Context = [new SpeechRecognitionContext("user", [new SpeechRecognitionContextContent("input_text", "代码改变世界")])]
});
await asr.FinishTaskAsync(taskId);

var duration = 0;
await foreach (var message in asr.GetMessagesAsync())
{
    var sentence = message.Payload.Output?.Sentence;
    if (sentence?.SentenceEnd == true)
    {
        Console.WriteLine($"Recognized: {sentence.Text}");
        duration = Math.Max(duration, message.Payload.Usage?.Duration ?? 0);
    }
    else if (sentence?.Text?.Length > 0)
    {
        // intermediate results may be revised, update the text of the sentence identified by SentenceId instead of appending them
        Console.WriteLine($"Interim result of sentence {sentence.SentenceId}: {sentence.Text}");
    }
}

Console.WriteLine($"Billed duration: {duration}s");
```

Sensitive word filtering of the streaming models. The server expects the filter JSON-encoded as a string, the SDK takes care of it:

```csharp
using var asr = await dashScopeClient.CreateSpeechRecognitionSocketSessionAsync("qwen-audio-3.1-asr-flash-streaming");
var taskId = await asr.RunTaskAsync(
    new SpeechRecognitionParameters
    {
        Format = "pcm",
        SampleRate = 16000,
        SpecialWordFilter = new SpeechRecognitionSpecialWordFilter
        {
            SystemReservedFilter = true, // filtering is off by default
            FilterWithSigned = new SpeechRecognitionSpecialWordList { WordList = ["代码"] }, // replaced with **
            FilterWithEmpty = new SpeechRecognitionSpecialWordList { WordList = ["世界"] } // removed
        }
    });
// send audio and read the results the same way as above
```

Read the usage from the final result of each sentence, the `task-finished` event does not always carry it.

### Qwen3-ASR-Flash-Realtime
`qwen3-asr-flash-realtime` models use a separate realtime session (`CreateAsrRealtimeSocketSessionAsync`), which talks to the `/api-ws/v1/realtime` endpoint with event-based messages: configure the session (audio format, language, VAD) with `UpdateSessionAsync`, stream the audio with `AppendAudioAsync` (base64 encoded inside the messages, no binary frames) and end it with `FinishAsync`. The server closes the connection after `session.finished`, so a session cannot be reused.

The session starts in the VAD mode, where the server detects speech boundaries and submits the audio automatically, delivering incremental results in `conversation.item.input_audio_transcription.text` events (the accumulated text arrives in `Stash`, `Text` stays empty) and the final one in `...completed` (with the token usage). Leave `TurnDetection` at its default to keep the server's VAD settings, or set a configuration to tune them. Setting it to null (sent as an explicit `turn_detection` null) switches to the manual mode, where you call `CommitAudioAsync` to submit the buffered audio:

```csharp
using var asr = await dashScopeClient.CreateAsrRealtimeSocketSessionAsync("qwen3-asr-flash-realtime");
await asr.UpdateSessionAsync(
    new AsrRealtimeSession
    {
        InputAudioFormat = "pcm", // or opus
        SampleRate = 16000, // or 8000
        InputAudioTranscription = new AsrRealtimeTranscription { Language = "zh" }, // unset to auto detect
        // the VAD mode with custom settings; leave it unset to keep the server settings,
        // null switches to the manual mode (commit below)
        TurnDetection = new AsrRealtimeTurnDetection { Threshold = 0.0f, SilenceDurationMs = 400 }
    });
await using var audio = File.OpenRead("speech.pcm");
await asr.AppendAudioAsync(audio); // sent as base64 chunks of 3200 bytes
// manual mode only: submit the buffered audio for recognition
// await asr.CommitAudioAsync();
// VAD mode only: give the server a moment after the audio, see below
await Task.Delay(TimeSpan.FromSeconds(1));
await asr.FinishAsync();

await foreach (var e in asr.GetEventsAsync())
{
    switch (e.Type)
    {
        case "conversation.item.input_audio_transcription.text":
            Console.WriteLine($"Interim: {e.Stash}");
            break;
        case "conversation.item.input_audio_transcription.completed":
            Console.WriteLine($"Recognized: {e.Transcript} (language: {e.Language}, emotion: {e.Emotion})");
            break;
    }
}
```

In the VAD mode, do not call `FinishAsync` right after the last audio: `input_audio_buffer.append` has no acknowledgement, and a finish that arrives before the server has consumed the buffered audio ends the session without any transcription. Pushing a 4 second clip in one message lost it every time, in 3200 byte chunks (the `Stream` overload above) it takes about 300 ms, so wait a second to be safe. A live microphone stream delivers the audio continuously and does not run into this.

## Real-Time Voice Conversation (Qwen-Audio-Realtime)
The qwen-audio-3.x-realtime models (plus / flash) are full-duplex voice assistants: stream the user audio in, the server runs VAD / ASR / LLM / TTS in a pipeline and streams back the response text and audio. Create a session with `CreateAudioChatSocketSessionAsync` (same `/api-ws/v1/realtime` endpoint, event-based messages):

```csharp
using var chat = await dashScopeClient.CreateAudioChatSocketSessionAsync("qwen-audio-3.1-realtime-plus");
await chat.UpdateSessionAsync(
    new AudioChatSession
    {
        Voice = "longanqian", // longanqian_v3.1 on 3.1 plus
        Instructions = "You are a helpful assistant.", // system prompt of the session
        TurnDetection = new AudioChatTurnDetection
        {
            Type = "server_vad", // or "smart_turn": meaningless sounds ("um") do not trigger a turn
            Threshold = 0.5f,
            SilenceDurationMs = 500
        }
        // set TurnDetection = null instead for the push-to-talk mode: commit the audio with
        // CommitAudioAsync() and trigger the inference with CreateResponseAsync()
    });

// consume the events while the audio streams in (see below), then send the audio
await using var audio = File.OpenRead("speech.pcm"); // raw pcm, 16kHz 16bit mono
await chat.AppendAudioAsync(audio);
```

In the server_vad / smart_turn mode the server detects the speech boundaries and triggers the inference automatically; the interim ASR results arrive as `conversation.item.input_audio_transcription.delta` events (`Text` is the confirmed part, `Stash` the tentative remainder), the streamed response text and audio as `response.audio_transcript.delta` / `response.audio.delta` (base64 pcm, 24kHz — also available decoded via `GetAudioAsync()`), and a turn ends with `response.done`:

```csharp
var consuming = Task.Run(async () =>
{
    // ReSharper disable once AccessToDisposedClosure
    await foreach (var e in chat.GetEventsAsync())
    {
        switch (e.Type)
        {
            case "conversation.item.input_audio_transcription.delta":
                Console.WriteLine($"Heard: {e.Text}{e.Stash}");
                break;
            case "response.audio_transcript.delta":
                Console.WriteLine($"Said: {e.Delta}");
                break;
        }
    }
});
await using var file = File.Create("response.pcm");
await foreach (var b in chat.GetAudioAsync())
{
    file.WriteByte(b);
}
```

Beyond the audio loop the session also supports text input and history injection (`CreateItemAsync` with message items), function calling (`Tools` in the session config, execute the call and write the result back with a `function_call_output` item, then trigger the next turn with `CreateResponseAsync`), interrupting the model (`CancelResponseAsync`), and managing the conversation (`RetrieveItemAsync` / `DeleteItemAsync`). The 3.1 plus model additionally takes `InputAudioTranscription.Language` / `OutputAudio.Language` (both directions of translation-like control) and `MaxHistoryTurns`; smart_turn accepts `VoiceprintAudioUrls` for speaker enhancement. The session ends when it is disposed — there is no session.finish.

## Real-Time Multimodal Conversation (Qwen-Omni-Realtime)
The qwen3.8-omni-flash-realtime, qwen3.5-omni-plus-realtime and qwen3.5-omni-flash-realtime models understand speech, images (video frames) and text, and answer in speech and text - with function calling, remote MCP tools and web search on top. Create a session with `CreateOmniRealtimeSocketSessionAsync` (same `/api-ws/v1/realtime` endpoint, event-based messages). The Bailian documentation serves qwen3.8-omni-flash-realtime on the workspace domain only, configure `WorkspaceId` on the client for it:

```csharp
using var chat = await dashScopeClient.CreateOmniRealtimeSocketSessionAsync("qwen3.8-omni-flash-realtime");
await chat.UpdateSessionAsync(
    new OmniRealtimeSession
    {
        Voice = "Tina", // the default; the voices a model takes are listed in the Bailian documentation, an unsupported one fails the response
        Instructions = "你是个人助理小云，请你准确且友好地解答用户的问题，始终以乐于助人的态度回应。", // system prompt of the session
        TurnDetection = new OmniRealtimeTurnDetection
        {
            Type = "server_vad", // or "semantic_vad": backchannel responses and background noise do not end a turn
            Threshold = 0.5f,
            SilenceDurationMs = 800
        }
        // set TurnDetection = null instead for the manual mode (push-to-talk, see below)
    });

// consume the events while the audio streams in (see below), then send the audio
await using var audio = File.OpenRead("speech.pcm"); // raw pcm, 16kHz 16bit mono
await chat.AppendAudioAsync(audio);
// the server only detects the end of the speech after some silence, which a live microphone keeps
// delivering: with a recorded clip keep appending silence until the response is done
// AppendImageAsync(frame) sends video frames as base64 jpg, about one per second
```

In the VAD mode the server detects the speech boundaries, commits the audio and triggers the response by itself: the recognized speech arrives as `conversation.item.input_audio_transcription.delta` events (`Text` is the confirmed part, `Stash` the tentative remainder), the response text as `response.audio_transcript.delta` events, the audio as `response.audio.delta` (base64 pcm, 24kHz — also available decoded via `GetAudioAsync()`), and a turn ends with `response.done` carrying the usage:

```csharp
var consuming = Task.Run(async () =>
{
    // ReSharper disable once AccessToDisposedClosure
    await foreach (var e in chat.GetEventsAsync())
    {
        switch (e.Type)
        {
            case "conversation.item.input_audio_transcription.delta":
                Console.WriteLine($"Heard: {e.Text}{e.Stash}");
                break;
            case "response.audio_transcript.delta":
            case "response.text.delta": // text only responses, see the modalities below
                Console.WriteLine($"Said: {e.Delta}");
                break;
            case "conversation.item.created" when e.Item?.Type == "mcp_approval_request":
                await chat.RespondToMcpApprovalAsync(e.Item.Id); // approve the MCP tool call the server waits for
                break;
        }
    }
});
await using var file = File.Create("response.pcm");
await foreach (var b in chat.GetAudioAsync())
{
    file.WriteByte(b);
}
```

In the manual mode (`TurnDetection = null`, sent as an explicit `turn_detection` null) nothing happens until the audio is committed and the response is requested, e.g. for a push-to-talk button. Text goes in the same way, as a user message item: `CreateItemAsync` with `Type: "message"`, `Role: "user"` and an `input_text` content, followed by `CreateResponseAsync()`:

```csharp
await chat.UpdateSessionAsync(new OmniRealtimeSession { TurnDetection = null });
await using var audio = File.OpenRead("speech.pcm");
await chat.AppendAudioAsync(audio);
await chat.AppendImageAsync(await File.ReadAllBytesAsync("frame.jpg")); // optional: the frames of the turn, after its audio started
var itemId = await chat.CommitAudioAsync(); // turns the audio (and the images) into a user message item
var response = await chat.CreateResponseAsync(); // completes at response.done, after the streamed deltas
Console.WriteLine(response.Output![0].Content![0].Transcript);
```

### Function calling and MCP tools
Configure `Tools` in the session: a `function` tool is executed by the client, a `mcp` tool is a remote MCP server (public https, streamable HTTP) whose tools the server discovers and executes. The two can be combined, neither with the web search (`EnableSearch`). A response that needs a function ends with `function_call` items in its output: execute them, write the results back and trigger the next response:

```csharp
await chat.UpdateSessionAsync(
    new OmniRealtimeSession
    {
        TurnDetection = null,
        Tools = new List<OmniRealtimeTool>
        {
            new(
                Type: "function",
                Function: new OmniRealtimeFunction(
                    "get_current_weather",
                    "当你想查询指定城市的天气时非常有用。",
                    new { type = "object", properties = new { location = new { type = "string" } }, required = new[] { "location" } }))
        }
    });
// ... append and commit the audio asking for the weather, then:
var response = await chat.CreateResponseAsync();
var call = response.Output!.First(o => o.Type == "function_call");
// execute the function, then:
await chat.CreateItemAsync(
    new OmniRealtimeItem { Type = "function_call_output", CallId = call.CallId, Output = "北京今天天气为霾转晴，气温4/-4℃，微风" });
var answer = await chat.CreateResponseAsync();
```

For an MCP tool use `new OmniRealtimeTool(Type: "mcp", ServerLabel: "deepwiki", ServerUrl: "https://mcp.deepwiki.com/mcp", RequireApproval: "always")` instead. The tools are discovered right after the session was updated (`mcp_list_tools.*` events; only responses created after `mcp_list_tools.completed` can use them). With `RequireApproval` set to `always` (the default) the server asks before each call with a `conversation.item.created` event carrying an `mcp_approval_request` item - answer it with `RespondToMcpApprovalAsync(itemId, approve: true)` while consuming the events, as in the loop above (`never` executes without asking). The `CreateResponseAsync` in flight then completes with a response whose output holds the `mcp_call` items (`Output`, or `Error` when 