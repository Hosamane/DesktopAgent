# test_post.py

import requests
import subprocess
import time
import pyautogui
import pygetwindow as gw


from window_tracker import is_target_window_active

# def is_notepad_active():

#     try:
#         window = gw.getActiveWindow()

#         if window and "Notepad" in window.title:
#             return True

#     except Exception:
#         pass

#     return False


def safe_type(text):

    for ch in text:

        if not is_target_window_active():
            print("Target window is not active. Please focus the target window and try again.")
            return False

        pyautogui.write(ch)

    return True



def save_posts():
# Fetch posts from JSONPlaceholder API
   posts = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    ).json()
   posts = posts[10:12]
#    subprocess.Popen("notepad")
   time.sleep(2)
   for post in posts:
        
        pyautogui.hotkey("ctrl","n")
        time.sleep(1)
        # if not is_notepad_active():
        #     print("Notepad is not active. Please open Notepad and try again.")
        #     return
        text = f"Title: {post['title']}\n\n{post['body']}"

        # Type content
        # if not is_notepad_active():
        #     print("Notepad is not active. Please open Notepad and try again.")
        #     return
        time.sleep(1)
     
        if not safe_type(text):
            return
        pyautogui.write(text, interval=0.01)


        # Save file
        # if not is_notepad_active():
        #     print("Notepad is not active. Please open Notepad and try again.")
        #     return
        pyautogui.hotkey("ctrl", "shift","s")
        time.sleep(2)

        filename = f"post_{post['id']}.txt"
        pyautogui.write(filename)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

        windows = gw.getAllTitles()

        popup_found = False
        for title in windows:
            # print(f"Window: {title}")
            if "Confirm Save As" in title:
                popup_found = True
                print("Save As confirmation popup detected.")
                break

        if popup_found:    
            pyautogui.hotkey("alt", "y")   # Move to Yes
            # pyautogui.press("enter")  # Confirm overwrite
            time.sleep(1)
        
        
        print(f"Saved {filename}")

   print("Single post test completed.")


