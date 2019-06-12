@Echo off
cd C:/MyProjects/hi

Set root=C:\MyProjects
Set WshShell = WScript.CreateObject("WScript.Shell")

:Create()
cd %root%
python C:\MyProjects\utsavcode\commands.py %1
EXIT /B 0