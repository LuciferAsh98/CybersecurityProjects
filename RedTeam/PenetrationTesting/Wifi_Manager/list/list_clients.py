# list_clients.py

import os

def list_clients():
    with open('/tmp/wifi_scan-01.csv', 'r') as file:
        for line in file:
            if "Station MAC" in line:
                print(line.strip())

if __name__ == "__main__":
    list_clients()
