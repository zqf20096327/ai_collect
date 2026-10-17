<div align="center">
    
![Logo Animation](https://github.com/user-attachments/assets/3f5eb226-87b2-4313-a315-ed1b73064889)

</div>

<div align="center">
    <a href="https://chromewebstore.google.com/detail/chat-box-chat-with-all-ai/hhaaoibkigonnoedcocnkehipecgdodm" target="_blank">
       <img src="https://img.shields.io/badge/Chrome%20Web%20Store-Sen%20Chat-red?style=for-the-badge&logo=chromewebstore&logoColor=white" alt="Chrome Web Store" />
    </a>
    <a href="https://addons.mozilla.org/en-US/firefox/addon/chat-box-chat-with-all-ai/"
    target="_blank">
        <img src="https://img.shields.io/badge/Firefox%20ADD%20ONS-Sen%20Chat-red?style=for-the-badge&logo=firefoxbrowser&logoColor=red" alt="Firefox ADD-ONS" />
    </a>
    <a href="https://github.com/MinhxThanh/Chat-Box" target="_blank">
       <img src="https://img.shields.io/badge/GitHub-Sen%20Chat-black?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
    </a>
    <a href="https://www.senchatai.com/">
       <img src="https://img.shields.io/badge/Web-SenChatAI.Com-purple?style=for-the-badge&logo=w404&logoColor=white" alt="W404" />
    </a>
    
</div>
<div align="center">
<a href="https://www.buymeacoffee.com/mr.thanh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
</div>

---

<div align="center">
  <img width="1095" alt="Sen Chat Description Image" src="https://github.com/user-attachments/assets/2cd01baf-ba5c-46c9-995a-323fdc7bd2fb" />

https://github.com/user-attachments/assets/4eb39d5b-a145-4c99-ae13-408c431933ce
</div>

***Sen Chat*** is a browser extension that streamlines your online experience by integrating AI chat, advanced web search, document interaction, and more into a convenient sidebar.

## What's New In V0.8.3
- **✏️ Renamed Extension**: Change name from ChatBox to Sen Chat.
- **🔍 Tab Popup Search**: Add Tab popup search for quicker access and queries.
- **💬 Improved Chat Messages**: Improve chat message display for better readability and context.
- **🧹 UX Cleanup**: Remove code that copies text to clipboard when hover displays quick actions.
- **🔧 Bug Fixes**: Fixed some other issues and improved overall stability.

## Key Features

Sen Chat offers a rich set of functionalities to streamline your AI interactions and information gathering:

-   **🌙 Modern Dark UI**: Sleek and intuitive interface built with Shadcn UI and Tailwind CSS.
-   **⚡️ Quick Access Shortcut**: Open/close the sidebar instantly with `Cmd/Ctrl + E` (improved toggle functionality).
-   **💬 AI Chat**: Engage in conversations with various AI models directly from the sidebar.
-   **📝 Contextual Text Selection**: Highlight text on any website to use it as context in your chat.
- **💬 Floating Chat Window**: Draggable quick-chat 
overlay with selected-text preview, model picker, 
live streaming with stop, Ctrl/Command + M.
-   **🔧 Enhanced Quick Actions**: Select any text to reveal improved quick action buttons for:
    -   **📊 Summarize**: Get concise summaries of lengthy content
    -   **💡 Explain**: Understand complex concepts in simple terms  
    -   **🌍 Translate**: Translate text to any language
    -   **✍️ Rewrite**: Improve text clarity and engagement
    -   **📝 Fix Grammar**: Automatically correct grammar, spelling, and punctuation in any language
-   **✨ Custom Prompts**: Create and save your own custom prompts for quick reuse.
-   **📚 Improved Chat History**: Easily access and manage multiple past conversations with improved reliability.
-   **🎨 Custom Theme Colors**: Personalize Sen Chat with custom color themes for primary, background, and message colors.
-   **⚙️ Flexible API Configuration & Refreshed UI**:
    -   Configure API keys and endpoints for various AI providers in a more intuitive settings panel.
    -   Supports major providers like **OpenAI, DeepSeek, Claude (Anthropic), Cerebras, OpenRouter**, as well as **Local LLMs (via Ollama)** and **Custom OpenAI-compatible endpoints**.
    -   Load and select from available AI models from your configured provider.
-   **🚀 Advanced Web Search & Scraping**:
    -   Integrates with **Firecrawl** and **Jina AI** for superior web search results.
    -   Requires configuring your Firecrawl or Jina API key in settings for these features.
    -   Defaults to **DuckDuckGo** for web searches if Firecrawl/Jina are not configured.
    -   Leverage AI (including **Local LLMs**) to refine search queries or process search results for enhanced information gathering.
    -   Scrape and summarize content directly from URLs to use as context in your chat.
-   **📄 Document Chat Powerhouse**:
    -   Upload and interact with various document types including PDF, DOCX, TXT, HTML, CSS, JS, MD, and JSON.
    -   Utilizes semantic chunking to handle large documents effectively.
    -   View document context (name, size, estimated tokens) directly in the chat interface.
-   **🖼️ Multimedia & Contextual Awareness**:
    -   Upload images to include in your conversations with AI models that support vision.
    -   **📺 Enhanced YouTube Integration**: Get summaries, ask questions, and interact with YouTube videos more effectively.
-   **🔒 Secure Local Storage**: Your API credentials and conversations are stored securely in your browser's local storage.

## Installation

### Development Mode

1.  Clone this repository:
    ```bash
    git clone https://github.com/MinhxThanh/Chat-Box.git
    cd Chat-Box
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Build the extension:
    ```bash
    npm run build
    ```
4.  Load the extension in Chrome:
    -   Open Chrome and navigate to `chrome://extensions/`.
    -   Enable "Developer mode" in the top-right corner.
    -   Click "Load unpacked" and select the `dist` directory from this project.

### Firefox (Temporary Install)

1. Build the Firefox bundle:
   ```bash
   npm run build:firefox
   ```
2. Open Firefox and navigate to `about:debugging#/runtime/this-firefox`.
3. Click "Load Temporary Add-on…".
4. Select `dist-firefox/manifest.json`.

Note: Temporary add-ons are removed when Firefox restarts. Re-load via `about:debugging` when needed.

## Usage

1.  Pin the extension icon to your browser toolbar for easy access.
2.  Click the extension icon in your browser toolbar to open the chat sidebar.
3.  Use the right navigation panel to access different features:
    -   💬 **Chat**: Return to the main chat interface.
    -   📚 **History**: Access your previous conversations.
    -   ➕ **New Chat**: Start a fresh conversation.
    -   ⚙️ **Settings**: Configure API keys and preferences.
4.  In **Settings**, configure your APIs:
    -   **AI Provider**:
        -   Enter your AI provider API key.
        -   Specify the base API endpoint (e.g., `https://api.openai.com/v1`).
        -   Click "Load Models" to fetch and select your desired AI model.
    -   **Custom Search Engine (Optional but Recommended)**:
        -   Choose between Firecrawl, Jina, or Default.
        -   Enter the API key for your selected search engine (Firecrawl or Jina) to enable advanced web search and URL scraping features.
4.  Start chatting with the AI, searching the web, or interacting with your documents!

### Using with Local LLMs (e.g., Ollama)

You can configure Sen Chat to work with local LLMs like those served by [Ollama](https://ollama.com/).

1.  **Run your Ollama server**:
    Open your terminal and run the following command. This makes Ollama accessible to the extension.
    ```bash
    OLLAMA_HOST=0.0.0.0 OLLAMA_PORT=11434 OLLAMA_ORIGINS='*' ollama serve
    ```
    *   `OLLAMA_HOST=0.0.0.0`: Allows connections from any network interface.
    *   `OLLAMA_PORT=11434`: Standard Ollama port.
    *   `OLLAMA_ORIGINS='*'`: Allows requests from any origin, necessary for the Chrome extension to connect.

2.  **Configure Sen Chat Settings**:
    -   Go to the Sen Chat **Settings** panel.
    -   For **Endpoint**, enter: `http://localhost:11434/v1`
    -   For **API Key**, enter: `no-key` (Ollama's OpenAI-compatible endpoint doesn't strictly require a key, but the field might be mandatory in the UI. Any non-empty string should work).
    -   Click "Load Models" to see models available from your Ollama instance.


## Demo
<div align="center">

### Tab popup Search
https://github.com/user-attachments/assets/2e2a8a1c-c91a-4d9a-a09f-3ed46a066f8b

### Floating Chat
https://github.com/user-attachments/assets/9cafb6e5-4278-4ea0-9e5a-d547c2a2ee9c

<img width="1280" height="800" alt="AI Chat 1280x800" src="https://github.com/user-attachments/assets/0482d0fe-8abf-4bfc-b597-f8be906ffb4f" />

</div>

## Technologies Used

-   **Core Framework**: React
-   **Bundler & Compiler**: Webpack, Babel
-   **UI & Styling**: Tailwind CSS, Shadcn UI, Radix UI, Lucide React
-   **Browser Extension**: Chrome Extension APIs (Manifest V3)
-   **Local Database**: Dexie (IndexedDB)
-   **AI**: OpenAI-compatible REST plus provider SDKs (OpenAI, Anthropic/Claude, Cerebras); local LLMs via Ollama.


## License

This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details.
