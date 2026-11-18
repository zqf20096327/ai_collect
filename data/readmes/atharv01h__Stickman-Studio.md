<p align="center">
  <img src="docs/images/banner.png" alt="Stickman Studio Banner" width="100%">
</p>

<p align="center">
  <a href="https://stickmanstudio.netlify.app/"><img src="https://img.shields.io/badge/Website-stickmanstudio.netlify.app-00C7B7.svg?style=for-the-badge&logo=netlify" alt="Official Website"></a>
  <a href="https://github.com/atharv01h"><img src="https://img.shields.io/badge/Creator-Atharv%20Hatwar-7C3AED.svg?style=for-the-badge&logo=github" alt="Creator: Atharv Hatwar"></a>
  <a href="https://github.com/atharv01h/Stickman-Studio/stargazers"><img src="https://img.shields.io/github/stars/atharv01h/Stickman-Studio?style=for-the-badge&logo=github&color=F59E0B" alt="GitHub Stars"></a>
  <a href="https://github.com/atharv01h/Stickman-Studio/network/members"><img src="https://img.shields.io/github/forks/atharv01h/Stickman-Studio?style=for-the-badge&logo=github&color=6366F1" alt="GitHub Forks"></a>
  <a href="https://github.com/atharv01h/Stickman-Studio/issues"><img src="https://img.shields.io/github/issues/atharv01h/Stickman-Studio?style=for-the-badge&color=EC4899" alt="GitHub Issues"></a>
  <a href="https://github.com/atharv01h/Stickman-Studio/pulls"><img src="https://img.shields.io/badge/PRs-Welcome-22C55E.svg?style=for-the-badge" alt="PRs Welcome"></a>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License: MIT">
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-0078D6.svg?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 / 11">
  <img src="https://img.shields.io/badge/Privacy-100%25%20Offline-22C55E.svg?style=for-the-badge" alt="100% Offline">
  <img src="https://img.shields.io/badge/Zero_Cloud-100%25_Free-06B6D4.svg?style=for-the-badge" alt="100% Free & Offline">
</p>

---

# 🎬 Stickman Studio

