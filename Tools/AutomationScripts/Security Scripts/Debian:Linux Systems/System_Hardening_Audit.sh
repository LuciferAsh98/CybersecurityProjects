#!/bin/bash

# System Hardening Audit Script
# Enhanced CLI with Additional Hardening Checks

# Define Colors
GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
CYAN="\033[1;36m"
RESET="\033[0m"

# Function to print headers
function header() {
    echo -e "${CYAN}========================================${RESET}"
    echo -e "${BLUE}$1${RESET}"
    echo -e "${CYAN}========================================${RESET}"
}

# Function to print success
function success() {
    echo -e "${GREEN}[✔] $1${RESET}"
}

# Function to print warning
function warning() {
    echo -e "${YELLOW}[!] $1${RESET}"
}

# Function to print error
function error() {
    echo -e "${RED}[✘] $1${RESET}"
}

# Function to log output
LOG_FILE="system_audit.log"
function log_output() {
    echo "$1" >> $LOG_FILE
}

# Start Audit
header "System Hardening Audit - Enhanced"

# 1. Kernel Version Audit
header "Checking Kernel Version"
kernel_version=$(uname -r)
echo -e "${CYAN}Kernel Version:${RESET} $kernel_version"
log_output "Kernel Version: $kernel_version"
if [[ "$kernel_version" < "5.4" ]]; then
    warning "Kernel version is outdated. Consider upgrading to a newer version."
    log_output "Kernel version is outdated."
else
    success "Kernel version is up-to-date."
fi

# 2. Secure Boot Verification
header "Checking Secure Boot Status"
if [ -d /sys/firmware/efi ]; then
    success "Secure Boot is enabled."
    log_output "Secure Boot: Enabled"
else
    warning "Secure Boot is not enabled. Ensure your system firmware supports it."
    log_output "Secure Boot: Disabled"
fi

# 3. Disk Encryption Check
header "Checking Disk Encryption"
if lsblk -o NAME,FSTYPE,MOUNTPOINT | grep -q "crypt"; then
    success "Disk encryption is enabled."
    log_output "Disk Encryption: Enabled"
else
    warning "Disk encryption is not enabled. Consider using LUKS for full-disk encryption."
    log_output "Disk Encryption: Disabled"
fi

# 4. Password Policy Audit
header "Auditing Password Policy"
minlen=$(grep ^minlen /etc/security/pwquality.conf 2>/dev/null | awk '{print $3}')
if [[ -z "$minlen" || "$minlen" -lt 12 ]]; then
    warning "Weak password policy detected. Ensure minimum password length is at least 12."
    log_output "Password Policy: Weak (minlen=$minlen)"
else
    success "Password policy is strong (minlen=$minlen)."
    log_output "Password Policy: Strong (minlen=$minlen)"
fi

# 5. SELinux/AppArmor Status Check
header "Checking SELinux/AppArmor Status"
if command -v getenforce &>/dev/null; then
    selinux_status=$(getenforce)
    if [ "$selinux_status" = "Enforcing" ]; then
        success "SELinux is enabled and enforcing."
        log_output "SELinux: Enabled and Enforcing"
    else
        warning "SELinux is not enforcing. Consider setting it to 'Enforcing'."
        log_output "SELinux: Not Enforcing"
    fi
else
    if command -v aa-status &>/dev/null; then
        apparmor_status=$(aa-status --enabled 2>/dev/null)
        if [[ "$apparmor_status" == *"profiles are loaded"* ]]; then
            success "AppArmor is enabled."
            log_output "AppArmor: Enabled"
        else
            warning "AppArmor is not enabled."
            log_output "AppArmor: Not Enabled"
        fi
    else
        warning "Neither SELinux nor AppArmor is enabled. Consider enabling one for better security."
        log_output "SELinux/AppArmor: Not Enabled"
    fi
fi

# 6. Check for World-Writable Files
header "Checking for World-Writable Files"
world_writable_files=$(find / -xdev -type f -perm -0002 2>/dev/null)
if [ -n "$world_writable_files" ]; then
    warning "World-writable files found. Review the list below:"
    echo "$world_writable_files"
    log_output "World-Writable Files:\n$world_writable_files"
else
    success "No world-writable files found."
    log_output "World-Writable Files: None"
fi

# 7. Unnecessary SUID/SGID Binaries
header "Checking for Unnecessary SUID/SGID Binaries"
suid_files=$(find / -perm /6000 -type f -exec ls -l {} \; 2>/dev/null)
if [ -n "$suid_files" ]; then
    warning "SUID/SGID binaries found. Review the list below:"
    echo "$suid_files"
    log_output "SUID/SGID Binaries:\n$suid_files"
else
    success "No unnecessary SUID/SGID binaries found."
    log_output "SUID/SGID Binaries: None"
fi

# 8. Antivirus/Anti-Malware Presence
header "Checking for Antivirus/Anti-Malware"
if command -v clamscan &>/dev/null; then
    success "ClamAV is installed."
    log_output "Antivirus: ClamAV Installed"
else
    warning "Antivirus software not detected. Consider installing ClamAV or similar tools."
    log_output "Antivirus: Not Installed"
fi

# 9. Log Rotation Configuration
header "Checking Log Rotation Configuration"
if [ -f /etc/logrotate.conf ]; then
    success "Log rotation is configured."
    log_output "Log Rotation: Configured"
else
    warning "Log rotation is not configured. Consider setting it up to prevent log overflow."
    log_output "Log Rotation: Not Configured"
fi

# 10. Process Priority Checks
header "Checking Process Priorities for Critical Services"
processes=$(ps -eo pid,pri,comm --sort=-pri | head -10)
echo -e "${CYAN}Top 10 processes by priority:${RESET}"
echo "$processes"
log_output "Top Processes by Priority:\n$processes"

# Audit Complete
header "System Hardening Audit Completed"
echo -e "${CYAN}Detailed log saved to $LOG_FILE${RESET}"