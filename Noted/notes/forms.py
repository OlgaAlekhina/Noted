from django.forms import ModelForm
from .models import Task, UserProfile
from django import forms
from django.contrib.auth.models import User


# форма для добавления задачи
class TaskForm(ModelForm):
    task_title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}))
    task_date = forms.DateField(label='Когда сделать:', widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-widget'}))
    task_priority = forms.BooleanField(label='Сделать приоритетной', required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'check-priority'}))

    class Meta:
        model = Task
        fields = ['task_title', 'task_date', 'task_priority']


# форма для редактирования данных пользователя
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


# форма для редактирования аватара
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = UserProfile
        fields = ['avatar', ]

