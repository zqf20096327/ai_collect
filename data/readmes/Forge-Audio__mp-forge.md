<p align="center">
  <img src="app/icons/icon.png" alt="The MP Forge logo: the word FORGE across a grid of sixteen red pads" width="192">
</p>

<h1 align="center">MP Forge</h1>

<p align="center">
  <b>Make plugins for your MPC creatively.</b><br>
  A free, open-source desktop app for Akai MPC hardware.
</p>

<div align="center">

[![GET STARTED][get-started-button]][get-started]

[**Get started**][get-started] · [Website][website] · [Download][download] · [Watch the trailer][trailer] · [What you need][what-you-need] · [The safety checks][safety-checks] · [Where it stands][status]

<img src="docs/public/images/top-bar.svg" alt="MP Forge: free and open source, plugins for Akai MPC. Status: safe to send." width="816">

</div>

## What it is

MP Forge is a desktop app for making your own instruments and effects for the Akai MPC. Start from your own
idea, remix an open plugin, or press I'M FEELING LUCKY, and an AI of your choice builds it with Akai's own MPC
Plugin SDK.

You play the real plugin on your computer straight away, and shape its sound and its screen until it is yours.
MP Forge runs twelve safety checks on it, then sends it to your MPC. There is no code to write and no build
tools to install.

<p align="center">
  <img src="docs/src/assets/bille-tumbler-finished.png" alt="MP Forge with a finished plugin open, an effect called Bille Tumbler. On the left is the conversation: the plugin was built, its knobs were made to glow violet on request, and it was sent to an MPC. On the right is the plugin's MPC screen, a pyramid tumbling over a floor above violet knobs, with the play, send and edit buttons above it and the sixteen hardware knobs beside it. The status reads SAFE TO SEND." width="880">
</p>

<p align="center"><img src="docs/public/images/step-row.svg" alt="" width="250"></p>

## How it works

<table>
  <tr>
    <td align="center" valign="top" width="25%">
      <img src="docs/public/images/step-describe.svg" alt="" width="68"><br>
      <b>1. DESCRIBE IT</b><br>
      Say what you want as you would to a friend: "a worn tape echo that gets seasick when I turn it up".
    </td>
    <td align="center" valign="top" width="25%">
      <img src="docs/public/images/step-build.svg" alt="" width="68"><br>
      <b>2. BUILD IT</b><br>
      The AI writes the plugin. MP Forge builds it for every MPC and runs twelve safety checks on it.
    </td>
    <td align="center" valign="top" width="25%">
      <img src="docs/public/images/step-play.svg" alt="" width="68"><br>
      <b>3. PLAY IT</b><br>
      See its screen as it will look on the MPC and play the real plugin. Ask for changes until it is right.
    </td>
    <td align="center" valign="top" width="25%">
      <img src="docs/public/images/step-send.svg" alt="" width="68"><br>
      <b>4. SEND IT</b><br>
      Once it is safe to send, it goes over your network to a USB drive or SD card in your MPC.
    </td>
  </tr>
</table>

<p align="center"><img src="docs/public/images/step-row.svg" alt="" width="250"></p>

## What it can do

- **Instruments and effects.** Each has a touch screen of pages with knobs, faders and switches, artwork,
  presets, and controls mapped to the MPC's sixteen hardware knobs. A plugin can play sound files you add.
- **The AI you choose.** Claude, ChatGPT, OpenAI, Google, xAI, Mistral, DeepSeek or OpenRouter through your
  own account, or models that run on your own computer through Ollama, with no account at all.
- **Twelve safety checks.** MP Forge reads the plugin's code, builds it with Akai's tools and plays it through
  Akai's simulator. A plugin that does not pass cannot be sent.
- **See it and hear it first.** The plugin's screen is shown as it will look on the MPC. The real plugin plays
  through your speakers, with a piano for an instrument and a beat or a sound of your own for an effect.
- **Change it by asking.** A version is kept before every change, and you can go back to any of them.
- **Edit the look by hand.** Move, resize and restyle the controls, and add your own artwork.
- **Starting points.** I'M FEELING LUCKY builds a surprise. REMIX A PLUGIN starts from a plugin in the Open
  MPC catalog. The plugin architect asks you a few questions first.
