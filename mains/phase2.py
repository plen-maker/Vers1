print("wassup phase2 :3 Is it gonna be fun? I m back with more fun :3 ")
ready = input("are you ready? (y/n) ")
if ready.lower() == "y":
    print("lets goooooo :3 ")
else:
    print("too bad :3 ")
import os
from socket import socket
from typing import Type

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

print("sooo we are so bacck!")
print("heres your wifi")
# Source - https://stackoverflow.com/a/24196955
# Posted by Martin Konecny, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-12, License - CC BY-SA 4.0

# Source - https://stackoverflow.com/a/24196955
# Posted by Martin Konecny, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-12, License - CC BY-SA 4.0

# python3.7
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:", hostname)
print("Your Computer IP Address is:", IPAddr)