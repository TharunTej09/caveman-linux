# Server Operations Cheatsheet

## First Five Minutes

```bash
hostnamectl                         # confirm the host
uptime                              # uptime and load
free -h                             # memory pressure clues
df -hT                              # filesystem capacity
systemctl list-units --failed       # failed services
journalctl -p warning --since today # important recent journal entries
ss -lntup                           # listening services
```

## Change Safely

```text
Define expected result
        ↓
Capture baseline and backup
        ↓
Validate configuration
        ↓
Make one controlled change
        ↓
Verify service and user outcome
        ↓
Rollback if validation fails
```

## Common Operations

| Need | Ubuntu/Debian example |
| --- | --- |
| Review updates | `apt list --upgradable` |
| Validate Nginx | `sudo nginx -t` |
| Archive data | `tar -czf backup.tgz PATH` |
| Synchronise data | `rsync -a SOURCE/ DEST/` |
| Verify a file | `sha256sum FILE` |
| SSH effective config | `sudo sshd -T` |
| Recent boots | `journalctl --list-boots` |

## Incident Note

Record: impact, start time, detection, evidence, hypothesis, one change at a time, validation, recovery time, root cause, and prevention. Do not delete evidence or restart first merely to make an alert disappear.
