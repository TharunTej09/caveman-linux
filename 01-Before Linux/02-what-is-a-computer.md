# What Is a Computer?

## 🎯 Why Should I Care?

Linux does not float in the air—it runs on a computer. Understanding the main parts of that computer helps you diagnose slow systems, full disks, memory shortages, and broken network connections.

## 🪨 Story — Inside the Storage Cave

The storage cave cannot provide anything by itself. Chief Grog needs workers and equipment inside it:

- A **Thinker** who follows instructions and makes decisions
- A **Working Table** holding items needed right now
- A **Storage Room** keeping resources for later
- A **Messenger** communicating with other caves
- An **Energy Fire** powering all the work

Together, these parts make the cave useful.

## 🖼️ From the Cave to Technology

| Inside the Cave | Computer Hardware | Main Job |
|---|---|---|
| Thinker | CPU | Processes instructions |
| Working table | RAM | Holds information currently in use |
| Storage room | SSD or disk | Keeps files and programs |
| Messenger | NIC | Sends and receives network data |
| Energy fire | PSU | Supplies electrical power |

## 🧠 What Is a Computer?

A **computer** is a machine that receives input, processes instructions, stores information, and produces output.

```text
Input → Processing → Storage → Output
```

### CPU — The Thinker

The **CPU (Central Processing Unit)** executes instructions and performs calculations. A server may have several CPU cores, allowing it to work on multiple tasks.

### RAM — The Working Table

**RAM (Random Access Memory)** holds programs and data currently being used. RAM is fast but temporary: its contents disappear when the computer loses power.

A larger working table lets workers handle more active tasks. In the same way, more RAM lets a computer keep more active data readily available.

### SSD or Disk — The Storage Room

Storage devices keep the operating system, programs, and files even after power is turned off. SSDs are generally faster than traditional hard disk drives.

### NIC — The Messenger

The **NIC (Network Interface Card)** connects the computer to a network using Ethernet, Wi-Fi, or another technology.

### PSU — The Energy Fire

The **PSU (Power Supply Unit)** converts and supplies electrical power to the computer's components.

## 💻 How This Appears in Linux

```bash
lscpu
free -h
lsblk
ip addr
```

| Command | Hardware View |
|---|---|
| `lscpu` | CPU architecture and cores |
| `free -h` | RAM usage |
| `lsblk` | Storage devices and partitions |
| `ip addr` | Network interfaces and addresses |

Linux turns raw hardware details into information administrators can inspect and manage.

## ☁️ Production Reality

Cloud servers still use CPU, memory, storage, and networking—even when you cannot physically see the machine.

Choosing a cloud instance means choosing a combination of these resources. A database may need more memory and fast storage, while an AI workload may require powerful GPUs in addition to CPUs.

## 🎯 Think Like an Engineer

A server has a fast CPU but very little RAM and a slow disk. Could the server still feel slow? Which workload would be affected most, and what would you inspect first?

## 📌 Caveman Summary

```text
CPU thinks
RAM holds active work
Storage remembers
NIC communicates
PSU powers
```

> **A computer is a group of hardware components working together to process, store, and communicate information.**

