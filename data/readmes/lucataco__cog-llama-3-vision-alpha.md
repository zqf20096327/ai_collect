# qresearch/llama-3-vision-alpha Cog Model

This is an implementation of [qresearch/llama-3-vision-alpha](https://huggingface.co/qresearch/llama-3-vision-alpha) as a [Cog](https://github.com/replicate/cog) model.

## Development

Follow the [model pushing guide](https://replicate.com/docs/guides/push-a-model) to push your own model to [Replicate](https://replicate.com).

## Basic Usage

To run a prediction:

    cog predict -i image=@frieren.jpg -i prompt="Describe the image"


![input](frieren.jpg)

## License

The code in this repository is licensed under the [Apache License 2.0](LICENSE).

The model weights are not covered by this license. The bundled `mm_projector.bin` from [qresearch/llama-3-vision-alpha](https://huggingface.co/qresearch/llama-3-vision-alpha) and the SigLIP vision encoder are Apache 2.0, and the Llama 3 8B Instruct base model is under the [Meta Llama 3 Community License](https://www.llama.com/llama3/license/).
