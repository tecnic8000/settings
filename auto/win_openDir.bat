@echo off
setlocal

rem List of directories
set dirs="D:\REPO\sys" "D:\REPO\artSupp1" "D:\REPO\t8000"

rem Loop through each directory and open it
for %%d in (%dirs%) do (
    if exist %%d (
        start "" explorer %%d
    ) else (
        echo Directory not found: %%d
    )
)

endlocal