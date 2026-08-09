# 05 — TCP and UDP

> “Some cargo needs confirmation; some messages need speed.” — Chief Grog

## 🎯 Learning Objectives

- Compare TCP and UDP accurately.
- Explain TCP connection setup, ordering, acknowledgements, and retransmission.
- Describe UDP datagrams and application-managed reliability.
- Explain sockets, listening endpoints, and ephemeral ports.
- Inspect sockets and capture packets responsibly.

## 🏕️ Caveman Story

Chief Grog can send a reliable caravan: establish contact, deliver ordered crates, confirm progress, and resend a missing crate. Or he can send fast messengers who deliver independent notes without waiting for confirmation.

Neither method is always better. The choice depends on what the application needs.

## 🖼️ Big Concept Illustration

![A reliable ordered caravan contrasted with fast independent messengers](../images/07-talking-between-villages/tcp-and-udp-hero.png)

```text
TCP handshake                 UDP
Client        Server          Sender ─datagram─→ Receiver
  SYN ───────→                no transport handshake
      ← SYN-ACK               no built-in acknowledgement
  ACK ───────→
```

## 📖 Concept Explained Simply

**TCP** is connection-oriented and provides an ordered byte stream, acknowledgements, retransmission, flow control, and congestion control. A normal connection starts with SYN → SYN-ACK → ACK.

Sequence numbers track bytes, and an acknowledgement normally indicates the next byte expected. Receiver flow control prevents overwhelming the endpoint; congestion control responds to network conditions. A normal close uses FIN/ACK exchanges.

**UDP** sends independent datagrams with low transport overhead. It has no built-in connection handshake, ordering, acknowledgement, or retransmission. Applications can add their own reliability—modern protocols such as QUIC do this over UDP.

Commonly, HTTPS, SSH, email, and database connections use TCP. DNS queries, voice, gaming, DHCP, and telemetry commonly use UDP, though real protocols may use both.

A socket endpoint combines IP address, port, and protocol. A flow is commonly identified by source IP, source port, destination IP, destination port, and protocol. Clients usually use a temporary **ephemeral source port** while servers listen on a known destination port.

## 🌍 Real Linux Example

A browser may connect from `192.168.1.10:53124` to `203.0.113.20:443/TCP`. The server listens on `443`; it does not need to listen on the client’s ephemeral port.

Kubernetes and cloud load balancers still ultimately forward transport traffic to sockets. A healthy load balancer cannot help if the application is not listening on the expected address and port.

## 🛠️ Commands Introduced

### `ss` — Inspect Sockets

```bash
ss -tuln
sudo ss -tulnp
ss -tn state established
ss -s
```

- `-t` TCP; `-u` UDP; `-l` listening; `-n` numeric output.
- `-p` process information, often requiring privilege; `-a` all sockets.

For listening sockets, read protocol, local address/port, and process. `127.0.0.1:8080` accepts only local traffic; `0.0.0.0:8080` listens on all IPv4 local addresses, subject to firewall and routing.

### `tcpdump` — Observe Packets

```bash
sudo tcpdump -D
sudo tcpdump -nn -i eth0 -c 20
sudo tcpdump -nn -i eth0 tcp port 443
sudo tcpdump -nn host 192.168.1.20
sudo tcpdump -nn -i eth0 -w capture.pcap
sudo tcpdump -nn -r capture.pcap
```

`-nn` prevents hostname and service-name resolution, `-i` chooses the interface, `-c` limits capture count, and `-w` writes a capture. Captures can expose credentials, tokens, internal addresses, and user data; collect the minimum required and protect the file.

## 💡 Caveman Tip

“UDP is faster” is too broad. UDP has less built-in transport behaviour; application design and network conditions decide real performance and reliability.

## ⚠️ Common Mistakes

- Saying UDP can never be reliable.
- Assuming every DNS exchange uses UDP.
- Confusing a port with a socket or connection.
- Expecting client and server to use the same port.
- Running unrestricted packet captures on sensitive systems.

## 🧪 Hands-on Lab

### Mission: Watch the Messengers

1. Display listening TCP and UDP sockets.
2. Find the process owning one safe listening socket.
3. Open an HTTPS connection and observe its established socket.
4. Capture only a small number of packets for TCP port `443`.
5. Identify SYN, SYN-ACK, and ACK.
6. Compare that flow with a DNS UDP exchange.

Challenge: explain why a listening socket proves local readiness but not remote reachability.

## 📝 Quick Recap

```text
TCP → connection + ordered byte stream + recovery mechanisms
UDP → independent datagrams + application chooses extra behaviour
Socket endpoint → IP + port + protocol
```

## 🧠 Interview Questions

1. What happens during the TCP three-way handshake?
2. What do sequence and acknowledgement numbers accomplish?
3. How do flow control and congestion control differ?
4. What identifies a network flow?
5. Why might DNS use TCP?

## 📚 What's Next

Users remember names, not addresses. [06 — DNS](06-dns.md) introduces the village directory.
