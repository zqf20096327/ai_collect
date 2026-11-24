# ThinTNPU

**A thin PyTorch inference backend for the YOLO family (Detect / Segment / Classify) on Ascend 310P (`dav-2002`, 310P3 & 310P1).**

**Four generations, three tasks, one shared implementation: YOLOv5 / YOLOv8 / YOLO11 / YOLO26 — Detect, Segment, and Classify — no `torch_npu`.**

ThinTNPU implements PyTorch `PrivateUse1` directly on ACL runtime calls and precompiled Ascend C kernels. Its inference process does not import or link `torch_npu`, and does not load aclnn/TBE or spawn a compiler-worker pool. Single-image FP16 graph replay now beats native `torch_npu` graph capture on measured Ascend 310P3 workloads (~0.79×–0.82× native latency) at roughly 1/5 host memory. It remains a deliberately narrow, inference-only backend, not a general-purpose replacement for the Ascend PyTorch stack.

`WholeBlocked` provides architecture adapters for classic **YOLOv5**, **YOLOv8**, **YOLO11**, and **YOLO26** across **Detect**, **Segment**, and **Classify** heads. Backbone/neck features stay in `NC1HWC0`; head terminals restore `NCHW` (or `[1, nc]` logits/probabilities for Classify). `FrozenGraph` and `ShapeGraphCache` capture the prepared model for fixed-input-contract replay. Optional device-side frontends (`BGRFrontend` and `JPEGFrontend`) fuse preprocessing and `NC1HWC0` packing on-device. Model configuration is frozen; supported image dimensions are capacity-planned, not a hardcoded shape table.

| Family / Task | Architecture integration | Scope |
|---|---|---|
| YOLOv5 Detect | C3, k6 stem, SPPF and classic anchor/objectness Detect | Three detection levels; anchors, classes and strides come from the supplied module. No bundled loader or checkpoint. |
| YOLOv8 Detect | C2f and anchor-free DFL Detect | **3.691 ms** synchronized graph replay at 640² N=1 (**0.79×** historical native `torch_npu` graph). |
| YOLO11 Detect | C3k2/C3k, C2PSA Cube-BMM attention, fused residuals, depthwise-separable Detect | C0-aligned intermediates; **YOLO11n is not supported**. |
| YOLO26 Detect | C3k/PSABlock, residual SPPF, Q-prescaled attention, direct-distance Detect | Fused one-to-one branch, no DFL; device-resident NMS-free selection returns `[1,300,6]` for the measured 640² case. |
| YOLOv8 Segment | Classic three-level `Segment` head, `ConvTranspose2d` → 1×1 + `phase_to_space`, device `bmm_float`, fused `mask_geometry` | `ThinSegmentYOLO` returns owned CPU Ultralytics `Results` (ordinary & retina masks); supports `BGRFrontend` and `EncodedJPEG`. See [SEGMENT_AND_CLASSIFY.md](SEGMENT_AND_CLASSIFY.md). |
| YOLOv8 Classify | `Classify` head with FP32 `global_average`, Cube `bmm_float`, FP32-bias `linear_epilogue`, device softmax | `ThinClassifyYOLO` returns owned CPU Ultralytics `Results` with `probs`. See [SEGMENT_AND_CLASSIFY.md](SEGMENT_AND_CLASSIFY.md). |

## Latest Ascend 310P3 optimization measurements (fast SiLU + Cube BMM + fused residual + device frontend)

Following the October 2026 baseline, four optimization phases added a zero-`Exp`/zero-`Div` FP16 identity fast-SiLU epilogue (`conv_flow`, `conv_c4`, `depthwise_flow`), Cube Mmad BMM paths (`bmm_flow`), fused conv+residual adds (`conv_flow` / `whole_blocked`), non-16-aligned spatial tail fixes, faster `depthwise`/`phase_to_space` kernels, and device-side `BGRFrontend`/`JPEGFrontend` preprocessing.

### Whole-model FP16 N=1 synchronized graph replay (Ascend 310P3)

