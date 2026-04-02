Set WShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")
ScriptDir = FSO.GetParentFolderName(WScript.ScriptFullName)
DesktopPath = WShell.SpecialFolders("Desktop")
Set Shortcut = WShell.CreateShortcut(DesktopPath & "\ArcGIS Benchmark.lnk")
Shortcut.TargetPath = "wscript.exe"
Shortcut.Arguments = """" & ScriptDir & "\启动工具.vbs"""
Shortcut.WorkingDirectory = ScriptDir
Shortcut.Description = "ArcGIS Python2、3 与开源库性能对比测试工具"
Shortcut.IconLocation = ScriptDir & "\resources\icon.ico"
Shortcut.Save
MsgBox "Desktop shortcut created!", 64, "Done"
Set WShell = Nothing
Set FSO = Nothing


