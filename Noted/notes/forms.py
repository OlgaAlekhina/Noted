from django.forms import ModelForm
from .models import Task
from django import forms


# форма для добавления задачи
class TaskForm(ModelForm):
    task_title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст'}))
    task_time = forms.DateField(label='Когда сделать:', widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'date-widget'}))
    task_priority = forms.BooleanField(label='Сделать приоритетной', required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'check-priority'}))

    class Meta:
        model = Task
        fields = ['task_title', 'task_time', 'task_priority']

