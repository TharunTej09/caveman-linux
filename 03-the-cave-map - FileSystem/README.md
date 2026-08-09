# The Cave Map — Linux Filesystem

## Finding Everything Inside Linux

Before this chapter, the Caveman Chief showed us how Linux runs the village.

Now the Chief takes us **inside the cave**.

> “A warrior who cannot find food in his own cave will never survive.”
>
> — Chief Grog

Linux works the same way. If you cannot find files, understand paths, or locate storage, everyday administration quickly becomes confusing.

## 🧠 Why Should I Care?

In Linux, almost everything is represented or managed through the filesystem: application code, configuration, logs, user data, devices, and mounted storage.

Servers, Docker containers, Kubernetes workloads, cloud machines, and AI platforms all depend on it. Understanding the filesystem is therefore one of the first steps toward managing a real Linux server confidently.

## 🪨 The Caveman Story

Chief Grog’s cave has grown into a huge network of rooms.

- Families keep their belongings in one area.
- Village rules are stored in another.
- Daily records and warnings have their own room.
- Tools and supplies are arranged in known locations.
- New storage caves can be connected when more space is needed.

Without a map, a hunter may know that food exists but still be unable to find it. In Linux, that map is the **filesystem hierarchy**.

## 🖼 The Cave Map

```text
                         Mountain
                            ▲
                            │
                    ┌──── ROOT (/) ────┐
                    │          │       │
                  /home       /etc    /var       /usr
                    │          │       │           │
                  users      config   logs      programs
                    │
                  tharun
                    │
                Documents
                    │
                  Linux
```

The hierarchy begins at **root**, written as `/`. Every file and directory is reached by following a path downward from this single starting point—even when additional disks are attached through mounting.

## 🧩 Cave → Linux Mapping

| Caveman World | Linux World |
| --- | --- |
| Entire cave system | Filesystem |
| Cave entrance | Root directory (`/`) |
| Rooms | Directories |
| Stored items | Files |
| Directions to an item | Paths |
| New storage cave | Disk or partition |
| Connecting a new cave | Mounting |
| Cave map | Directory hierarchy |

## 🧭 Learning Journey

```text
Computer
   ↓
Disk
   ↓
Linux Filesystem
   ↓
Directories
   ↓
Files
   ↓
Paths
   ↓
Storage
   ↓
Mounting
   ↓
Real Linux Server
```

## 📚 Lessons in This Chapter

1. [Linux Filesystem](01-linux-filesystem.md) — understand the single directory tree that Linux uses.
2. [Important Directories](02-important-directories.md) — learn what locations such as `/home`, `/etc`, `/var`, and `/usr` contain.
3. [Paths](03-paths.md) — move confidently using absolute and relative paths.
4. [Files and Directories](04-files-and-directories.md) — create, inspect, copy, move, and remove filesystem objects.
5. [Mounting and Storage](05-mounting-and-storage.md) — connect disks and storage to the Linux directory tree.

### Command Ownership

This chapter uses the smallest command needed to make each filesystem concept observable: `pwd`, guided `cd` forms, basic listing/creation, and storage inspection. [Chapter 04](../04-finding-your-tools%20-%20Learn%20Commands/README.md) then teaches those familiar tools as complete command-line workflows—with options, composition, help, editing, scripting, and scheduling. That later reuse is deliberate progression, not a second introduction.

## 📌 Chapter Goal

By the end of this chapter, you should be able to look at a Linux path, understand where it leads, find important system data, and explain how storage becomes part of the filesystem.

```text
Cave Map → Filesystem → Directories → Files → Paths → Mounted Storage
```

## 🧭 Chapter Navigation

[← Meet the Caveman Chief](../02-Meet%20the%20Caveman%20Chief%20-%20Linux/README.md) · [Course Home](../README.md) · [Next: Finding Your Tools →](../04-finding-your-tools%20-%20Learn%20Commands/README.md)
