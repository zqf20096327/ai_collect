> 🚧 Experimental! – This package is in an early, exploratory stage and not production-ready. Expect sharp edges, breaking changes, and general chaos.

<a href="https://www.doji-tech.com/">
  <img src="https://www.doji-tech.com/assets/favicon.ico" alt="doji logo" title="Doji" align="right" height="70" />
</a>

# Diffusers
A Unity package to run pretrained diffusion models with Unity Sentis

[OpenUPM] · [Documentation (coming soon)] · [Feedback/Questions]

## About

This is essentially a port of Hugging Face’s [diffusers] library.

As of today only a limited number of pipelines and schedulers are supported (see below).

### Installation

<details>
  <summary> via OpenUPM </summary>
  
 1. In `Edit -> Project Settings -> Package Manager`, add a new scoped registry:

        Name: Doji
        URL: https://package.openupm.com
        Scope(s): tools.doji
 
  4. In the Package Manager install `tools.doji.diffusers` either by name or select it in the list under `Package Manager -> My Registries`

</details>

### Models

Models are delivered by [AI Model Hub] (`tools.doji.model-hub`), which is installed with this package.

- The package declares no model. Add the models you use to the project's manifest in `Project Settings > Doji > AI > AI Model Hub`, then download them there or in `Window > AI Model Hub`. One entry per model is enough, for example the default model [julienkay/sd-turbo]:

  ```json
  { "id": "julienkay/sd-turbo", "revision": "3c071e3da77c6e88ec2f174a185ce76ddd801c2a" }
  ```

  Without `files`, AI Model Hub takes every file of the repository. Pin a commit as `revision` for reproducible builds.
- Each part of a pipeline, for example `unet`, is `{part}/model.sentis` or `{part}/model.onnx`. Prefer repositories with `.sentis` files, such as [julienkay/FLUX.2-klein-4B-sentis-uint8]: they load as they are. AI Model Hub converts `.onnx` files once, which takes time and memory. When the project has both files of a part, the pipeline loads the `.sentis` file.
- List `files` only when the repository holds more than the pipeline reads, for example PyTorch weights, both `.onnx` and `.sentis` files, or components such as `safety_checker`. The pipelines read `model_index.json`, `scheduler/scheduler_config.json`, the `tokenizer/` files, and the model files and configs of `text_encoder`, `unet` (FLUX.2: `transformer`), `vae_decoder` and (for img2img) `vae_encoder`; SDXL also `tokenizer_2/` and `text_encoder_2/`.
- Builds bundle the models, or download them at runtime, as the AI Model Hub project settings say.

Review each model's license on Hugging Face before you use it.

### Usage

```csharp
using Doji.AI.Diffusers;

// Works on every platform. Models set to download at runtime are fetched on first use.
var pipeline = await DiffusionPipeline.FromPretrainedAsync("julienkay/sd-turbo", progress: progress);
var image = await pipeline.GenerateAsync("a cat", numInferenceSteps: 1, guidanceScale: 0f);

// High-level wrapper with txt2img and img2img, rendering to a RenderTexture.
using var sd = await StableDiffusion.FromPretrainedAsync("julienkay/sd-turbo");
```

`FromPretrained` (without `Async`) loads without waiting. It works in the Editor and for bundled or already downloaded models on Windows, macOS, Linux and iOS.

### Features/Roadmap
Some things that might be worked on next are:
- [x] add/fix classifier-free guidance
- [ ] support more models
  - [x] SD 1.5
  - [x] SD 2.1
  - [x] SDXL
  - [x] SD-Turbo
  - [x] SDXL-Turbo
  - [x] FLUX.2 [klein] (txt2img)
  - [ ] LoRA models
- [ ] more scheduler implementations
  - [x] PNDM
  - [x] DDIM
  - [x] EulerDiscrete
  - [x] EulerAncestralDiscrete
  - [x] FlowMatchEulerDiscrete
  - [ ] LCM
  - [ ] DDPM
  - [ ] KDPM2Discrete
  - [ ] KDPM2AncestralDiscrete
- [ ] more pipeline/model types
  - [x] txt2img
  - [x] img2img,
  - [ ] inpaint,
  - [ ] upscale,
  - [ ] depth2img
  - [ ] marigold
- [x] async pipeline methods (sliced inference)
- [ ] support multiple images per prompt
- [ ] write some documentation

### Dependencies
- [AI Model Hub] (`tools.doji.model-hub`)
- [tools.doji.transformers]
- [tools.doji.pngcs]

[OpenUPM]: https://openupm.com/packages/tools.doji.diffusers
[Documentation (coming soon)]: https://github.com/julienkay/tools.doji.diffusers
[Feedback/Questions]: https://discussions.unity.com/t/stable-diffusion-diffusers-transformers-package/332701?u=julienkay
[diffusers]: https://github.com/huggingface/diffusers
[tools.doji.transformers]: https://github.com/julienkay/tools.doji.transformers
[tools.doji.pngcs]: https://github.com/julienkay/tools.doji.pngcs
[AI Model Hub]: https://docs.doji-tech.com/tools.doji.model-hub
[julienkay/sd-turbo]: https://huggingface.co/julienkay/sd-turbo
[julienkay/FLUX.2-klein-4B-sentis-uint8]: https://huggingface.co/julienkay/FLUX.2-klein-4B-sentis-uint8
