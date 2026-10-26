# Hailuo AI

Hailuo is MiniMax's video generation model family, known for physically realistic motion, camera control and low per-clip cost.

> **Try Hailuo AI online →** [https://hailuo-ai.pro](https://hailuo-ai.pro?utm_source=github&utm_medium=ugc&utm_campaign=hailuo-official&utm_content=readme-top&utm_term=tier-b)

Hailuo AI is the video generation product and model family from MiniMax, the Shanghai AI company that also builds the MiniMax language models, the Speech text-to-speech line and the Talkie companion app. The first Hailuo video model, video-01, launched in late summer 2024 and drew attention for six-second 720p clips with smooth, believable human motion at a time when most competitors still struggled with hands and walking. Since then the family has grown through specialised variants (video-01-live for 2D animation, S2V-01 for subject reference, the Director models for camera control) to Hailuo 02 in June 2025 and Hailuo 2.3 in October 2025.

Hailuo 02 introduced a redesigned architecture that MiniMax calls Noise-aware Compute Redistribution, allowing native 1080p output and clips of 6 or 10 seconds while keeping generation cost low. Its showcase examples, gymnasts, divers, animals and crowd scenes with convincing physics, placed it near the top of the Artificial Analysis image-to-video leaderboard on release. Hailuo 2.3 refined motion, facial expression and stylised rendering, and shipped alongside a Fast variant for cheaper, quicker drafts. Camera control is a long-standing strength: bracketed commands such as [Pan left], [Zoom in] or [Tracking shot] in the prompt map directly to camera moves.

In the market Hailuo competes with Kuaishou's Kling, ByteDance's Seedance, Google's Veo 3 and OpenAI's Sora 2. Its positioning is value and motion quality rather than feature breadth: it does not generate audio natively and offers fewer editing modes than Veo 3.1 or Seedance 2.0, but its per-clip prices are among the lowest of the major hosted models and the consumer app at hailuoai.video has a generous free tier.

## Contents

- [What Hailuo AI can do](#what-hailuo-ai-can-do)
- [Versions](#versions)
- [How to access Hailuo AI](#how-to-access-hailuo-ai)
- [Prompt examples](#prompt-examples)
- [Hailuo AI vs alternatives](#hailuo-ai-vs-alternatives)
- [Pricing](#pricing)
- [FAQ](#faq)
- [Links](#links)

## What Hailuo AI can do

- Text-to-video and image-to-video, with a first frame or a first-and-last-frame pair as input.
- Clip lengths of 6 or 10 seconds at 768p or 1080p on Hailuo 02 and 2.3 (10 second clips are limited to 768p), 24 or 25 fps.
- Subject reference (S2V-01 and later): upload one photo of a person and the model keeps that face and appearance across new scenes.
- Camera control through bracketed commands in the prompt, such as [Push in], [Pull out], [Pan left], [Tilt up], [Tracking shot], [Static shot], which can be combined in one instruction.
- Realistic physics and complex motion: sports, dance, animals, fluids and fabric are consistent strengths since Hailuo 02.
- Stylised output: anime, 2D illustration and 3D animation looks, improved in Hailuo 2.3, with video-01-live as the earlier dedicated model for animating illustrations.
- Hailuo 2.3 Fast for lower-latency, lower-cost generations, and Hailuo Agent in the app for multi-shot storyboards from a single brief.
- API access through the MiniMax platform with the same models, plus separate MiniMax speech and music models that can be paired with the silent video.

Known limitations: Hailuo generates no native audio, so dialogue and sound must be added separately. Maximum clip length is 10 seconds and 1080p is only available at 6 seconds. There is no scene extension, video-to-video editing or multi-image fusion comparable to Veo 3.1 or Seedance 2.0, and prompt adherence for complex multi-step actions is weaker than for camera and single-subject motion. The free tier of the app applies a watermark and queues generations behind paid users, and content filters block real public figures and explicit material. Text inside the frame is unreliable.

## Versions

| Version | Released | Notes |
|---|---|---|
| video-01 (Hailuo AI launch) | 2024-09 | First public model: 6 second 720p clips at 25 fps, text-to-video, image-to-video added soon after. |
| video-01-live and S2V-01 | 2024-12 | video-01-live animates 2D illustrations with stable line art; S2V-01 (January 2025) adds subject reference from a single photo. |
| T2V-01-Director and I2V-01-Director | 2025-02 | Camera control models that follow bracketed commands such as [Pan left] and [Zoom in]. |
| Hailuo 02 | 2025-06 | New Noise-aware Compute Redistribution architecture; 768p and 1080p, 6 or 10 seconds, strong physics; near the top of the Artificial Analysis image-to-video leaderboard at release. |
| Hailuo 2.3 and 2.3 Fast | 2025-10 | Improved motion dynamics, facial expression and stylised rendering; Fast variant for cheaper drafts. |

## How to access Hailuo AI

Hailuo is a closed, hosted model. Official ways to use it:

- Hailuo AI web app (hailuoai.video) and mobile apps: free daily credits with a watermark and slower queue, plus Standard and Unlimited subscriptions that remove the watermark, add fast-track generation and unlock the newest models and 1080p.
- MiniMax API: the international developer platform at platform.minimax.io exposes MiniMax-Hailuo-02, MiniMax-Hailuo-2.3, MiniMax-Hailuo-2.3-Fast, the Director models and S2V-01, billed per clip by resolution and duration; a separate China platform serves domestic customers.
- Third-party hosts: fal.ai, Replicate, WaveSpeed and others mirror the Hailuo endpoints, usually within days of a MiniMax release.
- Bundled in creative tools such as Freepik, Krea and several video editors that license the API.

The consumer app requires an account and its free queue can be slow at peak times; the API requires a MiniMax platform account with prepaid balance, and the China and international platforms are separate. To try the model without an account, a subscription or a queue, [Hailuo AI](https://hailuo-ai.pro) offers pay-per-generation access.

**Fastest way to try it:** [Try Hailuo AI online](https://hailuo-ai.pro?utm_source=github&utm_medium=ugc&utm_campaign=hailuo-official&utm_content=readme-access&utm_term=tier-b) — no waitlist, runs in the browser.

## Prompt examples

**Camera-controlled reveal**

```text
[Push in][Pan right] A lone hiker stands on a granite ledge above a sea of clouds at sunrise, wind moving her jacket, warm rim light from the right, cinematic 35mm look, slow and steady camera.
```

**Physics showcase**

```text
A springer spaniel leaps off a wooden dock into a calm lake, slow motion, water spraying in an arc, sunlight glinting on the droplets, [Tracking shot] following the dog from the side, 10 seconds.
```

**Subject reference portrait**

```text
Using the reference photo, the same man walks through a crowded Tokyo crossing at night in a grey overcoat, neon reflections on wet pavement, [Static shot] as he approaches the camera and looks up, shallow depth of field.
```

**Anime style (2.3)**

```text
Anime style, a girl with short blue hair rides a bicycle down a hill lined with cherry trees, petals streaming past, bright spring afternoon, clean line art and flat shading, [Tilt down] from the treetops to the road.
```

**First and last frame**

```text
Start frame: a closed vintage suitcase on a bed. End frame: the suitcase open, filled with neatly folded clothes and a passport. 6 seconds, hands entering the frame to open and pack it, soft window light, [Static shot].
```

## Hailuo AI vs alternatives

| Model | Max resolution / duration | Native audio | Editing / references | Access | Price tier |
|---|---|---|---|---|---|
| Hailuo 2.3 (MiniMax) | 1080p at 6 s, 768p at 10 s | No | First/last frame, subject reference, camera commands | Hailuo app, MiniMax API, fal, Replicate | Low |
| Kling 2.6 (Kuaishou) | 1080p, 5 to 10 s | Yes | Elements references, first/last frame, motion brush | Kling app, Kling API, fal | Medium |
| Veo 3.1 (Google) | 1080p, 4K upscale, 8 s with extension | Yes, dialogue with lip sync | Up to 3 references, first/last frame, extend | Gemini app, Flow, Gemini API, Vertex AI | Medium-high |
| Seedance 2.0 (ByteDance) | 1080p, up to 15 s | Yes, dialogue with lip sync | Up to 9 images, 3 videos, 3 audio references | Dreamina, CapCut, Volcano Engine / BytePlus API | Low-medium |
| Sora 2 (OpenAI) | 1080p (Pro), up to 15 s | Yes | Remix, cameos | Sora app, ChatGPT, OpenAI API | Medium-high |

Hailuo is the value pick of the group: it costs the least per clip, has a usable free tier and matches or beats the others on raw motion realism and camera control. It gives up native audio, longer clips and the richer reference and editing systems that Veo 3.1 and Seedance 2.0 offer, so it suits silent b-roll, social clips and animation more than dialogue-driven scenes.

## Pricing

As of the last public information, MiniMax bills the Hailuo API per generated clip according to model, resolution and duration; Hailuo 02 launched with 768p six-second clips at $0.28, 768p ten-second clips at $0.56 and 1080p six-second clips at $0.49, and Hailuo 2.3 is priced in the same range with the Fast variant cheaper. The consumer app uses credits: a free daily allowance with a watermark, then Standard and Unlimited monthly plans that remove the watermark, unlock 1080p and the newest models and add priority generation. Plan prices have changed several times, so check hailuoai.video and platform.minimax.io for current figures.

For occasional use, [Hailuo AI](https://hailuo-ai.pro) provides pay-per-generation access with no subscription.

## FAQ

**What is Hailuo AI?**

Hailuo AI is the video generation model family and app from MiniMax, a Shanghai AI company. Its current models, Hailuo 02 and Hailuo 2.3, generate 6 or 10 second clips at up to 1080p with realistic motion and prompt-driven camera control.

**Is Hailuo AI free?**

Partly. The hailuoai.video app gives free daily credits with a watermark and a slower queue; removing the watermark, 1080p and the newest models require a Standard or Unlimited subscription, and the API is pay-per-clip.

**Is there a Hailuo AI API?**

Yes. MiniMax serves MiniMax-Hailuo-02, MiniMax-Hailuo-2.3, the Fast variant, the Director models and S2V-01 through platform.minimax.io with per-clip billing, and hosts such as fal.ai and Replicate mirror the endpoints.

**Does Hailuo AI have an official GitHub repository?**

No. Hailuo is a closed, hosted model and MiniMax has not released weights or an official repository for it. This page collects publicly available information.

**How do I try Hailuo AI online?**

Sign up at hailuoai.video for free credits, or use the MiniMax API. For pay-per-generation access with no subscription or queue, use https://hailuo-ai.pro.

**What are the limits of Hailuo AI?**

Clips are at most 10 seconds and 1080p is limited to 6 seconds, there is no native audio, no scene extension or video-to-video editing, the free tier is watermarked and queued, and content filters block real public figures and explicit material.

**How does camera control work in Hailuo?**

You put bracketed commands in the prompt, such as [Pan left], [Push in], [Tilt up] or [Tracking shot], and the model maps them to the corresponding camera move. Several commands can be combined in one bracket to describe a compound move.

## Links

- [Hailuo AI (official)](https://hailuoai.video)
- [MiniMax developer platform](https://platform.minimax.io)
- [MiniMax](https://www.minimax.io)
- [Try Hailuo AI online](https://hailuo-ai.pro)

---

*This is an independent, community-maintained information repository about Hailuo AI. It is not affiliated with, endorsed by, or sponsored by MiniMax. All trademarks belong to their respective owners. Corrections welcome via issues.*



_Last reviewed: 2026-09-22_
