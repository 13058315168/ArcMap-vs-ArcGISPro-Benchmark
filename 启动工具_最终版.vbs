' ArcGIS Python Benchmark GUI Launcher - Final Fixed Version
' 最终修复版 - 2026年3月30日

Option Explicit

Dim WshShell, fso, scriptPath, arcgisPython, guiScript, cmd

' 创建对象
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' 获取当前脚本所在目录
scriptPath = fso.GetParentFolderName(WScript.ScriptFullName)

' 定义Python和GUI脚本路径
arcgisPython = "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
guiScript = scriptPath & "\benchmark_gui.py"

' 检查文件是否存在
Dim pythonPath
If fso.FileExists(arcgisPython) Then
    pythonPath = arcgisPython
    MsgBox "将使用 ArcGIS Pro Python 运行", 64, "提示"
Else
    pythonPath = "python"
    MsgBox "将使用系统 Python 运行", 64, "提示"
End If

' 检查GUI脚本是否存在
If Not fso.FileExists(guiScript) Then
    MsgBox "错误：找不到 benchmark_gui.py 文件！" & vbCrLf & "路径：" & guiScript, 16, "错误"
    WScript.Quit 1
End If

' 构建命令
cmd = Chr(34) & pythonPath & Chr(34) & " " & Chr(34) & guiScript & Chr(34)

' 运行命令（显示窗口以便调试）
Dim result
result = WshShell.Run(cmd, 1, False)

If result <> 0 Then
    MsgBox "启动失败！错误码：" & result, 16, "错误"
End If

' 清理对象
Set WshShell = Nothing
Set fso = Nothing