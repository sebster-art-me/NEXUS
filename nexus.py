#!/usr/bin/env python3
"""
NEXUS - White Hat Hacking Toolkit
A comprehensive cybersecurity toolkit with 20+ tools for ethical hacking and penetration testing.
"""

import sys
import subprocess
import os
from typing import Dict, List, Callable

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ToolCategory:
    """Represents a category of security tools"""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tools: Dict[str, 'Tool'] = {}
    
    def add_tool(self, tool: 'Tool'):
        self.tools[tool.name] = tool

class Tool:
    """Represents a security tool"""
    def __init__(self, name: str, description: str, command: str, installed_check: str = None):
        self.name = name
        self.description = description
        self.command = command
        self.installed_check = installed_check or command.split()[0]
    
    def is_installed(self) -> bool:
        """Check if the tool is installed"""
        try:
            result = subprocess.run(
                ['which', self.installed_check],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def run(self, args: List[str] = None):
        """Execute the tool with given arguments"""
        if not self.is_installed():
            print(f"{Colors.FAIL}Error: {self.name} is not installed.{Colors.ENDC}")
            print(f"Install it using: sudo apt-get install {self.installed_check}")
            return
        
        cmd = self.command.split()
        if args:
            cmd.extend(args)
        
        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Tool interrupted by user{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}Error running {self.name}: {e}{Colors.ENDC}")

class NEXUS:
    """Main NEXUS toolkit class"""
    
    def __init__(self):
        self.categories: Dict[str, ToolCategory] = {}
        self._initialize_tools()
    
    def _initialize_tools(self):
        """Initialize all security tools organized by category"""
        
        # 1. RECONNAISSANCE TOOLS
        recon = ToolCategory("Reconnaissance", "Information gathering and network discovery")
        recon.add_tool(Tool("nmap", "Network exploration and security auditing", "nmap"))
        recon.add_tool(Tool("whois", "Query domain registration information", "whois"))
        recon.add_tool(Tool("dig", "DNS lookup utility", "dig"))
        recon.add_tool(Tool("host", "DNS lookup utility", "host"))
        recon.add_tool(Tool("traceroute", "Trace network path to destination", "traceroute"))
        recon.add_tool(Tool("netdiscover", "Active/passive ARP reconnaissance", "netdiscover"))
        self.categories["recon"] = recon
        
        # 2. VULNERABILITY SCANNING
        vuln_scan = ToolCategory("Vulnerability Scanning", "Identify security vulnerabilities")
        vuln_scan.add_tool(Tool("nikto", "Web server scanner", "nikto"))
        vuln_scan.add_tool(Tool("openvas", "Comprehensive vulnerability scanner", "openvas"))
        vuln_scan.add_tool(Tool("lynis", "Security auditing tool", "lynis"))
        self.categories["vulnscan"] = vuln_scan
        
        # 3. WEB APPLICATION TESTING
        web = ToolCategory("Web Application Testing", "Web security assessment tools")
        web.add_tool(Tool("sqlmap", "Automatic SQL injection tool", "sqlmap"))
        web.add_tool(Tool("dirb", "Web content scanner", "dirb"))
        web.add_tool(Tool("gobuster", "Directory/file & DNS busting tool", "gobuster"))
        web.add_tool(Tool("wpscan", "WordPress security scanner", "wpscan"))
        self.categories["web"] = web
        
        # 4. PASSWORD CRACKING
        password = ToolCategory("Password Cracking", "Password security testing")
        password.add_tool(Tool("john", "John the Ripper password cracker", "john"))
        password.add_tool(Tool("hashcat", "Advanced password recovery", "hashcat"))
        password.add_tool(Tool("hydra", "Network logon cracker", "hydra"))
        self.categories["password"] = password
        
        # 5. NETWORK ANALYSIS
        network = ToolCategory("Network Analysis", "Network traffic analysis and monitoring")
        network.add_tool(Tool("wireshark", "Network protocol analyzer", "wireshark"))
        network.add_tool(Tool("tcpdump", "Command-line packet analyzer", "tcpdump"))
        network.add_tool(Tool("ettercap", "Network sniffer/interceptor", "ettercap"))
        self.categories["network"] = network
        
        # 6. EXPLOITATION TOOLS
        exploit = ToolCategory("Exploitation", "Security testing and exploitation")
        exploit.add_tool(Tool("metasploit", "Penetration testing framework", "msfconsole"))
        exploit.add_tool(Tool("searchsploit", "Exploit database search", "searchsploit"))
        self.categories["exploit"] = exploit
        
        # 7. WIRELESS TESTING
        wireless = ToolCategory("Wireless Testing", "Wireless network security assessment")
        wireless.add_tool(Tool("aircrack-ng", "WiFi security auditing", "aircrack-ng"))
        wireless.add_tool(Tool("reaver", "WPS brute force attack", "reaver"))
        self.categories["wireless"] = wireless
        
        # 8. FORENSICS
        forensics = ToolCategory("Forensics", "Digital forensics and data recovery")
        forensics.add_tool(Tool("autopsy", "Digital forensics platform", "autopsy"))
        forensics.add_tool(Tool("binwalk", "Firmware analysis tool", "binwalk"))
        self.categories["forensics"] = forensics
    
    def display_banner(self):
        """Display NEXUS banner"""
        banner = f"""
{Colors.OKCYAN}╔═══════════════════════════════════════════════════════════════╗
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
╚═══════════════════════════════════════════════════════════════╝{Colors.ENDC}
        """
        print(banner)
    
    def list_categories(self):
        """List all tool categories"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}Available Tool Categories:{Colors.ENDC}\n")
        for idx, (key, category) in enumerate(self.categories.items(), 1):
            tool_count = len(category.tools)
            print(f"{Colors.OKGREEN}{idx}. {category.name}{Colors.ENDC} ({tool_count} tools)")
            print(f"   {Colors.OKCYAN}{category.description}{Colors.ENDC}")
        print()
    
    def list_tools(self, category_key: str = None):
        """List all tools or tools in a specific category"""
        if category_key:
            if category_key not in self.categories:
                print(f"{Colors.FAIL}Invalid category: {category_key}{Colors.ENDC}")
                return
            categories = {category_key: self.categories[category_key]}
        else:
            categories = self.categories
        
        total_tools = 0
        for key, category in categories.items():
            print(f"\n{Colors.BOLD}{Colors.HEADER}[{category.name}]{Colors.ENDC}")
            print(f"{Colors.OKCYAN}{category.description}{Colors.ENDC}\n")
            
            for tool_name, tool in category.tools.items():
                total_tools += 1
                status = f"{Colors.OKGREEN}✓{Colors.ENDC}" if tool.is_installed() else f"{Colors.FAIL}✗{Colors.ENDC}"
                print(f"  {status} {Colors.BOLD}{tool.name}{Colors.ENDC}")
                print(f"     {tool.description}")
            print()
        
        print(f"{Colors.BOLD}Total Tools: {total_tools}{Colors.ENDC}\n")
    
    def run_tool(self, tool_name: str, args: List[str] = None):
        """Run a specific tool"""
        for category in self.categories.values():
            if tool_name in category.tools:
                tool = category.tools[tool_name]
                print(f"\n{Colors.OKBLUE}Running {tool.name}...{Colors.ENDC}\n")
                tool.run(args)
                return
        
        print(f"{Colors.FAIL}Tool '{tool_name}' not found{Colors.ENDC}")
    
    def show_help(self):
        """Display help information"""
        help_text = f"""
{Colors.BOLD}{Colors.HEADER}NEXUS - White Hat Hacking Toolkit{Colors.ENDC}

{Colors.BOLD}Usage:{Colors.ENDC}
  python3 nexus.py [command] [options]

{Colors.BOLD}Commands:{Colors.ENDC}
  {Colors.OKGREEN}list{Colors.ENDC}                    List all available tools
  {Colors.OKGREEN}categories{Colors.ENDC}              Show all tool categories
  {Colors.OKGREEN}run <tool> [args]{Colors.ENDC}       Run a specific tool with optional arguments
  {Colors.OKGREEN}help{Colors.ENDC}                    Show this help message
  {Colors.OKGREEN}install-deps{Colors.ENDC}            Show installation commands for all tools

{Colors.BOLD}Examples:{Colors.ENDC}
  python3 nexus.py list
  python3 nexus.py categories
  python3 nexus.py run nmap -sV 192.168.1.1
  python3 nexus.py run sqlmap --help

{Colors.BOLD}Tool Categories:{Colors.ENDC}
  • Reconnaissance (6 tools)
  • Vulnerability Scanning (3 tools)
  • Web Application Testing (4 tools)
  • Password Cracking (3 tools)
  • Network Analysis (3 tools)
  • Exploitation (2 tools)
  • Wireless Testing (2 tools)
  • Forensics (2 tools)

{Colors.BOLD}Total: 25+ Security Tools{Colors.ENDC}

{Colors.WARNING}Warning: These tools are for authorized security testing only.
         Unauthorized access to computer systems is illegal.{Colors.ENDC}
        """
        print(help_text)
    
    def show_install_deps(self):
        """Show installation commands for all tools"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}Installation Commands:{Colors.ENDC}\n")
        
        all_tools = []
        for category in self.categories.values():
            for tool in category.tools.values():
                all_tools.append(tool.installed_check)
        
        print(f"{Colors.OKGREEN}Debian/Ubuntu/Kali Linux:{Colors.ENDC}")
        print(f"sudo apt-get update")
        print(f"sudo apt-get install -y {' '.join(all_tools)}")
        print()
        
        print(f"{Colors.OKGREEN}Arch Linux:{Colors.ENDC}")
        print(f"sudo pacman -Syu")
        print(f"sudo pacman -S {' '.join(all_tools)}")
        print()
        
        print(f"{Colors.WARNING}Note: Some tools may require additional repositories or manual installation.{Colors.ENDC}")
        print()

def main():
    """Main entry point"""
    nexus = NEXUS()
    nexus.display_banner()
    
    if len(sys.argv) < 2:
        nexus.show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "help" or command == "--help" or command == "-h":
        nexus.show_help()
    elif command == "list":
        nexus.list_tools()
    elif command == "categories":
        nexus.list_categories()
    elif command == "run":
        if len(sys.argv) < 3:
            print(f"{Colors.FAIL}Error: Please specify a tool to run{Colors.ENDC}")
            print(f"Usage: python3 nexus.py run <tool> [args]")
        else:
            tool_name = sys.argv[2]
            args = sys.argv[3:] if len(sys.argv) > 3 else None
            nexus.run_tool(tool_name, args)
    elif command == "install-deps":
        nexus.show_install_deps()
    else:
        print(f"{Colors.FAIL}Unknown command: {command}{Colors.ENDC}")
        nexus.show_help()

if __name__ == "__main__":
    main()
