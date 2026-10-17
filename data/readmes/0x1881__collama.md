# Collama - Run Ollama Models on Google Colab

<p align="center">
  <a href="README-tr.md">
    <img src="https://img.shields.io/badge/README-Türkçe-red?style=for-the-badge" alt="Türkçe README"/>
  </a>
</p>

Collama is a minimal and practical setup to run Ollama models directly on Google Colab.

It is designed for developers who don’t have a local GPU or want to quickly test LLMs without complex setup.

---

## Features

- One-click Ollama setup on Colab  
- Run models like Llama, Qwen, Deepseek, CodeLlama  
- LangChain integration (prompt → response pipeline)  
- Minimal setup, maximum speed  

---

## Who Is This For?

- Developers without a local GPU  
- People who want fast prototyping  
- Anyone experimenting with LLMs  
- Builders working on agents or automation  

---

## What Can You Do?

- Test coding LLMs  
- Experiment with prompt engineering  
- Build simple AI tools  
- Create LangChain + Ollama workflows  

---

## Quick Start

### Open and run in Colab:

https://colab.research.google.com/github/0x1881/collama/blob/main/Ollama_Setup.ipynb

### Run with external access using Cloudflare Tunnel:
Requirements:
- A Cloudflare account
- A domain connected to Cloudflare

Steps:
- Go to the Cloudflare Zero Trust panel: https://one.dash.cloudflare.com/
- Navigate to Networks > Connectors > Create a tunnel > Cloudflared
- Give your tunnel a name
- Select your device’s operating system (Debian)
- At the bottom, copy the token from the command:
- cloudflared tunnel run --token ***
- Add this token to Colab Secrets with the name CLOUDFLARE_TOKEN

Notebook:
https://colab.research.google.com/github/0x1881/collama/blob/main/Ollama_Setup_with_Cloudflare_Tunnel.ipynb

---

## Limitations

- Colab sessions are ephemeral (restart resets everything)  
- GPU usage is limited  
- Large models may not fit in memory  

---

## Contributing

This repository is open to contributions.

If your notebook uses Ollama to solve a real use-case that can help others learn something, feel free to open a pull request.

---

## Note

This repository is not intended for production use.  
It is designed as a quick test and playground environment.

## Acknowledgements

This project was inspired by https://github.com/5aharsh/collama.  
Thanks to the author for the initial work and concept.
