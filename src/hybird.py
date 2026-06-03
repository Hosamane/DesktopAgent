import time

from PIL import ImageGrab
import pyautogui
import cv2
import pyautogui
import easyocr
import torch
import groundingdino
from groundingdino.util.inference import (
    load_model,
    load_image,
    predict
)
import os


class HybridDetector:

    def  __init__(self):

        # OCR
        self.reader = easyocr.Reader(['en'])

        # GroundingDINO
        config_path = os.path.join(
            os.path.dirname(groundingdino.__file__),
            "config",
            "GroundingDINO_SwinT_OGC.py"
        )

        weights_path = r"D:\VISIONPROJECT\models\groundingdino_swint_ogc.pth"

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print(f"Using device: {self.device}")

        self.model = load_model(
            config_path,
            weights_path
        )

        print("GroundingDINO Loaded")

        # Templates
        self.templates = {
            "notepad": "notepad_icon.png"
            # "chrome": "templates/chrome_icon.png"
        }

    def take_screenshot(self):
        pyautogui.hotkey('win', 'd')    
        time.sleep(2)

        ImageGrab.grab().save("screen.png")

        return "screen.png"

    def find_with_ocr(self, image_path, target):

        print("Trying OCR...")
        pyautogui.hotkey('win', 'd')
        

        results = self.reader.readtext(image_path)

        for box, text, score in results:

            if target.lower() in text.lower():

                x = int(
                    (box[0][0] + box[2][0]) / 2
                )

                y = int(
                    (box[0][1] + box[2][1]) / 2
                )

                return {
                    "found": True,
                    "method": "ocr",
                    "x": x,
                    "y": y,
                    "confidence": float(score)
                }

        return {"found": False}

    def find_with_template(
        self,
        screen_path,
        template_path
    ):

        print("Trying Template Match...")

        screen = cv2.imread(screen_path)

        template = cv2.imread(template_path)

        if template is None:

            return {"found": False}

        h, w = template.shape[:2]

        result = cv2.matchTemplate(
            screen,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        _, score, _, loc = cv2.minMaxLoc(result)

        if score < 0.80:

            return {"found": False}

        return {
            "found": True,
            "method": "template",
            "x": loc[0] + w // 2,
            "y": loc[1] + h // 2,
            "confidence": float(score)
        }

    def find_with_dino(
        self,
        image_path,
        target
    ):

        print("Trying GroundingDINO...")

        image_source, image = load_image(
            image_path
        )

        boxes, logits, phrases = predict(
            model=self.model,
            image=image,
            caption=f"{target}.",
            box_threshold=0.15,
            text_threshold=0.15,
            device=self.device
        )

        if len(boxes) == 0:

            return {"found": False}

        best_idx = logits.argmax()

        best_box = boxes[best_idx]

        best_score = float(
            logits[best_idx]
        )

        height, width = (
            image_source.shape[:2]
        )

        cx, cy, bw, bh = (
            best_box.tolist()
        )

        cx *= width
        cy *= height

        bw *= width
        bh *= height

        center_x = int(cx)
        center_y = int(cy)

        return {
            "found": True,
            "method": "groundingdino",
            "x": center_x,
            "y": center_y,
            "confidence": best_score
        }

    def find(self, target):

        screen_path = (
            self.take_screenshot()
        )

  
        result = self.find_with_ocr(
            screen_path,
            target
        )

        if result["found"]:

            return result

   

        if (
            target.lower()
            in self.templates
        ):

            result = (
                self.find_with_template(
                    screen_path,
                    self.templates[
                        target.lower()
                    ]
                )
            )

            if result["found"]:

                return result



        result = self.find_with_dino(
            screen_path,
            target
        )

        return result



if __name__ == "__main__":

    detector = HybridDetector()

    result = detector.find(
        "notepad"
    )

    print("\nFINAL RESULT")
    print(result)

    if result["found"]:

        print(
            f"Found using {result['method']}"
        )

        print(
            f"Location: "
            f"({result['x']}, "
            f"{result['y']})"
        )

        print(
            f"Confidence: "
            f"{result['confidence']:.3f}"
        )

        # Uncomment later
        # import pyautogui
        # pyautogui.click(
        #     result["x"],
        #     result["y"]
        # )