

from PIL import ImageGrab
import cv2
import pyautogui
import time 
pyautogui.hotkey('win', 'd')
time.sleep(2)
img = ImageGrab.grab()

img.save("screen.png")

screen = cv2.imread("screen.png")
template = cv2.imread("notepad_icon.png")

print(screen is None)
print(template is None)
print("Screenshot shape:", screen.shape)
print("Template shape:", template.shape)
result = cv2.matchTemplate(
    screen,template,cv2.TM_CCOEFF_NORMED
)


_, max_val, _, max_loc = cv2.minMaxLoc(result)

print("Confidence:", max_val)
print("Location:", max_loc)
