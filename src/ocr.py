
import easyocr
import cv2
import pyautogui
import time
import os
from PIL import ImageGrab
from datetime import datetime



def ocr(app_name):
    pyautogui.hotkey('win', 'd')
    time.sleep(2)
    img = ImageGrab.grab()
    SCREENSHOT_DIR = "../screenshots"
    RESULT_DIR = "../results"

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(RESULT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join( SCREENSHOT_DIR,f"ocr_screenshot_{timestamp}.png")
    img.save(screenshot_path)
    pyautogui.hotkey('win', 'd')
    # OCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext(screenshot_path)

    # Load image for visualization
    img = cv2.imread(screenshot_path)

    target = app_name

    for detection in result:
        bbox, text, confidence = detection

        print(text)

        if target.lower() in text.lower():

            print("Found:", text)
            print("Confidence:", confidence)
            print("Coordinates:", bbox)

            # Rectangle coordinates
            x1 = int(bbox[0][0])
            y1 = int(bbox[0][1])

            x2 = int(bbox[2][0])
            y2 = int(bbox[2][1])

            # Draw rectangle
            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Center point
            x = int((x1 + x2) / 2)
            y = int((y1 + y2) / 2)

            # Draw center point
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

            print("Center:", x, y)
            pyautogui.hotkey('win', 'd')
            pyautogui.doubleClick(x, y-25,duration=1)

            # Show result
            result_path = os.path.join( RESULT_DIR, f"ocr_result_{timestamp}.png")

            cv2.imwrite(result_path, img)
            print(f"Saved ocr_result_{timestamp}.png")
            return True
            # Click center

    
    return False

