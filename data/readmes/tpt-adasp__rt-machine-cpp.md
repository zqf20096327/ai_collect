# rt-machine-cpp
`rt-machine-cpp` is a C++20 framework designed to build real-time audio machine-learning research prototypes.

It provides several building blocks:
 - Synchronous/asynchronous/remote processing
 - Pre/Post processing: STFT / Log-Mel & custom filters banks
 - Deep-learning inference: Onnxruntime / Executorch / Tensorflow Lite
 - Ability to add custom processing


To understand how to use the library please refer to the documentation section

## Deprecation notice
This code was open sourced because there will not be anyone at ADASP able to maintain this code anymore.

---
__*Before cloning :*__
This repository makes use of `git-lfs` to store large file objects (like models or wav files). Make sure you have git-lfs installed when cloning or
you might have some files missing (mostly for tests).

*On ubuntu you can install it by running* `apt-get install git-lfs`

# Build
This library is intended to be cross platform, so some information are platform
related. Therefore the following is divided between common needs / platform needs

---
This library uses CMake for cross-platform compiling. Please be aware CMake cache
most of the parameters you give it. That's why we don't give a value for every
single parameter on every section.

## Prerequisites [Common]
 - `cmake` >= 3.28
 - `clang-tidy` and `clang-format` for C++ linting/formating
 - `cmake-format` for cmake formatting
 - `python==3.10` for some dependencies
 - `ninja-build` (or you can use Make, but it's slower and VSCode natively uses ninja)
 - `mdm` to get ncpus
 - `jq` for JSON parsing

On Ubuntu 24.04 the setup should be :
```
sudo apt-get install -y ninja-build build-essential clang-tidy clang-format clangd mdm jq
conda install -c conda-forge onednn=3.7.2 cmake-format "cmake~=3.31"
```

**Check the [wiki page](https://gitlab.telecom-paris.fr/audible/protected/dev/general-documentation/-/wikis/C/C++-Setup)
for more up-to-date information about clang-tidy and clang-format setup**

To install the python packages needed for the build you can use the [requirements-public.txt](./requirements-public.txt) file.

If the python packages are not already installed, at configure time, CMake might 
try to install several python packages, depending on
the build options. To prevent installing these packages on your native environment,
cmake will detect if you run in a Python virtual env (conda/venv/virtualenv...).
If not you will need to add the `-D RTM_ENABLE_PYTHON_NATIVE_ENV=ON` option to
force the installation.

### Prerequisite [x86_64]
 - g++

### Prerequisite [arm64-v8a]
 - the GNU toolchain 10.2, installed under `/usr/local/aarch64-none-linux-gnu`

Use the given script to install it to the proper location
```shell
# Install the GNU toolchain 10.2 under /usr/local/aarch64-none-linux-gnu
sudo ./scripts/install_aarch64_gnu_toolchain.sh
```

### Prerequisite [Android arm64-v8a]
You'll need the Android NDK>=27.2.12479018. You can install it using the provided
script :
```bash
# you'll need your sudo passwd
./scripts/install_android_toolchain.sh
```

It will install it under `~/Android/Sdk`.  
The Android cli tools (like `adb`) must be reachable in the PATH.

## Build with CMake
Several command are provided to help build the library, but this library is 
designed to use VSCode CMake integration to build within VSCode.

### CMake configuration [Common]
 - `CMAKE_TOOLCHAIN_FILE` : the toolchain file for the build
 - `RTM_ENABLE_FLOAT` : Enable single floating-point support, default to ON
 - `RTM_ENABLE_DOUBLE` : Enable double floating-point support, default to ON
 - `RTM_ENABLE_ARM_BF16` : On ARM64, enables bf16 support, default to OFF
 - `RTM_ENABLE_ORT` : Enable ONNX runtime inference engine
 - `RTM_ENABLE_TFLITE` : Enable TFLite inference engine
 - `RTM_ENABLE_EXECUTORCH` : Enable EXECUTORCH inference engine
 - `RTM_ENABLE_FFTW` : Enable the fftw backend (fp64)
 - `RTM_ENABLE_FFTWF` : Enable the fftw backend (fp32)
 - `RTM_BUILD_TESTING` : Enable the build of the testing binaries, see [testing](#testing_c)
 - `RTM_BUILD_DOCS` : Enable the build of the documentation, default to OFF. See [documentation](#documentation_c)
 - `RTM_USE_ASAN` : (Debug option) Enable the use of ASAN for all the source code, default to OFF.
 - `RTM_VERBOSE_INIT_CHECK` : (Debug option) Enable stdout logging of failed INIT_CHECK, default to OFF
 - `RTM_USE_TRACY` : (Debug option) Enable the Tracy profiling system, see the wiki for how to setup.

### CMake configuration [x86_64]
To build for x86_64 on a x86_64 linux machine, the `CMAKE_TOOLCHAIN_FILE` is the
the only parameter needed

On the command line run :
```shell
cmake -D CMAKE_BUILD_TYPE:STRING=Release -D CMAKE_TOOLCHAIN_FILE:FILEPATH=x86_64-Toolchain.cmake -B build -G Ninja .
cmake --build build --config Release --target all
```

If using VSCode and the provided `cmake-kits.json`, simply select the kit `x86_64-GCC`

### CMake configuration [arm64]
To build for x86_64 on a x86_64 linux machine, the `CMAKE_TOOLCHAIN_FILE` is the
the only parameter needed

We provide two toolchain files :
 - `aarch64-rpi0_2W-Toolchain.cmake` : optimized for a rpi zero 2W cpu
 - `aarch64-rpi4-Toolchain.cmake` : optimized for a rpi4 cpu

On the command line run :
```shell
cmake -D CMAKE_BUILD_TYPE:STRING=Release -D CMAKE_TOOLCHAIN_FILE:FILEPATH=<Toolchain_file> -B build -G Ninja .
cmake --build build --config Release --target all
```

If using VSCode and the provided `cmake-kits.json`, simply select one of the kits : 
 - `rpi4-GNU`
 - `rpi0_2W-GNU`

### CMake configuration [Android arm64]
To build for Android arm64, you need to specify a few more parameters :
 - `CMAKE_TOOLCHAIN_FILE` : the path of the NDK toolchain, should look like `~/Android/Sdk/ndk/<ndk_ver>/build/cmake/android.toolchain.cmake`
 - `ANDROID_ABI=arm64-v8a`
 - `ANDROID_SDK_PATH` : the path to the Android SDK folder
 - `ANDROID_NDK_PATH` : the path to the Android NDK folder
 - `ANDROID_PLATFORM`: the version of the Android API you're building for. 30 is suggested (Android 11)

If you installed the Android SDK and NDK as default (in your home folder), I
strongly suggest using the VSCode CMake integration, and select the kit `Android armv8`
from the provided `cmake-kits.json`.

If you wish to build from the command line, run :
```
cmake -D CMAKE_BUILD_TYPE:STRING=Release -D CMAKE_TOOLCHAIN_FILE:FILEPATH=<path_to_android_toolchain> -B build -G Ninja -D ANDROID_ABI=arm64-v8a -D ANDROID_SDK_PATH=<path_to_android_sdk> -D ANDROID_NDK_PATH=<path_to_android_ndk> -D ANDROID_PLATFORM=30 .
cmake --build build --config Release --target all
```

### CMake configuration [iOS arm64]
The project was built and tested for iOS `16.1`

To build for iOS arm64, you need to specify a few mores parameters:
 - `CMAKE_TOOLCHAIN_FILE`: the path of the toolchain to use, we provided [one](./arm64-ios-Toolchain.cmake)
 - `CMAKE_GENERATOR`: `XCode` if you wanna build with XCode (recommended)
 - `PLATFORM`: `OS64` or `SIMULATORARM64` depending on if you wanna build for the iPhone or the simulator
 - `APPLE_SYSROOT`: `iphoneos` or `iphonesimulator` depending on if you wanna build for the iPhone or the simulator
 - `RTM_ENABLE_TFLITE`: `OFF` Tensorflow Lite support is not implemented for iOS
 - `RTM_ENABLE_EXECUTORCH`: `OFF` Executorch support is not implemented for iOS


If you used VSCode we suggest using the provided cmake kits: `iOS arm64`/`iOS simulator arm64`

After configuring, you can build through Xcode by opening `rt-machine-cpp.xcodeproj` that is generated in the build folder.


# Testing [Common]
<a name="testing_c">
</a>

To test the library you can either use the VSCode integrated option `CMake: Run Tests` or
build and run the tests on the command line

```shell
cmake --build build --config Release --target test
cd build && ctest -j$(ncpus)
```

## Testing [Arm64]
To enable testing the aarch64 binaries on your host amd64 machine, the Toolchain files are preconfigured to call `qemu-aarch64-static` to emulate an aarch64 cpu.

Make sure you have the `qemu-aarch64-static` binary in your path.
On Ubuntu you can install it using :
```shell
apt-get install -y qemu-user-static
```

Then you can run the tests as in the `[Common]` case

## Testing [Android]
To run the test for android generated code, you need to connect an Android device
of the target architecture. Make sure the device is available by running
`adb devices`.

The result should look like this :
```
List of devices attached
2ba10dab        device
```

Once the device is connected, you should be able to run the tests in the same way
as the common case. The `scripts/run_on_android_emulator` script will copy test data and
executable to the target and run it for you.

## Testing [iOS]
In order to run the tests, you can make use of Xcode for both physical and simulators after configuring and building using the corresponding cmake kit described in the `Build` section above. You might need a signing certificate to run the tests on a physical phone.


# Documentation
<a name="documentation_c">
</a>

This project use `Doxygen` documentation style and `breathe` to translate it into
Sphinx documentation. The build of documentation is not enabled by default.

## Prerequisite
```
apt-get install -y doxygen
```

## Build and install the doc
```
cmake -D RTM_BUILD_DOCS=ON -B build .
cmake --build build --target sphinx
cmake --install build --prefix install
```

The documentation can then be found under `install/share/doc/rt-machine-cpp/sphinx`

# Real-time safety
Even though RT stands for real-time and this project is tested using [rtsan](https://clang.llvm.org/docs/RealtimeSanitizer.html), some portions of the projects are not real-time safe.

For the tests to pass **some sections were on purposed marked as unsafe**. These will
not trigger the sanitizer. To find the unsafe section search for the `REALTIME_IGNORE` macro.

The goal is to have a code as safe as possible, but some backends are not.
They have nonetheless been internally used extensively as for most of ***our*** implementations
the jitter introduced by these real-time violation where not enough to break our deadlines.

## FFT backends
- `stft_fftw` is not real-time safe
- `stft_signalsmith` **is real-time safe**

## Inference backends
- `inference_onnxruntime` is not real-time safe
- `inference_tflite` is not real-time safe
- `inference_executorch` **is real-time safe**


# Misc
## Code style & VSCode integration
This repository provides both `.clang-tidy` and `clang-format` for automatic
linting and additionnal static analysis of the C++ code and `pylintrc` for Python code.

I highly suggest using the following extensions on VSCode :
 - [Basic C/C++ support](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
 - [Clang Format](https://marketplace.visualstudio.com/items?itemName=xaver.clang-format)
 - [CMake support](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
 - [CMake Format](https://marketplace.visualstudio.com/items?itemName=cheshirekow.cmake-format)
 - [Native debugger for cross and remote debugging](https://marketplace.visualstudio.com/items?itemName=webfreak.debug)
 - [Doxygen Documentation Generator](https://marketplace.visualstudio.com/items?itemName=cschlosser.doxdocgen)
 - [ShellCheck](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck)
 - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

This repository also provides a `cmake-kits.json` file to help configure CMake
for VSCode.

## Troubleshooting
Don't forget to check the wiki pages when encountering an issue. If not available
don't hesitate to add a new page for troubleshooting

### Executorch
Sometimes when configuring CMake with Executorch enabled, you see the following error:
```
[cmake] Error while generating /home/user/work/rt-machine-cpp/build/_deps/executorch-build/executorch_srcs.cmake. Exit code: 1
[cmake] Output:
[cmake] 
[cmake] Error:
[cmake] Traceback (most recent call last):
[cmake]   File "/home/user/work/rt-machine-cpp/build/executorch/build/buck_util.py", line 26, in run
[cmake]     cp: subprocess.CompletedProcess = subprocess.run(
[cmake]   File "/home/user/miniconda3/envs/rt-machine-cpp-dev/lib/python3.10/subprocess.py", line 526, in run
[cmake]     raise CalledProcessError(retcode, process.args,
[cmake] subprocess.CalledProcessError: Command '['/home/user/work/rt-machine-cpp/build/executorch/buck2-bin/buck2-3bbde7daa94987db468d021ad625bc93dc62ba7fcb16945cb09b64aab077f284', 'cquery', "inputs(deps('//runtime/executor:program'))"]' returned non-zero exit status 2.
[cmake] 
[cmake] The above exception was the direct cause of the following exception:
[cmake] 
[cmake] Traceback (most recent call last):
[cmake]   File "/home/user/work/rt-machine-cpp/build/executorch/build/extract_sources.py", line 232, in <module>
[cmake]     main()
[cmake]   File "/home/user/work/rt-machine-cpp/build/executorch/build/extract_sources.py", line 217, in main
[cmake]     target_to_srcs[name] = sorted(target.get_sources(graph, runner, buck_args))
[cmake]   File "/home/user/work/rt-machine-cpp/build/executorch/build/extract_sources.py", line 121, in get_sources
[cmake]     sources: set[str] = set(runner.run(["cquery", query] + buck_args))
[cmake]   File "/home/user/work/rt-machine-cpp/build/executorch/build/buck_util.py", line 31, in run
[cmake]     raise RuntimeError(ex.stderr.decode("utf-8")) from ex
[cmake] RuntimeError: Command failed: 
[cmake] Error validating working directory
[cmake] 
[cmake] Caused by:
[cmake]     0: Failed to stat `/home/user/work/rt-machine-cpp/build/executorch/buck-out/v2`
[cmake]     1: ENOENT: No such file or directory
```

This is a [known issue](https://github.com/pytorch/executorch/issues/4439) and
it's not looking like it's going to be fixed soon.

To solve it run the following command, using the `buck2` utility downloaded by
executorch at configure time :
```bash
cd build/executorch/buck2-bin  && ./buck2-* clean
```