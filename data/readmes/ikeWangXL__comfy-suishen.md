# Comfy 随身

用鸿蒙 App 或浏览器连接 Windows 电脑上的 ComfyUI，提交生成任务、查看进度和浏览图片。

## 实际演示

<img src="md/assets/demo/annotated/generated-carousel.svg" width="260" alt="生成页成图轮播，① 图片尺寸、像素量和扩写方式，② 提示词摘要">

① 看图片尺寸、像素量和扩写方式。② 看这张图的提示词摘要。

App 操作演示（约 2 分钟）

https://github.com/user-attachments/assets/b1bc7f0f-bb8e-4f53-94bb-be2b8ace925b

[下载原画质视频（MP4）](https://raw.githubusercontent.com/ikeWangXL/comfy-suishen/main/md/assets/demo/app-demo.mp4)

## 安装前

- **电脑**需要 64 位 Windows 10 或 11、Node.js 26 或更高版本，以及能正常出图的 ComfyUI。Server 启动时需要联网安装依赖。[Node.js 下载](https://nodejs.org/zh-cn/download)
- **鸿蒙设备**需要系统支持 API 26.0.0 或更高版本。侧载时准备一根能传数据的 USB 线。[查看设备 API 版本](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-2600)
- **日常使用**时，手机和电脑连在同一个局域网，电脑上的 ComfyUI 和 Server 都要开着。

## 启动 Windows Server

在仓库页点 **Code → Download ZIP**，解压后双击 `comfy_server/install-start.cmd`。打开控制台，确认 ComfyUI 已连接，选择一个存图目录，再复制「手机连接地址」。[Windows Server 操作手册](md/Windows%20Server%20操作手册.md)

## 使用 Web 版

把控制台显示的「手机连接地址」粘贴到浏览器，用 Server 账号登录。手机、平板和电脑都能用，浏览器所在设备与 Server 需要在同一个局域网。

## 安装鸿蒙 App

在 GitHub 的 **Releases** 里下载 `Comfy-Suishen-unsigned.hap`，用 Windows 电脑签名并安装到鸿蒙设备。[鸿蒙 App 安装说明](md/鸿蒙%20App%20安装说明.md)

打开 App，输入刚才复制的手机连接地址，用控制台的账号登录。[鸿蒙 App 操作手册](md/鸿蒙%20App%20操作手册.md)

如果生成页没有工作流，到控制台「图库与档案」上传从 ComfyUI 导出的 API 格式 JSON。需要在手机上调整参数时，可以对照示例给工作流加标记。[下载参考工作流](https://github.com/ikeWangXL/comfy-suishen/releases/download/v1.0.0-preview/Comfy-Suishen-Workflow-v1.1.json) · [工作流适配指南](md/ComfyUI%20工作流适配指南.md)

## App 出图与临时文件

为了避免 App 出图在 ComfyUI 的 `output` 和用户图库各留下一个长期保存的原图，Server 在提交任务时，将执行副本里的 ComfyUI 内置 `SaveImage` 节点换成 `PreviewImage`。ComfyUI 先把 PNG 写到 `temp`，Server 再读取原图并保存到用户指定的图库。

任何用户上传的工作流都适用这条规则。Server 按节点类型识别内置 `SaveImage`，节点名称和编号不影响识别。上传的 JSON 文件保持原样，在 ComfyUI 网页手动运行该工作流时仍按原配置保存。自定义插件的保存节点不在自动替换范围内。

**已知限制**。入库后，ComfyUI 的临时副本仍会占用磁盘空间，直到 ComfyUI 在启动或正常退出时清理临时目录。长时间不重启时，临时图仍可能累积。清理临时目录不会影响已入库的原图，也不会清理 `output` 中已有的历史文件。

## 交流与合作

有想法想讨论，或者想一起做点东西，欢迎发邮件给我。[805038230@qq.com](mailto:805038230@qq.com)
