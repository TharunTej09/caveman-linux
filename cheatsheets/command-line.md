# Command-Line Cheatsheet

## Navigate and Inspect

| Need | Command | Useful form |
| --- | --- | --- |
| Current location | `pwd` | `pwd -P` resolves symbolic links |
| List entries | `ls` | `ls -lah` includes hidden entries and readable sizes |
| Change location | `cd` | `cd ..`, `cd ~`, `cd -` |
| Identify a command | `type NAME` | Shows alias, builtin, function, or executable |
| Read help | `man COMMAND` | Search inside with `/word`; quit with `q` |
| Short help | `COMMAND --help` | Usually lists syntax and common options |

## Files and Text

| Need | Command |
| --- | --- |
| Create file / directory | `touch FILE` / `mkdir -p DIR` |
| Copy / move | `cp SOURCE DEST` / `mv SOURCE DEST` |
| Read safely | `less FILE` |
| First / last lines | `head FILE` / `tail FILE` |
| Follow a growing log | `tail -f FILE` |
| Search text | `grep -n 'PATTERN' FILE` |
| Find files | `find PATH -type f -name 'PATTERN'` |

## Compose Commands

```bash
producer | consumer       # pass standard output as input
command > file            # replace file with output
command >> file           # append output
command 2> errors.log     # redirect errors
command | tee result.txt  # display and save
```

## Shell Essentials

```bash
echo "$HOME"              # quote expansions
printf '%s\n' "$PATH"     # inspect search path
export NAME=value         # child processes inherit it
echo "$?"                 # previous exit status: 0 normally means success
history                   # recent interactive commands
```

Never paste an unfamiliar command into a privileged shell. Read it left to right and identify every target first.
