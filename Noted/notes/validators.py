from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# проверка email на уникальность в настройках пользователя
class EmailValidator:
    def __init__(self, user):
        self.user = user

    def __call__(self, email):
        if User.objects.filter(email=email).exists():
            user_mail = User.objects.filter(email=email).first()
            if user_mail != self.user:
                raise ValidationError("Пользователь с таким email уже зарегистрирован")


# проверка размера закачанной аватарки
def avatar_validator(file):
    limit = 512000
    if file.size > limit:
        raise ValidationError('Размер файла не должен превышать 500 Кб.')