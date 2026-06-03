import subprocess
import time
import pyautogui
count=0
subprocess.Popen("notepad")

time.sleep(2)

pyautogui.write(
    "\nHello World",
    interval=0.01
)
pyautogui.hotkey('ctrl','shift','s')
time.sleep(1)
pyautogui.write("hello_world"+str(count)+".txt", interval=0.5)
count+=1
pyautogui.press("enter")