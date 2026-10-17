<p align="center">
  <img src="docs/images/hub.jpg" alt="Optimus Prime at the Autobot HQ under the AUTOBOTS banner" width="100%">
</p>

<h1 align="center">Transformers (PS2) Decompilation</h1>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Status: active">
  <img src="https://img.shields.io/badge/platform-PlayStation%202-blue" alt="Platform: PlayStation 2">
  <img src="https://img.shields.io/badge/target-SLES--52388%20(PAL)-red" alt="Target: SLES-52388 (PAL)">
  <img src="https://img.shields.io/badge/matched-14.7%25-orange" alt="Matched: 14.7%">
</p>

<p align="center">
  A work-in-progress <b>matching decompilation</b> of <i>Transformers</i> for the PlayStation 2
  (Atari / Melbourne House, 2004), released in North America as <i>Transformers Armada: Prelude to Energon</i>.
</p>

---

## A note before you read on

This project is made with the help of AI, and I want to be upfront about that.

Transformers on the PS2 is a game I grew up with. It means a lot to me, and I know I am not the only one who still
thinks about it. This repository exists because of that love for the game and the nostalgia that comes with it.

A matching decompilation means turning more than 22,000 functions of machine code back into source code that compiles
to exactly the same bytes as the original game. Doing that by hand, alone, would take many years. With AI tools it
becomes possible. AI writes the first drafts, but nothing is accepted on its word: every function is checked byte for
byte with the original compiler, and after every change the whole game is rebuilt and compared with the retail
executable. If it does not match exactly, it does not go in.

If you see AI-assisted work as "AI slop" or "vibe coded", I respect that, and this project is simply not for you.
No hard feelings. To everyone else who loves this game as much as I do: welcome, and thank you for being here.

## Status

**Active, started in October 2026.** The source code is not public yet.

This repository exists so that anyone else who wants to decompile this game knows the work is already under way.
Please get in touch before starting a second effort: **open an issue here**.

## Target

| Region | Serial | Notes |
|---|---|---|
| Europe (PAL) | SLES-52388 | The version being decompiled |
| North America (NTSC-U) | SLUS-20668 | The same game, released as *Transformers Armada: Prelude to Energon* |

## Progress

A function counts as matched when C/C++ source compiles to exactly the same bytes as the function in the original
executable.

| Date | Functions matched | Share of the executable's code |
|---|---|---|
| 2026-10-16 | 7,108 of 22,295 | 7.4 % |
| 2026-10-17 | 10,661 of 22,295 | 14.7 % |

The table is updated as work is merged.

## Screenshots

Captured from the recompiled version of the game, rendered at a higher internal resolution than the PS2.

### 4:3, as on the PS2

<table>
  <tr>
    <td><img src="docs/images/jungle.jpg" alt="Optimus Prime on a jungle path in Amazon Basin"></td>
    <td><img src="docs/images/vista.jpg" alt="Optimus Prime on a ridge above the jungle hills"></td>
  </tr>
  <tr>
    <td><img src="docs/images/combat.jpg" alt="A Decepticon grunt's shot hitting Optimus Prime's shield"></td>
    <td><img src="docs/images/ambush.jpg" alt="A Decepticon flyer overhead during an ambush, LOCK-ON Mini-Con on the HUD"></td>
  </tr>
</table>

### Ultrawide (21:9)

The same moments in 4:3 and 21:9. The wider screen shows more of the world at the sides instead of cutting off the top
and bottom, and the HUD moves out to the screen edges.

<table>
  <tr>
    <th>4:3</th>
    <th>21:9</th>
  </tr>
  <tr>
    <td width="36%"><img src="docs/images/jungle.jpg" width="100%" alt="Amazon Basin jungle path in 4:3"></td>
    <td width="64%"><img src="docs/images/ultrawide-jungle.jpg" width="100%" alt="The same moment in 21:9, with more jungle at both sides"></td>
  </tr>
  <tr>
    <td width="36%"><img src="docs/images/beacon.jpg" width="100%" alt="Optimus Prime near a blue warp beacon in 4:3"></td>
    <td width="64%"><img src="docs/images/ultrawide-beacon.jpg" width="100%" alt="The same moment in 21:9, with more of the forest at both sides"></td>
  </tr>
</table>

<p align="center">
  <img src="docs/images/ultrawide-combat.jpg" width="100%" alt="A Decepticon grunt firing at Optimus Prime at close range, in 21:9">
</p>

## The plan

The decompilation is the foundation. Once the game exists as source code, it can be rebuilt as a true native PC game
and improved far beyond what the PS2 could do. These are the goals, not finished features:

| Goal | What it means |
|---|---|
| 🖥️ **Native PC version** | Built from the decompiled source, running natively with no emulation |
| 🔭 **HD and 4K** | Rendering at high internal resolutions, from 720p up to 4K, with sharp edges and clean text |
| 🎮 **Controller support** | Xbox controllers, DualSense and DualShock 4 (with rumble and light bar), keyboard, fully remappable |
| 🖼️ **Ultrawide** | 16:9, 21:9 and 32:9 with a wider view of the world and the HUD kept in proportion |
| 🧱 **HD textures** | Support for high resolution texture packs |
| ⚡ **High frame rates** | A stable 60 fps and beyond |
| 🔧 **Modding** | Readable source makes new content, fixes and tweaks possible |

## No game data

This repository does not and will not contain game data: no disc images, executables, BIOS files or extracted
assets. You need your own copy of the game.

## Legal

This is an unofficial fan project for preservation and research. It is not affiliated with or endorsed by Hasbro,
Atari or Melbourne House. Transformers is a trademark of Hasbro. Screenshots are captured from the game for illustration.
