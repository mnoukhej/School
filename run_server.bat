@echo off
call venv\Scripts\activate.bat
cd school_project
python manage.py runserver
pause
