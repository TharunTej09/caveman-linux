# 09 — Network Troubleshooting

> “Do not rebuild every road. Find the first place the messenger disappears.” — Chief Grog

## 🎯 Learning Objectives

- Define a precise symptom and determine its scope.
- Test connectivity from local state to application response.
- Distinguish DNS, route, port, firewall, MTU, and application failures.
- Interpret timeout, refusal, loss, and path evidence carefully.
- Document root cause, fix, validation, and prevention.

## 🏕️ Caveman Story

A messenger never reaches Food Village. Chief Grog does not blame the mountain or rebuild every road. He checks the messenger’s cave, local gate, address, neighbourhood, route, bridge, remote guard, service door, and return journey—in order.

At each step he asks for evidence. The first failed expectation narrows the investigation.

## 🖼️ Big Concept Illustration

![Chief Grog checking each stage of a broken messenger route](../images/07-talking-between-villages/network-troubleshooting-hero.png)

```text
Application expectation
        ↓
Local service → interface → address/prefix → route → neighbour
        ↓
Gateway → network path → destination firewall → listening port
        ↓
Application protocol → response path
```

## 📖 Concept Explained Simply

Begin with four questions:

1. What should work?
2. What exactly fails?
3. Where is the first failing boundary?
4. What changed?

A useful symptom says: “Server A cannot establish TCP to `10.20.30.40:443` since 10:15, but DNS resolution and gateway reachability work.” Then determine whether the scope is one application, host, subnet, site, address family, direction, or every user.

Test progressively:

```text
loopback → local address → gateway → remote IP → DNS name
         → destination port → application response
```

Use earlier evidence without reteaching its syntax: `ip link`, `ip address`, `ip route`, `ip neighbour`, `dig`, `ss`, `nft`/UFW/firewalld, and `tcpdump`.

Common clues—not guarantees—include:

| Evidence | Investigate next |
| --- | --- |
| IP works, name fails | Resolver, DNS path, records, search domain, cache |
| Local subnet works, remote fails | Route, gateway, forwarding, return path |
| Immediate TCP refusal | No listener, wrong bind, or active rejection |
| TCP SYN retransmits without reply | Drop, path failure, unavailable host, or broken return path |
| Small traffic works, large transfers stall | Path MTU, tunnel overhead, blocked ICMP |
| Intermittent wrong host | Duplicate IP or unstable neighbour state |
| Forward and return paths differ | Stateful firewall and asymmetric routing |

Even with a healthy network, TLS certificates, authentication, virtual-host selection, proxies, databases, application crashes, and resource exhaustion can still break the service.

## 🌍 Real Linux Example

An application server cannot reach PostgreSQL at `10.20.20.25:5432/TCP`. The source interface and route are correct; the gateway and destination reply; TCP receives an immediate refusal. That evidence shifts attention from general connectivity to service state, listening port, and bind address.

In cloud and Kubernetes environments, repeat the same flow across every boundary: node or pod route, security group, network ACL, load balancer, Service/endpoint, NetworkPolicy, container bind, and application health.

## 🛠️ Commands Introduced

### `ping` — Test ICMP Echo Behaviour

```bash
ping -c 4 192.0.2.20
ping -c 4 example.com
ping -s 1400 -c 4 192.0.2.20
```

Read replies, round-trip time, and loss. A failed echo test does not prove the host is down because ICMP may be filtered; a successful one does not prove TCP port `443` works.

On Linux, a controlled path-MTU probe may use:

```bash
ping -M do -s 1472 -c 4 192.0.2.20
```

Account for protocol headers and avoid assuming one size fits IPv4, IPv6, tunnels, or every path.

### `traceroute` — Probe the Layer 3 Path

```bash
traceroute example.com
sudo traceroute -I example.com
sudo traceroute -T -p 443 example.com
```

