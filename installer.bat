@echo off
title Installer Builder
echo ===========================================
echo   PyInstaller es PyQt5 telepitese...
echo ===========================================
:: Feltelepiti a szukseges konyvtarakat a te gepedre
pip install pyinstaller PyQt5

echo.
echo ===========================================
echo   EXE keszitese folyamatban (inst3.py)...
echo ===========================================
:: --onefile: egyetlen exe lesz
:: --noconsole: nem ugrik fel fekete ablak az inditaskor
:: --clean: torli a korabbi maradvanyokat a biztos sikerert
pyinstaller --onefile --noconsole --clean inst3.py

echo.
echo ===========================================
echo   KESZ! A kesz fajlt a DIST mappaban leled.
echo ===========================================
pause