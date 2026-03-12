import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def start_oopa():
    try:
        # Megnyitja az oopa.py-t egy új konzol ablakban
        # Feltételezzük, hogy az oopa.py ugyanabban a mappában van
        subprocess.Popen([sys.executable, "oopa.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        root.destroy() # Bezárja az ablakot
    except Exception as e:
        print(f"Hiba: {e}")
        root.destroy()

# Ablak létrehozása
root = tk.Tk()
root.title("Installer")
root.geometry("300x150")

# Szöveg az ablakban
label = tk.Label(root, text="Installer. Do you want to install?", pady=20)
label.pack()

# Gombok kerete
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# OK gomb
ok_button = tk.Button(button_frame, text="OK", width=10, command=start_oopa)
ok_button.pack(side=tk.LEFT, padx=5)

# Cancel gomb
cancel_button = tk.Button(button_frame, text="Cancel", width=10, command=root.destroy)
cancel_button.pack(side=tk.LEFT, padx=5)

root.mainloop()