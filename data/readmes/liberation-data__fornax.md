<a href="https://fornax4j.org/"><img src="https://raw.githubusercontent.com/liberation-data/fornax/main/website/public/images/splash.jpg" alt="fornax4j: open generative models for the JVM"></a>

# Fornax

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![GitHub stars](https://img.shields.io/github/stars/liberation-data/fornax?style=social)](https://github.com/liberation-data/fornax/stargazers)

<p align="center">
  <a href="https://fornax4j.org/#video" target="_blank">
    <img src="https://raw.githubusercontent.com/liberation-data/fornax/main/website/public/video/explainer-poster.jpg" alt="Watch: Fornax in two minutes (2:31)" width="700">
  </a>
  <br>
  <a href="https://fornax4j.org/#video" target="_blank">▶ Watch Fornax in two minutes</a> (2:31, with captions)
</p>

**Call open-weight models (language, vision, speech, images, songs, video) as plain Java methods, running on your GPU, inside your JVM.**

Try it with one line, with nothing installed but [JBang](https://www.jbang.dev) (from Fornax 0.3.0; JBang fetches a Java
22 or newer if you have none):

```sh
jbang fornax@fornax4j chat qwen3-4b "Write a haiku about a kiln"   # downloads the model on first use
```

`jbang image@fornax4j flux2-klein "a brick kiln at dusk"`, `song@`, `speak@`, `transcribe@`, `see@` and `server@` work the same
way: they are the [`fornax` command](https://fornax4j.org/docs/guides/cli/), run from Maven Central.

> Fornax was called **Kiln** until 0.1.0. Here's what changed:
> - **Maven:** `org.kiln4j:kiln-*` is now `org.fornax4j:fornax-*`.
> - **Packages:** `org.liberationdata.kiln` is now `org.liberationdata.fornax`.
> - **Settings:** `kiln.*` properties are now `fornax.*`, and `KILN_*` environment variables are now `FORNAX_*`.
> - **Studio:** Fornax Studio keeps using an existing `~/.kiln-studio`.

<!-- snippet: Readme#chat -->
```java
try (var llm = new LlamaModel("unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M")) {   // downloaded on first use, then loaded onto the GPU
    llm.chat(List.of(Message.user("Name a country song about a robot.")), Options.DEFAULT, System.out::print);
}
```

**Why:** no overhead between your code and the model.

- **The native runners themselves.** Fornax calls llama.cpp, stable-diffusion.cpp, acestep.cpp, yue2.cpp,
  whisper.cpp and stems.cpp directly. These are the same C/C++ engines the CLIs and servers use, so you get their speed and their model
  support.
- **On the GPU.** Vulkan today (AMD, Intel, NVIDIA). ROCm, CUDA and Metal builds come from the same script.
- **Nothing in between.** A Fornax call is a native function call through Java's Foreign Function & Memory API.
  There is no Python, no model server, no HTTP, no JSON round trip and no second process. Weights stay resident
  between calls, and tokens stream back to a Java callback as they are produced.

Fornax binds native inference engines with Java's Foreign Function & Memory API (Java 22+; Kiln 0.1.0 itself needs 25):

| Module | Engine | Models |
|---|---|---|
| `fornax-llama` | [llama.cpp](https://github.com/ggml-org/llama.cpp) (with `mtmd` for images) | any GGUF language model (Qwen, Llama, Gemma, Mistral, ...); vision language models (Qwen3-VL, PaddleOCR-VL, MedGemma, ...); embedding and reranker models (Qwen3-Embedding, Qwen3-Reranker) |
| `fornax-tts` | [llama.cpp](https://github.com/ggml-org/llama.cpp) (`mtmd`) | text to speech: Kokoro, ZONOS3, LFM3-Audio, Chatterbox, VoxCPM2, ... |
| `fornax-sd` | [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) | FLUX.1/FLUX.2, Qwen-Image and Qwen-Image-Edit, SD 1.x/2.x/XL/3, Wan, LTX |
| `fornax-acestep` | [acestep.cpp](https://github.com/ServeurpersoCom/acestep.cpp) | ACE-Step 1.5 songs (vocals, lyrics, up to several minutes) |
| `fornax-yue2` | [yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp) | YuE2 songs |
| `fornax-whisper` | [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | speech to text with word timings: Whisper large-v3-turbo, base.en, any ggml Whisper |
| `fornax-demucs` | [stems.cpp](https://github.com/betweentwomidnights/stems.cpp) | stem separation (vocals and backing, or drums, bass, other, vocals): HTDemucs v4, 6-stem and fine-tuned |

Images and songs work the same way, and a vision language model takes images in:

<!-- snippet: Readme#models -->
```java
try (var songs = new AceStepModel("ace-step")) {   // a catalogue set: its four files, downloaded on first use
    songs.generate(requestJson).audio().writeWav(new File("song.wav"));
}

try (var images = new DiffusionModel(DiffusionModel.Config.builder().model("flux2-klein").build())) {
    BufferedImage img = images.generate(new DiffusionModel.Request("a neon sign", 1024, 1024, 20, 4.0, 7)).get(0);
}

try (var vlm = new LlamaModel(LlamaModel.Weights.QWEN3_VL_4B)) {   // the GGUF plus its mmproj (vision encoder)
    String invoiceJson = vlm.extract(List.of(Message.user("Read this invoice.", Image.read(Path.of("invoice.png")))),
            invoiceSchema, Options.DEFAULT.withTemperature(0));      // constrained to a JSON schema
}
```

`DiffusionModel` also edits: a `Request` can carry reference images (Qwen-Image-Edit, FLUX.2), an init image and
strength (img2img), a mask (inpainting), a ControlNet hint and LoRAs. `Upscaler` runs ESRGAN models. See the
[images guide](https://fornax4j.org/docs/guides/images/).

## Getting started

Fornax is on Maven Central as `org.fornax4j`. Add an engine module (`fornax-llama`, `fornax-tts`, `fornax-sd`, `fornax-acestep`,
`fornax-yue2`, `fornax-whisper` or `fornax-demucs`) and the **natives jar** for your platform, which holds the engines' native libraries.

The quickest start is [`samples/hello-fornax`](samples/hello-fornax): a standalone app for Gradle and Maven that streams
a chat reply from Qwen3 4B. Copy it out and run `./gradlew run` or `mvn -q compile exec:java`.

The natives jars:

| Natives artifact | Platform | GPU backend |
|---|---|---|
| `fornax-natives-linux-x86_64-vulkan` | Linux x86-64 (glibc 2.39+: Ubuntu 24.04, Fedora 40 or newer) | Vulkan (AMD, Intel, NVIDIA) |
| `fornax-natives-macos-aarch64-metal` | macOS 13.3+ on Apple silicon | Metal |

No Windows natives jar yet: `native/build.sh` builds the engines in MSYS2's UCRT64 shell, experimentally
([#83](https://github.com/liberation-data/fornax/issues/83)).

On Linux, the GPU's Vulkan driver must be installed (it usually is; if not, see
[Installing GPU drivers](https://fornax4j.org/docs/gpu-drivers/)). With no GPU, Fornax stops rather than run on the CPU,
unless `-Dfornax.allowCpu=true` (or `FORNAX_ALLOW_CPU=true`).

Maven: import the BOM, then add modules without versions. `fornax-natives` brings in the natives jar for the machine
that builds (Maven activates its profiles by OS and arch):

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.fornax4j</groupId>
            <artifactId>fornax-bom</artifactId>
            <version>0.2.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>org.fornax4j</groupId>
        <artifactId>fornax-llama</artifactId>
    </dependency>
    <dependency>
        <groupId>org.fornax4j</groupId>
        <artifactId>fornax-natives</artifactId>
        <type>pom</type>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

Gradle (`build.gradle.kts`), which doesn't run Maven's profiles, so it names the natives jar for the machine that builds:

```kotlin
val fornaxNatives =
    if (System.getProperty("os.name").startsWith("Mac")) "macos-aarch64-metal" else "linux-x86_64-vulkan"

dependencies {
    implementation(platform("org.fornax4j:fornax-bom:0.2.0"))
    implementation("org.fornax4j:fornax-llama")
    runtimeOnly("org.fornax4j:fornax-natives-$fornaxNatives")
}
```

Run with `--enable-native-access=ALL-UNNAMED`. The first time an engine loads, Fornax extracts its library from the
natives jar into a per-version cache (`~/.cache/fornax/<version>/` on Linux, `~/Library/Caches/fornax/<version>/` on
macOS; move it with `-Dfornax.cache.dir`) and loads it from there.

**Choosing a backend.** Each natives jar is one platform and one GPU backend, so the jar you add is the choice.
Natives jars for different platforms can sit side by side (to ship one build for every platform, add both);
Fornax loads the one for the machine it runs on. If jars for several backends of the same platform are on the
classpath, `-Dfornax.backend=vulkan` (or `FORNAX_BACKEND`) picks one; otherwise Fornax prefers Metal, then CUDA, HIP and
Vulkan. For ROCm (HIP), CUDA or anything else, build the libraries yourself (see [Building](#building)) and point
`-Dfornax.library.path` at them, which always wins over a natives jar
([Set up on your platform](https://fornax4j.org/docs/platforms/) has the steps).

## Quick start (from source)

The fastest way to see Fornax work: build the engines and run the demo. One Java program has Qwen3 4B write a
country song, ACE-Step 1.5 sing it and FLUX.2 [klein] paint its cover, all in one JVM.

```sh
native/build.sh vulkan            # or hip | cuda | metal | cpu (see Building)
./gradlew single                  # writes single/single.wav, single/cover.png and single/lyrics.txt
```

The first run downloads the three models into the Hugging Face cache, logging each file; later runs need no network.
To fetch them ahead of time, run `fornax pull qwen3-4b`, `fornax pull ace-step-turbo` and `fornax pull flux2-klein`,
or `hf download` (the files are listed under [Models](#models)).
To try models without writing code, use [Fornax Studio](https://github.com/liberation-data/fornax-studio).

## Status

Early. Everything below runs from Java on Linux with an AMD Radeon 8060S (Ryzen AI Max+ 395 "Strix Halo",
128 GB unified memory) using the **Vulkan** backend:

| Model | Result |
|---|---|
| Qwen3 4B Instruct (Q4_K_M) | ~75 tokens/s, streamed through a Java callback: as fast as llama.cpp's own `llama-bench` |
| Qwen3-Embedding 0.6B (Q8_0) | ~420 embeddings/s (20-token passages, 256 to a batch), matching `llama-embedding`'s vectors (cosine 1.000000) |
| Qwen3-VL 4B Instruct (Q4_K_M) | a 1000×1300 invoice to schema-checked JSON (vendor, date, 4 line items, totals) in ~6 s; images read in 0.4 to 1.6 s, then ~60 tokens/s |
| PaddleOCR-VL 1.6 (0.9B) | the same invoice's text (prompt "OCR:") in ~1.5 s, ~200 tokens/s |
| MedGemma 1.5 4B (Q4_K_M) | the same invoice to JSON in ~6 s (Gemma 3 vision: 256 tokens an image, read in ~0.8 s) |
| ACE-Step 1.5 XL turbo | a 3 min 20 s song in 57 s |
| ACE-Step 1.5 turbo | a 60 s song in ~15 s |
| YuE2 3B (Q8_0) | a 60 s song in ~60 s |
| Whisper large-v3-turbo (q5_0) | 55 s of speech in 1.8 s (31× real time, 60 words/s) with DTW word timings, beam 5 |
| HTDemucs v4 (F32) | a 3 min 9 s song split into four stems in 26 s (7.3 s of audio per second; about 2.9 on the CPU) |
| FLUX.2 [klein] base 4B (fp8) | 768×768, 12 steps in ~130 s |
| Qwen-Image 2512 (fp8) | 1024×1024, 20 steps in ~13 min |

[Benchmarks](https://fornax4j.org/docs/benchmarks/) sets these against each engine's own tool and against ComfyUI, with
the command behind every figure.

The build script also knows the **ROCm (HIP)**, **CUDA** and **Metal** backends of the underlying engines. HIP passes
the test suite on the same machine (one rerank score drifts,
[#80](https://github.com/liberation-data/fornax/issues/80)) and has run LTX-2.5 video there (about 2.7× faster per
step than Vulkan, and the way to render long clips; see
[engine notes](docs/engine-notes.md)), and Metal passes the test suite on an Apple M2 Max with 32 GB (macOS 27.2: chat, vision, embeddings and reranking, speech,
transcription, stem separation, FLUX.2 [klein] images and upscaling, isolated workers and Dispatch; songs and video
haven't been run on a Mac yet). Intel Macs aren't supported. CUDA hasn't been tested yet. The Java code is the same for every backend: you pick one when you
build the native libraries. Reports and fixes welcome.

## How it works

Each engine is built into **one self-contained shared library** with its ggml linked in statically and kept
private. The engines pin different ggml versions, so this is what lets several of them share one process.

- `stable-diffusion.cpp` has a key/value C API, so `fornax-sd` binds it directly.
- `llama.cpp` has a C API too, but it passes structs by value and is mid-migration to a new batch API, so
  `fornax-llama` binds a small stable C layer (`fornax-llama/native`) instead.
- `acestep.cpp` and `yue2.cpp` are C++ only, so each gets a ~100-line C layer: JSON request in, PCM audio out.
- `whisper.cpp` has a C API, but it passes two large parameter structs by value, so `fornax-whisper` binds a small C
  layer (`fornax-whisper/native`) that takes plain arguments and a small struct of its own, and reads results back token
  by token.
- `stems.cpp` has a C ABI of size-tagged structs in a function table, so `fornax-demucs` binds a small C layer
  (`fornax-demucs/native`) over it: planar audio in, planar stems out.

Engine quirks and how to debug them: [docs/engine-notes.md](docs/engine-notes.md).

Every model class is `AutoCloseable`; weights are freed on `close()`, which is idempotent and safe while a call runs.
A model takes calls from any thread and runs them one at a time (a language model loaded with
[slots](https://fornax4j.org/docs/guides/language-models/#many-requests-at-once-slots) runs several together, in one
batch). The blocking methods run on your thread; the
`...Async` ones (`chatAsync`, `speakAsync`, `generateAsync`, ...) run on the model's own platform thread and return a
`CompletableFuture`, so virtual threads never pin a carrier through a generation, and streaming goes to a
`Flow.Subscriber` through a bounded buffer. `cancel()` works for every engine, and a callback that throws stops the
call and rethrows instead of crashing the JVM. See [Threading](https://fornax4j.org/docs/guides/threading/).

A native crash (a failed `GGML_ASSERT`, a segfault, a malformed GGUF) still takes the JVM down in-process, so Fornax
can also run a model in a **worker process**, opt-in: `LlamaModel.isolated(gguf)`, or `-Dfornax.isolation=process` for
every `LlamaModel`. It is the same `LlamaModel`, with the same blocking, async, streaming and cancel API. A crash fails
the call in flight with a `WorkerCrashedException`, and the next call restarts the worker and reloads the model. It
costs about 15 µs a call and a microsecond a streamed token. See [Isolation](https://fornax4j.org/docs/guides/isolation/).

`ModelPool` keeps models resident between uses, the way ComfyUI does: it unloads idle models least recently used
first to stay within a memory budget, optionally unloads after an idle timeout, and gives each model one user at a
time (or as many as its slots).

For servers, `Dispatch` serves many models from a few worker processes: it routes each request to the worker that
already has its model loaded, loads models on demand within one memory budget (least recently used out first), queues
requests as `INTERACTIVE` or `BATCH` with aging so batch work can't starve, and reloads a crashed worker's models
elsewhere. `qwen.submit(QoS.INTERACTIVE, llm -> llm.chatAsync(messages, options))`. See
[Dispatch](https://fornax4j.org/docs/guides/dispatch/).

`LlamaModel.chatJson` does OpenAI-style chat with **tool calling**, using the model's own chat template and
tool-call format (the same templates and parsers as llama-server): messages and tools in OpenAI's format in, a
message with `content`, `reasoning_content` and `tool_calls` out. A `json_schema` in the request constrains the reply
to that schema.

Loaded with an mmproj GGUF, a `LlamaModel` is a vision language model, through llama.cpp's `mtmd` (as `llama-mtmd-cli`
and `llama-server --mmproj` run them): `Message.user(text, images...)` with `Image.of(BufferedImage)`,
`Image.read(Path)` or `Image.decode(bytes)`; `chat`, `chatJson` and `extract` (a reply constrained to a JSON schema)
all take images. `LlamaModel.Weights` names the models Fornax has been tried with.

Loaded in `Mode.EMBED` or `Mode.RERANK`, a `LlamaModel` is an embedding model or a reranker, through llama.cpp's
pooled embeddings output (as `llama-embedding` and `llama-server --embedding` / `--reranking` run them), for search
over your own documents (RAG) with no vector database: `fornax-core`'s `Vectors.topK` scans the vectors in memory.

<!-- snippet: Readme#search -->
```java
try (var emb = new LlamaModel(LlamaModel.Weights.QWEN3_EMBEDDING_0_6B, LlamaModel.Mode.EMBED)) {
    float[][] docs = emb.embed(passages);                                       // L2-normalised, batched
    float[] q = emb.embed(List.of(question), EmbedOptions.query("Given a question, retrieve passages that answer it"))[0];
    List<Scored> nearest = Vectors.topK(q, docs, 20);
}
try (var rr = new LlamaModel(LlamaModel.Weights.QWEN3_RERANKER_0_6B, LlamaModel.Mode.RERANK)) {
    List<Scored> best = rr.rerank(question, candidates);                        // best first
}
```

## Building

Needs JDK 25, CMake, Ninja, a C++17 compiler, and the SDK for your GPU backend
(Vulkan: the Vulkan headers, `glslc` and SPIRV-Headers; on Fedora `dnf install vulkan-headers vulkan-loader-devel glslc spirv-headers-devel`).

```sh
native/build.sh vulkan            # or hip | cuda | metal | cpu; optionally list engines: llama tts sd acestep yue2 whisper demucs
./gradlew build
```

`native/build.sh` clones the engines at the commits pinned in `native/engines.properties` into `engines-src/`,
applies Fornax's patches from `native/patches/` (when a pin or a patch changes, it first resets that engine's tracked
files and its submodules', so keep no edits of your own there), and writes the libraries to
`build/native/<os>-<arch>-<backend>/`.
The Gradle build points the examples and tests at that folder; pick another backend with `-Pfornax.backend=hip`.
Without it, `./gradlew build` still compiles every module and runs the tests that need no engine library and no
model (the rest skip themselves): what CI runs on every pull request (`.github/workflows/ci.yml`), along with a
canary that publishes to a local repository and builds `samples/hello-fornax` against it.
The integration tests skip any model that isn't downloaded; `scripts/test-models.sh` fetches the ones they use
(about 20 GB, small enough for a 32 GB machine).

From Linux, `./gradlew testOnMac -Pfornax.macHost=<host>` (or `scripts/test-on-mac.sh <host>`) runs the tests on a Mac
over SSH against Metal: it copies the working tree there, builds the Metal libraries, runs `./gradlew test` and brings
the reports back to `build/mac-test/` (Gradle arguments go after the host, or in
`-Pfornax.macTestArgs='--tests *LlamaModelIT'`). The Mac needs Xcode's command-line tools, JDK 25, CMake and Ninja.

To use your own build in an application, put the libraries on `-Dfornax.library.path=<dir>` (or `FORNAX_LIBRARY_PATH`,
or the platform loader path) and run with `--enable-native-access=ALL-UNNAMED`; an explicit path wins over a
natives jar. Set `FORNAX_VERBOSE=1` to see the
engines' own logs.

On a power-limited GPU (for example a laptop on battery), a single long GPU dispatch can exceed the driver's
compute timeout and lose the device. Fornax decodes ACE-Step audio in 512-frame tiles to avoid that; tune it with
`FORNAX_ACESTEP_VAE_CHUNK`.

## Models

Fetch a model with `fornax pull <alias>`. To get the `fornax` command, install Fornax Studio and choose
**Install fornax command** from its menu (coming in the next Fornax Studio release), or build it from source (see
[The fornax command](#the-fornax-command)).

```sh
fornax pull qwen3-4b        # chat
fornax pull flux2-klein     # an image model: diffusion model, VAE and text encoder, from three repos
fornax list                 # every alias, what is downloaded, and other GGUF models in the cache
```

The aliases are Fornax's model catalogue (`ModelCatalog`): `qwen3-0.6b`, `qwen3-4b`, `qwen3-vl-4b`, `paddleocr-vl`,
`medgemma-4b`, `kokoro`, `whisper-large-v3-turbo`, `whisper-base.en`, `flux2-klein`, `qwen-image`, `qwen-image-edit`,
`ace-step-turbo`, `ace-step`, `ace-step-xl-turbo`, `ace-step-xl`, `yue2`, `ltx-2.5-distilled` and `ltx-2.5-dev`.
`fornax pull` also takes a repo (`fornax pull unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M`, or file names and globs).

Files go to the Hugging Face cache (`HF_HUB_CACHE`, `HF_HOME/hub` or `~/.cache/huggingface/hub`), in the layout
`hf download` uses. There is one cache: `fornax`, `hf`, Fornax Studio and your own app all see the same files, and nothing
is downloaded twice. Fornax also finds weights in a ComfyUI models folder (`FORNAX_MODEL_DIRS`).

From Java, the same thing is `FornaxHub`, in `fornax-core`: `FornaxHub.standard().pull(ModelCatalog.require("flux2-klein"),
listener)` fetches a model's missing files with resume, SHA-256 checks, progress, and a token for gated repos; it also
reports what is on disk and evicts a model's files. Or pass file paths directly. See
[Downloading models](https://fornax4j.org/docs/guides/models/).

Or fetch the files with the Hugging Face CLI:

```sh
hf download unsloth/Qwen3-4B-Instruct-2507-GGUF Qwen3-4B-Instruct-2507-Q4_K_M.gguf
hf download Qwen/Qwen3-VL-4B-Instruct-GGUF Qwen3VL-4B-Instruct-Q4_K_M.gguf mmproj-Qwen3VL-4B-Instruct-Q8_0.gguf
hf download PaddlePaddle/PaddleOCR-VL-1.6-GGUF PaddleOCR-VL-1.6-GGUF.gguf PaddleOCR-VL-1.6-GGUF-mmproj.gguf
hf download Qwen/Qwen3-Embedding-0.6B-GGUF Qwen3-Embedding-0.6B-Q8_0.gguf
hf download ggml-org/Qwen3-Reranker-0.6B-Q8_0-GGUF qwen3-reranker-0.6b-q8_0.gguf
hf download Serveurperso/ACE-Step-1.5-GGUF acestep-5Hz-lm-4B-Q8_0.gguf Qwen3-Embedding-0.6B-Q8_0.gguf \
    acestep-v15-turbo-Q8_0.gguf vae-BF16.gguf
hf download Serveurperso/YuE2-GGUF YuE2-3B-Q8_0.gguf YuE2-Vae-F32.gguf
hf download ggerganov/whisper.cpp ggml-large-v3-turbo-q5_0.bin ggml-base.en.bin
hf download thepatch/htdemucs-GGUF htdemucs-42M-v1.0-F32.gguf
hf download black-forest-labs/FLUX.2-klein-base-4b-fp8 flux-2-klein-base-4b-fp8.safetensors
hf download Comfy-Org/flux2-dev split_files/vae/flux2-vae.safetensors
hf download Comfy-Org/z_image_turbo split_files/text_encoders/qwen_3_4b.safetensors
```

## The fornax command

`fornax` fetches models and tries them without writing any code:

```sh
fornax pull qwen3-4b                              # an alias: every file the model needs
fornax pull unsloth/Qwen3-4B-Instruct-2507-GGUF   # lists the repo's GGUF models and asks which
fornax pull bartowski/google_gemma-3-4b-it-GGUF:Q4_K_M
fornax list                                       # the catalogue, what is downloaded, sizes
fornax rm flux2-klein                             # delete a model's files from the cache
fornax chat qwen3-4b "Write a haiku about a fornax"
fornax chat qwen3-4b                              # interactive; /reset, /exit
fornax image flux2-klein "a brick kiln at dusk"   # -> image.png; --width --height --steps --cfg --seed --out
fornax song ace-step-turbo "acoustic folk, warm vocal" --lyrics words.txt --seconds 60   # -> song.wav
fornax speak "Hello from Fornax"                  # kokoro -> speech.wav; --voice, --list-voices
fornax transcribe speech.wav                      # whisper-base.en; --words for each word's times
fornax see qwen3-vl-4b image.png "What is by the door?"
fornax server -m qwen3-4b                         # an OpenAI-compatible API at http://127.0.0.1:54154/v1
fornax test flux2-klein                           # load, generate a little, report speed
fornax info                                       # Java, native libraries, cache, token
```

Every command that runs a model downloads it first if it isn't in the cache yet, as `fornax pull` would. `image`, `song`
and `speak` write to `--out` (else `image.png`, `song.wav` or `speech.wav` here, numbered rather than overwrite one).
A reasoning model's `<think>` blocks (Qwen3's) are hidden in `fornax chat`; `--think` shows them. A gated repo
(LTX-2.5) needs its terms accepted on huggingface.co and `HF_TOKEN` (or `hf auth login`); the error says so.

**Installing it.** Fornax Studio installs `fornax` onto your `PATH` from its menu, **Install fornax command**, using
Studio's own Java and engines (coming in the next Fornax Studio release). On a machine without a desktop, such as a
server, build it from source: it needs JDK 25 to build and Java 22 or newer to run (`JAVA_HOME`, or `java` on
`PATH`).

```sh
native/build.sh vulkan                          # the engines (or -Pfornax.cli.nativesVersion=0.2.0, below)
./gradlew :fornax-cli:installDist                 # -> fornax-cli/build/install/fornax-cli/{bin,lib}
export PATH="$PWD/fornax-cli/build/install/fornax-cli/bin:$PATH"
```

The distribution's `lib/` holds the natives jar of each platform built in `build/native/`; with
`-Pfornax.cli.nativesVersion=0.2.0` it takes this platform's from Maven Central instead. `FORNAX_LIBRARY_PATH` points it
at other native libraries. The launcher, `bin/fornax`, takes its Java, its jars and its natives from `FORNAX_JAVA`,
`FORNAX_CLI_LIB` and `FORNAX_LIBRARY_PATH`, or from placeholders an installer fills in; see
[The fornax command](https://fornax4j.org/docs/guides/cli/).

Check each model's license before you use what it makes. Some are non-commercial: YuE2's weights are
CC BY-NC 4.0, for example.

## The OpenAI-compatible server

*On `main`, shipping in 0.3.0; not in 0.2.0.*

`fornax server` (or `FornaxServer`, in the `fornax-server` module, JDK only) serves Fornax's models over an
OpenAI-compatible HTTP API, so any OpenAI client, agent framework or tool can use them with no Java code:

```sh
fornax server -m qwen3-4b
curl -s localhost:54154/v1/chat/completions -d '{"messages":[{"role":"user","content":"Hi"}]}'
```

<!-- snippet: OpenAiServer#readme -->
```java
try (var server = FornaxServer.builder().model("qwen3-4b").build().start()) {
    server.await();   // OpenAI base URL: server.url(), http://127.0.0.1:54154/v1
}
```

It serves `POST /v1/chat/completions` (streaming, tools and `tool_calls`, `response_format` JSON schemas, `stop`,
images for a vision model), `GET /v1/models`, `POST /v1/embeddings`, `POST /v1/images/generations` (base64 PNGs),
`POST /v1/audio/speech` (WAV) and `POST /v1/audio/transcriptions` (a WAV file). A request may name the `-m`
models and catalogue models already downloaded (with `--allow-downloads`, any model Fornax loads: alias,
`org/name:TAG` or path, downloaded on first use), kept loaded in a `ModelPool` within `--budget-gb`. It listens on 127.0.0.1, refuses a foreign `Host` (DNS rebinding) and web pages unless `--cors`
allows their origin, and with `--api-key` needs `Authorization: Bearer`. See
[OpenAI-compatible server](https://fornax4j.org/docs/guides/openai-server/).

## Examples

```sh
./gradlew single    # three engines, one JVM: an LLM writes a song, ACE-Step sings it, FLUX.2 klein paints the cover
./gradlew chat --args='"Write a haiku about a fornax"'
./gradlew song --args='song.wav'                         # -Pdit=xl-turbo for the larger model
./gradlew yue2 --args='yue2-song.wav'
./gradlew speak --args='out.wav "Hello from the JVM" bm_george'   # -Pmodel=zonos3|lfm3-audio|chatterbox-turbo|...
./gradlew transcribe --args='audio.wav'                  # prints the text; writes audio.words.tsv and audio.srt
./gradlew separate --args='song.wav'                     # writes song-vocals.wav and song-backing.wav; --all for every stem
./gradlew image --args='klein out.png "a neon sign that says FORNAX"' -Psteps=12 -Pwidth=768 -Pheight=768
./gradlew see --args='photo.jpg "What is in this picture?"'      # -Pmodel=qwen3-vl-4b|paddleocr-vl|medgemma-4b
./gradlew see --args='form.png "Fill in the fields."' -Pschema=schema.json   # a reply that follows a JSON schema
./gradlew invoice   # draws a made-up invoice and reads it into JSON; -Pmodel=paddleocr-vl reads it with OCR first
./gradlew defects   # a tray of parts with a dented one: Qwen3-VL boxes the defects (out/defects-found.png)
./gradlew edit --args='in.png out.png "the same street in snow"' -Pstrength=0.6   # img2img; -Pmask=m.png inpaints
./gradlew edit --args='in.png out.png "make the sign say FORNAX"' -Pmodel=qwen-edit -Plora=lightning.safetensors:1 -Psteps=4 -Pcfg=1
./gradlew upscale --args='in.png out.png'                # RealESRGAN_x4plus: 4x
./gradlew search --args='docs "Why does a long video lose the GPU on Vulkan?"'   # embed, find and rerank passages in a folder
```

The song examples use the requests in `fornax-examples/src/main/resources/requests/`; pass your own JSON as a
second argument. The request formats are the engines' own (see
[acestep.cpp](https://github.com/ServeurpersoCom/acestep.cpp) and [yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp)).

## Fornax Studio

`fornax-studio-server` is the backend of [Fornax Studio](https://github.com/liberation-data/fornax-studio), a desktop app for
trying models: a JDK-only HTTP server on localhost (`com.sun.net.httpserver`, replies streamed as server-sent events)
that lists what in the Hugging Face cache Fornax can run, downloads Fornax's model sets into it (`FornaxHub`), keeps
models in a `ModelPool`, and serves chat (with a tool-calling demo through `chatJson`), images, songs (ACE-Step and
YuE2), video clips with sound (LTX-2.5, whose .mp4 needs ffmpeg) and questions about an image for a vision model
(Qwen3-VL, PaddleOCR-VL, MedGemma), as text or held to a JSON schema. The app starts it; to run it on its own:

```sh
./gradlew studioServer                    # http://127.0.0.1:5191; -Pport=, -Pbudget=<GB>, -Pstub=image,song,video
./gradlew :fornax-studio-server:studioJar   # one runnable jar, which the app ships
```

It answers only its own callers: a request whose `Host` isn't `127.0.0.1`, `localhost` or `[::1]` at its port (DNS
rebinding), or that carries an `Origin` (a web page in the browser), is refused with a 403. When `FORNAX_STUDIO_SECRET`
is set in its environment (the app makes one each launch), every route but `/api/health` also needs it in the
`X-Fornax-Studio-Secret` header.

On Linux, as with every Fornax engine, a GPU build refuses to load a model on a machine with no usable GPU (the request's
error says what to install) unless `FORNAX_ALLOW_CPU=true` is set in the server's environment.

## Roadmap

- Test and document the CUDA build, and songs and video on Metal; natives jars for HIP and CUDA.
- Video through stable-diffusion.cpp (`sd_generate_video`: Wan, LTX).
- `fornax-embabel`: an Embabel Agent `LlmService` and `LocalModelSource` (needs tool-call parsing in `fornax-llama`).
- An MLX module for Apple silicon, through `mlx-c`.
- A Kotlin layer with coroutine `Flow` streaming.

## License

Apache 2.0. The engines Fornax builds against are MIT-licensed; see [NOTICE](NOTICE).
