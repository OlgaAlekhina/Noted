Для деплоя проекта на сервер необходимо добавить файл .env со следующими переменными окружения:
(некоторые значения пришлю в частном порядке)

SECRET_KEY (django secret key)
DJANGO_DEBUG=   (пустая строка для продакшен или True для разработки)
ALLOWED_HOSTS
Настройки базы данных Postgres:
DB_HOST
DB_PORT
DB_LOGIN
DB_PASS
DB_NAME
Настройки почты:
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD


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

/main/date      # главная страница с задачами на конкретную дату, где date - дата в формате dd-mm-yyyy

/main/notes       # страница всех заметок с формой добавления новой

/main/tasks       # страница всех задач с формой добавления новой

/main/notes/id     # страница конкретной заметки, где id - целое число

/main/notes/edit/id   # страница для редактирования заметки, где id - целое число

/main/settings     # страница для редактирования персональных данных

/main/trash       # страница с удаленными заметками и задачами

/main/search?q=...      # страница с результатами поиска






