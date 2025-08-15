@echo off
echo ========================================
echo UI Test Automation - Dated Reporting
echo ========================================
echo.

REM Get current date and time
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "datestamp=%YYYY%-%MM%-%DD%"
set "timestamp=%YYYY%%MM%%DD%_%HH%%Min%%Sec%"

echo Test Execution Details:
echo Date: %datestamp%
echo Time: %HH%:%Min%:%Sec%
echo.

REM Create dated report directory
set "REPORT_DIR=reports\%datestamp%\%timestamp%"
if not exist "%REPORT_DIR%" mkdir "%REPORT_DIR%"

echo Creating report directory: %REPORT_DIR%
echo.

REM Run tests with dated reporting
python run_tests.py %*

echo.
echo ========================================
echo Test execution completed!
echo Report location: %REPORT_DIR%
echo ========================================
pause 