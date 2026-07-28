# 05 — Linux Installation

## 🧠 Big Question

> **How does a new village choose its Chief?**

A new computer or virtual machine may have CPU, memory, storage, and networking, but it still needs an operating system before it can become a useful Linux server.

Installing Linux is more than copying files. It means choosing the Chief, preparing storage, creating trusted users, defining the system's identity, and confirming that the new village is ready for work.

> **Why should I care?** Every Linux server begins with either an installation or a prepared machine image. Decisions made here affect security, storage, recovery, and future maintenance.

---

## 🪨 Caveman Story

A new village has been built.

It has land, workers, roads, and empty storage caves—but no Chief and no village rules.

The villagers gather to choose a leader. They first inspect the Chief's official scroll to ensure it is genuine. They then carry the scroll into the new village and begin the ceremony.

The chosen Chief learns:

- the **village name**;
- the **language and time** used by the villagers;
- the **names of trusted people**;
- the **rules for entering and working**;
- how the **storage caves** are divided; and
- which **essential tools** must be available.

When the ceremony is complete, the Chief asks everyone to leave and re-enter through the village gate. This is the first real test: can the Chief wake, recognise the village, and organise its resources without help?

Only then is the new village ready.

```text
New village
     ↓
Choose an authentic Chief's scroll
     ↓
Carry it to the village
     ↓
Prepare storage caves
     ↓
Create trusted villagers and rules
     ↓
Install the Chief and essential tools
     ↓
Open the gate for the first time
```

---

## 🖼 Story Diagram

### 1. The new village gathers to choose its Chief

![A new village gathering to choose its Chief](../images/05-Linux%20Installation/Screenshot%202026-07-28%20063213.png)

### 2. The village studies the new rules and responsibilities

![The villagers learning how their new village will be organised](../images/05-Linux%20Installation/Screenshot%202026-07-28%20063218.png)

### 3. A trusted Chief is selected

![The village selecting its new Chief](../images/05-Linux%20Installation/Screenshot%202026-07-28%20063223.png)

### 4. The Chief enters the village and begins organising it

![The chosen Chief entering the new village](../images/05-Linux%20Installation/Screenshot%202026-07-28%20063227.png)

```text
Download ISO
     ↓
Verify ISO
     ↓
Create bootable USB or attach ISO to a VM
     ↓
Boot the installer
     ↓
Choose language, keyboard, and network
     ↓
Partition the disk
     ↓
Create a user and set the hostname
     ↓
Install Linux and packages
     ↓
Reboot and perform the first login
```

---

## 🧩 Caveman → Computer Mapping

| Caveman Village | Linux Installation Step | Purpose |
| --- | --- | --- |
| Official Chief's scroll | Linux ISO image | Contains the installer and operating-system files |
| Checking the scroll's seal | Checksum or signature verification | Confirms the download is complete and authentic |
| Carrying the scroll into the village | Bootable USB or mounted virtual ISO | Makes the installer available to the machine |
| Opening the village ceremony | Booting the installer | Starts the installation environment |
| Dividing the storage caves | Disk partitioning | Organises space for Linux, boot files, data, and swap |
| Naming the village | Hostname | Gives the system an identity on a network |
| Registering a trusted villager | User creation | Creates an account for administration and daily work |
| Teaching the Chief essential duties | Package installation | Adds the base system and selected tools |
| Opening the village gate | First reboot and login | Confirms that the installed system can start and accept a user |

> **Installation turns unused hardware into an organised Linux system.**

---

## 💻 Technical Explanation

### 1. Choose a Linux distribution

Select a distribution that matches the workload, support requirements, and your team's experience.

For a first server lab, an **Ubuntu Server LTS** or another stable server distribution is a practical choice. In production, organisations may use Ubuntu LTS, Debian, Red Hat Enterprise Linux, Rocky Linux, AlmaLinux, SUSE Linux Enterprise, or a cloud provider's Linux image.

Consider:

- support lifetime;
- security update policy;
- available packages;
- hardware and application compatibility; and
- vendor or community support.

### 2. Download and verify the ISO

An **ISO image** is a file containing the installer and operating-system files. Download it from the distribution's official website.

Before using it, compare its cryptographic checksum with the checksum published by the distribution:

```bash
sha256sum ubuntu-server.iso
```

A matching checksum confirms that the file was not corrupted or unexpectedly changed. For stronger authenticity checks, follow the distribution's documented signature-verification process.

### 3. Prepare the installation media

For a physical computer, write the ISO to a USB drive with a trusted imaging tool. This operation erases the selected USB drive, so verify the target carefully.

