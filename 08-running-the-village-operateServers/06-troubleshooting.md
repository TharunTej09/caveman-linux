# 06 — Production Troubleshooting

> “Restore the feast first. Debate the broken cart after the village is fed.” — Chief Grog

## 🎯 Learning Objectives

- Separate symptom, impact, contributing factors, and root cause.
- Use a structured production incident workflow.
- Collect evidence before making changes or restarting services.
- Inspect open files, port owners, system calls, crashes, and boot delays.
- Validate recovery and turn incidents into preventive improvements.

## 🏕️ Caveman Story

The village food line suddenly stops.

Chief Grog first protects the villagers and limits the damage. He names an incident leader, records the time, checks what changed, and follows the food path until he finds the first broken boundary.

He makes the smallest safe repair, watches the line recover, and only then investigates why the cart failed and how to prevent another stoppage.

## 🖼️ Big Concept Illustration

![Chief Grog leading a calm evidence-driven response to a broken village service](../images/08-running-the-village/production-troubleshooting-hero.png)

```text
Detect → declare → assess impact → stabilise → collect evidence
      → form hypothesis → test safely → mitigate/fix → validate
      → monitor → document timeline → prevent recurrence
```

## 📖 Concept Explained Simply

Troubleshooting is a controlled learning process.

1. Define what should happen and what actually happens.
2. Determine scope, severity, start time, and affected users.
3. Check recent deployments, patches, configuration, traffic, and dependencies.
4. Follow the request path and identify the first failed expectation.
5. Form one falsifiable hypothesis.
6. Run the smallest safe test.
7. Mitigate user impact when necessary.
8. Apply one controlled fix and validate end to end.
9. Monitor for recurrence and document evidence.

A **symptom** is visible failure. A **contributing factor** increased likelihood or impact. A **root cause** is the underlying condition whose correction prevents the same failure path. Do not force a single cause when a system failure resulted from several interacting conditions.

### Why Should I Care?

During an outage, random commands increase risk and erase evidence. A shared method reduces recovery time, helps communication, and creates learning instead of blame.

## 🌍 Real Linux Example

Users receive HTTP 503 responses. The load balancer reports unhealthy backends. The service is running but repeatedly timing out on a database dependency. A recent credential rotation changed one secret but not another. The team rolls back the secret change, confirms request success, monitors recovery, and later improves rotation testing and alert context.

Cloud incidents may cross DNS, load balancers, IAM, quotas, managed dependencies, networks, and guest systems. Kubernetes incidents add scheduler, node, pod, Service, endpoint, volume, and policy boundaries. AI incidents may include model-loading, GPU allocation, out-of-memory, queue, tokenizer, and upstream data failures.

## 🛠️ Commands Introduced

Earlier commands are intentionally combined here: `systemctl`, `journalctl`, health tools, networking checks, and `curl`. The following commands fill specific diagnostic gaps.

### `lsof` — Identify Open Files and Network Endpoints

```bash
sudo lsof /var/log/example.log
sudo lsof -iTCP:8080 -sTCP:LISTEN -nP
sudo lsof +L1
```

The first finds processes holding a file. The second identifies a TCP listener without DNS or service-name conversion. `+L1` finds open files whose link count is below one—useful when deleted files still consume disk space.

### `fuser` — Find Processes Using a Resource

```bash
sudo fuser -v /mnt/data
sudo fuser -v 8080/tcp
```

`-v` shows process details. This helps explain a busy mount or port. Avoid `-k` in production unless process termination is explicitly planned and approved.

### `strace` — Observe System Calls

```bash
strace -f -o /tmp/example.strace command --argument
sudo strace -f -tt -p PID -o /tmp/process.strace
```

`-f` follows child processes, `-tt` adds precise timestamps, `-p` attaches to a PID, and `-o` stores output. Tracing can affect performance and expose sensitive data. Use a narrow time window, protect the output, and prefer reproduction outside production.

### `coredumpctl` — Inspect Recorded Process Crashes

```bash
coredumpctl list
coredumpctl info PID_OR_EXE
sudo coredumpctl debug PID_OR_EXE
```

Availability depends on systemd-coredump configuration and retention. Core dumps may contain credentials or customer data. Restrict access and use a debugger only in an authorised environment.

### `systemd-analyze` — Investigate Boot and Unit Timing

```bash
systemd-analyze time
systemd-analyze blame
systemd-analyze critical-chain
systemd-analyze verify /etc/systemd/system/example.service
```

`time` summarises boot phases, `blame` ranks unit activation time, `critical-chain` shows timing dependencies, and `verify` checks a unit file. A slow-listed unit is not necessarily on the critical path, so interpret `blame` with `critical-chain` and logs.

## 💡 Caveman Tip

Keep an incident notebook with timestamps, observations, hypotheses, commands, changes, owners, and results. Memory becomes unreliable under pressure.

## ⚠️ Common Mistakes

- Restarting before collecting logs, state, and timestamps.
- Changing several variables simultaneously.
- Treating correlation as causation.
- Debugging the host while ignoring dependencies and recent changes.
- Attaching heavy tracing tools to critical processes without assessing risk.
- Declaring recovery after one successful request.
- Writing a post-incident report focused on blame instead of system improvement.

## 🧪 Hands-on Lab

### Final Mission: Restore the Village Service

Create a disposable systemd service that listens on a high port and writes to a lab directory.

1. Record its expected request, response, port, user, files, and dependencies.
2. Introduce one fault: wrong file permission, occupied port, invalid unit option, or missing dependency.
3. State impact, scope, start time, and the last known change.
4. Gather service, log, health, port, and file-owner evidence using the smallest relevant tools.
5. Write one hypothesis and one test that could disprove it.
6. Apply one controlled fix.
7. Validate the process, listener, application response, logs, and stability over several checks.
8. Produce a timeline with symptom, evidence, cause, mitigation, validation, and preventive action.

## 📝 Quick Recap

```text
Protect users → preserve evidence → find first failed boundary
              → test one hypothesis → change one thing
              → validate deeply → monitor → learn
```

Incident note template:

```text
Expected / actual / impact / scope:
Start time / detection / recent changes:
Evidence and hypotheses:
Mitigation / fix / owner:
Validation and monitoring:
Root cause / contributing factors / prevention:
```

## 🧠 Interview Questions

1. What evidence would you collect before restarting a failed service?
2. How do symptom, contributing factor, and root cause differ?
3. When would you use `lsof`, `strace`, or `coredumpctl`?
4. Why might `systemd-analyze blame` be misleading by itself?
5. How do you validate that an incident is truly resolved?
6. What makes a useful blameless post-incident review?

## 📚 What's Next

Troubleshooting often happens from a distant workstation. Next, learn safe access in [07 — Remote SSH Administration](07-remote-ssh-administration.md).
