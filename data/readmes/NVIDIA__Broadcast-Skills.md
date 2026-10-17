# NVIDIA Broadcast Skills

Agent skills that let an AI agent drive [NVIDIA Broadcast](https://www.nvidia.com/broadcast-app/) — applying AI effects to your camera, microphone, and speaker, processing local media files, and managing devices — through the local MCP gateway that NVIDIA Broadcast exposes on loopback.

![Platform: Windows](https://img.shields.io/badge/platform-Windows-blue)
![Requires: NVIDIA Broadcast 2.3.0+](https://img.shields.io/badge/NVIDIA%20Broadcast-2.3.0%2B-76B900)
![License: CC-BY-4.0 AND Apache-2.0](https://img.shields.io/badge/license-CC--BY--4.0%20AND%20Apache--2.0-lightgrey)

## Skills

| Skill | What it does | Version |
|---|---|---|
| [`nvidia-broadcast`](skills/nvidia-broadcast/) | Apply and tune AI effects, process local media files, select devices, and change camera resolution over MCP | 1.0.0 |

This repository is a home for NVIDIA Broadcast agent skills.

## What you can do

Once the skill is installed, you ask your agent in plain language and it drives Broadcast for you:

> What NVIDIA Broadcast effects are currently enabled?

> Turn on microphone noise removal and blur my background to 70%.

> Explain the available microphone effects and recommend one for a video call.

> List my cameras, then switch to `<camera name>` at 1080p and 60 fps.

> Process `C:\path\to\my\videos\clip.mp4` with video noise removal and Studio Voice.

Under the hood that covers:

| Capability | Detail |
|---|---|
| **Live AI effects** | Toggle and tune camera, microphone, and speaker effects — several at once in a single call |
| **Local file processing** | Apply the same effects to local media files, individually or as a tracked batch, with pause, resume, cancel, and retry |
| **Device control** | List available cameras, microphones, and speakers, and switch the active one |
| **Camera resolution** | Change resolution and frame rate, on its own or together with a device switch |
| **Guided install** | Offer to install or update NVIDIA Broadcast when it is missing or too old — only after you explicitly say yes |

### Effects

The app decides what is actually available on your machine, and the gateway advertises the live list on connect. These are the effects the skill knows about:

**Camera** — background blur, background replace, background remove, virtual key light, vignette, video noise removal, video super resolution, video frame generation, eye contact, auto frame

**Microphone** — noise removal, room echo removal, studio voice

**Speaker** — noise removal, echo removal

Most effects take parameters, such as `strength` on background blur or `warmth` on the virtual key light. Your agent reads the exact IDs, parameters, and ranges from the running app rather than guessing.

## Requirements

- **Windows** with an NVIDIA RTX GPU
- **[NVIDIA Broadcast](https://www.nvidia.com/broadcast-app/) 2.3.0 or later.** The MCP gateway first ships in 2.3.x — **2.2.x and older cannot be driven by this skill at all**, no matter how it is configured. If Broadcast is missing or too old, the skill can offer to install or update it for you.
- An **agent that supports skills and can act as an MCP client** over Streamable HTTP

## Install

**1. Install NVIDIA Broadcast 2.3.0 or later** from <https://www.nvidia.com/broadcast-app/>, if you do not have it already.

**2. Add the skill to your agent.** Clone this repository and copy the skill folder into wherever your agent loads skills from:

```bash
git clone https://github.com/NVIDIA/Broadcast-Skills.git
```

Then copy `Broadcast-Skills/skills/nvidia-broadcast/` into your agent's skills directory. Keep the folder intact — `SKILL.md`, `references/`, and `scripts/` are all used at runtime.

**3. Ask for something.** Start a new session and ask your agent to blur your background or clean up your mic. The skill walks it through starting Broadcast if needed, resolving the gateway port, and registering the connection itself.

### If your agent cannot register MCP servers at runtime

Some clients only load MCP servers from a config file at startup. Add the gateway to your MCP configuration and restart the client:

```json
{
  "mcpServers": {
    "nvidia-broadcast": {
      "type": "http",
      "url": "http://127.0.0.1:18100/gateway"
    }
  }
}
```

`18100` is the default and correct on almost every install. No API key or header is required. If that port was already taken, Broadcast uses the next free port in `18100`–`18109`; see [`references/connection.md`](skills/nvidia-broadcast/references/connection.md) for how to find the one it bound.

For a client that cannot use Streamable HTTP at all, Broadcast ships an stdio bridge. Open **Settings → AI Agent Resources** in NVIDIA Broadcast and copy the stdio command from there, so a non-default install location is handled correctly.

## How it works

NVIDIA Broadcast 2.3 and later run a Model Context Protocol server bound to loopback, and publish the port it actually bound in `%APPDATA%\nvidia-broadcast\gateway.json`.

The skill tells your agent how to find that port, register `http://127.0.0.1:<port>/gateway` as a Streamable HTTP MCP server, and confirm it is really talking to Broadcast before sending anything. From there the agent calls the gateway's tools directly.

What the skill adds is the operating knowledge around those tools: which effect IDs and parameters are real, how to batch several changes into one call instead of many, how to track a file-processing batch to completion, when to stop and ask you instead of guessing — and a firm set of rules about what never to do, such as reading effect state from saved settings files or reaching the gateway from a shell.

## Repository layout

```
skills/
  nvidia-broadcast/
    SKILL.md              The skill itself — rules, tools, and worked flows
    references/           Loaded on demand for detail
      connection.md         Endpoint discovery, startup, WSL, rate limits
      effects.md            Effect IDs, parameters, incompatibilities
      examples.md           Complete tool-call examples
      file-processing.md    File and batch workflow
      installation.md       Consent, download, and verification flow
      troubleshooting.md    Full symptom table
      mcp-tool-contract.md  Complete public tool contract
    scripts/
      launch_broadcast.ps1  Starts NVIDIA Broadcast hidden and detached
CONTRIBUTING.md
LICENSE
```

The skill folder also carries evaluation artifacts used during development. Only the files listed above matter at runtime.

## Troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| Your agent reports Broadcast tools are unavailable | The MCP connection was never established | Restart your agent and retry. If it persists, confirm Broadcast is installed and check its version |
| Connection refused, and you are running in WSL | NAT-mode WSL has its own loopback | Switch WSL to mirrored networking, or run your agent on Windows |

The full symptom table, including error codes and recovery paths, is in [`references/troubleshooting.md`](skills/nvidia-broadcast/references/troubleshooting.md).

## Contributing

This project is not currently accepting contributions. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

See [LICENSE](LICENSE).

Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
