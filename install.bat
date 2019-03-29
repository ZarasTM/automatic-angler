@echo off

python -h > nul
IF %ERRORLEVEL% NEQ 0 (
	ECHO Couldnt find Python. It might have not been installed or added to enviromental variables...
	PAUSE
	exit
)

pip > nul
IF %ERRORLEVEL% NEQ 0 (
	ECHO Couldnt find pip. Try installing/reinstalling Python or pip...
	PAUSE
	exit
)

pip install pynput
pip install pillow
PAUSE