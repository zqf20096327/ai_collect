<p align="center">
  <img src="docs/banner.svg" width="820" alt="Pithos CORE: language models in x86-64 assembly, on Linux and bare metal">
</p>

<p align="center">
  <b>LiquidAI language models in x86-64 NASM, on Linux and as a standalone operating system.</b><br>
  LFM3-1.7B and LFM2.5-350M with no libc, booting from BIOS or UEFI into a Unicode chat console.
</p>

<p align="center">
  <img alt="NASM x86-64 assembly" src="https://img.shields.io/badge/NASM-x86--64%20assembly-7c5cf6">
  <img alt="Runtime with no libc and no Python" src="https://img.shields.io/badge/runtime-no%20libc%2C%20no%20Python-ec5c8c">
  <img alt="Runs on Linux and on bare metal with BIOS or UEFI" src="https://img.shields.io/badge/runs%20on-Linux%20%7C%20bare%20metal%20BIOS%20%26%20UEFI-f5a05a">
  <a href="#lfm3-17b-the-main-model"><img alt="Model LFM3-1.7B Q4_K_M" src="https://img.shields.io/badge/model-LFM3--1.7B%20Q4__K__M-6366f1"></a>
  <a href="#lfm25-350m-the-compact-model"><img alt="Model LFM2.5-350M BF16" src="https://img.shields.io/badge/model-LFM2.5--350M%20BF16-8b5cf6"></a>
  <img alt="AVX2 and FMA, up to 16 CPUs" src="https://img.shields.io/badge/SIMD-AVX2%20%7C%20FMA%2C%20up%20to%2016%20CPUs-14b8a6">
  <a href="#console-and-commands"><img alt="Console with Unicode, colour emoji and 13 keyboard layouts" src="https://img.shields.io/badge/console-Unicode%2C%20colour%20emoji%2C%2013%20layouts-6b7280"></a>
  <a href="#verification"><img alt="Verified against Transformers" src="https://img.shields.io/badge/verified-against%20Transformers-2ea043"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-2ea043"></a>
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/benmaster82/Pith_OS?color=3b82f6">
</p>

<p align="center">
  <a href="#build-and-usage">Quick start</a> ·
  <a href="#pithos-core-in-qemu-from-cd-or-usb">Boot from CD or USB</a> ·
  <a href="#console-and-commands">Console</a> ·
  <a href="#boot-options-and-limits">Options and limits</a> ·
  <a href="#keyboard-layouts">Keyboard layouts</a> ·
  <a href="#performance">Performance</a> ·
  <a href="lfm3/README.md">LFM3 internals</a> ·
  <a href="README.it.md">Italiano</a>
</p>

![Pithos CORE running LFM3-1.7B: chat with Chinese, Japanese, Korean and colour emoji](docs/screenshots/pithos-core-chat.png)

Pithos CORE runs LiquidAI LFM3-1.7B, the main model, from its Q4_K_M GGUF, and LFM2.5-350M, the compact model, from its official BF16 weights. Each model has a Linux executable and a standalone kernel that boots from BIOS or UEFI, from CD or a USB stick, uses up to 16 CPUs and offers a Unicode graphical console and a serial port. The BPE tokenizer, AVX2/FMA kernels, parallel workers, block prefill, sampling and chat commands are shared. The runtime needs neither libc nor Python. An independent project, inspired by llm.asm, not a fork.

## LFM3-1.7B: the main model

The runtime quantizes every matrix input to Q8_K and computes integer products with the Q4_K and Q6_K rows of the GGUF, as ggml does. It implements the sandwich norm, seven-tap short convolutions, attention with a 256-position sliding window, partial RoPE and per-head output gates. Its answers match an FP32 reference built on the official `modeling_lfm3.py`; the details are in [lfm3/README.md](lfm3/README.md).

### Build and usage

The build needs NASM, GNU ld, GNU make 4.3 or later and Python 3 with the tokenizers package. The GGUF and the official tokenizer files come from Hugging Face.

~~~sh
hf download LiquidAI/LFM3-1.7B-GGUF LFM3-1.7B-Q4_K_M.gguf --local-dir weights
hf download LiquidAI/LFM3-1.7B tokenizer.json tokenizer_config.json chat_template.jinja --local-dir lfm3-ref
make lfm3 LFM3_MODEL=weights/LFM3-1.7B-Q4_K_M.gguf LFM3_TOKENIZER=lfm3-ref/tokenizer.json
./build/lfm3/lfm3-next weights/LFM3-1.7B-Q4_K_M.gguf --chat 256
./build/lfm3/lfm3-next weights/LFM3-1.7B-Q4_K_M.gguf --text 128 "Write two sentences about Turin."
~~~

The options are `--chat [N]`, `--text N "prompt"`, `--generate N ID ...`, `--encode` and `--decode`; `LFM_THREADS` selects 1 to 16 threads and `LFM_CONTEXT` 1 to 32,768 positions. The `build/lfm3/tokenizer.bin` tables must stay next to the executable.

### Pithos CORE in QEMU, from CD or USB

