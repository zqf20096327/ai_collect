# 微信消息补全

Windows 64 位桌面微信的 Rust 托盘程序。在微信输入框按 `Ctrl+Alt+空格` 生成一条灰色建议，按 Tab 填入草稿。输入框为空时写回复，有文字时续写。打字或切换会话会收起建议。

![输入“明天下午三点到，”后按 Ctrl+Alt+空格，草稿上方出现灰色建议，按 Tab 填入](assets/screenshot-completion.png)

## 快速开始

从源码运行时先按下方「构建」生成程序。发布版安装与换机见 [新电脑部署教程](<新电脑部署教程.md>)。

1. 打开 `wechat-completion.exe`，填模型 API 地址、模型名和 API Key，保存后点「测试连接」。
2. 在「手动测试」点「填入示例」，把光标放进草稿框按 `Ctrl+Alt+空格`，看到灰字按 Tab。
3. 勾选「在微信中启用 Ctrl+Alt+空格」。要从本机接口读完整历史，按 [本机服务文档](weflow-local/README.md) 起服务、填令牌。

模型接口需支持 OpenAI 兼容的流式 Chat Completions。

## 历史来源

默认自带 OCR，不装任何服务也能用：勾选「允许读屏获取聊天历史」（默认开启）时，程序用 `assets/ocr/` 的模型识别微信窗口当前显示的消息，条数不够就向上翻页补读，用完恢复原视图。只覆盖窗口内的消息，图片和语音读不到。

起本机服务后消息从数据库取满设置的条数，长消息、引用和图片附件一起交给模型。填了服务地址时读屏作为兜底；取消勾选读屏则只用服务，服务不通就中止本次预测。

## 历史记录

消息条数设 50 时，取当前会话最近 50 条，双方各算一条，模型同时参考草稿。

按快捷键时，程序用微信窗口标题匹配唯一的私聊会话，再按会话 ID 读取消息。只读单聊，多个联系人同名时停止读取并提示。

「最近一次预测」显示提交给模型的会话、历史来源、消息条数、触发时的草稿和附图所在消息，按时间从旧到新排列。

## 回复风格

「从聊天生成提示词」在本机分析本人发出的文字。配套服务扫描已有历史，其他兼容接口用近期采样，最多 90 个会话、每个会话 200 条。勾选「预测时使用」后，预测同时参考长期风格、当前会话近期消息和草稿。

## 本机服务

仓库自带 `weflow-local`，用来读完整历史：它直接解密读微信 4.x 的 `xwechat_files` 目录，对外提供与补全程序配套的 HTTP 接口，不依赖微信界面。需要 Python 3.14 x64 和自备的 `db_key`，会话能按备注、昵称、微信号匹配。安装、配置、接进程序和接口见 [本机服务文档](weflow-local/README.md)。

默认监听 `127.0.0.1:5031`。托盘程序在端口空闲且配置匹配时可在后台启动它。「退出软件」只结束补全程序，服务独立运行。

## 数据与隐私

触发预测时，近期聊天、当前草稿和启用的风格提示词提交给配置的模型接口，开启图片选项时附图一并提交。关闭读屏后，程序仍在本机识别窗口标题、草稿和光标。

## 构建

适用于 Windows x64 GNU 工具链。装 Rustup 和 MSYS2 的 `mingw-w64-x86_64-gcc`，把 `mingw64\bin` 加入当前 PowerShell 的 `PATH`，在仓库根目录执行：

```powershell
rustup toolchain install stable-x86_64-pc-windows-gnu
cargo +stable-x86_64-pc-windows-gnu test --release --locked
cargo +stable-x86_64-pc-windows-gnu build --release --locked
```

配套服务可用合成数据单独测试，步骤见 [本机服务文档](weflow-local/README.md)。

排查时加 `--diagnose` 或 `--diagnose-screen`；设 `WECHAT_COMPLETION_TRACE=1` 后日志写入 `%LOCALAPPDATA%\WeChatCompletion\trace.log`。

## OCR 资源

`assets/ocr/` 取自 RustO! 的 PP-OCRv6 Tiny 0.3.2，保留 [模型包 MIT 许可](assets/ocr/LICENSE) 与 [PaddleOCR 权重 Apache 2.0 许可](assets/ocr/LICENSE-APACHE-2.0)。[RustO!](https://github.com/byrizki/rusto-rs) · [模型包](https://registry.npmjs.org/@rustors%2fmodel-ppocrv6-tiny/0.3.2)

## 社区
本项目在 [LINUX DO](https://linux.do) 社区发布与讨论。
## 许可证

MIT，见 [LICENSE](LICENSE)。`assets/ocr/` 内文件按上游许可分发。
