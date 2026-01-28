@ECHO OFF
@SET PYTHONIOENCODING=utf-8
@SET PYTHONUTF8=1
@FOR /F "tokens=2 delims=:." %%A in ('chcp') do for %%B in (%%A) do set "_CONDA_OLD_CHCP=%%B"
@chcp 65001 > NUL
@CALL "C:\Users\PRATIK RAJ\anaconda3\condabin\conda.bat" activate "c:\Users\PRATIK RAJ\OneDrive\Desktop\Customer Retention System\.conda"
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@"c:\Users\PRATIK RAJ\OneDrive\Desktop\Customer Retention System\.conda\python.exe" -Wi -m compileall -q -l -i C:\Users\PRATIK~1\AppData\Local\Temp\tmppu3z_1yq -j 0
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@chcp %_CONDA_OLD_CHCP%>NUL
