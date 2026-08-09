# Filesystem and Storage Cheatsheet

## Important Places

| Path | Purpose |
| --- | --- |
| `/` | root of the entire directory tree |
| `/home` | regular users' home directories |
| `/etc` | system and service configuration |
| `/var` | changing data such as logs and queues |
| `/usr` | installed programs, libraries, and shared data |
| `/tmp` | temporary data; not durable storage |
| `/boot` | bootloader and kernel-related files |
| `/dev` | device interfaces |
| `/proc` | live kernel and process view |

## Paths

```text
/etc/ssh/sshd_config   absolute: begins at /
./script.sh            relative: current directory
../archive             relative: parent directory
~/notes                relative to your home
```

## Capacity and Mounts

| Need | Command |
| --- | --- |
| Block devices and filesystems | `lsblk -f` |
| Mounted filesystem capacity | `df -hT` |
| Directory usage | `du -sh PATH` |
| Current mounts | `findmnt` |
| Persistent mount configuration | `cat /etc/fstab` |

Mounting connects a filesystem to a directory called a mount point. Verify device names, filesystem type, mount point, and backup before changing storage.
