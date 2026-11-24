# magpie 安卓版（Android 17 / API 37.2）

把 [yetone/magpie](https://github.com/yetone/magpie) 的网关和网页界面装进一个 Android APK：网关在应用的前台服务里运行，WebView 打开 magpie 自己的页面，手机上的 agent 通过 `http://127.0.0.1:3425/v1` 使用它。

本项目基于 [gllhack/magpie-android](https://github.com/gllhack/magpie-android) 的 Android 壳子方案，跟进上游最新稳定版 **v0.1.4652**（2026-11-21），并把 Android 构建链、Go、Bun、Gradle、AGP、Android SDK 与 NDK 全部升级到当前最新稳定版本。

> 这是非官方 Android 移植。magpie 本身由 yetone 开发，项目地址：[yetone/magpie](https://github.com/yetone/magpie)。

![主界面](screenshots/01-main-ui.png)

## 当前构建

| 组件 | 版本 |
| --- | --- |
| magpie 上游 | v0.1.4652 |
| Go | 1.27.4 |
| Java / JDK | 21.0.13 |
| Gradle | 9.9.2 |
| Android Gradle Plugin | 9.5.2 |
| Android SDK Platform | 37.2（Android 17 QPR2） |
| Android Build Tools | 37.0.0 |
| Android NDK | r30（30.0.16248370） |
| Bun（插件运行时） | 1.4.5 |
| 应用版本 | 0.1.4652（versionCode 4652） |
| APK ABI | `arm64-v8a`、`x86_64` |

## 功能

- **一个本地网关**：默认监听 `127.0.0.1:3425`，给 Claude Code、Codex、Gemini CLI 等 agent 当统一 base URL。
- **完整网页界面**：magpie 自己的供应商、账号、模型、路由组、插件和设置页面都在 APK 里，首次启动自动打开。
- **前台服务**：通知栏常驻，进程退出后自动按退避重启；支持开机自启和忽略电池优化。
- **局域网访问**：可在设置里监听 `0.0.0.0:3425`，网页界面始终只绑定本机。
- **插件运行时**：内置 Bun 1.4.5 的 Android 构建，社区插件可以直接安装和运行。
- **应用内检查更新**：从本仓库的 GitHub Release 读取最新版本，支持跳转 Release 或直接下载 APK。
- **Material 3 风格壳子**：底部弹出菜单、设置、日志、端口修改、复制网关地址。

## 构建

### 环境

Linux（x86_64 或 ARM64 均可，Android 手机上的 Ubuntu proot 也可以）：

- JDK 21
- Go 1.27.4
- Android SDK：Platform 37.2、Build Tools 37.0.0
- Android NDK r30
- `curl`、`unzip`、`zip`
- ARM64 主机额外需要 `clang-19`、`lld-19`、`qemu-user-static`（AAPT2 只有 x86_64 版本）

macOS/Windows 建议直接用 GitHub Actions，或在 WSL/Git Bash 里执行同一份脚本。

### 一键构建

```bash
export ANDROID_HOME=/path/to/android-sdk
export ANDROID_NDK_HOME=$ANDROID_HOME/ndk/30.0.16248370

# 手机：只编 arm64-v8a，产物约 212 MB
./scripts/build-apk.sh --abis arm64-v8a

# 模拟器：只编 x86_64
./scripts/build-apk.sh --abis x86_64

# 两个架构的通用包（约 434 MB）
./scripts/build-apk.sh
```

产物：

```text
dist/magpie-android-arm64-v8a.apk
dist/magpie-android-x86_64.apk
# 或 dist/magpie-android-universal.apk
```

只重新打包 APK、复用上次网关二进制：

```bash
./scripts/build-apk.sh --skip-gateway --abis arm64-v8a
```

不内置 Bun（插件页会提示没有插件运行时，APK 会小约 100 MB）：

```bash
./scripts/build-apk.sh --no-bun --abis arm64-v8a
```

### 分开构建

```bash
# 只编网关到 android/app/src/main/jniLibs/<abi>/libmagpie.so
ABIS=arm64-v8a ./scripts/build-magpie-android.sh

# 再打 APK
./scripts/build-apk.sh --skip-gateway --abis arm64-v8a
```

`GOPROXY` 默认 `https://goproxy.cn,direct`；网络能直连 Go 模块时可以改成 `https://proxy.golang.org,direct`。

### GitHub Actions

`.github/workflows/android-release.yml` 会在推送 `v*-android` tag 时自动构建两个 ABI 的 APK，并创建 GitHub Release：

```bash
git tag v0.1.4652-android
git push origin v0.1.4652-android
```

也可以在 Actions 页面手动触发 `Android APK`。

## 安装

```bash
adb install -r dist/magpie-android-arm64-v8a.apk
```

没有电脑时，把 APK 传到手机，点开安装即可。首次安装需要允许“安装未知应用”。

打开后 magpie 会自动启动网关，顶部状态栏显示端口；点 `⋮` 打开菜单：

1. **复制网关地址**：得到 `http://127.0.0.1:3425/v1`，填到手机上的 agent 里。
2. **设置**：改网关端口、网页端口、局域网访问和开机自启。
3. **查看日志**：网关最后 300 行输出，出问题先看这里。
4. **检查更新**：访问本仓库的最新 Release。

## 应用内更新

应用内更新逻辑在：

```text
android/app/src/main/java/com/magpie/android/UpdateChecker.java
```

它请求：

```text
https://api.github.com/repos/1527183723/magpie-android/releases/latest
```

版本号从 Release 的 `tag_name` 中提取（例如 `v0.1.4652-android` → `0.1.4652`），与已安装 APK 的 `versionName` 比较。发现新版本时，应用会显示更新说明，并提供：

- **下载 APK**：优先选择 `magpie-android-<当前 ABI>.apk`，没有时回退到 `magpie-android-universal.apk`；
- **打开 Release**：打开该 Release 的 GitHub 页面。

发布新版本时，请保持以下约定：

| 项目 | 约定 |
| --- | --- |
| Git tag | `v<上游版本>-android`，例如 `v0.1.4652-android` |
| APK 资源名 | `magpie-android-arm64-v8a.apk`、`magpie-android-x86_64.apk` |
| 版本号 | `android/version.properties` 的 `versionName` 与 tag 中的数字一致 |
| 签名 | 必须使用仓库内的固定签名密钥，保证覆盖安装 |

如果要换到自己的 GitHub 仓库，只改 `UpdateChecker.java` 里的 `REPO` 常量即可。

应用启动时最多每 24 小时自动检查一次；也可以随时从菜单手动检查。GitHub 未登录 API 有每小时 60 次的限额，超限时应用会提示稍后再试。

## 目录

| 目录 | 内容 |
| --- | --- |
| `android/` | Android 工程，壳子代码在 `android/app/src/main/java/com/magpie/android/` |
| `upstream/` | magpie 上游源码（v0.1.4652），仅把默认 Bun 运行时更新到 1.4.5 |
| `scripts/` | Linux/CI 构建脚本：网关、Bun、APK |
| `screenshots/` | 应用截图 |
| `dist/` | 构建产物（不提交） |

## 签名

`android/keystore/magpie-release.jks` 是项目公开、可复现的签名密钥，所有本地和 GitHub Actions 构建都用它签名，这样新版本可以直接覆盖安装。它**不适合上架 Google Play**：密钥是公开的，任何人都能用同一个包名签名。

需要私有签名时，用自己的 keystore，并设置：

```bash
export MAGPIE_KEYSTORE_PASSWORD=...
export MAGPIE_KEY_ALIAS=...
export MAGPIE_KEY_PASSWORD=...
```

## 运行时与体积

| 组成 | 大小（约） |
| --- | --- |
| arm64 magpie 网关 | 106 MB |
| arm64 Bun 1.4.5 | 113 MB |
| x86_64 magpie 网关 | 114 MB |
| x86_64 Bun 1.4.5 | 118 MB |

所以单 ABI APK 约 212–224 MB，通用包约 434 MB。只编手机用的 `arm64-v8a` 最省空间。

## 已知限制

- `minSdk = 36`，只支持 Android 16 及以上。
- 当前仓库的 Release APK 使用公开测试签名，适合直接安装和开源分发，不适合应用商店。
- 部分社区插件依赖 Bun 的 Android 构建；Bun 本身在 Android 上仍可能遇到 JIT/系统调用限制，装不上时先看应用日志和插件页提示。
- 应用内更新只负责检测和跳转下载，不会静默安装 APK；Android 系统会要求用户确认安装。

## 许可证

本项目沿用上游 MIT 许可证；上游版权归 yetone 所有，Android 壳子与构建脚本的修改归本项目贡献者所有。详见 [LICENSE](LICENSE)。
