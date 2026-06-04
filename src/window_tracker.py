import pygetwindow as gw
import time

TARGET_WINDOW = None


def capture_target_window():

    global TARGET_WINDOW

    time.sleep(2)

    TARGET_WINDOW = gw.getActiveWindow()

    if TARGET_WINDOW:

        print(
            f"Target Window: "
            f"{TARGET_WINDOW.title}"
        )


def is_target_window_active():

    global TARGET_WINDOW

    if TARGET_WINDOW is None:
        return False

    active = gw.getActiveWindow()

    if active is None:
        return False

    return (
        active._hWnd ==
        TARGET_WINDOW._hWnd
    )