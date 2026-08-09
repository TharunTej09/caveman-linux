# 04 — Root and Sudo

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain why the `root` account is exceptionally powerful.
- Distinguish `sudo` from `su`.
- Inspect which privileged commands your account may run.
- Change passwords safely.
- Apply the principle of least privilege.

## 🏕️ Caveman Story

Chief Grog holds a master key that opens every village cave. The key is necessary for repairing gates and assigning ownership, but carrying it all day would turn one small mistake into a village-wide disaster.

Instead, a villager brings one approved task to the Chief. The Chief grants temporary authority for that task, records the decision, and the villager returns to normal work.

That is the idea behind `sudo`.

## 🖼️ Big Concept Illustration

![Chief Grog granting temporary authority for one protected task](../images/05-protecting-the-treasure/root-and-sudo-hero.png)

```text
Normal user
    ↓ requests approved task
sudo policy
    ↓ temporary privilege
Task runs
    ↓
Normal user continues
```

```text
root → UID 0 → unrestricted administrative identity
```

## 📖 Concept Explained Simply

`root` is the superuser account with UID `0`. It can read or alter almost any ordinary file, manage users, control services, and change system configuration.

Linux provides two common privilege paths:

| Method | Meaning | Typical use |
| --- | --- | --- |
| `sudo` | Run an authorised command as another user, normally root | Preferred for specific administrative tasks |
| `su` | Start a shell as another user | Identity switching and controlled troubleshooting |

`sudo` can be limited by policy and commonly leaves an audit trail. This supports **least privilege**: use only the access needed, only for as long as needed.

## 🌍 Real Linux Example

An engineer restarting a service should elevate only the restart or status task—not spend an entire work session as root.

```text
Need → approved command → authenticated elevation → logged action → normal work
```

Cloud environments often add another layer: a human identity first connects through an approved access system, then uses restricted `sudo` rules inside the VM.

## 🛠️ Commands Introduced

### `sudo` — Run an Authorised Command

```bash
sudo command
```

Runs one command with the identity allowed by the sudo policy, usually root. It commonly asks for **your** password, not the root password.

```bash
sudo -l
```

Lists the commands the current user is allowed—or forbidden—to run through `sudo`. This is a safe place to start.

```bash
sudo -i
```

Starts a root login-style shell. Use it only when several related administrative commands genuinely require it, and leave it immediately afterward. The prompt may change, but always verify your identity.

### `su` — Switch User

```bash
su username
```

Starts a shell as another user while generally retaining more of the current environment.

```bash
su - username
```

Starts a login shell for that user, loading an environment closer to a fresh login.

```bash
su -
```

Requests a root login shell and normally requires the root password. Many distributions lock direct root-password login and expect `sudo` instead.

### `passwd` — Change an Account Password

```bash
passwd
```

Changes the current user's password after verification.

```bash
sudo passwd username
```

An authorised administrator can set another user's password. Do not pass a password as a command-line argument; it can leak through history or process information.

## 💡 Caveman Tip

Before pressing Enter on a privileged command, ask: **What exact resource will change, and how will I verify it?**

## ⚠️ Common Mistakes

- Using `sudo` to silence a permission problem without understanding ownership.
- Remaining in a root shell longer than necessary.
- Assuming `sudo` and `su` are interchangeable.
- Forgetting that root can bypass protections that normally prevent accidents.
- Sharing passwords or placing them in scripts and shell history.
- Editing sudo policy directly without syntax validation and a recovery session.

## 🧪 Hands-on Lab

### Mission: Borrow the Chief's Authority

Use a disposable VM with an account intentionally configured for sudo access.

1. Record your normal identity with the identity tools from Lesson 01.
2. Inspect your allowed sudo rules with `sudo -l`.
3. Run one harmless, instructor-approved identity check through `sudo`.
4. Start a privileged login shell only if the lab permits it.
5. Verify that the effective identity changed to root.
6. Leave the privileged shell immediately and verify your normal identity.
7. Change only your own lab-account password if the environment permits it.

Do not change root or another user's password on a shared system.

### Engineer Challenge

Explain why `sudo` for one approved command is easier to audit and safer than performing an entire troubleshooting session in a root shell.

## 📝 Quick Recap

- Root is the UID `0` superuser.
- `sudo` provides policy-controlled elevation for commands.
- `sudo -l` shows permitted sudo actions.
- `su` changes the shell's user identity.
- `passwd` manages passwords interactively.
- Privilege should be temporary, minimal, and verifiable.

## 🧠 Interview Questions

1. What makes root different from a normal user?
2. What is the difference between `sudo command` and `sudo -i`?
3. How does `su - username` differ from `su username`?
4. Why is least privilege important?
5. Why should passwords never be passed on a command line?

## 📚 What's Next

Owner, group, and others handle most cases. When one extra villager needs a special rule, continue to [05 — Access Control](05-access-control.md).
