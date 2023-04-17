from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# проверка email на уникальность
class EmailValidator:
    def __init__(self, user):
        self.user = user

    def __call__(self, email):
        if User.objects.filter(email=email).exists():
            user_mail = User.objects.filter(email=email).first()
            if user_mail != self.user:
                raise ValidationError("Пользователь с таким email уже зарегистрирован")