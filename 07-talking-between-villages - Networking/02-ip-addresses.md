# 02 — IP Addresses

> “A messenger needs a destination, not just a road.” — Chief Grog

## 🎯 Learning Objectives

- Explain IPv4 and IPv6 addresses.
- Distinguish public, private, loopback, link-local, static, and dynamic addresses.
- Explain DHCP, NAT, and the default gateway at a practical level.
- Inspect addresses, saved connections, and route selection.

## 🏕️ Caveman Story

The village builds roads, but every cave looks similar. Chief Grog gives each cave a location marker. Messengers now know where a parcel begins and where it must end.

Local markers work inside the village. To reach the wider kingdom, messengers leave through the main gate, which presents the village’s public identity.

## 🖼️ Big Concept Illustration

![A messenger using unique cave symbols and a main village gateway](../images/07-talking-between-villages/ip-addresses-hero.png)

```text
Village network 192.168.1.0/24
├── Chief cave   192.168.1.10
├── Food cave    192.168.1.20
├── Tool cave    192.168.1.30
└── Gateway      192.168.1.1 → other networks
```

## 📖 Concept Explained Simply

An IP address identifies an **interface** on an IP network; it is not a permanent serial number for an entire device.

IPv4 uses 32 bits written as four decimal octets:

```text
192.168.1.10 = 11000000.10101000.00000001.00001010
```

IPv6 uses 128 bits written in hexadecimal. Consecutive zero groups may be compressed once:

```text
2001:db8:0:0:0:0:0:10 → 2001:db8::10
```

Private IPv4 ranges are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`. They are not normally routed directly on the public Internet. NAT can translate many private connections through a public address.

Important special addresses include IPv4 loopback `127.0.0.1`, IPv6 loopback `::1`, and IPv4 link-local `169.254.0.0/16`. A link-local address can appear when normal configuration, such as DHCP, is unavailable.

**DHCP** commonly follows Discover → Offer → Request → Acknowledge. A **static** address is manually configured or consistently reserved; a **dynamic** address is leased. The **default gateway** is the router used when no more specific route matches.

## 🌍 Real Linux Example

A cloud VM often receives a private address through provider-managed configuration while a public IP is translated or routed at the cloud edge. Replacing the VM may change either address, so DNS and automation should not assume an address is permanent.

Linux chooses an outgoing interface, gateway, and source address from its routing table—not from guesswork.

## 🛠️ Commands Introduced

### `ip address` — Inspect Interface Addresses

```bash
ip address
ip -4 address show
ip -6 address show dev eth0
```

Read the interface, address family, prefix length, scope, and lifetime. `scope host` is local to the machine; `scope link` stays on the link; `scope global` is usable beyond the local host subject to routing.

Temporary mutation examples:

```bash
sudo ip address add 192.168.1.50/24 dev eth0
sudo ip address delete 192.168.1.50/24 dev eth0
```

They may not survive reboot and can break remote access or create duplicate addresses.

### `ip route` — Inspect Route Selection

```bash
ip route
ip route get 203.0.113.20
```

`ip route get` shows the selected route, next hop, interface, and source address without sending a packet.

### `nmcli connection show` — Inspect Saved Profiles

```bash
nmcli connection show
nmcli connection show "Wired connection 1"
```

A connection profile is saved configuration; a device is the interface using it. Do not confuse the two.

### `dhclient` — Request a DHCP Lease

```bash
sudo dhclient eth0
sudo dhclient -r eth0
```

Some modern distributions use different DHCP clients or NetworkManager internally. Releasing a lease remotely can disconnect you.

## 💡 Caveman Tip

Ask “Which interface owns this address?” and “Which route will Linux select?” A machine can have several interfaces and several addresses at the same time.

## ⚠️ Common Mistakes

- Treating an IP address as permanent device identity.
- Confusing public, private, and link-local addresses.
- Forgetting the CIDR prefix when adding an address.
- Assuming a default route is always the route actually selected.
- Changing a remote host’s address or gateway without console access.

## 🧪 Hands-on Lab

### Mission: Give Every Cave an Address

1. Display all IPv4 and IPv6 addresses.
2. Identify loopback, private, global, and link-local scopes.
3. Find the default gateway.
4. Ask Linux which route and source address it would use for `203.0.113.20`.
5. Inspect the active NetworkManager profile if available.

Challenge: explain whether the visible address appears static or dynamically assigned, and state what evidence supports your answer.

## 📝 Quick Recap

```text
Interface + IP/prefix → local identity
Destination outside local network → selected route → gateway
Name → DNS → address (covered later)
```

## 🧠 Interview Questions

1. Why does an IP address belong to an interface rather than permanently to a device?
2. What is the purpose of a default gateway?
3. What are the private IPv4 ranges?
4. What does DHCP provide besides an address?
5. Why might `169.254.x.x` appear?

## 📚 What's Next

Addresses identify locations. [03 — Subnets and CIDR](03-subnets-and-cidr.md) explains which locations share a neighbourhood.
