# JADX-NO-MCP

## [中文 README](README_zh.md)

JADX-NO-MCP is a desktop and CLI helper for APK reverse engineering. It wraps JADX, optional apktool output, Java call graph extraction, native `.so` symbol analysis, packer detection, and AI-friendly Markdown reports into one workflow.

The project is designed for security researchers who want a compact export directory that can be reviewed manually or sent to an AI assistant without dumping an entire decompiled APK into context.

## Features

- GUI and CLI modes
- JADX decompilation with bundled `jadx`
- Optional apktool Smali export
- Early APK packer/protector detection before expensive decompilation
- Manifest, permission, deep link, SDK, URL/IP, dangerous API, and hardcoded secret scanning
- Java method index and caller/callee graph
- Native `.so` analysis with ABI de-duplication
- JNI-first native Markdown output
- Lightweight JNI CFG extraction through `llvm-objdump` or `objdump` when available
- AI-focused output files such as `ai_context.md`, `file_index.md`, and compact security reports

## Requirements

- Python 3.9+
- Java JDK 11+
- Windows, Linux, or macOS

Bundled tools:

- `bin/jadx` / `bin/jadx.bat`
- `lib/jadx-1.5.5-all.jar`
- `lib/apktool.jar`

Optional Python packages:

```bash
pip install ttkbootstrap
```

Optional system tools:

```bash
llvm-objdump --version
objdump --version
```

`llvm-objdump` or `objdump` is only needed for native JNI CFG disassembly. If neither is installed, native reports still include JNI symbols, imports, exports, and risk markers.

## Quick Start

Start the GUI:

```bash
python jadx_ai_analyzer.py
```

Analyze one APK from CLI:

```bash
python jadx_ai_analyzer.py target.apk
```

Analyze a directory of APK files:

```bash
python jadx_ai_analyzer.py apk_dir --batch
```

Specify output directory:

```bash
python jadx_ai_analyzer.py target.apk -o export_for_ai
```

Skip security scan:

```bash
python jadx_ai_analyzer.py target.apk --no-scan
```

Skip native `.so` analysis:

```bash
python jadx_ai_analyzer.py target.apk --no-so
```

Skip Smali export:

```bash
python jadx_ai_analyzer.py target.apk --no-smali
```

Note: Smali export is available through the GUI option. The current CLI flag only controls skipping Smali export.

## CLI Options

```text
apk                  APK file path, or APK directory when --batch is used
-o, --output         Output directory, default: export_for_ai
--jadx               Custom JADX executable path
--cfr                Path to cfr.jar (default: auto-detect bin/cfr.jar)
--decompiler         auto( jar/class -> CFR, falls back to JADX) / cfr / jadx
--batch              Analyze all .apk files in a directory
--no-smali           Skip Smali export
--no-scan            Skip security scanning
--no-so              Skip native .so analysis
```

## Analysis Flow

1. Early packer/protector detection
2. JADX decompilation
3. Optional Smali export
4. Native library extraction
5. Metadata extraction
6. Security scan
7. Java call graph extraction
8. Native `.so` analysis
9. AI-focused report export

In GUI mode, if a known packer/protector is detected, a confirmation dialog asks whether to continue. Selecting `No` stops the analysis before expensive decompilation continues.

## Output Structure

Each run creates a timestamped directory under the configured output path:

```text
export_for_ai/
  appname_YYYYMMDD_HHMMSS/
    ai_context.md
    file_index.md
    report.json
    sources/
    resources/
    lib/
    methods/
    native_analysis/
    security/
```

Important files:

- `ai_context.md` - top-level AI-readable summary
- `file_index.md` - compact navigation index
- `report.json` - structured findings when security results exist
- `methods/*.jsonl` - per-class method graph records
- `native_call_chain.md` - JNI/native summary
- `native_method_index.md` - Java native method declarations and callers
- `native_analysis/*_functions.md` - JNI-first native symbol and CFG summaries
- `security/packer.md` - packer/protector hits grouped by vendor
- `security/permissions.md` - Android permissions
- `security/urls_extracted.md` - extracted URLs and IPs

## Native Analysis

Native analysis is optimized for APKs that ship the same `.so` across multiple ABI folders. The tool selects one copy per library name with this priority:

```text
x86_64 > x86 > arm64-v8a > armeabi-v7a > other
```

For JNI functions, the Markdown report focuses on:

- JNI entry point
- Java class and method mapping
- symbol address and size
- calls and branches parsed from objdump output
- risky imports such as `dlopen`, `dlsym`, `ptrace`, `syscall`, and `system`

Performance guards are applied:

- no whole-library objdump fallback
- max 20 JNI CFG attempts per `.so`
- skip CFG for `.so` files larger than 30 MB
- skip disassembly output larger than 2 MB
- objdump timeout is limited

## Packer Detection

Packer detection is performed before decompilation. It scans APK zip entries and DEX content using rule types adapted from ApkCheckPack:

- exact native path
- native library name
- asset or special file path
- regular expression path match
- DEX string or Java class marker

When a match is found, details are exported to:

```text
security/packer.md
```

## AI Usage

For AI-assisted review, start with:

```text
file_index.md
ai_context.md
security/packer.md
native_call_chain.md
```

Then drill into:

```text
methods/*.jsonl
native_analysis/*_functions.md
security/*.md
```

The reports intentionally avoid large separators and verbose plain text so token usage stays lower.

## Limitations

- Static analysis cannot fully resolve dynamic registration, encrypted DEX, reflection, or runtime-loaded code.
- Native CFG depends on exported JNI symbols and local objdump support.
- Packer detection is signature based and may produce false positives or miss custom protectors.
- Decompiled Java from JADX can be incomplete or inaccurate for heavily obfuscated APKs.

## Legal Notice

Use this tool only on APKs you own, have permission to analyze, or are allowed to inspect under applicable law and policy.

## References

- https://github.com/moyuwa/ApkCheckPack/
- https://github.com/bstee615/tree-climber
- https://github.com/P4nda0s/IDA-NO-MCP