~~~sh
make lfm3-os-image LFM3_MODEL=weights/LFM3-1.7B-Q4_K_M.gguf LFM3_TOKENIZER=lfm3-ref/tokenizer.json OS_KEYMAP=us
python3 os/run.py --iso build/lfm3/pithos-core.iso --cpus 4 --display gtk
python3 os/run.py --iso build/lfm3/pithos-core.iso --uefi --usb --cpus 4 --display gtk
~~~

`build/lfm3/pithos-core.iso`, about 1.13 GB, is a hybrid GRUB image for BIOS and UEFI that can be written raw to a USB stick. It holds the kernel, the unchanged GGUF and the tokenizer tables; after boot the kernel works entirely in RAM. The image opens the chat with 1,024 tokens per answer, an 8,192-position context and up to six CPUs ([options and limits](#boot-options-and-limits)); `OS_KEYMAP` sets the default keyboard layout. It needs 2 GiB of RAM below 4 GiB and a CPU with AVX2, FMA and F16C; Secure Boot must be disabled.

#### Booting a real PC

Pithos CORE has booted on a real laptop, in UEFI mode from a USB stick, with the built-in keyboard working. To write the stick on Windows, open the ISO in [Rufus](https://rufus.ie), press Start and, when Rufus detects an ISOHybrid image, choose **Write in DD Image mode**: ISO mode rebuilds the boot files with Rufus's own and may not start. On Linux, `sudo dd if=build/lfm3/pithos-core.iso of=/dev/sdX bs=4M conv=fsync status=progress`, where `/dev/sdX` is the whole stick, not a partition; everything on it is erased.

On the target machine, disable Secure Boot and pick the stick from the firmware boot menu (often F12, F11, F8 or Esc). Loading the 1.1 GB module takes a while before the console appears. The keyboard is read through the PS/2 controller: laptop keyboards are usually wired that way, while USB keyboards need the firmware's legacy USB emulation (often "USB Legacy Support" or CSM). Without it the chat still appears but does not accept keys.

### Boot options and limits

The ISO embeds its kernel options in `grub.cfg`; they are chosen when the image is built, through make variables that apply to either model:

| Option | Make variable | LFM3 default | LFM2.5 default | Meaning |
| --- | --- | --- | --- | --- |
| `tokens=` | `OS_TOKENS` | 1,024 | 512 | maximum tokens per answer, reasoning included; at most the context |
| `context=` | `OS_CONTEXT` | 8,192 | 4,096 | positions for the whole conversation: system prompt, history and answers; 1 to 32,768 |
| `threads=` | `OS_THREADS` | 6 | 6 | CPUs used, 1 to 16, never more than the machine has |
| `keymap=` | `OS_KEYMAP` | `us` | `us` | keyboard layout, see below |

~~~sh
make lfm3-os-image LFM3_MODEL=weights/LFM3-1.7B-Q4_K_M.gguf LFM3_TOKENIZER=lfm3-ref/tokenizer.json OS_TOKENS=2048 OS_CONTEXT=16384 OS_KEYMAP=it
~~~

Changing a variable rebuilds only the ISO. The FP32 KV cache takes 44 KiB per position with LFM3 and 24 KiB with LFM2.5, and must fit in the RAM below 4 GiB next to the model; if it does not, the kernel stops at boot with an error.

| Context | LFM3 cache | LFM2.5 cache |
| --- | --- | --- |
| 4,096 | 176 MiB | 96 MiB |
| 8,192 | 352 MiB | 192 MiB |
| 16,384 | 704 MiB | 384 MiB |
| 32,768 | 1.4 GiB | 768 MiB |

With 2 GiB of RAM, LFM3 reaches about 20,000 positions; 32,768 needs 3 GiB. During the chat two notices refer to these limits:

- *Response reached the token limit. The assistant turn was closed.* The answer used all its tokens and was cut. `/set tokens 2048` raises the limit up to the context size, without rebooting.
- *Context full. Use /clear or reboot with a larger context= value.* The conversation filled the context. `/clear` starts a new one; a larger `OS_CONTEXT` gives longer conversations.

The status line and `/stats` show the context in use, for example `ctx 220/8192`.

### Keyboard layouts

Pithos CORE has thirteen keyboard layouts generated from the XKB data, with Shift, AltGr, Caps Lock and dead keys:

| Code | Layout | Code | Layout | Code | Layout |
| --- | --- | --- | --- | --- | --- |
| `us` | US English (default) | `es` | Spanish | `se` | Swedish |
| `uk` | UK English | `pt` | Portuguese | `fi` | Finnish |
| `it` | Italian | `br` | Brazilian ABNT2 | `no` | Norwegian |
| `de` | German | `ch` | Swiss German | `dk` | Danish |
| `fr` | French AZERTY | | | | |

The layout the image starts with is chosen when it is built, through `OS_KEYMAP`; the same variable applies to both models:

~~~sh
make lfm3-os-image LFM3_MODEL=weights/LFM3-1.7B-Q4_K_M.gguf LFM3_TOKENIZER=lfm3-ref/tokenizer.json OS_KEYMAP=it
make lfm3-os-image LFM3_MODEL=weights/LFM3-1.7B-Q4_K_M.gguf LFM3_TOKENIZER=lfm3-ref/tokenizer.json OS_KEYMAP=de
make os-image MODEL=weights/model.safetensors OS_KEYMAP=fr
~~~

With `os/image.py` the layout is a kernel option, for example `--options "mode=chat tokens=1024 context=8192 threads=6 keymap=es"`. Once booted, `/keymap uk` switches the layout during the chat without restarting; the current layout is shown at the end of the status line. Rebuilding with a different `OS_KEYMAP` only regenerates the ISO, not the kernel or the bundle.

### Console and commands

The console shows the Pithos mark, the model, the conversation with word wrapping, and a status line with generation and prompt speed, time to first token, context, decoding, reasoning, cores and keyboard layout. Chinese, Japanese, Korean and colour emoji appear on screen; the keyboard follows thirteen layouts (us, uk, it, de, fr, es, pt, br, ch, se, fi, no, dk) with AltGr, Caps Lock and dead keys.

| Command | Effect |
| --- | --- |
| `/set temp 0.7` | sampling with a temperature; 0 is the default greedy decoding |
| `/set top-k 50`, `top-p 0.95`, `min-p 0.05`, `repeat 1.1`, `seed 42`, `tokens 2048` | candidate filters, repetition penalty, seed and maximum tokens per answer, up to the context |
| `/think on`, `/think off`, `/think show`, `/think hide` | reasoning before the answer, shown dim or summarised |
| `/system TEXT` | system prompt; restarts the conversation |
| `/stats`, `/set`, `/reset`, `/help`, `/clear`, `/quit` | statistics, settings, defaults, help, new conversation, exit |
| `/keymap it`, Esc | keyboard layout; Esc clears the line or stops the answer (kernel only) |

![Sampling settings, an answer and the command list, with live statistics in the status line](docs/screenshots/pithos-core-commands.png)

![Reasoning mode: the model's reasoning appears dim before the answer](docs/screenshots/pithos-core-reasoning.png)

### Performance

Measured on 27 November 2026 on an Intel Core i5-10500H, WSL2 with four visible CPUs, a 465-token prompt and 64 generated tokens.

| Threads | First token | Prompt | Generation |
| --- | --- | --- | --- |
| 1 | 19.67 s | 24 tokens/s | 9.79 tokens/s |
| 4 | 7.95 s | 59 tokens/s | 17.77 tokens/s |

On the same machine the pithos C engine, with four threads on Windows, processed the same prompt at 56-62 tokens/s and generated 19-21 tokens/s.

### Verification

~~~sh
make verify-lfm3 verify-lfm3-tokenizer verify-lfm3-os LFM3_MODEL=weights/LFM3-1.7B-Q4_K_M.gguf LFM3_TOKENIZER=lfm3-ref/tokenizer.json LFM3_REF=lfm3-ref
~~~

The tokenizer matches the official one on 62 texts and on all 128,000 IDs. Every block of the model reproduces the FP32 reference given the same Q8_K inputs, the final argmax matches on prompts of up to 721 tokens, and greedy answers are the reference argmax except at near ties. Logits and answers are bitwise identical between 1 and 16 threads, between block and token-by-token prefill, and between Linux and the kernel on 1, 2, 3, 4 and 6 cores.

## LFM2.5-350M: the compact model

![Pithos CORE running LFM2.5-350M](docs/screenshots/pithos-core-lfm2.png)

Inference for the official BF16 weights of LiquidAI/LFM2.5-350M, with FP32 activations and accumulation, a scalar path for CPUs without AVX2, and bitwise verification against Transformers. Linux loads the weights with mmap and uses persistent threads; the kernel receives weights and tokenizer from the bootloader and starts its own workers, with the same Pithos CORE console.

### Build and usage

The build needs NASM, GNU ld, GNU make 4.3 or later and Python 3 with the tokenizers package; the verified tokenizers version is 0.23.3. On x86-64 Linux with the Hugging Face client installed, run from the source directory

~~~sh
hf download LiquidAI/LFM2.5-350M --revision 9921cd4d82c0e3986887aa4b376f9446729ef8a3 --include model.safetensors config.json tokenizer.json tokenizer_config.json chat_template.jinja --local-dir weights
make MODEL=weights/model.safetensors
./build/lfm-next weights/model.safetensors 1 314 271
./build/lfm-next weights/model.safetensors --text 64 "Write a greeting in Italian."
./build/lfm-next weights/model.safetensors --chat
~~~

A Python generator checks tensor shapes and types and emits the checkpoint offsets. A second generator compiles the official tokenizer into `build/tokenizer.bin`, with the vocabulary, BPE merges, added tokens and Unicode categories taken from the same engine as the reference. The tables take 4,224,959 bytes and must ship next to the executable. The runtime finds them through `/proc/self/exe` and checks their size and checksum. Python is needed only for the build and the verifications. To choose the interpreter, pass `PYTHON=/path/to/venv/bin/python` to make.

`--text N "prompt"` applies the official template for one user message and the assistant prefix, generates up to N tokens and streams the UTF-8 answer. Tokens marked special are left out of the text. Decoding keeps UTF-8 sequences split across tokens and replaces malformed ones with U+FFFD. The answer ends without adding characters to the generated text. Each invocation starts a one-turn conversation. The templated text may take at most 8,191 bytes and must fit the cache.

To use the current build from PowerShell in the repository directory:

~~~powershell
wsl -d Ubuntu -- ./build/lfm-next /opt/lfm-model/model.safetensors --text 64 "Write a greeting in Italian."
~~~

`--chat [N]` keeps the model, the workers and the history in memory between turns. N limits the tokens generated per answer and defaults to 128, reduced to the context size if needed. Enter one question per line, `/clear` to reset the conversation and `/quit` or EOF to exit. Answers go to stdout, while labels and status messages use stderr.

~~~powershell
wsl -d Ubuntu -- ./build/lfm-next /opt/lfm-model/model.safetensors --chat
wsl -d Ubuntu -- env LFM_CONTEXT=4096 LFM_THREADS=6 ./build/lfm-next /opt/lfm-model/model.safetensors --chat 128
~~~

`LFM_CONTEXT` accepts 1 to 32,768. The default is 2,048 in chat and 512 in the other modes. The FP32 KV cache is allocated dynamically and takes 24 KiB per position, so 48 MiB at 2,048 positions and 768 MiB at 32,768. Weights and work buffers take additional memory. UTF-8 text stays limited to 8,191 bytes per request, template included.

Before accepting a turn, the chat checks the space needed for the new prompt, N answer tokens and two positions to close the turn. When there is not enough, it prints a message and waits for another line. `/clear` resets the position and the convolution state. New tokens overwrite KV rows before they are read.

The history keeps the IDs actually generated. Each answer ends with EOS and a newline, as in the template. If generation reaches N before EOS, the program reports the limit and adds the closing tokens to the history. Malformed or overlong input is rejected before the model state changes.

The default thread count is the smaller of six and the CPUs available in the process affinity. `LFM_THREADS` selects 1 to 16 threads, the main thread included. If the system limits worker creation, the program uses the workers that were created.

~~~sh
LFM_THREADS=4 ./build/lfm-next weights/model.safetensors 1 314 271
~~~

`--generate N`, after the checkpoint and before the IDs, generates up to N tokens. The default is one, compatible with the original CLI. Generation stops at N tokens or at EOS token 7, which is included in the output. N must be positive, and the prompt length plus N minus one must fit the configured context. The last predicted token is emitted without taking a new cache position. All arguments are checked before inference.

The IDs in the next example are the question `What is the capital of France?` in the official chat template.

~~~sh
./build/lfm-next weights/model.safetensors --generate 32 1 6 6423 708 3493 856 779 5706 803 4481 540 7 708 6 64015 708
~~~

It prints the IDs `1098 5706 803 4481 856 5242 523 7`, one per line. The equivalent call with `--text 32 "What is the capital of France?"` prints `The capital of France is Paris.`

The diagnostic modes `--encode "text"` and `--decode ID ...` expose the tokenizer. Encode returns IDs without an implicit BOS and decode leaves out special tokens. Both respect the token count allowed by the configured context and use only the tables, so the checkpoint path can be replaced by `_`.

### Booting as a kernel in QEMU

The kernel runs inference and chat with no Linux in the guest. Multiboot 1 supports QEMU direct boot; Multiboot 2 supports GRUB in BIOS and UEFI mode. The code sets up the GDT, paging, long mode, the SSE/AVX state and exception handlers. The cache is allocated from the bootloader's RAM map; weights and tokenizer stay in memory.

Besides the Linux build tools this needs GNU objcopy, QEMU, Pillow and the DejaVu, Unifont and Noto Color Emoji fonts. Font generation uses `FONT_PYTHON=python3`, separate from a `PYTHON` that may point at the model's venv. The verified setup uses KVM on Linux/WSL2 with access to `/dev/kvm`. To install the BIOS/UEFI image tools as well on Ubuntu:

~~~sh
sudo apt-get install --no-install-recommends qemu-system-x86 qemu-system-gui python3-pil python3-fonttools fonts-dejavu-core unifont fonts-noto-color-emoji grub-pc-bin grub-efi-amd64-bin xorriso mtools ovmf
make os MODEL=weights/model.safetensors
python3 os/run.py build/lfm-boot.bundle
~~~

The build produces `build/lfm-os.elf` and `build/lfm-boot.bundle`. The bundle holds an unchanged copy of the BF16 checkpoint and of the tokenizer tables: 713,213,887 bytes with the verified files. The kernel is an ELF32 for QEMU's Multiboot loader but switches to 64 bits before inference. The intermediate ELF64 stays available in `build/lfm-os.elf64`.

In the prepared environment, from PowerShell in the repository directory:

~~~powershell
wsl -d Ubuntu -- make os MODEL=/opt/lfm-model/model.safetensors OS_BUNDLE=/opt/lfm-model/lfm-boot.bundle PYTHON=/opt/lfm-venv/bin/python
wsl -d Ubuntu -- /opt/lfm-venv/bin/python os/run.py /opt/lfm-model/lfm-boot.bundle
~~~

The launcher gives the VM six CPUs and asks the kernel for six workers, the main processor included. `--cpus` changes the virtual CPUs and `--threads` the processors requested by the kernel, both from 1 to 16. The ACPI MADT tables list the processors, which start through xAPIC and the INIT/SIPI sequence. The kernel uses only processors that started and support the selected SIMD path; unsupported ACPI or xAPIC leaves one processor active. Each worker computes whole matrix rows and keeps the reduction order.

Direct boot uses 2,048 positions and at most 32 tokens per answer. The chat supports `/clear`, `/quit`, Ctrl-D, CRLF and backspace, and the engine commands described for the main model except reasoning. `--context` and `--tokens` change the limits. The default RAM is 2 GiB; `--memory` changes the VM memory. The cache keeps its cost of 24 KiB per position. If memory is insufficient, the kernel prints an error and stops.

`--display gtk` opens the video console, the same Pithos CORE console as the main model: Unicode with colour emoji, thirteen keyboard layouts, a status line and the chat commands. Direct boot uses VGA text; GRUB requests a 32-bit RGB framebuffer, normally 1024x768. COM1 keeps the complete UTF-8 text with the same colour sequences. Without a serial port, inference and the video console keep working.

For a single answer or the generated IDs:

~~~sh
python3 os/run.py build/lfm-boot.bundle --mode text --tokens 32 --prompt "What is the capital of France?"
python3 os/run.py build/lfm-boot.bundle --mode ids --tokens 8 --prompt "What is the capital of France?"
~~~

The single modes delimit the result with `<lfm-output>` and `</lfm-output>` on the serial port. The launcher interprets QEMU's `isa-debug-exit` device and returns zero when the kernel ends correctly. With direct QEMU, host exit code 33 means guest success and 35 a guest error; exit code 1 from a QEMU start-up error stays an error. Without KVM, `--accel tcg` works, but software emulation of inference is much slower.

### BIOS/UEFI and USB image

~~~sh
make os-image MODEL=weights/model.safetensors
python3 os/run.py --iso build/lfm-os.iso --display gtk
python3 os/run.py --iso build/lfm-os.iso --uefi --display gtk
python3 os/run.py --iso build/lfm-os.iso --uefi --usb --display gtk
~~~

`build/lfm-os.iso` is a hybrid GRUB image of about 729 MB holding the kernel, the tokenizer and the unchanged BF16 checkpoint. It can be written raw to a USB stick to boot an x86-64 machine with BIOS or UEFI. The build only creates the ISO file and never writes to physical devices. GRUB reads the data from the medium and hands it to the kernel; after boot the kernel works entirely in RAM and does not access the filesystem.

The image starts the chat with 512 tokens per answer, a 4,096-position context and at most six active CPUs. The parameters are embedded in `grub.cfg`; the launcher can change virtual CPUs and RAM but rejects kernel parameters that could not change the image. For an image with different limits:

~~~sh
python3 os/image.py build/lfm-os.elf build/lfm-boot.bundle build/lfm-os.iso --options "mode=chat tokens=128 context=4096 threads=4 keymap=it"
~~~

The prepared environment also keeps a copy on the Linux filesystem, which avoids the cost of disk access through the Windows mount:

~~~powershell
wsl -d Ubuntu -- make os-image MODEL=/opt/lfm-model/model.safetensors OS_BUNDLE=/opt/lfm-model/lfm-boot.bundle OS_IMAGE=/opt/lfm-model/lfm-os.iso PYTHON=/opt/lfm-venv/bin/python
wsl -d Ubuntu -- /opt/lfm-venv/bin/python os/run.py --iso /opt/lfm-model/lfm-os.iso --uefi --usb --display gtk
~~~

The image path uses QEMU q35 with AHCI/DMA, which avoids loading the weights through IDE PIO. USB emulation uses a USB2 EHCI controller: xHCI produced intermittent firmware hangs during tests on WSL/KVM, even with MSI disabled. Loading about 713 MB through EHCI can take over a minute; CD or direct boot is faster for development. OVMF uses xAPIC, PCI MMIO below 4 GiB and a temporary copy of the firmware variables. The MMIO window size is set through the [official OVMF configuration](https://github.com/tianocore/edk2/blob/master/OvmfPkg/RUNTIME_CONFIG.md). The image is not signed: PCs with Secure Boot enabled must disable it to boot.

Booting is verified in QEMU, not yet on a physical PC. Current compatibility requires usable RAM below 4 GiB, a 32-bit RGB framebuffer below 4 GiB or VGA/serial, and a PS/2 or serial keyboard. There is no USB HID driver: booting from USB is handled by the firmware and GRUB and does not imply that every USB keyboard works after boot. CPUs with x2APIC already enabled fall back to one core. The console and the workers busy-wait; idle power saving is not implemented yet. On physical hardware `/quit` halts the processors but does not perform an ACPI power-off.

### Kernel verification

~~~sh
make verify-os MODEL=weights/model.safetensors
make verify-platform MODEL=weights/model.safetensors
~~~

`verify-os` compares tokens, UTF-8 text and all 65,536 logits with single-threaded Linux. It covers chat with history, reset, input errors, the cache limit, CPUs without AVX/XSAVE, a missing or corrupt module and insufficient RAM. `verify-platform` checks generation on 1, 2, 3, 4, 6 and 16 CPUs, logits on 3 and 6 CPUs, the fallback without ACPI, VGA, the PS/2 keyboard and a missing COM1. It also boots the image from emulated CD and USB with BIOS and UEFI, checks an answer in each case and saves the screens to `build/os-*.png`. It needs KVM and also builds the image and the diagnostic kernel `lfm-os-logits.elf`.

Verification completed on 26 November 2026 with QEMU 10.2.1 and KVM on WSL2: five greedy sequences and three text answers match Linux; all logits are bitwise identical for two prompts. The bundle preserves the SHA-256 hashes of checkpoint and tokenizer. The serial chat and boot error tests passed as well. With a 32,768-position context, allocation and the first prediction are verified with 2 GiB of RAM, and the cache refusal with 1 GiB; this is not a numerical verification of 32,768-token sequences. The Linux suites for logits, generation, chat, tokenizer and threads passed after the platforms were separated.

The platform checks passed on 1, 2, 3, 4, 6 and 16 CPUs, with bitwise identical logits on 3 and 6 CPUs and the fallback without ACPI. BIOS/UEFI boots from emulated CD and USB completed an answer typed on the PS/2 keyboard. The UEFI/USB path with EHCI was also verified after a cold WSL start and on subsequent boots. Without the QEMU exit device, all four checked processors reach HLT after `/quit`. The Linux suites for logits up to 512 tokens and generation up to 64 tokens were run again successfully. With the Pithos CORE console all these suites passed again on 27 November 2026.

The kernel benchmark runs with no other VMs or benchmarks in parallel:

~~~sh
make benchmark-os MODEL=weights/model.safetensors
~~~

It uses six vCPUs, 2 GiB of RAM, a 512-position context, the same 25-token prompt as the Linux benchmark and 64 generated tokens. It compares 1, 2, 4 and 6 active CPUs, checks that the IDs are identical, and runs one warm-up and three samples per configuration in alternating order. It separates VM loading and start-up from prefill and subsequent generation. Samples and medians are in `build/os-benchmark.json`.

Measured on 26 November 2026 on an Intel Core i7-10750H, QEMU 10.2.1/KVM on WSL2, BF16 weights on the Linux filesystem. Prefill in the table excludes VM start-up; the total includes it. Subsequent generation measures the 63 intervals between the first and the sixty-fourth token.

| Active CPUs | Prefill and first token | Subsequent generation | Total with VM start-up |
| --- | --- | --- | --- |
| 1 | 990 ms | 20.67 tokens/s | 4.61 s |
| 2 | 782 ms | 29.05 tokens/s | 4.00 s |
| 4 | 648 ms | 29.55 tokens/s | 3.41 s |
| 6 | 623 ms | 32.13 tokens/s | 3.23 s |

Six CPUs gave the best result among the measured configurations, about 55% faster generation than one CPU. The result applies to this machine and this workload; BIOS/UEFI image boots are not part of the benchmark, which uses QEMU's direct Multiboot loading.

Linux/WSL remains the host that runs QEMU and the preparation tools. The tests are not a hardware compatibility certification or a speed comparison with other runtimes.

### Quality

The project uses only the official BF16 weights, with FP32 activations and accumulation. This configuration gave the best quality among those tried and keeps the precision of the original weights. The checkpoint takes 708,984,464 bytes; cache and buffers need additional memory.

`quality_corpus.json` holds 12 original texts, six Italian and six English, for 1,739 evaluated tokens, and eight simple requests. It is a small diagnostic corpus, not a benchmark representative of general capabilities.

~~~sh
make evaluate-quality MODEL=weights/model.safetensors
~~~

The evaluation uses Transformers in FP32 with the official BF16 weights, one BOS per document, no truncation or added EOS, and averages weighted by token count. One document per language is checked by comparing the last logits with the assembly runtime. The answers to the eight requests are generated by the runtime. Method, corpus hash, per-document results and complete answers are in `build/quality-report.json`.

The measured perplexity is 27.44 in Italian, 32.86 in English and 29.55 overall. Five of the eight answers meet the requested result and format. The comparison ignores case, spaces and final periods; an explanation added when a single word is requested can therefore count as non-compliant.

### Verification

With PyTorch and a Transformers release that supports LFM2 installed, run:

~~~sh
make verify MODEL=weights/model.safetensors
~~~

The test compares the greedy prediction and all 65,536 logits for sequences of 1, 2, 5, 16, 64 and 512 tokens. The question formatted with the official chat template is repeated to exercise the cache limit as well. The reference uses the same weights in FP32 with eager attention. The tolerances are 0.001 absolute and 0.0001 relative. The test also checks that out-of-range or malformed arguments are rejected.

On this machine the verification environment lives in Ubuntu WSL2, in `/opt/lfm-venv`. From PowerShell in the repository directory:

~~~powershell
wsl -d Ubuntu -- make verify MODEL=weights/model.safetensors PYTHON=/opt/lfm-venv/bin/python
~~~

With AVX2/FMA the prompt is processed in blocks of 15 tokens, keeping the BF16 weights. The scalar path still processes the prompt token by token.

BF16 verification completed on 26 November 2026 on Ubuntu WSL2 with NASM 3.01, PyTorch 2.15.0+cpu and Transformers 5.24.1. The six predictions match the reference, up to 512 tokens. The largest absolute logit error is 0.00018620. The question `What is the capital of France?` yields `The` (ID 1098) as its first token. The ELF executable is static; weights and tokenizer tables are separate files.

SHA-256 of the verified checkpoint

~~~text
1c9c77a4471a7f590f85240f74ed1fc26df7fbde88c3006724e2f93ca993ea4e
~~~

### Implementation

- main.asm checks the model, runs the layers and computes the logits with the shared embedding matrix.
- platform_linux.asm handles the CLI, file loading, memory and I/O through Linux system calls.
- os/boot.asm and os/platform.asm handle the 64-bit start, the boot module, RAM allocation and the I/O of the standalone kernel.
- os/multiboot.asm normalizes the Multiboot 2 boot information; os/smp.asm detects and starts the CPUs and distributes matrix rows.
- os/ui.asm draws the Pithos CORE console on VGA or an RGB framebuffer, with Unicode glyphs, colour emoji and keyboard layouts; os/console.asm is the former Latin-1 console.
- kernels.asm implements matrix-vector products, RMSNorm, the exponential and the causal convolution with two history samples per channel.
- attention.asm normalizes queries and keys per head, applies RoPE and computes grouped-query attention over the cache.
- engine.asm implements sampling, the system prompt, statistics and the chat commands for both models.
- layers.inc holds the order of the ten convolution blocks and the six attention blocks.
- threads.asm implements the worker pool with the clone and futex system calls. Each worker computes whole matrix rows. A short spin precedes the futex wait, and the process ends all workers through exit_group.
- tokenizer.asm implements Unicode pre-tokenization, added-token matching, BPE merges and streaming UTF-8 decoding. The tokenizer runs on the main thread between inference jobs and uses read-only tables.
- chat.asm handles line input, chat commands, recovery from input errors and cache allocation through the platform backend.

The AVX2 matrix-vector products expand BF16 to FP32 exactly and use four independent FMA accumulators. Kernel selection also checks operating-system support for the YMM registers through XGETBV. RoPE rotations are computed once per position and reused by the 144 query/key heads of the six attention layers. RMSNorm computes a single division per vector.

On the same AVX2/FMA path, the exponential of the SiLU in the MLPs and of the attention softmax processes eight values per instruction. Argument reduction follows Cephes, with a fifth-degree polynomial and the same ±80 bounds as the x87 version. Over 1,048,576 inputs between -90 and 90 the largest error is 1.002 ulp, against 0.5 ulp for x87. The softmax masks the final partial block, so positions past the current one are neither read nor summed. The scalar build and CPUs without AVX2/FMA keep the x87 exponential, with bitwise identical results. All Linux and kernel verifications passed with this change: logits within the Transformers tolerances, with a largest error of 0.000115, and bitwise identical across threads, cores and between Linux and the kernel. On a machine with four CPUs visible in WSL2, generation rose by about 10-14%, with a run-to-run noise of about 10%.

Attention also has an AVX2/FMA path. The 64 query components stay in registers during the products with the keys, and a single pass over the positions accumulates all value components. The 16 heads are distributed among the workers, and each partition uses its own score row. Every head is computed by the same code whatever the thread, so the logits stay bitwise identical between 1 and 16 threads or cores. Linux and the kernel share the job mechanism: the workers run the function named by `job_entry`, which can be the matrix product or attention. The scalar attention path stays on the main thread. On the same machine, with 1,900 cached positions, generation rose from 15.8 to 21.4 tokens/s on one thread and from about 23 to 28 tokens/s on four.

The prompt is processed in blocks of 15 tokens, set at compile time with `-DPREFILL_BLOCK=N`. In the matrices each weight row is read once per block, and each converted BF16 vector serves up to three tokens. Each (row, token) pair uses the same four accumulators and the same reduction tree as the single-token product, so the block prefill is bitwise identical to token-by-token processing. Normalization, convolution state, RoPE and attention advance one token at a time in the original order. The keys and values of the block are written to the cache before attention, and each token reads only positions up to its own. Logits, generation and chat transcripts match the previous version byte for byte, for prompts of 1 to 511 tokens and with 1, 3 and 4 threads. On the same machine, measuring the whole process up to the first token:

| Prompt | Threads | Token by token | Blocks | Speed-up |
| --- | --- | --- | --- | --- |
| 25 tokens | 1 | 896 ms | 371 ms | 2.4x |
| 512 tokens | 1 | 18.66 s | 7.53 s | 2.5x |
| 25 tokens | 4 | 631 ms | 179 ms | 3.5x |
| 512 tokens | 4 | 16.55 s | 3.51 s | 4.7x |

Block prefill is limited by FMA throughput rather than memory bandwidth, so it scales with threads; blocks larger than 15 tokens did not improve the times.

The architectural choices follow the LFM2 technical report and the checkpoint configuration. The dense matrices of the convolution blocks and the MLPs remain the main target of the vector kernels. [Liquid AI technical report](https://arxiv.org/html/2511.23404v1#S2)

To compare the scalar path and the automatically selected one on the same checkpoint, run

~~~sh
make benchmark MODEL=weights/model.safetensors
~~~

The benchmark measures the time of the whole process to predict one token, prompt included. It runs one warm-up and three repetitions in alternating order, checks the predicted token and saves all samples to `build/benchmark.json`. The file must stay identical for both executables. On WSL, the location of the weights in the filesystem strongly affects the measurement. The Linux copy used for local comparisons is in `/opt/lfm-model/model.safetensors`.

Measured on 26 November 2026 on an Intel Core i7-10750H, Ubuntu WSL2, one thread and BF16 weights on the Linux filesystem. Medians of five repetitions after warm-up, comparing `lfm-scalar` and `lfm-next`.

| Prompt | Scalar matvec | AVX2/FMA matvec | Speed-up |
| --- | --- | --- | --- |
| 1 token | 351.68 ms | 65.26 ms | 5.39x |
| 16 tokens | 4,455.52 ms | 637.90 ms | 6.98x |

To repeat this configuration from the Linux shell in the repository directory:

~~~sh
make build/lfm-scalar build/lfm-next MODEL=/opt/lfm-model/model.safetensors
python3 benchmark.py /opt/lfm-model/model.safetensors build/lfm-scalar build/lfm-next --repeats 5 --output build/benchmark.json
~~~

Latency includes start-up, mmap, prompt processing and the final prediction. The measurements in this section predate the block prefill described above. Results of other runtimes require a comparison with the same weights, precision and hardware.

The following parallelism comparison, on the same CPU and with five repetitions after warm-up, gave these medians for the 16-token prompt.

| Threads | Latency | Speed-up over 1 thread |
| --- | --- | --- |
| 1 | 668.33 ms | 1.00x |
| 2 | 481.73 ms | 1.39x |
| 4 | 470.67 ms | 1.42x |
| 6 | 472.06 ms | 1.42x |
| 8 | 469.80 ms | 1.42x |

The results at 4, 6 and 8 threads are close. The default of six limits thread use on this six-core CPU. The limit concerns the matrix-vector products, while the other operations stay on the main thread.

~~~sh
make benchmark-threads MODEL=/opt/lfm-model/model.safetensors
make verify-threads MODEL=/opt/lfm-model/model.safetensors
~~~

The thread verification compares logits bit for bit with the single-threaded path, includes partitions with remainders and contexts up to 512 tokens, runs eight requests in four simultaneous processes and checks invalid LFM_THREADS values.

The chat and the dynamic context are verified with

~~~sh
make verify-chat MODEL=/opt/lfm-model/model.safetensors PYTHON=/opt/lfm-venv/bin/python
~~~

The comparison with Transformers covers four turns, reset, truncated answers and turn closing, rejected input, CRLF and EOF after an incomplete line. It also checks exact cache exhaustion, a 513-token prompt with a 1,024-position context and the configuration limits. At 32,768 positions it checks allocation and a first prediction. The full logit verification stays on contexts up to 512 positions.

The tokenizer is verified with

~~~sh
make verify-tokenizer MODEL=/opt/lfm-model/model.safetensors PYTHON=/opt/lfm-venv/bin/python
~~~

774 encoding cases and 1,130 decoding cases passed, including every vocabulary ID in groups of 256, the added tokens, multilingual text, emoji and malformed or incomplete UTF-8. The tests also check input limits and table lookup when the working directory changes. Missing or corrupt tables produce an error. Text inference in English, Italian and Chinese matches inference started from the IDs of the official tokenizer.

Continuous generation is verified and measured with

~~~sh
make verify-generation MODEL=/opt/lfm-model/model.safetensors PYTHON=/opt/lfm-venv/bin/python
make benchmark-generation MODEL=/opt/lfm-model/model.safetensors
~~~

The verification compares with Transformers an answer ended by EOS, an answer limited to three tokens, a 64-token sequence and two tokens generated after a 511-position prompt. It also checks compatibility with the original CLI, invalid arguments and the identity of the long sequence between one and six threads.

Benchmark of 26 November 2026 on the same CPU, BF16 weights on the Linux filesystem, a 25-token prompt and 64 generated tokens. Medians of three repetitions after warm-up.

| Threads | Time to first token | Subsequent generation | Total time |
| --- | --- | --- | --- |
| 1 | 979 ms | 21.45 tokens/s | 3.92 s |
| 6 | 700 ms | 28.41 tokens/s | 2.92 s |

The benchmark observes the tokens on stdout. The time to first token includes process start-up and prefill. The subsequent speed is computed over the 63 intervals after the first token. All samples are saved to `build/generation-benchmark.json`.

[Official checkpoint and configuration](https://huggingface.co/LiquidAI/LFM2.5-350M/tree/main)

## License

Pithos CORE is released under the [MIT license](LICENSE). The console glyphs come from DejaVu Sans Mono ([os/FONT-LICENSE.txt](os/FONT-LICENSE.txt)) and from GNU Unifont and Noto Color Emoji, both used under the SIL Open Font License 1.1 ([os/CONSOLE-FONTS-LICENSE.txt](os/CONSOLE-FONTS-LICENSE.txt)). The keyboard layouts are generated from the xkeyboard-config data ([os/KEYMAPS-LICENSE.txt](os/KEYMAPS-LICENSE.txt)). The Pithos mark comes from the [pithos](https://github.com/benmaster82/Pithos) project by the same author.

The model weights are not part of this repository. LFM3-1.7B and LFM2.5-350M are distributed by Liquid AI under their own licenses (the LFM3 GGUF declares the LFM Open License, `lfm1.0`), which also apply to the boot bundles and ISO images built from them.
