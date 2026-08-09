# 07 — Text Editors: Nano and Vim

## 🎯 Learning Objectives

- Choose a beginner-friendly or production-available terminal editor.
- Open, change, save, search, and exit without losing work.
- Validate important configuration after editing.

## 🏕️ Caveman Story

The village rules are carved on tablets. Reading a tablet is not enough when the Chief must correct a gate rule. He needs a writing tool—and must know how to save or abandon a change.

## 🖼️ Big Concept Illustration

```text
Open → Understand current text → Edit → Review difference
     → Save → Validate → Apply
```

## 📖 Concept Explained Simply

`nano` is straightforward and displays common shortcuts. `vim` is modal: normal mode controls the editor, insert mode enters text, and command-line mode saves or exits. Learn one comfortably and know the survival keys for the other because minimal servers may provide only one.

### Why Should I Care?

Configuration is often plain text. A safe editor workflow prevents accidental truncation, malformed settings, and service outages.

## 🌍 Real Linux Example

An engineer copies a service configuration, edits one value, reviews the change, runs the service's validation command, and reloads only after validation succeeds.

## 🛠️ Commands Introduced

```bash
nano notes.txt
vim notes.txt
```

Nano essentials: `Ctrl+O` write, `Ctrl+W` search, `Ctrl+X` exit. The `^` shown in Nano means Ctrl.

Vim essentials: `i` insert, `Esc` normal mode, `/text` search, `:w` save, `:q` quit, `:wq` save and quit, `:q!` abandon unsaved changes.

## 💡 Caveman Tip

For system configuration, copy the file first and change one logical item at a time. Saving a file is not proof that its syntax is valid.

## ⚠️ Common Mistakes

- Editing a generated file instead of its source configuration.
- Using `:q!` and unintentionally discarding work.
- Restarting a service without validating its configuration.
- Editing production without a backup, review, or rollback path.

## 🧪 Hands-on Lab

1. Create `editor-lab.txt` with Nano; add three village rules, search for one, save, and exit.
2. Open the same file in Vim; use `i` to add a line, then save with `:wq`.
3. Open it again, make a temporary change, and abandon that change with `:q!`.
4. Read the file and confirm which changes remain.

## 📝 Quick Recap

Nano optimises for immediate discoverability. Vim optimises for powerful modal editing. A production edit ends with validation, not merely saving.

## 🧠 Interview Questions

1. Why is Vim described as modal?
2. How do you exit Vim without saving?
3. What should happen after editing a service configuration?

## 📚 What's Next

Turn command knowledge into a repeatable tool in [08 — Shell Scripting](08-shell-scripting.md).
