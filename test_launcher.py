#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""启动器测试工具"""
import os
import sys
import subprocess
import time

def test_direct_python():
    """直接测试Python运行"""
    print("=== 测试直接运行Python ===")

    # 测试系统Python
    print("\n1. 测试系统Python:")
    try:
        result = subprocess.run([sys.executable, "benchmark_gui.py"],
                              capture_output=True, text=True, timeout=3)
        print(f"   返回码: {result.returncode}")
        if result.stderr:
            print(f"   错误: {result.stderr[:200]}")
    except Exception as e:
        print(f"   失败: {e}")

    # 测试ArcGIS Python
    print("\n2. 测试ArcGIS Pro Python:")
    arcgis_python = r"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
    if os.path.exists(arcgis_python):
        try:
            result = subprocess.run([arcgis_python, "benchmark_gui.py"],
                                  capture_output=True, text=True, timeout=3)
            print(f"   返回码: {result.returncode}")
            if result.stderr:
                print(f"   错误: {result.stderr[:200]}")
        except Exception as e:
            print(f"   失败: {e}")
    else:
        print("   ArcGIS Pro Python 未找到")

def test_batch_files():
    """测试批处理文件"""
    print("\n=== 测试批处理文件 ===")

    batch_files = [
        "launch_gui.bat",
        "启动工具_批处理版.bat"
    ]

    for bat_file in batch_files:
        if os.path.exists(bat_file):
            print(f"\n测试 {bat_file}:")
            try:
                # 使用start命令在新窗口运行
                subprocess.run(f"start /wait cmd /c {bat_file}", shell=True, timeout=5)
                print(f"   已尝试启动 {bat_file}")
            except Exception as e:
                print(f"   失败: {e}")

def test_vbs_files():
    """测试VBS文件"""
    print("\n=== 测试VBS文件 ===")

    vbs_files = [
        "启动工具.vbs",
        "启动工具_最终版.vbs",
        "start_gui_hidden.vbs"
    ]

    for vbs_file in vbs_files:
        if os.path.exists(vbs_file):
            print(f"\n测试 {vbs_file}:")
            try:
                result = subprocess.run(['cscript', '//nologo', vbs_file],
                                      capture_output=True, text=True, timeout=5)
                print(f"   返回码: {result.returncode}")
                if result.stderr:
                    print(f"   错误: {result.stderr[:200]}")
            except Exception as e:
                print(f"   失败: {e}")

def check_environment():
    """检查环境"""
    print("\n=== 环境检查 ===")

    print(f"当前目录: {os.getcwd()}")
    print(f"Python版本: {sys.version}")
    print(f"Python路径: {sys.executable}")

    # 检查文件
    required_files = [
        "benchmark_gui.py",
        "launch_gui.bat",
        "启动工具.vbs"
    ]

    print("\n文件检查:")
    for file in required_files:
        exists = os.path.exists(file)
        size = os.path.getsize(file) if exists else 0
        print(f"   {file}: {'存在' if exists else '不存在'} ({size} bytes)")

if __name__ == "__main__":
    check_environment()
    test_direct_python()
    test_batch_files()
    test_vbs_files()

    print("\n=== 建议 ===")
    print("1. 如果批处理文件无法运行，尝试右键以管理员身份运行")
    print("2. 如果VBS文件无法运行，检查Windows Script Host是否被禁用")
    print("3. 可以直接运行: python benchmark_gui.py")