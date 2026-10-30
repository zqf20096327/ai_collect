# nishanth_embodied_agent

**Natural-language → vision-grounded pick and place on a UR3e in simulation, driven by Claude.**

This package turns the UR3e + Robotiq 2F-140 + RealSense D435i setup from my
master's thesis into an LLM-controlled embodied agent. You type an instruction
in plain English; a Claude vision model grounds the objects it sees in the
RealSense view; a Claude planner breaks the instruction into pick / place /
move-to steps; MoveIt 2 plans and Gazebo executes.

```
user text ──▶ LLM planner (Claude, tool use)
                 │
                 ├─ describe_scene ──▶ Claude VLM on RGB frame
                 │                     ▶ back-project (depth, K) ▶ base_link
                 │
                 ├─ pick / place ──▶ MoveIt 2 (MoveGroup action)
                 │                   ▶ Robotiq 2F-140 (Float64MultiArray)
                 │
                 └─ check_safety  ──▶ F/T wrench + proximity
```

## Why this exists

The thesis hybrid controller already makes UR3e motion *safe* around humans.
This repo adds the layer above it: turning a single instruction ("put the red
block next to the blue cup") into a grounded, executable plan without a
hand-written state machine.

## Features

- **Tool-use loop over Anthropic's Messages API** — 8 tools:
  `describe_scene`, `move_to`, `pick`, `place`, `open_gripper`,
  `close_gripper`, `check_safety`, `home`.
- **Vision grounding**: Claude Sonnet VLM returns a JSON list of objects with
  (u, v) pixel centres; depth + camera intrinsics back-project to 3D; TF2
  transforms into the `base_link` planning frame.
- **MoveIt 2 via the MoveGroup action** (no moveit_py needed on Humble) with
  position + orientation constraints for pose goals and joint constraints
  for the home pose.
- **Gripper** via the Robotiq 2F-140 mirrored `Float64MultiArray`
  `[v, -v, v, -v, -v, v]` command.
- **Safety gate** wrapping the thesis's F/T and proximity topics, read-only.
- All tools are plain Python callbacks, so the same ROS 2 node can be reused
  for other LLMs or tool-calling frameworks.

## Requirements

- Ubuntu 22.04, ROS 2 Humble
- MoveIt 2 (Humble)
- `ur_description_gz`, `ur3e_moveit_config` (my thesis packages) — the sim
  launch includes the UR3e + Robotiq 2F-140 + RealSense D435i + workspace.
- `anthropic` Python SDK (pulled in via `setup.py`)
- `ANTHROPIC_API_KEY` exported in the environment.

## Install

Put this directory inside your colcon workspace:

```
ros2_ws/src/nishanth_embodied_agent/
```

Then from the workspace root:

```bash
cd ~/ros2_ws
pip install anthropic opencv-python                # SDK deps
rosdep install --from-paths src -i -y --rosdistro humble
colcon build --packages-select nishanth_embodied_agent --symlink-install
source install/setup.bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Run

Launch sim + agent together (one terminal):

```bash
ros2 launch nishanth_embodied_agent embodied_agent.launch.py
```

In a second terminal, send a command:

```bash
ros2 run nishanth_embodied_agent agent_cli "put the red block next to the blue cup"
```

Watch the transcript stream back:

```
[cli] sent: put the red block next to the blue cup
[tool] describe_scene({})
[result] describe_scene -> {'success': True, 'count': 2, ...}

[assistant] I see a red block at (x=-0.42, y=0.05) and a blue cup at (x=-0.38, y=-0.10). Picking up the block first.
[tool] pick({'x': -0.42, 'y': 0.05, 'z': 0.13, 'label': 'red_block'})
[result] pick -> {'success': True, 'action': 'pick', ...}
[tool] place({'x': -0.36, 'y': -0.10, 'z': 0.13})
[result] place -> {'success': True, 'action': 'place', ...}

=== FINAL ===
Done — moved the red block next to the blue cup.
```

You can also publish raw commands if you prefer:

```bash
ros2 topic pub --once /agent/command std_msgs/String "{data: 'put everything on the right side'}"
ros2 topic echo /agent/transcript
```

## Topics

| Topic                  | Type                | Role                                    |
|-----------------------|---------------------|-----------------------------------------|
| `/agent/command`       | `std_msgs/String`   | **Input** — natural-language instruction |
| `/agent/transcript`    | `std_msgs/String`   | **Output** — JSON events (text / tool_use / tool_result / final / error) |
| `/realsense/image`     | `sensor_msgs/Image` | RGB feed from Gazebo RealSense          |
| `/realsense/depth_image` | `sensor_msgs/Image` | Depth feed (MONO16, mm)                |
| `/realsense/camera_info` | `sensor_msgs/CameraInfo` | Intrinsics                         |
| `/robotiq_group_position_controller/commands` | `std_msgs/Float64MultiArray` | Gripper (mirrored 6-element) |

## Configuration

Edit `config/agent.yaml` to tune model, topics, or motion defaults:

```yaml
agent:
  ros__parameters:
    llm_model: "claude-sonnet-4-6"
    velocity_scaling: 0.3
    pick_approach_height_m: 0.08
    ...
```

## Layout

```
nishanth_embodied_agent/
├── config/agent.yaml
├── launch/embodied_agent.launch.py
├── nishanth_embodied_agent/
│   ├── agent_node.py               # main ROS 2 node
│   ├── agent_cli.py                # CLI publisher
│   ├── planner/
│   │   ├── llm_client.py           # Claude tool-use loop
│   │   ├── system_prompt.py
│   │   └── tool_schemas.py         # 8 tool schemas
│   ├── tools/
│   │   ├── describe_scene.py       # VLM + back-projection
│   │   ├── motion.py               # MoveGroup action client
│   │   ├── gripper.py              # Robotiq 2F-140 publisher
│   │   ├── pick_place.py           # compound primitives
│   │   └── safety.py               # F/T + proximity read-only gate
│   └── vision/
│       └── backproject.py          # pixel → 3D + TF helpers
├── package.xml
├── setup.py
└── README.md
```

## Design notes

- **Why the MoveGroup action and not `moveit_py`?** On ROS 2 Humble the
  Python bindings are still incomplete; the action API is stable, already
  exercised by the thesis code, and trivially wrapped.
- **Why a tool-use loop over a single prompt?** Grounding (`describe_scene`)
  and execution (`pick`) both need to be verifiable by the planner — the LLM
  gets real tool results, not hallucinated ones, and can re-plan if a step
  fails.
- **Why the base64 JPEG path?** D435i RGB at 640×480 encodes to ~50 KB JPEG,
  well below Anthropic's per-message image cap and under 300 ms network trip.
- **Where the thesis safety layer fits.** This node never replaces the
  hybrid admittance / proximity controller — it only *queries* their state
  so the LLM can refuse unsafe motions before it even dispatches them.

## Roadmap

- Grounded grasp planning (GraspNet or geometric heuristics instead of
  "grab the centre pixel").
- Speech input (Whisper) and speech output.
- Multi-step memory across commands (scratchpad file).
- Real-hardware launch on the lab UR3e (drop `with_sim:=false`, swap the
  controller topic for the hardware one).

## Author

Nishanth Sundaran — M.Eng AI thesis on HRI with force feedback on UR3e.
