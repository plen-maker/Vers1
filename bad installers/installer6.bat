@echo off
title Installer Builder es Letolto
echo ===========================================
echo   1. Fajlok letoltese a GitHubrol...
echo ===========================================

:: Letoltjuk az oopa.py-t
curl -L -o oopa.py https://raw.githubusercontent.com/plen-maker/Vers1/main/oopa.py

:: Letoltjuk a phase2.py-t
curl -L -o phase2.py https://raw.githubusercontent.com/plen-maker/Vers1/main/phase2.py

echo.
echo ===========================================
echo   2. Szukseges konyvtarak telepitese...
echo ===========================================
pip install pyinstaller PyQt5

echo.
echo ===========================================
echo   3. EXE keszitese...
echo ===========================================
:: Itt az inst3.py-t csomagoljuk be
pyinstaller --onefile --noconsole --clean inst3.py

echo.
echo ===========================================
echo   KESZ! A dist mappaban van az inst3.exe.
echo   Kuldd el az inst3.exe-t, az oopa.py-t es a phase2.py-t!
echo ===========================================
pause