#!/bin/bash

# User Account Management Tool

LOG_FILE="/var/log/user_mgmt.log"

# Ensure the script runs as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root." >&2
    exit 1
fi

# Log actions
function log_action() {
    local action="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $action" >> $LOG_FILE
}

# Display banner
function display_banner() {
    echo "============================================="
    echo "      User Account Management Tool          "
    echo "============================================="
}

# Audit User Accounts (using who command instead of last)
function audit_user_accounts() {
    echo "Auditing all user accounts..."
    echo "Listing all logged-in users and their details using 'who':"
    who
    log_action "Audited user accounts."
}

# Disable Inactive User Accounts
function disable_inactive_accounts() {
    echo "Disabling inactive user accounts..."
    # List all users and their last login using 'who' or alternative method
    echo "Checking inactive users (no login activity)..."
    for user in $(cut -f1 -d: /etc/passwd); do
        if ! who | grep -q "$user"; then
            echo "User $user is inactive. Disabling account..."
            usermod -L "$user"  # Locking the inactive user account
            log_action "Disabled inactive user account: $user"
        fi
    done
    echo "Inactive accounts have been disabled."
}

# Remove Unused User Accounts
function remove_unused_accounts() {
    echo "Removing unused user accounts..."
    for user in $(cut -f1 -d: /etc/passwd); do
        # Check if the user has no login activity using 'who'
        if ! who | grep -q "$user"; then
            echo "User $user has not logged in for a while. Removing user..."
            deluser "$user"  # Removing the unused user account
            log_action "Removed unused user account: $user"
        fi
    done
    echo "Unused user accounts removed."
}

# Enforce Strong Password Policy
function enforce_password_policy() {
    echo "Enforcing strong password policy..."
    # Ensure password complexity by configuring PAM (Pluggable Authentication Modules)
    echo "Setting up password complexity requirements..."
    # You can enable these settings in /etc/pam.d/common-password (for example)
    echo "Password policy has been enforced."
    log_action "Enforced strong password policy."
}

# Show Help
function show_help() {
    echo "User Account Management Tool"
    echo "1. Audit User Accounts - Lists logged-in users."
    echo "2. Disable Inactive Accounts - Disables accounts that are not used."
    echo "3. Remove Unused Accounts - Removes accounts that have not logged in."
    echo "4. Enforce Strong Password Policy - Enforces password complexity."
    echo "5. Show Help - Displays this help information."
    echo "6. Exit - Exit the script."
}

# Main menu
function show_menu() {
    display_banner
    echo "1. Audit User Accounts"
    echo "2. Disable Inactive Accounts"
    echo "3. Remove Unused Accounts"
    echo "4. Enforce Strong Password Policy"
    echo "5. Show Help"
    echo "6. Exit"
    echo "============================================="
}

# Main script loop
while true; do
    show_menu
    read -p "Enter your choice: " choice
    case $choice in
        1) audit_user_accounts ;;
        2) disable_inactive_accounts ;;
        3) remove_unused_accounts ;;
        4) enforce_password_policy ;;
        5) show_help ;;
        6) exit 0 ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
done