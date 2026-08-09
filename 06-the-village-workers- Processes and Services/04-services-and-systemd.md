# 04 — Services and systemd

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain what a service is and how `systemd` manages units.
- Distinguish starting a service now from enabling it at boot.
- Start, stop, restart, reload, enable, and disable services safely.
- Read service-specific and recent system logs.

## 🏕️ Caveman Story

At night, most villagers go home. The fire keeper, gate guard, and water keeper remain on duty because the village depends on them continuously.

Chief Grog appoints a supervisor who starts these workers in the correct order, checks their condition, records their messages, and can bring them back after a failure.

## 🖼️ Big Concept Illustration

![Chief Grog supervising always-on village workers at night](../images/06-the-village-workers/services-and-systemd-hero.png)

```text
Boot → systemd → dependencies → services → ready system
```

```text
systemd
├── ssh.service
├── nginx.service
├── database.service
├── timer units
├── mount units
└── target units
```

## 📖 Concept Explained Simply

A **service** provides a long-running capability, often in the background. A **daemon** is the process that performs such background work; a systemd service unit describes how that daemon should be started and managed.

`systemd` is the init and service manager used by many Linux distributions. PID 1 starts early in boot, activates units according to dependencies, and supervises their lifecycle.

Two actions are often confused:

```text
start  → make active now
enable → arrange activation during future boots
```

Likewise, **reload** asks a service to reread configuration without a full stop when supported; **restart** stops and starts it, usually causing more disruption.

## 🌍 Real Linux Example

After changing an Nginx configuration, an engineer validates it first and then requests a reload so existing connections can often continue. If the service fails, its unit status and journal reveal the exit code and recent messages.

In cloud images and containers, service management can differ. Traditional VMs commonly use systemd; a minimal container often runs its application directly and relies on a container orchestrator for lifecycle management.

## 🛠️ Commands Introduced

### `systemctl` — Manage systemd Units

```bash
systemctl status ssh
systemctl is-active ssh
systemctl is-enabled ssh
```

Checks detailed status, current activity, and boot enablement. On some distributions, the unit is named `sshd` instead of `ssh`.

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
```

- `start`: activates now.
- `stop`: deactivates now.
- `restart`: performs a stop followed by a start.
- `reload`: rereads configuration if the unit supports it.

```bash
sudo systemctl enable nginx
sudo systemctl disable nginx
sudo systemctl enable --now nginx
```

- `enable`: configures future boot activation but does not necessarily start now.
- `disable`: removes boot enablement but does not necessarily stop now.
- `enable --now`: enables and starts in one operation.

### `journalctl` — Read the systemd Journal

```bash
journalctl -u nginx
journalctl -u nginx --since "30 minutes ago"
```

`-u` filters by unit; `--since` limits the time range.

```bash
journalctl -f
journalctl -xe
```

- `-f`: follows new log messages live.
- `-x`: adds available explanatory text.
- `-e`: jumps near the end of the journal.

Use `sudo` when journal permissions restrict the required entries.

## 💡 Caveman Tip

Before changing a remote-access service, keep a second tested session or console available. A valid command can still lock you out when configuration or firewall state is wrong.

## ⚠️ Common Mistakes

- Assuming `enable` immediately starts a service.
- Assuming `disable` immediately stops it.
- Restarting when a supported reload would reduce disruption.
- Restarting SSH from the only remote session without recovery access.
- Reading the entire journal instead of filtering by unit and time.
- Assuming every Linux system or container uses systemd.

## 🧪 Hands-on Lab

### Mission: Inspect the Fire Keeper

On a disposable VM:

1. Determine whether your SSH unit is called `ssh` or `sshd`.
2. Check its detailed, active, and enabled states.
3. Read its messages from the last 30 minutes.
4. Follow new journal entries, then stop following without stopping the service.
5. Choose a harmless test service—not your only SSH connection—and practise start, stop, and restart.
6. Compare enablement before and after `enable` and `disable`.
7. Re-enable anything that the VM needs after reboot.

## 📝 Quick Recap

- Services provide long-running capabilities.
- systemd manages many kinds of units and usually runs as PID 1.
- Start/stop affect the current state; enable/disable affect boot activation.
- Reload and restart are not interchangeable.
- The journal provides unit-aware logs.

## 🧠 Interview Questions

1. What is the relationship between a daemon and a service unit?
2. What is the difference between `start` and `enable`?
3. When is reload preferable to restart?
4. How would you view logs for one unit from a recent time window?
5. Why might `systemctl` fail inside a container?

## 📚 What's Next

The workers are supervised. Next, learn whether they have enough CPU, memory, and I/O capacity in [05 — CPU, Memory and Load](05-cpu-memory-and-load.md).
