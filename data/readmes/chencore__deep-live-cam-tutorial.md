# Deep-Live-Cam 完整安装与使用教程

> 实时 AI 换脸工具，一张图片即可实现直播/视频换脸

## 这是什么？

Deep-Live-Cam 是一个开源的实时人脸替换工具。

**核心能力：**
- 一张图片就能换脸
- 实时处理，延迟极低
- 支持直播、视频、摄像头
- 本地运行，隐私安全

**效果演示：**
- 直播换脸
- 视频会议虚拟形象
- 电影实时换演员
- 制作梗图/短视频

---

## 系统要求

### 最低配置
- **GPU:** NVIDIA 2060/3060 或更高（6GB 显存）
- **或者:** AMD GPU 6GB 显存 / Apple Silicon M1/M2/M3
- **CPU:** 也能跑，但慢（约 2-5 FPS）
- **内存:** 16GB 推荐
- **硬盘:** 2GB 以上（模型 + 依赖）

### 推荐配置
- NVIDIA 3080/4080 或更高（12GB+ 显存）
- 32GB 内存
- 可达 15-20 FPS

---

## 安装方法

### 方法一：Quickstart 版本（新手推荐）

适合：不想折腾的技术小白

**优点：**
- 解压即用
- 不需要配置环境
- 预装所有依赖

**缺点：**
- 需要付费订阅
- 更新不如 GitHub 版及时

**获取地址：**
deeplivecam.net/index.php/quickstart

---

### 方法二：GitHub 源码安装（免费）

适合：有技术基础的用户

#### Windows 安装

**1. 安装前置依赖**

```bash
# 安装 Python 3.11
# 下载地址：python.org/downloads

# 安装 Git
# 下载地址：git-scm.com/download/win

# 安装 ffmpeg
# 方法一：winget install ffmpeg
# 方法二：从 ffmpeg.org 下载，添加到 PATH

# 安装 Visual Studio 2022 Runtime
# 下载地址：visualstudio.microsoft.com/visual-cpp-build-tools/
```

**2. 克隆项目**

```bash
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
```

**3. 下载模型文件**

从 HuggingFace 下载：
- [GFPGANv1.4.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.onnx)
- [inswapper_128_fp16.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx)

放到 `models/` 文件夹

**4. 创建虚拟环境**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**5. GPU 加速（NVIDIA）**

```bash
# 安装 CUDA Toolkit 12.8
# 下载地址：developer.nvidia.com/cuda-12-8-0-download-archive

# 安装 cuDNN v8.9.7
# 下载地址：developer.nvidia.com/rdp/cudnn-archive

# 安装 PyTorch + onnxruntime-gpu
pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.21.0
```

**6. 运行**

```bash
python run.py --execution-provider cuda
```

---

#### macOS 安装（Apple Silicon）

**1. 安装依赖**

```bash
# 安装 Python 3.11（必须是这个版本）
brew install python@3.11

# 安装 tkinter
brew install python-tk@3.10
```

**2. 克隆项目**

```bash
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
```

**3. 创建虚拟环境**

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**4. 安装 CoreML 支持**

```bash
pip uninstall onnxruntime onnxruntime-silicon
pip install onnxruntime-silicon==1.13.1
```

**5. 下载模型**

同 Windows，放到 `models/` 文件夹

**6. 运行**

```bash
python3.10 run.py --execution-provider coreml
```

⚠️ **注意：** macOS 必须用 `python3.10` 命令，不是 `python`

---

#### Linux 安装

```bash
# 安装系统依赖
sudo apt update
sudo apt install python3.10 python3-pip git ffmpeg

# 克隆项目
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 下载模型到 models/ 文件夹
# ...

# CPU 运行
python run.py

# GPU 运行（需要 CUDA）
python run.py --execution-provider cuda
```

---

## 使用方法

### 基本操作

**1. 启动程序**

```bash
python run.py --execution-provider cuda
```

**2. 打开界面**

浏览器会自动打开 `http://localhost:8080`

**3. 三个步骤**

1. **选择脸** - 上传一张正面清晰的照片
2. **选择摄像头** - 选择你的 webcam
3. **点击 Live** - 开始实时换脸

### 参数说明

```bash
# 基本运行
python run.py

# 指定执行设备
python run.py --execution-provider cuda      # NVIDIA GPU
python run.py --execution-provider coreml    # Apple Silicon
python run.py --execution-provider cpu       # 纯 CPU

# 指定端口
python run.py --port 8888

# 处理视频文件
python run.py --target video.mp4 --source face.jpg -o output.mp4
```

### 高级功能

**Mouth Mask（嘴巴遮罩）**
- 保留原始嘴部动作
- 让表情更自然

**Many Faces（多人换脸）**
- 同时处理多个人脸
- 每个人可以用不同的脸

**Face Enhancer（面部增强）**
- 使用 GFPGAN 提升面部质量
- 修复模糊/噪点

---

## 常见问题

### Q: 运行报错 "No module named '_tkinter'"

macOS 解决：
```bash
brew reinstall python-tk@3.10
```

### Q: 模型加载失败

检查：
1. 模型文件是否在 `models/` 文件夹
2. 文件名是否正确（区分大小写）
3. 文件是否完整（重新下载）

### Q: FPS 很低

可能原因：
1. 没用 GPU（检查 CUDA 是否安装正确）
2. 显存不足（降低分辨率）
3. CPU 性能不够

### Q: 换脸效果不好

建议：
1. 使用高质量、正面的源照片
2. 光线充足
3. 开启 Face Enhancer

### Q: 提示内容违规

工具内置审核，会拒绝处理：
- 裸露内容
- 暴力画面
- 敏感素材

---

## 道德与法律

⚠️ **重要提醒：**

**合法使用：**
- 使用他人脸需要获得同意
- 发布内容要标注是 deepfake
- 不要用于欺诈、骚扰、诽谤

**工具限制：**
- 内置内容审核
- 可能添加水印
- 违规可能导致项目关闭

**你的责任：**
- 使用者需遵守当地法律
- 开发者不对用户行为负责

---

## 性能参考

| 配置 | FPS |
|------|-----|
| i9 + RTX 4090 (24GB) | 20+ |
| i7 + RTX 3080 (10GB) | 12-15 |
| i5 + RTX 3060 (6GB) | 8-10 |
| Apple M2 Max | 10-12 |
| Apple M1 | 6-8 |
| 纯 CPU | 2-5 |

---

## 相关链接

- **GitHub:** github.com/hacksider/Deep-Live-Cam
- **官网:** deeplivecam.net
- **模型下载:** huggingface.co/hacksider/deep-live-cam
- **Discord:** 社区支持

---

## 更新日志

- 2026-04: 支持多人同时换脸
- 2026-03: 添加嘴巴遮罩功能
- 2026-02: CoreML 支持 Apple Silicon

---

> 最后更新：2026-04-04
> 
> 教程作者：[你的名字]
> 
> 原文链接：[待补充]
