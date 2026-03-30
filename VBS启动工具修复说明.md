# VBS启动工具修复说明

## 问题分析

"启动工具.vbs"无法打开的原因可能有：

1. **Windows Script Host被禁用** - 需要检查注册表设置
2. **VBS脚本编码问题** - 需要确保使用正确的编码
3. **路径问题** - Python或GUI脚本路径不正确
4. **权限问题** - 需要管理员权限运行

## 解决方案

### 方法1：使用批处理文件（推荐）

我们创建了 `启动工具_批处理版.bat`，这是一个更可靠的替代方案：

```batch
@echo off
chcp 65001 >nul
REM 自动检测Python环境并启动GUI
```

**使用方法**：双击运行 `启动工具_批处理版.bat`

### 方法2：使用修复版VBS

创建了多个修复版本的VBS脚本：

1. `启动工具_修复版.vbs` - 基础修复版本
2. `启动工具_最终版.vbs` - 完整修复版本，包含错误提示

**使用方法**：双击运行对应的.vbs文件

### 方法3：直接运行Python

如果上述方法都不行，可以直接运行Python：

```bash
python benchmark_gui.py
```

## 测试结果

- ✅ GUI脚本本身可以正常启动
- ✅ Python环境检测正常
- ✅ 批处理启动器工作正常
- ✅ VBS脚本已修复常见问题

## 注意事项

1. 如果提示"Windows Script Host被禁用"，需要：
   - 按Win+R，输入`regedit`打开注册表
   - 找到`HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings`
   - 将`Enabled`值改为1

2. 如果仍然无法运行，请以管理员身份运行CMD，执行：
   ```
   reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows Script Host\Settings" /v Enabled /f
   ```

3. 建议优先使用批处理版本，它更稳定且易于调试。