# Linux Firewall Management Tool

A simple Python-based command-line tool for managing the Linux firewall (UFW) and packet filtering (iptables) through an interactive menu — no need to memorize `ufw`/`iptables` syntax.

## Features

- View current firewall status
- Enable / disable the firewall (UFW)
- List all active UFW rules and iptables INPUT chain rules
- Block or allow a specific IP address
- Block or allow a specific port
- Simple, menu-driven CLI — easy to use for quick firewall administration

## Requirements

- Linux (tested on Ubuntu)
- Python 3.x
- `ufw` installed and configured
- `iptables` installed
- `sudo` / root privileges (the script runs privileged commands)

## Installation

```bash
git clone https://github.com/aradhyat369/linux-firewall-manager.git
cd linux-firewall-manager
```

No external Python packages are required — the script only uses the standard library (`os`).

## Usage

Run the script with Python 3. Since it executes `sudo` commands, you'll be prompted for your password when a privileged action is run:

```bash
python3 linuxFirewall.py
```

You'll see a menu like this:

```
========== LINUX FIREWALL ==========
1. Firewall Status
2. Enable Firewall
3. Disable Firewall
4. List Rules
5. Block IP
6. Allow IP
7. Block Port
8. Allow Port
0. Exit
====================================
Enter choice:
```

Enter the number corresponding to the action you want to perform.

### Examples

- **Block an IP:** Choose option `5`, then enter the IP address (e.g. `192.168.1.10`) when prompted.
- **Allow a port:** Choose option `8`, then enter the port number (e.g. `8080`) when prompted.

## How It Works

The tool wraps two native Linux utilities:

- **UFW (Uncomplicated Firewall)** — used for high-level firewall status, enabling/disabling, and port rules.
- **iptables** — used directly for fine-grained IP blocking (`DROP` rule on the `INPUT` chain) alongside the corresponding UFW rule.

## Security Notes

- This script requires `sudo` privileges and directly modifies system firewall rules — use with caution, especially on production or remote servers (blocking the wrong IP/port could lock you out).
- User input (IP addresses, ports) is currently passed directly into shell commands. If you plan to extend this project, consider adding input validation (e.g. regex-checking IPs) and using `subprocess.run()` with argument lists instead of `os.system()` to reduce shell-injection risk.
- Always test in a safe/local environment (e.g. a VM) before running on a live system.

## Disclaimer

This is a personal/educational project for learning firewall administration and Python scripting. Use responsibly and only on systems you own or have explicit permission to manage.
