@echo off
setlocal

rem List of directories
set dirs="C:\path\to\directory1" "C:\path\to\directory2" "C:\path\to\directory3"

rem Loop through each directory and open it
for %%d in (%dirs%) do (
    if exist %%d (
        start "" explorer %%d
    ) else (
        echo Directory not found: %%d
    )
)

endlocal