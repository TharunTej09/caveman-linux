# 03 — Containers

> “Move the workshop, not the whole mountain.” — Chief Grog

## 🎯 Learning Objectives

- Explain a container as an isolated Linux process rather than a small VM.
- Describe namespaces, cgroups, capabilities, and layered filesystems.
- Distinguish an image from a running container.
- Identify container isolation, persistence, and security boundaries.
- Observe Linux primitives that container runtimes use.

## 🏕️ Caveman Story

Chief Grog's craftsmen travel between cities. Rebuilding every workshop by hand produces different tools and unreliable results.

Grog creates a sealed portable workshop. It carries the required tools and instructions, opens quickly, and looks consistent wherever it travels.

The workshop has its own view of workers, roads, and files. Yet it still uses the destination city's land, guards, and Chief. It is isolated—not a separate mountain.

## 🖼️ Big Concept Illustration

![Portable caveman workshops sharing one Linux city while remaining isolated](../images/09-building-modern-cities/containers-hero.png)

```text
Container A             Container B
App + libraries         App + libraries
     │                        │
Namespaces + cgroups + capabilities
              │
        Shared Linux kernel
              │
        Physical or VM host
```

| Portable workshop | Container concept |
| --- | --- |
| Workshop blueprint | Image |
| Open workshop | Container |
| Separate view | Namespace |
| Resource allowance | Cgroup |
| Permitted tools | Linux capability |
| Shared city Chief | Host kernel |

## 📖 Concept Explained Simply

A container is one or more processes isolated and constrained using operating-system features.

- **Namespaces** give processes separate views of resources such as process IDs, mounts, networks, hostnames, users, and inter-process communication.
- **Cgroups** organise processes and account for or limit CPU, memory, and I/O resources.
- **Capabilities** split powerful root privileges into smaller units that can be granted or removed.
- **Layered filesystems** combine read-only image layers with a small writable container layer.
- An **image** is an immutable package template. A **container** is a runtime instance of that image.

Containers normally share the host kernel. A Linux container therefore is not a complete independent machine and must be compatible with the host's kernel. Isolation reduces interaction; it is not an automatic security guarantee.

### Why Should I Care?

Containers make application packaging faster and more consistent, but production reliability depends on understanding what is isolated, where data lives, which resources are limited, and what still belongs to the host.

## 🌍 Real Linux Example

Two web containers on one VM have different process and network namespaces. Each sees its own filesystem view, while both processes are scheduled by the same Linux kernel. Cgroups prevent one workload from consuming all available memory.

In cloud and AI platforms, containers package APIs, data jobs, notebooks, model servers, CUDA user-space libraries, and sidecars. GPU containers still need compatible host drivers and explicit device access; the GPU is not magically contained inside the image.

## 🛠️ Commands Introduced

These commands expose the Linux foundations beneath container runtimes. Use a disposable lab VM; namespace entry may bypass expected isolation and often needs elevated privileges.

### `lsns` — List Linux Namespaces

```bash
lsns
lsns -t pid
lsns -t net
lsns -p $$
```

- `-t` filters by namespace type.
- `-p $$` shows namespaces used by the current shell process.
- Namespace IDs help reveal which processes share the same view.

### `unshare` — Start a Process in New Namespaces

```bash
unshare --user --map-root-user --uts --fork bash
```

Inside the new shell, change the isolated hostname and then exit:

```bash
hostname lab-workshop
hostname
exit
```

`--user --map-root-user` creates a user namespace mapping the current user as root inside it. `--uts` creates a hostname namespace. `--fork` runs the program as a child. Availability depends on kernel and system policy.

### `nsenter` — Enter an Existing Process Namespace

```bash
sudo nsenter --target PID --mount --uts --ipc --net --pid bash
```

`--target` selects a process, and the other options enter its namespaces. This is a powerful diagnostic technique. Use only on authorised workloads and leave with `exit`.

### Inspect Cgroups

```bash
systemd-cgls
systemd-cgtop
```

`systemd-cgls` shows the cgroup hierarchy. `systemd-cgtop` provides a live resource view by control group. Container runtimes and systemd commonly place workloads into this hierarchy.

## 💡 Caveman Tip

When debugging a container, ask four questions: which image created it, which namespaces it sees, which cgroup limits it, and where persistent data actually lives.

## ⚠️ Common Mistakes

- Calling a container a lightweight VM without explaining the shared kernel.
- Running container processes as root when it is unnecessary.
- Giving broad capabilities or privileged access.
- Storing durable data only in the writable container layer.
- Shipping secrets inside an image.
- Assuming a resource request is the same as an enforced limit.
- Entering production namespaces without authorisation or an audit trail.

## 🧪 Hands-on Lab

### Mission: Open an Isolated Workshop

Use a disposable Linux VM:

1. Record the namespaces of your current shell with `lsns -p $$`.
2. Start a new user and UTS namespace with `unshare`.
3. Change the hostname inside it and confirm the host hostname is unchanged.
4. Compare the namespace IDs inside and outside the isolated shell.
5. Inspect the system cgroup hierarchy.
6. Draw which components are isolated and which kernel is shared.
7. Exit the namespace and explain why no VM boot occurred.

## 📝 Quick Recap

```text
Image → container process
          ├── namespaces: what it can see
          ├── cgroups: resources it can use
          ├── capabilities: privileged actions it may perform
          └── shared host kernel
```

## 🧠 Interview Questions

1. Why is a Linux container not a complete virtual machine?
2. What do namespaces and cgroups each provide?
3. What is the difference between an image and a container?
4. Where should persistent container data live?
5. Why can a privileged container be dangerous?
6. What host dependency matters for GPU containers?

## 📚 What's Next

You now understand the Linux primitives. [04 — Docker](04-docker.md) turns them into a practical workflow for building and operating portable applications.
