# Open Source Higgsfield [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Open-source Higgsfield AI alternatives on GitHub, starting with every notable project built for ComfyUI's #OpenSourceHiggsfield challenge: Genjutsu-style character swap, one-tap effects, camera re-shoots and full studios that run open-weights models on your own GPU or on Comfy Cloud.

102 challenge projects and 6 older alternatives, with stars and licenses as of 2026-11-01. Browse the same list by category at [jutsustudio.com/open-source-higgsfield](https://jutsustudio.com/open-source-higgsfield/).

This is an unofficial community list. It is not affiliated with or endorsed by Higgsfield or Comfy.

## The challenge

- **October 16, 2026.** ComfyUI announced the [#OpenSourceHiggsfield challenge](https://comfy.org/open-source-higgsfield/): "Higgsfield promised to open-source their entire platform. They didn't." Comfy and its partners, including NVIDIA, RunPod and MiniMax, put up $25,000 in prizes for open-source builds on the Comfy Developer Platform. The suggested tracks were Cinematic Studio, Re-shoot a video and Openjutsu (swap a character in a video).
- **October 26.** The Comfy team released its own entry, [OPENjutsu](https://github.com/D3voz/openjutsu), an open-source Genjutsu-style character swap, and the clonable [comfy-openjutsu](https://github.com/Comfy-Org/comfy-openjutsu) app template.
- **October 28.** Builder Night in San Francisco.
- **October 29.** ComfyUI [said](https://x.com/ComfyUI/status/2115928993623109648) Higgsfield had sent it a cease and desist asking it to shut the challenge down.
- **October 30.** Submission deadline.

Entries were found through the #OpenSourceHiggsfield tag on X and through GitHub search. Empty repositories, clones of other entries and private placeholders are left out.

## Most starred

| Project | What it does | Stars | License |
| --- | --- | --- | --- |
| [OPENjutsu](https://github.com/D3voz/openjutsu) | The Comfy team's open-source Genjutsu-style character and object swap: drop a video and a photo, press Generate. Also changes hair or clothes, removes objects or moves the person to a new place. | 910 | MIT |
| [ComfyArt](https://github.com/jtydhr88/ComfyArt) | Free design canvas on your own ComfyUI: an infinite tldraw canvas with a design agent; image, video, audio and 3D run locally. | 411 | MIT |
| [ComfyUI-Continuity](https://github.com/roadmaus/ComfyUI-Continuity) | One node for AI video and stills: write a prompt, attach media with @ and press Render; six model families, all local through ComfyUI core. | 139 | MIT |
| [OpenField](https://github.com/wexloops/openfield) | Studio for video, stills and 3D on your own GPU: every app is a ComfyUI workflow with a screen on top, open weights only. | 124 | none |
| [Open Source Canvas](https://github.com/raph651/open-source-canvas) | Node canvas that runs ComfyUI workflows. | 106 | MIT |
| [comfy-openjutsu](https://github.com/Comfy-Org/comfy-openjutsu) | Official clonable character-swap app and development guide from Comfy: upload a clip and a character image, get a 5 to 15 second part back with the character in it. | 81 | MIT |
| [agentY](https://github.com/szprivate/agentY) | AI agent inside ComfyUI: describe the result and it picks or builds the workflow, runs it and puts the output on your canvas; any LLM, fully local with Ollama, plus a built-in image, video and 3D viewer, Atlas worlds and Gaussian splats. | 46 | MIT |
| [Body Double](https://github.com/lucataco/open-source-higgsfield) | Same take, new cast: swaps the actors in a clip with open-weights models only. | 45 | Apache-2.0 |
| [CreatorOS Studio](https://github.com/thePloggy/CreatorOS-Studio) | Self-hosted studio for one recurring character, from a one-line brief to a finished reel: camera moves, effects, talking avatars, motion transfer and a video editor. | 45 | Apache-2.0 |
| [H3 Recast](https://github.com/Bambushu/h3-recast) | Swaps up to three people in an existing clip in one pass with MiniMax H3 and a BFS LoRA, keeping the motion, set and audio; optional FaceRefine lip pass, 16 GB VRAM and 64 GB RAM. | 37 | MIT |
| [Picky](https://github.com/chenthedesignmaker/ComfyUI-Picky) | Render a shot ten ways and keep the one you love. | 29 | GPL-3.0 |
| [Motion Previs Studio](https://github.com/navarisun1982/comfyui-motion-previs-studio) | 3D camera, character and motion previs, an open take on Higgsfield 3D. | 27 | MIT |
| [OpenKatana](https://github.com/rk0neki/OpenKatana) | Agent-driven video editing with a studio UI, ComfyUI Apps, a CLI and an MCP server. | 20 | Apache-2.0 |
| [Seam](https://github.com/jdnichollsc/seam) | Two shots in, one AI transition out: smoke, water and more. | 19 | MIT |
| [Director's Cut](https://github.com/leonardofrito/Directors-Cut) | Local asset library and reference-to-video studio for ComfyUI. | 16 | MIT |

## Contents

- [Character swap (Openjutsu)](#character-swap-openjutsu)
- [All-in-one studios](#all-in-one-studios)
- [Effects and VFX](#effects-and-vfx)
- [Camera, reshoot and previs](#camera-reshoot-and-previs)
- [Films, music videos and stories](#films-music-videos-and-stories)
- [Ads and UGC](#ads-and-ugc)
- [Characters and datasets](#characters-and-datasets)
- [Canvases, front ends and tools](#canvases-front-ends-and-tools)
- [Beyond the challenge](#beyond-the-challenge)
- [Contributing](#contributing)

## Character swap (Openjutsu)

Open-source takes on Higgsfield Genjutsu: replace the person in a video with a character from one image and keep the camera, motion and sound.

- [OPENjutsu](https://github.com/D3voz/openjutsu) - The Comfy team's open-source Genjutsu-style character and object swap: drop a video and a photo, press Generate. Also changes hair or clothes, removes objects or moves the person to a new place. ★ 910 · MIT · [launch post](https://x.com/Devozikjr/status/2115078855321141502)
- [comfy-openjutsu](https://github.com/Comfy-Org/comfy-openjutsu) - Official clonable character-swap app and development guide from Comfy: upload a clip and a character image, get a 5 to 15 second part back with the character in it. ★ 81 · MIT
- [Body Double](https://github.com/lucataco/open-source-higgsfield) - Same take, new cast: swaps the actors in a clip with open-weights models only. ★ 45 · Apache-2.0 · [launch post](https://x.com/lucataco/status/2116050693601558608)
- [H3 Recast](https://github.com/Bambushu/h3-recast) - Swaps up to three people in an existing clip in one pass with MiniMax H3 and a BFS LoRA, keeping the motion, set and audio; optional FaceRefine lip pass, 16 GB VRAM and 64 GB RAM. ★ 37 · MIT · [launch post](https://www.reddit.com/r/comfyui/comments/1x9n0dl/h3_recast_swap_up_to_3_people_in_a_clip_in_one/)
- [Swapjutsu](https://github.com/jutsuhq/swapjutsu-seedance-character-swap) - Free Mac app that swaps a character into any video: prepares the clip on the Mac with Vision, Core ML and MLX, then renders on Seedance 2.5 through Comfy or on your own ComfyUI with Wan 2.2 Animate. ★ 7 · MIT · [launch post](https://x.com/itsnex1s/status/2112238675396354545)
- [Open Jutsu Studio](https://github.com/lvsas/OpenJutsuStudio) - Video studio that puts your characters into real footage on your own ComfyUI, reopens an H3 take to continue the story and exports a vertical before/after reel. ★ 5 · Apache-2.0 · [launch post](https://www.reddit.com/r/comfyui/comments/1xjette/open_jutsu_studio_put_your_characters_into_real/)
- [Kagami](https://github.com/demoncase/kagami) - Open-source version of Higgsfield Genjutsu. ★ 2 · MIT · [launch post](https://x.com/demoncase/status/2114914686663598506)
- [ComfyUI H3 one-click swap](https://github.com/D3voz/comfyui-h3-oneclick-swap) - ComfyUI nodes for MiniMax H3 character and object swaps with tracked-person matching. ★ 1 · MIT
- [openjutsu (SydFloyd)](https://github.com/SydFloyd/openjutsu) - Genjutsu alternative on ComfyUI with open-weights models only. ★ 1 · Apache-2.0
- [openjutsu (Ex8-ca)](https://github.com/Ex8-ca/openjutsu) - Genjutsu Motion Transfer alternative running MiniMax H3 locally. ★ 0 · MIT
- [OpenJutsu (fetchloom)](https://github.com/fetchloom/OpenJutsu) - Web-based video-to-video studio inspired by Genjutsu, self-hostable, with motion transfer. ★ 0 · MIT
- [openjutsu-cat](https://github.com/SvetimFM/openjutsu-cat) - Openjutsu-style motion transfer driven by depth performances from a Kinect or any video. ★ 0 · MIT
- [OSH Character Studio](https://github.com/LLannnn/OSHCharacterStudio) - ComfyUI replacement for Genjutsu character work. ★ 0 · GPL-3.0
- [Utsushi](https://github.com/regiellis/utsushi) - Video studio for your own ComfyUI, written in Go: motion transfer, object swap and style. ★ 0 · MIT

## All-in-one studios

Higgsfield-style apps with many tools behind one screen: effects, camera moves, characters and editing, on your own GPU or Comfy Cloud.

- [OpenField](https://github.com/wexloops/openfield) - Studio for video, stills and 3D on your own GPU: every app is a ComfyUI workflow with a screen on top, open weights only. ★ 124 · no license · [launch post](https://x.com/strangelooptv/status/2115577068541125062)
- [agentY](https://github.com/szprivate/agentY) - AI agent inside ComfyUI: describe the result and it picks or builds the workflow, runs it and puts the output on your canvas; any LLM, fully local with Ollama, plus a built-in image, video and 3D viewer, Atlas worlds and Gaussian splats. ★ 46 · MIT · [launch post](https://youtu.be/4vtsBWx3Q9k)
- [CreatorOS Studio](https://github.com/thePloggy/CreatorOS-Studio) - Self-hosted studio for one recurring character, from a one-line brief to a finished reel: camera moves, effects, talking avatars, motion transfer and a video editor. ★ 45 · Apache-2.0
- [OpenKatana](https://github.com/rk0neki/OpenKatana) - Agent-driven video editing with a studio UI, ComfyUI Apps, a CLI and an MCP server. ★ 20 · Apache-2.0 · [launch post](https://x.com/rk0neki/status/2113466389545841002)
- [Director's Cut](https://github.com/leonardofrito/Directors-Cut) - Local asset library and reference-to-video studio for ComfyUI. ★ 16 · MIT · [launch post](https://x.com/oLeonardoFrito/status/2114819677386088802)
- [OpenSourceHiggsfield](https://github.com/kevin9327/OpenSourceHiggsfield) - Three-in-one cinema and video studio on open weights. ★ 10 · MIT
- [Comfield](https://github.com/synthetic-ape/comfield) - Higgsfield-style creative studio for AI images and video on ComfyUI. ★ 6 · MIT · [launch post](https://x.com/synthetic_ape/status/2111116405890330982)
- [HyperKut Studio](https://github.com/MajoorWaldi/HyperKut-Studio) - Local ComfyUI video studio for creating, remixing and editing video. ★ 6 · MIT
- [MarcoStudio](https://github.com/NeoMarcoPolo/marcostudio) - 13 image and video tools on your own ComfyUI with open-weights models. ★ 5 · MIT
- [Backlot](https://github.com/Arfolomew/backlot) - Open-source Higgsfield that runs on a 16 GB card with local open-weights video. ★ 4 · MIT · [launch post](https://x.com/Arfolomew/status/2112257381589491971)
- [Cheapsfield](https://github.com/dougliell/Cheapsfield) - Fully local, open-weights creative studio for Windows with Higgsfield-style apps. ★ 4 · Apache-2.0
- [EasyComfee](https://github.com/sintetizacom/easycomfee) - Higgsfield-style studio on ComfyUI: image, video and LTX VFX. ★ 3 · MIT · [launch post](https://x.com/sintetizacom/status/2115884037902393594)
- [FrameForge Studio](https://github.com/RahmelJackson/frameforge-studio) - Creative studio inspired by Higgsfield, powered by ComfyUI workflows. ★ 3 · MIT · [launch post](https://x.com/Rahmeljackson/status/2114708845754782072)
- [OpenIllusion](https://github.com/GETHUK-BIGEMPEROR/OpenIllusion) - Turns ComfyUI workflows into one-click templates: pick one, drop in a photo, clip or sound, press Run. ★ 3 · MIT · [launch post](https://x.com/tzu_crypto/status/2115801099768832392)
- [Rosesfield](https://github.com/rossaai/rosesfield) - Open-source Higgsfield alternative on ComfyUI with 25+ apps for image and video. ★ 2 · MIT
- [Opensfield](https://github.com/codyclack/opensfield) - Higgsfield rebuilt on ComfyUI: 146 tools in one app. ★ 1 · MIT
- [Parametric Studio](https://github.com/parametricparadigm/ComfyUI_Parametric_Studio) - Local studio on ComfyUI spanning 82 open model families: guided forms, recipes and a crew of AI specialists, with the real graph behind every render shown in 3D. ★ 1 · AGPL-3.0 · [launch post](https://www.reddit.com/r/comfyui/comments/1xjg4vk/parametric_studio_every_open_model_one_studio/)
- [Susano](https://github.com/norioversoul/susano) - Open-weights studio on ComfyUI with Openjutsu, Tsukuyomi, Cinematic and Influencer apps. ★ 1 · MIT
- [CineStudio](https://github.com/MachineLearningAmateur/cinestudio) - Scene control for renders made with LTX 2.5 on ComfyUI. ★ 0 · MIT · [launch post](https://x.com/matongzhan/status/2116050590874861729)
- [Darius](https://github.com/Niutonian/Comfyui_Darius_OS) - ComfyUI workspace with a hosted interactive demo. ★ 0 · no license · [launch post](https://x.com/niutonian/status/2115458064937578621)
- [Haggs](https://github.com/IBFolding/haggs) - Film studio on Comfy from script to screen, with every shot and its price in view. ★ 0 · MIT
- [Hildegard](https://github.com/baney75/hildegard) - AI studio on your own GPU: video, voice, characters and 3D. ★ 0 · AGPL-3.0
- [Hoodsfield AI](https://github.com/designn2future/hoodsfield-ai) - Local-first AI film studio on ComfyUI: idea in, finished video out. ★ 0 · Apache-2.0 · [launch post](https://x.com/Official_Marc_H/status/2115931696319098891)
- [Liberty Cut](https://github.com/E5EnclaveInc/liberty-cut) - Cinematic studio built only on open weights (LTX-Video). ★ 0 · MIT
- [Montagio](https://github.com/Jubzh-29/montagio) - Viral video effects and camera moves as an open-source Higgsfield alternative. ★ 0 · AGPL-3.0
- [Vision Orchestrator](https://github.com/stellartune-studio/vision-orchestrator) - Chat with an LLM as the director while it grows a production blueprint: story, characters, materials, shots. ★ 0 · no license · [launch post](https://x.com/StellartuneCore/status/2116083086421319846)

## Effects and VFX

One-tap viral effects and plate-preserving VFX, the open version of Higgsfield presets.

- [Seam](https://github.com/jdnichollsc/seam) - Two shots in, one AI transition out: smoke, water and more. ★ 19 · MIT · [launch post](https://x.com/jdnichollsc/status/2116019265275150774)
- [SpEdE](https://github.com/Burgstall-labs/ComfyUI-SpEdE) - Click an object in a Gaussian splat, then remove, replace or restyle it. ★ 15 · AGPL-3.0 · [launch post](https://x.com/TheBurgstall/status/2115895644426834025)
- [Element Forge](https://github.com/Zitroffi/comfyui-element-forge) - AI VFX elements for your own footage: LTX-2.5 generates fire, lightning, smoke or particles, then Element Forge tracks, lights and layers them into the shot so they stay editable. ★ 8 · MIT · [launch post](https://www.reddit.com/r/comfyui/comments/1xjj8t8/element_forge_editable_ai_vfx_for_real_footage/)
- [FreeField](https://github.com/droppedmyza/freefield) - Higgsfield-style viral effects as ComfyUI workflows: one photo in, one shareable clip out. ★ 6 · MIT · [launch post](https://x.com/droppedmyza/status/2113669761762726058)
- [Pickups](https://github.com/thekhoma/pickups) - Video app on top of ComfyUI: pick a shot and change the weather, the lighting or what is in the frame. ★ 6 · MIT
- [LiDAR Lab](https://github.com/chinesepowered/hack-comfy) - LiDAR scan, clones, vanish and bullet-time effects that run on a laptop CPU. ★ 3 · Apache-2.0 · [launch post](https://x.com/ChinesePowered/status/2115643778866483208)
- [PlateLock](https://github.com/TusharTechs/platelock) - Plate-preserving generative VFX: add the effect, keep the original shot. ★ 3 · MIT
- [Forkfield](https://github.com/marciano71/forkfield) - Fork any video: Higgsfield-style effects where every clip keeps its recipe. ★ 1 · MIT
- [MOTNGRFX](https://github.com/okkazoo/MOTNGRFX) - Node pack and browser app that turns a song, a few images or a short brief into a kinetic-type motion graphic, with 3D type landing on the beat, on open weights. ★ 1 · Apache-2.0 · [launch post](https://x.com/OKKazooo/status/2116165296981688625)
- [Conjure](https://github.com/Orazen/conjure) - One photo, one tap, a whole VFX shot: gold statue, inflate, disintegrate, earth zoom-out on FLUX and LTX. ★ 0 · no license · [launch post](https://x.com/sudotarunai/status/2114782959060595110)
- [Earthfall](https://github.com/jamiejk/earthfall) - Higgsfield's Earth Zoom as an open app: pick a landmark, add a portrait, get a ten-second dive from orbit through cloud to that person. ★ 0 · GPL-3.0 · [launch post](https://x.com/jamie_jk/status/2116104753834803415)
- [FXjutsu](https://github.com/audriu/fxjutsu) - Higgsfield-style VFX presets on your own footage with LTX-2.5. ★ 0 · no license
- [One-take VFX](https://github.com/Kainotomic/one-take-vfx) - Add disintegrate, levitate, fire, portal or time-freeze to a phone clip with LTX 2.5. ★ 0 · MIT · [launch post](https://x.com/apple_techie/status/2115988400557981807)

## Camera, reshoot and previs

Re-shoot a clip from a new angle, plan camera moves in 3D, or check that a render followed the move.

- [Motion Previs Studio](https://github.com/navarisun1982/comfyui-motion-previs-studio) - 3D camera, character and motion previs, an open take on Higgsfield 3D. ★ 27 · MIT
- [360 Scout to Film](https://github.com/Alvinvision/360-Scout-to-Film-Consistency) - Camera-controlled 360 location references and multi-shot video inside ComfyUI. ★ 4 · MIT
- [ReAngle](https://github.com/Tekholms-LW/ReAngle) - Re-shoot any video from a new camera angle with ComfyUI and LTX-2.5. ★ 4 · Apache-2.0
- [TimeFlight](https://github.com/EmmanuelRiveros/TimeFlight) - Drone flights over real places that go back in time, from open geodata. ★ 4 · Apache-2.0
- [Hero Frame Rig](https://github.com/metababe-eth/hero-frame-rig) - Change the focus of any clip after it is made. ★ 3 · Apache-2.0 · [launch post](https://x.com/metababa_eth/status/2115097941488615565)
- [One-shot Multicam](https://github.com/apsolut/one-shot-multicam) - Turn one selfie video into a multi-camera edit. ★ 3 · MIT · [launch post](https://x.com/apsolut/status/2115181931788935556)
- [Open Higgsfield Reshoot](https://github.com/pyoonpyoon/open-higgsfield) - A 3D virtual film set that re-shoots any photo from a new angle. ★ 2 · MIT
- [Motion Guard](https://github.com/junco3/motion-guard) - Checks AI video against its 3D motion reference before an expensive upscale. ★ 1 · Apache-2.0
- [Open Cinema](https://github.com/LaytonGott/open-cinema) - Direct a shot, then change the lens afterwards: LTX-2 video plus physically based depth of field. ★ 1 · GPL-3.0
- [Shot Board](https://github.com/ArcSolver/shot-board) - Write one scene, get six shots, pick a hero take and redraw the cuts from it. ★ 1 · MIT · [launch post](https://x.com/arcsolve_ai/status/2115962151626313766)
- [Comfy Dial](https://github.com/ylchen333/comfy-dial) - Draw a camera move in 3D; it renders takes, measures the camera each one used and regenerates only the part that drifted. ★ 0 · MIT
- [previz2shot](https://github.com/MVOlekhno/previz2shot) - Blender grey playblast to a finished shot with FLUX.2 Klein and LTX-2.5. ★ 0 · MIT · [launch post](https://x.com/MaksimOlekhno/status/2115477011305058334)
- [Shot Director](https://github.com/bolttmade/shot-director) - Free previs, then one real render: a camera-move studio for Comfy. ★ 0 · MIT
- [ShotCheck](https://github.com/soft-jelly/shotcheck) - CPU-only camera-motion checker: match, mismatch or inconclusive. ★ 0 · MIT · [launch post](https://x.com/shotcheck_dev/status/2116061588457443645)
- [Toybox Director](https://github.com/mahdi-salmanzade/toybox-director) - Block a shot with toys on a 3D stage, then render it with open-weights LTX. ★ 0 · MIT · [launch post](https://x.com/MahdiSPHP/status/2115900815995183196)

## Films, music videos and stories

From a logline, a song or a document to a finished video.

- [Picky](https://github.com/chenthedesignmaker/ComfyUI-Picky) - Render a shot ten ways and keep the one you love. ★ 29 · GPL-3.0 · [launch post](https://x.com/DesignMakerChen/status/2115981756948164708)
- [Mondo Music Video](https://github.com/hodgemann/mondo-music-video) - Music-video studio with an actor protocol and optional MCP tools. ★ 12 · Apache-2.0 · [launch post](https://x.com/mann_hodge/status/2115910199978709476)
- [seriesmith](https://github.com/bgstratt/seriesmith) - A series config and markdown episode scripts in, finished episodes out: any shot on any model, on your own GPU or on Comfy's cloud. ★ 3 · MIT
- [Oneliner](https://github.com/thaohienhomes/oneliner) - Type one line, get a cinematic trailer on Comfy Cloud, LTX and ffmpeg. ★ 2 · MIT
- [OpenReel](https://github.com/smithysw7/openreel) - One logline in, a character-consistent short film out. ★ 2 · MIT · [launch post](https://x.com/ChigoQI/status/2114360365467480182)
- [Xenoform](https://github.com/tysonfarrington-cmyk/xenoform) - Song in, music video out, on your own GPU with open weights. ★ 2 · MIT · [launch post](https://x.com/tysostudio/status/2116015118178009491)
- [Hero's Journey](https://github.com/spiritform/herosjourney) - The monomyth as a generative experience starring you. ★ 1 · MIT · [launch post](https://x.com/spiritform/status/2115674848630591970)
- [LeafReel](https://github.com/Editorenbici/leafreel) - Any document into a narrated explainer video in 8 visual styles. ★ 1 · Apache-2.0 · [launch post](https://x.com/EditorEnBici/status/2115458693860933941)
- [Storyboard Studio](https://github.com/DialloWill/storyboard-studio) - Open rebuild of Higgsfield Cinema Studio for music-video storyboards. ★ 1 · MIT
- [Cat Tapes](https://github.com/Nemont3/cat-tapes) - Lo-fi VHS cat home videos made locally with LTX. ★ 0 · MIT
- [Crew Cut](https://github.com/GiveMePrompts/crew-cut) - A party game that makes a movie: phones become characters, friends direct scenes. ★ 0 · MIT

## Ads and UGC

Product ads, UGC-style clips and personalized spots.

- [ComfyField](https://github.com/ergophobian/comfyfield) - Insert your product into proven viral short-form formats and post on schedule. ★ 2 · MIT · [launch post](https://x.com/indefatigabile/status/2116060732353863810)
- [Open Ads Studio](https://github.com/jhoard/open-ads-studio) - Open-weights rebuild of Higgsfield Ads Studio with label-exact, compliance-checked product shots. ★ 2 · Apache-2.0
- [Reelmatch](https://github.com/vidyabharadwaj03/reelmatch) - Describe a campaign, drop in photos, get a UGC-style ad draft. ★ 1 · MIT
- [Urban Cuts](https://github.com/jk-automations/urban-cuts) - ComfyUI App Mode clone of Higgsfield Urban Cuts: a photo plus outfits or products. ★ 1 · Apache-2.0
- [HiggsOpen](https://github.com/kingofmit/ComfyUI-HiggsOpen) - Rebuild of Higgsfield Diffuse: a topic in, a viral short video out. ★ 0 · no license
- [Open Ad Studio](https://github.com/moonz-1/open-ad-studio) - Open-source AI creative agency on ComfyUI. ★ 0 · MIT

## Characters and datasets

Lock a character look, build LoRA datasets, keep identities consistent.

- [comfyui-sameface](https://github.com/fixed-42/comfyui-sameface) - Custom node that measures where an image edit moved the parts of a face and moves them back, on open weights. ★ 8 · Apache-2.0
- [Boson](https://github.com/0xMisterBailey/Boson) - Your taste as plain files in git that every next generation reads. ★ 1 · MIT
- [Character Lock](https://github.com/ZhuEvgeny/Character-lock-comfy) - One reference image in, a locked character look out. ★ 1 · MIT · [launch post](https://x.com/xx0618/status/2116021940309672166)
- [Dataset Forge](https://github.com/ToxicLizard99/Dataset-Forge) - One face in, a full character LoRA dataset out. ★ 1 · MIT
- [Soul Person Enhance](https://github.com/Soussa4535/SoulPersonEnhance) - Enhance each person in a photo separately, or only the ones you pick. ★ 1 · AGPL-3.0 · [launch post](https://x.com/Soussa_3d/status/2116049274685313503)

## Canvases, front ends and tools

Node canvases, web UIs and helpers that put a friendlier face on ComfyUI.

- [ComfyArt](https://github.com/jtydhr88/ComfyArt) - Free design canvas on your own ComfyUI: an infinite tldraw canvas with a design agent; image, video, audio and 3D run locally. ★ 411 · MIT · [launch post](https://x.com/jtydhr88/status/2114927438518219073)
- [ComfyUI-Continuity](https://github.com/roadmaus/ComfyUI-Continuity) - One node for AI video and stills: write a prompt, attach media with @ and press Render; six model families, all local through ComfyUI core. ★ 139 · MIT
- [Open Source Canvas](https://github.com/raph651/open-source-canvas) - Node canvas that runs ComfyUI workflows. ★ 106 · MIT · [launch post](https://x.com/RaphaelLiu10/status/2115913910075449637)
- [KubaNodes](https://github.com/kubakubkub/ComfyUI_KubaNodes) - Visual toolset for pictures made of parts: projection mapping with regions, per-region diffusion, a director window, and video and 3D scene tools. ★ 10 · GPL-3.0
- [Freavy](https://github.com/FrameDeptCo/freavy) - Local-first node canvas for AI image and video on ComfyUI. ★ 7 · MIT
- [ComfyUI-Spool](https://github.com/doubletwisted/ComfyUI-Spool) - Video timeline for ComfyUI: queue workflows per clip, review the generated takes and assemble a sequence. ★ 4 · GPL-3.0
- [Justae Flow](https://github.com/HomoLapis/justae-flow) - ComfyUI inside the open-source EffectCraft editor. ★ 2 · GPL-3.0
- [Ask Higgsy](https://github.com/mhaihq/hana-comfy-hack) - Video-call a small animated guide that helps you pick the right model. ★ 1 · MIT · [launch post](https://x.com/Hello_Sinha/status/2115965713789935964)
- [FrameCommander](https://github.com/welski3/framecommander) - Web UI for MiniMax H3 video through ComfyUI workflows on RunningHub. ★ 1 · MIT · [launch post](https://x.com/itswelski/status/2116007537149710584)
- [RenderRepo](https://github.com/crystalattice/CBI_RenderRepo) - Local-first package manager for ComfyUI workflows: discover, inspect, install and open workflows while reusing the models and nodes you already have. ★ 1 · GPL-3.0 · [launch post](https://www.reddit.com/r/comfyui/comments/1xfkqzq/my_entry_for_comfys_open_source_higgsfield/)
- [Open Studio for Affinity](https://github.com/viriato68/open-studio-for-affinity) - Local AI editing inside Affinity, powered by ComfyUI. ★ 0 · MIT
- [openfield (Blender MCP)](https://github.com/obaidiDev/openfield) - The Higgsfield Blender MCP stack made local-first with a self-hosted gateway. ★ 0 · GPL-3.0

## Beyond the challenge

Older open-source Higgsfield alternatives on GitHub, most of them cloud front ends that need someone's API key.

- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) - Formerly Open-Higgsfield-AI. The biggest web and desktop studio; cloud models through Muapi.ai. ★ 31,970 · MIT
- [open-higgsfield](https://github.com/wide-trace/open-higgsfield) - Next.js web app with a hosted demo; needs a platform API key. ★ 5,173 · no license
- [HeliosGen](https://github.com/SegFault42/HeliosGen) - Tauri desktop app with a Mac build; generations through kie.ai. ★ 3,224 · no license
- [LTX Desktop](https://github.com/Lightricks/LTX-Desktop) - Lightricks' own desktop app for running LTX video models locally. ★ 2,199 · Apache-2.0
- [BeatDesign](https://github.com/BeatAPI/BeatDesign) - Local web workspace on Node.js; generations through BeatAPI. ★ 306 · Apache-2.0
- [Kawarimi](https://github.com/jutsuhq/kawarimi-local-character-swap) - Local character swap for Windows and Linux on Wan 2.2 Animate through ComfyUI. Made by the maintainers of this list. ★ 2 · MIT

## Contributing

Missing a project? Open a pull request that adds it to [projects.json](projects.json) with a one-line summary, then run `node scripts/build.mjs` to refresh the stats and this README. Projects need a public repository with a README.

See also [Awesome Higgsfield](https://github.com/jutsuhq/awesome-higgsfield) for SDKs, MCP servers and agent skills built on Higgsfield itself.

Maintained by [Jutsu Studio](https://jutsustudio.com/), the open-source Higgsfield desktop app for Mac ([GitHub](https://github.com/jutsuhq/jutsu-studio)).

## License

[CC0 1.0](LICENSE). To the extent possible under law, the maintainers waive all copyright to this list.
