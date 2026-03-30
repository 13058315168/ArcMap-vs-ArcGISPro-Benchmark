Set WShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")
ScriptDir = FSO.GetParentFolderName(WScript.ScriptFullName)
DesktopPath = WShell.SpecialFolders("Desktop")
Set Shortcut = WShell.CreateShortcut(DesktopPath & "\ArcGIS Benchmark.lnk")
Shortcut.TargetPath = "wscript.exe"
Shortcut.Arguments = """" & ScriptDir & "\Æô¶¯¹¤¾ß.vbs"""
Shortcut.WorkingDirectory = ScriptDir
Shortcut.Description = "ArcGIS Python Performance Benchmark Tool"
Shortcut.IconLocation = ScriptDir & "\resources\icon.ico"
Shortcut.Save
MsgBox "Desktop shortcut created!", 64, "Done"
Set WShell = Nothing
Set FSO = Nothing
