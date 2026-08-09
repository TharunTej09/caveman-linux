# 03 — Signals

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain signals as asynchronous notifications to processes.
- Distinguish graceful termination from forced termination.
- Pause, resume, or select processes safely.
- Keep an appropriate command running after logout.

## 🏕️ Caveman Story

Chief Grog does not wrestle every worker away from a task. He sends a clear message:

- “Finish safely and go home.”
- “Pause where you are.”
- “Continue working.”
- “Emergency—stop immediately.”

A trained worker can clean the tools before leaving. In a true emergency, the guard removes the worker instantly—but unfinished work may be left behind.

## 🖼️ Big Concept Illustration

![Chief Grog sending different signals to village workers](../images/06-the-village-workers/signals-hero.png)

```text
Chief → Message → Worker → Defined action
Linux → Signal  → Process → Handle, ignore, stop, continue, or exit
```

```text
SIGTERM → graceful opportunity → cleanup → exit
SIGKILL → kernel stops process immediately → no cleanup handler
```

## 📖 Concept Explained Simply

A **signal** is a notification delivered to a process. Signals are identified by names and numbers.

| Signal | Number | Normal purpose |
| --- | ---: | --- |
| `SIGHUP` | 1 | Terminal hangup; many daemons interpret it as reload |
| `SIGINT` | 2 | Interactive interrupt, commonly from `Ctrl+C` |
| `SIGKILL` | 9 | Immediate kernel-enforced termination |
| `SIGTERM` | 15 | Polite request to terminate; the default for `kill` |
| `SIGCONT` | 18 | Continue a stopped process on Linux |
| `SIGSTOP` | 19 | Stop a process; cannot be handled or ignored |

Signal numbers can differ on some Unix-like systems, so names communicate intent better. `SIGKILL` and `SIGSTOP` cannot be caught, blocked, or ignored.

## 🌍 Real Linux Example

During a deployment, an application should normally receive `SIGTERM`. It can stop accepting work, finish or reject in-flight requests, close files, and exit. Orchestrators such as Kubernetes use this graceful period before eventually forcing termination if the process does not exit.

## 🛠️ Commands Introduced

### `kill` — Signal One PID

```bash
kill PID
kill -TERM PID
```

Sends `SIGTERM` by default. Use `-TERM` when you want the intent to be explicit.

```bash
kill -STOP PID
kill -CONT PID
```

Pauses and resumes a process.

```bash
kill -KILL PID
```

Forces immediate termination. Use it only after graceful termination fails and you understand the impact.

### `pkill` — Signal Processes by Matching Criteria

```bash
pkill -TERM -x firefox
```

Signals processes matching an exact name. Without `-x`, broader pattern matching can select more processes than intended.

```bash
pkill -TERM -u "$USER" -x process_name
```

Limits matches to the current user.

### `killall` — Signal All Processes with a Name

```bash
killall -TERM process_name
```

Signals processes bearing that name. Behaviour varies across Unix families, so verify the local manual before using it outside Linux.

### `nohup` — Survive Terminal Hangup

```bash
nohup script.sh >script.log 2>&1 &
```

Runs the command ignoring `SIGHUP`; `&` places it in the shell's background, and redirection stores output. This does not make the command a managed production service.

## 💡 Caveman Tip

First identify the exact process, then send the least destructive signal that can solve the problem. `SIGKILL` is an emergency axe, not a normal door handle.

## ⚠️ Common Mistakes

- Assuming `kill` always means `SIGKILL`; its default is `SIGTERM`.
- Signalling by a broad name without previewing possible matches.
- Force-killing a database or stateful process without checking recovery impact.
- Expecting a process to clean up after `SIGKILL`.
- Treating `nohup` as a substitute for `systemd` supervision.

## 🧪 Hands-on Lab

### Mission: Direct a Safe Test Worker

Use a disposable test process that belongs to you; `sleep 300` is only a harmless lab helper.

1. Start it in the background with `nohup sleep 300 >sleep.log 2>&1 &`.
2. Record the PID printed by the shell.
3. Pause it with `SIGSTOP`.
4. Resume it with `SIGCONT`.
5. Request graceful termination with `SIGTERM`.
6. Verify that it exits.
7. Repeat only in the disposable lab and use `SIGKILL` to observe the difference.

Never practise on SSH, a database, or an unknown production process.

## 📝 Quick Recap

- Signals are messages sent to processes.
- `SIGTERM` allows graceful handling; `SIGKILL` does not.
- `SIGSTOP` pauses and `SIGCONT` resumes.
- Name-based signalling is powerful and requires careful matching.
- `nohup` handles terminal hangup but does not supervise a service.

## 🧠 Interview Questions

1. What happens when `kill PID` is used without a signal option?
2. Why should `SIGTERM` normally precede `SIGKILL`?
3. Which signals cannot be caught or ignored?
4. What risk comes with `pkill` and `killall`?
5. Why is `nohup` not a service manager?

## 📚 What's Next

Some workers must start at boot and remain available. Meet their supervisor in [04 — Services and systemd](04-services-and-systemd.md).
