# LiteRT-Models

<img src="https://github.com/user-attachments/assets/3c764bf0-32ac-4b65-814b-a73e1aba1cfc" width="100%">

LiteRT is Google's on-device ML runtime for Android and the successor to TensorFlow Lite (renamed 2024-09): PyTorch models are converted with Google's `litert-torch` into `.tflite` files that run every op on the phone's GPU through [`CompiledModel`](https://ai.google.dev/edge/litert) (ML Drift), e.g. DINOv2 ViT-S/14 at 448² runs in 53.6 ms on a Galaxy S26 GPU ([npubench](npubench/), LiteRT 2.2.0, median of 50 runs, 2026-08).

This repository is the model zoo for that path: **91 converted models** (as of 2026-09-08), each with its download, input/output shapes, preprocessing, the conversion script that produced it, and a standalone Android sample app (Kotlin). No MediaPipe and no vendor SDK: the `.tflite` graphs run on `CompiledModel` GPU with every op delegated (no CPU fallback), and the chat models run on LiteRT-LM. The GPU-compatibility rewrites these conversions need are catalogued in [docs/LITERT_CONVERSION_GUIDE.md](docs/LITERT_CONVERSION_GUIDE.md) and packaged in [`litert_gpu_toolkit/`](litert_gpu_toolkit/).

**If you like this repository, please give it a star.**

# Models

