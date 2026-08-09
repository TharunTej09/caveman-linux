# 07 — Switches and Routers

> “The local guide knows every cave; the road chief knows every village.” — Chief Grog

## 🎯 Learning Objectives

- Distinguish Layer 2 switching from Layer 3 routing.
- Explain MAC addresses, ARP, and IPv6 neighbour discovery.
- Describe forwarding tables, VLANs, gateways, and longest-prefix matching.
- Inspect Linux neighbours and software bridges.
- Follow local and routed packet delivery.

## 🏕️ Caveman Story

Inside one village, a local guide learns which path leads to each cave. For a different village, the messenger goes to the gate, where a road chief selects the best known route.

The guide is like a switch. The road chief is like a router. They solve different parts of the same journey.

## 🖼️ Big Concept Illustration

![A local junction guide and road chief forwarding messengers within and between villages](../images/07-talking-between-villages/switches-and-routers-hero.png)

```text
Same subnet:
Host A → resolve destination MAC → switch → Host B

Different subnet:
Host A → resolve gateway MAC → switch → router → next network → Host B
```

## 📖 Concept Explained Simply

A **switch** normally forwards Ethernet frames within a Layer 2 domain using a learned MAC-address table. It learns source MAC locations and forwards known destinations to the matching port. Broadcasts and unknown destinations may be flooded within the VLAN.

A **router** forwards IP packets between Layer 3 networks. A host compares the destination with its own prefix. If remote, it sends the frame to the gateway’s MAC address while keeping the remote IP as the packet destination.

IPv4 **ARP** maps a local IPv4 address to a MAC address. IPv6 performs related neighbour discovery with ICMPv6. Linux stores results in a neighbour table with states such as `REACHABLE`, `STALE`, `DELAY`, `PROBE`, and `FAILED`.

A **VLAN** creates a separate logical Layer 2 broadcast domain over shared switching infrastructure. Communication between VLANs requires Layer 3 routing and policy.

Routers choose the most specific matching route—**longest-prefix match**. A `/24` route wins over a matching `/16`, which wins over a default `/0` route. Route metrics help choose among otherwise comparable routes.

## 🌍 Real Linux Example

Linux can act as a host, software switch, or router. Container platforms commonly attach namespaces to Linux bridges; cloud networks implement switching and routing virtually; Kubernetes overlays may encapsulate traffic between nodes.

When troubleshooting, distinguish the IP destination from the next-hop MAC destination. For remote traffic, the first Ethernet frame targets the gateway—not the final remote server.

## 🛠️ Commands Introduced

### `ip neighbour` — Inspect Address-to-Link Resolution

```bash
ip neighbour
ip neighbour show dev eth0
```

Read IP, interface, link-layer address, and neighbour state. `FAILED` suggests local resolution failed; `STALE` is not automatically a fault.

### `bridge` — Inspect Linux Software Switching

```bash
bridge link
bridge fdb show
bridge vlan show
```

These views show bridge ports, the forwarding database, and VLAN membership. Output is meaningful only when Linux bridging is configured.

### `arping` — Test IPv4 Local-Link Ownership

```bash
sudo arping -I eth0 -c 3 192.168.1.1
sudo arping -D -I eth0 -c 3 192.168.1.50
```

The first asks for a local IPv4 neighbour. `-D` performs duplicate-address detection before assigning an address. ARP does not cross routers.

### `tracepath` — Observe the Routed Path and MTU

```bash
tracepath example.com
```

Uses increasing hop limits and can report path-MTU information without the same privileges some traceroute modes require. Missing hop replies do not prove forwarding stopped.

## 💡 Caveman Tip

For remote traffic, the destination IP remains remote while the first frame’s destination MAC belongs to the local gateway.

## ⚠️ Common Mistakes

- Saying switches use IP addresses for ordinary Layer 2 forwarding.
- Expecting ARP to discover a host across a router.
- Treating a `STALE` neighbour entry as failure.
- Confusing the default gateway with DNS.
- Forgetting VLAN boundaries and return routes.

## 🧪 Hands-on Lab

### Mission: Follow the Local Guide

1. View the neighbour table before and after contacting a local gateway.
2. Identify the gateway’s MAC and state.
3. If using containers or VMs, inspect any Linux bridge and forwarding entries.
4. Trace a path to a remote test destination.
5. Draw the destination IP and destination MAC for the first hop.

Challenge: describe what would fail if the correct IP route existed but neighbour resolution for the gateway failed.

## 📝 Quick Recap

```text
Switch → local frames using MAC knowledge
Router → packets between IP networks using routes
ARP/ND → local IP-to-link neighbour discovery
```

## 🧠 Interview Questions

1. How does a switch learn its forwarding table?
2. What does ARP do, and where does it operate?
3. How does longest-prefix matching work?
4. Why does remote traffic use the gateway’s MAC address?
5. What problem does a VLAN solve?

## 📚 What's Next

The road reaches the server, but a specific guarded door must admit it. Continue to [08 — Ports and Firewalls](08-ports-and-firewalls.md).
