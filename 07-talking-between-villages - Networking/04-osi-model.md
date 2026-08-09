# 04 — The OSI Model

> “One worker should not translate, route, guard, and carry every message.” — Chief Grog

## 🎯 Learning Objectives

- Explain why networking uses layered models.
- Describe the seven OSI layers and the four-layer TCP/IP model.
- Follow encapsulation and de-encapsulation.
- Distinguish data, segments/datagrams, packets, frames, and bits.
- Use layers as a troubleshooting guide without treating them as rigid law.

## 🏕️ Caveman Story

A long-distance message passes through specialists. One understands the request, another formats it, another tracks the conversation, another divides it for transport, another selects the road, and another prepares it for the local path.

At the destination, a matching team reverses the work until the original request reaches the correct villager.

## 🖼️ Big Concept Illustration

![Seven village stations adding and removing layers from a messenger parcel](../images/07-talking-between-villages/osi-model-hero.png)

```text
7 Application    network services used by applications
6 Presentation   representation, encryption, compression
5 Session        conversation management
4 Transport      TCP/UDP, ports, delivery behaviour
3 Network        IP addressing and routing
2 Data Link      local frames, MAC addresses, switching
1 Physical       electrical, optical, or radio signals
```

## 📖 Concept Explained Simply

Layering lets each component solve a focused problem while exposing a useful interface to the layer above.

| OSI layer | Common ideas | Data unit |
| --- | --- | --- |
| 7–5 | HTTP, DNS, TLS, sessions, formats | Data |
| 4 | TCP, UDP, ports | Segment or datagram |
| 3 | IPv4, IPv6, routing | Packet |
| 2 | Ethernet, MAC, VLAN | Frame |
| 1 | Copper, fibre, radio | Bits |

Encapsulation adds control information as data moves down the stack:

```text
Application data
  ↓ add TCP/UDP information
Segment or datagram
  ↓ add IP information
Packet
  ↓ add local-link header/trailer
Frame
  ↓ encode
Bits/signals
```

The destination removes those layers in reverse. The practical TCP/IP model combines OSI Layers 5–7 as Application, keeps Transport and Internet, and combines Layers 1–2 as Link.

Real protocols do not always fit one OSI box perfectly. TLS, for example, is commonly discussed around the application/session/presentation area. Use the model to reason, not to force every implementation into a rigid label.

## 🌍 Real Linux Example

An HTTPS failure can be investigated from the bottom up: link detected, address assigned, route selected, TCP port reachable, TLS negotiation successful, then HTTP response correct.

Virtual switches, tunnels, overlays, and service meshes add layers, but the same questions remain: what is encapsulated, where, and which component removes it?

## 🛠️ Commands Introduced

### `ethtool` — Inspect an Ethernet Link

```bash
sudo ethtool eth0
sudo ethtool -i eth0
sudo ethtool -S eth0
```

The first view may show speed, duplex, auto-negotiation, and link detection. `-i` shows driver and firmware details. `-S` displays driver-specific counters whose names vary.

Do not change speed, duplex, offload, or negotiation settings without understanding both ends of the link.

### `lldpctl` — Discover the Local Link Neighbour

```bash
sudo lldpctl
```

When an LLDP daemon and supporting network are available, it may reveal the connected switch, port, device name, and VLAN-related information. No output does not prove the cable is disconnected.

## 💡 Caveman Tip

Say precisely where evidence belongs: an Ethernet **frame** carries an IP **packet**, which carries a TCP **segment** or UDP **datagram**.

## ⚠️ Common Mistakes

- Treating OSI as a perfect protocol implementation diagram.
- Calling every unit of network data a packet.
- Assuming every switch is only Layer 2 or every firewall only one layer.
- Starting at the application while ignoring link and route evidence.
- Changing physical-link parameters to “test” a production interface.

## 🧪 Hands-on Lab

### Mission: Follow the Messenger

For one HTTPS request, identify the application protocol, encryption mechanism, transport protocol, destination port, IP protocol, local-link frame type, and physical medium. Draw encapsulation in both directions.

Inspect your Ethernet link and driver where supported. Challenge: place a failed certificate, missing route, closed port, and disconnected cable at the most useful troubleshooting layer.

## 📝 Quick Recap

```text
Sender:      data → segment/datagram → packet → frame → bits
Destination: bits → frame → packet → segment/datagram → data
```

## 🧠 Interview Questions

1. Why are layered networking models useful?
2. What is the difference between a frame and an IP packet?
3. At which layer do ports belong?
4. How does the TCP/IP model map roughly to OSI?
5. Why should engineers avoid treating OSI as rigid law?

## 📚 What's Next

Layer 4 introduces two different messenger styles. Continue to [05 — TCP and UDP](05-tcp-and-udp.md).
