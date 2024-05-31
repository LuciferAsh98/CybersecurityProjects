#!/usr/bin/python3

import os
from lib.argument_parser import parse_arguments
from scan.scan_networks import scan_networks
from list.list_aps import list_aps
from list.list_clients import list_clients

def main():
    args = parse_arguments()
    
    if args.mode == "scan_networks":
        scan_networks(args.interface, args.time)
    elif args.mode == "list_aps":
        list_aps()
    elif args.mode == "list_clients":
        list_clients()
    else:
        print("Invalid mode. Use --help for more information.")

if __name__ == "__main__":
    main()
