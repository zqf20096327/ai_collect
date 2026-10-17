# 🤖 The Ollama Uninstall Guide macOS/Windows/Linux

Currently, the official installation scripts make it incredibly easy to get Ollama running, but there is no readily discoverable documentation for cleanly uninstalling it.

I propose adding a dedicated `Uninstall.md` file to the repository. Placing this in its own explicitly named file makes it much easier for users to find when they need to remove the software or do a clean reinstall, rather than burying it inside a general troubleshooting guide.

Below, you will find the accurate, reverse-engineered manual teardown commands for macOS, Windows, and Linux. **I have also included interactive script files (`.sh` and `.ps1`) in this folder if you prefer an automated one-click removal.**

>[!WARNING]
> **Regarding model data:** The optional manual commands below to remove the `.ollama` directories will completely wipe your downloaded models and cache. If using the automated scripts, you will be interactively prompted to keep or delete these files.
>
> **Package Manager Note:** These teardowns and scripts are designed *only* for users who installed Ollama via the official download links or `curl` scripts. If you installed Ollama using a package manager (like Homebrew, Winget, Chocolatey, or Docker), please use your package manager's native uninstallation commands instead.

---

## 🍎 macOS

**The Setup:** `curl -fsSL https://ollama.com/install.sh | sh`
**The Reality:** The Mac script is essentially a downloader. It downloads a compressed `.zip` file containing `Ollama.app`, extracts it directly into `/Applications`, and creates a symbolic link in `/usr/local/bin` so the terminal recognizes the `ollama` command. It stores downloaded model blobs in `~/.ollama`.

**The Accurate Teardown:**

```bash
# 1. Kill any running Ollama processes
pkill -f ollama

# 2. Remove the symlink created by the script
sudo rm /usr/local/bin/ollama

# 3. Remove the core application bundle
sudo rm -rf /Applications/Ollama.app

# 4. Wipe the model directory and cache
rm -rf ~/.ollama
```

---
**The Automated Method (Using the Script):**
If you prefer not to enter the commands manually, you can use the included `uninstall-mac.sh` script. This script executes the teardown safely and will interactively ask if you want to keep or delete your downloaded models.

- Open Terminal and navigate to the directory containing the script.
- Make it executable: `chmod +x uninstall-mac.sh`
- Run the script: `./uninstall-mac.sh`

>[!NOTE]
> You will be prompted for your administrator password to remove the application bundle.
---
>[!TIP]
> ✅ Verify Uninstallation
>
> To confirm that Ollama has been completely removed from your system, and to check if any heavy model weights were left behind, run this quick check in your terminal:

```bash
if ! command -v ollama &> /dev/null; then if [ -d ~/.ollama ]; then echo -e "✅ Ollama app is removed, but model weights remain.\n💡 To delete them, run: rm -rf ~/.ollama"; else echo "✅ Ollama and all model weights have been completely removed."; fi; else echo "❌ Ollama is still installed."; fi
```

---

## 🪟 Windows

**The Setup:** `irm https://ollama.com/install.ps1 | iex`
**The Reality:** The PowerShell script does not install Ollama manually. It simply downloads `OllamaSetup.exe` into a temporary directory and executes it with a silent flag (`/SILENT`). The `.exe` then writes the core application into your Local AppData folder and registers an official uninstaller (`unins000.exe`) with Windows. Models are saved in `C:\Users\<YourUsername>\.ollama`.

**The Accurate Teardown (via PowerShell as Administrator):**

```powershell
# 1. Kill the background Ollama processes
Stop-Process -Name "ollama" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "ollama app" -Force -ErrorAction SilentlyContinue

# 2. Trigger the official uninstaller exactly as Windows would, but silently
$UninstallExe = "$env:LOCALAPPDATA\Programs\Ollama\unins000.exe"
if (Test-Path $UninstallExe) {
    Start-Process -FilePath $UninstallExe -ArgumentList "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART" -Wait
}

# 3. Clean up any orphaned AppData folders left behind
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Programs\Ollama" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Ollama" -ErrorAction SilentlyContinue

# 4. Wipe the downloaded models
Remove-Item -Recurse -Force "$env:USERPROFILE\.ollama" -ErrorAction SilentlyContinue
```

