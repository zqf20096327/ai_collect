# Deep-Learning-Accelerator-Transformer-FPGA

This project implements a **Transformer model** architecture from scratch, directly onto an **FPGA**.  
Each essential block of the Transformer is modularized in **Verilog**, focusing on **matrix processing**, **parallelism**, and **hardware efficiency**.


## Project Structure

| Module Name                     | Description                                          |
| -------------------------------- | ---------------------------------------------------- |
| `PositionalEncoding.v`           | Adds positional information to input embeddings.     |
| `encoder_layer.v`                | Complete encoder layer: attention + feedforward.     |
| `feedforward.v`                  | Feedforward neural network layer.                    |
| `layer_normalisation.v`          | Normalizes activations for stable training.           |
| `masked_multi_attention_head.v`  | Implements masked multi-head self-attention.          |
| `multi-attention_layer.v`        | Implements standard multi-head self-attention.        |


## Key Features

- **Matrix Processing Acceleration**  
  All major computations (dot products, matrix multiplications, additions) are optimized and parallelized for FPGA execution.

- **Modular Layer Design**  
  Each Transformer component (attention, feedforward, normalization, positional encoding) is separately implemented for flexibility and testing.

- **Hardware Efficiency**  
  Design focuses on **pipelining**, **parallelism**, and **resource optimization** for real-time inference applications.

- **Scalability**  
  The design allows easy scaling of the number of attention heads, model dimension size, and layer stacking.


## How It Works

1. **Input Data** is passed with positional encoding.
2. **Multi-Head Attention** computes context vectors.
3. **Layer Normalization** ensures stability and faster convergence.
4. **Feedforward Networks** add non-linearity and learning capacity.
5. **Stacked Encoder Layers** enable deeper feature extraction.
6. **Matrix Computations** are heavily optimized using FPGA-specific design patterns (e.g., parallel MAC units, dataflow pipelining).


## Applications

- **Real-Time NLP Acceleration** on Edge Devices
- **Low-Latency Inference** for Vision Transformers (ViTs)
- **Energy-Efficient** Deep Learning Processing
- **Autonomous Systems**, **Medical Imaging**, and **Surveillance**
  

## Future Work

- Extend to **full Transformer encoder-decoder** design.
- Implement **dynamic quantization** for further resource optimization.
- Integrate **AXI interfaces** for easy SoC integration.

## License:
This project is licensed under the [MIT License](LICENSE).

## Contact

Feel free to reach out for collaborations or just a friendly hello!

-   **Email:** naharjainam91@gmail.com
-   **LinkedIn:** https://www.linkedin.com/in/jainam-nahar-280292253
-   **GitHub:** https://github.com/jainamnahar14surat
-   **Website** https://jaina-portfolio.netlify.app/
