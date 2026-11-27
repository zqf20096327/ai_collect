# X.SuperResolution

在本地完成图片放大、降噪与细节增强的桌面工具。基于 Avalonia 和 NCNN-Vulkan，提供 Waifu2x、Real-ESRGAN、SRMD 三种引擎，图片处理无需联网。

[下载发行版](https://github.com/X-Lucifer/X.SuperResolution/releases) · [模型目录说明](FOLDER_STRUCTURE.md) · [安装包构建说明](installer/README.md)

## 运行预览

以下预览展示石墨绿配色在亮色和暗色下的图片工作区。

**石墨绿 · 亮色**

![X.SuperResolution 亮色主题：图片工作区与增强设置](docs/screenshots/workspace-light.png)

**石墨绿 · 暗色**

![X.SuperResolution 暗色主题：算法选择、画质设置与任务操作](docs/screenshots/workspace-dark.png)

## 功能

- **三种增强引擎**：切换 Waifu2x、Real-ESRGAN、SRMD，并选择对应模型、倍率和降噪参数。
- **批量任务队列**：一次添加多张图片，分别查看进度、状态与耗时。同时运行 1–4 条任务，默认 1 条。停止操作会取消正在执行的任务并停止派发后续任务。
- **输出可配置**：在系统设置里选择 PNG、JPG 或 WEBP，设置保存目录和文件名后缀。点击目录路径可打开文件夹。
- **性能参数**：选择 GPU 设备、分块大小、线程配置及 TTA。
- **运行记录**：查看批次耗时、处理日志和设备信息；批次结束时记录完成情况与本批次实际使用的完整输出目录。
- **界面响应**：任务列表按可视范围创建行，后台导入文件及准备引擎，合并日志与进度通知，降低大批量任务对界面的影响。
- **桌面体验**：石墨绿、克莱因蓝、竞速红、青柠绿和电光紫各有亮暗两款。左下角的系统设置分为通用、界面和关于。界面页可切换配色、语言和本机字体；顶栏支持快捷切换中英文及同组亮暗外观。关于页包含功能说明、版本和 GitHub 项目链接。
- **系统托盘**：托盘菜单可打开主界面或退出应用。启用“关闭窗口时最小化到托盘”后，关闭窗口会保留正在运行的批次。

## 系统与运行环境

当前仓库面向 **Windows 10 / 11 x64** 提供发布脚本，使用 **.NET 10**。目标电脑需要支持 Vulkan 的 GPU 及相应的 x64 显卡驱动。

两款绿色版均内置 .NET 运行时和所需的原生运行库，解压后即可启动 `X.SuperResolution.exe`。Full 随附全部内置模型，Thin 只省去模型文件。使用 Thin 处理图片前，将所需引擎的模型目录放到主程序旁。

托管版和 NativeAOT 安装包均包含全部内置模型。NativeAOT 将应用预编译为原生 EXE，NCNN、OpenMP 和图形库以 DLL 随包分发。

## 快速开始

1. 从 [Releases](https://github.com/X-Lucifer/X.SuperResolution/releases) 下载适合的发行包，安装或解压到有写入权限的目录。
2. 启动 `X.SuperResolution.exe`，点击 **添加图片**。支持 PNG、JPG、JPEG、WEBP，单张上限为 50 MB。
3. 在 **增强设置** 中选择引擎、模型、放大倍率和降噪参数。Waifu2x 的 CUNet 可用 1× 仅降噪，两套 UpConv 模型从 2× 起步，最高可选 32×。Real-ESRGAN 的 animevideov3 支持 2×、3× 和 4×，x4plus 系列使用原生 4×，保留完整画面。
4. 在 **系统设置 → 通用** 选择输出格式、目录与文件名后缀。首次启动使用 PNG 和 `_out`，保存在程序目录下的 `output` 文件夹。
5. 点击 **开始增强**，在任务队列查看进度，在 **运行记录** 查看日志与耗时。

同一批次的输出重名或与队列中的输入路径相同时，程序会追加 `_2`、`_3` 等编号。已有的同名历史输出在新结果写入成功后替换。

系统设置自动保存到程序目录下的 `settings.json`，包括主题、界面字体、语言、输出目录、格式、后缀、默认引擎、GPU、线程配置、并发数和关闭行为。下次启动时，工作区会打开选定的 Waifu2x、Real-ESRGAN 或 SRMD 引擎。已有配置会沿用亮暗主题、语言和输出目录，原默认模型会转换为其所属引擎。具体模型在工作区选择，每个批次使用点击开始时的参数。

使用可选的 `realesrnet-x4plus` 时，将同名的 `.param` 和 `.bin` 文件放入 `models` 目录。重启后即可在工作区的 Real-ESRGAN 模型列表中选择它。

## 模型与目录

模型文件夹应与主程序放在同一目录，保持原有名称及内部结构。完整包的主要目录如下：

```text
X.SuperResolution/
├── X.SuperResolution.exe
├── vcomp140.dll
├── models/                              # Real-ESRGAN
├── models-cunet/                         # Waifu2x CUNet
├── models-srmd/                          # SRMD
├── models-upconv_7_anime_style_art_rgb/   # Waifu2x 动漫模型
├── models-upconv_7_photo/                # Waifu2x 照片模型
├── output/                              # 默认输出目录，运行时创建
└── settings.json                        # 设置保存后创建
```

各模型的文件组成见 [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md)。精简包需要补齐所使用引擎的模型；不要将 `.param` 与 `.bin` 文件拆开或改名。

## 从源码运行

准备 .NET 10 SDK。原生引擎还需要 Vulkan 驱动及 x64 `vcomp140.dll`；可通过 Visual Studio 的“使用 C++ 的桌面开发”工作负载取得 OpenMP 运行库。

在仓库根目录执行：

```powershell
dotnet restore X.SuperResolution.slnx
dotnet build X.SuperResolution.slnx
```

将 OpenMP 运行库复制到调试输出目录，再启动程序：

```powershell
$vcompPath = & .\scripts\Resolve-Vcomp140.ps1
Copy-Item -LiteralPath $vcompPath -Destination .\X.SuperResolution\bin\Debug\vcomp140.dll
dotnet run --project .\X.SuperResolution\X.SuperResolution.csproj --no-build
```

模型和原生引擎文件由项目配置复制到构建输出目录。

## 构建发布包

准备 .NET 10 SDK、7-Zip、NSIS 3 Unicode、MSVC C++ 桌面开发工具和 Windows SDK。在仓库根目录运行以下命令即可发布。

```powershell
.\scripts\release-win-x64.ps1
```

四个发行文件都在 `artifacts/release/` 目录下。

| 文件名 | 内容 |
| --- | --- |
| `X.SuperResolution-win-x64-full.7z` | 含全部内置模型的绿色版 |
| `X.SuperResolution-win-x64-thin.7z` | 仅省去模型的绿色版 |
| `X.SuperResolution-win-x64.exe` | 含全部内置模型的托管版安装包 |
| `X.SuperResolution-win-x64-NativeAOT.exe` | 含全部内置模型的 NativeAOT 安装包 |

单独生成一种包或复用已有发布目录的命令见[安装包构建说明](installer/README.md)。

## 常见问题

| 现象 | 检查方式 |
| --- | --- |
| 缺少 `vulkan-1.dll` | 从显卡厂商官网下载并更新支持 Vulkan 的 x64 驱动。 |
| 原生引擎无法加载或缺少 `vcomp140.dll` | 确认使用 x64 程序，并保留发行包中的运行库；源码运行时按上述步骤复制 OpenMP 运行库。 |
| 找不到模型或模型加载失败 | 检查模型目录名称、位置及 `.param` / `.bin` 文件是否完整，并确认所选模型与当前引擎匹配。 |
| 图片没有进入任务队列 | 检查文件格式和单张大小限制；超出限制的提示可在运行记录中查看。 |
| 不知道结果保存在哪里 | 查看系统设置中的输出目录；默认位置为程序目录下的 `output`。 |

## 第三方项目

- [Avalonia](https://github.com/AvaloniaUI/Avalonia)：桌面界面框架。
- [ncnn](https://github.com/Tencent/ncnn)：神经网络推理框架。
- [waifu2x-ncnn-vulkan](https://github.com/nihui/waifu2x-ncnn-vulkan)
- [realesrgan-ncnn-vulkan](https://github.com/nihui/realesrgan-ncnn-vulkan)
- [realsr-ncnn-vulkan](https://github.com/nihui/realsr-ncnn-vulkan)
- [srmd-ncnn-vulkan](https://github.com/nihui/srmd-ncnn-vulkan)

## 使用声明

不得将该程序用于任何商业及违法用途。
