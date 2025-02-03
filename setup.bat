@echo off

python -m venv .venv
echo .venv created


call .venv\Scripts\activate.bat
echo .venv activated.

python.exe -m pip install --upgrade pip
echo pip upgrade -- done

echo Installing dependencies...
pip install -r requirements.txt
echo requirements installed

cd school_project
python manage.py makemigrations
python manage.py migrate


echo Creating .gitignore file...

echo .venv/ > .gitignore
:: Create .gitignore and add the .venv directory
echo .gitignore file created.

echo.
echo Setup complete! Now you can run the server using run_server.bat

pause
