@echo off
set /p ver=gb or jp?
set /p os=ios or android?
set /p amount=How many rerolls to make?
cd source
cls
start cmd.exe /k python bot.py reroll %ver% %os% %amount%
exit