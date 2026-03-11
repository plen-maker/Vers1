print("wassup phase2 :3 Is it gonna be fun? I m back with more fun :3 ")
from curses import window
import os

user_home = os.path.expanduser("~")
roblox_path = os.path.join(user_home, "AppData", "Local", "Roblox", "Versions")
try:
    for root, dirs, files in os.walk(roblox_path):
        if "RobloxPlayerBeta.exe" in files:
            teljes_utvonal = os.path.join(root, "RobloxPlayerBeta.exe")
            os.startfile(teljes_utvonal)
            break
except Exception as e:
    pass 
import time

time.sleep(5)

os.system("taskkill /F /IM RobloxPlayerBeta.exe /T")

import webbrowser

# A videó URL-je
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Megnyitás a böngészőben
webbrowser.open(video_url)

