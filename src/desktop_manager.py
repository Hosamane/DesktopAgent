import pyautogui
import pygetwindow as gw
import time


def show_desktop():

    active = gw.getActiveWindow()

    # If some window is active,
    # minimize all windows
    if active is not None:

        print(
            f"Minimizing active window: "
            f"{active.title}"
        )

        pyautogui.hotkey("win","d")

        time.sleep(2)

    print("Desktop is visible")


def restore_windows():

    pyautogui.hotkey("win","d")

    time.sleep(1)