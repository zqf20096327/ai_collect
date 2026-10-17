# Awesome GPT-Image-2.5 Prompts

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

A curated collection of prompts, techniques, and API notes for **ChatGPT Images 2.5** — OpenAI's newest image model, released September 8, 2026, and its API counterparts **GPT-Image-2.5 Flare** and **GPT-Image-2.5 Sunburst**. This repository tracks what's actually new in 2.5 (sharper details, more precise single-element editing, better multi-turn consistency, faster generation) and collects prompt patterns tuned to those improvements.

Whether you're building an image generation app, upgrading a `gpt-image-2` integration, or just want prompts that exploit 2.5's editing precision, you'll find practical patterns here.

> **Want to use GPT-Image-2.5 without an OpenAI account?** **[MuAPI](https://muapi.ai)** is bringing GPT-Image-2.5 online as a hosted API. The landing page is live now at [muapi.ai/gpt-image-2.5](https://muapi.ai/gpt-image-2.5) (**coming soon** — endpoints are being wired up); in the meantime [GPT-Image-2](https://muapi.ai/playground/gpt-image-2-text-to-image) is available today with a simple REST call. [Get your API key →](https://muapi.ai)

> **API Usage:** Prompts below are written for the [OpenAI Images API](https://platform.openai.com/docs/api-reference/images) using models `gpt-image-2.5-flare` / `gpt-image-2.5-sunburst`, and apply equally to ChatGPT Images 2.5 in the ChatGPT app.

```python
import openai

client = openai.OpenAI()
response = client.images.generate(
    model="gpt-image-2.5-flare",   # or gpt-image-2.5-sunburst for premium precision
    prompt="<paste any prompt from this list>",
    size="1024x1024",
    quality="high",
    n=1,
)
print(response.data[0].url)
```

---

## Related Projects

- [GPT Image 2 playground](https://muapi.ai/playground/gpt-image-2-text-to-image) — Try the current-generation model on MuAPI while 2.5 rolls out.
- [MuAPI GPT-Image-2.5 landing page](https://muapi.ai/gpt-image-2.5) — Coming soon: hosted API access to Flare and Sunburst.
- [MuAPI API reference](https://muapi.ai/docs/api-reference) — Endpoint and prediction lifecycle documentation.
- [Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts) — The prior-generation prompt collection this repo builds on.
- [Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills) — Run these prompts as AI agent skills in Claude Code, Cursor, and Gemini CLI.
- [muapi-cli](https://github.com/SamurAIGPT/muapi-cli) — Run image-generation prompts via CLI with MuAPI.
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — Open-source generative media studio covering image, video, and audio generation.
- [awesome-ai-image-models](https://github.com/Anil-matcha/awesome-ai-image-models) — Compare AI image models by API, price & quality.

## What's New in 2.5

Per [OpenAI's announcement](https://openai.com/index/introducing-chatgpt-images-2-5/), Images 2.5 is a meaningful step up from 2.0, not just a speed bump:

- **~50% lower generation latency** than Images 2.0
- **Reference-photo fidelity** — better at preserving the actual subject (face, pet, product) across new settings, styles, and compositions
- **Precision editing** — changes only what you ask for; the rest of the image (background, composition, unrelated subjects) stays untouched, even in complex scenes
- **Multi-turn consistency** — earlier edits in a conversation stay intact as you keep iterating, instead of drifting or degrading
- **Better complex-instruction handling** — more reliable with layered/structured prompts, transparent backgrounds, and real-world factual content
- **Sketch input** — draw a rough layout/contour in ChatGPT (`@Sketch`) and use it as a visual guide for the final image
- Two API tiers: **Flare** (default, fastest, same quality/editing gains) and **Sunburst** (slower, tuned for maximum edit precision on premium creative work)

---

## Table of Contents

- [Reference Photo Fidelity](#reference-photo-fidelity)
- [Precision Editing (Single-Element Changes)](#precision-editing-single-element-changes)
- [Multi-Turn Editing Chains](#multi-turn-editing-chains)
- [Sketch-to-Image](#sketch-to-image)
- [Complex Layouts & Transparent Backgrounds](#complex-layouts--transparent-backgrounds)
- [Infographics & Typography](#infographics--typography)
- [Campaign & Product Creative](#campaign--product-creative)
- [Resources & API Docs](#resources--api-docs)
- [Contributing](#contributing)

---

## Reference Photo Fidelity

Prompts that lean on 2.5's improved subject-preservation from a reference image — the model is more likely to keep the actual person/pet/object recognizable while changing everything around it.

### Baby Portrait Remix

**Prompt:**
```
Using the attached photo of the baby as the exact reference for facial features and expression, generate a soft studio portrait: warm golden-hour lighting, neutral cream backdrop, the baby wrapped in a cream knit blanket, gentle smile, shallow depth of field. Keep the baby's face, proportions, and skin tone fully consistent with the reference photo — only the setting, lighting, and wardrobe should change.
```

### Pet in Costume, New Scene

**Prompt:**
```
Using the attached photo of the dog as reference, keep the dog's exact breed markings, fur pattern, and face fully recognizable. Dress the dog in a tiny superhero costume and place it standing heroically on a rooftop at sunset, cape blowing in the wind, cinematic lighting. Do not alter the dog's face or proportions.
```

### Photobooth-to-Headshot

**Prompt:**
```
Using the attached photobooth strip as reference for the subject's face, generate a single professional LinkedIn-style headshot: neutral gray background, soft studio lighting, navy blazer, confident closed-mouth smile. Preserve the exact facial structure, skin tone, and hairstyle from the reference photos.
```

### Composite Party Photo

**Prompt:**
```
Using the three attached individual photos as face references, generate one composite group photo of all three people standing together at an outdoor birthday party, string lights in the background, everyone laughing, natural evening light. Each person's face must stay recognizable and consistent with their own reference photo.
```

### "Making the Bed" Everyday Scene

**Prompt:**
```
Using the attached photo of the bedroom as the exact reference for layout, furniture, and wall color, generate an image of the same room with the bed now neatly made with fresh white linens and plumped pillows, morning light coming through the window. Keep every piece of furniture, the wall art, and the room proportions identical to the reference.
```

---

## Precision Editing (Single-Element Changes)

2.5's headline improvement is editing only what you ask for. These prompts are written to isolate one change and explicitly protect everything else.

### Swap One Product, Keep the Set

**Prompt:**
```
In the attached product photo, replace only the beverage bottle in the center with a matte black can labeled "PEAK", keeping the exact same lighting, shadows, reflective surface, background props, and camera angle. Do not change anything else in the scene.
```

### Change Background, Keep Subject Pixel-Identical

**Prompt:**
```
Take the attached portrait and replace only the background with a blurred golden-hour city skyline. Keep the subject's pose, expression, clothing, lighting on the face, and edge detail on the hair exactly as in the original — do not regenerate or alter the subject.
```

### Update Copy on an Existing Poster

**Prompt:**
```
On the attached poster, change only the headline text from "SUMMER SALE" to "FALL COLLECTION" in the same font, size, color, and position. Keep every other design element, image, and layout exactly as it is.
```

### Recolor a Single Garment

**Prompt:**
```
In the attached fashion photo, change only the color of the jacket from red to forest green, preserving the fabric texture, folds, shadows, and every other element of the outfit and background exactly as shown.
```

---

## Multi-Turn Editing Chains

Prompts written as a sequence — each step should build on the last without the earlier edits drifting or degrading.

### Full-Body Outfit Build (Multi-Turn)

**Turn 1:**
```
Take the attached full-body photo and change the top to a white linen shirt, keeping the pose, face, and background identical.
```
**Turn 2 (apply to the result of Turn 1):**
```
Now change the pants to tailored charcoal trousers, keeping the shirt, face, pose, and background exactly as they now are.
```
**Turn 3 (apply to the result of Turn 2):**
```
Now add brown leather loafers, keeping everything else in the image identical to the previous step.
```

### Multi-City Travel Ticket Series

**Turn 1:**
```
Design a vintage-style train ticket for a trip from "Paris" to "Lisbon", cream cardstock texture, art-deco border, punch-hole detail, fictional route number and date.
```
**Turn 2 (apply to the result of Turn 1):**
```
Now generate the same ticket design and layout for a second leg: "Lisbon" to "Marrakech", keeping the exact border style, cardstock texture, typography, and punch-hole placement identical — only the city names, route number, and date should change.
```

### Rotating Product Cube (Multi-Turn)

**Turn 1:**
```
Generate a product render of a glass cube containing a single red rose, studio lighting, pure white background, front-facing angle.
```
**Turn 2 (apply to the result of Turn 1):**
```
Now rotate the same cube 45 degrees to show the side face, keeping the lighting, rose position inside the cube, glass material, and background exactly consistent with the previous image.
```

---

## Sketch-to-Image

Prompts meant to pair with a rough sketch (drawn via `@Sketch` in ChatGPT, or a simple line drawing supplied as a reference image).

### Room Layout from Sketch

**Prompt:**
```
Using the attached rough sketch as the layout reference for furniture placement, generate a photorealistic modern living room: light oak flooring, sage green accent wall, natural daylight from the window shown in the sketch. Match the sketch's room proportions and furniture positions exactly.
```

### Outfit Concept from Sketch

**Prompt:**
```
Using the attached sketch as the silhouette and construction reference, generate a photorealistic fashion photo of the outfit: flowing midi dress in dusty rose fabric, cinched waist, studio lighting, full-body shot on a plain background. Follow the sketch's proportions and design lines closely.
```

---

## Complex Layouts & Transparent Backgrounds

Prompts that push 2.5's improved handling of structured layouts and alpha-channel output.

### App Icon Set, Transparent Background

**Prompt:**
```
Generate a set of 6 minimalist app icons on a transparent background: camera, chat bubble, calendar, settings gear, heart, and share arrow. Consistent line weight, rounded corners, single accent color (#4F46E5), no background fill, evenly spaced in a grid.
```

### Sticker Sheet, Transparent Background

**Prompt:**
```
Create a die-cut sticker sheet of 8 cute cartoon fox stickers in different poses (waving, sleeping, jumping, waving a flag, drinking coffee, reading, dancing, winking), each with a white die-cut border, transparent background, consistent art style and color palette across all 8.
```

### Structured UI Concept

**Prompt:**
```
Generate a high-fidelity settings screen for a fitness app: top status bar, "Settings" title, grouped list sections (Account, Notifications, Privacy, Billing) each with an icon, label, and chevron, toggle switches where relevant, bottom tab bar with 4 icons. Clean modern iOS-style design, consistent spacing and typography throughout.
```

---

## Infographics & Typography

### Coffee Brewing Method Comparison

**Prompt:**
```
Design a clean infographic comparing four coffee brewing methods: pour-over, French press, espresso, and cold brew. Include for each: brew time, grind size, and flavor profile, using icons and a consistent card layout. Color palette: coffee brown, cream, charcoal. All text must be sharp and legible.
```

### Product Launch Announcement Card

**Prompt:**
```
Design a 4:5 social announcement card for a product launch. Headline "Introducing Nova", subheading "The lightest laptop we've ever made", small product render in the center, minimalist background gradient (deep navy to black), clean sans-serif typography, subtle glow around the product.
```

---

## Campaign & Product Creative

### Skincare Hero Shot

**Prompt:**
```
Generate a premium skincare product hero shot: frosted glass bottle with gold cap on a wet marble surface, soft water droplets, diffused daylight, minimal shadow, shallow depth of field, editorial beauty-brand aesthetic. No text on the bottle label — leave it blank for overlay.
```

### Seasonal Retail Banner

**Prompt:**
```
Design a wide retail banner (16:9) for a fall footwear sale: pair of leather boots on fallen autumn leaves, warm amber and rust color grading, soft bokeh background, space reserved on the left third for text overlay, no text baked in.
```

---

## Resources & API Docs

### Official References

- [OpenAI: Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/) — the official announcement this repo is based on
- [OpenAI Images API Reference](https://platform.openai.com/docs/api-reference/images)
- [OpenAI Pricing](https://openai.com/api/pricing)

### API Quick Reference

```python
# Standard generation — Flare (default, fastest)
response = client.images.generate(
    model="gpt-image-2.5-flare",
    prompt="your prompt here",
    size="1024x1024",      # 1024x1024, 1536x1024, 1024x1536, auto
    quality="high",
    n=1,
)

# Premium precision editing — Sunburst
response = client.images.edit(
    model="gpt-image-2.5-sunburst",
    image=open("original.png", "rb"),
    prompt="change only the [element] — keep everything else identical",
)
```

### Prompt Engineering Tips for 2.5

1. **State what must stay the same, not just what should change** — 2.5 rewards explicit "keep X identical" instructions during edits far more reliably than 2.0 did.
2. **Chain edits one change at a time** — multi-turn consistency is the headline improvement; don't bundle five changes into a single edit if you need precision on each.
3. **Reference photos work better now** — lean on them for subject fidelity instead of describing a face/product from scratch.
4. **Ask for transparent backgrounds explicitly** — layout and alpha-channel handling is meaningfully better than prior versions.
5. **Pick the right tier** — use Flare for iteration speed and high-volume generation, Sunburst when a single edit needs maximum precision (e.g. final campaign creative).

---

## Use GPT-Image-2.5 via MuAPI

[MuAPI](https://muapi.ai) is bringing GPT-Image-2.5 online as a hosted API — no OpenAI account required. The [landing page](https://muapi.ai/gpt-image-2.5) is live now; the endpoints themselves are **coming soon**.

Flare and Sunburst will ship as four separate MuAPI endpoints (one per tier, per mode), matching MuAPI's usual per-model catalog pattern rather than a single endpoint with a tier parameter:

- `gpt-image-2.5-flare-text-to-image`
- `gpt-image-2.5-flare-image-to-image`
- `gpt-image-2.5-sunburst-text-to-image`
- `gpt-image-2.5-sunburst-image-to-image`

In the meantime, [GPT-Image-2](https://muapi.ai/playground/gpt-image-2-text-to-image) is available today via the same pattern this collection's prior-generation companion repo, [Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts), documents:

```python
import httpx, time

API_KEY = "your-muapi-key"
BASE = "https://api.muapi.ai/api/v1"

resp = httpx.post(
    f"{BASE}/gpt-image-2-text-to-image",
    headers={"x-api-key": API_KEY},
    json={"prompt": "A photorealistic image of a red panda in a bamboo forest at golden hour"},
)
request_id = resp.json()["request_id"]

while True:
    result = httpx.get(f"{BASE}/predictions/{request_id}/result", headers={"x-api-key": API_KEY}).json()
    if result["status"] == "completed":
        print(result["outputs"])
        break
    time.sleep(3)
```

Get your API key at [muapi.ai](https://muapi.ai). Watch [muapi.ai/gpt-image-2.5](https://muapi.ai/gpt-image-2.5) for the moment 2.5 endpoints go live.

---

## Contributing

Contributions are welcome! Submit a Pull Request to add prompts that specifically exercise what's new in 2.5 (precision editing, multi-turn consistency, reference-photo fidelity, sketch input, transparent backgrounds).

**Guidelines:**
- Include the full prompt text (or full turn sequence for multi-turn prompts)
- Note which 2.5 capability the prompt is meant to showcase
- Categorize appropriately
- Example images are encouraged but not required

---

## License

This project is licensed under the Creative Commons Attribution 4.0 International License — see the [LICENSE](LICENSE) file for details.

*Community-maintained. Not affiliated with OpenAI.*
