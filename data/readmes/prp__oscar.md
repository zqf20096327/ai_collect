# Oscar: Elastic LLM Serving for Larger-than-Memory LLMs on Apple Silicon

Oscar is an elastic LLM offloading service for Apple Silicon machines, written in Rust, that runs mixture-of-experts (MoE) models that are larger than the machine's memory. Existing offloading LLM runtimes allocate a fixed amount of memory to a model at load time and keep the rest of the model on disk. Instead, Oscar uses a machine's spare memory elastically: it continuously adjusts its memory use, taking unused memory from other applications and returning memory when other applications demand it. Oscar exploits idle CPU and GPU cycles to prefetch model experts into memory to improve serving performance.

Oscar can therefore run large quantised open-weight LLMs on Apple Silicon machines with a fraction of the memory that the models occupy. For example, on a MacBook Pro M5 Max with 64 GB of memory, Oscar runs the 2.8-trillion-parameter Kimi K3.1 Pro model, which is 577 GB in size (9× the machine's memory), at a decoding rate of 1.7 tokens/second. Models that exceed a machine's memory by smaller factors run at interactive speeds: a 178-billion-parameter Qwen3.8-Flash-Next model (113 GB) decodes at 33 tokens/second, and a 397-billion-parameter Qwen3.5-397B-A17B model (161 GB) at 12 tokens/second.

<p align="center">
  <img src="docs/menu.png" width="398" alt="Oscar's menu: the decoding status, memory use, the models and a download"><br>
  <em>Oscar decoding with a served model, while downloading another model</em>
</p>

## Oscar's Unique Approach

<p align="center">
  <img src="docs/architecture.svg" width="860"
       alt="Oscar's four mechanisms: the event-driven engine over sealed and paged layers, elastic memory management, routing-aware prefetching and self-drafting">
</p>

- **Elastic memory management.** Oscar manages a Mac's unified memory similar to how an OS manages its page cache: it uses all free memory for serving but gives up the memory under pressure. Oscar's memory planner traces a model's memory use (its resident weights, expert weights, session state and working memory) ahead of time and produces a memory plan for each LLM phase. The memory plan includes the KV cache of a conversation: state for completed turns is offloaded to disk, so follow-up turns or restarts avoid recomputation. Oscar manages memory as fixed-size segments, which its adaptive memory controller sheds and regrows between model tokens as available memory changes. 
- **Event-driven unified memory engine.** Oscar exploits the unified memory architecture of Apple Silicon, in which the CPU and GPU share the same memory: expert weights are loaded from disk directly into the memory that GPU kernels compute on, without extra memory copies. Model layers whose experts fit in memory are sealed and executed by the GPU without overhead; the remaining layers are paged, fetching experts from disk. The boundary between sealed and paged layers moves as memory is shed and regrown. Paged layers are executed in an event-driven fashion: Oscar submits all layers of a token to the GPU at once, instead of interrupting it at each paged layer, and a paged layer waits only until the CPU signals that its missing experts are in memory.
- **Routing-aware expert prefetching.** Oscar predicts the activated experts ahead of time, so they can be prefetched without blocking the GPU: while the GPU executes a layer, a router lookahead feeds the current activations into the routers of future layers and prefetches the experts. The predictions also determine which experts can be evicted from memory. An optional approximate routing mode trades exact output for fewer disk reads: it replaces activated experts that are not in memory and have a low routing weight with available experts.
- **Opportunistic self-drafting of experts.** When the decoding rate is bounded by disk reads, the GPU has idle capacity. Oscar uses this spare capacity to prefetch experts for future tokens, beyond the reach of the router lookahead: on a second GPU stream, the model itself drafts the next tokens ahead of the main decoding pass. The draft never waits for disk reads: it computes with the experts that are in memory and ignores missing ones, and the activated experts are used as predictions for prefetching. As self-drafting competes with the main decoding pass for the GPU, Oscar measures its benefit at runtime and only drafts when it increases the decoding rate.

## Features

**Using Oscar**

- 🤖 **Agentic coding** with OpenCode, preconfigured for the served model
- 💬 **Interactive terminal chat** with control over thinking and reasoning effort
- 🔌 **OpenAI-compatible API server** with streaming chat completions, tool calling and reasoning output
- 🖥️ **Oscar menu bar app** to select, download and remove models, to monitor status and memory use, and to launch chat and coding sessions
- ⌨️ **Command line interface** to serve, chat with and manage models
- 🔒 **Fully local**: prompts and outputs never leave the machine

**Models**

- 🧠 **Latest open-weight MoE models** of the Qwen, GLM and Kimi families, including hybrid architectures with recurrent layers, each with its own chat template and sampling settings
- 📥 **Model downloads from Hugging Face**, from the menu bar app or command line
- 🗜️ **Efficient quantisations**: based on Unsloth's quantised models, with tensors potentially re-quantised at download, making large models tractable in the available memory

**Engine**

- ⚡ **Custom Metal GPU kernels** that compute directly on the quantised weights, without expanding them in memory, for 1-bit to 8-bit quantisation formats
- 🍎 **Support for different Apple Silicon generations**, from M1 to M5 CPU/GPUs
- 🛡️ **No runtime out-of-memory failures**: a model that does not fit the machine is rejected at load time, not
  during serving
- 🪄 **Automatic configuration**: memory and performance settings are derived from the model and the machine by default

## Supported Models and Performance

<table>
  <thead>
    <tr>
      <th colspan="4">Model</th>
      <th colspan="4">Performance<br>(tokens/second)</th>
      <th colspan="2">Memory</th>
    </tr>
    <tr>
      <th align="left" rowspan="2">Name</th>
      <th align="right" rowspan="2">Params</th>
      <th align="left" rowspan="2">Quantisation</th>
      <th align="right" rowspan="2">Disk<br>usage</th>
      <th colspan="2">1k context</th>
      <th colspan="2">24k context</th>
      <th align="right" rowspan="2">Oversub-<br>scription</th>
      <th align="right" rowspan="2">Minimum</th>
    </tr>
    <tr>
      <th align="right">Decode</th>
      <th align="right">Prefill</th>
      <th align="right">Decode</th>
      <th align="right">Prefill</th>
    </tr>
  </thead>
  <tbody>
    <tr><td nowrap><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen3.6-35B-A3B</a></td><td align="right">35B</td><td nowrap>Q4_K</td><td align="right" nowrap>20 GB</td><td align="right" nowrap>151</td><td align="right" nowrap>3,300</td><td align="right" nowrap>120</td><td align="right" nowrap>3,760</td><td align="right" nowrap>0.3×</td><td align="right" nowrap>4.4 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/Qwen/Qwen3-Coder-Next">Qwen3-Coder-Next</a></td><td align="right">80B</td><td nowrap>Q4_K</td><td align="right" nowrap>42 GB</td><td align="right" nowrap>128</td><td align="right" nowrap>2,540</td><td align="right" nowrap>97.8</td><td align="right" nowrap>2,810</td><td align="right" nowrap>0.7×</td><td align="right" nowrap>4.6 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen3.8-Flash-Next</a></td><td align="right">178B</td><td nowrap>Q3_K</td><td align="right" nowrap>113 GB</td><td align="right" nowrap>33.4</td><td align="right" nowrap>316</td><td align="right" nowrap>30.2</td><td align="right" nowrap>620</td><td align="right" nowrap>1.8×</td><td align="right" nowrap>6.8 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/Qwen/Qwen3-235B-A22B">Qwen3-235B-A22B</a></td><td align="right">235B</td><td nowrap>Q4_K</td><td align="right" nowrap>124 GB</td><td align="right" nowrap>6.9</td><td align="right" nowrap>89</td><td align="right" nowrap>6.5</td><td align="right" nowrap>400</td><td align="right" nowrap>1.9×</td><td align="right" nowrap>13.8 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/zai-org/GLM-5.3-Flash">GLM-5.3-Flash</a></td><td align="right">321B</td><td nowrap>Q3_K</td><td align="right" nowrap>130 GB</td><td align="right" nowrap>8.6</td><td align="right" nowrap>79</td><td align="right" nowrap>7.6</td><td align="right" nowrap>206</td><td align="right" nowrap>2.0×</td><td align="right" nowrap>8.7 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen3.5-397B-A17B</a></td><td align="right">397B</td><td nowrap>Q3_K</td><td align="right" nowrap>161 GB</td><td align="right" nowrap>12.0</td><td align="right" nowrap>65</td><td align="right" nowrap>11.5</td><td align="right" nowrap>566</td><td align="right" nowrap>2.5×</td><td align="right" nowrap>10.7 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/zai-org/GLM-5.2">GLM-5.2</a></td><td align="right">754B</td><td nowrap>Q3_K</td><td align="right" nowrap>313 GB</td><td align="right" nowrap>2.3</td><td align="right" nowrap>33</td><td align="right" nowrap>1.5</td><td align="right" nowrap>53</td><td align="right" nowrap>4.9×</td><td align="right" nowrap>24.8 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/moonshotai/Kimi-K3.1-Pro">Kimi K3.1 Pro</a></td><td align="right">2.8T</td><td nowrap>KLX-IQ1_S</td><td align="right" nowrap>577 GB</td><td align="right" nowrap>1.7</td><td align="right" nowrap>23</td><td align="right" nowrap>1.6</td><td align="right" nowrap>33</td><td align="right" nowrap>9.0×</td><td align="right" nowrap>38.0 GB</td></tr>
    <tr><td nowrap><a href="https://huggingface.co/moonshotai/Kimi-K3">Kimi K3</a></td><td align="right">2.8T</td><td nowrap>UD-IQ1_M</td><td align="right" nowrap>629 GB</td><td align="right" nowrap>1.6</td><td align="right" nowrap>22</td><td align="right" nowrap>1.4</td><td align="right" nowrap>30</td><td align="right" nowrap>9.8×</td><td align="right" nowrap>42.3 GB</td></tr>
  </tbody>
</table>

(Measured on a MacBook Pro M5 Max with 64 GB of memory in High Power mode, with Oscar limited to 52 GB and the models on the internal SSD (13.5 GB/s throughput); the quantisation is that of the expert weights.)

**Disk space during installation.** The table shows a model's size once installed. Installing it temporarily needs about 95 GB more, because Oscar downloads a higher-precision version in parts and converts it locally. For example, Qwen3-Coder-Next occupies 42 GB but needs 132 GB to install. The two Kimi models need no extra space.

## Running Oscar

Oscar requires a Mac with Apple Silicon (M1 to M5) and macOS 27 or later, with the minimum required memory of the chosen model (see the table above).

### 1. Running Oscar from the binary release

1. Download `Oscar-<version>.dmg` from the [releases page](https://github.com/prp/oscar/releases),
open it and drag Oscar to Applications.
2. Launch Oscar. As the release is not notarised by Apple, macOS blocks the first launch with a
   dialog saying that "Oscar" was not opened. To allow Oscar to run, you need to change the
   security settings:
   - Click Done in the dialog (not Move to Bin).
   - Open System Settings > Privacy & Security and scroll down to Security.
   - Click Open Anyway next to the message that "Oscar" was blocked, and confirm with your password.

   Oscar's O icon then appears in the menu bar. Accept the offer to install the `oscar` command if
   you want to use the command line tool.
3. Open the menu and click the download arrow next to a model. Qwen3.6-35B-A3B is the smallest
   supported model (20 GB on disk, about 55 GB to install).
4. Click the model's name to serve it.
5. Choose Launch Chat to chat with the model in a terminal, or Launch OpenCode to start a coding
   session in a folder of your choice ([OpenCode](https://opencode.ai) must be installed separately).
   Any other OpenAI-compatible client can also connect directly to `http://127.0.0.1:11434/v1`.

### 2. Running Oscar from the source code

1. Install Xcode with the Metal toolchain, and [rustup](https://rustup.rs).
2. Get the source and prepare its dependencies:

   ```bash
   git clone --recursive https://github.com/prp/oscar.git
   cd oscar
   ./setup.sh                # repeat after every git pull to patch third-party dependencies
   ```

3. Build Oscar. One command builds both the command line binary and the menu bar app:

   ```bash
   cargo app                 # target/release/oscar and target/release/Oscar.app
   ```

4. Launch the Oscar menu bar app and continue as with the binary release, or use the `oscar` command
   directly:

   ```bash
   open target/release/Oscar.app
   target/release/oscar list
   ```

### 3. Using Oscar from the command line

With the `oscar` command installed (step 2 of the binary release, or the source build), download a
model and chat with it:

```bash
oscar download --model qwen3.6-35b-a3b
oscar chat --model qwen3.6-35b-a3b
```

The commands of `oscar`:

| Command | What it does |
|---|---|
| `oscar list` | Lists the supported models and which are on disk |
| `oscar download --model <MODEL>` | Downloads a model from Hugging Face and re-quantises it |
| `oscar serve --model <MODEL>` | Serves a model as an OpenAI-compatible server on port 11434 |
| `oscar chat --model <MODEL>` | Chats with a model in the terminal |
| `oscar check-model --model <MODEL>` | Checks a model's files and its memory plan on this machine |
| `oscar print-config --model <MODEL>` | Prints every setting a launch would use |
| `oscar delete --model <MODEL>` | Removes a model from disk |

Without `--model`, Oscar uses the model last selected in the menu bar app. `oscar <command> --help`
lists all options of a command; the most important ones are described under Configuration.

Each run of `oscar serve` or `oscar chat` writes a log to `~/.oscar/oscar.log`, with its memory
plan and every request's token rates and SSD figures. The logs of the nine runs before it are kept
as `oscar.log.1` to `oscar.log.9`, and no log grows beyond 16 MB. The menu bar app writes the same
log (Open Log in its menu).

## Technical details

### Configuration

Oscar is configured through command line options and environment variables.

The main options of `oscar serve` and `oscar chat`:

| Option | Description | Default |
|---|---|---|
| `--mem <GB>` | Maximum memory that Oscar uses | The physical memory that the machine has available  |
| `--static-mem` | Disables elastic memory: Oscar keeps the memory that it allocates at load time | Elastic memory |
| `--max-input-tokens <N>` | Maximum prompt length; a smaller value leaves more memory for experts | Model-specific; 131,072 for most models |
| `--max-output-tokens <N>` | Output length guaranteed after a prompt of maximum length | Model-specific; 16,384 for most models |
| `--kv-cache-dir <DIR>` | Directory for the session state (KV cache) on disk; an empty value disables it | `~/.oscar/kv_cache` |
| `--host <HOST>`, `--port <PORT>` | Address of the server | `127.0.0.1`, `11434` |

Environment variables:

| Variable | Description | Default |
|---|---|---|
| `OSCAR_DRAFT=self\|none` | Enables or disables self-drafting | Model-specific |
| `OSCAR_APPROX_ROUTING=<θ>` | Enables approximate routing: a selected expert that is not in memory and has a routing weight below θ is replaced by an expert in memory | Disabled |

#### Setting wired memory limits

Oscar needs to keep model weights in wired memory, i.e. memory that macOS cannot page out. By default, macOS limits wired memory to about 80% of a machine's physical memory. Oscar works within these limits, but raising them gives Oscar more memory and thus a higher decoding rate for large models. On a Mac with 28 GB of memory or more, the following command raises the limits so that all but 5 GB of memory can be wired:

```bash
sudo sysctl vm.global_no_user_wire_amount=$((5 << 30)) vm.user_wire_limit=$(($(sysctl -n hw.memsize) - (5 << 30))) iogpu.wired_limit_mb=$((($(sysctl -n hw.memsize) >> 20) - 5120))
```

The limits are reset at each reboot. On a Mac with less than 28 GB of memory, the default limits are higher than the ones above and should be kept.

## Acknowledgements

Oscar builds on [mistral.rs](https://github.com/EricLBuehler/mistral.rs) and [candle](https://github.com/huggingface/candle), on the GGUF model format of [llama.cpp](https://github.com/ggml-org/llama.cpp), and on the quantised models published by [Unsloth](https://huggingface.co/unsloth) and [KarLexAI](https://huggingface.co/KarLexAI).

## License

Copyright © 2026 Imperial College London. Oscar is licensed under either the [MIT license](LICENSE-MIT) or the [Apache License 2.0](LICENSE-APACHE), at your option.
