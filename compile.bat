REM Adds the screensaver file to a wrapper to use with Windows screensaver

@echo off
title Screensaver Compiler
cls

echo Which file would you like to build? 
echo.
dir /b *.py
echo.
set /p input= Screensaver file: 
if not exist "%input%" goto error

for %%F in ("%input%") do set "output=%%~nF.scr"

echo using System.IO; > Config.cs
echo namespace Screensaver { >> Config.cs
echo internal static class BuildConfig { >> Config.cs
echo public const string CurrentDir = @"%CD%"; >> Config.cs
echo public const string ScriptFile = @"%input%"; >> Config.cs
echo } >> Config.cs
echo } >> Config.cs

C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe /target:winexe /out:"%output%" Screensaver.cs Config.cs > NUL 2>&1

del Config.cs

echo %output% compiled!
goto ex

:error
cls
echo The file you entered does not exist!
goto ex

:ex
pause
@REM  exit