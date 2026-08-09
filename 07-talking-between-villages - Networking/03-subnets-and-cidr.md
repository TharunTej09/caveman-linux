# 03 — Subnets and CIDR

> “Good boundaries tell a messenger what is local and what needs a gate.” — Chief Grog

## 🎯 Learning Objectives

- Explain why networks are divided into subnets.
- Read CIDR prefixes and subnet masks.
- Calculate basic IPv4 network, broadcast, and host ranges.
- Decide whether two addresses are in the same subnet.
- Apply subnet planning to cloud networks.

## 🏕️ Caveman Story

The village grows until hunters, farmers, builders, and guards crowd one enormous space. Chief Grog creates neighbourhoods with clear boundaries.

Inside a neighbourhood, messengers deliver directly. To reach another neighbourhood, they use a gateway. The boundaries improve organisation, security, address management, and fault isolation.

## 🖼️ Big Concept Illustration

![Chief Grog dividing a large settlement into organised neighbourhoods](../images/07-talking-between-villages/subnets-and-cidr-hero.png)

```text
10.0.0.0/16
├── 10.0.1.0/24  Web
├── 10.0.2.0/24  Application
├── 10.0.3.0/24  Database
└── 10.0.4.0/24  Management
```

## 📖 Concept Explained Simply

CIDR tells us how many leading address bits identify the network:

```text
192.168.1.10/24
             └─ 24 network bits; 8 host bits

/24 mask = 11111111.11111111.11111111.00000000
         = 255.255.255.0
```

For IPv4:

```text
total addresses = 2^(32 - prefix)
traditional usable hosts = total - network - broadcast
```

For `192.168.1.0/24`, the network is `.0`, traditional host range is `.1`–`.254`, and broadcast is `.255`.

Example: `192.168.1.70/26`. A `/26` has blocks of 64 addresses. `.70` falls in `.64`–`.127`:

| Item | Address |
| --- | --- |
| Network | `192.168.1.64` |
| First host | `192.168.1.65` |
| Last host | `192.168.1.126` |
| Broadcast | `192.168.1.127` |

Two IPv4 hosts can communicate directly at Layer 3 when their addresses, interpreted with the relevant prefix, identify the same subnet. Otherwise, a router is required.

`/31` is useful on IPv4 point-to-point links and `/32` identifies one address. IPv6 LANs commonly use `/64`; do not blindly apply IPv4 broadcast assumptions to IPv6.

## 🌍 Real Linux Example

A cloud virtual network might reserve separate subnets for public entry points, applications, databases, and management. Cloud platforms reserve some addresses, and container or Kubernetes growth can consume far more addresses than node count suggests.

Plan for current systems, scaling, load balancers, private endpoints, cluster nodes, and future subnets. Overlapping CIDRs make routing and network peering difficult or impossible.

## 🛠️ Commands Introduced

### `ipcalc` — Calculate IPv4 Boundaries

```bash
ipcalc 192.168.1.70/26
```

Depending on implementation, output includes address, netmask, network, host range, broadcast, wildcard, and host count. Verify that the package’s interpretation matches your environment.

### `sipcalc` — Calculate IPv4 or IPv6 Prefixes

```bash
sipcalc 192.168.1.70/26
sipcalc 2001:db8:1234:1::/64
```

Both utilities may require package installation. Use them to verify reasoning—not to replace understanding the network boundary.

## 💡 Caveman Tip

The prefix is the boundary. Never decide “same network” by comparing only the first three decimal octets; that shortcut works for some `/24` examples and fails elsewhere.

## ⚠️ Common Mistakes

- Believing `/24` means 24 available hosts.
- Assigning a traditional network or broadcast address to a host.
- Creating overlapping subnets.
- Forgetting cloud-reserved addresses and future growth.
- Memorising decimal masks without understanding prefix boundaries.

## 🧪 Hands-on Lab

### Mission: Divide the Growing Village

Divide `10.20.0.0/24` into four equal subnets. For each, record network, prefix, broadcast, and traditional usable host range. Assign them to web, database, monitoring, and management zones.

Expected networks: `10.20.0.0/26`, `10.20.0.64/26`, `10.20.0.128/26`, and `10.20.0.192/26`. Calculate manually, then verify with `ipcalc` or `sipcalc`.

Challenge: explain why `10.20.0.63` cannot normally be assigned to a host in the first subnet.

## 📝 Quick Recap

```text
IP address + prefix → network boundary
same subnet         → direct Layer 3 delivery
different subnet    → gateway and routing
```

## 🧠 Interview Questions

1. What does `/26` mean?
2. How many addresses are in an IPv4 `/27`?
3. What are the network and broadcast addresses for `192.168.5.130/25`?
4. Why are overlapping subnets a problem?
5. Why is `/64` important in IPv6 LAN design?

## 📚 What's Next

Subnets describe boundaries. [04 — OSI Model](04-osi-model.md) follows the specialised workers who prepare every message for travel.
