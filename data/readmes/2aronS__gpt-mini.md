# gpt-mini

![license](https://img.shields.io/badge/license-MIT-blue)
![status](https://img.shields.io/badge/status-active-brightgreen)
![rust](https://img.shields.io/badge/rust-1.70%2B-orange)
![build](https://img.shields.io/badge/build-passing-success)

> Pure Rust implementation of a minimal GPT transformer

A small, educational implementation of a GPT-style transformer in Rust. Good for learning how transformers work under the hood without framework abstractions.

## table of contents

- [install](#install)
- [usage](#usage)
- [api](#api)
- [contributing](#contributing)
- [license](#license)

## install

```bash
cargo add gpt-mini
```

Or add to `Cargo.toml`:

```toml
[dependencies]
gpt-mini = "0.1"
```

## usage

```rust
use gpt_mini::{GPTConfig, GPT, Tokenizer};

fn main() {
    // configure model
    let config = GPTConfig {
        vocab_size: 50257,
        n_layer: 12,
        n_head: 12,
        n_embd: 768,
        block_size: 1024,
        dropout: 0.1,
    };
    
    // initialize model
    let mut model = GPT::new(config);
    
    // tokenize input
    let tokenizer = Tokenizer::new("vocab.json");
    let tokens = tokenizer.encode("Hello, world!");
    
    // generate
    let output = model.generate(&tokens, 50);
    let text = tokenizer.decode(&output);
    
    println!("{}", text);
}
```

Training example:

```rust
use gpt_mini::{GPT, Trainer, Dataset};

let dataset = Dataset::from_file("data.txt")?;
let mut trainer = Trainer::new(model, dataset);

trainer.train(
    epochs: 10,
    batch_size: 32,
    learning_rate: 3e-4,
)?;

trainer.save("model.bin")?;
```

## api

### `GPTConfig`

Configuration struct for model architecture.

| field | type | description |
|-------|------|-------------|
| `vocab_size` | `usize` | vocabulary size |
| `n_layer` | `usize` | number of transformer layers |
| `n_head` | `usize` | number of attention heads |
| `n_embd` | `usize` | embedding dimension |
| `block_size` | `usize` | maximum sequence length |
| `dropout` | `f32` | dropout probability |

### `GPT`

Main model struct.

**Methods:**

- `new(config: GPTConfig) -> Self` - create new model with random weights
- `from_pretrained(path: &str) -> Result<Self>` - load pretrained weights
- `forward(&mut self, idx: &[usize]) -> Tensor` - forward pass
- `generate(&mut self, idx: &[usize], max_tokens: usize) -> Vec<usize>` - generate tokens

### `Tokenizer`

BPE tokenizer for text encoding/decoding.

**Methods:**

- `new(vocab_path: &str) -> Self` - load vocabulary
- `encode(&self, text: &str) -> Vec<usize>` - text to tokens
- `decode(&self, tokens: &[usize]) -> String` - tokens to text

### `Trainer`

Training loop implementation.

**Methods:**

- `new(model: GPT, dataset: Dataset) -> Self` - create trainer
- `train(&mut self, epochs: usize, batch_size: usize, learning_rate: f32) -> Result<()>` - run training
- `save(&self, path: &str) -> Result<()>` - save model checkpoint

## contributing

prs welcome. open an issue first for big changes.

Run tests with:

```bash
cargo test
```

Format code:

```bash
cargo fmt
```

## license

MIT
