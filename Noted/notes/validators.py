from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from string import punctuation, whitespace


# проверка email на уникальность в настройках пользователя
class EmailValidator:
    def __init__(self, user):
        self.user = user

    def __call__(self, email):
        if User.objects.filter(email=email).exists():
            user_mail = User.objects.filter(email=email).first()
            if user_mail != self.user:
                raise ValidationError(_("Пользователь с таким email уже зарегистрирован"))


# валидатор длины пароля в форме регистрации
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

valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
INVALID_CHARS = set(punctuation + whitespace) - valid_chars

# валидатор спецсимволов пароля в форме регистрации
class CharacterValidator:
    def __init__(self):
        pass

    def validate(self, password, user=None):
        for char in INVALID_CHARS:
            if char in password:
                raise ValidationError(
                    _("Пароль может содержать только буквы и символы '!@#$^&()_.-' без пробелов"),
                    code="password_invalid_chars",
                    params={},
                )

    def get_help_text(self):
        return _(
            "Your password must contain only letters and special characters '!@#$^&()_.-' without spaces."
        )


# валидация пароля в формах
def validate_password(password):
    valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    invalid_chars = set(punctuation + whitespace) - valid_chars
    for char in invalid_chars:
        if char in password:
            return False