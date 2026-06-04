import time
import pyautogui
import pygetwindow as gw

from hybrid import HybridDetector


class NotepadLauncher:

    def __init__(self):
        self.detector = HybridDetector()

    def wait_for_notepad(self, timeout=10):

        start = time.time()

        while time.time() - start < timeout:

            titles = gw.getAllTitles()

            for title in titles:

                if "notepad" in title.lower():

                    try:
                        win = gw.getWindowsWithTitle(title)[0]
                        win.activate()
                    except:
                        pass

                    return True

            time.sleep(0.5)

        return False

    def launch(self):

        for attempt in range(3):

            print(f"Attempt {attempt+1}")

            result = self.detector.find("notepad")

            if not result["found"]:
                continue

            pyautogui.doubleClick(
                result["x"],
                result["y"]
            )

            if self.wait_for_notepad():
                print("Notepad launched")
                return True

        raise Exception(
            "Failed to launch Notepad"
        )