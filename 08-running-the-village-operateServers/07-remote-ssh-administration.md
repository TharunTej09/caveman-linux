# 07 — Remote SSH Administration

## 🎯 Learning Objectives

- Explain SSH client, server, host identity, user authentication, and encrypted session.
- Connect with keys, transfer files, and use a safe client configuration.
- Diagnose remote-access failures without weakening security.

## 🏕️ Caveman Story

Chief Grog must command a distant village. A guarded tunnel encrypts every message. Before entering, each side checks identity: the traveller verifies the village seal, and the guard verifies the traveller's key.

SSH is that guarded tunnel.

## 🖼️ Big Concept Illustration

```text
Administrator        encrypted SSH transport        Linux server
    client  ─────────────────────────────────────→  sshd
       │          verify server host key              │
       └────────── prove user identity with key ──────┘
```

## 📖 Concept Explained Simply

The `ssh` client contacts an SSH server, normally `sshd` on TCP port 22. The server presents a host key so the client can detect impersonation. The user then authenticates—preferably with a protected private key while the matching public key is authorised on the server.

The private key stays on the client. A fingerprint warning after a server was previously trusted must be investigated; deleting the warning blindly defeats host verification.

### Why Should I Care?

Most cloud and data-centre Linux servers are administered remotely. One careless SSH change can expose credentials or lock every operator out.

## 🌍 Real Linux Example

An engineer connects through a bastion host using a named key, transfers a reviewed configuration, validates it remotely, reloads the service, and keeps a second session open until access is reverified.

## 🛠️ Commands Introduced

```bash
ssh user@server                       # interactive session
ssh -v user@server                    # client-side diagnostic detail
ssh-keygen -t ed25519 -a 64           # create a modern key pair
ssh-copy-id user@server               # install public key when supported
scp report.txt user@server:/tmp/      # copy a file
sftp user@server                      # interactive file transfer
ssh-keygen -lf ~/.ssh/id_ed25519.pub  # show public-key fingerprint
```

A reusable client entry in `~/.ssh/config` can define `Host`, `HostName`, `User`, `IdentityFile`, and `ProxyJump`. Protect the directory and private configuration appropriately.

Server-side checks:

```bash
sudo sshd -t
sudo sshd -T
systemctl status ssh
sudo journalctl -u ssh --since "15 minutes ago"
```

Some distributions name the service `sshd`. Validate configuration before reload. When changing remote access, keep a verified session or provider console available.

## 💡 Caveman Tip

Host verification answers “is this the intended server?” User authentication answers “is this an authorised user?” Both are required.

## ⚠️ Common Mistakes

- Sharing or copying a private key to the server.
- Accepting an unexpected changed host key without independent verification.
- Disabling password login before key access and console recovery are tested.
- Exposing port 22 to the entire internet instead of restricting source paths.
- Debugging by weakening permissions or authentication controls.

## 🧪 Hands-on Lab

1. Use two lab VMs, or one VM and its host with reachable SSH networking.
2. Generate an Ed25519 key with a passphrase.
3. Verify the server's host-key fingerprint through its console before first trust.
4. Install only the public key and connect with `ssh -v`.
5. Transfer a harmless file with `scp`, verify its checksum on both sides, and remove the remote copy.
6. Review authentication logs for the successful connection.

## 📝 Quick Recap

```text
Verify server → establish encryption → authenticate user
              → authorise access → operate → audit
```

## 🧠 Interview Questions

1. What is the difference between a host key and a user key?
2. Why must a private key remain private?
3. How would you change SSH settings without locking out the team?
4. What sequence would you use to diagnose an SSH timeout versus permission denied?

## 📚 What's Next

Complete the [server operations module](README.md), then continue to [Chapter 09 — Building Modern Cities](../09-building-modern-cities%20-%20Cloud-Containers-Kubernetes/README.md).
