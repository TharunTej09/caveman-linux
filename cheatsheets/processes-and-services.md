# Processes and Services Cheatsheet

## Processes

```bash
ps -ef                              # snapshot of all processes
ps -o pid,ppid,stat,%cpu,%mem,cmd -p PID
pgrep -a NAME                       # find PID and command
top                                 # interactive activity view
pstree -p                           # parent-child relationships
kill -TERM PID                      # request graceful termination
kill -KILL PID                      # last resort; no cleanup
```

Common states: `R` running/runnable, `S` sleeping, `D` uninterruptible sleep, `T` stopped, `Z` zombie.

## systemd Services

```bash
systemctl status SERVICE
systemctl is-active SERVICE
sudo systemctl restart SERVICE
sudo systemctl enable --now SERVICE
journalctl -u SERVICE --since "30 minutes ago"
journalctl -u SERVICE -f
systemctl list-units --failed
```

Before restarting a failed service: capture status, recent logs, configuration validation, resource state, and the time the issue began.

## Load and Memory

```bash
uptime          # load averages
free -h         # memory and swap
vmstat 1        # CPU, run queue, memory, and I/O trends
```

A high number is evidence, not a diagnosis. Compare it with the normal baseline and user impact.