> **Designed and Engineered by [Atharv Hatwar](https://github.com/atharv01h)**  
> **Official Website:** **[https://stickmanstudio.netlify.app/](https://stickmanstudio.netlify.app/)**  
> An autonomous, **100% local, free, offline AI video production suite** for Windows. Turn any topic or narration script into a dynamic, voiced, full-screen animated reel or explainer film — **Moving Stickman** or **Cinematic Illustrated Reels** — with zero paid APIs, zero subscriptions, and full privacy.

<p align="center">
  <b>⭐ If you find Stickman Studio useful, please star the repository — it helps more creators discover free, open-source video tools!</b>
</p>

<p align="center">
  <a href="https://alternativeto.net/software/stickman-studio/about/?utm_source=badge&utm_medium=referral" target="_blank">
    <img src="https://alternativeto.net/static/badges/badge-compact-color.svg"
         alt="Stickman Studio | AlternativeTo"
         width="244" height="79"
         style="width: 244px; height: 79px;" />
  </a>
</p>

### ⚖️ Why Stickman Studio? (vs. Cloud Video SaaS)

| Capability | **Stickman Studio (Open Source)** | Commercial SaaS (Vyond / InVideo / Doodly) | Cloud Generative AI (Sora / Runway / Kling) |
|---|---|---|---|
| **Price** | **100% Free Forever** | $30 – $99 / month | $20 – $100 / month (credit drains) |
| **Data Privacy** | **100% Local & Offline** | Cloud hosted & user-data logged | Cloud processed & stored |
| **API Keys & Accounts** | **Zero Keys / No Accounts** | Mandatory login & subscription | Paid API credits required |
| **Animation Quality** | **Physics kinematics + 1,000+ Vector Objects** | Static pre-baked puppet clipart | Hallucinatory morphing & artifacts |
| **Speech Narration** | **Local Kokoro-82M ONNX (Natural)** | ElevenLabs add-on ($$$) or robotic TTS | Additional paid audio add-on |
| **Choreography Control** | **45 Semantic Story Metaphors** | Manual timeline keyframing | Random prompt lottery |
| **Procedural Library** | **1,000+ Objects & 1,750+ Backdrops** | Stock templates (few hundred) | Uncontrollable noise |
| **Rendering Speed** | **Fast CPU / GPU NVENC streaming** | Cloud queue bottlenecks | Server generation wait times |

---

## 🔥 What's New in Stickman Studio 2.6 (Autonomous AI Director & Living Visual Intelligence)

Stickman Studio 2.6 introduces an autonomous **Inbuilt AI Director**, **Continuous Character Kinematics**, **Dynamic Multi-Layout Staging**, **Topic-Specific Procedural World Generation**, and **Moving Stickman Text Boundary Protection**:

- 🧠 **Autonomous Inbuilt AI Director (`InbuiltAIDirector` & `ScriptIntelligence`)**:
  Zero Ollama or external models required! Instantly generates (<15ms) viral scripts and storyboards 100% offline. Features **Dual Scripting Modes**:
  - *Solo Narrative*: Paced, high-hook storytelling with narrative retention anchors.
  - *Conversational Dialogue Duel*: Alex & Maya dynamic two-person dialogue with automated speaker turn-taking and gender-distinct TTS synthesis.
  - *Domain-Fused Compound Topics*: Deep conceptual understanding for compound subjects (e.g., "AI in Medicine", "Stoicism and Money", "Psychology of Habits").
- 🏃 **Continuous Character Kinematics in CIS Mode**:
  Completely eliminated static cardboard cutouts! Characters in Cinematic Illustrated Stickman mode are fully alive throughout the entire shot:
  - *1.25 Hz Breathing Cycle*: Natural chest expansion and vertical rise-and-fall ($\pm 4.5\text{px}$).
  - *Subtle Posture Sway*: Realistic weight shift ($\pm 0.016\text{ rad}$) and natural body angle wobble.
  - *Narrative Emphasis Gestures*: Contextual lean-in and assertive head/torso nods timed to mid-sentence narrative beats.
  - *Alive Fallback Loop*: Organic camera and character bobbing in native Python + FFmpeg fallback rendering.
- 🌍 **Topic-Specific Procedural World Generation**:
  Topic context is automatically propagated into background inference so shots never fall back to generic blank paper. Expanded [ai_background_engine.py](src/engine/ai_background_engine.py) with dedicated environments for `STOIC_PHILOSOPHY` (ancient temples & pillars), `PSYCHOLOGY_MIND` (neural colliders & quantum realms), `STARTUP_BUSINESS` (executive skylines), `SCIENCE_INNOVATION` (cleanrooms & formula boards), `CAFE_LIFESTYLE`, and `CHESS_STRATEGY`.
- 📐 **Dynamic Multi-Layout Staging in CIS Mode**:
  Broke rigid uniform card-and-actor staging into 6 distinct spatial choreographies:
  - *Clean Stage*: Natural diorama without a heavy box; character freely interacts with semantic props.
  - *Split-Screen Duel*: Side-by-side contrast duel ($cx=310$ vs $cx=780$) with central kinetic divider lines.
  - *Floating Callout Panorama*: Lower-third badge leaving top 70% open for grand panoramic scenes.
  - *Editorial Spread*: High-end asymmetrical layout with hero anchored on right ($cx=810$) and unboxed typography.
  - *Big Typo Banner*: Climactic takeaway with an impact header and hero centered below.
  - *Comic Beats*: Kinetic speech and thought bubble exchange with reacting character.
- 🔤 **Moving Stickman Text Overflow & Missing Text Elimination**:
  Overhauled [scene_composer.py](src/animation/scene_composer.py) and [assets.py](src/animation/assets.py). Speech bubbles, thought bubbles, headline banners, rebel badges, and concept cards now use iterative font auto-shrinking down to 9-11px, intelligent line-wrapping, and safety ellipsis truncation. Text is 100% contained within bounds with zero edge clipping.

---

## 🔥 What's New in Stickman Studio 2.5 (Massive Cinematic & AI Upgrade)

Stickman Studio 2.5 introduces a comprehensive, deep-level overhaul of **Cinematic Illustrated Mode** (`CISPipeline`), dramatically scaling visual resources, procedural intelligence, and performance:

- 🎨 **Massive 1,000+ Procedural Vector Objects Library**:
  Engineered a high-performance procedural vector engine ([procedural_object_engine.py](file:///D:/StickMan%20video%20software/src/engine/procedural_object_engine.py)) spanning 15 concrete domains (Vehicles, Tech, Finance, Tools, Fitness, Medical, Nature, Animals, Food, Architecture, Psychology, Social, Science, Music, Fantasy) featuring iconic, glossy vector art (twin-bell alarm clocks with 12 hour ticks, modern smartphones with dynamic islands & chat bubbles, glossy highlight hearts, retro cars, etc.).
- 🌐 **Universal Generative Semantic Synthesizer**:
  Deterministically creates handsome, heraldic vector badges and symbols for *any* arbitrary English noun not in the static catalog — ensuring 100% visual coverage with 0 blanks and zero debug text boxes!
- 🌌 **1,750+ Procedural Environmental Backgrounds**:
  Expanded [ai_background_engine.py](file:///D:/StickMan%20video%20software/src/engine/ai_background_engine.py) to synthesize 35 distinct atmospheric skies and 50 horizon environments tailored per sentence beat, replacing flat blank paper with rich Light Mode (clean architectural outlines on paper) and Dark Mode (glowing cosmic neon).
- 🎬 **45 Cinematic Choreographies**:
  Expanded from 20 to 45 bespoke scene choreographies covering Stoicism, Dark Psychology, Tech/AI, Wealth, Neuroscience, Athletics, Relationships, and Life Metaphors.
- 🛡️ **Smart Collision-Free Positioning & CTA Guard**:
  Integrated 2D spatial bounding-box collision clearance in [cis_scene_illustrator.py](file:///D:/StickMan%20video%20software/src/engine/cis_scene_illustrator.py). Props automatically detect occupied coordinates and never collide with actors, mirrors, or the interactive `BOOKMARK & FOLLOW` CTA button.
- ⏱️ **Sub-Second Audio-to-Video Synchronization**:
  Introduced [timeline_manager.py](file:///D:/StickMan%20video%20software/src/engine/timeline_manager.py) to lock audio and video durations to exact frame-accurate boundaries, eliminating audio cutoffs and lingering silent video frames.
- 💎 **Obsidian Studio 2.0 UI**:
  Upgraded [main_window.py](file:///D:/StickMan%20video%20software/src/ui/main_window.py) and [cis_mode_panel.py](file:///D:/StickMan%20video%20software/src/ui/cis_mode_panel.py) with an obsidian `#0A0E17` palette, glowing segmented mode switcher pills (`🎬 Moving Stickman` / `✦ Cinematic Illustrated`), numbered step badges (`💡 Step 1`, `📝 Step 2`, `⏱️ Step 3`), and a live target-aware word counter meter.
- ⚡ **Optimized for 8 GB RAM & 4 GB VRAM**:
  Entirely procedural execution with sub-millisecond generation per asset, zero memory leakage, and lightweight performance on AMD Ryzen 5 / GTX 1650 hardware.

---

## 🌟 Studio Interface Overview

Stickman Studio runs inside a sleek, non-blocking **Obsidian-Studio PySide6 UI** built for fast startup (`< 1s`), smooth tab switching, live style card previews rendered asynchronously, and instant two-way engine controls:

<p align="center">
  <img src="docs/images/ui_studio.png" alt="Stickman Studio Obsidian Dark UI" width="95%">
</p>

---

## 🎥 StickMan Videos Showcase (Real Production Demos)

Below are real-world, full-length productions created and rendered end-to-end with **Stickman Studio** (from `D:\StickMan Videos`), showcasing procedural stickman kinematics, semantic prop choreography, kinetic subtitles, and multi-scene pacing:

<table align="center" width="85%">
  <tr>
    <td align="center" width="50%">
      <b>🧠 Overthinking At Midnight</b><br>
      <i>Neuroscience & Sleep Psychology Explainer</i><br><br>
      <img src="docs/images/demos/demo1_overthinking_night.gif" width="260"><br><br>
      <sub>11:47 PM bedside clock, stickman blinking awake, thought cloud pop & brain diagram</sub>
    </td>
    <td align="center" width="50%">
      <b>🎭 God-Level Manipulation</b><br>
      <i>Dark Psychology & Manufactured Free Will</i><br><br>
      <img src="docs/images/demos/demo2_illusion_puppet.gif" width="260"><br><br>
      <sub>Marionette puppet strings, cross handles drop & choice architecture stage</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <b>⚠️ The "Martyr" Trap</b><br>
      <i>Social Dynamics & Inverted Freeze Mode</i><br><br>
      <img src="docs/images/demos/demo3_martyr_trap.gif" width="260"><br><br>
      <sub>Dramatic inversion to dark X-ray canvas with glowing red strings & crown</sub>
    </td>
    <td align="center" width="50%">
      <b>🚩 Why People Remember You</b><br>
      <i>Viral Relationship Reel & Boundary Clarity</i><br><br>
      <img src="docs/images/demos/demo4_remember_utility.gif" width="260"><br><br>
      <sub>Sequential message notification flurry, phone props & boundary contrast</sub>
    </td>
  </tr>
</table>

### 📊 Featured Video Productions

| Production Title | Topic & Narrative Genre | Format & Runtime | Key Animation & Techniques Demonstrated | Scene Count |
|---|---|---|---|---|
| **Why Do People Remember You Only When They Need You?** | Relationship Boundaries & Utility vs. Genuine Connection | `9:16 Vertical Reel` • 125.6s (1080p) | Notification flurry, favor handoff, ghosting timeline, boundary shields, takeaway cards | 16 Scenes |
| **The Architecture of Manufactured Free Will** | Dark Psychology & Choice Architecture | `9:16 Vertical Reel` • 98.1s (1080p) | Marionette puppet strings, Door A vs. Door B trap, shadow master, ladder climb | 7 Scenes |
| **Why Your Brain Replays Embarrassing Moments at Night** | Neuroscience & Sleep Psychology | `9:16 Vertical Reel` • 54.8s (1080p) | Bedside clock, thought bubble pop, prefrontal cortex bouncer, megaphone alarm | 7 Scenes |
| **The "Martyr" Trap: How The Loudest Victim Runs The Room** | Social Dynamics & Guilt Manipulation | `9:16 Vertical Reel` • 45.0s (1080p) | Inverted dark freeze mode, puppet strings, glowing crown, confrontation cards | 5 Scenes |
| **Why Narcissists Always Have It Worse Than You** | Dark Psychology & Ego Dynamics | `9:16 Vertical Reel` • 113.8s (1080p) | The "One-Up Olympics", wound badges, spotlight shift, psychological supremacy | 13 Scenes |
| **The Zeigarnik Effect: Open Loop Attraction** | Cognitive Psychology & Mystery | `9:16 Vertical Reel` • 90.9s (1080p) | Unfinished puzzle cards, open loop sparks, closed folder contrast, magnet orbit | 8 Scenes |
| **The Push-Pull Dynamic in Social Attraction** | Interpersonal Dynamics & Dating Psychology | `9:16 Vertical Reel` • 83.5s (1080p) | Pedestal dynamics, push/pull tension cards, brain sparks, magnetic confidence | 8 Scenes |
| **Can You Tell If Someone Secretly Likes You?** | Non-Verbal Body Language & Subtle Cues | `9:16 Vertical Reel` • 117.6s (1080p) | Eye gaze triangulation, room focus shifts, posture leaning, subtle cue zooms | 14 Scenes |

---

## ✨ Key Highlights

| Feature | What It Does |
|---|---|
| 🔒 **100% Free & Offline** | Zero cloud APIs or recurring keys. Powered by local **Kokoro ONNX / SAPI TTS**, procedural vector engines, optional local **Ollama**, and optional local **`LCM_Dreamshaper_v7`**. |
| 🧠 **Autonomous Inbuilt AI Director** | 100% offline neural intelligence generating viral scripts & storyboards instantaneously (<15ms) in both **Solo Narrative** and **Alex & Maya Dialogue Duel** modes with zero Ollama dependency. |
| 🏃 **Continuous Character Kinematics** | Characters in CIS mode are continuously alive with 1.25 Hz breathing chest expansion ($\pm 4.5\text{px}$), body weight sway, and narrative emphasis gestures. |
| 🎭 **Dual Animation Modes** | Switch seamlessly between **Mode 1: Moving Stickman** (full joint kinematics & 2.5D rooms) and **Mode 2: Cinematic Illustrated Reels** (`CISPipeline` multi-sprite & canvas reels with 45 choreographies). |
| 🎨 **1,000+ Procedural Objects & 1,750+ Backdrops** | High-performance vector engine synthesizing bespoke props across 15 domains + 1,750+ procedural skies and horizons with topic-aware inference and zero blanks. |
| 🔤 **Text Overflow & Missing Text Safety** | Dynamic font auto-scaling down to 9px, intelligent wrapping, and safety truncation in speech bubbles, thought clouds, headline banners, and cards. |
| 🛡️ **Collision-Free Prop Layout & CTA Protection** | 2D spatial clearance ensures props never overlap actors or stage elements, and strictly prevents floating props from covering the interactive `BOOKMARK & FOLLOW` button. |
| ⏱️ **Sub-Second Audio-Video Sync** | Dedicated timeline orchestrator (`TimelineManager`) locks audio and video durations to exact frame-accurate boundaries, preventing premature audio cutoffs or lingering silent frames. |
| ✨ **Flagship `AUTO` Style Synthesizer** | Default **`AUTO • AI Script Studio (Best)`** dynamically mixes styles per beat **and** invents bespoke hybrid palettes & lighting (*Obsidian Amber Chalk*, *Velvet Violet Noir*, *Warm Kraft Editorial*, etc.). |
| 🧠 **45 Script-Matched Choreographies** | Semantic planner maps your script clauses directly into story metaphors (`give_and_withdraw`, `split_mirror_ideal`, `boundary_shield`, `tether_break`, `mind_storm_calm`, `two_path_fork`, `domino_chain`, etc.). |
| 🎨 **Dual Background AI (`Procedural` vs. `LCM`)** | Choose **Procedural Vector AI** (instant CPU speed) or **Local Diffusion (`LCM DreamShaper`)** across **both** Moving Stickman & CIS Mode 2 with synchronized controls. |
| 🎙️ **Smart Auto Voice Speed & CTA Screen** | Auto-calibrates TTS pacing to fit duration naturally (`compute_auto_voice_speed` + refinement) and optionally appends a custom animated **Ending `+ FOLLOW` / CTA Screen** with spoken outreach. |
| 💎 **Obsidian Studio 2.0 Desktop UI** | Modernized `#0A0E17` UI with glowing segmented mode pills, step progress badges, live target-aware word counter meter, and GPU NVENC / CPU export in `9:16`, `16:9`, or `1:1`. |

---

## 🎭 Dual Production Modes in Action

### 1. Mode 2 — Cinematic Illustrated Stickman Reels (`CISPipeline`)
Designed for psychology, mindset, storytelling, and viral short-form reels — every scene selects its matching choreography, layout architecture, prop visual, and `AUTO_MIX` canvas backdrop:

<p align="center">
  <img src="docs/images/cis_choreographies_showcase.png" alt="CIS Mode 2 Choreographies & Ending CTA Showcase" width="95%">
</p>

- **Canvas Styles (`Visual World & Style`)**:
  - `✨ Auto (1000+ Multi-Domain Visuals)` (`AUTO_MIX` — dynamically alternates craft paper, sage canvas, blueprint grid, obsidian neon, and charcoal themes per beat)
  - `💼 Wealth, Finance & Business` · `💻 Tech, Coding & AI Systems` · `🏋️ Fitness, Health & Athletics` · `🏛️ Stoicism, Philosophy & History` · `⚡ Habits & Productivity` · `🧠 Dark Psychology`
  - `📓 Classic White Sketchbook (B1)` · `📰 Warm Editorial (B2 Cream)` · `🌌 Obsidian Dark Chalkboard (B3 Neon)`
- **6 Layout Architectures**: `clean_stage`, `big_typo_banner`, `split_screen`, `comic_beats`, `floating_callout`, `editorial_spread`.
- **Procedural Object Engine (1,000+ Vector Objects)**:
  - 15 concrete domains: Vehicles, Tech, Finance, Tools, Fitness, Medical, Nature, Animals, Food, Architecture, Psychology, Social, Science, Music, Fantasy.
  - Universal Generative Semantic Synthesizer: Bespoke vector emblem synthesis for any arbitrary noun.
  - Smart collision detection: Evaluates candidate coordinates with 2D distance checks to avoid actor and mirror overlap.
- **Ending Follow / CTA Screen Guard**:
  - Configurable button presets (`+ FOLLOW`, `+ SUBSCRIBE`, `BOOKMARK & FOLLOW`), headline, cursor tap, ringing bell, and custom voiceover.
  - Dedicated protection rule guarantees CTA interactive buttons are 100% unobstructed by props.

<details>
<summary><b>Click to view all 45 CIS Choreographies & 15 Object Domains</b></summary>

- **45 Choreographies**:
  1. `cta_celebration` (Bookmark, follow, subscribe celebration with animated cursor & bell)
  2. `split_mirror_ideal` (Present reality vs. elevated self-image reflection)
  3. `two_path_fork` (Bifurcating paths, divergence, difficult choices)
  4. `phone_trap` (Modern digital addiction, dopamine cage, scrolling trap)
  5. `hourglass_sprint` (Race against fading sand, urgency, deadlines)
  6. `dumbbell_gym_lift` (Discipline, resistance training, physical transformation)
  7. `terminal_code_deploy` (Software engineering, terminal compilation, deploy pipeline)
  8. `crypto_market_rally` (Financial charts, bullish green candlesticks, market momentum)
  9. `battery_supercharge` (Energy renewal, exhaustion vs. 100% capacity)
  10. `rocket_launchpad_stage` (Gantry towers, countdown, staging separation)
  11. `scales_of_justice` (Fairness, moral weight, legal balance)
  12. `pedestal_bust_trap` (Idolization, falling off the pedestal, false authority)
  13. `bridge_cross` (Bridging the gap between two cliffs, overcoming obstacles)
  14. `boundary_shield` (Erecting emotional boundary walls, deflection)
  15. `tether_break` (Severing toxic attachments, snapping elastic cord)
  16. `give_and_withdraw` (Conditional generosity, giving with leverage)
  17. `scale_tipping` (Gradual accumulation until balance tips)
  18. `chess_checkmate_move` (Strategic calculation, endgame checkmate)
  19. `puzzle_assembly` (Fitting cognitive pieces together, epiphany)
  20. `radar_scanner_sweep` (Sonar sweep, threat detection, opportunity scanning)
  21. `atom_quantum_orbit` (Nucleus with electron orbits, fundamental science)
  22. `compound_interest_snowball` (Exponential accumulation, tiny habits compounding)
  23. `focus_pomodoro_timer` (Deep work sprint, ticking timer dial)
  24. `staircase_climb` (Step-by-step upward climb to mountain summit)
  25. `mirror_truth` (Confronting undeniable reflection)
  26. `protective_couple_shield` (Relational defense, sheltering partner)
  27. `notification_fishhook` (Baiting algorithm hook, intermittent rewards)
  28. `crowd_filter` (Filtering signal from ambient crowd noise)
  29. `split_cards_slide` (Comparative slide cards, before vs. after)
  30. `magnet_orbit` (Magnetic attraction, gravitational capture)
  31. `question_burst` (Central thinker, expanding question marks, lightbulb)
  32. `domino_ripple` (Single trigger toppling domino chain)
  33. `spotlight_shift` (Dark stage with traveling spotlight reveal)
  34. `rocket_breakthrough` (Cloud penetration, ceiling breakthrough)
  35. `mind_storm_calm` (Chaotic cognitive storm subsiding into clarity)
  36. `idea_spark_build` (Initial spark igniting an engineered structure)
  37. `lighthouse_fog_beam` (Rotating beam piercing heavy ocean fog)
  38. `dopamine_spike_chart` (Euphoric high followed by baseline drop)
  39. `stoic_pillar_stand` (Unshakable pillar in raging winds)
  40. `neural_net_synapse` (Pulsing neurons firing across synaptic cleft)
  41. `iceberg_hidden_depth` (Surface 10% vs. colossal 90% subsurface truth)
  42. `hamster_wheel_break` (Escaping the endless consumerist loop)
  43. `dna_evolution_spiral` (Double helix rotating spiral, biological adaptation)
  44. `eisenhower_grid_sort` (Urgent vs. important 4-quadrant decision matrix)
  45. `dynamic_synthesizer` (Fully autonomous composition synthesizer matching input semantics)

- **15 Procedural Object Domains (1,000+ Assets)**:
  `Vehicles`, `Technology`, `Finance`, `Tools`, `Fitness`, `Medical`, `Nature`, `Animals`, `Food`, `Architecture`, `Psychology & Metaphors`, `Social & Communication`, `Science & Space`, `Music & Art`, `Fantasy & Medieval`.

</details>

---

### 2. Dual Background AI: Procedural Vector AI vs. Local `LCM DreamShaper`

Switch effortlessly between lightning-fast **Procedural Vector AI** and locally cached **`SimianLuo/LCM_Dreamshaper_v7`** diffusion backdrops — both **Background AI** and **Illustration Engine** controls stay synchronized automatically:

<p align="center">
  <img src="docs/images/lcm_vs_procedural.png" alt="Procedural Vector AI vs LCM DreamShaper Diffusion Comparison" width="95%">
</p>

> [!TIP]
> On systems with limited VRAM or CPU-only setups, `LCM DreamShaper` caches every generated scene backdrop locally and automatically unloads model weights from memory once illustration finishes so TTS and video encoding run at full speed.

---

### 3. Mode 1 — Moving Stickman (`SceneComposer`) & `AUTO` Style Synthesizer

Full procedural 2x supersampled stickman acting, prop handoffs, facial expressions, eye tracking, blinking, camera motion, and **`AUTO` Scene Style Synthesis**:

<p align="center">
  <img src="docs/images/auto_styles_showcase.png" alt="Mode 1 AUTO Style Synthesizer Multi-Beat Render" width="95%">
</p>

<p align="center">
  <img src="docs/images/sample_scene.png" alt="Moving Stickman 2.5D Scene Render" width="90%">
</p>

<details>
<summary><b>Click to view all 16 Visual Styles in Mode 1 (`auto` + S1–S15)</b></summary>

| ID | Style Name | Description |
|---|---|---|
| `auto` | **AUTO • AI Script Studio (Best)** *(Default)* | Mixes styles per beat AND synthesizes custom hybrid palettes & lighting tuned to the script |
| `s1_rsa_whiteboard` | **S1 RSA Whiteboard Explainer** | Crisp cream paper canvas, blueprint ink, dry-erase sketch lines |
| `s2_cyberpunk_neon` | **S2 Cyberpunk Neon Terminal** | Dark futuristic slate with glowing neon cyan & magenta rim lighting |
| `s3_retro_pop_comic` | **S3 Pop Art & Retro Comic** | Halftone comic panels, bold dynamic outlines, saturated accents |
| `s4_notion_startup` | **S4 Notion & Tech Minimalist** | Clean editorial startup aesthetic with structured pastel cards |
| `s5_dark_gold_wealth` | **S5 Luxury Gold & Finance** | Obsidian-black canvas with metallic gold geometric accents |
| `s6_chalkboard_academy` | **S6 Academic Chalkboard Lecture** | Classic green slate board with textured chalk strokes & dust |
| `s7_ghibli_watercolor` | **S7 Cozy Ghibli Storybook** | Warm illustrated pastoral gradients and soft ambient lighting |
| `s8_shonen_manga` | **S8 Shonen Manga Action** | High-contrast monochrome ink, speed lines, dramatic impact frames |
| `s9_retro_arcade` | **S9 8-Bit Retro Arcade CRT** | Pixel grid backdrop with retro arcade palette & subtle scanlines |
| `s10_blueprint_cad` | **S10 Blueprint CAD Engineering** | Technical drafting grid, cyan schematic callouts, crisp geometry |
| `s11_graffiti_punk` | **S11 Urban Street Art & Graffiti** | Energetic spray-paint stencil highlights on dark urban backdrop |
| `s12_cinematic_noir` | **S12 1940s Detective Film Noir** | Moody high-contrast shadows, Venetian blind light beams, amber noir |
| `s13_cinematic_storyteller` | **S13 Cinematic Storyteller** | 2.5D narrative staging with floor reflections & golden hour glow |
| `s14_chameleon_adaptive` | **S14 Chameleon Dynamic** | Adaptive scene-by-scene selection across classic packs by mood |
| `s15_minimalist_accent` | **S15 Minimalist Ink & Accent** | High-impact distraction-free ink & single bold accent storytelling |

</details>

---

## 🏛️ System Architecture

```
                                      STICKMAN STUDIO
                                 Engineered by Atharv Hatwar
                                               │
            ┌──────────────────────────────────┴──────────────────────────────────┐
            ▼                                                                     ▼
   [ Moving Stickman Mode ]                                        [ Cinematic Illustrated Mode ]
 • AUTO Style Synthesizer + S1–S15                               • Semantic Storyboarder (45 Choreos)
 • 3-Phase Joint Kinematics                                      • ProceduralObjectEngine (1,000+ Props)
 • Procedural Rooms & LCM Diffusion                              • AIBackgroundEngine (1,750+ Environments)
 • Multi-Beat Style Morphing                                     • Collision-Free Layout & CTA Protection
            │                                                                     │
            └──────────────────────────────────┬──────────────────────────────────┘
                                               ▼
                                  [ Audio & Voice Pipeline ]
                        • Kokoro ONNX Neural TTS + Windows SAPI Fallback
                        • Smart Auto Voice Speed & Dialogue Duo Mode
                        • Procedural DSP Music & SFX + Sidechain Ducking
                                               │
                                               ▼
                                 [ Timeline & Rendering Engine ]
                        • TimelineManager (Frame-Accurate Audio-Video Sync)
                        • Native Autopilot / Canvas Compositor & FFmpeg NVENC
                        • Optional Animated Ending Follow / CTA Card
                                               │
                                               ▼
                                    🎬 Fullscreen 1080p MP4
```

---

## 💻 Hardware Requirements

Designed specifically to operate efficiently within tight hardware envelopes:

| Component | Minimum Specification | Recommended Specification |
|---|---|---|
| **Operating System** | Windows 10 (64-bit) | Windows 11 (64-bit) |
| **Processor** | Intel Core i5 / AMD Ryzen 3 | AMD Ryzen 5 4600H / Intel Core i7 |
| **System RAM** | 8 GB RAM | 8 GB – 16 GB RAM |
| **Graphics Card** | Intel UHD Graphics (CPU Mode) | NVIDIA GTX 1650 (4 GB VRAM) or higher |
| **Python** | Python 3.11+ | Python 3.11 or 3.12 (for CUDA PyTorch wheels) |
| **Disk Space** | 4 GB free space | 8 GB free space (for models & videos) |

---

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/atharv01h/Stickman-Studio.git
cd Stickman-Studio
```

### 2. One-Click Setup (Run Once with Internet)

Run the automated installer script to configure all packages, engines, and models:

```batch
setup_windows.bat
```

What the automated installer configures:
- **Python & Pip**: Detects Python 3.10+ (or auto-installs Python 3.11 via `winget` if Python is missing)
- **Python Dependencies**: Installs and verifies `PySide6`, `Pillow`, `numpy`, `soundfile`, `requests`, `tqdm`, `kokoro-onnx`, `piper-tts`
- **FFmpeg & FFprobe**: Locates local/system binaries or auto-downloads Gyan.dev essentials build into `./ffmpeg/` and permanently registers it in your Windows User `Path`
- **Neural Voices (~115 MB)**: Automatically downloads and caches `kokoro-v1.0.int8.onnx` and `voices-v1.0.bin` (54 voices across 8 languages)
- **Directories & Typography**: Initializes runtime folders and verifies bundled `Caveat.ttf` & `NotoSans.ttf` fonts
- **Hardware Acceleration Probe**: Tests NVIDIA NVENC GPU acceleration (`h264_nvenc`) with automatic fallback to high-quality CPU encoding (`libx264`)

> [!NOTE]
> Once setup completes and local models (`Kokoro ONNX`, optional `LCM_Dreamshaper_v7`) are cached, you can disconnect from the internet completely — everything runs 100% offline.

### 3. Launch & Health Check

```batch
run.bat          :: Launch GUI (or run: python main.py)
health_check.bat :: Verify dependencies, FFmpeg & GPU status
```

---

## 🎬 How to Generate Your First Video

1. **Choose Production Mode**: Select **Moving Stickman** or **✦ Cinematic Illustrated** at the top left.
2. **Enter Topic & Script**: Type a topic and paste your script (or pick **Auto-Generate** / **Improve**).
3. **Select Style & Background AI**:
   - Keep **`AUTO • AI Script Studio (Best)`** / **`✨ Auto (Mix + Custom Styles)`** selected for dynamic script-matched variety.
   - Pick **Procedural Vector AI** (instant) or **LCM DreamShaper AI** (local diffusion scenic backdrops).
4. **Voice Speed & Ending CTA**: Keep **Voice Speed: Auto (Smart Fit)** enabled and optionally toggle **Ending Follow / CTA Screen** with your handle/call-to-action.
5. **Generate & Export**: Click **Generate Video** (or **Generate Illustrated Video**), preview right inside the **Preview & Export** tab, or find your rendered MP4 inside `output/`.

---

## 📂 Project Structure

```
Stickman-Studio/
├── .github/                           # Community health & issue templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
├── assets/
│   └── fonts/                         # Bundled Caveat & NotoSans typography + OFL licenses
├── docs/                              # Visual documentation & media assets
│   └── images/                        # Banner, UI screenshots & rendered feature showcases
│       ├── banner.png
│       ├── app_icon_512.png           # Official 512x512 app icon & logo
│       ├── social_preview.png         # GitHub 1280x640 OpenGraph social preview card
│       ├── ui_studio.png
│       ├── cis_choreographies_showcase.png
│       ├── lcm_vs_procedural.png
│       ├── auto_styles_showcase.png
│       ├── sample_scene.png
│       ├── styles_grid.png
│       └── demos/                     # Real production GIF video demos from D:\StickMan Videos
│           ├── demo1_overthinking_night.gif
│           ├── demo2_illusion_puppet.gif
│           ├── demo3_martyr_trap.gif
│           └── demo4_remember_utility.gif
├── src/
│   ├── animation/                     # Moving Stickman kinematics, props, & compositor
│   │   ├── assets.py                  # Procedural vector props & cache-keyed backgrounds
│   │   ├── scene_composer.py          # Director transitions, camera choreography & auto styles
│   │   └── stickman.py                # 3-phase joint animator & facial expression engine
│   ├── audio/                         # Programmatic DSP music, SFX, & sidechain audio mixer
│   ├── captions/                      # Word-level kinetic typography & subtitles
│   ├── engine/                        # Core AI orchestration, CIS & diffusion engines
│   │   ├── ai_background_engine.py    # 1,750+ procedural vector sky & horizon environments
│   │   ├── cis_manifest_builder.py    # Multi-shot kinetic manifest & mixed theme builder
│   │   ├── cis_pipeline.py            # Mode 2 Cinematic Illustrated end-to-end orchestrator
│   │   ├── cis_scene_illustrator.py   # 45-choreography sprite/prop/collision-free illustrator
│   │   ├── cis_storyboard_planner.py  # Semantic script-to-choreography & CTA planner
│   │   ├── inbuilt_ai_director.py     # Autonomous shot director, pacing & camera choreography
│   │   ├── lcm_image_engine.py        # Local SimianLuo/LCM_Dreamshaper_v7 diffusion engine
│   │   ├── llm_manager.py             # Optional local Ollama LLM integration
│   │   ├── procedural_object_engine.py# 1,000+ vector objects across 15 domains & synthesizer
│   │   ├── procedural_scene_engine.py # Scene 0 establishing shot & domain environment mapper
│   │   ├── quality_control.py         # Automated QA, collision clearance & visual verification
│   │   ├── scene_planner.py           # Natural language script decomposition
│   │   ├── script_intelligence.py     # Genre-aware script analysis & beat breakdown
│   │   ├── semantic_scene_brain.py    # In-process neural semantic metaphor & emotion engine
│   │   ├── text_sanitizer.py          # Visual text sanitizer & typography protector
│   │   └── timeline_manager.py        # Frame-accurate audio-video timeline synchronization
│   ├── styles/                        # Mode 1 Auto synthesizer & S1-S15 style pack registry
│   ├── tts/                           # Offline Kokoro ONNX & SAPI TTS + auto voice speed
│   ├── ui/                            # Obsidian-Studio PySide6 desktop GUI
│   │   ├── cis_mode_panel.py          # Mode 2 controls (canvas, engine, pacing, CTA)
│   │   ├── dual_script_editor.py      # Dual-character dialogue script editor
│   │   ├── main_window.py             # Obsidian Studio 2.0 main window & hero mode switcher
│   │   ├── preview_player.py          # Native video preview player
│   │   ├── settings_dialog.py         # Hardware & configuration controls
│   │   ├── style_cards.py             # Async 16-card style gallery with AUTO hero card
│   │   └── voice_panel.py             # Voice selection & auto/manual speed controls
│   ├── utils/                         # Configuration and hardware detection
│   └── video/                         # Mode 1 FFmpeg NVENC/CPU encoding pipeline
├── .gitignore                         # Clean repository filter (blocks cache/models/temp)
├── CONTRIBUTING.md                    # Contributor guide & development setup
├── health_check.bat                   # Diagnostic environment checker
├── LICENSE                            # MIT License (Atharv Hatwar)
├── main.py                            # Application launch orchestrator
├── README.md                          # Comprehensive project documentation
├── requirements.txt                   # Python dependencies
├── run.bat                            # One-click startup script
├── setup_windows.bat                  # Automated Windows environment installer launcher
└── setup_windows.ps1                  # One-click PowerShell installation & dependency engine
```

---

## 🔧 GPU Acceleration Tips (GTX 1650 / NVIDIA)

- **Python 3.11 / 3.12 with CUDA**:
  If you have an NVIDIA GPU (such as GTX 1650 4GB) and want PyTorch CUDA acceleration for LCM diffusion backgrounds:
  ```bash
  pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
  ```
- **NVENC Hardware Encoding**:
  In **Settings → Performance**, ensure **NVIDIA Hardware Acceleration (NVENC)** is checked to offload H.264 video encoding to your GPU.
- **Memory Management**:
  Both the Ollama LLM and LCM DreamShaper pipeline automatically unload after their stage completes to free RAM/VRAM for TTS synthesis and video encoding.

---

## ⭐ Star History

If you love Stickman Studio and want to support free, open-source creative technology, please consider giving us a star! Every star helps creators find open-source alternatives to paid SaaS.

<p align="center">
  <a href="https://star-history.com/#atharv01h/Stickman-Studio&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=atharv01h/Stickman-Studio&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=atharv01h/Stickman-Studio&type=Date" />
      <img alt="Stickman Studio Star History Chart" src="https://api.star-history.com/svg?repos=atharv01h/Stickman-Studio&type=Date" width="85%" />
    </picture>
  </a>
</p>

---

## 🤝 Community & Contributions

We welcome contributions from animators, developers, and creators worldwide:
- **Contributing Guidelines**: Check out [CONTRIBUTING.md](CONTRIBUTING.md) for architecture guides and PR instructions.
- **Bug Reports & Ideas**: Open an issue using our [GitHub Issue Templates](https://github.com/atharv01h/Stickman-Studio/issues/new/choose).

---

## 👤 Author & Creator

<table align="center">
  <tr>
    <td align="center">
      <b>Atharv Hatwar</b><br>
      <i>Lead Architect, Designer & Engineer</i><br>
      Creator of <b>Stickman Studio</b><br>
      GitHub: <a href="https://github.com/atharv01h">@atharv01h</a> • Repository: <a href="https://github.com/atharv01h/Stickman-Studio">Stickman-Studio</a>
    </td>
  </tr>
</table>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for complete details.

```
MIT License

Copyright (c) 2026 Atharv Hatwar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<p align="center">
  <b>Stickman Studio</b> • Created with ❤️ by <b><a href="https://github.com/atharv01h">Atharv Hatwar</a></b> • Zero Cloud • 100% Offline
</p>
