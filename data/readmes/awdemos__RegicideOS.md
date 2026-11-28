<div align="center">

# RegicideOS

AI-native. Rust-first. Immutable Linux.

> Converge and conquer.

> **Development status:** The Dagger and Catalyst pipeline builds stage4, SquashFS, QCOW2, and live ISO artifacts. The repository includes a populated COSMIC overlay and the complete source gate passes. Full production certification is not claimed. Disposable OS-image certification is a separate release gate, and bare-metal installation is unverified. See [STATUS.md](STATUS.md) for current evidence.

[![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://kernel.org/)
[![Btrfs](https://img.shields.io/badge/Btrfs-8db600?style=for-the-badge&logo=linux&logoColor=white)](https://btrfs.wiki.kernel.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)

**Latest release:** [RegicideOS v0.0.1](https://github.com/awdemos/RegicideOS/releases/tag/v0.0.1). Bootable live ISOs for RegicideOS (Gentoo) and RegicideOSArch (Arch), released in split chunks with SHA256 checksums because GitHub caps individual assets at 2 GiB.

[Install](#install-and-build) · [Roadmap](#roadmap) · [Contributing](#contributing) · [Download v0.0.1](https://github.com/awdemos/RegicideOS/releases/tag/v0.0.1)

</div>

## Why RegicideOS

RegicideOS is a Gentoo stage4 with [COSMIC](https://github.com/pop-os/cosmic-epoch) as the default desktop. The root filesystem is a read-only Btrfs volume, and stateful data lives on separate subvolumes. Updates are prepared offline, verified, and swapped atomically. The live image is a SquashFS produced by the Catalyst and Dagger pipeline, so what boots is byte-for-byte what was validated.

The direction is plain: move system components to Rust where possible, and add AI capabilities at the system level. Dagger caching reuses compiled stages, so later builds take far less time than the first run. Benefits come first: a steady base, verified images, and a build you can repeat.

"Regicide" refers to the kings of the current operating system marketplace: unsafe programming languages, bloated legacy stacks, and human-centric system administration. The work is built in the open.

Full production certification is not claimed. The current Gentoo image ships 905 packages, including the local `emerge` toolchain; the Arch variant ships 536 binary packages without that toolchain.

## One family, one build system

RegicideOS is the primary Gentoo base. [RegicideOSArch](https://github.com/awdemos/RegicideOSArch) is the faster Arch variant with a WSL path and an ARM64 path. RegicideOSArch uses binary `pacman` packages and ships a dedicated `dagger_pipeline_wsl.py` pipeline that produces a WSL2-ready rootfs tarball for `wsl --import`.

Both distributions share one build discipline. Dagger drives repeatable, cached stages. Catalyst and Dagger produce the stage4 tarball, SquashFS image, QCOW2 image, and live ISO. Published images carry SHA256 checksums.

regicideDB is the Turso-backed per-agent database and audit substrate. It keeps agent state and an audit record alongside the build and install work.

## Security is a practice

Security is a set of mechanisms you can check, not a badge. RegicideOS uses an immutable Btrfs root, snapshot and rollback tooling through `regicide-update`, `regicide-image`, and `regicide-rollback`, SHA256-verified images, and installer preflight that stages and verifies an image before partitioning. Archive extraction is validated, with numeric owners preserved and rollback on handoff failure. BtrMind ships monitor-only by default. Containers move toward a rootless direction.

Status gates are explicit. Final security review, disposable OS-image certification, fresh current-source image certification, and bare-metal installation are not claimed. See [STATUS.md](STATUS.md) for current evidence.

Safety notes in short form:

- Use a 64-character hexadecimal SHA256 digest for normal installs. `--allow-unverified` is development-only.
- `regicide-cosmic.img` is the ROOTS filesystem, not a bootable USB image.
- Write the LUKS passphrase file with `printf`, not `echo`. A trailing newline becomes part of the key.
- Dagger needs a rootful Docker or Podman runtime. Rootless Podman cannot create the `dagger0` bridge. A root-run pipeline needs `mksquashfs` on the host.
- BtrMind service defaults to dry-run monitoring. Real cleanup requires explicit root invocation and `dry_run = false`.

## Install and build

The installer implements a basic UEFI install flow. Bare-metal installation remains unverified, and fresh current-source image certification is pending. See [STATUS.md](STATUS.md).

### Requirements

- 64-bit x86 processor
- 12GB disk space minimum (20GB recommended)
- UEFI firmware
- Internet connection
- Existing Linux live environment (e.g., Fedora Workstation) for bare-metal installs

### Verified command patterns

Run image installation and real cleanup commands as root. Replace placeholder paths, digests, and whole-disk devices with reviewed values. Use a 64-character hexadecimal SHA256 digest. `--allow-unverified` is development-only.

```bash
installer --image /path/to/regicide-cosmic.img --checksum <64-hex-digest> /dev/sdX
regicide-image install /path/to/image.tar.xz --checksum <64-hex-digest>
regicide-image install /path/to/image.tar.xz --allow-unverified
btrmind --dry-run --config /etc/btrmind/config.toml run
sudo btrmind --config /etc/btrmind/config.toml cleanup
```

Remote `Manifest.toml` version entries must contain `sha256`; missing or malformed digests fail preflight. Installer metadata requests have total deadlines, and downloads use connection and stalled-response timeouts without a total deadline on a healthy slow body. `regicide-image` stages into a validated directory before handoff. BtrMind is monitor-only by default.

### Build from source

Build with the Catalyst scripts in `build-system/catalyst/` or the Dagger pipeline. Dependencies:

```bash
emerge -av dev-util/catalyst app-arch/pixz sys-fs/squashfs-tools
emerge -av app-emulation/qemu sys-fs/cryptsetup
```

#### Stage4 and SquashFS

Catalyst on a Gentoo host:

```bash
cd build-system/catalyst
sudo ./build.sh
```

Dagger with a rootful Docker or Podman runtime:

```bash
DAGGER_PROGRESS=plain dagger run python build-system/dagger_pipeline.py --plain
```

> The Dagger engine image needs to create the `dagger0` bridge, so it
> cannot run under **rootless Podman**. If your default `docker` endpoint is a
> rootless Podman socket, start the rootful Podman socket and point Dagger at it:
>
> ```bash
> sudo systemctl enable --now podman.socket
> DOCKER_HOST=unix:///run/podman/podman.sock sudo -E dagger run python build-system/dagger_pipeline.py --plain
> ```
>
> A root-run pipeline needs `mksquashfs` on the host. On Gentoo install `sys-fs/squashfs-tools`; on Fedora or Arch install `squashfs-tools`.

The pipeline splits the build into six cacheable stages in `build-system/catalyst/stages/`. The COSMIC stage compiles many Rust packages from source, so the first run can take hours. Later runs reuse cached stages and the `distfiles` and `binpkgs` cache volumes. Use `--plain` or `DAGGER_PROGRESS=plain` for plain text logs. Two build modes:

```bash
# Main pipeline (default): reuse binary packages via --usepkg for fast rebuilds
DAGGER_PROGRESS=plain dagger run python build-system/dagger_pipeline.py --plain

# From-source pipeline: full recompile; still populates the binpkg cache volume
REGICIDE_USE_BINPKGS=0 DAGGER_PROGRESS=plain dagger run python build-system/dagger_pipeline.py --plain
```

> For faster local builds without Sigstore signing, add `--skip-sign`:
> ```bash
> DAGGER_PROGRESS=plain dagger run python build-system/dagger_pipeline.py --plain --skip-sign
> ```
> This skips cosign artifact signing, which needs interactive browser authentication for keyless mode or a cosign key pair for local signing.

Both methods produce:

- `build-system/catalyst/output/stage4-amd64-systemd-cosmic.tar.xz`
- `build-system/catalyst/output/regicide-cosmic.img` (live SquashFS image)

#### QCOW2 VM image

```bash
# Unencrypted
sudo ./build-vm-image.sh \
    --squashfs output/regicide-cosmic.img \
    output/stage4-amd64-systemd-cosmic.tar.xz \
    output/regicide-cosmic.qcow2 20G

# Encrypted with LUKS2 (recommended)
printf 'regicide-secure-test' > /tmp/regicide-passphrase.txt
sudo ./build-vm-image.sh \
    --encrypt --passphrase-file /tmp/regicide-passphrase.txt \
    --squashfs output/regicide-cosmic.img \
    output/stage4-amd64-systemd-cosmic.tar.xz \
    output/regicide-cosmic-enc.qcow2 20G
```

Historical boot evidence: unencrypted and encrypted QCOW2 images were previously observed reaching a serial-console login prompt and the COSMIC greeter. Fresh current-source image certification is pending. Prebuilt live ISOs are in [v0.0.1](https://github.com/awdemos/RegicideOS/releases/tag/v0.0.1). The default user is `regicide` with password `regicide`; root has no password set, so manage root with `sudo passwd root` after login. The example LUKS passphrase is `regicide-secure-test`. Write the passphrase file with `printf`; a trailing newline becomes part of the key.

#### Live ISO

Download the split ISO chunks from the [v0.0.1 release](https://github.com/awdemos/RegicideOS/releases/tag/v0.0.1), reassemble, and verify:

```bash
# RegicideOS (Gentoo + COSMIC)
cat regicide-cosmic-amd64.iso.part* > regicide-cosmic-amd64.iso
sha256sum -c regicide-cosmic-amd64.iso.sha256

# RegicideOSArch (Arch + COSMIC)
cat regicide-arch.iso.part* > regicide-arch.iso
sha256sum -c regicide-arch.iso.sha256
```

Both ISOs boot under UEFI in QEMU or virt-manager, or can be written to a USB drive. Identify the USB device (`/dev/sdX`), unmount its partitions, and write the ISO:

```bash
sudo umount /dev/sdX*
sudo dd if=regicide-cosmic-amd64.iso of=/dev/sdX bs=4M status=progress conv=fsync
```

Or use `scripts/flash-usb.sh`, which defaults to the built ISO and verifies the write:

```bash
./scripts/flash-usb.sh /dev/sdX
```

To regenerate a matching ISO from an existing SquashFS without recompiling stage4:

```bash
DAGGER_PROGRESS=plain dagger run python build-system/dagger_pipeline.py \
  --plain \
  --iso \
  --from-tarball build-system/catalyst/output/stage4-amd64-systemd-cosmic.tar.xz \
  --from-squashfs build-system/catalyst/output/regicide-cosmic.img \
  --skip-sign
```

#### Bare metal

Boot an existing Linux live environment, clone the repo, build the installer, and point it at the local SquashFS image. `regicide-cosmic.img` is the ROOTS filesystem, not a bootable USB image.

```bash
cargo build --release -p installer
test -x .cargo-targets/target/release/installer
sudo ./.cargo-targets/target/release/installer \
    --image build-system/catalyst/output/regicide-cosmic.img \
    --checksum <64-hex-digest> \
    /dev/sdX
```

#### AI agent installation procedure

Deterministic steps with verifiable success criteria. Paths assume the repo was cloned into the current working directory. Prerequisites: a Gentoo host or container with Portage, root access, `/dev/kvm`, and `emerge -av dev-util/catalyst app-arch/pixz sys-fs/squashfs-tools app-emulation/qemu sys-fs/cryptsetup`.

A. Build the Catalyst stage4 and SquashFS from source.

1. Enter the Catalyst build directory and run the builder.

   ```bash
   cd "$(pwd)/build-system/catalyst"
   sudo ./build.sh
   ```

2. Verify the stage4 tarball exists.

   ```bash
   test -f "$(pwd)/output/stage4-amd64-systemd-cosmic.tar.xz"
   ```

3. Verify the live SquashFS image exists and is non-empty.

   ```bash
   test -s "$(pwd)/output/regicide-cosmic.img"
   ```

4. Success criterion: both commands return exit code `0`.

B. Build an encrypted bootable QCOW2 image.

1. Create the passphrase file without a trailing newline. The example passphrase is `regicide-secure-test`.

   ```bash
   printf 'regicide-secure-test' > /tmp/regicide-passphrase.txt
   ```

   > A trailing newline becomes part of the LUKS key when `cryptsetup` reads the file, so typing the passphrase later will fail. Use `printf`, not `echo`.

2. Build the encrypted QCOW2 image from the stage4 tarball and SquashFS.

   ```bash
   cd "$(pwd)/build-system/catalyst"
   sudo env REGICIDE_LUKS_PASSPHRASE="$(cat /tmp/regicide-passphrase.txt)" \
       ./build-vm-image.sh \
       --encrypt \
       --passphrase-file /tmp/regicide-passphrase.txt \
       --squashfs "$(pwd)/output/regicide-cosmic.img" \
       "$(pwd)/output/stage4-amd64-systemd-cosmic.tar.xz" \
       "$(pwd)/output/regicide-cosmic.qcow2" 20G
   ```

3. Verify the QCOW2 image exists.

   ```bash
   test -s "$(pwd)/output/regicide-cosmic.qcow2"
   ```

4. Verify the partition table.

   ```bash
   sudo parted -s "$(pwd)/output/regicide-cosmic.qcow2" print > /dev/null 2>&1
   ```

5. Success criterion: the build prints `RegicideOS QEMU image build complete!`, exit code is `0`, and the QCOW2 file has a partition table. The LUKS passphrase for the example is `regicide-secure-test`.

C. Boot the QCOW2 image in QEMU.

1. Ensure no other QEMU process holds the image, then copy `OVMF_VARS.fd`.

   ```bash
   pkill -9 -f 'qemu-system-x86_64' 2>/dev/null || true
   cp /usr/share/OVMF/OVMF_VARS.fd /tmp/ovmf-vars.fd
   ```

2. Boot with UEFI and a serial console.

   ```bash
   qemu-system-x86_64 \
       -enable-kvm \
       -m 8G \
       -smp 4 \
       -cpu host \
       -machine type=q35,accel=kvm \
       -drive if=pflash,format=raw,readonly=on,file=/usr/share/OVMF/OVMF_CODE.fd \
       -drive if=pflash,format=raw,file=/tmp/ovmf-vars.fd \
       -nographic \
       -hda /tmp/regicide-cosmic.qcow2
   ```

3. For encrypted images, enter `regicide-secure-test` when prompted.

4. Success criterion: the VM reaches the COSMIC greeter or serial login prompt. Log in as `regicide` / `regicide` and run `systemctl status systemd-logind` to confirm it is `active (running)`.

D. Observe the VM in a GUI window.

On a host with a display server, launch with a SPICE console instead of `-nographic`:

```bash
cp /usr/share/OVMF/OVMF_VARS.fd /tmp/ovmf-gui.fd
qemu-system-x86_64 \
    -enable-kvm -m 8G -smp 4 -cpu host -machine type=q35,accel=kvm \
    -drive if=pflash,format=raw,readonly=on,file=/usr/share/OVMF/OVMF_CODE.fd \
    -drive if=pflash,format=raw,file=/tmp/ovmf-gui.fd \
    -vga qxl -spice port=5920,disable-ticketing=on \
    -serial file:/tmp/regicide-gui-serial.log \
    -hda /tmp/regicide-cosmic.qcow2
```

Attach a SPICE viewer:

```bash
remote-viewer spice://localhost:5920
```

For encrypted images, enter `regicide-secure-test` in the VM window when prompted.

E. Install to bare metal from the live SquashFS image.

1. Boot the target machine from an existing Linux live environment, clone the repo, and build the installer.

   ```bash
   cargo build --release -p installer
   ```

2. Verify the installer binary.

   ```bash
   test -x "$(pwd)/.cargo-targets/target/release/installer"
   ```

3. Identify the target disk, calculate the image digest with `sha256sum`, and run the installer against the local SquashFS image. Replace the digest placeholder and `/dev/sdX` with real values. Verification and staging complete before partitioning.

   ```bash
   sudo "$(pwd)/.cargo-targets/target/release/installer" \
       --image "$(pwd)/build-system/catalyst/output/regicide-cosmic.img" \
       --checksum <64-hex-digest> \
       /dev/sdX
   ```

4. Verify the installer exited cleanly.

   ```bash
   echo $?
   ```

5. Success criterion: the installer exits `0` and the target disk has a partition table with a `ROOTS` partition.

   ```bash
   sudo parted -s /dev/sdX print | grep -q ROOTS
   ```

Keep the example passphrase `regicide-secure-test` available for unlocking or decrypting the image later. The VM builder exposes SPICE on port `5920` by default:

```bash
remote-viewer spice://localhost:5920
```

If a display is unavailable, boot with `-nographic` and inspect the serial console. If `/tmp` is a tmpfs, it can fill up and GTK applications may report "Disk quota exceeded":

```bash
df -h /tmp
```

Move temporary files to `/var/tmp` when `/tmp` is near capacity.

### Automated configuration

```bash
cat > regicide-config.toml << 'EOF'
drive = "/dev/sda"
image = "build-system/catalyst/output/regicide-cosmic.img"
checksum = "<64-hex-digest>"
filesystem = "btrfs"
username = "your-username"
applications = "minimal"
EOF

sudo ./.cargo-targets/target/release/installer -c regicide-config.toml
```

Explicit CLI values take precedence over TOML values. `checksum` and `allow_unverified` conflict after CLI and TOML settings are merged.

## Operate

Boot the live ISO headlessly and attach a VNC viewer to watch the COSMIC greeter come up:

```bash
cp /usr/share/OVMF/OVMF_VARS.fd /tmp/regicide-iso-vars.fd
chmod u+w /tmp/regicide-iso-vars.fd
qemu-img create -f qcow2 /tmp/regicide-iso-test.qcow2 30G
qemu-system-x86_64 -enable-kvm -m 8G -smp 4 -cpu host \
    -machine type=q35,accel=kvm \
    -drive if=pflash,format=raw,readonly=on,file=/usr/share/OVMF/OVMF_CODE.fd \
    -drive if=pflash,format=raw,file=/tmp/regicide-iso-vars.fd \
    -cdrom regicide-cosmic-amd64.iso \
    -drive file=/tmp/regicide-iso-test.qcow2,format=qcow2,if=virtio \
    -netdev user,id=net0,hostfwd=tcp::2225-:22 \
    -device virtio-net-pci,netdev=net0 \
    -vga std -vnc :0
```

Connect a VNC client to `localhost:5900` and log in as `regicide` / `regicide` over forwarded SSH on port `2225`.

## Roadmap

### AI integration

| Phase | Feature | Status |
|-------|---------|--------|
| Now | BtrMind local AI assistant | Source tests pass; monitor-only by default |
| 2026 | Package optimization AI | 📋 Planned |
| 2026 | Predictive system maintenance | 📋 Planned |
| 2026 | Intelligent resource allocation | 📋 Planned |
| 2027 | Natural language system control | 📋 Planned |
| 2027 | Kernel migration | 📋 Planned |

### Delivery

- [x] Core installer with Btrfs validation and verified pre-partition image staging
- [x] Read-only root filesystem and bootable image pipeline
- [x] Modular Rust installer with orchestrated install flow
- [x] BtrMind AI agent with monitor-only service defaults and explicit root cleanup
- [x] Bootable QCOW2 VM image
- [x] Bootable ISO / Base system image
- [x] Cosmic Desktop integration
- [ ] Rust replacements of core GNU utilities
- [ ] Memory-safe package manager
- [ ] Advanced AI capabilities (predictive maintenance, NL control)
- [ ] Kernel integration

## Contributing

Help is welcome with:

- **Rust development:** rewriting system components in Rust
- **AI integration:** implementing intelligent system features
- **Overlay creation:** developing useful package collections
- **Documentation:** improving guides and references
- **Testing:** bug reports and verification

Found a bug? Please [file an Issue](https://github.com/RegicideOS/RegicideOS/issues) with detailed logs, the command you ran, and your environment so we can reproduce it.

## License

RegicideOS is licensed under the **GNU General Public License v3.0**.

Built on the foundation of Gentoo Linux and the COSMIC Desktop ecosystem.

<div align="center">

**© 2026 Andrew White · RegicideOS Project**

</div>
