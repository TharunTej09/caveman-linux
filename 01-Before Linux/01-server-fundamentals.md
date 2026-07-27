# Server Fundamentals

## 🎯 Why Should I Care?

Servers power most digital services you use:

- Websites and mobile applications
- Email and online banking
- Cloud platforms
- Docker and Kubernetes workloads
- Data pipelines and AI applications

Understanding what a server does gives you a reason to learn Linux: Linux is one of the main operating systems used to run and manage servers.

## 🪨 Story — The Village Has a Storage Problem

One hundred cavemen live together. Every day they need food, water, weapons, tools, and medicine.

![A caveman village sharing resources](../images/01-before-linux/village-community.png)

At first, everyone keeps supplies inside their own cave. Soon:

- Food goes missing.
- Weapons are difficult to find.
- Tools are duplicated or forgotten.
- Some caves have too much while others have nothing.

Chief Grog creates one protected **storage cave** where shared resources can be organized and provided to the village.

![The village's shared storage cave](../images/01-before-linux/shared-storage-cave.png)

When a hunter needs a spear, the hunter asks the storage keeper. The keeper finds the spear and returns it.

![The storage cave providing a shared service](../images/01-before-linux/storage-cave-server.png)

In computing, the shared storage cave behaves like a **server**.

## 🖼️ From the Cave to Technology

![A hunter communicating with the storage cave](../images/01-before-linux/client-server-flow.svg)

| Caveman World | Computer World |
|---|---|
| Hunter | Client |
| Storage cave | Server |
| Village road | Network |
| Asking for a spear | Request |
| Receiving a spear | Response |
| Food, tools, and medicine | Data, applications, and services |

## 🧠 What Is a Server?

A **server** is a computer or software system that provides resources or services to other computers over a network.

The word *server* can describe:

1. A physical or virtual computer running server software.
2. A program that listens for requests and sends responses.

The computers or applications making those requests are called **clients**.

```text
Client  ── Request ──>  Server
Client  <─ Response ──  Server
```

## 🧠 Common Server Roles

| Server Role | What It Provides |
|---|---|
| Web server | Websites and web content |
| File server | Shared files and directories |
| Database server | Stored and organized data |
| Email server | Email delivery and storage |
| Application server | Business logic and application features |
| Media server | Video, audio, and images |

One server can perform several roles, and one service can also be spread across many servers.

## 💻 How This Appears in Linux

Linux administrators often begin by identifying a server and checking its basic health:

```bash
hostname
uptime
free -h
df -h
ip addr
```

| Command | What It Helps You See |
|---|---|
| `hostname` | Which server you are using |
| `uptime` | How long it has run and its current load |
| `free -h` | Available and used memory |
| `df -h` | Filesystem space |
| `ip addr` | Network interfaces and IP addresses |

You do not need to memorize the output yet. For now, notice that Linux provides tools for observing and managing the server.

## ☁️ Production Reality

In production systems:

- AWS EC2, Azure Virtual Machines, and Google Compute Engine provide virtual servers.
- Docker containers commonly run applications on Linux hosts.
- Kubernetes coordinates containerized applications across groups of servers.
- Databases and data platforms run services that accept client requests.
- AI model servers accept prompts or data and return generated results.

Large services rarely depend on only one machine. Engineers use multiple servers so the service can handle more users and continue working when a machine fails.

## 🎯 Think Like an Engineer

The village grows from 100 people to one million. What is likely to become a problem first: storage space, road capacity, the number of storage workers, or security?

How could Chief Grog prevent the entire village from depending on one storage cave?

## 📌 Caveman Summary

```text
Hunter       → Client
Village road → Network
Storage cave → Server
Spear        → Resource
Ask          → Request
Receive      → Response
```

> **A client asks, a server provides, and a network connects them.**

