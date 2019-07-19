@echo off
title Web Server Installer v1.0
color 0b

goto installer

:installer
echo ========================================================================================================================
set /p installed=Have you already installed the server? [Y/N]
goto installFlask

:installFlask
pip install flask
goto installDatabase

:installDatabase
pip install flask-sqlalchemy mysql-python
goto webserver

:webserver
echo ========================================================================================================================
set /p flask_app_name=Enter name of the webserver python script: 
echo ========================================================================================================================
set /p flask_app_location=Enter location of the webserver python script: 
goto setFlaskApp

:setFlaskApp
set FLASK_APP=%flask_app_location%\%flask_app_name%
goto ending

:ending
echo ========================================================================================================================
echo .
echo 			Everything should be installed, to start the server just type "flask run"
echo .
echo ========================================================================================================================
pause 
exit


if %installed%==Y
	goto ending
elseif %installed%==N
	goto installFlask
else
	goto installer
