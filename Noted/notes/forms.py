from django.forms import ModelForm
from .models import Note
from django import forms


class NoteForm(ModelForm):
    # post_text = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 30}), label='Текст объявления:')

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