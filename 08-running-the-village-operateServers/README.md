# 08 — Running the Village: Operating Linux Servers

> “Building a village is only the beginning. Keeping it healthy, secure, and recoverable is the real work.” — Chief Grog

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Read server health as a connected system rather than isolated numbers.
- Use logs, metrics, and alerts to understand what changed.
- Patch packages safely with validation and rollback planning.
- Design backups around recovery requirements and prove that restores work.
- Reduce attack surface without locking yourself out.
- Administer remote servers securely over SSH.
- Troubleshoot production incidents with evidence and controlled changes.

## 🏕️ Caveman Story

Chief Grog’s village is now connected to distant settlements. Its workers, roads, gates, and storage caves are busy every day.

But a village does not remain healthy by accident. Food can run low, tools can wear out, thieves can test the gates, records can disappear, and one broken service can affect everyone.

Chief Grog creates an operations team. They inspect the village, maintain it, protect it, preserve copies of important records, and respond calmly when something fails.

## 🖼️ Big Concept Illustration

![Chief Grog and the operations team running a healthy protected village](../images/08-running-the-village/operating-servers-overview-hero.png)

```text
Observe → Understand → Change safely → Validate → Recover if needed
   ↑                                                    │
   └──────────────── Learn and improve ─────────────────┘
```

```text
Village health     → Server health
Village records    → Logs and metrics
Tool maintenance   → Packages and patches
Emergency supplies → Backups
Gates and guards   → Security hardening
Incident team      → Troubleshooting
```

## 📖 Concept Explained Simply

Running a production server is a continuous cycle—not a collection of emergency commands.

| Lesson | Operational question | Main outcome |
| --- | --- | --- |
| [01 — Server Health](01-server-health.md) | Is the server healthy? | Establish and interpret baselines |
| [02 — Logs and Monitoring](02-logs-and-monitoring.md) | What happened, and when? | Turn signals into actionable evidence |
| [03 — Packages and Patching](03-packages-and-patching.md) | How do we change software safely? | Patch with testing and rollback |
| [04 — Backups and Recovery](04-backups-and-recovery.md) | Can we restore what matters? | Build and test recovery capability |
| [05 — Security Hardening](05-security-hardening.md) | How do we reduce risk? | Apply defence in depth |
| [06 — Troubleshooting](06-troubleshooting.md) | How do we restore service safely? | Diagnose, mitigate, validate, learn |
| [07 — Remote SSH Administration](07-remote-ssh-administration.md) | How do we reach a distant server safely? | Verify hosts, use keys, transfer files, and diagnose access |

### Why Should I Care?

Every website, database, container platform, cloud workload, and AI service eventually depends on servers that must remain available and trustworthy. An engineer who can install Linux but cannot operate it safely is not yet ready to own production systems.

## 🌍 Real Linux Example

A production API becomes slow after a release. An operator compares current CPU, memory, disk, and request signals with the normal baseline; correlates the change with deployment logs; mitigates the impact; restores a known-good version; validates user traffic; and records a preventive action.

The same operating loop applies to a small Ubuntu VM, an AWS or Azure instance, a Kubernetes node, a database server, and a GPU-backed model-serving host.

## 🛠️ Commands Introduced

| Lesson | Commands taught here |
| --- | --- |
| Server Health | `vmstat`, `mpstat`, `iostat`, `pidstat`, `sar` |
| Logs and Monitoring | `logger`, `dmesg`, `tail`, `watch`, `logrotate` |
| Packages and Patching | `apt`, `apt-cache`, `dpkg`, `dnf`, `rpm`, `dnf history` |
| Backups and Recovery | `tar`, `rsync`, `sha256sum`, `restic` |
| Security Hardening | `sshd -T`, `visudo -c`, `fail2ban-client`, `auditctl`, `ausearch`, `lynis` |
| Troubleshooting | `lsof`, `fuser`, `strace`, `coredumpctl`, `systemd-analyze` |
| Remote SSH Administration | `ssh`, `ssh-keygen`, `ssh-copy-id`, `scp`, `sftp` |

Earlier commands such as `systemctl`, `journalctl`, `free`, `df`, `ss`, and `curl` reappear only as supporting evidence in realistic workflows. Their basic syntax remains in the lesson where it was first taught.

## 💡 Caveman Tip

Know what “normal” looks like before the emergency. A number without a baseline, workload, time range, and user impact can be misleading.

## ⚠️ Common Mistakes

- Treating a monitoring alert as the root cause.
- Patching production without a tested rollback or recovery path.
- Calling a backup successful without performing a restore test.
- Hardening SSH without preserving a second verified session or console access.
- Restarting services before collecting volatile evidence.
- Making several changes at once and losing the real cause.

## 🧪 Hands-on Lab

### Module Mission: Operate a Production Village

Use a disposable Linux VM:

1. Record a health baseline under idle and controlled load.
2. Create a test service and send a synthetic log message.
3. Review available package updates and document a patch plan.
4. Back up the service data and restore it to a separate path.
5. Run a non-destructive security audit and prioritise three findings.
6. Break the test service safely, diagnose it, restore it, and write a short incident timeline.

Do not practise destructive failure scenarios on a production server.

## 📝 Quick Recap

```text
Healthy server
     ↓
Useful signals + safe maintenance + tested recovery + layered security
     ↓
Evidence-driven incident response
     ↓
Reliable production service
```

## 🧠 Interview Questions

1. What is the difference between monitoring a symptom and finding a root cause?
2. Why should patches be treated as controlled changes?
3. What makes a backup strategy recoverable rather than merely complete?
4. How would you harden a remote server without locking yourself out?
5. What evidence should be collected before restarting a failed service?

## 📚 What's Next

Begin with [01 — Server Health](01-server-health.md) and learn how Chief Grog recognises a healthy village.

## 🧭 Chapter Navigation

[← Talking Between Villages](../07-talking-between-villages%20-%20Networking/README.md) · [Course Home](../README.md) · [Next: Building Modern Cities →](../09-building-modern-cities%20-%20Cloud-Containers-Kubernetes/README.md)
