# <img src="CodexPing/Assets.xcassets/AppIcon.appiconset/logo_1024.png" alt="CodexPing logo" width="160" style="border-radius: 22%;">

# CodexPing

https://github.com/user-attachments/assets/b112f62c-7d78-45dd-8589-2c567ba40b12

Tired of switching back to Codex only to realise it’s been waiting on your input?

CodexPing is a small macOS status app that keeps a floating overlay in sync with Codex activity — even when you’re not using the Codex app directly (like when you’re in VS Code with the extension). It makes sure you never miss when Codex is waiting on you.

Free to use! The only condition is that you leave a star on the repo ⭐️

It listens to the status of your Codex chat and shows one of four states:

- `Working`
- `Needs Input`
- `Done`
- `Idle`

When the app is configured correctly, the overlay appears across spaces and updates automatically as Codex runs.

## Features

- Floating always-on-top overlay that works across macOS Spaces
- One-click setup installer for the required Codex hook configuration
- Animated visuals for each state
- Audible chime when Codex is done or awaiting input.
- Fades out when unused

## Setup

### Requirements

- macOS
- Xcode
- Codex installed locally

### Download latest release

1. Download the latest .dmg release.
2. Drag into your Applications folder.

### Run from Xcode

1. Clone this repository.
2. Open `CodexPing.xcodeproj` in Xcode.
3. Select the `CodexPing` scheme.
4. Build and run the app.

### Configure Codex hooks

When the app launches, it checks whether Codex hooks are set up.

If setup is incomplete, open the app, select the your `.codex` directory (usually in `~/.codex`) and use **Install Recommended Setup**. This will:

- enable codex hooks
- write or update `~/.codex/hooks.json` with the recommended status hooks

## Usage

1. Launch CodexPing.
2. Confirm the setup screen shows all requirements as satisfied.
3. Start a Codex session.
4. Watch the overlay update as Codex moves through working, waiting for input, and finishing.

The overlay stays visible only when setup is complete. If hooks are missing, the setup screen is shown instead.

## Contributing

Contributions are welcome. A good workflow is:

1. Open an issue or describe the change you want to make.
2. Make the change in a small, focused branch.
3. Add or update tests where it makes sense.
4. Verify the app still builds and the UI behaves correctly.

If you plan to contribute code, please keep the overlay behavior and setup flow aligned with the existing app design.

## Acknowledgements

Created by Kane Testa.
