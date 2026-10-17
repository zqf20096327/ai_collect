<div align="center">

# OpenRouter PHP

**A modern, fully-typed PHP client for the [OpenRouter](https://openrouter.ai) API.**

One elegant interface to hundreds of LLMs — chat, streaming, tool calling, structured outputs, conversation memory, a knowledge base, automatic retries, and a fully test-friendly architecture. No framework required.

[English](#-english) • [فارسی](#-فارسی)

[![Latest Version](https://img.shields.io/packagist/v/hojjatjh/openrouter-php.svg?style=flat-square)](https://packagist.org/packages/hojjatjh/openrouter-php)
[![Total Downloads](https://img.shields.io/packagist/dt/hojjatjh/openrouter-php.svg?style=flat-square)](https://packagist.org/packages/hojjatjh/openrouter-php)
[![PHP Version](https://img.shields.io/packagist/php-v/hojjatjh/openrouter-php.svg?style=flat-square)](https://packagist.org/packages/hojjatjh/openrouter-php)
[![License](https://img.shields.io/packagist/l/hojjatjh/openrouter-php.svg?style=flat-square)](LICENSE)

</div>

---

## 🇬🇧 English

OpenRouter gives you a single, OpenAI-compatible gateway to hundreds of models from many providers. **OpenRouter PHP** wraps that gateway in a clean, dependency-free, strongly-typed PHP package so you can ship AI features in minutes instead of hand-rolling cURL calls.

### 📑 Table of Contents

- [Why This Library](#-why-this-library)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage](#-usage)
  - [Chat](#-chat)
  - [Message Helpers](#-message-helpers)
  - [Streaming](#-streaming)
  - [Tool Calling](#-tool-calling)
  - [Structured Outputs](#-structured-outputs)
  - [Conversation Memory](#-conversation-memory)
  - [Knowledge Base](#-knowledge-base)
  - [Model Fallback and Routing](#-model-fallback-and-routing)
  - [Automatic Retries](#-automatic-retries)
  - [Helper Endpoints](#-helper-endpoints)
- [Error Handling](#-error-handling)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

### 💡 Why This Library

- **One API, every model.** Switch between OpenAI, Anthropic, Google, Meta, Mistral and more by changing a single string.
- **Batteries included.** Streaming, tools, JSON schema, memory, retries and a knowledge base are built in — not left as an exercise.
- **Typed and predictable.** Rich response objects and a dedicated exception per HTTP status mean fewer surprises in production.
- **Testable by design.** The network layer sits behind a `Transport` interface, so your tests never touch the internet.
- **Zero dependencies.** Pure PHP plus `ext-curl` — drop it into any project or framework.

### ✨ Features

- 💬 **Chat completions** — simple string prompts or full message arrays
- 🌊 **Streaming** — token-by-token responses through a callback (SSE)
- 🛠️ **Tool / function calling** — define tools and drive the tool-call loop
- 📐 **Structured outputs** — force valid JSON or a strict JSON Schema
- 🧠 **Conversation memory** — stateful chats, with optional **persistent** storage on disk
- 📚 **Knowledge base** — ground answers on your own data
- 🔁 **Automatic retries** — exponential backoff with jitter for transient failures
- 📊 **Helper endpoints** — list models, check credits, inspect generation stats and cost
- 🧯 **Rich exceptions** — a precise exception per HTTP error code
- 🧪 **Test-friendly** — a `Transport` interface lets you mock the network entirely
- 🪶 **Zero dependencies** — pure PHP + `ext-curl`, framework-agnostic

### 📦 Requirements

- PHP **8.1** or higher
- `ext-curl`, `ext-json`

### ⬇️ Installation

Install the package via [Composer](https://getcomposer.org):

```bash
composer require hojjatjh/openrouter-php
```

### 🚀 Quick Start

Create a client with your API key and send your first prompt:

```php
<?php

require 'vendor/autoload.php';

use OpenRouter\\OpenRouter;

$client = new OpenRouter(
    apiKey: getenv('OPENROUTER_API_KEY'),
    options: ['default_model' => 'openrouter/free'],
);

echo $client->chat('Explain recursion in one sentence.')->content();
```

> 🔑 Grab your API key at [openrouter.ai/keys](https://openrouter.ai/keys). **Never hard-code it** — read it from an environment variable instead.

### ⚙️ Configuration

Every option is passed through the second constructor argument. The defaults are sensible, so you only set what you need:

```php
$client = new OpenRouter(
    apiKey: getenv('OPENROUTER_API_KEY'),
    options: [
        'base_url'        => 'https://openrouter.ai/api/v1', // API base URL
        'default_model'   => 'openrouter/free',              // used when a call omits 'model'
        'referer'         => 'https://your-app.com',         // sent as HTTP-Referer
        'title'           => 'My App',                       // sent as X-Title
        'timeout'         => 60,   // request timeout in seconds
        'connect_timeout' => 10,   // connection timeout in seconds
        'max_retries'     => 2,    // retry attempts (0 disables retries)
        'retry_delay_ms'  => 500,  // base backoff delay in milliseconds
    ],
);
```

### 🧭 Usage

#### 💬 Chat

Pass a single string for a quick prompt, or a full array of messages for complete control. The returned `ChatResponse` exposes the content, the model that actually answered, the finish reason, and token usage.

```php
use OpenRouter\\Support\\Message;

// Shortcut: a single user message
$res = $client->chat('Hello!');

// Full control with a message array
$res = $client->chat([
    Message::system('You are a helpful assistant.'),
    Message::user('Give me three PHP tips.'),
], ['model' => 'openai/gpt-4o-mini', 'temperature' => 0.7]);

echo $res->content();       // the assistant's reply
echo $res->model();         // model that actually answered
echo $res->finishReason();  // stop | length | tool_calls | ...
print_r($res->usage());     // prompt/completion token counts
```

Per-request `options` are merged straight into the request body, so **any** OpenRouter parameter works out of the box (`max_tokens`, `top_p`, `reasoning`, and more).

#### 🧱 Message Helpers

Build well-formed messages without memorizing the wire format — including multimodal image inputs:

```php
use OpenRouter\\Support\\Message;

Message::system('You are concise.');
Message::user('Hi');
Message::assistant('Hello, how can I help?');
Message::tool($toolCallId, 'the tool result');

// Multimodal
Message::image('What is in this picture?', ['https://example.com/cat.jpg']);
Message::imageFile('/path/to/local.png'); // embedded as a data URI
```

#### 🌊 Streaming

Stream the answer token-by-token for a responsive, real-time UX. Your callback receives each chunk as it arrives, and the fully-assembled `ChatResponse` is returned once the stream ends.

```php
$client->chatStream(
    'Write a short poem about the sea.',
    function (string $chunk): void {
        echo $chunk; // printed as it arrives
        flush();
    },
);
```

#### 🛠️ Tool Calling

Let the model call your own functions. Define the tools, run whatever the model requests, feed the results back, and get a final grounded answer:

```php
use OpenRouter\\Support\\Tool;
use OpenRouter\\Support\\Message;

$tools = [
    Tool::define('get_weather', 'Get the current weather for a city', [
        'type' => 'object',
        'properties' => [
            'city' => ['type' => 'string', 'description' => 'City name'],
        ],
        'required' => ['city'],
    ]),
];

$messages = [Message::user('What is the weather in Tehran?')];

$res = $client->chat($messages, ['tools' => $tools]);

if ($res->hasToolCalls()) {
    // 1) keep the assistant message (it carries the tool calls)
    $messages[] = $res->message();

    // 2) run each requested tool and append its result
    foreach ($res->toolCalls() as $call) {
        $result = myWeatherLookup($call->arguments['city']); // your code
        $messages[] = Message::tool($call->id, $result);
    }

    // 3) send everything back to get the final answer
    $res = $client->chat($messages, ['tools' => $tools]);
}

echo $res->content();
```

#### 📐 Structured Outputs

Guarantee machine-readable results by forcing the model to answer with valid JSON that matches your schema. Use `json()` for free-form JSON, or `schema()` for a strict, validated shape:

```php
use OpenRouter\\Support\\ResponseFormat;

$schema = [
    'type' => 'object',
    'properties' => [
        'title'     => ['type' => 'string'],
        'sentiment' => ['type' => 'string', 'enum' => ['positive', 'neutral', 'negative']],
    ],
    'required'             => ['title', 'sentiment'],
    'additionalProperties' => false,
];

$res = $client->chat('Analyze: \"What a wonderful day!\"', [
    'response_format' => ResponseFormat::schema('analysis', $schema),
]);

$data = $res->json(); // decoded associative array
echo $data['sentiment']; // \"positive\"
```

#### 🧠 Conversation Memory

Keep context across turns with a stateful conversation. It remembers previous messages automatically:

```php
$chat = $client->conversation();
$chat->system('You are a friendly assistant.');

echo $chat->send('My name is Hojjat.')->content();
echo $chat->send('What is my name?')->content(); // remembers: \"Hojjat\"
```

**Persistent memory** survives process restarts by saving history to disk. Implement the `ConversationStore` interface to store history anywhere (a database, Redis, etc.):

```php
use OpenRouter\\Memory\\JsonFileStore;

$store = new JsonFileStore(__DIR__ . '/storage/chat.json');
$chat  = $client->conversation(store: $store); // loads existing history if present

if (! $chat->hasHistory()) {
    $chat->system('You are a friendly assistant.');
}

$chat->send('Remember that my favorite color is blue.');
// On the next run, from a fresh process, history is loaded automatically.
```

#### 📚 Knowledge Base

Ground the model on your own facts to reduce hallucinations. Add snippets or files, then feed the generated prompt to a conversation:

```php
use OpenRouter\\Knowledge\\KnowledgeBase;

$kb = (new KnowledgeBase())
    ->instruction('Answer only from the knowledge below. If unknown, say so.')
    ->add('Our store is open Sat–Wed, 9 to 17.')
    ->addFile(__DIR__ . '/faq.txt');

$chat = $client->conversation();
$chat->system($kb->toSystemPrompt());

echo $chat->send('When are you open?')->content();
```

> For very large corpora, prefer a retrieval (RAG) approach and feed only the relevant chunks.

#### 🔁 Model Fallback and Routing

Because per-request options pass straight through, resilient routing needs no extra code — try several models in order, or express provider preferences:

```php
$res = $client->chat($messages, [
    'models' => ['openai/gpt-4o-mini', 'openrouter/free'], // tried in order
    'route'  => 'fallback',
]);

$res = $client->chat($messages, [
    'provider' => ['order' => ['OpenAI', 'Together'], 'allow_fallbacks' => true],
]);
```

#### 🔂 Automatic Retries

Transient failures — network drops, `429`, and `5xx` — are retried automatically with exponential backoff and jitter. Tune or disable this via `max_retries` and `retry_delay_ms`. Permanent errors (such as `401` or `400`) are **never** retried.

#### 📊 Helper Endpoints

Inspect the platform beyond chat: list available models, check your credit balance, and pull cost and token stats for any generation:

```php
$models  = $client->models();   // available models + pricing
$credits = $client->credits();  // ['total_credits' => ..., 'total_usage' => ...]

$res   = $client->chat('Hi');
$stats = $client->generation($res->id()); // cost & token stats for that request
```

### 🧯 Error Handling

Every failure maps to a dedicated exception, all extending `OpenRouterException`, so you can catch exactly what you care about:

| HTTP status | Exception |
|-------------|-----------|
| 400 | `BadRequestException` |
| 401 | `AuthenticationException` |
| 402 | `InsufficientCreditsException` |
| 403 | `PermissionException` |
| 404 | `NotFoundException` |
| 408 / 524 | `TimeoutException` |
| 429 | `RateLimitException` |
| 5xx | `ServerException` |
| network | `TransportException` |

```php
use OpenRouter\\Exceptions\\AuthenticationException;
use OpenRouter\\Exceptions\\RateLimitException;
use OpenRouter\\Exceptions\\OpenRouterException;

try {
    $res = $client->chat('Hello');
} catch (AuthenticationException $e) {
    // invalid API key
} catch (RateLimitException $e) {
    // slow down
} catch (OpenRouterException $e) {
    // any other API/transport error
    echo $e->getMessage();
}
```

### 🧪 Testing

The client depends on a `Transport` interface, so you can inject a fake implementation and test your code without hitting the network:

```php
$client = new OpenRouter('test-key', ['default_model' => 'openrouter/free'], $fakeTransport);
```

Run the full test suite with:

```bash
vendor/bin/phpunit
```

### 🤝 Contributing

Contributions are welcome! Please open an issue to discuss significant changes first, keep the code style consistent, and make sure `vendor/bin/phpunit` passes before submitting a pull request.

### 📄 License

Released under the [MIT License](LICENSE).

---

<div dir="rtl">

## 🇮🇷 فارسی

سرویس OpenRouter یک درگاه واحد و سازگار با OpenAI است که به صدها مدل از ارائه‌دهنده‌های مختلف دسترسی می‌دهد. کتابخانه‌ی **OpenRouter PHP** این درگاه را در یک پکیج تمیز، بدون وابستگی و کاملاً type-safe بسته‌بندی می‌کند تا به‌جای نوشتن دستیِ درخواست‌های cURL، در چند دقیقه قابلیت‌های هوش مصنوعی را به پروژه‌ات اضافه کنی.

### 💡 چرا این کتابخانه؟

- **یک API، همه‌ی مدل‌ها.** با تغییر یک رشته‌ی ساده بین OpenAI، Anthropic، Google، Meta، Mistral و بقیه جابه‌جا شو.
- **همه‌چیز آماده است.** استریم، ابزارها، JSON Schema، حافظه، تلاش مجدد و پایگاه دانش از پیش ساخته شده‌اند.
- **تایپ‌دار و قابل‌پیش‌بینی.** آبجکت‌های پاسخِ غنی و یک استثنای مجزا برای هر کد خطای HTTP، غافل‌گیری در محیط عملیاتی را کم می‌کنند.
- **تست‌پذیر از پایه.** لایه‌ی شبکه پشت interface به نام `Transport` قرار دارد؛ پس تست‌هایت هرگز به اینترنت وصل نمی‌شوند.
- **بدون وابستگی.** فقط PHP خالص و `ext-curl` — در هر پروژه یا فریم‌ورکی قابل استفاده است.

### ✨ قابلیت‌ها

- 💬 **چت** — با یک رشته‌ی ساده یا آرایه‌ی کامل پیام‌ها
- 🌊 **استریم** — دریافت پاسخ توکن‌به‌توکن با callback
- 🛠️ **Tool / Function Calling** — تعریف ابزار و مدیریت چرخه‌ی فراخوانی
- 📐 **خروجی ساختارمند** — گرفتن JSON معتبر یا مطابق یک JSON Schema دقیق
- 🧠 **حافظه‌ی گفتگو** — گفتگوی حالت‌دار، همراه با ذخیره‌سازی **ماندگار** روی دیسک
- 📚 **پایگاه دانش** — پاسخ‌دهی بر اساس داده‌های خودت
- 🔁 **تلاش مجدد خودکار** — backoff نمایی برای خطاهای گذرا
- 📊 **اندپوینت‌های کمکی** — لیست مدل‌ها، اعتبار حساب، آمار و هزینه‌ی هر درخواست
- 🧯 **خطاهای دقیق** — یک استثنای مجزا برای هر کد خطای HTTP
- 🧪 **مناسب تست** — با interface به نام `Transport` می‌توانی شبکه را کامل شبیه‌سازی کنی
- 🪶 **بدون وابستگی** — فقط PHP خالص و `ext-curl`

### 📦 پیش‌نیازها

- PHP نسخه‌ی **۸.۱** یا بالاتر
- افزونه‌های `ext-curl` و `ext-json`

### ⬇️ نصب

پکیج را با [Composer](https://getcomposer.org) نصب کن:

<div dir="ltr">

```bash
composer require hojjatjh/openrouter-php
```

</div>

### 🚀 شروع سریع

یک کلاینت با کلید API خود بساز و اولین درخواست را بفرست:

<div dir="ltr">

```php
<?php

require 'vendor/autoload.php';

use OpenRouter\\OpenRouter;

$client = new OpenRouter(
    apiKey: getenv('OPENROUTER_API_KEY'),
    options: ['default_model' => 'openrouter/free'],
);

echo $client->chat('بازگشتی (recursion) را در یک جمله توضیح بده.')->content();
```

</div>

> 🔑 کلید API را از [openrouter.ai/keys](https://openrouter.ai/keys) بگیر و **هیچ‌وقت مستقیم در کد ننویس** — آن را از یک متغیر محیطی بخوان.

### ⚙️ پیکربندی

همه‌ی تنظیمات از طریق آرگومان دوم سازنده پاس داده می‌شوند. مقادیر پیش‌فرض منطقی‌اند، پس فقط چیزی را که لازم داری تنظیم کن:

<div dir="ltr">

```php
$client = new OpenRouter(
    apiKey: getenv('OPENROUTER_API_KEY'),
    options: [
        'base_url'        => 'https://openrouter.ai/api/v1', // API base URL
        'default_model'   => 'openrouter/free',              // used when a call omits 'model'
        'referer'         => 'https://your-app.com',         // sent as HTTP-Referer
        'title'           => 'My App',                       // sent as X-Title
        'timeout'         => 60,   // request timeout (seconds)
        'connect_timeout' => 10,   // connection timeout (seconds)
        'max_retries'     => 2,    // retry attempts (0 disables retries)
        'retry_delay_ms'  => 500,  // base backoff delay (milliseconds)
    ],
);
```

</div>

### 🧭 راهنمای استفاده

#### 💬 چت

برای یک درخواست سریع، یک رشته بده؛ یا برای کنترل کامل، آرایه‌ای از پیام‌ها. آبجکت `ChatResponse` بازگشتی، محتوا، مدلی که واقعاً پاسخ داده، دلیل پایان و مصرف توکن را در اختیارت می‌گذارد.

<div dir="ltr">

```php
use OpenRouter\\Support\\Message;

// Shortcut: a single user message
$res = $client->chat('سلام!');

// Full control with a messages array
$res = $client->chat([
    Message::system('تو یک دستیار مفید هستی.'),
    Message::user('سه نکته‌ی PHP بگو.'),
], ['model' => 'openai/gpt-4o-mini', 'temperature' => 0.7]);

echo $res->content();
echo $res->model();
echo $res->finishReason();
print_r($res->usage());
```

</div>

هر `option` که برای یک درخواست بدهی، مستقیم به بدنه‌ی درخواست اضافه می‌شود؛ پس هر پارامتر OpenRouter بدون کد اضافه کار می‌کند.

#### 🧱 هلپرهای پیام

بدون به‌خاطر سپردن قالب داخلی، پیام‌های درست بساز — از جمله ورودی تصویری (multimodal):

<div dir="ltr">

```php
use OpenRouter\\Support\\Message;

Message::system('کوتاه جواب بده.');
Message::user('سلام');
Message::assistant('سلام، چطور کمکت کنم؟');
Message::tool($toolCallId, 'نتیجه‌ی ابزار');

// Multimodal
Message::image('توی این عکس چیست؟', ['https://example.com/cat.jpg']);
Message::imageFile('/path/to/local.png');
```

</div>

#### 🌊 استریم

پاسخ را توکن‌به‌توکن استریم کن تا تجربه‌ی کاربری زنده و بلادرنگ داشته باشی. callback تو هر تکه را به‌محض رسیدن می‌گیرد و بعد از پایان استریم، همان `ChatResponse` کامل بازگردانده می‌شود.

<div dir="ltr">

```php
$client->chatStream(
    'یک شعر کوتاه درباره‌ی دریا بگو.',
    function (string $chunk): void {
        echo $chunk;
        flush();
    },
);
```

</div>

#### 🛠️ فراخوانی ابزار (Tool Calling)

بگذار مدل توابع خودت را صدا بزند. ابزارها را تعریف کن، هر چیزی را که مدل درخواست کرد اجرا کن، نتیجه را برگردان و پاسخ نهایی و مستند را بگیر:

<div dir="ltr">

```php
use OpenRouter\\Support\\Tool;
use OpenRouter\\Support\\Message;

$tools = [
    Tool::define('get_weather', 'گرفتن آب‌وهوای فعلی یک شهر', [
        'type' => 'object',
        'properties' => [
            'city' => ['type' => 'string', 'description' => 'نام شهر'],
        ],
        'required' => ['city'],
    ]),
];

$messages = [Message::user('هوای تهران چطور است؟')];

$res = $client->chat($messages, ['tools' => $tools]);

if ($res->hasToolCalls()) {
    // keep the assistant message (it carries the tool calls)
    $messages[] = $res->message();

    // run each requested tool and append its result
    foreach ($res->toolCalls() as $call) {
        $result = myWeatherLookup($call->arguments['city']);
        $messages[] = Message::tool($call->id, $result);
    }

    // send everything back to get the final answer
    $res = $client->chat($messages, ['tools' => $tools]);
}

echo $res->content();
```

</div>

#### 📐 خروجی ساختارمند

با مجبور کردن مدل به پاسخ در قالب JSON معتبرِ منطبق بر اسکیمای تو، نتیجه‌ی ماشین‌خوان تضمین کن. برای JSON آزاد از `json()` و برای قالب دقیق و اعتبارسنجی‌شده از `schema()` استفاده کن:

<div dir="ltr">

```php
use OpenRouter\\Support\\ResponseFormat;

$schema = [
    'type' => 'object',
    'properties' => [
        'title'     => ['type' => 'string'],
        'sentiment' => ['type' => 'string', 'enum' => ['positive', 'neutral', 'negative']],
    ],
    'required'             => ['title', 'sentiment'],
    'additionalProperties' => false,
];

$res = $client->chat('این متن را تحلیل کن: What a wonderful day!', [
    'response_format' => ResponseFormat::schema('analysis', $schema),
]);

$data = $res->json();
echo $data['sentiment']; // \"positive\"
```

</div>

اگر فقط JSON معتبر بدون ساختار مشخص می‌خواهی، از `ResponseFormat::json()` استفاده کن.

#### 🧠 حافظه‌ی گفتگو

با یک گفتگوی حالت‌دار، زمینه را در طول چند نوبت حفظ کن؛ پیام‌های قبلی به‌صورت خودکار به خاطر سپرده می‌شوند:

<div dir="ltr">

```php
$chat = $client->conversation();
$chat->system('تو یک دستیار خوش‌برخورد هستی.');

echo $chat->send('اسم من حجت است.')->content();
echo $chat->send('اسم من چه بود؟')->content(); // یادش می‌ماند: حجت
```

</div>

**حافظه‌ی ماندگار** با ذخیره‌ی تاریخچه روی دیسک، بین اجراهای مختلف باقی می‌ماند. برای ذخیره در دیتابیس، Redis یا هر جای دیگر، interface به نام `ConversationStore` را پیاده‌سازی کن:

<div dir="ltr">

```php
use OpenRouter\\Memory\\JsonFileStore;

$store = new JsonFileStore(__DIR__ . '/storage/chat.json');
$chat  = $client->conversation(store: $store); // loads existing history

if (! $chat->hasHistory()) {
    $chat->system('تو یک دستیار خوش‌برخورد هستی.');
}

$chat->send('یادت باشد رنگ موردعلاقه‌ام آبی است.');
// On the next run, from a fresh process, history is loaded automatically.
```

</div>

#### 📚 پایگاه دانش

برای کاهش توهم (hallucination)، مدل را روی واقعیت‌های خودت متکی کن. تکه‌ها یا فایل‌ها را اضافه کن و پرامپت ساخته‌شده را به گفتگو بده:

<div dir="ltr">

```php
use OpenRouter\\Knowledge\\KnowledgeBase;

$kb = (new KnowledgeBase())
    ->instruction('فقط بر اساس دانش زیر جواب بده. اگر نمی‌دانی، بگو نمی‌دانم.')
    ->add('ساعت کاری فروشگاه: شنبه تا چهارشنبه، ۹ تا ۱۷.')
    ->addFile(__DIR__ . '/faq.txt');

$chat = $client->conversation();
$chat->system($kb->toSystemPrompt());

echo $chat->send('کی باز هستید؟')->content();
```

</div>

> برای حجم دانش خیلی زیاد، بهتر است از روش بازیابی (RAG) استفاده کنی و فقط تکه‌های مرتبط را بفرستی.

#### 🔁 fallback مدل و مسیریابی

چون option های هر درخواست مستقیم پاس داده می‌شوند، مسیریابیِ مقاوم بدون کد اضافه کار می‌کند — چند مدل را به‌ترتیب امتحان کن یا ترجیح provider را مشخص کن:

<div dir="ltr">

```php
$res = $client->chat($messages, [
    'models' => ['openai/gpt-4o-mini', 'openrouter/free'], // tried in order
    'route'  => 'fallback',
]);

$res = $client->chat($messages, [
    'provider' => ['order' => ['OpenAI', 'Together'], 'allow_fallbacks' => true],
]);
```

</div>

#### 🔂 تلاش مجدد خودکار

خطاهای گذرا — قطعی شبکه، `429` و `5xx` — به‌صورت خودکار با backoff نمایی و jitter دوباره تلاش می‌شوند. با `max_retries` و `retry_delay_ms` قابل تنظیم یا غیرفعال کردن است. خطاهای دائمی (مثل `401` و `400`) هرگز دوباره تلاش **نمی‌شوند**.

#### 📊 اندپوینت‌های کمکی

فراتر از چت، پلتفرم را بررسی کن: لیست مدل‌های موجود، موجودی اعتبار، و آمار هزینه و توکنِ هر تولید:

<div dir="ltr">

```php
$models  = $client->models();   // available models + pricing
$credits = $client->credits();  // ['total_credits' => ..., 'total_usage' => ...]

$res   = $client->chat('سلام');
$stats = $client->generation($res->id()); // cost & token stats
```

</div>

### 🧯 مدیریت خطا

هر خطا به یک استثنای مشخص نگاشت می‌شود که همه از `OpenRouterException` ارث‌بری می‌کنند؛ پس دقیقاً همان چیزی را که برایت مهم است می‌گیری:

<div dir="ltr">

| HTTP status | Exception |
|-------------|-----------|
| 400 | `BadRequestException` |
| 401 | `AuthenticationException` |
| 402 | `InsufficientCreditsException` |
| 403 | `PermissionException` |
| 404 | `NotFoundException` |
| 408 / 524 | `TimeoutException` |
| 429 | `RateLimitException` |
| 5xx | `ServerException` |
| network | `TransportException` |

```php
use OpenRouter\\Exceptions\\AuthenticationException;
use OpenRouter\\Exceptions\\RateLimitException;
use OpenRouter\\Exceptions\\OpenRouterException;

try {
    $res = $client->chat('سلام');
} catch (AuthenticationException $e) {
    // invalid API key
} catch (RateLimitException $e) {
    // slow down
} catch (OpenRouterException $e) {
    echo $e->getMessage();
}
```

</div>

### 🧪 تست

کلاینت به interface به نام `Transport` وابسته است؛ پس می‌توانی یک پیاده‌سازی قلابی تزریق کنی و بدون زدن به شبکه، کد خود را تست کنی:

<div dir="ltr">

```php
$client = new OpenRouter('test-key', ['default_model' => 'openrouter/free'], $fakeTransport);
```

```bash
vendor/bin/phpunit
```

</div>

### 🤝 مشارکت

مشارکت‌ها استقبال می‌شوند! لطفاً برای تغییرات مهم ابتدا یک issue باز کن، سبک کد را یکدست نگه دار و پیش از ارسال pull request مطمئن شو که `vendor/bin/phpunit` سبز است.

### 📄 لایسنس

تحت [لایسنس MIT](LICENSE) منتشر شده است.

</div>

---

<div align="center">
Made with ❤️ by <a href="https://github.com/hojjatjh">hojjatjh</a>
</div>
