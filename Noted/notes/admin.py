from django.contrib import admin
from .models import Note, Tag


# регистрация моделей в админке
admin.site.register(Note)
admin.site.register(Tag)
