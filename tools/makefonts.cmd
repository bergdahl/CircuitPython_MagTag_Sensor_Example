otf2bdf3\otf2bdf -v -p 18 -o ExoSemiBold-18.bdf -l "45 46 48_57 77 98 109 112" Exo-SemiBold.ttf
otf2bdf3\otf2bdf -v -p 36 -o ExoSemiBold-36.bdf -l "37 48_57 77 80 97 104" Exo-SemiBold.ttf
otf2bdf3\otf2bdf -v -p 72 -o ExoBold-72.bdf -l "46 48_57 77 186" Exo-Bold.ttf

copy /y ExoSemiBold-18.bdf ..\src
copy /y ExoSemiBold-36.bdf ..\src
copy /y ExoBold-72.bdf ..\src
