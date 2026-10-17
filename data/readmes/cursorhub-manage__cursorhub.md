# 🚀 Cursor 账号管理器

> 一款强大的 Cursor AI 编辑器账号管理工具

[![GitHub Release](https://img.shields.io/github/v/release/cursorhub-manage/cursorhub?style=flat-square)](https://github.com/cursorhub-manage/cursorhub/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/cursorhub-manage/cursorhub/total?style=flat-square)](https://github.com/cursorhub-manage/cursorhub/releases)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-blue?style=flat-square)](https://github.com/cursorhub-manage/cursorhub/releases)

---

## 📥 下载最新版本

### 👉 [点击这里下载最新版本](https://github.com/cursorhub-manage/cursorhub/releases/latest)

| 平台 | 下载链接 | 说明 |
|------|---------|------|
| 🍎 **macOS** | [下载 .dmg](https://github.com/cursorhub-manage/cursorhub/releases/latest) | 支持 macOS 10.15+ |
| 🪟 **Windows** | [下载 .exe](https://github.com/cursorhub-manage/cursorhub/releases/latest) | 支持 Windows 10/11 |
| 🐧 **Linux** | [下载 .AppImage](https://github.com/cursorhub-manage/cursorhub/releases/latest) | 支持主流 Linux 发行版 |

---

## 界面预览

![CursorHub 界面预览](./assets/preview.png)

## 🚀 快速开始

### 1. 下载安装

前往 [Releases 页面](https://github.com/cursorhub-manage/cursorhub/releases/latest) 下载对应平台的安装包。

### 2. 安装应用

#### macOS
```bash
# 打开下载的 .dmg 文件
# 拖拽应用到 Applications 文件夹
# 首次打开需要在"系统偏好设置 → 隐私与安全性"中允许
```

#### Windows
```bash
# 运行下载的 .exe 文件
# 按照安装向导完成安装
```

#### Linux
```bash
# 赋予执行权限
chmod +x cursorhub-*.AppImage

# 运行应用
./cursorhub-*.AppImage
```

### 3. 开始使用

1. 点击"导入账号"按钮
2. 粘贴 Cursor 的 Cookie 或 Token
3. 解析并导入账号
4. 点击"应用"切换账号

---

## 📖 使用教程

### 导入账号

支持以下格式：

1. **WorkosSessionToken** 格式
```
user_abc123::eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

2. **JWT Token** 格式
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

3. **混合导入** - 支持多行粘贴，自动识别和去重

### 应用账号

1. 在账号列表中选择目标账号
2. 点击"应用"按钮
3. 应用会自动：
   - 检测 Cursor 是否运行
   - 关闭 Cursor（如需要）
   - 重置机器ID
   - 写入新的 Token
   - 提示重新启动 Cursor

---

## ❓ 常见问题

### Q: 支持哪些平台？

A: 支持 macOS、Windows 和 Linux 主流操作系统。

---

## 🔗 相关链接

- 📦 [Releases 页面](https://github.com/cursorhub-manage/cursorhub/releases)
- 📖 [使用文档](https://github.com/cursorhub-manage/cursorhub/blob/main/README.md)
- 🐛 [问题反馈](https://github.com/cursorhub-manage/cursorhub/issues)
- 💬 [讨论区](https://github.com/cursorhub-manage/cursorhub/discussions)

---

## 最新版本

前往 [Releases](https://github.com/cursorhub-manage/cursorhub/releases/latest) 查看最新版本和更新内容。
