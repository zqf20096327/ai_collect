# Signs of AI design

A field guide to the visual tells of AI-generated design: websites, app interfaces, images, video, logos, slide decks, social graphics, illustration, and print. Modeled on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), which documented the tells of machine-written prose. This project does the same for machine-made visuals.

None of these signs proves anything on its own. Almost every pattern here was invented by human designers first; AI tools amplified their frequency and uniformity until they became fingerprints. One match is noise. Ten matches is a signature. Read the [how to use this guide](#how-to-use-this-guide) section before accusing anyone of anything.

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Content is licensed [CC BY-SA 4.0](LICENSE): copy it, translate it, build tools on it.

## Use it as a design rules file

This guide reads in two directions. As a detector, it tells you what to look for. As a rules file, it tells your coding agent what to design against, so your own project stops converging on the same defaults. Drop [design-rules.md](design-rules.md) into your project as `CLAUDE.md`, `.cursorrules`, or `AGENTS.md`, or paste it into a system prompt. It is written as "prefer a real decision over the reflex," not a blanket ban, because most of these patterns are legitimate in the right context. The point is to make the choice deliberate instead of default.

## Contents

- [How to use this guide](#how-to-use-this-guide)
- [Part I: Websites and app interfaces](#part-i-websites-and-app-interfaces)
- [Part II: AI-generated images](#part-ii-ai-generated-images)
- [Part III: AI-generated video](#part-iii-ai-generated-video)
- [Part IV: Logos and branding](#part-iv-logos-and-branding)
- [Part V: Slide decks and documents](#part-v-slide-decks-and-documents)
- [Part VI: Marketing, social, and print](#part-vi-marketing-social-and-print)
- [Part VII: Copy embedded in design](#part-vii-copy-embedded-in-design)
- [Signs that no longer work](#signs-that-no-longer-work)
- [Why models converge](#why-models-converge)
- [Related work](#related-work)

## How to use this guide

Each entry lists what to look for, why models produce it, and the false positives: legitimate human work that shows the same sign. Entries carry two labels.

Reliability describes how much a single match tells you. "Strong" means few humans produce it by accident (garbled letterforms, hallucinated extra limbs, placeholder text left in a shipped deck). "Moderate" means it is meaningful mostly in combination. "Weak" means humans do it constantly and the sign only matters at high density.

Status describes whether the sign still applies to current tools. Models patch their tells. Hands were the canonical image tell in 2023 and are mostly fixed in frontier models now. Purple gradients were the canonical UI tell of 2024 and are already migrating toward cream palettes and italic serif heroes. A guide like this decays; that is why it is a repository and not an article.

Three rules of interpretation:

1. Stack signs, never single ones. Every entry here is defensible in isolation. A dark hero with a glow is also the house style of Linear, Raycast, and a hundred human teams that copied them years before generative tools existed. The fingerprint is the co-occurrence of many defaults with no deviation anywhere.
2. Judge the absence of decisions, not the presence of a style. The recurring theme across every category: AI output is the statistical median of its training data. The tell is not that Inter is a bad typeface. The tell is Inter, unchosen, next to twenty other unchosen defaults.
3. Do not use this list to harass people. Identifying AI involvement in a design is not evidence of low effort, deception, or bad work, and misidentifying a human designer's work as AI causes real harm. Human detection accuracy on current AI images is barely above chance. Treat every conclusion as probabilistic.

---

## Part I: Websites and app interfaces

The output of v0, Lovable, Bolt, and LLM-generated frontends (Claude, ChatGPT, Cursor builds). This is the most heavily documented category because the generators share a narrow toolchain: Tailwind CSS, shadcn/ui, Lucide icons, Framer Motion. The defaults of that toolchain, replicated across millions of tutorial pages in training data, became the AI look.

### Color and gradients

#### Purple-to-indigo gradient

The most cited tell in the category. Indigo-to-violet hero washes and gradient buttons, typically built from Tailwind's `indigo-500` (#6366F1), `violet-500` (#8B5CF6), or `purple-500` (#A855F7). One 2026 crawl put blue-purple gradient prevalence at roughly 78 percent of indexed marketing sites, up from about 10 percent in 2020.

Why: Tailwind shipped indigo as its demo accent in 2019. Thousands of tutorials replicated it, saturating training data, so models learned that modern web equals indigo. Generated sites then re-entered training corpora and compounded the bias.

False positives: purple is a legitimate brand color. The tell is the unchosen gradient in the exact default hue, stacked with other defaults.

Reliability: moderate. Status: active but migrating (see cream palette below).

#### Neon-on-dark with glow

Cyan, violet, or pink accents on near-black backgrounds, with colored box shadows behind cards and buttons (`box-shadow: 0 0 20px rgba(139,92,246,0.5)`).

Why: the dark-SaaS look dominates design-inspiration training data; it is the signature output of v0 and Cursor builds.

False positives: large. This is the "Linear style" that Linear, Raycast, and Reflect built by hand from around 2019, and thousands of human teams copied it before AI tools existed. A dark glowing SaaS page alone proves nothing about authorship.

Reliability: weak alone. Status: active.

#### Cream and beige "tasteful" palette

Warm cream page background, often with an amber accent. The second-wave default that appeared after purple gradients became a public joke.

Why: models absorbed the anti-purple backlash and learned that cream signals a tasteful startup. It became the new reflex, which is the general life cycle of these tells.

False positives: editorial, food, and craft brands use warm neutrals deliberately.

Reliability: moderate. Status: active, rising.

#### Emerald fallback

When a prompt bans purple, models cascade to emerald (#10B981) as the next safe accent, sometimes ignoring explicit written guidance against green.

Why: next most probable accent in the learned hierarchy.

False positives: green is standard for success states and for finance and health brands.

Reliability: moderate. Status: active.

#### Gradient text

Gradient fill clipped to headings and to big metric numbers, carrying no meaning.

Why: a common Tailwind demo pattern (`bg-clip-text`) that models pattern-match from dashboard templates.

Reliability: moderate. Status: active.

#### Timid, evenly weighted palettes

Several muted colors at equal visual weight, with no single dominant color and no sharp accent. Bold, committed palettes are statistically rare in output because they are statistically rare in the median of training data.

Reliability: weak. Status: active.

### Typography

#### Inter everywhere

Inter (or a system sans) as the only typeface on the page. The tell is not the font; it is the font unchosen, appearing beside twenty other unchosen defaults.

Why: the most used interface typeface in training data and the configured default of the Tailwind and shadcn stack.

False positives: countless hand-built products use Inter deliberately, including Linear itself.

Reliability: weak alone. Status: active.

#### Geist, Space Grotesk, Instrument Serif

Geist has been called the new Inter: it is v0's default because it is Vercel's typeface, so it saturates v0 output. Space Grotesk is the reach when the model or the user tries to escape Inter, which made it a tell of its own. Instrument Serif is the newest reflex, usually italic, usually enormous, usually in a hero.

Reliability: moderate. Status: active.

#### Oversized italic serif display headline

A huge italic serif hero headline, or a single serif-italic accent word dropped inside a sans headline. The universal "tasteful AI startup" hero of 2025 and 2026, applied to products whose register does not call for it.

Why: models conflate distinctive with appropriate.

False positives: editorial brands legitimately want expressive serifs. The question is whether the serif is doing work or decoration.

Reliability: moderate. Status: active, rising.

#### Single family, single weight, flat hierarchy

One type family for the whole page, sometimes one weight for everything, size steps too close together to create hierarchy, letter spacing crushed on display type, all-caps section labels sprayed everywhere.

Why: font pairing and typographic scale require judgment the generator skips.

Reliability: moderate in combination. Status: active.

#### Monospace as decoration

Body copy or ordinary labels set in a code font for hacker atmosphere, making a marketing page read like a terminal.

False positives: developer-tool docs and terminal-adjacent products.

Reliability: moderate. Status: active.

### The hero section

#### Eyebrow chip above the headline

A tiny uppercase tracked label, or a pill badge ("New", "v2.0 is here", a sparkle prefix), sitting directly above a centered oversized headline. A variant adds a decorative dot prefix and a trailing thin line.

Why: the default AI SaaS hero shape in training data. Models treat the ornament as editorial polish and emit it whether or not there is anything to announce.

Reliability: moderate. Status: active; one of the most recognizable current tells.

#### The full hero formula

Centered stack: badge, a full sentence set at 64 pixels or larger, one-line subhead, two calls to action (gradient primary reading "Get Started", ghost secondary), and a gradient orb or glow floating behind.

Why: the modal SaaS hero in training data. It is also a genuinely effective conversion layout, which is how it became modal.

False positives: the structure works and humans use it on purpose. The tell is the formula with zero deviation plus copy that could describe any product.

Reliability: moderate. Status: active.

#### Gradient orbs and blobs

Abstract purple or violet gradient blobs floating behind the hero, sometimes animated, sometimes following the cursor.

Reliability: moderate. Status: active.

### Layout and structure

#### The three-card feature row

Exactly three equal cards below the hero, each with an icon on top, a short heading, and two lines of text. The single most consistently named tell across every source that documents this category.

Why: Tailwind tutorials taught grid layout with three columns; the median SaaS feature section in training data is a triptych; v0 emits it by default and its output becomes the next model's training data.

False positives: a triptych is a clean, responsive-friendly layout that humans also default to. Suspicion rises when the content visibly does not come in threes but was forced into three anyway.

Reliability: moderate. Status: active.

#### Bento grid

An asymmetric boxed grid, often dark with accent-colored tiles. It spread as the safe alternative once three-card rows were called out, and is now a tell of its own.

Reliability: moderate. Status: active.

#### Icon tile stacked above heading

A small rounded-square icon container above a heading: the universal AI feature-card template, emitted in this exact shape by every major generator. A variant centers one enormous line icon above the text.

Reliability: moderate. Status: active.

#### Numbered section markers (01 / 02 / 03)

Two-digit display numbers as section labels, or a horizontal step row with circled numbers. Editorial scaffolding one tier deeper than the eyebrow chip.

False positives: genuinely sequential processes.

Reliability: moderate. Status: active.

#### Repeated section kickers

The same tiny uppercase label repeated above every section heading ("FEATURES", "PRICING", "FAQ"). The model templates one section and stamps it.

Reliability: moderate. Status: active.

#### The cookie-cutter page order

The full skeleton in fixed order: hero, logo wall, three-card features, testimonial carousel, stats row, pricing table, FAQ, footer with a repeated call to action. One 2026 analysis found about half of indie SaaS pricing pages following an identical nine-element template.

False positives: this is also the standard human landing-page playbook. Zero deviation plus other fingerprints is the signal.

Reliability: weak alone. Status: active.

#### Animated stat counters and implausible numbers

A horizontal stat banner ("500K Users · 50M Downloads · 99.9% Uptime"), numbers counting up on scroll. The layout is common; the tell sharpens when the numbers are invented, such as "Trusted by 5,000+ teams" on a domain registered last month.

Reliability: strong when the numbers are checkable and false. Status: active.

#### Logo soup

A grayscale wall of client or partner logos mid-page, present whether or not those relationships exist. Generators emit the trust bar because the median page has one; some shipped pages carry fully hallucinated logo sets.

Reliability: strong when the logos are fabricated. Status: active.

#### Monotonous spacing

One spacing value everywhere, identical section padding top to bottom, generous whitespace with no rhythm variation: six screens of scroll for two thousand words.

Why: models internalized sparse SaaS minimalism as "professional" and apply it uniformly, with no compression or expansion for emphasis.

Reliability: moderate. Status: active.

### Cards, borders, and surfaces

#### rounded-2xl everything

One large border radius (16 to 24 pixels) applied to every card, input, button, and image, rounding the whole interface into the same soft blob.

Why: shadcn's default radius plus the learned association of soft with modern.

Reliability: moderate. Status: active.

#### The untouched shadcn card

`rounded-2xl shadow-lg p-6`, a one-pixel light border, the default muted primary color, components that look exactly like the documentation examples. The library is excellent; the tell is that nobody changed a single token.

Reliability: moderate. Status: active.

#### The ghost card

A hairline border paired with a wide diffuse shadow on the same card: two edge treatments, no commitment to either.

Reliability: moderate. Status: active.

#### Colored left-border accent strip

A three or four pixel colored border on one side of an ordinary card, pattern-matched from alert components. On real alerts it is semantic; sprayed on ordinary cards it is decoration.

Reliability: strong in decorative use. Status: active.

#### Cards inside cards

Every content block boxed, then boxes nested inside boxes, because containment feels organized and avoids real hierarchy decisions.

Reliability: moderate. Status: active.

#### Reflexive glassmorphism

Frosted-glass blur on cards, modals, and navs where there is no layering problem to solve, plus glow borders as decoration.

False positives: glass legitimately solves overlay-on-imagery problems.

Reliability: moderate. Status: active.

### Icons and imagery

#### The Lucide five

Lucide (shadcn's default icon set) with the same recurring picks across unrelated products: Sparkles for AI, Zap for fast, Shield for secure, Check for benefits, BarChart3 for analytics, ArrowRight on every call to action.

Reliability: moderate. Status: active.

#### Emoji as feature icons

A rocket, gear, sparkle, or check emoji standing in for designed icons in feature cards and headings. Rare in professional hand-built work, which makes it one of the stronger tells in this part.

Reliability: strong. Status: active.

#### The fake terminal hero

A code-window mockup with three macOS traffic-light dots as the hero visual, on products that are not developer tools.

Reliability: moderate. Status: active.

#### Plastic illustrations and generated headshots

Overly smooth 3D blob illustrations, crude hand-coded SVG scenes, and founder or testimonial headshots with perfect pores and nothing behind the eyes (see Part II for the image tells that expose these).

Reliability: strong for generated headshots. Status: active.

### Motion

#### The same fade-in on everything

An identical fade-up entrance (`opacity: 0, y: 20`) on every section, scroll-triggered, with a uniform stagger.

Why: Framer Motion dominates React animation training data and ships in generator output; one pattern covers all entrances.

False positives: real teams use this exact polish move constantly. Weak alone.

Reliability: weak. Status: active.

#### Bounce and elastic easing

Dialogs that spring in, cards that overshoot. Impressive-looking curves overrepresented in tutorial data; reads dated.

Reliability: moderate. Status: active.

#### Motion incoherence

Scattered, uncoordinated micro-interactions: buttons that snap with no transition next to cards that animate elaborately, hover states that do nothing, a spinner as the only loading state, layout properties animated with visible jank.

Why: tutorials teach effects in isolation, and the model never sees its output run.

Reliability: moderate. Status: active.

### Trust sections, pricing, and footers

#### Testimonial walls with fake people

A grid of one-sentence broad praise ("Game-changing tool!") from first-name-only or generated-sounding people ("Sarah Chen", "Marcus Williams") with stock or AI-generated avatars, no use-case specifics anywhere.

Reliability: strong when the people are not findable. Status: active.

#### Fabricated trust chrome

Compliance badges for audits that never happened, invented user counts, roadmap sections implying momentum that does not exist. Trust signals are part of the learned template, generated whether or not the facts are.

Reliability: strong when checkable. Status: active.

#### Three-tier pricing with a highlighted middle

Three tiers, "Most Popular" badge on the middle one, monthly-annual toggle, checkmark lists, enterprise tier reading "Contact us."

False positives: this is standard human practice; template-identical execution is the tell.

Reliability: weak alone. Status: active.

#### Footer fingerprints

Four to five link columns (Product, Company, Resources, Legal), a generic "We are a team of passionate developers building the future of X" blurb, a default favicon, and, near-conclusively, a generator attribution left in: "Built with v0", "Built on Lovable".

Reliability: strong for attribution links and default favicons. Status: active.

### Code-level fingerprints

For readers who can view source. Verbatim Tailwind stacks like `bg-gradient-to-br from-blue-600 to-purple-500` and `rounded-2xl shadow-lg p-6`; spacing exclusively in `gap-4` / `p-6` / `my-8` multiples; `dark:` prefixes sprayed on every element. Tool signatures: shadcn `@/components/ui/*` imports and Geist point to v0; a Vite scaffold with visible Supabase boilerplate points to Bolt; a `lovable.dev` meta tag or "Built on Lovable" badge is conclusive; Material Symbols instead of Lucide points to Gemini-generated output. Quality gaps travel with these: missing alt text, skipped heading levels, div soup, no form validation, no keyboard support, because models train on static code and never experience the page.

Reliability: strong for tool signatures. Status: active.

---

## Part II: AI-generated images

Photorealistic and stylized output from Midjourney, DALL-E, Flux, Stable Diffusion, GPT-image, Imagen, and Grok. The category where tells decay fastest: several canonical 2023 signs are fixed, and detection increasingly rests on scene logic and physics rather than rendering errors. Human accuracy at identifying current AI images in studies is barely above chance, so stack signs aggressively here.

### Color and tone

#### The yellow cast

A persistent warm sepia wash over GPT-image outputs: whites drift to cream, shadows go muddy brown, skin looks jaundiced. Named and memed from spring 2025 ("piss filter"); later OpenAI models reduced but did not eliminate it. A uniform amber tint on an otherwise clean image remains one of the fastest tells for the OpenAI family specifically.

False positives: golden hour, tungsten light, warm filters, faded film scans.

Reliability: moderate. Status: active, weakening.

#### Teal-and-orange grading

Complementary teal shadows against orange skin and highlights, blockbuster-poster style, in scenes that give no reason for it. Strongest in Midjourney.

False positives: actual film stills and any photo run through popular grading presets.

Reliability: weak alone. Status: active.

#### Everything saturated at once

Vivid sky, vivid foliage, glowing skin, no dull or dead zones anywhere. Real photographs almost always contain boring regions; aesthetic-preference tuning removes them.

False positives: phone HDR pipelines and influencer editing.

Reliability: weak alone. Status: active.

#### Missing sensor noise

Shadows and skies perfectly clean at pixel level, or grain painted on evenly rather than varying with exposure.

False positives: heavily denoised or AI-upscaled real photos. Social recompression also destroys the evidence either way.

Reliability: moderate, requires zoom. Status: active.

### Faces and skin

#### Waxy skin

Poreless, airbrushed, slightly glossy skin with no fine hair, blemishes, or micro-shadows. Check cheeks and forehead at zoom.

False positives: the highest false-positive tell in this part. Retouching, beauty filters, and soft studio light produce the same look on real photos.

Reliability: weak alone. Status: active but weakening; current models can render pores when asked.

#### The same face everywhere

Symmetric, conventionally attractive, mid-twenties faces recurring across unrelated images, each model family with its own attractor face. Flux models repeat cheek dimples and a dipped chin so consistently that users file bug reports.

Why: preference tuning collapses output diversity onto one commercially perfect face.

Reliability: strong across a set of images, weak on one. Status: active, growing.

#### Eye and catchlight mismatch

Reflections in the two eyes differing in shape or position, pupils of unequal size or shape, eye reflections that disagree with the visible environment.

Reliability: moderate, requires zoom. Status: active.

#### Ears, earrings, glasses, jewelry

Melted ear cartilage, mismatched earrings, glasses frames that differ left versus right, temples that vanish behind the head, necklaces dissolving into skin, watch faces with garbled numerals. Thin symmetric man-made objects are what patch-based generation handles worst.

Reliability: strong. Status: active.

#### Hair merging into background

Strands that loop into themselves, hair fusing with background or clothing, a faint halo at the hair-background boundary.

False positives: bad cutouts and phone portrait-mode masking errors.

Reliability: moderate. Status: active.

### Anatomy and people

#### Hands under load

The famous tell, relocated. Resting hands are mostly fixed in frontier models; failures now concentrate where hands interact: gripping a microphone, interlaced fingers, two people holding hands, chopsticks. Background figures fail more than subjects. A correct hand no longer proves a real photo.

Reliability: strong when present. Status: partially fixed; check interactions, not poses.

#### Cloned crowds

Background crowds where faces repeat, everyone shares one age and build, faces smear past the second row, or every head faces the same direction with identical posture. Compute goes to the subject; crowds are texture.

Reliability: strong. Status: active; one of the best current tells for event and news imagery.

#### Context-inappropriate grooming

Perfect hair, clean clothes, and full makeup on disaster victims, refugees, soldiers, manual laborers. The beauty prior ignores scene semantics.

Reliability: moderate. Status: active; useful specifically against fake news imagery.

### Text in images

#### Garbled secondary text

The big split of the current generation. Foreground headline text is now largely fixed: several models render short strings cleanly. But background signage, license plates, book spines, small print, and non-Latin scripts still degrade into plausible-looking gibberish, letters blending or changing font mid-word. Check the third sign in the scene, not the first.

Reliability: strong. Status: active for secondary text; fixed for headlines.

### Composition and style

#### Dead-center framing

Subject centered, facing camera, balanced negative space, across an entire feed. Real candid photography produces awkward crops and clutter; models rarely do.

Reliability: weak alone, moderate across a set. Status: active.

#### Over-symmetry

Faces, buildings, and ornament more bilaterally symmetric than reality, patterns repeating too perfectly.

Reliability: moderate. Status: active in architecture and decoration, weakening in faces.

#### The epic-cinematic default

Dramatic rim light, volumetric rays, haze, golden-hour or moody-blue palette, painterly gloss: mundane subjects rendered like stills from a prestige fantasy film. The Midjourney house look, produced by tuning on community upvotes.

False positives: actual cinema and heavily graded concept photography.

Reliability: moderate. Status: active, though newer models offer neutral modes.

#### Uniform fake bokeh

Background blur equally strong at every distance, no focus falloff, sharpness combinations no lens produces, bokeh discs without optical character.

False positives: phone portrait mode fakes blur the same way on real photos.

Reliability: moderate. Status: active.

### Scene logic and physics

The most durable tells in the category, because fixing them requires scene-level world models rather than better rendering.

#### Shadows that disagree

One sun, shadows pointing different directions, objects missing shadows, lengths inconsistent with each other.

Reliability: strong. Status: active.

#### Wrong reflections

Mirrors, water, windows, and sunglasses reflecting content that disagrees with the scene: wrong geometry, missing subjects, generic smears. Mirrors remain the classic trap even for 2026 frontier models.

Reliability: strong. Status: active.

#### Background geometry breakdown

Windows misaligned with the building grid, rooflines implying different vanishing points, railings gaining extra segments, stairs to nowhere, road markings curving into nothing. Experienced checkers now look here first, since faces got fixed first.

Reliability: strong. Status: active.

#### Nonsensical object logic

Door handles on the hinge side, chairs with three legs, cables connecting to nothing, utensils fused to plates, bare trees in a summer scene. Semantic errors outlast rendering errors.

Reliability: strong. Status: active.

#### Texture without fractal detail

Fabric woven too evenly, stone with regular joints, fur without strand variation, surfaces that tile rather than vary. Real materials are irregular at every scale.

Reliability: moderate, requires zoom. Status: active.

### Provenance

#### Watermark ghosts

Faint smeared remnants of stock-photo watermarks hallucinated into images. Mostly gone from frontier models, still surfacing in open-weight checkpoints. When present, near-conclusive.

Reliability: strong. Status: fading.

#### Metadata and content credentials

Generated images carry no real camera EXIF; conversely, C2PA Content Credentials and Google SynthID marks positively identify AI origin where present. Both weaken under recompression and screenshots, and messaging apps strip EXIF from real photos too, so absent metadata proves little; present provenance marks prove a lot.

Reliability: strong when marks are present. Status: active and growing.

### Model signatures

Quick family fingerprints, useful in combination: yellow cast plus soft painterly finish plus clean headline text points to OpenAI. Teal-orange plus epic-cinematic grade points to Midjourney. A recurring dimple-and-dipped-chin face points to Flux. High photorealism with edge halos and dissolving jewelry points to Grok. Clean hands, clean text, and almost no visible tells points to Imagen, where detection falls back to SynthID.

---

## Part III: AI-generated video

Sora, Veo, Runway, Kling, and successors. Physics remains the most reliable tell because it is the hardest thing to fake.

#### Object impermanence

Objects appear, vanish, or transform between frames; a held item changes shape or swaps hands; background props drift. No persistent object state exists across frames.

Reliability: strong. Status: active, concentrated at clip boundaries and long shots.

#### Breathing textures

Static regions (walls, sky, fabric weave) shimmer subtly frame to frame because each frame is re-synthesized rather than tracked.

Reliability: strong. Status: active.

#### Boiling backgrounds

Foliage, crowds, and architectural detail churn while the main subject stays clean, because compute concentrates on the subject.

Reliability: strong. Status: active.

#### Dream physics

Water, smoke, fabric, and collisions behaving almost right: too-smooth motion, weightless objects, hair moving with no wind. Current models have narrowed this to subtle rather than blatant, but it persists.

Reliability: strong. Status: active, subtler each generation.

#### Gait errors

Gliding or puppet-like walks, feet that slide or never plant, legs swapping mid-stride, especially in side views and crowds.

Reliability: strong. Status: active, improving.

#### Missing microexpressions

Blinking is convincing now, but the sub-100-millisecond asymmetric muscle movements around eyes and mouth during speech are absent or too symmetric. Visible with attention or slow motion.

Reliability: moderate. Status: active.

#### Audio tells

No room tone, no breaths or hesitations, robotic cadence, slight lip-sync drift.

Reliability: moderate. Status: active.

#### Watermark handling

Sora outputs carry a moving watermark; cropped or blurred removal leaves odd aspect ratios and smeared patches. Watermarks can also be faked onto real footage, so treat as one signal, not proof.

Reliability: moderate. Status: active.

---

## Part IV: Logos and branding

#### The gradient orb

A circular or hexagonal mark with a central void, soft organic curves, and a blue-purple-teal gradient. So uniform across AI companies that a viral essay catalogued dozens of near-identical marks.

Why: copycat legitimacy-seeking plus generators trained on the same corpus, re-emitting the statistically average tech mark.

False positives: important one. Human agencies designed most of the famous orbs, including OpenAI's own mark. The orb signals the AI-company branding trend more reliably than machine authorship.

Reliability: weak for authorship. Status: active.

#### Recycled industry motifs

Category-default symbols with no connection to the actual business: flames and dumbbells for fitness, hexagons for tech, shields for finance, lotuses for wellness. The mark feels like a mashup of five competitors' logos.

Reliability: weak alone. Status: active.

#### Geometric animal heads

Low-poly lion, wolf, fox, or eagle heads built from triangular facets in a single gradient: a staple of every AI logo generator's suggestion set.

False positives: this was a human Dribbble fad around 2014 to 2018, so older human logos in the style exist in bulk.

Reliability: weak. Status: active.

#### Mockup-only delivery

The logo exists only as a glossy raster render on a fake storefront or embossed business card. No flat version, no one-color version, no icon-only lockup, no vector file. Image models generate a picture of a logo presentation, not a logo system. Asking for the SVG resolves the question immediately.

Reliability: strong. Status: active.

#### Geometric drift and type wobble

Repeated shapes that are not actually identical, corner radii that vary, curves wobbling where they meet straights, stray anchor points; in wordmarks, uneven spacing, mismatched stroke weights, characters that look imported from different typefaces. Diffusion approximates geometry pixel-wise instead of constructing it.

Reliability: strong; the most technically reliable logo tell. Status: active.

#### Fails the favicon test

Tiny highlights, inner shadows, and 3D bevels that collapse when the mark scales to 24 pixels or prints in one color. Generators optimize one attractive render, not reproduction across media.

Reliability: strong. Status: active.

---

## Part V: Slide decks and documents

Output of Gamma, Tome, Beautiful.ai, Canva Magic Design, and LLM-drafted decks.

#### The icon-heavy three-column card grid

Every content slide resolves to three or four equal cards, each with a flat line icon on top, a short Title Case heading, and two lines of text. All the major deck generators default to this.

Why: template engines map any list onto the safest grid, and the LLM conveniently produces points in threes, which feeds the grid.

False positives: three-column layouts are normal consulting-deck grammar. The tell is uniformity across the whole deck plus icons that do not match their content.

Reliability: moderate. Status: active.

#### Icon soup

Flat line icons from a shared library at identical stroke weight, matched to text by keyword rather than meaning: a lightbulb for anything resembling an idea, a handshake for anything resembling a partnership, and periodically something absurd, like headphones drawn inside a silhouette's head.

Reliability: strong when the mismatch is visible. Status: active.

#### Uniform slide grammar

Every title in Title Case, about six words, often "Something: Something Else." Every slide with three or four bullets of near-identical length, each opening with a verb. Identical margins on every slide; no slide breaks the grid for emphasis; the whole deck lacks a visual arc.

Reliability: moderate. Status: active.

#### Decorative charts with fabricated data

Charts and stat callouts with suspiciously round, unsourced numbers; real entity names paired with invented statistics; or, near-conclusively, unresolved placeholders like "Platform X" and "20XX". A 2026 test of six AI presentation makers found claim-verification rates between 44 percent and zero.

Reliability: strong. Status: active.

#### Emoji bullets

Rocket, lightbulb, check, and target emoji as bullet markers or heading prefixes in a business deck, applied uniformly to every section.

False positives: startup and Notion culture used emoji headers before AI.

Reliability: moderate. Status: active.

#### The generic scaffold

Intro, Problem, Solution, Benefits, Conclusion, regardless of content, opened with "In today's fast-paced world." Footers that appear on some slides and vanish on others.

Reliability: moderate; the opener phrase alone is strong. Status: active.

---

## Part VI: Marketing, social, and print

#### The interchangeable flyer

Bold gradient background, oversized headline, stock-like people, a predictable arrangement of icons: polished enough to look finished, generic enough to be forgettable. Community-event posters have their own strain: cramped compositions, bunting, smiling children and cute animals, text on wooden planks, a yellow-beige undertone, and identical output across unrelated towns.

Reliability: moderate; convergence across sources is the real signal. Status: active.

#### Hallucinated micro-errors

The extra paw on the puppy, six fingers around a pint glass, a garbled venue name, ornament that dissolves on zoom. Detection here is forensic: check the second-order details, not the composition.

Reliability: strong; near-conclusive. Status: active.

#### The carousel template

Eight to ten square slides, one aphorism per slide in huge type, a swipe cue, progress dots, a hook slide ("Steal my framework"), a follow-me slide. Carousel generators template the layout while the LLM writes the copy, so both layers converge.

False positives: the format was human growth-hacking grammar first; the copy tells (Part VII) separate the layers.

Reliability: weak visually, moderate with copy tells. Status: active.

#### The thumbnail kit

Shocked open-mouth face with slightly waxy generic features, red circle or arrow, bold yellow text, hyper-saturated background: prompt monoculture rendering the same thumbnail across unrelated channels.

False positives: the formula itself is human-era clickbait grammar; the waxy face and cross-channel sameness are the AI layer.

Reliability: weak alone. Status: active.

#### Corporate Memphis, machine edition

Flat vector people with elongated limbs, tiny heads, and blue or purple skin. The style is human (it dates to late-2010s tech branding) but it is the densest illustration style in training data, so generators emit it as the default answer to "illustration for a tech blog." Attribute to AI only via limb-count errors, inconsistent stroke logic, and off-model repeats.

Reliability: weak for style alone, strong with errors. Status: active.

#### The soft-anime wash

Watercolor-ish anime rendering applied to everything after the Ghibli-style trend of 2025: mascots, wedding invites, ads. Check hands, background text, and the yellow cast to attribute.

Reliability: weak alone. Status: active.

#### Die-cut sticker packs

Glossy chibi characters with a thick white die-cut outline, delivered as packs of six to twelve with identical lighting, subtle asymmetry drift between pack items, and melted small accessories.

Reliability: moderate. Status: active.

#### Print and merch tells

Book covers with dramatic imagery but distorted title lettering and filigree that dissolves on zoom. Blur and banding in print from upscaled low-resolution generations. Embossing, foil, and stitching that are painted light-and-shadow illusions rather than physical processes; texture that ignores fabric folds on shirt mockups. On marketplaces: products with no customer photos, "for illustration purposes only" disclaimers, and reviews saying it looks different in person.

Reliability: strong for garbled type plus dissolving ornament together. Status: active.

---

## Part VII: Copy embedded in design

Design carries words, and the words leak authorship. Full prose coverage belongs to Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing); these are the patterns as they surface inside designed artifacts.

#### The weightless headline

"Build faster. Ship smarter." Grammatically perfect, could describe any product. Related forms: "Transform your X with Y", the all-in-one-platform subhead, strict three-beat lines ("Build, ship, scale") never broken for rhythm.

Reliability: weak alone; human marketing is often equally vague. Status: active.

#### The buzzword layer

Marketing diction at density: "streamline", "supercharge", "empower", "world-class", "enterprise-grade", "best-in-class", "battle-tested", "unlock", "unleash", openers like "In today's fast-paced world", and the familiar adjective padding ("robust", "seamless", "comprehensive"). Every one of these was coined by human marketers; density and combination are the fingerprint.

Reliability: moderate at density. Status: active.

#### Punctuation and cadence density

Em dash frequency several times the human baseline; a manufactured-contrast aphorism closing every section; the negation pivot ("It's not just X. It's Y.") as a hero line; FAQ questions that paraphrase content already on the page.

False positives: high for any single instance. Strong human writers use every one of these devices. Rate is the signal, never the occurrence.

Reliability: weak per instance, moderate at density. Status: active.

#### Title Case Everything

Every heading, button, label, and chart title in Title Case with total uniformity, including places humans drift into sentence case.

Reliability: weak alone. Status: active.

#### The sparkle glyph

The four-point sparkle as a universal AI badge on features, decks, and marketing. Usability research found users do not naturally read it as meaning AI at all; its ubiquity is herd adoption, the same dynamic as the gradient orb.

Reliability: signals an AI feature label, not necessarily AI authorship. Status: active.

---

## Signs that no longer work

Tells decay. Citing these as evidence in 2026 mostly signals an outdated checklist. Kept here because their life cycle is the best argument for maintaining this list as a living document.

Six fingers on resting hands: fixed in frontier image models; only complex grips and background figures still fail. Garbled headline text: fixed for short foreground strings in several models; secondary text still breaks. Grossly asymmetric eyes and painted-on teeth: fixed in frontier portrait output; wide laughs and background faces still fail. The obvious uncanny-valley face: human detection accuracy has fallen to roughly 62 percent in large studies, barely above chance. And on the UI side, the purple gradient is already migrating: the models that learned everyone hates it now reach for cream, emerald, and italic serifs instead, which is how those became entries above.

## Why models converge

Four mechanisms produce everything in this list.

Statistical averaging. A generative model fills every unspecified decision with the median of its training data. An ambiguous prompt returns the average of every Tailwind tutorial, stock photo, and pitch deck the model ever saw. Specific constraints narrow the distribution; absence of constraints is what you can see in the output.

Toolchain defaults. On the web side, a handful of libraries (Tailwind, shadcn, Lucide, Framer Motion) supply the defaults that generators emit verbatim. The defaults are fine; unmodified defaults at scale become a signature.

Preference tuning. Image models are tuned on human aesthetic ratings, which reward centered, saturated, symmetric, epic, and flattering. The tuning removes the boring regions, awkward crops, and imperfections that real photographs and real design contain.

The feedback loop. Generated output ships, gets indexed, and becomes training data for the next generation, concentrating every bias above. Convergence across unrelated sources is therefore the meta-tell in every category: identical pub posters in different towns, identical startup logos, identical hero sections. Individual artifacts prove less than side-by-side sameness.

## Related work

This guide stands on prior documentation efforts, which are worth reading in full: Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing); [impeccable.style/slop](https://impeccable.style/slop/), a 46-pattern generated-UI catalog with a CLI detector; the [925 Studios tell list](https://www.925studios.co/blog/ai-slop-design-tells); [solodesign.cc on design slop](https://solodesign.cc/blog/ai-design-slop-the-tells/) and its 50-rule detector; [Why Your AI Keeps Building the Same Purple Gradient Website](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website); the [Sailop state of the AI-generated web report](https://www.sailop.com/blog/ai-slop-2026-state-of-the-ai-generated-web); [shitfa.st](https://shitfa.st/), an archive of AI-written landing pages; the [GIJN reporter's guide to detecting AI content](https://gijn.org/resource/guide-detecting-ai-generated-content/); NN/g's [sparkle icon research](https://www.nngroup.com/articles/ai-sparkles-icon-problem/); and the [Patterns journal paper on generative convergence](https://www.cell.com/patterns/fulltext/S2666-3899(25)00299-5). Detailed per-claim sources live in [SOURCES.md](SOURCES.md).

## Maintainer

Compiled and maintained by [Febian](https://www.febian.com), an enterprise AI architect. This is a living document, not a personal essay: corrections, new tells, and status updates from anyone are welcome through [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Text content: [CC BY-SA 4.0](LICENSE). Attribute this repository and share adaptations under the same terms.
