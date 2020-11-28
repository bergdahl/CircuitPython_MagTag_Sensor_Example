SET DPI=112
SET FONT=Exo-SemiBold
SET SIZE=6
otf2bdf3\otf2bdf -v -r %DPI% -p %SIZE% -o %FONT%-%SIZE%.bdf -l "32_126 161_255" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src

SET FONT=Exo-SemiBold
SET SIZE=12
otf2bdf3\otf2bdf -v -r %DPI% -p %SIZE% -o %FONT%-%SIZE%.bdf -l "32_126 161_255" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src

SET SIZE=18
otf2bdf3\otf2bdf -v -r %DPI% -p %SIZE% -o %FONT%-%SIZE%.bdf -l "32_126 161_255" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src

SET FONT=Exo-Bold
SET SIZE=42
otf2bdf3\otf2bdf -v -r %DPI% -p %SIZE% -o %FONT%-%SIZE%.bdf -l "32_126 161_255" %FONT%.ttf
move /y %FONT%-%SIZE%.bdf ..\src
