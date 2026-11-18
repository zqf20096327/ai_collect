<p align="center">
  <img alt="Solarian, open source robotics framework" src="./media/readme/solarian-ultraviolet-black-text-white.svg" width="100%">
</p>

<div align="center">

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/solarian-dev/solarian/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange)](https://pypi.org/project/solarian/)
[![PyPI](https://img.shields.io/pypi/v/solarian)](https://pypi.org/project/solarian/)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/S7rfmJfpm5)

</div>

**Open-source Python framework to build, simulate, train and deploy AI robots, with open hardware that runs UMI policies on any arm.**

<p align="center">
  <img src="media/readme/solarian-point-dont-prompt.gif" alt="Click an object and the robot picks it; click a spot and it places it there" width="800">
</p>

<p align="center"><i>Point, don't prompt: click an object (SAM 2) and a spot (TAPNext), and two UMI policies pick and place it. No teleoperation.</i></p>

<p align="center">
  <a href="https://solarian.dev">Website</a> ·
  <a href="https://solarian.dev/docs">Docs</a> ·
  <a href="https://youtu.be/mJ5frL_mHjM">Video</a> ·
  <a href="https://www.raulgarreta.com/posts/why-i-built-an-open-source-robotics-dev-framework">Why I built it</a>
</p>

**Solarian** is an open-source robotics framework designed to build, simulate, teleoperate, train, and deploy robots. From hardware to AI control in one Python stack.

Solarian brings the developer experience of a modern Python library to robotics, and it is built around low level control using learned policies: ACT, diffusion policies, rather than hand-programmed logic alone. Plus high level control using an agentic harness around VLMs. At the structural level, a robot is a Python class made of modules (reusable components such as arms, grippers, cameras, etc), each module a class made of sensors and actuators. The same project runs in simulation and on hardware, and recording, training, and serving a policy all happen inside the framework.

The goal is to have modularized robots, that can be reused, not only their structure, but their skills. Solarian adopts [UMI](https://umi-gripper.github.io/) as its main path to learning manipulation: demonstrations come from a handheld gripper, and policies describe the gripper's motion rather than one arm's joints, so a trained skill can run on another compatible arm without new data. Open hardware and models live alongside the code, as building blocks for people and AI agents alike. Read more in [Why I created Solarian](https://www.raulgarreta.com/posts/why-i-built-an-open-source-robotics-dev-framework).

## Features

- **[Real-time modules](https://solarian.dev/docs/modules).** A robot is built from modules such as an arm, a gripper, or a camera. Each runs in its own process at its own rate, so a 500 Hz arm never waits on a 30 Hz camera.
- **[Kinematics built in](https://solarian.dev/docs/ik).** Command the end effector, and the module solves inverse kinematics every tick. Command the joints, and the module solves forward kinematics too.
- **[AI Agentic Controller](https://solarian.dev/docs/agentic_controller).** Agentic control for any robot: a harness around any vision-language model (Anthropic, OpenAI, or any OpenAI-compatible server) takes a high-level task from chat, plans it, and carries it out by calling your physical skills as tools, while a fast monitor model watches each one through the cameras.
- **[Simulation built in](https://solarian.dev/docs/simulation).** `solarian run-robot --sim` runs the same robot class and YAML in MuJoCo instead of on hardware.
- **[Plugins](https://solarian.dev/plugins).** Solarian is extensible by design: actuators and sensors (servos, cameras, etc), modules (arms, grippers, etc), skills (low level learned policies and heuristics) install as plugins, config included. `solarian create-plugin` starts your own.
- **[Recording](https://solarian.dev/docs/recording), [datasets](https://solarian.dev/docs/datasets), and [training](https://solarian.dev/docs/training).** Record every camera and signal at its native rate, curate episodes, train diffusion, ACT, or UMI policies, and serve them back to the robot.
- **[Typed observations and actions](https://solarian.dev/docs/observations) and [Hydra configuration](https://solarian.dev/docs/project-configs).** Pydantic schemas bound to your modules, and composable YAML you can override from the command line.

## Getting started

```bash
pip install solarian
pip install "solarian[all]"   # optional: AI, agentic controller, and simulation extras
```

Visit our [Documentation](https://solarian.dev/docs/overview) to get started with Solarian.

Visit the [Tutorials](https://solarian.dev/docs/tutorials) to learn Solarian by building a demo robot arm project.

## A quick look

This is a trimmed version of `arm1`, a [Solarian Arm 1](https://solarian.dev/hardware) with a UMI-style gripper and a wrist camera. A robot is a class whose attributes are its modules. The `scene` is what `--sim` uses to build the MuJoCo world.

```python
from solarian.core import Robot
from solarian.sim import CameraMount, ModuleAttachment, SceneConfig
from solarian_arm1 import ARM_MJCF_PATH
from solarian_arm1.arm import Arm1Module
from solarian_picamera import PiCameraModule
from solarian_gripper1 import MJCF_FEETECH_PATH as GRIPPER_MJCF
from solarian_gripper1.gripper_feetech import Gripper1FeetechModule


class Arm1Robot(Robot):
    right_arm = Arm1Module(ik_tcp=Gripper1FeetechModule.tcp_from_flange)
    right_gripper = Gripper1FeetechModule()
    right_wrist_camera = PiCameraModule()

    scene = SceneConfig(
        world_mjcf="assets/sim_scene.xml",
        attachments=[
            ModuleAttachment(module="right_arm", mjcf=ARM_MJCF_PATH, parent_body="world", prefix="right/"),
            ModuleAttachment(
                module="right_gripper",
                mjcf=GRIPPER_MJCF,
                parent_site="right/flange",
                child_site="flange",
                prefix="right_gripper/",
            ),
        ],
        # A MuJoCo camera looks down -Z; the exported camera frame's +Z points away from the gripper.
        cameras=[CameraMount(name="right_wrist_cam", site="right_gripper/camera", quat=[0.0, 1.0, 0.0, 0.0], fovy=160.0)],
    )
```

The controller decides what the robot does. Here it teleoperates the arm from the keyboard, names its tools (a skill plus the params it binds), binds keys to them, and marks the ones the agentic controller may call:

```python
from solarian.core import Controller
from solarian.core.event import Event, EventType, event_handler
from solarian.core.skill import Tool
from solarian_move import MoveSkill
from solarian_umi import UMISkill
from solarian_gripper1.aperture import APERTURE_CLOSED_MM, APERTURE_OPEN_MM

from arm1.skills import CartesianTeleopSkill

ARM = {"arm": "right_arm", "gripper": "right_gripper"}
TELEOP = {**ARM, "frame": "ee", "gripper_min_mm": APERTURE_CLOSED_MM, "gripper_max_mm": APERTURE_OPEN_MM}


class Arm1Controller(Controller):
    tools = {
        "teleop": Tool(CartesianTeleopSkill, TELEOP),
        "home": Tool(MoveSkill, {**ARM, "pose": "home"}),
        "move_to_pose": Tool(MoveSkill, ARM, agent_enabled=True),
        "pick_object": Tool(UMISkill, {"config": "pick_object.yaml"}, agent_enabled=True),
    }

    def on_start(self):
        self.start_tool("teleop")

    @event_handler(EventType.KEY_DOWN)
    def start_bound_skill(self, event: Event) -> None:
        match event.data.get("key"):
            case "0":
                self.start_tool("home")
            case "4":
                self.start_tool("pick_object")
```

Run the relay server, the robot, and the controller from the project directory. Each can run on a different machine; `--deployment` picks the profile in `conf/deployment/` that says where.

```bash
solarian run-server
solarian run-robot --sim     # drop --sim to drive the real arm
solarian run-controller
```

The simulated arm going to its ground pose, jogged from the keyboard, then back home:

<p align="center">
  <img alt="Solarian Arm 1 in MuJoCo" src="https://raw.githubusercontent.com/solarian-dev/solarian/main/media/readme/sim.webp" width="720">
</p>

The controller window shows the live observations, the wrist camera, and the agentic controller's chat:

<p align="center">
  <img alt="Solarian controller GUI" src="https://raw.githubusercontent.com/solarian-dev/solarian/main/media/readme/controller-gui.png" width="720">
</p>

<!-- The real Solarian Arm 1, seen from outside. Record media/readme/arm1-real.webp, then uncomment:
<p align="center">
  <img alt="Solarian Arm 1 on the real robot" src="https://raw.githubusercontent.com/solarian-dev/solarian/main/media/readme/arm1-real.webp" width="720">
</p>
-->

## Community

To chat with other community members, you can join the [Solarian Discord server](https://discord.gg/S7rfmJfpm5).

## Contributing

Solarian is early, and contributions are welcome. A few guidelines to start with:

- For anything larger than a small fix, open an issue or ask on [Discord](https://discord.gg/S7rfmJfpm5) before writing the code, so we can agree on the approach.
- To work on Solarian itself, install it from source and run the tests:

  ```bash
  git clone https://github.com/solarian-dev/solarian.git
  cd solarian
  pip install -e ".[all]"
  pytest tests/
  ```

  On Apple Silicon that install builds `atomics` from source, and `xformers` with the `ai` extra (`.[all]` includes it). It needs git and a C compiler.
- New hardware support and skills usually belong in a plugin rather than in the core. Start one with `solarian create-plugin`, and list it in the [Plugin Directory](https://solarian.dev/plugins/submit).

A `CONTRIBUTING.md` and a code of conduct are coming.

## License

Solarian is licensed under the [Apache License 2.0](https://github.com/solarian-dev/solarian/blob/main/LICENSE). Copyright 2026 PrimaryKey Inc. Vendored third-party code keeps its own license; see [NOTICE](https://github.com/solarian-dev/solarian/blob/main/NOTICE). Model weights are downloaded separately and keep their upstream licenses.

Solarian and the Solarian logo are trademarks of PrimaryKey Inc. See the [trademark policy](https://github.com/solarian-dev/solarian/blob/main/TRADEMARKS.md).
