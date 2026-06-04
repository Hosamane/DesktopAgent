from time import time

from ocr import ocr
from api.post_save import save_posts
from template_matching import template_matching
from windows_search import windows_search

app_name = "notepad"
def open_application(app_name):
    print("Trying OCR...    ")
    if ocr(app_name):
        print("Application found using OCR")
        return True
    
    print("Trying Template Matching...    ")
    if template_matching():
        print("Application found using Template Matching")
        return True
    
    print("Trying Windows Search...    ")
    if windows_search(app_name):
        print("Application found using Windows Search")
        return True     

    print("Application not found")
    return False



if __name__ == "__main__":
    if open_application(app_name):
        print("waiting for application to load")
        # time.sleep(1)
        save_posts()
    else:
        print("Could not open application")
