
import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
import time

print("Taking screenshot...")
pyautogui.hotkey('win', 'd')
time.sleep(2)
img = ImageGrab.grab()
img.save("screen1.png")

print("Screenshot saved as screen1.png")
screen = cv2.imread("screen1.png")
template = cv2.imread("notepad_icon1.png")

if screen is None:
    raise Exception("screen1.png not found")

if template is None:
    raise Exception("notepad_icon1.png not found")


result = cv2.matchTemplate(
    screen,
    template,
    cv2.TM_CCOEFF_NORMED
)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(f"\nMatch Confidence: {max_val:.4f}")


h, w = template.shape[:2]

top_left = max_loc

bottom_right = (
    top_left[0] + w,
    top_left[1] + h
)

center_x = top_left[0] + w // 2
center_y = top_left[1] + h // 2


cv2.rectangle(
    screen,
    top_left,
    bottom_right,
    (0, 255, 0),
    3
)

cv2.circle(
    screen,
    (center_x, center_y),
    5,
    (0, 0, 255),
    -1
)


cv2.imwrite("detected.png", screen)


print("\nDetection Successful")
print(f"Top Left     : {top_left}")
print(f"Bottom Right : {bottom_right}")
print(f"Center X     : {center_x}")
print(f"Center Y     : {center_y}")
pyautogui.doubleClick(center_x, center_y, duration=1)

print("\ndetected.png saved")