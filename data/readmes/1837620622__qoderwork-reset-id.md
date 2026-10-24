# QoderWork CN + QoderCN 设备ID重置 & 请求拦截工具

QoderWork CN（阿里桌面 AI 智能体）和 QoderCN（代码编辑器）的本地设备标识重置 & 网络请求拦截方案。

## 为什么改 device-id 还不够？

QoderWork CN 使用**多层设备指纹系统**，包括：

| 层级 | 内容 | 可修改性 |
|------|------|----------|
| 文件级 ID | `machine-id`、`installation_id` | ✓ 可修改 |
| 应用缓存 | `device_id_salt`、`blob_storage` | ✓ 可修改 |
| RUM 遥测 | `_arms_uid`（阿里云监控） | ✓ 可修改 |
| UMID SecurityGuard | C 库基于硬件序列号生成签名令牌 | ✗ 不可伪造 |
| **硬件序列号** | macOS 序列号、Hardware UUID | ✗ **不可变** |

> 即使修改了所有本地文件，QoderCN 后台服务仍可从**硬件序列号重新生成 machine-id**。

## 方案一：本地 ID 重置（仅改文件 ID）

修改本地存储的设备标识文件，适合快速重置。

### macOS

```bash
chmod +x reset_qoderwork_id.sh
./reset_qoderwork_id.sh
```

### Windows

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\reset_qoderwork_id.ps1
```

> 仅替换 ID 值，不删文件，不丢失账号信息。

---

## 方案二：请求拦截代理（推荐）

网络层面拦截 API 请求，替换设备标识，使服务器看到**全新的设备身份**。

### 原理

在 QoderWork CN 和服务器之间建立一个本地代理，自动拦截并替换：

- `X-Machine-Id` 请求头 → 替换为随机 UUID
- URL 参数中的 `machine_id` → 替换为随机 UUID
- 请求体中的设备字段 → 替换为随机 UUID
- 响应体中的 UUID → 替换为随机 UUID

### macOS 使用

```bash
# 1. 安装 mitmproxy
brew install mitmproxy

# 2. 启动拦截代理
chmod +x start_proxy.sh
./start_proxy.sh

# 3. 设置系统代理（WiFi → 高级 → 代理）
#    网页代理: 127.0.0.1:8080
#    安全网页代理: 127.0.0.1:8080

# 4. 首次需要信任证书：访问 http://mitm.it 下载安装

# 5. 打开 QoderWork CN 并登录/注册新账号

# 6. 完成后关闭代理，关闭系统代理
```

### Windows 使用

```powershell
# 1. 安装 mitmproxy
winget install mitmproxy

# 2. 启动拦截代理
mitmproxy -s qoder_intercept.py --listen-port 8080

# 3. 设置系统代理
#    设置 → 网络和 Internet → 代理 → 手动代理
#    HTTP: 127.0.0.1:8080
#    HTTPS: 127.0.0.1:8080

# 4. 首次信任证书

# 5. 打开 QoderWork CN 并登录

# 6. 完成后关闭代理
```

## 文件说明

| 文件 | 说明 |
|------|------|
| `reset_qoderwork_id.sh` | macOS 本地 ID 重置脚本 |
| `reset_qoderwork_id.ps1` | Windows 本地 ID 重置脚本 |
| `qoder_intercept.py` | mitmproxy addon，网络层拦截替换设备标识 |
| `start_proxy.sh` | macOS 代理启动脚本 |

## 注意事项

- 代理方案需要信任 mitmproxy CA 证书（有安全风险，用完即关）
- 账号认证文件不受影响，登录状态保留
- 建议配合新账号注册使用
