# MuonClip

This is a simple implementation of MuonClip in pure pytorch from the Kimi K2 Paper. [Read it here](https://arxiv.org/pdf/2507.20534)

## Code

```python
import torch
import torch.nn as nn
from typing import Optional, Dict, Any, List
import math


def newton_schulz_iteration(M: torch.Tensor, num_iterations: int = 5) -> torch.Tensor:
    """
    Perform Newton-Schulz iteration to orthogonalize a matrix.
    
    The Newton-Schulz iteration computes an approximate orthogonal matrix
    from M by iteratively refining: X_{k+1} = X_k * (3I - X_k^T X_k) / 2
    
    Args:
        M: Input matrix to orthogonalize
        num_iterations: Number of iterations (default: 5)
    
    Returns:
        Approximately orthogonal matrix
    """
    # Initialize with normalized input
    X = M / (M.norm() + 1e-7)
    
    # Iteratively refine
    for _ in range(num_iterations):
        # X = X * (3I - X^T X) / 2
        X = 1.5 * X - 0.5 * X @ (X.T @ X)
    
    return X


class MuonClip(torch.optim.Optimizer):
    """
    MuonClip optimizer as described in Kimi K2 paper.
    
    Combines the token-efficient Muon optimizer with QK-Clip for stability.
    
    Args:
        params: Iterable of parameters to optimize
        lr: Learning rate (default: 2e-4)
        momentum: Momentum coefficient (default: 0.95)
        weight_decay: Weight decay coefficient (default: 0.1)
        qk_clip_threshold: Maximum attention logit threshold τ (default: 100.0)
        qk_clip_alpha: Balance parameter for Q/K scaling (default: 0.5)
        newton_schulz_iters: Number of Newton-Schulz iterations (default: 5)
        rms_scale_factor: RMS scaling factor (default: 0.2)
    """
    
    def __init__(
        self,
        params,
        lr: float = 2e-4,
        momentum: float = 0.95,
        weight_decay: float = 0.1,
        qk_clip_threshold: float = 100.0,
        qk_clip_alpha: float = 0.5,
        newton_schulz_iters: int = 5,
        rms_scale_factor: float = 0.2,
    ):
        if lr < 0.0:
            raise ValueError(f"Invalid learning rate: {lr}")
        if momentum < 0.0 or momentum >= 1.0:
            raise ValueError(f"Invalid momentum value: {momentum}")
        if weight_decay < 0.0:
            raise ValueError(f"Invalid weight_decay value: {weight_decay}")
        
        defaults = dict(
            lr=lr,
            momentum=momentum,
            weight_decay=weight_decay,
            qk_clip_threshold=qk_clip_threshold,
            qk_clip_alpha=qk_clip_alpha,
            newton_schulz_iters=newton_schulz_iters,
            rms_scale_factor=rms_scale_factor,
        )
        super().__init__(params, defaults)
    
    @torch.no_grad()
    def step(self, closure=None, attention_max_logits: Optional[Dict[str, torch.Tensor]] = None):
        """
        Performs a single optimization step.
        
        Args:
            closure: A closure that reevaluates the model and returns the loss
            attention_max_logits: Dict mapping layer names to max logit values per head
                                 Format: {"layer.0.attn": tensor([max_logit_head_0, ...])}
        
        Returns:
            Optional loss from closure
        """
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()
        
        # Step 1: Muon optimizer update
        for group in self.param_groups:
            lr = group['lr']
            momentum = group['momentum']
            weight_decay = group['weight_decay']
            ns_iters = group['newton_schulz_iters']
            rms_scale = group['rms_scale_factor']
            
            for p in group['params']:
                if p.grad is None:
                    continue
                
                grad = p.grad
                state = self.state[p]
                
                # Initialize momentum buffer
                if 'momentum_buffer' not in state:
                    state['momentum_buffer'] = torch.zeros_like(grad)
                
                momentum_buffer = state['momentum_buffer']
                
                # Only apply Muon to 2D weight matrices
                if grad.dim() == 2:
                    n, m = grad.shape
                    
                    # Update momentum: M_t = μ * M_{t-1} + G_t
                    momentum_buffer.mul_(momentum).add_(grad)
                    
                    # Apply Newton-Schulz orthogonalization
                    ortho_update = newton_schulz_iteration(
                        momentum_buffer, 
                        num_iterations=ns_iters
                    )
                    
                    # Scale to match Adam RMS: O_t = NS(M_t) * sqrt(max(n,m)) * 0.2
                    scale_factor = math.sqrt(max(n, m)) * rms_scale
                    ortho_update = ortho_update * scale_factor
                    
                    # Apply weight decay and update: W_t = W_{t-1} - η(O_t + λW_{t-1})
                    p.add_(ortho_update, alpha=-lr)
                    p.add_(p, alpha=-lr * weight_decay)
                    
                else:
                    # For non-2D parameters (biases, norms), use simple momentum + weight decay
                    momentum_buffer.mul_(momentum).add_(grad)
                    p.add_(momentum_buffer, alpha=-lr)
                    if weight_decay > 0:
                        p.add_(p, alpha=-lr * weight_decay)
        
        # Step 2: QK-Clip
        if attention_max_logits is not None:
            self._apply_qk_clip(attention_max_logits)
        
        return loss
    
    @torch.no_grad()
    def _apply_qk_clip(self, attention_max_logits: Dict[str, torch.Tensor]):
        """
        Apply QK-Clip to attention weights based on max logits per head.
        
        Args:
            attention_max_logits: Dict mapping parameter names to max logit per head
                Example structure for tracking:
                {
                    "layer.0.attn.Wq_c": tensor([max_logit_head_0, max_logit_head_1, ...]),
                    "layer.0.attn.Wk_c": tensor([...]),
                }
        """
        tau = self.defaults['qk_clip_threshold']
        alpha = self.defaults['qk_clip_alpha']
        
        for group in self.param_groups:
            for p in group['params']:
                param_name = self._get_param_name(p)
                
                if param_name not in attention_max_logits:
                    continue
                
                max_logits = attention_max_logits[param_name]
                
                # Determine which heads need clipping
                needs_clip = max_logits > tau
                
                if not needs_clip.any():
                    continue
                
                # Compute per-head scaling factors: γ_h = min(1, τ / S^h_max)
                gamma = torch.clamp(tau / max_logits, max=1.0)
                
                # Apply different scaling based on component type
                if 'Wq_c' in param_name or 'Wk_c' in param_name:
                    # Head-specific components: scale by sqrt(γ)
                    sqrt_gamma = torch.sqrt(gamma)
                    self._scale_attention_heads(p, sqrt_gamma, needs_clip)
                    
                elif 'Wq_r' in param_name:
                    # Query rotary: scale by γ
                    self._scale_attention_heads(p, gamma, needs_clip)
                    
                elif 'Wk_r' in param_name:
                    # Key rotary (shared): don't touch to avoid cross-head effects
                    pass
    
    @staticmethod
    def _scale_attention_heads(
        param: torch.Tensor, 
        scale_factors: torch.Tensor, 
        mask: torch.Tensor
    ):
        """
        Scale specific attention heads in a parameter tensor.
        
        Args:
            param: Parameter tensor (shape depends on architecture)
            scale_factors: Scaling factor per head
            mask: Boolean mask indicating which heads to scale
        """
        # Assumes first dimension is the head dimension
        # This may need adjustment based on actual weight layout
        num_heads = scale_factors.shape[0]
        
        if param.dim() == 2:
            # Shape: [num_heads * head_dim, in_features] or similar
            head_dim = param.shape[0] // num_heads
            
            for h in range(num_heads):
                if mask[h]:
                    start_idx = h * head_dim
                    end_idx = (h + 1) * head_dim
                    param[start_idx:end_idx] *= scale_factors[h]
        
        elif param.dim() == 3:
            # Shape: [num_heads, head_dim, in_features]
            for h in range(num_heads):
                if mask[h]:
                    param[h] *= scale_factors[h]
    
    def _get_param_name(self, param: torch.Tensor) -> str:
        """Helper to get parameter name for tracking."""
        # This would need to be implemented with proper parameter name tracking
        # In practice, you'd maintain a mapping in __init__ or use named_parameters
        if not hasattr(self, '_param_to_name'):
            self._param_to_name = {}
        return self._param_to_name.get(id(param), "")
    
    def register_attention_params(
        self, 
        param_name_mapping: Dict[str, torch.nn.Parameter]
    ):
        """
        Register attention parameters for QK-Clip tracking.
        
        Args:
            param_name_mapping: Dict mapping descriptive names to parameters
                Example: {
                    "layer.0.attn.Wq_c": model.layer[0].attn.Wq_c,
                    "layer.0.attn.Wk_c": model.layer[0].attn.Wk_c,
                }
        """
        if not hasattr(self, '_param_to_name'):
            self._param_to_name = {}
        
        for name, param in param_name_mapping.items():
            self._param_to_name[id(param)] = name
```
