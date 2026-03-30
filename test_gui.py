#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试GUI是否能正常启动"""
import os
import sys
import tkinter as tk
from tkinter import messagebox

def simple_test():
    """简单的GUI测试"""
    try:
        root = tk.Tk()
        root.title("GUI测试")
        root.geometry("300x200")

        label = tk.Label(root, text="GUI启动成功！", font=("Arial", 16))
        label.pack(expand=True)

        btn = tk.Button(root, text="确定", command=root.destroy)
        btn.pack(pady=20)

        root.mainloop()
        return True
    except Exception as e:
        print(f"GUI启动失败: {e}")
        return False

if __name__ == "__main__":
    print("正在测试GUI...")
    if simple_test():
        print("GUI测试通过！")
    else:
        print("GUI测试失败！")