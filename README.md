# 🪨 Caveman Linux

> Learn Linux through one evolving world: cave → village → city → cloud → AI infrastructure.

Caveman Linux is a free, story-first Linux course for beginners who want practical system-administration skills without losing sight of *why* each concept matters. Chief Grog turns hardware, filesystems, commands, permissions, processes, networks, servers, containers, Kubernetes, and AI infrastructure into one connected mental model.

## Why This Course Is Different

Most courses begin with a wall of commands. This course begins with a problem:

```text
🧠 Question → 🪨 Story → 🖼️ Diagram → 💻 Linux → 🧪 Practice → 🌍 Production
```

The analogy makes the idea memorable; the technical explanation makes it accurate; the lab makes it useful.

## Who This Is For

- Complete Linux beginners
- Cloud, DevOps, data, and AI learners who need stronger foundations
- Developers moving from a laptop to production servers
- Interview candidates who want to explain concepts, not only memorise commands

No previous Linux experience is required. Basic computer use and permission to run a disposable virtual machine are enough.

## Course Map

| Chapter | Caveman journey | What you will learn |
| --- | --- | --- |
| [01 — Before Linux](01-Before%20Linux/README.md) | Meet the village | Computers, hardware, servers, software, operating systems, and clients |
| [02 — Meet the Caveman Chief](02-Meet%20the%20Caveman%20Chief%20-%20Linux/README.md) | Meet Chief Grog | Linux, kernel, shell, distributions, boot, installation, and first health checks |
| [03 — The Cave Map](03-the-cave-map%20-%20FileSystem/README.md) | Learn the cave layout | Filesystems, directories, paths, files, and mounted storage |
| [04 — Finding Your Tools](04-finding-your-tools%20-%20Learn%20Commands/README.md) | Use the tool rack | Commands, text, search, shell environment, editors, scripting, and scheduling |
| [05 — Protecting the Treasure](05-protecting-the-treasure%20-%20UserPermissions/README.md) | Control the keys | Users, groups, permissions, ownership, sudo, and access control |
| [06 — The Village Workers](06-the-village-workers-%20Processes%20and%20Services/README.md) | Organise work | Processes, states, signals, services, CPU, memory, and load |
| [07 — Talking Between Villages](07-talking-between-villages%20-%20Networking/README.md) | Connect villages | IP, subnets, protocols, DNS, routing, ports, firewalls, and diagnosis |
| [08 — Running the Village](08-running-the-village-operateServers/README.md) | Operate production | Health, logs, patching, backups, hardening, SSH, and troubleshooting |
| [09 — Building Modern Cities](09-building-modern-cities%20-%20Cloud-Containers-Kubernetes/README.md) | Scale the village | VMs, cloud, containers, Docker, Kubernetes, and infrastructure as code |
| [10 — Teaching the City to Think](10-teaching-the-city-to-think%20-%20Understand%20AI%20Infra/README.md) | Run intelligent systems | AI infrastructure, GPUs, serving, vectors, LLM platforms, and observability |

## Recommended Learning Path

Work through the chapters in order the first time. Each chapter depends on the mental model built before it.

```text
Computer → Linux → Filesystem → Commands → Permissions
    → Processes → Networking → Operations → Cloud → AI
```

After a chapter, complete the related [hands-on labs](labs/README.md). Keep the [cheatsheets](cheatsheets/README.md) nearby for recall after you understand the concepts.

## Start Practising

Use a disposable Ubuntu or other Linux virtual machine. Never practise destructive commands on a production server.

1. Read [Before Linux](01-Before%20Linux/README.md).
2. Build a safe environment with [Lab 01 — Create a Linux VM](labs/01-create-linux-vm.md).
3. Continue in chapter order and type commands yourself.
4. Predict the result before pressing Enter, then verify it.
5. Record mistakes and observations in your own engineering notebook.

## Labs and Quick References

- [Hands-on Labs](labs/README.md) — complete guided missions with verification and cleanup
- [Linux Cheatsheets](cheatsheets/README.md) — compact, task-oriented reminders

## Safety Principles

- Use a disposable VM or lab environment.
- Read a command and confirm its target before using `sudo`, `rm`, `chmod`, `chown`, firewall rules, mounts, or package changes.
- Preserve a second SSH session or console before changing remote access.
- Back up important data and test restoration.
- Treat copied commands as examples to understand, not magic spells.

## Contributing

Corrections, clearer stories, accessible diagrams, labs, and production examples are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change. Please report security concerns through [SECURITY.md](SECURITY.md), not a public issue.

## License

This project is available under the [MIT License](LICENSE).

---

If you understand the story, you will not need to memorise the concept.
