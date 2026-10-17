# Inferno

A Rust inference engine made with the sole purpose of running the latest larger
models on an HPE ProLiant DL580 Gen9. It reads GGUF weights, distributes CPU work
across NUMA nodes, and optionally uses CUDA. The primary platform is Linux on
x86-64 with AVX2/FMA.

Implemented architectures: `llama`, `qwen35`, `qwen35moe`, and `glm5next`.
Architecture support does not imply compatibility with every model or
quantization. The GLM path includes concurrent slots, a shared prefix cache,
optional disk persistence, DFlash2 drafting, and vision through a separate mmproj.

## Build and run

Use a current stable Rust toolchain and Cargo. Download models separately;
weights are not included. CUDA dynamically loads the NVIDIA driver
(`libcuda.so.1`) and NVRTC (`libnvrtc.so.13`, `.12`, or `.so`).
Use `--no-gpu` for an explicit CPU run.

```sh
cargo build --release --locked
scripts/fetch-test-model.sh
target/release/inferno inspect models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf
target/release/inferno run models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf \
  -p 'Once upon a time,' -n 32 -t 8 --no-gpu
```

Running `inferno` without arguments prints usage and exits with status 2.
Add `--numa` to distribute weight rows and pin workers to NUMA nodes.
Budget memory for weight copies, per-sequence state, and caches.

## API

The server provides OpenAI-compatible `/v1/models` and `/v1/chat/completions`
endpoints, including SSE streaming. Create a file containing your API key,
restrict its permissions to 0600, and run:

```sh
target/release/inferno serve /path/to/model.gguf \
  --model-id local-model --listen 127.0.0.1:8082 \
  --api-key-file /path/to/api-key -t 8 --no-gpu
```

Features depend on the architecture; validate concurrent slots, vision, and
drafting on GLM5Next. Vision accepts image `data:` URIs, not remote URLs.
`--cache-dir` saves prompt state on clean SIGTERM/SIGINT shutdown; protect
that directory as you would the input conversations.

## Development and measurement

Run `cargo test --release --locked`. Tests requiring local model fixtures or
GPU hardware may return early; a passing suite alone does not validate those
paths. Synthetic GGUF generators in `scripts/make-tiny-*.py` require Python,
NumPy, and the `gguf` package.

`inferno bench` measures memory bandwidth, kernels, and dispatch overhead;
`run --timers` reports model phase timings. See [CONTRIBUTING.md](CONTRIBUTING.md)
for validation, [docs/releasing.md](docs/releasing.md) for public snapshots, and [docs/architecture.md](docs/architecture.md) for design and limits.

## Release status

This is development version 0.1.0. Support performance claims with reproducible
measurements specifying the model, configuration, and revision. Inferno is authored by **Jan Imrich** and licensed under [MIT](LICENSE),
including commercial use. Model weights, dependencies and model-derived
fixtures retain their own terms; see [THIRD_PARTY.md](THIRD_PARTY.md).
Model weights and operational data are not distributed here.
