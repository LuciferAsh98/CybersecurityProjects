# WiFi Manager

## Overview

WiFi Manager is a versatile command-line utility designed for network enthusiasts and professionals. This tool facilitates various Wi-Fi network operations, including scanning networks, listing access points and clients, and other essential network management tasks. WiFi Manager is built with the aim of providing a practical resource for legitimate network administration and research purposes.

## Features

- **Network Scanning**: Identify available Wi-Fi networks in the vicinity.
- **Access Point Listing**: List all available Wi-Fi access points.
- **Client Listing**: Identify all clients connected to a specific Wi-Fi network.
- **Flexible Modes of Operation**: Various modes to perform different network management tasks.

## Prerequisites

- **Operating System**: Linux or macOS
- **Python**: Version 3.x
- **Aircrack-ng**: Required for certain operations

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/wifi_manager.git
    ```

2. **Move the repository to a suitable location**:

    ```bash
    sudo mv wifi_manager /usr/local
    ```

3. **Rename the main script and make it executable**:

    ```bash
    sudo mv /usr/local/wifi_manager/wifi_manager.py /usr/local/wifi_manager/wifi_manager
    sudo chmod +x /usr/local/wifi_manager/wifi_manager
    ```

4. **Create a symbolic link for easy access**:

    ```bash
    sudo ln -s /usr/local/wifi_manager/wifi_manager /usr/local/bin/wifi_manager
    ```

5. **Ensure `/usr/local/bin` is in your `PATH`**:

    ```bash
    echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bash_profile
    source ~/.bash_profile
    ```

## Usage

### Command-line Options

| Option             | Description                            |
|--------------------|----------------------------------------|
| `-h` or `--help`   | Show help message and exit             |
| `--mode=<mode>`    | Specify the mode to use                |
| `--interface=<interface>` | Specify the Wi-Fi interface   |
| `--time=<time>`    | Specify the time for scanning          |
| `--channel=<channel>` | Specify the Wi-Fi channel number   |
| `--access-point=<access-point>` | Specify the access point MAC |
| `--client=<client>` | Specify the client MAC               |
| `--number=<number>` | Specify the number of packets to send |

### Modes of Operation

| Mode            | Description                                      |
|-----------------|--------------------------------------------------|
| `scan_networks` | Scan for available Wi-Fi networks                |
| `list_aps`      | List available Wi-Fi access points               |
| `scan_clients`  | Scan for clients connected to a Wi-Fi network    |
| `list_clients`  | List clients connected to a specific Wi-Fi network |

### Examples

1. **Scan Wi-Fi networks**:

    ```bash
    sudo wifi_manager --mode=scan_networks --interface=wlan0 --time=120
    ```

2. **List available Wi-Fi networks**:

    ```bash
    sudo wifi_manager --mode=list_aps
    ```

3. **Scan a Wi-Fi network for clients**:

    ```bash
    sudo wifi_manager --mode=scan_clients --interface=wlan0 --channel=6 --access-point=FF:FF:FF:FF:FF:FF --time=120
    ```

4. **List clients connected to a Wi-Fi network**:

    ```bash
    sudo wifi_manager --mode=list_clients
    ```

## Acknowledgments

This project was inspired by various network management tools and built upon open-source contributions. Special thanks to [ezhil56x](https://github.com/ezhil56x) for providing foundational ideas and resources.
