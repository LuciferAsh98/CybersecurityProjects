# Advanced Spyware Tool

This advanced spyware program is trying to show how spyware works and tries to steal user information.

## DISCLAIMER

The Python program is for educational purposes only. Do not use it for any delinquent purposes. The author will not be responsible for any kind of malicious activity.

## WHAT IS SPYWARE?

Spyware is a type of malicious software -- or malware -- that is installed on a computing device without the end user's knowledge. It invades the device, steals sensitive information and internet usage data, and relays it to advertisers, data firms, or external users.

## FEATURES OF THIS CODE

1. Records keystrokes and stores them in a text file.
2. Records clipboard data in a text file.
3. Records Google search history and stores it in an Excel file.
4. Retrieves user system information like IP address, hostname, OS, etc.
5. Takes a screenshot when the program stops.

## REQUIREMENTS

- Python 3.x
- `pynput` library
- `pandas` library
- `pyperclip` library
- `pillow` library
- `openpyxl` library
- `sqlite3` library

## INSTALLATION

1. **Clone the repository or download the files:**

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Install the required dependencies:**

    ```bash
    pip install pynput pandas pyperclip pillow openpyxl
    ```

## USAGE

1. **Create the spyware script:**

    ```bash
    nano spyware.py
    ```

2. **Copy and paste the content of the spyware script into `spyware.py`.**

3. **Make the script executable:**

    ```bash
    chmod +x spyware.py
    ```

4. **Run the spyware script:**

    ```bash
    sudo python3 spyware.py
    ```

## FILE STORAGE

The logs and other files are stored in the following hidden directory: `/var/www/html/.sysfiles`. This directory contains:

- `.logs.txt`: Keystroke log file
- `.clipboard.txt`: Clipboard log file
- `.search_history.xlsx`: Google Chrome search history log file
- `.system_info.xlsx`: System information log file
- `.screenshot.png`: Screenshot file

### Verifying File Storage

You can navigate to this directory and list the files using:

```bash
cd /var/www/html/.sysfiles
ls -a

SECURITY AND ETHICAL CONSIDERATIONS
Unauthorized Use: Using spyware without permission is illegal and unethical.
Privacy: Always respect privacy and comply with laws and regulations regarding data protection.