# 04 — Searching

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Search the live filesystem by name and type.
- Use a filename index for fast searches.
- Find matching text inside files.
- Discover how the shell resolves a command and where related files may live.

## 🏕️ Caveman Story

The storage cave has grown too large. Chief Grog knows the missing map exists, but he does not know which shelf holds it.

Sometimes he searches for an object by its name. Sometimes he opens many records and searches for a warning written inside them. Sometimes he asks where a particular tool is stored.

Those are three different questions, so they need different search tools.

## 🖼️ Big Concept Illustration

![Chief Grog searching a large storage cave for files and matching text](../images/04-finding-your-tools/searching-hero.png)

```text
What are you searching for?
          │
    ┌─────┼───────────┐
    │     │           │
  File  Text inside  Command
    │     │           │
 find  grep        which / whereis
```

```text
Need → Choose search area → Match → Verify result → Use
```

## 📖 Concept Explained Simply

Searching has two dimensions:

- **Where to search**: one directory, an entire tree, or a prebuilt index.
- **What to match**: a filename, file type, text pattern, or command name.

Start with the narrowest sensible location. Searching `/` can be slow and produce permission errors; searching an application directory is usually faster and more meaningful.

## 🌍 Real Linux Example

When a service configuration is missing, an engineer may search `/etc` for a filename. When a service returns errors, they may search its log directory for the word `error`. When documentation refers to a tool, they may check which executable the current shell will run.

## 🛠️ Commands Introduced

### `find` — Search the Live Filesystem

```bash
find /etc -name "nginx.conf"
```

Searches below `/etc` for an exact, case-sensitive name.

```bash
find /var/log -type f -name "*.log"
```

`-type f` restricts results to regular files. Quote wildcard patterns so the shell does not expand them before `find` receives them.

```bash
find /etc -type d -name "*.d"
```

`-type d` restricts results to directories.

### `locate` — Search a Filename Index

```bash
locate nginx.conf
```

Searches a system-maintained filename database and is often faster than `find`. Results can be stale if the index has not yet recorded recent changes, and the command may not be installed by default.

### `grep` — Search Text

```bash
grep "ERROR" application.log
```

Prints lines containing the exact pattern.

```bash
grep -i "error" application.log
```

`-i` ignores letter case.

```bash
grep -n "error" application.log
```

`-n` includes matching line numbers.

```bash
grep -r "listen" /etc/nginx
```

`-r` searches files recursively below a directory. Limit the directory to avoid slow, noisy searches.

### `which` — Show the Executable the Shell Would Use

```bash
which python
```

Searches the shell's command path and prints the matching executable. Aliases, functions, or built-ins may require shell-specific inspection beyond this introductory tool.

### `whereis` — Find Common Command-Related Locations

```bash
whereis nginx
```

Searches standard locations for a command's binary, source, and manual-page files. It answers a broader question than `which`.

## 💡 Caveman Tip

Search names with `find` or `locate`, search file contents with `grep`, and search for installed tools with `which` or `whereis`.

## ⚠️ Common Mistakes

- Searching the whole filesystem when a smaller directory is known.
- Forgetting quotes around `*.log` in a `find` pattern.
- Confusing a filename search with a content search.
- Assuming `locate` always knows about newly created files.
- Treating “no output” as a crash; it often means no match.
- Assuming `which` reports every alias, function, or shell built-in.

## 🧪 Hands-on Lab

### Mission: Find the Lost Village Map

Use your `LinuxToolsLab` practice tree where possible.

1. Search it for files named `food-list.txt`.
2. Search it for all regular files ending in `.txt`.
3. Search those records for a word you placed in them, ignoring case.
4. Repeat the content search with line numbers.
5. Compare a `locate` result with a live `find` result if `locate` is installed.
6. Identify the executable path of `grep`.
7. Ask `whereis` for the broader set of `grep` locations.

### Engineer Challenge

Find configuration files below `/etc`, log files below `/var/log`, and the executable used when you run `ls`. Explain why each search starts in a different place.

## 📝 Quick Recap

- `find` searches the current filesystem tree.
- `locate` searches a fast but potentially stale index.
- `grep` searches text inside files.
- `which` shows the executable found through the command path.
- `whereis` checks standard locations for related binary, source, and manual files.

## 🧠 Interview Questions

1. What is the difference between `find` and `locate`?
2. How do `find -type f` and `find -type d` differ?
3. What do `grep -i`, `grep -n`, and `grep -r` do?
4. Why should a wildcard given to `find -name` be quoted?
5. How do `which` and `whereis` answer different questions?

## 📚 What's Next

You can find the right records. Next, connect tools and control their data in [05 — Pipes and Redirection](05-pipes-and-redirection.md).
