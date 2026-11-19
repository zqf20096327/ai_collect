# android-agent

**Let an AI agent use your Android phone and its apps — about 10× cheaper than screenshot-based tools.**

Works from your computer (Windows, macOS, Linux) or directly on the phone (Termux, no PC needed).
Plugs into Claude Code, Cursor, Claude Desktop and any other MCP client.

![One sentence in: a model opens YouTube, reads the screen as text and plays a video, in 6 steps](docs/demo.gif)

## How it works

Most phone agents look at the screen as images (~1,500 tokens per look).
android-agent reads it as a short numbered list from Android's accessibility tree, and after the
first look sends only what changed:

```
com.android.settings | portrait | 15 items
[0] button "Search settings"
[5] button "Wi-Fi · HomeNetwork"
[6] button "Bluetooth · On"
[9] button "Hotspot · Off"
```

That screen is ~150 tokens. The agent replies `tap 5`.

![12×34 on a real phone's calculator by label: ~294 tokens instead of ~13,500 with screenshots](docs/demo-calculator.gif) Screenshots are used only when text is
not enough (games, Flutter apps, maps).

In a first test (6 everyday tasks: Settings, YouTube search, Calculator, Clock, Play Store, Maps)
19 screen reads cost **~2,700 tokens**, versus **~28,500** as screenshots. See [BENCHMARK.md](BENCHMARK.md).

## Requirements

- An Android phone with Developer options (Android 11+ for wireless; any version with a USB cable)
- Python 3.10+ and `adb` (Android platform-tools) on the computer — or Termux on the phone
- No other dependencies. Optional: Pillow (smaller fallback screenshots) and Tesseract
  (reads text from apps that expose none, e.g. games; set `AA_OCR_LANG=eng+deu` etc.)

## Quick start — from a computer (easiest)

1. Install adb:
   - Windows: `winget install Google.PlatformTools`
   - macOS: `brew install android-platform-tools`
   - Linux: `sudo apt install adb`
2. On the phone: *Settings → About phone →* tap *Build number* 7 times, then
   *Developer options →* turn on **USB debugging**.
   Xiaomi / Redmi / POCO: also **USB debugging (Security settings)** and **Install via USB**.
3. Plug the phone in with a data cable and tap **Allow** on the phone.
4. Run:
   ```sh
   git clone https://github.com/nebigoktug/android-agent
   cd android-agent
   python setup.py
   ```
   Setup finds the phone, remembers it, offers to install ADB Keyboard (for non-English text)
   and to register the MCP server with Claude Code.

## Quick start — on the phone itself (Termux, no PC)

1. Install **Termux** from F-Droid (the Play Store version is outdated).
2. In Termux:
   ```sh
   pkg install -y git python android-tools
   git clone https://github.com/nebigoktug/android-agent && cd android-agent
   python setup.py
   ```
3. Turn on **Wireless debugging** in Developer options. For the one-time pairing, put Termux and
   Settings in **split screen** (the pairing code disappears if you leave Settings), choose
   *Pair device with pairing code*, and type the address and code into setup.

The wireless port changes after a reboot; android-agent tries to find the phone again on the local
network by itself, and you only need to pair once.

## Using it with an AI agent

**Claude Code:** setup can register it, or:
```sh
claude mcp add phone -- python /path/to/android-agent/mcp_server.py
```
Also copy `SKILL.md` into `~/.claude/skills/android-agent/` — it teaches the agent the cheap way to
use the tools and when it must ask you first.

**Other MCP clients (Cursor, Claude Desktop, …):** add a stdio server with the command
`python /path/to/android-agent/mcp_server.py`.

Tools: `screen`, `tap`, `type`, `swipe`, `key`, `open_app`, `open_link`, `list_apps`, `wait`,
`screenshot`, `rotation_lock`.

## Let a model do the whole task (experimental)

`agent.py` runs the loop itself: give it a task in plain language.

```sh
pip install anthropic && export ANTHROPIC_API_KEY=...
python agent.py "turn on Bluetooth and tell me which devices are paired"

# or any OpenAI-compatible endpoint (Gemini, Groq, OpenRouter, a local Ollama, ...)
export OPENAI_API_KEY=...
python agent.py --provider openai --base-url https://generativelanguage.googleapis.com/v1beta/openai/ \
                --model gemini-2.5-flash "what are my last 5 notifications about?"
```

It asks you in the terminal before anything irreversible, prints each step, and reports tokens used.

## Using it by hand

```sh
python phone.py screen                 # what is on screen (then only changes)
python phone.py tap 5                  # by number from the last screen read...
python phone.py tap "Bluetooth"        # ...or by label, matched on the live screen
python phone.py tap -t 7               # by text even when it is a number (keypads)
python phone.py find "Developer options"          # scrolls until it is on screen
python phone.py wait-for "Sent" 20     # waits until it appears
python phone.py type "hello" , key enter          # chain commands with a lone comma
python phone.py open youtube --fresh   # open an app at its home screen
python phone.py link "geo:0,0?q=Eiffel+Tower"     # deep links skip many taps
python phone.py notifications         # what is new, without opening any app
python phone.py status                # battery, screen, front app, keyboard, network
python phone.py swipe up
python phone.py record yt , open youtube --fresh , tap Search , type "{q}" , key enter , stop
python phone.py play yt q=lofi          # replays without the model: zero tokens
python phone.py ocr                    # games/Flutter: text from the image, still tappable by number
python phone.py shot                   # small screenshot, only when needed
python phone.py help
```

## Optional: companion app (7× faster, no keyboard switching)

The `companion/` folder is a small Android app with an accessibility service. When it is on,
screen reads take ~0.4 s instead of ~3 s, it works while videos play, and text in any language is
typed directly. It is **optional**: everything above works without it.

- It listens only inside the phone (127.0.0.1:7912) and answers only requests with your private key.
- It shows a list of every action it performed, and a switch to pause the assistant.
- A small **status light** in the corner: green while the assistant acts, yellow when idle, red when
  it is waiting for your OK (or something failed), grey when paused. The system accessibility
  button works as an emergency stop (tap to pause / resume).
- Accessibility is a sensitive permission — the app explains on its first screen what it can see.

Install the APK from [Releases](https://github.com/nebigoktug/android-agent/releases/latest), follow the 3–4 steps on its screen, tap
**Copy key**, then run `python setup.py --service` and paste the key. To go back to plain adb,
delete `~/.config/android-agent/service.json` or set `AA_NO_SERVICE=1`.

## Safety and privacy

- **Blind-tap guard:** before every tap the screen is re-read; if you switched apps, opened the
  notification shade, or the button moved or disappeared, android-agent stops instead of tapping
  the wrong thing.
- **Ask first:** `SKILL.md` tells the agent to ask you before sending messages, paying, deleting,
  installing, or changing account settings.
- **Your keyboard stays yours:** ADB Keyboard is enabled only while typing non-English text, then
  your keyboard is restored and ADB Keyboard is disabled again.
- **Where data goes:** screen text goes only to the AI agent you connect (and its provider).
  android-agent itself sends nothing anywhere. Secure screens (banking apps) appear empty — by design.

## Troubleshooting

| Problem | Fix |
|---|---|
| `unauthorized` in `adb devices` | Unlock the phone and tap **Allow** on "Allow USB debugging?" |
| Taps do nothing / `INJECT_EVENTS` error | Xiaomi: turn on **USB debugging (Security settings)** |
| `INSTALL_FAILED_USER_RESTRICTED` | Xiaomi: turn on **Install via USB**, retry and accept on the phone |
| "could not read the screen" | The screen is locked or animating — unlock it; reads are retried automatically |
| Wireless connection lost | Keep Wireless debugging on; if it does not reconnect, run `python setup.py` again |
| An app looks wrong in landscape | `python phone.py lock` (pins portrait), `unlock` restores your setting |
| No phone over USB | Use a data cable (not charge-only); try another port |

## Status

Early (v0.4). Tested on a Xiaomi with Android 16 (Termux, wireless). Device-free tests run on
Windows, macOS and Linux in CI. Reports from other phones are very welcome — please open an issue
with your phone model and Android version.

## License

MIT. ADB Keyboard (optional, installed by setup) is GPL-2.0, by senzhk.
