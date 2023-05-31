from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


# проверка email на уникальность в настройках пользователя
class EmailValidator:
    def __init__(self, user):
        self.user = user

    def __call__(self, email):
        if User.objects.filter(email=email).exists():
            user_mail = User.objects.filter(email=email).first()
            if user_mail != self.user:
                raise ValidationError(_("Пользователь с таким email уже зарегистрирован"))


# валидатор пароля в форме регистрации
class LengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Пароль должен содержать не менее 8 символов"),
                code="password_too_short",
                params={"min_length": self.min_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_length)d characters."
            % {"min_length": self.min_length}
        )