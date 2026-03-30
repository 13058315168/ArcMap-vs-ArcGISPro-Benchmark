#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ArcGIS Python Performance Benchmark - Modern UI Design
现代化美观界面设计 - Material Design风格
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import subprocess
import threading
import json
import time
import webbrowser
from datetime import datetime, timedelta

try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext, filedialog, messagebox
except ImportError:
    import Tkinter as tk
    import ttk
    from ScrolledText import ScrolledText
    import tkFileDialog as filedialog
    import tkMessageBox as messagebox

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from utils.settings_manager import SettingsManager, get_text, DEFAULT_CONFIG

# 现代化配色方案 - Material Design
COLORS = {
    'bg_primary': '#f5f7fa',       # 主背景色 - 浅灰蓝
    'bg_secondary': '#ffffff',     # 卡片背景 - 纯白
    'bg_header': '#1a237e',        # 头部深蓝
    'accent_primary': '#3949ab',   # 主强调色 - 靛蓝
    'accent_secondary': '#5c6bc0', # 次强调色
    'accent_success': '#43a047',   # 成功绿
    'accent_warning': '#fb8c00',   # 警告橙
    'accent_danger': '#e53935',    # 危险红
    'text_primary': '#212121',     # 主文字 - 深灰
    'text_secondary': '#757575',   # 次文字 - 中灰
    'text_light': '#ffffff',       # 浅色文字
    'border': '#e0e0e0',           # 边框色
    'hover': '#e8eaf6',            # 悬停色
}


class ModernButton(tk.Canvas):
    """圆角按钮控件"""
    def __init__(self, parent, text, command=None, bg_color=None, fg_color=None,
                 width=120, height=40, radius=8, font_size=12, bold=True, **kwargs):
        self.bg_color = bg_color or COLORS['accent_primary']
        self.fg_color = fg_color or COLORS['text_light']
        self.hover_color = self._lighten_color(self.bg_color)
        self.pressed_color = self._darken_color(self.bg_color)
        self.command = command
        self.radius = radius

        super().__init__(parent, width=width, height=height, bg=parent.cget('bg'),
                        highlightthickness=0, cursor='hand2', **kwargs)

        self.font = ('Microsoft YaHei', font_size, 'bold' if bold else 'normal')
        self.text = text

        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        self.bind('<Button-1>', self._on_press)
        self.bind('<ButtonRelease-1>', self._on_release)

        self._draw_button(self.bg_color)

    def _lighten_color(self, hex_color, factor=0.15):
        """变亮颜色"""
        r = int(min(255, int(hex_color[1:3], 16) + 255 * factor))
        g = int(min(255, int(hex_color[3:5], 16) + 255 * factor))
        b = int(min(255, int(hex_color[5:7], 16) + 255 * factor))
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def _darken_color(self, hex_color, factor=0.15):
        """变暗颜色"""
        r = int(max(0, int(hex_color[1:3], 16) - 255 * factor))
        g = int(max(0, int(hex_color[3:5], 16) - 255 * factor))
        b = int(max(0, int(hex_color[5:7], 16) - 255 * factor))
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def _draw_button(self, color):
        """绘制圆角按钮"""
        self.delete('all')
        width = self.winfo_width()
        height = self.winfo_height()

        # 绘制圆角矩形
        self.create_rounded_rect(2, 2, width-2, height-2, self.radius, fill=color, outline='')

        # 添加文字
        self.create_text(width//2, height//2, text=self.text, fill=self.fg_color,
                        font=self.font, anchor='center')

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        """创建圆角矩形"""
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_enter(self, event):
        self._draw_button(self.hover_color)

    def _on_leave(self, event):
        self._draw_button(self.bg_color)

    def _on_press(self, event):
        self._draw_button(self.pressed_color)

    def _on_release(self, event):
        self._draw_button(self.hover_color)
        if self.command:
            self.command()

    def config(self, **kwargs):
        """配置按钮属性"""
        if 'text' in kwargs:
            self.text = kwargs['text']
            self._draw_button(self.bg_color)
        if 'state' in kwargs:
            state = kwargs['state']
            if state == 'disabled':
                self.unbind('<Enter>')
                self.unbind('<Leave>')
                self.unbind('<Button-1>')
                self.unbind('<ButtonRelease-1>')
                self.config(cursor='')
                # 灰色显示
                gray = '#9e9e9e'
                self.delete('all')
                width = self.winfo_width()
                height = self.winfo_height()
                self.create_rounded_rect(2, 2, width-2, height-2, self.radius, fill=gray, outline='')
                self.create_text(width//2, height//2, text=self.text, fill=self.fg_color,
                                font=self.font, anchor='center')
            elif state == 'normal':
                self.bind('<Enter>', self._on_enter)
                self.bind('<Leave>', self._on_leave)
                self.bind('<Button-1>', self._on_press)
                self.bind('<ButtonRelease-1>', self._on_release)
                self.config(cursor='hand2')
                self._draw_button(self.bg_color)


class CardFrame(tk.Frame):
    """卡片式框架"""
    def __init__(self, parent, title=None, **kwargs):
        super().__init__(parent, bg=COLORS['bg_secondary'], **kwargs)

        # 添加阴影效果（通过边框模拟）
        self.config(highlightbackground=COLORS['border'], highlightthickness=1)

        if title:
            self.title_label = tk.Label(
                self, text=title, bg=COLORS['bg_secondary'],
                fg=COLORS['accent_primary'], font=('Microsoft YaHei', 14, 'bold'),
                anchor='w', padx=15, pady=10
            )
            self.title_label.pack(fill='x')

            # 分隔线
            separator = tk.Frame(self, height=2, bg=COLORS['border'])
            separator.pack(fill='x', padx=15)


