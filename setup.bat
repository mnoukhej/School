@echo off
python -m venv venv
call venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
cd school_project
python manage.py makemigrations
python manage.py migrate
echo.
echo Setup complete! Now you can run the server using run_server.bat
pause
