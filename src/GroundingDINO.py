

import time

from PIL import ImageGrab
import torch
import groundingdino
from groundingdino.util.inference import (
    load_model,
    load_image,
    predict,
    annotate
)
import cv2
import os
import pyautogui



TARGET = "spotify."
SCREENSHOT = "screen2.png"


print("Taking screenshot...")
pyautogui.hotkey('win', 'd')
time.sleep(2)
img = ImageGrab.grab()
img.save(SCREENSHOT)

print(f"Screenshot saved: {SCREENSHOT}")


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {DEVICE}")



config_path = os.path.join(
    os.path.dirname(groundingdino.__file__),
    "config",
    "GroundingDINO_SwinT_OGC.py"
)

weights_path = r"D:\VISIONPROJECT\models\groundingdino_swint_ogc.pth"

print("CONFIG :", config_path)
print("WEIGHTS:", weights_path)

model = load_model(
    config_path,
    weights_path
)

print("Model loaded successfully")

image_source, image = load_image(SCREENSHOT)

print("Image Shape:", image.shape)


boxes, logits, phrases = predict(
    model=model,
    image=image,
    caption=TARGET,
    box_threshold=0.15,
    text_threshold=0.15,
    device=DEVICE
)

print("\nTotal Detections:", len(boxes))

if len(boxes) == 0:
    print("No detections found.")
    exit()


all_frame = annotate(
    image_source=image_source,
    boxes=boxes,
    logits=logits,
    phrases=phrases
)

cv2.imwrite("all_detections.png", all_frame)

print("Saved: all_detections.png")



best_idx = logits.argmax()

best_box = boxes[best_idx]
best_score = logits[best_idx]
best_phrase = phrases[best_idx]

print("\nBEST DETECTION")
print("Phrase     :", best_phrase)
print("Confidence :", float(best_score))


best_frame = annotate(
    image_source=image_source,
    boxes=best_box.unsqueeze(0),
    logits=best_score.unsqueeze(0),
    phrases=[best_phrase]
)

cv2.imwrite("best_detection.png", best_frame)

print("Saved best_detection.png")



height, width = image_source.shape[:2]

cx, cy, bw, bh = best_box.tolist()

cx *= width
cy *= height
bw *= width
bh *= height

x1 = int(cx - bw / 2)
y1 = int(cy - bh / 2)

x2 = int(cx + bw / 2)
y2 = int(cy + bh / 2)

center_x = int((x1 + x2) / 2)
center_y = int((y1 + y2) / 2)

print("\nPIXEL COORDINATES")
print(f"Top Left     : ({x1}, {y1})")
print(f"Bottom Right : ({x2}, {y2})")
print(f"Center       : ({center_x}, {center_y})")



result = {
    "target": TARGET,
    "method": "groundingdino",
    "confidence": float(best_score),
    "x": center_x,
    "y": center_y
}

print("\nRESULT")
print(result)


# import pyautogui
# pyautogui.click(center_x, center_y)