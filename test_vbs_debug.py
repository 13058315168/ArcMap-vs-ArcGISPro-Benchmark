#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VBS脚本启动调试工具"""
import os
import sys
import subprocess

def test_vbs_execution():
    """测试VBS脚本执行"""
    print("=== VBS脚本执行测试 ===")

    # 创建一个简单的测试VBS脚本
    test_vbs = "test_run.vbs"
    with open(test_vbs, 'w', encoding='gbk') as f:
        f.write("""
' 测试VBS脚本
MsgBox "VBS脚本运行正常！", 64, "测试"
""")

    # 尝试运行测试脚本
    print("正在运行测试VBS脚本...")
    try:
        result = subprocess.run(['cscript', '//nologo', test_vbs],
                              capture_output=True, text=True, timeout=10)
        print(f"cscript返回码: {result.returncode}")
        if result.stderr:
            print(f"错误: {result.stderr}")
    except Exception as e:
        print(f"运行失败: {e}")

    # 清理测试文件
    if os.path.exists(test_vbs):
        os.remove(test_vbs)

def check_python_paths():
    """检查Python路径"""
    print("\n=== Python路径检查 ===")

    # 检查ArcGIS Pro Python
    arcgis_python = r"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
    print(f"ArcGIS Pro Python: {arcgis_python}")
    print(f"存在: {os.path.exists(arcgis_python)}")

    # 检查系统Python
    print(f"\n系统Python: {sys.executable}")
    print(f"版本: {sys.version}")

def create_simple_launcher():
    """创建简化版启动器"""
    print("\n=== 创建简化版启动器 ===")

    simple_vbs = "启动工具_简化版.vbs"
    vbs_content = """' 简化版启动器
Dim WshShell, fso, scriptPath, cmd
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' 获取脚本路径
scriptPath = fso.GetParentFolderName(WScript.ScriptFullName)

' 使用系统Python运行GUI
cmd = "python """ & scriptPath & \\\\benchmark_gui.py" & """"

' 显示命令行窗口运行（便于调试）
WshShell.Run cmd, 1, False

Set WshShell = Nothing
Set fso = Nothing
"""

    with open(simple_vbs, 'w', encoding='gbk') as f:
        f.write(vbs_content)

    print(f"已创建简化版启动器: {simple_vbs}")
    print("请双击运行此文件测试")

if __name__ == "__main__":
    test_vbs_execution()
    check_python_paths()
    create_simple_launcher()