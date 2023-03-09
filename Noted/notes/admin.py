from django.contrib import admin
from .models import Note, Task


# регистрация моделей в админке
admin.site.register(Note)
admin.site.register(Task)
