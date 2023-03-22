from django.contrib import admin
from .models import Note, Task, UserProfile


# регистрация моделей в админке
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(UserProfile)
