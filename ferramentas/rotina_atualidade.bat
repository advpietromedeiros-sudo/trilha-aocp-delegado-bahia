@echo off
rem Rotina contra conteudo desatualizado (D-018): baixa de novo a lei seca oficial (Planalto), compara com a
rem anterior e grava revisao\relatorios\AAAA-MM-DD.txt. Nao agenda nada: o comando para agendar esta no relatorio,
rem e agendar e decisao do titular. Sem "pause" de proposito, para poder rodar agendada.
cd /d "%~dp0.."
py -3 --version >nul 2>&1
if %errorlevel%==0 (
    py -3 ferramentas\verificar_atualidade.py --rotina
) else (
    python ferramentas\verificar_atualidade.py --rotina
)
exit /b %errorlevel%
