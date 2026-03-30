@echo off
chcp 65001 >nul
REM ArcGIS Python Benchmark GUI Launcher - Batch Version
echo 正在启动 ArcGIS Python 性能基准测试工具...

REM Check if ArcGIS Pro Python exists
if exist "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" (
    echo 使用 ArcGIS Pro Python 运行...
    "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" "%~dp0benchmark_gui.py"
) else (
    echo 使用系统 Python 运行...
    python "%~dp0benchmark_gui.py"
)

if %errorlevel% neq 0 (
    echo.
    echo 启动失败！请确保已安装 Python。
    pause
)