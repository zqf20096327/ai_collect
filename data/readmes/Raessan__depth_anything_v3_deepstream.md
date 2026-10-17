# depth_anything_v3_deepstream: Real-time Depth Anything V3 with NVIDIA DeepStream

Real-time monocular depth estimation using [Depth Anything V3](https://github.com/ByteDance-Seed/Depth-Anything-3) as a production DeepStream 8.0 / TensorRT pipeline. Supports USB cameras, video files, images, and RTSP streams on desktop GPUs and NVIDIA Jetson.

![Demo](assets/demo.gif)

## Features

- **Real-time inference**: Full TensorRT FP16 pipeline via DeepStream 8.0
- **Multiple models**: DA3METRIC-LARGE (metric depth), DA3MONO-LARGE, DA3-SMALL/BASE/LARGE-1.1
- **GPU-accelerated visualization**: Percentile-normalized inferno colormap via CUDA
- **Side-by-side view**: `--show-original` tiles the original frame alongside the depth map
- **Flexible input**: Camera (V4L2), video file, image (JPEG/PNG), RTSP stream, generic URI

## Benchmarks

Measured on RTX 5070 Laptop GPU (8 GiB), DeepStream 8.0, TensorRT FP16, 504×504, batch size 1.

| Model | Params | FPS | GPU Mem |
|-------|--------|-----|---------|
| DA3-SMALL | 34M | 30 | 522 MiB |
| DA3-BASE | 135M | 30 | 744 MiB |
| DA3-LARGE-1.1 | 411M | 30 | 1312 MiB |
| DA3METRIC-LARGE | 334M | 30 | 1208 MiB |
| DA3MONO-LARGE | 334M | 30 | 1208 MiB |

## Installation

### Dependencies

1. **Install CUDA Toolkit**

   Follow the [NVIDIA CUDA installation guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).

2. **Install DeepStream SDK**

   Download and install from [NVIDIA DeepStream](https://developer.nvidia.com/deepstream-sdk).

3. **Install GStreamer development libraries**

   Follow the [GStreamer installation guide](https://gstreamer.freedesktop.org/documentation/installing).

### Model Export

Export a DA3 checkpoint to ONNX using the script in `export/`. See [`export/README.md`](export/README.md) for the conda environment setup, required source patches, and per-model export commands.

Exported ONNX files go to `models/`. On first run DeepStream builds the TensorRT FP16 engine and caches it alongside the ONNX.

### Switching Models

Edit `configs/config_infer_depth_anything_v3.txt` to point at a different model:

```ini
onnx-file=/depth_anything_v3_deepstream/models/DA3-SMALL.onnx
model-engine-file=/depth_anything_v3_deepstream/models/DA3-SMALL.onnx_b1_gpu0_fp16.engine
```

### Build

```bash
cd depth_anything_v3_deepstream
mkdir -p build && cd build
cmake ..
make -j$(nproc)
```

## Docker

Docker support with NVIDIA Container Toolkit is available for simplified deployment.

### Prerequisites

1. Install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) on the host machine.

### Build and Run

```bash
xhost +local:docker   # grant display access to the container
docker compose build
docker compose up
```

Access the container:

```bash
docker exec -it depth_anything_v3_deepstream bash
```

## Usage

Build and run from inside the container (or natively after following the Installation steps):

```bash
cd /depth_anything_v3_deepstream/depth_anything_v3_deepstream/build
```

**USB camera:**
```bash
./depth_anything_v3_deepstream --source-type camera --source-uri /dev/video0
```

**Video file:**
```bash
./depth_anything_v3_deepstream --source-type file --source-uri /path/to/video.mp4
```

**Image:**
```bash
./depth_anything_v3_deepstream --source-type image --source-uri /path/to/image.jpg
```

**RTSP stream:**
```bash
./depth_anything_v3_deepstream --source-type rtsp \
    --source-uri rtsp://192.168.1.100:8554/stream
```

**Side-by-side (original + depth):**
```bash
./depth_anything_v3_deepstream --source-type file \
    --source-uri /path/to/video.mp4 --show-original true
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--source-type` | `camera`, `file`, `image`, `rtsp`, `uri` | `camera` |
| `--source-uri` | Device path, file path, or stream URL | `/dev/video0` |
| `--framerate` | Target frame rate (camera only) | `30` |
| `--config` | Path to nvinfer config file | see `configs/` |
| `--show-original` | Tile original frame alongside depth | `false` |
| `--debug` | Print pipeline string and emit DOT file | `false` |
| `--dot-file` | Path for pipeline DOT file | `./pipeline.dot` |

## Architecture

**Single-model pipeline** (default):
```
Source → nvstreammux → nvinfer(DA3) → depth_probe → nveglglessink
```

**Side-by-side pipeline** (`--show-original true`):
```
Source → nvstreammux → tee
           ├─ original → nvvideoconvert(NVMM RGBA) ──────────────────┐
           └─ nvinfer(DA3) → depth_probe → nvvideoconvert(NVMM RGBA) ┤
                                           nvstreammux → nvmultistreamtiler → nveglglessink
```

DA3 is a standalone encoder-decoder — the full model runs in a single `nvinfer` element. The pad probe extracts the depth tensor from `NvDsInferTensorMeta` and applies percentile normalization and inferno colormap rendering directly to the display surface via a CUDA kernel.

The raw model output can be converted to metric depth in meters (DA3METRIC-LARGE only):
```
metric_depth_m = focal_pixels × raw_output / 300.0
```
where `focal_pixels = (fx + fy) / 2` from the camera intrinsic matrix.

## License

- Code: Apache-2.0
- Depth Anything V3: see [upstream license](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/LICENSE)
- NVIDIA DeepStream SDK: NVIDIA proprietary

## References

- [Depth Anything V3](https://github.com/ByteDance-Seed/Depth-Anything-3)
- [ros2-depth-anything-v3-trt](https://github.com/ika-rwth-aachen/ros2-depth-anything-v3-trt) — ONNX export script
- [NVIDIA DeepStream SDK](https://developer.nvidia.com/deepstream-sdk)
- [dinov3_deepstream](https://github.com/Raessan/dinov3_deepstream) — related multi-task pipeline by the same author
