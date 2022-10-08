@echo off
cd F:\Roblox Launcher
python -m PyInstaller --onefile RobloxPlayerLauncher.py
cd F:\Roblox Launcher\dist\
REM copy RobloxPlayerLauncher.exe C:\Users\Take_1337\AppData\Local\Roblox\Versions\version-0beb053becad47aa
color a
echo COMPILED!
pause