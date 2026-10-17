# ros2-fast-stereo : ROS2 FastFoundationStereo

<p align="center">
  <img src="assets/outdoors_disparity.gif" alt="ROS2 + FastFoundationStereo TRT"><br>
  <img src="assets/reflective_point_cloud.gif" alt="Point Cloud of Reflective Surfaces">
</p>

A ROS2 (Jazzy) workspace for real-time stereo-rectified depth estimation from both pinhole and wide-FOV camera pairs, using a TensorRT-accelerated port of [Fast-FoundationStereo](https://github.com/NVlabs/Fast-FoundationStereo). It's built from three packages:

| Package | Purpose |
|---|---|
| [`camera_models`](src/camera_models) | Camera abstraction library — 7 projection models (pinhole, Double Sphere, fisheye polynomial, Kannala-Brandt 8, equirectangular, Mei, Omni) behind one `pixelToRay`/`rayToPixel` interface, loadable from ROS2 params or YAML. |
| [`perception_utils`](src/perception_utils) | Precomputes pixel-to-pixel reprojection maps between two cameras (CPU and CUDA/NPP-ready), used to rectify arbitrary camera pairs into a shared virtual pinhole view. |
| [`ffs_depth`](src/ffs_depth) | ROS2 nodes (`ffs_depth_node`, `quad_stereo_node`) that rectify camera pairs on the GPU and run a TensorRT stereo-matching engine to publish disparity images and colored point clouds. Works with any camera model in `camera_models`, including fisheye pairs with heavily overlapping fields of view. |

See each package's own README for API/config/topic details.

## Abstract

Conventional real-time stereo pipelines assume a narrow-baseline, forward-facing camera pair whose optical axes are already nearly parallel, and typically bounce image data between CPU and GPU across separate rectification and inference stages. `ros2-fast-stereo` relaxes both constraints.

Recently, foundational approaches in downstream perception tasks such as FastFoundationStereo have been closing the accuracy gap with offline, non-real-time stereo methods, but the surrounding integration work needed to actually deploy them on arbitrary camera rigs has lagged behind.

In `ros2-fast-stereo`, camera pairs are described through a unified abstraction spanning seven projection models: Pinhole, Double Sphere, fisheye polynomial, Kannala-Brandt 8, equirectangular, Mei, and Omni. A "stereo pair" here can be two wide field-of-view, non-parallel cameras whose optical axes point in different directions, as long as their fields of view overlap. The rectifying rotation that aligns them onto a shared virtual pinhole view is then derived automatically from each camera's calibrated pose.

Once a synchronised frame pair arrives over ROS subscription, every stage of the pipeline from GPU remap, normalisation, TensorRT stereo-matching inference, and disparity-to-depth conversion all run on-device via CUDA, NPP, and TensorRT, with image data crossing the host/device boundary only once per frame going in and once coming out. This keeps CPU-GPU synchronisation off the hot path end-to-end, from image subscription to published depth.

This setup can also be extended to multiple stereo pairs with overlapping fields of view as seen in the quad-stereo setup below to achieve omnidirectional depth estimation.

## Usage

### 1. Set up the Dev Container

The workspace ships a VS Code Dev Container (`.devcontainer/devcontainer.json` + root `Dockerfile`) with ROS2 Jazzy, CUDA 13.2, and TensorRT 10.16 preinstalled, plus GPU passthrough.

To install TensorRT 10.16 with the dev container,

**Prerequisites**: Docker with the NVIDIA Container Toolkit (`--gpus all` support), and VS Code with the "Dev Containers" extension (or the `devcontainer` CLI).

Download the TensorRT tarball from [here](https://developer.nvidia.com/tensorrt/download/10x) and place it in the root of the repo. Ensure that the TensorRT version is compatible with your GPU driver and computer architecture.

1. Open this repo in VS Code → "Reopen in Container" (or `devcontainer up --workspace-folder .`).
2. The workspace is mounted at `/workspace`; `build/`, `install/`, and `log/` are separate Docker volumes so they persist across container rebuilds.
3. `/opt/ros/jazzy/setup.bash` is sourced automatically on shell start; `/workspace/install/setup.bash` is sourced too once it exists (see `entrypoint.sh`).

See [`ffs_depth`'s README](src/ffs_depth/README.md#dev-container) for more container details (base image, GPU/device args, default user).

### 2. Build `camera_models`

```bash
colcon build --packages-select camera_models --cmake-args -DCMAKE_BUILD_TYPE=Release
source install/setup.bash
```

### 3. Build `perception_utils`

```bash
colcon build --packages-select perception_utils --cmake-args -DCMAKE_BUILD_TYPE=Release
source install/setup.bash
```

### 4. Build `ffs_depth`

```bash
colcon build --packages-select ffs_depth --cmake-args -DCMAKE_BUILD_TYPE=Release
source install/setup.bash
```

`ffs_depth` needs a TensorRT engine at runtime, which is not checked into the repo — see [TensorRT engine requirements](src/ffs_depth/README.md#tensorrt-engine-requirements) for how to obtain/export one from Fast-FoundationStereo.

### 5. Export a TensorRT engine

`ffs_depth` needs a TensorRT engine at runtime, which is not checked into the repo. Download the ONNX model (any version, this was tested on 23_36_37_8_iters_320x736):

- [Fast-FoundationStereo ONNX model](https://drive.google.com/file/d/19vkjOQlgmHDDoJ14QjroXn2mCPm64hRY/view?usp=drive_link)

Then compile it into a TensorRT engine with `trtexec`:

```bash
trtexec --onnx=<onnx_file_path> --saveEngine=<trt_path> --useCudaGraph --fp16
```

> **Note:** `--fp16` may not be supported on all x86 machines — if engine build fails or produces bad output, drop the `--fp16` flag and build an fp32 engine instead.

### 6. Launch

```bash
ros2 launch ffs_depth ffs_launch.py engine_path:=/path/to/ffs.trt          # single stereo pair
ros2 launch ffs_depth quad_stereo_launch.py engine_path:=/path/to/quad_ffs.trt  # 4 stereo pairs
```

Each `colcon build` step above can be combined into one `colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release` from the workspace root once you're iterating rather than building the first time. The per-package order above matters because `perception_utils` depends on `camera_models`, and `ffs_depth` depends on both.

## Quad Stereo Depth Estimation

<p align="center">
  <img src="assets/quad_stereo.gif" alt="Quad Stereo Depth Estimation">
</p>

`quad_stereo_node` runs four stereo pairs (`front`, `left`, `back`, `right` — 8 cameras total) through a single batch-4 TensorRT engine, useful for full-surround depth coverage rather than a single forward-facing pair. See [`ffs_depth`'s README](src/ffs_depth/README.md#quad_stereo_node) for the camera/pairing config format. The above dataset was processed into a rosbag from the [Sunny Omnidirectional Dataset by SNU Robot Vision Lab](https://sites.google.com/view/snu-rvlab/research/omnistereo)

To run it, download the batch-4 ONNX model:

- [Fast-FoundationStereo batch-4 ONNX models](https://drive.google.com/drive/folders/1O8V6B17x6fV3xxtqzjwhuqIOhbnULpoo?usp=sharing)

Compile it into a TensorRT engine with `trtexec`, the same way as the single-pair model in [Usage step 5](#5-export-a-tensorrt-engine):

```bash
trtexec --onnx=<onnx_file_path> --saveEngine=quad_ffs.trt --useCudaGraph --fp16
```

> As before, `--fp16` may not be supported on all x86 machines — drop it and build an fp32 engine if the build fails or output looks wrong.

Then launch `quad_stereo_node`, pointing `engine_path` at the engine you just built:

```bash
ros2 launch ffs_depth quad_stereo_launch.py engine_path:=/path/to/quad_ffs.trt
```

When visualising the point clouds from the 4 pairs in Rviz, make sure to set the global frame to "base_link".

## Dependencies

- **ROS2**: Jazzy (`rclcpp`, `std_msgs`, `sensor_msgs`, `message_filters`, `image_transport`, `tf2_ros`)
- **Math/CV**: `OpenCV`, `Eigen3`
- **GPU**: CUDA Toolkit 13.2 (`CUDA::cudart`, `CUDA::nppicc`, `CUDA::nppig`), TensorRT 10.16 (`nvinfer`, `nvinfer_plugin`) — an NVIDIA GPU is required to run `ffs_depth`
- **Internal**: `camera_models`, `perception_utils` (this workspace), consumed by `ffs_depth`
- **Containerized dev environment**: Docker + NVIDIA Container Toolkit (`--gpus all`), VS Code "Dev Containers" extension — see [Usage](#usage)
- **External model**: a TensorRT engine exported from [NVlabs/Fast-FoundationStereo](https://github.com/NVlabs/Fast-FoundationStereo) — not included in this repo, see [Usage step 5](#5-export-a-tensorrt-engine)

## Topics

All topics are published/subscribed by `ffs_depth`'s nodes (`camera_models` and `perception_utils` are libraries with no ROS interface of their own).

### `ffs_depth_node` (single stereo pair)

| Topic | Direction | Type | Notes |
|---|---|---|---|
| `/cam_front_left/image_raw` | Sub | `sensor_msgs/Image` | Remapped to `/fisheye/left/image_raw` in the launch file |
| `/cam_front_right/image_raw` | Sub | `sensor_msgs/Image` | Remapped to `/fisheye/right/image_raw` |
| `/ffs/front/stereo_image` | Pub | `sensor_msgs/Image` (rgb8) | Rectified left/right side-by-side viz; only if `viz_reprojections` is true |
| `/ffs/front/disparity` | Pub | `sensor_msgs/Image` (bgr8) | MAGMA-colorized disparity; only computed if subscribed |
| `/ffs/front/point_cloud` | Pub | `sensor_msgs/PointCloud2` (xyz+rgb) | `frame_id: map`; only computed if subscribed |

### `quad_stereo_node` (4 stereo pairs)

| Topic | Direction | Type | Notes |
|---|---|---|---|
| `/cam0/image_raw` … `/cam3/image_raw` | Sub | `sensor_msgs/Image` | Remapped to `/fisheye/{left,right,bleft,bright}/image_raw` |
| `/quad_stereo/<pair>/disparity` | Pub | `sensor_msgs/Image` (bgr8) | One per pair, `<pair>` ∈ `{front, left, back, right}` |
| `/quad_stereo/<pair>/point_cloud` | Pub | `sensor_msgs/PointCloud2` (xyz+rgb) | `frame_id: <pair>_map` |
| `/tf_static` | Pub | `tf2_msgs/TFMessage` | Static `base_link` → `<pair>_map` transforms, broadcast once at startup |

Full parameter/config details are in [`ffs_depth`'s README](src/ffs_depth/README.md#ros2-interface).

## Performance

| Configuration | Weights | Resolution | Compute | Mean Inference |
|---|---|---|---|---|
| Single Stereo | `23-36-37_8_iters` | 320 x 736 | NVIDIA RTX 5000 Blackwell | 35 ms |
| Quad Stereo | `20-30-48_4_iters` | 320 x 736 | NVIDIA RTX 5000 Blackwell | 140 ms |
| Single Stereo | `23-36-37_8_iters` | 320 x 736 | NVIDIA Jetson AGX Orin | 128 ms |

## Datasets

Coming Soon!

## License

Refer [here](https://github.com/NVlabs/Fast-FoundationStereo?tab=License-1-ov-file).

## Citation

If you use this repository, please cite it:

```bibtex
@misc{praveen2026ros2faststereo,
  author       = {Praveen Elango},
  title        = {{ros2-fast-stereo}: Real-Time TensorRT Stereo Depth Estimation for ROS2},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/praveenelango/ros2-fast-stereo}}
}
```

If you use the stereo-matching model this package runs, please also cite the original Fast-FoundationStereo paper:

```bibtex
@article{wen2026fastfoundationstereo,
  title={{Fast-FoundationStereo}: Real-Time Zero-Shot Stereo Matching},
  author={Bowen Wen and Shaurya Dewan and Stan Birchfield},
  journal={CVPR},
  year={2026}
}
```

Paper: [arXiv:2512.11130](https://arxiv.org/abs/2512.11130) · Code: [NVlabs/Fast-FoundationStereo](https://github.com/NVlabs/Fast-FoundationStereo)

If you use the Sunny Omnidirectional dataset rosbag from SNU Robot Vision Lab, please cite them:

```bibtex
@article{won2020end,
    title={End-to-End Learning for Omnidirectional Stereo Matching with Uncertainty Prior},
    author={Won, Changhee and Ryu, Jongbin and Lim, Jongwoo},
    journal={IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI)},
    year={2020},
}
```

```bibtex
@inproceedings{won2019sweepnet,
    title={Sweepnet: Wide-baseline omnidirectional depth estimation},
    author={Won, Changhee and Ryu, Jongbin and Lim, Jongwoo},
    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
    pages={6073--6079},
    year={2019},
}
```
Dataset: [Omnidirectional Stereo Dataset](https://sites.google.com/view/snu-rvlab/research/omnistereo)

## Acknowledgements

I would like to thank the authors of FastFoundationStereo:
* [Bowen Wen](https://www.linkedin.com/in/bowen-wen/)
* [Shaurya Dewan](https://www.linkedin.com/in/shaurya-dewan-1b07231a2/)
* [Stan Birchfield](https://www.linkedin.com/in/stan-birchfield-9b53762/)

and the authors of the SNU Robot Vision Lab for the Omnidirectional Stereo dataset:
* [Changhee Won](https://www.linkedin.com/in/changhee-won-7140a915b/)
* Jongbin Ryu
* [Jongwoo Lim](https://www.linkedin.com/in/jongwoolim/)
