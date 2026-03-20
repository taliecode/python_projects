# Python System Info

A lightweight script that prints useful information about your system straight to the terminal. No dependencies, just Python's standard library.

---

## Features

- Detects your OS and version
- Shows your machine's hostname and IP address
- Displays the number of CPU cores
- Shows disk usage — total, used, and free (in GB)
- Handles errors gracefully (e.g. if IP address can't be resolved)

## Getting Started

No installs needed. Just run:

```bash
python system_info.py
```

## Output

When you run the script you'll see something like this:

```
=== System Info ===
OS: <your OS and version>
Hostname: <your machine name>
IP Address: <your local IP>
CPU Count: <number of cores>
Disk Total: <total GB>
Disk Used:  <used GB>
Disk Free:  <free GB>
```

## Requirements

- Python 3

## Author

taliecode