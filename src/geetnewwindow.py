import pygetwindow as gw
import time

def get_new_window(open_function):

    before = set(gw.getAllTitles())

    open_function()

    time.sleep(2)

    after = set(gw.getAllTitles())

    new_windows = list(after - before)

    if not new_windows:
        return None

    return new_windows[0]