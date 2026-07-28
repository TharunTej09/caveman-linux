# Why Computers Need an Operating System

## 🎯 Why Should I Care?

A computer can have powerful hardware and useful programs but still needs something to coordinate them. The operating system controls how programs share CPU time, memory, storage, devices, and access.

Linux is the organizing layer behind many servers, containers, cloud systems, and AI machines.

## 🪨 Story — A Village Without a Chief

The village already has workers, tools, food, storage caves, and roads.

![Workers and tools in the village](../images/01-before-linux/village-workers.png)

But nobody is organizing them:

- Two workers grab the same spear.
- One worker fills every storage room.
- Someone takes another person's tools.
- Less important jobs occupy all the workers.
- Nobody controls entry to protected caves.

Everything exists, but nothing is coordinated. The result is chaos.

![An unorganized village in chaos](../images/01-before-linux/village-chaos.png)

Then Chief Grog arrives.

Chief Grog decides who works, who waits, where resources are stored, who may use each tool, and who is allowed to enter.

![Chief Grog organizing the village](../images/01-before-linux/chief-grog.png)

In our story, Chief Grog represents the **operating system**. In this course, that operating system is Linux.

## 🖼️ From the Cave to Linux

| Village | Computer | What Linux Does |
|---|---|---|
| Workers | Processes | Schedules which process runs |
| Working space | RAM | Allocates and protects memory |
| Storage caves | Filesystems | Organizes stored data |
| Tools | Hardware devices | Coordinates access using drivers |
| Guards | Security controls | Enforces users and permissions |
| Roads | Networking | Sends and receives data |
| Chief Grog | Operating system | Coordinates the entire system |

## 🧠 What Is an Operating System?

An **operating system (OS)** is the main software layer that manages hardware, runs programs, controls access to resources, and gives users ways to interact with the computer.

```text
User
  ↓
Applications
  ↓
Operating system
  ↓
CPU, RAM, storage, network, and devices
```

Applications normally ask the operating system for resources instead of controlling hardware directly.

## 🧠 What Linux Manages

### Processes

A running program is a **process**. Linux schedules processes so many programs can share CPU time.

### Memory

Linux allocates RAM to processes and keeps their memory areas separated.

### Files and Storage

Linux organizes persistent data into files and directories on filesystems.

### Devices

Device drivers allow Linux to communicate with disks, keyboards, network cards, GPUs, and other hardware.

### Users and Permissions

Linux controls which users and programs may read, change, execute, or delete resources.

### Networking

Linux manages network interfaces, addresses, connections, and the movement of data.

## 💻 How This Appears in Linux

```bash
ps -eo pid,ni,stat,comm      # See processes, priority, and current state
findmnt                      # See the filesystem layout Linux presents
ls -l /dev | head           # See device interfaces managed by the kernel
id                           # See the current user's identity and groups
ip -brief link               # See network links managed by Linux
```

Each command reveals a different operating-system responsibility: scheduling work, organising storage, exposing devices, enforcing identity, and controlling network interfaces. Detailed performance and service diagnosis is intentionally saved for the troubleshooting lesson.

## ☁️ Production Reality

- Linux virtual machines run workloads in AWS, Azure, and Google Cloud.
- Docker containers share features provided by the Linux kernel.
- Kubernetes commonly coordinates containers across Linux nodes.
- Databases depend on Linux memory, storage, process, and network management.
- AI servers rely on Linux to coordinate CPUs, GPUs, memory, models, and network traffic.

Strictly speaking, Linux is the kernel at the center of a Linux-based operating system. In beginner conversation, people often use “Linux” for the complete operating-system environment.

## 🎯 Think Like an Engineer

One program begins using nearly all available memory. What should the operating system protect, and what could happen to other programs if it did nothing?

## 📌 Caveman Summary

```text
Workers     → Processes
Workspace   → Memory
Store caves → Filesystems
Guards      → Permissions
Chief Grog  → Linux
```

> **Linux is the chief of the computer: it coordinates work, resources, devices, and access.**
