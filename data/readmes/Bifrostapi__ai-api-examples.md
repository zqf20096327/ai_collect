# Bifrostapi AI API Gateway 🚀

![GitHub stars](https://img.shields.io/github/stars/Bifrostapi/ai-api-examples)
![GitHub license](https://img.shields.io/github/license/Bifrostapi/ai-api-examples)
![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI%20Compatible-blue)
![Models](https://img.shields.io/badge/Models-GPT%20Claude%20Gemini%20DeepSeek-purple)

One API to access GPT, Claude, Gemini, DeepSeek and other LLMs.

## Why Bifrostapi?

Building AI applications often requires managing multiple AI providers:

- Different API formats
- Multiple API keys
- Complex billing systems
- Difficult model switching

Bifrostapi provides a unified API layer that makes AI infrastructure simpler.

**One API.  
Multiple models.  
Simple integration.**

---

## Features

✅ OpenAI-compatible API

✅ Access multiple AI models through one endpoint

✅ Simplified API key management

✅ Unified AI infrastructure

✅ Developer-friendly integration

✅ Flexible model switching

---

## Supported Models

| Provider | Models |
| --- | --- |
| OpenAI | GPT models |
| Anthropic | Claude models |
| Google | Gemini models |
| DeepSeek | DeepSeek models |
| More | OpenAI-compatible models |

---

## Quick Start
### 1. Install OpenAI SDK

```bash
pip install openai
```

### 2. Connect to Bifrostapi

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="YOUR_API_ENDPOINT"
)

response = client.chat.completions.create(
    model="your-model",
    messages=[
        {
            "role": "user",
            "content": "Hello Bifrostapi"
        }
    ]
)

print(response)
```
