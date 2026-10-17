I've been a paying user of ChatGPT Plus, Claude Pro, and Google Gemini Advanced since the beginning. However, for tasks involving automated text processing (summarization, transformation) of large datasets, I needed a non-GUI solution. I was using the OpenAI API, but then I discovered [OpenRouter AI](https://openrouter.ai) on February 16, 2025. OpenRouter AI offers a generous free tier, so I created `or-cli.py` to leverage it for my text processing needs. I've also added Ollama integration to use self-hosted models from [Hugging Face](https://huggingface.co/models?pipeline_tag=text-generation&sort=trending). On February 24, 2025 added [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) support as well to `or-cli.py`.

This repository serves as my adventures in learning more about AI through coding and extending `or-cli.py` :sunglasses:

# or-cli.py - OpenRouter AI Command-Line Interface

A versatile Python command-line tool for interacting with AI models through the [OpenRouter API](https://openrouter.ai/docs), supporting direct API calls, request caching via [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/), or via [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) or local model inference with [Ollama](https://ollama.ai/) which can optionally leverage [Microsoft LLMLingua](https://llmlingua.com/) prompt token compression techniques to reduce prompt token sizes. Also supports [RAG Integrations for txtAI and Cloudflare AutoRAG](#rag-integration). For OpenRouter AI API and Cloudflare Workers AI pricing, you can see the below [LLM Moddel Pricing Tables](#llm-model-pricing-tables).

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Configuration](#configuration)
  - [Cloudflare Workers AI Integration](#cloudflare-workers-ai-integration)
    - [Setting Up Cloudflare Workers AI](#setting-up-cloudflare-workers-ai)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Command-Line Arguments](#command-line-arguments)
- [List Models](#list-models)
- [Example Usage](#example-usage)
  - [RAG Integration](#rag-integration) [[demo page](examples/example-txtai-rag-1.md)]
    - [Cloudflare AutoRAG](#cloudflare-autorag) [[demo page](examples/example-cloudflare-autorag-1.md)]
      - [How Cloudflare AutoRAG Integration Works (Technical Summary)](#how-cloudflare-autorag-integration-works-technical-summary)
      - [Cloudflare AutoRAG Environment Variables Required](#cloudflare-autorag-environment-variables-required)
      - [Cloudflare AutoRAG Key Options](#cloudflare-autorag-key-options)
      - [Cloudflare AutoRAG Example](#cloudflare-autorag-example)
      - [Cloudflare AutoRAG Example --cfrag-search-only](#cloudflare-autorag-example---cfrag-search-only)
      - [Cloudflare AutoRAG Example --cfrag-search-only --multi](#cloudflare-autorag-example---cfrag-search-only---multi)
      - [Cloudflare AutoRAG Example --cfrag-search-only --eval](#cloudflare-autorag-example---cfrag-search-only---multi)
      - [Cloudflare AutoRAG with ---webpage mode](#cloudflare-autorag-with----webpage-mode)
    - [txtai](#txtai)
      - [txtai_api.py Features](#txtai_apipy-features)
      - [New or-cli.py Command-line Arguments](#new-or-clipy-command-line-arguments)
      - [How It Works - or-cli.py + txtai_api.py](#how-it-works---or-clipy--txtai_apipy)
      - [txtai RAG Examples](#txtai-rag-examples)
      - [Compatibility](#compatibility)
  - [Web Search](#web-search) [[demo page](examples/example-web-search-txtai-rag-1.md), [demo 2](examples/example-web-search-txtai-rag-2.md), [demo 3](examples/example-web-search-txtai-rag-3.md), [demo 4](examples/example-web-search-txtai-rag-4.md)]
    - [Example 1 Latest Nginx version](#example-1-latest-nginx-version)
    - [Example 2 Super Bowl 2025](#example-2-super-bowl-2025)
      - [Stream Chat With txtai RAG](#stream-chat-with-txtai-rag)
    - [Multi-Search Example](#multi-search-example)
    - [Example Linkup + Brave Search API Combined Web Search](examples/example-web-search-txtai-rag-4.md)
  - [Streaming Chat Support](#streaming-chat-support)
  - [Basic Usage](#basic-usage) [[demo page](examples/example-basic-prompts.md)]
    - [PDF Text Extraction With py-zerox](#pdf-text-extraction-with-py-zerox)
    - [PDF Text Extraction With pdf2image](#pdf-text-extraction-with-pdf2image)
    - [PDF Text Extraction](#pdf-text-extraction)
    - [PDF Text Extraction + Microsoft LLMLingua-2 Prompt Token Compression](#pdf-text-extraction-with-microsoft-llmlingua-2)
  - [Working with files](#working-with-files) [[code base inspection demo 1](examples/example-code-inspection-prompts.md), [demo 2](examples/example-code-inspection-prompts2.md), [demo 3](examples/example-code-inspection-prompts3.md)]
  - [Working with images](#working-with-images)
  - [Model Selection](#model-selection)
  - [Token Usage and Limits](#token-usage-and-limits)
  - [Prompt Compression](#prompt-compression) [[demo page](examples/example-llmlingua-compression-prompts.md)]
  - [Multi-model Features](#multi-model-features) [[demo page](examples/example-multi-model-prompts.md)]
  - [Multi-model Evaluation Features](#multi-model-evaluation-features) [[demo page](examples/example-evaluation-prompts.md)]
  - [Web Page Processing](#web-page-processing)
    - [Xenforo Thread Summary](#xenforo-thread-summary)
    - [Xenforo Large Thread Summary](examples/example-xenforo-summary-large-thread-1.md)
    - [Xenforo Thread Summary Extended With Opik Tracing](examples/example-xenforo-summary-follow-up-1.md)
    - [Xenforo Thread Summary Using Structured Schema JSON Format](examples/example-xenforo-summary-structured-schema-json-output-1.md)
  - [Local Ollama Integration](#local-ollama-integration)
  - [Conversational Exchanges](#conversational-exchanges)
  - [Structured Output](#structured-output) [[Xenforo demo page](examples/example-structured-xenforo-output.md), [demo page](examples/example-structured-output.md)]
  - [Structured Eval And Follow-Up](#structured-eval-and-follow-up)
    - [Example 1: Inline Schema for Evaluation](#example-1--inline-schema-for-evaluation)
    - [Example 2: File-Based Schema for Evaluation](#example-2--file-based-schema-for-evaluation)
    - [Example 3: Inline Schema for a Single Follow-up](#example-3--inline-schema-for-a-single-follow-up)
    - [Example 4: File-Based Schema for a Follow-up](#example-4--file-based-schema-for-a-follow-up)
  - [Tool Calling](#tool-calling)
  - [Provider Routing](#provider-routing)
  - [Online Search](#online-search)
  - [Tokenizer Count](#tokenizer-count)
  - [Prompt Templates](#prompt-templates) [[demo page](examples/example-prompt-templates.md)]
    - [Example 1 – Simple YAML Template (No Variables)](#example-1--simple-yaml-template-no-variables)
    - [Example 2 – YAML Template with a Single Variable](#example-2--yaml-template-with-a-single-variable)
    - [Example 3 – JSON Template (No Variables)](#example-3--json-template-no-variables)
    - [Example 4 – JSON Template with Variable Substitution](#example-4--json-template-with-variable-substitution)
    - [Example 5 – Multi-line YAML Template with Multiple Variables](#example-5--multi-line-yaml-template-with-multiple-variables)
    - [Example 6 – YAML Template with Two Variables on One Line](#example-6--yaml-template-with-two-variables-on-one-line)
    - [Example 7 – YAML Template Simulate Chain Of Thought](#example-7--yaml-template-simulate-chain-of-thought)
    - [Example 8 – YAML Template Simulate Chain Of Draft](#example-8--yaml-template-simulate-chain-of-draft)
    - [Example 9 – YAML Template Thorough Reasoning](#example-9--yaml-template-thorough-reasoning)
    - [Example 10 - Auto Extract Reasoning Traces](#example-10---auto-extract-reasoning-traces)
- [Technical Details](#technical-details)
  - [Functions Overview](#functions-overview)
  - [Yappi Profiling](#yappi-profiling)
- [Advanced Features](#advanced-features)
  - [Prompt Compression](#prompt-compression)
  - [Multi-model Evaluation](#multi-model-evaluation)
  - [Web Page Processing](#web-page-processing)
  - [Cloudflare AI Gateway Integration](#cloudflare-ai-gateway-integration)
    - [Cloudflare AI Gateway Custom Metadata](#cloudflare-ai-gateway-custom-metadata)
    - [Cloudflare AI Gateway Screenshots](#cloudflare-ai-gateway-screenshots)
    - [Cloudflare Workers AI Examples](#cloudflare-workers-ai-examples)
      - [Cloudflare Workers AI Gateway Screenshots](#cloudflare-workers-ai-gateway-screenshots)
  - [Local Ollama Integration](#local-ollama-integration)
- [LLM Moddel Pricing Tables](#llm-model-pricing-tables)

## Overview

`or-cli.py` is a powerful command-line interface (CLI) tool designed to communicate with AI language models through multiple pathways:

1. **Direct API Access** to OpenRouter's extensive model catalog - <https://openrouter.ai/docs/api-reference/overview>
2. **Cloudflare AI Gateway** OpenRouter API proxied for request proxying with intelligent caching - <https://developers.cloudflare.com/ai-gateway/>
3. **Cloudflare Workers AI** [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) and their hosted [LLM models](https://developers.cloudflare.com/workers-ai/models/) also via proxied Cloudflare AI Gateway.
4. **Local Ollama API** for on-premise model inference - <https://ollama.com> and use self-hosted LLM models from [Hugging Face](https://huggingface.co/models?pipeline_tag=text-generation&sort=trending)

The tool streamlines AI interactions for a wide range of applications, from simple text completions to sophisticated multi-model evaluations, webpage analysis, and token-optimized prompt engineering.

## Architecture

```text
+================================================================+
|                        or-cli.py (v1.8)                        |
+================================================================+
                              |
+---------------------------- | -----------------------------------+
| LLM PROVIDERS               v                                    |
|  +------------+  +------------+  +----------+  +---------------+ |
|  | OpenRouter |  | CF Gateway |  | CF Workers|  | Local (Ollama/| |
|  | (320+)     |  | (Cache)    |  | AI (@cf/) |  | vLLM)         | |
|  +------------+  +------------+  +----------+  +---------------+ |
+------------------------------------------------------------------+
                              |
+---------------------------- | -----------------------------------+
| RAG & SEARCH                v                                    |
|  +------------+  +------------+  +------------+  +-------------+ |
|  | CF AutoRAG |  | txtai RAG  |  | Linkup     |  | Brave       | |
|  | (R2+AI)    |  | (:7234)    |  | Search     |  | Search      | |
|  +------------+  +------------+  +------------+  +-------------+ |
+------------------------------------------------------------------+
                              |
+---------------------------- | -----------------------------------+
| PROCESSING & TOOLS          v                                    |
|  +------------+  +------------+  +------------+  +-------------+ |
|  | LLMLingua-2|  | XenForo    |  | Structured |  | Vision/     | |
|  | Compress   |  | HTML->MD   |  | Outputs    |  | Image       | |
|  +------------+  +------------+  +------------+  +-------------+ |
+------------------------------------------------------------------+
                              |
+---------------------------- | -----------------------------------+
| OBSERVABILITY               v                                    |
|  +----------------------------------------------------------+   |
|  |                     Opik Tracing                         |   |
|  |              (Local Docker :5173 / Cloud)                |   |
|  +----------------------------------------------------------+   |
+------------------------------------------------------------------+
```

## Key Features

- **Multimodal Support**: Send text prompts with optional image inputs.
- **Code-Aware Processing**: Special handling for code snippets with the `--code` flag.
- **Enhanced Webpage Handling**:
  - Convert HTML to Markdown with intelligent content extraction via `--webpage`.
  - JavaScript rendering support with `--js-render` for dynamic web content.
  - Authentication options with username/password, cookies, or custom headers.
- **Advanced Prompt Compression**: Reduce token usage by up to 60% with Microsoft LLMLingua compression techniques.
- **Multi-Model Workflows**:
  - **Evaluation Mode**: Have models evaluate each other's responses with `--eval`.
  - **Comparison Mode**: Get parallel responses from multiple models with `--multi`.
- **Conversation Support**: Maintain context across messages with `--follow-up`.
- **Usage Analytics**: Track token consumption and costs with `--tokens`.
- **Debugging Tools**: Detailed logging with `--debug` and performance profiling with `--yappi`.
- **Customizable Generation**: Fine-tune outputs with temperature, seed, top_p, and more.
- **JSON Structured Outputs**: Format responses as structured data when needed.
- **Enhanced PDF Extraction**:
  - **AI-Driven Parsing**: Use the `--pdf` flag to leverage py‑zerox for advanced PDF parsing that captures text along with images, tables, and graphs. If flag not passed, a more basic PDF extract method is used.
  - **PDF-to-Image Conversion**: Use the `--pdf2img` flag to convert PDF pages into images (via pdf2image) and embed them in Markdown for visual presentation. If flag not passed, a more basic PDF extract method is used.
- **Web Search**: Enable [LinkUP](examples/example-web-search-txtai-rag-1.md) amd [Brave Search API](examples/example-web-search-txtai-rag-2.md) web search via `--search` and `--search-api`. Works with `--rag` flag to save web
  results to txtai RAG embedded vector database.
- **Opik Tracing**: Integrated [Opik Tracing support](examples/example-xenforo-summary-follow-up-1.md) for both Opik Cloud and self-hosted Opik Docker instances (`--opik-local`). Opik tracing can be fully disabled with `--private` flag.
- **Tool Calling**: OpenAI-compatible function calling with built-in tools and custom tool definitions via `--tools` and `--tool-choice`.
- **Provider Routing**: Optimize for speed (`--routing nitro`), cost (`--routing floor`), or free tier (`--routing free`).
- **Online Search**: Native OpenRouter web search with `--online` flag (powered by Exa.ai, $4/1000 results).

## Configuration

**Configure API Keys and Environment**:

   - Set your OpenRouter API key via the `OPENROUTER_API_KEY` environment variable or the `--api-key` flag
   - For Cloudflare AI Gateway: set `USE_CLOUDFLARE_AI_GATEWAY=y`, `CF_ACCOUNT_ID`, and optionally `CF_GATEWAY_ID`
   - For Ollama: ensure your instance is running at `http://localhost:11434/v1`
   - February 24, 2024: Cloudflare Worker AI support added (see below).

### Cloudflare Workers AI Integration

`or-cli.py` now supports an alternative [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) endpoint via a separate [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/providers/workersai/) for processing requests. This is enabled via the new environment variable `USE_CLOUDFLARE_WORKERS_AI`. By default, this variable is set to `n` (disabled). When set to `y`, the tool will route requests through Cloudflare Workers AI, which omits certain parameters (such as `seed` and `max_tokens`) that are not supported by this endpoint.

The default Cloudflare Workers AI model used is currently `@cf/meta/llama-3.2-3b-instruct` <https://developers.cloudflare.com/workers-ai/models/llama-3.2-3b-instruct/>. Cloudflare Workers AI has a variety of other LLM models listed at <https://developers.cloudflare.com/workers-ai/models/>.

#### Setting Up Cloudflare Workers AI

To enable and configure Cloudflare Workers AI, set the following environment variables in your shell or environment configuration:

```bash
export USE_CLOUDFLARE_WORKERS_AI=y
export CF_API_TOKEN=your_cloudflare_api_token_here
export CF_ACCOUNT_ID=your_cloudflare_account_id_here
# Optionally, set a custom gateway ID (defaults to "workers-ai" if not set)
export CF_GATEWAY_WORKER_AI_ID=your_custom_gateway_id
```

**Notes:**

- When `USE_CLOUDFLARE_WORKERS_AI` is enabled, the CLI automatically adjusts API requests (e.g., omitting `seed` and `max_tokens`) to meet the endpoint’s requirements.
- To use the standard OpenRouter AI endpoint, ensure `USE_CLOUDFLARE_WORKERS_AI` is unset or set to `n`.
- Cloudflare Workers AI pricing <https://developers.cloudflare.com/workers-ai/platform/pricing/> and limits <https://developers.cloudflare.com/workers-ai/platform/limits/>.

## Requirements

- **Python**: 3.6 or higher

| **Dependency**   | **Description**                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| requests         | HTTP communication                                                                                |
| openai           | OpenAI SDK for API formatting                                                                     |
| aiohttp          | Asynchronous HTTP for webpage fetching                                                            |
| beautifulsoup4   | HTML parsing                                                                                      |
| trafilatura     | HTML to Markdown, JSON, CSV, XML conversion                                                       |
| htmlmin2         | HTML minification                                                                                 |
| orjson           | Fast JSON processing                                                                              |'
| json           | JSON processing                                                                              |'
| pillow           | Image processing                                                                                  |
| pygments         | Syntax highlighting and language detection                                                        |
| jsmin            | JavaScript minification                                                                           |
| cssmin           | CSS minification                                                                                  |
| llmlingua        | Required for --compress features                                                                  |
| yappi            | Required for performance profiling                                                                |
| tiktoken         | OpenAI's official tokenizer for accurate token counting (default for --tokenizer-method)           |
| transformers     | Hugging Face tokenizers for model-specific tokenization (optional for --tokenizer-method hf)       |
| strip-tags     | Filter out HTML tags for --webpage mode       |
| pypdf        | PDF extraction                                |
| py-zerox      | AI-driven PDF parsing that handles mixed content (text, images, tables, and graphs) via the `--pdf` flag |
| pdf2image    | Converts PDF pages to images for visual extraction and Markdown embedding using the `--pdf2img` flag |
| cachetools       | Efficient caching for request results                                                            |
| playwright       | Browser automation for JavaScript rendering (optional for --js-render)                            |

Install all dependencies with:

```bash
pip install requests openai aiohttp beautifulsoup4 trafilatura htmlmin2 orjson json lmlingua yappi pillow tiktoken transformers strip-tags pypdf
```

## Usage

Run the script with command-line arguments to customize behavior. For full help:

```bash
python or-cli.py -h
usage: or-cli.py [-h] [--rag | --cfrag] [--cfrag-search-only] [--rewrite-query | --no-rewrite-query] [--max-results MAX_RESULTS] [--score-threshold SCORE_THRESHOLD] [-p PROMPT] [-m MESSAGE] [-c]
                 [-i IMAGE] [--model MODEL] [--ollama] [--vllm] [--ollama-max-tokens OLLAMA_MAX_TOKENS] [-t] [-d] [--api-key API_KEY] [--temperature TEMPERATURE] [--seed SEED] [--top-p TOP_P]
                 [--max-tokens MAX_TOKENS] [--response-format RESPONSE_FORMAT] [--structured-outputs] [--include-reasoning] [--limits] [--eval] [--eval-thinking] [--multi] [--xenforo-debug]
                 [--webpage WEBPAGE] [--webpage-feed-format {html,markdown,json,xml,csv}] [--strip-tags] [--condense [CONDENSE]] [--compress]
                 [--compress-device-map {cuda,cpu,mps,balanced,balanced_low_0,auto}] [--compress-long] [--compress-long-question COMPRESS_LONG_QUESTION] [--compress-extended]
                 [--compress-batch-size COMPRESS_BATCH_SIZE] [--compress-force-token COMPRESS_FORCE_TOKEN] [--compress-target-tokens COMPRESS_TARGET_TOKENS]
                 [--compress-dynamic-compression COMPRESS_DYNAMIC_COMPRESSION] [--compress-drop-consecutive COMPRESS_DROP_CONSECUTIVE] [--compress-keep-newlines]
                 [--compress-keep-sentence-count COMPRESS_KEEP_SENTENCE_COUNT] [--compress-token-ratio COMPRESS_TOKEN_RATIO] [--compress-concate-question COMPRESS_CONCATE_QUESTION]
                 [--compress-context-compress-rate COMPRESS_CONTEXT_COMPRESS_RATE] [--compress-context-target-token COMPRESS_CONTEXT_TARGET_TOKEN]
                 [--compress-reorder-context COMPRESS_REORDER_CONTEXT] [--compress-rate COMPRESS_RATE] [--compress-save] [--compress-save-path COMPRESS_SAVE_PATH] [--follow-up FOLLOW_UP] [-q]
                 [--yappi] [--yappi-path YAPPI_PATH] [--yappi-export-format {callgrind,snakeviz,gprof2dot}] [--chunk-method {fixed,paragraph,sentence,overlap}]
                 [--chunk-mode {independent,sequential}] [--chunk-size CHUNK_SIZE] [--overlap-size OVERLAP_SIZE] [--tokenizer-method {tiktoken,hf}] [--stream] [--schema SCHEMA]
                 [--structured-schema STRUCTURED_SCHEMA] [--template TEMPLATE] [--template-vars TEMPLATE_VARS] [--structured-eval] [--structured-follow-up] [--pdf] [--pdf2img] [--skip-cache]
                 [--list-models] [--list-models-filter LIST_MODELS_FILTER] [--list-models-filter-id LIST_MODELS_FILTER_ID] [--js-render] [--auth-username AUTH_USERNAME]
                 [--auth-password AUTH_PASSWORD] [--auth-cookies AUTH_COOKIES] [--auth-headers AUTH_HEADERS] [--rag-results RAG_RESULTS] [--rag-summarize] [--rag-url RAG_URL] [--rag-key RAG_KEY]
                 [--rag-format {default,markdown,compact}] [--search] [--search-results-purge] [--search-api SEARCH_API] [--multi-search MULTI_SEARCH]
                 [--max-concurrent-search MAX_CONCURRENT_SEARCH] [--private] [--opik-local] [--opik-force-local]

CLI for OpenRouter, Ollama, or vLLM with advanced features and RAG support. Use --rag to enable retrieval augmented generation with txtai.

options:
  -h, --help            show this help message and exit
  --rag                 Enable RAG mode using txtai API
  --cfrag               Use Cloudflare AutoRAG for retrieval and generation via aiSearch endpoint.
  --cfrag-search-only   Use Cloudflare AutoRAG /search endpoint to retrieve context only, then use OpenRouter for generation.
  --rewrite-query, --no-rewrite-query
                        Enable or disable query rewriting for AutoRAG
  --max-results MAX_RESULTS
                        Maximum number of results to retrieve from AutoRAG
  --score-threshold SCORE_THRESHOLD
                        Minimum similarity score threshold for AutoRAG results
  -p, --prompt PROMPT   System prompt/instructions.
  -m, --message MESSAGE
                        User message. If not provided, reads from stdin.
  -c, --code            Escape code in message.
  -i, --image IMAGE     Path to image file.
  --model MODEL         LLM model to use (default: google/gemini-2.0-flash-exp:free). When used with --eval, pass two or three comma-separated models.
  --ollama              Use local Ollama endpoint and default model.
  --vllm                Use local vLLM endpoint.
  --ollama-max-tokens OLLAMA_MAX_TOKENS
                        Override the maximum prompt token context size (default: 8000)
  -t, --tokens          Show token usage.
  -d, --debug           Enable debug logging.
  --api-key API_KEY     API key override.
  --temperature TEMPERATURE
                        Sampling temperature (default: 0.3 for determinism)
  --seed SEED           Fixed seed for deterministic output (optional)
  --top-p TOP_P         Top-p sampling.
  --max-tokens MAX_TOKENS
                        Max tokens to generate.
  --response-format RESPONSE_FORMAT
                        Response format (e.g., 'json').
  --structured-outputs  Enable structured outputs.
  --include-reasoning   Include reasoning tokens.
  --limits              Show API key limits.
  --eval                Evaluate response with additional models.
  --eval-thinking       Evaluate response with additional models using thorough reasoning prompts.
  --multi               Multi-model response mode.
  --xenforo-debug       Enable detailed XenForo structure debugging
  --webpage WEBPAGE     URL to process into Markdown.
  --webpage-feed-format {html,markdown,json,xml,csv}
                        Feed format for webpage processing: 'html' returns raw HTML; 'markdown' returns converted Markdown (default).
  --strip-tags          Remove all HTML tags from the fetched webpage content. Used with --webpage
  --condense [CONDENSE]
                        Condense level for webpage fetching.
  --compress            Compress prompt with LLMLingua.
  --compress-device-map {cuda,cpu,mps,balanced,balanced_low_0,auto}
                        The computing environment for compression. Options: cuda, cpu, mps, balanced, balanced_low_0, auto. Default is cpu.
  --compress-long       Use LongLLMLingua for coarse compression.
  --compress-long-question COMPRESS_LONG_QUESTION
                        Override default question for coarse compression (e.g. 'Summary this text').
  --compress-extended   If set with --compress, save extended compression parameters to files.
  --compress-batch-size COMPRESS_BATCH_SIZE
                        Set maximum batch size for prompt compression (default: 400)
  --compress-force-token COMPRESS_FORCE_TOKEN
                        Set maximum force token for prompt compression (default: 10000)
  --compress-target-tokens COMPRESS_TARGET_TOKENS
                        Target token count for compression (--target_token, default: -1)
  --compress-dynamic-compression COMPRESS_DYNAMIC_COMPRESSION
                        Dynamic context compression ratio (--dynamic_context_compression_ratio, default: 0.4)
  --compress-drop-consecutive COMPRESS_DROP_CONSECUTIVE
                        Drop consecutive tokens (--drop_consecutive, default: True)
  --compress-keep-newlines
                        Retain newline splits in the compressed prompt (--keep_split, default: False)
  --compress-keep-sentence-count COMPRESS_KEEP_SENTENCE_COUNT
                        Number of sentences to retain (--keep_sentence_number, default: 0)
  --compress-token-ratio COMPRESS_TOKEN_RATIO
                        Token budget ratio for compression (--token_budget_ratio, default: 1.4)
  --compress-concate-question COMPRESS_CONCATE_QUESTION
                        Include the question in the compressed prompt (--concate_question, default: True)
  --compress-context-compress-rate COMPRESS_CONTEXT_COMPRESS_RATE
                        Compression rate for context-level compression (--context_level_rate, default: 1.0)
  --compress-context-target-token COMPRESS_CONTEXT_TARGET_TOKEN
                        Target token count for context-level compression (--context_level_target_token, default: -1)
  --compress-reorder-context COMPRESS_REORDER_CONTEXT
                        Method for reordering context (--reorder_context, default: 'sort')
  --compress-rate COMPRESS_RATE
                        Compression rate for LLMLingua-2 (default: 0.4)
  --compress-save       If set with --compress, save compressed prompt to file and exit
  --compress-save-path COMPRESS_SAVE_PATH
                        File path to save compressed prompt when --compress-save is used
  --follow-up FOLLOW_UP
                        Follow-up messages to send to the assistant
  -q, --quiet           Hide header output (quiet mode)
  --yappi               Enable yappi profiling for performance analysis
  --yappi-path YAPPI_PATH
                        Optional file path to save yappi profiling results
  --yappi-export-format {callgrind,snakeviz,gprof2dot}
                        Optional export format for yappi profiling data.
  --chunk-method {fixed,paragraph,sentence,overlap}
                        Select the local chunking method: fixed, paragraph, sentence, or overlap.
  --chunk-mode {independent,sequential}
                        Processing mode for chunking: 'independent' sends each chunk as a separate API call; 'sequential' processes chunks with overlapping context.
  --chunk-size CHUNK_SIZE
                        Maximum chunk size (in tokens) for chunking methods. Defaults to 8000 tokens.
  --overlap-size OVERLAP_SIZE
                        Overlap size (in characters/tokens) for overlapping chunking.
  --tokenizer-method {tiktoken,hf}
                        Select the tokenizer to use: 'tiktoken' for OpenAI/OpenRouter models (default) or 'hf' for Hugging Face tokenizers.
  --stream              Enable streaming mode.
  --schema SCHEMA       Inline schema definition in the format 'field1,field2 type,field3'. Example: --schema 'name,age int,short_bio'. If provided, the script will automatically generate a JSON
                        schema from the given fields.
  --structured-schema STRUCTURED_SCHEMA
                        Path to a JSON schema file for structured output. Supported by OpenAI, Google, Meta, Deepseek models.
  --template TEMPLATE   Name of the prompt template file (YAML or JSON) to load from the templates folder.
  --template-vars TEMPLATE_VARS
                        JSON string of variables for template substitution, e.g. '{"name": "User"}'.
  --structured-eval     Enforce structured output format for evaluation responses (requires --eval and --schema/--structured-schema)
  --structured-follow-up
                        Enforce structured output format for follow-up responses (requires --follow-up and --schema/--structured-schema)
  --pdf                 Use py‑zerox for enhanced PDF extraction
  --pdf2img             Use pdf2image to convert PDF pages to images and embed them in Markdown
  --skip-cache          Bypass the Cloudflare cache
  --list-models         List available OpenRouter.ai models info
  --list-models-filter LIST_MODELS_FILTER
                        Filter models by a substring in the model name
  --list-models-filter-id LIST_MODELS_FILTER_ID
                        Filter models by a substring in the model ID
  --js-render           Use Playwright to render JavaScript for webpage processing
  --auth-username AUTH_USERNAME
                        Username for authenticated web sessions
  --auth-password AUTH_PASSWORD
                        Password for authenticated web sessions
  --auth-cookies AUTH_COOKIES
                        JSON file containing cookies for authenticated web sessions
  --auth-headers AUTH_HEADERS
                        JSON file containing headers for authenticated web sessions
  --rag-results RAG_RESULTS
                        Number of results to fetch from txtai (default: 10)
  --rag-summarize       Summarize txtai results (default: False)
  --rag-url RAG_URL     txtai API URL
  --rag-key RAG_KEY     txtai API key
  --rag-format {default,markdown,compact}
                        Format for the retrieved context
  --search              Perform web search using Linkup API and save results in markdown format for RAG
  --search-results-purge
                        Purge txtai indexed documents related to web searches and reload txtai
  --search-api SEARCH_API
                        Select which search API to use: linkup, brave, or comma-separated list (e.g., linkup,brave)
  --multi-search MULTI_SEARCH
                        Comma-separated list of search queries to run in parallel
  --max-concurrent-search MAX_CONCURRENT_SEARCH
                        Maximum number of concurrent searches
  --private             Disable Opik tracing for privacy
  --opik-local          Use local Docker Compose Opik instance instead of cloud
  --opik-force-local    Force using local Opik without connectivity checks
```

### Command-Line Arguments

| Flag | Description | Optional/Required | Default Value |
|------|-------------|-------------------|---------------|
| `-p`, `--prompt` | System prompt/instructions for the AI | Required* | N/A |
| `-m`, `--message` | User message to send | Optional | Reads from stdin |
| `-c`, `--code` | Indicates message contains code (applies escaping) | Optional | False |
| `-i`, `--image` | Path or URL to an image file to include with `-m` prompt. Use with an image-input supporting model (e.g. `google/gemini-2.0-flash-001`) | Optional | N/A |
| `--model` | AI model(s) to use; comma-separated for `--eval` or `--multi` | Optional | google/gemini-2.0-flash-lite-preview-02-05:free |
| `--ollama` | Use local Ollama API instead of OpenRouter | Optional | False |
| `--ollama-max-tokens` | Maximum prompt token context for Ollama | Optional | 8000 |
| `-t`, `--tokens` | Display token usage and cost information | Optional | False |
| `-d`, `--debug` | Enable detailed debug logging | Optional | False |
| `--api-key` | Override API key | Optional | From environment variable |
| `--temperature` | Sampling temperature (higher = more creative) | Optional | 0.3 |
| `--seed` | Fixed seed for deterministic output | Optional | None |
| `--top-p` | Nucleus sampling value | Optional | 1.0 |
| `--max-tokens` | Maximum tokens to generate (≥1) | Optional | None |
| `--top-k` | Top-k sampling (0=disabled) | Optional | 0 |
| `--min-p` | Min-p sampling threshold [0-1] | Optional | 0.0 |
| `--top-a` | Top-a dynamic sampling [0-1] | Optional | 0.0 |
| `--repetition-penalty` | Repetition penalty [0-2] | Optional | 1.0 |
| `--frequency-penalty` | Frequency penalty [-2,2] | Optional | 0.0 |
| `--presence-penalty` | Presence penalty [-2,2] | Optional | 0.0 |
| `--response-format` | JSON format specification | Optional | None |
| `--structured-outputs` | Enable structured outputs if model supports it | Optional | False |
| `--tools` | Path to JSON file with OpenAI-compatible tool definitions | Optional | N/A |
| `--tool-choice` | Tool invocation mode: auto (model decides), required (force), none (disable) | Optional | auto |
| `--parallel-tool-calls` | Allow model to make multiple tool calls in parallel | Optional | True |
| `--no-parallel-tool-calls` | Force sequential tool execution | Optional | - |
| `--routing` | OpenRouter provider routing: nitro (fastest), floor (cheapest), free | Optional | N/A |
| `--online` | Enable OpenRouter web search via :online model suffix (Exa.ai) | Optional | False |
| `--online-results` | Max web search results when using --online | Optional | 5 |
| `--include-reasoning` | Include reasoning tokens in response | Optional | False |
| `--limits` | Check API key rate limits and usage | Optional | False |
| `--eval` | Evaluate first model's response with second/third model | Optional | False |
| `--eval-thinking` | Evaluate response with additional models using thorough reasoning prompts | Optional | False |
| `--multi` | Get responses from all specified models | Optional | False |
| `--xenforo-debug` | Enable detailed XenForo structure debugging | Optional | N/A |
| `--webpage` | URL to convert to Markdown for input | Optional | N/A |
| `--webpage-feed-format` | Format for processing the webpage content. Options: markdown, html, json, xml, csv. | Optional | markdown |
| `--strip-tags` | Remove all HTML tags from the fetched webpage content. Used with `--webpage` |
| `--condense` | Condense level (1-3) for Xenforo multi-page thread analysis | Optional | 1 (if specified) |
| `--compress` | Enable prompt compression with Microsoft LLMLingua | Optional | False |
| `--compress-device-map` | Controls method of compression {cuda, cpu, mps, balanced, balanced_low_0, auto} | Optional | cpu |
| `--compress-long` | Enable two-stage compression pipeline. When combined with `--compress`, the script first applies a coarse-level compression using LongLLMLingua (for very long contexts) followed by fine-grained token-level compression using LLMLingua‑2. | Optional | False |
| `--compress-long-question` | Custom prompt to guide coarse compression | Optional | "" |
| `--compress-extended` | Save detailed compression parameters to files | Optional | False |
| `--compress-batch-size` | Batch size for compression | Optional | 400 |
| `--compress-force-token` | Force token value for compression (passed to `force_context_number`) | Optional | 10000 |
| `--compress-rate` | Compression rate (0.0–1.0) for LLMLingua‑2 | Optional | 0.4 |
| `--compress-target-tokens` | Sets the target token count for the compressed prompt. A value of `-1` means unused. | Optional | -1 |
| `--compress-dynamic-compression` | Specifies the dynamic context compression ratio. Lower values result in more aggressive compression. | Optional | 0.4 |
| `--compress-drop-consecutive` | If true, consecutive tokens in the force token list are dropped to reduce redundancy. | Optional | True |
| `--compress-keep-newlines` | Retains newline characters in the compressed prompt, preserving original formatting. | Optional | False |
| `--compress-keep-sentence-count` | Number of sentences to retain in each context during compression | Optional | 0 |
| `--compress-token-ratio` | Defines the token budget ratio for compression | Optional | 1.4 |
| `--compress-concate-question` | If enabled, includes the original question in the compressed prompt | Optional | True |
| `--compress-context-compress-rate` | Sets the compression rate for context-level compression | Optional | 1.0 |
| `--compress-context-target-token` | Specifies the target token count for context-level compression | Optional | -1 |
| `--compress-reorder-context` | Determines the method for reordering context before compression (e.g., `"sort"`) | Optional | "sort" |
| `--follow-up` | Add follow-up message(s) | Optional | [] |
| `--compress-save` | Save compressed prompt to file and exit | Optional | False |
| `--compress-save-path` | File path for saved compressed prompt | Optional | ./compress-text.txt |
| `-q`, `--quiet` | Hide header output (quiet mode) | Optional | False |
| `--yappi` | Enable yappi profiling | Optional | False |
| `--yappi-path` | Path for profiling results | Optional | N/A |
| `--yappi-export-format` | Format for profiling data export | Optional | N/A |
| `--tokenizer-method`   | Selects the tokenizer to use for measuring token counts. Options: `"tiktoken"` (default) for OpenAI/OpenRouter models, or `"hf"` for Hugging Face tokenizers.                                                                      | Optional          | tiktoken       |
| `--chunk-method`       | Specifies the method for splitting input text into chunks. Options: `"fixed"`, `"paragraph"`, `"sentence"`, or `"overlap"`.                                                                                                                | Optional          | N/A            |
| `--chunk-mode`         | Defines how chunks are processed. `"independent"` sends each chunk as a separate API call, while `"sequential"` processes chunks in order, carrying forward context. For code inputs (as detected via lexer), sequential mode is forced. | Optional          | N/A            |
| `--chunk-size`         | Sets the maximum chunk token size..                                                                                           | Optional          | 8000          |
| `--overlap-size`       | (Used with `"overlap"` chunking) Specifies the number of characters/tokens that overlap between consecutive chunks to preserve context.                                                                                                   | Optional          | 200            |
| `--stream` | Enabling streaming chat mode | Optional | N/A |
| `--schema` | Inline schema definition in the format `'field1,field2 type,field3'` (e.g., `'name,age int,short_bio'`). Automatically generates a JSON schema for structured output. | Optional | N/A |
| `--structured-schema` | Path to a JSON schema file for structured output. Supported by models such as OpenAI, Google, Meta, and Deepseek. | Optional | N/A |
| `--template`              | Name of the prompt template file (YAML or JSON) to load from the templates folder             | Optional          | N/A           |
| `--template-vars`         | JSON string of variables for template substitution (e.g. `{"name": "User"}`)                  | Optional          | N/A           |
| `--structured-eval`          | Enforce structured output format for evaluation responses (requires --eval and schema flag)    | Optional                                       | False         |
| `--structured-follow-up`     | Enforce structured output format for follow-up responses (requires --follow-up and schema flag)  | Optional                                       | False         |
| `--pdf` | Use py‑zerox for enhanced PDF extraction | Optional | False |
| `--pdf2img` | Use pdf2image to convert PDF pages to images and embed them in Markdown | Optional | False |
| `--skip-cache` | Bypass the Cloudflare cache | Optional | False |
| `--list-models` | List available OpenRouter.ai models info | Optional | False |
| `--list-models-filter` | Filter models by a substring in the model name | Optional | False |
| `--list-models-filter-id` | Filter models by a substring in the model ID | Optional | False |
| `--js-render` | Use Playwright to render JavaScript for webpage processing | Optional | False |
| `--auth-username` | Username for authenticated web sessions | Optional | N/A |
| `--auth-password` | Password for authenticated web sessions | Optional | N/A |
| `--auth-cookies` | JSON file containing cookies for authenticated web sessions | Optional | N/A |
| `--auth-headers` | JSON file containing headers for authenticated web sessions | Optional | N/A |
| `--rag` | Enable RAG mode using txtai API | Optional | False |
| `--rag-results` | Number of results to fetch from txtai | Optional | 100 |
| `--rag-summarize` | Summarize txtai results | Optional | False |
| `--rag-url` | txtai API URL | Optional | <http://localhost:7234> |
| `--rag-key` | txtai API key | Optional | xzy |
| `--rag-format` | Format for retrieved context | Optional | default |
| `--search` | Perform web search using Linkup API and save results in markdown format for RAG | Optional | N/A |
| `--search-results-purge` | Purge txtai indexed documents related to web searches and reload txtai | Optional | N/A |
| `--search-api` | Select which search API to use with --search: linkup (default) or brave | Optional | N/A |
| `--multi-search` | Comma-separated list of search queries to run in parallel | Optional | N/A |
| `--max-concurrent-search` | Maximum number of concurrent searches | Optional | N/A |
| `--private`             | Disable Opik tracing for privacy        | Optional | N/A |
| `--opik-local`          | Use local Docker Compose Opik instance instead of cloud        | Optional | N/A |
| `--opik-force-local`    | Force using local Opik without connectivity checks        | Optional | N/A |
| `--cfrag` | Enable Cloudflare AutoRAG mode | Optional | N/A |
| `--cfrag-search-only` | When combined with `--cfrag`, will bypass Cloudflare AutoRAG LLM model for OpenRouter LLM models | Optional | N/A |
| `--rewrite-query` / `--no-rewrite-query` | Enable or disable query rewriting (default: disabled) | Optional | N/A |
| `--max-results N` | Max number of retrieved chunks (top-K) | Optional | N/A |
| `--score-threshold 0.N` | Minimum similarity score (0-1) | Optional | N/A |
| `--stream` | Enable streaming response | Optional | N/A |

\* Required unless `--limits` is specified

**Notes:**

- **Webpage Condense Levels**:
  - Level 1: First 1/3 + last 1/3 of pages
  - Level 2: First 2/5 + last 1/5 of pages
  - Level 3: First 1/5 + last 1/5 of pages

## List Models

To list all OpenRouter AI API supported LLM models with `--list-models` flag:

```bash
python or-cli.py --list-models
```

To filter the OpenRouter AI API supported LLM models with `--list-models` and `--list-models-filter` flag by model `name`:

<details>
  <summary>python or-cli.py --list-models --list-models-filter "gemini pro 1.5"</summary>

```json
[
  {
    "id": "google/gemini-pro-1.5",
    "name": "Google: Gemini Pro 1.5",
    "created": 1712620800,
    "description": "Google's latest multimodal model, supports image and video[0] in text or chat prompts.\n\nOptimized for language tasks including:\n\n- Code generation\n- Text generation\n- Text editing\n- Problem solving\n- Recommendations\n- Information extraction\n- Data extraction or generation\n- AI agents\n\nUsage of Gemini is subject to Google's [Gemini Terms of Use](https://ai.google.dev/terms).\n\n* [0]: Video input is not available through OpenRouter at this time.",
    "context_length": 2000000,
    "architecture": {
      "modality": "text+image->text",
      "tokenizer": "Gemini",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0.00000125",
      "completion": "0.000005",
      "image": "0.0006575",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 2000000,
      "max_completion_tokens": 8192,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "tools",
      "tool_choice",
      "seed",
      "response_format",
      "structured_outputs"
    ]
  }
]
```

</details>

<details>
  <summary>python or-cli.py --list-models --list-models-filter "gemini 2"</summary>

```json
[
  {
    "id": "google/gemini-2.0-flash-lite-001",
    "name": "Google: Gemini 2.0 Flash Lite",
    "created": 1740506212,
    "description": "Gemini 2.0 Flash Lite offers a significantly faster time to first token (TTFT) compared to [Gemini Flash 1.5](/google/gemini-flash-1.5), while maintaining quality on par with larger models like [Gemini Pro 1.5](/google/gemini-pro-1.5), all at extremely economical token prices.",
    "context_length": 1048576,
    "architecture": {
      "modality": "text+image->text",
      "tokenizer": "Gemini",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0.000000075",
      "completion": "0.0000003",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 1048576,
      "max_completion_tokens": 8192,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "tools",
      "tool_choice",
      "max_tokens",
      "temperature",
      "top_p",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "response_format",
      "structured_outputs"
    ]
  },
  {
    "id": "google/gemini-2.0-flash-thinking-exp:free",
    "name": "Google: Gemini 2.0 Flash Thinking Experimental 01-21 (free)",
    "created": 1737547899,
    "description": "Gemini 2.0 Flash Thinking Experimental (01-21) is a snapshot of Gemini 2.0 Flash Thinking Experimental.\n\nGemini 2.0 Flash Thinking Mode is an experimental model that's trained to generate the \"thinking process\" the model goes through as part of its response. As a result, Thinking Mode is capable of stronger reasoning capabilities in its responses than the [base Gemini 2.0 Flash model](/google/gemini-2.0-flash-exp).",
    "context_length": 1048576,
    "architecture": {
      "modality": "text+image->text",
      "tokenizer": "Gemini",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 1048576,
      "max_completion_tokens": 65536,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop"
    ]
  },
  {
    "id": "google/gemini-2.0-flash-thinking-exp-1219:free",
    "name": "Google: Gemini 2.0 Flash Thinking Experimental (free)",
    "created": 1734650026,
    "description": "Gemini 2.0 Flash Thinking Mode is an experimental model that's trained to generate the \"thinking process\" the model goes through as part of its response. As a result, Thinking Mode is capable of stronger reasoning capabilities in its responses than the [base Gemini 2.0 Flash model](/google/gemini-2.0-flash-exp).",
    "context_length": 40000,
    "architecture": {
      "modality": "text+image->text",
      "tokenizer": "Gemini",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 40000,
      "max_completion_tokens": 8000,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop"
    ]
  }
]
```

</details>

<details>
  <summary>python or-cli.py --list-models --list-models-filter "deepseek"</summary>

```json
[
  {
    "id": "deepseek/deepseek-r1-zero:free",
    "name": "DeepSeek: DeepSeek R1 Zero (free)",
    "created": 1741297434,
    "description": "DeepSeek-R1-Zero is a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step. It's 671B parameters in size, with 37B active in an inference pass.\n\nIt demonstrates remarkable performance on reasoning. With RL, DeepSeek-R1-Zero naturally emerged with numerous powerful and interesting reasoning behaviors.\n\nDeepSeek-R1-Zero encounters challenges such as endless repetition, poor readability, and language mixing. See [DeepSeek R1](/deepseek/deepseek-r1) for the SFT model.\n\n",
    "context_length": 163840,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Other",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 163840,
      "max_completion_tokens": null,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logprobs",
      "logit_bias",
      "top_logprobs"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-llama-8b",
    "name": "DeepSeek: R1 Distill Llama 8B",
    "created": 1738937718,
    "description": "DeepSeek R1 Distill Llama 8B is a distilled large language model based on [Llama-3.1-8B-Instruct](/meta-llama/llama-3.1-8b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:\n\n- AIME 2024 pass@1: 50.4\n- MATH-500 pass@1: 89.1\n- CodeForces Rating: 1205\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.\n\nHugging Face: \n- [Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) \n- [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B)   |",
    "context_length": 32000,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Llama3",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0.00000004",
      "completion": "0.00000004",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 32000,
      "max_completion_tokens": 32000,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logit_bias"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-qwen-1.5b",
    "name": "DeepSeek: R1 Distill Qwen 1.5B",
    "created": 1738328067,
    "description": "DeepSeek R1 Distill Qwen 1.5B is a distilled large language model based on  [Qwen 2.5 Math 1.5B](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It's a very small and efficient model which outperforms [GPT 4o 0513](/openai/gpt-4o-2024-05-13) on Math Benchmarks.\n\nOther benchmark results include:\n\n- AIME 2024 pass@1: 28.9\n- AIME 2024 cons@64: 52.7\n- MATH-500 pass@1: 83.9\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.",
    "context_length": 131072,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Other",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0.00000018",
      "completion": "0.00000018",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 131072,
      "max_completion_tokens": 32768,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "top_k",
      "repetition_penalty",
      "logit_bias",
      "min_p",
      "response_format"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-qwen-32b:free",
    "name": "DeepSeek: R1 Distill Qwen 32B (free)",
    "created": 1738194830,
    "description": "DeepSeek R1 Distill Qwen 32B is a distilled large language model based on [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.\n\nOther benchmark results include:\n\n- AIME 2024 pass@1: 72.6\n- MATH-500 pass@1: 94.3\n- CodeForces Rating: 1691\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.",
    "context_length": 16000,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Qwen",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 16000,
      "max_completion_tokens": 16000,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-qwen-32b",
    "name": "DeepSeek: R1 Distill Qwen 32B",
    "created": 1738194830,
    "description": "DeepSeek R1 Distill Qwen 32B is a distilled large language model based on [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.\n\nOther benchmark results include:\n\n- AIME 2024 pass@1: 72.6\n- MATH-500 pass@1: 94.3\n- CodeForces Rating: 1691\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.",
    "context_length": 131072,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Qwen",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0.00000012",
      "completion": "0.00000018",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 131072,
      "max_completion_tokens": 8192,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "repetition_penalty",
      "response_format",
      "top_k",
      "seed",
      "min_p"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-qwen-14b",
    "name": "DeepSeek: R1 Distill Qwen 14B",
    "created": 1738193940,
    "description": "DeepSeek R1 Distill Qwen 14B is a distilled large language model based on [Qwen 2.5 14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models.\n\nOther benchmark results include:\n\n- AIME 2024 pass@1: 69.7\n- MATH-500 pass@1: 93.9\n- CodeForces Rating: 1481\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.",
    "context_length": 64000,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Qwen",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0.00000015",
      "completion": "0.00000015",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 64000,
      "max_completion_tokens": 64000,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logit_bias"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-llama-70b:free",
    "name": "DeepSeek: R1 Distill Llama 70B (free)",
    "created": 1737663169,
    "description": "DeepSeek R1 Distill Llama 70B is a distilled large language model based on [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:\n\n- AIME 2024 pass@1: 70.0\n- MATH-500 pass@1: 94.5\n- CodeForces Rating: 1633\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.",
    "context_length": 128000,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Llama3",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 128000,
      "max_completion_tokens": null,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logprobs",
      "logit_bias",
      "top_logprobs"
    ]
  },
  {
    "id": "deepseek/deepseek-r1-distill-llama-70b",
    "name": "DeepSeek: R1 Distill Llama 70B",
    "created": 1737663169,
    "description": "DeepSeek R1 Distill Llama 70B is a distilled large language model based on [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:\n\n- AIME 2024 pass@1: 70.0\n- MATH-500 pass@1: 94.5\n- CodeForces Rating: 1633\n\nThe model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models.",
    "context_length": 131072,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Llama3",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0.00000023",
      "completion": "0.00000069",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 131072,
      "max_completion_tokens": 8192,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "repetition_penalty",
      "response_format",
      "top_k",
      "seed",
      "min_p"
    ]
  },
  {
    "id": "deepseek/deepseek-r1:free",
    "name": "DeepSeek: R1 (free)",
    "created": 1737381095,
    "description": "DeepSeek R1 is here: Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass.\n\nFully open-source model & [technical report](https://api-docs.deepseek.com/news/news250120).\n\nMIT licensed: Distill & commercialize freely!",
    "context_length": 163840,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "DeepSeek",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 163840,
      "max_completion_tokens": null,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "reasoning",
      "include_reasoning",
      "temperature"
    ]
  },
  {
    "id": "deepseek/deepseek-r1",
    "name": "DeepSeek: R1",
    "created": 1737381095,
    "description": "DeepSeek R1 is here: Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass.\n\nFully open-source model & [technical report](https://api-docs.deepseek.com/news/news250120).\n\nMIT licensed: Distill & commercialize freely!",
    "context_length": 64000,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "DeepSeek",
      "instruct_type": "deepseek-r1"
    },
    "pricing": {
      "prompt": "0.0000007",
      "completion": "0.0000025",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 64000,
      "max_completion_tokens": 16000,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "reasoning",
      "include_reasoning",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logit_bias"
    ]
  },
  {
    "id": "deepseek/deepseek-chat:free",
    "name": "DeepSeek: DeepSeek V3 (free)",
    "created": 1735241320,
    "description": "DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous versions. Pre-trained on nearly 15 trillion tokens, the reported evaluations reveal that the model outperforms other open-source models and rivals leading closed-source models.\n\nFor model details, please visit [the DeepSeek-V3 repo](https://github.com/deepseek-ai/DeepSeek-V3) for more information, or see the [launch announcement](https://api-docs.deepseek.com/news/news1226).",
    "context_length": 131072,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "DeepSeek",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 131072,
      "max_completion_tokens": null,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logprobs",
      "logit_bias",
      "top_logprobs"
    ]
  },
  {
    "id": "deepseek/deepseek-chat",
    "name": "DeepSeek: DeepSeek V3",
    "created": 1735241320,
    "description": "DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous versions. Pre-trained on nearly 15 trillion tokens, the reported evaluations reveal that the model outperforms other open-source models and rivals leading closed-source models.\n\nFor model details, please visit [the DeepSeek-V3 repo](https://github.com/deepseek-ai/DeepSeek-V3) for more information, or see the [launch announcement](https://api-docs.deepseek.com/news/news1226).",
    "context_length": 64000,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "DeepSeek",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0.0000004",
      "completion": "0.0000013",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 64000,
      "max_completion_tokens": 16000,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "top_k",
      "min_p",
      "repetition_penalty",
      "logit_bias"
    ]
  }
]
```

</details>

To filter the OpenRouter AI API supported LLM models with `--list-models` and `--list-models-filter-id` flag by model `id` i.e. `google/gemini-2.0-flash-thinking-exp:free`:

<details>
  <summary>python or-cli.py --list-models --list-models-filter-id "google/gemini-2.0-flash-thinking-exp:free"</summary>

```json
[
  {
    "id": "google/gemini-2.0-flash-thinking-exp:free",
    "name": "Google: Gemini 2.0 Flash Thinking Experimental 01-21 (free)",
    "created": 1737547899,
    "description": "Gemini 2.0 Flash Thinking Experimental (01-21) is a snapshot of Gemini 2.0 Flash Thinking Experimental.\n\nGemini 2.0 Flash Thinking Mode is an experimental model that's trained to generate the \"thinking process\" the model goes through as part of its response. As a result, Thinking Mode is capable of stronger reasoning capabilities in its responses than the [base Gemini 2.0 Flash model](/google/gemini-2.0-flash-exp).",
    "context_length": 1048576,
    "architecture": {
      "modality": "text+image->text",
      "tokenizer": "Gemini",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 1048576,
      "max_completion_tokens": 65536,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop"
    ]
  }
]
```

</details>

For `google/gemini-2.0-flash-lite-preview-02-05:free`:

<details>
  <summary>python or-cli.py --list-models --list-models-filter-id "google/gemini-2.0-flash-lite-preview-02-05:free"</summary>

```json
[
  {
    "id": "google/gemini-2.0-flash-lite-preview-02-05:free",
    "name": "Google: Gemini Flash Lite 2.0 Preview (free)",
    "created": 1738768262,
    "description": "Gemini Flash Lite 2.0 offers a significantly faster time to first token (TTFT) compared to [Gemini Flash 1.5](/google/gemini-flash-1.5), while maintaining quality on par with larger models like [Gemini Pro 1.5](/google/gemini-pro-1.5). Because it's currently in preview, it will be **heavily rate-limited** by Google. This model will move from free to paid pending a general rollout on February 24th, at $0.075 / $0.30 per million input / ouput tokens respectively.",
    "context_length": 1000000,
    "architecture": {
      "modality": "text+image->text",
      "tokenizer": "Gemini",
      "instruct_type": null
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 1000000,
      "max_completion_tokens": 8192,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "tools",
      "tool_choice",
      "max_tokens",
      "temperature",
      "top_p",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "response_format",
      "structured_outputs"
    ]
  }
]
```

</details>

For `google/gemma-3-27b-it:free`:

<details>
  <summary>python or-cli.py --list-models --list-models-filter-id "google/gemma-3-27b-it:free"</summary>

```json
[
  {
    "id": "google/gemma-3-27b-it:free",
    "name": "Google: Gemma 3 27B (free)",
    "created": 1741756359,
    "description": "Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 128k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs and function calling. Gemma 3 27B is Google's latest open source model, successor to [Gemma 2](google/gemma-2-27b-it)",
    "context_length": 131072,
    "architecture": {
      "modality": "text->text",
      "tokenizer": "Gemini",
      "instruct_type": "gemma"
    },
    "pricing": {
      "prompt": "0",
      "completion": "0",
      "image": "0",
      "request": "0",
      "input_cache_read": "0",
      "input_cache_write": "0",
      "web_search": "0",
      "internal_reasoning": "0"
    },
    "top_provider": {
      "context_length": 131072,
      "max_completion_tokens": 8192,
      "is_moderated": false
    },
    "per_request_limits": null,
    "supported_parameters": [
      "max_tokens",
      "temperature",
      "top_p",
      "stop",
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "response_format",
      "structured_outputs"
    ]
  }
]
```

</details>

## Example Usage

### RAG Integration

Tried integrating various RAG tools into `or-cli.py` - including Milvus, Weaviate and Ragflow. However, some of these used too much system resources even at idle i.e. memory consumption for Ragflow idled at ~18GB! I settled on using [txtai](https://neuml.github.io/txtai/) right now with ~2.2GB idle. Update: Cloudflare Developer Week 2025 released [Cloudflare AutoRAG](https://blog.cloudflare.com/introducing-autorag-on-cloudflare/).

#### Cloudflare AutoRAG

[Cloudflare AutoRAG](https://blog.cloudflare.com/introducing-autorag-on-cloudflare/) is a game-changing as it removes one of the pain points of local system resource usage.

The `--cfrag` flag in `or-cli.py` enables integration with **Cloudflare AutoRAG**, a fully managed Retrieval-Augmented Generation (RAG) service. It allows you to query your private knowledge base stored in Cloudflare R2, with optional query rewriting, similarity filtering, and streaming responses.

This complements the existing `--rag` mode (which uses local txtai) by providing a **cloud-based, scalable, and maintenance-free RAG pipeline**.

##### How Cloudflare AutoRAG Integration Works (Technical Summary)

- **Data Storage:** You upload documents (PDFs, Markdown, HTML, images, etc.) to a Cloudflare R2 bucket.
- **Indexing:** AutoRAG automatically converts, chunks, embeds, and indexes your data into a Vectorize vector database.
- **Querying:**
  - Your query is optionally rewritten by an LLM to improve retrieval.
  - The rewritten (or original) query is embedded and matched against the vector index.
  - Top relevant chunks are retrieved based on similarity score and count thresholds.
  - An LLM generates a final answer grounded in the retrieved context.
- **API:** The integration calls the Cloudflare REST API endpoint `/accounts/{ACCOUNT_ID}/autorag/rags/{AUTORAG_NAME}/ai-search` when only `--cfrag` flag is used but if `--cfrag --cfrag-search-only` flags are used together, `or-cli.py` uses a different `/accounts/{ACCOUNT_ID}/autorag/rags/{AUTORAG_NAME}/search` endpoint and bypasses [Cloudflare AutoRAG default LLM model's](https://developers.cloudflare.com/autorag/configuration/models/) response and just passes the AutoRAG search results to `or-cli.py` native LLM models via Openrouter AI - thus can use one of ethir 300+ LLM models to digest AutoRAG search results and then provide a response.
- **Streaming:** Supports server-sent event (SSE) streaming for incremental responses.
- **Security:** Uses API tokens stored in environment variables.

##### Cloudflare AutoRAG Environment Variables Required

Set these in your `.env` file or environment:

```env
CF_ACCOUNT_ID=your_cloudflare_account_id
CF_AUTORAG_NAME=your_autorag_instance_name
CF_AUTORAG_API_TOKEN=your_api_token_with_autorag_permissions

R2_ACCESS_KEY_ID=your_r2_access_key_id
R2_SECRET_ACCESS_KEY=your_r2_secret_access_key
R2_ENDPOINT_URL=https://<accountid>.r2.cloudflarestorage.com
R2_BUCKET_NAME='your_r2_bucket_name'
```

##### Cloudflare AutoRAG Key Options

| Option | Description | Example |
|---------|-------------|---------|
| `--cfrag` | Enable Cloudflare AutoRAG mode | `--cfrag` |
| `-m` or `--message` | User query message | `-m "Explain the architecture"` |
| `--rewrite-query` / `--no-rewrite-query` | Enable or disable query rewriting (default: disabled) | `--rewrite-query` |
| `--max-results N` | Max number of retrieved chunks (top-K) | `--max-results 5` |
| `--score-threshold 0.N` | Minimum similarity score (0-1) | `--score-threshold 0.5` |
| `--stream` | Enable streaming response | `--stream` |
| `-d` or `--debug` | Enable verbose debug output | `-d` |

##### Cloudflare AutoRAG Example

The `or-cli.py` integration is done via a Python module script `cf_autorag_api.py` which can also run standalone to feed documents to Cloudflare AutoRAG specified Cloudflare R2 S3 bucket and to query the Cloudflare AutoRAG - similar to `txtai` with `txtai_api.py` script.

Example of uploading Chain Of Draft whitepaper PDF file, `cod.pdf` to the Cloudflare AutoRAG specified Cloudflare R2 S3 bucket:

~~~bash
python cf_autorag_api.py --upload --local-path cod.pdf --bucket-name $R2_BUCKET_NAME --remote-path ai_docs/cod.pdf
~~~

~~~bash
python cf_autorag_api.py --upload --local-path cod.pdf --bucket-name $R2_BUCKET_NAME --remote-path ai_docs/cod.pdf
2025-04-07 23:37:50,330 - __main__ - INFO - Uploading cod.pdf to bucket '$R2_BUCKET_NAME' as 'ai_docs/cod.pdf'
2025-04-07 23:37:50,713 - __main__ - INFO - Upload successful.
Upload completed successfully.
~~~

Then to query the Cloudflare AutoRAG embedded vector database for `cod.pdf` information.

```bash
python cf_autorag_api.py "what is chain of draft" --rewrite-query --max-results 5 --score-threshold 0.5
```

~~~bash
python cf_autorag_api.py "what is chain of draft" --rewrite-query --max-results 5 --score-threshold 0.5
{
  "answer": "**Chain of Draft (CoD)** is a novel prompting strategy that aims to reduce verbosity in large language models (LLMs) by encouraging them to generate concise, dense-information outputs at each step, similar to how humans approach problem-solving [([see document](https://github.com/sileix/chain-of-draft))](https://github.com/sileix/chain-of-draft). \n\nThis approach is inspired by human cognitive processes, where individuals often jot down only the critical pieces of information that help them progress when solving complex tasks, such as mathematical problems, drafting essays, or coding. By emulating this behavior, LLMs can focus on advancing toward solutions without the overhead of verbose reasoning.\n\nThe key characteristics of Chain of Draft include:\n\n* Concise reasoning drafts\n* Reduced latency and computational costs\n* Comparable or superior accuracy to standard Chain-of-Thought (CoT) prompting strategies\n* Significant cost advantages due to reduced token usage\n\nAs demonstrated in the experiments conducted across various benchmarks, Chain of Draft maintains or even improves accuracy compared to standard Chain of Thought, while significantly reducing token usage and latency [([see document](https://github.com/sileix/chain-of-draft))](https://github.com/sileix/chain-of-draft).",
  "sources": []
}
~~~

Then doing the same querying the `or-cli.py` that calls :

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 5 --score-threshold 0.5
~~~

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 5 --score-threshold 0.5

--- AutoRAG Answer ---

**Chain of Draft (CoD)** is a novel prompting strategy that aims to reduce verbosity and latency in large language models (LLMs) by generating concise, dense-information outputs at each step, similar to how humans approach problem-solving [([Chain of Draft: Thinking Faster by Writing Less](https://github.com/sileix/chain-of-draft))](https://github.com/sileix/chain-of-draft).

It is inspired by human cognitive processes, where only critical pieces of information are captured, making LLMs more practical for real-world applications where efficiency is paramount ([document](ai_docs/cod.pdf)).

By using CoD, LLMs can achieve similar accuracy as Chain of Thought (CoT) while using significantly fewer tokens, reducing computational costs and latency ([Table 6](ai_docs/cod.pdf)).
~~~

##### Cloudflare AutoRAG Example --cfrag-search-only

If `--cfrag --cfrag-search-only` flags are used together, `or-cli.py` uses a different `/accounts/{ACCOUNT_ID}/autorag/rags/{AUTORAG_NAME}/search` endpoint and bypasses [Cloudflare AutoRAG default LLM model's](https://developers.cloudflare.com/autorag/configuration/models/) response and just passes the AutoRAG search results to `or-cli.py` native LLM models via Openrouter AI - thus can use one of ethir 300+ LLM models to digest AutoRAG search results and then provide a response.

Without `--cfrag-search-only` flag, AutoRAG will allow one of Cloudflare AutoRAG default LLM models (`@cf/meta/llama-3.3-70b-instruct-fp8-fast`, `@cf/meta/llama-3.1-8b-instruct-fast`, and `@cf/meta/llama-3.1-8b-instruct-fp8`) to provide the response.

When `--cfrag-search-only` flag is used, allow `or-cli-.py` to use OpenRouter AI LLM models, i.e. below example uses OpenRouter AI LLM model, Google Gemini 2.0 Flash `google/gemini-2.0-flash-exp:free`. Definitely a better quality response than the one Cloudflare AutoRAG LLM models provided above.

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t

----- Assistant Response (OpenRouter via CF RAG) -----
Based on the provided context, Chain of Draft (CoD) is a novel prompting strategy for Large Language Models (LLMs) designed to improve efficiency and reduce computational costs in reasoning tasks. Here's a breakdown of what it is:

*   **Inspired by Human Cognition:** CoD is inspired by how humans solve complex problems. Instead of verbose explanations, humans often jot down concise notes or drafts containing only the essential information needed to progress.
*   **Concise Intermediate Steps:** CoD encourages LLMs to generate minimalistic, dense-information outputs at each step of the reasoning process. This contrasts with Chain-of-Thought (CoT), which often involves lengthy and verbose reasoning steps.
*   **Efficiency and Reduced Latency:** By focusing on essential information and reducing verbosity, CoD aims to reduce latency (response time) and computational costs (token usage) without sacrificing accuracy.
*   **Improved Cost-Effectiveness:** CoD reduces the number of input tokens required for prompting and shortens the output token length, directly lowering computational costs.
*   **Comparable or Superior Accuracy:** The research suggests that CoD can achieve comparable or even superior accuracy compared to standard CoT prompting strategies.
*   **Adaptable to Various Reasoning Techniques:** CoD employs a per-step budget, allowing unlimited reasoning steps, which makes it more adaptable to various structured reasoning techniques.

----- Generation Stats -----
Model Used: google/gemini-2.0-flash-exp:free
Provider Name: Google AI Studio
Generation Time: 1522 ms
Model Name: Google: Gemini 2.0 Flash Experimental (free)
Context Length: 1048576
Max Completion Tokens: 8192
Is Moderated: False
Modality: text+image->text
Tokenizer: Gemini
Supported Parameters: tools, tool_choice, max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, response_format, structured_outputs
Prompt Tokens: 2719
Completion Tokens: 276
Total Tokens: 2995
Total Cost: $0.00000000
Usage: 0
Latency: 360 ms
Native Tokens Prompt: 2914
Native Tokens Completion: 280
Native Tokens Reasoning: 0
Native Tokens Total: 3194
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

Let's try using OpenRouter AI with Google Gemini 2.5 Pro `google/gemini-2.5-pro-exp-03-25:free` to compare responses:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model google/gemini-2.5-pro-exp-03-25:free

----- Assistant Response (OpenRouter via CF RAG) -----
Based on the provided context, **Chain of Draft (CoD)** is a novel prompting strategy for Large Language Models (LLMs) designed to solve complex reasoning tasks more efficiently than traditional methods like Chain of Thought (CoT).

Here's a breakdown of its key characteristics:

1.  **Inspiration:** It's inspired by how humans solve problems, often relying on concise drafts or shorthand notes to capture essential insights rather than writing out every detailed step (Sources 1, 2, 4, 5, 7).
2.  **Mechanism:** Instead of generating verbose, step-by-step reasoning like CoT, CoD encourages the LLM to produce minimalistic, concise, yet informative intermediate reasoning outputs or "drafts" at each step (Sources 2, 4, 5). It focuses on essential calculations or transformations needed to progress (Source 4).
3.  **Implementation:** It involves instructing the model to think step-by-step but to keep each thinking step minimal, for example, by suggesting a limit like "five words at most" per step (though this isn't strictly enforced) (Source 9).
4.  **Goal:** To reduce the verbosity, latency (response time), and computational cost (token usage) associated with LLM reasoning, without sacrificing accuracy (Sources 2, 3, 5, 7).
5.  **Comparison to CoT:** While CoT emphasizes detailed, step-by-step explanations, CoD prioritizes efficiency and minimalism. CoD aims to achieve similar or even better accuracy than CoT but with significantly fewer tokens used, leading to lower costs and faster responses (Sources 2, 3, 5).

----- Generation Stats -----
Model Used: google/gemini-2.5-pro-exp-03-25:free
Provider Name: Google AI Studio
Generation Time: 3581 ms
Model Name: Google: Gemini 2.5 Pro Experimental (free)
Context Length: 1000000
Max Completion Tokens: 65535
Is Moderated: False
Modality: text+image->text
Tokenizer: Gemini
Supported Parameters: tools, tool_choice, max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, response_format, structured_outputs
Prompt Tokens: 2699
Completion Tokens: 346
Total Tokens: 3045
Total Cost: $0.00000000
Usage: 0
Latency: 8268 ms
Native Tokens Prompt: 2913
Native Tokens Completion: 1164
Native Tokens Reasoning: 0
Native Tokens Total: 4077
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's Google Gemma 3 27b LLM model `google/gemma-3-27b-it:free`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model google/gemma-3-27b-it:free

----- Assistant Response (OpenRouter via CF RAG) -----
Based on the provided documents, **Chain of Draft (CoD)** is a novel prompting strategy for Large Language Models (LLMs) designed to reduce latency and computational cost while maintaining or even improving accuracy compared to standard Chain-of-Thought (CoT) prompting.

Here's a breakdown of what it is:

* **Concise Reasoning:** CoD encourages LLMs to generate *concise, dense-information outputs* at each step, rather than lengthy, verbose reasoning steps like traditional CoT. It focuses on essential information.
* **Human-Inspired:** It's inspired by how humans solve problems – by jotting down only the *critical pieces of information* needed to progress.
* **Efficiency:** By compacting reasoning steps, CoD reduces the number of tokens used (both input and output), leading to lower computational costs and faster response times (lower latency).
* **Accuracy:** Despite being more concise, CoD achieves comparable or superior accuracy to CoT.

----- Generation Stats -----
Model Used: google/gemma-3-27b-it:free
Provider Name: Google AI Studio
Generation Time: 34488 ms
Model Name: Google: Gemma 3 27B (free)
Context Length: 96000
Max Completion Tokens: 8192
Is Moderated: False
Modality: text+image->text
Tokenizer: Gemini
Supported Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, top_k, min_p, repetition_penalty, logprobs, logit_bias, top_logprobs
Prompt Tokens: 1040
Completion Tokens: 196
Total Tokens: 1236
Total Cost: $0.00000000
Usage: 0
Latency: 1519 ms
Native Tokens Prompt: 1112
Native Tokens Completion: 214
Native Tokens Reasoning: 0
Native Tokens Total: 1326
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's Nvidia Llama 3.3 Nemotron Super 49b LLM model `nvidia/llama-3.3-nemotron-super-49b-v1:free`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model nvidia/llama-3.3-nemotron-super-49b-v1:free

----- Assistant Response (OpenRouter via CF RAG) -----
Based on the provided context from multiple sources (all from the same document, `ai_docs/cod.pdf`, but different chunks), here is a concise answer to your question:

**What is Chain of Draft (CoD)?**

* **Definition**: Chain of Draft (CoD) is a novel prompting strategy for Large Language Models (LLMs).
* **Inspiration**: Inspired by how humans solve complex tasks, focusing on concise, essential information.
* **Key Characteristics**:
        + **Concise Intermediate Reasoning Outputs**: Encourages LLMs to generate minimalistic yet informative outputs at each step.
        + **Efficiency**: Prioritizes efficiency and minimalism, reducing verbosity.
* **Benefits** (compared to Chain of Thought, CoT):
        + **Similar or Improved Accuracy**
        + **Significantly Reduced Token Usage** (as low as 7.6% of CoT's tokens in some cases)
        + **Lower Latency**
        + **Reduced Computational Costs**
* **Purpose**: Makes LLMs more practical for real-world applications where efficiency is crucial, across various reasoning tasks (e.g., arithmetic, common sense, symbolic reasoning).

----- Generation Stats -----
Model Used: nvidia/llama-3.3-nemotron-super-49b-v1:free
Provider Name: Chutes
Generation Time: 5762 ms
Model Name: NVIDIA: Llama 3.3 Nemotron Super 49B v1 (free)
Context Length: 131072
Max Completion Tokens: None
Is Moderated: False
Modality: text->text
Tokenizer: Other
Supported Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, top_k, min_p, repetition_penalty, logprobs, logit_bias, top_logprobs
Prompt Tokens: 1335
Completion Tokens: 243
Total Tokens: 1578
Total Cost: $0.00000000
Usage: 0
Latency: 684 ms
Native Tokens Prompt: 1351
Native Tokens Completion: 242
Native Tokens Reasoning: 0
Native Tokens Total: 1593
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's Nvidia Llama 3.1 Nemotron Nano 8b LLM model `nvidia/llama-3.1-nemotron-nano-8b-v1:free`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model nvidia/llama-3.1-nemotron-nano-8b-v1:free

----- Assistant Response (OpenRouter via CF RAG) -----
Based on the provided context, Chain of Draft (CoD) is a novel prompting strategy for Large Language Models (LLMs) that aims to mimic human reasoning processes. Unlike traditional methods like Chain of Thought (CoT), which can produce verbose and computationally expensive outputs, CoD encourages LLMs to generate concise, dense-information outputs at each step. This approach prioritizes efficiency and minimalism, aligning more closely with how humans typically approach problem-solving by jotting down only essential intermediate results. CoD achieves similar accuracy as CoT while using significantly fewer tokens, reducing latency and computational costs without sacrificing accuracy. The paper introduces CoD as a way to make LLMs more practical for real-world applications where efficiency is paramount. The code and data for CoD are available at https://github.com/sileix/chain-of-draft.

----- Generation Stats -----
Model Used: nvidia/llama-3.1-nemotron-nano-8b-v1:free
Provider Name: Chutes
Generation Time: 1034 ms
Model Name: NVIDIA: Llama 3.1 Nemotron Nano 8B v1 (free)
Context Length: 131072
Max Completion Tokens: None
Is Moderated: False
Modality: text->text
Tokenizer: Other
Supported Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, top_k, min_p, repetition_penalty, logprobs, logit_bias, top_logprobs
Prompt Tokens: 2704
Completion Tokens: 170
Total Tokens: 2874
Total Cost: $0.00000000
Usage: 0
Latency: 1650 ms
Native Tokens Prompt: 2728
Native Tokens Completion: 172
Native Tokens Reasoning: 0
Native Tokens Total: 2900
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's ByteDance UI-TARS 72b LLM model `bytedance-research/ui-tars-72b:free`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model bytedance-research/ui-tars-72b:free

----- Assistant Response (OpenRouter via CF RAG) -----
Chain of Draft (CoD) is a novel prompting strategy that substantially reduces the latency required for reasoning while achieving comparable or even superior accuracy compared to standard Chain-of-Thought prompting strategies. It leverages concise reasoning drafts to speed up response generation without sacrificing correctness. Additionally, CoD offers significant cost advantages by compacting the reasoning steps, reducing the number of input tokens required for few-shot prompting and shortening the output token length, directly lowering computational cost.

----- Generation Stats -----
Model Used: bytedance-research/ui-tars-72b:free
Provider Name: Chutes
Generation Time: 6894 ms
Model Name: Bytedance: UI-TARS 72B  (free)
Context Length: 32768
Max Completion Tokens: None
Is Moderated: False
Modality: text+image->text
Tokenizer: Other
Supported Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, top_k, min_p, repetition_penalty, logprobs, logit_bias, top_logprobs
Prompt Tokens: 2432
Completion Tokens: 90
Total Tokens: 2522
Total Cost: $0.00000000
Usage: 0
Latency: 3297 ms
Native Tokens Prompt: 2608
Native Tokens Completion: 92
Native Tokens Reasoning: 0
Native Tokens Total: 2700
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's Meta Llama 4 Maverick LLM model `meta-llama/llama-4-maverick:free`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model meta-llama/llama-4-maverick:free

----- Assistant Response (OpenRouter via CF RAG) -----
Chain of Draft (CoD) is a novel prompting strategy for Large Language Models (LLMs) that encourages them to generate concise, dense-information outputs at each step when solving complex tasks. It is inspired by how humans typically approach problem-solving by jotting down only the critical pieces of information that help them progress.

The main idea behind CoD is to reduce the verbosity and latency associated with traditional Chain of Thought (CoT) prompting strategies, which often involve lengthy and elaborate reasoning steps. By limiting the number of words used in each reasoning step, CoD aims to achieve similar accuracy as CoT while using significantly fewer tokens, thereby reducing computational costs and latency.

According to the provided sources, CoD has been shown to be effective across various reasoning tasks, including arithmetic reasoning, common sense reasoning, and symbolic reasoning. The results demonstrate that CoD can maintain or even improve accuracy compared to CoT while significantly reducing token usage and latency.

The key benefits of CoD are:

1. Reduced latency and computational costs
2. Improved efficiency in solving complex tasks
3. Comparable or superior accuracy to traditional CoT prompting strategies

Overall, Chain of Draft is a promising approach to improving the efficiency and effectiveness of LLMs in solving complex reasoning tasks.

----- Generation Stats -----
Model Used: meta-llama/llama-4-maverick:free
Provider Name: Chutes
Generation Time: 3822 ms
Model Name: Meta: Llama 4 Maverick (free)
Context Length: 256000
Max Completion Tokens: None
Is Moderated: False
Modality: text+image->text
Tokenizer: Other
Supported Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, top_k, min_p, repetition_penalty, logprobs, logit_bias, top_logprobs
Prompt Tokens: 2704
Completion Tokens: 251
Total Tokens: 2955
Total Cost: $0.00000000
Usage: 0
Latency: 738 ms
Native Tokens Prompt: 2693
Native Tokens Completion: 251
Native Tokens Reasoning: 0
Native Tokens Total: 2944
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's Meta Llam 4 Scout LLM model `meta-llama/llama-4-scout:free`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model meta-llama/llama-4-scout:free

----- Assistant Response (OpenRouter via CF RAG) -----
Based on the provided context, Chain of Draft (CoD) is a novel prompting strategy for large language models (LLMs) that aims to reduce verbosity and latency while maintaining accuracy in complex reasoning tasks.

**Definition:** Chain of Draft is a prompting approach that encourages LLMs to generate concise, dense-information outputs at each step, mimicking how humans externalize thought by jotting down only critical pieces of information.

**Key characteristics:**

1. **Concise reasoning drafts**: CoD focuses on essential calculations or transformations needed to progress, reducing unnecessary elaboration.
2. **Reduced verbosity**: CoD aims to minimize the number of words used in each reasoning step.
3. **Latency and cost reduction**: By compacting reasoning steps, CoD reduces the number of input tokens required for few-shot prompting and shortens output token length, directly lowering computational cost.
4. **Comparable or superior accuracy**: CoD achieves similar or better accuracy compared to standard Chain-of-Thought (CoT) prompting strategies.

**Inspiration:** The approach is inspired by human cognitive processes, where individuals often jot down only critical pieces of information to facilitate thought processes when solving complex problems.

**Benefits:**

1. **Reduced latency**: CoD significantly reduces the latency required for reasoning.
2. **Cost efficiency**: CoD offers substantial cost advantages by reducing the number of input tokens and output token length.
3. **Practicality**: CoD makes LLMs more practical for real-world applications where efficiency is crucial.

Overall, Chain of Draft is a novel prompting strategy that balances accuracy and efficiency, making LLMs more suitable for applications requiring low latency and high-quality responses.

----- Generation Stats -----
Model Used: meta-llama/llama-4-scout:free
Provider Name: Chutes
Generation Time: 4489 ms
Model Name: Meta: Llama 4 Scout (free)
Context Length: 512000
Max Completion Tokens: None
Is Moderated: False
Modality: text+image->text
Tokenizer: Other
Supported Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed, top_k, min_p, repetition_penalty, logprobs, logit_bias, top_logprobs
Prompt Tokens: 2724
Completion Tokens: 342
Total Tokens: 3066
Total Cost: $0.00000000
Usage: 0
Latency: 307 ms
Native Tokens Prompt: 2705
Native Tokens Completion: 330
Native Tokens Reasoning: 0
Native Tokens Total: 3035
Cache Discount: None
Temperature: 0.3
Top P: 1.0
Seed: None
Max Tokens: None
Compress: N/A
Compress Rate (Setting): N/A
Original Tokens (LLMLingua-2): N/A
Compressed Tokens (LLMLingua-2): N/A
Compression Rate (LLMLingua-2): N/A
Saving (LLMLingua-2): N/A
LLMLingua-2 max_batch_size: N/A
LLMLingua-2 max_force_token: N/A
~~~

And OpenRouter AI's stealth Quasar Alpha LLM model `openrouter/quasar-alpha`:

~~~bash
python or-cli.py --cfrag -p "You are a helpful assistant" -m "what is chain of draft?" --rewrite-query --max-results 20 --score-threshold 0.5 --cfrag-search-only -t --model openrouter/quasar-alpha

----- Assistant Response (OpenRouter via CF RAG) -----
Chain of Draft (CoD) is a novel prompting strategy for large language models (LLMs) designed to perform complex reasoning tasks m