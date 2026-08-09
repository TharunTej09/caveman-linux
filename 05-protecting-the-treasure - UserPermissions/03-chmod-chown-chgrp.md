# 03 — Changing Permissions and Ownership

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Change permissions using symbolic and numeric modes.
- Explain how octal values map to read, write, and execute.
- Change a file's owner and owning group.
- Apply recursive changes only after evaluating their scope.

## 🏕️ Caveman Story

A treasure chest has the wrong lock. Chief Grog must make three separate decisions:

- Change what the current owner, team, or visitors may do.
- Hand ownership of the chest to another villager.
- Assign the chest to another team.

Changing the lock is not the same as changing the owner. Linux uses a different tool for each job.

## 🖼️ Big Concept Illustration

![Chief Grog changing locks, transferring ownership, and assigning a group key](../images/05-protecting-the-treasure/ownership-and-permissions-hero.png)

```text
Change abilities → chmod
Change owner     → chown
Change group     → chgrp
```

```text
Audience:   u owner   g group   o others   a all
Action:     + add     - remove  = set exactly
Permission: r read    w write   x execute
```

## 📖 Concept Explained Simply

Permission and ownership are related but different metadata:

```text
Treasure
├── Owner: who possesses it
├── Group: which team is attached
└── Mode: what owner, group, and others may do
```

Learn symbolic mode first because it says what changes. Numeric mode sets all three permission classes at once.

| Permission | Value |
| --- | ---: |
| Read (`r`) | 4 |
| Write (`w`) | 2 |
| Execute (`x`) | 1 |

Add values within each class: `7 = rwx`, `6 = rw-`, `5 = r-x`, `4 = r--`, and `0 = ---`.

## 🌍 Real Linux Example

A production deployment may make a script executable, assign it to the deployment account and application group, and prevent unrelated users from accessing it.

```text
Correct owner + correct group + least permission = controlled deployment
```

Broad recursive changes can break applications or expose secrets. Engineers inspect the target and use the smallest change that solves the requirement.

## 🛠️ Commands Introduced

### `chmod` — Change Permission Mode

Symbolic examples:

```bash
chmod +x deploy.sh
```

Adds execute permission according to the current `umask`-aware symbolic behavior when no audience is supplied. Prefer an explicit audience when precision matters:

```bash
chmod u+x deploy.sh
chmod g+w shared.txt
chmod o-r private.txt
chmod a-w published.txt
chmod u=rw,g=r,o= private.txt
```

`u`, `g`, `o`, and `a` choose the audience. `+`, `-`, and `=` add, remove, or replace its permissions.

Numeric examples:

```bash
chmod 755 deploy.sh
```

Sets `rwxr-xr-x`: owner gets `7`, group `5`, others `5`.

```bash
chmod 644 report.txt
```

Sets `rw-r--r--`: owner gets `6`, group `4`, others `4`.

```bash
chmod -R g+rX project
```

`-R` applies recursively. Uppercase `X` adds execute only to directories and to files that already have execute for someone, making it safer than blindly adding `x` to every file.

### `chown` — Change Owner

```bash
chown grog report.txt
```

Changes the owning user. This usually requires administrative privilege.

```bash
chown grog:hunters report.txt
```

Changes owner and group together.

```bash
chown -R grog:hunters project
```

Changes ownership throughout a directory tree. Inspect the tree first; recursive ownership mistakes can stop services from working.

### `chgrp` — Change Owning Group

```bash
chgrp developers report.txt
```

Changes only the owning group.

```bash
chgrp -R developers project
```

Changes the group recursively. A regular user can generally assign a file only to a group they belong to.

## 💡 Caveman Tip

Describe the desired result in words before choosing syntax: “Owner may read and write; group may read; others receive nothing.” Then express it symbolically or numerically.

## ⚠️ Common Mistakes

- Using `777` to bypass understanding.
- Confusing `chmod` with `chown`.
- Forgetting that numeric mode replaces all three class modes.
- Running `-R` from the wrong location or on a symbolic link-sensitive tree.
- Adding execute to ordinary data files.
- Changing application ownership without knowing which service account needs it.

## 🧪 Hands-on Lab

### Mission: Replace the Treasure Locks

Use disposable files in a practice directory.

1. Create a file named `private-note.txt` using a previously learned tool.
2. Inspect its current mode and ownership.
3. Set owner read/write, group read, and no access for others using symbolic mode.
4. Set the same result with numeric mode and explain why it is `640`.
5. Make a practice script executable for its owner only.
6. If your lab account has permission, assign a group you belong to.
7. Inspect every result before and after the change.

Do not change ownership on system files. Ownership exercises requiring another user should be performed in a disposable VM under instructor guidance.

### Engineer Challenge

Predict the final mode after `chmod u=rw,g=r,o= private-note.txt`. Then explain why `chmod 640` produces the same basic permissions.

## 📝 Quick Recap

- `chmod` changes permissions.
- Symbolic mode expresses a targeted change.
- Numeric mode uses `r=4`, `w=2`, and `x=1` for each class.
- `chown` changes the owner and can also change the group.
- `chgrp` changes only the group.
- Recursive changes require careful scope checks.

## 🧠 Interview Questions

1. What is the difference between `chmod`, `chown`, and `chgrp`?
2. What permissions does `750` represent?
3. Why is symbolic mode useful?
4. What is the difference between lowercase `x` and uppercase `X` in recursive changes?
5. Why can a recursive ownership change break a service?

## 📚 What's Next

Some ownership changes require administrative power. Learn how to use that power responsibly in [04 — Root and Sudo](04-root-and-sudo.md).
