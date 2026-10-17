# kannolo

Official kANNolo library for Kolmogorov-Arnold neural network operations

```
cargo add kannolo
```

```rust
use kannolo::{KAN, SplineConfig};

fn main() {
    let config = SplineConfig {
        grid_size: 5,
        spline_order: 3,
    };
    
    let mut kan = KAN::new(&[2, 5, 1], config);
    
    let input = vec![0.5, -0.3];
    let output = kan.forward(&input);
    
    println!("output: {:?}", output);
}
```

## notes

KANs replace fixed activation functions with learnable univariate functions on edges. Each edge learns a spline (B-spline basis by default). This makes the network more interpretable and often more parameter-efficient than MLPs.

The KA representation theorem says any multivariate continuous function can be written as sums and compositions of univariate functions. That's the theory. In practice, you get networks that are easier to visualize and prune.

Grid size controls spline resolution. Higher values give more expressive functions but cost more parameters. Spline order is typically 3 (cubic). Start with grid_size=5 and tune from there.

Training uses standard backprop. The spline coefficients are the learnable parameters.

```rust
use kannolo::{KAN, SplineConfig, Optimizer, Loss};

fn train_xor() {
    let config = SplineConfig {
        grid_size: 5,
        spline_order: 3,
    };
    
    let mut kan = KAN::new(&[2, 4, 1], config);
    let mut opt = Optimizer::adam(0.01);
    
    let data = vec![
        (vec![0.0, 0.0], vec![0.0]),
        (vec![0.0, 1.0], vec![1.0]),
        (vec![1.0, 0.0], vec![1.0]),
        (vec![1.0, 1.0], vec![0.0]),
    ];
    
    for epoch in 0..1000 {
        let mut total_loss = 0.0;
        
        for (x, y) in &data {
            let pred = kan.forward(x);
            let loss = Loss::mse(&pred, y);
            total_loss += loss;
            
            kan.backward(y);
            opt.step(&mut kan);
        }
        
        if epoch % 100 == 0 {
            println!("epoch {}: loss = {:.6}", epoch, total_loss / data.len() as f32);
        }
    }
}
```

MIT
