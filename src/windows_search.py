import pyautogui
import time


def windows_search(app_name):

    print(f"Searching for {app_name} using Windows Search...")

    pyautogui.press("win")

    time.sleep(1)

    pyautogui.write(
        app_name,
        interval=0.05
    )

    time.sleep(1)

    pyautogui.press("enter")

    print(f"{app_name} launched")

    return True


