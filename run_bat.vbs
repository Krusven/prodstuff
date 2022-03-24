Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "D:\Software Dev\prodstuff\run_checker.bat" & Chr(34), 0
Set WshShell = Nothing