- **Share what you make.** Export a plugin's project as one file and hand it to another musician, who brings
  it into their own MP Forge and carries on from there.
- **Sent the careful way.** A plugin goes onto a USB drive or SD card in the MPC, never onto its built-in
  storage, so pulling the drive out always takes the plugin away again.

<p align="center"><img src="docs/public/images/step-row.svg" alt="" width="250"></p>

## Get MP Forge

1. Download MP Forge for macOS, Windows or Linux from the [download page][download].
2. Install it and open it. MP Forge checks what it needs on your computer and fetches Python and Akai's
   build tools itself if they are missing. There is nothing else to install.
3. Follow [Get started][get-started] from there: pick an AI, make your first plugin, check it and send it.

What you need besides MP Forge itself:

| | |
| --- | --- |
| **An AI** | An account with an AI service, or Ollama for models on your own computer. |
| **An MPC** | Running MPC OS 3.10.1 or later, with External Plugin Support switched on under Preferences → Enhancements (Beta), and a USB drive or SD card in it. |

[What you need][what-you-need] has the full list.

<p align="center"><img src="docs/public/images/step-row.svg" alt="" width="250"></p>

## Where it stands

- **Version 0.1.5 is out**, with installers for macOS, Windows and Linux on the [download page][download].
  They are not signed yet, so macOS and Windows each warn the first time MP Forge is opened.
  [Getting started][get-started] says what to do.
- **Written on a Mac, and tested by hand on a Mac and on Windows.** Linux is tested by automated tests so
  far, not yet by hand.

[Where MP Forge stands][status] has more.

## Join in

- **Talk to us** on the [Forge Audio Discord][discord]: get help, show the plugins you have made, and ask for
  what MP Forge is missing.
- **Keep it going.** MP Forge is free and stays free. If it is useful to you, a donation on
  [Ko-fi][donations] helps.

<p align="center">
  <a href="https://ko-fi.com/forgeaudio"><img src="docs/public/images/donate-on-ko-fi.svg" alt="Donate on Ko-fi" width="314"></a>
</p>

## Build from source

For developers. MP Forge is a Tauri 2 app with a Rust engine, and builds with Rust, Git and Python 3.

```sh
git clone https://github.com/Forge-Audio/mp-forge.git
cd mp-forge
./scripts/check-sdk.sh    # fetches Akai's SDK at the version in sdk.pin and proves it works here
cd app
cargo run
```

[Building from source][building-from-source] has every step, Windows and the tests included.

| Folder | What it holds |
| --- | --- |
| `app/` | The desktop app, built with Tauri 2. Its screen is plain JavaScript, in `app/ui/`. |
| `engine/` | The Rust engine: the safety checks, the AI's work, building, playing and sending. |
| `directives/` | The instructions the AI is given. |
| `screen-tests/` | Test plugins for trying out what an MPC's screen supports. |
| `scripts/` | `check-sdk.sh`, which fetches Akai's SDK and checks it. |
| `docs/` | The docs site. `npm install` and `npm run dev` in that folder show it on your computer. |

## Licence

MP Forge is free and open source, under the [GNU General Public License, version 3 or later](LICENSE).

## Not made by Akai

MP Forge is an independent tool made by Forge Audio. It is not affiliated with, sponsored by or endorsed by
Akai Professional or inMusic Brands. MPC and Akai are trademarks of their owners.

[get-started]: https://forge-audio.github.io/mp-forge/getting-started/
[what-you-need]: https://forge-audio.github.io/mp-forge/what-you-need/
[safety-checks]: https://forge-audio.github.io/mp-forge/safety-checks/
[status]: https://forge-audio.github.io/mp-forge/status/
[building-from-source]: https://forge-audio.github.io/mp-forge/building-from-source/
[website]: https://forge-audio.github.io/mp-forge/
[download]: https://forge-audio.github.io/mp-forge/download/
[trailer]: https://youtu.be/mRqsBG5l61k
[discord]: https://discord.gg/EWkFTAEgJr
[donations]: https://ko-fi.com/forgeaudio
[get-started-button]: docs/public/images/get-started.svg
