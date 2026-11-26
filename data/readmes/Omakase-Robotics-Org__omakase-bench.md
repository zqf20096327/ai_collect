# omakase-bench

[日本語](README.ja.md)

Name a model, run robot tasks in simulation, get a scored report.

```sh
omakase-bench run --model anthropic/<model> --interface tools --suite core@1
```

runs every task of the frozen `core@1` suite on its 20 seeds in MuJoCo, lets the model drive the robot
through a robot API, scores every episode from the simulator's ground truth (never from what the model
says), and writes `results.json`, `report.html` and a video per episode.

It is a framework as much as a benchmark: bring a URDF and you have a robot; add a package and you have a
task.

## Quick start

```sh
git clone https://github.com/Omakase-Robotics-Org/omakase-bench && cd omakase-bench
uv sync                         # add --extra anthropic / --extra openai for the model clients
uv run omakase-bench doctor     # rendering, video, sandbox, keys and client libraries
```

Requires Python 3.11 or newer. Rendering uses `MUJOCO_GL=egl` by default; without an EGL driver install
`libOSMesa` and `PyOpenGL` and set `MUJOCO_GL=osmesa`.

Run the simple task, pick a cube and put it into a tray:

```sh
# the scripted reference solution: no model, no key
uv run omakase-bench run --task core/cube_to_tray --model scripted/oracle --seeds 0-2

# a stand-in model through the same interface a real model uses: still no key (the cost shown is nominal)
uv run omakase-bench run --task core/cube_to_tray --model mock/place --interface tools

# a model: needs its client library (uv sync --extra anthropic) and a key (ANTHROPIC_API_KEY / OPENAI_API_KEY, or --env-file)
uv run omakase-bench run --task core/cube_to_tray --model anthropic/<model> --interface tools --seeds 0-2 --max-usd 2

# the same task on another robot
uv run omakase-bench run --task core/cube_to_tray --model scripted/oracle --robot arm6
```

Each run writes `runs/<time>_<task or suite>_<backend>/` with `results.json` and `report.html`, and per
episode `episodes/<subject>/<task>/<seed>/` with `trace.jsonl`, `result.json` and `episode.mp4`. `omakase-bench list` shows the suites, tasks, robots and backends.

## Concepts

| | |
| --- | --- |
| **Robot** | A URDF plus `robot.yaml` (arms, grippers, cameras, base, named poses, limits). `robots/d1` is a two-arm mobile manipulator; `robots/arm6` is a six-joint arm made of boxes. Nothing else in the code names a robot's joints. |
| **Task** | A package `tasks/<family>/<task>/`: a YAML definition (scene, what varies per seed, instruction, success check, budget) and a reference solution. Success is read from simulator ground truth. |
| **Suite** | A named, versioned list of tasks and seeds, frozen with a hash so results stay comparable: `core@1`, `manip@1`, `grip@1`, `team@1`, `games@1`. |
| **Interface** | How a subject acts. `tools`: one robot API call per model turn. `code`: a program against the same API, run in a sandbox. `ee`: fingertip targets step by step from camera images. `chunks`: joint action chunks for VLA policies. `scripted`: the reference solutions. |
| **Backend** | What executes the commands: MuJoCo (default, CPU), Isaac Sim, or a real robot. Simulators add reset and ground truth; a task says what it needs. |
| **Harness** | Everything between the model and the robot: the turn loop, the one robot API all commands pass through, safety checks, IK, observations. |

## Robot models

The robot descriptions live in [`src/omakase_bench/robots/`](src/omakase_bench/robots/), one folder per robot.

| Robot | URDF | Meshes | Bench config |
| --- | --- | --- | --- |
| D1 (two arms, lift, head, mobile base) | [`d1/d1.meshes.urdf`](src/omakase_bench/robots/d1/d1.meshes.urdf) (mesh visuals), [`d1/d1.urdf`](src/omakase_bench/robots/d1/d1.urdf) (primitive shapes only) | [`d1/meshes/`](src/omakase_bench/robots/d1/meshes/) | [`d1/robot.yaml`](src/omakase_bench/robots/d1/robot.yaml) |
| arm6 (six-joint test arm) | [`arm6/arm6.urdf`](src/omakase_bench/robots/arm6/arm6.urdf) | none (boxes) | [`arm6/robot.yaml`](src/omakase_bench/robots/arm6/robot.yaml) |

Both URDFs of the D1 have the same kinematics and collision geometry; they differ only in the visuals.
The D1's daemon API subset and camera interface description are in [`d1/api/`](src/omakase_bench/robots/d1/api/).

## Documentation

- [docs/architecture.md](docs/architecture.md): the layout and the interfaces it rests on
- [docs/new_robot.md](docs/new_robot.md): add a robot from a URDF
- [docs/new_task.md](docs/new_task.md): add a task
- [docs/real_robot.md](docs/real_robot.md): run on the real robot (the safety gates, what differs from simulation)
- [docs/reference.md](docs/reference.md): commands, models, the robot API, the `ee` interface, multi-robot tasks, backends
- [docs/decisions.md](docs/decisions.md): why things are the way they are
- [docs/results/](docs/results/README.md): recorded results

## Showcase: chess between two robots

`games/chess` puts two robots at one board, one model per robot. Each names its move to a referee, moves
the pieces with its own arms from camera images, and is checked piece by piece; the clocks run while a
model thinks and while its robot moves.

Claude Opus 5.5 (White) against gpt-6.2-astra (Black), played to the end in MuJoCo: Black won by
checkmate in 28 moves (`28. gxf3 Rxh3#`), no illegal move by either side, 5 manipulation faults by White and 2 by Black.
The game, its analysis and the per-model figures are in [docs/results](docs/results/README.md).

![Chess between two robots: the last three moves of the game](docs/media/chess_highlight.gif)

*The end of the game: Black offers the queen (`27... Qf3`), White takes it (`28. gxf3`), Black mates (`28... Rxh3#`).*

```sh
uv run omakase-bench run --task games/chess --seeds 0 --no-video      # scripted players, the Opera Game; a few minutes on a CPU, prints when done
```

## Licence

Apache License 2.0 (`LICENSE`, `NOTICE`). Every mesh file is listed in `assets.yaml` with its hash, source
and licence. The source of the D1 daemon's OpenAPI subset is described in
`src/omakase_bench/robots/d1/api/PROVENANCE.md`.
