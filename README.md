# 1. Used environmental variables

| Variable name       | Default value | Notes                                 |
| ------------------- | ------------- | ------------------------------------- |
| SECRET_KEY          | -             | Django secret key                     |
| DJANGO_DEBUG        | -             | Empty string for prod or True for dev |
| ALLOWED_HOSTS       | -             | List of allowed hosts (CORS)          |
| DB_HOST             | -             | Database Host                         |
| DB_PORT             | -             | Database Port                         |
| DB_LOGIN            | -             | Database Username                     |
| DB_PASS             | -             | Database user password                |
| DB_NAME             | -             | Database name                         |
| EMAIL_HOST_USER     | -             |                                       |
| EMAIL_HOST_PASSWORD | -             |                                       |

# 2. Как запустить проект на своем локальном сервере через IDE PyCharm:
clone this repo
```
git clone git@gitlab.com:pineapple-practice/noted/Noted.git
```
create virtual env
```
python -m venv venv
```
activate created venv
```
venv\scripts\activate
```
install requirements
```
pip install -r requirements.txt
```
run server
```
python manage.py runserver
```

# 3. Available pages

- signup (для регистрации пользователя)

- login (для входа зарегистрированного пользователя)

- logout (для выхода пользователя)

- reset_password (для восстановления пароля по email)

- /main (главная страница)

- /main/date (главная страница с задачами на конкретную дату, где date - дата в формате dd-mm-yyyy)

- /main/notes (страница всех заметок с формой добавления новой)

- /main/tasks (страница всех задач с формой добавления новой)

- /main/notes/id (страница конкретной заметки, где id - целое число)

- /main/notes/edit/id (страница для редактирования заметки, где id - целое число)

- /main/settings (страница для редактирования персональных данных)

- /main/trash (страница с удаленными заметками и задачами)

- /main/search?q=... (страница с результатами поиска)
