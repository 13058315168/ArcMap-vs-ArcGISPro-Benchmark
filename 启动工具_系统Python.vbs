Set WShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")
ScriptDir = FSO.GetParentFolderName(WScript.ScriptFullName)
Cmd = "pythonw """ & ScriptDir & "\benchmark_gui_modern.py"""
WShell.Run Cmd, 0, False
Set WShell = Nothing
Set FSO = Nothing
