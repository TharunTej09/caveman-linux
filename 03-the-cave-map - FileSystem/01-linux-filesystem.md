# 01 — The Linux Filesystem

## 🧠 Big Question

**How does Linux organise everything when a computer may contain millions of files?**

## 🪨 Caveman Story

Chief Grog’s village once stored food, weapons, medicine, and sleeping supplies in one giant cave.

Nobody knew where anything belonged. Hunters searched through food to find spears, while healers searched through weapons to find medicine.

The Chief solved the problem by creating one organised cave system. Every room had a purpose, and every room could be reached from the same entrance.

Linux uses the same idea. Its organised cave system is called the **filesystem**.

## 🖼 Story Diagram

### The Caveman Village

```text
                    Main Cave Entrance
                           │
                       Chief Cave
                    ┌──────┼──────┐
                    │      │      │
                Food Cave  │  Weapon Cave
                           │
                      Sleeping Cave
```

The entrance leads to every room. In Linux, that entrance is the **root directory**, written as `/`.

### Windows and Linux

```text
Windows                              Linux

  C:\                                  /
  D:\                                  │
  E:\                              Everything

Separate drive trees                 One directory tree
```

Windows commonly presents storage as separate drive letters. Linux presents files and attached storage through one hierarchy beginning at `/`.

### The Linux Filesystem Tree

```text
/
├── home
├── etc
├── usr
├── var
├── boot
└── dev
```

These directories have different responsibilities. The next lesson explores them in detail.

## 🧩 Caveman → Computer Mapping

| Caveman World | Linux World |
| --- | --- |
| Entire cave system | Filesystem |
| Main cave entrance | Root directory (`/`) |
| Cave rooms | Directories |
| Food, tools, and records | Files |
| Route to a room | Path |
| Your current room | Working directory |

## 💻 Technical Explanation

A **filesystem** is the structure Linux uses to organise and access data on storage devices.

Linux arranges that data as a tree:

- `/` is the top of the tree.
- Directories create branches.
- Files are stored within those directories.
- Paths describe where files and directories are located.

Unlike the usual Windows drive-letter view, Linux connects disks and partitions to locations within this one tree. This creates a consistent view whether the data lives on a local disk, cloud volume, USB drive, or network storage.

> **Important:** `/` is the root of the whole filesystem. `/root` is a separate directory used as the root user’s home. They are not the same thing.

### What Is the Working Directory?

The **working directory** is the directory your terminal is currently positioned inside.

Think of it as the room where your warrior is standing right now. Before working with nearby files, you should know your current location.

## 🌍 Real-World Example

When an engineer investigates a web server, they may need application files, configuration, and logs. These can live in different directories, but all are reachable through the same filesystem tree beginning at `/`.

## ☁ Cloud Example

A cloud virtual machine may have a system disk and several additional data disks. Linux can connect them to chosen directories while still presenting one organised filesystem tree.

## 🤖 AI Infrastructure Example

An AI server may keep model files, datasets, application code, and logs on different storage devices. Linux paths give applications one consistent way to locate all of them.

## ⚡ Linux Commands

### Show Your Current Location

```bash
pwd
```

`pwd` means **print working directory**. It prints the full path of the directory where you are currently standing.

Example output:

```text
/home/tharun
```

This means your terminal is currently inside the `tharun` directory, which is inside `/home`.

This lesson intentionally introduces only `pwd`. You will learn commands for viewing and navigating files in their dedicated lessons.

## 🧪 Hands-on Lab

### Find Your Location

1. Open a Linux terminal.
2. Print your current directory:

   ```bash
   pwd
   ```

3. Read the path from left to right, beginning at `/`.
4. For this guided exercise, move to the filesystem root:

   ```bash
   cd /
   ```

   `cd` will be explained properly in the paths lesson; here it is used only to place you at root.

5. Print your location again:

   ```bash
   pwd
   ```

Expected final output:

```text
/
```

### Check Your Understanding

- What was your starting working directory?
- What did `pwd` show after you moved to root?
- Why does every absolute Linux path begin with `/`?

## 🎯 Interview Questions

1. What is a filesystem?
2. What does `/` represent in Linux?
3. How does the Linux filesystem view differ from Windows drive letters?
4. What is a working directory?
5. What does `pwd` display?
6. Are `/` and `/root` the same location?

## 📌 Key Takeaways

- Linux organises files and directories as one tree.
- The tree begins at the root directory, `/`.
- Additional storage becomes part of this same hierarchy.
- Your current terminal location is the working directory.
- `pwd` prints the full path to that location.

## 🪨 Caveman Summary

```text
Main Cave Entrance
        ↓
      Root (/)
        ↓
   Organised Rooms
        ↓
    Directories
        ↓
   Stored Supplies
        ↓
       Files

Where is the warrior standing?
        ↓
       pwd
```