For VirtualBox or VMware, create a VM and attach the ISO to its virtual optical drive. No physical USB is required.

A comfortable beginner lab VM can use:

| Resource | Suggested Lab Size |
| --- | --- |
| CPU | 2 virtual CPUs |
| RAM | 2–4 GB |
| Disk | 25 GB or more |
| Network | NAT for simple internet access |

These are learning defaults, not universal production requirements. Size a production server for its actual workload.

### 4. Boot the installer

Start the physical machine or VM and select the installation media. On physical hardware, you may need to change the BIOS or UEFI boot order.

Choose the correct:

- language;
- keyboard layout;
- time zone;
- network configuration; and
- installation profile.

Servers usually use a minimal installation so fewer unnecessary packages, services, and security risks are introduced.

### 5. Partition the disk

Partitioning divides storage into areas with different responsibilities.

Common Linux storage components include:

| Component | Purpose |
| --- | --- |
| EFI System Partition | Stores UEFI boot files |
| `/boot` | Stores kernels and boot-related files when separate |
| `/` | The root filesystem containing the Linux system |
| `/home` | Stores user data when configured separately |
| `/var` | Stores changing data such as logs, caches, and service data |
| Swap | Provides memory overflow space and may support hibernation |

For a first VM, automatic guided partitioning is usually appropriate. Production designs may use LVM, disk encryption, RAID, or separate filesystems to improve flexibility, isolation, resilience, or security.

> Partitioning can destroy existing data. Always confirm the selected disk and have a tested backup before changing a machine that contains important data.

### 6. Set the hostname and create a user

The **hostname** identifies the machine. Use a meaningful naming standard such as `web-01`, `db-test-01`, or `ai-gpu-01` rather than a random name.

Create a normal administrative user with a strong password. Use `sudo` for approved administrative tasks instead of working as `root` for everyday activity.

If the installer offers SSH server installation, enable it only when remote access is needed. Production SSH should use controlled network access and preferably key-based authentication.

### 7. Install the base system and packages

The installer copies the operating system to disk, installs a kernel and bootloader, creates the user, and applies the selected configuration.

Avoid selecting every optional package. A smaller system is easier to understand, update, and secure. Additional software can be installed later through the distribution's package manager.

### 8. Reboot and perform the first login

When installation finishes:

1. detach the ISO or remove the USB drive;
2. reboot from the installed disk;
3. log in using the new account;
4. confirm system identity, networking, storage, and time; and
5. install available security updates.

The first successful login proves only that Linux started. A production-ready server still requires validation, patching, access controls, monitoring, backups, and workload-specific configuration.

---

## 🌍 Real-World Example

An engineer preparing a new web server might follow this path:

```text
Approved Ubuntu LTS image
          ↓
Verified checksum
          ↓
Minimal server installation
          ↓
Named web-prod-01
          ↓
Administrative user + SSH key
          ↓
Security updates installed
          ↓
Nginx deployed
          ↓
Monitoring, backup, and health checks enabled
```

Production teams normally document or automate this build so two servers do not receive different settings by accident. Repeatability matters as much as a successful installation.

---

## ☁ Cloud Example

Cloud engineers rarely install Linux interactively from a USB drive. They select a trusted provider image and launch a virtual machine from it.

```text
Trusted cloud image
        ↓
VM size and disk selected
        ↓
Network and firewall rules attached
        ↓
SSH key or managed identity configured
        ↓
cloud-init applies first-boot configuration
        ↓
Monitoring confirms readiness
```

Tools such as Terraform, cloud-init, and image-building pipelines can make this repeatable. The steps are still conceptually the same: choose the operating system, prepare storage, create identity and access, install packages, boot, and validate.

---

## 🤖 AI Infrastructure Example

An AI server needs Linux plus a compatible hardware and software stack:

```text
Approved Linux image
        ↓
GPU-compatible kernel and drivers
        ↓
Container runtime or Python environment
        ↓
CUDA or another compute platform
        ↓
Model-serving framework
        ↓
Model weights and application
        ↓
GPU, service, and inference health checks
```

The Linux installation is only the foundation. Driver, kernel, container-runtime, and framework versions must be compatible. Production AI images are often prebuilt and tested so every GPU node starts with the same known configuration.

---

## ⚡ Linux Commands

This is a **post-installation acceptance check**, not a general health check. A few commands intentionally revisit earlier concepts because an installer must prove that the selected OS, storage layout, account, and network configuration were actually applied.

### Verify the downloaded installer

```bash
sha256sum linux-image.iso   # Compare this value with the publisher's checksum
```

Run this on a Linux host before booting the ISO. Replace the filename with the ISO you downloaded.

