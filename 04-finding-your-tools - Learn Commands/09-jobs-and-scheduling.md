# 09 — Job Control and Scheduling

## 🎯 Learning Objectives

- Distinguish foreground jobs, background jobs, processes, and scheduled tasks.
- Pause, resume, foreground, and safely detach interactive work.
- Choose between cron and systemd timers.

## 🏕️ Caveman Story

Some workers need Chief Grog's attention now; others can work behind the cave. Night guards must begin at a known time even when the Chief is asleep. Job control organises today's workers; scheduling assigns future shifts.

## 🖼️ Big Concept Illustration

```text
Terminal now: foreground ↔ stopped ↔ background
Future work: schedule → service starts → result is logged
```

## 📖 Concept Explained Simply

A shell job belongs to the current shell session. `Ctrl+Z` stops the foreground job; `bg` continues it in the background; `fg` brings it back. A trailing `&` starts a background job. `nohup` can protect simple work from terminal hangup, but a service manager is better for durable production workloads.

Cron expresses calendar schedules compactly. A systemd timer activates a service unit and provides dependency handling and journal logs.

### Why Should I Care?

Backups, cleanup, certificate renewal, and reports must run predictably even when no engineer is logged in—and failures must be visible.

## 🌍 Real Linux Example

A systemd timer runs a backup service nightly. The service has explicit credentials and limits; the timer's last and next runs are visible; the journal records success or failure.

## 🛠️ Commands Introduced

```bash
jobs -l                         # jobs in this shell
command &                       # start in background
bg %1                           # continue job 1 in background
fg %1                           # foreground job 1
nohup command >job.log 2>&1 &   # simple detached work
crontab -e                      # edit current user's cron table
crontab -l                      # list it
systemctl list-timers --all     # systemd timers
systemd-run --user --on-active=2m /path/to/script.sh
```

Cron fields are `minute hour day-of-month month day-of-week command`. Use absolute paths and redirect output intentionally because cron has a small environment.

## 💡 Caveman Tip

Schedule the command only after it works manually with the same user, paths, environment, and permissions.

## ⚠️ Common Mistakes

- Assuming `&` makes work survive logout.
- Scheduling relative paths or relying on an interactive `$PATH`.
- Overlapping long-running jobs without locking or idempotency.
- Creating a schedule without monitoring its result.

## 🧪 Hands-on Lab

1. Start `sleep 300`, stop it with `Ctrl+Z`, inspect `jobs -l`, resume with `bg`, and return it with `fg`.
2. End it with `Ctrl+C`.
3. Create a script that appends the date to `~/cave-timer.log`.
4. Schedule a one-time user task with `systemd-run --user --on-active=2m`.
5. Inspect `systemctl --user list-timers --all` and verify the log after it runs.

## 📝 Quick Recap

Job control manages work attached to one interactive shell. Cron and systemd timers start future work; production scheduling also needs logging, failure detection, overlap control, and safe retries.

## 🧠 Interview Questions

1. What is the difference between a process and a shell job?
2. How do `bg` and `fg` work?
3. Why might systemd timers be preferable to cron on a systemd host?
4. Why should scheduled tasks use absolute paths?

## 📚 What's Next

Your command toolkit is ready. Continue to [Chapter 05 — Protecting the Treasure](../05-protecting-the-treasure%20-%20UserPermissions/README.md).
