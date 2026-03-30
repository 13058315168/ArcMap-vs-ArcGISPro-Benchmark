' ArcGIS Python Benchmark GUI Launcher - Fixed Version
' 修复版启动工具

Dim WshShell, fso, scriptPath, cmd
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get script directory
scriptPath = fso.GetParentFolderName(WScript.ScriptFullName)

' Check if ArcGIS Pro Python exists
Dim arcgisPython
arcgisPython = "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

If fso.FileExists(arcgisPython) Then
    ' Use ArcGIS Pro Python
    cmd = Chr(34) & arcgisPython & Chr(34) & " " & Chr(34) & scriptPath & "\benchmark_gui.py" & Chr(34)
Else
    ' Use system Python
    cmd = "python " & Chr(34) & scriptPath & "\benchmark_gui.py" & Chr(34)
End If

' Show command window for debugging (1 = show, 0 = hide)
WshShell.Run cmd, 1, False

Set WshShell = Nothing
Set fso = Nothing