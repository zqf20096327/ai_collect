# DPVI-SLAM

> Monocular visual-inertial SLAM with deep patch tracking and loop closure

A modified version of [DPV-SLAM](https://github.com/princeton-vl/DPVO) that uses the IMU backend of [DEIO](https://github.com/arclab-hku/DEIO) to estimate metric-scale trajectories.

<p align="center">
  <img src="assets/dpvi_slam_mh01.gif" width="720"><br>
  <sub><a href="https://projects.asl.ethz.ch/datasets/euroc-mav/">EuRoC</a> MH_01, with loop detection deferred to the end of the sequence.</sub>
</p>

## Installation

Tested on Ubuntu 22.04 with Python 3.11, PyTorch 2.3.1 and CUDA 11.8.

```bash
git clone --recursive https://github.com/Leeseunghun03/DPVI-SLAM.git
cd DPVI-SLAM
conda env create -f environment.yml
conda activate dpvi

wget https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.zip
unzip eigen-3.4.0.zip -d thirdparty

pip install --no-build-isolation .
```

GTSAM is modified to extend its Python wrapper, so install it from `thirdparty/gtsam`:

```bash
cd thirdparty/gtsam
mkdir build && cd build
cmake .. -DGTSAM_BUILD_PYTHON=ON -DGTSAM_PYTHON_VERSION=3.11 \
    -DGTSAM_BUILD_TESTS=OFF -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
    -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX
make -j4
make install
make python-install
cd ../../..
```

Download the DPVO weights ([models.zip](https://drive.google.com/file/d/1dRqftpImtHbbIPNBIseCv9EvrlHEnjhX/view?usp=sharing)) and place `dpvo.pth` in the repository root.

### Classic loop closure (optional)

Requires the OpenCV C++ library (`libopencv-dev` on Ubuntu).

```bash
cd DBoW2
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX
make -j4
make install
cd ../..

pip install ./DPRetrieval
```

ORB vocabulary from [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3):

```bash
wget https://github.com/UZ-SLAMLab/ORB_SLAM3/raw/master/Vocabulary/ORBvoc.txt.tar.gz
tar -xzf ORBvoc.txt.tar.gz
```

### Viewer (optional)

Pangolin needs the packages listed in `Pangolin/scripts/install_prerequisites.sh`.

```bash
cd Pangolin
mkdir build && cd build
cmake .. -DBUILD_PANGOLIN_PYTHON=OFF -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX
make -j4
make install
cd ../..

pip install --no-build-isolation ./DPViewer
```

Pass `--viz` to open the viewer.

## EuRoC

Download the sequences in ASL format and place them as `<eurocdir>/<scene>/mav0`.

```bash
python evaluate_euroc.py --eurocdir <eurocdir> --scenes MH_01_easy --plot --save_trajectory
```

Use `--opts ENABLE_IMU False` for monocular DPV-SLAM. `demo.py` works as in DPVO.

## Other datasets

Copy `config/euroc.yaml` and set

| Key | |
|---|---|
| `T_BC` | camera-to-body (IMU) transform, row-major 4x4 |
| `ACC_NOISE`, `GYR_NOISE` | white noise densities |
| `ACC_BIAS_NOISE`, `GYR_BIAS_NOISE` | bias random walk densities |
| `GRAVITY` | local gravity magnitude |

Images must be undistorted, and H and W multiples of 16. Timestamps are in seconds.

```python
import torch
from dpvo.config import cfg
from dpvo.dpvo import DPVO

cfg.merge_from_file("config/my_dataset.yaml")
slam = DPVO(cfg, "dpvo.pth", ht=H, wd=W)
slam.set_imu(imu)  # (N, 7): t, wx, wy, wz, ax, ay, az  [s, rad/s, m/s^2]
with torch.no_grad():
    for t, image, intrinsics in stream:  # image: (3, H, W) uint8 BGR CUDA tensor, intrinsics: fx, fy, cx, cy
        slam(t, image, intrinsics)
    poses, tstamps = slam.terminate()
```

## Acknowledgements

The GTSAM extensions in `thirdparty/gtsam` come from [DBA-Fusion](https://github.com/GREAT-WHU/DBA-Fusion) and [DM-VIO](https://github.com/lukasvst/dm-vio).

## References

```bibtex
@article{teed2023deep,
  title={Deep Patch Visual Odometry},
  author={Teed, Zachary and Lipson, Lahav and Deng, Jia},
  journal={Advances in Neural Information Processing Systems},
  year={2023}
}

@inproceedings{lipson2024deep,
  title={Deep Patch Visual SLAM},
  author={Lipson, Lahav and Teed, Zachary and Deng, Jia},
  booktitle={European Conference on Computer Vision},
  year={2024}
}

@inproceedings{guan2025deio,
  title={{DEIO}: Deep Event Inertial Odometry},
  author={Guan, Weipeng and Lin, Fuling and Chen, Peiyu and Lu, Peng},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops},
  pages={4665--4674},
  year={2025}
}
```

## License

DPVI-SLAM is released under GPLv3, as it includes GPL code from DBA-Fusion, DM-VIO and evo.
Third-party licenses are listed in [THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES).
