
import pyautogui
import time
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x:4d} Y: {y:4d}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopped")
# pyautogui.hotkey('win', 'd')
# time.sleep(2)
# pyautogui.moveTo(777, 352, duration=1)
# pyautogui.doubleClick()
