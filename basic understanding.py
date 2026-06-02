import subprocess
import time
import pyautogui

# Open Notepad
subprocess.Popen("notepad.exe")

# Wait for Notepad to launch
time.sleep(3)

# Click roughly in the center of the screen
pyautogui.click(700, 400)

# Type text
pyautogui.write("Hello World", interval=0.05)

pyautogui.hotkey("ctrl","s")