Default probe behaviour varies by implementation. `-I` uses ICMP; `-T -p 443` uses TCP toward port `443`. Asterisks can mean filtered or rate-limited diagnostic replies even when forwarding continues.

### `mtr` — Observe Path Behaviour Over Time

```bash
mtr -rw -c 20 example.com
sudo mtr --tcp --port 443 -rw -c 20 example.com
```

Focus on end-to-end behaviour. Apparent loss at one intermediate router is not necessarily transit loss if later hops and the destination respond normally.

### `nc` — Test a Transport Port

```bash
nc -vz example.com 443
nc -vzu 192.0.2.53 53
```

TCP success confirms a transport connection, not correct application behaviour. UDP tests are less definitive because no handshake exists. Create listeners only in authorised disposable labs.

### `curl` — Test the Application Layer

```bash
curl -I https://example.com
curl -v --connect-timeout 5 https://example.com
curl -L https://example.com
curl --resolve example.com:443:192.0.2.20 https://example.com
```

`-I` requests headers, `-v` exposes DNS/connect/TLS/HTTP stages, `-L` follows redirects, and `--resolve` tests a chosen IP while preserving the hostname for TLS and HTTP. Verbose output can expose sensitive headers—review before sharing it.

### `iperf3` — Measure Authorised Throughput

```bash
iperf3 -s
iperf3 -c SERVER_IP
iperf3 -c SERVER_IP -R
iperf3 -c SERVER_IP -P 4
iperf3 -c SERVER_IP -u -b 20M
```

One endpoint runs server mode and the other connects. `-R` reverses direction, `-P` uses parallel streams, and `-u -b` requests UDP at a target rate. Tests generate significant traffic; coordinate them and avoid production saturation.

## 💡 Caveman Tip

Every command should answer a question. Write the hypothesis first, run the smallest safe test, record the result, and change only one variable.

## ⚠️ Common Mistakes

- Running every network command without a hypothesis.
- Testing only by name or only with `ping`.
- Ignoring IPv6 and the return route.
- Restarting networking before collecting evidence.
- Assuming a timeout always means firewall DROP.
- Running packet captures or throughput tests without authorisation.
- Fixing several variables at once and losing the root cause.

## 🧪 Hands-on Lab

### Final Mission: Restore Communication Between Villages

Scenario: application server `10.20.10.15/24` cannot connect to database server `10.20.20.25/24` on `5432/TCP`.

1. State the expected flow and exact symptom.
2. Verify source interface, address, prefix, and selected route using earlier lessons.
3. Test gateway, destination IP, and path.
4. Test TCP port `5432` and classify timeout, refusal, or success.
5. Confirm PostgreSQL’s listener and bind address.
6. Inspect host, network, and cloud firewall policy.
7. Capture only the relevant handshake attempt.
8. Correct one identified fault.
9. Retest transport and application behaviour.
10. Document root cause, evidence, fix, validation, and preventive action.

Challenge: introduce one DNS error and one MTU-related symptom separately. Prove each without changing unrelated configuration.

## 📝 Quick Recap

```text
Define → scope → verify local state → test route/path → test port
       → inspect firewall/listener → test application → capture if needed
       → fix one cause → validate → monitor → document
```

Evidence template:

```text
Source / destination / port / protocol:
Expected / actual / start time / recent change:
Interface / address / route / neighbour:
DNS / reachability / path / port / firewall:
Packet and application evidence:
Root cause / fix / validation / prevention:
```

## 🧠 Interview Questions

1. A server works by IP but not by name. What do you test?
2. Why can `ping` succeed while HTTPS fails?
3. What does immediate TCP refusal usually suggest?
4. How can asymmetric routing affect a stateful firewall?
5. Why may traceroute show asterisks even when the destination works?
6. How would you prove an MTU problem?
7. What evidence should be collected before restarting networking?

## 📚 What's Next

You can now follow a packet from application to destination and diagnose where it stops. Return to the [module map](README.md), complete the three-village project, then continue to server operations and production networking.
