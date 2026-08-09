# 05 — Security Hardening

> “The strongest gate still fails if every villager carries its key.” — Chief Grog

## 🎯 Learning Objectives

- Explain attack surface, least privilege, defence in depth, and secure baselines.
- Prioritise hardening by risk rather than applying random checklists.
- Validate SSH and sudo configuration before activation.
- Add authentication protection, auditing, and security assessment.
- Preserve recoverability while changing remote access controls.

## 🏕️ Caveman Story

Chief Grog protects the village with layers.

Only required gates remain open. Guards verify identities. Workers receive only the keys needed for their jobs. Important actions enter a permanent record. Extra treasure is not left beside the gate. The guards practise what to do if one wall is breached.

No single wall is perfect, so the village limits both the chance and the impact of failure.

## 🖼️ Big Concept Illustration

![Chief Grog inspecting layered village security with gates, guards, keys, and audit records](../images/08-running-the-village/security-hardening-hero.png)

```text
Identity → least privilege → host configuration → service exposure
        → patching → monitoring/audit → backup/recovery
```

```text
Internet → cloud/network controls → host firewall → authenticated service
                                              → authorised user/process
                                              → protected data
```

## 📖 Concept Explained Simply

Hardening reduces unnecessary exposure and makes compromise harder to achieve, detect, and expand.

- **Attack surface:** reachable services, identities, software, and interfaces an attacker can target.
- **Least privilege:** grant only the access required, for only as long as required.
- **Defence in depth:** use independent protective layers.
- **Secure baseline:** an approved, repeatable configuration that can be measured for drift.
- **Audit trail:** evidence of security-relevant actions and outcomes.

Start from asset value, threats, exposure, and business requirements. Then remove unused services and accounts, enforce strong authentication, restrict privileges and network access, patch, centralise logs, protect secrets, and test recovery.

### Why Should I Care?

Most production servers are continuously scanned. A forgotten service, excessive permission, leaked key, or weak operational process can turn one mistake into a wider breach.

## 🌍 Real Linux Example

An Internet-facing VM permits SSH only through a controlled management path, uses individual keys and MFA where supported, disables direct root login, grants audited sudo roles, exposes only the application port, ships security logs centrally, applies timely patches, and retains protected backups.

Cloud IAM, security groups, metadata-service protections, disk encryption, and workload identities add layers outside the guest. Kubernetes uses RBAC, Pod Security controls, NetworkPolicy, secret management, image policy, and runtime detection. AI systems must also protect model artifacts, prompts, datasets, tokens, and high-value GPU capacity.

## 🛠️ Commands Introduced

These tools inspect and validate controls. Changing access on a remote host can lock you out: keep a second tested session and provider console or break-glass path before applying changes.

### `sshd -T` — Validate Effective SSH Server Configuration

```bash
sudo sshd -t
sudo sshd -T | less
sudo sshd -T -C user=tharun,host=server.example,addr=192.0.2.10
```

`-t` validates syntax. `-T` prints effective configuration. `-C` evaluates conditional `Match` rules for supplied connection attributes. Validate before reload, then test a new connection before closing the old one.

### `visudo -c` — Validate Sudo Policy

```bash
sudo visudo -c
sudo visudo -cf /etc/sudoers.d/operations
```

Use `visudo` to edit safely because it checks syntax and locking. `-c` checks policy; `-f` targets a file. Prefer narrowly scoped commands and groups over unrestricted `ALL` rules.

### `fail2ban-client` — Inspect Authentication Bans

```bash
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

Fail2ban reacts to repeated failures by updating a configured ban action. It is an additional control, not a substitute for strong authentication, restricted exposure, or rate limiting. Confirm the jail actually matches your log source.

### `auditctl` and `ausearch` — Inspect Linux Audit Evidence

```bash
sudo auditctl -s
sudo auditctl -l
sudo ausearch -m USER_AUTH -ts today
sudo ausearch -k identity-files -ts today -i
```

`auditctl -s` shows audit status and `-l` lists loaded rules. `ausearch` filters by message type or rule key; `-i` interprets numeric values. Persistent rules belong in the distribution’s audit rules configuration, not ad hoc production commands.

### `lynis` — Run a Non-Destructive Host Audit

```bash
sudo lynis audit system --quick
```

Lynis reports findings and suggestions. Treat output as input to risk assessment—not a command to apply every recommendation blindly. Test changes and document accepted exceptions.

## 💡 Caveman Tip

Every hardening change needs four things: the risk it reduces, the owner, a safe validation method, and a recovery path.

## ⚠️ Common Mistakes

- Editing SSH, sudo, or firewall policy without recovery access.
- Disabling controls to “make it work” and forgetting to restore them.
- Applying a benchmark without considering the server’s role.
- Sharing root accounts or long-lived private keys.
- Storing secrets in scripts, shell history, images, or repositories.
- Collecting audit logs locally but not protecting or reviewing them.
- Assuming a hardened server no longer needs monitoring and backups.

## 🧪 Hands-on Lab

### Mission: Protect the Village Without Closing It

Use a disposable VM with console access:

1. List the server’s purpose, exposed services, privileged identities, and valuable data using earlier lessons.
2. Run SSH syntax and effective-configuration checks without changing anything.
3. Create a lab sudoers fragment with one harmless command, validate it, and test it with a non-root lab user.
4. Inspect Fail2ban status if installed; explain what protection it does and does not provide.
5. Review audit status and search today’s authentication records.
6. Run a quick Lynis audit and prioritise three findings by likelihood, impact, and operational cost.
7. Document validation and rollback for one proposed hardening change.

## 📝 Quick Recap

```text
Know the asset and threat
       ↓
Reduce exposure + enforce identity + least privilege
       ↓
Patch + audit + monitor + recover
       ↓
Validate continuously and manage drift
```

## 🧠 Interview Questions

1. What is attack surface, and how would you reduce it on a Linux server?
2. What does defence in depth mean in practice?
3. How would you change SSH safely on a remote cloud VM?
4. Why should benchmark findings be risk-assessed rather than blindly applied?
5. What is the difference between authentication, authorisation, and auditing?

## 📚 What's Next

Even a well-operated, hardened server can fail. [06 — Troubleshooting](06-troubleshooting.md) teaches a calm production incident method.
