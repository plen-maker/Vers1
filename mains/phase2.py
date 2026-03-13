print("wassup phase2 :3 Is it gonna be fun? I m back with more fun :3 ")
import time

ready = input("are you ready? (y/n) ")
if ready.lower() == "y":
    print("lets goooooo :3 ")
else:
    print("too bad :3 ")
import os
from socket import socket
from tracemalloc import start
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

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:", hostname)
print("Your Computer IP Address is:", IPAddr)

print("now we are gonna restart your computer to apply the changes?") 
q1 = input("do you want to restart? (y/n) ")
if q1.lower() == "y":
    print("well too bad")

time

if q1.lower() == "n":
    print("well too bad")

so = input("So do you want to get the discordapp token? (y/n) ")

if so.lower() == "y":
    print("well too bad")

elif so.lower() == "n":
    print("well too bad")

print("You are getting no where. Are you?")
time.sleep(2)

import os
import subprocess

def open_discord():
    path = os.path.expandvars(r"%LocalAppData%\Discord\Update.exe")
    if os.path.exists(path):
        subprocess.Popen([path, "--processStart", "Discord.exe"])
    else:
        # Ha nincs telepítve, nyissa meg a böngészőt
        import webbrowser
        webbrowser.open("https://discord.com")

open_discord()

time .sleep(2)

import webbrowser
import sys

def kilepes_es_discord(self):
   
    webbrowser.open("discord://") 
    
 
    sys.exit()

print("sooo we are so bacck!")
time.sleep(2)
print("I got your roblox and discord ")
time.sleep(2)
print("It s on the server!")
time.sleep(2)
print("youre cooked ")
time .sleep(2)

steam1 = input("do you want to get the steam token? (y/n) ")
if steam1.lower() == "y":
    print("well too bad")

elif steam1.lower() == "n":
    print("well too bad")

time .sleep(2)

import os
import subprocess
import winreg

def steam_inditasa():
    try:
        # 1. Megkeressük a Registry-ben, hová van telepítve a Steam
        # Ez akkor is megtalálja, ha a D: vagy E: meghajtón van!
        hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
        steam_path, _ = winreg.QueryValueEx(hkey, "SteamExe")
        winreg.CloseKey(hkey)

        # 2. Elindítjuk a megtalált EXE-t
        # A "steam://open/main" paraméter biztosítja, hogy a főablak ugorjon fel
        subprocess.Popen([steam_path, "steam://open/main"])
        print(f"Steam elindítva innen: {steam_path}")

    except Exception as e:
        # Ha valamiért nem találja a Registry-ben, próbáljuk a sima linket
        import webbrowser
        webbrowser.open("steam://open/main")
        print("Registry hiba, sima link indítása...")

import os

def steam_bezarasa():
    # A /F kényszeríti a bezárást, a /IM pedig a folyamat neve alapján keres
    # A >nul 2>&1 rész azért kell, hogy ne ugorjon fel fekete ablak hibaüzenettel
    os.system("taskkill /F /IM steam.exe /T >nul 2>&1")
    print("Steam folyamat leállítva.")

math1 = input("Can you do a simple calculation? (y/n) ")
if math1.lower() == "y":
    print("Then answer this.")

elif math1.lower() == "n":
    print("well too bad")


time .sleep(1)

math1a = input("What is 2 + 2? ")
if math1a == "4":
    print("Correct!")
else:
    print("Wrong answer.")
time .sleep(2)
webbrowser.open("https://www.google.com")
import os
time.sleep(2)
# Kilövi a Chrome összes folyamatát
os.system("taskkill /F /IM chrome.exe /T >nul 2>&1")

webbrowser.open("https://www.google.com")
import os
time.sleep(2)
# Kilövi a Chrome összes folyamatát
os.system("taskkill /F /IM chrome.exe /T >nul 2>&1")

print("I have your google account too :3 ")
time .sleep(2)
print("I have your roblox, discord, steam and google account :3 ")
time .sleep(2)
print("I have all your accounts :3 ")
time .sleep(2)

print("So if that was simple and fun do this math")
math2 = input("solve this: ζ(s)=∑n=1∞1/ns")
if math2.lower() == "1":
    print("Correct!")
else:
    print("Wrong answer.")
time .sleep(2)
print("I have no clue too!")
time .sleep(2)


