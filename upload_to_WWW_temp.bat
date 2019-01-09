@echo off

REM places starting with !! should be filled with user specific data

"D:\...\Blog\WinSCP-5.13.4-Portable\WinSCP.com" ^
  /log="D:\WinSCP.log" /ini=nul ^
  /command ^

    "open sftp://!!username@!!hosting.server.org/ -hostkey=""ssh-ed25519 256 !!g............................ig="" -rawsettings FSProtocol=2" ^
    "cd /home/!!domain_name_user/domains/!!URL_of_targe_site/public_html" ^
	"rm *" ^
	"lcd ""D:\...\output""" ^
    "cd /home/!!domain_name_user/domains/!!URL_of_targe_site/public_html" ^
    "put *" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

exit /b %WINSCP_RESULT%

