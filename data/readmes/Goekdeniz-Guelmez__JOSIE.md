<p align="center">
  <img src="docs/logo.png" alt="Josie logo" width="160">
</p>

<h1 align="center">JOSIE</h1>

<p align="center">
  <b>Your Mac. With a voice.</b><br>
  A voice and chat assistant that listens, knows who's speaking, talks back with a natural voice, and takes real action in your Reminders, Calendar, Maps and Messages.<br>
  Hearing, voice recognition and speech all run on your Mac, so your voice never leaves it.
</p>

<p align="center">
  <a href="https://goekdeniz-guelmez.github.io/JOSIE/"><b>Website</b></a> ·
  <a href="https://x.com/ActuallyIsaak/status/2111818137947852897">Watch a 6-minute call</a> ·
  <a href="#ten-ways-to-hold-a-conversation">Call engines</a> ·
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  Free · Apple Silicon (M1 or newer) · macOS 14 Sonoma or newer · No account
</p>

> [!IMPORTANT]
> **Josie launches on 1 December 2026** (midnight, Central European Time). The [website](https://goekdeniz-guelmez.github.io/JOSIE/) counts down to it. Until then there is no installer here or in [Releases](https://github.com/Goekdeniz-Guelmez/JOSIE-Voice/releases); the 1.0.0 release notes describe what's coming.

---

## Talk or type

Switch between **Voice** and **Chat** with one tap. It's the same conversation either way: start a call, hang up, keep typing, and JOSIE remembers it all. Every conversation is saved in the sidebar and in the Library. The [website](https://goekdeniz-guelmez.github.io/JOSIE/) opens with a working copy of this screen: start a call, or switch to Chat and ask something.

<table>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-voice-idle-1600.webp"><img src="docs/images/mac-voice-idle-800.webp" alt="JOSIE on the Mac: the Voice screen with the orb, before Start call (real capture)"></a><br><sub><b>Voice</b>: just talk, and JOSIE answers out loud (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-chat-1600.webp"><img src="docs/images/mac-chat-800.webp" alt="An empty Chat on the Mac, ready for a first message (real capture)"></a><br><sub><b>Chat</b>: type when you can't talk (real capture)</sub></td>
  </tr>
</table>

## Gets things done

JOSIE works with the Apple apps you already use. Ask out loud and it really happens:

| App | Say | What happens |
|---|---|---|
| **Reminders** | "Remind me to bring a jacket at 7:30." | Added to Reminders, with the time set. |
| **Calendar** | "What's on tomorrow? Put lunch with Sam on Friday at noon." | Reads your day and adds the event. |
| **Maps** | "Find a pharmacy near me that's still open." | Looks up places and directions in Maps. |
| **Messages** | "Text Alex that I'm running ten minutes late." | Writes the draft in Messages. You tap Send. |

Each app is off until you turn it on in Settings → Apple tools, macOS asks your permission first, and nothing is sent without your tap.

## The real thing

**Six minutes. One call. No cuts.** A real session on a MacBook Pro M4 Pro, with Qwen3 speech recognition and synthesis at 4-bit and DeepSeek 4.1 Flash on Ollama Cloud: a conversation turns into work, with more than 100 tool calls along the way. No speed-ups. [Watch it on X](https://x.com/ActuallyIsaak/status/2111818137947852897).

## What Josie can do

| | |
|---|---|
| **Real conversation** | Knows when you've finished talking. Interrupt Josie just by speaking. |
| **Knows your voice** | Learns you from three short phrases and tells people apart. |
| **Voices you choose** | Pick a preset, clone a voice from a short recording, or describe a new one in words. Fourteen speech engines, among them Qwen3-TTS, Kokoro, Gradium Phonon, Ming-3.0 and ZONOS3-Mini with 27 voices and 44.1 kHz audio. |
| **Choose how it hears** | Ten speech recognition engines, among them Qwen3-ASR, NVIDIA Parakeet, Voxtral Realtime, Whisper, IBM Granite Speech and Apple's on-device recognizer. All on your Mac. |
| **Native call engines** | Nine experimental speech-to-speech engines: LFM3, Nemotron VoiceChat, Moshi, Realtime Venus, caramel-1, Awaken, Haru, Sophon-Realtime and Trelis Duplex. Eight are full duplex and listen while they speak. Add your own Hugging Face fine-tune. |
| **Private by design** | Hearing, voice recognition and speech run on your Mac. Your data stays on your Mac. No account. |
| **Takes real action** | Adds reminders and events, finds places in Maps and drafts Messages (you tap Send). Each one is off until you turn it on. |
| **Sees what you show it** | Turn on the camera and ask about what it sees. Needs an image-capable model. |
| **Adapts to the room** | Volume follows background noise, with echo cancellation. |
| **Living sky** | The background follows the real time of day under Apple's Liquid Glass design, with stars and the occasional shooting star at night. |
| **Personas** | Talk to JOSIE, JARVIS, HAL 9000, Her, Joi or a character you write, each with its own prompt, voice and orb colour. |
| **Your iPhone, your Mac** | On iPhone and iPad, pick your Mac as the provider, at home or over Tailscale. The call runs on your Mac, you can show Josie a photo, and the phone follows the Mac's memories, Library and name. |
| **Wake words** | Answers when a sentence starts or ends with your wake word, with a follow-up window and listen-back. Mac only. |
| **Apple Watch calls** | Start, end and mute a call from your Watch, or connect it straight to your server with the Watch's own microphone. |
| **Your choice of model** | Use Ollama, Anthropic's Claude through the Messages API, an OpenAI-compatible service or Apple Intelligence for the language model. |
| **Documents, pictures and media** | The Library reads Word and PowerPoint files, pictures and PDF figures, and embeds audio and video for search. |
| **Speech that rests** | Unloads the speech models after a quiet period you set, from 5 to 240 minutes. The next call loads them again. |
| **API wall** | A full-width dashboard shows the local API's clients, streams and tool calls at a glance. `/v1/realtime` talks to the loaded full-duplex engine, with up to four live or realtime sessions. |
| **Export and tidy up** | Export recorded calls for training, as OpenAI fine-tuning data, a MoshiRAG dataset and more. Delete the chats you select, or all of them. |
| **Its own chat prompt** | Write separate instructions for Chat and Voice. Muted in a call? Typed messages still get a text reply. |
| **Acknowledgements** | Settings → Acknowledgements on Mac, iPhone and iPad lists the projects, model families and licences JOSIE builds on, with thanks to Neywa Labs and Lucas Newman. |

## Ten ways to hold a conversation

Josie is a native Mac app built with SwiftUI and MLX Swift. Pick a call engine per call: the cascaded pipeline chains specialist models you choose yourself, and the nine native engines are single speech-to-speech models. Everything except the language model runs on your Mac's Apple Silicon.

**The cascaded pipeline** (the default):

- **Listening:** echo cancellation and an echo gate keep JOSIE's own voice out. Silero VAD notices when you speak, and Smart Turn v3 decides whether you've finished, may have finished (the language model starts early, its answer held back), or are still talking.
- **Speech recognition:** Qwen3-ASR by default, or one of nine others, including NVIDIA Parakeet, Voxtral Realtime, Whisper and Apple's on-device recognizer (chosen in Settings).
- **Who's speaking:** WeSpeaker, ported to MLX, recognises your voice and any voices you add.
- **The brain:** a language model in [Ollama](https://ollama.com) on your Mac (`qwen3.5:0.8b` by default), with up to 5 tool rounds per turn. In Settings you can switch to Anthropic's Claude or any OpenAI-compatible service with your own key, or to Apple Intelligence on macOS 26.
- **Speech:** Qwen3-TTS by default, with voice cloning and voice design, or one of thirteen others, including Kokoro, Gradium Phonon and ZONOS3-Mini (chosen in Settings). Replies are spoken in chunks while they are still being written.
- **Barge-in:** a second of your voice stops playback with a short fade, and the conversation keeps only the words you actually heard.

**All ten engines** (native engines are experimental; memory figures are approximate):

| Engine | Made by | Size | Core | Step | Remembers | Tools in JOSIE |
|---|---|---|---|---|---|---|
| **Cascaded pipeline** | JOSIE | Your choice | Your language model | Per turn | Last 40 turns | All tools |
| **LFM3** | Liquid AI | Audio 2B · Omni 2B | LFM3 2B | Whole turns | 24,576 tokens | Via your LLM |
| **Nemotron VoiceChat** | NVIDIA | 11B | Nemotron-H, 56 layers | 80 ms | About 8 min | Via your LLM |
| **Moshi** | Kyutai | 7B | Helium 7B + depth transformer | 80 ms | About 4 min | RAG variant |
| **Realtime Venus** | inclusionAI | Omni 9B | Qwen3-8B (MiniCPM-o) | 1 s units | 6,000–8,000 tokens | Via your LLM |
| **caramel-1** | naklecha | 413M | Own 413M, no text | 80 ms | About 4 min | Voice only |
| **Awaken** | Avera Labs | 8B | Qwen3-8B (Fun-Audio-Chat) | 200 ms | About 3 min | Voice only |
| **Haru** | Higurashi AI | 4B | Qwen3.5-4B | 133 ms | Up to 60 min | Voice only |
| **Sophon-Realtime** | Adventists AI | 4B Flash | Qwen3-4B thinker + Qwen3-TTS talker | 80 ms | 8 exchanges / 120 s | Voice only |
| **Duplex** | Trelis | duplex-1 200M | Own 200M, two tracks | 80 ms | 3–5 min | Voice only |

LFM3 answers your finished turn; the other eight native engines are full duplex. "Via your LLM" means the engine hands a request to the language model you selected, which runs your tools and returns the result to be spoken. The [website](https://goekdeniz-guelmez.github.io/JOSIE/#how) draws each engine's architecture, step by step. Sketches of the [Mac voice pipeline](docs/diagrams/02-mac-voice-pipeline.png), [tool routing](docs/diagrams/04-tools-architecture.png) and [iPhone-to-Mac calls](docs/diagrams/06-iphone-mac-live-sequence.png) are in `docs/diagrams`.

When no call has run for a while (5 to 240 minutes, 15 by default), the speech models unload; the next call loads them again. After setup, everything works offline except the language model, which runs in Ollama on your Mac.

## Make it yours

- **Models: A mind of your choosing.** Keep the language model on your Mac with Ollama, connect Claude or an OpenAI-compatible service, or choose Apple Intelligence. Set Full or Light prompts for Voice and Chat, and pick how calls run.
- **Tools & MCP: Connected. On your terms.** Connect the Apple apps you use, turn on web search, and add MCP servers. Set Read, Add or Full access per tool.
- **Memory: Pick up the thread.** JOSIE remembers useful facts, finds things in earlier conversations, and pulls the right passage from your documents.
- **Agents: A little help. A lot more done.** Agent mode searches, reads, checks and hands focused tasks to specialists. Give each one its own instructions, tools and step limit, and call it in with @.
- **Skills: Your habits. Its instructions.** Turn a set of instructions into a reusable Markdown skill: a writing style, a meeting format, a way of explaining. Attach it with @ when it matters.
- **Beyond the app: Your Mac, as an endpoint.** Turn on the optional OpenAI-compatible server to use the Mac’s pipeline from other apps, scripts, or your iPhone and iPad.

## Screenshots and clips

### Clips

Click a picture to play the clip. All clips are silent.

<table>
  <tr>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-native-engines-walkthrough.mp4"><img src="docs/videos/real-native-engines-walkthrough-poster.jpg" alt="Native engine settings: the architecture picker, Moshi models, an empty custom-repository form and LFM3 choices (real capture)"></a><br><sub>▶ Native call engine settings (real capture)</sub></td>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-dashboard-map-walkthrough.mp4"><img src="docs/videos/real-dashboard-map-walkthrough-poster.jpg" alt="Dashboard latency and the existing embedding graph in 2D and 3D (real capture)"></a><br><sub>▶ Dashboard and embedding map (real capture)</sub></td>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-ipad-navigation.mp4"><img src="docs/videos/real-ipad-navigation-poster.jpg" alt="Empty landscape Chat, the menu, provider settings and Conversation on an iPad simulator (real capture)"></a><br><sub>▶ iPad navigation (real capture)</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-iphone-navigation.mp4"><img src="docs/videos/real-iphone-navigation-poster.jpg" alt="Voice, Chat, the avatar menu, Settings, Conversation and Tools & MCP on an iPhone simulator (real capture)"></a><br><sub>▶ iPhone navigation (real capture)</sub></td>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-ios-orb-idle.mp4"><img src="docs/videos/real-ios-orb-idle-poster.jpg" alt="The orb breathing on the iPhone while JOSIE waits (real capture)"></a><br><sub>▶ The orb, idle (real capture)</sub></td>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-sky-day-to-night.mp4"><img src="docs/videos/real-sky-day-to-night-poster.jpg" alt="The sky behind the orb at eight times of day, from dawn into night (real capture)"></a><br><sub>▶ The sky from morning to night (real capture)</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><a href="docs/videos/real-sky-night-shooting-stars.mp4"><img src="docs/videos/real-sky-night-shooting-stars-poster.jpg" alt="The night sky behind the orb with stars and the occasional shooting star (real capture)"></a><br><sub>▶ Night sky with shooting stars (real capture)</sub></td>
    <td width="33%" align="center" valign="top"><a href="docs/videos/josie-transcript-morph.mp4"><img src="docs/videos/josie-transcript-morph-poster.jpg" alt="Turning the transcript on and off during a call (mockup)"></a><br><sub>▶ Show or hide the transcript mid-call (mockup)</sub></td>
    <td width="33%" align="center" valign="top"><a href="docs/videos/josie-menu-bar-api.mp4"><img src="docs/videos/josie-menu-bar-api-poster.jpg" alt="The menu bar extra: the API Server switch turns on and shows the local address (mockup)"></a><br><sub>▶ Menu bar extra with the local API server (mockup)</sub></td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top"><a href="docs/videos/josie-api-river.mp4"><img src="docs/videos/josie-api-river-poster.jpg" alt="Dashboard API server: live tiles above a river of requests, stream chunks and tool calls (mockup)"></a><br><sub>▶ Every request to the local API (mockup)</sub></td>
  </tr>
</table>

### Screenshots

Real captures are unretouched screenshots of the current app from the main branch, taken on 13 November 2026. Selected native settings are unsaved drafts, and no model was downloaded for them. Screens that need a live call or personal data have not been captured yet and are still mockups.

<details open>
<summary><b>Mac</b> (6)</summary>
<br>

<table>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-call-engine-picker-1600.webp"><img src="docs/images/mac-call-engine-picker-800.webp" alt="The call engine picker: Cascaded Pipeline, LFM3, Nemotron VoiceChat, Moshi, Realtime Venus, Caramel-1, Awaken and Haru (real capture)"></a><br><sub>Pick a call engine (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-haru-engine-1600.webp"><img src="docs/images/mac-haru-engine-800.webp" alt="Haru 4B engine settings with call context, your selected voice and a precision picker (real capture)"></a><br><sub>Haru 4B: full duplex in your chosen voice (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-models-on-this-mac-1600.webp"><img src="docs/images/mac-models-on-this-mac-800.webp" alt="Models on this Mac with their installed local precisions (real capture)"></a><br><sub>Models on this Mac and their precisions (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-zonos3-settings-1600.webp"><img src="docs/images/mac-zonos3-settings-800.webp" alt="ZONOS3-Mini speech settings with Not downloaded states and precision choices (real capture)"></a><br><sub>ZONOS3-Mini speech settings (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-audio-1600.webp"><img src="docs/images/mac-settings-audio-800.webp" alt="Audio and devices with the system microphone fallback (real capture)"></a><br><sub>Audio and devices (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-mcp-1600.webp"><img src="docs/images/mac-settings-mcp-800.webp" alt="Tools and MCP server list (real capture)"></a><br><sub>Your MCP servers (real capture)</sub></td>
  </tr>
</table>

</details>

<details>
<summary><b>Mac · Call engines</b> (5)</summary>
<br>

<table>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-venus-model-picker-1600.webp"><img src="docs/images/mac-venus-model-picker-800.webp" alt="Realtime Venus with the Venus-Omni 9B model picker and its delegation switches (real capture)"></a><br><sub>Realtime Venus hands hard work to your LLM (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-moshi-model-picker-1600.webp"><img src="docs/images/mac-moshi-model-picker-800.webp" alt="Moshi model picker: Moshiko, Moshika, Seamless and RAG, plus Add custom (real capture)"></a><br><sub>Moshi and its model variants (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-lfm3-model-picker-1600.webp"><img src="docs/images/mac-lfm3-model-picker-800.webp" alt="LFM3 model picker with Audio 2B and Omni 2B (real capture)"></a><br><sub>LFM3 Audio and Omni (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-native-add-custom-1600.webp"><img src="docs/images/mac-native-add-custom-800.webp" alt="The empty Add custom form for a Hugging Face repository (real capture)"></a><br><sub>Add your own model from Hugging Face (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-native-memory-1600.webp"><img src="docs/images/mac-native-memory-800.webp" alt="Moshi engine page: how long a call it remembers (real capture)"></a><br><sub>How much of a call each engine remembers (real capture)</sub></td>
  </tr>
</table>

</details>

<details>
<summary><b>Mac · Calls</b> (6)</summary>
<br>

<table>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-call-orb-1600.webp"><img src="docs/images/mac-call-orb-800.webp" alt="A call with transcripts hidden: the big orb and five call controls (mockup)"></a><br><sub>Voice: just talk (mockup)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-call-1600.webp"><img src="docs/images/mac-call-800.webp" alt="A call with transcripts shown and a tool call (mockup)"></a><br><sub>Live transcripts (mockup)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-attachments-drop-1600.webp"><img src="docs/images/mac-attachments-drop-800.webp" alt="A PDF dragged onto a call (mockup)"></a><br><sub>Drop a PDF onto a call (mockup)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-camera-1600.webp"><img src="docs/images/mac-camera-800.webp" alt="A call with the camera on (mockup)"></a><br><sub>Ask what the camera sees (mockup)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-mute-chip-1600.webp"><img src="docs/images/mac-mute-chip-800.webp" alt="A call after a timed mute, with the countdown chip (mockup)"></a><br><sub>A timed mute (mockup)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-call-debug-1600.webp"><img src="docs/images/mac-call-debug-800.webp" alt="A call with the developer latency overlay (mockup)"></a><br><sub>Developer overlay (mockup)</sub></td>
  </tr>
</table>

</details>

<details>
<summary><b>Mac · Library, voice and dashboard</b> (16)</summary>
<br>

<table>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-embedding-map-1600.webp"><img src="docs/images/mac-embedding-map-800.webp" alt="The Library's embedding map in 2D (real capture)"></a><br><sub>The embedding map in 2D (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-embedding-map-3d-1600.webp"><img src="docs/images/mac-embedding-map-3d-800.webp" alt="The embedding map in 3D (real capture)"></a><br><sub>The same map in 3D (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-voice-studio-1600.webp"><img src="docs/images/mac-voice-studio-800.webp" alt="Voice settings for the selected Phonon engine (real capture)"></a><br><sub>Voice settings follow the engine (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-overview-1600.webp"><img src="docs/images/mac-dashboard-overview-800.webp" alt="Dashboard overview with local usage totals (real capture)"></a><br><sub>Dashboard overview (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-calls-1600.webp"><img src="docs/images/mac-dashboard-calls-800.webp" alt="Dashboard call analytics from local data (real capture)"></a><br><sub>Calls (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-chat-1600.webp"><img src="docs/images/mac-dashboard-chat-800.webp" alt="Dashboard chat analytics from local data (real capture)"></a><br><sub>Chat (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-latency-1600.webp"><img src="docs/images/mac-dashboard-latency-800.webp" alt="Dashboard latency per voice-turn stage (real capture)"></a><br><sub>Latency (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-embeddings-1600.webp"><img src="docs/images/mac-dashboard-embeddings-800.webp" alt="Dashboard embeddings inventory (real capture)"></a><br><sub>What's indexed (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-api-1600.webp"><img src="docs/images/mac-dashboard-api-800.webp" alt="Dashboard API server in its idle state (real capture)"></a><br><sub>API server (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-library-1600.webp"><img src="docs/images/mac-library-800.webp" alt="The Library window with filters and a chunk preview (mockup)"></a><br><sub>The Library (mockup)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-voice-id-1600.webp"><img src="docs/images/mac-voice-id-800.webp" alt="Voice ID enrolment with three phrases (mockup)"></a><br><sub>Voice ID (mockup)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-highlights-1600.webp"><img src="docs/images/mac-dashboard-highlights-800.webp" alt="Dashboard highlights: Wrapped tiles and records (mockup)"></a><br><sub>Highlights (mockup)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-speakers-1600.webp"><img src="docs/images/mac-dashboard-speakers-800.webp" alt="Dashboard speakers with match confidence (mockup)"></a><br><sub>Speakers (mockup)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-dashboard-export-1600.webp"><img src="docs/images/mac-dashboard-export-800.webp" alt="Dashboard export for training (mockup)"></a><br><sub>Export for training (mockup)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-menu-bar-1600.webp"><img src="docs/images/mac-menu-bar-800.webp" alt="The menu bar extra during a call (mockup)"></a><br><sub>Menu bar (mockup)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-hub-menu-1600.webp"><img src="docs/images/mac-hub-menu-800.webp" alt="The avatar menu (mockup)"></a><br><sub>Avatar menu (mockup)</sub></td>
  </tr>
</table>

</details>

<details>
<summary><b>Mac · Settings and onboarding</b> (12)</summary>
<br>

<table>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-models-1600.webp"><img src="docs/images/mac-settings-models-800.webp" alt="Settings, Models and endpoints (real capture)"></a><br><sub>Models &amp; endpoints (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-speech-engines-1600.webp"><img src="docs/images/mac-settings-speech-engines-800.webp" alt="Settings, Speech engines (real capture)"></a><br><sub>Speech engines (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-conversation-1600.webp"><img src="docs/images/mac-settings-conversation-800.webp" alt="Settings, Conversation (real capture)"></a><br><sub>Conversation and wake words (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-tools-1600.webp"><img src="docs/images/mac-settings-tools-800.webp" alt="Settings, Tools with access depth (real capture)"></a><br><sub>Tools (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-documents-1600.webp"><img src="docs/images/mac-settings-documents-800.webp" alt="Settings, Documents and search (real capture)"></a><br><sub>Documents &amp; search (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-agents-1600.webp"><img src="docs/images/mac-settings-agents-800.webp" alt="Settings, Agents (real capture)"></a><br><sub>Agents (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-skills-1600.webp"><img src="docs/images/mac-settings-skills-800.webp" alt="Settings, Skills (real capture)"></a><br><sub>Skills (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-api-1600.webp"><img src="docs/images/mac-settings-api-800.webp" alt="Settings, API server with the key hidden (real capture)"></a><br><sub>API server (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-assistant-1600.webp"><img src="docs/images/mac-settings-assistant-800.webp" alt="Settings, Assistant (real capture)"></a><br><sub>Assistant (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-appearance-1600.webp"><img src="docs/images/mac-settings-appearance-800.webp" alt="Settings, Appearance (real capture)"></a><br><sub>Appearance (real capture)</sub></td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top"><a href="docs/images/mac-settings-diagnostics-1600.webp"><img src="docs/images/mac-settings-diagnostics-800.webp" alt="Settings, Version and diagnostics (real capture)"></a><br><sub>Diagnostics (real capture)</sub></td>
    <td width="50%" align="center" valign="top"><a href="docs/images/onboarding-models-1600.webp"><img src="docs/images/onboarding-models-800.webp" alt="Onboarding: choosing on-device model sizes (mockup)"></a><br><sub>First-launch model download (mockup)</sub></td>
  </tr>
</table>

</details>

<details open>
<summary><b>iPhone, iPad and Apple Watch</b> (18)</summary>
<br>

<table>
  <tr>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-onboarding-welcome.webp"><img src="docs/images/ios-onboarding-welcome.webp" width="180" alt="iPhone welcome screen (real capture)"></a><br><sub>Welcome (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-voice-idle.webp"><img src="docs/images/ios-voice-idle.webp" width="180" alt="iPhone Voice, idle (real capture)"></a><br><sub>Voice (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-chats.webp"><img src="docs/images/ios-chats.webp" width="180" alt="iPhone chats list, empty (real capture)"></a><br><sub>Chats (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-chat-empty.webp"><img src="docs/images/ios-chat-empty.webp" width="180" alt="iPhone Chat, empty (real capture)"></a><br><sub>Chat (real capture)</sub></td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-onboarding-gpt-live.webp"><img src="docs/images/ios-onboarding-gpt-live.webp" width="180" alt="iPhone onboarding: Connect GPT-Live (real capture)"></a><br><sub>Connect GPT-Live (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-onboarding-tour.webp"><img src="docs/images/ios-onboarding-tour.webp" width="180" alt="iPhone onboarding tour (real capture)"></a><br><sub>Tour (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-menu.webp"><img src="docs/images/ios-menu.webp" width="180" alt="iPhone avatar menu (real capture)"></a><br><sub>Menu (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-settings.webp"><img src="docs/images/ios-settings.webp" width="180" alt="iPhone Settings (real capture)"></a><br><sub>Settings (real capture)</sub></td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-settings-providers.webp"><img src="docs/images/ios-settings-providers.webp" width="180" alt="iPhone Settings, Providers (real capture)"></a><br><sub>Providers (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-settings-conversation.webp"><img src="docs/images/ios-settings-conversation.webp" width="180" alt="iPhone Settings, Conversation (real capture)"></a><br><sub>Conversation (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-settings-tools.webp"><img src="docs/images/ios-settings-tools.webp" width="180" alt="iPhone Settings, Tools and MCP (real capture)"></a><br><sub>Tools (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/watch-direct.webp"><img src="docs/images/watch-direct.webp" width="180" alt="Apple Watch direct-call idle screen (real capture)"></a><br><sub>Watch, direct call (real capture)</sub></td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top"><a href="docs/images/watch-call.webp"><img src="docs/images/watch-call.webp" width="180" alt="Apple Watch as an iPhone remote (real capture)"></a><br><sub>Watch, phone remote (real capture)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-call.webp"><img src="docs/images/ios-call.webp" width="180" alt="iPhone GPT-Live call (mockup)"></a><br><sub>A GPT-Live call (mockup)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-call-mac.webp"><img src="docs/images/ios-call-mac.webp" width="180" alt="iPhone call through Josie on the Mac with a photo (mockup)"></a><br><sub>Calling your Mac (mockup)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-live-activity.webp"><img src="docs/images/ios-live-activity.webp" width="180" alt="Lock Screen Live Activity (mockup)"></a><br><sub>Live Activity (mockup)</sub></td>
  </tr>
  <tr>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-dynamic-island.webp"><img src="docs/images/ios-dynamic-island.webp" width="180" alt="Dynamic Island during a call (mockup)"></a><br><sub>Dynamic Island (mockup)</sub></td>
    <td width="25%" align="center" valign="top"><a href="docs/images/ios-dashboard-calls.webp"><img src="docs/images/ios-dashboard-calls.webp" width="180" alt="iPhone Dashboard, Calls (mockup)"></a><br><sub>iPhone dashboard (mockup)</sub></td>
  </tr>
</table>

</details>

<p><a href="docs/images/ipad-chat-1600.webp"><img src="docs/images/ipad-chat-800.webp" alt="An empty landscape iPad Chat (real capture)"></a><br><sub>iPad Chat, landscape (real capture)</sub></p>

<sub>Pictures and clips marked (mockup) are rendered from the app's source with demo content; ones marked (real capture) are recorded from the running app.</sub>

## Good to know

- **Other models:** in Settings, switch to Anthropic's Claude, any OpenAI-compatible service with your own key, or to Apple Intelligence on macOS 26.
- **Run setup again:** Settings → Setup → Run setup again.
- **Apple tools:** turn them on one by one in Settings. macOS asks permission the first time each is used.
- **Optional extras** download only if you want them: voice design (3.1 GB) and word timestamps (1.3 GB).
- **For tinkerers:** Dashboard → Chat counts tokens per reply. Settings → Developer → Debug overlay shows live latency on the call screen.

## FAQ

**Can I download it?** Not yet. The first public Mac DMG arrives on **1 December 2026** on [GitHub Releases](https://github.com/Goekdeniz-Guelmez/JOSIE-Voice/releases). Watch the repository to hear the moment it ships.

**Is it free?** Yes.

**Does my voice go to the cloud?** No. Hearing, voice recognition and speech run on your Mac, and by default the language model (Ollama) does too. If you switch to an online model, your text goes to that service.

**Do I need an account?** No.

**Does it work on Intel Macs?** No, Apple Silicon (M1 or later) only.

**Is there an iPhone or iPad version?** Not as a download yet. On iPhone and iPad, calls use OpenAI GPT-Live, your own compatible server, or Josie on your Mac over your network or Tailscale. Connected to your Mac, they follow its memories, Library and name. See the iPhone and iPad screenshots above.

**Does it work with Apple Watch?** Yes, with watchOS 10 or later. The Watch app comes with the iPhone app. It can start, end and mute the call on your iPhone, or run its own call with the Watch's microphone, straight to OpenAI or to a JOSIE or compatible server.

**Can I use Claude?** Yes. Choose Anthropic as the language model in Settings and add your API key. Your text then goes to Anthropic.

**Can it listen for its name?** Yes, on the Mac. Turn on wake words in Settings → Conversation.

**It says "Ollama isn't running".** Open Ollama from Applications, then click Recheck in JOSIE's setup.

**JOSIE can't hear me.** Open System Settings → Privacy & Security → Microphone and turn on Josie.

**How much space does it need?** About 5 GB of voice models plus about 1 GB for the language model, at the default small sizes.

**How do I uninstall it?** Drag Josie to the Trash. To remove its data and models too, delete the `Josie` folder in `~/Library/Application Support`.

## The JOSIE model family

<img src="docs/logo.png" alt="JOSIE orb" width="56" align="left">

The JOSIE model family is a separate project by the same author: custom fine-tuned, personality-driven language models, trained entirely on Apple Silicon with [MLX-LM-LoRA](https://github.com/Goekdeniz-Guelmez/mlx-lm-lora). The app does not need them; it works with whichever language model you choose. Meet the models on [Hugging Face](https://huggingface.co/Goekdeniz-Guelmez).

<br clear="left">

## About this repository

This repository hosts the Josie website and visuals. The site lives in [`docs/`](docs/) and is published by GitHub Pages at **[goekdeniz-guelmez.github.io/JOSIE/](https://goekdeniz-guelmez.github.io/JOSIE/)** on every push to `main`. It is a static page with no build step:

| File | What it is |
|---|---|
| [`docs/index.html`](docs/index.html) | The page. Every section stays readable without JavaScript. |
| [`docs/site.css`](docs/site.css) | The one stylesheet: the app's sky, glass, bubble and call-button styles. |
| [`docs/site.js`](docs/site.js) | Interactions: the live app in the hero, tabs, the feature filter, the release pop-up and countdown, and the download lookup after launch. |
| [`docs/sky.js`](docs/sky.js) | The app's Metal sky shader and time-of-day model, ported to WebGL. Scrolling moves the sky from morning to night. |
| [`docs/orb.js`](docs/orb.js) | The app's liquid orb shader and palettes, ported to WebGL. |

App downloads will be published in [GitHub Releases](https://github.com/Goekdeniz-Guelmez/JOSIE-Voice/releases), starting with the first DMG on 1 December 2026; the app's source code is private.

Built with MLX Swift, Qwen3-ASR, Qwen3-TTS, Parakeet, Kokoro, Silero VAD, Smart Turn v3 and WeSpeaker. Thanks to Neywa Labs and Lucas Newman. Ollama is a separate app by its own developers.

Feedback: goekdenizguelmez.ml@gmail.com · [Sponsor on GitHub](https://github.com/sponsors/Goekdeniz-Guelmez)
