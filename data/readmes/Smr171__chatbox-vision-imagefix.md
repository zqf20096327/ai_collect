# Chatbox Vision ImageFix

> 基于 [Chatbox](https://github.com/Bin-Huang/chatbox) v1.23.5 的 Windows x64 修改版，聚焦知识库图片识别链路。

**非官方修改版，与 Chatbox 官方团队无关。**

## 这是什么

这个版本不是换一个更强的模型，而是修复 Chatbox 把知识库内容交给模型时丢失图片的问题：

- 本地 PDF 解析走的是文字提取，不是原图读取；
- 检索结果里可能只有“图 3-2”这样的文字，没有图；
- 原图读取、PDF 按页渲染、局部裁剪、模型缓存和超时控制，任何一环出问题，模型都看不到正确的图。

本版把这条链路补上，并尽量把“读图失败”和“模型读错图”区分开。

详细排查记录见博客：[换遍模型，Chatbox 知识库为什么还是看不清图片？](https://ssmr.tech/posts/chatbox-kb-image-debug)

## 下载

安装包不放在 Git 仓库里（超过 GitHub 单文件 100 MiB 限制），请到本仓库的 [Releases](../../releases/latest) 页面下载：

| 文件 | 说明 |
| --- | --- |
| `Chatbox-Vision-ImageFix-1.23.5-Setup-x64.exe` | Windows x64 安装包，118.4 MiB |
| `SHA256SUMS.txt` | 安装包与源码资产的 SHA-256 |
| `Chatbox-Vision-source-v1.23.5.tar.gz` | 完整对应源码（不含 node_modules 与构建产物） |
| `Chatbox-Vision-reviewed-source.zip` | 逐文件审阅包（修改过的文件） |
| `Chatbox-Vision-all-changes.patch` | 相对上游 v1.23.5 的完整补丁 |

## 主要改动

- 知识库原图读取和按需视觉分析（`inspect_knowledge_base_images`）
- 本地 PDF 按页渲染：保留文字检索与页码关联，识图时回到原页
- 细线与图表局部裁剪修正：逐像素扫描、优先完整内容区、找不到可靠边界就保留整块
- 切换视觉模型后立即失效缓存，避免“设置里换了、请求还是旧模型”
- 区分超时、接口拒绝和供应商服务错误；增加阶段耗时日志
- 读图请求显式低推理强度与 8192 token 上限；单图 150 秒、整体 210 秒
- 保留独立安装身份，可与官方 Chatbox 并用

## 本版不包含

- 背景/壁纸相关改动：全窗口背景、GIF/APNG 处理、背景视频、透明度实时预览、显示模式等均未纳入，界面与配置保持官方 v1.23.5 基线。
- 视觉模型的 API 密钥、账户配置、聊天记录、知识库数据库、教材 PDF、壁纸素材。
- 自动更新服务。

## 安装

1. 退出正在运行的 Chatbox Vision（包括托盘进程）。
2. 运行 `Chatbox-Vision-ImageFix-1.23.5-Setup-x64.exe`。
3. 如果沿用原 Chatbox Vision 安装目录，可更新独立版并继续使用原数据。
4. 首次安装且检测到原版数据时，安装器会在原版退出后复制聊天和知识库；不会覆盖原数据。
5. 安装后，在知识库设置中配置支持图片输入的视觉模型和凭据。

更详细的安装与使用说明见 [INSTALL.zh-CN.md](INSTALL.zh-CN.md)。

## 使用前提

- Windows x64
- 一个支持图片输入的视觉模型及其 API 凭据
- 使用 PDF 按页读图时，导入时的原 PDF 需要保留，不要删除、移动或改名

## 已知限制

- 纯扫描件仍需 OCR；应用不会因为配置了视觉模型就自动给整本扫描件做 OCR 和索引。
- 提高 PDF 渲染尺寸只能放大已有像素，不能补回原图本身没有的细节；低分辨率内嵌位图仍可能读不清。
- 密集弯曲虚线、交叉连接点等细节，模型仍可能漏读或读错方向。
- 模拟接口测试只验证“图片确实进入请求”，不代表真实模型的答题准确率。
- 真实 DeepSeek Flash 同题两次验证约 45.5 秒和 43.0 秒完成，关键连接正确；这不是速度或准确率保证。
- 工具层成功不等于整段聊天一定成功，仍受模型、网络和供应商服务状态影响。

## 校验下载

Windows PowerShell：

```powershell
Get-FileHash .\Chatbox-Vision-ImageFix-1.23.5-Setup-x64.exe -Algorithm SHA256
```

Linux / macOS（把 Release 资产下载到同一目录后）：

```bash
sha256sum -c SHA256SUMS.txt
```

安装包 SHA-256：

```text
ea1f63e5b0bca286a3a2dd5e4c958606170ec1479581d61611287273cf456f86
```

## 验证范围

最终构建通过：

- 227 项图片修复相关测试
- 8 项迁移测试
- 完整 TypeScript 检查
- main / preload / renderer 三项构建
- 打包启动检查
- 本机 PDF 读图链路检查

打包后另用隔离配置和本机模拟视觉接口检查了 PDF 原图确实进入请求，以及新增背景视频接口不存在。

## 隐私

仓库和安装包不包含 API 密钥、模型账户配置、聊天记录、知识库数据库、教材 PDF 或壁纸素材。模型配置属于本机数据。

## 许可证与源码

本项目基于 [Chatbox](https://github.com/Bin-Huang/chatbox) v1.23.5，遵循 **GNU GPL v3.0**，见 [LICENSE](LICENSE)。

修改版对应源码随 Release 提供：

- `Chatbox-Vision-source-v1.23.5.tar.gz`：完整对应源码（不含 `node_modules` 与构建产物）
- `Chatbox-Vision-reviewed-source.zip`：修改过的文件逐文件审阅包
- `Chatbox-Vision-all-changes.patch`：相对上游 v1.23.5 的完整补丁

上游源码：<https://github.com/Bin-Huang/chatbox>

本仓库为非官方修改版；Chatbox 名称与相关商标归其各自所有者。
