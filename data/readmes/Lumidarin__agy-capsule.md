# agy-capsule

**中文** | [English](./README.en.md)

Antigravity 输入框底栏的上下文与配额胶囊。

<p align="center">
  <img src="assets/composer-quota-light.png" width="100%" alt="浅色输入框：内联胶囊与多模型额度面板" />
</p>
<p align="center">
  <img src="assets/composer-context-dark.png" width="100%" alt="深色输入框：上下文组成面板，右侧展示 3 分钟黄色预警与 4 分钟红色过期状态" />
</p>

## 功能

- **内联双胶囊**：嵌入输入框底栏，按当前会话与模型动态读取真实上下文上限（如 `256k` / `512k`，未发起首轮前显示 `0 / --`），实时显示 Context 占比与 5h / Weekly 剩余配额。
- **Token 构成明细**：悬停查看 `Turn0`、`Read`、`Think`、`Write` 分段占比与 Token 用量。
- **缓存过期提醒**：距上一轮满 3 分钟变黄倒计时（`~1m`），满 4 分钟变红标记 `Cache` 过期。
- **多模型配额面板**：自动匹配底栏当前模型（如 `Gemini`、`Claude`、`Argon`、`Carbon`），悬停查看各分组 5h 与周配额剩余比例及重置倒计时。
- **窄屏自适应折叠**：底栏变窄时逐级退让（先隐藏周配额，再依次只保留配额与上下文图标，最后省略号压缩模型名），保留悬停弹窗并避免重叠。
- **本地字体回退**：优先使用思源黑体，未安装时使用系统 UI 字体；不下载字体，也不要求额外安装。
- **昼夜自适应 & 跨版本兼容**：直接复用宿主 CSS 变量；通过原生 Sidecar 与 CDP 挂载，不改客户端源码，客户端升级后直接使用。

## 安装

1. 将 [`agy-capsule`](./agy-capsule) 文件夹复制到 Antigravity 插件目录：
   - **Windows**: `%USERPROFILE%\.gemini\config\plugins\agy-capsule`
   - **macOS / Linux**: `~/.gemini/config/plugins/agy-capsule`
2. 在 Antigravity 的 **Plugins** 面板启用 **agy-capsule**。

## 声明

- **缓存过期提示仅供参考**：缓存状态（3 分钟预警 / 4 分钟过期）系根据距上一轮对话的时间间隔本地估算，实际命中情况以服务端为准。
- **测试环境与反馈**：目前仅在 **Windows** 环境下完成测试，欢迎在 **macOS** 环境下测试并反馈问题或提交 PR。

## License

[MIT](./LICENSE)
