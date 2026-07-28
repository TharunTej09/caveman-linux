# 06 — Linux Server Health and Troubleshooting

## 🧠 Big Question

> **How does the Chief know whether the village is healthy—and what should he check when something goes wrong?**

A server can be powered on and still be unhealthy. It may be slow, out of storage, disconnected from the network, or running a failed service.

> **Why should I care?** Installing Linux is only the beginning. Production engineers must recognise problems, find their causes safely, restore service, and prevent the same incident from happening again.

---

## 🪨 Caveman Story

Every morning, Chief Grog walks through the village.

He checks:

- whether the **workers** are overloaded;
- whether the **working tables** have enough room;
- whether the **food caves** are becoming full;
- whether the **roads** are open;
- whether each village service is operating;
- and whether the **village record book** contains warnings.

One morning, the spear workshop stops delivering tools.

Chief Grog does not immediately replace the workshop or punish a worker. First, he asks:

1. What exactly is broken?
2. When did it begin?
3. Is the whole village affected, or only the workshop?
4. Are the workers, tables, storage caves, and roads healthy?
5. What does the village record book say?

He discovers that the workshop itself is running, but its storage cave is full. He safely clears old, approved records, confirms that the workshop can deliver spears again, and creates an alert so the cave cannot fill silently next time.

That is troubleshooting: **observe, narrow down, fix the cause, verify recovery, and prevent recurrence**.

---

## 🖼 Story Diagram

```text
                    Chief Grog
                         │
             “Is the village healthy?”
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
     Workers       Working tables    Storage caves
       CPU               RAM              Disk
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  Roads and gates
                  Network and ports
                         │
                         ▼
                  Village services
              Processes and systemd units
                         │
                         ▼
                Village record book
                        Logs
                         │
                         ▼
                Find and fix the cause
                         │
                         ▼
                 Verify for the user
```

---

## 🧩 Caveman → Computer Mapping

| Caveman Village | Linux Server | Health Question |
| --- | --- | --- |
| Chief Grog | Linux administrator | Who investigates and coordinates recovery? |
| Workers | CPU and processes | Is too much work competing for processing time? |
| Working tables | RAM and swap | Is there enough temporary working space? |
| Food and storage caves | Filesystems and disks | Is storage full, slow, or unavailable? |
| Roads | Network interfaces and routes | Can traffic reach the correct destination? |
| Village gates | Network ports and firewall rules | Is the service reachable through the expected port? |
| Workshop | Application or systemd service | Is the required service running correctly? |
| Village record book | System and application logs | What happened, and when? |
| Village doctor | Troubleshooting process | How do we diagnose and restore health safely? |
| Morning inspections | Monitoring and alerts | Can trouble be detected before users report it? |

> A healthy server is not merely running. Its required services must have enough resources and must be reachable by their users.

---

## 💻 Technical Explanation

### What does “healthy” mean?

A Linux server is healthy when it can provide its intended service reliably. Health therefore depends on both the machine and the workload:

- CPU has enough capacity;
- memory pressure is controlled;
- filesystems have free space and inodes;
- network interfaces, routes, and name resolution work;
- required services are running and listening;
- logs do not show unresolved failures; and
- users can complete the action they expect.

A database server and a web server may have different healthy values. Learn the normal baseline for each system before deciding that a number is “high” or “low.”

### The safe troubleshooting workflow

```text
Identify the correct server
          ↓
Define and reproduce the symptom
          ↓
Establish when the problem started
          ↓
Check CPU, memory, disk, and network
          ↓
Inspect the affected process or service
          ↓
Read relevant logs and recent changes
          ↓
Form a hypothesis and test it
          ↓
Apply the smallest safe fix
          ↓
Verify the service from the user's view
          ↓
Record the cause and prevent recurrence
```

Do not begin by rebooting, restarting everything, or deleting files. Those actions can remove evidence, interrupt healthy workloads, and hide the real cause.

### Symptoms are not root causes

“The website is down” is a symptom. Possible causes include:

- the web service stopped;
- the configuration is invalid;
- the port is not listening;
- the disk is full;
- DNS points to the wrong address;
- a firewall blocks traffic;
- or a database dependency is unavailable.

