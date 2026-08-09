# 04 — Backups and Recovery

> “Treasure is not protected because a copy exists. It is protected when the copy can rebuild the village.” — Chief Grog

## 🎯 Learning Objectives

- Distinguish backup, snapshot, replication, archive, and high availability.
- Define Recovery Point Objective (RPO) and Recovery Time Objective (RTO).
- Apply the 3-2-1 backup principle and protect copies from the same failure.
- Create, verify, and restore file backups safely.
- Design restore tests that prove business recovery.

## 🏕️ Caveman Story

Chief Grog stores seed in the main granary. A second granary nearby protects against a broken door—but not a flood that reaches both buildings.

So the village keeps several copies, on different materials, with one copy beyond the valley. The keepers regularly open a sealed basket and grow a test crop.

The test proves what the inventory list cannot: the seed can bring the village back.

## 🖼️ Big Concept Illustration

![Chief Grog verifying protected backup stores and a successful village recovery test](../images/08-running-the-village/backups-and-recovery-hero.png)

```text
Production data → local backup → separate storage → off-site/immutable copy
                         │                          │
                         └──── verify ── restore test ── validate service
```

| Caveman concept | Recovery concept |
| --- | --- |
| How much recent grain can be lost? | RPO |
| How long until food returns? | RTO |
| Second nearby granary | Local backup or replica |
| Sealed store beyond the valley | Off-site or immutable backup |
| Growing a test crop | Restore test |

## 📖 Concept Explained Simply

- A **backup** is an independent recoverable copy.
- A **snapshot** captures state at a point in time, usually within one storage platform.
- **Replication** copies changes for availability but can also copy deletion or corruption.
- An **archive** preserves data for long-term retention.
- **High availability** reduces interruption; it does not replace backup.

The 3-2-1 principle suggests three copies, on two media or failure domains, with one off-site. Modern ransomware planning often adds an offline or immutable copy and verified recovery.

RPO defines acceptable data loss measured in time. RTO defines acceptable restoration time. These business requirements determine frequency, technology, cost, and test cadence.

Application consistency matters. Copying database files while they are changing may not create a valid backup. Use database-native dumps, coordinated snapshots, or application-aware tooling where required.

### Why Should I Care?

Hardware failure, operator error, corruption, ransomware, and failed deployments are inevitable possibilities. Recovery is the control that limits their business impact.

## 🌍 Real Linux Example

A PostgreSQL service has a one-hour RPO and four-hour RTO. The design combines frequent database-aware backups, encrypted off-site storage, protected credentials, retention rules, and quarterly restores into an isolated environment where integrity and application queries are validated.

Cloud snapshots are useful but can share an account, region, or control plane with production. Kubernetes configuration, persistent data, secrets, and external dependencies need separate recovery plans. Large AI systems may back up model artifacts and configuration while regenerating replaceable caches from authoritative data.

## 🛠️ Commands Introduced

Practise only with disposable data and restore into a separate destination first.

### `tar` — Create and Inspect an Archive

```bash
tar -czf app-config-$(date +%F).tar.gz /etc/example-app
tar -tzf app-config-2026-07-30.tar.gz
mkdir -p restore-test
tar -xzf app-config-2026-07-30.tar.gz -C restore-test
```

`-c` creates, `-t` lists, `-x` extracts, `-z` uses gzip, `-f` selects the archive, and `-C` chooses the extraction directory. Archives are not automatically encrypted, off-site, incremental, or application-consistent.

### `rsync` — Synchronise Files Efficiently

```bash
rsync -aHAXvn /srv/example/ /backup/example/
rsync -aHAXv --delete /srv/example/ /backup/example/
```

`-a` preserves common metadata, `-H` hard links, `-A` ACLs, `-X` extended attributes, `-v` shows actions, and `-n` performs a dry run. Trailing slashes matter. `--delete` makes the destination mirror deletions and can destroy recovery history—use it only after reviewing a dry run and destination.

### `sha256sum` — Record and Verify Integrity

```bash
sha256sum app-config-2026-07-30.tar.gz > app-config-2026-07-30.tar.gz.sha256
sha256sum -c app-config-2026-07-30.tar.gz.sha256
```

A checksum detects change or corruption; it does not prove authenticity unless the checksum itself is protected.

### `restic` — Use a Versioned Encrypted Backup Repository

```bash
export RESTIC_REPOSITORY=/backup/restic-repo
restic init
restic backup /srv/example
restic snapshots
restic check
restic restore latest --target ./restore-test
```

Restic provides encrypted, deduplicated, versioned backups. Supply credentials through a protected mechanism, not shell history. Repository checks are valuable, but only a restore plus application validation proves recoverability.

## 💡 Caveman Tip

Write the restore procedure before the incident, automate it where possible, and test it with people who may actually be on call.

## ⚠️ Common Mistakes

- Treating RAID, replication, or snapshots as complete backup strategies.
- Keeping every copy in the same server, account, or region.
- Backing up encrypted data without protecting recovery keys separately.
- Using `rsync --delete` without a dry run or version history.
- Restoring over production before validating an isolated restore.
- Measuring backup success but not restore duration and application integrity.

## 🧪 Hands-on Lab

### Mission: Rebuild the Food Store

1. Create disposable configuration and data files under a lab directory.
2. Define an RPO and RTO for the imaginary service.
3. Create and inspect a `tar` archive.
4. Generate and verify its checksum.
5. Preview an `rsync` copy, then perform it without `--delete`.
6. Delete one lab source file deliberately.
7. Restore into a separate directory.
8. Compare contents, ownership, permissions, and a simple application check.
9. Record actual recovery time and whether the stated RTO was met.

## 📝 Quick Recap

```text
Business impact → RPO + RTO → backup design → protected copies
              → integrity check → isolated restore → application validation
```

## 🧠 Interview Questions

1. What is the difference between RPO and RTO?
2. Why does replication not replace backup?
3. What does application-consistent backup mean?
4. What risks does `rsync --delete` introduce?
5. How would you prove that a backup is recoverable?

## 📚 What's Next

Recovery limits the impact of failure. [05 — Security Hardening](05-security-hardening.md) reduces the chance and reach of an attack.
