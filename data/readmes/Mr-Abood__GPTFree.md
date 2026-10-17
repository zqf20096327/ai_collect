# Algion - Free OpenAI-compatible API

🚀 Access powerful AI models through our OpenAI-compatible API.  Completely free and ready to use. 

## Overview

Algion provides a free alternative to OpenAI's API, offering access to advanced AI models without any cost.  Our API is fully compatible with OpenAI's client libraries, making it easy to integrate into your projects.

## Quick Start

### Get Your Free API Key

Get your personal API key for free through our Telegram bot:
- **Bot:** [@AlgionBot](https://t.me/AlgionBot)

Simply start a chat with the bot and it will provide you with your unique API key instantly! 

### API Configuration
- **Base URL:** `https://api.algion.dev/v1`
- **API Key:** Get yours from [@AlgionBot](https://t.me/AlgionBot)

### Installation

```bash
pip install openai
```

### Basic Usage

```python
import openai

client = openai.OpenAI(
    api_key="YOUR_API_KEY",  # Get your key from @AlgionBot
    base_url="https://api.algion.dev/v1"
)

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": "Hello! How are you?"}
    ]
)

print(response.choices[0].message.content)
```

### JavaScript/Node.js Example

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',  // Get your key from @AlgionBot
  baseURL: 'https://api.algion.dev/v1',
});

const response = await client.chat.completions.create({
  model: 'gpt-4.1',
  messages: [{ role: 'user', content: 'Hello! How are you?' }],
});

console.log(response.choices[0].message.content);
```

### cURL Example

```bash
curl -X POST "https://api.algion.dev/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "messages": [{"role": "user", "content": "Hello! How are you?"}]
  }'
```

## Available Models

- `gpt-5.1`
- `gpt-5`
- `gpt-5-mini`
- `gpt-4.1`
- `gpt-4o`
- `gpt-4o-mini`
- `gpt-4-0125-preview`
- `gpt-4`
- `gpt-3.5-turbo`
- `claude-opus-4.5`
- `claude-sonnet-4.5`
- `claude-haiku-4.5`
- `claude-sonnet-4`
- `gemini-3-pro-preview`
- `gemini-2.5-pro`
- `grok-code-fast-1`
- More models coming soon!

## Features

- ✅ **100% Free** - No hidden costs or rate limits
- ✅ **OpenAI Compatible** - Drop-in replacement for OpenAI API
- ✅ **Easy Registration** - Get your API key instantly via Telegram
- ✅ **Personal API Keys** - Each user gets their own unique key
- ✅ **Active Development** - Regular updates and new models

## API Endpoints

All endpoints follow OpenAI's API specification:

- `POST /v1/chat/completions` - Chat completions
- `GET /v1/models` - List available models
- More endpoints coming soon!

## Rate Limits

Currently, there are no strict rate limits, but we ask users to be reasonable with their usage to ensure the service remains available for everyone. 

## Status & Updates

This project is currently in **Beta**. Join our community:

- **Get API Key:** [@AlgionBot](https://t.me/AlgionBot)
- **Updates Channel:** [@algion](https://t.me/algion)

Stay updated on:
- New model releases
- Feature announcements  
- Service updates
- Community discussions

## Contributing

We welcome contributions!  Whether it's bug reports, feature requests, or code contributions, feel free to get involved.

## Support

- **Website:** [algion.dev](https://algion.dev)
- **Get API Key:** [@AlgionBot](https://t.me/AlgionBot)
- **Telegram Channel:** [@algion](https://t.me/algion)
- **Issues:** Create an issue in this repository

## Disclaimer

This service is provided as-is. While we strive for high availability, please consider this when building production applications. 

---

⭐ **Star this repo if you find it useful!**

Made with ❤️ for the developer community

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Mr-Abood/GPTFree&type=Date)](https://star-history.com/#Mr-Abood/GPTFree&Date)
