from django.forms import ModelForm
from .models import Note
from django import forms


# форма для добавления задачи
class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['note_title', 'note_text', 'note_author', 'note_priority', 'note_time', 'tags']

        widgets = {
            'note_author': forms.HiddenInput(),
        }

        labels = {
            'note_title': 'Заголовок',
            'note_text': 'Детали',
            'note_priority': 'Приоритет',
            'note_time': 'Когда сделать (yyyy-mm-dd)',
            'tags': 'Тэги',
        }