# 07 — Talking Between Villages: Networking

> “A village that cannot communicate is a village that cannot grow.” — Chief Grog

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Follow a request from an application to a destination service.
- Explain addressing, subnetting, routing, DNS, ports, and transport protocols.
- Distinguish the jobs of switches, routers, and firewalls.
- Inspect Linux network state without changing it accidentally.
- Troubleshoot connectivity with evidence, one layer at a time.

## 🏕️ Caveman Story

Chief Grog’s village has organised caves, protected treasure, and healthy workers. But it cannot produce everything alone. Food Village has grain, Tool Village has axes, and Water Village controls the wells.

They need roads, addresses, messengers, gates, maps, and rules. Linux servers need the same things to communicate with users, databases, APIs, containers, cloud services, and other servers.

## 🖼️ Big Concept Illustration

![Chief Grog observing messengers travelling between connected villages](../images/07-talking-between-villages/networking-overview-hero.png)

```text
Application → Port → TCP/UDP → IP → Route → Local link → Firewall → Service
```

```text
Client Village                    Server Village
192.168.10.10                     10.20.1.50
      │                                 ▲
   Switch → Router → Internet → Router → Switch
                    │
                 DNS guide
```

## 📖 Concept Explained Simply

When you open `https://example.com`, several decisions happen:

```text
Name → DNS answer → destination IP → route → transport connection
     → destination port 443 → firewall decision → server response
```

Each lesson owns one part of that journey. The goal is not to memorise isolated commands; it is to know where a packet is, what decision comes next, and what evidence proves a failure.

| Lesson | Main question | Primary concept |
| --- | --- | --- |
| [01 — Network Fundamentals](01-network-fundamentals.md) | Why connect computers? | LAN, WAN, packets, bandwidth, latency |
| [02 — IP Addresses](02-ip-addresses.md) | How is an interface located? | IPv4, IPv6, DHCP, gateway |
| [03 — Subnets and CIDR](03-subnets-and-cidr.md) | Is a destination local or remote? | Prefixes, ranges, subnet design |
| [04 — OSI Model](04-osi-model.md) | What happens at each layer? | Layers and encapsulation |
| [05 — TCP and UDP](05-tcp-and-udp.md) | How is data transported? | Reliability, datagrams, sockets |
| [06 — DNS](06-dns.md) | How do names become addresses? | Resolution, records, caching |
| [07 — Switches and Routers](07-switches-and-routers.md) | How does traffic move? | MAC, neighbours, switching, routing |
| [08 — Ports and Firewalls](08-ports-and-firewalls.md) | How are services reached safely? | Ports and filtering policy |
| [09 — Network Troubleshooting](09-network-troubleshooting.md) | Where did communication fail? | Layered diagnosis |

## 🌍 Real Linux Example

A web application may need DNS to locate a database, a route to reach its subnet, TCP to create a reliable connection, port `5432` to reach PostgreSQL, and firewall permission in both the host and cloud network. One missing link breaks the request.

This same packet journey continues into Docker bridges, Kubernetes Services, cloud virtual networks, load balancers, and AI model-serving clusters.

## 🛠️ Commands Introduced

| Lesson | Commands taught here only |
| --- | --- |
| Network Fundamentals | `hostname`, `hostnamectl`, `ip link`, `nmcli device status` |
| IP Addresses | `ip address`, `ip route`, `nmcli connection show`, `dhclient` |
| Subnets and CIDR | `ipcalc`, `sipcalc` |
| OSI Model | `ethtool`, `lldpctl` |
| TCP and UDP | `ss`, `tcpdump` |
| DNS | `dig`, `host`, `resolvectl`, `getent hosts` |
| Switches and Routers | `ip neighbour`, `bridge`, `arping`, `tracepath` |
| Ports and Firewalls | `nft`, `ufw`, `firewall-cmd` |
| Network Troubleshooting | `ping`, `traceroute`, `mtr`, `nc`, `curl`, `iperf3` |

Commands may appear in later missions, but their syntax is explained only in their teaching home.

## 💡 Caveman Tip

Always describe a network test with four facts: **source, destination IP or name, port, and protocol**. “The network is broken” is not a diagnosis.

## ⚠️ Common Mistakes

- Treating the Internet, a LAN, and Wi-Fi as the same thing.
- Assuming successful `ping` proves an application works.
- Changing routes, interfaces, or firewall rules during a remote session without recovery access.
- Troubleshooting only IPv4 when the application selected IPv6.
- Running many commands without a hypothesis or recording evidence.

## 🧪 Hands-on Lab

### Module Mission: Connect Three Villages

Build a disposable lab with a client subnet, a router, and a server subnet. Give every interface an address, verify routes and neighbours, resolve a hostname, expose HTTP, allow only required ports, capture a TCP handshake, then deliberately break DNS, routing, and firewall policy one at a time.

For each failure, record what should work, the first failing layer, the evidence, the fix, and the final validation.

## 📝 Quick Recap

```text
Need to communicate
       ↓
Address + subnet + route
       ↓
Name resolution + transport + port
       ↓
Switches + routers + firewall
       ↓
Destination service
```

## 🧠 Interview Questions

1. How does a host decide whether a destination is local or remote?
2. What is the difference between a frame, packet, segment, and datagram?
3. Why can a name fail while its IP address still works?
4. What does a listening socket prove—and what does it not prove?
5. How would you investigate a timeout differently from a refusal?

## 📚 What's Next

Begin with [01 — Network Fundamentals](01-network-fundamentals.md) and build the road between two villages.

## 🧭 Chapter Navigation

[← The Village Workers](../06-the-village-workers-%20Processes%20and%20Services/README.md) · [Course Home](../README.md) · [Next: Running the Village →](../08-running-the-village-operateServers/README.md)
