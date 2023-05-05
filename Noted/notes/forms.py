from django.forms import ModelForm
from .models import Task, UserProfile
from django import forms
from django.contrib.auth.models import User
from .validators import EmailValidator, avatar_validator


# форма для добавления задачи
class TaskForm(ModelForm):
    task_title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Добавьте название...'}))
    task_date = forms.DateField(label='', widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-widget',
                                                'style': 'border: 1px solid #ced4da; border-radius: 0.375rem; padding: 3px 8px; text-transform: uppercase;'}))
    task_priority = forms.BooleanField(label='Приоритет', required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'check-priority'}))

    class Meta:
        model = Task
        fields = ['task_title', 'task_date', 'task_priority']


# форма для редактирования данных пользователя
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('instance')
        self.fields['email'].validators.append(EmailValidator(user))

    class Meta:
        model = User
        fields = ['email', ]


# форма для редактирования аватара
class UpdateProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = UserProfile
        fields = ['avatar', 'name']

