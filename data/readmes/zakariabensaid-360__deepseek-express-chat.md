# 💬 Express DeepSeek Chat

A fast, responsive web interface built with **Express.js**, **Tailwind CSS**, and **Ollama**. Chat locally with **DeepSeek-R1** on your machine with zero cloud API keys and complete privacy.

---

## 🚀 Features

- **100% Local Execution:** Runs entirely on your hardware via Ollama.
- **Lightweight Architecture:** Styled with Tailwind CSS CDN and powered by Node.js.
- **DeepSeek Integration:** Default support for `deepseek-r1:1.5b` (fast & lightweight).

---

## 🛠️ Setup Instructions

### 1. Download & Install Ollama

Ollama serves as the local background backend hosting the DeepSeek model weights.

1. Visit the official download portal:
   👉 **[https://ollama.com/download/](https://ollama.com/download/)**
2. Choose your operating system (**Windows**, **macOS**, or **Linux**) and run the installer.
3. Open your terminal and confirm the installation:
   ```bash
   ollama --version
   ```
4. Install the deepseek-r1:1.5b model
   ```bash
   ollama pull ollama run deepseek-r1:1.5b
   ```

5. Run the express app
   ```bash
   node main.js
   ```