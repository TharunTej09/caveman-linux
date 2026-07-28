# What Is a Computer?

## 🎯 Why Should I Care?

Linux does not float in the air—it runs on a computer. Understanding the main parts of that computer helps you diagnose slow systems, full disks, memory shortages, and broken network connections.

## 🪨 Story — Inside the Storage Cave

The storage cave cannot provide anything by itself. Chief Grog needs workers and equipment inside it:

- A **Thinker** who follows instructions and makes decisions
- A **Worker Team** that performs many similar calculations together
- A **Working Table** holding items needed right now
- A **Storage Room** keeping resources for later
- A **Messenger** communicating with other caves
- An **Energy Fire** powering all the work

Together, these parts make the cave useful.

## 🖼️ From the Cave to Technology

| Inside the Cave | Computer Hardware | Main Job |
|---|---|---|
| Thinker | CPU | Processes instructions |
| Worker team | GPU | Performs many similar calculations in parallel |
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

The CPU is like a small group of highly skilled thinkers. Each thinker can handle many different kinds of work, make decisions, and quickly move from one task to another.

### GPU — The Worker Team

The **GPU (Graphics Processing Unit)** contains many smaller processing units designed to perform large numbers of similar calculations at the same time.

Imagine Chief Grog needs to solve one complicated village dispute. He gives it to the Thinker—the CPU.

Now imagine the village must count every stone in one thousand baskets. Instead of asking one Thinker to count each basket in sequence, Chief Grog gives one basket to each member of a large Worker Team—the GPU. Many baskets are counted simultaneously.

```text
One complicated, changing task
              ↓
        CPU — Thinker

Many similar calculations
              ↓
      GPU — Worker Team
```

GPUs were originally designed for graphics, where many pixels must be calculated together. Their parallel design also makes them useful for AI model training, model inference, scientific computing, and video processing.

> A GPU is not automatically faster than a CPU. It provides the greatest benefit when software can divide suitable work into many parallel calculations.

### RAM — The Working Table

**RAM (Random Access Memory)** holds programs and data currently being used. RAM is fast but temporary: its contents disappear when the computer loses power.

A larger working table lets workers handle more active tasks. In the same way, more RAM lets a computer keep more active data readily available.

RAM does not perform calculations. It provides a fast workspace where the CPU and GPU can find the instructions and data they currently need.

### SSD or Disk — The Storage Room

Storage devices keep the operating system, programs, and files even after power is turned off. SSDs are generally faster than traditional hard disk drives.

Unlike RAM, storage is persistent. The storage room keeps supplies overnight; the working table is cleared when the village loses power.

### CPU, GPU, RAM, and Storage Together

These components have different responsibilities, but they cooperate on every workload:

| Component | Caveman Role | What It Does | Does It Keep Data After Power Off? |
|---|---|---|---|
| CPU | Skilled Thinker | Runs general instructions and makes decisions | No |
| GPU | Large Worker Team | Runs many suitable calculations in parallel | No |
| RAM | Working Table | Holds active instructions and data | No |
| SSD or HDD | Storage Room | Keeps programs, models, and files | Yes |

For an AI workload, the storage room may hold a model file. The file is loaded through RAM, calculations are performed by the CPU and GPU, and the result is returned to the application.

```text
Model on SSD
     ↓
Loaded into RAM
     ↓
CPU coordinates the program
     ↓
GPU performs parallel calculations
     ↓
Result returned to the user
```

### NIC — The Messenger

The **NIC (Network Interface Card)** connects the computer to a network using Ethernet, Wi-Fi, or another technology.

### PSU — The Energy Fire

The **PSU (Power Supply Unit)** converts and supplies electrical power to the computer's components.

## 💻 How This Appears in Linux

```bash
lscpu
free -h
lsblk
lspci | grep -Ei 'vga|3d|display'
ip addr
```

| Command | Hardware View |
|---|---|
| `lscpu` | CPU architecture and cores |
| `free -h` | RAM usage |
| `lsblk` | Storage devices and partitions |
| `lspci \| grep -Ei 'vga\|3d\|display'` | Detected graphics or GPU devices |
| `ip addr` | Network interfaces and addresses |

Linux turns raw hardware details into information administrators can inspect and manage.

On a system with supported NVIDIA drivers, `nvidia-smi` can show the GPU model, memory usage, temperature, driver version, and active GPU processes. The command is not available on every computer.

## ☁️ Production Reality

Cloud servers still use CPU, memory, storage, and networking—even when you cannot physically see the machine.

Choosing a cloud instance means choosing a combination of these resources. A database may need more memory and fast storage, while an AI workload may require powerful GPUs in addition to CPUs.

## 🎯 Think Like an Engineer

A server has a fast CPU but very little RAM and a slow disk. Could the server still feel slow? Which workload would be affected most, and what would you inspect first?

## 📌 Caveman Summary

```text
CPU thinks
GPU performs parallel work
RAM holds active work
Storage remembers
NIC communicates
PSU powers
```

> **A computer is a group of hardware components working together to process, store, and communicate information.**
