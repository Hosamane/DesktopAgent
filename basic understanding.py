# import subprocess
# import time
# import pyautogui

# # Open Notepad
# subprocess.Popen("notepad.exe")

# # Wait for Notepad to launch
# time.sleep(3)

# # Click roughly in the center of the screen
# pyautogui.click(700, 400)

# # Type text
# pyautogui.write("Hello World", interval=0.05)

# pyautogui.hotkey("ctrl","s")



import groundingdino
import os

print("GroundingDINO:", groundingdino.__file__)

base = os.path.dirname(groundingdino.__file__)

for root, dirs, files in os.walk(base):
    for f in files:
        if "SwinT_OGC" in f:
            print(os.path.join(root, f))