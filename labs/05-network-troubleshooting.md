# Lab 05 — Troubleshoot the Village Road

## 🎯 Mission

Diagnose connectivity in layers: interface, address, route, DNS, transport, and application.

## Prerequisites

- A Linux VM with network access
- `ip`, `ping`, `ss`, `getent`, and `curl`

## ⚠️ Safety

This lab is read-only. Do not change routes, DNS, firewall rules, or cloud security groups on a production system.

## Starting State

Choose one known HTTPS destination allowed by your environment, such as `example.com`.

## Tasks

1. Check interfaces and assigned addresses:

   ```bash
   ip -brief address
   ```

2. Check the route used for an internet address:

   ```bash
   ip route
   ip route get 1.1.1.1
   ```

3. Test the local TCP/IP stack and default gateway:

   ```bash
   ping -c 2 127.0.0.1
   ping -c 2 GATEWAY_IP
   ```

4. Resolve the destination name:

   ```bash
   getent ahosts example.com
   ```

5. Test the application and inspect local sockets:

   ```bash
   curl -I --max-time 10 https://example.com
   ss -tn
   ```

6. Write a short evidence table: layer checked, command, observation, and conclusion.

## ✅ Verification

- A non-loopback interface has an address.
- A default route exists when external access is expected.
- Loopback responds.
- `getent` returns one or more destination addresses.
- `curl` completes an HTTPS request or returns an error that clearly identifies the failing layer.

## Troubleshooting Clues

| Observation | Likely investigation |
| --- | --- |
| No interface address | VM adapter, DHCP, or interface state |
| No default route | Network configuration or DHCP |
| IP works but name fails | DNS resolver path |
| DNS works but TCP times out | Route, firewall, proxy, or destination availability |
| TCP connects but HTTP fails | TLS, virtual host, authentication, or application |

Some networks block ICMP, so a failed `ping` alone does not prove that the destination is down.

## Cleanup

No system changes were made. Keep your evidence table as a reusable troubleshooting checklist.

## 🧠 Think Like an Engineer

Why is “the network is down” an incomplete diagnosis? State the exact layer and evidence you would include in a useful incident update.
