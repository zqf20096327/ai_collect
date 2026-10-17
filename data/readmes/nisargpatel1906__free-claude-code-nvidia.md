<pre>
███╗   ██╗ ██╗   ██╗ ██████╗ ██████╗  ██████╗  █████╗  
████╗  ██║ ██║   ██║ ╚══██╔╝ ██╔══██╗ ╚══██╔╝ ██╔══██╗ 
██╔██╗ ██║ ██║   ██║    ██║  ██║  ██║    ██║  ███████║ 
██║╚██╗██║ ╚██╗ ██╔╝    ██║  ██║  ██║    ██║  ██╔══██║ 
██║ ╚████║  ╚████╔╝  ██████╗ ██████╔╝ ██████╗ ██║  ██║ 
╚═╝  ╚═══╝   ╚═══╝   ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ 

 ██████╗ ██╗       █████╗  ██╗   ██╗ ██████╗  ███████╗      ██████╗  ██████╗  ██████╗  ███████╗ 
██╔════╝ ██║      ██╔══██╗ ██║   ██║ ██╔══██╗ ██╔════╝     ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝ 
██║      ██║      ███████║ ██║   ██║ ██║  ██║ █████╗       ██║      ██║   ██║ ██║  ██║ █████╗   
██║      ██║      ██╔══██║ ██║   ██║ ██║  ██║ ██╔═══╝      ██║      ██║   ██║ ██║  ██║ ██╔═══╝  
╚██████╗ ███████╗ ██║  ██║ ╚██████╔╝ ██████╔╝ ███████╗     ╚██████╗ ╚██████╔╝ ██████╔╝ ███████╗ 
 ╚═════╝ ╚══════╝ ╚═╝  ╚═╝  ╚═════╝  ╚═════╝  ╚══════╝      ╚═════╝  ╚══════╝ ╚═════╝  ╚══════╝
</pre>

# 🆓 Free Claude Code with NVIDIA NIM — Complete Setup Guide

