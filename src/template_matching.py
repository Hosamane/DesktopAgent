
import os

import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
import time

def template_matching():
    SCREENSHOT_DIR = "../screenshots"
    RESULT_DIR = "../results"

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(RESULT_DIR, exist_ok=True)
    print("Taking screenshot...")
    pyautogui.hotkey('win', 'd')
    time.sleep(2)
    img = ImageGrab.grab()
    screenshot_path = os.path.join(SCREENSHOT_DIR, "template_screenshot.png")
    img.save(screenshot_path)

    print("Screenshot saved as template_screenshot.png")
    screen = cv2.imread(screenshot_path)
    template = cv2.imread("D:\\VISIONPROJECT\\templates\\notepad_icon1.png")

    if screen is None:
        raise Exception("template_screenshot.png not found")

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


    result_path = os.path.join(RESULT_DIR, "template_detected.png")
    cv2.imwrite(result_path, screen)


    print("\nDetection Successful")
    print(f"Top Left     : {top_left}")
    print(f"Bottom Right : {bottom_right}")
    print(f"Center X     : {center_x}")
    print(f"Center Y     : {center_y}")
    # pyautogui.hotkey('win', 'd')
    if max_val < 0.8:
        print("Template not found")
        return False
    pyautogui.doubleClick(center_x, center_y, duration=1)
    print("\ntemplate_detected.png saved")
    return True
