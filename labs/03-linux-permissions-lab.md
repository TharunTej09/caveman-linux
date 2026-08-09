# Lab 03 — Protect the Shared Treasure

## 🎯 Mission

Create a shared project directory where a team can collaborate while outsiders remain blocked.

## Prerequisites

- A disposable Linux VM
- A user with `sudo` permission

## ⚠️ Safety

Use only the explicitly named `/tmp/caveman-permissions-lab` path and the lab accounts below. Do not recursively change permissions on system directories.

## Starting State

```bash
sudo groupadd cavebuilders
sudo useradd -m -s /bin/bash hunterlab
sudo useradd -m -s /bin/bash builderlab
sudo usermod -aG cavebuilders hunterlab
sudo usermod -aG cavebuilders builderlab
sudo mkdir /tmp/caveman-permissions-lab
```

## Tasks

1. Assign group ownership and shared-directory permissions:

   ```bash
   sudo chown root:cavebuilders /tmp/caveman-permissions-lab
   sudo chmod 2770 /tmp/caveman-permissions-lab
   ```

2. Decode `2770`: setgid on the directory, full owner/group access, and no access for others.
3. Create files as two different users:

   ```bash
   sudo -u hunterlab touch /tmp/caveman-permissions-lab/hunter-note
   sudo -u builderlab touch /tmp/caveman-permissions-lab/builder-note
   ```

4. Inspect identity, ownership, and permissions:

   ```bash
   id hunterlab
   id builderlab
   ls -ld /tmp/caveman-permissions-lab
   ls -l /tmp/caveman-permissions-lab
   ```

5. Verify that an unrelated user cannot list the protected directory:

   ```bash
   sudo -u nobody ls /tmp/caveman-permissions-lab
   ```

   A permission-denied result is expected.

## ✅ Verification

- The directory group is `cavebuilders`.
- Its mode includes `rwxrws---`; the `s` shows setgid.
- Files created by both lab users inherit group `cavebuilders`.
- `nobody` cannot list the directory.

## Troubleshooting Clues

- If group membership appears missing in an interactive login, start a new session after `usermod`.
- If created files do not inherit the group, confirm the directory setgid bit with `ls -ld`.
- File write collaboration can also depend on each user's `umask`; directory access alone does not guarantee group-writable files.

## Cleanup

```bash
sudo rm -r /tmp/caveman-permissions-lab
sudo userdel -r hunterlab
sudo userdel -r builderlab
sudo groupdel cavebuilders
```

Confirm the path before running the recursive removal.

## 🧠 Think Like an Engineer

How would you allow one auditor read-only access without adding that person to the write-capable team? Consider a POSIX ACL.