Troubleshooting moves from the visible symptom toward evidence of the underlying cause.

### The four golden signals

Production teams often begin with four broad signals:

| Signal | Meaning | Example |
| --- | --- | --- |
| Latency | How long work takes | A page needs 10 seconds to load |
| Traffic | How much work arrives | Requests per second |
| Errors | How much work fails | HTTP 500 responses |
| Saturation | How full a resource is | CPU queue, memory pressure, or disk usage |

Linux commands help investigate these signals on one server. Monitoring systems show their history across many servers.

---

## 🌍 Real-World Example

Users report that a website is unavailable.

```text
Confirm the report with curl
          ↓
Check whether Nginx is active
          ↓
Check whether ports 80 or 443 are listening
          ↓
Read the Nginx journal
          ↓
Check disk, memory, and CPU pressure
          ↓
Correct the evidence-backed cause
          ↓
Test the website again
```

If the log says `No space left on device`, restarting Nginx is not the real fix. The engineer must identify what filled the filesystem, safely recover space, restart only if necessary, verify the website, and improve retention or alerting.

---

## ☁ Cloud Example

In AWS, Azure, or Google Cloud, server health has two views:

```text
Cloud platform view
VM state • disk • network rules • load balancer health
                     +
Linux guest view
CPU • RAM • filesystem • processes • services • logs
                     ↓
              Complete diagnosis
```

A VM can appear “running” in the cloud console while its application has failed. Conversely, Linux may be healthy while a cloud firewall rule or load balancer prevents users from reaching it.

Production engineers combine Linux evidence with cloud metrics, health checks, audit logs, and monitoring alerts.

---

## 🤖 AI Infrastructure Example

An AI inference server has additional health layers:

```text
Linux host health
CPU • RAM • disk • network
          ↓
GPU health
memory • temperature • utilisation • driver
          ↓
Model server health
process • port • logs • queue
          ↓
Inference health
latency • errors • tokens per second
```

A model response may be slow because the CPU is saturated, GPU memory is full, model weights are still loading, requests are queued, or storage cannot read data fast enough. A single command rarely tells the whole story.

On supported NVIDIA systems, `nvidia-smi` adds GPU-specific evidence. General CPU, memory, service, network, and log checks still remain essential.

---

## ⚡ Linux Commands

These commands belong to this lesson because they answer diagnostic questions. Some inspect concepts seen earlier, but here they are combined into a structured incident investigation.

### 1. Confirm the server and incident time

```bash
hostname                    # Which server am I investigating?
date                        # What time does this server report?
uptime                      # How long has it run, and what is its load average?
```

Always confirm the hostname before changing anything. Accurate time matters when matching a user report to log entries.

`uptime` shows load averages for the last 1, 5, and 15 minutes. Load includes tasks running on the CPU and tasks waiting for certain resources. Compare it with CPU count and the server's normal baseline; a load value is not automatically good or bad.

```bash
nproc                       # Show the number of available processing units
```

### 2. Inspect CPU and running work

```bash
top                         # Live view of load, CPU, memory, and processes
htop                        # Friendlier interactive view, if installed
ps -eo pid,ppid,stat,%cpu,%mem,comm --sort=-%cpu | head
```

In `top`, check overall CPU use, load, process count, and the processes consuming the most resources. Press `q` to exit.

The `ps` command creates a snapshot sorted by CPU consumption. Important fields are:

| Field | Meaning |
| --- | --- |
| `PID` | Process identifier |
| `PPID` | Parent process identifier |
| `STAT` | Process state |
| `%CPU` | Recent CPU consumption |
| `%MEM` | Percentage of physical memory used |
| `COMMAND` | Process name |

High CPU may be legitimate during busy work. Identify the process and workload before sending a signal or stopping it.

### 3. Inspect memory pressure

```bash
free -h                     # Summarise RAM and swap usage
vmstat 1 5                  # Sample processes, memory, paging, I/O, and CPU
ps -eo pid,%mem,rss,comm --sort=-%mem | head
```

