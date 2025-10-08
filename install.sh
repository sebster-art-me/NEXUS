#!/bin/bash

# NEXUS Installation Script
# Installs all security tools for the NEXUS toolkit

set -e

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║   NEXUS White Hat Hacking Toolkit - Installation             ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "Cannot detect operating system. Please install tools manually."
    exit 1
fi

echo "Detected OS: $OS"
echo ""

# Function to install on Debian/Ubuntu/Kali
install_debian() {
    echo "Installing tools for Debian/Ubuntu/Kali Linux..."
    sudo apt-get update
    
    # Core tools that are usually available
    sudo apt-get install -y \
        nmap \
        whois \
        dnsutils \
        traceroute \
        tcpdump \
        john \
        hydra \
        aircrack-ng \
        binwalk \
        sqlmap \
        nikto \
        dirb \
        lynis \
        wireshark \
        ettercap-text-only || true
    
    # Tools that might need additional repos
    echo "Some tools may require additional repositories or manual installation:"
    echo "  - metasploit-framework (may need msfconsole)"
    echo "  - gobuster"
    echo "  - wpscan"
    echo "  - hashcat"
    echo "  - openvas"
    echo "  - reaver"
    echo "  - autopsy"
    echo "  - netdiscover"
    
    echo ""
    echo "You can install these manually or from their official sources."
}

# Function to install on Arch Linux
install_arch() {
    echo "Installing tools for Arch Linux..."
    sudo pacman -Syu --noconfirm
    
    sudo pacman -S --noconfirm \
        nmap \
        whois \
        bind-tools \
        traceroute \
        tcpdump \
        john \
        hydra \
        aircrack-ng \
        binwalk \
        sqlmap \
        nikto \
        wireshark-cli \
        ettercap || true
    
    echo "Some tools may need to be installed from AUR:"
    echo "  - metasploit"
    echo "  - gobuster"
    echo "  - wpscan"
    echo "  - hashcat"
    echo "  - openvas"
    echo "  - reaver"
    echo "  - autopsy"
    echo "  - netdiscover"
}

# Install based on OS
case $OS in
    ubuntu|debian|kali)
        install_debian
        ;;
    arch|manjaro)
        install_arch
        ;;
    *)
        echo "Unsupported OS: $OS"
        echo "Please install tools manually using your package manager."
        exit 1
        ;;
esac

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║   Installation Complete!                                     ║"
echo "║                                                               ║"
echo "║   Run: python3 nexus.py list                                 ║"
echo "║   to see which tools are installed                           ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
