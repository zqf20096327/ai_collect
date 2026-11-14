<p align="center">
  <a href="https://opencyclone.vercel.app"><img src="website/brand/poster.png" alt="OpenCyclone. Don't buy an AI phone. Repurpose the one you have." width="100%"></a>
</p>

<h1 align="center"><img src="website/brand/logo.png" alt="" width="36" align="top"> OpenCyclone</h1>

<p align="center"><a href="https://opencyclone.vercel.app">Website</a> · <a href="#install">Install</a> · <a href="INSTALL-WITH-AI.md">Install with an AI agent</a> · <a href="https://github.com/Exorust/opencyclone/releases">Releases</a></p>

An open-source AI agent for a stock Android phone. You say or type what you need. The phone does it in your own apps, in the background, and asks you before it sends, pays, or deletes anything.

OpenCyclone needs no special phone and no changed system. It runs on Android 12 or later as a normal app.

## What it does

- **Tasks in your apps.** "Tell the group chat I'm running ten minutes late." The agent opens the app on a hidden display, reads the screen, and taps and types as a person does. Your visible screen stays free.
- **One approval before anything leaves.** Before a tap on Send, Pay, Delete, or a button it cannot read, the task stops. You see the recipient, the exact text or the attached items, and two buttons, for example "Send to Alex" and "Not now".
- **Notifications handled for you.** "Handle my notifications for the next hour." A message that asks for something becomes a prepared task that waits for your approval. Rules in plain words: "Hide NordVPN notifications."
- **Apps built on request.** "Build me an app to learn Spanish." The phone asks what matters, writes a small app, tests it, and puts it on your home page. Change it by asking. Share it as one file.
- **Widgets.** "Make a widget that shows my streak and how many tasks I ran today." You see a draft with live data, change it by asking, and save it.
- **History.** Swipe right for every past task with its approval, its result, and "Ask again".
- **Voice.** Tap to talk, or hold the power button if you make OpenCyclone the phone's assistant. Speech is recognised on the phone by default.
- **Your choice of model.** Sign in with ChatGPT or OpenRouter, use your own key, or use a model on your own network.
- **A home screen, if you want one.** The page can replace your launcher. This is optional.

## How it works

| Part | What it does |
|---|---|
| Helper process | A small process with the rights of Android's developer shell. It creates a hidden display, starts apps on it, and sends taps and text. It is started once through wireless debugging, in the way Shizuku does it. No root. |
| Accessibility service | Reads the buttons, fields, and texts of the hidden display. |
| Agent loop | Each step sends a picture and a numbered list of screen elements to the model. The model answers with one action. The app waits until the screen is quiet, checks the result, and repeats. |
| Approval gate | Code, not a prompt. It inspects every action before it runs. The model cannot skip it. |
| Notification listener | Reads incoming notifications. One-time codes and notifications from protected apps are dropped before the model sees anything. |

## Safety

- Every action that commits something is held for your approval: a tap on a button with a word such as Send, Pay, Order, Delete, or Confirm; a tap on a button without a readable label; the Enter key in a text field; a call to a connected service that is not read-only; a direct phone call.
- When you approve, the app reads the screen again. If the recipient, the text, or the number of attached items changed, nothing is sent and you are asked again.
- An approval needs an unlocked phone.
- Banking apps, authenticators, password managers, and the phone's settings are never operated. You can add apps to this list.
- Text that comes from another person, in a message or on a screen, is treated as data. It cannot give the agent instructions that pass the gate.
- A task stops after 30 steps or 10 minutes, and when it repeats itself.

## Privacy

- Pictures of the hidden display and the text of your request go to the model you chose. Nothing else leaves the phone.
- Speech is turned into text on the phone by default. If you choose a voice service on the internet, the Privacy screen says where your voice goes.
- Model keys and sign-in tokens are stored encrypted with a key from the Android Keystore.
- Notification text is not kept after the day ends, unless it became a task.

## Requirements

- A phone with Android 12 or later. Development and tests use a Pixel 7 with Android 17.
- A computer with `adb` for the first setup.
- A model that accepts pictures and tool calls.

## Install

Release packages are not published yet. You build the app on a computer and install it over USB. This takes about 15 minutes the first time.

### The short way: let an AI coding agent do it

If you use an AI coding agent that can run commands on your computer (Claude Code, Codex, Cursor, Gemini CLI), connect the phone with a cable and give the agent this sentence:

```
Install OpenCyclone on my Android phone. Follow https://raw.githubusercontent.com/Exorust/opencyclone/main/INSTALL-WITH-AI.md
```

The agent checks your tools, gets the package, runs the setup script, reads each result, and tells you what to tap on the phone. It does not see your model key or your pairing code. The steps it follows are in [`INSTALL-WITH-AI.md`](INSTALL-WITH-AI.md). The manual steps follow.

