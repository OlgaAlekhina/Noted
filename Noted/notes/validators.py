from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# проверка email на уникальность
def validate_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError("Пользователь с таким email уже зарегистрирован")