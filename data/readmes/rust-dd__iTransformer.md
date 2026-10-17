![Build Workflow](https://github.com/rust-dd/iTransformer/actions/workflows/rust.yml/badge.svg)
[![Crates.io](https://img.shields.io/crates/v/itransformer?style=flat-square)](https://crates.io/crates/itransformer)
![License](https://img.shields.io/crates/l/itransformer?style=flat-square)

# iTransformer: Rust Implementation

An **iTransformer** implementation in **Rust** using [Hugging Face Candle](https://github.com/huggingface/candle), inspired by the [lucidrains iTransformer repository](https://github.com/lucidrains/iTransformer), and based on the original research and implementation from [Tsinghua University's iTransformer repository](https://github.com/thuml/iTransformer).

## 📚 **What is iTransformer?**

iTransformer introduces an **inverted Transformer architecture** designed for **multivariate time series forecasting (MTSF)**. By reversing the conventional structure of Transformers, iTransformer achieves state-of-the-art results in handling complex multivariate time series data.

### 🚀 **Key Features:**
- **Inverted Transformer Architecture:** Captures multivariate correlations efficiently.
- **Layer Normalization & Feed-Forward Networks:** Optimized for time series representation.
- **Flexible Prediction Lengths:** Supports predictions at multiple horizons (e.g., 12, 24, 36, 48 steps ahead).
- **Scalability:** Handles hundreds of variates with efficiency.
- **Zero-Shot Generalization:** Train on partial variates and generalize to unseen variates.
- **Multiple Model Variants:** ITransformer, ITransformer2D, and ITransformerFFT.
- **Hardware Acceleration:** Metal (macOS) and CUDA support via Candle.

### 🛠️ **Architecture Overview**

iTransformer treats each time series variate as a **token**, applying attention mechanisms across variates, followed by feed-forward networks and normalization layers.

![Architecture](https://raw.githubusercontent.com/thuml/iTransformer/main/figures/architecture.png)

### 📊 **Key Benefits:**
- **State-of-the-Art Performance:** On benchmarks such as Traffic, Weather, and Electricity datasets.
- **Improved Interpretability:** Multivariate self-attention reveals meaningful correlations.
- **Scalable and Efficient Training:** Can accommodate long time series without performance degradation.

### 📈 **Performance Highlights:**

iTransformer consistently outperforms other Transformer-based architectures in multivariate time series forecasting benchmarks.

![Results](https://raw.githubusercontent.com/thuml/iTransformer/main/figures/main_results_alipay.png)

## 📥 **Installation**

To get started, ensure you have Rust and Cargo installed. Then:

```bash
# Add iTransformer to your project dependencies
cargo add itransformer
```

For GPU acceleration:
```bash
# macOS Metal support
cargo add itransformer --features metal

# CUDA support
cargo add itransformer --features cuda
```

## 🏗️ **Model Variants**

This library provides three model variants:

| Model | Description |
|-------|-------------|
| `ITransformer` | Base inverted transformer for multivariate time series forecasting |
| `ITransformer2D` | Extended variant with granular time attention via `num_time_tokens` parameter |
| `ITransformerFFT` | Variant with additional Fourier tokens prepended to the attention sequence |

## 📝 **Usage**

### ITransformer (Base Model)

```rust
use candle_core::{Device, DType, Tensor};
use candle_nn::{VarBuilder, VarMap};
use itransformer::ITransformer;

fn main() -> candle_core::Result<()> {
    let device = Device::Cpu;
    let varmap = VarMap::new();
    let vb = VarBuilder::from_varmap(&varmap, DType::F32, &device);
    
    let model = ITransformer::new(
        vb,
        137,                      // num_variates
        96,                       // lookback_len
        6,                        // depth
        256,                      // dim
        Some(1),                  // num_tokens_per_variate
        vec![12, 24, 36, 48],     // pred_length
        Some(64),                 // dim_head
        Some(8),                  // heads
        None,                     // attn_drop_p
        None,                     // ff_mult
        None,                     // ff_drop_p
        None,                     // num_mem_tokens
        Some(true),               // use_reversible_instance_norm
        None,                     // reversible_instance_norm_affine
        false,                    // flash_attn
        &device,
    )?;
    
    let time_series = Tensor::randn(0f32, 1f32, (2, 96, 137), &device)?;
    let preds = model.forward(&time_series, None, false)?;
    println!("{:?}", preds);
    Ok(())
}
```

### ITransformer2D (Time Token Variant)

```rust
use candle_core::{Device, DType, Tensor};
use candle_nn::{VarBuilder, VarMap};
use itransformer::ITransformer2D;

fn main() -> candle_core::Result<()> {
    let device = Device::Cpu;
    let varmap = VarMap::new();
    let vb = VarBuilder::from_varmap(&varmap, DType::F32, &device);
    
    let model = ITransformer2D::new(
        vb,
        137,                      // num_variates
        96,                       // lookback_len
        4,                        // depth
        256,                      // dim
        8,                        // num_time_tokens (lookback_len must be divisible by this)
        vec![12, 24],             // pred_length
        Some(32),                 // dim_head
        Some(4),                  // heads
        None, None, None, None, None, None,
        false,                    // flash_attn
        &device,
    )?;
    
    let time_series = Tensor::randn(0f32, 1f32, (2, 96, 137), &device)?;
    let preds = model.forward(&time_series, None, false)?;
    println!("{:?}", preds);
    Ok(())
}
```

### ITransformerFFT (Fourier Token Variant)

```rust
use candle_core::{Device, DType, Tensor};
use candle_nn::{VarBuilder, VarMap};
use itransformer::ITransformerFFT;

fn main() -> candle_core::Result<()> {
    let device = Device::Cpu;
    let varmap = VarMap::new();
    let vb = VarBuilder::from_varmap(&varmap, DType::F32, &device);
    
    let model = ITransformerFFT::new(
        vb,
        137,                      // num_variates
        96,                       // lookback_len
        4,                        // depth
        256,                      // dim
        Some(1),                  // num_tokens_per_variate
        4,                        // num_fft_tokens
        vec![12, 24],             // pred_length
        Some(32),                 // dim_head
        Some(4),                  // heads
        None, None, None, None, None, None,
        false,                    // flash_attn
        &device,
    )?;
    
    let time_series = Tensor::randn(0f32, 1f32, (2, 96, 137), &device)?;
    let preds = model.forward(&time_series, None, false)?;
    println!("{:?}", preds);
    Ok(())
}
```

## 📁 **Project Structure**

```
src/
├── attend.rs           # Attention computation
├── attention.rs        # ToQKV, ToValueResidualMix, ToVGates, ToOut, Attention
├── feedforward.rs      # GEGLU, FeedForward
├── itransformer.rs     # Base ITransformer
├── itransformer2d.rs   # ITransformer2D with time tokens
├── itransformer_fft.rs # ITransformerFFT with Fourier tokens
├── lib.rs              # Module declarations and re-exports
├── mlp_in.rs           # Input projection layer
├── pred_head.rs        # Prediction heads
├── revin.rs            # Reversible Instance Normalization
```


## 📖 **References**

- **Paper:** [iTransformer: Inverted Transformers Are Effective for Time Series Forecasting](https://arxiv.org/abs/2310.06625)
- **Original Implementation:** [thuml/iTransformer](https://github.com/thuml/iTransformer)
- **Inspired by:** [lucidrains/iTransformer](https://github.com/lucidrains/iTransformer)

## 🏆 **Acknowledgments**

This work draws inspiration and insights from the following projects:
- [Reformer](https://github.com/lucidrains/reformer-pytorch)
- [Informer](https://github.com/zhouhaoyi/Informer2020)
- [FlashAttention](https://github.com/shreyansh26/FlashAttention-PyTorch)
- [Autoformer](https://github.com/thuml/Autoformer)
- [Time-Series-Library](https://github.com/thuml/Time-Series-Library)

Special thanks to the contributors and researchers behind iTransformer for their pioneering work.

## 📑 **Citation**

```bibtex
@article{liu2023itransformer,
  title={iTransformer: Inverted Transformers Are Effective for Time Series Forecasting},
  author={Liu, Yong and Hu, Tengge and Zhang, Haoran and Wu, Haixu and Wang, Shiyu and Ma, Lintao and Long, Mingsheng},
  journal={arXiv preprint arXiv:2310.06625},
  year={2023}
}
```

## 🌟 **Contributing**

Contributions are welcome! Please follow the standard GitHub pull request process and ensure your code adheres to Rust best practices.

---

This repository is a Rust adaptation of the cutting-edge iTransformer model, aiming to bring efficient and scalable time series forecasting capabilities to the Rust ecosystem.
