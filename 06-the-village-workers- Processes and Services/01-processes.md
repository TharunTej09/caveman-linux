# 01 — Processes

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Distinguish a stored program from a running process.
- Explain PID, PPID, user, terminal, CPU time, and command fields.
- Display processes in several useful views.
- Find a process by its name.

## 🏕️ Caveman Story

A recipe carved on stone cannot feed the village by itself. It becomes useful only when a cook reads it and begins cooking.

The stone recipe is a **program**. The cook actively following it is a **process**. Two cooks can follow the same recipe at the same time, just as Linux can create multiple processes from one program.

Chief Grog gives each active worker a unique token so he can identify and manage that worker precisely.

## 🖼️ Big Concept Illustration

![A stored recipe becoming active work in Chief Grog's village](../images/06-the-village-workers/processes-hero.png)

```text
Stone recipe → Cook starts → Ingredients and stove → Cooking
   program         run          memory + CPU         process
```

```text
One program
    ├── Process 2410
    ├── Process 2418
    └── Process 2431
```

## 📖 Concept Explained Simply

A **program** is executable code stored on disk. A **process** is one running instance with its own identity and resources.

Important process details include:

| Field | Meaning | Caveman idea |
| --- | --- | --- |
| PID | Unique process ID | Worker's token |
| PPID | Parent process ID | Worker who started it |
| USER / UID | Account running it | Villager identity |
| TTY | Controlling terminal, if any | Village office window |
| TIME | CPU time consumed | Time using the shared stove |
| CMD / COMMAND | Program and arguments | Job being performed |

Processes form families. A shell may start a command as its child; that command may create children of its own.

## 🌍 Real Linux Example

An Nginx server commonly has one master process and multiple worker processes. The master coordinates configuration and lifecycle; workers handle connections. If one worker becomes unhealthy, its PID identifies the exact running instance—not merely the Nginx program installed on disk.

## 🛠️ Commands Introduced

### `ps` — Take a Process Snapshot

```bash
ps
```

Shows processes associated with the current terminal.

```bash
ps -ef
```

Uses UNIX-style options to show every process in a full listing, including UID, PID, PPID, start time, and command.

```bash
ps aux
```

Uses BSD-style options: `a` includes other users' terminal processes, `u` adds a user-oriented view and resource fields, and `x` includes processes without a controlling terminal.

> `ps -ef` and `ps aux` overlap, but their columns and option traditions differ. Choose the view that answers your question.

### `pgrep` — Find Matching PIDs

```bash
pgrep sshd
pgrep -a sshd
```

Finds processes by name. `-a` also prints the full command line, making matches easier to verify.

```bash
pgrep -u "$USER" -a bash
```

`-u` limits matches to one user.

### `pidof` — Find PIDs for an Exact Program

```bash
pidof sshd
```

Prints PIDs for a running program name. It is convenient for exact daemon names, while `pgrep` provides richer matching and filtering.

## 💡 Caveman Tip

Never act on a PID until you confirm its user and command. PIDs are reused after processes exit, so an old PID can later identify a different worker.

## ⚠️ Common Mistakes

- Calling an installed program a process before it is running.
- Assuming one program always creates only one process.
- Confusing PID with PPID.
- Reading `TIME` as wall-clock runtime; it is accumulated CPU time.
- Copying a PID from old output without verifying it again.

## 🧪 Hands-on Lab

### Mission: Count the Village Workers

1. Use the basic process snapshot and identify your shell.
2. Compare the columns in the two full process views.
3. Find the PID and full command line for your shell.
4. Search for `sshd` or another known service process.
5. Record one process's PID, PPID, user, TTY, CPU time, and command.
6. Explain which process likely started it.

## 📝 Quick Recap

- A program contains instructions; a process is those instructions running.
- Every process has a PID and normally a parent identified by PPID.
- Processes run as users and consume resources.
- `ps`, `pgrep`, and `pidof` answer different process-discovery questions.

## 🧠 Interview Questions

1. What is the difference between a program and a process?
2. Can one program have multiple PIDs? Why?
3. What is a PPID?
4. Why might a process have `?` in its TTY column?
5. When would you prefer `pgrep -a` over `pidof`?

## 📚 What's Next

You can identify the workers. Next, learn whether they are running, waiting, sleeping, stopped, or finished in [02 — Process States](02-process-states.md).
