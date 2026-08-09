# Lab 04 — Troubleshoot a Busy Worker

## 🎯 Mission

Create a controlled CPU-heavy process, identify it from evidence, communicate with it safely, and confirm recovery.

## Prerequisites

- A disposable Linux VM
- `procps` tools (normally installed by default)

## ⚠️ Safety

The workload is intentionally wasteful. Run only one instance and record its PID so you do not signal the wrong process.

## Starting State

Record an idle baseline:

```bash
uptime
free -h
```

## Tasks

1. Start a named background workload:

   ```bash
   bash -c 'exec -a cave-spinner yes > /dev/null' &
   echo $!
   ```

   Save the printed PID.
2. Find and inspect it:

   ```bash
   pgrep -a cave-spinner
   ps -o pid,ppid,stat,%cpu,%mem,etime,cmd -p PID
   top -p PID
   ```

   Replace `PID` with the saved number. Press `q` to exit `top`.
3. Ask the worker to pause, inspect its state, then continue:

   ```bash
   kill -STOP PID
   ps -o pid,stat,cmd -p PID
   kill -CONT PID
   ```

4. Request graceful termination:

   ```bash
   kill -TERM PID
   ```

5. Verify that the process is gone and compare the load again:

   ```bash
   ps -p PID
   uptime
   ```

## ✅ Verification

- The workload appears with high CPU usage.
- Its state includes `T` after `SIGSTOP`.
- It resumes after `SIGCONT`.
- `ps -p PID` no longer shows it after `SIGTERM`.

## Troubleshooting Clues

- **No process found:** it may already have exited; start the workload again and save the new PID.
- **Wrong process in `top`:** confirm the PID using `pgrep -a` before sending signals.
- **Process survives `SIGTERM`:** recheck identity and state before considering `SIGKILL`; escalation should be evidence-based.

## Cleanup

Run `pgrep -a cave-spinner`. If the lab process remains, send `SIGTERM` to its exact PID. Do not use broad patterns on a shared system.

## 🧠 Think Like an Engineer

In production, what evidence would you capture before stopping a busy process, and how would you tell whether it is the cause or merely a symptom?
