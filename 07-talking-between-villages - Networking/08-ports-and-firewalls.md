# 08 — Ports and Firewalls

> “Reaching the cave is not permission to enter every door.” — Chief Grog

## 🎯 Learning Objectives

- Explain ports, bindings, listening sockets, and common service ports.
- Distinguish inbound, outbound, stateful, and stateless filtering.
- Compare DROP and REJECT outcomes.
- Understand default-deny and least-privilege policy.
- Inspect basic `nftables`, UFW, and firewalld configuration safely.

## 🏕️ Caveman Story

One large cave contains a healer, tool keeper, and food store. Each service has a different door. A guard checks the messenger’s direction, destination door, message type, origin, and whether the journey belongs to an approved conversation.

An address finds the cave. A port finds the service. The firewall decides whether traffic may pass.

## 🖼️ Big Concept Illustration

![A village guard admitting approved messengers to specific service doors](../images/07-talking-between-villages/ports-and-firewalls-hero.png)

```text
Client → destination IP → protocol + port → firewall → listening socket

22/TCP SSH    53/UDP+TCP DNS    80/TCP HTTP    443/TCP HTTPS
```

## 📖 Concept Explained Simply

TCP and UDP ports are 16-bit numbers from `0` to `65535`. System or well-known ports are `0–1023`; registered ports are `1024–49151`; the remaining range is commonly used dynamically, though operating systems configure their actual ephemeral ranges.

A process may bind to:

- `127.0.0.1:8080`: local IPv4 loopback only.
- `192.168.1.20:8080`: one local address.
- `0.0.0.0:8080`: all local IPv4 addresses.
- `[::]:8080`: IPv6 wildcard, with IPv4 behaviour depending on system settings.

A **stateful** firewall tracks connection state and can allow reply traffic for an established flow. A **stateless** rule evaluates packets without that connection context.

`DROP` silently discards matching traffic; `REJECT` actively returns an error. Both can be appropriate. A production policy commonly starts with default deny, allows established traffic and required administration, then permits only documented service flows.

Host firewalls are only one layer. Cloud security groups, network ACLs, Kubernetes NetworkPolicies, load balancers, and application access controls can all affect a connection.

## 🌍 Real Linux Example

An Nginx server may listen on `0.0.0.0:443`, but clients still fail if the host firewall, cloud security group, route, or load balancer blocks the path. Conversely, an open firewall rule cannot help if no process is listening.

In containers, publishing a host port and permitting it through a firewall are distinct decisions. In Kubernetes, a Service port, container port, and NetworkPolicy must align.

## 🛠️ Commands Introduced

Use the firewall manager designed for the host. Do not mix front ends casually, because UFW and firewalld ultimately program underlying packet-filtering rules.

### `nft` — Inspect Native nftables Rules

```bash
sudo nft list ruleset
sudo nft list tables
```

Rules are organised as tables → chains → rules. Base chains attach to hooks such as input, forward, and output and have priorities and policies.

Mutation example for an authorised test host only:

```bash
sudo nft add rule inet filter input tcp dport 443 accept
```

Do not paste this blindly: the table and chain must already exist, ordering matters, and an unmanaged change may not persist.

### `ufw` — Use Ubuntu’s Firewall Front End

```bash
sudo ufw status verbose
sudo ufw status numbered
sudo ufw allow 443/tcp
```

Before enabling or changing UFW remotely, make sure the management path—commonly SSH—is explicitly allowed and recovery access exists.

### `firewall-cmd` — Use firewalld

```bash
sudo firewall-cmd --state
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
sudo firewall-cmd --add-service=https
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

Runtime and permanent configuration are separate. Test runtime policy first, then make the intended rule permanent and verify after reload.

## 💡 Caveman Tip

Document every allowed flow as **source → destination → protocol/port → reason → owner**. “Allow everything from the subnet” is rarely the least-privilege answer.

## ⚠️ Common Mistakes

- Opening a firewall port when no service is listening.
- Allowing a service on both TCP and UDP without need.
- Enabling default deny remotely before preserving management access.
- Assuming one host rule represents every cloud or container firewall layer.
- Making a runtime firewalld rule and expecting it to survive reboot.

## 🧪 Hands-on Lab

### Mission: Guard the Service Door

On a disposable VM with console access:

1. Identify one test service’s protocol, bind address, and port using `ss` from Lesson 05.
2. Inspect the active firewall manager and current policy.
3. Record a baseline connection test.
4. Permit only the required port from an appropriate source.
5. Verify allowed traffic and one denied port.
6. Confirm the management connection remains available.
7. Remove the temporary test rule using that firewall manager’s documented method.

Challenge: explain how timeout and immediate rejection might differ, while noting neither result proves a single root cause by itself.

## 📝 Quick Recap

```text
IP → host
port + protocol → application socket
firewall policy → permit, drop, or reject the flow
```

## 🧠 Interview Questions

1. What is the difference between a port and a socket?
2. What happens when a service binds only to `127.0.0.1`?
3. How do stateful and stateless filtering differ?
4. What is the difference between DROP and REJECT?
5. Why should runtime and persistent firewall configuration be verified separately?

## 📚 What's Next

All journey components now exist. [09 — Network Troubleshooting](09-network-troubleshooting.md) teaches how to find the exact broken step.
