# 08 — Shell Scripting

## 🎯 Learning Objectives

- Build a small Bash script with variables, arguments, conditions, loops, and functions.
- Use strict error handling and meaningful exit statuses.
- Validate a script before trusting it with important systems.

## 🏕️ Caveman Story

Chief Grog repeats the same morning checks until he writes a checklist that any trained guard can follow. A script is that executable checklist: repeatable, reviewable, and still dependent on good instructions.

## 🖼️ Big Concept Illustration

```text
Input → Validate → Decide → Repeat work → Report → Exit status
```

## 📖 Concept Explained Simply

A Bash script is a text file containing shell instructions. The shebang chooses the interpreter; positional parameters accept input; conditions branch; loops repeat; functions name reusable work.

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

target=${1:-/}
check_space() {
  df -h -- "$target"
}

if [[ -e "$target" ]]; then
  check_space
else
  printf 'Target not found: %s\n' "$target" >&2
  exit 1
fi
```

### Why Should I Care?

Automation makes correct work repeatable—and makes mistakes repeatable too. Validation, quoting, review, logs, and least privilege are part of scripting.

## 🌍 Real Linux Example

A health-check script tests a filesystem, service endpoint, and certificate expiry, then returns non-zero so a monitoring system can alert.

## 🛠️ Commands Introduced

```bash
bash script.sh /var       # run with an argument
bash -n script.sh         # syntax check without execution
chmod u+x script.sh       # allow direct execution
./script.sh /var
shellcheck script.sh      # static analysis when ShellCheck is installed
read -r answer            # safely read one line of input
```

Use `[[ ... ]]` for Bash conditions. Quote expansions such as `"$target"`; use `--` before path arguments where supported.

## 💡 Caveman Tip

Start by automating a process you can already perform and verify manually.

## ⚠️ Common Mistakes

- Parsing human-formatted command output when a stable machine-readable interface exists.
- Hiding errors or ignoring exit statuses.
- Embedding secrets in source code.
- Running an entire script as root when only one operation needs privilege.
- Testing destructive logic against real data.

## 🧪 Hands-on Lab

1. Save the example as `cave-health.sh`.
2. Run `bash -n` and ShellCheck if available.
3. Test it with `/`, your home directory, and a missing path.
4. Add a loop that checks every path supplied as an argument.
5. Record the exit status for successful and failed runs.

## 📝 Quick Recap

Good scripts accept input, validate assumptions, quote data, fail visibly, return useful statuses, and remain safe to test.

## 🧠 Interview Questions

1. What does a shebang do?
2. Why use `set -Eeuo pipefail`?
3. Why should variable expansions usually be quoted?
4. What is ShellCheck used for?

## 📚 What's Next

Control interactive work and schedule automation in [09 — Jobs and Scheduling](09-jobs-and-scheduling.md).
