<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png">
  <img src="assets/banner-light.png" alt="ComfyUI-Nemotron-Image: NVIDIA's Nemotron-Labs-Image-30B-A3B, native in ComfyUI." width="100%">
</picture>

**ComfyUI-Nemotron-Image** runs NVIDIA's
[Nemotron-Labs-Image-30B-A3B](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B) natively in ComfyUI.

- **Autoregressive, not diffusion.** A 30B mixture-of-experts language model (3B active per token) writes the image
  as 16×16-pixel codes, row by row.
- **One node replaces the sampler.** **Nemotron Image Generate** does what KSampler does in a diffusion workflow: it
  takes the prompt and returns a `LATENT`.
- **The pixel decoder is a stock `VAE`.** The model's image tokenizer loads as a normal VAE, so the core
  **VAE Decode** node turns the codes into pixels.

Research and evaluation use only: see [License](#license).

https://github.com/user-attachments/assets/9f24b3d8-b856-41d5-9806-f0025c6cb181

An 84-second explainer of how the model writes a picture, with sound. [Full quality (1080p, 60 fps)](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/resolve/main/assets/nemotron_image_promo.mp4).

<p>
<a href="assets/showcase/CORE-3_2.jpg"><img src="assets/showcase/CORE-3_2.jpg" alt="A glass perfume bottle with a brass cap on wet black slate beside a slice of blood orange, rim-lit on black." width="35.2%"></a> <a href="assets/showcase/CIN-01_2.jpg"><img src="assets/showcase/CIN-01_2.jpg" alt="A lone astronaut standing in a golden wheat field under a pale sky." width="62.4%"></a><br>
<a href="assets/showcase/FSH-04_4.jpg"><img src="assets/showcase/FSH-04_4.jpg" alt="A magazine cover with the masthead NORRSKEN and a male model in a pale blue suit against a mint wall." width="23.7%"></a> <a href="assets/showcase/PRD-11_4.jpg"><img src="assets/showcase/PRD-11_4.jpg" alt="A lemonade ad: a bottle labelled Sólida among lemon slices on bright yellow, the word LEMONADE below." width="23.7%"></a> <a href="assets/showcase/PNT-06_4.jpg"><img src="assets/showcase/PNT-06_4.jpg" alt="A Byzantine-style icon of a red fox with a golden halo on a gold-leaf ground." width="23.7%"></a> <a href="assets/showcase/MAC-09_4.jpg"><img src="assets/showcase/MAC-09_4.jpg" alt="An exploded view of a wristwatch, gears and springs floating between the dial and the case." width="23.7%"></a><br>
<a href="assets/showcase/X-OBJ-11_4.jpg"><img src="assets/showcase/X-OBJ-11_4.jpg" alt="A black typewriter seen from above on dark wood, the sheet in it reading Hello world." width="32.1%"></a> <a href="assets/showcase/DRW-12_2.jpg"><img src="assets/showcase/DRW-12_2.jpg" alt="A human skull drawn in fine black stippling on cream paper." width="32.1%"></a> <a href="assets/showcase/WLD-03_2.jpg"><img src="assets/showcase/WLD-03_2.jpg" alt="Macro of a fuzzy jumping spider with big black eyes on a green leaf with dew drops." width="32.1%"></a><br>
<a href="assets/showcase/LND-05_3.jpg"><img src="assets/showcase/LND-05_3.jpg" alt="Green northern lights over a frozen lake, a red wooden cabin with a lit window among snowy spruces." width="48.8%"></a> <a href="assets/showcase/PRD-14_1.jpg"><img src="assets/showcase/PRD-14_1.jpg" alt="An outdoor kit laid out on grey granite: green jacket, hiking boots, steel bottle, beanie, compass, map and enamel mug." width="48.8%"></a><br>
<a href="assets/showcase/FSH-07_3.jpg"><img src="assets/showcase/FSH-07_3.jpg" alt="A model in a bright yellow swimsuit on a rocky Mediterranean beach in hard sun." width="24.3%"></a> <a href="assets/showcase/X-SCL-01_4.jpg"><img src="assets/showcase/X-SCL-01_4.jpg" alt="A tiny person at the foot of a giant redwood, looking up." width="17.2%"></a> <a href="assets/showcase/X-SPA-01_1.jpg"><img src="assets/showcase/X-SPA-01_1.jpg" alt="A red cube on a blue sphere on a green cylinder against grey." width="22.7%"></a> <a href="assets/showcase/MAC-03_1.jpg"><img src="assets/showcase/MAC-03_1.jpg" alt="Extreme macro of a fly's compound eye, every facet visible." width="30.5%"></a><br>
<a href="assets/showcase/PNT-14_3.jpg"><img src="assets/showcase/PNT-14_3.jpg" alt="A Dutch Golden Age still life: a fallen silver goblet, a peeled lemon, an oyster and grapes with a fly." width="35.1%"></a> <a href="assets/showcase/X-PHY-04_3.jpg"><img src="assets/showcase/X-PHY-04_3.jpg" alt="A chrome sphere on a checkerboard floor reflecting the photographer." width="26.1%"></a> <a href="assets/showcase/SUR-05_1.jpg"><img src="assets/showcase/SUR-05_1.jpg" alt="A man reading a newspaper on a sofa in a living room filled with clouds." width="35.1%"></a><br>
<a href="assets/showcase/X-BND-02_4.jpg"><img src="assets/showcase/X-BND-02_4.jpg" alt="A man in a red hat and blue scarf next to a woman in a blue hat and red scarf." width="46.1%"></a> <a href="assets/showcase/X-POS-25_1.jpg"><img src="assets/showcase/X-POS-25_1.jpg" alt="Five people in warrior II pose in a yoga studio, all facing the same way." width="51.5%"></a>
</p>

All twenty come from the int8 file at seed 42, four images per prompt, on an RTX 3090 or 4090. Nothing was retouched;
the beach photo has an 80-pixel strip cropped from the bottom, where the model wrote a caption. Click an image for
the full size.

<details>
<summary>Prompts and sizes</summary>

- [Perfume bottle on wet slate](assets/showcase/CORE-3_2.jpg), 1024×1024, image 2 of 4: Product photo of a clear glass perfume bottle with a brushed brass cap, standing on wet black slate, water droplets on the glass, a slice of blood orange beside it, dark background, hard rim light from behind, sharp reflections and caustics on the slate
- [Astronaut in a wheat field](assets/showcase/CIN-01_2.jpg), 1360×768, image 2 of 4: A film still of a lone astronaut in a wheat field.
- [Magazine cover](assets/showcase/FSH-04_4.jpg), 880×1184, image 4 of 4: Magazine cover with a male model in a pastel suit against a mint wall, the masthead "NORRSKEN" at the top and cover lines on the left.
- [Lemonade ad](assets/showcase/PRD-11_4.jpg), 880×1184, image 4 of 4: An ad for a fictional lemonade brand called "Sólida". A sweating glass bottle bursts through a wall of lemon slices, with ice and water splashing around it. Bright yellow background, hard sunlight shadows, the logo clearly printed on the bottle.
- [Fox icon](assets/showcase/PNT-06_4.jpg), 880×1184, image 4 of 4: A Byzantine-style icon of a fox saint with a golden halo, egg tempera on wood, gold-leaf background, cracked varnish.
- [Exploded wristwatch](assets/showcase/MAC-09_4.jpg), 880×1184, image 4 of 4: An exploded view of a mechanical wristwatch, every gear and spring floating in order above the case, studio lighting.
- [Typewriter](assets/showcase/X-OBJ-11_4.jpg), 1024×1024, image 4 of 4: A vintage typewriter, top-down, a sheet of paper in it reading "Hello world".
- [Stippled skull](assets/showcase/DRW-12_2.jpg), 1024×1024, image 2 of 4: A stippled illustration of a human skull made entirely of tiny black dots.
- [Jumping spider](assets/showcase/WLD-03_2.jpg), 1024×1024, image 2 of 4: macro, jumping spider, fuzzy, big eyes, green leaf, dew drops, studio flash
- [Northern lights over a cabin](assets/showcase/LND-05_3.jpg), 1248×832, image 3 of 4: Northern lights over a frozen lake in Swedish Lapland, a small red wooden cabin with a lit window on the shore, snow-covered spruce trees, stars visible, long-exposure photograph.
- [Outdoor product range](assets/showcase/PRD-14_1.jpg), 1248×832, image 1 of 4: A product range photo for a fictional outdoor brand called "Fjällgård". Seven items are laid out on a large slab of pale grey granite outdoors: a dark green waterproof jacket folded neatly, a pair of brown leather hiking boots with red laces, a steel water bottle with the logo engraved on it, a wool beanie, a compass, a folded paper map and a small enamel mug. Each item has its own space with even gaps between them, all facing the same way, as in a catalogue. Lichen and a few pine needles on the rock add texture. Soft overcast light with gentle shadows toward the lower right. Shot from directly above, everything in focus, true colours, the logo readable on the bottle.
- [Beach editorial](assets/showcase/FSH-07_3.jpg), 880×1184, image 3 of 4: Plus-size model in a bright yellow swimsuit on a rocky Mediterranean beach, hard midday sun, confident pose, editorial colour.
- [Person at a redwood](assets/showcase/X-SCL-01_4.jpg), 768×1360, image 4 of 4: A tiny person at the foot of a giant redwood, looking up.
- [Cube, sphere, cylinder](assets/showcase/X-SPA-01_1.jpg), 880×1184, image 1 of 4: A red cube on top of a blue sphere, which sits on top of a green cylinder.
- [Fly's eye](assets/showcase/MAC-03_1.jpg), 1024×1024, image 1 of 4: Extreme macro of a housefly's compound eye, every facet visible, focus-stacked, iridescent colours.
- [Golden Age still life](assets/showcase/PNT-14_3.jpg), 1184×880, image 3 of 4: Dutch Golden Age still life. A silver goblet knocked over on a white tablecloth, a half-peeled lemon with its rind spiralling over the edge of the table, oysters, and a fly on a bunch of grapes. Dark background, oil glazes, every reflection painted precisely.
- [Chrome sphere](assets/showcase/X-PHY-04_3.jpg), 1024×1024, image 3 of 4: A chrome sphere on a checkerboard floor reflecting the room and the photographer.
- [Living room of clouds](assets/showcase/SUR-05_1.jpg), 1184×880, image 1 of 4: A living room flooded with clouds up to the sofa cushions, a man calmly reading a newspaper, photograph.
- [Red hat, blue hat](assets/showcase/X-BND-02_4.jpg), 1184×880, image 4 of 4: A man in a red hat and a blue scarf next to a woman in a blue hat and a red scarf.
- [Yoga class](assets/showcase/X-POS-25_1.jpg), 1248×832, image 1 of 4: A yoga class of five people in warrior II pose, all facing the same way.

</details>

## Quick start

**1. Install the nodes.** Clone the pack into ComfyUI's `custom_nodes` and restart ComfyUI:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PedroMarinhoDev/ComfyUI-Nemotron-Image
```

Or, in ComfyUI Manager, use **Install via Git URL** with `https://github.com/PedroMarinhoDev/ComfyUI-Nemotron-Image`. Or from the [Comfy Registry](https://registry.comfy.org/nodes/nemotron-image-native): `comfy node install nemotron-image-native`. There is nothing to `pip install`.

**2. Download the weights** from [PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI):
one model file into `models/diffusion_models/nemotron-image/` and the pixel decoder into `models/vae/nemotron-image/`.
From the `ComfyUI` folder:

```bash
hf download PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI nemotron_labs_image_30b_a3b_w4a8.safetensors --local-dir models/diffusion_models/nemotron-image
hf download PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI nemotron_labs_image_tokenizer_bf16.safetensors --local-dir models/vae/nemotron-image
```

For another precision, use its file in the first line: `nemotron_labs_image_30b_a3b_w4a8_int8dense.safetensors`,
`nemotron_labs_image_30b_a3b_w6a8.safetensors`, `nemotron_labs_image_30b_a3b_int8_convrot.safetensors` or
`nemotron_labs_image_30b_a3b_bf16.safetensors`.

**3. Open the workflow.** Drag [`example_workflows/nemotron_image_t2i.json`](example_workflows/nemotron_image_t2i.json)
into ComfyUI, write the prompt in **Nemotron Image Generate** and run.

## Which file

All five model files hold the whole model. They differ in how the weights are stored, mostly the routed experts,
which are 90% of the model. **Error** is the KL divergence from the bf16 file, explained under [Quality](#quality).
How each file was made is on the [model card](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI).

| File | Size | Where the experts go | Error vs bf16 | Pick it for |
|---|---|---|---|---|
| [W4A8](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/blob/main/nemotron_labs_image_30b_a3b_w4a8.safetensors) | 22.7 GB | on a 24 GB card: 18.8 GiB of VRAM, +1.25 GiB for the live preview; 2.8 GiB of RAM | 0.033 | any card from 12 GB |
| [W4A8 int8 dense](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/blob/main/nemotron_labs_image_30b_a3b_w4a8_int8dense.safetensors) | 21.6 GB | as W4A8, with the Mamba and attention weights also in int8: 1 GiB less VRAM | 0.034 | the same cards as W4A8, the fastest file: 13–16% faster at one image, error 4% higher |
| [W6A8](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/blob/main/nemotron_labs_image_30b_a3b_w6a8.safetensors) | 30.0 GB | system RAM (27 GiB), with a cache on the card | 0.017 | a 24 GB card, closer to bf16, about a quarter more time than W4A8 |
| [int8](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/blob/main/nemotron_labs_image_30b_a3b_int8_convrot.safetensors) | 35.5 GB | system RAM (30.5 GiB), with a cache on the card | 0.015 | the closest to bf16, 31–40% more time than W4A8 |
| [bf16](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/blob/main/nemotron_labs_image_30b_a3b_bf16.safetensors) | 65.3 GB | system RAM (57.5 GiB; needs about 80 GB of RAM), with a cache on the card | — | the reference, about 3.9 min an image |
| [pixel decoder](https://huggingface.co/PedroMarinhoDev/Nemotron-Labs-Image-ComfyUI/blob/main/nemotron_labs_image_tokenizer_bf16.safetensors) | 1.24 GB | the pixel decoder: 0.63 GiB of VRAM, loaded on demand | — | needed by every file |

- **Two W4A8 files:** the int8 dense one also stores the Mamba and attention weights in int8, which makes it the
  fastest and smallest file.
- **Fast path:** every file runs on the pack's CUDA kernels on NVIDIA cards (tested on an RTX 4090 and an RTX 3090).
  With the experts in system RAM, an expert cache on the card serves 97–99.7% of the reads for W6A8 and int8 on a
  24 GB card, and 84% for bf16.
- **RAM** is the server process's own memory while the file is loaded, kept across prompts and released when
  ComfyUI unloads the model. The mapped file's page cache comes on top and is reclaimable.
  - **bf16** needs about 80 GB of RAM available to ComfyUI for its host copies. With less, it runs on the plain
    PyTorch path, about 30 min an image, and says so in the log.
  - **int8 with about 48 GB of RAM**: ComfyUI's RAM-pressure cache can drop the loaded model after each prompt, so
    every prompt loads it again (about 11 s more).
- **VRAM:** the output head's text rows stay in system RAM. With dynamic VRAM (ComfyUI's default) the decoder loads
  its 0.63 GiB on demand and the tokenizer's encoder never reaches the card.

## Speed

Seconds per 1024×1024 image (4,250 tokens), from queueing to the saved image, through a real ComfyUI server.
Hits are the expert cache's share of expert reads.

| Card | File | First call | Warm, 1 image | 4 per batch | 8 per batch | Hits at 1 / 4 / 8 |
|---|---|---|---|---|---|---|
| RTX 4090 | W4A8 | 42.6 | 26.1 | 9.6 | 6.6 | resident |
| RTX 4090 | W4A8 int8 dense | 25.8 | **21.8** | **8.5** | **6.1** | resident |
| RTX 4090 | W6A8 | 42.7 | 33.1 | 12.2 | 9.5 | 99.4 / 99.7 / 99.5% |
| RTX 4090 | int8 | 43.1 | 36.6 | 21.7 | 17.2 | 98.5 / 97.2 / 96.9% |
| RTX 4090 | bf16 | 236.7 | 232.7 | | | 83.8% |
| RTX 3090 | W4A8 | 47.6 | 30.8 | 12.7 | 11.0 | resident |
| RTX 3090 | W4A8 int8 dense | 30.8 | **26.7** | **11.7** | **10.2** | resident |
| RTX 3090 | W6A8 | 49.0 | 38.7 | 16.2 | 13.6 | 99.4 / 99.7 / 99.6% |
| RTX 3090 | int8 | 51.4 | 40.3 | 22.6 | 18.9 | 98.6 / 97.4 / 97.1% |
| RTX 3090 | bf16 | 231.8 | 222.6 | | | 84.0% |

Every row was measured with nothing else on either card. The first call includes loading the file and, for the
files with experts in RAM, copying them there. bf16's pace is set by the link to the card, not by the card: a warm
image reads about 1.9 TB of missed experts.

**Smaller cards**, measured on the 4090 with the rest of the card held by another process (one image, warm):

| Card | File | Seconds per image | Hits |
|---|---|---|---|
| 16 GB | W4A8 | 36.1 | 98.5% |
| 16 GB | W6A8 | 94.7 | 90.4% |
| 12 GB | W4A8 | 77.2 | 88.7% |

**Which file for your card:**
- **24 GB:** a W4A8 file: the int8 dense one takes 22 s an image on a 4090 and 27 s on a 3090, the other 26 and
  31 s, and much less per image in batches. W6A8 if you want it nearer bf16, at about a quarter more time.
- **16 GB:** W4A8, 36 s an image through the expert cache. W6A8 takes 95 s.
- **12 GB:** W4A8, 77 s an image. It is the only file measured on that size.
- **bf16** only to check against the reference: about 3.9 min an image on either card, with about 80 GB of RAM.

The four recommended sizes take the same time as 1024².

## Quality

Each file is teacher-forced on four real 1024² images: the bf16 file's image codes go through it, and the KL
divergence from bf16's next-code distribution is measured at the sampling temperature 0.9, over 16,384 positions.
Lower is closer to bf16.

| File | KL, bf16's expert choices forced | KL, the file's own expert choices |
|---|---|---|
| int8 ConvRot | 0.0149 | 0.0267 |
| W6A8 | 0.0169 | 0.0288 |
| W4A8 | 0.0331 | 0.0465 |
| W4A8 int8 dense | 0.0344 | 0.0480 |

**The floor is 0.016:** running NVIDIA's own model in bf16 instead of fp32 already moves it by that much, so int8
and W6A8 are within the rounding noise of bf16 itself. W4A8 adds about as much again; the int8 dense file adds
3–4% to that.

In the test images (36 images at 1024²: 6 prompts × 2 seeds × W4A8, W6A8 and int8), the three files look like
one quality class. The same seed gives a different image on each file, so they do not compare side by side.

## What the model gets wrong

From the 36 test images:

- **Text** is right 34 times out of 36. The two misses are both on the bakery sign at one seed: "NEMOTRCON" (W4A8)
  and "NEMOTRRON" (int8). The honey label and all three poster lines are exact on every file.
- **Short prompts invite unasked text.** "A cinematic photograph of a red fox in a snowy pine forest at dawn" added
  a signpost with garbled writing in 4 of 6 images.
- **Anatomy** held up: no extra tails or limbs in 6 foxes and a cat at four sizes. The first fox rendered on the
  bf16 file had a tail at each end.
- **Objects:** the cat's mug came out with two handles at two of the four sizes.

## Nodes

**Load Nemotron Image** (`NEMOTRON_IMAGE`)

| Input | |
|---|---|
| `model_name` | A Nemotron Image model file in `models/diffusion_models`. |
| `experts` | `auto` (default): on the GPU when the whole file fits beside about 2.5 GB of working room, else in system RAM. `in RAM` or `on the GPU` force it. |
| `engine` (advanced) | `auto` (default): the pack's CUDA kernels when they support the file and card, else the plain PyTorch path. `reference`: always the plain path, for checking. |

**Nemotron Image Generate** (`LATENT`)

| Input | Default | |
|---|---|---|
| `model` | | From the loader. |
| `prompt` | | Write it in detail: colours, quantities, text to show, shapes, where things are. |
| `width`, `height` | 1024 | Multiples of 16. Recommended: 1024×1024, 1184×880, 1248×832, 880×1184. |
| `seed` | 0 | Image i of a batch does not depend on the batch size. |
| `batch_size` | 1 | Images generated together; much faster per image on a card that holds the experts. |
| `temperature`, `top_p`, `top_k` | 0.9, 1.0, 0 | The model card's settings. |
| `system_prompt` (optional) | | Replaces the model card's system prompt. |
| `vae` (optional) | | The decoder, for a live preview: a real decode of the rows so far, at most every 2 s. Not needed for the image. |

**Load Nemotron Image Decoder** (`VAE`): the decoder file in `models/vae`. Use it with the core **VAE Decode**.
Don't use tiled decoding: it leaves colour blocks at the tile edges.

The example workflow wires Loader → Generate → VAE Decode → Save Image, with the decoder also connected to
Generate for the live preview (start ComfyUI with `--preview-method auto`).

## License

> [!IMPORTANT]
> **Research or evaluation only.** Nemotron-Labs-Image-30B-A3B and its image tokenizer are under the
> [NVIDIA License](LICENSE-NVIDIA). It limits the weights and every derivative work of them, including the quantized
> files, to non-commercial research or evaluation (section 3.3). This pack is also bound by it, because
> `nemotron_image/vae.py` is ported from NVIDIA's proprietary tokenizer code and stays under that license.

The rest of the code is under the [GNU GPL v3](LICENSE). The parts ported from Apache-2.0 sources keep that license
([LICENSE-APACHE](LICENSE-APACHE)). [NOTICE](NOTICE) lists every part and its license. This project is not affiliated
with, sponsored or endorsed by NVIDIA.
