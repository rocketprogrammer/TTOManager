@echo off
cd ..
py -m nuitka --onefile main.py
move min.exe built
pause
