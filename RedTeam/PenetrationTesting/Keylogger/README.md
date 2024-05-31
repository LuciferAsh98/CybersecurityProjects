# Keylogger Project

This project demonstrates a simple keylogger that logs keystrokes and sends the data to a server in real-time. It is intended for educational purposes only.

## Legal Disclaimer

This script is provided for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit permission before using such tools on any system.

## Requirements

- Python 3.x
- `pynput` library
- `pandas` library

## Installation

1. **Clone the repository or download the files:**

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Install the required dependencies:**

    ```bash
    pip install pynput pandas
    ```

## Running the Server

1. **Navigate to the directory containing the `server.py` script:**

    ```bash
    cd /path/to/server.py
    ```

2. **Run the server script:**

    ```bash
    sudo python3 serverlisten.py
    ```

   The server will start listening for incoming connections on port 8080.

## Running the Keylogger

1. **Navigate to the directory containing the `keylogger.py` script:**

    ```bash
    cd /path/to/keylogger.py
    ```

2. **Run the keylogger script:**

    ```bash
    sudo python3 keylogger.py
    ```

   The keylogger will start capturing keystrokes and attempting to fetch clipboard data. This data will be sent to the server specified in the script.

## Files

- `serverlisten.py`: The server script that listens for incoming connections and prints received data in real-time.
- `keylogger.py`: The keylogger script that captures keystrokes and sends the data to the server.

## Modifications

- **Server Address:** Replace the IP address and port in the `SERVER_ADDRESS` variable in `keylogger.py` with your server's IP address and desired port.

## Security and Ethical Considerations

- **Unauthorized Use:** Using keyloggers without permission is illegal and unethical.
- **Privacy:** Always respect privacy and comply with laws and regulations regarding data protection.

## Troubleshooting

- **No Module Named `pynput`:** Ensure you have installed the required dependencies using `pip install pynput pandas`.
- **Permission Denied:** Run the scripts with `sudo` to ensure necessary permissions for capturing keystrokes and network operations.
- **Connection Refused:** Ensure the server is running and listening on the specified IP address and port.
