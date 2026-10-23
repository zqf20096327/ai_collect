# Hermes Local Starter

A beginner-friendly installer for a **local Hermes Agent + Ollama + Qwen 3.5 9B** setup on Ubuntu/Debian-based Linux desktops, including Zorin OS.

## What it does

1. Checks the Linux distribution and basic prerequisites.
2. Installs Ollama from its official installer if it is missing.
3. Enables and starts the Ollama system service.
4. Downloads `qwen3.5:9b` using `ollama pull`.
5. Installs Hermes Agent for the current user using the official Hermes installer in non-interactive mode if it is missing.
6. Configures Hermes to use Ollama's local OpenAI-compatible endpoint at `http://127.0.0.1:11434/v1`.
7. Runs verification checks and `hermes doctor`.

It does not bundle or copy anyone's personal data, API keys, chat history, or existing configuration into this repository. If `~/.hermes/config.yaml` already exists, the installer makes a timestamped backup before changing the model/provider fields.

## Requirements

- Ubuntu/Debian-based Linux desktop (Ubuntu, Linux Mint, Zorin OS, etc.).
- Normal user account with `sudo` access.
- Internet access for the installers and model download.
- At least 12 GB free disk space recommended; more is better.
- **16 GB RAM recommended** for Qwen 3.5 9B. Performance depends on CPU, GPU, VRAM and context size. A smaller model may be needed on low-memory computers.

The installer currently expects `systemd` and an `ollama.service`. It is not a native Windows/macOS installer and does not support WSL without systemd or every Linux distribution.

## Install

From a terminal opened in this repository:

```bash
chmod +x install.sh verify.sh
./install.sh
```

Do **not** run the whole script with `sudo`; Hermes should be installed under the normal user's account. The script requests sudo for system-level installation when needed.

The first model download is several gigabytes and can take a while.

## Verify and use

```bash
./verify.sh
ollama list
ollama run qwen3.5:9b
hermes
```

Installer log: `~/.local/state/hermeslocal/install.log`

## Re-running

The script skips Ollama/Hermes installation if their commands already exist and does not delete existing models or configuration. It reuses the existing model if Ollama has it and backs up the Hermes config before changing model settings. It is intended for a personal workstation, not unattended fleet deployment.

## What it does not do

- Does not create or include API keys.
- Does not expose Ollama to the network.
- Does not install a HUD or voice assistant.
- Does not guarantee that the 9B model will run quickly on every computer.
- Does not uninstall existing software or delete existing models/configuration.

## Official documentation

- Hermes installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation/
- Hermes model providers: https://hermes-agent.nousresearch.com/docs/integrations/providers/
- Ollama Linux installation: https://github.com/ollama/ollama/blob/main/docs/linux.mdx
