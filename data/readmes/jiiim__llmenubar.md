<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jiiim/llmenubar-arr/main/images/banner-white-text.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/jiiim/llmenubar-arr/main/images/banner-black-text.png">
    <img src="https://raw.githubusercontent.com/jiiim/llmenubar-arr/main/images/banner-black-text.png" width="640" alt="LLMenuBar - jiiim/llmenubar">
  </picture>
</p>

# LLMenuBar

## Overview

LLMenuBar is a lightweight, native macOS menu bar app that starts, stops, and configures a local inference engine that you install separately. It currently supports the [Splash](https://github.com/incoai/splash) inference engine.

<p align="center">
  <img src="https://raw.githubusercontent.com/jiiim/llmenubar-arr/main/images/menu-bar-menu-00A.png" width="438" alt="LLMenuBar menu">
</p>

## Why LLMenuBar

Splash has its own desktop app. LLMenuBar is a menu bar app that runs `splash serve` instead.

- **Ultralight.**
  - **Memory efficient:** After opening and closing its windows and serving a model, LLMenuBar's memory usage peaked at 65 MB, while Splash.app 1.6.1 peaked at 358 MB.
  - **No baked-in chat window:** Use a web chat in your browser, where you can control font sizes and other preferences.
  - **No baked-in terminal window:** Run a full-featured terminal app, your own agent, or both.
  - **No baked-in log viewer:** One click opens the log in macOS's Console.app.
- **Out of the way.** LLMenuBar has no Dock icon and does not appear in the Command-Tab switcher unless one of its windows is open.
- **A real Mac menu.** LLMenuBar's menu works as Mac menus have worked since 1984: click the menu bar icon, drag to an item, and release. One click opens the chat page in your browser, and the menu provides many other features.
- **Speed at a glance.** LLMenuBar can keep the generation speed visible at a glance — with zero clicks — while you remain focused in your agent, editor, or application of choice.
- **Every Splash option.** All `splash serve` options are available — including draft model, vision projector, local model name, revision, and offline mode. The General pane shows the exact command it runs.
- **Your own Splash.** Use Homebrew's `splash`, a source checkout, or Splash.app's runtime. The desktop app does not need to be installed.
- **Logs and environment.** Configure the log folder and log size, enable crash traces, or add extra environment variables for the engine.
- **Copy settings with ease.** One click copies the OpenAI or Anthropic endpoint, your API key, or any of your model names.
- **Settings applied in one step.** Edit settings, press **Apply**, and the engine restarts with the updated command.
- **A considered, Mac-native design.** Every configuration option is logically grouped into coherent Settings panes.
- **Secrets secured in Keychain.** If you set a Hugging Face access token for private or gated models or a server API key, those secrets are stored in the macOS Keychain.

## Requirements

- macOS 26 or later on an Apple silicon Mac.
- Splash, installed or built separately: the Splash desktop app, the `splash` command installed with `brew install incoai/tap/splash`, or the `splash` executable from a source checkout. See the [Splash project](https://github.com/incoai/splash) for its requirements.

LLMenuBar 0.0.6 is known to work with Splash 1.6.1, 1.7.0, 1.7.1, 1.7.2 and 1.7.3 and may work with newer releases.

## Install

Both methods install the same signed and notarized build. Homebrew is recommended because it also handles updates.

### Homebrew (Recommended)

```sh
brew install --cask jiiim/tap/llmenubar
```

The cask requires an Apple silicon Mac running macOS 26 or later and refuses to install elsewhere.

#### Updating

Refresh Homebrew's copy of the tap, then upgrade to install the newest release:

```sh
brew update
brew upgrade --cask llmenubar
```

The upgrade does not quit LLMenuBar or stop the `splash` process it manages. The running app keeps serving until you quit and reopen it; the new version starts on relaunch. Your settings, including the selected executable and model, are stored outside the app bundle and survive the upgrade.

### DMG

1. Download the DMG and its `.sha256` file from the [latest release](https://github.com/jiiim/llmenubar/releases/latest).
2. Optional: verify the download from the directory containing both files, in Terminal:

   ```sh
   shasum -a 256 -c LLMenuBar-vX.Y.Z-arm64.dmg.sha256
   ```

3. Open the DMG and drag **LLMenuBar** onto the **Applications** shortcut.
4. Open **LLMenuBar** from `/Applications`.

## Initial Setup

The first time LLMenuBar opens, it asks for two things before starting anything: the inference engine to run and the model to serve. Everything here can be changed later in Settings.

- **Inference Engine.** Homebrew's `splash` and `Splash.app` are listed when they are installed, each with its version and a **Use** button. If an engine is not installed, its item shows how to get it: a copyable `brew install` command or a link to Splash's releases. **Another location** accepts any `splash` executable, such as the one from a source checkout, or a `Splash.app` located elsewhere.
- **Large Language Model.** Enter a Hugging Face model as `owner/repo`, optionally followed by `:VARIANT`, or pick one from **Suggestions**, which lists our recommended model for each supported Apple silicon memory configuration, from 24 GB up to your Mac's memory. For a private or gated model, optionally add an access token. Or choose **On this Mac** and select a GGUF file or a local model folder.
- **Download location.** For a Hugging Face model, this shows the download folder, the free space there, and whether the model fits. If your shell profile sets a Hugging Face location, it is detected once here and saved with your choices.

**Continue** becomes available once both choices work, and it tells you what is missing until then.

<p align="center">
  <img src="https://raw.githubusercontent.com/jiiim/llmenubar-arr/main/images/set-up-llmenubar-00A.png" width="574" alt="Set Up LLMenuBar Window">
</p>

## Settings

The Settings window keeps a draft until you press **Apply**; closing it or pressing **Revert** drops the draft. Applying while Splash is running restarts it so the new command takes effect.

- **General**: the `splash` executable or `Splash.app` and its version, general app behavior, whether the Mac may sleep while the engine answers, extra environment variables for the engine, the command preview, and a way to reset all Splash options.
- **Model**: Hugging Face or local files; a vision projector and draft folder for local files; a revision, an access token, and a draft repository for Hugging Face; the Hugging Face download location, with free space and whether the chosen model fits; text-only mode; a chat template of your own; and offline mode.
- **Server**: whether Splash listens on this Mac only, on every network, or on a UNIX socket, the port, extra hostnames and web origins, and the browser chat page.
- **Memory**: memory and context limits, how long an idle model stays loaded, streaming from the SSD, KV-cache, recurrent-state, cached-state, and activation precision, and Neural Engine use and recalibration.
- **SSD Cache**: the cache size, its daily write budget, and whether it is kept across restarts.
- **API**: the OpenAI and Anthropic endpoints to copy, including this Mac's network names when Splash listens on every network, an optional API key (requested in the browser chat sidebar), and the model names clients may request, including local file names.
- **Requests**: the thinking effort, for requests that set none or for every request, request limits, how many requests run at once, how the engine schedules them, and sampling defaults for requests that set none.
- **Diagnostics**: where the log is kept and how large it may grow, and a switch to make the engine record a crash trace.

<p align="center">
  <img src="https://raw.githubusercontent.com/jiiim/llmenubar-arr/main/images/settings-general-00A.png" width="688" alt="Settings | General Pane">
</p>

## Uninstall

Disable **Launch at login** in Settings and quit LLMenuBar first, then remove the app. An uninstalled app that is still running keeps its server alive.

For a Homebrew installation:

```sh
brew uninstall --cask llmenubar
```

For a DMG installation, move `/Applications/LLMenuBar.app` to the Trash.

Neither method touches your `splash` executable or your models, and neither removes LLMenuBar's settings, log, or keychain items.

### Removing Settings, Secrets, and the Log

To remove LLMenuBar's settings, secrets, and log, quit LLMenuBar from its menu and wait until its icon leaves the menu bar (it stops the engine first). Then run the commands below. If you changed the log folder in Settings → Diagnostics, use that path in the last command.

```sh
defaults delete com.jiiim.llmenubar
security delete-generic-password -s com.jiiim.llmenubar -a api-key
security delete-generic-password -s com.jiiim.llmenubar -a huggingface-token
rm -ri ~/Library/Logs/llmenubar
```

That preferences domain holds the settings, the recent paths, and the saved menu bar position. The API key and the Hugging Face token are items in your login keychain, and the two `security` commands remove them; either one reports that the item could not be found if you never set it. The log folder holds the captured engine log. If you reinstall afterwards, LLMenuBar starts with the setup window, as for a new user. The same commands, run without uninstalling, reset the app to that state.

A copy of LLMenuBar run directly from a source build keeps its settings in a second domain, which `defaults delete llmenubar` removes.

macOS keeps its Login Items and Notifications permission records separately; these commands do not change them. Turn **Launch at login** off in Settings first, or remove LLMenuBar under System Settings → General → Login Items.

## Bug Reports and Feature Requests

LLMenuBar accepts bug reports and feature requests as [GitHub Issues](https://github.com/jiiim/llmenubar/issues). See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Build from Source

Build your own copy to audit, modify, or fork the source. Building requires macOS 26, an Apple silicon Mac, and the Xcode Command Line Tools.

```sh
make test
make bundle
```

`make test` runs the test suite. `make bundle` writes the debug app to `.build/debug/LLMenuBar.app`, and `make run` builds it and opens it.

To build a release app and install it in `/Applications`:

```sh
make install
```

If LLMenuBar is running, `make install` asks it to quit and waits until it has exited before replacing it. Quitting stops the engine first, so the wait can take a while. Press Control-C to cancel the install.

Source builds use an ad hoc signature and are intended for local use.

## License and Trademarks

The LLMenuBar source code and original bundled assets are available under the MIT License. Copyright James Martin.

"LLMenuBar" and the LLMenuBar logo are trademarks not covered by that license; see [TRADEMARKS.md](TRADEMARKS.md).

Splash, GGUF models, macOS, and Xcode are separate works and are not distributed under this project's license. Refer to their respective terms and licenses.
