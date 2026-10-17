# KawaiiGenerator

## Update
- 03/20/2023: Change repository's name from KawaiiGenerator to senju.

## Overview
KawaiiGenerator enables users to try and compare deep learning tasks related to anime images and videos.

## Showcase

Each category image is a compact collage of the README results for that application group.

### Super Resolution
![](./data/showcases/super_resolution.jpg)

Implementations: [SRGAN](./super_resolution/srgan/README.md), [ESRGAN](./super_resolution/esrgan/README.md), [Residual Attention Module](./super_resolution/ram/README.md)

### Image Style Transfer
![](./data/showcases/image_style_transfer.jpg)

Implementations: [Image Manipulation](./image_manupilation/README.md), [CycleGAN](./image_style_transfer/cycle_gan/README.md), [StarGAN](./image_style_transfer/star_gan/README.md), [RelGAN](./image_style_transfer/rel_gan/README.md), [U-GAT-IT](./image_style_transfer/ugatit/README.md), [InstaGAN](./image_style_transfer/insta_gan/README.md), [AdaIN](./image_style_transfer/ada_in/README.md), [Style Attention Network](./image_style_transfer/style_attention_net/README.md)

### Illustration Generation
![](./data/showcases/illustration_generation.jpg)

Implementations: [DCGAN](./illustration_generator/dcgan/README.md), [DRAGAN](./illustration_generator/dragan/README.md), [Spectral Normalization GAN](./illustration_generator/spectral_norm_gan/README.md), [Relativistic GAN](./illustration_generator/ra_gan/README.md), [SRResNet + DRAGAN](./illustration_generator/sr_res_net_gan/README.md), [Residual Blocks GAN](./illustration_generator/residual_gan/README.md), [RealnessGAN](./illustration_generator/realness_gan/README.md), [BodyGAN](./illustration_generator/body_gan/README.md), [Latent Discovery](./illustration_generator/latent_discovery/README.md)

### Video Processing
![](./data/showcases/video_processing.jpg)

Implementations: [Recycle-GAN](./video_processing/recycle_gan/README.md), [Add Blink](./video_processing/add_blink/README.md). Full animations: [Recycle-GAN](./video_processing/recycle_gan/mtou.gif), [Add Blink](./video_processing/add_blink/cv_generation.gif)

### Character Applications
![](./data/showcases/character_applications.jpg)

Implementations: [Line Extraction](./line_extraction/README.md), [Saekano Character Recognition](./saekano_character_recognition/README.md), [Hair Style Transfer](./hair_style_transfer/README.md)

## GUI Application
![](./data/gui_im.png)

KawaiiGenerator also offers a GUI application that enables users to try applications like the figure above. At present, only `.png` files can be processed.

### Getting Started

#### 0. Download Pre-trained file
You can download pre-trained files for GUI application from [this link](https://github.com/SerialLain3170/KawaiiGenerator/releases/tag/v0.1.0-alpha). After that, you need to move `decoder.pt` and `encoder.pt` to `gui/server/ckpts/`.

#### 1. Docker image preparation
Build docker images via:

```bash
bash build.sh
```

#### 2. Start GUI
Start application via the command below and access `0.0.0.0:5000`. It will take a little time to show the start page.

```bash
docker-compose up -d
```