| Model | Task | Device | Latency | Download |
| ----- | ---- | ------ | ------- | -------- |
| [YOLO11n](#yolo11n) | Object detection | Pixel 8a | 18+ FPS, live camera | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/yolo11n.tflite) |
| [YOLO26n](#yolo26n) | Object detection |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/yolo26n.tflite) |
| [RF-DETR Nano](#rf-detr-nano) | Object detection (DETR, live camera) | Pixel 8a | ~110 ms/frame (~9 fps) | [🤗 HF](https://huggingface.co/litert-community/RF-DETR-Nano-LiteRT) |
| [RT-DETRv2-S](#rt-detrv2-s) | Object detection (DETR, still image) | Pixel 8a | ~615 ms/frame | [🤗 HF](https://huggingface.co/litert-community/RT-DETRv2-S-LiteRT) |
| [D-FINE-S](#d-fine-s) | Object detection (DETR, still image) |  |  | [🤗 HF](https://huggingface.co/litert-community/D-FINE-S-LiteRT) |
| [SSDLite320 MobileNetV3](#ssdlite320-mobilenetv3) | Object detection | Pixel 8a | ~30 FPS, live camera | [🤗 HF](https://huggingface.co/mlboydaisuke/ssdlite320-mobilenetv3-litert) |
| [YOLO + DeepSORT (OSNet)](#yolo--deepsort-osnet) | Multi-object tracking |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v3/osnet_x0_25.tflite) |
| [MoViNet-A0 (streaming)](#movinet-a0-streaming-kinetics-600) | Video action recognition |  |  | [🤗 HF](https://huggingface.co/litert-community/MoViNet-A0-Stream-LiteRT) |
| [PIDNet-S](#pidnet-s-real-time-cityscapes) | Semantic segmentation (Cityscapes) | Galaxy S26 | 16.20 ms (NPU 5.48) | [🤗 HF](https://huggingface.co/litert-community/PIDNet-S-Cityscapes-LiteRT) |
| [YOLO26n-pose](#yolo26n-pose) | Pose estimation |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/yolo26n_pose.tflite) |
| [RTMPose-s](#rtmpose-s) | Pose estimation (17 keypoints) | Pixel 8a | ~4 ms | [🤗 HF](https://huggingface.co/litert-community/RTMPose-s-LiteRT) |
| [RTMW-m](#rtmw-m-whole-body-133-keypoints) | Whole-body pose (133 keypoints) | Pixel 8a | ~6 ms | [🤗 HF](https://huggingface.co/litert-community/RTMW-m-WholeBody-LiteRT) |
| [RTMPose-Hand](#rtmpose-hand-21-keypoints) | Hand pose (21 keypoints) | Pixel 8a | ~4 ms | [🤗 HF](https://huggingface.co/litert-community/RTMPose-Hand-LiteRT) |
| [RTMPose-Animal](#rtmpose-animal-ap-10k-17-keypoints) | Animal pose (AP-10K) | Pixel 8a | ~5 ms | [🤗 HF](https://huggingface.co/litert-community/RTMPose-Animal-AP10K-LiteRT) |
| [DewarpNet](#dewarpnet) | Document dewarping | Galaxy S26 | 17.64 ms (NPU 4.99) | [🤗 HF](https://huggingface.co/litert-community/DewarpNet-LiteRT) |
| [Ultra-Fast-Lane-Detection](#ultra-fast-lane-detection) | Lane detection | Pixel 8a | ~20 ms | [🤗 HF](https://huggingface.co/litert-community/Ultra-Fast-Lane-Detection-LiteRT) |
| [TwinLiteNet](#twinlitenet) | Drivable area + lanes | Pixel 8a | ~44 ms | [🤗 HF](https://huggingface.co/litert-community/TwinLiteNet-LiteRT) |
| [EDSR (×4)](#edsr-4) | Super-resolution ×4 | Pixel 8a | ~23 ms | [🤗 HF](https://huggingface.co/litert-community/EDSR-x4-LiteRT) |
| [DehazeFormer-MCT](#dehazeformer-mct) | Image dehazing | Pixel 8a | ~255 ms/frame | [🤗 HF](https://huggingface.co/litert-community/DehazeFormer-MCT-LiteRT) |
| [Cloth Segmentation (U²-Net)](#cloth-segmentation-u2net) | Clothing segmentation | Pixel 8a | ~88 ms | [🤗 HF](https://huggingface.co/litert-community/Cloth-Segmentation-U2Net-LiteRT) |
| [U²-Net Portrait](#u2-net-portrait) | Portrait sketch | Pixel 8a | ~12 ms | [🤗 HF](https://huggingface.co/litert-community/U2Net-Portrait-Sketch-LiteRT) |
| [Silent-Face (MiniFASNetV2)](#silent-face-minifasnetv2) | Face liveness / anti-spoofing | Pixel 8a | ~5 ms | [🤗 HF](https://huggingface.co/litert-community/Silent-Face-Anti-Spoofing-LiteRT) |
| [6DRepNet](#6drepnet) | Head pose | Galaxy S26 | 8.18 ms (NPU 1.74) | [🤗 HF](https://huggingface.co/litert-community/6DRepNet-HeadPose-LiteRT) |
| [SINet-V2](#sinet-v2) | Camouflaged object detection | Galaxy S26 | 12.39 ms (NPU 3.08) | [🤗 HF](https://huggingface.co/litert-community/SINet-V2-Camouflage-LiteRT) |
| [DM-Count](#dm-count) | Crowd counting |  |  | [🤗 HF](https://huggingface.co/litert-community/DM-Count-Crowd-LiteRT) |
| [YOLACT-ResNet50](#yolact-resnet50) | Instance segmentation | Pixel 8a | ~41 ms | [🤗 HF](https://huggingface.co/litert-community/YOLACT-ResNet50-LiteRT) |
| [MobileSAM](#mobilesam) | Tap-to-segment (SAM) |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/mobilesam_encoder.tflite) |
| [SAM 2.1 (Hiera-Tiny)](#sam-21-hiera-tiny) | Tap-to-segment (SAM 2.1) | Pixel 8a | 610 ms encoder / 76 ms decoder | [🤗 HF](https://huggingface.co/mlboydaisuke/SAM2-hiera-tiny-LiteRT) |
| [EdgeTAM (SAM2)](#edgetam-sam2) | Tap-to-segment (SAM 2, mobile) | Pixel 8a | ~110–220 ms encoder / ~60 ms decoder | [🤗 HF](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT) |
| [EdgeTAM Video](#edgetam-video-sam2-tracking) | Video object tracking (SAM 2 memory) | Pixel 8a | ~0.45 s/frame | [🤗 HF](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT) |
| [RMBG-1.4 (ISNet)](#rmbg-14-isnet) | Background removal |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/rmbg14.tflite) |
| [ormbg](#ormbg-open-apache-20) | Background removal (Apache-2.0) | Pixel 8a | 246 ms (1024², run + readback) | [🤗 HF](https://huggingface.co/litert-community/ormbg-LiteRT) |
| [DIS (IS-Net)](#dis-is-net-general-use) | High-precision cutout | Galaxy S26 | 72.43 ms (NPU 24.21) | [🤗 HF](https://huggingface.co/litert-community/DIS-ISNet-LiteRT) |
| [MODNet](#modnet-trimap-free) | Portrait matting | Pixel 8a | ~79 ms/frame | [🤗 HF](https://huggingface.co/litert-community/MODNet-LiteRT) |
| [LaMa-Dilated](#lama-dilated) | Inpainting |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/lama_dilated.tflite) |
| [MI-GAN](#mi-gan-mobile-inpainting--object-removal) | Inpainting / object removal | Pixel 8a | ~6 ms (512²) | [🤗 HF](https://huggingface.co/litert-community/MI-GAN-512-Places2-LiteRT) |
| [CLIP ViT-B/32](#clip-vit-b32) | Zero-shot classification |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/clip_image_encoder.tflite) |
| [Places365 ResNet18](#places365-resnet18-scene-recognition) | Scene recognition | Pixel 8a | ~2 ms | [🤗 HF](https://huggingface.co/litert-community/Places365-ResNet18-LiteRT) |
| [DINOv2 ViT-S/14](#dinov2-vit-s14) | Dense features (PCA visualization) | Galaxy S26 | 53.58 ms (NPU 86.00) | [🤗 HF](https://huggingface.co/litert-community/DINOv2-ViT-S14-LiteRT) |
| [DSINE](#dsine) | Surface normal estimation |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/dsine.tflite) |
| [Parakeet (FastConformer-CTC)](#parakeet-fastconformer-ctc) | Speech recognition | Pixel 8a | ~0.4 s per 16 s window | [🤗 HF](https://huggingface.co/litert-community/Parakeet-tdt-ctc-110m-LiteRT) |
| [Whisper-tiny](#whisper-tiny) | Speech recognition |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/whisper_encoder.tflite) |
| [wav2vec2-CTC](#wav2vec2-ctc-fully-gpu-single-pass) | Speech recognition (CTC, single pass) | Pixel 8a | ~22 ms per 10 s clip | [🤗 HF](https://huggingface.co/litert-community/wav2vec2-base-960h-CTC-LiteRT) |
| [Kokoro-82M](#kokoro-82m) | Text-to-speech (EN / JA) | Pixel 8a (CPU) | RTF 0.60 | [🤗 HF](https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/resolve/main/onnx/model_fp16.onnx) |
| [Matcha-TTS](#matcha-tts) | Text-to-speech (FFT-free) | Pixel 8a | RTF ~0.8 | [🤗 HF](https://huggingface.co/litert-community/Matcha-TTS) |
| [Dia2-1B](#dia2-1b-dialogue) | Dialogue text-to-speech | Pixel 8a (CPU) | ~190 s per 4 s utterance | [scripts](dia2/) |
| [VibeVoice-Realtime-0.5B](#vibevoice-realtime-05b) | Streaming text-to-speech |  |  | [scripts](vibevoice/) |
| [Pocket TTS (Kyutai)](#pocket-tts-kyutai) | Text-to-speech (flow-matching LM, GPU) | Pixel 8a | RTF ~1.0 | [🤗 HF](https://huggingface.co/mlboydaisuke/Pocket-TTS-LiteRT) |
| [KittenTTS nano 0.8](#kittentts-nano-08-dynamic-length) | Text-to-speech (dynamic length) |  |  | [scripts](kittentts/) |
| [Inflect-Nano-v2](#inflect-nano-v2-dynamic-length-exact-streaming) | Text-to-speech (exact streaming) | Mac | 25–32 ms first chunk | [scripts](inflect/) |
| [Sopro v2 turbo](#sopro-v2-turbo-zero-shot-voice-cloning) | Text-to-speech (zero-shot voice cloning, EN / PT / FR / DE) | Galaxy S26 GPU (acoustic + encoders) + CPU (AR, vocoder); Pixel 8a pending | TTFA 2.07 s, RTF 0.41 (S26, release) | [🤗 HF](https://huggingface.co/litert-community/sopro-v2-turbo) |
| [Audio8-TTS-Preview-0.6b](audio8_tts/) | Text-to-speech (zero-shot voice cloning, 11 languages) | Galaxy S26 (CPU) | RTF 1.12 on screen, 1.42–1.50 in the device check (2026-10-10) | [🤗 HF](https://huggingface.co/litert-community/Audio8-TTS-Preview-0.6b) |
| [Ming-3.0-tts-0.5B](ming3tts/) | Text-to-speech (7 languages, 44.1 kHz, built-in voices) | Galaxy S26 (GPU + NPU) | 8.9 s of speech in 9.6 s (0.93× real time), first audio after 1.87 s; 1.35× real time with every graph on the NPU, an option in the app (2026-10-27) | [🤗 HF](https://huggingface.co/litert-community/Ming-3.0-tts-0.5B) |
| [SmolVLM-256M](#smolvlm-256m) | Vision-language model |  |  | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/smolvlm_vision.tflite) |
| [SmolVLA](#smolvla-lerobotsmolvla_base) | Vision-language-action robot policy | Galaxy S26 | 207 ms per 50-step action chunk (GPU) | [scripts](smolvla/) |
| [RWKV-7 World 0.1B](#rwkv-7-world-01b) | Text generation (RNN LM, whole forward on GPU) | Pixel 8a | ~18 ms/token | [🤗 HF](https://huggingface.co/litert-community/RWKV-7-World-0.1B-LiteRT) |
| [Whisper + SmolLM2 + Kokoro](#whisper--smollm2--kokoro-pipeline) | Voice assistant pipeline | Pixel 8a | ~5 s per turn, end-to-end | [module](voiceassistant/) |
| [DAC 16kHz](#dac-16khz) | Neural audio codec | Pixel 8a | RTF ≈ 0.82 | [🤗 HF](https://huggingface.co/mlboydaisuke/DAC-16kHz-LiteRT) |
| [Mimi (Kyutai)](#mimi-kyutai-2024) | Neural audio codec (streaming) | Pixel 8a | RTF ≈ 0.35 | [🤗 HF](https://huggingface.co/litert-community/Mimi) |
| [wav2vec2 Keyword Spotting](#wav2vec2-keyword-spotting) | Keyword spotting | Pixel 8a | ~19 ms per 1 s clip | [🤗 HF](https://huggingface.co/litert-community/wav2vec2-keyword-spotting) |
| [PANNs CNN14](#panns-cnn14-audio-tagging) | Audio tagging (AudioSet) | Pixel 8a | ~0.22 s per 10 s clip | [🤗 HF](https://huggingface.co/litert-community) |
| [CREPE](#crepe) | Pitch detection | Pixel 8a | ~75 ms/frame | [🤗 HF](https://huggingface.co/litert-community) |
| [TIGER-DnR](#tiger-dnr-dialog--effects--music) | Audio source separation | Pixel 8a | ~4.5 s per 12.06 s chunk per stem | [🤗 HF](https://huggingface.co/litert-community) |
| [pyannote 3.1 stack](#pyannote-31-stack-segmentation--wespeaker) | Speaker diarization | Pixel 8a | ~1.2 ms per embedding window | [🤗 HF](https://huggingface.co/litert-community) |
| [Nemotron-3-Diarization](#nemotron-3-diarization-streaming-sortformer-8-speakers) | Speaker diarization (streaming, up to 8 speakers) | Galaxy S26 | 171 ms per 0.72 s step (RTF 0.24, FP32) | [🤗 HF](https://huggingface.co/litert-community/Nemotron-3-Diarization-LiteRT) |
| [CMGAN](#cmgan-noise-suppression) | Speech enhancement | Pixel 8a | ~20 ms per 2 s chunk | [🤗 HF](https://huggingface.co/litert-community) |
| [Basic Pitch](#basic-pitch-audio-to-midi) | Music transcription (audio → MIDI) | Pixel 8a | ~4.4 ms per 2 s window | [🤗 HF](https://huggingface.co/litert-community) |
| [XFeat](#xfeat-local-features) | Image matching (local features) | Pixel 8a | ~0.4 ms per 640×480 image | [🤗 HF](https://huggingface.co/litert-community) |
| [CLIPSeg](#clipseg) | Text-prompted segmentation | Pixel 8a | ~8.7 ms text + ~8.2 ms vision | [🤗 HF](https://huggingface.co/litert-community) |
| [RAM++](#ram-recognize-anything-plus) | Image tagging (open vocabulary) | Pixel 8a | ~2 s per photo | [🤗 HF](https://huggingface.co/litert-community) |
| [NIMA](#nima-neural-image-assessment) | Image quality assessment | Pixel 8a | ~173 ms | [🤗 HF](https://huggingface.co/litert-community) |
| [Vision-RWKV (VRWKV-S)](#vision-rwkv-vrwkv-s) | Image classification | Pixel 8a | ~28 ms | [🤗 HF](https://huggingface.co/litert-community/Vision-RWKV-S-LiteRT) |
| [PlantNet-300K](#plantnet-300k-1081-plant-species) | Fine-grained classification (plants) | Galaxy S26 | 3.34 ms (NPU 0.89) | [🤗 HF](https://huggingface.co/litert-community/PlantNet-300K-ResNet18-LiteRT) |
| [3DDFA_V2](#3ddfa_v2-3d-face-alignment) | 3D face alignment |  |  | [🤗 HF](https://huggingface.co/litert-community) |
| [BiSeNet](#bisenet-face-parsing) | Face parsing | Galaxy S26 | 25.05 ms (NPU 7.01) | [🤗 HF](https://huggingface.co/litert-community/BiSeNet-Face-Parsing-LiteRT) |
| [HSEmotion](#hsemotion-facial-emotion-recognition) | Facial emotion recognition | Pixel 8a | ~2 ms | [🤗 HF](https://huggingface.co/litert-community/HSEmotion-B0-LiteRT) |
| [PP-OCRv5](#pp-ocrv5) | OCR | Pixel 8a | ~9 ms detector + ~9 ms recognizer | [🤗 HF](https://huggingface.co/litert-community/PP-OCRv5-LiteRT) |
| [Real-ESRGAN x4v3](#real-esrgan-x4v3) | Super-resolution ×4 | Galaxy S26 | 12.30 ms (NPU 3.29) | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/real_esrgan_x4v3.tflite) |
| [GFPGAN v1.4](#gfpgan-v14-blind-face-restoration) | Blind face restoration |  |  | [🤗 HF](https://huggingface.co/litert-community/GFPGAN-v1.4-LiteRT) |
| [Bonsai Image 4B](bonsai_image/) | Text-to-image (ternary DiT, CPU) | Galaxy S26 (CPU) | 23.5 s per 256×256 image (app, 4 steps, 2026-10-09) | [🤗 HF](https://huggingface.co/litert-community/Bonsai-Image-ternary-4B) |
| [iris-3b Turbo](#iris-3b-turbo) | Text-to-image (pixel-space DiT, GPU) | Galaxy S26 | 212.6 s per 768×768 image (app, 4 steps, first image after the install, 2026-10-21) | [🤗 HF](https://huggingface.co/litert-community/iris-3b-Turbo-LiteRT) |
| [MoGe-2 ViT-S](#moge-2-vit-s) | Monocular geometry (points, normals, depth) | Pixel 8a | ~522 ms | [GitHub](https://github.com/john-rocky/LiteRT-Models/releases/download/v3/moge.tflite) |
| [Depth Anything 3 Small](#depth-anything-3-vit-s-small) | Monocular depth | Pixel 8a | ~1.8 s/image | [🤗 HF](https://huggingface.co/mlboydaisuke/Depth-Anything-3-Small-LiteRT) |
| [Metric3D v2 ViT-S](#metric3d-v2-vit-s) | Metric depth | Pixel 8a | ~44 ms | [🤗 HF](https://huggingface.co/mlboydaisuke/Metric3D-v2-LiteRT) |
| [TIPSv2-B/14 DPT](#tipsv2-b14-dpt-depth-normals-segmentation) | Depth + normals + segmentation | Pixel 8a | ~0.9 s/image | [🤗 HF](https://huggingface.co/litert-community/TIPSv2-B14-DPT-LiteRT) |
| [YuNet](#yunet) | Face detection | Pixel 8a | ~4 ms (640²) | [🤗 HF](https://huggingface.co/litert-community/YuNet-Face-LiteRT) |
| [RTMPose-Face](#rtmpose-face-wflw-98-point-face-alignment) | Face alignment (98 keypoints) | Pixel 8a | ~4 ms | [🤗 HF](https://huggingface.co/litert-community/RTMPose-Face-WFLW-LiteRT) |
| [L2CS-Net](#l2cs-net) | Gaze estimation | Pixel 8a | ~3 ms | [🤗 HF](https://huggingface.co/litert-community/L2CS-Gaze360-LiteRT) |
| [UniSal](#unisal) | Saliency prediction | Pixel 8a | ~3 ms (256²) | [🤗 HF](https://huggingface.co/litert-community/UniSal-Saliency-LiteRT) |
| [M-LSD-tiny](#m-lsd-tiny) | Line detection | Pixel 8a | ~2 ms | [🤗 HF](https://huggingface.co/litert-community/M-LSD-tiny-LiteRT) |
| [Fast Neural Style](#fast-neural-style-4-styles) | Style transfer (4 styles) | Pixel 8a | ~9 ms (256²) | [🤗 HF](https://huggingface.co/litert-community/Fast-Neural-Style-LiteRT) |
| [CPGA-Net](#cpga-net) | Low-light enhancement | Pixel 8a | ~2 ms (256²) | [🤗 HF](https://huggingface.co/litert-community/CPGA-Net-LowLight-LiteRT) |
| [NAFNet](#nafnet-deblur) | Deblur / denoise | Pixel 8a | ~42 ms (256²) | [🤗 HF](https://huggingface.co/litert-community/NAFNet-GoPro-width32-LiteRT) |
| [Qwen3-Embedding-0.6B](#qwen3-embedding-06b) | Text embedding (RAG) | Pixel 8a | ~390 ms per embedding | [🤗 HF](https://huggingface.co/litert-community/Qwen3-Embedding-0.6B-LiteRT) |
| [Qwen3-Reranker-0.6B](#qwen3-reranker-06b) | Text reranking (RAG) |  |  | [🤗 HF](https://huggingface.co/litert-community/Qwen3-Reranker-0.6B-LiteRT) |
| [Laya Multilingual](#laya-multilingual-typed-text-decisions) | Text classification / triage with request-time questions (EN / JA) | Galaxy S26 | 51 ms per question (GPU), 36 ms (NPU) | [🤗 HF](https://huggingface.co/litert-community/Laya-Multilingual-LiteRT) |
| [Laya English + typed-decisions](#laya-multilingual-typed-text-decisions) | English text classification / typed decisions with request-time questions (ModernBERT-large) | Galaxy S26 | 123 ms per question (GPU), 66 ms (NPU) | [🤗 HF](https://huggingface.co/litert-community/Laya-English-LiteRT) |
| [Julia-1](#julia-1-typed-decisions) | Typed decisions: choice / score / yes-no questions about a text (EN) | Galaxy S26 | 82 ms per question (GPU FP32) | [🤗 HF](https://huggingface.co/litert-community/Julia-1-LiteRT) |
| [Open Decision (DeBERTa-v3-large)](#open-decision-deberta-v3-large-typed-decisions) | Typed decisions: choice / score / yes-no questions about a text (EN), one forward pass per request | Galaxy S26 | 697 ms per 512-token request (GPU FP32, 3 questions) | [🤗 HF](https://huggingface.co/litert-community/Open-Decision-DeBERTa-v3-Large-LiteRT) |
| [ModernBERT-Ja-310M Decision](#modernbert-ja-310m-decision-japanese-cross-encoder-typed-decisions) | Japanese typed decisions: choice / score / yes-no questions about a text, one graph call per candidate | Galaxy S26 | 229 ms per 256-token pair (GPU FP32), 42 ms (NPU) | [🤗 HF](https://huggingface.co/mlboydaisuke/ModernBERT-Ja-310M-Decision-LiteRT) |
| [GLiClass-Edge v3.0](#gliclass-edge-v30-zero-shot-text-classification) | Zero-shot text classification (EN): up to 25 labels scored in one forward pass, single- or multi-label | Galaxy S26 | 5.8 ms per request at 128 tokens, 8.3 ms at 256 (GPU FP32) | [🤗 HF](https://huggingface.co/litert-community/GLiClass-Edge-v3.0-LiteRT) |
| [Kev-0.8B](#kev-08b-typed-decisions) | Typed decisions: choice / score / yes-no questions about a text or JSON state, calibrated probabilities (EN) | Galaxy S26 | 102 ms per question at the 128-token window, a 3-question request in 367 ms (GPU); 66 ms and 298 ms (NPU) | [🤗 HF](https://huggingface.co/litert-community/Kev-0.8B-LiteRT) |
| [d1-omni-600M](#d1-omni-600m-typed-decisions-about-text-photos-and-speech) | Typed decisions: yes-no / choice / score questions about a voice note, a photo or a text, a probability for every option | Galaxy S26 | an 8.3 s voice note and 1 question in 153 ms, a photo and 1 question in 211 ms, a text and 2 questions in 96 ms (sample app, GPU; decision graphs at FP32) | [🤗 HF](https://huggingface.co/litert-community/d1-omni-600M-LiteRT) |
| [d1-3B](#d1-3b-typed-decisions-desktop) | Typed decisions: yes-no / choice / score questions about a text, a JSON value or a photo, a probability for every option | Apple M4 Max (Mac, Metal float32) | 3 questions in 153.9 ms, a photo and 1 question in 389.3 ms | [🤗 HF](https://huggingface.co/litert-community/d1-3B-LiteRT) |
| [clef-flash](#clef-flash-typed-decisions-desktop) | Typed decisions: yes-no / choice / score questions about a text, a JSON value or a photo, every question answered at once with a probability for every option | Apple M4 Max (Mac, Metal float32) | a 236-token request in 360.7 ms, a 1,007-token request in 1,346.9 ms, a request with one photo (448 px tile, 688 tokens) in 1,493.8 ms | [🤗 HF](https://huggingface.co/litert-community/clef-flash-LiteRT) |
| [Phocinae-Largha-150M](#phocinae-largha-150m-typed-decisions) | Typed decisions: choice / score / yes-no questions about a text, calibrated probabilities (EN / ZH) | Galaxy S26 | 19.8 ms per question at 384 tokens (NPU), 22.9 ms (GPU FP16); a 3-question request in 114 ms (NPU, the editor) | [🤗 HF](https://huggingface.co/litert-community/Phocinae-Largha-150M-LiteRT) |
| [Timestral-209M](timestral/) | Time-series forecasting: 21 quantiles for up to 1,024 steps of your own series (univariate, context up to 8,192 steps); weights: Mistral AI Modified MIT License (condition 2: no rights if the company's or employer's monthly revenue exceeds $20 million) | Galaxy S26 | 21.1 ms per forecast (NPU), 30.8 ms (GPU FP16), 57.5 ms (CPU int8, 4 threads): a 120-value series, 300-step horizon, median of 10 forecasts in the sample app's debug build | [🤗 HF](https://huggingface.co/mlboydaisuke/Timestral-209M-LiteRT) |
| [WeVisOne-VL-2B](wevisone/) | Cut out what you name in a photo (alpha matte, transparent PNG), plus detection, pointing, counting and reading text, from one 2B vision-language model | Galaxy S26 | 4.7 s (a 640 × 480 picture) and 5.8 s (a 3000 × 2029 photo) from the picture and words to the cut-out (GPU) | [🤗 HF](https://huggingface.co/litert-community/WeVisOne-VL-2B) |
| [Falcon3-3B-Instruct](#falcon3-3b-instruct) | LLM chat (LiteRT-LM) | iPhone 17 Pro | ~27 tok/s | [🤗 HF](https://huggingface.co/mlboydaisuke/Falcon3-3B-Instruct-LiteRT) |
| [Llama-3.2-3B-Instruct](#llama-32-3b-instruct) | LLM chat (LiteRT-LM) | iPhone 17 Pro | ~18.5 tok/s | [🤗 HF](https://huggingface.co/mlboydaisuke/Llama-3.2-3B-Instruct-LiteRT) |
| [Ministral-3-3B-Instruct-2512](#ministral-3-3b-instruct-2512) | LLM chat (LiteRT-LM) | iPhone 17 Pro | ~17.6 tok/s | [🤗 HF](https://huggingface.co/mlboydaisuke/Ministral-3-3B-Instruct-2512-LiteRT) |
| [SmolLM3-3B](#smollm3-3b) | LLM chat (LiteRT-LM) | iPhone 17 Pro | ~22.5 tok/s | [🤗 HF](https://huggingface.co/mlboydaisuke/SmolLM3-3B-LiteRT) |
| [Qwen3.8-27B](#qwen38-27b-mac-chat-app) | LLM chat (LiteRT-LM), a 27B model in a Mac app ([litertlm-chat-mac](litertlm-chat-mac/)) | Apple M4 Max (Mac, GPU) | ~18.4 tok/s | [🤗 HF](https://huggingface.co/litert-community/Qwen3.8-27B) |
| [Qwen3-ASR-1.7B](asr_litertlm/) | Speech recognition, 30 languages (LiteRT-LM) | Galaxy S26 (CPU) | 2.49 s for a 6.4 s clip (RTF 0.39) | [🤗 HF](https://huggingface.co/litert-community/Qwen3-ASR-1.7B) |
| [Qwen3-ASR-1.7B-15s](asr_litertlm/) | Speech recognition, 30 languages, the same weights with a 15 s encoder window (LiteRT-LM) | Galaxy S26 (CPU) | 1.79 s for a 6.4 s clip (RTF 0.28) | [🤗 HF](https://huggingface.co/litert-community/Qwen3-ASR-1.7B) |
| [Fun-ASR-Nano-2512](asr_litertlm/) | Speech recognition, zh / en / ja (LiteRT-LM) | Galaxy S26 (CPU) | 1.19 s for a 6.4 s clip (RTF 0.19) | [🤗 HF](https://huggingface.co/litert-community/Fun-ASR-Nano-2512) |
| [Confucius4-R2T2](asr_litertlm/) | Speech recognition, zh / en, a Qwen3-ASR-1.7B fine-tune (LiteRT-LM) | Galaxy S26 (CPU) | 2.59 s for a 6.4 s clip (RTF 0.40) | [🤗 HF](https://huggingface.co/mlboydaisuke/Confucius4-R2T2-LiteRT) |

Latency is the figure each model's section below records, on the device named; blank means this repository records no measurement. **Galaxy S26** rows (Snapdragon 8 Elite Gen 5) come from [npubench](npubench/): LiteRT 2.2.0 `CompiledModel` GPU, median of 50 runs after warm-up, `run()` plus output readback, thermal status NONE, 2026-08; the value in parentheses is the same phone's Hexagon NPU. 50 models were measured that way — see [Snapdragon NPU](#snapdragon-npu-hexagon). The Galaxy S26 (CPU) rows dated 2026-10 (Qwen3-ASR-1.7B, Fun-ASR-Nano-2512, Confucius4-R2T2, Bonsai Image 4B, Audio8-TTS-Preview-0.6b), the Galaxy S26 GPU row of iris-3b Turbo and the Galaxy S26 GPU + NPU row of Ming-3.0-tts-0.5B are instead the sample apps' own device checks on the same phone, as their sections say. **Pixel 8a** (Tensor G3, Mali GPU, fp16) figures marked `~` come from each model's conversion notes; per [docs § Latency figures](docs/LITERT_CONVERSION_GUIDE.md#latency-figures-time-run--readback), figures recorded before 2026-08 may time only the asynchronous `run()` call (ormbg's earlier "~10 ms" re-measured at 246 ms with the readback). Camera FPS, RTF, tok/s and per-turn figures are end-to-end app measurements. The Model column links to the full entry: I/O shapes, preprocessing, license, conversion script and sample app.

# Run a model in 5 lines

Gradle: `implementation("com.google.ai.edge.litert:litert:2.1.3")` (Google Maven). Put the `.tflite` in `app/src/main/assets/`, then:

```kotlin
val model = CompiledModel.create(context.assets, "model.tflite", CompiledModel.Options(Accelerator.GPU), null)
val inputs = model.createInputBuffers()
inputs[0].writeFloat(floatArray)     // preprocessed as the model's entry says (layout, mean/std)
val outputs = model.run(inputs)
val result = outputs[0].readFloat()  // readFloat() waits for the GPU: time run() + readFloat() together
```

Models over ~150 MB load from a file path instead of the APK: `CompiledModel.create(path, options, null)` — see [How to use](#how-to-use) and each module's `install_to_device.sh`.

# How to use

1. Download the `.tflite` model from the GitHub Release link below.
2. Place it in your app's `assets/` directory.
3. Use the `CompiledModel` API with `Accelerator.GPU` to load and run inference.

```kotlin
val options = CompiledModel.Options(Accelerator.GPU)
val model = CompiledModel.create(context.assets, "model.tflite", options, null)
val inputBuffers = model.createInputBuffers()

// Write input data
inputBuffers[0].writeFloat(floatArray)

// Run inference
val outputBuffers = model.run(inputBuffers)
val result = outputBuffers[0].readFloat()
```

**Dependency** (build.gradle.kts):
```kotlin
implementation("com.google.ai.edge.litert:litert:2.1.3")
```

## LiteRT or TensorFlow Lite? The names

LiteRT is TensorFlow Lite renamed (2024-09-04). The `.tflite` format and the models did not change; the coordinates did. Verified 2026-09-05:

| Old name | New name | Note |
|---|---|---|
| `org.tensorflow:tensorflow-lite` (last 2.17.0) | `com.google.ai.edge.litert:litert` 2.2.0 — Google Maven, not Maven Central | `Interpreter` + `CompiledModel`, minSdk 23; the 1.4.x line is `Interpreter`-only, minSdk 21 |
| `org.tensorflow:tensorflow-lite-gpu` + `GpuDelegate` | nothing extra on 2.x: `CompiledModel.Options(Accelerator.GPU)` | `litert-gpu` stops at 1.4.2 |
| `NnApiDelegate` / Qualcomm `qnn-litert-delegate` | `Accelerator.NPU` on `CompiledModel` | NNAPI is deprecated from Android 15 |
| `pip install tflite-runtime` (last release 2023, wheels to Python 3.11) | `pip install ai-edge-litert` (cp310–cp314) | `ai_edge_litert.interpreter.Interpreter`, `ai_edge_litert.compiled_model.CompiledModel` |
| `pip install ai-edge-torch` | `pip install litert-torch` (`litert_torch.convert(model, sample_inputs)`) | every model in this zoo was converted with it |
| MediaPipe LLM Inference API | LiteRT-LM (`com.google.ai.edge.litertlm:litertlm-android` 0.16.1) | MediaPipe LLM Inference is maintenance-only |

Two `CompiledModel` GPU rules: every op in the graph must be GPU-compatible (no CPU fallback), and tensors are rank 4 at most. Full mapping with sources: [docs/LITERT_CONVERSION_GUIDE.md § Three PyTorch → Android routes](docs/LITERT_CONVERSION_GUIDE.md#three-pytorch--android-routes-on-one-model-measured-2026-09-05) <!-- TODO(lane B, articles): replace this in-repo anchor with the published article URL -->

## Shared components

Utilities that recur across the sample apps live as canonical sources in
[`common/`](common/README.md) (Kotlin: `CompiledModelRunner`, `ImageTensor`,
`RealtimeCameraPipeline`, `AudioCapture`, `MathOps`). Each app keeps a vendored
copy so it stays standalone; `python tools/sync_common.py --check` keeps the
copies identical to the canonical.

On the conversion side, the GPU-compatibility patches (fp16-safe norms,
zero-stuff ConvTranspose, zero-pad MaxPool, GELU rewrites, …) are packaged in
[`litert_gpu_toolkit/`](docs/LITERT_CONVERSION_GUIDE.md#litert_gpu_toolkit--canonical-patch-catalog)
— import them instead of re-implementing per script.

# Projects using these models and recipes

- [PocketTTS-LiteRT](https://github.com/geneing/PocketTTS-LiteRT) — Pocket TTS (Kyutai) on Android with LiteRT. It was extracted from its author's fork of this repository and builds on the [`pockettts/`](pockettts/) module, the shared Kotlin helpers under [`common/`](common/README.md), and the conversion recipes ([README](https://github.com/geneing/PocketTTS-LiteRT/blob/2dba83888706fb52339767670a36ef22348aecd4/README.md#acknowledgements)). Its author added an int8 flow-LM, an NPU path for the Mimi decoder transformer on Tensor G5, and their own Pixel 10 measurements on CPU, GPU, and NPU ([results](https://github.com/geneing/PocketTTS-LiteRT/blob/2dba83888706fb52339767670a36ef22348aecd4/docs/RESULTS.md)).
- [dpm](https://github.com/OliverHenrichs/dpm) — a tool for dancers to map the patterns they know. Its video-anonymization module adapts this repository's EdgeTAM video tracker ([`edgetam-video/`](edgetam-video/)) and its conversion script to track several objects ([source](https://github.com/OliverHenrichs/dpm/blob/e7f800b0efe02b909ef2ca3f74179c6ff746625a/modules/video-anonymize/android/src/main/java/expo/modules/videoanonymize/EdgeTamTracker.kt)).
- [ImageSplitter](https://github.com/mozico-565/ImageSplitter) — an Android app that splits a photo into numbered parts for large prints. Its build downloads `real_esrgan_x4v3.tflite` from this repository's `v1` release, and its `AiUpscaler` runs the model to upscale images ([source](https://github.com/mozico-565/ImageSplitter/blob/98325b1b03788d0b102932336c181a7a9e4f4a13/app/build.gradle#L35-L50)).

# Object Detection

### YOLO11n

YOLO11: Ultralytics latest YOLO with improved backbone and neck architecture. Pure CNN — runs at **18+ FPS** on Pixel 8a GPU via CompiledModel.

Converted from SavedModel to eliminate GPU-incompatible ops (PACK/SPLIT).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [yolo11n.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/yolo11n.tflite) | 10 MB | Float32 [1, 384, 384, 3] NHWC | Float32 [1, 84, 3024] | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | [AGPL-3.0](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) | [yolo/](yolo/) |

**Output format**: `[1, 84, N]` — 84 = 4 bbox (cx, cy, w, h normalized 0-1) + 80 COCO class scores (sigmoid). Requires NMS post-processing.

**Preprocessing**: RGB normalized to 0-1 (divide by 255). No ImageNet mean/std.

### YOLO26n

YOLO26: Edge-first vision AI with NMS-free end-to-end detection. Up to 43% faster CPU inference vs YOLO11 with DFL removal and ProgLoss.

Original model outputs `[1, 300, 6]` (NMS-free with top-k), but top-k uses GPU-incompatible ops (TOPK_V2, GATHER). Reconverted with top-k removed — raw output matches YOLO11 format.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [yolo26n.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/yolo26n.tflite) | 9.3 MB | Float32 [1, 384, 384, 3] NHWC | Float32 [1, 84, 3024] | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | [AGPL-3.0](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) | [yolo/](yolo/) |

**Output format**: Same as YOLO11n — `[1, 84, N]` with NMS post-processing in app. Bbox coords are normalized 0-1.

**Preprocessing**: RGB normalized to 0-1 (divide by 255). No ImageNet mean/std.

### RF-DETR Nano

RF-DETR (Roboflow 2025, an LW-DETR derivative): a **transformer** detector (windowed DINOv2 backbone +
deformable-attention DETR decoder) running **fully on CompiledModel GPU** — the first transformer/DETR
detector in this zoo to do so. Converted with **litert-torch** + a **2-graph split** (the two-stage
query selection `TOPK`/`GATHER` runs on the host between the graphs) + **SafeLayerNorm** (the projector
and decoder LayerNorms overflow Mali fp16). Device-verified on Pixel 8a: both graphs fully `LITERT_CL`
(Graph A `1381/1381`, Graph B `404/404`); runs **live camera at ~9 fps (~110 ms/frame)** — a transformer
detector entirely on the GPU — and reproduces the PyTorch detections at IoU 0.98–0.99.

| Model | Size (fp16) | Input | Outputs | Original Project | License | Sample App |
| ----- | ----------- | ----- | ------- | ---------------- | ------- | ---------- |
| RF-DETR-Nano (Graph A + Graph B) | 48.6 MB + 7.6 MB | Float32 [1, 3, 384, 384] NCHW | enc_class[1,576,91] / enc_coord[1,576,4] / memory[1,576,256] → boxes[1,300,4] / logits[1,300,91] | [roboflow/rf-detr](https://github.com/roboflow/rf-detr) | [Apache-2.0](https://github.com/roboflow/rf-detr/blob/main/LICENSE) | [rfdetr/](rfdetr/) |

**Output format**: Graph B gives `boxes` (cxcywh, normalized 0-1) + `logits` (91 = COCO id space). Host
applies sigmoid + score threshold + cxcywh→xyxy + per-class NMS.

**Preprocessing**: square resize to 384×384, RGB, ImageNet mean/std normalization. See
[litert-community/RF-DETR-Nano-LiteRT](https://huggingface.co/litert-community/RF-DETR-Nano-LiteRT).

### RT-DETRv2-S

RT-DETRv2 (Baidu 2024, `PekingU/rtdetr_v2_r18vd`): a real-time **transformer** detector (ResNet18-vd
backbone + hybrid AIFI/CCFM encoder + plain deformable-attention DETR decoder) running **fully on
CompiledModel GPU**. Converted with **litert-torch** + a **2-graph split** (two-stage `TOPK`/`GATHER` on
the host). The on-device gate here was **not** an fp16 wall but a Mali bug where a 3D *token* tensor
`[1,N,256]` that fans out inside the graph is silently corrupted — fixed by emitting only the two clean
leaves (`enc_class` + `memory_raw`) and moving the per-token tail (`enc_output` + box head) to the host
on the 300 selected tokens (exact, since per-token ops commute with gather). Device-verified on Pixel 8a:
both graphs fully `LITERT_CL` (Graph B `704/704`); reproduces the PyTorch detections at IoU 0.98–1.00
(COCO val giraffe 7/7, cats 6/6). **Still-image** demo — RT-DETR's 8400-token / 80×80 deformable decoder
is ~350 ms of GPU compute (GATHER-free tent-matmul), so ~615 ms/frame, not real-time.

| Model | Size (fp16) | Input | Outputs | Original Project | License | Sample App |
| ----- | ----------- | ----- | ------- | ---------------- | ------- | ---------- |
| RT-DETRv2-S (Graph A + Graph B) | 33.8 MB + 7.7 MB | Float32 [1, 3, 640, 640] NCHW | enc_class[1,8400,80] / memory_raw[1,8400,256] → boxes[1,300,4] / logits[1,300,80] | [lyuwenyu/RT-DETR](https://github.com/lyuwenyu/RT-DETR) | [Apache-2.0](https://github.com/lyuwenyu/RT-DETR/blob/main/LICENSE) | [rtdetr/](rtdetr/) |

**Output format**: Graph B gives `boxes` (cxcywh, normalized 0-1) + `logits` (80 = contiguous COCO id
0–79). Host applies sigmoid + score threshold + cxcywh→xyxy + light NMS.

**Preprocessing**: square resize to 640×640, RGB, [0,1] rescale only (no ImageNet normalization). See
[litert-community/RT-DETRv2-S-LiteRT](https://huggingface.co/litert-community/RT-DETRv2-S-LiteRT).

### D-FINE-S

D-FINE (USTC 2024, `ustc-community/dfine-small-coco`) — the **SOTA real-time DETR** — running **fully on
CompiledModel GPU**. HGNetV2 backbone + hybrid AIFI/CCFM encoder + an **FDR** (Fine-grained Distribution
Refinement) decoder. Converted with **litert-torch** + the same **2-graph split** as RT-DETRv2 (host topk +
per-token tail). D-FINE was previously **parked** as a "FDR decoder fp16 wall" — but that was a misdiagnosis:
the real cause was the same Mali 3D-token fan-out bug (the raw `memory` output was silently garbage), and
with clean memory the FDR decoder is perfect. Device-verified on Pixel 8a: Graph A `511/511` + Graph B
`850/850` LITERT_CL, real-image detections at IoU 0.99–1.00 (still-image; deformable decoder GPU-compute-bound).

| Model | Size (fp16) | Input | Outputs | Original Project | License | Sample App |
| ----- | ----------- | ----- | ------- | ---------------- | ------- | ---------- |
| D-FINE-S (Graph A + Graph B) | 13.0 MB + 8.8 MB | Float32 [1, 3, 640, 640] NCHW | enc_class[1,8400,80] / memory_raw[1,8400,256] → boxes[1,300,4] / logits[1,300,80] | [Peterande/D-FINE](https://github.com/Peterande/D-FINE) | [Apache-2.0](https://github.com/Peterande/D-FINE/blob/main/LICENSE) | [dfine/](dfine/) |

**Output format**: Graph B gives `boxes` (cxcywh, normalized 0-1) + `logits` (80 = contiguous COCO id
0–79). Host applies sigmoid + score threshold + cxcywh→xyxy + light NMS.

**Preprocessing**: square resize to 640×640, RGB, [0,1] rescale only (no ImageNet normalization). See
[litert-community/D-FINE-S-LiteRT](https://huggingface.co/litert-community/D-FINE-S-LiteRT).

### SSDLite320 MobileNetV3

![SSDLite320-MobileNetV3 object detection on-device (LiteRT GPU, Pixel 8a)](https://huggingface.co/mlboydaisuke/ssdlite320-mobilenetv3-litert/resolve/main/samples/demo.jpg)

Lightweight (**0.59 GMACs**) single-shot detector — torchvision's SSDLite320-MobileNetV3-Large. **BSD-3** (permissive, unlike the AGPL YOLO family) and converts **patch-free** through litert-torch, the clean path for official LiteRT samples.

The model's built-in postprocess (DefaultBoxGenerator + NMS) lowers to GPU-incompatible `GATHER_ND`/`TOPK`/`>4D`, so the export taps each feature level's **raw 4D head conv outputs** (NCHW) and moves anchor decode + multiclass NMS to Kotlin — no model-internal op rewrite (same technique as the YOLOX raw-head / U²-Net `d0` samples). Keeping **NCHW** I/O (no `to_channel_last_io`) also avoids the channel-last × MobileNetV3 SqueezeExcitation `GATHER_ND` blow-up, so it converts stock-clean.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [HF: mlboydaisuke/ssdlite320-mobilenetv3-litert](https://huggingface.co/mlboydaisuke/ssdlite320-mobilenetv3-litert) (or [reproduce](ssdlite/scripts/convert_ssdlite.py)) | 7.2 MB FP16 | Float32 [1, 3, 320, 320] NCHW | 12× raw head: cls `[1, 546, H, W]` + box `[1, 24, H, W]` per level (H = 20,10,5,3,2,1) | [pytorch/vision](https://github.com/pytorch/vision) | [BSD-3](https://github.com/pytorch/vision/blob/main/LICENSE) | [ssdlite/](ssdlite/) |

**Output format**: 6 feature levels × {classification, box regression}. 6 anchors/location, 91 classes (COCO 90 + background). Decode in Kotlin mirrors torchvision `SSD.postprocess_detections` + `BoxCoder(10,10,5,5)`: softmax → best non-background class → threshold → default-box decode → per-class NMS. Verified **298/300 boxes @ IoU 0.99** vs stock torchvision on the FP16 tflite.

**Preprocessing**: RGB, NCHW, normalized `pixel/127.5 - 1` → `[-1, 1]` (mean = std = 0.5, **not** ImageNet); bilinear stretch-resize to 320×320.

**GPU compatibility**: BANNED NONE, Flex/Custom NONE, max tensor ndim 4, 0 dynamic dims (ops include `SUM×8` = SqueezeExcitation global pools, `TRANSPOSE×11`). **On-device verified (Pixel 8a, Tensor G3)**: CompiledModel GPU delegates all 286 graph nodes to OpenCL (`LITERT_CL`, 1 partition, no CPU fallback) and runs the live camera at **~30 FPS** with correct detections.

**Conversion**: `ssdlite/scripts/convert_ssdlite.py` (litert-torch, 4D-head-tap, FP16 `float_casting`) + `ssdlite/scripts/validate_decode.py` (decode parity vs torchvision).


# Multi-Object Tracking

### YOLO + DeepSORT (OSNet)

<img src="https://github.com/user-attachments/assets/d4cacaa1-da30-49f4-8e63-9789ee5bd1a7" width="300">

| | |
|---|---|
| **Module** | [`yolo-tracking/`](yolo-tracking/) |
| **Detection** | YOLO11n — 384×384, 10 MB |
| **Re-ID** | OSNet x0.25 — 256×128 → 512-dim embedding, ~1.4 MB |
| **Tracker** | DeepSORT (Kalman + Hungarian + cascade matching) |
| **Pipeline** | YOLO detect → OSNet Re-ID per crop → DeepSORT track |

Real-time multi-object tracking with appearance-based re-identification. YOLO11n detects objects, OSNet x0.25 extracts 512-dim appearance embeddings from each detection crop, and DeepSORT maintains track identities using cosine similarity on embeddings gated by Mahalanobis distance from Kalman-predicted positions.

Both ML models run on **CompiledModel GPU**. The tracker logic (Kalman filter, Hungarian algorithm, cascade matching) runs in Kotlin on CPU.

| Model | Download Link | Size | Input | Output | Original Project | License |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- |
| YOLO11n | [yolo11n.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/yolo11n.tflite) | 10 MB | Float32 [1, 384, 384, 3] NHWC | Float32 [1, 84, 3024] | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | AGPL-3.0 |
| OSNet x0.25 | [osnet_x0_25.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v3/osnet_x0_25.tflite) | 867 KB | Float32 [1, 3, 256, 128] NCHW | Float32 [1, 512] | [KaiyangZhou/deep-person-reid](https://github.com/KaiyangZhou/deep-person-reid) | [MIT](https://github.com/KaiyangZhou/deep-person-reid/blob/master/LICENSE) |

**Preprocessing**: YOLO — RGB 0-1. OSNet — RGB with ImageNet normalization (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), NCHW layout.

**Conversion**: `yolo-tracking/scripts/convert_osnet.py` — uses `litert_gpu_toolkit.convert_for_gpu()`. OSNet is a pure CNN, no special GPU patches needed.

# Video Action Recognition

### MoViNet-A0 (streaming, Kinetics-600)

The first **video-input** model in this zoo: it recognises *actions* across a stream of camera frames (not a single image), one frame at a time, with constant memory. [MoViNet-A0](https://arxiv.org/abs/2103.11511) streaming variant (Google Research), trained on **Kinetics-600** (600 action classes), running **fully on CompiledModel GPU**.

MoViNet is a causal 3D CNN whose temporal convolutions and global-average-pools each keep a small buffer of the recent past, so it can be fed one frame at a time and sharpens its prediction as more frames of the same action arrive. The stock streaming graph carries that history in **5D** state tensors `[1, T, H, W, C]`, which the GPU delegate cannot compile (all tensors must be ≤4D). So the model is re-authored as a **single-frame, 4D-only functional forward** with every recurrent buffer threaded explicitly through the graph I/O.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| MoViNet-A0 stream | [movinet_a0_stream.tflite](https://huggingface.co/litert-community/MoViNet-A0-Stream-LiteRT) | 15 MB | frame [1, 3, 172, 172] NCHW + 46 state tensors | logits [1, 600] + 27 state tensors | [Atze00/MoViNet-pytorch](https://github.com/Atze00/MoViNet-pytorch) ([google-research/movinet](https://github.com/tensorflow/models/tree/master/official/projects/movinet)) | [Apache-2.0](https://github.com/Atze00/MoViNet-pytorch/blob/main/LICENSE) | [movinet/](movinet/) |

**I/O** (47 inputs / 28 outputs) — `input[0]` = current RGB frame (NCHW, 0..1); `input[1..28]` = 28 temporal-conv stream buffers `[1,C,H,W]`; `input[29..44]` = 16 streaming avg-pool running sums `[1,C,1,1]`; `input[45]` = `inv_count` (1/frame-number); `input[46]` = constant `1.0`. `output[0]` = Kinetics-600 logits; `output[1..11]` = current per-conv frames; `output[12..27]` = fresh per-frame means. The **stream-buffer shift register and pool running-sum accumulation are done host-side** — the graph consumes recurrent state but only emits fresh tensors.

**Conversion** (`movinet/scripts/build_movinet.py`, litert-torch): temporal depthwise convs (kernel 3/5 over the stream buffer) become a per-channel weighted sum of the buffered frames; streaming pools become `avg = (running_sum + mean) * inv_count`; the tf-`same` residual average pool is reformulated as `count_include_pad=True` + a constant boundary-correction mask so it lowers to `AVERAGE_POOL_2D + MUL`. Result: **all float32, 0 tensors of rank > 4, 0 banned ops, 0 composites** — matches the original PyTorch model bit-for-bit (corr 0.99999999999). Keeping the recurrent state in-graph tripped three silent Mali `CompiledModel` bugs (input-passed-through-to-output loses its compute use; a `state + tensor` output reads zero; a conv output that is both consumed and emitted has its emitted copy corrupted ~2.5× → fp16 blow-up over frames), so all state plumbing is host-side and each emitted stream frame is decoupled from its compute use by a multiply against the runtime `1.0` input. Device GPU (Pixel 8a) locks onto "jumping jacks" within a few frames.

**Sample app**: [movinet/](movinet/) — live camera → per-frame inference → top-5 Kinetics-600 action bars. Tap to restart the classification window.

# Semantic Segmentation

### PIDNet-S (real-time, Cityscapes)

Real-time **semantic segmentation** running fully on the LiteRT `CompiledModel` GPU. [PIDNet-S](https://arxiv.org/abs/2206.02066) (CVPR 2023) segments a road scene into the **19 Cityscapes classes** (road, sidewalk, building, car, person, sky, …) at ~17 FPS on a Pixel 8a. PIDNet is a three-branch CNN (P: detail, I: context, D: boundary) — a **pure CNN that converts to a fully GPU-compatible graph with zero patches**.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| PIDNet-S | [pidnet_s.tflite](https://huggingface.co/litert-community/PIDNet-S-Cityscapes-LiteRT) | 30 MB | Float32 [1, 3, 1024, 1024] NCHW (ImageNet-norm) | Float32 [1, 19, 128, 128] logits | [XuJiacong/PIDNet](https://github.com/XuJiacong/PIDNet) | [MIT](https://github.com/XuJiacong/PIDNet/blob/main/LICENSE) | [pidnet/](pidnet/) |

**Preprocessing**: RGB, resize to 1024×1024, ImageNet normalization (mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225]), NCHW. **Postprocessing**: argmax over the 19 channels per pixel → Cityscapes-colored label map (1/8 res) → upscale.

**Conversion** (`pidnet/scripts/build_pidnet.py`, litert-torch): PIDNet has no attention, no dynamic shapes at a fixed input, and `align_corners=False` on every bilinear resize, so it converts with **zero GPU patches** — `CONV_2D` ×75, `RESIZE_BILINEAR` ×11, `AVERAGE_POOL_2D`, `ADD`/`MUL`/`SUB`/`SUM`, `LOGISTIC`; **0 tensors of rank > 4, 0 banned ops**. CPU-exact vs PyTorch (corr 0.99999999999, 100% argmax); device Mali GPU (fp16) agrees at 97% of pixels with correct classes (~59 ms/frame at 1024²). The trained weights are loaded from an ONNX mirror whose initializer names match the original repo's PyTorch keys.

**Sample app**: [pidnet/](pidnet/) — live camera → PIDNet-S GPU → Cityscapes-colored segmentation overlay.

# Pose Estimation

### YOLO26n-pose

<img src=https://github.com/user-attachments/assets/55e864bc-5e26-4025-a814-a6fcd5683a4d width=300>

Real-time human pose estimation with Ultralytics YOLO26n-pose. 17 COCO keypoints + skeleton overlay, runs on CompiledModel GPU. Three input modes in the sample app: live camera, picked image, picked video — all share the same pose decoder.

Converted via **litert-torch** by wrapping the head with `end2end=False, export=True, format='tflite'`. This bypasses the default end-to-end NMS-free path (which compiles to GPU-incompatible `TOPK_V2`/`GATHER`) and exposes the legacy one-to-many head output. Ultralytics' default ONNX → onnx2tf path breaks on the YOLO26 backbone (`model.2/m.0/Add` channel mismatch), so the conversion goes PyTorch → litert-torch directly, the same path used for MobileSAM, RMBG, and DSINE in this repo.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [yolo26n_pose.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/yolo26n_pose.tflite) | 12 MB | Float32 [1, 3, 384, 384] NCHW | Float32 [1, 56, 3024] | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | [AGPL-3.0](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) | [yolo-pose/](yolo-pose/) |

**Output format**: `[1, 56, N]` — `4 bbox (cx, cy, w, h) + 1 person conf + 17 keypoints * 3 (x, y, vis)`. Bbox is YOLO **xywh center format** (the legacy one-to-many head emits xywh, not xyxy). Bbox and keypoint xy values are in input image pixel space (0..384); person confidence and per-keypoint visibility are sigmoid-activated (0..1). Requires NMS post-processing.

**Preprocessing**: RGB normalized to 0-1 (divide by 255), planar NCHW layout. No ImageNet mean/std.

**Sample app**: [yolo-pose/](yolo-pose/) — Camera / Image / Video mode toggle, skeleton overlay matching either FILL_CENTER (camera) or FIT_CENTER (image/video).

### RTMPose-s

RTMPose-s (mmpose, CSPNeXt + RTMCC/SimCC head): the SOTA real-time **top-down** 2D human pose model — 17 COCO keypoints for a centered person — running **fully on the GPU** (`256/256` LITERT_CL on a Pixel 8a, **~4 ms**, fp16 **11.1 MB**). Apache-2.0 (vs the YOLO pose model's AGPL), device-vs-PyTorch SimCC corr **0.999**, keypoints within **0.3 px**.

Converted via **litert-torch** with two numerically-exact, on-device-only re-authorings (both pass the desktop op-check yet were needed for a correct Mali result — *residency ≠ correctness*): (1) the RTMCC **`ScaleNorm` (RMS)** input reaches ≈|274| so its `Σx²`≈3.6M **overflows fp16** on Mali → `norm=∞` → all-zero head; fixed by scaling `x` down before squaring (same class as the NAFNet SafeLayerNorm). (2) The GAU attention **`act@act` BMM** → broadcast-multiply + reduce-sum (K=17 tokens).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [rtmpose_s_fp16.tflite](https://huggingface.co/litert-community/RTMPose-s-LiteRT) | 11.1 MB | Float32 [1, 3, 256, 192] NCHW | simcc_x [1,17,384], simcc_y [1,17,512] | [open-mmlab/mmpose](https://github.com/open-mmlab/mmpose) | [Apache-2.0](https://github.com/open-mmlab/mmpose/blob/main/LICENSE) | [rtmpose/](rtmpose/) |

**Output format**: two 1D SimCC distributions per keypoint; argmax over the bins (÷ split=2) → pixel x/y. **Preprocessing**: center-crop to 3:4, resize 192×256, ImageNet 0-255 normalize, NCHW. Top-down (one centered person).

**Sample app**: [rtmpose/](rtmpose/) — image picker + COCO skeleton overlay.


### RTMW-m (whole-body, 133 keypoints)

RTMW-m (mmpose, CSPNeXt + CSPNeXtPAFPN neck + RTMW/SimCC head): **whole-body** 2D pose — **133 COCO-WholeBody keypoints** (17 body + 6 feet + 68 face + 42 hands) for a centered person. The model ControlNet/animation pipelines use. Runs **fully on the GPU** (`531/531` LITERT_CL on a Pixel 8a, **~6 ms**, fp16 **66 MB**), device-vs-PyTorch SimCC corr **0.999**, keypoints within **0.2 px**.

Converted via **litert-torch** with the RTMPose-family re-authorings (SafeRMSNorm for the `ScaleNorm` fp16 overflow + GAU `act@act` BMM → broadcast-reduce) **plus** `nn.PixelShuffle` → depth-to-space `ZeroStuffConvT2d` (the RTMW head's PixelShuffle upsample lowers to a 6D tensor; the fixed depth-to-space `ConvTranspose2d` keeps it 4D — reused from NAFNet/Metric3D).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [rtmw_fp16.tflite](https://huggingface.co/litert-community/RTMW-m-WholeBody-LiteRT) | 66 MB | Float32 [1, 3, 256, 192] NCHW | simcc_x [1,133,384], simcc_y [1,133,512] | [open-mmlab/mmpose](https://github.com/open-mmlab/mmpose) | [Apache-2.0](https://github.com/open-mmlab/mmpose/blob/main/LICENSE) | [rtmw/](rtmw/) |

**Sample app**: [rtmw/](rtmw/) — image picker + whole-body skeleton (body/feet/face/hands color-coded).


### RTMPose-Hand (21 keypoints)

RTMPose-m hand (mmpose, CSPNeXt + RTMCC/SimCC head): **hand** pose — the **21 standard hand keypoints** (wrist + 4 joints × 5 fingers) for a centered hand. Runs **fully on the GPU** (`333/333` LITERT_CL on a Pixel 8a, **~4 ms**, fp16 **28 MB**), device-vs-PyTorch SimCC corr **0.999**. Same RTMPose-family re-authorings as the body model (no PixelShuffle — no neck).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [rtmhand_fp16.tflite](https://huggingface.co/litert-community/RTMPose-Hand-LiteRT) | 28 MB | Float32 [1, 3, 256, 256] NCHW | simcc_x [1,21,512], simcc_y [1,21,512] | [open-mmlab/mmpose](https://github.com/open-mmlab/mmpose) | [Apache-2.0](https://github.com/open-mmlab/mmpose/blob/main/LICENSE) | [rtmhand/](rtmhand/) |

**Sample app**: [rtmhand/](rtmhand/) — image picker + 21-keypoint hand skeleton (per-finger color).


### RTMPose-Animal (AP-10K, 17 keypoints)

[RTMPose](https://github.com/open-mmlab/mmpose) (mmpose, Apache-2.0) **animal pose** trained on **AP-10K**: 17 animal keypoints (eyes, nose, neck, tail root, and the four limbs) for pets / wildlife. The **same model family** as RTMPose-s above — only the config/checkpoint change to AP-10K, and the two on-device Mali fixes (SafeRMSNorm + GAU broadcast-reduce) transfer **unchanged**. Runs **fully on the GPU** (`333/333` LITERT_CL on a Pixel 8a, **~5 ms**, device-vs-PyTorch SimCC corr **0.999**, 17/17 keypoints).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [rtm_animal_fp16.tflite](https://huggingface.co/litert-community/RTMPose-Animal-AP10K-LiteRT) | 27.5 MB | Float32 [1, 3, 256, 256] NCHW | simcc_x [1,17,512], simcc_y [1,17,512] | [open-mmlab/mmpose](https://github.com/open-mmlab/mmpose) | [Apache-2.0](https://github.com/open-mmlab/mmpose/blob/main/LICENSE) | [rtmanimal/](rtmanimal/) |

**Output**: output[0] = simcc_x, output[1] = simcc_y; each keypoint = `argmax` over its 1D SimCC (bins = pixels × 2). **Preprocessing**: center-crop to square, resize 256×256, mmpose mean/std (RGB, 0-255).

**Sample app**: [rtmanimal/](rtmanimal/) — image picker + 17-keypoint AP-10K animal skeleton.


# Document Dewarping

### DewarpNet

Real-time **document dewarping / rectification** running fully on the LiteRT `CompiledModel` GPU. [DewarpNet](https://github.com/cvlab-stonybrook/DewarpNet) (ICCV 2019) flattens a photographed, curved/folded document — the core of a document scanner. Two CNNs (WCNet UNet → BMNet DenseNet) predict a backward-mapping grid on the GPU; the `grid_sample` unwarp is a tiny host-side step. First document-processing model in the zoo.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| DewarpNet | [dewarp.tflite](https://huggingface.co/litert-community/DewarpNet-LiteRT) | 189 MB | Float32 [1, 3, 256, 256] NCHW (BGR, /255) | Float32 [1, 2, 128, 128] backward map | [cvlab-stonybrook/DewarpNet](https://github.com/cvlab-stonybrook/DewarpNet) | [MIT](https://github.com/cvlab-stonybrook/DewarpNet/blob/master/LICENSE) | [dewarp/](dewarp/) |

**Preprocessing**: BGR, resize 256×256, `x/255` (no mean/std), NCHW. **Unwarp (host-side)**: blur the backward map (3×3), resize to the image size, then bilinear `grid_sample(image, map)` → the flattened document.

**Conversion** (`dewarp/scripts/build_dewarp.py`, litert-torch): pure CNN → fully GPU-compatible (**371/371 nodes on the delegate, 1 partition**; device corr 0.999866, ~24 ms) with two exact patches — `ConvTranspose2d` → ZeroStuffConvT2d (Mali rejects `TRANSPOSE_CONV`) and `Hardtanh(0,1)` → `relu(x)-relu(x-1)` (Mali rejects `RELU_0_TO_1`). CPU-exact vs PyTorch (corr 0.9999999999).

**Sample app**: [dewarp/](dewarp/) — live camera → DewarpNet GPU → flattened document.

# Lane Detection

### Ultra-Fast-Lane-Detection

Real-time **lane detection** running fully on the LiteRT `CompiledModel` GPU. [Ultra-Fast-Lane-Detection](https://github.com/cfzd/Ultra-Fast-Lane-Detection) (ECCV 2020) reformulates lane detection as fast **row-wise classification**: the ResNet18 network runs on the GPU, and a tiny host-side arg/expectation decode turns the grid into lane points. First lane-detection model in the zoo; an ADAS building block.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| Ultra-Fast-Lane-Detection (ResNet18, CULane) | [ufld.tflite](https://huggingface.co/litert-community/Ultra-Fast-Lane-Detection-LiteRT) | 178 MB | Float32 [1, 3, 288, 800] NCHW (RGB, ImageNet-norm) | Float32 [1, 201, 18, 4] (griding+1, rows, lanes) | [cfzd/Ultra-Fast-Lane-Detection](https://github.com/cfzd/Ultra-Fast-Lane-Detection) | [MIT](https://github.com/cfzd/Ultra-Fast-Lane-Detection/blob/master/LICENSE) | [ufld/](ufld/) |

**Preprocessing**: RGB, resize 800×288, `x/255` then ImageNet-normalize, NCHW. **Decode (host-side)**: per lane & row anchor, softmax over the 200 grid cells → expectation column (drop if argmax = "no lane" index 200); map column → x via `linspace(0,799,200)`, row anchor → y.

**Conversion** (`ufld/scripts/build_ufld.py`, litert-torch): pure CNN → fully GPU-compatible (**41/41 nodes on the delegate, 1 partition**; device corr 0.999982, ~20 ms) with one patch — the ResNet18 stem `MaxPool2d(padding=1)` `-inf` PADV2 → 0-pad + unpadded maxpool (exact post-ReLU). CPU-exact vs PyTorch (corr 0.9999999999996).

**Sample app**: [ufld/](ufld/) — live camera → UFLD GPU → per-lane points overlaid.

### TwinLiteNet

Real-time **drivable-area + lane-line segmentation** running fully on the LiteRT `CompiledModel` GPU. [TwinLiteNet](https://github.com/chequanghuy/TwinLiteNet) (2023) is an ultra-light ESPNet-based network with two segmentation heads — the ADAS "where can I drive" + "where are the lanes" building block. Only 3.1 MB.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| TwinLiteNet | [twinlite.tflite](https://huggingface.co/litert-community/TwinLiteNet-LiteRT) | 3.1 MB | Float32 [1, 3, 360, 640] NCHW (RGB, /255) | 2× [1, 2, 360, 640] (drivable area + lane line) | [chequanghuy/TwinLiteNet](https://github.com/chequanghuy/TwinLiteNet) | [MIT](https://github.com/chequanghuy/TwinLiteNet/blob/main/LICENSE) | [twinlite/](twinlite/) |

**Preprocessing**: RGB, resize 640×360, `x/255`, NCHW. **Decode**: `argmax` over the 2 classes of each head → drivable-area mask + lane mask.

**Conversion** (`twinlite/scripts/build_twinlite.py`, litert-torch): pure CNN → fully GPU-compatible (**270/270 nodes on the delegate, 1 partition**; device corr 0.99997/0.99998, ~44 ms) with one patch — `ConvTranspose2d` → ZeroStuffConvT2d (Mali rejects `TRANSPOSE_CONV`). CPU-exact vs PyTorch (corr 1.0).

**Sample app**: [twinlite/](twinlite/) — live camera → TwinLiteNet GPU → drivable area (green) + lanes (red).

# Super-Resolution

### EDSR (×4)

Real-time **×4 single-image super-resolution** running fully on the LiteRT `CompiledModel` GPU. [EDSR](https://arxiv.org/abs/1707.02921) (CVPR 2017 winner) upscales a low-res image 4× with sharp detail. First super-resolution model in the zoo.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| EDSR-base (×4) | [edsr.tflite](https://huggingface.co/litert-community/EDSR-x4-LiteRT) | 7.7 MB | Float32 [1, 3, 128, 128] NCHW (RGB, /255) | Float32 [1, 3, 512, 512] (RGB 0–1) | [eugenesiow/edsr-base](https://huggingface.co/eugenesiow/edsr-base) | [Apache-2.0](https://github.com/eugenesiow/super-image/blob/main/LICENSE) | [edsr/](edsr/) |

**Preprocessing**: RGB, `x/255`, NCHW. **Output**: clamp 0–1, ×255.

**Conversion** (`edsr/scripts/build_edsr.py`, litert-torch): pure CNN, but the **PixelShuffle** upsampler lowers to rank-5/6 reshapes the Mali delegate rejects (the classic super-resolution wall). Exact fix — **PixelShuffle(r) ≡ a fixed-weight `ConvTranspose2d(stride=r)`** → ZeroStuffConvT2d. Result: **68/68 nodes on the delegate, 1 partition**; device corr 0.999946, ~23 ms. CPU-exact vs PyTorch (corr 1.0). This patch also unblocks other PixelShuffle SR models.

# Image Dehazing

### DehazeFormer-MCT

Real-time **image dehazing** with the network fully on the LiteRT `CompiledModel` GPU. [DehazeFormer](https://github.com/IDKiro/DehazeFormer) (TIP 2023, MCT curve-mapping variant trained on a mixed dataset for real-world haze) removes fog / haze / smoke and restores contrast. The 256×256 network predicts 72 per-pixel curve parameters; the curves are applied to the **full-resolution** frame host-side, so output resolution is independent of network resolution.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| DehazeFormer-MCT (mixed) | [dehazeformer_base.tflite](https://huggingface.co/litert-community/DehazeFormer-MCT-LiteRT) | 17 MB | Float32 [1, 3, 256, 256] NCHW (RGB, [-1,1]) | Float32 [1, 72, 256, 256] curve params | [IDKiro/DehazeFormer](https://github.com/IDKiro/DehazeFormer) | [MIT](https://github.com/IDKiro/DehazeFormer/blob/main/LICENSE) | [dehaze/](dehaze/) |

**Preprocessing**: RGB, `x/255*2-1`, NCHW at 256×256. **Decode (host-side)**: trilinear curve lookup per full-res pixel — `out[c] = Σᵢ trilinear(curve[c][i], depth=xᵢ, y, x)`, then `clamp(-1,1)*0.5+0.5` (exact official grid_sample mapping, replica corr 1.0).

**Conversion** (`dehaze/scripts/build_dehaze.py`, litert-torch): Swin-style windowed attention re-authored with the established recipes — window partition/reverse ≤4D, qkv channel slices, baked relative-position bias, reflect pads → slice+concat (litert-torch lowers `reflection_pad2d` to banned `GATHER_ND`, **including padding=0 reflect convs**), SKFusion 5D→4D pairwise softmax, Conv+PixelShuffle → ZeroStuffConvT2d. ⭐New Mali finding: a single `MEAN` over C·H·W (1.5M elements) **overflows the fp16 accumulator** → NaN; RLN global norm + SKFusion global pool re-authored as **hierarchical means** (equal-window `avg_pool` stages, mathematically identical). Result: **2042/2042 nodes on the delegate, 1 partition**; device corr 0.999998, E2E vs the official pipeline corr 0.999997, ~255 ms/frame. Desktop corr vs PyTorch 1.0000000.

**Sample app**: [dehaze/](dehaze/) — live camera → DehazeFormer GPU + host curve mapping → dehazed frame full-screen, tap to compare.

**Sample app**: [edsr/](edsr/) — live camera → EDSR GPU → ×4 super-resolved center region.

# Clothing Segmentation

### Cloth Segmentation (U²-Net)

Real-time **clothing segmentation** running fully on the LiteRT `CompiledModel` GPU. [cloth-segmentation](https://github.com/levindabhi/cloth-segmentation) is a U²-Net trained on iMaterialist-Fashion to segment **upper-body / lower-body / full-body clothing** — the building block for virtual try-on and fashion apps.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| Cloth Segmentation (U²-Net) | [clothseg.tflite](https://huggingface.co/litert-community/Cloth-Segmentation-U2Net-LiteRT) | 176 MB | Float32 [1, 3, 768, 768] NCHW (RGB, [-1,1]) | Float32 [1, 4, 768, 768] (argmax → clothing class) | [levindabhi/cloth-segmentation](https://github.com/levindabhi/cloth-segmentation) | [MIT](https://github.com/levindabhi/cloth-segmentation/blob/main/LICENSE) | [clothseg/](clothseg/) |

**Preprocessing**: RGB, resize 768×768, `(x/255 - 0.5)/0.5`, NCHW. **Decode**: `argmax` over the 4 classes → 0 background, 1 upper body, 2 lower body, 3 full body.

**Conversion** (`clothseg/scripts/build_clothseg.py`, litert-torch): pure CNN → fully GPU-compatible (**254/254 nodes on the delegate, 1 partition**; device corr 0.999798, ~88 ms) with one defensive patch — `align_corners=True` → `False`. CPU-exact vs PyTorch (corr 1.0). ⚠ Strip the `module.` prefix when loading the checkpoint.

**Sample app**: [clothseg/](clothseg/) — live camera → U²-Net GPU → clothing segments (upper/lower/full).

# Portrait Sketch

### U²-Net Portrait

Real-time **portrait sketch generation** running fully on the LiteRT `CompiledModel` GPU. The [U²-Net](https://github.com/xuebinqin/U-2-Net) portrait model turns a face photo into a **hand-drawn pencil line portrait** — a fun creative / AR filter.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| U²-Net Portrait | [portrait.tflite](https://huggingface.co/litert-community/U2Net-Portrait-Sketch-LiteRT) | 176 MB | Float32 [1, 3, 512, 512] NCHW (RGB, ImageNet-norm) | Float32 [1, 1, 512, 512] (0–1) | [xuebinqin/U-2-Net](https://github.com/xuebinqin/U-2-Net) | [Apache-2.0](https://github.com/xuebinqin/U-2-Net/blob/master/LICENSE) | [portrait/](portrait/) |

**Preprocessing**: RGB, resize 512×512, `x/255` then ImageNet-normalize, NCHW. **Decode**: min-max normalize the output, then invert (`1−x`) for dark strokes on white paper.

**Conversion** (`portrait/scripts/build_portrait.py`, litert-torch): pure CNN → fully GPU-compatible (**893/893 nodes on the delegate, 1 partition**; device corr 0.998683, ~12 ms) with one defensive patch — `align_corners=False`. CPU-exact vs PyTorch (corr 1.0).

**Sample app**: [portrait/](portrait/) — live camera → U²-Net GPU → live pencil portrait.

# Face Liveness / Anti-Spoofing

### Silent-Face (MiniFASNetV2)

Real-time **face liveness / anti-spoofing** running fully on the LiteRT `CompiledModel` GPU. [Silent-Face-Anti-Spoofing](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing) detects **presentation attacks** — a printed photo or a replayed screen shown to the camera — so a live face passes and a fake is rejected. The anti-fraud building block for face login / e-KYC. Tiny (1.85 MB).

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| Silent-Face (MiniFASNetV2) | [silentface.tflite](https://huggingface.co/litert-community/Silent-Face-Anti-Spoofing-LiteRT) | 1.85 MB | Float32 [1, 3, 80, 80] NCHW (BGR, /255, face crop) | Float32 [1, 3] softmax (class 1 = live) | [minivision-ai/Silent-Face-Anti-Spoofing](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing) | [Apache-2.0](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing/blob/master/LICENSE) | [liveness/](liveness/) |

**Preprocessing**: face crop (~2.7× the face box), BGR, resize 80×80, `x/255`, NCHW. **Decode**: softmax; class 1 = live, 0 & 2 = spoof (print / replay); live score = `output[1]`.

**Conversion** (`liveness/scripts/build_silentface.py`, litert-torch): pure CNN → fully GPU-compatible (**168/168 nodes on the delegate, 1 partition**; device corr 1.0, ~5 ms) with zero patches — PReLU lowers to GPU-clean relu ops. CPU-exact vs PyTorch (corr 1.0).

**Sample app**: [liveness/](liveness/) — live camera → MiniFASNetV2 GPU → LIVE / SPOOF verdict.

# Head Pose Estimation

### 6DRepNet

Real-time **6-DoF head pose estimation** running fully on the LiteRT `CompiledModel` GPU. [6DRepNet](https://github.com/thohemp/6DRepNet) (ICIP 2022) regresses a continuous 6D rotation from a face crop — yaw / pitch / roll for driver-monitoring, AR, and attention. RepVGG (deploy) backbone.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| 6DRepNet | [6drepnet.tflite](https://huggingface.co/litert-community/6DRepNet-HeadPose-LiteRT) | 157 MB | Float32 [1, 3, 224, 224] NCHW (RGB, ImageNet-norm, face crop) | Float32 [1, 6] (6D rotation) | [thohemp/6DRepNet](https://github.com/thohemp/6DRepNet) | [MIT](https://github.com/thohemp/6DRepNet/blob/master/LICENSE) | [sixdrepnet/](sixdrepnet/) |

**Preprocessing**: face crop, resize 224×224, RGB, ImageNet-normalize, NCHW. **Decode (host-side)**: Gram-Schmidt the 6D → 3×3 rotation matrix → Euler `pitch=atan2(R21,R22)`, `yaw=atan2(-R20,√(R00²+R10²))`, `roll=atan2(R10,R00)`.

**Conversion** (`sixdrepnet/scripts/build_6drepnet.py`, litert-torch): deploy-mode RepVGG (plain convs) → fully GPU-compatible (**36/36 nodes on the delegate, 1 partition**; device corr 0.9993, ~21 ms) with zero patches. Use the deploy weights (fused `rbr_reparam`). CPU-exact vs PyTorch (corr 1.0).

**Sample app**: [sixdrepnet/](sixdrepnet/) — live camera → 6DRepNet GPU → 3D head-pose axes.

# Camouflaged Object Detection

### SINet-V2

Real-time **camouflaged object detection** running fully on the LiteRT `CompiledModel` GPU. [SINet-V2](https://github.com/GewelsJI/SINet-V2) (TPAMI 2022) finds objects that **blend into their background** — hidden animals, concealed items, defect/polyp-style targets — where ordinary segmentation fails.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| SINet-V2 (Res2Net-50) | [sinet.tflite](https://huggingface.co/litert-community/SINet-V2-Camouflage-LiteRT) | 100 MB | Float32 [1, 3, 352, 352] NCHW (RGB, ImageNet-norm) | Float32 [1, 1, 352, 352] sigmoid | [GewelsJI/SINet-V2](https://github.com/GewelsJI/SINet-V2) | [Apache-2.0](https://github.com/GewelsJI/SINet-V2) | [sinet/](sinet/) |

**Preprocessing**: RGB, resize 352×352, ImageNet-normalize, NCHW. **Output**: sigmoid map, high = concealed object; resize + threshold/overlay.

**Conversion** (`sinet/scripts/build_sinet.py`, litert-torch): pure CNN → fully GPU-compatible (**2447/2447 nodes on the delegate, 1 partition**; device corr 0.994) with two patches — ZeroPadMaxPool for the Res2Net stem + `align_corners=False`. CPU-exact vs PyTorch (corr 0.997).

**Sample app**: [sinet/](sinet/) — live camera → SINet-V2 GPU → concealed objects highlighted.

# Crowd Counting

### DM-Count

Real-time **crowd counting** running fully on the LiteRT `CompiledModel` GPU. [DM-Count](https://github.com/cvlab-stonybrook/DM-Count) (NeurIPS 2020) regresses a person **density map** whose sum is the crowd size — it counts hundreds of people where detector-based counting saturates.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| DM-Count (VGG19, UCF-QNRF) | [dmcount.tflite](https://huggingface.co/litert-community/DM-Count-Crowd-LiteRT) | 86 MB | Float32 [1, 3, 512, 512] NCHW (RGB, ImageNet-norm) | Float32 [1, 1, 64, 64] density map | [cvlab-stonybrook/DM-Count](https://github.com/cvlab-stonybrook/DM-Count) | [MIT](https://github.com/cvlab-stonybrook/DM-Count/blob/master/LICENSE) | [crowdcount/](crowdcount/) |

**Preprocessing**: RGB, resize 512×512, ImageNet-normalize, NCHW. **Output**: non-negative density map at 1/8 resolution; `sum(map)` = estimated person count, normalize per-frame for the heatmap overlay.

**Conversion** (`crowdcount/scripts/build_dmcount.py`, litert-torch): pure CNN (VGG19 + conv regression head) → fully GPU-compatible (**30/30 nodes on the delegate, 1 partition**; device corr 0.99998, count within 0.4%) with **one exact rewrite** — the mid-graph `F.upsample_bilinear` (align_corners=True `RESIZE_BILINEAR`, banned on the delegate) is a linear operator, re-authored as two constant-matrix multiplies (→ `FULLY_CONNECTED`; the constant must be on the RHS — the delegate rejects `BATCH_MATMUL` with a constant LHS). Desktop corr vs PyTorch 1.000000.

**Sample app**: [crowdcount/](crowdcount/) — live camera → DM-Count GPU → density heatmap + live person count.

# Instance Segmentation

### YOLACT-ResNet50

Real-time **instance segmentation** (per-object COCO masks) running fully on the LiteRT `CompiledModel` GPU. [YOLACT](https://arxiv.org/abs/1904.02689) (ICCV 2019): the network (ResNet50 + FPN + protonet + heads) runs on the GPU; the lightweight decode (NMS + linear-combination masks) runs host-side — the RF-DETR raw-head pattern. First instance-segmentation model in the zoo.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| YOLACT-ResNet50 | [yolact.tflite + priors.bin](https://huggingface.co/litert-community/YOLACT-ResNet50-LiteRT) | 125 MB | Float32 [1, 3, 550, 550] NCHW (BGR) | loc [1,19248,4] + conf [1,19248,81] + mask [1,19248,32] + proto [1,138,138,32] | [dbolya/yolact](https://github.com/dbolya/yolact) | [MIT](https://github.com/dbolya/yolact/blob/master/LICENSE) | [yolact/](yolact/) |

**Preprocessing**: BGR, resize 550×550, `(x - [103.94,116.78,123.68]) / [57.38,57.12,58.40]` (no /255), NCHW. **Decode (host-side)**: SSD box decode vs the baked 19248 priors (variances [0.1,0.2]) → per-class NMS (IoU 0.5) → lincomb masks `sigmoid(proto @ coeff)` cropped to each box.

**Conversion** (`yolact/scripts/build_yolact.py`, litert-torch): base YOLACT (no deformable conv) is a pure CNN → fully GPU-compatible (**138/138 nodes on the delegate, 1 partition**; device corr 0.99999–1.0 on all 4 outputs, ~41 ms) with **one patch** — the ResNet50 stem `MaxPool2d(padding=1)` lowers to a `-inf` PADV2 (rejected by Mali), replaced by a 0-pad + unpadded maxpool (exact post-ReLU); the scripted FPN is made traceable by disabling YOLACT's JIT. The 3D `[1,19248,C]` head outputs survive the Mali delegate. CPU-exact vs PyTorch (corr 1.0).

**Sample app**: [yolact/](yolact/) — live camera → YOLACT GPU → colored instance masks + boxes + COCO labels.

# Segmentation

### MobileSAM

<img src="https://github.com/user-attachments/assets/e9d0cc88-4d49-4ba4-ae8a-86c39befa80e" width="300">

MobileSAM: Fast Segment Anything on mobile. Tap anywhere to segment — encoder runs once per image (GPU), decoder runs per tap (CPU). Based on TinyViT encoder (6.1M params) + SAM mask decoder (4.1M params).

Encoder converted via **litert-torch** (the only converter that preserves Vision Transformer attention accuracy). Decoder runs on ONNX Runtime due to TFLite conversion limitations with cross-attention.

| Model | Download Link | Size | Input | Output | API |
| ----- | ------------- | ---- | ----- | ------ | --- |
| Encoder | [mobilesam_encoder.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/mobilesam_encoder.tflite) | 28 MB | Float32 [1, 3, 1024, 1024] NCHW | Float32 [1, 256, 64, 64] NCHW | CompiledModel GPU |
| Decoder | [mobilesam_decoder.onnx](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/mobilesam_decoder.onnx) | 16 MB | Embeddings + point coords | Mask [1, 1, 1024, 1024] + IoU | ONNX Runtime CPU |

**Preprocessing**: RGB with `mean=[123.675, 116.28, 103.53]`, `std=[58.395, 57.12, 57.375]`. NCHW planar layout.

**Decoder inputs**: `image_embeddings` [1,256,64,64] + `point_coords` [1,2,2] + `point_labels` [1,2] + `mask_input` [1,1,256,256] + `has_mask_input` [1] + `orig_im_size` [2]

**Sample app**: [mobilesam/](mobilesam/) — Image picker + tap-to-segment with mask overlay.

**Original project**: [ChaoningZhang/MobileSAM](https://github.com/ChaoningZhang/MobileSAM) | [Apache-2.0](https://github.com/ChaoningZhang/MobileSAM/blob/master/LICENSE)

### SAM 2.1 (Hiera-Tiny)

The **full** SAM 2.1 (Meta) — the Hiera hierarchical ViT, not the distilled EdgeTAM — running entirely on **CompiledModel GPU**. Tap a point, get a mask. The heavy Hiera image encoder runs once per image; the tiny mask decoder runs per tap. Also the subject of a cross-framework benchmark: **[LiteRT vs MLX on the same Apple GPU](sam2/BENCHMARK.md)**.

Converted with **litert-torch** from the `transformers` `Sam2Model`. The SAM 2 mask decoder converts unchanged; the Hiera encoder needs three numerically-exact rewrites (parity held at corr 1.0 after each): **bake the windowed positional embedding** (constant for a fixed 1024² input — removes the bicubic `GATHER_ND` and the tiled `BROADCAST_TO`), **4-D window partition/unpartition** (the upstream 6-D `view`+`permute` becomes split-H→transpose→split-W; ML Drift rejects >4-D tensors), and **4-D multi-scale attention** (the fused 5-D `qkv` reshape becomes a channel-wise q/k/v slice). Result: `banned ops = NONE`, `>4-D tensors = 0` for both graphs.

> ⚠ **Keep the batch dim in attention.** A rank-3 attention (`q/k/v` shaped `[heads, N, d]`) compiles, delegates every node, passes the op gate and matches PyTorch on the host — yet ML Drift **silently mis-computes it** (corr 0.265 vs CPU on a Pixel 8a; still 0.473 with fp32 GPU compute forced, so it is a correctness bug, not an fp16 wall). See [GPU Compatibility Notes](#gpu-compatibility-notes).

| Model | Download Link | Size | Input | Output | API |
| ----- | ------------- | ---- | ----- | ------ | --- |
| Encoder | [sam2_encoder.tflite](https://huggingface.co/mlboydaisuke/SAM2-hiera-tiny-LiteRT) | 80 MB | Float32 [1, 3, 1024, 1024] NCHW | Float32 [1, 4194304] (ie \| fpn0 \| fpn1) | CompiledModel GPU |
| Decoder | [sam2_decoder.tflite](https://huggingface.co/mlboydaisuke/SAM2-hiera-tiny-LiteRT) | 17 MB | Float32 [1, 4194816] (ie \| sparse \| fpn0 \| fpn1) | Masks [1, 3, 256, 256] | CompiledModel GPU |

**Preprocessing**: resize to 1024×1024, divide by 255, ImageNet mean/std `[0.485,0.456,0.406]`/`[0.229,0.224,0.225]`, NCHW planar. The point→token prompt encoder runs in Kotlin/Swift from `sam2_prompt.bin`.

**Fidelity**: converted graphs match the PyTorch model at corr **1.0** (mask IoU 1.0/0.997/1.0). Device (all `fullyGPU`, mask foreground ≈ the 64.9k-px reference): Pixel 8a GPU enc **610 ms** / dec **76 ms**; iPhone 17 Pro (Metal) enc **248 ms** / dec **16 ms**.

**Sample apps**: [sam2/](sam2/) (Android, tap-to-segment + headless benchmark), [sam2-ios/](sam2-ios/) (iOS, LiteRT `CompiledModel` C API on Metal), [sam2-mlx-ios/](sam2-mlx-ios/) (iOS, a full **mlx-swift** port of the MLX SAM 2 image path, corr 1.0 vs the Python reference — used as the MLX side of the benchmark). Conversion: [sam2/scripts/convert_sam2.py](sam2/scripts/convert_sam2.py).

**Original project**: [facebook/sam2.1-hiera-tiny](https://huggingface.co/facebook/sam2.1-hiera-tiny) ([facebookresearch/sam2](https://github.com/facebookresearch/sam2)) | [Apache-2.0](https://github.com/facebookresearch/sam2/blob/main/LICENSE)

### EdgeTAM (SAM2)

EdgeTAM (Meta, CVPR 2025): on-device Segment Anything 2. Tap an object to segment it. RepViT backbone + FPN neck encoder (runs once per image) and a SAM2 mask decoder (runs per tap) — **both on CompiledModel GPU**. Image-segment mode only (the novel 2D Spatial Perceiver lives in the video-memory path, skipped). 9.1M params.

Converted via **litert-torch** (MobileSAM-style split): image **encoder** (image → embeddings + FPN), a tiny **prompt encoder in Kotlin** (point → sparse embedding, bit-exact vs the model — the positional `coords @ Gaussian` trips a `batch_matmul` converter pass, so it stays off-graph), and the mask **decoder** (embeddings + FPN + sparse → masks). Both graphs use a single concatenated input/output so CompiledModel never maps same-sized tensors by order. GPU-compat patches: **SqueezeExcite global avg-pool `mean((2,3))` → two single-axis means** (a single multi-axis `SUM` over ~65k elements silently returns NaN on the Pixel 8a ML Drift delegate — see [GPU Compatibility Notes](#gpu-compatibility-notes)), **ConvTranspose2d → zero-stuff + Conv2d** (`TRANSPOSE_CONV` rejected on-device), and a 4D mask decoder. Exact erf-GELU is kept (it is GPU-correct; the sigmoid approximation hurt mask quality).

| Model | Download Link | Size | Input | Output | API |
| ----- | ------------- | ---- | ----- | ------ | --- |
| Encoder | [edgetam_encoder.tflite](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT) | 10 MB | Float32 [1, 3, 1024, 1024] NCHW | Float32 [1, 4194304] (ie \| fpn0 \| fpn1) | CompiledModel GPU |
| Decoder | [edgetam_decoder.tflite](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT) | 17 MB | Float32 [1, 4194816] (ie \| sparse \| fpn0 \| fpn1) | Masks [1, 3, 256, 256] | CompiledModel GPU |

**Preprocessing**: resize to 1024×1024, divide by 255, ImageNet mean/std `[0.485,0.456,0.406]`/`[0.229,0.224,0.225]`, NCHW planar.

**Fidelity**: split pipeline corr **1.0** vs the full PyTorch model; on-device circle self-test `mask_fg=11376` (PyTorch ≈ 11816). Pixel 8a GPU: encoder ~110–220 ms (first run includes shader compile), decoder ~60 ms/tap → interactive tap-to-segment.

**Sample app**: [edgetam/](edgetam/) — image picker + tap-to-segment with mask overlay. Conversion: [edgetam/scripts/convert_edgetam.py](edgetam/scripts/convert_edgetam.py).

**Original project**: [facebook/EdgeTAM](https://github.com/facebookresearch/EdgeTAM) ([yonigozlan/EdgeTAM-hf](https://huggingface.co/yonigozlan/EdgeTAM-hf)) | [Apache-2.0](https://github.com/facebookresearch/EdgeTAM/blob/main/LICENSE)

### EdgeTAM Video (SAM2 tracking)

EdgeTAM's full **video object tracking** (Segment Anything 2 memory mechanism) running on-device on CompiledModel GPU — tap an object on the first frame and it is segmented and **tracked across the following frames**, on the GPU. This is the SAM2 memory pipeline (not per-frame re-segmentation): each frame's mask conditions the next via a rolling memory bank.

Four stateless per-frame graphs run on the GPU; the rolling memory bank (7 spatial-memory frames + up to 16 object-pointer frames) is managed in Kotlin — the standard on-device SAM2 split. Verified frame-by-frame **IoU ~1.0** vs the HF PyTorch model, and **on-device GPU tracking verified** on a Pixel 8a (the mask follows a moving target within ~1 px/frame).

| Graph | Role | Size (FP16) |
| ----- | ---- | ----------- |
| [encode.tflite](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT)   | frame → image features + FPN                          | 10 MB |
| [memcond.tflite](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT) | memory attention over the fixed-7 bank (masked) → conditioned features | 26 MB |
| [decode.tflite](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT)   | mask decoder → 3 masks + IoU + object pointers + score | 18 MB |
| [memorize.tflite](https://huggingface.co/mlboydaisuke/EdgeTAM-LiteRT) | memory encoder + 2D Spatial Perceiver → new memory | 5 MB |

**Conversion** (litert-torch): the memory attention's **RoPE** (5D `rotate_pairwise`) is rewritten as a baked even/odd projection permutation + `rotate_half` with constant cos/sin; the cross-attention temporal/spatial 5D regroup is replaced by a constant masked `cos_k`; the 2D Spatial Perceiver's **Swin-style window partition (6D)** is replaced by a **grouped one-hot `Conv2d` space-to-depth** (stays 4D — the trick that lets window attention run on CompiledModel GPU at all); and several on-device-only fixes (constant-input `MEAN`/`DIV`/`SELECT` are rejected by ML Drift: latents tainted to runtime, single-key softmax skipped, sine position-encodings baked). See [GPU Compatibility Notes](#gpu-compatibility-notes) and [edgetam-video/scripts/convert_edgetam_video.py](edgetam-video/scripts/convert_edgetam_video.py).

**Preprocessing**: per-frame resize to 1024×1024, divide by 255, ImageNet mean/std, NCHW planar.

**Sample app**: [edgetam-video/](edgetam-video/) — pick a video, tap an object on the first frame, watch the tracked mask overlay play back. Pixel 8a GPU ~0.45 s/frame (offline). Reference pipeline: [edgetam-video/scripts/deploy_ref_flat.py](edgetam-video/scripts/deploy_ref_flat.py).

**Original project**: [facebook/EdgeTAM](https://github.com/facebookresearch/EdgeTAM) ([yonigozlan/EdgeTAM-hf](https://huggingface.co/yonigozlan/EdgeTAM-hf)) | [Apache-2.0](https://github.com/facebookresearch/EdgeTAM/blob/main/LICENSE)

# Background Removal

### RMBG-1.4 (ISNet)

RMBG-1.4: High-quality background removal based on ISNet (U2-Net variant). Pure CNN architecture — 44M params, runs on CompiledModel GPU. Outputs alpha matte for clean foreground extraction.

Converted via **litert-torch** from [briaai/RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4). Output is sigmoid-activated (0-1 mask), no post-processing needed.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [rmbg14.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/rmbg14.tflite) | 176 MB | Float32 [1, 3, 1024, 1024] NCHW | Float32 [1, 1, 1024, 1024] | [briaai/RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4) | [bria-rmbg-1.4](https://bria.ai/bria-huggingface-model-license-agreement/) | [rmbg/](rmbg/) |

**Preprocessing**: RGB normalized as `(pixel/255 - 0.5)`. NCHW planar layout.

### ormbg (open, Apache-2.0)

[ormbg](https://huggingface.co/schirrmacher/ormbg): a fully **open, Apache-2.0** background-removal model (an ISNet trained for photorealistic subject cut-out) — the permissively-licensed alternative to the non-commercial RMBG-1.4. Pure CNN, fully on CompiledModel GPU — 246 ms per 1024² frame on a Pixel 8a (2026-09-05, run + readback, thermal status 0; the “~10 ms” quoted here earlier timed only the asynchronous `run()`).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [ormbg.tflite](https://huggingface.co/litert-community/ormbg-LiteRT) | 176 MB | Float32 [1, 3, 1024, 1024] NCHW (RGB, /255) | Float32 [1, 1, 1024, 1024] alpha | [schirrmacher/ormbg](https://huggingface.co/schirrmacher/ormbg) | [Apache-2.0](https://huggingface.co/schirrmacher/ormbg) | [ormbg/](ormbg/) |

**Preprocessing**: RGB, `x / 255` (no mean/std). **Output**: raw alpha matte — min-max normalize per frame before compositing.

**Add to your app**: [ormbg/INTEGRATION.md](ormbg/INTEGRATION.md) — one Gradle line, one drop-in Kotlin file, the model download with its checksum, and the on-device check with its expected values ([`ormbg/recipe.json`](ormbg/recipe.json) carries the same facts for agents).

### DIS (IS-Net, general-use)

[DIS](https://github.com/xuebinqin/DIS) (ECCV 2022): high-accuracy **dichotomous image segmentation** — cuts out the main object with fine structure detail (thin stems, petals, wires) for e-commerce product photos and graphics. IS-Net, fully on CompiledModel GPU, ~11 ms/frame on a Pixel 8a.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| DIS (IS-Net general-use) | [dis.tflite](https://huggingface.co/litert-community/DIS-ISNet-LiteRT) | 176 MB | Float32 [1, 3, 1024, 1024] NCHW (RGB, x/255−0.5) | Float32 [1, 1, 1024, 1024] alpha | [xuebinqin/DIS](https://github.com/xuebinqin/DIS) | [Apache-2.0](https://github.com/xuebinqin/DIS) | [dis/](dis/) |

**Preprocessing**: RGB, resize 1024×1024, `x/255 − 0.5`, NCHW. **Output**: sigmoid alpha (0–1).

**Conversion** (`dis/scripts/build_dis.py`, litert-torch): pure CNN → fully GPU-compatible (**247/247 nodes on the delegate, 1 partition**; device max|diff| 0.00034, ~11 ms) with one defensive patch — `align_corners=False`. CPU-exact vs PyTorch (max|diff| 0.0).

**Sample app**: [dis/](dis/) — live camera → DIS GPU → high-precision cutout.

**Conversion** (`ormbg/scripts/build_ormbg.py`, litert-torch): pure CNN → fully GPU-compatible (**246/246 nodes on the delegate, 1 partition**; device corr 0.999881; 246 ms/frame on a Pixel 8a, see [ormbg/INTEGRATION.md](ormbg/INTEGRATION.md)) with one defensive patch — `align_corners=True` → `False` on the bilinear upsamples. CPU-exact vs PyTorch (corr 0.9999999999).

**Output format**: Sigmoid mask (0-1). Apply as alpha channel to original image for transparent background.

# Portrait Matting

### MODNet (trimap-free)

Real-time **portrait matting** running fully on the LiteRT `CompiledModel` GPU. [MODNet](https://arxiv.org/abs/2011.11961) (AAAI 2022) predicts a **soft alpha matte** for a person — no trimap, no green screen — for background blur/replace (video calls, virtual backgrounds). ~79 ms/frame on a Pixel 8a. Distinct from RMBG background removal: MODNet targets soft human alpha (hair detail).

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| MODNet | [modnet.tflite](https://huggingface.co/litert-community/MODNet-LiteRT) | 26 MB | Float32 [1, 3, 512, 512] NCHW ([-1,1]) | Float32 [1, 1, 512, 512] alpha | [ZHKKKe/MODNet](https://github.com/ZHKKKe/MODNet) | [Apache-2.0](https://github.com/ZHKKKe/MODNet/blob/master/LICENSE) | [modnet/](modnet/) |

**Preprocessing**: RGB, resize 512×512, normalize to [-1,1] (`(pixel/255 - 0.5)/0.5`), NCHW. **Output**: soft alpha matte 0–1; composite `fg·α + bg·(1-α)`.

**Conversion** (`modnet/scripts/build_modnet.py`, litert-torch): pure CNN (MobileNetV2 backbone), 2 re-authoring patches → fully GPU-compatible (**0 tensors of rank > 4, 0 banned ops**): (1) SE block `Linear`→`1×1 conv` (the 2D-reshape confuses NCHW↔NHWC), (2) **fp16-safe hierarchical-mean InstanceNorm** — MODNet's IBNorm runs InstanceNorm over up to 512² spatial, whose variance `sum(dd²)` overflows fp16 on Mali (matte degrades, corr 0.94); computing the mean via a cascade of `/2` avg-pools (magnitude-bounded, exact) restores GPU corr **0.99994** with clean edges. CPU-exact vs PyTorch (corr 0.99999999999).

**Sample app**: [modnet/](modnet/) — live camera → MODNet GPU → foreground composited over a replaceable background (tap to change).

# Inpainting

### LaMa-Dilated

LaMa-Dilated: Large Mask Inpainting with dilated convolutions. Draw a mask over unwanted objects and the model fills in the region naturally. Based on [LaMa](https://github.com/advimman/lama) with FFT blocks replaced by dilated convolutions for GPU compatibility.

Pre-converted TFLite from [Qualcomm AI Hub](https://aihub.qualcomm.com/models/lama_dilated). Pure CNN, 361 ops, all GPU-native.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [lama_dilated.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v1/lama_dilated.tflite) | 174 MB | Float32 [1, 512, 512, 3] + [1, 512, 512, 1] NHWC | Float32 [1, 512, 512, 3] NHWC | [advimman/lama](https://github.com/advimman/lama) | [Apache-2.0](https://github.com/advimman/lama/blob/main/LICENSE) | [lama/](lama/) |

**Preprocessing**: Image RGB normalized to 0-1 (divide by 255). Mask is single channel 0-1 (1 = area to inpaint).

**Sample app**: [lama/](lama/) — Image picker + finger drawing mask + inpainting with before/after toggle.

### MI-GAN (mobile inpainting / object removal)

[MI-GAN](https://github.com/Picsart-AI-Research/MI-GAN) (Picsart AI Research, **ICCV 2023**, MIT): a "magic eraser" — paint over an object and it is removed and inpainted. A mobile-designed StyleGAN-style generator (separable convs, nearest-upsample, **no norm**) — far smaller/faster than LaMa above. Verified **fully on the GPU** (`509/509` LITERT_CL on a Pixel 8a, **~6 ms** at 512×512, device-vs-PyTorch corr **0.99998**, **16.3 MB** fp16).

Converted via **litert-torch** with **no re-authoring** — the inference generator is already GPU-clean (depthwise-separable conv, `nn.Upsample(nearest)` + FIR-filter grouped conv, leaky-ReLU clamp → `MAXIMUM`/`MINIMUM`, no normalization). The FFT-free, norm-free generator lane.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [migan_fp16.tflite](https://huggingface.co/litert-community/MI-GAN-512-Places2-LiteRT) | 16.3 MB | Float32 [1, 4, 512, 512] NCHW (`concat(mask−0.5, rgb·mask)`) | Float32 [1, 3, 512, 512] ([−1,1]) | [Picsart-AI-Research/MI-GAN](https://github.com/Picsart-AI-Research/MI-GAN) | [MIT](https://github.com/Picsart-AI-Research/MI-GAN/blob/main/LICENSE) | [migan/](migan/) |

**I/O**: input `concat(mask−0.5, rgb·mask)` (rgb ∈ [−1,1], mask = 1 keep / 0 erase); composite back as `rgb·mask + out·(1−mask)`. **Preprocessing**: center-crop, resize 512×512.

**Sample app**: [migan/](migan/) — image picker + finger-paint mask + on-device erase.


# Zero-Shot Classification

### CLIP ViT-B/32

CLIP: Zero-shot image classification using OpenAI's CLIP ViT-B/32 image encoder with pre-computed text embeddings. Classify any image into 96 diverse labels without task-specific training.

Converted via **litert-torch** (ViT architecture). Text embeddings pre-computed with prompt template "a photo of a {label}".

| Model | Download Link | Size | Input | Output | API |
| ----- | ------------- | ---- | ----- | ------ | --- |
| Image Encoder | [clip_image_encoder.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/clip_image_encoder.tflite) | 352 MB | Float32 [1, 3, 224, 224] NCHW | Float32 [1, 512] | CompiledModel GPU |
| Text Embeddings | [text_embeddings.bin](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/text_embeddings.bin) | 192 KB | — | Float32 [96, 512] | Pre-computed |

**Preprocessing**: RGB with CLIP normalization (mean=[122.77, 116.75, 104.09], std=[68.50, 66.63, 70.32]). Center-crop to square, resize to 224x224. NCHW planar layout.

**Classification**: Cosine similarity between image embedding and text embeddings → softmax with temperature 100.

**Sample app**: [clip/](clip/) — Image picker + top-10 classification results with confidence bars.

**Original project**: [mlfoundations/open_clip](https://github.com/mlfoundations/open_clip) | [MIT](https://github.com/mlfoundations/open_clip/blob/main/LICENSE)

### Places365 ResNet18 (scene recognition)

ResNet18 trained on [Places365](http://places2.csail.mit.edu/) (CSAILVision, MIT): **scene/place recognition** across **365 categories** (beach, kitchen, forest, office, restaurant, …) — a distinct task from object classification (it answers *what kind of place* a photo is). Pure CNN → runs **fully on the GPU** (`61/61` LITERT_CL on a Pixel 8a, **~2 ms**, fp16 **22.8 MB**, device-vs-PyTorch corr **1.0**, top-1 match).

Converted via **litert-torch** with two numerically-exact re-authorings: the global `AdaptiveAvgPool2d(1)` → `mean(3).mean(2)`, and the ResNet stem `MaxPool2d(3,s2,p1)` → **zero-pad + valid max-pool** (PyTorch's max-pool pads with `-inf` → a `PADV2` the Mali delegate won't delegate; since the pool follows a ReLU, a 0-pad is exactly equivalent and emits a delegatable `PAD`).

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [places_fp16.tflite](https://huggingface.co/litert-community/Places365-ResNet18-LiteRT) | 22.8 MB | Float32 [1, 3, 224, 224] NCHW | Logits [1, 365] | [CSAILVision/places365](https://github.com/CSAILVision/places365) | [MIT](https://github.com/CSAILVision/places365/blob/master/LICENSE) | [places365/](places365/) |

**Preprocessing**: center-crop, resize to 224×224, /255, ImageNet mean/std, NCHW. Output 365-class scene logits; softmax + argmax for top-k.

**Sample app**: [places365/](places365/) — image picker + top-5 scene categories.


# Dense Feature Visualization

### DINOv2 ViT-S/14

Run the self-supervised [DINOv2](https://github.com/facebookresearch/dinov2) ViT-S/14 backbone fully on the LiteRT `CompiledModel` GPU and visualize its **dense patch features** — a top-3 PCA of the tokens mapped to RGB. Semantically similar patches (object parts vs background) land near each other in feature space, so they share a color and the object "pops out" with no labels or segmentation. The first self-supervised-backbone / feature-visualization demo in the zoo.

| Model | Download Link | Size | Input | Output | Original Project | License | Sample App |
| ----- | ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| DINOv2 ViT-S/14 | [dinov2_s_fp16.tflite](https://huggingface.co/litert-community/DINOv2-ViT-S14-LiteRT) | 45 MB | Float32 [1, 3, 448, 448] NCHW (ImageNet-norm) | Float32 [1, 1024, 384] patch tokens | [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) | [Apache-2.0](https://github.com/facebookresearch/dinov2/blob/main/LICENSE) | [dinov2/](dinov2/) |

**Preprocessing**: resize 448×448, ImageNet normalization, NCHW. **Decode (host-side)**: top-3 PCA of the 1024×384 token matrix (power iteration on the 384×384 covariance) → per-patch RGB → upscaled overlay.

**Conversion** (`dinov2/scripts/build_dinov2.py`, litert-torch): the proven ViT recipes — fused-qkv attention decomposed to 4D `[1,heads,N,d]` (C12), **SafeLayerNorm** (deviation scaled by 1/64 before squaring so the fp16 variance doesn't overflow on DINOv2's massive activations), **LayerScale** (`ls1`/`ls2`) baked into the projections, and **tanh-GELU** (`0.5x(1+tanh(…))`) — the sigmoid-GELU approximation drifts to feature corr 0.968 over 12 blocks, tanh → 0.99999. The pos_embed is baked at a fixed 448 grid by timm at model creation, so there is no runtime interpolation (no `GATHER_ND`). Result: **864/864 nodes on the delegate, 1 partition**, ~8 ms; device fp16 patch features vs desktop fp32 corr 0.996.

**Sample app**: [dinov2/](dinov2/) — pick a photo → image and its DINOv2 feature-PCA side by side.

# Surface Normal Estimation

### DSINE

DSINE (CVPR 2024): Per-pixel surface normal estimation from a single image. Outputs unit normal vectors visualized as RGB color map. Uses EfficientNet-B5 encoder with a custom decoder incorporating camera ray direction encoding.

Converted via **litert-torch** with encoder + decoder initial prediction only (ConvGRU iterative refinement skipped for TFLite compatibility). Additional patches: GroupNorm → 4D manual ops, Conv2d_WS weights baked, F.normalize replaced.

| Download Link | Size | Input | Output | Original Project | License | Sample App |
| ------------- | ---- | ----- | ------ | ---------------- | ------- | ---------- |
| [dsine.tflite](https://github.com/john-rocky/LiteRT-Models/releases/download/v2/dsine.tflite) | 282 MB | Float32 [1, 3, 480, 640] NCHW | Float32 [1, 3, 480, 640] | [baegwangbin/DSINE](https://github.com/baegwangbin/DSINE) | [MIT](https://github.com/baegwangbin/DSINE/blob/main/LICENSE) | [dsine/](dsine/) |

**Preprocessing**: RGB with ImageNet normalization (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]). NCHW planar layout.

**Output format**: `[1, 3, 480, 640]` — unit normal vectors (X, Y, Z) in [-1, 1]. Visualize as `RGB = (normal + 1) / 2 * 255`.

# Speech Recognition

### Parakeet (FastConformer-CTC)

NVIDIA Parakeet (`parakeet-tdt_ctc-110m`, the CTC branch): the 17-layer FastConformer encoder + CTC head run **fully on the LiteRT CompiledModel GPU** on a Pixel 8a — the first big global-attention transformer in this zoo to survive the Mali fp16 path end to end. On-device transcript matches PyTorch exactly (real-frame logits corr 0.99997), 3105/3105 ops on LITERT_CL (1 partition), ~330 ms GPU + ~70 ms host mel ≈ 0.4 s end-to-end per 16 s window (device-app measured).

Converted via **litert-torch**: RelPositionMultiHeadAttention re-authored as manual ≤4D matmuls, GLU→`a·sigmoid(b)`, masking folded into a GPU-clean additive attention bias for the fixed window, CTC `ConvASRDecoder` fused into the graph. Key fix: the subsampling front-end emits very large pre-norm activations (|x|≈7000), so the LayerNorm variance is reduced entirely in a down-scaled domain (never rebuilding the large variance, which overflows fp16 on Mali → blank output).

| Model | Download Link | Size | Input | Output | API |
| ----- | ------------- | ---- | ----- | ------ | --- |
| Encoder + CTC | [parakeet_ship_fp16.tflite](https://huggingface.co/litert-community/Parakeet-tdt-ctc-110m-LiteRT) | 226 MB | mel [1, 80, 1601] + frame mask [1, 201] | CTC logits [1, 201, 1025] | CompiledModel GPU |

**Preprocessing**: 16 kHz mono → NeMo log-mel (80 bins, preemphasis 0.97, 512-pt FFT, slaney filterbank, per-feature norm), computed in Kotlin. Audio up to 16 s is padded to the fixed window.

**Decoding**: greedy CTC (drop blank + repeats) + SentencePiece detokenize (1024 pieces), on the host.

**Sample app**: [parakeet/](parakeet/) — Microphone recording + bundled sample + transcription display.

**Original project**: [NVIDIA NeMo / parakeet-tdt_ctc-110m](https://huggingface.co/nvidia/parakeet-tdt_ctc-110m) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

### Whisper-tiny

Whisper: OpenAI's speech recognition model running on-device. First implementation with LiteRT GPU-accelerated encoder. Supports microphone recording and audio file input with 10 language options.

Encoder converted via **litert-torch** with SigmoidGELU patch. Decoder exported to ONNX with manual attention (SDPA disabled for ONNX compatibility). No KV-cache — acceptable for tiny's 4 