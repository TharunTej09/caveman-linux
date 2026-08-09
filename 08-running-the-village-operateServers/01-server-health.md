# 01 — Server Health

> “A single empty basket does not describe the whole village.” — Chief Grog

## 🎯 Learning Objectives

- Define server health in terms of user-facing service and resource pressure.
- Interpret CPU, memory, disk I/O, load, and process activity together.
- Compare current behaviour with a useful baseline.
- Distinguish utilisation, saturation, and errors.
- Collect a short production-safe health snapshot.

## 🏕️ Caveman Story

Each morning, Chief Grog checks the village.

He does not count only the workers. He checks whether workers are waiting, whether the working tables are crowded, whether storage carts are delayed, and whether villagers are receiving food on time.

A busy village can be healthy. A quiet village can still be broken. Health means the village is completing its work reliably.

## 🖼️ Big Concept Illustration

![Chief Grog checking workers, tables, storage carts, and village health signals](../images/08-running-the-village/server-health-hero.png)

```text
User experience
      ↑
Application and dependencies
      ↑
Processes and queues
      ↑
CPU ─ RAM ─ Disk I/O ─ Network
```

| Caveman signal | Linux signal |
| --- | --- |
| Workers are busy | CPU utilisation |
| Workers wait in line | Run queue or I/O wait |
| Working tables are full | Memory pressure |
| Storage carts move slowly | Disk latency and utilisation |
| Work finishes late | Application latency |

## 📖 Concept Explained Simply

A healthy server delivers its intended service within acceptable limits. Start with the service, then inspect the resources supporting it.

- **Utilisation** asks how busy a resource is.
- **Saturation** asks whether work is waiting for that resource.
- **Errors** reveal failed operations.
- **Latency** measures how long work takes.
- **Throughput** measures how much work completes.

Load average is not a CPU percentage. On Linux it represents runnable tasks plus tasks in uninterruptible sleep, commonly waiting on I/O. Interpret it with CPU count, workload, and supporting evidence.

Memory marked “used” is not automatically a problem because Linux uses spare RAM for cache. Look for sustained pressure, swapping, reclaim activity, allocation failures, and application impact.

### Why Should I Care?

Production incidents are often chains: a slow disk delays requests, queues grow, memory rises, and CPU later becomes busy. Reading only the final number can produce the wrong fix.

## 🌍 Real Linux Example

An API has high latency. CPU utilisation is moderate, but `vmstat` shows high I/O wait and blocked tasks while `iostat` shows one volume with sustained latency. The evidence points toward storage pressure rather than insufficient CPU.

On cloud VMs, also compare guest signals with provider metrics such as disk burst credits, throttling, instance limits, and host maintenance. On AI servers, add GPU utilisation, memory, temperature, and data-loading throughput—but first prove whether the GPU is actually the bottleneck.

## 🛠️ Commands Introduced

Use earlier commands such as `uptime`, `free -h`, `df -h`, `top`, and `ss` only as supporting checks. This lesson introduces time-based performance tools, commonly provided by the `procps` and `sysstat` packages.

### `vmstat` — Observe System-Wide Pressure

```bash
vmstat 1 5
vmstat -w 1 5
```

The first line is an average since boot; later lines describe each interval. Useful fields include runnable tasks (`r`), blocked tasks (`b`), swap in/out (`si`/`so`), I/O wait (`wa`), and CPU idle (`id`). `-w` uses wider output.

### `mpstat` — Compare CPU Activity

```bash
mpstat 1 5
mpstat -P ALL 1 5
```

The first form reports aggregate CPU activity. `-P ALL` reveals imbalance across logical CPUs. High `%iowait` is a clue that needs storage evidence; it is not proof of a failed disk.

### `iostat` — Inspect Device I/O

```bash
iostat -xz 1 5
```

`-x` shows extended device statistics, `-z` hides inactive devices, and the interval/count produce a short sample. Interpret latency, queueing, throughput, and utilisation together; names and fields differ across versions and device types.

### `pidstat` — Attribute Activity to Processes

```bash
pidstat 1 5
pidstat -r -d 1 5
```

The first view samples per-process CPU. `-r` adds memory and page-fault data; `-d` adds I/O. Sampling is more useful than a single instant.

### `sar` — Review Historical Activity

```bash
sar -u 1 5
sar -r
sar -d
```

`-u` shows CPU, `-r` memory, and `-d` device activity. Historical data exists only if collection is installed and enabled. Match the time window and timezone to the incident.

## 💡 Caveman Tip

Use the USE method for each resource: check **Utilisation, Saturation, and Errors**. Then connect the result back to service latency and failures.

## ⚠️ Common Mistakes

- Treating high CPU utilisation as unhealthy when useful work completes normally.
- Treating Linux cache as wasted or unavailable memory.
- Comparing load average directly across servers with different CPU counts.
- Reading the first `vmstat` or `iostat` line as the current interval.
- Collecting a one-second snapshot and declaring a root cause.
- Running heavy benchmarks during an active incident without approval.

## 🧪 Hands-on Lab

### Mission: Establish the Village Baseline

1. Record the VM’s CPU count and intended workload using commands from earlier lessons.
2. Capture five-second samples with `vmstat`, `mpstat`, `iostat`, and `pidstat` while idle.
3. Run a small, controlled CPU or file-copy workload in a disposable environment.
4. Capture the same samples again.
5. Identify what changed in utilisation, saturation, latency, and process ownership.
6. Write a baseline with timestamp, workload, expected range, and evidence.

## 📝 Quick Recap

```text
Start with service health
        ↓
Check utilisation + saturation + errors
        ↓
Correlate CPU + memory + disk + processes
        ↓
Compare with baseline and user impact
```

## 🧠 Interview Questions

1. Why is high CPU utilisation not always a problem?
2. What does Linux load average represent?
3. How would you distinguish memory usage from memory pressure?
4. Why can disk pressure appear as an application latency problem?
5. What is the value of a performance baseline?

## 📚 What's Next

Health signals tell us that something changed. [02 — Logs and Monitoring](02-logs-and-monitoring.md) helps us discover what happened and when.
