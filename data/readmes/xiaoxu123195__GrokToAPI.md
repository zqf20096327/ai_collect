<div align="center">

# 🚀 GrokToAPI

**High-Performance OpenAI-Compatible Gateway for Grok AI**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.22%2B-00ADD8?logo=go)](https://golang.org/)
[![GitHub Stars](https://img.shields.io/github/stars/xiaoxu123195/GrokToAPI?style=social)](https://github.com/xiaoxu123195/GrokToAPI/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/xiaoxu123195/GrokToAPI)](https://github.com/xiaoxu123195/GrokToAPI/issues)

[English](README.md) | [中文](README_zh.md)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Supported Models](#-supported-models)
- [Quick Start](#-quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Service](#running-the-service)
- [API Usage](#-api-usage)
  - [Chat Completion](#chat-completion-openai-compatible)
  - [List Models](#list-models)
- [Admin Dashboard](#-admin-dashboard)
  - [Authentication](#authentication)
  - [Token Management](#token-management)
- [Project Structure](#-project-structure)
- [Configuration Reference](#-configuration-reference)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

**GrokToAPI** is a high-performance API gateway that seamlessly bridges **Grok** (XAI's conversational AI) with an **OpenAI-compatible interface**. Built with Go for maximum reliability and speed, it provides:

- ✅ Enterprise-grade token management
- ✅ Intelligent media caching system
- ✅ Comprehensive admin dashboard
- ✅ Full OpenAI API compatibility
- ✅ Advanced TLS fingerprinting to avoid rate limits

Perfect for developers who want to integrate Grok AI into their applications using familiar OpenAI SDK patterns!

---

## ✨ Features

### 🔌 **Core Capabilities**

- **OpenAI-Compatible API** - Drop-in replacement for OpenAI clients
- **Multiple Model Support** - 6 Grok models including fast, expert, and video generation
- **Streaming & Non-Streaming** - Full support for Server-Sent Events (SSE)
- **Token Pool Management** - Intelligent quota tracking with automatic tier fallback

### 🎬 **Media Handling**

- 📸 Automatic caching of images and videos from Grok responses
- 🗄️ LRU-based cache management with configurable size limits
- 🔗 URL rewriting for local media serving
- 🖼️ Support for both URL and base64 image modes

### 🎛️ **Admin Features**

- 📊 Web-based dashboard for token and system management
- 📈 Real-time statistics and usage tracking
- 🔑 Bulk token operations (add/delete/test)
- ⚙️ Live configuration updates

### 🔐 **Advanced Security**

- 🕵️ TLS Fingerprinting - Advanced browser mimicry
- 🛡️ Bearer token authentication
- 🔒 Rate limit handling and monitoring

### 🧠 **Intelligence Features**

- 💭 Model reasoning display (`show_thinking`)
- 🌐 Web search integration
- 📊 Per-model usage statistics
- 🏷️ Response tag filtering

---

## 🎯 Supported Models

| Model | Description | Usage Multiplier | Super Token Required |
|:------|:------------|:----------------:|:--------------------:|
| `grok-3-fast` | ⚡ Fast lightweight model | 1x | ❌ |
| `grok-4-fast` | 🧠 Fast Grok 4 with mini thinking | 1x | ❌ |
| `grok-4-fast-expert` | 🎓 Expert mode with enhanced reasoning | 4x | ❌ |
| `grok-4-expert` | 🏆 Full Grok 4 expert capabilities | 4x | ❌ |
| `grok-4-heavy` | 💎 Most powerful model | 1x | ✅ |
| `grok-imagine-0.9` | 🎥 Video generation model | - | ❌ |

---

## 🚀 Quick Start

### Prerequisites

- **Go** 1.22.0 or higher
- Valid **Grok API tokens** (Normal or Super tier)

### Installation

```bash
# Clone the repository
git clone https://github.com/xiaoxu123195/GrokToAPI.git
cd GrokToAPI

# Build the binary
go build -o groktoapi ./cmd/groktoapi
```

Or download pre-built binaries from the [Releases](https://github.com/xiaoxu123195/GrokToAPI/releases) page.

### Configuration

1️⃣ **Copy the configuration template:**
```bash
cp data/setting.toml.example data/setting.toml
```

2️⃣ **Edit `data/setting.toml` with your settings:**

```toml
[grok]
api_key = "your-api-key"              # Any string for API validation
proxy_url = ""                        # Optional HTTP proxy
show_thinking = true                  # Display model reasoning
stream_chunk_timeout = 120            # Per-chunk timeout (seconds)
stream_total_timeout = 600            # Total stream timeout (seconds)

[global]
base_url = "http://localhost:8000"    # Your service URL
log_level = "INFO"                    # DEBUG, INFO, WARN, ERROR
image_mode = "url"                    # "url" or "base64"
admin_username = "admin"              # Dashboard username
admin_password = "your-secure-password"  # Dashboard password
image_cache_max_size_mb = 512         # Image cache limit (MB)
video_cache_max_size_mb = 1024        # Video cache limit (MB)
```

3️⃣ **Add your Grok tokens:**
- Manually edit `data/token.json`, or
- Use the Admin API after starting the service

### Running the Service

```bash
# Default (listens on :8000)
./groktoapi

# Custom configuration
./groktoapi -config /path/to/setting.toml -addr :8080
```

The service will be available at `http://localhost:8000` 🎉

---

## 📡 API Usage

### Chat Completion (OpenAI Compatible)

**Streaming Request:**
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "grok-4-fast",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ],
    "stream": true
  }'
```

**Non-Streaming Request:**
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "grok-4-fast",
    "messages": [
      {
        "role": "user",
        "content": "Hello, Grok!"
      }
    ],
    "stream": false
  }'
```

### List Models

```bash
curl http://localhost:8000/v1/models \
  -H "Authorization: Bearer your-api-key"
```

**Response:**
```json
{
  "object": "list",
  "data": [
    {
      "id": "grok-4-fast",
      "object": "model",
      "created": 1677649963,
      "owned_by": "xai"
    }
  ]
}
```

---

## 🎛️ Admin Dashboard

Access the admin dashboard at: **`http://localhost:8000/v1/admin/`**

### Authentication

**Login to get a session token:**
```bash
curl http://localhost:8000/v1/admin/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "your-password"
  }'
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Token Management

**Add Tokens:**
```bash
curl http://localhost:8000/v1/admin/api/tokens/add \
  -H "Authorization: Bearer your-admin-token" \
  -H "Content-Type: application/json" \
  -d '{
    "tokens": ["token1", "token2"],
    "token_type": "Normal"
  }'
```

**Get Statistics:**
```bash
curl http://localhost:8000/v1/admin/api/stats \
  -H "Authorization: Bearer your-admin-token"
```

**Response Example:**
```json
{
  "pool_stats": {
    "normal": {
      "active": 10,
      "limited": 2,
      "expired": 1
    }
  },
  "usage_stats": {
    "grok-4-fast": 150,
    "grok-4-expert": 45
  },
  "total_quota": 750
}
```

📖 **Full API Documentation:** [docs/admin_api.md](docs/admin_api.md)

---

## 📂 Project Structure

```
GrokToAPI/
├── 📁 cmd/
│   └── 📁 groktoapi/           # 🚪 Application entry point
├── 📁 internal/
│   ├── 📁 api/                 # 🌐 HTTP routing and handlers
│   ├── 📁 cache/               # 💾 Media caching system
│   ├── 📁 chat/                # 💬 Chat service layer
│   ├── 📁 config/              # ⚙️ Configuration management
│   ├── 📁 grok/                # 🤖 Grok API client
│   ├── 📁 models/              # 📋 Model definitions and catalog
│   ├── 📁 storage/             # 🗄️ Token persistence
│   ├── 📁 token/               # 🎫 Token pool management
│   └── 📁 logger/              # 📝 Logging utilities
├── 📁 data/
│   ├── ⚙️ setting.toml         # Configuration file
│   └── 💾 token.json           # Token storage
├── 📁 docs/                    # 📚 Documentation
└── 📁 web/                     # 🎨 Frontend assets (future)
```

---

## ⚙️ Configuration Reference

### `[grok]` Section

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `api_key` | string | - | API authentication key (any string) |
| `base_endpoint` | string | - | Custom Grok API endpoint (optional) |
| `proxy_url` | string | - | HTTP proxy for API requests |
| `cache_proxy_url` | string | - | Separate proxy for media downloads |
| `cf_clearance` | string | - | Cloudflare clearance cookie |
| `x_statsig_id` | string | - | Browser fingerprinting ID (base64) |
| `dynamic_statsig` | bool | false | Auto-generate Statsig ID |
| `filtered_tags` | string | - | Comma-separated tags to filter |
| `stream_chunk_timeout` | int | 120 | Per-chunk timeout (seconds) |
| `stream_total_timeout` | int | 600 | Total stream timeout (seconds) |
| `stream_first_response_timeout` | int | 30 | Initial response timeout (seconds) |
| `show_thinking` | bool | true | Display model reasoning process |

### `[global]` Section

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `base_url` | string | - | Base URL for media file serving |
| `log_level` | string | INFO | Logging level (DEBUG/INFO/WARN/ERROR) |
| `image_mode` | string | url | Media format ("url" or "base64") |
| `admin_username` | string | admin | Dashboard username |
| `admin_password` | string | - | Dashboard password |
| `image_cache_max_size_mb` | int | 512 | Image cache size limit (MB) |
| `video_cache_max_size_mb` | int | 1024 | Video cache size limit (MB) |

---

## 🛠️ Development

### Building

```bash
# Build for current platform
go build -o groktoapi ./cmd/groktoapi

# Build for Linux
GOOS=linux GOARCH=amd64 go build -o groktoapi-linux ./cmd/groktoapi

# Build for Windows
GOOS=windows GOARCH=amd64 go build -o groktoapi.exe ./cmd/groktoapi
```

### Testing

```bash
# Run all tests
go test ./...

# Run with coverage
go test -cover ./...

# Generate coverage report
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

### Dependencies

| Package | Purpose |
|:--------|:--------|
| [`gin-gonic/gin`](https://github.com/gin-gonic/gin) | 🌐 HTTP web framework |
| [`bogdanfinn/tls-client`](https://github.com/bogdanfinn/tls-client) | 🔐 Browser fingerprinting |
| [`rs/zerolog`](https://github.com/rs/zerolog) | 📝 Structured logging |
| [`spf13/viper`](https://github.com/spf13/viper) | ⚙️ Configuration management |
| [`google/uuid`](https://github.com/google/uuid) | 🆔 UUID generation |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔨 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 GrokToAPI Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🙏 Acknowledgments

- 🐍 Originally ported from a Python implementation
- ⚡ Built with Go for enhanced performance and reliability
- 🤖 Powered by [XAI's Grok](https://x.ai/) conversational AI
- 💙 Inspired by the open-source community

---

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/xiaoxu123195/GrokToAPI/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/xiaoxu123195/GrokToAPI/discussions)
- 📧 **Email**: [Create an issue](https://github.com/xiaoxu123195/GrokToAPI/issues/new)

---

<div align="center">

**Made with ❤️ by the GrokToAPI Team**

⭐ Star us on GitHub — it helps!

[⬆ Back to Top](#-groktoapi)

</div>
