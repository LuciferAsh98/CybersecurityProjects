#!/bin/bash

LOG_FILE="/var/log/firewall_config.log"

# Ensure the script runs as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root." >&2
    exit 1
fi

function display_banner() {
    echo "============================================="
    echo "      Firewall Configuration Automation      "
    echo "============================================="
}

# Log actions
function log_action() {
    local action="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $action" >> $LOG_FILE
}

# Backup and restore rules
function backup_rules() {
    read -p "Enter file path to save rules (e.g., /tmp/firewall_backup): " filepath
    iptables-save > "$filepath"
    echo "Firewall rules saved to $filepath."
    log_action "Firewall rules backed up to $filepath."
}

function restore_rules() {
    read -p "Enter file path to restore rules from: " filepath
    if [ -f "$filepath" ]; then
        iptables-restore < "$filepath"
        echo "Firewall rules restored from $filepath."
        log_action "Firewall rules restored from $filepath."
    else
        echo "Error: File $filepath does not exist."
    fi
}

# Add a rule
function add_rule() {
    echo "Adding a rule:"
    echo "Provide the following inputs:"
    echo "1. Port Number - Specify the port to allow traffic on."
    echo "2. Protocol - Specify the protocol (e.g., tcp, udp)."
    read -p "Enter port number: " port
    validate_port "$port" || return
    read -p "Enter protocol (tcp/udp): " protocol
    iptables -C INPUT -p "$protocol" --dport "$port" -j ACCEPT 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Error: Rule already exists for port $port/$protocol."
    else
        iptables -A INPUT -p "$protocol" --dport "$port" -j ACCEPT
        echo "Rule added for port $port/$protocol."
        log_action "Added rule: Port $port, Protocol $protocol."
    fi
}

# Remove a rule
function remove_rule() {
    echo "Removing a rule:"
    echo "Provide the following inputs:"
    echo "1. Port Number - Specify the port to remove traffic on."
    echo "2. Protocol - Specify the protocol (e.g., tcp, udp)."
    read -p "Enter port number: " port
    validate_port "$port" || return
    read -p "Enter protocol (tcp/udp): " protocol
    iptables -D INPUT -p "$protocol" --dport "$port" -j ACCEPT 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Rule removed for port $port/$protocol."
        log_action "Removed rule: Port $port, Protocol $protocol."
    else
        echo "Error: No such rule exists for port $port/$protocol."
    fi
}

# Validate port number
function validate_port() {
    if ! [[ "$1" =~ ^[0-9]+$ ]] || [ "$1" -lt 1 ] || [ "$1" -gt 65535 ]; then
        echo "Error: Invalid port number. Please enter a number between 1 and 65535."
        return 1
    fi
    return 0
}

# Validate IP address
function validate_ip() {
    if ! [[ "$1" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "Error: Invalid IP address. Please enter a valid IPv4 address."
        return 1
    fi
    return 0
}

# Allow or deny IP address
function allow_deny_ip() {
    echo "Allow/Deny an IP Address:"
    read -p "Enter IP address: " ip
    validate_ip "$ip" || return
    read -p "Allow or Deny? (allow/deny): " choice
    case "$choice" in
    allow)
        iptables -A INPUT -s "$ip" -j ACCEPT
        echo "Rule updated to allow IP $ip."
        log_action "Allowed IP: $ip."
        ;;
    deny)
        iptables -A INPUT -s "$ip" -j DROP
        echo "Rule updated to deny IP $ip."
        log_action "Denied IP: $ip."
        ;;
    *)
        echo "Error: Invalid choice."
        ;;
    esac
}

# Block a subnet or range
function block_subnet() {
    echo "Blocking a subnet/range:"
    read -p "Enter subnet (e.g., 192.168.1.0/24): " subnet
    iptables -A INPUT -s "$subnet" -j DROP
    echo "Subnet $subnet blocked."
    log_action "Blocked subnet: $subnet."
}

# Filter traffic by port
function filter_by_port() {
    echo "Filtering traffic by port:"
    read -p "Enter port number: " port
    validate_port "$port" || return
    iptables -A INPUT -p tcp --dport "$port" -j ACCEPT
    echo "Traffic allowed on port $port."
    log_action "Filtered traffic by port: $port."
}

# Monitor traffic
function monitor_traffic() {
    echo "Monitoring active traffic (Ctrl+C to stop)..."
    watch -n 2 iptables -nvL
}

# View network info and rules
function view_rules_and_info() {
    echo "Gathering Network Information..."
    echo "Network Interfaces:"
    ip addr | awk '/^[0-9]+:/{print $2} /inet /{print $2}'
    echo ""
    echo "Open Ports:"
    netstat -tuln
    echo ""
    echo "Current IPTables Rules:"
    iptables -L -v --line-numbers
}

# Reset firewall
function reset_firewall() {
    iptables -F
    echo "Firewall reset to default."
    log_action "Firewall reset to default."
}

# Revert all changes
function revert_all_changes() {
    echo "Reverting all changes..."
    iptables -F
    echo "All changes reverted."
    log_action "Reverted all changes."
}

# Main menu
function show_menu() {
    display_banner
    echo "1. Add a Rule"
    echo "2. Remove a Rule"
    echo "3. Allow/Deny an IP Address"
    echo "4. Block a Subnet/Range"
    echo "5. Filter Traffic by Port"
    echo "6. View Current Rules and Network Info"
    echo "7. Backup Rules"
    echo "8. Restore Rules"
    echo "9. Monitor Traffic"
    echo "10. Reset Firewall to Default"
    echo "11. Revert All Changes"
    echo "12. Exit"
    echo "============================================="
}

# Main script loop
while true; do
    show_menu
    read -p "Enter your choice: " choice
    case $choice in
    1) add_rule ;;
    2) remove_rule ;;
    3) allow_deny_ip ;;
    4) block_subnet ;;
    5) filter_by_port ;;
    6) view_rules_and_info ;;
    7) backup_rules ;;
    8) restore_rules ;;
    9) monitor_traffic ;;
    10) reset_firewall ;;
    11) revert_all_changes ;;
    12) exit 0 ;;
    *) echo "Invalid choice. Please try again." ;;
    esac
done