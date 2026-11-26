# XCcv 多功能视觉平台（XCcv Multi-functional Platform）

[![CI](https://github.com/Arbhh/XCcv_Multi-functional-Platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Arbhh/XCcv_Multi-functional-Platform/actions/workflows/ci.yml)

中文 | [English](README_EN.md)

XCcv 是一个面向工业视觉场景的**离线桌面端**多功能深度学习视觉平台，全量开源。
覆盖 **数据标注 → 模型训练 → 测试评估 → 部署推理服务** 全流程，并附 **模型工具**
（结构化剪枝 / TensorRT 加速）、**流程图编排**（57 个内置算子）与 **缺陷样本合成** 工具。
零基础用户通过桌面 UI 即可完成一个视觉模型从数据到权重再到产线服务的完整落地，
全程本地运行、数据不出内网。
界面支持**中文 / English 一键切换**（主界面「设置」中切换，全平台同步生效）。

![XCcv 主界面（AI 平台）](docs/images/main.png)

> 主界面：标注 → 训练 → 测试 → 部署 四步完成模型落地；左侧导航进入传统平台、
> 流程图与部署平台，卡片含模型工具与推理服务状态胶囊。

## 功能总览

| 模块 | 能力 |
|---|---|
| 标注平台 | 集成 labelme 标注器：矩形 / 多边形、自动保存、类别体系管理；**AI 智能标注**（S 键智能多边形、B 键画笔塑形、L 键单张智能标注、目录批量预标注，基于 SAM / EfficientSAM）；OK/良品目录徽标、标注质量要点、AI 复核疑似漏标 |
| 训练平台 | 项目制管理；**五类任务 14 种内置模型**（分类 / 检测 / 分割 / 无监督与少样本异常检测 PatchCore、CIF、SubspaceAD / OCR CRNN，含 ResNet / MobileNetV3 / YOLO11 / Faster R-CNN / Mask R-CNN）；快速配置与专家模式双轨参数；工业优化（CBAM/ECA、DCNv2、Focal 系损失等）；训练加速（冻结骨干、AMP、TF32、早停、灰度、确定性复现）；P2 小目标头、负样本训练、切图训练；逐类指标表、数据网格、划分环形图随参数实时重绘、图像增强全算子实时预览、Loss 判读、run_manifest、数据体检、多训练对比 |
| 测试平台 | 单图 / 批量推理；置信度与 IOU 阈值实时调节；类别筛选；4K 大图分块推理；结果导出为统一 JSON / labelme / COCO；**标准 / 项目复盘双页**（自动对训练集批量；复盘页**已评估 / 未评估解耦**——已评估按 正确 / 漏检 / 过检 三组，未评估生产图按 OK / NG 两组）、维度阈值拖线与键入（置信度/面积/短边/长边/灰度差，扫描曲线给出阈值处各分组的图数、与右侧分组同口径，切换范围曲线随之换口径）、复判回流、模型 A/B 比对（比对结果缓存复用 + 总体优劣比例条）、推理耗时/显存统计；分数语义随模型声明（置信度 / 分类概率 / 图像分数 z） |
| 部署平台 | **HTTP 推理服务**（FastAPI）：模型/流程加载为常驻 API、单帧与批量推理、叠加图渲染、WebSocket 二进制流推理、耗时分段打点（`X-XCcv-Timing` 响应头）；API Key 认证、并发准入、模型路径白名单、自托管离线 Swagger 文档；**模型加载**窗口与 **C# 测试** Demo（`service/csharp` 单文件 SDK + WinForms 演示，系统 csc 直接编译）；一键一致性自检（本地推理 vs 服务推理逐框比对） |
| 模型工具 | **结构化通道剪枝**（Torch-Pruning DepGraph；训练前预剪枝供迁移学习 / 训练后剪枝，独立子进程 + 内存水位看门狗 + 紧急终止）；**TensorRT 引擎导出**（YOLO 走 ultralytics 原生路径；分类走内存 ONNX→TRT；Mask R-CNN 特征段加速，跨显卡算力预检与友好降级） |
| 流程图 | 与 AI 平台同级的独立模块：内置 **57 个 AI 与通用算子**（模型推理 / 传统视觉算子：斑点分析、模板匹配、找线找圆、测量定位 / 检出过滤 / 裁图与合并 / 逻辑判定 / 外部算子插件后端 / 输出）；Web 画布拖拽编排，节点库分「AI 算子 / 传统算子」；支持运行预览、保存 JSON、打包 / 解包 `.xvap`、批量运行；附 9 个模板（AI 过滤、级联裁图合并、检测→分割级联、模板匹配预筛等） |
| 缺陷样本合成 | 把缺陷贴图以泊松融合自然合成到良品图上，扩充稀缺缺陷样本（独立进程，内嵌 Web 界面） |
| 界面语言 | **中文 / English 一键切换**：主界面「设置」对话框切换后全平台自动生效；常驻界面文案与高频消息同步翻译（详见 [README_EN](README_EN.md)） |

> 流程图模块支持 AI 与传统视觉算子的可视化编排（66 个节点 / 9 个模板），覆盖模型推理、
> 传统视觉定位测量、检出过滤、裁图合并、逻辑判定与结果输出等常用产线链路。

## 环境要求

- Windows 10 / 11（x64）
- Python 3.11（建议使用独立虚拟环境）
- GPU：可选。NVIDIA 显卡可显著加速训练与推理；CPU 亦可运行（推荐配合小模型）
- 磁盘：依赖（PyTorch 等）约需 6~8 GB 空间
- 可选：TensorRT 运行库（模型加速 / `.engine` 推理需要；`pip install tensorrt`，
  或设置环境变量 `TENSORRT_DIR` 指向含 `nvinfer_10.dll` 的目录）

## 安装

```bat
:: 1) 创建并激活虚拟环境（Python 3.11）
python -m venv venv
venv\Scripts\activate

:: 2) 安装 PyTorch（按官方源选择 CUDA / CPU 版本，示例为 CUDA 12.8）
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

:: 3) 安装其余依赖
pip install -r requirements.txt
```

## 快速开始

> **启动环境（重要）**：主界面、流程画布、缺陷样本合成都依赖 PyQtWebEngine。
> `run_*.bat` 为纯 ASCII 脚本，**不要求本目录存在 venv**，按下列优先级逐个实测
> （唯一的判据是能否 `import PyQt5.QtWebEngineWidgets`）：
>
> 1. `XCCV_PY` 环境变量；
> 2. 本目录 `python_path.txt`（一行：指向 python.exe 的完整路径）；
> 3. PATH 中的 `python`；
> 4. `py` 启动器（`py -3`）；
> 5. 本目录 `venv` / `.venv`（可选兜底）。
>
> 全部不可用时输出英文指引，并调用 `tools\env_check.py` 打印中文诊断（列出每个候选
> 是否可用及失败原因）。推荐在目标机器上写一行 `python_path.txt`，例如：
> `<项目目录>\venv\Scripts\python.exe`（该文件已加入 .gitignore，每台机器可不同）。

双击 `run_main.bat`（或 `python -m xccv.app`）打开主界面，按卡片进入各平台：

1. **标注**：新建项目 → 导入图片 → 绘制矩形 / 多边形（可选按 S 使用 AI 智能多边形）；
2. **训练**：选择项目与模型（分类 / 检测 / 分割 / 异常检测 / OCR）→ 快速配置或专家模式 → 开始训练，实时查看曲线与逐类指标；
3. **测试**：加载项目最新模型（best.pt）→ 单图 / 批量推理 → 标准页看结果，或切「项目复盘」页：
   先「已评估」按 正确 / 漏检 / 过检 调阈值，再切「未评估」看生产图 OK / NG；支持复判回流与 A/B 比对；
4. **部署平台**（左侧导航同级模块）：启动 HTTP 推理服务 → 加载模型/流程为常驻 API →
   单帧 / 批量 / WebSocket 推理；C# 测试卡片一键编译运行 WinForms Demo；
5. **流程图**（左侧导航同级模块）：选择数据路径与流程 JSON →「运行流程」看单图结果，
   或「编辑流程」在画布中拖拽 AI / 传统算子编排，支持打包为 `.xvap` 与批量运行；
6. **模型工具**：训练前/后剪枝生成轻量模型；把 best.pt 导出为 TensorRT 引擎（.engine）提速产线推理；
7. **缺陷样本合成**（可选）：主界面卡片进入，合成缺陷样本扩充训练集；
8. **界面语言**：主界面「设置」→「界面语言」选 English，保存后全平台窗口自动切换。

命令行入口（等价于主界面卡片）：

```bat
run_annotation.bat   :: 标注平台
run_training.bat     :: 训练平台
run_testing.bat      :: 测试平台
run_flow.bat         :: 流程图（独立窗口；主界面左侧导航亦可进入）
run_modeltools.bat   :: 模型工具（剪枝 / TensorRT 加速）
run_deploy.bat       :: 部署平台（推理服务 / 模型加载 / C# 测试）
run_service.bat      :: 推理服务（无界面服务进程）
run_defectgen.bat    :: 缺陷样本合成
```

推理服务也可直接以命令行启动：`python -m xccv.service.main --host 127.0.0.1 --port 8600`
（首次启动自动生成 API Key，保存在 `platform_data/service/config.json`；接口文档见
`http://127.0.0.1:8600/docs`）。C# Demo：`xccv\service\csharp\build_demo.bat` 一键编译
（使用系统自带 .NET Framework csc，无第三方依赖）。

详细上手文档见 [docs/quickstart.md](docs/quickstart.md)（English: [docs/quickstart_EN.md](docs/quickstart_EN.md)）。

**文档索引**：项目简介见 [docs/XCcv多功能视觉平台_项目简介.docx](docs/XCcv多功能视觉平台_项目简介.docx)
（English: [docs/XCcv多功能视觉平台_项目简介_EN.docx](docs/XCcv多功能视觉平台_项目简介_EN.docx)）；
安装环境、权重获取、标注、训练、部署与 0.7.x 迁移等问题见
[docs/FAQ.md](docs/FAQ.md)（English: [docs/FAQ_EN.md](docs/FAQ_EN.md)）。

### 可选：权重与示例数据（均不随仓库分发）

> **本仓库不分发任何模型权重与示例数据**。权重按各自发布方许可由使用者自行获取；
> 示例数据以独立数据包分发。仓库与源码包内只有代码、文档与界面图标。

| 资源 | 获取方式 | 放置位置 |
|---|---|---|
| SAM 系列（AI 智能标注） | 官方渠道自取（如 `sam2.1_t.pt`、`mobile_sam.pt`），遵循发布方许可 | `weights/sam/` |
| DINO ViT-B/8（CIF） | 官方渠道自取 | `weights/dino/`（或环境变量 `XCCV_DINO_CKPT`） |
| DINOv2（SubspaceAD） | 官方渠道自取；国内网络可设 `HF_ENDPOINT=https://hf-mirror.com` | `weights/dinov2/`（或 `XCCV_DINOV2_CKPT`） |
| YOLO COCO / torchvision 基准权重 | `python xccv/engine/weights/download_weights.py` 一键下载（仅本机） | `xccv/engine/weights/` |
| 缺陷合成示例数据（约 33 MB） | 下载 `XCcv-Platform-testdata-0.8.0.zip` | 解压到 `xccv/defectgen/`（得到 `testdata/`） |
| maskrcnn18 slim 初始权重 | `python tools/build_maskrcnn18_init.py` 自建；或 `tools/convert_mmdet_r18.py` 转换 mmdet 权重 | `weights/` |

缺失时相关功能给出明确指引，其余功能不受影响。`.gitignore` 已排除
`weights/`、`xccv/engine/weights/`、`xccv/defectgen/testdata/` 与
`*.pt / *.pth / *.onnx / *.engine / *.xva / *.xcs`。

### 从 0.7.x 迁移

0.8.0 起模型权重为**明文** `best.pt` / `.engine`（训练产物不再封装加密容器）；
旧版的加密权重容器（`.xva` / `.xcs`）不再支持加载——加载时会得到明确提示，
请用 0.8.0 重新训练或重新导出。

## 目录结构

```
XCcv-Multi-functional platform/
├── xccv/                  # 主包
│   ├── annotation/        #   标注平台（labelme 宿主 + AI 智能标注）
│   ├── training/          #   训练平台
│   ├── testing/           #   测试平台（标准页 + 项目复盘页）
│   ├── deploy_platform.py #   部署平台（推理服务窗口 / 模型加载 / C# 测试）
│   ├── service/           #   HTTP 推理服务（FastAPI + C# SDK 与 Demo）
│   ├── modeltools/        #   模型工具窗口（剪枝 / TensorRT 加速）+ 流程画布宿主
│   ├── defectgen/         #   缺陷样本合成（FastAPI + 内嵌 Web）
│   ├── flow_platform.py   #   流程图页（与 AI 平台同级）
│   ├── workbench.py       #   传统算子工作台
│   ├── engine/            #   纯逻辑引擎（数据管线 / 模型注册表 / 指标 / 结果契约）
│   │   ├── models/        #     14 种内置模型（含剪枝 / 导出支持）
│   │   └── flow/          #     流程图引擎（类型化端口 IR / 执行器 / 57 算子）
│   └── assets/            #   图标资源
├── labelme/               # vendored labelme 5.8.1（GPLv3，含本地修改，
│                          #   清单见 labelme/MODIFICATIONS.md）
├── tests/                 # 单元测试（含 tests/modules 模块行为锁）
├── tools/                 # 环境体检 / 文档对账 / 逐模块测试运行器
├── docs/                  # 快速上手 / 配图
├── licenses/              # 许可证文本（AGPL-3.0 / labelme GPLv3 / CIF MIT /
│                          #   SubspaceAD Apache-2.0 / BSD-3 / MIT）
├── requirements.txt
└── run_*.bat              # 各平台启动脚本
```

运行期数据（项目、日志、运行配置）生成于 `platform_data/`，不随仓库分发；
引擎权重放 `weights/` 或 `xccv/engine/weights/`（均已 gitignore）。

## 许可

- 本项目代码以 **GNU Affero General Public License v3.0（AGPL-3.0）** 发布，见 [LICENSE](LICENSE)。
- `labelme/` 目录为 labelme 5.8.1 的 vendored 副本并含本地修改，遵循 **GPLv3**，
  许可文本见 [licenses/labelme-LICENSE-GPLv3.txt](licenses/labelme-LICENSE-GPLv3.txt)。
- 训练链路使用的 ultralytics（YOLO11 / SAM）为 **AGPL-3.0** 许可；如需闭源商用，
  请自行评估其企业许可方案。
- CIF 后端代码源自 [Sunny5250/CIF](https://github.com/Sunny5250/CIF)（MIT），
  SubspaceAD 后端代码源自 [CLendering/SubspaceAD](https://github.com/CLendering/SubspaceAD)
  （Apache-2.0）；剪枝依赖 [Torch-Pruning](https://github.com/VainF/Torch-Pruning)（MIT）。
  修改部分按 AGPL-3.0 授权，许可全文见 `licenses/`。
- 部署服务内置的 Swagger UI 静态资源为 Apache-2.0（Apache Software Foundation）；
  TensorRT 为可选外部运行库（Apache-2.0），不随仓库分发，请自行安装。
- 第三方依赖清单与许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)，
  论文引用见 [CITATIONS.md](CITATIONS.md)。

## 免责声明

本项目按"现状"提供，不附带任何明示或默示的担保。使用本工具训练的模型用于生产环境前，
请自行完成充分验证。
