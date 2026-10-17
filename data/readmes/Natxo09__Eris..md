# Eris. 🪐

<div align="center">
  <img src="Eris./Assets.xcassets/AppIconNoBg.imageset/ChatGPT Image 19 jun 2025, 09_16_02.png" width="128" height="128" alt="Eris Icon">
  
  **Chat with AI privately on your iPhone and iPad**
  
  [![Platform](https://img.shields.io/badge/platform-iOS%20%7C%20iPadOS-blue.svg)](https://developer.apple.com/xcode/)
  [![Swift](https://img.shields.io/badge/Swift-5.9+-orange.svg)](https://swift.org/)
  [![MLX](https://img.shields.io/badge/MLX-Apple%20Silicon-green.svg)](https://github.com/ml-explore/mlx)
</div>

## About

Eris is a private AI chat application that runs entirely on your device using Apple's MLX framework. Named after the dwarf planet that challenged our understanding of the solar system, Eris challenges the notion that AI must live in the cloud.

### Key Features

- 🔒 **100% Private** - All conversations stay on your device
- 🚀 **Blazing Fast** - Powered by Apple Silicon and MLX
- 📡 **Offline First** - Works without internet connection
- 🤖 **Multiple Models** - Support for Llama, Qwen, DeepSeek, and more
- 🎨 **Native Design** - Built with SwiftUI for a seamless Apple experience
- 💾 **Local Storage** - Your data never leaves your device
- 🎯 **Syntax Highlighting** - Beautiful code blocks with syntax highlighting for 100+ languages
- 📝 **Markdown Support** - Full markdown rendering for formatted text, lists, tables, and more
- 🌑 **Dark Mode** - Easy on your eyes, day or night
- ☀️ **Light Mode** - Clean and bright interface for daytime use

## Requirements

### For Users
- iPhone with A13 Bionic chip or newer with 6GB+ RAM (iPhone 11 Pro/Pro Max, SE 2nd gen, 12 series and later)
- iPad with M1 chip or newer (iPad Pro/Air with M1, M2, or M4)
- iOS 17.6+ / iPadOS 17.6+
- ~2-8GB free storage per model

### Compatible Devices
✅ **iPhone**: 11 Pro, 11 Pro Max, SE (2nd gen), 12 series, 13 series, 14 series, 15 series, 16 series  
❌ **Not Compatible**: iPhone 11 (base model), iPhone X, XS, XS Max, XR, and older models

### For Developers
- Apple Silicon Mac (M1, M2, M3, M4)
- macOS 14.0+
- Xcode 15.0+
- Physical iPhone/iPad for testing (see note below)

⚠️ **Important Development Note**: iOS Simulators are not supported as MLX requires actual hardware acceleration with Metal 3 support. You'll need a physical iPhone or iPad with A13 chip or newer for testing and debugging.

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/Natxo09/Eris.git
cd Eris.
```

2. Open in Xcode:
```bash
open Eris..xcodeproj
```

3. Select your target device and build (⌘+B)

4. Run the app (⌘+R)

## Supported Models

Eris supports a variety of quantized models optimized for Apple Silicon:

### General Purpose
- **Llama 3.2** (1B, 3B) - Meta's latest efficient models
- **Qwen 2.5** (0.5B, 1.5B, 3B) - Alibaba's multilingual models
- **Gemma 2** (2B) - Google's lightweight model
- **Phi 3.5 Mini** - Microsoft's small but capable model

### Reasoning
- **DeepSeek-R1-Distill-Qwen** (1.5B in 4bit/8bit) - Advanced reasoning capabilities

## Usage

1. **First Launch**: The app will guide you through downloading your first model
2. **Chat**: Start conversations with your AI assistant
3. **Switch Models**: Access different models from Settings → Model Management
4. **Manage Data**: Delete chats or models from Settings → Danger Zone
5. **Use Shortcuts**: Integrate Eris with Apple Shortcuts for quick AI tasks

## Privacy & Security

- ✅ No telemetry or analytics
- ✅ No network requests except for model downloads
- ✅ All data stored locally using SwiftData
- ✅ Models downloaded from Hugging Face are cached locally
- ✅ Full data deletion available in settings

## Technical Details

### Architecture
- **UI**: SwiftUI
- **ML Framework**: MLX / MLX Swift
- **Data Persistence**: SwiftData
- **Model Format**: Quantized models (4-bit/8-bit)

### Project Structure
```
Eris./
├── Models/          # Data models and ML integration
├── Views/           # SwiftUI views
│   ├── Chat/        # Chat interface
│   ├── Settings/    # Settings and management
│   └── Onboarding/  # First-run experience
├── Utils/           # Utilities and helpers
└── Intents/         # Shortcuts integration
```

## Shortcuts Integration

Eris includes powerful Shortcuts integration that allows you to use AI capabilities throughout iOS without opening the app. Perfect for quick tasks, automation, and integrating AI into your workflows.

### Available Shortcuts

#### 1. Quick Chat
Start a conversation with Eris directly from Shortcuts.

**Parameters:**
- **Message** (required): Your question or prompt
- **Continue Conversation**: Keep the conversation going after each response
- **Response Style**: Choose how Eris responds
  - Normal: Standard helpful responses
  - Concise: Brief and to the point
  - Detailed: Comprehensive answers with examples
  - Creative: Imaginative and creative responses
  - Professional: Formal business tone
- **Save Chat**: Save the conversation in the app (default: off)
- **Model Name**: Type a model name like "Llama", "Qwen", "Gemma" (optional)

**Example Uses:**
- "Hey Siri, ask Eris about quantum computing"
- Quick questions while working
- Integration with other shortcuts

#### 2. Summarize Text
Get quick summaries of any text.

**Parameters:**
- **Text to Summarize** (required): The content you want summarized
- **Summary Length**: 
  - Brief: 1-2 sentences
  - Medium: 1 paragraph
  - Detailed: Multiple paragraphs
- **Save Chat**: Save the summary in the app (default: off)
- **Model Name**: Choose a specific model (optional)

**Example Uses:**
- Summarize articles from Safari
- Condense meeting notes
- Quick overview of long emails

#### 3. Translate Text
Translate between 12+ languages using on-device AI.

**Parameters:**
- **Text to Translate** (required): The content to translate
- **Target Language**: Language to translate to (default: Spanish)
- **Source Language**: Language to translate from (default: Auto-detect)
- **Save Chat**: Save the translation (default: off)
- **Model Name**: Choose a specific model (optional)

**Supported Languages:**
English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, Russian, Hindi

**Example Uses:**
- "Hey Siri, translate this to Spanish with Eris"
- Translate clipboard content
- Multi-language communication

#### 4. Generate Text
Create various types of content with AI assistance.

**Parameters:**
- **Type of Text**: What to generate
  - Email
  - Message
  - Social Media Post
  - Paragraph
  - List
  - Creative Ideas
- **Topic or Context** (required): What the text should be about
- **Tone**: Writing style
  - Professional
  - Casual
  - Friendly
  - Formal
  - Humorous
  - Neutral
- **Save Chat**: Save the generated text (default: off)
- **Model Name**: Choose a specific model (optional)

**Example Uses:**
- Generate email drafts
- Create social media content
- Brainstorm ideas
- Write quick messages

### Setting Up Shortcuts

1. **Install Eris** and download at least one AI model
2. **Open Shortcuts app** on your iPhone/iPad
3. **Search for "Eris"** in the Gallery or when adding actions
4. **Add shortcuts** to your collection
5. **Customize** parameters as needed
6. **Add to Siri** for voice activation

### Advanced Tips

#### Model Selection
- Leave the model field empty to use your default model
- Type partial names: "llama" finds all Llama models
- Model names are case-insensitive
- Only downloaded models can be used

#### Performance Optimization
- The first shortcut run loads the model (slower)
- Subsequent runs are much faster (model stays in memory)
- For best performance, use smaller models (0.5B-1.5B)

#### Automation Ideas
1. **Morning Briefing**: Summarize news articles automatically
2. **Email Assistant**: Generate professional responses
3. **Language Learning**: Translate and save phrases
4. **Content Creation**: Generate daily social media posts
5. **Research Helper**: Quick explanations of complex topics

#### Combining with Other Apps
- Use with **Safari**: Summarize web pages
- Use with **Notes**: Generate content directly
- Use with **Mail**: Draft responses
- Use with **Messages**: Translate conversations
- Use with **Clipboard**: Process copied text

### Troubleshooting

**"No model selected" error**
- Open Eris and download a model first
- Make sure a default model is selected in Settings

**"Model not found" error**
- Check the model name spelling
- Ensure the model is downloaded
- Try using partial names (e.g., "qwen" instead of full name)

**Shortcuts run slowly**
- First run is always slower (model loading)
- Use smaller models for better performance
- Close other apps to free memory

**Chat not saving**
- Enable "Save Chat" parameter
- Check storage space
- Ensure Eris has necessary permissions

## Roadmap

View our roadmap and progress at [eris.natxo.dev/roadmap](https://eris.natxo.dev/roadmap)

### Bug Fixes
- [x] Chat name only applies after exiting and re-entering the chat
- [x] Improve Markdown formatting for AI responses
- [ ] Model testing across devices (continue testing all AI models on different devices and platforms for optimal performance)

### Upcoming Features
- [x] Shortcuts integration (Apple Shortcuts for automation and quick actions)
- [ ] Voice input/dictation support (OpenAI Whisper or similar)
- [ ] Image support in conversations
- [ ] Native macOS app (not iPad port)

## Community

Join our Discord community for support, discussions, and updates: [https://discord.gg/nr2qpfzCsd](https://discord.gg/nr2qpfzCsd)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

This project was inspired by [Fullmoon iOS](https://github.com/mainframecomputer/fullmoon-ios) and wouldn't be possible without:

- Apple's [MLX](https://github.com/ml-explore/mlx) framework
- The [Hugging Face](https://huggingface.co) community
- All the open-source model creators

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

Created by Ignacio Palacio - [natxo.dev](https://natxo.dev)

---

### A Note About the Commit History 😴

If you're browsing through the commit history and wondering why there are so many commits that just say "commit"... well, I have a confession to make. 

I started this project late one night with zero intention of it becoming anything serious. It was supposed to be a quick experiment, maybe a few lines of code to test out MLX. But you know how it goes - "just one more feature" turned into "oh, this actually works!" which turned into "wait, people might actually use this."

So there I was, half-asleep, committing code with the eloquence of a zombie: "commit", "commit", "commit". By the time I realized this was becoming a real project, the damage was done. My git history looks like I fell asleep on the keyboard with my finger on the enter key.

I promise I'm usually better at commit messages. Usually. When I'm awake. ☕

*PS: If you're a hiring manager reading this, I swear this isn't representative of my professional work. Please check out my other repos where I actually wrote meaningful commit messages like "fix: resolved null pointer exception in user authentication flow" instead of just "commit" 47 times in a row.*