# Awesome Inference Engines [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Inference engines and execution systems for large language models, from portable local runtimes to highly specialized GPU kernels and distributed model serving.

The focus is **where and how model computation happens**: hardware, supported model families, quantization, KV and recurrent-state management, memory tiering, batching, and serving architecture. A model manager or API proxy is useful, but it is not automatically an independent inference engine; those projects have their own section.

This is a curated technical reference, not a leaderboard. Performance claims should be evaluated against matching model weights, workloads, hardware, and correctness. Specialized engines can be outstanding within a narrow envelope and unsuitable outside it.

For specific hardware, model, and memory constraints, see the [source-backed compatibility matrix](compatibility.md). For measurements you can reproduce on your own system, use the [streaming benchmark probe](bench/README.md). The matrix reports upstream claims; the probe does not imply that an engine has been independently tested.

## Contents

- [Choose by hardware and workload](#choose-by-hardware-and-workload)
- [Specialized and model-specific engines](#specialized-and-model-specific-engines)
- [Apple Silicon inference](#apple-silicon-inference)
- [General-purpose local inference](#general-purpose-local-inference)
- [Production and high-throughput serving](#production-and-high-throughput-serving)
- [On-device, edge, and browser inference](#on-device-edge-and-browser-inference)
- [Execution libraries and kernel foundations](#execution-libraries-and-kernel-foundations)
- [Servers, frontends, and orchestration](#servers-frontends-and-orchestration)
- [Benchmarks and related lists](#benchmarks-and-related-lists)
- [Evaluating performance claims](#evaluating-performance-claims)

## Choose by hardware and workload

**CPU or mixed CPU/GPU, GGUF:** Start with llama.cpp, ik_llama.cpp, or llama-cpp-turboquant. Check offload, quantization, context memory, and CPU bandwidth.

**Apple Silicon, broad coverage:** Explore mlx-lm, MLX Swift LM, llama.cpp, vLLM Metal, and Magnitude. Check macOS/Metal requirements, unified memory, and batch size.

**Apple Silicon, specialized agents:** Explore Kapitsa, Espetero, TensorFold, Rapid-MLX, rMLX, Splash, and rec. Check supported checkpoints, image input, and tool calls.

**Apple Silicon, native Swift:** Explore MLX Swift LM, swama, and SwiftLM. Distinguish embeddable libraries from standalone servers.

**Apple Silicon, native MTP decoding:** Explore MTPLX for models with multi-token-prediction heads. Check model-pack support, unified-memory requirements, and measured benefit over plain decoding.

**Apple Silicon, speculative decoding:** Explore mlx-dspark for DSpark/DFlash and lookup-based speculation on MLX models, or Splash for DFlash 2 on its supported families. Check drafter compatibility, quantization, and workload-specific acceleration.

**Consumer NVIDIA GPUs:** Explore ExLlamaV3, llama.cpp, Paddock, Magnitude, and RustingStrata. Match checkpoint format, CUDA generation, and KV-cache precision.

**Large MoE beyond VRAM:** Explore Strata, FreeToken, Project Maya, KTransformers, atomic-engine, and Magnitude. Expert residency and PCIe/SSD transfer costs dominate.

**Blackwell-specific local engines:** Explore Basalt, NInfer, Infernix, Hyperflare, and squid5090. Confirm compute capability, CUDA version, and model packs.

**AMD Strix Halo:** Explore Gufo. Confirm the exact Ryzen AI MAX target and ROCm setup.

**AWS Trainium:** Explore TrnRT. Confirm the Neuron SDK, instance type, and supported checkpoints.

**Multi-user or distributed serving:** Explore vLLM, SGLang, RTP-LLM, TensorRT-LLM, and TokenSpeed. Measure throughput, TTFT, and tail latency together.

**Phones, browsers, and embedded devices:** Explore LiteRT-LM, ONNX Runtime GenAI, ExecuTorch, MNN, and WebLLM. Check model conversion, memory, power, and accelerator delegates.

These are **starting points**, not universal recommendations. Verify platform and model compatibility in the linked project's documentation.

## Specialized and model-specific engines

These projects deliberately optimize a narrower combination of model architecture, hardware, or memory layout. Fork lineage matters: a distinctive fork is not necessarily a new engine from scratch.

- [Avalon](https://github.com/freriadoc/Avalon) - Fork of llama.cpp tuned for Qwen3.8-Flash-Next, with host/GPU expert caching and an emphasis on AMD/ROCm.
- [Basalt](https://github.com/jesdga95/basalt) - Blackwell-focused local engine with Qwen and DeepSeek model paths and host-resident MoE experts.
- [DeepInfer](https://github.com/deepseek-ai/DeepInfer) - DeepSeek's model-specific offline inference framework with optimized kernels, expert parallelism, asynchronous scheduling, and DSpark verification.
- [DeepSeek Ultrafast](https://github.com/basetenlabs/deepseek-ultrafast) - Rust and CUDA engine for DeepSeek-V4.1-Flash on NVIDIA B200, B300, and GB300, with block draft-and-verify decoding, 1M-context serving, and RDMA KV-cache sharing; check its **Elastic License 2.0 / source-available terms**.
- [FreeToken](https://github.com/FlashML-org/FreeToken) - Edge-native MoE serving engine with CPU/GPU co-execution, expert caching, and elastic memory allocation.
- [Gufo](https://github.com/gufo-org/gufo) - Native engine tailored to AMD Strix Halo, spanning language and additional modalities.
- [Hyperflare](https://github.com/NVIDIA/hyperflare-inference) - NVIDIA research prototype for local serving on SM120/SM121 GPUs and DGX Spark, with a Rust runtime, planned memory and conversation state, and no Python on the serve path.
- [Infernix](https://github.com/BarachielFallen/infernix) - NInfer-derived C++/CUDA engine tuned for Qwen-family inference on RTX 50-series hardware.
- [KTransformers](https://github.com/kvcache-ai/ktransformers) - Heterogeneous CPU/GPU inference and kernel framework aimed at large models and MoE workloads.
- [NInfer](https://github.com/Neroued/ninfer) - C++/CUDA engine for selected models on RTX 5090 and DGX Spark, including speculative decoding and multi-device paths.
- [PolyStrata](https://github.com/simplexai-labs/PolyStrata) - Combines upstream Strata execution with separate backends for additional model families.
- [Project Maya](https://github.com/mw00/project-maya) - Strata-derived, model-specialized engine targeting large GLM, DeepSeek, and MiniMax-family models.
- [Speedy](https://github.com/DevDock-AI/Speedy) - Strata-derived MoE runtime tuned for consumer NVIDIA GPUs and agent workflows; check its **personal/non-commercial license**.
- [squid5090](https://github.com/tensorfish/squid5090) - Zig and sm_120a CUDA engine for Inkling-2-Mini text and vision serving on NVIDIA RTX 5090-class GPUs, with an OpenAI-compatible HTTP server.
- [Strata](https://github.com/Niko1221/Strata) - Heterogeneous local MoE inference using GPU, CPU, host memory, and SSD expert tiers.
- [Sync-Strata](https://github.com/hiruhiru2005/sync-strata) - Strata fork with dedicated Qwen3.8-Flash-Next model packs and quantization work.
- [TensorFold](https://github.com/ashhart/TensorFold) - Native Zig engine with direct Metal, CUDA, and Vulkan execution paths and speculative decoding.
- [TrnRT](https://github.com/RunAnywhereAI/trnrt) - Open AWS Trainium2 serving engine with NKI megakernels, prefix caching, and an OpenAI-compatible API, currently focused on GLM-5.3-Flash.
- [Xolotl](https://github.com/Indras-Mirror/Xolotl) - Substantially extended Strata descendant for large MoE models on consumer NVIDIA hardware.
- [yasaheni](https://github.com/sahenjp/yasaheni) - Linux and GGUF input port of the YASAKANI engine.
- [YASAKANI](https://github.com/yasakani-dev/yasakani) - Windows/NVIDIA model-specific CUDA engine, principally optimized for Qwen3.8-27B.

## Apple Silicon inference

- [Espetero](https://github.com/JarJarFran/espetero) - Native C++/Metal runtime supporting concurrent text, vision, and classification requests.
- [Kapitsa](https://github.com/nace-ai/kapitsa) - Apple Silicon-native inference engine for selected model families and local coding-agent use.
- [libmlxforge](https://github.com/hvasconcelos/libmlxforge) - Embeddable C++/MLX LLM engine with continuous batching and a C ABI; its HTTP server is a testing harness.
- [lithos-metal](https://github.com/lithos-ai/lithos-metal) - Open-source native Metal engine with mixer megakernels, GPU-resident generation control, and DSpark speculative decoding.
- [MLX](https://github.com/ml-explore/mlx) - Apple Silicon array-compute framework used to build inference engines; **not a standalone LLM server**.
- [MLX Swift LM](https://github.com/ml-explore/mlx-swift-lm) - Swift-native LLM/VLM inference library on MLX, providing model implementations, generation, quantized-model support, and fine-tuning.
- [mlx-dspark](https://github.com/ARahim3/mlx-dspark) - MLX-native Apple Silicon inference engine with DSpark, DFlash, and lookup speculative decoding, target-model token verification, and OpenAI/Anthropic-compatible serving.
- [mlx-lm](https://github.com/ml-explore/mlx-lm) - General-purpose LLM inference and fine-tuning on the MLX framework.
- [mlx-serve](https://github.com/ddalcu/mlx-serve) - Native Zig-backed Apple Silicon runtime and Swift app for local language and multimodal model serving through several API formats.
- [mlx-vlm](https://github.com/Neywa-Labs/mlx-vlm) - Vision-language inference and model utilities on MLX.
- [MTPLX](https://github.com/youssofal/MTPLX) - Apple Silicon MLX-based runtime with custom Metal kernels and native multi-token-prediction speculative decoding, plus OpenAI/Anthropic-compatible serving.
- [oMLX](https://github.com/jundot/omlx) - MLX-based inference server with continuous batching and tiered, persistent KV caching.
- [Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) - Apple Silicon MLX serving engine with continuous batching, prefix caching, agent tool-call support, and OpenAI/Anthropic-compatible APIs.
- [rec](https://github.com/recursive-oss/rec) - Apple Silicon engine for Recursive Flint models, targeting M4/M5 Pro and Max machines with at least 48 GB of unified memory.
- [rMLX](https://github.com/Pushkinist/rMLX) - Rust-native, single-binary MLX inference server for Apple Silicon with multimodal generation and quantized KV-cache options.
- [Splash](https://github.com/incoai/splash) - Apple Silicon engine for selected model families, with specialized Metal kernels, DFlash 2 speculative decoding, automatic memory planning, and OpenAI/Anthropic-compatible serving on macOS 26.4+.
- [swama](https://github.com/Trans-N-ai/swama) - Swift/MLX local inference runtime for language, vision, embeddings, and speech with an OpenAI-compatible server and menu bar app.
- [SwiftLM](https://github.com/SharpAI/SwiftLM) - Native Swift/MLX inference server for Apple Silicon with OpenAI-compatible serving and optional SSD-streamed MoE experts.
- [TurboFieldfare](https://github.com/drumih/turbo-fieldfare) - Swift/Metal, Gemma 4-specific engine that streams routed experts from SSD to reduce resident memory.
- [vLLM Metal](https://github.com/vllm-project/vllm-metal) - Apple Silicon plugin for vLLM, with MLX as a primary compute backend.

## General-purpose local inference

- [atomic-engine](https://github.com/AtomicBot-ai/atomic-engine) - Fork of llama-cpp-turboquant (itself a llama.cpp fork) with memory-budgeted serving and SSD expert streaming for large MoE models, plus an OpenAI-compatible server.
- [BitNet](https://github.com/microsoft/BitNet) - Specialized runtime for BitNet-family 1-bit and low-bit model architectures.
- [ExLlamaV3](https://github.com/turboderp-org/exllamav3) - Consumer-GPU inference library with EXL3 quantization, batching, CPU offload, and parallelism.
- [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) - Performance-oriented llama.cpp fork with additional quantization and CPU/hybrid optimizations.
- [Kinetic](https://github.com/Veloresearch/kinetic) - Rust GGUF runtime for Windows and Linux, running supported models on CPU, NVIDIA CUDA, or Vulkan, with an OpenAI-compatible server.
- [llama-cpp-turboquant](https://github.com/TheTom/llama-cpp-turboquant) - Fork of llama.cpp adding TurboQuant low-bit KV-cache types and WHT-rotated or ConvRot weight quantization on CPU, CUDA, Metal, Vulkan, and SYCL.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - Portable C/C++ model execution with GGUF, broad quantization, and diverse CPU/GPU backends.
- [Magnitude](https://github.com/magnitudedev/magnitude) - Local GGUF engine that tiers MoE experts across GPU, RAM, and SSD, with automatic per-chip kernel tuning on Apple Silicon, NVIDIA, AMD, and Intel.
- [mistral.rs](https://github.com/EricLBuehler/mistral.rs) - Rust inference runtime for local accelerated and quantized language/multimodal models.
- [MLC-LLM](https://github.com/mlc-ai/mlc-llm) - Compiler and runtime deployment stack targeting multiple hardware platforms.
- [ONNX Runtime GenAI](https://onnxruntime.ai/docs/genai/) - Generation runtime built on ONNX Runtime, handling token sampling, search, KV caching, and model-specific generation across execution providers.
- [Paddock](https://github.com/truespar/paddock) - Native Rust inference engine with in-tree CUDA and Metal kernels, paged KV caching, and GGUF/safetensors loading; Apple Silicon support targets macOS 26+ and is pre-release.
- [PowerInfer](https://github.com/Tiiny-AI/PowerInfer) - Local CPU/GPU heterogeneous LLM inference with activation-aware execution.
- [RustingStrata](https://github.com/RustingStudio/RustingStrata) - Pure-Rust GGUF engine (not a Strata fork) with runtime-compiled CUDA or Vulkan kernels, overlapping CPU/GPU MoE experts, and an OpenAI/Anthropic-compatible server; check its **RustingStrata License 1.0**.

## Production and high-throughput serving

- [FastDeploy](https://github.com/PaddlePaddle/FastDeploy) - Paddle ecosystem inference and serving stack with optimized model execution backends.
- [LightLLM](https://github.com/ModelTC/LightLLM) - High-throughput LLM inference and dynamic request scheduling.
- [LMDeploy](https://github.com/InternLM/lmdeploy) - Serving and deployment toolkit including the TurboMind inference engine.
- [Mini-SGLang](https://github.com/sgl-project/mini-sglang) - Compact, runnable SGLang-style serving engine and readable reference for radix caching, chunked prefill, and tensor-parallel execution.
- [RSInfer](https://github.com/open-agent-infra/RSInfer) - Production serving engine for NVIDIA SM100 with hot-reloadable schedulers and kernels, aimed at live agent-driven engine modification without full restarts.
- [RTP-LLM](https://github.com/alibaba/rtp-llm) - Alibaba's production LLM inference engine with custom CUDA kernels, dynamic batching, prefix caching, and disaggregated prefill/decode execution.
- [SGLang](https://github.com/sgl-project/sglang) - High-performance generation and serving with request scheduling, prefix caching, and structured output.
- [Sonar](https://github.com/dphnAI/sonar) - vLLM-derived inference engine formerly named Aphrodite Engine.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA-optimized LLM execution with kernel, quantization, batching, and multi-GPU capabilities.
- [TokenSpeed](https://github.com/lightseekorg/tokenspeed) - Production serving engine for agentic workloads, with a C++ control plane, Python execution plane, and a pluggable kernel layer including Blackwell MLA implementations.
- [vLLM](https://github.com/vllm-project/vllm) - Model-serving engine with continuous batching and paged KV-cache management.
- [vLLM-Ascend](https://github.com/vllm-project/vllm-ascend) - Hardware plugin extending vLLM serving to Ascend accelerators.
- [vLLM-Omni](https://github.com/vllm-project/vllm-omni) - Multimodal generation and serving within the vLLM ecosystem.

## On-device, edge, and browser inference

- [ExecuTorch](https://github.com/pytorch/executorch) - PyTorch-native on-device execution stack for mobile, wearable, embedded, and other edge hardware.
- [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) - Google's cross-platform, on-device LLM runtime built on LiteRT for mobile, desktop, web, and embedded systems.
- [MNN](https://github.com/alibaba/MNN) - Lightweight mobile and embedded neural-network runtime with LLM deployment support.
- [ncnn](https://github.com/Tencent/ncnn) - Mobile-focused neural-network inference framework with CPU and GPU backends.
- [TensorRT Edge-LLM](https://github.com/NVIDIA/TensorRT-Edge-LLM) - NVIDIA edge-device framework for optimized LLM inference.
- [Transformers.js](https://github.com/huggingface/transformers.js) - Browser and JavaScript runtime for Transformer models using web-compatible execution backends.
- [WebLLM](https://github.com/mlc-ai/web-llm) - Browser-based LLM inference engine using WebGPU.

## Execution libraries and kernel foundations

These are **building blocks**, not necessarily complete inference servers. They matter because several engines share or extend their computation primitives.

- [Candle](https://github.com/huggingface/candle) - Rust tensor framework with efficient local model inference implementations.
- [CTranslate2](https://github.com/OpenNMT/CTranslate2) - Optimized Transformer inference runtime, widely useful for translation and speech workloads.
- [FlashInfer](https://github.com/flashinfer-ai/flashinfer) - GPU attention, GEMM, and MoE kernel library and generator for inference engines.
- [IREE](https://github.com/iree-org/iree) - Compiler and runtime for portable accelerator execution of ML models.
- [ML Drift](https://github.com/google-ai-edge/ml-drift) - Google AI Edge on-device GPU inference framework and successor to the TFLite GPU delegate, with OpenCL, Metal, WebGPU, and OpenGL ES backends; **not a standalone LLM server**.
- [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai) - Intel-oriented generative AI runtime APIs and optimized model pipelines.
- [Resin](https://github.com/ekzhang/resin) - Experimental Rust scheduler and KV-cache library for building model-specific inference engines, with pluggable CUDA and MLX runners; **not a standalone LLM server**.

## Servers, frontends, and orchestration

An API endpoint, cluster scheduler, or model manager can be indispensable without being the component that computes tokens. This separation prevents backend wrappers from being mistaken for independent engines.

- [Dynamo](https://github.com/ai-dynamo/dynamo) - Distributed inference serving infrastructure coordinating backend execution and data movement.
- [exo](https://github.com/exo-explore/exo) - Distributed local inference across personal devices with automatic peer discovery.
- [Goethe](https://github.com/meshapplied/goethe) - Self-hosted OpenAI-, Anthropic-, and LiteLLM-compatible gateway with optional kernel packs that otherwise fall back to SGLang, then llama.cpp.
- [KoboldCpp](https://github.com/LostRuins/koboldcpp) - Integrated llama.cpp-derived runtime and server, especially for story and roleplay use cases.
- [llama-swap](https://github.com/mostlygeek/llama-swap) - Local proxy that starts and swaps underlying model servers on demand.
- [llm-d](https://github.com/llm-d/llm-d) - Kubernetes-native architecture for distributed LLM serving.
- [LocalAI](https://github.com/mudler/LocalAI) - Self-hosted multi-backend inference API for many model families and runtimes.
- [Ollama](https://github.com/ollama/ollama) - Local model packaging, management, and serving with embedded execution backends.
- [Ray Serve](https://github.com/ray-project/ray) - Distributed application-serving framework that orchestrates inference workloads.
- [TabbyAPI](https://github.com/theroyallab/tabbyAPI) - OpenAI-compatible serving frontend for ExLlamaV3.
- [Triton Inference Server](https://github.com/triton-inference-server/server) - Multi-backend production inference-serving infrastructure, distinct from TensorRT-LLM.

## Benchmarks and related lists

- [Awesome Inference Specialization](https://github.com/SJTU-iBDS-Lab/awesome-inference-specialization) - Research-oriented index of specialized inference execution systems.
- [Awesome LLM Inference Engine](https://github.com/sihyeong/Awesome-LLM-Inference-Engine) - Survey-based taxonomy of serving engines, systems, and optimization techniques.
- [Awesome Local AI](https://github.com/janhq/awesome-local-ai) - Broad local AI ecosystem, beyond runtime implementations.
- [Awesome Local LLM](https://github.com/rafska/awesome-local-llm) - Local model execution platforms, inference engines, and development tools.
- [Awesome Local LLMs](https://github.com/vince-lam/awesome-local-llms) - Local LLM repository discovery and related ecosystem projects.
- [InferenceX](https://github.com/SemiAnalysisAI/InferenceX) - Open benchmark platform and AgentX agentic-trace harness for comparing production inference servers; inspect each result's hardware and workload context.
- [LlamaPerf Engines](https://llamaperf.com/engine) - Community-submitted engine performance results; inspect each result's measurement context.
- [LLM Repos](https://llmrepos.com) - Repository discovery and project growth tracking.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) - Community announcements and experiments; treat reported performance as leads for verification.

## Evaluating performance claims

Compare engines against the **same workload and quality constraints**, not just a headline token rate:

**Model and artifact:** Model ID, revision, quantization, tokenizer, context configuration, and speculative-draft weights.

**Hardware and software:** GPU and driver, CPU, RAM, interconnect, SSD, OS, engine version, and build flags.

**Request:** Prompt length, filled context, output length, modality, warm/cold prefix state, and concurrency.

**Performance:** Time to first token, prefill throughput, decode throughput, end-to-end completion time, tail latency, peak memory, and energy when available.

**Reliability:** Tool-call validity, structured-output compliance, long-context behavior, numerical fidelity, and repeatability.

**Evidence:** Reproduction command, raw per-run data, sample size, variance, and exact benchmark artifacts.

An engine may improve speed by changing quantization, skipping computations, using speculative decoding, or narrowing model support. These are different tradeoffs; record them explicitly. Source repositories document claimed capabilities, **not independent validation of every claim**.

For earlier generations, maintenance-mode, and archived engines, see [historical engines](historical.md).

## Contributing

See [contributing.md](contributing.md) to propose an engine, update a description, or correct a model/hardware claim. Original implementations and genuinely useful forks are welcome; unsupported performance claims and duplicate wrappers are not.
