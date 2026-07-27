# Why Computers Need an Operating System

## Big Question

Who organizes all the hardware and software inside a computer?

## Story

The village already has everything it needs:

- Workers ready to perform tasks
- Food and tools ready to be used
- Storage caves filled with resources
- Roads connecting different parts of the village

![Workers and tools in the village](../images/SH6.png)

But there is one major problem: **nobody is in charge**.

Without someone organizing the village:

- Two workers grab the same spear at the same time.
- One worker fills every storage room and leaves no space for anyone else.
- Someone takes another person's tools without permission.
- Important jobs wait while less important jobs use all the workers.
- Nobody controls who may enter protected caves.

The workers exist. The tools exist. The storage exists. The roads exist. Yet nothing works properly.

The result is **chaos**.

![An unorganized village in chaos](../images/SH7.png)

## The Chief Arrives

The village needs a chief who can organize people, resources, and rules.

The chief decides:

- Who works
- Who waits
- Who uses each tool
- Who stores food and where it is stored
- Which jobs are most important
- Who protects the treasure
- Who is allowed to enter

![The chief organizing the village](../images/SH8.png)

In our computer story, the chief is the **operating system**.

For this course, that operating system is **Linux**.

## What Is an Operating System?

An **operating system (OS)** is the main software that manages a computer's hardware, runs programs, controls access to resources, and provides a way for users to interact with the computer.

Linux does for a computer what the chief does for the village: it keeps everything organized and makes sure resources are used safely and fairly.

## From the Village to Linux

| Village | Computer | What Linux Does |
|---|---|---|
| Workers | CPU processes | Decides which process runs and for how long |
| Working space | RAM | Gives programs memory and prevents unsafe conflicts |
| Storage caves | SSD and files | Organizes data into files and directories |
| Roads | Network connections | Controls communication between computers |
| Tools | Hardware devices | Helps programs use keyboards, disks, network cards, and other devices |
| Treasure guards | Security controls | Protects files and system resources |
| Entry rules | Users and permissions | Decides who can access or change something |
| Chief | Linux | Coordinates the entire system |

## What Linux Manages

### 1. Processes — Who Works and Who Waits

A running program is called a **process**.

Many processes may want to use the CPU at the same time. Linux schedules them, giving each process a turn and deciding which work should run first.

```text
Many processes  →  Linux scheduler  →  CPU time
```

Without this coordination, programs could interfere with one another or one program could take control of the CPU forever.

### 2. Memory — Who Gets Working Space

Programs need RAM while they are running. Linux gives each process the memory it needs and keeps processes separated.

This is like the chief assigning each worker a workspace so that nobody takes over the entire cave or damages another worker's materials.

### 3. Storage — Where Information Is Kept

Linux organizes information on storage devices using **files** and **directories**.

It keeps track of where data is stored, how it is named, and who is allowed to use it—just as the chief decides where food, weapons, and treasure belong.

### 4. Permissions — Who Can Enter

Not every person should be allowed to enter every cave. In the same way, not every user or program should be allowed to read, change, or delete every file.

Linux uses users, groups, and permissions to control access and protect the system.

### 5. Devices — Who Uses Each Tool

Programs need a safe way to use hardware such as disks, keyboards, screens, printers, and network cards.

Linux communicates with these devices through **device drivers** and coordinates their use so programs do not fight over the same hardware.

### 6. Networking — How Messages Travel

Linux manages network connections and helps programs send and receive information. It controls how data moves between the computer and other devices, like a chief maintaining the village roads and messenger system.

## The Complete Picture

Applications do not normally control hardware directly. They ask the operating system for what they need.

```text
User
  ↓
Applications
  ↓
Linux Operating System
  ↓
Hardware: CPU, RAM, SSD, NIC, and other devices
```

Linux stands between applications and hardware, coordinating requests and keeping the computer stable, useful, and secure.

## Simple Definition

**Linux is the chief of the computer: it decides who works, who waits, where information is stored, which devices are used, and who is allowed access.**
