
import easyocr
import cv2
import pyautogui
import time
from PIL import ImageGrab
pyautogui.hotkey('win', 'd')
time.sleep(2)
img = ImageGrab.grab()

img.save("screen.png")



# OCR
reader = easyocr.Reader(['en'])
result = reader.readtext("screen.png")

# Load image for visualization
img = cv2.imread("screen.png")

target = "Notepad"

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
        
        pyautogui.doubleClick(x, y,duration=1)

        # Show result
        cv2.imwrite("result.png", img)
        print("Saved result.png")

        # Click center

        break