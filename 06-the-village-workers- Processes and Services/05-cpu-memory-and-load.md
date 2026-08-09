# 05 — CPU, Memory and Load

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Distinguish CPU use, memory pressure, swap, load average, and I/O wait.
- Read a quick system-health snapshot.
- Collect short live and historical performance samples.
- Start or adjust a process with an appropriate scheduling priority.

## 🏕️ Caveman Story

The village has many workers but only a few cooking fires, worktables, and supply carts.

When too many workers need the same fire, a queue forms. When the tables fill, supplies move to a slower storage cave. When carts are delayed on muddy roads, workers wait even though the cooking fire is not fully busy.

Chief Grog must measure the right shortage before adding more resources.

## 🖼️ Big Concept Illustration

![Chief Grog checking workload and resource pressure across the village](../images/06-the-village-workers/cpu-memory-and-load-hero.png)

```text
CPU cores      → shared cooking fires
RAM            → fast working tables
Swap           → slower overflow cave
I/O            → supply carts and roads
Load average   → workers running or waiting for required resources
```

```text
Processes
   ├── need CPU
   ├── allocate memory
   └── wait for I/O
            ↓
      System health
```

## 📖 Concept Explained Simply

These measurements answer different questions:

- **CPU usage:** How much processor time is busy, idle, or waiting on I/O?
- **Memory:** How much RAM is used, available, cached, or under pressure?
- **Swap:** Is disk-backed overflow being used? Activity matters more than usage alone.
- **Load average:** Average number of tasks runnable or in uninterruptible wait over 1, 5, and 15 minutes on Linux.
- **I/O wait:** Time CPUs were idle while tasks waited for I/O; high values can indicate a storage bottleneck but need supporting evidence.
- **Niceness:** A user-space hint that influences CPU scheduling priority. Higher nice values mean a process is more willing to yield CPU.

Compare load with the number of logical CPUs. A load of `4` means something very different on a 2-CPU system and a 32-CPU system.

## 🌍 Real Linux Example

Suppose an API is slow. High load plus high user CPU suggests compute pressure. High load plus high I/O wait and storage latency suggests a disk bottleneck. Frequent swap-in and swap-out suggests memory pressure. Each case needs a different fix.

Cloud monitoring dashboards expose the same ideas at scale, but command-line evidence is invaluable when an alert leads you onto a server.

## 🛠️ Commands Introduced

### `free` — Summarise Memory

```bash
free -h
```

`-h` uses human-readable units. Focus on **available** memory rather than the **free** column alone because Linux uses spare RAM for reclaimable cache.

### `uptime` — Show Runtime and Load Averages

```bash
uptime
```

Shows time, uptime, logged-in user count, and 1-, 5-, and 15-minute load averages.

### `vmstat` — Sample CPU, Memory, Paging, and Scheduling

```bash
vmstat 1 5
```

Prints five samples one second apart. Important fields include runnable tasks (`r`), blocked tasks (`b`), swap-in/out (`si`, `so`), I/O wait (`wa`), and idle CPU (`id`). The first line is typically an average since boot; later lines describe each interval.

### `iostat` — Inspect CPU and Device I/O

```bash
iostat -xz 1 5
```

`-x` adds extended device statistics, `-z` hides inactive devices, and the final values request one-second samples. Availability and field names depend on the `sysstat` package and version.

### `sar` — Review Collected Performance History

```bash
sar -u 1 5
sar -r
```

`-u` reports CPU activity; `-r` reports memory activity. Historical data is available only when sysstat collection is installed and enabled.

### `nice` — Start with Adjusted Niceness

```bash
nice -n 10 sleep 60 &
```

Starts a harmless lab process with niceness `10`, giving it lower CPU preference than the default `0`. Ordinary users can usually increase niceness; raising priority requires privilege.

### `renice` — Adjust a Running Process

```bash
renice -n 15 -p PID
```

Changes niceness for an existing PID. The range is normally `-20` (higher scheduling priority) to `19` (lower scheduling priority).

## 💡 Caveman Tip

One metric rarely proves a bottleneck. Correlate symptoms with CPU, runnable tasks, memory availability, swap activity, and device I/O over the same time window.

## ⚠️ Common Mistakes

- Treating load average as a percentage.
- Calling cached RAM “wasted” or assuming low free memory is automatically bad.
- Assuming any swap usage means immediate failure.
- Diagnosing from the first `vmstat` or `iostat` line without noticing the since-boot average.
- Lowering the numeric nice value without understanding that this raises CPU priority.
- Installing monitoring tools during an incident without considering repository or change-control rules.

## 🧪 Hands-on Lab

### Mission: Diagnose the Slow Village

1. Record available memory and swap use.
2. Record the 1-, 5-, and 15-minute load averages.
3. Collect five short `vmstat` samples.
4. If available, collect extended device statistics and note I/O wait or busy devices.
5. If historical collection is enabled, inspect CPU and memory reports.
6. Start the harmless `sleep` example at niceness `10`.
7. Change it to niceness `15` using its PID.
8. Write whether the snapshot suggests CPU, memory, or I/O pressure—and cite at least two measurements.

## 📝 Quick Recap

- CPU, memory, swap, load, and I/O describe different constraints.
- Load represents demand, not CPU percentage.
- Available memory is more useful than free memory alone.
- Interval samples reveal more than a single snapshot.
- Niceness influences CPU scheduling preference; it does not guarantee CPU time.

## 🧠 Interview Questions

1. What do the three load-average values represent?
2. Why should load be compared with CPU count?
3. What is the difference between free and available memory?
4. What do `si`, `so`, and `wa` help reveal?
5. Does a higher nice value mean higher or lower CPU priority?
6. Why might high load coexist with modest CPU usage?

## 📚 What's Next

You can now identify, control, supervise, and measure Linux workers. Continue to [07 — Talking Between Villages](<../07-talking-between-villages - Networking/README.md>) to learn how those workers communicate across networks.
