# 制作EXE可执行文件

## 方法一：使用PyInstaller（推荐）

### 步骤1：安装依赖
```bash
pip install pyinstaller pillow
```

### 步骤2：准备图标
将您的图片转换为ico格式：
```bash
python convert_icon.py your_image.png
```

或者直接放在 `resources/icon.ico`

### 步骤3：创建EXE
```bash
python create_exe.py
```

或者在命令行直接运行：
```bash
pyinstaller --name=ArcGIS_Benchmark --windowed --onefile --icon=resources/icon.ico --add-data=config;config --add-data=utils;utils --add-data=benchmarks;benchmarks --add-data=data;data benchmark_gui_modern.py
```

### 步骤4：创建桌面快捷方式
运行生成的 `create_desktop_shortcut.vbs`

## 方法二：使用auto-py-to-exe（图形界面）

```bash
pip install auto-py-to-exe
auto-py-to-exe
```

然后在浏览器中配置：
- Script Location: `benchmark_gui_modern.py`
- Onefile: `One File`
- Console Window: `Window Based`
- Icon: 选择 `resources/icon.ico`
- Additional Files: 添加 `config`, `utils`, `benchmarks`, `data` 文件夹

## 打包后的文件

打包完成后，文件结构：
```
dist/
├── ArcGIS_Benchmark.exe    # 主程序
└── ... (依赖文件)
```

## 注意事项

1. **杀毒软件误报**：某些杀毒软件可能会误报PyInstaller打包的exe，请添加信任
2. **文件大小**：单文件exe会比较大（约50-100MB），因为包含了Python解释器
3. **首次运行**：首次运行可能会稍慢，因为需要解压临时文件

## 分发建议

1. 将 `resources` 文件夹和exe一起分发
2. 或者使用安装程序（如Inno Setup）创建安装包
3. 可以创建绿色版压缩包，解压即用
