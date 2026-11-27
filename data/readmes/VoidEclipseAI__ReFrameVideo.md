<p align="center"><img src="web/reframe-favicon.svg" alt="ReFrameVideo" width="120"></p>

# ReFrameVideo

English · [中文](README_zh.md) · [LoRA](https://huggingface.co/VoidEclipseAI/ReFrameVideo-LoRA) · [Installation](docs/INSTALL.md) · [Tutorial](web/ui/tutorial-en.md)

**An open-source toolkit for editing and regenerating video frames: change anything, freely.**

https://github.com/user-attachments/assets/8cbb910d-248c-41c0-be0c-d0c10e85afd0

<sub>The promo uses film clips, shown only to demonstrate the tool. All rights belong to their owners.</sub>

ReFrameVideo is an open-source personal project that lets you freely change the picture of an existing video. Move, scale or delete the people and objects in it, or change the aspect ratio, and AI regenerates the whole clip. It has two parts:

- **A video editor**: uses SAM 3.1 to turn the elements of a video into layers that you edit freely, as in Photoshop, with reference images to control the final shot.
- **The ReFrameVideo LoRA**: trained on MiniMax H3, it regenerates the whole clip from your edit and fills in the gaps naturally.

## Features

- **Detect subjects**: type a name or click in the image to cut people and objects out as layers (SAM 3.1, with optional MatAnyone2 soft edges for hair).
- **Edit the shot**: move, scale, flip and hide layers, expand or crop the frame, and use masks to control what gets redrawn; with versions and an action history.
- **Generate references**: create a first frame, a background and other reference images from your edit (Qwen Image 2.1 or MiniMax H3 Image) and pick the best one.
- **Generate video**: MiniMax H3 + the ReFrameVideo LoRA regenerate the whole clip; long videos can be edited in segments.
- **Extend and export**: plug in your own ComfyUI workflows or a cloud API; every input given to the model, and the workflow, can be exported.

## Getting started

You need Python 3.10+, [FFmpeg](https://ffmpeg.org/) (on PATH) and a machine with ComfyUI (can be this one).

1. **Set up ComfyUI**: install the models listed in the [installation guide](docs/INSTALL.md); copy `comfyui/ComfyUI-Reframe/` into ComfyUI's `custom_nodes/`; put the ReFrameVideo LoRA ([Hugging Face](https://huggingface.co/VoidEclipseAI/ReFrameVideo-LoRA) / [ModelScope](https://modelscope.cn/models/VoidEclipseAI/ReFrameVideo-LoRA)) in `models/loras/`.
2. **Download and start**:

   ```bash
   git clone https://github.com/VoidEclipseAI/ReFrameVideo.git
   cd ReFrameVideo
   ```

   On Windows, double-click `start.bat` (the first run installs the dependencies). On Linux / macOS:

   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   .venv/bin/python start.py
   ```

3. On first launch, enter the ComfyUI address (press Enter if it runs on this computer). Your browser opens `http://127.0.0.1:8765`.

## Tutorial: an example

An AI-generated clip of a woman sitting at a desk. We shrink her and the cup together, then expand the landscape frame to 1:1 and let the model paint the new areas above and below. All screenshots come from this project.

**1. Detect**: click "+" at the top to import the video. In the **Layers** panel, type `person` and click **Detect**, then do the same for `cup`. Select both layers and merge them so they move together.

![Detect the person and the cup, then merge them into one layer](web/ui/tutorial/en/1_detect.jpg)

**2. Edit**: scale the layer down to 87%, and set the ratio to 1:1 under **Frame**. The checkerboard marks empty space (where the person was, plus the new strips above and below) that the model fills in during generation.

![Person scaled down, frame expanded to 1:1](web/ui/tutorial/en/2_edit.jpg)

**3. Check the redraw area**: press `M` to see what will be redrawn: red = fill in, green = keep, dark red = the blend band between new and old pixels. The default **Vacated shape: Rect ×3** turns the person-shaped hole into blocks, so the model is less likely to paint another person into it. Adjust it in the **Mask** panel if needed.

![Press M to show the redraw area](web/ui/tutorial/en/3_mask.jpg)

**4. Generate a first frame**: click "+" in the page bar to add a **First frame**, click **Generate candidates** in the **Generate** panel (four at a time), and pick the cleanest one in **Image results**. The first frame sets the look of the result; it is optional, but a clean one makes results much more stable.

![Pick the first frame in Image results](web/ui/tutorial/en/4_first_frame.jpg)

**5. Generate the video**: go back to **Video editing**, open the **Generate** panel, check that this first frame is among the references, and click **Generate video**. Recommended: LoRA at 1.0 plus the [Pika H3 Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex) speed-up LoRA at 6 steps; the prompt can stay empty. A 5-second clip takes about 4–5 minutes on an RTX 4090, and the result appears in **Video results**.

![The Generate panel](web/ui/tutorial/en/5_generate.jpg)

**Result** (top left to bottom right: original, rough cut (gray = to be filled), selected first frame, output):

![Original, rough cut, first frame and output](docs/images/tutorial/compare.jpg)

The output video (left: original, right: result):

https://github.com/user-attachments/assets/d0faf678-9df7-4419-8916-b3ce83fd1724

The book icon in the app's left toolbar opens this tutorial at any time. For more (removing a person, replacing the background, long videos, exporting to your own ComfyUI) see the [full tutorial](web/ui/tutorial-en.md). To run the exported inputs in your own ComfyUI, see [Run in your own ComfyUI](web/ui/tutorial-comfyui-en.md).

## How it works

ReFrameVideo does no 3D reconstruction: you decide where things go and what may change, and the model produces a plausible result from the original video and the references. The editor turns your edit into three inputs for MiniMax H3:

- **Rough cut**: the video with objects in their new positions and the gaps painted gray;
- **Mask**: marks, frame by frame, what to redraw and what to keep;
- **First frame**: what the final picture should look like.

The ReFrameVideo LoRA teaches H3 to treat the gray as "empty, fill me"; without it, H3 often copies the gray. See [how it works](docs/工作原理.md) (Chinese).

## Known limitations

- **Output quality**: people may deform, extra objects may appear, backgrounds may be wrong or frames inconsistent; check large moves and complex occlusion carefully.
- **Camera motion**: testing mostly covered static shots, slow pans and tracking shots. Fast whip pans, orbits and big zooms are not well tested and may work much worse. Edits are placed in screen space, so with large camera moves a moved object may not stay attached to the scene.
- **Visual style**: the LoRA was trained on live-action footage only, so animation, cartoons and 3D renders may work less well.
- **Kept areas**: the final video is the model's full output and is not pasted back pixel by pixel, so kept areas may differ slightly.
- **Security**: the backend is for the local browser only and has no authentication; do not expose it to the internet.
- **Platforms**: fully tested on Windows only.
- **Why the editor isn't part of ComfyUI**: editing means dragging layers on the frame, checking masks frame by frame, adjusting frame ranges on a timeline and previewing again and again. That kind of interaction is hard to use inside ComfyUI's node graph, so ReFrameVideo is a standalone editor and ComfyUI only runs the models. Every input sent to the model (rough cut, mask, reference images, prompt) and the `workflow_api.json` can be downloaded with **Export**, ready to generate in your own ComfyUI workflow. Example: [workflows/ReFrameVideo_H3_example_workflow_api.json](workflows/ReFrameVideo_H3_example_workflow_api.json) is the workflow behind the tutorial example's final video.

## Feedback and support

ReFrameVideo is a one-person project. I did the concept, the LoRA training, the interaction design and the testing; the code and documentation were written with the help of an AI coding assistant (Claude Code).

- **Feedback**: please open an Issue for problems or requests, with steps to reproduce and logs.
- **Donations / compute**: you can support the project on [Ko-fi](https://ko-fi.com/voideclipseai); it mainly pays for training compute. The next LoRA is planned to add person and object replacement, any-keyframe references and more visual styles. If you can offer GPU compute, please get in touch.
- **Collaboration**: I am open to integration, custom development and research collaboration.

Contact: email voideclipseai@gmail.com · WeChat voideclipseai

## Acknowledgements

ReFrameVideo is built on these open-source projects and models. Thanks to their authors:

- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) and [MiniMax H3 Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) (MiniMax): the video and image-editing models, and the base model of the ReFrameVideo LoRA.
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI): every model runs in ComfyUI. Thanks also to Comfy-Org for packaging [MiniMax H3](https://huggingface.co/Comfy-Org/MiniMax-H3) and other model files.
- [Pika H3 Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex) (Pika): the speed-up LoRA behind 6-step generation.
- [SAM 3](https://github.com/facebookresearch/sam3) (Meta): subject detection and segmentation.
- [Qwen Image](https://github.com/QwenLM/Qwen-Image) and [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) (Qwen team): reference images and image-to-prompt descriptions.
- [MatAnyone 2](https://github.com/pq-yang/MatAnyone2) and the [ComfyUI-MatAnyone](https://github.com/FuouM/ComfyUI-MatAnyone) node: soft edges such as hair.
- [FFmpeg](https://ffmpeg.org/), FastAPI, OpenCV, NumPy and other open-source libraries.

## License

Copyright © 2026 VoidEclipseAI

- **ReFrameVideo** (including the `comfyui/ComfyUI-Reframe/` node pack): [GNU AGPL-3.0](LICENSE). You may use, modify and use it commercially for free; if you distribute a modified version or offer it as a network service, you must release its source under AGPL-3.0.
- **Commercial license**: available if AGPL-3.0 does not suit you (for example, closed-source integration into your product). Contact: email voideclipseai@gmail.com · WeChat voideclipseai
- **Models**: this repository contains no models. The ReFrameVideo LoRA is a MiniMax H3 derivative under the MiniMax H3 Community License Agreement; other models follow their own licenses, so please review them before use. Sources of third-party prompts are in [app/prompts/THIRD_PARTY.md](app/prompts/THIRD_PARTY.md) (Chinese).
