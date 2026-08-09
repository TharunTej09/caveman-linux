# Lab 01 — Create a Linux Virtual Machine

## 🎯 Mission

Build a safe Linux practice village, log in, and prove that the operating system can see its CPU, memory, disk, and network.

## Prerequisites

- VirtualBox, VMware Workstation/Player, Hyper-V, or another hypervisor
- A current Ubuntu Server LTS ISO downloaded from the official Ubuntu website
- At least 2 CPU threads, 4 GB RAM, and 25 GB free disk space recommended

## ⚠️ Safety

Use a new virtual disk. During installation, confirm that the selected disk belongs to the VM—not a physical disk containing important data.

## Starting State

Create a VM named `caveman-linux-lab` with NAT networking and a dynamically allocated virtual disk. Attach the ISO and start the VM.

## Tasks

1. Choose the normal installation path and accept the detected keyboard and network settings.
2. Use the entire **virtual** disk when prompted.
3. Create a non-root user and a memorable hostname such as `grog-lab`.
4. Select OpenSSH Server if the installer offers it; do not expose the VM directly to the internet.
5. Reboot, remove/eject the ISO, and log in.
6. Inspect the new system:

   ```bash
   hostnamectl
   cat /etc/os-release
   lscpu
   free -h
   lsblk
   ip -brief address
   ```

7. Update package metadata and installed packages:

   ```bash
   sudo apt update
   sudo apt upgrade
   ```

8. Create a hypervisor snapshot named `clean-install` after the upgrade completes.

## ✅ Verification

- `hostnamectl` shows the hostname you chose.
- `/etc/os-release` identifies Ubuntu.
- `lscpu`, `free -h`, and `lsblk` broadly match the VM resources you assigned.
- At least one non-loopback interface appears in `ip -brief address`.
- The VM boots without the ISO attached.

## Troubleshooting Clues

- **No bootable medium:** reattach the ISO and place the virtual optical drive first in the VM boot order.
- **No IP address:** confirm the virtual adapter is enabled and attached to NAT.
- **Install is very slow:** increase assigned RAM or CPU without exceeding the host's capacity.
- **`sudo` fails:** log in with the user created by the installer and confirm the password.

## Cleanup

Keep this VM and its `clean-install` snapshot for later labs. Shut it down cleanly with `sudo poweroff` when not in use.

## 🧠 Think Like an Engineer

Why is a snapshot useful before an experiment, and why is it not a replacement for a backup stored outside the VM?
