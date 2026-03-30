Set WShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")
ScriptDir = FSO.GetParentFolderName(WScript.ScriptFullName)
VenvPython = ScriptDir & "\venv\Scripts\pythonw.exe"
If FSO.FileExists(VenvPython) Then
    PythonPath = VenvPython
Else
    PythonPath = "pythonw"
End If
Cmd = "\"" & PythonPath & "\" \"" & ScriptDir & "\benchmark_gui_modern.py\""
WShell.Run Cmd, 0, False
