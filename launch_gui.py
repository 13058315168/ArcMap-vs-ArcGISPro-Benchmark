#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
启动器 - 自动检测Python并启动GUI
"""
import os
import sys
import subprocess

def find_python():
    """查找可用的Python解释器"""
    # 尝试的Python路径
    candidates = [
        r"C:\Python312\pythonw.exe",
        r"C:\Python311\pythonw.exe",
        r"C:\Python310\pythonw.exe",
        r"C:\Users\Administrator\AppData\Local\Programs\Python\Python312\pythonw.exe",
        r"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\pythonw.exe",
        r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\pythonw.exe",
    ]

    for path in candidates:
        if os.path.exists(path):
            return path

    # 尝试系统PATH中的pythonw
    try:
        result = subprocess.run(['where', 'pythonw'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().split('\n')[0]
    except:
        pass

    return None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gui_script = os.path.join(script_dir, 'benchmark_gui_modern.py')

    python = find_python()
    if python:
        subprocess.Popen([python, gui_script], cwd=script_dir)
    else:
        # 回退到python（会显示CMD窗口）
        subprocess.Popen(['python', gui_script], cwd=script_dir)

if __name__ == '__main__':
    main()
