# Hardware and Software

## 🎯 Why Should I Care?

Most computer problems belong to one of two worlds: the physical equipment or the instructions running on it. Knowing the difference helps you ask whether a failure comes from hardware, software, or the way they interact.

## 🪨 Story — The Hunter and the Spear

A hunter owns a spear, a bow, and a stone axe. These are physical tools that can be seen, touched, and carried.

![A hunter carrying a physical tool](../images/01-before-linux/hunter-with-tool.png)

The hunter must also know how to choose a tool, aim it, use it safely, and complete the hunt. That knowledge provides instructions for using the physical equipment.

![A spear representing physical hardware](../images/01-before-linux/spear-hardware.png)

Without knowledge, the spear does nothing useful. Without a physical tool, knowledge alone cannot perform the task.

```text
Physical tool + Knowledge = Successful hunt
Hardware      + Software  = Working computer
```

## 🖼️ From the Cave to Technology

| Caveman World | Computer World |
|---|---|
| Spear, bow, and axe | Hardware |
| Hunting knowledge | Software |
| Hunter following instructions | Computer running a program |
| Completed hunt | Completed task |

## 🧠 Hardware

**Hardware** means the physical parts of a computer.

Examples include:

- CPU and RAM
- SSDs and hard drives
- Network cards
- Keyboards, mice, and monitors
- GPUs and power supplies

Hardware provides the ability to perform work, but it needs instructions.

## 🧠 Software

**Software** is a collection of programs and instructions that tells hardware what to do.

Examples include:

- Linux and Windows
- Web browsers
- Text editors
- Databases
- Games and mobile applications
- Web servers such as Nginx

Software is stored on hardware and executed using hardware.

## 🧠 How They Work Together

When you open a web browser:

1. The browser software provides instructions.
2. The CPU executes those instructions.
3. RAM holds the active program and data.
4. Storage keeps the browser's files.
5. The NIC sends and receives network data.
6. The monitor displays the result.

Neither side is useful alone.

## 💻 How This Appears in Linux

Linux can show whether something is a physical device, an executable program, or a running instance of that program:

```bash
lspci                         # List hardware connected through PCI
file /bin/ls                  # Identify what kind of software file /bin/ls is
command -V ls                 # Show which ls command the shell will run
ps -eo pid,comm,args --sort=pid  # Show running software processes
```

This is the key distinction: `lspci` discovers devices, `file` and `command` inspect stored software, and `ps` shows software currently executing. The hardware lesson inspects component capacity in detail; this lesson focuses on recognising the boundary between the two layers.

## ☁️ Production Reality

Engineers match software requirements to hardware or cloud resources:

- Databases often benefit from memory and fast storage.
- Web applications need enough CPU and network capacity.
- AI software may require GPUs and large amounts of memory.
- Containers package software, but still depend on host hardware.

Buying faster hardware cannot always fix inefficient software, and optimized software cannot exceed every physical limit.

## 🎯 Think Like an Engineer

An application becomes slow after an update, but the hardware has not changed. What evidence would help you decide whether the new software is the cause?

## 📌 Caveman Summary

```text
Spear     → Hardware
Knowledge → Software
Both      → Useful work
```

> **Hardware is the equipment. Software is the instructions. Together, they make a working computer.**
