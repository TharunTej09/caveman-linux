# 06 — The Village Workers: Processes and Services

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Explain the difference between a program, process, and service.
- Inspect processes, PIDs, owners, and parent-child relationships.
- Recognise common process states and understand CPU scheduling.
- Control processes with signals safely.
- Manage long-running services with `systemd`.
- Interpret CPU, memory, swap, load, and I/O indicators.

## 🏕️ Caveman Story

Chief Grog has organised the caves, tools, and treasure—but a village is useless without workers.

Food does not cook itself. Wood does not cut itself. Fires do not remain lit by themselves. Some villagers finish one task and leave; others guard the gate through the night.

Linux works the same way:

```text
Villager doing a job       → Process
Worker who stays on duty   → Service
Chief assigning turns      → Linux scheduler
Chief's instructions       → Signals
Village supervisor         → systemd
```

## 🖼️ Big Concept Illustration

![Chief Grog overseeing the village workers](../images/06-the-village-workers/village-workers-hero.png)

```text
Program → Run → Process → Manage → Service → Monitor → Healthy server
```

```text
Linux system
├── Short-lived processes      finish after a task
├── Interactive processes      work with a user
├── Background processes       work without the foreground
└── Services                   provide long-running capabilities
```

## 📖 Concept Explained Simply

A **program** is stored instructions. A **process** is a running instance of those instructions. Linux may run hundreds or thousands of processes while sharing CPU time, memory, files, and devices between them.

A **service** is a process—or coordinated group of processes—designed to provide a capability over time. SSH accepts remote logins, a web server answers requests, and a database stores and retrieves data.

Linux must continually answer:

```text
Who should run now?
Who must wait?
How much memory is available?
Did a worker stop?
Should it be restarted?
Is the village overloaded?
```

## 🌍 Real Linux Example

When a web request reaches a production server, a web-service process accepts it, application processes perform work, a database service retrieves data, and the kernel schedules them all on limited CPU and memory.

Containers and Kubernetes do not replace this model. A container still runs Linux processes, and a Kubernetes workload is healthy only when those processes and their dependencies are healthy.

## 🛠️ Commands Introduced

| Lesson | Village question | New commands |
| --- | --- | --- |
| [01 — Processes](01-processes.md) | Who is working? | `ps`, `pgrep`, `pidof` |
| [02 — Process States](02-process-states.md) | What is each worker doing? | `top`, `htop`, `pstree` |
| [03 — Signals](03-signals.md) | How does the Chief communicate? | `kill`, `killall`, `pkill`, `nohup` |
| [04 — Services and systemd](04-services-and-systemd.md) | Who keeps working? | `systemctl`, `journalctl` |
| [05 — CPU, Memory and Load](05-cpu-memory-and-load.md) | Is the village healthy? | `free`, `uptime`, `vmstat`, `iostat`, `sar`, `nice`, `renice` |

Each command has one teaching home. Later lessons may combine it in a mission, but do not explain it again.

## 💡 Caveman Tip

Troubleshoot from observation to action: identify the worker, understand its state and owner, inspect its service or logs, and only then change or stop it.

## ⚠️ Common Mistakes

- Confusing a program file with a running process.
- Assuming sleeping processes are unhealthy.
- Using `SIGKILL` before allowing graceful shutdown.
- Restarting SSH carelessly while connected remotely.
- Treating load average as CPU percentage.
- Blaming low “free” memory when Linux is using RAM efficiently for cache.

## 🧪 Hands-on Lab

### Final Mission: Save the Village

On a disposable Linux VM:

1. Find the busiest worker and record its PID.
2. Discover its parent and current state.
3. Gracefully stop a safe test process; force-stop only if it refuses.
4. Verify that the SSH service is healthy without interrupting your access.
5. Read recent service logs.
6. Check CPU, memory, load, and I/O wait.
7. Run one background task at a lower priority.
8. Write a short diagnosis supported by command output.

The individual lessons prepare every step; the final mission combines them into a production troubleshooting workflow.

## 📝 Quick Recap

```text
Stored instructions
        ↓
     Program
        ↓ run
     Process
        ↓ managed by
Kernel scheduler + signals + systemd
        ↓ observed through
CPU + memory + load + I/O
```

## 🧠 Interview Questions

1. What is the difference between a program, process, and service?
2. What do PID and PPID identify?
3. Why can a sleeping process be healthy?
4. Why should `SIGTERM` normally come before `SIGKILL`?
5. What is the difference between starting and enabling a service?
6. What can cause high load besides CPU work?

## 📚 What's Next

Begin with [01 — Processes](01-processes.md) and meet the workers who make Linux feel alive.

## 🧭 Chapter Navigation

[← Protecting the Treasure](../05-protecting-the-treasure%20-%20UserPermissions/README.md) · [Course Home](../README.md) · [Next: Talking Between Villages →](../07-talking-between-villages%20-%20Networking/README.md)
