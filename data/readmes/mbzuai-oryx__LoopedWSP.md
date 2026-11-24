<h1 align="center">
  <img src="assets/villain_claude.svg" alt="Villain Claude logo" height="88" align="middle">&nbsp;
  Looped Weight-Space Programming
</h1>
<h3 align="center">LLM-Written Transformers for Long Algorithmic Reasoning</h3>

<p align="center">
  <a href="https://python-arch.github.io/">Abdelrahman Elsayed</a>*,
  <a href="https://ahmedheakl.github.io/">Ahmed Heakl</a>*,
  <a href="https://amshaker.github.io/">Abdelrahman Shaker</a>,
  <a href="https://sites.google.com/view/fahadkhans">Fahad Khan</a>,
  <a href="https://salman-h-khan.github.io/">Salman Khan</a>,
  <a href="https://www.anthropic.com/claude">Claude Opus 5.5</a>
  <br>
  <sub>* Equal contribution</sub>
</p>

<p align="center">
  <a href="https://mbzuai.ac.ae/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/mbzuai_logo_dark.svg"><img src="assets/mbzuai_logo.svg" alt="MBZUAI, Mohamed bin Zayed University of Artificial Intelligence" height="48"></picture></a>
</p>

<p align="center">
  <a href="https://mbzuai-oryx.github.io/LoopedWSP/"><img src="https://img.shields.io/badge/Blog-Read%20the%20post-eb6834?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDJoOWw1IDV2MTVINnoiLz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE1IDJ2NWg1Ii8%2BPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik05IDEyaDhNOSAxNmg4TTkgOGgzIi8%2BPC9zdmc%2B" alt="Read the blog post"></a>
  <a href="https://mbzuai-oryx.github.io/LoopedWSP/demo/maze.html"><img src="https://img.shields.io/badge/Demo-Maze-2a78d6?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHJlY3QgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHg9IjMiIHk9IjMiIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgcng9IjIiLz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTMgOWg2TTE1IDN2NmgtNE05IDE1djZNMjEgMTVoLTZ2LTNNOSAxNWgzIi8%2BPGNpcmNsZSBjeD0iNiIgY3k9IjYiIHI9IjEuNiIgZmlsbD0id2hpdGUiLz48Y2lyY2xlIGN4PSIxOCIgY3k9IjE4IiByPSIxLjYiIGZpbGw9IndoaXRlIi8%2BPC9zdmc%2B" alt="Maze demo"></a>
  <a href="https://mbzuai-oryx.github.io/LoopedWSP/demo/index.html"><img src="https://img.shields.io/badge/Demo-Tower%20of%20Hanoi-6250d6?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0yIDIxaDIwTTUgMjFWOE0xMiAyMVY4TTE5IDIxVjgiLz48cmVjdCB4PSIxLjUiIHk9IjE3IiB3aWR0aD0iNyIgaGVpZ2h0PSIzIiByeD0iMSIgZmlsbD0id2hpdGUiLz48cmVjdCB4PSIyLjUiIHk9IjEzLjUiIHdpZHRoPSI1IiBoZWlnaHQ9IjMiIHJ4PSIxIiBmaWxsPSJ3aGl0ZSIvPjxyZWN0IHg9IjMuNSIgeT0iMTAiIHdpZHRoPSIzIiBoZWlnaHQ9IjMiIHJ4PSIxIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg%3D%3D" alt="Tower of Hanoi demo"></a>
  <a href="https://huggingface.co/spaces/ahmedheakl/LoopedWSP"><img src="https://img.shields.io/badge/Hugging%20Face-Space-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face Space"></a>
</p>

<p align="center">
  <img src="assets/teaser.png" width="100%" alt="Two panels. On the left, a confused cartoon Claude is asked to solve a maze itself, draws a path that runs into a wall, and solves 26% of the test mazes. On the right, a scheming cartoon Claude works the weights of a small transformer like a puppeteer, and the transformer loops until it finds the right path, solving 100% of the test mazes.">
</p>

