@echo off
python.exe --version >NUL 2>&1
if errorlevel 1 goto error
echo Python.exe found in the path.
python main.py
if errorlevel 1 goto runerror
goto end

:ERROR
echo.
echo Sorry, Unable to find python. Please make sure Python is install
echo and part of your paths and try again.

:runerror
echo.
echo Sorry, unable to run the script. Please contact hess.joel@gmail.com for assistance.

:END
