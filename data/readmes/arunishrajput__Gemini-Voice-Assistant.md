# Gemini Voice Assistant

A wake-word voice assistant for your terminal. It listens on your microphone,
transcribes what you say, chats with Google's Gemini API, and speaks the
reply back — all inside a live-updating text UI built with [Rich](https://github.com/Textualize/rich).

![Gemini Voice Assistant — conversation view](assets/screenshot-conversation.svg)

## Features

- **Live terminal UI** — a status header (Idle / Listening / Recognizing /
  Thinking / Speaking / Paused), a scrolling conversation log, and a footer
  with your wake word, exit words, and current model, all refreshed in place.
- **Wake word activation** — say the wake word (default `"gemini"`) to start
  forwarding speech to Gemini; say an exit word to pause without quitting.
- **Text-to-speech replies** via `pyttsx3`, with a configurable speaking rate.
- **Demo mode** (`--demo`) — preview the entire UI with a scripted
  conversation, no microphone or API key required.
- **Config via `.env`, environment variables, or flags** — your API key lives
  in a git-ignored `.env` file, never in the source code.

## Preview

Idle, waiting for the wake word:

![Listening state](assets/screenshot-listening.svg)

Try it without a microphone or API key:

```bash
python main.py --demo
```

## Prerequisites

- Python 3.9+
- A microphone
- A [Gemini API key](https://aistudio.google.com/app/apikey)
- `PyAudio`'s system dependency, **PortAudio**:
  - macOS: `brew install portaudio`
  - Debian/Ubuntu: `sudo apt install portaudio19-dev`
  - Windows: usually not required — `pip install PyAudio` uses a prebuilt wheel
- A text-to-speech engine for `pyttsx3` (built in on macOS and Windows; on
  Linux install one with `sudo apt install espeak`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arunishrajput/Gemini-Voice-Assistant.git
   cd Gemini-Voice-Assistant
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API key using a `.env` file:**

   ```bash
   cp .env.example .env
   ```

   Then open `.env` and replace the placeholder with your own
   [Gemini API key](https://aistudio.google.com/app/apikey):

   ```
   GEMINI_API_KEY=your-api-key-here
   ```

   `main.py` loads `.env` automatically via `python-dotenv`. The file is
   listed in `.gitignore`, so your key never gets committed — don't remove it
   from there, and never commit `.env` itself.

## Usage

```bash
python main.py
```

- Say the wake word (default `"gemini"`) to start sending what you say to
  Gemini.
- Say an exit word (`"exit"`, `"stop"`, `"quit"`, `"bye"`, `"goodbye"`) to
  pause — the assistant keeps listening for the wake word to resume.
- Press `Ctrl+C` to quit.

### Command-line options

Every environment variable below can be set in `.env` (see `.env.example`),
exported in your shell, or overridden with its flag.

| Flag             | Environment variable | Default            | Description                                  |
| ---------------- | --------------------- | ------------------- | --------------------------------------------- |
| `--api-key`       | `GEMINI_API_KEY`      | —                   | Your Gemini API key                           |
| `--model`         | `GEMINI_MODEL`        | `gemini-2.5-flash`  | Gemini model to chat with                     |
| `--wake-word`     | `WAKE_WORD`           | `gemini`            | Word that activates the assistant             |
| `--exit-words`    | `EXIT_WORDS`          | `exit,stop,quit,bye,goodbye` | Comma-separated words that pause it  |
| `--voice-rate`    | `VOICE_RATE`          | `200`               | Text-to-speech rate (words per minute)        |
| `--demo`          | —                      | off                 | Run a scripted UI preview, no mic/API needed  |

## How it works

The assistant is a small state machine, rendered live by `tui.py`:

```
Idle → Listening → Recognizing → (wake word?) → Thinking → Speaking → Listening
                                        │
                                   (exit word?) → Paused → Listening
```

- `main.py` drives the loop: capture audio, transcribe it with
  `speech_recognition`, send it to Gemini via the `google-genai` SDK, and
  speak the response with `pyttsx3`.
- `tui.py` owns the `AssistantUI` — it tracks state and conversation history
  and renders them as a `rich.layout.Layout` inside a `rich.live.Live`
  session, so the screen updates in place instead of scrolling.

## Project structure

```
main.py            entry point: argument parsing, speech loop, Gemini calls
tui.py              Rich-based terminal UI (state, transcript, layout)
requirements.txt    dependencies
.env.example        template for your local .env (copy it, then fill it in)
assets/             README screenshots
```

## Troubleshooting

- **`PyAudio` fails to build** — install PortAudio first (see Prerequisites),
  then re-run `pip install -r requirements.txt`.
- **No sound / TTS errors on Linux** — install `espeak`:
  `sudo apt install espeak`.
- **`Missing Gemini API key` error** — make sure `.env` exists (copied from
  `.env.example`) and contains a `GEMINI_API_KEY` line, or pass `--api-key`.
- **Nothing happens when you talk** — check your OS microphone permissions
  for your terminal app, and try increasing the timeout by editing
  `recognizer.listen(source, timeout=5, ...)` in `main.py` if your mic is slow
  to pick up sound.

## Contribution

Feel free to fork this repository, create a feature branch, and submit a pull
request. Contributions, issues, and feature requests are welcome!

## Acknowledgments

- [Google Gen AI SDK](https://github.com/googleapis/python-genai)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [Rich](https://github.com/Textualize/rich)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
