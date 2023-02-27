from django.contrib import admin
from .models import Note, Tag, Task


# регистрация моделей в админке
admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Task)
