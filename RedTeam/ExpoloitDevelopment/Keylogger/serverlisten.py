import socket
import sys

# _*_ coding: utf-8 _*_
# Tested on Linux (e.g., Linux kali 6.5.0-kali2-amd64)

common_ports = {
    20: 'FTP Data',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    465: 'SMTPS',
    993: 'IMAPS',
    995: 'POP3S',
}

def scan_ports(target):
    open_ports = []
    for port in range(1, 1024):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                service = common_ports.get(port, 'Unknown Service')
                open_ports.append((port, service))
    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <IP to Scan>")
        sys.exit(1)

    target_ip = sys.argv[1]
    print(f"Scanning {target_ip} for open ports...")
    open_ports = scan_ports(target_ip)
    if open_ports:
        print(f"Open ports on {target_ip}:")
        for port, service in open_ports:
            print(f"Port {port}: {service}")
    else:
        print(f"No open ports found on {target_ip}.")
