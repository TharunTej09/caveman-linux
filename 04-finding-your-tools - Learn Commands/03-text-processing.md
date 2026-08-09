# 03 — Text Processing

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Display short text and page through long files.
- Inspect the beginning or end of a file.
- Follow a growing log.
- Count, sort, and remove adjacent duplicate lines.

## 🏕️ Caveman Story

Chief Grog discovers ancient cave writings. One message fits on a small tablet, another fills a long scroll, and the village log grows every minute.

He does not read every record in the same way:

- A short tablet can be read all at once.
- A long scroll needs paging.
- A warning may be near the bottom.
- A changing watch log must be followed live.
- A supply list may need counting and sorting.

The question determines the reading tool.

## 🖼️ Big Concept Illustration

![Chief Grog reading tablets, scrolls, and village records](../images/04-finding-your-tools/text-processing-hero.png)

```text
Short text → Display everything
Long text  → Open and scroll
Start      → Read the first lines
End        → Read the last lines
Live log   → Follow new lines
List       → Count, sort, remove repeats
```

```text
Text file → Command → Useful view or transformed text
```

## 📖 Concept Explained Simply

Linux configuration, logs, scripts, and command output are commonly plain text. Text-processing tools usually read data and print a result; they do not modify the original file unless output is deliberately redirected.

Choose the smallest useful view. Displaying an enormous log in full is slower and harder to read than inspecting its last few lines or opening it in a pager.

## 🌍 Real Linux Example

During an incident, an engineer may inspect the last lines of a service log and then follow new entries while reproducing the problem. For a configuration file, a pager provides safe read-only inspection without opening an editor.

## 🛠️ Commands Introduced

### `cat` — Display or Combine Short Files

```bash
cat village-map.txt
```

Prints the complete file to standard output. It is best for short content.

```bash
cat part-one.txt part-two.txt
```

Prints files in the supplied order, effectively combining their output.

### `less` — Page Through Long Text

```bash
less /var/log/syslog
```

Opens a scrollable, read-only view. Common controls are `Space` for the next page, `b` for the previous page, `/word` to search forward, and `q` to quit. Some distributions use a different main system log path.

### `more` — Page Forward Through Text

```bash
more village-map.txt
```

Displays text one screen at a time. It is simpler and less flexible than `less`, but is common on minimal systems.

### `head` — Read the Beginning

```bash
head -n 10 village-map.txt
```

Shows the first 10 lines. `-n` sets the number of lines. The shorter `head -10` form is also widely supported.

### `tail` — Read or Follow the End

```bash
tail -n 10 village.log
```

Shows the last 10 lines.

```bash
tail -f village.log
```

`-f` keeps watching the file and prints new lines as they are appended. Press `Ctrl+C` to stop following.

### `wc` — Count Text

```bash
wc -l village.log
```

`-l` counts lines. Without options, `wc` reports lines, words, and bytes.

### `sort` — Sort Lines

```bash
sort villagers.txt
```

Prints lines in sorted order. It does not change the original file.

### `uniq` — Collapse Adjacent Duplicate Lines

```bash
uniq sorted-villagers.txt
```

Removes repeated lines only when identical lines are adjacent. This is why sorted input is commonly used before `uniq`; the connection is practised in Lesson 05.

## 💡 Caveman Tip

Do not pour an entire warehouse of records onto the floor. Use `head`, `tail`, or `less` to inspect only what you need.

## ⚠️ Common Mistakes

- Using `cat` on a huge file and flooding the terminal.
- Forgetting to quit `less` with `q`.
- Leaving `tail -f` running and thinking the prompt is frozen.
- Assuming `sort` edits the source file.
- Expecting `uniq` to remove duplicates scattered throughout unsorted input.

## 🧪 Hands-on Lab

### Mission: Read the Village Watch Log

Use a harmless text or log file available in your lab.

1. Display a short file with `cat`.
2. Open a longer file with `less`; search for a word and quit.
3. Read its first 10 lines with `head -n 10`.
4. Read its last 10 lines with `tail -n 10`.
5. Count its lines with `wc -l`.
6. Sort a list containing repeated names.
7. Observe that the original list remains unchanged after sorting.
8. Follow an actively changing practice log with `tail -f` if one is available; otherwise practise starting and stopping the command with `Ctrl+C`.

## 📝 Quick Recap

- `cat` displays short files.
- `less` and `more` page through text.
- `head` and `tail` inspect the beginning and end.
- `tail -f` follows a growing file.
- `wc -l` counts lines.
- `sort` orders lines; `uniq` collapses adjacent duplicates.

## 🧠 Interview Questions

1. Why is `less` usually better than `cat` for a large log?
2. How do you stop `tail -f`?
3. Does `sort` modify the input file?
4. Why is sorted input commonly given to `uniq`?
5. Which command would you use to count log lines?

## 📚 What's Next

You can read cave records. Next, learn how to locate files, content, and executables in [04 — Searching](04-searching.md).
