# 01 — Network Fundamentals

> “A messenger without a road carries nothing.” — Chief Grog

## 🎯 Learning Objectives

- Define a network, packet, interface, client, and server.
- Distinguish LAN, WAN, and the Internet.
- Compare bandwidth with latency.
- Recognise common physical and logical topologies.
- Inspect host and interface identity safely.

## 🏕️ Caveman Story

Food Village has grain. Tool Village has axes. Water Village has wells. Without roads and messengers, each settlement remains isolated.

A road creates a path. A messenger divides a large order into manageable parcels. One villager requests supplies; another provides them. That is the beginning of a network.

## 🖼️ Big Concept Illustration

![Separate resource villages connected by request and response roads](../images/07-talking-between-villages/network-fundamentals-hero.png)

```text
Client                          Server
“May I have a tool?” ─request─→ “I provide tools”
                       ←response─
```

```text
Laptop ─┐
Server ─┼─ Switch ─ Router ─ WAN / Internet ─ Remote network
Printer ─┘       local LAN
```

## 📖 Concept Explained Simply

A **network** is a group of devices able to exchange data. A Linux machine may be a client, server, or both.

- **LAN:** a limited local area such as a home, office, or data-centre segment.
- **WAN:** connects networks over larger distances.
- **Internet:** a global network of networks.
- **Interface:** the logical doorway used to communicate, such as Ethernet, Wi-Fi, or loopback.
- **Packet:** a bounded unit carrying addressing, protocol information, payload, and integrity information.

Large messages are divided into packets so links can share capacity and failed pieces can be handled efficiently.

```text
Bandwidth = how much data can travel per second
Latency   = how long one journey takes
```

A wide road can carry many carts and still be far away. High bandwidth does not guarantee low latency.

Modern Ethernet LANs commonly resemble a **star** around a switch. Physical topology describes cables and radios; logical topology describes how traffic behaves.

## 🌍 Real Linux Example

An application on a cloud VM sends packets through a virtual interface. The provider’s virtual network carries them to another VM or gateway even though the “switches” are implemented in software.

The loopback interface, usually `lo`, lets applications communicate with the same machine through `127.0.0.1` or `::1` without leaving it.

## 🛠️ Commands Introduced

### `hostname` and `hostnamectl` — Identify the Host

```bash
hostname
hostnamectl
```

`hostname` prints the current host name. `hostnamectl` provides the static hostname and related system metadata on systemd-based distributions.

```bash
sudo hostnamectl set-hostname cave-server-01
```

Changing a hostname can affect prompts, certificates, monitoring, automation, and name resolution. Follow the naming policy in production.

### `ip link` — Inspect Network Doorways

```bash
ip link
ip link show dev lo
```

Important fields include interface name, flags such as `UP` and `LOWER_UP`, MTU, state, and link-layer address.

```bash
sudo ip link set dev eth0 up
sudo ip link set dev eth0 down
```

These mutate interface state. Do not bring down the interface carrying your remote session.

### `nmcli device status` — Check NetworkManager Devices

```bash
nmcli device status
```

Shows device, type, state, and active connection. It is relevant only where NetworkManager is installed and managing the device.

## 💡 Caveman Tip

An interface being `UP` means Linux has enabled it; `LOWER_UP` indicates the lower-level link is detected. Neither proves that addressing, routing, DNS, or an application is correct.

## ⚠️ Common Mistakes

- Assuming every Ethernet interface is named `eth0`.
- Confusing the hostname with an IP address.
- Calling Wi-Fi “the Internet.”
- Treating bandwidth and latency as the same measurement.
- Disabling a remote server’s active interface.

## 🧪 Hands-on Lab

### Mission: Inspect the Village Gates

1. Print the hostname and detailed host information.
2. List interfaces and find `lo`.
3. Identify the interface that is both `UP` and `LOWER_UP`.
4. Record its MTU and link-layer address.
5. If available, determine whether NetworkManager manages it.

Challenge: draw your machine, its interfaces, and which one reaches the LAN. Do not change any interface state.

## 📝 Quick Recap

```text
Device → interface → local network → router → remote network
Message → packets → shared links → destination
```

## 🧠 Interview Questions

1. What is the difference between a LAN, WAN, and the Internet?
2. Can one Linux machine be both client and server?
3. Why can a high-bandwidth connection still feel slow?
4. What is the purpose of the loopback interface?
5. What is the difference between `UP` and `LOWER_UP`?

## 📚 What's Next

Roads exist. Next, [02 — IP Addresses](02-ip-addresses.md) gives every network doorway a location.
