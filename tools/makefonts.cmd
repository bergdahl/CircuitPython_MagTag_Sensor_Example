SET DPI=112
SET FONT=Exo-SemiBold
SET SIZE=18
otf2bdf3\otf2bdf -v -r %DPI% -p %SIZE% -o %FONT%-%SIZE%.bdf -l "45 46 48_57 77 98 109 112" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src

SET SIZE=36
otf2bdf3\otf2bdf -v -r %DPI% -p %SIZE% -o %FONT%-%SIZE%.bdf -l "37 48_57 77 80 97 104" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src

SET FONT=Exo-Bold
SET SIZE=72
otf2bdf3\otf2bdf -v -r %DPI% -p 72 -o %FONT%-%SIZE%.bdf -l "46 48_57 77 186" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src
