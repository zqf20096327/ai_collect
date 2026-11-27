# MicMask

**安卓端真正的原生实时 AI 变声软件**

![MicMask](docs/screenshots/banner.png)

[![Release](https://img.shields.io/github/v/release/Taocrypt/MicMask?label=release)](https://github.com/Taocrypt/MicMask/releases/latest)
[![License](https://img.shields.io/github/license/Taocrypt/MicMask)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Taocrypt/MicMask?style=flat)](https://github.com/Taocrypt/MicMask/stargazers)

MicMask 在手机本地把你的声音实时转换成另一个音色，并直接送进 QQ、微信、游戏等应用的麦克风。对方听到的，就是变声后的声音。

## 为什么选 MicMask

- **无需 Root**：借助 [Shizuku](https://shizuku.rikka.app/) 以 shell 身份注入麦克风，普通手机即可使用。
- **不用虚拟机、不用双开容器**：目标应用正常安装、正常打开，不需要把软件装进虚拟机或分身容器里。
- **真·本地 AI 实时推理**：基于 RVC 音色转换，ONNX Runtime 在手机 CPU 上运行，录音全程不上传。
- **低延迟**：端到端约 300 ms（骁龙 8 Gen 3 标准档实测）。
- **开源免费**：GPL-3.0 协议，无订阅、无内购。

## 功能

- **AI 实时变声**：标准 0.3 秒 / 省电 0.5 秒两档，自动测速选档、跟不上时自动降档；半音偏移、检索比例（index）、静音门限、线程数、推理绑大核等可调；变声中可直接切换音色
- **推理加速（2.1 测试版起）**：声码器可选 ORT / NEON fp16 / 骁龙 NPU，HuBERT 可选上 NPU；NPU 运行库首次使用时经你同意后从官方 Maven 源下载，不随安装包分发
- **一键性能测试**：实测本机后自动采用最快的声码器、HuBERT 后端和特征 / 合成线程数
- **音色微调（实验）**：响度跟随（音量起伏跟原声走）、共振峰偏移（音高不变改厚薄）、相位锁定（减轻块边界的轻微嗒嗒声）
- **导入音色**：社区模型仓库一键下载；手机直接导入 RVC `.pth` + `.index`（本机转换与量化）；兼容 w-okada 导出的 ONNX
- **生效范围**：自动识别任何正在录音的应用，或手动指定目标应用
- **普通变声**：低延迟升降调 + 音色效果，内置男变女、萝莉、御姐、大叔、机器人等预设，自定义预设可用分享码分享
- **虚拟声卡**：场景预设、空间、动态、均衡等效果
- **音效包送麦**：内置 CC0 音效，支持 `.mim3` 音效包的制作、导入与分享
- **文件变声**：整段音频高质量转换，长音频自动分段，可导出或直接送麦
- **文字转语音**：基于 GPT-SoVITS 的本地中文语音合成
- **悬浮窗**：在游戏或聊天界面里切换模式、预设，查看性能
- **普通模式**：没有 Shizuku 时回退为扬声器外放的录播变声
- **应用内更新**：从 GitHub Releases 更新，国内可自动选择下载镜像
- **使用教程**：App 内「设置 → 其他 → 使用教程」，联网自动获取最新版

## 截图

<p align="center">
<img src="docs/screenshots/store/01.png" width="30%"> <img src="docs/screenshots/store/02.png" width="30%"> <img src="docs/screenshots/store/03.png" width="30%">
<img src="docs/screenshots/store/04.png" width="30%"> <img src="docs/screenshots/store/05.png" width="30%"> <img src="docs/screenshots/store/06.png" width="30%">
</p>

宣传图由 [NimoteShot](https://github.com/mobiledevloperlab/nimoteshot) 基于实机截图（`docs/screenshots/01–06.png`）生成。

## 下载

前往 [GitHub Releases](https://github.com/Taocrypt/MicMask/releases/latest) 下载 `MicMask-<版本>-android-arm64-v8a.apk`。已安装的用户可以在 App 内「设置 → 其他 → 关于 MicMask → 检查更新」直接升级。

## 快速开始

1. **安装 MicMask**，首次打开阅读并同意使用说明，允许麦克风权限。
2. **安装并启动 Shizuku**（Android 11+ 可用无线调试启动，无需电脑和 Root），在 MicMask「设置 → 运行模式」选择「Shizuku 模式」并授权。
3. **获取音色**：在「设置 → 模型仓库」添加你信任的仓库后下载音色，或在「变声 → AI 变声」点「导入模型」导入 `.pth` + `.index`。
4. **开始变声**：选中音色，调整音高偏移（男声→女声 +12），点「开始」。
5. **打开 QQ / 微信 / 游戏** 正常语音即可。戴耳机并打开「实时耳返」可以听到自己的变声效果。

详细步骤、参数说明和排错见 **[使用手册](docs/manual.md)**。

## 系统要求

| 项目 | 要求 |
| --- | --- |
| Android | 8.0 及以上；Shizuku 注入模式需要 Android 10 及以上 |
| 架构 | 仅 arm64-v8a |
| 处理器 | 实测设备为骁龙 8 Gen 3；中端芯片建议使用省电 0.5 秒档；骁龙平台可选 NPU 加速 |
| 其他 | 实时注入需要 Shizuku；建议佩戴耳机 |

## 已知限制

- 端到端约 300 ms 为骁龙 8 Gen 3 标准档实测，其他机型延迟可能更高；性能不足时会自动降到省电档。
- 量化模型相对电脑端有一定音质损失。
- 外放场景可能啸叫，请戴耳机。
- 部分机型的系统音频策略不支持注入，实时变声不可用（可用普通模式录播）。
- 普通模式为扬声器外放，对方可能同时听到原声。
- 无线调试启动的 Shizuku 在手机重启后需要重新启动。

更多问题见手册的 [常见问题与排查](docs/manual.md#常见问题与排查)。

## 模型说明

MicMask **不附带任何音色模型**。在「设置 → 模型仓库」填写仓库地址（models.json 链接、GitHub 或 CNB 仓库），或在 AI 变声页导入本地模型。请只使用你本人的声音或已获得授权的模型。

## NPU 与推理加速

2.1 测试版起，AI 实时变声可以把部分推理交给骁龙 NPU（QNN HTP）：

- **声码器**：自动 / ORT / NEON fp16 / NPU。自动会实测几种方式取最快；NEON fp16 需要 ARMv8.2 半精度指令。
- **HuBERT 用 NPU**：独立开关；首次使用会在本机改写并编译模型，不比 CPU 快或校验不通过就自动留在 CPU。
- **NPU 组件**：高通 QNN 运行库按高通自己的许可发布，不属于 MicMask 的开源部分，不随 APK 或仓库分发；首次开启时经你同意后，从 Maven Central 或其国内镜像下载官方包并逐个校验。
- 支持的骁龙平台按 SoC 自动匹配 HTP 版本（V68–V81）。联发科等非骁龙芯片只用 CPU：天玑 9300 系实测 NNAPI 和 WebGPU 都比 CPU 慢，所以不接。
- 出错或校验不通过会自动退回 CPU 通路，不影响出声。

各机型实测数据、日志与转换脚本见 [qnntest/results](qnntest/results/README.md)。实测延迟口径仍以「骁龙 8 Gen 3 标准档实测约 300 ms」为准，其他机型以你自己的性能测试为准。

## 从源码构建

```sh
./gradlew :app:assembleDebug
```

需要 JDK 17、Android SDK（compileSdk 37）。发版签名通过 `-PsigningProps=signing.properties`（storeFile / storePassword / keyAlias / keyPassword）传入，签名文件不要放进仓库。

推送 `v<版本号>` 标签后，GitHub Actions 会自动构建并发布 Release，说明取自 [CHANGELOG.md](CHANGELOG.md)。App 内置的使用教程在构建时由 `docs/manual.md` 复制生成，只需维护这一份文件。

## 赞赏与交流

- **赞赏**：MicMask 完全免费、开源。喜欢的话可以在 [爱发电](https://afdian.com/a/taocrypt) 支持一下，赞助者会出现在 App 的赞赏墙上，赞助期内 App 不显示推广。
- **QQ 交流群**：780988679
- **问题反馈**：[GitHub Issues](https://github.com/Taocrypt/MicMask/issues)，或 App 内「关于 MicMask → 交流反馈 → 反馈问题」（可附带日志）

## 致谢

- [atri-vc](https://github.com/spider996/atri-vc)：本项目的起点，实时 RVC 安卓实现
- [RVC-Android](https://github.com/ouor/RVC-Android)：安卓端 RVC 推理方案参考
- [mobile-rvc](https://github.com/nasuiyile/mobile-rvc)：手机端实时变声参考；原生 NEON fp16 声码器内核移植自该项目，响度跟随、共振峰偏移、相位锁定三项参数也参考了它的实现（MIT，声明见 NOTICE.md）
- [RVC WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)：Retrieval-based Voice Conversion 音色转换
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)：文本转语音
- [ONNX Runtime](https://github.com/microsoft/onnxruntime)：端侧推理引擎
- [Shizuku](https://github.com/RikkaApps/Shizuku)：免 Root 获取 shell 权限
- [Miuix](https://github.com/compose-miuix-ui/miuix)：界面组件库

上游与第三方声明见 [NOTICE.md](NOTICE.md)。

## 免责声明

- 本项目仅供学习与娱乐。禁止用于冒充他人、诈骗、骚扰或任何违法用途，使用者自行承担全部责任。
- 使用他人声音模型前须取得权利人授权；用真人或角色的声音可能涉及他人权益。依法需要标识的合成内容，请按要求标识。
- 以上为使用提醒，不构成法律意见。

## 许可证

[GPL-3.0](LICENSE)。上游与第三方声明见 [NOTICE.md](NOTICE.md)。

公告、推荐位、反馈与可选匿名统计使用 Beacon SDK（MIT，见 [beacon/LICENSE](beacon/LICENSE)）；源码或本地构建未注入后台地址时自动关闭。
