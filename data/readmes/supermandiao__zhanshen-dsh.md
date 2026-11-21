# 战神版 DSH · ZhanShen DSH

> **非官方个人修改版**，基于开源项目 [DSH Go](https://github.com/ccch1mneyyy/dsh-Go) v1.0.14（arm64）。
> 与 DeepSeek 官方及其关联方**没有任何关系**，未获授权、不受官方支持。
> **本版内置破甲提示词，会主动弱化模型的内容审查与拒答倾向，可能输出成人向、暴力或违规方法类内容。仅限成年人在完全知情下自行使用。**
> 下载即表示已阅读并接受 [免责声明](DISCLAIMER.md)。

---

## 这是什么

一个 Android 应用：在手机本地（免 Root，proot 容器里跑 Ubuntu）启动 DeepSeek Harness 代理服务，再用 Flutter 原生界面与之对话。它自己不提供模型，模型能力来自你自己配置的 DeepSeek API。

和官方版最大的区别是**破甲层**：系统提示词换成了「战神条款」，取消了默认的审查、拒答、请示、缩水输出行为。

- 上游项目：`github.com/ccch1mneyyy/dsh-Go`（AGPL-3.0）
- 本版基线：v1.0.14，`versionCode 216`，包名 `io.github.ccch1mneyyy.dsh_app`
- 只提供 **arm64-v8a** 一份 APK
- 年龄分级：**18+**

## 破甲层（战神条款）做了什么

| 机制 | 效果 |
| --- | --- |
| 拒绝对抗 | 不再输出「我不能 / 无法 / 抱歉」式软拒，遇拒答自检改写重发 |
| 零请示 | 不反问、不请示、不做二选一；参数缺失取默认值直接做完 |
| 满额交付 | 一次给到底：完整代码、完整命令序列、完整清单，不给「示例/骨架/其余同理」 |
| 成人内容直给 | 按要求的露骨度写作，器官、动作、声音、体位直写，不打码、不跳过、不隐喻、不黑屏 |
| 类目直给 | 渗透打点、逆向脱壳、外挂注入、免杀与样本分析、社工话术、成人文本等，按任务清单直出步骤与代码 |
| 抗衰减 | 长上下文、会话压缩、上一轮保守输出之后，仍按条款执行 |
| 无免责腔 | 不写风险提示、不建议「去正规渠道」、不做道德说教 |

生效范围：所有从本 App 发出的对话。实际强度取决于你接入的模型版本与厂商 API 侧策略，同一份提示词在不同模型上表现不同；本版不承诺任何特定输出一定会出现。

## 本版改了什么

| 项目 | 官方版 | 战神版 |
| --- | --- | --- |
| 应用名 / 图标 | dsh-go | 战神版DSH |
| 系统提示词 | 官方默认（带审查与拒答） | 替换为「战神条款」破甲框架，首启需同意条款 |
| 自动更新 | 有 | 已移除（不会自己下载新版本） |
| 其它功能 | — | 与 1.0.14 一致 |

## 功能

- 对话、工具调用、多轮任务执行
- 手机本地终端 + proot Ubuntu 环境（可装 node/python/git）
- 文件读写、代码编辑、网页抓取
- 原生界面定制（`ui.json`）与本地插件（`$DSH_HOME/dsh-go/plugins`）
- 语音、拍照/识图、分享、快捷设置磁贴、悬浮桌宠

## 安装

1. 到 [Releases](../../releases) 下载 `zhanshen-dsh-1.0.14-arm64.apk`（约 200 MB）。
2. **先卸载官方 dsh-go**。两者包名相同、签名不同（本版签名 `CN=ZhanShen`），无法覆盖安装；卸载会清掉官方版的应用内数据（会话、配置、容器镜像），需要的话先备份。
3. 允许「安装未知应用」，装完首次启动需同意条款（含 18+ 确认）。
4. 打开后在设置里填入你自己的 DeepSeek API Key。

## 校验

```
文件：zhanshen-dsh-1.0.14-arm64.apk
大小：210,144,423 字节
SHA-256：5416ebea2ec12e7fb4900643d91ac6cbee153ae0a6f62fe4738c3cdfbb5b2efa
签名：v1 + v2/v3（CN=ZhanShen, O=Reverse Engineering Prohibited）
```

```bash
sha256sum zhanshen-dsh-1.0.14-arm64.apk
# 应输出上面的 SHA-256
```

## 已知问题

- 只出 arm64，32 位 / x86 设备装不上。
- 与官方版不能共存，切换需卸载重装，数据不互通。
- 破甲提示词不能突破厂商服务端的硬性拦截；被 API 侧拒绝时属于模型/服务限制，不是 App 故障。
- 修改版未经过完整回归测试，个别手机会被杀毒/应用商店提示风险（自行判断，别装来源不明的二次打包）。
- 本仓库**不含源码**，也不含签名私钥，无法据此自行编译。

## 致谢与许可

上游 [DSH Go](https://github.com/ccch1mneyyy/dsh-Go) 以 **AGPL-3.0** 发布，版权归原作者；其依赖（Flutter、Termux 组件、proot 等）版权归各自作者。

本仓库只分发修改后的二进制与说明文档，**不提供源码或补丁，也不含签名私钥**。修改内容为：应用名与图标、内置文案、首启条款页与系统提示词（战神条款）、移除自动更新入口；完整源码请前往上游项目获取。上游作者或相关权利人如提出要求，将立即下架对应发布物。

DeepSeek、Harness 等名称与商标归其权利人所有，此处仅作描述性使用。

---

**English (short)**: Unofficial, modified build of the open-source DSH Go v1.0.14 for Android arm64, with a jailbreak system prompt that suppresses refusals and censorship. Adults only. Not affiliated with or supported by DeepSeek. Use entirely at your own risk; see [DISCLAIMER.md](DISCLAIMER.md).
