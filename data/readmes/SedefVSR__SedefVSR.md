# SedefVSR

AI video upscaler for Windows. Turns old or low-resolution footage into sharp
4× super-resolution with a diffusion model that runs fully on your own NVIDIA
GPU — no cloud, your footage never leaves the machine.

![SedefVSR — split compare view](assets/app.PNG)

## Features

- **4× upscaling** — diffusion super-resolution tuned for consumer NVIDIA GPUs
- **Live split compare** — check one upscaled frame against the original before any long render
- **Export queue** — batch several files with live progress, ETA and real fps
- **Pause / resume** — interrupt a render and continue later, even after a restart
- **Trim ranges** — render only the frames you selected on the timeline
- **Modern codecs** — H.265/HEVC · H.264 · AV1 (hardware NVENC encode) · MP4 / MKV / MOV / WebM
- **Images too** — PNG / JPEG / WEBP / BMP / TIFF / DPX / EXR, or export a video render as a frame sequence
- **Smart VRAM management** — adapts chunk sizes to the available graphics memory automatically

## Requirements

| | |
|---|---|
| **OS** | Windows 10 / 11 (64-bit) |
| **GPU** | NVIDIA with 8 GB VRAM or more |
| **Disk** | ~12 GB for the runtime and AI models |

## How it works

Diffusion-based super-resolution with temporal-consistency control (no flicker
between frames), PyAV decoding, hardware NVENC encoding and a Qt6/QML desktop
interface.

## Languages

English · Türkçe · Azərbaycanca · Deutsch · Русский · Français

## Links

- Website: https://sedefvsr.nuhyurdu.com
