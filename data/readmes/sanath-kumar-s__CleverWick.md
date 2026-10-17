# Cleverwick

## 👋 Introduction
Hello! I am **Sanath K S**, the creator of Cleverwick. This project is the result of my journey to build a truly portable, offline, and private AI assistant that anyone can give proper and effecient results with utmost optmization.

---

## 🚀 About the Project
**Cleverwick** is a lightweight, self-contained Artificial Intelligence application designed to run entirely offline. Unlike ChatGPT or Gemini, which rely on massive server farms and internet connections, Cleverwick brings the power of Large Language Models (LLMs) directly to your local hardware.

The core philosophy is **Hyper-Portability**. You can install this entire system on a USB pen drive, plug it into any Windows computer, and start chatting with an AI immediately—no internet, no installations, and no data leaves your drive.

---

## ✨ Features
*   **100% Offline & Private**: Your data never leaves your device. Chat history and processing happen locally.
*   **Plug & Play Portability**: Designed to run directly from a USB drive without installing Node.js or Python on the host machine.
*   **Universal Compatibility**: Automatically adjusts to use available CPU threads for optimal performance on almost any modern laptop.
*   **Modern UI**: A beautiful, responsive interface built with Next.js 16 and Turbopack for a premium, fluid experience.
*   **Model Agnostic**: Supports widely available GGUF format models (like Qwen 2.5, Phi-3, Mistral).
*   **Persistent & Private Memory**: Local sessions and memory stores are saved automatically to your portable drive.

---

## 🛠️ Tech Stack
This project was built using a powerful combination of modern web frameworks and low-level system integrations:

*   **Frontend**: [Next.js 16](https://nextjs.org/) (React Framework) with **Turbopack** for blazing-fast development and performance.
*   **Desktop Shell**: [Electron 41](https://www.electronjs.org/) for a native desktop experience that manages the backend lifecycle.
*   **Backend**: [Node.js](https://nodejs.org/) & Express for handling API requests and system operations.
*   **AI Engine**: [Llama.cpp](https://github.com/ggerganov/llama.cpp) (via `llama-server`) for efficient CPU-based inference.
*   **Styling**: Vanilla CSS & Tailwind CSS with glassmorphic aesthetics.

---


## 📖 How to Use It (Step-by-Step)

### 📥 First Time Setup (If cloned from GitHub)
If you have just downloaded or cloned this repository, you must restore the ignored folder structure and dependencies first:

1.  **Launch `setup.bat`**: Double-click the file named **`setup.bat`**.
2.  **Wait**: This will recreate missing directories (`models`, `tmp`, etc.) and install the required Node.js libraries.
3. **Run `npm run dev:all`**: This will start the development server and the desktop application.
4. **Chat**: Your desktop application window will open automatically.

### 🚀 Running the App
1.  **Add a Brain**: Place your model file (ending in `.gguf`) inside the **`models/`** folder. 
2.  **Launch**: Double-click **`start_pocketnode.bat`**.
3.  **Chat**: Your desktop application window will open automatically.

---

## 📂 Project Structure
For the tech-savvy, here is how the magic is organized:

```bash
Cleverwick/
├── models/             # Where .gguf AI models live (Ignored by Git)
├── runtime/            # The llama.cpp executable engine
├── backend/            # Express server (The bridge between UI and AI)
├── electron/           # Desktop shell and main process logic
├── scripts/            # Setup, restoration, and dev maintenance scripts
├── .next/              # Compiled Frontend Application
├── setup.bat           # THE MAGIC SWITCH for restoration
├── start_pocketnode.bat # THE MAGIC SWITCH for launching
└── package.json        # Dependencies list
```

---

## 🔧 Troubleshooting
*   **"Workspace root inferred incorrectly"**: This is handled automatically by our `next.config.mjs` which explicitly sets the Turbopack root.
*   **Backend Unreachable**: Ensure no other process is using the local port. You can run `npm run reset` to clear stuck instances.
*   **Missing Libraries**: If binaries are missing, run **`setup.bat`** to verify your environment.

---

## ❤️ Credits
*   **Llama.cpp Team**: For making LLMs runnable on CPUs.
*   **Vercel**: For Next.js and the Turbopack engine.
*   **Open Source Community**: For the libraries that make offline-first AI possible.

---

## 👤 Creator
**Sanath K S**
*Developer, Designer, & AI Enthusiast*

---

## 📌 Version
**v1.1.0 (Portable & Reliable Edition)**  
*Build Date: March 2026*
