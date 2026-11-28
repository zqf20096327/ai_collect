# NeurCo

**Neural Rendering Compiler: Generative Video Models as Programmable Renderers**

<p align="center">
  <a href="https://openraiser.github.io/NeurCo/"><img src="https://img.shields.io/badge/Project-Page-2b7fff" alt="Project Page"></a>
  <a href="https://github.com/OpenRaiser/NeurCo"><img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://huggingface.co/datasets/Fortunaa/NeurCo-VComBench"><img src="https://img.shields.io/badge/Dataset-VComBench-FFD21E?logo=huggingface&logoColor=black" alt="VComBench dataset"></a>
  <a href="https://huggingface.co/datasets/Fortunaa/Neurco-Vbench2-testmini"><img src="https://img.shields.io/badge/Result-VBench--2.0-FFD21E?logo=huggingface&logoColor=black" alt="VBench-2.0 results"></a>
  <a href="https://huggingface.co/datasets/Fortunaa/Neurco-SciVbench-testmini"><img src="https://img.shields.io/badge/Result-Sci--VBench-FFD21E?logo=huggingface&logoColor=black" alt="Sci-VBench results"></a>
</p>

NeurCo probes a frozen video model and turns what that model can reliably do into a capability manual. A request is written as a model-agnostic program of objects, constraints, events, and cameras, then compiled into text, external operators, or both. Requirements the model already handles stay as they are. The rest are rewritten or routed to another execution strategy.

Author One\* · Author Two\* · Author Three · Author Four · Author Five

Institution Placeholder · \*Equal contribution

## Method

NeurCo treats a frozen video model as a backend whose instruction set is not known in advance. It measures that backend once, then compiles each request against the measurement.

![Overview of NeurCo. Offline profiling builds a capability manual. Online compilation keeps supported requirements and adapts the rest into a prompt, conditions, and operations.](assets/overview.png)

Offline, probe tasks run on the frozen model and are scored into a capability manual: which control, at which difficulty, under which input mode. Online, a request is split into requirements. Requirements the manual marks as supported stay unchanged. Weak ones are rewritten or handed to an external operator. The execution plan is a prompt, optional visual conditions, and operations, rendered by the same frozen model.

![NeurCo pipeline. (A) Offline probing builds a capability manual. (B) Requests are parsed into an IR and compiled with the manual. (C) Execution uses text rewriting or a motion reference on a frozen model.](assets/method.png)

**A. Offline capability profiling.** A shared vocabulary of semantic controls is probed at graded difficulty under text-to-video, image-to-video, and reference-to-video. Each trial is judged. The manual stores the success rate and a status of ok, weak, bad, or unknown when a control was not scored.

**B. Capability-guided compilation.** The request becomes a model-agnostic intermediate representation of objects, constraints, events, and cameras. The compiler looks up the manual for the target model. Supported requirements stay in the original prompt. Unsupported ones are adapted only when a compatible intervention exists: a text rewrite, a reference image, a first frame, a proxy video, or shot concatenation. If none applies, the requirement is kept and left unresolved.

**C. Backends and execution.** One path rewrites the prompt and can retain a first frame. Another supplies a motion reference when text alone cannot carry the motion, and falls back to text if that reference does not validate. The generator stays frozen.

## VComBench

VComBench has 380 compositional tasks across T2V, I2V, and R2V, with 1,617 scored requirements over 34 controls. The tasks are released at [Fortunaa/NeurCo-VComBench](https://huggingface.co/datasets/Fortunaa/NeurCo-VComBench). **Req.** is requirement satisfaction. **All** is joint success on every requirement of a task. A video can satisfy some requirements and still fail the task.

<table>
  <tr>
    <td width="50%"><img src="assets/vcombench.png" alt="VComBench composition: 128 text-to-video, 113 image-to-video, and 139 reference-to-video tasks, with representative controls for content, space, motion, time, camera, and appearance."></td>
    <td width="50%"><img src="assets/scoring.png" alt="Requirement satisfaction versus joint task success. Satisfying two of three requirements scores 2/3 on Req. and 0 on All."></td>
  </tr>
</table>

NeurCo (T) is text-only compilation. NeurCo (T+O) also uses external operators. External PE is an external prompt enhancer.

| Method | H3 Req. / All | Wan Req. / All | Seedance 2.5 Req. / All |
| --- | --- | --- | --- |
| Native | 66.5 / 28.2 | 46.8 / 8.4 | 68.5 / 26.9 |
| NeurCo (T) | 67.7 / 27.9 | 47.9 / 8.4 | **69.7 / 27.5** |
| NeurCo (T+O) | **69.3** / 25.3 | **52.3 / 11.8** | 68.2 / 25.8 |
| External PE | 72.5 / 33.2 | 50.6 / 12.7 | 71.3 / 31.1 |
| External PE + NeurCo (O) | **73.0** / 33.7 | **52.5 / 14.5** | **72.1 / 32.2** |
| External PE + NeurCo (T) | 72.4 / 32.7 | 46.3 / 9.0 | 71.7 / 32.1 |
| External PE + NeurCo (T+O) | 72.0 / **34.5** | 50.0 / 12.3 | 71.8 / 31.5 |

On native inputs, text-only compilation is strongest for Seedance 2.5 (68.5→69.7 Req.). Wan and H3 gain more from text plus operators (46.8→52.3 and 66.5→69.3 Req.).

The project page shows a small set of Native vs NeurCo clips for H3, Wan, and Seedance 2.5. Wan reference-to-video clips are labeled R2V (VACE).

## Data

- [VComBench](https://huggingface.co/datasets/Fortunaa/NeurCo-VComBench)
- [VBench-2.0 testmini results](https://huggingface.co/datasets/Fortunaa/Neurco-Vbench2-testmini)
- [Sci-VBench testmini results](https://huggingface.co/datasets/Fortunaa/Neurco-SciVbench-testmini)

## Citation

```bibtex
@article{neurco2026,
  title   = {Neural Rendering Compiler: Generative Video Models as Programmable Renderers},
  author  = {Author One and Author Two and Author Three and Author Four and Author Five},
  journal = {arXiv preprint},
  year    = {2026}
}
```

## License

[MIT](LICENSE)
