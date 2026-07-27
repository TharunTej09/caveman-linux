# Linux Server Health and Troubleshooting

## Big Question

When a Linux server has a problem, how do we find the cause safely?

## The Chief Inspects the Village

When something goes wrong in the village, the chief does not immediately rebuild everything. First, the chief observes:

- Which village is this?
- How long has it been running?
- Are the workers overloaded?
- Is there enough working space?
- Are the storage caves full?
- Are the roads connected?
- Is the required service operating?
- What do the activity records say?

A Linux administrator follows the same approach: **observe first, identify the cause, and then apply the smallest safe fix**.

## A Simple Troubleshooting Method

Use this order when investigating a server:

```text
Identify the server
        ↓
Confirm the symptom
        ↓
Check CPU, memory, disk, and network
        ↓
Check the affected process or service
        ↓
Read the logs
        ↓
Fix the cause
        ↓
Verify that the service recovered
```

Do not restart a service or delete files before understanding the likely cause. A quick action can hide useful evidence or make the problem worse.

## Essential Health-Check Commands

### 1. Identify the Server and User

```bash
hostname
whoami
```

| Command | What It Shows | Why It Matters |
|---|---|---|
| `hostname` | The server's hostname | Confirms that you are working on the intended server |
| `whoami` | The current user | Helps explain which permissions and commands are available |

Always confirm the server and your user before making changes.

### 2. Check Uptime and System Load

```bash
uptime
```

This displays:

- The current time
- How long the server has been running
- The number of logged-in users
- Load averages for the last 1, 5, and 15 minutes

A high load average can indicate that the system has more work than its CPU or other resources can handle. Interpret it alongside the number of CPU cores and other system metrics; a load number is not meaningful by itself.

### 3. Check Memory

```bash
free -h
```

The `-h` option displays values in a human-readable format such as MiB and GiB.

Pay particular attention to the `available` value. Linux intentionally uses unused RAM for caching, so a small `free` value alone does not necessarily mean that the server has a memory problem.

### 4. Monitor Processes

```bash
htop
ps -ef
```

| Command | Purpose |
|---|---|
| `htop` | Interactive view of CPU, memory, and running processes |
| `ps -ef` | Snapshot listing of running processes with detailed information |

`htop` may not be installed on every server. The commonly available `top` command can be used instead:

```bash
top
```

Look for processes consuming unusually high CPU or memory, but investigate why before stopping them.

### 5. Check Filesystem Space

```bash
df -h
```

This shows the used and available space on mounted filesystems. Check the `Use%` column for filesystems that are close to full.

To investigate which directories consume space, an administrator may use:

```bash
du -xh --max-depth=1 /path/to/check
```

Start with a specific, known path. Avoid deleting files until you understand what created them and whether they are still required.

### 6. Check Network Interfaces

```bash
ip addr
```

This displays network interfaces and their IP addresses. It helps answer:

- Is the expected interface present?
- Is it active?
- Does it have the expected IP address?

An interface marked `UP` is enabled, but further tests may still be needed to confirm that another system is reachable.

### 7. Check a Service

```bash
systemctl status nginx
```

This shows whether the Nginx service is running, stopped, or failed. It also displays recent status information that may point to the problem.

Replace `nginx` with the name of the service you are investigating:

```bash
systemctl status ssh
systemctl status docker
```

Service names can differ between Linux distributions.

### 8. Read Service Logs

```bash
journalctl -u nginx
```

This displays journal entries for the Nginx service. To focus on the current boot and recent messages, use:

```bash
journalctl -u nginx -b --no-pager -n 50
```

Logs often explain why a service failed—for example, an invalid configuration, missing file, occupied port, or permission problem.

Some system information and logs require elevated permissions. Use `sudo` only when your account is authorized and the task requires it.

## Quick Server Inspection

These commands provide a useful first look at a server:

```bash
hostname                    # Show the server hostname
whoami                      # Show the current user
uptime                      # Show uptime and load averages
free -h                     # Check memory usage
df -h                       # Check filesystem usage
ip addr                     # Show network interfaces and IP addresses
ps -ef                      # List running processes
htop                        # Monitor processes interactively
systemctl status nginx      # Check the Nginx service
journalctl -u nginx         # View Nginx service logs
```

These commands primarily inspect the system. Commands such as restarting services, changing permissions, and deleting files modify the system and require greater care.

## Troubleshooting Quick Reference

| Symptom | Probable Cause | How to Verify | Possible Fix | Prevention |
|---|---|---|---|---|
| Server is slow | CPU, memory, disk I/O, or a dependency is overloaded | Use `uptime`, `top` or `htop`, `free -h`, and `iostat` | Correct the cause, tune the workload, or add capacity | Establish performance baselines and capacity alerts |
| Disk is full | Large logs, temporary files, or growing application data | Use `df -h` and carefully scoped `du -xh` commands | Archive or remove confirmed safe data, fix uncontrolled growth, or extend storage | Configure log rotation and disk-usage alerts |
| Service is unavailable | Stopped process, invalid configuration, port conflict, firewall rule, or failed dependency | Use `systemctl status`, `journalctl`, and `ss -tulpn` | Correct the fault, validate the configuration, and restart safely | Use health checks, configuration validation, and rollback plans |
| SSH access fails | Network rule, SSH service, key, username, or file permission problem | Test connectivity and use console access to inspect the SSH service and authentication logs | Restore the correct rule, service, key, user, or permission | Maintain tested break-glass access and configuration control |
| Error rate is high | Application bug, overload, or downstream service failure | Examine application logs, metrics, traces, and dependency health | Roll back, fail over, reduce load, or repair the dependency | Use staged deployments and service-level alerts |

`iostat` may require the `sysstat` package. If a referenced tool is unavailable, use the tools already installed on the system or follow your organization's approved installation process.

## Example Investigation: Nginx Is Unavailable

Suppose users cannot open a website served by Nginx.

### Step 1: Confirm the Correct Server

```bash
hostname
whoami
```

### Step 2: Check the Service

```bash
systemctl status nginx
```

### Step 3: Read Recent Logs

```bash
journalctl -u nginx -b --no-pager -n 50
```

### Step 4: Check Whether a Process Is Listening

```bash
ss -tulpn
```

### Step 5: Check Basic Resources

```bash
uptime
free -h
df -h
```

### Step 6: Correct and Verify

Fix the specific cause you discovered. Then check the service status and test the website again. A command succeeding is not enough—the user-facing service must also work.

## Important Habits

- Confirm the hostname before making changes.
- Record the exact error and time it occurred.
- Change one thing at a time.
- Read logs before restarting a failed service.
- Never delete unknown files merely to free space.
- Verify the result from the user's point of view.
- Document the cause, fix, and prevention measure.

## Simple Definition

**Linux troubleshooting is a process of observing the system, narrowing down the cause, applying a safe fix, and verifying recovery.**

Remember: **identify, inspect, understand, fix, and verify.**
