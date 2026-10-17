# 📚 `edufsdp`

A minimal and educational implementation of Fully Sharded Data Parallel (FSDP).

Built by digging through PyTorch's FSDP codebase and isolating the core mechanics of [sharding](https://github.com/0xNaN/edufsdp/blob/master/src/edufsdp/edufsdp.py#L137-L152), [gathering](https://github.com/0xNaN/edufsdp/blob/master/src/edufsdp/edufsdp.py#L199-L209), and [state transitions](https://github.com/0xNaN/edufsdp/blob/master/src/edufsdp/edufsdp.py#L44-L102) for educational clarity.
</br></br>

## Features and Limitations

This implementation mirrors some of the core concepts of [`torch.distributed.fsdp`](https://github.com/pytorch/pytorch/tree/main/torch/distributed/fsdp):

### Features

- _Parameter Sharding_: Implements a `FULL_SHARD` strategy, where model parameters, gradients, and optimizer states are sharded across data-parallel ranks.
- _Auto Wrapping_: Provides a policy-based function (`wrap_fn`) for automatically wrapping and sharding.
- _Activation Checkpointing_: Supports activation checkpointing for memory efficiency during forward and backward passes.

### Limitations

This implementation mainly aims to show FSDP states and communication. As such, it lacks many optimizations and features of the official PyTorch FSDP, for example:

- _Sync Collectives_: All collective operations (`all_gather`, `reduce_scatter`) are blocking, with no overlap between communication and computation (i.e., no prefetching).
- _No Mixed Precision_: Does not support mixed precision; computations/communication are performed using the provided dtype (e.g., master weights are not forced to be `float32`).
- _No Meta Device_: Doesn't use the meta device to optimize sharding.
- _No CPU Offloading_: Sharded parameters remain on the GPU, with no mechanism for CPU offloading to save memory.

## Quick Setup

Ensure you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/), then:

```bash
uv sync
```

Alternatively, you can use standard `pip` and `venv`:
```bash
python3.11 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install .
```

## Run

You can run a minimal training loop comparing `edufsdp` with the standard `torch` FSDP, by training a fresh Qwen2-0.5 on [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories):

```bash
# Two ranks, Qwen2-0.5B and EduFSDP
PROCESSES=2 MODEL=qwen2 BACKEND=nccl MBS=8 ACC=2 STEPS=3 EVAL=0 FSDP=edufsdp ./scripts/train.sh
```
```bash
Ranks = 2, FSDP = edufsdp, Acc = 2
1/3: Loss = 12.067031, Peak = 13006.0 MB, Time = 6.7548s
2/3: Loss = 11.321454, Peak = 15382.0 MB, Time = 1.0896s
3/3: Loss = 10.492050, Peak = 15382.0 MB, Time = 1.0921s
```
```bash
# ...same with FSDP=torch
Ranks = 2, FSDP = torch, Acc = 2
1/3: Loss = 12.067031, Peak = 14238.0 MB, Time = 7.7054s
2/3: Loss = 11.321454, Peak = 16614.0 MB, Time = 1.1203s
3/3: Loss = 10.492050, Peak = 16614.0 MB, Time = 1.1080s
```

Let it run long enough if you only care about stories (`EVAL=20 STEPS=1000`):
```text
280/1000: Loss = 3.615633, Peak = 15382.0 MB, Time = 1.1021s
281/1000: Loss = 3.493644, Peak = 15382.0 MB, Time = 1.1021s
=== eval ===
Once upon a time there was a young little girl named Lily. She loved to sing all day. One day
282/1000: Loss = 3.390410, Peak = 15382.0 MB, Time = 2.4894s
283/1000: Loss = 3.459949, Peak = 15382.0 MB, Time = 1.1043s
```

### On CPU
If you don't have access to an NVIDIA GPU, you can try with the GLOO backend on CPU (also with a very tiny model to just make the code run):
```bash
PROCESSES=2 MODEL=tiny MBS=16 ACC=2 STEPS=3 EVAL=0 FSDP=edufsdp ./scripts/train.sh
```
```
Ranks = 2, FSDP = edufsdp, Acc = 2
1/3: Loss = 1.021882, Peak = N/A, Time = 0.0362s
2/3: Loss = 1.010545, Peak = N/A, Time = 0.0035s
3/3: Loss = 1.040771, Peak = N/A, Time = 0.0027s
```

## Profiling

Memory visualization for a single training step (GBS=8, SEQ=256) of Qwen2-0.5B across two GPUs, generated using the [PyTorch Memory Visualizer](https://docs.pytorch.org/memory_viz):

<div align="center">

|                                                            EduFSDP                                                            |                                                          PyTorch FSDP                                                          |
| :---------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------: |
| <a href="./assets/qwen2-edufsdp-step1.png"><img src="./assets/qwen2-edufsdp-step1.png" width="400" alt="EduFSDP Profile"></a> | <a href="./assets/qwen2-torch-step1.png"><img src="./assets/qwen2-torch-step1.png" width="400" alt="PyTorch FSDP Profile"></a> |

</div>

## Useful Links

- https://github.com/pytorch/pytorch/tree/main/torch/distributed/fsdp
- https://dev-discuss.pytorch.org/t/rethinking-pytorch-fully-sharded-data-parallel-fsdp-from-first-principles/1019
- https://iitm-pod.slides.com/arunprakash_ai/pytorch#/0/12/1
