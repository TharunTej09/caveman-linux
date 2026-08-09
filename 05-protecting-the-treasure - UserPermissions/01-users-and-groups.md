# 01 — Users and Groups

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain why Linux gives every user a numeric identity.
- Distinguish a user from a group.
- Identify your UID, primary GID, and supplementary groups.
- Check which users currently have login sessions.

## 🏕️ Caveman Story

Chief Grog knows every villager by name, but names alone are not enough. Two villagers could share a similar name, and rules must remain precise.

So the Chief gives each villager a unique clay identity token. He also organises villagers into teams: hunters, healers, and builders.

A villager has one main team and may help other teams. When someone approaches a protected cave, the guard checks the identity token and team membership before deciding which rule applies.

## 🖼️ Big Concept Illustration

![Chief Grog assigning identities and organising villagers into groups](../images/05-protecting-the-treasure/users-and-groups-hero.png)

```text
Village
├── Hunters
│   ├── Grog
│   └── Nala
├── Builders
│   └── Koda
└── Healers
    └── Mira
```

```text
User account
├── Username
├── UID                 unique user number
├── Primary GID         main group number
└── Supplementary GIDs  additional team memberships
```

## 📖 Concept Explained Simply

A **user** is an identity used by a person or a service. Linux makes access decisions using numeric user IDs (**UIDs**), even though humans normally work with usernames.

A **group** is a named collection of users. Groups let an administrator grant one rule to a team instead of configuring every member separately.

```text
Villager      → User
Clay token    → UID
Main team     → Primary group
Other teams   → Supplementary groups
```

System services often have their own accounts. This isolates them so a compromised service does not automatically inherit a human administrator's access.

## 🌍 Real Linux Example

A deployment engineer may belong to a `developers` group, while a web service runs as a separate account such as `www-data`. Both can be given only the access their roles require.

On a production incident, the first question is often not “Why is the file broken?” but “Which identity is the process using?”

## 🛠️ Commands Introduced

### `whoami` — Show the Effective User

```bash
whoami
```

Prints the username whose permissions the current shell is using. This matters after changing identity or using privileged access.

### `id` — Show Numeric Identity and Groups

```bash
id
```

Shows the current user's UID, primary GID, and all group memberships.

```bash
id username
```

Shows the same identity information for another known user.

### `groups` — Show Team Memberships

```bash
groups
```

Lists groups for the current user.

```bash
groups username
```

Lists groups for the named user. The first group shown is commonly the primary group, although `id` makes that relationship clearer.

### `users` — Show Users with Login Sessions

```bash
users
```

Prints usernames currently logged in. A name can appear more than once when the user has multiple sessions.

### `finger` — Show Human-Friendly Account Details

```bash
finger
```

Shows login information for current sessions.

```bash
finger username
```

Shows available details for one account. `finger` is optional and may not be installed on modern minimal servers.

## 💡 Caveman Tip

Use `id` when you need the complete identity picture: **who**, **primary group**, and **additional groups** in one result.

## ⚠️ Common Mistakes

- Assuming a username is the internal identity; Linux permission checks use UIDs and GIDs.
- Confusing the primary group with supplementary groups.
- Expecting new group membership to appear in an already-running login session.
- Assuming `users` lists every account; it lists active login sessions.
- Treating a missing `finger` command as a system failure.

## 🧪 Hands-on Lab

### Mission: Identify the Villager

1. Print your effective username.
2. Display your UID, primary GID, and all groups.
3. Print only the group membership view.
4. Check which users have active sessions.
5. If available, inspect your account with `finger`.
6. Write down which group is primary and which groups are supplementary.

### Engineer Challenge

Compare `whoami`, `id`, and `users`. Explain why their outputs answer three different questions even though all concern users.

## 📝 Quick Recap

- A user is a person or service identity.
- Linux identifies users and groups with UIDs and GIDs.
- Every user has one primary group and may have supplementary groups.
- `whoami`, `id`, `groups`, `users`, and `finger` answer different identity questions.

## 🧠 Interview Questions

1. What is the difference between a username and a UID?
2. What is the difference between a primary and supplementary group?
3. Why do services often run under dedicated user accounts?
4. Why can the same name appear more than once in `users` output?
5. Which command gives the most complete identity summary?

## 📚 What's Next

You know who the villagers are. Next, learn how Linux reads the locks protecting their treasure in [02 — Linux Permissions](02-linux-permissions.md).
