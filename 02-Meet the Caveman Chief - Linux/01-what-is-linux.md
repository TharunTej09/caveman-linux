# 01 — What Is Linux?

## 🧠 Big Question

> **If the village already has workers, tools, food, and storage, why does it need a Chief?**

A computer may have powerful hardware and useful applications, but something still has to coordinate them. That coordinator is the **operating system**.

---

## 🪨 Caveman Story

Chief Grog's village has grown.

Hundreds of villagers arrive every morning. Hunters need spears, builders need tools, doctors need medicine, and families need food and shelter.

Without anyone organising the village, chaos begins:

- Two hunters try to take the same spear.
- Five villagers enter the same storage cave.
- One worker takes more food than everyone else.
- Nobody knows which job should happen first.
- Restricted caves and valuable treasure are left unprotected.

The villagers finally choose an intelligent leader: **Chief Grog**.

The Chief decides:

- who works and who waits;
- who receives food, tools, and storage;
- which task is most urgent;
- who may enter protected caves; and
- how the village's limited resources are shared.

The workers still perform the jobs, but the Chief keeps the entire village organised.

That is the role Linux plays inside a computer.

---

## 🖼 Story Diagram

![Chief Grog and the village workers](<../images/02-Meetthe CaveManChief Linux/Screenshot 2026-07-27 212446.png>)

![A growing caveman village](<../images/02-Meetthe CaveManChief Linux/Screenshot 2026-07-27 212451.png>)

![Villagers working together under organised leadership](<../images/02-Meetthe CaveManChief Linux/Screenshot 2026-07-27 212457.png>)

```text
Hunters     Builders     Doctors     Families
    \          |           |          /
     \         |           |         /
      +--------+-----------+--------+
                       |
                       v
                  Chief Grog
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Workers      Storage      Security
          |            |            |
          +------------+------------+
                       |
                       v
              An organised village
```

---

## 🧩 Caveman → Computer Mapping

| Caveman Village | Computer System |
| --- | --- |
| Chief Grog | Linux kernel |
| Hunters and workers | Applications and processes |
| Food and working time | CPU time |
| Working table | RAM |
| Storage cave | SSD or hard disk |
| Village rules | Users and file permissions |
| Roads and messengers | Network interfaces and connections |
| Spears, tools, and carts | Hardware devices |

The Chief does not hunt, build, or heal. He coordinates the villagers who do. In the same way, Linux coordinates applications and hardware so they can work together safely.

---

## 💻 Technical Explanation

**Linux is the core of an operating system.** More precisely, Linux is a **kernel**: the central layer that communicates with the computer's hardware and manages its resources.

In everyday conversation, people often say “Linux” to mean a complete Linux operating system—such as Ubuntu, Debian, Fedora, or Rocky Linux. A complete system combines the Linux kernel with command-line tools, libraries, services, and applications.

Linux is responsible for several essential jobs:

| Responsibility | What Linux Does |
| --- | --- |
| Process management | Decides which program can use the CPU and for how long |
| Memory management | Allocates RAM and keeps processes separated |
| Storage management | Reads, writes, and organises data through filesystems |
| Device management | Communicates with disks, keyboards, screens, GPUs, and other hardware through drivers |
| User and permission management | Controls who can access files, commands, and system resources |
| Networking | Sends and receives data through network interfaces |

Linux does not write your document, serve your webpage, or train your AI model. Applications do that work. Linux gives those applications controlled access to the resources they need.

> **Chief Grog manages the village. The Linux kernel manages the computer.**

---

## 🌍 Real-World Example

When you open a web browser, the browser does not directly control the CPU, memory, disk, network card, or screen. It asks the operating system for access.

```text
You open the browser
        ↓
Linux starts the browser process
        ↓
Linux allocates CPU time and RAM
        ↓
Linux reads browser files from storage
        ↓
Linux sends requests through the network
        ↓
Linux displays the result on the screen
```

This coordination happens continuously and usually without the user noticing it.

---

## ☁ Cloud Example

A common cloud setup looks like this:

```text
Cloud virtual machine
        ↓
Ubuntu Linux
        ↓
Nginx web server
        ↓
Website or API
        ↓
Client receives a response
```

The cloud provider supplies virtual hardware. Linux manages that hardware, while Nginx and the application provide the actual service.

---

## 🤖 AI Infrastructure Example

Linux is also widely used on servers that train and run AI models.

```text
GPU server
    ↓
Linux operating system
    ↓
GPU driver and CUDA
    ↓
PyTorch
    ↓
AI model
    ↓
Model response
```

Linux coordinates CPU time, RAM, storage, networking, and access to GPUs while the AI framework and model perform the computation.

---

## ⚡ Linux Commands

Use these commands to ask the Chief about the system:

```bash
uname -a                # Show kernel and system information
hostnamectl             # Show hostname and operating system details
cat /etc/os-release     # Identify the Linux distribution
uptime                  # Show how long the system has been running
```

> `hostnamectl` may not be available on minimal Linux systems. The other commands still provide the essential information.

---

## 🧪 Hands-on Lab

Open a Linux terminal and complete the following investigation.

1. Run `cat /etc/os-release` and identify the distribution name and version.
2. Run `uname -r` and record the kernel version.
3. Run `hostname` and identify the computer's hostname.
4. Run `uptime` and find how long the system has been running.
5. Compare your operating system version with your kernel version. Are they the same?

**Expected discovery:** the Linux distribution and Linux kernel have different names and version numbers because the kernel is only one part of the complete operating system.

---

## 🎯 Interview Questions

1. What is Linux?
2. What is the difference between Linux and a Linux distribution?
3. What is the role of the Linux kernel?
4. Which computer resources does Linux manage?
5. Why is Linux commonly used on servers and cloud systems?

---

## 📌 Key Takeaways

- Linux is the kernel at the centre of a Linux operating system.
- A Linux distribution combines the kernel with tools, libraries, services, and applications.
- Linux manages processes, memory, storage, devices, permissions, and networking.
- Applications perform useful work; Linux coordinates their access to hardware.
- Linux is widely used across servers, cloud platforms, containers, and AI infrastructure.

---

## 🪨 Caveman Summary

```text
Growing village
      ↓
Chief Grog
      ↓
Organises workers, tools, storage, and rules

Computer system
      ↓
Linux kernel
      ↓
Organises applications, hardware, memory, and access
```

> **No Chief, no order. No operating system, no organised computer.**
