# 大肥鱼（Big Fat Fish）

基于 DeepSeek 官方前端示例（`chat-demo`）改造的安卓客户端，应用显示名为「大肥鱼」，与官方品牌无关联。原生 WebView 壳 + 前端资源内置，配合一组原生能力桥，得到接近官方 App 的移动端体验。

<p>
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue.svg" />
  <img alt="platform" src="https://img.shields.io/badge/platform-Android%208.0%2B-3ddc84.svg" />
  <img alt="language" src="https://img.shields.io/badge/Kotlin-2.x-7f52ff.svg" />
  <img alt="frontend" src="https://img.shields.io/badge/React-18-61dafb.svg" />
</p>

> ⚠️ 第三方开源项目，**与 DeepSeek 官方无关**，未获得官方背书。项目名称与图标仅用于说明用途，正式分发前建议替换为自有素材（详见[免责声明](#免责声明)）。

## 截图

|                       对话                       |                      侧边栏                      |                     搜索历史                     |
| :----------------------------------------------: | :----------------------------------------------: | :----------------------------------------------: |
| <img src="docs/images/chat.png" width="240">     | <img src="docs/images/sider.png" width="240">    | <img src="docs/images/search.png" width="240">   |
|              **拍照 / 相册 / 文件**              |                    **圈画标注**                  |                     **设置**                     |
| <img src="docs/images/attach.png" width="240">   | <img src="docs/images/editor.png" width="240">   | <img src="docs/images/settings.png" width="240"> |
|                  **深色对话**                    |                  **深色侧边栏**                  |                   **欢迎页**                     |
| <img src="docs/images/dark.png" width="240">     | <img src="docs/images/sider-dark.png" width="240"> | <img src="docs/images/welcome.png" width="240"> |

## 功能

- **对话**：流式输出、停止与重新生成、多版本切换、继续生成；深度思考可折叠（默认只展示最新部分），支持联网搜索
- **富文本**：Markdown、代码高亮、KaTeX 公式、Mermaid 图表
- **模型**：`Flash` / `Pro` 可选，推理强度与最大输出长度可调；登录账号后无需 API Key 即可对话
- **附件**：拍照 / 相册（支持多选、选中即传）/ 本地文件；大图预览与就地圈画标注
- **花费可见**：每条回复显示输入输出 token 与金额估算，按官方价格表区分高峰 / 空闲时段，旁边「?」说明以实际账单为准
- **侧边栏**：跟手推开主界面（非覆盖），置顶分组、多选批量管理、搜索命中定位、滚动位置保持；上千条历史也流畅
- **外观**：浅色 / 深色 / 跟随系统，四档字号，中英双语，可调朗读音色
- **数据**：导入官方导出的历史 ZIP（单条不兼容只跳过），导出分块写入系统「下载」
- **移动端**：返回键逐级关闭弹层、键盘弹出时输入框上移、生成期间后台不中断

## 下载安装

从 [Releases](https://github.com/xdtbp/DaFeiYu/releases) 下载最新 APK 安装即可，支持 Android 8.0 及以上。

首次启动会展示权限用途说明与免责声明，同意后进入引导页，可完成权限申请、登录或配置 API Key、导入历史。

## 使用

1. **配置凭证**：登录 Harness 账号，或在「设置 → 数据管理」填入 DeepSeek 开放平台的 API Key，二者满足其一即可对话。
2. **查看余额**：侧边栏底部显示账号头像、昵称与余额，点击可刷新；API Key 余额在「设置 → 数据管理」中查看。
3. **导入历史**：「设置 → 数据管理 → 导入」，选择官方导出的 `deepseek_data-*.zip`；单条会话不兼容时只跳过该条。
4. **导出历史**：「设置 → 数据管理 → 导出」，文件保存至系统「下载」目录。
5. **常见操作**：「+」打开拍照 / 相册 / 文件；侧边栏「⋯」菜单可重命名、置顶、多选、删除会话。

## 更多文档

| 文档                                                  | 内容                             |
| :---------------------------------------------------- | :------------------------------- |
| [docs/FEATURES.md](docs/FEATURES.md)                   | 按模块罗列的完整功能清单         |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)           | 前端与原生壳的模块划分、数据流   |
| [docs/BUILD.md](docs/BUILD.md)                         | 构建步骤、签名发布、常见报错     |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)     | 安装与使用中的常见问题           |
| [CHANGELOG.md](CHANGELOG.md)                           | 各版本更新记录                   |

## 免责声明

- 本项目为个人学习与自用目的开发的第三方客户端，**与 DeepSeek 官方无任何关联**，不代表官方立场。
- 项目中的产品名称、图标等素材版权归其权利人所有；正式发布前请替换为自有品牌素材，以规避商标风险。
- 使用账号令牌访问官方接口属于非公开用法，可能随官方策略变化而失效，请自行评估账号风险。
- 本项目按 MIT 协议「按现状」提供，不对数据丢失、账号异常等后果承担责任。
- AI 生成内容仅供参考，需自行甄别。

## 许可证

本项目以 **MIT** 协议开源，详见 [LICENSE](LICENSE)。

前端部分基于 DeepSeek 官方 `chat-demo`（MIT, Copyright © 2026 DeepSeek）修改，原始许可证保留在 [web/LICENSE](web/LICENSE)，第三方说明见 [NOTICE.md](NOTICE.md)。