---
**The Automated Method (Using the Script):**
If you prefer not to enter the commands manually, you can use the included `uninstall-windows.ps1` script. This script triggers the silent uninstaller, cleans up orphaned folders, and interactively asks if you want to keep or delete your downloaded models.

**Method 1 (File Explorer):** Right-click the `uninstall-windows.ps1` and select **Run with PowerShell**. Click "Yes" if prompted by UAC.
**Method 2 (Terminal):** Open PowerShell as Administrator, navigate to the script's folder, and run: `.\uninstall-windows.ps1`

---
>[!TIP]
> ✅ Verify Uninstallation
>
> To confirm that Ollama has been completely removed from your system, and to check if any heavy model weights were left behind, run this quick check in PowerShell:

```powershell
if (!(Get-Command ollama -ErrorAction SilentlyContinue)) { if (Test-Path "$env:USERPROFILE\.ollama") { Write-Host "✅ Ollama app is removed, but model weights remain.`n💡 To delete them, run: Remove-Item -Recurse -Force `"$env:USERPROFILE\.ollama`"" -ForegroundColor Yellow } else { Write-Host "✅ Ollama and all model weights have been completely removed." -ForegroundColor Green } } else { Write-Host "❌ Ollama is still installed." -ForegroundColor Red }
```

---

## 🐧 Linux

**The Setup:** `curl -fsSL https://ollama.com/install.sh | sh`
**The Reality:** The Linux script does heavy system-level configuration. It downloads the raw executable to `/usr/local/bin/ollama`, creates a dedicated background `ollama` user account (so the service can run securely without your personal user account), generates a `systemd` service file in `/etc/systemd/system/`, and sets the default model storage to `/usr/share/ollama`.

**The Accurate Teardown:**

```bash
# 1. Stop and disable the background service
sudo systemctl stop ollama
sudo systemctl disable ollama

# 2. Remove the systemd service file and refresh the daemon
sudo rm /etc/systemd/system/ollama.service
sudo systemctl daemon-reload

# 3. Remove the binaries
sudo rm $(which ollama)
# (Optional fallback if the script placed libraries here)
sudo rm -rf /usr/local/lib/ollama 

# 4. Delete the dedicated system user and group created by the script
sudo userdel ollama
sudo groupdel ollama

# 5. Wipe the root-level model directory
sudo rm -rf /usr/share/ollama

# 6. Wipe any local user models (if you ran models without the system service)
sudo rm -rf ~/.ollama
```

---
**The Automated Method (Using the Script):**
If you prefer not to enter the commands manually, you can use the included `uninstall-linux.sh` script. This script safely stops the systemd services, removes the binaries and dedicated system user, and interactively asks if you want to keep or delete your downloaded models.

- Open Terminal and navigate to the directory containing the script.
- Make it executable: `chmod +x uninstall-linux.sh`
- Run the script: `./uninstall-linux.sh`

>[!NOTE]
> You will be prompted for your `sudo` password to cleanly remove the background services and system user.
---

>[!TIP]
> ✅ Verify Uninstallation
>
> To confirm that Ollama has been completely removed from your system, and to check if any heavy model weights were left behind, run this quick check in your terminal:

```bash
if ! command -v ollama &> /dev/null; then if [ -d ~/.ollama ] || [ -d /usr/share/ollama ]; then echo -e "✅ Ollama app is removed, but model weights remain.\n💡 To delete them, run: sudo rm -rf ~/.ollama /usr/share/ollama"; else echo "✅ Ollama and all model weights have been completely removed."; fi; else echo "❌ Ollama is still installed."; fi
```

---

## ⚠️ Disclaimer

> [!CAUTION]
> This is provided "as is" without warranty of any kind. I am not responsible for any damage, data loss, or issues caused by the use of this information. **Use it at your own risk.**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

