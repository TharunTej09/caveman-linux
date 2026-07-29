# 05 — Mounting and Storage

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Distinguish a disk, partition, filesystem, and mount point.
- Explain why storage must be mounted before its files are accessible.
- Inspect block devices, mounted filesystems, and disk usage.
- Mount and unmount storage safely in a controlled environment.

## 🏕️ Caveman Story

A supply cart reaches Chief Grog's village, but its supplies are still outside the cave.

Owning the cart is not enough. The Chief must prepare its storage boxes, choose a doorway in the cave, and connect the cart to that doorway. Only then can villagers reach its contents through the normal cave map.

Linux treats disks the same way. A storage device becomes part of the directory tree when its filesystem is connected to a **mount point**.

## 🖼️ Big Concept Illustration

![Chief Grog connecting storage devices to cave mount points](../images/03-the-cave-map-filesystem/mounting-and-storage-hero.png)

### From Hardware to an Accessible Directory

```text
Disk or SSD
     ↓
  Partition
     ↓
 Filesystem
     ↓
   Mounted
     ↓
Mount point beneath /
     ↓
Files become accessible
```

### USB Storage

```text
USB device
     ↓
Linux detects the device
     ↓
Filesystem is mounted
     ↓
Files are accessible through a directory
```

### The Mount Point

```text
Storage device             Linux filesystem
   /dev/sdb1  ── mount ──> /mnt/data
                                  │
                              Stored files
```

### Cloud Disk

```text
Cloud volume
     ↓
Attached to virtual machine
     ↓
Linux block device
     ↓
Mounted at a folder
     ↓
Application data
```

## 📖 Concept Explained Simply

### Storage Device

A disk, SSD, USB drive, or cloud volume provides physical or virtual storage capacity. Linux commonly presents these as **block devices** beneath `/dev`.

### Partition

A **partition** is a defined region of a storage device. One disk can contain one or more partitions, each used independently.

### Filesystem

A **filesystem** such as ext4 or XFS defines how files, directories, and metadata are organised inside a partition or device.

### Mount Point

A **mount point** is an existing directory where Linux attaches a filesystem. After mounting, entering that directory reveals the files stored on the attached filesystem.

### Mount and Unmount

- **Mounting** connects a filesystem to the Linux directory tree.
- **Unmounting** disconnects it cleanly after pending writes are completed.

Removing a disk without unmounting can interrupt writes and risk corruption. Unmount first, then detach the device.

## 🌍 Real Linux Example

A production database server may keep the operating system on one disk and database files on a larger dedicated volume mounted at `/data`. The application uses `/data` like any other directory even when the storage is a separate cloud disk.

## 🛠️ Commands Introduced

### `lsblk` — Show Block Devices

```bash
lsblk
```

Shows disks, partitions, their sizes, and where they are mounted. The tree layout helps reveal which partitions belong to each disk.

```bash
lsblk -f
```

`-f` means **filesystems**. It adds useful details such as filesystem type, label, UUID, and mount point.

### `df` — Show Mounted Filesystem Usage

```bash
df -h
```

`df` reports capacity and free space for mounted filesystems. `-h` means **human-readable**, displaying sizes in units such as MB and GB.

### `du` — Estimate Directory Usage

```bash
du -sh /var/log
```

`du` estimates space used by files and directories:

- `-s` means **summary**, returning one total instead of every child item.
- `-h` means **human-readable**, using units such as KB, MB, and GB.

Use `df` to ask, “How full is the filesystem?” Use `du` to ask, “Which directory is using the space?” Their values can differ because they measure different things.

### `mount` — Connect a Filesystem

```bash
mount
```

With no arguments, `mount` displays currently mounted filesystems. The output can be long on a production system.

```bash
mount /dev/sdb1 /mnt/data
```

This connects the filesystem on `/dev/sdb1` to the existing mount point `/mnt/data`. Mounting normally requires administrative privileges. Never guess the device name on a real server.

### `umount` — Disconnect a Filesystem

```bash
umount /mnt/data
```

Unmounts the filesystem attached at `/mnt/data`. The command is spelled `umount`, without the first **n**. It can fail when a process is still using that filesystem; investigate the user before forcing anything.

## 💡 Caveman Tip

Think in this order:

```text
Can Linux see the disk?
        ↓
Does it have a filesystem?
        ↓
Where is it mounted?
        ↓
How much space is available?
```

This prevents confusing an attached device with an accessible filesystem.

## ⚠️ Common Mistakes

- Confusing a disk with a mounted filesystem.
- Mounting the wrong partition because the device name was guessed.
- Mounting over a directory that already contains files, which temporarily hides those files.
- Removing storage before unmounting it.
- Using `df` when trying to find which directory consumes space.
- Treating an unmounted cloud disk as missing simply because its files are not visible.

## 🧪 Hands-on Lab

### Part 1: Safe Storage Inspection

Display the block-device tree:

```bash
lsblk
```

Add filesystem details:

```bash
lsblk -f
```

Review mounted filesystem capacity:

```bash
df -h
```

Estimate the size of the log directory:

```bash
du -sh /var/log
```

Review the mounted-filesystem list:

```bash
mount
```

### Part 2: Controlled Mount Practice

Perform this part only in a disposable lab VM with an instructor-provided unused partition and an existing `/mnt/data` directory. Replace `/dev/sdb1` only after confirming the correct lab device with `lsblk -f`.

```bash
mount /dev/sdb1 /mnt/data
df -h
umount /mnt/data
```

Do not practise mounting an unknown device on a production machine.

## 📝 Quick Recap

- Storage hardware provides capacity; a partition divides it; a filesystem organises its data.
- A mount point connects that filesystem to the Linux directory tree.
- `lsblk` shows devices, `df` shows filesystem capacity, and `du` estimates directory usage.
- `mount` connects storage and `umount` disconnects it safely.
- Attached does not always mean mounted.

## 🧠 Interview Questions

1. What is the difference between a disk, partition, filesystem, and mount point?
2. What is the difference between `df` and `du`?
3. What additional information does `lsblk -f` display?
4. Why should storage be unmounted before it is detached?
5. What happens to existing directory contents while another filesystem is mounted over that directory?
6. Why might `umount` report that a target is busy?

## 📚 What's Next

You now understand the complete cave map—from paths and directories to the storage beneath them. Next, you will use this foundation to navigate, inspect, search, and transform data confidently with Linux tools.