### Confirm the installation choices

```bash
cat /etc/os-release         # Confirm the installed distribution and version
hostname                    # Confirm the village/server name chosen during setup
id                          # Confirm the current account, UID, and group membership
systemd-detect-virt         # Identify VirtualBox, VMware, cloud, or bare metal
```

`cat /etc/os-release` is intentionally repeated from the distributions lesson: there it teaches distro identity; here it verifies that the installer produced the system you selected.

### Validate the installed storage layout

```bash
lsblk -f                    # Match partitions to filesystems and mount points
findmnt --verify            # Check /etc/fstab for mount-definition problems
findmnt /                   # Confirm which filesystem provides the root directory
swapon --show               # Confirm configured swap, if the design uses it
```

### Validate first-login access and networking

```bash
ip -brief address           # Confirm each interface has the expected address
ip route show default       # Confirm a default gateway exists
getent hosts example.com    # Confirm the configured resolver can answer
ss -lnt                     # Confirm expected TCP services are listening
```

### Review installation evidence

```bash
sudo less /var/log/installer/syslog  # Ubuntu/Debian installer log, when retained
sudo cloud-init status --long        # Cloud-image initialization state, when used
sudo sshd -t                         # Validate SSH server configuration, if installed
```

Paths and commands vary by distribution and installation method. A missing installer log or `cloud-init` command is normal when that method was not used. Package updating is covered by the distribution's package-manager workflow; production troubleshooting is covered in its own lesson.

---

## 🧪 Hands-on Lab

### Install Linux in VirtualBox or VMware

1. Download an Ubuntu Server LTS ISO from the official Ubuntu website.
2. Verify its SHA-256 checksum using your host operating system's checksum tool.
3. Create a VM with 2 virtual CPUs, 2–4 GB RAM, and at least 25 GB of dynamically allocated storage.
4. Attach the ISO and use NAT networking.
5. Start the VM and select the server installation option.
6. Choose the correct language, keyboard, and time settings.
7. Use guided partitioning for this disposable lab VM.
8. Set a meaningful hostname such as `caveman-lab-01`.
9. Create a normal user. Install OpenSSH only if you plan to practise remote access.
10. Complete the installation, detach the ISO, and reboot.
11. Log in and run the acceptance checks from this lesson.
12. Confirm the chosen OS, hostname, account, disk layout, gateway, DNS resolution, and optional SSH access.

Create a short validation record containing:

- distribution and version;
- hostname;
- kernel version;
- IP address;
- disk layout and free space;
- failed services, if any; and
- installation date.

### Think Like an Engineer

You must build 100 identical Linux servers.

Would you install each one manually? What could become inconsistent—users, partitions, packages, SSH settings, or security updates?

Consider how a standard image, cloud-init, configuration management, or Infrastructure as Code could make the installation repeatable and auditable.

---

## 🎯 Interview Questions

1. What is a Linux ISO image?
2. Why should an ISO checksum be verified?
3. What is the difference between installing on physical hardware and a virtual machine?
4. What happens during Linux installation?
5. What is disk partitioning, and why must it be planned carefully?
6. What are `/`, `/boot`, `/home`, `/var`, and swap used for?
7. Why are minimal server installations preferred in production?
8. Why should administrators use a normal account with `sudo` instead of logging in as `root` for daily work?
9. Which checks would you perform after the first boot?
10. Why is a successful login not enough to declare a server production-ready?
11. How do cloud images and cloud-init change the installation process?
12. How would you build many identical servers reliably?

---

## 📌 Key Takeaways

- A Linux installation gives hardware or a VM an operating system, identity, users, storage layout, and essential packages.
- Download installation media from a trusted source and verify it before use.
- Partitioning affects capacity, security, maintenance, and recovery.
- Minimal installations reduce unnecessary packages, services, and attack surface.
- The first boot must be followed by identity, resource, network, time, service, log, and update checks.
- Production systems also need controlled access, monitoring, backups, hardening, and documented recovery.
- Standard images and automation make large-scale Linux installation consistent and repeatable.

---

## 🪨 Caveman Summary

```text
Official Chief's scroll → Linux ISO
Check the seal          → Verify checksum or signature
Carry in the scroll     → Bootable USB or attached VM ISO
Open the ceremony       → Boot the installer
Divide storage caves    → Partition the disk
Name the village        → Configure the hostname
Register villagers      → Create users and permissions
Teach essential duties  → Install Linux and packages
Open the village gate   → Reboot and log in
Inspect the village     → Perform post-install validation
```

> **A good installation does not merely start Linux—it creates a Linux system that can be trusted, understood, maintained, and recovered.**
