# Consistent AI Character Prompts

A free, open prompt library for creating **consistent AI virtual influencers and AI models** — the same character across many scenes, outfits, and lighting setups.

> The hardest problem in AI image generation isn't quality — it's **consistency**. Generic tools (Midjourney, DALL·E, raw Stable Diffusion) give you a different face every time. This library + a character-specific model (LoRA) keeps the *same* identity across an entire feed, catalog, or comic.

## Why consistency matters
- **Virtual influencers** need the same face every post to build a believable persona.
- **Ecommerce** needs one model across the whole product catalog.
- **Comics / webtoons** need the protagonist to look the same in every panel.
- **Brand ambassadors** need a recognizable, reusable face.

## The scene prompt library

Pair each scene prompt with your character trigger (LoRA token) or reference. Designed for portrait 9:16 social content.

| Scene | Prompt |
|---|---|
| Cafe | `cinematic lifestyle photo in a cozy cafe, sitting by the window with a latte, soft natural morning light, candid editorial style, fashionable casual outfit, warm tones, shallow depth of field` |
| Beach (golden hour) | `lifestyle photo at the beach during golden hour, flowing summer dress, warm sunset light, ocean background, candid editorial style, medium shot` |
| Street style | `street style photo in a stylish city, chic urban outfit, confident pose, soft daylight, editorial aesthetic, medium shot` |
| Gym / fitness | `fitness photo in a modern bright gym, stylish activewear, candid post-workout moment, natural light, medium shot` |
| Elegant dinner | `evening photo at an upscale restaurant, chic dinner outfit, warm ambient candle lighting, sophisticated editorial style, medium shot` |
| Travel | `travel photo at a scenic European old town street, stylish travel outfit with sunglasses, bright daylight, wanderlust aesthetic, medium shot` |
| Mirror OOTD | `mirror selfie OOTD in a stylish bedroom, trendy casual outfit, holding phone, natural window light, authentic influencer aesthetic` |
| Rooftop sunset | `golden hour rooftop photo overlooking city skyline, chic evening outfit, wind in hair, warm sunset glow, aspirational aesthetic` |
| Bookstore | `cozy candid photo in a charming bookstore cafe, smart casual outfit holding a book, warm indoor light` |
| Autumn park | `autumn park walk, stylish coat and scarf, fallen leaves background, soft overcast light, seasonal aesthetic` |
| Hotel morning | `luxury hotel room morning photo by the window, elegant loungewear with coffee, soft morning light` |
| Studio portrait | `clean studio portrait with soft pastel background, fashionable minimalist outfit, professional beauty lighting, editorial aesthetic` |
| Office / business | `professional photo in a bright modern office, tailored business casual outfit, confident posture by a glass wall, soft daylight, corporate editorial style, medium shot` |
| Poolside summer | `poolside summer photo at a resort, stylish swimsuit with a light cover-up and sunglasses, bright midday sun, turquoise water background, vacation aesthetic, medium shot` |
| Snow / winter | `winter photo in a snowy street, cozy knit sweater with a wool coat and scarf, soft diffused snowfall light, warm breath in cold air, seasonal editorial style, medium shot` |
| Garden / floral | `spring garden photo surrounded by blooming flowers, flowing floral dress, soft golden backlight, dreamy romantic aesthetic, medium shot` |
| Art gallery | `candid photo in a minimalist art gallery, chic monochrome outfit, looking at a painting, soft museum lighting, sophisticated editorial style, medium shot` |
| Kitchen / cooking | `lifestyle photo cooking in a bright modern kitchen, casual apron over a stylish outfit, candid moment plating food, warm natural light, authentic aesthetic` |
| Yoga / wellness | `wellness photo in a serene studio, fitted activewear in a calm stretching pose, soft morning light through large windows, mindful aesthetic, medium shot` |
| Nightlife / city lights | `evening photo on a vibrant city street at night, chic going-out outfit, bokeh neon lights background, cinematic low light, confident aesthetic, medium shot` |
| Coffee co-working | `candid photo working at a stylish coffee shop, smart casual outfit with a laptop, focused expression, warm afternoon window light, modern creative aesthetic` |
| Festival / outdoor | `outdoor festival photo in a sunny open field, boho-chic outfit with layered accessories, warm afternoon light, joyful candid moment, lifestyle aesthetic, medium shot` |

