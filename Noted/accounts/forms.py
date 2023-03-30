from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


# форма для регистрации пользователя
class NewUserForm(UserCreationForm):
	username = forms.CharField(label='', widget=forms.TextInput (attrs={'class': 'form-control my-inp', 'placeholder': 'Имя'}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control my-inp', 'placeholder': 'E-Mail'}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control my-inp', 'placeholder': 'Пароль'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control my-inp', 'placeholder': 'Повторите пароль'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

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


