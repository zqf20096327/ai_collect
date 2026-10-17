# DLSS-G Stream Worker

An open-source Windows worker that runs NVIDIA DLSS Frame Generation on offline
RGBA frame sequences. It exposes a small binary stdin/stdout protocol designed
for ComfyUI and other local video tools.

The worker owns the D3D12 device, uploads color and motion-vector textures,
invokes the NGX Frame Generation feature, reads generated frames back to system
memory, and keeps the GPU session alive for the full sequence.

## Status

Version 0.1.0 is an experimental release. It has been built with Visual Studio
2022 and tested on Windows 11 with an RTX 5090 and DLSS-G runtime 310.9.0.
The 2x path completed the included 512×512 smoke test: three source frames
produced three worker responses, each containing one finite, nonzero generated
RGBA frame. The first response is intentionally discarded by clients because
there is no preceding source frame.

This is an unofficial project. It is not an NVIDIA product and does not contain
`nvngx_dlssg.dll` or the NVIDIA DLSS SDK.

## Requirements

- Windows 10 2004 or newer; Windows 11 is recommended
- NVIDIA GPU and driver supported by the supplied DLSS-G runtime
- Hardware-accelerated GPU scheduling (HAGS)
- Visual Studio 2022 with the C++ desktop workload
- CMake 3.25 or newer
- A local checkout of the [NVIDIA DLSS SDK](https://github.com/NVIDIA/DLSS)
- A legally obtained `nvngx_dlssg.dll` placed beside `dlssg-worker.exe`

NVIDIA distributes the SDK and runtime under its own terms. Read the license in
the NVIDIA repository before downloading, building, or distributing a binary.

## Build

```powershell
git clone https://github.com/NVIDIA/DLSS.git NVIDIA-DLSS
cmake -S . -B build -A x64 -DDLSS_SDK_DIR="C:/path/to/NVIDIA-DLSS"
cmake --build build --config Release
ctest --test-dir build -C Release --output-on-failure
```

The executable is written to `build/Release/dlssg-worker.exe`. Copy your
compatible `nvngx_dlssg.dll` into the same directory before running a probe.

```powershell
build\Release\dlssg-worker.exe --probe
```

A successful probe returns one JSON object on stdout. Diagnostics go to stderr
so they cannot corrupt the binary stream.

## GPU smoke test

The test client needs NumPy:

```powershell
python tests/smoke_client.py build/Release/dlssg-worker.exe
```

It sends three synthetic moving frames through the persistent worker. This
checks initialization, feature creation, texture upload, NGX evaluation,
readback, and protocol framing. It does not measure visual quality.

## ComfyUI-DLSS5

Copy these files into `ComfyUI-DLSS5/runtime/dlssg/`:

```text
dlssg-worker.exe
nvngx_dlssg.dll
```

Restart ComfyUI and run `DLSS Frame Generation Status` before processing video.
The protocol remains compatible with ComfyUI-DLSS5 v0.3.0.

## Input limitations

The v1 stream carries RGBA8 color and RG16F motion vectors. It does not carry a
real depth buffer or camera matrices. The worker supplies constant depth and
identity camera transforms to satisfy the NGX interface. This makes the worker
useful for offline video interpolation, but it cannot match a game integration
that receives accurate geometry, camera, HUD-less color, and optical-flow data
from the renderer.

The next protocol revision will add optional depth and camera metadata without
breaking existing v1 clients.

## Safety

The worker does not access the network, launch child processes, or write output
frames to disk. It loads NVIDIA's NGX core and `nvngx_dlssg.dll` through the
official NGX loader. Only run runtime DLLs whose origin and hash you trust.

See [SECURITY.md](SECURITY.md) for reporting instructions and
[docs/PROTOCOL.md](docs/PROTOCOL.md) for the wire format.

## License

The original worker source is MIT licensed. NVIDIA SDK headers, static
libraries, runtime DLLs, drivers, and model files are separate works governed by
NVIDIA's terms. They are neither relicensed nor redistributed here.

