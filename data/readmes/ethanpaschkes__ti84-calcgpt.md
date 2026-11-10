# CalcGPT: ChatGPT and Fortnite on a TI-84 Plus CE

**A graphing calculator that answers questions with ChatGPT and streams games and websites.** A stamp-sized Wi-Fi board plugs into
the calculator's USB port and gets its power from the calculator. It talks to a small free program on your own computer. You type
with the calculator keys; answers type themselves onto the screen, and a game or a web page arrives as pictures. No soldering.

> ## Saw the video? Start here: **[TUTORIAL.md](TUTORIAL.md)**
> About $20 of parts, about an hour, written for people who have never used a terminal. Ready-made files, nothing to compile.
>
> **Test status, 10 November 2026:** the ready-made firmware was flashed onto a real board from the flasher page and read back
> identical. The full run of this public build on a real calculator is being done right now (until then it is proven on computers
> only), and Windows is untested. Details at the top of the tutorial.

<p align="center">
  <img src="docs/images/hero.jpg" alt="A TI-84 Plus CE showing a streamed game over the Wi-Fi board on its back" width="720">
</p>

![TI-84 Plus CE](https://img.shields.io/badge/calculator-TI--84%20Plus%20CE-0a7bbb)
![XIAO ESP32C6](https://img.shields.io/badge/wireless-XIAO%20ESP32C6-e7352c)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

| ![A ChatGPT answer on the calculator screen](docs/calcgpt-answer.jpg) | ![The board in a printed case on the calculator's back](docs/images/door-module.jpg) | ![A game streamed to the calculator](docs/images/fortnite-gameplay.jpg) |
|---|---|---|
| ChatGPT answering, word by word | A Wi-Fi board in a printed battery-door case (tape works too) | A game streamed to the calculator |

---

## Two ways to build it

| | **The tutorial build** (recommended) | The advanced build |
|---|---|---|
| Guide | **[TUTORIAL.md](TUTORIAL.md)** | [INSTALL.md](INSTALL.md) |
| Board | Seeed Studio **XIAO ESP32C6** (about $5 to $13) | ESP32-S3-DevKitC-1 or XIAO ESP32C6 |
| Server | Your own computer, same Wi-Fi. Free | Your own cloud server (Fly.io, about $2.50 a month): works from any network |
| Firmware | **Ready-made**: flash it from a web page | You build it, with your own server name and secret inside |
| Does | ChatGPT, games and websites as pictures, MATH | ChatGPT anywhere; pictures need a computer at home as well |
| You need to know | Nothing. Never used a terminal is fine | A terminal, and patience for a toolchain install |

Both need a **TI-84 Plus CE** (the colour-screen model; not the older TI-84 Plus or Silver Edition), a mini-USB **OTG** adapter, a
USB **data** cable and, for ChatGPT, your own OpenAI API key. Calculator OS 5.4 or older runs the programs directly; newer needs the
free [arTIfiCE](https://yvantt.github.io/arTIfiCE/) jailbreak, and has not been tested with these builds.

## What it really does (measured, not hoped)

On the real calculator with the XIAO ESP32C6: ChatGPT starts answering in 2 to 3 seconds. The picture stream carries about 47 KB a
second: about **5 pictures a second** at small size in 4 grays, 1.7 a second full screen, 0.6 a second in 240 colours. No sound. So
yes, Fortnite runs and you can play it, slowly. It needs your computer on and on the same Wi-Fi the whole time.

## Let an AI walk you through it

Copy this into ChatGPT, Claude or any assistant that can read web pages:

```text
Help me build the calculator from https://github.com/ethanpaschkes/ti84-calcgpt . I am a beginner. Read
https://raw.githubusercontent.com/ethanpaschkes/ti84-calcgpt/main/TUTORIAL.md and walk me through it ONE small step at a time.
Tell me what I should see after each step and wait for me to say it worked. Never ask me to paste a password or a key into the chat.
```

**Three rules:** never solder to the calculator; never paste a key or password into a chat, an issue or a file you share; and this is
a hobby project, **not for tests** or anywhere a teacher has not said yes.

## What it does

- **CALC** is a phone-style home screen with a passcode lock: Settings (Wi-Fi), ChatGPT, Math, Web, Sites and one tile per bookmark (Fortnite, YouTube, Wikipedia...). It shows a tile only when its program is on the calculator. The top bar says **Online** or **Offline**.
- **ChatGPT** streams answers and has 24 tools: exact maths done on the server, plus forms, choices and **drawn diagrams** on the calculator screen.
- **MATH** is a guided maths app (triangles with a to-scale drawing, quadratics, equations, unit circle, statistics). It needs no Wi-Fi.
- **REELS** is the picture viewer: a Chrome window on your computer, shaped to the calculator's screen, with the calculator's keys as mouse, keyboard or game controller (**stat** = game mode).
- In the source but not in the download: BROWSER (a text browser), CHAT (Messages on a Mac), CAMERA (a camera board) and LOADER (updates over Wi-Fi, switched off: it is not reliable yet).

## FAQ

The full FAQ (cost, other calculators, school, safety, why it is slow) is at the end of **[TUTORIAL.md](TUTORIAL.md#faq)**. The short version:

**Does it work on the TI-84 Plus Silver Edition or the plain TI-84 Plus?** No. Those use a different processor. It needs the TI-84
Plus **CE**.

**Is it allowed at school?** Ask your teacher. Using it on a test, quiz or exam is cheating. Do not bring it to an exam.

**What does it cost?** About $20 of parts. The server is free on your own computer. ChatGPT costs a fraction of a cent per question
on your own OpenAI key. Fortnite on Xbox Cloud Gaming is free.

**Is the ready-made firmware safe to share?** Yes. It holds no Wi-Fi name, password or key. The board finds the server on your own
network by itself, and the server accepts it from your local network only.

**Do I need to solder or 3D print?** No. Please do not solder to the calculator. Tape holds the board.

## More

| | |
|---|---|
| **[TUTORIAL.md](TUTORIAL.md)** | **The step-by-step guide for the build in the video** |
| [Flash the board](https://ethanpaschkes.github.io/ti84-calcgpt/flash/) | The web page that puts the ready-made firmware on a XIAO ESP32C6 |
| [INSTALL.md](INSTALL.md) | The advanced build: your own cloud server, firmware built by you, other boards |
| [docs/ABOUT.md](docs/ABOUT.md) | How it works inside, every folder, tests, cabled use with no board, safety notes |
| [docs/ASSISTANT_PROMPT.md](docs/ASSISTANT_PROMPT.md) | The long version of the AI prompt, with guard rails |
| [cloud/README.md](cloud/README.md) | The server in depth: Fly.io, costs, security |
| [hardware/README.md](hardware/README.md) | 3D-print files and print guides |
| [wireless/PROTOCOL.md](wireless/PROTOCOL.md) | The wire protocol between board and server |

---

Made by [Ethan Paschkes](https://ethanpaschkes.com), student developer and glider pilot. MIT licence. If you build one, open an
issue or a discussion: I would love to see it.

Keywords: TI-84 Plus CE ChatGPT, TI-84 AI, calculator ChatGPT, ESP32 TI-84, TI-84 wifi, CE C toolchain, srldrvce, usbdrvce, cemetech.
