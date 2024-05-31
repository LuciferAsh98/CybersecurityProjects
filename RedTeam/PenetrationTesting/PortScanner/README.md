# Basic Port Scanner

## Description
This script is a basic port scanner that scans for open ports on a specified IP address within the range of 1 to 1024. It uses the `socket` library to attempt to connect to each port and reports back which ones are open along with the associated service, if known.

## Usage
To use this script, you need Python installed on your system.

### Running the Script
1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the following command:
   python3 port_scanner.py <IP to Scan>

4. Example 
   python3 port_scanner.py 192.168.9.9
