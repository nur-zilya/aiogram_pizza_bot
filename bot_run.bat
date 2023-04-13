@echo off

call %~dp0iogram_pizza_bot\venv\Scripts\activate

cd %~dp0iogram_pizza_bot

set TOKEN=

python bot_telegram.py

pause