### 1. What you need on the computer

- macOS, Linux, or Windows with a bash shell (WSL or Git Bash).
- Git.
- JDK 17. On macOS: `brew install openjdk@17`.
- The Android SDK with platform 36, and `adb` (Android platform tools) on your `PATH`. The simplest way is to install Android Studio and open the SDK Manager once. On macOS, `brew install --cask android-platform-tools` gives you `adb` alone.
- The SDK components NDK and CMake. Gradle downloads them on the first build if you accepted the SDK licences (`sdkmanager --licenses`).

### 2. Prepare the phone

1. Open **Settings > About phone** and tap **Build number** seven times. This turns on Developer options.
2. Open **Settings > System > Developer options** and turn on **USB debugging** and **Wireless debugging**. Wireless debugging needs a Wi-Fi connection.
3. Connect the phone to the computer with a USB cable and accept the "Allow USB debugging" question on the phone.
4. Run `adb devices`. The phone must appear with the word `device`.

### 3. Build

```bash
git clone https://github.com/Exorust/opencyclone.git
cd opencyclone/android
echo "sdk.dir=$HOME/Library/Android/sdk" > local.properties   # macOS default; on Linux it is usually $HOME/Android/Sdk
JAVA_HOME=<path to JDK 17> ./gradlew :app:assembleStandardDebug
cd ..
```

On macOS with Homebrew the JDK path is `/opt/homebrew/opt/openjdk@17`. The first build downloads Gradle and the libraries and can take 10 minutes. The package is written to `android/app/build/outputs/apk/standard/debug/app-standard-debug.apk`.

### 4. Install and grant the permissions

```bash
./setup.sh
```

The script installs the package and then turns on, over `adb`, the things the app cannot ask for itself: the accessibility service, notification access, the microphone, notifications, and the right to change secure settings. Each line of its output starts with `ok:` or `FAILED:`. If more than one device is attached, set `ANDROID_SERIAL` to the serial number from `adb devices`.

To let a long press of the power button open the listening screen, run `./setup.sh --assistant` instead.

### 5. First run on the phone

Open OpenCyclone. The first run has a few short steps:

1. **Connect once.** The app pairs with the phone's own wireless debugging and starts its helper process. Follow the steps on the screen. After this step you can remove the cable.
2. **Choose a model.** Sign in with ChatGPT or OpenRouter, enter your own key, or give the address of a model on your network.
3. **Permissions and voice.** Confirm what the script already granted and choose how speech is recognised.
4. **Try it.** Run a first request.

You can also make OpenCyclone your home app. This step is optional.

### After a restart of the phone

Android stops the helper process when the phone restarts. Open the app with Wi-Fi on and tap "Connect" again. You do not need the computer for this.

### Update and remove

- Update: `git pull`, build again, and run `./setup.sh` again. Your settings stay.
- Remove: `adb uninstall ai.opencyclone.standard`.

### If something fails

| What you see | What to do |
|---|---|
| `SDK location not found` | Create `android/local.properties` with the `sdk.dir=` line from step 3. |
| `FAILED: No device found` | Check the cable, accept the debugging question on the phone, and run `adb devices`. |
| `FAILED: More than one device` | Set `ANDROID_SERIAL=<serial number>` before `./setup.sh`. |
| `FAILED: Write secure settings` on a Xiaomi phone | Turn on "USB debugging (Security settings)" in Developer options and run the script again. |
| The app says "Not connected" | Turn on Wi-Fi and Wireless debugging, then tap "Connect" in the app. |

## Limits

- A task takes about 4 seconds for each step. A reply in a messaging app is 6 to 10 steps.
- Long tasks across several apps fail more often than short ones.
- One task runs at a time. Others wait.
- An app that marks its screen as secure cannot be read.
- The bundled speech model exists for 64-bit ARM phones only. Android's own recognizer is the default.
- With a third-party home app, Android's swipe animations and recent-apps screen are plainer on some phones.

## Development

```bash
cd android
./gradlew :app:testStandardDebugUnitTest      # unit tests
cd ..
tests/walk/walk.sh setup                      # scripted model for checks on a real phone, no paid model needed
tests/walk/walk.sh all
tests/walk/walk.sh look home_idle             # checks of a screen's look from a screenshot
```

## Credits and licence

OpenCyclone is a fork of [OpenCyvis](https://github.com/opencyvis/opencyvis-phone) at commit `3acd0a5`, by the OpenCyvis contributors. The helper process, the hidden display, and the first agent loop come from that project. The wireless-debugging code comes from Shizuku. See `NOTICE`.

Licence: Apache-2.0.

OpenCyclone is an independent project. It is not affiliated with Cyclon or with OpenCyvis.