## Trending aesthetic prompts (2026)

Beyond plain scenes, most social search now happens by **aesthetic**. Pair your character trigger with these trend-driven looks — each is portrait 9:16, medium shot, face-forward. Vary outfit/setting freely; keep the identity descriptors fixed.

| Aesthetic | Prompt |
|---|---|
| Old money | `old money aesthetic outfit, tailored neutral knit and trousers, country-club setting, soft overcast daylight, understated luxury, editorial style, medium shot` |
| Quiet luxury | `quiet luxury aesthetic, cashmere and minimalist tailoring in beige tones, refined modern interior, soft window light, expensive-but-subtle styling, medium shot` |
| Clean girl | `clean girl aesthetic, slicked-back bun, gold hoop earrings, dewy minimal makeup, neutral tank, bright airy background, natural daylight, medium shot` |
| That girl | `that girl aesthetic, matching athleisure set, matcha in hand, wellness morning routine, bright minimalist apartment, soft natural light, medium shot` |
| Coquette | `coquette aesthetic, soft pink outfit with lace and bow details, feminine romantic styling, dreamy soft focus, warm natural light, medium shot` |
| Tomato girl summer | `tomato girl summer aesthetic, red and white linen outfit, Mediterranean coastal village, bright midday sun, joyful vacation mood, medium shot` |
| Dark academia | `dark academia aesthetic, tweed blazer and turtleneck, old library with warm lamplight, moody scholarly atmosphere, editorial style, medium shot` |
| Cottagecore | `cottagecore aesthetic, flowing floral prairie dress, blooming countryside garden, soft golden backlight, pastoral romantic mood, medium shot` |
| Coastal grandmother | `coastal grandmother aesthetic, breezy linen shirt in soft neutrals, beach house porch, gentle diffused seaside light, relaxed elegant mood, medium shot` |
| Downtown girl | `downtown girl aesthetic, edgy leather jacket and slim trousers, gritty city street, cool overcast light, effortless NYC cool, medium shot` |
| Mob wife | `mob wife aesthetic, faux fur coat and bold red lip, dramatic glamorous styling, dim luxe interior, confident pose, cinematic low light, medium shot` |
| Pilates princess | `pilates princess aesthetic, pastel matching activewear set, bright airy studio, soft morning light, poised graceful pose, medium shot` |
| Streetwear | `streetwear outfit, oversized hoodie and cargo trousers with sneakers, urban concrete backdrop, crisp daylight, confident candid pose, medium shot` |
| Vamp romance | `vamp romance aesthetic, dark velvet dress and deep berry lip, moody candlelit interior, rich dramatic shadows, sultry editorial style, medium shot` |

> These aesthetics map to real, high-volume social searches. The point of a consistent character is that **the same face** can wear every one of them — that's what turns a model into a believable persona.

## Consistency tips
1. **Use a character-specific model (LoRA)** — the only reliable way to lock identity across scenes. Prompt engineering alone drifts.
2. **Keep the trigger token first** in every prompt.
3. **Vary scene/outfit/lighting, never the identity descriptors.**
4. **Medium shots** keep the face clear; avoid distant full-body for social.

## Further reading
- **[How to Keep a Consistent Character in Midjourney (2026 Guide)](https://www.picovix.app/blog/how-to-keep-consistent-character-midjourney)** — a deep dive on `--cref`, `--sref`, seeds, and prompt anchoring, where each breaks down, and the character-model alternative.
- **[Consistent character generator](https://www.picovix.app/features/consistent-character-generator)** — lock one identity across unlimited scenes without prompt wrestling.
- **[Free AI Character Consistency Prompt Generator](https://www.picovix.app/tools/character-prompt-generator)** — pick your platform (Midjourney / Stable Diffusion / DALL·E), describe your character once, and get a copy-ready prompt plus the exact identity-locking technique (`--cref`, LoRA, seed). Runs in the browser, no signup.

## See it live / try it
These prompts are demonstrated end-to-end (one AI model across many scenes) here:
- **Live showcase:** https://www.picovix.app/showcase
- **Build a consistent AI influencer:** https://www.picovix.app/features/ai-influencer-generator

Built with [Picovix](https://www.picovix.app) — an AI tool focused on consistent AI characters & virtual models.

## License
MIT — use freely. PRs with new scene prompts welcome.
