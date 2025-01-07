#!/bin/bash

# Script to automate Linux updates for Debian and Red Hat-based systems.
# Author: Aayush Pandey
# Date: $(date +"%Y-%m-%d")

# Variables
LOG_FILE="/var/log/linux_update.log"
REBOOT=false

# Function: Log messages to file
log_message() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" | tee -a "$LOG_FILE"
}

# Function: Update Debian-based systems
update_debian() {
    log_message "Starting updates for Debian-based system..."
    sudo apt update && sudo apt upgrade -y
    if [ $? -eq 0 ]; then
        log_message "Debian-based system updated successfully."
    else
        log_message "Error during updates for Debian-based system."
        exit 1
    fi
}

# Function: Update Red Hat-based systems
update_redhat() {
    log_message "Starting updates for Red Hat-based system..."
    sudo yum update -y || sudo dnf update -y
    if [ $? -eq 0 ]; then
        log_message "Red Hat-based system updated successfully."
    else
        log_message "Error during updates for Red Hat-based system."
        exit 1
    fi
}

# Function: Check if reboot is required
check_reboot() {
    if [ -f /var/run/reboot-required ]; then
        log_message "Reboot required after updates."
        REBOOT=true
    else
        log_message "No reboot required after updates."
    fi
}

# Detect the OS type and perform updates
log_message "Detecting operating system type..."
if [ -f /etc/debian_version ]; then
    update_debian
elif [ -f /etc/redhat-release ]; then
    update_redhat
else
    log_message "Unsupported operating system."
    exit 1
fi

# Check for reboot requirement
check_reboot

# Reboot if required
if [ "$REBOOT" = true ]; then
    log_message "Rebooting system in 1 minute..."
    sudo shutdown -r +1
fi

log_message "Linux update process completed."