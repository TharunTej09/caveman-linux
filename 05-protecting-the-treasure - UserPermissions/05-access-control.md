# 05 — Access Control

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain when an access control list is useful.
- View, add, modify, and remove ACL entries.
- Interpret the ACL mask and effective permissions.
- Explain how `umask` influences newly created files and directories.
- Design access using least privilege.

## 🏕️ Caveman Story

The treasure cave already has rules for its owner, team, and everyone else. Then one healer outside the assigned team needs temporary read access.

Changing the entire team would be too broad. Opening the cave to every visitor would be dangerous.

Chief Grog adds one special rule for that healer. The original locks remain, but the guard now checks an extra list before deciding.

This is an **Access Control List**, or ACL.

## 🖼️ Big Concept Illustration

![Chief Grog assigning different special access rules to individual workers](../images/05-protecting-the-treasure/access-control-hero.png)

```text
Requesting user
      ↓
Owner or named-user rule?
      ↓
Group or named-group rule? ──> ACL mask limits effective rights
      ↓
Others rule
      ↓
Allow or deny
```

```text
Basic model: owner | one group | others
ACL model:   basic model + named users + named groups
```

## 📖 Concept Explained Simply

Traditional permissions are simple and fast, but one owning group cannot express every real team arrangement. ACLs add specific user and group entries without changing the primary owner or opening access to everyone.

The **ACL mask** limits the effective permissions of named users, named groups, and the owning group. An entry may display `rwx` while the mask reduces what is actually effective.

`umask` solves a different problem. It removes permission bits from the application's requested default when a new file or directory is created.

```text
Requested creation mode
          minus masked bits
          ↓
Initial permissions
```

Common programs request up to `666` for files and `777` for directories; files do not normally begin executable. With `umask 022`, typical results are `644` files and `755` directories.

## 🌍 Real Linux Example

A project directory belongs to the `developers` group, but one external tester needs read and traverse access. An ACL can grant that user only the necessary rights without adding them permanently to the development group.

ACLs are useful for exceptions, but too many entries become difficult to reason about. If many users require the same access, a well-designed group is often clearer.

## 🛠️ Commands Introduced

ACL tools may be provided by an `acl` package and might not be installed on a minimal system. The filesystem must also support ACLs.

### `getfacl` — View Access Control Lists

```bash
getfacl project
```

Displays basic ownership entries, named ACL entries, the mask, and any default ACLs.

```bash
getfacl -p /srv/project
```

`-p` keeps the absolute path in the output instead of removing its leading slash.

### `setfacl` — Modify Access Control Lists

Grant or replace a named user's entry:

```bash
setfacl -m u:mira:rx project
```

`-m` modifies the ACL. `u:mira:rx` grants user `mira` read and execute/traverse access.

Grant a named group:

```bash
setfacl -m g:testers:r project/report.txt
```

Remove one named-user entry:

```bash
setfacl -x u:mira project
```

`-x` removes the specified ACL entry.

Create a default ACL for new children of a directory:

```bash
setfacl -d -m g:developers:rwx project
```

`-d` modifies the directory's **default ACL**. It affects newly created children, not existing contents.

Remove all extended access ACL entries while preserving basic mode entries:

```bash
setfacl -b project/report.txt
```

Use recursive ACL changes only after inspecting the tree; the same scope risk applies as with recursive ownership changes.

### `umask` — Control Initial Permissions

```bash
umask
```

Shows the current mask, often in octal form.

```bash
umask 027
```

For typical creation requests, masks group write and all permissions for others, commonly producing `640` files and `750` directories. This affects items created by the current shell and its child processes; it does not rewrite existing files.

```bash
umask -S
```

Shows the allowed initial permissions in symbolic form, which can be easier to read.

## 💡 Caveman Tip

Use groups for stable team access and ACLs for justified exceptions. After every ACL change, inspect the effective result—not only the entry you requested.

## ⚠️ Common Mistakes

- Using an ACL when a normal group would be simpler.
- Ignoring the ACL mask and misreading effective access.
- Expecting a default ACL to alter existing files.
- Confusing `umask` with a command that changes existing permissions.
- Granting directory read without execute/traverse when access to children is required.
- Applying recursive ACL changes without reviewing scope.

## 🧪 Hands-on Lab

### Mission: Protect the Chief's Treasure

Use a disposable VM with two pre-created practice users and one practice group. An instructor or lab setup should provision the accounts; account-creation utilities are intentionally outside this module's command set.

1. Create a `Treasure` practice directory with previously learned file tools.
2. Assign the intended owner and guardian group.
3. Give the owner full access, the group read/write/traverse access, and others no access.
4. Grant one extra practice user read/traverse access through an ACL.
5. Inspect the ACL and explain the effective permissions.
6. Remove that exceptional access and verify the result.
7. Set a restrictive `umask`, create a new practice file and directory, and compare their initial modes.
8. Restore the original `umask` before leaving the shell.

### Final Engineer Challenge

Design access for a company project:

- Developers need read/write access.
- A tester needs read-only access.
- Unrelated users need no access.
- New project files should not become public.

Choose where standard group permissions are sufficient, where an ACL is justified, and how you would verify each decision.

## 📝 Quick Recap

- ACLs add named-user and named-group rules.
- `getfacl` displays ACLs and effective access.
- `setfacl -m` grants or changes entries; `-x` removes one.
- Default ACLs affect newly created children.
- The ACL mask can limit effective rights.
- `umask` influences initial permissions, not existing files.

## 🧠 Interview Questions

1. When is an ACL preferable to changing the owning group?
2. What does the ACL mask control?
3. What is the difference between an access ACL and a default ACL?
4. Does `umask 022` set every new object directly to `755`?
5. Why should ACL results be checked with `getfacl`?
6. When is a group easier to maintain than several ACL entries?

## 📚 What's Next

You can now identify users, interpret permissions, change ownership, elevate safely, and apply special access rules. The treasure is protected—and you are ready to study the village workers: Linux processes and services.
