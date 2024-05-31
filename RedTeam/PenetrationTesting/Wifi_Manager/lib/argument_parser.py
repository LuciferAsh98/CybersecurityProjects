# argument_parser.py

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="WiFi Manager Utility")
    parser.add_argument("--mode", required=True, help="Mode of operation")
    parser.add_argument("--interface", help="Wi-Fi interface")
    parser.add_argument("--time", help="Time for scanning")
    parser.add_argument("--channel", help="Wi-Fi channel")
    parser.add_argument("--access-point", help="Access point MAC address")
    parser.add_argument("--client", help="Client MAC address")
    parser.add_argument("--number", help="Number of packets to send")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(args)
