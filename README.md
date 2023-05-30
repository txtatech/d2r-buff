# d2r-buff

This script sends a series of key presses to the currently active window. It uses the `win32gui` and `pynput` libraries to simulate key press events at the operating system level.

## Prerequisites

- Python 3.6 or above
- `win32gui` library: Install using `pip install pywin32`
- `pynput` library: Install using `pip install pynput`

## Usage

1. Install the required libraries mentioned in the "Prerequisites" section.

2. Copy and paste the provided code into a Python file (e.g., `macro_script.py`).

3. Run the script using the Python interpreter.

4. The script will start running and listen for the F12 key press event.

5. When you press F12, the script will send a series of key presses (`W`, `F4`, `F5`, `F6`, `W`) to the currently active window.

6. The script will continue running indefinitely, monitoring for the F12 key press event and sending the key presses whenever triggered.

Note: Make sure the game or application window you want to send key presses to is in focus when running the script.

## Customization

- You can modify the `keys_to_send` list in the `on_key_press` function to send a different series of key presses. Add or remove keys as desired.

- Adjust the sleep duration in the `time.sleep()` function inside the while loop to control the interval between each iteration of key press checks.

- You can update the `VK_CODES` dictionary to map different special keys to their corresponding virtual key codes if needed.
