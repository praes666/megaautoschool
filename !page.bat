@ECHO OFF
call "venv\Scripts\activate"
start http://127.0.0.1:8000/mypage
python manage.py runserver