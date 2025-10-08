# NEXUS Quick Start Guide

## Installation

```bash
# Clone repository
git clone https://github.com/sebster-art-me/NEXUS.git
cd NEXUS

# Install tools (automated)
chmod +x install.sh
sudo ./install.sh

# OR install manually
python3 nexus.py install-deps
```

## Basic Commands

```bash
# Show help
python3 nexus.py help

# List all tools
python3 nexus.py list

# Show categories
python3 nexus.py categories

# Run a tool
python3 nexus.py run <tool> [arguments]
```

## Quick Examples

### Reconnaissance
```bash
# Network scan
python3 nexus.py run nmap -sV 192.168.1.0/24

# Domain lookup
python3 nexus.py run whois example.com
python3 nexus.py run dig example.com
```

### Web Testing
```bash
# SQL injection test
python3 nexus.py run sqlmap -u "http://example.com/page?id=1" --batch

# Directory scan
python3 nexus.py run dirb http://example.com

# WordPress scan
python3 nexus.py run wpscan --url http://example.com
```

### Vulnerability Scanning
```bash
# Web server scan
python3 nexus.py run nikto -h example.com

# System audit
python3 nexus.py run lynis audit system
```

### Network Analysis
```bash
# Capture packets
python3 nexus.py run tcpdump -i eth0

# Launch Wireshark
python3 nexus.py run wireshark
```

### Password Testing
```bash
# Crack hashes
python3 nexus.py run john hashes.txt

# Brute force SSH
python3 nexus.py run hydra -l admin -P passwords.txt ssh://192.168.1.1
```

## Tool Categories

1. **Reconnaissance** (6 tools) - Network discovery
2. **Vulnerability Scanning** (3 tools) - Find security holes
3. **Web Application Testing** (4 tools) - Web security
4. **Password Cracking** (3 tools) - Password testing
5. **Network Analysis** (3 tools) - Traffic analysis
6. **Exploitation** (2 tools) - Penetration testing
7. **Wireless Testing** (2 tools) - WiFi security
8. **Forensics** (2 tools) - Digital forensics

**Total: 25 Security Tools**

## Legal Notice

⚠️ **AUTHORIZED USE ONLY**

Only use these tools on systems you own or have explicit permission to test.
Unauthorized access is illegal and unethical.

## Getting Help

For detailed tool documentation, see `TOOLS.md`
For full documentation, see `README.md`
