@echo off
cd ..
py -m nuitka --onefile main.py
move main.exe built/TTOManager.exe
pause
