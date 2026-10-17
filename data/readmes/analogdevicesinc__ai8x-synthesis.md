# ADI MAX78000/MAX78002 Model Training and Synthesis

November 7, 2024

**Note: This branch requires PyTorch 2. Please see the archive-1.8 branch for PyTorch 1.8 support. [KNOWN_ISSUES](KNOWN_ISSUES.txt) contains a list of known issues.**

ADI’s MAX78000/MAX78002 project is comprised of five repositories:

1. **Start here**:
    **[Top Level Documentation](https://github.com/analogdevicesinc/MaximAI_Documentation)**
2. The software development kit (MSDK), which contains drivers and example programs ready to run on the evaluation kits (EVkit and Feather):
    [Analog Devices MSDK](https://github.com/analogdevicesinc/msdk)
3. The training repository, which is used for deep learning *model development and training*:
    [ai8x-training](https://github.com/analogdevicesinc/ai8x-training/tree/develop) **(described in this document)**
4. The synthesis repository, which is used to *convert a trained model into C code* using the “izer” tool:
    [ai8x-synthesis](https://github.com/analogdevicesinc/ai8x-synthesis/tree/develop) **(described in this document)**
5. The reference design repository, which contains host applications and sample applications for reference designs such as [MAXREFDES178 (Cube Camera)](https://www.analog.com/en/design-center/reference-designs/maxrefdes178.html):
    [refdes](https://github.com/analogdevicesinc/MAX78xxx-RefDes)
    *Note: Examples for EVkits and Feather boards are part of the MSDK*

_Open the `.md` version of this file in a markdown enabled viewer, for example Typora (<http://typora.io>).
See <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet> for a description of Markdown. A [PDF copy of this file](README.pdf) is available in this repository. The GitHub rendering of this document does not show the mathematical formulas. Use the ≡ button to access the table of contents on GitHub._

---

[TOC]

## Part Numbers

This document covers several of ADI’s ultra-low power machine learning accelerator systems. They are sometimes referred to by their die types. The following shows the die types and their corresponding part numbers:

| Die Type | Part Number(s)                 |
| -------- | ------------------------------ |
| *AI84*   | *Unreleased test chip*         |
| AI85     | **MAX78000** (full production) |
| AI87     | **MAX78002** (full production) |

## Overview

The following graphic shows an overview of the development flow:

![Development Flow](docs/DevelopmentFlow.png)

## Installation

### File System Layout

Including the MSDK, the expected/resulting file system layout will be:

    ..../ai8x-training/
    ..../ai8x-synthesis/
    ..../ai8x-synthesis/sdk/ [or a different path selected by the user]

where “....” is the project root, for example `~/Documents/Source/AI`.

### Prerequisites

This software requires PyTorch. *TensorFlow / Keras support is deprecated.*

PyTorch operating system and hardware support are constantly evolving. This document does not cover all possible combinations of operating system and hardware. Instead, this document describes how to install PyTorch on one officially supported platform.

#### Platform Recommendation and Full Support

Full support and documentation are provided for the following platform:

* CPU: 64-bit amd64/x86_64 “PC” with [Ubuntu Linux 20.04 LTS or 22.04 LTS](https://ubuntu.com/download/server)
* GPU for hardware acceleration (optional but highly recommended): Nvidia with [CUDA 12.1](https://developer.nvidia.com/cuda-toolkit-archive) or later
* [PyTorch 2.3](https://pytorch.org/get-started/locally/) on Python 3.11.x

Limited support and advice for using other hardware and software combinations is available as follows.

#### Operating System Support

##### Linux

**The only officially supported platforms for model training** are Ubuntu Linux 20.04 LTS and 22.04 LTS on amd64/x86_64, either the desktop or the [server version](https://ubuntu.com/download/server).

*Note that hardware acceleration using CUDA is <u>not available</u> in PyTorch for Raspberry Pi 4 and other <u>aarch64/arm64</u> devices, even those running Ubuntu Linux 20.04/22.04. See also [Development on Raspberry Pi 4 and 400](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/RaspberryPi.md) (unsupported).*

This document also provides instructions for installing on RedHat Enterprise Linux / CentOS 8 with limited support.

##### Windows

On Windows 10 version 21H2 or newer, and Windows 11, after installing the Windows Subsystem for Linux (WSL2), Ubuntu Linux 20.04 or 22.04 can be used inside Windows with full CUDA acceleration, please see *[Windows Subsystem for Linux](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/WSL2.md).* For the remainder of this document, follow the steps for Ubuntu Linux.

If WSL2 is not available, it is also possible (but not recommended due to inherent compatibility issues and slightly degraded performance) to run this software natively on Windows. Please see *[Native Windows Installation](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/Windows.md)*.

##### macOS

The software works on macOS and uses MPS acceleration on Apple Silicon. On Intel CPUs, model training suffers from the lack of hardware acceleration.

##### Virtual Machines (Unsupported)

This software works inside a virtual machine running Ubuntu Linux 20.04 or 22.04. However, GPU passthrough is potentially difficult to set up and <u>not always available</u> for Linux VMs, so there may be no CUDA hardware acceleration. Certain Nvidia cards support [vGPU software](https://www.nvidia.com/en-us/data-center/graphics-cards-for-virtualization/); see also [vGPUs and CUDA](https://docs.nvidia.com/cuda/vGPU/), but vGPU features may come at substantial additional cost and vGPU software is not covered by this document.

##### Docker Containers (Unsupported)

This software also works inside Docker containers. However, CUDA support inside containers requires Nvidia Docker ([see blog entry](https://developer.nvidia.com/blog/nvidia-docker-gpu-server-application-deployment-made-easy/)) and is not covered by this document.

#### PyTorch and Python

The officially supported version of [PyTorch is 2.3](https://pytorch.org/get-started/locally/) running on Python 3.11.x. Newer versions will typically work, but are not covered by support, documentation, and installation scripts.

#### Hardware Acceleration

When going beyond simple models, model training does not work well without hardware acceleration – Nvidia CUDA, AMD ROCm, or Apple Silicon MPS. The network loader (“izer”) does <u>not</u> require hardware acceleration, and very simple models can also be trained on systems without hardware acceleration.

* CUDA requires modern Nvidia GPUs. This is the most compatible, and best supported hardware accelerator.
* ROCm requires certain AMD GPUs, see [blog entry](https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/).
* MPS requires Apple Silicon (M1 or newer) and macOS 12.3 or newer.
* PyTorch does not include CUDA support for aarch64/arm64 systems. *Rebuilding PyTorch from source is not covered by this document.*


##### Using Multiple GPUs

When using multiple GPUs (graphics cards), the software will automatically use all available GPUs and distribute the workload. To prevent this (for example, when the GPUs are not balanced), set the `CUDA_VISIBLE_DEVICES` environment variable. Use the `--gpus` command line argument to set the default GPU.

#### Shared (Multi-User) and Remote Systems

On a shared (multi-user) system that has previously been set up, only local installation is needed. CUDA and any `apt-get` or `brew` tasks are not necessary, with the exception of the CUDA [Environment Setup](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#environment-setup).

The `screen` command (or alternatively, the more powerful `tmux`) can be used inside a remote terminal to disconnect a session from the controlling terminal, so that a long running training session doesn’t abort due to network issues, or local power saving. In addition, screen can log all console output to a text file.

Example:

```shell
$ ssh targethost
targethost$ screen -L # or screen -r to resume, screen -list to list
targethost$
Ctrl+A,D to disconnect
```

`man screen` and `man tmux` describe the software in more detail.

#### Additional Software

The following software is optional, and can be replaced with other similar software of the user’s choosing.

1. Code Editor
   Visual Studio Code, <https://code.visualstudio.com> or the VSCodium version, <https://vscodium.com>, with the “Remote - SSH” plugin; *to use Visual Studio Code on Windows as a full development environment (including debug), see <https://github.com/analogdevicesinc/VSCode-Maxim>*
   Sublime Text, <https://www.sublimetext.com>
2. Markdown Editor
   Typora, <http://typora.io>
3. Serial Terminal
   CoolTerm, <http://freeware.the-meiers.org>
   Serial, <https://apps.apple.com/us/app/serial/id877615577?mt=12>
   Putty, <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>
   Tera Term, <https://osdn.net/projects/ttssh2/releases/>
4. Graphical Git Client
   GitHub Desktop, <https://desktop.github.com>
   Git Fork, <https://git-fork.com>
5. Diff and Merge Tool
   Beyond Compare, <https://scootersoftware.com>

### Project Installation

#### Free Disk Space

A minimum of 64 GB of free disk space is recommended, and datasets can be many times this size and should be stored separately. Check the available space on the target file system before continuing using

```shell
$ df -kh
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/sda2       457G  176G  259G  41% /
```

#### System Packages

Some additional system packages are required, and installation of these additional packages requires administrator privileges. Note that this is the only time administrator privileges are required.

##### macOS

On macOS use:

```shell
$ brew install libomp libsndfile tcl-tk sox
```

##### Linux (Ubuntu), including WSL2)

```shell
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
  libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
  libsndfile-dev portaudio19-dev libsox-dev
```

###### RedHat Enterprise Linux / CentOS 8

While Ubuntu 20.04 LTS and 22.04 LTS are the supported distributions, the MAX78000/MAX78002 software packages run fine on all modern Linux distributions that also support CUDA. The *apt-get install* commands above must be replaced with distribution specific commands and package names. Unfortunately, there is no obvious 1:1 mapping between package names from one distribution to the next. The following example shows the commands needed for RHEL/CentOS 8.

*Two of the required packages are not in the base repositories. Enable the EPEL and PowerTools repositories:*

```shell
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
$ sudo dnf config-manager --set-enabled powertools
```

*Proceed to install the required packages:*

```shell
$ sudo dnf group install "Development Tools"
$ sudo dnf install openssl-devel zlib-devel \
  bzip2-devel readline-devel sqlite-devel wget llvm \
  xz-devel tk tk-devel libffi-devel \
  libsndfile libsndfile-devel portaudio-devel
```

#### Python 3.11

*The software in this project uses Python 3.11.8 or a later 3.11.x version.*

First, check whether there is a default Python interpreter and whether it is version 3.11.x:

```shell
$ python --version
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
# no default python, install pyenv

$ python --version
Python 2.7.18
# wrong version, pyenv required
```

Python 2 **will not function correctly** with the MAX78000/MAX78002 tools. If the result is Python **3.11**.x, skip ahead to [git Environment](#git-environment). For *any* other version (for example, 2.7, 3.7, 3.8, 3.9, 3.10), or no version, continue here.

*Note: For the purposes of the MAX78000/MAX78002 tools, “python3” is not a substitute for “python”. Please install pyenv when `python --version` does not return version 3.11.x, <u>even if</u> “python3” is available.*

*Note for advanced users: `sudo apt-get install python-is-python3` on Ubuntu 20.04 will install Python 3 as the default Python version; however, it may not be version 3.11.x.*

##### pyenv

It is not necessary to install Python 3.11 system-wide, or to rely on the system-provided Python. To manage Python versions, instead use `pyenv` (<https://github.com/pyenv/pyenv>). This allows multiple Python versions to co-exist on the same system without interfering with the system or with one another.

On macOS:

```shell
$ brew install pyenv pyenv-virtualenv
```

On Linux:

```shell
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash  # NOTE: Verify contents of the script before running it!!
```

Then, follow the terminal output of the pyenv-installer and add pyenv to your shell by modifying one or more of `~/.bash_profile`, `~/.bashrc`, `~/.zshrc`, `~/.profile`, or `~/.zprofile`. The instructions differ depending on the shell (bash or zsh).

For example, on *Ubuntu 20.04 inside WSL2* add the following to `~/.bashrc`:

```shell
# WSL2
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

To display the instructions again at any later time:

```shell
$ ~/.pyenv/bin/pyenv init

# (The below instructions are intended for common
# shell setups. See the README for more guidance
# if they don't apply and/or don't work for you.)

# Add pyenv executable to PATH and
# enable shims by adding the following
# to ~/.profile and ~/.zprofile:
...
...
```

*Note: Installing both conda and pyenv in parallel may cause issues. Ensure that the pyenv initialization tasks are executed <u>before</u> any conda related tasks.*

Next, close the Terminal, open a new Terminal and install Python 3.11.8.

On macOS:

```shell
$ env \
  PATH="$(brew --prefix tcl-tk)/bin:$PATH" \
  LDFLAGS="-L$(brew --prefix tcl-tk)/lib" \
  CPPFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig" \
  CFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'" \
  pyenv install 3.11.8
```

On Linux, including WSL2:

```shell
$ pyenv install 3.11.8
```

#### git Environment

If the local git environment has not been previously configured, add the following commands to configure e-mail and name. The e-mail must match GitHub (including upper/lower case):

```shell
$ git config --global user.email "first.last@example.com"
$ git config --global user.name "First Last"
```

#### Nervana Distiller

[Nervana Distiller](https://github.com/analogdevicesinc/distiller) is automatically installed as a git sub-module with the other packages. Distiller is used for its scheduling and model export functionality.

### Upstream Code

Change to the project root and run the following commands. Use your GitHub credentials if prompted.

```shell
$ cd <your/project>
$ git clone --recursive https://github.com/analogdevicesinc/ai8x-training.git
$ git clone --recursive https://github.com/analogdevicesinc/ai8x-synthesis.git
```

#### Creating the Virtual Environment

To create the virtual environment and install basic wheels:

```shell
$ cd ai8x-training
```

Using the instructions above checks out the `develop` branch which supports PyTorch 2.3. The `main` branch is updated less frequently, but possibly more stable. To change branches, use the command `git checkout`, for example `git checkout main`.
For PyTorch 1.8 support, use the archive.

If using pyenv, set the local directory to use Python 3.11.8.

```shell
$ pyenv local 3.11.8
```

In all cases, verify that a 3.11.x version of Python is used:

```shell
$ python --version
Python 3.11.8
```

If this does <u>*not*</u> return version 3.11.x, please install and initialize [pyenv](#python-311).

Then continue with the following:

```shell
$ python -m venv .venv --prompt ai8x-training
$ echo "*" > .venv/.gitignore
```

If this command returns an error message similar to *“The virtual environment was not created successfully because ensurepip is not available,”* please install and initialize [pyenv](#python-311).

On macOS and Linux, including WSL2, activate the environment using

```shell
$ source .venv/bin/activate
```

On native Windows, instead use:

```shell
$ source .venv/Scripts/activate
```

Then continue with

```shell
(ai8x-training) $ pip3 install -U pip wheel setuptools
```

The next step differs depending on whether the system uses CUDA 12.1+, or not.

For CUDA 12:

```shell
(ai8x-training) $ pip3 install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu121
```

For ROCm 5.7:

```shell
(ai8x-training) $ pip3 install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/rocm5.7
```

For all other systems, including macOS:

```shell
(ai8x-training) $ pip3 install -r requirements.txt
```

##### Repository Branches

Using the instructions above checks out the `develop` branch which supports PyTorch 2.3. The `main` branch is updated less frequently, but possibly more stable. To change branches, use the command `git checkout`, for example `git checkout main`.
For PyTorch 1.8 support, use the archive.

###### TensorFlow / Keras

Support for TensorFlow / Keras is deprecated.

#### Updating to the Latest Version

After additional testing, `develop` is merged into the main branch at regular intervals.

After a small delay of typically a day, a “Release” tag is created on GitHub for all non-trivial merges into the main branch. GitHub offers email alerts for all activity in a project, or for new releases only. Subscribing to releases only substantially reduces email traffic.

*Note: Each “Release” automatically creates a code archive. It is recommended to use a git client to access (pull from) the main branch of the repository using a git client instead of downloading the archives.*

In addition to code updated in the repository itself, **submodules and Python libraries may have been updated as well**.

Major upgrades (such as updating from PyTorch 1.8 to PyTorch 2.3) are best done by removing all installed wheels. This can be achieved most easily by creating a new folder and starting from scratch at [Upstream Code](#upstream-code). Starting from scratch is also recommended when upgrading the Python version.

For minor updates, pull the latest code and install the updated wheels:

```shell
(ai8x-training) $ git pull
(ai8x-training) $ git submodule update --init
(ai8x-training) $ pip3 install -U pip setuptools
(ai8x-training) $ pip3 install -U -r requirements.txt  # add --extra-index-url if needed, as shown above
```

##### MSDK Updates

Please *also* update the MSDK or use the Maintenance Tool as documented in the [Analog Devices MSDK documentation](https://github.com/analogdevicesinc/msdk). The Maintenance Tool automatically updates the MSDK.

##### Python Version Updates

Updating Python may require updating `pyenv` first. Should `pyenv install 3.11.8` fail,

```shell
$ pyenv install 3.11.8
python-build: definition not found: 3.11.8
```

then `pyenv` must be updated. On macOS, use:

```shell
$ brew update && brew upgrade pyenv
...
$
```

On Linux (including WSL2), use:

```shell
$ cd $(pyenv root) && git pull && cd -
remote: Enumerating objects: 19021, done.
...
$
```

The update should now succeed:

```shell
$ pyenv install 3.11.8
Downloading Python-3.11.8.tar.xz...
-> https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tar.xz
Installing Python-3.11.8...
...
$ pyenv local 3.11.8
```



#### Synthesis Project

The `ai8x-synthesis` project does not require hardware acceleration.

Start by deactivating the `ai8x-training` environment if it is active.

```shell
(ai8x-training) $ deactivate
```

Then, create a second virtual environment:

```shell
$ cd <your/project>
$ cd ai8x-synthesis
```

If you want to use the main branch, switch to “main” using the optional command `git checkout main`.

If using pyenv, run:

```shell
$ pyenv local 3.11.8
```

In all cases, make sure Python 3.11.x is the active version:

```shell
$ python --version
Python 3.11.8
```

If this does <u>*not*</u> return version 3.11.x, please install and initialize [pyenv](#python-311).

Then continue:

```shell
$ python -m venv .venv --prompt ai8x-synthesis
$ echo "*" > .venv/.gitignore
```

Activate the virtual environment. On macOS and Linux (including WSL2), use

```shell
$ source .venv/bin/activate
```

On native Windows, instead use

```shell
$ source .venv/Scripts/activate
```

For all systems, continue with:

```shell
(ai8x-synthesis) $ pip3 install -U pip setuptools
(ai8x-synthesis) $ pip3 install -r requirements.txt
```

##### Repository Branches and Updates

Branches and updates for `ai8x-synthesis` are handled similarly to the [`ai8x-training`](#repository-branches) project.

#### Installation is now Complete

With the installation of Training and Synthesis projects completed it is important to remember to activate the proper Python virtual environment when switching between projects. If scripts begin failing in a previously working environment, the cause might be that the incorrect virtual environment is active or that no virtual environment has been activated.



### Embedded Software Development Kit (MSDK)

The Software Development Kit (MSDK) for MAX78000 and MAX78002 is used to compile, flash, and debug the output of the *ai8x-synthesis* (“izer”) tool. It also enables general software development for the microcontroller cores of the MAX78000 and MAX78002. It consists of the following components:

* Peripheral Drivers
* Board Support Packages (BSPs)
* Libraries
* Examples
* Toolchain
  * Arm GCC
  * RISC-V GCC
  * Make
  * OpenOCD

There are two ways to install the MSDK.

#### Method 1: MSDK Installer

An automatic installer is available for the MSDK. Instructions for downloading, installing, and getting started with the MSDK’s supported development environments are found in the [**MSDK User Guide**](https://analogdevicesinc.github.io/msdk/USERGUIDE/).

After installation and setup, continue with the [Final Check](#final-check).

#### Method 2: Manual Installation

The MSDK is also available as a [git repository](https://github.com/analogdevicesinc/msdk), which can be used to obtain the latest development resources. The repository contains all of the MSDK’s components _except_ the Arm GCC, RISC-V GCC, and Make. These can be downloaded and installed manually.

1. Clone the MSDK repository (recommendation: change to the *ai8x-synthesis* folder first):

    ```shell
    $ git clone https://github.com/analogdevicesinc/msdk.git sdk
    ```

2. Download and install the Arm Embedded GNU Toolchain from [https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).

    * Recommended version: 12.3.Rel1 *(newer versions may or may not work correctly)*
    * Recommended installation location: `/usr/local/arm-gnu-toolchain-12.3.rel1/`

3. Download and install the RISC-V Embedded GNU Toolchain from [https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases](https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/)

    * Recommended version: 12.3.0-2 *(newer versions may or may not work correctly)*
    * Recommended installation location: `/usr/local/xpack-riscv-none-elf-gcc-12.3.0-2/`

4. Install GNU Make

    * (Linux/macOS) “make” is available on most systems by default. If not, it can be installed via the system package manager.

    * (Windows) Install [MSYS2](https://www.msys2.org/) first, then install “make” using the MSYS2 package manager:

      ```shell
      $ pacman -S --needed base filesystem msys2-runtime make
      ```

5. Install packages for OpenOCD. OpenOCD binaries are available in the “openocd” sub-folder of the ai8x-synthesis repository. However, some additional dependencies are required on most systems. See [openocd/README.md](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/openocd/README.md) for a list of packages to install, then return here to continue.

6. Add the location of the toolchain binaries to the system path.

    On Linux and macOS, copy the following contents into `~/.profile`...
    On macOS, _also_ copy the following contents into `~/.zprofile`...
    ...adjusting for the actual `PATH` to the compilers and the system’s architecture (`TARGET_ARCH`):

    ```shell
    # Arm GCC
    ARMGCC_DIR=/usr/local/gcc-arm-none-eabi-10.3-2021.10  # Change me!
    echo $PATH | grep -q -s "$ARMGCC_DIR/bin"
    if [ $? -eq 1 ] ; then
        PATH=$PATH:"$ARMGCC_DIR/bin"
        export PATH
        export ARMGCC_DIR
    fi
    
    # RISC-V GCC
    RISCVGCC_DIR=/usr/local/xpack-riscv-none-elf-gcc-12.3.0-2  # Change me!
    echo $PATH | grep -q -s "$RISCVGCC_DIR/bin"
    if [ $? -eq 1 ] ; then
        PATH=$PATH:"$RISCVGCC_DIR/bin"
        export PATH
        export RISCVGCC_DIR
    fi
    
    # OpenOCD
    OPENOCD_DIR=$HOME/Documents/Source/ai8x-synthesis/openocd/bin/TARGET_ARCH  # Change me!
    echo $PATH | grep -q -s "$OPENOCD_DIR"
    if [ $? -eq 1 ] ; then
        PATH=$PATH:$OPENOCD_DIR
        export PATH
        export OPENOCD_DIR
    fi
    ```

    On Windows, add the toolchain paths to the system `PATH` variable (search for  “edit the system environment variables” in the Windows search bar).

Once the tools above have been installed, continue to the [Final Check](#final-check) step below.

#### Final Check

After a successful manual or MSDK installation, the following commands will run from on the terminal and display their version numbers:

* `arm-none-eabi-gcc -v`
* `arm-none-eabi-gdb -v`
* `make -v`
* `openocd -v`

`gen-demos-max78000.sh` and `gen-demos-max78002.sh` will create code that is compatible with the MSDK and copy it into the MSDK’s Example directories.

---



## MAX78000 and MAX78002 Hardware and Resources

MAX78000/MAX78002 are embedded accelerators. Unlike GPUs, MAX78000/MAX78002 do not have gigabytes of memory, and cannot support arbitrary data (image) sizes.

### Overview

A typical CNN operation consists of pooling followed by a convolution. While these are traditionally expressed as separate layers, pooling can be done “in-flight” on MAX78000/MAX78002 for greater efficiency.

To minimize data movement, the accelerator is optimized for convolutions with in-flight pooling on a sequence of layers. MAX78000 and MAX78002 also support in-flight element-wise operations, pass-through layers and 1D convolutions (without element-wise operations):

![CNNInFlight](docs/CNNInFlight.png)

The MAX78000/MAX78002 accelerators contain 64 parallel processors. There are four quadrants that contain 16 processors each.

Each processor includes a pooling unit and a convolutional engine with dedicated weight memory:

![Overview](docs/Overview.png)

Data is read from [data memory](#data-memory) associated with the processor, and written out to any data memory located within the accelerator. To run a deep convolutional neural network, multiple layers are chained together, where each layer’s operation is individually configurable. The output data from one layer is used as the input data for the next layer, for up to 32 layers (where *in-flight* pooling and *in-flight* element-wise operations do not count as layers).

The following picture shows an example view of a 2D convolution with pooling:
![Example](docs/CNNOverview.png)

### Data, Weights, and Processors

Data memory, weight memory, and processors are interdependent.

In the MAX78000/MAX78002 accelerator, processors are organized as follows:

* Each processor is connected to its own dedicated weight memory instance.
* A group of four processors shares one data memory instance.
* A quadrant of sixteen processors shares certain common controls and can be operated tethered to another quadrant, or independently/separately.

Any given processor can:

* Read from its dedicated weight memory,
* Read from the data memory instance it shares with three other processors, and
* As part of output processing, write to *any* data memory instance.

#### Weight Memory

*Note: Depending on context, weights may also be referred to as “kernels” or “masks”. Additionally, weights are also part of a network’s “parameters”.*

For each of the four 16-processor quadrants, weight memory and processors can be visualized as follows. Assuming one input channel processed by processor 0, and 8 output channels, the 8 shaded kernels will be used:

![Weight Memory Map](docs/KernelMemory.png)

*Note: Weights that are not 3×3×8 (= 72-bits) per kernel are packed to save space. For example, when using 1×1 8-bit kernels, 9 kernels will be packed into a single 72-bit memory word.*

#### Data Memory

Data memory in MAX78000/MAX78002 is needed for:

* Input data (unless [FIFOs](#fifos) are used),
* All layer’s activation data, and
* Inference outputs.

Data memory connections can be visualized as follows:

<img src="docs/DataMemory.png" alt="Data Memory Map" style="zoom: 67%;" />

All input data must be located in the data memory instance the processor can access. Conversely, output data can be written to any data memory instance inside the accelerator (but not to general purpose SRAM on the Arm microcontroller bus).

The data memory instances inside the accelerator are single-port memories. This means that only one access operation can happen per clock cycle. When using the HWC data format (see [Channel Data Formats](#channel-data-formats)), this means that each of the four processors sharing the data memory instance will receive one byte of data per clock cycle (since each 32-bit data word consists of four packed channels).

##### Multi-Pass

When data has more channels than active processors, “multi-pass” is used. Each processor works on more than one channel, using multiple sequential passes, and each data memory holds more than four channels.

As data is read using multiple passes, and all available processor work in parallel, the first pass reads channels 0 through 63, the second pass reads channels 64 through 127, etc., assuming 64 processors are active.

For example, if 192-channel data is read using 64 active processors, Data Memory 0 stores three 32-bit words: channels 0, 1, 2, 3 in the first word, 64, 65, 66, 67 in the second word, and 128, 129, 130, 131 in the third word. Data Memory 1 stores channels 4, 5, 6, 7 in the first word, 68, 69, 70, 71 in the second word, and 132, 133, 134, 135 in the third word, and so on. The first processor processes channel 0 in the first pass, channel 64 in the second pass, and channel 128 in the third pass.

*Note: Multi-pass also works with channel counts that are not a multiple of 64, and can be used with fewer than 64 active processors.*

*Note: For all multi-pass cases, the processor count per pass is rounded up to the next multiple of 4.*

### Streaming Mode

The machine also implements a streaming mode. Streaming allows input data dimensions that exceed the available per-channel data memory in the accelerator. *Note: Depending on the model and application, [Data Folding](#data-folding) may have performance benefits over Streaming Mode.*

The following illustration shows the basic principle: In order to produce the first output pixel of the second layer, not all data needs to be present at the input. In the example, a 5×5 input needs to be available.

<img src="docs/Streaming.png" alt="Illustration of Streaming Mode"/>

In the accelerator implementation, data is shifted into the Tornado memory in a sequential fashion, so prior rows will be available as well. In order to produce the _blue_ output pixel, input data up to the blue input pixel must be available.

![Streaming-Rows](docs/Streaming-Rows.png)

When the _yellow_ output pixel is produced, the first (_black_) pixel of the input data is no longer needed and its data can be discarded:

![Streaming-NextPixel](docs/Streaming-NextPixel.png)

The number of discarded pixels is network specific and dependent on pooling strides and the types of convolution. In general, streaming mode is only useful for networks where the output data dimensions decrease from layer to layer (for example, by using a pooling stride).

*Note: Streaming mode requires the use of [FIFOs](#fifos).*

For concrete examples on how to implement streaming mode with a camera, please see the [Camera Streaming Guide](https://github.com/analogdevicesinc/MaximAI_Documentation/blob/main/Guides/Camera_Streaming_Guide.md).

#### FIFOs

Since the data memory instances are single-port memories, software would have to temporarily disable the accelerator in order to feed it new data. Using FIFOs, software can input available data while the accelerator is running. The accelerator will autonomously fetch data from the FIFOs when needed, and stall (pause) when no enough data is available.

The MAX78000/MAX78002 accelerator has two types of FIFO:

##### Standard FIFOs

There are four dedicated FIFOs connected to processors 0-3, 16-19, 32-35, and 48-51, supporting up to 16 input channels (in HWC format) or four channels (CHW format). These FIFOs work when used from the Arm Cortex-M4 core and from the RISC-V core.

The standard FIFOs are selected using the `--fifo` argument for `ai8xize.py`.

##### Fast FIFO

The fast FIFO is only available from the RISC-V core, and runs synchronously with the RISC-V for increased throughput. It supports up to four input channels (HWC format) or a single channel (CHW format). The fast FIFO is connected to processors 0, 1, 2, 3 or 0, 16, 32, 48.

The fast FIFO is selected using the `--fast-fifo` argument for `ai8xize.py`.

*The code generator inserts FIFO-full checks for either type of FIFO. When the data source rate is equal to or slower than the network speed, these checks are not needed. Use `--no-fifo-wait` to suppress them. The checks are necessary when the data source can deliver faster than the network can process the data.*

### Number Format

All weights, bias values and data are stored and computed in Q7 format (signed two’s complement 8-bit integers, [–128...+127]). See <https://en.wikipedia.org/wiki/Q_%28number_format%29>.

The 8-bit value $w$ is defined as:

$$ w = (-a_7 2^7+a_6 2^6+a_5 2^5+a_4 2^4+a_3 2^3+a_2 2^2+a_1 2^1+a_0)/128 $$

<img src="docs/Numbers.png" alt="76543210" style="zoom:67%;" />

Examples:
| Binary    | Value        |
|:---------:|-------------:|
| 0000 0000 | 0            |
| 0000 0001 | 1/128        |
| 0000 0010 | 2/128        |
| 0111 1110 | 126/128      |
| 0111 1111 | 127/128      |
| 1000 0000 | −128/128 (–1)|
| 1000 0001 | −127/128     |
| 1000 0010 | −126/128     |
| 1111 1110 | −2/128       |
| 1111 1111 | −1/128       |

On MAX78000/MAX78002, _weights_ can be 1, 2, 4, or 8 bits wide (configurable per layer using the `quantization` key). Bias values are always 8 bits wide. Data is 8 bits wide, *except for the last layer that can optionally output 32 bits of unclipped data in Q17.14 format when not using activation.*

|          weight bits          |  min |  max |
| :---------------------------: | ---: | ---: |
|               8               | –128 | +127 |
|               4               |   –8 |    7 |
|               2               |   –2 |    1 |
|               1               |   –1 |    0 |
| *MAX78002 only*             1 |   –1 |   +1 |

Note that for –1/0 1-bit weights (and, to a lesser degree, –1/+1 1-bit weights and 2-bit weights) require the use of bias to produce useful results. Without bias, all sums of products of activated data from a prior layer would be negative, and activation of that data would always be zero.

In other cases, using bias in convolutional layers does not improve inference performance. In particular, [Quantization](#quantization)-Aware Training (QAT) optimizes the weight distribution, possibly deteriorating the distribution of the bias values.

#### Rounding

MAX78000/MAX78002 rounding (for the CNN sum of products) uses “round half towards positive infinity”, i.e. $y=⌊0.5+x⌋$. This rounding method is not the default method in either Excel or Python/NumPy. The rounding method can be achieved in NumPy using `y = np.floor(0.5 + x)` and in Excel as `=FLOOR.PRECISE(0.5 + X)`.

By way of example:

| Input                    | Rounded |
|:-------------------------|:-------:|
| +3.5                     | +4      |
| +3.25, +3.0, +2.75, +2.5 | +3      |
| +2.25, +2.0, +1.75, +1.5 | +2      |
| +1.25, +1.0, +0.75, +0.5 | +1      |
| +0.25, 0, –0.25, –0.5    | 0       |
| –0.75, –1.0, –1.25, –1.5 | –1      |
| –1.75, –2.0, –2.25, –2.5 | –2      |
| –2.75, –3.0, –3.25, –3.5 | –3      |

#### Addition

Addition works similarly to regular two’s-complement arithmetic.

Example:
$$ w_0 = 1/64 → 00000010 $$
$$ w_1 = 1/2 → 01000000 $$
$$ w_0 + w_1 = 33/64 → 01000010 $$

#### Saturation and Clipping

Values smaller than $–128⁄128$ are saturated to $–128⁄128$ (1000 0000). Values larger than $+127⁄128$ are saturated to $+127⁄128$ (0111 1111).

The MAX78000/MAX78002 CNN sum of products uses full resolution for both products and sums, so the saturation happens only at the very end of the computation.

Example 1:

$$ w_0 = 127/128 → 01111111 $$
$$ w_1 = 127/128 → 01111111 $$
$$ w_0 + w_1 = 254/128 → saturate → 01111111 (= 127/128) $$

Example 2:

$$ w_0 = -128/128 → 10000000 $$
$$ w_1 = -128/128 → 10000000 $$
$$ w_0 + w_1 = -256/128 → saturate → 10000000 (= -128/128) $$

#### Multiplication

Since operand values are implicitly divided by 128, the product of two values has to be shifted in order to maintain magnitude when using a standard multiplier (e.g., 8×8):

$$ w_0 * w_1 = \frac{w'_0}{128} * \frac{w'_1}{128} = \frac{w'_0 * w'_1}{128} ≫ 7 $$

In software,

* Determine the sign bit: $s = sign(w_0) * sign(w_1)$
* Convert operands to absolute values: $w'_0 = abs(w_0); w'_1 = abs(w_1)$
* Multiply using standard multiplier: $w'_0 * w'_1 = w''_0/128 * w''_1/128; r' = w''_0 * w''_1$
* Shift: $r'' = r' ≫ 7$
* Round up/down depending on $r'[6]$
* Apply sign: $r = s * r''$

Example 1:

$$ w_0 = 1/64 → 00000010 $$
$$ w_1 = 1/2 → 01000000 $$
$$ w_0 * w_1 = 1/128 → shift, truncate → 00000001 (= 1/128) $$

A “standard” two’s-complement multiplication would return 00000000 10000000. The MAX78000/MAX78002 data format discards the rightmost bits.

Example 2:

$$ w_0 = 1/64 → 00000010 $$
$$ w_1 = 1/4 → 00100000 $$
$$ w_0 * w_1 = 1/256 → shift, truncate → 00000000 (= 0) $$

“Standard” two’s-complement multiplication would return 00000000 01000000, the MAX78000/MAX78002 result is truncated to 0 after the shift operation.

#### Sign Bit

Operations preserve the sign bit.

Example 1:

$$ w_0 = -1/64 → 11111110 $$
$$ w_1 = 1/4 → 00100000 $$
$$ w_0 * w_1 = -1/256 → shift, truncate → 00000000 (= 0) $$

* Determine the sign bit: $s = sign(-1/64) * sign(1/4) = -1 * 1 = -1$
* Convert operands to absolute values: $w'_0 = abs(-1/64); w'_1 = abs(1/4)$
* Multiply using standard multiplier: $r' = 1/64 ≪ 7 * 1/4 ≪ 7 = 2 * 32 = 64$
* Shift: $r'' = r' ≫ 7 = 64 ≫ 7 = 0$
* Apply sign: $r = s * r'' = -1 * 0 = 0$

Example 2:

$$ w_0 = -1/64 → 11111110 $$
$$ w_1 = 1/2 → 01000000 $$
$$ w_0 * w_1 = -1/128 → shift, truncate → 11111111 (= -1/128) $$

* Determine the sign bit: $s = sign(-1/64) * sign(1/2) = -1 * 1 = -1$
* Convert operands to absolute values: $w'_0 = abs(-1/64); w'_1 = abs(1/2)$
* Multiply using standard multiplier: $r' = 1/64 ≪ 7 * 1/2 ≪ 7 = 2 * 64 = 128$
* Shift: $r'' = r' ≫ 7 = 128 ≫ 7 = 1$
* Apply sign: $r = s * r'' = -1 * 1 ≫ 7 = -1/128$

Example 3:

$$ w_0 = 127/128 → 01111111 $$
$$ w_1 = 1/128 → 00000001 $$
$$ w_0 * w_1 = 128/128 → saturation → 01111111 (= 127/128) $$

### Channel Data Formats

#### HWC (Height-Width-Channels)

All internal data are stored in HWC format, four channels per 32-bit word. Assuming 3-color (or 3-channel) input, one byte of the 32-bit word will be unused. The highest frequency in this data format is the channel, so the channels are interleaved.

Example:

![0BGR 0BGR 0 BGR 0BGR...](docs/HWC.png)

#### CHW (Channels-Height-Width)

The input layer (and *only* the input layer) can alternatively also use the CHW format (a sequence of channels). The highest frequency in this data format is the width W or X-axis, and the lowest frequency is the channel C. Assuming an RGB input, all red pixels are followed by all green pixels, followed by all blue pixels.

Example:

![RRRRRR...GGGGGG...BBBBBB...](docs/CHW.png)



#### Considerations for Choosing an Input Format

The accelerator supports both HWC and CHW input formats to avoid unnecessary data manipulation. Choose the format that results in the least amount of data movement for a given input.

Internal layers and the output layer always use the HWC format.

In general, HWC is faster since each memory read can deliver data to up to four processors in parallel. On the other hand, four processors must share one data memory instance, which reduces the maximum allowable dimensions of the input layer.

#### CHW Input Data Format and Consequences for Weight Memory Layout

When using the CHW data format, only one of the four processors sharing the data memory instance can be used. The next channel needs to use a processor connected to a different data memory instance, so that the machine can deliver one byte per clock cycle to each enabled processor.

Because each processor has its own dedicated weight memory, this will introduce “gaps” in the weight memory map, as shown in the following illustration:

![Kernel Memory Gaps](docs/KernelMemoryGaps.png)


### Active Processors and Layers

For each layer, a set of active processors must be specified. The number of input channels for the layer must be equal to, or be a multiple of, the active processors, and the input data for that layer must be located in data memory instances accessible to the selected processors.

It is possible to specify a relative offset into the data memory instance that applies to all processors.
_Example:_ Assuming HWC data format, specifying the offset as 16,384 bytes (or 0x4000) will cause processors 0-3 to read their input from the second half of data memory 0, processors 4-7 will read from the second half of data memory instance 1, etc.

For most simple networks with limited data sizes, it is easiest to ping-pong between the first and second halves of the data memories – specify the data offset as 0 for the first layer, 0x4000 for the second layer, 0 for the third layer, etc. This strategy avoids overlapping inputs and outputs when a given processor is used in two consecutive layers.

Even though it is supported by the accelerator, the Network Generator will not be able to check for inadvertent overwriting of unprocessed input data by newly generated output data when overlapping data or streaming data. Use the `--overlap-data` command line switch to disable these checks, and to allow overlapped data.

### Layers and Weight Memory

For each layer, the weight memory start column is automatically configured by the Network Loader. The start column must be a multiple of 4, and the value applies to all processors.

The following example shows the weight memory layout for two layers. The first layer (L0) has 8 inputs and 10 outputs, and the second layer (L1) has 10 inputs and 2 outputs.

![Layers and Weight Memory](docs/KernelMemoryLayers.png)

#### Bias Memories

Bias values are stored in separate bias memories. There are four bias memory instances available, and a layer can access any bias memory instance where at least one processor is enabled. By default, bias memories are automatically allocated using a modified Fit-First Descending (FFD) algorithm. Before considering the required resource sizes in descending order, and placing values in the bias memory with the most available resources, the algorithm places those bias values that require a single specified bias memory. The bias memory allocation can optionally be controlled using the [`bias_group`](#bias_group-optional) configuration option.

### Weight Storage Example

The file `ai84net.xlsx` contains an example for a single-channel CHW input using the `AI84Net5` network (this example also supports up to four channels in HWC).

*Note*: As described above, multiple CHW channels must be loaded into separate memory instances. When using a large number of channels, this can cause “holes” in the processor map, which in turn can cause subsequent layers’ kernels to require padding.

The Network Loader prints a kernel map that shows the kernel arrangement based on the provided network description. It will also flag cases where kernel or bias memories are exceeded.

### Example: `Conv2d`

The following picture shows an example of a `Conv2d` with 1×1 kernels, five input channels, two output channels, and a data size of 2×2. The inputs are shown on the left, and the outputs on the right, and the kernels are shown lined up with the associated inputs — the number of kernel rows matches the number of input channels, and the number of kernel columns matches the number of output channels. The lower half of the picture shows how the data is arranged in memory when HWC data is used for both input and output.

![Conv2Dk1x1](docs/Conv2Dk1x1.png)

### Activation Functions

MAX78000/MAX78002 hardware provides several activation functions.

#### None

There is always an implicit non-linearity when outputting 8-bit data since outputs are [clamped](#saturation-and-clipping) to $[–128, +127]$ (or $[–128/128, +127/128]$ during training). Due to the clamping, “no activation” behaves similar to PyTorch’s `nn.Hardtanh(min_value=-128[/128], max_value=127[/128])`.

<img src="docs/noactivation.png" alt="no activation" style="zoom:33%;" />

#### ReLU

All output values are [clipped (saturated)](#saturation-and-clipping) to $[0, +127]$. Because of this, `ReLU` behaves more similar to PyTorch’s `nn.Hardtanh(min_value=0, max_value=127[/128])` than to PyTorch’s `nn.ReLU()`.

<img src="docs/relu.png" alt="relu" style="zoom:33%;" />

#### Abs

`Abs` returns the absolute value for all inputs, and then [clamps](#saturation-and-clipping) the outputs to $[0, +127]$, similar to PyTorch `abs()` followed by `nn.Hardtanh(min_value=0, max_value=127[/128])`.

<img src="docs/abs.png" alt="abs" style="zoom:33%;" />

### Limitations of MAX78000 Networks

The MAX78000 hardware does not support arbitrary network parameters. Specifically,

* `Conv2d`:
  
  * Kernel sizes must be 1×1 or 3×3.
    *Note: Stacked 3×3 kernels can achieve the effect of larger kernels. For example, two consecutive layers with 3×3 kernels have the same receptive field as a 5×5 kernel. To achieve the same activation as a 5×5 kernel, additional layers are necessary.*
    *Note: 2×2 kernels can be emulated by setting one row and one column of 3×3 kernels to zero.*
  * Padding can be 0, 1, or 2. Padding always uses zeros.
  * Stride is fixed to [1, 1].
  * Dilation is fixed to 1.
  * Groups must be 1.
  
* `Conv1d`:
  
  * Kernel lengths must be 1 through 9.
  * Padding can be 0, 1, or 2.
  * Stride is fixed to 1.
  * Dilation can be 1 to 1023 for kernel lengths 1, 2, or 3 and is fixed to 1 for kernels with length greater than 3.
  
* `ConvTranspose2d`:

  * Kernel sizes must be 3×3.
  * Padding can be 0, 1, or 2.
  * Stride is fixed to [2, 2]. Output padding is fixed to 1.

* A programmable layer-specific shift operator is available at the output of a convolution, see [`output_shift` (Optional)](#output_shift-optional).

* The supported [activation functions](#activation-functions) are `ReLU` and `Abs`, and a limited subset of `Linear`. *Note that due to [clipping](#saturation-and-clipping), non-linearities are introduced even when not explicitly specifying an activation function.*

* Pooling:
  * Both max pooling and average pooling are available, with or without convolution.
  
  * Pooling does not support padding.
  
  * Pooling more than 64 channels requires the use of a “fused” convolution in the same layer, unless the pooled dimensions are 1×1.
  
  * Pooling strides can be 1 through 16. For 2D pooling, the stride is the same for both dimensions.
  
  * For 2D pooling, supported pooling kernel sizes are 1×1 through 16×16, including non-square kernels. 1D pooling supports kernel sizes from 1 through 16. *Note: Pooling kernel size values do not have to be the same as the pooling stride.*
  
  * Dilation must be 1.
  
  * Average pooling is implemented both using `floor()`and using rounding (half towards positive infinity). Use the `--avg-pool-rounding` switch to turn on rounding in the training software and the Network Generator.
  
    Example:
  
    * _floor:_ Since there is a quantization step at the output of the average pooling, a 2×2 `AvgPool2d` of `[[0, 0], [0, 3]]` will return $\lfloor \frac{3}{4} \rfloor = 0$.
    * _rounding:_ 2×2 `AvgPool2d` of `[[0, 0], [0, 3]]` will return $\lfloor \frac{3}{4} \rceil = 1$.
  
* The number of input channels must not exceed 1024 per layer.

* The number of output channels must not exceed 1024 per layer.

  * Bias is supported for up to 512 output channels per layer.

* The number of layers must not exceed 32 (where pooling and element-wise operations do not add to the count when preceding a convolution).

* The maximum dimension (number of rows or columns) for input or output data is 1023.
  
* Streaming mode:
  
  * When using data greater than 8192 pixels per channel (approximately 90×90 when width = height) in HWC mode, or 32,768 pixels per channel (181×181 when width = height) in CHW mode, and [Data Folding](#data-folding) techniques are not used, then `streaming` mode must be used.
  * When using `streaming` mode, the product of any layer’s input width, input height, and input channels divided by 64 rounded up must not exceed 2^21: $width * height * ⌈\frac{channels}{64}⌉ < 2^{21}$; _width_ and _height_ must not exceed 1023.
  * Streaming is limited to 8 consecutive layers or fewer, and is limited to four FIFOs (up to 4 input channels in CHW and up to 16 channels in HWC format), see [FIFOs](#fifos).
  * For streaming layers, bias values may not be added correctly in all cases.
  * The *final* streaming layer must use padding.
  * Layers that use 1×1 kernels without padding are automatically replaced with equivalent layers that use 3×3 kernels with padding.
  
* The weight memory supports up to 768 * 64 3×3 Q7 kernels (see [Number Format](#number-format)), for a total of [432 KiB of kernel memory](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/AHBAddresses.md).
  When using 1-, 2- or 4-bit weights, the capacity increases accordingly.
  When using more than 64 input or output channels, weight memory is shared, and effective capacity decreases proportionally (for example, 128 input channels require twice as much space as 64 input channels, and a layer with <u>both</u> 128 input and 128 output channels requires <u>four</u> times as much space as a layer with only 64 input channels and 64 output channels).
  Weights must be arranged according to specific rules detailed in [Layers and Weight Memory](#layers-and-weight-memory).

* There are 16 instances of 32 KiB data memory ([for a total of 512 KiB](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/AHBAddresses.md)). When not using streaming mode, any data channel (input, intermediate, or output) must completely fit into one memory instance. This limits the first-layer input to 32,768 pixels per channel in the CHW format (181×181 when width = height). However, when using more than one input channel, the HWC format may be preferred, and all layer outputs are in HWC format as well. In those cases, it is required that four channels fit into a single memory instance — or 8192 pixels per channel (approximately 90×90 when width = height).
  Note that the first layer commonly creates a wide expansion (i.e., a large number of output channels) that needs to fit into data memory, so the input size limit is mostly theoretical. In many cases, [Data Folding](#data-folding) (distributing the input data across multiple channels) can effectively increase both the input dimensions as well as improve model performance.

* The hardware supports 1D and 2D convolution layers, 2D transposed convolution layers (upsampling), element-wise addition, subtraction, binary OR, binary XOR as well as fully connected layers (`Linear`), which are implemented using 1×1 convolutions on 1×1 data:
  * The maximum number of input neurons is 1024, and the maximum number of output neurons is 1024 (16 each per processor used).
  
  * `Flatten` functionality is available to convert 2D input data for use by fully connected layers, see [Fully Connected Layers](#fully-connected-linear-layers).
  
  * When “flattening” two-dimensional data, the input dimensions (C×H×W) must satisfy C×H×W ≤ 16,384, and H×W ≤ 256. Pooling cannot be used at the same time as flattening.
  
  * Element-wise operators support from 2 up to 16 inputs.
  
  * Element-wise operators can be chained in-flight with pooling and 2D convolution (where the order of pooling and element-wise operations can be swapped).
  
  * For convenience, a `Softmax` operator is supported in software.
  
* Since the internal network format is HWC in groups of four channels, output concatenation only works properly when all components of the concatenation other than the last have multiples of four channels.

* Supported element-wise operations are `add`, `sub`, `bitwise xor`, and `bitwise or`. Element-wise operations can happen “in-flight” in the same layer as a convolution.

* Groups, and depthwise separable convolutions are not supported. *Note: Batch normalization should be folded into the weights, see [Batch Normalization](#batch-normalization).*



### Limitations of MAX78002 Networks

The MAX78002 hardware does not support arbitrary network parameters. Specifically,

* `Conv2d`:

  * Kernel sizes must be 1×1 or 3×3.
    *Note: Stacked 3×3 kernels can achieve the effect of larger kernels. For example, two consecutive layers with 3×3 kernels have the same receptive field as a 5×5 kernel. To achieve the same activation as a 5×5 kernel, additional layers are necessary.*
    *Note: 2×2 kernels can be emulated by setting one row and one column of 3×3 kernels to zero.*
  * Padding can be 0, 1, or 2. Padding always uses zeros.
  * Stride is fixed to [1, 1].
  * Dilation can be 1 to 16.
  * Groups can be 1, or the same as the number of input and output channels (depthwise separable convolution).

* `Conv1d`:

  * Kernel lengths must be 1 through 9.
  * Padding can be 0, 1, or 2, unless there are more than 64 input channels, when padding must be 0.
  * Stride is fixed to 1.
  * Dilation can be 1 to 2047 for kernel lengths 1, 2, or 3 and is fixed to 1 for kernels with length greater than 3.
  * Groups can be 1, or the same as the number of input and output channels (depthwise separable convolution).

* `ConvTranspose2d`:

  * Kernel sizes must be 3×3.
  * Padding can be 0, 1, or 2.
  * Stride is fixed to [2, 2]. Output padding is fixed to 1.

* A programmable layer-specific shift operator is available at the output of a convolution, see [`output_shift` (Optional)](#output_shift-optional).

* The supported [activation functions](#activation-functions) are `ReLU` and `Abs`, and a limited subset of `Linear`. *Note that due to [clipping](#saturation-and-clipping), non-linearities are introduced even when not explicitly specifying an activation function.*

* Pooling:

  * Both max pooling and average pooling are available, with or without convolution.

  * Pooling does not support padding.

  * Pooling strides can be 1 through 16. For 2D pooling, the stride is the same for both dimensions.

  * For 2D pooling, supported pooling kernel sizes are 1×1 through 16×16, including non-square kernels. 1D pooling supports kernel sizes from 1 through 16. *Note: Pooling kernel size values do not have to be the same as the pooling stride.*

  * Dilation is supported from 1 to 16, independently for both dimensions.

  * Average pooling is implemented both using `floor()`and using rounding (half towards positive infinity). Use the `--avg-pool-rounding` switch to turn on rounding in the training software and the Network Generator.

    Example:

    * _floor:_ Since there is a quantization step at the output of the average pooling, a 2×2 `AvgPool2d` of `[[0, 0], [0, 3]]` will return $\lfloor \frac{3}{4} \rfloor = 0$.
    * _rounding:_ 2×2 `AvgPool2d` of `[[0, 0], [0, 3]]` will return $\lfloor \frac{3}{4} \rceil = 1$.

* The number of input channels must not exceed 2048 per layer.

* The number of output channels must not exceed 2048 per layer.

* The number of layers must not exceed 128 (where pooling and element-wise operations do not add to the count when preceding a convolution).

* The maximum dimension (number of rows or columns) for input or output data is 2047.

* Streaming mode:

  * When using data greater than 20,480 pixels per channel in HWC mode (143×143 when height = width), or 81,920 pixels in CHW mode (286×286 when height = width), and [Data Folding](#data-folding) techniques are not used, then `streaming` mode must be used.
  * When using `streaming` mode, the product of any layer’s input width, input height, and input channels divided by 64 rounded up must not exceed 2^21: $width * height * ⌈\frac{channels}{64}⌉ < 2^{21}$; _width_ and _height_ must not exceed 2047.
  * Streaming is limited to 8 consecutive layers or fewer, and is limited to four FIFOs (up to 4 input channels in CHW and up to 16 channels in HWC format), see [FIFOs](#fifos).
  * Layers that use 1×1 kernels without padding are automatically replaced with equivalent layers that use 3×3 kernels with padding.
  * Streaming layers must use convolution (i.e., the `Conv1d`, `Conv2d`, or `ConvTranspose2d` [operators](#operation)).

* The weight memory of processors 0, 16, 32, and 48 supports up to 5,120 3×3 Q7 kernels (see [Number Format](#number-format)), all other processors support up to 4,096 3×3 Q7 kernels, for a total of [2,340 KiB of kernel memory](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/AHBAddresses.md).
  When using 1-, 2- or 4-bit weights, the capacity increases accordingly. The hardware supports two different flavors of 1-bit weights, either 0/–1 or +1/–1.
  When using more than 64 input or output channels, weight memory is shared, and effective capacity decreases.
  Weights must be arranged according to specific rules detailed in [Layers and Weight Memory](#layers-and-weight-memory).

* The total of [1,280 KiB of data memory](https://github.com/analogdevicesinc/ai8x-synthesis/blob/develop/docs/AHBAddresses.md) is split into 16 sections of 80 KiB each. When not using streaming mode, any data channel (input, intermediate, or output) must completely fit into one memory instance. This limits the first-layer input to 81,920 pixels per channel in CHW format (286×286 when height = width). However, when using more than one input channel, the HWC format may be preferred, and all layer outputs are in HWC format as well. In those cases, it is required that four channels fit into a single memory section — or 20,480 pixels per channel (143×143 when height = width).
  Note that the first layer commonly creates a wide expansion (i.e., a large number of output channels) that needs to fit into data memory, so the input size limit is mostly theoretical. In many cases, [Data Folding](#data-folding) (distributing the input data across multiple channels) can effectively increase both the input dimensions as well as improve model performance.

* The hardware supports 1D and 2D convolution layers, 2D transposed convolution layers (upsampling), element-wise addition, subtraction, binary OR, binary XOR as well as fully connected layers (`Linear`), which are implemented using 1×1 convolutions on 1×1 data:

  * The maximum number of input neurons is 1024, and the maximum number of output neurons is 1024 (16 each per processor used).
  * `Flatten` functionality is available to convert 2D input data for use by fully connected layers, see [Fully Connected Layers](#fully-connected-linear-layers).
  * When “flattening” two-dimensional data, the input dimensions (C×H×W) must satisfy C×H×W ≤ 16,384, and H×W ≤ 256. Pooling cannot be used at the same time as flattening.
  * Element-wise operators support from 2 up to 16 inputs.
  * Element-wise operators can be chained in-flight with pooling and 2D convolution (where the order of pooling and element-wise operations can be swapped).
  * For convenience, a `Softmax` operator is supported in software.

* The MAX78002 hardware supports executing layers sequentially or in programmed order, and it supports conditional branching based on data and address values and ranges and match counts.

* The MAX78002 hardware supports starting a network at any pre-programmed layer *(streaming is only supported in the first 8 layers)*. This can be used to run more than one network, and transitioning from one network to another.

* Since the internal network format is HWC in groups of four channels, output concatenation only works properly when all components of the concatenation other than the last have multiples of four channels.

* The MAX78002 hardware supports several processing speedups that accesses memory instances in parallel. The tools are capable of generating code that supports these speedups.

* Supported element-wise operations are `add`, `sub`, `xor`, and `or`. Element-wise operations can happen “in-flight” in the same layer as a convolution, *except* when the input is multi-pass (i.e., more than 64 channels), *and* a bias addition is also requested.

* *Note: Batch normalization should be folded into the weights, see [Batch Normalization](#batch-normalization).*



### Fully Connected (Linear) Layers

m×n fully connected layers can be realized in hardware by “flattening” 2D input data of dimensions C×H×W into m=C×H×W channels of 1×1 input data. The hardware will produce n channels of 1×1 output data. When chaining multiple fully connected layers, the flattening step is omitted. The following picture shows 2D data, the equivalent flattened 1D data, and the output.

For MAX78000/MAX78002, the product C×H×W must not exceed 16,384.

![MLP](docs/MLP.png)

### Upsampling (Fractionally-Strided 2D Convolutions)

The hardware supports 2D upsampling (“fractionally-strided convolutions,” sometimes called “deconvolution” even though this is not strictly mathematically correct). The PyTorch equivalent is `ConvTranspose2d` with a stride of 2.

The example shows a fractionally-strided convolution with a stride of 2, a pad of 1, and a 3×3 kernel. This “upsamples” the input dimensions from 3×3 to output dimensions of 6×6.

![fractionallystrided](docs/fractionallystrided.png)

---

## Model Training and Quantization

### Hardware Acceleration

If hardware acceleration is not available, skip the following two steps and continue with [Training Script](#training-script).

Before the first training session, check that hardware acceleration is available and recognized by PyTorch:

 ```shell
   (ai8x-training) $ python check_cuda.py
   System:                 linux
   Python version:         3.11.8 (main, Mar  4 2024, 15:29:36) [GCC 11.4.0]
   PyTorch version:        2.3.1+cu121
   CUDA/ROCm acceleration: available in PyTorch
   MPS acceleration:       NOT available in PyTorch
 ```

CUDA can be diagnosed using `nvidia-smi -q`:

```shell
(ai8x-training) $ nvidia-smi -q
...
Driver Version                            : 545.23.06
CUDA Version                              : 12.3

Attached GPUs                             : 2
GPU 00000000:01:00.0
    Product Name                          : NVIDIA TITAN RTX
    Product Brand                         : Titan
...
```

### Training Script

The main training software is `train.py`. It drives the training aspects, including model creation, checkpointing, model save, and status display (see `--help` for the many supported options, and the `scripts/train_*.sh` scripts for example usage).

The `models/` folder contains models that fit into the MAX78000 or MAX78002’s weight memory. These models rely on the MAX78000/MAX78002 hardware operators that are defined in `ai8x.py`.

To train the FP32 model for MNIST on MAX78000 or MAX78002, run `scripts/train_mnist.sh` from the `ai8x-training` project. This script will place checkpoint files into the log directory. Training makes use of the Distiller framework, but the `train.py` software has been modified slightly to improve it and add some MAX78000/MAX78002 specifics.

#### Distributed Training

On systems with multiple GPUs, the training script supports `DistributedDataParallel`. To use distributed training, prefix the training script with `scripts/distributed.sh`. For example, run `scripts/distributed.sh scripts/train_mnist.sh`. Note that (at this time) distributed training is only supported locally.

Since training can take a significant amount of time, the training script does not overwrite any weights previously produced. Results are placed in sub-directories under `logs/` named with the date and time when training began. The latest results are always soft-linked to by `latest-log_dir` and `latest_log_file`.

#### Troubleshooting

1. If the training script returns `ModuleNotFoundError: No module named 'numpy'`, please activate the virtual environment using `source .venv/bin/activate`, or on native Windows without WSL2, `source .venv/scripts/activate`.

2. If the training script crashes, or if it returns an internal error (such as `CUDNN_STATUS_INTERNAL_ERROR`), it may be necessary to limit the number of PyTorch workers to 1 (this has been observed running on native Windows). Add `--workers=1` when running any training script, for example;

   ```shell
   $ scripts/train_mnist.sh --workers=1
   ```

3. On resource constrained systems, training may abort with an error message such as `RuntimeError: unable to open shared memory object </torch_..._...> in read-write mode`. Add `--workers=0` when running the training script.

4. By default, many systems limit the number of open file descriptors.  `train.py` checks this limit and prints `WARNING: The open file limit is 2048. Please raise the limit (see documentation)` when the limit is low. When the limit is too low, certain actions might abort:

   ```shell
   (ai8x-training) $ scripts/evaluate_facedet_tinierssd.sh 
   WARNING: The open file limit is 1024. Please raise the limit (see documentation).
   ...
   --- test ---------------------
   165656 samples (256 per mini-batch)
   {'multi_box_loss': {'alpha': 2, 'neg_pos_ratio': 3}, 'nms': {'min_score': 0.75, 'max_overlap': 0.3, 'top_k': 20}}
   Traceback (most recent call last):
   ...
   RuntimeError: unable to open shared memory object </torch_202118_3977843486> in read-write mode
   OSError: [Errno 24] Too many open files
   ...
   ```

   To fix this issue, check `ulimit -n` (the soft limit) as well as `ulimit -n -H` (the hard limit) and raise the file descriptor limit using `ulimit -n NUMBER` where NUMBER cannot exceed the hard limit. Note that on many Linux systems, the defaults can be configured in `/etc/security/limits.conf`.

5. Datasets with larger-dimension images may require substantial amounts of system RAM. For example, `scripts/train_kinetics.sh` is configured for systems with 64 GB of RAM. When the system runs out of memory, training is abruptly killed and the error is logged to system journal. The following examples are from a system with 48 GB of RAM:

   ```shell
   ...
   Epoch: [13][  142/  142]    Overall Loss 1.078153    Objective Loss 1.078153    Top1 64.062500    LR 0.000500    Time 1.247024    
   --- validate (epoch=13)-----------
   1422 samples (32 per mini-batch)
   Epoch: [13][   10/   45]    Loss 1.082790    Top1 60.937500    
   Epoch: [13][   20/   45]    Loss 1.099474    Top1 60.312500    
   Epoch: [13][   30/   45]    Loss 1.113100    Top1 59.791667    
   Killed
   ```

   and from the system journal:

   ```shell
   kernel: oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/user.slice/user-1000.slice/session-11289.scope,task=python,pid=226828,uid=1000
   kernel: Out of memory: Killed process 226828 (python) total-vm:81269752kB, anon-rss:5711328kB, file-rss:146056kB, shmem-rss:648024kB, UID:1000 pgtables:97700kB oom_score_adj:0
   kernel: oom_reaper: reaped process 226828 (python), now anon-rss:0kB, file-rss:145268kB, shmem-rss:648024kB
   ```

   Training might succeed after reducing the batch size, reducing image dimensions, or pruning the dataset. Unfortunately, the only real fix for this issue is more system RAM. In the example, `kinetics_get_datasets()` from `datasets/kinetics.py` states “The current implementation of using 2000 training and 150 test examples per class at 240×240 resolution and 5 frames per second requires around 50 GB of RAM.”

6. On CUDA-capable machines, the training script by default uses PyTorch 2’s [`torch.compile()` feature](https://pytorch.org/docs/stable/generated/torch.compile.html) which improves execution speed. However, some models may not support this feature. It can be disabled using the command line option
   `--compiler-mode none`
   Disabling `torch.compile()` may also be necessary when using AMD ROCm acceleration.


### Example Training Session

Using the MNIST dataset and a simple model as an example, run `scripts/train_mnist.sh`. The following is the shortened output of an MNIST training session:

```shell
(ai8x-training) $ scripts/train_mnist.sh 
Configuring device: MAX78000, simulate=False.
Log file for this run: logs/2021.07.13-111453/2021.07.13-111453.log
{'start_epoch': 10, 'weight_bits': 8}
Optimizer Type: <class 'torch.optim.sgd.SGD'>
Optimizer Args: {'lr': 0.1, 'momentum': 0.9, 'dampening': 0, 'weight_decay': 0.0001, 'nesterov': False}
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to data/MNIST/raw/train-images-idx3-ubyte.gz
9913344it [00:01, 5712259.71it/s]                                                                                                                                                                                                                           
Extracting data/MNIST/raw/train-images-idx3-ubyte.gz to data/MNIST/raw

...

Dataset sizes:
        training=54000
        validation=6000
        test=10000
Reading compression schedule from: policies/schedule.yaml


Training epoch: 54000 samples (256 per mini-batch)
Named tensors and all their associated APIs are an experimental feature and subject to change. Please do not use them for anything important until they are released as stable. (Triggered internally at  /pytorch/c10/core/TensorImpl.h:1156.)

Epoch: [0][   10/  211]    Overall Loss 2.298435    Objective Loss 2.298435    Top1 13.710937    Top5 52.070313    LR 0.100000    Time 0.054167    
Epoch: [0][   20/  211]    Overall Loss 2.267082    Objective Loss 2.267082    Top1 16.464844    Top5 58.535156    LR 0.100000    Time 0.039278    
...
Epoch: [0][  211/  211]    Overall Loss 0.867936    Objective Loss 0.867936    Top1 71.101852    Top5 92.837037    LR 0.100000    Time 0.025054    

--- validate (epoch=0)-----------
6000 samples (256 per mini-batch)
Epoch: [0][   10/   24]    Loss 0.295286    Top1 91.367188    Top5 99.492188    
Epoch: [0][   20/   24]    Loss 0.293729    Top1 91.054688    Top5 99.550781    
Epoch: [0][   24/   24]    Loss 0.296180    Top1 91.000000    Top5 99.550000    
==> Top1: 91.000    Top5: 99.550    Loss: 0.296

==> Confusion:
[[581   2   3   1   2   3   4   3   2   4]
 [  0 675   4   1   3   0   1   4   0   0]
 [  5   6 501  21  11   2   4  25   7   4]
 [  1   4   7 549   3   5   0  11   2   1]
 [  2   6   7   0 525   1   3   9   0  12]
 [  0   8   2  10   5 464   3   8   6  12]
 [ 13  18   1   0  10   8 574   0   6   1]
 [  1  11   8   7   3   4   0 588   0   3]
 [ 26   4   7   5   9   9  16   5 482  21]
 [  4   9   5   7  36   8   0  19   6 521]]

==> Best [Top1: 91.000   Top5: 99.550   Sparsity:0.00   Params: 71148 on epoch: 0]
Saving checkpoint to: logs/2021.07.13-111453/checkpoint.pth.tar

...

Training epoch: 54000 samples (256 per mini-batch)
Epoch: [199][   10/  211]    Overall Loss 0.033614    Objective Loss 0.033614    Top1 98.984375    Top5 100.000000    LR 0.000100    Time 0.052778    
...
Epoch: [199][  211/  211]    Overall Loss 0.027310    Objective Loss 0.027310    Top1 99.181481    Top5 99.992593    LR 0.000100    Time 0.024874    

--- validate (epoch=199)-----------
6000 samples (256 per mini-batch)
Epoch: [199][   10/   24]    Loss 0.027533    Top1 98.984375    Top5 100.000000    
Epoch: [199][   20/   24]    Loss 0.028965    Top1 98.984375    Top5 100.000000    
Epoch: [199][   24/   24]    Loss 0.028365    Top1 98.983333    Top5 100.000000    
==> Top1: 98.983    Top5: 100.000    Loss: 0.028

==> Confusion:
[[599   0   1   1   0   0   3   0   0   1]
 [  0 685   0   1   0   0   0   2   0   0]
 [  0   1 581   0   0   0   0   2   2   0]
 [  0   0   1 578   0   2   0   1   1   0]
 [  0   1   1   0 558   0   0   0   1   4]
 [  1   0   0   2   0 513   1   0   1   0]
 [  2   1   0   0   1   0 625   0   2   0]
 [  0   1   3   1   0   0   0 619   0   1]
 [  1   0   1   1   1   1   2   0 577   0]
 [  0   0   0   0   2   1   0   6   2 604]]

==> Best [Top1: 99.283   Top5: 100.000   Sparsity:0.00   Params: 71148 on epoch: 180]
Saving checkpoint to: logs/2021.07.13-111453/qat_checkpoint.pth.tar
--- test ---------------------
10000 samples (256 per mini-batch)
Test: [   10/   40]    Loss 0.017528    Top1 99.453125    Top5 100.000000    
Test: [   20/   40]    Loss 0.015671    Top1 99.492188    Top5 100.000000    
Test: [   30/   40]    Loss 0.013522    Top1 99.583333    Top5 100.000000    
Test: [   40/   40]    Loss 0.013415    Top1 99.590000    Top5 100.000000    
==> Top1: 99.590    Top5: 100.000    Loss: 0.013

==> Confusion:
[[ 980    0    0    0    0    0    0    0    0    0]
 [   0 1133    1    0    0    0    0    1    0    0]
 [   1    0 1025    1    0    0    0    5    0    0]
 [   0    0    0 1010    0    0    0    0    0    0]
 [   0    0    0    0  978    0    2    0    0    2]
 [   0    0    0    3    0  888    1    0    0    0]
 [   0    1    0    0    1    2  953    0    1    0]
 [   0    1    0    0    0    0    0 1026    0    1]
 [   0    0    2    1    1    1    0    1  967    1]
 [   0    0    0    0    5    2    0    3    0  999]]


Log file for this run: logs/2021.07.13-111453/2021.07.13-111453.log

```

For classification, the “Top-1” score refers to the percentage of samples that returned the correct class (the correct target label), while “Top-5” is the percentage of samples the correct answer was one of the five highest ranked predictions. The “Loss” shows the output of the loss function that the training session aims to minimize (the “loss” numbers may be larger than 1, depending on the dataset and model). “LR” is the learning rate, and depending on the learning rate schedule used, LR may decrease as training progresses.

The “Confusion Matrix” shows both the target (expected) label on the vertical (Y) axis, as well as the highest ranked prediction on the horizontal (X) axis. If the network returns 100% expected labels, then only the diagonal (top left to bottom right) will contain values greater than 0.

When enabling TensorBoard (see [TensorBoard](#tensorboard)), these and other statistics are also available in graphical form:

![confusionmatrix](docs/confusionmatrix.png)

### Command Line Arguments

The following table describes the most important command line arguments for `train.py`. Use `--help` for a complete list.

| Argument                   | Description                                                  | Example                         |
| -------------------------- | ------------------------------------------------------------ | ------------------------------- |
| `--help`                   | Complete list of arguments                                   |                                 |
| *Device selection*         |                                                              |                                 |
| `--device`                 | Set device (default: AI84)                                   | `--device MAX78000`             |
| *Model and dataset*        |                                                              |                                 |
| `-a`, `--arch`, `--model`  | Set model (collected from models folder)                     | `--model ai85net5`              |
| `-f`, `--out-fold-ratio`   | Fold ratio for the model output (default: 1). Fold ratio 1 means no folding. | `--out-fold-ratio 4` |
| `--dataset`                | Set dataset (collected from datasets folder)                 | `--dataset MNIST`               |
| `--data`                   | Path to dataset (default: data)                              | `--data /data/ml`               |
| *Training*                 |                                                              |                                 |
| `--epochs`                 | Number of epochs to train (default: 90)                      | `--epochs 100`                  |
| `-b`, `--batch-size`       | Mini-batch size (default: 256)                               | `--batch-size 512`              |
| `--compress`               | Set compression and learning rate schedule                   | `--compress schedule.yaml`      |
| `--lr`, `--learning-rate`  | Set initial learning rate                                    | `--lr 0.001`                    |
| `--deterministic`          | Seed random number generators with fixed values              |                                 |
| `--resume-from`            | Resume from previous checkpoint                              | `--resume-from chk.pth.tar`     |
| `--qat-policy`             | Define QAT policy in YAML file (default: policies/qat_policy.yaml). Use “None” to disable QAT. | `--qat-policy qat_policy.yaml` |
| `--nas`                    | Enable network architecture search                           |                                 |
| `--nas-policy`             | Define NAS policy in YAML file                               | `--nas-policy nas/nas_policy.yaml` |
| `--regression` | Select regression instead of classification (changes Loss function, and log output) |  |
| `--compiler-mode` | Select [TorchDynamo optimization mode](https://pytorch.org/docs/stable/generated/torch.compile.html) (default: enabled on CUDA capable machines) | `--compiler-mode none` |
| `--dr` | Set target embedding dimensionality for dimensionality reduction                |`--dr 64`                        |
| `--scaf-lr` | Initial learning rate for sub-center ArcFace loss optimizer |  |
| `--scaf-scale` |Scale hyperparameter for sub-center ArcFace loss |  |
| `--scaf-margin` |Margin hyperparameter for sub-center ArcFace loss |  |
| `--backbone-checkpoint` |Path to checkpoint from which to load backbone weights |  |
| *Display and statistics*   |                                                              |                                 |
| `--enable-tensorboard`     | Enable logging to TensorBoard (default: disabled)            |                                 |
| `--confusion`              | Display the confusion matrix                                 |                                 |
| `--param-hist`             | Collect parameter statistics                                 |                                 |
| `--pr-curves`              | Generate precision-recall curves                             |                                 |
| `--embedding`              | Display embedding (using projector)                          |                                 |
| *Hardware*                 |                                                              |                                 |
| `--use-bias`               | The `bias=True` parameter is passed to the model. The effect of this parameter is model-dependent (the parameter does nothing, affects some operations, or all operations). |                                 |
| `--avg-pool-rounding`      | Use rounding for AvgPool                                     |                                 |
| *Evaluation*               |                                                              |                                 |
| `-e`, `--evaluate`         | Evaluate previously trained model                            |                                 |
| `--8-bit-mode`, `-8`       | Simulate quantized operation for hardware device (8-bit data). Used for evaluation only. |     |
| `--exp-load-weights-from`  | Load weights from file                                       |                                 |
| *Export*                   |                                                              |                                 |
| `--summary onnx`           | Export trained model to ONNX (default name: to model.onnx) — *see description below* |         |
| `--summary onnx_simplified` | Export trained model to simplified [ONNX](https://onnx.ai/) file (default name: model.onnx) |                     |
| `--summary-filename`       | Change the file name for the exported model                  | `--summary-filename mnist.onnx` |
| `--save-sample`            | Save data[index] from the test set to a NumPy pickle for use as sample data | `--save-sample 10` |
| `--slice-sample`  | For models that require RGB input, when the sample from the dataset has additional channels, slice the sample into 3 channels                                      |                                 |

#### ONNX Model Export

The ONNX model export (via `--summary onnx` or `--summary onnx_simplified`) is primarily intended for visualization of the model. ONNX does not support all of the operators that `ai8x.py` uses, and these operators are therefore removed from the export (see function `onnx_export_prep()` in `ai8x.py`). The ONNX file does contain the trained weights and *may* therefore be usable for inference under certain circumstances. However, it is important to note that the ONNX file **will not** be usable for training (for example, the ONNX `floor` operator has a gradient of zero, which is incompatible with quantization-aware training as implemented in `ai8x.py`).

### Observing GPU Resources

`nvidia-smi` can be used in a different terminal during training to examine the GPU resource usage of the training process. In the following example, the GPU is using 100% of its compute capabilities, but not all of the available memory. In this particular case, the batch size could be increased to use more memory.

```shell
$ nvidia-smi
+-----------------------------------------------------------------------------+
|  NVIDIA-SMI 470.42.01    Driver Version: 470.42.01    CUDA Version: 11.4    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:01:00.0  On |                  N/A |
| 39%   65C    P2   152W / 250W |   3555MiB / 11016MiB |    100%      Default |
+-------------------------------+----------------------+----------------------+
...
```

### Custom nn.Modules

The `ai8x.py` file contains customized PyTorch classes (subclasses of `torch.nn.Module`). Any model that is designed to run on MAX78000/MAX78002 should use these classes. There are three main changes over the default classes in `torch.nn.Module`:

1. Additional “Fused” operators that model in-flight pooling and activation.
2. Rounding, clipping and activation that matches the hardware.
3. Support for quantized operation (when using the `-8` command line argument).

#### set_device()

`ai8x.py` defines the `set_device()` function which configures the training system:

```python
def set_device(
        device,
        simulate,
        round_avg,
        verbose=True,
):
```

where *device* is `85` (the MAX78000 device code) or `87` (the MAX78002 device code), *simulate* is `True` when clipping and rounding are set to simulate hardware behavior, and *round_avg* picks one of the two hardware rounding modes for AvgPool.

#### update_model()

`ai8x.py` defines `update_model()`. This function is called after loading a checkpoint file, and recursively applies output shift, weight scaling, and quantization clamping to the model.



#### List of Predefined Modules

The following modules are predefined:

| Name                   | Description / PyTorch equivalent        |
| ---------------------- | --------------------------------------- |
| Conv2d                 | Conv2d                                  |
| FusedConv2dReLU        | Conv2d, followed by ReLU                |
| FusedConv2dAbs         | Conv2d, followed by Abs                 |
| MaxPool2d              | MaxPool2d                               |
| FusedMaxPoolConv2d     | MaxPool2d, followed by Conv2d           |
| FusedMaxPoolConv2dReLU | MaxPool2d, followed by Conv2d, and ReLU |
| FusedMaxPoolConv2dAbs  | MaxPool2d, followed by Conv2d, and Abs  |
| AvgPool2d              | AvgPool2d                               |
| FusedAvgPoolConv2d     | AvgPool2d, followed by Conv2d           |
| FusedAvgPoolConv2dReLU | AvgPool2d, followed by Conv2d, and ReLU |
| FusedAvgPoolConv2dAbs  | AvgPool2d, followed by Conv2d, and Abs  |
| ConvTranspose2d        | ConvTranspose2d                         |
| FusedConvTranspose2dReLU      | ConvTranspose2d, followed by ReLU |
| FusedConvTranspose2dAbs       | ConvTranspose2d, followed by Abs |
| FusedMaxPoolConvTranspose2d   | MaxPool2d, followed by ConvTranspose2d |
| FusedMaxPoolConvTranspose2dReLU       | MaxPool2d, followed by ConvTranspose2d, and ReLU |
| FusedMaxPoolConvTranspose2dAbs        | MaxPool2d, followed by ConvTranspose2d, and Abs |
| FusedAvgPoolConvTranspose2d           | AvgPool2d, followed by ConvTranspose2d |
| FusedAvgPoolConvTranspose2dReLU       | AvgPool2d, followed by ConvTranspose2d, and ReLU |
| FusedAvgPoolConvTranspose2dAbs        | AvgPool2d, followed by ConvTranspose2d, and Abs |
| Linear                 | Linear                                  |
| FusedLinearReLU        | Linear, followed by ReLU                |
| FusedLinearAbs         | Linear, followed by Abs                 |
| Conv1d                 | Conv1d                                  |
| FusedConv1dReLU        | Conv1d, followed by ReLU                |
| FusedConv1dAbs         | Conv1d, followed by Abs                 |
| MaxPool1d | MaxPool1d |
| FusedMaxPoolConv1d | MaxPool1d, followed by Conv1d |
| FusedMaxPoolConv1dReLU | MaxPool1d, followed by Conv1d, and ReLU |
| FusedMaxPoolConv1dAbs | MaxPool1d, followed by Conv1d, and Abs |
| AvgPool1d | AvgPool1d |
| FusedAvgPoolConv1d | AvgPool1d, followed by Conv1d |
| FusedAvgPoolConv1dReLU | AvgPool1d, followed by Conv1d, and ReLU |
| FusedAvgPoolConv1dAbs | AvgPool1d, followed by Conv1d, and Abs |
| Add | Element-wise Add |
| Sub | Element-wise Sub |
| BitwiseOr | Element-wise bitwise Or |
| BitwiseXor | Element-wise bitwise Xor |

#### Dropout

Dropout modules such as `torch.nn.Dropout()` and `torch.nn.Dropout2d()` are automatically disabled during inference, and can therefore be used for training without affecting inference. [Dropout](https://en.wikipedia.org/wiki/Dilution_(neural_networks)) can improve generalization by reducing overfitting, but should not be used for “analytical” functions.

*Note: Using [batch normalization](#batch-normalization) in conjunction with dropout can sometimes degrade training results.*

#### view(), reshape() and Flatten

There are two supported cases for `view()` or `reshape()`.

1. Conversion between 1D data and 2D data: Both the batch dimension (first dimension) and the channel dimension (second dimension) must stay the same. The height/width of the 2D data must match the length of the 1D data (i.e., H×W = L).
   Examples:
       `x = x.view(x.size(0), x.size(1), -1)  # 2D to 1D`
       `x = x.view(x.shape[0], x.shape[1], 16, -1)  # 1D to 2D`
   *Note: `x.size()` and `x.shape[]` are equivalent.*
   When reshaping data, `in_dim:` must be specified in the model description file.
2. Conversion from 1D and 2D to Fully Connected (“flattening”): The batch dimension (first dimension) must stay the same, and the other dimensions are combined (i.e., M = C×H×W or M = C×L).
   Example:
       `x = x.view(x.size(0), -1)  # Flatten`
   An alternate way to express the flatten operation is `torch.nn.Flatten()`.

#### Support for Quantization

The hardware always uses signed integers for data and weights. While data is always 8-bit, weights can be configured on a per-layer basis. However, training makes use of floating point values for both data and weights, while also clipping (clamping) values.

##### Data

When using the `-8` command line switch, all module outputs are quantized to 8-bit in the range [-128...+127] to simulate hardware behavior. The `-8` command line switch is designed for *evaluating quantized weights* against a test set, in order to understand the impact of quantization. *Note that model training always uses floating point values, and therefore `-8` is not compatible with training.*

The last layer can optionally use 32-bit output for increased precision. This is simulated by adding the parameter `wide=True` to the module function call.

##### Weights and Activations: Quantization-Aware Training (QAT)

Quantization-aware training (QAT) is enabled by default. QAT is controlled by a policy file, specified by `--qat-policy`.

* After `start_epoch` epochs, an intermediate epoch with no backpropagation will be realized to collect activation statistics. Each layer's activation ranges will be determined based on the range & resolution trade-off from the collected activations. Then, QAT will start and an additional parameter (`output_shift`) will be learned to shift activations for compensating weights  & biases scaling down.
* `weight_bits` describes the number of bits available for weights.
* `overrides` allows specifying the `weight_bits` on a per-layer basis.
* `outlier_removal_z_score` defines the z-score threshold for outlier removal during activation range calculation. (default: 8.0)
* `shift_quantile` defines the quantile of the parameters distribution to be used for the `output_shift` parameter. (default: 1.0)

By default, weights are quantized to 8-bits after 30 epochs as specified in `policies/qat_policy.yaml`. A more refined example that specifies weight sizes for individual layers can be seen in `policies/qat_policy_cifar100.yaml`.

Quantization-aware training can be <u>disabled</u> by specifying `--qat-policy None`.

The proper choice of `start_epoch` is important for achieving good results, and the default policy’s `start_epoch` may be much too small. As a rule of thumb, set `start_epoch` to a very high value (e.g., 1000) to begin, and then observe where in the training process the model stops learning. This epoch can be used as `start_epoch`, and the final network metrics (after an additional number of epochs) should be close to the non-QAT metrics. *Additionally, ensure that the learning rate after the `start_epoch` epoch is relatively small.*

For more information, please also see [Quantization](#quantization) and [QATv2](https://github.com/analogdevicesinc/ai8x-training/blob/develop/docs/QATv2.md).

#### Batch Normalization

Batch normalization after `Conv1d` and `Conv2d` layers is supported using “fusing.” The fusing operation merges the effect of batch normalization layers into the parameters of the preceding convolutional layer, by modifying weights and bias values of that preceding layer. For detailed information about batch normalization fusing/fusion/folding, see Section 3.2 of the following paper: <https://arxiv.org/pdf/1712.05877.pdf>.

After fusing/folding, the network will no longer contain any batchnorm layers. The effects of batch normalization will instead be expressed by modified weights and biases of the preceding convolutional layer.

* When using [Quantization-Aware Training (QAT)](#quantization-aware-training-qat), batchnorm layers <u>are automatically folded</u> during training and no further action is needed.
* When using [Post-Training Quantization](#post-training-quantization), the `batchnormfuser.py` script (see [BatchNorm Fusing](#batchnorm-fusing)) must be called before `quantize.py` to explicitly fuse the batchnorm layers.

*Note: Using batch normalization in conjunction with [dropout](#dropout) can sometimes degrade training results.*

### Adapting Pre-existing Models

In some cases, it may be possible to use generic models that were designed for non-MAX78000/MAX78002 platforms. To adapt pre-existing models to MAX78000/MAX78002, several steps are needed:

1. Check that all operators are supported in hardware (see [List of Predefined Modules](#list-of-predefined-modules), [Dropout](#dropout), and [Batch Normalization](#batch-normalization)).
2. Check that the model size, parameter count, and parameters to the operators are supported (see [Limitations of MAX78000 Networks](#limitations-of-max78000-networks) and [Limitations of MAX78002 Networks](#limitations-of-max78002-networks)). For example, padding must always be zero-padding, and `Conv2d()` supports 1×1 and 3×3 kernels.
3. Change from PyTorch *nn.modules* to the *ai8x* versions of the modules. For example, `nn.Conv2d(…)` ⟶ `ai8x.Conv2d(…)`.
4. Merge modules where possible (for example, `MaxPool2d()` + `Conv2d()` + `ReLU()` = `FusedMaxPoolConv2dReLU()`).
5. [Re-train](#model-training-and-quantization) the model. *This is necessary to correctly model clipping and quantization effects of the hardware.*

### Model Comparison and Feature Attribution

TensorBoard can be used for model comparison and feature attribution.

#### TensorBoard

[TensorBoard](https://www.tensorflow.org/tensorboard/) support is built into `train.py`. When enabled using `--enable-tensorboard`, it provides a local web server that can be started before, during, or after training, and it picks up all data that is written to the `logs/` directory.

For classification models, TensorBoard supports the optional `--param-hist` and `--embedding` command line arguments. `--embedding` randomly selects up to 100 data points from the last batch of each verification epoch. These can be viewed in the “projector” tab in TensorBoard.

`--pr-curves` adds support for displaying precision-recall curves.

To start the TensorBoard server, use a second terminal window:

```shell
(ai8x-training) $ tensorboard --logdir='./logs'
TensorBoard 2.4.1 at http://127.0.0.1:6006/ (Press CTRL+C to quit)
```

On a shared system, add the `--port 0` command line option.

The training progress can be observed by starting TensorBoard and pointing a web browser to the port indicated.

##### Examples

TensorBoard produces graphs and displays metrics that may help optimize the training process, and can compare the performance of multiple training sessions and their settings. Additionally, TensorBoard can show a graphical representation of the model and its parameters, and help discover labeling errors. For more information, please see the [TensorBoard web site](https://www.tensorflow.org/tensorboard/).

<img src="docs/lr.png" alt="learning rate" style="zoom: 50%;" /><img src="docs/top1.png" alt="top-1" style="zoom:50%;" /><img src="docs/objectiveloss.png" alt="objective loss" style="zoom:42%;" /><img src="docs/histogram.png" alt="histogram" style="zoom:50%;" /><img src="docs/model.png" alt="model" style="zoom:50%;" /><img src="docs/projector.png" alt="projector" style="zoom:50%;" />

##### Remote Access to TensorBoard

When using a remote system, use `ssh` in another terminal window to forward the remote port to the local machine:

```shell
$ ssh -L 6006:127.0.0.1:6006 targethost
```

When using PuTTY, port forwarding is achieved as follows:

![putty-forward](docs/putty-forward.jpg)



### BatchNorm Fusing

Batchnorm fusing (see [Batch Normalization](#batch-normalization)) is needed as a separate step <u>only when both</u> the following are true:

1. Batch Normalization is used in the network and
2. [Quantization-Aware Training (QAT)](#quantization-aware-training-qat) is <u>not</u> used (i.e., when [post-training quantization](#post-training-quantization) is active).

In order to perform batchnorm fusing, the `batchnormfuser.py` tool must be run *before* the `quantize.py` script.

*Note: Most of the examples either don’t use batchnorm, so no fusing is needed, or they use QAT, so batchnorm fusing happens automatically.*

#### Command Line Arguments

The following table describes the command line arguments for `batchnormfuser.py`:

| Argument            | Description                                                  | Example                                  |
| ------------------- | ------------------------------------------------------------ | ---------------------------------------- |
| `-i`, `--inp_path`  | Set input checkpoint path                                    | `-i logs/2020.06.05-235316/best.pth.tar` |
| `-o`, `--out_path`  | Set output checkpoint path for saving fused model            | `-o best_without_bn.pth.tar`             |
| `-oa`, `--out_arch` | Set output architecture name (architecture without batchnorm layers) | `-oa ai85simplenet`              |



### Data Folding

*Data Folding* is data reshaping operation. When followed by a Conv2d operation, it is equivalent to a convolution operation on the original image with a larger kernel and a larger stride.

On MAX78000 and MAX78002, data folding is beneficial because it increases available resolution and reduces latency. A typical 3-channel RGB image uses only three processors in the first layer which increases latency, and restricts the image dimensions to what can be fit into the data memories associated with three processors.

By creating many low resolution sub-images and concatenating them through the channel dimension, up to 64 processors and their associated data memories can be used. This results in a higher maximum effective resolution, and increased throughput in the first layer.

For certain models (see `models/ai85net-unet.py` in the training repository) this also improves model performance, due to the increase in effective kernel size and stride.

Note that data folding must be applied during model training. During inference, there is no additional overhead; the input data is simply loaded to different processors/memory addresses.



### Quantization

There are two main approaches to quantization — quantization-aware training and post-training quantization. The MAX78000/MAX78002 support both approaches.

For both approaches, the `quantize.py` software quantizes an existing PyTorch checkpoint file and writes out a new PyTorch checkpoint file that can then be used to evaluate the quality of the quantized network, using the same PyTorch framework used for training. The same new quantized checkpoint file will also be used to feed the [Network Loader](#network-loader-ai8xize).

#### Quantization-Aware Training (QAT)

Quantization-aware training is the better performing approach. It is enabled by default. QAT learns additional parameters during training that help with quantization (see [Weights and Activations: Quantization-Aware Training (QAT)](#weights-and-activations-quantization-aware-training-qat). No additional arguments (other than input, output, and device) are needed for `quantize.py`.

The input checkpoint to `quantize.py` is either `qat_best.pth.tar`, the best QAT epoch’s checkpoint, or `qat_checkpoint.pth.tar`, the final QAT epoch’s checkpoint.

Example:

```shell
(ai8x-synthesis) $ python quantize.py proj/qat_best.pth.tar proj/proj_q8.pth.tar --device MAX78000
```



#### Post-Training Quantization

This approach is also called *”naive quantization”*. It should be used when `--qat-policy None` is specified for training.

While several approaches for clipping are implemented in `quantize.py`, clipping with a simple fixed scale factor performs best, based on experimental results. The approach requires the clamping operators implemented in `ai8x.py`.

Note that the “optimum” scale factor for simple clipping is highly dependent on the model and weight data. For the MNIST example, a `--scale 0.85` works well. For the CIFAR-100 example on the other hand, Top-1 performance is 30 points better with `--scale 1.0`.

The input checkpoint to `quantize.py` for post-training quantization is typically `best.pth.tar`, the best epoch’s checkpoint, or `checkpoint.pth.tar`, the final epoch’s checkpoint.

Example:

```shell
(ai8x-synthesis) $ python quantize.py proj2/best.pth.tar proj2/proj2_q8.pth.tar \
--device MAX78000 --scale 0.85 --clip-method SCALE
```



#### Command Line Arguments

The `quantize.py` software has the following important command line arguments:

| Argument              | Description                                                  | Example 