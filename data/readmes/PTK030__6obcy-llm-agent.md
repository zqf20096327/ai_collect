<img width="2521" height="1540" alt="cligoal" src="https://github.com/user-attachments/assets/1d2fa165-c1e7-4420-ac15-2c6c825c984d" />
<div align="center">
  <h1>6obcy.org LLM Agent</h1>
  <p><strong>Fully Autonomous AI Agent for 6obcy.org with Selenium & LLMs</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python 3.12+" />
    <img src="https://img.shields.io/badge/Docker-Supported-2496ED?logo=docker" alt="Docker" />
    <img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium" alt="Selenium" />
    <img src="https://img.shields.io/badge/API-OpenRouter-FF5A5F.svg" alt="OpenRouter" />
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License MIT" />
  </p>
</div>

<hr />

## 📖 Overview

**6obcy LLM Agent** is an advanced, multi-threaded automation tool that brings Large Language Models (LLMs) to the popular Polish anonymous chat platform [6obcy.org](https://6obcy.org). 

Built with a **Modular Event-Driven Architecture**, the **Page Object Model (POM)** pattern, and **Selenium WebDriver**, this bot operates independently. It can search for strangers, automatically solve image CAPTCHAs using Vision AI, and conduct highly realistic conversations based on customizable personas.

> **Disclaimer:** This project was created for educational purposes, AI research, and to demonstrate web automation capabilities. Use it responsibly.

---

## ✨ Key Features

- 🧠 **Smart AI Autopilot**: Give the bot a persona (e.g., *"19-year old student from Warsaw"*) and a goal (e.g., *"Get their Instagram"*) and let it chat automatically.
- 👁️ **Automated CAPTCHA Solving**: Uses advanced Vision LLMs (via OpenRouter) to read and bypass 6obcy's image CAPTCHAs automatically.
- ⌨️ **Human-like Typing Simulation**: Configurable typing speed and simulated human errors to avoid detection.
- 🖥️ **Premium Terminal UI (TUI)**: Beautiful, interactive CLI built with `prompt_toolkit`. Features real-time logs, keyboard shortcuts, and a command bar.
- 🐳 **Docker Ready**: Run it isolated in a container with a virtual `Xvfb` display (Headless).
- ⚙️ **Hot-Swappable Configs**: Change the AI model, API keys, persona, or typing speed directly via chat commands without restarting the bot.

---

## 🚀 Installation & Usage

### Option 1: Using Docker (Recommended)
Docker provides a clean environment and runs Chrome headlessly using a virtual display (`Xvfb`), keeping your host machine completely free of browser windows popping up.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/6obcy-bot.git
   cd 6obcy-bot
   ```
2. **Add your OpenRouter API Key:**
   Create a `.env` file in the root directory:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```
3. **Run using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

### Option 2: Local Python Environment
If you want to watch the Chrome browser physically open and navigate the site, you can run the bot locally.

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up API Key:**
   You can either create a `.env` file or provide it directly in the Terminal when prompted.
3. **Run the bot:**
   ```bash
   python run.py
   ```

---

## ⚙️ Configuration & Commands

You can control the bot dynamically while it's running by typing commands starting with `/` in the terminal prompt.

### ⌨️ Keyboard Shortcuts
- `F2` : Disconnect and search for a new stranger immediately.
- `F4` : Toggle CAPTCHA mode (`manual` -> `semi-auto` -> `auto`).
- `F5` : Toggle AI Autopilot on/off.
- `F8` : Toggle Headless mode (hides/shows the Chrome browser).
- `Esc`: Gracefully quit the application.

### 💬 Chat Commands
| Command | Description |
|---|---|
| `/help` | Displays the help menu with all commands. |
| `/next` or `/n` | Skips the current stranger. |
| `/stop` or `/s` | Disconnects and stops searching. |
| `/start` or `/go` | Resumes searching for strangers. |
| `/persona <text>` | Changes the AI's personality dynamically. |
| `/goal <text>`| Changes the ultimate goal of the AI conversation. |
| `/model <name>` | Swaps the LLM model (e.g. `google/gemini-2.5-flash`). |
| `/key <key>` | Updates the OpenRouter API Key. |
| `/manual` | Disables AI. From now on, your typed messages are sent directly. |
| `/save <name>` | Saves the current conversation history to a Markdown file. |

All settings are automatically saved to `config.json` and persist across restarts.

---

## 🏗️ Architecture

This project is built using robust Software Engineering architectural patterns:
- **Modular & Event-Driven**: Logic is strictly separated into distinct layers: Application State (`state.py`), Browser Automation worker (`worker.py`), Event Dispatching (`events_handler.py`), and User Interface (`tui.py`).
- **Page Object Model (POM)**: Selenium interactions are encapsulated in `chat_page.py`, inheriting robust explicit waits from `base_page.py`.
- **Thread-safe Queues**: The blocking Selenium WebDriver runs in a daemon thread, communicating with the async Prompt Toolkit TUI via `queue.Queue`.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details. 
*Note: This project is not affiliated with, endorsed by, or sponsored by 6obcy.org.*
