# 02 — Important Linux Directories

## 🧠 Big Question

**If everything in Linux begins at `/`, how do we know which cave holds what we need?**

## 🪨 Caveman Story

Chief Grog has one enormous cave system, but he does not throw everything into the same room.

Every cave has a purpose:

- Villagers sleep in the **home caves**.
- Village rules stay in the **configuration locker**.
- Shared tools belong in the **tool cave**.
- Logs and changing supplies go to the **warehouse**.
- The fire-starting equipment stays near the **village entrance**.

Because every room has a known purpose, the villagers can find what they need without searching the entire mountain.

Linux works the same way. Its important directories are specialised rooms beneath the root directory, `/`.

## 🖼 Story Diagram

### The Entire Cave Map

```text
                              ROOT (/)
                                  │
        ┌────────┬────────┬───────┼───────┬────────┬────────┐
        │        │        │       │       │        │        │
      /home    /etc     /usr    /var    /opt     /boot    /tmp
        │        │        │       │       │        │        │
    Bedrooms   Rules     Tools  Warehouse  Extra   Engine  Temporary
                                                    Room    Basket
                                  │
                           ┌──────┴──────┐
                           │             │
                         /dev          /proc
                      Device Doors   Magic Window
```

Every branch begins at `/`, but each destination serves a different job.

### A Picture for Each Directory

| Linux Directory | Caveman Picture | What Belongs There |
| --- | --- | --- |
| `/home` | 🛖 **Bedrooms** | Each regular user normally receives a personal directory here. |
| `/etc` | 🔐 **Rules locker** | System-wide configuration, service settings, users, and security records. |
| `/usr` | 🧰 **Shared tool cave** | Most installed programs, libraries, and shared read-only data. |
| `/var` | 📦 **Changing warehouse** | Logs, caches, queues, mail, and other data that changes while the system runs. |
| `/opt` | 🧳 **Visiting trader's store** | Optional or third-party application packages. |
| `/boot` | 🔥 **Engine room** | Files needed to start Linux, including the kernel and bootloader data. |
| `/dev` | 🚪 **Device doors** | Interfaces representing disks, terminals, USB devices, and other hardware. |
| `/proc` | 🪟 **Magic window** | Live, virtual information about the kernel and running processes. |
| `/tmp` | 🧺 **Temporary basket** | Short-lived working files that applications do not need to keep permanently. |

> `/dev` and `/proc` look like ordinary directories, but Linux creates much of their content dynamically. They are views into devices and the running system, not normal storage rooms.

## 🧩 Caveman → Computer Mapping

| Caveman World | Linux World |
| --- | --- |
| Entire mountain | Root filesystem (`/`) |
| Villagers' bedrooms | User homes (`/home`) |
| Village rulebook | Configuration (`/etc`) |
| Shared tools | Programs and libraries (`/usr`) |
| Changing warehouse | Logs and changing data (`/var`) |
| Guest trader's equipment | Optional software (`/opt`) |
| Fire-starting room | Boot files (`/boot`) |
| Doors to physical tools | Device interfaces (`/dev`) |
| Window into village activity | System and process information (`/proc`) |
| Temporary basket | Temporary files (`/tmp`) |

## 💻 Technical Explanation

Linux follows a standard directory layout so people and programs know where different kinds of data should live. The exact contents vary between distributions, but the responsibilities remain broadly consistent.

### The Directories to Remember First

- **`/home` — user space:** Personal files and settings for regular users usually live here.
- **`/etc` — system configuration:** Administrators commonly work here when configuring the operating system and services.
- **`/usr` — installed software:** Contains many commands, libraries, and shared resources used by the system.
- **`/var` — changing system data:** Important during troubleshooting because service and system logs are commonly stored below `/var/log`.
- **`/opt` — optional applications:** Often used by self-contained third-party or commercial software.
- **`/boot` — startup files:** Holds files used during the Linux boot process. Change its contents only when you understand the effect.
- **`/dev` — devices as files:** Provides special interfaces through which Linux communicates with hardware and virtual devices.
- **`/proc` — live system view:** A virtual filesystem exposing current kernel and process information.
- **`/tmp` — temporary workspace:** Intended for temporary data. Do not treat it as permanent storage because cleanup policies may remove its contents.

### One Easy-to-Miss Directory

`/root` is the home directory of the privileged **root user**. It is not the same as `/`, which is the top of the entire filesystem.

## 🌍 Real-World Example

When a web service fails, an engineer may check its configuration under `/etc`, investigate its logs under `/var/log`, and identify its installed application files under `/usr` or `/opt`. Knowing the directory roles narrows the investigation immediately.

## ☁ Cloud Example

A Linux virtual machine in AWS, Azure, or Google Cloud uses the same directory ideas. Cloud-init settings may affect system configuration, application logs still commonly flow beneath `/var`, and users normally work inside `/home`.

## 🤖 AI Infrastructure Example

An AI inference server may keep the serving application under `/opt`, service configuration under `/etc`, changing logs under `/var`, and an engineer's scripts under `/home`. Large models and datasets may be mounted elsewhere, but they still join the same tree beneath `/`.

## ⚡ Linux Commands

### Change Your Current Directory

```bash
cd /etc
```

`cd` means **change directory**. It moves your terminal from its current directory to another directory.

Useful forms of the same command:

```bash
cd /
cd /home
cd ..
cd ~
cd -
```

| Form | Where It Takes You |
| --- | --- |
| `cd /` | The root of the filesystem |
| `cd /home` | The `/home` directory |
| `cd ..` | The parent directory, one level upward |
| `cd ~` | Your own home directory |
| `cd -` | The directory you were in previously |

This lesson intentionally introduces only `cd`. Commands for listing, creating, copying, and searching will appear in their own lessons.

## 🧪 Hands-on Lab

### Walk Through the Cave System

1. Open a Linux terminal.
2. Enter the root of the filesystem:

   ```bash
   cd /
   ```

3. Visit the system configuration cave:

   ```bash
   cd /etc
   ```

4. Move one level back toward root:

   ```bash
   cd ..
   ```

5. Visit the changing-data warehouse:

   ```bash
   cd /var
   ```

6. Return to your personal home directory:

   ```bash
   cd ~
   ```

7. Jump back to the directory you just left:

   ```bash
   cd -
   ```

### Think Before You Move

Which directory would you choose for each item?

- A user's personal notes
- A service configuration file
- A system log
- A temporary application file
- Files required while Linux starts

## 🎯 Interview Questions

1. What is normally stored in `/home`?
2. Why are `/etc` and `/var/log` important to system administrators?
3. How are `/dev` and `/proc` different from normal storage directories?
4. What is the difference between `/` and `/root`?
5. Why should permanent data not be stored in `/tmp`?
6. What do `cd ..`, `cd ~`, and `cd -` do?

## 📌 Key Takeaways

- Every important Linux directory belongs to one tree beginning at `/`.
- `/home` holds user data, `/etc` holds configuration, and `/var` holds changing data.
- `/usr` commonly holds installed software, while `/opt` is often used for optional applications.
- `/boot`, `/dev`, and `/proc` connect you to startup, devices, and live system information.
- `/tmp` is temporary and should not be trusted for permanent storage.
- `cd` moves your terminal between directories.

## 🪨 Caveman Summary

```text
One Mountain
     ↓
   Root (/)
     ↓
Specialised Caves
     ↓
Home · Rules · Tools · Logs · Devices
     ↓
Chief Grog chooses a destination
     ↓
Linux uses cd
```