| Model topology | Input | Latest Thin replay ms | Prior Thin ms | Native `torch_npu` graph ms | Speedup |
|---|---|---:|---:|---:|---|
| YOLOv8s (17 classes) | 640×640 | **3.691** | 4.575 | 4.67 (historical) | **0.79× native (1.265× faster)** |
| YOLOv8m-seg (3 classes) | 224×640 | **5.812** | 10.232 | 7.11 | **0.82× native** (1.76× vs prior Thin) |
| YOLOv8m-seg (3 classes) | 640×640 | **8.273** | 10.867 | — | 1.31× vs prior Thin |
| Classic YOLOv5m (11 classes) | 640×640 | **6.398** | 8.059 | — | 1.26× vs prior Thin |
| YOLO11m (5 classes) | 640×640 | **7.875** | 11.229 | — | 1.43× vs prior Thin |
| YOLO11m (14 classes) | 1280×1280 | **24.970** | 35.472 | — | 1.42× vs prior Thin |

### Key operator speedups (Ascend 310P3)

| Kernel / Workload | Before | After | Improvement |
|---|---:|---:|---:|
| Segment mask BMM `[1,3,32]@[1,32,8960]` | 1,263 µs | **25.4 µs** | **49.7×** |
| Segment mask BMM `[1,10,32]@[1,32,25600]` | 3,583 µs | **35.0 µs** | **102.4×** |
| Classify Linear `[1,1,1280]@[1,1280,1000]` | 5,453 µs | **121.4 µs** | **44.9×** |
| `depthwise_kernel` | baseline | optimized | **-56% to -63%** |
| `phase_to_space_kernel` | baseline | optimized | **-88% to -92%** |

### Device-side preprocessing (`BGRFrontend` & `JPEGFrontend`)

| Pipeline | CPU `LetterBox` + FP16 + H2D | Device `BGRFrontend` (sparse compact + async H2D + `bgr_pack`) | Speedup | Parity vs OpenCV `INTER_LINEAR` + FP16 |
|---|---:|---:|---:|---|
| `2048×2091 → 640×640` | 10.41 ms | **2.77 ms** | **3.76×** | `max_abs = 0.0` (bit-exact) |
| `2048×2091 → 1280×1280` | 39.91 ms | **6.34 ms** | **6.29×** | `max_abs = 0.0` (bit-exact) |

