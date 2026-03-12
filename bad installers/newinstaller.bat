@echo off
title Installer Generalas
echo ===========================================
echo   PyInstaller es PyQt5 telepitese...
echo ===========================================
:: Feltelepiti a szukseges konyvtarakat a te gepedre
pip install pyinstaller PyQt5

echo.
echo ===========================================
echo   EXE keszitese folyamatban (inst3.py)...
echo ===========================================
:: --onefile: egyetlen exe lesz, amit konnyu kuldeni
:: --noconsole: nem ugrik fel fekete ablak az inditaskor, csak a GUI
:: --clean: torli a korabbi maradvanyokat a hibamentes forditasert
pyinstaller --onefile --noconsole --clean inst3.py

echo.
echo ===========================================
echo   KESZ! A futtathato fajlt a DIST mappaban talalod.
echo ===========================================
pause