With `free -h`, focus on **available** memory rather than only **free** memory. Linux uses spare RAM as cache and can reclaim much of it when applications need space.

In `vmstat`, persistent swap-in (`si`) or swap-out (`so`) activity can indicate memory pressure. One short sample is evidence, not a complete conclusion.

`RSS` in the `ps` output is the process's resident memory in KiB.

### 4. Inspect filesystem capacity and inodes

```bash
df -h                       # Show capacity used on mounted filesystems
df -i                       # Show inode usage
du -xh --max-depth=1 /var 2>/dev/null | sort -h
```

`df -h` answers, “Which filesystem is full?” The `Use%` column is the first clue.

`df -i` checks inodes—the filesystem records used to represent files. A filesystem can have free bytes but be unable to create files because all inodes are used.

`du` answers, “Which directory is using the space?” Start with a specific, relevant path such as `/var`; scanning the whole server can be slow. Never delete an unknown file merely because it is large.

### 5. Inspect a service

```bash
systemctl status nginx --no-pager       # Current Nginx state and recent messages
systemctl is-active nginx               # Return whether Nginx is active
systemctl list-units --state=failed      # Show failed loaded units
```

Replace `nginx` with the service under investigation. A service can be `active` while still returning errors, so status is only one layer of evidence.

Before restarting a service, read its logs and validate its configuration when the application provides a validation command. For Nginx:

```bash
sudo nginx -t                # Validate Nginx configuration without reloading it
```

### 6. Read logs around the failure

```bash
journalctl -u nginx -b --no-pager -n 50   # Recent Nginx logs from this boot
journalctl -p warning..alert -b            # System warnings and worse from this boot
journalctl --since "15 minutes ago"        # Events within a useful time window
```

Use the service name, boot, severity, and time filters to reduce noise. Look for the first meaningful error, not only the final repeated message.

Some application logs live under `/var/log` instead of—or in addition to—the systemd journal:

```bash
sudo tail -n 50 /var/log/nginx/error.log
```

### 7. Inspect the network path

```bash
ip -brief address            # Are interfaces up, and do they have addresses?
ip route                     # Is there a route to the destination?
ping -c 4 1.1.1.1            # Can packets reach a known IP? ICMP may be blocked
getent hosts example.com     # Can the configured resolver resolve a name?
ss -lntup                    # Which TCP/UDP ports are listening, and by which processes?
```

Each command checks a different layer:

```text
Interface → IP address → Route → Destination → DNS → Listening service
```

`ping` failing does not always prove the host is down because firewalls may block ICMP. Test the actual application protocol as well.

### 8. Verify the service as a user would

```bash
curl -I http://localhost             # Test the local HTTP response headers
curl -sS -o /dev/null -w '%{http_code}\n' http://localhost
```

The first command shows the HTTP headers. The second prints the status code while suppressing the response body.

Testing `localhost` separates the local application from external DNS, load-balancer, firewall, and routing issues. After the local test succeeds, test the real hostname from outside the server.

### 9. Check recent kernel warnings

```bash
dmesg --level=err,warn | tail -n 30
```

Kernel messages may reveal disk, filesystem, driver, memory, or network-interface problems. Access may require `sudo` on secured systems.

### 10. Use optional specialised tools

```bash
iostat -xz 1 3              # Disk-device latency and utilisation; usually from sysstat
nvidia-smi                  # NVIDIA GPU status, utilisation, memory, and processes
```

These tools may not be installed or applicable. Follow the organisation's approved package process rather than installing diagnostic software during an incident without permission.

---

## 🧪 Hands-on Lab

### Diagnose a local web service

Use a disposable Linux VM. If Nginx is not installed, substitute another service that exists on the VM.

1. Record the server identity and current time:

   ```bash
   hostname
   date
   ```

2. Establish a resource baseline:

   ```bash
   uptime
   free -h
   df -h
   ```

3. Inspect the service and its recent logs:

   ```bash
   systemctl status nginx --no-pager
   journalctl -u nginx -b --no-pager -n 30
   ```

4. Confirm whether the expected port is listening:

   ```bash
   ss -lntup
   ```

5. Test the service locally:

   ```bash
   curl -I http://localhost
   ```

