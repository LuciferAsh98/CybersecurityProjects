# scan_networks.py

import subprocess

def scan_networks(interface, time):
    print(f"Scanning Wi-Fi networks on {interface} for {time} seconds...")
    subprocess.run(["sudo", "airodump-ng", interface, "--write", "/tmp/wifi_scan", "--output-format", "csv"], timeout=int(time))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Scan Wi-Fi networks.")
    parser.add_argument("--interface", required=True, help="Wi-Fi interface to use for scanning.")
    parser.add_argument("--time", required=True, help="Time to scan in seconds.")
    args = parser.parse_args()
    
    scan_networks(args.interface, args.time)
