# A simple script to automate screen captures with timestamps.

import datetime
import os

import pyautogui


def capture():
    folder = "screenshots"
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Generate a unique timestamp for the filename
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(folder, f"screenshot_{now}.png")

    print(f"Taking screenshot...")
    
    # Capture the screen and save the image to the specified path
    img = pyautogui.screenshot()
    img.save(path)
    
    print(f"Done! Saved to: {path}")

if __name__ == "__main__":
    capture()
