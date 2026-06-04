import time
import pygetwindow as gw
from desktop_manager import show_desktop
from ocr import ocr
from api.post_save import save_posts
from template_matching import template_matching
from windows_search import windows_search
from window_tracker import capture_target_window
app_name = "notepad"


def verify_notepad():

    for _ in range(10):

        windows = gw.getAllTitles()

        for title in windows:

            if "Notepad" in title:
                return True

        time.sleep(1)
    print("Notepad window not found")
    return False



def open_application(app_name):
    # show_desktop() 
    for attempt in range(3):
        print(f"\nAttempt {attempt + 1}/3")
        print("Trying OCR...    ")
        if ocr(app_name):
            print("Application found using OCR")
            if verify_notepad():
                print("Notepad window verified")
                return True
        
        print("Trying Template Matching...    ")
        if template_matching():
            print("Application found using Template Matching")
            if verify_notepad():
                print("Notepad window verified")
                return True
            
        
        print("Trying Windows Search...    ")
        if windows_search(app_name):
            print("Application found using Windows Search")
            if verify_notepad():
                print("Notepad window verified")
                return True
             

    print("Application not found")
    return False



if __name__ == "__main__":
    if open_application(app_name):
        print("waiting for application to load")
        capture_target_window()
        # time.sleep(1)
        save_posts()
    else:
        print("Could not open application")


