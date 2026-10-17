# ollama-colab

> Run Ollama LLMs on Google Colab's free GPU — exposed as a public API endpoint via Ngrok.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amin-tehrani/ollama-colab/blob/main/ollama-server.ipynb)
[![Stars](https://img.shields.io/github/stars/amin-tehrani/ollama-colab?style=flat-square)](https://github.com/amin-tehrani/ollama-colab/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## Why this exists

Running LLMs locally requires hardware most people don't have. Paying for OpenAI, Anthropic, or Llama API adds up fast. Google Colab offers free T4/A100 GPUs sitting idle. This notebook bridges the gap: spin up Ollama on Colab and expose it as a standard REST API endpoint you can hit from anywhere — your laptop, a LangChain app, a Python script, anything.

---

## How it works

```
Google Colab (free GPU)
  └─ Ollama server  (:11434)
       └─ Ngrok tunnel  ──►  https://xxxx.ngrok-free.app  (public endpoint)
```

Ollama's API is [OpenAI-compatible](https://ollama.com/blog/openai-compatibility), so any client that speaks OpenAI can point at this endpoint with zero changes.

---

## Prerequisites

1. **Google account** — to run Colab notebooks
2. **Ngrok account** — free tier is enough. Get your auth token at [dashboard.ngrok.com](https://dashboard.ngrok.com/get-started/your-authtoken)

---

## Usage

### 1. Open the notebook in Colab

Click the badge above, or open [`ollama-server.ipynb`](ollama-server.ipynb) directly in Google Colab.

### 2. Set your Ngrok auth token

In the notebook, find this cell and replace the placeholder:

```bash
!./ngrok authtoken <NGROK_AUTH_TOKEN>
```

### 3. Run all cells

The final cell starts the Ollama server, pulls `llama3`, and opens a Ngrok tunnel on port `11434`.

### 4. Get your endpoint

Find your public URL in the cell output or at [dashboard.ngrok.com/cloud-edge](https://dashboard.ngrok.com/cloud-edge):

```
https://xxxx.ngrok-free.app
```

---

## Using the endpoint

### curl

```bash
curl https://xxxx.ngrok-free.app/api/generate \
  -d '{"model": "llama3", "prompt": "Hello!", "stream": false}'
```

### LangChain

```python
from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(
    base_url="https://xxxx.ngrok-free.app",
    model="llama3"
)
print(llm.invoke("What is the capital of France?"))
```

### OpenAI-compatible client

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://xxxx.ngrok-free.app/v1",
    api_key="ollama"  # any non-empty string
)
response = client.chat.completions.create(
    model="llama3",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

---

## Changing the model

Edit the final cell — replace `llama3` with any model from [ollama.com/library](https://ollama.com/library):

```bash
ollama serve & ./ngrok http 11434 --host-header="localhost:11434" --log stdout & sleep 5s && ollama run mistral
```

Popular choices: `llama3`, `mistral`, `gemma2`, `phi3`, `codellama`, `deepseek-coder`

---

## Limitations

- Colab free sessions time out after ~12 hours of inactivity
- Free Ngrok gives one public URL per session (resets on restart)
- Model weights are re-downloaded each session unless you mount Google Drive

---

## License

MIT © Amin Tehrani
