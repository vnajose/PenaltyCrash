@echo off
REM Atalho para iniciar o PenaltyCrash com dois cliques.
cd /d "%~dp0"

python -m pip install -r requirements.txt -q
if errorlevel 1 (
    echo.
    echo Nao foi possivel instalar as dependencias.
    echo Verifique se o Python esta instalado e tente novamente.
    pause
    exit /b 1
)

python main.py
if errorlevel 1 (
    echo.
    echo Houve um erro ao iniciar o jogo. Veja a mensagem acima.
    pause
)
