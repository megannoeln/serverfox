# Serverfox

Serverfox is a Python CLI tool for Linux server administration, monitoring, and operational workflows. In its current stage, it works on a local machine. In the near future, it will act as an ssh client for remote server management.

The project is intentionally small and iterative. Instead of trying to replace every Linux command, Serverfox focuses on useful summaries and checks that help answer common server questions quickly.

## Current commands

### `health`
Shows a system health snapshot, including:
- operating system
- hostname
- current user
- CPU usage
- load average
- memory usage
- disk usage
- uptime
- overall health status

usage: 

```bash
python3 main.py health
```

### `net`
Shows basic connectivity information, including:
- local IPv4 address
- whether the machine can reach the internet

usage: 

```bash
python3 main.py net
```

### `services`
Checks one or more systemd services and prints a simple status summary.

usage: 

```bash
python3 main.py services nginx sshd redis
```

### `logs`
Shows recent logs for a single service using `journalctl`.

usage: 

```bash
python3 main.py logs nginx
```

### `ports`
Shows listening TCP ports, including:
- local port
- local address
- process name when available

usage: 

```bash
python3 main.py ports
```

## Why I'm building this project

My idea for Serverfox came from a growing interest in server administration, infrastructure, and Linux, as well as a way to practice:
- Python fundamentals
- command-line application structure
- process and service inspection
- logs and observability basics


## Design approach

I'm building Serverfox with a few design goals in mind:
- keep commands small and focused
- prefer useful summaries over just cloning known Linux commands
- handle missing tools and permission issues gracefully
- keep the code readable and beginner-friendly


## Requirements

- Python 3
- `psutil`

If you are using a virtual environment:

```bash
source .venv/bin/activate
python3 main.py
```

## Current limitations

- Some commands depend on Linux tools such as `systemctl` and `journalctl`
- Some commands may require elevated permissions depending on the environment
- The project is Linux focused, even though some development work happened on macOS. 
- That being said, most commands will work on either OS but not all of them. 

## Roadmap

Planned areas for future development:
- ssh access
- deployment-oriented checks and helpers
- improved log filtering
- richer service inspection

## What I've learned so far building this

This project has helped me practice:
- Python imports, functions, and modules
- argument handling with `sys.argv`
- interacting with the OS and subprocesses of a machine
- handling errors and permission issues gracefully
- designing CLI commands around real operational use cases
- what kind of information is important for a server administrator to find out quickly
