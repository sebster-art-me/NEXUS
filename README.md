# NEXUS - White Hat Hacking Toolkit

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗                ║
║   ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝                ║
║   ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗                ║
║   ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║                ║
║   ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║                ║
║   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                ║
║                                                               ║
║          White Hat Hacking Toolkit v1.0                      ║
║          Ethical Hacking & Penetration Testing               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

A comprehensive cybersecurity toolkit with 25+ professional tools for ethical hacking, penetration testing, and security research. Similar to Kali Linux and Arch Linux security distributions, NEXUS provides a unified interface to access and manage industry-standard security tools.

## 🚀 Features

- **25+ Security Tools** across 8 different categories
- **Unified Command-Line Interface** for all tools
- **Tool Installation Checker** to verify dependencies
- **Color-Coded Output** for better readability
- **Category-Based Organization** for easy navigation
- **Cross-Platform Support** (Linux, macOS, WSL)

## 📋 Tool Categories

### 1. Reconnaissance (6 tools)
Information gathering and network discovery:
- **nmap** - Network exploration and security auditing
- **whois** - Query domain registration information
- **dig** - DNS lookup utility
- **host** - DNS lookup utility
- **traceroute** - Trace network path to destination
- **netdiscover** - Active/passive ARP reconnaissance

### 2. Vulnerability Scanning (3 tools)
Identify security vulnerabilities:
- **nikto** - Web server scanner
- **openvas** - Comprehensive vulnerability scanner
- **lynis** - Security auditing tool

### 3. Web Application Testing (4 tools)
Web security assessment tools:
- **sqlmap** - Automatic SQL injection tool
- **dirb** - Web content scanner
- **gobuster** - Directory/file & DNS busting tool
- **wpscan** - WordPress security scanner

### 4. Password Cracking (3 tools)
Password security testing:
- **john** - John the Ripper password cracker
- **hashcat** - Advanced password recovery
- **hydra** - Network logon cracker

### 5. Network Analysis (3 tools)
Network traffic analysis and monitoring:
- **wireshark** - Network protocol analyzer
- **tcpdump** - Command-line packet analyzer
- **ettercap** - Network sniffer/interceptor

### 6. Exploitation (2 tools)
Security testing and exploitation:
- **metasploit** - Penetration testing framework
- **searchsploit** - Exploit database search

### 7. Wireless Testing (2 tools)
Wireless network security assessment:
- **aircrack-ng** - WiFi security auditing
- **reaver** - WPS brute force attack

### 8. Forensics (2 tools)
Digital forensics and data recovery:
- **autopsy** - Digital forensics platform
- **binwalk** - Firmware analysis tool

## 🔧 Installation

### Prerequisites
- Python 3.6 or higher
- Linux-based operating system (recommended: Kali Linux, Ubuntu, Arch Linux)

### Clone the Repository
```bash
git clone https://github.com/sebster-art-me/NEXUS.git
cd NEXUS
```

### Install Security Tools

#### Debian/Ubuntu/Kali Linux
```bash
sudo apt-get update
sudo apt-get install -y nmap whois dnsutils traceroute netdiscover \
    nikto openvas lynis sqlmap dirb gobuster wpscan john hashcat \
    hydra wireshark tcpdump ettercap-text-only metasploit-framework \
    exploitdb aircrack-ng reaver autopsy binwalk
```

#### Arch Linux
```bash
sudo pacman -Syu
sudo pacman -S nmap whois bind-tools traceroute netdiscover nikto \
    openvas lynis sqlmap dirb gobuster wpscan john hashcat hydra \
    wireshark-cli tcpdump ettercap metasploit aircrack-ng reaver \
    autopsy binwalk
```

Or use the built-in command:
```bash
python3 nexus.py install-deps
```

## 📖 Usage

### Basic Commands

#### Show Help
```bash
python3 nexus.py help
```

#### List All Available Tools
```bash
python3 nexus.py list
```

#### Show Tool Categories
```bash
python3 nexus.py categories
```

#### Run a Specific Tool
```bash
python3 nexus.py run <tool_name> [arguments]
```

### Examples

#### Reconnaissance
```bash
# Scan a network with nmap
python3 nexus.py run nmap -sV 192.168.1.0/24

# Query domain information
python3 nexus.py run whois example.com

# DNS lookup
python3 nexus.py run dig example.com

# Trace route to destination
python3 nexus.py run traceroute google.com
```

#### Web Application Testing
```bash
# Test for SQL injection
python3 nexus.py run sqlmap -u "http://example.com/page?id=1" --batch

# Directory brute forcing
python3 nexus.py run dirb http://example.com

# Scan WordPress site
python3 nexus.py run wpscan --url http://example.com
```

#### Vulnerability Scanning
```bash
# Scan web server
python3 nexus.py run nikto -h example.com

# System audit
python3 nexus.py run lynis audit system
```

#### Network Analysis
```bash
# Capture network traffic
python3 nexus.py run tcpdump -i eth0

# Launch Wireshark
python3 nexus.py run wireshark
```

#### Password Cracking
```bash
# Crack password hashes with John the Ripper
python3 nexus.py run john hashes.txt

# Brute force login
python3 nexus.py run hydra -l admin -P passwords.txt ssh://192.168.1.1
```

## ⚠️ Legal Disclaimer

**IMPORTANT: This toolkit is intended for AUTHORIZED SECURITY TESTING ONLY.**

- ✅ Use only on systems you own or have explicit written permission to test
- ✅ Conduct security research in controlled environments
- ✅ Follow responsible disclosure practices
- ❌ Unauthorized access to computer systems is ILLEGAL
- ❌ Using these tools without permission may result in criminal prosecution

By using NEXUS, you agree to use these tools ethically and legally. The developers of NEXUS are not responsible for any misuse or damage caused by this toolkit.

## 🛠️ Development

### Project Structure
```
NEXUS/
├── nexus.py          # Main toolkit script
└── README.md         # Documentation
```

### Adding New Tools

To add a new tool to NEXUS, edit `nexus.py` and add a new `Tool` object to the appropriate category:

```python
category.add_tool(Tool(
    name="tool_name",
    description="Tool description",
    command="command_to_run",
    installed_check="binary_name"
))
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational and authorized security testing purposes.

## 🌟 Acknowledgments

- Inspired by Kali Linux and other security-focused distributions
- Built on top of industry-standard open-source security tools
- Thanks to all the security researchers and tool developers

## 📧 Contact

For questions, suggestions, or security concerns, please open an issue on GitHub.

---

**Remember: With great power comes great responsibility. Use these tools ethically and legally.**