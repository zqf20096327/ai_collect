<p align="center">
  <img src="images/banner.png" alt="Robin. Train any voice. Hear it at 48 kHz. Fixed Seed Research Laboratory." width="100%">
</p>

<p align="center">
  <a href="https://huggingface.co/FixedSeed/Robin"><img src="images/pill-huggingface.png" alt="Hugging Face: FixedSeed/Robin" height="40"></a>
  <a href="https://audiorobin.io"><img src="images/pill-project-page.png" alt="Project page: audiorobin.io" height="40"></a>
</p>

Zero-shot cloning is never good enough for studio work. That's why we trained Robin: an open-weights model built for professionals in the open-source community. It launches with LoRA training scripts included and it renders at 48 kHz, the standard for film and video. Design a voice through text, re-voice your own takes with another voice or train a dedicated adapter model to always produce an exact voice using your own voice data.

- English and Japanese, or both in one line
- 48 kHz audio
- 3.58 B parameters: a 2.17 B planner writes the speech as tokens, and a 1.41 B flow-matching decoder turns that plan into sound
- Peak GPU memory in bf16: 8.2 GB to speak, 9.1 GB to change a voice, 9.9 GB to train a voice

## Files

The weights are on [Hugging Face](https://huggingface.co/FixedSeed/Robin); this repository holds the code.

| File | |
|---|---|
| `robin_v1.safetensors`, `robin_vae.safetensors`, `config.json`, `tokenizer.json` | the model |
| `speech_tokenizer_v3_25hz.onnx` | CosyVoice 3's speech tokenizer, for long text, voice changing and training |
| `robin_character_lora.safetensors` | Robin's own voice, as a LoRA |
| `package/` | the `robin` Python package: command line, app and LoRA training |
| `comfyui-robin/` | the ComfyUI nodes |
| `comfyui-workflow-examples/` | ComfyUI workflows to start from |

## Install

This downloads the weights and the code together:

```
hf download FixedSeed/Robin --local-dir robin
cd robin
pip install ./package
pip install "./package[gui]"   # for the app
```

## Use

```
python -m robin speak "That went better than expected [laughs]" --model . --voice "a warm, low voice, close to the mic" --out take.flac
python -m robin speak "Exactly what my take says." --convert my_take.wav --model . --voice "a bright, fast-talking woman" --out revoiced.flac
python -m robin gui --model .
```

Languages: `--lang en` (default), `--lang ja`, or `--lang mix` for English and Japanese in one line.

Inline tags in square brackets, such as `[laughs]`, `[sigh]`, `[crying]` or `[shouting]`.

`--convert` performs a recording of up to 45 seconds again in another voice, keeping its words, timing and delivery. The text must be exactly what the recording says.

`robin_character_lora.safetensors` is Robin's own voice:

```
python -m robin speak "Hi, I'm Robin." --model . --lora robin_character_lora.safetensors --out robin.flac
```

The app runs in your browser: speak with two takes side by side, change a voice from a description, and train a voice with live progress and a sample at every save.

## Train a voice

Robin learns a new voice through a LoRA trained on transcribed recordings of it. Each voice is saved as one file, and you set its strength when you use it.

A dataset is a folder of clips, each with a `.txt` transcript of the same name, plus an optional `voice.txt` that describes the voice:

```
my_voice/
├── line_001.txt    # what line_001.wav says
├── line_001.wav
├── line_002.txt
├── line_002.wav
├── …
└── voice.txt       # optional: the voice in plain words
```

```
python -m robin prep my_voice/
python -m robin train my_voice/ --model . --out my_voice_lora
python -m robin speak "This is my voice." --model . --lora my_voice_lora/lora.safetensors --out mine.flac
```

`prep` checks the folder first. It lists the clips it will leave out (no transcript, silent, too short or too long) and notes anything worth fixing: clipping, digits, low sample rates, transcripts that may not match, repeated lines. `train` saves a checkpoint every 200 steps and reads a sample line in the new voice at each save, so you can pick a step by ear. Stop it at any time; running it again continues from the last save.

Recommendations:

- **How much:** at least 15 minutes of speech. Our test voices averaged 20 minutes, in about 200 clips.
- **Each clip:** one or two sentences, 3 to 15 seconds. Anything from 1 to 30 seconds is accepted, so split longer takes.
- **Recording:** one speaker in a quiet, dead-sounding room, with the same mic and distance throughout. No music, effects or other voices. Keep peaks around −6 dBFS.
- **Format:** WAV or FLAC at 44.1 or 48 kHz. Lower rates train a duller top end, and clips below 16 kHz are left out.
- **Transcripts:** exactly the words spoken. Write numbers the way they're said ("fifty percent"), and mark sounds and delivery with tags like `[laughs]` or `[sigh]` where they happen. Re-record a stumble instead of transcribing it.
- **Range:** mix statements, questions and exclamations, short lines and long ones. A calm read trains a calm voice, so record the delivery you want back.
- **Tip:** write the script first, then record it line by line. The script is the transcript.

## ComfyUI

![Robin Loader, Robin LoRA and Robin Speak in ComfyUI](images/comfyui-speak.png)

Copy `comfyui-robin` into `ComfyUI/custom_nodes` and install its requirements into ComfyUI's Python:

```
pip install -r ComfyUI/custom_nodes/comfyui-robin/requirements.txt
```

The first run downloads Robin from [Hugging Face](https://huggingface.co/FixedSeed/Robin): the model into `ComfyUI/models/robin/robin`, and Robin's own voice into `ComfyUI/models/loras`. To place the files yourself, put `robin_v1.safetensors`, `robin_vae.safetensors`, `speech_tokenizer_v3_25hz.onnx`, `config.json` and `tokenizer.json` in `ComfyUI/models/robin/robin`, and `robin_character_lora.safetensors` in `ComfyUI/models/loras`.

Two workflows to start from. Drag one onto the ComfyUI canvas:

- [`Robin - LoRA Voice Inference Official.json`](comfyui-workflow-examples/Robin%20-%20LoRA%20Voice%20Inference%20Official.json): Robin's own voice reads a line.
- [`Robin - LoRA Voice Training Official.json`](comfyui-workflow-examples/Robin%20-%20LoRA%20Voice%20Training%20Official.json): checks a folder of clips and trains a voice LoRA on it.

| Node | |
|---|---|
| **Robin Loader** | Loads Robin, downloading whatever is missing on the first run. Its readout shows what is on disk, what is downloading and when Robin is ready. |
| **Robin LoRA** | Applies a voice LoRA at any strength from 0 to 2. `robin_character_lora.safetensors` is Robin's own voice; the voices you train are listed under `robin/`. |
| **Robin Speak** | Reads text in a voice you describe, or in the LoRA's voice. Long text is read in steady pieces, and tags like `[laughs]` can go anywhere. The last take plays on the node, with a download button; connect Save Audio to keep every take. |
| **Robin Voice Changer** | Performs a recording of up to 45 seconds again in another voice, keeping its words, timing and delivery. Give it exactly what the recording says. |
| **Robin Load Audio** | The recording for the Voice Changer. **Record** takes a line from your microphone and trims the silence around it; **Choose file**, or dropping a file on the node, adds one from your computer. Both are kept in `ComfyUI/input`. Recording works when ComfyUI is open on localhost or over https. |
| **Robin Check Dataset** | Checks a folder of clips before training. **Choose folder** uploads one from your computer into `ComfyUI/input/robin_datasets`, or type a path on the machine running ComfyUI. The report lists the clips it will leave out, and why. |
| **Robin Train LoRA** | Trains a voice LoRA on the checked folder, with live steps, losses and time left. Every save writes a checkpoint and reads the sample line in the new voice, which you can play on the node. Ranks, learning rates and the other settings fold away under **advanced**. Cancel the queue to stop; queue it again to continue from the last save. |

![Robin Check Dataset and Robin Train LoRA in ComfyUI](images/comfyui-train.png)

Trained voices are saved in `ComfyUI/models/loras/robin/<name>`: the finished `lora.safetensors`, and a checkpoint for each save.

Speech tokenizer: CosyVoice 3.

## License

Robin is released under the [Fixed Seed Open License](LICENSE).
