# Real-Time Object Detection with OpenCV

Legacy Python example for running a pretrained MobileNet SSD object detector on frames from a webcam using OpenCV's deep-neural-network module.

> [!IMPORTANT]
> This repository is an educational example, not an actively supported application. The detector and model assets date from 2020. Use OpenCV 4 because OpenCV 5 removed the Caffe importer used here.

## Features

- Live detection from an OpenCV camera
- MobileNet SSD inference through OpenCV DNN
- Configurable camera index and confidence threshold
- PASCAL VOC class labels
- Camera-independent model smoke tests

The current implementation uses OpenCV's default DNN backend. It does not require or configure CUDA, NVCaffe, or an NVIDIA GPU.

## Requirements

- Python 3.10 or newer
- OpenCV 4
- NumPy
- imutils
- A webcam or other camera visible to OpenCV
- A graphical desktop for the preview window

## Installation

```bash
git clone https://github.com/khlaifiabilel/real-time-object-detector.git
cd real-time-object-detector
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Usage

The bundled model files can be used directly:

```bash
python real_time_object_detection.py \
  --prototxt MobileNetSSD_deploy.prototxt.txt \
  --model MobileNetSSD_deploy.caffemodel
```

Use another camera index or confidence threshold when needed:

```bash
python real_time_object_detection.py \
  --prototxt MobileNetSSD_deploy.prototxt.txt \
  --model MobileNetSSD_deploy.caffemodel \
  --camera 1 \
  --confidence 0.5
```

Press `q` in the preview window to stop the detector.

## Detected Classes

The bundled model exposes 20 PASCAL VOC foreground classes:

```text
aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow,
diningtable, dog, horse, motorbike, person, pottedplant, sheep, sofa,
train, tvmonitor
```

## Model Assets

| File | SHA-256 |
| --- | --- |
| `MobileNetSSD_deploy.prototxt.txt` | `e781559c4f5beaec2a486ccd952af5b6fa408e9498761bf5f4fb80b4e9f0d25e` |
| `MobileNetSSD_deploy.caffemodel` | `761c86fbae3d8361dd454f7c740a964f62975ed32f4324b8b85994edec30f6af` |

Keep the prototxt and model together. The Python class ordering must match the model output.

## Testing

Install development dependencies and run the tests:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

The tests load the bundled Caffe model, run inference on a synthetic image, and validate argument handling without requiring a camera.

## Limitations

- Only live camera input is supported.
- The preview requires a graphical environment.
- There is no output recording or structured detection export.
- Frames are displayed at 400 pixels wide and inferred at 300 x 300 pixels.
- Detection accuracy and speed depend on the model, camera, scene, and host hardware.
- No production support, accuracy guarantee, or current platform matrix is provided.

## Attribution And Provenance

The detector script follows the example published by Adrian Rosebrock in the PyImageSearch tutorial [Real-time object detection with deep learning and OpenCV](https://pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/).

The model family is associated with [chuanqi305/MobileNet-SSD](https://github.com/chuanqi305/MobileNet-SSD), a Caffe MobileNet SSD trained on MS COCO and fine-tuned on VOC0712. The exact model and prototxt files in this repository are also byte-identical to files historically published by [djmv/MobilNet_SSD_opencv](https://github.com/djmv/MobilNet_SSD_opencv). The repository history does not establish which source supplied these exact assets.

Relevant research:

- [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
- [SSD: Single Shot MultiBox Detector](https://arxiv.org/abs/1512.02325)

## License

The original source code in this repository is available under the MIT License;
see [`LICENSE`](LICENSE). The bundled MobileNet SSD model and prototxt are
third-party assets with separate provenance and potentially separate terms.
Confirm their applicable upstream licenses before redistribution.

See [`.github/SECURITY.md`](.github/SECURITY.md) for private vulnerability reporting instructions.
