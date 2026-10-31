@echo off
cd /d "%~dp0"
title Trilha AOCP - Delegado Bahia
py -3 servidor.py
if errorlevel 1 python servidor.py
pause
