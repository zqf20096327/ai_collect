[English](README.md) · [한국어](README.ko.md) · [中文](README.zh-cn.md)

# image-editing-qwen-image-anyangle

This service changes the camera angle of a photo with Qwen-Image-2.1-Turbo and the AnyAngle LoRA. It takes the source photo together with a rough guide image rendered from a 3D model, and redraws the source from the guide's camera angle.

![Entering width, height, and seed in the gradio interface, uploading a source photo and a 60° guide, and getting the photo redrawn at the guide's angle](docs/images/shared/turbo-anyangle-webui-demo.gif)

## Quick start

It needs [model-compose](https://github.com/hanyeol/model-compose) at commit `51c7171c` or later. That version is not on PyPI yet, so install it from GitHub.

Install with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install "git+https://github.com/hanyeol/model-compose@51c7171c" python-multipart
```

Or with pip:

```bash
pip install "git+https://github.com/hanyeol/model-compose@51c7171c" python-multipart
```

Clone this repository:

```bash
git clone https://github.com/MindrLabs/image-editing-qwen-image-anyangle
cd image-editing-qwen-image-anyangle
```

Run it:

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True model-compose up
```

`expandable_segments` is on so that it fits on a 24 GB GPU. The first run downloads `Qwen/Qwen-Image-2.1-Turbo` (about 32.5 GB) and the AnyAngle LoRA (about 120 MB); no token is needed.

The API is at http://localhost:8096/api and the Gradio UI at http://localhost:8097. It takes two images, a source photo and a guide; see [Making a guide](#making-a-guide) for how to make the guide.

## Summary

Given a source photo and a 3D guide, Turbo + AnyAngle turns the person a full circle, following the guide's angles. With a text instruction and no guide, it barely turns left or right. Props such as the table change from angle to angle, and product labels can break.

![C-2 source, 12 3D guides at 30° steps, and the 12 results turned by those guides](docs/images/en/c2-guide-orbit.jpg)

Figure 1 (RTX 4090, seed 42): The results (bottom rows) follow the angles of the 3D guides (top rows) and turn the source person a full circle. The guides are a 3D model rendered on a gray background, so they have no background, a distorted face, and dark colors overall. The results bring back the source's background, colors, and face.

| Device | Status | One image (s, 896×1184, 8 steps) | Peak GPU memory (MiB) |
| :---: | --- | --- | --- |
| RTX 4090 (bf16, offload) | Measured | 33 | 23845 |
| DGX Spark (bf16, no offload) | Measured | 22.6 | 44421 |
| Apple M2 16GB (nf4) | Stopped (out of memory) | — | — |

- Each device ran the setting it could run. Loading the whole model without offload takes 44,421 MiB (measured on the DGX Spark), which does not fit in the RTX 4090's 24 GB, so offload was on there and off on the DGX Spark. The two times are not a like-for-like comparison.
- On the RTX 4090, peak GPU memory is the whole GPU's usage, so it includes about 1,089 MiB from another process on the same GPU. The DGX Spark has unified memory, so we summed only this service's processes as reported by nvidia-smi.
- On the DGX Spark, the results matched the RTX 4090 in angle and framing (C-2, TripoSplat guides at 12 angles, mean pixel difference 9.0–15.3 on a 0–255 scale).

## Test setup

We measured on one RTX 4090 (24 GB) and a DGX Spark (GB10, 128 GB unified memory) with Turbo at 8 steps, `true_cfg_scale` 1, AnyAngle strength 1.0, and 896×1184 output. On the RTX 4090 we turned on `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` to fit in 24 GB. Both machines are shared with other users. With few inputs and seeds we ran no statistical tests; numbers are per-image values or per-input ranges.

| ID | Content |
| :---: | --- |
| B-1 | Underwater background, person + serum bottle (ONDA) |
| B-2 | Sky background, person + mist bottle (SOLEN) |
| C-2 | Gray background, person + lipstick (mauve.lab) |
| M-1 | White background, male person + lip tint (mauve.lab) |

![The 4 inputs B-1, B-2, C-2, M-1](docs/images/en/inputs.jpg)

Figure 2: The 4 inputs. All are fictional people and products made beforehand with Qwen-Image-2.1; no photos of real people were used.

<details>
<summary>Tests and metrics</summary>

| Test | Conditions |
| :---: | --- |
| 3D guide (RTX 4090) | 4 inputs × 12 guide angles × seed 42. For C-2, B-1, and M-1 we also ran seeds 7·123 and AnyAngle off at 0·90·180·270° |
| 3D guide (DGX Spark) | C-2 × 12 TripoSplat guide angles × seed 42. Offload on ran only at 0·30·60° |
| Text instruction (RTX 4090) | 4 inputs × 6 instructions × seed 42, AnyAngle on and off |

| Metric | Meaning | Better |
| :---: | --- | --- |
| Face yaw | How far the face turned left or right relative to the input face. Guide tests use the same sign as the guide direction; text instructions count left as + | Closer to the guide or instructed angle |
| Face pitch | Angle up or down relative to the input face, + when looking up | Larger in the instructed direction |
| Face similarity | Cosine similarity of InsightFace (antelopev2) face embeddings against the input | Higher. Profiles score low even for the same person |
| Face size | Area of the face box relative to the input | Neutral in guide tests. For text instructions, smaller for wide and larger for close-up |
| Label CER | Character error rate of the product brand text (in parentheses in the table above) read by RapidOCR; 0 is exact | Lower |

</details>

<details>
<summary>Weights, software, and guide details</summary>

| Item | Details |
| :---: | --- |
| Weights | [Qwen/Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo/tree/fc13ba1986fcb905854dc8de2f52eee395f49b5b) + [lilylilith/QI_2.1_AnyAngle](https://huggingface.co/lilylilith/QI_2.1_AnyAngle/tree/5c8b4c8e05ba6328d54bf8d34ec724fef5a414ae) |
| LoRA file | A copy with the keys split. Difference from the original file: mean pixel difference 4.5–6.8 (DGX Spark, C-2 at 4 angles) |
| model-compose | RTX 4090: commit `493b9db5` (Pixal3D guide, text instructions), PyPI 0.4.125 (TripoSplat guides) / DGX Spark: commit `51c7171c` |
| Quick start recheck | RTX 4090, commit `51c7171c` with the original LoRA file, C-2 at 4 angles: same angles and framing (mean pixel difference 6.8–11.4) |
| DGX Spark environment | torch 2.13.0+cu130, diffusers 0.43.0, transformers 5.23.0, peft 0.21.3, driver 580.126.09 |
| Guide 3D | C-2: Pixal3D Mac port (`raven38/pixal3d-sv-q8_0-v1`) / all 4 inputs: TripoSplat (code `d8db9e0`, weights `56a96e6`) |
| Guide render | From the source viewpoint at 30° azimuth steps, gray background |
| Timing | From the second request after the server started. The first request, including model loading, took 57–388 s |

</details>

## Results

| Claim | How we checked | Pass |
| :---: | --- | --- |
| The face turns with the guide angle. | Face yaw, 4 inputs | ✓ |
| The person, clothes, and hair stay consistent all the way around. | Judged by eye | ✓ |
| The guide's distorted face does not carry into the result. | Judged by eye (near-frontal angles, zoomed in) | ✓ |
| The source background, which the guide lacks, carries over to other angles. | Judged by eye (B-1 underwater, B-2 sky) | ✓ |
| The result follows the guide angle only with AnyAngle. | AnyAngle on vs off (C-2, B-1, M-1) | ✓ |
| A different seed gives the same angle. | 3 seeds compared (C-2, B-1, M-1) | ✓ |
| The product label is readable at near-frontal angles. | Label CER (0·30·330°) | ✓ B-1, B-2, M-1 / ✗ C-2 |
| Props such as the table stay the same as the angle changes. | Judged by eye (C-2) | ✗ |
| A text instruction alone turns the camera 45° left or right. | Face yaw, AnyAngle on and off | ✗ at most 14° even with it on (M-1) |
| Wide, close-up, bird's-eye, and low angle work with Turbo alone. | Face size, face pitch | ✓ bird's-eye was weak on B-1 at −2° |

### Does it follow the guide angle?

Yes. In C-2 in Figure 1, the face turned about 1° short at 30° and 330°, 2–5° short at 60° and 300°, and 15° short at 90°; at 270° it reached 85–90° across 3 seeds.

- The output framing follows the guide and sits farther away than the input. Even at the front (0°) the face is 0.39–0.44× the input size, and the table and arms come into frame.
- The table changes from an angular edge at 0–60° to a round top at 90°. It is in neither the input nor the guide, so the model drew it anew at each angle.
- The label on the product in her hand is unreadable all the way around (CER 0.89–1.00). The 4 images with AnyAngle off keep a framing close to the input (face size 0.77–1.0×) and have a CER of 0–0.11.
- Zoomed in, the frontal face kept none of the guide's distorted eyes. The skin is less glossy than in the source.

<details>
<summary>Numbers: C-2 face and label by guide angle</summary>

| Guide angle | Face yaw | Face similarity | Face size | Label CER |
| :---: | --- | --- | --- | --- |
| 0° | 0.0° | 0.91 | 0.39× | 1.00 |
| 30° | 28.9° | 0.71 | 0.33× | 1.00 |
| 60° | 55.3° | 0.59 | 0.28× | 1.00 |
| 90° | 75.0° | 0.29 | 0.18× | 1.00 |
| 270° (−90°) | −84.9° | 0.55 | 0.29× | 1.00 |
| 300° (−60°) | −57.9° | 0.65 | 0.33× | 0.89 |
| 330° (−30°) | −28.8° | 0.80 | 0.35× | 1.00 |

Each cell is one C-2 image at seed 42. The back views (120–240°) are left out because no face was found or the values were unstable.

</details>

### Does it work on other photos?

Yes. B-1, B-2, and M-1 were turned with TripoSplat guides, and C-2 was turned once more with a TripoSplat guide to compare against the Pixal3D guide (Figure 1). The recipe and output size are the same.

![TripoSplat guides and results for B-1, B-2, M-1, C-2 at 60° steps](docs/images/en/triposplat-orbit.jpg)

Figure 3 (RTX 4090, seed 42): For each input, the top row is the TripoSplat guide and the bottom row is the result. Only 60° steps are shown. The splat guides keep much more of the source colors than the Pixal3D guide.

- The water of B-1 and the sky of B-2, which the guides lack, carried over all the way around. B-1's underwater scene, though, became one of her standing waist-deep in water.
- B-2's guide rendered the white top as blue in the back views, but the results kept the top white.
- B-1, B-2, and M-1 are already turned 6–8° the other way at 0°. For B-1 and M-1 the same bias appeared across 3 seeds, so it is not random noise.
- At 90°, the three inputs reached 61–70°, turning less than C-2 (74–76°).
- On the three inputs, the brand text on the label read almost exactly at 0·30·330°, while small text such as the volume on B-1 and B-2 was smeared. C-2's label broke with both guides (CER 0.56–1.00).
- For C-2, the face angles from the two guides differed by 1–8°. This is a comparison on one input.

<details>
<summary>Numbers: guide angle, face, and label by input</summary>

| Guide angle | B-1 | B-2 | M-1 | C-2 (TripoSplat) | C-2 (Pixal3D) |
| :---: | --- | --- | --- | --- | --- |
| 0° | −7.6° | −6.9° | −6.1° | 2.2° | 0.0° |
| 30° | 12.8° | 27.3° | 22.2° | 35.1° | 28.9° |
| 60° | 42.5° | 54.7° | 51.4° | 58.7° | 55.3° |
| 90° | 62.2° | 61.3°† | 66.1° | 76.3°† | 75.0° |
| 270° (−90°) | −104.0°† | −103.7° | −96.4° | −77.3° | −84.9° |
| 300° (−60°) | −75.3° | −73.8° | −65.4° | −51.0° | −57.9° |
| 330° (−30°) | −33.3° | −40.7° | −30.5° | −26.1° | −28.8° |

| Input (label) | Label CER 0° / 30° / 330° | Face size at 0° |
| :---: | --- | --- |
| B-1 (ONDA) | 0.00 / 0.00 / 0.00 | 0.52× |
| B-2 (SOLEN) | 0.00 / 0.00 / 0.00 | 0.45× |
| M-1 (mauve.lab) | 0.00 / 0.33 / 0.00 | 0.52× |
| C-2, TripoSplat (mauve.lab) | 0.56 / 1.00 / 1.00 | 0.40× |
| C-2, Pixal3D (mauve.lab) | 1.00 / 1.00 / 1.00 | 0.39× |

Each cell is one image at seed 42. The back views, 120–240°, are left out. † marks values whose pitch exceeded ±45°, where estimation on a profile may have been unstable. Zoomed to the source size, 0·30·330·300° kept the source face and hair on all three inputs.

</details>

### Is AnyAngle needed?

Yes. With AnyAngle off, the result stays frontal even as the guide turns (RTX 4090). On C-2, B-1, and M-1, the face yaw stayed within 0.6° and face similarity was 0.92–0.96: the model redrew the source almost as is. With it on, seeds 42, 7, and 123 turned to the same angle (within 5°).

![C-2 with the same guides at 0·90·180·270°, AnyAngle off and on](docs/images/en/c2-lora-on-off.jpg)

Figure 4 (RTX 4090, seed 42): C-2. The guide turns, but the AnyAngle-off row stays frontal; only the on row follows the guide angle.

<details>
<summary>B-1 and M-1 figure and numbers by seed</summary>

![B-1 and M-1 with the same guides at 0·90·180·270°, AnyAngle off and on](docs/images/en/triposplat-lora-on-off.jpg)

Figure 5 (RTX 4090, seed 42): The same test as Figure 4, on B-1 and M-1 with TripoSplat guides.

| Condition | C-2 | B-1 | M-1 |
| :---: | --- | --- | --- |
| AnyAngle on, 0° | −1.2 to 0.0° | −7.6 to −6.1° | −7.3 to −6.1° |
| AnyAngle on, 90° | 73.5–75.0° | 62.2–65.2°† | 66.1–69.8° |
| AnyAngle on, 270° | −89.7 to −84.9° | −104.0 to −101.5°† | −96.4 to −94.5° |
| AnyAngle off, 4 angles | −0.5 to 0.0° | 0.2–0.6° | 0.1–0.3° |
| AnyAngle off, face similarity | 0.93–0.95 | 0.92–0.95 | 0.95–0.96 |

AnyAngle on is the range over seeds 42·7·123; AnyAngle off is the range over 0·90·180·270° at seed 42. With AnyAngle on, 180° is a back view with no face.

</details>

### What about a text instruction with no guide?

Wide, close-up, bird's-eye, and low angle work with Turbo alone, but a 45° turn to the left or right barely happens even with AnyAngle on. This test gave only the source photo and a text instruction; it is not how the AnyAngle card says to use the LoRA.

![C-2 with 6 text instructions, AnyAngle off and on](docs/images/en/text-anyangle-on-off.jpg)

Figure 6 (RTX 4090, seed 42): C-2. The top row has AnyAngle off and the bottom row on. For the left and right 45° instructions, it barely turns even with AnyAngle on.

- At left 45° with AnyAngle on, only M-1 turned 14°; the other 3 stayed within 6°.
- With AnyAngle off, bird's-eye was weak on B-1 at −2°. With it on, B-1 reached −7°, B-2 −12°, and C-2 −15°, looking down more than with it off; M-1 was about the same at −11° and −10°.
- C-2 wide, both on and off, added a table and a second lipstick that the input did not have.

<details>
<summary>Instruction wording and numbers</summary>

Each of the 6 instructions is Chinese followed by an English translation.

| Instruction | Wording |
| :---: | --- |
| Wide | `将镜头转为广角镜头 Turn the camera to a wide-angle lens.` |
| Close-up | `将镜头转为特写镜头 Turn the camera to a close-up.` |
| Left 45° | `将镜头向左旋转45度 Rotate the camera 45 degrees to the left.` |
| Right 45° | `将镜头向右旋转45度 Rotate the camera 45 degrees to the right.` |
| Bird's-eye | `将镜头向上移动，俯视角度 Move the camera upwards to a bird's-eye view.` |
| Low angle | `将镜头向下移动，仰视角度 Move the camera down to a low-angle view.` |

Each cell is the range over the 4 inputs (B-1, B-2, C-2, M-1) at seed 42.

| Instruction | Measure | Turbo | Turbo + AnyAngle |
| :---: | --- | --- | --- |
| Wide | Face size | 0.07–0.17× | 0.10–0.18× |
| Close-up | Face size | 1.7–2.6× | 1.6–2.6× |
| Left 45° | Yaw | −0.4 to +2.5° | −2 to +14° |
| Right 45° | Yaw | −0.2 to −5° | −2 to −6° |
| Bird's-eye | Pitch | −2 to −11° | −7 to −15° |
| Low angle | Pitch | +7 to +28° | +7 to +20° |
| Left 45° | Face similarity | 0.93–0.95 | 0.87–0.93 |

</details>

## Recommendations

- For a chosen angle or a 360° turn, make a 3D model of the source, render guides from it, and use Turbo + AnyAngle. Turn AnyAngle on at strength 1.0 and pass the images in `[source, guide]` order (`source`, `guide`).
- Making the guide 3D with TripoSplat (9–11 s per input on the RTX 4090) was enough for all 4 inputs to follow the guide angles. We compared it with Pixal3D on only one input, C-2.
- On a machine with shared memory, such as the DGX Spark, delete the `cpu_offload: model` line from `model-compose.yml`. The results stay the same and the time per image dropped from 196–267 s to 22.6 s.

## Making a guide

A guide is an image rendered at the angle you want from a 3D model of the source photo. You can make the 3D with [TripoSplat](https://github.com/VAST-AI-Research/TripoSplat) or [Pixal3D](https://github.com/MindrLabs/image-to-3d-pixal3d/blob/main/README.md); this report used both. Render it with a tool such as Blender, and meet the conditions below.

| Condition | What to do |
| :---: | --- |
| Aspect ratio | Same as the source photo. This report rendered at 1024 pixels on the long side |
| 0° | Same viewpoint as the source photo |
| Background | Solid gray |
| Camera | 50 mm lens (36 mm sensor), object filling about 80% of the frame |

Example request (source + guide):

```bash
curl -o out.png localhost:8096/api/workflows/runs \
  -F workflow_id=generate -F wait_for_completion=true -F output_only=true \
  -F "input.source=@photo.png;type=application/octet-stream" \
  -F "input.guide=@guide.png;type=application/octet-stream" \
  -F input.width=896 -F input.height=1184 -F input.seed=42
```

Put the source photo in `source` and the guide in `guide`. Without an output size, the output follows the guide's aspect ratio, so set `width` and `height` to match the source. The default prompt is the LoRA card's `Change the camera angle from <image2> to <image1>.`

## Limitations and what we did not measure

### Limitations of the model

- It needs a guide. A text instruction alone barely turns the person 45° left or right (at most 14° even with AnyAngle on), so making a 3D model of the source is an extra step.
- It turns less toward the side. With a 90° guide, the face turned only 61–76°.
- Anything the guide lacks is redrawn at each angle. C-2's table changed shape, and B-1's underwater scene became one of her standing waist-deep in water.
- Labels on products held in the hand can break. C-2's label was not read correctly at any measured angle (CER 0.56–1.00), and the small text on B-1 and B-2 was smeared.
- It uses a lot of memory. It fills nearly all of a 24 GB card (23,845 MiB, including other processes), and a 16 GB Mac could not load it even in nf4.

### What we did not measure

- The regular Qwen-Image-2.1 (20 steps) made no images on the RTX 4090 24 GB: GPU memory allocation failed during the first step. So we could not compare against the setting the LoRA card calls best (CFG 3, 20+ steps).
- All inputs are generated images, so we did not check whether photos taken with a camera give the same results.

### Model card claims we did not verify

[AnyAngle LoRA card](https://huggingface.co/lilylilith/QI_2.1_AnyAngle/blob/5c8b4c8e05ba6328d54bf8d34ec724fef5a414ae/README.md):

- Results are best on the regular Qwen-Image-2.1 with CFG 3 and 20 or more steps.
- A Turbo model or Turbo LoRA is faster but loses some quality.
- The author made guides with Tripo Splat (Gaussian splats) or Trellis2 (3D models), and other splat and 3D generators also work. This report used TripoSplat (4 inputs) and Pixal3D (C-2), which the card names as an example of another generator; it did not use Trellis2.
- It can change the angle of illustrations and sketches as well as photos.
- If the 3D model gets the space wrong or is too rough (badly distorted anatomy or face), props get misplaced, and an unclear or low-resolution face can come out broken. (In this report, C-2's table changed at each angle, and the guide's distorted face did not carry into the results on any of the 4 inputs.)

## License

| Item | License | Commercial use |
| :---: | --- | :---: |
| This service | [`LICENSE`](LICENSE) | ✓ |
| Qwen/Qwen-Image-2.1-Turbo weights | [Qwen Research License](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo/blob/fc13ba1986fcb905854dc8de2f52eee395f49b5b/LICENSE) | ✗ |
| lilylilith/QI_2.1_AnyAngle LoRA | [Apache-2.0](https://huggingface.co/lilylilith/QI_2.1_AnyAngle/blob/5c8b4c8e05ba6328d54bf8d34ec724fef5a414ae/README.md) | ✓ |
| Guide 3D model generation: the Pixal3D Mac port [`pixal3d.cpp`](https://github.com/raven38/pixal3d.cpp) and `raven38/pixal3d-sv-q8_0-v1` | MIT; among the weights, only `dinov3.gguf` is under the DINOv3 License | Port ✓, DINOv3 not checked |
| Guide 3D generation: [TripoSplat](https://github.com/VAST-AI-Research/TripoSplat/tree/d8db9e018b413dd9c4a9fe22463781bf98e8e68d) and the [`VAST-AI/TripoSplat`](https://huggingface.co/VAST-AI/TripoSplat/tree/56a96e603204ec410c4da60c13ea4fa09a2169a9) weights | MIT. The DINOv3 encoder and FLUX.2 VAE inside the weight bundle have their own licenses | Code ✓, individual weights in the bundle not checked |

The AnyAngle LoRA is Apache-2.0, but the base weights are under a non-commercial license, so commercial use of Turbo + AnyAngle follows the base license. The input images were made with Qwen-Image-2.1, which is under the [Qwen Research License](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/d26bb61231c349cf6b7896fa83353113880e1ba3/LICENSE). The 3D models for guides are not part of this service and are made separately. The official Pixal3D pipeline uses a non-commercial model for background removal; for the licenses of other routes, see the [license section of the Pixal3D report](https://github.com/MindrLabs/image-to-3d-pixal3d/blob/main/README.md#license).
