Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "D:\path\to\batfile.bat" & Chr(34), 0
Set WshShell = Nothing