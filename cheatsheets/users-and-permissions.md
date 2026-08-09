# Users and Permissions Cheatsheet

## Identity

```bash
whoami                  # effective username
id                      # UID, primary GID, supplementary groups
groups USER             # group membership
getent passwd USER      # account database entry
getent group GROUP      # group database entry
```

## Read a Mode

```text
-rwxr-x---  owner  group  file
│└─┬┘└┬┘└┬┘
│  │   │  └─ others
│  │   └──── group
│  └──────── owner
└─────────── type (- file, d directory, l link)
```

`r=4`, `w=2`, `x=1`; therefore `750` means owner `rwx`, group `r-x`, others `---`.

## Change Access

```bash
chmod u+x script.sh              # symbolic mode
chmod 640 report.txt             # numeric mode
chown USER:GROUP file            # owner and group
chgrp GROUP file                 # group only
getfacl file                     # inspect ACL
setfacl -m u:USER:r-- file       # one-user exception
sudo -l                          # permitted sudo commands
```

Avoid `chmod 777`; grant the smallest access needed. Never run recursive ownership or mode changes until the target path is independently verified.
