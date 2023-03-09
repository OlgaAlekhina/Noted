from django.forms import ModelForm
from .models import Note
from django import forms


# форма для добавления задачи
class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['note_title', 'note_text', 'note_author', 'note_time']

        widgets = {
            'note_author': forms.HiddenInput(),
            'note_time': forms.HiddenInput(),
        }

        labels = {
            'note_title': 'Название',
            'note_text': 'Наберите текст...',
        }