@echo off
cd /d "%~dp0"
title Trilha AOCP - Atualizar lei seca oficial (Planalto)
echo Baixando a redacao oficial das leis do edital no Planalto...
echo Isso leva alguns minutos. Nao feche esta janela.
echo.
py -3 --version >nul 2>&1
if %errorlevel%==0 (
    py -3 ferramentas\atualizar_lei_seca.py %*
) else (
    python ferramentas\atualizar_lei_seca.py %*
)
echo.
pause
