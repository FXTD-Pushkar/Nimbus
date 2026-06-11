@echo off
setlocal enabledelayedexpansion
echo ========================================
echo Nimbus Houdini Batch Render UI
echo ========================================
echo.

set "TOOL_DIR=%~dp0"
set "PY_DIR=%TOOL_DIR%scripts\python"

if not exist "%PY_DIR%\batchui.cp311-win_amd64.pyd" (
    if not exist "%PY_DIR%\batchui.cp39-win_amd64.pyd" (
        if not exist "%PY_DIR%\batchui.cp37-win_amd64.pyd" (
            echo Error: no batchui pyd found in %PY_DIR%
            pause
            exit /b 1
        )
    )
)

rem --- Find newest installed Houdini (19.5 and up) ---
set "FOUND_HOUDINI="
set "BEST_VERSION="
set "BEST_PATH="

for %%v in (22 21.5 21 20.5 20.0 19.5) do (
    for /d %%d in ("C:\Program Files\Side Effects Software\Houdini %%v*") do (
        if exist "%%d\bin\hython.exe" (
            if not defined FOUND_HOUDINI (
                echo [%%v] %%d
                set "FOUND_HOUDINI=1"
                set "BEST_VERSION=%%v"
                set "BEST_PATH=%%d"
            )
        )
    )
)

if not defined FOUND_HOUDINI (
    echo No Houdini 19.5+ installation found.
    pause
    exit /b 1
)

rem --- NIMBUS_ROOT: use env if set (from user package JSON), else sibling of this tool ---
if not defined NIMBUS_ROOT (
    set "NIMBUS_PARENT=%TOOL_DIR%.."
    if "!BEST_VERSION!"=="21" if exist "!NIMBUS_PARENT!\H21_0" set "NIMBUS_ROOT=!NIMBUS_PARENT!\H21_0"
    if "!BEST_VERSION!"=="21.5" if exist "!NIMBUS_PARENT!\H21_5" set "NIMBUS_ROOT=!NIMBUS_PARENT!\H21_5"
    if "!BEST_VERSION!"=="20.5" if exist "!NIMBUS_PARENT!\H20_5" set "NIMBUS_ROOT=!NIMBUS_PARENT!\H20_5"
    if "!BEST_VERSION!"=="20.0" if exist "!NIMBUS_PARENT!\H20_0" set "NIMBUS_ROOT=!NIMBUS_PARENT!\H20_0"
    if "!BEST_VERSION!"=="19.5" if exist "!NIMBUS_PARENT!\H19_5" set "NIMBUS_ROOT=!NIMBUS_PARENT!\H19_5"
    if "!BEST_VERSION!"=="22" if exist "!NIMBUS_PARENT!\H22_0" set "NIMBUS_ROOT=!NIMBUS_PARENT!\H22_0"
)

if defined NIMBUS_ROOT (
    echo NIMBUS_ROOT=!NIMBUS_ROOT!
    set "PYTHONPATH=!NIMBUS_ROOT!\scripts\python;!PYTHONPATH!"
)

echo.
echo Found Houdini !BEST_VERSION!
echo Modules: %PY_DIR%
echo.

rem Launch compiled batchui (no .py shipped in public release)
"!BEST_PATH!\bin\hython.exe" -c "import sys; sys.path.insert(0, r'%PY_DIR%'); import batchui; batchui.main()" %*

exit /b %ERRORLEVEL%
