# 01 — The Linux Filesystem

## 🎯 Learning Objectives

- Explain why Linux presents one directory tree beginning at `/`.
- Distinguish a filesystem, directory, file, path, and working directory.
- Compare the Linux hierarchy with Windows drive letters.
- Use `pwd` to identify your current location.

## 🏕️ Caveman Story

Chief Grog once stored food, weapons, medicine, and bedding in one disorganised cave. The villagers wasted hours searching.

He redesigned the mountain as one connected system of rooms. Every room has a purpose, every supply has a place, and every route begins at the main entrance.

Linux calls this organised cave system the **filesystem**.

## 🖼️ Big Concept Illustration

```text
Caveman village                         Linux

Main cave entrance                      Root (/)
        │                                  │
  ┌─────┼─────┐                      ┌─────┼─────┐
Food  Tools  Beds                   home  etc   var
```

```text
Windows                              Linux

C:\   D:\   E:\                        /
separate drive trees                one hierarchy for everything
```

```text
/
├── home
├── etc
├── usr
├── var
├── boot
└── dev
```

## 📖 Concept Explained Simply

A **filesystem** defines how data is organised and accessed on storage. Linux presents directories and files as a tree:

- `/` is the top, called the root directory.
- Directories are branches that organise content.
- Files contain data.
- A path describes a route to a file or directory.
- The working directory is where the current shell is standing.

| Caveman world | Linux world |
| --- | --- |
| Entire cave system | Filesystem |
| Main entrance | Root directory (`/`) |
| Cave room | Directory |
| Stored supply | File |
| Directions | Path |
| Warrior's current room | Working directory |

Additional disks, USB devices, and network storage can join this same tree at chosen directories. `/` is the root of the whole filesystem; `/root` is only the root user's home directory.

### Why Should I Care?

Applications, configuration, logs, users, devices, containers, and model files are all reached through the Linux filesystem. If you cannot identify where you are, every later command becomes riskier.

## 🌍 Real Linux Example

A web server may read configuration below `/etc`, application files below `/var/www`, and logs below `/var/log`. Those locations can sit on different storage devices while still appearing in one tree.

## 🛠️ Commands Introduced

This concept lesson uses one location command:

```bash
pwd
```

`pwd` means **print working directory**. Example output `/home/tharun` means the shell is inside `tharun`, beneath `/home`.

Chapter 04 later revisits `pwd` as part of a complete navigation workflow. Here, it exists only to connect the filesystem idea to your current position.

## 💡 Caveman Tip

Before a file operation, ask: “Which server am I on, and which room am I standing in?”

## ⚠️ Common Mistakes

- Confusing `/` with `/root`.
- Expecting Windows drive letters in Linux.
- Assuming a path without a leading `/` begins at root.
- Treating mounted storage as a separate visible tree rather than part of the hierarchy.

## 🧪 Hands-on Lab

1. Open a Linux terminal.
2. Run `pwd` and write down the result.
3. For this guided step, run `cd /`; navigation is taught properly in Lesson 03.
4. Run `pwd` again. The expected output is `/`.
5. Explain each component of your original path from left to right.

## 📝 Quick Recap

```text
Main entrance → Root (/) → Organised rooms → Directories
                                   └───────→ Stored data → Files
Where am I? → pwd
```

Linux presents one directory hierarchy, and your working directory is one location inside it.

## 🧠 Interview Questions

1. What is a filesystem?
2. What does `/` represent?
3. How does the Linux hierarchy differ from Windows drive letters?
4. What is a working directory?
5. Why are `/` and `/root` different?

## 📚 What's Next

Explore the purpose of each major cave in [02 — Important Linux Directories](02-important-directories.md).
