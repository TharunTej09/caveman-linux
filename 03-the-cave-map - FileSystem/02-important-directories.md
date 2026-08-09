# 02 — Important Linux Directories

## 🎯 Learning Objectives

- Explain the purpose of the major directories beneath `/`.
- Identify likely locations for user data, configuration, logs, programs, startup files, devices, and temporary data.
- Use `cd` only as a guided way to visit these locations.

## 🏕️ Caveman Story

Chief Grog gives every cave a job. Families have bedrooms, rules stay in a protected locker, changing records enter a warehouse, shared tools have a workshop, and the fire-starting equipment stays near the entrance.

The layout helps a villager predict where something belongs before searching the whole mountain.

## 🖼️ Big Concept Illustration

```text
                               /
       ┌──────┬─────┬─────┬─────┬─────┬──────┬─────┬─────┐
     home    etc   usr   var   opt   boot   dev   proc  tmp
      beds   rules tools stock extras start doors window basket
```

| Directory | Cave image | Main purpose |
| --- | --- | --- |
| `/home` | Bedrooms | Regular users' personal directories |
| `/etc` | Rules locker | System-wide configuration |
| `/usr` | Shared workshop | Most installed programs, libraries, and shared data |
| `/var` | Changing warehouse | Logs, queues, caches, and other changing data |
| `/opt` | Visiting trader's store | Optional or third-party applications |
| `/boot` | Fire-starting room | Files needed during boot |
| `/dev` | Device doors | Interfaces to disks, terminals, and devices |
| `/proc` | Magic window | Live virtual kernel and process information |
| `/tmp` | Temporary basket | Short-lived working files |

## 📖 Concept Explained Simply

Linux follows a broadly standard hierarchy so people and programs can predict locations. Exact contents vary by distribution.

`/dev` and `/proc` are especially important: much of their content is created dynamically and represents devices or live system state rather than ordinary stored files. `/tmp` is not durable; cleanup policies may remove its contents. `/root` is the privileged root user's home, while `/` is the top of everything.

### Why Should I Care?

During an incident, knowing that configuration is commonly under `/etc` and logs under `/var/log` immediately narrows the search. The same layout appears inside VMs, containers, cloud hosts, and AI servers.

## 🌍 Real Linux Example

An engineer investigating Nginx may inspect configuration below `/etc/nginx`, logs below `/var/log/nginx`, and packaged program files below `/usr`. An AI service may place vendor software in `/opt` and mount large models elsewhere in the same tree.

## 🛠️ Commands Introduced

This directory-tour lesson uses the basic form of one navigation command:

```bash
cd /etc
```

`cd` means **change directory**. Here it is used only to visit named system locations. Lesson 03 teaches special path forms; Chapter 04 teaches `cd` as part of complete command-line navigation.

## 💡 Caveman Tip

Learn a directory's responsibility, not a fixed list of every file it might contain.

## ⚠️ Common Mistakes

- Storing permanent data in `/tmp`.
- Editing files in `/boot`, `/dev`, or `/proc` without understanding their role.
- Confusing `/usr` with a specific user's home.
- Assuming every distribution places every application in exactly the same location.

## 🧪 Hands-on Lab

Use only `cd` during this guided tour:

```bash
cd /
cd /etc
cd /var
cd /home
cd /tmp
```

Before each move, predict the kind of data associated with the destination. Do not modify system content. Return to `/` when finished.

## 📝 Quick Recap

```text
People → /home        Rules → /etc       Programs → /usr
Changes → /var        Startup → /boot    Devices → /dev
Live state → /proc    Temporary → /tmp   Optional apps → /opt
```

## 🧠 Interview Questions

1. Why are `/etc` and `/var/log` important during troubleshooting?
2. How do `/dev` and `/proc` differ from ordinary storage?
3. Why should `/tmp` not hold permanent data?
4. What is the difference between `/`, `/root`, and `/home`?

## 📚 What's Next

Learn how Linux describes routes between these rooms in [03 — Linux Paths](03-paths.md).
