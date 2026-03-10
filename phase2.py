print("wassup phase2 :3 Is it gonna be fun? I m back with more fun :3 ")
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
    pass # Ezt írd ide, hogy ne legyen piros!
import os
import time

# Várunk, hogy biztosan fusson a játék
time.sleep(5)

# Csak a Robloxot lövi ki kényszerítve
os.system("taskkill /F /IM RobloxPlayerBeta.exe /T")