6. Write a short incident note containing:

   - the exact symptom;
   - the time observed;
   - commands used;
   - evidence found;
   - the likely root cause;
   - the smallest safe fix; and
   - how recovery would be verified.

Do not deliberately fill a filesystem, exhaust memory, or stop a service on a shared or production machine.

### Think Like an Engineer

The server reports only 40% CPU use and plenty of free memory, but users still receive errors.

What would you check next?

Consider the service state, logs, listening port, disk space, DNS, downstream dependencies, and the user-facing request. Healthy CPU and RAM do not prove that the application is healthy.

---

## 🎯 Interview Questions

1. What does server health mean?
2. What is the difference between a symptom and a root cause?
3. Why should you confirm the hostname and time before troubleshooting?
4. What do the three load averages shown by `uptime` represent?
5. Why is low “free” memory not always a problem on Linux?
6. What is the difference between `df` and `du`?
7. How can a filesystem run out of space even when `df -h` reports free capacity?
8. What is the difference between `systemctl status` and `journalctl -u`?
9. How would you confirm that a service is listening on its expected port?
10. Why does a failed `ping` not always mean the destination is unavailable?
11. Why should logs be checked before restarting a service?
12. Why is a successful `systemctl` result not enough to prove recovery?
13. What should an incident record contain?
14. How would cloud health checks complement Linux commands?
15. Which additional signals matter on an AI inference server?

---

## 📌 Troubleshooting Quick Reference

| Symptom | Probable Causes | Verify With | Safe Direction |
| --- | --- | --- | --- |
| Server is slow | CPU queue, memory pressure, disk I/O, or dependency delay | `uptime`, `top`, `free -h`, `vmstat`, `iostat` | Find the constrained resource and responsible workload |
| Files cannot be created | Full filesystem or exhausted inodes | `df -h`, `df -i`, scoped `du` | Identify growth; archive or remove only approved data |
| Service is unavailable | Failed unit, invalid configuration, missing dependency, or port conflict | `systemctl status`, `journalctl`, `ss`, config test | Correct the evidence-backed fault, then restart or reload if required |
| Hostname does not resolve | DNS record or resolver problem | `getent hosts`, resolver configuration | Correct the appropriate DNS or resolver configuration |
| Remote connection fails | Route, firewall, service, port, or authentication problem | `ip route`, `ss`, service logs, application test | Identify which network or application layer fails |
| High application errors | Bug, overload, bad deployment, or failed dependency | Application logs, metrics, traces, dependency checks | Roll back, reduce load, or repair the confirmed cause |
| AI inference is slow | Queueing, GPU memory pressure, model loading, CPU or storage bottleneck | Service metrics, `nvidia-smi`, `top`, `iostat`, logs | Correct the constrained layer and re-test inference |

---

## 📌 Key Takeaways

- A powered-on server is not necessarily a healthy server.
- Start with the symptom and timeline, then collect evidence before making changes.
- CPU, memory, disk, network, services, and logs are connected parts of one system.
- `top`, `free`, `df`, `systemctl`, `journalctl`, `ip`, `ss`, and `curl` answer different diagnostic questions.
- A metric needs context: compare it with CPU count, workload behaviour, and a known healthy baseline.
- Restarting a service may restore it temporarily without fixing its root cause.
- Verify recovery through the same path the user relies on.
- Monitoring, alerts, capacity planning, and incident reviews help prevent repeated failures.

---

## 🪨 Caveman Summary

```text
Workers overloaded?        → Check CPU, load, and processes
Working tables crowded?    → Check RAM, swap, and memory pressure
Storage caves full?        → Check filesystems, inodes, and directories
Roads blocked?             → Check interfaces, routes, DNS, and reachability
Village gate closed?       → Check listening ports
Workshop stopped?          → Check the service and its configuration
What happened earlier?     → Read logs around the incident time
Did the repair work?       → Test the service as the user does
Could it happen again?     → Add monitoring, alerts, and prevention
```

> **A good Chief does not guess. A good Linux engineer follows evidence from symptom to root cause, restores the service safely, and verifies that the village is healthy again.**
