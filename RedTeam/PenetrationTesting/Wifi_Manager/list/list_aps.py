# list_aps.py

import os

def list_aps():
    with open('/tmp/wifi_scan-01.csv', 'r') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    list_aps()
