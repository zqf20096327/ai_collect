# Vibe AI | Universal Chat Client

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Platform](https://img.shields.io/badge/platform-web-orange.svg)

**Vibe AI** is a sleek, lightning-fast, single-file web interface for interacting with any standard OpenAI-compatible API endpoint. Whether you are running local models via Ollama/LM Studio or connecting to premium cloud providers, Vibe AI offers a perfectly polished, zero-setup frontend.

No installation, no build steps, no node_modules—just open the file in your browser.

## ✨ Features

### 💬 Universal API Support
* **Bring Your Own API:** Connect seamlessly to any backend that supports standard `/models` and `/chat/completions` endpoints.
* **Dynamic Model Fetching:** Click to fetch and cache all available models directly from your chosen provider.
* **System Prompts:** Full support for custom system instructions to shape the AI's behavior and personality.
* **Multimodal Vision:** Attach images (via URL or local File Upload) to chat with vision-capable models.

### 🛠️ Advanced Message Controls
* **Message Actions Toolbar:** Hover over (or tap on mobile) any message to reveal instant quick-actions.
* **Inline Editing:** Edit both user prompts and AI responses directly inside the chat bubble. Supports full Markdown re-rendering.
* **Regenerate & Retry:** Instantly regenerate an AI's response or resubmit a past prompt with a single click.
* **Copy & Delete:** Copy raw text/markdown instantly, or delete specific messages from the history context.

### ⚡ Peak Performance & Reliability
* **Single Source of Truth Architecture:** Built on a flawlessly synchronized state engine. History strictly tracks the visible UI, eliminating race conditions or duplicate contexts, even when modifying history during an active AI generation.
* **Cancellable Requests:** Instantly abort in-flight generations. Zero race conditions, zero UI locks, and no memory leaks.
* **Bulletproof State:** Your settings, selected models, and chat history are saved securely to your browser's LocalStorage with complete corruption-resistance.
* **Markdown Support:** Full support for GitHub Flavored Markdown (GFM), intelligent line breaks, code syntax highlighting, tables, and formatted text.

### 🎨 Beautiful UI / UX
* **Standalone Architecture:** The entire application runs perfectly from one isolated `index.html` file.
* **Responsive & Mobile Optimized:** A beautifully optimized, flexbox-driven layout. Mobile features a custom tap-to-activate logic to prevent accidental button clicks on touch screens.
* **Dynamic Dark/Light Mode:** Automatic theme detection based on your OS preference, complete with a manual override toggle and high-contrast element mapping.
* **Auto-Resizing Input:** The chat box scales comfortably as you type long, multi-line prompts.

## 🚀 Getting Started

### Prerequisites
* A modern web browser (Chrome, Firefox, Safari, Edge).
* An active API endpoint (e.g., OpenAI, Ollama, LM Studio, Groq, Anthropic via proxy, etc.).

### Installation & Usage
1.  **Download** the `index.html` file from this repository.
2.  **Open** the file in your browser (or host it locally via a simple HTTP server).
3.  Open the **Sidebar** (`☰`) and configure your connection:
    * **API Base URL:** Enter your endpoint (e.g., `http://localhost:11434/v1` or `https://api.openai.com/v1`).
    * **API Key:** Enter your key (if your provider requires authentication).
4. Click **Models** to populate the dropdown.
5. Select your model and start chatting!

## 🧩 Technologies Used

* **Core:** HTML5, CSS3, Vanilla JavaScript.
* **Network:** [Axios](https://axios-http.com/) for rock-solid HTTP requests and request cancellation.
* **Formatting:** [Marked.js](https://marked.js.org/) for beautiful Markdown rendering.
* **Icons:** [FontAwesome](https://fontawesome.com/).

## ⚠️ Disclaimer

* All data, chat history, and API keys are stored exclusively and securely in your browser's **Local Storage**. 
* Clearing your browser cache or site data will wipe your chat history and settings. No data is ever sent to third parties except the API provider you explicitly configure.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
