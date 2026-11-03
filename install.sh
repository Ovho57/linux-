#!/bin/bash

# Define colors for terminal output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}===================================================${NC}"
echo -e "${GREEN}   Kali Linux WSL Professional Installer (CLI)     ${NC}"
echo -e "${GREEN}===================================================${NC}"

# Check if the script is running as Administrator
# In a Windows CLI environment, checking for admin rights via bash can be tricky, 
# so we rely on the system commands to fail gracefully if not elevated.
echo -e "\n[*] Checking permissions..."
net session > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[+] Administrator privileges confirmed.${NC}"
else
    echo -e "${RED}[-] ERROR: Administrator privileges required.${NC}"
    echo -e "    Please run your terminal as Administrator and try again."
    exit 1
fi

echo -e "\n[*] Step 1: Installing/Updating WSL..."
# --no-distribution installs the core WSL without prompting for a distro immediately
wsl --install --no-distribution

if [ $? -eq 0 ] || [ $? -eq 1 ]; then
    # Code 1 usually means it's already installed and updated
    echo -e "${GREEN}[+] WSL is ready.${NC}"
else
    echo -e "${RED}[-] WSL installation encountered an issue.${NC}"
fi

echo -e "\n[*] Step 2: Downloading Kali Linux..."
wsl --install -d kali-linux

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}===================================================${NC}"
    echo -e "${GREEN}   SUCCESS: Kali Linux is installed!               ${NC}"
    echo -e "${GREEN}===================================================${NC}"
    echo -e "To launch Kali Linux, type the following command:"
    echo -e "   ${GREEN}wsl -d kali-linux${NC}"
    echo -e "\nOn first launch, you will be prompted to create a"
    echo -e "new UNIX username and password."
else
    echo -e "\n${RED}[-] ERROR: Kali Linux installation failed.${NC}"
    echo -e "    Ensure virtualization is enabled in your BIOS/UEFI."
fi
