# NEXUS Security Tools Reference

This document provides detailed information about each security tool included in the NEXUS toolkit.

## Table of Contents

1. [Reconnaissance Tools](#reconnaissance-tools)
2. [Vulnerability Scanning](#vulnerability-scanning)
3. [Web Application Testing](#web-application-testing)
4. [Password Cracking](#password-cracking)
5. [Network Analysis](#network-analysis)
6. [Exploitation Tools](#exploitation-tools)
7. [Wireless Testing](#wireless-testing)
8. [Forensics](#forensics)

---

## Reconnaissance Tools

### 1. Nmap (Network Mapper)
**Purpose:** Network exploration and security auditing

**Common Usage:**
```bash
# Basic scan
python3 nexus.py run nmap 192.168.1.1

# Version detection
python3 nexus.py run nmap -sV 192.168.1.0/24

# OS detection
python3 nexus.py run nmap -O 192.168.1.1

# Aggressive scan
python3 nexus.py run nmap -A 192.168.1.1
```

**What it does:** Discovers hosts and services on a computer network by sending packets and analyzing responses.

### 2. Whois
**Purpose:** Query domain registration information

**Common Usage:**
```bash
# Look up domain
python3 nexus.py run whois example.com

# Look up IP address
python3 nexus.py run whois 8.8.8.8
```

**What it does:** Retrieves domain registration details including registrar, creation date, and contact information.

### 3. Dig (Domain Information Groper)
**Purpose:** DNS lookup utility

**Common Usage:**
```bash
# Basic DNS lookup
python3 nexus.py run dig example.com

# Query specific record type
python3 nexus.py run dig example.com MX

# Reverse DNS lookup
python3 nexus.py run dig -x 8.8.8.8
```

**What it does:** Queries DNS servers for information about host addresses, mail exchanges, and other DNS records.

### 4. Host
**Purpose:** DNS lookup utility

**Common Usage:**
```bash
# Simple lookup
python3 nexus.py run host example.com

# Reverse lookup
python3 nexus.py run host 8.8.8.8
```

**What it does:** Performs DNS lookups and converts names to IP addresses and vice versa.

### 5. Traceroute
**Purpose:** Trace network path to destination

**Common Usage:**
```bash
# Trace route
python3 nexus.py run traceroute google.com

# Use ICMP instead of UDP
python3 nexus.py run traceroute -I google.com
```

**What it does:** Displays the route and measures transit delays of packets across a network.

### 6. Netdiscover
**Purpose:** Active/passive ARP reconnaissance

**Common Usage:**
```bash
# Passive scan
python3 nexus.py run netdiscover -p

# Active scan on specific range
python3 nexus.py run netdiscover -r 192.168.1.0/24
```

**What it does:** Discovers live hosts on a network by monitoring ARP traffic or sending ARP requests.

---

## Vulnerability Scanning

### 7. Nikto
**Purpose:** Web server scanner

**Common Usage:**
```bash
# Scan a web server
python3 nexus.py run nikto -h http://example.com

# Scan specific port
python3 nexus.py run nikto -h example.com -p 8080

# Output to file
python3 nexus.py run nikto -h example.com -o results.txt
```

**What it does:** Scans web servers for dangerous files, outdated versions, and specific problems.

### 8. OpenVAS
**Purpose:** Comprehensive vulnerability scanner

**Common Usage:**
```bash
# Start OpenVAS
python3 nexus.py run openvas
```

**What it does:** Full-featured vulnerability scanner that maintains a database of known vulnerabilities.

### 9. Lynis
**Purpose:** Security auditing tool

**Common Usage:**
```bash
# System audit
python3 nexus.py run lynis audit system

# Quick scan
python3 nexus.py run lynis audit system --quick
```

**What it does:** Performs security audits, compliance testing, and system hardening checks.

---

## Web Application Testing

### 10. SQLMap
**Purpose:** Automatic SQL injection tool

**Common Usage:**
```bash
# Test URL parameter
python3 nexus.py run sqlmap -u "http://example.com/page?id=1"

# Test with POST data
python3 nexus.py run sqlmap -u "http://example.com/login" --data="user=admin&pass=test"

# Enumerate databases
python3 nexus.py run sqlmap -u "http://example.com/page?id=1" --dbs
```

**What it does:** Detects and exploits SQL injection vulnerabilities in web applications.

### 11. Dirb
**Purpose:** Web content scanner

**Common Usage:**
```bash
# Basic directory scan
python3 nexus.py run dirb http://example.com

# Use custom wordlist
python3 nexus.py run dirb http://example.com /path/to/wordlist.txt

# Scan specific extensions
python3 nexus.py run dirb http://example.com -X .php,.html
```

**What it does:** Discovers hidden files and directories on web servers by dictionary-based attacks.

### 12. Gobuster
**Purpose:** Directory/file & DNS busting tool

**Common Usage:**
```bash
# Directory busting
python3 nexus.py run gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt

# DNS subdomain enumeration
python3 nexus.py run gobuster dns -d example.com -w subdomains.txt
```

**What it does:** Brute forces URIs, DNS subdomains, and virtual host names.

### 13. WPScan
**Purpose:** WordPress security scanner

**Common Usage:**
```bash
# Basic scan
python3 nexus.py run wpscan --url http://example.com

# Enumerate users
python3 nexus.py run wpscan --url http://example.com --enumerate u

# Enumerate plugins
python3 nexus.py run wpscan --url http://example.com --enumerate p
```

**What it does:** Scans WordPress websites for security vulnerabilities and misconfigurations.

---

## Password Cracking

### 14. John the Ripper
**Purpose:** Password cracker

**Common Usage:**
```bash
# Crack password hashes
python3 nexus.py run john hashes.txt

# Use wordlist
python3 nexus.py run john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Show cracked passwords
python3 nexus.py run john --show hashes.txt
```

**What it does:** Detects weak passwords by trying various cracking methods.

### 15. Hashcat
**Purpose:** Advanced password recovery

**Common Usage:**
```bash
# Dictionary attack
python3 nexus.py run hashcat -m 0 -a 0 hashes.txt wordlist.txt

# Brute force
python3 nexus.py run hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a
```

**What it does:** GPU-accelerated password cracking tool supporting many hash types.

### 16. Hydra
**Purpose:** Network logon cracker

**Common Usage:**
```bash
# SSH brute force
python3 nexus.py run hydra -l admin -P passwords.txt ssh://192.168.1.1

# HTTP form brute force
python3 nexus.py run hydra -l admin -P passwords.txt example.com http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"
```

**What it does:** Performs brute force attacks against various network protocols.

---

## Network Analysis

### 17. Wireshark
**Purpose:** Network protocol analyzer

**Common Usage:**
```bash
# Launch Wireshark GUI
python3 nexus.py run wireshark

# Capture on specific interface
python3 nexus.py run wireshark -i eth0
```

**What it does:** Captures and analyzes network traffic in real-time with detailed protocol information.

### 18. tcpdump
**Purpose:** Command-line packet analyzer

**Common Usage:**
```bash
# Capture all traffic
python3 nexus.py run tcpdump -i eth0

# Capture to file
python3 nexus.py run tcpdump -i eth0 -w capture.pcap

# Filter specific port
python3 nexus.py run tcpdump -i eth0 port 80
```

**What it does:** Captures network packets from the command line for analysis.

### 19. Ettercap
**Purpose:** Network sniffer/interceptor

**Common Usage:**
```bash
# Text mode
python3 nexus.py run ettercap -T

# ARP poisoning
python3 nexus.py run ettercap -T -M arp:remote /target_ip/ /gateway_ip/
```

**What it does:** Performs man-in-the-middle attacks and network sniffing.

---

## Exploitation Tools

### 20. Metasploit Framework
**Purpose:** Penetration testing framework

**Common Usage:**
```bash
# Launch Metasploit console
python3 nexus.py run metasploit
```

**What it does:** Comprehensive framework for developing and executing exploit code against remote targets.

### 21. SearchSploit
**Purpose:** Exploit database search

**Common Usage:**
```bash
# Search for exploits
python3 nexus.py run searchsploit apache

# Copy exploit to current directory
python3 nexus.py run searchsploit -m 12345
```

**What it does:** Command-line search tool for Exploit-DB database.

---

## Wireless Testing

### 22. Aircrack-ng
**Purpose:** WiFi security auditing

**Common Usage:**
```bash
# Crack WPA/WPA2
python3 nexus.py run aircrack-ng -w wordlist.txt capture.cap

# Monitor mode
python3 nexus.py run aircrack-ng --help
```

**What it does:** Suite of tools for assessing WiFi network security.

### 23. Reaver
**Purpose:** WPS brute force attack

**Common Usage:**
```bash
# Attack WPS
python3 nexus.py run reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv
```

**What it does:** Brute forces WPS PINs to recover WPA/WPA2 passphrases.

---

## Forensics

### 24. Autopsy
**Purpose:** Digital forensics platform

**Common Usage:**
```bash
# Launch Autopsy
python3 nexus.py run autopsy
```

**What it does:** Graphical interface for The Sleuth Kit and other forensic tools.

### 25. Binwalk
**Purpose:** Firmware analysis tool

**Common Usage:**
```bash
# Analyze firmware
python3 nexus.py run binwalk firmware.bin

# Extract files
python3 nexus.py run binwalk -e firmware.bin
```

**What it does:** Searches binary images for embedded files and executable code.

---

## Legal and Ethical Usage

**IMPORTANT:** All these tools must be used ethically and legally:

✅ **Authorized Use:**
- Testing your own systems
- Authorized penetration testing with written permission
- Educational purposes in controlled environments
- Security research with proper disclosure

❌ **Unauthorized Use:**
- Accessing systems without permission
- Causing damage or disruption
- Stealing data or credentials
- Any activity violating laws or regulations

**Remember:** Unauthorized access to computer systems is illegal in most jurisdictions and can result in criminal prosecution.

---

## Additional Resources

- [Kali Linux Documentation](https://www.kali.org/docs/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Offensive Security Training](https://www.offensive-security.com/)
