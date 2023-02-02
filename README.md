Как запустить проект на своем локальном сервере через IDE PyCharm:

Git -> clone -> https://github.com/OlgaAlekhina/Noted # скачать репозиторий с гитхаба на свой комп 

python -m venv venv # создать виртуальную среду 

venv\scripts\activate # активировать виртуальную среду (нужно делать из той папки, где лежит папка venv) 

pip install -r requirements.txt # установить зависимости для проекта, которые указаны в файле requirements.txt

python manage.py runserver # запустить сервер

Страницы:

/main/signin      # для регистрации пользователя

/main/login       # для входа зарегистрированного пользователя

/main/logout      # для выхода пользователя

/main/reset_password # для восстановления пароля по email

/main             # главная страница

/main/id        # страница конкретной задачи

/main/add         # страница для добавления новой задачи

/main/edit/id   # страница для редактирования задачи

/main/delete/id # страница для удаления задачи

/main/date      # список всех задач на конкретную дату

/main/next/date # страница с задачами на следующую неделю

/main/previous/date # страница с задачами на предыдущую неделю

Экраны, они же страницы:

1. Экран 
Данный экран предназначен для авторизации, регистрации и восстановления пароля

Что содержит:
Форму регистрации
Форму авторизации 
Форму восстановления пароля

2. Экран
Такой экран встречает пользователя после авторизации

Что может содержать:
Страницы ежедневника (они же даты)
Заметки на сегодняшнюю дату либо неделю
Фильтр дат и поиск для фильтрации вывода страниц (может быть и хэштеги...)
Кнопку "добавить быструю заметку"
Возможно какую-либо ещё ценную информацию для пользователя. 

3. Экран
Такой экран пользователь получает при работе с фильтрами на экране 2. То есть, на данном экране будут выведены заметки либо страницы, соответствующие данному фильтру

Что может содержать:
Заметки
Страницы ежедневника (они же даты)
Фильтр дат и поиск для фильтрации вывода страниц (может быть и хэштеги...)
Кнопку "добавить быструю заметку"
Возможно какую-либо ещё ценную информацию для пользователя. 


4. Экран страницы, она же дата. 
На экран страницы мы переходим из экрана Главная, когда выбираем одну из заметок

На данном экране мы показываем структуру заметки

Что может содержать:
Текстовое поле для ввода заметки (возможно поле тайтл и дескрипшн должны быть раздельными)
Отображение даты
Кнопка удалить
Кнопка править
Кнопка отправить по e-mail


