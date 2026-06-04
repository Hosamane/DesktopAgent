# test_post.py

import requests
import subprocess
import time
import pyautogui
import pygetwindow as gw

# Fetch posts from JSONPlaceholder API
posts = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
).json()

# Use only the first post
posts = posts[10:12]

# Open Notepad
subprocess.Popen("notepad")

time.sleep(2)
for post in posts:
    pyautogui.hotkey("ctrl","n")
    time.sleep(1)
    text = f"Title: {post['title']}\n\n{post['body']}"

    # Type content
    pyautogui.write(text, interval=0.01)

    time.sleep(1)

    # Save file
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