class SettingsDialog(tk.Toplevel):
    """设置对话框"""

    def __init__(self, parent, settings_manager):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.sm = settings_manager
        self.title(self.sm.get_text('settings_title'))
        self.geometry("900x700")
        self.minsize(800, 600)
        self.configure(bg=COLORS['bg_primary'])

        # Make dialog modal
        self.transient(parent)
        self.grab_set()

        self._create_styles()
        self._create_ui()
        self._load_settings()

        # Center dialog
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_y() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry("+{}+{}".format(x, y))

    def _create_styles(self):
        """创建ttk样式"""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # 配置样式使用与主窗口一致的字体
        base_size = int(12 * self.sm.get('ui_settings.font_scale', 1.0))

        self.style.configure('Modern.TFrame', background=COLORS['bg_primary'])
        self.style.configure('Card.TFrame', background=COLORS['bg_secondary'])

        self.style.configure('Modern.TLabel',
                           background=COLORS['bg_primary'],
                           foreground=COLORS['text_primary'],
                           font=('Microsoft YaHei', base_size))

        self.style.configure('Modern.TButton',
                           font=('Microsoft YaHei', base_size),
                           padding=5)

        self.style.configure('Modern.TCheckbutton',
                           font=('Microsoft YaHei', base_size),
                           background=COLORS['bg_secondary'])

        self.style.configure('Modern.TLabelframe',
                           background=COLORS['bg_secondary'],
                           font=('Microsoft YaHei', base_size, 'bold'))

        self.style.configure('Modern.TLabelframe.Label',
                           font=('Microsoft YaHei', base_size, 'bold'),
                           background=COLORS['bg_secondary'])

    def _create_ui(self):
        """创建设置对话框UI"""
        # 主容器
        main_frame = tk.Frame(self, bg=COLORS['bg_primary'], padx=20, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Notebook (tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Create tabs
        self.tab_basic = tk.Frame(self.notebook, bg=COLORS['bg_secondary'], padx=15, pady=15)
        self.tab_scale = tk.Frame(self.notebook, bg=COLORS['bg_secondary'], padx=15, pady=15)
        self.tab_results = tk.Frame(self.notebook, bg=COLORS['bg_secondary'], padx=15, pady=15)

        self.notebook.add(self.tab_basic, text=self.sm.get_text('tab_basic'))
        self.notebook.add(self.tab_scale, text=self.sm.get_text('tab_data_scale'))
        self.notebook.add(self.tab_results, text=self.sm.get_text('tab_results'))

        # Build each tab
        self._create_basic_tab()
        self._create_scale_tab()
        self._create_results_tab()

        # Buttons at bottom
        btn_frame = tk.Frame(main_frame, bg=COLORS['bg_primary'], height=60)
        btn_frame.pack(fill=tk.X, pady=(5, 0))
        btn_frame.pack_propagate(False)

        # Use standard tk buttons for settings dialog to avoid Canvas rendering issues
        tk.Button(
            btn_frame,
            text=self.sm.get_text('btn_save_settings'),
            bg=COLORS['accent_success'],
            fg=COLORS['text_light'],
            font=('Microsoft YaHei', 11),
            relief='flat',
            cursor='hand2',
            width=12, height=1,
            command=self._save_settings
        ).pack(side=tk.RIGHT, padx=5, pady=10)

        tk.Button(
            btn_frame,
            text=self.sm.get_text('btn_reset'),
            bg=COLORS['accent_warning'],
            fg=COLORS['text_light'],
            font=('Microsoft YaHei', 11),
            relief='flat',
            cursor='hand2',
            width=12, height=1,
            command=self._reset_defaults
        ).pack(side=tk.RIGHT, padx=5, pady=10)

        tk.Button(
            btn_frame,
            text=self.sm.get_text('menu_exit'),
            bg=COLORS['text_secondary'],
            fg=COLORS['text_light'],
            font=('Microsoft YaHei', 11),
            relief='flat',
            cursor='hand2',
            width=12, height=1,
            command=self.destroy
        ).pack(side=tk.RIGHT, padx=5, pady=10)

    def _create_basic_tab(self):
        """创建基本设置标签页"""
        # Language selection
        lang_frame = tk.LabelFrame(self.tab_basic, text=self.sm.get_text('label_language'),
                                   bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                                   font=('Microsoft YaHei', 12, 'bold'), padx=10, pady=10)
        lang_frame.pack(fill=tk.X, pady=(0, 15))

        self.lang_var = tk.StringVar(value=self.sm.get('language', 'zh'))
        tk.Radiobutton(lang_frame, text="中文", variable=self.lang_var, value='zh',
                      bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary']).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(lang_frame, text="English", variable=self.lang_var, value='en',
                      bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary']).pack(side=tk.LEFT, padx=10)

        # Python paths
        paths_frame = tk.LabelFrame(self.tab_basic, text="Python " + self.sm.get_text('menu_settings'),
                                    bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                                    font=('Microsoft YaHei', 12, 'bold'), padx=10, pady=10)
        paths_frame.pack(fill=tk.X, pady=(0, 15))

        # Python 2.7
        py27_frame = tk.Frame(paths_frame, bg=COLORS['bg_secondary'])
        py27_frame.pack(fill=tk.X, pady=5)

        tk.Label(py27_frame, text=self.sm.get_text('label_python27'), width=18,
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11), anchor='w').pack(side=tk.LEFT)
        self.py27_var = tk.StringVar(value=self.sm.get('python_paths.python27', ''))
        tk.Entry(py27_frame, textvariable=self.py27_var, font=('Microsoft YaHei', 11),
                bg='white', fg=COLORS['text_primary'], relief='solid', bd=1).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ModernButton(py27_frame, text=self.sm.get_text('btn_browse'), bg_color=COLORS['accent_secondary'],
                    width=80, height=30, font_size=10,
                    command=lambda: self._browse_python(self.py27_var)).pack(side=tk.LEFT, padx=2)
        ModernButton(py27_frame, text=self.sm.get_text('btn_verify'), bg_color=COLORS['accent_primary'],
                    width=80, height=30, font_size=10,
                    command=lambda: self._verify_python(self.py27_var.get(), '2.7')).pack(side=tk.LEFT, padx=2)

        # Python 3.x
        py3_frame = tk.Frame(paths_frame, bg=COLORS['bg_secondary'])
        py3_frame.pack(fill=tk.X, pady=5)

        tk.Label(py3_frame, text=self.sm.get_text('label_python3'), width=18,
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11), anchor='w').pack(side=tk.LEFT)
        self.py3_var = tk.StringVar(value=self.sm.get('python_paths.python3', ''))
        tk.Entry(py3_frame, textvariable=self.py3_var, font=('Microsoft YaHei', 11),
                bg='white', fg=COLORS['text_primary'], relief='solid', bd=1).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ModernButton(py3_frame, text=self.sm.get_text('btn_browse'), bg_color=COLORS['accent_secondary'],
                    width=80, height=30, font_size=10,
                    command=lambda: self._browse_python(self.py3_var)).pack(side=tk.LEFT, padx=2)
        ModernButton(py3_frame, text=self.sm.get_text('btn_verify'), bg_color=COLORS['accent_primary'],
                    width=80, height=30, font_size=10,
                    command=lambda: self._verify_python(self.py3_var.get(), '3.x')).pack(side=tk.LEFT, padx=2)

        # Test settings
        test_frame = tk.LabelFrame(self.tab_basic, text=self.sm.get_text('settings_title'),
                                   bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                                   font=('Microsoft YaHei', 12, 'bold'), padx=10, pady=10)
        test_frame.pack(fill=tk.X, pady=(0, 15))

        # Runs
        runs_frame = tk.Frame(test_frame, bg=COLORS['bg_secondary'])
        runs_frame.pack(fill=tk.X, pady=5)
        tk.Label(runs_frame, text=self.sm.get_text('label_runs'), width=18,
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11), anchor='w').pack(side=tk.LEFT)
        self.runs_var = tk.IntVar(value=self.sm.get('test_settings.runs', 3))
        tk.Spinbox(runs_frame, from_=1, to=10, textvariable=self.runs_var, width=10,
                  font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)

        # Warmup
        warmup_frame = tk.Frame(test_frame, bg=COLORS['bg_secondary'])
        warmup_frame.pack(fill=tk.X, pady=5)
        tk.Label(warmup_frame, text=self.sm.get_text('label_warmup'), width=18,
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11), anchor='w').pack(side=tk.LEFT)
        self.warmup_var = tk.IntVar(value=self.sm.get('test_settings.warmup', 1))
        tk.Spinbox(warmup_frame, from_=0, to=5, textvariable=self.warmup_var, width=10,
                  font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)

        # Multiprocess
        self.mp_var = tk.BooleanVar(value=self.sm.get('test_settings.enable_multiprocess', False))
        mp_frame2 = tk.Frame(test_frame, bg='white', padx=8, pady=5,
                            highlightbackground=COLORS['border'], highlightthickness=1)
        mp_frame2.pack(fill=tk.X, pady=5)
        tk.Checkbutton(mp_frame2, text=self.sm.get_text('chk_multiprocess'), variable=self.mp_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 12), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

        # Workers
        workers_frame = tk.Frame(test_frame, bg=COLORS['bg_secondary'])
        workers_frame.pack(fill=tk.X, pady=5)
        tk.Label(workers_frame, text=self.sm.get_text('label_workers'), width=18,
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11), anchor='w').pack(side=tk.LEFT)
        self.workers_var = tk.IntVar(value=self.sm.get('test_settings.mp_workers', 4))
        tk.Spinbox(workers_frame, from_=2, to=16, textvariable=self.workers_var, width=10,
                  font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)

        # Open-source
        self.os_var = tk.BooleanVar(value=self.sm.get('test_settings.enable_opensource', False))
        os_frame2 = tk.Frame(test_frame, bg='white', padx=8, pady=5,
                            highlightbackground=COLORS['border'], highlightthickness=1)
        os_frame2.pack(fill=tk.X, pady=5)
        tk.Checkbutton(os_frame2, text=self.sm.get_text('chk_opensource'), variable=self.os_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 12), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

    def _create_scale_tab(self):
        """创建数据规模标签页"""
        # Scale selection
        scale_select_frame = tk.Frame(self.tab_scale, bg=COLORS['bg_secondary'])
        scale_select_frame.pack(fill=tk.X, pady=(0, 15))

        tk.Label(scale_select_frame, text=self.sm.get_text('label_scale'),
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)
        self.edit_scale_var = tk.StringVar(value=self.sm.get('test_settings.data_scale', 'tiny'))

        scale_menu = tk.OptionMenu(scale_select_frame, self.edit_scale_var,
                                   *['tiny', 'small', 'standard', 'medium', 'large'])
        scale_menu.config(font=('Microsoft YaHei', 11), bg=COLORS['bg_secondary'],
                         fg=COLORS['text_primary'], relief='solid', bd=1,
                         highlightbackground=COLORS['border'], highlightthickness=1)
        scale_menu.pack(side=tk.LEFT, padx=5)
        self.edit_scale_var.trace('w', lambda *args: self._load_scale_settings())

        ModernButton(scale_select_frame, text=self.sm.get_text('btn_reset'),
                    bg_color=COLORS['accent_secondary'], width=120, height=32, font_size=11,
                    command=self._reset_current_scale).pack(side=tk.LEFT, padx=20)

        # Parameter fields
        params_frame = tk.Frame(self.tab_scale, bg=COLORS['bg_secondary'])
        params_frame.pack(fill=tk.BOTH, expand=True)

        params = [
            ('fishnet_rows', self.sm.get_text('param_fishnet')),
            ('random_points', self.sm.get_text('param_random_points')),
            ('buffer_points', self.sm.get_text('param_buffer')),
            ('intersect_features', self.sm.get_text('param_intersect')),
            ('spatial_join_points', self.sm.get_text('param_spatial_join')),
            ('calculate_field_records', self.sm.get_text('param_calculate')),
            ('constant_raster_size', self.sm.get_text('param_raster')),
        ]

        self.scale_param_vars = {}
        for key, label in params:
            frame = tk.Frame(params_frame, bg=COLORS['bg_secondary'])
            frame.pack(fill=tk.X, pady=8)

            tk.Label(frame, text=label, width=30,
                    bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                    font=('Microsoft YaHei', 11), anchor='w').pack(side=tk.LEFT)
            var = tk.IntVar()
            self.scale_param_vars[key] = var
            tk.Spinbox(frame, from_=1, to=10000000, textvariable=var, width=15,
                      font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)

        self._load_scale_settings()

    def _create_results_tab(self):
        """创建结果设置标签页"""
        # Result save options
        save_frame = tk.LabelFrame(self.tab_results, text=self.sm.get_text('tab_results'),
                                   bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                                   font=('Microsoft YaHei', 12, 'bold'), padx=10, pady=10)
        save_frame.pack(fill=tk.X, pady=(0, 15))

        self.save_py2_var = tk.BooleanVar(value=self.sm.get('result_settings.save_py2_results', True))
        cb_frame1 = tk.Frame(save_frame, bg='white', padx=8, pady=4,
                            highlightbackground=COLORS['border'], highlightthickness=1)
        cb_frame1.pack(fill=tk.X, pady=3)
        tk.Checkbutton(cb_frame1, text=self.sm.get_text('chk_py2'), variable=self.save_py2_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

        self.save_py3_var = tk.BooleanVar(value=self.sm.get('result_settings.save_py3_results', True))
        cb_frame2 = tk.Frame(save_frame, bg='white', padx=8, pady=4,
                            highlightbackground=COLORS['border'], highlightthickness=1)
        cb_frame2.pack(fill=tk.X, pady=3)
        tk.Checkbutton(cb_frame2, text=self.sm.get_text('chk_py3'), variable=self.save_py3_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

        self.save_os_var = tk.BooleanVar(value=self.sm.get('result_settings.save_os_results', True))
        cb_frame3 = tk.Frame(save_frame, bg='white', padx=8, pady=4,
                            highlightbackground=COLORS['border'], highlightthickness=1)
        cb_frame3.pack(fill=tk.X, pady=3)
        tk.Checkbutton(cb_frame3, text=self.sm.get_text('chk_os'), variable=self.save_os_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

        # Timestamp folder option
        self.timestamp_var = tk.BooleanVar(value=self.sm.get('result_settings.use_timestamp_folder', True))
        ts_frame = tk.Frame(self.tab_results, bg='white', padx=8, pady=5,
                           highlightbackground=COLORS['border'], highlightthickness=1)
        ts_frame.pack(fill=tk.X, pady=10)
        tk.Checkbutton(ts_frame, text=self.sm.get_text('chk_timestamp_folder'), variable=self.timestamp_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

        # Remember settings option
        self.remember_var = tk.BooleanVar(value=self.sm.get('ui_settings.remember_last_settings', True))
        rs_frame = tk.Frame(self.tab_results, bg='white', padx=8, pady=5,
                           highlightbackground=COLORS['border'], highlightthickness=1)
        rs_frame.pack(fill=tk.X, pady=10)
        tk.Checkbutton(rs_frame, text=self.sm.get_text('chk_remember_settings'), variable=self.remember_var,
                      bg='white', fg=COLORS['text_primary'],
                      font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary'],
                      activebackground='white', cursor='hand2').pack(anchor=tk.W)

        # Retention days
        retention_frame = tk.Frame(self.tab_results, bg=COLORS['bg_secondary'])
        retention_frame.pack(fill=tk.X, pady=10)

        tk.Label(retention_frame, text=self.sm.get_text('label_retention'),
                bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)
        self.retention_var = tk.IntVar(value=self.sm.get('result_settings.retention_days', 30))
        tk.Spinbox(retention_frame, from_=0, to=365, textvariable=self.retention_var, width=10,
                  font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)
        tk.Label(retention_frame, text=self.sm.get_text('retention_forever'),
                bg=COLORS['bg_secondary'], fg=COLORS['text_secondary'],
                font=('Microsoft YaHei', 11)).pack(side=tk.LEFT, padx=5)

        # Font scale
        font_frame = tk.LabelFrame(self.tab_results, text=self.sm.get_text('label_font_scale'),
                                   bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                                   font=('Microsoft YaHei', 12, 'bold'), padx=10, pady=10)
        font_frame.pack(fill=tk.X, pady=10)

        self.font_scale_var = tk.DoubleVar(value=self.sm.get('ui_settings.font_scale', 1.0))
        font_options = [
            (self.sm.get_text('font_scale_small'), 1.0),
            (self.sm.get_text('font_scale_normal'), 1.2),
            (self.sm.get_text('font_scale_large'), 1.5),
            (self.sm.get_text('font_scale_huge'), 2.0),
        ]
        for text, value in font_options:
            tk.Radiobutton(font_frame, text=text, variable=self.font_scale_var, value=value,
                          bg=COLORS['bg_secondary'], fg=COLORS['text_primary'],
                          font=('Microsoft YaHei', 11), selectcolor=COLORS['accent_primary']).pack(anchor=tk.W, pady=3)

    def _browse_python(self, var):
        """浏览选择Python可执行文件"""
        filename = filedialog.askopenfilename(
            title=self.sm.get_text('label_python27'),
            filetypes=[("Python Executable", "python.exe"), ("All Files", "*.*")]
        )
        if filename:
            var.set(filename)

    def _verify_python(self, path, version):
        """验证Python环境"""
        if not path or not os.path.exists(path):
            messagebox.showerror(
                self.sm.get_text('status_error'),
                self.sm.get_text('msg_invalid_python')
            )
            return

        def verify():
            try:
                result = subprocess.run(
                    [path, "-c", "import sys; print(sys.version)"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode == 0:
                    messagebox.showinfo(
                        self.sm.get_text('msg_verify_ok'),
                        "Python {}:\n{}".format(version, result.stdout.strip())
                    )
                else:
                    messagebox.showerror(
                        self.sm.get_text('msg_verify_fail'),
                        result.stderr
                    )
            except Exception as e:
                messagebox.showerror(
                    self.sm.get_text('msg_verify_fail'),
                    str(e)
                )

        threading.Thread(target=verify).start()

    def _load_settings(self):
        """加载所有设置到UI"""
        self._load_scale_settings()

    def _load_scale_settings(self):
        """加载当前规模的设置"""
        scale = self.edit_scale_var.get()
        config = self.sm.get_scale_config(scale)

        for key, var in self.scale_param_vars.items():
            if key in config:
                var.set(config[key])

    def _reset_current_scale(self):
        """重置当前规模为默认值"""
        scale = self.edit_scale_var.get()
        defaults = DEFAULT_CONFIG['data_scale_custom'].get(scale, {})
        for key, var in self.scale_param_vars.items():
            if key in defaults:
                var.set(defaults[key])

    def _save_settings(self):
        """保存所有设置"""
        # Basic settings
        self.sm.set('language', self.lang_var.get())
        self.sm.set('python_paths.python27', self.py27_var.get())
        self.sm.set('python_paths.python3', self.py3_var.get())
        self.sm.set('test_settings.runs', self.runs_var.get())
        self.sm.set('test_settings.warmup', self.warmup_var.get())
        self.sm.set('test_settings.enable_multiprocess', self.mp_var.get())
        self.sm.set('test_settings.mp_workers', self.workers_var.get())
        self.sm.set('test_settings.enable_opensource', self.os_var.get())

        # Scale settings
        scale = self.edit_scale_var.get()
        for key, var in self.scale_param_vars.items():
            self.sm.set_scale_config(scale, key, var.get())

        # Result settings
        self.sm.set('result_settings.save_py2_results', self.save_py2_var.get())
        self.sm.set('result_settings.save_py3_results', self.save_py3_var.get())
        self.sm.set('result_settings.save_os_results', self.save_os_var.get())
        self.sm.set('result_settings.use_timestamp_folder', self.timestamp_var.get())
        self.sm.set('result_settings.retention_days', self.retention_var.get())

        # UI settings
        self.sm.set('ui_settings.remember_last_settings', self.remember_var.get())
        self.sm.set('ui_settings.font_scale', self.font_scale_var.get())

        if self.sm.save_config():
            messagebox.showinfo(
                self.sm.get_text('msg_config_saved'),
                self.sm.get_text('msg_config_saved')
            )
            self.parent._on_settings_changed()
            # Notify to restart for font scale to take effect
            if self.font_scale_var.get() != self.parent.font_scale:
                messagebox.showinfo(
                    "Restart Required",
                    "Font scale changes will take effect after restart."
                )
        else:
            messagebox.showerror(
                self.sm.get_text('status_error'),
                "Failed to save configuration"
            )

    def _reset_defaults(self):
        """重置所有设置为默认值"""
        if messagebox.askyesno(
            self.sm.get_text('btn_reset'),
            "Reset all settings to default values?"
        ):
            self.sm.reset_to_defaults()
            self._load_settings()
            messagebox.showinfo(
                self.sm.get_text('msg_config_saved'),
                self.sm.get_text('msg_config_loaded')
            )


class ModernBenchmarkGUI(object):
    """现代化主GUI类"""

    def __init__(self, root):
        self.root = root
        self.sm = SettingsManager()
        self.font_scale = self.sm.get('ui_settings.font_scale', 1.0)

        # 自动检测Python路径（如果未设置）
        if not self.sm.get('python_paths.python27') or not self.sm.get('python_paths.python3'):
            detected = self.sm.auto_detect_python_paths()
            if detected['python27'] or detected['python3']:
                self.sm.save_config()

        # 状态变量
        self.is_running = False
        self.should_stop = False
        self.current_process = None
        self.start_time = None
        self.completed_tests = 0
        self.total_tests = 0
        self.test_queue = []

        self._setup_window()
        self._create_styles()
        self._create_ui()
        self._update_language()

    def _setup_window(self):
        """设置窗口"""
        self.root.title(self.sm.get_text('app_title'))
        self.root.geometry("1400x900")
        self.root.minsize(1200, 700)
        self.root.configure(bg=COLORS['bg_primary'])

        # 设置DPI感知
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

        # 设置图标
        icon_path = os.path.join(SCRIPT_DIR, 'resources', 'icon.ico')
        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)
            except:
                pass

        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_styles(self):
        """创建ttk样式"""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        base_size = int(12 * self.font_scale)

        # 自定义样式
        self.style.configure('Modern.TFrame', background=COLORS['bg_primary'])
        self.style.configure('Card.TFrame', background=COLORS['bg_secondary'])

        self.style.configure('Modern.TLabel',
                           background=COLORS['bg_primary'],
                           foreground=COLORS['text_primary'],
                           font=('Microsoft YaHei', base_size))

        self.style.configure('Title.TLabel',
                           background=COLORS['bg_header'],
                           foreground=COLORS['text_light'],
                           font=('Microsoft YaHei', int(24 * self.font_scale), 'bold'))

        self.style.configure('CardTitle.TLabel',
                           background=COLORS['bg_secondary'],
                           foreground=COLORS['accent_primary'],
                           font=('Microsoft YaHei', int(14 * self.font_scale), 'bold'))

        # 进度条样式
        self.style.configure('Modern.Horizontal.TProgressbar',
                           background=COLORS['accent_primary'],
                           troughcolor=COLORS['border'],
                           borderwidth=0,
                           thickness=int(20 * self.font_scale))

    def _font(self, size, bold=False, color=None):
        """获取字体配置"""
        scaled_size = int(size * self.font_scale)
        weight = 'bold' if bold else 'normal'
        return ('Microsoft YaHei', scaled_size, weight)

    def _create_ui(self):
        """创建主UI"""
        # 顶部标题栏
        self._create_header()

        # 主内容区
        main_container = tk.Frame(self.root, bg=COLORS['bg_primary'])
        main_container.pack(fill='both', expand=True, padx=20, pady=15)

        # 左侧控制面板
        left_panel = tk.Frame(main_container, bg=COLORS['bg_primary'])
        left_panel.pack(side='left', fill='y', padx=(0, 15))

        # 右侧内容区
        right_panel = tk.Frame(main_container, bg=COLORS['bg_primary'])
        right_panel.pack(side='left', fill='both', expand=True)

        # 左侧卡片
        self._create_quick_settings_card(left_panel)
        self._create_test_options_card(left_panel)

        # 右侧卡片
        self._create_progress_card(right_panel)
        self._create_log_card(right_panel)

        # 底部状态栏
        self._create_status_bar()

    def _create_header(self):
        """创建现代化头部"""
        header = tk.Frame(self.root, bg=COLORS['bg_header'], height=int(80 * self.font_scale))
        header.pack(fill='x')
        header.pack_propagate(False)

        # Logo区域
        logo_frame = tk.Frame(header, bg=COLORS['bg_header'])
        logo_frame.pack(side='left', padx=20, pady=10)

        # 图标（使用emoji或文字）
        icon_label = tk.Label(logo_frame, text='', bg=COLORS['bg_header'],
                             fg=COLORS['text_light'], font=('Segoe UI Emoji', int(32 * self.font_scale)))
        icon_label.pack(side='left', padx=(0, 10))

        # 标题
        title_frame = tk.Frame(logo_frame, bg=COLORS['bg_header'])
        title_frame.pack(side='left')

        self.title_label = tk.Label(title_frame, text='', bg=COLORS['bg_header'],
                                   fg=COLORS['text_light'], font=self._font(20, bold=True))
        self.title_label.pack(anchor='w')

        self.subtitle_label = tk.Label(title_frame, text='Performance Benchmark Tool',
                           bg=COLORS['bg_header'], fg='#9fa8da', font=self._font(11))
        self.subtitle_label.pack(anchor='w')

        # 右侧工具按钮
        tools_frame = tk.Frame(header, bg=COLORS['bg_header'])
        tools_frame.pack(side='right', padx=20)

        # 设置按钮
        ModernButton(tools_frame, text=' Settings', bg_color=COLORS['accent_secondary'],
                    width=100, height=36, font_size=11,
                    command=self._open_settings).pack(side='right', padx=5)

        # 语言切换按钮
        self.lang_btn = tk.Button(tools_frame, text='English', bg=COLORS['accent_secondary'],
                                 fg=COLORS['text_light'], relief='flat', cursor='hand2',
                                 font=self._font(11), padx=15, pady=5,
                                 command=self._toggle_language)
        self.lang_btn.pack(side='right', padx=5)

    def _create_quick_settings_card(self, parent):
        """快速设置卡片"""
        card = CardFrame(parent, title=' Quick Settings')
        card.pack(fill='x', pady=(0, 15), ipadx=10, ipady=10)

        # 数据规模
        scale_frame = tk.Frame(card, bg=COLORS['bg_secondary'])
        scale_frame.pack(fill='x', padx=15, pady=10)

        tk.Label(scale_frame, text=self.sm.get_text('label_scale_select'),
                bg=COLORS['bg_secondary'], fg=COLORS['text_secondary'],
                font=self._font(11)).pack(anchor='w')

        self.scale_var = tk.StringVar(value=self.sm.get('test_settings.data_scale', 'tiny'))
        scale_names = {
            'tiny': self.sm.get_text('scale_tiny'),
            'small': self.sm.get_text('scale_small'),
            'standard': self.sm.get_text('scale_standard'),
            'medium': self.sm.get_text('scale_medium'),
            'large': self.sm.get_text('scale_large')
        }

        self.scale_menu = tk.OptionMenu(scale_frame, self.scale_var,
                                       *[scale_names[k] for k in ['tiny', 'small', 'standard', 'medium', 'large']])
        self.scale_menu.config(font=self._font(12), bg=COLORS['bg_secondary'],
                              fg=COLORS['text_primary'], relief='flat',
                              highlightbackground=COLORS['border'], highlightthickness=1)
        self.scale_menu.pack(fill='x', pady=(5, 0))

    def _create_test_options_card(self, parent):
        """测试选项卡片"""
        card = CardFrame(parent, title=' Test Options')
        card.pack(fill='x', pady=(0, 15), ipadx=10, ipady=10)

        content = tk.Frame(card, bg=COLORS['bg_secondary'])
        content.pack(fill='x', padx=15, pady=10)

        # 多进程选项
        self.mp_var = tk.BooleanVar(value=self.sm.get('test_settings.enable_multiprocess', False))
        mp_frame = tk.Frame(content, bg='white', padx=10, pady=8,
                           highlightbackground=COLORS['border'], highlightthickness=1)
        mp_frame.pack(fill='x', pady=5)
        mp_check = tk.Checkbutton(mp_frame, text=self.sm.get_text('chk_multiprocess'),
                                 variable=self.mp_var, bg='white',
                                 fg=COLORS['text_primary'], font=self._font(13),
                                 selectcolor=COLORS['accent_primary'],
                                 activebackground='white', cursor='hand2')
        mp_check.pack(anchor='w')

        # 开源库选项
        self.os_var = tk.BooleanVar(value=self.sm.get('test_settings.enable_opensource', False))
        os_frame = tk.Frame(content, bg='white', padx=10, pady=8,
                           highlightbackground=COLORS['border'], highlightthickness=1)
        os_frame.pack(fill='x', pady=5)
        os_check = tk.Checkbutton(os_frame, text=self.sm.get_text('chk_opensource'),
                                 variable=self.os_var, bg='white',
                                 fg=COLORS['text_primary'], font=self._font(13),
                                 selectcolor=COLORS['accent_primary'],
                                 activebackground='white', cursor='hand2')
        os_check.pack(anchor='w')

        # 打开文件夹按钮
        folder_btn = tk.Button(content, text=' Open Temp Folder',
                              bg=COLORS['bg_primary'], fg=COLORS['accent_primary'],
                              relief='flat', font=self._font(11), cursor='hand2',
                              command=self._open_temp_folder)
        folder_btn.pack(fill='x', pady=(15, 0), ipady=8)

    def _create_progress_card(self, parent):
        """进度卡片"""
        card = CardFrame(parent, title=' Progress')
        card.pack(fill='x', pady=(0, 15), ipadx=10, ipady=10)

        content = tk.Frame(card, bg=COLORS['bg_secondary'])
        content.pack(fill='x', padx=15, pady=10)

        # 总进度
        tk.Label(content, text=self.sm.get_text('progress_total'),
                bg=COLORS['bg_secondary'], fg=COLORS['text_secondary'],
                font=self._font(11)).pack(anchor='w')

        self.total_progress = ttk.Progressbar(content, style='Modern.Horizontal.TProgressbar',
                                             mode='determinate', length=100)
        self.total_progress.pack(fill='x', pady=(5, 15))

        # 当前测试
        tk.Label(content, text=self.sm.get_text('progress_current'),
                bg=COLORS['bg_secondary'], fg=COLORS['text_secondary'],
                font=self._font(11)).pack(anchor='w')

        self.current_test_label = tk.Label(content, text=self.sm.get_text('status_ready'),
                                          bg=COLORS['bg_secondary'],
                                          fg=COLORS['text_primary'],
                                          font=self._font(14, bold=True))
        self.current_test_label.pack(anchor='w', pady=(5, 0))

        self.eta_label = tk.Label(content, text='',
                                 bg=COLORS['bg_secondary'],
                                 fg=COLORS['text_secondary'], font=self._font(11))
        self.eta_label.pack(anchor='w')

        # 控制按钮区
        btn_frame = tk.Frame(content, bg=COLORS['bg_secondary'])
        btn_frame.pack(fill='x', pady=(20, 0))

        # 现代化按钮
        self.run_btn = ModernButton(btn_frame, text=' Start Test',
                                   bg_color=COLORS['accent_success'],
                                   width=180, height=50, font_size=14,
                                   command=self._start_test)
        self.run_btn.pack(side='left', padx=(0, 10))

        self.run_all_btn = ModernButton(btn_frame, text=' Run All Scales',
                                       bg_color=COLORS['accent_warning'],
                                       width=180, height=50, font_size=14,
                                       command=self._start_all_scales)
        self.run_all_btn.pack(side='left', padx=(0, 10))

        self.stop_btn = ModernButton(btn_frame, text=' Stop',
                                    bg_color=COLORS['accent_danger'],
                                    width=180, height=50, font_size=14,
                                    command=self._stop_test)
        self.stop_btn.pack(side='left')

    def _create_log_card(self, parent):
        """日志卡片"""
        card = CardFrame(parent, title=' Log')
        card.pack(fill='both', expand=True, ipadx=10, ipady=10)

        # 工具栏
        toolbar = tk.Frame(card, bg=COLORS['bg_secondary'])
        toolbar.pack(fill='x', padx=15, pady=(10, 5))

        for text, cmd in [(' Clear', self._clear_log),
                          (' Save', self._save_log),
                          (' Copy', self._copy_log)]:
            btn = tk.Button(toolbar, text=text, bg=COLORS['bg_primary'],
                           fg=COLORS['text_primary'], relief='flat',
                           font=self._font(10), cursor='hand2', command=cmd)
            btn.pack(side='left', padx=(0, 5))

        # 日志文本框
        self.log_text = scrolledtext.ScrolledText(
            card, wrap='word', font=self._font(11),
            bg='#263238', fg='#aed581',  # 深色背景，绿色文字
            insertbackground='white',
            relief='flat', padx=10, pady=10,
            state='disabled'
        )
        self.log_text.pack(fill='both', expand=True, padx=15, pady=(0, 15))

        # 标签颜色
        self.log_text.tag_configure('INFO', foreground='#aed581')
        self.log_text.tag_configure('SUCCESS', foreground='#69f0ae')
        self.log_text.tag_configure('WARNING', foreground='#ffd54f')
        self.log_text.tag_configure('ERROR', foreground='#ff8a80')
        self.log_text.tag_configure('CMD', foreground='#82b1ff')

    def _create_status_bar(self):
        """状态栏"""
        self.status_bar = tk.Frame(self.root, bg=COLORS['bg_header'], height=30)
        self.status_bar.pack(side='bottom', fill='x')
        self.status_bar.pack_propagate(False)

        self.status_label = tk.Label(self.status_bar, text=self.sm.get_text('status_ready'),
                                    bg=COLORS['bg_header'], fg=COLORS['text_light'],
                                    font=self._font(10))
        self.status_label.pack(side='left', padx=15)

    def _log(self, message, level='INFO'):
        """添加日志"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        full_message = '[{}] {}\n'.format(timestamp, message)

        self.log_text.config(state='normal')
        self.log_text.insert('end', full_message, level)
        self.log_text.see('end')
        self.log_text.config(state='disabled')

    def _clear_log(self):
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, 'end')
        self.log_text.config(state='disabled')

    def _save_log(self):
        filename = filedialog.asksaveasfilename(defaultextension='.log')
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.log_text.get(1.0, 'end'))

    def _copy_log(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.log_text.get(1.0, 'end'))

    def _open_temp_folder(self):
        temp_dir = self.sm.get_temp_dir()
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        try:
            os.startfile(temp_dir)
        except:
            pass

    def _open_settings(self):
        """打开设置对话框"""
        SettingsDialog(self.root, self.sm)

    def _update_progress(self, current, total, test_name=''):
        """更新进度显示"""
        if total > 0:
            percentage = (current / total) * 100
            self.total_progress['value'] = percentage
            self.completed_tests = current
            self.total_tests = total

            # Update ETA
            if self.start_time and current > 0:
                elapsed = (datetime.now() - self.start_time).total_seconds()
                avg_time = elapsed / current
                remaining = avg_time * (total - current)
                eta_str = str(timedelta(seconds=int(remaining)))
                self.eta_label.config(text="{}: {}".format(self.sm.get_text('eta'), eta_str))

        if test_name:
            self.current_test_label.config(text=test_name)

    def _start_test(self):
        """开始单个测试"""
        if self.is_running:
            return

        # Get selected scale
        scale_text = self.scale_var.get()
        scale = scale_text.split()[0] if ' ' in scale_text else scale_text

        self.test_queue = [scale]
        self._run_tests()

    def _start_all_scales(self):
        """开始所有规模的测试"""
        if self.is_running:
            return

        self.test_queue = ['tiny', 'small', 'standard', 'medium', 'large']
        self._run_tests()

    def _run_tests(self):
        """运行测试队列"""
        if not self.test_queue:
            self._on_test_complete()
            return

        self.is_running = True
        self.should_stop = False
        self.start_time = datetime.now()
        self.completed_tests = 0

        # Update UI state
        self.run_btn.config(state='disabled')
        self.run_all_btn.config(state='disabled')
        self.stop_btn.config(state='normal')

        # Start test thread
        threading.Thread(target=self._test_worker).start()

    def _test_worker(self):
        """测试工作线程"""
        try:
            total_scales = len(self.test_queue)
            for idx, scale in enumerate(self.test_queue):
                if self.should_stop:
                    break

                self.root.after(0, lambda s=scale, i=idx, t=total_scales:
                    self._log("Starting scale: {} ({}/{})".format(s, i+1, t)))

                self._run_single_scale(scale)

                self.root.after(0, lambda: self._update_progress(idx + 1, total_scales))

        except Exception as e:
            self.root.after(0, lambda: self._log("Error: {}".format(str(e)), "ERROR"))

        finally:
            self.root.after(0, self._on_test_complete)

    def _run_single_scale(self, scale):
        """运行单个规模的测试"""
        py27_path = self.sm.get('python_paths.python27', '')
        py3_path = self.sm.get('python_paths.python3', '')

        if not py27_path or not os.path.exists(py27_path):
            self.root.after(0, lambda: self._log("Python 2.7 not found, skipping", "WARNING"))
        else:
            self._run_python_benchmark(py27_path, scale, 'py2')

        if not py3_path or not os.path.exists(py3_path):
            self.root.after(0, lambda: self._log("Python 3.x not found, skipping", "WARNING"))
        else:
            self._run_python_benchmark(py3_path, scale, 'py3')

            # Open source tests (Python 3 only)
            if self.os_var.get():
                self._run_python_benchmark(py3_path, scale, 'os')

    def _run_python_benchmark(self, python_path, scale, test_type):
        """运行Python基准测试"""
        if self.should_stop:
            return

        cmd = [
            python_path,
            'run_benchmarks.py',
            '--scale', scale,
            '--runs', str(self.sm.get('test_settings.runs', 3)),
            '--warmup', str(self.sm.get('test_settings.warmup', 1))
        ]

        if test_type == 'os':
            cmd.append('--opensource')

        if self.mp_var.get():
            cmd.append('--multiprocess')
            cmd.extend(['--mp-workers', str(self.sm.get('test_settings.mp_workers', 4))])

        test_name = "{} ({})".format(test_type.upper(), scale)
        self.root.after(0, lambda: self.current_test_label.config(text=test_name))
        self.root.after(0, lambda: self._log("Running: {}".format(' '.join(cmd)), "CMD"))

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )

            self.current_process = process

            for line in process.stdout:
                if self.should_stop:
                    process.terminate()
                    break
                line = line.strip()
                if line:
                    self.root.after(0, lambda l=line: self._log(l))

            process.wait()

            if process.returncode == 0:
                self.root.after(0, lambda: self._log("Completed: {}".format(test_name), "SUCCESS"))
            else:
                self.root.after(0, lambda: self._log("Failed: {} (code: {})".format(test_name, process.returncode), "ERROR"))

        except Exception as e:
            self.root.after(0, lambda: self._log("Error running {}: {}".format(test_name, str(e)), "ERROR"))

        finally:
            self.current_process = None

    def _stop_test(self):
        """停止测试"""
        if not self.is_running:
            return

        self.should_stop = True
        self._log("Stopping...", "WARNING")

        if self.current_process:
            try:
                self.current_process.terminate()
            except:
                pass

    def _on_test_complete(self):
        """测试完成回调"""
        self.is_running = False
        self.current_process = None
        self.test_queue = []

        # Reset UI
        self.run_btn.config(state='normal')
        self.run_all_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.total_progress['value'] = 0
        self.current_test_label.config(text=self.sm.get_text('status_ready'))
        self.eta_label.config(text="")

        elapsed = (datetime.now() - self.start_time).total_seconds() if self.start_time else 0
        self._log("All tests completed in {:.1f}s".format(elapsed), "SUCCESS")

    def _toggle_language(self):
        current_lang = self.sm.get('language', 'zh')
        new_lang = 'en' if current_lang == 'zh' else 'zh'
        self.sm.set('language', new_lang)
        self.sm.save_config()
        self._update_language()

    def _on_settings_changed(self):
        """设置变更后的回调"""
        self._update_language()
        self.mp_var.set(self.sm.get('test_settings.enable_multiprocess', False))
        self.os_var.set(self.sm.get('test_settings.enable_opensource', False))

    def _update_language(self):
        self.title_label.config(text=self.sm.get_text('app_title'))
        self.lang_btn.config(text=self.sm.get_text('btn_language'))

        # Update button texts
        self.run_btn.config(text=self.sm.get_text('btn_run'))
        self.run_all_btn.config(text=self.sm.get_text('btn_run_all'))
        self.stop_btn.config(text=self.sm.get_text('btn_stop'))

    def _on_closing(self):
        """窗口关闭处理"""
        if self.is_running:
            if not messagebox.askyesno("Confirm", "Tests are running. Exit anyway?"):
                return
            self._stop_test()

        # Check if remember last settings
        if self.sm.get('ui_settings.remember_last_settings', True):
            # Save current settings
            self.sm.set('test_settings.data_scale', self.scale_var.get().split()[0])
            self.sm.set('test_settings.enable_multiprocess', self.mp_var.get())
            self.sm.set('test_settings.enable_opensource', self.os_var.get())
            self.sm.save_config()

        self.root.destroy()


def main():
    root = tk.Tk()
    app = ModernBenchmarkGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
