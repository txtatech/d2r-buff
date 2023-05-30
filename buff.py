import time
import ctypes
import win32gui
from pynput import keyboard

# Define virtual key codes for special keys
VK_CODES = {
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
}

def send_keypresses(keys):
    # Get the handle of the currently active window
    window_handle = win32gui.GetForegroundWindow()
    if window_handle == 0:
        print("No active window found")
        return
    
    for key in keys:
        # Simulate key press event at the OS level
        if len(key) == 1:
            # Single character key
            ctypes.windll.user32.PostMessageW(window_handle, 0x0100, ord(key), 0)
            ctypes.windll.user32.PostMessageW(window_handle, 0x0101, ord(key), 0)
        else:
            # Special key
            vk_code = VK_CODES.get(key)
            if vk_code is not None:
                ctypes.windll.user32.PostMessageW(window_handle, 0x0100, vk_code, 0)
                ctypes.windll.user32.PostMessageW(window_handle, 0x0101, vk_code, 0)
            else:
                print(f"Unknown key: {key}")
        time.sleep(0.7)

def on_key_press(key):
    if key == keyboard.Key.f12:
        # Start sending key presses when F12 key is pressed
        keys_to_send = ['W', 'F4', 'F5', 'F6', 'W']
        send_keypresses(keys_to_send)

# Start the key press listener
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

while True:
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage

# The script will keep running indefinitely
