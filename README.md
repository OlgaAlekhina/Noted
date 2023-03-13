Как запустить проект на своем локальном сервере через IDE PyCharm:

Git -> clone -> https://github.com/OlgaAlekhina/Noted # скачать репозиторий с гитхаба на свой комп 

python -m venv venv # создать виртуальную среду 

venv\scripts\activate # активировать виртуальную среду (нужно делать из той папки, где лежит папка venv) 

pip install -r requirements.txt # установить зависимости для проекта, которые указаны в файле requirements.txt

python manage.py runserver # запустить сервер

Страницы:

signin      # для регистрации пользователя

login       # для входа зарегистрированного пользователя

logout      # для выхода пользователя

reset_password # для восстановления пароля по email

/main             # главная страница

/main/notes       # страница всех заметок

/main/notes/id     # страница конкретной заметки

/main/notes/edit/id   # страница для редактирования заметки

/main/date      # главная страница с задачами на конкретную дату