Downscale and equal-size `BGRFrontend` transforms match OpenCV `INTER_LINEAR` + `uint8 -> FP16 * FP16(1/255)` bit-for-bit (`max_abs = 0.0`). `JPEGFrontend` decodes compressed bytes directly via DVPP JPEGD (`ACL_YUVOUT_ALIGN_UP`, subject to DVPP's 8192 px hardware width/height limit) into the same `NC1HWC0` input layout. See [DEVICE_FRONTEND.md](DEVICE_FRONTEND.md).

### Precision contract change (fast SiLU)

Default `conv_flow`, `conv_c4`, and `depthwise_flow` now evaluate fused SiLU using a zero-`Exp` / zero-`Div` FP16 identity approximation:

$$\operatorname{silu}(x) = \max(x, 0) - \frac{|x|}{1 + \exp(\min(|x|, 10.5))}$$

where $\exp(a)$ is approximated in FP16 by a degree-3 polynomial raised to the 8th power (3 squarings) followed by FP16 reciprocal. **Outputs are therefore no longer bitwise identical to earlier exact FP32 `Exp+Div` Thin fixtures.** On end-to-end validation across all anchors, the measured maximum class-confidence difference versus the exact FP32 SiLU baseline is `<= 0.0044`. Within the same build, **`Thin eager == Thin capture == Thin replay` remains strictly bitwise identical**.

## Unified-family capture measurements (October 2026 baseline)

The table below preserves the original October 2026 four-family controlled comparison (prior to fast SiLU, Cube BMM and fused residuals) and its raw datasets in `benchmarks/`:

| Model topology | Thin replay ms | Native graph ms | Thin/native latency |
|---|---:|---:|---:|
| YOLOv8s, 17 classes | **4.57471** | 4.70555 | **0.972×** |
| Classic YOLOv5m, 11 classes | **7.98227** | 6.23399 | **1.280×** |
| YOLO11s, 80 classes | **6.90995** | 6.03161 | **1.146×** |
| YOLO26s, 80 classes, fused one-to-one NMS-free | **9.12324** | 7.18999 | **1.269×** |

The October 2026 baseline was measured on Ascend 310P3, FP16 N=1 input `[1,3,640,640]`, across five fresh-process rounds per family/backend (30 warmups, 101 synchronized samples per round, 40 processes, 4,040 timed samples; odd rounds Thin then native, even rounds reversed). Every sample is retained in [benchmarks/family_capture_640.json](benchmarks/family_capture_640.json). Historical v8 [capture](benchmarks/capture_640.json), [host overhead](benchmarks/host_overhead_reference.json), and [validation](benchmarks/family_validation.json) records remain untouched for historical reference.

## General primitives and architecture adapters

- **Dense & depthwise convolution**: Capacity-derived M/TN/TK tiling, nonresident pointwise weights, k6 stem support, fused residual addition (`conv_flow.cpp`), and multiplier-one C0-aligned k3/s1/p1 depthwise (`depthwise_flow.cpp`). Both 4D NCHW `[1,3,H,W]` and 5D blocked `[1,1,H,W,16]` inputs (from `BGRFrontend`/`JPEGFrontend`) are accepted by the stem. List-valued conv pair attributes (e.g. legacy `padding=[1,1]`) are normalized to tuples in `prepare_model`.
- **Cube & vector BMM (`bmm_flow.cpp`)**: Handles rank-three FP16 operands and blocked-layout attention (`cube_blocked_qk`, `cube_pv_blocked`, `cube_small_m`, `cube_general_3d`) as well as FP32-output `bmm_float` for Segment mask assembly and Classify Linear layers.
- **Segment & Classify primitives**: Non-overlapping square `ConvTranspose2d` lowering via 1×1 conv + `phase_to_space` (`flow_ops.cpp`), fused device `mask_geometry` (`mask_geometry.cpp`), and FP32 `global_average` + `linear_epilogue` (`classify_flow.cpp`).
- **Device selection (`selection_flow.cpp`)**: Device class-max, vector `RpSort16`/`MrgSort`, exact stable top-k prefixes, score/box gather and FP32 output packing for YOLO26.
- **Per-thread kernel loading (`native_launcher.cpp`)**: Wraps Ascend binary registration into `thread_local` handles so independent models on separate threads can capture and replay concurrently on one device within a single process.
- **Device frontends (`device_frontend.cpp`, `resize_csc_kernel.h`, `jpeg_frontend.py`)**: Sparse-row-compacted exact bilinear `BGRFrontend` and DVPP JPEGD `JPEGFrontend` writing directly to `NC1HWC0` graph input buffers.

See [WHOLE_BLOCKED.md](WHOLE_BLOCKED.md), [YOLO_ANCHOR_BASED.md](YOLO_ANCHOR_BASED.md), [YOLO11.md](YOLO11.md), [YOLO26.md](YOLO26.md), [SELECTION_FLOW.md](SELECTION_FLOW.md), [SEGMENT_AND_CLASSIFY.md](SEGMENT_AND_CLASSIFY.md), and [DEVICE_FRONTEND.md](DEVICE_FRONTEND.md).

## Capacity-driven planning, not a shape lookup table

The whole-model path has **no shape lookup table** and no 640-only dispatch. It computes plans from the actual dimensions and L1/UB/L0 capacity constraints. Spatial convolution enumerates legal M/TN/TK tiles, derives input-channel chunks and buffering arrangements from capacity, then ranks candidates using an arithmetic/data-movement cost model. Non-16-aligned spatial tail shapes are handled without the earlier tail performance cliff.

The planner coefficients are **310P3 defaults calibrated in one specific CANN/container environment**, not universal hardware constants. Recalibrate them when changing hardware, drivers or runtime/container environments. [Calibration metadata and coefficients](benchmarks/planner_calibration.json) document the environment, fit and units.

## Scope and accuracy

- External network inputs are allocation-base contiguous FP16 NPU `[1,3,H,W]` (or `[1,1,H,W,16]` from `BGRFrontend`/`JPEGFrontend`), with positive H/W divisible by 32. Capacity, DMA/index ranges and physical memory remain finite; `/32` does not imply unbounded inputs.
- **Bitwise equality means same-revision Thin eager versus Thin capture/replay.** It does not mean CPU FP32 bit-exactness, native-backend equality, or cross-revision equality against pre-fast-SiLU fixtures.
- Training, batch sizes > 1, dictionary/end-to-end segmentation heads, general grouped or dilated convolution, depthwise multiplier > 1, Focus/reorg stems, and YOLO11n remain outside the supported contract.

Read [LIMITATIONS.md](LIMITATIONS.md) before use. In particular, `.data` aliases and untracked output-mode attributes such as `Detect.format` can leave stale prepared/captured state.

## Build

Tested toolchain: aarch64 Linux, CANN 9.0.0 / AscendC, PyTorch 2.8.0+cpu, Python 3.11.15, and Ascend 310P (`dav-2002`, validated on **310P3** and **310P1**). V5/v8/v11/Segment/Classify use Ultralytics 8.3.233 plus separately supplied classic v5 definitions; v26 uses Ultralytics 8.4.189 in a separate frontend environment. The optional native baseline uses `torch_npu` 2.8.0.post1 in an isolated process. Obtain the CANN SDK and model dependencies separately.

```bash
docker run -d --name "$CONTAINER" \
  --device /dev/davinci0 --device /dev/davinci_manager \
  --device /dev/devmm_svm --device /dev/hisi_hdc \
  -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro \
  -v "$PWD:/workspace/ThinTNPU" "$CANN_IMAGE" sleep infinity

docker exec -u 0 "$CONTAINER" bash -c '
  set -eo pipefail
  source /usr/local/Ascend/ascend-toolkit/set_env.sh
  cd /workspace/ThinTNPU
  bash build_all.sh
'
```

Build as container root: CANN kernel merging writes SDK-owned single-object/fatbin directories. `build_all.sh` builds `libthin_backend.so` (including `native_launcher.cpp`), `_region_guard`, `libthin_blocked.so`, `libconv_flow.so`, `libflow_ops.so`, `libbmm_flow.so`, `libdepthwise_flow.so`, `libselection_flow.so`, `libmask_geometry.so`, `libclassify_flow.so`, and `libdevice_frontend.so` from source. Generated binaries are not bundled.

In the container, from the repository root:

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source env.sh
export PYTHONPATH="$PWD:${PYTHONPATH:-}"
export TORCH_DEVICE_BACKEND_AUTOLOAD=0
export YOLO_CONFIG_DIR="$PWD/.yolo-config"
```

Import `thin_backend` before moving tensors to `npu`; do **not** import `torch_npu` into that same process.

## Minimal inference & high-level APIs

Supply model definitions and trusted weights separately under their upstream licenses. No weights, images, or application-specific loaders are bundled.

### CLI examples (Detect)

```bash
python3 examples/infer.py --model /path/to/yolov8s.pt --height 640 --width 640
python3 examples/infer.py --model /path/to/yolo11s.pt --height 640 --width 640
python3 examples/infer_v26.py --model /path/to/yolo26s.pt --height 640 --width 640
```

### Shared low-level API (`FrozenGraph` and `ShapeGraphCache`)

```python
import torch
import thin_backend
from model_optimization import prepare_model
from whole_blocked import WholeBlocked, load_native_flow
from blocked_graph import FrozenGraph, ShapeGraphCache

load_native_flow()
with torch.no_grad():
    model = model.eval().requires_grad_(False).half().to('npu')
    prepare_model(model, fuse_silu=True)
    blocked = WholeBlocked(model)
    blocked.enable()
    # Single fixed shape:
    graph = FrozenGraph(blocked, blocked.run, example_npu_fp16)
    # Or bounded multi-shape residency (first-touch capture up to capacity, eager overflow):
    cache = ShapeGraphCache(blocked, blocked.run, capacity=4)

try:
    with torch.inference_mode():
        output = graph(input_npu_fp16)
        retained = output[0].cpu().clone()
        output_multi = cache(other_shape_npu_fp16)
finally:
    graph.close()
    cache.close()
```

### High-level predictors & device frontends

```python
import cv2
from segment_predictor import ThinSegmentYOLO
from classify_predictor import ThinClassifyYOLO
from jpeg_frontend import BGRFrontend, EncodedJPEG

# Segment (auto-uses BGRFrontend for ndarray when libdevice_frontend.so is built)
seg = ThinSegmentYOLO('/path/to/yolov8m-seg.pt', graph_cache_capacity=4)
bgr = cv2.imread('/path/to/image.jpg', cv2.IMREAD_COLOR)
seg_results = seg.predict(bgr, imgsz=640, half=True, conf=0.25, iou=0.7, retina_masks=False)
jpeg_results = seg.predict(EncodedJPEG('/path/to/image.jpg'), imgsz=640, half=True)
seg.close()

# Classify
cls = ThinClassifyYOLO('/path/to/yolov8m-cls.pt')
cls_results = cls.predict(bgr, imgsz=640, half=True)
cls.close()

# Standalone BGRFrontend -> FP16 NC1HWC0 [1, 1, H, W, 16] on NPU
frontend = BGRFrontend(imgsz=640, stride=32, rect=True)
blocked_x = frontend(bgr)
frontend.synchronize()
frontend.close()
```

Keep the model and wrapper unchanged for the graph's entire lifetime. Low-level graph outputs are borrowed buffers; high-level `ThinSegmentYOLO` and `ThinClassifyYOLO` return owned CPU Ultralytics `Results` objects.

## Verification and comparison

After building with `bash build_all.sh` and sourcing `env.sh`:

```bash
# Core backend, convolution, attention, depthwise, selection
python3 verify_full.py
python3 verify_flow_conv.py
python3 verify_flow_ops.py
python3 verify_anchor_flow.py
python3 verify_anchor_decode.py
python3 verify_materialize.py
python3 verify_bmm_flow.py
python3 verify_bmm_layout.py
python3 verify_depthwise_flow.py
python3 verify_selection_flow.py

# Segment, Classify, Device Frontends, ShapeGraphCache (no checkpoint required)
python3 verify_phase_to_space.py
python3 verify_mask_bmm.py
python3 verify_segment_masks.py
python3 verify_mask_geometry.py
python3 verify_segment_results.py
python3 verify_classify_ops.py
python3 verify_bgr_frontend.py
python3 verify_device_frontend.py
python3 verify_shape_graph_cache.py
```

For checkpoint-backed Segment, Classify, multi-thread concurrency, and four-family capture comparisons, see [SEGMENT_AND_CLASSIFY.md](SEGMENT_AND_CLASSIFY.md), [DEVICE_FRONTEND.md](DEVICE_FRONTEND.md), and [FAMILY_BENCHMARK.md](FAMILY_BENCHMARK.md).

## Source layout

- `thin_backend/`: backend registration and ACL graph wrapper.
- `backend.cpp`, `native_launcher.cpp`, `aten_adapter.cpp`, `ops.cpp`: allocator/runtime, per-thread kernel binary loader, ATen routing and operators.
- `conv_*.cpp`, `cube_layout.h`, `flow_ops.cpp`, `bmm_flow.cpp`, `depthwise_flow.cpp`: convolution, fast-SiLU epilogue, blocked flow (`phase_to_space`), Cube/vector BMM and depthwise kernels.
- `selection_*.h`, `selection_flow.cpp`: stable device selection, gather and final packing (YOLO26).
- `mask_geometry.cpp`, `segment_masks.py`, `segment_predictor.py`: Segment mask BMM/geometry postprocessing and `ThinSegmentYOLO`.
- `classify_flow.cpp`, `classify_predictor.py`: Classify `global_average`/`linear_epilogue` kernels and `ThinClassifyYOLO`.
- `device_frontend.cpp`, `resize_csc_kernel.h`, `jpeg_frontend.py`: `BGRFrontend` and `JPEGFrontend`/`EncodedJPEG`/`JPEGResults`.
- `strided_binary.h`, `strided_concat.h`: general strided elementwise/copy layouts.
- `model_optimization.py`, `whole_blocked.py`: prepared weights and architecture adapters.
- `region_guard.cpp`, `region_contract.py`, `blocked_graph.py`: frozen-state checks, `FrozenGraph`, and bounded `ShapeGraphCache`.
- `verify_*.py`, `examples/`, `benchmark_*.py`: verification suites, minimal examples, and isolated comparisons.

## License

ThinTNPU's own code is licensed under [Apache-2.0](LICENSE). Copyright 2026 maxesisnclaw.

Dependencies and model assets retain their own terms. Ultralytics model classes and forwards for v5/v8/v11/v26 (Detect, Segment, Classify) are subject to upstream AGPL-3.0 or separately obtained commercial terms; this repository's license does not override those obligations. Check the exact upstream revision you use. See [DEPENDENCIES.md](DEPENDENCIES.md).
