from django.forms import ModelForm
from .models import Task, UserProfile
from django import forms
from django.contrib.auth.models import User
from .validators import EmailValidator
from django.utils.translation import gettext_lazy as _


# форма для добавления задачи
class TaskForm(ModelForm):
    task_title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Добавьте название...')}))
    task_date = forms.DateField(label='', widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-widget',
                                                'style': 'border-radius: 0.375rem; padding: 4px 13px; font-size: 15px; background: rgba(255, 255, 255, 0.8);'}))
    # task_priority = forms.BooleanField(label='Приоритет', required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'check-priority'}))
    task_time = forms.TimeField(label='', required=False, widget=forms.widgets.TimeInput(attrs={'type': 'time', 'class': 'time-widget',
                                                                                'style': 'border-radius: 0.375rem; border: none; padding: 3px 12px; background: rgba(255, 255, 255, 0.8);'}))
    # task_timestamp = forms.CharField(widget=forms.HiddenInput(attrs={}))

    class Meta:
        model = Task
        fields = ['task_title', 'task_date', 'task_time', 'task_priority']


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
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control',  'onchange': 'fileinputChange()', 'style': 'opacity: 0; height: 0;', 'id': 'note-file'}))

    class Meta:
        model = UserProfile
        fields = ['avatar', 'name']

