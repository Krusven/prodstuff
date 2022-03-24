Set WshShell = CreateObject("WScript.Shell") 'starts a new windows shell process
WshShell.Run chr(34) & "D:\path\to\batfile.bat" & Chr(34), 0 'runs command and chr(34) tells command that there is string command in quotes
Set WshShell = Nothing 'Do not display a window