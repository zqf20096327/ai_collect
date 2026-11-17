# Libzora

[![Release](https://github.com/kingstacker/Libzora/actions/workflows/release.yml/badge.svg)](https://github.com/kingstacker/Libzora/actions/workflows/release.yml) [![Latest release](https://img.shields.io/github/v/release/kingstacker/Libzora)](https://github.com/kingstacker/Libzora/releases/latest)

[Official website](https://libzora.stacker.beauty)

[简体中文](README.zh-CN.md) · **English**

Libzora is a quiet, cross-platform ebook and Kindle manager built with Avalonia. It combines a local library, reading, annotations, AI assistance, format conversion, and Kindle transfer in one desktop app.

![Libzora library on macOS with six public-domain books](website/assets/library-en.webp?v=20261116-public-domain)

The desktop previews are captured from the macOS app and the mobile preview from the iOS app. The README library previews show the same six public-domain books from the local public-domain collection; English pages use the English app UI.

## Platform status

| Platform | Status | Notes |
| --- | --- | --- |
| Windows | ✅ Tested | Stable; minor fixes in progress |
| macOS | 🟡 Initial testing | Packages available; fixes and testing in progress |
| iOS | 🚧 In development | Initial version in development |
| Android | 🚧 In development | Initial version in development |
| Linux | ⏳ Pending testing | Full testing not yet done |

## Platform previews

| macOS | iOS |
| :---: | :---: |
| <img src="website/assets/macos-library-en.webp?v=20261116-public-domain" alt="Libzora library on macOS" width="460"> | <img src="website/assets/ios-library-en.webp?v=20261116-public-domain" alt="Libzora library on iOS" width="190"> |
| Library | Library |

## Features

- **Library** — Import EPUB, PDF, MOBI, AZW3, and TXT; TXT encoding and chapter/volume headings are detected automatically and converted to EPUB without Calibre. Manage metadata, covers, tags, collections, search, and reading status. When a book with the same title is imported, choose to add the format, keep it separately, or skip; deleted content goes to a recoverable trash first.
- **Kreader** — Open EPUB, PDF, and DRM-free AZW3 in the app; AZW3 uses the built-in KF8 reader without Calibre. Paginated or scrolling reading, table of contents, bookmarks, search, annotations, typography settings, reading progress, and read-aloud on Windows, Linux, and macOS (Linux requires mpv, ffplay, VLC, or GStreamer; macOS uses the built-in afplay).
- **PDF reading** — First-page library covers, continuous scrolling, single-page and two-page reading, fit-width/page controls, sharp zoom and 90° rotation. Supports selectable text, six underline/highlight styles, editable comments, and page annotations at arbitrary PDF positions through the page-note icon or right-click. Pages appear before full-book text indexing finishes; only visible regions are rendered at the screen's pixel density. Search, bookmarks and reading position use the same local reading data as EPUB. Scanned pages support viewing and page notes; OCR is not included.
- **AI assistant** — Ask questions about the current book, summarize chapters, explain selections, and choose from discovered models through DeepSeek, OpenAI, or compatible endpoints. Requests use relevant local excerpts only.
- **Kindle** — Detect USB/WPD/MTP devices, transfer books, manage fonts and dictionaries, and import `My Clippings.txt`.
- **Tools and sync** — Calibre conversion, encrypted local backups, protected credentials, and cross-device sync with your own S3 / WebDAV, free in the current version without an account. Account registration is not live yet. The account service manages identity and feature entitlements, not book storage.

## Download

Download the latest Windows, Linux, or macOS package from the [official site](https://libzora.stacker.beauty/#downloads); it automatically selects the latest stable release.

Backup download: [GitHub Releases](https://github.com/kingstacker/Libzora/releases).

Calibre is required separately for format conversion. Official GitHub releases provide Windows, Linux, and macOS packages. macOS builds support macOS 12 or later on Intel and Apple Silicon; when Apple distribution credentials are not configured, the DMG is ad-hoc signed and the first launch needs the Gatekeeper steps in [docs/macos-adhoc-install.md](docs/macos-adhoc-install.md).

The **Settings → Diagnostics** page checks the data directory, PDF parser, WebView, Calibre, TTS, and Kindle services, and is the first place to look for cross-platform issues. The library trash can restore a deleted book or a single format, and permanently purge items after confirmation; trash contents are included in local backups.

## Free / Trial / Lifetime

**The current client release is free**: full local features and cross-device sync with your own S3 / WebDAV work without an account, and registration is not available yet. The table below describes the planned account-service tiers, not an available sign-up or purchase flow.

| Plan | Price and duration | Features |
| --- | --- | --- |
| **Free** | Free forever | Full local reading and library management, USB Kindle features, plugins, and your own AI APIs |
| **Trial** | 7-day free trial, once per account; claimed explicitly by the user | All Free features plus cross-device books, reading progress, bookmarks, and annotations through your own S3 / WebDAV |
| **Lifetime** | ¥88 once, permanent; no renewals | All Free features plus permanent access to the same S3 / WebDAV cross-device sync |

Every account allows up to **6 simultaneously signed-in devices**. No plan provides official cloud storage or official cloud sync. The account service handles identity and feature entitlements only and does not receive your books. You configure your own storage and cover its storage and traffic costs; AI service costs follow your provider's terms. Trial expiry disables only paid sync features and does not delete data in your own storage or your local library. A purchased Lifetime remains valid when a trial ends.

Lifetime entitlements bind directly to the account. Protected administrators enable permanent access based on external authorization; clients can only refresh and validate entitlements, not grant themselves access. Purchase and enablement methods follow actual channel announcements; refresh entitlements after enablement. The existing 7-day and ¥88 rules remain unchanged, without announcing an available purchase channel, automatic payment, or payment gateway. The account service retains only necessary account/recovery, region, 6-device/session security, trial, entitlement validation/expiry, deactivation, and protected admin grant/revocation/audit functions. It does not process products, orders, or payments, issue/redeem/manage activation codes, accept feedback screenshots, or provide cloud objects or quota statistics.

Historical paid time-limited entitlements remain valid until their original expiry; they do not become permanent. Self-service account closure becomes password-and-typed-confirmation **account deactivation** and revokes sessions, retaining necessary license/audit records—not deleting server data. Local and user-provided storage data are retained; existing databases, ledgers, historical redeemed codes, and cloud files are not migrated or deleted as part of this change. Historical codes and ledgers are retained only for necessary read-only compatibility, not renewed redemption.

## Sync with your own S3 / WebDAV

Cross-device sync currently works without signing in: configure your own S3 or WebDAV storage and start syncing. Account registration is not available yet. Once the account service ships, accounts, entitlements, sessions, local libraries, and sync namespaces will remain independent between the China and International regions. See [account server setup](docs/account-server.md).

Choose **S3** or **WebDAV** in **Settings → Data & sync → Cloud sync**, enter your own connection details, and select **Save settings**. Book and snapshot transfers connect directly to your storage, not the account server. Both providers retain their own addresses and credentials. Manual, startup, exit, and scheduled sync use the saved selection.

For WebDAV, enter the URL of an existing directory, such as `https://dav.example.com/dav/`, and credentials if required. Some services require an app password. Libzora creates a sync subdirectory named `libzora` by default; change it in Advanced options. The connection test verifies read/write access and removes its test file. The server must support standard PROPFIND, MKCOL, GET, PUT, MOVE, and DELETE operations. Completed uploads are published with MOVE so interrupted transfers do not replace existing snapshots.

The sync subdirectory, encryption, scheduling, and transfer options are shared between providers within each region. Devices syncing the same directory need the same encryption key; use a new subdirectory when changing keys. Connection profile exports include only the selected provider's credentials. Existing `.libzora-s3.json` profiles remain supported; WebDAV profiles use `.libzora-webdav.json`.

Every `.libzora` data backup is encrypted with the locally configured sync key, including books, reading records, and library metadata. Import and export first prompt you to set that key if it is missing, even when cloud sync is disabled. To restore on another device, configure the original key before importing. Backups exclude connection passwords, account sessions, and the key itself. The key is never uploaded or recovered by the server; forgetting it makes existing encrypted data unreadable. Older plaintext backup files are rejected. See [encrypted backup details](docs/backup-encryption.md).

## Public-domain test books

The [公版书](公版书/README.md) folder contains the six EPUBs shown in the screenshots. Download and import them to test the library, reading, annotations, and Kindle transfers. Sources and SHA-256 checksums are included.

## Run from source

Requires the exact [.NET SDK 10.0.400](https://dotnet.microsoft.com/download/dotnet/10.0) pinned by `global.json`.

Windows (PowerShell):

```powershell
dotnet restore Libzora.sln -p:Platform=x64
dotnet build Libzora.sln -p:Platform=x64
dotnet test Libzora.sln --no-build -p:Platform=x64
# Run the slow regression suite explicitly before a release
dotnet test Libzora.sln --no-build -p:Platform=x64 -p:RunSlowTests=true
dotnet run --project src\Libzora.Desktop.Windows\Libzora.Desktop.Windows.csproj -p:Platform=x64
```

macOS:

```bash
dotnet build src/Libzora.Desktop.MacOS/Libzora.Desktop.MacOS.csproj
dotnet test tests/Libzora.Tests/Libzora.Tests.csproj
dotnet run --project src/Libzora.Desktop.MacOS/Libzora.Desktop.MacOS.csproj
```

Linux uses the same commands with `Libzora.Desktop.Linux` in place of `Libzora.Desktop.MacOS`.

Build a macOS app bundle for either architecture:

```bash
# Apple Silicon
bash scripts/build-macos-release.sh 1.1.3 artifacts/macos osx-arm64
# Intel
bash scripts/build-macos-release.sh 1.1.3 artifacts/macos osx-x64
# Universal (one package for both architectures)
bash scripts/build-macos-release.sh 1.1.3 artifacts/macos osx-universal
```

Every command works on either architecture: the bundled libmtp and libusb are built from source for the target (cross-compiled with the macOS SDK when it differs from the host), so an Intel Mac can produce the arm64 package and vice versa. CI uses `macos-26` for Apple Silicon and `macos-15-intel` for Intel, both pinned to Xcode 26.3; the ARM64 host image also matches the Icon Composer toolchain requirements.

`osx-universal` produces a single `Libzora.app` that starts natively on both Intel and Apple Silicon. A self-contained .NET publish contains architecture-specific native and ReadyToRun assemblies that cannot be combined into one file set, so the bundle carries both complete payloads under `Contents/MacOS/x86_64` and `Contents/MacOS/arm64` and a universal launcher execs the matching one. Expect roughly twice the download size of a single-architecture package.

The default test run skips expensive UI, rendering, and GC-stress cases while keeping core, platform, device, and a small UI smoke set. The skipped tests remain in the repository and can be enabled with `RunSlowTests=true`.

Linux also requires WebKitGTK and Secret Service. See [cross-platform notes](docs/cross-platform.md) for platform packages and signing details. Mobile heads live in `Libzora.Mobile.sln`; see [mobile notes](docs/mobile-skeleton.md) for workloads and simulator commands.

## Referenced technologies

- **Feature references and tools** — [Calibre](https://github.com/kovidgoyal/calibre) and [KFX Input](https://www.mobileread.com/forums/showthread.php?t=291290).
- **Runtime** — [Avalonia](https://github.com/AvaloniaUI/Avalonia), [CommunityToolkit.Mvvm](https://github.com/CommunityToolkit/dotnet), [EF Core](https://github.com/dotnet/efcore), and [PdfPig](https://github.com/UglyToad/PdfPig).
- **Testing** — [xUnit](https://github.com/xunit/xunit) and [VSTest](https://github.com/microsoft/vstest).

## Code contributors

Thank you to the developers who have submitted code and improvements to Libzora:

- sonianmu (Mutro)

## Acknowledgments

- Community: [LINUX DO](https://linux.do/?tl=en)
- Public-service site: any

## License

[GPL-3.0 License](LICENSE). Third-party components and bundled fonts retain their own licenses.

See [third-party notices](THIRD-PARTY-NOTICES.md) and the
[license/source distribution maintenance guide](docs/third-party-licenses.md).