We asked Claude Opus 5.5 to find the shortest path through hard 30×30 mazes from [Maze-Hard](https://huggingface.co/datasets/sapientinc/maze-30x30-hard-1k), a benchmark whose shortest paths run longer than 110 steps. It solved only 26% of the test mazes it was given. So we asked it for something else, a transformer that solves the mazes. In one Claude Code session, Claude set all 19,936 weights of a small transformer by hand, with no training. It had the final weights 39 minutes after it received the task, at a cost of about $19. That transformer solves 100% of the test mazes.

The trick is the loop. The transformer is a single block that runs over and over, with each pass moving a shortest-path search one step further. A bigger maze therefore needs more passes rather than more weights. The same weights solve 100% of the mazes we generated at 60×60 and at 100×100, even though Claude checked the transformer only on mazes up to 45×45. The 19,936 weights aren't a minimum either. With a cap of 1,000 weights, a fresh Claude Code session wrote a maze transformer with only 928. Trained models such as LDT and EBR use about 1,900× more, yet this one still solves 100%. In our runs, gradient descent didn't find these weights. When we reset Claude's transformer to random weights and trained it on the same 1,000 training mazes, every run solved 0% of the test mazes.

We call this approach *looped weight-space programming*. Claude used it on eight more tasks from well-known benchmarks, writing a transformer for each that solved every test problem we gave it. Here are three of them.

- **Sudoku-Extreme.** The transformer guesses and backtracks when it gets stuck, and it solved every one of the 141,040 test puzzles we ran.
- **Tower of Hanoi.** One block of 3,686 weights loops over 2 million times to play all 1,048,575 moves of the 20-disk puzzle without a single mistake.
- **GraphWalks.** The transformer reads prompts of up to 1 million tokens and scores 100%, against 66.8% for Claude Opus 5.5 itself.

The weights of every transformer and the prompts Claude received are all in this repository.

## Watch it solve a maze

<p align="center">
  <a href="https://mbzuai-oryx.github.io/LoopedWSP/#maze-hero"><img src="assets/maze_hero.gif" width="520" alt="Figure 2 of the blog. A 30 by 30 maze from Maze-Hard. Blue shading spreads from the goal G one cell per loop until it reaches the start S at loop 111. An orange path then grows from S back to G, and the maze is solved at loop 222."></a>
</p>

This is Figure 2 from the blog, drawn from the transformer's real state after every loop as it solves the first Maze-Hard test maze. In every loop, a wave of distances spreads one cell further from the goal G, shaded light to dark. Once it visits the start cell S, after 111 loops, the path grows from S back to G one cell per loop, until the maze is solved after 222 loops. You can also run the transformer yourself in the [in-browser demo](https://mbzuai-oryx.github.io/LoopedWSP/demo/maze.html).

## Results

<p align="center">
  <img src="assets/results_glance.png" width="640" alt="Bar chart of accuracy on ten tasks. On each task an orange line marks the transformer Claude wrote at 100%. The bars show the strongest trained models and LLMs we found. LDT reaches 99.8% on Maze-Hard, Sotaku v2 98.96% on Sudoku-Extreme and Gemini 4 Carbon 96.2% on GraphWalks. Trained models score 0% on graph search, 53.8% on parity and 3.5% on reasoning chains. On BIG-Bench the best scores are 69.6% for Boolean Expressions, 33.2% for Dyck Languages, 81.2% for Web of Lies and 56.9% for Shuffled Objects.">
</p>

The transformer Claude wrote for each task scores 100% (the orange line). The bars show the strongest trained models and LLMs we found for each task, Claude Opus 5.5 answering in text among them.

<p align="center">
  <img src="assets/maze_training.png" width="680" alt="Line chart of Maze-Hard test mazes solved against training time on a log scale. A star marks the transformer Claude wrote at 100%, ready after 39 minutes for $19 in tokens. Models trained by gradient descent rise more slowly and level off below it, led by EBR at 93.5%, FPRM at 92.6%, Looped Flows at 92.2% and TRM at 91.6%, with HRM at 81.7% and a standard transformer at 45.8%. The same architecture Claude wrote, trained from random weights by gradient descent, stays at 0%.">
</p>

Gradient descent doesn't find this solution. Claude had the maze transformer ready 39 minutes after it received the task, for about $19 in tokens. Every other line is a model trained by gradient descent on one H200 GPU, and the best of them, EBR, reaches 93.5%. Trained from random weights, the same architecture Claude wrote solves 0%.

<p align="center">
  <img src="assets/hanoi_disks.png" width="720" alt="Line chart of Tower of Hanoi accuracy against the number of disks. The transformer Claude wrote stays at 100% from 1 to 20 disks, playing 1,048,575 moves at 20 disks with zero mistakes. Claude 3.7 Sonnet (thinking) and DeepSeek-R1 drop to 0% by 11 disks.">
</p>

The puzzles show the loop at work. Claude 3.7 Sonnet (thinking) and DeepSeek-R1 drop to 0% by 11 disks, while the Tower of Hanoi transformer plays all 1,048,575 moves of the 20-disk puzzle with zero mistakes. Its Checker Jumping sibling finds the fewest possible moves at every size up to 40 per side.

## Run the weights

The `weights/` folder holds ten of the transformers together with `run.py`, one short script that runs any of them. It needs only Python 3 and numpy.

```bash
cd weights
python run.py maze --random 30
python run.py hanoi 10
```

Each command prints the answer and checks it. [`weights/README.md`](weights/README.md) shows how to run all ten.

## Prompts

The [`prompts/`](prompts/) folder holds the first message Claude received in each experiment, word for word. That includes the task descriptions for writing each transformer and the prompts behind Figure 10 of the blog post. [`prompts/README.md`](prompts/README.md) says which file belongs to which result.

## Credits

This work builds on [Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (Takehi, Teoh, Zhang and Khattab, MIT CSAIL, 2026). Maze-Hard and Sudoku-Extreme come from the [HRM paper](https://arxiv.org/abs/2506.21734) (Wang et al.), BIG-Bench Hard from Suzgun et al. and BIG-Bench Extra Hard from Kazemi et al. The Tower of Hanoi and Checker Jumping puzzles follow [The Illusion of Thinking](https://arxiv.org/abs/2506.06941) (Shojaee et al., 2025). The blog post lists all related work.

## Citation

If you use this work, please cite it as follows.

```bibtex
@misc{elsayed2026written,
  title        = {{Looped Weight-Space Programming: LLM-Written Transformers for Long Algorithmic Reasoning}},
  author       = {Elsayed, Abdelrahman and Heakl, Ahmed and Shaker, Abdelrahman and Khan, Fahad and Khan, Salman and {Claude Opus 5.5}},
  year         = {2026},
  month        = nov,
  howpublished = {\url{https://mbzuai-oryx.github.io/LoopedWSP/}},
  note         = {Blog post}
}
```

## License

Everything in this repository and on the blog, including the code, weights, text, figures and animations, is released under the [MIT license](LICENSE).
