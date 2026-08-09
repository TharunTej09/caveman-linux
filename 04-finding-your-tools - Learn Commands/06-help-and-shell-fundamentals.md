# 06 — Help and Shell Fundamentals

## 🎯 Learning Objectives

- Find trustworthy local help instead of guessing syntax.
- Explain command lookup, quoting, expansion, variables, and exit status.
- Distinguish shell variables from exported environment variables.

## 🏕️ Caveman Story

Chief Grog's translator does more than repeat words. It consults the tool manual, expands agreed symbols, finds the correct tool rack, and reports whether a job succeeded.

The Linux **shell** does the same between your typed line and the program that eventually runs.

## 🖼️ Big Concept Illustration

```text
Typed line → Shell reads and expands it → Finds command in PATH
          → Starts command → Returns exit status
```

## 📖 Concept Explained Simply

The shell interprets special characters before starting most external programs. Spaces separate words; quotes control expansion; variables hold values; `$PATH` lists directories searched for commands; and an exit status communicates success or failure.

```bash
name="Chief Grog"        # one shell variable
echo "$name"            # double quotes expand variables safely
echo '$name'             # single quotes preserve literal text
export VILLAGE=stone     # child processes inherit exported variables
```

Use `type` to learn what a command name means in the current shell. It may be an alias, function, builtin, or executable file.

### Why Should I Care?

Quoting and exit-status mistakes can make a script target the wrong files or continue after a failure. Help and inspection tools let an engineer verify behaviour on the actual installed system.

## 🌍 Real Linux Example

A deployment script uses an environment variable for its environment name and checks a validation command's status before restarting a service. The shell controls both decisions.

## 🛠️ Commands Introduced

```bash
man ls                 # full local manual; / searches, q quits
ls --help              # short command-specific help
type cd                # identify how this shell resolves a name
command -v nginx       # print the command that would run
env                    # exported environment
export APP_ENV=lab     # export a value to child processes
history                # interactive command history
echo "$?"              # previous command's exit status
```

`0` conventionally means success; non-zero means some form of failure. Never expose passwords or tokens through command history or shared process arguments.

## 💡 Caveman Tip

When unsure, inspect in this order: `type NAME`, `NAME --help`, then `man NAME`.

## ⚠️ Common Mistakes

- Leaving variable expansions unquoted when values may contain spaces or wildcard characters.
- Adding untrusted directories such as `.` to the start of `$PATH`.
- Assuming every command supports identical options.
- Treating all non-zero exit statuses as the same failure.

## 🧪 Hands-on Lab

1. Compare `type cd`, `type ls`, and `command -v ls`.
2. Create `village="Stone Valley"` and print it with double quotes, single quotes, and no quotes. Explain the difference.
3. Run `true`, inspect `$?`, then run `false` and inspect it again.
4. Export `VILLAGE=lab`; verify it with `env | grep '^VILLAGE='`.
5. Use `man grep` to find the option for case-insensitive matching.

## 📝 Quick Recap

The shell parses your instruction, expands controlled symbols, locates a command through `$PATH`, starts it, and receives an exit status.

## 🧠 Interview Questions

1. What is the difference between single and double quotes?
2. What does `$PATH` control?
3. How does an environment variable differ from an unexported shell variable?
4. What normally does exit status `0` mean?

## 📚 What's Next

Learn to change configuration and scripts safely in [07 — Text Editors](07-text-editors.md).
