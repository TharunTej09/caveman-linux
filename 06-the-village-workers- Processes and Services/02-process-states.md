# 02 — Process States

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain why a process changes state during its lifetime.
- Recognise running, sleeping, uninterruptible, stopped, zombie, and idle states.
- Understand how the scheduler shares limited CPU time.
- Observe live activity and parent-child relationships.

## 🏕️ Caveman Story

Five cooks need one stove. One cook uses it, others wait for a turn, and another sleeps until fresh food arrives. A paused worker keeps the job but does nothing until the Chief allows it to continue.

Not every worker who is waiting is lazy or broken. Waiting prevents villagers from wasting effort while they have nothing useful to do.

## 🖼️ Big Concept Illustration

![Village workers demonstrating different process states around a shared stove](../images/06-the-village-workers/process-states-hero.png)

```text
Created → Ready/Running → Sleeping or Waiting → Ready/Running → Exit
                         ↘ Stopped              ↗
```

```text
Many runnable workers → Linux scheduler → Limited CPU cores
```

## 📖 Concept Explained Simply

The Linux scheduler decides which runnable process receives CPU time. Processes frequently move between states:

| State | Typical code | Meaning |
| --- | --- | --- |
| Running / runnable | `R` | Executing now or ready for CPU |
| Interruptible sleep | `S` | Waiting for an event; can respond to signals |
| Uninterruptible sleep | `D` | Usually waiting for kernel I/O; not immediately interruptible |
| Stopped / traced | `T` or `t` | Paused by job control, a signal, or a debugger |
| Zombie | `Z` | Exited, but its parent has not collected its exit status |
| Idle kernel thread | `I` | Idle kernel worker on supported kernels |

A healthy server normally has many sleeping processes. They wake when input, a timer, or another event arrives.

A zombie is not still performing work and usually consumes almost no runtime resources, but many persistent zombies indicate that a parent process is failing to reap children.

## 🌍 Real Linux Example

A web worker spends much of its life sleeping while waiting for a request. It becomes runnable when traffic arrives, may wait on disk or network I/O, uses the CPU briefly, sends a response, and sleeps again.

High CPU is not proven by a large process count. State, CPU consumption, run queue, and I/O wait must be considered together.

## 🛠️ Commands Introduced

### `top` — Watch Processes Live

```bash
top
```

Displays a continuously updating view of system activity. Useful interactive keys include:

- `P`: sort by CPU use.
- `M`: sort by memory use.
- `1`: show individual CPU cores.
- `c`: toggle full command lines.
- `q`: quit.

The `S` column shows process state. Treat the values as evidence, not a diagnosis by themselves.

### `htop` — Use an Interactive Process Viewer

```bash
htop
```

Provides a more visual interface with meters, scrolling, search, sorting, and a tree view. It may not be installed on minimal servers.

### `pstree` — Display Process Families

```bash
pstree
pstree -p
```

Shows parent-child relationships as a tree. `-p` includes PIDs.

```bash
pstree -p "$USER"
```

Shows process trees rooted in processes belonging to the named user, depending on the implementation.

## 💡 Caveman Tip

Sleeping usually means efficient waiting. Investigate a state when it is unexpected, persistent, and connected to a symptom—not simply because its letter looks unfamiliar.

## ⚠️ Common Mistakes

- Assuming `R` means a process has been running continuously.
- Treating every `S` process as stuck.
- Believing a zombie is an active process consuming CPU.
- Trying to fix a zombie by targeting the already-exited child instead of investigating its parent.
- Using live viewers without noting that values change between refreshes.

## 🧪 Hands-on Lab

### Mission: Watch the Workers Change

1. Open the live process viewer.
2. Sort by CPU, then by memory.
3. Identify at least one `R` or `S` process.
4. Toggle per-core CPU activity and the full command line.
5. If installed, compare the same view in `htop`.
6. Display your process family with PIDs.
7. Explain why your terminal and shell have a parent-child relationship.

## 📝 Quick Recap

- Processes change state as they run, wait, pause, and exit.
- The scheduler shares CPU cores between runnable processes.
- Sleeping is normal; uninterruptible waits and zombies require context.
- `top`, `htop`, and `pstree` reveal live activity and process families.

## 🧠 Interview Questions

1. What is the difference between running and runnable?
2. Why are many server processes sleeping?
3. What usually causes state `D`?
4. What is a zombie, and which process should reap it?
5. How does `pstree` help during troubleshooting?

## 📚 What's Next

The Chief can see each worker's state. Next, learn how Linux asks a process to stop, pause, continue, or reload in [03 — Signals](03-signals.md).