[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-blue)]()  
[![NVIDIA NIM](https://img.shields.io/badge/NVIDIA-NIM%20Free%20Tier-76b900?logo=nvidia)]()  
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-orange)]()  
[![LiteLLM](https://img.shields.io/badge/LiteLLM-Proxy-purple)]()  

Use **Claude Code** (Anthropic's official AI coding agent) **completely free** by routing it through **NVIDIA's free NIM API** — with access to **100+ AI models** including Llama, Mistral, DeepSeek, Gemma, and more. **No Anthropic subscription needed!**

**Works on:** ✅ Windows &nbsp;&nbsp; ✅ macOS

---

## 📐 Architecture Overview

Claude Code natively communicates using Anthropic's API format. To make it work with NVIDIA NIM:
1. **Claude Code** acts as the frontend CLI tool, routing all requests to a local proxy instead of Anthropic's default servers.
2. **LiteLLM Proxy** runs locally on port `4000` as a translation layer. It intercepts Anthropic-formatted requests from Claude Code, converts them to OpenAI-compatible format, and forwards them to the NVIDIA NIM endpoint (`integrate.api.nvidia.com`).
3. **NVIDIA API Gateway** processes the model request and returns the response.

```
┌─────────────┐        (Anthropic TUI API)       ┌─────────────────┐
│ Claude Code │ ───────────────────────────────> │  LiteLLM Proxy  │
│     CLI     │ <─────────────────────────────── │ (http://localhost:4000)
└─────────────┘                                  └─────────────────┘
                                                          │
                                                          │ (OpenAI Format)
                                                          ▼
                                                 ┌─────────────────┐
                                                 │   NVIDIA NIM    │
                                                 │   API Gateway   │
                                                 └─────────────────┘
```


## 📋 Table of Contents
- [🔑 Step 0: Get Your Free NVIDIA API Key](#-step-0-get-your-free-nvidia-api-key)
- [🚀 Quick Start (Copy-Paste Guide)](#-quick-start-copy-paste-guide)
- [Step 1: Install Node.js & Python](#step-1-install-nodejs--python)
- [Step 2: Install Claude Code](#step-2-install-claude-code)
- [Step 3: Install LiteLLM Proxy](#step-3-install-litellm-proxy)
- [Step 4: Configure LiteLLM (`litellm_config.yaml`)](#step-4-configure-litellm-config-litellm_configyaml)
- [Step 5: Configure Claude Code Settings (`settings.json`)](#step-5-configure-claude-code-settings-settingsjson)
- [Step 6: Start & Stop the LiteLLM Server](#step-6-start--stop-the-litellm-server)
- [Step 7: Run Claude Code!](#step-7-run-claude-code)
- [🔄 Model Switch & Selection Guide](#-model-switch--selection-guide)
- [🗂️ NVIDIA NIM Models Directory](#-nvidia-nim-models-directory)
- [📐 Architecture Overview](#architecture-overview)
- [⚠️ Troubleshooting & Exceptions](#️-troubleshooting--exceptions)

> 💡 **Tip:** If you run into any command errors (e.g., `pip` not found, port conflicts, or permissions issues), scroll to the very bottom to find the **[Troubleshooting & Exceptions](#️-troubleshooting--exceptions)** section for quick copy-paste fixes!

---


## 🔑 Step 0: Get Your Free NVIDIA API Key

Before anything else, you need a **free** NVIDIA API key. Here is how to get one in 2 minutes:

1. Go to **https://build.nvidia.com**
2. Click **"Sign In"** → then **"Create Account"** (completely free, no credit card needed)
3. After logging in, click on **any model** (e.g., `meta/llama-3.1-70b-instruct`)
4. On the model page, click the green **"Get API Key"** button at the top right
5. Click **"Generate Key"** and copy your key — it looks like: `nvapi-xxxxxxxxxxxxxxxxxxxx`
6. **Save this key** — you will paste it in Steps 4 and 5 below

> **Free Tier:** NVIDIA gives you free API credits every month. No credit card required. The free tier is more than enough for personal coding use with Claude Code.

---

## 🚀 Quick Start (Copy-Paste Guide)

Follow these steps to get Claude Code running with NVIDIA models:

### Step 1: Install CLI Tools
Open your terminal and run:
```bash
# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Install LiteLLM Proxy
# Windows:
pip install litellm
# macOS:
# pip3 install litellm
```

### Step 2: Create the Configurations

**Windows users:**
1. Create a file at `%USERPROFILE%\.claude\litellm_config.yaml` and paste the full config from **Step 4** below (replace `YOUR_NVIDIA_API_KEY`).
2. Create a file at `%USERPROFILE%\.claude\settings.json` and paste the full settings from **Step 5** below (replace `YOUR_NVIDIA_API_KEY`).

**macOS users:**
1. Create a file at `~/.claude/litellm_config.yaml` and paste the full config from **Step 4** below (replace `YOUR_NVIDIA_API_KEY`).
2. Create a file at `~/.claude/settings.json` and paste the full settings from **Step 5** below (replace `YOUR_NVIDIA_API_KEY`).

> 💡 **Tip:** On macOS, run `mkdir -p ~/.claude` in Terminal first to create the folder if it doesn't exist.

### Step 3: Start the Local Proxy Server

**Windows** (CMD or PowerShell):
```cmd
litellm --config "%USERPROFILE%\.claude\litellm_config.yaml" --port 4000
```

**macOS** (Terminal):
```bash
litellm --config ~/.claude/litellm_config.yaml --port 4000
```

*(Keep this terminal window open while using Claude Code. See Step 6 for running it silently in the background.)*

### Step 4: Run Claude Code!
Open a new terminal window and run:
```bash
claude
```
Claude Code will automatically connect to your local proxy and use your configured NVIDIA model!

---

## Step 1: Install Node.js & Python

You need two runtimes. If you already have them, skip to Step 2.

### 🪟 Windows

**Option A — Install via Windows Package Manager (winget) — Recommended:**
```cmd
winget install OpenJS.NodeJS
winget install Python.Python.3.11
```

**Option B — Download manually:**
- **Node.js** (v18+): https://nodejs.org/en/download
- **Python** (v3.8+): https://www.python.org/downloads

After installing, close and reopen your terminal, then verify:
```cmd
node --version
python --version
```

### 🍎 macOS

**Option A — Install via Homebrew — Recommended:**
```bash
# Install Homebrew first if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Node.js and Python
brew install node
brew install python@3.11
```

**Option B — Download manually:**
- **Node.js** (v18+): https://nodejs.org/en/download
- **Python** (v3.8+): https://www.python.org/downloads

Verify in Terminal:
```bash
node --version
python3 --version
```

---

## Step 2: Install Claude Code

Claude Code is installed globally using the Node Package Manager (`npm`):

1. Open your **Command Prompt / PowerShell** (Windows) or **Terminal** (macOS).
2. Run the installation command:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
3. Verify the installation by checking its version:
   ```bash
   claude --version
   ```

---

## Step 3: Install LiteLLM Proxy

LiteLLM routes standard API requests to NVIDIA's gateway.

**Windows:**
```cmd
pip install litellm
```

**macOS:**
```bash
pip3 install litellm
```

---

## Step 4: Configure LiteLLM Config (`litellm_config.yaml`)

Create a configuration file named `litellm_config.yaml` inside your Claude configuration folder:
- **Windows:** `%USERPROFILE%\.claude\litellm_config.yaml`
- **macOS:** `~/.claude/litellm_config.yaml`

This config maps all NVIDIA NIM model IDs using a `custom_openai/` prefix, forcing LiteLLM to act as a generic OpenAI-compatible router and forward the literal model names directly to NVIDIA's gateway, bypassing outdated hardcoded internal translations.

<details>
<summary><b>Click to expand full copy-pasteable litellm_config.yaml (731 lines)</b></summary>

```yaml
litellm_settings:
  drop_params: true

model_list:
  - model_name: 01-ai/yi-large
    litellm_params:
      model: custom_openai/01-ai/yi-large
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: abacusai/dracarys-llama-3.1-70b-instruct
    litellm_params:
      model: custom_openai/abacusai/dracarys-llama-3.1-70b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: adept/fuyu-8b
    litellm_params:
      model: custom_openai/adept/fuyu-8b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: ai21labs/jamba-1.5-large-instruct
    litellm_params:
      model: custom_openai/ai21labs/jamba-1.5-large-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: aisingapore/sea-lion-7b-instruct
    litellm_params:
      model: custom_openai/aisingapore/sea-lion-7b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: baai/bge-m3
    litellm_params:
      model: custom_openai/baai/bge-m3
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: bigcode/starcoder2-15b
    litellm_params:
      model: custom_openai/bigcode/starcoder2-15b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: bytedance/seed-oss-36b-instruct
    litellm_params:
      model: custom_openai/bytedance/seed-oss-36b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: databricks/dbrx-instruct
    litellm_params:
      model: custom_openai/databricks/dbrx-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: deepseek-ai/deepseek-coder-6.7b-instruct
    litellm_params:
      model: custom_openai/deepseek-ai/deepseek-coder-6.7b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: deepseek-ai/deepseek-v4-flash
    litellm_params:
      model: custom_openai/deepseek-ai/deepseek-v4-flash
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: deepseek-ai/deepseek-v4-pro
    litellm_params:
      model: custom_openai/deepseek-ai/deepseek-v4-pro
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/codegemma-1.1-7b
    litellm_params:
      model: custom_openai/google/codegemma-1.1-7b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/codegemma-7b
    litellm_params:
      model: custom_openai/google/codegemma-7b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/deplot
    litellm_params:
      model: custom_openai/google/deplot
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/diffusiongemma-26b-a4b-it
    litellm_params:
      model: custom_openai/google/diffusiongemma-26b-a4b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-2-2b-it
    litellm_params:
      model: custom_openai/google/gemma-2-2b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-2b
    litellm_params:
      model: custom_openai/google/gemma-2b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-3-12b-it
    litellm_params:
      model: custom_openai/google/gemma-3-12b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-3-4b-it
    litellm_params:
      model: custom_openai/google/gemma-3-4b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-3n-e2b-it
    litellm_params:
      model: custom_openai/google/gemma-3n-e2b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-3n-e4b-it
    litellm_params:
      model: custom_openai/google/gemma-3n-e4b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/gemma-4-31b-it
    litellm_params:
      model: custom_openai/google/gemma-4-31b-it
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: google/recurrentgemma-2b
    litellm_params:
      model: custom_openai/google/recurrentgemma-2b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: ibm/granite-3.0-3b-a800m-instruct
    litellm_params:
      model: custom_openai/ibm/granite-3.0-3b-a800m-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: ibm/granite-3.0-8b-instruct
    litellm_params:
      model: custom_openai/ibm/granite-3.0-8b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: ibm/granite-34b-code-instruct
    litellm_params:
      model: custom_openai/ibm/granite-34b-code-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: ibm/granite-8b-code-instruct
    litellm_params:
      model: custom_openai/ibm/granite-8b-code-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/codellama-70b
    litellm_params:
      model: custom_openai/meta/codellama-70b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.1-70b-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.1-70b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.1-8b-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.1-8b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.2-11b-vision-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.2-11b-vision-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.2-1b-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.2-1b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.2-3b-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.2-3b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.2-90b-vision-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.2-90b-vision-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-3.3-70b-instruct
    litellm_params:
      model: custom_openai/meta/llama-3.3-70b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-4-maverick-17b-128e-instruct
    litellm_params:
      model: custom_openai/meta/llama-4-maverick-17b-128e-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama-guard-4-12b
    litellm_params:
      model: custom_openai/meta/llama-guard-4-12b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: meta/llama2-70b
    litellm_params:
      model: custom_openai/meta/llama2-70b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: microsoft/kosmos-2
    litellm_params:
      model: custom_openai/microsoft/kosmos-2
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: microsoft/phi-3-vision-128k-instruct
    litellm_params:
      model: custom_openai/microsoft/phi-3-vision-128k-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: microsoft/phi-3.5-moe-instruct
    litellm_params:
      model: custom_openai/microsoft/phi-3.5-moe-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: microsoft/phi-4-mini-instruct
    litellm_params:
      model: custom_openai/microsoft/phi-4-mini-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: microsoft/phi-4-multimodal-instruct
    litellm_params:
      model: custom_openai/microsoft/phi-4-multimodal-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: minimaxai/minimax-m2.7
    litellm_params:
      model: custom_openai/minimaxai/minimax-m2.7
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: minimaxai/minimax-m3
    litellm_params:
      model: custom_openai/minimaxai/minimax-m3
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/codestral-22b-instruct-v0.1
    litellm_params:
      model: custom_openai/mistralai/codestral-22b-instruct-v0.1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/ministral-14b-instruct-2512
    litellm_params:
      model: custom_openai/mistralai/ministral-14b-instruct-2512
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-7b-instruct-v0.3
    litellm_params:
      model: custom_openai/mistralai/mistral-7b-instruct-v0.3
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-large
    litellm_params:
      model: custom_openai/mistralai/mistral-large
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-large-2-instruct
    litellm_params:
      model: custom_openai/mistralai/mistral-large-2-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-large-3-675b-instruct-2512
    litellm_params:
      model: custom_openai/mistralai/mistral-large-3-675b-instruct-2512
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-medium-3.5-128b
    litellm_params:
      model: custom_openai/mistralai/mistral-medium-3.5-128b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-nemotron
    litellm_params:
      model: custom_openai/mistralai/mistral-nemotron
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mistral-small-4-119b-2603
    litellm_params:
      model: custom_openai/mistralai/mistral-small-4-119b-2603
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mixtral-8x22b-v0.1
    litellm_params:
      model: custom_openai/mistralai/mixtral-8x22b-v0.1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: mistralai/mixtral-8x7b-instruct-v0.1
    litellm_params:
      model: custom_openai/mistralai/mixtral-8x7b-instruct-v0.1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: moonshotai/kimi-k2.6
    litellm_params:
      model: custom_openai/moonshotai/kimi-k2.6
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nv-mistralai/mistral-nemo-12b-instruct
    litellm_params:
      model: custom_openai/nv-mistralai/mistral-nemo-12b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/ai-synthetic-video-detector
    litellm_params:
      model: custom_openai/nvidia/ai-synthetic-video-detector
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/cosmos-reason2-8b
    litellm_params:
      model: custom_openai/nvidia/cosmos-reason2-8b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/embed-qa-4
    litellm_params:
      model: custom_openai/nvidia/embed-qa-4
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/gliner-pii
    litellm_params:
      model: custom_openai/nvidia/gliner-pii
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/ising-calibration-1-35b-a3b
    litellm_params:
      model: custom_openai/nvidia/ising-calibration-1-35b-a3b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemoguard-8b-content-safety
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemoguard-8b-content-safety
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemoguard-8b-topic-control
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemoguard-8b-topic-control
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemotron-51b-instruct
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemotron-51b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemotron-70b-instruct
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemotron-70b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemotron-nano-8b-v1
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemotron-nano-8b-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemotron-nano-vl-8b-v1
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemotron-nano-vl-8b-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemotron-safety-guard-8b-v3
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemotron-safety-guard-8b-v3
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.1-nemotron-ultra-253b-v1
    litellm_params:
      model: custom_openai/nvidia/llama-3.1-nemotron-ultra-253b-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1
    litellm_params:
      model: custom_openai/nvidia/llama-3.2-nemoretriever-1b-vlm-embed-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.2-nv-embedqa-1b-v1
    litellm_params:
      model: custom_openai/nvidia/llama-3.2-nv-embedqa-1b-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.3-nemotron-super-49b-v1
    litellm_params:
      model: custom_openai/nvidia/llama-3.3-nemotron-super-49b-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-3.3-nemotron-super-49b-v1.5
    litellm_params:
      model: custom_openai/nvidia/llama-3.3-nemotron-super-49b-v1.5
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-nemotron-embed-1b-v2
    litellm_params:
      model: custom_openai/nvidia/llama-nemotron-embed-1b-v2
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama-nemotron-embed-vl-1b-v2
    litellm_params:
      model: custom_openai/nvidia/llama-nemotron-embed-vl-1b-v2
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/llama3-chatqa-1.5-70b
    litellm_params:
      model: custom_openai/nvidia/llama3-chatqa-1.5-70b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/mistral-nemo-minitron-8b-8k-instruct
    litellm_params:
      model: custom_openai/nvidia/mistral-nemo-minitron-8b-8k-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemoretriever-parse
    litellm_params:
      model: custom_openai/nvidia/nemoretriever-parse
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-3-content-safety
    litellm_params:
      model: custom_openai/nvidia/nemotron-3-content-safety
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-3-nano-30b-a3b
    litellm_params:
      model: custom_openai/nvidia/nemotron-3-nano-30b-a3b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
    litellm_params:
      model: custom_openai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-3-super-120b-a12b
    litellm_params:
      model: custom_openai/nvidia/nemotron-3-super-120b-a12b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-3-ultra-550b-a55b
    litellm_params:
      model: custom_openai/nvidia/nemotron-3-ultra-550b-a55b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-3.5-content-safety
    litellm_params:
      model: custom_openai/nvidia/nemotron-3.5-content-safety
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-4-340b-instruct
    litellm_params:
      model: custom_openai/nvidia/nemotron-4-340b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-4-340b-reward
    litellm_params:
      model: custom_openai/nvidia/nemotron-4-340b-reward
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-content-safety-reasoning-4b
    litellm_params:
      model: custom_openai/nvidia/nemotron-content-safety-reasoning-4b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-mini-4b-instruct
    litellm_params:
      model: custom_openai/nvidia/nemotron-mini-4b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-nano-12b-v2-vl
    litellm_params:
      model: custom_openai/nvidia/nemotron-nano-12b-v2-vl
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-nano-3-30b-a3b
    litellm_params:
      model: custom_openai/nvidia/nemotron-nano-3-30b-a3b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nemotron-parse
    litellm_params:
      model: custom_openai/nvidia/nemotron-parse
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/neva-22b
    litellm_params:
      model: custom_openai/nvidia/neva-22b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nv-embed-v1
    litellm_params:
      model: custom_openai/nvidia/nv-embed-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nv-embedcode-7b-v1
    litellm_params:
      model: custom_openai/nvidia/nv-embedcode-7b-v1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nv-embedqa-e5-v5
    litellm_params:
      model: custom_openai/nvidia/nv-embedqa-e5-v5
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nv-embedqa-mistral-7b-v2
    litellm_params:
      model: custom_openai/nvidia/nv-embedqa-mistral-7b-v2
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nvclip
    litellm_params:
      model: custom_openai/nvidia/nvclip
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/nvidia-nemotron-nano-9b-v2
    litellm_params:
      model: custom_openai/nvidia/nvidia-nemotron-nano-9b-v2
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/riva-translate-4b-instruct
    litellm_params:
      model: custom_openai/nvidia/riva-translate-4b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/riva-translate-4b-instruct-v1.1
    litellm_params:
      model: custom_openai/nvidia/riva-translate-4b-instruct-v1.1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: nvidia/vila
    litellm_params:
      model: custom_openai/nvidia/vila
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: openai/gpt-oss-120b
    litellm_params:
      model: custom_openai/openai/gpt-oss-120b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: openai/gpt-oss-20b
    litellm_params:
      model: custom_openai/openai/gpt-oss-20b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: qwen/qwen3-next-80b-a3b-instruct
    litellm_params:
      model: custom_openai/qwen/qwen3-next-80b-a3b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: qwen/qwen3.5-122b-a10b
    litellm_params:
      model: custom_openai/qwen/qwen3.5-122b-a10b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: qwen/qwen3.5-397b-a17b
    litellm_params:
      model: custom_openai/qwen/qwen3.5-397b-a17b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: sarvamai/sarvam-m
    litellm_params:
      model: custom_openai/sarvamai/sarvam-m
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: snowflake/arctic-embed-l
    litellm_params:
      model: custom_openai/snowflake/arctic-embed-l
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: stepfun-ai/step-3.5-flash
    litellm_params:
      model: custom_openai/stepfun-ai/step-3.5-flash
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: stepfun-ai/step-3.7-flash
    litellm_params:
      model: custom_openai/stepfun-ai/step-3.7-flash
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: stockmark/stockmark-2-100b-instruct
    litellm_params:
      model: custom_openai/stockmark/stockmark-2-100b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: upstage/solar-10.7b-instruct
    litellm_params:
      model: custom_openai/upstage/solar-10.7b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: writer/palmyra-creative-122b
    litellm_params:
      model: custom_openai/writer/palmyra-creative-122b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: writer/palmyra-fin-70b-32k
    litellm_params:
      model: custom_openai/writer/palmyra-fin-70b-32k
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: writer/palmyra-med-70b
    litellm_params:
      model: custom_openai/writer/palmyra-med-70b
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: writer/palmyra-med-70b-32k
    litellm_params:
      model: custom_openai/writer/palmyra-med-70b-32k
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: z-ai/glm-5.1
    litellm_params:
      model: custom_openai/z-ai/glm-5.1
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
  - model_name: zyphra/zamba2-7b-instruct
    litellm_params:
      model: custom_openai/zyphra/zamba2-7b-instruct
      api_key: "YOUR_NVIDIA_API_KEY"
      api_base: https://integrate.api.nvidia.com/v1
      max_tokens: 4096
```
</details>

---


## Step 5: Configure Claude Code Settings (`settings.json`)

To redirect Claude Code's traffic to your local LiteLLM proxy and make the mapped models discoverable, configure the `settings.json` file inside your `.claude` folder:
- **Windows:** `%USERPROFILE%\.claude\settings.json`
- **macOS:** `~/.claude/settings.json`


<details>
<summary><b>Click to expand full copy-pasteable settings.json (88 lines)</b></summary>

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:4000",
    "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
    "ANTHROPIC_API_KEY": "temp-key",
    "CLAUDE_API_KEY": "temp-key",
    "ANTHROPIC_AUTH_TOKEN": "temp-key",
    "NVIDIA_API_KEY": "YOUR_NVIDIA_API_KEY"
  },
  "primaryInstance": {
    "endpoint": "http://localhost:4000"
  },
  "hasCompletedOnboarding": true,
  "telemetry": "off",
  "permissions": {
    "defaultMode": "bypassPermissions"
  },
  "model": "meta/llama-3.1-70b-instruct",
  "availableModels": [
    "abacusai/dracarys-llama-3.1-70b-instruct",
    "bytedance/seed-oss-36b-instruct",
    "deepseek-ai/deepseek-v4-flash",
    "deepseek-ai/deepseek-v4-pro",
    "google/diffusiongemma-26b-a4b-it",
    "google/gemma-2-2b-it",
    "google/gemma-3n-e2b-it",
    "google/gemma-3n-e4b-it",
    "google/gemma-4-31b-it",
    "meta/llama-3.1-70b-instruct",
    "meta/llama-3.1-8b-instruct",
    "meta/llama-3.2-11b-vision-instruct",
    "meta/llama-3.2-1b-instruct",
    "meta/llama-3.2-3b-instruct",
    "meta/llama-3.2-90b-vision-instruct",
    "meta/llama-3.3-70b-instruct",
    "meta/llama-4-maverick-17b-128e-instruct",
    "meta/llama-guard-4-12b",
    "microsoft/phi-4-mini-instruct",
    "microsoft/phi-4-multimodal-instruct",
    "minimaxai/minimax-m2.7",
    "minimaxai/minimax-m3",
    "mistralai/ministral-14b-instruct-2512",
    "mistralai/mistral-large-3-675b-instruct-2512",
    "mistralai/mistral-medium-3.5-128b",
    "mistralai/mistral-nemotron",
    "mistralai/mistral-small-4-119b-2603",
    "mistralai/mixtral-8x7b-instruct-v0.1",
    "moonshotai/kimi-k2.6",
    "nvidia/ai-synthetic-video-detector",
    "nvidia/gliner-pii",
    "nvidia/ising-calibration-1-35b-a3b",
    "nvidia/llama-3.1-nemoguard-8b-content-safety",
    "nvidia/llama-3.1-nemoguard-8b-topic-control",
    "nvidia/llama-3.1-nemotron-nano-8b-v1",
    "nvidia/llama-3.1-nemotron-nano-vl-8b-v1",
    "nvidia/llama-3.1-nemotron-safety-guard-8b-v3",
    "nvidia/llama-3.3-nemotron-super-49b-v1",
    "nvidia/llama-3.3-nemotron-super-49b-v1.5",
    "nvidia/nemoretriever-parse",
    "nvidia/nemotron-3-content-safety",
    "nvidia/nemotron-3-nano-30b-a3b",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
    "nvidia/nemotron-3-super-120b-a12b",
    "nvidia/nemotron-3-ultra-550b-a55b",
    "nvidia/nemotron-3.5-content-safety",
    "nvidia/nemotron-content-safety-reasoning-4b",
    "nvidia/nemotron-mini-4b-instruct",
    "nvidia/nemotron-nano-12b-v2-vl",
    "nvidia/nemotron-parse",
    "nvidia/nvidia-nemotron-nano-9b-v2",
    "nvidia/riva-translate-4b-instruct-v1.1",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "qwen/qwen3-next-80b-a3b-instruct",
    "qwen/qwen3.5-122b-a10b",
    "qwen/qwen3.5-397b-a17b",
    "sarvamai/sarvam-m",
    "stepfun-ai/step-3.5-flash",
    "stepfun-ai/step-3.7-flash",
    "stockmark/stockmark-2-100b-instruct",
    "upstage/solar-10.7b-instruct",
    "z-ai/glm-5.1"
  ],
  "autoUpdatesChannel": "latest",
  "skipDangerousModePermissionPrompt": true
}
```
</details>

---


## Step 6: Start & Stop the LiteLLM Server

### Start the Server (Manual)

**Windows** (CMD or PowerShell):
```cmd
litellm --config "%USERPROFILE%\.claude\litellm_config.yaml" --port 4000
```

**macOS** (Terminal):
```bash
litellm --config ~/.claude/litellm_config.yaml --port 4000
```

*(Keep this terminal window open while using Claude Code. See below to run it silently in the background.)*

---

### Start the Server (Automatic/Silent Startup) - Optional

**Windows:**
To run the server invisibly in the background, place a Visual Basic Script (`start_litellm_proxy.vbs`) inside the Windows Startup folder:
`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\start_litellm_proxy.vbs`

Script content:
```vbs
Set WshShell = CreateObject("WScript.Shell")
Dim configPath
configPath = WshShell.ExpandEnvironmentStrings("%USERPROFILE%") & "\.claude\litellm_config.yaml"
WshShell.Run "litellm --config \"\"" & configPath & "\"\" --port 4000", 0, False
```

> 💡 **Tip:** If `litellm` is not found, replace `litellm` in the script with the full path to the `litellm.exe` inside your Python virtual environment or Scripts folder (e.g., `%USERPROFILE%\AppData\Local\Programs\Python\Python311\Scripts\litellm.exe`).

**macOS:**
To run the proxy silently in the background, create a shell script:

```bash
# Create the startup script
cat > ~/start_litellm.sh << 'EOF'
#!/bin/bash
nohup litellm --config ~/.claude/litellm_config.yaml --port 4000 > /tmp/litellm.log 2>&1 &
echo "LiteLLM started. PID: $!"
EOF

# Make it executable
chmod +x ~/start_litellm.sh

# Run it
~/start_litellm.sh
```

---

### Stop the Server

**Windows:**
Create a batch script named `stop.bat` using the code below and run it to stop the server at any time:

```cmd
@echo off
echo Stopping LiteLLM Proxy Server...

REM Terminate litellm.exe process directly
taskkill /F /IM litellm.exe 2>nul

REM Terminate any process currently holding port 4000 open
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :4000 ^| findstr LISTENING') do (
    echo Terminating process PID %%a listening on port 4000...
    taskkill /F /PID %%a 2>nul
)

echo.
echo LiteLLM Server stopped successfully.
pause
```

**macOS:**
Create a shell script named `stop_litellm.sh` in your home directory to stop the server:

```bash
# Create the stop script
cat > ~/stop_litellm.sh << 'EOF'
#!/bin/bash
echo "Stopping LiteLLM Proxy Server..."

# Kill by process name
pkill -f "litellm" && echo "LiteLLM process terminated."

# Also free port 4000 if still held
lsof -ti:4000 | xargs kill -9 2>/dev/null && echo "Port 4000 freed."

echo "LiteLLM Server stopped."
EOF

# Make it executable
chmod +x ~/stop_litellm.sh
```

To stop the server, just run:
```bash
~/stop_litellm.sh
```

---

## Step 7: Run Claude Code!

Once the local proxy is running, open a new terminal window (CMD, PowerShell, or Terminal) and run:

```bash
claude
```

That's it! Claude Code will connect to your local LiteLLM proxy and authenticate using the free NVIDIA NIM models. 🎉

---

## 🔄 Model Switch & Selection Guide

You can switch between any of the configured NVIDIA NIM models inside your Claude Code session or select one when launching.

### 1. Interactive Model Selector
To view a list of **all available models** and select one interactively, simply run the `/model` command with no arguments inside your Claude Code session:
```bash
/model
```
Use the **arrow keys** to scroll through the full list of 63+ configured models, and press **Enter** to switch. This is the recommended way to browse all models.

### 2. Direct Model Switching
If you know the model ID, you can switch directly mid-session by typing:
```bash
/model <model-id>
```
*Example:*
```bash
/model meta/llama-3.1-70b-instruct
```

### 3. Launch with a Specific Model
You can start Claude Code with a specific model using the `--model` flag in your terminal:
```bash
claude --model <model-id>
```
*Example:*
```bash
claude --model nvidia/llama-3.1-nemotron-70b-instruct
```

---

## 🗂️ NVIDIA NIM Models Directory

Here is the complete directory of the **63 models** listed in the NVIDIA Models Guide, organized by series and capability.

<details>
<summary><b>📂 Click to expand NVIDIA NIM Models Directory (63 Models)</b></summary>

### 🦙 Meta Llama Series (General Purpose)
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `abacusai/dracarys-llama-3.1-70b-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model abacusai/dracarys-llama-3.1-70b-instruct` |
| `meta/llama-3.1-70b-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.1-70b-instruct` |
| `meta/llama-3.1-8b-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.1-8b-instruct` |
| `meta/llama-3.2-11b-vision-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.2-11b-vision-instruct` |
| `meta/llama-3.2-1b-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.2-1b-instruct` |
| `meta/llama-3.2-3b-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.2-3b-instruct` |
| `meta/llama-3.2-90b-vision-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.2-90b-vision-instruct` |
| `meta/llama-3.3-70b-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-3.3-70b-instruct` |
| `meta/llama-4-maverick-17b-128e-instruct` | Strong general-purpose reasoning, conversation, coding, and multilingual tasks. Extremely versatile industry standard. | `/model meta/llama-4-maverick-17b-128e-instruct` |

### 🤖 General Purpose Language Model
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `bytedance/seed-oss-36b-instruct` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model bytedance/seed-oss-36b-instruct` |
| `deepseek-ai/deepseek-v4-flash` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model deepseek-ai/deepseek-v4-flash` |
| `deepseek-ai/deepseek-v4-pro` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model deepseek-ai/deepseek-v4-pro` |
| `moonshotai/kimi-k2.6` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model moonshotai/kimi-k2.6` |
| `nvidia/ai-synthetic-video-detector` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model nvidia/ai-synthetic-video-detector` |
| `nvidia/gliner-pii` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model nvidia/gliner-pii` |
| `nvidia/ising-calibration-1-35b-a3b` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model nvidia/ising-calibration-1-35b-a3b` |
| `nvidia/riva-translate-4b-instruct-v1.1` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model nvidia/riva-translate-4b-instruct-v1.1` |
| `openai/gpt-oss-120b` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model openai/gpt-oss-120b` |
| `openai/gpt-oss-20b` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model openai/gpt-oss-20b` |
| `qwen/qwen3-next-80b-a3b-instruct` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model qwen/qwen3-next-80b-a3b-instruct` |
| `qwen/qwen3.5-122b-a10b` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model qwen/qwen3.5-122b-a10b` |
| `qwen/qwen3.5-397b-a17b` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model qwen/qwen3.5-397b-a17b` |
| `sarvamai/sarvam-m` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model sarvamai/sarvam-m` |
| `stepfun-ai/step-3.5-flash` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model stepfun-ai/step-3.5-flash` |
| `stepfun-ai/step-3.7-flash` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model stepfun-ai/step-3.7-flash` |
| `stockmark/stockmark-2-100b-instruct` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model stockmark/stockmark-2-100b-instruct` |
| `upstage/solar-10.7b-instruct` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model upstage/solar-10.7b-instruct` |
| `z-ai/glm-5.1` | General text generation, summarizing, classification, and standard chatbot interactions. | `/model z-ai/glm-5.1` |

### 💎 Google Gemma Series
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `google/diffusiongemma-26b-a4b-it` | Highly capable lightweight model family, strong at math, reasoning, and instruction-following. | `/model google/diffusiongemma-26b-a4b-it` |
| `google/gemma-2-2b-it` | Highly capable lightweight model family, strong at math, reasoning, and instruction-following. | `/model google/gemma-2-2b-it` |
| `google/gemma-3n-e2b-it` | Highly capable lightweight model family, strong at math, reasoning, and instruction-following. | `/model google/gemma-3n-e2b-it` |
| `google/gemma-3n-e4b-it` | Highly capable lightweight model family, strong at math, reasoning, and instruction-following. | `/model google/gemma-3n-e4b-it` |
| `google/gemma-4-31b-it` | Highly capable lightweight model family, strong at math, reasoning, and instruction-following. | `/model google/gemma-4-31b-it` |

### 🛡️ Safety & Moderation Guardrails
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `meta/llama-guard-4-12b` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model meta/llama-guard-4-12b` |
| `nvidia/llama-3.1-nemoguard-8b-content-safety` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model nvidia/llama-3.1-nemoguard-8b-content-safety` |
| `nvidia/llama-3.1-nemoguard-8b-topic-control` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model nvidia/llama-3.1-nemoguard-8b-topic-control` |
| `nvidia/llama-3.1-nemotron-safety-guard-8b-v3` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model nvidia/llama-3.1-nemotron-safety-guard-8b-v3` |
| `nvidia/nemotron-3-content-safety` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model nvidia/nemotron-3-content-safety` |
| `nvidia/nemotron-3.5-content-safety` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model nvidia/nemotron-3.5-content-safety` |
| `nvidia/nemotron-content-safety-reasoning-4b` | Content moderation, topic control, and safety filtering. Best used as a secondary check layer for inputs and outputs. | `/model nvidia/nemotron-content-safety-reasoning-4b` |

### ⚙️ Microsoft Phi Series
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `microsoft/phi-4-mini-instruct` | Small, highly efficient, and fast models that punch above their weight class in reasoning and logic. | `/model microsoft/phi-4-mini-instruct` |
| `microsoft/phi-4-multimodal-instruct` | Small, highly efficient, and fast models that punch above their weight class in reasoning and logic. | `/model microsoft/phi-4-multimodal-instruct` |

### ⚡ MiniMax Series
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `minimaxai/minimax-m2.7` | Highly responsive, low-latency conversational tasks and quick text generation. Great for snappy real-time interactions. | `/model minimaxai/minimax-m2.7` |
| `minimaxai/minimax-m3` | Highly responsive, low-latency conversational tasks and quick text generation. Great for snappy real-time interactions. | `/model minimaxai/minimax-m3` |

### 🌪️ Mistral AI Series
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `mistralai/ministral-14b-instruct-2512` | Excellent logic, reasoning, and multi-lingual processing. High-quality output and fast token generation. | `/model mistralai/ministral-14b-instruct-2512` |
| `mistralai/mistral-large-3-675b-instruct-2512` | Excellent logic, reasoning, and multi-lingual processing. High-quality output and fast token generation. | `/model mistralai/mistral-large-3-675b-instruct-2512` |
| `mistralai/mistral-medium-3.5-128b` | Excellent logic, reasoning, and multi-lingual processing. High-quality output and fast token generation. | `/model mistralai/mistral-medium-3.5-128b` |
| `mistralai/mistral-small-4-119b-2603` | Excellent logic, reasoning, and multi-lingual processing. High-quality output and fast token generation. | `/model mistralai/mistral-small-4-119b-2603` |
| `mistralai/mixtral-8x7b-instruct-v0.1` | Excellent logic, reasoning, and multi-lingual processing. High-quality output and fast token generation. | `/model mistralai/mixtral-8x7b-instruct-v0.1` |

### 🟢 NVIDIA Native Language Model
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `mistralai/mistral-nemotron` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model mistralai/mistral-nemotron` |
| `nvidia/llama-3.1-nemotron-nano-8b-v1` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/llama-3.1-nemotron-nano-8b-v1` |
| `nvidia/llama-3.1-nemotron-nano-vl-8b-v1` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/llama-3.1-nemotron-nano-vl-8b-v1` |
| `nvidia/llama-3.3-nemotron-super-49b-v1` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/llama-3.3-nemotron-super-49b-v1` |
| `nvidia/llama-3.3-nemotron-super-49b-v1.5` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/llama-3.3-nemotron-super-49b-v1.5` |
| `nvidia/nemotron-3-nano-30b-a3b` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-3-nano-30b-a3b` |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` |
| `nvidia/nemotron-3-super-120b-a12b` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-3-super-120b-a12b` |
| `nvidia/nemotron-3-ultra-550b-a55b` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-3-ultra-550b-a55b` |
| `nvidia/nemotron-mini-4b-instruct` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-mini-4b-instruct` |
| `nvidia/nemotron-nano-12b-v2-vl` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-nano-12b-v2-vl` |
| `nvidia/nemotron-parse` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nemotron-parse` |
| `nvidia/nvidia-nemotron-nano-9b-v2` | Highly optimized general-purpose dialogue, instruction following, and fast inference on NVIDIA GPU architectures. | `/model nvidia/nvidia-nemotron-nano-9b-v2` |

### 🔍 Embeddings & Retrieval (RAG)
| Model ID | Use Case | Switch Command |
| :--- | :--- | :--- |
| `nvidia/nemoretriever-parse` | Generating vector embeddings for semantic search, document retrieval, and Retrieval-Augmented Generation (RAG) pipelines. | `/model nvidia/nemoretriever-parse` |

</details>

---

## 👤 Author & Support

This guide is maintained by **[Nisarg Patel](https://github.com/nisargpatel1906)**.

⭐ **If this project helped you run Claude Code for free and saved you subscription costs, please consider giving it a Star on GitHub!** It helps other developers find this project and run Claude Code for free!

## ⚠️ Troubleshooting & Exceptions

This section covers every real-world failure you might hit, with exact commands to fix them.

---

### ❌ Exception 1 — `pip` or `pip3` not found (Windows & macOS)

**Cause:** Python was installed without being added to PATH, or pip is not available.

**Windows fix:**
```cmd
REM Try this first
py -m pip install litellm

REM If that fails, reinstall Python from https://www.python.org/downloads
REM IMPORTANT: Check "Add Python to PATH" during installation
```

**macOS fix:**
```bash
# Try using python3 directly
python3 -m pip install litellm

# Or upgrade pip first
python3 -m ensurepip --upgrade
python3 -m pip install litellm
```

---

### ❌ Exception 2 — `brew` not found after Homebrew install (macOS Apple Silicon M1/M2/M3)

**Cause:** On Apple Silicon Macs, Homebrew installs to `/opt/homebrew/` which is not in PATH by default.

**Fix:** Run this after the Homebrew installer finishes:
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```
Then verify:
```bash
brew --version
```

---

### ❌ Exception 3 — `npm install -g` permission error (Windows)

**Cause:** Running without administrator privileges.

**Fix:** Right-click on CMD or PowerShell → **"Run as Administrator"**, then run:
```cmd
npm install -g @anthropic-ai/claude-code
```

---

### ❌ Exception 4 — `winget` not found (Windows)

**Cause:** `winget` requires Windows 10 version 1709 or later with App Installer installed.

**Fix:** Install Node.js and Python manually instead:
- Node.js: https://nodejs.org/en/download
- Python: https://www.python.org/downloads

---

### ❌ Exception 5 — Port 4000 already in use

**Cause:** Another application is already using port 4000.

**Windows fix:**
```cmd
REM Find what is using port 4000
netstat -aon | findstr :4000

REM Kill it by PID (replace 1234 with the actual PID from above)
taskkill /F /PID 1234

REM Or run LiteLLM on a different port (then update settings.json accordingly)
litellm --config "%USERPROFILE%\.claude\litellm_config.yaml" --port 4001
```

**macOS fix:**
```bash
# Find what is using port 4000
lsof -i :4000

# Kill it by PID (replace 1234 with actual PID)
kill -9 1234

# Or run on a different port
litellm --config ~/.claude/litellm_config.yaml --port 4001
```

> **Note:** If you change the port, update `"ANTHROPIC_BASE_URL"` and `"endpoint"` in `settings.json` to match (e.g., `http://localhost:4001`).

---

### ❌ Exception 6 — Claude Code shows errors or agent breaks mid-task

**Cause:** The selected NVIDIA model does **not support tool/function calling**. Claude Code heavily relies on tool use to read files, run commands, and edit code. Models without tool support will fail.

**Fix:** Use one of these models which are confirmed to support tool calling:
```
meta/llama-3.1-70b-instruct
meta/llama-3.3-70b-instruct
meta/llama-3.1-8b-instruct
mistralai/mistral-large
nvidia/llama-3.1-nemotron-70b-instruct
```

In Claude Code, switch model with:
```bash
claude --model meta/llama-3.1-70b-instruct
```

---

### ❌ Exception 7 — "Request timed out" or rate limit errors

**Cause:** NVIDIA's free tier limits to approximately **40 requests per minute**. Heavy Claude Code sessions can hit this.

**Fix options:**
- Wait 60 seconds and retry
- Switch to a less-used model (smaller models have higher rate limits)
- Upgrade to NVIDIA NIM paid tier for no rate limits

---

### ❌ Exception 8 — `litellm` command not found after install (macOS)

**Cause:** pip3 installs litellm into a location not in your shell PATH.

**Fix:**
```bash
# Run directly via python3
python3 -m litellm --config ~/.claude/litellm_config.yaml --port 4000

# Or find where it was installed and add to PATH
python3 -c "import site; print(site.USER_BASE)"
# Add the /bin from the output above to your PATH in ~/.zshrc
```

---

### ❌ Exception 9 — `claude` command works but shows "model not found" error

**Cause:** The model name in `settings.json` does not match any model in `litellm_config.yaml`.

**Fix:** Make sure the `"model"` value in `settings.json` exactly matches a `model_name` entry in `litellm_config.yaml`. Example:

`settings.json`:
```json
"model": "meta/llama-3.1-70b-instruct"
```
`litellm_config.yaml` must have:
```yaml
- model_name: meta/llama-3.1-70b-instruct
```

---

### ❌ Exception 10 — LiteLLM starts but Claude Code cannot connect

**Cause:** LiteLLM is running but `ANTHROPIC_BASE_URL` in `settings.json` is wrong, or the proxy crashed silently.

**Fix:**
1. Verify the proxy is actually running — open a browser and go to `http://localhost:4000` — you should see a LiteLLM status page
2. Make sure `settings.json` has exactly:
   ```json
   "ANTHROPIC_BASE_URL": "http://localhost:4000"
   ```
3. Check LiteLLM logs in the terminal window where you started it for error messages

---

---

*Guide created and maintained by **[Nisarg Patel](https://github.com/nisargpatel1906)**. If you like this project, please add a ⭐ to show your support!*
