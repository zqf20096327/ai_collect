# Privacy AI Workstation

**Version:** 2.1.0

Installer for a privacy desk on one Windows or Linux PC. It scans the machine, shows one card per app, and installs only what you accept and what is not already there. It does not create accounts or phone home.

## What you get

| Piece | What it is |
|--------|------------|
| Brave | Privacy browser. DuckDuckGo is also offered on Windows |
| Mullvad | VPN app. You create the account and connect |
| Proton Mail, Drive | Mail and files. You create the Proton account |
| KeePassXC | Password vault stored on this PC |
| Signal | Encrypted desktop chat |
| LibreOffice | Local office suite |
| Ente Auth | Two-factor codes on this device |
| Ollama + LibreChat | Chat with models on this PC, at http://127.0.0.1:3080 |
| Quad9 DNS | Off unless you say yes |

Git and Docker are installed only if you chose local AI and they are missing. On Linux, install Docker Engine yourself. An existing LibreChat checkout is left alone.

After install, run `python privacy-ai-workstation.py guide`. `paw guide` is the same command when `paw` is on your PATH. Both print this README. The guide is below.

## Supported platforms

| Platform | Status |
|----------|--------|
| Windows 10 / 11 | Supported |
| Linux x86_64 / ARM64 | Supported. Docker Engine is manual |
| macOS, phones | Not installed by this tool. Phone notes are in the guide |

## Quick start

Python 3.10+ is required. If it is missing, use the bootstrap script.

**Windows (PowerShell):**

```powershell
.\scripts\bootstrap.ps1
```

**Linux:**

```bash
chmod +x scripts/bootstrap.sh scripts/install.sh
./scripts/bootstrap.sh
```

Or, when Python is already on the machine:

```powershell
python privacy-ai-workstation.py
```

Useful commands:

| Command | What it does |
|---------|----------------|
| `install` | Scan, then ask once per app |
| `install --yes` | Take the defaults. DNS stays off |
| `install --dry-run` | Print the plan. Install nothing |
| `audit` | Hardware and what is already installed |
| `status` | Installed vs missing |
| `progress` | Last run, on this PC only |
| `guide` | How to use the desk, including a phone |
| `start` / `stop` | Start or stop LibreChat. Does not rewrite its config |

Press Enter to accept an app. Private DNS stays off unless you answer yes. `--yes` does not change the default browser or create desktop shortcuts. An interactive install asks, and both default to no.

While an app is installing, a moving bar stays on screen until that install finishes. LibreOffice can take longer than the other apps. It is not stopped at 15 minutes.

## Honest limits

This does not make you invisible. It does not move mail, files, or chats you already have somewhere else. Local AI chats are stored on this PC and are not encrypted by PAW. See [docs/platforms.md](docs/platforms.md) for Docker and LibreChat limits.

## How to use this desk

PAW installs the apps. You decide what you actually use. Until you sign in and switch a habit, the old account still has the data.

Commands below are written as `paw ...`. From this folder, `python privacy-ai-workstation.py ...` does the same thing when `paw` is not on your PATH.

This does not make you invisible. Sites you log into still receive what you type. Mail, photos, and chats already sitting at Google, Microsoft, Apple, or Meta stay there. PAW does not move or delete that pile.

### On this PC

1. Open Mullvad, Proton, and Signal and sign in. Create a KeePassXC vault. Those apps do nothing for you until that is done.
2. Use Brave for everyday browsing. On Windows, DuckDuckGo is there for search. Set Brave as the default browser when you are ready.
3. Connect Mullvad on café Wi-Fi and other networks you do not trust. While it is connected, the ISP sees the VPN, not each site. The site you open still sees the visit. Mullvad uses its own DNS during that session.
4. Send new mail from Proton. Leave old Gmail where it is, or forward only what you choose. Use Proton Drive for new files. Files left in OneDrive, Google Drive, or on the desktop are not picked up for you.
5. Save new passwords in KeePassXC. Stop saving new ones in the browser. Import from Chrome only if you want that copy in the vault.
6. Use Signal for new private chats. Old WhatsApp, iMessage, and SMS threads stay in those apps.
7. Edit documents in LibreOffice when you do not want them opened in Microsoft 365. The file still sits on this PC in the clear unless you encrypt the drive yourself.
8. Move two-factor codes to Ente Auth as you sign into each account. The old authenticator keeps working until you change that account.
9. For local AI, run `paw start`, open http://127.0.0.1:3080, and run `paw stop` when you are done. Those chats stay on this PC. They are not encrypted on disk. Do not publish port 3080 on the internet.
10. Private DNS (Quad9) stays off unless you said yes. It only matters while the VPN is off. It blocks some malware names. It is not a VPN and it does not block ads.

Encrypting the whole drive (BitLocker on Windows Pro, or VeraCrypt) is separate. PAW does not turn it on. It protects the disk when the PC is off. It does not hide chats from you, or from programs running while you are signed in.

Check what is on the machine anytime with `paw status`.

### On a phone

The same idea: use the private app for the thing you are doing now. The phone OS still holds whatever you leave in the old accounts.

**A Pixel, if you are willing to replace the operating system.** GrapheneOS is a hardened Android system for supported Google Pixel phones only. Installing it unlocks the bootloader and erases the phone, so back up anything you need first, then follow the official install guide at https://grapheneos.org/install. After it is on:

- Use Vanadium, the browser that comes with GrapheneOS.
- Install Signal, Mullvad, Proton Mail, Proton Drive, and Ente Auth from each developer’s own release. Add sandboxed Google Play only when an app has no other build.
- Open the KeePassXC vault in an Android KeePass app such as KeePassDX. Copy the vault file yourself. Do not put it in Google Drive or iCloud.
- Optional: Android Private DNS set to `dns.quad9.net`. Mullvad replaces that while the VPN is connected.
- Leave Ollama and LibreChat on the PC. Do not open the chat server to the internet so the phone can reach it from anywhere.

**Any other Android phone.** You can still install Signal, Mullvad, Proton, Ente, Brave, and DuckDuckGo. The system underneath is still the vendor’s Android, not GrapheneOS.

**iPhone.** GrapheneOS cannot be installed. Use Signal, Proton, Mullvad, and Ente from the App Store, and Safari or Brave for browsing. iCloud still holds whatever you leave synced.

Local AI is the piece that stays on the computer. A phone does not get that same offline chat archive.
