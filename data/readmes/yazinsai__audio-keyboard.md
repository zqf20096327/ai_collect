<p align="center">
  <img src="docs/images/hero.png" alt="My Board: type like Gboard, write like you" width="100%">
</p>

<h1 align="center">My Board</h1>

<p align="center">
  <b>The AI-first Android keyboard.</b><br>
  Everything you like about Gboard, plus an assistant that writes in your voice.
</p>

<p align="center">
  <img alt="Android 10+" src="https://img.shields.io/badge/Android-10%2B-3DDC84?logo=android&logoColor=white">
  <img alt="Kotlin" src="https://img.shields.io/badge/Kotlin-100%25-7F52FF?logo=kotlin&logoColor=white">
  <img alt="English and Arabic" src="https://img.shields.io/badge/English%20%2B%20العربية-✓-0B57D0">
  <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-blue">
</p>

---

Most "AI keyboards" are a chat window stapled onto a mediocre keyboard. My Board goes the other way. It starts as a
faithful Gboard: same key geometry measured to the pixel, same suggestion strip, same glide typing, same feel under your
thumbs. Then it adds the things Gboard won't do.

- **It replies before you ask.** Open a chat and three replies are already waiting in the suggestion strip, written
  the way *you* text that person.
- **You say what you mean, it writes the message.** Tap ✦ and speak an instruction ("tell her Thursday works and ask
  what time"). The finished message lands in the field, in your voice, aware of what's on screen.
- **It remembers people.** Each chat gets its own memory: who they are to you, how you talk, the facts worth bringing
  up later, and what you want from the relationship.
- **It gets better the more you use it.** It learns from what you send, what you edit, and which drafts you pick or
  ignore.

And it's private by design: nothing goes to Google, there's no analytics, and the AI only ever talks to the service
**you** choose.

## ✦ AI features

<table>
  <tr>
    <td align="center" width="33%"><img src="docs/images/waiting-replies.png" alt="Waiting replies in the suggestion strip"><br><b>Waiting replies</b><br><sub>Three drafts appear in the strip when you open a remembered chat. Tap one and it's in the field.</sub></td>
    <td align="center" width="33%"><img src="docs/images/spark.png" alt="✦ writing a reply from a spoken instruction"><br><b>✦ Say it, it's written</b><br><sub>Speak an instruction, get the message. It reads the screen so the reply fits the conversation.</sub></td>
    <td align="center" width="33%"><img src="docs/images/chat-memory.png" alt="The chat memory panel"><br><b>Chat memory</b><br><sub>A goal, a profile and dated notes for every chat, written and kept up to date for you.</sub></td>
  </tr>
</table>

| Feature | What it does |
|---|---|
| **✦ Prompt** | Speech as an instruction. "Make it shorter", "say no politely", "what's 15% of 80": the result goes straight into the field. Select text first to rewrite it. |
| **Dictation** | Speech typed verbatim, never restyled. Chunked while you talk, retried if the network drops, and safe to keep talking hands-free. |
| **Waiting replies** | Drafts three replies (a quick reaction, a fuller answer, a follow-up question) as soon as you open a chat you've asked it to remember. |
| **Learns your voice** | Keeps the messages you send so ✦ matches your length, slang, emoji and language mix. Import old WhatsApp chats to give it a head start. |
| **Chat memory** | History, a short profile, notes ("birthday on the 28th") and an optional goal (banter, getting closer, strictly professional) per chat. |
| **Picks** | Every draft gets a verdict: picked, sent unchanged, edited or ignored. Drafts drift toward what actually lands. |
| **Lock chat memory** | Optional: your fingerprint before anyone can open what it remembers about your chats. |

## ⌨️ A real keyboard first

<table>
  <tr>
    <td align="center" width="33%"><img src="docs/images/glide-dark.png" alt="Glide typing in dark mode"><br><b>Glide typing</b><br><sub>English and Arabic, with Gboard's trail.</sub></td>
    <td align="center" width="33%"><img src="docs/images/arabic.png" alt="Arabic layout"><br><b>Arabic, done properly</b><br><sub>Full RTL layout, Arabic dictionary and autocorrect, Eastern digits if you want them.</sub></td>
    <td align="center" width="33%"><img src="docs/images/emoji.png" alt="Emoji panel"><br><b>Emoji, searchable</b><br><sub>Search in English or Arabic, skin tones remembered, recents up top.</sub></td>
  </tr>
</table>

- Key geometry, colours and long-press panels measured against Gboard, light and dark.
- Suggestions, next-word prediction and autocorrect for English and Arabic, built from open word lists and tuned
  against an accuracy harness (fixes ~60% of typos, changes 0.2% of correct words).
- Personal dictionary, learned words, clipboard history with pins, number row, adjustable height, haptics and sound.
- Password-manager key and inline autofill chips (1Password, Google) in sign-in fields.
- Respects incognito and password fields: nothing is learned, read or sent there, and ✦ and the mic hide themselves.

## 🔒 Privacy

My Board was built for one person who cared a lot about what leaves his phone. That shows.

- **No Google, no analytics, no ads.** The only network calls are to the AI service you configure.
- **You pick the AI.** [Venice AI](https://venice.ai) (private models that don't keep what you send) or your own
  OpenAI-compatible servers (for example [Speaches](https://github.com/speaches-ai/speaches) and
  [llama.cpp's server](https://github.com/ggml-org/llama.cpp)) on your own network.
- **Off until you turn it on.** Learning how you write, remembering chats, waiting replies and the debug log all start
  off. Turn them on in Settings → AI writing when you want them.
- **On-device storage.** Learned words, messages, chat memory and clipboard stay on the phone in no-backup storage.
  Audio is deleted once transcribed.
- **Never in sensitive fields.** Password and incognito fields are never read, learned from or sent anywhere.
- **Lockable.** Turn on *Lock chat memory* and the chat panel, Settings → Chats and the debug log ask for your
  fingerprint first. They also block screenshots and screen recording.

<p align="center"><img src="docs/images/privacy-settings.png" alt="AI writing settings" width="300"></p>

### About the accessibility permission

✦ and chat memory read the text of the app under the keyboard through an Android accessibility service called
*My Board screen context*. It's only needed for those features, it reads only when the keyboard is open (and, for
remembered chats, only in the messaging apps you've listed), and you can leave it off and still use everything else.

## 🚀 Getting started

**Requirements:** Android 10 or newer, and for the AI features either a Venice AI API key or your own server.

### Install

Download the latest `my-board-<version>.apk` from [Releases](https://github.com/yazinsai/audio-keyboard/releases/latest)
and open it on your phone. Android asks you to allow installs from your browser or file manager the first time.
For automatic updates, add `https://github.com/yazinsai/audio-keyboard` to [Obtainium](https://github.com/ImranR98/Obtainium)
instead.

Every release is built from its tag by GitHub Actions and signed with the same key. Its certificate SHA-256 is:

```
6A:4B:68:3B:EB:4B:CC:B1:C6:CD:89:41:C7:EB:74:C4:96:51:71:F9:1E:6C:E1:81:3F:E3:25:86:4F:53:7B:8F
```

Check it with `apksigner verify --print-certs my-board-<version>.apk`, or with [AppVerifier](https://github.com/soupslurpr/AppVerifier)
once it's installed. Play Protect may warn about installing a keyboard from outside the Play Store; that's expected for
sideloaded keyboards.

### Build and install

```bash
git clone https://github.com/yazinsai/audio-keyboard.git
cd audio-keyboard
tools/fetch_wordlists.sh && tools/fetch_emoji.sh      # dictionaries and emoji data (checked by SHA-256)
echo "sdk.dir=$HOME/Library/Android/sdk" > local.properties   # your Android SDK
./gradlew :app:installDebug                            # or :app:assembleRelease
```

Release builds are signed with the key in `keystore.properties` (git-ignored: `storeFile`, `storePassword`,
`keyAlias`, `keyPassword`). Without one they fall back to the debug key, which is fine for sideloading your own build.
A build you make yourself is signed with a different key from the published releases, so uninstall one before
installing the other.

### Set it up

1. Open **My Board** and follow the three steps: enable it, switch to it, allow the microphone.
2. Tap **Turn on AI writing** and pick your service under **AI service**:
   - **Venice AI:** paste an API key from [venice.ai/settings/api](https://venice.ai/settings/api).
   - **My server:** enter the addresses of your speech-to-text and chat servers (any OpenAI-compatible
     `/v1/audio/transcriptions` and `/v1/chat/completions`).
3. Turn on **Read the screen for ✦** for context-aware writing, then **Learn how I write**, **Remember chats** and
   **Waiting replies** as you like.
4. In a chat, tap the chat's name in the toolbar to open its memory, or just start typing.

## 🧱 How it's built

```
app/      Android: the input method service, keyboard view, panels, settings, accessibility screen reader
engine/   Pure Kotlin, JVM-tested: dictionaries, suggestions, autocorrect, glide decoding, voice pipeline,
          prompts, chat memory, writing-style store
tools/    Data fetchers, a dev loop for the emulator (tools/dev.sh), a voice proxy for fault injection
```

- No third-party UI framework: the keyboard is drawn on a single `View` for speed (≈1 ms per key in release builds).
- Dictionaries are compiled at build time and memory-mapped straight from the APK.
- The engine has ~400 JVM unit tests: `./gradlew :engine:test :app:testDebugUnitTest`.
- Live tests against a real service are opt-in:
  `VENICE_API_KEY=... ./gradlew :engine:test -Pvoice=venice -Pllm=venice --tests '*Live*'`.

The project's vocabulary (Chat, History, Profile, Goal, Note, Waiting reply…) is defined in
[GLOSSARY.md](GLOSSARY.md). Voice and dictation research notes are in [docs/voice.md](docs/voice.md).

## 🤝 Contributing

Issues and pull requests are welcome. A few ground rules:

- Never commit API keys, your own server addresses, or real messages. Chat-screen test fixtures must be scrubbed with
  `tools/scrub_dump.py`.
- Anything that reads, learns or sends must stay off by default and never run in password or incognito fields.
- Run the JVM tests before opening a PR.

## 📄 License

[MIT](LICENSE). Word lists (Leipzig Corpora, CC BY 4.0), Unicode emoji data and Material Symbols are under their own
licenses; see [THIRD_PARTY.md](THIRD_PARTY.md).

My Board is an independent project and isn't affiliated with Google. Gboard is a trademark of Google LLC.
