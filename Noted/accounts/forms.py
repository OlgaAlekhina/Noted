from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm):
	username = forms.CharField(label='Введите свой ник', min_length=4, max_length=150)
	email = forms.EmailField(label='Введите email')
	password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise ValidationError("Этот ник занят")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise ValidationError("Пользователь с таким email уже зарегистрирован")
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Пароли не совпадают")

		return password2

	def save(self, commit=True):
		user = User.objects.create_user(
			self.cleaned_data['username'],
			self.cleaned_data['email'],
			self.cleaned_data['password1']
		)
		return user